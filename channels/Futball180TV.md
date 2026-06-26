<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn5.telesco.pe/file/sP7IuOnoEyfCSWWMsQho6qEvmTbDcEeMrfmZwXgQJSs_rOi7UgDa6MgtI-aqFPlMFcmOIVdyjf7EFfVJMZ3H_-xSkjEwIoNpoqKSL-ccuWUSSNnJgfitez3v1K4RP0XOKB4qMmwn1wTJak6wrMXzcBpNrgC6sNKky-9kY5b4qKVwqKm09TNFCziG9xpaF27MhLZKcwd--1UOqBTeMawzoZ4l9p0d1hT8_wjBb3JExjY0UvIsyR6AD9TG1NDWLBovrR0N1jtcH_mDAI_wpR4WgykxR7Fiqu1RU1DsxC8aguQi-Xw35qMf2dlioaFqt7uNEny0ITcsuDVvvWMe5SWbHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 696K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 06:03:55</div>
<hr>

<div class="tg-post" id="msg-95985">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai9W8XEhBUV_SBeMMMZHY7JO0wUwjyNOrK9tyEUPqxGF3ZAKScmn3JynvREyNDV_FHx6D1phgMerRl11jd-UgqrzdQd8U4tWuGmK7SnftPgz-VL0KNwwqB1UvvfGMBm1TN274WEmFFakPRu4c45Pw49oLpC30U4DP1Q7ZAm4HD3bD6gHtPn-1GOcPTuhmSHbKzgJ0vCH1N93Rob4xdiGuy8DSRh4CXrlxK0lQiWm7SSF9fkSGKeYqyXVr41dCu1HqTb39ax9tQhftW09zrU1h_A1dzmn1cMlyXKzaNMWPtI8-m3FLxUB-OwYRX5Suf-iblX6excZ8n-xFXyc9F5d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایلر دردن در حال تماشای بازی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 843 · <a href="https://t.me/Futball180TV/95985" target="_blank">📅 05:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95984">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba51004b9.mp4?token=i6_ctgNSTqcZR4lS7VXpBIClDvYxvRQkraWhXXy8oJcUHio1Ud8IkXmA2_BFkhNR648DHGPFiOKUmFwemTNhHkPp2SfQcXA-IlvTzrece3C4IMLCDwKIBsJ4EZ52v2ZJLoTM-6GfKDZxZIDoq3_BBd37h1xVjRlMf6bvoGPYFPivoOfcOJNTC3nD19q8XqcT17DYEc2ddWqH7uzv8wkD51iaJl1iTH_4-njwg2xOFn0RpjU9sEf5FlvdCG_kzQMdQZCzSODkYEwV8POvLI1W0d5mNDTyxRY17CwS5OZUvpISitJO80WqVivMoPKWpK-5vGrG4rFarPQGKrK42EfTbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba51004b9.mp4?token=i6_ctgNSTqcZR4lS7VXpBIClDvYxvRQkraWhXXy8oJcUHio1Ud8IkXmA2_BFkhNR648DHGPFiOKUmFwemTNhHkPp2SfQcXA-IlvTzrece3C4IMLCDwKIBsJ4EZ52v2ZJLoTM-6GfKDZxZIDoq3_BBd37h1xVjRlMf6bvoGPYFPivoOfcOJNTC3nD19q8XqcT17DYEc2ddWqH7uzv8wkD51iaJl1iTH_4-njwg2xOFn0RpjU9sEf5FlvdCG_kzQMdQZCzSODkYEwV8POvLI1W0d5mNDTyxRY17CwS5OZUvpISitJO80WqVivMoPKWpK-5vGrG4rFarPQGKrK42EfTbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل اول آمریکا به ترکیه توسط تراستی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/95984" target="_blank">📅 05:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95983">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72cd71076b.mp4?token=jyOVnuCm4hsFg4H-r4rOQFGEynPKyPICywP5-ALAIt-6JJT_bwXXLuZoQfGMc0bT6ckMcpAh--WkBAzSHHimVbMlnttNnrLHsPOoTuNQlfWenLv_UFBMAv7x-ZN_2YcdTpm-CsAZP25WjPr08JBKbb5D_Wd0zk8Se4F_n8TJRW39Xt6w1knx69APPBDY0v1-DJFPkK0bKKyrRZ0GPn2-6urLmUu3_LfUbDoFhv8iwCJn4H4rfYxLN-lCkgzP56vdkik-nPyttK6yneS6T7Jn2rVtqcE4w-J1Yg8kBfbhzmFhlfs8v4HdXok5qWS5oY21me-nFRspNLZUuQKYdNyp2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72cd71076b.mp4?token=jyOVnuCm4hsFg4H-r4rOQFGEynPKyPICywP5-ALAIt-6JJT_bwXXLuZoQfGMc0bT6ckMcpAh--WkBAzSHHimVbMlnttNnrLHsPOoTuNQlfWenLv_UFBMAv7x-ZN_2YcdTpm-CsAZP25WjPr08JBKbb5D_Wd0zk8Se4F_n8TJRW39Xt6w1knx69APPBDY0v1-DJFPkK0bKKyrRZ0GPn2-6urLmUu3_LfUbDoFhv8iwCJn4H4rfYxLN-lCkgzP56vdkik-nPyttK6yneS6T7Jn2rVtqcE4w-J1Yg8kBfbhzmFhlfs8v4HdXok5qWS5oY21me-nFRspNLZUuQKYdNyp2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل اول آمریکا به ترکیه توسط تراستی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/Futball180TV/95983" target="_blank">📅 05:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95982">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPuA71DilijM7caK2jMeZX_eybS_ceiSV9PGKGBgC2C84-7YiwcXzasI7DQfOmEa_krC7ja8iJ8ZzlNt2yUypFbX-xY3NDbScNZrBsxHvLlNLOnvgt0m9oT2CdpEPLdJiOya_vqN2e3ptWD_t7xIeGrP408ExaYOOX0eUZRvUzZtDb63nuttFOUfFsFDG57GSuA9CzIArosSLxqoOTMH8GKrjjG7-2EF-To5lOJg13i3Ze3XH1Q1SyX5xDMfEW9xxGRwmkLZ7BxR7eVDMW1NBETJTdoN4vxNfnxtXQcVHgqsyeWi2Y1S720fTPoq3GMJ0IdY9qfSOqJ3xvMrxTNcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
جدول فعلی برترین تیم‌های سوم مرحله گروهی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/95982" target="_blank">📅 05:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95981">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0ZoaUZEOppC9RqnFr4uQHTIUUOgW0zG4AczsNVV_Tr1bsMUMTPr-390SHLYRjfAOmATi4WxawFbPEWovPgs09AYGVj9HPVb09kVO9NLn-xqAkTSwgUqohqgguNpZPyoc0BcGy88-zVzBjReY-RneTx8RdnKQRkEOn5UGUh1wVfK7bCB32Nlugt8MPyJOpvErF93ZL8oB3QqRK2VjmMbse6Q97sqPWIdwfArVIS378txlIucECq_Nfks9H-mTOQlY0_eEiTGGC91h1PTY7ZPfhHcN42M9kuv73LBUllD-SaoF_jhF_zerNlblvI7KqQfIB0U9pxn8O1weW-iT85qIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین حضور تیم‌های آسیایی در مرحله حذفی جام جهانی:
5 بار —  ژاپن
4 بار —  کره جنوبی
3 بار —  استرالیا
1 بار —  عربستان سعودی
1 بار —  کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/Futball180TV/95981" target="_blank">📅 05:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95980">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBAz1WH_eaXPMBhuOA1CQpCnDDLN1S8Fstr1rchFCfYu3KJgutXJ71ckSN0AfD5jTcGmFY2pbPB7wiN6LW1daNH-uU23tlYcY2cqwB-F9VsXj_I9dvxKTp4lhYdvZFoecm1I_c2oryxGzw7cm3pOxXnPoITf0a-Tx6CVY9aRzJ9vAykIJEuPFVcj_z55EtLzG4iz0eDK3hnxa8_td6qZyjrQU2BXfEyhBy9qptMZGizLCl6hAxikiwobWnUkdV-cMk-Ebxrv9-RTaGvU1a97ZkZwo110_Bz4Ta1DPJrxugMckYRsFOcirJj8upffcdMlfr8uW1dLx4A00Udqu0q_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
بازیکنان رئال مادرید با 9 گل‌زده بیشترین گل را بین دیگر باشگاه های جهان در جام جهانی ۲۰۲۶ زده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/Futball180TV/95980" target="_blank">📅 04:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95979">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf6SP-vwOCUzDQUeTSsegrB1dSpcm1TBE5LqvodfIqqsg_E7RuBioVle_kynm_KQLrfbLDY87gvu-wDrh-R937-UNLvOCQlSfiwAIZwe88Sjd6CfO4LYdMtg_m13ky8Dt8slVTnFFkVStRO0hE4wchdEHhk19WwhQzcvKVFd0glEyu4lWt9dDCh0SF-6b525LaC2xHHpLU7IDGaMHfqrGIggKbQuUyVcHU4Uw8_ow5kfD_N8flyF22UJHvwXlBFOyvCcIJcwB-Tcsn7BpQidwiVs2cvuCvbCWLhIdbLzqNU_E1C1EtJSit-hmxtFS6U3TLWlSZaF5nKmQMgsl_WKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F جام جهانی 2026 پس از پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/95979" target="_blank">📅 04:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95978">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIwf_GUG3qU0OybCOgUdSylyC0_6qbFmNfqzkPv6T2op2vNCJwXAgIul5MVCCTQcosf4Z6qz79BHy1jEWSZyljm3wixvdlrc3rco-TEB_3ySXA18_9yiAutN8-WZ2RhEwpgSVbcy-NaNSNWljExXjshU53zXiXM8E78qA1csWfseuSxS_ADGLHBfQYXEeDhY16fgwMZTHLh5R07KN_ZKpITkGbRmtBcz-PUElElkeLiW5Mk4ZU6FmKe3kjPXrf7OGZrbxZoEOMMdo_2jkb7mEQHxBWj4n-TJktTH4C-jN-6_ij_i4UHOWfOBWlo4Hx8GXoJgOUsaQ4zPZA01WwweMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تکلیف دو تا از مهم‌ترین بازیای این مرحله جام‌جهانی مشخص شد:
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/Futball180TV/95978" target="_blank">📅 04:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95977">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETeBojntr2W4s-MoerO-VRiCFspN6LV_EpZWXujSOcRltTV-I76b_4BErdvLBbnwHXK6voCS95jvc48thwlFMgcI8xpC0BJ59OsweIqG_SpMDs33WGalV8J9uIGJk2ELAJgPntdsVl9YPHFvPwbxxLIMsd4ybBr142OoTs6CUf-33ZLnI90_wcsojS5fXdFgmbl18QAbGBUfQEVfVit6gLwsrZJtokumzICnk7k3YF210RyrWCCIK0c2quGsi4i1WyYt-GCoNThoba9GRBq5FMGv3Pni8A4Wt2rlQPYcNnTaPEg4H0A9rXBfSYkrb_63U-_ldYgopdOpkjn1AqCiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | سوئد دست در دست هلند و ژاپن صعود کرد!
🇸🇪
سوئد 1 -
🇯🇵
ژاپن 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/Futball180TV/95977" target="_blank">📅 04:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95976">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzESAYOHAvaeaQxXfjNLqpdkOfWF2KBdp7HTOnvkcoJjtFZ7nJXTbkX_lGP-m0n0V1EjTJxkpoWBeGuzCDf3UdPEBFSw_FCXpOzm_FnGApYFQJKuhmoEbH11E6FD-6LSkevoU9rGyAEsh9FDyqQKfOd0Ja0f7rPAt1VJ6hGEZqyqzCfPHqD7zjUQQhi9AUVFp96H2_x-ReUALLU78yoqBIyHB2_Pwqhr2dkb0_f3_PavgYWcEQEIV8CObh92570sPROoKBRdXPYtKmPMc2C4MQ2Z5608UEdqcohzz61zJRgwH5mFpAYsxxS6VwTiNeLyyeEjyxZXjXlQBurd0_LfqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | زیبا مثل لاله‌های نارنجی؛ تیم کومان احتمالا حرف‌های مهمی برای گفتن دارد
.
🇳🇱
هلند 3 -
🇹🇳
تونس 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/Futball180TV/95976" target="_blank">📅 04:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95974">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qj6x6myutTPxWVBSBgZh9Wh70ZvFibGkFyrESTCHfpbNRu5Comuper4j9F9RZw31NhKVZ0wpSudHgtZzQfc1uLWWW09ss8RcWmEoTOF-jpqXk_7dnEg5Dje3OhzwOVXnhjpEUkReXgHO5t-T0mPLTbJMQYt1gLA7GDnPTpHkG_4bZfJ_GlJq2VWF6vJSI_sEugD2AjzAzTDiCPZH6qgpw5hRpCOd3X08-N_W7n0RNUXGrOJvx5Nt5uKEcxJEsaEU-gNTWe4nVO5iGvIvI2IqYUyG-lfJDJR_g4YMFbwqb7qDoV9F73yTmGhhaRkYwvUwppSf1wbw5H8W-G_QnaQlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v95LBZwOIg8gaoT18ayJZwYLEtRZZUV-bx0hvdClwzW6UGKlVUARvyYpIbq1dXcBsPvkaEulbNjiDyoqlRJrydtzh89b_mJHvE6P5wUlhmEpcrJMfrp2BE662GzrvhtR7VTu9-K-tXWuTJ1-UPzt4lhC2qXx2At1xe2VwOgZ3pxxZCxqYjJR6ia5TwZxaZfy6kHrOWh-vKQILB8g8iJfKPBcogbqF8KyV1RDK4ZDyF8oTax70JW14Vh0n5OyRvsGXOwrEOf1mgSuZTUI6NuZ8LuFYCI40AGacjtuF4vHCUHb8dKn-bUxuYkM12lX2hD6X-Q6Lo1LjHxSUKVclSFMgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
🇺🇸
ترکیب رسمی ترکیه و آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/95974" target="_blank">📅 04:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95972">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlhUr0uCV-BCfDsqn_1-w3nXp4HPE47Lp3Njqcg4tkgp9PiOceom2ghxSeLKFgh43VNNWkoGIDIAqHBJG3w3dgmH9KxFIBYd3j8Jmx_YJuD-jrukE61fzNVm53gSjnNSA_Ur6c9Q4MMe3qRZ2zpbaOC2DDYXZ9On6UNkyHdvozvHRECJKZyxNoJQxhu_BY2fK7gDn-dbITVNxFyV3pE-ljIo2r7vcoBwSXjDub5ZBqhWvshW5LfumA6UiNnYdqxW-h98dBZKBUSlFxN0Hc9Tey9cUYyey2LJuY7HvYSM4asqKcrLfXaT4PDBEuzS2_Fwm7mVxt98SPmmwOVkR9EDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpwZHb-202GkVKsKs3pNhLUXfQZZU1HKvwI4uNfx2OoZGRNVOaez9wERUobCCXQMfapDvMu8Lr8WSwRboEDh-Mrwq2NdhRDOldtLWehPLuEkK414c8Hh2aUXjlhBaJ55cAO_dH1bX8HQBO384b1YB9rsyhwP_WiItifTfCRpLR4nT88xBRMWWLSRu3ZBPj_cyGhPFThZHwSFfV9MCPf63blO2L5n4B1tFwUKnTqFWugUdsDmu6_HyHDh3-coDcbtavGtejECoGug-m1MB5xCxU4a_qr1fVNe3ZLWr4PKijbzKtE3Rx9B7mKUJTeKpzLOrfiCGBJ9w3ckD0IVgtO_oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇺
🇵🇾
ترکیب رسمی پاراگوئه و استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/Futball180TV/95972" target="_blank">📅 04:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95971">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b281416ebf.mp4?token=RWhmLE4rhfJHv8XbheTqOWQLh5YTNZzzSkttz6OAHdjIy5CTz9G0JTfruqS35aBOueAk8lwzWdNYPFDaADsE-Bh-qr__c32P0WvUWwjicTtZZ6mX2E39r7WbkL8HLvYeDD-H5mtzxq5mYJbJkM3MyxBMyo0fqnCIXL_M3sK9l-3I8nciC3qe9H5kxxDyKf-JPYJhSGHA9-VsgxnfrCLh-LGKCN1CvPZXNwf6uDKMWX2X_lYYLPoudiXzGH_lReFj-hBZ1vCrNYhtNJ4amjlvk3dmnUp9b3FVnU94_vJifZ1Ko1U0sAetTekj-v9VXxJqZupKjwBhS7mmpmhjAu1a8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b281416ebf.mp4?token=RWhmLE4rhfJHv8XbheTqOWQLh5YTNZzzSkttz6OAHdjIy5CTz9G0JTfruqS35aBOueAk8lwzWdNYPFDaADsE-Bh-qr__c32P0WvUWwjicTtZZ6mX2E39r7WbkL8HLvYeDD-H5mtzxq5mYJbJkM3MyxBMyo0fqnCIXL_M3sK9l-3I8nciC3qe9H5kxxDyKf-JPYJhSGHA9-VsgxnfrCLh-LGKCN1CvPZXNwf6uDKMWX2X_lYYLPoudiXzGH_lReFj-hBZ1vCrNYhtNJ4amjlvk3dmnUp9b3FVnU94_vJifZ1Ko1U0sAetTekj-v9VXxJqZupKjwBhS7mmpmhjAu1a8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللل اول تونس به هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/95971" target="_blank">📅 04:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95970">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac282eb0c.mp4?token=TpNfaX-VswD3t8AHOqtvc-XqcQV2-BchAnR5NkDml6xmPhCtCgix_4Vp02-xsskO-4bKhz8UhW7IMIMmr2eP9cihqX4cDBTVB4LDWODqlbSnZJzRF7K5S0CVHXGBZvA_10GFXAX1iPXpDPo-7NRHPMhA2SeM4xANEgDrA741dQZRvjaY2GE3qdah4K0YbX18EDcIP0ppYvr4sTdXgI7T3b2XuEgKIFR2DNIiUSWWpTYz44vRcefVozWYPftGnmMF00BZQKLXu4uzBvSJmjxnSsvUFvhnmhyrytwJ9w1nBCo_Lpq9VlgAp_vmJos0fFdVilAB1Niu7XoUeHkP1-bH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac282eb0c.mp4?token=TpNfaX-VswD3t8AHOqtvc-XqcQV2-BchAnR5NkDml6xmPhCtCgix_4Vp02-xsskO-4bKhz8UhW7IMIMmr2eP9cihqX4cDBTVB4LDWODqlbSnZJzRF7K5S0CVHXGBZvA_10GFXAX1iPXpDPo-7NRHPMhA2SeM4xANEgDrA741dQZRvjaY2GE3qdah4K0YbX18EDcIP0ppYvr4sTdXgI7T3b2XuEgKIFR2DNIiUSWWpTYz44vRcefVozWYPftGnmMF00BZQKLXu4uzBvSJmjxnSsvUFvhnmhyrytwJ9w1nBCo_Lpq9VlgAp_vmJos0fFdVilAB1Niu7XoUeHkP1-bH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان نیمه اول بازیهای همزمان
🇳🇱
هلند 2 -
🇹🇳
تونس 0
🇯🇵
ژاپن 0 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/Futball180TV/95970" target="_blank">📅 04:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95966">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nup9UzP5pUqP7Bi1Sn3F2vxAJSl7sQiQlgMo6oGCrNHlnR5tVMotz27gGg1ouTCC03c18WhGIDreA46gtzhM9BJkP2iij9R0Eqm80R346ivP3i0cN_9ZkH-CFiNSQGbQksNS75PvXBRNNdFBkls_BmoN0iRJTcywGln74i50u5hCyTtCHeZBMss3AdP6yUG0F0lxbNId-0bnsaAo1gSvCf5YA-RvUT-FoYPouosIIZ26ktUnGxKDtWWofzpnJ5uRTgXV0-QbDXw9tZVhTToJZ6Oh0oI-OiRmf-g_mGOwLt8w716jXenHfWGoA7KL72X-ZvVLGaS57Vze9w35oF8KVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cP8GT97xwdwfXz673bFxa5Sij3NbDL-Al8LPSd6_CO6bWdmEjbKHV1owAIMvmlYl_Ggge7-rL0bl62WR3o94PevjYhyMm-uFB4Uytdf2Ashz4fvDVU3DhDSFWxNptD7PlLmxjv6xuWmQB2sRlaM--GaJTrc9MiQQbxNYERXUGhvWTHC4dhdjqj9uRTePzffusw13idD3Gj1M3m6Mbx_nbTs1lRjEpjL6KHUe0a7HYcpF_cQGQXEDaHUJl8rr0_GRAm7BNTus2-HBs4-zf-G1zRA86bgj6HzHhyqzXC3eD5cSUkzouQKnT8xjUdqMcJK_n7_29vu9hj9gjUyJd4IuwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXKubBtRIPwtIqqZuPuFJMhnH7GdFj3y9OoQs56QGh_nDozc6VO3FDLeTmCOoYyfCkNth5NVXoWR5wjjWqFsmfvSTDIz48wsDT6Yky8Kqzx4iv9D86T__uLYYPre2Up6Ekp7CgY_ekKnqhGMgOcX1N5FkwbLh-OxvWHPcHcaVJDywOL9-Kadwx7aiXCVq9bPqna0tG0szFVEbLRamupjqJkYBi6fNgIa8gbeVScsRjVqTpHHmKwSbuWD4nMaHUh0mtG2uGSx74aZP15Ty7vfpvm991NAjHjwQvHm4dx22YmAKfGOk7BZpTlDkIV1_LXrxV9L_HSdKzWP3t_NwTc1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKwLqvuHiKuxmGqH59C9Vfp3xyGC-D491KeFFVE6XSMAHrwKHjDa9SP-jcMecyoifL8PEPk6RFY9LGfSlPDKqqFqS___6_6RJOMSuUsRigUW7B1P14ijX5qoqyb3MXHxWLnVjUq1f_9k1EB_hbBnLUB9TbcH3NHx1GAOTypDZdjkgoEqhDXTru7Zwh4dFt7BcR7Sfs9Y74-kwFzg1OKktTHewZs4F0rnMSbx5VW_kMzovpJMvfb1fFbp-QQWI0jqP05e919Q9enmZgy_DBkzrPFv8qq1WZTp7j1FptsRo6XFJomAvo4YTeWghRpPiyVDpHWRGVP9QvZznFImB-mVdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندریک برای احترام به زیدی تو بازیای جام‌جهانی یه چسب زخم دور انگشتش میپیچه تا نماد حلقه ازدواج باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/Futball180TV/95966" target="_blank">📅 03:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95965">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پایان نیمه اول بازیهای همزمان
🇳🇱
هلند 2 -
🇹🇳
تونس 0
🇯🇵
ژاپن 0 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/Futball180TV/95965" target="_blank">📅 03:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95964">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPxmfdi2HUR2Fal1Nn4v0XUlCLPLvlKbIpD7FYZcACMD6PQfEEIxg8wQy9K-bTNHNWUjdGwjWtVymAijqOiEJx5M1M-KSi_NIMimTLNGof9TrnwV-7uaiFCapJCs_OeUfeWHyxhoh3kW-2RhqnZSHE2OSVFdODlPPmuGNcylQre79W91VSduL4WFsZj2IK_VzkwnQ7ePZBGiTPpn3Fnn6kvKthMfzrq65kZgzkaPW9nuQU0s1vrn_Y8tA5Ujsl8WfUHPyTyCHm22M0oPp0kI9WmN-B4JwTLCQ3FrHxna30bct49kYzAHkolxlO5Mfinsdz9xeajuhvWTrPHvp-YZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه برزیل تو گروه خودش در جام جهانی تو 44 سال اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/95964" target="_blank">📅 03:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95963">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1CpA5azl7as-Vuv4DuuQ2-kWxS0aws96XA2vpDP2_fxw7PnWmQAozQR-FyjMrPyVN23Qbag5Zz_jspqOzs9SgL6nDYOcP1hJPo3lBNIMylQf2Lgoa0NLGMCXSJZL-nd3tXUEiPv0crlIod4wADYgGM-l9n4m3vbZIB45TLvh04XM1i9HeW9c8VRWMIm4R-TLgxJPVU0x3lAqa9W4ySJLk-qgXyj3wqi7fGgwjbz35ZuNes0HfgH-MylEthmhz3JnglyeJzexmLrqJXeuqeF5f_9_XDjZGUrAC1p2n0CGAdkiw4GBYNbMK4VFc37Es32xsr7Chxm11EeBw5eigPb0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم طرفدار کدوم تیمه ولی نباید از دستش بدید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/Futball180TV/95963" target="_blank">📅 02:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95962">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48b42c7dc.mp4?token=id-IVacWSOvR8NT34LcATQGLJzmY5fMSlPshsq8zkJv1vi1MbdIEyEVBznlkcalHHs7ZO4PIYUBUjmUdsBJ9Xczl7vw_VnV5zz55W5RWPdqH3IrAimRUtn4JvC1cS0dDlE73nYyQCbi2n-tgcOG-F1x-lTsqvclaO7ek0VyULBuA2f-coGn63bAs8lxWO0OGn3iIKsSGmi7uMk91iCiawdZD8WL2r3KAmroFk1wZE8io8d_O7OTAU2ZGYOQZqhrMcHMAXeDTnMNqHtVR0YqNURc60F4zF04-EOwhJNgy5et0gF8I7bGqPvYcO7t7o9MgoUEu9ZNZ3WVFAsM_KiyWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48b42c7dc.mp4?token=id-IVacWSOvR8NT34LcATQGLJzmY5fMSlPshsq8zkJv1vi1MbdIEyEVBznlkcalHHs7ZO4PIYUBUjmUdsBJ9Xczl7vw_VnV5zz55W5RWPdqH3IrAimRUtn4JvC1cS0dDlE73nYyQCbi2n-tgcOG-F1x-lTsqvclaO7ek0VyULBuA2f-coGn63bAs8lxWO0OGn3iIKsSGmi7uMk91iCiawdZD8WL2r3KAmroFk1wZE8io8d_O7OTAU2ZGYOQZqhrMcHMAXeDTnMNqHtVR0YqNURc60F4zF04-EOwhJNgy5et0gF8I7bGqPvYcO7t7o9MgoUEu9ZNZ3WVFAsM_KiyWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم هلند به تونس توسط بروبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/95962" target="_blank">📅 02:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95961">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOvUIKO_U99IDN2EKTXblyKC5ai3vl1XiETfeKQ1EzFadGLkqqBZs9vFkJTbIVxlYreqABmMbdx3yL5HQrz0fiZY8jR9TbhNR87dzQhbPIscdX3vWm0Oq9VjIWUmGRe-27b0GPyyjFZvHDPKfqOosUCsHbWTSagbQocpK9_ujk9VtIuZU_hY0o2mO3l4OfPeAo3tAOnFSIUwXcEVs3gtTesKuTNtlMuMMuNM64sCu5S4wCy7z4pTNjsLAIOBfbFPHsaP5pmBCWqQKYRqHxcfap0_q56m-BflSOV7d3cTQHl4YKeXO7Yf2U-V-fDKZa0cTF9E183Bu4kbp_gaRt7aZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای ژاپن تو استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/95961" target="_blank">📅 02:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95960">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf81f3272d.mp4?token=QL6J0hsG0u1FMGCZX6pvZ2ALQscf9NhzCVEu_t7p7bmwJPKJmz2YS_QVdCaOIkojIzT3yz7gPSAKRDYaFqZ23QFYhyoCBgjBX8M0gdkXiAmrIOV9ZjeB9xeZWLmKCSSH_wwecqpFzj1wDYRRmCnM6Vrx6rRJX_sN4dSdYvmV0CacrTpSoOCqeMrwVu9h4xuivKBnE937-IciB62f4YS4__anA9vZVe6v8PBgqkAJbZ9jxSYdDIpW1Ba9y2MFuEoTxiwa58MjzsWpOmCTtqxgI4qKXJfVVrlOnbuyrqkGcXCKA2yrTtlPK9s-TuipvccqO2tD7qYO1-3tzQZl1VRY2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf81f3272d.mp4?token=QL6J0hsG0u1FMGCZX6pvZ2ALQscf9NhzCVEu_t7p7bmwJPKJmz2YS_QVdCaOIkojIzT3yz7gPSAKRDYaFqZ23QFYhyoCBgjBX8M0gdkXiAmrIOV9ZjeB9xeZWLmKCSSH_wwecqpFzj1wDYRRmCnM6Vrx6rRJX_sN4dSdYvmV0CacrTpSoOCqeMrwVu9h4xuivKBnE937-IciB62f4YS4__anA9vZVe6v8PBgqkAJbZ9jxSYdDIpW1Ba9y2MFuEoTxiwa58MjzsWpOmCTtqxgI4qKXJfVVrlOnbuyrqkGcXCKA2yrTtlPK9s-TuipvccqO2tD7qYO1-3tzQZl1VRY2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول هلند به تونس توسط اسخیری (گل‌به‌خودی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/95960" target="_blank">📅 02:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95959">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هلند دومی هم زد</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/Futball180TV/95959" target="_blank">📅 02:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95958">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هلند دقیقه 2 زد</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/95958" target="_blank">📅 02:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95957">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
📊
🏆
آپدیت تیم‌های برتر سوم جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/95957" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95956">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2dYvUBrYKjo-EOB5P2adZOwgBkBTYiVG4fUtDJW53Zp7fuk-P3SyDC25pYIgbu1JAdA1MUO5IWeEspQzgDuq_fv3Hm8QWKoVm8DdQZHNvH68I19BBRo8CuirJZia5xlI9vCLTIhaJhw-zwPSiVp4_4dPJ3r0sEpA_z_j_jDcWU7CTu3TfdIJrwOYKN_jJUoVpIzYiZQ6h-uk2zi-0PQ09bsbTeu2fyODmfMKF6CoHrCQZBXc1aink6ZaMZHk9JTSLqKxk40ToiihCVy_qruF3S8YMi6ruR3xCsLA5xRZqsnGchsOThDa4XW5KvpSapFupkEC2u1jT-psrCMYinsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت تیم‌های برتر سوم جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/95956" target="_blank">📅 02:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95955">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZcHGxjIRhjIHbU2kk8yV3MuzH1-CUCbjZepS6pAv8vc9OqPN2dJF-JWFeLqAcV1BnrabhdYq-i__jML4UubjxZqfXWJeF886mhPwF3wlUzmwRJ4kmMp0LmpqYac_hI1UvBUBkne3_mdMuts0iNuVZPWVhDaVAxN9RymKgLz_y3BpqwjkbV1AJRHnTbSpwEe6_LXpLJY9xqVFebEhHfrEwNAeLYxBEQ1rGr6HJ9s9L3kvSJGv5gMvHc4ri1Oj5SguoKA5WD9vt4Zb55BadN639AZ_Q0WeV2h51usn2H5FQtG7Uh4I_DyBQbZYVbXnzoydK33WITCFC7X-GciRwPoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های که تاکنون صعودشان به مرحله بعدی رقابت‌ها قطعی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/95955" target="_blank">📅 01:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95953">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRvhlcB_rMoFmHhbArtcYI7hOi4ziHk5K2H_2LhbuyYTK3GS6kFbJJJDonKOI2Azdgs6G8ipI_eKFDeoArhP3vUcRc3DUcHhNh68O7jJqTuyMqi7oIcLc6A1C1qGbvTl15jQRPbTKF_N4YLQYV2lRoOxpuDFi2ekXXXZtgSOpyH8oIOt7d_iPdV-L-mJ6svAYs-_PYzBy7vksdnQDo0786o_1c8rc3dlECoK0wpFd7VhHfAoDZupSiIIbvbBiO46RNyIQ2mhI_c5mAi9-2Db0dnAVHX6k92NQUucGTMq6WoiF-l9QfXwLk4HaGIxSgBoN4YCI5AovSddHshYwOyxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3ph3cwU7Zec8oleEvhtnPpN7jRtG4PLLuXMJ5hJZd-WuCk-1n7GzMoXagxQdstNB356HAvni12IpZnM7PhZqdFh5zPNpeJkkDFavK9AGFs_mG8sJsClkAOiUHhCjiCpn_UokzRVvU9DnkPuamedvWFjwwzde7p8TiKIow-I45AanTtPr7YwoshhNXMG4X7ZfQjo29740YoI7uTylFrt_KfXUEIKxsppvDeEcRHCN_H4ZgssxYquSwh6bq4MPmCLQsb05oOX2Kr3kuDqM41mXsy2Syl_1Lzya7rTSKSOTdmfeGIvDcX8vyJ7TVvHGw5YKOqlxrfYkWKrhrS9JOM09Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇹🇳
🇳🇱
ترکیب دو تیم تونس و هلند
ساعت ۰۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/95953" target="_blank">📅 01:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95952">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYtdGlLw0bb2r6lETtmYf4ckSH8nn7ZFD6bKYNTSj_F-J1SR1d_vM1i9cB_rVdx5WEthXvL-Lpio55WtUqZxtaMffdHZIJrPtXgqFbtHVcxoVPeB2tsnuhlNVzWB3P2ualYaOWTGMmLxrXdJsdcFIg4Bi9FirAZj7pFGnhPk12zF2KqHVDA9QSCow0DtfPsZHa-J5rmaQ3EBnLeK2verKT5pCX4Y0f4VLXM0cMICRXW_O-BwSFer69xeQXjYrDOkyDnavOTZ9MuwykBrO_bC87eFi4Rz0kn5dn5PFLAnBIBYAOy4XHHsvRGSYvvc_T-ngPm2ox7PzOPw9d3pZYZ6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇮
تیم ملی ساحل عاج برای اولین بار در تاریخ خود در یک دوره جام جهانی به دو پیروزی دست یافت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/95952" target="_blank">📅 01:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95951">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOo5VuzO2AEY68NzQA61b6lI16Kb5nnxNnFDYo8UxE0Y62TUUycUx0mM2oLg-tiWwO863Vnml8j4CY9bo1l-4bv3h5Dhhn86dIEWPu8E0DmVPmIXw6-Yw17JjcasSv25-CHDY5qAxkTtTzyw_1j6EfMrUrksMGnJh8AwA2NOiECrH3TX_qf5Ge7l8h8nPlKTzrBYEWJ3KiZ22OHgp8h7QRA-7DrrrtlWqvOgfSdEOHdxqtBRakfk7OO7DfbJUeLGRunrCJuAhK5shos5UvYoVKOV2bMvntCU_GWdxALtBJk8MTR5k5vqOu59CBVCdan_4wKFoKCfjhjj_oq9WO2MTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مانوئل نویر در 9 بازی متوالی در جام جهانی گل دریافت کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/95951" target="_blank">📅 01:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95950">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UINVvF-Zyx2taY8gXx9Fl_jcUJ_3rkWVDjGIziheqCJPT4471KOCvcOy7d8Po4j1tTIRUoUCv9VNOQL6VyN2rN4F2Yry9bOqVS3zugExTFIqv0KBYJu1ptVZDLUX-k1Hj-U5Lw-qo-2Op6-JXnljyFeropKYfRjSTJby2C5j0kgdE-GFzMW6LgkeSHrWsu6jgL4zsOWjL3Tbzawpwyv46jf8l9cJei4nmJv_YNzueCZ-Un33r6H-jN-oOSkTaHsdSei74rSyK1wZrD9xt6KRD4kF661sV3JWRtjRSLdBzMJKs0WVlPdrRE0X4IxoCP3MoBAZAL7PEXWRID6mZNJJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇮
🚨
🔥
🏆
یان دیوماندی تنها بازیکن این قرن است که در سه بازی اول خود در جام جهانی به دو دستاورد زیر رسیده است:
💥
بیش از ۱۰ دریبل کامل
💥
ایجاد بیش از ۱۰ موقعیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/95950" target="_blank">📅 01:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95949">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/95949" target="_blank">📅 01:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95948">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEhPuDlRsS5gDOQcV-0qYzNjr2h6qE0s5LwzvWRxdKjSTIuzC8kPCaBm3YPE-p3b4UnI3X3rcTj5LjgjbWg8lkZroA-sAQdWPzBWShivND26woXyK5b23wv7QP5FuOdpDfLVeUj_8sMG4aVLMUEKtGEge6MyJz0TG0VkDHEANpvtkZ1g6RVC9gHqAMgCl92xBl5RChC2jUpHkPkrKw76ogeCGZfaV-CGUp-DgT2tYWFXptVvWe5v5lEY0cCmUWs9QfAbhmm_LZX5xcnRN7pQw288w2PV1YYjlCJieBnMFYrdI_-t0PxH-53XiWOvSEtMnvZG8VQ6SniXlTI2n56yIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/95948" target="_blank">📅 01:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95946">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd2WukgEDCW7Tb8MI6Rd4uPkYsAFHHX0WcbLlGx4QzPBYd4A6HS1IzKxKyU3iCK7o0a1LzRMxPrfvsNkERg9hVSVoCSdvzXi0ajrkCKxYWICztFtgykUiU54wfOdzze4P6NXZOIlnhJRqZ_-2HvS7IKD8EZ5xG4Ty5oNGUh678Bpj0GRoUCrA6lg4u_5KB9lGceKph_kbSEDDPyfhn55Kt5NzPXIr9BaF08qD3c5KLK5SOl9NP_zbDLZ9A8bSqnwpDKvlzD1iKIckrae_W2SavxNiNDJ8SbN-zJm7dYmVUH-6fngEMpx91bgYEMAJSqIDU3D3-gpdorwxK0sEwfF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
❌
تیم‌هایی که بیشترین باخت را در تاریخ جام جهانی داشته‌اند:
‏
🇲🇽
مکزیک — ۳۱ باخت
‏
🇩🇪
آلمان — ۲۵ باخت
‏
🇦🇷
آرژانتین — ۲۴ باخت
‏
🇧🇷
برزیل — ۲۱ باخت
‏ ‏
🇪🇸
اسپانیا — ۱۹ باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/95946" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جام جهانی 2026 با حضور 3,605,357 هوادار، به بزرگترین جام جهانی تاریخ تبدیل شد، البته که هنوز تو مرحله گروهی هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/95945" target="_blank">📅 01:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNBsAwnURBEvj7_kEaSkTmBWDKwLtxUqYGJ-2ntLOBYND4UisI5RGwAkC3zQ8hNGnkXt9bhyb0lbkxQjmB_-Qgsqv04ZfMjL_-8eDzgnuZTWitucCx2BYun_v1lqRQE20BuzZL-o-z6euxu1o1ntHEud7exmv4OTGmLZsqSl8TX0zhQFXUQckOaVQOt6E1NnOsnldaIfDoM2ZpcN5jBId4ZOxwDFiuBAmx1WhQYYhJrYVLeqq4BiRwwlpb3mDF0NvDZUFcHt1wwexmhcCtQKo47giPNYZbWN3mWWwN_ISDdXudB6Sej_USMp6uqkShj-GAqw1l7IXIE31a5YIip-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی اکوادور بعد گل تیمش رفت با زنش لب گرفت
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/95944" target="_blank">📅 01:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95943">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVzDFrTA_kkvIWgEJj_Oj_-AXGOdwYoBBpcrYzmSCrTj7b8w-JyDjl5HFWODNmJSqDNeLEOIJvn_cb1_eaT70n_8GoDUttTzx20XJh5M2w_G2egwvnxdvmcNAZIEFSHGrZ4mfdHynSfGAmKygzWiu-NIy2H1x0JTyVoCgTppPhb7SzvmS0aTKe8eMUeaYpE8YPuC3gOmJ6puqeqdbmmrAwrTZL431hOuw5bO0mewNqUop6NCN4FohkAISLX6OdwBARwxv5Zg7FEXioTvOevnN6Irp0vZoAGqWTdBX96WTVOHSw90eSJjJv58UUyq9yuJNIchO4KzLK83P5imUEKbWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه E جام جهانی 2026 پس از پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/95943" target="_blank">📅 01:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95942">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇨🇼
تیم ملی کوراسائو در مرحله گروهی با جام جهانی 2026 خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/95942" target="_blank">📅 01:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plSkqKzVBEe2rX57robNJDqPUZurJ02BjVLZfbe90BC8nicOlyuYtpf9V7FI9gL-LWRSs2dzuuXvcL7zMF_nZNRHCg6KFiztZHS1gvzPfZWEkWLnfGRBsgCENl5s7goFCi9gJBaPHYcy5gT0dJJZXPQZRkNg5uh299wGLW7J6SGwiV-xMWUftNH1KhF-U47DFUkvtiYpc8pm18KFmVxH4yizx__F4N4bssCzsjEPDQ8X8O98uM02GvFB8XUcDAest8EM5HssFwh2CeKgVdNgG-ZUe8Km_rIA0i2vjRRsF515TMxZ2S9mr8NDumQNIsaFDXaqDAz4pI6FSsZfjP6_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | رستگاری اکواردوری ها در هفته آخر و صعود به دور حذفی
🇩🇪
آلمان 1 -
🇪🇨
اکوادور 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/95941" target="_blank">📅 01:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🏆
پایان بازی | نیکولاس پپه امضای صعود ساحل عاج را نهایی کرد
🇨🇮
ساحل عاج 2 -
🇨🇼
کوراسائو 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/95940" target="_blank">📅 01:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95938">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZ96U_816GH6kxS4QPj8MxHOuGmEFBpjnQOAnIORdWIYT1bIYkh8I0vxWzZKiq4jrN-cbV0BgqdrQp4ldKLIlcViqELWWaC7_rPvtXaFBGHiw0r4HwT1TIWxt_DNVFBmMfvp5Ax4LDtFihIdyTC1dHdNAd7yOyrBBTR5bfUIXYR2EhPZwfucogfFVdvGqCikyZGV_7sv34VD8u9TG5Ky0MvDeHWDf9oq8R1in61c7XW6L7ukNq2iHcNTT7sPYJ1f710PORUGdk4s2it6QxHyRRyXMAm3pA9DsjqKVAXT5MvhYNUyUX8b8s6GHf1X8dR0AZBhocSUQ3CxDnurE-tW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUEkinOcfvyeGzuCd4GC6eH9zJbaHo8KJmdy37cbOy1o2TqzxE1BNryQWylpwt5lQFy9zba1c20aglwqA3m6ZdZrB8gq3mDWJfSjgVrnkiDqGUdYyKE5QTGDGt8h3xTVoDtRXcen8xpmTDbNHpgkI-V6iknd2cq5FQKUNeYCC5BiA2G_NeN2zL1WlfmQrvgVJzBLMtFvNTxJjBDjlhNiaaIo_FfZ9PARVGbT0FCoI7g5eh-_wMRCxXnEgX8qgu1MNJn_k6vyrbqR3VL5lpRHAoh96S2xCWDy05FsszF0H8vMqCJwUYwgF6_TR_IuhXnME60-et78_B_1ck-F2dcJYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
🇸🇪
ترکیب ژاپن و سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/95938" target="_blank">📅 01:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95937">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dbd9f7642.mp4?token=rliKYFzTFYWV-QD3jC2O1Vk-julz5tUwh5KSEmzHyd5UjYVC9QQUVYFzV2n-WGbRlJEggwJg5AL2E6RET5WMfAtcaFUx4Z6zN_Zr9yQT6lalPByrL0tBveCB2N920WPXqeNchS-ytcaWQSOwWjc5KJvFPeCu6w4IR20XFncM2BzRfpLttT0EIDm1o-8qQ-8NUrE_gUGDDHruPSAznI1UdK5Jxf5pcVzJreLp9ILtoXRwOyGZ6TaT3HJp0VB6qk-yXnj-reIXwbj-FfL6AF-B6mbKl90aY9fBUmv4N-90pqdxtZmdahahHHajcEF0Xir6-xcMQtS22yXxvLkzEQjUkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dbd9f7642.mp4?token=rliKYFzTFYWV-QD3jC2O1Vk-julz5tUwh5KSEmzHyd5UjYVC9QQUVYFzV2n-WGbRlJEggwJg5AL2E6RET5WMfAtcaFUx4Z6zN_Zr9yQT6lalPByrL0tBveCB2N920WPXqeNchS-ytcaWQSOwWjc5KJvFPeCu6w4IR20XFncM2BzRfpLttT0EIDm1o-8qQ-8NUrE_gUGDDHruPSAznI1UdK5Jxf5pcVzJreLp9ILtoXRwOyGZ6TaT3HJp0VB6qk-yXnj-reIXwbj-FfL6AF-B6mbKl90aY9fBUmv4N-90pqdxtZmdahahHHajcEF0Xir6-xcMQtS22yXxvLkzEQjUkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اکوادور به آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/95937" target="_blank">📅 01:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95936">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCZA0XeVB6qX7Oii13IqmNtyCfr5ZvrMOJCXHZuBcRaSYuDlRO1eMLdRHv51tZtRQxQ49uaEbqfFc3ZYgAg5Fr85xXq9CkQzdxL51YjuRkEb1t9dwdCOxDKcd4MaufshaWePa_qZasqYqTca7C6TIfYPd4hn0ECN4b3FxlibvJKXfQX0oiEMYjDs2NLKODeuNO-6d_YhDZjAy3VY_X1YfEEgZx15PynT-lEbTZxlCymjJ96NUNNbXsY-pcaYBeRgYa48FwvN_NgSj00PJ3yaP2ts0gPK-rH6cF6PXszEGZtNav9TJyshZCrSwN7EDPzSTY0XMKbSiRFRrsmGENjNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی اکوادور بعد گل تیمش رفت با زنش لب گرفت
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/95936" target="_blank">📅 01:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95935">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نویر اینجا هم رید</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/95935" target="_blank">📅 01:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95934">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اکوادور دومی رو زددددد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/95934" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95933">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/95933" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95932">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qg-RGRRX1ANQQD7HSgL-OmNvUCBqmW2ejnWqbxjhur0vNrI6w3IuaeOeSz7JItbVhz8K2t61er1yWbXa1iIFHmIVYW0hAXbJXYY7WTk0XAjOPEtN3oZHf1bpYhXe-G8iHh35bcycGCTxk-DhdH--7HJB6-4ErCDKZheriSb-cPXCu1JdumxtKx0E-NIr_K1beHiqk_hFPuTdO0S-gub5zk2zdMTtQ3ap7k1_S93hWffH_wgZXh4rPGw7JhWBgN1mmxtL8m9agbeLVKzT7dpoO2NlT4PbQGY1vZTlBymNBk2hErd7k3bHIoo0XQgqXLbrP1lpLI4LwnWW8HBT_32rMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نویر
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95932" target="_blank">📅 01:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95931">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3fb1037b27.mp4?token=q5--CxmNMIXkVaHDFmnPGt17sr_JgddUU-ifkvCMzApPUqibmzsdNEhQ7zmxQMZ_5w4Y5ILXT4FKx6i1hRZU6ObizkP2679eBZKcOxTMKvNuEhDPruCdf-tQjrP19bS0gAxNKElsw1yScP5sFl8XOPpnk0w1BFRNgoS9AHlMk_Kj3wFFxkQynyM5yqjB29Z3gOl6JgH5wQQLexlhTQ3um1ebVsYOrs3-wsJHXJJPQMzmENvLoNN1FSyvTFJR0sBKLj1dc-pg01AkBN5h51O2E0nuqS8fxqzmRZRWqYo9futADUbBO3ToApc2C9CnmcbFFkidfliZN8Tb01rC87JKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3fb1037b27.mp4?token=q5--CxmNMIXkVaHDFmnPGt17sr_JgddUU-ifkvCMzApPUqibmzsdNEhQ7zmxQMZ_5w4Y5ILXT4FKx6i1hRZU6ObizkP2679eBZKcOxTMKvNuEhDPruCdf-tQjrP19bS0gAxNKElsw1yScP5sFl8XOPpnk0w1BFRNgoS9AHlMk_Kj3wFFxkQynyM5yqjB29Z3gOl6JgH5wQQLexlhTQ3um1ebVsYOrs3-wsJHXJJPQMzmENvLoNN1FSyvTFJR0sBKLj1dc-pg01AkBN5h51O2E0nuqS8fxqzmRZRWqYo9futADUbBO3ToApc2C9CnmcbFFkidfliZN8Tb01rC87JKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ساحل عاج به کوراسائو روی دبل نیکولاس پپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95931" target="_blank">📅 01:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95930">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گلللللللللللل دوم ساحل عاج</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/95930" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95929">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کار زیبا و قشنگ این پدر که برای کودک نابیناش بازی رو اینطوری گزارش‌ میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95929" target="_blank">📅 00:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95928">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/95928" target="_blank">📅 00:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95927">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzML0Tg2IiyVDwAovJsUDJFJHXRke0e2zPISfJa5x4Q6ImEvyOz4ejphcWIuwKX01_4Afi9JXKgn695eRvSChHUTn5yOgUB2Oiuh6BN3uOnvrNBwAK1BESCJx3GQI0A09XkNhl-56k6CnVBzizV47yHmswYniJTVlARkYGd4mXDCYvYg1hXtT1716oaNIHhi4VWVgg-kUpAK_GRSIGN8BuQ098mn2RcqFtHPinjls7gIqIgW3rljM_d0kE89BZ27VS2R81WjJRWFVbXfxXWNvFE6yidaGYGX3N9k2ib8GkU2iA6sS83HEhDDmTbEhOCOsX8ALWhqX-B7iBUgELLGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/95927" target="_blank">📅 00:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95926">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eW32l5q0CPSs2MACJanpZhir3EPrvluBhzG_YckCAadM91r5Q7SbcRLsPHQIGBEZiUfIFns4jCNjkJEt6AHQjGqn11Thr1l8MQNsNWXIBluyYNwWLjk89gOzSnUpAOMRL7Cwd2YAuri8GDsxxo939N5wZ9b75W0GGj_dlsPWvfikSi2H1kvdFerRoi-GA0vKond-i7yBHiRCZ0dYva1whjdbkW_MMCdCe-3z-KvNnU8B49y57EYot3U3IrN6yhcBpWOztuPG2T_v_jo_7v8AQ0i2717pDwfM0Yte7ZDx-h6TIzl6o7y7fEUz2N0WRZAY395ao8ncR9E3P1eagfW9lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشلوتربرگ تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/95926" target="_blank">📅 00:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95925">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae9310246.mp4?token=lg6pisFS-5P_Badqa3opCpqsowEtH3pd5mhmaVxTv8eXkCG9THIwuBCtr30-QPzJud59VUqkHZ26Lq0Ve-5mmnh0AKYG0d7bRWQnDDU6rOPkQYPvKpnghuo5WT5z1FHl9_9L77PUsx4LGcRA23c9nVyIG6pGXijhSkyHX4pi0R8oQNeMDWztGShMNG6_9wAz3A5h-d5SkmODFDZRKvkYZ8PrG1jlhe7OVXNatoXYLEkZvDsk4l9s1vs7pmu2AFpaH9QiTs0QeA4ShDGvffnKVyf9KyBabFPuh_y4G4GKMyjuA3kkfo3IDgsr9iGQtzZ7--ozrYBFdxqNJgY2_b_HIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae9310246.mp4?token=lg6pisFS-5P_Badqa3opCpqsowEtH3pd5mhmaVxTv8eXkCG9THIwuBCtr30-QPzJud59VUqkHZ26Lq0Ve-5mmnh0AKYG0d7bRWQnDDU6rOPkQYPvKpnghuo5WT5z1FHl9_9L77PUsx4LGcRA23c9nVyIG6pGXijhSkyHX4pi0R8oQNeMDWztGShMNG6_9wAz3A5h-d5SkmODFDZRKvkYZ8PrG1jlhe7OVXNatoXYLEkZvDsk4l9s1vs7pmu2AFpaH9QiTs0QeA4ShDGvffnKVyf9KyBabFPuh_y4G4GKMyjuA3kkfo3IDgsr9iGQtzZ7--ozrYBFdxqNJgY2_b_HIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مورینیو : امیدوارم بازیکن های رئال از جام جهانی سریع تر حذف شن و برگردن تا پیش فصل حاضر باشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/95925" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95924">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/95924" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95923">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYc552cl3sv95MiRFKLPxy0s03CVbDZxO0M3-8d1Cya4ahOllisRaAROFfP5Ve-_KGGFxf0vzlkCRtiKOdFj6sWGj4tnSNHaK-5dwO2oCbHP_h1kZ4gR0XVdaBjE67CzZYgQ3KI0JxlrNUkUdopfC5uPpiJczmU7NJ2s6snOC26-GboOllxVOtYIYrgy2XYaIHTlx4Sz_yneKVNJcxWcv0DkSqAToK8DHK9k0MDAJoBh3rGHg4uyRnV9kiCe9CTGMVT9Pv-04IcN-e-SYBuUXeRpg-h-kov2I2sOrSBC42f3Y-t9zt3zHYs4zxQnjrYMaMbzq7vG1aGdWlBsfwoLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شو حاجی خسته شو، ببین من خسته شدم نشستم. مردک یه بازیو از دست نمیده.
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/95923" target="_blank">📅 00:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95922">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کی گفته تو داور باشی آخه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/95922" target="_blank">📅 00:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95921">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پنالتییییییی برای آلمان</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/95921" target="_blank">📅 00:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95920">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پنالتییییییی برای آلمان</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95920" target="_blank">📅 00:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95919">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
الیوت اندرسون با قراردادی ۵ ساله به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95919" target="_blank">📅 00:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95918">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRX-LS6afgkdUu5SG2I3s3zZcsbH8OUqPRpXYmtAbsVDaEgEwMPp4Y9kou8Ub6eFklcJ3T_Slb9-IC6r2YU1n81G2dgflvpvmZ9gAzpGe0KgIGteLfb9rlIQcz1dl7zdgpry-t5cR9U6qhP0n7u0HaCstiFaP5_S6O185eYp1kCa0RSs1jMTDH71oOPA7o_BNiMNZZjWwDg57QbZSH7meZY0F-TZyfV13VYYj1jZWO3lYxltqp7PORqZVFt_uKvZpRiLHgWwy_AuHx4IaUc5hWpt5DlqM04n6o8l9pLpuPnrvjX8ZdKBdwagSIay6wESJj_og9BJzlbGUZS_stbK1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری؛ منچسترسیتی با الیوت اندرسون به توافق دست یافت و حالا مذاکرات با ناتینگهام برای تکمیل قرارداد درحال انجام است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95918" target="_blank">📅 00:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95917">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پایان نیمه اول بازی های گروه E؛
🇩🇪
آلمان 1 - 1 اکوادور
🇪🇨
🇨🇮
ساحل عاج 1 - 0 کوراسائو
🇨🇼
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/95917" target="_blank">📅 00:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95916">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQU-84jNwl2uks3TMKKaSWPPBBaoyKtwnk4xKOf2Ystu0jDl7cA43yPJQlTKwCY2mXgJbq70ozJOCS-K4i63hgwak6C_NP7F5O1wDUj9lk8zh4qx4ecmtMdH3ivq7zH9zDnQ11E63lKD-cU1QNm0UmJxbWH_PrrZ3YMyMlUc1wQFt3AWZr__XUnnP-mfQCFqYH0oSRdxYUtPLkkZ35E1E4d2CNgO7AQyUYhUTzfpKZTDD1IZHLuBE8RLjs7blEQPb-SVD11eEr-kY_1inDzp4XJguyPPdC_TAWDkxrA6mkHRWpgPJY1Yz_5xFXfHjYMWi7QRW44qDwSrrXBwc2xKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
❌
فووووری آرشیو وار: گل آلمان بخاطر خطای پاولوویچ باید رد میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95916" target="_blank">📅 00:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95915">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بازی رفت آب درنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95915" target="_blank">📅 23:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95914">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇩🇪
گل اول آلمان به اکوادور توسط سانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95914" target="_blank">📅 23:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95913">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5rDWRF6N1czeL1YNoteBcJDJteds1JVHb0s2NUuAhqxeIFrETkJh9PjLo3CBC5kqv_LnqLRV6L45vL949BSrJlUU7dPXI6PlaiSRjJ4Vd_jnKbRAxc-uWfPVv7qHBYIKNtQIr8wHs7OV3PSd3qlQQWhpa3WGQjR5v01TNQHbg5q-sEKDtXE0MjCJkUV3mx5_EQTr-S3e_olKJ05Uf-zEo4o36D81V7RHmLv178WLLnwhM4Fa0Lo5oTFeAA7uj7nfJ2e-if9vO5-BGSxrphScbq9gNMaZfc-etckuFHJBUs2x3spN66_S6JWpkEzUyTCe_Lav3ZleigYVVqmCJX2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شو حاجی خسته شو، ببین من خسته شدم نشستم. مردک یه بازیو از دست نمیده.
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95913" target="_blank">📅 23:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95912">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986547037.mp4?token=Y4_w07KYcarxRy2nOaQdM6DXjvH0t-xRKPj2SMq6UGXJR5Uh-pNKD62oedy_WfP4q8K5rJUTs2FE_4T9TsTaYEHq5EAtxPz0zTWP2WxDg4cCmAMfgRaRLaFpz1mUoFAO5WB_dnz1LQnkt4LAGlbQqzMX1wJ-9j1Yaj29PQMqMnF3dAfNz3HcbVzjBX9McN3TYTgQ1EMJhauXGB42usv_VGFrtWQfF40VEXdvrz8tIHFIR8Ui5lhD8L8sFGZxgu0SoOublfF7F3Z7t3QDoHsImrZPWQDJhTzWKG3RQj6RUCHAg0DG3GeEgRMwj7sKkUQrbXUsP6H4AS0XSRCAOxBsGwA5ukvsKqKK7lzsBhkXQsHoN_Is8EuH0UfazRpycWO3b0p5f-l04M0BIJpKA_7t92Qpcq9MLCvIUm2dsEaHn3t5hDKrggd3Na3ma4AyGwhu-tUg61F4pCl99bZkSToyqV4wFXWsIKsxTzjF8ICw9aVnevpOKbOK5zGAXTy1E-urZekw4etGLpQtedXb5O034epHPuDHxRCy7kCdLFjqzWEvVaTcceNgC__zIkOHG9Be4MM3jXVnc1CmT3UEB-7c7ol4WYK8OH-N8MWG7jSoaMWuq9XV3Zbvr67PvZ_gtRkuj1k3jCDNCVuQkmwacs0bQpEtf7mjk34xFw2_1nB8shU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986547037.mp4?token=Y4_w07KYcarxRy2nOaQdM6DXjvH0t-xRKPj2SMq6UGXJR5Uh-pNKD62oedy_WfP4q8K5rJUTs2FE_4T9TsTaYEHq5EAtxPz0zTWP2WxDg4cCmAMfgRaRLaFpz1mUoFAO5WB_dnz1LQnkt4LAGlbQqzMX1wJ-9j1Yaj29PQMqMnF3dAfNz3HcbVzjBX9McN3TYTgQ1EMJhauXGB42usv_VGFrtWQfF40VEXdvrz8tIHFIR8Ui5lhD8L8sFGZxgu0SoOublfF7F3Z7t3QDoHsImrZPWQDJhTzWKG3RQj6RUCHAg0DG3GeEgRMwj7sKkUQrbXUsP6H4AS0XSRCAOxBsGwA5ukvsKqKK7lzsBhkXQsHoN_Is8EuH0UfazRpycWO3b0p5f-l04M0BIJpKA_7t92Qpcq9MLCvIUm2dsEaHn3t5hDKrggd3Na3ma4AyGwhu-tUg61F4pCl99bZkSToyqV4wFXWsIKsxTzjF8ICw9aVnevpOKbOK5zGAXTy1E-urZekw4etGLpQtedXb5O034epHPuDHxRCy7kCdLFjqzWEvVaTcceNgC__zIkOHG9Be4MM3jXVnc1CmT3UEB-7c7ol4WYK8OH-N8MWG7jSoaMWuq9XV3Zbvr67PvZ_gtRkuj1k3jCDNCVuQkmwacs0bQpEtf7mjk34xFw2_1nB8shU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇨
گل مساوی اکوادور به آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95912" target="_blank">📅 23:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95911">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a82b1e615b.mp4?token=itI3AXWsUmp7ZyvFeA0eNLsgdu9XGkyxFbvtTHyQmOffwqIYQwbvLzRPW55ykZHnqsMSEswQNY4fcPLvhRLHUq4qRZWaUrYc4mtndVDSnJqR5-2fmkSuOJUFpX6P9Qp8O-o7hOWoTL20okfLNeWYH_kTDlVVVOFyXLVp3tGubXqcAUwqoaXmyMmA-cG-EMyQJ5nrlD8KY4vAZrPB8NBPJ3bjCWcJG99x251oZmqy9OABbucgsqCcu_VYntenld27To1PzKsDCuRRPEsGQQYUXS2tIHS8X6Z9pWW85GHQlkYOHnFbRhenXUY-ZOYJmaED3rjlD0gKnBU4TokVuD0kZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a82b1e615b.mp4?token=itI3AXWsUmp7ZyvFeA0eNLsgdu9XGkyxFbvtTHyQmOffwqIYQwbvLzRPW55ykZHnqsMSEswQNY4fcPLvhRLHUq4qRZWaUrYc4mtndVDSnJqR5-2fmkSuOJUFpX6P9Qp8O-o7hOWoTL20okfLNeWYH_kTDlVVVOFyXLVp3tGubXqcAUwqoaXmyMmA-cG-EMyQJ5nrlD8KY4vAZrPB8NBPJ3bjCWcJG99x251oZmqy9OABbucgsqCcu_VYntenld27To1PzKsDCuRRPEsGQQYUXS2tIHS8X6Z9pWW85GHQlkYOHnFbRhenXUY-ZOYJmaED3rjlD0gKnBU4TokVuD0kZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇮
گل اول ساحل عاج به کوراسائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/95911" target="_blank">📅 23:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95910">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گللللل مساوی اکوادور</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95910" target="_blank">📅 23:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95909">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گللل ساحل عاج زد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95909" target="_blank">📅 23:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95908">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ae52ce55.mp4?token=Ul2uvOkYQarPrfcnqOHuhmmp31trp8fuNbfGwbNT9KdzPuYVtdqruZuel3rLXiyqMCoDE4hjJp_qthC3eDTBmVRVmr2EJHtu8UG1TLnabFrNgdYP0aX7kM1XrXz1tO0sJLv_Td6GtFPrPyVUIeTcxGfWTUKbp8qmenuIisFRMr8AMnKOf9VEig00K4IOi9-G2nvcrH2DK1LAzoK4T5L-1jnJgZsM30teM4M3GcLHqtLDOjtQkNUweqHaEbZR1ZOH5PH0nWaVLKbKeWkp_3vzgTJz0Ht9c9NSRaUvUS21MRQc8UgJKAgMJ7d4QJRWWSF2qckWN_03fQn2f8EQPjhTTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ae52ce55.mp4?token=Ul2uvOkYQarPrfcnqOHuhmmp31trp8fuNbfGwbNT9KdzPuYVtdqruZuel3rLXiyqMCoDE4hjJp_qthC3eDTBmVRVmr2EJHtu8UG1TLnabFrNgdYP0aX7kM1XrXz1tO0sJLv_Td6GtFPrPyVUIeTcxGfWTUKbp8qmenuIisFRMr8AMnKOf9VEig00K4IOi9-G2nvcrH2DK1LAzoK4T5L-1jnJgZsM30teM4M3GcLHqtLDOjtQkNUweqHaEbZR1ZOH5PH0nWaVLKbKeWkp_3vzgTJz0Ht9c9NSRaUvUS21MRQc8UgJKAgMJ7d4QJRWWSF2qckWN_03fQn2f8EQPjhTTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل اول آلمان به اکوادور توسط سانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95908" target="_blank">📅 23:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95907">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سانههههههه</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95907" target="_blank">📅 23:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95906">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گللللل اول آلمان</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95906" target="_blank">📅 23:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95905">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بازیای گروه E شروع شددد
کوراسائو
🆚
ساحل عاج
آلمان
🆚
اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95905" target="_blank">📅 23:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95903">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ne--BQ4Srv30nferF-27kJJyAQ3i-qOFyuqFcZTaxZvhQWoKZRcMh_6-7K8Wx2425iAdu72ssbPoeFGN1B3VWS-T_KZ1_egFopDNvkMbyfcUtXAjit06j3ZIoDQNSqvZiol00uYSqwKw6LFHYuHwBroxNOl0xNCEk87uimWTNRnL4iBFgc17LwO2mn-NKmRDNCLryUMS7DUrkJyIs8Py3nC611u4G7e7RBwv-4DpQTxXcoQ7Tb-HjOkqFHGtQzcMbmn9lYrSWCq02YYcJA57hqKpqsFaU7aIzDUnLZ-CpGBXm0YqJB3ss9v3gypKOJX8TpNyXUIcjSXfkmJG9ZwHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_XqWE2W_6k-r5_n5E-Q4gMZjCclQZ2nNpSbEiT23wos_MgMQlaD-uES6T5f9T-GW1fLgQYO_-NGXO-iWwDi4RgTcluC8m_QLezerHJm_kmC3VCs1wxcuCGZQnsX_lOg-CLowl8jwRuSaiBhF_kbQFa7Cx7FBEtrxtHef3pSE_4RsU7lP7vTOnYz7Tvj1svnisg3j6GgJUCi0LSWW8bKr7jibmgwpGwE4MRji34Wk9H8A2okZKDow3mO1A8oyglFFWuW9TsqxfyU1_MRAPhGNCYhpfH8MGNB9pa64guj3xSXggv_dDm2JnLnbl7IzJaF9UlUgGlDeLHZTdN99JOfaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مسی سر شوخیو با ژنرال باز کرد.🫪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95903" target="_blank">📅 23:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95902">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7dcfaf7a.mp4?token=OZYwaLHdk6ZY7l5_n-6E9Vv7GyjKRHDdqgVOfSokP2T0XKwNu6HGgroLZn01oecobsZjJeVMQqyMMwXJIeUiukMFCvtGDLWAMx0mAGtSO6jjBYZMvTEE-2PzjtqQllo13OTCDjRc5Ipp7NDfeO2afYg2kRQlLzkViYJSXR3uhC87PBt3G0_m3TsaDzZLJmfW7VrsguBYmIDHnKbpCcVJDoQfjasMYyv8WDTMzOLMMeooxtccS1DRDUkowQDhIzGYKC2Ne5sC1DlE5RqAmMOyI9chtOQCaX3lak3PV0RQJBcSwQpRD2w6O2Mn2gAyPvOGBv3wT0sqrVe3NewrMSRVgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7dcfaf7a.mp4?token=OZYwaLHdk6ZY7l5_n-6E9Vv7GyjKRHDdqgVOfSokP2T0XKwNu6HGgroLZn01oecobsZjJeVMQqyMMwXJIeUiukMFCvtGDLWAMx0mAGtSO6jjBYZMvTEE-2PzjtqQllo13OTCDjRc5Ipp7NDfeO2afYg2kRQlLzkViYJSXR3uhC87PBt3G0_m3TsaDzZLJmfW7VrsguBYmIDHnKbpCcVJDoQfjasMYyv8WDTMzOLMMeooxtccS1DRDUkowQDhIzGYKC2Ne5sC1DlE5RqAmMOyI9chtOQCaX3lak3PV0RQJBcSwQpRD2w6O2Mn2gAyPvOGBv3wT0sqrVe3NewrMSRVgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلفظ اسم بازیکنای بارسا توسط داداش یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/95902" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95901">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1bmpddHubQGbmWvSiBfOuTuiskeoLxigewiEbDJmesOuIWCbv0fcX4w7YYf36a9m08IgUh8DBekVTIFOQ0FMeukZdszabnvInBirzu6aw2rUDsTnPDHoYIdCBRWyfSbGfAk_w3FfZzfj-NczXyK3jwbsU7rSw0iADWO20YN-ftLxw1IIXL8g_Hc4xabVwJov1e9OX0Dr7e6oAq0-MdnT8Njet3zepvey-4reqo1yKgazU8DHCMaf1HvFpjuAtz2oqagsSjHtSChfhENNQATQpO-c7V94luSWSW-4ujdTx7J3PqacsM9PKf8Wa5qH5VSqv_xv6SiD18GMLgMf8Ctnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
رنکینگ آنلاین توپ طلای جام جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95901" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95900">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKSsWOBVijesOvZjUx3-NcQiyS2QsjatKISXztYvnTEliSQe1Fcci2wxc9A0_dCtb0I-EJ9_asI65tFYi5U46VtplHUr-Oci1vtTWGXgtPcKpRLLI40KvRUcMllqU4MMOrMelKXVPEWYRSsKy7fl5KsCoZvPMEiGEe4cUjUZSsvr375M-150qiRBTMM_selxb7Oh8fiw3NKZ8q9hR4P6qdwvSpGR3iD20mtP_xWCbkNwoLHq0U54f6VdvVEAaR0WgSgiKSng_tmOLVHmTkKbEGNiTNHvQwhpvSFVNZ7Uj37sjwOApKQOl5nzeq7JvzvOD7AS-eOEypvB7Kl8ELg5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو مسیر متفاوت پیش روی کریس و رفقا در صورت صدرنشینی گروه یا دوم شدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95900" target="_blank">📅 23:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95898">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYG_sW0NgG9BgsjoxlzZPKVtqNA3pw6UJVyC0LUCILhG0juKQTMrB-O0DVqP76tVnpBnlaP7jlMxAF8-cP-q6MyqSay5RosAAnwWUqoO-p-9_ftimV3CJz7KA-BkRysZJYBxMm3A5x8Ge9lJ-lfwN595so32U63zmMgDh_LwSguVLpCy1yGVrsKudNEnMDpnDD9lPerKVmDQg7XRVfSAlSUa6XyDbXNJzp3n1yq-LYiyINLK9nbxJD4V0qUnQQOav-VTIcFKL_TzEpnUiaVAyTdWX7zhvDgErxJoOF1RXix5YXT2ZVE-VqnbB9PjpolYCz76GOoZwCnbWACo1df3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEfz8CaqesyR2jpb7MOVbhwDgOMpBtxMJCMmXeUa5rnCrD3g5V9dBk2TOSo-JHmJuWYtpvt8EyfPgpifBuKxfACFtdfrBY6mo5Ksn3Lf0J2tNCqbbpAqhfHjiZOHHsfTbLD1MXIFAMdFLSHRi9K94fQFM9mHjA3ZnpdbUdAqIWYBHxyTj6yTb23HfsfQDvDz9qMehu12cYPAB4M_T1ToHTibDPIqyVYeXWdmzeKRT_v3r1QxUsiTJiDS68bCC5qt3R-eryCi_DJGiA966dcLgc5kCBS_Tv1rJk0awalyuwNZnpywRxiCfrg8NnlxAiakddrbNgJT8jXcadxBjRLN-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
فرانک کسیه صد و پنجمین بازی خود را برای تیم ملی ساحل عاج انجام میدهد و با رکورد دیدیه دروگبا برابری می کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95898" target="_blank">📅 22:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95897">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZlQIBqvilv7AcZhFK62lnCJ1fKeHI3JUqMIvfNgRzWFbE4kInBQo1Z7lvHl5Pfv5h0Abt8EuKC2dtQoA5ztjOpdxYtOm1kndoyi4LUI4fNYL7Zygy6F_jaZVnAht9utd7CIKToCHIiY6I_ewzv7gELly_r_D_arSfXlyChBx8NTgT7rORxsSvdIrwr4U_Dnl7kehHPS3OPCWYa0n0j1RISIr04TR-TIf7oVT3VEOhaBy20Om71Y6iaONVHzTl8NizGHNesIbL6GDOKaw-mt7IVwdQQvVrGB3vUf1MUnTLZHM2ARO_pi8zM0CVIWqM20JQWA5nCjZLOE_FzJJv725A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری کریم بنزما در حمایت از وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95897" target="_blank">📅 22:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95895">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sG6iHHmy7vAhQm6lOdWW8WQ4d0Vn7R-jHPyKV5CQe3c2QL4R0suaF8j-tIdNpwXEhTHSAzZ8MWKyNGNFeb35K6vktW4jeTg2m3ynJW2FHZ4xKWQW104d0Bsrvfgq_mr8-wJrbxbalf0MfcZ0Y01WMf-6ofFgMKpSozzp0M7Sbvj1QDV0UlwMnlrcOlfBJFAz2SiHmG3206rYTomXcElVBWpf0Z5jmjNh_OQ5zb3mUJj93McBAS3eSaCGkNn2-M5z_EnxjwlobzN2t9FhLQo_dZ6uBbpeQuLEXLl2xa6tVvG7YvXxWZN0LGrlz1L030x9_ymLqZkEYKFkLXoaJctLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMuiq_lMUzAE9XB-lI2tSf5sFVUqYZ6CvbVIDUH7Tx80Wi9Hd26MfuvlFCzCbD30D6QTB72XZ7JKOxNig1oEJ3ZSCs5IIh3ubnNkxLl08jXnVKNmt2A6vyznnS7-VWYKZWzXclo7uDb3XbyP5eQC4gjr2gTcNhPog3OQtYNjF8JtCStWmRcrE20iXfqQeRsUfeiwvz50WoJEoZSXzD15sfkinWFOtBo7k_3e3P7GGGOzXG1K_yR2j7KV4LH9_27kgi1Zr48X0FhIRkM3EVzZgRQejXNIPkiCYYqMoQriKOU8pSWmpJ8odeledncY2e5CtFXpxK8pOikdGP9p7VIi0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
😀
ترکیب رسمی آلمان و اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/95895" target="_blank">📅 22:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95893">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAGrxH33gN6kZmNdALIfMiDbdBgrxNbV8ImBd9HczrW6RVXvN-chaSQ3tAbfVHapvPkGdc9iyEHwjDBfot0jNG_Ti8_Y-DLCIbTO32uj6pj2d5NlFTsdDeNy-oIjNP0g104dcAeG--JcVhuGuBcS3jaVEsurIqYNtftTP723CCezmr_MnOSNJpZfuJ79Hfsf4y3Ex8qWUsta4OymSrFMagsIJ0Lonkw3VgrzRCXNrw6PzUWirH1SAkTf__t9lv71ozgrwhYpU0ThCPcyR8OpJaZEINu4MPvrCxjwj2UaNCNrRs0uho2hO5NNyyErNloAstH6ESs_jJVuhQgxReAvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHRIO__0Sa1vmqeEcNklQQcFOg3JenOb-_3IHnPkywgZ1tCemHkAp3ZpBM1g_dlxbwCDBbMiFAyIw8OB7RzWbcD-X7y3cT89SHoQ20_lAqr-uAdVsD8rlcvK-njMhDLN0ybq8aWEU2Hf1qWmdGe6iOkeQxFa0Zp1AEXyAo1JyOkKjk0lC5TM5j0O9NOuxOXBe37T-Sq2hpUopm1obUjICDy3QHZ5CS7EKi83nfBA9sLTAjfdhfvp94C4FjyAt34XgSNaDr5cje5vNMTBcHTaSLzkqKOexhkfa6Foynddkl8wfzXdmGp766McGnsmXYmRUDZOR1uu6SS4aZ08KKI2Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب ساحل‌عاج و کوراسائو؛ ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95893" target="_blank">📅 22:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95892">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b5db1264.mp4?token=uFmEimg1xq9bIcT-Ei4crhAxiUu7J4P9xfBU3qmdyz_8lu7rpMJMJ89cXhe8REq0z1VvQOisrGdz4d7zy-KKKhV7nZ6pI7iFnnIoHLVcai1__8pC6aY2o7Nv1Emy4ZYJL7l2SR2HemT2iiByCo6KHUOkkSJZjn21ng1dEJ-JEKfiU7UerSzam96lnMgMg1bzB3Jg3HF4IHPIe0i8O_Pe9QXz_GbmIwHq9Kj9e81d_x3aNLCifUiZnIl49AL-t3ZYhbNfDMJsHwRs7GhAbf-i2D4NoXOIe2w5gUIAF0Yyk0KoaeeUnBr4aXFEyowsmCIWBO6VwoFnK6Sa-gOlThB5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b5db1264.mp4?token=uFmEimg1xq9bIcT-Ei4crhAxiUu7J4P9xfBU3qmdyz_8lu7rpMJMJ89cXhe8REq0z1VvQOisrGdz4d7zy-KKKhV7nZ6pI7iFnnIoHLVcai1__8pC6aY2o7Nv1Emy4ZYJL7l2SR2HemT2iiByCo6KHUOkkSJZjn21ng1dEJ-JEKfiU7UerSzam96lnMgMg1bzB3Jg3HF4IHPIe0i8O_Pe9QXz_GbmIwHq9Kj9e81d_x3aNLCifUiZnIl49AL-t3ZYhbNfDMJsHwRs7GhAbf-i2D4NoXOIe2w5gUIAF0Yyk0KoaeeUnBr4aXFEyowsmCIWBO6VwoFnK6Sa-gOlThB5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا لیونل مسی پنالتی‌زن خوبی نیست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95892" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95891">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98f8a62d4.mp4?token=WiTpkmytQ0lSvkzxayxmeWBb3yd3_2djuroYb0Oyca4RaVVAyKcYwmi1ODP4ID8wtiFkrCyTBu4S5MUf80VR61u-AwwGlDonTWxeHn1UjaPCu1KJ2-Hq3b7ss9LJdSE1R-boOC-psVh1GBPs64EA0g0B1jVm7OIRp0hYgNZyHSUNdoA7gUKZRjI3WWt9ZmypiyBMx9o3gwpmK-wZ6DahXJN2wQ49W55SvNJeZOlKjyYJ1AL_W8ZhP5lJc7VaG3FoDrRLoFEr2FjVhaagGYtctAW3A-K06ouYVHLnMZn3X38d8t7ZklYDlwG-47dnDPvlMeUGboDrJmc_OXjbThcSvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98f8a62d4.mp4?token=WiTpkmytQ0lSvkzxayxmeWBb3yd3_2djuroYb0Oyca4RaVVAyKcYwmi1ODP4ID8wtiFkrCyTBu4S5MUf80VR61u-AwwGlDonTWxeHn1UjaPCu1KJ2-Hq3b7ss9LJdSE1R-boOC-psVh1GBPs64EA0g0B1jVm7OIRp0hYgNZyHSUNdoA7gUKZRjI3WWt9ZmypiyBMx9o3gwpmK-wZ6DahXJN2wQ49W55SvNJeZOlKjyYJ1AL_W8ZhP5lJc7VaG3FoDrRLoFEr2FjVhaagGYtctAW3A-K06ouYVHLnMZn3X38d8t7ZklYDlwG-47dnDPvlMeUGboDrJmc_OXjbThcSvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
این دو تا فن مکزیک تو همین جام جهانی مطرح شدن و اخیرا کلی طرفدار پیدا کردن، البته دلیل طرفدار پیدا کردنشون هم خیلی واضح و بزرگ مشخصه.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95891" target="_blank">📅 22:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95890">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009dc59e9d.mp4?token=bKM8OtEKUm2ranBwhfC8MLhx038I3aZgSPp4mas4j8grmFqJLU-eV-u99V0Yx8iwZvY7hlAFhmFoERbwdDDsyKhskGncKkLvKIIelYiK7HJJ-d7cq9drqK9Hud0D1jd4CbvqbNcY1rXMsSaiI_OUz7Iv0NQgMZdthukzgqu0ig64qlyevywD4A94ezbPynqhfkHimIL5p5IzeS6OVqeeSqY4ygHxin1gDpaTs-udNPsDFGdHFV5tIIrwjUwIv3LV4BSiw726tKG4xSaqQxDyUwALrNfP4Xo1QduD1uAvvF8a8JOfMXptbfW0WhRKpOQmGmHLkOPo0DiTy2W6Y6QNpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009dc59e9d.mp4?token=bKM8OtEKUm2ranBwhfC8MLhx038I3aZgSPp4mas4j8grmFqJLU-eV-u99V0Yx8iwZvY7hlAFhmFoERbwdDDsyKhskGncKkLvKIIelYiK7HJJ-d7cq9drqK9Hud0D1jd4CbvqbNcY1rXMsSaiI_OUz7Iv0NQgMZdthukzgqu0ig64qlyevywD4A94ezbPynqhfkHimIL5p5IzeS6OVqeeSqY4ygHxin1gDpaTs-udNPsDFGdHFV5tIIrwjUwIv3LV4BSiw726tKG4xSaqQxDyUwALrNfP4Xo1QduD1uAvvF8a8JOfMXptbfW0WhRKpOQmGmHLkOPo0DiTy2W6Y6QNpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای هلند قبل بازی با تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95890" target="_blank">📅 21:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95889">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqjoU5mNaSLH2MMAjIYEKyRvx-hn9Tcxb41ILGFdH5fJroFDtMy2VUHVaWcSwHpdxNcboetY4PN0rPpUOrRAKt9BPJXeYL6qA7rd91O1k6vF28bAJDbkg5pRJ1xWlsmnNMXJL1vNUeeHJQo3h5QUV9hXlhKa5C5_RG-V4mPWGaJZfU4625nQ58UmjSeu4A4Lo7Ix9cwC-a-pyVshYjrMeDAG3_EvTMPyXz0MjNQE-T3_0sCdMEpCCGPoA7VR_Xafzl9BBTmKQ_uLXnvayLqhbzDyqn9NUCv3bVAJU9aQEnWCoN3DuSCZPVXxfmfO0WOLklosQu2WtCMliIyjxCrgBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇿
❌
پاتریک‌شیک مهاجم تیم‌ملی جمهوری‌چک بعد حذف از جام‌جهانی از بازی‌های ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95889" target="_blank">📅 21:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95888">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCEfEZ305v2Aq_pT1mQK5UcWL13jDT9IooRG8BVXweqg0ClC-WYbhWnFqkh59TU3XOUTdTxLn8wqiSmRgzPI0YHZ3gqni-TO62mCTmYNt1iVUaDWrtlnQtOfNU-0RsqrDm7_7EDpuf4brycu9jOMEc0adGHHyqbFTi6i4VdU-CW6cd6do0AqCnTuP9NbdvPWtri7URWkDDP95ByIehbG5dy13NAp8BZYVwEY-Bi0pot-WDCzgdRoi43A0m-d6cvUBeIhRUitQq6gNyg_BhewzEiz_55fpur2YQPZ6eOAwr8hPjyCsJ8-cbRiTrbKqvPrqcpNh2fAwLjtyMFnj8b8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه هوادار به یامال کمربند قهرمانی WWE هدیه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95888" target="_blank">📅 21:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95887">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWgKeWviS23LM65DdQRr8BQjy674GM-2RjLAvLnHHre-aau3RCsa02HH2FfaVFZzMcqibTb110qfbVoAfi2YS0ZD4mwHUUaxFRy6D6EAEM4JbA6qF906m0kPB-QX-_vci6or5WCRDo-UytGxG-JXoxONCWycsY1-Jg3rQ5iHbMiJooVDdVxnFcDOmnP0-aNZFjkKzuaO0kCDWEZF4sKzx7ldGqOSIMaOQEeu2hIk3QohueGV0H8ISMQN8oPCt33VsWniqqq87cytQmTvcVYY10DpR0K3lAsspz-xsuaUNDJfD-oO7kUaRvdEWI4ZboerjoF8sCc1FUx6jYpIePMYVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇨
🆚
🇩🇪
🗓️
۴ تیر
⏰
۲۳:۳۰
اکوادور
🆚
آلمان
📌
آلمانِ صعود کرده در نبرد مرگ و زندگی اکوادور؟
جایی که یک مدعی قدرتمند برای حفظ روند کامل پیروزی‌ها وارد میدان می‌شود و تیمی دیگر برای آخرین شانس صعود می‌جنگد.
⚽
🔥
آلمان، که با دو برد متوالی صعودش به مرحله بعد را قطعی کرده، حالا با خیالی آسوده اما با هدف قدرت‌نمایی وارد این مسابقه می‌شود تا جایگاه خود را به عنوان یکی از مدعیان اصلی تثبیت کند در مقابل
اکوادور، که با تنها یک امتیاز در وضعیت سختی قرار دارد، می‌داند این بازی حکم مرگ و زندگی دارد و برای زنده نگه داشتن امیدهای صعود، فقط یک گزینه دارد: پیروزی.
🚀
⚡️
آیا آلمان به روند بردهایش ادامه می‌دهد؟
یا اکوادور یکی از غافلگیری‌های بزرگ این گروه را رقم می‌زند؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95887" target="_blank">📅 21:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95886">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zgwxl4j2nZwBbbNdqcZWmEguXMWP5sAwmOkB413oC5qNkl3YqAVsyfyF0Z5O6kFuQ-y2kvPFYM2Aq6yi6-JJsjmR1FS0xXtBubNe8oUjQe5k6k6StPyOMUsK3EvC_I1Yt_ydlnaiPK4xAXLxNulgKH6k1CJS6j0fJF0hM11jvS7rZBu12Nzjg0EVruBNRNxQ69BgrAHPzew4XXpVe-gbOjAxHH1TUI1yZG83oBjAG979c0N6IdPh4YYUALzJGZ45j3JOaPVkoOuXM6K4xWZ625T70iNWflWO6Gq8K21WuXLYe7uSq3daUIVYIQS6nY2j3BZJzuew40z49EAdlJ1Vtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#فوووووری
؛ با اعلام رومانو، ناتان براون مدافع چپ ۲۳ ساله فرانکفورت با عقد قراردادی به ارزش ۵۵ میلیون یورو به بایرن‌مونیخ پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95886" target="_blank">📅 21:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95885">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
⚪️
🔵
فوری از رومانو: رئال مادرید بند بازخرید ۹ میلیون یورویی نیکو پاز رو فعال کرد و او به باشگاه برمیگرده. کومو تا دوشنبه فرصت داره با ۶۰ میلیون یورو او رو دائمی کنه، در غیر این صورت نیکو دوباره به رئال برمیگرده و وارد بازار نقل‌وانتقالات میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95885" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95884">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGOjF8lNzhAq07G1VqRlk1lox2SS_J4SN4UWko9IQMscK7wFIjSjEPoWcoRYLyQQOZmfPeKrWz_rEWQtiPl9yPWdwA2dyPW7Ni5uKxUHuIxppAb5lWPv8wXLxojI_4Ks9Kn8-SvE_5ds9lIQDiHWp4CdgA8R-vEHqHBlXdtzDZSAXcKThmdY0pmepgTEZiaAmqbyYcb_C8ctg6aecZ5APoxe7l73JpdmgSfc9qh1QlG49sMgo52T9wPlNLkjV5eKD721LBMfPGxNdG0FzzZ07TWm5SHIUZ7piLtFKSFyobCCUJR-fAk5pJkfxR5XHMajzIG_F_rilkbNFlgs5RlULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
ریو‌فردیناند: پس از درخشش وینیسیوس باید بگویم که بزرگترین خیانت دهه اخیر فرانس فوتبال، ندادن توپ‌طلا به وینی بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95884" target="_blank">📅 21:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95883">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZiXiUHiYLgW3AR9bZQMvWwpVdOJqKdU6mcxjbDuqkY0zE4FTdZfc8SeZRqhZFsBvNvpfebV5SqvyLpJP0cOIJxyQ0GfoJ-tWq6k5NfGB9mY0nV1prW-EF73QJkJDWFXlhJoQGdN3bZd_7_q9EHIhwPzqXMW8oEUJhGqfSrWDrlX7z3QmaglQoXChF0G7XU-yOoNhllGu5Y6mZ1rGsv1eaTx_3grSXtzoQ-gXYepJI69sPFRKyefNF9gvoPbvj45yZNci6r5DOj-S0LQlXSPAjKIU_tmGjPLDzrDtjJdcGphDHRAQRpi11g_H2EmS70mTrxuaCfWm7dzK4Y7hAAH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
#فوووووری
؛ جام باشگاه‌های جهان از فصل ۲۰۲۹ با حضور ۴۸ تیم برگزار خواهد شد. بزودی فیفا درباره نحوه برگزاری مسابقات توضیح خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95883" target="_blank">📅 20:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95882">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9cGoJZcmfMM-ilTt5bsfbHYPeLyuNmkx882XCeTck4QWKmm7GhsqbO3czWey_EFpbIsPVOozBdsD-VxKpB7e0UrkPVGKauqIdizT2a4QhXndcMYm6JJU4pq8MOFnHNaC-mi1L7e41om9MBsBZbQUAvE683eekFn3Tcb-tcX2lZP0r_Kt2gHP42iDG1THxuzJMkq-pzIoKZA__t6F40Hugi3zon5cgRS4A_FItPZgjLIgkosnBHauh3A-ltlg-iOPu776AAeY73KbuW_MOqFJ3bBXPCtsDOP6BHYee_XhsKCW-HUU89Zwxj_SA_gJHg2iLUz-XcmBi5W17RKphBDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو تو استادیومای آمریکا میدن 13 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95882" target="_blank">📅 20:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95881">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh0kfApbsBX54tMacqXNKkzDN-qub1rkX6d2JZM16E4Ahuxbt9unhAFYUDWvEBbZ6MeR7GoiQQCY96kZGEDiv8dliMD2sdfxy30nbjx9AdI_5lyMzfBiUsJ-0uGjDqGNvIrLCxYkt4ITRHq1L_D3EByDGLmywdQSuecXiuFBcrN-lXG5UgQtditoTmZPsXd37ncvkwoItjjaZvPHmdu4KMFQIlcGk2fiOS9spmTIagGXguBWOq4DvP7irQGyfA9Q4W2whuFU4JktvNjFDLbCc1ga3H5TS7OCc_M54tk8IcR6z6doh-T5DJOhyO8F2DbE0omgHgcCCYfOtPmH7u_N_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
مارک‌کوکوریا:
دلیل عصبانیت هواداران بارسا برای من مهم نیست. واقعیت اینه بارسا به من پیشنهادی نداد اما دو تیم مادریدی خواهان من بودن و ترجیح دادم به پرافتخارترین تیم تاریخ فوتبال یعنی رئال‌مادرید برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95881" target="_blank">📅 20:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95880">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh6UjU5wS3Den-6J5RcuszJpkpFjZ3RSPyzqlldHWfXCOGPZRVN6wYl-Ez4E1eoAGjAoY6SoE-oEN4ut-FVlygxqQ7OJN0ScOBU_mYdq6IVr6Ax1hrOs5FPE_ujJpbyTFmibGkKUG7EMfyI1pEHaNbipXSpv0dxTyGvzaKiOpUl28pgFtjMhmOYECN7SNwtp1xixU21giQG5MkiAWtv2EoGoHzKCvh3LTQ6UuCkeZ65WyenuWGdCeWtJlLZZzbdHWgRfJ0OZTNKt0ZTupnsuZH-uH4a9XJLwNxu3Aurgyjx_q1jkLEezVcZt8q0Lxb_zj3xmZl0TAxzl11Cf6bBASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
🏆
بازیکنان برزیلی تاریخ که در مرحله گروهی هر سه بازی جام‌جهانی را گلزنی کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95880" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95879">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPWMgLUYO1czdDF7H-DhYyVIbnDFztDPBUO2fZ4dpUo8pTW2BZN7fS2uWt0t04mxUdg_SqaEHFRCRNmo0z9GMiV-hO9lrOMDb8-3ETcpqfCOSq40ijoyU06Rx5Us-bE4eP9JFUJ_HAh9XvD7NpiTN08EyC3xy7irVfEGyyABZ5DPw39KC6MV-gRGGXRimm0gdtuTViT0ZWouZM2ZCTo0-jmw7V5SUOWGKJqowR90bOzq1QxetM3n6YCYtjprmWKD4XdfrJiXVEGRsRRayeUFBuyai_sgMqv1pkZAYHP79mjoRdG8A1KJd4k1wYheoOh8V9K1xcFiTRa2nMNrC46_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
پیام رئیس فیفا اینفانتینو:
دیدن تو که فوتبال بازی می‌کنی همیشه یکی از بزرگ‌ترین امتیازات این ورزش بوده است، لیونل مسی عزیز.
در زمین بازی، تو غیرممکن را ممکن می‌کنی و باعث می‌شوی کل جهان برای تحسین استعدادت متحد شود.
برای تو یک آغوش گرم می‌فرستم. ممنونم برای همه چیزهایی که انجام دادی تا فوتبال محبوب‌ترین ورزش روی کره زمین شود.
😊
برای تو تولدی شاد و موفقیت‌های بیشتر در یکی از آخرین بازی‌های مرحله گروهی این جام جهانی آرزو می‌کنم، جایی که با تیم ملی‌ات از عنوان قهرمانی که چهار سال پیش در قطر کسب کردی دفاع خواهی کرد.
تو هنوز هم شور فوتبال را به میلیون‌ها نفر در سراسر جهان منتقل می‌کنی، همان‌طور که هیچ‌کس جز تو نمی‌داند چگونه این کار را انجام دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95879" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95878">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/95878" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95877">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npymefwXRHhEpXtky6It67PhmS_3iMFPlqfCWh-eMf5oa2V_D1MArlz16rHdwfzjrVSPNTBcIrotSy1F9ljteIOOswRnr78HBk9vwES2G7eqUDQqHX4XnaqbdvVBIfbNmLKmmS1psfyFrcVxBZTz-DKN2yQX2T1KFOuC5suKjtJD3du_p4j71pyrGvnKuIc6PeWoFlUc43p7NY5pIfKKdyUbvm0t2LTIzNKbLNzhmIg148sqTi-6cVOYJaZU-wMjYp80ACWF5sUG8LM8uyj9NL0gifLGj8M2b6BRAS3_QomERs8Q0gDhh31AgWsuvlV-ia1lVvOFy5Ey46MP6wrgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95877" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95876">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB_Xw2KOaFruWOXrTwVA8h5Rgh_oe8xNkq3aXLI5eD4wWFHPJJ0yv1pMxiRpBdQPDorEwlg3OiydxB-hNAxLuIHOA8zUgXSjt4q-PikibIXcImK6TdSF-PvMu3pi0rw9fEelDfuNgdrPPMYv-e1Z6y635phInSF_dYQ4lMA9yBG-DF7cHyTNaSsVs75kSz2D_k884HdXAJk8mAjsx1YBHqa8bAQJxvoy_6MI-Ez3M7OCC2GgqUKjjrmDQqNW70IR-lvjL_iegaTVdlOHDa7HeRVzRuOQ6s49Y2RHe2mfs8_TmtWvOk-VE2j3SsntYmDq97Tmu2f7SGK98P6seGY8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پایان بازی | هفته دوم لیگ ملت های والیبال روز اول
🇮🇷
ایران
0️⃣
×
3️⃣
آمریکا
🇺🇸
🇮🇷
23 | 20 | 29
🇺🇸
25 | 25 | 31
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95876" target="_blank">📅 20:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95875">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2N3iTBmif0u3McmfeSgayKaWlLSGwUqro5Mwp6jpLcmoHWIFaBMyXoy7ZWVGX1MNT220qkTyhPA-sXaz8j99AOicKEPmT4yYum-lsZ18hkfCsWgnQCUtxXI3hH1cgiV2rf2SiG2c2h2InF6zslLWnKog_QOevz9X5ibzBdi3IR2bvW3_-ODusMb2KnJCBJspKwZxuZWDD0-iq6pdHwPc3LzmQfODwZdNer_PbU1PXNAu1iLgZ55rVYYZanZRKVOOPKxlg018E8ttcXn6ORZ4yTbbowJaJyeimATWzTeL9czqUD8Qj23VJq3NKNJHo2h-mcaZ6GrkRgYEaHvM4LYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پایان بازی | هفته دوم لیگ ملت های والیبال روز اول
🇮🇷
ایران
0️⃣
×
3️⃣
آمریکا
🇺🇸
🇮🇷
23 | 20 | 29
🇺🇸
25 | 25 | 31
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95875" target="_blank">📅 20:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95874">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa774ae16d.mp4?token=RIsj3jJAtVTKdJ4vKszq0EBfyGC2mkhVSNAC8SYDZGpIuw8948BkLli6K3vFY0ATgu2k44yrc0Jy1dmTz8Tkm2HIjIpmD_O7vUHPe1HM1R8RNzVVU94eGQOueWjTfzKrigXC5y7wMt9iYrqOQ43OL1R_shJcQ1VLSRJGB3akrcVrhFQTp0yp33NhyOGg7I0vYDqDLLjoN6UHzGnSg-Jt6Rgj9pBetY3DjfzbWvcQSAfkQBsf2ORFsmj292WvOjyiIVj08g1EIyGAqnZ3kmjGW_vxmwau_cgYPyHKVqZ7MORPpuKf3Dbb6bMBObvLS4Ayzn9f0ImM_DvD_b_9Gbcz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa774ae16d.mp4?token=RIsj3jJAtVTKdJ4vKszq0EBfyGC2mkhVSNAC8SYDZGpIuw8948BkLli6K3vFY0ATgu2k44yrc0Jy1dmTz8Tkm2HIjIpmD_O7vUHPe1HM1R8RNzVVU94eGQOueWjTfzKrigXC5y7wMt9iYrqOQ43OL1R_shJcQ1VLSRJGB3akrcVrhFQTp0yp33NhyOGg7I0vYDqDLLjoN6UHzGnSg-Jt6Rgj9pBetY3DjfzbWvcQSAfkQBsf2ORFsmj292WvOjyiIVj08g1EIyGAqnZ3kmjGW_vxmwau_cgYPyHKVqZ7MORPpuKf3Dbb6bMBObvLS4Ayzn9f0ImM_DvD_b_9Gbcz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇻🇪
ویدیویی هولناک از لحظات اولیه زمین لرزه شدید روز گذشته در ونزوئلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95874" target="_blank">📅 20:22 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
