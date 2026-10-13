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
<img src="https://cdn4.telesco.pe/file/YCYF6kahegkRptXgtw0mdFGZx3gwxwrDy6DPdFJFZLR-RJPN3_9nYncmuLf6mdmqnc-7neShtQT9BdnNpePFoBzggWROH6IZ7XVe8aGOjJlFoU3jVd7bPB9pE-BQIZYVXHWRw-2CfodRl5JPGwa5b9pNsa4ncegA3_GMO4wgWxj1HP3s3EAK5BurS7AxyYBc1btEYlxIi-f5rUhr2mosbtXFpAznzcPpJHpizHAK2hpDHhn6iGnGoJt1AGR4vHJye8ZC3YkhWrTsmVeP98ELnmDYXSAOMXNq2TxXKUhOPcJZ6ttTpyO9a6L0kBucPo4M2htAfxAspUUWv8OlmLXm4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 269K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 22:53:43</div>
<hr>

<div class="tg-post" id="msg-84798">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8tJ-pLBy4Oapjxl8J_2_l6opcfbfl_zGRZyp2lbpXfl372QYbZSYlzcAkVRJ8NaoNF7HY-IV3_hwNa_DZ8jxBGJW-r3yaScGM7ZisRdBdj_-c0tzugY7rh5U0oiOguCr-7GzJvvfJAA9zxZGVd5aT6jzqlqJqnF-eXwWsW7awaQpkTSDO85CMNGJWjuonmGZ2fLx0laZGegNPaT3XAR74L6oFo-J5Jc2GubHGWFNy5BWMvX4_ncbJ7soW2C7PBhENIRuNFUMe7wPNKoxnhI-UWgmqxMf843ARq_7ijHsOovzBtaI6KUTuyy77BNWYULgyB4sKvt9qdf20DSl1pLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvr-RtfLc7MgkK3ss36oKhPze_EvP9YpRGzD4CNb6pCxIlV2vL9VckNuxuHoJJMPP_vAqNtAoUtjHxK7XmCIIG1Y0PoJyaO02LUgZ_tTTWVEjCJlNRz_rXZiyE2KF7OWkO8XqzgQjhp76F9ND_7pFzyoOvp0UhXHTeV8yWCo4DlUaGmrgERTxKKPYkrAry3486cCkcVX3ayuldV1XPMFNxJfLYS9yDuezROBr6av8r95Jy8XvaW504CHyXvlB38n3rL1P22Fsi3cs3KGXWPu-lS_EsYG56uXGmwEQ1A0XlN-WA2o22P-GIvNTypk1u_mSsprWlHS2zfkcfBV3Nb1Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی ترب دارن دم و دستگاه لوازمات جنسی مثل دیلدو و واژن مصنوعی و بات پلاگ رو میفروشن.
حتی صندلی و ابزار شکنجه ام موجوده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/funhiphop/84798" target="_blank">📅 22:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84797">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941b0ce75a.mp4?token=Ra60EUfz-4QwfW0pPSxMZEOUtmQ0lhYEe7amij4P2-HFJf9OvOZAO-n1qHjCuBmpooXHo1UL2qwi-gqqBIkGDBoQ6Iz2vNe3y7YSF_DcfzxIekA10Q_b4r3VIWDyPOfyTX2MEszpIkXgpLcGFQnrxwWNSoB3__-t8Uy2g1phsDjaj8Tuq3C23uziR_ZpJeXn1yhz3LSPM8O3daDO53_QB9jG_dptVTP5wyJzJsGCAOm0okIGixwpfdI4K5qP5ZiT5czcQnRY8lVcros6-v-ELCu-xpo_CW_IoYclPdHyUOa2JahPh6pPJbg1xa815rS3ptn2VFCvbgml5v5y4CAIVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941b0ce75a.mp4?token=Ra60EUfz-4QwfW0pPSxMZEOUtmQ0lhYEe7amij4P2-HFJf9OvOZAO-n1qHjCuBmpooXHo1UL2qwi-gqqBIkGDBoQ6Iz2vNe3y7YSF_DcfzxIekA10Q_b4r3VIWDyPOfyTX2MEszpIkXgpLcGFQnrxwWNSoB3__-t8Uy2g1phsDjaj8Tuq3C23uziR_ZpJeXn1yhz3LSPM8O3daDO53_QB9jG_dptVTP5wyJzJsGCAOm0okIGixwpfdI4K5qP5ZiT5czcQnRY8lVcros6-v-ELCu-xpo_CW_IoYclPdHyUOa2JahPh6pPJbg1xa815rS3ptn2VFCvbgml5v5y4CAIVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین تی ام واسه خودش و دوست دخترش ۱۸ پرومکس خریده
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/funhiphop/84797" target="_blank">📅 22:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84796">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/StxQQa5ezODoqZroeAKtK-oXcf9pQykmhgMb6vvEfPeFZcadTUVUVbR6swHPXcKz_NnjkAA1gA4qRDjtn0TO66CTVWKFndeolyaOa1dpvjmfi0-nLDm92MdxLoN7UU4wEZpZ7b21vq9pNOMXT735jv9vW3LuP7Ti-kKLMuCdBTO1exKg_Wvyw4omvUY-_or1ipbBfHPP1SekdBEJ4Uj1dZaXgOvQq4WmCIU1VEhVHTV2dizBU7IEiVdHhbPq9bL7ZzpiU1fUgAGj545Dnn9Mv3n5M3h6K8zXbz7awjXpBsJkSX1PND4IO2BHYHreBA2bkxotbVSkHdosK9D7JrhZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار همجنسگرای شهر مونشن‌گلادباخ المان با یک مرد ایرانی به اسم سیروس دبیر
ازدواج کرد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/funhiphop/84796" target="_blank">📅 21:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84795">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">The Memory</div>
  <div class="tg-doc-extra">Creator (ft Alidanesh & Sahar)</div>
