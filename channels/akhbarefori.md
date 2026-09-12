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
<img src="https://cdn4.telesco.pe/file/ceNHDQbfAK16gq_FGVVgh5iLUnT-tFU0ZzLRVHeyPA1DCRJi8n-G6ZzDz0WoO4Vtm-ohqK14AYDL3HEtW4MyPkZQUrx0wXOKoWS3AZ2bjMyJcTPehJ-lGdmizZeSdFear0oQDvtX7-VMG7NZKSEGuZ9YVP7iAxUNjHm-Sb-KrxpedW463hi_-ckPyDu-XDLU1HpMfkAODuRiMolHmR9kqQwhtfCN8JrNXoGIe03P4NUdSGcEIfr3YIQPz1LAiEHYDZwR9TRAuNnmHmlxpdxRpYdQD2DM2bW1_nt3G2M9ubH5jSPek7UsHH5Ct5avkE0c19mGsnnOQZwc7ScD0FSuwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.22M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 17:45:14</div>
<hr>

<div class="tg-post" id="msg-689277">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae86cf3f01.mp4?token=BqzjclRVDZtVEZ1WCau-wZSKfbRrSzgxSkyv0kRMfWVHbB6KKggWIa8lQ1oIEc1cGNp1Yj_8oA8YsaLZWOSJp8CtM5OQG87t7wAMQogc2gKjKBfNNah5G01vn6Qc1nQIpHt9huwzJ_vFz6BaD-QlXM0hrhSpI5kHOXqSc7uFFAeqjABORMHLBxHPuJHjIC_ya0QzaAnA5YoWRZw1FQs7qUVEDXkhv9fKWihMn9tsmrDERGd-vymN4Pxso53f05hFEqEaw2C1IKqYtV5UHBW0xbdU8myctYEZLSRP-5ACpX_nnWtqjOwnSQTWlgUoB9PxZBr5Fzxv9dUoFu7Nk4mjgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae86cf3f01.mp4?token=BqzjclRVDZtVEZ1WCau-wZSKfbRrSzgxSkyv0kRMfWVHbB6KKggWIa8lQ1oIEc1cGNp1Yj_8oA8YsaLZWOSJp8CtM5OQG87t7wAMQogc2gKjKBfNNah5G01vn6Qc1nQIpHt9huwzJ_vFz6BaD-QlXM0hrhSpI5kHOXqSc7uFFAeqjABORMHLBxHPuJHjIC_ya0QzaAnA5YoWRZw1FQs7qUVEDXkhv9fKWihMn9tsmrDERGd-vymN4Pxso53f05hFEqEaw2C1IKqYtV5UHBW0xbdU8myctYEZLSRP-5ACpX_nnWtqjOwnSQTWlgUoB9PxZBr5Fzxv9dUoFu7Nk4mjgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیدا شدن جستجوگر مادون قرمز رهگیر موشکی تاد نزدیک مرز اردن با سوریه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/akhbarefori/689277" target="_blank">📅 17:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689276">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
رئیس‌جمهور چین، شی جین‌پینگ، پیشنهاد ایفای نقش در مذاکرات صلح میان آمریکا و ایران را مطرح کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/689276" target="_blank">📅 17:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689275">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
بقایی: مجموعاً ۴ موشک طی ۳۵ ثانیه به لامرد برخورد کرده‌اند / ما قطعا این جنایت را پیگیری خواهیم کرد  بقائی:
🔹
شواهد و مدارک نشان می‌دهد که جنایت لامرد قطعاً توسط آمریکا اتفاق افتاده است و در آن شکی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/689275" target="_blank">📅 17:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689274">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بقایی: مجموعاً ۴ موشک طی ۳۵ ثانیه به لامرد برخورد کرده‌اند / ما قطعا این جنایت را پیگیری خواهیم کرد
بقائی:
🔹
شواهد و مدارک نشان می‌دهد که جنایت لامرد قطعاً توسط آمریکا اتفاق افتاده است و در آن شکی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/689274" target="_blank">📅 17:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689273">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51dc103e87.mp4?token=Qlb7OD_SyB3PQccGP821u1C9FXdk1WoYiHFI5dwxCZTGBfAvKV6fOcsS49Y61O69vODkzCKZIa_QdQosX-_KFdbUgWG7uakFlU4BkOUcFqo-EcmhoszFYkogwrFBQIKzmTBM5kdsgJjbEsLT1PTuyRpV78lZcqa_HoVClGi8c13bXV6rOQxlMpAtyUjJp5VLGPHxvExFWOwLaxN3DcsLSqF9fHeZ5D6s9L5b1TcuH7CFZ43r-sm_EXSHkqB-VsPon4-1w8PcIjwAwqVedqAFB6i8lN66ps6y4K2NETX5k5EUgC-xs3hsHg81DVrJNrYutO9iVp3faAAWaqQa2mfFnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51dc103e87.mp4?token=Qlb7OD_SyB3PQccGP821u1C9FXdk1WoYiHFI5dwxCZTGBfAvKV6fOcsS49Y61O69vODkzCKZIa_QdQosX-_KFdbUgWG7uakFlU4BkOUcFqo-EcmhoszFYkogwrFBQIKzmTBM5kdsgJjbEsLT1PTuyRpV78lZcqa_HoVClGi8c13bXV6rOQxlMpAtyUjJp5VLGPHxvExFWOwLaxN3DcsLSqF9fHeZ5D6s9L5b1TcuH7CFZ43r-sm_EXSHkqB-VsPon4-1w8PcIjwAwqVedqAFB6i8lN66ps6y4K2NETX5k5EUgC-xs3hsHg81DVrJNrYutO9iVp3faAAWaqQa2mfFnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از تسلط نیروهای مسلح یمن بر برج کنترل تردد کشتی‌ها در تنگه باب‌المندب در شهر مخا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/689273" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689272">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
رویترز به نقل از منابع نظامی عراق: منطقه مرزی الطیب با ایران پس از کشف محل‌های پرتاب پهپاد بسته شده است./ الجزیره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/689272" target="_blank">📅 17:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689271">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVvaiSXacQaevVpbBDZsTwzngF5XJ-CY1354mFzeFSMgbcBZCdgj6BD6YySWnLxKTgwKf6jOTOzJ5pr6HlhUMvNaMbeXtTQ0Qp-jAW9UT2XKwvqAtU8Kz_c5cONMvwjbTG4VR-qX59mEE9kVXyukZAH44WW3kasY7Zo0NAmO33LHu7cTky9PvwL9YYLXvkQXdkvKsBO1qdTG9wZvmCMuUbrids3aRLiCiEih7iN8bPd7_pbmBf2fQ-T7c-JP0hJxO_Y9LMOtsZHbrq82vRAgvSFA8ePbE44-bBAODQTUNVBe2cth0sOnJf696Yq6UarQUoHCsKjg_ClYHVWW8f-qXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مایک آدامز
:
نفوذ آمریکا در خاورمیانه اکنون کاملاً فروپاشیده است
نویسنده و فعال‌رسانه‌ای آمریکایی:
🔹
تمام شد؛ از اینجا به بعد، کار برای آمریکایی‌ها قرار است خیلی دشوارتر شود؛ ترامپ حسابی گند زد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/689271" target="_blank">📅 17:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689270">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-RulKQ3NddOVfnDIU56xcE_obhqS_41QT7gFUql6qsCXPEKHyyZNdhwzNzQ_xfHrfegqrLioQ0LD9MC7FVPJXA0JPG9dpCar_BkShBK4aX_g6ApmoQgT6Qngd_LFKSt6xkuksa3It9KUdebd776aeLN3WTZ42AsD8IluAR-cF_GODGMNNojYVaKVHUGRFRDzj_pn-rRBQ8UV6YmYHeRkbSAxnRvJf768yAvGX_RGhPpVodWb6VSXTrYTS6KbVRUgW5FNaSOgLrn60moI91oEIynHWDoX05Ld_fEhdiUJDueg7TCpIoHdsSaLsrjX9GpCQWpdVVBnZ-V11TKeFdyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ملک اجاره‌ای دچار خرابی شد؛ مسئول پرداخت هزینه به عهده کیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/689270" target="_blank">📅 17:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689269">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGxXq8jTHDtqPOzB1OQOG73v2LgNxzv8QFYnXHppZl0Tn-o5XeBz-Sz4rTThUyAGPZnXHE7MHM-Sge8mrSZLrSmE-b-2r9aMp2wODikhV4UvzH996mUECLoI55vZwrl8TKIp4RRkW2NmTf5lAaWvgcnyWMKaNHoHcaCbtRF9Y9hAxDpEvavcuVz1UvlVKYRbG8xENLNTSgTsTWokaKH4mEUerX_V-TWHDA1tmzq3K5YnEi1DByRCme0HktHeRYP7G8-FI3ftboV1ZD0prGY3afvZ4Ge-kfoN4nxqIoDd5JHmBl7T0CWcyfkglw4yZFRdlU2vDJj5D3jpbwCDQs8p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اجرای عملیات اضطراری برای جلوگیری از بروز خاموشی در صالحیه و گلستان
🔻
مدیرعامل شرکت توزیع نیروی برق استان تهران از اجرای عملیات اضطراری احداث ۳ فیدر فشار متوسط از پست فوق‌توزیع بهارستان برای افزایش قابلیت اطمینان شبکه و جلوگیری از بروز خاموشی در شهرهای صالحیه و گلستان خبر داد.
🔹
این عملیات با حضور ۴۰ اکیپ عملیاتی و طی ۵ روز انجام شد که طی آن ۱۸ کیلومتر شبکه فشار متوسط هوایی و ۲ کیلومتر شبکه زمینی احداث و ۵ کیلومتر از شبکه موجود نیز اصلاح و بهینه‌سازی شد.
🆔️
@nabzeetehran</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/689269" target="_blank">📅 17:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689267">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
مهاجرانی: فعلاً تغییری در نرخ و حجم بنزین سهمیه‌ای نداریم
سخنگوی دولت:
🔹
به‌محض اینکه منبع مالی پایدار برای کالابرگ تأمین شود، مبلغ کالابرگ افزایش پیدا خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/689267" target="_blank">📅 16:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689266">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQrDL3Xl60SQ2hNQ48xyeWAlvlrKyD9Y16CKdBaoXOXJC6nxb4L2kAsenMrrZlpPYA2Dq8ZbSrx3Ah0zUIp7dI2HpW0U-3SzgQCCY3q2XbD5Vn6kV5rInwm35S50iqfKoUJpmDncdzH8xfYsT2vBHrKGpL0D3hzPq0ipXk_ys3kT2NDxhSD7oCwc8FMgZi_gUXsFrbaYUiJ3SYc48k3aF2tBmE7mSgWr5zviVBnFCvLRNQd5BKmP_cNkjkKRVTHKkyjF0Tti-jtYSOu5Z6Mypnj30mkexqneJ70fcpoSRz42DqZQKwLgVsmYEEMdIzvwmwvw1ntI06M4Ah65M-u85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای کامل از بین بُردن بوی بد در خانه
🏠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689266" target="_blank">📅 16:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689265">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
بحرین اعلام کرد که در نشست ایران درباره تنگه هرمز شرکت نخواهد کرد/ همچنین طرف هیچ‌گونه نشستی که ایران در آن حضور داشته باشد، نخواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/689265" target="_blank">📅 16:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689264">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
شایعه توقف پروازهای عراق تکذیب شد
سازمان هواپیمایی:
🔹
پروازهای ایران به نجف و بغداد طبق برنامه در حال انجام است؛ فرودگاه بصره به دلایل داخلی عراق بسته شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/689264" target="_blank">📅 16:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689263">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
حاجی دلیگانی، نماینده مجلس: طرح سه فوریتی را برای خروج از NPT آماده کرده‌ایم و بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/689263" target="_blank">📅 16:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689262">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4b31107.mp4?token=ifa_v__xdEpY21UP16yhmMDCu8AoRFHi-AgEvMaVN8hyCOJb-ijK2pSwoD-GqhsyaNJ2WAxeBYLkPXons3Xbl21_wwVD3pWv4bJH3XWvPaF8Pnq230C02ER-s1L0AMUDhXeTmkncgM5BP2L_QBiYGau5EYDoT390LXhjTq3JoRwPAnpBExvnty3JKy3XMap45E1IC-vg11KkFNomTUeRNI4eZpijPo6D1H4w4G_FLwkfAa85Xh6Cffe6FsXuEhBjqIEwAHpAatUvddAGg4GiQxQj00g_Qh79yzNOhk-lvvNkF8_9Sa1dnt1yPv1orBBbSCiFRktNcbtlMRtylX7OTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4b31107.mp4?token=ifa_v__xdEpY21UP16yhmMDCu8AoRFHi-AgEvMaVN8hyCOJb-ijK2pSwoD-GqhsyaNJ2WAxeBYLkPXons3Xbl21_wwVD3pWv4bJH3XWvPaF8Pnq230C02ER-s1L0AMUDhXeTmkncgM5BP2L_QBiYGau5EYDoT390LXhjTq3JoRwPAnpBExvnty3JKy3XMap45E1IC-vg11KkFNomTUeRNI4eZpijPo6D1H4w4G_FLwkfAa85Xh6Cffe6FsXuEhBjqIEwAHpAatUvddAGg4GiQxQj00g_Qh79yzNOhk-lvvNkF8_9Sa1dnt1yPv1orBBbSCiFRktNcbtlMRtylX7OTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از روی دود اگزوز، عیب خودرو را تشخیص دهید
🚙
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/689262" target="_blank">📅 16:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689261">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-rJZD2mO3fUDWrH3-9ptx7J9_7s3lijlIgRUP9ukOY_LfIZyiSq341iJdCl47yzE7zBZLsXxEckSPP5Gy-WTc6jn1sRULHfzB5ljDlRGbvamC9MMmkPqRHw93n9xG3wMnGrfO7YOhh0zm33KE2F0wmHHJnomUq7bfvyRKWUxypZteesmcboG0OcOgcAvOkGuxSg-3d5i5wkHKyLN8p0RF9_569oEg-dM18tvZTWb22pm_fG87CTkB8ykXmNytsoVg6FOZV6H05RFSTWfcM9dyNt3O9veC3c6bUAh7NsVKoDtPTQlOLSC6Tp558NJttmDdxiNKyW23oulcC7vdB_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره میدان ولیعصر(عج) موقتا تغییر نمی‌کند/ آغاز ایمن‌سازی دیوارنگاره
به‌دلیل انجام عملیات ایمن‌سازی، دیوارنگاره میدان ولیعصر(عج) موقتا با اثر جدید جایگزین نخواهد شد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/689261" target="_blank">📅 16:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689260">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر انجمن تولیدکنندگان مرغ گوشتی: ۶۰۰ هزار تن مرغ روی دست مرغداران مانده است
پرویز فروغی، دبیر انجمن تولیدکنندگان مرغ گوشتی در
#گفتگو
با خبرفوری:
🔹
برای تأمین مصرف داخل و ذخایر استراتژیک، حدود ۲ میلیون و ۱۰۰ هزار تن تولید مرغ کافی است اما در شرایط فعلی ما حدود ۲ میلیون و ۷۰۰ هزار تن مرغ تولید می‌کنیم که بیش از نیاز کشور است و این مرغ مازاد روی دست مرغداران مانده است.
🔹
درحال حاضر مرغداری‌ها در ضرر شدید هستند و خیلی از آن‌ها ورشکست شده و از دور خارج شده‌اند و با ادامه این روند شرایط بدتر هم می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/689260" target="_blank">📅 16:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689259">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPl9FGAluc3FXSx_W4Yt2zWyTE5a3sAp474qKiPX5Z7x3-nCA2M55LWmks04OIh8lzU64_R0VwKj4R0T4ipsz85K2nUGFn_IypeE9jcLzb4I1YyD2KCoOTEsj-5Ku3rvm3OQdBOxaVxfnPlk7GrrsuJiDnQCy3cU9YefOyRBgwb_STyVHCBFPSdAKwecgrc4_tVz-lJK_WAR-_TS5CjHhdMusgCz1OpCVWuYMNfNbaF64hHx1LcLhEB-MCa_i-N6ZsMNgBefo1RBAjhfSz8wWes06tQv8drOGMwiXHbVhMl4C3DGmHKnClSelRJKJ4RdVRZ4TQo2WhfSHyP3YRjXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ که این حرف‌ها را می‌زند، ظاهراً ماجرای آخرین درگیری با حوثی‌ها را یادش رفته؛ همان ماجرایی که ناو «ترومن» مانور گریز داد و یک F-18 آمریکایی در دریای سرخ سقوط کرد!
به توییتر خبرفوری بپیوندید
👇
https://x.com/Akhbare_Fori/status/2098737810995806411</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/689259" target="_blank">📅 16:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689258">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تحریم به ارسال مقالات رسید
🔹
معاون تحقیقات و فناوری وزیر بهداشت، با انتشار تصویری از صفحه محدودیت دسترسی شرکت Salesforce به دلیل قوانین تحریم‌های آمریکا، از ممانعت کاربران ایرانی از ارسال مقاله به یک مجله علمی خبر داد و گفت: این دیگر تحریم علمی نیست، جنگ علمی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/689258" target="_blank">📅 16:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689257">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سی‌ان‌ان: قیمت گازوئیل در آمریکا بیش از ۵۵ درصد افزایش یافته و در برخی جایگاه‌ها به حدود ۹ دلار رسیده است؛ در صورت عبور قیمت از ۱۰ دلار، برخی تابلوهای پمپ‌بنزین امکان نمایش آن را ندارند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/689257" target="_blank">📅 16:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689256">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z04UJt_f5gvjn3A3iovJAC2co4LYYh608mCbQVMDkoky3YHMCjdoLhAQ5vxz9OeFuOH1cLhuFe6iu-eU-tZd4gfZ9X9Z3DaIt5ymS1WxOZ98sa0tkwSwLIZLh0XQOTpCSBOz8uYthgYItD-8dFtmp7tYLhPaiwbYKmHZXnMrFZ-cVxlMyjFY7TgA2aPYroxnPZneW5nOPg_oCAhVV3pvyf9mSQUydvPQw5kpOy-6RprgfzZTg4BpwlI_22odHmCAeABJW_pPFfndcnjZEySa4Tqe3zGUjQzpyR6lxM-si7A1ZTWtyrUIHMGYalvvh_9DDpPiRDfoClhUf_1Y2ijB4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرداخت خسارت خودروهای جنگ از ۴۰ هزار میلیارد ریال گذشت؛ منازل از امروز در نوبت جبران خسارت
🔹
رئیس‌کل بیمه مرکزی اعلام کرد تاکنون خسارت ۳۵ هزار و ۸۴۱ خودروی آسیب‌دیده در دو جنگ به ارزش بیش از ۴۰ همت  پرداخت شده است.
🔹
همزمان؛ پرداخت خسارت اثاثیه منازل آسیب‌دیده از جنگ ۱۲ روزه از امروز آغاز شده و بیمه ایران روند رسیدگی و پرداخت پرونده‌های باقی‌مانده را ادامه می‌دهد.
🔹
بیمه مرکزی تأکید کرده پرداخت خسارت‌ها بدون وقفه در حال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/689256" target="_blank">📅 16:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689255">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
خبرنگار المیادین در صنعا: تردد کشتی‌ها از طریق تنگه باب‌المندب به‌صورت عادی و منظم در جریان است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/689255" target="_blank">📅 16:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689254">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سخنگوی سابق وزارت‌خارجه آمریکا: ما دقیقا می‌دانستیم داریم مدرسه را هدف می‌گیریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/689254" target="_blank">📅 16:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689253">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f796d356a.mp4?token=YfapI2Ne_5A3pSUWOetXn1gxlOmLOp5-yT2kwblFVWxn4QRhoo0uWCMpXhvPo_WoaZJ-iCcDrqPlwtPpKjY1khCLURrTxNNSOBOjal_9Kwdw3g8juNV1uogirP08JWy4o0lolzhUZjnbGc3Y_y0fQsOdIFi7wXnqUMInUfzFbnZlxN6X-W5eltppRwirx-qwnncl9p_yxGptPuKANvUv1bC_2Z7ENMxJCjZsLpOTevfqgbl58CQ0xMDMDaw7dptOVtg2TBPotgbkb81YdTKRux0do3qE1Y7xmefyb1lBUNePltL1iItGGEEsCKRUYP-0quSNpw8-xt63b63KSvPPbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f796d356a.mp4?token=YfapI2Ne_5A3pSUWOetXn1gxlOmLOp5-yT2kwblFVWxn4QRhoo0uWCMpXhvPo_WoaZJ-iCcDrqPlwtPpKjY1khCLURrTxNNSOBOjal_9Kwdw3g8juNV1uogirP08JWy4o0lolzhUZjnbGc3Y_y0fQsOdIFi7wXnqUMInUfzFbnZlxN6X-W5eltppRwirx-qwnncl9p_yxGptPuKANvUv1bC_2Z7ENMxJCjZsLpOTevfqgbl58CQ0xMDMDaw7dptOVtg2TBPotgbkb81YdTKRux0do3qE1Y7xmefyb1lBUNePltL1iItGGEEsCKRUYP-0quSNpw8-xt63b63KSvPPbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کینه شتری ترامپ از ناتو بخاطر تنگه هرمز!  ترامپ:
🔹
ناتو نمی‌خواست درباره تنگه هرمز به ما کمک کند. پس چرا ما باید به آنها کمک کنیم؟ #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/689253" target="_blank">📅 16:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689252">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
کارشناس قطری: ترامپ قرار بود بر تنگه هرمز تسلط پیدا کند، امروز نه تنها بر هرمز مسلط نیست بلکه تنگه باب المندب هم به دست متحدان ایران افتاده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/689252" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689251">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e33b0ddbc.mp4?token=ndn7oiPYZXGOoJ3_Det7KRkMC_K3G86p6HARsYj2Z1FjOI6YSDTIa8yLkBWGL2z_VzzkMDW4ev2_GImjWMWDVWJUY9xDPpkNy0LWNkBORlAtsGMX92HP1GQ9uO9_1Q5thnviIhcJYGyMadewUVjSnjlUiUlOB_xDLzpZpjzPsZPFPzlvqm5CVlTHrkAZUKAzBo-D0i7SP7lomlO5CmcUnobCksWHmgtVTIYtLKFlS9Cl_4YIfC0f6ZhQytFPu0oKzpcjW6-LbEU2EtxdjGJpbQjdL2Sas0VMTXGtN4uHiz0in77qppOkQCmkwC4Bb2x79oYZMqrSuLI7fl3WGYer8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e33b0ddbc.mp4?token=ndn7oiPYZXGOoJ3_Det7KRkMC_K3G86p6HARsYj2Z1FjOI6YSDTIa8yLkBWGL2z_VzzkMDW4ev2_GImjWMWDVWJUY9xDPpkNy0LWNkBORlAtsGMX92HP1GQ9uO9_1Q5thnviIhcJYGyMadewUVjSnjlUiUlOB_xDLzpZpjzPsZPFPzlvqm5CVlTHrkAZUKAzBo-D0i7SP7lomlO5CmcUnobCksWHmgtVTIYtLKFlS9Cl_4YIfC0f6ZhQytFPu0oKzpcjW6-LbEU2EtxdjGJpbQjdL2Sas0VMTXGtN4uHiz0in77qppOkQCmkwC4Bb2x79oYZMqrSuLI7fl3WGYer8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کینه شتری ترامپ از ناتو بخاطر تنگه هرمز!
ترامپ:
🔹
ناتو نمی‌خواست درباره تنگه هرمز به ما کمک کند. پس چرا ما باید به آنها کمک کنیم؟
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/689251" target="_blank">📅 15:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689250">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb966b696.mp4?token=oqpyS-afJdebVR7E2l4ziBswtaDD9n8mjRcl-2ZG3LyEE6YQAcBtvAUtTslrt_b3xSxqzubWo4ZuzVyFx3k0kdQ0ex3YebmWcZvvFz5TruUo9Am_h_db-BdTdiCj6V1dknRWA2vfoWGM8f_bQvREC4ycapqFxcrZWPzErcofIanr6ldeBB98WcljanrprpmzxGSc9S56XtC2TfxGZ3AY8axnA_lPg5L7gTcOXtlXYyhtubeqt3L94ciSniSgVsZ-7u8H01Pmiv4vmzUcpHgpNYNPSYUjR6Kg-Evu7kjxErN4I-KSMpN4k9UHCvQFjhzUx5ZRPIqQ4osSy4ykyU0kqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb966b696.mp4?token=oqpyS-afJdebVR7E2l4ziBswtaDD9n8mjRcl-2ZG3LyEE6YQAcBtvAUtTslrt_b3xSxqzubWo4ZuzVyFx3k0kdQ0ex3YebmWcZvvFz5TruUo9Am_h_db-BdTdiCj6V1dknRWA2vfoWGM8f_bQvREC4ycapqFxcrZWPzErcofIanr6ldeBB98WcljanrprpmzxGSc9S56XtC2TfxGZ3AY8axnA_lPg5L7gTcOXtlXYyhtubeqt3L94ciSniSgVsZ-7u8H01Pmiv4vmzUcpHgpNYNPSYUjR6Kg-Evu7kjxErN4I-KSMpN4k9UHCvQFjhzUx5ZRPIqQ4osSy4ykyU0kqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: ریشهٔ مردمان زیدیه شیعه در یمن، که امروزه انصارالله یمن را تشکیل می‌دهند، به مازندران و گیلان بازمی‌گردد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/689250" target="_blank">📅 15:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689247">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9207a3b1ca.mp4?token=aQDU306H5rg4i7ixnpOYqDHJZ0voVD0PviWCqt-MJ4vbJYXUAzmsRdxppjhkWLAb4T470PTr7DVdDKd9ShomIDn4TYp70fAAy3L9QloAVmJ1rsyoMeI6qZJI_blP0DYvhbOwr4ThbEkrzHrVlALkWL5QisKZ7fSct4LKirFC6RKeXTSoxVwO4NCcpE5mNfq_WFl5hmeBjBjqHtXMHKIJS_ZO-OBne_0B7e0YYqLbRVRYUasy8SnbRhhQpU1fzp9utbjsXcdM2h2UTxkfrxN8YbKBoSHe6-R6VBnB_ZiXt1bK5XefGRY_4TEt_VX0SBtswtQphmTcfLIKh19FQgvoADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9207a3b1ca.mp4?token=aQDU306H5rg4i7ixnpOYqDHJZ0voVD0PviWCqt-MJ4vbJYXUAzmsRdxppjhkWLAb4T470PTr7DVdDKd9ShomIDn4TYp70fAAy3L9QloAVmJ1rsyoMeI6qZJI_blP0DYvhbOwr4ThbEkrzHrVlALkWL5QisKZ7fSct4LKirFC6RKeXTSoxVwO4NCcpE5mNfq_WFl5hmeBjBjqHtXMHKIJS_ZO-OBne_0B7e0YYqLbRVRYUasy8SnbRhhQpU1fzp9utbjsXcdM2h2UTxkfrxN8YbKBoSHe6-R6VBnB_ZiXt1bK5XefGRY_4TEt_VX0SBtswtQphmTcfLIKh19FQgvoADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبران بریکس در دهلی‌نو نهال کاشتند؛ نماد وحدت و رشد آینده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/689247" target="_blank">📅 15:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689246">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ ایران به فینال آسیا راه یافت، شاگردان پیاتزا کانگوروها را هم شکست دادند
🔹
ایران ۳ - ۱ استرالیا
🇮🇷
۲۵ | ۱۷ | ۲۵ | ۲۵
🇳🇿
۲۱ | ۲۵ | ۱۷ | ۲۲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/689246" target="_blank">📅 15:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689244">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
آسیاتک حتی در شرایط جنگی خدمات خود را توسعه داد!
محمد بابایی، معاون کسب و کار آسیاتک در گفتگو با خبرفوری:
🔹
آسیاتک حتی در شرایط جنگی سعی کرده است که زیر ساخت های خود را پایدار نگهدارد و خدمات ارزنده ای را ارائه بدهد .
🔹
آسیاتک خدمات خود را حتی در این شرایط گسترده تر کرده است تا جایی که در زمنیه فیبرنوری نیز در ۱۰ استان کشور خدمات ارائه می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/689244" target="_blank">📅 15:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689243">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dba894d91.mp4?token=JK_sWJC4ThVf0pWC7cpXWKc8wxHnRcADPN-YZiGZoK5E-O_bOVtRdNfsGLa3rVytI_Tn33BBEeUnTJMwTjQzSHUVx-zvsI4ra6XAFrXIEDuUKdW2zjPv8DuU0k9hpXZszsyB-RJphKENb76Gj3rhIFKUFCFZrCzweWeaMvtjQhAQNy3aqHCJT79odxIBF4BKewByiiUXPPfKpYJfXfGjBnCszaU4b__q77S50NMVmUqKeBg2z1sw8bGRdbKt4YEE6-TSg_7-xOHHzs9SVai98Z9jtqXUj_H7_MR0ZOiQx9K6rnFNiZj5DGWGAH5Y3rAn5XtYKI5UkH4cP5iMZLAkLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dba894d91.mp4?token=JK_sWJC4ThVf0pWC7cpXWKc8wxHnRcADPN-YZiGZoK5E-O_bOVtRdNfsGLa3rVytI_Tn33BBEeUnTJMwTjQzSHUVx-zvsI4ra6XAFrXIEDuUKdW2zjPv8DuU0k9hpXZszsyB-RJphKENb76Gj3rhIFKUFCFZrCzweWeaMvtjQhAQNy3aqHCJT79odxIBF4BKewByiiUXPPfKpYJfXfGjBnCszaU4b__q77S50NMVmUqKeBg2z1sw8bGRdbKt4YEE6-TSg_7-xOHHzs9SVai98Z9jtqXUj_H7_MR0ZOiQx9K6rnFNiZj5DGWGAH5Y3rAn5XtYKI5UkH4cP5iMZLAkLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین سیمایی‌صراف وزیر علوم: چرا باید پول دانشگاه صرف روزنامه و خبرگزاری شود؟/ چرا عده‌ای مدام دانشگاه را می‌کوبند و باعث التهاب می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/689243" target="_blank">📅 15:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689242">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkZbAN-iUOe08-Fxn1-RoNfCFoPW-XxhYs0DNhwaoeJ6iGxumDULsmLtJTwoLVKvrg61bjPHbl4qfhF1gMEkuvLR0Hig62Nh08vPJZXDUsr5fOKpvHve0gOjg9eURxULOCpelHH-sklAqS5tb2JwB899cg6GCBpiYnieeDi9DAAReHSQdfiBnyg-Cy7nRmShtvfmm05MC69lSdKM2Wy_Uzi-WVthf2Cmm3yIbySjR5M-6C0tIM1dkdolW4Jvvfi_KHD_zNCyIrDCb2I0Z1wIxz1eqtAK1Uut_P3DSE44s7moYKlDCvH_ajyaM6S9j0ZJVPGv7-mDoBJQ_pWhu-Mbkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ در مورد حمله به خط لوله نفت عربستان: به احتمال زیاد ایران مسئول این حمله است    ترامپ:
🔹
جنگ ایران خیلی زود پایان خواهد یافت. جنگ ایران احتمالا پس از انتخابات میان‌دوره‌ای پایان خواهد یافت./ حوثی‌ها نمی‌خواهند با ما بجنگند‌‌. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/689242" target="_blank">📅 15:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689241">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde8b54263.mp4?token=uq0fzHFP9Olwk-tVoQLqOsq2J-YMFcYX6sFgE4Ufe8He06K1L9BEiULcifIu8MFumOScG3o2mVA5XZEI9VphgmgZvlsFbiC0olYod3llriO_O_vy8yee4cvg4ZCWpgrUmhv6t18nUKqQj_tFM4s3jHA6n5AlK4cIgMIcbqO52GuH1HRnLutx1C1xmpMCmq6J_py0ZU7qy-8mN1qZrCm5Ou_yRDVGw528Oh4MvCRsHQX7pQh70Jb8i1ej1u9Qh_P0vR9KF3O_JLasxjFYBXPaa88zjjPSIyQ8W46pdFsN2NHbfA9uq53-r3bmjqBMU-zoZfMjSASo2lRXNJ_Ct526Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde8b54263.mp4?token=uq0fzHFP9Olwk-tVoQLqOsq2J-YMFcYX6sFgE4Ufe8He06K1L9BEiULcifIu8MFumOScG3o2mVA5XZEI9VphgmgZvlsFbiC0olYod3llriO_O_vy8yee4cvg4ZCWpgrUmhv6t18nUKqQj_tFM4s3jHA6n5AlK4cIgMIcbqO52GuH1HRnLutx1C1xmpMCmq6J_py0ZU7qy-8mN1qZrCm5Ou_yRDVGw528Oh4MvCRsHQX7pQh70Jb8i1ej1u9Qh_P0vR9KF3O_JLasxjFYBXPaa88zjjPSIyQ8W46pdFsN2NHbfA9uq53-r3bmjqBMU-zoZfMjSASo2lRXNJ_Ct526Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر مدل ماکارونی کاربرد خاص ‌خودش رو داره که برای یک مدل غذا ساخته‌شده #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/689241" target="_blank">📅 15:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689240">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: ما تنگه هرمز را به‌طور بسیار قدرتمندانه کنترل می‌کنیم؛ هیچ‌کس شاهد وقوع این اتفاق نبود
🔹
ما به‌طور متوسط روزانه ۲۵ قایق را از بین می‌بریم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/689240" target="_blank">📅 14:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689239">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e03c587a6d.mp4?token=E8aN_Z5GN7OcG41Z9hfqxA-yJ9Afk_g1PeVxHWniZHIl7ukxZFIKdXOVXyby7SphQt9UFynB4suz2LwR53Be8k_bYmPWryWFLoMbr4Ei553GGY5IQSzV6OibxonwnIcH6Qj6FQc1OkoY-s0cJbwE747juq2dzpAS708eHUxB8kclAX_vWa_YzWe_qzSzwm5NDhsTFk5x93rG7xzUmwFZEpTD7Ciq1KWsKguiENUWt0n8IE_euWYJCr15MVLLCLcTlQwVBWcplLoyLUnKFKERHCK76_lRSUnzcnFhB6ABfTmhcAa7knVVRi9B_WV26gK5OkywN9P3UAprdH1lGFr_zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e03c587a6d.mp4?token=E8aN_Z5GN7OcG41Z9hfqxA-yJ9Afk_g1PeVxHWniZHIl7ukxZFIKdXOVXyby7SphQt9UFynB4suz2LwR53Be8k_bYmPWryWFLoMbr4Ei553GGY5IQSzV6OibxonwnIcH6Qj6FQc1OkoY-s0cJbwE747juq2dzpAS708eHUxB8kclAX_vWa_YzWe_qzSzwm5NDhsTFk5x93rG7xzUmwFZEpTD7Ciq1KWsKguiENUWt0n8IE_euWYJCr15MVLLCLcTlQwVBWcplLoyLUnKFKERHCK76_lRSUnzcnFhB6ABfTmhcAa7knVVRi9B_WV26gK5OkywN9P3UAprdH1lGFr_zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر قوز گردن، کمر و یا کمردرد دارید، این حرکات را انجام دهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/689239" target="_blank">📅 14:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689231">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvNrLI1k4GHHGg1bA2u3RqvVHiYHA9GxA5d-Tr7VKiw65uxDwV4CGUJYd7uX8LzfjQ2Icbzx74R6sdlp6FdQWWkkJjMZRQ3Y9H40w9p3wmNm3YYRdAnji2B1CLm4h1tBQ6wJkL2eAUwjFsWBXovqKzLwyZUKO3OrVbMsJbAOEnYnm6EIDzZUGR90KIReRZQfAj5aYkWEMV-5TytTg44hEP4eKYCv_eBB0w9PNOEN7f1rd115RdxNNifGpNHptxBOKAr976OKNgHKpo6nowHZBXLGiCUBtDEQta-MkmhjQZSjW4Bbsrox1r11KTT1xukSG7O9ornvXNPcxwJ1rgTvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGM2062NcRWKbiXnAtlITmVYTEhuYKbXHRcjVZUXG3uOAqZLf95-gqzoJZqvFqIFUKkygjOiSPg-ynCD39oRRpD8HbCPIopp0WqtGqWc5TrsXl66aC2f3fXn56bgzkWW1b1yq1QW0ewiXri_vfpS50z90YLemiNvNHhUwKmLli240gVhwMBJE8yLstxlvaJ_J7E1b1SCe1a4bEfsh4iQZIM9fFU4_5Yty2BEvdksYyxrO6sfRDDRjaC1B18cGRHNxTiJ1Q0KzrjpsAy9XBqPxQOYSYw27ncKuASvWXnPgZBHZI041atWDv3d0TMtlmrhFQHJjoQatfXmBKd3Tsz37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAn65miqJirCWjDamfYdpAcB0Xqa52R4AxkysvZh6HSeQbmJlJ9s8UKsMIzdDbYMEVk9-0y0Ac8Ba0GLPUzoyq1ZrrQclbtCK_uH4S3ATWUetX_u3qLXrKXoZ9IkImw4gOejHJpBblaVwvMnnCMYbnSzqDS0UPTmopkxAStbk_uxz28Zit0TTmkvuID2kqubVQorQAtqja80I5lKUYFEpCfQJ1zqPB3la-Zglmq9y7rXaQHpeDtgN33tSpN_ugmoX-QQS1zz8nJfX9QwSTsvSnJM1f-nFI3oy0LzbxWcyzDtSOWu8-v42F0XZsHxucP-77929Vf4fTzeEHa6rNrIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfC2HbsBV4CdcxjBkDRwlj4EOCe8pgBfffMC1pCjamXu_sNVhuV-IvmLcKLFr6CNcgxlPHHIYHGQOJobKuhu3zvxVA3qRk9YMUr32Fuq1hpaqqYUJ45sAW9GndL7D0OApulcqL2Q-wal4pEI4a_EA81im7jF07vWVPrScXDu_oLfu07Wymu2HfmA6WYEJh38up0o665kB8KXBgD0y2Crag1QKkjbSGdaM9Wt175pM-RRwV9HVY5lnxagtIH478yDTNwIn06NtVOCb3JaIZ0rFSQ3f_N94aHIN0fXpmHMeI2ENLnydZrqPfq0BOagnO6N-kTrC6AzO12NvMk8SVy4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXENHTgriuR48g_DiRG79VWR3adnc7THvAnu7jJAadhjC6LjWMDomx90EIMrzItta68oC7iDGDwSuTmaMQ-PEvY8Xmng2mL151cQry0qn3jDdPXeOqyWf9xRiVSeMZ1qWYelNqb6m8XTtHCgBaZKnXfSOckwYVPvIqI1cQE9f3uh_uZYPwFnzFDn2jjVlR1_XZY008vdfmna8_90fx8awJCbQaR6JwtN0Yjvpk13BMhYf4tdHowzYcPo-NwcUqBiqySsdvxLK0bHCl3rx5GJnN3r6sts9QvrRDPUMadK4h7My44R8rwIrZBtMdMe2MNW_bVpatF7O4v-9IK8nWY-Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQfL5UvJvdqBpSFp34UKvCCRr-Oc6cNk_QeyHRzLn_7X8fbN40GGXtvq79OeMc5BhMn78O-Cuxb9tn8eNbJFfLdbsuVD9Wti2gEb0bI3tziYRU3yB5CoC8whga7qdIB0BNrJqPdzqKtMc7Z3mbhlHbyZZ8MDpo5utxG-sG5boICSRMtkGpeJd3mdD4GQO-g9t1RYytaP-rX1i-0NuRVTBKwSuU33DZ0MYDxQrhbNA76clR9Cnpc5sP3BygYqNRZ7ryLwGLMpJrKHfc3WR2AWvkRrQdTM_qrUuYPBzdZGmCJVa8NbUcHr2mpECbP5MAinhu5W8JtHJvgDz9qQQdooLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XV7LOOUuHkyZOYgoJIUPDWsJJAkBUOGkPf4NFXjmnQ1Gr2D5ug2YDwy-yQy45jozm-x0CqqeN_1se3D2fSR0RyS7JrVziIVWp0MnwGDMJN5GdxaVKciA_Aj8LL45dIV79uI6l5fJ0EAT86a6AIIauaUunexfI52lihPJPVCGu_3p_DEW9zBzw9riL7BQAIIapV0PPgTT1-XyO0x2I7cbpPNM-Zlrj-1LOONJgBHacG_YZ9I1G6g2cWf3Bt6F-5e3I5AkvmoOrf-u2Bx-FyI9obDTwl_8cffVlQ-4VKPAUyt0oYEJe-R7w2snzBWpSwFTQ-t60QiuBzeMV0CLWM6jyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZyJMNoiCpYUNB9PKS7JAyX2oFjs22_g-PDnWH0Tw4aE7xIdbjj7CfmYto9KuU8iUTHag47aZsXH8TOsKIiFQ4dqUCvQyblXg3xXslnX-x2igCv8GrqJHVv3fdzB_OaMx7xZABigAu4aWHG60H16aV_udiXBk3Olkd2q2B8LnRfqcTzGenpZqTbHt8ljXneR9DNGlbIB2cG9Aniq4vf34lKBvXi1IFUj7Qv-G2HQuAdjKFTdjZy6vtSFPwXQFbkRE2flpN1qS4WNwmt0_S8Yqtl52oHp780k3GlExQycOIMNMXPJx_mKj0A0d93GBDdAkbrSjT2FkdyCm3NUlOy6F1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت اثرِ یک همراهی
💫
✨
هر همراهی، وقتی به نیت خیر گره می‌خورد، می‌تواند اثری ماندگار بر جای بگذارد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این اثر را ماندگار می‌کند.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/689231" target="_blank">📅 14:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689230">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/689230" target="_blank">📅 14:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689229">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0NRQR_wVV_6-RS_Ky4rFvC5aIhOyQk7JBFpIOkcqXPShvCcl2uD97wE8Py9zpJdRHDTKXq_B-BpVEssHCGHVSHySw7PbjgiqmihZIkueLn1_0TcRgSfLOi9fODejIlNFliUql78cVDZj1CrFV5_oEQpxQU5TLbUO7FO9pB5HOxtI4ZYORC1OeX3aMxk3mwp1EesXzyq0UICLmfX_ueqagcdBWO2HoGaVSGinPtNpxixf7X1eMwKJEtPfigiTHFBa4rIO3Xz0td-CCK-j26WRNdcGofo6i0-B7SMFvildfKE8H4ZXXZNcveI-KO4q4yPrxDWDDBeEYJUBXX6k0PsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمایت و همراهی مدیران وزارت نفت با شریعتمداری مدیرعامل هلدینگ خلیج فارس
🔹
اطلاعات رسیده به میز نفت از همراهی پنهانی تعدادی محدود از مدیران شرکت ملی نفت و زیرمجموعه‌های وزارت نفت با جبهه محمد شریعتمداری حکایت دارد؛ مدیرانی که در ظاهر کنار محسن پاک‌نژاد ایستاده‌اند، اما در پشت صحنه روی شکست وزیر نفت شرط بسته‌اند. انگیزه اصلی این همراهی، نه اختلاف کارشناسی، بلکه نگرانی از موج برکناری‌ها پس از تعیین تکلیف مناقشه هلدینگ خلیج فارس است.
🔹
همه این افراد به‌ دلیل حواشی، تصمیم‌های پرهزینه و عملکرد سؤال‌برانگیز، صندلی خود را در خطر می‌بینند و بقای شریعتمداری را سپری برای حفظ موقعیتشان تلقی می‌کنند. گزارش‌ها از تماس‌ها، انتقال اطلاعات و هماهنگی‌هایی حکایت دارد که جزئیات آن پس از تکمیل مستندات منتشر خواهد شد. میزنفت تأکید می‌کند سکوت فعلی به معنای بی‌اطلاعی نیست. مناقشه خلیج فارس سرانجام تمام می‌شود؛ اما پرونده مدیرانی باقی می‌ماند که برای نجات صندلی خود، وارد یک قمار پنهانی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/689229" target="_blank">📅 14:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689228">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI1tKCWsb31U2DMU8Z2dJI8p9QKAm9gTetogsE_esP6xgJ1zpkefsBk6QPARc8_u4czG-RSXhrapcil75cJIbrktAS0OfjX7HFlZrWMR4uei4YrFMSbZIcO9QI9dkDJVvsUMnGGX3JlPXldld7KLi0UZaH-yNXWoxQVVNvGKzMrzydHKH8lvMyW3yiYeIc4BHPNe5ltAfc4vfIRhfi7AM3dOJHOBU_mFJWhkE0zDlcl3PsXbXPBNZLvC-Dud2gTVGs6U5p2VdQXBF-Q8089Wsl_8IntfbrsQOTcPQrPgGh5eOdT1MTEj6tkW7bqotRCrDH7czTCxVOv8owPRCF83hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارین افیرز: جبهه دوم ایران پیشروی جسورانه حوثی‌ها، جنگ‌های غرب آسیا را دگرگون کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/689228" target="_blank">📅 14:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689227">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olx8dGSKx7rfFEN7hint_0rZpSLgtCOnI_CQX3vXfIXe6HfmVpEm0Ob9oQNTvRa0sDvb9gGbzn7EHQCyAYcteRS4rQFGYAiHJkuLLqLwj2OvjWmjQgEex6l_YKUClw3SB5UZ_KjX_Lp3Ix3JWBi8X51bWNCE_5fRxRZf99BOwR_KF0usi_R5P6qBJ_W9EwYTeDYYdO0Ho3FXLq4GZgI14-fExIbNfrAThWVX7dOgtMCSlf4RyM2ASSo-4JPPoGl4EaEcWGPulp8RNC3COy_i6bUmVyS2T9GFlYQpoiS7qFGvH4ohZuPy94AXju4ibCwQY_KpSsvd4HDdeqfwRxdKcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت ترامپ درباره امید مردم ایران
🔹
ترامپ توییتی زده‌بود که در آن ناخواسته به ترس آمریکا و رژیم صهیونیستی از امید مردم اشاره کرده‌بود. امیدی که با انکار هرگونه امکان بهبود، با بزرگ‌نمایی قدرت خود و کوچک‌نمایی طرف مقابل و با اختلاف‌افکنی و القای فروپاشی داخلی دنبال کشتن آن در جامعه ایران هستند. واقعیت این است که آن‌ها از امید، بیشتر از بمب می‌ترسند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/689227" target="_blank">📅 14:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689226">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
مقاومت عراق اتهام حمله به تاسیسات انرژی عربستان را رد کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/689226" target="_blank">📅 14:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689225">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHaMxrp1VMlQZQVW_klMi2xwzYkMa4KloSEBbc8XkQlXmWohq_6D_zUbXyu57Sb-31eFnKzfvv2gHPeaO_TBv5akYOjQo80TPCBg3vdz_3iyuwHn2KQB76zUsYKrj5d4TGlom1MoF0t2-VeFqnESlTb8O9fXb54mAo63qCFkUByNXpv1auUVQyzQV-ZUkyrauwSvdjxWXFvgIPhhvy8uHslfWhUJ4ESuvW-WQR_26AyWAetQI9xUvk2gNhAG13IYv6JkffDB0gZlwoLH9pPP6eq4oTYlBADtgJon0-MUp3q0Q7_vPGkqiiWsvtWApYyZ4Ga5y6FHVKix21pCdRJB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با گلدوزی می‌تونی خیلی راحت لباس‌های لکه‌دارت رو کاور کنی
🪷
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/689225" target="_blank">📅 14:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689224">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای ترامپ در مورد حمله به خط لوله نفت عربستان: به احتمال زیاد ایران مسئول این حمله است    ترامپ:
🔹
جنگ ایران خیلی زود پایان خواهد یافت. جنگ ایران احتمالا پس از انتخابات میان‌دوره‌ای پایان خواهد یافت./ حوثی‌ها نمی‌خواهند با ما بجنگند‌‌. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/689224" target="_blank">📅 13:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689222">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c005ed5d.mp4?token=ZZ7Sb2gAy5Us1jJXonOvhswOTIxpIGS95GskyScvkq2x1HUEEdI2jBZ3r08ihwiey2SI7nxzds6Srs9ckU-2-zxx_gp8ZVSyGA1mhv2W4K9gjLqYHv51-w5aV6TGOOcJDjsmot8nzsl85LVKDtN_g9hO6Tdp0V21152M23Sn-wfgAnk8qo-evp-Hn88k0NK7oleuG80uw07_nXszbg4rJN4JFJnaP20s7UFlKoMttsiyuEVuwrUZBuCLuIqCZOAjDSP33XKBu1siYvnRcqHNwZMpHr41tj2zc4orgYu2KAC1aaiZfYWO_cssrNfSibuh6CUb61eC19IG53RskZl91Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c005ed5d.mp4?token=ZZ7Sb2gAy5Us1jJXonOvhswOTIxpIGS95GskyScvkq2x1HUEEdI2jBZ3r08ihwiey2SI7nxzds6Srs9ckU-2-zxx_gp8ZVSyGA1mhv2W4K9gjLqYHv51-w5aV6TGOOcJDjsmot8nzsl85LVKDtN_g9hO6Tdp0V21152M23Sn-wfgAnk8qo-evp-Hn88k0NK7oleuG80uw07_nXszbg4rJN4JFJnaP20s7UFlKoMttsiyuEVuwrUZBuCLuIqCZOAjDSP33XKBu1siYvnRcqHNwZMpHr41tj2zc4orgYu2KAC1aaiZfYWO_cssrNfSibuh6CUb61eC19IG53RskZl91Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاربرد هررنگ چسب برق رو از زبان خودشون یاد بگیر
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/689222" target="_blank">📅 13:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689221">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
از ساعاتی پیش یک تیم تروریستی در بخشان سراوان توسط نیروهای قرارگاه قدس سپاه محاصره شده و رزمندگان در حال انهدام تیم می‌باشند
🔹
گزارش تکمیلی در بیانیه قرارگاه تا ساعاتی دیگر به اطلاع مردم شریف ایران خواهد رسید./ صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/689221" target="_blank">📅 13:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689220">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
عربستان حمله به خط لوله نفتی خود را تأیید کرد  وزارت انرژی عربستان:
🔹
خط لوله نفتی شرق به غرب این کشور در ریاض و مدینه منوره، روز پنجشنبه، هدف حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/689220" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689219">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ff2d89ba.mp4?token=c5sJdPTWkrPzE_lGzsnGhDEXaDs8ugRm91Y2ndpakFgTRwIsiomUzh3jLEoBcezM9zNIDtQJaKmp6SOS3cib4OTGkSNN75l-AlA9251ZH8TI5mxLsr28yFxFXj1zcJyPN8DsfTmCwAaSyaMPaW7jcgf5cNXCcqhBfybzvJ6CosQakHpCejZkiLmDn2mta4rNoPJpitCPigL6_W3ethkE3fzIoxcI53u4l-IVL7aLIwsqESYf4-Ar3yUosfsn88MdfDMiVkgXLtfxCz3mhRXlCnK63P_ofQ-g6Y_ea9wutRwqmWeMftNbIWsUiNuzDBMr89gHRrKEblAUfZvD5WxtQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ff2d89ba.mp4?token=c5sJdPTWkrPzE_lGzsnGhDEXaDs8ugRm91Y2ndpakFgTRwIsiomUzh3jLEoBcezM9zNIDtQJaKmp6SOS3cib4OTGkSNN75l-AlA9251ZH8TI5mxLsr28yFxFXj1zcJyPN8DsfTmCwAaSyaMPaW7jcgf5cNXCcqhBfybzvJ6CosQakHpCejZkiLmDn2mta4rNoPJpitCPigL6_W3ethkE3fzIoxcI53u4l-IVL7aLIwsqESYf4-Ar3yUosfsn88MdfDMiVkgXLtfxCz3mhRXlCnK63P_ofQ-g6Y_ea9wutRwqmWeMftNbIWsUiNuzDBMr89gHRrKEblAUfZvD5WxtQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در واکنش به تحولات مربوط به ایران مدعی شد: همه‌چیز خوب پیش خواهد رفت #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/689219" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689218">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crjI-UXVowTDn6eVA4e6gXixAOVXGtIe9L9j1lZ7Tvo7RyqOwX-AjFrW8Zb2z4yDWv68MbO9TxihB_mCdZb3YSqYbGr9GcvP1zJL8S47FzDjA4A27noFLYK1Sd1JNnHXCriObUXEO8zmMdeeUUrY8r7wYihbk6nt96iRSa74rWEkn3E0H_61kHMqyQNpPRkp_fFmw-69IRFe3Xgher-cbVI7ve9VdbyQXOQL-77xnzupHRyzI91ZN0EGk8tnUvfw9H1JE6Mg5QKYTiVQAg0UufxpM63xHNubKkJs5Or8wzqxTv-ej_xJR4iX5pm9l5gV4I6LAdlBz5uNHGyTddFTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشست مشترک فرماندهان ارتش و سپاه پاسداران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/689218" target="_blank">📅 13:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689216">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl8IQ5pUandFw4xsFrn8VEURuZmicFMdZAN0jRlxke_fLGkMfWM1UYEGnGUWwp04mH4c-75zT87rdw3fkLl7wQ4vPwMkwmB1TESO_mw0j044TnUim-O3y_o-Pa3khYzSFnnduvknoLy8jL5Ggp7D08l_7CXcMS7Ngu8cfDBnAsa76XQm22rMnug2utOpFUHE5uqA5Sx9MlXwK70IUslxaHBED-joFGhjzM1R-9rN3dyYK3I17sQ7niAwAXUgNhF7thBOZh3cJ7Cl_gRp3xUKM2dIpOWp7uGa3dU5AH6gn0dfpSsUbnS9bMAsmVk3BVPUdML0_2WiXFEY8qzm9KGs_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87e10581af.mp4?token=XFgnvmrt6-x6zakvMTcx-FKAKPIeQMCuWYhxLAcBROyshAzza92fEP53yvJEgpiH7HWMXVyEePsWkxgu7HqEoyDsknYGteWaqtuIfNYL6kzz2IeZ9Zkbzg0MTOcDxX9nXKfD901yif1UQUiXZLLjdRXYf0F4OTFxN9rNqoOZkiH8_v3m_an4D_pW7KlNXjeuMycFkO27KoHBz8Y6UGiH8AeiaKXHF35ctoMfd27_d6Q8QJ0qW6Dk_DQT1VxBMdwdmhg5TGgj7UGWiRMz6ALX3UAUVCX-7bdjFrOAQbQo9DmK1mAhVMW1n6RKjZZCWONuTgC3LSQMKsNKVoiuHxSHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87e10581af.mp4?token=XFgnvmrt6-x6zakvMTcx-FKAKPIeQMCuWYhxLAcBROyshAzza92fEP53yvJEgpiH7HWMXVyEePsWkxgu7HqEoyDsknYGteWaqtuIfNYL6kzz2IeZ9Zkbzg0MTOcDxX9nXKfD901yif1UQUiXZLLjdRXYf0F4OTFxN9rNqoOZkiH8_v3m_an4D_pW7KlNXjeuMycFkO27KoHBz8Y6UGiH8AeiaKXHF35ctoMfd27_d6Q8QJ0qW6Dk_DQT1VxBMdwdmhg5TGgj7UGWiRMz6ALX3UAUVCX-7bdjFrOAQbQo9DmK1mAhVMW1n6RKjZZCWONuTgC3LSQMKsNKVoiuHxSHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه سفارت ایران به سنتکام درباره تنگه هرمز
🔹
صفحه رسمی سفارت ایران در زیمبابوه با انتشار این ویدئو نوشت: «وضعیت سنتکام وقتی اتفاقات تنگه هرمز رو رصد می‌کنه!»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/689216" target="_blank">📅 13:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
مدیرعامل شرکت شهر فرودگاهی امام خمینی: تمامی پروازهای نجف و بغداد از سوی فرودگاه امام خمینی در حال انجام است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/689214" target="_blank">📅 13:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689212">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2dheZCxPWAE55bXgD4adi5MJ_2ykiqM9GoR8AlPxh4hhtEz2FRzeZWGCkDXAgrV2KGd60eX4VVHiiq8apip70zLaQhQY17lWggwFBmRB4h8DCDwnQ9nylEsd0J22_3t4O-t28vroRukH34aHHwb2jj9KW5N_DiYXIO6fCpwlthl9AsEx1D80OWmA_7fst3ivnwfNXh1FN0EcurVARg0Y3e05TnJASwBcpU3a7eDXf9O5EanyRjZeCKwWAoQ0il3nTrNfeS2oaal9R9gq7CYqJlPEQgTVkQcf5GyWAckOL3cV4MFmz-XmZc2WrRznJQfml6e_-kqZvpEvLlfo8I54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_خودرو
| قیمت روز خودرو های بازار کشور؛ امروز ۲۱ شهریور ۱۴۰۵
🔹
بازار خودرو امروز در امتداد موج صعودی هفته‌های گذشته بازگشایی شد و بخش عمده‌ای از مدل‌ها همچنان با افزایش قیمت همراه شدند.
🔹
بررسی روند معاملات گویای آن است که بازار خودرو طی یک ماه اخیر، سنگین‌ترین دوره جهش قیمتی خود در سال جاری را ثبت کرده و شکاف قیمت‌ها با نرخ‌های پیشین به شکل چشمگیری عمیق‌تر شده است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/689212" target="_blank">📅 12:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689211">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85b001aeb.mp4?token=X5PCRBrCaQH4cZk35bkqfDZfT0Da7xQQGmkyu339ifu7ZlufQylW6BnU6_n3IbAXmW-0F442XJ6oCx0q3oYQxyIySANLygR2MdX3x9gkuHA9zKb_3xMU_k9Dtj-0eDS-u5SSorMgPHT8x1ZhCNgw_TZKtLC-stY0d0tOJXx4TSWNfNwpB0alQtbmECIXixjiz4wiqyw0wvRaFwyz2GOSjPed2wJd64j00XbjWFCLFFdYZEkNa1dOdjGF4_a4k1jVvEQ8PIanW07ZOFg75gQltP4C1s6G_ZyJrhOrMhgGVirpDlU9CpQjN3hnt_lUeToXK5Or27O-yPXKJucQ8VvfMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85b001aeb.mp4?token=X5PCRBrCaQH4cZk35bkqfDZfT0Da7xQQGmkyu339ifu7ZlufQylW6BnU6_n3IbAXmW-0F442XJ6oCx0q3oYQxyIySANLygR2MdX3x9gkuHA9zKb_3xMU_k9Dtj-0eDS-u5SSorMgPHT8x1ZhCNgw_TZKtLC-stY0d0tOJXx4TSWNfNwpB0alQtbmECIXixjiz4wiqyw0wvRaFwyz2GOSjPed2wJd64j00XbjWFCLFFdYZEkNa1dOdjGF4_a4k1jVvEQ8PIanW07ZOFg75gQltP4C1s6G_ZyJrhOrMhgGVirpDlU9CpQjN3hnt_lUeToXK5Or27O-yPXKJucQ8VvfMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در واکنش به تحولات مربوط به ایران مدعی شد: همه‌چیز خوب پیش خواهد رفت
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/689211" target="_blank">📅 12:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689210">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729f8f860a.mp4?token=HgF3C4PdTYRQZ6VdTmILccsSadsMbkNPDERoee9UtI7_a6zaPvfj0iscu2MSgsyxLcI95keszv9lnLvezXRbth05GHSRHSkHGdGHKqYlkAHoAcN29J_HtQDSj_GT5r5bQwQ1GCSSBZZXpx9kN-Z6tHx3W5VVHJ7-7586HIS2DyuchFgNs0izwqAFdiCdRLFF64LuhNoDKNg4v4Xp6QuRRAFfRlhYclxYJWAIn1ybNzs2LWiCabbILLM4xiGXAeqnyB3qcS_kdFgXjnvEnEdo03hkIt12kj39Po4nn9y8NqieHDjyImpEpEHUXk1T0sGp6AujTAvvYdJwRCT4oxvWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729f8f860a.mp4?token=HgF3C4PdTYRQZ6VdTmILccsSadsMbkNPDERoee9UtI7_a6zaPvfj0iscu2MSgsyxLcI95keszv9lnLvezXRbth05GHSRHSkHGdGHKqYlkAHoAcN29J_HtQDSj_GT5r5bQwQ1GCSSBZZXpx9kN-Z6tHx3W5VVHJ7-7586HIS2DyuchFgNs0izwqAFdiCdRLFF64LuhNoDKNg4v4Xp6QuRRAFfRlhYclxYJWAIn1ybNzs2LWiCabbILLM4xiGXAeqnyB3qcS_kdFgXjnvEnEdo03hkIt12kj39Po4nn9y8NqieHDjyImpEpEHUXk1T0sGp6AujTAvvYdJwRCT4oxvWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/689210" target="_blank">📅 12:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689208">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1985c52952.mp4?token=RyFQx_dcziI07EXs43mCydzX0DDsLEXLWK6j4MU04Tnihvi1AVL9ayUNh5bUAIFB5vrYyO1GwrOoqzxE41Yf1oZyPUgNLSjEbWg5WyQbTNqFytVGyF6ZyhBllud9_bWg9ml7j_-kkgBw9Pr2ufXF1XuSvhCsKETTqCtFB37oX-rYiXw78tRTttJnhUNu_uC25cN3ujQ7Wt4CuNG7dCtEHXRODGfONHo68UOiksd_xMDDanlXiPSDNZJg2FE0gNz6LMBKl0jXQ_ZqUgWnZrteVgl2QxGGIbD4YIluC1o8lQcHJg09_mBza4-A4h3XxiyO1X0AsNQLqu7BuSYUu736Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1985c52952.mp4?token=RyFQx_dcziI07EXs43mCydzX0DDsLEXLWK6j4MU04Tnihvi1AVL9ayUNh5bUAIFB5vrYyO1GwrOoqzxE41Yf1oZyPUgNLSjEbWg5WyQbTNqFytVGyF6ZyhBllud9_bWg9ml7j_-kkgBw9Pr2ufXF1XuSvhCsKETTqCtFB37oX-rYiXw78tRTttJnhUNu_uC25cN3ujQ7Wt4CuNG7dCtEHXRODGfONHo68UOiksd_xMDDanlXiPSDNZJg2FE0gNz6LMBKl0jXQ_ZqUgWnZrteVgl2QxGGIbD4YIluC1o8lQcHJg09_mBza4-A4h3XxiyO1X0AsNQLqu7BuSYUu736Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند جالب برای رفع بوی بد و عرق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/689208" target="_blank">📅 12:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689207">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ekl9WI08H2kq2Sgq7gs90o5oZjxs5a3r5EyOL15uzddts4_s66mRwN9kEcyXukmwzqUzn49RBNZaj-Gqf3UvjeH---qmlpg-v-Dmngqd0DVs3iGBZejkCrKGMs_qArswujzaPbA7wy301BdfXywbP5FMDhAZnBxLqvJ3x-zkEX1APGVjhdbW_WBgfChgDOPwNwM8dZKR6-ER5Q1Az8sG5AVM979L_GU-MbiWHSeOoX-UcWhfB0RbARt_1mmDwWlIzbgK_qynQuP2MohoLDyU2RTrVQQzsAJt3_oj-m5U4qpq7xourlG6gozvUbYBb_NITKZSkpdjNGf8fp1jNypLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرسنگی به‌ عنوان سلاح در محاصره پاریس/ چرا ترامپ نمی‌تواند تاریخ را تکرار کند؟
🔹
امروز ترامپ سعی می‌کند از طریق روش محاصره، مردم ایران را به جان هم بیندازد اما این روش توسط او ایجاد نشده بلکه محصول یک روند تاریخی است که ریشه در حوادث مختلف دارد. یکی از محاصرات تاریخی که احتمالا ترامپ را به سمت این اقدام خبیثانه هدایت کرده، محاصره پاریس در سالهای ۱۸۷۰ و ۱۸۷۱ است.
گزارش تاریخی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3244515</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/689207" target="_blank">📅 12:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689206">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
تکذیب تعطیلی مرز مهران  ‌فرماندار مهران:
🔹
مرز مهران باز است و فعالیت‌های مسافری و گمرکی در این مرز برقرار است و هیچ‌گونه تعطیلی یا توقفی در روند فعالیت مرز با کشور عراق وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/689206" target="_blank">📅 12:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689205">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6bd17689d.mp4?token=q5SQTtl6GNCzOToIb7SEMn3DbFhpJylVeG-slvJ9P2Xk3pl2kzGuAKhFbXRN0q1cAW62Ju3NPuyagpT20x_RMV-rK7te12PZzA9nCIxc-BJoexYZTFyzrmOI6OZaEdla9jSM_KWAvURvxgiJjg11k6SgBPcz1XsU5-8Tphod2Sj2vT3fR22C5674pjNuKUfWcRrKWuXw2PVqrHcncxXQ9d0xT55rIu68NigNU2AWHkHQ61ltQ5M_PJHg6Eyz3QGKhTNYR59Yd_pdFwZOtyt8NAvNQ20N8dUmoQ1A6ZKdlBiDYKYNDX54wSr5RvoyWXsMDLMUpJpzkRSB7PLMjhtEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6bd17689d.mp4?token=q5SQTtl6GNCzOToIb7SEMn3DbFhpJylVeG-slvJ9P2Xk3pl2kzGuAKhFbXRN0q1cAW62Ju3NPuyagpT20x_RMV-rK7te12PZzA9nCIxc-BJoexYZTFyzrmOI6OZaEdla9jSM_KWAvURvxgiJjg11k6SgBPcz1XsU5-8Tphod2Sj2vT3fR22C5674pjNuKUfWcRrKWuXw2PVqrHcncxXQ9d0xT55rIu68NigNU2AWHkHQ61ltQ5M_PJHg6Eyz3QGKhTNYR59Yd_pdFwZOtyt8NAvNQ20N8dUmoQ1A6ZKdlBiDYKYNDX54wSr5RvoyWXsMDLMUpJpzkRSB7PLMjhtEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: موشک از خاک یک کشور حاشیه جنوبی خلیج‌فارس به لامرد شلیک شده/ ایرانیان برای همیشه این مسئله را مطالبه خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/689205" target="_blank">📅 12:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689204">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/689204" target="_blank">📅 12:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689203">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ee7cc5f4.mp4?token=QvmDBCm8pKT2dYIcigfTdB9DYrtoF-9b1QnoLPNy_Qnw8AtWJqw2PAakPDI4vtqMiAXyemeHNv4CCWUcyrcvLP8pfBJVlG1ip2J1GlSN5rr9ztW4DI3nFABU1jOdaxBsLLiL0-9zK-IRTO351zWWBiUnCWZN4dSoUQOV71Vez8LbZNgPEaxRripVFf9H-HiC_DaNEeQxZ5kP4KpaKtX0Xp3w4t4oVbHGtAj1uJHq92AGxoWOmGWCC8X24a6ANn83jdWYhtXOMHJyBJ7PZaVdqwbLmEoJZ1TygSL3Mg9HsvpjhOZ-gWSeXOt7udZVJgfoaYEhG8SH5NuQlzh4YH5xiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ee7cc5f4.mp4?token=QvmDBCm8pKT2dYIcigfTdB9DYrtoF-9b1QnoLPNy_Qnw8AtWJqw2PAakPDI4vtqMiAXyemeHNv4CCWUcyrcvLP8pfBJVlG1ip2J1GlSN5rr9ztW4DI3nFABU1jOdaxBsLLiL0-9zK-IRTO351zWWBiUnCWZN4dSoUQOV71Vez8LbZNgPEaxRripVFf9H-HiC_DaNEeQxZ5kP4KpaKtX0Xp3w4t4oVbHGtAj1uJHq92AGxoWOmGWCC8X24a6ANn83jdWYhtXOMHJyBJ7PZaVdqwbLmEoJZ1TygSL3Mg9HsvpjhOZ-gWSeXOt7udZVJgfoaYEhG8SH5NuQlzh4YH5xiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد حاجی‌پور، ملی‌پوش والیبال ایران با تماشاگران برای نجات توپ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/689203" target="_blank">📅 12:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689202">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6242363ef5.mp4?token=of103OhIAT7nc1LRVEhbjTALxtWPZV6fp65Iw_AN7vt8G1L3xvJ9Xcpt0TDt8ml62AJVvbAsE-TqgG2okITnsMYmlg6-_WiDf_vZFIMbYi11HYgQc8ifO6Skdm9NQgBW7sfdS1TxXMuau1AlUapMk48dHM9y4CBZHwfNaP-HBk8yiocLIbrnUs9WVgI6aZODJ3P-0eh6_CzhPsJ0cSSmKfUeTybcs7-ipekKckCYK5IO4PwfxmJfpZTUx-H6LhSaP_1Ueftjr6AfZD3czPvIsff1k4c511QeQaywoPnhIQs4WNGnj_yafZWltuij2-9bTdC3-73wfvULencLDx3m7W10p6T-Iv4eO0h-tC3J4MLU7_-m5JTMQgJF-zKJyEPZQFfdPlC-KovEmsIJWXlXRqe5ntgyPP9u2mkFUCM7NIX_6o3EEmwbVY41VwG-chDs4pUwCUV597riwJ6oYKrMgrylOc_CgREfqMLYrsJqpSP-FKYUIQuDZvcWnR7Rnr_MnXEgkg29Fbu96XExRSTGI8T8wIsREsZdlYygRqILSxewX2f2j5ApNhJZyWnDIOjqkezak1E65lXUj9RuemL215VWDlTBEMPbOMS30PgjI8_snVaWhrewvxI7xJdr6S-MSZVcsj7D2Vk1lqXo9dLvSypPohygcW9_tLGpVV_kOzE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6242363ef5.mp4?token=of103OhIAT7nc1LRVEhbjTALxtWPZV6fp65Iw_AN7vt8G1L3xvJ9Xcpt0TDt8ml62AJVvbAsE-TqgG2okITnsMYmlg6-_WiDf_vZFIMbYi11HYgQc8ifO6Skdm9NQgBW7sfdS1TxXMuau1AlUapMk48dHM9y4CBZHwfNaP-HBk8yiocLIbrnUs9WVgI6aZODJ3P-0eh6_CzhPsJ0cSSmKfUeTybcs7-ipekKckCYK5IO4PwfxmJfpZTUx-H6LhSaP_1Ueftjr6AfZD3czPvIsff1k4c511QeQaywoPnhIQs4WNGnj_yafZWltuij2-9bTdC3-73wfvULencLDx3m7W10p6T-Iv4eO0h-tC3J4MLU7_-m5JTMQgJF-zKJyEPZQFfdPlC-KovEmsIJWXlXRqe5ntgyPP9u2mkFUCM7NIX_6o3EEmwbVY41VwG-chDs4pUwCUV597riwJ6oYKrMgrylOc_CgREfqMLYrsJqpSP-FKYUIQuDZvcWnR7Rnr_MnXEgkg29Fbu96XExRSTGI8T8wIsREsZdlYygRqILSxewX2f2j5ApNhJZyWnDIOjqkezak1E65lXUj9RuemL215VWDlTBEMPbOMS30PgjI8_snVaWhrewvxI7xJdr6S-MSZVcsj7D2Vk1lqXo9dLvSypPohygcW9_tLGpVV_kOzE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور میشه که مردها با یک سرماخوردگی ساده احساس می‌کنند به آخر خط رسیدن #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/689202" target="_blank">📅 12:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689201">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسبدگردان آسمان(سبدگردان آسمان)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fC0CzgPV_hETBJAZ6EqIP-B8zNknlKhVAeWN1JGQ3dK7zbTrnEeHSze3wh8r5sUkSD_Owa8twRjaIGlrh2NmFrble_DiOSnDHxs6pUfRa1Eo_x4ckDA0YU5C6ETwzk02LyvurHNTerMs2PSAvySUsQdVL6oTqBYwMB5uCf0251STOkr4wXdORR9GeXJzoUdctMJ9xbHUULipmKasmRNE9a-b4tapia_zKJPQA7Ndv5Je4KKdqmi3pQIR_87tql1NMvgCh29AKt7xPsBxJfX1NIzBa_iiBRgPd3C4rRatKt8ej_RmqcAbI9b_pkBb2O2bUr9CZrx1b4x9YeuFrG75rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💯
۲،۷۷۰،۰۰۰ تومان سود ماهانه به ازای هر ۱۰۰ میلیون تومان
با صندوق درآمد ثابت
آسمان سهند
🎁
%۳۸ سود روزشمار، اول هر ماه!
✅
سود بیشتر از بانک
✅
واریز خودکار ماهانه
✅
بدون مالیات و جریمه برداشت
✅
محاسبه سود روزشمار بدون وقفه (حتی در تعطیلات)
✅
بیش از ۱۵ سال سابقه فعالیت
🔗
مشاوره رایگان
صندوق درآمد ثابت سهند
.....
سبدگردان آسمان
.....
☎️
مرکز تماس: ۰۲۱۴۱۷۹۳۰۰۰
🌐
وبسایت آسمان
📩
سبدگردان آسمان</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/689201" target="_blank">📅 12:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689200">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMyAlfSexQZpJhgT_YFB-gZD5wFE0ShajcCj08-WNdwZHiqM12D1If5-Njp3A_mzXDaiChjMxk0k4ImBS4l2PzgwiztrDQlwXBYRX32xvslNuXn-T01UI6spurpst6ZlnY2h8ndRxAy2OU8Ed6Dl-g2_iYD9UAamTQAoashdnfnmjOp1Z48RcB7jAYZLAjdzZzC28Zbo65_BX3-0wFGDqPqDzgwbD-G-YN6KbP4btygjJarY991eefWrsn1_5dsTvGeRv7s-hETp9v5myazo_mABSoi4KQINMR3Rdui7pjBGvcWeTdGYImb9-jsaIT0EOjATbgaZ_AhmLjIED4PiYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ ایران به فینال آسیا راه یافت
،
شاگردان پیاتزا کانگوروها را هم شکست دادند
🔹
ایران ۳ - ۱ استرالیا
🇮🇷
۲۵ | ۱۷ | ۲۵ | ۲۵
🇳🇿
۲۱ | ۲۵ | ۱۷ | ۲۲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/689200" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689198">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEv-Y2aRdfFybaabZ6RKb0EB3Vua7FEmyT5SUwRiGpqXPnK6h0PAnTiZzVe6KRW707m6R1LHkXVE_S4FrstzL0ntGnkj3Xb4Fc_WXq0z3A0R2kiwEMF9USqxKbMWbXGALRmej_hQ_rvFLiGVbGtIL2bEvOMzjIWjJmgk_NAf-WTrgg0MhTFd31HfF0KZV3IXQM-ph1MfpabVmTKM5Bq1akpnWOEZJRJmMxSr6fptfyx1cFA1lY1pWuRm4o1ZWxRsSFs-a9ibWtXeMBct7l1AXzKGLc4nBdeeNcBBLDTrrZlag24rYPD05xoMTWOBQeJQ17sM8Gdn8atJJgwbP8lPHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/689198" target="_blank">📅 11:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689197">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f56cd818.mp4?token=hqyoT7cPWVI5ow5y15NeNA-B2yDSe12V3VCDAIO9VHiQ6NkqTq5zSIEAYdAr6MJYcd98QxA5RYXM0gEk0yKU7DJy6MzfwM734K7lcUw8-NQdhkyVTVItLejfCxjdOgVp2yX3YPruZEqswIvwCRrxvOqLPOmbSnSLG1i6_s8EYEfXRdLQdNzpLxvud3bybr6dKp-HA-s-6cI3BtXoMt2aEourxr4xg6KQ7S-a0jwkHNGYx5QaTVWCtkNfcmqb9Vx3DHNWAcsPVNoq-gzO2SoLM1lQOOBN4zFaCCfR4lgMVOJYcrJcXM5BDHh9wGh5n_H3BTJysmp3nxlOQ7lkWSi_PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f56cd818.mp4?token=hqyoT7cPWVI5ow5y15NeNA-B2yDSe12V3VCDAIO9VHiQ6NkqTq5zSIEAYdAr6MJYcd98QxA5RYXM0gEk0yKU7DJy6MzfwM734K7lcUw8-NQdhkyVTVItLejfCxjdOgVp2yX3YPruZEqswIvwCRrxvOqLPOmbSnSLG1i6_s8EYEfXRdLQdNzpLxvud3bybr6dKp-HA-s-6cI3BtXoMt2aEourxr4xg6KQ7S-a0jwkHNGYx5QaTVWCtkNfcmqb9Vx3DHNWAcsPVNoq-gzO2SoLM1lQOOBN4zFaCCfR4lgMVOJYcrJcXM5BDHh9wGh5n_H3BTJysmp3nxlOQ7lkWSi_PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این
تصویر را خوب ببینید؛ نوجوانِ سیستان‌وبلوچستانی، ماکت پدافندی که خودش ساخته را به محفل ستاره‌ها آورده و از آرزوی بزرگش می‌گوید
🔹
«سربازان در گهواره‌ خمینی» بزرگ شدند؛ جنگیدند، درخشیدند، جان دادند، اما میدان را خالی نکردند.
🔹
«سربازان در گهواره‌ خامنه‌ای» تازه دارند بزرگ می‌شوند؛ با این نسل چه خواهید کرد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/689197" target="_blank">📅 11:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689196">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pY_DZYle8Jwqbob1GTenh4KurJr1psxJRufuXHsGAvHCIC1w_gOaAO-OElbiWdwduhKALHGZEWNbsBSp7tL-Yc8J880cCy3rat6KwKI5hFQccv18r3tFWXHhREckfg4pTLnvhRe4xzCp7SSujpRWi5Lgu3QvYu_z0tw1I44tj4iitCTphuc5dk7F__5mvostVnA8Jz7rC3WsMZoFjk2c5Q7s_sPeO21N9JtU264HJ2Rdcx28_bUeA3gAwDZnZ_64lcZQBR7kxGjwMWHdv3HbMMKWrmGN-P7qRqGPS0k4-cH7wJszl1pWyT2jWAxlmMtSa2NKLG9JwR--q_t-lZb0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕰
ساعت نگارگری پنج تن
ترکیبی از هنر ایرانی، هویت مذهبی و یک دکور متفاوت برای خانه یا محل کار.
✨
مشخصات:
▫️
قطر: ۳۶ سانتی‌متر
▫️
جنس: پلی‌وود
▫️
طراحی: نگارگری با مضمون پنج تن
💰
قیمت اصلی: ۲٬۱۹۸٬۰۰۰ تومان
🔥
قیمت ویژه: ۱٬۹۴۴٬۰۰۰ تومان
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/689196" target="_blank">📅 11:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689195">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb48de1ee6.mp4?token=Xfqe3ZyTtTYWK_GPrLRqDZvKFg7SDQ8k3p4H3dNmsoj7nFeDfsUA8MW9m7FnIQH2acQEybpIC7BJIwd3V75NRRlsFNzJJcAUdSpwYbp_3xani6nR5aR3sbLlXII58_AtmTeIMLBclDf7WuFWf2Hz0YIeENGg4uLey0uyr71uAvKFhIpb7k7yOlci54Z91N3pNtrWqgWuowDm9Fp3Xhhh4kz5kAn5AdoL5RD0n4w5Cz4HAxxPKv0AJj-tfc_ob7qVPVbpkInuU1x9Hj67DmJotJsjla_EzOppKAUjnsMLm5otBwcY_xFkf4Bjyx6Akr5H7Dv3gkGXNkiG-ATkrf8MSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb48de1ee6.mp4?token=Xfqe3ZyTtTYWK_GPrLRqDZvKFg7SDQ8k3p4H3dNmsoj7nFeDfsUA8MW9m7FnIQH2acQEybpIC7BJIwd3V75NRRlsFNzJJcAUdSpwYbp_3xani6nR5aR3sbLlXII58_AtmTeIMLBclDf7WuFWf2Hz0YIeENGg4uLey0uyr71uAvKFhIpb7k7yOlci54Z91N3pNtrWqgWuowDm9Fp3Xhhh4kz5kAn5AdoL5RD0n4w5Cz4HAxxPKv0AJj-tfc_ob7qVPVbpkInuU1x9Hj67DmJotJsjla_EzOppKAUjnsMLm5otBwcY_xFkf4Bjyx6Akr5H7Dv3gkGXNkiG-ATkrf8MSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«بنیاد شهید آیت‌الله رئیسی» از این بلاگر اقتصادی به‌ دلیل طرح ادعاهای کذب دربارهٔ رئیس‌جمهور شهید شکایت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/689195" target="_blank">📅 11:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689194">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ME8UTtPH3lyjta3_cAZfm0OUn8FHEfJvZ8_0pihTEQuxHMhLjmEH6FHFO7RPbujn8t7Cm7yjsJCtVHvRddWec7ypqBnm3LodcfC9vSOu7EkFKfBsNcs0bEi2E2zGG47yM6VMe_deVAoux5qkZcBT79g__uPdrklqnaJ90SbE86-rSCZVKHItDTYj4eIBumpNRl0bxOh5B9M8yMn3c5zhUqgMGU_2si_zuUdYVZp4_omxYsAbnyfMNg-b6Rz73NV_9K2Njz6miKJeXY20KzzVOXtbI7GVqMw8269Cq1mUKzHxvgTM2WfXyoDNdUQU7tO2cXG5S2zf-iS9dDD_JnYZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت کاربر یمنی: عربستان و امریکا دارن پیروزی‌های یمن رو نگاه میکنن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/689194" target="_blank">📅 11:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689193">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/X6tGck3fG8twv_7S6Y_t1RsCSqbizCv_-gdsPwl0DK3qr5m4mFJKYJD2coQoH7KSFD1AYyr7u6Rp0uTobQvdrRyS_eIFMtXOzL7BqdMjcdBgIp0TQc0206wm5DBb0r2UhQyCkGJVskDZiC__IfURVnb-VKJvyXn5xQNol-PMUb7U69K0FWCSM-EnUE91JhAIc54WKZRwVjPdOgqLJWCkDNXE4OM-QMGpYbd4tfrWjMcCrzvU3Dk4Iy-XuSXWR6nd5zfD9vG3KimdqsJchBnGqaMY-wOhDW2MAyR-gPSkNO4anKGgSs41bXI84RkVgcXEJzvXK3I7OpRKZqBXNHaFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس هیأت عامل ایمیدرو: نتایج بسیار خوب اکتشاف در معادن جدید چادرملو، سودآوری آینده را تضمین می‌کند
محمدمسعود سمیعی‌نژاد معاون وزیر صمت و رئیس هیأت عامل ایمیدرو:
🔹
در چارچوب سیاست‌های ایمیدرو، چندین معدن جدید در اختیار چادرملو قرار گرفته تا این شرکت بتواند عملیات اکتشاف آنها را تکمیل کند و خوشبختانه به نتایج بسیار خوبی هم رسیده‌اند که آینده شرکت را می‌توانند برای سهامدارانشان تضمین کنند.
🔹
چادرملو یکی از شرکت‌های بزرگ و مهم زنجیره فولاد کشور است و مدیریت جدید این شرکت اقدامات خوبی در فعال‌سازی معادن کوچک و تأمین مواد اولیه از این معادن شروع کرده است.
🔹
چادرملو با توسعه معادن جدید و برداشت سنگ آهن از چالش اتمام ذخایر عبور می‌کند.
🔹
چادرملو، معادن کوچک را وارد مدار تولید کرده و در کنار آن، موضوع اشتغال را در این بخش مدیریت کرده و می‌بینیم که سال گذشته رشد تولید و سودآوری داشته‎ است./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/689193" target="_blank">📅 11:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689191">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
وزیر نیرو: ممکن است بارش‌های سهمگین داشته باشیم/ همه آماده باشند؛ نباید غافلگیر شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/689191" target="_blank">📅 11:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689189">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/689189" target="_blank">📅 11:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689187">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمدیریت دارایی گندم</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgNVLIQHu5HoSsxNhdzw3GAs6AL_oVI1TxjeQfD0EWYoSBAadj6hib_APMGC2unU2F-Ww-ly3yBRfGE--2NvWi7XcSGsinemjLKjz_9AW6s_FgPuHGz0fyh_1vK2b1Wzaq_1riazFOcSzlo_tFbpp0pYrdzh5XKpP7HZfw0-q26V2JuuIXLm2nCtbmViJN1bnJKsGC9SGJE5FEWGSelw1smWO9ok32Xj3QHAZo8wEDXXDHtR_C4IASuFKOxdFLxhmC-zVtN7NvKeSHfNv_2kT7oyKOcp1OMH0IbmMESnPsvkapROsv9TrYAxsAGtVf6IJGEhAXuDimPUNBXWCo3RvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبد سرمایه‌گذاری خوب، لزوماً سبدی با ترکیب ثابت نیست
😇
در سبد ثروت، وزن سهام، طلا و صندوق‌های درآمد ثابت متناسب با شرایط بازار تغییر می‌کند و ترکیب سبد به‌صورت اختصاصی مدیریت می‌شود.
🔵
۳۰۵٪ بازدهی از ابتدای دوره
🔵
حدود ۱۷۰٪ تورم در همین بازه
✅
سبدگردانی اختصاصی
✅
مناسب سرمایه‌های بالای ۵ میلیارد تومان
✅
قرارداد یک ‌ساله
✅
امکان دریافت اعتبار از کارگزاری
✅
مشاهده روزانه وضعیت سبد
✅
ارتباط مستقیم با مدیر سبد
🔗
هماهنگی جلسه مشاوره اختصاصی
🔤
پشتیبانی:
@gandom_mediaa
☎️
شماره تماس: 02192003330
🌾
نقشه راه سودآوری با گندم:
@GandomFinance</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/689187" target="_blank">📅 11:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689186">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_0sBBmzzernaqWOYI1vRpK6P4h5V3vAZHxFJRjTavMEKsrOVNmsixXkEZbe_iZk8tERj-2YLbyDRd-YF2UWfpN6vSkAMw23Y01fyz5ImqLesO5TWdo2dxeUmTX42Oe-1prrGGQJ3VQj-h8_yY9kwAQtrsW_HaxT5Z5jf4brgzMjMozSGM9De7GYYMQUImt75EEhAAyLO07YTjOP2AcAR0Tguhv2nWqT9SwNHIBA_v55ijnAqdwfSJiqo3jxZ2rBzB4TGcX9Iui4lEMTFKuQ18WSBVRQPnmpt8Drj4d96Nd-KlgygwzAFCYUShq_CbSOhpagXK81PrspBQ72imnnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر پاکستانی: من پاکستانی‌ام و در کنار یمن می‌ایستم/ لعنت به سعودی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/689186" target="_blank">📅 10:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689185">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سایت عبری والا: افسران ذخیره اسرائیلی خواستار گسترش عملیات در داخل سوریه شده‌اند و برخی از آن‌ها ایده اشغال دمشق را مطرح می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/689185" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689183">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7e1db5944.mp4?token=AU6sYkai7dMuZmEZI_6JnAIX8I363hia8frfygj65v3eqvjhQmKqX4Y0SGQce8kEg0O8MX4zTSWiM982cGZ5uYh310faKdwxcbvmyTGRcd9HhN7Y4jhrqABh3uyepb3Ia3Zqy24Vo2KAw9ixbjDWHTwGFXr4otpQsfvwQv8-VexWV6S9ySNgSyImIoxzaIF3OwqXQjRW1rdAazXQulQy1bK6lp1xQbKp41JSVxpN3A8J9sEw5lObUKLh6dN3tGkJxxiN6HU5FZejZUZBRrgluULYkTpSPEIR6sKMHGIOFj4GPO0iiRUBS_LZXewx2YlLprkhOS55Zg6JY654tszyLIfeB77ZKOxBSp1_jjDPT9VXAZTpVmDXuviy4tin4fr02MPBBRcjRl9lp_lsNsezqYSiOrb2Qfydi5G7IBSkKD_lad-4ksJc4D8MCRzA0wsDRKXNAPw4FeY78DX8LC7MIE4jnZS2PYVbBj_JSNVclKnDxueXyZ-LDmjazj9llD9T3qDKtA5ZH_gRtHwtXFjJze8b6XKDRbJ6sSOCfdcQakgf5z4C3jLNziRwuoBk6B4sK01Zv1ELJ-T3Cnepnxu-D_-B0mzpU6p-Y3L1nGDLlNF4lY12FqBn22kEdNf2FMzkJBb9xsaCKtnrEemCTsHyTar1iNl3W63h5GuLrRK4znw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7e1db5944.mp4?token=AU6sYkai7dMuZmEZI_6JnAIX8I363hia8frfygj65v3eqvjhQmKqX4Y0SGQce8kEg0O8MX4zTSWiM982cGZ5uYh310faKdwxcbvmyTGRcd9HhN7Y4jhrqABh3uyepb3Ia3Zqy24Vo2KAw9ixbjDWHTwGFXr4otpQsfvwQv8-VexWV6S9ySNgSyImIoxzaIF3OwqXQjRW1rdAazXQulQy1bK6lp1xQbKp41JSVxpN3A8J9sEw5lObUKLh6dN3tGkJxxiN6HU5FZejZUZBRrgluULYkTpSPEIR6sKMHGIOFj4GPO0iiRUBS_LZXewx2YlLprkhOS55Zg6JY654tszyLIfeB77ZKOxBSp1_jjDPT9VXAZTpVmDXuviy4tin4fr02MPBBRcjRl9lp_lsNsezqYSiOrb2Qfydi5G7IBSkKD_lad-4ksJc4D8MCRzA0wsDRKXNAPw4FeY78DX8LC7MIE4jnZS2PYVbBj_JSNVclKnDxueXyZ-LDmjazj9llD9T3qDKtA5ZH_gRtHwtXFjJze8b6XKDRbJ6sSOCfdcQakgf5z4C3jLNziRwuoBk6B4sK01Zv1ELJ-T3Cnepnxu-D_-B0mzpU6p-Y3L1nGDLlNF4lY12FqBn22kEdNf2FMzkJBb9xsaCKtnrEemCTsHyTar1iNl3W63h5GuLrRK4znw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از یک رستوران و پرزنت غذاهای لاکچری این رستوران به یکی از مسئولین شرکت نفت که در فضای مجازی پربازدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/689183" target="_blank">📅 10:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689181">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
دستمزد ۱۹۰۲ درصد بالاتر رفت؛ تورم خوراکی ها ۳۷۴۵ درصد بود
/
دولت به افزایش حقوق کارگران در نیمه دوم سال تن می‌دهد؟
🔹
افزایش ۶۰ درصدی حداقل مزد در ابتدای سال‌جاری، قدمی برای جبران هزینه‌های تحمیل شده به معیشت خانوارهای کارگری بود؛ اما حالا آمارهای رسمی، فشار تورمی بر معیشت کارگران را تأیید می‌کند و طبق قرار قبلی، باید تمهیداتی برای افزایش دوباره دستمزد اندیشیده شود.
گزارشی در این‌باره را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3244607</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/689181" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689180">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای وزارت خارجه عربستان: خط لوله «شرق ـ غرب» در چندین حمله پهپادی که از عراق انجام شده، هدف قرار گرفت و این حملات به مصدومیت و جراحات انسانی منجر شد
🔹
عربستان تأکید می‌کند که حق خود برای اتخاذ تمامی اقدامات لازم و تضمین‌کننده حفاظت از حاکمیت، امنیت و…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/689180" target="_blank">📅 10:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689179">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
یک سال فعالیت در مسیر استاندارد و ارتقا کیفیت
🔹
استاندارد، فقط یک مهر روی محصول نیست؛ از تدوین و اجرای استانداردها تا ارزیابی انطباق، تأیید صلاحیت و نظارت بر بازار، بخش مهمی از کیفیت و اعتماد عمومی را رقم می‌زند.
🔹
اداره ‌کل استاندارد خراسان رضوی در یک سال گذشته، در مسیر ارتقای کیفیت و حمایت از حقوق مصرف‌کنندگان، اقداماتی از جمله صدور و تمدید پروانه‌های استاندارد، تدوین استانداردهای ملی و بین‌المللی، برخورد با تخلفات و آموزش‌های تخصصی را دنبال کرده است.
🔹
این ویدئو روایتی است از اقدامات اداره استاندارد در راستای کیفیت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/689179" target="_blank">📅 10:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689177">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
کارت‌های ملی فعلی تا پایان ۱۴۰۵ اعتبار دارند/ رئیس سازمان ثبت احوال: نسل جدید کارت‌های ملی جدید از ابتدای سال آینده صادر می‌شود
/ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/689177" target="_blank">📅 10:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689176">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/689176" target="_blank">📅 10:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689175">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
فدراسیون فوتبال ایران جریمه شد
🔹
فدراسیون فوتبال ایران، به دلیل ارائه دیرهنگام درخواست برای صدور مجوز بازی دوستانه تیم فوتبال امید کشورمان مقابل تیم کایسری اسپور ترکیه، مطابق مقررات AFC برای صدور مجوز رقابت‌های بین‌المللی به میزان هزار دلار جریمه شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/689175" target="_blank">📅 10:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689174">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
فرمانده ‌هوافضا: آمریکایی‌ها پهپاد لوکاس را ‌از روی شاهد ۱۳۶ ساختند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/689174" target="_blank">📅 10:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689173">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/894a3db316.mp4?token=cH5e_06BVUTa9gwCeSw9PfvLmpBUZmn8hA7m9lrtosLWIZQ4_6PD0n7gHvbQio-It6ZqwbG1hZwAd6HeppS-1XBN5EEVjabI1mCPz_7dHGbrggy0srOONlC8GrY4widpvAHddD2Be9O3PHbBTGN0vwgsHyZpAZ8KTjk7VE0HHOC0r71VLyN9SOv-hTSFIvxiMW6LpYEdET9PCP_oHfIRJ6EC0rdeW-P2xjRqzn5QhRAMOZKLp0my7L9OOFqDOUtp3wL0Zrl5KacF0zNNQciGiV5lj2hDtlXyJV_V4TuNVlArSZL2VZH38tnG83Rzq1X0h78zqbwKoB6NFNCdO8zF_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/894a3db316.mp4?token=cH5e_06BVUTa9gwCeSw9PfvLmpBUZmn8hA7m9lrtosLWIZQ4_6PD0n7gHvbQio-It6ZqwbG1hZwAd6HeppS-1XBN5EEVjabI1mCPz_7dHGbrggy0srOONlC8GrY4widpvAHddD2Be9O3PHbBTGN0vwgsHyZpAZ8KTjk7VE0HHOC0r71VLyN9SOv-hTSFIvxiMW6LpYEdET9PCP_oHfIRJ6EC0rdeW-P2xjRqzn5QhRAMOZKLp0my7L9OOFqDOUtp3wL0Zrl5KacF0zNNQciGiV5lj2hDtlXyJV_V4TuNVlArSZL2VZH38tnG83Rzq1X0h78zqbwKoB6NFNCdO8zF_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند همیشه کباب‌تابه‌ای تازه، اقتصادی و فوری داشته باش  مواد لازم:
🔹
سویا خشک: ۲۰۰ گرم
🔹
گوشت چرخ‌کرده: ۳۰۰ گرم
🔹
آرد سوخاری: ¼ پیمانه
🔹
روغن مایع: ۲ تا ۳ قاشق غذاخوری
🔹
جعفری خشک یا تازه: ۲ قاشق غذاخوری
🔹
نمک: ۱ قاشق غذاخوری
🔹
پاپریکا، پودر پیاز، پودر…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/689173" target="_blank">📅 10:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689172">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f4a86dc5.mp4?token=bDoQ4pbTWNXbFlTfTPDxDds3DKFzTgomyNvEKe6O4lmiNLDPpVWup6a7RJSp9_Bl8g6KfvPCKaDKymfL5Uuv7cVYR9oLDbKVIOxAFbK7QOcYu7etcTM2VRboYbVaH7ZWC12LE2VsfrYufFJBi-cIgU-d9YG3uKGD-1Ap4gdJKQVOvdFZcMgyn5uH0Qdgb8l5PBUOTpg3mt6CKB-wyYFetcq8-FL5lZ59i248Li0Au_H-B1hRRGv9yTk512c_r1KsAxeO_yNOQfCf-c0lDn8sud--e597w65F-aYFIGgxzk4R5DgW6-W2WZ7KLCUZ5lVfZkxYgDTaud3VH8j7cqeBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f4a86dc5.mp4?token=bDoQ4pbTWNXbFlTfTPDxDds3DKFzTgomyNvEKe6O4lmiNLDPpVWup6a7RJSp9_Bl8g6KfvPCKaDKymfL5Uuv7cVYR9oLDbKVIOxAFbK7QOcYu7etcTM2VRboYbVaH7ZWC12LE2VsfrYufFJBi-cIgU-d9YG3uKGD-1Ap4gdJKQVOvdFZcMgyn5uH0Qdgb8l5PBUOTpg3mt6CKB-wyYFetcq8-FL5lZ59i248Li0Au_H-B1hRRGv9yTk512c_r1KsAxeO_yNOQfCf-c0lDn8sud--e597w65F-aYFIGgxzk4R5DgW6-W2WZ7KLCUZ5lVfZkxYgDTaud3VH8j7cqeBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از ساعاتی پیش یک تیم تروریستی در بخشان سراوان توسط نیروهای قرارگاه قدس سپاه محاصره شده و رزمندگان در حال انهدام تیم می‌باشند
🔹
گزارش تکمیلی در بیانیه قرارگاه تا ساعاتی دیگر به اطلاع مردم شریف ایران خواهد رسید./ صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/689172" target="_blank">📅 09:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689171">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سپاه اصفهان: احتمال شنیده‌ شدن صدای انفجار کنترل‌شده در جنوب اصفهان تا ساعت ۱۴ امروز
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/689171" target="_blank">📅 09:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689169">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51fdf27086.mp4?token=jAaH4-v0fcu3Xs18rjGZPLheCrISBOoyc6Ys_I6DOh0DDsSWyiI-ATdDt6Klag2oyPEaoQg91nVgY_VklqL9-9KWv16r3zB2HWzrxKSaJJGK12Jf0_qMZJeWyKzirbUl2pO8m1Q3yUhCu07PyZoxGM2l-KSS8GmzzMCTdZz9Uj87U7o0nzA0fXCvBCtJNY77uY_6N5E2YEwUdc-JMNa9J39sRwnR56GTg9qUYb6ckV_ETha71lN36PZSclGLEt_11ZTB2ut-Ew8VClLEVr1Z3XAlWieYv1e91S6SMUXRx0S_ed1-ZNSUJ3KKAcs88c97x2L2T_F-xn8Cn9ORdpxEuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51fdf27086.mp4?token=jAaH4-v0fcu3Xs18rjGZPLheCrISBOoyc6Ys_I6DOh0DDsSWyiI-ATdDt6Klag2oyPEaoQg91nVgY_VklqL9-9KWv16r3zB2HWzrxKSaJJGK12Jf0_qMZJeWyKzirbUl2pO8m1Q3yUhCu07PyZoxGM2l-KSS8GmzzMCTdZz9Uj87U7o0nzA0fXCvBCtJNY77uY_6N5E2YEwUdc-JMNa9J39sRwnR56GTg9qUYb6ckV_ETha71lN36PZSclGLEt_11ZTB2ut-Ew8VClLEVr1Z3XAlWieYv1e91S6SMUXRx0S_ed1-ZNSUJ3KKAcs88c97x2L2T_F-xn8Cn9ORdpxEuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرت زدن ترامپ جنایتکار در مراسم ۱۱ سپتامبر
🔹
وبگاه آمریکایی «دیلی بیست» درباره چرت زدن او در این مراسم نوشت: «ترامپِ ۸۰ ساله نتوانست برای ادای احترام به قربانیان ۱۱ سپتامبر بیدار بماند.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/689169" target="_blank">📅 09:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689168">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/689168" target="_blank">📅 09:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689159">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای فایننشال‌تایمز به نقل از منابع مطلع: وزرای خارجه کشورهای خلیج فارس برای پیشبرد توافق هرمز با عراقچی دیدار می‌کنند
🔹
این نشست قرار است روز دوشنبه در شهر ساحلی صلاله در عمان برگزار شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/689159" target="_blank">📅 09:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689157">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
تکذیب تعطیلی مرز مهران
‌فرماندار مهران:
🔹
مرز مهران باز است و فعالیت‌های مسافری و گمرکی در این مرز برقرار است و هیچ‌گونه تعطیلی یا توقفی در روند فعالیت مرز با کشور عراق وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/689157" target="_blank">📅 09:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689156">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/689156" target="_blank">📅 08:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689153">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e9030f43.mp4?token=hue29NJdVL7z6AuppJOIzx9OrQtyFP4D6-6x72aButaAZVm-DHmQYhPoZpj9aUWg0_I416S_UgUH53GJEPQuzDrn1sc7jVn42E4xH-2mWppGoqL1_fUKQQsIoKx4FIRT4mK8SplbaVcZxKoM8-pr6MBZET58qDQzJX6la0EjjF0mwBuCW_q13mXryqufG64P5xLzZnuV2OQEg7gm3k8L8_klT5F5qegon9iJlHUzRn7u7TZPWn4mSM6VVU2QsRP-nyESVapk1VJplc-4tMq3OuPLVC_ZhttuIC7KF8AJ3XhMcXDNotQlgU8rXOyuBGvG6ZVwfn1v1zQXCAGHdvAk5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e9030f43.mp4?token=hue29NJdVL7z6AuppJOIzx9OrQtyFP4D6-6x72aButaAZVm-DHmQYhPoZpj9aUWg0_I416S_UgUH53GJEPQuzDrn1sc7jVn42E4xH-2mWppGoqL1_fUKQQsIoKx4FIRT4mK8SplbaVcZxKoM8-pr6MBZET58qDQzJX6la0EjjF0mwBuCW_q13mXryqufG64P5xLzZnuV2OQEg7gm3k8L8_klT5F5qegon9iJlHUzRn7u7TZPWn4mSM6VVU2QsRP-nyESVapk1VJplc-4tMq3OuPLVC_ZhttuIC7KF8AJ3XhMcXDNotQlgU8rXOyuBGvG6ZVwfn1v1zQXCAGHdvAk5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری نیروهای امنیتی با افراد مسلح در بخشان سراوان  معاون امنیتی استاندار سیستان‌ و بلوچستان:
🔹
نیروهای امنیتی با شناسایی محل تجمع یکی از گروهک‌های مسلح و معاند در سراوان، آنها را غافلگیر کرده و ضربه سختی به این گروه وارد کردند.
🔹
این گروه قصد انجام یک عملیات…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/689153" target="_blank">📅 08:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689152">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb40c5dc75.mp4?token=VUlJcmHi6UNi3UDld8BHsO4H04McztrnzBeG37Ls0sRkaubLC82dSeyV66u2-ftDiRHDLlV88Qp_mieqx0H4noEWhZZA7QGuEOTq_lSJx3OhYx7-TP4puil-LSvRTSqShjSQsk7HunceqhQ8iKJTbyqPJzOANnRRgWtfFbF4MOxZroWXnSyA8H99F5qHcvmbmStfFyZUSSUVV-YCXp4N3WY4oPWujYkB4329dBCCHbLbzVXnm-CRAKQbrUSzM3w47iwilVxa0bXFaCZGDd75CwaLUMuIHQN4hR2n9M-IdD-Cqka7XtA6K0cgUZmjhaX6VAf_7P9XYEgKsBj02LJgbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb40c5dc75.mp4?token=VUlJcmHi6UNi3UDld8BHsO4H04McztrnzBeG37Ls0sRkaubLC82dSeyV66u2-ftDiRHDLlV88Qp_mieqx0H4noEWhZZA7QGuEOTq_lSJx3OhYx7-TP4puil-LSvRTSqShjSQsk7HunceqhQ8iKJTbyqPJzOANnRRgWtfFbF4MOxZroWXnSyA8H99F5qHcvmbmStfFyZUSSUVV-YCXp4N3WY4oPWujYkB4329dBCCHbLbzVXnm-CRAKQbrUSzM3w47iwilVxa0bXFaCZGDd75CwaLUMuIHQN4hR2n9M-IdD-Cqka7XtA6K0cgUZmjhaX6VAf_7P9XYEgKsBj02LJgbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: خیلی‌ها فکر می‌کنند اگر در انتخابات ببازیم، من عصبانی‌تر می‌شوم و کار را یکسره می‌کنم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/689152" target="_blank">📅 08:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689151">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10a23745f.mp4?token=PckKmuUTeHNVxuu6hEzUtsMQFCa6jNN9GyPosfCdaGMyC1AMrMw92pF78xeH6bUYg3x_VOwxDkzEqdYmFSLkDZTiHYHKm4EC2-dlDb-ii5LwEzz2Myqazhkws6IdNgTPq-3wv-d6AaiwqK_fZ7zF4XsJSCp0X-ZVampde5AsvcXUoMOC_UQibHqwR_y398U8DPFqhCQWpn2frEkWfmfpxRt_9qHNH_6RTYTQ0pO4snjEJQewPCU22yna53MRGgN48oBJ22E7SVVUkauDQvZu5YUfGk-a3fDVzlKwWptZZE9VRecqGiBcdFf0F-ScRTfFZrByOUiIGy7SJVON1XLNKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10a23745f.mp4?token=PckKmuUTeHNVxuu6hEzUtsMQFCa6jNN9GyPosfCdaGMyC1AMrMw92pF78xeH6bUYg3x_VOwxDkzEqdYmFSLkDZTiHYHKm4EC2-dlDb-ii5LwEzz2Myqazhkws6IdNgTPq-3wv-d6AaiwqK_fZ7zF4XsJSCp0X-ZVampde5AsvcXUoMOC_UQibHqwR_y398U8DPFqhCQWpn2frEkWfmfpxRt_9qHNH_6RTYTQ0pO4snjEJQewPCU22yna53MRGgN48oBJ22E7SVVUkauDQvZu5YUfGk-a3fDVzlKwWptZZE9VRecqGiBcdFf0F-ScRTfFZrByOUiIGy7SJVON1XLNKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صمصامی، نماینده مجلس: بیش از ۸۶ میلیون بشکه نفت کشور به‌ صورت اعتباری به یک شخص واگذار شده و صرفا ۳۰ میلیون به خریدار نهایی منتقل شده، اما سرنوشت ۵۶ میلیون بشکه نامعلوم است! شخص وزیر باید پاسخگو باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/689151" target="_blank">📅 08:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689150">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سازمان رسانه‌ای رژیم صهیونیستی از برگزاری دور جدید مذاکرات اسرائیل با لبنان در روزهای سه‌شنبه و چهارشنبه در شهر «رم» خبر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/689150" target="_blank">📅 08:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689149">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLCdg7bTYBrGz2jTSucQFtCOrAbgAUXHsu72eQp6IvWxOnaj2a-WBhzVS5OOyhLVbWA3mzlim3IBRC9K5GMepG42KkQ89eMtLlp265xgrMVRzr6xz4RILNrtwtKoUFm12fnEiC6tjYMWpqNasFqigEuoAPB996AugGbpQxO8V_LSuPYw2f0VTk5LCp4XbE0jJN_91Fq0uXrlKy_gqxmtt0dABk1CVt3fvzdelZ1Ihftt7Fsxms3PzbkvUqsliYHyN7fsXkfEqcGDiKqYI6B4OUr4un1H_v1I1MJkACIcx9WRXbFQdP5zLSotHafznYH2MUBTtbToG5RYHZvfqxvoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون: اگر مقاومت عراق می‌تواند جواهر تاج زیرساختی عربستان را هدف قرار دهند، پس هیچ شکی وجود ندارد که ایران هم می‌تواند هر زیرساختی را، در هر لحظه هدف قرار دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/689149" target="_blank">📅 08:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689148">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7UpbvzQxxxts2fh08YEil1icLLk-BAnhFWRCyPyQFyci3WkCVhGtesaV7lGNbu1ZEw1dsl4ExJ7zM4e47e_50_SX0jeRcvYUe3jfDY_iX5mxS9B4m6I-MusGX95u_1FyTEGFJw7x4BonHpO9XbJsoFfWJ6saP7lbotisf8Mv1YuoJhcWDXn-uSBiDAeCJ6F4NKJWViApMqJlfSabnT4uoK-5dvgKi6W1mtK7tDwZqfN3iMI_XqHd91ag_zh85HDfpUoRDwc2-9Mat53v1OaJuVgaiEArfwNoQMytqVCdQzrQ2u5Yh17CKeIPvGWwkO-SswBJwLOyw2tPNH6UK_5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاد دانشگاه میامی: سقوط سعودی بزرگ‌تر از سقوط دیوار برلین خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/689148" target="_blank">📅 08:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689143">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IEJWbNalofkoHO2q7ZTlfc6aXNpr37K5mYMLzSWruPBPKMEmhChj_4jcW7BobyN-GHeivytsfjD8t1Bd6LFDzTdlxYn3LGkC9Lh1AqL7wF9cWpKQzEo273ZV6g6kyYB3j8b25IFpOb0gM_QpdujnnezBVVqPm6DORBePiN4p32XZpvpCJJMolyE2znUJebBkosgBdsAgB-T_7UiiDc1EVD4FqCAU9Zz1XRWJr8Y3PbS3fG3xA-vYXkLevEdXzC_gDLSpRXP_HIij1N6LeSKT0sRfVYRRBMBhdjgL_07biYpjYRoc8sXlSOhOM_fBJOyxGLvjqEL8Y_C8ZAZseQZbmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guiC1YLdnQMdmOvAsGkuCFXWuj3_zSKmxjdY5PRg2h1_T6ChaYgMycSDl1y-RJut_SDWPvN4f03o-DlWhO0vlAMNfQf9GoRkAZ5JVnoxJLgZv0Exck6Jf_sTI9GNdFq7iffUQlUqh55KQs4PS90d1o4hj9TE8tV--OLJA16rSQDYxoVxA_g-G0xSk3hBO5LtxwEMda4EkSq-MoqWO-w20bGy-tWzmRjLtlB-rFookWXOqTGaQtXwyLN90wiWSfwpWIbU8vAqtk1-asnGHwZqC_2-zNLXIuNkv3NeKLCGxC0W_xmhkAKs3VDVWJ3nGRjJKYxCrZm5PYT6XoqKZVGjxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEiff47DypD0fsLGuiVulXnKE3blA4ZI-SXxj4hAb-ZP6oEWGr27pH11ltKH4v3oxTi8F1_U0zKU5cBPsw2uSRXKCatlk1hO4G8yFQ5yWpCGHtSxNa-t79oNHb9Ef6psjsZWnu5ncq7smf7A4i8kHrg7BFFZ8E4TeOVoOYX2ZbXP9k2zB7AxOz0rohSA5rGAII1TN7dLh3uqzUjZr65F4Y6A9ZQQpNKC3jalZyqbruXzJEJBCLt7ebQ6YJRFZSxXz6P64_-qeBQAdgkg5K5Pf65DSduYTW6OonqqIGbKUuJiBmc6IpsZ2UqePe0m6U1GHLHSX6K2JL-qY2oKnKIboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dv79ekGQ4boeajAjQ1OLLdxXWVZY-oMrQ1LSdM-xUNmlgQIFohJY1hykjaBAgWQaXIikotw7ZgipqQqSWYqKc5zRMf3Yj4MgGVZA2lIZyOuVT-Y3pjpMOxUMW68dseDan5QGc8CmKIrLfnSHx04H8DoVRRXyzgechhU_hNIJGa2M4ThQ05CXb5BImVoXN6q5TzA-GEeCh145MbAn_eEs78yIAnXqcJnHqXlrCxzIaFDXgI5eFMRNRNNVa1TL9KtrZsxo133gyFubLCvTXgOZBuSxTgKhBLaQLrOw0aDTVx1La5Nq5zLUiJ3EAUdc9MwQt0hii1PKX1dvvA9YfWMlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yr-WGT-zCBvOW3Lg4Btb8lh37IIQW7dH18o-VGNgBDJWFMREaaefDRTeShSVN_muET4sEamXUHObNPpAuhzRr6c6BjZHMq5xiFuR9rBf0UfyHQlfeFVtlPOKqRp9oOBDZPgpDvuXHes2jjs0QnjttZm7aIj2N4_ciW5XjWnneVztJEj1D4NntTHRE4SaBaAfhzMlbVaP9wsgjC3cnPAo-YWZ-eY-EwOPFy4cSfrt29M0tOnSu0Ih0me56IvfK-QIVKXPxc_Xi5fyxjmeY_0i7P-4xWGrJprSaCG69Mc9IIP2Nn5h1mLJQ6toH3H1AdiA6Nvw7A7XNXIMsCYksc8Y9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قیمت عرفی مشروبات الكلی، جهت تعيين جریمه در سال ۱۴۰۵ اعلام شد
🔹
ارزان‌ترین نوع مشروبات الکلی، آبجو قوطی با قیمت عرفی ۴۲۰ هزار تومان و گران‌ترین آنها ویسکی جانی واکر بلو با قیمت ۳۱ میلیون تومان معرفی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/689143" target="_blank">📅 08:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6723a95a5.mp4?token=i76VNm6lq0nTJ-12Vog50JUWGBN3Yuac1v09a-fG3OrOuzzWUfyTNFCClyizB9qb53b-nnx9vR9dY_LLx8XEnE0MUodgfmJgnxvHOpALriCshaOJgkWzSyi9ASNFdkLxdYqnTCcOD-McKjOOXD1QowMSxU6eIoSevYIc2K5cF5X9SNQj054MGtz3743LOi6BX3fMJIiGmGl52txSIwY0OnuIeA26akZsadsaOBxOfavXKdPexkzDOFnfJDXI3rss9lzzlkqs_XkwwcgwOawTFWh4lpCSxGFJvpS17yCstKLVM_zP1vg76MolPFjQqGKWVAyJueZBZtXCo-W8vxdAlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6723a95a5.mp4?token=i76VNm6lq0nTJ-12Vog50JUWGBN3Yuac1v09a-fG3OrOuzzWUfyTNFCClyizB9qb53b-nnx9vR9dY_LLx8XEnE0MUodgfmJgnxvHOpALriCshaOJgkWzSyi9ASNFdkLxdYqnTCcOD-McKjOOXD1QowMSxU6eIoSevYIc2K5cF5X9SNQj054MGtz3743LOi6BX3fMJIiGmGl52txSIwY0OnuIeA26akZsadsaOBxOfavXKdPexkzDOFnfJDXI3rss9lzzlkqs_XkwwcgwOawTFWh4lpCSxGFJvpS17yCstKLVM_zP1vg76MolPFjQqGKWVAyJueZBZtXCo-W8vxdAlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری تلویزیون الجزایر از فعالیت‌های پشت پرده مزدوران امارات در این کشور
🔹
تلویزیون الجزایر با انتشار اسناد و مکالمات ضبط‌ شده، از دستورات مستقیم مقامات اماراتی به مزدوران داخلی برای تبلیغ و تمجید از بن‌زاید خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/689142" target="_blank">📅 08:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689141">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
وب‌سایت «اینترسپت»: یک شرکت هواپیمایی آمریکایی ارسال تجهیزات نظامی به اسرائیل را از طریق پروازهای مسافری از سر گرفته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/689141" target="_blank">📅 08:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e545e3479.mp4?token=ShuyWaH1cMz5YN3kcDAGXiHmtKoD69VewD2_XKVHRBoJgWIvA3IIPBa-zWqXShZMNiA1PPG1-toF3kmLMRoztnGAoEow33unFuh-MpvS6dWtuXhxtE3cGHkOxEWkU4niVMp892gqfUKhpiPSuUkggLHTY1f5-wSLmZgKwVZUDWVkTRupt42rmR7Ze9ZqEc8og3MlnGhR8OQgOLDn6e4eswJQldfAvgqWS_xFi7h-rcnie1JIS2A3yUxs9JJqfajzgfpQ-TQOyEFz6MEbRhe-9eiATXQ2ZcaZtdLtKvh15YkqfqVcJxhH4AvcNPibF4-KU6Scp8UMIWQ_p9-117SB8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e545e3479.mp4?token=ShuyWaH1cMz5YN3kcDAGXiHmtKoD69VewD2_XKVHRBoJgWIvA3IIPBa-zWqXShZMNiA1PPG1-toF3kmLMRoztnGAoEow33unFuh-MpvS6dWtuXhxtE3cGHkOxEWkU4niVMp892gqfUKhpiPSuUkggLHTY1f5-wSLmZgKwVZUDWVkTRupt42rmR7Ze9ZqEc8og3MlnGhR8OQgOLDn6e4eswJQldfAvgqWS_xFi7h-rcnie1JIS2A3yUxs9JJqfajzgfpQ-TQOyEFz6MEbRhe-9eiATXQ2ZcaZtdLtKvh15YkqfqVcJxhH4AvcNPibF4-KU6Scp8UMIWQ_p9-117SB8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری نیروهای امنیتی با افراد مسلح در بخشان سراوان
معاون امنیتی استاندار سیستان‌ و بلوچستان:
🔹
نیروهای امنیتی با شناسایی محل تجمع یکی از گروهک‌های مسلح و معاند در سراوان، آنها را غافلگیر کرده و ضربه سختی به این گروه وارد کردند.
🔹
این گروه قصد انجام یک عملیات نسبتاً بزرگ در شهر سراوان را داشت که با اقدام نیروهای امنیتی، تعداد زیادی از اعضای آن به هلاکت رسیدند و عملیات مقابله با آنها همچنان ادامه دارد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/689138" target="_blank">📅 08:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/689137" target="_blank">📅 08:00 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
