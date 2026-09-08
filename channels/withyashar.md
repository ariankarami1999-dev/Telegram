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
<img src="https://cdn4.telesco.pe/file/O09Lk02bvORMsBNhKxcrzcS6JO_t9OhFhUGZzyXHFAaeWk8H75L9eCD6euCTu_RzMCd6EswLcEf8s4pU1TRwG6muryiXD7ynJAKVYrCHPW4cxAsjBNPUrHf8qgSOLeINL6EK19GMDZWL15idwssn-QmBIAIfH8vX2pg_qV-1V6knavnUh1sZ3CyTQS2Yt6ZRrOIR7mHznp5pal8vckfZ5LIenvGbBhTWQHJ-kVaYanqN0S6CYSp6jLsh-2zyE_tN2W9o7jBmw9usF4ILXr5JdZ6HSBAsjbXKLzTpBuHp_n2h2oQjkkvOVBirPB-RBS0mCER6xZzxzt7GdzXXUsnWWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 449K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 17:38:33</div>
<hr>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تهران و کرج صدای رعد سنگینی شنیده شد همه نیم متر پریدن و فک کردن حمله شروع شده
@WarRoom</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/22552" target="_blank">📅 16:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22551">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرگزاری رسمی کره‌جنوبی،
یونهاپ (Yonhap)
، امروز گزارش داده وزارت دفاع کره‌جنوبی اعلام کرد یک تیم تحقیقاتی برای
ارزیابی وضعیت امنیتی تنگه هرمز و بررسی شرایط منطقه
اعزام شده است. سئول همچنان در حال بررسی گزینه اعزام نیرو برای مشارکت در تأمین امنیت کشتیرانی در هرمز است، اما
هنوز تصمیم نهایی درباره اعزام نیروی نظامی گرفته نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/22551" target="_blank">📅 16:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پرتاب موشک از کرمان به سمت تنگه هرمز، نقشه و عکس ارسالی @WarRoom</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/22550" target="_blank">📅 16:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22549">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqi6d7c1Eou0jjGJM23HA9QSgODArsUJTCxY-3CSM_4Zwld4bnPn-wZSwJrn1smN0P-0R5epLLGNQ5KcVXHTVrqszCB5oE4uamEGG_1kBZm9r7b8VvGBlnCH0A5n26s9Fvi2GUnxOgWhmOdf8c63E30Vfeqghz4NfevLR4VbVMP1zrYcDA6Qj6MH8V1NNl69TJVK-oE0XmXWra2q7SdpScU43vgrAY5Tb3Z-hge0rmVq1e5ZbDdmJi9Bqj3wtP2_3rJY6s-22XL6ceXghznVHIJ_JlMagJkXBRXrodQzatTn8wO96rzRNJFBpvx-q35YoZz14steneijKScSMf0yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش های بسیار از صدای انفجار از محدوده زندان قزلحصار و هم اکنون عکس و رؤیت ستون دود از این محدوده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/22549" target="_blank">📅 15:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22548">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjJu5jRxOq8tO4CploZhH5c_SNvzWddpU-JOOBfdTkMOSisPyZ_jQKpMe7464aNl1cIEw9QiGlgGgDnYC8u5YESwLXi5i3Pcm-58S3nuCBp2d2EztDIkU3nS7VknQ3uGtVO3MPukLH6vv0IbGd64JzB_KdQGHOudts0obMxPOrbt3o5qOBJyJIoqB1SzvEIt6XLFbf_4-nCHbP91-28UWIIF0PBTEnJPLVZztjE_-bV2zm0EQi-eYm-iEYgT6qW0lS8OoYShES6VPfQqGMftgbOENQBF-N-3_sG4FAna-Bj-BkJcwa528mpWzOUtqDqjd3jA5BaxrALn8Mus2K2-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غرب شمال غزه هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/22548" target="_blank">📅 15:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پزشکیان: نسل جدید با دستور همراه نمی‌شود؛ باید با او گفت‌وگو کرد
نمی‌توان صرفاً دستور داد و انتظار داشت نسل جدید از آن تبعیت کند. او تأکید کرد تحول در نظام تربیتی باید متناسب با شرایط نسل جدید و با نگاهی آینده‌نگر باشد و حل مسائل جامعه نیز به
تقویت گفت‌وگو و استفاده از ظرفیت‌های مردمی در مسجد و محله
نیاز دارد. وی همچنین گفت آنچه امروز در جامعه دیده می‌شود، برونداد نظام تربیتی کشور است و برخی فرصت‌ها برای تربیت نسل جدید در دوران کودکی و نوجوانی به اندازه کافی مورد استفاده قرار نگرفته است
@WarRoom
یاشار : این نسل شیک پاسارگادی خر نمیشه
🫶🏻
✌🏼</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/22547" target="_blank">📅 15:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رویترز : دولت انگلیس امروز قوانین جدیدی برای تشدید فشار اقتصادی بر ایران ارائه کرد؛ این اقدامات
بخش‌های انرژی، فلزات، بانکداری، بیمه و کشتیرانی
را هدف قرار می‌دهد و محدودیت‌های تجاری و مالی علیه تهران را گسترش می‌دهد. همچنین اختیارات لندن برای تحریم کشتی‌های مرتبط با ایران افزایش یافته و
فرود هواپیماهای ایرانی در انگلیس ممنوع خواهد شد، مگر در موارد استثنایی
@WarRoom</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/22546" target="_blank">📅 15:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXT1i7kCjbtqdbcik5Qmkr3SSz4PuPQXU0gjXg5CDuYReFh5rXele6NzKrNwC28l4_2W1WU5DJ-XgTf56w0VeTcTxMq0KQXtULUIycNOWOhN-vXYnBnv3qbSwRqXiD-3v-qnWyRgoG71PoZpp-GdCEtZkvzuyAv-jI4MduVuZOfGd3MeQ0WG1HVBn7YGZG6I4HRJMU8NmpNUt2HEcO0WQyxXxiUJLPqUj9gsg-wgJw3gO0soqTKXi_Wz3F2ceTUeVHwS5excnwtzgOHsONUBw_b4QCNf5hAs8l-4KqTdfn7Eifc-RlqlpUCoT1rOtxThGnmDyw6qktfP9n0Wjjb6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پیش عبدالرووف اسحاقی، فرمانده بسیج پارود در سیستان بلوچستان به هلاکت رسید
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/22545" target="_blank">📅 15:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1rg4eY0d9p1Ax-0rUHhNJVCOGqUibq3cKVVj9FEEtNLsLGPIOGt6FOWaRHTwMMW0r2U2yw-XpLta9fmLOOCCFFEVtineoIfz6Bir8BmmM20WzT-rbhC9Ix7WeQ17qp8anqhDOPk96uXPQFx_ktj4vsKbOW52BOoLCHC0jgMxdExo6W2CLq18StIzjoT4MH62gSAhqT2WAJ14kX_Ag47hIpyUivCKjfJDNPXR9PW5XL4g9Afahp84c1M_iCgK2R-OFZIJn9_VzVwjyk3LFehLcuhVjLHDAr6j6XT9iYTHpT9Gdx3NdnMzqk5lTCWafu2MZB0FBJUnJUMmPuKFd2tng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک بالستیک از کرمان به دریای مکران
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/22544" target="_blank">📅 14:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22543">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXvU7u1bAZJbYaCBpIavk7qfRSxgSDvKETfutl49DnxyVqXzy79UwNRFUi2JZtqk-AOORABhWVsU0XYwHbSi6QtVWpBMDORoe0JLDHntT3Y1bvkVFpvECXc2HDkrAsJIN1jKmN4hYgawkKKe3v5L8Y6tSzTcGEqAt6-j8HikASvlDDqz37g0glWvN3sMLJcpMUOluPYAsRrLLxNm8u_qLj6vsT7SbJhkWPLaoBTg3EcjGZOUP-vEK6dx8VoAltqPrH4m-v1zSpQf8HQqEJdpdhNUx2Bn42Sr_bNtAHbZJpEd6RJtppFA20lo_T7QBBJtzVo3oMsfe-39Co6avqwU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از کرمان به سمت تنگه هرمز، نقشه و عکس ارسالی
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/22543" target="_blank">📅 14:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارش های متعدد از پرتاب موشک از کرمان به سمت دریا
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/22542" target="_blank">📅 14:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دیشب اعتراض به گرانی بنزین در کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/22541" target="_blank">📅 14:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c790194bb.mp4?token=X75KLELvOEoRyHyCl0XGl3l1m6ejAQqvX13LjuSdCQ68x4hcSim-jBY1_had2iN7eQZ638u4-IHUdwQsoJ28QU6VpWLJvBAaJAhJamyui1_dk6aRHgBKTdsr0ZkJxN56ulRITsYue-FzwPsmBaK_bLmw7jk20C6oKPYh36oOVNYcoU1KvIp9oKNnAEJbtQ3iqQJM3zBxpFcvxCZt9gvKnjlPTDiMliiKj03zKG-ceYyVZeauLV-koFY7G-sKBtM_oToFvAuj6yzUgEM36nup50QOCZMQsPhpnLgSfz91emB41wE4V_65dYdIgdB3EQVM_llfKer3WEJGcTV-Qk1vk45ahYIvPxD9Cb_aU7M3XgcoRtB8hCzMVfwg25b5z4bTJOMlXo_vY3NBacbcs9z-5nTP6993Zmeu02qlIOkiakUv02hFxo0dCyKknimLtZPiQ4C17wD_CQ9E26nIYekrGH2x-wKBap9D1TWbT2LYe4-QBkMd6MDAfpenxxwWzLZdmOv2lzIgY_8EqwnVloBMi78bOPR9x3RJ65DsDPpn_540JYHsaqjFJU5mdU7MuyAizjEFqIwAOaTTs6atnUHXKc7i2f-kqE7yNWNp48Jm1o_b84vifNlYsKhT7ah3nLSsP17-uBLoF7kfIjJqHOJfNaycAtv83VTlDRcAKDgwgGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c790194bb.mp4?token=X75KLELvOEoRyHyCl0XGl3l1m6ejAQqvX13LjuSdCQ68x4hcSim-jBY1_had2iN7eQZ638u4-IHUdwQsoJ28QU6VpWLJvBAaJAhJamyui1_dk6aRHgBKTdsr0ZkJxN56ulRITsYue-FzwPsmBaK_bLmw7jk20C6oKPYh36oOVNYcoU1KvIp9oKNnAEJbtQ3iqQJM3zBxpFcvxCZt9gvKnjlPTDiMliiKj03zKG-ceYyVZeauLV-koFY7G-sKBtM_oToFvAuj6yzUgEM36nup50QOCZMQsPhpnLgSfz91emB41wE4V_65dYdIgdB3EQVM_llfKer3WEJGcTV-Qk1vk45ahYIvPxD9Cb_aU7M3XgcoRtB8hCzMVfwg25b5z4bTJOMlXo_vY3NBacbcs9z-5nTP6993Zmeu02qlIOkiakUv02hFxo0dCyKknimLtZPiQ4C17wD_CQ9E26nIYekrGH2x-wKBap9D1TWbT2LYe4-QBkMd6MDAfpenxxwWzLZdmOv2lzIgY_8EqwnVloBMi78bOPR9x3RJ65DsDPpn_540JYHsaqjFJU5mdU7MuyAizjEFqIwAOaTTs6atnUHXKc7i2f-kqE7yNWNp48Jm1o_b84vifNlYsKhT7ah3nLSsP17-uBLoF7kfIjJqHOJfNaycAtv83VTlDRcAKDgwgGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب اعتراض به گرانی بنزین در کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/22540" target="_blank">📅 13:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اتاق جنگ با یاشار : مردم شریف ایران، شرایط ایمنی حمل‌ونقل کشور به‌شدت نگران‌کننده شده است. در بخش هوانوردی، گزارش‌هایی از اختلال سامانه‌های ناوبری گزارش شده همچنین بعد از‌جنگ اکثر سامانه های راداری نابود شده اند و از ترس حملات خاموش کردن عمدی ترانسپوندر برخی…</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22539" target="_blank">📅 13:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش هایی ااز پمپ بنزین پاسداران و پیروزی هم دارم ، ایست شدید و چک کردن گوشی ها هم انجام میشه کاربری گفت گوشی دوستشو چک کردن و گرفتنش @WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/22538" target="_blank">📅 13:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromK M</strong></div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/22537" target="_blank">📅 13:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcOZZvCq1R6PjEwHmYmvjtez9zCHa5Wf8K3MM6y1oRhmaxluJrEKQOH1a95TjTqiNcPzcgIDqswWceIRxouCaeNhys9EB-wsQV_Hn9QOcY8Z7VKf5FuLb9XLuUyJCZzEIdQ1NIVV4Z34iyM5dcHjjWzABDlrr3LNZsvXm6oSZIDw5P0G75dFLM2h7D9fmdOKU4wWvpx5LGYuJi2YJb_J-i-MTo7zLmkQXsC2HHkvXK0vzs6cnckCsFQrdQ35vZ3fkncgOnDu0onKA9V8Zff9vMNGUgTEZKOaymep11vaO29MF7u8u7BDoT-w16MT12eCwlM1zsZdG4JWXSi3D-m4vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : درخواستی :
یمن وارد فاز درگیری گسترده با حوثی‌ها شده؛
چند جبهه از الجوف و مأرب تا البیضاء، الضالع، تعز و حدیده هم‌زمان فعال شده‌اند و نیروهای ضدحوثی در برخی مناطق پیشروی کرده‌اند. نیروهای دولتی یمن در الجوف و البیضاء نیز مدعی پیشروی هستند؛ در این جبهه‌ها نیروهای دولت یمن، قبایل محلی، نیروهای نزدیک به عربستان و گروه‌های مورد حمایت، از جمله نیروهای طارق صالح و العمالقه، حضور دارند. به نظر می‌رسد هدف اصلی افزایش فشار بر حوثی‌ها و عقب‌راندن آنها از مناطق نزدیک به باب‌المندب باشد؛ زیرا هم‌زمانی این جبهه‌ها حوثی‌ها را مجبور می‌کند نیرو و تجهیزات خود را میان چند محور تقسیم کنند. الجزیره به نقل از معاون وزیر دفاع یمن: «تصمیم برای آزادسازی صنعا و یکسره کردن کار گرفته شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22536" target="_blank">📅 13:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پزشکیان در توییتر: با توجه به ادامه حملات و شرایط ، جنگ ادامه خواهد داشت
جمهوری اسلامی ایران همواره با جنگ مخالف بوده و حفظ منافع مردم و امنیت منطقه را در پرهیز از آتش افروزی دانسته است. اما چنانکه تا امروز در برابر تجاوز، دلیرانه به دفاع برخاسته است این مقاومت را تا پشیمانی کامل متجاوزان با قوت ادامه خواهد داد و پاسدار حقوق ملت بزرگ ایران خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22535" target="_blank">📅 12:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22534" target="_blank">📅 11:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22533" target="_blank">📅 11:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">به گزارش TRT ترکیه :
آمریکا پیشنهاد جدیدی را از طریق پاکستان به تهران منتقل کرده است
.
وزارت امور خارجه ایران اعلام کرد تهران در حال بررسی آخرین پیشنهاد ارائه‌شده از سوی آمریکا با میانجی‌گری پاکستان است؛ هم‌زمان دونالد ترامپ از قرار داشتن مذاکرات در «مراحل نهایی» خبر داد و دو طرف هشدارهایی درباره احتمال ازسرگیری حملات نظامی مطرح کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22532" target="_blank">📅 11:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tASEcSrW0RK2O8-_ld-t0m9JffhmgBknHtycUDYHDWAlaKVZH7gEPpKlVWleUNYRD0_edjRDad_C3InhXPxldcto9QfUTv7DN8BLtEqnSf7en1hKR8fk0rP9pbJq4tvoK48kj8LsrJcsUm1sYoCVvHw8yCwwR1cV-C4Jh54taTyp9-JAM6N56eSk9Hbxrmff7h4WwWfaklXMIrk7NJFNXvGuGXA8dkWr6rxwTUXxdf6MR34TM5-XOnqFtDQia8jL34VXfsvBimpD4NEUGgA23CfWLDlkMI_3jjvOwsJvfBLTpbaWlYSyWTKPntjzGa6d20l4_lP-kCoK6gs18W1G8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت ۹۹.۱۰$
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22531" target="_blank">📅 11:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الکسی لیخاچف، مدیرعامل شرکت دولتی روس‌اتم، در پاسخ به پرسشی درباره ساخت نیروگاه‌های جدید در ایران گفت: «بدون شک، آنها چنین علاقه‌ای دارند.
ایران علاقه‌مند به گسترش همکاری با روسیه برای ساخت واحدهای جدید نیروگاه هسته‌ای است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22530" target="_blank">📅 11:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی: دسترسی به برنامه هسته‌ای ایران باید فوراً برقرار شود
رافائل گروسی هشدار داده نبود دسترسی و اطلاعات کافی درباره مواد و تأسیسات هسته‌ای ایران یک نگرانی جدی برای اشاعه هسته‌ای است. همزمان آمریکا، بریتانیا، فرانسه و آلمان برای
ارجاع پرونده ایران به شورای امنیت
تلاش می‌کنند.
نمایندگی جمهوری اسلامی نزد آژانس
اعلام کرده اجرای کامل تعهدات پادمانی
تا زمانی که آمریکا و اسرائیل حملات خود را متوقف نکنند، از دید تهران قابل اجرا نیست
و گروسی باید ابتدا خواستار توقف حملات شود.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22529" target="_blank">📅 10:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تحولات امروز در اطراف علی‌الطاهر
پس از اعلام کنترل اسرائیل،
حملات اسرائیل در منطقه نبطیه و اطراف علی‌الطاهر ادامه یافته
و کفررمان، در نزدیکی این ارتفاعات، نیز هدف حملات سنگین قرار گرفته است. رویترز از کشته‌شدن دست‌کم
۱۲ نفر
در حمله به کفررمان خبر داده است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22528" target="_blank">📅 10:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وال‌استریت ژورنال : درآمد نفتی ایران در حال خشک‌شدن است
، بارگیری نفت ایران پس از محاصره دریایی آمریکا
۸۵ درصد کاهش یافته
و ذخایر نفتی شناور ایران از حدود ۹۰ میلیون بشکه در ژوئیه به حدود
۲۹ میلیون بشکه
رسیده است. این روزنامه پیش‌بینی کرده ذخایر موجود در صورت ادامه روند فعلی تا اواسط اکتبر به‌شدت کاهش یابد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22527" target="_blank">📅 10:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fllc6RJ8FjN0751BJDBqOX8Ie_0MXSfQls5nWiyLwKtgL_BFCCAGQ764eMTjUdEZz0trGVh6O2HrmGaH3IN8J_BpNNHlDd3BW02BJLF5KIA-1NlXNBdOfzNOuLm42zhXbyQoFGHZwrGUxNEUDWFkw2YM4auksVM0r80idOX_v7Glg0lhL8EVqgknraXHdddGoSUZ55sUevS5qUw5YtYrdEOnYV5qZf8Tm_h5bNOH2HSg_YldPCMCmc6TgQ6ngVomRaJ6NAdroNW1FIoGjS5MHLKMvphvqUH8aVlZhe1XEQE9CUfc8kUSrtuk1p77ZnPi7v5hplMh5FqWvlQfzXzpMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : قیمت نفت با پیروزی ما در جنگ با ایران، به‌شدت سقوط خواهد کرد؛ درست مانند همه‌چیز دیگری که در حال کاهش است، اما حتی بیشتر! قیمت هر گالن نفت به ۳ دلار خواهد رسید و در نهایت به کمتر از ۲ دلار در هر گالن خواهد رسید. همه این اتفاقات به‌سرعت رخ خواهد داد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22526" target="_blank">📅 06:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh2a_g4FfWgeZlBRWVEmm5EdPUHDA7EnhWxJqLSRuSoB4ZDfPow4AGA8PhwfzKfu1MLB4s2dkkVA4dfvM8BCi2NbqdteDOAC5xCyh2cr8XhbHaARFQa0uVCv8HqLQ6kXjAthjc1vPw_H3WVpYIH6PQYU5vwwPu7r6hu9kexkz0f6Sry07VUJDFD2QJEHXTYo4AgBOX2o9j8LMNJ158CF7L0Qb1LPylOGxdL790itD_GjnazO6t92oXaa4v6eKp9jbITL1nLLFguRQsX_59mhFFKT7NbOPf-iFpskDUVqM_i8_PVEE-iDYHHGZ1Ijig9AHyLoC8ZpOYIlQzTg00k61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نیرو دریای ایران
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22525" target="_blank">📅 01:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش هایی ااز پمپ بنزین پاسداران و پیروزی هم دارم ، ایست شدید و چک کردن گوشی ها هم انجام میشه کاربری گفت گوشی دوستشو چک کردن و گرفتنش
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22524" target="_blank">📅 00:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بوشهر صدای تیز اندازی گزارش شده
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22523" target="_blank">📅 00:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش ارسالی تایید نشده : پمپ بنزین شهر ری‌در همین لحظه به آتش کشیده شد
@WarRoom
🚨
🚨
🚨
در انتظار تایید و فیلم ها هستم</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/22522" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1Fu9jEQIH62zjCKdsvSwkxqz7CA0Y6gaVnIuzy4E0oazKdtnW0oGv_SPp8y5tWBVPJLC2kC8k8YjIvnlcu6Mi0J6FPQFcBr0jSa2-MzC_hI7a-BlffDsSRLCv_2ni0pQo5jXFhkNK_grjs-khts8gIFn5gFK7TMtnB_fmHEmk1ygmhxukURtd33yesMP8EpHuO2LORTCIVzlI9v6YfYCbdIXN9wdgNlE9JvGqqdOhIY9tp2ZFmMwylqZgUuL098Rszvuq6eSnYIJANYSnyNcXMXYmueihIMUPtjz1Iu6kIozw8JzpJ5EJOq9rWDTXL1l2ctvII4I7qvMEyiT262TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند هواپیمای جنگ الکترونیک و تهاجمی ایی‌ای-۱۸جی در جریان عملیات پرواز شبانه، از عرشه پرواز ناو هواپیمابر جورج اچ. دبلیو. بوش به پرواز درمی‌آید؛ این ناو در حمایت از اجرای محاصره آمریکا علیه ایران در دریای مکران فعالیت می‌کند. تا امشب، نیروهای فرماندهی مرکزی آمریکا برای اطمینان از اجرای کامل محاصره، مسیر
۹۴ کشتی
تجاری را تغییر داده‌اند، ۳ کشتی را از کار انداخته‌اند و ۲ کشتی را با سوار شدن نیروها بازرسی کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22521" target="_blank">📅 00:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نرخ سوم بنزین, از همین لحظه ۱۰،۰۰۰ تومان شد
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22520" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کپلر: تردد کشتی‌ها در تنگه هرمز هفته گذشته ۲۸ درصد کاهش یافت و به ۷۷ فروند رسید
بر اساس داده‌های شرکت کپلر، که در زمینه اطلاعات، داده‌ها و تحلیل‌های مربوط به کالاها و کشتیرانی فعالیت می‌کند، تردد کشتی‌ها در تنگه هرمز هفته گذشته ۲۸ درصد کاهش یافت و به ۷۷ فروند رسید
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22519" target="_blank">📅 23:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22518">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxNyuvsD724Ke2BxCgY7pBlaIlAS4um-eFBqqjSVaIFZK1leWBjzegTz7fDszU5q0R_rJB52_IKxrXbRn-fsNnkAUYvx-gvjohYPwdstbOOTAx0KzdpySnec0BywGpvr-FNj4KBsAnFECOT3pzSaY5wC-hZsfebal3yM2tz-mZ2G9hZz5YTAMSGQmGC7fP08koeEG7TathS-nn8WBtWaWLrKtC5qjxUvNfheojSGyaSwpBb--4eaG_5MkMa_m1m_hM1q7cNWrmLWa8d-ZKh_5is-7o7auQ-lvABkL13zYaDf39SNjOmYlQSiIbVomEZAVLdVFfOjGf5o7ifysGLnqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : چند پرتاب از سیریک به تنگه و صدای انفجار از تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22518" target="_blank">📅 22:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71f020c05.mp4?token=IKoWD63Bgxgd9Qfi3ij7trjFXLwafRGN7uVVxUw2iDcpBQEw4ur08ugjgFvzHIkTKnSxjVAw0bO6mURp81mOeXCCRY2uftO36QkZhPFqZE4t-HtiVtyM0PavlyWhaEGo66-M6P1_H5j_ClmsQ18stqPH0WxoOHKDCGCtqOYbkwlMM_aZLZNT9a5MzDm3lEdJl1QWVTwyLnfmOKNkIJ-q3e7Sk0gqS92cllNNzCpKKKwjmEOV0XdxRRrChdwu4P5NbF9W7HajK47PDvuKG1Ln7nuifN3UWw2non0bbdYyXsQeqLErv9tW6MPRkUHC_CNYJ-pTeJdYEw6OUhHjkJNljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71f020c05.mp4?token=IKoWD63Bgxgd9Qfi3ij7trjFXLwafRGN7uVVxUw2iDcpBQEw4ur08ugjgFvzHIkTKnSxjVAw0bO6mURp81mOeXCCRY2uftO36QkZhPFqZE4t-HtiVtyM0PavlyWhaEGo66-M6P1_H5j_ClmsQ18stqPH0WxoOHKDCGCtqOYbkwlMM_aZLZNT9a5MzDm3lEdJl1QWVTwyLnfmOKNkIJ-q3e7Sk0gqS92cllNNzCpKKKwjmEOV0XdxRRrChdwu4P5NbF9W7HajK47PDvuKG1Ln7nuifN3UWw2non0bbdYyXsQeqLErv9tW6MPRkUHC_CNYJ-pTeJdYEw6OUhHjkJNljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : سلام یاشار این اوضاع امشب قشم یه ماشین بزرگ سیاه هم جلو بود پر آدم
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22517" target="_blank">📅 21:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSina</strong></div>
<div class="tg-text">یاشار خوبی داداش
داداش تهران به شدت جو امنیتی شده من رفتم بنزین بزنم غروبی تو تمام خیابون ها داره موتوری‌های یگان ویژه میچرخه،سره میدان ها یگان ویژه وایسادع حتی جلو پمپ بنزین ها
رفیقمم از پاساژ علاالدین گفت که خواستیم اعتصاب کنیم اطلاعات اومد نزاشت.
داداش تهران منتظره یه جرقه‌است</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22516" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid</strong></div>
<div class="tg-text">یاشار جان من رفیقم تو اگاهیه
میگه امشب اماده باشن
ک ی موقع مردم نریزن ببرون
😅
😅</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22515" target="_blank">📅 21:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش ۲ پرتاب از سیریک ۹:۲۰ دقیقه
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22514" target="_blank">📅 21:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22513">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه، با انتقاد شدید از اقدامات اسرائیل گفت که دروغ‌ها و خرابکاری‌های این کشور باعث شکست تفاهم‌نامه اسلام‌آباد میان ایران و آمریکا شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22513" target="_blank">📅 21:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">روزنامه تلگراف انگلیس: رئیس جمهوری سابق ایران ( روحانی) خواهان برگزاری رفراندوم برای پایان جنگ شد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22512" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر در گفت‌وگو با CNN گفت
اولویت قطر بازگشایی تنگه هرمز، کاهش فشار اقتصادی و جلوگیری از تشدید درگیری‌هاست.
او تأکید کرد قطر به دنبال
راه‌حلی پایدار و گفت‌وگویی فراگیر میان کشورهای منطقه
است و معتقد است تحریم‌ها تاکنون نتیجه مطلوبی نداشته‌اند. همچنین قطر چند طرح، از جمله
یادداشت تفاهم
، برای رسیدن به توافق ارائه کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22511" target="_blank">📅 20:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U95bTNbZagiPbR1nrPePrzhDuK7IBoYzJtyfCyrEbqolKpC3Lf6sGZVi7Wi6DFujdiIplDsHbBCtyuFXIGe_5pWAxBJu7pcwmTv0ZTjGqTrdmQnsUcDkuur9mWGQDf1R5BV6-FS_G-1IWF8zeKITTtJDzDCpJlBykqqqBWHAqM42Fv4trmuR3_KlshmoWiMrc_9JntsxFR0zztEYG34R5oXrQKMJRiOATVnuqWxbSpGDdw73BgpOEQrG4IbYxX0ys_G9mFNVeWqVaXSUiwKga2-7XNyTehiZJ8KoY-ff0ERw-CINYh85xb_mncirhWMThGKCTfRtJOo00tauILY_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث، گزارشی از
وال‌استریت ژورنال
را با این مضمون منتشر کرد:
مسعود پزشکیان و محمدباقر قالیباف
بر ضرورت
پایان دادن به جنگ و مذاکره برای خروج از آن
تأکید کرده‌اند و خواستار تقویت اقتصاد ایران در شرایط فعلی شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22510" target="_blank">📅 19:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ : در انتخابات میان دوره ای به پیروزی قاطع دست خواهیم یافت و آمریکا را نجات خواهیم داد‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22509" target="_blank">📅 18:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688ebf7bb6.mp4?token=Hw6eVqI_aNRZFG9o9w14gfn6LgA2pfASDw003VUP1Qq_bKiJ5kaP-iBIOVbDGn1EQjcDU72tYms-cW7xaFDa-dAI3KSxQq7FPC_LTSXnxzcEjcEixfEM6tABq9IW2eXK3pGrvBooryC6KLTLjmlJW5AWGbuqPTkAVjgfS1rBNUYsFMTA8YDr4-3Bx3sKJH8_JwrKiLwMsmSel-w_SULHmUTSVCQEaJUrVzUdqBo2UZXyY5EbEAzi_qleobbHFTG7HojcD65oXJs_TwRL_idXLb-vMX2iIkYN6yRFsCEeZrZYgS7S090Emp6TWI4wjEFNh5tS0JjnTnRgybdJ2f-0kR9XNPbMgMLvw9nOueDHEnB7VXW_yPulBRocIiSq7FTpi5xXDjMT5dCaNARxKAZmapRUMPr7azaOHqsaPyC7EqyDkqPaxM_ddLRc_XZehmgmw-ctpaEW19wVgnklh69H_ag_RV9-yyuvfFxqVSyGiTcjPcv-E6IE1L9zIXgQocgktMvY-DMk99XsJlL_i8GE3Du4m1EJtzvAAAYPaY3UDULkQlicsCuw3DpiaztnhML1jDeIC8chheypDgDX8Aupl_iu-22K_6ZfVb8WkNC0Vu_tQlyWXtXyc3tvimjyWxucq3_6_1YAeMUnY8AuDho6JNX4FNH83wgDZvpYA8Q9TWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688ebf7bb6.mp4?token=Hw6eVqI_aNRZFG9o9w14gfn6LgA2pfASDw003VUP1Qq_bKiJ5kaP-iBIOVbDGn1EQjcDU72tYms-cW7xaFDa-dAI3KSxQq7FPC_LTSXnxzcEjcEixfEM6tABq9IW2eXK3pGrvBooryC6KLTLjmlJW5AWGbuqPTkAVjgfS1rBNUYsFMTA8YDr4-3Bx3sKJH8_JwrKiLwMsmSel-w_SULHmUTSVCQEaJUrVzUdqBo2UZXyY5EbEAzi_qleobbHFTG7HojcD65oXJs_TwRL_idXLb-vMX2iIkYN6yRFsCEeZrZYgS7S090Emp6TWI4wjEFNh5tS0JjnTnRgybdJ2f-0kR9XNPbMgMLvw9nOueDHEnB7VXW_yPulBRocIiSq7FTpi5xXDjMT5dCaNARxKAZmapRUMPr7azaOHqsaPyC7EqyDkqPaxM_ddLRc_XZehmgmw-ctpaEW19wVgnklh69H_ag_RV9-yyuvfFxqVSyGiTcjPcv-E6IE1L9zIXgQocgktMvY-DMk99XsJlL_i8GE3Du4m1EJtzvAAAYPaY3UDULkQlicsCuw3DpiaztnhML1jDeIC8chheypDgDX8Aupl_iu-22K_6ZfVb8WkNC0Vu_tQlyWXtXyc3tvimjyWxucq3_6_1YAeMUnY8AuDho6JNX4FNH83wgDZvpYA8Q9TWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تفنگداران دریایی و ملوانان ناو آبراهام لینکلن، مشغول عشق و حال در کلابهای  پاتایا، تایلند. @WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22508" target="_blank">📅 18:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ در تروث ویدیو برنامه مارک لوین را بازنشر کرد: در این گفت‌وگو، ویکتور دیویس هنسون ترامپ را «معکوس‌کننده‌ی انقلاب» می‌نامد؛ یعنی رئیس‌جمهوری که قصد دارد روندی را که طی۵۰سال آمریکا و سیاست خارجی آن را تغییر داده، معکوس کند. در مورد ایران نیز تأکید می‌شود…</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22507" target="_blank">📅 18:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏خبرگزاری عراقی «بغداد الیوم» گزارش داده بیش از ۱۵۰ نفر آزادی خواه ایرانی به محل اسکان دانشجونماهای عراقی گروه تروریستی «حشدالشعبی» حامی جمهوری اسلامی در دانشگاه سمنان هجوم برده و شماری از آنان را مورد ضرب‌وشتم قرار دادند. تعدادی زخمی شدند و ادعا کرده پول،…</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22506" target="_blank">📅 18:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الجزیره: ایران به آمریکا اطلاع داده که در صورت اشغال کامل تپه علی‌الطاهر توسط اسرائیل، مستقیماً وارد عمل می‌شود، این منطقه محل استقرار تاسیسات مهم و استراتژیک حزب‌الله است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22505" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سی‌بی‌اس نیوز:
وزارت دادگستری آمریکا در حال احیای یک قانون قدیمی مربوط به
توقیف کشتی‌ها و محموله‌های نفت ایران
است تا بتواند نفتکش‌های ایرانی را هدف اقدامات حقوقی قرار دهد. این موضوع بخشی از فشار اقتصادی آمریکا بر تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22504" target="_blank">📅 17:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd84c2849.mp4?token=VqIS8rQADnI43654S80Miecd9NFcbAw8izzS4XRk6Qq0bAcjhPkM5nebP_886prbc9bLSb0wIeDKpM82_tDCplldjyUwQ9FJvcqex2ZzejskVJ6xZW1FpsixQj2DEILxsTvw2KabWevxhMkDvHB9OALf5psS4L9dYY-qFzHO4Dne2JZPKYeX_339m2fJR2ap6f3yS8PNb4peLo1KnHNUBqhtiT5KdUGLLS3Gkvi-4IsOQl6hZqWbftoyCy2NNzRLMXX1uuEJ12FNHzERWrtbZ9_VmWTxQgbmAF_U1yAUWD-JpBIiU3AlqzEu-tEEkW7grfR7FSRPSLh2Kucbu8Um4DOJ8gM85m4GK8yWNjZa_fYcvpOF9lbUZQpNV8OmxbdcmFWS1z87QR5fvKvLI_hljmwaRoS53wqUKOgCWwxuy5y6eA-GBbPc5spkuTcTZtRD54Vt4b-4WiRj5W6iRhq5o7tyBQcV_Q0rySO7hLAl_NZrya5m6nVj7TB3m33XaDwoLN4_yx1z0SYcUXk-nuEeBxs1V50DP2KRSVA8Vv64lzKcd0bt5BvrGObBltYhxkihMRcPjvc9-ElUZsqfP0zclDSRbtrPzHobC7QH7YwKqIUzYD0rRMuRGoGN9w-sZ13Kk6cltNy4XCeY5w3KatjajR4-6MMa4eyy4zcgYXiHzpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd84c2849.mp4?token=VqIS8rQADnI43654S80Miecd9NFcbAw8izzS4XRk6Qq0bAcjhPkM5nebP_886prbc9bLSb0wIeDKpM82_tDCplldjyUwQ9FJvcqex2ZzejskVJ6xZW1FpsixQj2DEILxsTvw2KabWevxhMkDvHB9OALf5psS4L9dYY-qFzHO4Dne2JZPKYeX_339m2fJR2ap6f3yS8PNb4peLo1KnHNUBqhtiT5KdUGLLS3Gkvi-4IsOQl6hZqWbftoyCy2NNzRLMXX1uuEJ12FNHzERWrtbZ9_VmWTxQgbmAF_U1yAUWD-JpBIiU3AlqzEu-tEEkW7grfR7FSRPSLh2Kucbu8Um4DOJ8gM85m4GK8yWNjZa_fYcvpOF9lbUZQpNV8OmxbdcmFWS1z87QR5fvKvLI_hljmwaRoS53wqUKOgCWwxuy5y6eA-GBbPc5spkuTcTZtRD54Vt4b-4WiRj5W6iRhq5o7tyBQcV_Q0rySO7hLAl_NZrya5m6nVj7TB3m33XaDwoLN4_yx1z0SYcUXk-nuEeBxs1V50DP2KRSVA8Vv64lzKcd0bt5BvrGObBltYhxkihMRcPjvc9-ElUZsqfP0zclDSRbtrPzHobC7QH7YwKqIUzYD0rRMuRGoGN9w-sZ13Kk6cltNy4XCeY5w3KatjajR4-6MMa4eyy4zcgYXiHzpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت , وزیر انرژی امریکا
:
ماموریتی که نیروی دریایی ما انجام می‌دهد فقط اسکورت کشتی‌ها نیست ! بلکه ، جلوگیری از خروج هرگونه نفت یا محصولات صادراتی جمهوری اسلامی میباشد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22503" target="_blank">📅 16:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4abd87594.mp4?token=YYf3P_Ju-Uker7aUnRMAYYPTt6Kz_pWzuFdRP1XxjsrCfpgmz_1bx2OsoWJvsRjGRnCTQ92pGP-SDz9hPKpcMduvEA2MUnH_010-PDFvX9pLgJtBEzpG2mcLxcijDYG7oejM4gS28kPLqBthzFt3vkCVkGuNLpt7UHdKJ7bCNfalqG2kqptQt_5fjvhUKOX5tK8rILx2LD915_cm1sSnjmeQAJUfS-vXSItTWro-G9oxtDUh9niQHWRiJFwsHcBinmYyWialdYkjdPoIMDB-yLE_HntV1GuJxKUGCmfhHHSCcvSP6BqMgPElOl3goO90JuDjnY6dZhdDQtP1HDwmFBATfb17-ZlDTS1Uq7jPdZd8hYp73hpbFZBeB-uL3AHSEmocC3hZ7u-HS0Jj98FWfj51u98PNWSQp2mZCPv3Tl9CmFwnmDT-xvLCWZ71v1YbHX28wR-bzisQmn0OLEzB-4Dc2fMJVu4nqLKry6YGFZXnUdKWj3pSMigdgj1EvYMxGwW_BilICeP643gchVf5QIJHMjDCM7wUwXAuf8QwKgMHTVvOWScznj-XD1bKreY8FNCjdy_q3olU6pLYRoc9wMCbtC7TzZ_wckukZp9lVsfnoe6_j40B7g_YDSbI0nKeiRu711LaI-Iya4-0zXHmNxXEMyvW5BT3G61eT5ehOw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4abd87594.mp4?token=YYf3P_Ju-Uker7aUnRMAYYPTt6Kz_pWzuFdRP1XxjsrCfpgmz_1bx2OsoWJvsRjGRnCTQ92pGP-SDz9hPKpcMduvEA2MUnH_010-PDFvX9pLgJtBEzpG2mcLxcijDYG7oejM4gS28kPLqBthzFt3vkCVkGuNLpt7UHdKJ7bCNfalqG2kqptQt_5fjvhUKOX5tK8rILx2LD915_cm1sSnjmeQAJUfS-vXSItTWro-G9oxtDUh9niQHWRiJFwsHcBinmYyWialdYkjdPoIMDB-yLE_HntV1GuJxKUGCmfhHHSCcvSP6BqMgPElOl3goO90JuDjnY6dZhdDQtP1HDwmFBATfb17-ZlDTS1Uq7jPdZd8hYp73hpbFZBeB-uL3AHSEmocC3hZ7u-HS0Jj98FWfj51u98PNWSQp2mZCPv3Tl9CmFwnmDT-xvLCWZ71v1YbHX28wR-bzisQmn0OLEzB-4Dc2fMJVu4nqLKry6YGFZXnUdKWj3pSMigdgj1EvYMxGwW_BilICeP643gchVf5QIJHMjDCM7wUwXAuf8QwKgMHTVvOWScznj-XD1bKreY8FNCjdy_q3olU6pLYRoc9wMCbtC7TzZ_wckukZp9lVsfnoe6_j40B7g_YDSbI0nKeiRu711LaI-Iya4-0zXHmNxXEMyvW5BT3G61eT5ehOw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
حاوی الفاظ رکیک ولی به جا
,
دقت فرمایید.
⚠️
جمهوری اسلامی در یک تصویر
، خودش لنگان لنگان با لباسی ژولیده، بدنی نحیف و لاغر،خرکش بدون تعادل همه پرچم ها را یکجا را بر دوش میکشد
😂
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22502" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">روسیه و کره شمالی نخستین پل ارتباطی میان دو کشور را افتتاح کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22501" target="_blank">📅 15:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الجزیره: حملات هوایی اسرائیل به جنوب لبنان، از سر گرفته شده است. @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22500" target="_blank">📅 15:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b12d040c7.mp4?token=SfSnV1tFcd9ffI4SBpDg2RNKzloLxYXq_K_oHzzq8Wk-vbkPkwVs9ZT3dIeAzsAQA9-IUrZlJsoPduAKk9Q5lc6QO2gzjoa1U0s10fyLZZe8AYBUF4w3Wwwzz6oQaj8F3ceudwgFnC4PEvMWV-xT-NNBWd0eMuKs8z67JkPpghLLnilvGJ6Up6slr70My02rSMHPGAIpCitsS4SDNWrmDt64g3WGyVrATMZlTqe5NpyPZf0ji2MMC_3zN9Z_oHIRiE0sAkVoHlG4srIkc28TzTRjBCshZLaRpMOs3p2F1qJXcA7vzf_taiZeAGnzyMLlnK4hm8_Sdp0OWHWAqyxAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b12d040c7.mp4?token=SfSnV1tFcd9ffI4SBpDg2RNKzloLxYXq_K_oHzzq8Wk-vbkPkwVs9ZT3dIeAzsAQA9-IUrZlJsoPduAKk9Q5lc6QO2gzjoa1U0s10fyLZZe8AYBUF4w3Wwwzz6oQaj8F3ceudwgFnC4PEvMWV-xT-NNBWd0eMuKs8z67JkPpghLLnilvGJ6Up6slr70My02rSMHPGAIpCitsS4SDNWrmDt64g3WGyVrATMZlTqe5NpyPZf0ji2MMC_3zN9Z_oHIRiE0sAkVoHlG4srIkc28TzTRjBCshZLaRpMOs3p2F1qJXcA7vzf_taiZeAGnzyMLlnK4hm8_Sdp0OWHWAqyxAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ اگه را داشت ماشین ریاست جمهوری رو هم الان معاملشو بسته بود ، یه ایرانی هم گذرموقتش میکرد میاورد ایران دور دور
😂
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22499" target="_blank">📅 15:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک منبع اسرائیلی به i24NEWS: مشخص نیست جرقه‌ای که باعث شعله‌ور شدن اعتراض در تهران شود چه زمانی خواهد بود، اما خواهد آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22498" target="_blank">📅 14:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فایننشال تایمز گزارش داد
تأسیسات نفتی شرکت آرامکو در منطقه جازان عربستان سعودی امروز هدف حمله جدید قرار گرفته‌اند.
میزان خسارت در حال بررسی است و به گفته یک منبع مطلع، ابعاد حمله با حمله ماه گذشته به این تأسیسات مشابه بوده است.
جازان به‌دلیل نزدیکی به مرز یمن، طی ماه‌های اخیر چندین بار هدف حملات حوثی‌ها قرار گرفته است. آرامکو در حمله قبلی اعلام کرده بود اختلال ایجادشده
تأثیر قابل‌توجهی بر عملیات یا وضعیت مالی شرکت نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22497" target="_blank">📅 14:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommorteza</strong></div>
<div class="tg-text">علاالدین داشتن اعتصاب میکردن اطلاعات ریخت بالا گفت باز کنید یا بازداشت میشین</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22496" target="_blank">📅 14:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromyasaman sh</strong></div>
<div class="tg-text">یه دونه‌ای
دلم گرفته بود داشتم گریه می‌کردم. وویست رو باز کردم گفتی زارتان زورتان خندیدم.</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22495" target="_blank">📅 14:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2827c98c29.mp4?token=qZOiDrTVVw9d9s2bSDqPX8D114egncBXfGqmmWe0dIFSDPnbEEU9R5S_gT74m0Mc0Vaqu-c5qTwpPVgeBKeS6Bj2DhEwvokfMGNlb4LFDV6AvqyHNiCfn6k_mB16kvbB42UOVPk8n5zktZQbEOEFhyUuKsFdQo4jFj9OiY8JhfqzIJH3URt8NEpJOkuUAaT8WwPhdfaJGdZga6qDT99R8ae50c4msmRcphQMLiZfJzwZHXHmXGC7Pbs8eFH74kHrRYBZg9tjwLp3vaDbUrxDCw3rs9Cqa3OFQcu9XWah4JS7ZNHuP7IIwq8ptuf-zWlX9fiLUH9c_pV6g0oJJNa8Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2827c98c29.mp4?token=qZOiDrTVVw9d9s2bSDqPX8D114egncBXfGqmmWe0dIFSDPnbEEU9R5S_gT74m0Mc0Vaqu-c5qTwpPVgeBKeS6Bj2DhEwvokfMGNlb4LFDV6AvqyHNiCfn6k_mB16kvbB42UOVPk8n5zktZQbEOEFhyUuKsFdQo4jFj9OiY8JhfqzIJH3URt8NEpJOkuUAaT8WwPhdfaJGdZga6qDT99R8ae50c4msmRcphQMLiZfJzwZHXHmXGC7Pbs8eFH74kHrRYBZg9tjwLp3vaDbUrxDCw3rs9Cqa3OFQcu9XWah4JS7ZNHuP7IIwq8ptuf-zWlX9fiLUH9c_pV6g0oJJNa8Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : مردم شریف ایران، شرایط ایمنی حمل‌ونقل کشور به‌شدت نگران‌کننده شده است.
در بخش هوانوردی، گزارش‌هایی از اختلال سامانه‌های ناوبری گزارش شده همچنین بعد از‌جنگ اکثر سامانه های راداری نابود شده اند و از ترس حملات خاموش کردن عمدی ترانسپوندر برخی هواپیماها منتشر شده است؛ موضوعی که می‌تواند شناسایی و تفکیک هواپیماها را برای کنترل ترافیک هوایی دشوار کند و خلبانان در موارد بسیار بصورت چشمی هدایت را انجام میدهند ، در ویدئوی تازه در این رابطه نیز یک هواپیمای کاسپین در فاصله‌ای حدود ۳۰۰ متری از یک هواپیمای تابان عبور کرده است.
در جاده‌ها نیز وضعیت بدتر است فرسودگی ناوگان و مشکلات نگهداری به علت هزینه بسیار بالا سرویس ، خطرات جدی ایجاد کرده است. تنها در تازه‌ترین حادثه، نقص سیستم ترمز یک تانکر حامل بنزین در محور سنندج–همدان باعث برخورد با خودروهای دیگر و آتش‌گرفتن تانکر شد؛ ۱۱ نفر در این حادثه جان باختند و ۷ نفر مصدوم شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22494" target="_blank">📅 14:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو: ما به نابودی خرابکاران، پیگیری کسانی که آن‌ها را اعزام می‌کنند و تخریب زیرساخت‌های تروریسم در کرانه باختری ادامه خواهیم داد. @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22493" target="_blank">📅 13:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو: ما به نابودی خرابکاران،
پیگیری کسانی که آن‌ها را اعزام می‌کنند
و تخریب زیرساخت‌های تروریسم در کرانه باختری ادامه خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22492" target="_blank">📅 13:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آمریکا و اتحادیه اروپا در تلاشن شورای حکام آژانس بین‌المللی انرژی اتمی قطعنامه‌ای تصویب کنه که پرونده هسته‌ای ایران رو به شورای امنیت سازمان ملل ارجاع بده.
جمهوری اسلامی هم تهدید کرده که اگه این کارو انجام بدید، جواب متقابل میدیم. بالاخره از ان‌پی‌تی خارج میشن.
پیمان NPT در سال
۱۹۶۸
برای جلوگیری از گسترش سلاح‌های هسته‌ای ایجاد شد و در
۵ مارس ۱۹۷۰
به اجرا درآمد. ایران
از دوره پهلوی
عضو NPT بوده و جمهوری اسلامی در سال ۱۹۷۹ از این پیمان خارج نشد و عضویت ایران ادامه پیدا کرد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22491" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22490" target="_blank">📅 13:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gisUOQmVu5VZTkYZoLmd_zGpbyrO7Nhl3IsvtRagc-gpdvfqdpI0pjtoYrI1TfUkwpOH9HnmeSaSi3Kp9lKqu0N3_A2iOGliyFVTuhZ8OAwpTAHTzlBLRPXcBs2mIJR5CYQXAiTifgZMbMKufMReWqNSfPjA7jzQlPyYalmvN6HmBMu20bLqEbro3hB6zeL6j1WVfV2oKb1PPSbW6gjee2n4S_y0yqMm-OQkhqREfsUJ3OtYy2BHsM69J9TTvd17HwaptWyhL-5jVvJUYdbMm78riZHkTQRDTjA8pK8RvAARouOQd6J4fdsZFxydzR9QXhwRPy4cbwH1quwxarXRbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث ویدیو برنامه مارک لوین را بازنشر کرد:
در این گفت‌وگو، ویکتور دیویس هنسون ترامپ را
«معکوس‌کننده‌ی انقلاب»
می‌نامد؛ یعنی رئیس‌جمهوری که قصد دارد روندی را که طی۵۰سال آمریکا و سیاست خارجی آن را تغییر داده،
معکوس کند
. در مورد ایران نیز تأکید می‌شود که ترامپ برخلاف سیاست رؤسای جمهور پیشین،
به دنبال مهار موقت جمهوری اسلامی نیست، بلکه می‌خواهد تهدید اصلی رژیم را از میان ببرد
؛ به‌ویژه
توان هسته‌ای و موشکی و ظرفیت آن برای تهدید آمریکا و متحدانش
. هنسون این رویکرد را بخشی از همان
«معکوس‌کننده‌ی انقلاب» گسترده‌تر ترامپ
می‌داند؛ یعنی
شکستن سیاست‌های گذشته و بازگرداندن ابتکار عمل به آمریکا
. نکته امیدوارکننده برای مردم ایران این است که در این نگاه،
جمهوری اسلامی صرفاً یک حکومت مزاحم برای مذاکره و مهار نیست، بلکه یک تهدیدی است که باید قدرت آن از بین برود.
این گفت‌وگو همچنین بر این ایده تأکید دارد که در صورت
تضعیف قدرت رژیم، مردم ایران و نیروهای مخالف جمهوری اسلامی می‌توانند نقش مهمی در تغییر آینده کشور داشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22489" target="_blank">📅 13:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtPNlrixcHmlJQIZSq-PRouIKaihfRpFqvKwPhIA0hoZr6-_Bh1Syh8SqDtPx5Or-TwNwf2aiT7nwcnHdQt9m6icMYWwNV9pKyuqEyUqB0BeyFPcH3x9AjTJioqaCQBWlEJhKP-OphUTt8xfxZJti_6Po7C6bSRel8oBNzrQY66fN_veHunUk-I7W3zgQj5FWrPHI7jHETeqhVLkRdWjrvsiw6A934fO0BxSaWX7JILMaKrZyl3I6xTW6ZKOVJzEuqpHN0-rgT58aB4VnlIPMrUhu7HJW9Q8uNKezeXLzUHUSyo9PA_xOknHe3RjCx24m9vWRAPe_Tpe6Dog4yFIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث و نظارت بر نابودی قایقهای تندرو
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22488" target="_blank">📅 13:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22487">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbc57d78d.mp4?token=vZgSnt2ms9uqnZldNSfBfcyoRYJgOj7hiAcTewrw755IkTVVkBE877OGvjB4qJJxCQA0oTlB9Jxu4agyj90sxx1FkGJEMX7mSz2jTZJbXtx716GyO6Ivf0ufGSu2IwyrsYQ8QxGDg7V4iWmOehbJpKtuwdyR__H6Xi85Am0N-k6YzufZRuDqW6D8FMGHScKNNmJqC7NDIt85kbcIsysgSQ4MEkTvtDPelrY7BUSdtrtMuEsw2NDFNjTXPUZcBsTdnKoy06k_7YuMe7J3wnCd-aS4F0cNfeG7H7rPrRqnmP4J4-hvkcjTsXEal0wA87elCKnhm-WIoSR3Wd2lcKxBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbc57d78d.mp4?token=vZgSnt2ms9uqnZldNSfBfcyoRYJgOj7hiAcTewrw755IkTVVkBE877OGvjB4qJJxCQA0oTlB9Jxu4agyj90sxx1FkGJEMX7mSz2jTZJbXtx716GyO6Ivf0ufGSu2IwyrsYQ8QxGDg7V4iWmOehbJpKtuwdyR__H6Xi85Am0N-k6YzufZRuDqW6D8FMGHScKNNmJqC7NDIt85kbcIsysgSQ4MEkTvtDPelrY7BUSdtrtMuEsw2NDFNjTXPUZcBsTdnKoy06k_7YuMe7J3wnCd-aS4F0cNfeG7H7rPrRqnmP4J4-hvkcjTsXEal0wA87elCKnhm-WIoSR3Wd2lcKxBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادای احترام یکی از آسیب دیدگان چشمی به ناو هواپیمابر آبراهام لینکلن در تایلند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22487" target="_blank">📅 12:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش های
تایید نشده
از منهدم کردن یک کشتی جدید در
خارگ
توسط امریکا
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22486" target="_blank">📅 12:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ارسالی : سلام یاشار امروز از تعزیرات اومدن گفتن تمام لاستیک های کهنه که جلوی آپاراتی ها هستش باید فوراً جمع کنن کلا 24ساعت مهلت دادن برای جمع‌آوری گفتن به خاطر این دوباره ممکنه اعتراضات شروع بشه اگه مردم لاستیکا رو از جلو در مغازتون برداشتن و تو خیابون آتیش زدن  خسارتش رو باید مغازه دار بده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22485" target="_blank">📅 12:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22484">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بقایی سخنگوی وزارت امور خارجه: ظرف روزهای آینده، تفاهم ایران و عمان درباره تنگه هرمز نزد سازمان بین‌المللی دریانوردی ثبت خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22484" target="_blank">📅 11:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بقایی: بنا داریم در نشست مجمع عمومی سازمان ملل مشارکت کنیم به شرط آنکه آمریکا ویزایمان را به موقع صادر کند
فرانسه، انگلیس و آلمان به دنبال تشدید اوضاع هستند، حتما ایران در قبال اقدام نسنجیده‌ سه کشور اروپایی و آمریکا تدابیر لازم را می‌اندیشد
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22483" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b940d08b.mp4?token=COedyNCOS7M5Ag66B1YyRjNg2jT00B1e1YobDtSqIdww5KVLy03LnwdE9sjC7T0AStTqhPRpDhOa9iGGvj1srT5B462X_Zoi0aRucxZxQzLJdM-ATS_tvWHdjz4eTeXvxHkFc0_Cb5G_uGZXeBQUXsdnkp98tPscxb9MDtucPtrYsvc3izZoAXe89kmWsJ0LY0i3YNffYVxtQP_ky8XASmL6VGWxr7kdsRng6wAs80jFLgkVKEIhkaSHkiRXgkU6Z_xvwMcP2I76LWNK-IoON2rTml7K5rZsJ9yfOdkNG__E3WKf8lxKoCJLJuYLYsAs35aWDq0lpzTOlPSR6ORPN4HkXk0eqiOzBpx8vvg6kei6-i7UcbI3XdXgRPpVq57dj6U7rmK1__s7yAAvGw_u8-EDcTl6AX_9CGlH57gq6u0lN7txSH4_gME6ALDLKdVvMjplY7tmGUwlCOrcYc8MI_A1YVnvD2imNAVsOWoHRiD1hj8xx4cFCTQrqxPz9c_oiGCKy7pZk79RBqwCAHX3XCXE4P8q5-LYG_ZkEoByBCzKFHnu108fuCXdyTt33IL5Wr869_FJK_q0e061CKogfcrzf-IFBUj2NbBIHnDa5FKKl2RlQUuPwXjbH2uuZwrJV-64BGbsEUj4Grx1uQaptsOEH-X4nDCoYxsSFbTmgDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b940d08b.mp4?token=COedyNCOS7M5Ag66B1YyRjNg2jT00B1e1YobDtSqIdww5KVLy03LnwdE9sjC7T0AStTqhPRpDhOa9iGGvj1srT5B462X_Zoi0aRucxZxQzLJdM-ATS_tvWHdjz4eTeXvxHkFc0_Cb5G_uGZXeBQUXsdnkp98tPscxb9MDtucPtrYsvc3izZoAXe89kmWsJ0LY0i3YNffYVxtQP_ky8XASmL6VGWxr7kdsRng6wAs80jFLgkVKEIhkaSHkiRXgkU6Z_xvwMcP2I76LWNK-IoON2rTml7K5rZsJ9yfOdkNG__E3WKf8lxKoCJLJuYLYsAs35aWDq0lpzTOlPSR6ORPN4HkXk0eqiOzBpx8vvg6kei6-i7UcbI3XdXgRPpVq57dj6U7rmK1__s7yAAvGw_u8-EDcTl6AX_9CGlH57gq6u0lN7txSH4_gME6ALDLKdVvMjplY7tmGUwlCOrcYc8MI_A1YVnvD2imNAVsOWoHRiD1hj8xx4cFCTQrqxPz9c_oiGCKy7pZk79RBqwCAHX3XCXE4P8q5-LYG_ZkEoByBCzKFHnu108fuCXdyTt33IL5Wr869_FJK_q0e061CKogfcrzf-IFBUj2NbBIHnDa5FKKl2RlQUuPwXjbH2uuZwrJV-64BGbsEUj4Grx1uQaptsOEH-X4nDCoYxsSFbTmgDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید : در روشن‌ترین روز، در تاریک‌ترین شب، هیچ پلیدی از دید من پنهان نخواهد ماند. بگذار کسانی که قدرت پلیدی را می‌پرستند، از قدرت من برحذر باشند... نور فانوس سبز!
کد سیگنال این پیغام
:در داستان اصلی «Brightest Day»،
Entity منبع اصلی حیات و نیروی زمین
است که پس از حملات نکرون و نیروهای تاریکی به‌شدت تضعیف می‌شود.
Entity به دلار آمریکا، منبع اصلی قدرت اقتصاد جهانی، تشبیه شده که بر اثر سال‌ها سیاست انفعالی و بی‌ثباتی‌های ناشی از جمهوری اسلامی تضعیف شده است.
حلقه فانوس سبز نیز نماد
اراده، غلبه بر ترس و ایجاد تغییر
است؛ و جهت‌گیری آن به سمت سرزمین ویران‌شده، به حرکت ترامپ و آمریکا به سوی خاورمیانه و به‌ویژه
ایران، به‌عنوان مرکز ثقل منطقه
تعبیر می‌شود. در پایان داستان، نور سفید نگهبانی را برای احیای زمین انتخاب می‌کند؛ این تصویر نماد
آغاز دوره‌ای تازه برای بازگرداندن ثبات و امنیت به منطقه
است.
پیام نهایی: پایان دوران مماشات با جمهوری اسلامی، اراده برای تغییر و آغاز روند بازسازی نظم خاورمیانه با محوریت ایران
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22482" target="_blank">📅 11:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مدیرعامل شرکت فرودگاه‌ها:
۲۷ فرودگاه در جنگ آسیب دیدند
که آسیب‌ها در سطوح مختلف پروازی، باند، ساختمان های ایمنی، دستگاه‌های کمک ناوبری و بازرسی، ترمینال های مسافری و...بودند.بارها گفته‌ایم که بعد از آتش‌بس جنگ ما تازه شروع شده است.
بازسازی آنها کار سختی بود، ولی انجام شد، زیرا در بخش ساخت و ساز فرودگاهی توان خوبی داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22481" target="_blank">📅 10:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4f398265.mp4?token=RFg4KLWTSmXxdmUcuUzc-HLyHO9juh_lNM3lpve-oTcGRvUEohhEJkJ-4cGtY32ormxW95VvaLeakfJXMtx_RyNcj3t9Oza_iGhPeST-OIACLgadr4mGibZexs2b8O5sbXPWeAwN442mgpKLS608OW7FK0pZzzWX95xaEHKM3P861s3ZpHuuDNpyrZN7TG8YQgbvFkKjvBdZpf_q_9Bbh6LoijUdkyVGB3p_sN3zi_lA8uyeNVEa3uiyj6H3zoiB5MWb7RoCPyn5mrf-RC0KNQ4V0m-YyDptGsDNnZKAd5T6lDG0aCDeaXJ-CiGjvx_dx05LGOVIw4DiDjqoXXnlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4f398265.mp4?token=RFg4KLWTSmXxdmUcuUzc-HLyHO9juh_lNM3lpve-oTcGRvUEohhEJkJ-4cGtY32ormxW95VvaLeakfJXMtx_RyNcj3t9Oza_iGhPeST-OIACLgadr4mGibZexs2b8O5sbXPWeAwN442mgpKLS608OW7FK0pZzzWX95xaEHKM3P861s3ZpHuuDNpyrZN7TG8YQgbvFkKjvBdZpf_q_9Bbh6LoijUdkyVGB3p_sN3zi_lA8uyeNVEa3uiyj6H3zoiB5MWb7RoCPyn5mrf-RC0KNQ4V0m-YyDptGsDNnZKAd5T6lDG0aCDeaXJ-CiGjvx_dx05LGOVIw4DiDjqoXXnlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏خبرگزاری عراقی «بغداد الیوم» گزارش داده بیش از ۱۵۰ نفر آزادی خواه ایرانی به محل اسکان دانشجونماهای عراقی گروه تروریستی «حشدالشعبی» حامی جمهوری اسلامی در دانشگاه سمنان هجوم برده و شماری از آنان را مورد ضرب‌وشتم قرار دادند. تعدادی زخمی شدند و ادعا کرده پول، تلفن همراه و ساعت برخی از آنها نیز گرفته شده. گزارش‌هایی از تجمع مقابل خوابگاه و محاصره تعدادی از دانشجویان عراقی منتشر شده است. پلیس رژیم جمهوری اسلامی در محل حاضر شد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22477" target="_blank">📅 10:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc3ca6006.mp4?token=QKbfDb5Br60sWf6Vzz4KxZcuTO60tn23f3iLDrdjdw2vR6d9RF-Avhl-54lxNG3NkOPyY1s9kC1tLcltDqCXgvvAZHGKyNNBufseG1X1gRw7nAzCzTtZ5QJNiavFVDgfOds_4njgtocvwGK_zDa7NkhRG8E0gp4oV5Ar6MYSBo_pfeakPtJItiC8jtSjhTmNJzHw2bgMxyURS9AcuVGVxg1avxuU_rt3PEgkN4HxC7HaGQCZwuqg_ROiQxOAb5uWCP6z9dfoJqYfNKzbMCcdwCBKcoPUP9-BB5GZrvhPYf073mjf9CP-JlPkvvwxdKCZS2Gjq0uuhx_Okebh8rlnJ72PSOXqMo9-MxM5SFbgJbkFAYPSB2PH0tPjp0KZAeSF_krn_Ut4bErsoL1uG0nHltHSd9fjDUQVWfJILEz7cqfLS-ppczQFiYuoCEB5yvKNHJHPjVb05fjMHfo08UCqlU2LctowGibDXtlXeiY9uAY5TYG0BHLV59mLNcWwQA04d3c4G4vRcgI4IagCwI_aVeg-oJfGUc6_fIAmvpNvdwZq9_FmnoY3xdc6dp7C-XO7-WlfzxeZGcFQlrKDSj371hYNASCkUFx51r5MpBzgc8ET2-ZF_4fIdTpYnWK8fekxBJ5LUy9D7LaJuCP5NAQeW78Ezr3cv_HG_h61yBGIX3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc3ca6006.mp4?token=QKbfDb5Br60sWf6Vzz4KxZcuTO60tn23f3iLDrdjdw2vR6d9RF-Avhl-54lxNG3NkOPyY1s9kC1tLcltDqCXgvvAZHGKyNNBufseG1X1gRw7nAzCzTtZ5QJNiavFVDgfOds_4njgtocvwGK_zDa7NkhRG8E0gp4oV5Ar6MYSBo_pfeakPtJItiC8jtSjhTmNJzHw2bgMxyURS9AcuVGVxg1avxuU_rt3PEgkN4HxC7HaGQCZwuqg_ROiQxOAb5uWCP6z9dfoJqYfNKzbMCcdwCBKcoPUP9-BB5GZrvhPYf073mjf9CP-JlPkvvwxdKCZS2Gjq0uuhx_Okebh8rlnJ72PSOXqMo9-MxM5SFbgJbkFAYPSB2PH0tPjp0KZAeSF_krn_Ut4bErsoL1uG0nHltHSd9fjDUQVWfJILEz7cqfLS-ppczQFiYuoCEB5yvKNHJHPjVb05fjMHfo08UCqlU2LctowGibDXtlXeiY9uAY5TYG0BHLV59mLNcWwQA04d3c4G4vRcgI4IagCwI_aVeg-oJfGUc6_fIAmvpNvdwZq9_FmnoY3xdc6dp7C-XO7-WlfzxeZGcFQlrKDSj371hYNASCkUFx51r5MpBzgc8ET2-ZF_4fIdTpYnWK8fekxBJ5LUy9D7LaJuCP5NAQeW78Ezr3cv_HG_h61yBGIX3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخیراً تماس هایی از مبداء نامشخص
(شماره نمایشی سوریه) با مردم بومی جنوب کشور حاصل میشود و درخواست میکنند که طی درگیری های پیشِ‌رو هیچگونه حمایتی از سپاه نداشته باشند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22476" target="_blank">📅 10:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS.A.H74</strong></div>
<div class="tg-text">سلام آقا یاشار گل خوبی من بندرکنگ هستم سمت دریا ساعتای ۶صدای مهیب انفجار اومد نمیدونم چی بوده</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22475" target="_blank">📅 10:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">العربیه: در حملات اسرائیل به کفررمان در جنوب لبنان تا این لحظه 9 نفر کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22474" target="_blank">📅 10:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رویترز , تنگه هرمز در پایین‌ترین سطح تردد: داده‌های کپلر نشان می‌دهد میانگین عبور کشتی‌های حامل کالا از تنگه هرمز در ۱۰ روز گذشته به حدود ۱۰ کشتی در روز رسیده که پایین‌ترین سطح از ماه مه است. همزمان ایران اعلام کرده قصد دارد یک منطقه ممنوعه جدید در نزدیکی…</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22473" target="_blank">📅 08:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش صدای انفجار یا پرتاب موشک از چابهار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22472" target="_blank">📅 08:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رویترز , تنگه هرمز در پایین‌ترین سطح تردد:
داده‌های کپلر نشان می‌دهد میانگین عبور کشتی‌های حامل کالا از تنگه هرمز در ۱۰ روز گذشته به حدود
۱۰ کشتی در روز
رسیده که پایین‌ترین سطح از ماه مه است. همزمان ایران اعلام کرده قصد دارد یک منطقه ممنوعه جدید در نزدیکی تنگه ایجاد کند؛ در مقابل، عملیات دریایی آمریکا همچنان فشار شدیدی بر مسیر صادرات نفت ایران وارد می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22471" target="_blank">📅 07:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UURrQcj1POn93oc7k4A0E950mUEBIQ9h6xBTRZ60jsBrUCKhJykXG1gLsRdHrQNDFEnltsbwCkbd1Wu54qeg7Ni1H35GV6DXhqQypVK9DIsYm1wNW0KpPaaf_LfzawkzecbQ6zzVCo1P7GH5_opGn3BAxMGHTvXdksA6ca97GB4OJYqf_FpQ3dyBx-9wTBxJO2AElpFt83cHFNIQFlLeMKI7g-7CAbuXW3cVdJqAg1mSBK9tdS9GBSx_wqro-sWo_6IRp9_RcmdtH-_52vx--fsG-SkRnB4REpmrsY3Qfzgz42jfPbKVPROV58bZTXnkt7ytXUaH5y_9W3yZDAe19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : سلام یاشار جان امشب اینو دیدم تو خیابون تهران رو زمین بود ، به نظر از این تراکت ها تو تعداد پخش شده باشه تو شهر ، آخر این حکومت رسیده و جشن آزادی بزرگی قراره بگیریم
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22470" target="_blank">📅 00:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1RN04wOKbpKauLU-NzsQLlKZ4du3mZlC6RjvY-e0xOVc7vIIOPMDQF8xb7kaYrBbftx0hV5oKUESCS65ls2-EYb7WY9n5kYQ3dAtl6g_99DNQKYtz_ic7HABwEifz2PmOi56tH9517Yz2Gp9qnqJkdFkl2rqcOtNs5Cdmh12ZK2LFzCiDJg2WEj1VyH0y_lKX5R2qjxOQQ0hgyKCbrrY5TflAitaKsz_FcHpltnZuSeFsF7cpeY96ZIgDIeikpfrqlIlr-uG25gx48BXYah1Z038tUA4V2EBaU0vby8bY_5n-A4XeBSuQREDxGySic1d0kQb2Pr8bFYexxxF2hVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنی که جمهوری اسلامی او را «شاه‌مهره» می‌نامد، اکنون در زندان قم جانش در خطر است، برای نجاتش کمک کنیم
نازنین برادران، معروف به
«رها پرهام»
، پس از اعتراضات دی‌ماه توسط اطلاعات سپاه بازداشت شده و بنا بر اطلاعات خانواده، اکنون در
زندان قم
نگهداری می‌شود. رسانه‌های حکومتی مدعی شده‌اند او
معاون و دست راست بیژن کیان
، رئیس اندیشکده «صدای آزادی»، بوده و برای
هدایت اعتراضات و اجرای طرح براندازی جمهوری اسلامی
آموزش دیده است. آنها همچنین مدعی ارتباط او با
آدام لوینگر، افسر سابق پنتاگون
و دیدار او با
تام کاتن، سناتور آمریکایی
شده‌اند. نهادهای حکومتی همچنین می‌گویند او در تدوین ساختار حقوقی دوران پس از جمهوری اسلامی نقش داشته است.
اعضای خانواده وی به من گفتند که او قانون پس از براندازی جمهوری اسلامی را نوشته و آن را به سازمان ملل برده است.
اعضای خانواده وی می‌گویند
او از نخستین روز بازداشت ممنوع‌الملاقات بوده و حتی اجازه تماس تلفنی و شنیدن صدایش را نداشته‌اند
و اکنون
کیفرخواست پرونده‌اش در حال صدور است
. خانواده نسبت به وضعیت و امنیت جانی او به‌شدت نگران هستند و خواستار توجه رسانه‌ها و نهادهای حقوق بشری به پرونده او هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22469" target="_blank">📅 00:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZ3f6pXxDmbUjJ43c0Gr_-4lcRd3E5NRKgzoYlPOyGk5B84kl5Hcs5FqfHhqk3kmZ3Jr_uXCIPe7JQXvGKejv69787m3QDZnYOUOrjYYepJWinqdZXbgNwV6LesUBpoX5RkE7varbPSBUqjp90ElyI0gtayLjOi95VqMdsagB7U1z248UA2fmNqoKpgYxznC19Dhspvj4CEljbm1EDvUloPkd4IxFBvvklYxa0e21-crTMvDZ7_0VUbcre12zbuAAqUNdj1Tw0GRdoUbuSkL5GiZcDflefu16B0sFmwViTutKag_INQP_SqPrgUyDmj6drIkLVjXwmvv2WMmNPpS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند. @WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22468" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22467" target="_blank">📅 23:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FS9TEBHYNiuDcOlTrAp9pHGnoZFOIiHUjPoJr88aHvZBCfRd2GEnmCpTrO7x_X3xLwl9hpWrZq8JxmirY--d3dy-LauNujZKOh50NemOgBAmLb5dN7Zlv6u7iwiwG82TdVN-Y24n1PJzW3Xc7zktprYpZlWPEi08pyjSNMNie6JdLxykxgqN66-yeJy7N9rMLfaJaODKkxiasm8MoXw0F6mPSFVSWTFahH4z2RF3u6CZg7frA8_2sgTRacirLwOEgIqrUIQkCB9QrVHX5zb5I6kZ9Vt1DVoXOrWwbaT83xS_a3_iF0bdMvXJu9nfAHV40Y5qThfc_hrjQYvuMOi3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران کشوری در حال فروپاشی است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22466" target="_blank">📅 23:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_Cf_lsHnf74rHu7jHuKWDUfhc9iYMb6-zW2FoIFzvlSUU8LB0tGYC2hoyFY_aSA6yIerffWYllXWm9xLJevURJ9PmU1DTSxmfNi_fOfnjuHbetRe5MTyqbXLm4txaU44vlcsbwNGR8-HCP9YggwhZG7LlcglxdWcBCNYFzkk5JKzgndS62zZFJu0suqhT8wGGue4u6sGrghGYDx5K_lq_p3Gdwwf-CgRdBeO5FoXY1lr2bSpEIXFuK_e9F-RctzFyhFm4fn5R98SAleDmqwx66GcCIFrxWtYtGzUaAmvCaHaypIJTWQotullT3u9f8GpIds5X-41Er-Q-b-RfirFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : حجم نفت هرمز برگشته است!
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22465" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJxc1ZyUA4CAziBI8NfUfygQiiVpAXA8y6n-K3DcYQkFYKh41QlEL88ybUCkckmqehacfqJHX1sdEXlqXniyEv-KaFKhH7-k7iCH1HRl_U6X7DkPXecXuaTigBAD0Y2oGFmGIQacuk4d6Dbz8gH1E86NYBbl0GOCgEuLeK6Q-R8b-o7k70JF3z06hcD5hM3oO3CHblEVK0HCrAw9tExAmvhgz_Ts-rsixi5t7iCZjnFL5HCLN4UkvW7zxrO3U2CVgiI5Sz1KZFQZUEeBNkY0E3yKCckzTv36tgFho_ZthE1V4V-_0zCkv3E5X2qtkpmA0tKkHzSvpyolIgbsk20RDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : کابوس برایشان بساز
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22464" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hT-b_NcPs7HaGPNl3DVGzViZ_25FPZZ-j0SHfPh5GpQA9JI4Qegq0KDne5wZsOBvibh9UrqM3EH5rbIl2amvMTOW2QYTflATqnrb1Htxl7nkKrLxi7poipkoRay1jPdXODNTzTX8LVVHKFbdsa6S8ohtHQZXho8zBPSyQpG_7901TM9jbD-bNGFPSYhjnRrGJd8-IYvI71zEOWTmxZBAKhImgGWxHf1rryHkxisu28gh6mesWCyltn49i7QVkatO7C74Srv3UH83M3J0NlwYxaKUggiDRh7zVkWiJ99cfhKQka7z37iZesn5inMKYO2afw6Fw3CkWyT2I0-mHTDAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : صادرات نفت ایران در حال سقوط است
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22463" target="_blank">📅 22:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uepCQAKc6TWHb6H6VBqdr89GApmNQZRN437RvZzpOfkGMR6KviFDCaxv7zhSnQCQC6PbwG7zxnVRcN70Y8JlQMqr_AsUnT5UbKyCs5v9xk2kTD8CV11R5LOqLjqduzC-jZrH8iYoRFkoHHfPXnrSYY55rdN-TxRENh87_ojXqY4sGxG_x1TrQdUuYx2YmeJT1Sqh3Ax0dQZ7Cgl6icXqCv0x9Qfx71PLMQ33lZKIT_LQuUa6IY_9J9lRyCAx6fMbcR-ypBCmFdwet-GvmFlnS86Dcx6amIHtU7ZameWKYmgkdtzh-goTHiiKAC5B8xKttqv4hxT75P0lLPJu30hbQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
ایران دچار ابرتورم است
پول ایران نابود شد
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22462" target="_blank">📅 22:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv4rYNxVRJnyC-KLJEwbPnKMetULhMbIkXHMYD6-qyHC-DwwyPRCyGC6UgcPAUQWdw-VBBXsciUotRPvzLhJ1tKz_Gj2vghenXbZR54GPGKfw0zFvcuLDIsRs8FV2dcJ-6b0tcZP1WtYcDtX4hCZ5r-doPf7GSoquLmrFbtkQAVRgEOVUCTQnNsX42g49aASFbCfWXaUs5E_XNVbwYlBiCq9U8UbLlcO7C2l19hVLmHAI25Tvhm2Bz5mc7qc_8h35ta2-PZpnvT-MjX-fQaykQPLxEJUogOz08B9JTT9oU_bFCCBXWb8jARSSK6tLeUHQP2mhmN-qHDceh5B3pyxog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : خداحافظ خارگ
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22461" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ارتش اسرائیل پس از شلیک دو پهپاد انفجاری حزب‌الله به سمت نیروهایش در ارتفاعات علی‌الطاهر، موج تازه‌ای از حملات را در جنوب لبنان آغاز کرد. اسرائیل اعلام کرده
انبارهای تسلیحاتی، مراکز فرماندهی و زیرساخت‌های زیرزمینی حزب‌الله
را هدف قرار داده و برای انهدام دو مسیر زیرزمینی در زیر ارتفاعات علی‌الطاهر نیز آماده می‌شود. همزمان گزارش‌ها از
انفجارهای شدید و درگیری‌های سنگین در منطقه نباطیه و اطراف علی‌الطاهر
حکایت دارد
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22460" target="_blank">📅 22:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr7k_9rmocjQQXRg13MfqnTcG9qGR5nfj30eNRMkBPqFz256glFsHUwj2Nmgfaw41TxCP2eG31rb4h5xeNTSKotluG2y8nR_sGYhtUS2xOm61CYVGpZz-cSwYMmI5IgPpo9xjEehfRFdrPVLz-1po1MmhJWBWNwpEeB0iwwogHnEW4YwZGw-v9aE3O-zvKOR-deWpV9n0rskBNLq3rnaSx1Jfp2lqFr0aa1R_ob4zQtT8OKcmd1FhloKHp4fVsS6fO07fvs5ms6BnNiMzcaDe4tPcNG7qBwrIZkI5xoFJiMKbBN2uareOdsFObsh8el5U3i6WJMJFtgMRfyOIoyrtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: نقشه ایران رو برعکس کنید میشه تصویر من
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22459" target="_blank">📅 21:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22458" target="_blank">📅 21:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رژیم:نرخ سوم بنزین تغییر کرد/ سهمیه اول و دوم بدون تغییر
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند. افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22457" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کان نیوز:
ارتش اسرائیل قصد دارد
شبکه تونل‌ها و زیرساخت‌های زیرزمینی حزب‌الله در منطقه علی الطاهر در جنوب لبنان را به‌طور کامل منفجر کند
و بر اساس گزارش‌های اسرائیلی،
در انتظار تأیید مقامات سیاسی برای اجرای این عملیات است.
گزارش‌های پیشین نیز از آماده‌سازی مواد منفجره در این منطقه خبر داده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22456" target="_blank">📅 21:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22455">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22455" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22454" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin</strong></div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22453" target="_blank">📅 20:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتانیاهو: ما مصمم هستیم که مأموریت سرنگونی رژیم ایران را به پایان برسانیم.
پایان جمهوری اسلامی نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22452" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee397b868b.mp4?token=TjCxydZPTJkR1mzSABiOYg-0QLTSVPNH-T0vyVUgslyHWnQIrQPsOQsquka0RE7dOL-lPSZtsheL1fA7V_kx6RSfwSeAItaeQx-8t3A6gvCWgggaSeMOFD4JmnAuzAYD10er3gabXPYLwiVe6yaJvGimAe6U6JC5TI6ioJ1IDBIxoBQEbiW81Yx_e94exUETJQZMXjIbjHaL12kmg6VPF0mukBusHzeaymd1-D6iuHYwTnD0PdrlItctd73lOeunpLgSFuNyDZLcnL1R4qdNpn6PSc2IGoyavxMSXYXI0aYuybhgdn_JZn-z_aeFAp-sVg2lsNOPUXwoOOVkIjAfgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee397b868b.mp4?token=TjCxydZPTJkR1mzSABiOYg-0QLTSVPNH-T0vyVUgslyHWnQIrQPsOQsquka0RE7dOL-lPSZtsheL1fA7V_kx6RSfwSeAItaeQx-8t3A6gvCWgggaSeMOFD4JmnAuzAYD10er3gabXPYLwiVe6yaJvGimAe6U6JC5TI6ioJ1IDBIxoBQEbiW81Yx_e94exUETJQZMXjIbjHaL12kmg6VPF0mukBusHzeaymd1-D6iuHYwTnD0PdrlItctd73lOeunpLgSFuNyDZLcnL1R4qdNpn6PSc2IGoyavxMSXYXI0aYuybhgdn_JZn-z_aeFAp-sVg2lsNOPUXwoOOVkIjAfgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جرد کوشنر: در دنیا چیزی به نام دشمنی ابدی یا دوستی ابدی وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22451" target="_blank">📅 20:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا، در مصاحبه با
مارتا رادزاتز، خبرنگار ارشد ABC News
در برنامه
This Week
درباره ادامه جنگ و سیاست آمریکا در قبال برنامه هسته‌ای ایران گفت:
ممکن است دولت ترامپ به توافق هسته‌ای با ایران دست پیدا نکند و در عوض، توانایی تهران برای دستیابی به سلاح هسته‌ای را از بین ببرد.
رایت تأکید کرد هدف اصلی آمریکا جلوگیری از هسته‌ای شدن ایران و کاهش توانایی این کشور برای تهدید منطقه است و گفت
اگر توافقی حاصل نشود، گزینه نظامی برای نابود کردن این توانایی همچنان روی میز خواهد بود.
او همچنین گفت آمریکا در حال وارد کردن
«درد کوتاه‌مدت»
به اقتصاد و بازار انرژی است تا به گفته او به وضعیت بلندمدت بهتری برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22450" target="_blank">📅 20:32 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
