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
<img src="https://cdn4.telesco.pe/file/iBBnj6TmPR_opyBQUkrk1K27OUvrgYHEsBE8EcfElK7up-zrRZrGEORGCE8oT0_UQI_VVqVv4CkOHE7ixwpsxDkOOV7YAcOaumtR4tz2aMLuR486YVaS1uUKidGNZNfPgtvxlhZhYRT779hIMhEeag55ztyoMBN1xmexdjO26p2SfddNYJtTnYC5aMXMrU09AZynoiVbEG-WYGm3tkJnFp7-3qt1iw8J1Hm8rFKsxbFo5jOCTHpI4ZK0DlFtYXVx-wFAFde5Yfc20yrzpRyWgYCHtjZwvc2_hzjZ_NpmH4ljWOzm0SAN3xwv-SAxCxB9OIKsgGY6_owvYgAGjqe02Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 13:43:38</div>
<hr>

<div class="tg-post" id="msg-677266">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
فرمانداری جاسک شایعات تخلیه شهرستان را تکذیب کرد
فرمانداری شهرستان جاسک:
🔹
وضعیت در شهرستان جاسک کاملاً عادی است و خبرهای مربوط به تخلیه منطقه صحت ندارد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/akhbarefori/677266" target="_blank">📅 13:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677265">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH6hKrjQmBlgVO-iWLxZFKfXQDIolO_144c18__dYgrGykHFZs6YeuYj6-H-p4ryAHai3PUC_cjRdmGjBTSzdOzOJtX-wtZTfa_RWA6c-rGi0wLQrk822HI17vLnTAi4V1vmeIwypMOVe5P3PDuVBmwcbL2ugfpGiRq5tOuRf_c1rvxyhzVGJ7CrUbmt3zivmw3UauuxgQhby84oV2QrVayCLqDf_0pFvCHGtVSHSY1fk0TKF74GU0l_Tjr6eVoS7nbjlBDFiTsQ_23-Ae-kcfiEsNZ80twOzOOXHZiEXxFGX-u77rjaX8ZdFUfESDgOlqcq9h7WrmjWfujTb28VWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
یکی از زیبایی‌های اربعین، همین عشق و پذیرایی بی‌منت مردم عراق است
▫️
با رعایت چند نکته ساده، میتوانیم قدردان محبتشان باشیم
▫️
به اندازه غذا برداریم، غذا را هدر ندهیم و قدر محبت کسانی که برای پذیرایی از ما زحمت می‌کشند را بدانیم.
🤍
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/677265" target="_blank">📅 13:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677264">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20563fa6a9.mp4?token=R3BVetR3F0L3TZi19t1hzuMWcEWdz4rnLJChuHxH4fpJESy3e_3iwI9w7falrQvR61FuKuszSsc6XgVvgOlgLwCQBu1FDwYYIe8RSCni1mo1u-AuRLOW7yHIryDVz1LfdGm35ohV9qCtdL8OwlZiMdfQnSfsl45CmZB3vIM9sT4rBQYfqS9XCTZh1wG6x0H988g3Eh5H37sZu7S7p02Sgb9bDkia3Wj23kvAJvYsPZR4XsshcLR4et2fJFmI800lcdbfjZZLNzKR_LLlS8n1rHejLpCjHFMx3TXdKprRgVaEnhdc7L_A91ck8RBGGSlzFsoYDcSYfCFKFlngyxDRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20563fa6a9.mp4?token=R3BVetR3F0L3TZi19t1hzuMWcEWdz4rnLJChuHxH4fpJESy3e_3iwI9w7falrQvR61FuKuszSsc6XgVvgOlgLwCQBu1FDwYYIe8RSCni1mo1u-AuRLOW7yHIryDVz1LfdGm35ohV9qCtdL8OwlZiMdfQnSfsl45CmZB3vIM9sT4rBQYfqS9XCTZh1wG6x0H988g3Eh5H37sZu7S7p02Sgb9bDkia3Wj23kvAJvYsPZR4XsshcLR4et2fJFmI800lcdbfjZZLNzKR_LLlS8n1rHejLpCjHFMx3TXdKprRgVaEnhdc7L_A91ck8RBGGSlzFsoYDcSYfCFKFlngyxDRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج پر دردسر علی دایی در بزرگداشت اکبر عبدی با هجوم مردم/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/677264" target="_blank">📅 13:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677262">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrLpri7Yq18WJUqEmSl0nMz7LgcIRqn7HTR7tz2AccgrUpizt_ZzC2ctscMroToLKLPpAZt31SiuGdK_YyYF3WSW71v6h5d93o_QZypfRloR-UIZxy984NVFpfOqwCTHpLHvfwYcFoyw45LwZarxxTJkS8p03w3LrWiuw75kSfc6s0CwoGf0tkFXkgO3l423MCKHGwnrnqSXHttKdp_lN75TVQb1mWkSZ5ylbYCXcjdVCiXyOYB2ZcSbJVWdZMKK-uMMua1MF6rlBCogXo-B0tkAoP1UStq8EcT_Pl_0FLqS793kG3ts-TVSO-szcz2s33o3wjDoDRksLR-tt-Dt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عجیب اما واقعی؛
بازیگر «کلید اسرار» که پند و اندرز معروف بود حالا تحت تعقیبه و جایزه ۵۰۰ هزار دلاری برای بازداشتش تعیین شده!
🔹
چهره‌ای که سال‌ها با نقش‌های اخلاقی و پندآموز در سریال «کلید اسرار» شناخته می‌شد، حالا به دلیل ادعاهای مطرح‌شده درباره ارتباط با گروه FETO، در ترکیه خبرساز شده و گفته می‌شود برای بازداشت او جایزه تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/677262" target="_blank">📅 13:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677261">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
خودربایی دختر جوان برای فرار از ازدواج اجباری
🔹
دختر ۳۲ ساله‌ای که خانواده‌اش مفقودی او را گزارش کرده بودند، سناریوی آدم‌ربایی را خودش طراحی کرده بود تا با دریافت ۵ میلیارد تومان و مقداری دلار از خانواده، به پسر مورد علاقه‌اش برسد.
🔹
تحقیقات پلیس تهران نشان داد ماجرا ساختگی بوده و انگیزه او، نارضایتی از رفتار خانواده و مخالفت با ازدواج تحمیلی بوده است. پرونده پس از روشن شدن حقیقت مختومه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/677261" target="_blank">📅 13:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677260">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b270a75bf.mp4?token=gCCV5t3j_S5qSbaEAFNcU1phnMwrUQepXYGpp2pr6pBqMgREJV8Y5vrPnOlKa3BIXh_rzNM73Obx0TKYJP0qNrCHgtNfPgks0W-3CdTqzKr0MBBmJsPriL5eM1w56OEagNUtcRdW3NDvVqufTqkqJ-MmRZv82xCxJPQ-KB3NZUlDz1o2_zmbCgUtFQpgeXWKDxX4SkqQnQLo8KT5W4JDrqUqP6ZeTdvr2ZHsofr671PBBqxL4eSlbh9AEVjcpIa5TIJ7VYL4qBzi3q-aj23qts-WsfIc9_WsiBxhnKVctOJFZC2tlRa1FG7eROMjLVlon7lFDExbMJx45maQYrs-IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b270a75bf.mp4?token=gCCV5t3j_S5qSbaEAFNcU1phnMwrUQepXYGpp2pr6pBqMgREJV8Y5vrPnOlKa3BIXh_rzNM73Obx0TKYJP0qNrCHgtNfPgks0W-3CdTqzKr0MBBmJsPriL5eM1w56OEagNUtcRdW3NDvVqufTqkqJ-MmRZv82xCxJPQ-KB3NZUlDz1o2_zmbCgUtFQpgeXWKDxX4SkqQnQLo8KT5W4JDrqUqP6ZeTdvr2ZHsofr671PBBqxL4eSlbh9AEVjcpIa5TIJ7VYL4qBzi3q-aj23qts-WsfIc9_WsiBxhnKVctOJFZC2tlRa1FG7eROMjLVlon7lFDExbMJx45maQYrs-IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظامیان اسپانیا مانع ورود مهاجران مراکشی به سئوتا می‌شوند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/677260" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677256">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGfcWRYmEChx9FOiMyzlEiVsPzKSG6PBstppquJA_W25x3_xVQa0sIkg3xTF7CXAbYA1KPEJmbxQJxaEVIWu1pfEd1vt_FELflCoxOGGWkCepEom68-zjiBPKWRu8RfX8OKataQBl9I0EqijhPX4naMqxLKrUGLjOcVtUBvmjVVj5sqpZt3wZjQ5V-z3wpB6JwBJmxIOUhT1YU1cw76XJUvYULkYgBfL2Rnpx-07ESqeDvG7sasxzB69mY7kpCic44PYGHsHPckqcVi8eH_B2xtppk9BS-KyWeRj-qFauKQ0jVm8xw3xQourNUpYejgbI87zMtMMvFPP0bAKHT7OFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIbXFQ1QnyN-WS8qCdNSYWG2Hap2fvnkDOAD-0bK0gEDDGePbpRoH35FBJq485oApX5MR1-ZmjBxMv0WMLOwdt1Z2pnVRr7-i6H0SdNLYQNNu6zN_66lp2u6gHOlzPKRvTkeqjM_ZxAAUgYUJ4LNKXUAJYwJ7rfRs_5JXIDGxvgUaxAvOB0YigGeWcnkIEjBKrQph0DbtuVXTS6y_0BuYLUX4IzHC27psHqFPhgH0TXvq20TfWeKz2UQxf3j_Tx7KLW4PP6FYeXDvu2Jh18akK7INElNw8GK1pSXB1RtdG0qOD6H69qhp3TSoAaHLwriTTNq6kia99Bep_IhK4hZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9WU4woSD30R13p5xl268nFJQwP1EGyEsybfzFJYEC2Kve9WImx7sJ4qOdHmzLlmCgjOpXeWiIOBF7BP6nhw5D9KUFwQGtW0pqoAUPQa54CKbtxDRHKhX6IBMmn_Dti1sz1YSJ3CbNw7TyF-4KYCH-tK-S7twSFHf2YLRr9Y5KtUm_bNJTbj_ybD_bqghUZGK0GTjqXUQBz6gAr6MyNeRaTgDvvx9cb4HBQKekF8VNmajzfobYJNAgZjNjcwerIbcVkf3kzc3brw_bHQHkFPpZCy8uSE9HLs1PzHtpK1bDf1WMtAhcX9-P2fj2nAton93TWRWZXOikjhzsQ1MDnhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuZMFkp6S0RxBT7506AW3dzgpLd6D-5nagr7FXGBMpL50YlZ2Clnr06-USI0aWCNRqgsuM-hFIDmCI_ABwxGjAuDuy3g9W0EsEobjsYD-5xEVJUHNut2xdqkGQq5EK3iP0zG1MTVsrnV5LkIRmgHuTpWReOh50xJzwpcag_qJRhLLwI1HXpREIAWmfXwWPI0UVcsRb_iINmXfT-Z9HWQGMce2eHdI2qIoiwd92BSpG8rEA7JAcxco5grtmBQQEmO0l18-nkm8m8o93rJFbZb_SHHDpClSP9nzSPHIyIC7GhUrMKDL79e2pqkRC5UJLQaQI2KX1XSco46Y-bC08uSSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اکثر افراد نوع اضطرابی که دارن رو نمی‌شناسن‌، با این پست نوع اضطرابی که دارین رو تشخیص بدین #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/677256" target="_blank">📅 13:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677255">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
پلیس فتا: انتشار محتوای خشونت‌آمیز و تحریک‌کننده جرم است
رئیس پلیس فتا:
🔹
تولید، انتشار یا اشتراک محتوای تحریک‌کننده خشونت، تهدید، آموزش اعمال مجرمانه یا تشویش اذهان عمومی در فضای مجازی جرم بوده و با متخلفان طبق قانون برخورد خواهد شد.
🔹
شهروندان می‌توانند موارد مجرمانه را از طریق شماره
۰۹۶۳۸۰
به پلیس فتا گزارش کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/677255" target="_blank">📅 13:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677254">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdtTq3IQpVLfzRDODN6aAU8nDo2PirQw_m9eN6OCGd-eZTIwRlNRYQUgBy25PDoikjRdM7MQnpalvQLnt0TDPtpvsQkZPFxy_Rb7q_o1Q41Wq-VLZ5NYPRr92qOu7BK1dElmTqFhe71FqQ_i_91WuaYjzVTv8FR8PfFWRPlAxSLyXySe9lyb1ShVzzmLcFEn0z4GUf8tKq0cKbA-FJNo0aTlYs2SXqe-rGGVOG9fizMirkJU1haeu5sBPnkat4L5OLY0_J1qtalUD0eWdQlhPWmm3BPRaQ76y0mj0JF1aFuvoRbiFvjGu5cnSprbUhA6UdMuvGenf9XyxsDoqAhDrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه فاکس نیوز با انتشار نموداری جدید اعلام کرد که از موجودی ۲۳۳۰ موشک پاتریوت ایالات متحده پیش از جنگ با ایران، حدود دو سوم آن مصرف شده و ذخایر این سامانه پدافندی ارتش آمریکا به حدود ۸۰۰ موشک رسیده است
🔹
همچنین مطابق اطلاعات منتشر شده توسط فاکس نیوز، نیمی از ذخایر سامانه پدافندی تاد آمریکا نیز مصرف شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/677254" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677252">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fcbbd55ac.mp4?token=dg9qj2g3kVid33sKwMJuKXusYNpZ1h7EqM5GwTUBoWIBk7ZlEvw2iWqg0jCAQuVA_WiYmDpns67Z8p4XtxtaXrBal0UmzzhzTRqM1f89Ycft1OZtjKQPtsiGvxaF6MTx_ZlNWgIakg2lUGLA-yzRhUpXAGMsSSvAQGdrPDwIS_Ckc9cc7axBi3iog2c1WA9OMgEZ6kM8rwbS98NnLWVGekysv6_I2AZmKJ9d-4FBFBPjktm8_U64YMTlZ60ylATNF8x99N8XyYaZMq8ZkIIEzuwEdm0gpFphWctL-gMldwMr-rPeY3k3V15IJF0xRcC86u0IwdKk7H6L6nFkuiY0NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fcbbd55ac.mp4?token=dg9qj2g3kVid33sKwMJuKXusYNpZ1h7EqM5GwTUBoWIBk7ZlEvw2iWqg0jCAQuVA_WiYmDpns67Z8p4XtxtaXrBal0UmzzhzTRqM1f89Ycft1OZtjKQPtsiGvxaF6MTx_ZlNWgIakg2lUGLA-yzRhUpXAGMsSSvAQGdrPDwIS_Ckc9cc7axBi3iog2c1WA9OMgEZ6kM8rwbS98NnLWVGekysv6_I2AZmKJ9d-4FBFBPjktm8_U64YMTlZ60ylATNF8x99N8XyYaZMq8ZkIIEzuwEdm0gpFphWctL-gMldwMr-rPeY3k3V15IJF0xRcC86u0IwdKk7H6L6nFkuiY0NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/677252" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677251">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-text">🌟
وزیر نیرو از اعجاز همدلی  می‌گوید...
🌟
روایتی از اعتماد و ایثار مردم است که در سکوت خانه‌ها شکل گرفت و روشنایی‌اش در سراسر ایران ماندگار شد....
#قرار_همدلی
|
#مدیریت_مصرف
|
#پویش_۲۵درجه_قرار_همدلی
#صنعت_برق_عرصه_تلاش_خدمت
@tavanironline
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/677251" target="_blank">📅 13:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677250">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/It97SkczRQ0xmpCgGFt61TZIcuWIkcJQYnvBlvZU57aF3PKqxRglC7rNTQwtOKcE1E0OX-srmHeBZWYV_pdvA_YvBk1pcOgGM60GUMX7sNdvWIebg701F1cnqM6jp9eSeK6i4pXTElMCbujIScqwhsikhbrf8FwPhjmendTOwfSqykWIsDWydBNdg9EbsZg9-Ji5Vsa45NmYPHFP73rK3ext8MCi66O77C5hlmYAhj2PXR6e5T3uGQCAZQyZjKlO4KAJ04IfPcHarAWzBs0mmci-4TB_2waJkSjM7Jvg4vG7tENJNrrYCDPijRNFUkDBnw3DSI3xQxCj6mlqg5nlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۱۰ مرداد ماه
🔹
در بازار طلای امروز با حرکت در محدوده‌ حساس قیمتی، شاهد افزایش قیمت طلای ۱۸ عیار و سکه امامی و بهار آزادی بودیم.
🔹
قیمت‌های اعلام‌شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/677250" target="_blank">📅 12:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677249">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feed9248e1.mp4?token=RS9X86MQZsUBbfRup2zM4LJ_IjNm22OPodDmX3-t2cYbnp8stnH4h_DiXwvZDAqZ4ORZxUK4pQ9JBmlSiuekkF-UexLtZbK7QqSbuVd98_UrS38PWYyOhxKJJUUx4GZQqEsvpgPUo333vpRLVAJtTgPI7ADbinj1eFoYhIK3HxUBZUQpDF3_fAD25ui9rZQ0f3_9Cg81avW15jkUPqXNCi37TtKwh3Gcqo4ZLIPdJim-2QaRVp6pIDDMBbNdsX0bURFq5H28a5LH1co_k8Aeie-gA337uB9dgQSWgd05otcBIKQbwEjaqKhExeo0BPd1FD2945csoru6sfjB8QWKm24MzOxzlB_nBj_BaysIJ5h0zrmxr-Hz9koN8FHCs7fzHft8aZ0VMZWP5vYemUah5WwdDv2kxIN2B4CqmYtfTWrrO6495-SvBzXmZoIOwFtXaCm1vC8h86e7jYCiKZTCzZqh2X0PTWAMo793iJNALZNTu8k2-pb0iznPaK6d6Sx7pjZ76VFs8v25o9Zwt2HGfQZ8mr6_55YCzWHRzVH106Hlbq0-KKCqbNgFFLgV6ec7QWM6LOkP1IEjK0JYsxAnOdDO62j2SAVEk6CKdaDR1gUkHNAqdC2e2ibxsDcnHmqRED_AKuGbHSjo55sYh7qFEwosjjT8aD-FdnRU938WtIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feed9248e1.mp4?token=RS9X86MQZsUBbfRup2zM4LJ_IjNm22OPodDmX3-t2cYbnp8stnH4h_DiXwvZDAqZ4ORZxUK4pQ9JBmlSiuekkF-UexLtZbK7QqSbuVd98_UrS38PWYyOhxKJJUUx4GZQqEsvpgPUo333vpRLVAJtTgPI7ADbinj1eFoYhIK3HxUBZUQpDF3_fAD25ui9rZQ0f3_9Cg81avW15jkUPqXNCi37TtKwh3Gcqo4ZLIPdJim-2QaRVp6pIDDMBbNdsX0bURFq5H28a5LH1co_k8Aeie-gA337uB9dgQSWgd05otcBIKQbwEjaqKhExeo0BPd1FD2945csoru6sfjB8QWKm24MzOxzlB_nBj_BaysIJ5h0zrmxr-Hz9koN8FHCs7fzHft8aZ0VMZWP5vYemUah5WwdDv2kxIN2B4CqmYtfTWrrO6495-SvBzXmZoIOwFtXaCm1vC8h86e7jYCiKZTCzZqh2X0PTWAMo793iJNALZNTu8k2-pb0iznPaK6d6Sx7pjZ76VFs8v25o9Zwt2HGfQZ8mr6_55YCzWHRzVH106Hlbq0-KKCqbNgFFLgV6ec7QWM6LOkP1IEjK0JYsxAnOdDO62j2SAVEk6CKdaDR1gUkHNAqdC2e2ibxsDcnHmqRED_AKuGbHSjo55sYh7qFEwosjjT8aD-FdnRU938WtIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/677249" target="_blank">📅 12:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677248">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8JFbkNmlQxc-FZwUwOU3k7Duno7bBdvtmeNtWOl4Pg_OOb6WqXr51t2wprf9X7qm25Qm_9JIviH_mQHDeojjpTMApwsMdR5cfY2weGMnqASNgD4g--tnAoKkoybmsfqKQI9inT1708FAJDjGAKr-PYvWrrnS7QahdnyyoNJYzVQUQAtJ1bUQqo4IU2Tm18ApFIV-Bb-qkdNBuAaMCzixRo2mUXhkeXeOU5QrkYFNFMrKaUfFI7TCXBBeYip96QPJPseFR_jIXPtJV-3Ns1x-xn0EzMFgr5o19yzgnQrp31Ubu1UaQx4xmv9f0lKzL2nQHXA4V9-yLROg0Mw2PFXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس: اگر به ایران ضربه‌ای زده بشه، کل منطقه و تاسیسات آن را به عصر حجر برمی‌گردانیم. به نفعتان هست که حماقت نکنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/677248" target="_blank">📅 12:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677247">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8jyEmA1BMFgskLB-xzZJOXp2u_RaOL2So7J7ZI0lNRZq_Qx3t0EtO0tCxRm4PqOaXzqENYc3Wr0YwY79BOP2FcYB2qTzoTIywKL9xfunFiRcRDezpkb9bAX1DiZIr1Jw2yYbuNcZbzAsCCud223ItjdpGSg8QzaJ4JovhfRwgXBUXV6QUQBMC-huzAwhJgxHhnQaOGwsJCXJR90FWAO-q4EdKAtgLYmItUeVRGyHzj7H3a3xr65g4JgHZ_V90nSqW83fRahcj6Id3cn4hgF3Tk3VQ92HP4JbMfLnR7u00T3tPYOAegXk2hgg-stZ8bBsmgAdbWg_Ez5PJkn5jK24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین پادشاه ایران در اروپا؛ سفر پرهزینه ناصرالدین‌شاه به فرنگ
عکسى تاریخی از اولین سفر ناصرالدین شاه قاجار به اروپا سال ۱۲۵۲
🔹
ناصرالدین‌شاه آن زمان ۴۳ سال داشت و بعدها دو بار دیگر نیز راهی فرنگ شد. علاقه او به سفرهای اروپایی آن‌قدر زیاد بود که تأمین هزینه سفرهای بعدی، با مخارج سنگین و دریافت وام‌های خارجی همراه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/677247" target="_blank">📅 12:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677246">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پاکستان به ائتلاف دریایی عربستان پیوست
🔹
پاکستان به همراه ۱۳ کشور دیگر به ائتلاف دفاع دریایی به رهبری عربستان پیوست؛ ائتلافی با هدف تأمین امنیت دریای سرخ، باب‌المندب، خلیج عدن و حفاظت از کشتیرانی و زنجیره انرژی جهانی.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/677246" target="_blank">📅 12:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677245">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b23215cb0.mp4?token=f_CohG_vYiWJQ-f8hU5zVsoEVzRmqRFzmxGrx1HkW1WaliADZ3IRt1KU25UZOH3RLNFPAa2tFMhPjtTjnYdioW5w3lahsep0kChHNXRFKxXQfb1XTtHzlV_lu0UDn-ZzJxtUkhntB1HSNSGYL3GWQ2ZBfS2-0gZBdZClg0klPF8IQkhaDIDm2iHs8IW-QgEBJ_LIukQmZ6TrwszG3FhTQ_zVjh-ZCezeBtgHD00qLXKAZXm95xWJ69_Id1nNh_k9I8AsC8mrjfdBc1peypELjB0ispQM-MnW_mKWYnErDdjpNjWHFNIKOaG0BwrWE1ueU3nVA_0pGEkg6SQ0eGfxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b23215cb0.mp4?token=f_CohG_vYiWJQ-f8hU5zVsoEVzRmqRFzmxGrx1HkW1WaliADZ3IRt1KU25UZOH3RLNFPAa2tFMhPjtTjnYdioW5w3lahsep0kChHNXRFKxXQfb1XTtHzlV_lu0UDn-ZzJxtUkhntB1HSNSGYL3GWQ2ZBfS2-0gZBdZClg0klPF8IQkhaDIDm2iHs8IW-QgEBJ_LIukQmZ6TrwszG3FhTQ_zVjh-ZCezeBtgHD00qLXKAZXm95xWJ69_Id1nNh_k9I8AsC8mrjfdBc1peypELjB0ispQM-MnW_mKWYnErDdjpNjWHFNIKOaG0BwrWE1ueU3nVA_0pGEkg6SQ0eGfxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
اینجا همه یک عنوان دارند؛ «خادم حسین»
❤️
▫️
روایتی از مردمی که با عشق، خستگی راه را تحمل می‌کنند تا در بزرگ‌ترین اجتماع عاشقان حسینی، خادم باشند.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/677245" target="_blank">📅 12:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677244">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpmtmSAuMYubfzyi1oSIZjfG0OKSE5BzcBze6HpbB9E0OfWSvADfKXIlAO9gZww-BypEboNifW37UDYfPtcvtLfDkS4W5ZZq4n-wxs-L8Xlg6dX3EgjNx2j9UsJDZNnY86BUoO7lvb-AvYe6UzTEe3nz-zElb03twc7cfSIjvPXLTruL5xy350pZxeexuPzvTZWWF3zd3kEy3hBhsyW3avPeuP51cpUx-sLz8ydHG-zgWshTFcH0E7x8ocZbkDwA28sa7mhrOsNTUEsUVJF1xLNjmK-YrNq9yNXII-UYTP2dfgO9DszViZ1798l34gCoombn1vjAd58DJmsoFRjZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانشمندان راز کوررنگی را کشف کردند
🔹
دانشمندان ژاپنی کشف کرده‌اند که فقط چند تفاوت بسیار کوچک در چشم، می‌تواند باعث شود بعضی افراد رنگ‌های قرمز و سبز را متفاوت ببینند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/677244" target="_blank">📅 12:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677243">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29cc88ce4b.mp4?token=cRYsPQDpHUvhLW4xi-219vp-oOGSrHo7iYDEvsDOFfUy7ypMaJnuVajGgWfcn232l9JJSbogztR8M2gr3ZCwfhuxNP5fYMofGK6vQvmwJdBTxTjjjokikt5j5fJDs8bik5UjFBz_NMh9GFLuiagKDWnBSbcoKpRBrJlzs8aEeV-O0Vzp0W1F76z-l_f-w3VH2JQdD9ohtgxGnqX2jInH5kGdAxsPA4Aw5FCBP60HLuWXjjpCxB10nP0TC7dkGslwbXkHRboojTtMLt-8LsjQ9q0mCThYQPVGmuHYNzZfKg3ZMqcn3r9L29v6nqPDcuSsSrMVDUN7d0Shjt93EdUAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29cc88ce4b.mp4?token=cRYsPQDpHUvhLW4xi-219vp-oOGSrHo7iYDEvsDOFfUy7ypMaJnuVajGgWfcn232l9JJSbogztR8M2gr3ZCwfhuxNP5fYMofGK6vQvmwJdBTxTjjjokikt5j5fJDs8bik5UjFBz_NMh9GFLuiagKDWnBSbcoKpRBrJlzs8aEeV-O0Vzp0W1F76z-l_f-w3VH2JQdD9ohtgxGnqX2jInH5kGdAxsPA4Aw5FCBP60HLuWXjjpCxB10nP0TC7dkGslwbXkHRboojTtMLt-8LsjQ9q0mCThYQPVGmuHYNzZfKg3ZMqcn3r9L29v6nqPDcuSsSrMVDUN7d0Shjt93EdUAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی ارتش: به‌تازگی از پهپادهای جدیدی استفاده کرده‌ایم که جزئیات آن در روزهای آینده اعلام خواهد شد
🔹
برد پهپاد‌های ما تا حدی است که به سرزمین‌های اشغالی می‌رسد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/677243" target="_blank">📅 12:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677242">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huDka3T_rAoA_idcdyR1j4TEevgbkl10Vj08YFSgzINyk8z5bojW1YWZM05kGIjT-MtN6Bgm40X3E4sYEbqvLapin2Wiqt0WKzL9B5KlFITI3O9DNmtK0blk-jbzSqzn85XdPNQqCgms9fJhcGbDLlJ3PbRgUD6TAMD-ODyHqrf1I3RD2mAcqJhqXq06xUDWw3J-3BT_LRx4pwJqtgeeMgniZGMqJ6TuCLHKaiVszjvAaQq6Mzhea7UY2qjp9tRs5bgf9QX8n6uVJRLDOqjrJeZU4MDHHJ49AuvfEs6U4mQwab8TXIRoE_RPJHpZOUHxkPeMF5wTYNuRNhEsYH41Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأکید مدیرعامل هلدینگ خلیج‌فارس بر تسریع در اجرای پروژه‌های تأمین برق شرکت‌های آسیب‌دیده با مشارکت مپنا
محمد شریعتمداری، در نشست مشترک مدیران گروه صنایع پتروشیمی خلیج‌فارس با مدیران گروه صنعتی مپنا:
🔹
از نخستین روز پس از حمله به شرکت‌های زیرمجموعه هلدینگ، مسیرهای مختلف برای تأمین برق از منابع گوناگون با جدیت دنبال شده است تا روند تولید در کوتاه‌ترین زمان ممکن به شرایط پایدار بازگردد.
🔹
حفظ پایداری انرژی مجتمع‌های پتروشیمی در صدر برنامه‌های هلدینگ قرار دارد. تدوین جدول زمان‌بندی دقیق برای طراحی، اجرا، ساخت و بهره‌برداری از پروژه‌های نیروگاهی شرکت‌های آسیب‌دیده ضرورتی راهبردی است.
خلیل بهبهانی، مدیرعامل گروه صنعتی مپنا:
🔹
این مجموعه آماده برای ارائه برنامه عملیاتی و اجرای به‌موقع پروژه‌های نیروگاهی شرکت‌های آسیب‌دیده را دارد. با توجه‌ به جایگاه راهبردی گروه صنایع پتروشیمی خلیج‌فارس در اقتصاد کشور و نقش تعیین‌کننده آن در استمرار تولید و تأمین نیازهای کشور، مپنا مشارکت در اجرای پروژه‌های این هلدینگ را رسالتی ملی می‌داند و همه ظرفیت‌های فنی و اجرایی خود را برای تحقق این هدف به کار خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/677242" target="_blank">📅 12:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677241">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea4aea03d.mp4?token=byY3wQzSzLoumakKeXwviphVa4J8SGRQLgH1skWqorTQ9khG1aReVV2nM-n9v-SYsXgewAJ3kanyNfOhjHk0DfvZMIJtn4LShf16DgHEZMUxAm30Z9o_tbAUuEdMRidmX9hGkSKi5fghAvLJdG0AFvM2ZkX4XLUqJLcUETGLB9mvGGBdeO1GX8LguDLBWxXatSzt0sTHj8jhJGzm1ReG0GtnAUhFNYnA8aLmkoNOcfJi64G7G-byMIx5Nx8_CEISazL8lDlA7j3nRv3nxCs95f5HwJHlwP7OzmOo0cw_5T77GKA_pVI33qwLTFZ_JieDikkDgcfOs6NUmh_kpYRp-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea4aea03d.mp4?token=byY3wQzSzLoumakKeXwviphVa4J8SGRQLgH1skWqorTQ9khG1aReVV2nM-n9v-SYsXgewAJ3kanyNfOhjHk0DfvZMIJtn4LShf16DgHEZMUxAm30Z9o_tbAUuEdMRidmX9hGkSKi5fghAvLJdG0AFvM2ZkX4XLUqJLcUETGLB9mvGGBdeO1GX8LguDLBWxXatSzt0sTHj8jhJGzm1ReG0GtnAUhFNYnA8aLmkoNOcfJi64G7G-byMIx5Nx8_CEISazL8lDlA7j3nRv3nxCs95f5HwJHlwP7OzmOo0cw_5T77GKA_pVI33qwLTFZ_JieDikkDgcfOs6NUmh_kpYRp-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات معجزه‌آسا؛ سپر دفاعیِ پدر زیر چرخ‌های مرگ!
لحظاتی نفس‌گیر از عبور قطار از روی پدر و فرزندی که میان ریل و سکو گیر افتاده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/677241" target="_blank">📅 12:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677240">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzUQcHEQFSHkH0YllCBJJxKtYhsvnDOkXrKAQPa2bVqB1bEiQJ4NidPprHv6MgDtxwUrtvCe-rH8DXOmKoL-cTGRB3adXZnwZ9DXNw0A6KvS_lvZZCPKc79dQdmZr-mxWuNTT_P20ksbQuWyNRm15-UlwgOUQI4reJH2tPvxbE9lpSs_OTP06HgwamrtbCzI-1vKPmf2kM4giDFw4ontUFfZPLOLMD8axqicFEBzCRlUuD0PiXmKTxkLhrKOzMZDzZcD3Y9A5r90cu9_oxui2XNXSuG9nmcSR5mJzBogJetYsTikpO9F_n6QLclEDq52D_iraC12x63yHIzbaCTTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
فروش ویژه بازنشستگان
🔺
بازنشستگان کشوری
🔺
بازنشستگان و مستمری بگیران تامین اجتماعی
بدون پیش پرداخت،بدون ضامن و بدون چک
طرح کالا پی(بایک چک دیجیتال ۲۴ ماهه)
طرح مانیسا(با یک برگ چک)
گوشی و لب تاب تا لوازم خانگی
از ۶ ماه تا ۳۶ ماه
با برترین برند های لوازم خانگی
دوو
سامسونگ
اسنوا
هایسنس
پاکشوما
دیپونت و….
قاسم آباد نبش شاهد ۳۱ لوازم خانگی ابری
@Abri_kalaa
تماس
09914835014
09152166100
@Abri_kala</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/677240" target="_blank">📅 12:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677238">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqIaAFTMXe2IWHFV_ML7ALLgLTdtAvJXMPAI7QnoTF_I5-haEYmksnvWiH2b5zUaQ7Go-wZ-PB7Qr_MtR59pzid7-35kDC3ukr0ccjn1KqUGvwQK65LPa7EmOUR4pg6HT3Mqmqskib5fb-K-obDuAyP--oypRPOzlQ1wCwMBVMk9Sq0i-6svJvE65nHMPljRhJ4lCp1IhSlPDaXKeyVTw4fXDk0sxED4qkV1LtnIQVneQhaWUPCYRgZsG6t_xdzN3_6qllbeekMkybOT3isBMC9qAh9t05HpOJsKmhbd8_ESpIQIr-8G4Puh2AeXovcbvpdCUqNWziHSmFQqKyj6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از 30 درصد کاهش وزن
، با استفاده از
آمپول های لاغری زیر نظر پزشک
در « دکترساینا »
🔸
آمپول‌های لاغری
، بروزترین و موثرترین راه کاهش وزن هستند که با تاثیر بر گیرنده های دوگانه GLP-1 و GIP و تقلید عملکرد هورمون طبیعی سیری در بدن، باعث کاهش اشتها ، بهبود متابولیسم و در نهایت کاهش وزن می‌شوند.
🔹
با استفاده از سرویس کاهش وزن با آمپول های لاغری در دکتر ساینا کاربران می توانند علاوه بر
دریافت ویزیت رایگان درباره تزریق دارو ، از مزایایی همچون مسیر درمان اختصاصی ، ارسال رایگان دارو از داروخانه ، ضمانت اصالت و حفظ زنجیره سرد و پشتیبان 24 ساعته
سلامت برخوردار شوند.
👈
مشاوره رایگان با پزشک</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677238" target="_blank">📅 12:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677237">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیریت بحران اصفهان: صدای انفجار امروز در جنوب و غرب اصفهان ناشی از انفجارهای کنترل‌شده است.
🔹
سخنگوی دولت: سهمیه یارانه‌ای بنزین خانوارها حفظ خواهد شد
🔹
انتخاب واحد نیم‌سال اول دانشگاه آزاد اسلامی از ۲۴ مرداد آغاز می‌شود.
🔹
سخنگوی ستاد مرکزی اربعین: تاکنون بیش از ۳ میلیون نفر برای شرکت در راهپیمایی بزرگ اربعین از کشور خارج شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677237" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677233">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8fh68R3GmKS8RfUXCoOFc2IUJYwT7yA3oI_a91OtwAJqhnAuLUxUk2oAbeq5wp-DVlt1weGtb-3eQlGG6CJusXNds7jlFf86jRDeP8YXyinnux3uUDCm0NXvLCnXpAcqMA5Q9bxPkdWC1XwvBXnREZtPdeNg43D9A-fXnYCby_ldG3FQFH6gqcsPf7ic80hzc4m4eeZ2bvA1Sd1kEohhy00_k7vZFURJxcUO3HFZLlDnWRWAX8j9iIGsK8ec9sfY05LP4fFD-TGjxG6W0-k27_Xa4UoULE9HJKQQpym2K_s_gl36T9hRN9QiuBuRzCAfL3gNGtM26OkKjgZGh5KYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JGgB0C4eyajQxOCd-DWjMWfasG6X8-IyyUimic_rbQc9EQx2cE5VrOhhqtnPGLsus0pL-DbBCtaqFiHCrQy98SEA1fDkIuWueQcsQQScBhNeqpLLgW4NFTtWfV3z-lXbTWXRf49rUVMuyTKzL1VWiHEgVa1N8mrtpQnJ1TSf4a3_4SOXMU2MSdsV-qY8kYN_GxAtqVRv-H689mwxqf_qEd1fHr3K7OTZL_C3psU7LHRycg3U31QQ9DHu2nHIQaNubkRYkMlbZdLqs6yYfIeEAHbEwAd8a8IuCcvc8GaDZMoErPINdYWKh6f-yqpzxyDzHM92aJ2gjtmC5MRnDeU2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPPMZZ3mN2qarMBKiv2F25l8fQovCdyCGuToHDBn1SY10vlCw0BXohAmWFlIii7WeP2DFSLT1D35e15-WNqRh89LIiTkYo-bdraQHrmKC0seANmv9DJHg_leRfqQG7rdz1vLeQFAMredalIb0T6wN7G-uCsOQGj3SwQzyRnBttq6xBrUGdajyj1Wz5BiG-2gt-QL1IOBbOfnRqxCu_TUaltiwo2uFxBn93z8AJU7u7A8LNdZ9YKdX9Wh1kUtQnOM3jnSRs9z1Sjrm6My8ucRkhhzkmVDjceY28YSqrzXp7I_hWzTGon1hbJo7DymcAhIbcvXsk-KHk4E9cBNm_-Ltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ctlVNyGJoVj1ietJWa4jxxk8nMesNkHSfSwu9W2_G7i3zuYPnHtG_NRXC0OEfe6zn8HVQcqytPY1LeDI-zp2wHW5U1bbhx6Ns3apLubugkGLsEdZn0NYEPPl19T7UXrdJl9WkQpWBvDEjXwkEG-ruaFrHGa8bZP55DrTaNkxbgIOntwNTz-yWTJ1py3SM1nCkQKPa1adlbbKvqaNcoP1ssO7l1TsNwEfS7G-Do8sojNH1Q1nfeOY7AkpmMOAxISFxIrfNzlUvLqDGFhEjyr92g9GKi6h72-zf7PniTCHfzHWg-qLMbpEEUCPbjtFyt19JYcJa9OvUi5qp_r2_tcUHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کاروان های خون خواهی امام شهید با پرچم های سرخ از حرم امیر المومنین وارد پیاده روی اربعین می شوند
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/677233" target="_blank">📅 11:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677232">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا به شهروندانش در اردن؛ برای ترک خاورمیانه آماده باشید
🔹
سفارت آمریکا در اردن از شهروندانش خواست با توجه به احتمال تشدید ناگهانی تنش‌ها، اختلال در پروازها و بسته شدن حریم هوایی، خروج از منطقه خاورمیانه را مدنظر قرار دهند و از نزدیک شدن به پایگاه‌های نظامی آمریکا خودداری کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/677232" target="_blank">📅 11:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677231">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlJXss982gY3wRv-AfLkpzSe5DWlHBJUHg7VtZvOaFC6M2rfcG5m9rIlENqLb4M-_R6HdrECZ1-QGWIPqlfvcjvT2UdlkdEf0TNwwCuX7nGRTLMS_jOVkjxuQcV7frArqAds-D6jMfq2uGuZAuzrEBVrxkzaVOcARa84QpuqwszFSwdxWyITiI-vo4d4iyh95a7eW0CLqVCTN1tu4wHSgzz-6LioHeCbICLSppVkBP65QkVaYhLYKjujyIvHn4gmtf-ZkMhBqxhYYE-iG3c53weozpCqBc1NZWeMWH9p_v6FE5yK2_v8erO7zxrIHNVvcJaYXJb0Ta4iMnYVUFN3eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو هفته پرتعطیلی در پیش؛ فعالیت‌های اقتصادی با وقفه مواجه می‌شود
🔹
با تعطیلی روز سه‌شنبه و همچنین تعطیلی سه روز پایانی هفته آینده، عملاً بخش زیادی از فعالیت‌های اداری و اقتصادی در دو هفته پیش‌رو با وقفه روبه‌رو خواهد شد و بسیاری از امور و پرونده‌های اقتصادی تا پایان تعطیلات به تعویق می‌افتد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/677231" target="_blank">📅 11:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677230">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCO6CjsnrMZQJVaymOI9ZTsRAZd0gaWJ6JmuQvodAEsL1DgAUA4BYarVJk6oefX7sKkSt9773l9PCdel_KZVZsFsIQQjP7as-VWEdbzsb57e-KZxxe-i6vHG1UlANmBrEwIuhz0J5La4VRYq4kyc1wby1dhFAUHaBmJ5wwZkdBJoRkdBDJgz8PBj53b_Zfk4A5HLVlo5zscRkKN_46YRRBwKiAK3CIaPUeiQYNibGSIGoFAuW6ZTPDJwES66VFsVUi_MLvlx8HtmsP2RMaU8hPg6K-exML7o1WjSoMViZBy8k9Jec86eI0FhOqayNI-yRvtafIKC14JT6WcGdv7cYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت خبرنگار خبرفوری از جنایت شب گذشته ترامپ در قشم/ حضور در خانه‌ای که شب گذشته در قشم هدف حمله موشکی آمریکا قرار گرفت/برخی از اهالی که خانه‌هایشان تخریب شده در سفر کربلا هستند/ خبرفوری @AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/677230" target="_blank">📅 11:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677229">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
امکان واردات کالاهای اساسی از همه گمرکات کشور فراهم شد
🔹
این مصوبه شامل کالاهایی مانند برنج، روغن نباتی، حبوبات، گوشت قرمز، جو، ذرت و کنجاله است که با ثبت سفارش و اخذ مجوزهای قانونی، به‌صورت انتقال بدون ارز قابل واردات خواهند بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/677229" target="_blank">📅 11:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677228">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egpvNxKepmbK08FIs0Dq9jl2UKCWP8C4Lke-A1tbOKNqILu29ZJq1L25qTj3BIOrqxFAZuubWpcZ9kSnWjHe5-4dDnZLRqRyf5awleuLJFVIiaukB8crsa_Hjc_U5V1haE6QOj2nicFI-0jjIPM5voE-7X00PnqAAOZ2u3nxidSUCFz0kBoQQ6LDA7BIUw-2uvNE_mmwe54zDv0Ol1K0eRBjav4C8NOGbedQtpEhcvXF3SpzH-dW2z1ZtMANLgQidapAo_xSiJCWqFxTs6qSxnG8SU_Ykkg-qyrgrpxa2khXQS1lk8K5vfj5Isuy85q-x5ZttxbVoeg6YcKJ2ErrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
احترام به سالمندان، فقط یک ادب اجتماعی نیست؛ بخشی از فرهنگ مسیر اربعین است.
گاهی یک همراهی کوتاه، خستگی یک راه بلند را کم می‌کند
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/677228" target="_blank">📅 11:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677227">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
عضو کمیسیون اصل ۹۰: مطمئنم غارت پول نفت بدون بده‌بستان میان چند حلقه ممکن نبود/ پشت پرده تراستی‌‌های آلوده یک جریان است نه یک مدیر
مجید دوستعلی، عضو کمیسیون اصل ۹۰ مجلس، درباره پرونده تراستی‌های نفتی:
🔹
بازنگشتن پول نفت نمی‌تواند کار یک فرد باشد و بدون هماهنگی میان چند حلقه در قراردادها و انتخاب تراستی‌ها، چنین اتفاقی رخ نمی‌داد.
🔹
برخی تراستی‌ها پول نفت را بازنگردانده‌اند و همه عوامل دخیل، از انتخاب‌کنندگان تا مدیران مرتبط، باید شناسایی و پاسخگو شوند./ ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/677227" target="_blank">📅 11:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677226">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b26cff82.mp4?token=cuF2Twys7NhbJtvbtkKQZW2W9bf5JgfIczegKUJxrrzHf3uOEnIALEnFjRcOb_HyZRAXuYbd8kysp1KcgSROifG-YPnFmXGTu31KOkIpSjzzGff_Mgvc2ezOJQ4VyD0hBZBVAil8uM1ifNGrLs1R_iqeEr7nzQN2-Q0EIZ7gDIgt6-vU2ww81qBdWw8gIYs-2bAm1WEg0KHkBNhGFVaxZjjzSEGSRwRVJk8BVXfoZd934aPdz3Rd9Enxi1d0AEjI8OjINqAyjHKhrmIX0Ox0vwXoohqPcscyTGdjyRtwPYu_4plt7ezWLiY6seWPj_a0SyB2N7Jae3j96iSlcu_sjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b26cff82.mp4?token=cuF2Twys7NhbJtvbtkKQZW2W9bf5JgfIczegKUJxrrzHf3uOEnIALEnFjRcOb_HyZRAXuYbd8kysp1KcgSROifG-YPnFmXGTu31KOkIpSjzzGff_Mgvc2ezOJQ4VyD0hBZBVAil8uM1ifNGrLs1R_iqeEr7nzQN2-Q0EIZ7gDIgt6-vU2ww81qBdWw8gIYs-2bAm1WEg0KHkBNhGFVaxZjjzSEGSRwRVJk8BVXfoZd934aPdz3Rd9Enxi1d0AEjI8OjINqAyjHKhrmIX0Ox0vwXoohqPcscyTGdjyRtwPYu_4plt7ezWLiY6seWPj_a0SyB2N7Jae3j96iSlcu_sjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
احمد ایراندوست این ویدیو رو  پست کرده و گفته تقدیم میکنمش به روح عمو اکبر (عبدی)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/677226" target="_blank">📅 11:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677225">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f1f9f26.mp4?token=M11Y8WtgzvsgqSfQKawUk9YfiQCipzlfktdKE36JffPXPbknPO0WyptNkNe9g0DahjHrKXof-9rXTwtVgpxTQ2yF-krmx4ITetRVL_5VplGjTao6ymy0y7BzTD1_mWc8hhBgAad8nZPkWolGgldv8YSEB9axUdC4RVzfATtdtMPEYpCsx_GdHueVlB3NagNZ_OwFO7BEgmIXkVLL0QTmO39-m04N3vsfUq-_uJOfy2_DGpTk7osoE-Ah5yViBFTrdq_KrjIt4W6LZN0IRy7jDLN23qZBQQzOZRdubcpLJTvlpz9P0jxXBi76Tl_vvA4zhZmq5pOUPEmt80qZORZzrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f1f9f26.mp4?token=M11Y8WtgzvsgqSfQKawUk9YfiQCipzlfktdKE36JffPXPbknPO0WyptNkNe9g0DahjHrKXof-9rXTwtVgpxTQ2yF-krmx4ITetRVL_5VplGjTao6ymy0y7BzTD1_mWc8hhBgAad8nZPkWolGgldv8YSEB9axUdC4RVzfATtdtMPEYpCsx_GdHueVlB3NagNZ_OwFO7BEgmIXkVLL0QTmO39-m04N3vsfUq-_uJOfy2_DGpTk7osoE-Ah5yViBFTrdq_KrjIt4W6LZN0IRy7jDLN23qZBQQzOZRdubcpLJTvlpz9P0jxXBi76Tl_vvA4zhZmq5pOUPEmt80qZORZzrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوش مصنوعی به کمک ربات‌های نظافتچی آمد!
🔹
ساعتی ۳۰ دلار میدی خونه رو برق میندازه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/677225" target="_blank">📅 11:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677224">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سرلشکر عبداللهی فرمانده قرارگاه مرکزی حضرت خاتم‌الانبیا:هر کشوری که خود را سپر دفاعی آمریکای جنایتکار و متجاوز قرار دهد، در آتش جنگ خواهد سوخت
🔹
آمریکا با هدف سلطه منطقه‌ای، مسیر آتش‌افروزی را دنبال می‌کند.
🔹
کشورهای مسلمان باید بدانند قرار گرفتن در کنار آمریکا و تبدیل شدن به سپر دفاعی آن، هزینه جنگ را بر آنها تحمیل خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/677224" target="_blank">📅 11:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677223">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159deb788d.mp4?token=LTDnQahIgB9mFIuJWVopNwn1LYKeQHILtnON1D-Rx3TtWzHFyi43puPQotNqE-eJoQjY2kYqy3tvXKyKORghFx8N8Klah9yaPDt3bKfZf5zEDeh7vcwMD8CUfG_k45kvHRi7j6ze7lpty3sWkAAXMucef_PIROUsfhgQpT7kRVWwirY7hCKpm3Hf_sDZsoyc7CAB2Yyo_x9FQG4r-5la9qwKdWhhI3iULBK8T82TjFVADiF_OBACEuvt-El9VtRDCA33Rh95QK8tPC6lgewoo8DIQEaOgVH3UDak8MF9UWnDFfQ7MhqXZ36cRK4U-lKZS1AmYCEEuNfSvxtaLazGIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159deb788d.mp4?token=LTDnQahIgB9mFIuJWVopNwn1LYKeQHILtnON1D-Rx3TtWzHFyi43puPQotNqE-eJoQjY2kYqy3tvXKyKORghFx8N8Klah9yaPDt3bKfZf5zEDeh7vcwMD8CUfG_k45kvHRi7j6ze7lpty3sWkAAXMucef_PIROUsfhgQpT7kRVWwirY7hCKpm3Hf_sDZsoyc7CAB2Yyo_x9FQG4r-5la9qwKdWhhI3iULBK8T82TjFVADiF_OBACEuvt-El9VtRDCA33Rh95QK8tPC6lgewoo8DIQEaOgVH3UDak8MF9UWnDFfQ7MhqXZ36cRK4U-lKZS1AmYCEEuNfSvxtaLazGIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی قابل تأمل از دختری ۱۹ ساله که در این سن دهمین عمل زیبایی خود را انجام می‌دهد...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/677223" target="_blank">📅 11:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677221">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سخنگوی ارتش: ترامپ تنها پس از گذشت ۲۰ روز، تفاهم‌نامه اسلام‌آباد را نقض کرد/ عملیات‌های بسیار موثری علیه پایگاه‌های آمریکا در بحرین، کویت و اردن انجام دادیم؛ آسیب‌های جدی وارد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/677221" target="_blank">📅 11:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677219">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
جنایت دوباره رژیم صهیونیستی در غزه
؛
حمله پهپادی رژیم اشغالگر به شهر غزه
🔹
یک پهپاد ارتش رژیم اسرائیل به محله شیخ رضوان در شهر غزه حمله کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/677219" target="_blank">📅 11:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677218">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffd47e5f7f.mp4?token=CDsFxNyZLomLLAOzBhaSs1KAPuvXMV9mFBbKM8FUyac10ghZxK2g9RJFiIWmMCvSko6XFUQc9lq3o4zxlwL977qLMJIT_L-pwmiVWNu4oufvxFViHs2aheaG8gg1jwrf35E8w0Di27ZqpN__m3iJX_pqaPk_5SZQyWd5J4i0uebz87YVlYwT9W-yCZKKSooutnGyVPnkC68ls7icngVS9LuyBcQfWq0AZdWvSum00tgEqpy0yoH8zw_s0eJo_ifqPA45rDLf2M0c77BQ6m2iVtJAAiCi7W23XkRjnJ2gR6Qd71h2g6QGeX0mnXqC498wkyP2svq36D3eF7omXAXpFDpMRu-vEW0rQ4pheQK8q-ECcf9_Mjs5bPiDA1S7wL3z19P_DHcEVI6GrwNh2zc-fnY0ywsi7mj1Mdajhlhidyqu7JNurZDMa_GJ-jseHn_Q0PcQsePeJsdrahtQRWZ742f2u_KjOrKYWRL_e7uFnRAIePAx2W0jub-j8hPC87YzmclGkjQ_2Zbu0Ilc4UT0CKUUJ9YFv8IymDbcSAQPBWuFqRL0uZgxlBDh0Iug01D9TXMGsa_B7ZAy5LPp05y1kqhK3HychubaN3_Xm0q-OiVFwWUmwEczx0iP8QUQxXX8UJPUs_6okpXcgyXkq-FpdgdW5YfJ8es7cptWZ0Kntls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffd47e5f7f.mp4?token=CDsFxNyZLomLLAOzBhaSs1KAPuvXMV9mFBbKM8FUyac10ghZxK2g9RJFiIWmMCvSko6XFUQc9lq3o4zxlwL977qLMJIT_L-pwmiVWNu4oufvxFViHs2aheaG8gg1jwrf35E8w0Di27ZqpN__m3iJX_pqaPk_5SZQyWd5J4i0uebz87YVlYwT9W-yCZKKSooutnGyVPnkC68ls7icngVS9LuyBcQfWq0AZdWvSum00tgEqpy0yoH8zw_s0eJo_ifqPA45rDLf2M0c77BQ6m2iVtJAAiCi7W23XkRjnJ2gR6Qd71h2g6QGeX0mnXqC498wkyP2svq36D3eF7omXAXpFDpMRu-vEW0rQ4pheQK8q-ECcf9_Mjs5bPiDA1S7wL3z19P_DHcEVI6GrwNh2zc-fnY0ywsi7mj1Mdajhlhidyqu7JNurZDMa_GJ-jseHn_Q0PcQsePeJsdrahtQRWZ742f2u_KjOrKYWRL_e7uFnRAIePAx2W0jub-j8hPC87YzmclGkjQ_2Zbu0Ilc4UT0CKUUJ9YFv8IymDbcSAQPBWuFqRL0uZgxlBDh0Iug01D9TXMGsa_B7ZAy5LPp05y1kqhK3HychubaN3_Xm0q-OiVFwWUmwEczx0iP8QUQxXX8UJPUs_6okpXcgyXkq-FpdgdW5YfJ8es7cptWZ0Kntls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت صاحب خانه از لحظه سرقت طلاهای خود و نوه های کوچکش با شمشیر و تبر
گفت اگر طلایی پیدا کنم که مخفی کرده باشید شکمتان را سفره می کنم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/677218" target="_blank">📅 11:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677213">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29749a0fae.mp4?token=S-3NomBGwxpGpn_FJszs3ISPuZXcFjL1FghsVGtta0kskQtdu2zjbed2CvBNOSurzZG5wpL0h3PYvt5vCgvW7FaaN1q8lPdMw0fjOkH5KTw_gBWlUMG1NpKtGMIkB_h_Au3ukFfsnsj4IAy9j4RzXkyM-qAdieE0GW1P8huWgfJVLmOqQLj_9AzutTTgUc1KqltZ5aLSTBMU_zw3KbeJbnpvndh58si4iyf9jBkyAn4hi8vckerY9BcfEjzf7NfY9r1aDsgrGqDlBFdtm4H-KFdcrZ3qMjiUx2JOahOA6cpMrQ6JtaX5ykZjpQ2F9_lMKYF5Wsd2AvbzJcH9i3pXkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29749a0fae.mp4?token=S-3NomBGwxpGpn_FJszs3ISPuZXcFjL1FghsVGtta0kskQtdu2zjbed2CvBNOSurzZG5wpL0h3PYvt5vCgvW7FaaN1q8lPdMw0fjOkH5KTw_gBWlUMG1NpKtGMIkB_h_Au3ukFfsnsj4IAy9j4RzXkyM-qAdieE0GW1P8huWgfJVLmOqQLj_9AzutTTgUc1KqltZ5aLSTBMU_zw3KbeJbnpvndh58si4iyf9jBkyAn4hi8vckerY9BcfEjzf7NfY9r1aDsgrGqDlBFdtm4H-KFdcrZ3qMjiUx2JOahOA6cpMrQ6JtaX5ykZjpQ2F9_lMKYF5Wsd2AvbzJcH9i3pXkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پرده زندگی عجیب مالک میلیاردر تلگرام
؛
پاول دوروف: نه خانه دارم، نه قایق، نه جت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/677213" target="_blank">📅 11:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677212">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJwYxiyWQdZydmW6h2OPZA2as455EygIoQAU3iGUhfVmwt1ZxqzOOHDjSjR4tE8Kv-74hrchnlfbkod6bv5kK2hvzTfQVFVAyPOx23tBbGLl9egDC0HpfFMwfi4t1JPPL_OKnhop3FSNhL9DMYwIUH9Tsy4Je2Av6NX6rxKoAgJCrCO6E-6RIk6F8mXaBxMsboRlnNc5zE_pB7s5hSbGDxVygOggX2rVGq9kspzXUXriM0S0pzPAe8YTlBQCVsJQDQTmYKFI7m19LqlwBG1ADRtS6plW87EDHaN4LNuGCr4yO51KFP4tmwP-xxHmQxTFw6lwNYMJK0Qrs9C01W24fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش چشمگیر ذخایر دفاعی آمریکا
🔹
به گزارش فاکس‌نیوز، ذخایر موشک‌های رهگیر پاتریوت آمریکا از حدود ۲۳۰۰ فروند به کمتر از ۸۲۷ فروند کاهش یافته است.
🔹
ذخایر سامانه تاد (THAAD) نیز از ۴۵۲ به کمتر از ۲۷۸ فروند رسیده و جبران این کمبود دست‌کم ۳ سال زمان می‌برد.
@amarfact</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/677212" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677211">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a694ba76.mp4?token=ufM6GiGljgAFvHSg52Qm1eLwKQqoTEKESbpEiGszbpE-K3l3DGAPcpl7fRnLvogU5eihe3xACvbPETbanND8hF80GHbG8NUhLxn3Y9ynh-ryfFCp6IvRHt6uHmFaGQSR9nCTUtPe2dVtz1qQM7QjzawkKKaIhXZR7of8Azphwy2dVfxqlWA3GYuyE6Xpnjo9TUOUykNrAD7VV2K-QLa3TWILjFlVNKc3J4zwVt-LCV4HKTgc6Qv5yW-lA3qyXDe6uPKRj1SlWaV8AR1rqjTh3ZDrbBeLApWOUSSjSK1-hiTb-13-iIvUVHOiTePB1BW87tEb3rBZvGuy7Ly5-dbslQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a694ba76.mp4?token=ufM6GiGljgAFvHSg52Qm1eLwKQqoTEKESbpEiGszbpE-K3l3DGAPcpl7fRnLvogU5eihe3xACvbPETbanND8hF80GHbG8NUhLxn3Y9ynh-ryfFCp6IvRHt6uHmFaGQSR9nCTUtPe2dVtz1qQM7QjzawkKKaIhXZR7of8Azphwy2dVfxqlWA3GYuyE6Xpnjo9TUOUykNrAD7VV2K-QLa3TWILjFlVNKc3J4zwVt-LCV4HKTgc6Qv5yW-lA3qyXDe6uPKRj1SlWaV8AR1rqjTh3ZDrbBeLApWOUSSjSK1-hiTb-13-iIvUVHOiTePB1BW87tEb3rBZvGuy7Ly5-dbslQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاحالا نوک قله دماوند و کاسه قله دماوند رو دیده بودین؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/677211" target="_blank">📅 10:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677210">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ستاد مبارزه با مواد مخدر: کشت شقایق الیفرا فقط برای تولید دارو است
مدیرکل درمان ستاد مبارزه با مواد مخدر:
🔹
هدف از آیین‌نامه کشت شقایق الیفرا، فقط تأمین مواد اولیه داروهای مخدرپایه است و ارتباطی با کشت خشخاش ندارد.
🔹
این طرح هنوز اجرایی نشده و کشت آزمایشی بذر با مجوز وزارت جهاد کشاورزی، در اراضی محصور و تحت نظارت کامل انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/677210" target="_blank">📅 10:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677209">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/178ccbb251.mp4?token=iRVvr2geT3OqHzzVP5wUu0-8RYB7Sc0P6FrTByYpfvQLTl-E2btdWiE47ilhUpZH52dh5uRF2-Gy6wlMud3sye12c3f-pEQ9AxHrPD4lBbFFfrV76XwNo1vWxmfQuNZSbj1xow9xGcXDaqxybCGqlYfFZ3BAmkZ0psxX46OZx_r2HeePNAykB26Hh7SXvleWum7BGcxVtaLlYeY4a2LKPAZA_PeVBQQOKFPkmI2qy04WZPlHAlBH7Pu3o_KQ5-SN5Xig0yvmhF7eI1bOrFhwCBVP9ILt5EVvXalyVJ3ti2aTr8_Sq2aB-c9eW382x2lpen9evmCDO0owBz72lPaC6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/178ccbb251.mp4?token=iRVvr2geT3OqHzzVP5wUu0-8RYB7Sc0P6FrTByYpfvQLTl-E2btdWiE47ilhUpZH52dh5uRF2-Gy6wlMud3sye12c3f-pEQ9AxHrPD4lBbFFfrV76XwNo1vWxmfQuNZSbj1xow9xGcXDaqxybCGqlYfFZ3BAmkZ0psxX46OZx_r2HeePNAykB26Hh7SXvleWum7BGcxVtaLlYeY4a2LKPAZA_PeVBQQOKFPkmI2qy04WZPlHAlBH7Pu3o_KQ5-SN5Xig0yvmhF7eI1bOrFhwCBVP9ILt5EVvXalyVJ3ti2aTr8_Sq2aB-c9eW382x2lpen9evmCDO0owBz72lPaC6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمهوری تا ابد اسلامی میماند
🇮🇷
به حق الله #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/677209" target="_blank">📅 10:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677208">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سخنگوی ارتش: ترامپ تنها پس از گذشت ۲۰ روز، تفاهم‌نامه اسلام‌آباد را نقض کرد/ عملیات‌های بسیار موثری علیه پایگاه‌های آمریکا در بحرین، کویت و اردن انجام دادیم؛ آسیب‌های جدی وارد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/677208" target="_blank">📅 10:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677207">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
فایننشال تایمز: توان موشکی ایران پس از ۵ ماه جنگ همچنان عملیاتی است
🔹
فایننشال تایمز در گزارشی تحلیلی و با استناد به ارزیابی کارشناسان برجسته نظامی و راهبردی، تقابل پنج‌ماهه اخیر را بررسی کرده و نوشته است برخلاف هدف اعلام‌شده واشنگتن برای نابودی کامل توان و خطوط تولید موشکی تهران، قدرت موشکی ایران نه‌تنها از بین نرفته، بلکه کارایی خود را حفظ کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/677207" target="_blank">📅 10:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677206">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/549b63786a.mp4?token=KnMtT3YzHFLzk_y16CcF9fuhxkruuv5jp8zA0BjxheQvrcdoKlvn4F6uJw2ckZiGmYJOEbrBEi3wuoXcOiThsCtohqEXRn1GnrLakc_meScshzSaU7AXEm0Q0t6Gv2g4Apzwb95-ig3CpmBCFkBtyDtwWp-gM40zIg7PU97bcQUcvY3vJ-KGm94ILzQdbwRAK0VEcC4siO3FTm-xrLh4lPLDEd-FG1ONPE-Qai32AKK4cK73nghUuNSr2C_OETwp81Lu4vjFXx2I7WVx6NGM2yqBHkkxcWRm9EpmbCebzLIsRSUkuWKKmFmFhD2WbnKfipQsy8jNTDnKUh4slUtd5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/549b63786a.mp4?token=KnMtT3YzHFLzk_y16CcF9fuhxkruuv5jp8zA0BjxheQvrcdoKlvn4F6uJw2ckZiGmYJOEbrBEi3wuoXcOiThsCtohqEXRn1GnrLakc_meScshzSaU7AXEm0Q0t6Gv2g4Apzwb95-ig3CpmBCFkBtyDtwWp-gM40zIg7PU97bcQUcvY3vJ-KGm94ILzQdbwRAK0VEcC4siO3FTm-xrLh4lPLDEd-FG1ONPE-Qai32AKK4cK73nghUuNSr2C_OETwp81Lu4vjFXx2I7WVx6NGM2yqBHkkxcWRm9EpmbCebzLIsRSUkuWKKmFmFhD2WbnKfipQsy8jNTDnKUh4slUtd5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
توصیه استاد فاطمی‌نیا برای جاماندگان اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/677206" target="_blank">📅 10:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677204">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
همشهری: بستن تنگه هرمز کافی نیست؛ باید با ناامن کردن منطقه خزر راه نفت اسرائیل را در منطقه قفقاز و جمهوری آذربایجان بست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/677204" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677203">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PspY-5DZVwI-fsu4_N6iOkd4jXFp88hiv_X6_obPXIMVVmnQr1_hzQu2bE_oYz1gL3uCLpFX91JS6uvP44ovXANgmwxj1u7OOeUQXKpFhiiOlMjZqWEl0a22LOsfKG6eksXFDTV7guKLJly_sQuNtaaGub_n2ka_3HcbOQ4P_pkzSAxyg76hVGnO1XEjZ_Yk3OQDcpnw-DII-flouQu2ZwN6A3-o8mfGyRwK7IcDYyyMAYcHl3RZg0mVpVmgWK1PqVZIt6oJDfWRlyR8nrYRYHRTO96Cq5KYKWOsWflWH7EVWkquug7zbTkyYP7TgBs0rRcwNOtWhsY8JCHX1wX6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رفیقدوست: امام من را صدا کرد و گفت بمب اتم نسازید / تنگه هرمز آبراه بین‌المللی نیست / جنگنده هم ساخته‌ایم و در حال تکثیرش هستیم
محسن رفیقدوست:
🔹
وزارت اطلاعات حدود ۱۰۰ گروه نفوذی را شناسایی و دستگیر کرده است.
🔹
هر نقطه‌ای که از آن به ایران حمله شود، هدف مشروع محسوب می‌شود.
🔹
ایران در حوزه موشکی جزو قدرت‌های برتر جهان است و جنگنده بومی نیز ساخته شده و در حال تولید است.
🔹
در حوزه دفاعی به خودکفایی رسیده‌ایم و نیاز چندانی به خرید تسلیحات نداریم.
🔹
تنگه هرمز متعلق به ایران است و آبراه بین‌المللی نیست.
🔹
امام خمینی به من تأکید کرد بمب اتم نسازید؛ چون سلاحی غیرقابل استفاده و نابودکننده انسان‌هاست و به‌نظر من دکترین هسته‌ای ایران تغییر نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/677203" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677202">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKOh9DfRj__5eirazn-8T_uJwmEatoylB4Y86UDmrJvHy70xA8_jMVFRDzcy7KLgrFJzttcd-xaDJGo44-i09np3rm3v876sVYIkcQcU49a0TOwCZmOSG5W6b0OEHpnmy2gZG02ew2WR5LGlW49mcGYr24L7ztcBSaQtbeVgF6lRfkve_sJpJ0ovJWDQcn0BXY0PdNuW8gY0C8HWWCbPrdH1_DWE4ThbKJE1_4oIoehJ-Mc7meM2HzN8e4BL1XM7yPW8lZpC9hxBymvbiY1Kc22mwyAg0PoQ4aGAh4u87fviaAU1aRkdkYfQikawnh0lNDOXx8t6HBBhXkVbjSeSCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جورجیا ملونی نخست وزیر ایتالیا از تعلیق موقت پیمان شنگن با اسپانیا و برقراری کنترل‌های مرزی شدید با اسپانیا پس از هجوم مهاجران مراکشی به شهر سبته/سئوتا متعلق به اسپانیا خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/677202" target="_blank">📅 10:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677201">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
پیام بن‌گویر به نخست‌وزیر اسپانیا
🔹
وزیر امنیت داخلی اسرائیل از نخست وزیر اسپانیا خواست درهای کشور خود را به روی ساکنان غزه باز کند تا به آنجا مهاجرت کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/677201" target="_blank">📅 10:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677200">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYMJWZx4uN9dPxVkklzokvQ6jw-zQRrhzh_XKKheFJSGKG03tU1_tnxK7Xv030rD1ruhFggWvcUT_hAyPF4ZKr0ARtqgnZnferChOiCt3GZuzJqkzLSzU6Mm74g05xPa_9ATmFAMqqG1OwzxTm6_vOcpB7FXSUOFqoJsn2zmr97naa5K5Of8WTPevNDJZ6PRB5rPB6JEtwLhnW09cWuUkSrZGXmH3W6u1sHAjW2WKkhzBDlyRimPyDWjB0dzW1-sLvnTeetw1bIYP4u8Ypydz6cK-xZtLEo6imoI1yvDgsQo8ZQhaJ2QzVyDvEk9yj0xfwug5lBaSZYe4FT0jDpX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست خداحافظی میلاد محمدی از پرسپولیس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/677200" target="_blank">📅 10:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677199">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e46502dce.mp4?token=oR01w2krdwoRm30AuTw78m8xxchXgvKzLWU4ZVv-wLRctut5QV_-JFDwdhAwTN10j061fc5BXxa61xVCfnBHI3M8yJ8kJP0YTbk6veBtQYxDyaqc4rzFWsrjYbwn4-uPd8SBRyqpBUAyqNWynKCKp2Xni-Z8I75HtLQdBqncq37I06YmLB6LERFst0IePzTV5usNvcLfLJo1gmo2PApoRb11aVJtvcMVf5NIvo-_H5S_KxblOE-xjAR8JMasSGStvU39RPnJbPnx4bKc_ZrWSO4zimP092rHPJo9oNqYSfS57d8iFKljdOap6PO1PQ3xrXLkumie7Ox-2ptKsEaYJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e46502dce.mp4?token=oR01w2krdwoRm30AuTw78m8xxchXgvKzLWU4ZVv-wLRctut5QV_-JFDwdhAwTN10j061fc5BXxa61xVCfnBHI3M8yJ8kJP0YTbk6veBtQYxDyaqc4rzFWsrjYbwn4-uPd8SBRyqpBUAyqNWynKCKp2Xni-Z8I75HtLQdBqncq37I06YmLB6LERFst0IePzTV5usNvcLfLJo1gmo2PApoRb11aVJtvcMVf5NIvo-_H5S_KxblOE-xjAR8JMasSGStvU39RPnJbPnx4bKc_ZrWSO4zimP092rHPJo9oNqYSfS57d8iFKljdOap6PO1PQ3xrXLkumie7Ox-2ptKsEaYJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاج حسین یکتا: قرار نیست قصاص و خون‌خواهی را به ظهور موکول کنیم/ ما خون‌خواهی و قصاص را مقدمه ظهور می‌دانیم
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/677199" target="_blank">📅 10:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677198">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
آخرین وضعیت ترافیکی محورهای منتهی به مرزهای اربعینی/ترافیک سنگین در محور منتهی به ایلام
جانشین پلیس راه راهور فراجا:
🔹
در برخی محورهای منتهی به تهران و محور حمیل – سرابله – ایلام ترافیک سنگین مشاهده می‌شود.
🔹
سایر محورهای شمالی و اغلب مسیرهای منتهی به مرزهای اربعینی با تردد روان همراه هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/677198" target="_blank">📅 10:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677197">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec63f82889.mp4?token=HOPifC_iXluhIVCQ9gcLCc8riOv0TcfG2eBwGm-8eJLUIhxYtEGIflaXWsGENUjy2JZUPwqKlEj8Eu8HVnz4vjrWILHdOFdcINKI3_Bv7Hx76rlpQp6bfYwfnpRsrE_o5rdBL3hk4YRoDHce3_8-ps9Bd6O5PQLJe4o6dHAM1nxw3wyQbchnNTtKPotg1wD2h4YCk5GWhj0kWgXfd-b_OlF-QeFidkFIhoOQzMKnt4Fm6TAngzhjbyzGMejo5UK_YsFYoO4b7iKq0xctCUrwBautacqTOQOtRBjgwFL1mfzLxtx36kABnQJzUWu9_0kxhiVOU9jWyg-25djA2mXo_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec63f82889.mp4?token=HOPifC_iXluhIVCQ9gcLCc8riOv0TcfG2eBwGm-8eJLUIhxYtEGIflaXWsGENUjy2JZUPwqKlEj8Eu8HVnz4vjrWILHdOFdcINKI3_Bv7Hx76rlpQp6bfYwfnpRsrE_o5rdBL3hk4YRoDHce3_8-ps9Bd6O5PQLJe4o6dHAM1nxw3wyQbchnNTtKPotg1wD2h4YCk5GWhj0kWgXfd-b_OlF-QeFidkFIhoOQzMKnt4Fm6TAngzhjbyzGMejo5UK_YsFYoO4b7iKq0xctCUrwBautacqTOQOtRBjgwFL1mfzLxtx36kABnQJzUWu9_0kxhiVOU9jWyg-25djA2mXo_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی تازه از روز حمله به محافظان احمدی‌نژاد
🔹
ابهام‌ها درباره حمله به محل اقامت محمود احمدی‌نژاد و هدف قرار گرفتن تیم حفاظتی او همچنان ادامه دارد. به‌ویژه پس از انتشار گزارش‌هایی که مدعی شدند آمریکا و اسرائیل سناریویی برای خارج کردن او از ایران و بازگرداندنش به قدرت طراحی کرده بودند.
🔹
حالا عبدالرضا داوری، مشاور پیشین احمدی‌نژاد جزئیاتی تازه از روز حمله، وضعیت محافظان و اتفاقات پس از آن روایت کرده است./ هفت‌صبح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/677197" target="_blank">📅 10:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677196">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1184e18f.mp4?token=pK_IdZ5pt90baEiogUqfgpFTWebM6I9EsP6iYLYFzo44nlWEMk8UZocl0zZzQyEbFfz5KHJRgba23WC1w-LHjFTbcX05vlQJKlK0r7lktjQZLqihamlCAkOILz6efA6cRjNSTMPEAHGzOJzqosypC9Q9hQOK7ypW-oF4tLjW4aPe6pR17SctbrK5hrmy3QrYtEEDnQ10AaG-br4fHaGsouWHJXvJGhRa49aVo0ElDJJEG8qUCLeA7jJRm7P3dy8xvIabTMzeIcVCFq5hoeZ29Zi1Gp30Ol1MfcgNfyioMVnk_L5I9KvmYidJvRu9xVgLa1F7ftjnuDr1KqAwGjOL4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1184e18f.mp4?token=pK_IdZ5pt90baEiogUqfgpFTWebM6I9EsP6iYLYFzo44nlWEMk8UZocl0zZzQyEbFfz5KHJRgba23WC1w-LHjFTbcX05vlQJKlK0r7lktjQZLqihamlCAkOILz6efA6cRjNSTMPEAHGzOJzqosypC9Q9hQOK7ypW-oF4tLjW4aPe6pR17SctbrK5hrmy3QrYtEEDnQ10AaG-br4fHaGsouWHJXvJGhRa49aVo0ElDJJEG8qUCLeA7jJRm7P3dy8xvIabTMzeIcVCFq5hoeZ29Zi1Gp30Ol1MfcgNfyioMVnk_L5I9KvmYidJvRu9xVgLa1F7ftjnuDr1KqAwGjOL4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی ارتش: ترامپ تنها پس از گذشت ۲۰ روز، تفاهم‌نامه اسلام‌آباد را نقض کرد/ عملیات‌های بسیار موثری علیه پایگاه‌های آمریکا در بحرین، کویت و اردن انجام دادیم؛ آسیب‌های جدی وارد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/677196" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677195">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
آکسیوس: حملات جدید ممکن است با مشارکت اسرائیل انجام شود
آکسیوس به نقل از یک مقام آمریکایی:
🔹
ترامپ به‌طور جدی در حال بررسی آغاز حملات علیه اهداف انرژی در ایران طی روزهای آینده است، اما هنوز دستور نهایی برای انجام آن را صادر نکرده است.
🔹
این حملات همچنین ممکن است برای نخستین بار طی چندین هفته، شامل مشارکت ارتش اسرائیل نیز باشد؛ و چنین تشدیدی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/677195" target="_blank">📅 10:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677193">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b451f88a68.mp4?token=SOJNALZ6_Ni7en9uHaPAfK3jdCuhg0_wBB8gnEY6je4H9ZPyFvNcPjXPtbpK2l7E8-i8glmuM00F6VTztu883lRANuwOv883DMb-O280Iav_sDIgH3KQKs19OBZAqjcKpC6mLIPfqnK1jr-TA5ng3jZjgXPkKO7LdUQ_BF7iTfvDHvJ4O5HeLl1GuyJwffphqvy-HbaDBgYZ0_htY4C-_Ll_X41xjDQTr6muh87een5a9UdoVoi-fRaAGE7q7fdUDjnPRUSc2NojizeicSsYkyIbko_6SaaoDTtgEMf4XRCRNwxrLAL9LL8klig7uRca-CA4RpC4b3df8rElDwjGZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b451f88a68.mp4?token=SOJNALZ6_Ni7en9uHaPAfK3jdCuhg0_wBB8gnEY6je4H9ZPyFvNcPjXPtbpK2l7E8-i8glmuM00F6VTztu883lRANuwOv883DMb-O280Iav_sDIgH3KQKs19OBZAqjcKpC6mLIPfqnK1jr-TA5ng3jZjgXPkKO7LdUQ_BF7iTfvDHvJ4O5HeLl1GuyJwffphqvy-HbaDBgYZ0_htY4C-_Ll_X41xjDQTr6muh87een5a9UdoVoi-fRaAGE7q7fdUDjnPRUSc2NojizeicSsYkyIbko_6SaaoDTtgEMf4XRCRNwxrLAL9LL8klig7uRca-CA4RpC4b3df8rElDwjGZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تغییرات ظاهری و کیفیت خودرو برندهای بزرگ دنیا از گذشته تا امروز
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/677193" target="_blank">📅 10:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677192">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
حمله پهپادی به کویت
🔹
ستاد کل ارتش کویت اعلام کرد که سامانه‌های پدافندی این کشور در حال مقابله با «پهپادها» هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/677192" target="_blank">📅 10:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677191">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNeAK6bnT9kvOaD71FjvBCZlsbUnibn1gOsqXjFfzHfz6Irs9xTCSpzMLBhBpfN8vD5pZKWRb-xC_d1FFrw6s_5Iv-iPMg7v7Wl_yeqXUnNlHQRIkPV0_gDCAZO4zDCFQbI2B79Qy4RGW5Hq9lGEJcR6kUInI7sjg34DqlH565XFLKlczwyLDQfPiC-Of1hxo_zb6NsfhpjiHJdOVW6UaYo2ZB1Yj8RXpxtvWg5qMmWBir9p7YzZxrX0qlUvcykhZ-nsbtK8xyxaQNzxEtJnq0TMK9G2Zgx0YdaktZdnCjRi7iywSMUGubKDRpGlYSQJOPyBRfLkrFplnGZH42SAoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از شهید مصباح‌الهدی در کنار رهبر شهید انقلاب
🔹
این عکس متعلق به آرشیو شخصی خانم سیده هدی حسینی خامنه‌ای است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/677191" target="_blank">📅 10:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677190">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAkvDd38rDthSHG4WFwPUh2dgIRs47QOGwMhKagUCwtFx1o5GGLuxGMyGFGPe1zC3PwLyBO51nnPL3GDf_ugoALrHeaG77hgW7O7Ch4GOMBsILk-EP3YzhNPDAXQl4yOsBtaDG1MJsUlByHPCjZEtHVPsgerwbNr8xse6NOz_hrtGw2gm-jeaPj1GZjqyWNSFquiaQVy2DDyatBb3Dc2jUlLCPME5jTucJInBvRTsHPNWQfeIke5NL5pj7KatIqKch18t3Oz46RxGBHyeQ6qvk7mive7z0Z7hJ8UxxSYDhXUO_BTWolenLbdnoFabGSB5zJapEQTtnbJ4pRxVGUzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فقط با سه قلم مواد، یک دسر فوری و کم‌کالری درست کن
😎
مواد لازم:
🔹
دو لیوان طالبی خرد شده
🔹
یک لیوان شیر (پروشیر)
🔹
یک لیوان آب گرم
🔹
یک بسته پودر ژله بدون قند #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/677190" target="_blank">📅 10:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677189">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a02884086.mp4?token=MmKazSkW76Zht2rwxl1Uzwnd0lFSjxu4Bw8V-JPFIrsbmO1N4FTFh0Dwa7m1tbIGm3SLsBaXdsXfL0-dNSRB7A9_wln4CHRq6m9rV2TZpfaeTe5DRzJ-RQ2y03cPxFFaUnHyqUgSVJ6SEBOXAmm_VonRI-2NIKEsgnkkzxu40RDDLEUUJIS8wksshiJFYUgHC6DFr6PDMz2t7aK8jBIVkbddIXG_lQmMKru2tY2gjoh9zbSRW5GzamluswcWuLRwlmpen6Ebzot2M1AHBNg5pwCWTYfWkdbSbOMDBjeEnZADtPapZczXjD6K4w9bKGtyVjSbnhvmPDpJ6a-VIOI-iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a02884086.mp4?token=MmKazSkW76Zht2rwxl1Uzwnd0lFSjxu4Bw8V-JPFIrsbmO1N4FTFh0Dwa7m1tbIGm3SLsBaXdsXfL0-dNSRB7A9_wln4CHRq6m9rV2TZpfaeTe5DRzJ-RQ2y03cPxFFaUnHyqUgSVJ6SEBOXAmm_VonRI-2NIKEsgnkkzxu40RDDLEUUJIS8wksshiJFYUgHC6DFr6PDMz2t7aK8jBIVkbddIXG_lQmMKru2tY2gjoh9zbSRW5GzamluswcWuLRwlmpen6Ebzot2M1AHBNg5pwCWTYfWkdbSbOMDBjeEnZADtPapZczXjD6K4w9bKGtyVjSbnhvmPDpJ6a-VIOI-iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاکم بحرین خطاب به ایران: حضرت محمد(ص) پس‌از قرن‌ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگر به بحرین حمله نکنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/677189" target="_blank">📅 09:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677188">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1047710156.mp4?token=T23ZrMT3Z7V5TQCbECa2q7Yao7QTwsEzooV16PC79AKt1dfpyVmlRAl4_6dJAsEfLqHgjZxfwoQzxN1ycDKpVt7YcU5fv6PPLzfbtxU7UQB5frKDDDBvjHrWsMlVLxnXMZb0a5YYtyO9Jr-gqkuyOoB9ga9R1PL5dfKsSh9FgAngkjbrL69yYDl4EswPvc6TFlz6f1MWQGrAgOyI6TXmq4PfYnx5mRX2Eae5bqTv7ITZjIAxVl6WSXK9BAL1oKV0KbQR_YNGpEFJhpy5NboMhBsoxt_HZFlIs3G0JbXFiCFdCSizZKFiWWHyrMoj2NCyZ1pm_GSeL3vozWGFL17AW00ep_n9nSDuQn-FhmbGVl6DA7eBeII0N2HenkqWqwsqnHMGgheu-VBQd11onXoTxPDYn7gDxStPtvy4XkUWPerzCdyGj_Be1u5-nwAwZSY0bWZs0cS_bwELGDMHnC0itVgCZyVf947rzq_TxG5w5dFt3QGB-Y7nUB3ip90oBE9drOqiv1Lc1QkxjrWC-stJ8YRFyCGRG67XvvGjvSwxEJh-Dhlp8Cawzl9A0f4OuYcAg_R8cTIo7Ei3in2dktvi479I_-R60cabv-jRX0QDfx5hepwGAcv6LpTh4FTyhyIcS9KCUjz18DG3pVKOQl-BmcdUfHP1YIE-rYGvhmc1JC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1047710156.mp4?token=T23ZrMT3Z7V5TQCbECa2q7Yao7QTwsEzooV16PC79AKt1dfpyVmlRAl4_6dJAsEfLqHgjZxfwoQzxN1ycDKpVt7YcU5fv6PPLzfbtxU7UQB5frKDDDBvjHrWsMlVLxnXMZb0a5YYtyO9Jr-gqkuyOoB9ga9R1PL5dfKsSh9FgAngkjbrL69yYDl4EswPvc6TFlz6f1MWQGrAgOyI6TXmq4PfYnx5mRX2Eae5bqTv7ITZjIAxVl6WSXK9BAL1oKV0KbQR_YNGpEFJhpy5NboMhBsoxt_HZFlIs3G0JbXFiCFdCSizZKFiWWHyrMoj2NCyZ1pm_GSeL3vozWGFL17AW00ep_n9nSDuQn-FhmbGVl6DA7eBeII0N2HenkqWqwsqnHMGgheu-VBQd11onXoTxPDYn7gDxStPtvy4XkUWPerzCdyGj_Be1u5-nwAwZSY0bWZs0cS_bwELGDMHnC0itVgCZyVf947rzq_TxG5w5dFt3QGB-Y7nUB3ip90oBE9drOqiv1Lc1QkxjrWC-stJ8YRFyCGRG67XvvGjvSwxEJh-Dhlp8Cawzl9A0f4OuYcAg_R8cTIo7Ei3in2dktvi479I_-R60cabv-jRX0QDfx5hepwGAcv6LpTh4FTyhyIcS9KCUjz18DG3pVKOQl-BmcdUfHP1YIE-rYGvhmc1JC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت قالیباف از چگونگی شکل گیری میدانی به نام خیابان در جنگ تحمیلی سوم
یک ساعت بعد از بمباران ما متوجه شهادت رهبری شدیم
تا زمانی که توانستیم مسئولان را جمع کنیم ساعت ۸ شب بود.
در آنجا تصمیم گرفتیم ساعت ۸ صبح فردا شهادت رهبری را اعلام کنیم.
ساعت ۱۰ شب چون نباید مسئولان در کنار هم باشند پراکنده شدیم.
ساعت ۱۲ شب شبکه‌های ماهواره‌ای شهادت را اعلام کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/677188" target="_blank">📅 09:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677187">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
حادثه دریایی دوم در سواحل عمان
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) امروز اعلام کرد که گزارشی از یک حادثه در فاصله ۲۱ مایل دریایی شمال‌شرقی خصب عمان دریافت کرده است.
🔹
ناخدای نفتکش گزارش داده که در نزدیکی شناور، شاهد پاشیده شدن عظیم آب و انفجار بوده است. طبق اطلاعیه این نهاد، تاکنون هیچ‌گونه آسیبی به این نفتکش گزارش نشده است.
🔹
به گزارش سازمان تجارت دریایی بریتانیا، مقام‌ها در حال بررسی این حادثه هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/677187" target="_blank">📅 09:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677186">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
قالیباف: ما جنگ را پیروز شدیم ولی باید پیروزی را تثبیت و ثبت کنیم و حتما کشور هم باید امید به آینده داشته باشد و چشم‌انداز آینده آن روشن باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/677186" target="_blank">📅 09:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677185">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
هشدار دو غول نفتی آمریکایی: ادامه جنگ علیه ایران قیمت بالای سوخت را ماندگار می‌کند
🔹
دو شرکت بزرگ نفتی شامل اکسون موبیل (XOM.N) و شورون (CVX.N) به عنوان تولیدکنندگان برتر نفت ایالات متحده هشدار دادند که عرضه جهانی گازوئیل و سایر محصولات پالایش یافته می‌تواند همچنان به دلیل جنگ علیه ایران محدود بماند و تداوم قیمت بالای انرژی را در نیمه دوم سال جاری میلادی رقم بزند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/677185" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677184">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
تمسخر تناقض‌گویی‌های ترامپ درباره ایران توسط مجری آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/677184" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677183">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAvcfcvA52SEqxQAQpzxa_N18RvVW2HVwHAXLhw2P3QbdRB7oC3uJ5vyC9TXn-pQly0LyPx91BTwgH5NtnJW9NGCORx5kveRMOAQyB4aPfjhJeRQPhbrCQNbN6COIhXk59iJ3vHPby841GOu6Ewlw7vIN-vrC6UC7HhuLQzBj6_jF0rYnzqaXyecV6vzBpap4CM61fjGaH7uE4xHb3OUtOkF2oNIgWEgVIzoBR7ECg_DcwRIqRKojXYnLbWcIGfwDPizt5YIMcws6s13Advp8tIufgXmc8bLLkUm5BKVXqI9IARZbB07E2_zaxK-Hhu8FHtMbkEgWIFNbYqL_knoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واسه هر اتاقی چه گیاهی مناسبه؟
🪴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/677183" target="_blank">📅 09:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677179">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfCCG7UtRrG9aAnGLltmhwyvSWQMZaLEHZjRUW_ElHVA2YMeRfd1bgaXtAgfGKALMYJXleRL4vJk3z8AAe5ItoZiGyYQGenfGe4FdVrXUmsfq8cfG9aAQsj25FgU3PY0e_s9nC3nHGVvXA9JVx43rZWDyv2DjhZtH-jQnf9pcdMmmsSnLdxCUSSz7gPUjEQGJzLF7KRjV5ZSRIb1QdAZlQc3QMGopdbQdC2Cp0h3LvPuif11CUivr6nQjdLBxeW52GhWe-0EgqN_iVWWPeTF75Xu1dzwnDK-47AbdTdDAqaDS91MKjWtT5ZO6_aZqlV5cKP2EXQFJGvrozLTj5udiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای تجزیه‌طلبان بلوچ پاکستان درباره تصرف دو پایگاه ارتش
🔹
گروه تجزیه‌طلب ارتش آزادی‌بخش بلوچ مدعی شد دو پایگاه ارتش پاکستان را در شهر کویته، مرکز ایالت بلوچستان، به تصرف خود درآورده است. این گروه همچنین ادعا کرد که در جریان این عملیات، ۱۴ نظامی ارتش پاکستان کشته شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/677179" target="_blank">📅 09:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677172">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svx93fFatieukhE4-aZqDF9mjV4hir0a--CeQi3_aWwA1V6STjz6NzceUAZ4ndh9sGL5_yPC1u_lFsp33IMaVJ3u5fl8z07ECdF3PUpDcxfm3VDQ3RBhoBUQ30zEHzzFyYMEuoPogMo2neJXy8nePlhUay1PrrOQq3HZw65xur45E4S0AnF6y4RflF_xyU40rv5qGkwXZ2JtuBgLkqFSYBR272lu2wu7d1dBB6Xee1gNJcuEgTI5miGWjLw8Rtu_gbTJPLTLeFYKqUYxqR9dA2sVTOfvvNPE_GpoMza9K8h4jqQaGpTL6PX5S8tY5vb5pESJgO8NPSr4lua-HlFiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرفروش‌ترین خودروهای تمام دوران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/677172" target="_blank">📅 08:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677171">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoizkShXTPoEFHnaB40dFilj83MACxVJmKYUF3d_UAgzfSGpFmpBXKjT7pxUMqn9pyzPtOzJ7hWcCpi2Bk_CKKgJx5NNyiREj8_WEaUik27sACVrAcKCb3pYSRq7Vn30iHaGvvf9zRCMOo5NSkQUB5lLXSgExD4ATqVdVc3MiklyjOUk3-82UUDqiQKek1k7uz7aygomtUTuVZPzQ0f_4Tz6XWISBecKACzNCcC3uvsDtCx2nW0skt__-9ynDQ-CONTgMEkvxTijLtOcIhbFaGUUHQ7FbF7ClOSwJPhcvOTyQ1VVWk1wgRlsY3XLYeoGY8Kykwzw9D1-n4VhfIv8YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ زرد: آنچه که در اسپانیا اتفاق می‌افتد، با ده‌ها هزار مهاجر غیرقانونی که به آن حمله کرده‌اند، در ایالات متحده در دوران دولت خواب‌آلود جو بایدن اتفاق افتاد، و اگر دموکرات‌ها دوباره به قدرت برسند، دوباره اتفاق خواهد افتاد، حتی بدتر.نگذارید کشورمان نابود شود. به جمهوری‌خواهان رأی دهید و به ایالات متحده افتخار کنید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/677171" target="_blank">📅 08:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677170">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdHNVgsXqbp3yr99Trk72CA-RdqrKmZQKTjGUEyg19agVQ6BG0ouN2LXlf6ZF6SOp1UGgGeh88363e3nH2ClEyBpE1d_Y9K_64MeXp9GmCb_jgHTsMqDptCrGCK4ULoWmjeHOV-PKVS5S4KiE-mJ0HDtkX0o2seLMzd8XOpM3HTkGvF_G9GB8Q5e7LdYFjZCqZHmnWgV1mtDcBGEOKUPzqPxekFvXyHMnfoceDrpMenQyplDzZgzvOC7CXMNqnhE8figeFU23UfiIoVThpfpO2oRGYzVWQkRlOzqH6tXwycjpMbrawSTAQ9q0_yEKlhFtV3DcNcGyF-swcttoaWK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قند رایج در مواد غذایی می‌تواند به پخش سلول‌های سرطانی کمک کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/677170" target="_blank">📅 08:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677169">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4862af396f.mp4?token=BzlR9-yQNhn_MwHS-5H5Ffo2oKqLTfyJ-fMx8QiP35cZC-LQ3klJGJofQDjznr_puyzdH3KQNUCJqV5mPRFba4ilNiO6RVNLEIAg8mkeLnK1qeL8BTLcWu5F6OazD_22vOK7uwbSTJH1TxJZnJMz1N2MXwUevZbNJasD7_URByKPXyu5r1t_Ew5wElOzJs4LUgp2fFCVDvTtlKbLpSyrK6mTfh59c7_zoOUCzQl6V1afiJEWhkhrPPILvf0w6vQbaHUMJ6GVXrssddbhtEs8xPtV6tZfcGrGOCZBrHX99mTDM55UsWpuw31YV5L7rYue4n8rpDKDhgzFbxEAjfYBug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4862af396f.mp4?token=BzlR9-yQNhn_MwHS-5H5Ffo2oKqLTfyJ-fMx8QiP35cZC-LQ3klJGJofQDjznr_puyzdH3KQNUCJqV5mPRFba4ilNiO6RVNLEIAg8mkeLnK1qeL8BTLcWu5F6OazD_22vOK7uwbSTJH1TxJZnJMz1N2MXwUevZbNJasD7_URByKPXyu5r1t_Ew5wElOzJs4LUgp2fFCVDvTtlKbLpSyrK6mTfh59c7_zoOUCzQl6V1afiJEWhkhrPPILvf0w6vQbaHUMJ6GVXrssddbhtEs8xPtV6tZfcGrGOCZBrHX99mTDM55UsWpuw31YV5L7rYue4n8rpDKDhgzFbxEAjfYBug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر زانو درد، درد هنگام راه رفتن یا احساس ضعف در مفصل زانو دارید این ویدئو رو حتما ببینید #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/677169" target="_blank">📅 08:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677168">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
رسانه‌ آمریکایی سی‌بی‌اس در مورد حمله به زیرساخت‌های ایران
🔹
رسانه‌ آمریکایی سی‌بی‌اس در ادعایی عنوان کرد آمریکا و اسراییل با فرا رسیدن پایان هفته میلادی برای بمباران زیرساخت‌های ایران از جمله نیروگاه‌های برق و پالایشگاه‌ها آماده می‌شوند.  بیشتر بخوانید
👇
…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/677168" target="_blank">📅 07:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677166">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btn6_va2XBVxqPlopWXWNMHFgkR7hMVc8Euro2bXFHJ4DjOe9mXQ0B1QjxWPSC_HBAmk49uLh3R1Ah3O_Cj9yTYOxG76WpFNaR5RlRR7iwHkRyACzXNz4JXg7Qv1JOP6behwhZNZO4juDXBfNAkuJ4do0oXu7NbxdpVU70ADhIJWqtDGqrWGw9snA-DOmX9l0eRMlpqJH3cPnlWxZqU3emIShy3fW0McJXwcfBoKUp1pQnX01nknKXsTAx9TYU1wu_wATQSlwt1crA0PNl_J6nWb0zwngDfZMC8hLEEXuTXanISkUhRN4X2DV7NI44o50iVH7-s7oz8DFcBKgd7iiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۰ مرداد ماه
۱۷ صفر ‌۱۴۴۸
۱ آگوست ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/677166" target="_blank">📅 07:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677159">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cf6df173.mp4?token=XzcLByAbRNmqACsZbiPZsjhdBibAJ8jxsyDLqSAaapg_5kg_TDUDNxVqSplJb0yHugu0eZFwGPjS4Iw4wTNP0oJyrtT_pirMPdszERBD4gWsDioUvsSoypj8CF4p1bNTI9k1AalN6JzEO_6K9MUPGxoxNrIciXwGDyUM5O0Khz_HKlhYmLHZnQqfO7qSeTQxGbZuWV32VUe3iUblRnEd5bAdD9BdfoLjFr6rgTEcAboFkah4BugsAOF3m8Kfum91s5H2qyCnWBeNfNq1LkBiHaBieX3SMUUm1UUIDoCh1NHYNP6i1VescqKMOlVTN1oVVL8ADGzCNOnV8eIglhw8Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cf6df173.mp4?token=XzcLByAbRNmqACsZbiPZsjhdBibAJ8jxsyDLqSAaapg_5kg_TDUDNxVqSplJb0yHugu0eZFwGPjS4Iw4wTNP0oJyrtT_pirMPdszERBD4gWsDioUvsSoypj8CF4p1bNTI9k1AalN6JzEO_6K9MUPGxoxNrIciXwGDyUM5O0Khz_HKlhYmLHZnQqfO7qSeTQxGbZuWV32VUe3iUblRnEd5bAdD9BdfoLjFr6rgTEcAboFkah4BugsAOF3m8Kfum91s5H2qyCnWBeNfNq1LkBiHaBieX3SMUUm1UUIDoCh1NHYNP6i1VescqKMOlVTN1oVVL8ADGzCNOnV8eIglhw8Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: تنگه هرمز متعلق به ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/677159" target="_blank">📅 05:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677147">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1749506c74.mp4?token=F1yRj6nX3JhmAhAXbPLGv5kEgjjKdRjbWUwdSI5k9Rd5bg35NPRByvSewWpx-v_rEuQuQ5ic2JcIX9GqF6HgPpfFZoxh8LWoK_sJL_by6iqo1cZSYXeLCFKn47aPXR9LPg7bgJfywZZeORpUfay2Q3Z6oqYGtqbmYc78s7Es-MbkA-nWllhJ8l06Y2PNXtZCgmy2ywa2NQOiQ_UOrM070EuJn8ZafIn--T3ca7X35O8Ombi_VjexPCXrvuFpcX_qHJGO3fzHyerGabNWb0p4GYOKCYPAPrqW887_oKCkrkCKr3qYfE-Ln41K-42G8wvEPtfqdePQ6nk-djeQHKRWzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1749506c74.mp4?token=F1yRj6nX3JhmAhAXbPLGv5kEgjjKdRjbWUwdSI5k9Rd5bg35NPRByvSewWpx-v_rEuQuQ5ic2JcIX9GqF6HgPpfFZoxh8LWoK_sJL_by6iqo1cZSYXeLCFKn47aPXR9LPg7bgJfywZZeORpUfay2Q3Z6oqYGtqbmYc78s7Es-MbkA-nWllhJ8l06Y2PNXtZCgmy2ywa2NQOiQ_UOrM070EuJn8ZafIn--T3ca7X35O8Ombi_VjexPCXrvuFpcX_qHJGO3fzHyerGabNWb0p4GYOKCYPAPrqW887_oKCkrkCKr3qYfE-Ln41K-42G8wvEPtfqdePQ6nk-djeQHKRWzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از موکب‌داران عراقی با انتشار کلیپی نوشت: این تصویر آقای علی لاریجانی در منطقه شط ‌الله (منطقه‌ای روستایی تابع طویریج) هنگام عبور او در زیارت اربعین و در میان عراقی‌های ساده و معمولی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/677147" target="_blank">📅 03:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677146">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b623cfa5e7.mp4?token=OdE7JpfMw-KPoNt7IOz4t_zghUKr99GJtLia83O_bQw9DnPmz0bf2Lp7hjay7Xpaif5aqfcwyqHaizMf3oiTIcekDpfCI2LOLg2F6heDOZ3HFvvCCHxpJ_h7RSvY68E5y_X-d40K74H1upN-jPCadPdTauzT2tOl-qQsFfrr2S8FkhPOcMKlsnuF7nnUMixajwVkpPLR0YOmCLqaXFUaxOSL5WHpfUNy8wpwOT264RhzuwcPwAqJWZHdvyvGFRXaUvLpx3SMS_8P6181F3YXC30-xAAinsarHbQqTzjWfpkUOHO9_Ry8d2osnEEbOrXyqjYnfg_COp-zsfCV5IOAWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b623cfa5e7.mp4?token=OdE7JpfMw-KPoNt7IOz4t_zghUKr99GJtLia83O_bQw9DnPmz0bf2Lp7hjay7Xpaif5aqfcwyqHaizMf3oiTIcekDpfCI2LOLg2F6heDOZ3HFvvCCHxpJ_h7RSvY68E5y_X-d40K74H1upN-jPCadPdTauzT2tOl-qQsFfrr2S8FkhPOcMKlsnuF7nnUMixajwVkpPLR0YOmCLqaXFUaxOSL5WHpfUNy8wpwOT264RhzuwcPwAqJWZHdvyvGFRXaUvLpx3SMS_8P6181F3YXC30-xAAinsarHbQqTzjWfpkUOHO9_Ry8d2osnEEbOrXyqjYnfg_COp-zsfCV5IOAWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات موشکی به اوکراین، آسمان کی‌یف را مثل روز روشن کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/akhbarefori/677146" target="_blank">📅 03:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677145">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
هشدار عراقچی به انگلیس درباره همکاری با متجاوزان
🔹
عراقچی در گفت‌وگوی تلفنی با وزیر خارجه انگلیس، هرگونه همکاری با متجاوزان یا استفاده آنان از قلمرو و امکانات کشورها برای حمله به ایران را غیرقابل‌قبول و مشمول حق دفاع مشروع دانست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/677145" target="_blank">📅 02:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677141">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
نگرانی ترامپ از حملات تلافی‌جویانۀ ایران به زیرساخت‌های انرژی منطقه
سی‌ان‌ان:
🔹
آمریکا به‌دلیل نگرانی از حملات تلافی‌جویانه ایران علیه زیرساخت‌های انرژی منطقه و تأثیر آن بر بازار نفت، هنوز تصمیم نهایی برای حمله به تأسیسات انرژی ایران نگرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/677141" target="_blank">📅 02:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677140">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
یک مقام ارشد امنیتی: برنامه گسترده‌ای برای پاسخ به دیوانگی احتمالی آمریکا آماده کرده‌ایم
یک مقام ارشد امنیتی:
🔹
ادعاهای رسانه‌های آمریکایی در مورد حملات احتمالی امریکا و رژیم به زیرساخت‌های ایران را نوعی دیوانگی قلمداد می کنیم. چون ما برنامه گسترده‌ای برای پاسخ اماده کرده‌ایم که شامل زیرساخت‌های حیاتی رژیم صهیونی و زیرساخت‌های انرژی آمریکا در منطقه است و برای آن اماده‌ایم.
🔹
نیروهای مسلح ایران، چه در جنگ ۴۰ روزه و چه در تداوم آن در هفته‌های اخیر نشان داده‌اند که هم توان انجام چنین کاری را دارند و هم اراده آن‌ را./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/akhbarefori/677140" target="_blank">📅 01:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677139">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از یک مقام آمریکایی: ترامپ در حال بررسی آغاز حملات علیه اهداف انرژی در ایران طی روزهای آینده است، اما هنوز دستور نهایی برای انجام آن را صادر نکرده است
🔹
این حملات همچنین ممکن است برای نخستین بار طی چندین هفته، شامل مشارکت ارتش اسرائیل نیز باشد؛ و چنین تشدیدی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/677139" target="_blank">📅 01:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677138">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
نورالدین الدغیر خبرنگار الجزیره در تهران: در میان افزایش لحن تهدیدآمیز واشنگتن علیه ایران و بسته شدن تنگه هرمز توسط تهران،
نشانه‌هایی وجود دارد که حاکی از آن است که مذاکرات مربوط به تنگه (هرمز) دست‌کم در شرایط فعلی، برای رسیدن به نتیجه نهایی با دشواری مواجه شده است
/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/akhbarefori/677138" target="_blank">📅 01:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677129">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_xo1A2-JzfhroSFlLZ2a84XBWUEY7i-NLC3KxDVR9yjNfBDIudgSt670rqhOBEdGa7aZSO3Gl8tnr7uDR710R7kNJ_ykP0FqNcH21J2_uZQvhsj-eNDSeo-I7tKiYNEVyTlpvqOnJeu8uau-PgBs-3OdMGirbQbWAZEYphIrqFuA26x524S2xn8X4W0sVJpTXF4IzMvzWPo-AbL_77m1vqUEniNC-tuiPMgy41324SXr4XxSFY7Iy9eaEyAe-38bqQ9TH7ReGd_-nyAZaAEjf2W-FvU2NyQbb4ViIFCqncTTq8GVzTZ_uydp7A3s02EAIEb9g-Si-_p1aZi4tPnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUbG2zJ5rNoiI4mB3MKiyiGfqy-sj7mUp4xvm_7HlhKIgrHzvbv9uEIP1LTT6u6vTtrm0jn1owTUUdasvDCDkSKbTuxm4KLqhYkmeiP0TjnnRZuV5yw2S82DUunYvXBPIipo61Qe6IfVsbnz1MgiRDEHT1mIeY5MZUR_r5T3uVJg8JPAU1ag9LeFFRuw-fifQ5XCmvuoOwVvao6YfRB75_XRdcHFkzniKvvFLRu06ASkY3Tm2K0cEJU-tdq_COYwokpaDSDTH7nl9EnrMDI047Raf-sLi_yiZD2sPw2TShxx6P-7d-P90l1RNZwVEbShCCR3VpEifuPqr-XBD2pkYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1p77JLFa-khSLUAmktEx9wJHSQUZJi2R_wz-vbELu_lb4ojhTE9L_XiyFxJ-gUqgaOBp2aQO5U7opzGIBY7YY68Yr6dWQGDwsGOMUBmycZfYmX78_cgL63JyPJShkNM8CEYwQ0PTq1UPsaCrZ7Cr9U6O7UX1w3LNY-KvXUfAR8EURS8wG2qBjOfK3QKD0qUTWAtib93o_Ucz7NfYYN_E03RgoHpudt3oIFipxdMOUOSzHWAskzN7iOxN1DvnaNGIqBBvm5-yG-McyAdObfwEBdvJUqP-efRPDa_FRGBmKfg4V2tqsBqdXC0cfLYiEZVw9ZROKTgOIs6y32IBOPC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUKY7zo-vT1pcSJBdsNwjqX7MsCePWxdnpCyVA9-SXR9GvjZQZE3ofaXoeuxYbEsGSFYNocIGrlwo8pMg0GgspJSk44-XlYReYuAoQvWsIz4JAAMa8drMcIqPWFTtCjWwkQDIi7MWozXyp6EbcClsjowcong9_Gg-s-5ctT-780p1195z0xBK6mwGMNhwRMPyQYhwda4PWiBDvx8fJJqm3FoEmAppwfCNUzZh83vjqWb6RFXR0sjeFXvPiA1tv1LjYIZ3SwitzTY6lec2-IFip7LvqFrw4tZI01lV7_Kwe-ykgu62YBP1HHiPOPx-H0p7IlgUiKlfy-junjMSYH1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJurk_zMf-Z9_ebfuf_PlAr1FQTUCpfjxXhmLQUJx5YP6q6znZYKvzNNUWU12v9zBJwiRKnT5LAqy1suWa2FdPbKfLABYWbWmFe1-BRsJp1-nBzNPpMG4sbt_ZjApqfXO19OxlgcxSjIV9PILo4vHLyjai6ts47byvLKC15-0pDPMs6PT7cslzImoi3CXQX9Qhy5vtt0sdaKVtL5ICxuc8iD4gGwTWe9PTYy4GRYaMJV9dvqzapJuE-EPk7kyzEeYHSnBQ_i6JPDW3wq3SP2dE-Gv3p_8DQjXnMp7iI8pZE002GR09xaadTh8bNGifalQIqEeKtQbPUhtIMUT7QWWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROGpe-X5gvfBMqfZUILlGjVmMxrBaUSUN3j4sTzshl0qeycruYrgkrkYiaEzIKTvXrxR8x3uWApuz4hWPD5tFDUwxr5DAjgP7dvSGsLmYL7KC4F0BXwmGb6BlCag4FL65iKhzCWHcXeE1hwVbzWKEt-AYIE1qC-2oiv4t-8dAaesksqilMtUASdjqKhyB5XPYNim5fVm0V-Q8bKYtnIVJjaDBygRryOjuMZ_Pc_1zmHaa0dBNH_nSV1TWoHDS-936nHqHvRrVQQkDX8CAlEu2ox0hpWczlrYtNAdCCDGQ5ihuJxJXKWM8yjvYnTXyQuZos5qmC_bO3hmrYySvbzZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5RKQcrLOezXamWiNDO9twCSf1p4yU86V894GW0Cc-HN8MFFrSqAR1yzBq7Cnn0p3TDZEU6QUvduPwT-7carrJ260IfYCPfKOy6TwGMeYduCS_jygYlynauTR5RNLmhNHn6VEuuHPclTBfjd8-w2udbKdf_CuBqQogpJqAGgs9WdrpSoaHFwwXL2JuJZQEM2mtwfxLPHhktYYcNf3Ak32cl2b52jQUzSRgUXQkzeF9QJvlT703XR2Bn8OzqmMLVDFT_mRWmeGo9oWr8A0RcBqknZ2Gg3EtQkXZYQrOkp96m0Zi-bMBv4G9SNKsOc--Lh2175F4eIzTZyWDQhnEbHHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0AdbCZkQu27bOjFySRA4w9jhHczExyuV2vZoz-QaWn_CwfbdA8lb3hexGDX6mLhGr_yjk8rnmIXK_IxT_HYFIbVdC9nY44kXbDmTI7_0flqaozTPC6BzNLMyQtNUG2WUM52mgFHRdMKbJ9h3UKzKoYvLAg6U0abbVz4s-EbW3WzhR3Cm4XM2ViU9KCXUmGIynKx93CKYsd0p_M-k7cG_TxzzH8V0wl6snIm_nSLj18MYpJ_I4Hs21sgAwRz3XnDWJakwGY44_kjQ8ihkhRkdE_sFkDeFnAvkX7M6nN0M1flJDHIvQkL2zGwSdXAsat1_VLubeI43OqEV_xfLSmvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUKSN5vQzk0zLPO6OipKW2CICT-GmTNzJUq_qiJQSqS2FHFWgaFUlA92ZB-ceBLN5T6WzL0NaNzNxZ11PBEUfcrbW8uI0pIDAjhZ8QAHDrNKOsRUqggQg6_wSmYCNpKzWJUDr_LXfGr30AQx2ZlQAZ3N3CHvq2l7GTepdWeZ3JTJ70aeUxne4NZUblyF7N7tXEHeWWv09AK95FeoZnJtg1z5Z3y5LGiVqgOBYHFT6WHvWW1Pv26W0TWyoYUNquEBB8iOAl7FYFKKhlm-0fj_HO_NFk0XwpCgp52Wtz9YMgXG7HJMCYiyjVuCA2px7zNyjS4z1Gj2dmz1BhlHtEy3CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت از جنسِ ایثار
💫
✨
آنچه از مکتب حسینی به یادگار مانده، تنها یک روایت نیست؛ فرهنگی‌ست از ایثار، همدلی و خدمت.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با توزیع گوشت قربانی، این فرهنگ را در مسیر حمایت از خانواده‌های ایرانی زنده نگه داشته است.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/akhbarefori/677129" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677127">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9Yrzcvagh11FMmFVLJ75D1COW-au5tmescEKc37lXC-u7skzoGWinLRmZy07FjME4GWhN0QU44P8pfP9B-3BlemAgwFEl0jjl_iBjPQLtIK0WPjYnGveyd0gj8IH7aaQgS75aoKSUHdysp9XRUETlaJeBc38jGmvo5kFwCHiXMzGwD49dNMLS3Xwt9MKCrUfAzagdoZ0FQost3CU9u3jZe6Yz5EZT9t2ICPXvLGTy0aNQi9kA_QuhqLYCac6CBaY946WqjkGebqGmazmV2iijQlSSG8-p-pJFreqg-GSDYsws2c98VSrV_xnbjMeqEM67fgFMlhYeOjJaQ5Ho2Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش قیمت نفت به اخبار این چند دقیقه درباره حمله آمریکا به زیرساخت‌های ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/677127" target="_blank">📅 01:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677126">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
فایل مکالمه اخطار نیروی دریایی سپاه و برگشتن نفتکش ها از مسیر غیرقانونی و بدون مجوز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/677126" target="_blank">📅 00:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677125">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
رسانه‌ آمریکایی سی‌بی‌اس در مورد حمله به زیرساخت‌های ایران
🔹
رسانه‌ آمریکایی سی‌بی‌اس در ادعایی عنوان کرد آمریکا و اسراییل با فرا رسیدن پایان هفته میلادی برای بمباران زیرساخت‌های ایران از جمله نیروگاه‌های برق و پالایشگاه‌ها آماده می‌شوند.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3234572</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/677125" target="_blank">📅 00:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677121">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf23f5a92a.mp4?token=mGqfFqyoFGHPPbDyJm8WAdej2KYZgwcIoZttRTCY53JmHMqmr8_e3D2AWxNSFXRyyDwxtT7Xc3VR2PqR9OMed3DXEr3t3IX1MmxZthRY5QOfHyE4qOFZl_rGejYG_tjWFGHM1B-RdmrF_nvtEHEbXM6KVBOeqbfQGhYtgwf82sDrpytOJ9QOn66-4OF5z_fQa4HYG4MBMSm2ZPW6yRvOpaiOKog_sTGE93sraRT7PWn1YjxVmkLAwDBX5r2uNvv2GzKkWO__eCtIAR88nrG8S1r9GjQ-MZzEhi7ldbg3nKsjIJrjoxA4mBvANVKtc6972oMcpiIJa-t4BjdyNWWVyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf23f5a92a.mp4?token=mGqfFqyoFGHPPbDyJm8WAdej2KYZgwcIoZttRTCY53JmHMqmr8_e3D2AWxNSFXRyyDwxtT7Xc3VR2PqR9OMed3DXEr3t3IX1MmxZthRY5QOfHyE4qOFZl_rGejYG_tjWFGHM1B-RdmrF_nvtEHEbXM6KVBOeqbfQGhYtgwf82sDrpytOJ9QOn66-4OF5z_fQa4HYG4MBMSm2ZPW6yRvOpaiOKog_sTGE93sraRT7PWn1YjxVmkLAwDBX5r2uNvv2GzKkWO__eCtIAR88nrG8S1r9GjQ-MZzEhi7ldbg3nKsjIJrjoxA4mBvANVKtc6972oMcpiIJa-t4BjdyNWWVyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری: من پیش‌بینی کردم که قبل از اینکه از قدرت کناره‌گیری کنی، گرینلند تحت کنترل عملیاتی آمریکا قرار خواهد گرفت
ترامپ:
🔹
اگر این پیش‌بینی را کردی، درست گفتی. در واقع، باید روی این موضوع شرط ببندی.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/677121" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677119">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqS8VjuAPThkWWlR_BdcXJantZxhrjjwZ_Ecs7P5y0bp5yye14mlajXN_EYQAuKtrpQQWcKncEHsM5Z51XKBgSt0JEHXMaUA9zWSG6KeDTCl5TUrpdptxiUgv9xd4ziuojPX1yG54zyj31HR8JSKvW8mDZsGp0WQBPWYX7RQ8cma9euVJWfBCgG4inMpKLTwHicXc7EV9InV4XDjYq7UK4wbkEGnZeXYhTPIHA6FmVePZglMF4WyHO3Bvd283UFimBEj5mcA3kZmFlEwz5LwM-rx_khM2_dmmZAUXFRifTlrNt10OaR5QX31y4EmXK5VAX_b92dw75udpPO2Gq-YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یکی از جلوه‌های زیبای اربعین اینه که پابه پای عراقی‌ها، ما هم از زوار حسین(ع) میزبانی کنیم
#میزبان_باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/677119" target="_blank">📅 00:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHcgzo6qEaJhU5K56ere1YUrVCmtbXVRPWi3RBTIXzCJpNbRwN9fsZ6DMvLvdmgNKZbMcSRi4QKgrTlDJFfW-BC7MrdesKrIR87BpiqrMxYhqcQwxBh325eMbwajoVgnWGIj8JoTp9fQr8Ga4fQ48FFg8X3KaIrti3ol8ych1IDKh7nWsKWr26TFhqpgC9cwGFsQXtoX8hyhc8hUrc9vEvxeao1cdTLHfv3OmkcOcnZEmjw-Vi9LOBof-cSOcuS30jXYO7DZoVC5uZFnMobZh5wmzfsQT9ckkkLUcuvq7BJEKeRjgFEFDflRteAQgQlHb3BDdbRcmJMqmrxv0w5G7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
از مهمون بودن تا خادم شدن، تو طریق‌الحسین فقط به اندازه یه پیش‌بند بستن فاصله‌ست. برادریِ عراقی و ایرانی تو همین چای‌خونه‌های ساده معنا پیدا میکنه.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/677118" target="_blank">📅 00:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOLLtgglD7KxGn4Mi2uu1tBfQK1PjPy6-5TPywQTuyxQIgF6lPhQAAxSegxwZkOOgBOacLlbJEoeQjMOIwNMoT8JNoqN-B8I3Zen9yxXKal1Zzrfo56mFvKijXbdVEemY_X8YF_G88u_7rTnSL9XayS79u350Ilx3K0NUsnTXy9YN2oJDCVkB3SR0yVMONRgsLg1evmwXR3fi-yIKVsTYcnCFMszY3vfdfqxnjsHp64sTATDctbv_Tna2tvBp4Dk8HADTo18xensgPSqxfdKr77k-oURJFjE3Bd99IYNk5Cp1D_FtTKh9SY2Uah22rB1LTlAVNH_bIZl65775yFuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/677117" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677116">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
گنج ۱۲۴ هزار مگاواتی ایران؛ ثروتی که خاموش است
🔹
برآوردهای سازمان انرژی‌های تجدیدپذیر و بهره‌وری انرژی برق نشان می‌دهد ایران از ظرفیت توسعه ۱۲۴ هزار مگاوات انرژی‌های تجدیدپذیر برخوردار است. ظرفیتی که ۷۱ هزار مگاوات آن به انرژی خورشیدی و ۴۹ هزار مگاوات به انرژی بادی اختصاص دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/677116" target="_blank">📅 23:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677115">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
تعداد مأموران شهید درگیری مسلحانهٔ دیروز در شادگان به ۳ تن رسید
فرمانده انتظامی خوزستان
:
🔹
شهید علیرضا فتحی که دیروز در مأموریت مقابله با قاچاقچیان مسلح مجروح شده بود، با وجود تلاش کادر درمان، بر اثر شدت جراحات به شهادت رسید.
🔹
پیش‌تر هم شهید مهدی مهدوی‌کیا و شهید سینا سیاه‌نژاد در همین حادثه به شهادت رسیده بودند/ فارس
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/677115" target="_blank">📅 23:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677114">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab10cc9b66.mp4?token=U4Z5_y7tIsulriwsW3AzZnbP_2SxWTFB7jc1vcs1O2zwvpw4H7cEAzMBB4BEcvusPQRmhU8trjP8p7L1465igs7ybNQn9NF_tlz5Bw0CF1W5Ay3WvN3qELh__tGtghD9VZaKoflh23s6PzyFb_umLRdjyX5eouBVh1iGlF-4fvnETSOO4rXXj0p2rOeAk9wHv9Z0wKGFdib4RrAQUK8FR4VktlmSfJb064j7Dz0lcJph-H6_xBZAT1md9kc6oeRTjoky8MfRhMJLDC14HwWDFTu62fyRqBe3QFIaBk_K-aZk7lSrzyi4tiwXT5aIfdZ5ksXUbDSvfIfDl248A3qvfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab10cc9b66.mp4?token=U4Z5_y7tIsulriwsW3AzZnbP_2SxWTFB7jc1vcs1O2zwvpw4H7cEAzMBB4BEcvusPQRmhU8trjP8p7L1465igs7ybNQn9NF_tlz5Bw0CF1W5Ay3WvN3qELh__tGtghD9VZaKoflh23s6PzyFb_umLRdjyX5eouBVh1iGlF-4fvnETSOO4rXXj0p2rOeAk9wHv9Z0wKGFdib4RrAQUK8FR4VktlmSfJb064j7Dz0lcJph-H6_xBZAT1md9kc6oeRTjoky8MfRhMJLDC14HwWDFTu62fyRqBe3QFIaBk_K-aZk7lSrzyi4tiwXT5aIfdZ5ksXUbDSvfIfDl248A3qvfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون، مجری آمریکایی: ما ایران را به یک قدرت جهانی تبدیل کردیم، و این کشور حداقل تا پایان عمر ما یک قدرت جهانی باقی خواهد ماند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/677114" target="_blank">📅 23:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677112">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emp99Tnl3b6ivsQpfl70uiablkuVkA7v-4J0HVAi0lii5OL5ybx9Mhef6EbYVy1Ez-uW0Hd4LLc1n_6hSsp0aNofAhTLpeGIxn3BRgir_qwrR2geDPt-BMCQZzFnZc-Rk1OWJcr1oTgPEsS1pP1fNcbAIvywrS0qavPk7HwiDqshxjqXOsASiGNT7trzfnWOsi_IviCpE-k6vxzIC9nliyMp7O3_FV1RpCzFJ_qx1ASgorm5p6czZQ9qDVSeCPwlUU76g_trtV6RMPvZ6J6HZ0UZntbSInJycBGhO3ZDb9rgbLotVCjayswIK41I47F_YjEezG37AJ707ew0wOCa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UiUEysvGXgtHbnAiBFLBwN64MRUEc7f3FjmuzxYUxyShve035ggLg9IT_Z61i7ljOi7gF-vCsiQtgOg4m6rfv72RDyPGGPznHny-gFaDfJ5c-rDiBpYEz43M_kCu1JOzTrTr6hD7wOw8tAzzpHJWgXZ_NgjsWzMSqceNGnHjrT1Ii-ZiF8aZY3y_RnqE6gJ6jmc4LXadxLnKht0NLHsstx4P5vCyE5jVevtQQq1W0f-mKlc764Ys6KNJ142i0dwBkyONTRQw4awM2OmsTA24KEk5p3eLL-vkXqvLq3K0-oBDY7ya1gr5pGCRskhkk-GhRPvXy2YDCvKn7od1tBy-jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
امید عالیشاه با انتشار پستی در صفحه اینستاگرام خود از هواداران پرسپولیس خداحافظی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/677112" target="_blank">📅 23:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677111">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9cudVq80xD-OzwZYhxZMXmaVyKYa7dAwOzBOEhRExr6UkS7cPuel74DuLs1jlZAVcVrZlsPiA65V6ypAaF12dcHXxDFZU_FtOPJ9PJMfwce3wYbgI9Rm4FwBPlle0SKu6nl7u9-uviVpatQ4vrtWtpaJLDqATPRHW3qK7h5d13hFFU5qC8lbxcOMKEY5_6p1FPcrQjLTqpvbV2LfbMMBFh_Px7XZsBZ7VsW0BsZHJWcIJtq89NY7IQJLWxtJFdZl6kIur7kdMFZIzKrZzqgA9TT1CQucRggENyp4aDR9lvqXgENFSTnlJ8n5BpPbHhO9DNlb7qH5KX_I9uDXzt7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
۱۰۰۱ سفر کربلا
✨
▫️
همین حالا با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲ در پویش «زیارت به نیابت» ثبت‌نام کنید و شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/677111" target="_blank">📅 23:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677110">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acBll130bGO2lazDFo7CB4fKy7_Ex0VrwH_WZxjkvyuuLa3y6k2G6sl7c7HAU_xQkTJocNEikRCjuZlMdv0nnPBfBJO1maaSVjNj9b74_rm2ahRJGiAyaQ94jo0fJVuC2HM6AoBCZcV_7XtX-K3UxTYFO9f8DlHYcP--nPRMezgaWfXb0Sx55wqVC6lPtYCWakY0YvtfVN3-Dsi82AKzCg836MO6TTqekssyauIUT6Lf8UXlLG5itf07H_aFU_czniPaTM5w9dkMpCSbtPlr8ixFk-RQ7kgd7sQjzsbADLxLee2_FFN6LAjUmRGVAH0on1IwXejnOH7weqXHwW_H5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
نیویورک پست: سنتکام طرح بمباران دو هفته‌ای ایران را آماده کرد
🔹
طرح شامل یک بمباران مداوم دو هفته‌ای است، نه حملات شبانه محدود که در دور قبلی درگیری‌ها دیده می‌شد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/677110" target="_blank">📅 23:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677109">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ماجرای حمله بمب‌افکن‌های ارتش به پایگاه العدید آمریکا چیست؟
🔹
دو فروند بمب‌افکن سوخو ۲۴ ارتش ایران، ۱۱ اسفند سال گذشته در پاسخ به حملات آمریکا و اسرائیل، با عبور از رادارهای پیشرفته، پایگاه العدید قطر را بمباران کردند و خسارات سنگینی به آن وارد ساختند.…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/677109" target="_blank">📅 23:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677108">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جنوب کشور در جنگ ۵.۵ همت خسارت دید
هادی هاشم‌نیا، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
۲۰۰ قایق شخصی و ۵۰ لنج بر اثر حملات دشمن در جنوب نابود شده‌اند، چندین اسکله در سیریک و بندرعباس آسیب کلی و نسبی دیده‌اند و به‌ صورت کلی ۵.۵ همت خسارت وارد شده‌ است. خسارت‌ها بر اثر جنگ باید اولویت‌بندی شود و بین نهادهای متولی تقسیم شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/677108" target="_blank">📅 23:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677105">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df730cd0b5.mp4?token=uuayB0sKJJwKMJbc1KaWpIE5Ec-SPyJawNecPOriHrJOd98HSl0nYWToN_ndVTNZ2SVKOqkMnw6ULCLx-Kt2VJDB2SGfeNe_qdYPOTRK2wYZBTIOUfxHdybd-izPhw3xdnV6fymteBscvGHi2sB6PYmJIyC80nksOC3DVYqd6-gd269fkf9D65-Wzx_ei9fPQn_dls5D7_2IALdqI749EZ7vg-WVimtcDtlv_yS8BlBMbk_blaoDl6ULhkmWMb8Qe3tQQc4jGp0z4B6hsFbeeJ-eTwpRVggCZ-uphdujEEv9Tw3cOHZ6dftZCWbxzt3SJCeqd3lfty6ar3pi784dWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df730cd0b5.mp4?token=uuayB0sKJJwKMJbc1KaWpIE5Ec-SPyJawNecPOriHrJOd98HSl0nYWToN_ndVTNZ2SVKOqkMnw6ULCLx-Kt2VJDB2SGfeNe_qdYPOTRK2wYZBTIOUfxHdybd-izPhw3xdnV6fymteBscvGHi2sB6PYmJIyC80nksOC3DVYqd6-gd269fkf9D65-Wzx_ei9fPQn_dls5D7_2IALdqI749EZ7vg-WVimtcDtlv_yS8BlBMbk_blaoDl6ULhkmWMb8Qe3tQQc4jGp0z4B6hsFbeeJ-eTwpRVggCZ-uphdujEEv9Tw3cOHZ6dftZCWbxzt3SJCeqd3lfty6ar3pi784dWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خدا راه شکست را به سوی امتی که در برابر ظلم ایستادگی کردن، بسته است... #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/677105" target="_blank">📅 23:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677102">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nky-uNatfgk3TvS4XJFzBciCdGuna9OCOeqptKTWXaeJERwd9-mn0V3nQxP4Wmxa3idu6L1jMHvtrjZj2HUrTaw1OfOWtOLuHRunVsJQlJSi0Q4_BQbc8ztqDnpfxOSUzcWE6cVnWCuuVElfuBMajQ_FICwDia3X7neyB1i21ekUlmEl8VqFdVSDJtuQutBpOd-Keh7c_hCCHfdsMQt_lFCWdxL6Q_VNup2giHom0ui5hUUYV09Um6fyS2IP3cUIhFKA9jYEeBPyCO5dxx3cKm_3MAqmv1FkjFF0TLd-rTeDqt3SNKstk0AN3ZkuS6LqcXokWSdBwE_pyyHu66GP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاوشگر کنجکاو ناسا دریاچه‌ای عجیب از الگوهای کندویی‌شکل در مریخ پیدا کرد
🔹
مریخ‌نورد ناسا در دهانه گیل، تصاویری از دشتی با الگوهای چندضلعی ۴ تا ۸ سانتی‌متری ثبت کرده که می‌توانند نشانه‌ای از وجود آب در مریخ باشند.
🔹
این ترک‌ها احتمالاً بر اثر انقباض و انبساط گِل ناشی از تغییرات دما یا خروج آب از رسوبات ایجاد شده‌اند. کنجکاوی پیش‌تر مولکول‌های ارگانیکی در خاک مریخ یافته بود که نشان‌دهنده شرایط مناسب برای حیات در گذشته این سیاره است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/677102" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
