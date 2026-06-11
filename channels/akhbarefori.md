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
<img src="https://cdn4.telesco.pe/file/hz1dAJAz7YUKMn4vI8n8wN7bI4_Yn8SDCs5GkSkVTmPAybU9qVca62UqqtJOxMys8T4hAMqvcnAURn6BduFGp4A8J_BtUWJCYByslbIfZez0ErOErVGwMizN13ur4TQFdBtWRdRt_hFwALlKUrFZMeatzWOeGSxt1psgIZLMHai5861tOwfEvRQP7WSmciPjZXQQEG_oLQkRYnrtKIhmotdp62tZKGKMBzqIGcBkLRm4IMM044TJlmSV_aXyAEgaRMLLbfKBbP0gO83345hIdGmxTrNOn6Q8KVwyjBRFYJf-QV0cmkfd5XfgA-vcMApwGCMGYju-3NLkjUSJRZ4R9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.6M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 22:11:38</div>
<hr>

<div class="tg-post" id="msg-658556">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تسنیم: تا زمانی که موضوع تفاهم احتمالی، از سوی ایران اعلام نشود، هرگونه اخبار ترامپ در این زمینه را باید به حساب پیامهای قبلی او گذاشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/658556" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658555">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرفوری
pinned «
♦️
عقب‌نشینی ترامپ: حمله امشب لغو شد  ادعای ترامپ در شبکه اجتماعی تروث سوشال:
🔹
با توجه به اینکه مذاکرات با ایران به بالاترین سطح ایران رسیده و مورد تأیید قرار گرفته است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده امشب علیه…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/658555" target="_blank">📅 22:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658554">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
فارس: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
🔹
هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تایید نشده است؛ این را یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران  گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/658554" target="_blank">📅 22:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658550">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eheEAyXKWl3_lD35AyGzIrtE6VGpLo64OtgFCcobla7XhDe0NxQK8xb7OX2UBAoRcoDWlJY_AnyWMjR6KBnlKo8UwDZQCfuyutr-b5pFa4Vsy2N0__RjOiCXwH0xyQSK9DAbk0_gaol93VN2GOWhNcJCAykuQ02LtKxinkkbgGFO3oUB9LK9J_M8UA4EqPoGz_gG67A1vPXyk7OmvVdpB3P8RfyvEAWZaeZwWCAPvveVgeVMANyKWcaITXiltX-2_FddEH7dMMILJFK_qruQEmV2igIeLa4WYh2RvOX7QZVy9Bfwgdr0R9CjkdDAqhSRldHbswk4nkf0FML2WzOUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pf_1KECv4MufljAN92TJlUKie6vuKwf8krjYlkTxiDJTqTfG-2WG-M59CUbkTWmelGsfw-ETHfhHIePHg32og-XEsrCpL69Cu8Mmd-IbZFZy9eVhaoNYq3vxvx_7SYFwtkMzGGY9zoBp4aGgGWbGqF1anE6avKh5DM3A5LYF3Xh_PLO-_UFUwe-FVxOXmDFrcrgGW9u0zHpEiNm0fNezgTOunR2R86i5h8KNUvjSlpjfsoq1uu_Jzy68ZlsXzhKX5VJAKfBi7ZypSMKVg3mHoS8eoqCaycn8uZ4HR0MLQhmAbv31BM6pnkYxUsDhiLW4rsGQ9omAtHMKSVE24HqBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Imeo1Gp4jt2XtqzukdHg4pDyufsV1kTGuwz-TlLUf-YureA9yEzCaBqlwEUoiG7eEGU-YK0d_cUCTVhV3Rxr_46S3BSkv6xy_p8a4LAxXXrFU98N1GXTg7fWKetFl2qAdMjOzePBFUxjKp3mgE4dgWa7WW4lKTPjgrtt0T_ZH8livrkYckyjt_K7ESr2P8KpTjXpLrZhgC0xGlwqpbGuPTrHaTYGbazGz69Jgy96ImXd9NiBbZLaTSETcjST_RqzfmgREZGnWXISVzkZOhPKdwJ_oTslP1ZHdUfMDeKXLcv1HC65SczRwXN8Fa7VXLzL2aA84POwDPARfMgyaRDa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTsEm511po6mCc3GRRZHKoT0FCv9H_pAwxDCWuB_WpUoXdVnNsiDUR0OWnRjtHX0Agsc7qA0sRhbWr1PXHLxQVOsERKcMSvh5CubbLr7LfZGRMcjvlKjQXoBhKx2IfGglqrIqJ-dofgNUyH6jnhixjlH5Q3B1aqxuyykc9DVPI-HiIVgfc4Hr1E5--5_UtanX6FIqRDkIqOUYV5jgg16pclW4elJd1iHLjdOrPln0g4Q0ym8XrtJTLH3EOco_NS1T7IhTs0IMH0s5rkdyNy_UztGDjJl4b2Z5FhCcIlh0o10ui8koROUG3rfP143dx2Qesy_ug-sos_Iu9X7UPNaAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری دیگر از مراسم افتتاحیه جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/658550" target="_blank">📅 21:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658549">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23fb166215.mp4?token=NVnhenlaeXEZBFyyjzz9EKl_N28f6hTJJkdBLaV5VBf1SSXz1t-M-ooEcOgRp7qjibUKdQe91Mi3hbIvcZXLGV9FWSiApBWL-MezilthJQyhN_-VoPjDIl7SbX1sGVMjYidBopkLvs5Kwk0gIB5dXkyouV6M7_F9ETE2uHZNfN9sDMWvf6dEfOwrF1TwZ6mLZzFh5sMMT-WsFnjVZyfdRbvWxKeKxgLnWPWBdxo3YKgPpb1ouqg5VDd5wTg8YJLDY5hdroW6JjYPD6stwZ7b3YdoCO-TSSYvq1I4m0_oLsWaAOPVd2Je5ngJgtBSfvi50uHj9qktF5F-k17UCN-EiS0YyZIYyRfph8gj1iEjoi3CiU48pgjCFPAEuc_Rf4IMWIDvfKwLVEiexkSAAn1JM_C1jf-bdYiXKf48GXQ6kwsPZnpsinphdkC_iiA4RmwKLsG0rwy8ZsY9-09spwnCUeUl66bncgiLCF31shX936wKfUxp4Ba43qHxomNbexnLxARGDw2dpYg9MK8taW31T2kJPJtJQdoCdEnPunTEHAbJPHoVXyVz4Tnb1VvfqAdL3TfOZQ9kU3PaX9Po0aXi1W_hls6XWpzEddhrMsJmeUheP82AENNFR80zc3-F8eRxnXLRfL1m1Qx4MUcy5BQEiAEc3diZU9ZuQRzZR2y81Hk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23fb166215.mp4?token=NVnhenlaeXEZBFyyjzz9EKl_N28f6hTJJkdBLaV5VBf1SSXz1t-M-ooEcOgRp7qjibUKdQe91Mi3hbIvcZXLGV9FWSiApBWL-MezilthJQyhN_-VoPjDIl7SbX1sGVMjYidBopkLvs5Kwk0gIB5dXkyouV6M7_F9ETE2uHZNfN9sDMWvf6dEfOwrF1TwZ6mLZzFh5sMMT-WsFnjVZyfdRbvWxKeKxgLnWPWBdxo3YKgPpb1ouqg5VDd5wTg8YJLDY5hdroW6JjYPD6stwZ7b3YdoCO-TSSYvq1I4m0_oLsWaAOPVd2Je5ngJgtBSfvi50uHj9qktF5F-k17UCN-EiS0YyZIYyRfph8gj1iEjoi3CiU48pgjCFPAEuc_Rf4IMWIDvfKwLVEiexkSAAn1JM_C1jf-bdYiXKf48GXQ6kwsPZnpsinphdkC_iiA4RmwKLsG0rwy8ZsY9-09spwnCUeUl66bncgiLCF31shX936wKfUxp4Ba43qHxomNbexnLxARGDw2dpYg9MK8taW31T2kJPJtJQdoCdEnPunTEHAbJPHoVXyVz4Tnb1VvfqAdL3TfOZQ9kU3PaX9Po0aXi1W_hls6XWpzEddhrMsJmeUheP82AENNFR80zc3-F8eRxnXLRfL1m1Qx4MUcy5BQEiAEc3diZU9ZuQRzZR2y81Hk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
⁨ ⁨ سوت آغاز جام جهانی به صدادراومد
⚽️
آماده‌اید برای روزهایی پر از هیجان، رقابت
وشگفتی؟
🎁
این بار هیجان فقط به مستطیل سبز محدودنمیشه
💫
بانک شهر با برنامه‌های ویژه، جوایز جذاب واتفاقات متفاوت، قراره حال‌وهوای جام جهانی را برای شما هیجان‌انگیزتر از همیشه بکنه!
🔴
همراه ماباشید تازه شروع بازیه…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/658549" target="_blank">📅 21:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658547">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
درک مرگ اطرافیان از جمله همسرم و .....
🔹
00:07:20 رازهای مگویی که از گفتنش منع شده بودم
🔹
00:18:40 لحظه‌ای که متوجه مردنم شدم
🔹
00:27:30 نشان‌هایی از حضور روح من در کنار خانواده
🔹
00:33:30 واگذاری مغازه و امتناع از فروشندگی بعد از تجربه نزدیک به مرگ
🔹
00:39:30 رؤیت مرگ همسرم در برزخ و به وقوع پیوستن آن در این دنیا
🔹
00:59:20 رسیدن به پوچی در پی افکار علت خلق شدنم
🔹
قسمت دوازدهم (صدای سخن عشق)، فصل چهارم
🔹
#تجربه‌گر
: مسعود نبی چنانی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/658547" target="_blank">📅 21:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658546">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
عراقچی شنبه راهی پاکستان می‌شود
ادعای الحدث:
♦️
وزیر امور خارجه ایران احتمالاً روز شنبه به پاکستان سفر خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/658546" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658545">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قهرمان جام‌جهانی ۲۰۲۶ معرفی شد!
🔹
یک اقتصاددان مطرح آلمانی که قهرمان سه دوره گذشته جام‌جهانی را بر اساس مدلی اقتصادی درست پیش‌بینی کرده بود، قهرمان این دوره را هم معرفی کرد.
🔹
بر چه اساسی و با چه مدلی؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/658545" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658544">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای نیویورک پست: ایران پیش‌نویس یک توافقنامه را از طریق میانجی‌های قطری به ایالات متحده ارائه کرده است
🔹
منابع می‌گویند این متن نهایی‌سازی و برای بررسی به واشنگتن ارسال شده است.
🔹
یک منبع آمریکایی دریافت این پیش‌نویس را تأیید کرده است، هرچند جزئیاتی فاش…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/658544" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658543">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
عقب‌نشینی ترامپ: حمله امشب لغو شد  ادعای ترامپ در شبکه اجتماعی تروث سوشال:
🔹
با توجه به اینکه مذاکرات با ایران به بالاترین سطح ایران رسیده و مورد تأیید قرار گرفته است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده امشب علیه…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/658543" target="_blank">📅 21:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658542">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084dc07fe2.mp4?token=V6-Wuwgd1RFrHl6ZYalNqFe2eVtlOQhytzlJ4Ypz9Syiw_-PcjlLxcJAMSvLq2uBqwH_Qcnt35qxs3lSl2fjKF3P1dD1ZM57WKtAI2NgXfmIYylR-EQinm6ft0mAbx9rns3FI4dH9WxCYVwyHIR2dlWkADe08_-Ua4PMHEyF7NfBZUr3MN008gFJ5Zc41wE3XsJ9632HC1cgTBgM0GRHMTt4OLuYHYCSvH9wzlVvhZPOrAljGbun2zaz86FAssplBpbiIF2r19eckZwk7e_doUWbH6CQq_1oyI2c6jZ83-nk_frPUWfvRBBsMAqGomqb-2OfsGrmKCDRSlwcMKoeWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084dc07fe2.mp4?token=V6-Wuwgd1RFrHl6ZYalNqFe2eVtlOQhytzlJ4Ypz9Syiw_-PcjlLxcJAMSvLq2uBqwH_Qcnt35qxs3lSl2fjKF3P1dD1ZM57WKtAI2NgXfmIYylR-EQinm6ft0mAbx9rns3FI4dH9WxCYVwyHIR2dlWkADe08_-Ua4PMHEyF7NfBZUr3MN008gFJ5Zc41wE3XsJ9632HC1cgTBgM0GRHMTt4OLuYHYCSvH9wzlVvhZPOrAljGbun2zaz86FAssplBpbiIF2r19eckZwk7e_doUWbH6CQq_1oyI2c6jZ83-nk_frPUWfvRBBsMAqGomqb-2OfsGrmKCDRSlwcMKoeWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم افتتاحیه جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/658542" target="_blank">📅 21:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658541">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSWnCS_GCkODUnaCK2tK3rmM7l-l39Kl2BiOmCjKRckHmQs4VjrXF_6MAKIb6nl0K1dPXs34U-LEiG5vWJKjqrKxe74373SVoILIknpYxuxcAHg5dJ-37lVEhwHusuNcpKILqxhFIk2RFGFPJffr1EcNaTAIjF_k2I1l13q4-P38PH1wpkowUaYokMmbw22V7g4DUxJFxHzbKK2XmiZU6YR1knj0ToLcdJRXtyim-WeQe7eQAnxxtgjkIki-rLcA51YmwcR-HSXuCSj98m8mRqZNgk1OCINSr6BHZF0clsLCvpoPpKUdRW2VyMfATLleEcnu1VwtxGGTsu1myI2YHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تبعات دادن امتیاز میزبانی جام جهانی به آمریکا
🔹
ورود هواداران از کشورهای سنگال، غنا، کنگو، ایران، اردن، کیپ ورد، ازبکستان، اکوادور، هائیتی، مصر و الجزایر به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/658541" target="_blank">📅 21:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658540">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtZ3mVuy0c9Fr6adl2JjJyMj-8NwUNRZt6oh4ITzdfftHdhK9fdTQ6M2pYnt4JPcibN0NmwQaB__zvCjeQTyvmXnpuF68WzC8Z316Ot2Qhj7kcLNnPNQ-egvg5UK_MU4JLu3KpWadPBDJt1RrKkwTSCMojmiTdGTv7fBclyUk2CkuWrAhGn24aVnIEM-XWxONUNoxtUnjXcFX0LPpMANUwkGPtiX5QlKIY51uNOhK_B2ANr2ZhBGJv7pVkAQcOBHX4BW_J_UW84yEeV-ttZxDSLHMRjNZXsKAZoy5iWhteamlQEKIMP0Q2yXpo289y1TAfqHpyePqiK1Ywr8-f_WPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت به زیر ۹۰ دلار رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/658540" target="_blank">📅 21:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658539">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oh6VVWdna3U9kMq4tPhuPfR5uERw3gW_aaYCl4Tug3Gao5Zhm4p2ooNYfCtW3lhz9IatKHL_IanjvHCzTrvM6rhUEWltVxD6AcwHN6Cohq7GDS1wQ_43hFgHBo8Vu4V9YzJfwdN1-GbkHtJa7UGh2LPpY1x-ULulb55o_WCcL50FohK7hpO-cISgYUWM91Wf-X2Th89-oREA3sR__DRa6qKISJSpjjYWnMOm49xv94FneN-bVT_g-beJ_0w3t7aANGQ25tMuc1_HnIRj2lqLYSTcoWVMvvSE8n0FjuJP7SO6BBdOq061FltVDuIxYVGcjAhQwNCPn-95LlBOFO8WWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موقعیت رادار هشدار زود هنگام AR-۳۲۷ که گفته میشود در کوه دخان در بحرین مورد اصابت پرتابه نیروهای مسلح ایران طی حملات امروز قرار گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/658539" target="_blank">📅 21:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658533">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gh_NL9PIGjuTxIujMdII-UG16X23CkWJFpJHG_lgyAWz4LPpCpCI860QT1hh6rB9N6iqeYiwOxXHIVPvHSvM9oAhBAF8Q-I07wcVd9zzb9YINvaGMh03M5olk3510-TmUXcE9V4GFA9dZ6QI2zYmeEaYyUv01pBxcL9n7PDQ0FMvlGbUfCfyF6qVUdk0Imwg1Ej_10G9x38vEVRBHqARUVmHuMhxrs6wnCLa7Udar-gsdYELakOkuMi-Rpmelwpj18kzkniTBdhDxx2aN10ZQ0NK3tSiYNzzPwsnCDvygFmMWSHtwVkbEqnxoG-bGsK95Uw-2btoTovE85dVyMYE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-AqESLEClToB1ywUoU3ReQe1XsOgpKMQlFJ134lgwo9My8mcfMjBQZtlJIG28oB4rCUznI8G9Wa1ZMFUOPC0W2i-YUR-LoadT3tQTFvGrK2Hqa2Z2X19r4YEkPGIMaP2hYymYX7Vv4GyHrbjhUXuKmEC08jUsTJ_2zsKf6jF7TEdqtxzXklO3-8_thNOgLNI2qyyidNKDOmmfzUhBtuaBFIxLGYS043G8TIYQulyXUf2QpB-3FDwpuujfPNaJdRgNrqwq5C4QFIsAIxLxDWKgY1WXEm5xQVN0nEiPCylt_7IsBGRW6VC2f3lEsHMpnTQA9WjcRGmcw55_fTqDKnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxsW3Hn7fWyceL3fgfAGwwpH_8ju72SJO0bbCK-ZvPmQMs5klwjpWODeElhEiniMQnur4Sn1nZNOsQ8sJ2k4JawSPrJmbfFFdquzC3aJ3x4vcpVDFryae45p2A5qZ4pzOTtrxcQX8w6psMwu10DW-hL3_MgwDQy0jdKLKza69lCQt8MR4tateVjVHUsPqyblWtf8JqJlNsDSP33eOg1mHq3FPA-F-IpPJnefo0ApRUS0OPBdCKpdgZFDxc3eYfL8Lc4BPeLS1LGt41W-RnsBByd3ALjjh-v9FGzMYShUSvf3yQvqnzxwYwi7hFVmmbsyfeSk2i7Hs4Cy5XuGyaVcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOXYYeEkv85Fwk8K_xuZy6HtVBRVOgjq7TbG1YIjoMjJDls7ubEXUTdm9Yid2e5rI5Hgcg28CYzOjwQFhxgiOdNoSBX_L4OXhCcaK7WU-ybLqlL9sI6KYAwDPngRG-14IQ9UXySZL_0xzch1aylX3mdjHylLHUcwpShnhy2PMp8VSo6XTuGG9Dmw6yXL2yHJwWNFGfKekRGEpokUpLsvDejPlIFQGfWCz7Cz1GMu1CRBm_iIcjxcgiEG60FVK4q6iDgRytJXgLf32rgKW_XFdWXqwzUIjKuN4O4BHyE83_196Q2IrWEe4Z0HirxNrCd4NI06bDwUcCyjflVYIaZ5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vD7JZQmY-fbsZ7Dj2GTC42FGJHwE7gzqM9NoSfdqBjyUDvq3RuyBg_lNieFGmH8CE90QBt0H764Xc1wNxtY5zcS6AbcYR7qzWMF8Tg1Q4XrisfZavPphx5z5ha4LqfZbjMsMKyH4v5NhAEhbJadODIvTGj7qNmadNeA7f6rs0lbiIuknGS_bUd41NEH3rURGFNit-Mrm7at5eBxF3rQgv2eiAO32pWQIHzE0qG5W4M2LFwgEitYC_TEZ297xjNmPnYHSaXOgwjGfuSrnBz6LlBPFUWjppcM7-137iAnjCxh1CJ3v2pA_rPxDkpbQDaUYxbTkCUy9efxVZ0KT5HDLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dT4xfRooQa8siHd5FAVZa627wwUOAgVGdGNoPNzOWMOnT5tZOtglc_4h5UCOUuC7P_6GeUrm_M3mZ17OHrFzEjpPi1HEFEBjNdUosULJ8R2oanWRxUHkZatIZIP1FT16GS6LoiPxcZALUPhN7MwR-rm3EN825ucvxRAFhyD2S_nM6c_i3iHQNQ3mUnnm9-azoBjFwQ4TR6zfcuPD_W2Xw6TobvTiuv2WVzXWEXH2q2yek8_kH4CKXAVU648yvr91miCiLc6WKjG8rXETPDgO2ObNoR8fYQ1bMKTltm9lmq_CRplieYXFP49c7ECt6UOA1kJeGWQBZkyht6p1ZVqazw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از هواداران فوتبال در حاشیه بازی افتتاحیه جام جهانی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/658533" target="_blank">📅 21:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658532">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
عقب‌نشینی ترامپ: حمله امشب لغو شد
ادعای ترامپ در شبکه اجتماعی تروث سوشال:
🔹
با توجه به اینکه مذاکرات با ایران به بالاترین سطح ایران رسیده و مورد تأیید قرار گرفته است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده امشب علیه ایران را لغو کردم.
🔹
مذاکرات و نکات نهایی، هم از نظر چارچوب کلی و هم در جزییات کامل، توسط همه طرف‌های درگیر شامل ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران تأیید شده است.
🔹
محاصره دریایی تا زمان نهایی شدن این توافق به طور کامل و با قدرت به قوت خود باقی خواهد ماند
🔹
زمان و مکان امضای این توافق به زودی اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/658532" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658531">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB6cqKr_rPbFi9rf2pC9zPqvlOhbTTyyYchNZOUrtv2w4_vUiRyQ1XPBpjlj6FbLbHsoNrEJlaYE8Z4S1Fg6y-fWlFAHCmwE2_UYe3iX84K-WFd9b4lR4U8l-sz4Cn9_VU7MYrtooMXDmkpJn9FgZAmg0BznRwDUKPMiYCXw4UV_F0wlZwO-vfpvGErIwh3OltBph2m5ib73FqQDB6V88_fjMe--MUOE6w20KtSEoF3ibF7U3VY3OqaAkHmYjMD8NxAOgGdE6-dixRS-X992N0Vsw5bqKBYysq299POKfooQpzKvXiZMFzzsYvX4Mh1cDw5V4p41BnKEIJvEwPwNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین رتبه بندی شبکه های صدا و سیما در میزان مخاطب/ سه؛ آی فیلم ،خبر
🔹
جدیدترین نظرسنجی در خصوص پرمخاطب‌ترین شبکه‌های تلویزیونی  توسط مرکز افکار سنجی متا  در سراسر کشور برگزار منتشر شد
🔹
مطابق  این نظرسنجی‌ شبکه سه در رتبه اول پربیننده‌ترین شبکه‌های تلویزیونی حضور دارد.
🔹
شبکه آی‌فیلم و شبکه خبر نیز  با فاصله کمی در جایگاه دوم و سوم قرار دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/658531" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658530">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciZK72UTUGxpjfNI4MkXx1a2IialHq4PwMo-IvJWJxVxnKMP_tY3fTbTICAVexIFz1epdJ_xi_KKBgIGWr0EkaeOHPJlXNK7nkM-EjqrRE_GE3qy4zZuueLCkumjSWqNJBG-yXQrAQ9QHCI4ohtW0DVtnzKfQtQX_RmowhMiMYSUfRjSWLUv57mAJF2xJp3K7rTspt-gifQzjczxeoJAjyf_jJrzF1dY4CMDyuUEfe8dFjJVMuX5LkoyDeWUBdqkUuNED56ehEJevw7uNl0Q82VICn7GOoJOXNseBvjR4nmU07VHc4lqGvbtEJmPEAHY3oMoeyHcg9yosdfcWg7bEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جوان‌ترین بازیکنان جام جهانی ۲۰۲۶
🔹
ژیلبرتو مورا، هافبک مکزیک با ۱۷ سال و ۲۴ روز سن، جوان‌ترین بازیکن جام جهانی ۲۰۲۶ است.
🔹
رکورد نورمن وایت‌ساید، بازیکن ایرلند شمالی در این جام هم شکسته نخواهد شد. او با ۱۷ سال و ۴۱ روز سن، در جام ۱۹۸۲ مقابل یوگوسلاوی به میدان رفت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/658530" target="_blank">📅 20:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658529">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
هرگونه خطای محاسباتی دشمن پاسخی فراتر از تصور خواهد داشت
وزارت دفاع و پشتیبانی نیروهای مسلح:
🔹
بی‌تردید نیروهای مسلح جمهوری اسلامی ایران امروز از آمادگی، توانمندی و قدرت دفاعی قوی‌تر از گذشته برخوردارند و هرگونه خطای محاسباتی یا تعرض به امنیت و تمامیت ارضی کشور با پاسخی قاطع، پشیمان‌کننده و فراتر از تصور غلط دشمنان مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/658529" target="_blank">📅 20:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658528">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv9r0CZzeSlki153tR_NQ5EG4kUnj7BFMGxnNd7niNM5hecKpMTmtGqrxsk9FzldEZP4TmQcbmmrb6Q83-xffW9AOqmgHNXafOPk4eh4zt7zulVLb-vRWaODQ_jZibF6FuJB3jQZvNTVcg1KJRV2BNhWZ7dLdHKtk8l0jLA2Wztsb95rgklCFBTco4rYjPmCxT2NvJPKWaqHVn_xjbpuPDyUHsgbtt9AZC253FcTljp3uJGwWqw1Tz21NicBtIUKd2XaVvNJTaQ2pOWx8QKY3iTQy697W2GIFkgcoKXlrJIpyHlMuJCNcu6ZNu8sRijcVGwe7IDOhzyG1XY36tmVKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دوره "جنگ ضربتی شبانه" میان ایران و آمریکا/ آیا جنگ‌های کوچک به جنگ بزرگ می انجامند؟
🔹
ضربات محدود و کنترل شده به راحتی می‌توانند از کنترل خارج شوند. خروج از کنترل به راحتی می تواند سبب ازسرگیری جنگ بزرگ شود و دو طرف را به عصر جنگ سخت (مانند جنگ ۴۰ روزه) بازگرداند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3222279</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/658528" target="_blank">📅 20:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658527">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbAdJzfPQ9Xuy4l_z4hsXazq6Gn0ftAPYIjWfDOGmwukYJhDrJ8MHyRpvViEi5CisgPYcDf3R4ZavfUjM1Sj3OHGyzgIEjYpauoUATgiC20OOq0pcjcUjDxRmmLHOUHkC7xR_Uj4Yzh7QfunrffNulN0rhxhmBYWCZ1-gE35NKjnJJ1QZdfNl8rlSRsfd9-m6YoaTnaGkT7JuvOM0jmje4TeAgFZtnROtR43VGNuwZ8LYILxzQkaF2U-njaRMlruRmHoi5aS2cYyqb2tP4P_XZN3i92MIZCmLDThSN7naF_-E5P3ks6DGGnSuqfyiXU-SYdF4TeggK29tkeMnS1M9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خطر هجوم مار و تمساح به کمپ تمرینی تیم‌ها در جام جهانی!
🔹
به گزارش نشریه مارکا، ‏پس از اینکه تیم ملی سوئیس هشدارهایی درباره وجود مارها دریافت کرد، ‏تیم ملی نروژ نیز از وجود تمساح‌ها و حیوانات وحشی در نزدیکی اردوگاهشان مطلع شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/658527" target="_blank">📅 20:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658526">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نتانیاهو نشست امنیتی اضطراری برگزار می‌کند
🔹
شبکه ۱۳ تلویزیون رژیم صهیونیستی از برگزاری نشست مشورتی امنیتی با حضور نخست‌وزیر این رژیم خبر داد.
🔹
این نشست در پی تشدید تنش‌های اخیر میان ایران و آمریکا و با هدف بررسی وضعیت میدانی و ارزیابی تهدیدات احتمالی برگزار شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/658526" target="_blank">📅 20:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658525">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMVf3cciIQwSaPrKlSDz2EXcoV8moCACy2zKNXJA73T_rwG5mXgxQHo781Z62djDmRTFjIDRWj-gOmSIayt_1NbtIDCAop-l6qYKJJBWJW6NjBC8Su5p5HPMhNpoIDWwAi9eHhLhcXkA_0tmnmYTmrjajGSLYAclyHsk3ZL_kRyQ6j9T1rFzTsRJXFp7Ne1YR1sPP5tzyDld9bdNZdvNnM_jzFU1oJxIpERrAWmxx909RIGStpAIfGF2QI-v53sQCslGAOTkhjZB4vd2hzf8DD-GUavC7CrLspFE-v5dZSjjravr-57b4ym4tnS42wAfnTJntpSq2P6rjphaxss0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: توانمندی‌های دفاعی امروز کشور فرسنگ ها جلوتر از دو ماه گذشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/658525" target="_blank">📅 20:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658524">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7619da40.mp4?token=A__IsvJY9K3KI_7yVgfuKcnmQneWkBZecpAYBWw49a7d0vkgsZHBdY_pG3IFXKQPVgrPpBVHJbYJUBrZQVuwc45sF0DugEQr21sddCW0WOWTDFausUoCjRgxpNCWoBnToycZpIOusqhRTAA2nLzof8JCWAOACkwezOwOLe7hHek-8-NMSRtszokrxgMUHAh4Alblco81wBl1XYX7FR9VB0q9HFJlNGnuDQrCFlQm4j0mD4Uj1YBh5L5sswGlJhAk4lkmSx3x34bQ2mPOykMBPt4_nUq-2V40342I5RxTZrquQhyQ_WKOBOyDZJ5RIpkWLkvwOaZ-o2RK0Tq8uw0T-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7619da40.mp4?token=A__IsvJY9K3KI_7yVgfuKcnmQneWkBZecpAYBWw49a7d0vkgsZHBdY_pG3IFXKQPVgrPpBVHJbYJUBrZQVuwc45sF0DugEQr21sddCW0WOWTDFausUoCjRgxpNCWoBnToycZpIOusqhRTAA2nLzof8JCWAOACkwezOwOLe7hHek-8-NMSRtszokrxgMUHAh4Alblco81wBl1XYX7FR9VB0q9HFJlNGnuDQrCFlQm4j0mD4Uj1YBh5L5sswGlJhAk4lkmSx3x34bQ2mPOykMBPt4_nUq-2V40342I5RxTZrquQhyQ_WKOBOyDZJ5RIpkWLkvwOaZ-o2RK0Tq8uw0T-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درب‌های ورزشگاه تاریخی آزتکا مکزیکوسیتی میزبان افتتاحیه جام جهانی ۲٠۲۶ برای ورود هواداران باز شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/658524" target="_blank">📅 20:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658523">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
هشدار نظامی وزیر جنگ آمریکا به کوبا
وزیر جنگ آمریکا:
🔹
برای دولت کوبا عاقلانه نخواهد بود که تلاش کند به انواع تسلیحاتی دست یابد که توانایی هدف قرار دادن این پایگاه یا خاک اصلی آمریکا را داشته باشند.
🔹
هیچ کشوری در جهان نمی‌تواند با توانایی‌های ایالات متحده آمریکا برابری کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/658523" target="_blank">📅 20:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658522">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromtalasea_mag</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0zXdJ1sZlpPpx9COgVKtdclheorwImHiC8W5YM5H8EyDeVdfeTsMJpVjO5BMLfmgnk8-WQUcenf0O3EICLQrVQ79fI1pZhlrzwLcFmCDoSwce6PrYhdp8QUwzUDT1XB5u2rHYIeDe4HKiwscVzdiKP9Lz2NJaK0aXvQMprhPUXdceSAKdqN9LmN9PVZJGUdOGkrGcnjw6be9b-tBEF1f-3ieU_lxuFEFNHuH-0jGUBwMOBXjjG-O_gBh49YvjE72ZJSXK_AAewsOVwuB-C4LGYH5BLSOl_9dRsBEQHmz2Ucr5NevAGoiFNtByIf988KP_6TuGLan3L-uYzoIXJz8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/658522" target="_blank">📅 20:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658520">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794ea7d026.mp4?token=DH3eBA4zRJpS7gwJOxNOYNBbNWYE3KlfH2MPrh9uf-i1VpRfTZSK6wYYPFkglD4w2cCtzjq1G6-5O5EI5klYjmUTnh5fDGDbOvmJnKFcwummxye_I0dxPqEG7alWG2228s6yut_Q5elfSU2WUDK5bSVuj2K-WiVidRoZiO-_U1B1wiYyGFWd7dldOOCsL5fo0R4irf-vqdSWzKMYFOdHxcdP3aT0UwpvaxzRr3qlSdszQVjTUKgdC1WJj7Hu_totmYaVMM1RjuipDDTfRsv59VI8VTPl8X1_pHqE6tBu8j6vbFPk3QdyoZSOFLR5milM5epr_gnr-8i1J9yltFUXFXIWlvqhvUOCwvFXw6xrrmd1WwVVo31krtKF5J7evqUWm9TrGqrE51Di80JUPVwiJ3PCAVZPy9rAL-ZBkVy9IzfReng2b39bvkcGvLYYBBJPN9klMEijYv7eiCGUytPCLnWdJIQtQ1uBLjYU0M6yYck1ncsGC2O8zjen-2ZbON2lTmeV-7h6GEnsXgn5v0JJooVnEIe_cgNJBVOP1rZHYxnTy9Qp_mcoT88PKSfFix9IWCPR2xz0ZP4igZagBKcwM4LBek2YKP9VZT7CAKegSGHjS58sL8BbgsL9nloDM6ZfxBCcnFIDmwVhn9dZFwdVtYm94vPE2WAtBbnTd47FIQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794ea7d026.mp4?token=DH3eBA4zRJpS7gwJOxNOYNBbNWYE3KlfH2MPrh9uf-i1VpRfTZSK6wYYPFkglD4w2cCtzjq1G6-5O5EI5klYjmUTnh5fDGDbOvmJnKFcwummxye_I0dxPqEG7alWG2228s6yut_Q5elfSU2WUDK5bSVuj2K-WiVidRoZiO-_U1B1wiYyGFWd7dldOOCsL5fo0R4irf-vqdSWzKMYFOdHxcdP3aT0UwpvaxzRr3qlSdszQVjTUKgdC1WJj7Hu_totmYaVMM1RjuipDDTfRsv59VI8VTPl8X1_pHqE6tBu8j6vbFPk3QdyoZSOFLR5milM5epr_gnr-8i1J9yltFUXFXIWlvqhvUOCwvFXw6xrrmd1WwVVo31krtKF5J7evqUWm9TrGqrE51Di80JUPVwiJ3PCAVZPy9rAL-ZBkVy9IzfReng2b39bvkcGvLYYBBJPN9klMEijYv7eiCGUytPCLnWdJIQtQ1uBLjYU0M6yYck1ncsGC2O8zjen-2ZbON2lTmeV-7h6GEnsXgn5v0JJooVnEIe_cgNJBVOP1rZHYxnTy9Qp_mcoT88PKSfFix9IWCPR2xz0ZP4igZagBKcwM4LBek2YKP9VZT7CAKegSGHjS58sL8BbgsL9nloDM6ZfxBCcnFIDmwVhn9dZFwdVtYm94vPE2WAtBbnTd47FIQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانک مرکزی مخالف افزایش قیمت کالابرگ نیست
🔹
منابع نزدیک به بانک مرکزی می‌گویند بانک مرکزی معتقد است حمایت از معیشت مردم ضروری است و تقویت قدرت خرید مردم باید در اولویت باشد.
🔹
به گفته این منابع بانک مرکزی مخالف افزایش کالابرگ نیست؛ بلکه مخالف تورم است و معتقد است منابع کالابرگ نباید از محل چاپ پول باشد‌‌.
🔹
حمایت از مردم وقتی اثرگذار است که از جیب تورم پرداخت نشود. اگر منابع کالابرگ با چاپ پول تأمین شود، افزایش قیمت‌ها خیلی زود اثر این حمایت را خنثی می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/658520" target="_blank">📅 20:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658518">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB0mBF7Ns33VTyZVPSxWTvG0YuLaRAMe4za1YqxHxCfpW5iXAy1Ae4RYUBxmb03wbfXQYzXc08ix5c0AvJVSRKlod2LZ6VyDJLYeB1USfawHZj3J_Zs9PHPmOw2LS4vlBsP6Q0stCwhtcCCfnQlscOAagvDqc92GtJXwt_HqIpkwyoFHmdqN3mSqMh082tWxRieYHx5ANi_PPqxKdqO4O8hfMYKyjbQGy2eQH7l5mUKscl10sUfdTBxK7Hn_UE8ju0Acamz3SoH-aDWn5RT4cOqYGuJfJmd0epP3IEOWWKN_pKILH2dJ1IeDFykN9huN7obLTa2SNrRKemHuHmbp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خارک ما
🔹
با وجود اعلام آتش‌بس میان ایران و آمریکا، در مدت اجرای آن موارد متعددی از نقض تعهدات از سوی آمریکا گزارش شد. آخرین مورد نیز شب گذشته رخ داد که طی آن، حملات نظامی آشکار و گسترده‌ای علیه خاک ایران انجام گرفت. با این حال، این اقدامات نتوانست اهداف اعلامی مقامات آمریکایی را محقق کند. رئیس‌جمهور گستاخ آمریکا امروز در پستی تازه مدعی شد که در آینده نزدیک جزیره خارک و سایر زیرساخت‌های نفتی ایران را تحت کنترل خواهد گرفت. این در حالی است که ملت ایران در طول تاریخ بارها ثابت کرده‌اند در دفاع از تمامیت ارضی و حاکمیت ملی خود استوار هستند. جزیره خارک بخش جدایی‌ناپذیر خاک ایران بوده و خواهد ماند و هیچ قدرت خارجی قادر نخواهد بود حتی کوچک‌ترین بخش از سرزمین ایران را تصرف کند.
🔹
هفتصدوهفتادودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/658518" target="_blank">📅 20:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658517">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d7dac072.mp4?token=bgnYfdzn-toFUVzVZdPsi3f2jd2Ezg8dCS5l7Q4CYtj9Jm3Z75U9MmVH8wHQZkTkNvqpRT30ZI5DfgIVv--dlshHQi64Degb6QxFpl-aRpg6mAIvID2gfcL23Yhaz-wY0hNpZbTFzaGpHTA6QjFpjDi7Whdh7G_YZW988Lwx6cFrbdl1XkhrQJsaoHyv8s3dc2q4wxsQdd-tRlZ9RzFA517e8Gxkuz3j0Rca_LBZTDssLUWjOpKmYFv_SlW0v9OmOREOw3Jt3A7E0S0fVhgDt8WEHh2VuaJt2Dhmezc7gBD3vJS-_tLN6pUweBnF5V9LIWwDN-NrZr-t6roKk_gepj9wvKbll59jtNGzs1uAV-V9y51qlH7ZY1tB19SLtJR_WSo9f7-JJaduQZTZzpNogEnsxbr9h2-3zDLDo_tsupWoFN_WUQWbMpia0m0VYXYGqnCy_G_ABEKqIIPsMCV2CrsG91W-AWRAFc9VdYEu2vjGTq7velAn6U-HOt2vL3bORVR6j5PmFKLdIgwbz9BE8RaWILLIXZP6q_CB7--noPh-KRl7mRQBdbeDnHgp0C-kRFg8VSf_bN5l-F-PCfnFn5mxL0roVj-YsXk40JWn1njv6_KKkSb1iufo6YmBKxKUcwmkElMzBUa5rMhHBZ-hSQSphj6fpooAq8j9E0AGVGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d7dac072.mp4?token=bgnYfdzn-toFUVzVZdPsi3f2jd2Ezg8dCS5l7Q4CYtj9Jm3Z75U9MmVH8wHQZkTkNvqpRT30ZI5DfgIVv--dlshHQi64Degb6QxFpl-aRpg6mAIvID2gfcL23Yhaz-wY0hNpZbTFzaGpHTA6QjFpjDi7Whdh7G_YZW988Lwx6cFrbdl1XkhrQJsaoHyv8s3dc2q4wxsQdd-tRlZ9RzFA517e8Gxkuz3j0Rca_LBZTDssLUWjOpKmYFv_SlW0v9OmOREOw3Jt3A7E0S0fVhgDt8WEHh2VuaJt2Dhmezc7gBD3vJS-_tLN6pUweBnF5V9LIWwDN-NrZr-t6roKk_gepj9wvKbll59jtNGzs1uAV-V9y51qlH7ZY1tB19SLtJR_WSo9f7-JJaduQZTZzpNogEnsxbr9h2-3zDLDo_tsupWoFN_WUQWbMpia0m0VYXYGqnCy_G_ABEKqIIPsMCV2CrsG91W-AWRAFc9VdYEu2vjGTq7velAn6U-HOt2vL3bORVR6j5PmFKLdIgwbz9BE8RaWILLIXZP6q_CB7--noPh-KRl7mRQBdbeDnHgp0C-kRFg8VSf_bN5l-F-PCfnFn5mxL0roVj-YsXk40JWn1njv6_KKkSb1iufo6YmBKxKUcwmkElMzBUa5rMhHBZ-hSQSphj6fpooAq8j9E0AGVGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای که به وضوح نشان می‌دهد تعدادی موشک مستقیماً بر روی پایگاه موفق السلطی سقوط می‌کنند و از تمام لایه‌های دفاع هوایی عبور می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/658517" target="_blank">📅 20:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658516">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
هشدار قرارگاه مرکزی حضرت خاتم الانبیاء(ص): یا صادرات نفت و گاز برای همه است و یا برای هیچ کس امکان نخواهد داشت
فرمانده قرارگاه مرکزی حضرت خاتم‌الانبیاء(ص):
🔹
آمریکا از یک سو حرف از توافق و مذاکره می‌زند و از سوی دیگر شرارت می‌کند و این تناقض آشکار در رفتار و گفتار آمریکا عامل اصلی ناامنی در منطقه است و به همین دلیل امنیت تجارت و اقتصاد بین‌المللی و کشورها، بویژه تنگه هرمز را به خطر انداخته است.
🔹
هشدار می‌دهیم چنانچه آمریکا بار دیگر بخواهد حملاتی را علیه ایران قهرمان انجام دهد، پاسخی شدیدتر از قبل دریافت خواهد کرد و آتش جنگ علاوه بر ناامنی در منطقه، فراگیر و گسترده تر خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/658516" target="_blank">📅 20:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658515">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmdwrZ1qzt6v6I0XM04HrqSQCNApsoHBkpyi7TvaYJcmOwszS0fIttJedu7ZEghdtb-N5whWyA2Otj_--qEmtYPtYrvlCkDD9Xc0bWFpbp-pmVHIoKjrjvpW3oeFPlaBzfKs4wf4WpwjmypkwwUZ78ce5_HPDkhA4U-PPfXaoU85XQ7Hq8ZoFRbOp2WXA6-3_sYg4qz5fTPGfpJGC-BqQAxSy1-isktS2uEdKH8O55a1oX_cn42YCbKBmwe-5AT59ALN9AG1TOipgmOXKVTajyJP1-riLQCcdeyVV7ywV_pk57J-Bw-8EtA43ySFTeoHjcQEr-Qe9Fd10fWMb_2R-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه: اگر آمریکا می‌خواهد شکست‌های قبلی خود را دوباره تجربه کند، پشیمان خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/658515" target="_blank">📅 20:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658514">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHsTGAMmFLyJlJnMkzYk3X57WPlvZLhhlgsEb4fFjJHL-2HqwMs1QVQ4l_0HLLR57p4DlGvij37KEiWuMYMA__BbxPHU4lVUK60hm7bE9yfIu7N4YbHD_LoJAs6oqND8sA2Yopoi2fLY588tIauvTveLWsoqmPj8zf8ujK3qMsJfrOZvbLkfIu5rq3qAyzBuDVBJb_d-SqbQdGsgfPyMgjKPz8eA4rCmo7SrI74SJTpOADuLBaSIT_hmxGs01GxT5SxFZkGSC0L6nhakTVU0JWCdQVgtmgtTWnmGB_HGgsYKkn2wpMI4ytqHu4QbI-jIYLi6m-y-h_jc0u_djJgKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساعت شنیِ انتقام به کار افتاده و عقربه‌های زمان شهادت می‌دهند که هیچ جنایتی بدون هزینه باقی نمی‌ماند
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/658514" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658512">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K51X_3DMilvECRNca77_3ZU4Fs9JHPFNsUnYJ93VGk5xO3sNrgEcsbs3PByPgf5yJxqQTbh_9UNxdebKxNPZWRV4BErnfttseLaA2pK202kfUnshC9CJrAHZ3CL7etdd-oq5hyHyomCAG4_96rYB7oCGFN2zFnORZeDOrwyrSZTdJoSzIO97M6Ocb0q9czu_sHgHyk_lFJamQGZBvsQQf86x2ZzXXJji3xMjlxlgododWxZvnXGznqCnqIvK6NO5OFZYTXnK2lU5DvwK2gPeHEQHcZlWamUFBCtzkwduVFwrqj5gag4vKWbqIdbiOVnphudHK9-gJW5mOqzF5Eeddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWRd_U-YNgBNt1Rrd0ki9bND5d1zNi0sqfv4Sy6xt9Z07OX8t71dd3Jxse6FAklKLNZM294_BkglRuDoIIbTCC2j5m0F6ih18pje3xuJbUeFhdoLsBaOuzAd9VpWUCGcyT_AS99JfQcF0zFAFa0R5dvfW7r9Gt_ORtbI13wpFnj6oBNn3KE4aNjf9xAR_ePrFhOfR0hy8SPwtnMHuEU4wzWSlhqM6Lc94UEsfVmkjXOHxHqv8yXxBBB1rTMdKefVOlcKXkTpZhyBzcWS3FGna5jczwwGrV9G76boQ4CHBJvb-ZMOna9-ypD5y1lduMaHe4UNzVzLbXkggeV2lO_Mow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: نازنین
🖋
نویسنده: فئودور داستایوفسکی
🔹
«نازنین» داستانی کوتاه اما عمیق درباره عشق، سوءظن، تنهایی و خودفریبی است؛ جایی که راویِ نامطمئن، حقیقت رابطه و فاجعه‌ای پنهان را لایه‌به‌لایه آشکار می‌کند. اثری رازآلود و تأثیرگذار.
🔹
مطالعه این کتاب به کسانی…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/658512" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658511">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43e891a63.mp4?token=Wr9LjvzjlkkM5VELeSZp7v4MQ5kS9TgjkFHBI4HmZPnfu2LlhyrgqcK17GUyYeqWHuMHTY128AWV6Rm9bYKau97LiYfTSA7BzoWFpOY2m_KQKPaM72CkSMAZKkOUL4B2ao9uW-JLvW6YJr5wvW3XLVAj2K98qfaY9V8oBgEv4vIu5XDt3J21D7b5zLauaj4_NqRIv84J5eIlkMAX_yVil96W9mYaBpuZUYQzWUA_Wc07a-Wj9G-A_6ruaWuYpuNeAb0LTjV8KenfuJ2GZTVUm7dyYIbqyWtgSE88v7JcMIjTMb1UAU8r4UqsN1TS2lcsf8XwaED537tHMFwzCx8udQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43e891a63.mp4?token=Wr9LjvzjlkkM5VELeSZp7v4MQ5kS9TgjkFHBI4HmZPnfu2LlhyrgqcK17GUyYeqWHuMHTY128AWV6Rm9bYKau97LiYfTSA7BzoWFpOY2m_KQKPaM72CkSMAZKkOUL4B2ao9uW-JLvW6YJr5wvW3XLVAj2K98qfaY9V8oBgEv4vIu5XDt3J21D7b5zLauaj4_NqRIv84J5eIlkMAX_yVil96W9mYaBpuZUYQzWUA_Wc07a-Wj9G-A_6ruaWuYpuNeAb0LTjV8KenfuJ2GZTVUm7dyYIbqyWtgSE88v7JcMIjTMb1UAU8r4UqsN1TS2lcsf8XwaED537tHMFwzCx8udQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یهودیان ارتدکس افراطی در اعتراض به طرح سربازگیری رژیم صهیونیستی، بزرگراهی را در قدس اشغالی مسدود کرده و باعث ایجاد ترافیک سنگین شدند./جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/658511" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658509">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf43df983.mp4?token=m4cz5-d18QHWmA0uCeo38KHo-Av9Xme67R6cru7UB_Hu6Qr9P92-Qim_fX8YnkgJeqQQVr_2vzdGXSvG6QSnyNeEeDFVcNonbfpY0t46cNgcW65evBr22Knd1i-GilhqVKD8emR--FeHOBogramoBt0b2G91hUWJmwqZxzWkYt9cTNo9QSDE5sdoWLnQaatFOxePvBDxh5BlAI1E2PXYDHcPDWmQY_IHjOX94KImXcQDZJVAAjWVHRPp3oKSY3E0UzGWu80kiVjcE3G2uy4pg3hsgdAu_G_jtBh-4sA0OpGCz22a_yjVmVtvE0Cy5ZO-5QCRjo1xGx_j7Su6kzYqHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf43df983.mp4?token=m4cz5-d18QHWmA0uCeo38KHo-Av9Xme67R6cru7UB_Hu6Qr9P92-Qim_fX8YnkgJeqQQVr_2vzdGXSvG6QSnyNeEeDFVcNonbfpY0t46cNgcW65evBr22Knd1i-GilhqVKD8emR--FeHOBogramoBt0b2G91hUWJmwqZxzWkYt9cTNo9QSDE5sdoWLnQaatFOxePvBDxh5BlAI1E2PXYDHcPDWmQY_IHjOX94KImXcQDZJVAAjWVHRPp3oKSY3E0UzGWu80kiVjcE3G2uy4pg3hsgdAu_G_jtBh-4sA0OpGCz22a_yjVmVtvE0Cy5ZO-5QCRjo1xGx_j7Su6kzYqHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلدینگ تبلیغاتی رسانه‌ای باران برگزار می‌کند؛
"نقطه تصمیم "
🤝
همراه با مدیران و فعالان کسب‌وکار، از تجربه عبور از بحران و ساختن آینده بشنویم.
📅
یکشنبه ۲۴ خرداد | ساعت ۱۶
📍
هتل نوین پلاس
🔗
ثبت‌نام از طریق ایوند
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/658509" target="_blank">📅 20:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658508">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llYlFW3H615aARj46dzYcv7Q474GvR1ZWqWt1RfrqjzcOQ1-akHE6JbcXKHl8H1wLmIZ8wuIHn9Mh-032UBvdvbBopUePUotaWiWr1JH7E_ITmOdY_OyZvY4vaUqmQ-WD_fUrjBR-Uzz_K8P7eWfqWAnhifKtpjVNUYWHg46CdSLCKIUgAnWDc-8c0CAP4ZAxOO-zSrL8Gor1yOfG2x83d8DyQxKAuIbfZ1jWAY51y0eXvPy-_5ESZ8YVvo5cdAr0PYczeclJ8cmoqhSqYZ4-sG5NmzuHlXIm1flu9nCeCgMYeBKdKTv8V77b_FHexBRIb8RV2D22gCMINru-dQGTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام پایگاه‌ها دیشب هدف موشک‌های ایران قرار گرفت؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/658508" target="_blank">📅 19:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658507">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
آغاز مذاکرات امنیتی مستقیم میان ایران و امارات برای کاهش تنش
🔹
پس از ماه‌ها تنش، مقامات امنیتی ایران و امارات برای نخستین بار از زمان آغاز درگیری‌های منطقه‌ای اخیر، دیدار مستقیم و سطح‌بالا برگزار کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/658507" target="_blank">📅 19:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658505">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSJ8YGUO-uwTPuJRRFrxQnk9wWPSFblz6MwM4fnHVz-_efDlY-YHD_WxBnCt1OygWKPoeJFQMpzUeZZZ9w05UdWXomIB6YJsqEtDUQ9WSpvyj4JEjO0oggGSiHO0YHhPAVmN3c4SZR_uS2Vx3YQmMHs3iYmD5SVwZVqDnzrfeYavxZxTEZBG_lYGGdJQTOHe92EHWL8pZ5FAyUJtzDA4mA2206hzT2HNL5wJVrVm6s9aL0narjT2XrU7REMozdj2PLzNgeRoBN4YveAfR9wRWpsa9DlYcfoiatwtDv_9q4sqVK7pFR901Fh3E51bh655B7VU0j-I0YbwDWj0Wxz-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده نیروی قدس سپاه پاسداران: پیروزی نهایی از آن حزب‌الله است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/658505" target="_blank">📅 19:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658504">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8559da74.mp4?token=bgsVFLfC3soEyyWe8VdsvyDxtufrwDnyQhFZ-wpT4PZC0iJ2MEbGslMmBm-u6wXTX-8PVOt8bwCYIvTEL-j4UbVpcRcNyAnfG3FIAycnsq6nJiKLNd-j8VFxnk0UTXAYykGgwG-v8Ip7Wd_I8iUwcCC7z49TwpIfHKlzYUTgJCoKho1yxiqX65Oq-3YBkoeqA76-pbI2pcSDyBHIxMpRQUz6FqGY1EeZ6ayoR_3pPRx3JGGtRwLd3D68-RGvHb-NqJyYg4eJEp_d5UGVcx4F3EE26l-GwPCBZCJmCbwQJcptZHrFZFsSGrVKRXP0djc_i2YVCv8PftbITUJRPq8GGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8559da74.mp4?token=bgsVFLfC3soEyyWe8VdsvyDxtufrwDnyQhFZ-wpT4PZC0iJ2MEbGslMmBm-u6wXTX-8PVOt8bwCYIvTEL-j4UbVpcRcNyAnfG3FIAycnsq6nJiKLNd-j8VFxnk0UTXAYykGgwG-v8Ip7Wd_I8iUwcCC7z49TwpIfHKlzYUTgJCoKho1yxiqX65Oq-3YBkoeqA76-pbI2pcSDyBHIxMpRQUz6FqGY1EeZ6ayoR_3pPRx3JGGtRwLd3D68-RGvHb-NqJyYg4eJEp_d5UGVcx4F3EE26l-GwPCBZCJmCbwQJcptZHrFZFsSGrVKRXP0djc_i2YVCv8PftbITUJRPq8GGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملۀ هوایی شدید رژیم صهیونیستی به شهر النبطیه در جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/658504" target="_blank">📅 19:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658503">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fefa4eec1c.mp4?token=b4DCIXFwCgivN13PDDPobLTVGSUJLbRU-PGU2ImFGb1bH9XRna5fIojlEGS5jSAWnzswJClApRoBBRYV9B2Rf-jmi1jzY6QSUXvD-bytyxomBDlrFvJDcKIy07XM_4ERvAjxenRc5S4zbE3lMriNP9tckpzmF4TeZn7u37HCs-U3zyYO0adKpcc4TuTO-bsYGlkTmhx6UlVIUI7Q26dTGmfWL18aQVxhFl4BhNBn5ELIol2kwp8ltTChYmdGS5dcfTEUcmdO7OicXOngv5HxYiYod_HULfwXWuj8ujJTWZXVy0afW2cZwZ9cpufY3IL1R1Olf0xpRFP7EgAcbJ0-GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fefa4eec1c.mp4?token=b4DCIXFwCgivN13PDDPobLTVGSUJLbRU-PGU2ImFGb1bH9XRna5fIojlEGS5jSAWnzswJClApRoBBRYV9B2Rf-jmi1jzY6QSUXvD-bytyxomBDlrFvJDcKIy07XM_4ERvAjxenRc5S4zbE3lMriNP9tckpzmF4TeZn7u37HCs-U3zyYO0adKpcc4TuTO-bsYGlkTmhx6UlVIUI7Q26dTGmfWL18aQVxhFl4BhNBn5ELIol2kwp8ltTChYmdGS5dcfTEUcmdO7OicXOngv5HxYiYod_HULfwXWuj8ujJTWZXVy0afW2cZwZ9cpufY3IL1R1Olf0xpRFP7EgAcbJ0-GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سردار رادان به تهدیدهای ترامپ
🔹
رزمندگان بلدند زبان تهدید را چگونه پاسخ دهند، تا جایی که [دشمنان] مقابل ایران سر تعظیم خم کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/658503" target="_blank">📅 19:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658502">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
سخنگوی پنتاگون: پنتاگون یک مشکل مربوط به کیفیت هوا را شناسایی کرده است که اتخاذ اقدامات احتیاطی را ضروری کرده؛ این اقدامات تا زمانی ادامه خواهد داشت که اهمیت و ابعاد این موضوع را مشخص کنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/658502" target="_blank">📅 19:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658501">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
خروج قطار مسافربری تبریز ـ مشهد از ریل در میانه
🔹
قطار مسافربری تبریز ـ مشهد در محدوده ترکمنچای (اطراف جاده ورزقان) از ریل خارج شد.
🔹
در پی این حادثه، تیم‌های امدادی و عملیاتی هلال‌احمر میانه بلافاصله به محل اعزام شدند.
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/658501" target="_blank">📅 19:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658500">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/093d33fe81.mp4?token=JI8NteIh8o7w2FUjwtO72H2QiwnBWWRUdfcWtyLKfw6i3gf_fsIwrZX-Mvn9-j5C_zux0k8LWzfmmAEoCtzMxUQFmeiK87Q2cu-twDRTt22Bb9d6KW2nuEPeX-lylHj7t_Y98hK334HWTPer3Y5GUhsmFE_lA60W8CMQySegNXiVXF-PX2SEC_plETDElBHyATLJI8ZofRoFC_f577DgEEKcMfFrBbskTrQe74v8e_6L75WATx46mmimr-IO1hecegP_rPSIawG5rGA6pqQlhxizFfxGb1x41DwNjkBxaYPGcmDwo-hik1T1Z-o8fqcMRqRVJX5FWwsnxxH-IInMpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/093d33fe81.mp4?token=JI8NteIh8o7w2FUjwtO72H2QiwnBWWRUdfcWtyLKfw6i3gf_fsIwrZX-Mvn9-j5C_zux0k8LWzfmmAEoCtzMxUQFmeiK87Q2cu-twDRTt22Bb9d6KW2nuEPeX-lylHj7t_Y98hK334HWTPer3Y5GUhsmFE_lA60W8CMQySegNXiVXF-PX2SEC_plETDElBHyATLJI8ZofRoFC_f577DgEEKcMfFrBbskTrQe74v8e_6L75WATx46mmimr-IO1hecegP_rPSIawG5rGA6pqQlhxizFfxGb1x41DwNjkBxaYPGcmDwo-hik1T1Z-o8fqcMRqRVJX5FWwsnxxH-IInMpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای مرد آزاده راهت ادامه خواهد داشت و قاتلینت به سزای اعمالشان خواهند رسید...
#WillPayThePrice
‎
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/658500" target="_blank">📅 19:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aebd782004.mp4?token=js8T2aUQ7ihMx2sLJDyQ9vhrFpffUFDuNYs1wucBJVSsO7WggBSzZONSKdsxjMYgRo77Z7YkO20cdsJ0CDSM4MA4_5r_4xUPjzHfK4nGiqmv27cCzi-UzvBXaffUzhrFwU-ExAz697rMujnD98gx53O8FTW0BULxEU_z3qh0oFjcbYf9xuNvuT3TbrgoQ3-RSPT5T7fSzNJrwzRIoxymRVRGHqWjwLIj2W6piSSmNvoUDLxUvZij8BvyuZCNOIKJoX-olOmK5DpSFUWDJ1Oj-PwM1WjrEdLEH30Gfa_L6REe_NfhWYXE7hVKYjyD-IIj93sT6AMwQl0V122hye8ZSMAk-IeO7R-IcmDn59Pxo0Ez6PiBJ6OT9GsGrd_my4ck5Og-aL-fOKunmCbeq6ZPwoOd-1hyrkvF9_Fe2CBIrJ5iUGwuFCniuwfwm9XKLPIa-T3lA_6rMlOZLyT6jYP-jCF5hBiQKs6YEi7SOFjiC5gnU8DDFswa35WTcqe0XGltR3YI9eaBQa_bDimRzJOV12BOPI4ZBTG0OZI-aATDeHEMzALrYa38XJTH-ZtnbxZzDjTmImMtZFfzy9wqD-Xd482TDVWNFPgtnKp0taXwP6XiO1nWN6dMmRQJ-p60xVXJcebJh5Ax5i7CzLNJtzo7xyLPAAAu0SNjkGIdmjvIPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aebd782004.mp4?token=js8T2aUQ7ihMx2sLJDyQ9vhrFpffUFDuNYs1wucBJVSsO7WggBSzZONSKdsxjMYgRo77Z7YkO20cdsJ0CDSM4MA4_5r_4xUPjzHfK4nGiqmv27cCzi-UzvBXaffUzhrFwU-ExAz697rMujnD98gx53O8FTW0BULxEU_z3qh0oFjcbYf9xuNvuT3TbrgoQ3-RSPT5T7fSzNJrwzRIoxymRVRGHqWjwLIj2W6piSSmNvoUDLxUvZij8BvyuZCNOIKJoX-olOmK5DpSFUWDJ1Oj-PwM1WjrEdLEH30Gfa_L6REe_NfhWYXE7hVKYjyD-IIj93sT6AMwQl0V122hye8ZSMAk-IeO7R-IcmDn59Pxo0Ez6PiBJ6OT9GsGrd_my4ck5Og-aL-fOKunmCbeq6ZPwoOd-1hyrkvF9_Fe2CBIrJ5iUGwuFCniuwfwm9XKLPIa-T3lA_6rMlOZLyT6jYP-jCF5hBiQKs6YEi7SOFjiC5gnU8DDFswa35WTcqe0XGltR3YI9eaBQa_bDimRzJOV12BOPI4ZBTG0OZI-aATDeHEMzALrYa38XJTH-ZtnbxZzDjTmImMtZFfzy9wqD-Xd482TDVWNFPgtnKp0taXwP6XiO1nWN6dMmRQJ-p60xVXJcebJh5Ax5i7CzLNJtzo7xyLPAAAu0SNjkGIdmjvIPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده از خوشحالی یک الاغ پس از دیدن صاحبش بعد از مدت‌ها در لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/658499" target="_blank">📅 19:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
نبی: مشکل ویزای ملی پوشان حل شد
سرپرست تیم ملی:
🔹
احتمالا نیمی از ۱۵ نفری که ویزا نگرفته اند ویزای خود را دریافت می‌کنند.
🔹
در تلاش هستیم تیم ملی روز شنبه به آمریکا سفر کند اما به ما ابلاغ کرده‌اند که یک روز قبل از بازی حضور داشته باشید.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/658498" target="_blank">📅 19:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gewL4GgfGBbXbaW8UNUed7c-aKPGth0GWSC4XfUjWPIi6xpqIjr2xLELHcHI4qS0iKfZqUbKYcXHaJ2A0LrNPoaCLcaWtrcXSclkduOFsoUL1Vf87T6Xwdiv4oG7DBiBCmWrIbIAR6j6YGYe_f9TDerG17XNSMLq4LPeAnQlE3I7yc5ZLMWU45HdqfZA4gbF_0C80H_oxXZ2VALFFDxNDPokp4GKVVWVRzDXJRqIRMLcDS28yGH_w5mir9PGuMZZN4XqCo0-iOyQTbxzZBKf7k8C3tXLxHb_LZJv9x-sQ9fdWqPvbZUmyY96o05lVS_KrpSKSacfEAxjteVGxd_x8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس مجلس: ایرانی متفاوت خواهید دید!
قالیباف:
استراتژی‌های اشتباه و تصمیمات بدون فکر، صحنه بازی را به شکلی فاجعه‌بار به نقطه صفر برمی‌گرداند؛ زیرساخت‌های انرژی و بازارها را به انفجار می‌کشاند و مردابی بی‌پایان پدید می‌آورد که سال‌ها در آن گرفتار خواهید شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/658497" target="_blank">📅 19:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658496">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
♦️
وزیر علوم: مجازات قضایی و انتظامی برای کسانی که در دانشگاه پرچم مقدس ایران را آتش زدند
🔹
کسانی که پرچم منحوس پهلوی را در دانشگاه برافراشتند و پرچم مقدس جمهوری اسلامی ایران را آتش زدند، از لحاظ قضایی و انتظامی به پرونده‌شان رسیدگی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/658496" target="_blank">📅 19:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658495">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای الحدث: نشست قریب‌الوقوع کشورهای میانجی‌گر واشنگتن و تهران
الحدث:
🔹
پاکستان، قطر، عربستان سعودی، مصر و ترکیه برای ارزیابی تلاش‌های میانجی‌گری تشکیل جلسه می‌دهند.
🔹
نشست پنج‌جانبه به دنبال یافتن تضمین‌هایی برای اجرای توافق بین آمریکا و ایران است./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/658495" target="_blank">📅 18:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658494">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCU4GZVwe5GpvSqzXrbWW-jIDv_dU1HfkdDJBU-QMMPBzXOTbWxRkrF0dU0cddO_sjwSJYEUpPo1YsLokC5nZ7ut8ZtzZIsh4BdZ7OyuaTO_8KQPFpVuAhRH164H_Iliz2HEKa4_cTsgy8su6HYinoM9kt-438fHdtj8yyfTnNfH7BuhwDU6VH1g0grSSI4BjgqqgjWneoVxMLLlBjvNMeINygRlYtnF9GXUZl-WfgrpaKPgG3CjJWSqGrJ9EWwgw3x4fYvowwUZZ2K7_b4j-WLp2ukHOqFbZYePbhG_EKpsRHlIgVFhn1v3gRxjTiW6cDzipRWPPiLhoKczaXp7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/658494" target="_blank">📅 18:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658493">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تخلیه اضطراری طبقات مختلف پنتاگون در پی هشدار امنیتی  سی‌ان‌ان:
🔹
در ادامه حادثه امنیتی امروز در وزارت جنگ آمریکا، عملیات تخلیه پرسنل از چندین طبقه ساختمان پنتاگون آغاز شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/658493" target="_blank">📅 18:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658492">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
پنتاگون در پی یک حادثه امنیتی تعطیل شد
🔹
وزارت جنگ آمریکا، دقایقی پیش در پی بروز یک حادثه امنیتی، درب‌های اصلی ساختمان پنتاگون را بست.
🔹
گزارش‌های اولیه حاکی از آن است که این تعطیلی در پی شناسایی و احتمال وجود مواد خطرناک و مشکوک در محوطه ساختمان صورت گرفته…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/658492" target="_blank">📅 18:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658491">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
پنتاگون در پی یک حادثه امنیتی تعطیل شد
🔹
وزارت جنگ آمریکا، دقایقی پیش در پی بروز یک حادثه امنیتی، درب‌های اصلی ساختمان پنتاگون را بست.
🔹
گزارش‌های اولیه حاکی از آن است که این تعطیلی در پی شناسایی و احتمال وجود مواد خطرناک و مشکوک در محوطه ساختمان صورت گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/658491" target="_blank">📅 18:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658490">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b32e9f76.mp4?token=k5XmWOrIMhgEiYXQxuRygxiBCI6LElqg16sQnM_KEw146rKyOQG7igE8aTr28w3pmgIflVZlOArLW13tNgdg6FHsdUNITU4p6DsTw-JDSSpgNs-3vbSFFsCTn9aGx2tnSk5uDhQrJlIExrl-5rXv1kmZsxvzl_npAn3L0DYHdgaENNpi9NCnCoYmLD9mPhX5-pzqOa3k0_vN8q0VJjDjfifCQzxFuQes7ttaGWLDswQKvWFnevNts7gbAcaiDmihfsKWCUI3ooGAf2bYXmAtnjzauodlWerQDXMCwNmTZwtVuG9aEl6sH7xdrM0YR153Jy2xTv9auRP2WOanblUJpS8LhNyknv00PTFkXyQ_RpGNiDjvhbkCGTPTWmcdVRB-uNh3e74yYFWaLquOoHy4N6JNNJITNzwOZ0drCX8WVHTMR6uKiRjpx2PxTK0xfQS_6-I5oTDsKCaNmnnPIl8mEIaisuotqCNBbTMu5LE9mq8ypEkhHhKXwJX8-w3wmbEUGPRRcApxcKFEqPoWqdvVOgfnDf51tI1MZ3k-sv7A8SCcD10xCoVIw69ALvdxwDMbrR0Rd5YEr3_IXX1HWnzxlfvxlmKzaojtr-mcHT8nhmnUVBBS44HpFD5OrD6i6Gmd2x-HZCm70KWSyi7BygYXbw87o2G_Ewk31mWPUSL9wtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b32e9f76.mp4?token=k5XmWOrIMhgEiYXQxuRygxiBCI6LElqg16sQnM_KEw146rKyOQG7igE8aTr28w3pmgIflVZlOArLW13tNgdg6FHsdUNITU4p6DsTw-JDSSpgNs-3vbSFFsCTn9aGx2tnSk5uDhQrJlIExrl-5rXv1kmZsxvzl_npAn3L0DYHdgaENNpi9NCnCoYmLD9mPhX5-pzqOa3k0_vN8q0VJjDjfifCQzxFuQes7ttaGWLDswQKvWFnevNts7gbAcaiDmihfsKWCUI3ooGAf2bYXmAtnjzauodlWerQDXMCwNmTZwtVuG9aEl6sH7xdrM0YR153Jy2xTv9auRP2WOanblUJpS8LhNyknv00PTFkXyQ_RpGNiDjvhbkCGTPTWmcdVRB-uNh3e74yYFWaLquOoHy4N6JNNJITNzwOZ0drCX8WVHTMR6uKiRjpx2PxTK0xfQS_6-I5oTDsKCaNmnnPIl8mEIaisuotqCNBbTMu5LE9mq8ypEkhHhKXwJX8-w3wmbEUGPRRcApxcKFEqPoWqdvVOgfnDf51tI1MZ3k-sv7A8SCcD10xCoVIw69ALvdxwDMbrR0Rd5YEr3_IXX1HWnzxlfvxlmKzaojtr-mcHT8nhmnUVBBS44HpFD5OrD6i6Gmd2x-HZCm70KWSyi7BygYXbw87o2G_Ewk31mWPUSL9wtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حزب الله منتشر کرد
🔹
تصاویری از عملیات هدف قرار دادن سربازان ارتش تروریست اسرائیلی در شهر خیام، جنوب لبنان، با هلیکوپتر تهاجمی ابابیل توسط سربازان مقاومت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/658490" target="_blank">📅 18:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658489">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c91665100f.mp4?token=VI5A2I4zOHwmvjINVEydk3Yb953jm-PYpZn2PfFyTfr5pnTQHEl45tc_0hlUGK4zvFtdBguIG5mHXZoeK2xFF5jusGsJD1bW10ezvZf7FiYqfzH9vgFMyBt1rO1DJ0QlVNTwqsn6JvL-BEbm_QQES178gPJBu_smNk3eNnYwNdrHol4wAnzpyOY1QOdY8es6WL4QdF8PAv49AbOtSafJRy1LTP96r2Ke2GTU9-_FRWKQSGmMzy8lck8673WmEDfEB1Zom8qLhwbSQW5V9NqgYoSJnas-ljMD-MEM9xfDnuwG8oP34tfcwiEUdLl8IpCiBFhNiB6gQsX2_qG_o0vjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c91665100f.mp4?token=VI5A2I4zOHwmvjINVEydk3Yb953jm-PYpZn2PfFyTfr5pnTQHEl45tc_0hlUGK4zvFtdBguIG5mHXZoeK2xFF5jusGsJD1bW10ezvZf7FiYqfzH9vgFMyBt1rO1DJ0QlVNTwqsn6JvL-BEbm_QQES178gPJBu_smNk3eNnYwNdrHol4wAnzpyOY1QOdY8es6WL4QdF8PAv49AbOtSafJRy1LTP96r2Ke2GTU9-_FRWKQSGmMzy8lck8673WmEDfEB1Zom8qLhwbSQW5V9NqgYoSJnas-ljMD-MEM9xfDnuwG8oP34tfcwiEUdLl8IpCiBFhNiB6gQsX2_qG_o0vjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی ترامپ برای بار چندم به اعلام پیروزی ایران توسط رسانه‌های دنیا اعتراف می‌کند
ترامپ:
🔹
مشکل این است که این می‌تواند بزرگترین توافق تاریخ باشد. آنها می‌توانند پرچم سفید تسلیم را تکان دهند و بگویند «الحمدلله» و رسانه‌های جعلی بگویند «این یک پیروزی بزرگ برای ایران بود».
🔹
این دیوانه‌وارترین چیزی است که تا به حال دیده‌ام، ما داریم آنها را می‌کشیم. این ماییم که داریم آنها را می‌کشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/658489" target="_blank">📅 18:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658487">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
حنظله از نفوذ به ارتباطات مرتبط با مقامات موساد خبر داد
🔹
گروه هکری «حنظله»، امروز پنج‌شنبه اعلام کرد که موفق به دسترسی به اطلاعات و مکالمات مرتبط با شماری از مقامات پیشین و کنونی در دستگاه اطلاعاتی اسرائیل (موساد) شده است.
🔹
این گروه همچنین اشاره کرده که به داده‌هایی مربوط به فعالیت‌ها و عملیات‌های سایبری دست یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/658487" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658486">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA_kHn0ByvNP7agiLYEWQZa0O14c4UFwlyF2_57H_FB9rZFnZLT2tkMgphXXEHjf7lfOUivsnR6roiMEazxmmSVz4e1PqmODxGU90I_TwIIP5n_aeW6lWVfFg_5fXpoTRF0YgzCHgxjBbw4iyTS3JJI_HU33nmzAU2d5Hsc_xq2RJG89HAH9PnQzD-VtP4LMqpPZ2mV_qgHIVUISjvDpx-2fAzsD1CbinRnQtM_6J2zX5c7fFMkEKtGQCRXbRFhMoo4hhdCg_ijqAGUqcDM39tdsBDCRG9fL__74Q0ayJDkFbYzT40Ej14SoI0OBgQOaWm0pCGLw19fIp3YpQfrgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند؛ جایی که یک انتخاب می‌تواند سازمان را تغییر دهد.
در رویداد تخصصی «نقطه تصمیم» جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود در مواجهه با بحران‌ها، تصمیم‌های دشوار و فرصت‌های پنهان بازار سخن خواهند گفت.
اگر به دنبال شنیدن تجربه مدیرانی هستید که در خط مقدم تصمیم‌گیری قرار داشته‌اند، این رویداد را از دست ندهید.
یکشنبه ۲۴ خردادماه ۱۴۰۵- ساعت ۱۶ – مشهد، هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/658486" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658484">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cc32c8bb.mp4?token=BEmFxP_yhn1R-4d9JjSxMtUjD7dv4PN5e--QdSyvl1ffSu43SeCr65594I3ty4z-dlol5c6pfNcGON4FYJhl6lJNeZZhnB8Ry6aX5Kklet9UmLhXSybNAOZbLFB0LKCKUzvNvMcYsQKS0gfIK1drfdpkHXJCKkmik9CRHaI_VStTJkGJFK67jSAbYe2MoyIexLtN72BnHzijv4sWTXqTFLCAa1rlojx_q2TpxMMuX5N-vI4oszy_F0ZvmhdvWxpY709NRVkhJuAWQlfqk9XHVhzODMDrSH16Ghsfw0ul_oEVkVIJBvhpmu1MzlnnAui7mC0eIpM09dCF-d48rLX7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cc32c8bb.mp4?token=BEmFxP_yhn1R-4d9JjSxMtUjD7dv4PN5e--QdSyvl1ffSu43SeCr65594I3ty4z-dlol5c6pfNcGON4FYJhl6lJNeZZhnB8Ry6aX5Kklet9UmLhXSybNAOZbLFB0LKCKUzvNvMcYsQKS0gfIK1drfdpkHXJCKkmik9CRHaI_VStTJkGJFK67jSAbYe2MoyIexLtN72BnHzijv4sWTXqTFLCAa1rlojx_q2TpxMMuX5N-vI4oszy_F0ZvmhdvWxpY709NRVkhJuAWQlfqk9XHVhzODMDrSH16Ghsfw0ul_oEVkVIJBvhpmu1MzlnnAui7mC0eIpM09dCF-d48rLX7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همیشه دنبال تصرف خارک بوده‌ام
ترامپ:
🔹
ترجیح من همیشه تصرف جزیره خارک بوده است. راستش را بخواهید، نمی‌دانم آمریکا جراتش را داشته باشد یا نه. اگر این کار را بکنید، کلی پول درمی‌آورید.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/658484" target="_blank">📅 18:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658483">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bafc936097.mp4?token=gWPG-Ql__jVKGrtB5AlfSZ6Mkc9HZj7JEUMPfse5t60q7TLu5GCHRjU8bUlMqzVZnsgM2di_XotNQVdQHc-XlB26GmCO9dM-wFhrUePY7o5v-CZYHzWYp_HEX2YyLEmhYhmjmR6zhIbAZJorL0ebVP7KqFvHB71TRLMx87VUpmf9rOF9jMMENiCD0SShOZMJM_dKcLt8AFp5SP5p7hNhtTpEUtOXVhUF7iWEkDBx_VyfpaAS55ZI2457wZlKDCC-hRoOg0tBQEl0lAF0GkQFao_34-j8QhcaKpAi0SQ4bJ7Uf-kYmap3vyRinE_bKtdJRnn2kVhRDlNQKRUkvLtAaYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bafc936097.mp4?token=gWPG-Ql__jVKGrtB5AlfSZ6Mkc9HZj7JEUMPfse5t60q7TLu5GCHRjU8bUlMqzVZnsgM2di_XotNQVdQHc-XlB26GmCO9dM-wFhrUePY7o5v-CZYHzWYp_HEX2YyLEmhYhmjmR6zhIbAZJorL0ebVP7KqFvHB71TRLMx87VUpmf9rOF9jMMENiCD0SShOZMJM_dKcLt8AFp5SP5p7hNhtTpEUtOXVhUF7iWEkDBx_VyfpaAS55ZI2457wZlKDCC-hRoOg0tBQEl0lAF0GkQFao_34-j8QhcaKpAi0SQ4bJ7Uf-kYmap3vyRinE_bKtdJRnn2kVhRDlNQKRUkvLtAaYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهین بی شرمانه ترامپ نسبت به ملت شریف ایران؛ در حال متوقف کردن یک ملت بسیار شرور هستیم
ترامپ:
🔹
ما در حال متوقف کردن یک ملت بسیار شرور هستیم که هزاران نفر از مردم ما را کشته است. اکنون، ایران در موقعیت نهایی قرار دارد آنها چاره‌ای ندارند. تنها نکته منفی این است که همه در مورد آن اشتباه مینویسند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/658483" target="_blank">📅 18:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658482">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607e2db7d7.mp4?token=pSYt28EaADyiRg7AEn51mY8yceNgUkp22-H-zJF0oaH_huxb4MvvyxhmoqBym_FrIJA9a4im_KidDrWA6x1R57i0MBBfd8-LEyGhZvyqlIsux6mYRIGkfjTPj4asmamrQdJzrbAHnZ6A4s5oUWQ91R813-aAlbuz8_FmGC82Qynfb3YI6p6FO1kZESipssxHxpzQkeNktCYoddu_HhcqfPSqZw4Sc7Y23cVWLapHaaHOCstaFCCzjeFs-YzXhQgrq9gfy-fWO5HtwjWyivGo48DYeY0ib1Xvkz-L07ZLEM_hM3sjf2y4hJvxsmdCXvw8tF6mYrLaToNh8J0y5UQWOXO25m-k46iTgeWDJN26OBWKIGKSte4f1VLbhO3NRss2cdsMtY_uWyYlI-Z3MW8K3V01rnmSuemCg2WpznwKJgrhNNe9eiywOuJCOEH--CvZFa85VHl2Y7dccx1RBMJIRPJ0rrm0HENlclzdBiXH4n6Wnt4_jClfxdX2sGPn1_ZSvXgdeyrndnlyzY4cmdERtbKCWrQEdk9y78DsU8V1nU-t9D5fKO5P9yu2Pj4q6auCY0exzvZGiPQWSYzBkFaJVQ3gr3iE6C_9NXY8OK8NpgZUVSyws_tg5h_VS3MAX0TYBkkP_ewvg1PRLja5kLITeav4KfDC59CeVrxrsMDQIUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607e2db7d7.mp4?token=pSYt28EaADyiRg7AEn51mY8yceNgUkp22-H-zJF0oaH_huxb4MvvyxhmoqBym_FrIJA9a4im_KidDrWA6x1R57i0MBBfd8-LEyGhZvyqlIsux6mYRIGkfjTPj4asmamrQdJzrbAHnZ6A4s5oUWQ91R813-aAlbuz8_FmGC82Qynfb3YI6p6FO1kZESipssxHxpzQkeNktCYoddu_HhcqfPSqZw4Sc7Y23cVWLapHaaHOCstaFCCzjeFs-YzXhQgrq9gfy-fWO5HtwjWyivGo48DYeY0ib1Xvkz-L07ZLEM_hM3sjf2y4hJvxsmdCXvw8tF6mYrLaToNh8J0y5UQWOXO25m-k46iTgeWDJN26OBWKIGKSte4f1VLbhO3NRss2cdsMtY_uWyYlI-Z3MW8K3V01rnmSuemCg2WpznwKJgrhNNe9eiywOuJCOEH--CvZFa85VHl2Y7dccx1RBMJIRPJ0rrm0HENlclzdBiXH4n6Wnt4_jClfxdX2sGPn1_ZSvXgdeyrndnlyzY4cmdERtbKCWrQEdk9y78DsU8V1nU-t9D5fKO5P9yu2Pj4q6auCY0exzvZGiPQWSYzBkFaJVQ3gr3iE6C_9NXY8OK8NpgZUVSyws_tg5h_VS3MAX0TYBkkP_ewvg1PRLja5kLITeav4KfDC59CeVrxrsMDQIUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو را به هرکسی می‌پرستید هوای پیشکسوتان ایران را داشته باشید | همین حالا مجتبی محرمی نه درآمد دارد نه بیمه است
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/658482" target="_blank">📅 18:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658481">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af52ba85d3.mp4?token=Vc2rQgqI47gJfTO_x6GGMyAsoXCTWuHJD41Yd8alWpFQdquCNnFMGnzP_sNvPZXtAj7xsnAhAA3hxih-8vCGw_ryDx2KgV5Gh_uO-G3TXsUsrtt3FNSEd-JlaSCkcbAwiycuNjEwJBS-QFFUI-vgwZzz6Fpk4kAhcLE6d2LucK8misxUGr2CCD-0NLP5X7qIQoHWKQiKzM1loV2MDTyeo7ytkLVGwMWM7pKzmZLnGpVF2bxJdwRNKsdJiW4pWcm2ytsRKHqtVl27wyMvZJEHaH5w8hI0stol2iwYWKGrr3azv08ewGc7nzRwyYjKeR2Xccrf4SmemNQn4t7mCfWY_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af52ba85d3.mp4?token=Vc2rQgqI47gJfTO_x6GGMyAsoXCTWuHJD41Yd8alWpFQdquCNnFMGnzP_sNvPZXtAj7xsnAhAA3hxih-8vCGw_ryDx2KgV5Gh_uO-G3TXsUsrtt3FNSEd-JlaSCkcbAwiycuNjEwJBS-QFFUI-vgwZzz6Fpk4kAhcLE6d2LucK8misxUGr2CCD-0NLP5X7qIQoHWKQiKzM1loV2MDTyeo7ytkLVGwMWM7pKzmZLnGpVF2bxJdwRNKsdJiW4pWcm2ytsRKHqtVl27wyMvZJEHaH5w8hI0stol2iwYWKGrr3azv08ewGc7nzRwyYjKeR2Xccrf4SmemNQn4t7mCfWY_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت دو پهپاد انتحاری به مقر تروریست‌های تجزیه‌طلب در شمال عراق
🔹
منابع عراقی از اصابت دو پهپاد انتحاری شاهد ۱۳۶ به یک انبار تروریست‌های تجزیه‌طلب کُرد در منطقه «قوش تپه» واقع در شمال اربیل خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/658481" target="_blank">📅 18:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658480">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxne4YZ7yarV18v1hQRDF1149Z6vYChbrTBMRR4qQQsoFz47JvPm6_RTifDMrHAMci_sEIvPWWBspJ-7sOb2w-2xfQUr1j3zMpTWAMgc-YxS6NmltYmiUY4JK6BEp23YV99uPx37VO7W2YN9xj9kGf5FVmHtz9DXCbOVELp_4T5xfO2L5C044HrYRLXcSKiPsduV8xq-cACnP9-PjzGK15BMudCBfWN3UxJrGB19peGsr7QIkTEEv-psmkkrtAp_bMX9Ws2GJ194Wimwg5l8xpOfB_wjP_NTNE2z3MQ3SEW2XW0qOkAAnrtnDvzPJoQQhdXETewpSA-orF6Fb89KFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهستی گنجوی، بانوی شاعری که نمی‌شناختید
🔹
مهستی گنجوی تنها یک شاعر نبود؛ او بانویی دانشمند، موسیقی‌دان و چهره‌ای فرهنگی در عصر سلجوقیان بود که در روزگاری مردسالار، با استعداد و دانش خود به شهرتی کم‌نظیر رسید. آثار و آوازه او گواه حضور فعال زنان در شکوفایی…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/658480" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658479">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای بلومبرگ درباره دیدار امنیتی سطح‌ بالای ایران و امارات
بلومبرگ:
🔹
ایران و امارات نخستین دیدار امنیتی رو در رو در سطح بالا را از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران برگزار کرده‌اند؛ اقدامی که نشانه‌ای از تلاش برای کاهش تنش‌ها توصیف شده است؛ ابوظبی برای حفاظت از اقتصاد و سرمایه‌گذاری‌های خود به دنبال ثبات است و تهران نیز به بهبود روابط با یکی از شرکای مهم تجاری پیش از جنگ علاقه‌مند است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/658479" target="_blank">📅 18:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658478">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7accbfba0.mp4?token=EKIwJ5T11c3_XikeGTaVBZ8a4Gr8sDvzQUXcjs7_qcJKik9e1SIxnIlZ9rrqGSOsKPm8sIqLz79lJCrb5fT3H-Jm1Vpr3xRq-h3GCoBKyn93OFMNtfVewJACsGTEvn-kAlU2jE3k29ROAx2GOUBJGxVvsYRukqfQin-GFLLjSCOkXSbyYXFIIxVCQEFm82xpXu2crMdLFWPPVCm0Ni52ZSZrxiU0DVw-8vF9VJnhe79JDwz-xUOZcBS_PQztsivBZHR1zyP0-2nmzKOwUUn9yKzp39plGtOpU4TOmloct6YRAhi6nxCSRx9m0H0O0Zm6vi-hPfiyYgXfNrqjI1sgNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7accbfba0.mp4?token=EKIwJ5T11c3_XikeGTaVBZ8a4Gr8sDvzQUXcjs7_qcJKik9e1SIxnIlZ9rrqGSOsKPm8sIqLz79lJCrb5fT3H-Jm1Vpr3xRq-h3GCoBKyn93OFMNtfVewJACsGTEvn-kAlU2jE3k29ROAx2GOUBJGxVvsYRukqfQin-GFLLjSCOkXSbyYXFIIxVCQEFm82xpXu2crMdLFWPPVCm0Ni52ZSZrxiU0DVw-8vF9VJnhe79JDwz-xUOZcBS_PQztsivBZHR1zyP0-2nmzKOwUUn9yKzp39plGtOpU4TOmloct6YRAhi6nxCSRx9m0H0O0Zm6vi-hPfiyYgXfNrqjI1sgNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش ربات‌های نظافتچی هوش مصنوعی در چین
🔹
چین در خانه‌های پکن در حال آزمایش ربات‌های نظافتچی مجهز به هوش مصنوعی است؛ این ربات‌ها در کنار نیروهای خدماتی کار می‌کنند و هرچند بخشی از کار را سبک‌تر کرده‌اند، اما هنوز به کمک انسان نیاز دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/658478" target="_blank">📅 17:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658476">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gR6d-ZMLOI6G-hmj0yKa2V-NdiqS95i9wzBFrwbwxe9m1AFWIFYD58n358I5bq7hWyH-2tpWLZkTdHSOxi7ooxne8YfI9lnwLkorWek8a2GpgXzRRJUzAAUm8Ff_-HOODo7EP9WtM4au6adjfgLbaASwpGxvB09keqylT8G6RB1E1y76VhSiroy72G1qwy3F79Rg8BGuIF3DkJDtEsMoMVfqLWoRH68c7AQuwNmUChZ5ji-nNDKriySxvaWPHkCUKgxI1SJXGglYsHml_n-RE0pOHDeupJaoS2u7J9tcRfh25rSBIE7NpS7dN1Dbgcjpro0X7Y7DGpjWjkYDAUP3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBwpasxEyCblyhZ3hCiLwQZFeEDkHZ6kznHSXL1B6FWHa4qmtT9scjBSMZbDFrnLZGrt2vJuF4ZkR8ChB8Hw4h8AZU54rwV3kqBLa_hEIy_W8IAMPAMTwJyRK3VmDDiMuk2hsxtpvgmNEFhZYlBmaw8hOhj5o6zmu3F4TRuU8MLuo4duxE2GhnVi_PsZxTBajjdQMbQx0mzB9cmfg9_nn5S9zP3tLqlvEs37vNTJ-4JXl7boQJtRTcOIuoWR2kpQZUR0Qfzjs7PcbRc6ZrFGTfDiSRCkE7eAVn8qf7zitIjyFJ9_U7iED5KSuDQOyvybHcG_0XF4XudUDF3_ciS4TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از ورزشگاه آزتکا مکزیک پیش از شروع مراسم افتتاحیه مسابقات جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/658476" target="_blank">📅 17:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658475">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYrF0QXq7K4Y80k6cX8Vmvs_RQQBVYcvOPwhMw2qxHS8P_U2QRqSBgrQuzBH5hsWQdzwZPf9F-VyhlN4TYaK69qIJf_fMTY-j3puj_6XyrfjCJwJTuNBJicvhlN0EA7H6-Fv90Oxvt9OPyaIQw15mC2McSWvtWjhbra52xtaBG9ZGerz1y70SUPdiYBAkKA9t8h9sjUJR8kcoEqWvC8CKFdI7lF-jhX_9BsTTY3L3HJv7Wl9XGtb-hu4Kb5BFUiaouZVG0nYpcVCXqva9RNXck3cacASqohtfO-HO-8All1RrI_MUekOOTA0wZTak_VkRqPa0HG5CXJajWsTCZGgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: کارشناسان تأکید دارند که ایران با بمباران، تسلیم نمی‌شود
🔹
دونالد ترامپ حملات به ایران را از سر گرفته است، به این امید که تهران را تحت فشار قرار دهد تا توافقی متناسب با خواسته‌های واشنگتن را بپذیرد، اما کارشناسان هشدار می‌دهند که این اقدام تأثیر معکوس خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/658475" target="_blank">📅 17:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658474">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/041fe85849.mp4?token=Q0-K-t4oAs6FN-wXnOcLQksbgeS4VcF_QWMCmJQpwTMtw3rFsx38wMDdVMOMiuQCBpwPqqBtjrJu8iVPXqZCeSM4lNkiaQJXLxlUD0Aff1qRimN9044R3hQt5qceqNGPYbQKtQAL9ZjzD2DGV09RacflrHY5pku6f7odwbP-OpDvmixrpCOFQtOqA5S6RFk4gZWnBqUmNKcFDFjcKlWMMUcw4zA1WMsmSbjdPG8i3-Nh_u1DLYZeHexA-lv7t6-KLYv3F_6DhvT8rAHWeHrigdwvWx-JQno-vqy7BdXXAQmw8GSombxnzC5fW6CQvsUTGM8P4aUA6LLjUzaYPlIsfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/041fe85849.mp4?token=Q0-K-t4oAs6FN-wXnOcLQksbgeS4VcF_QWMCmJQpwTMtw3rFsx38wMDdVMOMiuQCBpwPqqBtjrJu8iVPXqZCeSM4lNkiaQJXLxlUD0Aff1qRimN9044R3hQt5qceqNGPYbQKtQAL9ZjzD2DGV09RacflrHY5pku6f7odwbP-OpDvmixrpCOFQtOqA5S6RFk4gZWnBqUmNKcFDFjcKlWMMUcw4zA1WMsmSbjdPG8i3-Nh_u1DLYZeHexA-lv7t6-KLYv3F_6DhvT8rAHWeHrigdwvWx-JQno-vqy7BdXXAQmw8GSombxnzC5fW6CQvsUTGM8P4aUA6LLjUzaYPlIsfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفری از این تیم ملی ایران، باید فوتبال را ببوسند و کنار بگذارند
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/658474" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658471">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8e764a90.mp4?token=DGC2zzFFUDanOawbMD1-H66CEpHRf3rOyjBxsHLLS1Cv7zba1Q7HjtiZeEUFdlbAVllDO8eepXdipv9-3URjwAgqZQOJY8sI_drPuZotqF9GltopCjTI2MKHilkHOFVPVDZWYmCXd-IPMq9tnn9Ko0kKFBsFbbWyk0Ws9yRtRuaCsrOg6o-7foOpzXQ8W5cz2rQg0pt-c829rqfGvnR2WmJaTvugs4TTKmvhM89vaQ1hh3mbmGzvhq8jgXAtjMmGVU7s_FfDgN0CY3M8U8TvLFr0EwayD4rgDuipUfZavFLmmw-ttCmPw5Qn65WW8j0syiY_hkA5kjluSrQKQwf8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8e764a90.mp4?token=DGC2zzFFUDanOawbMD1-H66CEpHRf3rOyjBxsHLLS1Cv7zba1Q7HjtiZeEUFdlbAVllDO8eepXdipv9-3URjwAgqZQOJY8sI_drPuZotqF9GltopCjTI2MKHilkHOFVPVDZWYmCXd-IPMq9tnn9Ko0kKFBsFbbWyk0Ws9yRtRuaCsrOg6o-7foOpzXQ8W5cz2rQg0pt-c829rqfGvnR2WmJaTvugs4TTKmvhM89vaQ1hh3mbmGzvhq8jgXAtjMmGVU7s_FfDgN0CY3M8U8TvLFr0EwayD4rgDuipUfZavFLmmw-ttCmPw5Qn65WW8j0syiY_hkA5kjluSrQKQwf8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا مکزیک است؛ چند ساعت مانده به افتتاحیه رسمی جام جهانی
🔹
با حضور صدها پلیس و نیروی امنیتی جو امنیتی شدیدی در مسیرهای منتهی به ورزشگاه آزتک، میزبان بازی افتتاحیه، برقرار شده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/658471" target="_blank">📅 17:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658470">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAvBE2-T7GRqb4RWsewXxT0hnpIzJU13XEozHwAl_q3KGUdYJQtN6mJb2RqUSaAxIvRggW1SeoI3miqHxKMSzQVuG-6gSrF5yRGlIsWmrn0zoB4iAM4R8HB7d1_FNxFAbsspQ2lCSAp944ngEQLcmlcZrC4lRmgDGQyGHn6cCElRoa3kP9AcrBalTfxyEMXmgRnulE_EOQZZff_YxFrUgJiemKsAkdjbYcPFLN1rJLuNnAh4WFBeEqN5m-QnFznu-2gzRcASBCgHsb4A72mE6G6Q1L0MgLN16ps_uI1T31snJun0AP3mqJoctPDzslr67kRLKyK_JzZzd8cxA7Zl8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریچارد مدهرست، روزنامه‌نگار انگلیسی: یک چیز هست که ترامپ هیچ‌وقت در موردش دروغ نمی‌گوید: دزدیدن نفت. دولت دزدان دریایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658470" target="_blank">📅 17:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658469">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای
وال استریت ژورنال: آمریکا امشب به ایران حمله خواهد کرد تا ایران توافق را امضاء کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/658469" target="_blank">📅 17:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658468">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4616e0d1.mp4?token=sVoUC9yn8gDpA6_47-kXKySKmhecPmrEJIIpx4klG3ooUXlTeuvrktOP6fQdijnXD-VMrpxfPdpfZIVdect_Zgd7ubgRqn0ap0QJiULIW1Fte11I31C3lpE1D2YTXTxOezQQ85WYXSN89k88VehA3OuWbSVBUmJLOHyQ6_YDmXqln_h0sJTnUcQUY35hQsnWrnfE8cpCIJvcrnrQJKry-A94rIYnGECdjOUAqy-6ENMjhmuxLlinqjtwbGH8cs1McOunEyHubMeYl5HUgQy1LXpAIqgXDjomZzSc2Rqa-h6Jl2laLI2dp5WYcopMBLz2ShdrDm7ugM2OM8qSwkxj6yqsW9ZCGgeiAhftoCLs7hRZ4SM38U6Wa3CAKxHmhOZ_0hfELISoRxirQBfMKuOxf_h1VT3kb1kuVmVGbejNRE9IB3nDhj7ii6amvDZ88ScXZ8pwxzhnf1iSM4g_9ljYHJb5huE_4AK4HX1vxFmfsY_WU7-YfOFoeZ9ZXa7-ddIuU7SBLvNmGRD-_1tS_gDZa0DQhkLzBggQykkmyftDWSz-OQQrC8jGcWykRKW6mAksNjGtHQ_R3BsigUOhnM495lsha_OUD7qVBKEXIp1ys6xu1JS_4-oJTaOluzCDZKwnqlILJsrOM6kQyHH1elhHDCYhpUmL9QVBph4dZiLihCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4616e0d1.mp4?token=sVoUC9yn8gDpA6_47-kXKySKmhecPmrEJIIpx4klG3ooUXlTeuvrktOP6fQdijnXD-VMrpxfPdpfZIVdect_Zgd7ubgRqn0ap0QJiULIW1Fte11I31C3lpE1D2YTXTxOezQQ85WYXSN89k88VehA3OuWbSVBUmJLOHyQ6_YDmXqln_h0sJTnUcQUY35hQsnWrnfE8cpCIJvcrnrQJKry-A94rIYnGECdjOUAqy-6ENMjhmuxLlinqjtwbGH8cs1McOunEyHubMeYl5HUgQy1LXpAIqgXDjomZzSc2Rqa-h6Jl2laLI2dp5WYcopMBLz2ShdrDm7ugM2OM8qSwkxj6yqsW9ZCGgeiAhftoCLs7hRZ4SM38U6Wa3CAKxHmhOZ_0hfELISoRxirQBfMKuOxf_h1VT3kb1kuVmVGbejNRE9IB3nDhj7ii6amvDZ88ScXZ8pwxzhnf1iSM4g_9ljYHJb5huE_4AK4HX1vxFmfsY_WU7-YfOFoeZ9ZXa7-ddIuU7SBLvNmGRD-_1tS_gDZa0DQhkLzBggQykkmyftDWSz-OQQrC8jGcWykRKW6mAksNjGtHQ_R3BsigUOhnM495lsha_OUD7qVBKEXIp1ys6xu1JS_4-oJTaOluzCDZKwnqlILJsrOM6kQyHH1elhHDCYhpUmL9QVBph4dZiLihCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از آغاز تا پایان ماجرای حملات بامداد
🔹
جزئیات ضربات نیروهای مسلح به پایگاه های آمریکایی در منطقه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/658468" target="_blank">📅 17:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658467">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4uQgmRA4BGz0lYeWblCpnKBd3IkTWHupWLODH2FNgQ2yFicq_BZiRx012UJDSc0fOORzr9tPM5WDaIGPTbk-hOyI0E5LMVSH6piRyKQCPFGHSrw1zrCSMwGZU1pP_EeR0BWP9bVTWr6j-sPsMSQcHFkElAJUBLlOoUrqjUO-nob9EfS-NybePsM3MwL-jJSUzzkCQSlk_BeO7R55ki8GZ9VWbNBFeCRlpDuQn8rutsg7-eAI-1-JYhzA-MbmZCMtKloWYSvBiytfqKYydUkd6I6I3PRxBNK-e7BQL2d7Psk41bLvcl1Nxzge_NL4LwH9jafFiOwPcRHUYlJ-xnMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: دریافت‌کننده جایزه صلح فیفا یک روز قبل از شروع جام جهانی فوتبال، ایران را بمباران کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/658467" target="_blank">📅 17:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658466">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJOs3cf_7O56oRZTSeLzmjhOcB92wRO3mLiBklduF-HQfE8zttmWNWpbY6f5EvatbPqO1iWdzkMrItFArIzh2XHkgxy_l6_zTvdqZh2otqb3p8UaP4gQldpt1sbKXowX3kzi5AMiIVxsuHW3VTimn2Dfw_HrPok1rYhB6y5d2G9jl0d9YJil52iCY_WtrblwqSFt8R0avm6VoCoW6DMbejRxfsv94xZy61HBpfGqQbOxh8ntjdudq78VJl0Ly-vj-j3BkDk9i4UMb9zgGceASwVpAST3OISNxZKu0wEeHyR8xvoCADvjlVVOGCASwpWVyYtJMM4KdwLmt6TSnI2aPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لوگوهای جام جهانی از سال ۱۹۳۰ تا ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/658466" target="_blank">📅 16:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658465">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d414eaa82a.mp4?token=OsMKRxrc-Ne7gkkQ0BXsK8wd6lj02G-PFiSqCt8JeI2DfCyWdeskaa69BJBpt1DdAlQugd6sfh4kEhTrvDmPR4hGaF-vbZn5nQ3QBmRLuH9VDbOp8wZQz-epau0tfrorermM3bqlnDgJ3_fxE--1tHQpzZdGmnMoOhAQNseL5AVZxRydxFU_RpOSPRyaQP_7qEY6WMnlE5AqQHCe8C1nbBl8k3XAjKucQFtYE4mz5XbrXGqtZO2LMHI3az5tKLAoulSw64r4odRhpNd2U4pTvVYamnid8yMuYWw-qhuXWSYdpI6P9LKlqBYlkJs0OCHS9UNQzzGB8W8FOS0sd_LlAGKLyAgxwaDwk9kxMjna9egukgh4wDEdm7BkNCh2DiSjkxfNXTGYjONhSVOrVDzr5b2jhE52rz21de5NdimHVVeGcaMHGLAfrp2inHj3sf80lctWBaKnzlyppYcPx0SJ1H2G0KUgNC4Ha1VJ4pO0Z_u5JIAsYQHBp-0-JM-nR-IVT9YBRfdauq8RTQBw9dMZi7LdDKTsSm7lNLj_yxolvbBHZjsjSf_a7mDZoT12HpNFXxIp7gxsdRjpgurbdZiyXwi9_Ic5PXGqp-mkSaNZXcGcwuSvO6M33ecbKm6MK9tHvnnJCPrvMAnbf5hNRnGnPhnV2xZOVKZEiDDm0pg81mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d414eaa82a.mp4?token=OsMKRxrc-Ne7gkkQ0BXsK8wd6lj02G-PFiSqCt8JeI2DfCyWdeskaa69BJBpt1DdAlQugd6sfh4kEhTrvDmPR4hGaF-vbZn5nQ3QBmRLuH9VDbOp8wZQz-epau0tfrorermM3bqlnDgJ3_fxE--1tHQpzZdGmnMoOhAQNseL5AVZxRydxFU_RpOSPRyaQP_7qEY6WMnlE5AqQHCe8C1nbBl8k3XAjKucQFtYE4mz5XbrXGqtZO2LMHI3az5tKLAoulSw64r4odRhpNd2U4pTvVYamnid8yMuYWw-qhuXWSYdpI6P9LKlqBYlkJs0OCHS9UNQzzGB8W8FOS0sd_LlAGKLyAgxwaDwk9kxMjna9egukgh4wDEdm7BkNCh2DiSjkxfNXTGYjONhSVOrVDzr5b2jhE52rz21de5NdimHVVeGcaMHGLAfrp2inHj3sf80lctWBaKnzlyppYcPx0SJ1H2G0KUgNC4Ha1VJ4pO0Z_u5JIAsYQHBp-0-JM-nR-IVT9YBRfdauq8RTQBw9dMZi7LdDKTsSm7lNLj_yxolvbBHZjsjSf_a7mDZoT12HpNFXxIp7gxsdRjpgurbdZiyXwi9_Ic5PXGqp-mkSaNZXcGcwuSvO6M33ecbKm6MK9tHvnnJCPrvMAnbf5hNRnGnPhnV2xZOVKZEiDDm0pg81mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره ناب مرتضی فنونی زاده از علی پروین با تقلید صدای سلطان!
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/658465" target="_blank">📅 16:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658463">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ترامپ در مصاحبه با فاکس نیوز: امشب بمباران بیشتری علیه ایران انجام خواهد شد، و این بمباران بزرگتر و قوی‌تر خواهد بود!
🔹
ترامپ: اگر ایرانی ها توافق را امضا نکنند، بشدت بمباران خواهند شد؛ عجله کنید، هنوز می‌توانیم به بزرگترین توافق تاریخ برسیم! #Devil
🇮🇷
…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/658463" target="_blank">📅 16:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658462">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUCYCeH2H1iozaQPhbWr3D4_ZEgnYzn4lEWD1jajULVEB9K9qa9kmiwaP3fxLu508mMNyAyvssBmr3daCHyGWJ32O7b3pm-_21y00fO8CCmm9252zQ7XkmZ9F_N7mp6DJPo-RWwE3dwRP1mHZ1oaVst62zm8gbj8bLsb5iH1CEZfSKmNiHPZrZ-EwL25vsRE1G_uYj_A6wLrIU9vl35sSHHIWK7lNOahXkwd0AHmMbYpAOpq2U9BlXTI5HvUnLDay6DvwRmCaNYlh24m3wXEQKohRyDSOxsBvXxd2EG_hyOAiajP1vMpMjU7UmAENEtYf0e_raFiWArKltU2XVraiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: ترامپ راهی جز تسلیم در برابر ایران ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/658462" target="_blank">📅 16:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658461">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ترامپ: ما با جنگنده و هواپیما‌های خود بر فراز تهران پرواز میکنیم و ایرانی ها از آن خبر ندارند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/658461" target="_blank">📅 16:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658460">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ترامپ متوهم: مردم در ایران نمی‌توانند آب بنوشند و من نمی‌خواهم این اتفاق بیفتد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/658460" target="_blank">📅 16:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658459">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
اراجیف ترامپ: پل‌ها هدف بعدی حملات ما هستند! اما من نمی‌خواهم این کار را انجام دهم زیرا وقتی این کار را می‌کنم، مردم رنج می‌برند  ترامپ:
🔹
ما برای معترضان ایرانی سلاح فرستادیم، اما از کردها بسیار ناامید شدیم زیرا آنها سلاح ها را به معترضان تحویل ندادند.…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/658459" target="_blank">📅 16:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658458">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
یاوه‌گویی وزیر خزانه‌داری آمریکا درباره پولهای بلوکه‌ شده ایران
اسکات بسنت در شبکه اجتماعی ایکس:
🔹
هر خسارتی که ایران به متحدان ما در خلیج فارس وارد کند، از محل وجوهی که از حساب‌های ایران برداشت می‌شود، جبران خواهد شد.
🔹
هر عوارضی که به نهاد مدیریت آبراه خلیج فارس پرداخت شود، با برداشت وجوه از حساب‌های آنها خنثی می‌گردد. هر حمله‌ای که ایران انجام دهد، تنها پیامدهای اقتصادی و مالی متوجه آن را عمیق‌تر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/658458" target="_blank">📅 16:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658457">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ترامپ در مصاحبه با فاکس نیوز: ما با ایران در حال مذاکره هستیم!  ترامپ:
🔹
اگر ایران توافق را امضا نکند، آن را به شدت بمباران خواهم کرد
🔹
ترجیح می‌دهم جزیره خارک را در اختیار داشته باشم. ما هنوز به اندازه کافی به ایران ضربه نزده‌ایم!
🔹
ایرانی‌ها بسیار مغرور…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/658457" target="_blank">📅 16:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658456">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ترامپ در مصاحبه با فاکس نیوز: ما با ایران در حال مذاکره هستیم!
ترامپ:
🔹
اگر ایران توافق را امضا نکند، آن را به شدت بمباران خواهم کرد
🔹
ترجیح می‌دهم جزیره خارک را در اختیار داشته باشم. ما هنوز به اندازه کافی به ایران ضربه نزده‌ایم!
🔹
ایرانی‌ها بسیار مغرور هستند و ۴۷ سال است که در خاورمیانه قلدری می‌کنند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/658456" target="_blank">📅 16:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658454">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be5416d91.mp4?token=ZxebxnXM0ioXFS3rikvSbXo_QHjkEWoMP4ftTtHbWlAPDr0Z5PTOqaeovHeEdK1A_kUfUrpKH99vuPrt_TnVnYPIvpDZXwRx4DgaanOa2azMqsgCn7y_BVpNjpSvM_0fKGNFI884h_dZE1cdpetEOV7JQT45TpNha0zwCoG8n9k6YUHJK3zALBVWu0NfX7iNuzOS5hNRazq7CbnqbKdNFTwoJpqQUqhgAwYX2f-uGB4GcqRtTGzxSjYi8LkLExuijSeMr63d42IPTrvPA_EajNLdhI694a2SFDC9s3jEYS2Wh9pJ8mfaEUSasOeuvJf7sTABjN9TdmPYLCQdU_X-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be5416d91.mp4?token=ZxebxnXM0ioXFS3rikvSbXo_QHjkEWoMP4ftTtHbWlAPDr0Z5PTOqaeovHeEdK1A_kUfUrpKH99vuPrt_TnVnYPIvpDZXwRx4DgaanOa2azMqsgCn7y_BVpNjpSvM_0fKGNFI884h_dZE1cdpetEOV7JQT45TpNha0zwCoG8n9k6YUHJK3zALBVWu0NfX7iNuzOS5hNRazq7CbnqbKdNFTwoJpqQUqhgAwYX2f-uGB4GcqRtTGzxSjYi8LkLExuijSeMr63d42IPTrvPA_EajNLdhI694a2SFDC9s3jEYS2Wh9pJ8mfaEUSasOeuvJf7sTABjN9TdmPYLCQdU_X-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزدک میرزایی کارشناس شبکه اسرائیلی اینترنشنال: حالا اگه تیم ایران بازی اولش رو بُرد و صعود کرد چی بگیم!؟ اگر بازی اولو ببرن نمیشه دیگه جمعشون کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/658454" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658453">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3be75479.mp4?token=OAwNPmhzypLP9kmU1-WBhDGPSG81Mo6HzH3Ji2AGoQWaL38QqWk6SIYQXuzYK2RBrviyLuq493OP25OlRLOQ62_15ZENRYykISLhMprAntJiimctnf5u2NqBS0lCU4z1zKAsfhov5--n0dsgaDd8VGgf6e7ym6lSuvZIhJrz8dUQFt2e2xQKqYSCP9gerc2TFxLmOlsXkLz5I6TQT-mhBVPe__FpyKQRPTs6CZdQxEuJwl-EjvCDKzL8nyfTKJECT2NvUmlaq7gQGvILVguqGd4dTXAASEaUnnHUrOXEjXB7cgYVy8jsVa7vSnUBxaP6k1JK541HNBaCOzZ91LBC2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3be75479.mp4?token=OAwNPmhzypLP9kmU1-WBhDGPSG81Mo6HzH3Ji2AGoQWaL38QqWk6SIYQXuzYK2RBrviyLuq493OP25OlRLOQ62_15ZENRYykISLhMprAntJiimctnf5u2NqBS0lCU4z1zKAsfhov5--n0dsgaDd8VGgf6e7ym6lSuvZIhJrz8dUQFt2e2xQKqYSCP9gerc2TFxLmOlsXkLz5I6TQT-mhBVPe__FpyKQRPTs6CZdQxEuJwl-EjvCDKzL8nyfTKJECT2NvUmlaq7gQGvILVguqGd4dTXAASEaUnnHUrOXEjXB7cgYVy8jsVa7vSnUBxaP6k1JK541HNBaCOzZ91LBC2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوان‌گرایی در تیم ملی شوخی است | حاج صفی دیگر باید برود تیم پیشکسوتان بازی کند
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/658453" target="_blank">📅 16:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658452">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nci8gLdtBKtWUEYaHjciAZMmBMQyxL8cWRo42bPvWbiEKpZbPV_iQnotVeZA4FArrzIIPrOLbH-fisneo4ON38L_V9Tl5XGfGL6Hmw-lCGtp3ibE_-3fXXRE5mtnP5PsujgMW-axNMR87w0r6yO1dBbJztIXVgHNl_IP6CjckwLoic7Zm7jOMzs__EJaDeUMUq4PEUGraw3GIiihONloRXoMKeRKvq6dGPmdiwAi2FoH-sSB6NranTbW9efyW6Cvj8gYIWniW1q7MGl06MYWBtMh3QHDIFuf7kugYbAMqIzpSbq8GQrZKAYeIuzIE2qAXkk9RMLPsn0eRnhFb8kcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف سواد مالی، تربیت بچه‌ایه که پول براش ابزارِ ساختن زندگیه، نه دغدغه یا دردسر #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/658452" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f645fb06f.mp4?token=PClSfQhjmI2jGf0oACqnXOQEWKeYPokxl6FOh3MgSaabkOg4aFVS-pKI3qb2U7Qc_bbf9qQ2mIgPKSEbHnrEsg_SCl7uuglW0-J0DSziNt26cIr_rN1VjLAWO9oF8t4gSlldJzAjvS96J-c1H3H4gqNpvRc_TjqbpwI2SLyDjhWzVpYQ2bF4atm6Nw2PDZ0O8bQ8Nvz2DltwBNRF_fijGBVxyfAYMyLAXM53BGh7Vd7i89K8VmPh6a3dOLGy50Rng4QF-2fpmZ7D3hDbdrLYglBXz9r593SUbvuJCNwVt8O8YXjmV7kpJEzUwjcl1oM-2Bie5iDF8W_cjQ08yxxsPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f645fb06f.mp4?token=PClSfQhjmI2jGf0oACqnXOQEWKeYPokxl6FOh3MgSaabkOg4aFVS-pKI3qb2U7Qc_bbf9qQ2mIgPKSEbHnrEsg_SCl7uuglW0-J0DSziNt26cIr_rN1VjLAWO9oF8t4gSlldJzAjvS96J-c1H3H4gqNpvRc_TjqbpwI2SLyDjhWzVpYQ2bF4atm6Nw2PDZ0O8bQ8Nvz2DltwBNRF_fijGBVxyfAYMyLAXM53BGh7Vd7i89K8VmPh6a3dOLGy50Rng4QF-2fpmZ7D3hDbdrLYglBXz9r593SUbvuJCNwVt8O8YXjmV7kpJEzUwjcl1oM-2Bie5iDF8W_cjQ08yxxsPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش متجاوز صهیونیستی در خاک سوریه ایست و بازرسی ایجاد کرد
🔹
نظامیان رژیم صهیونیستی در ادامه تجاوزات خود به خاک سوریه، یک ایست بازرسی در جاده «معریه - عابدین» در حومه غربی درعا ایجاد کردند.
🔹
این گشت نظامی با استقرار در این محور، اتوبوس‌های حامل دانش‌آموزان مقطع آموزش پایه و نیز خودروهای غیرنظامیان را متوقف و بازرسی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658451" target="_blank">📅 16:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyFEXnlPyyOKISbXdoEyitVtY3EgSDL-dPUbUVfLIfe_-l_fghz-boZF84A1V-XMaOkggBa7HShvaNU4xaTdeJzUsUKiekDQqAFlN7trAeHLnCoPjRnpe30_xfyZamHVO2MTxiKiDpETtv7tuFrzrIdKPgjIay5-WyOUneJGKLbjnBS0nYWT37onCnxBVHfIQCJqqmFtpl3egJCjoxHMi98GEW16yqK5kpMNVgPoS1hpwAb_AtOLjYPq_DsmyMWLjfAOFgXRAzXAW1p6X_aXCyLZLrBrLehT0DFx6rbA0xqGA9XUk7h5_Ge2FZ9t1TQIItWmW7KvTKZnCYU0yIo0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گنده‌گویی جدید ترامپ: آمریکا امشب هم به ایران حمله خواهد کرد
ترامپ:
🔹
ایالات متحده امشب به ایران ضربه‌ای بسیار سخت خواهد زد (ناوگان دریایی، نیروی هوایی، رادار، ضد هوایی و تمام اشکال دیگر دفاعی آن، همراه با بیشتر توان تهاجمی‌اش، از بین رفته‌اند!)
🔹
در آینده‌ای نه چندان دور، ما جزیره خارک و دیگر نقاط زیرساخت نفتی را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم گرفت، درست مانند کاری که با ونزوئلا انجام داده‌ایم، که برای هر دو کشور ونزوئلا و ایالات متحده آمریکا بسیار موفقیت‌آمیز بوده است. از توجه شما به این موضوع سپاسگزاریم!
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/658450" target="_blank">📅 16:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658447">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1663ac3f.mp4?token=uyJNtrpKwYcTc2qinWuhe6mDLRDBSFOEWDgWfZKaNiXiZ98RCCg3V5FMHpKsRqxLx75pfq79Y5Iftet8vld1S7zcjyO8RIX0mjrziWbdCgzE7KFx1UE8-NOdd1K-Zejjbl4VJC1eI6WwsUgLT0cdY81PhbblWopvZQbdckooY78Z-glmKjoxMO1FWV7qnuxjFNMZf5U8VIOOitxryIfeEpzvTABn3yP2KKm1HeQhOuE3lGe8GkIfGdcVW5VHZf8vVAHISsOm44hi_tCVIU6tuJ3iKPChkWs6_hnfy4q7wDcjxyo7qd-K3aorZq9YsrO2khR1EUZ8UAxpP2NfUjkAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1663ac3f.mp4?token=uyJNtrpKwYcTc2qinWuhe6mDLRDBSFOEWDgWfZKaNiXiZ98RCCg3V5FMHpKsRqxLx75pfq79Y5Iftet8vld1S7zcjyO8RIX0mjrziWbdCgzE7KFx1UE8-NOdd1K-Zejjbl4VJC1eI6WwsUgLT0cdY81PhbblWopvZQbdckooY78Z-glmKjoxMO1FWV7qnuxjFNMZf5U8VIOOitxryIfeEpzvTABn3yP2KKm1HeQhOuE3lGe8GkIfGdcVW5VHZf8vVAHISsOm44hi_tCVIU6tuJ3iKPChkWs6_hnfy4q7wDcjxyo7qd-K3aorZq9YsrO2khR1EUZ8UAxpP2NfUjkAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری ترسناک از لحظه بمباران یک نمایندگی خودرو در نارمک تهران| ۱۸ اسفند ۱۴۰۴
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/658447" target="_blank">📅 15:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658446">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
آمریکا ورود هواداران تیم ملی فوتبال ساحل‌عاج به خاک این کشور را ممنوع کرد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/658446" target="_blank">📅 15:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658444">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkS8FJJca-BEDzO6hdjfMzheYlXWhuwCXGuKfK0--NBssMc1X8U0_FZsTbL4laJGtUtUXBeAKSnEQzbm_rUnpti6krbqXv4IrnJdY44E8Ce9K34-PtDp717ifiu2wnhE54NamXwM41_Agk73pqCTpPO8--JgzEXD24ncTB60VyAejeNp9-oGKlwZ1AY3U4iJCEVHgvFJIyicLx72Ub1NwxQO1ZujCKCgzmaZjVo3bHN2fW5GeR5UUkIbuLkWkBZ7cPgunSd7AjSlVMXD8-e-unFRcW4vM4Qciha_pysvop2PEzVenopWLmBH4oTF9jeUwUYEbGHiNLm5JMZ6dx_YCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلندترین و کهن‌ترین درختان ایران
🔹
عکس راست: بلندترین درختِ ایران. «بلوط بُلَندْمازو» با ارتفاع بیش‌ از ۶۰ متر
🔹
عکس چپ: کُهن‌ترین درختِ ایران. «سرو ابرکوه» با سن حدودا ۴۰۰۰سال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/658444" target="_blank">📅 15:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658443">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIBBenBv7PK-5_zczvc_P9oTGeOSpf6MTnMq9eGp6ZtNzRfr_Y4eb2mktCY7OQqTw9rResCv08jOKFmlLqe-g2Ic2m6YeVVbUjXFthHackWvdRHM3M3mTvkObj5Bq4FIXgalmJEnEt7nNZ1tjMYXCiGsIaXO9wbigZvkaQ5hLdNf9YuPM7Zc5Pnl9pMIgZDRCFRsqT6jol59Y6P6XkpIUz4HdDtSEG4QBsiRPEy8IfYOgmBnK6DNI5TQ-30sSPXIWWAg6XkAbn8OOYrp-oBnDF7J5tthuFYdl5MhSweMGPKdEAxx18w_3tDaksIxnFvZt4Tzy68F54B1SWeixqCXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایشگاه فرهنگی مذهبی عطر سیب
ویژه عرضه محصولات فرهنگی مذهبی و ملزومات ایام محرم
🔹
میدان آئینی امام حسین (ع)
▪️
از تاریخ ۲۱ خرداد تا ۲۸ خرداد از ساعت ۱۶
🔹
افتتاحیه امروز ساعت
۱۷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/658443" target="_blank">📅 15:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658440">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeCJHzAElF_DRZcG9UVi0_k3NOnu17LVr-ttVPLUMweaqxRJE2fzucAdlIY6lGBQn8Gm9bXoHjG4C8wjTD_JyVvTeTyO0_iSTZYwHUdBuAZhUmmouara70Og6d4CiQ5heu0jkOIafEMrRKAvfDoHqWdt3UN9DiYKyzMxgROtiAo0duF9h0CwM0godj4apT9Z8IB3DXj_drR7KClWz2DyJCyYcxjjC9NkOSeZl9jXv1qdA0UqbakhC5DMBDAbifeEN6GYfwm76mGl5WBLEHFamknYhBQ7QTIUQLBslhizUuZE8ltU7_3rSXtf_O474arGS207L7NfqC1SNV_s4zKY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دکتر علی احسانیان، در ایام جنگ رمضان در شهر نیس فرانسه به طرز مشکوکی به قتل رسیده بود، پیکر مطهرشان برای تدفین امروز به کشور برگشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658440" target="_blank">📅 15:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658437">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
یک منبع نزدیک به تیم مذاکره‌کننده، ادعای سی‌ان‌ان درباره مذاکرات جدید ایران و آمریکا را تکذیب کرد
🔹
این منبع آگاه تأکید کرد که جمهوری اسلامی ایران در روند مذاکرات بر مواضع و خطوط قرمز اعلام‌ شده خود ایستادگی کرده و از مطالبات اصلی خود عقب‌نشینی نکرده است.
🔹
متنی که پیش‌تر از سوی طرف ایرانی مورد تأکید قرار گرفته، همچنان مبنای مواضع تهران است و پیش‌بینی تیم مذاکره‌کننده این است که در نهایت طرف آمریکایی ناچار به پذیرش چارچوب‌های اصلی همان متن شود.
🔹
علت اصلی افزایش فشارها، ایستادگی ایران بر مواضع خود در مذاکرات است
🔹
متن مورد نظر ایران، به دلیل تأمین منافع و مطالبات تهران، تاکنون با موافقت کامل طرف آمریکایی مواجه نشده و همین مسئله یکی از مهم‌ترین موانع دستیابی به تفاهم نهایی به شمار می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/658437" target="_blank">📅 15:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658435">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeEwExjRk1aznLvG0Eek_jhvcjKLe8RrZsyFS22pHCgkC-7aPS9xEUDOIFnZVWo017FLztlGw5eZuDrFhdVGXX5r-dmSsBDT2jAXhm0_AGfX67MIIInMXPg6fuwW1d2Hqfj8bN_Fx3wdMGS-4C_i9qlS4L7yMMUmTGBumJossv3hCkOQ8IIxM_OTwWPbRn0DY6rjYRglJQGn1QkVUwXHMjhyN9ixXbGJBobbhQT-ayasqzI7kE2foXTppvh1NBCctPH5ibqeMKWGGEQ9yIuR7aEoJIR_eMWd0zkID2a4r0LknvMNoDEqcp8w-XGG-gdUj3EcEK_wwj8OkorLmsWGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه مسابقات امروز جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/658435" target="_blank">📅 15:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658432">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcvAkQRHDIPVWyfvPh9uEwCgKVqH3mLK739tb4TrSOQW8kpWY2nD-4g5WmjcWHQKjfU1dnYlNflRMrigpnDSCWEqeSLy4JIHMJu8BYPW_ISrg6b02KO4Bxhw64QX2e99vRDwgnz0PDS1uQhVqfUq-mzbpopiIfSUUaCesNnHZ967ooI2TllyqxqwYBZb4fIjA1EqoAxJ32MEkrgORyu3bzmTk1RtRuaIFv1_robhaEVBf6JwRbMbohIehc3T631CRD55vFQEcbor_uVKKwzhYCXUBFLiuTnAlTiHy7MO-wW41TkA5dEPFDW9vEfgoENlqOwQ6ITTJMYjWfzX0ytAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKog0doRnwU7jTlY3OMLqiBHhMyS7TYQNqX9OSSVrYdg_F6xWCe2g3CeNVnRXAqgkPuOeloqvb-KfaAiPQWtt7LXqzT9eD4cX4f1djfEgZlYzhIt2FE1ZB1kg10pc80WfKjZK9yWuSOyLQb_42-bJpAT31C6YHr4lwE6oSHv8PhIptjqciyMpTLVE6ju8wYbMhZBXhxl2y9NS9wVQRNkAbQ0hN3UP8BicwAHK8ct-Q6M23fJvw2QAtLoyxEkqQNJqiabxTZxf1LmZWQMJo9CUSh3KUni719lI3ftIdmkd-DEC7DqdztwpoBs1FdJdzcsMTITLuzZf7L_txtvP3HLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fo5-6axboqeX372OJ9Ux_yJ8wwcKcwef8TMNeGTRh6oHbqiBpCkkWF_lz0GsCR1UjMQM-Q3yOrjqJrWvxRJ7K67Caf0J3cFNT55GZ9l4RB7ibAZWKxzSnypgTVe0us-l_ziVr2JgxjJHLH-cJMvVPDOMfwiE1UaFtqUscq5MQ9h-269B0zZKFGz3iHjh1w4FBuu8rMH51s6Ab4B7_Eormw6aAP6thPAsgzw7G5zCyxa8AE7uMtz6d_piZXUzwkYpHUoA_taQnK9lASyYvbPQASDWfGSBch9FM5gQ5j6d_TNwCCAH8r4X-B3xGUVf5kkafBzd4FtdX9s0FylDs6TP3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از دانشمند ایرانی که توسط عوامل موساد به شهادت رسید
🔹
دانشمند متعهد و نخبه، شهید دکتر علی احسانیان که در تاریخ ۸ فروردین ماه در میانه جنگ تحمیلی سوم در شهر نیس فرانسه در حالی که مشغول تحقیقات در حوزه هوش مصنوعی بود، توسط عوامل موساد هدف حمله ترور قرار گرفت و به شهادت رسید./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/658432" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658431">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
حمله سنتکام به یک نفتکش با پرچم گینه بیسائو در دریای عمان
🔹
ستاد فرماندهی تروریستی مرکزی ایالات متحده (سنتکام) اعلام کرد نفت‌کشی که با پرچم گینه بیسائو در در دریای عمان در حال حرکت بود، توسط یکی از جنگنده‌های آمریکایی هدف دو فروند موشک هلفایر قرار گرفت.…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/658431" target="_blank">📅 15:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658430">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622f83f9b0.mp4?token=otU5IZWbFpKSd0X1ZfISKSlTlHbbJC1ENIDjKRj2JfL2Uia6yZsaxLG42LolGGl-psu9zUEFsn4FHg1B8eF6l_nR_518eDZmwmepM_jUuiC_zIgzs5epwJ0aQ3f26VrlTh6Qf_u19ItgH2p4WqXxV9-aESRm--dDkjKnSnfObxfvGa4VIV1qumkPUsfRsVxizKGGWN8cPMjR28mrR3wzmoyLH4E4dmWZU3nRTrQoUo7MuBADwDiTrLxl7-CWNVjq3aJQuG8vgVyjhaYdBBOUxBVl9_O4S-5DFWnFVpNi3kkOkJoJSFXoWhNRCTc7hOubWaWX2yd5HdV-6JuC711ZEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622f83f9b0.mp4?token=otU5IZWbFpKSd0X1ZfISKSlTlHbbJC1ENIDjKRj2JfL2Uia6yZsaxLG42LolGGl-psu9zUEFsn4FHg1B8eF6l_nR_518eDZmwmepM_jUuiC_zIgzs5epwJ0aQ3f26VrlTh6Qf_u19ItgH2p4WqXxV9-aESRm--dDkjKnSnfObxfvGa4VIV1qumkPUsfRsVxizKGGWN8cPMjR28mrR3wzmoyLH4E4dmWZU3nRTrQoUo7MuBADwDiTrLxl7-CWNVjq3aJQuG8vgVyjhaYdBBOUxBVl9_O4S-5DFWnFVpNi3kkOkJoJSFXoWhNRCTc7hOubWaWX2yd5HdV-6JuC711ZEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا همه با پرویز دهداری دشمن شدند؟ | من در خواب نامه استعفا را در هواپیما امضا کردم
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/658430" target="_blank">📅 15:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658429">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
حمله سنتکام به یک نفتکش با پرچم گینه بیسائو در دریای عمان
🔹
ستاد فرماندهی تروریستی مرکزی ایالات متحده (سنتکام) اعلام کرد نفت‌کشی که با پرچم گینه بیسائو در در دریای عمان در حال حرکت بود، توسط یکی از جنگنده‌های آمریکایی هدف دو فروند موشک هلفایر قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/658429" target="_blank">📅 15:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658428">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUWF4hJU1WwdS6diyjtP4wOkly-I8zBk6FhrXpxmWhSpnLLNBlK-3qJK0xDWavc-jH3HTM4TbZVyZl9pDH0lpk7pt2iPdQqUoAj1xBbMT8AdaE8Juzk-C7jS2aQD2VfXUvr7aBmc7g4BNGgLBN9Z_B3yKg9TW51m_YntQE7cH0ZR2YRseN9-LDr5WFHW3so2Bq5pGOm9EOtkep2pezYgsEBXpv0-ykCfvKOqM5u9veZ7fWxHQhcsDVKKyo_rFaNgeiw6QOEr0gDZB6hixt2YK0yS1TsXe4FTdwCiYlm5qzaeHWNObXtB8g7igYUZAoHfL_lCqE13Tf8nWV2pg0lmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسدود شدن دوباره تنگه هرمز چه بلایی سر جهان می آورد؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/658428" target="_blank">📅 15:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658427">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsdLHnrlCk31aG0z-3BOiAJWrV76sZKzUlmvvlTO_QEIVl314yjW4mDOgdgWTyJyo-OimDwWuapMVEzFNvg5OkvxFtt7CrqFvxwSS2BwAQhCIdaa1xAxe5vSxkRV9WzIrjm-01ocv3qp8INRhzJZ112TPJ5qGpCzjwCPo5oEdI_93ChP_-iXQrY36Sim8huWBn7rrge1re8cF7CcYgyC5hnlvyxp5f0aOvUPB--_S9XL7Jb3HIkG7EITnOdDW18wWIJkq508mK6yru3yVvRukSJ5_4-O2W6HsX7tuYOyWU7SKFA5GYW95PbKwhXY9atw3rmxcuBeBwb2lpqQ4rdIeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند؛ جایی که یک انتخاب می‌تواند سازمان را تغییر دهد.
در رویداد تخصصی «نقطه تصمیم» جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود در مواجهه با بحران‌ها، تصمیم‌های دشوار و فرصت‌های پنهان بازار سخن خواهند گفت.
اگر به دنبال شنیدن تجربه مدیرانی هستید که در خط مقدم تصمیم‌گیری قرار داشته‌اند، این رویداد را از دست ندهید.
یکشنبه ۲۴ خردادماه ۱۴۰۵- ساعت ۱۶ – مشهد، هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/658427" target="_blank">📅 15:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658425">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPOt5BI1He2RJYpHJ0rDXwauxoW3HpoQpOwrGiz2WGt2_tI-wU6kQ_HCFrNizw-4WfMnXpPGFgp8IJOhFQYiLTm-DEBRckVOd2RNtw5xRpjXMmUbCXRMsSd7Ginq5GjHfXGk4WaArLTy5L2JzRKI_AVRPAaU13tmwMCLdXu7CfsXINFOHOsaydYK1cTIsnNzcrIEYPuA6xHCyq0HWPoVBBHyD7n7RtfH0p9kbyWXJ3O0tHmbv6ME58618VVbny51LpTK5AanlBJwvteCBHZPZxsjT9krN3d0Rrqv9-Dm_LcszRnUnQuL5xGFc0pkq9mPnS_yeEu14PCcJNESBksa-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmEF5DHf4KAY2ed_52mcDLdwknCt1Y0QFV8PsdRL1Or19WUnb-Usc5heLiguS_q5-QxjuhJMnaS0fFTFA0Liyx_DerORJT6gTQsHmzlgILPrpHl5mcsZsLmNlje234aKJsHnkWbeoQRy5BcP6ZpLie9eJ6hL-B207FKhdR2K-2xvx1WaR5U72aQKV_wHEKqIQtf817g8oRNOUNwgItqxuR789-bEZJ3yNN3nn4u3iFtaWFMR_dysUc5bC_XinLeSW9XAseE3we9FpWTs56qjswHDQvuxtvtE1-pyOOKv3CV_AhNyhhcfLHowl0exL3L9-CSDu9HFrIk5XMvpWTGbww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تداوم نقض آتش‌بس حمله رژیم صهیونیستی به صور در لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/658425" target="_blank">📅 14:59 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
