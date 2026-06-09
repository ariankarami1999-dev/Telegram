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
<img src="https://cdn4.telesco.pe/file/DM5pz3A82iLdrLYW9uqHyvZx1Bvg9J_nxzj7ktlOlOaN_wds7n-IJYpYAGGF9SIxk5MTk091Zk2nMoSmMNXPyXca6b1r54uqUFR6ySg8Pa3JLvAhPD2WiONubsJg4Zs5PuzSv5cJEIcqGYhBPpGj2sALuQkuqstLV22SotiWJso34WGcl-G0VjSxsPqzq5KFeG1IQg2hK-Qik3pNLmFj_EHtPK9P4b5jwvqSfVK_REaWInwIFkVWgtj9uPyA2YzqBIC7MmoIizzH5LT8WEUhci5I8p-mRP-EteN40VaaW8PREqBhXld_rZRJaPTdypHN1XF4TOO432G3uRnuZgGu5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 19:46:14</div>
<hr>

<div class="tg-post" id="msg-440964">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njXbd-qOd32DZp_1UvOMT0JvkqEs4_7vs0aHHcAaZGKRAiD__tmISPqONFBsYah0wtzvXMkex5y54CtYCtOejjmzNa83bmiCeySFQn9Ajj5QapKfHQfDtHX-Kpr33TiKhrtK77g2WRKzJZFHhGkRvFgcPTYHyAfTjkw3x3q43Y-NJvum8OSX80Z2_MoatcupVbXq8yxjgk8Ek2uKyZB4FNElw4j5Pj36WQ07l7EhqArIMdkwZnqE1W1ogLi-uq5d9HIFx3xXfLkKd8eZ9KJjvSRqLQliA_oN18Kkfcx5QDzChXCFE1wGPkpx8FXuSLqPCSZOI6P-9oarMxa9-9Gadg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSJOlR5YqPMrKWKFe9y7AXvTJK_4PH-Aq_ykHBwc2kmkjXwUTR6FLJwMCnumcjuN5hpmxewMgPZv6GvQ-n-eZUz_nvyf5tzI342psph7TvuyVmsxu9fXUyuIN9yLOW_eVhtQgxikMGD-7H3M7WOArdqR8BmXKP0gL382TqVPH9rxlPQHFxrtHXsWnkMoYlq407hCiQF8bDNkIlqyRsUtbi-GGe0mqiOMGrfqIn4Ru_EsneRY1-r7vXdwES1f5sgVAfGyu-Gewhc8gvVpLCxMrc2_mkEPZllolY0JLoQaBnF1JpXHbLPz1EqgHK2LCyOt72KLTKcOTPoIMEZr_nmW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PS4aBWmOjzGOF_8-VllK6uRhgq7PDtQU-gb6gWv2co7k9EnSfhwH41DuOP5UyUTqYX8yWLMvrXnLMMrzAM3ub0CcIGIxZBSeRY6fzZUA_ZgHfSg5nt3yEzjSovTHnK-HocbAEw8e0XQucjmnDZB15gsDDy4IWEEv-CiMI8A74QXZuOXIRrrvW2uX3VvaxZZ8CCyobtv56Fhrnm4KGEP0FdefDNTOu93bKcrp4B92rHMcbUm5tUyunnp1kIGgc1SlpPUfU3UWmYlmZLEAp5qkG1lr9B6Xda1cfr_gfOIxJoZUGIhKyqvYGZkzVIC_LerAwW0r0H80RKnIdV1JWiWgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWxuyc38t2ZLl7uxQMifIExPEO2HHstI1Y2mkSy7MM801eKrSS6GMqkM7akF0ppF3NmaAM6UAXvJY9qF_rskGia7r9ar6UP0tF7i5lFJFl6dvGZ-X08sYvvqopDqePsGn-yCTGnSQvXjYP6HNPQWNQlViUHqe9xaiiiefYzeKKZVEKvzJ-lZPJZEH7x1XZpZtezOUAbBitw7CEkcxh99neS0B3o3VgtMaGCMeRCdRFKXPaMpdczPJUkovsPJYnFcM4qCSJR_PMjU-nqcn-ySOeCUZ0Nc1SLZ9gGMaLZnzE5RYSv5vkX5Rrwy99LAsHQFMfQDV2JsSU3Ni-DJ9TbHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjpRt4TANZIQIS3p62dHLs_4VUc0DJrNCuRZEMJ_1adoI16PAHIFVLYgjh0doMF4tM-lCTFF0_N_d5k3WpB3lzefUfLfe3kg86gaykJNeMuMeR8UFuKwW7pMhgXgxM0S9WIsAZGNFSEA1RlUShhictjZsoftvjtfU5ewRCUMj2Ihn3E1EaDMfxfntPYHHhQ9haiyE_DLdCat7ew4t5cSbF2IGZ_4cyrsFXnyFnBoqf_mh2kp-7zBBSOIQ04HCAN-MhVLYZYn29HyuN53-VH3n_3GIsAQkqtRQCXJIHaGaqcKVoV_jM9R_l7H3bT2QU5tITCgIKldQJdznu_2n4MiBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtgmxXv6X8vVsSDlhjVUJTj1dfFW509vGPvUOCoOYqjNV2USPvHPAXmKKHuaNZYLSGe-fj6_m2HoRQ-fntrLpbxPKPTHy7mwhRoCkZvb_5IAd7_fXgudhDnHPbwajnhF2thnHotkTAIVgCJn_CMcu7sT2ajZ3V7EtYEhVvuokAYgHbk3DshO9-bOs79vApJfxfsZrLByLv91_sy2egUFPT9gR1c4rKAOmgTWpu_gDoEp11G1qFHfgCO4tzXOMCrEail20TVBxS84xCz5WIgHPSWj051laojnew7D5TOTmHyuoAFwp6u9-PvYnW4Z0W0Fg24eiWVMOIIwDI8QRg9lWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKJHDUk_TRJHoNtbZpM30-i30fTOrDETuUiQYQSyomaIz2-fM22bNK4xJS4Bx0yPHsMMOu-l5YhaCzl28fNHk5su_SgrHOrNsY1-lXqrH_ICfcb2_Rl1XX2h5izfFSFb3uITt6J_Kz44TkqH8US5LwSVFv7rMeyDfFV4fn3ygBRs-Ee6v4qG1to3t8pBEdgh3yQ-1kkZP30pVsI7gF2caV830AVQPASv9bIOQKqWhnJU77GX-ULg6wV7fjmg7ZMJ3z6OkqeikLLcT3JPVDKmRHD7jRAGUBXmR_rpD1JTmKY2E2K7R8FS87RqYmEhMtxpv0wffgYSneJH5zOdma9oHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازگشت حاجی‌های اصفهانی به فرودگاه شهید بهشتی
عکس:
حمیدرضا نیکومرام
@Farsna</div>
<div class="tg-footer">👁️ 42 · <a href="https://t.me/farsna/440964" target="_blank">📅 19:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440963">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev7hUyYTuR-dLDP4PSpsl6G77Bg9_8RVasMOgWPi__Td1CSYUfz-e5JH8EfcPluV2UEDWXXfBVFDFQZeMsil4VNOtg3YrPy-KyHv74TdB1w5frEqyfWP76DjLAex0bmQU5-yCB4qn_RqyHBJdrNU-8lCB5sBlf-yC0RoF2Lb3W6hU2OpGKod8SQmK3jll4hUKPMhdzQzjK6lM9rZsqD502q5NxMoCkhKxNi2PMbm3mH_6VSbIcYOUuAwvhP7r0wydchYeoMy2SU_WkaTOWWmFNXD2xNwTgfZCtAF_d57lsyPNLKS2V-6PkhRxu0NTlqYV41e-GnF2WYve-K_0QXAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریشان‌گویی‌های ترامپ درباره تقویم توافق با ایران ادامه دارد
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا همچنان در حال ارائه جدول‌های زمانی جدید در خصوص احتمال دستیابی به توافق با ایران است.
🔹
او در جدیدترین اظهارنظر امروز سه‌شنبه مدعی شده که توافق با ایران می‌تواند ظرف «دو تا سه روز» حاصل شود.
🔹
این نخستین بار نیست که دولت ترامپ وعده توافق قریب‌الوقوع با ایران را داده است. از زمانی که وزیر خارجه او مارکو روبیو گفت که مذاکره برای رسیدن به توافق با ایران «چند روز زمان می‌برد» الان چند هفته گذشته است.
🔹
شبکه خبری سی‌ان‌ان امروز گزارش داد ترامپ طی دو ماه گذشته دست‌کم ۳۷ بار ادعاهایی درباره نزدیک بودن توافق با ایران مطرح کرده است.
🔹
این رسانه در تحلیلی به رفتار ترامپ به چند دلیل اشاره کرده که از جمله نوشته او ممکن است این‌طور فکر کند که تکرار مداوم این گزاره آن را سرانجام به واقعیت تبدیل خواهد کرد.
🔹
با این حال، برخی از تحلیلگران هم معتقدند که ایجاد برداشت‌های عمومی درباره نزدیک بودن طرف‌ها به توافق بخشی از راهبرد دونالد ترامپ برای کنترل بازارهای مالی است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 371 · <a href="https://t.me/farsna/440963" target="_blank">📅 19:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440962">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a76fa83f43.mp4?token=uuBv6Ft_c_LHy1fMmVUw-UBhEvdNKWTeIpabL5UnoQLVCM4CaearnX2-soDn49rJzhMhv9tVZ6l2oRY9OAf1XzKi5JRBhINlIaZXkgWyAUZAAj43R3-7DfgyUoYEKNTEdvJXv45IgGn6nU9l8GOv_vJXVFRR8O07iXb5m98JViBjmNALfotTS059HAvtnrigQt2fsV7YgIoP6R2fsgYw4zByGOKPHF15Ce2n-svVRbRRbEgloEi5czvOT9i8nOa8YDG8-KQ4-JzWWcAiqH-ax98gfZF4BIBMUa8GoUc59e8rRhfGz12rT5rKo25CezAxoyngwjzh2fez_DtnfLJHVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a76fa83f43.mp4?token=uuBv6Ft_c_LHy1fMmVUw-UBhEvdNKWTeIpabL5UnoQLVCM4CaearnX2-soDn49rJzhMhv9tVZ6l2oRY9OAf1XzKi5JRBhINlIaZXkgWyAUZAAj43R3-7DfgyUoYEKNTEdvJXv45IgGn6nU9l8GOv_vJXVFRR8O07iXb5m98JViBjmNALfotTS059HAvtnrigQt2fsV7YgIoP6R2fsgYw4zByGOKPHF15Ce2n-svVRbRRbEgloEi5czvOT9i8nOa8YDG8-KQ4-JzWWcAiqH-ax98gfZF4BIBMUa8GoUc59e8rRhfGz12rT5rKo25CezAxoyngwjzh2fez_DtnfLJHVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا در ۳۰ ثانیه ۷۲۰ هزار ترکش بر سر مردم لامرد ریخت!  @Farsna</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/farsna/440962" target="_blank">📅 19:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440961">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo2SZJWSMeUphcXEgNFUCInmC2lppO24k4DEdfVK652EdkWdLbpg6_LqHE96azhKkQTUnbMLSpjmvYiKGjGnxa8yxj6JpdCdj57AfhtTRm3tTO279piQ-wNeBWDZ4hSihWKHu4IZmuLcsaZbzJVKcJcnOhxMWtUD3jtaUgcK3ZHRCqLacoYWKUNcRnaiyAddIU92Fham9pl0XY0fFkxT7yb5SZFQIRdZnZ-ViktWtn_hnLRDqASpnrrquAgmHwk15FD9hp2TQT3UEu7GsJJ7zozC59_j4lnEf-twpjo_aWSJL1vAmWuMxLR55o_o8Dem5oo9gKQye8wcDU0KftDHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین از دل دریا اورانیوم استخراج کرد
🔹
چین اعلام کرد با دستیابی به فناوری استخراج اورانیوم از آب دریا، موفق شده چندین کیلوگرم اورانیوم را از محیط‌های واقعی دریایی استخراج کند؛ دستاوردی که می‌تواند مسیر تجاری‌سازی این فناوری را هموار کند.
🔹
برآوردها نشان می‌دهد حدود ۴.۵ میلیارد تن اورانیوم در اقیانوس‌های جهان وجود دارد؛ رقمی که بیش از هزار برابر ذخایر شناخته‌شدۀ اورانیوم در خشکی‌هاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/farsna/440961" target="_blank">📅 19:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440960">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی زرهی ارتش رژیم صهیونیستی در نبطیه هدف اصابت قطعی پهپاد انتحاری ابابیل قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/farsna/440960" target="_blank">📅 19:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440959">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92c29ad0a.mp4?token=heSleToB_czZ4MKaD5W8ejJZPWa5M1nXvkydQt0Nre8wx2Yit26WaUH84SfVVyMeuBRotNacTuvBHGSUwTzLC7J9dAkjTHunnjofW_5lsxWhh04-VlCCHnx0vh3toVsU17auwQqZGpPLiAckjRJRscPTPkeW4raoPfaELYZJPE4MPG-5Jz-Pnmc6s7HtHHxy1sAdLZLMNMP2YOMagmxBjHYtesBVALwnILakQfmmunmFtvWExSmuAhcQ2dUAHRiYcQmrqX69BmpTwzuRnYsz6aXXDBUs0r15h243K2xiYMEbUGxLeEZK7TyT1O5GOuP4Qv4X-b9YNdRMfhf6n4z_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92c29ad0a.mp4?token=heSleToB_czZ4MKaD5W8ejJZPWa5M1nXvkydQt0Nre8wx2Yit26WaUH84SfVVyMeuBRotNacTuvBHGSUwTzLC7J9dAkjTHunnjofW_5lsxWhh04-VlCCHnx0vh3toVsU17auwQqZGpPLiAckjRJRscPTPkeW4raoPfaELYZJPE4MPG-5Jz-Pnmc6s7HtHHxy1sAdLZLMNMP2YOMagmxBjHYtesBVALwnILakQfmmunmFtvWExSmuAhcQ2dUAHRiYcQmrqX69BmpTwzuRnYsz6aXXDBUs0r15h243K2xiYMEbUGxLeEZK7TyT1O5GOuP4Qv4X-b9YNdRMfhf6n4z_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر جدید دوربین مداربستۀ بیمارستان لامِرد در ساعت حمله به این شهر  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/440959" target="_blank">📅 19:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440958">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎥
تشییع دو شهید نیروی پدافند هوایی ارتش در تهران
🔸
«سید بهمن حسینی» و «علیرضا عبیری» از نیروهای پدافند ارتش، در جریان حملۀ روز گذشتۀ رژیم صهیونیستی و در حین ماموریت به شهادت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/farsna/440958" target="_blank">📅 19:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440957">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEQKc1vRef6zraeaDpFIfpSNWyP7Gmtg30RTGvxtjmiYAw1ueKQVlqRmr1ZGNhPQbswS4mm1CKKiENTArSJM5dilqMD80UjLMVDlWzplLF57iT2ubsd4tnj1BbmGZ725CPgAOJIRubB_jyu1CuSbJn599X_mu7xN2sSFn8maEU417uVgl1_BBUTGQZmSAFt1c87jzZICjb6UbQvzA-tBl-7UA90XZxv2I-pSEvApc8Bmn3zY8J_0Esc-Mrx9I-e7oNy-JIcFxFSq7Uxrd5gPYgbpEsXPyVB5uxH62_GOJpNhDoKM0-2Msbm9urHkWzxkoT3COwBSG8tC9s5YpC8mRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهار شد، قاتل دریاچۀ ارومیه برگشت
🔹
همه در آسمان‌ها به دنبال راه‌حل‌های خشکی دریاچۀ ارومیه هستند، اما به‌گفته مدیر روابط‌عمومی جهاد کشاورزی آذربایجان‌غربی، چغندر روی زمین سالانه معادل ۷/۴ درصد آب دریاچه را قورت می‌دهد؛ یعنی اگر آذربایجانی‌ها فقط ۱۳ سال از…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/440957" target="_blank">📅 19:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440956">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdDOhDJP2tJ95Jxo-ZpVEO7xLOfGDRIF6vNWrhZY9vlqeEHBLiyL-jb_LjsRwU61EX2W35YBir8cANKU353gUeX9yjd-Apg2ty7yFnwaXoxoXB6j0HuR_DAWs8hv337QdNnUEw2-F9pZ7tQKDAX0v0QrBO-V7s2AcKFMZ1dmWGk2fCz7sDbSS4-6w6asVFLl5AsDLS40s7woBNFMk7JmlpD7-4We_ZXrEP3DBZvO94H7KM0eKcl_T1Umk7VrxNSh1L9JtsMKpgqPUTHrNGOrVwALo294K1w9hCybPBAeM1b3GdItW54HdbVEko0ycfnHRZx0AvXGT8AifS5UKhc9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۴ درجه‌ای دما در تهران تا پایان هفته
🔹
اداره هواشناسی تهران: از فردا تا جمعه وزش باد شدید همراه با گردوخاک در بخش‌هایی از استان مورد انتظار است، همچنین دمای پایتخت تا آخر هفته به ۳۷ درجه سانتی‌گراد خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/440956" target="_blank">📅 18:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440955">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNK1UUFXUWuRLumWX8gXMMj0GS3ahyO0wZJgCdlMG1wfYbEZbkVO5p3bJF8Y-XA8AinQ0xdtAFLEFP7hmZS0sNzy32v5izYRzshl_cKxqG4qsbI7pzHm9mY_1YOXjVhYawasx844Te__vPCWwAHhCloYz9LTVHy5SXBUL7sjjuueNQgYE7tukIIi1cbYfTKXqNcqFYk99fwZZAl4wCVyk4NcOEU4wXOY4roDdO7UN_8DIJ8UFEOkan3Kx6wZO9kNnkp-EnqhUGY7ydcHDde0X2s-XamTnVKlhDWI_j_k0GBQW__uDx3nmH9PnU67ku4hQF-aa5S55lSk71q2fQJNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت یک صهیونیست با ادعای جاسوسی برای ایران
🔹
رعنان اوهانا، ۴۴ ساله، نام فردی است که  توسط نیروهای امنیتی اسرائیل با ادعای جاسوسی برای ایران بازداشت شده است.
🔹
رژیم صهیونیستی مدعی شده که این فرد در چندین مأموریت به عکس‌برداری از مناطق حساس پرداخته و مبالغی را نیز دریافت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/440955" target="_blank">📅 18:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440954">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjSZcNVwfkFzQoSKVJXhFzc2DzZ1sVO5f5nBjMAUs9ARqx3WqS9HR16_tfQCpUMgzS9cnef78wrylMn-S_b9JvLhs8v3yzqD-oZsIwl7lyaCw9WuHKu3sIr4eV6nATa_Azgmwe7V3-u8MdwVp8AfSJKa12E9B46bzMVIchKaslrXFV01-6_mJoiq51metrXeSmsIjyyIRReQ2lWFfDyGOYeQ3rOAUCrqY2Tzf890UkKnWDb_LGZifuv2-V95bcNj1MMUWmbn1sRSXTOTY-WvoMp6gbAMa43X696NPFarCypOQzeuhaFjI4qWyPPXodMCgjr51qVlLx5DXFgkmuENBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یکی از کارکنان شهرداری تهران
🔹
سخنگوی شهرداری تهران: در صدمین روز از مقاومت تاریخی مردم ایران، امید بختیاری، یکی از کارکنان شهرداری در حمله دشمن به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/440954" target="_blank">📅 18:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440953">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">قوه‌قضائیه: خبر احضار چند سینماگر به دادسرا صحت ندارد
🔹
از ابتدای سال ۱۴۰۵ هیچ سینماگری در رابطه با حوادث دی به مرجع قضایی احضار نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/440953" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440952">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/286eeda6c1.mp4?token=IpLzBfzOoLF4-x_qPqlHzAOkd_3H7X7P2HvsL1S9N70RLV10OM-6kIMWA8uTs-_ORLfJuaMyozQmgiqW_zGM7cxlLEypDe6D52_eR9unp8e5bHfQVcU0x-FX2bVkdQw9cQ52kZVricsqZ2KnNKE7vjFTNPI6Yxsmvwp3ueXVw6CW1xPJ0j4P1C247d0SwFqshPUf6bpybwQuJJIygBKjkRHeJLIui_78H5b1P29q4NBHaR7GTxeNm3mwSrR_UJojnIjGKXVBHgDiwqJ11H3ZysXe7AgQwZrui0qWd5f9IVnDP7h8CWpNcdj9NOXpRsp6LKHv0mOoGV-n9rbgfMWysT2hw3mEw0Mn-2ldLLpJGo3oMrlL4brekg1pth6QmZE3iKudJfZ5-KC3EiLZ0Jf-SbYIP4bqO-ic-fw79JAM5hzVqz-iUi47SQDocdCrXGwNbaNUXQjxI6BRyayqeE_Ktp37FuDI9rz0rcYVYtqc0S7Tc6d2_onVJyiwDGs5odIVYxb0eC1Nt3X-RBXHY9aJl7cMqRnYoVKzztwUTEwY12_UZwNTPqefsmNybtnw_3d6Q5W__ZMMDS_RSd-ShyGXmdydeRlAFwQXiwdf2BXAuNqR80YfSTEXsn_b5RsAXRFoBFx3b6i5Txy73Dve5RHOjJRnXpQ8ld6joSTUWUvKzco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/286eeda6c1.mp4?token=IpLzBfzOoLF4-x_qPqlHzAOkd_3H7X7P2HvsL1S9N70RLV10OM-6kIMWA8uTs-_ORLfJuaMyozQmgiqW_zGM7cxlLEypDe6D52_eR9unp8e5bHfQVcU0x-FX2bVkdQw9cQ52kZVricsqZ2KnNKE7vjFTNPI6Yxsmvwp3ueXVw6CW1xPJ0j4P1C247d0SwFqshPUf6bpybwQuJJIygBKjkRHeJLIui_78H5b1P29q4NBHaR7GTxeNm3mwSrR_UJojnIjGKXVBHgDiwqJ11H3ZysXe7AgQwZrui0qWd5f9IVnDP7h8CWpNcdj9NOXpRsp6LKHv0mOoGV-n9rbgfMWysT2hw3mEw0Mn-2ldLLpJGo3oMrlL4brekg1pth6QmZE3iKudJfZ5-KC3EiLZ0Jf-SbYIP4bqO-ic-fw79JAM5hzVqz-iUi47SQDocdCrXGwNbaNUXQjxI6BRyayqeE_Ktp37FuDI9rz0rcYVYtqc0S7Tc6d2_onVJyiwDGs5odIVYxb0eC1Nt3X-RBXHY9aJl7cMqRnYoVKzztwUTEwY12_UZwNTPqefsmNybtnw_3d6Q5W__ZMMDS_RSd-ShyGXmdydeRlAFwQXiwdf2BXAuNqR80YfSTEXsn_b5RsAXRFoBFx3b6i5Txy73Dve5RHOjJRnXpQ8ld6joSTUWUvKzco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نذور موشکی شاهرود به خط مقدم رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/440952" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440951">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj7SvMqedkKbYYGP7C_A5V6zrziCp81HkM8dtCXpfE6rTV_abKC2HnL8P8Wrar2vBuZWSukCBreFKDZqDwHxND3-vDyRSszbcZ2Y_0tVLoJqphgdPma8lgBISmY-3rKY-c0Y6k3JWQURwjKcBZts534TOutrWhYPHd_FZRxBcq5937SeCu5WUSjxOWEPzwqJ19g3F6JoMCNSW-MTmYMqy0DWGPykh7EWpwWLsOjcU_IWU4yNS5BBHQ52HaIpTPqFHr58a1Y_kWfiZWBSErYwikfNxyhm6d8V_HbRYsEa7dN973qLaAFMfZxKIb4qo3ehbu_j4p8q5Ckb1umTVGOBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ با عصبانیت مصاحبه با خبرنگار آمریکایی را ترک کرد
🔹
ترامپ در اواسط مذاکره با خبرنگار رسانه آمریکایی ان‌بی‌سی، پس از سوالات این خبرنگار، با عصبانیت جلسه را ترک کرد‌.
🔹
ترامپ در حین ترک مصاحبه خطاب به خبرنگار گفت: تو یا فاسد هستی یا احمق، رسانه شما هم…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/440951" target="_blank">📅 18:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440950">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIHDI61IG3U3773DVSnsnp7AjL-C3K829ExQuESjZBENQGq6TfOH41rmsbB-uA-m4ApuqSmz7uid28Dd5jx9wCF7X5ukBadNlvcj8z8NsnBSE44NX97ERfYwN4jT72xQZRDJIJWF2rDA9HPjEl3h9vL7MCMXbwsbBwGSCBaNeclqvclCPAgoci142yS5PjricGShtNwe-KpO49bOHdgQouRupp6nIyTY2S7FSTqZTMSogElu98R-ZcfX9vkxkx91GmDm04fQwd7UuppninZGGKf41JLJDHZrDoLwiWaVXl3WBW9o4rLGr5AiLqPYYoYAfAj5QYQfl1_I8T6ihln8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط حماس برای آغاز اجرای مرحلۀ دوم توافق غزه
🔹
سخنگوی جنبش حماس: گذار به مرحلۀ دوم توافق آتش‌بس، منوط به توانایی میانجی‌ها، کشورهای ضامن و «شورای صلح» است که بتوانند اسرائیل را به توقف نقض توافق و پذیرش این توافقات ملزم کنند.
@Fsrana</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/440950" target="_blank">📅 18:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440949">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjQ8vnQs16q-4oFAF63J-TmlNm32bYt8zrT8xzQrkMZHRDz9r-L6vIOmZ8vXGApSSDbvicXp7x1Ns_TM1loU81r15gJR28QZQyy0mZnR98miDAKnKe8cIYLI6q6CNxXnA2TNeQ-xlI76I-iblGh5mcUKxUfgsc8wM__sdlLqD9WlE4udnZdd108TWo38sh4TLK4BxY5_V27qoQGkkqC5bozQA73PjVxhKtycDN-CpJij7uVf8vmUZg2PvVWL1TvRIVgh5NVRxn4OyrOUWJ9JUPkVJpPTIgx8iZ7D2Jj-QphHPMOTJtqRZ7aZcq9zSO-AwNliSnEm5Xka4C8tti1eRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه ورود بن گویر به خاکش را ممنوع کرد
🔹
وزیر امور خارجه فرانسه: به همتای ایتالیایی خود می‌پیوندم و از اتحادیهٔ اروپا می‌خواهم بن گویر را تحریم کند؛ وزیر امنیت داخلی اسرائیل از ورود به خاک ما منع شده است. @Farsna</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/440949" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440948">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwzd3wZL7Z5jkkmIoZbhNqE8qd1E9VnIeKX6VZnxZk6p7CukNFoAS8eG41HaskJxntoStAn0LEpMaX8w8AytWX0DJ1oVJ1iYa8Slay9sYO9Jkd128ICrizfPndQkUVIcjIvEpLPw-ZH-go7obwUOyu9snrVkHi4L_lFQ7jKVU7p0J0_lcg1DL-ohrXceHVUuT3ZkJK4T8UlSiUueJfql3uyegczadncAGJFhyMSgoIuY0Dt1jGwqAwj-nbUPVy6WH4d9-vfPMMakMYo6jfzuYOk9gdL58YrqfAAWTweVOW3y80N6u00jxOFuYsLyVbUHM_XvNUrBDcW-m-WOn_IqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
چاپ ایران‌چک جدید ۱۰۰ هزار تومانی به یاد شهدای میناب
🔹
بانک مرکزی اعلام کرد سری جدید ایران‌چک‌های ۱۰۰ هزار تومانی با طرح یادمان شهدای مدرسۀ شجره‌طیبۀ میناب چاپ و به‌تدریج وارد شبکۀ بانکی کشور خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/440948" target="_blank">📅 17:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440947">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bahQgSCcbWhtzVodxz4wJqXm-4KICk5U7sQ4Ln4mZa1CYsCrARXJlO9vyru3AcKZ-CHX4G9HAcM26i43BrHHi5WIz2ofa-f9Yka9P2CAZSFhzsxNjwnoC_tsxBtRWwdDlSI59pGQFKM3XEOSGDjqGfgZJauu-awzlUie4jhHq0Mkos_iLeI8OEn6PZYzEkgQjI6PZcs86odNhuu2cEwoXnyLbIYyhEUdPHGJpY3ruYHHcFDjpMfc3KT_8ywtEbhnF7cPvdGwmyf0oAacnhCM_IyayW_FVRjIvh5m-LC8G9xCZIO94lgqJHioCChpqWfw6V_qUCyJ7vQa6j0knAJGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوجهٔ ارزان‌ به مرغداران تحویل می‌شود
🔹
کارگروه امنیت غذایی و تنظیم بازار کالاهای کشاورزی امروز تصویب کرد جوجهٔ یک‌روزه در «سامانهٔ بازارگاه وزارت جهاد کشاورزی» به قیمت مناسب به مرغداران فروخته شود.
🔹
بر اساس این مصوبه، یک‌سوم از جوجه یک‌روزه تولیدی کشور به قیمت مناسب در بازارگاه عرضه می‌شود و به تدریج تمام جوجه‌ها از طریق این سامانه، مستقیم و بدون دخالت واسطه‌ها، توزیع خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/440947" target="_blank">📅 17:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440942">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvE9U04TiRm8RD6pBhIY6RSbYrxUGQRpoxSWn1Xi8VMJVK6ApZNb1HME-mt4ENEfYrQi7wfzIHqskU4LP3kJ-_MWTJd60MXzpyHU7cWoFp6B7u7KB8-pW4bLdnQhgISik_esr8Q2mmEQ5zh1rucWi4Pj2UhNPdV2uncHWQLsnDpwQfnHVxgVwrn9kxg2VZsBwZ04O3Jk0jsQvi73KVRfZ4ggDwlXtol70bKq2QKhRUMTMc6C-O5ocjoKomnp-LMMhuka2z2Zm_nt8-4sh3RzXML9FnAb8lB0MNLShjL8x3lirIcymTC0sPQ_GpiA4Wo1Oq7tM_6uj6yk6ORSQU-ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5zE86hK8gPp5nygi0Q0PlUV57FRVAJg5z0-MT_-8BC3B9nu-Uda7jyDemvgemz72TD_OgwEwBfkm_K3ut3MYWhMs0pZAekimXfD592ruB9COaptzmGcNkj9n3QPVslya5H1FmjcsMqluiwdq6M5cvicswYrEamOdamKU0o1np_DLQXqqcwETzOz_PgVMTGtqJ55jE8B0L8Iua2jr7rCBEfj29nfMS75KUKHtBftZDBLln_uxnvnwU-TrnP5MJeqQtiC_vMziNX4-Zz293JaVN_L75VYc1l7kTzSNO-iaW1iwtiI023N18mcpzIwNYTK879fnBKinhi5SOu0bkXWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcqjBuvgB5j9kpV8ztXJ-Xi6ANTABXczXBiGALopx6Zq99ySXcbwH9rq-4-ndHKb2HAIrjARR6j1RBrYPOfRZQRHiIXAx6T1qYpkVBRMUQD0phG0bzcrnrJp0k-f6vj0x67JsTxCWXFgpoQlm6dNslDACUvhr1teLj5YZpSG2SHC0ixm7sw2R0nqtiOZJufdbW56Xjxp-TuTC-aSzjD8UAaO60Qh1Twq981EgHpZ6YxYu6YeXMOGWdA5zYBrQsUR6_7JzzZrK6JVoNM1iw4oEjTBrxg_dFtQs2qxXfv6l-1EDhm0g4NlStTxjcsHxZDso-DGcMo7NSCAhWogQnvatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gdhya6DsOlikkimdbyWT31uoqK98A-bdU9K-E10nGc0395ANKbk0tXG39Tk06G5_sfmukfxeYTKG4tspAjDBUf8nH_i5b6PD9t2SxWEvPIDbDKSoi-2XFYdOno_96w-Zd8b82Y1b_WRygdfuFzhrIL6FSSnFOSTLReDzdKlRSBr3OZ_DNkK6Tr5aPJQKNz-1PH2UFYnN7dLUgGfPtc6hMv0H--CQbKT1GWwvBBxTZ5z7hpXP5SCcIGUg2wLnLr5WXsz90oqtYLhf4UuX928eZ58F45KZLUg0GtyY1zigUhe8qsO8F3nWXZrg1qnBUkE946VkRwVvaDSEruoLTHIPFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DhY_vzodow9pPkWCudlZxkvrvG_Vme1hzvwNpyvLksGRVyhyTXcYD_bG-JxoJGrDaLWk8QUWSLPiDz-sLQDUP61MADuaShGhJgBAKxveWlMwnrEltY_hkRXAhFVR7BSK2IVs3ou1yFAjUbcBVuAqJBplZ8f04L1-Gm3FUvHuDkpYt1KoUfhi2lmRXsbJG9PvNHhsLEz4b1WaaP3MWSPBntIJg2Gk_Epxv9gn8QDQ5SfnCV41p1Xq88Sx_QfySWzsIuvq18aLwpgJ3K7lQbWCNSOAQXSwCdaPL1yzPQ6Wdl2xbi1Dd9sQ6wsCwuBWE_BTvUN3AJQ0acuf8xBxO06rEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رها‌سازی پرندگان شکاری در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/440942" target="_blank">📅 17:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440941">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTBPDM6FrmeTzk5EZu9MtSEDkxW03dpHjeljUk_CJbd6jq5047DhXrqUmB2gICjARb4u_MI7kfNkK1bsU6VQgyeBmanrj3QH1pBkSKfTG2d0T-bxOJL4_Qaefc9Rym-LqALgR_WbGRJ39pCgh0dwZtcpqmGuTNh218NbEWBIiGoHTYyUi0Ai121RIG2uF60N3O-aE76WNt-hSJAeYUqrKoAIKVhuIWtFlgfAtZBdXB3K2YUyCGPoQtCc3K018nVW2aQil1qv7oCeE8gggwtZH7mPa-27D8Jm0p1XOIY63Odc9Xhlv33SW5XyG7HklJnn0uR2omeP2K7uql4urdj5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف خطاب به مردم: درود خدا بر شما که کشور را از دهان گرگ‌ها بیرون کشیدید
🔹
صد روز از جهاد ملتی که برای حفظ ایرانِ جان قیام کرد می‌گذرد.
🔹
درود خدا بر شما که پشت ایران را گرم کردید، دشمن را ناامید ساختید و کشور را از دهان گرگ‌های درّنده‌ای که برای تسلیم کردن ایران اسلامی دندان تیز کرده بودند، بیرون کشیدید.
🔹
پاینده ایران و زنده باد مقاومت ملت بزرگ ایران
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/440941" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440940">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhw_WF7YFYYcguapXZykdi4i72scQkY_DQ28E2IXOkW5lEsHM529IS3kLi2-AOdZ54OH7w_-zXiYCvCbGix8aTWikYJ6d3e9ZUiRs6hqUlUozCvIUGkA2w7-vM5Lb7LP3cnGo30Z6hGJo3BFOxP1WduBK3mVQNwXrDqvbj0xD8rBZZbjI0gKnYXT2QdNfZzHTNVa6aZloApXgZ1bOhWWV7f_c7stQ8Hh9bRhdeTYsNwliNTf07l0d7H8k7fqaA2YPft4NMr0sWj5dVN3nXemuGjcuSOzPsgST2a83pWEp1-hF03diyzcqLTH3mihq6hQg2KKykopNjplSliWOJzrGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ یک میلیونی دیگر کفاف نمی‌دهد
🔹
دی ماه سال گذشته در زمان حذف افزایش قیمت کالاهای متاثر از ارز ترجیحی محرز بود و دولت جهت پوشش افزایش هزینه‌های خانواده کالابرگ در نظر گرفت.
🔹
خبرگزاری فارس در تاریخ ۱۶ دی ماه سال گذشته
با توجه به نرخ کالاها در ۱۶ دی یعنی پس از افزایش ناشی از حذف ارز ترجیحی محاسبه کرد که کالابرگ یک میلیون تومانی افزایش هزینه‌های خانواده را به صورت کامل پوشش می‌دهد.
🔹
این گزارش واکنش‌های بسیاری داشت و مردم معتقد بودند، همزمان با تورم مبلغ کالابرگ ثابت کفاف افزایش هزینه‌ها را نخواهد داد.
🔹
اما سخنگوی دولت اعلام کرد، خرداد ماه سال ۱۴۰۵، مبلغ کالابرگ متناسب با تورم افزایش خواهد یافت.
🔹
در خردادماه قیمت‌ سبد کالای ۱۱ گانه افزایش جدی پیدا کرده، به نحوی که میزان افزایش قیمت کالا در ۱۹ خرداد ۱۴۰۵ نسبت به قیمت‌ها در قبل از حذف ارز ترجیحی برای هر نفر ماهانه ۳ میلیون تومان است. عددی که در ۱۶ دی ماه تنها ۱ میلیون تومان بود.
🔹
به عبارت دیگر دولت برای عمل به قول خود یعنی پوشش افزایش هزینه‌های ارز ترجیحی باید رقم کالابرگ را ۲ میلیون تومان افزایش دهد و به ۳ میلیون تومان برسد.
@Farseconomy</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/440940" target="_blank">📅 17:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440939">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi5Of2vP2jKJ8Pu1xCljy0h4L2_T3qEAM7cX7vHmBb4prOhF8hc_f50tr5_kbZP4g6kDKpOQLlkaiMCvEolrZjY6VY3DZfOTkFPNoZJn_2n72hm1pCsQRekBFalWlhNDYouC201Nyti8uwKNzaOnEmRCEtoEIpuNZr5hUApQRXrcnfln7btBPZ6IzISwj6H6UKcecuorWil4swaOJDhwxc54vclUy1kws1_8FMPpfrEQ8_V9JeoS3_HWa2YYgR_ngxrC9g28lE4wwdAo8e81CVPnqCvFUlZKsbiy2ENyIGHyCs29hSEJqxaaKkZ_wzj__6eVEUdaLMfvONuIKx-9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۴۲ درصدی هزینه‌های طرح ترافیک و خدمات شهری
🔹
رئیس کمیسیون حمل‌ونقل شورای شهر تهران: طبق مصوبۀ دولت، کلیه هزینه‌های عوارض یا بهای خدمات، متناسب با نرخ تورم اعلامی یعنی ۴۲ درصد افزایش می‌یابد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/440939" target="_blank">📅 16:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440938">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696cefc457.mp4?token=P2W7217aGBdfJUYstHO7A6PdXU_BbUSFYFEbYkIJB3zbuvoEIWhHj3jV58LPY6njd5U22PbBHyj_1NuxPWVfgMaY9te-ihS6dXdoirWwcH5m_nyASS0AQJdlGtzzjpWt1zKlPPi-HqNsO6m3BdbDU7cKkbDagYZgIMoaMv5kGmBJwR_NCXw2U3b8e4lyvuqYt9dCU1wr7JYpZkw6J9hbB0-lgKAXTyvPoGpRKfZvt9FZFXzSj4Z24yIugV7DCPYlZvI748_wRfYBEhMmOui6-gwFXfR_GS-SqQ4PbsKZ_6eyjo2J7GYfd0FMmT5tLhXXsaNqztVb-CMV9oLx7EKmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696cefc457.mp4?token=P2W7217aGBdfJUYstHO7A6PdXU_BbUSFYFEbYkIJB3zbuvoEIWhHj3jV58LPY6njd5U22PbBHyj_1NuxPWVfgMaY9te-ihS6dXdoirWwcH5m_nyASS0AQJdlGtzzjpWt1zKlPPi-HqNsO6m3BdbDU7cKkbDagYZgIMoaMv5kGmBJwR_NCXw2U3b8e4lyvuqYt9dCU1wr7JYpZkw6J9hbB0-lgKAXTyvPoGpRKfZvt9FZFXzSj4Z24yIugV7DCPYlZvI748_wRfYBEhMmOui6-gwFXfR_GS-SqQ4PbsKZ_6eyjo2J7GYfd0FMmT5tLhXXsaNqztVb-CMV9oLx7EKmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتتاح راه‌آهن ۱۷۳ کیلومتری اردبیل-میانه
🔹
پزشکیان: ۴۳ کیلومتر از راه‌آهن اردبیل-میانه که روند ساخت آن به دلیل بروز بحران‌ها، جنگ‌ و تحریم‌های ظالمانه بیش از ۲۰ سال به طول انجامیده، در دولت چهاردهم اجرا شد.
🔹
امروز پیام ما به کل دنیا این است که در تمام بحران‌ها، ایران ما در مسیر پیشرفت و توسعه قرار دارد و با همراهی مدیران و مردم بر تمام مشکلات فائق خواهیم آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/440938" target="_blank">📅 16:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440937">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrBDV1EcWn_OdmRR-aqE2RgsoxCrbVh1I65qhAx4-4X7pOWnlRLb5tRb85xStJYRdE6qPehXmNnODhogK0fcsXzQ7kN8DYL9UrOmE-RZCwWx0HuTC-Lo6S90smToNGkaBX94cBwoH0q3WBh2OfXjMXFbhHgkmWty1QvBIzbMIKqELC5OTxzXJlyOVCAQuXGdTVzUQhIS5c638AGamukqcWv-jlnjsYnFDcIf_bDmo40xa0S_R6ae_6DjZ5e8tIbPAXLUgUid-t2R9ZwNWQj_oqo6Q0HqVOiy2B3G2Uv4VqRp7nENvFBrRGQHnbj2LJhBgGyO9b0xbjZ-mmmi-T4vzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ دیوان عدالت اداری دستور توقف مصوبهٔ ایجاد ستاد فضای مجازی را صادر کرد
🔹
دیوان عدالت اداری اعلام کرد: در پی طرح شکایاتی دربارهٔ ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» هیئت تخصصی صنایع و بازرگانی دیوان عدالت اداری با احراز ضرورت و فوریت…</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/440937" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440936">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUgj8sd4WOK2pJtEQnVF8zU-_jKZcid9U10QVDBik17T0CHPCmd2H-cPqIGE8ZR1nSxvfCEFPC2qES8SEXnAmx0wigq3-VxYdocNcEtRLwZ4UPUK6Bpm_kKTkuaSHaARgDBgEGSEeBcJIFhy8poXyOlmOyie7Q_32kAHEwv1M9X6cAaWoafwkGpckq08ScGBmDdsOjGCX0bfksod8ENQvTfKQEYdeafVm1vbSACxAABcu4NQfY4bkHk4XlHmYybYs70PwdtdWwCdZekWkbKi-JKcMecmyCKNjaDmucjmblIbRRyRt9aCRTEgJeMKtlPRIglFkMAmedV6RYTM4sqm1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با تصمیم شورای معین شورای‌عالی انقلاب فرهنگی، تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد
🔹
همچنین شورای معین با کاهش تعداد دروس امتحانات نهایی پایۀ یازدهم به ۶ درس برای کنکور ۱۴۰۶ موافقت کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farsna/440936" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440935">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌
🔴
ارتش صهیونیستی: یک نیروی حزب‌الله از مرز عبور و به‌سمت نیروهای ما شلیک کرد.  @Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/440935" target="_blank">📅 16:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440934">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی زرهی ارتش رژیم صهیونیستی در نبطیه هدف اصابت قطعی پهپاد انتحاری ابابیل قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/440934" target="_blank">📅 16:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440933">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2_f0ZhBDor0uq0hNA88gNlXtEHqkBF5NZNKrNjrzMxqWTDtBhj9pwl17iVbe_Z7xE6SOa5etcu8GCXyC1h7dvVm7HKgbw8HoXSoqjbfcTKrIcW-oTfQ44pM4lnsZDl0fkirlwIBxm6c7tVtzbJk91socKE26XG4I2nT-RERD8x_ANSW7Qrcl1a6hTl1vLV0CG2sEq48HD8ZyiL8eU3PN9ppnxBJ0ZpNtXBTQ6FVr2ybM882BqtoXROHgAmUvYA7_Uqoyl5HyOnbK8ANXIEwjUHQMi9LvTcOyT8g5Drl1kDO7LYJ2oFl9w1SnFe-x0YKCmbydrgTBoVX3vbrtYnTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلی ۱۲ پاسگاه محیط‌بانی سمنان به دلیل کمبود نیرو
🔹
مدیرکل حفاظت محیط‌زیست استان سمنان: ۱۲ پاسگاه محیط‌بانی به دلیل کمبود نیرو تعطیل شده و معاونت محیط انسانی تنها با پنج نفر فعالیت می‌کند.
🔸
استان سمنان با دارا بودن ۱۸ درصد مناطق تحت مدیریت کشور، زیستگاه ۸ گونه از گرازهای وحشی خاورمیانه، آخرین بازمانده‌های یوزپلنگ آسیایی و تمام نشخوارکنندگان وحشی ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/440933" target="_blank">📅 16:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa48ff6f2f.mp4?token=Ke-kPrdj4FgmEmwcjJgCt65c97G7PzwZJCLjVrF3dSo3iJ2rhRSPl6j6YPXvfKzH7n4VW73eeUrkNJm9Tq3BTcTVOE-zLnoUvnv6_AtIusq0Zx9stirCObaG2Pp1NKV7vgJfJsADJ2ZnKOQZgYzPgdqeIeFWGRyZ9MOoqfNsEBGGHuBhV_Rui6dzNLHArLAHIO7NKa0SxJtED6SNUEKEnsMFadOQhMM2yU-BYg8kJTxRBuKacnpa68UlYm_HN_lD3dNh-SPzGRDcfdgLxdcaDIDFXKBy-TvINc9pM1oETknEgVA37VOMz6PS1DcNL5JO00n_H51_qo2zFjozJqSfSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa48ff6f2f.mp4?token=Ke-kPrdj4FgmEmwcjJgCt65c97G7PzwZJCLjVrF3dSo3iJ2rhRSPl6j6YPXvfKzH7n4VW73eeUrkNJm9Tq3BTcTVOE-zLnoUvnv6_AtIusq0Zx9stirCObaG2Pp1NKV7vgJfJsADJ2ZnKOQZgYzPgdqeIeFWGRyZ9MOoqfNsEBGGHuBhV_Rui6dzNLHArLAHIO7NKa0SxJtED6SNUEKEnsMFadOQhMM2yU-BYg8kJTxRBuKacnpa68UlYm_HN_lD3dNh-SPzGRDcfdgLxdcaDIDFXKBy-TvINc9pM1oETknEgVA37VOMz6PS1DcNL5JO00n_H51_qo2zFjozJqSfSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی حزب اصلاح‌طلبِ ندای ایرانیان: ایستادگی نیروهای مسلح در ماجرای لبنان هوشمندانه بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/440932" target="_blank">📅 16:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
حادثهٔ امنیتی در شمال سرزمین‌های اشغالی باعث اعلام وضعیت اضطراری شد
🔹
رسانه‌های صهیونیستی: به‌دلیل حادثهٔ امنیتی مشکوک به نفوذ رزمنده‌های حزب‌الله، از شهرک‌نشینان مسکاف عام، مرگلیوت و مناره خواسته شده در خانه بمانند و جاده‌های این منطقه مسدود شده است. @Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/440931" target="_blank">📅 15:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
حادثهٔ امنیتی در شمال سرزمین‌های اشغالی باعث اعلام وضعیت اضطراری شد
🔹
رسانه‌های صهیونیستی: به‌دلیل حادثهٔ امنیتی مشکوک به نفوذ رزمنده‌های حزب‌الله، از شهرک‌نشینان مسکاف عام، مرگلیوت و مناره خواسته شده در خانه بمانند و جاده‌های این منطقه مسدود شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/440930" target="_blank">📅 15:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMD1duoh_NIBOCcNNaFUw4B2hwI2LZbSu0oK2U3SJbrY2lmHSss7bOGqTt9D-IPK9zreR-AeUaIByCijKYuYGGGiTgjkusV9FqNU1cDPxoaq-ja5i5XsBOzc1AOFuqaP2HMsp5va9rMZtExt0qztaEpEBMe7Kd28BYF2OJiZ4GoRkNAI1SADfkzzG-b-VolZO1wMLqwtXRTql0toooZVJfygnS5mVIYMfFe-VHkvt4B-aBLjiTGbn_vLa36ABRE3cb6MUfYPBWtDNS1EKCVJLYHSd2ioubQLE4Og989XB5_LYg5oufeAK8J1rYEunNC3A1gSzEs0wVDHq2zxrzu6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خطر خطای محاسباتی
برای
مسئولان
🔹
رهبر انقلاب: دشمن با شکست در میدان نظامی بر تا‌ب‌آوری مردم و ایجاد خطای محاسباتی مسئولان تمرکز دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/440929" target="_blank">📅 15:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440928">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI7YWaw2RLf-UbZZgCiuvTEOErCOMQfUAO63-XzLE8GR6SxU-N7g0BTqKoJFGogerdqS-8MlldWxrXUJHRjZWnu8V11ISvn_KJ89ARf8NSm2LZF60wXv6UOXGEkl8q2KmoA6LD4T389pWwGfHFhM4oGJU742lmqmVx1M3U9t5argOktriigOVUEVS6VRgM_P4NRboIGyaer99viT2kZGll1j0CibV1RAP6amj4sQVMRTWH86qCFiiXaS1yVyu3dik0mCaK_ZUGGo2XPPgGK5m8LqEsXBdZnzLuK2o7_Op9zNqW8Vdn-13zXb6OOtOu35jReCtJTkbsU6Xnc1z5OPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‎‌ آخرین وضعیت فرودگاه‌های کشور
🔹
روابط‌عمومی سازمان هواپیمایی ایران: تمام فرودگاه‌های غرب کشور تا اطلاع ثانوی بسته شده است.
🔹
درپی حملهٔ رژیم صهیونیستی در شب گذشته به فرودگاه‌های تهران، فرودگاه‌های مهرآباد و امام خمینی(ره) نیز بسته شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/440928" target="_blank">📅 15:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440926">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b876bc18.mp4?token=o23ZvfB3fjSznecnj4qXZSP2DkmPpNLmyHf7ATC_SgwBWTWmKPa2WNpJuU55OgfuaxzgVLQUpIkmi3p5RAHG6tzqacR4WqWjNkvV-F5Jvqyz1QXhicdDQb3inKuYw2bcOlgjqUFM30h5Gm6cA6QT0K7sAbd-zcok_00zAgRAQ-N_OvwRDsaycHiqlj7noPjirND_d9d0nms-f7ec13PirCd6tOhWFzmRQtgRVrrOiRT2W_LhVc4J1H564XkckWYyjYg7UrH823iZ1Rg6fWpPR9G5F3XLBVM_z4mBE5zE8N1FAmYdcBWAkrJPfesvES_o2pWyYXsjUAUx3MHrF4_mmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b876bc18.mp4?token=o23ZvfB3fjSznecnj4qXZSP2DkmPpNLmyHf7ATC_SgwBWTWmKPa2WNpJuU55OgfuaxzgVLQUpIkmi3p5RAHG6tzqacR4WqWjNkvV-F5Jvqyz1QXhicdDQb3inKuYw2bcOlgjqUFM30h5Gm6cA6QT0K7sAbd-zcok_00zAgRAQ-N_OvwRDsaycHiqlj7noPjirND_d9d0nms-f7ec13PirCd6tOhWFzmRQtgRVrrOiRT2W_LhVc4J1H564XkckWYyjYg7UrH823iZ1Rg6fWpPR9G5F3XLBVM_z4mBE5zE8N1FAmYdcBWAkrJPfesvES_o2pWyYXsjUAUx3MHrF4_mmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبض حیات وحش در جنگل‌های هیرکانی مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/440926" target="_blank">📅 15:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440925">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXOu--TaK2gK6QtqobY7zLyYgDFMD7j5Oxu85IezAFsdxu5k6U9vlsYyV8cMv9SSlJMPV8uoP8Up34_F3u-iKk0S85Vo1u2gflfd_1fxSP2fDSoQ1iKcAHrg5tr6hgkVYGotB6b4aAcuErda6c8pNis_bfpsagF1qk95F6TcOHgVE9Z7EnCzPCHz8sYwAGqvd3sSfgE9mwQ-sm50unbeBiLj6R7TvjyV7DXBHJJZgBO-3yaE80PdEjNazG9N05UNUS3GcBeI3ZGIHNpwo5rfGdbAhseGfALn5EB4M-AmzNTtebVOWEzHqhVI1BuL7WnE3f_zsoLsCNUP4EdAt07Lgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه به نخست‌وزیر آلبانی: برای درک و شعور مردم خودتان احترام قائل باشید
🔹
به‌تازگی نخست‌وزیر آلبانی، ایران را به تحریک اعتراضات مردمی در تیرانا علیه واگذاری بخشی از اراضی این کشور به جرد کوشنر، داماد ترامپ، متهم کرده است.
🔸
سخنگوی وزارت خارجه در پاسخ به نخست‌وزیر آلبانی گفت: بهتر است برای درک و شعور مردم خود, به‌عنوان یک ملت بافرهنگ و دارای تاریخ غنی، احترام قائل باشید. آنها آنقدر زیرک و فهیم هستند که راست را از ناراست تشخیص دهند.
🔸
اگر می‌خواهید حاکمیت ملی خود را بفروشید، به خودتان مربوط است. نیازی نیست به ما توضیح بدهید. اما وقتی با اعتراض و خشم افکار عمومی خودتان مواجه می‌شوید، از دیگران برای فرار از پاسخگویی خرج نکنید.
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/440925" target="_blank">📅 15:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440924">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhMn9U01fVmrNC7TmjxVYBmxNRhR0lVHz9uOUt2Df2hUXfppIiIk2ICFXafhPtMnlPRweWHaBkStQIXjan_mI9WPVcjTrhPS1lpDXT0WPtkWRZHf2GmomYvbvyGVb62h3ZbLCZNxi--Lz8P3fqnPKroxNKkkEo20-rOulKiI3yyqFnpa7zeH8Wl2q29Pfis8kuHhtX_laA6L4NNn5IfhYGwbA2IZJQvRBzcHkeZ87TUveU1zqaMhB6Ow8YnxP6XIjOJeSR2PGOmMhRjNCEe5NRVW3Gr_nmrFuW-EYWeT4qVSisVvM0MgvFk8EYAfUo3Xh7mXs0MJQLffzxowWabSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ارتباطات: توسعۀ فیبرنوری را با قدرت ادامه می‌دهیم‌
🔹
کار خوب دولت سیزدهم در توسعۀ فیبرنوری را با قدرت ادامه می‌دهیم‌ از برنامه عقب نیستیم.
🔹
یکی از اولویت‌های دولت چهاردهم توسعه فیبرنوری و نسل ۵ اینترنت همراه است و نگاه ما در این زمینه سیاسی نیست و به دنبال کار کارشناسی هستیم.
🔹
توسعۀ فیبرنوری و 5G به صورت توامان در دستورکار است. رشد ۴ برابری اتصال در کشور داشتیم و پوشش فیبرنوری از ۱۰ میلیون مشترک عبور کردیم و از برنامه عقب نیستیم، البته در کلانشهرهای تهران و اصفهان مشکل داریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/440924" target="_blank">📅 15:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440917">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZogFZ8B9gqQ2ahiTYBHmVNeeynSbC_63Idny_TzU8DtLKYdxpzWKai18sivpe35X3AZv3atFjQnISSjtOsNeX03hU3dEIj7N88R_2-_PRShheBk1t8IR9P9FHbRsgc5ykJdzinzQk26XpQpblpoX1ojF4UpJNPedPf4q2FSfVe6AAFlm1m32hJrmXOYn88qHN8ya5RPa8OEGzROSwB3qBEXJ2i-kxcR9z2O5lRah2s3L3aqcGm10C4rp-pIo_R8Nv-fEednFI9BeCI6YGfd17e945frdhLA81JW74oRZjJv6jX2eUIYi8imlH2fzbZRSmhbCP17UL4NiUfNqBaFjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAu-qSQtJ0MUrGFAHmHyw13hN-RRn5zGqbK0qlGq9MWPgQIK5DgF2m0EHbeN95v9jQv25eTAIf-ApZcS6wz6whX6ZrOgMZIRfGB2geFKxcGPkiwfl5Wo-JczegyQNg7IC0ok9uAJkPGznTj2MuzUEdbDIR6X4smPVu3jwNY46tg2zqAuGsMI8A5gbVp7aLOdTp_lVghvzCGyJbWECc_sGHgZkOw0wOwdYFSh5e-nVK38saLHgdOXG4HzfPmEc2-l2cVO6yQuvD7NKxElb2m957RJ4a0x3kSFWcX8uiMulwerL_YGfKSL08Rf_TSKyWlIzfsAZA_u4jmpmJ5OHP4xpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJy5ck1Ex8_KyayvhyDlhMvi9iGubgcz5A_kyhWwWd3Mu9mWz0gyvhBhGrzbb2-2w9B_ZrZ1-_FdM9MTruCAvqgbpLnGgz3O8j9WDG-t6qXwpRRA-m9s8lY96agH_41uvS8q3UDiJIGRSkF3BVUtsyIYoEc3gTSkv7nvUFmNuO4lQ5EE1KvRLHQxdxiE5m5uTU3XbKGFOrh2JYpI85UApClc1IdctjwFwvQHyBrXi31ianh4MzD9WPcDYAcRLjdCl91e2VqUzUV_AJMC-YMX_VbdtsamXSGqafxntfqVNxHDpieUSArwap05xjfiH0eFQWcmYEaFsO7i7qTp7XnrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dutwn6s1Xbm64InJ4rx9QARirOTGZFL0-XPpjc_sMt8sSEEAHlQkpFZ2j06eIlrUXKNJxu8d4bdKAdULj0p_O72XYEmlY0953dIawhUWDFw4FnK5M3AaSNZOezDZuOYh15VbKgf9so5C_UO_hlbE5L7VVEo6dqRAroJvB0ZTFcSwTcujIAzd6RPbNKdus_MhYaxtKaT633wY9zxmYGOWkVJeypcIc5Ai__iU-B8f3JaIB4FK0nmrZ324PspRLa-X0t4Gea7jULCjfaJkSu0jzbJ6IH9FbMXKBOaUK_KKTC8SLeuE5i2NJUj4pKTAWJnk2fV7UqeATXQ0Wt2m0aooRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9bKJDQzzdr9mprog5LK_999on2nrM4BaxW5KCF05-6NjB7yK9cPehobpFPATG4mHKl_MKE4xjgE6bY0otFl41P2dl5tyTTrIvfAkKNZIYGHjIGasvwtXMSUHpXQwY58Ai4VieGaZ9ir3H056Q27DIcsvldI_IAT6_gjsvevRL9jHEr3H6lRZ4hUYxMOo51izBVaAKHWgGix8DwcybR0b1qoRE-ydfpj3smHkTYLSbGEq7sFiTgGBw3esMoXYqtN8VyVlGVWrarM9JWDB4VzmQqIwlIZXZ3a2iV_lQy3nENr7bmdpxCg6xLZsf52NijMeIRtWkwNGxZG9vZTKYGN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5cExy81o0wQrYiQ0xyeH-LElrLLEEXJV6xA28LCGFM1BNtcu_JFqknuEG2PLd1WuuzMmtvImqEQjdJ8jW1AHGbVUCQhcvEZ8uKT_Fx4LdpAOXt85twnNI-IdMegCo6Hb1zHNg62N8Sxwe6wBz4IRIbRNwQXV-KtqYq2NnawIASsgCNF6q8pR8hzALAxOqpWSZAA_k9-E5x7romiWEk5fy76cqrHS9JX95wPFVptN7EvFSJoEEiYS2XdvyLmcjvcnPjJFhUV4l4REQDAK0HzhrE_RYo1tu8eHqRj8YvJU6xd2P5YrnARO407t4Y8BsS_A0Z_YKoF5OAHP-UnxlRmdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7_OwO0cMCT1Sp5BoyToc7idfshArs0djjmNZa6u19nJUebtqeBLYyb7v8fRorUuW4RKCll14yJTC5ucC5Nf0HLtnzDoCP5mUFri7qvHa-xMMgXQi1CVAkInpbzX_wgfNw5Gu9YLuFWfPZxWvg7sXAaQbZDqhmGqVrKtYWd2PhD1HPMhxxMLput3JJKHZGZ2AARdx6LZGr_KMRmdVrJPRUjBRhg1ainyiGjEM_Ycb0AuNuGaA1BTpab3vCaqmr3721C-3oLC428_gCUIFCDH-P2B_WcfrThpbBRpBMk6qXCIGfS5QjE4jp7Qa0greQnytJYoWhdvyJIBJ2SV_g0EXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
حضور رئیس هلال‌احمر در خبرگزاری فارس   @Farsna - Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/440917" target="_blank">📅 14:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440916">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d06b05d9c.mp4?token=JnMy3-eKbJFt4UUb7K5AnqkZX1KpyTIRQmbmYhOU5HqYbVwMsKctF2LdwxZ5_pECRb5CA1WqgGq9tY6nn7sma3N7YUV-L9mwAi29x-D3tBBeEqwOMrvtfcaCs-sMcynpQibGkrjTHLVmixBzGPMX7GMmxbX7WO5qM_QQkjjYW5LO8AiuTVw5vd25EfoJB8o8JCCaGx0StNlNl3TefUNOALIU1zF9U598H1CXmaPhQRjPqyyHfLZT8aYSRdcjYDRkJeP5h7zqiS5vuL3aRWR_DYis2zW328BSrekVAvqUhMYprIdpvy-gk1XTOCkX5a8cI3OMQO6RMlUkjtzUkWwM7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d06b05d9c.mp4?token=JnMy3-eKbJFt4UUb7K5AnqkZX1KpyTIRQmbmYhOU5HqYbVwMsKctF2LdwxZ5_pECRb5CA1WqgGq9tY6nn7sma3N7YUV-L9mwAi29x-D3tBBeEqwOMrvtfcaCs-sMcynpQibGkrjTHLVmixBzGPMX7GMmxbX7WO5qM_QQkjjYW5LO8AiuTVw5vd25EfoJB8o8JCCaGx0StNlNl3TefUNOALIU1zF9U598H1CXmaPhQRjPqyyHfLZT8aYSRdcjYDRkJeP5h7zqiS5vuL3aRWR_DYis2zW328BSrekVAvqUhMYprIdpvy-gk1XTOCkX5a8cI3OMQO6RMlUkjtzUkWwM7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ مدیرعامل فولاد مبارکه: به نقش‌آفرینی در تامین بازار فولاد کشور متعهدیم
🔹
زرندی: شرکت فولاد مبارکۀ اصفهان با وجود قرار داشتن در دشوارترین شرایط عملیاتی، رویکرد مسئولانۀ خود را در قبال بازار فولاد کشور حفظ کرده و تمام ظرفیت‌های تولیدی و بازرگانی خود را برای…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/440916" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440915">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde5aa2c4e.mp4?token=I_ohoUtUmoQPuObeHZEThNolPmfwf6qWJXBC3lvJqj23e-u6uyzjy4hU-XY43INJqzm0AZEN63cCwm_2NPwdvlS40PdBUDYXD263Co3YW0ZsDLhfbKqemocx2SVV8TQqTdvjFMUN96HImttjzppafONRASw_Sf8OmH50dNwsOEAO-AuWmwItg3HQ-_gPxYprlUVE23k88PK_Jy8EHCJk-PxaWvGOjdbo588eGwhsrcmIdO4j0_RiOLB4qoJmeI0ajy2UThArHkCVQM6RoZDyyBOTVW1BHCo71kxyBXAkAn1kxLbEZreEwhjwASwLprFSaoPIKUo-79RCZsk59oNAbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde5aa2c4e.mp4?token=I_ohoUtUmoQPuObeHZEThNolPmfwf6qWJXBC3lvJqj23e-u6uyzjy4hU-XY43INJqzm0AZEN63cCwm_2NPwdvlS40PdBUDYXD263Co3YW0ZsDLhfbKqemocx2SVV8TQqTdvjFMUN96HImttjzppafONRASw_Sf8OmH50dNwsOEAO-AuWmwItg3HQ-_gPxYprlUVE23k88PK_Jy8EHCJk-PxaWvGOjdbo588eGwhsrcmIdO4j0_RiOLB4qoJmeI0ajy2UThArHkCVQM6RoZDyyBOTVW1BHCo71kxyBXAkAn1kxLbEZreEwhjwASwLprFSaoPIKUo-79RCZsk59oNAbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کپلر: تردد در تنگۀ هرمز به‌شدت کاهش یافته است
🔹
مؤسسۀ رهیابی دریایی کپلر اعلام کرد داده‌های ماهواره‌ای از محدود شدن قابل‌توجه تردد کشتی‌ها در تنگۀ هرمز حکایت دارد.
🔹
در ۳ روز جمعه، شنبه و یکشنبه تنها ۸ شناور تجاری و غیرتجاری از تنگۀ هرمز عبور کرده‌اند؛ رقمی که تقریباً نصف میزان تردد در آخرهفتۀ قبل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/440915" target="_blank">📅 14:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440914">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPMauwV0od-zn6rFudH7KEdek0yaPC0qm1cayCSLgM8VEfzrM_cGQQUVOKTURiBp0yLyIG34490fKfpexlrEgMJmcdsZ9uw89KQzljKHguRxBdX5CFwGsMCnCRa0GgG26t1LvXgfT49k8h254H6YL08-ggeMjVowoG8pbbpoUovntnC-yjj1g04eJsbYn4ThabNArBXM97oRsuSPjIGqVAJFjNBiDW5TXEHOOwjqUobocPUh6Z5gMdAQXF1s8qirhM7BAXYoJO6EYEsCStJiBKSOTjwkD6P94HY6f2yJ5ZbD_z2qiY-IuB2jjic6b3_7q0BxE6rdH164FqCV_c33ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی فوتبال عراق به‌دنبال پوشیدن پيراهن سیاه در شب عاشورا
🔹
فدراسیون فوتبال عراق به دلیل همزمانی بازی‌اش با سنگال در جام جهانی با شب شهادت امام حسین (ع)، از فیفا درخواست کرد مجوز پوشیدن پیراهن مشکی را برای این مسابقه صادر کند. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/440914" target="_blank">📅 14:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440913">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184902a768.mp4?token=vhjBTRyyGvkbxmUz24TzU9FXOx0OSLBmF9tj0vspxNGWd94xGDDLjlenZxHXoiPasNaWHvnaD9OaRWSrKqoFzr9wCS-Kl64cmrLVMHopkB34kSCxPAQf7bJjDVR-xFSpR7xR4k1IOSPt86b-hqa1GwFMzbQv4exXYywX5XsvQQLHEPVjd3TIOF2ZyvHlI8-rET484yz3YsVb56Xb5KiGPG5SscIEdqciHMQLJIihbhUjph1Q1N28kH3HbA4CSiQT0COWgOgZKbmpJXeGjPdpUNicQ8fEhzOvK0QPSDU-G1OqX15ydsomJB1e60Lq0Zaq46Q-IPA3AK2TT7kGxznHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184902a768.mp4?token=vhjBTRyyGvkbxmUz24TzU9FXOx0OSLBmF9tj0vspxNGWd94xGDDLjlenZxHXoiPasNaWHvnaD9OaRWSrKqoFzr9wCS-Kl64cmrLVMHopkB34kSCxPAQf7bJjDVR-xFSpR7xR4k1IOSPt86b-hqa1GwFMzbQv4exXYywX5XsvQQLHEPVjd3TIOF2ZyvHlI8-rET484yz3YsVb56Xb5KiGPG5SscIEdqciHMQLJIihbhUjph1Q1N28kH3HbA4CSiQT0COWgOgZKbmpJXeGjPdpUNicQ8fEhzOvK0QPSDU-G1OqX15ydsomJB1e60Lq0Zaq46Q-IPA3AK2TT7kGxznHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ترامپ سقوط بالگرد نظامی این کشور در تنگۀ هرمز را تائید کرد و گفت حال خلبان‌ها خوب است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/440913" target="_blank">📅 14:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440912">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DH-eNOOET940nB-fUoPyHhPbiTjX7LyhAahqwU9KUZrW21QsJI61mpmKAVRPjXq68u6Re9gZseymsbt3tljqsWpVfSITFhZ1HkKK2DZsy-s-ETqjJlX4TnlF7YN86OVDv5K6aXd_WPphbJSqfQ-lCQdNLc3l5TZsSe5ctF2c3RMxgMk-b3yhVDuY1_FfzjzN1KQu4ezELYHMw7nkhsAwetb58_zkzCwXg88MiJQJzSctHj_tXhHIi2DVIFZ-V5GxA_3FZr9wtaMTvk2A3dG-0TXKuxnR_iawClAM5Gc-DowU0DPTTUUkk4kEOj7DusNdNRXFbEVMwUgawZ16SGjoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع علیه تأثیر معدل؛ اعتراض آموزشی یا آخرین مقاومت صنعت کنکور؟
🔹
اعتراض به تأثیر قطعی معدل در کنکور طی هفته‌های اخیر با تجمعات و فعالیت‌های گسترده مجازی همراه شده است.
🔹
درحالی‌که معترضان این سیاست را تهدیدی برای عدالت آموزشی می‌دانند، موافقان معتقدند افزایش نقش سوابق تحصیلی به کاهش وابستگی آموزش به تست‌زنی و مهار بازار چند ده هزار میلیارد تومانی کنکور کمک می‌کند.
🔹
کارشناسان تأکید دارند که در کنار رسیدگی به نگرانی‌های دانش‌آموزان، باید نقش منافع اقتصادی فعالان صنعت کنکور در مخالفت با این اصلاحات نیز مورد توجه قرار گیرد.
🖼
اما درخواست دانش‌آموزان منطقی است یا خیر؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/440912" target="_blank">📅 14:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440911">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a8c1b8fa.mp4?token=EDWDsBbgN1jVglgXqX95ItavyEw1P5dVDGR5ZUK0W9G3C3qTs879qaM0IPcVCpAMmW-MFZPTppWQ2uArX0tHj9RYShjdGB_IVuGdd4uITc9r1Veoa09x4R02O3jI_D6lzDkMnlJjtdEqjMdIfnnI6fojrlKHZ4s61uG_rfgSfxnku7EIOeQ1RldvV7kFX9d0zaI3utppd0LX5dVI_10MFqunk7EU9n5HoUqkm1NDbRNiWHfXeYqPcADSeThVRyj1UIcz0YjjRsDlEgdLzYQR-kd68o5kFyJuxgw5jg87oOHJ2uE8RMUd1254j2a9wI1uuN1dwPUBI1hbkszKvXVdYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a8c1b8fa.mp4?token=EDWDsBbgN1jVglgXqX95ItavyEw1P5dVDGR5ZUK0W9G3C3qTs879qaM0IPcVCpAMmW-MFZPTppWQ2uArX0tHj9RYShjdGB_IVuGdd4uITc9r1Veoa09x4R02O3jI_D6lzDkMnlJjtdEqjMdIfnnI6fojrlKHZ4s61uG_rfgSfxnku7EIOeQ1RldvV7kFX9d0zaI3utppd0LX5dVI_10MFqunk7EU9n5HoUqkm1NDbRNiWHfXeYqPcADSeThVRyj1UIcz0YjjRsDlEgdLzYQR-kd68o5kFyJuxgw5jg87oOHJ2uE8RMUd1254j2a9wI1uuN1dwPUBI1hbkszKvXVdYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متخصصان صنعت هسته‌ای موفق به بهره‌مندی از فناوری  پرتودهی گاما در حوزۀ سلامت و  امنیت غذایی شدند
🔹
رئیس انرژی اتمی: به‌زودی ۳ مرکز پرتودهی دیگر در کشور راه‌اندازی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/440911" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440910">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd21840df.mp4?token=QMcllL1dSkl0n5-ebcziSo2TN7Skqx55n6HcChxfOv3fybHfXu21EcMCuX0ulO8GzFvetxUdcAwbpLwc3jL1grTUUnBUBYxeznSJT-6vAgtHN25aq7g4hnHO9EjJHZ0h0bRmbZlRlSEr4z3DeBeXh9x_Br1RQR-bzQk_OHDtndGOPb4FSgRByTVwF5r18Nqd66eVhmeb4_IsgPDuE3q60zqvJM_Jf73VFTjanhe2HAObS4IjbAzm2HLmCPNlaSkZTfakhNqEUqtB-t0a5K3oi9DyznWNFFny1cnQFdaLFqwJtRGwy81ffiL4M2FGn8VSdlc8n8XUnAN91GX2qscn3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd21840df.mp4?token=QMcllL1dSkl0n5-ebcziSo2TN7Skqx55n6HcChxfOv3fybHfXu21EcMCuX0ulO8GzFvetxUdcAwbpLwc3jL1grTUUnBUBYxeznSJT-6vAgtHN25aq7g4hnHO9EjJHZ0h0bRmbZlRlSEr4z3DeBeXh9x_Br1RQR-bzQk_OHDtndGOPb4FSgRByTVwF5r18Nqd66eVhmeb4_IsgPDuE3q60zqvJM_Jf73VFTjanhe2HAObS4IjbAzm2HLmCPNlaSkZTfakhNqEUqtB-t0a5K3oi9DyznWNFFny1cnQFdaLFqwJtRGwy81ffiL4M2FGn8VSdlc8n8XUnAN91GX2qscn3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس هلال‌احمر در خبرگزاری فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/440910" target="_blank">📅 13:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440909">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nU0HBvpYsCKjgqExWODhlvKIDzOQsN56EgMDdsDq2bi6pW1ia9PFgYfVoxQO6Twuzf4fKYfV6fQV24kSApn7Fm0YK8Q3XzMEdXnvMXUMez26N3uq1AgM4t-saO80Lh08N5e-hAYki2rFy1vuhfYLZ5mrOHUnRA4Np7ijqgaCiHUQEC5v1LVDablNTN3TdgpZaBse3VKhU4PFSQPbxEcZPa-kA6f168iR87ngdW8QmYOry2v6v7mgNJrXo--UkNTDeqBrKpBCyuL4Y_vf4ExUgekoHUUuuMXlGXq_7yLXTnNERwvZ5FNGOmVlj_uiyBpsVWu6SUq0tGhX_0prf4jTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
😇
رشد حدود ۲۴ درصدی سهام «سمایه»؛ بازتاب اعتماد بازار به مسیر تحول بانک سرمایه
🔵
گزارش «صدای بورس» با نگاهی به روند معاملات سهام بانک سرمایه، به آثار برنامه‌های اصلاحی، ارتقای شفافیت و اقدامات تحولی بانک در ماه‌های اخیر پرداخته است.
🔗
متن کامل گزارش را
اینجا
بخوانید
#بانک_خوب_سرمایه_است
‌
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/440909" target="_blank">📅 13:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440908">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جانفدایان اقتصادی ارس (۱)
مجتمع فولاد آذرآبادگان ارس
در روزهای جنگ رمضان، منطقه آزاد ارس با همراهی فعالان اقتصادی، صنعتگران، کارگران و تیم مدیریتی خود، اجازه نداد چرخه تولید و اقتصاد متوقف شود.
در سایه مدیریت، هماهنگی و حمایت‌های انجام‌شده، واحدهای صنعتی منطقه همچنان به فعالیت خود ادامه دادند و ارس به نمادی از پایداری اقتصادی در روزهای بحران تبدیل شد.
شرکت مجتمع فولاد آذرآبادگان ارس از واحدهای شاخص صنعتی منطقه آزاد ارس، یکی از مجموعه‌هایی بود که در این روزها با تکیه بر توان کارکنان و مدیران خود، تولید را بدون وقفه ادامه داد.
این قسمت از مجموعه «جانفدایان اقتصادی ارس» روایتی است از تلاش و ایستادگی کارگران، صنعتگران و مدیرانی که در روزهای سخت، سنگر تولید را حفظ کردند و اجازه ندادند چرخ‌های اقتصاد از حرکت بازایستد.
#جانفدایان_اقتصادی_ارس
#منطقه_آزاد_ارس</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/440908" target="_blank">📅 13:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440907">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/440907" target="_blank">📅 13:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440906">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پروازهای فرودگاه هاشمی‌نژاد مشهد لغو شد
🔹
سخنگوی فرودگاه‌های خراسان‌رضوی: با توجه به شرایط پیش آمده کلیه پروازهای فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد لغو شد. @Farsan - Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/440906" target="_blank">📅 13:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440901">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_21UjEaoCsOV-cko_JWLTv4LRiPpbXgtqGGgM02MKQo5iiUUDZj-8b6-f624Wso02CNP6Joc0w6sYB-44m42rmQfeZZRvFiqKX5bVd3gbloSNHav1qws4Olh9yIgv6uP-BS2v6Hv8j4a_b2u4ZP3gh3ijbhyaRDwrbuX-4Yyqg0hrjptdWNUm572rKvLyn_fBI9VtfsTyZcXPcgKy6Dv8MecO-I9FEVcVlOTcsRZsi3VfhLYZ7GG3o7bIWHdY0iwnCHqLkYZ52LbYZsE5UmfVYv3DbbfG6SsL7lqViTym3-S8GL1XgheEYaYxj80dd4ZklquIkSlmocKZ1yfFB4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ih7u3s4iytJTVJMo7TBFsyDq-Y-Hmui3zPG5_pxYZnoVnactlX2oHPnYCEwaIa5ZN4rG6NcBO76tCF0X7YZjf-MmiQ8k5ylTzj1ZpU34-dUIqvjD8FnP3atIgESUdn0AjceRLFsT2XI5sebq6xTETEICQv0PHY_a9tKXtM3todzPZbFnneHPlyWHvUE1XnCnqcg7wCDiyh4f6NV4cy5BxKMZTgB-tJve-fT0X2BJI7SRgr7r8sz1Hur4o_OwPLNtvWEdY1jiwiW757gP5gYGVvl-hmAAbpf0a8-S9AnL2h6PuMkkns5mroTqYM59bXk7h8iU12KN5wPv5NvDBEbweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qA-UL-GkBYhvUnyDyrhGK7azpOJzWxDjxuYqoaAwigJZ3vA3wkoSzmxpXBJy8pvgL-Jo7Dk5YJ84ouXq5G34XNO9FdQ6LlOOL39ZgcYvR3wvcYKa9nUcPndhMLfLVsDBRV6DaBYenhpu4WpK1QTVyoFZLmFa2aA1ywldBCgGdYRjBTC3OfrYJ31ORcQWA__pPNHL_eXI_aDLTCBwYa8c18Yj3gWTANBGCaxmCjbdAPuoNF28n_O62w0ZRD5dRTwx2kmhrLNttPUtGhOtqRGy9LALI_Ob4BNdlvLxRCM30gxeDjJdmbR9HQ1l0W_Egg4ZTPi80BruxsZcHruM8GKmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8YrwecVo2xc0D9I4e0oy-thaNrGeBeB8mXzUNxBfvLKKJP6r8vLlASu87NJXzvePq-6bK9pO9wgBpAV7_kl_yqxJvbKjcfYlCZrbuFzMm1n6mnbTTSG6FrxphwzdUY8caXrZsARo8naOm7kL8uqLBQFhDic0nRLOJlgtrX11Z_E8pDgkoVIv09rX7kbtdpXuNJJMUTwP60vUHuImfygLJOmy3HR40_I6Ra1uxHYKLwWpmqFGsirWt8rnXTtL5Wp-9peRDjMnhbqlWz8NAAXMQbN51j-fJSuPGwc8dJV4Wv4rpS2u58TlgFyVYIT1oQFYlWV3Y5wfsjP5_WDhWle1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2Xi7EKEo2ftYFjc4jili7CrpDhEfO9gEX11Ru-cDMf4yC6Bzesrevd64_oXP5IApUO0QNl5MckAbXHpfHqET1HZJ0fKkzTRewtrjZUmm1WCrsihpholzOjbWxL22ow131Yn-YmFH0cxBvvgnaJZy_HHKlK0zUdIxyY5lqaqhSXVYQTO1BetT0MULh0E8bg7qykRZbu0VS61g9fHFeGAyexqaeJYyVSDcVnHEYqrh9DbTEA-cr-Ijz6oIs_Nd76wu2Uv2CuIGXYZzyjDgGypWMSi38dl_g354zCUM0AtUiW5J4tL7jI1aqZ1EMzlutOdFZD6aR5VvOD1Uu9TyiaqyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار اعضای دفتر حفظ و نشر آثار رهبر شهید با خانوادهٔ سردار شهید سعیدی‌راد
🔸
سردار شهید مرتضی سعیدی‌راد همراه با رهبر شهید انقلاب، در اولین روز جنگ رمضان در اثر حملهٔ آمریکایی-صهیونیستی به‌شهادت رسیدند.
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/440901" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFcc24uXus_Luwkpj-fDKX7HgVnU3nC_iepBbxxgAdwVPQbAUk0QyhalIIT0fQPefe19nZd6XoIwDqP1pdTdN9_uuocYQq0JYVcz1uz-phXJBxxdu_hGuDHQn5CplBTJlHYMeU2wyPuQ38RNU3gMDqbhuo3RJPBQVHu9LroHHDHxUmXg6OMhT8xNOJ9zS-wJwhaOa94FaRqGObcK0Tzeyw6ITLofa42seFOKWMWqVJPG3c5WFmKtE6n8c7ostfYb2GC7NqZQbkg78s2DtGc5sDWEH4JsULNPAJd_DcG28-dsL_v7pKIUzCarDkcqgXbFEe1xkAZ9R-d7rJl5nrdf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عبدالله گنجی: روایت منتشرشده دربارهٔ جراحت پای رهبر انقلاب غیر واقعی است
🔹
در خبرها آمده بود که یکی از اعضای محترم مجلس خبرگان رهبری در سیرجان گفته «جراحت رهبر معظم انقلاب در ٩ اسفند در حد قطع پا بود که با درایت پزشکان مشکل مرتفع شده است.
🔹
با پزشکان معالج شخصاً صحبت کردم. هم تکذیب کردند، هم از این خبر غیرواقعی تعجب کردند! گفتند اگر صلاح بود از قول ما به مردم بگویید «از اول هیچ مشکل اساسی وجود نداشت و ندارد».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/440900" target="_blank">📅 13:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440899">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6f3658ef.mp4?token=prI6OxXNLx32-QMkLw7YH5O2Q6OIDZ8QduCKVb-npvE958ZD7iqIadH3E4cofQEEypF3jF3T70EeZ52cxFifGavoIn_MeLvb471RNbglWJ5MV9XPb4W9okAkkXQdBBXvWdUx-Z0dylxzHYaOIUecDvt7ke2S8XjhIqLfTbXmW0Ja0ZFPzkOPBRzbrppKS7bWEPLHF0zrRiLhl-CHC9hDHAXINt7Sf1yZVej4DuJbcTMFHz08lJY7r-OGiLVzjjlC4X9AbVbS001O6flLtHvc7wxr7-6iFX_zhpUfuQOaB0jsZjR3_3KZd062R5PBJTsGNRdKWnDhChjUsnyF6a-lPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6f3658ef.mp4?token=prI6OxXNLx32-QMkLw7YH5O2Q6OIDZ8QduCKVb-npvE958ZD7iqIadH3E4cofQEEypF3jF3T70EeZ52cxFifGavoIn_MeLvb471RNbglWJ5MV9XPb4W9okAkkXQdBBXvWdUx-Z0dylxzHYaOIUecDvt7ke2S8XjhIqLfTbXmW0Ja0ZFPzkOPBRzbrppKS7bWEPLHF0zrRiLhl-CHC9hDHAXINt7Sf1yZVej4DuJbcTMFHz08lJY7r-OGiLVzjjlC4X9AbVbS001O6flLtHvc7wxr7-6iFX_zhpUfuQOaB0jsZjR3_3KZd062R5PBJTsGNRdKWnDhChjUsnyF6a-lPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار مرگبار خودروی بمب‌گذاری شده در مسکو
🔹
همزمان با ادامه جنگ روسیه و اوکراین، مقامات روس خبر کردند که یک نفر بر اثر انفجار خودروی بمب‌گذاری شده در حومه شرقی مسکو کشته شد.
🔹
این انفجار در نزدیکی همان شهری رخ داده است که سال گذشته سپهبد یاروسلاو موسکالیک در آن ترور شد. او که معاون رئیس اداره اصلی عملیات ستاد کل بود، در یک بمب‌گذاری خودرو کشته شد.
🔹
دفتر دادستانی منطقه مسکو اعلام کرد که بر تحقیقات در مورد این انفجار نظارت دارد اما هنوز هیچ مظنون یا انگیزه‌ای معرفی نشده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/440899" target="_blank">📅 13:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440898">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
عاملی: تصمیم‌گیری دربارۀ قیمت‌های اینترنت پرو مربوط به شورای‌عالی فضای مجازی نیست
🔹
عضو شورای‌عالی فضای مجازی: بسته اینترنت پرو فضای تبعیض‌آمیزی ایجاد کرده و قیمت‌های گران آن در شورا تصویب نشده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/440898" target="_blank">📅 13:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440897">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiVt5m-rQWJFF5nTQfLCNuGza6YUg3qbV9qd3ldrow-Bp9J1iztaWSfvRB2oteKkmO-FNJ6bQI6UKirRtgfnPzzvGVVOKRA1Az-kw-FxyOwdxxPZV2-zjzPxLdiBdYwW-AIIesgz9b7zuxRJnWgxIF4DkIEg2O7A3YsODFSFC0hoc9MuJZ6kCqCHhJTV_PK7_Kqg5D9BuOTYmjgfLpNVMT21LaM6EWTLY5ZNoqd_yPVU81TWuQl6Fz6LxasM-CzXNRAh7VBh9RV4C5JGCM0zF6MjttBoxPko49Ws67ZIbAR4oyn3H--L0h814K8AKGFI6Bx08e2C1D-TSNliXGHIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تعویق انتخابات شوراها با مصوبۀ شورای‌عالی امنیت ملی
🔹
رئیس ستاد انتخابات کشور: با مصوبۀ شورای‌عالی امنیت ملی و درپی شرایط جنگی، انتخابات شوراها و انتخابات میان‌دوره‌ای مجلس و خبرگان به تعویق افتاد و زمان جدید برگزاری آن پس از اعلام پایان جنگ تعیین و اطلاع‌رسانی…</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/440897" target="_blank">📅 13:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440896">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5x-4f8iWWaK_SSwzmx9naanKPYr9GG7gd6Q6Zv7LpbhorcO5k0Hcxm4cOPAMsELV9jpHzzKXOdSwn3KzVqVRcFBmXKERHF669Xqpd5NU6GQEpmroQUIurrmDdTJOCZwsHyKZhYLUcXniLUd31cGgdNNhCX4FEW-TkVW_0IGnEwb3qKTY3VmbXKo-IuYUMcxrb8GYDhIHyVrgskSdfbw3MXXbzyi2nFtw5T3nwiH7xIazSy8UQbffMw5VwOpU__YUpRq9rMuN8BlAY8gnbRXFh5QCjHm8yJ78v-rlblUJnpnuiEkCZNmiwNaH-kydIwEbhNMdsfWCjGuI39Tvs7QPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با جهش سه‌رقمی ۴.۵ میلیونی شد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۱۵ هزار واحدی به ۴ میلیون و ۵۴۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/440896" target="_blank">📅 12:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440886">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6kgoUgTSshPJuzXn4srX2HXP4xAd-G0Yezstsd-1NE62wsHR8Trbx29dbASwZT0XUVPHSPHMndOA1_x3ro48y27LRKjIaYWs2omiDexl8zRnf5RhrGFXMFDPg-z13r9tom_9WbO9ZoX17ErUXmo4xKHg9-OF6LBphnXxCYcHLsSGhRfRf9lx5DJfwx8dtfLtJN-xaNXMzsUpm58KapmVOCVRTQmmcqqi0d_V06uhBUQrKTrKRvEcoQP5vNeK34wPoG9S3J1PHBvD5AJ5YwXIoyPkD_NftTYtuu74rwvWMV4uKN-gYLsADVvSjrZsIb4aMWYeIhiYPGE-cGRurQuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQLkUYgMjMfjXK_Ddf283X-n7sC58mSNkLOvWbX6InWtRCQ02miujfAUjCcARRLwObdHtvkdE-l6lnCvbdpZy9w83g992RjJBlA6dh4KkwM9KJCbNIvcfj0EAdLq0Ksqn5rJldlDki8SDpF96BQJ5DWwJOFCkE0ykfaw8BHMwwu39wEQkzmv6WSGqS75E4jvSK9PR3eRNbv66dvH7_EDfnHYJ2HUhrqyp3vBfLXbIIWxYrpOurZpesg-OpdUQIRLs8DnpIsARSCKl4Y5EvATPR4j8xsnr4NF-nw6htkC_vdxoJKTvAuWklOwF7q-7YqsBCCMWqY5QA95WBlsw0HHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_tqSs76g4pHTO9rejgFb-Dt3nI5z7hQ7pFas43kifIyXiOfgqNufxQwIzAaF2vDaPb4POrRQzYUS4q4i9uxb1Flx5l4RWdo-cpfs2aSJWNSqmWyDKYIx8HNY0v5do4nClNAT_Ie2d80DqLI4VpbF3pAR5tzxgqjFr7fCVv2nQ8V6Sl3MqzviNiSXsz9TnekifoSGTC8Gz-F67bLXgf-p0gZBdOtKOMUbj6av-4U0gHQOTRLnKX-THpjUNjjg41krHp0tb7mCFZ6tzZYWvn8REI2K7hJXtcAEA7C025lnA0Jc0bpOjIYahzp1AS-1AP8OcFJm8KeynCKjFq1psA45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QaAkEYEAa2w6U2rFfQGEwZyP5x9eGBq6HFrYF5-nV2p2c75Lv4OOMbKRJrJ-FXIqRaKhYkY7-XXHhA3uwzX_L1ZUeFtJgp_Ptj9QZr7s7AtdhMRCGtgiLk15tuA1zYyxtmrY8WpUxO-Cb_q_S7Yf7Ma5pVVpZhmshwPOd01gJBgrH4CnnvWkcNbZPbketgjqc7-Drv2MWgZTGS1CMtsLE2TvKlw96Km9iB0AbdAeNxoqsDwIPrWmh0X1dCsPpjYLU9JBXHabywaApasYLvNYhAn1kSq7OPv7t3n03ggXfV44UThUhBW16h5wmCnU595NyHssFHZZzU1DQ4QMfJaZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcuS_JG0wltgaU9_4kCcbWTRsAF86HXx_bI8SJWl-RkSbhBIvoMgpTs0vq56eq2ZYBciPdxjA4Q-PnY0HaXn3QqBNkvC2UglF5BastfKfA-7iaC0HA65rtyBKIAcg9ndg_KRp1QelErg6X1qa8GkJYq5-V_4-ZrjMNoBBkJ2TzsYytMf86Br4WIqHO13r9c9eMzjyxjmvykq-vPKpq-YhNq6gMk1EOefWK4IEv4m-vPgYpHwCzx1nNSqSylZvUVf-LsIo7QIFcHFuzuN_8z-nKsQv03Rk8KSCMY07UDEjo77yAu9mFbCT3qF7Ib6FKOotRIXcI8J_gw7DhOsLw7_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7iPA0IwBvxmyrzkz0pu8c-5NZNKpLFXRrbm1WGwF4IRbzwCYSqT_TK_lraKW4Mp2ho5gHuHneVjKBN6J6kJ7DzReF1roKU_tIW5Fi0rTpgA_V4rIMbstJ5FBqcCwjUUQuD634e2C3LrWYY5jh6xWZw4zaKT0mF7DhazzLQU_fTJ9yDmB5bcoIj2k4jnQPeEEj4ZjC_NikUuFzLHgV-CN4ngLMRLW5IsDo2l00cntsGLohHrE7bcAjAmda3HFCWZL48CFbLRmx1Wt3VXOZzyt4XDHQD9csrR6RuDzDI7X3_KB2RF8HjP1WOBZyWj-PYECg7QQoTfPX2KdhSTsqu6iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNg0oYHVMRgSCj_O68DtnxHv87WIRFvUrFo_C70FVpGrzM14k8Y1T_Atr9c0p4JSCSdpEAitbnG33eD44UEgrk4zLA3VIhQiXhpQuMU6pV4QxfQJ2XZopvTX1-2CubMNXrSMCcc8nKs54Xx-3wA4NbQJ8q0dTDOpisM3eHSj6Nv_UyNgkxIxkYtcLdqb98eTakoF9-0a6R4WWoX4sumfbZ0wHQUw2uD-7NJ7rc2TC09ScdNjY-N6enDQGzSkjHY0JXEYP1zKmUxLjy4PSB-A-5FbTWPawBSRBO4TV0e2XqsIvq5ZadnxLG-UZ7jo_FxwMbw2v_d4zPYhDzrn4fcHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X69juzC3kv7PSMPz6G8dVAC6recAU9BLTNp4BeIxdXC-PFpXuOZVpTvVg2aNpfxjvzAr70r_vMS-44UvvGkFR61qqwuvSu6-lqw-mSINqf2t02E2H5u7Ymn4oJr_E-tAqiWeXaTFAqHG4e0dQxG502U6Q0es2g0azPo6O8vtW9XVwmMCF7bjDkyyO06PflFNuP-rH8Ia88EjHA0WpKryh5Z2TrUOg0Wf5nyFjxgJ2aENvDLBDtSnea1E8GCs5FIR_z0VYOmuL_eqAirQZdSrzZkp6nsjevnmEYBcWVQWfyd2EUFUMoYyZ6CSuyLu7_qekSkSjhlYNQ7i0NsxHLUJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTVuly6Td0YRlZnEH10CAGlVnQsYinkCQNRow8A0onzlhYcLgR4FNhu99sl7tHZJjlf93hfgjt7TgdFxVk9_sgiMO5FoukQTKgu5IAMd0YsGC_zvQie7GSaJ3Q-fpZX4VzExTZjUWfZy0mN7z73rNbFCdsKMJI7iEzZLCtVkH2mp1Lp1KqRax_EMLVhFqRSxWVGfwPNCnrYBwc2ybuea5pxZifkaIxXQH0vNsU6m7ITjKiIcYsQjFizKkiVoUPZY7Y7j-tKeZoQZ8bupAjSPUrsTdqAw8whYQZP-kbMtxbT1UnDmZPxQMNl_crzPUjoSb52PH816f6g7ld-1ezEZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSK8d48xAhFvHDYIRvpY8jYwm6YL9rqLlIdkw3QLC2cEwzP01DkdULpzocMxuua9yNMHQVmX7dPSSXYLXYRfpofjYwFhyiQrAq3TB_Z8qJNPaiEXVQP5jONJFAT6srjRoUEk-CuuSOQExglKTqeNshAs7hwUIOn99NyoOsVCcCnHhKaFT_QSEu8Gg_9s5pRBJVRWPrXgexVA5ZnO5oKr9zkH6JUZx42sPfyQaC_Ox2lYsFtbb7IH4_bxpNuIsHP3QY_3PikD-pqj0pyK8XQNSuYg8pbB-HrQ0vOB1rU_5jizDkg-LmpQYW_AsNse8jxokttSvQp4RON_5bxpJYONzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی به‌جامانده از صدمین شب بعثت مردم
عکس:
محمدحسن اصلانی
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/440886" target="_blank">📅 12:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440885">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOGoNlHggvfziX0rvatjUlLlEdlPKGNlPJxMQplU-pxw0NK6-t-wtcsYIOnIjEwf0KbhDkbEvxTv2fTahC3yyCus_gHDwiALeMFNXBSVh77qPW5g410dMkUOemMtVK-moXlU-yTowYE6t0l6GzuHRHiFhyGILrP3gyfXwdaNWluLgcMbWTJnqwgsdsflA4OvreNmCy6fuQ33TrloKBaZkQfrCbJalKCEwPKixxqIhduOkbuzufu1RUG-pqP5EYRbasNdkrkDtjolPyZKE-9D4EoucPiQYSorAC8EDw6-Ny0m2DHmM3M4JuTuC4trlkdHLoxn2iZQKk3jgqMaTryeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعزام محرمانه چتربازان آمریکا به اسرائیل برای تصرف جنوب ایران
🔹
خبرنگار آمریکایی کنت کلیپنستاین در خبری اختصاصی گزارش داد که در اوج جنگ با ایران، «ایالات متحده به طور محرمانه چتربازان خود را به اسرائیل فرستاد.»
🔹
در گزارش کلیپنستاین در وبگاه شخصی او آمده است: «وقتی پنتاگون در ماه مارس اعلام کرد که لشکر ۸۲ هوابرد در حال اعزام به خاورمیانه است، یک موضوع کلیدی را پنهان کرد: برخی از چتربازان به اسرائیل اعزام شدند.»
🔹
او نوشت: «یک منبع نظامی درگیر در برنامه‌ریزی جنگ به من گفت که این اعزام با برنامه‌های مشترک احتمالی جدید ایالات متحده و اسرائیل برای تصرف جزیره خارگ و ایجاد قلمرو ساحلی در داخل ایران مرتبط است.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/440885" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440884">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">توقیف اموال ۱۳ متهم همکاری با معاندین در فارس
🔹
رئیس‌کل دادگستری فارس: پروندهٔ قضایی برای بیش از ۲۰ نفر از عوامل کانال جعلی معروف به «گارد جاویدان» در شهرستان زرین‌دشت تشکیل شد.
🔹
در گام نخست، اموال ۱۳ نفر از متهمان این پرونده شناسایی و به‌نفع حقوق عامه توقیف شده است.
🔹
انتشار محتوا‌های مجرمانه و جریحه‌دارکنندهٔ احساسات عمومی که امنیت روانی جامعه و ارزش‌های دینی مردم را هدف قرار داده بود، از دید نهاد‌های امنیتی پنهان نماند.
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/440884" target="_blank">📅 12:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440883">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNQPgZ8Fmgxh8i0d9ZqjfBJ0yXLWnlo9FIlV8IP0v4ek1Tq81hFHX1a9DAt5kUW5WsYl7x4Zwk2StaFe7SnkzNiyq8bg5FNpV_zkuJSk02zgnDS-zjZhA9iGWbWsHD8nqGWs29ziVbdzwa0Rf20RjAjp2WCL1dCf94MiOvzbMjee1nywOWmNxrEoA1_fQlsFRyXSBRpZVu89lr7B6ghVDHIBIVEKIoTD3R--COPjdyZGYqteBOTN-QVl2C99y2f4Fsy15Uet5-e3d4Gcn1PiGJiGX1g-y64He4TZQ7_vSvR7-uz9_X-skjbaoIPcES5TSvNm3vNw9LoSTU3Zqa7DoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین وضعیت اتصال اینترنت بین‌الملل
🔹
با ادامه روند بازگشایی اینترنت از عصر امروز، از ساعتی قبل دسترسی به اینترنت همراه نیز برقرار شده و کاربران از اتصال دوباره به اینترنت بین‌الملل خبر می‌دهند.
🔹
داده‌های «کلودفلر رادار» نشان می‌دهد ترافیک شبکه اینترنت…</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/440883" target="_blank">📅 12:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440882">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1826abf8b0.mp4?token=j3BX-1oEv6LewdMgtV3LoQ2tzkUaqBbTbeOj_XKvCP3T48kDNXs0lgnJ1jFSvtkfWRvCAadkx2AYHuicAfYf09XNlMVlsGYyEks0mrpEUbh6Xt5Y2-kFxk3VUMU2PdL5F25omNk3eP-j-wgrrNfwKWT4AKTIaK1PMNzOwBapli6A3ut74oH3TaC7yJQ41eaHzUWmCCj1uSmddcuQKJdmwilkQ6meiXaJQhDl1WHDua4k9O4bX0l2v3hIXpUZa99po0PBRzXoW6GcQHUvtBiuDO4_yY2n4ffgdAcQUkPq1bP65uQnX6LtArMEJm2XK9_z0CIe9yTGdwM4l-KMKf858A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1826abf8b0.mp4?token=j3BX-1oEv6LewdMgtV3LoQ2tzkUaqBbTbeOj_XKvCP3T48kDNXs0lgnJ1jFSvtkfWRvCAadkx2AYHuicAfYf09XNlMVlsGYyEks0mrpEUbh6Xt5Y2-kFxk3VUMU2PdL5F25omNk3eP-j-wgrrNfwKWT4AKTIaK1PMNzOwBapli6A3ut74oH3TaC7yJQ41eaHzUWmCCj1uSmddcuQKJdmwilkQ6meiXaJQhDl1WHDua4k9O4bX0l2v3hIXpUZa99po0PBRzXoW6GcQHUvtBiuDO4_yY2n4ffgdAcQUkPq1bP65uQnX6LtArMEJm2XK9_z0CIe9yTGdwM4l-KMKf858A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام رضا(ع) برای ماه محرم آماده می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/440882" target="_blank">📅 11:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440881">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آمریکا ۲۰ درصد اینترنت را برای ایرانی‌ها تحریم کرده است
🔹
درحالی‌که آمریکا از «اینترنت آزاد برای همه» سخن می‌گوید، بخش قابل‌توجهی از خدمات و زیرساخت‌های اینترنتی را برای کاربران ایرانی مسدود کرده است.
🔹
براساس آمارها، از میان حدود یک میلیون دامنهٔ برتر اینترنتی جهان، نزدیک به ۲۰۰ هزار دامنه برای کاربران ایرانی تحریم شده‌اند.
🔹
این محدودیت در میان ۱۰۰ هزار وبگاه مهم دنیا که در توسعهٔ محصولات دیجیتال نقش کلیدی دارند، به حدود ۳۰ درصد می‌رسد؛ یعنی نزدیک به یک‌سوم این زیرساخت‌ها برای ایرانیان در دسترس نیست.
🔸
ابزارهای شناخته‌شده‌ای مانند Adobe Creative Cloud، Figma، Midjourney و Canva نیز در فهرست خدمات محدودشده برای کاربران ایرانی قرار دارند.
🔸
در حوزهٔ هوش مصنوعی و توسعهٔ نرم‌افزار نیز تحریم‌ها دسترسی به برخی خدمات شرکت‌های بزرگ فناوری از جمله Oracle، GitLab و Google Gemini را با محدودیت مواجه کرده است.
🔹
این موارد تنها بخشی از فهرست بلندبالای خدمات و ابزارهایی است که به دلیل تحریم‌های آمریکا از دسترس کاربران ایرانی خارج شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/440881" target="_blank">📅 11:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440880">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkBjy9WA3GM7-Le7el4CBNVtB7qfBbqpUdJ9WoebBe5A9Al7sELwrJ_0XS8i8IJh9dPn5S5vbo16A9bsRKCa_dYYrNXauhz7V9GIvFSaOR_QcbATiekcifvSwM5n5wWAPFcH_1wPXgR4mWzPLSIz0ShEjDpIogaDQrVMwkmK8HJ1a5LySB4KLbJ-5qotGPtz7Dy9QdDmEWqmbrOqAYpdfbGgQ_tmxX1bbrM8iWtSy_-BucmCUAoXKeTLm34lfnWMilIVLoPK1EvbyCpra5JQvo3VchTh51bLG0xAukphQVA1Gu87euvx4YNJ-W4cAq-DFg3lwS-A7_1Fnl9usZTDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیۀ شماره ۱ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه
🔹
برنامه‌ریزی‌های لازم برای برگزاری باشکوه مراسم وداع، تشییع و تدفین امام مجاهد شهیدمان توسط دستگاه‌های مسئول و گروه‌های مردمی، درحال پیگیری است؛…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/440880" target="_blank">📅 11:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440879">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ade9a5ee.mp4?token=pbhJEHUnXaFVudX9wnFFLY0AnrRo3hzEcV-olx1okH9XJSdZ0SvmikvIvf_jjtQNaYGuVGtxUnZEhwSFpBpwIZGxjHzrMQrCOYeafm3AZ2FToeC_WYeXXtbqIt0AFs05ZFUu0za53UNr54CmwZnfprNcpERD83PHAPCysXFoKdwfjDYX4s_EjT17XOpNxkqIzb1vIsB-tHFIMrDDbfW_FSwrJyRzmVgj10-UTmkBYlcPMnG-qRagzh5qH2XBwR0Vy5fgbu2-Vf-8cYjt8GrmaGiYEFgJiySSZrByqxffIBS_xeiOdHgt8VmeiUHVlnudABSWv9SBRmM7iHwFxtrxjUWdQYb9KzwFO4JGKC6XJY9kt5wAK3kt6y6STVfc9bNhgtokcA-r7UJdzu_c_aOXV3lkUvcwZ7psVltrJbwgpcTsIyYEEp2_w-F4Xv08tHnVLDg_STXXhB0EFyi88yiqNj8KVb1tsqqDJxIJ-Bql0xqfzQKQPDOk0j39q7eMQTFbIPLO3TKUlM7aji7sINO5bZUbu1TMTUAnEhA6y_ExdPXpp23qZRT98mrXeL3D0aQ-a6mEC80IsnBSXAFfPhlY7763XD1oVfLHVcK4QyfzAKM9pZQswjuWHXw8im9QCUKEr8rIb0zDy8wEijxonsYWu_aLx3wBz11QythccZO2YFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ade9a5ee.mp4?token=pbhJEHUnXaFVudX9wnFFLY0AnrRo3hzEcV-olx1okH9XJSdZ0SvmikvIvf_jjtQNaYGuVGtxUnZEhwSFpBpwIZGxjHzrMQrCOYeafm3AZ2FToeC_WYeXXtbqIt0AFs05ZFUu0za53UNr54CmwZnfprNcpERD83PHAPCysXFoKdwfjDYX4s_EjT17XOpNxkqIzb1vIsB-tHFIMrDDbfW_FSwrJyRzmVgj10-UTmkBYlcPMnG-qRagzh5qH2XBwR0Vy5fgbu2-Vf-8cYjt8GrmaGiYEFgJiySSZrByqxffIBS_xeiOdHgt8VmeiUHVlnudABSWv9SBRmM7iHwFxtrxjUWdQYb9KzwFO4JGKC6XJY9kt5wAK3kt6y6STVfc9bNhgtokcA-r7UJdzu_c_aOXV3lkUvcwZ7psVltrJbwgpcTsIyYEEp2_w-F4Xv08tHnVLDg_STXXhB0EFyi88yiqNj8KVb1tsqqDJxIJ-Bql0xqfzQKQPDOk0j39q7eMQTFbIPLO3TKUlM7aji7sINO5bZUbu1TMTUAnEhA6y_ExdPXpp23qZRT98mrXeL3D0aQ-a6mEC80IsnBSXAFfPhlY7763XD1oVfLHVcK4QyfzAKM9pZQswjuWHXw8im9QCUKEr8rIb0zDy8wEijxonsYWu_aLx3wBz11QythccZO2YFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین سالگرد شهادت سربازان سیدعلی، شهیدان حاجی‌زاده و محمود باقری
🗓
پنجشنبه ۲۱ خرداد، ساعت ۱۷ الی ۱۹، قطعه ۵۰ گلزار شهدای بهشت زهرا
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440879" target="_blank">📅 11:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440877">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efad1994eb.mp4?token=Ja3YaFk21c9Dx_zl1R2xEMa3V0SlKregF11XwuBkbjQ0l9Nxi0u6MQNJlqxZ0UGdFkoe3gKJWpTVIWL6tF79SmMPBNNeNpZhHMz75b6CNW-dTNVKM8m-imlRmM8XEd2x9gVstHvCOkHtaxXcWfIQoim7MGSPbFRJe3TTSh8ZEfhrrY73jFVMrZMfFaxfduQhC00470cgjYFs0Emhf0J4g96Hta7tRPcp5MNHljhGQ66QP08xNnLEsPlWIvvGa1cNCI2_e0V_SEb9ud-uLn2grHvbyx5-1jaIMY9ZsZQI6rxKzxiIS6PBM8FzsvNLWwN36CI_slzlw8tsDfOZfoCPUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efad1994eb.mp4?token=Ja3YaFk21c9Dx_zl1R2xEMa3V0SlKregF11XwuBkbjQ0l9Nxi0u6MQNJlqxZ0UGdFkoe3gKJWpTVIWL6tF79SmMPBNNeNpZhHMz75b6CNW-dTNVKM8m-imlRmM8XEd2x9gVstHvCOkHtaxXcWfIQoim7MGSPbFRJe3TTSh8ZEfhrrY73jFVMrZMfFaxfduQhC00470cgjYFs0Emhf0J4g96Hta7tRPcp5MNHljhGQ66QP08xNnLEsPlWIvvGa1cNCI2_e0V_SEb9ud-uLn2grHvbyx5-1jaIMY9ZsZQI6rxKzxiIS6PBM8FzsvNLWwN36CI_slzlw8tsDfOZfoCPUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رژیم صهیونیستی باز هم خواستار تخلیهٔ شهر صور شد
🔹
ارتش صهیونیستی دقایقی پیش برای ساکنان شهر صور در جنوب لبنان هشدار تخلیه صادر کرد و الجزیره هم از حملات توپخانه‌ای این رژیم به مناطقی در صور خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440877" target="_blank">📅 10:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440876">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سخنگوی شهرداری تهران: با توجه به شرایط موجود در کشور، استفاده از مترو و BRT در هماهنگی با شورای شهر تهران همچنان رایگان خواهد بود.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440876" target="_blank">📅 10:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440875">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5b736132.mp4?token=T2PUQv9dSHV0DZx3NbajuYMrBAG_BwVAxKoEzlQxQVMCR0MXAgxc69osX8oQZqEd0qZS-yCry61vVPGThipSiM8y-T8HaJyZ_YhzhJ4MXi-kzaSRxTXGgJIk2pYXUbMxUdsYTqSl2vr2PL-2y55wJxTKGV43rLvswlJduiKfP8Umbt2S4Xh2I7X3yhPjBMkgT5aqlElYtUWuvVirz8ZG4QI2JH-F96hu9WllplWWbGszUXeF9HMZbqYXprQiUF4lieB8aVJGx1YYYAJeI9Q-Jgp9uHp7YtSuAzoSOCP3H3mVn_yVB4lBv-a6BHfVoxdLT-yXHmBU5-0y8cWk6hZZeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5b736132.mp4?token=T2PUQv9dSHV0DZx3NbajuYMrBAG_BwVAxKoEzlQxQVMCR0MXAgxc69osX8oQZqEd0qZS-yCry61vVPGThipSiM8y-T8HaJyZ_YhzhJ4MXi-kzaSRxTXGgJIk2pYXUbMxUdsYTqSl2vr2PL-2y55wJxTKGV43rLvswlJduiKfP8Umbt2S4Xh2I7X3yhPjBMkgT5aqlElYtUWuvVirz8ZG4QI2JH-F96hu9WllplWWbGszUXeF9HMZbqYXprQiUF4lieB8aVJGx1YYYAJeI9Q-Jgp9uHp7YtSuAzoSOCP3H3mVn_yVB4lBv-a6BHfVoxdLT-yXHmBU5-0y8cWk6hZZeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قوه‌قضائیه از توقیف بخشی از املاک علی کریمی خبر داد
🔹
قوه‌قضائیه اعلام کرد: با استعلامات صورت‌گرفته از سازمان ثبت اسناد و املاک، برخی از املاک علی کریمی که سعی در اختفای آن‌ها داشته، با کار پیچیدهٔ حقوقی-اطلاعاتی در استان البرز شناسایی شده و ۲ واحد تجاری…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/440875" target="_blank">📅 10:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440874">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌ فدراسیون فوتبال: اقدام دولت آمریکا در ندادن ویزا کینه‌توزانه و کاملا سیاسی است
🔹
در آستانه آغاز جام جهانی، دولت آمریکا در ادامۀ اقدامات کینه‌توزانه خود علیه تیم ایران در تصمیمی غیرورزشی و البته کاملا سیاسی از صدور ویزای ارکان مهم مدیریتی و اداری تیم ملی…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440874" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440873">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxpK_yjjSXeERaZjDT7M2z19A4gjqcUfGX4ppg2fM6HGxwrs1bt3s0cin7I0zi41nxbmf8zUFNz6YjjSMOS7IAhvJ9qDR4Len0ZgneFo_XRs_0-dKa5N5lksGcw7LwIQXCzyd4IqIp5Z8TQYdO46i_qTb70Q3gFMnnintdPuO-rPJBf5gCMJZ0Oz2ytkP5Q-b-Yxey6Xa9C7GzbG7eInWSysCLW9F0zTI1mNIhrdYJ8hE6VbicYW0zIdQ55aHev-ERyblgL2i6JzbhipaXyixhHXqrTmcUTF1bfcwiuK8LJauvHX7mmBGv8gtPNOkgVV6jqQ2ICbXvnLd3YHsEq-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/440873" target="_blank">📅 10:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440870">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c45693aeb.mp4?token=HkhH_7lFqaIfUktlHKACKL4SVE-0-CsaWULHa9KsaZ7KRXgCXdSvBAN-ivD4q2rGTuk9AtjzG-fVp8a1uNREQz3aCWgzvkOyoAKd9N6xNjH8FKEPH9QsvwiB4WlpzIkcyFTwlVglSQAjWJdiW1py3Wk7mJHWAvDzf2p1HY_v3Q2Vl_psW-Q4S5BNo6akmre_RqSr--jqbZRG6deGXUZeea9hwVzjxh7nj-xYWwC0qTAEMAj9Hv37OaGoJazhZ2MY7KhDiKZs6T1rvKwt13GjAjF_3Vr4d9cThrFKVslP55ogRizbIxry6tDae8zmgJfhKALLJCPH6azYkeD6IR6W7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c45693aeb.mp4?token=HkhH_7lFqaIfUktlHKACKL4SVE-0-CsaWULHa9KsaZ7KRXgCXdSvBAN-ivD4q2rGTuk9AtjzG-fVp8a1uNREQz3aCWgzvkOyoAKd9N6xNjH8FKEPH9QsvwiB4WlpzIkcyFTwlVglSQAjWJdiW1py3Wk7mJHWAvDzf2p1HY_v3Q2Vl_psW-Q4S5BNo6akmre_RqSr--jqbZRG6deGXUZeea9hwVzjxh7nj-xYWwC0qTAEMAj9Hv37OaGoJazhZ2MY7KhDiKZs6T1rvKwt13GjAjF_3Vr4d9cThrFKVslP55ogRizbIxry6tDae8zmgJfhKALLJCPH6azYkeD6IR6W7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش ترامپ به هو شدن در داخل و بیرون ورزشگاه: فکر می‌کنم تشویق شدم
🔹
حضور دونالد ترامپ رئیس‌جمهور آمریکا در بازی سوم فینال ان‌بی‌ای با واکنش منفی تماشاگران همراه شد. زمانی که تصویر ترامپ هنگام پخش سرود ملی آمریکا روی نمایشگر بزرگ سالن به‌نمایش درآمد، حاضران در ورزشگاه او را با صدای بلند «هو» کردند.
🔹
با این حال، ترامپ دراین‌باره به خبرنگاران گفت: واقعاً عالی بود. فکر می‌کنم بیشتر تشویق بود. خیلی بلند بود و بسیار پرشور.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/440870" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440869">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47eae22ebe.mp4?token=k5Yn3eT3xzCWEGXTOLmZFIefbrbj0CJyQKISch4EbO5ooe_0wsoIJkAwNhGfl3J_YGHLjLHM0JxSl2VQ_mMaoqcjJJc2zCe_LucU445PW10lgCmzsJ5piiUypiqtUOTOzrZEaT1XvX2KT-8YubNMH0GSa8of02cA3nrw1BSio1H6qAQVNnroBI4IYggEiLS5zyUcj_kG3uy-sZuNHTPr_DVg6ySgcyjY9V_uURD-sraDQS2H4GO0IH6ZUccNLD6GU5hsHqnA_FacVSTJiJycFyhOJRaP3tRMbV_8bfuykJ-EsuVLbE3RlCr9PKjJkzmy9NdYsInrrIh8M-GdE5Bd0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47eae22ebe.mp4?token=k5Yn3eT3xzCWEGXTOLmZFIefbrbj0CJyQKISch4EbO5ooe_0wsoIJkAwNhGfl3J_YGHLjLHM0JxSl2VQ_mMaoqcjJJc2zCe_LucU445PW10lgCmzsJ5piiUypiqtUOTOzrZEaT1XvX2KT-8YubNMH0GSa8of02cA3nrw1BSio1H6qAQVNnroBI4IYggEiLS5zyUcj_kG3uy-sZuNHTPr_DVg6ySgcyjY9V_uURD-sraDQS2H4GO0IH6ZUccNLD6GU5hsHqnA_FacVSTJiJycFyhOJRaP3tRMbV_8bfuykJ-EsuVLbE3RlCr9PKjJkzmy9NdYsInrrIh8M-GdE5Bd0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلم دوربین مداربسته از درگیری خواهران منصوریان با مسئولان فدراسیون ووشو  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/440869" target="_blank">📅 08:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440868">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
سقوط بالگرد نظامی آمریکا در نزدیکی تنگۀ هرمز
🔹
طبق گزارش نیویورک تایمز، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/440868" target="_blank">📅 08:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440867">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2030c628b3.mp4?token=SR7iOkm8EI4Zgrb6Dz1Eo92clrq6U9V7P5U0E4nmQrwkw6WEyW19QgtzbjLMEC_nh_UYzLnln5ACjaDn-bOtzueNqMI4JfBeao6_j1T10QMoVGQsv_XtageGnBV4WZDTK-msd7shNrFPt9AvzvY9RSxw_wHiDGqwemMXNRXf9aymLrlVTRVvdVYw0rm1FXDdGNs-b1xgH9kproaVUDwzSd2elbT1X2gZpUGKRUqOAzaDFKYTSRJpytjxdrO9f3kn2WiYPehTH6lmI4o9-SzXGwwRcEUc-ffkx20Gbq17MnVdCu12YFvDS5Dn0wBpFldKvHl9ohA1IrOBwNMUFuuyOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2030c628b3.mp4?token=SR7iOkm8EI4Zgrb6Dz1Eo92clrq6U9V7P5U0E4nmQrwkw6WEyW19QgtzbjLMEC_nh_UYzLnln5ACjaDn-bOtzueNqMI4JfBeao6_j1T10QMoVGQsv_XtageGnBV4WZDTK-msd7shNrFPt9AvzvY9RSxw_wHiDGqwemMXNRXf9aymLrlVTRVvdVYw0rm1FXDdGNs-b1xgH9kproaVUDwzSd2elbT1X2gZpUGKRUqOAzaDFKYTSRJpytjxdrO9f3kn2WiYPehTH6lmI4o9-SzXGwwRcEUc-ffkx20Gbq17MnVdCu12YFvDS5Dn0wBpFldKvHl9ohA1IrOBwNMUFuuyOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افزایش ۸۰ درصدی قیمت مواد شوینده از دی‌ماه تا الان
🔹
مواد شوینده در دی‌ پارسال ۵۰ درصد و اردیبهشت‌‌ امسال ۳۰ درصد گران شد.
🔹
چه عواملی باعث افزایش قیمت مواد شوینده می‌شود؟
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/440867" target="_blank">📅 08:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440866">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz0jsqR9VQ5yrWYvgjhWLNPv_zddZ5dmcfsN9pZRl1k3fpu7EM8yD20h_KChFk6pzUCnY_yZZRujiPXR9YKZwLxZk_K6b_ZtCwYZCPLSTeHL1mTFyiU2dn4Na9DVMojiGUFvhOhnQJkxy-7J8SIxYIJFIGVdPPz9nhSnJINLeDyeTRVUSiMBSAWR9_MKCKMGs63-vlevp1KinGw2SlQ_7j-0APb9J3uuHzJx06pObM3BLNcQOmcd1p_2bO8T8lxRTB28zUqVVd-TkAKbD2ivzvXEincBic62SSC-Ysi2SRE_kWZAv32g4PtIuR1YIB8FdMk0iJm3aqdOH6_B37CPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی کل سپاه: آفرین بر شما مداحان، شاعران و هنرمندان متعهد
🔹
۱۰۰ روز از درخشش بی‌نظیر ملت مؤمن و شجاع ایران می‌گذرد‌. بعثتی الهی که جهان را شگفت‌زده کرد و زورگویان مستکبر را در مقابل ارادۀ ملتی بصیر و مقاوم تسلیم کرد و ان‌شاءالله پاداش این ایستادگی بی‌مثال، گشایش و فرج برای بشریت و هموار شدن مسیر حاکمیت قسط و عدل بر جهان خواهد بود.
🔹
در این حماسۀ ماندگار، ستایش‌گران اهل بیت و هنرمندان متعهد، از ارکان اصلی حضور با نشاط و شورانگیز مردم بودند.
🔹
۲۲ ذی‌الحجه سالروز شهادت تجسم عشق و ایمان و منادی برجسته آزادی و عدالت و ولایت میثم تمار، فرصتی مغتنم برای تجلیل از این سربازان سلحشور سپاه امام زمان (عج) است.
🔹
آفرین بر شما مداحان، شاعران و هنرمندان متعهدی که در حماسۀ بعثت عظیم ملت ایران صمیمانه در کنار ملت خود بودید و عاشقانه پای آرمان‌های قائد شهیدمان ایستادید و شکوه و عظمت این قیام را دو چندان کردید.
🔹
حشر با حیدر کرار، امیرالمومین علی بن‌ابی طالب علیه‌السلام و جایگاهی چون میثم تمار نصیبتان باد.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/440866" target="_blank">📅 08:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440865">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شهردار نیویورک: ویزای یک‌روزه با روح جام‌جهانی تعارض دارد
🔹
کارشکنی دولت آمریکا علیه تیم‌های شرکت‌کننده در جام‌جهانی باعث شده تا زهران ممدانی، شهردار مسلمان نیویورک به سیاست‌های ترامپ انتقاد کند.
🔹
ممدانی در بخشی از صحبت‌هایش گفته، صدور ویزای یک‌روزه برای یک تیم (ایران) برای شرکت در جام‌جهانی با روح جام‌جهانی تعارض دارد.
🔸
هنوز جام‌جهانی آغاز نشده میزبانی آمریکا به دلیل کارشکنی‌ها و برخوردهای تحقیرآمیز زیرسوال رفته و به سوژۀ اول جام‌جهانی تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/440865" target="_blank">📅 08:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440864">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
سقوط بالگرد نظامی آمریکا در نزدیکی تنگۀ هرمز
🔹
طبق گزارش نیویورک تایمز، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/440864" target="_blank">📅 07:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440863">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_AjxRS0h4ZqXbhxzZ68KmCyhwu6Xf-fgXaWDdeLUnpljBPMZya1nLh7KA07afYzdlYK2zk2g9tAul8XkWvkpgK0sl1sSwJ_3Q4g30Te79PkmMqmkBNbzjpj-Hthd8dcR_fzSR5MRFNZcLfenrwxhcvX-jC2drHGI7xTg0er8ot3BE5wSNb_xlRI3ivHM14S4MgYB50jIsZ3egQbG5rnUfehjfH395nm35dyIozNQjNJRv5ui6D3p8dcGpD_nIvZnvmBkUtPocus_kCXcVWYbw8LEOzgAAUa0TO9aDRtdisJWjE8zoo8C_x_q6PwHXTShJKVNoIuLFKhUyox8Sc4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح آمریکا برای بستن راه‌های غیرمستقیم تأمین فناوری چین
🔹
قانونگذاران آمریکایی با هدف جلوگیری از دسترسی غیرمستقیم شرکت‌های چینی به تراشه‌های پیشرفته، خواستار تشدید نظارت و گسترش محدودیت‌های صادراتی شدند.
🔹
نمایندگان کنگرۀ آمریکا معتقدند برخی شرکت‌های چینی می‌توانند با استفاده از واحدهای ثبت‌شده در خارج از چین، محدودیت‌های صادراتی واشنگتن را دور بزنند و به فناوری‌های پیشرفتۀ موردنیاز برای توسعۀ سامانه‌های هوش‌مصنوعی دسترسی پیدا کنند.
🔹
این درخواست در حالی مطرح شده که دولت آمریکا طی سال‌های اخیر مجموعه‌ای از محدودیت‌های صادراتی را برای جلوگیری از انتقال فناوری‌های حساس نیمه‌رسانا به چین اعمال کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/440863" target="_blank">📅 07:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440862">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رگبار، رعدوبرق و وزش‌باد شدید در برخی مناطق کشور
🔹
هواشناسی: در شمال استان‌های آذربایجان‌غربی و آذربایجان‌شرقی، اردبیل، شمال زنجان، استان‌های ساحلی دریای خزر، ارتفاعات و دامنۀ البرز مرکزی در استان‌های قزوین، البرز و تهران، شمال سمنان، خراسان‌شمالی و شمال خراسان‌رضوی در بعضی ساعت‌ها ابرناک، رگبار و رعدوبرق و گاهی وزش‌باد شدید موقت پیش‌بینی می‌شود.
🔹
در شمال شرق، شرق، جنوب و جنوب‌غرب در بعضی از ساعت‌ها وزش‌باد شدید و احتمال خیزش گردوخاک دور از انتظار نیست.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/440862" target="_blank">📅 07:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440861">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ادارات البرز از امروز با ۵۰ درصد ظرفیت فعالیت می‌کنند
🔹
با اعلام استانداری البرز، با هدف تسهیل شرایط کاری گروه‌های دارای شرایط ویژه، فعالیت کلیۀ وزارتخانه‌ها، سازمان‌ها و دستگاه‌های اجرایی استان البرز تا اطلاع ثانوی با حداقل ۵۰ درصد کارکنان و به‌صورت حضوری خواهد بود.
اولویت دورکاری با چه کسانی است؟
🔸
افراد دارای معلولیت
🔸
بانوان به‌ویژه بانوان باردار یا دارای فرزند معلول یا فرزند شش ساله و کمتر
🔸
کارکنان دارای بیماری‌های خاص
فعالیت‌ بانک‌ها چگونه است؟
🔹
تمامی شعب بانک‌ها فعال می‌باشد.
🔹
مدیران شعب می‌توانند با حداقل ۵۰ درصد نیروهای شاغل در شعب، روند خدمت‌رسانی را ادامه دهند.
چه کسانی از این بخشنامه مستثنی هستند؟
🔸
تمامی رده‌های مدیریتی استان
🔸
واحدهای عملیاتی دستگاه‌های خدمات‌رسان و شهرداری‌ها
🔸
مراکز درمانی، نهادهای نظامی، انتظامی و امنیتی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/440861" target="_blank">📅 06:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440860">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPcMC5R9TCIr644V-0l-E_NdyfrXSn2hIePAPiBkhg0t3YBJR4VaoejWhHKxceGzfxGx4HDReTaDOzdHCrkBMYsRjnXeSnCo1DMxR0ndjNC817UbQYsMHNTsk2FjAksi_Q1UUtRpTmvaqASBvNFL4QZEfttdEnl45p-BCE2cGcsVgTFIrqclVmSonBK_-vUJPQUDxzMFLuGqotW3iGhLnzRI1H9AaNI5CqFwhy8HBAvaMA6w4SVciK27iOAsBCpmjc0rxHSmeEBp29QOtvlTcS-dnwPPWC7CrqHl6r8WJQ-YY06Dsjd7FvcdU5AO2_0OwEncErdCNDtQa-jYQqnBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سوپر ماریو گلکسی» اولین فیلم میلیارد دلاری سال شد
🔹
در حالی که هالیوود هنوز در انتظار نخستین ابرموفقیت تجاری سال ۲۰۲۶ بود، «سوپر ماریو گلکسی» با عبور از مرز یک میلیارد دلار فروش جهانی، نه‌تنها این عنوان را از آن خود کرد، بلکه جایگاه مجموعه «ماریو» را در میان پردرآمدترین فرانچایزهای انیمیشنی تاریخ تثبیت کرد.
🔹
این فیلم که محصول مشترک استودیوهای یونیورسال پیکچرز، ایلومینیشن و نینتندو است، پس از پایان اکران آخر هفته اخیر به فروش ۴۲۸.۵ میلیون دلار در آمریکای شمالی و ۵۷۱.۵ میلیون دلار در بازارهای بین‌المللی دست یافت و مجموع فروش جهانی خود را از یک میلیارد دلار فراتر برد.
🔹
فرانچایز «سوپر ماریو» یکی از موفق‌ترین و پرفروش‌ترین مجموعه‌های سرگرمی در تاریخ جهان است.
🔹
ماجرای این شخصیت نمادین در سال ۱۹۸۱ با بازی «دانکی کونگ» آغاز شد، جایی که او با نام «جامپمن» به عنوان یک قهرمان ظاهر شد تا یک گوریل بزرگ را شکست دهد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/440860" target="_blank">📅 05:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440859">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65515e97a2.mp4?token=hDdf7rf4HnsQwwQj_ePFsNn6yYtFBwHQwD4G5DsBWLg3qRIzoDO1lJPHStTi-EiBVusv4jQ9JxhtFsD1UpNfR1TS--STk8cM__8Xdy9dyc7ursU0JrgLVr6vcs5bIQwbrJLgt6K-yFG7VrluJc2ChMrEvEwwQgE5P0ONGoHKUKw6eEYPi2ofab_T045EnJYVF8jJ6--oNLJ_CQbSyLM5hLJFJyvFGsm_zhOdHdvDJuGBZMTaEtNxmaHYhg4uKl0-WdY7pRFXYHM5X0q5oC4VebAPNt7T_tpvk4bcHSI43hH2AqKQo6vkqdtoi9LuY6mLy3ZvL9RsQp1k2VoW2WUk_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65515e97a2.mp4?token=hDdf7rf4HnsQwwQj_ePFsNn6yYtFBwHQwD4G5DsBWLg3qRIzoDO1lJPHStTi-EiBVusv4jQ9JxhtFsD1UpNfR1TS--STk8cM__8Xdy9dyc7ursU0JrgLVr6vcs5bIQwbrJLgt6K-yFG7VrluJc2ChMrEvEwwQgE5P0ONGoHKUKw6eEYPi2ofab_T045EnJYVF8jJ6--oNLJ_CQbSyLM5hLJFJyvFGsm_zhOdHdvDJuGBZMTaEtNxmaHYhg4uKl0-WdY7pRFXYHM5X0q5oC4VebAPNt7T_tpvk4bcHSI43hH2AqKQo6vkqdtoi9LuY6mLy3ZvL9RsQp1k2VoW2WUk_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پدر و مادرتان برای خدا حساب ببرید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/440859" target="_blank">📅 03:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440858">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بانویی که تعمیر پرچم در خیابان را نذر امام زمان(عج) کرده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/440858" target="_blank">📅 03:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440857">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انصراف تیم ملی فوتبال امید از بازی دوستانه با بحرین
🔹
تیم ملی فوتبال امید ایران که این روزها اردوی آماده‌سازی خود را در آنتالیای ترکیه برگزار می‌کند، از شرکت در مسابقات دوستانه با حضور بحرین و چند تیم دیگر انصراف داد.
🔹
گفته می‌شود این تصمیم در واکنش به مواضع و اقدامات برخی کشورهای حاضر در این تورنمنت علیه ایران گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/440857" target="_blank">📅 02:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440856">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVoM3kt6KNiizgMLJlq3fI-1Jy4USllI-HGB2gfWoIMwnacXOHv6JoVRmCp2gZq_c4DQnBBlYd0hGr5jDhPfck9T8SVx6QcIFWR6FskDPbD0WgkfTSU9nJqhfMyOBqG8G0PC8IqA_YQ7InJWow9ZattqwOMl3j4RfUEU4IxcZshA11_kPdCNQ2O8XOkZNf94bx6wVG42NBOblnDH_7uwRrv7uS-i7BSTEFWt2EDfPn8NOWw8CSulcvy0SibRH0Z30qUOgUwHmQFflNfEI5JmDgpNGer0a4GHfyAONjmrGxCCDz8YC_euw8OeIIfThFhRox4URXojWlPs4b8LV6LLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی داور افتتاحیه جام بیست‌وسوم
🔹
ویلتون پریرا سامپایو، داور برزیلی قضاوت افتتاحیۀ جام‌جهانی ۲۰۲۶ که از ساعت ۲۲:۳۰ پنجشنبه بین مکزیک و آفریقای جنوبی برگزار می‌شود را برعهده گرفت.
@Sportfars</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/440856" target="_blank">📅 01:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440855">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دو شهید و ۱۰ زخمی در حملۀ صهیونیست‌ها به شهر مروانیۀ لبنان
🔹
وزارت بهداشت لبنان: در حملۀ هوایی رژیم‌صهیونیستی به شهر مروانیه در جنوب این کشور، دو نفر از جمله یک کودک شهید و ۱۰ نفر دیگر زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/440855" target="_blank">📅 01:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440849">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cG5Vl6tPPBl24xgZDgetfgn0-_tNO6JP-30tDntI5EEbhQ-KtJ2_iTSzcCS2jcYOM_Jkd4mRUu8L4LVNx4wiA8P704LChCKRZ8TWtp92SqeZZgT9OdC_qZ5qzAJpugqdeLSU_PzgtEwcU_qkzDBCaSwqIXxx426cUhfSKE8vtOZzktRp0lOdmw5GJcS-5Ur_VrrC_kuGz7Tq25bxaDcKg1VtPvoInxQNdQIQskXO_9MUPyRIz7A4bkRQxfJX2L-yRbQe7miN7yifQ3qyBBypSM-rdf6inqTvl_DvcsZctYRmClW67pHsvd8IM0m2NKoaD9Ey8NyGU2Xq1Wwc-yyGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iq33YrChoPVv1ReDVBLcH19REjnrsn1vA_XAeTkKTNN3Vn_qCW9SXAadGY_ZAXpAVCM7K3uLdZoyQgk1rFW1JBnwOupiUK_Kjy0GoWI_0t_eGiK76tmUzmh0MqoWsOYl01UNObKAzCjLT4f1F5f_MkOO8TF2d2KiMeQTsPr0CDrwM2VyDJqlYKbg4v7AcyS1wEdyHJaxph8B7_JuFbgxKlBZB_dpIlQu46TtefF8ATZ5PnIDqC1IYmb1M8Dy5NTKqDGm2c87uwSqrRD3LuPaWdBfVOirspsXiSE1XkpAuOAt6sWAUwVdBExdJ7ZP7r_lYCjYjpXdmQeFUKE15ZR-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5L2XkrMBYyiUOD2K9gwjNvKuRTgEIPjMSk5G8HH3rQoHpVuKimHp8STGtlrCkGANFZ_Kfi-MnWqKmHC2GUXLSar115LfD16Q5mK7nd_2xQ9C0t80s86cX3xQfZ3EW111-YeLmyeTRj0L6PSC94sxIqC2rF1OidVo-XJhiw-oKlNnpC2mB0Vu5sQuVz-eBt15JoQrz45ivVFg7gdgj1zg_W4OdfmpfvA8EpacQpGy6WlsBqPZeuRTQMkMSVFgOUecO9wBO9LNcNuwYRbLhy-VPCXsfx4JUyAWDrfApQ2RJk3GDTCzmJerQccfPD3dHJ_n7Ug0DshGJ_FvSN29kT7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1auoFXWq5nMLPtuizv58mSYdwgPgvudsL67XQWoZOiqXiQy697-sZ0W671NCm8ltzL7un1sCN9zkP7lwubPoE7zvYW9WVDe2tsPtBYmNziCDPu_t04L-ms5AU1FxNYMgpsJe4jg9NLOARSkp09-Pbmlz2wq6GNTgN02eNqO7Cx8mA68PPZ3Z1Gg37Xued5XdRXVgdKj-eHANY9FdKM47YP-T-FBMAz6bWTug8IfymDnC1ODr0FKbSKjjUc4xDtdjJTQSLrZIS8RNpzn_Haz8onp6QbpNJtmrrvOVh5Bzd8jKd0T0U_0R-BsyHyDgGT5XVKjjZzlvN7iQQJkUtaFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a55EHGVRxgI6VShp5mgMd9-lZm5hMO9hsOKZPoSSQEEENMH4jORwEe8xk1kZ3em3dV2xCTa2DlJlTnRv9dN7O3R7JhTSzZYzWdiuysQeBr8IvVoq-agqmHzNx2aP0TozW5IrtJNy2y-sHA4XfIzVW1gwuLcClx5_dtEYAdnecYUJ1sHPDc3UK5I5lPDTiztn_fdPxTmK0I-rTDNStk6G32V9iTEnG-C70k_gB_YE09NyJQ1-9h1YlPRB20gTKsORN6RaIC3OaXYIIzoZwtdnW2KfLTCQJtMnhKBEps7cLIHmuXOFD5x7nkO6dmxn0AKQk8hfXfAT-xcI6QdbACtXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3sR6fX4cqp3GYFD-_KZEIHgsveBUJTJlZShnQTQiJJOjRi7aEmywlMl3YC61IEYi4odLWIKSZt_Zkvip-ehEEgCWTkkuECe5cYCd7vHc_2e60o6XVgPm9yNASRbkABC1E1A9GGlLpAJ4UeczooEEwpTa73V-ma59galXEUV5rhZ06zv5VqpH503w7sN_z6oBB-6G_4eO2EA0B57A1UqKTXNB1WLdgJqfi_VOLEQve5FmFLD7uTqlzwfLSwyy-njBqMROCS4HnzpfYcHPmGNuGWNZTSQiW8viMM8K694-HY2YByY5ccDzAd-X2OjqSs8u7U0_pgNYxlyGl-jSOgXRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۹ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440849" target="_blank">📅 01:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440839">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBskTveuduqiIPM3QS-Eam6J9ufhzOo2zRfam7MRlRt3KQGP-rDOTaDes29e_Z8DTYUWSJFJRfbilaILt2AX9DwTUWGAgzYI7SFaP8fnTv1oYN8SRqGkmIJJUbhZIwz1kC4QdqppZeH3ymzZuQcRbXRFNwYv6iylgYG_GVW9OwZfzkDdWhxNN9lwB6PM8Ibikdeb_1D4Lpg3x7s0UyTay3eZC2DclVfz3MR9Odbr8ZqqtFXlUzkD2tz-6ErmRcjuAn0nbQ7l6S__7TXv-4Z4Bczqwl3qduuMxYp3n-oK7kyX9rSa4MAtHviLBPt2WBkcjlZDtA5ogdW7213-DyOieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dheJq2bzTrdx0pwbEnLG5wCz0w7-nXJRMO-IHoyEg42jF5Qu1fQuEttBMeABxaqOfI38XLVUzpAB9ox8q4K2oeZnn8JqpWDWIi65I_XR2RcqQxwCK4FgY5-MaZTwSSK1d4qDLj0HXZtLiMhOHQ5GvN_iPh-8n6X_14YeHSGEwWsTSV6s7QfaemwDRXbAGN-MC7zkhTtRLad7KHGoyB4YrMH-N76lTppgMwbJVkRnkvHUjh4G7aDx2U6uV501U9QAj5XJCzKh2g_W6UBFavBclAS24KpGGeFh81GRVjXbOIhCxfvKWHjxlouwhlEdFr_9gTQfFSElgRsAU3EvdJ9BvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAaxdalgoye4Ubj8tpeY3FqVPXGzrL2qWIYXfMiL0o38UTteCWlzHKdklqg62PlzK24_hzoN4_mP-5zx9Vmfzs2_hnCNdApo48uPu2Wci62MDzKLL5_Ba9ZoMWNTsBwFULgImglwANRyOIMXm-HNC5vSQGsqGcGP0xlgg8TQrV8EVuz6I3uP9GgXAHlFNrPr6Dt9cjWzTR85h--YUKPrb_ersUddFnZkDRFzaFvk5pd59pc1MqR3FOzwFAWKc5_NLq_v4TEmawFH6Xx4Zz_Q0pE10w6b-LybJMpb3vooQ0ReN9OWieSNjwON_c-He0RarYWWj5UjjxzrapbuNMYTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFpBhWFp1AJxFD6-4gxBjd7b1dEZLuDqI7-lVJ3ajOatPs1rrXPPFQ2SEKVQuBOd4GgiCoRMsPomx0RAGRbSgTgCvtdB88eFXSeW-ky7wxdnB5zVFuBqsCEKM5ml7HmZicb3rIUDuuWMwQbkV5bxkykpDBgMxxNp1GVF2IoVcm_s9H9YosTz5tFc3L5zxxCzdRU4k_GppOktChWu2DMqiucDXIjhiIW1q1lxocyYT-Kq8LDGrFHK57FNE5T9eBb5YM2mVcYmyNUEjCHYflfY0oyQDKCtbAA47S02P5lanwktigxtwqVeLTotmEkYH-kM5yyNhO9IcWbILcc0CMvqLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CafUiww7SE9TcwzIKChRPQIwviV_nFJ9OdqF6QrV8nxZP77f76hoyZ969BE4zgPfhCRmXiVMyXV9JqTchU384cV0H8D_wKRhXmOd90Z8h2YXJ43rLEGhylp1RjfLAPqNUzI28hKEeQWchUVB4Ld8Wg-crvKE8n9I17t471oZGvzG5Gd1c2u2JiilBB4XB1Dk-qAev-vxM1W01hvd07tuoB0vWowgncEER8hNHHw-foY-9Ot7CGQVKo6yFONHK91T7DW54sgKA-0ko2P-1QQxWKaBqpDPdr7fdHYlA6O_5c8zmvkEz9vegNGpsxk7wTDPpCexGLwl0J44EJ1P7PEUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNQxqUr7EwsH5Su9qWXw37QQedV8eH_w8s67x6ccMmLEFAIRRLtC21mN01BaPBQ7Nv1mUJBYSMuV0wkeQprf_40JCpD1efpWBGQ25QJ4sLlAqU09fe0cGREZcuYSvRP46jHtf2gjkiwpLYck8J52hXcN47Nm409otuiJHyOx4oV2x-MgkaDVESB6R4RCmHyP18uPbXB_3TMIjJmv1HadEJHLZk5uLimn53FvvSAq64O15hFdBCnlQ5GSB17j7Wh7JUFO3sl7wj3RiKUo48Wtgj5hQRMXNg7XHZwERRFfwSGvkKaiDNPvwNE-9_ykt6h20D77m--NGb0t0zAI0sY56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBMtSYGnwU12XwRb3OQvLmkdhr2-cA4QMWGZjnz0BqlUe7-8ToOW7dAPaDYXmyV-cTrkbEz9JX04DdK4O1OiHr4DCTv9dRGVtLXR9vA3Rdw5St7qA14PRe-KGv5piHXNhgKEDyngim0iQM2oW46eOv10gyZYm3KfPV4QuEXywdScYvOam08IeJUYcpEuJKLC_VoQLwkhtMl539GqLSKFN2_9Ql3URNC2-0pW9JMZZrhHpQIopk80ryEaxcw5Uy0BgYJvYHB2Kt6EXrAmbcJwrCPKYRf2zztyGN_B-icR3xPqk70-4dlIM1WFjLq2yxwyn1LfDMD48oWIlbGZszHISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhaU2-l4RigxY2bjX4WN3qT50QdIqJQw9RrCS6b-tiHLCeUKdrLffDFirUf25PKsk55bBXvY__zYVg0Rx-OXsy7C5MR0mDC0t7nJF-KfP-tQ-3Xk__AyJ_3DH6tzsxYgS6uz7z8P6a5KmJ6adL3lSVjDsCTui2LSL8m487iig6k-WZmHh5a6NxiNZdTTWAPK1SqC12j1Q-WHs0lXkcE9mfCjNBD1Zjtado0jvUzpeqWNIMhY8Mbzq8YIk0mWR9wgN7uUa1SWn0nmC4Rpqbm8vaClMpylw7JWhUnevFShV5u5oJj4gKsI_PQnzaPHoPKuVGPIblhyg8o7UMkRVjoK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4_aS-0_6yl3mf0r0axTq52W9lGe6Ob-FjiV1LMNd5Sqb_qIwog2PbHS_VoXq2wwu6bbHouHGcTPt9TXT5Bfyh6F6VXK6daBqEkaznBlIMuOmXPyvYlkT83REyHYkKRWxeA-kvkLxcrdM-HEgaYaB6gi46jMhbw9rKi1OW8oSnucFc9CeSfTssxgff8QYWEwjcJkBIs-KF_W_lD7wKC6SaVBkH1cSm94aHPR6kDTPD1gZoPGO1vVnH-dOm8fZDP0IXDoKwlDv8BsQ9ffxC820uL8aAN65eIC-ZldToRcqiA0vmtTMv2vBBB5fKnXHTtc0UHaRkhlGYHZKusyqH8BIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_A7JXmorJ4laGcOHib57OjUXGM3sX6uyU8Hh9iHF2DGLX62yVAW2dEAhxWz4DkQgf0_zC7MT6sjbhDQgBXaHMFWT4Z6Vo-0xpDCSbvGb5U2joTSnMWxiIszsrtfVp0z-TO-mQXhbseJN-d29Aez9GB-8cuBlPnWK38Wui9vIMgm4oxszzeTKFdFmJWVN9Yo2I3LukJ9iBbAMZ_Vrpl3uPCgHwMQMC8s6F89eqr3q1zD4D8pfmnBG6jSj7NzoiYA8POqxM7IX13PQ6bYoSi-LkPyCA8nyqMaOhHfgOSZIAyzqRnpHMNHbTXlrOK2y_5x-tHO6KTX81TXE1bqhilU4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/440839" target="_blank">📅 01:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440838">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7e4651d4.mp4?token=lCiEzbAOnJNyc9bytMUAP37QRJVpCozv4Qj9uQwxuW8M3z7qqcDF5QdoHIrWSJh623PuZJORPsA0vbNpUh8Xx_YF8TUu0PCffhRSkpN3GrbqVzp-7LBCMD4rh04Idf6EFcbArb19uPCTje2rHJFlSWnfubjYeeTeg2Y2u8s7VCjqXmVMvqdxYZtJDfFuOtjjKfg321r4ECpqjdOCmbgTv4Gt9cT71ZIoptUPO5AfJ3mqvjeP9JizxVq1X63G_EB313Px2NFjcHUrvJwI3RqTtcj6M5YOAXLX6RvsVtwlw2lzPr2jMT-S7YwRivs4NPsEof6OVEw7NmVK30u7LQPIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7e4651d4.mp4?token=lCiEzbAOnJNyc9bytMUAP37QRJVpCozv4Qj9uQwxuW8M3z7qqcDF5QdoHIrWSJh623PuZJORPsA0vbNpUh8Xx_YF8TUu0PCffhRSkpN3GrbqVzp-7LBCMD4rh04Idf6EFcbArb19uPCTje2rHJFlSWnfubjYeeTeg2Y2u8s7VCjqXmVMvqdxYZtJDfFuOtjjKfg321r4ECpqjdOCmbgTv4Gt9cT71ZIoptUPO5AfJ3mqvjeP9JizxVq1X63G_EB313Px2NFjcHUrvJwI3RqTtcj6M5YOAXLX6RvsVtwlw2lzPr2jMT-S7YwRivs4NPsEof6OVEw7NmVK30u7LQPIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بقائی: افتخار به دزدی اموال ایرانیان شرم‌آور است
🔹
سخنگوی وزارت خارجه با انتشار ویدئویی از اظهارات وزیر خزانه‌داری آمریکا که با افتخار از سرقت اموال متعلق به ایران صحبت می‌کند، با اشاره به فرازی از نمایشنامۀ «مکبث» نوشت: اکنون او درمی‌یابد که جاه و مقامش بر اندامش زار می‌زند؛ همچون جامهٔ غولی بلندبالا بر تنِ دزدی فرومایه و کوتوله.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/440838" target="_blank">📅 01:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440837">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">زمین‌لرزۀ ۵ ریشتری بخش‌هایی از استان هرمزگان را لرزاند
🔹
زلزله‌ای به بزرگی ۵ ریشتر و در عمق ۲۲ کیلومتری زمین، منطقۀ سرگزاحمدی در شمال هرمزگان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/440837" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olZ90u1XiHHhYrFoZv2OHc1x3U2bNvp6XXKq_TfBJlNcbxA4HToMNCpNR7bcwb-UtYblxWBlv7DI078baSS1mLDjsAmTUGYQvF7uzqLdePHXU_iz4Qi3D5QynEIHGc6nJI7amdFlIg_dVBQRsW7Ol1aL-vJJMq5xkAuNO8KgITvqL4lK52NNkeyDFAelTj4ntgl6IC_hwmdBxQPARVga8helHodmYT0hyKfm17v1mfRl3VJ4WKBVo1LgicjTjBbMq4MIgZoU_4Bgy1Bqw2O1nQxm9bfQxp7muHWMEtthh-Tb9G0gy01pw-7rAxlrfi6gvQRUF9b7pUC5GCvdNouXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط و نشان ایران دربارۀ مذاکرات با آمریکا
🔹
شبکۀ الجزیره شامگاه امروز دوشنبه به نقل از یک مقام ایرانی گزارش داد که آمریکا تغییراتی در پیش‌نویس تفاهم‌نامه ایجاد کرده و این مسئله قابل پذیرش نیست.
🔹
وی همچنین به طرف آمریکایی هشدار داد که هرگونه نقض آتش‌بس می‌تواند بر مذاکرات تأثیر بگذارد و ایران به‌صورت جدی با آن برخورد خواهد کرد.
🔹
این مقام که اشاره‌ای به نامش نشده، تاکید کرد اگر آمریکا پول‌های بلوکه شده ایران را آزاد نکند و به تحریم‌ها پایان ندهد، هیچ توافقی حاصل نخواهد شد.
🔹
وی در پایان گفت که برقراری ثبات و امنیت در منطقه فقط با وجود یک سازوکار بازدارندۀ واقعی در برابر تجاوزات محقق خواهد شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/440836" target="_blank">📅 00:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae82c887e8.mp4?token=pN2nIUinWQnIlVk7XE4nlMtQu-MLSLNL9FKJ6rKpgp7yCPB9rHg22f9eMVtdIppiGpmH8vEiF2ZGqXSO6yyX2l7thyn_dI4vOYVi3f2Y_EyCyHbEsdhcP2C5jVJPDCo8xTYACg4ZH-5eZf5Dm7-BrdejTs-I2wRAKPzQo_YlPKVuBLM9AgE7uh_vjyen6BBCJk70zsqhvrnwl6BcZ0iJrL-3GNPPw7W7T3g_kvBSchiWs2qU7aFI2g7lR03xkHZg_I9miJyaqkQm9BfSRUZ1JNUVmuk_YHlRbVi5dRaLEckzcnezAGnTjHrrI5VcmXXj8b8IY1bhpHHpLgShOFUxtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae82c887e8.mp4?token=pN2nIUinWQnIlVk7XE4nlMtQu-MLSLNL9FKJ6rKpgp7yCPB9rHg22f9eMVtdIppiGpmH8vEiF2ZGqXSO6yyX2l7thyn_dI4vOYVi3f2Y_EyCyHbEsdhcP2C5jVJPDCo8xTYACg4ZH-5eZf5Dm7-BrdejTs-I2wRAKPzQo_YlPKVuBLM9AgE7uh_vjyen6BBCJk70zsqhvrnwl6BcZ0iJrL-3GNPPw7W7T3g_kvBSchiWs2qU7aFI2g7lR03xkHZg_I9miJyaqkQm9BfSRUZ1JNUVmuk_YHlRbVi5dRaLEckzcnezAGnTjHrrI5VcmXXj8b8IY1bhpHHpLgShOFUxtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا خوزستان؛ ۱۰۰ شب حضور، ۱۰۰ شب ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/440835" target="_blank">📅 00:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کشف تجهیزات پشتیبان هدایت جنگنده‌های صهیونیستی در جنگل‌های تنکابن
🔹
مجموعه‌ای از تجهیزات فنی و سامانه‌های زمین‌پایۀ مورد استفاده در پشتیبانی و هدایت جنگنده‌های مهاجم، در ارتفاعات جنگلی شهرستان تنکابن در استان مازندران کشف و جمع‌آوری شد.
🔹
این تجهیزات در یکی از مسیرهای اصلی ورود جنگنده‌های دشمن به حریم هوایی پایتخت مستقر بوده‌اند.
🔹
این منطقه در جریان «جنگ رمضان» یکی از کریدورهای اصلی ورود جنگنده‌های اسرائیلی برای اجرای حملات علیه تهران و مناطق شمالی کشور محسوب می‌شد.
@Farsna
ـ
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/440834" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۵ شهید و ۸ زخمی در حملۀ صهیونیست‌ها به شهر صور لبنان
🔹
وزارت بهداشت لبنان اعلام کرد در نتیجۀ حملات هوایی رژیم صهیونیستی به شهر صور در جنوب این کشور، ۵ لبنانی به شهادت رسیده و ۸ نفر نیز زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/440833" target="_blank">📅 00:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBtJFch8rw1uXT3EOQ0fLVvhTxk4BbAERNe1deMOeDAIEV0nML-C96cvHpcppFVxvySsBYS1kcR6AMioxTULkeD4SEmjzm8uW166cEiHrizMhMfb8txaD--PFqmXlrc_HBr0c0zuJLkZbS0VC4ZXuPuSnUYJnO-pOISwJTAoULqSYYyLynKWHr-aYaGDdnaZhqs_r2kl3ctLGe-p1uktnZA7DfBFJ5H8RbH4uWQJvdrA5yWPB43rK6S0C8gmn78CIf6hJaOvPHEGbHRotUPdxodMEmTUv8rQFMLC1VrJffiRzfyLxnhJ2Gd3bXhrISD8jpj0vp8WULcYz2ZvnD17Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
فرمانده هوافضا: حضور در خیابان را تا زمانی که رهبری اراده می‌کنند حفظ کنید
🔹
باید با پیوند زدن «میدان، خیابان و دیپلماسی» عزت و اقتدار را برای ایران و ملت‌های آزاده فراهم کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/440832" target="_blank">📅 00:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da8c2c141.mp4?token=tf-WdP8dOZW5SD_wQH9OdDQ7PFYtLakOsYVTxCS5HfcXyEbpYL2lUABRNVgsmyzvg4snpjD7nLq6Pm0g2MeO3fbrKh8-DeSuMuBlfw8CFO_sZtnu7GrkPl91sb9h1f569yvLNhd4Df8r2WEv0Nzl4yTIDrsivdwFE2NziopM7_KLGLdlp9KW3pQRHEgnpyDjgeKS5_SLEUrtgHrScaW6RkZ70KNO41lS5iKqS7KYI12g-iwB8VRj7uEEaWHuGvtxOqz0oIODM0bEKnGNXcy1YPd_J5PEPtvYgFtACS-Pt_lwsvg8Gmr7_8fwl8CE1cSRNOeDlGNOOkVbvuHesCA7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da8c2c141.mp4?token=tf-WdP8dOZW5SD_wQH9OdDQ7PFYtLakOsYVTxCS5HfcXyEbpYL2lUABRNVgsmyzvg4snpjD7nLq6Pm0g2MeO3fbrKh8-DeSuMuBlfw8CFO_sZtnu7GrkPl91sb9h1f569yvLNhd4Df8r2WEv0Nzl4yTIDrsivdwFE2NziopM7_KLGLdlp9KW3pQRHEgnpyDjgeKS5_SLEUrtgHrScaW6RkZ70KNO41lS5iKqS7KYI12g-iwB8VRj7uEEaWHuGvtxOqz0oIODM0bEKnGNXcy1YPd_J5PEPtvYgFtACS-Pt_lwsvg8Gmr7_8fwl8CE1cSRNOeDlGNOOkVbvuHesCA7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس صداوسیما: سرمایه‌دارانی که با امکانات کشور در امارات سرمایه‌گذاری کرده‌اند باید این سرمایه‌ها را بازگردانند یا اموالشان توقیف شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/440831" target="_blank">📅 00:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
برخی منابع از حملۀ پهپادی یمن به اراضی اشغالی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/440830" target="_blank">📅 00:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd2299f3a.mp4?token=tYuZNiZWCEaHv0CSy2WvVXeYsVtpVAD-YNNE3AllW3tcuN7avwFt_PZoYD2reahr2bdRsLYdtMTfz_jlr073lAr6jDtnbvR7et5Q689PHut49cGVPsQk0qzTwyi109bP38ltiRjJvsdVWNHG8iQQDcQQ5KY7MFIn7I1n3Au4GbTNerE1--whQKEIETpS1e7WzA7sBl9l4qEKBFpyKoWPGuPuQaJsGaOgEyEfyucENjzOKAuGQhBD4-qBdFqwqZIzHVndnktMk4YCTF5Z7kxzn0X0LwqGgHZfO9YEQZbJtpJKLX94ZFZ3e9FY0tieg6AiFncHvRE2_Y4O_L6WzKoK4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd2299f3a.mp4?token=tYuZNiZWCEaHv0CSy2WvVXeYsVtpVAD-YNNE3AllW3tcuN7avwFt_PZoYD2reahr2bdRsLYdtMTfz_jlr073lAr6jDtnbvR7et5Q689PHut49cGVPsQk0qzTwyi109bP38ltiRjJvsdVWNHG8iQQDcQQ5KY7MFIn7I1n3Au4GbTNerE1--whQKEIETpS1e7WzA7sBl9l4qEKBFpyKoWPGuPuQaJsGaOgEyEfyucENjzOKAuGQhBD4-qBdFqwqZIzHVndnktMk4YCTF5Z7kxzn0X0LwqGgHZfO9YEQZbJtpJKLX94ZFZ3e9FY0tieg6AiFncHvRE2_Y4O_L6WzKoK4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«می‌مانیم پای کار وطن» شعار صدمین شب تجمعات میدان انقلاب تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/440829" target="_blank">📅 23:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440828">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfLapd-0FKoTbXyXLxg3eys1dPiEcx0tFu07uKdgCyKropjdTuIlMGFGSaj26URwdkK9IZB-kHAbzRTn2hnYbGMBrtLLoAkffUbW1xFTJqCgIqtU5euncTfnXYppEDKAkGe7iq9Jj1cB42URyYFdrrYLWqop6MwlPH171O0CsPozB37HYoLq6ZGY_jVVOEjumYE3Y97aLfrBAOE1MiYPQDgIepYVrCJ2GgaipazezUZb_zxDtkE7Xj-KEciu0YCUgDKMecKOJaNbfKjEr544PLI-snrP5XbCDBQdgLQ8v2_KtUdpPKh3wyTZCpofPWOIWJ-9sk3GTt-L4gRI-Ztj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کنگره خواستار تحقیقات درباره حمله اسرائیل به کشتی آمریکایی شد
🔹
توماس مسی، نماینده جمهوری‌خواه کنگره آمریکا، خواستار تحقیقات جدید درباره حمله اسرائیل به کشتی یواس‌اس لیبرتی شده و خواستار به رسمیت شناخته شدن بازماندگان و کشته‌شدگان این حادثه شده است، مسئله‌ای که به گفته او ۵۹ سال است معطل مانده است.
🔸
به گزارش الجزیره، امروز سالگرد این حمله است و در ۸ ژوئن ۱۹۶۷ جنگنده‌ها و قایق‌های اسرائیلی در سواحل مصر به این کشتی آمریکایی حمله کردند که در نتیجه آن ۳۴ تن از نیروهای آمریکایی کشته و بیش از ۱۷۰ نفر زخمی شدند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440828" target="_blank">📅 23:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440827">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اطلاعات جدید از کمک‌های اردن به اسرائیل در حملات علیه ایران
🔹
یک منبع نظامی در گفت وگو با فارس: بخش عمده‌ای از حملات موشکی جنگنده‌های اسرائیلی علیه ایران، از حریم هوایی اردن صورت گرفته است.
🔹
جنگنده های رژیم صهیونیستی به دلیل جایگزینی تجهیزات راداری و پدافندی غرب ایران، در حمله اخیر از «مهمات دورایستای هوا به زمین» استفاده کرده‌اند.
🔹
همچنین بالگردهای ارتش اردن نیز در عملیات رهگیری موشک‌ها و پهپادهای شلیک‌شده ازسوی ایران نقش حمایتی قابل توجهی به ارتش اسرائیل ایفا کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440827" target="_blank">📅 23:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4970268c70.mp4?token=Y8DwexGw-e4MiWm11dVWkeKiU9Un2hIWi5HMxkl-qnvhK5HSWDzjGAFOAa4nAvq_RyrvD8Q07L0vsKHr5cgC0jsbyv72-Im8Qt0PpXmWu7xNUtfp23M21CcHoSCALt1UIOnDJqTLMcMDcTqUVVwkutBrdeaoASahkVylj3lOVh-OaWlqyWAYr8-QMrtxCNo8cY7XyFItNXJRlVLWnXbbzvw7vKCZjv-TkQ-M7uLg6QYAQCIlrqitREJ2TUQPIDs0C_J00aw3NzCBz_lvheYLcVjiKQ9XrwhMuXM9Rw5u_PhLpgEf3xYGJ27tZ9jiNFTTUBu_Hx0lUoVK2a9F77IO-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4970268c70.mp4?token=Y8DwexGw-e4MiWm11dVWkeKiU9Un2hIWi5HMxkl-qnvhK5HSWDzjGAFOAa4nAvq_RyrvD8Q07L0vsKHr5cgC0jsbyv72-Im8Qt0PpXmWu7xNUtfp23M21CcHoSCALt1UIOnDJqTLMcMDcTqUVVwkutBrdeaoASahkVylj3lOVh-OaWlqyWAYr8-QMrtxCNo8cY7XyFItNXJRlVLWnXbbzvw7vKCZjv-TkQ-M7uLg6QYAQCIlrqitREJ2TUQPIDs0C_J00aw3NzCBz_lvheYLcVjiKQ9XrwhMuXM9Rw5u_PhLpgEf3xYGJ27tZ9jiNFTTUBu_Hx0lUoVK2a9F77IO-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپاد شاهد پیام‌رسان بوشهری‌ها شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440826" target="_blank">📅 23:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440825">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mqe0-Uom1FKiJUJrXmcvPJGOb3JEm0Dm-62uaTT971GO1T2jDVmNEC2aZN03Bstmoj70aDcqk9bpl93f3czhPoH4ItvN5HicSXr1MK2sqA0R2p7PfPh14N8-rstCm8obOCyG6uS8-Q_Eg_P1Ymmk_DyJVNXhCl_u-hujGbWsEEFwF4ue8NCbWWUfPFxGSdM4TwWqXoWB5Rx141SP06K4k_I_WL2N1_kShcxD6HgnBYpCFGTN7Ol5Xkb0duVJz4DcphfKq-0xkFrUbW4fDdeQl0W3BzH2ydD5YvHjth6o3ZtiiRD6c2uxSqyYIG6jwKVgUGgO-geRExpXO9ghO2hUJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما؛ از اتهام سیاه‌نمایی تا رپورتاژ برای دولت؛ نظر شما چیست؟
🔹
رئیس‌جمهور و برخی از اعضای تیم رسانه‌ای دولت، معتقدند صداوسیما نسبت به اقدامات دولت «سیاه‌نمایی» می‌کند و این را در روزهای اخیر صراحتا بیان کرده‌اند.
🔸
همزمان، گروهی از مخاطبان نیز از تلویزیون انتقاد دارند که مطالبات مردم دربارهٔ وضعیت سخت اقتصادی و مشکلات معیشتی را به‌درستی منعکس نمی‌کند و اقدامات صداوسیما را به «رپورتاژ خبری برای دولت» تشبیه می‌کنند.
🔹
از سوی دیگر، دولت بخش عمده‌ای از مشکلات فعلی را ناشی از جنگ می‌داند؛ اما برخی کارشناسان و مردم معتقدند در کنار تاثیرات جنگ، بخشی از تورم و نابسامانی‌های اقتصادی ریشه در سیاست‌های پیش از جنگ دارد.
🖼
نظر شما چیست؟
اینجا
در نظرسنجی شرکت کنید
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/440825" target="_blank">📅 23:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96edf34919.mp4?token=TFjudCmvCWgvOrL2oDhhczsDL0INHtOSK8cWh4Kp_j9kXK17fGTK3SEXjPkoKR1pzoMDTbWo6vtyZG3krOfj2dxXXf_qNWVzED2Ltz-vPFD9MXJsAnNwAlTwfpafsypz6hjgp5ZDNIBCr64xhzkZwY4t3flFfclB5Agw4CJxqs734iNDArqg8shL8mP_QpTNreqQGPrdBhP-cpwBG429jN4JoYSeUJMA3JxUzvzg8D36ir3GGzy6MT85wAjg5J-mbnhqtTi4v6H9bSBbsPlV-fvZwapEzJb9LsBG5Gg2NPsxWSnHXwTginBYY_ykz1tPVdTEVYpxz6KkCiw-rfzZkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96edf34919.mp4?token=TFjudCmvCWgvOrL2oDhhczsDL0INHtOSK8cWh4Kp_j9kXK17fGTK3SEXjPkoKR1pzoMDTbWo6vtyZG3krOfj2dxXXf_qNWVzED2Ltz-vPFD9MXJsAnNwAlTwfpafsypz6hjgp5ZDNIBCr64xhzkZwY4t3flFfclB5Agw4CJxqs734iNDArqg8shL8mP_QpTNreqQGPrdBhP-cpwBG429jN4JoYSeUJMA3JxUzvzg8D36ir3GGzy6MT85wAjg5J-mbnhqtTi4v6H9bSBbsPlV-fvZwapEzJb9LsBG5Gg2NPsxWSnHXwTginBYY_ykz1tPVdTEVYpxz6KkCiw-rfzZkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علویان طبرستان حامی جبهۀ مقاومت
🔹
اجتماع شمارۀ ۱۰۰ مردم ساری با شعارهایی در دفاع از شیعیان لبنان برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440824" target="_blank">📅 23:46 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
