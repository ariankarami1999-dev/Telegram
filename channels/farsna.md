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
<img src="https://cdn4.telesco.pe/file/ZgSC30HvIyvhDsv_lxGrRByua-BXWfGCrtKuD57wpkjCE0prJdpLMEW1c740U9e4yjNvMQwhDoIYxp6cHznwaINshV1gXDJ01OEGlEKG-0ggBkSAaqZ_hPZ2lpFMp3yg1qOltv8DS-5EE3hRAL-6iDhTmnFD6-K3Gs2EB4RsDXdlqU_ZPw-fFUASlAlvTIzx305BLOyayU71Sz4qdxD39hr9maGzthtZzbq0wJptxmTFdAaL7P2-cn0c-99TKyAe3zEAr8lG2bwaJ14zgIQuuAY5N6WesAlYlygW_hEOJDihzc36WOTZNBJFLpjxa4cReyqtz0wZF2_1xvss9Tz6Bg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.86M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 12:43:35</div>
<hr>

<div class="tg-post" id="msg-467023">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duMBZ7FeftGuzHbKySavk9Ogl2DFTF212wcqm9HbJygWLES7wjO3-60KfEKOToPOwmTIQ3KdbICrc_Ms0oov1zPUHJaoiZBej5JQ9w1t7kmK45r5hRi85dP86QUIo14558hLN6oBVBLjWuPiU-88FGFvqfnM0stAoLPxtp9vDvoEJFE_ZFt0L8syQlJfdfF__dXRn7-cvhUQSdEcjUPdlCcdBm8_exg2jvyl2dmFdWfv7lBN-DMHKfwyvCTbkHrjgD99_JixwHCM3kJ-KZjxFnlkcthmYuIBo06KoGtFS0XSDGaJZo7tLoKCd_WyBUyE0nA2ykegA51sGLDgXBKVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4fiQZk6tSwvcEirSK3uZVG0BSP__4d7tpZZoIrIE-3Z-K03BiQIuEw3yyatF6XerRfeD1xeF9k0Ox6ZPJkNasIzaUB7EuY2rIZuGwC_fbAumMHdILK-1QXMCVUeFTyCvkKc7bukxWXW1xyoyCTOGYTh0Sn0EXoMwleXX43wwX5eQTjNM21iYaDE0ZkV7j5LuNCLF-WicoXKyYan7w1FUMun7NxrtfHtjapP4T1zXQOPWyMyQ_onlPd_fF_SVnUZ9HtZswy67LFH1h7nXEkF_wlk6yX2nzg-PNKSFjil03DNNBq-7l1VRC8FFF96hmVsFU2tTNDt9AkBi6KkcgAz_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رصد قایق «شبه‌نظامی» چین در ساحل تایوان
🔹
در حالی که تنش‌های غرب با چین بر سر تایوان ادامه دارد، رویترز از شناسایی یک قایق «شبه‌نظامی» چینی در سواحل اقیانوس آرامِ تایوان خبر داد.
🔹
به روایت این رسانه غربی، در ماه آگوست یک قایق شبه‌نظامی چینی به همراه دو شناور دیگر در سواحل تایوان مشاهده شد که این نخستین مورد ثبت‌شده از حضور چنین شناوری در این منطقه حساس است.
🔹
به روایت این رسانه، «مقامات تایوان معتقدند که چین با استفاده هم‌زمان از امکانات نظامی، شبه‌نظامی و غیرنظامی، در حال تمرین برای محاصره دریایی احتمالی است.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/farsna/467023" target="_blank">📅 12:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467018">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6oGFsEU8XPBGx8peg_T2VPR0mSfwelKzlZK3UVMsgJehdU4mOB75n0JwidUJkrFrutW9KOv-qF0-pTkdg7R1tbn-4lUa8qiokSQ4kz1CwxE0He3BaW1qR5kCWQwhYIZVFPHrWzqIQfYNeE0Z5-lX9Cr9CH5g5ePppWvx0_88atlESuO79yk6DSkX6Hn_kAc7mAKX5KzbnOm9n_rLAElKWqKEYt3zw7fTSkh7iBWseQMnEmRZGDusumUXsN0jj5rMEVxvd2Vpc50hr3IhLbNb8w7ppYIWG3pKa2050d2U2KSjh7GGGYKTWrxEhPrKLZyUI1cPpD3mi9hzxfjtGF2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtWyDGUQ57J00FCPyOc6xBja3U4KqDM3vSedLqazgE6PCDxghNmPm7t93M1r823pxZ4Uz2suob_kfN9ycChIpC2218k7pKLxLCPHbAfZAdLfgRkORlJA-e9NVkE9YJ7o4qcBPiSB6ajLC6jvNK3ocA8wt6BbirNwyrJclUAghPWO12zepAsj59I1XBaMWIvuiDiNm__IXXBXnYynSwUUAbS9gXoqUrAIagDkbVoU-dKhqExYGt2kTc4JnXmhRoaQdNGPXCJKCjaKv-brIxbz9tbJNUsTUtL2ai7MNIQCw4I2wEYjCq9G51EVxp4tio8WWZ6hhlKStQwgaNKiucbHCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmgr86B1Ge9F7EWnX9N0CkSbaPuJ-OTSYt2Q_AHYkOwHOg6tS7yMwdng3nNvuaScFAztldQd8sWJ_SZIodi6QrhEzl0dRLWi_TGrsbp1tPia-yaYvBTr6MCAYScSCvtitKDKo7jEAV_lzLmTKXjwILdGAKIQYp07f2HrEZut2-XDKa890Asn2rTuzzSDpSrwjvtCA09kA7mhJEHVCFCXg2XJjBQCeCr4jCoHWGZWrA3HqSsQSleMTZELYgWA-tSuAZah7E4EbtKlV5uhrkAWUuUQwkKZqrg8S7dptqZKtmna9Qzf5Fu0GcVr6YHdj8KnEq2jSFGNX7zJE3GamWpt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gpy8DmAVumJAJeDfRuBpJDY7NzYkZ5pO_haTcOS6P0QmT_-QWASPW19OK37nCP4qm7-DtjWqiv-Sbu4Hx0aJRSlen4a2Dvnf2ekXW_pcjBEbsBz4Q_CatfFzu6zBQ8IoQJDWs5e2tdJHH7_oi1UCHOveglfFvzmRb7tj_HSX10KmY874zajhd6jq43ycvjb4GqiGm7gJwe3OqlEwXYJTAb8C1rnstTnspI145NjrZNtoMA4xhLMGAiusf29cKIA5C85hGoCC1ZXb8ImAi5H_UV8M1yybGH1dbUgOxI4bcSxPok1PT_eZsUXXnd15SqFKIAJFRoy4dcSzODJ9DvuH7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYDjbo8j3Awlq6WoRriv7aJJDfsWkwLISEbA10i2Wy1GWbX7cyRc84ligfDd9x34MsZlebAIUGj0H7g1iY7pwkbNvgIGiHziT8sb5MwuwsSPZ6_PShYnFhIJL7V8LcnxhG9EdLdAfhXo0AqJOf231CYgKbqKBzVGgVq74MgxnOX642Q2gHFmthJT2KoTemoKpslauopfmuhJG97413AK_P5o6Wctf_NLNZifsbTpolJ4_WvwyjYZlWcUiwpsWNaKDp7WVilxtx1M6ojLBR_pFPGrmko25M-BXSUnt7_OeQXgly3pn2vaekcfFPPPyjhF2frFpjJK2JBC3ECkQ7T8bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور پزشکیان در جمع فرماندهان نیروی انتظامی کشور
@Farsna</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/farsna/467018" target="_blank">📅 12:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467016">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3dbd405f.mp4?token=TUrs0G6RpR3_IqHzH0lra9Q2uzAabOYOr01btyjilmiw5ziMHdUDQO_cB8QK2zlXIpHM_mho8gNl9V5hHsa3Px40ijCcP-rU2Ss2p6FQLY0PJxyex7xcKfWcyrD3yVGQn6q_BuEvEcfwaLLa1XGcNLytv0yqYrcoDY4O72vQdwH3jDfVUd3zBQpnipTgvoW4tfsMGKhJRL1sFfvvdGJoafBfUu7MskEDavxjz9hcL789OqwGrpF6blQYramSSgGC513GpL_k1jZQg-1uHBXanyk5hRWavHrP6XlxGr_N0vqGIlOTixs25VIjJfUC1pQHNNOk6OgSrix4QCN7iCpgWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3dbd405f.mp4?token=TUrs0G6RpR3_IqHzH0lra9Q2uzAabOYOr01btyjilmiw5ziMHdUDQO_cB8QK2zlXIpHM_mho8gNl9V5hHsa3Px40ijCcP-rU2Ss2p6FQLY0PJxyex7xcKfWcyrD3yVGQn6q_BuEvEcfwaLLa1XGcNLytv0yqYrcoDY4O72vQdwH3jDfVUd3zBQpnipTgvoW4tfsMGKhJRL1sFfvvdGJoafBfUu7MskEDavxjz9hcL789OqwGrpF6blQYramSSgGC513GpL_k1jZQg-1uHBXanyk5hRWavHrP6XlxGr_N0vqGIlOTixs25VIjJfUC1pQHNNOk6OgSrix4QCN7iCpgWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از خسارات جدید به آرامکوی عربستان
🔹
تصاویر ماهواره‌ای نشان می‌دهد که به بخشی از تأسیسات آسیب‌دیدهٔ آرامکو در جنوب ریاض خسارات جدیدی وارد شده است.
🔹
به‌گزارش پایگاه تحلیل تصاویر ماهواره‌ای «سور اطلس»، یک مخزن ذخیرهٔ سوخت منهدم شده و لکه‌ای تیره در سمت راست آن نیز مشاهده می‌شود که می‌تواند نشانه نشت نفت باشد.
@Farsna</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/farsna/467016" target="_blank">📅 12:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467015">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pepnm0g27_J6LBu_luubIcstbQAr8EXOhUTs69JQmC86H6G4QLNmHp4nL53Im2pK6tV056kmOLtovf0WPDu8t0yU-vg9uvjfWIdasyKeXQ2zF7pzrYL5guzPzNbVxNAfCN8LASj5ktoYMdmgaxubqaSYTXtXZqDVtYtywkBr7QMkDG3rng4li8aOquDGBW3yFBpqcNeB_Sw6YYInbuyfE8K9grxwk3rz7SmX_Z8muxRZnnCIRklVLyadl_A_APJklYm4gspwlbHGVLzWDXD1orJwhDNBWqu34Gy6Z1H1ltH4MLOSej50oMs6QbYwywf9uGbrkso-ZfRZKrwPysUBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان از آیت‌الله نوری همدانی عیادت کرد
@Farsna</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/467015" target="_blank">📅 12:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467014">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-text">🎥
ببینید
👇
👇
روایت مجمع تاپیکو؛ گزارش عملکرد سال  ۱۴۰۴
🔸
تاپیکو در سال گذشته به‌رغم دو جنگ و یک ناآرامی عملکرد درخشانی از خود به‌جا گذاشت.
🔸
اینک تاپیکو ۱۰ درصد صنعت پالایش کشور و ۱۰ درصد صنعت پتروشیمی کشور را در اختیار دارد و جزو ۸ شرکت برتر بازار سرمایه ایران است.
🔶
روح‌الله شهیدی پور مدیرعامل در بخش اول به دستاوردهای تاپیکو در سال ۱۴۰۴ اشاره‌ می‌کند.
@tappico1381</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/farsna/467014" target="_blank">📅 12:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467013">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7i4DMadLdva8MjxGutmb5xYhQYlXdbdcXiYut_0xyhfXr85nxpvK9sJWdJADogiEnYR1-rZ6Lnf0uFmLcFOuLZZVF3oIEgSziPzbrV6iWCPUy-rNG3FnUrXhPlIPpW93hWwtLyxbfPNpU0i5mcMZaB4YmoL87xj1hD2W28d_LWp36gAbvnJXyPmSdGDTubJ7_1kv_wPqx0SKosBbn1rLXGZQ7xVAb-Gd3pTxe_G455bOUXIARs4SCm4MNOUaVUvN-fbFec40nbpbYuZm7NhFmkckb0BJX-HDo08_A1N2RMazjiUTYFD8ruhHQPC-gCLpivxlCbInglYfWdOqsVuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/467013" target="_blank">📅 12:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467012">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/467012" target="_blank">📅 12:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467011">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حملهٔ مسلحانه به مینی‌بوس حامل کارکنان نزاجا در زاهدان
🔹
روابط‌عمومی لشکر ۸۸ زرهی نزاجا: ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، مورد حملهٔ مسلحانه قرار گرفت.
🔹
در این درگیری یک نفر به‌نام محمدرضا اوکاتی به‌شهادت رسید و ۳ نفر مجروح شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/farsna/467011" target="_blank">📅 12:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467010">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLEx04oe4a0pKCSDqFoYGVtqSxnC6isDgBLq3nHQN9Vxb7CNkGSZZc1RaIOknznuy7MYLrY5acLaAd64x1c29_3ihPSyGKUUO8vfNi7CVTZDNc1EA5z0lTI333gYVZGvYbYSGXbwNaKeVhubHSL1eEqh5COHdJT7cN_WP6Y4Z14qgaw13fPNC3wqCMvzB_0EXuJ9YZJJ9UNyqxZWDz4d30jiIWowxJyEO6r5YvvV8rCTSq5p8lehlXgdDyScrpEsQWz5KSjewxG_Ffxy3-waxNYn2V5W3vS-nV_uJ8YyE2mq_CnaVbnvjkhi4Te4IzVWvSXLXkG3DAoJV6nOJef0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیاتی از پرونده محسن بابائیان؛ کسی که با خودرو حافظان امنیت را زیر گرفت
🔹
رسانه‌های ضدانقلاب مدعی شدند «محسن بابائیان» صرفاً به دلیل حضور در اعتراضات دی‌ماه ۱۴۰۴ به اعدام محکوم شده است؛ روایتی که تنها بخشی از ماجرا را برجسته می‌کند.
🔹
پیگیری‌های فارس نشان می‌دهد موضوع پرونده صرفاً حضور در تجمعات نبوده و بر اساس اطلاعات یک منبع آگاه، بابائیان به اقدام خشونت‌آمیز با خودروی پراید علیه مردم و نیروهای حافظ امنیت متهم شده است.
🔹
این منبع آگاه همچنین گفته است که وی در جریان رسیدگی قضایی، به ارتکاب این اقدام اعتراف کرده است.
🔹
تقلیل یک پرونده امنیتی و قضایی به «مجازات اعتراض» بدون اشاره به اتهامات مطرح‌شده، تصویری ناقص از پرونده ارائه می‌کند و برای قضاوت درباره حکم صادرشده باید مجموعه اتهامات و مستندات پرونده را مورد توجه قرار داد.
🔗
متن کامل گزارش را
اینجا
بخوانید
@Farspolitics</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/467010" target="_blank">📅 12:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467009">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f385332896.mp4?token=ZB1puJQnFOXJBOF3xmbzluxydEb8ErMqlpp9Z7PGS6MyoXMQQ3rWahAf7ekxtDUxttNYxSEPxrS_ExUrzK2koPIojWjNdm1EBn04lgzM5NXiXToOagbxRtl-G4R0u-EN8bXgeZVUi3-MDCZ6cBmuVtz8jpWrgRk-DUSwunb_z66K9VlzliUCvQ8yS677enHNdycOIxJn1S9j6H-y03ieJzpU6SakDtRsRvKZ22tky4N0nu1ph-d2mu3Eh9EmLCVUPWBlWTOfYKpc5c_k8F3nml4UIRpyy0ftL6AL-Y7yJidVEKvlsWFvREagmBaVBn36AZx0pde5DbkZvHa4jc6P2WVEaqV64sKK3hsvKZfn6Id93g0Uve6ht5DEdK8pkvnK0YsVe0Tg2GaPf500fXL4g3aHxyMMd6Dcr4CLz9gbPg0nMVNkhy993RFLaJU95m4vRNePZuPlXwrluhQhuCKF6LeIw3Kp0fCHCdcVCH9SAB-QAMOL783fVsguwp_uBa2XHJ-f8X-uz_L4oxBXsyyiuKn7t3KgHzZchnmuH5FkBhdIdGi3ZiUno_2dxgcjt3_MvYBtft5uvM_4vDADcMBT3JunsLOMk2DtvV1mkJWOq7TSPwCgNiwinxjs0cWE-8g_ubHZXH6akacWtPn5IXFpG78HTrD3-XrZFq6iCLbuqe8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f385332896.mp4?token=ZB1puJQnFOXJBOF3xmbzluxydEb8ErMqlpp9Z7PGS6MyoXMQQ3rWahAf7ekxtDUxttNYxSEPxrS_ExUrzK2koPIojWjNdm1EBn04lgzM5NXiXToOagbxRtl-G4R0u-EN8bXgeZVUi3-MDCZ6cBmuVtz8jpWrgRk-DUSwunb_z66K9VlzliUCvQ8yS677enHNdycOIxJn1S9j6H-y03ieJzpU6SakDtRsRvKZ22tky4N0nu1ph-d2mu3Eh9EmLCVUPWBlWTOfYKpc5c_k8F3nml4UIRpyy0ftL6AL-Y7yJidVEKvlsWFvREagmBaVBn36AZx0pde5DbkZvHa4jc6P2WVEaqV64sKK3hsvKZfn6Id93g0Uve6ht5DEdK8pkvnK0YsVe0Tg2GaPf500fXL4g3aHxyMMd6Dcr4CLz9gbPg0nMVNkhy993RFLaJU95m4vRNePZuPlXwrluhQhuCKF6LeIw3Kp0fCHCdcVCH9SAB-QAMOL783fVsguwp_uBa2XHJ-f8X-uz_L4oxBXsyyiuKn7t3KgHzZchnmuH5FkBhdIdGi3ZiUno_2dxgcjt3_MvYBtft5uvM_4vDADcMBT3JunsLOMk2DtvV1mkJWOq7TSPwCgNiwinxjs0cWE-8g_ubHZXH6akacWtPn5IXFpG78HTrD3-XrZFq6iCLbuqe8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش حامیان فلسطین در قلب توکیو علیه اسرائیل
🔹
در سالروز طوفان‌الاقصی، صدها نفر از حامیان فلسطین در توکیوی ژاپن تظاهرات برپا کردند و خواهان پایان اشغالگری رژیم صهیونیستی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/467009" target="_blank">📅 11:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467008">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حملهٔ تروریستی به خودروی پلیس در نصرت‌آباد زاهدان
🔹
ساعتی پیش یک خودروی پلیس در منطقهٔ نصرت‌آباد زاهدان هدف حملهٔ تروریستی قرار گرفت.
🔹
در جریان این حمله چند فرد مسلح به‌سمت خودروی پلیس تیراندازی کردند.
📝
اخبار تکمیلی متعاقبا اعلام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/467008" target="_blank">📅 11:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466998">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HksqV50FhxOa8WmAz_MQiEZksDe20KP_dPjeRB7aXMG-cnTDWHwx-6kYWzmF6rlpzH_Hbbd9p2TGMNjdG7Ym7NZml4rXtHUkif-1OFOUlPBPDj3XFn1eAJzjS2CGWYo39HOnWytuIw2YKmzWJ0kUl1hVW5hj2gWMbBpPNfUgRijeYksxcaXlcCnxGa4s2SawVooSX2yRZtkfvowzPOVTITUvx-dwIdDdG2ciNMgSIUMEvZb-g-TawZVBMWmiAlOKtnxx3fAqxaib5FrnM5QJp5ZoS-2igGQZrMkZLGSzzpWCRTkZTXJ0U5f29iL9jg-srYN6NhYfdWjnGZhO_2saGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEU70HpWH45yR278C2FtMO9d2jPEF0xY_MEkxvZvaJttHqNgyYB1rmXMPfryxKKG9D1zqTo1qryCfXqikuq1cwG0NXGRZosKbqRrDKqkYHoELbdZFB2Kyx5_Kp6uZwJe15MVejHlxXFYz8eLLVvkWyH3MzOxcG_mee30ZBfOrksgVSyaodxTKLqidHVKBsdzjxydh5BiHkymS7v1lSgS6PcgM_RmCuZLxQCTR2tgWSgKTCXJo6XumxkIpFsBgkmyo4aXZWrKdpPlqAhSFu1a6pDWrIeOJ_2LaHxp4LI2cax9gulrsyWbp1nUtxwopNMeli3W_0kbP-Q2QEUIzPSn7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MN3g3JtP_wmfdBSP7o-eQjb8PTSYZBqEB0Jj7rYNiqpDQSb9WOxWXpoSQ7FIcGTYmjRpoyGeR7SfY4UI0XLA1H_eXaF-wFCId3UKV6UtNGtWa92GOoNimWKj6RzWn2KN1aRWj55OQ7ERqjmXUVA7Bep7e0DIZRWEDcjVxtEoqwntn9Oak9-epNFaOabqavzEHoTIeBKaQMLTysF2bxCzCGMBUI1G_GPh405SaFh6agYyVyLAh-GeV4zAWFDleTXR5DyNsTadtZAhyBnRybaLcZ7W97aWhkiazD86m4CA3T05-Zi0-7qlMVg3f6Ahjook3nUYzskIXQOx8-AHe9LV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOU5hKtU7KCAdnwJRnYHT9KPnvqnK1snOzc3CgACFPZZgPGo6yUctW1iNGLQK_630ruS_bj3EM2ZIKC9AfH6Musovw2TrB9NnOr2joM7SMdQOc14S56Xt3uELVw_0gz_ai7Cx4WYSV4xIqrqMGk0e4ZKXHcTh6EJmLwj_D6UwPZTPZ7HJaj-RZg66fy_wCc0Wny6x5ITeYyJRux9m9KxN_AYkEskRm2w2piLJSPvdS62pXDMPiK1I07zey40zF9tBqi3tYkIvMgqDK5kl1KCWtDv6ziYY6gnZr7ZryXdse-7-pBDgSTcgb7BidsZx1XGNXJupGn1nOLulbbveIsD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ua0-UYs8jfqyAnExrDRb0WGojzB40hhV4kseSGltSUZScIRbvt6L3XefwRCwiqdSPe8njtmS3EE5MAwTLHK15v-C5N_jG6UjVvwicRvgMEZOtbULzRVZr6sp_ZXeEp6dIuV3_geNKV_MZGrPYb7hmFsFHqwWGF0Ev1i57Hs_ucrYs2BO4YzQtIp2naOFtbfmAZ5w0_EmC-PVMGhkJARt-yBSI-GDWNly6HzvGTGphmgVj07R-rRMA0sFTyobnogtThqB1XAdVgIxWiuxBRj_r3o0hrIawkTg347lnUVpXit_xOADE16isNYaMQzcEfL8uscmWDLjtfGJa-kAuTCD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUEiQ_xwe_8OgdpN144q6vCeq0AjSU9tzszUEBOZQZ3LvULyfVi9wUlDIr3BTyVleUrOVk0xJa6iK_vGMaH06vBz9egY4O30cfiy7xjjTgRvQ9-IJybHQH-60aVXQo71dJTqBmXLebpTzG3bFA708-dS9N010l4cMcMKMa1PZondzbaLNBLYmiu43Lr-m1_iAu42gqeOYvnfGc0asWRErJ9ZKaL1wyg-MScJzJfecdGprVJY2MOrqU1xaxKR2vHl4wDKLd0nNLgixbfC6Qux8h_6slcOMeFCUO_jkrKb1JcgrTTtmMwN8ASZbPzJfwcDogeww9j8ZvpvfkAqDzF0XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSSl3DFAniOjAP4wyt7n3M7AltutbDYeCfytlHJowpcrYiVPKbJgu_I-EaFpG0_XSReCKf5RkotP8bluajQbFX6p6M6SHvN3xV-uAzSR_aUj0XQUk5rASFqvYijlI7flkN1AVPjASxjyJaRajKmn-miNrj1QE1RlD9I4Yseo0TLwo-0E81bercBpSS0LF9RFjthdlyUq0SEdjiS4tVgHFKdyTXk6dlKt5Jou-JcqyEcJvuUQ0ariEtN7DFHXCtpGBhIaM0oqdNSMSTZnH2dKv1emwgMRHW9_pMFTp9Ylz19aqnyPEVpJr0XA21AkalHrIbrdCrRZegyy43-pcTI7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJuYGIul0L0UUsEAHfMTNDFjXKP4mX4FWnrsCvaU07WYF_OAvlbSQDVRyiqXh80G7n-nyHJR5CYExsuPTGXfVtd9uDDM-fjP5UMGZk6sH03uYq568voDz7mz_z-NWPmWAusSK0K4GCyP3bZ2NUU5VOjsVsDy2LUa0IR62eANLFG5V4KJYonbQrvgTLjJ1I432i67XcQxgiCcgku4vbG2qHALRWEy-PaMJJXSKpwr68I3oQCRYVPTpZ3bAaZ56lHBz7P8mITfPrkxX3TOBXVh9aZb7DX0EdVdeWozag7ibjf0XMt9cjifCAL-gWgL5Qn5j4vu3VXshBk9rgsdExNSdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TM9KNLyYO3vR6i-NrN0pPHQ71AFQ2H9PnxkiMM_g71aNThjr2sZ3PiZqoIg82ClkY-z-XAzlwG0_jVwCtX6hd6HAopgAF_FcOrvBLH7vpxA4TX6UaqO0cprzv8hiC2OAdDfQIy7YR5XlrrUyAGy8Sn-BEIskOwWWvyzfMgnLr2vfnPASIICJK_LwG1D4kE0m7P40o279Hu_wOIBaeJXlPqB5qNxrS6x92ZLilZudMmpx29_AAXJeZafF6rZMwQItHWpdXjcFn2Qq7iCVRPIoJGoW4xoEYjCua1ldGnbCD8E2A0EV3P70FBwXVA89eOLiQ2ljM541_Wz8l1PL_BVylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLhv9BJiSppHfM3_Zb1mMB8BeKKd0Gjhuy4P_cIRIKMPs_sC4ynxtoTii47SSFVErQ1146e3bm-BSdzXRJRyh_wAVe02NP_tAphFD6OX4ukiaTdJqtuzJ3IgpEsLoH0siQgA28sk-XRj5_0p99B2VJRVwKItOnTuWJ132o4pHUgxyoMAXWdCDP1Os-pKcUNP64gj1GjbuFMWwBCbUHc3iY-hwpQUOaixySjHEZBD4Jk5qU91fEl7K7Y20TKLPH723aIxBqnjmSB6AeVj9p535UbvFKzfxhWA-uGdkVKnpOg4v7E3piZBkJ9vHjOEvR-alG57bkDVdiCq7w4i2Hb2aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خط
‌
ونشان جان‌فدایان چهارمحال‌وبختیاری برای آمریکا
🔹
رزمایش ۳۰ هزار نفری جان‌فدایان در چهارمحال‌وبختیاری برگزار شد.
عکس:
رضا کمالی‌دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/466998" target="_blank">📅 11:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466997">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bABdjIxU3eYYTyAzpxGVgWsEpj-jy5EsjjjYQ9TzbhkDyx_-XWsJPEg79j8sZWvQdrm37md52pmWhZdHdv111Og-f0RVxDEOYgiTzTZeeWyP6AIUieCt_OHjOYHoDLHKqVlhlsW8ZlwWNaa4abHlZmp1fSUWU147tFckaIvmd456FAP1jmA3tyRqE0nLt1CKNDXyTZdwofxmDHtalHSCVny-ic4jsd-p6frV8YRdof6qRusaPfomU9yY1d-6Pb63IuNMkAMP6t54NLPQc7nZWE4ictiNpDQc9-2LrPh75z4jjPbqiMxVnGx0kJQ9qCZLDYsMpluEerElRbjqrT6ZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمدهٔ اشکالات آیین‌نامه جذب هیئت علمی اصلاح شد
🔹
رئیس سازمان بسیج اساتید: عمدهٔ اشکالات آیین‌نامهٔ استخدامی اعضای هیئت علمی جدید با ابلاغ اصلاحیه برطرف شد.
🔹
برخی نکات همچنان نیازمند بررسی است که از جملهٔ آنها می‌توان به کمرنگ‌شدن نقش هیئت‌های اجرایی جذب، به‌ویژه در فرآیند تبدیل وضعیت اعضای هیئت علمی، اشاره کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/466997" target="_blank">📅 11:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466996">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b64EuSiec5Hovc4x3TrhN1HuwmDieqYaS6TO3yFIYbl8x_uo9zvzUhLEpXEHUV5APjbUFjWPkRtTO-6RaG2vm6YjvAUEDDfXEuXa2ndjER1RXdDNMxAq_TNIJR7fBQK24x4HPq6qekykpJjY__zzStgP5q80r-zQjCnSwS-LD5TNZXhVB6GdHOJYwqCi1OmKSZi2FBMyxRxcU1fnenGsFCJbgslE3XBF_uDLvv9EnrYs5XGi26VmnllXduZXdj3rOSW6ZOjCp6ilsE4oVbgnEbsdK9sJLOC4hIrynmSjRI1zNVpc1ZRz_d_tlo9dMKR-QKWCK3pHTV7Tg3w2YO3bjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور از هرمز به پایین‌ترین حد ۲ ماه رسید
🔹
داده‌های حمل‌ونقل نشان می‌دهد شمار کشتی‌های عبوری از تنگهٔ هرمز به پایین‌ترین سطح خود در بیش‌از ۲ ماه گذشته کاهش یافته است.
🔹
این اتفاق پس‌از آن رخ داد که حملات به نفتکش‌های عبوری از این آبراه حیاتی، هفتهٔ گذشته به بالاترین سطح خود از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران رسید.
🔹
براساس داده‌های منتشرشده از سوی شرکت کپلر، تنها ۷ کشتی باری روز سه‌شنبه از این تنگه عبور کردند که کمترین شمار از ۲۳ ژوئیه (اول مرداد) تاکنون است.
🔸
گفتنی است قیمت برنت در‌حال‌حاضر به ۱۰۴ دلار در هر بشکه رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/466996" target="_blank">📅 11:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466995">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات عمل‌نکرده در سیریک
🔹
فرمانداری سیریک: به‌دلیل انهدام مهمات عمل‌نکرده در روستای سرخور طاهرویی تا ساعت ۱۲ امروز، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/466995" target="_blank">📅 11:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6NxsqSx87V-b7HUjxTBtf0_bfQlHH4ZLbGkqXadxEOq8JEfMVuBbD3NvojbtLl0XdWyuS_2SkulX821cbsCQh0TTo7K_cerFjYBCyYoyoDRkAwgOsV6NM8LKMjXU7XgeCa21pBvrUOqPp6P0neYJHXKW26PVpzyQvvcUtI6gc45kcfPN_f3rNb_0eh39m__E7Hsa8gA_-Z9TJ5lt1yK9GQskYiT0QOJRSigwqyddTbH5GwQCTWbLDqZXYH2YGBzUqznj8l4AmDEC5rnciWprNwCmjAwDjTDsQ3ug8fywoBWIwbrw7a-5IYNZkROqvx6byz1u1Hhd6VRKbpDNOCoMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgqXCWROStlVwfP-1G3DD2v8-LxZb8dB4165UX7Nsj6E6W-HoY_gTOK7KGfxgQakoOXy0UPQm6bKxm2h38gAUtLdjvsJZF_XJ73NYuf71V2Yg1UBBwUrFDzrmv6Gik3o87KxFqg96TxipDjLqZMqRPUHclpcq5JIz5JuSJBTT3i4I87LnBR90b74bfTc6Z2T-FtWpJrT_ekirWmbn7si9drb0fz_BjMXfvpYSKdcaqIxxBM0kp2BgeeVo-56jNBm7lFvEqdP9x-mPD98nX3430OzfEgSlrPzmla9DZmOYz_ZI9Aym7G_vWhqNbMbs0_-R06mRv4qO57ByfNbL0B2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PB0_-HmqjnauxD_zRTLn7mtTOhKEmK5udr0Nlw3F9UrY-tue5TiJ6qGOSN-lu-ccqckbfnGBx5TdUsUsZ4lC0kK5zSPTQxRHL5zha3-sAeDsJlqN8rXH3ctp01fBBMUf39yGIPZouef7-qeamcUQTQQA_2oEm7gLUB9DFwwzDnB30Co6gcJVxaxaWJw0qjzzJcJ-MvEXiE_VClCt2RsPCsg8V-f2YbrIH-1vTXbNGZf2ubvrlnOeYAM35FW3qjX9QwN3bRUl2K-9P_lqf7pyxMPW3b1MuO8l39pEHrOlCZAMLWdx15sR9zfQ7oOJ2TgHiIZIxfmwE0G0iHwc_GMTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0YSck7kHqYVrwOJHwyaTpGnx6z73w8m_2LB_cHhNIem-sKlr6gnggbD3CYBBoSB41-ujnb6zK2eX8a5zd4WxytSZP6yCdxHAnbt2NlLtDDgDwReQuDoThTFqayrEsf_Erg8Rt9fbO9SnYxAIQbuZyQrrD7k9W2u7ENAi6MChd99rcZZGMNgzA5xH4v-LFmR3R6fqzTX4dVz3w-1vzSlfq9Wdhg9oRZgW21vMTwJTtXZaLEvTX4V76z_DrKkhwUTsK34F-lShCYTeDike6VuIGkBMlbiF7l57TWRFVQHe4JAPNiXZxWlML_N-KFQdy66JQYbtvW-aVf03-MRDmWgyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sz-ffJRlW7PGIh4N05YFHnbOrKbU6NF_nlCFackcDs1rPT-FCUDOGVxtzbdj4dHrLSgjxBkG_gt0gPbQgMvlIf_945eCA5n9ehOi4kybaI3Cq2yxAWrBPU3VnOJQRvgHRMU0CdJzgHVcFXlTHDUpvzgy5ujli8_XTwPXoB5_VCtZD_CYa8_u1VbY59QaK4kZMDP-g3L2XlKjlewfhJ1ZRhVYo31k1lmo0pF7mcg_REVom5xMtEjcwX618X9pBnqZZHjanxY0C-vb1hIDJz4zVdOoJmUGNZS3RqmFo9SaEAZ7xIbFB_20ms9mcRl7i4bqgE4ruLxQwdB6M3dtFUpXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ez9QiCmrwMYCo-j0WE9ZZOQJsszmKNuxkhxQo1ZZEs36oI9dNnjT2Fe6uzWOLDezmswPELq4LfzEJTKo-KPbp5IXJlAeLts6mgpgv_Iyx_BcLyJm2qYD951tJ6ul8zdq-6nLOOzMiv43wU2EQ8le1RCaKkUM4VX_xzSIORWhwKs5q7he38YPDP2ssqcN53bpK0OevPSSungsxsIpg6fqA0aVX60MwrK-IwCq4rEOtpUsgENF61HRpNqSm40cIgvRbASAoiR4gj1giJJnccZaYr5kW8KNU_92bkiw1_sluFjF3yW05RazaoRh10wiKL1RK5u_8fqZXdDYcaiUyg0vMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ks2MZaDoOjrOgzVmzvbm2UhxeQwIXnsT2jvhJztx4A4as0C6zunGzZiWfCLFC2wNEC4DfkfGHacqI_acxWRUT5Gx6zUXXmrwk4G0pt_QEkTnTgNVnejp_riaQcGC-OG2RpsoTtmNpoqUYuFRXV92TCYX4Z6bVAefTcXn9atDqBw6STj-y8mXbgu6Ibs1Rk7lLIlksiEO1xE6Jrb3la1wBpNSZ7APXHZOLigJojuJGd2bcGQzXjiwiwzB2lvWVKZYLaJ4nr1MdiE7gGq0gYAuU0yAKXCGslbflMRIt8uWvixej_KLDAcGoA5qMpZwkOK2AEZ_2nDGFDr4jRdkw-aFpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرواز بادبادک‌ها در آسمان خلیج فارس
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/466988" target="_blank">📅 11:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS76ksDWC-_mivSvtQrB2uX_YhkZB6bXUOtPPNDEi7WjdnaJUTb5aKZJUQ7Ff-Fap6QrV5subVeIsfIQli6r0MykgzlfLkGptnp4fu3CYIVGO-WQ8ZPdIzGse-T8IyeVYUygipBmBKKBZAGWhLBSXzbn8h1S_nek4_J4_-UkxPp39pGAH5bovRDD2cix8CnuZsbufFrDm7SdiycR7AZUezplthxd_ipMPWYPNgaaGloKQxH7qBdv0lrANIW_PfK9xkswVeDAkanSq22crtsY3zkcW3QNH8tWYiP0-0w5rmBET3f_vUkWI7OxXQatlx4ZSubCznVC8a6tOqpjgP_3CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احضار ۲ عضو هیئت‌رئیسهٔ فدراسیون فوتبال به کمیتهٔ اخلاق
🔹
علی خطیر و حجت کریمی، ۲ عضو هیئت‌رئیسه فدراسیون فوتبال، که دوشنبهٔ این هفته در یک برنامهٔ تلویزیونی اظهارات غیرمسئولانه‌ای داشتند به کمیتهٔ اخلاق احضار شده‌اند.
🔹
این ۲ مسئول دوشنبه علیه یکدیگر اتهام‌زنی و حتی محتویات جلسات خصوصی فدراسیون را هم عنوان کرده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/466987" target="_blank">📅 10:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466986">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چند انفجار در پایتخت عربستان و توقف پروازهای فرودگاه ریاض خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/466986" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqtja2YPOkxt3Evr4pbpgCeSN6MnkBlwXcaeVNaZrmX6qqoCLHIBZ2RTC6mhVLptw7aG4Xei2RLRWnU6aDu-iyOXIukrqCTINBwhlpzISMl5wRnwfmva_MgESu5q2mUr1hVuDVT6ZfUE5v9pQ1nCwvf3qj6XE-ijeZ4p2HnTrUDodvX6asaLd8jmoNxP0sPbYTUJjIUdyfU3dLDaJlJUnk2loc2k8D3y5Fd8paKToQsUtC1vSyUbKm2AiMokXh5CiPv1ORaJm3fKtAyz8c8GyxpzDPYkh65iAJgz8SXANi_u5GJEJ8_gx2OfQvDYCFASFq5uWyGk79sIUHpG3lHleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست مقامات عالی‌رتبهٔ کشورهای ساحلی خزر در ترکمنستان با حضور ایران
🔹
گروه کاری مقامات عالی‌رتبه کشورهای ساحلی دریای خزر، با حضور نمایندگان ویژهٔ این کشورها در امور خزر از جمله معاون وزیر خارجهٔ ایران در شهر آوازهٔ ترکمنستان برگزار شد.
🔹
در این نشست، آخرین تحولات و ابعاد مختلف پدیدهٔ کاهش سطح آب دریای خزر و پیامدهای آن مورد بررسی قرار گرفت و بر ضرورت تقویت همکاری‌های ۵ جانبه برای شناسایی دلایل این معضل و مقابله با آثار و تبعات آن تأکید شد.
🔹
یکی از مهم‌ترین موضوعات مورد بررسی در این نشست، پیشنهاد تشکیل کمیسیون کشورهای ساحلی خزر برای بررسی مسائل مرتبط با کاهش سطح آب دریای خزر بود که با حضور مقامات عالی‌رتبهٔ کشورهای ساحلی تشکیل خواهد شد و بررسی مستمر ابعاد و پیامدهای کاهش سطح آب خزر و مقابله با آن را در دستورکار خود قرار خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/466985" target="_blank">📅 10:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حملهٔ تروریستی به خودروی پلیس در نصرت‌آباد زاهدان
🔹
ساعتی پیش یک خودروی پلیس در منطقهٔ نصرت‌آباد زاهدان هدف حملهٔ تروریستی قرار گرفت.
🔹
در جریان این حمله چند فرد مسلح به‌سمت خودروی پلیس تیراندازی کردند.
📝
اخبار تکمیلی متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/466984" target="_blank">📅 10:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDAQvJiGmsY7CvipZyGndfLx9_qP9KykHzHaXFWTdExLzbf1DkElJJ4NWJVWXtXaP4OAzhy7zK7_zzDOoLYky1v4bTiruFt5foL-JK06SC3dvrdrCTeYtLAZbNZWdPD2kHLf-WVJ9RQ1JqJTJ6Jir2Y5FPkRLYTmVZx1Q_CGhVFTGiQs3DOOA7hV8JcytJ2Cb1JKx5odle-DtlX98fM7AsDZGR9KUxy9qxjI7V5B0WdekrX7nsfInDyr_o4jO_axZzveCxJRfLKdTs31PQ6LG70B_K7aFvR4fTbOQtLZen8hluWyCTU64gw_JguFINNoj5QN_MGEAUN4tRXzAxRkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمشق: در کنار عربستانیم اما نیرو نمی‌فرستیم
🔹
پس از آنکه اکسیوس، طرح ریاض و دمشق برای اعزام هزاران نظامی سوری به یمن را فاش کرد، مشاور رسانه‌ای ابومحمد الجولانی با رد این ادعا گفت که سوریه در کنار عربستان می‌ایستد، اما خبر اعزام نیروهای سوری به یمن صحت ندارد.
🔹
«احمد موفق زیدان» طی پستی در «ایکس» (توییتر سابق) نوشت: «امنیت پادشاهی عربستان سعودی و منطقه خلیج [فارس] از امنیت سوریه جدا نیست. ما در دمشق در کنار برادران خود در سرزمین حرمین شریفین، محکم و قاطعانه ایستاده‌ایم؛ با این حال، ادعاهای مطرح‌شده توسط برخی رسانه‌ها درباره درخواست پادشاهی برای اعزام نیروهای سوری به عربستان سعودی یا یمن، نادرست و بی‌اساس است. خداوند پادشاهی را از شر بدخواهان حفظ کند».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/466983" target="_blank">📅 10:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fk0zzKuM4__eaQvMpP34UtjUFaG9MtR4fha5aS8EfouYBDeFrIPTWkJ-pDxJWX0nvw20acxoo3ldRjgKCcH1wAAkyipBnnvd6VTdZrc05cO3FoAjLOxcCDBOvCz8kCojMNC7PkXj6cgi8_mewvu7m_74NRvsuTs9gBchKBJxrbN3c__vshrxY-WXoaFyj2hM0kOwB9WtNQEoZVK7D90gWWWAJOpU0LiMQ6DkTDc1jjk-V6eCqLgoNBeT-TMIb4E-nq9Pd8ownLq5dmLkkYxfnmTZkPi00AfvvjN-Y253xk4vzOXTcUAe4PwdIO2ITHu3vjpbi9tPTdntyQ0dcF7Q4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ام‌دی‌ها به آسمان ایران برمی‌گردند
🔹
سازمان هواپیمایی کشوری با بررسی شرایط فنی، مجوز ادامه پرواز هواپیماهای خانواده MD را با رعایت الزامات و دستورالعمل‌های صلاحیت پروازی صادر کرد.
🔹
براساس نامهٔ مدیرکل دفتر صلاحیت پرواز، موتورهای JT8D-200 که تا ۳۱ شهریور از مراکز تعمیراتی داخلی ترخیص شده‌اند، در صورت رعایت الزامات فنی می‌توانند به فعالیت خود ادامه دهند.
🔸
این تصمیم در شرایطی گرفته شده که ممنوعیت پرواز برخی هواپیماهای MD باعث کاهش ظرفیت پروازی و نگرانی درباره افزایش قیمت بلیت و فشار مالی بر ایرلاین‌ها شده بود.
🔸
با این حال، سازمان هواپیمایی پیشنهاد کرده تا زمان تعیین تکلیف امریه صلاحیت پروازی سال ۲۰۲۱، ورود هواپیماهای MD-80 جدید به کشور همچنان ممنوع باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/466982" target="_blank">📅 10:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZiAzA6XdaDrQojhjK9vxhsgAbrDiIV2Pb42njtw817lEeTXnNtKYC5qkZ_MrXR_CDZ2i207qScYx3JQI9Kr95b2ntnjLIU5T8TmOJFxaElVakGPz4xlyE_ODffpQp3lBlDjFaOTbUkTHEzTyH4N1ZhrhuOOaVOfHqLZgKYbIxpB0zyc4cJPmPveqGBFzMQNJBRlQNqlw6DQSCfAzEcYcM1azGDhbqP6bxb9jzCCgKB83i1CD0kf4I9HIeo8jiqzZFte_wDvxLkYWZIBDmpSiCxKtXadJ34WlIV_PmfLa-wuQCZJqVdDe-duRjirDxJa0WQGD-w4SACAwbCjZlSP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط ۳۷ درصد اسرائیلی‌ها خود را پیروز جنگ غزه می‌دانند
🔹
درحالی‌که نتانیاهو خود را پیروز نسل‌کشی غزه می‌داند، تازه‌ترین نظرسنجی در اراضی اشغالی نشان می‌دهد تنها ۳۷ درصد اسرائیلی‌ها معتقدند رژیم صهیونیستی در جنگ غزه پیروز شده است.
🔹
درحالی‌که ۶۳ درصد بر این باورند که احتمال وقوع مجدد حمله‌ای مشابه عملیات ۷ اکتبر (طوفان‌الاقصی) وجود دارد.
🔹
این نظرسنجی با مشارکت ۱۰۱۳ نفر  با میزان خطای ۲.۵ درصدی انجام و نتایج آن از طریق شبکهٔ ۱۳ تلویزیون اسرائیل منتشر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/466981" target="_blank">📅 10:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">صدای انفجار در بندرعباس مربوط به امحای مهمات است
🔹
استانداری هرمزگان: انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس امروز انجام می‌شود؛ صدای انفجار دقایقی قبل در بندرعباس نیز ناشی از همین عملیات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/466980" target="_blank">📅 09:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a0424389.mp4?token=bGZR-ZIKObf34z0XYJ8vl-INWAIaGHzm4XE30P7azUOvdMWRS-ASy9kdV_wifUjBmDVsh2OEIoHx_-yj4glhyMg5n7rU1IzkH-TunqrRyDImZ73DAI1R9qGnhw6QYIOSmHIw64jz6ywCmELWiFavqknb0GCag2L9gqUbs-_tIavVssGGP116KVV7POmld9spJvQMsnBM436u-wziymo9g67JmFhCSK0GE_xoIqn_xpee7lAdRo2GkzmnnwxsVQRaLczGM7JHH9lkVZwI-MpRl3c69aXreCWFBwTpOSZk-baEGA4LzWOq37tv2M1mCCoURqVnI8ibXh9kyqj11S4bDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a0424389.mp4?token=bGZR-ZIKObf34z0XYJ8vl-INWAIaGHzm4XE30P7azUOvdMWRS-ASy9kdV_wifUjBmDVsh2OEIoHx_-yj4glhyMg5n7rU1IzkH-TunqrRyDImZ73DAI1R9qGnhw6QYIOSmHIw64jz6ywCmELWiFavqknb0GCag2L9gqUbs-_tIavVssGGP116KVV7POmld9spJvQMsnBM436u-wziymo9g67JmFhCSK0GE_xoIqn_xpee7lAdRo2GkzmnnwxsVQRaLczGM7JHH9lkVZwI-MpRl3c69aXreCWFBwTpOSZk-baEGA4LzWOq37tv2M1mCCoURqVnI8ibXh9kyqj11S4bDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
النجار، تحلیل
‌
گر سیاسی: موازنهٔ قدرت به‌نفع ایران است
🔹
آمریکا با تمام عظمتش، اسرائیل، اروپا و همهٔ کشورهای حاشیهٔ خلیج فارس با همهٔ ثروت و اموالشان، قادر نیستند تنگهٔ هرمز را باز کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/466979" target="_blank">📅 09:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY13EbzDW-XQ4QIGbRK_42tCYvl1wS6wvc8azKDGpKRNVsiTAmOSyphuWWbtI2pbt8e6Iw6ztGT9OLGTM7rw0mZDAFAxN3eCLBZOm8JSbpUggfmU4q09QBGiYFnhKpZ6pXcyNUeWNxD3SihOtctIElq2S8tlIZSBtqjXNYooJ6elZkdBBhZ6MPj1sxuFaWlJC8Hrb1Y2nRrI91ePGYHcHrnSpuFPELnH1jQE9wjgA75QGPKzVXU1mH7pzlNs6MmOTDAztnqwLV6gzyRLiMrw3kLYCDPOvHr4hxJxLfT7XsAvAOPFdr3AXiaNchYunsuRr8DaAvtTCYQKxNYszavc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی خطاب به سنتکام: نمی‌توانید مردم را برای همیشه فریب دهید
🔹
واکنش وزیر خارجه به پنهان‌کاری سنتکام از خسارات وارد آمده به ارتش امریکا: در ماه می، سرویس پژوهشی کنگرهٔ آمریکا اذعان کرد که نیروهای مسلح ایران ۴۲ فروند از هواپیماهای نظامی آمریکا را از چرخه خارج کرده‌اند. اکنون این رقم به ۸۱ فروند رسیده است. تعداد واقعی به‌مراتب بیشتر است.
🔹
مدرک؟ سنتکام اجازه نمی‌دهد حتی یک سناتور کنگره از پایگاه‌هایی که مدعی است وضعیتشان کاملاً عادی است، بازدید و آن‌ها را بررسی کند.
🔹
نمی‌توانید مردم را برای همیشه فریب دهید.
@Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/466978" target="_blank">📅 09:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466976">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWOsejSyhQjFaI94HMhAz6v0po4jxemYIxKI109sbapHCLLM_xPtS1s2VPiSkes_k6wfeKKXVUDjx03c-ASWGnMuoD2-nMmMneM0UY5D1bbfv3cQvnFOpSjwZrbd70lXY2WzDsqLjX6L0Dh1SU9T5SuWz4qcnFbfjRlH2SNKeFzVvx3gdHHEjAlcDLEx3c-9ddORYWL3pVCPrWW8LdIIJHl9Jn66asQAK5J8M6aXsLr8vXoLwo0-zysl0EmovNjoIKnGm4g_Rai3xPn62Oq7at22n6xWoEIoliHqAXRRk53kb4UfeUaG3pvzQK44TOsV_lR0WRzUZYvODKQWMftpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس تا ۱۵ مهرماه تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا۱۵ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/farsna/466976" target="_blank">📅 09:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466975">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNcyUXBDty-DinLZYs90clVtC3WizbXF62Dttz7oiJ-Di8yeciIVl3EptppRuiRwrlqUO4P5V1GOMimAhMn9jfWCD-KS1iyhSzb2JBXKJXSV8S6X1qdXKqnqhvDubOY979VKmETE9wLrYFQfxW_hW9rlbe5yeDWU74VuUKbombZWUGdMDVLtpdlM0H71RXjZnxom02sHu6rQ3pgCjA-uP1Xnomzps325JtADLOb-ZkvCcG-hgfpRKYK1VLQ8DfJWdaiSSpVX2trF88zP8g8EGLjX97gVJS1dg2cnX5vFlO8btmorC-adYNv4IIR_gMf0sO2oEtnfMZ2lFxax0oWGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندار کالیفرنیا: ترامپ دیوانه و خطرناک است
🔹
فرماندار کالیفرنیا در واکنش به اظهارات اخیر دونالد ترامپ، او را «دیوانه و خطرناک» خواند و گفت رئیس‌جمهور پس از فرستادن گارد ملی و تفنگداران دریایی برای اشغال کالیفرنیا، اکنون خواستار هدف قرار گرفتن لس‌آنجلس و…</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/466975" target="_blank">📅 09:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466974">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76d1b4d0d.mp4?token=jfqHGOh3UmXAaG2dtXQF_596Fnhv9aZs1rIiRPVJIGBOoDbjOyysXoEMgjJz0dmXLJf8lW9JTOdMcRm0ZySlyUzevOtqq7Ed5vFtvlgmAbcdThCnnY2mUEHP33FKu20B_Ff96oSCr83NYRqeMXEIT01jsQNyySOKlCsXDRvsJQdt1E0KpjEFl9QzmMXAfSpMUT2WQYBLHFb8lmVuxZFXfQ9yHRYeEbHpVTykcJsP4W9HhNtvxc5MBFtEVY_H6nfCLs7u5wCKd8hjKMfK6KSM3MS6cCb3focFEvntN5ISeAj9939RVGyEDIR3cI5I9Mjjeb45psg4ehoz2WOxvJ_JWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76d1b4d0d.mp4?token=jfqHGOh3UmXAaG2dtXQF_596Fnhv9aZs1rIiRPVJIGBOoDbjOyysXoEMgjJz0dmXLJf8lW9JTOdMcRm0ZySlyUzevOtqq7Ed5vFtvlgmAbcdThCnnY2mUEHP33FKu20B_Ff96oSCr83NYRqeMXEIT01jsQNyySOKlCsXDRvsJQdt1E0KpjEFl9QzmMXAfSpMUT2WQYBLHFb8lmVuxZFXfQ9yHRYeEbHpVTykcJsP4W9HhNtvxc5MBFtEVY_H6nfCLs7u5wCKd8hjKMfK6KSM3MS6cCb3focFEvntN5ISeAj9939RVGyEDIR3cI5I9Mjjeb45psg4ehoz2WOxvJ_JWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارندگی‌ها تا شنبه در برخی نقاط شمالی کشور همچنان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/466974" target="_blank">📅 08:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466973">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHwHge1jD9Dmq9JP1ns3hnIWUnxgruDBhSwzDZWe1C5j81s-6My9Ypox-U_D4g-lwMNen2hBeDZMdsbCrsQgHaQPBL8xyTtMIW41iLEBJldxCQPBlgojQvyjuolt45c-c5obnFNxsmytTr5zFhIDaegNgXMWLCSTPD5O9gWmQP2ZIoOEcaqE-0u-KuSz1vHONJ5Q7M-KCXXz2RP1MaJLqr8ny9iOnLtE5BF7fUWHMii5yWaquVuJmA8ky_N68aosIGWjGXwFF99PytV-hJcc5X9JzqpJa2tTLmr_kFJKnOW34A_EF0-7K31hcYfPx4GZPIrVoxh6Rv9gDkypfutu-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۱۰۰ دلاری کمر اوراق آمریکا را شکست
🔹
قیمت نفت برنت با عبور از ۱۰۰ دلار، نگرانی‌ها دربارهٔ بازگشت تورم را افزایش داد و موج تازه‌ای از فروش اوراق خزانهٔ آمریکا را رقم زد.
🔹
بازده اوراق ۱۰ سالهٔ آمریکا تا ۵.۳۶۴ درصد بالا رفت و به بالاترین سطح ۲۴ سال گذشته رسید؛ بازده اوراق ۳۰ ساله نیز با ثبت ۵.۶۹۶ درصد، رکورد ۲۴ ساله زد.
🔹
افزایش قیمت نفت و نگرانی از ماندگاری تورم باعث شده سرمایه‌گذاران دربارهٔ مسیر نرخ بهرهٔ آمریکا دوباره تجدیدنظر کنند.
🔹
از سوی دیگر، ورود شرکت‌هایی مانند اسپیس‌ایکس به بازار بدهی و برنامهٔ این شرکت برای جذب حدود ۴۰ میلیارد دلار سرمایه، رقابت بر سر منابع مالی را بیشتر کرده است.
🔹
تحولات بازار اوراق درحالی ادامه دارد که تداوم ناامنی‌های منطقه‌ای و نگرانی دربارهٔ امنیت مسیرهای انتقال انرژی، به‌ویژه تنگهٔ هرمز، می‌تواند فشار بیشتری بر قیمت نفت و در نتیجه تورم آمریکا وارد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/466973" target="_blank">📅 08:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466966">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFs8y_Qq83Gr3OClNSEO9PyWHjkUwdu8v_nGozggwcx7yB7HpNUVKljH1F9IHB2aPBDZ16OwTssT08GUTeGS94JM-CXFBDQRe06H-jpirFnLxg7WLsOjZd674dxjxN1eaER-t10j2-uzCEOrr0tF11_yJ0LK3YkKXgBACMXiEexziNIOFAZE1PIbAGslVaCo2u6VYdjmCdI2chlatq9SnAfkXUgbctO0SxAX7xIvXCe3CJvB_QpnNkXoG9Mfoxyaqt95U3-I2MA-k2vEOMogQVGassvFJyTiHlhMtP7sv3MPmM1d2MfRidgJwZ4XgqVMVWGy5WwfY7pD6U1phZyXMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMWyWPlePKRpYA4CmyHYVQCgzLLbT5M3r2Y6-6nYUsHTqNEOELSCJvxeh_R_2dUN9vBgUw6D3SPyV3GWaG2E2VTVJXNlqAZc7dSOz4i9uPstB-y6pM0mkoRaEMFePgynCxvJaoAVq6Lu5FomXczZokL5c96KVRNQb-ruW3cktWwkmHlJHP0yaNaMRamb7hXgim0Urpe1iQtCbLzO4tPin6Rr6efdSex5ZeYDmjE3cV3B2I68u8tQKI4waF8Q2or1dg7zbSOmW0lxXV8-MqnnWV5DBlkyqVe5XBvN3Wr9Ml0Bg5tEOlZmrBddj5Qe0vxsBJOlRSRmxYaJI7A36_4eEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcZplas9t_NWCb_dllZ4q0VZa1KlqGJ28T6hpjJmsh5T8Z9xUxHG81HrJi_VI9IRPqrg5RfnW1OTwcccRlGjVk8o65FLE-szevxY9de2gZR9dJavt_mGWxGyrikK-aXIos_bDRjTi6kfuPYTuLCa9y5sgGaSrL3uQiyHo6cqMsn6vzp0WbRVlmRAr87pPpFgyPVto2Gm4UcLBZgByrgvppHiL4flqctBbbVXTyKF76_4HANfRi-kxScewJLytx6nud7B_1envLGjM44D-orUgyQtLh7JFimC05FwwYB2TTMcPa_Zhe7OvEPxLJdTPn4pobgiGvpBSUIL2S97CjlDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkLyvUAJIemwNpZTzUls3xoZNuHD3ndb7njcke9a9ehnocUkgdfTmPs6u1oJKGnUxrOrk6Suv-_mjVfwfuvaE-L3U1Eew4701ksvcTIxDdP-6o0-tFaTd8lOFYXEplpMVDkRYv1dFH9YpQggrLHnyVTCqBVv7ZWDGeAjXgK2ewqzuWESNRNVYv6pQBGm4Y0lrONJ4egxJ_1Lp71CmybhKkusdIoqP1Nz10OdmeAEk3vNaUvSYv4sG9ArG-jv0_AJOAJcwhJUIgfKyAHgoGV9siQE7etSiy0pandN0odMfvReF3eJ9Ns1JSpP1vCFb7pioxylUmA3wkZjpOCBLFfTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qig4JB15E585cpU3FV51Ks-S5fZHY6Uo4nus-aHwwgS-oZhcLlDRQTsbWUJLIG6uIM8TycnMksrRbaW_60kUmhHUF1Lrvve_xsoGEeVmZ3WkJMJIqCsGCGTwwk0ARP6PMC_csxnaMS8X7UUSJOPfqF0HyH4VxgBE59cPwt11eyLT5b1_YQtwsRTKSJEWlvJagA8drkICa4GKx2N5EPZ03FYTtA2SgjU05M-wtioOStrct0yYN7SAFYDv6V6MDikCCXmYryDX_t5TIjucHvss1WgjL1pnk7Df5nUJqVEP8EoO0cVDpCS6fDeRCcJdcfOhqmn5dSIoQd3Bp3gfb3aMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKr_5WShJMJ1FeRtX6knmLBWcrK02qNeMxE_GgE6mu9IcH9kl5X5EONI0rgN-CSrhDjjqWPYtpoeb1ByB41sGx6hQROAfJBe_PsglZFr5TwFMlk1h4MNsvFhAzICgJtPJvTeeN-MQvhuC6y9ShfemKDjA690umZYoG3nkrx0rfOIktKuqvGuUrhO3Q8b41eWSBw_cwryEgS4MUJ8j0WD_ber8yf9bYsfriVwD-Z9SPTAyzjiQU_1NiiFlYW2S82Zni4q410RbL27OBVlHmJevsU9GKl_foqwK8ScdqpuEPdiX543M5JFJvBexGT3i1ikMs8bj03AnK1G9iFqFSp4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHZ_sp8DQ2GpmmCKgzTDtErH4B_OV59vNLkQDM_DiXlB_Mn-vxwiyx6TOmQfg9IPDEjaTqXW7TxpayzThan6MhaN3uQDMY5fQV4kBvGMYqA8PorknOiHVzWEprgJQqyjyu0wA76-as5mcrgXj3wHi15mfeIxmnuzsN_2nRu8l3W8U9io6INCc9xxAdmF9xbdJOqERmlPlclGIYxC0-80GI9SUAzzuJr54Akz260_5n0U43R8Rghb3hCEIbXMu7cNZNyhvyEH8uVmNa75BNeHjqi0CrLhOU1zw6yLtuph5DClEva0DnrYii8HPNjcgZO3-oWcYBSPcKMsKFoEvW4lFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزرعهٔ پرورش کروکودیل در ملایر
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/466966" target="_blank">📅 08:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466965">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16d416136e.mp4?token=FctqSbUCx0tJPBTKB67fTVH4lWMcAIA1b0uJtsyYYohSvGbrDtmiWa5fSGVA9OXPcR2q1hJL7hPYRkKvSR7S5mbzicVd0l-qVtR0hujLAsGfVrLwQeOeTCBeApFG_JNB31O4c4emKjPdoLj07_BEH1V0HmHYLWm9beBScPjp6lKSu3-jMRrdni077zcj83WXQbMSlXWN9csCki6JTaGyjzwNVKOd3T6qt3N-npXVx3NO9uC2o37gkdvUV7DIEfVZnm55aZl7JGnlaTK7z-dIrsPY5QYxQvadxSwwgCn6D_FDhP2JP2S2UnPzAhVXjVm1hUVFXxHQ5CBAIsoz30-t8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16d416136e.mp4?token=FctqSbUCx0tJPBTKB67fTVH4lWMcAIA1b0uJtsyYYohSvGbrDtmiWa5fSGVA9OXPcR2q1hJL7hPYRkKvSR7S5mbzicVd0l-qVtR0hujLAsGfVrLwQeOeTCBeApFG_JNB31O4c4emKjPdoLj07_BEH1V0HmHYLWm9beBScPjp6lKSu3-jMRrdni077zcj83WXQbMSlXWN9csCki6JTaGyjzwNVKOd3T6qt3N-npXVx3NO9uC2o37gkdvUV7DIEfVZnm55aZl7JGnlaTK7z-dIrsPY5QYxQvadxSwwgCn6D_FDhP2JP2S2UnPzAhVXjVm1hUVFXxHQ5CBAIsoz30-t8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورزش‌نکردن مثل سیگار کشیدن است!
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/466965" target="_blank">📅 08:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466964">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پرواز نجف-تهران به زمین نشست
🔹
نخستین پرواز بین‌المللی پس از دوران جنگ چهل روزه، صبح امروز از مبدأ نجف در فرودگاه بین‌المللی امام خمینی(ره) تهران به زمین نشست.
🔹
این پرواز به‌صورت رفت و برگشت خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/466964" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: فرودگاه ملک خالد در رياض را با یک فروند موشک بالستیک هدف قرار دادیم.   @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/466963" target="_blank">📅 07:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vntNpJcUEbtcGLnfMclMUTKy8-uTQy9a01jbUYkvT_ZVKBhhpfemMOk8lysG__5mSgUf-gYyX30dLBYv4c2HiLrffIiCsEkknkajcxtI70gJ-9im_28bPbd38CAs3XsoiFeWnN5Mj8k33tmGUkw_b_9z9KcMEKtWDwiKL3sXLpL5_eko47REIHjU4GqRTMcICGQm1kWTAYnUwTz8yiL2d-WESveajCVayOhkM7bskIdthezQAigCS_M8AKcXSJOXirW3D9KKFuA4OXDXAf72Am3b7Bjoc0ZoZ-dNnk4PmHE0Yb1yaLQEvMjFr661PXicmZMSoN2GHhCwqmsYHWknbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار یک نفتکش در نزدیکی قطر
🔹
سازمان تجارت دریایی انگلیس: یک نفتکش در نزدیکی قطر هدف چند اصابت قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/466962" target="_blank">📅 07:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هوای تهران در مرز آلودگی است
🔹
شاخص امروز کیفیت هوای پایتخت با رسیدن به عدد ۹۶ در محدودۀ «قابل‌قبول»، اما در مرز وضعیت آلودگی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/466961" target="_blank">📅 07:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoTkKaPXrgqoFdf7RPNXnCz4lWxOAy7QTVxCtek3PgUezjv-4ChUIAeoCDaRFG5ZaF5fsXP2CZvDqwZFKXg13tUc-7PyItrkH8FczJHnf3rAh0fCkPN1m4kjDSACLCDEAugfQ7AAnFMFC3FdbuaNNT9vhggJBf3nk383l58dcaYKo4zpNcsqBg6t64FFO6yV4fdGNUxhbw_dAF7nXL_FvVfBiBNyQDKJvn6XTTDGBDeJObrd59wzZTVWET6_OKec4J6mVzK5ykfvzhwpetTkwCiLxjrJQoc6k58HaNIpfn_C2kd-MztsSlPwFMAX2bh9LaaE-UqGTyLV7nu9LTN5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگزاری انتخابات میان‌دورهٔ آمریکا بدون ناظران اروپایی
🔹
برای اولین‌بار در ۲۴ سال اخیر، یک انتخابات فدرال در آمریکا بدون حضور ناظران سازمان امنیت و همکاری اروپا برگزار خواهد شد.
🔹
دولت آمریکا به ریاست دونالد ترامپ تروریست، از دعوت ناظران سازمان امنیت و همکاری اروپا برای نظارت بر انتخابات میان‌دوره‌ای ۲۰۲۶ خودداری کرده است.
🔸
سازمان امنیت و همکاری اروپا از سال ۲۰۰۲ بر تمام انتخابات فدرال در آمریکا نظارت داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/466960" target="_blank">📅 07:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466958">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: با موشک‌های بالستیک تجمع مزدوران سعودی را در پادگانی در منطقهٔ «رأس العاره» هدف قرار دادیم.   @Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/466958" target="_blank">📅 06:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466957">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه: بازار نفت هم دروغ‌گویی ترامپ را فهمیده است
🔹
علی محمدی، معاون سیاسی نیروی دریایی سپاه در واکنش به ادعای آمریکا دربارهٔ عبور نفت و کشتی‌ها از تنگهٔ هرمز گفت: اگر واقعاً نفت و کشتی از تنگهٔ هرمز عبور می‌کنند، چرا بازار نفت متناسب با این ادعا واکنش نشان نمی‌دهد؟ چون بازار هم می‌فهمد شما دروغ می‌گویید.
🔹
اگر نیروی دریایی سپاه را نابود کرده‌اید، چرا در فاصلهٔ ۶۰۰ تا ۷۰۰ کیلومتری قرار گرفته‌اید و به تنگهٔ هرمز نزدیک نمی‌شوید؟
🔹
نیروی دریایی سپاه بر تردد شناورها در خلیج فارس، تنگهٔ هرمز و دریای عمان اشراف کامل دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/466957" target="_blank">📅 06:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466956">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyBa8_nqAgxSgz6mIG-fIyQXzy8XijIXsCNFDbVs6Sm5sqRiTPFJjMI7mbZ79iejQ08eKz154lnN_lblty21z49mgWeekQE6DUaTMIMWRpCuWCq2PqmOF7Kc0BXbH3GrvIgVzueZQFMx_B1fqQQUbxJVU7ErmG7MPoWKFjA3qGwIjF22rS6iVVnYuwmOB-NBekeh0zvjP5o032gxkNXqq6Mr4nrM6O0oBL4BEWG1gbsDPXigj3GiYMKM5RGqfM5rn1TYx7AhSBcl4sE3WhE6pKkC-IkZRB02NfyVB7mtbRLu2W607FxgAIpvHv37R9adcin1CJIRdBoFl08nZXCXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعودی‌ها برای مبارزه با یمن دست به دامن سرکردهٔ سابق القاعده شدند
🔹
یک مقام آگاه آمریکایی و یک مقام نظامی سوری گفتند که شورشیان حاکم بر دمشق درحال بررسی ارائهٔ کمک نظامی به متحد کلیدی خود، عربستان سعودی، هستند.
🔹
به گزارش رویترز، منابع آگاه افزودند که گزینه‌های در حال بررسی شامل کمک دفاعی برای محافظت از پادشاهی در برابر حملات یا اعزام نیروی تهاجمی برای کمک به نیروهای یمنیِ تحت حمایت عربستان، در مبارزه با انصارالله است.
🔹
مقام آمریکایی شرح داد که عربستان سعودی از شورشیان سوری درخواست کرده است که نیروی نظامی برای مبارزه با انصارالله اعزام کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/466956" target="_blank">📅 06:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466955">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن:
با موشک‌های بالستیک تجمع مزدوران سعودی را در پادگانی در منطقهٔ «رأس العاره» هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/466955" target="_blank">📅 06:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466954">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/466954" target="_blank">📅 06:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466953">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سرنگونی پهپاد ترکیه‌ای رژیم سعودی توسط یمن
🔹
سخنگوی نیروهای مسلح یمن از انهدام یک فروند پهپاد مسلح ساخت ترکیهٔ ارتش سعودی، بر فراز آسمان استان تعز این کشور خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/466953" target="_blank">📅 05:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466952">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOpJDhp_uinEZzB4lBPc4pXvgWOtuiU4nGgvLUMNJD9qAK1WyMGt1hkgQeFowgNJbKoaYyrwGPTHd8Z9sJK_NhpH-HfrI532IhavILVL_1DX_h7DrzdnZlEMoy7wExFZdz_mER7TICf7Na6OP-jbnFBz21cxhntEK4NoTZebn4rh0HX0vYoECQCgeMmrxFuuMZS8yXSVGhl-F5DeEO1iobOW5AsUC7aAl_0O92SuFlTg9_V-T4bhQiBWl_ry564b4mu-qqwRtw1pkSesPxkJ51ZxGCgXi-hjAbG61mgXq0p_L-QR3Z7T6jACmIPgM8od9SNkL0DD_YLH96oxIiiPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم حملات رژیم صهیونیستی به جنوب لبنان
🔹
المیادین: توپخانهٔ اشغالگران، حومهٔ شهرک میفدون در شهرستان النبطیه را گلوله‌باران کرد.
🔹
منطقهٔ وادی‌السلوقی و اطراف تله‌الدبشه نیز هدف حملات صهیونیست‌ها قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/466952" target="_blank">📅 05:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466951">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7iAxYrX7ni4WpiApj-O8pjbcPGBYy6SAbtcXh2A8FJLOPrjJicDzc9pI24iOcKOaVDGDmA4s3vijdWGwEALSNlg6a0POaJlBgaFipr5m98r20_hbhYPF-LTASVh29ASVB7IHY_UX5cRBzWqOIaWqtehLRChoFVjNBczWQMq5xbHqzEOWnzNAbSl71s8UZAomCMa67MXfIVgfkCWYQXf0mrKVic7GBkbuhmD0vVeT9ihRndgrH9c0yKyjku8wGCX8YLorGyG0RUBH82Bmbw2qIfrmfIxlKVj6YDt_ZJk0P1qhPQbT7D2-IWaC-iXMYD1g26BSKAaFJLGAHHfm_ACOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا اتهامات جدیدی علیه مادورو، رئیس‌جمهور سابق ونزوئلا مطرح می‌کند
🔹
سی‌ان‌ان: دادستان‌های نیویورک قصد دارند اتهامات جدیدی علیه رئیس‌جمهور سابق ونزوئلا، مبنی بر شکنجهٔ آمریکایی‌های بازداشتی در کشورش طرح کنند.
🔹
این اتهامات مربوط به بیش از دوازده شهروند آمریکایی است که به ادعای واشنگتن، در زمان قدرت مادورو زندانی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/466951" target="_blank">📅 05:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466944">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOwWYYvBhItqpy33AS_hhALyftOtsSGe0Rqth_3U7OLwxB8dmwEyTPGTNj8mX0s3HTITmot_DU4uyuQkgxhv4drzc7H3EhePjHFcgoUD4YGedbpcjMZD2swRqeCqOV3P9O2llh0gBclc_XhyUWVlM9ABZAszYRvI9ic2XFiPeNvvN-sFqYWekx2P0TlHs1_PcgNQEbD4ZUmZfvLkMo1Ikj7v3JF3ZYQ-l3Currp33BRuNeDP4Kz9skYFnocarQdogq44IH6eIvmL9F5dkjRM3o_aen1I7GiOg1sFphKdIkKii5_q9nFGEkkOHIqP2-S-fTeM2TOY55I_KO_wZBDO3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8trJ1l7fhRNPslFwqJpYb7dZuq0I7BjmcAtc7868oc0P6HNfJTH6Kfr_gdKD8E1UWO4dKxysTfn1SyxkSdSxExbIA3wl7g8s1oDLICkmLCB7pBZjP8woTp4IY8O40EB1u8OiOyvDM6Wi52-YHwHO2cWiZ6RACVo-c7CN_Oye8d2_G29No1i0So_D-gkInbEufkF8VdtjWKjNBs3SAlCiSpad9gZmcYBWst85zufUl32uXlv_PBG2D_153VHF01bbvFeyRLk-ut607Rp7SoIePXmbCrOrg8xEl1fLMyAfH-7QkGQ_rERpEOqeBbkXR54SrqtHoo7CQdJ9RykqKboow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lq5HK56zlXggmZSZtup1phuHF24vfnIb2HvVXtt5BbJoaQiIjG2aaY4anSRQS5yy0DLbS_22j_GLryLpQaPwxALeaLKmpZmlcLxKmSDo2K2961mADZ9YVCpIbeBFdkqGmFPjWLTIIh86OzryS0KjHWnI_U9-SDGwXba0uH5lW6KXsDXrcY0y001FlcF-oI8L5YQ8fxJa5iifbELP2lgFNOUkn40AXPPr5zIPiJqbSWUnV8NuSibEBI7-RhPd7Q-J8X_U7rnDnAXQzCAtZmoSUa-tdCiheBmMT6Zvifz7yu0NJqS9VDl7YqgLBl7WSi0jbpHbRlCDAPZH2Z5FhWZWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIRZHZ0TU1tSkwgFOyOMXFKwt7UChvpf4NOwx6ufm6GrHl4mt44oDGE-CDBS_d6omItuMzOXAGrMVsGU2AwJXdvuQQbh1Ih7vcqiewPDquZ_Cm8SxFni7Iz3Rp6YUGBdty2EXgq5suPsW0BFffqLMny5YSDa3ruIJd7Se5IYrhwlo4xrepjV1VJ5-QKjSu-cY0YanGIrB0-18yBMXjiFTbZOjUMWWZPrOALizy7vybQFZqSTIQ7fk_GNQ8IO1InNE_c4d5sqA9br-1X4W2sOMmMWaDKQGcIQvMlNst_YUOsqp39cyUdNRAsME9Ba9pCdh48DBkYQESdQ3YHgFDxn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wmys9eFXGb_ldOeic85eqDqmz0LpOhcxnN0kAJ2cqyY4GnbGUPRKyjyo8bqjhhpwRSSlst6BlHocApmd7iyX3hFJyMo3likRBC5PH4gMWKp8Th72gKPVE3Vv8G06QOKBA3Pp7Uc6wJZ1mTUPU25SikY3hwHSpjb-XV2gUCO7LuhOTDOjx-6JE8JODlB3-vxfzxQqnIDaiBLcU44w02eZ9SLXMrLQononMNKC-bAIyp67OGQOsAnfKra_Ks8ZVc0ywSNgb3XRJn7ASoSioYOQY7LFDy0Ry5fQ_sJa46mskW-JZ3BRztrN2DCOaplnMgNPMP7c1c552zsJxjUhqbctTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FuakfqN4xSuNRJQuFZ4B55qgwCcInc85zUhIuMvSo4kTs464RPX5qTVWrmegzJNd9ufElQsuLc_nZYYNEfnbx67QD3qsfxs6imcSiSvSDrL1NehOSTRjD6mXHYzVYYc0fbLk4pZuwOCo-pIFWqBkYzhv9GximLHPJTXheBDDtDGxZT_eS42JUkKwonBSLo0tFQ1N-Q6HEzEUykDlZbwU2odySjk7Lex4y01sZnrPQaXe7D6njc7p6JQI28Va5nzZaht93jzjq2paXpkEJGhQwo1Wd1ZaaG_1k8k5fAUAh6LU0nRZkxtj0E8KI_0PowXeLS1-iAf7jZZQYu6f9P6LJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nh1Wxj-hFDlPDXK46TLHSIlmamt3jZRuVzkVlYCHmMHDSMhwk9T3ajZkMIFy51Zb14d0uPF-YD3t2Q8soWELi50qstHIog_d4GTxI2i1nB18dYKH1Gus3qKrByUxHbGecYXjvmNBJf2N92KafBoc4-D8AQsJsyFmF0GpaAXUAX4ZJPf5UsX8-ZKMkMfuEgomDUpgt_ajhBOfpvnuvROVlq5czn7G9WKQg3z8dgiW0d68j7OtYBjsWqi2qUoU27WRPP5AnKe9EnOSPWKRY0MgoNo0i5wwAbtDFcDnT1zqobl5vjjzY7ca_hW-rwvcBH3fFd3XW5d5jXOcGJUfykTGQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
روایت شمس و مولانا با صدای معتمدی
🔹
محمد معتمدی در آیین افتتاح آرامگاه شمس تبریزی در خوی قطعاتی با موضوع شمس تبریزی و مولانا اجرا کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/466944" target="_blank">📅 04:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466942">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQ8nHdvrjg6epjl6DpXcd99OAFNxz9NjDebEQS-vKUiXnvtfhNre1WaXclAjhQcDtrkcS9fDwDsetAUtoErO01oMsSgeO-MaXh-3AwGG6ZlKOttwWhGT3Awa2OHEC4qwu4kPbqeufGPaYSixsr_n5-fYrXrEawODx9yq2VTKS3JaHV-H_m3MeRQQ61wGvOHx2nJdDDIXgzd3Wtfu8x4qSo6tKKWN7CzXVBS9Iqa4ut_X8y1O_y88_ZOGHPrKdSHNJ5dnl1sxpOOd1oPJg7jO_pbCa0aN_IG3SVho5PKg-VWEK09on7bKHtrwREJnMYWij8GlaCS8QM0IwtRBMyi8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DdiVf7gg1P67Wvv8ywIILo2UcbT7539lganApVSSkE5XeWYZ1ggyU_VDzkolp6o_aPex33Th8cYHHszC8eIfUjFC5WbqbEy4q3FDCADiK5bnVkPHRc5xtDNH6kA6KCbnsb1p6XHUAlT4b4kWunlYDPGEwc43LHRJ7sMZ7nOdVVDbuovRVrLb4qHw8Gw3MyFXCPyqaExNRzMkxT7pXfSh_F1CqhYHsQVGCj21B1-zPJ_VdtgwonnEw025fNpVqRngWi7bsVNuT2mjxdpEnggd_Q3800DMJft0xyTVYAl1RgU2B5O960KHwdQUuwiX80NeRUuEQBuHHHw7Nfd6GVGjGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سقوط یک پله‌ای فوتبال ایران در آخرین رده‌بندی فیفا
🔹
فیفا رده‌بندی جدید تیم‌های ملی پس از فیفادی اخیر را منتشر کرد که در آن ایران با یک پله سقوط در ردۀ ۲۳ جهان و دوم آسیا قرار گرفته است.
🔹
ژاپن همچنان بهترین تیم آسیایی است و در رده هفدهم قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/466942" target="_blank">📅 03:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466940">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تصاویر جدید از ضربۀ حملات ایران به پایگاه آمریکایی «عدیری»
🔹
تصاویر جدیدی که به دست شبکه سی‌بی‌اس نیوز رسیده، خسارات گسترده‌ای را در پایگاه محل استقرار نظامیان آمریکایی در کویت پس از حملات موشکی و پهپادی ایران نشان می‌دهد.
🔹
نظامیان آمریکایی که خواستند نامشان فاش نشود، در مصاحبه با سی‌بی‌اس پایگاه العدیری را «کاملاً نابود شده» توصیف کرده و گفتند که ایران «آنها را به شدت مورد اصابت قرار داد».
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/466940" target="_blank">📅 03:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466939">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اگر شب‌ها خوابتان نمی‌برد بخوانید
🔹
بی‌خوابی یا کم‌خوابی مزمن، سلامت جسم و روان را به خطر می‌اندازد. فرد بی‌خواب دچار خستگی، کاهش تمرکز، کندی واکنش، تحریک‌پذیری و افت عملکرد تحصیلی و شغلی می‌شود.
🖼
به‌چه‌کسی بی‌خواب می‌گویند؟
یک متخصص اعصاب و روان: بی‌خوابی زمانی مطرح است که فرد دست‌کم سه شب در هفته و برای بیش از یک ماه، در شروع خواب یا تداوم آن مشکل داشته باشد؛ در چنین شرایطی، پیش از هر اقدامی باید علت بی‌خوابی مشخص شود.
🖼
درمان بی‌خوابی از رعایت اصول بهداشت خواب آغاز می‌شود
:
🔹
داشتن ساعت منظم برای خواب و بیداری
🔹
پرهیز از مصرف کافئین در ساعات پایانی روز
🔹
کاهش استفاده از تلفن همراه و سایر صفحات نمایشگر پیش از خواب
⚠️
مصرف داروهای خواب‌آور نباید بر اساس تجربه یا نسخه‌پیچی خانوادگی انجام شود
🔹
قرص خواب، در صورت نیاز، تنها بخشی از درمان است و جایگزین ریشه‌یابی علت بی‌خوابی نمی‌شود.
🔹
مراجعه به روانپزشک برای شناسایی علت اختلال خواب و انتخاب روش درمان مناسب، به‌ویژه در موارد طولانی‌مدت، ضروری است.
🔗
مضرات بی‌خوابی و خطرات داروهای خواب‌آور را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466939" target="_blank">📅 01:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466938">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f0accde21.mp4?token=tgHWxxqd2R1CzDf9NaU3RXk7s_JdG3iK9-p82wGq3B8T5Y9NBu3lw3IS_E_L0xXTRXZiLqB3MyNNNSJUwrzseot_0pNEcDmUa6K8MN5zYMVvl5yOxhAiUiuzxNaLZK9eT5PSBLYQ1xg3qd9hOYIEC6jJ5V4dwmyol73WFr_hbb4PvkJo5LJ7oAQO0XvIdl4EUS1ay1yq7Hk1YG5vs2nRDC80hNMoaLxV7T-xYj4J89ZT-4Bq69MQ2XnS2pmaRH7JTdEvgQGo4DIs8b_dYY3Aovel1tHGlaXZ1SqpTavhIIccYJ7T1-povHuxwCMSmn4ZxgJa6ICHAjf1C-QP_l_eQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f0accde21.mp4?token=tgHWxxqd2R1CzDf9NaU3RXk7s_JdG3iK9-p82wGq3B8T5Y9NBu3lw3IS_E_L0xXTRXZiLqB3MyNNNSJUwrzseot_0pNEcDmUa6K8MN5zYMVvl5yOxhAiUiuzxNaLZK9eT5PSBLYQ1xg3qd9hOYIEC6jJ5V4dwmyol73WFr_hbb4PvkJo5LJ7oAQO0XvIdl4EUS1ay1yq7Hk1YG5vs2nRDC80hNMoaLxV7T-xYj4J89ZT-4Bq69MQ2XnS2pmaRH7JTdEvgQGo4DIs8b_dYY3Aovel1tHGlaXZ1SqpTavhIIccYJ7T1-povHuxwCMSmn4ZxgJa6ICHAjf1C-QP_l_eQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تولد یک‌سالگی کودکی که هیچ‌وقت پدر شهیدش را ندید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466938" target="_blank">📅 00:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466931">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3BT4odGdRhoJSTql3hIPGrDPPUdibACeyeNlxSFXuaXoWpX_ZM40FyqcRCccQh1BGFsFxrMR1hksEXBufrpfv_Oyjqvn5V2MtAiq0O0-qzsttpWfu2J-oPBY-lpw-1bxQMoNN_-16RXJWhrvRHomxk-tIEU6sUsbse32OaXqfzPmw__akwyeDY0-cRajHS_VL3Giav8wWf1xjQVzRUbRxmDvMkLJPZ_qZWDUn401bLKAcQzBF3aYyW7HtK105a1RL-6oEY0fGoJN_IEofmwJ6NXgyNgbBbaHusxxkVh2KMKaqkvZ366-1QHN5DK5c1O9fr8FKLdEjEEREGWa822bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-W7HSKQHY0klnwdx20gn2R_xT80p6xOnWgUF--X6jieZ3pkvZNtXMfGcj_Q0pSK34acgz8gXuO8qelsivcHtlHBI1vg75qkF3zIJMzO5dgdP1IzLssU5Q6-eCWWGbgMNOWwU8JCXvLBe6rGkQgqFvT3hf8Wf1Xsfi3V2gkoYjyWeprmLbt_M1Er_xa3Eb8HmYsAJ0qQtqOfu3avCVnZySPKSbY0I-Qe5fxpfI0R2D3wB5NOTzk6jjh3dUF-mX5Hu-Msvy2mUQIu0eZogs2xlaXn7crb6FB_4gmxMs7JpqUJUnT9rvcDfglx_Bm8gbZs6j8hOQoWVv5j3BrVR-ILYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXb2xPMo8jD1Jw0y3VKI2gSzYflCkITW3h26JHKXc_X2nzoBE_VkM-CWgsQrcZ8WhxHK2wT3F4f5cRWNXvMvGpukFqmwU_utLjFpw-cawBtxvmhDFLC01lixOwLjJUGqH5dELUrdOd1tPXCy_0a4jVyzg42AbePuHLFTY7SglnPTuGlmw84t2yvjx2tFk1LFJBlY_viF5nEAFwDX5dvk_4IMIm0dRr0Z3kvPGHdlaNRBQTQwtP6ChQufAyOU_oBAs9iXPZ636wz73W3lPMyb-EJs-Wx-vFiawhTkHdis-01e_xmYefidnH-MNhA1P9QkD1PWkAHSXHSPRIRLfiaL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvZT3e1f2WtfwpUiFwuv610i78WUt7jza6sGWySHNjfB0RPrjYeitfSoywwaxqTMzkJWhikfNy8bM17tey3ftiotR2nLXTkB1h2WcEz5GusMCLnRjjaIaVEG43TJVpqFCn3cFGe0N-zFAszaAYEN5AbmrQCewP7jN1OCERNR7PkGd0WZbU1Q8RsoyaBEZJMxRDVh7akxalM-ctGQ8u1veW9SrI3g0rTnuKNAjCK6_AWdgfSIcF4MW8ZtH2xlZpROg31xJHNPjHvKZsO694uD25cgnCy-733Dfx70yJBzrJONFg_Lt9noYYQsXyqhPOo1VHN2q_yVHoCCtyUS6orguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4J4FdQUiIm8Fx25mhRHYOCh3_Kc1JCj_MVfVPNLxUC4qBJ2KSE97bXcppFZFzLoDgUY5IdwxmFQlvcursxaNn5oKXCLsSbwALwrS3hSgJG8C5UUHDCkkZTqI8S83miPEVEtfa01bwU7KU0vCaaztYTIu2XL3K_Ermc-eoEfjrtdvfXtR9Z1SVwBFSn1LJ5bMvuk4TczT09SmDGRECNr7kHTTr25rPC3O5z317ta2jU0xk2-NkwGZgnSSHL4XimXvYZAhmCdHC5wUARmKBXXIIheHToSitMj9sMQrbJARc9w2WA-lYtTbwEII6e2c2IcuNMBpChnmtRX6Fqxnw6njA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c0c_P3jrevkbM66a65zK_xsXuY6up_vTmplOfxMgxo47dx2Y7XqaoD6SsBhRDi23eLqkGZGUuNaTvTOaxOAwbKlDrzSyurxXYmyd09lWh9myn9Kri_zf-dJbtc_xg38TprDoZF-fmw0nfkHrbpfibe4xzH3mDLwQGFjUV9ey1KsZNW76k_xjQmkC1rpMDsWl9zejQJBoaUhrgg2w0TJJ2EfXaL7IFS3Gs7QpEAbzSbrILMiFnc9B7APsLSBsyDvsuFd_7CkgQNwDRntMbuALVIIgF2eonav-qvYa3uynErPVarCDtLUlAe7bQdytd-qFvVI01OjnZbSUk2_qQcgAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csGo7z5Vn8CMqwPY_EvLj-19hWKCUQJKm_KNg9FX-bjAC27qJLgy3qwHXounFw7QENhSi8S1hRDTLUriN-JCraj8G0g46AOIW86M3ArJqpMmjMQ3gMW6C7hcYT7rhFJR9ZOCrHNmKNTcnduyNBAPx6s5C6_CNMy0WZNfBKKxmNradKg1NwwaBEdtZxhjtiup9uhr_3dthz3LGvijyp1eFbzy8oLts2PsmEzCeSyr9WkbpRgqdzSW1Rpcf8H1WZx5lNdHkVAajR46ihutMJukw3kxHLVqSM6lHYqMoP5hYuex7h-a575LY2kTRtfIFxEPpNoH8kUfuN3H-nDLlVsA6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رونمایی از سردیس شهید سرلشکر محمدسعید ایزدی در میدان فلسطین تهران
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466931" target="_blank">📅 00:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466930">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCaPviWdUkoJ6NAvff1PuzLuhqfFhN7WmB7kSp9u1vcmUbzrgWy22VkjFGqVTGieZTMT6pT_OhMGThc0vOnwAlcjLdEr4KVkR2AKItQ1xtjlUTuum4dpdSVoDJwY5g7Y077W__plY4z1o-5uQagIVqy1NqSVj3VEgH0F8AiJkichZZRzUBzB5fUQ-63qnjatoucPB9m89A2Joj3ybUzX3BQeE7X6Yn-1gvSjC0w6_B93f32Kvh6jHH4NTq5eqTNJyXb-tmY93u3vsSwpAHhWbeg_ZQFdHCHRMcut6MeIrvV0TFkPDrBcx-ukTyR28V4IU_xVn1uzyG1Ihoa6PfGnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبلِ توخالی
🔹
روباهی گرسنه در بیشه‌ای می‌گشت که به طبلی بزرگ پای درختی برخورد. هر بار که باد می‌وزید، شاخه‌های درخت به پوست طبل می‌خورد و صدایی بسیار بلند و هولناک در جنگل می‌پیچید.
🔹
روباه با دیدن جثهٔ بزرگ و شنیدن صدای مهیب طبل، پیش خود خیال کرد که درون آن پر از چربی و گوشت لذیذ است.
🔹
با زحمت و ولع فراوان پوست طبل را پاره کرد، اما وقتی درونش را دید، متوجه شد که کاملاً توخالی است و ذره‌ای پیه و گوشت در آن نیست!
🔹
پس زبان به عبرت گشود و گفت: «فهمیدم که هر چیزی که هیکلش درشت‌تر و صدایش سهمگین‌تر باشد، فایده و خاصیتش کمتر است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/466930" target="_blank">📅 00:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466929">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVQ95C8TbI_k5VN2y69DOIFsYz9YE8ynTPvjLFgwsU0aLMuu8RoGY6iFur52_pcYOG3lw2I0sWpoXkQj8g9PwcQ1SlgfFVjQnDnCN68_EviW8o9KWmIZHymwtW5P8H_FPRF2SQ6cU9nWJVchz4XamnPHWGGg9qmRIHSm6QkHQfmJdhEi7FRQnKSmMqhkLtNI4qM20Hq_k524Xo7zLe0kWU6F5dhTmQ7BH1jqGSIl6Mexzoucqylps20MKF2Gijui4x-XxqNq6uFRkOLy300CMDEj5en2oFCW7-fUrGXd67EFpnLIveGKbaZmFKLzU-xooU7JLp4gzGtg6o7fVm_RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطعات حساس جنگنده اف-۳۵ به دست چین افتاد
🔹
بلومبرگ: یک اشتباه در روند ارسال قطعات جنگنده پیشرفته اف-۳۵، باعث شد محموله‌ای که قرار بود از مسیر کره جنوبی و تایوان به آمریکا منتقل شود، به هنگ‌کنگ تغییر مسیر دهد و در نهایت به دست چین برسد.
🔹
محمولۀ موردنظر شامل دو قطعه از جنگنده اف-۳۵ بود: سایه‌بان کابین خلبان و درِ محفظه تسلیحات؛ هر دو قطعه با موادی جاذب امواج راداری پوشانده شده بودند؛ موادی که در کاهش بازتاب امواج رادار و تقویت قابلیت رادارگریزی جنگنده نقش دارند.
🔹
یکی از مسئولان دفتر حسابرسی دولت آمریکا گفته: احتمالا چین پس از دستیابی به قطعات تلاش کرده با مهندسی معکوس آنها، ساختار و فناوری به‌کاررفته را بررسی کند و راه‌هایی برای مقابله با قابلیت‌های فنی جنگنده بیابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/466929" target="_blank">📅 00:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466928">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7pFOrZjgADvxwoyYxzeFXth6IClh1zbtBLfCTv8wdAp68SVGrvU47uYVBzqSAbI8uxfOwR4EY0CYaqpOuL3jpuH0o6VoDuFERYiZDCRFCNmQijigHspYandP6J9tur0dtqNiekXfAfhaWt3S8c7ZPGQNHQ404ctNR8448zdfxMyxu8s5DFpUIwGsdwvl2WQNRGYxwdnr_9nInP1n2M9kZujKqPHCJFB35Ds2N3Csz_X0-QHM1J5UC4R2mn3IdEEjxW9bXqcCr9FEeLs-mK_2ki7pk0ppyC-y6HeJCA4dRnnMPElrJYNQKleCfxbnzm6AeSV7fBDCRAaYsQ2txs_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس مجلس: وزارت راه باید قانون مالیات بر خانه‌های خالی را اجرا کند
🔹
نیکزاد: قانون مالیات بر خانه‌های خالی نوشته شده است؛ وزارت راه و شهرسازی باید خانه‌های خالی را شناسایی کند و از آنها مالیات بگیرد و سامانۀ مربوطه را تکمیل کند.
🔹
البته من معتقدم مالیات…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466928" target="_blank">📅 23:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466927">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a6bedbf.mp4?token=WZB2NyjYY3cnEfR9_4tzBbxkoGHn5ES0dlVi2kppOCKwj6rcJGhgsNxSzFhTScHYPSf2I2V2vR8L2x4vkooQOxdv1NKHxFdnsFFE0YflTRD1vpJr6asHAMTrFMMrMW5tU2A6Q-ENmdJX_4xL0izXJJ7V6T5wrv8_kDa6JhTHgl6FZczeChG-cO2iE2K8hhSqvMQGrOv4-7W9OzkYy_HHyyFsRNgPF_OYOOeK0Lgr2EI7jsIGu5S4gwgugxQNJ3WbMa5WYp0bqsbTW9pFLu020KYKi-VAdglEHVzHXAisF7RO5tzZ-nXBQoGWjYacm7gQgz-uXFMnoKKGACMx2fqrvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a6bedbf.mp4?token=WZB2NyjYY3cnEfR9_4tzBbxkoGHn5ES0dlVi2kppOCKwj6rcJGhgsNxSzFhTScHYPSf2I2V2vR8L2x4vkooQOxdv1NKHxFdnsFFE0YflTRD1vpJr6asHAMTrFMMrMW5tU2A6Q-ENmdJX_4xL0izXJJ7V6T5wrv8_kDa6JhTHgl6FZczeChG-cO2iE2K8hhSqvMQGrOv4-7W9OzkYy_HHyyFsRNgPF_OYOOeK0Lgr2EI7jsIGu5S4gwgugxQNJ3WbMa5WYp0bqsbTW9pFLu020KYKi-VAdglEHVzHXAisF7RO5tzZ-nXBQoGWjYacm7gQgz-uXFMnoKKGACMx2fqrvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: جامعه زمانی به آسایش و عدالت می‌رسد که درک مردم آن‌قدر بالا برود که عملیات روانی را به‌سرعت تشخیص دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466927" target="_blank">📅 23:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466926">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce2f555247.mp4?token=n8ykvEt9cLmD517FS6SieIev1MAzv_2c04iLd7Pcl4Xf33ds-aSAYfQb2TSpjRDPMZiGSBPr44DgtzmnB7e1xMgMDGvNyEt0tynTp7VJLQ2hPoraqHAtj8eXs_bCzO3iR0i4_jMw8eicrQ6lzsaaD_6zXVvsXfYyTqxHpX1ecM2y2ptXf7ZGZNepU_qqcYtT_cakMGxAJ9M5J6D5BlanSZ17S-Bz6hnJ97okk8KprDYo8Xq1qGuB08_NrhCvDaqPj-jZUyLv-7_RWx-uPHZewNYx8-ELwhka-ebfpBAu1Tm2c8j0rl5EpfrCeNTtg0ZlklUntd9Qd3E7EsmqCAVASQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce2f555247.mp4?token=n8ykvEt9cLmD517FS6SieIev1MAzv_2c04iLd7Pcl4Xf33ds-aSAYfQb2TSpjRDPMZiGSBPr44DgtzmnB7e1xMgMDGvNyEt0tynTp7VJLQ2hPoraqHAtj8eXs_bCzO3iR0i4_jMw8eicrQ6lzsaaD_6zXVvsXfYyTqxHpX1ecM2y2ptXf7ZGZNepU_qqcYtT_cakMGxAJ9M5J6D5BlanSZ17S-Bz6hnJ97okk8KprDYo8Xq1qGuB08_NrhCvDaqPj-jZUyLv-7_RWx-uPHZewNYx8-ELwhka-ebfpBAu1Tm2c8j0rl5EpfrCeNTtg0ZlklUntd9Qd3E7EsmqCAVASQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتتاح مقبرۀ شمس تبریزی در شهر خوی آذربایجان‌غربی  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/466926" target="_blank">📅 23:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466925">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA7Z3Tvbg-dyNOeYN2iRuB79JBOYL5fW9oPRyrPWcIRSef5kXYOA7rzMc_uDzpxYNKLX2uPsYjmVMjp7c8zyNHPA2vHf_abKnDgSR9LglFEgRZpeV-gaGllIcqWbOT8u4xlM25dFxjMc1z4EHHmyHixkMoj8e_jQi3nxU1xO_ibQeHL7t-kvRWsaocUgehj5qP5aa9LmNqeoq6JYesqc-3t0D3Z9vdHTIrFwusjAST5yRWTCQRNdi_I1kZpRBHfSkOYbC4jh_-lDrvPur-BQpTSzvmjkrj7hA_EcGHT4AWGQS5VkXeUbVnw35O1dU63s5mxbUw-aawsBCWXcWk7ibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانه‌هایی که برای فروش نیستند!
🔹
«در تهران بیش از یک میلیون مسکن خالی داریم که به نوعی احتکار شده‌اند» این جمله رئیس مجلس محمدباقر قالیباف است.
🔹
دولت می‌تواند با گرفتن مالیات از خانه‌های خالی، مالکان را به سمت اجاره یا فروش ملک سوق دهد، اما میزان مالیات اخذ…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466925" target="_blank">📅 23:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466924">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/236f2a908f.mp4?token=IPUuqdPBxNfWL226K6zv6-opAw60JZPPavWDg2kvB5ugF5nnnMKLQcZJUf_85QPLooORFfDoZ1CnKcdmg5q62NsrUgGNIiyC-8WboS1DETrNnon6rJaKlWFALbIamIh-JNWuGpCLkHevciiDgE3uyJjWzgQJdrijnxgSApqcpo5wQd1JmykYH15c9fX4e95fQ1FVC5O_v7MKHnt9v8dwRZb1AhC3Po3Odv0XmSQkmAwxXIrxfVgsuV2KYR8fnDu3KdI7dq_-fKbPk7lnXusMrmHYJy2LjFpn2kR3kQD0kXcUb5o_kLjpeWR6RWs4HjTRyQlSpIUBGKvT9M5koPauEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/236f2a908f.mp4?token=IPUuqdPBxNfWL226K6zv6-opAw60JZPPavWDg2kvB5ugF5nnnMKLQcZJUf_85QPLooORFfDoZ1CnKcdmg5q62NsrUgGNIiyC-8WboS1DETrNnon6rJaKlWFALbIamIh-JNWuGpCLkHevciiDgE3uyJjWzgQJdrijnxgSApqcpo5wQd1JmykYH15c9fX4e95fQ1FVC5O_v7MKHnt9v8dwRZb1AhC3Po3Odv0XmSQkmAwxXIrxfVgsuV2KYR8fnDu3KdI7dq_-fKbPk7lnXusMrmHYJy2LjFpn2kR3kQD0kXcUb5o_kLjpeWR6RWs4HjTRyQlSpIUBGKvT9M5koPauEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش وزیر پیشین نفت به ترامپ: به دروغ پناه برده‌اند
🔹
ترامپ دیشب از استعفای وزیر نفت ایران دستاوردسازی کرد و گفت: وزیر نفت ایران استعفا داد و گفت این کشور نه اقتصاد دارد، نه نفت، نه هیچ چیز.
🔹
پاک‌نژاد در پاسخ به این ادعا، عنوان کرد: استعفای من هیچ ارتباطی…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466924" target="_blank">📅 23:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466923">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee18efaaee.mp4?token=GHAh3kw1kBiIIIx44dbPAvEgIAqdLnRnlFK2eGVMTpTVSIwoZ656v-0ProHUyoM-IEUcmLVcPpkW5rFkMAK47q6IL2HP_EgU8JQz1A_xGjesvbV-g_TH1jfNxADpDFim8_XClhvBRNGMTcdpaLeMSnIQa04ePV3uUCX8jv3ivXhYezEjSe4BXYiB_vg7wPoEeKcni-X8SaGCZr2a5ZddFQAauG0T5dGhkmeEkkk4goxqC_M5MB2btAcZ3w6lXugvBc8Ue7GudqTmsPi38npt5pRdQCNkhrx12Pe-rs0KWunaeguu8WlUHj1LxSH-GKGq9sdMSOWCdCOykqaUSjHJ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee18efaaee.mp4?token=GHAh3kw1kBiIIIx44dbPAvEgIAqdLnRnlFK2eGVMTpTVSIwoZ656v-0ProHUyoM-IEUcmLVcPpkW5rFkMAK47q6IL2HP_EgU8JQz1A_xGjesvbV-g_TH1jfNxADpDFim8_XClhvBRNGMTcdpaLeMSnIQa04ePV3uUCX8jv3ivXhYezEjSe4BXYiB_vg7wPoEeKcni-X8SaGCZr2a5ZddFQAauG0T5dGhkmeEkkk4goxqC_M5MB2btAcZ3w6lXugvBc8Ue7GudqTmsPi38npt5pRdQCNkhrx12Pe-rs0KWunaeguu8WlUHj1LxSH-GKGq9sdMSOWCdCOykqaUSjHJ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۲۲۱ طبس؛ میدان هنوز قصه دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466923" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466922">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6_1pF6xsbVoXluZhfbo9PYJInE81X0MaiYo9IfKOMkTXhlB02bYRt7NgBDiwZo0PqP0YylXzsPdp-dZ9VKm678YharOEZMYweaNpalQFFM-7Rjwac3sWgWT2meIBYqKshOBfYgv05pNm1kiTHaJQDTCXte-XLdztoWEZIMgVUzEZ9YFzcHR-YUzoEKWQFilcWnzGIT2MzNBLiFcSGNZa9zuA5FdJ51-gmlJG78zN7QiRrrHXoAy9wC_POV6s8wB0e2rQQn8R9oF0uPh79eMZLKsEEbaoyfmUxFCSQhrvrED9iquTdlKAHNws7PWKrhquGbQC0QarJapAhm6fVnHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار یک نفتکش در نزدیکی قطر
🔹
سازمان تجارت دریایی انگلیس: یک نفتکش در نزدیکی قطر هدف چند اصابت قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/466922" target="_blank">📅 23:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466921">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
تصاویر دیده‌نشده از حضور رهبر شهید انقلاب در مراسم دانش‌آموختگی نیروهای مسلح سه روز پس از عملیات طوفان الاقصى
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466921" target="_blank">📅 23:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466920">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
سازمان هواپیمایی عربستان: فرودگاه‌ ملک خالد در ریاض و فرودگاه شهر ابها مورد حملۀ هوایی قرار گرفتند.
🔹
برخی منابع خبری از توقف پروازها در فرودگاه ملک خالد خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466920" target="_blank">📅 23:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466919">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd94d2bc6.mp4?token=si5AldqWxkEdN9N6BOdfYw3360tpRddXleHzgX9AelHuKAGImZoUdjaRFVI1Rmpq1TFLlZrJidNWrI8JtvO5NjQORQj_Ru1TSBXa4EwnvOgERFvUDjGvkrXhwuoR5cVJ7apIBodtFuaPyFxWrRjMW-Ihpv1OE8bytEqd9k_VAg8fqgcAi9afmCkNiKvmtC8ENZ6ZoKdKR08_BFIBgCEF5YrKTPfyoWF5exJs_trXFxwgi_UwRQqjotyiEDN7uk2vcDoFA0A5oA4_VQnzIYbUGvbAc4Izt1oSXN2DFJ-igtTl70t6uVH1um5vbzS3FalCBXyj6Y-Rgfufgmk4TQScKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd94d2bc6.mp4?token=si5AldqWxkEdN9N6BOdfYw3360tpRddXleHzgX9AelHuKAGImZoUdjaRFVI1Rmpq1TFLlZrJidNWrI8JtvO5NjQORQj_Ru1TSBXa4EwnvOgERFvUDjGvkrXhwuoR5cVJ7apIBodtFuaPyFxWrRjMW-Ihpv1OE8bytEqd9k_VAg8fqgcAi9afmCkNiKvmtC8ENZ6ZoKdKR08_BFIBgCEF5YrKTPfyoWF5exJs_trXFxwgi_UwRQqjotyiEDN7uk2vcDoFA0A5oA4_VQnzIYbUGvbAc4Izt1oSXN2DFJ-igtTl70t6uVH1um5vbzS3FalCBXyj6Y-Rgfufgmk4TQScKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا زاکانی: به مادرانی که در سال ۱۴۰۵ صاحب فرزند شده‌اند، تا ۲ سال خدمات ویژه ارائه خواهد شد
🔹
به ازای هر فرزند، ۳.۵ تا ۴ میلیون تومان به‌صورت ماهانه تعلق خواهد گرفت.
🔹
مادران برای ثبت‌نام در این طرح باید به سامانهٔ شهرزاد مراجعه کنند. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466919" target="_blank">📅 23:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466918">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a605c86601.mp4?token=pHSFDsPbMRlrdWQs1ZQ3CaIHXF321t1zs9g8AvesBLS-bmL07mPPYOpiKcYDJJ69PRzIHcqSF8M0lEKI55yd4JUYdAiXDN0Ralcx6ubaljmB73c0uMsV5DPfUjU1cNMUP3N7iaw5pL9raUzh6tdbw_AJKGxV3uqDA9g6o33mhwzTqV7ZfDBzluEuRz1zEGqkVdttcXmcCcgo-f_F8gEbD17nFFt-I3UQPMPiOsJxcROCuqQuXpwUAo3vfgHMZbxVzD30xiHs8jm_plb2QsiPWmd61pq_cuI1MxHJS_ADtk4PfTCm9AnHklqefPAyvwWE2ij0XJ9c_XY1498nPVjWlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a605c86601.mp4?token=pHSFDsPbMRlrdWQs1ZQ3CaIHXF321t1zs9g8AvesBLS-bmL07mPPYOpiKcYDJJ69PRzIHcqSF8M0lEKI55yd4JUYdAiXDN0Ralcx6ubaljmB73c0uMsV5DPfUjU1cNMUP3N7iaw5pL9raUzh6tdbw_AJKGxV3uqDA9g6o33mhwzTqV7ZfDBzluEuRz1zEGqkVdttcXmcCcgo-f_F8gEbD17nFFt-I3UQPMPiOsJxcROCuqQuXpwUAo3vfgHMZbxVzD30xiHs8jm_plb2QsiPWmd61pq_cuI1MxHJS_ADtk4PfTCm9AnHklqefPAyvwWE2ij0XJ9c_XY1498nPVjWlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: نوسازی ۶۲۹ هکتار از تهران را در دستورکار قرار دادیم
🔹
شهردار تهران: قانون الحاق به شهرها یکی از راه‌های فاصله گرفتن دولت از فروش نفت است.
🔹
یک درصد شهر تهران را یعنی ۶۲۹ هکتار را در ۱۸ منطقه شناسایی کردیم که نیازمند نوسازی است.
🔹
در ۲ هفتهٔ آینده…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466918" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466917">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
منابع لبنانی: رژیم صهیونیستی مناطقی در جنوب لبنان از جمله اطراف شهرک‌های حداثا، المنصوری، سلوقی و زبکین را بمباران کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/466917" target="_blank">📅 22:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466916">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b957a1b42.mp4?token=Rin8Nu3SMwsj4TTQZzKmKQWe_0OAeeTNi7C5xJuoBl1Ur8gmny3Ys81Ur-YPxvJlB9OI5gwmOZ9fLMXhqpsQa5xC_rfVsqZlZTMGSfLPXfWOjTGKUpRXDM-L7UMzhYSU5HJoqPsN8f_PueqjvbhtTfb5oAx_9WpSkPhNPuSfyZJa5zoUaCMvqJ55cc5fGf7zHqK1m3vMrfV7Chx-aB2NDABfXr3BF3yB-Si4scXcWr1eGzqIOT3pYkOxBFO4CH2oNIZUPX8ptbr7CFtDjUfHj86RlhPtbcSZy43DIcIpRB1qda0i5zvhioAFmwxZqdhfN3VKwlEXuTsTtgCgohUcXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b957a1b42.mp4?token=Rin8Nu3SMwsj4TTQZzKmKQWe_0OAeeTNi7C5xJuoBl1Ur8gmny3Ys81Ur-YPxvJlB9OI5gwmOZ9fLMXhqpsQa5xC_rfVsqZlZTMGSfLPXfWOjTGKUpRXDM-L7UMzhYSU5HJoqPsN8f_PueqjvbhtTfb5oAx_9WpSkPhNPuSfyZJa5zoUaCMvqJ55cc5fGf7zHqK1m3vMrfV7Chx-aB2NDABfXr3BF3yB-Si4scXcWr1eGzqIOT3pYkOxBFO4CH2oNIZUPX8ptbr7CFtDjUfHj86RlhPtbcSZy43DIcIpRB1qda0i5zvhioAFmwxZqdhfN3VKwlEXuTsTtgCgohUcXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: ما از طریق واردات و حذف واسطه‌ها یک میزانی از کالاها را در اختیار گرفتیم و به بازارها کاری نداریم  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466916" target="_blank">📅 22:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466915">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859d884080.mp4?token=fzNgVGQT7buqjWuvFieCesmnxCFMliSJ_TCsD1lCCufKctZN0GKN0NekMBqi1YqbnaAu2u5mUVuWcMxUwMbpP-IuLs1CCi2pBpDM-p9X5elmsunMmcYJQQSPWF3fMnkpv-nN87E750p_S78rhP9AAw7sBaeDhYVskQwkp_i9XilZYgsKzPUteCwIluDIvknw3uumCwe8HofT1NhIsQDr04-4kFWfFg9i53PwYc8JXeRvJ0i2esrYefbjfBdCMG-iZ0M-_AlJxOSPKovEpJzw-L88dBYc-LzftedLgCwIi4K6oPlDLUp6cspCnYT1ZTZdocyG9YUpMkY7nElp4txD6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859d884080.mp4?token=fzNgVGQT7buqjWuvFieCesmnxCFMliSJ_TCsD1lCCufKctZN0GKN0NekMBqi1YqbnaAu2u5mUVuWcMxUwMbpP-IuLs1CCi2pBpDM-p9X5elmsunMmcYJQQSPWF3fMnkpv-nN87E750p_S78rhP9AAw7sBaeDhYVskQwkp_i9XilZYgsKzPUteCwIluDIvknw3uumCwe8HofT1NhIsQDr04-4kFWfFg9i53PwYc8JXeRvJ0i2esrYefbjfBdCMG-iZ0M-_AlJxOSPKovEpJzw-L88dBYc-LzftedLgCwIi4K6oPlDLUp6cspCnYT1ZTZdocyG9YUpMkY7nElp4txD6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: برخی اقلام در طرح تورم صفر ۵ تا ۵۰ درصد زیر قیمت میادین عرضه می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466915" target="_blank">📅 22:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466914">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شنیده شدن دو صدای انفجار از سمت دریا در کوهستک
🔹
دقایقی پیش صدای ۲ انفجار همراه با موج بلند از سمت دریا در منطقه کوهستک سیریک در شرق هرمزگان شنیده شد.
🔹
تاکنون ماهیت و علت دقیق انفجارها مشخص نشده است اما بر اساس گمانه‌زنی‌های اولیه، این صداها ناشی از شلیک تیر هشدار به سمت شناورهای متخلف در محدوده تنگه هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/466914" target="_blank">📅 22:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466913">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee7e152513.mp4?token=VLy2_XmECogeemO2anxfwgyv3JNcedEP9R9P_rpipnjS2p2KjwQhARMAKuMDMooL9mMBpAbfAGEz_yCSNUg_ow3ABZBc0YSZbKfQbt0D87z8Ax4AOtCt3EQ3VQc8DCEiEMpcESoaM9d7bxHXf7cN7GBBff2f-8MN9uqJhZdWfzErkJFhJced5581BROK6v3PIx0qSljdvZ8TesDvG0qTGlyYeQTMn4DvRb-RNCvb2XXPSdMW7b4ZQWKmELCSJ--nNAXBDgbsv9KEK8kmhoFfhb2P3_kdYQB9UqrAkyCx9DMTTjV7tN_0NNiZO6gWrBxSwgEPTZaHAYD9Y8OsORVOAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee7e152513.mp4?token=VLy2_XmECogeemO2anxfwgyv3JNcedEP9R9P_rpipnjS2p2KjwQhARMAKuMDMooL9mMBpAbfAGEz_yCSNUg_ow3ABZBc0YSZbKfQbt0D87z8Ax4AOtCt3EQ3VQc8DCEiEMpcESoaM9d7bxHXf7cN7GBBff2f-8MN9uqJhZdWfzErkJFhJced5581BROK6v3PIx0qSljdvZ8TesDvG0qTGlyYeQTMn4DvRb-RNCvb2XXPSdMW7b4ZQWKmELCSJ--nNAXBDgbsv9KEK8kmhoFfhb2P3_kdYQB9UqrAkyCx9DMTTjV7tN_0NNiZO6gWrBxSwgEPTZaHAYD9Y8OsORVOAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: از اعتبار شهرداری و اعتبار بانک‌ها و فرصتی که از بانک مرکزی برای تسویه ارز می‌گیریم، استفاده می‌کنیم تا این طرح درست اجرا شود  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/466913" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466912">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک تروریست در شهرستان گلشن سیستان‌وبلوچستان به هلاکت رسید
🔹
پلیس سیستان‌وبلوچستان: در پی وقوع انفجار در مسیر خروج ۲ گروه انتظامی از ستاد فرماندهی انتظامی شهرستان گلشن، افراد مسلح به سمت نیروهای انتظامی تیراندازی کردند.
🔹
نیروهای انتظامی در واکنش به این حمله، یکی از مهاجمان را به هلاکت رساندند و تعدادی دیگر از مهاجمان نیز مجروح شدند.
🔹
منطقه همچنان تحت رصد و پایش نیروهای امنیتی و انتظامی قرار دارد و اقدامات برای شناسایی و برخورد با سایر عوامل این حمله ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466912" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466911">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ebf243c97.mp4?token=UywsmsohU65bvg47xX22EQjWtgKUDnJbZaaL29-9F5327H-_XQ3J25uFbprxTRgLULx3UhmDWYpp688vDZn3F2ZrwzmFE2yRcpKRRcHLQxLtAr8DGcLtR0-gYb-XniA2hJmaFxz_St4JtPC7hN7XrpqzFqon5a2qecnbtg8qulUpSIO1bfnUfLTJhUkqhMqSX19Y2dOUyp4wCI6LbbqK5xmyIQkWNMqK6g_WQi3pMGc8ODaUISiAe6LJ_lWNtcnFz72QZkgDbNooDIMvFlUzvx7NYODnlLIj0EpF9bG2BhmKrhmh-AVKzQvYsbmsS6gD0MP-RYqTj_GYJDwuCvpRbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ebf243c97.mp4?token=UywsmsohU65bvg47xX22EQjWtgKUDnJbZaaL29-9F5327H-_XQ3J25uFbprxTRgLULx3UhmDWYpp688vDZn3F2ZrwzmFE2yRcpKRRcHLQxLtAr8DGcLtR0-gYb-XniA2hJmaFxz_St4JtPC7hN7XrpqzFqon5a2qecnbtg8qulUpSIO1bfnUfLTJhUkqhMqSX19Y2dOUyp4wCI6LbbqK5xmyIQkWNMqK6g_WQi3pMGc8ODaUISiAe6LJ_lWNtcnFz72QZkgDbNooDIMvFlUzvx7NYODnlLIj0EpF9bG2BhmKrhmh-AVKzQvYsbmsS6gD0MP-RYqTj_GYJDwuCvpRbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: از اعتبار شهرداری و اعتبار بانک‌ها و فرصتی که از بانک مرکزی برای تسویه ارز می‌گیریم، استفاده می‌کنیم تا این طرح درست اجرا شود
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466911" target="_blank">📅 22:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466910">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: هواپیماها و تسلیحاتی که بارها و بارها به‌وسیلۀ آن به یمن حملۀ هوایی شده آمریکایی هستند و استفاده و به‌کارگیری آن‌ها به آمریکا وابسته است. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/466910" target="_blank">📅 22:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466909">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dac456efa0.mp4?token=PjqIu98af2xTsN5RYJjwgrgkaymxweIgH00BkoZvblZLOcnaEv3DdRp3muMKs7x_vDeFdt5ZeV8ZLyi8HiwGJCmLEz1soB-mcYt4mLIzAD2Vp67ol3rXxMK9L3qHG9v70gUaPf2OYMlB6zxfDazKRBT_8NxY6-rM-bZWGc_E6BakvjQQHb-w9V7zxgDFFVeMeT6fGGkLeZxQIaeQHfNw5OV6QWKVZlL--kpL5awP3C2ahvem0RvolZ5i3ZBvWr9tjWBloO4_xq_uKQCYGY5OvibSn0nrGnqxU29AyQkTY_jbEh_kpRh_AgPX9PY50xh0jhYSR35s6D1YAawByoM5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dac456efa0.mp4?token=PjqIu98af2xTsN5RYJjwgrgkaymxweIgH00BkoZvblZLOcnaEv3DdRp3muMKs7x_vDeFdt5ZeV8ZLyi8HiwGJCmLEz1soB-mcYt4mLIzAD2Vp67ol3rXxMK9L3qHG9v70gUaPf2OYMlB6zxfDazKRBT_8NxY6-rM-bZWGc_E6BakvjQQHb-w9V7zxgDFFVeMeT6fGGkLeZxQIaeQHfNw5OV6QWKVZlL--kpL5awP3C2ahvem0RvolZ5i3ZBvWr9tjWBloO4_xq_uKQCYGY5OvibSn0nrGnqxU29AyQkTY_jbEh_kpRh_AgPX9PY50xh0jhYSR35s6D1YAawByoM5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: ۸۳ درصد ناوگان اتوبوسرانی را نوسازی کردیم
🔹
امروز بالغ بر ۲۵۰۰ اتوبوس به ناوگان اضافه شده است و علاوه بر این، توانستیم دیروز برای اولین‌بار اتوبوس سه‌کابین را وارد بندر کنیم و این روند درحال توسعه است.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466909" target="_blank">📅 22:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466908">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc2a0e22d.mp4?token=RC6kDGk4fNvWHpOcenscBrcco48Vi9Wy0aMY02AXP_F8iDa6AiDv3EMFYyihMQrtIMb_qqiPFVeZG_uatNpnbg6qQP_WOv1d7D8BEq5-YjXwXvhho4MWMWl43wAAugmDRU-WYwhzuYNSAPNO99UrktpxEjvK86qoxRkTWHZeBCDhrfJE9S88iTBqubvdDJrdJozmdR9g6I6KxD0dyEgfVhSpNSSnfFgbQfDvTj8uG68GAg_Ci1PDy24IK5QJcmDdHspLws0LfKS6wwMwlxPmw8msiaNQ0zZCpI4mOiLsbcJPSCofY9cf7HwIgHbgL9SfhkJmRf0TNwW5IspW20R3PT7U9CmDXBtGVNUaUD-uWb9L5Z_Bcdpj926v1wneDpRHEtM1khRHff1Dd7IaX5-D36hsKduJ8gs7a1uNcjL6fA4hXRF7xPXywtJPrjgK7i_fhhqkZeqka6pSGz1smGCsQ42PQXkkLSyoGKqnyDPw-mHBCtGjBewFD3VlOFbWde-XEXIg2TPwHbbfrw5dVHyKHvVO3WR5tvmcOwCwiDSvdK97PUI-622EnEN11haph_4BE7A0EHWaVaSes4rEZBOebRfVpp9Dctv67IIQSQO2v7q8XNL2LGubQoM3aI8DrxbxTTa6jWj1-6w8A7f4rCriqLtyipaoBinbQxTJny3oAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc2a0e22d.mp4?token=RC6kDGk4fNvWHpOcenscBrcco48Vi9Wy0aMY02AXP_F8iDa6AiDv3EMFYyihMQrtIMb_qqiPFVeZG_uatNpnbg6qQP_WOv1d7D8BEq5-YjXwXvhho4MWMWl43wAAugmDRU-WYwhzuYNSAPNO99UrktpxEjvK86qoxRkTWHZeBCDhrfJE9S88iTBqubvdDJrdJozmdR9g6I6KxD0dyEgfVhSpNSSnfFgbQfDvTj8uG68GAg_Ci1PDy24IK5QJcmDdHspLws0LfKS6wwMwlxPmw8msiaNQ0zZCpI4mOiLsbcJPSCofY9cf7HwIgHbgL9SfhkJmRf0TNwW5IspW20R3PT7U9CmDXBtGVNUaUD-uWb9L5Z_Bcdpj926v1wneDpRHEtM1khRHff1Dd7IaX5-D36hsKduJ8gs7a1uNcjL6fA4hXRF7xPXywtJPrjgK7i_fhhqkZeqka6pSGz1smGCsQ42PQXkkLSyoGKqnyDPw-mHBCtGjBewFD3VlOFbWde-XEXIg2TPwHbbfrw5dVHyKHvVO3WR5tvmcOwCwiDSvdK97PUI-622EnEN11haph_4BE7A0EHWaVaSes4rEZBOebRfVpp9Dctv67IIQSQO2v7q8XNL2LGubQoM3aI8DrxbxTTa6jWj1-6w8A7f4rCriqLtyipaoBinbQxTJny3oAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«الله‌اکبر، خامنه‌ای رهبر»؛ شعار یک‌صدای مردم شاهرود در شب‌های اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/466908" target="_blank">📅 22:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466907">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عبور از مسیر غیرمجاز تنگۀ هرمز، به روایت ملوان هندی
🔹
یک ملوان هندی با نام مستعار «سینگ» با فارس گفت‌وگو کرده و روایت خود از عبور کشتی GFS Galaxy از تنگه هرمز و هدف‌قرار‌گرفتن آن را بازگو کرده است.
🔹
او علت اعلام نام مستعار در گفت‌وگو را ترس از پیگیری حقوقی…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466907" target="_blank">📅 21:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466906">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
۲۲۱ شب حماسه سازی مردم مراغه برای وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/466906" target="_blank">📅 21:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466905">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">البخیتی، عضو دفتر سیاسی انصارالله یمن: زمانی که سعودی اخبار پیشروی در تعز را منتشر می‌کرد مزدورانش در محاصرۀ نیروهای مسلح یمن قرار داشتند.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466905" target="_blank">📅 21:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466904">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1219f7bd2.mp4?token=MPglVbBU1wRy4PvsMiiALJhdySE50X0u3dRYaoFyS7xPFpD1gX4gjVF5sFVNCEVTDI085KRGrRYSAS7m9YuVrn5j8A0GLYxO7al6w8F-TzxYvql_rFqo6s5ILPqZWtKF1LmI7fxEHGJPjTkCF-Mk-hON8Xqupz3vuyMm7yIFN0ljvCI35-nhrEc9NHTlsAXeiQzNcCbJWG2JBPLFnkSdYJLGdY6n4DjpBoXzjrLkXeU0ygJEjGKapna_Zk-rlK6vTxMWJMcH7UElngGaPU8i8k2_2FXf1Djc1Rht0yJd-Dqx_P1wEoZnaG0th-c-cwGnTLDzbZZn-7pnDIwT-JSPrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1219f7bd2.mp4?token=MPglVbBU1wRy4PvsMiiALJhdySE50X0u3dRYaoFyS7xPFpD1gX4gjVF5sFVNCEVTDI085KRGrRYSAS7m9YuVrn5j8A0GLYxO7al6w8F-TzxYvql_rFqo6s5ILPqZWtKF1LmI7fxEHGJPjTkCF-Mk-hON8Xqupz3vuyMm7yIFN0ljvCI35-nhrEc9NHTlsAXeiQzNcCbJWG2JBPLFnkSdYJLGdY6n4DjpBoXzjrLkXeU0ygJEjGKapna_Zk-rlK6vTxMWJMcH7UElngGaPU8i8k2_2FXf1Djc1Rht0yJd-Dqx_P1wEoZnaG0th-c-cwGnTLDzbZZn-7pnDIwT-JSPrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گناباد در شب ۲۲۱؛ عاشقی زیر آسمان وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466904" target="_blank">📅 21:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466903">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTnABHsxOxDbFRvTAJ-iglAKS36kz4Onv9R070AUbEdClLmy3AFPnbZCSFcUy4XRW_rHjIYvUeFtEK1xTwf8pno7eKPPxov3ykmKfrJur7XoeemzNNTmapRzAoa7KGp6JZeFeFBjaC237h9qg22FpuumQ_kZv-OVJdnpmg9eXySCY5uLcChhAyLXAhSmupNCV00aKDEfSliIPCskN4W7Z_9ejyU57Q-nOZXXP_yBF88CpTg9xdNqBOxoZOKJC46Q1jwSnpegrYnw20uiQQczS7XQkUWejzHJ5o0u3t9MDoAZ53nBL0j-b5BAk3KlmS77mjVAH04a8p_E3SKsVKByjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تیم سپاهان نقاشی کودکان اوتیسمی را به‌عنوان پوستر بازی با فجر سپاسی منتشر کرد
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466903" target="_blank">📅 21:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466902">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6abf3a44.mp4?token=fGTS9OUOj6wGGOHGuRm-MTAxPFgfVGRZ-wGwXoV005s7YlEg5pJ344sg0GIqVHpEE4yutpFh5MGfOPXDpfgTglbbZ3JF2o65VykMi-Qn0rtY8w7lEoZ1GT7ykRtrz-15iw4cDmEDFwQUlKznR5XKWdOpoXw1QqlLmc7FNIol6--6QLjLwsTgeJgkASmElOmwoqOuQi0BF2zSnfGi_8JYGKS0RI0pps_ZMFYbNovW7UxOFBkiiffZMbZOwpTsDNQUKpEE9sE7AEi8nXw6UqkRbsb1c-gy3nJ2gWqpq6916DG1fbAi1uYnyzQr5FnePHt3i59F4Yv3SG6VcSU4GxykZXwhpDNzG-4mVDzfSfebnfuFId4Bzb8-h6UFJ85dNowB0zk4iTSFqCzx0Ygk2YMM7VSf0cHb_DmXqQp-uSCGMFzz1qR1oZEDpme_0vdBo4xm0EKPQ0tr2fG_yXU5sHHG3CyXjwlNGwmEyFZMVeYRXYYEEOLZ1AlyH3vsAYcH1fYSinWShsYx_hfdV8124bDL5Q5v7pNQm4XN9_y5Tt682lDtf2Oimetc6-bC_3ZFq9uzW-1txcWwORptecIWUCON_eFs6tNBRGt1rQwVc9JT0eNnNXlrxgQ5NgWBPkM4yGJz4PagIH703QihfOEfpWQYXwA227AwkJu8m7hsLeN-8qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6abf3a44.mp4?token=fGTS9OUOj6wGGOHGuRm-MTAxPFgfVGRZ-wGwXoV005s7YlEg5pJ344sg0GIqVHpEE4yutpFh5MGfOPXDpfgTglbbZ3JF2o65VykMi-Qn0rtY8w7lEoZ1GT7ykRtrz-15iw4cDmEDFwQUlKznR5XKWdOpoXw1QqlLmc7FNIol6--6QLjLwsTgeJgkASmElOmwoqOuQi0BF2zSnfGi_8JYGKS0RI0pps_ZMFYbNovW7UxOFBkiiffZMbZOwpTsDNQUKpEE9sE7AEi8nXw6UqkRbsb1c-gy3nJ2gWqpq6916DG1fbAi1uYnyzQr5FnePHt3i59F4Yv3SG6VcSU4GxykZXwhpDNzG-4mVDzfSfebnfuFId4Bzb8-h6UFJ85dNowB0zk4iTSFqCzx0Ygk2YMM7VSf0cHb_DmXqQp-uSCGMFzz1qR1oZEDpme_0vdBo4xm0EKPQ0tr2fG_yXU5sHHG3CyXjwlNGwmEyFZMVeYRXYYEEOLZ1AlyH3vsAYcH1fYSinWShsYx_hfdV8124bDL5Q5v7pNQm4XN9_y5Tt682lDtf2Oimetc6-bC_3ZFq9uzW-1txcWwORptecIWUCON_eFs6tNBRGt1rQwVc9JT0eNnNXlrxgQ5NgWBPkM4yGJz4PagIH703QihfOEfpWQYXwA227AwkJu8m7hsLeN-8qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفانی که زاویهٔ دوربین‌ها را تغییر داد
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/466902" target="_blank">📅 21:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466901">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e84c609aa.mp4?token=bKXRPqb4WU6rQ1U-OD30kNigv4RSYSn-xaU8V0NjN9pNE3X4IF6Xyi8GmuwTwp4PHN5mC24E39MVvdpA7j3CzyZUy4YPtVQE0udikC0zEaSkT61YSNaEE0I_s8QOYsHXn9VVPPu-3t6PeLaTPBtPTq6qbIVqovtOmYWPcyAVpLoWT01BUGe8GWeggkdL-VASDZDem8sjviRziRVAWZEeecBKvuMv8todjYg9SEXOpFkVmC6hWZOlSWaNrAk2IdqsqwetGxqcGMLo-1R6ru9XyVs_6bqiFVDCqrMjxQs9jn5AaF7ZAmeZeIvxMcWshfsdHRp9ErFy8C1OxL2RieD3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e84c609aa.mp4?token=bKXRPqb4WU6rQ1U-OD30kNigv4RSYSn-xaU8V0NjN9pNE3X4IF6Xyi8GmuwTwp4PHN5mC24E39MVvdpA7j3CzyZUy4YPtVQE0udikC0zEaSkT61YSNaEE0I_s8QOYsHXn9VVPPu-3t6PeLaTPBtPTq6qbIVqovtOmYWPcyAVpLoWT01BUGe8GWeggkdL-VASDZDem8sjviRziRVAWZEeecBKvuMv8todjYg9SEXOpFkVmC6hWZOlSWaNrAk2IdqsqwetGxqcGMLo-1R6ru9XyVs_6bqiFVDCqrMjxQs9jn5AaF7ZAmeZeIvxMcWshfsdHRp9ErFy8C1OxL2RieD3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از تندیس شمس تبریزی در خوی
🔹
در سفر وزیر گردشگری به آذربایجان‌غربی سازۀ جدید مقبرۀ شمس تبریزی افتتاح و از تندیس این شاعر نامور ایرانی رونمایی شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466901" target="_blank">📅 21:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466900">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db8oBj7hbMNB7hxSrX8T2TlYfad6rctsbfktAQYoi68CtlXBAzttF8k3NfFSJAVJ2FbmLycqaz39k4_I1T5KLnlsgCt9zaJipwJEg9wt3lUxN1U1W_1U_cgakCgZvURqyaCdetS-zLk8Zq9ViyVu8kQcKUUB4y9Hm7_U7bNq7A0lhjaNue-vJ_oSDQ19iKD14_dJM8VrnxYfzP90zrViuKlfy5WulIv-J4v5OS2LN9VrS8g_3YsGJOLdE-oHiQrel_kzHLmXvbHUvaiarOMdEO73RnyjbkIdw3Q87iUQTbaZy2xEKUOqK5Awg3-eXRqgoTOAL2EPyjOhWJ5xdUC31Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع مزدوران سعودی هدف موشک‌های یمن شد
🔹
سخنگوی نیروهای مسلح یمن: تجمع نیروهای متجاوز سعودی که قصد پیشروی به‌سمت مواضع نیروهای ما در شرق استان الجوف داشتند را با موشک و پهپاد هدف قرار دادیم.
🔹
در این حمله ده‌ها نفر از آن‌ها کشته، زخمی یا به‌اسارت درآمدند و…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466900" target="_blank">📅 21:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466899">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889dea5fe9.mp4?token=KeTWDdZZMAf4tOvL2GXYbIaxM79HazT8Rgc3lVH6_eHhPXqg2zD1WonByD9nsMbLF5TgZFjVg_tvI-e7LikhdTNfFRovOCB2iMijSADEVyqrlZFXUK5VrGnh7gqOoIsZvKRJDZOkzvFtbebNeuyHlUxgKnngMyPj67V6ISWcrQ7Z55y5mZQehu-HppoFPhgV49kU38890-0XClOqR84M-K4uofWclGxO3nxmXw7wJFZ9_4jZHjWEmNH_rTZOtx9XdwwbhbXH2emhenTmi0azOkVLghgYD7cuJuWBTPXHRLLODmdcNFlLaetwkWdefUWyObL0GjFZCcFniM6ejBkdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889dea5fe9.mp4?token=KeTWDdZZMAf4tOvL2GXYbIaxM79HazT8Rgc3lVH6_eHhPXqg2zD1WonByD9nsMbLF5TgZFjVg_tvI-e7LikhdTNfFRovOCB2iMijSADEVyqrlZFXUK5VrGnh7gqOoIsZvKRJDZOkzvFtbebNeuyHlUxgKnngMyPj67V6ISWcrQ7Z55y5mZQehu-HppoFPhgV49kU38890-0XClOqR84M-K4uofWclGxO3nxmXw7wJFZ9_4jZHjWEmNH_rTZOtx9XdwwbhbXH2emhenTmi0azOkVLghgYD7cuJuWBTPXHRLLODmdcNFlLaetwkWdefUWyObL0GjFZCcFniM6ejBkdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مظلوم‌نمایی از تروریست ممنوع!
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/466899" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466898">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab936b32ca.mp4?token=gcBJKvTKeMdpiaRmXqv_4oyzWy2NZk1oV81ATwQKg_9D-TQjzWB5oxjeq4-8iOrAW5iNFiMAIVPhY-D_CoAZGpvjIrAayIisfRcMWmhzUyEOBewv2rCwaNX2bt_KFXZdT1ybxd4IxnG7qBNzB_rC1HGZq8Fl60TBhDhhzV95c41P1Ag_pcsZs9jWshMGiunAhJk1JhGfAe2on-wI3gv8y-Rb5gvFP9mtO3cbOaQ7kkRqeVdl3EFDVS_tbNyJhiRSFsJHeTBJu_f9-1A0rjjPGbM7fDt0Kf6YW9Skz4vCUl8bCA2BcMmp87zVHVZCEWoUhE2LxI1xOu68Xh-4CEcrYGJkG-HaYhd1I8Fqb0KGMO17XXbm05hu91_y5cLCvKmziNvbl-H2fMVWgqolnv-gcx6SEmWc24w51JYOQe-uqCyezJH65R5Jr1iobD45cxdPPwk669lmTr70pIB_-Qpmh9z56H6wMkLh5552qq0eaQyHSRdn1wXrkLIQaZky2kLPjappqWpmgXtGiDl4nGwfZJ5CSHNc979N2J3DQx5uj-dcSs7ItQhjzdRAfBGgpfOvlb4a5qt77U0-RqwvCTZleu7Hr9CHMBq4DdsPNOQwu8Lxdchd4KmUSNjJIO2omvWPqYbH3-Twcar1iKzwx1yluPkk2knhdshaXm_jfwatlk4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab936b32ca.mp4?token=gcBJKvTKeMdpiaRmXqv_4oyzWy2NZk1oV81ATwQKg_9D-TQjzWB5oxjeq4-8iOrAW5iNFiMAIVPhY-D_CoAZGpvjIrAayIisfRcMWmhzUyEOBewv2rCwaNX2bt_KFXZdT1ybxd4IxnG7qBNzB_rC1HGZq8Fl60TBhDhhzV95c41P1Ag_pcsZs9jWshMGiunAhJk1JhGfAe2on-wI3gv8y-Rb5gvFP9mtO3cbOaQ7kkRqeVdl3EFDVS_tbNyJhiRSFsJHeTBJu_f9-1A0rjjPGbM7fDt0Kf6YW9Skz4vCUl8bCA2BcMmp87zVHVZCEWoUhE2LxI1xOu68Xh-4CEcrYGJkG-HaYhd1I8Fqb0KGMO17XXbm05hu91_y5cLCvKmziNvbl-H2fMVWgqolnv-gcx6SEmWc24w51JYOQe-uqCyezJH65R5Jr1iobD45cxdPPwk669lmTr70pIB_-Qpmh9z56H6wMkLh5552qq0eaQyHSRdn1wXrkLIQaZky2kLPjappqWpmgXtGiDl4nGwfZJ5CSHNc979N2J3DQx5uj-dcSs7ItQhjzdRAfBGgpfOvlb4a5qt77U0-RqwvCTZleu7Hr9CHMBq4DdsPNOQwu8Lxdchd4KmUSNjJIO2omvWPqYbH3-Twcar1iKzwx1yluPkk2knhdshaXm_jfwatlk4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در سومین سالگرد طوفان‌الاقصی، مردم در اجتماعات شبانه پرچم فلسطین را برافراشتند
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466898" target="_blank">📅 20:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466897">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osnh4enfMdArBYIcZhbDqmNnz2tKzgu_L3TAHz6rVk26TubpEd5r5koWjBA6H5kRZz22U9USfft2wfBcr3h4ZtBdEQEMtTOr9qNbNXueWRdoqXpwNL-AO_fZ7Y8Z70CcTDpAHLH1I6Ndi8e8I8DwxJFnl0ap2F8ibzS01nSEfje3D0MUuGQzEBKZYz0JKWsW7lqlVjlxnDOWEkAGPnl9wvmd45iLvNNZTrgbEzcnLN-yykXuhxQ8akhat77CD_o38EkmzfUjisEFvuEI7KAk0RbCTlAeaWDCQIwiAm2eLo_GYJOkUYR3ZwkvJrFhuPABEkNeG_zi_nArJK_2P8tbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از مجسمۀ ترامپ به نام «طاعون نارنجی» در پارلمان اروپا
🔹
در یکی از گذرگاه‌های پرتردد داخل پارلمان اروپا، سیاستمداران اکنون با مجسمۀ‌ برهنه‌ای از ترامپ مواجه می‌شوند که با لایه‌ای نازک از ورق طلا پوشانده شده است.
🔹
این مجسمۀ مِسی که با عنوان «پادشاه بی‌عدالتی» نیز شناخته می‌شود، رئیس‌جمهور آمریکا را درحالی به تصویر می‌کشد که بر شانه‌های مردی کوچک و نحیف سوار شده، در حالی که در دستانش یک چوب گلف بلند و یک ترازوی عدالت قرار گرفته است.
🔹
در متن حک‌شده بر پایه مجسمه آمده است: «من بر پشت مردی نشسته‌ام. او زیر بار سنگین من در حال فرو رفتن است. هر کاری برای کمک به او انجام خواهم داد؛ جز پایین آمدن از پشتش.»
🔹
این اثر هنری که طاعون نارنجی نام دارد، در مقر رسمی پارلمان اروپا در استراسبورگ فرانسه نصب شده است؛ ینس گالشیوت سازندۀ این مجسمه گفته: ترامپ در حال نابود کردن تمام چیزهایی است که من به آن‌ها اعتقاد دارم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466897" target="_blank">📅 20:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466896">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۴.pdf</div>
  <div class="tg-doc-extra">2.5 MB</div>