</div>
<a href="https://t.me/funhiphop/84795" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator ( Alidanesh و sahar ) بنام The Memory منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/funhiphop/84795" target="_blank">📅 21:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84794">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp9iFEiAAIePekaxu6Z58r3hQGTuwMt_YMkOCCC2lmfsP8_K7zBg7r62vkzkfLpvlythfNLm7Pul5qfSAW3KxkYfref4HEpzX-6qMZX1kCZvdT4FgJM_iAijYeoW3V87ytlK5zW3npQ8RQLFXwBJfaSclA7ypPeS22cFE8QyvjFTuCSCHTrPp1pfnpEKuu2OgPU6uS_iktvQvdVUPaTtNnefeZT9P5zhqND_3enp3cLTWOaG-yOCNgDDMq1GvHJjGdRqM3JI_lrLsbN8mqSuQXtvFVDdR91UaKgvI2SC4SF4VJpjiSy6G_dfDZuyxHZBiMqhEQbOE_gEkcvDs5xcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator ( Alidanesh و sahar ) بنام The Memory منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/funhiphop/84794" target="_blank">📅 21:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84793">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f013a68a.mp4?token=KURysiTUVSI9VP0Ha5QEPzmFXakd8zWpPBA0tXP__lBoMxjPKszvfZ7ovScGs0zh2Pe_usCP7NQb42i4GzGOnbf2AYRBH_D99hpe-qeEJHvaDgi4nn2xYEm2J-XAGTUEFmLyY7bd_65ckW-0lfPejzB-OubA-gzGjdH0IInwl9nA4M9oAhWXwES8igxxEgjQKySGuDSvyVGUJzJD9mNOLryruLL7cFZThoZWaiadw_H8QJw62ztxIFg7MiOb4E-ttcXSbvRxiOhsw2gggyIk7h_EyhxqUHp4p-5nLWUCG0FLxydalZswAO9_7On_Qp7S40e96v0jN_qQjW3hn1G52w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f013a68a.mp4?token=KURysiTUVSI9VP0Ha5QEPzmFXakd8zWpPBA0tXP__lBoMxjPKszvfZ7ovScGs0zh2Pe_usCP7NQb42i4GzGOnbf2AYRBH_D99hpe-qeEJHvaDgi4nn2xYEm2J-XAGTUEFmLyY7bd_65ckW-0lfPejzB-OubA-gzGjdH0IInwl9nA4M9oAhWXwES8igxxEgjQKySGuDSvyVGUJzJD9mNOLryruLL7cFZThoZWaiadw_H8QJw62ztxIFg7MiOb4E-ttcXSbvRxiOhsw2gggyIk7h_EyhxqUHp4p-5nLWUCG0FLxydalZswAO9_7On_Qp7S40e96v0jN_qQjW3hn1G52w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستان کرمانشاه: در بازرسی از یک تریلی در مرز پرویزخان، ۹۹ سلاح کمری، ۱۰ کلاشینکف، ۱۷۰۰ فشنگ و ۱۹۸ خشاب کمری کشف شد که در بخش‌های مختلف خودرو جاسازی شده بودند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/84793" target="_blank">📅 20:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84791">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZqF_YmHSAlm6gY3Ksr_zhQZH8QzaquohGKPV-IMef_AjpvTricqP8BdrpszDfa-WQVb_tVsg2z9FODPiuzJmMymCtv2taI2xcAc6FpzbajGnOWt7FVm594ednleYA2UpXtwLs2hwvEEht4BG_RSvQ5BHn9q8HcPu6mza9FAYserAnqImCR179kqSLHXICF5z8MqMWWog6XeI0ROKqfUeMk6UFjVtr3DJcu75quyEu6NFXWIfaqe4oUbForK4ogcvCss6Fu-gvFATi6fATXuPUpQki2ILuR-1BDC4s0va3EMCu637hrpQlJTUOqplT45eMskkLZRsCBM7saKJvL9e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZjWUjOpka3a-Iz6mxzcByJBFigoPtsAIh-n7QuijWKFLP7RTuCzI3nYyodpz9coiKMsromBpSdd6PziXWuCwK5Me3xml9atQsz15nNBsqlmbLWZ32thlXEjMavE8LmpQPD_H6Up4WFfZEXrxjSiVNQKW4x3cINA-I-YeHmEbSPYkioM4wCO5ma7RqOMpZgK2F5MKBo5KyzxrCFsHqw-ajv1atMFiwb6-7ItCtvzXtnbbD4qNYEea89uKFvVbvc1CmtuoNra5jMltZwmsl-qSfn0S05UfiJyvv8ExWCV3uDAzAj4dj_fZktkznlrFChCv1PrVmnwL8X-bvMX10P4vKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بررسی تخصصی و کامل معنی “سیکتیر”
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/84791" target="_blank">📅 20:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84789">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQLMFcCshk-uQee0DO7am1hK7ENVElQBOl8ytz62Cz2qPVDDXjLwajYioXSmAb59it9v60MyecM88YgwD3DDVFvX-ZvAM_I-zwDxuhDBTR0AA6xWnrewfK3BViD-GCJHhNTvsMbhKcFddr_nPx7k5mg49YadJk4qtX0RmpuwPN21dW4Vv6v7zz55e684rAliuwsTs3EKCznvDHKIXbIMtc2YZhhVwjRmjGpJbXFXdXqvH40H6RPKp4OzQWEcaHEQUnYr-wS1h9oiVIMBgN-789wZOUM4mhWmi6X0NwQlp_skLiN3EWiWrsDxLAx4TwEY8W28oJ7Z0RnxiNESExXPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11bb640d1.mp4?token=vp9zc__6LEZ4nbBN-EbnDn9vPMPDDPsG8_Xo9SLatE99dEbUHF0AW2yg9kUPgq6RZH8zRB6F--1BTk8IkVbj4dBehRJN1Rmf5oqb8MwtUhBUUn9gvV_JWeMfL_swcIyLg5edYqnir4CfFQXZRi5OpLi0u1uNKp3xcSiOTameh32WNycyxoiIumhIU6ZeK4WIw5G0VLj-dG8AAnhSaTsRJgZzlbOhqzNvsuMrU-YS7fjtJ1eNkV1kX-v9YbDdp4Sxfr2iWVheAn7HAl7mpqDZ8ZYXGk3_Laj8hXgHOkfueXNzcXVyvt8Mfb0NKKuF2C_JAUn3kavNyTlpn6wdmZTjFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11bb640d1.mp4?token=vp9zc__6LEZ4nbBN-EbnDn9vPMPDDPsG8_Xo9SLatE99dEbUHF0AW2yg9kUPgq6RZH8zRB6F--1BTk8IkVbj4dBehRJN1Rmf5oqb8MwtUhBUUn9gvV_JWeMfL_swcIyLg5edYqnir4CfFQXZRi5OpLi0u1uNKp3xcSiOTameh32WNycyxoiIumhIU6ZeK4WIw5G0VLj-dG8AAnhSaTsRJgZzlbOhqzNvsuMrU-YS7fjtJ1eNkV1kX-v9YbDdp4Sxfr2iWVheAn7HAl7mpqDZ8ZYXGk3_Laj8hXgHOkfueXNzcXVyvt8Mfb0NKKuF2C_JAUn3kavNyTlpn6wdmZTjFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بعد از اینکه «محمدرضا گلزار» به «رضا عطاران» تیکه انداخت که به خودش نمیرسه تا مردمی جلوه کنه؛ دیشب عطاران با این تیپ توی‌ جشنواره فیلم بوسان کره جنوبی ظاهر شد.
@FunHipHop
| Temsah</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/84789" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84788">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/funhiphop/84788" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84787">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wh_hzfqpxbjEGvr2hnN0x3g72QtxPQZmkEzWFxctWmPAoOu06EGeC_lDYGqC_vjl2uiwhr83w730secnN_t4mrtsU_XoRScjfviap5g8oBg33ib4bWgeE-rVsla7kQAtD8Dur_wckgfeEz0vtPX6gbTwojQsMp42LqogBSFaRnjB7ruXPb74d0B3HYIpflalVAIZ1ZGrRPM8n1782DtMzLg4JaRef4c41yqdtQRaxNqWXYZlpwIAlGJ9Wb9bhXjTsQ0N1_7k_STAb7trgqqaE_iRWlu7zWWeU22FXB7ToQD3HoZ7EgM8aVTs9R0bx7puiqFjOiJIQ1iQZ7pO93NIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G21
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/funhiphop/84787" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84786">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:
بزودی درباره ایران تصمیم بزرگی‌ خواهم گرفت.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/84786" target="_blank">📅 19:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84785">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d183db41bd.mp4?token=fCFPMyTBIqPnJy2aY6uXZtLh2ckp6FNeLqnNXVI81jDNmc7zuEJXplp6namnX_f87BKH59iFeWc4Qq2muxnTd9a0LH-Ocyax3R8YJYm6mOsvrhRMwrql3piG-1sLGVhr0wQd1D7rMiZ9QD840GqVq5GKljh0Wm1a4j4TCqotZgxg3RFuORWKU6HP2Utdr2eA7rpKuquoojtOs0HqDrXgote_YubhnBEDK0em4Kvy2V8OhwoufONOGVFawEIjmhGILEFxEndQIxT7852h81ZGf6-BIhjMr_ImsLaqTAoryrUDxUzQQpy8MIXDRQ9o8UXlMWi7Wh8JjbXGZSctXfF9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d183db41bd.mp4?token=fCFPMyTBIqPnJy2aY6uXZtLh2ckp6FNeLqnNXVI81jDNmc7zuEJXplp6namnX_f87BKH59iFeWc4Qq2muxnTd9a0LH-Ocyax3R8YJYm6mOsvrhRMwrql3piG-1sLGVhr0wQd1D7rMiZ9QD840GqVq5GKljh0Wm1a4j4TCqotZgxg3RFuORWKU6HP2Utdr2eA7rpKuquoojtOs0HqDrXgote_YubhnBEDK0em4Kvy2V8OhwoufONOGVFawEIjmhGILEFxEndQIxT7852h81ZGf6-BIhjMr_ImsLaqTAoryrUDxUzQQpy8MIXDRQ9o8UXlMWi7Wh8JjbXGZSctXfF9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهردار کرج:
همه ایرانی‌ها، کرجی هستن ولی خودشون خبر ندارن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/84785" target="_blank">📅 18:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84784">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0c459f41.mp4?token=W4c8Z5BzJ_CDfmicOoaRgSIcumvpbqy4qZhfWyD6WiqAKu9Z5zyVcRzBN-cFot_hd3yFwuBnj2NZ-c5ZAHi6V_PeRpttHFIIu06C-hgwhlLeKZb868YlhaFbrvEaCRV965GdXwWfbeDXQ1LKjiUiQAQPR2OmeBK_cppS_La30YB9vJUPb6N_Xi1Xr5rAdkX3mSkGMezZ5S-01fMtGD2fgh7GZzA7yuWkdthYevYBvcb5tpZKBhgHfa7Wx2ofSA_nBklwX2CY_5hES4t8tSHBvK8Kqd1KxzRZKJc-CyAuS6G2McsQjPlMCiJTQcPt1bBZOAjHVmJtPuYvk812qqIH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0c459f41.mp4?token=W4c8Z5BzJ_CDfmicOoaRgSIcumvpbqy4qZhfWyD6WiqAKu9Z5zyVcRzBN-cFot_hd3yFwuBnj2NZ-c5ZAHi6V_PeRpttHFIIu06C-hgwhlLeKZb868YlhaFbrvEaCRV965GdXwWfbeDXQ1LKjiUiQAQPR2OmeBK_cppS_La30YB9vJUPb6N_Xi1Xr5rAdkX3mSkGMezZ5S-01fMtGD2fgh7GZzA7yuWkdthYevYBvcb5tpZKBhgHfa7Wx2ofSA_nBklwX2CY_5hES4t8tSHBvK8Kqd1KxzRZKJc-CyAuS6G2McsQjPlMCiJTQcPt1bBZOAjHVmJtPuYvk812qqIH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید سحری برا استقلال و یاسر آسانی کار زده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84784" target="_blank">📅 17:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84780">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G9sHSnNUF7_hA_SIZs6QUH86RdZHazgbHq2UVIwl05yP6NJBYC1cCVhIfnsp8FQ9eYccAFyWXi6SW9Q1zX3iMw5cG8Lre7Le_QVqJqbz4VupEJ4srGfUdxCPXRcGLYJwjHg7x1KbsJQBHgOseS6vVhrsin4vs7EmM6BD0Asdp9jXeUwUU5qJgKAbfhkUq9UbdoBLNlUprFvyr61JHSBSj61ebrRuPdvv1x60pkDgZ3lyQ0XhBN9YBg-Em5mbbdgwbui0G2SVOf3TmvQkUe2_TTW8BP6PtuZhNc7YN7fVYcGw9pOLywjdBkPCNJpc2nzy1LXuqeQqvn41kr-sY2eVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFIWImMq0nDMUgFL_ZxkMe5PJKx0pRwL7qMdq7_ZUcjzjo_LpJ-qMvXzyhKhdJ7lNOnjH3JKrJ4--Izp1PlPyn2Vcr_IIlICILv8nLzi_2ae7eTC01NH7vLD8Qqnc7YkqWLWAGMC7SJX3VEK4LgcvXtImMmj9XplFy_KeV6CnLNs15AZYYMPi1XjFCbXPcI2haoCtOJ_zfjc9gNyllR8NiQdLYP7T2tdtH2X98EDraN4JKFHITYhb2ESEts1P96hY-E8cUq1O2s3FmkXN0CLRKGOSBLDRWgFPHIenJdPjuKWE9Vjfg1AGzLSpD6GF7bU4o_diw4zT10hbbq-hXDt1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOx5CB80EiLqQNNFhZ5Ji-vLEN8tgaWFXN_quXd0dSVn1uhkt7TiqJhgZ_KNqiKVvCaAUyv-o57ft6j1nW8SgK2aqhIYC5akNIWAwX5NR_h-mD4nwb0iYXXeD2-ipFtoCOH_J1qOfXEegXYullJNdQU7DiduvEZ5GUi7Id8tUEFwTMVwY7Vr-hQX16WpCtdNiKSSmhPYq8LMv-fTfN7fgVPqT8F70j9pvTyWBi6v5B2iVOutGvhAi8uV0ktMOgtuREsvYmOnUBxtkL5P2PiBludNhoxqzi_maDNHMFjA0MGfYRBmTmXJlixOlBWO_1KavmuzwQp7jtWMyNpK5G0ttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZ8riJXqgrX99xEb2JALty9HmCi_96DoPoXelwM5AdHFMxEdnA61SM02qFsnbYjQLtwdy78DtYUFHiyHquC7pEtWkYlq1n7bce4F5-shqYwG_LbFfkUT9ZF4n5tIHR10nIfFwSCNh9AU-mO1hdF78TiYDlngbDdSO1SttTSkkLpnkWjj0I4ZIGCd5FHgg0FH8S-MuwfMdwZdcZmPAZCuV5AynTXyg94oooZf2gl9r0Oocm_M5ilUK95nFnDyXOTKfMxvGXASosuge2p31YLskxRZ2BWWwMu7uQ5vnhQNeSNa-TBJVzr7Cu3orMcFhOVgnqx6uaLXkooeVIJ_v7tiqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز یه عکاس فرانسوی تونست از پدیده‌ی زیبای red sprite | رِد اسپرایت ، عکاسی کنه؛
رد اسپریت‌ها نورهای قرمز کوتاه‌مدتی هستن که گاهی بالای ابرهای تندری، تو آسمون دیده میشن.
اونا فقط چند لحظه (هزارم ثانیه) می‌درخشن و معمولاً بعد از رعدوبرق‌های خیلی قوی ظاهر میشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/84780" target="_blank">📅 16:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84779">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=JZj_A6BX7OMrVtdno19ppcIdq38QFXe4HivTG-G_WekIAComJFwI8c9edZMLJ91rwnBNtEG2RBFqrgqgP_pKCUm7hnB1dwheHoGPurtohIADuX43E61oSWbTPTpA_HXT-DqLKY_jFaWInDKB_R0T-NoFDTyRyXU_7a-tUSx41FU9lxvjc2Mm8BZXhPDofouFph424R6Ss9v7HqGHKSZKocuVi5M-FtzdUHHJYGrAjcRi0zqzEs85RLwc_Hjqy8_DVEG1TBravCuNAm-GCasTmCi5u9f5UbUuFBjxWGseUKXAw2KWjTxWkCvE_z7KocBykri_qhdwCDN1LDJHAa1YkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=JZj_A6BX7OMrVtdno19ppcIdq38QFXe4HivTG-G_WekIAComJFwI8c9edZMLJ91rwnBNtEG2RBFqrgqgP_pKCUm7hnB1dwheHoGPurtohIADuX43E61oSWbTPTpA_HXT-DqLKY_jFaWInDKB_R0T-NoFDTyRyXU_7a-tUSx41FU9lxvjc2Mm8BZXhPDofouFph424R6Ss9v7HqGHKSZKocuVi5M-FtzdUHHJYGrAjcRi0zqzEs85RLwc_Hjqy8_DVEG1TBravCuNAm-GCasTmCi5u9f5UbUuFBjxWGseUKXAw2KWjTxWkCvE_z7KocBykri_qhdwCDN1LDJHAa1YkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست یه خانوم از اثار کتک خوردنش و 10 هزار کامنت این شکلی...
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84779" target="_blank">📅 15:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84778">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehdi</strong></div>
<div class="tg-text">بنظرت لیگ دانش آموزان بلاروس پخش زنده داره؟</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84778" target="_blank">📅 15:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84777">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مرگ دختر جوان در ژاپن بر اثر سقوط یک زن از طبقه یازدهم
زنی ۲۹ ساله که قصد خودکشی داشت، از طبقه یازدهم یک ساختمان به پایین پرید و روی دختری رهگذر سقوط کرد دختر جوان جان باخت، اما این زن زنده ماند؛ گفته می‌شود این زن به اعدام محکوم خواهد شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84777" target="_blank">📅 14:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84776">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کل مصاحبه گلزار فقط اونجاش که گفت اینایی که پولدارن ولی مثلا برا مردمی بودن به خودشون نمیرسن و درویشی زندگی میکنن کسخلن
تا خود صبح باهاش موافقم، کصکش پول زندگی خوب داری چته مثل کیرخر زندگی میکنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84776" target="_blank">📅 12:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84775">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=syvbqVqfODQ978MGkzxzQpHtgLAqZyTBgPJVR83xBOuva7eYAvyoUep5uHnTsdxVpEaHOqhly5TSDO1RkJ0_fhrMzBKNP3AK4nwaCuim2Tc0zIRx5G3rJZNw0EQ-9aZ9OmIEV-LbXN7yWBJ_MfyQjlVKejwkI90UboUNtr8HV-JgBju7g6mBNMFK4-rjLvRU6swwWdF_I5pbr9wxDhfWDHJUo10hVQEUsmcdWXHXPQmXB69U2Ox4PxTnS-aYF31uDw8M-wkm6YQAznAW9U4WtaRJYeFsrygq-RrMexkKzXOwOvpptp6mdzEyV-zGHyeDcRD7thM1iaEMTKaHivt6VYDtQJ6g-JIrX7NIgEehNaJYTYa56MiGyQPJwBdIFDrb-1Z6kyO83gNY8tkBfIpmyBzuZMEX4OxYuYn6BDFf4Xw_o9tHSxB9B93QycAPIGg2aA249wWwoVe2oryMy_RVJufvd6xb-A0yIp0fKodnXG4jhNV_J7R7diYNlS_B7e_TuRTseUOwtTHVBGxdBtoilOlwpLBFZRWBRBkY87Ntnjc9FaicPCPMJuTVblZMAX7vDFjTTLP6yfELuv3363_z4Q3bfA9URjt_7r3ScOzBs8wm82MOg_nl6wiuWy7Aev1tpW8OQCrdXur2PvQVRTlRAY-JzEm2-zVjhIXQFveW7qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=syvbqVqfODQ978MGkzxzQpHtgLAqZyTBgPJVR83xBOuva7eYAvyoUep5uHnTsdxVpEaHOqhly5TSDO1RkJ0_fhrMzBKNP3AK4nwaCuim2Tc0zIRx5G3rJZNw0EQ-9aZ9OmIEV-LbXN7yWBJ_MfyQjlVKejwkI90UboUNtr8HV-JgBju7g6mBNMFK4-rjLvRU6swwWdF_I5pbr9wxDhfWDHJUo10hVQEUsmcdWXHXPQmXB69U2Ox4PxTnS-aYF31uDw8M-wkm6YQAznAW9U4WtaRJYeFsrygq-RrMexkKzXOwOvpptp6mdzEyV-zGHyeDcRD7thM1iaEMTKaHivt6VYDtQJ6g-JIrX7NIgEehNaJYTYa56MiGyQPJwBdIFDrb-1Z6kyO83gNY8tkBfIpmyBzuZMEX4OxYuYn6BDFf4Xw_o9tHSxB9B93QycAPIGg2aA249wWwoVe2oryMy_RVJufvd6xb-A0yIp0fKodnXG4jhNV_J7R7diYNlS_B7e_TuRTseUOwtTHVBGxdBtoilOlwpLBFZRWBRBkY87Ntnjc9FaicPCPMJuTVblZMAX7vDFjTTLP6yfELuv3363_z4Q3bfA9URjt_7r3ScOzBs8wm82MOg_nl6wiuWy7Aev1tpW8OQCrdXur2PvQVRTlRAY-JzEm2-zVjhIXQFveW7qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فنای گالاتاسرای دیشب جلو هتل بارسا:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84775" target="_blank">📅 11:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یعنی هنوز ایرانی ای وجود داره که فیسبوک استفاده کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84774" target="_blank">📅 11:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84773">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗺𝗶𝗻</strong></div>
<div class="tg-text">ما سیاه پوستیم((((؛
همونایی که…
بغض نمیذاره حرف بزنم
حرف دلته؟
خب حمایت کن سیاه پوستا به حمایت نیاز دارن((((؛</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84773" target="_blank">📅 11:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84772">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">من دقت کردم از وقتی فوتبالیست های خوب دنیا سیاه پوستا شدن برکت از این ورزش رفته، چرا انقدر عمر حرفه ای ورزشتون تو فوتبال کوتاهه شما سیه چرده ها، ملت هنوز با مسی و رونالدویی که تو لیگای پرت دنیا بازی میکنن کری میخونن واسه هم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84772" target="_blank">📅 11:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84771">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=vJ3Eg0sivltrADLb4N141pnRFO73K89pv-eTYraqf0p-G0bEwrvLDjSZEWc3Rg_pQ0GnmD0vq1NLtt6l-jkwf24THPU8WOhBLrt3CcCnCXs-pkUDq0gjymSUlntAKjtZ3rzjogo5D6F1G1GbMkxB7_R-agmTPI8a8qzGfQubBt1uznRtF-L7j3PFs2_1PPdiQ0VijApQtILcVxH8mwnJzbV7PQ5UauZYx3h2fRbevcnO3UGm7rrM9GlrjDLq64EWe-LO_JnTBOHFxT1dF2z0Qwue1xR_KmBxZ0n2EiJKGnDXjGCKP34RLH8VAz6LgPWR0-95Ut71jh_0iBvk5WcTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=vJ3Eg0sivltrADLb4N141pnRFO73K89pv-eTYraqf0p-G0bEwrvLDjSZEWc3Rg_pQ0GnmD0vq1NLtt6l-jkwf24THPU8WOhBLrt3CcCnCXs-pkUDq0gjymSUlntAKjtZ3rzjogo5D6F1G1GbMkxB7_R-agmTPI8a8qzGfQubBt1uznRtF-L7j3PFs2_1PPdiQ0VijApQtILcVxH8mwnJzbV7PQ5UauZYx3h2fRbevcnO3UGm7rrM9GlrjDLq64EWe-LO_JnTBOHFxT1dF2z0Qwue1xR_KmBxZ0n2EiJKGnDXjGCKP34RLH8VAz6LgPWR0-95Ut71jh_0iBvk5WcTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شعار موردعلاقه‌ ام «گی‌ها حامی فلسطین هستند!» می‌دانید اگر گی باشید، تو فلسطین چه بلایی سرتان می‌آورند؟ شما را از بالای ساختمان به پایین پرت می‌کنند. شما را به بالای بلندترین ساختمانی که دارند می‌برند . البته ساختمان چندان بلندی هم ندارند ولی از آنجا به پایین پرتتان می‌کنند. با این‌ حال، مدام می‌بینم گی‌ها از فلسطین حمایت می‌کنند!»
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84771" target="_blank">📅 11:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84770">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBgI3aZbFGuwlSB3dD4mHRhyyW54KWdhhT-1TiktvqEHpyHmhvK7dklK425wSajhTUVu2irz7UF0YhyMoh3zAQD-RnqFHHlKll9gO249Jestbk_DmjXJvxfpTLyQ_s1NCB5b908fMQFW7T_YrzO0leYn19QH7MPBcE9EArNKI7wnbRVPdIQ_IPEoXgUOo2HRD-OjjpuJ8dUDllX6EJYT7W6cvcgRyz3r0l6QfQ7nLpZ79PBmBQAYFcL2UArgqABXsYPhFk9T62uNG98BjauPzpb-4TlSA80k4cuS2RDoyF7rwFQa6rBVZZ0et5_2fVxIR9iOk8msFIrZRcll7uQvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت دیوار پر شده از آگهی فروش سبدهای گل دخترهایی که به مناسبت روز دختر، جعبه گل هدیه گرفته‌اند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84770" target="_blank">📅 10:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84769">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84769" target="_blank">📅 10:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84768">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=XAHXQeib4gfQgPM6OGquyETAOvnPrnEN4wZGIpxiX6lK1L1Ac_D-QFw2vc46OoVssPNKCN6L7XEBt4zBKpKRfMmFpmVAavChUEi74-X0eGJefWnIyF2ih0ui61j4NgZN8lmJ5OTHV3ygmlASMrtpVWfULzRJcxEpmj3agk75F-XJz7y7csZk_ztY6DA_N8QOY2vqa5xMc8ALj4PsYZG72RB0W9sbVXzEtO1nGJ8SfE28waMhDjG93leJyD15jW5XQpcVQfyFBfmpdOhgbpdUfkfHQlcuD-ENMPfSkR0C9cBD4IzGFLDl64BGiWhbLlB2hgefAxmExvKbw3Cc6h9GGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=XAHXQeib4gfQgPM6OGquyETAOvnPrnEN4wZGIpxiX6lK1L1Ac_D-QFw2vc46OoVssPNKCN6L7XEBt4zBKpKRfMmFpmVAavChUEi74-X0eGJefWnIyF2ih0ui61j4NgZN8lmJ5OTHV3ygmlASMrtpVWfULzRJcxEpmj3agk75F-XJz7y7csZk_ztY6DA_N8QOY2vqa5xMc8ALj4PsYZG72RB0W9sbVXzEtO1nGJ8SfE28waMhDjG93leJyD15jW5XQpcVQfyFBfmpdOhgbpdUfkfHQlcuD-ENMPfSkR0C9cBD4IzGFLDl64BGiWhbLlB2hgefAxmExvKbw3Cc6h9GGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل مسی اسرائیلی نباشیم
☝️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84768" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84767">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5hXEQQTiYbv9DD73xSwijX8TSEk1IYHrygmxlQeUb_zDw0kxSHYUTqMpepRY8ucts6vpyWLSKnZBOfIRwhtOIypuEoAq1zGnlUVMrECw0bolcx1k73vUIqC9gyU5andipASrjrs01MIcrLyvAsx87IGrXQ69yMhq8gQo7YwaLq1mwzt4933LLtpCrOfsyIylTfS7fau-yghlHo7nGejci963ybff7F1_MeZPzYgLlWQp75Q2uSuajDS1-KxdHSXbN5DcVFYleaOpA6FXuQX2vRuI4rLoiLU71p4Sxx_GzzRzJ_j4UVlp-ON0nvSq_tZZAtBPqkdwnVgJ962rnFo3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84767" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84766">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=jM5Sn17kF9zPyJxb-u4nfCJcbj9L-okFaeIpRJdxgwzRTfgmFnQaFMpOjMIi6tKxQ0kfXX8M9egFEjFLNxIcETwxac6okz_vCUXWsNU_9nPMn7keFsT9r_bSkVL9dqOB4kuH5Ek4KD5ALPRnxR50Bt8ZOXRK-ExcZRYIfLr5T_gw712Z8o-8b2YNWI9F0s6XURlXUs8v8J0IMG6GqQP2QE6fGNt5Q5iGDmFFRVecQtYJuixOMo4ahJNrIgh8u8_JM9KUpRIrURzAitVDe1no8RDH7o5XjcVsxXh8Ocforuy2lpChiSHrTYOoKQVU1TmzkThwZ1UirUFDUqOxUOf9WBqhySzcsa0ASfUyhW4qislRzqDoxP6PEVMvSLOeGS2WOhHkLXXNmKg25i88-AKMkNam0aHycabF2HKrr1ZWXu9x6XJBfnQd5MTJXN4JvNFhdcQvL3C7lzi7q0lMjQi10HmMRD7XsyFQGrLMIy1YS3gLQwVtPyKIEBmaOARLUByP_3AdsbuD_Y71HcUFZE1D5TNoqpdQo1M-ivGAZ2DWjryaK3mbetICyV832oK_kJZU5tGk1R3PcZz979t84FwEOkm8MV1S8FmVWN9Dikie_Z_rE12ervpbbX2E6gGgtN3FG9SA9ukUMDvAIdKnI2RzC5kr8y186ZxKUjulR99H_ZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=jM5Sn17kF9zPyJxb-u4nfCJcbj9L-okFaeIpRJdxgwzRTfgmFnQaFMpOjMIi6tKxQ0kfXX8M9egFEjFLNxIcETwxac6okz_vCUXWsNU_9nPMn7keFsT9r_bSkVL9dqOB4kuH5Ek4KD5ALPRnxR50Bt8ZOXRK-ExcZRYIfLr5T_gw712Z8o-8b2YNWI9F0s6XURlXUs8v8J0IMG6GqQP2QE6fGNt5Q5iGDmFFRVecQtYJuixOMo4ahJNrIgh8u8_JM9KUpRIrURzAitVDe1no8RDH7o5XjcVsxXh8Ocforuy2lpChiSHrTYOoKQVU1TmzkThwZ1UirUFDUqOxUOf9WBqhySzcsa0ASfUyhW4qislRzqDoxP6PEVMvSLOeGS2WOhHkLXXNmKg25i88-AKMkNam0aHycabF2HKrr1ZWXu9x6XJBfnQd5MTJXN4JvNFhdcQvL3C7lzi7q0lMjQi10HmMRD7XsyFQGrLMIy1YS3gLQwVtPyKIEBmaOARLUByP_3AdsbuD_Y71HcUFZE1D5TNoqpdQo1M-ivGAZ2DWjryaK3mbetICyV832oK_kJZU5tGk1R3PcZz979t84FwEOkm8MV1S8FmVWN9Dikie_Z_rE12ervpbbX2E6gGgtN3FG9SA9ukUMDvAIdKnI2RzC5kr8y186ZxKUjulR99H_ZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه بادیگاردا این یارو رپره میگفتن خلوت کنید آقای بولینه و نمیذاشتن طرف نزدیک بشه، دو هفته مغزمون گاییده نمیشد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84766" target="_blank">📅 08:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84764">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=IKNVdPYzelSnG83ivVcmssfmplvcLucruiecnFgWvWA1csZtDF6Yltiwnw1ndSdLu5HgPV631hNE3BglhfXYH_tC0M4_Pl28vaadT5PvlS1gRIZ8LTRGCLpl-loDOXqPUVvYVIySCNNpQmjWNLgqq5SdVWViC-ebrL-fWaGaUHeFybEJJST5kGVTmevV4YXNDPRX4kq99PicF5iDIGLFJGv69MQj2cjHeBzb64EHHS6qRkdOp-X6txZGG0nkwH5br6eSsHm7XV0NojcWiu2wVPeT4ABDti5rxVS_y22NuiqilvvEG_pqST8HGnBw9zl5_1ivC_6UbnK5PsuzEormBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=IKNVdPYzelSnG83ivVcmssfmplvcLucruiecnFgWvWA1csZtDF6Yltiwnw1ndSdLu5HgPV631hNE3BglhfXYH_tC0M4_Pl28vaadT5PvlS1gRIZ8LTRGCLpl-loDOXqPUVvYVIySCNNpQmjWNLgqq5SdVWViC-ebrL-fWaGaUHeFybEJJST5kGVTmevV4YXNDPRX4kq99PicF5iDIGLFJGv69MQj2cjHeBzb64EHHS6qRkdOp-X6txZGG0nkwH5br6eSsHm7XV0NojcWiu2wVPeT4ABDti5rxVS_y22NuiqilvvEG_pqST8HGnBw9zl5_1ivC_6UbnK5PsuzEormBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تورکا حسابی خایه کردن از بارسلونا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84764" target="_blank">📅 07:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84763">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=Odfn0UO5MS38s2sMxNheRFFHMQxs0MaWXL2MZf9V8jqSZOTqtuJ3THAYhzG7G9_u0auHdeHuPLfC0_ykLmMR47Y_G7qKFa5s664vd8Xv04wrAIbaAH6cmoQETnKxFDTtwXxhu4nHysF64lL4nb2c9bD3vvamjF2oi4zDqm3Pu_Cx_6K89yHXpK90JCnrHev5F5Q0fN_apgXtkXhULsaObSfw3XJ40hC81C5vfF5WX3OWkdWjwz7tQKGkwiFtHdDi5Aow0DI52eyPT7sflT3BvkEB4EN09e1p6JAzW0cEEwHz0JW-gX0ebVQSUnAxVmrcYW7l3gPUOsmJk2SMBdC_3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=Odfn0UO5MS38s2sMxNheRFFHMQxs0MaWXL2MZf9V8jqSZOTqtuJ3THAYhzG7G9_u0auHdeHuPLfC0_ykLmMR47Y_G7qKFa5s664vd8Xv04wrAIbaAH6cmoQETnKxFDTtwXxhu4nHysF64lL4nb2c9bD3vvamjF2oi4zDqm3Pu_Cx_6K89yHXpK90JCnrHev5F5Q0fN_apgXtkXhULsaObSfw3XJ40hC81C5vfF5WX3OWkdWjwz7tQKGkwiFtHdDi5Aow0DI52eyPT7sflT3BvkEB4EN09e1p6JAzW0cEEwHz0JW-gX0ebVQSUnAxVmrcYW7l3gPUOsmJk2SMBdC_3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثال عملی سخت کار نکن هوشمندانه کار کن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84763" target="_blank">📅 01:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84762">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAi6era6104aEyIo2_OxyWV0BnpZvaIwUG2ZVFRLEDtN1RH106ZiuyZUKW-Kj7lZYH3y9S5UMhFT1YumrDI-I3wOqf5T9i0RFs2iMic1AH2g6b6UjxR-NWXbI3PzYOvYg7EIOaV5eOtyezyppaUSszX9rAaItD2yLqP2DVmNcVHHqErWEELss4WvlvitloPyvrIW25EaKNDVCdtVNLWzOPBd-j-BH3GSxaOZ9LmzpeeJH5GhY3MS_6BshlC-bovyE0HeJQEsQxilFl0hSuWMUPmwfGGjXG5N_7cuQuDwKI4tHvz8LjRs8HuvWxCIED8DleixarviIdshXs-lxUkSig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84762" target="_blank">📅 00:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84761">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خدابیامرز نقشش تو سریال اینطوری بود که اگه اون لحظه جلو آدم سبز میشد تیکه تیکه اش میکردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84761" target="_blank">📅 00:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84760">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbWf6BBEBwqqPH2KGI9I6TNGJAb47cBCwz7LpXg1lk5ZOXCjdZjud_pbfNBkw-bn1il1xxhR5JCcb8OYXIdzXEeD-FQrki3g4dHNceqaVLKIT4l3g8vqIi0pqSlu3Bu5sMEkjOKF-IymiQ22oLZ0NV0ZIRxJqz_KRqUTdK6jzqJ-Rk9sjpgXZxnHtTGswkvo5d-lwTP1i7O8LNg9uSJ6DkndM7w7ePD47ktbpgn_myNOyVo4XEeL3jztYlvqJx7eK0FZEMSe8CtYvMWZLY8HNABCiDB0oKOrlokbDM8ksI6G11j0u_SSgaF2M0jzFFn8XSne4ZKxOUVPAYE6rX24Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84760" target="_blank">📅 00:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84757">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5sM2gNa_VgviX7eix28jBekNhxAyOq9DEOd746ZrV7SiQvAqdmKPtgLQDpJXEMXFo4s4tgWpUaO1brAsaVKa8jjuhPiwA_ia8_C2-x6IFOPaimUM9-R1P6xVR6mfNdbXNrOYb5VSnBXyNX3IpHHfNgom5dS9SnI6tTdvQ5s5MrUvWD9D_IHJjjzBBuljNLvSfJIovgP4uXOv6wJOTY9pbP9CILFK5CpuZn_C0q1ngzv-_7NlAIXHYfUryR6mCz_sNTKoub_fi1TJwCiGaJwsKtVpJ2Jqx1nO4E0IDbrwtQU8VSC7C-i1OYQHNxxKdoayMfyWFqmavtAXtsM3OFBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داشتم زیر استرس جون میدادم حاجی</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84757" target="_blank">📅 23:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84756">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6Njj5Vrr7iFrYf6h1w7zDAhLvsLwYTVsEir__ibb04VSGgcyt-LYkcnrSkMj7HVCIKVW03k1boqEJ4_I6kX-Hd2s3KxbqFx8oWi70-D2nQpqdnCZ76ej-szHstNhmBpavj1_cK4JFI2_BC8tRzM42cdkEpkCrbtG1rCVw4uHhSEqMro4JP6wlvsOUZI-eWKYpUp0dnYG-yxG1J28m6qPhTNSyV0QLIpScKQBiXNqfkCEPDaG4Wsn6s9rP55SC-332UAgqmxQ3VWYP9G2cyyr4Shm2S7waTsyP-c-FoOAMP85flhNqyGSgIeXkvS36HO_xfyt3rjFPkpTehnlIgq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید فدایی و شاپور و رفیقشون ارین بختیاری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84756" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84755">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حبیب کیرتو بخورم</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84755" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84754">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvuQHKfdnAg6c542-wXtTJlgGkuKIZFcyH0w3dzc3ZRdThtF7jbZyCYBpEaS4I244rOD7t6iama5pkQphV1XQ-1cJlcby3F9xlFj51_bOx74S80MYFxU2mrsvJUEh3W7qL0KnP__IZsQPs-YZ6OeqxBbwHxju7MyL9NNlkLVStW1ZI25xTbvTBwx0gGzta6DONDOc4iRg2aNsk8Scs3oyNJgiHAiVc6-_LHmgsYbs0ldKSXJ8px9MaRQf6FzyuhMFsXXZpbfA4QMYs-FB_xuUORSLOBJYLaxMsC9ONtIeCM1vTKO-BufXmRziMOiR87lPu3UtpIPJpZbSit9tdeSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه رو
😂
😂</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84754" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84751">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هنوزم نمیتونم درک کنم چرا هلدینگ دو میلیون دلار داد این سعید دالگخیزان رو بخره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84751" target="_blank">📅 23:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84750">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQG-xToAtZ6FIxWoBO_dutqClqSuZtYDtyqX4LbupZiIAo4xnL5_mvr0NrIkewE5Sh8Tq5GtFrh-Vr9re2oQIwHo4S1IZ2xw9m7xrkC8RRTjVKH_WbWPMq08vVYFcb6LFL4HUGfwYUB2-UmJebf2N9Bb2JnXX3MpghT8OMVixQKK8rf9AfOglBRP9Bfq8txipjmvSA9i7xEk4U4W-zyqb61IzVDiGiPNe-pzOavHQh47rWzkulSV429VfroIlkOqi5xV567isbDj7ggrjMIzasn4alofndoyntN7rj6AnUKpV3FZOJ2RLIqMF2iFqn7NxmhUMaSSwvW4ou7VNKmALg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84750" target="_blank">📅 22:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84749">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84749" target="_blank">📅 22:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84746">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940390f975.mp4?token=BomAiz0NbrL6XbMZf4KQIpNRHwKqWtcmHloavb_bEWGCRORB4ErEw5QDdvd8zNlPJQc-X8WWBUxskfe-r6q9HXkq_J1poBSONwl6s1VhHL3Ic79QeqECnzJdA8QAbPmIQPqNhDZT2S0jUJvSDApcNqBEejnEf5hzK1qdGIunE7gL_yA0N1dGfDgUHB6eiNJU8pbDzCClpOYaazDKaMD15ZptmNvYKTs1OdP3i8LXO65XK7z9y3Gsgsadj4BjkkEFDC_9nKBTF5C-Ao1yRaVx4D9ai_stLP0MzXRFx-OYefjufexZhZxVL_WHvZfD_SLr5ARU4ncmfFA66uBRHLhsJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940390f975.mp4?token=BomAiz0NbrL6XbMZf4KQIpNRHwKqWtcmHloavb_bEWGCRORB4ErEw5QDdvd8zNlPJQc-X8WWBUxskfe-r6q9HXkq_J1poBSONwl6s1VhHL3Ic79QeqECnzJdA8QAbPmIQPqNhDZT2S0jUJvSDApcNqBEejnEf5hzK1qdGIunE7gL_yA0N1dGfDgUHB6eiNJU8pbDzCClpOYaazDKaMD15ZptmNvYKTs1OdP3i8LXO65XK7z9y3Gsgsadj4BjkkEFDC_9nKBTF5C-Ao1yRaVx4D9ai_stLP0MzXRFx-OYefjufexZhZxVL_WHvZfD_SLr5ARU4ncmfFA66uBRHLhsJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84746" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84745">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=Cxii9zjSpIw-ZVV5fiHI3p7UTWNnvWMplhK2t-noBN1Z0dWtcUo4gDFB-mnPiUftgett0yce1SGnvVgPNfhNvrBk-rHbn8V0RHqb4WUETgjPI-3IqwC1BnhEmj2O1W30QQFupJhudo1FFAw9KP1sDVx5ldP_uiEOXJwZeFpAbCehHk6PNJ1XZgqD0T5u_LxfVAgQHmx2cLBjAyN9Eqmo8G1BAFRcckna-XGczXIyJZpZdVe8OlNrN7lg9VTj_iI4eKGJ8kxtiDknJpYOKvSz15LwWn4IobTL1EXUOHzXCExeGhpq_iA_xGIe6CP50Zgdgg2bL1VmmsEMannNNkxFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=Cxii9zjSpIw-ZVV5fiHI3p7UTWNnvWMplhK2t-noBN1Z0dWtcUo4gDFB-mnPiUftgett0yce1SGnvVgPNfhNvrBk-rHbn8V0RHqb4WUETgjPI-3IqwC1BnhEmj2O1W30QQFupJhudo1FFAw9KP1sDVx5ldP_uiEOXJwZeFpAbCehHk6PNJ1XZgqD0T5u_LxfVAgQHmx2cLBjAyN9Eqmo8G1BAFRcckna-XGczXIyJZpZdVe8OlNrN7lg9VTj_iI4eKGJ8kxtiDknJpYOKvSz15LwWn4IobTL1EXUOHzXCExeGhpq_iA_xGIe6CP50Zgdgg2bL1VmmsEMannNNkxFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر بخاطر آژیر خط امنیتی (احتمال حمله حوثی ها به ریاض) به تعویق افتاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84745" target="_blank">📅 22:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84744">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بازی پرسپولیس الهلال بخاطر حملات موشکی حوثی های یمن به عربستان لغو شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84744" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84743">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ناموسا آسانی حقش لیگ ایران نیست</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84743" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84740">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">استقلال یه بازیکن داره اسمش احمدی عه، یه بازی قبل دربی رفت سال پیش مصدوم شد، ساپینتو میگفت به دربی میرسه، یسال گذشته هنوز مصدومه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84740" target="_blank">📅 22:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84737">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آسانی نیست استقلال در سطح تیم سالن بچه محلای ما بازی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84737" target="_blank">📅 22:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84735">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بازی استقلال تو آسیا شروع شد...
گزارش لایو با چاقال اسپورت
🤣
🤣
👇
@Chaghalsport</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84735" target="_blank">📅 21:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84734">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR1w-WSRo2M3ChZ6iwAjx6KnOrVV2gvIUaovTAfy8EF4JOICVhyZQXABqACXVpExxTTW7b22sr1KIe3-TX1MiEStklsYnJc0dEjOVeqovhu6s6zMwpzmjnMgwJC9bEonWgoVvmdKAgoGUeYL059nD8bI8YOBQK8sXtrytLkogRLJBE3nL8CKO4Qio_If51J4QcILCuhvEHDNc0TtrsDG2tEdZCzFUgqF3fjz2ukfpyQI0-GlPDGBsH_LFeZaPBTYAA7b4SpshbRu6CTt6m7UWpsk6pj7HY9FN3-1ufdAK_G8nWO7SD3gAO81cuzqz9F131KDcK7Fv5W6vI2-JJ2aEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پرسپولیس برای بازی امشبش جلو النصر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84734" target="_blank">📅 21:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84733">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=LS1GezDvEckd_kfKVQ-2UzpfRSeKst47kr1psY0fNCuvjKfDR9A6KLl69d7Q7BN_Fs9_m4o5a97IEUI2OxIS2N8K-GirqTNCWpuDywmbm0pNiODhCVXMe5ivJLe2ohmALVAOcN5tn_GdN_Be9_jMYIUflXW46MXgKAkANu_mgBIl_g-DDA5hpzOwwMiPrzuEnBpPvlwvAw3TpmsiLDs7wFleiD5bB7R7ydDCJbyxB_kDf3oaUroqKGk02TSlIBPS80jpzT4epltOkx5pSjb6RPYd0KyalF2fhiPCAJsxMexIVUTNBVlAFV41SRygw_dyElz3hH6hvYmiNSxCVzdSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=LS1GezDvEckd_kfKVQ-2UzpfRSeKst47kr1psY0fNCuvjKfDR9A6KLl69d7Q7BN_Fs9_m4o5a97IEUI2OxIS2N8K-GirqTNCWpuDywmbm0pNiODhCVXMe5ivJLe2ohmALVAOcN5tn_GdN_Be9_jMYIUflXW46MXgKAkANu_mgBIl_g-DDA5hpzOwwMiPrzuEnBpPvlwvAw3TpmsiLDs7wFleiD5bB7R7ydDCJbyxB_kDf3oaUroqKGk02TSlIBPS80jpzT4epltOkx5pSjb6RPYd0KyalF2fhiPCAJsxMexIVUTNBVlAFV41SRygw_dyElz3hH6hvYmiNSxCVzdSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا چیکارش دارید خودش دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84733" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84732">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هالند راجب شایعات سقوط منچسترسیتی و جدا شدنش از سیتی: خب اگه سیتی سقوط کنه مسی باید نگران بشه، چون من برم چمپیونشیپ رکورد ۹۲ گل تو یسالش تو خطر میفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84732" target="_blank">📅 20:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84731">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzKPHyopLwCL1kyJ4MSt7xtDjwpc1eNCeJamy6TzUePdWpcGtHpR_5iKVpgtpVvXDDeWhkbCdkYStLot6GDb1UYuWndnpGJK_RajtRt_d3UESNEG8Iza061uKDS6KVLJJC6OAlgsWOr3bx8w3S123LIp514JRxWe1D_fhw8NZLYL-qGBFFp4bFIFS1zmEVFwlvwIdntcKawUhx7q9i9syd896uka36G5uIU9Gh-a5LuUgzI-fa4ksIv9cMZJj1Bu4d_vzulYF0IFh8TTYJAC3JC9OSv20AOxYMFW4JhI2C0P_sQKAHul5lRTWALF2NNAOgYoO4wu35xSrKng6W9xcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران رتبه ۴۵۹ بهترین شهرای جهان رو با کمال شایستگی کسب کرد‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84731" target="_blank">📅 20:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84730">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=o3CF7CPj3sM_TlS3UY92aAtWgXrCn5aFzZJUfPLFv0qJaz4Sobx6fw4_AeuNu_2wH4-xl95sTNjvBHvbblN5Qu1UXQbK6CtILKlGtr4eDW6qT_wrlfj-IaGzb_4hA2KQkqmz7GkIifI9BvdX2wpA9ofmGlLwf3cMnl8fobNdT0OaKrkuqaEmypyKSPn1t-KeHlcqj5VOeuJSzuqUcqAajSDOZY39R9V4YOwCs3AVEraSkA2vj14rMNcz7FMFJxUULTgIY6POwXWrvle1JMZNCqT8T7IxPKKtB6Fsi50Hk1SLUAOicy9sk2iTOl99HIwgt3wrmmcAdNITAu-zl5u6og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=o3CF7CPj3sM_TlS3UY92aAtWgXrCn5aFzZJUfPLFv0qJaz4Sobx6fw4_AeuNu_2wH4-xl95sTNjvBHvbblN5Qu1UXQbK6CtILKlGtr4eDW6qT_wrlfj-IaGzb_4hA2KQkqmz7GkIifI9BvdX2wpA9ofmGlLwf3cMnl8fobNdT0OaKrkuqaEmypyKSPn1t-KeHlcqj5VOeuJSzuqUcqAajSDOZY39R9V4YOwCs3AVEraSkA2vj14rMNcz7FMFJxUULTgIY6POwXWrvle1JMZNCqT8T7IxPKKtB6Fsi50Hk1SLUAOicy9sk2iTOl99HIwgt3wrmmcAdNITAu-zl5u6og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کن برا ۲۵ تومن حقوق مجبور باشی بری تو باغ وحش درس بدی، معلما واقعا بدبختن حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84730" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84729">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKaXHuYypUMwSDDHRRRuDZWwtivDFtRcykey-ZOql3mWZwYdcTBhUclbIr-i6Vhs7ELRuWYRP8pbcvs3xs-hqsxnu2vQB_9gJCmAZdJTGtm35w0ijnjDWOuGZNP0600bE8K4bOEmb4tW3Nm67_tIS2lS-zJoqH6rKP2razYqXQBTGa087dSTxAGmg0iPQdZc3kaGeTc3TmCyygjzgDE8stxHOmb63dCeqcl7z_JK1an0HPn_0WDW1tfKCw1IBhDM8VyE2tFknuwHLgKZL8VCPXyqixFE6ZOW5UMhrbZYTMpPX_FvKSIM1ljPTj--3ZZX3C7a4RyEI3xwQFoVNQpKEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G20
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84729" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84728">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شاهین نجفی میخواد بیاد استانبول، دسترسی بهش راحت تره لطفا با راکت بزنیدش</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84728" target="_blank">📅 19:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84727">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نخست‌وزیر بریتانیا: حمله به پایگاه RAF فیرفورد تقریبا به‌طور قطع به دستور سپاه پاسداران انجام شده است.
اندی برنهام اعلام کرد:
«می‌توانم تایید کنم که ارزیابی ما نشان می‌دهد این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریبا به‌طور قطع به دستور سپاه پاسداران انقلاب اسلامی انجام شده است.
ما چنین تهدیدهایی در خاک خود را تحمل نخواهیم کرد. با استفاده جمهوری اسلامی از شبکه‌های مجرمانه مقابله خواهیم کرد و از تمام اختیارات خود برای هدف قرار دادن این شبکه‌ها و منابع مالی آنها استفاده می‌کنیم.
تحریم‌های بیشتری اعمال خواهیم کرد تا توانایی جمهوری اسلامی و سپاه پاسداران برای آسیب رساندن به ما را محدود کنیم.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84727" target="_blank">📅 18:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84726">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شین: پرتاب دو موشک بالستیک از یزد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84726" target="_blank">📅 17:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84724">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZKAO3DpkAo0Fqk35sWGbs4GFVi-0YaofrwW1YQlu9yLXYkcTVDtj4egneCBdZSza_c_TAChJiZoijFUGkjnTzjlU__wbapNe4cqycE2FOR0JfxWGChZ1boqvZv8PBSZWYQl1oEWfoJ0-VlrJ6W4kGAEw57GU2rJ9rB2zdGCNTgjrgFJ5SYMMexFOs4AGf0E0H475wPOP3L3RWkorwz3ZfWs8o4kLIs484J0Bjbup6-DtQjPBE_kXATqYKFyydlTJF2FgyGqSU-eSKyFgj_eVNs1VhJQO2Y1OxfmpucrtI-fWJ-DFan6TW17UqLNJHytdNIRyAulfQ1jV4oFlNSOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YPKj3OShF52NxVtG0Vt-ZWTfKEWIfKX0sCdw0cp0w2fw-0DzONw8EMDr9oe_FbwW-nHEqRIzbUi7p118UBzC72Tbut-ApkGmCIyI2FyNOkCU2Ccr9wNKBZQ5oCAvDVqQsIEmndMVJ0rs0wgRvRRwnt4S5cz2czZf6QcvBFzvSFLVB4vwaAtzmIUiN76_NyglcpvukWbRCRkopbki96pXoV1x4i-LJds4gFOi2ZGRJerFOnH5bt-Q-iffENS3ULi4eJUncGL-eMtnpKaGKb27lARHm6HmTEYJPAQ7WSDEgFpu5gUae1apVbRHa3DbhvzELp9KoU0WMGQFKAHVPq03lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84724" target="_blank">📅 16:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84723">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=p5y1fBqBtTOffdlk_GhxYYUl-oN_cwHqeYToYPCO0lPOtfNObFarf8BYGY7oiE0hfOXMcBrk9fU9pXEIVMZZgSXjq5I9GbGVA9XFDH-9uT3fnadqvmevd2TLPSl2ayWSeDZb05eIIdTknHqnuF17cU_LDNF35sUBBMmIwN2D9vpkxzlqdAQsTmMG4Qb80jlfVatpGx07iRVLju8o7AoGmggtHpIZprIqfjIsXGZG3HJefCaiXHvW9F70a9FAmjoFimtDyYgyGrXCt7gCc_fawgctbCHJUflGc05D0BY5OcgZSHZ2Y56sHxP3lVN6k16yzveFRiwJS2JUVthviJjrCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=p5y1fBqBtTOffdlk_GhxYYUl-oN_cwHqeYToYPCO0lPOtfNObFarf8BYGY7oiE0hfOXMcBrk9fU9pXEIVMZZgSXjq5I9GbGVA9XFDH-9uT3fnadqvmevd2TLPSl2ayWSeDZb05eIIdTknHqnuF17cU_LDNF35sUBBMmIwN2D9vpkxzlqdAQsTmMG4Qb80jlfVatpGx07iRVLju8o7AoGmggtHpIZprIqfjIsXGZG3HJefCaiXHvW9F70a9FAmjoFimtDyYgyGrXCt7gCc_fawgctbCHJUflGc05D0BY5OcgZSHZ2Y56sHxP3lVN6k16yzveFRiwJS2JUVthviJjrCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ی نفر تو ارومیه اومده واسه ی مسیر نزدیک اسنپ بگیره بعد اسنپ رفته بخاطر ۱۰۰ هزارتومن یه راننده از ساری فرستاده، راننده و مسافر هر دو پشماشون ریخته:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84723" target="_blank">📅 16:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84722">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krT5aeCyHmbPvkDeaCGL_aEqk3IZyf8wGfM-wntai8kRhjGBHILzK_kBvxSGxMilMP_MqBcls31fPSHmtWR9XioQiewcu8K3BrdU01QcfrquQE-4K_4A5eMRAGu_6HPnb4MXDG5aAS1uTS1TG7bxaeC5KsZ1B_8z_Pu9Rcv32atg4H0VW6dkrUkrLqVj31PFgAKIRBdojYgBMR-OK6bk6MnNasij97uwc8xewzcAoJ-SBEXQd7LZCwpXtI2Hu0awkoN2NlaCAD2MvWErwC30qhyIoZ0QFdLtdMyjLORT4qRupavEnxnkw8EXM7NmspUizmRVbPdqlaMMA4fCJ-RVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84722" target="_blank">📅 15:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84721">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=LUqE_402FOynBFUiECUgKN2uHlxzoERxTnaPa6nY5vk5-pDZUc9MXUpY6M13qvvDd0ycwukn8qKpgVjeClm9ky2_2S0XpQYrhmBi2NmsLyoJha8u63rDK-Yw7FC8avQNnyy4QFt4CIT4q8KCU5zL0fi1wAWzY-MB1JuR7LV9Vbv0Nm8A8brObFfoEvOGMqHYlT7kNuB74tH0rlgpECHxIz1uK0r1ZkhRu6nosBjlInA9_tWEqYxULE7XYilv2l-8DlMJdO9_ZcMD7MuyYhtVcVpmiN5Cdkfvb3y2K8xsEEPQmLJsB9Pi4mlvpdBChxcRGMcGc23tA5LzaI3NTxX5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=LUqE_402FOynBFUiECUgKN2uHlxzoERxTnaPa6nY5vk5-pDZUc9MXUpY6M13qvvDd0ycwukn8qKpgVjeClm9ky2_2S0XpQYrhmBi2NmsLyoJha8u63rDK-Yw7FC8avQNnyy4QFt4CIT4q8KCU5zL0fi1wAWzY-MB1JuR7LV9Vbv0Nm8A8brObFfoEvOGMqHYlT7kNuB74tH0rlgpECHxIz1uK0r1ZkhRu6nosBjlInA9_tWEqYxULE7XYilv2l-8DlMJdO9_ZcMD7MuyYhtVcVpmiN5Cdkfvb3y2K8xsEEPQmLJsB9Pi4mlvpdBChxcRGMcGc23tA5LzaI3NTxX5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرین حرفه ای کماندو ها و نوپو تو سنندج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84721" target="_blank">📅 13:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84720">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نظام‌وظیفه با درخواست کمیسیون پزشکی علیرضا بیرانوند مخالفت کرد و این بازیکن از اول آبان‌ماه باید به سربازی اعزام‌شود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84720" target="_blank">📅 12:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84719">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پزشکیان : داریم در تهران آب زیرزمینی را استفاده می‌کنیم و اگر تهران هم با همین روند رشد کند از کجا باید آب بیاوریم؟ باید برای حل این موضوعات چاره‌ اندیشی کنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84719" target="_blank">📅 11:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84718">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scZZMjocR0u9AKQH_nut9_p29orOVT5M-dhybAH57HFLpqNxCvbEuoVlLlz82e_f7jhF0_G6dC7W40S6Ra5qKsU8b9OVzzYlLyBvOi3ASeFrQU_Iq6_MorzZoUoAuCN6WurkSJMFftmmlPNnSn6h3TuGbsBvTxE4q0iPnzTSKuFWOC8XxakBncKR3i6mgAaQ1sFMI5wrZLVj3o2DbMXJhTdqMkjssMIjDqg8AVyL3rdSywKC67K1gNTcGVjkwyiQNtFUWCfPLc7shZEk5YMSv0Ev0CrAQDrTYA78j_8bU7MPEQG2MHEZ1gZgKYHbvS7eDU2NYRd9KYBTnV1LxJGqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84718" target="_blank">📅 11:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84717">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=m_2eT1XQjLUU47h3bZ0QcNb8TyTPUCyE_7rFDi5r9TbRlhXAeyRBFpj1Sk3hmImXzOletJjl7KMpkJf6TYEbx-qswEJe8HK4558F2sImdVEEBiMx1Nu_WHZgQhL_iKg-7TR3sBH2B2ATBzGjhM45EJl81u8DGIcQS6Slhev-JxYg91aMaYbUOPNNYwPAPOBNou-I97uNYIdpyipvxTeBn1iopkmvi7WSr0n0bjZAtlSHel8Qslk9jJEZRWr6fGK7cTAkh7ur-yMIQPtc6B37SxP5pMeyQazOqHDiz0dfhjx7D9QEmsmR5owLjliHhUBBfeBTpYKTRELZSTmn6IF1oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=m_2eT1XQjLUU47h3bZ0QcNb8TyTPUCyE_7rFDi5r9TbRlhXAeyRBFpj1Sk3hmImXzOletJjl7KMpkJf6TYEbx-qswEJe8HK4558F2sImdVEEBiMx1Nu_WHZgQhL_iKg-7TR3sBH2B2ATBzGjhM45EJl81u8DGIcQS6Slhev-JxYg91aMaYbUOPNNYwPAPOBNou-I97uNYIdpyipvxTeBn1iopkmvi7WSr0n0bjZAtlSHel8Qslk9jJEZRWr6fGK7cTAkh7ur-yMIQPtc6B37SxP5pMeyQazOqHDiz0dfhjx7D9QEmsmR5owLjliHhUBBfeBTpYKTRELZSTmn6IF1oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره دختر اومد تو اکسپلورم باورم نمیشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84717" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84715">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfqFHEPUIzuHu-nPCYnRBnWxZ9pmvZRFws-ADKX1bLmC7WjoRgA3JDZb6A8g-ZnNw8OD-DP4jhxugA1GK4o9Azwf9JTrK54hOy1-Qy_Dxkq5GbiR22r1n80WEytEcRpExg5t9P9HLC5Kv1iCvICBKNu8BXVqFoA2GWPDhgalLfY64ywEGs6fvESEElWOKhZhloHFz_d9op6fLcR0szk1FWdIanS4-ywiQAm9tA6gYnCOWWND4E7kOe6ST1lJyXrCG-0Locy90xnc3H1PvFZwRCQRdJ8NsmJlWOQSYaA3604gXigvXJ-OWiaIqGO8H8x5ef6-P1fmQRCifcg8dVLz5A.jpg" alt="photo" loading="lazy"/></div>
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
r20
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84715" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84714">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=vFVPirMrk6QPvosPftMR1tmlrITenY9JQUyO0_-V6tqEXDxOzCwBrlSRVuD_9NTxOD_lTW_OlMpAyhEZEbFZdbQ-8Hf5e1QZNLfJhCmaZod0DnkAOcuDvQxt00OjxC4yiRYsE0uRBDLhlHss3cvh6dQ94AAAJACn617b_tfPrqc-DyYfG36Xg1bVRQkVp_jgun-wRGKlVaLp4FqLcR2N7wYltdMVqnxYs2wP0VOEHkEgJXObKYdSf-cyvyhCiXG4N9kX-55BjfEdEKk0uHJFOwBwivBAd_mWAiXlV5I_kcgvkTInto-hFjmLSqW1MgMBouQmzkqp07JGX1yJRnXGbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=vFVPirMrk6QPvosPftMR1tmlrITenY9JQUyO0_-V6tqEXDxOzCwBrlSRVuD_9NTxOD_lTW_OlMpAyhEZEbFZdbQ-8Hf5e1QZNLfJhCmaZod0DnkAOcuDvQxt00OjxC4yiRYsE0uRBDLhlHss3cvh6dQ94AAAJACn617b_tfPrqc-DyYfG36Xg1bVRQkVp_jgun-wRGKlVaLp4FqLcR2N7wYltdMVqnxYs2wP0VOEHkEgJXObKYdSf-cyvyhCiXG4N9kX-55BjfEdEKk0uHJFOwBwivBAd_mWAiXlV5I_kcgvkTInto-hFjmLSqW1MgMBouQmzkqp07JGX1yJRnXGbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار دعوای دخترای دهه نودی بخاطر یه پسر
انگار یه دختری به دوست پسر یه دختر خانوم دیگه تو اینستاگرام ریکوئست داده و همین باعث ناراحتیش شده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84714" target="_blank">📅 10:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84713">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">روسیه حرف ترامپو به چپشم نگرفت و به نیروگاه برق خارکیف اوکراین حمله کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/84713" target="_blank">📅 01:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84712">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به رضا پیشرو ميگن: از مسافرت برامون چی آوردی؟ ميگه: تشريف.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/84712" target="_blank">📅 01:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84711">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/84711" target="_blank">📅 00:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84710">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دسسسسسخوش و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/84710" target="_blank">📅 23:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84709">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUXBzSJrl4BAlsDRabGXNeN4EL2JEwoEznHdddqMhZS0IsUVMkhxPL9DOSPBnacPzdw_6CEC_cV2IQ7tSMXb60-6l-7eWBOMNxQyMyVAJMqEN-qKmedJ_dTH-MNJx6dBcW7t5yY10pIpS2lIqYCq1R351qXf7b-nBmmkeI0fD5aWOzzJySsI4pz9a29Z8AjJ3X4vc2exiHnnHz7Ony6nzKdu9JRQBtG2ZphsxtFworOv1qvdqF34hdvJFtLuN2TrSg-PgCoxobbYXYxlipIcT_81ckMkHEtr8sdilJli2I4O9VHPfgUqaEDBUCvg_UXFJACTzyUALa5sQ2-9q8E-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان First blood از اینجا اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/84709" target="_blank">📅 23:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84708">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84708" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84707">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/84707" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84706">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خاطرات وینی پرایم داره برا ارائوخو زنده میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84706" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84705">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوکو خداسسسسسسسسس</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84705" target="_blank">📅 20:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84704">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUUpHsrgLk9Vqnrghzx8-CY7_Vqi7Yg3bBc2X8tmlSliGNYeMYQ4YZokKvPGbeL2upQwem57H3Gr2fQZDLKL0W5yx9qEpIQ6qjs5453bxG911nsFjFk_pabY1DCsu6P9VFq0BhqPrIzHP5tiII2qnyFv-vRiM1R93POfkwAI2TpyQm8V6UWBwVjkBLVRCcMHAU2IYFFGdMaloA3NVMzp1z-hjjzom0a-_fSeGxav04g_eCE6sZZU_GyHrxP_B9YmrE27R0sk00_a4I0mjCLqSNEttaWZMpSbbFRDomEPllA2wurofARN-vqvdUz2c8_6afpBjimLToYD_nPOGQZmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه سخنان شگفتی به زبان  می‌رانی، ای مرد؟
❌
چی کصشر میگی کصخل
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84704" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84702">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C429-7CZ5lJZQ7U_yjkjt_iRbsQwKcX7Ubm24zVPxMmSSuApomTq0ftTs1wblIWIR8ExS0iW0fFhBhsvBSIdoOMblHOw1vopJNxAhSumn7gnpk7e4w-OVQwn7nO00NA3yl11-ULORXl-0u5047DxBC_FUvdTpgeTcJQaCkzn28ovILl-2bOflsF4ss_q9ybRzK3dOgLqohcZaZU3Iw2ff4tpGYjI9ctd8Zt1yUoHmqMvPbkTt_HBu_kdg0CLM8pHqMxy9jLPmEbmMTmpCPofOt6pnIPqOwCGYSjh2S2TipzdthWqbRbzdWjT94ljc6kdcRPZjM3hH4omTyzLmYUUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بابلسر ی کافه افتتاح شده که با پستونک به مشتریا نوشیدنی میده :
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84702" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84700">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veV_dgRC6CCyvuHZ5BWrGTVA2Pw3WYxdLpnr3dhp9i4zjBqtZnjo_aS3m0X2VRQlL5sObyp6RhkSuZX_1aNU5sUmY28m0F2v7pHoXO3dz1m05Kvc61jAr1g4aH77OX4plBTS1T6eGmUyKHqStafekl9LCNatrAaBYMnRXw_umdD_HclikBMgeKJME2ArIDideMBMxQ8mb0d6EPTyKdhdHnAK9UPg0rEnfeeXbi9lmPTADRPGzeBBHsZlLWPwIbE52pfggwL09iMAZyZ20w3VDjkfLYKh9QTpo69trL8zFW0m7tdKH9A2X-HYfvgcD1eeaTss7cCGGRQWV1FV-c6anQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به طرفدارا لیورپول صبر بده، حضرت ایوب هم نمیتونست همزمان مونیوز و بارکولا رو تحمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84700" target="_blank">📅 18:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84699">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LocO14CuT9jukVD166yzrpuCWZjEUg3b58jZ2cK5ed6ge0rWWC9VH3qS6fc0NpjL2D86UDBcuUTa0pJg0CVkvkeI0KJSYy8xJz_Bln7zy66dh-bMc6Djfuh3JCtzsUqeMKMy8mFBGGgCeAkbJRdZL-0q38ABFphGOZQKEmOeMaQqBZT8v7BCHqSxUQrTHf7rsHV7ljRHXHWVkjfRzgv3lhvHNc8VBhOnGT4sMV4IGDo4uedfJ3xNTXmZ0i4D3ZQ7d_AsJBBNCYuSCelw26esDJqk9Oo-s8tyaMeg3zL8X3L-LuLCEkkDFPvYYsRxMhW0HeGxIFXb8gHiXmKklL1uOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیری که گل‌گهر برای رسیدن به بحرین رفته:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84699" target="_blank">📅 16:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84698">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=he-fTu7FZlSGgIB3KXsSkym0p8q7jtl9eEH1pJMpFPMfrqkOxvPuL2OF2wplI3IJhRFVMZwOpNvB6JMM_f0MC7GEZfmhuNfJ0rLvHmYjT3bOztz39jbVQMz3vBv9sJO8F-md0D940ubQqVfao-3DsjBSGN0dW774t8JtTKkMWS-3TDy91IMk5LdPOPMdG8W3SGB6EAYJoYnba08ZigKEzk-8KuzYziLvyBImqWCtjNZeO6dilW1fPMv6eXKstMd2K-xkqBOokyrtDZUT8irKhSwC81kaquSt04MR_vU8pVOefBaVonPMSEBQ-IPdJjwt3ux5qqtz8BZMxHLFs_IJzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=he-fTu7FZlSGgIB3KXsSkym0p8q7jtl9eEH1pJMpFPMfrqkOxvPuL2OF2wplI3IJhRFVMZwOpNvB6JMM_f0MC7GEZfmhuNfJ0rLvHmYjT3bOztz39jbVQMz3vBv9sJO8F-md0D940ubQqVfao-3DsjBSGN0dW774t8JtTKkMWS-3TDy91IMk5LdPOPMdG8W3SGB6EAYJoYnba08ZigKEzk-8KuzYziLvyBImqWCtjNZeO6dilW1fPMv6eXKstMd2K-xkqBOokyrtDZUT8irKhSwC81kaquSt04MR_vU8pVOefBaVonPMSEBQ-IPdJjwt3ux5qqtz8BZMxHLFs_IJzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا ابوطالب یک رپرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84698" target="_blank">📅 16:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84697">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دختر خانومای گل، روزتون مبارک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84697" target="_blank">📅 16:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84696">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVZFL3LsJetN1g3sd-CC1b_ZEq4M0u0SJIoRaTJio9YuqAZuSHIKFkfmdrlEAGzEENATSDh4qrtu5mmmRW9hM5lSSmVJPpVPjUplNpMPpN4cTlcEEQXiKh0Hx9N85-rYwe75YCRX-4dSTveiL8fpRvDHDJdFK8aUXLfRhrLMo5lX9ZJ7TO9gFVezWygk0prf3a991m9Q5WOjXsx17h-nVVsJintooE98CpVGjJ751V_SmiJTA7kNOt-FJAKM49S6g520BR552owrVsjtvaj0N1SMp1SVKnDyzt_ibPXlMThDxosTpTuKpckcMqEP-AP1ZehSbgnZLrCFD_hHIh-nHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراز پدرته کصکش، حرف دهنتو بفهم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84696" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84694">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaYPrfZQJy4FEAqPZjDPgET0dbEJUC1FcuovL0TIDziZrNvltzQXTC5dyD2rpRMqHfMJcnN_RfLX7L36QNCzYPsKNQIdxTo_EQzic3kmN3pQiXttZRihraP2GiKFcc_ChqHugIMUCWzNCPNKaZ-QNOPIdVTQhHLVYFwCY6xJS7O9LfWEYAscx_52xsbO99JResfAIdOAjUKWYSJWh4amo4tVWw09WRPzQmsGuB44Slo0Y3vw_CML6qqc28h5_R2ftJhLJaRXq70QGJifjUi8iaIURmVEhdx_I1z60R_e7Hv-X8wLMi5G_k0mUHnUp5Axnb_-R8VoyJIBB0g73MBSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم یه سری رفتم موزه همینجوری تابلو راهنما رو با یه شاهکار هنری اشتباه گرفته بودم دیگه نرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84694" target="_blank">📅 14:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84693">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">زلنسکی:
اوکراین آماده است تا حملات خود به پالایشگاه‌های نفت روسیه را متوقف کند، اگر روسیه نیز حملات خود به زیرساخت‌های انرژی ما را متوقف کند.
پ.ن: این ترامپ لامصب چیه که از یه راست افراطی مخالف مذاکره که کشورشو به کام جنگ با یه ابرقدرت کشونده همچین آدمی ساخته
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84693" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84692">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=h4Kbf5TgGIvZFPRL1WR09M4eKC_bhRlXA3I1Ln4sGlvi_4xatYxTWX7GLkXxOoo9A0iC7FYsksQbWDbMCJLjOmsy8MKB2JccSQsBqZfzM7biRo2vOXukFLdnreCkkza1lfebN2yqsCp3kc3m3FVed2cp6KSaJcEj7g-1-k74zoFt3ToruyHxHch8Y4g9E0AlNAJePWDZf0asCYicCd80XlEF8uUTco_kDBQFXNQplJ2sK9VY3Pdhc8_AcG9_UFEYhtXCOl3RdODWvUQs-UDRhy1faE1cq6n5Y7-i_7DLFjz2zVNjdpYSZFBZbv79whkE0ojxnHSBd4_56FECaGieDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=h4Kbf5TgGIvZFPRL1WR09M4eKC_bhRlXA3I1Ln4sGlvi_4xatYxTWX7GLkXxOoo9A0iC7FYsksQbWDbMCJLjOmsy8MKB2JccSQsBqZfzM7biRo2vOXukFLdnreCkkza1lfebN2yqsCp3kc3m3FVed2cp6KSaJcEj7g-1-k74zoFt3ToruyHxHch8Y4g9E0AlNAJePWDZf0asCYicCd80XlEF8uUTco_kDBQFXNQplJ2sK9VY3Pdhc8_AcG9_UFEYhtXCOl3RdODWvUQs-UDRhy1faE1cq6n5Y7-i_7DLFjz2zVNjdpYSZFBZbv79whkE0ojxnHSBd4_56FECaGieDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنازم یه جوان فلسطینی که کشته شده بود بعد از به صدا درومدن آژیر خطر پاشد فرار کرد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84692" target="_blank">📅 13:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84691">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iICocpPdb0PBSwij-M8N8vCvMlnHV3Q0cbl96zt7fVuYMEX5FzOSklOtOI6AsoUDrWRSNEOdMzv_nANgW7QZgU_14Vd_K4OmHYH1km0vEROmYU1WNxma5RxK0OozS4pO7YiNO3KuwcTUX6NoTL3_zC_uw202qjnA2g9SHD14qwbHwZ9YDddzCuGZyr9a9TB6dF6lrbwkCYup3LJEbfQnnE8oVLE5dMIvsS5W29BwwgDd4A_o6Iwi_RXtasMLmkqOxlCfeXL6mEOMoCtsH4vIx9QrHwlph_0yi7ECMsMXTaBJFPiLdyQWekcDMWSt3TlKfkumK1wdAXY2OImhU3iimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگتون بالاست مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84691" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfcMn12-s98ep6yN_KHWMotpiubHaeeAla5yrcCsL7doGIoJva4_jflrHlIBOISAkl_1T4TqqujCvm6L99GvFQ2tM_6KPqguam6igzOEcCKMDijF6SC7PLJtWu0AT_mIFrvOjs0G7lkVz-Nx6re2hgJvMy5F5cbToifZWV33LpKJ55HDgbhuYdUv7WZ6jMkEBNERry6MT9KdLZyBk5yO4csWp0HOIZwDg6KQszySmH_dlPx1Nw7wGSVpEtaB37qIWth9ST1OakOIdccI12rqiJcBpEE88RxijdqY98_tS2EgwdslQwvy2F5i_HsgI0WFzeQUCbYjezxHx6QGucqUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دم هرکی اینو ساخته گرم یه ماه بود از تهه دل نخندیده بودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84688" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQuvJD0Fk1tl4R6bQxz7ttppbxVdvNViOuY0NnhAcaBOB85uwKuX3j4Jw-WWJOWwPqKAOxy9sbdhgKwdXz0PJM2vxY_1rfuEtJo4A5seGykxk1nw7aUHfjT2Q6JnZOFlOcmCN_d3V0tHjIAPDMVJO2nA-OM0L_kZnFBxlBu_CFx9Uz7utBnxS2SrB2-CCNCTt9Llrj3O0xC4ABk5J7dvvhdmu-mKQ_DDp4wTWm2zCYnuNby_w0K5sAlVKFJGPomAhme7wS5MYnXm89CVIPu6NVLov7U_Y189RkII1xqd3V4TnpZgQpUSmeoCxNWLLpfQxdB1_l7aNyVpNL3QkCBZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم واس دلت دادا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84687" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84686">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">داور کسکش فقط به من کارت نداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84686" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=AaK-LLS2s1TMhXUyJlLh5HRMU7pYVyB_MI8aFwEeRiz8VLNzjT-u-5KE4rOWVcduWEIaN5zZoKS3Ps3uTG1Clcw1YueKlikvM0YRlR0F2SVYluwlNKG59MqcuWEVpFbzjC0RwIXnWMQYsBgoxBGOTJrDghlJ3LADSCMh0wOdq2yrSBEudPkpn2JxImx-Gpb3Wtm-E4CdAXa0K1dQHqzgmpaXRxCUSJX0fAKkIi26o9oxbvwVwWYjNic7zVC5A8E_15pXlTJ6dow3kABQNaFuDGJInEwr7y479j3bk5vCUSemYcXbkC1l78jDnV0z6HYh3IsG9otpCzVeH7lWW-dOYJDd9Qw6DHwwbama7MeZGlRSoHDmv57ETieCtc_3n4Unx3WCnGloV1w6RgR-9Ltg5Jdb076rQ6F3OYcSzEESYmatKjSSBRncz5Iz60iljIcAstekfvCLbWp0i4HrIUgE2TAVNtuBQjzKmNFZKx-fBh4_CHoLToaFU21kdCg4Y5bLQKnd3g_rzjaNIHDHQM6INLXN8kS8irNsUJ43mQfQXJXLvX4LwjOTzG_eRQD-3GkLK7YvizBnVWw6eW4O0RF9cVKFaaPrsYDZ3Q4L1sqSTIYRQnwHZjGFo1kibGqBbftTau6P3kHhgjwa32y5BDyehQGMpuUSh0p3Ch_DeL2vixc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=AaK-LLS2s1TMhXUyJlLh5HRMU7pYVyB_MI8aFwEeRiz8VLNzjT-u-5KE4rOWVcduWEIaN5zZoKS3Ps3uTG1Clcw1YueKlikvM0YRlR0F2SVYluwlNKG59MqcuWEVpFbzjC0RwIXnWMQYsBgoxBGOTJrDghlJ3LADSCMh0wOdq2yrSBEudPkpn2JxImx-Gpb3Wtm-E4CdAXa0K1dQHqzgmpaXRxCUSJX0fAKkIi26o9oxbvwVwWYjNic7zVC5A8E_15pXlTJ6dow3kABQNaFuDGJInEwr7y479j3bk5vCUSemYcXbkC1l78jDnV0z6HYh3IsG9otpCzVeH7lWW-dOYJDd9Qw6DHwwbama7MeZGlRSoHDmv57ETieCtc_3n4Unx3WCnGloV1w6RgR-9Ltg5Jdb076rQ6F3OYcSzEESYmatKjSSBRncz5Iz60iljIcAstekfvCLbWp0i4HrIUgE2TAVNtuBQjzKmNFZKx-fBh4_CHoLToaFU21kdCg4Y5bLQKnd3g_rzjaNIHDHQM6INLXN8kS8irNsUJ43mQfQXJXLvX4LwjOTzG_eRQD-3GkLK7YvizBnVWw6eW4O0RF9cVKFaaPrsYDZ3Q4L1sqSTIYRQnwHZjGFo1kibGqBbftTau6P3kHhgjwa32y5BDyehQGMpuUSh0p3Ch_DeL2vixc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
این فوق العادس پسر. من میتونم کسشر ترین حرف‌ها رو بزنم، و شما تشویق می‌کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84685" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84684" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84683" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1UKR_Q_-5slTr_bcfiSB1jHUR7zclDURFQrx_5t8n2TsRAnDpi0q_hiMIECuR021AIHsrl6AXPhB_RSN0nY2CwV2oSGqyYcKEsx8OsK_JzqJZlPDkDzcvTYe926RKbLoJKGguAPxvtQU3kj7YLTJX07hw3UoZZxXqOrpaCQs-xg239bHxjV_6lhL8CIXB2UiF1NLhOVDuZaB3Syk-RAzEvh1alJkG3lQRRUhBxFgTtckxWw_iLKdX3gqNt9vw-SMicuDiq6KUTz7SzGnNDzutyBs-jJkUR1T2K_McKaDqPgow2QgcTiqDFG8oo3EqMPoYJXWFF5WYbvLAFgCc21uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNwhRqFHCQmuFzYWWSC1Owhfz5XfEwLhYIHpycfLgeQ0danDxa3IeKr22QGjBOqXFcQPK7NjPaZ66tic3WelKlnPUvMdaoTzW-ISIzClo6RacP2u3ZVNtmqlg3YAvp4XbsbSnJvSLiys1KHZaQsL7HZ-ca-ApEka18vzqhZ2kceBA3_ICbyFOzS6v5tOocbSJanEGborgeNangqIwNqxeb0Tk3Fvb83vYDCiVBdtfFmBWULhPbqMh4qnKW7LN4r6rAu4J7oz0Hl9h8WiZ2HTU9G2KzN1bAbRTks47v5B96rhVmZpGVpvcpyn_IPwc4EXDzXeK9oKeWD1OVy4TunIJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با پاسپورت شمرون به ۱۹۵ تا کشور میشه سفر کرد؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84681" target="_blank">📅 23:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84677">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtMNrjYSFjNtu9D4mqnTRU1bTapYwOGsIhrjyFSbllr6OEYlDj6uukRfjx7teFo1ndLjd9AaPY6k7CNpvysGxIxS5hgcl6UlmBUfws30HYC-6Bz7CEFqekgHxTqXXpa9N6ZlaCz-KiQAnQyaperJWGg6yT705COx6oZxz0lP575ZnE_cUKkDgxKj28HOtBInnOXzU5idjm-hfZpn1HVOai2P9qv2RGQ25edctZZAwVPvqMTY2vPO6oxnGtJN8814jVrq9AAYYpAJejYtJNlvW6D7y-Vaah10u3TGsfNiP6LEUVoDE4B0haPyTx4aI5DVC6a_yQqEvj4cDVp_7HsFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2Q0fMXrMQhDP6lJgyhD5hTem1DcXfYm8CjMWhuGtg1qCCWFGqW4K--Ybay0N21BYSJDBk2eQ5afZvX18sP68oNZ-b1Tpo1wYGn7xPjFYNV3Guix5OHO1Cm4GaQdHOpb27xtyOoGLxUP9i9XMeROhS6KCe8NJFVVHJRLaIlnH1YLE0WTuLDe7sLiRKWzJf9GGfb6ouFGz2G4EQec5ceRIWNoSHnpECsCdJoc3fOO0JsT_tRBzDyjqG13dDfCosl9i1j6Vqvf9lRnqZcYVm-gKTz4VjxlucbuOGIleUWjkeMr8Jfzk51wEGvnHQZmsjhaEFuS9mfxY3I6jzM8NKjJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKYgUKnP3MTfNgUONAX1-Jm2fzagf28ALHwuiQDT3yq6mXihLXaJCw3SOaEXCH4uYu5Of9csiOfCcD-KZfN_xWtM_37e1LR2IRFFHTPRk5akVK-ISXUZSbAk-hTXS1rpI8iVHcsgnzn5ijbv0FZsxO0cwK82NyiuZnvs7hrdFh02662cxOCezY8PLWAT4vIq404hV_LwD40rzGlMzz8Vjjzq52bgIv-44WgEVpKbzLXyAp80fjR6ezy7AWhbx-gLtIXpmkDP-HHiXgLHtnIE8uFM4yypNTxx8dPrQ_k5zlXJfKrMDsLJEiF5-_0_QT0KohD7OEKhPUfvzJ3LtCOb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8syFmkyL8C4-Yczp7PJDm37WWydMqLgYoXd5PkXNhquF4E7_ahpsmB9XtQdZiRq0347N3sanQ6YI1ayb7-GN7bdroxnAFLR8X8nHfG8KRsCy2nntdn90-rzNbI4X2jhyxbdB1Sii-Vh5w2RydonlMjpbb1rAnGOFP7NO7K4fxek9IaH0qQshCcY97RvPCaLdtTWZ4agkw_SQpqgNw0ramYHB_YVm7p4NG4VsCnumBE72p6KRLie0H4SCWDV4KmAuWxspScNXhlh7z6zhAfPfJldAVMJnZRq5TjxOa42T3o2Qus_kKBrF1pxu8w4RbghkGHuQnBSs6oAWs32RgVfyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسیجی‌ها امروز با پرچم فلسطین رفتن دم در سفارت فرانسه که به سرکوب خشونت آمیز اعتراضات تو فرانسه اعتراض کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84677" target="_blank">📅 22:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84676">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=dndo_rIcNx_areQKonkpYLx2k4oqmwGCtT7sQLiPQz_A6YhySXoeB_otjXWeTPuoQh5wK0YjTcjwqBhHJpDImy-WtwNS38J_bCN5kpEA8jbUmxaECDnOx0fD0OTak4lsvcGI_o6b6MlzcSJYM_OeVq9HycONOzT0jVkB5if7kbLkm8Yea924CQqViz21nxuhALIXU66mJFowOGVu_fpg9mRVFPWwq6gtsIbs_2_woDQR_u3H3C_mX723w8HTWqU13aQ-usRepPXWyHGKlYvvC-bFNdQUdlh1SHrXjFmtM-GKPu1G4ck_tMH-3FkCD68TZkzC6iCDvXlPjsJdKPWbJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=dndo_rIcNx_areQKonkpYLx2k4oqmwGCtT7sQLiPQz_A6YhySXoeB_otjXWeTPuoQh5wK0YjTcjwqBhHJpDImy-WtwNS38J_bCN5kpEA8jbUmxaECDnOx0fD0OTak4lsvcGI_o6b6MlzcSJYM_OeVq9HycONOzT0jVkB5if7kbLkm8Yea924CQqViz21nxuhALIXU66mJFowOGVu_fpg9mRVFPWwq6gtsIbs_2_woDQR_u3H3C_mX723w8HTWqU13aQ-usRepPXWyHGKlYvvC-bFNdQUdlh1SHrXjFmtM-GKPu1G4ck_tMH-3FkCD68TZkzC6iCDvXlPjsJdKPWbJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمسه میگه به خدا من بادیگارد ندارم چرا به من فحش میدید
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84676" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84675">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlOQr6UbiigtyDgKhiNkXiiHjYGaQ-K-sOz9jfNa-6vm7Z6viCWmyklqvIEMYJJp7ju3uDrIbXFucLOlIyOKCU30XSZhxZf7GprPiroogn-tPooVkSC151ZXCXKeLSONMwuji9h7QDJjvnAXjGR_U78yQjI8fz-1eICFqMZ7hRu1F-AcXNctiKxyM8fD7u1aIc5fW0didBf4HJvboYPGl8K-2Q0YcHZEUXMFiHHFjHTg9ex8RFHV6c8U1ZRISX-ok9yofM2XBPwrcd717NyLTFrdrBkfD4k1KVut4KA4U69Mbe2fA9SvywfkytrSsJDC02AEe5QuQKt0egRDcjgdIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم.
بعد از اون کامنتای مردم، اسطوره نوید برگشت به تیجی گفت شما اسطوره و مرجع تقلید منید و افتخار می‌کنم که باهاتون تو یه خاک نفس می‌کشم؛
تیجی هم اد استوری کرد نوشت پرچمت بالاس
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84675" target="_blank">📅 21:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84674">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Talangor</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84674" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84673">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbkAcaEQYj00SUzPVQNF1h5G_SoldlBm0ovERUpBU4hfbyEge5_H-l_QDtVbMv7IqOTp_2T63066syRX5kAX0gyLA1L7KP8Y2TPKX31dIpPklIqe_KJkjDOovi13smwrjmGvzEl8-ZekibfYEw1-_IE0dq8zvXHi1NWDJMfmGL5adP4VBGtr_1hY16cUs-Nh0ibnwt1ZjTAFaawCcQHkMuJT0pSsdXx1uOhHc1VrJK_IdZKZ_aM11bmJWgpa2LqzlEcOQqoPK_e278J6XZzcBapUt_VmsgblD_oxdjOeFOYZtiMdenUKPQKPy-2rnIHofmSlh8RBCDxEf_kNOxlEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84673" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84672">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=T-kzIwTA0Gl8SIeFuCoPQ9WrX1Sc0wQTUaGCmB2U7s3JowxWKWpg6tBATKCGJilXyg41eR-vTo28kAm969pQ32FfWaA-E96Ty-pYvexGHC5oRJ_vQIYORNiBTCRRTLuqnJYAf2HzG8-7Bq4t0TjC6rjCpa5FfBs5fJiL_bJGJOwshw0v8OiOIVvL1pEssZM6QdzPLH0fBg6ofJW9Me4ym1iD0n4uvMXveAwa5PFRFFzIWk2VAO6-2xmNaDigSQstcHgq0xT1bfsSKtF_FKTQZuVREaCpRm941cvIuKJ86nLg_6Cz71ftFK1H_C4oHOa_3bg7kBb3ZDqaQqlsYYFKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=T-kzIwTA0Gl8SIeFuCoPQ9WrX1Sc0wQTUaGCmB2U7s3JowxWKWpg6tBATKCGJilXyg41eR-vTo28kAm969pQ32FfWaA-E96Ty-pYvexGHC5oRJ_vQIYORNiBTCRRTLuqnJYAf2HzG8-7Bq4t0TjC6rjCpa5FfBs5fJiL_bJGJOwshw0v8OiOIVvL1pEssZM6QdzPLH0fBg6ofJW9Me4ym1iD0n4uvMXveAwa5PFRFFzIWk2VAO6-2xmNaDigSQstcHgq0xT1bfsSKtF_FKTQZuVREaCpRm941cvIuKJ86nLg_6Cz71ftFK1H_C4oHOa_3bg7kBb3ZDqaQqlsYYFKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین عرفان جان میدونم ضرورتی نداره من الان این پستو بزارم، ولی تورو خدا برای یک بارم شده یچی بخون بشه گوش داد، من خیلی دوستت دارم ولی واقعا نمیشه گوشت داد، لطفا لطفا
🙏
🫀
🌱
🌹
✨
🌟
⭐️
🔥
🌈
☀️
🌨
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84672" target="_blank">📅 20:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84671">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ترامپ درباره اوکراین:
«پیشنهاد می‌کنم اوکراین رهبر جدیدی انتخاب کند که بتواند به توافق برسد.
-به دلایلی، زلنسکی هیچ‌وقت به توافق نمی‌رسد.»
بابا یکی جلوی این کصکشو بگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84671" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
