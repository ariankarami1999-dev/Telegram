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
<img src="https://cdn4.telesco.pe/file/vz7bcqj_oJXVCfvEPmgQELfxh4t-5QdLg4VcQ4emrlDbWIfuZX4Guzy3wnoZ2_qBKCdoJ_XkaEaiElq4d-lSZxiitRSNIJEZ1tNz9CCCyQy_MNbii1XfO9q4UbABREeYT0TbIijW_iEU8MZx75RiSFutgPju_glLE-2p-tFaDrdYg6q2eDk4bcCpsqcDdi63u_jnEabHngR_SWm3zLbgTJKoXHxT1WPSdglSu3O8Xt9cJRgcN78bGLCSfwKdrFc8ZSFHHs1tDviZB3M0EZ9gwbx3sGACeHw3SNJZ8WWic8CG1hX89q_7lKZO4oNihxEASCFf33Qq9koXB4y1C8xjpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 471K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتارتباط با ما:@ads_Persianaaهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 02:50:38</div>
<hr>

<div class="tg-post" id="msg-31534">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fshSOYsX8VS5xLJTqCzfHtXmAXPD8nMrHxwVs5DIINZxJ4F9l-YG1qF-9FTULM3K49cAzWrzlBnjTvdpZKTyLK-s5j9b1kya-7UvIoj-hOTxQn50BLSmySNA5tZjAyUS9xju47a9NvB7bS3lsxaCXy_QhdgR9LL_BExc0nLZ9IP33UQkfUJxgUVwCNBoHszNWjjiFpuyZbhix0Ev61b-lsrLhMp63FDcek-iGR3nmn0ukzXgp57j3zjjNrZEyhcYqEUijF9SrL8oAdZnx6BrMEBVGIh_wKOgKrc5XWlBS5DDLzRwzoGBbIilejOe8wXVIk-UbwlnUPCtc9_OFy6H4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پنج مدعی اصلی دریافت جایزه توپ طلا؛ امباپه بالاتر از همه؛ لامین یامال درتعقیب ستاره فرانسوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/persiana_Soccer/31534" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31533">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot-2_i2wK4qd075cDtNBXU_aTknR334rItngV91AsJWrtBM7uwPAHviAlLa7XrfRjRsCnfANMxR1CUJ1HomD8VWyQwr9ltN_LFvkxW6MfYBRAbNsjKVGp4Z_eB02eYhtZoHohPeky7oXlzRCHP_Hp1MD1693bao2ypUutFWA4G48-lt_gu32b6vD_L46jgkUuCbBBzMSxqZfO1Q2zdKhtrdC3rpjdttzVNtaqHUnyw_jBnTobaBe79e6VtK-c7LmMniHBySau2kNpwiI11aE_Q0jstbDSR1VVmpM1omVh7x7Zt1aZwuND4xUBsKiwtgHY9Ohw2p9315wItomuNfS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ نخبگان آسیا در پایان هفته دوم رقابت‌ها؛ الهلال دوبرصفر السد رو شکست داد؛ شباب الاهلی در شب درخشش سردار الاتحاد رو در عربستان شکست داد. آبی ها با پنجره بسته در رتبه دوم. شاگردان جوادنکونام دوازدهم‌جدول‌رده‌بندی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/persiana_Soccer/31533" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31532">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBussiness Account</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX1_KnwBeFrJS0P281G5ykccQOTGBP9eLOYbXzPXY-sMrviZA1FtP2qLbP-GVmFpJTSm-nzl0bzSIGNHuvWjv-HsGqXnpIOD5JmoBjouOPwklzSybgcwW1lqs7pKCVklO59hs94QByBc58wCcVI4r-bONY7TVcGWwnGto-OKZCQ9nmcEPo6SvWK4-le6fgvy1BtGdtcjLjntvHkPPrP9_ZhJC9iimYurJMpTpb-oZAqZneUjCsw11G9Q2W-Br1ALdLXEcxZuwJzwxRqnPq64RV50Ac51HY2KwLxIdEcsXF2WffANv6huqa00uYzQBcUEkPOPkjJqblOBWECAXu-AKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
‼️
تاحالا شده دلت بخواد وارد بازار ترید بشی ولی علم کافیشو نداشته باشی ؟!
💵
چاره ی کار اینجاست!
یه هوش مصنوعی اومده که خودش بازارو تحلیل میکنه و اتومات برات ترید میکنه، اونم رایگان !
❌
دیگه وقت و پولتو صرف یادگیری علم ترید نکن، ترند دنیا الان هوش مصنوعیه ازش عقب بمونی باختی!
⚠️
بیا تو این کانال نتایج رو ببین خودت:
➡️
https://t.me/+gaXi_cMYHks5MDA0</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/persiana_Soccer/31532" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31531">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVqdkZNVFOWe2jBZ66xhhugriOYm4c9M8CuEvdKYlOECydVJPnFL6EtzPqWErPgprj3aCnwApLtJO-3xPqCEypp-TkEL1WyormQPMer999C_lf0BHM4ZfK6umNKGhLXkyJICH0mOymDtJ9N8erVu8jI6WRZspwNIyA7bVMT4158HfA0bJe0PrTZu_M3itnoRxD2Q4TDIK8P7j2D_OE6cq7_chztkJt9EZUVU4Ta9z0dkATsfXL8yxXc6CmQXrZu2yz3EIQ9LDIJniWwlnx_2GbFZq5No62dPtau320hukqGhp7b9U-NRfMMZEYfsEmb2V6Pq3EPuR7HJQKAdkrbnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای امشب هفته دوم لیگ قهرمانان اروپا؛ پیروزی پرگل بارسا مقابل گالاتاسرای در خاک ترکیه و شکست تلخ شیاطین سرخ برابر اتلتیکو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/31531" target="_blank">📅 00:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31530">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📊
نتایج دیدارهای امشب هفته دوم لیگ قهرمانان اروپا؛ پیروزی پرگل بارسا مقابل گالاتاسرای در خاک ترکیه و شکست تلخ شیاطین سرخ برابر اتلتیکو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/31530" target="_blank">📅 00:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31529">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoKGoe9wNgsTYCavQUltQUNJJqQG7mvNjzn-WYBWHdx8aBS_wzX9CxjDTOsQKI9_Ki_sDSV514wQ8ELUJUsPXVb2lZ6MfOisCmhKdCr8eoRgRKE5bx0MzJLFn9TVLqYLdLmnffELd6CE9kpWtVTZ5W9-2Yj7UF_4YXo28GouwpBMBKEG-rJZeNrAwyN4qeU31sqEsUQk9vSscZYaTqKYTVjVKhO8nHmqgMzUuKjJL3vE3YEovHefDefBr5k4YAPHqrPBPxJ-KofZLAMeQAp0hg8-Xms0tESman3jKCnhgvIf67H8ursVg7Q_Z8BWKJqWb5g1M5VRGV2ljSyD18XiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌نیمه‌اول‌مسابقات‌امشب‌لیگ قهرمانان اروپا؛ شکست یک نیمه ای یونایتد و بایرن و توقف بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/31529" target="_blank">📅 00:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31528">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECpNSFFCdEyyb0Qrc7qnnqSc7McKDDX0j6e3naBJ-YfdR-3SF5SSRrBs13ZofJCN34Z6vwlMS4-fEeBYBv3tTzkIj04tLNGHtJ01NhKzX7pmjLIUEgx0e2KNO0jNYPWOOM4xfHM5mjOAS_9TjU3Aip6oeHG-2XTiJHcX7qz5PDw-rBFo94CQZmnFTUykkDzxf-9v7-fgGXz9diGYHRhVq7GxUKDSbWCluu0zofJPzR2rU3_NWSy3286PGh3Dq8c5K32EOsP-nBo0HbzQMTl8zGeL_nsBnbRDwdFEtSb-kKDjd1MdMU8jaHqNMjKA4QOIvbV-p2gXrk3Ck8hrr4AdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/31528" target="_blank">📅 00:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31527">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZChFh1QI_0tiDWJXtYalQ4GXyBe_h8UZMQehZoIvaiZf-amgPFcHTrwimGPCbWSpI8YLI57fbx3tnl24UYYleWGT0DOcDczcg2_hzo8VUbAZIO0B-Iz9PyMNRDgr2wV-TBb-_GlMyEdVpn4egvicCiAX3lCdV_52crLxeyoZ5zj_aVsoeslKvo_XqKiHfEerKezUwq28fXVha7jFQdBJCgUZdB2qYa586HtjyGqYbLkSeQjuXns2xX7l5ImwemE9jJ-M8pGRfhSLVGjF8sTq-NpYD5lq6qu9C4LkToD9v3l6zhbmriUse2W59TJsX2_qf0MX5K1DhZaqqeXQzBZ2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قول حمید مریخ ایجنت یاسر آسانی به مدیریت باشگاه استقلال: در نیم‌فصل یک ستاره خارجی دیگر در حد یاسر آسانی برای خط حمله خواهم آورد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/31527" target="_blank">📅 00:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caWsmUbdXhqpgJ8OTUAVA-4Ocnv2V2G3c-p7FcJcoShlQm7WEtOirr-CDwv9vMgbq8rdBNJNtecut_HKRR0yqwHpvrHHlh2o5rgbL91_m4hYX2A4mnS2adtb-LZVAwGB-XCX4f6HmKlCqC6cW9l7ohFMzLPfz54TNF8KVCB4i7Mh2xwKyP-zM6nIadz9fII53RA4e_J6-430lxGbqcox57JkeUClyX8emIrd6JJalQmkI_9Zwf4TjgksT_xsnCQt89X-cvbOJa89GpZpThxwrss_7OJztgwd5hIIydJuHeetXDRX9KbAKz-rR8q_ExUeYB31T_VgWS2JqfeFYEwEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دبل‌ تماشایی‌ سردار آزمون مقابل تیم الاتحاد درخاک‌عربستان روی پاس هوشمندانه رضا غندی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/31526" target="_blank">📅 23:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3UsAJ_mHJ8A94_6Yn3V-e8qP4b4w7lGJj9w6aUIBM1T1wSRhTbb2LSX9eS4PVJX9O7EEqwhhf_tqSt7h9LAdtpbosZD2dsJXu106ULK89t8talorcnr5epjDKr2S4saCBCTCdPyj8ikHTFOTTjOmB5nXbvTYLyKoQOrBWMwlZcKqCAkn30MKSAq4ckeQWdMxq-WcYhE9EQ7VHidfWJcl9CcWW8D_h942_UPixUmTacHTKHSRE4-7nOfGS97c4n9A2561XgbPP53uTafDOE_Ynti6_1kMNGBE82GtwfFbvSWd8BudWgFTJQBsiijlbuk9NeSy0a8Yl7reQnJ0jjHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/31525" target="_blank">📅 23:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO-6WOfWYLtyWlEJ-1lL9lmnIlxu-NPNKq7bPjKg2Awv8wsx7D0Jwtdq-L7SrpWT4XUur6sTBfTKXTCbtsxIlB4v2qP8SmamAismRLlH0v8KP3T891xbbsUpw9dV0M2gI6E-luHFtAunBW6ZKocM0Qd1cs3UfCIvDBX2S6B9NUtcWRDKBKDvmHhijkJAXUFkUHu6oBPX2iAIxwEX8gF7LZa1aIVYHYFwKydS4Q_vTfy6VX51onPH1D7MGe452ccwdkC6LAaoBcj4uHegrhDWcs5Jucxr-GDgLIZzxkAmwvomxw6v6caBoIPl1AxeGILnX4J_ML0Jgi_kvbR48Nnxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس در بازی فردا با خیبر خرم آباد؛ تیوی بیفوما دچارسرماخوردگی شده و اگه به بازی نرسه به‌احتمال‌زیاد اورونوف جایگزین او در ترکیب‌اصلی‌سرخ‌هاخواهدشد. کنعانی زادگان و ایری نیز دیگر غایبان پرسپولیس در این بازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/31524" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31523">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e058158de7.mp4?token=QsVYl_Xp_YjKjnyUEp8gAZRRge7Nu1wYySgkOtYWTv30868WTYBSAB9poc25_Q7Wu-eJC6jGjh2UXFgZrAFN7ZXWkkdplo9gOEFo6nRp_p_56zhmcvE2gSoItiNoDa9yX5ajhU--p7AKuyIqMhi1OqyCBNFE1GEdYYUv-1YEjV_shTeLK4Rdadq2R4XFxocjTOYm4-8eOll0oS0KWCJ6lNVQYWLatI7wyj6Dhhw7lB3BUhCCj9b0SJzkpITBbdAkVfXOs3h1wQCw0k48PcSYkfhQn7x0BNVfXbRYTLSAx8bOf6vYBQAyG50UybGFR0wee_kpcZbDfc9r-tQ3IA_oEmCdELcUXHw6a2tPUxX4n1XnlP1i1BxC5Ma0a30SRnyu2ExaFJ8cypMGbahvQwAB7OztG9i-As9rTYgIyeid_uLZOX88w5SQvYApR5x5Sn8CzP2qbhQtx3qtBntbGf8ldWUmCUVmFbl2XMWBM17NG5ayFKYUmV7L8Y4qlqpAprPAqz6stSWGGBYNwG0B3XWKjRahRODHiI0_KDKZ2hRQr2RQpAC8OAR0cq1i3iJXaYvhPgIlN4IQZcZctOsD9nNoTnCTpzWvkFR8fFVWzBhEslLTQKmx8plBQr_ZNYYBa8sdpF84EyvbvtMA3o2lVqxx2izJ5ipI7z5fWBsniIawSVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e058158de7.mp4?token=QsVYl_Xp_YjKjnyUEp8gAZRRge7Nu1wYySgkOtYWTv30868WTYBSAB9poc25_Q7Wu-eJC6jGjh2UXFgZrAFN7ZXWkkdplo9gOEFo6nRp_p_56zhmcvE2gSoItiNoDa9yX5ajhU--p7AKuyIqMhi1OqyCBNFE1GEdYYUv-1YEjV_shTeLK4Rdadq2R4XFxocjTOYm4-8eOll0oS0KWCJ6lNVQYWLatI7wyj6Dhhw7lB3BUhCCj9b0SJzkpITBbdAkVfXOs3h1wQCw0k48PcSYkfhQn7x0BNVfXbRYTLSAx8bOf6vYBQAyG50UybGFR0wee_kpcZbDfc9r-tQ3IA_oEmCdELcUXHw6a2tPUxX4n1XnlP1i1BxC5Ma0a30SRnyu2ExaFJ8cypMGbahvQwAB7OztG9i-As9rTYgIyeid_uLZOX88w5SQvYApR5x5Sn8CzP2qbhQtx3qtBntbGf8ldWUmCUVmFbl2XMWBM17NG5ayFKYUmV7L8Y4qlqpAprPAqz6stSWGGBYNwG0B3XWKjRahRODHiI0_KDKZ2hRQr2RQpAC8OAR0cq1i3iJXaYvhPgIlN4IQZcZctOsD9nNoTnCTpzWvkFR8fFVWzBhEslLTQKmx8plBQr_ZNYYBa8sdpF84EyvbvtMA3o2lVqxx2izJ5ipI7z5fWBsniIawSVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت‌برگ‌ریزون‌گل‌تماشایی یاسر آسانی در بازی امشب استقلال‌به‌الغرافه به‌سوپرگل‌خاطره انگیز آرین روبن در دوران حضورش در باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/31523" target="_blank">📅 22:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31522">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUJGgzbtjfYcHYg5e9EtwuOoB_b9VaBMvI2wLPLcD8zmgHGv28hcVl2LBsWkq4GRznzJnkvIu-oPEm6NLuR7nle_mWND2qRhsebrKeTOvmvueQEPg2GkZM_6eVJqKKUgu67rG-C4TOXaAg4ggvR4LtkS37CNo3FmLJjREtXnCzsgp5sTkrp4WgEPtOHy6s186UnyXGZpaKFjx8xH1eKOjG4p_ZLHHQd_FytOp4AzCMLkvTkXo00OnIH09KbcRTFsjJkm9dPfL3H0t814EfBdWb6ASrpQItasdVU0M0CHe9JmDlGUlqlMyc_jTo-UXH8K0bqfW8mp10Izxc_t9b-YnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دانیال ایری مدافع جوان تیم پرسپولیس که چند هفته به دلیل مصدومیت دور از میادین بود در فاصله 24 ساعت تا دیدار باخیبرخرم‌آباد به تمرینات گروهی سرخپوشان بازگشت اما به احتمال بسیارزیاد در بازی فردا در ترکیب فیکس حضور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/31522" target="_blank">📅 22:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31521">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=dTwiSrtqih0oyKdcTZ8GszxnuzPNXzJxsVKZp8FeVBGQJw4WimYNpAt-u9Sz0Xk5xoOYYcBU8RCsjuUZXZn28MZ45CIwxROyiewPdNmyMXp3NMnrUdjKyC6vDTlfUBbJmqBu3inWTFHov23trCFPJFtmHOTvM8_fP3YtF093IfAyjYrAOCX7wT-QnC6QiDnPjTtFUht8T0xQxE--dnq0C7q8t7BaES4dK_Ywxa_Q8LaasSkMuz1t-jeTpssUQ13ye0dAHeQlOhnHF-87mCFjJpA8vDSTa8uBhzgwdgMQ5YOcx3ye060GCkA_VQV0CtRU0VMCBepdoeZFZTSRUnj_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=dTwiSrtqih0oyKdcTZ8GszxnuzPNXzJxsVKZp8FeVBGQJw4WimYNpAt-u9Sz0Xk5xoOYYcBU8RCsjuUZXZn28MZ45CIwxROyiewPdNmyMXp3NMnrUdjKyC6vDTlfUBbJmqBu3inWTFHov23trCFPJFtmHOTvM8_fP3YtF093IfAyjYrAOCX7wT-QnC6QiDnPjTtFUht8T0xQxE--dnq0C7q8t7BaES4dK_Ywxa_Q8LaasSkMuz1t-jeTpssUQ13ye0dAHeQlOhnHF-87mCFjJpA8vDSTa8uBhzgwdgMQ5YOcx3ye060GCkA_VQV0CtRU0VMCBepdoeZFZTSRUnj_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گلزنی‌سردارآزمون ستاره‌ایرانی شباب الاهلی دربازی امشب‌مقابل الاتحادعربستان در لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/31521" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31520">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/559d04596c.mp4?token=jMaAF6Pr2ugUpsdCU_0sD4UD91PbD0ywsYkUuQbz-_QHMjT0Kw69EA6qZpfyXaESBNeVIxEoyjLgjnNeWJk8PlT-zfonEHec7xJORoZyXnknK8iPjFHvuOWcwVlmicesH2C3eByp4RKu_vdyBOreyfX0FMfv82FD5-OymeaPTcxXdSvzhCOvB1PF7sFhcLCE5ddT3dwkyC-wongb7NGCf8qFHE1JO5r1DYZ_cvOdYThnkeiR6LiSHc29DXcR5VfVmooIShXy3fmA0gvhK8dn8Si8rOIh8AoVknjbnZGGrgg9usg74z299GVI6ic1wvcJdN4B6B7WIpH0cYDRFTgk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/559d04596c.mp4?token=jMaAF6Pr2ugUpsdCU_0sD4UD91PbD0ywsYkUuQbz-_QHMjT0Kw69EA6qZpfyXaESBNeVIxEoyjLgjnNeWJk8PlT-zfonEHec7xJORoZyXnknK8iPjFHvuOWcwVlmicesH2C3eByp4RKu_vdyBOreyfX0FMfv82FD5-OymeaPTcxXdSvzhCOvB1PF7sFhcLCE5ddT3dwkyC-wongb7NGCf8qFHE1JO5r1DYZ_cvOdYThnkeiR6LiSHc29DXcR5VfVmooIShXy3fmA0gvhK8dn8Si8rOIh8AoVknjbnZGGrgg9usg74z299GVI6ic1wvcJdN4B6B7WIpH0cYDRFTgk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول لیگ نخبگان آسیا در پایان دیدارهای امشب؛ دو بازی مونده که السد فردا به مصاف الهلال میره و الاتحاد نیز از شباب الاهلی و یاران سردار و سعیدعزت‌میزبانی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/31520" target="_blank">📅 22:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31519">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDM1uYwjBQVuQIIpCqg_a5o4uzZPhygBAW4wKd7WPnkcs_t2NFerAj8olyykYrkPbrI1s59NAynHUFn-5c6lK744-To2ucWqGg863GF03CILbbCOjt-JcV7B7DptlveqU2NM7YE6jerX3QST0T5jLxGOKnivbEr2QW1kvWMyKhtksfVEyDwCm1gv1Oj1ZLgdyFl0mewaqMSeeTVsCFTGS0F5Nl2IrMLEJ-s4uv2pCMupq9YjFiaqdR2Us9XnAD0F79rG7IHx-O7xAkdzbSJS8pcqqN9qWeRWPqFybuzwFFZ1knuOEKTRGHaOUPeLbaw3mPI6il0V9S-8tLGxFGk49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/31519" target="_blank">📅 21:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31516">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6Q_Q9fkpaXF1JALrsKNsRKMSLGmjdbrrhCtK2AeufWEhA0uQdihHwxvCCU_Q8FviO2LpQ9i0rANLgOrONn4VKJh0rlTRrZbLrw8kaPsV743VF1kBvv-TGeKU3hcBKAOqHD75W_-jhOg6cPKjk_0Fq2t1maqky6I0l8djm58eUfx2NO21ljM9ZQRT9COazelNjsMRl6ncWHHUK4hFKYdEGTH3Oho27szLpUx1FXdaQAQ6QwolD9gQp7y9oNjgYn-rFgVxglzl4gsFZzHzLJcn4oyv2TFv5rV1cerPx2ui0GQeHMh9ORCmoVaYpNNVXxy5wWmDsGDcrJZmlxKHTthLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syHdJoVZYba1KgfkA_GhVt_9cGHnYiR2VuAaBxgq4yp2crCUexGiMexaxrcg3fPUslzyvCqOFZ6QQqOLjlZQGC5zU906RcrmXx04RiDBJc6B3FigOlm82bGj3nE3NKJWW2cB7polifben17kji9ABy9L7tRE7XtZhU1eWwt_anxCL_5wd_wE3_2RAk8SZPAnpGFAMymtrQ_cJbqTEYC8Xee-PI4d7uCWspoRISl6Sx0GKHKKzFUXFjDsmPLg3e8ZpxalzB8gRp4Iw0QNLBvRV_xsw5kPSTDj2oxVUcuG2T424jTIVzaAv5jLaTKHjHaSrQJMc0Akl8MLXRB3adDMzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا
؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/31516" target="_blank">📅 21:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31514">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6YsgX5r5-A2PJnY43lXRFurMDuTVPA3tb13DfGJYtrOHsCTwt6eJAHRO3sd-IR7YgHK8myRrAm8l4xPwxSTihjuvlnPugWttkYTAtkv7oG-mvcPIiKKOL1z3RUmeQ4taEvmLWMurI-9eQFtMVmPE0-83yETRGWCZHoNbRxT-tktSn2xGA4mwnhQqyWM8psw5txiBkkgedQcBwsbM1BuIGEEq5uGUCVpfV_029Ano1buuYae5pzQF_huPY3SvcaUJ5j3VAFlvmJAAS6XPEFCNWUTmwK5GIGkWjq3TV97G7CG_DYvX6-WFJ-gZY5TtSIcJgylpV4PAUFsx3kE2L3zsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZI0HGFaR9bsiOmE3KIgZtTl5mByM3QKzhgo6b_wDQE6QPxKlyGJQkl432MdO9s5jo6tl7KdlP_siJRhR5LJRfFX-KtrEgFLE8jbYRpHpnFfD5Qk3BZrbk5zZndCbh-yoSbDl6Hwp0iFqLSHlhCHGalOK_EwGK-R10yipvnAmnR6ZhbSAAeB3xXhau9j9R3Lwq7RRjZ9oD2hTR66wct1JVOtc9R7E7g8-Q_BLTJvCEsI-tt45NKeojX8TH1k10QdQnFyynLe5FTMRRbIbUYEpjktkQx6ezlAlZBGpMgulhFp9tgE2A3vLQTAH2XS6dBskxdSmjtI8gXwNaYvg0D0Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
کاکا اسطوره برزیلی باشگاه آث میلان: وقتی همسر سابقم گفت‌که‌میخواد از من جداشه و مجردی زندگی کنه من همه تلاشمو کردم که اون بمونه ولی دیگه لحظه ای فرا رسید که اون گفت: نمیخوام.
‼️
اون روز به درسی از زندگی رسیدم که میخوام به تمامی مردای‌جهان بگم: برای موندن…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/31514" target="_blank">📅 21:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31513">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBKj4gP-LJUxJYO7Rnbr8hxWuJp1SP_ZQnn7X2bx5GPR0GNi2n5jkkDv04s8yn-8VPCsBJJJer5iMX__YZ8NGantjB1UqUxgURAN0EPk0yKIskYxPsyCBIdYROeS0HywTe-ELnISNdoaN2AK_M_uTSGo_EZAk1DgFyurL0H91Z_wJLCJOn7CUdFxDa6rAsp9Givnyp7JGht4xxKpUYZoPC9W5kqQDSd8l4SmrfKgxuvB11oWJEBjbtomNyS9Ml22VLsy_rnIOXynwpGRr_s9-SUS908ZL8Evfypl070pg1zmJSsHctDgnLOT8P__eTT_hsRoAk6wSVDtRM0LALVktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/31513" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31512">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00694d1532.mp4?token=Xd0zjmpmgAj4_1La0lr1iW2wu_h7ucd8GmeGmoggYElCHSIiUy0STJPzPL1PEvbXArDxtAvSzJIcQEUd5LiN87q71OGDxhfp4D5bKEVZa5mFMeyBGdJVJFd1yNqE4i0sLtAIfkF8--HFlO9pFGOuk4hy-gw2XqzDj-7ilzqTAY0atpyeC70GeMowSezLn4tNHoZ1uBSDyd3bNuCbcTQPQGKTr7T3O0c6Ae_gYqjeHsoRFBg1YtrbTVU5Q0P1x4JEz6IMJbMnJDE6qpMt3KpgU9ltEyvpnmnsmnAb8pQXVYmI9LtieynFL0Leeow4w7mdFo0xcgtYBJLuFfn1pTQiVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00694d1532.mp4?token=Xd0zjmpmgAj4_1La0lr1iW2wu_h7ucd8GmeGmoggYElCHSIiUy0STJPzPL1PEvbXArDxtAvSzJIcQEUd5LiN87q71OGDxhfp4D5bKEVZa5mFMeyBGdJVJFd1yNqE4i0sLtAIfkF8--HFlO9pFGOuk4hy-gw2XqzDj-7ilzqTAY0atpyeC70GeMowSezLn4tNHoZ1uBSDyd3bNuCbcTQPQGKTr7T3O0c6Ae_gYqjeHsoRFBg1YtrbTVU5Q0P1x4JEz6IMJbMnJDE6qpMt3KpgU9ltEyvpnmnsmnAb8pQXVYmI9LtieynFL0Leeow4w7mdFo0xcgtYBJLuFfn1pTQiVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌امیرقلعه‌نویی‌علیه عادل:
خودشون برنامه‌ دارند و مجوز گرفتن‌ از اسرائیل مجوز گرفتن یا جمهوری اسلامی؟ اسپانسراتونم که مال جمهوری اسلامیه. تا جایی که تونستی تیم ملی رو زدی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/31512" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31511">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icfomzqlyiU_UUCCoX9lNtVZtkGGQ8srbs2oFpPD8yGX0xQVFCol4taJA3WRlHd98Pl1iJkTqI2Frf5lPYRVK72nce52xe7UydnhvkO8l5ulJO4UmhU0sMV6iPajX08sxxT3eQfUxNJ8qQGWXwo0yjo2CZ1Ct0UmBnsM5aESgtvS4dKPFoEvpvS36dzyhFn7G4OxxpoecBz8jOhxWAYsBgGRi9YpD-zcTqdmWx3gxfUb_VhTBStxio3yT6bCo2yOt6kGmSGayKddVj0KPHLr2UnEgomRmZtn_HsNpra4SNzdAV3f1GRTihtCovn3F4JMryrVDKnRhsAcwt-O9XOY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه سازمان نظام وظیفه پاسخ مثبت بدهد؛ علیرضا بیرانوند دروازه‌بان 34 ساله تیم ملی با عقد قراردادی تا پایان خدمت سربازی به تیم لیگ یکی نیرو زمینی تهران خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/31511" target="_blank">📅 20:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31510">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=bAMPaiJT0HDQqkdeM6871djO3DIMvBcSVKPtkiaFoa0z8DWFOdPer18yWPEJ0xZhhsFn8dICKoqlVJ-YDUeJriCszp5GlBsoUlikbgIJGu5T85QTzq3z1N4yPaFAmU_HLZ--kEgBEVVKs12E7B7UDXqQZ508RKISCLhqLLd5FRKVETPbuCctAfatXrSmbh5D65wLNivupiKCkquMzyYcJ49aen-k1nHBR3boYfSqy1cTBHCZDBOq1h5haDU9r7KBCnvNlDqZ3vVO7ks2zU9NUvnQ82jr9A2FSff1It-96hiVzazAd6jfVRm7NmECELMI8IISofg96j0HrKNUqrhilw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=bAMPaiJT0HDQqkdeM6871djO3DIMvBcSVKPtkiaFoa0z8DWFOdPer18yWPEJ0xZhhsFn8dICKoqlVJ-YDUeJriCszp5GlBsoUlikbgIJGu5T85QTzq3z1N4yPaFAmU_HLZ--kEgBEVVKs12E7B7UDXqQZ508RKISCLhqLLd5FRKVETPbuCctAfatXrSmbh5D65wLNivupiKCkquMzyYcJ49aen-k1nHBR3boYfSqy1cTBHCZDBOq1h5haDU9r7KBCnvNlDqZ3vVO7ks2zU9NUvnQ82jr9A2FSff1It-96hiVzazAd6jfVRm7NmECELMI8IISofg96j0HrKNUqrhilw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/31510" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31509">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5tziIzlaMn-K0PZCM-Hg9Ek_708IpUve4hbJbestD7NbJQI0CsbKng-tSK38Cym-lKR9gCE1ztNl47HqyOCkYXp67fK9gAxG-vAKcVLmXgB5dANna_2O3PaqM4N4jw319XzxmnJ24dFolSHhdCWmvdGVETY176VmQ-cH0L39cRXAbjgYLzkw7X7dpAhP9feKVzw7mjrB21nJsZYIbEYqxQPbsywLoDpfLeEcVALTJcKxjjNMQOliBShWs0gTIsh2UsZrQRX3F9TBxt-qTQvZ9gi31zESrvUA7aSza3HhTfR9IibbmM4qKp43YyAE4ddvOGtvtdgwhcQlOt6iyLPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/31509" target="_blank">📅 19:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31508">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/31508" target="_blank">📅 19:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31507">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📊
جدول‌ آنلاین‌لیگ‌برتر درپایان دیدار معوقه دوتیم سپاهان
🆚
ذوب؛ فردا در صورت پیروزی پرسپولیس مقابل خیبر خرم‌آباد؛ سرخ‌ها صدرنشین خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31507" target="_blank">📅 19:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31506">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfxJSbDarNz_7XysuF-KHWInE38A-nrj5iXXsai9nA4u8_3dWjvZMvNiZq8LuDFtp6bn5ApDMGqsJmzHm57GzM9kvNgvIBuH-H1Mf1dagt0L2QgQczKcF1mjmwJrUh7d0ZThDhNF-la6mfbn_sfcGywJRWhs57eSykjy0kg5apl8ylMEiA8nWw7hmw7i0E3pv8Rq7sy2QdKlDXp6ArigZ4YiQFb_ZNvfeoGSamqv81cjXP5vMSAPCSM3MPphzc2RfthapWszqavROtQ6OJKjemZLHp67NG0KlMjGBGySMW3jtJK_Hl-ENsoK2korxi3xxT7MSxU5sdTe4H-Gr9uqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی با گلزنی به الغرافه به آمار ۱۱ گل زده در ۱۲ بازی لیگ نخبگان رسید. او حالا بالاتر ازفیرمینو ۱۰ گله و به تنهایی دررده‌سوم بهترین گلزنان‌لیگ‌نخبگان‌قرار داره. ریاض‌محرز با ۱۳ و سالم الدوساری با ۱۲ گل زده بالاتر از آسانی قرار دارند.
⚪️
…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/31506" target="_blank">📅 18:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31505">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkHRd8NUicoq1nAs2NGVyWfl-matYHVuHze8V2bWhMSy38IPg7F85lk9ZmdonCwrXJ4Z7GPQTYCoaIuh6guK_jIZbQOUJmL4oaR8TQ78sDw-TNF2k9oWolxSJiBYVuNGRBX10dgQ6qzne9l_faEjKIjxNaXnX5NYsv2IrkV-k-WdjVt3XTeC23-BLJgQpcwKE7Y5LnCwTj6pcVN74B6IAR6NqSQz5C22HjLVnSJA-sWtM9E4OZe21WXY17S3CG_0Gp5OUeu1dAuBXHdTKO6F9KEBCaH_YtYR5dJaIL_YD1RO9rLzQ94cFOWvoDoDKYXlq15J1XIOD3MQsOnUBM0-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در شب برد دو بر یک سپاهان مقابل ذوب آهن در شهرآورد اصفهان؛ سیدحسین‌حسینی بازهم نتوانست برای طلایی‌پوشان‌ موفق به کلین‌شیت شود‌. سپاهانِ محرم نوید کیا شیرین با این پیروزی شانزده امتیازی شد و در رتبه چهارم جدول رده بندی قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31505" target="_blank">📅 18:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31504">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🟢
🟡
گل‌اول‌ودوم سپاهان به ذوب آهن در نیمه اول دیدار امروز دوتیم‌توسط مهدی لطفی و کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31504" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31502">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW0BissLdM47ehMJwo20YLFUD9VYx9I7g9w9s3Q7GPrd2O--qaFdLsPkUJsIkQPQ5nPtJnRbQNUNlyUeF_Axhm6QDOTjj4q-Si_xXWM7TC_vgU7B-4HGTqXPP6xBpn_LQAA_ysKjqlZSuXxwgNOi0fYaDqp5nVK8V2W0E3TmUD0cjlpd95sF79KbS0x2Xcw4nWSmnO-lxmGiAJ37y-i99vGppgnb3Xw2P150zVa0ebYRer8fEHTFxQhgJ2KcfYkOOOwueKhT0l9sbjjlq-30wEcqmI_rFY4Cb72YeYFFseam9aMoK_t5nKnGvLX1axhCYJXBCp851yabaepjFIoCDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31502" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31501">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5NBCQqBwU_txYpWY9y9-yq0zPQPgKfdyhzbCqDxibYpBGrv8jYxnkLkFgxZSMtr7YcxrpnflCsKRXBuV5PJ3BnqKiMap0G8fcmOg9qN9bNzN6qQo6vNRyHEOn_RDCvwV8MfdjWrJdtXLJilxQCZTjlR5hC_2U3NUiY5GZ3P8Dy8o1eMrC5-nppkLpXTF1tO4BSFZG5plpDHNCQnhq7m93hbbXZPRuxR9mfzYvjQVoufRvX4PwO094nTE1m6zVieBP4AKttuqaglyuX3XpnzwbcL3rpTaIWbH2i7oxNXSe4QwGN6Hlgxck2ClcyenMgwo6PUCupWvRbXV3XQu7Ei4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد استقلالِ سهراب بختیاری زاده مقابل سه‌تیم‌مطرح قطری: 3 مسابقه، 3 پیروزی، 7 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31501" target="_blank">📅 17:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31500">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=SKfL0hY7LttwzcujyQ0FxP1nI_WzK8M6mfuSNAUvVkyEvyAeijeUlxYLburCulO4HsAnI0_0Z0DIochfjEPeA4dpHDDvGHnUWiWR60e-QLZDmepxj87TMoQJywOX7nNHMWp_hYmrkmlDScH4F8xMLt81919X5_69oXkihg2PMIWdajuMsuRuQDmroqB5M3OL-3gcc-jCUBPcaaKS-wAuQ7ETuXXvvcA1O7Kf4LfUnFsY1fvYbV_dkLwI1Wb4C_Dh8ba0XNAaXVcZVGdvrRLs5jFFUeIJC52F_MjkppC01saIFOgMNGAbJXDOMydIp1R8MYqFsLlkLxCjKAMTyKBRqUOGUtLjqsLnegIJXz9g0OJQ17aDzbW156jU7kXzdIkQ56puND2xpr6Y3pB2nXYyqCJVUTeFOR06hIpQxoMTx-fRgSVJ4oOYFHB_7IyL16kj7p7_j5QcQhYAkoXcdzrx355QQrXTpcvIzo3Xe5fuGbBOdsIOGg6R4ktmQDdDxPff56bMe3ky7EiSRPwx5ue_M9pcFD8HdMXtuhP0pss9Q-qMR99ilB96lWp34sYiyDJaHIGIa4Wb-dWICD3hO2P4SpGgfkD770PYluWQrq2bJAQICoL3tHrd4qZ6d-7rNy3puglQbzRmznIjyp-5uIwQNJKs23uNLV8JVqIOQ0kJLhU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=SKfL0hY7LttwzcujyQ0FxP1nI_WzK8M6mfuSNAUvVkyEvyAeijeUlxYLburCulO4HsAnI0_0Z0DIochfjEPeA4dpHDDvGHnUWiWR60e-QLZDmepxj87TMoQJywOX7nNHMWp_hYmrkmlDScH4F8xMLt81919X5_69oXkihg2PMIWdajuMsuRuQDmroqB5M3OL-3gcc-jCUBPcaaKS-wAuQ7ETuXXvvcA1O7Kf4LfUnFsY1fvYbV_dkLwI1Wb4C_Dh8ba0XNAaXVcZVGdvrRLs5jFFUeIJC52F_MjkppC01saIFOgMNGAbJXDOMydIp1R8MYqFsLlkLxCjKAMTyKBRqUOGUtLjqsLnegIJXz9g0OJQ17aDzbW156jU7kXzdIkQ56puND2xpr6Y3pB2nXYyqCJVUTeFOR06hIpQxoMTx-fRgSVJ4oOYFHB_7IyL16kj7p7_j5QcQhYAkoXcdzrx355QQrXTpcvIzo3Xe5fuGbBOdsIOGg6R4ktmQDdDxPff56bMe3ky7EiSRPwx5ue_M9pcFD8HdMXtuhP0pss9Q-qMR99ilB96lWp34sYiyDJaHIGIa4Wb-dWICD3hO2P4SpGgfkD770PYluWQrq2bJAQICoL3tHrd4qZ6d-7rNy3puglQbzRmznIjyp-5uIwQNJKs23uNLV8JVqIOQ0kJLhU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد ستاره‌ایرانی جوهور دارالتعظیم؛ شهاب زاهدی از ابتدای فصل تاکنون در پنج بازی سوپر لیگ هفت گل و در دو حضور تعویضی در جام حذفی نیز سه گل زده تا با 10 گل بهترین گلزن این تیم باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/31500" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31499">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9RVJISe2bMwbrVd3CGioDYoJYGy54GbrzCwo6JtyG7clUgMmTlDiAR9TjgPbWnbJQ6KlDvgSgen_giuGwD0FdBECJDA_MTGlKCquBrm81CNd9XgnbShgX-8Pn2r9IS7yXFXMbbqwQddrsi-12GUjVtGnox1Ri3-I4HJOIK84z7NB8y7lzicWdaykT1wcNi6G3jAfnShIaIOb30DhjnejKUJnNPTWWr68JMjMT_lzKsCsONf_KrVGND6wCx3B8rr6q5nfmQErkeotw_uDk3Ys_7-KKAaSoQozv0RjYiTMtYTygqG0BIzzqJgac54XJuamVLOj_vObhhgyiBsxpBcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شماتیک‌ترکیب‌بارسلونا دربازی سال 2022 با گالاتاسرای ترکیه در لیگ قهرمانان اروپا که آبی اناری ها موفق شدند اون مسابقه رو دو بر یک ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/31499" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31498">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بانک تحصیلات ،بانک  مشاوره اخذ مدارک دانشگاهی. واحدهای معتبر ایران. کارشناسی، کارشناسی ارشد، دکترا.‌ پزشکی عمومی،داروسازی،دندانپزشکی
پیراپزشکی. با استعلام.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@banketahsilat
⬇️
⬇️
⬇️
⬇️
⬇️
جهت ارتباط با ادمین
@tahsilat_azad
@tahsilat_azad</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/31498" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31497">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ht_6AQGXtGbIBUzpbr3YlBA9aDid_8wcxNNELPBs7Aa8tgsJrNk-hCurf5zIcBmzRRkAgHo7T5Sk0QaVeb5Yai1zuIJlaDEBCw3V-Q5GJ4RPfH4wHLV13-Dxz48aIgEaU-_Algy_0e7Coxqh-Gf1eOqRTscTbn2dz-A_-_FWv3Oj_gTXISaH4ePjm8tn5CCOhBlIXaKGEHiTkLIoWSPKhr8l7P02xb-nav6eMJKyM7T5mBXmAuTMn1hzhfR0eZe9NvgDjQrCCHAf_sIeBN00f0AfhrdK8Nqrw4U_-VqWg1DrLxPDH5uVz664Pse5QE5BmxVAjWcqdxNlDf1ZcmVY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیدارفرداپرسپولیس
🆚
خیبر؛
ششمین تقابل دو تیم‌است. در ۵ دیدار قبلی خیبر سه برد و پرسپولیس دو پیروزی کسب‌کرده.تقابل‌های پرسپولیس و خیبر ۱۳ گل داشته که سهم پرسپولیس شش گل و خیبر هفت گل بثمر رسانده. اسماعیل بابایی، ایگور سرگیف، علی علیپور،اورونوف و عیسی‌مرادی گلزنان تقابل‌های این دو تیم بودند که در دیدار فردا هم حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31497" target="_blank">📅 16:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31496">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=r9fLs98A_KgBL1vz8qPbtk-YCt9ac94fhb6-628v9JxcMBGMxfsvtGDqpzjwv2fQ3KDRIe9Ao_I5FdzFXhOcTREPaHuxYrDFJzj3P6YWFGoYye7Qni2jt0p1-t_hTpzLZptNskpDdpHEI5BCUwuA86gikO49Xz6A63yUyphE47320cFkWHysSMh1Mkyu8GhQOBF8gFPYNxggDmBUZUMn6VH9FWz9RH781R_Dh2eAiGAqjsD1CAfi-h1_SzN7fP_pi6my_1_vy-6ZFa9k_UNRS3oKLrFdZh37ctufl4yA_0_sdUMJy82o9ecFqbTXJlaqP25I3jZ4cnfsp7AA_SxGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=r9fLs98A_KgBL1vz8qPbtk-YCt9ac94fhb6-628v9JxcMBGMxfsvtGDqpzjwv2fQ3KDRIe9Ao_I5FdzFXhOcTREPaHuxYrDFJzj3P6YWFGoYye7Qni2jt0p1-t_hTpzLZptNskpDdpHEI5BCUwuA86gikO49Xz6A63yUyphE47320cFkWHysSMh1Mkyu8GhQOBF8gFPYNxggDmBUZUMn6VH9FWz9RH781R_Dh2eAiGAqjsD1CAfi-h1_SzN7fP_pi6my_1_vy-6ZFa9k_UNRS3oKLrFdZh37ctufl4yA_0_sdUMJy82o9ecFqbTXJlaqP25I3jZ4cnfsp7AA_SxGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
معوقه هفته هفتم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل ذوب اهن؛ ساعت 16 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31496" target="_blank">📅 16:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31495">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSeMs_Mawl9Mr5gey_IG4wivpFVvfuRu6MN26PaQsCP6R13gF9SBuD9CuVUH8wvp0ExbXxcEGE_OOK0D_uJgFL5Kfossadc9lcEEfMpcm4UBtqWUpdaFFVwuaCMGPRQRVoWIAns4tV6OOFuEeWJXWROlNKqVuA3Bn4cQeK4hU2KkQDoGqX0RKkhCfK0ALFsp1FXxnwLKKgWVf6CzYT76i5JDUaWkF4eaItUaW0Yede5dv5-3k2jz3LBGPuE5ZPMOkIhudFvPINn5mk1AP3C99kohn2dsLGTPYZufvFTshLmwdFtPHnAJhOVgIZiIk7AMYS-dtkBkpNvD1sTEQTCd1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ یاسین جرجانی مدافع‌جوان فصل قبل آلومینیوم با قرار دادی سه ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31495" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31494">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP-00K8cnB2psuOSFbw_DRfGn6Ka69sCesmRVIKskyoFzVyC2V2Xs63AyJsG8BEc4KFBxxX7Ke-fcI-ox-GDR0ggHl9lHWzxW8GdoKQUCIsnZ2lOL8hIIYcSBgUOV54DA-cK5t2q5X2In6yJtr7lIcCnHL2QHBPhYcaM5kGH7svWwwwtJaMqJciHSa7xeiXVhheaycDDJC_F8zTBQ9bU1cAI-Fh-vj2VIdwgyEk9jFd0__0nMdKFlsPADfcU2QbyuSnCIv87w1iqJHESyG1nabt8rdiM-D8VhjO47b_zyAP9weoRJSszZLAv4q2GoQhB6jumUKnlwwl-e5iq1U2GzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
دانیال ایری و حسین کنعانی‌زادگان دو مدافع میانی پرسپولیس به دلیل مصدومیت دیدار روز چهار شنبه مقابل تیم خیبر خرم آباد رو نیز از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31494" target="_blank">📅 15:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31493">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRTiEJ35JEBcsj8MUqMrB7vQ3SThqZC9R7qPloEbZn3zcWVhXrXaIC1Y8-RLLWf8dYQ8_5QDq7M-X_gQiwbpEQiYl7e7hnPcwwc9ECvuyVeuFvo0LsDI0t9Ns94ICXR8sSKWAfcOr32e6_vqhfph9Qwb_yWlnkzfyTWLwL-SpiojzBLftX31b8sKr8BCDN7gnNbximKQMNTymlLPl9-FK3iAVO2Bh_js6PvCoQ_Tk5ufTV5YRmDSsCN1yBZboNg4Sw0KFCaAiDDfXE9BzapZ7QKoZWDfpc3SV1YxFPTr508U6uy9aec0penKyhvotW8JfgjOUVx41nGRAxl-tFeKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ معوقه‌هفته‌هفتم رقابت‌های لیگ برتر که قراره امروز و فردا برگزار بشه. درصورت برد پرسپولیس در بازی فردا سرخ‌ها صدرنشین میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31493" target="_blank">📅 15:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31492">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tkw3plPIgeQPrIiPDHR0jcqovHnvmTfq1G9wrjuwEHKKcGLnDjhYA1QPegx1K04wl1ho65G9f_xUf-krTGjiCeoETPUFqozURZgPKxlIHLqfE1dYt9KBCC70D80RdoGTr-4awClCNowELcph0xWSLT5-RkV7jpGwyoflKFa69PQJxQIM4MZW4oSsJNjWWlYU9_6nxLq90sh1lasdWq7BlZ8YDwyNM82is5nWC8InGxpbWAY4foU6Nh1FzvPj93urTRQUxAnVqrEm2G88H8uX7jxPRS3sscOrf6kilARpRc9G0XR9bU_M-Z54Km3cQMMye6s_TEP0IVyLcRIGIRZ84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31492" target="_blank">📅 14:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31491">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmDA6G0DiNYIj7ODdPeeKwmOZs-pU1kPF1S5J-qyKYHmm72QaD3NNtZdYfzvKKroQR7ch4QzdZwo1DKFL4QKCaEYKty-h35m3Noi4IIFEcnZn7pursDG58l7puQADK8QUqGEHsJkwTkjONkGgF_wH4CwvakMEUOZESwMUB84s2N562_uxTZ1iZv2bjpMjsKE3Q1m8t1y5cJulr3VwBvK7TC_cnByeCSzZe72Cb8tMby15GyJGNHjOg1BkyZbAFRBBxR0nB9oTRaDA3MJIoVYbRFjPl3xoegtsij_eAQYtf73W8tSflJo6j_hPMPTp5PyBPeYLWuxWahdbGM0pQJDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد! جواد نکونام سرمربی تراکتور: شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31491" target="_blank">📅 14:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31490">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQPPXnggOLeOLSpKVKBUE9vSsehFOe7-PKyXRbvpBOuLfFb7zhtv5wJsp8h7Kd6eI2Nx5zf9ZrxnzqM8Sol5MyxKaGi2F5gNwe2gSMdPF5kNEEOFYDDcekYo65LrxY1IOfBjJjFFI3i0qLtYP9sETqvUI2KitUN4UZwIea3dfohqaTpjv_-pLAtC8om6hQdAHQmDvCkfHTIxk5w_Skkl2Vf3hFddMDDVTZ_s3fVgauz6s7upjnxKHKv5DgMCSGxEvpC6XXXrSMwTQcuT-5ITRz9urw4wZVQk8VDBk7s-R-3zlJboCekPHmuyP5nJA8GqSCOhSPJre0lZZqa-rbildQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییر زمان چند دیدار هفته نهم و دهم؛ استقلال و گل گهر بجای یکشنبه روز دوشنبه بازی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31490" target="_blank">📅 13:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31489">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYkp8wy57oA_ON3oOEyTCExLKC4Un7teB-ZNrUv1Yph2QSmtaVJRTSjPft9veFD0pNbAtEdl3azNXmyv2G0JPC-Qui-moBFof4xIYFTkCv7cHtqC3PHvKM2L2qHWBUQYV4h9Oi1Hb2HAinF1rDMA2yDdqC0tKaXzYlTllhR6wLWsFa7dZ0MAsw7vdtDGRxtcdCKJ3AfhFYcdEn6xPUXjtxpF1gFgnlNMVBTM2Cs5Uu9TA-T3y_gZNimVQczAfnkZCj8WvlbceLbDS5P4OV5cYi6QUZEzTFzLTmlDWQ7dOxQcWIRssPXe1m_2kulwYuimql6wl3WJkTVL4Aw3ktNt4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛سخنگوی‌نظام‌وظیفه: باتوجه به کسری‌ هایی که علیرضابیرانوندبخاطرمتاهلی و داشتن‌فرزند خورده سربازی او تیرماه سال آینده به پایان میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31489" target="_blank">📅 13:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31488">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNqoeoIiXNdDn0r1Nd0vRhDYHitheaLK5yAKILUwEEgmM44UV_7ZewxAzJTRXBpIJ_yKTORYstMqN_k-vGEVYLguIJkhYnIrpNmwbBSHH84iNb8t95gJhZGzXn-Dz7nQtpQIpcFzC0oEMabHRmb1F5OTX8hQ9cXJrrKje-qgM3kyqc8qr2YXFHirUODzdes3bgKxbguxUMeB4AFqpU0p-B8FYwkJDlbp5UXSi65nCZsRM7nuJHqW_HxNInNNtsBS2O6kC4oTYqXr0qk730ygDkTyf7xTEi1T1TxXleuBxPechouLNvgbqJi0N14babdd6DUJUiwBvtvZ6MlGEpgrdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درهفته‌پنجم‌رقابت‌های‌بوندسلیگا؛ شاگردان نیکو کواچ در دورتموند درحالیکه تا دقیقه 85 دو بر صفر از وردربرمن جلو بود در عرض تنها هفت دقیقه دو گل دریافت کرد و 3 امتیاز شیرین پرید. زنبورها در چهار بازی اخیر خود به پیروزی رسیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31488" target="_blank">📅 12:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31487">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnIJ7CMQYG5fWsk8wb1e8R3KIsvRsxW-GNbQBDRrd6rxLlN9jXfjtFeDEDNs8KsCjtBGf8bwrgarLZZQWFvLo0g0jwZg4df1YLxT6e1Sp5cKwLTznFUdslVZ1DyaXnVBOzaYMUJkhni8YaMf-tQUAp1XhxJ0XH0LF-yr7Y9ELxjPxJgASVL42qQH2xGmFf5HS9fE7OcRB2quCzxzMkV4vA--AxktxPzkiF4Uk-HHH-KVR3qDzUqLqknv_1feIgOY_LYBqQFGOhsOA7f7Tfh_AxV2M_sNr3EUNPaAYHz8CmeCYyfD5qwNR0EZPKTdFTmPPcwoyGrvzc9edAlsYGj9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکثر مسابقات لیگ برتر مصر رو ایشون گزارش میکنه و برای هرمسابقه 5 هزار دلار دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31487" target="_blank">📅 12:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31486">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz1aLDb06PS3kG17mT40wJ904c0ppSAx3roSxrJQ7uJXxjU-FdFFypHUDzpTn6yINO3VcR5n1LuUQJ00ctmye_c7nkDbkeiDizPWblDHJhseczgkBRLktw6x2_hnw4aWZ_VoMccEUbltTb0ZTZjrN3ib8uJirdNPe5VGBdKCVz5Pejfo8D40LKHjjy0_VyxbnZELEpLI4fH6e0MGePpC2R-RbYAyYGLNILRtGi_HdiEM28hsSPJEumMGTnrTx2UsSmHu6ITztCAxLhwJVhYp03HD5P6Bvwe1k_cKt4LOvtfXEw6DpwrvMB6ugdMrJMQKy23bNjRqf13M3us2b_PpDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسیرسفر گلگهر از سیرجان تا بحرین را مشاهده میکنید. پرواز از سیرجان به تهران، از تهران به نجف، از نجف به بغداد با اتوبوس، از بغداد به مسقط عمان، از عمان به منامه. به همین دلیل خواستار به تعویق افتادن دیدار با استقلال شدند که مخالفت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31486" target="_blank">📅 12:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31485">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=nop_MHysKAOu8stozIMRpC87Dv8ZPj2EDO7CinPkLMdRAyG7TwzcDdhTFqtd9zhWFJNwigZC-44zjGQQKjhoMfdDzLq52YtkX3RzzmcelukbmVrqJ_57W2ya3_jeiIYlLyHXUoJOTRRUNsm_UIczWnvjKfSgah1BnawdVf16jdRKlKwFJLoaZps0GqGb-H4ylVetMwZyQk99k2ZSc-SyNpsh7RtKGejKpo8R2tTse_GnbsXCp5qHBRYTT7JiNWzp4_jlDT4Qx8SuacU05PAgMsvhJA33PNDas8kB3GQczli3mmkYlDBNuQpAkvRsEZTPfvKQsAVuxpvwynTfMXyXo3jHxrA8jMiQjLzxzTyxL13He7kmRLuMd4Kcg8tyT61UWRwm2eCEu63igj0q7-3s-CtvLLL9siuNjkjMbXbbJYS6NjmPsqo-N8RxqLHNf59lPLy7lg3V5bSQdN4sbGuzex1fuX3FHqpsOip9Zda7wQHALGYYd_mGm3BmgZczPzQPuNCwX-08qbj4UT6SW5Q8LcP9hTnEI77Q4ntIcGFVO3u0ws-JNnhP1PEY9J9ARCoI9cozsf5ZMWjpEZDahAxOyU9ouAaMdqdQJZi-EO0ztiVpgh0lSTu91A9-SsMJIsNVNIrfMjCpDLNNLx9Spx2cLFLuj_zzVDXmqI--s2NcPsM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=nop_MHysKAOu8stozIMRpC87Dv8ZPj2EDO7CinPkLMdRAyG7TwzcDdhTFqtd9zhWFJNwigZC-44zjGQQKjhoMfdDzLq52YtkX3RzzmcelukbmVrqJ_57W2ya3_jeiIYlLyHXUoJOTRRUNsm_UIczWnvjKfSgah1BnawdVf16jdRKlKwFJLoaZps0GqGb-H4ylVetMwZyQk99k2ZSc-SyNpsh7RtKGejKpo8R2tTse_GnbsXCp5qHBRYTT7JiNWzp4_jlDT4Qx8SuacU05PAgMsvhJA33PNDas8kB3GQczli3mmkYlDBNuQpAkvRsEZTPfvKQsAVuxpvwynTfMXyXo3jHxrA8jMiQjLzxzTyxL13He7kmRLuMd4Kcg8tyT61UWRwm2eCEu63igj0q7-3s-CtvLLL9siuNjkjMbXbbJYS6NjmPsqo-N8RxqLHNf59lPLy7lg3V5bSQdN4sbGuzex1fuX3FHqpsOip9Zda7wQHALGYYd_mGm3BmgZczPzQPuNCwX-08qbj4UT6SW5Q8LcP9hTnEI77Q4ntIcGFVO3u0ws-JNnhP1PEY9J9ARCoI9cozsf5ZMWjpEZDahAxOyU9ouAaMdqdQJZi-EO0ztiVpgh0lSTu91A9-SsMJIsNVNIrfMjCpDLNNLx9Spx2cLFLuj_zzVDXmqI--s2NcPsM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31485" target="_blank">📅 12:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31484">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV57rgEVFPphJ5GGKm2UmfBYHuLK7qr2jQQwxZoGxRUmL4wvg-OzPI4wZdn2hYEYcHjt1q-IT8sJvWWlgTmMOfqxcA-vsI6PgvJ294GZXOre8miD0XC01B05hRGxgpxatcfNTp5CJyj9HGxYyIXi3jZsHa7cTTkTj6zVz086fQGTiW-wrWh5DZFvFPusMRJE5uXXtMWDwR9L9df7zSrB0gWQzp2Jwmvam8tfOD1_g-ICRtLgkHG_YcMvXvum1VKmzGYCcIwUBw0d4KG55ifMNyIZcL21BGN19OATBzWz1NMoKYNJ4IPqFpGNGCiR-7M9_tfIIGPEA2RTcmzF64azaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
با اعلام رومانو؛ دنی کارواخال مدافع راست رئال مادرید با قراردادی یک ساله به ختافه پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31484" target="_blank">📅 11:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31483">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhogDCRCIpCoRFcQWPWbiPq8EqFVl_sW7qzNCi0lh0VPHtSB6sDUlsoyrSfodOIcuQNeN-8Zy1TQOqG0fiHgjJij3B8di3bm8dVtj6cPFL_HOicr5yQCFC9TMS9WBgULbHeBZNO7zmSe7HHqYdiyayrUt4QSKoEJ2yozDkWmnHSyiZ4IwK7D20n-i-PE0SJWuRhdHPHig7Rt9LnTrOriuMY9NE_8Tmyxketm-1qTxdT0wSvEEqJ4BYvNcL5BiLLYzk555fFahVY70pgPU-0nXuQvr7BiDzh85dr81bHLgAhJQSPhMiGxnVbovkPiFXpsVwG6edeFEbUk-HC0u62D9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمایت‌تمام‌قد کریس‌رونالدو از کشور عربستان در جنگ با حوثی‌های یمن: جنگ هم شود از اینجا نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31483" target="_blank">📅 11:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31482">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCsImGHvmJvaXvh3mrNAyq7z7ou9vfrZztFWTRzVrjSboKdwABh04P7V1pS6sBxai0CDdEF0zxM1XEJ614sJYPWHGfqKIswEQcq0tgtEh3aC-hiHtPM7cs7iIzhIdkx5J7COlLGIaHDb3BnaScrv8PJKEE3GseIMQMo9LBvID_tTLF1xkMP5lq_Gxpyt3JYBBRAHprIQdaZz-k100JwIN8Ne52tpzoRdQi4ngyUTQ2nd3h3yTjBcPJ0_yvGHEDXjuVwJgovhCiOIJBL-lkEj08iw2yYJ4q-K8a3NdzoMfVV8i3YCde5wudOcMTl3kN1SYQ78io_q_fTitFmmCK9c-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31482" target="_blank">📅 10:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31481">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvAd1Dn_ZvTdScoR6Qp-F2KtE8E_qQszPFSCKv15c3yYQ7wJoHj2aBU9lN3lbAGdEBiZjcYMfGGYwPSHFBXYWVQlxrCv6pDB6lxkYl0BqyXS3hKcCyaGcENLTWIFNxLpa-OdSbnq_FMP42H_VEQKZdWkXQiUdl8VoDyGQGB6hdPzX2hn5m1pml9Z_dILSbnlnu9eyVx1xtb47ECDzuP7XzzCsRSk12ioSjG_RucanM9-Jv3_rZFWUkdB7T9UTwk-qEzHs1xCoAFAMRUPTL4Q-1VLexEAmBHEQftSgHpks8AdIxPPhWXTRpYqt7u5jm7eVE39igqZb5fmFodVNjP3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
برنامه‌مسابقات‌این هفته رقابت‌های لیگ قهرمانان اروپا که قراره فرداشب و پس فرداشب برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31481" target="_blank">📅 10:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31480">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtbJe0wA1Xt5PXlEKrNUAKq89RP_gLyhjyG2SiLNQco8AC-afqlPWDVSPyf9Fp4qPraJ_YbSGTIpKVsFbpYMOWMil8x11zzeYR8svhqxpg9-5cICljwGGWMVhiiKH_q0n-x5X7jJTUW55JsyAGjZBDBuq2SNW3Z-sbUtexJsfnrIe2qkj0l6rXXAtbYMedpc-10gZOXuCR2Sx9JaVIsZGsmPePVaSpZiJSDL0V73qSz0eYSPQ-KMmrYoWoliIhpfz-z5kO8iVRq88tvD2ArzHf7JaNRpBMdjdZjPPWqnMzjfqp2pdgjgdNGG7wJ2vU8vm5wP65I6S9sP8Z6PVzw30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
👤
سعید الهویی دستیار و همه‌کاره کادر فنی امیرقلعه‌نویی رسما گفت که مهدی قایدی بخاطر اون مصاحبه‌اش باامیرحسین قیاسی خط‌خورده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31480" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31479">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxmKPIRozj7-og8dvvD3pg4y6VsAqeoYthB_XDz_Xi-hlR070EfxQXFcqozqf2ZbjlLMVNwzr9-R4Mc76-u9p8PbKiCtwhTqlrTu4mfJJev6tZoy7oPDwW-EcY2Su5y_rov-OmclW7eIpK97j9xaAT0ZcgqVRgAqWo9Z97UT5Hr_VbSWDCONB5jektkDPlI88rb1XYuTn1W07mgY_XKqVxHaGXauLMAZmHHRwhWg-fUCRZskHC0O0m7dos5yLv72bYd01_y1YOA1RZOqxeRD9owYtzlvNq_Pw6P8KLkPhRhIuyIdsURzCyzGgXMm_filslbLjcElg2-Mis-kO7q20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته نهم و دهم رقابت های لیگ برتر که قراره از شنبه 25 مهرماه استارت بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31479" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31478">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY_eJ1EYO8WYeDXoZq43obR9TrPL_hEyCCLS6gdyUwoF0MgtuA2fsfbj_V6fVEtjULXxq8Vz8WKzznA9kFysE4J6osAq7O2xmc_3WxWiq5nsE7MlhhkI5ia2nCe1fW5vcoh4HNGATHCQdkGRdDX7_IE0-qW6K7DdnEEyahhkf6VMFFVQhKOThglqoJ1uVGyXBOUC9Y-ZrdBrr2SVysKW5z1_VG4My-U1VLWHArhkKPNO50DgDIui3yHDd349eM9Vx9DI7ieXUoLJ1ZwhXWw9lw7KPQBIMWf8oSwqEjkukCvJfmVkoo6k-4_Blx4NCSncPgPm8EHcz7ck0O_k8o-gKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r21
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31478" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31477">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=SrPgG5TyfeR5ajnLkaJnnjjba-V6T7d5aA6inol5P741F22ARidLy7OesffDRhoPH2PZ3TKVPN1ko5CWeWXYRquCz45FeZVF_hji9v9fU79FfuQKvz2RK2pOe35s200fCK601sbBYu2FI23vuR-WrgtyKtvnGkauC6fSKHYIDy0Xu4RJAdw0lQ48k5AUQPnQFIwEbvIRWvA-2H5UrJCitexoNj-g6Xhh3eVAFi_9mhF_kbs-S_wCyGyb03Ks_uWowPt9z4UXtPn1-VuxqsWTKurEzetX6XqlwIYExI1uA8L_vvbmqK9suSPQM7wL-Ga7Oc9ZeKtx_-Rawpljtw9IVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=SrPgG5TyfeR5ajnLkaJnnjjba-V6T7d5aA6inol5P741F22ARidLy7OesffDRhoPH2PZ3TKVPN1ko5CWeWXYRquCz45FeZVF_hji9v9fU79FfuQKvz2RK2pOe35s200fCK601sbBYu2FI23vuR-WrgtyKtvnGkauC6fSKHYIDy0Xu4RJAdw0lQ48k5AUQPnQFIwEbvIRWvA-2H5UrJCitexoNj-g6Xhh3eVAFi_9mhF_kbs-S_wCyGyb03Ks_uWowPt9z4UXtPn1-VuxqsWTKurEzetX6XqlwIYExI1uA8L_vvbmqK9suSPQM7wL-Ga7Oc9ZeKtx_-Rawpljtw9IVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دستور محمدرضا زنوزی مالک تراکتور به حجت کریمی: قرارداد علیرضا بیرانوند روفسخ کن. او دیگر به هیچ عنوان جایگاهی در تراکتور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31477" target="_blank">📅 09:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31476">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=m5Kp-5IX3hA2_SKFoto9_yDfrrLQyOtm_pboZIikRB6JcvpandIG9mKaI14T7N2CBds9QbHTZtL2dq7QPbX2eVlG63MspObkGeW1EHDuG2a7eGW_2jAcvcsA7d_c9fb98icNQR5kGc1zaZBdJPRqIoTqbm-F4kOq_pfYR15DntaxxAML7hzOnLoJsmHjm_JNZiwsWHj3s__q7P3ZbdLRtE4AoMMF8SuUhkQj-t2GHiCBDDbXkMG5leRRA_5j77mKrIaqKdE7-x5kzD09JwWzj8ZakE7VbVCK6BsY5xQZLmQjc9_AO6f-91kw9oy_4WqcZNty62GUP89wf2spFG5MCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=m5Kp-5IX3hA2_SKFoto9_yDfrrLQyOtm_pboZIikRB6JcvpandIG9mKaI14T7N2CBds9QbHTZtL2dq7QPbX2eVlG63MspObkGeW1EHDuG2a7eGW_2jAcvcsA7d_c9fb98icNQR5kGc1zaZBdJPRqIoTqbm-F4kOq_pfYR15DntaxxAML7hzOnLoJsmHjm_JNZiwsWHj3s__q7P3ZbdLRtE4AoMMF8SuUhkQj-t2GHiCBDDbXkMG5leRRA_5j77mKrIaqKdE7-x5kzD09JwWzj8ZakE7VbVCK6BsY5xQZLmQjc9_AO6f-91kw9oy_4WqcZNty62GUP89wf2spFG5MCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش حامد لک به صحبت‌های بیرانوند علیه علی دایی: طوری می‌گوید در نوجوانی کارگری کرده که انگارهمه‌فوتبالیست‌های‌ایران در خانواده میلیاردر متولد شده‌اند. ببند دهنت رو بابا. حرف نزن تو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31476" target="_blank">📅 09:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31475">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=U3WzLpoyKEFvgxhAVRgchL2T19DFhcF5dQIysCcATlmf7W6WPLgsyQjzE5sg6tNJNWJZ6_4urxY9g9uoLqHJsGdFui5GbJFyDAjLVA4N8u0Qu5hbji6Z_f9JHU18JEdad4f45gn5DjURqeN4etWi3SGeARYn4IFGjhcY1b4Zrto03d-Ivxzk-JtEoBqund_y8URR3YwFXGxfF3qr7iS26qSCufYWYc-0g5g49m7HDKrDngO7TDR0DampfE96PR-lsSUe0OIxRYh30Dh66KQFYmt-oHE9vqgEs4jbU6hsP6_MxrjWKwTzpGuS9zeWYLXDQbirRPObfe9iTmHeML6Xvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=U3WzLpoyKEFvgxhAVRgchL2T19DFhcF5dQIysCcATlmf7W6WPLgsyQjzE5sg6tNJNWJZ6_4urxY9g9uoLqHJsGdFui5GbJFyDAjLVA4N8u0Qu5hbji6Z_f9JHU18JEdad4f45gn5DjURqeN4etWi3SGeARYn4IFGjhcY1b4Zrto03d-Ivxzk-JtEoBqund_y8URR3YwFXGxfF3qr7iS26qSCufYWYc-0g5g49m7HDKrDngO7TDR0DampfE96PR-lsSUe0OIxRYh30Dh66KQFYmt-oHE9vqgEs4jbU6hsP6_MxrjWKwTzpGuS9zeWYLXDQbirRPObfe9iTmHeML6Xvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دیدنی‌کریس‌رونالدو در بازی شب گذشته النصر مقابل نفتچی از زاویه‌ای متفاوت؛ CR7 بدون نگاه به دروازه حریف توپ رو وارد دروازه کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31475" target="_blank">📅 09:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31474">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFkqr4IGfvmxguFvqzI9AOucnQ-YWNaBVwvHfZaPK0DvQObGGc7kE15GdFXqBE5rWpua2n6zByNiAjL4ge0xcuoNZNgDX3un04d_9KFdDf8yp4H6NspwI8434zOhGFTE_RAHtpb4bxuhC9Z6-kgt_PSJpWM_NMl0I0RU9hkI25Rut3QyWNRl0KcApbufHNSX_2SwpzBVLf9-B_SY17ZgT7JTPIG42ECb6VjQWoKnGDHPvV0OHsaPJJnvPE0rCzzdVffkZMf9IxUx8W13AMHx8v1EZDyaMaOQrH7u3FxUeB3BLB0In_WPvCj8WM4Ut4afH62zwBEJTatCMGZsNyp6OTjr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFkqr4IGfvmxguFvqzI9AOucnQ-YWNaBVwvHfZaPK0DvQObGGc7kE15GdFXqBE5rWpua2n6zByNiAjL4ge0xcuoNZNgDX3un04d_9KFdDf8yp4H6NspwI8434zOhGFTE_RAHtpb4bxuhC9Z6-kgt_PSJpWM_NMl0I0RU9hkI25Rut3QyWNRl0KcApbufHNSX_2SwpzBVLf9-B_SY17ZgT7JTPIG42ECb6VjQWoKnGDHPvV0OHsaPJJnvPE0rCzzdVffkZMf9IxUx8W13AMHx8v1EZDyaMaOQrH7u3FxUeB3BLB0In_WPvCj8WM4Ut4afH62zwBEJTatCMGZsNyp6OTjr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/31474" target="_blank">📅 02:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31472">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9wYnrH3aDaN9FrYji3Mt8O2yAinjIvZgO_CvMgiSJ7r3gztqU4Cl8nnG52c1dObCRj9Gr9Ny_1LKqoq9D5PiSNWXDi6ztZlrdG-ZEixs0AaS--2Ec8hnNVMWKW6e4c0MmSVINtB-KzGKvvvFlLpVqxfgDkiud4_ayFuHqcJGFqeSyFNmxiyoHDnjBpX89OccW7YT9MMxNq54TeuMhkQhoLsknP1xweZanhBYK1XH75tpTJ8LN9qGg6YIqF-vwEpNyeNFxQCnwrvYyyqu_Wx6tXBZ0F4x3SCyftIq8Fg1JJ9ObpWSUPnd96cdj34URVOcQqDQLdp5-WsKvbrPZuncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/31472" target="_blank">📅 01:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31470">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4LR9hwjocsU-zFNf5K-NQlVZ__gRnFoAq7m2THx-JBWDNi-yU7fhYpLVtYud85UOpi40Z3J8X5Me1kYsASpD98SBNty9d78JtRENEETuoDA3Nj2i6RldKmkLasOBf0NsBPLIJBF46OemLT4gI6wO3NViYT6GBwBDPAqrVUPkrKxl6tO0xks96WG1yCD-F9OVMAcX6HDklgtRwo0xS0SDg5I_pQk4iWVPTMghLbOXuikgq8zxp1sWDow0eS07ovVJpqW8wkzYscTIvUXH5Kv_NxiPiHrsXdLJVjBvVhmsGJllNMViZRYnHWLqg0AewQBlxoUh1cSaGOWL0gIEEF9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ از دوئل تماشایی شیاطین سرخ با شاگردان سیمئونه تا نبرد بارسا و گالاتاسرای‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/31470" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31469">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxkA1e8K8RmM5JoUiVSGEJcn2xobJVs1m0le8GbbYtb8DBGTW-e9Gjrf-sFAH672IuIegwVrpHfIrBvE9JjNJIq_rcarahaR24P6cvUh_MpjOquL7uACnhz_XvevqRbYdLiHgm4S0QhoVgE8wtRnr7TQsRltlSsMU7tV3oZ9UJSWm8-YFtTLXz24DwCWmKPaxuZfMD2sh6UnH_QLfZWO_Q5cafyAn0D28vf6oe1_DTDlG4i7_AhMvfddld7uxMaPcwmmfy4ZhOOfVeL4-SKYQ_J3FjVG3T62nUhn64rXhoHXMXzcmFvhIPr4J0IhDw13Eu8D-HkFeqyLXh2l4drOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
دومین برد پیاپی استقلالی‌ ها درلیگ‌نخبگان آسیا 2027 با سهراب بختیاری‌زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/31469" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31466">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsZ6AB-TKg-2FgkRObAzOA5dBJXJctQjndufKFW05herF44wSkamkWxM3BTHY2v7UyH4pFzS1A_W0WgYJz7K-9mfSmm8fSzhBqLSpPs_YCDV507DYOuXteazAzSJewpSEmmA_YoTMhHe9Qv-ipoIWnMUoblpBZEzu_hOAue2kkCbw4wTO4afQkcAKDrp3QsvaYKd-4zV4LBH_4gj0wh4VEv8S_Z9tX3EksD9k_nrQG4N-4dYk-CeZjWjb0DaLp3DfwmYvXQ_-Wo_oPbkDDDfqKHOUU2HqDm7sxNfC2ijzzyWPXUxQg3sF7mz-E6NX94becsevX752MEI_r4GVj-inA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGF6l7TGzzmBhl1EUH9dETfI1PthvbxjX6ppVOJAGVnIy0ivRmIA_i-BtuLWLOFu8kycDZ6QG0IlydFT3abmCIoV06FciAozNBBna8TKRrmLk0EdDqZEt11d1_KI6VpUU3nXP1yIdphIMyY9gLIyibK4Tq_2Yx5Ja1JydU4KBAKCjPdRuo1sCrl-RwlJegVwCYobO_uOyg8DnLRyfApJLm1t-SxAdYlSSXqmAdAEMwVbti4njvL1Wk52fk-7zRdgTgvciOmzTjtXBMtnbWjxfMMCQkuMzOnEKwxWqXFSSYJPakZYLCVbQXoh8u57l7KGa1vXt64nOYlQ_XGeJMo_zA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/31466" target="_blank">📅 00:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31465">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxeS2_aEQuSlLntQPdHiakK0ilJ6c4zGPsYJK6x2j9m7cPQvi4FAJpUHP9pjNexRwzmEe2kiNjl_T32mGtGkoiIn2i-zQ5lg5CctJf4qtV93a8CzLvp_dmvGgmgF-e-Y0YJ95m-OWKQrrMthaMDm0i1HUneHk_XDxfOxoQ5BrFNuQ41SZxAJPs6Igzu5mNlRkX0AEb2Yw8NLhAuSR8CKxYPvzW7plpmRtpMDjSPk4xc8ibUFx3JxpGS24fBQYrLTlD6iuTWQg0fHV1sVY89o05HVLGGw0F_wqudmHlR49BWvaB9CZFcYDZWhLuLiqIKgwx3txWjj2t_Qd7PXeY0W0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/31465" target="_blank">📅 00:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31463">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYCTyZE0Q4FgsWMFv_w0txM7Va7Pj0CIioEAylk6aoo6jHupzJG6vrra8LKM1SpyW36tx4MMKSImUDyKirsvoDftEqqP3mxHGXDALlpaiqE8VzjnScPzueMywBNvg-aTxMnb3QkOfx6Feq_fCXe1nxDpa9scJlTnwX0QnPk3C3wZOAxaQOWOSyj3524VdiHCrlVUILdxAjaFWuQon77W0V9rNS4m2Hv1g_OExJsNueCLO7VltaNRBr5HmmM5R8zzILUL3o_LNF8Ly-7LCXLCYUlfWd-P1bSADeG6UBTGdAXzVu4SXkCJZaVH1vjN8Hlftw6DjA543Rg_VAKicQLaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ یحیی گلمحمدی سرمربی دهوک عراقی توافقی قراردادش رو با این تیم عراقی فسخ کرد و به احتمال فراوان با عقد قراردادی چهار ساله سرمربی تیم امید خواهد شد. فدراسیون با افشین قطبی برای هدایت تیم ملی امید به توافق نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/31463" target="_blank">📅 00:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31462">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVuXcsu_vb9LzoqufivxE2ECAB6P35fCyXtRTo83nU4bHYv7-ebIDQBE_udrTHp01FBgkTmmmC5nEg-ZVhIcjSPyt1T0cJcUgH0tUYTDI69QahKxBclxiqMdctWo1wL76IalNAidrRGq83C55vjFNYmGtgXj7yx5I9psrr9_jD9EzyiJZU8f7zyTkJ9oE2k_NgL46yG0e_hkR25_NBb6y0s0w-22y-gQld0-UsCifQDn2JKYHzooaDR-nmlhcMReSBGqUlany-geSEWZVpuyV4cPym2qwu2ns3I4t7fEHxBnvTJ5sZQEA_8DJZ7jijdwML1IMsXcovRl76WcXiCk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگام این چه خبری که منتشر شد؛ آرجی میته، بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، به‌دلیل خودکشی در سن ‌34 سالگی درگذشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/31462" target="_blank">📅 00:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31461">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=hlCYHA9_jpbZ0-KfmG3uZpaVZWiWQaBjafzSgHuHzn9G2_FIHflp29culVzwEFs_JgMVF8_pZjm0k8cWMbwV3hrFMZuKesZQZD1PKdwqW0YrOHa1r1hxPgZ9s24u1gY4kqsv2WjeG4cGpn5s9owUcd8OVj4zydCcIsYPkJgf3-xXJU70cw0QmSpv5PsSiF1wKu9yBwN7aze6GeghET5qjI9QZsoaoz_93Q6DuMwGnWMFqSu41FB8id-mX3U5PfXTb9xhRxTuY_adLgS_yfblAJC3uIORHcxadc9MuM_eTqI9ymd22Au-hbWt77dUeL5v7rLtNuE1SUTdrNHluc1rKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=hlCYHA9_jpbZ0-KfmG3uZpaVZWiWQaBjafzSgHuHzn9G2_FIHflp29culVzwEFs_JgMVF8_pZjm0k8cWMbwV3hrFMZuKesZQZD1PKdwqW0YrOHa1r1hxPgZ9s24u1gY4kqsv2WjeG4cGpn5s9owUcd8OVj4zydCcIsYPkJgf3-xXJU70cw0QmSpv5PsSiF1wKu9yBwN7aze6GeghET5qjI9QZsoaoz_93Q6DuMwGnWMFqSu41FB8id-mX3U5PfXTb9xhRxTuY_adLgS_yfblAJC3uIORHcxadc9MuM_eTqI9ymd22Au-hbWt77dUeL5v7rLtNuE1SUTdrNHluc1rKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش از بازی با گالاسرای در UCL
؛ یکی از خبرنگاران درباره‌وضعیت‌فعلی رئال از هانسی فلیک سوال پرسید که اون‌هم‌عصبی‌شد و گفت امیدوارم بالاخره یه روزی یاد بگیری از این سوالات نپرسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/31461" target="_blank">📅 00:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31460">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwQKk0s7QjkgVmzmUE5jZuoOS_VvEcPPImP3C7jz3lPkm22yOwX2ibHaZQ2Khdzs3yWDx8gbqL7718Y70ui4onopagZxG9lRVeMbHc0pP5NMqqeGdrrYBBe0xGv7Uqyj9RJ52W8uL6B30JhPslc-MH7hvNDwKYOHWeaDjDDr4KVG_5kImCxgJVpSUmwr8Ku7xPCfMdncMyM7_o910UkCYapVJkA3LD16FjX6eZEmraCD54Xtjo8xczFwXduAcoIx5tL8cDCsljxdX9lNfVAENcNHP6dI88F0aRPN_pt5BdSP26s_XEGFdZ-xTep97HmXvEQU4arRUl5v9lKyM4O29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/31460" target="_blank">📅 00:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31459">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXQv_mflna5umZLDQArrYcqZijGJksuIuzQ0OsnF6CGemY8JikOYXhkJZsupav7Ugiq03LuSS9rb-YD1cGbMMCnlSZy3N-NNFtRBGc1WTK7Q9clB9Gw8wLHI7Xdrzda-16rKqtsqYrj3DvExTIHQ9lYYC2F6hNS0BtI2wuT_S0lekXEaj_F3iwWDob5a97Ff49hsldaVRPoyavmAWV2WU9pbn8jOpHJrvXNfF5XiqNTJjzeZL08YGD4CPcS2ZEv7W5qTSIG0dGgDBX4gQvoTtPznGYBKG-FP7YaEj07z_SvS78AjmCxvQgYnzFgplBcQdZzFSfHvCyAE3yQNWEAQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/31459" target="_blank">📅 23:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31458">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P01R91hC3qlt7uZWt3XdTCAbk7vYf86R8tV0WZ1PAqCG9TrUYKnCGEAyrhKgfF36oZ_maAR6GSONoGE1YgPdwy4kcZt-Jpm8KA3VgtDW8qm4c8dIY5LPxIb_47zybLdad3k57NcWRAojubeBS44w3T8baDgw60zUUrZA7Fj2opeui76Fq2_z6Z89ADefI70_Is3NxoPu0XcHwir31r5fSdWpR6S4_GEvWRVhwqp6jFab97lM1PRIlWjWD1Y0ZtjYbmlfZfefjfY_kJChqJHA9YVhhonu4Ile1w7zwJ-Ci8ksnbmHLIX9y1okrcN10iKMWcwlSlKS2RigcSs9plwXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/31458" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31457">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57855f950d.mp4?token=uLNJ6dSKpiYhZ7YQz5OIF-T1ler3SriKr2qYnGo1ZtA3aknBnqOtrlKV-FotaplE1kJBNIj50RXBj1JpwsTmqFaiMUBLwSXPVLSRuMdYTLxitAYgh8Hu12dniIKKWNWOMdEfhhCVSJaIv4DsVoV9JEGpFV6Je8oVAy76GcwnD4mRv89JLu9XZrx8JH9nHY4plwN9D8I0IwzoUI0VlfTVgntw6LzePcFfkI0iWT76WmZYkrqlzH232WzfHzDGskDoUN4ld1OAbskzf-3j--BIOM6ScjwOBecK6eTlKE__WPCr4g77RPqe97E6Ef1Pa0jrToup6yXinTWwmy-DWI-0VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57855f950d.mp4?token=uLNJ6dSKpiYhZ7YQz5OIF-T1ler3SriKr2qYnGo1ZtA3aknBnqOtrlKV-FotaplE1kJBNIj50RXBj1JpwsTmqFaiMUBLwSXPVLSRuMdYTLxitAYgh8Hu12dniIKKWNWOMdEfhhCVSJaIv4DsVoV9JEGpFV6Je8oVAy76GcwnD4mRv89JLu9XZrx8JH9nHY4plwN9D8I0IwzoUI0VlfTVgntw6LzePcFfkI0iWT76WmZYkrqlzH232WzfHzDGskDoUN4ld1OAbskzf-3j--BIOM6ScjwOBecK6eTlKE__WPCr4g77RPqe97E6Ef1Pa0jrToup6yXinTWwmy-DWI-0VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/31457" target="_blank">📅 23:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31456">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJVbP8vcVZ0FE5eRLqohdRIP8z7A9JSjs6zip-2PUHXTHCqlc5oHWGeAc8Qb7XqjH-D6_S0tGkYiHw6CZ3Xuy3huu6QKD8NAWnwLYFLgDoG1Jr2FhjejlgGoRKT_dsZpvtFD4msLLlVgPoQg_cg3txL2GyDN_tVzyOwE1nrinwgFgZyiJNdlZz0p5oRZdCulDJhcVrA6T1dKBPrztLBoH02oYhKWmcInG4gIlMnph1eVegcuxyLrrBy9pQw9yUR3K9hkwKY0I85qKtfraFSS75ZV9rmXQXSjPa0kuCVAZdasgkJzm1HC-hXR6x8pqjD4cTwzEWlhu_eHt8wygReYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حوثی های یمن: بزودی تمومه ستاره های فوتبال از عربستان خارج میشن. کار میکنیم که عربستان نتونه هیچ‌فوتبالی‌رو درخاکش برگزار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/31456" target="_blank">📅 23:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31455">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=rg5HfGRZUOQSiZW69WYAHji0HAEYhj5x4XZMzGMWkfeXWbpMQlI_xD-nUXkHAogpE6qMyVav570jkyQZFPBt7ulLlZ5HLXHDthVhR0kbLTfEW7vAkBXIossNP1HWrlQm0bEtgH9m0sXcByPpHP5o8DxpnA4mHds7B7V7AVGS5p81NdIYFaA_tOqea0IU0GeLLnefFfUbBBvU94Sxu2kBPLcWFx_IeHxIZD3UqtStxu3K5Xd3hqDOzIfKLGpnzJS33dZ8qL2MdUJ1wWYJ-OqxhvbvXOrOaKFMV5h5ZnUGAb4-VGYmwCJY-vB7_8vDEQrsiwe158QMZ6pEOVGysHxtYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=rg5HfGRZUOQSiZW69WYAHji0HAEYhj5x4XZMzGMWkfeXWbpMQlI_xD-nUXkHAogpE6qMyVav570jkyQZFPBt7ulLlZ5HLXHDthVhR0kbLTfEW7vAkBXIossNP1HWrlQm0bEtgH9m0sXcByPpHP5o8DxpnA4mHds7B7V7AVGS5p81NdIYFaA_tOqea0IU0GeLLnefFfUbBBvU94Sxu2kBPLcWFx_IeHxIZD3UqtStxu3K5Xd3hqDOzIfKLGpnzJS33dZ8qL2MdUJ1wWYJ-OqxhvbvXOrOaKFMV5h5ZnUGAb4-VGYmwCJY-vB7_8vDEQrsiwe158QMZ6pEOVGysHxtYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
قطری‌ها خیلی زود دومیم خوردند؛ گل دوم استقلال به الغرافه توسط گودرزی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/31455" target="_blank">📅 23:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31454">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=Je5ZJL_PkzPaPGKLj6Ox0WVea9DjVhpsau26PeQSBx6D3AbcH_hoRS7oIVqFHAee52y03VORIuT5jHWbn8-j1w7va3nnadwrzxAC-97ASUCZfFM3bmEjIZChupPFk3vD1MG23lRJSsw3MSOoJc1lTVQtKgJ9hMJCS_dYHpQyx-Pjisc3WlkFM3G-LFSTwGKfzydq6ghkdwhbMf_cg7AcwDSakuGH5rDt-QXauL_yLrCiLkbSTzZHfe8xQM55MxnyTEa8_NBgCEr502O2kUyLfIoJcG2dhSrgFv1ZQvmKLOeuqO-vsfsc66TtGJ9zEI0N38U2iUlRGKJVaqnEmO8PMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=Je5ZJL_PkzPaPGKLj6Ox0WVea9DjVhpsau26PeQSBx6D3AbcH_hoRS7oIVqFHAee52y03VORIuT5jHWbn8-j1w7va3nnadwrzxAC-97ASUCZfFM3bmEjIZChupPFk3vD1MG23lRJSsw3MSOoJc1lTVQtKgJ9hMJCS_dYHpQyx-Pjisc3WlkFM3G-LFSTwGKfzydq6ghkdwhbMf_cg7AcwDSakuGH5rDt-QXauL_yLrCiLkbSTzZHfe8xQM55MxnyTEa8_NBgCEr502O2kUyLfIoJcG2dhSrgFv1ZQvmKLOeuqO-vsfsc66TtGJ9zEI0N38U2iUlRGKJVaqnEmO8PMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آبی‌ها گل مساوی رو از قطری‌ها دریافت کردند؛ گل اول‌الغرافه به استقلال توسط فرجانی ساسی 48
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/31454" target="_blank">📅 23:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=E0bkGYaF1aW_Od69xaaoEX1xKZbJDDCkoHuFNFTUBJpwBdzFxpydqJXmdAi3EjgmS-rD5X7mWX5jZry39X7HBawdfhxVpyjXd2gQTiClKBEzlBrlSGHySVGzcK9qHCsNLUmNDfEhjGzjEoPYnsLE2BVAF6c8Hvqr1sl0w6Nspk2ScW_K5LRYqXDE4Z9yqgSF442XTwHlmeiY4l2T3MY5su2xPqMAW4ZeHeqy9iFicJnT09jY_FlKi56sNKPWRSCXAG23I4HpsP_WEs96ENnQet4jcNKIUBvj3jmmcC4J9cnfKRRIjKYcMpbB8V93P7Bccq3FDk9DmIuRlOb1Nos7MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=E0bkGYaF1aW_Od69xaaoEX1xKZbJDDCkoHuFNFTUBJpwBdzFxpydqJXmdAi3EjgmS-rD5X7mWX5jZry39X7HBawdfhxVpyjXd2gQTiClKBEzlBrlSGHySVGzcK9qHCsNLUmNDfEhjGzjEoPYnsLE2BVAF6c8Hvqr1sl0w6Nspk2ScW_K5LRYqXDE4Z9yqgSF442XTwHlmeiY4l2T3MY5su2xPqMAW4ZeHeqy9iFicJnT09jY_FlKi56sNKPWRSCXAG23I4HpsP_WEs96ENnQet4jcNKIUBvj3jmmcC4J9cnfKRRIjKYcMpbB8V93P7Bccq3FDk9DmIuRlOb1Nos7MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/31453" target="_blank">📅 23:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcOTcKIjntzuJ-RlMb4X5IYln5Qp7aP8EmBWlziImb_MCQfPn8GgIt7n0dldOkLJ6FAZHg03AKzpuZD_Z4fo4y_C_31lFVU9Y18qnIkzom7ypWbAo7LevhUiK51_PrkuJ76CMmSublkgyFWkJDQzyqM2TkufnZI8vfT5TCCLCkEHu8UqtP-89W5aQH9QNZeMQoxkwJgnYoaPST8dnevf0asN_qPlJ6DGaH0tR6vPFFZ1BJphrks6YUoqlkFRSd4L6LxCU0jbuh1XhjktN8QSXZMQOed-RxHFlN72k784bGPg_hPy_SHFUFOxuD_KhyLYwrjF4hKfDjdTAHDVjVuy8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/31452" target="_blank">📅 22:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wuje6kPNsGANe-vOlMuSSUmoUld-Bthfid9C8S5ABDhtyF67wpSJgx23PZS-sdmHKLSYYgBwrkxHwbZd9GEaSB3dYbVYVYxorpRAb18fT9a-qI1CXx2ZGzEjihBGUm5q9kj_qqebZ2DHgF-vY_G4CzOMW-PTi8CBeytRmobWHBJnJYwizMfamZcB4vp27FceqlXApqCJuG8zqBnCDHcj5KEWhbr07FCVHA-mPdR1WgzFD7FqjsaWQIHe7TDlB7CWe728e6HtDXyl9BSKB5bWWHCzjFlxFZOR46Ic-gNSUBGSoPJfdtUZHpOzJVSrzMAiIw9vS3UM2m9I3-DFlAC0PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی‌امشب النصر درلیگ‌نخبگان‌بخاطر هشدار امنیتی و احتمال حمله‌حوثی‌های‌یمن‌تاخیر خورد. عربستان با این‌وضع 3 ماه‌دیگه‌میخواد جام ملتها رومیزبانی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/31451" target="_blank">📅 22:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31450">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔵
👤
سوپرگل پشم ریزون فوق ستاره آلبانیایی تیم استقلال بلافاصله بعد از اومدن به زمین بازی؛ گل اول استقلال به الغرافه توسط یاسر آسانی در دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/31450" target="_blank">📅 22:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31449">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=AKYcOToWoddxBUkdWmNNx2rXOAZ73lbQj3SFfnpTQztCBr-tuieendNkWVuuoaSRsV-X4V9_Bg7rT7Vh9ag8ivk2jK0iHitK-wX6KzYQNk2bPOyEWseuHl0d1gClCuM8VuNz1uWls-8fk63TnRgS-deQgsqvF3jZidHgowTL6tmzOcFeBKL8qbCUrUOKeYePNE_nVUORh1jodH4r6vpRTa01530m-xCzkfqum1pnGsjDAf4zSQKxOUL7TOr7Z0N2PXpCOrLquj8DtxtdvHZ0K0dl7CkguY3KeOcLWVSeNdYzpLpBhd5E82ysODSge7f1RgTa0Hr-uVVfpCkZGw9Jjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=AKYcOToWoddxBUkdWmNNx2rXOAZ73lbQj3SFfnpTQztCBr-tuieendNkWVuuoaSRsV-X4V9_Bg7rT7Vh9ag8ivk2jK0iHitK-wX6KzYQNk2bPOyEWseuHl0d1gClCuM8VuNz1uWls-8fk63TnRgS-deQgsqvF3jZidHgowTL6tmzOcFeBKL8qbCUrUOKeYePNE_nVUORh1jodH4r6vpRTa01530m-xCzkfqum1pnGsjDAf4zSQKxOUL7TOr7Z0N2PXpCOrLquj8DtxtdvHZ0K0dl7CkguY3KeOcLWVSeNdYzpLpBhd5E82ysODSge7f1RgTa0Hr-uVVfpCkZGw9Jjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک ترکیب استقلال برای دیدار حساس امشب مقابل الغرافه قطر در هفته دوم لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/31449" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31448">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=ACgKSph9exnhuzfoWy9AtuTdY8cavEwCzwj0OvI6oDa0BRI8fEtUW9EzkxCsMz8TBEl_pHjxaC2joKRw0WImfCbp3WJapvxKCdAoQJOtQ2qdLDaelnolKoPDCbtpfZj0YKwYnVoMP-NRhOC379cZwNr2TwcCbIjOY3KahwfmJMSTa29HEreuxdzMgjj_pLe_EHlq3bRUTVTpWdm8wZmnzLyEvqZ3wg9lN7FjqzY5POBCmIqcRh2kGPjJmYfS3Ex0aypeNVIJOLvYsHFB4ZBBGUTvpQ-7r9XWFEjsU7fYf5HXP2iTMxO0zjM7Jpy75OkCyA6DZn2pNdyoQ4HWybvK5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=ACgKSph9exnhuzfoWy9AtuTdY8cavEwCzwj0OvI6oDa0BRI8fEtUW9EzkxCsMz8TBEl_pHjxaC2joKRw0WImfCbp3WJapvxKCdAoQJOtQ2qdLDaelnolKoPDCbtpfZj0YKwYnVoMP-NRhOC379cZwNr2TwcCbIjOY3KahwfmJMSTa29HEreuxdzMgjj_pLe_EHlq3bRUTVTpWdm8wZmnzLyEvqZ3wg9lN7FjqzY5POBCmIqcRh2kGPjJmYfS3Ex0aypeNVIJOLvYsHFB4ZBBGUTvpQ-7r9XWFEjsU7fYf5HXP2iTMxO0zjM7Jpy75OkCyA6DZn2pNdyoQ4HWybvK5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به دلیل جنگ اخیر دو کشور عربستان و یمن و شلیک و برخورد چندموشک به‌فرودگاه های عربستان احتمال‌گرفتن‌میزبانی جام ملت های آسیا از عربستان وبرگزاری این مسابقه در یک کشور دیگه وجود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31448" target="_blank">📅 22:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31447">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=ohCgHIzz3SeYmek5DtGeBdu9UO5EaCz2iW_Bx9flLvnhASYCIKjxTt_YOZtWzXmD6-_B7wT_Zbw8Zu5X0T85vz8S2xUPIOLYXm3eRDDW_1A6RYsu9O_Vs6HbQFHOmJn0xI5SPPwvrZ80RYhewQzS0R45r8dlD45-2_lZAJJokHYQ22noWxlO3CmSr9Ay1Csow2tSPTMfA2FPvG4A6e9GFFJHF4WMFm8pbH8azMvxFFF1Lkc_dLn_S98QljF9f8uUdGRti1hTxx0RfuzR_QOlEWh5U0339786uhMtBx_okuDTUCsm93O4K5ey3AO6LxUU6-Nvw0ljaFbF-tTIU0pK8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=ohCgHIzz3SeYmek5DtGeBdu9UO5EaCz2iW_Bx9flLvnhASYCIKjxTt_YOZtWzXmD6-_B7wT_Zbw8Zu5X0T85vz8S2xUPIOLYXm3eRDDW_1A6RYsu9O_Vs6HbQFHOmJn0xI5SPPwvrZ80RYhewQzS0R45r8dlD45-2_lZAJJokHYQ22noWxlO3CmSr9Ay1Csow2tSPTMfA2FPvG4A6e9GFFJHF4WMFm8pbH8azMvxFFF1Lkc_dLn_S98QljF9f8uUdGRti1hTxx0RfuzR_QOlEWh5U0339786uhMtBx_okuDTUCsm93O4K5ey3AO6LxUU6-Nvw0ljaFbF-tTIU0pK8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی جالب از فوق ستاره‌های حال حاضر فوتبال اگه خانوم میبودند؛ نیمار خیلی بهش میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31447" target="_blank">📅 21:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31446">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiPGAfhATbifvN9-oEExXw0a48bFs9pjl7yhKhaFzWfWtFvx3nU38eS9cFSnSelfi-Bq2mSQ9Db2WrIM-1ohu-7qOvxPSRsh-WJjTW8UGhiwZ94kbnPv2f4V9osXgIztz0KAMV-2ZdtTA7EansGoZSpzM_zT8cyAQQRBtK7KBszrChw_V8I56dyBc6_W3eWnayoUR5YWvWAeSG_xS5aesNvPhWDe52ipcfTPZVJtaXy_kSMX6LAeNrR6GJkRoB0PlWx8848igmBi2y_OzDC36dV21PMR-scfOf0komBDoJFAuP--qi8h-8pYWxS2ytYJAnGdCSeZ5LQ9Q0DRtWTAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باگذشت‌‌بیش‌از 15 دقیقه از مسابقه بازی تراکتور و الشمال؛ شبکه‌ورزش موفق به دزدیدن تصاویر شد و بازی تراکتور الان داره پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31446" target="_blank">📅 21:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31445">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_HndsDtstOHbjx6OmyKC_O7wk4ZjiJCCzlhZNAxpDrmo3Tn9S0ALKvuEfAxSwOmpsf-2X_yD-bFODF9HP4TySyJdavBGBU1HCDKfNsb0WIVzqCVm6zwGpsdYeRdFcjQZ-Iu275oor7zshfpL9qye3sOSOL0OLBRh6B9VgbUbcN7aeeavnSqJcgOC2wr0rmVkyqbJAjb9aryz4tAhuHUmEMvysB9WCzPVG7eVcy0YCUfwmKl5W4_DO2OFKBVSINKbGBIrpEg5j5mZBCn8RgdkstUDvQ63JlfV07a2mBPq9mum-l-sDxe3N1L2DjE1hpC0fTLWd1b4yjQ_wB6ste3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛آغاز هفته‌دوم لیگ الیت با نبرد حساس شاگردان بختیاری‌زاده مقابل الغرافه   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31445" target="_blank">📅 21:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31444">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meZ-kbJldDz4t3-jFuo4Hkq3AIQjJfdvKTrhs9zWs1vQPnBaHKropSbumlouG_VPC311pulVL_qUWY6bd2jHokqHDbDiirATI0czuaR0Sp8ktzh6ayUuZ3QnUGr4lKBvSB1Yaxp3FVvLddrERJ7pEz8xIDI7nH51hciVKxjrg04X0mo3eQuC2RgBzCAhbMXW8W9q3bjjRAz2896EYX3Jw0EZ8NCtKNPbfSo7KI2qo_fU2EUigOCbP6kToPAk0Lu9ZXBqMGV9_jMid2F2O3_omx8JcQRCyOu2jcX19c72-Q90Z4T6NPkh8QD9-E80Tj9Xt3juj4laFcmS22xAE0LrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار باشگاه فنرباغچه و فن کریس رونالدو که در ورزشگاه بازی شب‌گذشته تیم ملی کشورش مقابل فرانسه درهفته‌اول لیگ ملت‌های اروپا حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31444" target="_blank">📅 20:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31443">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOSP9S9zyRgq3PWHkSWoWPRtguCNhfKXWnAG8_9Bl8m1lrHyZNBROI5YB-umOKmUVLZYJ0woRflCie_37eudk0s0AhnV_6gRIfwdfXEZyPbb4mMGmvWvn3yHgcNIvGpey5JOQrl-KoAh0lXFGIZwQ4EeXxqtH77vLlKsPr0T2WFUYeEChi1tQo6uYSPZte8s3eTl7FR97BzypgzbEBbj-NXuxe4Apx1iXEW26aTK9LkP-n2-x7ZIxUknzV8PqW8g_AqU8F9PQL4wo6x8QaErhCIYXHfxEUjpHbORm9aezWLtcImtsuDkkN4kRGG1a6-eeANy0PY6SBxUTMvFK0EcHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌نخبگان‌آسیا؛ ترکیب استقلال برای دیدار مقابل الغرافه قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31443" target="_blank">📅 20:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31442">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_oRckL58Q2np7Gkt1-0pgfjPd8aRq32yew7EihWXOqaFWN-NQvgKppw8wcZ5j7TlNjszDXzx9lEe5YlPIkm_Dfd5yGoUdObzlRwMfApQACFSeca4nio0NRXWpqlvIWIYigjflWqbRXsnlDahDRpM4DpDxY19CESIfr7yboTcQ1vvLKc1ntxK-ocPfpSboUsVMjDu09Dbhd3FxRUZLZOkCdKqfl7YitYFgnkWm3cznqlpx1uhIIJweTK5Wtpx_MCLIci20hPl-_OeqZZjVgY7BzdoAlLuLBZlPOMgkKiRhlYlfr7iqBZT09zMFcAYj-RE0yBijd4dwe0HAc9bjY4IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31442" target="_blank">📅 20:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31441">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=mfFzJT8yW-x49k5XaUdn8B9ilsaMUt8mpfLFGeNH0XZIQIOprAOsc_e3xWn-jt20YrVpnlnVRudGdEyy4AbsN1f1ZkePvQbohleln0yvZKxSHKkuhyNufiDu-vulC2Tbtj6_UD9smoedcFr-9IgKbxfY36rsQjGlRP8kGov8hpQ--epqDvJSA3Ik0mcH9EzahXi8ftJtsZifXL1CdCn_qC6IvRhzolLXq5WiCWlRmoxaFyQQk_lvzbonhSfbj_Jwr3oFNrXeRVsrdPapTbLe2yqPJ2QZecBBsDHeMvTqY_uzMWoe0p9t_3AOLlFKJ5-LS_DFNefUQ7F5_ypaodrmHQuHLeI0ldGbP9_NcWGrpDFkkJDMS0eMqv_CyJjb4Kmk9xdC9N9TqL_JJoFh4ZTKrHqmOpUggn-8a-4KDVxXOwa8CPjN1NLnPBvK3tbbLLVrmiOGQaMV3NHk0Dco62wAiqf28zFunpRIybjDQfwt5926TYUQMRmSwY49TgmpG2xl6JugAH-d6quiM0suW6Qq-oeJZ39YLNhauWY5jPbjghGWYMN8fQ8ATF3ib152dB_LkxZqcpEs7JGvloulTUBHBIikmvLMnlWVa9X1f1-U-N8jhtTR2aZVobFBlF3-MotmsqFT04qT2H7fvFLrtfGl_tetNUAk9seElrGbOllsyQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=mfFzJT8yW-x49k5XaUdn8B9ilsaMUt8mpfLFGeNH0XZIQIOprAOsc_e3xWn-jt20YrVpnlnVRudGdEyy4AbsN1f1ZkePvQbohleln0yvZKxSHKkuhyNufiDu-vulC2Tbtj6_UD9smoedcFr-9IgKbxfY36rsQjGlRP8kGov8hpQ--epqDvJSA3Ik0mcH9EzahXi8ftJtsZifXL1CdCn_qC6IvRhzolLXq5WiCWlRmoxaFyQQk_lvzbonhSfbj_Jwr3oFNrXeRVsrdPapTbLe2yqPJ2QZecBBsDHeMvTqY_uzMWoe0p9t_3AOLlFKJ5-LS_DFNefUQ7F5_ypaodrmHQuHLeI0ldGbP9_NcWGrpDFkkJDMS0eMqv_CyJjb4Kmk9xdC9N9TqL_JJoFh4ZTKrHqmOpUggn-8a-4KDVxXOwa8CPjN1NLnPBvK3tbbLLVrmiOGQaMV3NHk0Dco62wAiqf28zFunpRIybjDQfwt5926TYUQMRmSwY49TgmpG2xl6JugAH-d6quiM0suW6Qq-oeJZ39YLNhauWY5jPbjghGWYMN8fQ8ATF3ib152dB_LkxZqcpEs7JGvloulTUBHBIikmvLMnlWVa9X1f1-U-N8jhtTR2aZVobFBlF3-MotmsqFT04qT2H7fvFLrtfGl_tetNUAk9seElrGbOllsyQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ریا بوز، استعداد ۱۹ ساله انگلیسی، پس از حضور درآکادمی‌ های چلسی و برایتون و تجربه اسپورتینگ، حالا بازیکن وستهمه و بصورت قرضی برای ساندرلند بازی میکنه. به‌ایشون‌لقب آلیشا لمن جدید داده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31441" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31439">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq_UQlt5QJgP4EeIAS1DKsfk8TWxW8A2kwRNVjiz3wrWLJ0Cf0Fp0CV1druou_SmoeCnGrcO2d6TC2IL_I42igikEcLnZnijRwjxQEUOvSEfyKV1ZyB5BGRfHCq0rJjLDyfkQaiiHR0ucved8ApF5eLHbRAyiRwW7YrN9IyHClvdAkXd3e1HiA4fg5osffahNLF301KqFCtHNsJ82C5HKxhEcA4slI8WmIHrfj72xItD00BYIeWeWywjG1Ho7kFbrOUqtNLDrjZ7aSFpKT9LkYjT0zK0AE-DZbEcPsgSbU-BScDiIURuYiY1YnHc4kYgt5lHnfwjRkEGHI1kuS7aQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31439" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31438">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMfCQKo1aeV7u9CdocJBfL0eaJSp890W_-ZZvYfSkhhoP54CG1MUIfmjnv41lsY2GApgPl22dVhE4jVEBVTD9XBO0CFYWD8ElBpopKDD3hTD6aYNnpmtyDN-xLxxfBj7RAAPUUyH_gRDjuEMkRPdKi1252eTBwLn7th2Xv8rPXw0OYvFt7jtFibT-9J5HCz2lX-8UxmuL58M9CCC3P1qwIaTEqFRcfdREjHFlVLHYVrYK39ihkxURDJerjDEe73VJcAqxzgeRsat99TrZuMoi3d6RhIH7LHSBK4EWWXJGGnXR5pH00bh0HYJauOd4CwibniUHcL0YfBF41khiF3E_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مقایسه‌عملکرد مهدی‌تارتار
🆚
وحید هاشمیان دوسرمربی فعلی و سابق‌پرسپولیس بعد از هفت بازی ابتدایی‌سرخپوشان درلیگ برتر: مهدی تارتار: 5 برد، 1 مساوی،1 شکست، 16 امتیاز؛ وحید هاشمیان: 1 برد، پنج مساوی، 1 باخت و کسب تنها 8 امتیاز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31438" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31437">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK3xZB-eMKR5KJqbK4Cvu5AaW2sImhwJssoxSnraw0sjwlLemOtYrjUIvi_tGoVIbd0RsF3g_epJCWqjHrMPnQB9ma8iVo0PTv2RjKMOFOXGDRO1YV1MOImBr5xp4_P5kVsvv6LbyWuaDuFQEbRPnHYi0II5q_tzYAIGCgf2Fkk497GfN9PSpTgdAKBFW0gwI9IbsgGnQ4SnxDJ5aspLmqMXFVexAnsYGcDw1FjnPW9DNxdAlSXVlm5STqYMju15PRKd6ZVtpefcyt9c74pEsVq5x2Q4X3gD8T7By1-nXbd8cCXqJH4PNp2gbTUujizAi61-iFcoIxO7fZe6Ok3hwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فدراسیون فوتبال اسپانیا؛ وینیسسوس جونیور ستاره برزیلی تیم رئال مادرید مسابقه سوم آبان‌ماه با بارسا رو بدلیل محرومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31437" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31436">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGVR0ES8mKvTe0Fa1xXpRUJGUJqFVd8M6pGq1MN_JSL0l4eLegSPWHNkAJJef90jDWu8bKxWRBJmm2xS-k6zfo6d44HGjmle5tedyUAlLpKKKyoi2S3KVUBpsyaOAfEVQoQmJDUQli16Ny-tsBWaQDcJkhR4SUCGPnLOxmCD489HHkzycH6bNIJpHQ22AA9YElf1tkkihwsn-HHn0O7rcM6QpJ0ZXALcE7kVyPAPIuVC7wWm-yj_zDb5iqVV9QNj9_mO_2CN6WIMbv87FGhe0TnB7AAaKBrbgDVtLNdnGmbjoJIOc5dkcABcmyBBRtP7g8iF3W4ftqYanqxIkKoyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه از هزینه‌ای که باشگاه بارسلونا برای جذب پدری کرد بابقیه‌باشگاه‌هاکه برای جذب بازیکن هم پستی پدری هزینه‌کرده. پدری درحال‌حاضر یکی از بهترین و آماده ترین هافبک فوتبال جهانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31436" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31434">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G64TpTchIlscJmszG35HeQn_XZPPvI9A4W-HVAiKd3G5pYhN-aji5WKeDsu5OunXSWNO9Jlo6IAsrfPFDi5hZCf8cJfGD63hBidKc2JRvtsFztn3SXcfo8fRAxkgl0Ip7cQAL9jpACvOaIvT4BVLF9y3ILS5jrvgo7CSAdzKvvvjHvP08iJgacw8BaAhaFMsBeZn7tq4STuHeBhZTdb3JIFHqX14lrCYdFa0KW4z0_uPAARskvU7bZVPj-Ct3Jm-yUZc9df0Ph5KOtb-LO3MnEZyEFCPBOUtYBQJXkulWZ9z1hSSeUGzLd0MC4LE4vFTSqlljwW35QQY9kIcMBajWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31434" target="_blank">📅 18:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31433">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=nEgCOEgM7bM8dX0INKUPxV3CmZuuoquhFlpAjZcINKnbJukrgioJ1YO_f1kKAffOkhXGeONFnQHjTlO7HTHQDncyTqbOe3aPZ3naFLGXSosam7AcKvyslzGFWQTU1oGpX6D9rZD8DCwEia2ArXRaOmrbCI57EnIWaNfHiiwaaz3FYzsxS1nbT8h4QXHLndlO-OBTD86u97wVu0fuvJbn76oJOoV2ExcSor6c1e6mddDey0mlKOgFcDZQ_JM0y3Mr8GOg0ff59mRGp6GDW_8ZyO7Ifh8dXkZ4Bd0dleGQmean4mEpFL2oS6U1waIk0HXy2A-3dX2l33B1AsqUMZZ26w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=nEgCOEgM7bM8dX0INKUPxV3CmZuuoquhFlpAjZcINKnbJukrgioJ1YO_f1kKAffOkhXGeONFnQHjTlO7HTHQDncyTqbOe3aPZ3naFLGXSosam7AcKvyslzGFWQTU1oGpX6D9rZD8DCwEia2ArXRaOmrbCI57EnIWaNfHiiwaaz3FYzsxS1nbT8h4QXHLndlO-OBTD86u97wVu0fuvJbn76oJOoV2ExcSor6c1e6mddDey0mlKOgFcDZQ_JM0y3Mr8GOg0ff59mRGp6GDW_8ZyO7Ifh8dXkZ4Bd0dleGQmean4mEpFL2oS6U1waIk0HXy2A-3dX2l33B1AsqUMZZ26w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد!
جواد نکونام سرمربی تراکتور:
شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31433" target="_blank">📅 18:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31432">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2DTsgdsTKSLl0ftn7ckLGCVprC6o3k0LJ0Wk6MdNkO4SHfyuVMFV4HSl76npyzxzz6HmbSLV8kaCKxl6I07AojeEczsMxg7GwRJJpbY5YMVonOJJTkGw1mRbmPdYRG0cWzhhogjW5PH9Qd9L4gVedXLd-uesibxqkjHQ7ll-zlftRLkTg7lMEtBAts9d6VT7KlkjIGXjpcHaXdHu0s9XoaI1imx3pkRzgCCZVw7XJ2Zn6ynFXZyUxY0YlFdUy93wYVJHiMXM19FcewXuU46FrVLcTarb_LQ2J0eafyluz2nP385e1d6OGp65F-iQjJWgZntxcZVVPQ6uXkyp6bAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31432" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31431">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjSWVw3ctlQiO3Gx61Y7HXfAXRX_9wL3mwJ4HUBO4s2jrXvfSkV5IVr8sfg6MJiiMFNZJ4Zk7NvJXt8M7jIuoSTpBAQEulx35Dsri1ophmJdKM45gk7oXZwoHlyBI6kH2X9mooTIjcfBGbtKpmqmpAX8D8f9dit9VxPP7c2JyKzlecsh-5JdndvptbRAriHickDrBQ713zXYi4B7sp-CFaty6njewx674JoxFLWjZCc2yiH9QcNM8n_qeDw9ukhk_6XWRC-NgBCkXK8RQItgMh8PrIAFHYyrPlhkXv0awC0ehCvAuEgV2EK8TenwobxL4GR9TB22_ErUhUXDzsFprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قد عجیب پسر رونالدو!
کریس جونیور درحالی‌که فقط ۱۶ سالشه، قدش به حدود ۱۹۰ سانتی‌ متر رسیده و حالا ازپدرش کریس‌رونالدو باقد حدود ۱۸۷ سانتی‌مترم بلندتره! جالب اینجاست که با توجه به‌سنش، هنوز صفحه رشد قدیش بسته نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31431" target="_blank">📅 18:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31430">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpH5a8xz5fARGCGgkdzVKcVmTnIosM0TGWQY1g-Km9dv3pMb45lyx19TUdRDG_a2iyfQzfhAJLwtRXSv_d_DcNLgeKMLdgr8zApZlxSmZY6cxcybjbP-IioiCottdFpPaAXWHmkrD19WBqcHTO3FsFKj8GdzIWUqo56MxjCYqsN6foL9AZ9Ye7xI7cbwWxRys67yKtGSJDsXFTe0h9iTh8J2vt6Rhek4MPAd4Ju4L1hNHjXSHgP6Ptwmypz0VRg5g_-jiwTQCRNGj_4ffUeY9FX6YwWbEsqSGJ6aVotnbbj06KbP-IkebY8DM_9_7HMvO9PV7hv2qy7AsnP-k6gZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31430" target="_blank">📅 17:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31429">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOvr276LtYeyDbuEXIGuXV-aXOEtXMlbjNhYlrTmRhuGNZ3-eoWwNBcsZkv02Mxj_KumHorP_iork6GcUYfoeNXAahP9BuktFw6e3r9YD3W8y-AuSiMnPuthi3j03IhOHH3VcHB5pxLZch_qitH-qGYesHsg7S9ZDdm4cLSZkUFORHEIcG_vshgLeHTmj64_8Uf6OKVRXgMhc5JcCIc1g1SKvKPZ5kzfgdxgqHHquUIZcup85MS8WAto8XOW31gEUCjt3pkynCNB1zBOkuwVaORr1kDQON-PoN5ZOM15Lp1TkUFfBQeRMLH4y1m5AyGHMpHt5SdBA0CmJcCkOwn1DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخواست‌پزشکی‌علیرضابیرانونددروازه‌بان سابق پرسپولیس و تراکتور ازسوی‌سازمان نظام وظیفه رد شد و از اول آبان ماه اعزام پادگان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31429" target="_blank">📅 17:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31428">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqIfLnZhOIil_0b-Q80RXcVf47AkJlCwXoktOZmEvLkMX9CxcqZmmE8BByzPfZYDOygyDLMflJ-gPr2ggtqqEAY3ns-az80k52-cPscQqHzGNHUStVUmQG96nNfzqRYkTImtjSRBhNeVyuPjpoTWIhWHmE9TQavdb6A3Vbo9O5Mvr2oRAENQdl9PUitjaZxict_THl3aYR3Alrs-dftdShdSaNuyY_K9gSh_9LGUizi7dO3GVfxRd5PozK4z-JbntNIc5H3G8zc8F4uTlti9gToDn7yMuF72oK6-J2Hh_1s9zheJWbNjLXS-1HG6UviWPWY9ag0bW31E-xGe0dxGUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ سهراب بختیاری زاده سرمربی تیم استقلال در تماس بامدیریت باشگاه درخواست جذب همزمان یوسف مزرعه و یادگار رستمی دو ستاره 21 ساله فولاد خوزستان و فجرسپاسی رو داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31428" target="_blank">📅 16:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31427">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQ4GOm2lATz7iAOEBquManUQZyjI3sC7F2bLGbWHCalUyskSFWGAJGOhg91-d_Y2mZ3rrGgucBuBoR-7rM24tAftNnq61Bkr0F9zl40TwdmgOSTy2L5QsY6GmySDiVxi2CS82LW-WwX3MQYPhNMsZpSCKamDzBrv2Ruox6gPMPAVbCRfbh0Lko9czl3Tidohnoftot4ERZZgte-2CIhrVNdNxPw3DT7SYgj2vzxBFpyQRtFNVhYwgWeXoWzxahz5KauLyzv3P-Pjcw_dSxGpK3sMYciJq1qqcPP_55bvk7-U-1W_jbXsBVdpmF-Ku4CYKmsjSu5O2JvXY9gmELFnCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
#تکمیلی؛ کازویوشی میورا ۵۹ ساله قراردادش را با باشگاه فوکوشیما تمدید کرد‌. میورا فوتبال حرفه ای خودش را ۴۱ سال قبل و از سال ۱۹۸۶ شروع کرده و در فوریه ۲۰۲۷ میورا ۶۰ ساله خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31427" target="_blank">📅 15:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31426">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
ویدیو کامل قسمت سوم فان 360 با امیر مهدی ژوله با بالاترین کیفیت؛ عالی بود حتما ببینید تا آخر.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31426" target="_blank">📅 14:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31425">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWx_pfijVT2nwXe0YHqziewSeLHshkh4m8XjELLWOUJALuUucV5AUXF7eSBUDsfOG69iGuflngZANeY479jZFWfruXfxIer6Xkem5sbCLkELQbRMSyEsYhYu8SD7yvPBIOL03-xa1CBVcPOKoUqt-b3FvENS5YPRPeJpGjnFX0VrIgpzHQb2_TEHZmBcSen71SFc9F9y8fd5fO0M9YdX1TEcTYX1JMGKtUbTIjdkycc7vD1FIVV-U7hhuxeiZc5zErDTLoufaDGyBYqNaTNJOEnNuGc5-XA83SZqGcMlL31ct0s442TbZKx9B2del8H8wkuHliftr10GK-ONRLg7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به دلیل جنگ اخیر دو کشور عربستان و یمن و شلیک و برخورد چندموشک به‌فرودگاه های عربستان احتمال‌گرفتن‌میزبانی جام ملت های آسیا از عربستان وبرگزاری این مسابقه در یک کشور دیگه وجود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31425" target="_blank">📅 14:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31424">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEmkW6C-dIbS2H1quX04WMoK_x6pl87kLrj5ko2n_GV84QrGHFEVPUfaHTRVLPjL_tI9MfcXw2NnPgqyK_EanRmVl4fR8L2IVoyJXTn9V2oaivKpVm5qMtUZ7E6Ll7HiuoKQQ6-ABG6rRQFuojUJjgPo3pFhJq2D9LacdY932oHAVTLCDaJn5FUgP7Xxh46MA6O-LTih8MFKLMbf0dzH3ySKkC62yl2ZEOdU3Jd7sZZNul27V7P69KLYnYnv9SJtGtdQDfQU_otLsqm-sC47oR0P1817LdnnXGZMKE6zA6_Chodsp4_335OMBK8eXxPViszHNGiR5Q1MuFjwAmAPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31424" target="_blank">📅 13:57 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