</div>
<a href="https://t.me/farsna/466896" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۴۳.pdf</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/466896" target="_blank">📅 20:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466891">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czUMn6ksr54wK3-ARpY9AudyxL28HdHqP3lrQlJzJ6lx4RF8i2Fon5uckyafrLgCTSsTIy6gIvFNUaw2QlGCy5tvKfeKLFeYYedvAKBNpKVQ2RPf8VO2uDgkokLDrt_CEVBJdc6BZ5G5tbtlTJSN6xH30lenowU9Bb1DIsi9rytCp01ZgqER_T3Dbn-Q8tbLy-UIbtyDdHf8Y5QhscqmJex0ioiSFdVIhsPUK9vCz9ZLVSAMTCwNJY5z4S4Fm-a0rhteBLQJ2NKgLqgvNZetx6vVAKvNB5asV1E9sEhChjCqVypRE-whQwNPllfu2JA1n_gOJOfN0oJbM9AymOjNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bro_bNjyXhVo07nGkiHtEdrUx_0y14NujAkJqtqAWx6aFbGZqo5LG7UEB0La_Se7hj10rN6UnCB04-C7E3vuKBIJ_4lXOkzKSGTB3pc7AzaNTJeabLvdo3xCf5RxTpE9BxoxOJgMahdBysrROWA4pLJC4YS1qxB909W_5epqbcR_7AQIkX5rqqMXVZq-sxbIqXLL-b2UkM1HMyHra0aOY5s57YVItN5moNVJo7KJV5LDfeH1Gjicg4my-X_LQrWpDkOZrBNMmqrOqJq5WkWTH5i2Bj0p61lRtiYRcFRM1KtVbM9nbxmRJBFEziiCrvVa263qb9SzIzkHTHoH_WsQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_sWCtrOQdR1GF3jN9_wEZBbWa3QDCT0Jt6MwM1jCTY9Hyhg_2-BfQGpdPLNkYRNxdULvEiAZCdst612WHkTr684qJ_xQA3i3fJjVvEZgfmxw2OJlSi-uRrguSW5EF8lWsZG4o-CjbqtPvLm3fiT-fl7LnF-N5LarSeeDzH72uaHFRXbIiOG4CyJEUczQASnBE6wa6EYXZg5dyrW1KFRXeGmpz4l38Ujqqr0pOecn3E_g9rMKPVuL_WOLPp0el_ppGhzXlwXSV2_dz_eFBECbIA_ySwy9J_5AfHibXo-qp6Af6xjOBvwxnASxLTcBcNzHchT8j8mtqP0cDWetvWFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZkXwdsqyTbGxwC5qzrvi59qLlJeZwudQYhf3ob5ioSu2QJ14y6DsxqwIhEgivvtR1wxrMqraK80iSRFSZEVXfmmH-OXcYY9jbqVtsQxySFvgkt8V8KJVviCUzZkMozBNr626s3VllX3xth1SI_HJDqMawdu_JYHz-EZCamCm5ZsSI-0kd4DrL12cbbDltXoIUpBreUHuAxj7RhgHBhD4g29WtfmHyEPQVckqHIS1g3VNYEvsvNa1BlHk6sRRcjbsUAbOcvO-IkoB2KFZsFy9HGz4oLNfHfAnyDyD0UPCklHWfotbRPyn1SU4TmxzkL0ez8FW52qSz18wW-pf4ZOrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujqguPG8yr4nhQ2iF6DdIqPe-69rh211jZQqDD6y5P4xcmIru4QsBhvWW2PiFE8uufl82K5Q3CplQEJ9pMdYYnG8uwADVb-doRrQQ7-8Zi6Di8gio2mq757nueu1XssoqMQqQS2MeyT0v-sNG9ezwCpqxc8VdYx2xlSs51nLp8Sem3--bwSA6tPlNDNU6ZfZWuM8eGoJJOCHuK1C7QQRq1S58NgLsL1j0kxNCUh0kQtTOFstjRb9FeB4w44a9jVqHuT75dN7bUwhOrN5k-S-ogrEdpyrcjc3tH-lOmH2eSGsaeb98snDrC6AT7kO-WqajzPQqeNbqHjjltSe6qbXkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار اعضای دفتر حفظ و نشر آثار رهبر شهید انقلاب با خانواده سرلشکر شهید رضاییان
🔹
اعضای دفتر حفظ‌ونشر آثار رهبر شهید انقلاب، همراه با سردار حسین اشتری، مشاور رئیس ستاد کل نیروهای مسلح، با حضور در منزل سرلشکر شهید غلامرضا رضاییان، رئیس پیشین سازمان اطلاعات فراجا، ضمن ادای احترام به مقام شامخ این شهید والامقام، با خانوادۀ ایشان دیدار و گفت‌وگو کردند.
🔸
سرلشکر شهید غلامرضا رضاییان، در ۹ اسفند ۱۴۰۴، در جلسۀ شورای‌عالی دفاع و درپی حمله و جنایت صهیونی-آمریکایی به بیت رهبر شهید انقلاب، به فیض شهادت نائل آمد.
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/466891" target="_blank">📅 20:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466890">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e2c4a0c4.mp4?token=GxGUJRwYJ6pV-iBASlMyWVza12oEdoS32iNSNjXmte3IrdT8xJTwsk8V3ktIa54AzmZn9etlEsk1c3uiHHNkznVlKXXxppuzz7sIBvRvWURbukjJj84TCH4QbiLblOKPBgr8QZLUdcUG6TVqGKlmQ9lejTVK2yH8Y-7ktLxdjBL4-YiNCBS2uj0hW45jS81GMFum3FiLFy6QZEwNCz5fyymWLLDIU4yqH8cYHS5rrmazYTNz0GAyENr5j1vLp7dtpfdglcYWMOojyNNB8MGxWHPSRy-8DlwxY9plPsvJ_rj6503_1TDk-Xab4Wh04oH4MdzmHepa2HuSUYYVqi0AIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e2c4a0c4.mp4?token=GxGUJRwYJ6pV-iBASlMyWVza12oEdoS32iNSNjXmte3IrdT8xJTwsk8V3ktIa54AzmZn9etlEsk1c3uiHHNkznVlKXXxppuzz7sIBvRvWURbukjJj84TCH4QbiLblOKPBgr8QZLUdcUG6TVqGKlmQ9lejTVK2yH8Y-7ktLxdjBL4-YiNCBS2uj0hW45jS81GMFum3FiLFy6QZEwNCz5fyymWLLDIU4yqH8cYHS5rrmazYTNz0GAyENr5j1vLp7dtpfdglcYWMOojyNNB8MGxWHPSRy-8DlwxY9plPsvJ_rj6503_1TDk-Xab4Wh04oH4MdzmHepa2HuSUYYVqi0AIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانگ حماسی جان‌فدایان چهارمحال‌وبختیاری، دشمن را به لرزه انداخت
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/466890" target="_blank">📅 20:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466889">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امارات استفاده کشتی‌های ایرانی از بنادر خود را ممنوع کرد
🔹
ادارهٔ دریانوردی وزارت انرژی و زیرساخت امارات اعلام کرد که ۴۷۲ شناور حق استفاده از خدمات بندری امارات را ندارند.
🔹
بررسی‌ها نشان می‌دهد بخش عمده این شناورها مرتبط با ایران هستند یا از مسیر ایران برای عبور از تنگۀ هرمز استفاده کرده‌اند.
🔸
قراردادن پایگاه‌ در اختیار آمریکا و حتی حملۀ مستقیم به خاک ایران در جنگ اخیر، راه‌اندازی ناوگان نفتکش‌های شاتل برای تضعیف اهرم تنگهٔ هرمز، ادعای اشغال جزایر سه‌گانه توسط ایران در سازمان ملل، دیدار‌های مکرر با نخست‌وزیر رژیم صهیونیستی فهرست بلندبالا از اقدامات دولت امارات در ماه‌های اخیر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/466889" target="_blank">📅 20:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466888">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da12bc4ba.mp4?token=JBbPLz8KpqTDaQksiIKcszf_wbRVM82xGDph8SSE4zZZuGBcYiWn6OSZz3qgXqm43z5jcZZheded2S-QrwUCdvmU9YMG3E37-zZ7LrMudPFFXBJJz79v34s_3sTzCXrUse49kiANQehlJBDKX-S2jUmQAPWZB1DVJCW813fzdBQGKIeir2TVg6yz_YVRgBSMydR7tciOFirgOJPKKYibZDxuMOU3zhqv1nKcEX9ZbDmnZJaolMX_q4IXs9Hx9g42V9cLqzSXNqFSHV6F0XSCCbaGRLT8jXHPaIfaVIZ89dQtTRa-ndCG4ISQSJDykAcZyz_Um7zYUrhelR1f9bGYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da12bc4ba.mp4?token=JBbPLz8KpqTDaQksiIKcszf_wbRVM82xGDph8SSE4zZZuGBcYiWn6OSZz3qgXqm43z5jcZZheded2S-QrwUCdvmU9YMG3E37-zZ7LrMudPFFXBJJz79v34s_3sTzCXrUse49kiANQehlJBDKX-S2jUmQAPWZB1DVJCW813fzdBQGKIeir2TVg6yz_YVRgBSMydR7tciOFirgOJPKKYibZDxuMOU3zhqv1nKcEX9ZbDmnZJaolMX_q4IXs9Hx9g42V9cLqzSXNqFSHV6F0XSCCbaGRLT8jXHPaIfaVIZ89dQtTRa-ndCG4ISQSJDykAcZyz_Um7zYUrhelR1f9bGYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از تندیس شمس تبریزی در خوی
🔹
در سفر وزیر گردشگری به آذربایجان‌غربی سازۀ جدید مقبرۀ شمس تبریزی افتتاح و از تندیس این شاعر نامور ایرانی رونمایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/466888" target="_blank">📅 20:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466887">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cc8074b1.mp4?token=RU5csO7YMuNW66U-2_RYBUtS_RnHWALGvYSzaZ-NU5-z30JiBh9dof8aNzefeNS9vgYGvM2X77f4M60ATImpWrF7RfUXnHhmQzd2JY9jkICv6kQE3cE3nik7bSQb0Ff2TyMZmKkCx9wCmZLymQMg8MVNr8ExL2P39C8n8wrMKWpvU067ALVpLFhCLKV20ebYNci3gBfKwR6Ubtq9WAGO9wXLEm5uLHb-s3scqXnnUbiiRkE5M5fn0XaU1TfesMs0Y-akNtSGiJ_BC2EOQacYJqKN5R3iJRNZT7LH0IDWziqTxWZSm4_6XNiJp8zYfFwAlYmh_0n_fZvujGEBPsyoCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cc8074b1.mp4?token=RU5csO7YMuNW66U-2_RYBUtS_RnHWALGvYSzaZ-NU5-z30JiBh9dof8aNzefeNS9vgYGvM2X77f4M60ATImpWrF7RfUXnHhmQzd2JY9jkICv6kQE3cE3nik7bSQb0Ff2TyMZmKkCx9wCmZLymQMg8MVNr8ExL2P39C8n8wrMKWpvU067ALVpLFhCLKV20ebYNci3gBfKwR6Ubtq9WAGO9wXLEm5uLHb-s3scqXnnUbiiRkE5M5fn0XaU1TfesMs0Y-akNtSGiJ_BC2EOQacYJqKN5R3iJRNZT7LH0IDWziqTxWZSm4_6XNiJp8zYfFwAlYmh_0n_fZvujGEBPsyoCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای دریاچهٔ گازوئیل در جاده آبادان-اهواز چه قرار بود؟
🔹
انتشار تصاویری از تجمع حجم زیادی گازوئیل در جاده آبادان-اهواز و شکل‌گیری ترافیک، در روزهای گذشته در فضای مجازی خبرساز شد.
🖼
اما ماجرا چه بود؟
مدیر شرکت خطوط لوله و مخابرات نفت منطقه خوزستان اعلام کرد که این حادثه شامگاه سه‌شنبه ۱۴ مهر به‌دلیل ایجاد انشعاب غیرمجاز توسط سارقان مواد نفتی رخ داده است.
🔹
عملیات ایمن‌سازی، مهار نشت، ترمیم خط و پاکسازی کامل محل در کوتاه‌ترین زمان ممکن انجام گرفت و در حال حاضر این خط لوله در مدار بهره‌برداری قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/466887" target="_blank">📅 20:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466886">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRCP62M594kJgBxRbkObyrnhO8DAaZs0Axe8jqItVzzvpkviwj-gRAhEaWEjOZxsEnXmBViXU9Q_hUVvSXOhRBe_co1ArIbwwrtaGZoglifT1RXcooI-U-8noBBubmnAdJUDQfshJKDvIECHg0EkPg3QRmIrljGJ3TzRRKsPoZ-XlvlOq0aVeO5TXBWWXfefVhf5PLoIr4h9MiseTZK_CAvcI0HfBK1SMEzdylveuazadt1YwGewlLZZWuMCt4C2FSMdS25g8Yn36l_1-BqhIk2930ELI81JJZDoiaCPI9xLxKkFmE1K1IvHhQZ3GaZk32j2Vn45o7sECe50Ojl1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلای دبی پروازها به تل‌آویو را تا اطلاع ثانوی متوقف کرد
🔹
فلای‌دبی که روزانه ۱۰ پرواز رفت‌وبرگشت بین دبی و تل‌آویو داشت، به‌دنبال حادثه پرواز جنجالی چهارشنبه گذشته پروازهایش را تا اطلاع ثانوی تعلیق کرد.
🔸
روز چهارشنبه ۳۰ سپتامبر، هواپیمای فلای‌دبی از دبی به…</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/466886" target="_blank">📅 20:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466885">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
رهبر انصارالله:  سعودی زیر چتر آمریکا قرار دارد و تحت پوشش آمریکا به یمن حمله می‌کند. خواسته اصلی سعودی نیز ورود مستقیم و همه‌جانبه آمریکا به این جنگ بوده است. @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/466885" target="_blank">📅 20:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466884">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎥
بانوان شهرکردی جان‌فدای ایران شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/466884" target="_blank">📅 20:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466883">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601ed69b31.mp4?token=ATblpaQUToRgWVKAPjT5BrvqtLI5hWo1URq0IkjVP_ZltWBZ_Mbf7uEUT8Atthh1pGWdX8G6L0m8U6S7pn9vlAf7XTZm7SCWOkwPOX7vQej8r5Lxj-8uWgVecZxZQb4kgm20GFZJ0JV65rqpnnWbGXVRz0tzOfRLIEfSAEgS12kI9FvX3a0H3W4pFtIO-tVa-nPNZxyyLaQp34prm10GnlDn1X4qjYX68d3rUPUeaNn8ftWpvXgnGms52ts-mJL_GYj8GCosnMWVYRPu5-u5cBf8zAAhhxECODjoagtDIL7xH1KZDhkh9Knzf6hyBnJJxPOKRV3XEVu5sub2y6rCEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601ed69b31.mp4?token=ATblpaQUToRgWVKAPjT5BrvqtLI5hWo1URq0IkjVP_ZltWBZ_Mbf7uEUT8Atthh1pGWdX8G6L0m8U6S7pn9vlAf7XTZm7SCWOkwPOX7vQej8r5Lxj-8uWgVecZxZQb4kgm20GFZJ0JV65rqpnnWbGXVRz0tzOfRLIEfSAEgS12kI9FvX3a0H3W4pFtIO-tVa-nPNZxyyLaQp34prm10GnlDn1X4qjYX68d3rUPUeaNn8ftWpvXgnGms52ts-mJL_GYj8GCosnMWVYRPu5-u5cBf8zAAhhxECODjoagtDIL7xH1KZDhkh9Knzf6hyBnJJxPOKRV3XEVu5sub2y6rCEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بقائی: عملیات‌های پرچم دروغین جنایت‌های آمریکا و اسرائیل را نمی‌پوشاند
🔹
سخنگوی وزارت خارجه با انتشار ویدئویی درباره تاریخچه عملیات‌های پرچم دروغین آمریکا و رژیم صهیونیستی در ۷ دهۀ گذشته نوشت: پرچم‌ دروغین، شگردی دیرینه‌ است: اول صحنه‌سازی کن، سپس انگشت اتهام را به سمت دیگری دراز کن، و در آخر از نتایجش بهره‌مند شو.
🔹
در وضعیتی که افکار عمومی آمریکا و جهان از جنگ غیرقانونی و تجاوزکارانه علیه ایران به ستوه آمده‌اند و متجاوزان هیچ راهی برای توجیه تجاوز نظامی خود ندارند، آنها مانند کسی که در حال غرق‌شدن است برای نجات خود به هر تخته‌پاره‌ای از جنس دروغ آویزان می‌شوند.
🔹
بقائی پیش ازاین با اشاره به اتهام‌زنی‌ها به ایران در ماجراهای پایگاه فرفرود انگلیس و پرواز فلای‌دبی به گفته بود: گویا رژیم صهیونیستی و مدافعانش در اروپا و آمریکا به دنبال این هستند که هم موضوع فلسطین و غزه را به حاشیه برانند و هم تجاوز نظامی آمریکا و رژیم صهیونیستی علیه ایران را و این‌گونه القا کنند که گویا تهدید جدیدی از جانب ایران متوجه منطقه یا جامعه جهانی است.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/466883" target="_blank">📅 20:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466882">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bilv1Z69WG5qpyeqgBc0edgQPELv0ydoeCOXNMF4perP2CUyvWj2gnUiTz2Xdug-5SNnQSgsyvhy_kS9hSHHdikz-JCyQ8M91JMh5D1iDUG_mQ4qD0gABYAI7jGFM7KOAV3h9LqArpFmGtK8HI3uMDeRDzt6NX224owDY_U5k7QbsDgMaQFrDB4Qj5R67BrrdEgPktPx3X7vijDU6Ho0xjW2kfVW1VnfFw6etcm1ExnLUonNjZGuc3EEbPphxfA3VTvD4jaAlwvoiLQJNNN4KQ3KlbOUK1vJJbU7NiYwJg4GQ0TB70RvBRhEyLNahC7wovV2Vgo_3lwj2Ss3R9EUxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار تهران: اولین محمولۀ متروباس‌های ۲۶ متری با عبور از محاصره وارد ایران شد
🔹
زاکانی: امروز ثابت کردیم محاصرۀ آمریکایی ناتوان‌تر از آن است که بتواند جلوی ارادۀ ایرانی‌ها بايستد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/466882" target="_blank">📅 19:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466881">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162720c36d.mp4?token=CtL4uj8ZYUH6twMprgvdgvbdyHFn9K-EezibKQZ0VyMG_qmnPLMcM850tN7tWy5sbOi3kvZSLZ1EHWyasFLQTnwYIttvIOzqKEEr1o5mlwbZf5VsrMKR62tpYz1pLjdTZCYpHYu2Z0oaL25en1lbL7PkROmmank8YfrC8lepHEa4d1gwOKQXTo5VwxSn671RsjPaNx9PZOEMK4tsNxt2Q40xBFUAgCLWh9H4jvwqAa3QWUDITIa_-KSso9M-HJhGLwQCeIBRJamt8l09iM6n4bTTYyXQUm62TJHJ743S9eCX0Zf7y55iWcrxk_g59dapwqg6BNICOWeIlh4QTjIhPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162720c36d.mp4?token=CtL4uj8ZYUH6twMprgvdgvbdyHFn9K-EezibKQZ0VyMG_qmnPLMcM850tN7tWy5sbOi3kvZSLZ1EHWyasFLQTnwYIttvIOzqKEEr1o5mlwbZf5VsrMKR62tpYz1pLjdTZCYpHYu2Z0oaL25en1lbL7PkROmmank8YfrC8lepHEa4d1gwOKQXTo5VwxSn671RsjPaNx9PZOEMK4tsNxt2Q40xBFUAgCLWh9H4jvwqAa3QWUDITIa_-KSso9M-HJhGLwQCeIBRJamt8l09iM6n4bTTYyXQUm62TJHJ743S9eCX0Zf7y55iWcrxk_g59dapwqg6BNICOWeIlh4QTjIhPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اکتشافات نوین، مطالبه‌ای برای شناسایی دقیق‌تر منابع شد
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/466881" target="_blank">📅 19:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466880">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKEJ7Ehh2oAhrWBRXQsPyn26iYNK-7aPqbn-sDcY6XmmTTkH2PTT4vJdw-3EYorXd0QkWM3qoUmtyPeemTqPo0vze0aqaI3SG18Jb-xE2kHV8d5znfPB703xBHnPkMPJMQ4_GgSM1HLLZHniIfTBetSRvgNSXrFUage0Kh0I9_u6yg6uasFOSAuLsyGjZzStE6vwJ6xP6Ks2e8gXuTSeZNhNcL1W_vjZd7fTlHZOE3cw1PGHevktjsA1m2JMZiYxhkR2EXCHwrbMQw-4VFrusae6TKoIwrLkWdPrHKExpVV-LDiZKYmdqYEBP57pH5x8nlt4Q043NAs0YR8vgXZj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد نفتکش‌زنی در تنگهٔ هرمز شکست
🔹
رویترز: طبق اعلام منابع رصد حوادث دریایی، تنها در یک هفته اخیر ۱۳ نفتکش در تنگهٔ هرمز هدف حمله قرار گرفته و ۷ نفتکش هم پس از هشدار از ادامه تردد در هرمز منصرف شده‌اند.
🔹
قیمت نفت امروز از ۱۰۲ دلار گذشت و پیش‌بینی بانک‌های بین‌المللی افزایش شدید قیمت نفت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466880" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466879">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌ احضار سفیر فرانسه به وزارت خارجه ایران
🔹
در پی برخورد خشونت‌آمیز دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گستردۀ حقوق بشر، امروز سفیر فرانسه در تهران به وزارت امور خارجه احضار شد.
🔸
اداره کل حقوق بشر وزارت امور خارجه با یادآوری تعهدات…</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/466879" target="_blank">📅 19:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466878">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94c87c2307.mp4?token=W_MK_ea4ZF-GHZ7njL87rQ3ltMN1tV_ZJEojLe8ZI1B1xljF1MzA6eMC2z8qG0THOG2eWGG8H9TAvgXmMiLntsOJag871XDU5coQ4T1L_W-SKfYrvi1b3gQWMtvLWpeNhU1i9kd0gdYDhTxiq2h3cS1P3J5KKnD9ox8mQ3yHPTW9zp6axdoDc2peMrfzJurumnm8MUvFIQGTPRlR02FZxB9R-Yod5dH4gT6-SlWPqjfDzVmhGT3nK85nUGlZTimh9peJ3lk9d4e7NkBa4A0XuJAa7cezQof8CheZ1xyxymoEn0kJvq12FqCMkt8TjFyYmSwvVPO3_iiv1Ohr2ag1yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94c87c2307.mp4?token=W_MK_ea4ZF-GHZ7njL87rQ3ltMN1tV_ZJEojLe8ZI1B1xljF1MzA6eMC2z8qG0THOG2eWGG8H9TAvgXmMiLntsOJag871XDU5coQ4T1L_W-SKfYrvi1b3gQWMtvLWpeNhU1i9kd0gdYDhTxiq2h3cS1P3J5KKnD9ox8mQ3yHPTW9zp6axdoDc2peMrfzJurumnm8MUvFIQGTPRlR02FZxB9R-Yod5dH4gT6-SlWPqjfDzVmhGT3nK85nUGlZTimh9peJ3lk9d4e7NkBa4A0XuJAa7cezQof8CheZ1xyxymoEn0kJvq12FqCMkt8TjFyYmSwvVPO3_iiv1Ohr2ag1yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز آمار: سرشماری غیرحضوری نفوس و مسکن از ۲۵ مهرماه آغاز می‌شود
🔹
۳ گروه هدف ما خواهند بود که برای آن‌ها پیامک ارسال خواهد شد. پیامک‌ها حتماً با سرشماره مشخص ارسال می‌شود و لینکی نخواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/466878" target="_blank">📅 19:25 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
