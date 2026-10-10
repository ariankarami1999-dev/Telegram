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
<img src="https://cdn1.telesco.pe/file/a715VvXRqz1aAMR37DNmeGwscV4oY8t2USIO-SkTnIOsY7tWsCOQRN03jh8U2wT0yBNnycmPPZWpg7WGjIoyoCkiBi2f0hIJYAG0PDZwAUcMPCBXweCx_A-QHDGQ1tEHpcfh-2jg1---O27IeQePcXJ_MSPFs2K6Ddu4yYuk42hGBXvxB48oOVP7Ib23pCz72JzVT5eundhqpY5nSCDkELqDh1d33rqhw29cI20_HMP1Be9ZnyfYz2dtLfNAw8jrfntCqUEhXJ2R7QnQtZ5Az6sxSx3Fh-WasdMiGVbRN9bOwNYYkx7D5gAHqqpW5iHeqnhCtM1s7LkIw-T4bOmSdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.39M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی می‌گن. اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جوری که می‌خواستم به خودم نشون داده بشن می‌گذارم.ممنون از حمایت‌های ماهانهvhdo.nl/patreonیا گاهانهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 03:38:05</div>
<hr>

<div class="tg-post" id="msg-78679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRsKrUT8tNB87DKRiQGWyB9vJP59i2HXetNYfWz7MKMTfKX5olO8LJhvvEC90RF1swndWoyDbgrPx2MI5NZ8vDk4Vzj4UZEmghIkrTHFtKnplOaLveaBfy5erxqWlDEiWwag5jEeIIdXRdgEQt39Fu6o3R6ebAQNGp7DVGZ94FydReDBEj2p00vPxfyrzGFjRA5kd5iWHIFqGzzpWoAoUyW3VRqUnny__RNXGKIqQRKbuaLEVUswkZxsqHvdbE20NPsYEpFMca2Awd8xmkBgMBn5PJivP0tFtT7JrtMiGOCSlG4UjQV8yC9Ymc7XAT67RT-psT0d_BMomAnlZB-0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در شبکه اجتماعی تروث سوشال اعلام کرد کنترل کامل آمریکا بر تنگه هرمز، همراه با توافق تازه واشینگتن و مسکو برای عرضه میلیون‌ها تن گازوئیل روسیه به بازار جهانی، باعث کاهش سریع و چشمگیر قیمت این سوخت خواهد شد.
ترامپ گفت پس از گفت‌وگو با ولادیمیر پوتین، رییس‌جمهوری روسیه، توافق شده است که مسکو بلافاصله بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و جهان عرضه کند و ۵۰۰ هزار تن دیگر نیز در ماه نوامبر تحویل دهد.
به گفته او، روسیه پس از آن یک میلیون تن گازوئیل دیگر به بازار عرضه خواهد کرد و با توجه به وضعیت پالایشگاه‌های این کشور، سه میلیون تن دیگر نیز در مدت کوتاهی تحویل خواهد داد.
رییس‌جمهوری آمریکا گفت کنترل کامل تنگه هرمز از سوی واشینگتن و افزایش عرضه گازوئیل روسیه، قیمت این سوخت را برای مصرف‌کنندگان آمریکایی و دیگر کشورهای جهان به‌سرعت کاهش خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/78679" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=g-QjCuVmWaJzOYXp4c5hDuDqr-44qwYt5V0MLGE79FYEG8mYPhlzP7GO5HIaFJy90Xqje3ST2quFh2Gkqi3UBGMxjUAO0atYYMsbPBfnCqPNEC2hpSL-byWo_w8hPwB7kqjfMRoAJXfnKxOreU6O4t8WmNDKc9cAt_qE2_5QvKFbfrGiBixMvMnABLPAGaI4J-c8QDNvjRsAZtsSTBcjgxMOc2cul5KnoTX5HEzNXLJerd2O_k5UzK1VeCovo057bNZUXBeeu89Rn9VvW5Oodl-YtJnAYenEwqoGpMUrBb4gEIRJKqauUTUzr67Sbh1x9Ibs9iWIREWV5aYOagt5bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=g-QjCuVmWaJzOYXp4c5hDuDqr-44qwYt5V0MLGE79FYEG8mYPhlzP7GO5HIaFJy90Xqje3ST2quFh2Gkqi3UBGMxjUAO0atYYMsbPBfnCqPNEC2hpSL-byWo_w8hPwB7kqjfMRoAJXfnKxOreU6O4t8WmNDKc9cAt_qE2_5QvKFbfrGiBixMvMnABLPAGaI4J-c8QDNvjRsAZtsSTBcjgxMOc2cul5KnoTX5HEzNXLJerd2O_k5UzK1VeCovo057bNZUXBeeu89Rn9VvW5Oodl-YtJnAYenEwqoGpMUrBb4gEIRJKqauUTUzr67Sbh1x9Ibs9iWIREWV5aYOagt5bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی درباره صداهایی که نمی‌دونم این بار هم آتش‌بازی بوده یا چی:
سلام وحید جان شرق تهران صدای پدافند و انفجار ممتد
صدای یک انفجار و بعد چندتا پدافند شرق تهران
وحید تهرانپارس صدای انفجار شدید بعد ضد هوایی الان ساعت ۸/۳۰
صدای شبیه پدافند یا تیراندازی در تهرانپارس شرق تهران
سلام وحید جان خوبی
پدافند تهرانپارس 5 مین  کار کرد ساعت  ۸:۳۰ دقیقه شب
وحید جان شرق تهران صدای تیر اندازی اومد الان
دود هم دیده میشه تو اسمون.
آپدیت:
دو ساعت بعد دوباره شرق تهران:
صدایی شبیه به تیراندازی در محله مجیدیه
ساعت ۱۰:۴۰ دقیقه ۱۷ مهر
چند دقیقه بعد: دوباره اومد این سری انگار رگبار بود
سلام ساعت ۲۲:۴۷ صدای تیراندازی چندین بار. مجیدیه شمالی‌
چند دقیقه بعد: الان هم دوباره اومد
صدای پدافند شرق تهران
سلام وحید جان
صدای پدافند همچنان پست سر هم
مجیدیه
صدای پدافند
مجیدیه
سمت مجیدیه تهران صدای تیر اندازی و پدافند میاد
صدای پدافند میاد
دولت کلاهدوز
سلام وحيدجان سمت اختياريه صداي پدافند مياد ساعت٢٢:٥٧
صدا پدافند سمت پاسداران
چند بار شلیک ساعت ۲۲:۵۷
سلام صدای تیر اندازی شمال شرق تهران ۱ دقیقه ممتد اومد الان قطع شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78677" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78675">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NHnvsZ2EwrVppUvlMg8ZeJ_5VZ56mVRrccWmKvqO9NZI_gXVK50cYGt8_vuj-THL484IHOILhG3YFhEnuE3DG5T6otYf8yNLDTjquD22p3vQcTxpWO33uijPzsNE_yFBu1Cm7ivWuYKMKbavsuKd9vJgx-JlTauDxtKZdy2Qm1b5IEdLXDwAZ_T_iLZhSdiT4uSBzKG6Q15h6hPtCaO87pniPBZRv1KLZ2ZldxgK5puEdo7UFqT8h6OKFhrUWyeZqf_Z-RqY7LiB67Ajh3vyb4uJjIdRhxVYpv9Chqp7wRyvJKY8Zqplxn61aLZHjEVI7mutS_QHQCvuOYcMOKJPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f20c8d9bec.mp4?token=V9PV_qFyHBA2Nb9ssCqyH0HWePJrEgO1SbXbVs1KElE1Zk0gGeA4SfjEjwsii7uENsdczhWTn3DdIg9oOQhHFrLaMYSjEEaLTxD_ZNgrwxh2WWiqkZFet-lUM0FADdw6PHS-dOXNFBz0vwcuE4WIysloAeYnEgbVxtykZRujj8_WHtG4HtLoDMq_zDdbTHFcthya8Y3YJTWG_hIRlfvBLq_N3x6HNxze0NB_m1sanLf3pSbOoJi86ia10S-OWfBF9q_vcWjVDbwHIKhpf2Q9iRBNR77JZt72u_CaMm-RaeKvFvelQRe0OulrqF7y9DRJKKi3TFLHZEZswZd8_3MfOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f20c8d9bec.mp4?token=V9PV_qFyHBA2Nb9ssCqyH0HWePJrEgO1SbXbVs1KElE1Zk0gGeA4SfjEjwsii7uENsdczhWTn3DdIg9oOQhHFrLaMYSjEEaLTxD_ZNgrwxh2WWiqkZFet-lUM0FADdw6PHS-dOXNFBz0vwcuE4WIysloAeYnEgbVxtykZRujj8_WHtG4HtLoDMq_zDdbTHFcthya8Y3YJTWG_hIRlfvBLq_N3x6HNxze0NB_m1sanLf3pSbOoJi86ia10S-OWfBF9q_vcWjVDbwHIKhpf2Q9iRBNR77JZt72u_CaMm-RaeKvFvelQRe0OulrqF7y9DRJKKi3TFLHZEZswZd8_3MfOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، گفت اگر حکومت ایران به سلاح هسته‌ای دست می‌یافت، ممکن بود پس از حمله به اسرائیل و دیگر نقاط خاورمیانه، کشورهای اروپایی و شهرهایی مانند لس‌آنجلس و سن‌دیگو در آمریکا را نیز هدف قرار دهد.
ترامپ جمعه ۱۷ مهر در مراسم روز کلمبوس در کاخ سفید گفت جمهوری اسلامی پیش از حمله بمب‌افکن‌های بی‌۲ آمریکا، تنها دو تا سه هفته تا دستیابی به سلاح هسته‌ای فاصله داشت.
او گفت در صورت دستیابی جمهوری اسلامی به این سلاح، حکومت ایران به‌سرعت از آن استفاده می‌کرد و ابتدا اسرائیل و سپس دیگر نقاط خاورمیانه را هدف قرار می‌داد.
رییس‌جمهوری آمریکا افزود کشورهای اروپایی احتمالا پیش از آمریکا در معرض چنین حمله‌ای قرار می‌گرفتند و شهرهای لس‌آنجلس و سن‌دیگو نیز می‌توانستند از اهداف احتمالی باشند.
ترامپ گفت: «دیگر لازم نیست نگران این موضوع باشیم. آن‌ها به سلاح هسته‌ای دست نخواهند یافت.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۱۷ مهرماه در مراسم روز کریستف کلمب در کاخ سفید، با اشاره به درگیری‌های نظامی با جمهوری اسلامی گفت که این وضعیت به‌زودی پایان می‌یابد و قیمت سوخت نیز به‌شدت کاهش خواهد یافت.
ترامپ در سخنانش با اشاره به عملیات نظامی آمریکا علیه ایران گفت: «ما مانع دستیابی ایران به سلاح هسته‌ای شدیم.» او افزود که پایان درگیری‌ها از راه‌های مختلف امکان‌پذیر است و تاکید کرد: «به هر شکلی، این وضعیت خیلی زود پایان خواهد یافت.»
رئیس‌جمهوری آمریکا همچنین درباره توان نظامی جمهوری اسلامی گفت: «آن‌ها نه نیروی نظامی دارند، نه نیروی دریایی، نه نیروی هوایی و نه تجهیزات پدافند هوایی.» او در ادامه با اشاره به محاصره دریایی اعلام کرد که آمریکا مسیر عبور کشتی‌ها را مسدود کرده است.
این اظهارات در شرایطی مطرح می‌شود که واشینگتن هم‌زمان با ادامه فشارهای اقتصادی علیه جمهوری اسلامی، محدودیت‌های دریایی و تحریم‌های مرتبط با صادرات نفت ایران را دنبال می‌کند. تنگه هرمز نیز به یکی از محورهای اصلی تنش‌های نظامی و اقتصادی میان دو کشور تبدیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/78675" target="_blank">📅 20:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qsR-qqaJNaJP1QpEfFUkBcnzbsusCx1ZOE8tGDfaLaa9xsWx9irMD8e-BAEcXX5crTeg11eud3xuYi27qNE1iECnk7Rlk5lB9mN1vIjZr8i5FgcyDsR8ySv09WXMGEKVDe8IQpz-z9Q_rd0vsheKjhTFmz9pMWmPdnMb7DEDl5mTZeyUoE6vhwW2F1VZOUVb3f3s7RGw9SamjYGquLb7axsbD7onFTQdvEG8BUnVMUYK6t38rSdeMcLK0AmNE17ArXdxbnFmPzqp1go1LFeS1RfA6kL3Yr0mSb9bFmPe9SmnV26rjbBJPm-UfMy_GHZYLpkrptquyWyx9EK1NjH4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صداوسیما با انتشار گزارشی اولیه، از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای انتظامی استان سیستان‌ و بلوچستان خبر داد و نوشت در این حادثه نصرت افتخاری، معاون اجتماعی انتظامی استان سیستان و بلوچستان، در منطقه چشمه زیارت زاهدان کشته شد.
این منبع نوشت عامل اصلی بمب‌گذاری هنگام فرار کشته شد.
خبرگزاری فارس، رسانه وابسته به سپاه پاسداران نیز گزارش داد این حادثه در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان رخ داده و چند نیروی پلیس در جریان آن دچار جراحت شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78674" target="_blank">📅 18:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e9Z7KqMQDjYWGUJV5doF3xQwDFHP0wKOp6qumPokCnH300EaJkJDDxBdwclbTLkDG0CWBRwnQ0Z3ur0VVOm9H38ZgKJOxJTlsr53Ll0X7Gw4z3nVIQfes8LJw_wJK0BJWnXbi2RTzSFJjYDVL3DuLVkQ7fMVkC7Wual8NE27u-TwMG1uTPxCKKBHGqkK3tsLKvRco_XIMRsCo-p0dFehYxTTIO6FnMgwVj3OddSjGCjp6CNtTCqCw_Ub8O0omfLJGyafpKH5wFJYRAbRWZdF101BoF1kyYbqvQVxf567JoMXc_ZagVMavrWSr6ruMuS4QT6qzfI3pc9_726HgsGTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران،  اعلام کرد یک کشتی حامل گاز مایع به‌نام «ان‌وی سان‌شاین»، متعلق به شرکت نات‌ویت را هنگام عبور از جنوب تنگه هرمز هدف قرار داده است.
سپاه پاسداران اعلام کرد این کشتی در حال عبور از مسیری «غیرقانونی» بود و پس از اصابت، موتورخانه و سامانه رانش آن دچار آتش‌سوزی گسترده شد.
نیروی دریایی سپاه همچنین اعلام کرد کنترل تنگه هرمز را در اختیار دارد و اجازه حضور نیروهای نظامی آمریکا در این منطقه را نخواهد داد.
سپاه پاسداران در این بیانیه اعلام کرد شرکت‌های کشتیرانی که با آمریکا همکاری کنند، با تحریم و اقدامات تنبیهی علیه شناورهای خود روبه‌رو خواهند شد.
بر اساس این بیانیه، سپاه از این پس برخورد با شناورهایی را که از مسیرهای غیرمجاز عبور کنند، به تنگه هرمز محدود نخواهد کرد و این کشتی‌ها را در سراسر منطقه هدف اقدامات تنبیهی قرار خواهد داد.
@
VahidOOnLine
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)، روز جمعه ۱۷ مهر، با انتشار هشدار جدیدی اعلام کرد که حادثه‌ای در ۱۳ مایل دریایی غرب راس‌الخیمه در امارات متحده عربی رخ داده است.
بر اساس گزارش‌های دریافتی از منابع مختلف، این شناور مورد اصابت یک پرتابه ناشناس قرار گرفته که منجر به بروز حریق شده است؛ آتش‌سوزی مذکور تاکنون مهار و خاموش شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78673" target="_blank">📅 16:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAoKWwp0-xEwyXITGwwoUXFt5E9nfxdM_Y5FFekKzkcb0GEO7AWBli0rnsF0P23pLJSYLRSBkLEoxzOPrsQBihi_yacNk9nDnXxO0d2AygLTF_vTTSJeZB6Gej9pwMtPROkWDUap4wjrMXZeWPG8bh9B9xpXiLAyZ2pua_756kG4YWsmYA9camw5Xnilw7f-M-pC68ynOMRMqiWCIv1fp2p6okro4RuxNKNZqJmhwm7kMW9MzxIIafmHGzbGY3KLDGneEXL6EF2_pHzQT4p8FFPThabQ9qHGVePZSCfYY-xsK3WEfigeu5pPp2s5xBPmo6t3bUrPQQH383FPr92CZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه‌های نیویورک‌تایمز و وال‌استریت ژورنال در گزارش‌هایی از بررسی گزینه‌های تازهٔ حمله به ایران در دولت آمریکا و تقویت حضور نظامی این کشور در خاورمیانه خبر داده‌اند.
این گزارش‌ها در حالی منتشر شده‌اند که دونالد ترامپ، رئیس‌جمهور آمریکا، روز پنج‌شنبه ۱۶ مهر اعلام کرد ایالات متحده پیش از انتخابات میان‌دوره‌ای سوم نوامبر به ایران حمله نخواهد کرد.
نیویورک‌تایمز به نقل از مقام‌های آمریکایی گزارش داده است که ارتش ایالات متحده در حال تدارک گزینه‌هایی برای ازسرگیری عملیات رزمی گسترده علیه ایران است و پنتاگون به دستور آقای ترامپ طرح‌هایی را برای حمله به زرادخانه‌های پهپادی و موشکی، تأسیسات انرژی و دیگر مراکز نظامی ایران تدوین کرده است.
به گفتهٔ مقام‌هایی که با این روزنامه گفت‌وگو کرده‌اند، تیم امنیت ملی رئیس‌جمهور آمریکا و پنتاگون در ماه‌های اخیر پنج پیشنهاد برای انجام عملیات‌های بزرگ علیه ایران یا حوثی‌های یمن به او ارائه کرده‌اند، اما آقای ترامپ هر بار این طرح‌ها را رد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78672" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFhVAtP_kQN1xYwK_Uxmp7j79VYwRX3mSgyAgtFqMFcr7OXYYo3BLQoJSp6eIv9rs5jrE93lSD0Ars6FqG-akUrplydMxqtt0jVfHIe6DN7wVOYPuAJMUNVfH225C69QDF4K-2tnT1mHVrvWo4ZO2JQSR4oaiPGyVZ6_PEmleubDFV6kDVvt9mGbypgcebdDQEzYShdRZ0_TqXSeYGXgNOBoGboF19TMRYyRgmHi5ID51NRymZT4IWu5Td6fx5yeRV1iXDnbD6I4Ivfx5gQ6V0NuA1hhqTrvcZDVeNxYG-qORO_P6Am4SZWV4dcOpUL7jVQOVbR8ADrgHoQ-mGNyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت اوپن‌ای‌آی اعلام کرد حساب‌های کاربری مرتبط با یک عملیات نفوذ رسانه‌ای با منشأ ایران را مسدود کرده است؛ عملیاتی که در آن، گردانندگان با استفاده از چت‌جی‌پی‌تی و هویت‌های جعلی روزنامه‌نگاری، نزدیک به ۱۰۰ مقاله درباره جنگ ایران و آمریکا را در حدود ۱۲ رسانه اینترنتی در کشورهای مختلف منتشر یا بازنشر کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/78671" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vko3ajRIb5TfEmlO8P0xc8Mjfc4BaPlugPG5nhklwviSbVoBNhdNQ2cMps8NElqvMQ_iFZQaX4bzXVoGU9Qk5CWkCmNytG38MPHBu3tqecR5ziNd9cOgutkzgjB9_-oASIcjhUlYT9BmZGDFi5aj99NOav1xMWMucdds2GWt91wF4ysz2J67XW1aBmUo1-9A0I9QRl3hZH0gevWKR9bZL2iPozpuOd6KQmc6u9Ax7RueXV6kA8YUKbnZPJOr4BeOmvlA7fEmmp9U7WkrSiyv__N1JwKHoSEdJZLAcCIYgOkOALtStZOiN0GWVd_0CcH8GLQ3C6WwcMv4kbPsLjVa4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد واشینگتن احتمالا تا پایان هفته حدود یک میلیارد دلار دارایی رمزارزی مرتبط با جمهوری اسلامی را مصادره خواهد کرد.
بسنت گفت دولت دونالد ترامپ کارزار «فشار حداکثری» علیه جمهوری اسلامی را به کارزار «انزوای کامل» تبدیل کرده است.
به گفته او، این سیاست علاوه بر محدودیت‌های مالی، مسیرهای دریایی، هوایی و زمینی ارتباط ایران با خارج از کشور را نیز در بر می‌گیرد.
وزیر خزانه‌داری آمریکا گفت امارات متحده عربی و عمان در اجرای این سیاست با واشینگتن همکاری می‌کنند و دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن مسیرهای زمینی ورود و خروج از ایران است.
@
VahidOOnLine
اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتقاد از سفرهای خارجی مقام‌های جمهوری اسلامی گفت اعضای سپاه پاسداران دیگر نمی‌توانند برای دیدن «جراح پلاستیک خود در لندن، معشوقه‌هایشان در پاریس و پول‌هایشان در ژنو» به خارج از ایران سفر کنند.
بسنت در ادامه گفت: «اگر جمهوری اسلامی را دوست دارند، حالا همان‌جا گیر افتاده‌اند و می‌توانند از آن لذت ببرند.»
وزیر خزانه‌داری آمریکا گفت سیاست دولت دونالد ترامپ برای منزوی کردن جمهوری اسلامی، فراتر از تحریم‌های مالی است و محدود کردن سفر مقام‌های حکومتی به خارج از کشور نیز بخشی از این برنامه به شمار می‌رود.
او همچنین با استناد به گزارش اخیر نیویورک‌تایمز گفت اقدامات دولت آمریکا باعث ایجاد نگرانی و آشفتگی در میان اعضای سپاه پاسداران شده است.
بسنت افزود اقداماتی که واشینگتن علیه جمهوری اسلامی انجام داده، پیش از این سابقه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/VahidOnline/78670" target="_blank">📅 16:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a954e7da9.mp4?token=dJ8FKdJzj-8Ceia4tXpVByjF6amY7ryp1vbFzGvVJDUNaYcuUy3tR_Hre683RHC3hT-D8DNZ1uODP_Kggb3Huy3zfX4dWv4yqHJNR-p5D4F3sG1BJ1CDdPMRfjIUYKInhPocDq9IYusRocw6PKuAqikiqtYqR8cxtg63xZpBitalT-jmOvP__7obKZS1oz7Eghp_cv-8jkIY4Thqj0Y83AfVImdmXXz23Lr18PPoMwhAbGPaG27tSokmiW3_uQfH_FxLAwCbEevFQRnFvedKYvRnak7Xi7MYW1OlCOy6vkBmUbYPz2f2qBUq01Wja-5ZsWP-yY3h-LOXWdwS97JGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a954e7da9.mp4?token=dJ8FKdJzj-8Ceia4tXpVByjF6amY7ryp1vbFzGvVJDUNaYcuUy3tR_Hre683RHC3hT-D8DNZ1uODP_Kggb3Huy3zfX4dWv4yqHJNR-p5D4F3sG1BJ1CDdPMRfjIUYKInhPocDq9IYusRocw6PKuAqikiqtYqR8cxtg63xZpBitalT-jmOvP__7obKZS1oz7Eghp_cv-8jkIY4Thqj0Y83AfVImdmXXz23Lr18PPoMwhAbGPaG27tSokmiW3_uQfH_FxLAwCbEevFQRnFvedKYvRnak7Xi7MYW1OlCOy6vkBmUbYPz2f2qBUq01Wja-5ZsWP-yY3h-LOXWdwS97JGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان روز پنج‌شنبه ۸ اکتبر (۱۶ مهر)، با ولادیمیر پوتین، رئیس‌جمهور روسیه، دیدار و گفت‌وگو کرد.
این دیدار در ترکمنستان و در حاشیه دو نشست «کشورهای ساحلی دریای خزر» و «سران کشورهای مستقل مشترک‌المنافع» صورت گرفت.
پوتین در این دیدار خطاب به پزشکیان گفت «ما می‌دانیم که ایران تلاش‌های واقعی برای پایان دادن به این درگیری انجام می‌دهد؛ درگیری‌ای که ایران در آغاز آن هیچ تقصیری ندارد.»
پزشکیان هم در این دیدار به پوتین گفت «هر بار که [با آمریکا] گفت‌وگو می‌کنیم، دوباره حمله می‌کنند، ولی ما از میز مذاکره و گفت‌وگو کنار نخواهیم کشید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/78669" target="_blank">📅 16:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/imTEcfhPVWl2snjIsmPBQHzdnBwMpuvAQ4s1fE1lLJce5Hyc2LLPOU6bJ_Fo4HlD2tsX5AvJfDVrjksiQR_t6gMwVSQbo0cjb6omsLHRFbv6Tck56y_L5oxNL16issjfqGsToQF59rOU_OPuRLl7FJQNeh_qe0X9xeEjVkBTog80vu-UR4p3Bt2vBvA_oCjfIlkLcUw0zSXhhiH7VI7QtjYHWndmfjwYupCC6-6kTtJHgxvghMU38T8Pcf3x2qYlEUtSY-OJHUCDk_e3XxMglxJeB7nLRWECE2kQpwUfa3N1NH4hcMobkqtNBVLt39D8NhFVzgTyRzebcHNbQW3D0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OEBFsym3Ttuh5JsCQkWehDBsom87tfsewPvoVMe_CeVHEp8NWxiwuNKrEAGbc_FXGvmX8aOmlui1OyELpd0GuRVyHqxZMpTJ7-q1kIu01tN_y4p1F8JEmW4iL2VYd6dhFV8Y5BowSeyxjq_mx1pliA0_iJ67TW3iVnYwvZFwUzJyTduiDkxKd2KrxBlc2rmL5vEmoGtM8rUAorxQH4_V9NGekt-hLNxAR2pGeSf210oSVz8lEy3FWWyiR1HN8fq7Q9DoFf0v9dKXFim6PkORqZaY8JLyoAEQXNDAuz_x4Lf0oOlSXcrwxJMLEYI3VUbdUErcw6tCg56Mx83WgTCkUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی در بیانیه‌ای جمعه ۱۷ مهر اعلام کرد که در پی دو حمله به فرودگاه بین‌المللی ملک خالد ریاض در روز پنجشنبه، سه شهروند این کشور کشته و شماری از شهروندان سعودی و اتباع خارجی زخمی شدند.
بر اساس این گزارش، در حمله نخست، تاسیسات فرودگاه و در حمله دوم، یکی از هواپیماهای شرکت هواپیمایی سعودی هدف قرار گرفت.
این سازمان اعلام کرد پس از این دو حمله، فعالیت فرودگاه از سر گرفته شد و تردد پروازها به حالت عادی بازگشت.
شرکت هواپیمایی سعودی نیز اعلام کرد که یکی از کارکنان این شرکت در میان کشته‌شدگان بوده و یکی از هواپیماهای آن هنگام توقف روی زمین در فرودگاه آسیب دیده است.
سازمان هواپیمایی کشوری عربستان سعودی همچنین اعلام کرد که فعالیت‌های عملیاتی فرودگاه بین‌المللی ملک خالد از سر گرفته شده و تردد هوایی در این فرودگاه به حالت عادی بازگشته است.
@
VahidOOnLine
شرکت هواپیمایی سعودی (السعودیه) اعلام کرد کاپیتان حمود علی الکثامی، خلبان این شرکت، روز پنجشنبه ۱۶ مهر ماه در حادثه فرودگاه بین‌المللی ملک خالد در ریاض جان خود را از دست داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/78667" target="_blank">📅 16:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLKtauTwGiqJCNVkkYzAq058PfkeF-zuk27Lraew6q3aFAXMBDnYRBInPXUvz7Tgq7ecw6hDrY2wt0yXsUzkzwbOyUcLZTdeyhCL3Os9L91lOPlWV-iEQ0xwSbZt9QVecsGbS8mx0mh1oiaWW2z2utCvQ_3C93qsIUc6zDHn1qce96G0_H5E4lTKs3VErLbS7GUbP_4B5aUg5VD4RD-lbSuLouD5bHDDkVpqxcqzeEo9OkqixFYClFP6WOBVeSvPY8n4lO2C81UUbp6n5exbNaN9X4D2gKXePyBhb7ywP_pAnatFZt21lhOyXrnLBs7nB1U_-hGMrzdHtM5ah4U1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی از کشته شدن رئیس پلیس پیشگیری شهرستان فاریاب در استان کرمان بر اثر تیراندازی افراد مسلح خبر دادند. این حادثه در حالی رخ داده که طی دو روز گذشته چندین حمله مسلحانه دیگر علیه نیروهای نظامی و انتظامی جمهوری اسلامی در مناطق جنوب شرقی ایران گزارش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/78666" target="_blank">📅 16:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SrKCe5oDvy2h8Ol5d1BTXMuVsPNkNkvdbbZubKntFkobXcH--NiwDqE5Tij9cH3K4d19rGUk5671gBCCiSKp8yI0F0VnBamZ7SVmNR7TWYHHYeNOVlD_bT55B_dtuq_mYipRbPfkxX1OJL8MaGB1gIpEcVkTQfnlwtPNuMI0Anr4BY1NmLudhoIVUchlvmPRiHqh0yv2ioKiC0MK9bkgDtWJVPMpgiBmdQKC_CAe3VSqizUkvmEQCUEKr_5VHgPCvkbqqXBKwPcU6z_OJQiRJMHBgz_Al-fDAXY53YMRsqtKhS0EWdsWrf2hDCnBHQUiGQD0RN7l3AOqqT9WDuOJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترانه و رومینا رحیمی، دو خواهر بازداشت‌شده در جریان اعتراضات دی‌ماه ۱۴۰۴ و از متهمان پرونده موسوم به «میدان شهدای اصفهان»، در زندان دولت‌آباد این شهر به سر می‌برند.
ترانه رحیمی در مرحله بدوی به اعدام و ۱۱ سال حبس و رومینا رحیمی به ۳۶ سال حبس محکوم شده‌اند. وکلای آنان به این احکام در دیوان عالی کشور اعتراض کرده‌اند.
#ترانه_رحیمی
#رومینا_رحیمی
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/78665" target="_blank">📅 16:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78664">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFjdfJOeMDkZXmkUDcDAfkTn_M9BfnmtpgmaooW4X_30CtNyxN_k7PWSxed6UgCa6gNjLRlegzPG1a6bLhTKTsF2IlqobUd1mqjC-dvzci3c9wZsfrHo4thKeIes2dlbYHnQlO7PV-aaS22gIkBEEt2i5ZRF2ZTyovCTwV9Le2zk5s6daoJkPE78hbsmduDwyGhB3o52KawNRvYKTCckjjzG4c5VNfGU-SA3FKaQqrBxk5mR-oDMsUITlj2ONqKOUBjD87H0_OyIV6owvnqZSKpvDdbPdMeYJh3Xj1Pb0B-TcX79MZR0nOCrNzbj0NOUvwIwEWw3L91QsVjw63qasg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رسانه‌های جعلی و ساختگی دارند تلاش می‌کنند این‌طور وانمود کنند که من از دشمن دعوت می‌کنم سن‌دیگو و لس‌آنجلس را بمباران کند، در حالی که آنچه واقعاً درباره‌اش صحبت می‌کردم این بود که افزایش موقت قیمت بنزین، بهای ناچیزی است که باید برای جلوگیری از دستیابی ایران به سلاح هسته‌ای پرداخت کرد. و اگر می‌خواهید بدانید بهای سنگین واقعی چیست، می‌توانید تصور کنید اگر آن‌ها سن‌دیگو و/یا لس‌آنجلس را بمباران کنند، چه اتفاقی خواهد افتاد؟
تنها کاری که من کردم، مقایسه پرداخت مبلغی کمی بیشتر برای بنزین، آن هم برای مدتی کوتاه، با بمباران شهرهای بزرگ ما بود.
همه این را می‌دانستند، رسانه‌های جعلی هم می‌دانستند، اما همچنان بیرون می‌آیند و می‌گویند که من از دشمن می‌خواهم دو شهری را که عاشقشان هستم بمباران کند.
«حرف‌های من کاملاً روشن است، اما این‌ها آدم‌های پستی هستند و فکر می‌کنند می‌توانند مدام اخبار جعلی منتشر کنند و قسر در بروند!»
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78664" target="_blank">📅 23:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZFKakrn1qcAP8YQSWO4VCglaL3E7V2nuO9_WRmQnttIlVIm4OUEArZeZCz9nEMkq1Q2hrjzbAUj32CRlYyG2QWEpu0lJz-3tevfGMqzECnVLhhZjNmnUfRTLVNRybTeqQWkZl-vOjVGQJS2YevbWcumIGeAo8ReHqsyfCXLzbo-gkg4y8cX21_CdtJVDxT8ZFweDQvxYlC0g9jA1BarJ8WBPTRsUgLfuNTTzYLN250cnuzEuFkaY4I69FXWtVIzK0NrQvrqXeuyXfuAsYNwMQT8Sxgl2KXXGJDZaKyrm5rLiLVT6RVMWZz9hBdts65Olog5nizRf3uKh1b63sXby-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات در جریان است، پیش از انتخابات حمله نمی‌کنیم
ترجمه ماشین:
ما در حال انجام گفت‌وگوهای سازنده‌ای با جمهوری اسلامی ایران هستیم. می‌خواهم برای همه روشن کنم که اگرچه ایران هم از نظر اقتصادی و هم از نظر نظامی در وضعیت بسیار بدی قرار دارد و اگرچه محاصره همچنان با تمام قدرت برقرار خواهد ماند، در حالی که نفت با حجم بی‌سابقه‌ای از تنگه هرمز عبور می‌کند (تنها دیشب ۲۲ میلیون بشکه، بدون اینکه حتی یک بشکه از ایران آمده باشد یا به مقصد ایران برود!)، ما تا پیش از انتخابات میان‌دوره‌ای که قرار است روز ۳ نوامبر در ایالات متحده برگزار شود، در هیچ زمانی به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!
پرزیدنت دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78663" target="_blank">📅 20:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78662">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b534ce975d.mp4?token=sHiRrjFi-1nPZvUC7uxGjAf9ebT5BwUy4gRXYOgUwqxd3fq0Kv44eOMtRUnMeNtDY13MIr7Wv9mpKmARUVXOw1M5CNsfIiLCOx7pPklZnyB7olorMXePtrwHpQN56jRge3exXWlDuAx8Eci1VFr9qY4U_VD_Zzb0HuXwKKFLxuvXZoOwppBCB3mDgBvtkV3nzevUjRxcQz1oTbl53terLd7L_82_wW_AIe4UG-lnQJplqSdHkhMFij6StLSY2rSnv1IYKIHIAKk5Un3TJ0vkradUtcvMh84R0OuPYaSip3LjMTH6R26eqvwIVjFoEE_P-2fRtAhXzKR79KvllmJusw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b534ce975d.mp4?token=sHiRrjFi-1nPZvUC7uxGjAf9ebT5BwUy4gRXYOgUwqxd3fq0Kv44eOMtRUnMeNtDY13MIr7Wv9mpKmARUVXOw1M5CNsfIiLCOx7pPklZnyB7olorMXePtrwHpQN56jRge3exXWlDuAx8Eci1VFr9qY4U_VD_Zzb0HuXwKKFLxuvXZoOwppBCB3mDgBvtkV3nzevUjRxcQz1oTbl53terLd7L_82_wW_AIe4UG-lnQJplqSdHkhMFij6StLSY2rSnv1IYKIHIAKk5Un3TJ0vkradUtcvMh84R0OuPYaSip3LjMTH6R26eqvwIVjFoEE_P-2fRtAhXzKR79KvllmJusw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ گفت: «من باید در مورد ایران اقدام می‌کردم، چون آنها به سلاح هسته‌ای دست پیدا می‌کردند و آن وقت می‌فهمیدید مشکل یعنی چه.»
رئیس‌جمهوری آمریکا در ادامه با اشاره به احتمال حمله موشکی ایران به شهرهای آمریکا گفت: «ببینیم اگر آنها روزی به لس‌آنجلس یا سن‌دیگو حمله می‌کردند، چه اتفاقی می‌افتاد. این دو شهر به دلیل موقعیت جغرافیایی‌شان بیشتر مطرح هستند و منظور من حمله موشکی است.»
ترامپ افزود: «اگر چنین اتفاقی می‌افتاد، وحشتناک بود. بگذارید لس‌آنجلس یا شهری مانند سن‌دیگو را هدف قرار دهند. بگذارید یکی از شهرهای بزرگ ما را هدف حمله قرار دهند. آن وقت است که می‌فهمید مشکل واقعی چیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78662" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78661">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhYA-QvKZcvR6TMevNtgJBrO09R2UWVjRmCoYyzTu5iyrWMjh6MvKuumTHlXdxojlVOeyCSXDrMwnvG6GQfthlBbj0lZ1P4xhRTrQ_pK4NcfEP5dTWdnYCbAZht0PhwkTJWyGB5fORn6KS-WCp02qDwfy-TmhByrGRbDhq2ytlPG-vLG8GSGHD6W8IQR3-LZAU-9fMUt1i6ZoSnIunkGh4LWOBZAavR_7yZo14LLd_jr1Mag18jm4iqn2RlSQKC3PwIXQYazGDyKSmW8-FeKIdTf1SctNanLKzafpT1h972nLGKgO3ow4eWF9UeIUCQKBurqeXdd4WP_dvUE66BieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز پنج‌شنبه ۱۶ مهر گزارش داد شرکت هواپیمایی لوفت‌هانزای آلمان پروازهای خود به ریاض را تا ۲۴ مهر و ایر ایندیا پروازهای خود به مقصد و از مبدا پایتخت عربستان سعودی را تا ۱۸ مهر لغو کرده‌اند.
این تصمیم همزمان با تشدید حملات حوثی‌های یمن مورد حمایت جمهوری اسلامی به فرودگاه‌ها و زیرساخت‌های عربستان سعودی اعلام شد.
حوثی‌ها اعلام کردند فرودگاه بین‌المللی ملک خالد در ریاض را با موشک بالستیک هدف قرار داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78661" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mV7Vu6sMocPutg4eyn9g8-WiCit6CY63cM5kgNJOaxkZEUxZAfQ8Yrx9JDk2Hn8Rq11Y2cUKl3VXbrMmkL27pHypOuTXMZPcIHS6tPbM-kkSpI5c4z3bbMXPXE3N2IFRG_p-igbX_oP2mT7PPMRc5exYlWAsTn1p11iZ7z1pEy12mHF_-thd8g-ykEUH7clKbu-fib7vzL2lkRu549gx8esvOJ1M0Ft5pP2n5ihBs3K9abH2Ry6VDo-ubhMgz_GOC_qmOqoffFY4jhWorP5tEMMOflnmdvhfc-cZrvpq-pnZjuPibQG95KrSGn2NvWzLg-_ITKiWcBMdv97VEqYTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارگارت همیلتون، دانشمند آمریکایی و از پیشگامان مهندسی نرم‌افزار که نقش مهمی در فرود نخستین فضانوردان آمریکایی بر سطح ماه داشت، در ۹۰ سالگی درگذشت. او رهبری گروهی از متخصصان را بر عهده داشت که نرم‌افزارهای مورد استفاده در ماموریت‌های فضایی آپولوی ناسا را طراحی و توسعه دادند.
موسسه فناوری ماساچوست (MIT) با تایید درگذشت همیلتون اعلام کرد که او روز چهارشنبه هشتم مهرماه ۱۴۰۵، برابر با ۳۰ سپتامبر ۲۰۲۶، از دنیا رفته است. این موسسه در بیانیه‌ای، همیلتون را از پیشگامان علوم کامپیوتر توصیف کرد که پیش از فراگیر شدن حرفه مهندسی نرم‌افزار، در توسعه این حوزه نقش مهمی داشت.
همیلتون از سال ۱۹۵۹ تا اواسط دهه ۱۹۷۰ در موسسه فناوری ماساچوست فعالیت می‌کرد و مدیریت بخش مهندسی نرم‌افزار را بر عهده داشت. گروه تحت مدیریت او نرم‌افزارهای هدایت و کنترل فضاپیمای آپولو ۱۱ را طراحی کرد که در فرود تاریخی نیل آرمسترانگ و باز آلدرین بر ماه در سال ۱۹۶۹ نقش تعیین‌کننده‌ای داشتند.
در جریان این ماموریت، رایانه فضاپیما لحظاتی پیش از فرود با مشکل پردازش بیش از ظرفیت روبه‌رو شد، اما نرم‌افزار طراحی‌شده توسط گروه همیلتون توانست با اولویت‌بندی وظایف، عملیات فرود را ادامه دهد.
باراک اوباما، رئیس‌جمهوری پیشین آمریکا، در سال ۲۰۱۶ به پاس دستاوردهای علمی همیلتون و نقش او در پیشرفت فناوری فضایی، نشان آزادی ریاست‌جمهوری را به او اهدا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78660" target="_blank">📅 19:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bo_nH9LPZcOTMoxIcCygJkCdgoWdCrGFt8iyBrgAxqvbRpV3tteA9iPzaoPK65r9tLBZb_mtZhAC1ftXFMb9eODktuN0WFUZJfg8iukNsoGdwNsvIRi41NndyTO-4Kl7Svg5ufbaLw4eWlP_ERoOKly3Vsz9bxt7G7rg4LyGmzkEXPII8AdndPb0DaOEuchncZw4fiVo9RASj_VIOw60QdZQbPponBhZEGUmWX-YwkYUlwJhuDWgP-_amnridat1iC9epCuMZzlKPoOueZWew36BF4dRisrycDxcZ-sf0SASMy6bhX5_ITYnsu1Cs-8NZWrcN-qT8dsqzHQeZX-xjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی در چارچوب طرحی به ارزش حدود ۲۱ میلیارد دلار، توسعه میدان نفتی مرجان را برای افزایش ظرفیت تولید نفت و فرآوری گاز دنبال می‌کند؛ میدانی مشترک با ایران که بخش ایرانی آن «فروزان» نام دارد. براساس گزارش مرکز داده‌های باز ایران، عربستان روزانه حدود ۷۳ میلیون مترمکعب گاز از این میدان برداشت می‌کند، در حالی که ایران از بخش خود گازی تولید نمی‌کند.
در تازه‌ترین مرحله توسعه مرجان، شرکت نفت عربستان، آرامکو، قراردادی با شرکت آمریکایی «کی‌بی‌آر» برای نوسازی تاسیسات این میدان امضا کرده است. کی‌بی‌آر روز سه‌شنبه ۱۴ مهر ۱۴۰۵ اعلام کرد خدمات مهندسی و اجرای پروژه را برای تاسیسات فرآوری، فشرده‌سازی گاز و زیرساخت‌های برق مرجان ارائه خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78659" target="_blank">📅 15:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78658">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pF83oQpOGNns7HW-O6VXkdwn1f_b9IFjeRV_nsH9xUnsEqqzgbW-sRQ3Pt6l-HpV8kA83gjPk45_6c4I4o4F_qukjnc0x0euXYSq_rrfwShJBtqJzHnH7fghjW57YLEbK40QifgraVf7gM5gfxGCmo8AT3fCZpVK2ulnIhp3zfnlVllnUA9rqYfzMBSjSiQADoRCT8y-Htv-dieanbAlmJ4CqS8jLEh9oBC79Fwt0LKXWVscsRpDVER9HdpKssIYTZI9bSrouu6roYBQR0apPX56sDsKZNHP2hvtN7sK06ZyRLOfluhO87799gEPbGcaXEyshEH1dgSMuzFHU_uIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز، روز پنجشنبه ۱۶ مهر ماه، گزارش داد شمار کشتی‌هایی که از تنگه هرمز عبور می‌کنند، پس از افزایش حملات به نفتکش‌ها در هفته گذشته، به پایین‌ترین سطح در بیش از دو ماه گذشته رسیده است.
رویترز بر اساس داده‌ها و تحلیل‌های شرکت تحلیل کپلر گزارش کرد، روز سه‌شنبه فقط ۷ کشتی تجاری از تنگه هرمز عبور کردند که پایین‌ترین رقم از اول مردادماه تاکنون محسوب می‌شود.
عبور نفت خام از این تنگه نیز با کاهش ۲۷ درصدی نسبت به بالاترین سطح زمان جنگ در هفته قبل، به دست‌کم ۱۰.۱ میلیون بشکه در روز رسید که معادل ۷۴ درصد سطح پیش از جنگ است.
به گفته تحلیلگران کپلر، بخش عمده این کاهش به انتقال محموله‌ها از کشتی به کشتی در دریای عمان مربوط می‌شود.
به گزارش رویترز، با این حال، صادرات از سواحل دریای عمان و دریای سرخ به ۶.۷ میلیون بشکه در روز افزایش یافت، رقمی بیش از دو برابر سطح پیش از جنگ که به جبران کاهش عرضه از طریق تنگه هرمز کمک کرد.
داده‌های کپلر نشان می‌دهد تعداد کشتی‌های عبوری روز چهارشنبه به ۱۰ عدد افزایش یافت، اما همچنان بسیار کمتر از بیش از ۲۰ کشتی در روزهای یکشنبه و دوشنبه بود.
این گزارش پس از آن منتشر می‌شود که حملات به نفتکش‌های عبوری از تنگه هرمز در هفته گذشته به بالاترین میزان هفتگی از زمان آغاز جنگ ایران رسید. پیش از آغاز جنگ در نهم اسفند سال گذشته، روزانه حدود ۱۲۵ کشتی تجاری بزرگ شامل نفتکش‌ها، کشتی‌های حامل گاز، کشتی‌های فله‌بر و کشتی‌های کانتینری از تنگه هرمز عبور می‌کردند.
همزمان، دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنحشنبه نموداری در شبکه اجتماعی تروث سوشال منتشر کرد که نشان می‌دهد سطح تردد نفت از تنگه هرمز به میزان پیش از جنگ آمریکا و اسرائیل علیه ایران بازگشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/78658" target="_blank">📅 15:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78657">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7pETNSaEeC8_g3NCqTj8CCdLJo03-mz6pmL4Z-Lf39HMrxZl0oS86WZbyBWO1Mfq_gIHobgsWyX3I0sqj7GxJMaNFcfSuas325y5CyOk5FNawtW_J9UKf4QMupx1X9usYteUHs3tydZGZtBrGHORIcWX9NkSHknOh4IR12jIhXmgaUWMVCvDfoGsiVZfJTAJNytPXI8LhzDVaEaQK6us5yhDg2yHtg5idFqZ7v5Uq7x1OcYwtQ2rHe_xPzdL4OiGkj1CCqwKcSGIlsmfOvm6Jaa1AwUplRqUNClz26aLEy93vo7z_pRBRyGfgupu7X6HtFyJZL6H1x4RaJ2JfZ35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی حمله افراد مسلح ناشناس به ستاد فرماندهی انتظامی شهرستان گلشن در سیستان‌وبلوچستان، نیروی انتظامی وقوع انفجار و تیراندازی در این منطقه را تایید کرد. هم‌زمان، ارتش جمهوری اسلامی از کشته‌شدن یک نفر و زخمی‌شدن سه نفر دیگر در حمله‌ای جداگانه به مینی‌بوس حامل کارکنان ارتش در زاهدان خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/78657" target="_blank">📅 15:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d9ANKdw5VIi0ToOQzfYwwLhl-3jfWyD-D6o3KOMJo_iobD_KBeWTp3TYgq3RZ3RwE0aP8nZwPNOkYj7gv70I7I28u0YcLySPPgwmeOsPdYYGzZZZnFR4PNlngRHK0DEXMILXwyzWjxrrTwNaueyvRHR9RRL2sKFIlJmSnBhRchrIOskgRPEAewJP-XXzwXftZC7rMauNCKI4eHqrgcbtpG3_NDX7l9sDMRr5GfunL1oIxLAw_T4fN_0WfzapmXhSlSeJMXlbclDXFRVaM3z9jYIm2FJqd_Yd21FY1X7Jt-4U-VH_hh0S1ljD-hr-5PBaQYHRm9EbZqRWFtpe4ZwcQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز
پنج‌شنبه ۱۶ مهر در گزارشی تحقیقی بر اساس گفت‌وگو با بیش از ۷۵ کارشناس حقوق بشر، وکیل و شهروند ایرانی نوشت ایران پس از اعتراضات دی‌ماه شاهد شدیدترین سرکوب چند دهه اخیر از سوی جمهوری اسلامی است.
به نوشته رویترز، دستگاه‌های امنیتی و قضایی جمهوری اسلامی با همکاری صداوسیمای حکومتی، از طریق اعدام‌های شتاب‌زده، محاکمه‌های غیرعلنی، پیگردهای قضایی گسترده و انتشار اعترافات اجباری، در پی ایجاد فضای ترس و خاموش کردن مخالفان هستند.
بر اساس این گزارش، از ۲۸ اسفند ۱۴۰۴ تاکنون دست‌کم ۳۴ نفر از افرادی که در ارتباط با اعتراضات دی‌ماه بازداشت شده بودند، اعدام شده‌اند. پنج نفر از آن‌ها تنها در ۱۰ روز گذشته اعدام شدند. در مقابل، طی چهار سال پس از اعتراضات ۱۴۰۱، در مجموع ۱۵ نفر در ارتباط با آن اعتراضات اعدام شدند.
رویترز همچنین گزارش داد مقام‌های امنیتی ارمنستان در ماه مه به گروهی از معترضان ایرانی درباره تهدیدهای جدی علیه جانشان هشدار دادند و از آن‌ها خواستند برای حفظ امنیت خود و خانواده‌هایشان این کشور را ترک کنند.
اشکان، معترض ایرانی ۳۰ ساله که در جلسه با مقام‌های امنیتی ارمنستان حضور داشت، گفت به آن‌ها هشدار داده شد افرادی احتمالا برای ربودن، ترور یا آسیب رساندن به آن‌ها اعزام شده‌اند. رویترز نوشت روایت او را با گفته‌های معترض دیگری که در همان جلسه حضور داشت و فایل صوتی آن جلسه تطبیق داده است.
رویترز همچنین نوشت نهادهای امنیتی جمهوری اسلامی با تهدید خانواده‌های مخالفان ساکن خارج از کشور در داخل ایران، لغو گذرنامه‌ها و خودداری از ارائه خدمات کنسولی، فشار بر منتقدان را به خارج از مرزهای ایران گسترش داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78656" target="_blank">📅 15:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLptYjN5_TyYWBcc9184HUp61knTVOldLGPhb6CMdMUuGs96FLCU5Rty1wKKs115a_BR-g6Rlg9aTEFtlDthaGKIjgOv0hqdzaLPLrSYU__tgY4lcVfrQv2Oykvs4Pf2wK2t7V4Oy3-JaDrZCDzkVx9PjbR6Pw9EcJ3QRnGOb8joYyy8wF1Z30XW2mPxlHZphky6U8JKFnrNA5aUuy9NzoOzOyFZXO5-aNmxxFYdbpsHX8_50ut2TUxGLDWFMdr_9Y5-GpvtpkDZJJ3j_gl5amQrvIjGaaE_FVho6Ze88QU8peVAFg3WZnQzC7Wik0JWsBrtpje0fRiXr_qyBs8R3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، بامداد پنجشنبه ۱۶ مهر در سخنرانی در ایالت تگزاس درباره جنگ با ایران گفت این جنگ «خیلی زود» پایان خواهد یافت و ایران را «کشوری شکست‌خورده» توصیف کرد.
ترامپ گفت: «وقتی این جنگ تمام شود که خیلی زود خواهد بود، آن‌ها یک کشور شکست‌خورده‌اند، کمی رمق برایشان مانده، اما نه زیاد.»
او همچنین با اشاره به نفت عبوری از تنگه هرمز گفت این نفت در سراسر جهان توزیع می‌شود و بار دیگر بر نقش آمریکا در انتقال نفت از این مسیر تاکید کرد.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا در جریان یک گردهمایی انتخاباتی در تگزاس گفت «ما به زودی از ایران خارج می‌شویم و قیمت نفت هم مثل سنگ پایین می‌آید.»
او گفت افزایش بهای نفت ارزش جلوگیری از دستیابی ایران به سلاح هسته‌ای را دارد.
رئیس‌جمهور آمریکا همچنین در مورد احتمال دستیابی به یک توافق با ایران گفت: فکر می‌کنم این توافق واقعاً چیزی است که می‌خواهم انجام دهم، اما آیا آن‌ها حاضرند برای متوقف کردن برنامه هسته‌ایشان چیزی به ما پیشنهاد دهند؟ و ما قطعاً هرگز اجازه نخواهیم داد ایران سلاح هسته‌ای داشته باشد.
آقای ترامپ همچنین با تکرار سخنان جنجالی چند روز گذشته‌اش در مورد حمله فرضی ایران به لس‌انجلس و سن‌دیگو گفت: «همین چند روز پیش گفتم: بگذارید موشکی به سن‌دیگو یا لس‌آنجلس اصابت کند... بگذارید به سن‌دیگو یا لس‌آنجلس حمله کنند تا شاهد اتفاقات ناگوار باشید... ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما از شهرهایمان محافظت می‌کنیم. ما از کشورمان محافظت می‌کنیم. ما اجازه نمی‌دهیم چنین چیزی رخ دهد.»
این سومین سفر دونالد ترامپ در طول یک ماه گذشته به تگزاس برای تبلیغ نامزدهای جمهوری‌خواه محسوب می‌شود؛ نامزدهایی که در تلاش برای حفظ کنترل کنگره، اکنون با رقابت‌های انتخاباتی میان‌دوره‌ایِ به‌طور غیرمنتظره‌ای فشرده روبرو هستند.
ترامپ در ورزشگاهی مملو از جمعیت در سن‌آنتونیو سخنرانی کرد تا از کن پکستون، نامزد جمهوری‌خواه سنا در این ایالت حمایت کند که در رقابتی تنگاتنگ با جیمز تالاریکو، رقیب دموکرات خود، قرار دارد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78655" target="_blank">📅 05:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9NsSLnRPm7RDpVgc42JhqnDpocFzCYtm-fQAgJY10adboyyjZbjsjSeJqBDF_ijIeU7Oba-RfWLRgTjaEj5BbowzAcwk9Tj8p9TeOk5-mCBt5wfjopdL9wduIlkEZCcJiC7p4UQuFZoXeX4llvPWgqbI2xmX6gm-zx_ACfkTkuQn_Uwm8hYvA9Eo9klGZqR68gA3gtPCnW-_8dImt-OUQ3TutK7pyl-AeAzNWX0SStGiN5S6pBk7U6k-neSRKuFY386ZQ2JOJcpyPt2fW2erMenkzLLKlznU-UD_0X-LIy8MuJ27arn9psF1R_vde62N4PNBtvsh1B1C3GvZsipCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رسانه آمریکایی گزارش کرده‌اند که پنتاگون برای حمله احتمالی مجدد به ایران طی روزهای آتی آماده می‌شود.
سایت خبری اکسیوس به نقل از مقام‌های آمریکایی گزارش کرده طی روزهای اخیر پنتاگون با صدور دستورالعملی از سنتکام (فرماندهی مرکزی آمریکا در منطقه خاورمیانه) خواسته روند آمادگی خود را برای از سرگیری عملیات رزمی عمده علیه ایران تکمیل کند.
همچنین مجله آتلانتیک هم در گزارشی اختصاصی به نقل از دو مقام آمریکایی نوشته کاخ سفید از پنتاگون خواسته است تا گزینه‌هایی برای حمله به اهداف ایرانی تدوین کند که امکان اجرای آن‌ها پیش از انتخابات میان‌دوره‌ای وجود داشته باشد.
به گزارش آتلانتیک، دونالد ترامپ مشتاق است پیش از انتخابات، قیمت بنزین را کاهش دهد و به پیشرفتی عمده در مناقشه با ایران برسد.
به گزارش اکسیوس، دستورالعمل پنتاگون شامل تاریخ مشخصی برای آغاز حملات نبود و دونالد ترامپ هنوز تصمیم نهایی را اتخاذ نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78654" target="_blank">📅 05:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_LBbHiJDFrmJJTJiHGpAy6V37Y_bDLGWhJuvav2vgcVK0Uiz3060RoyoycUdTa3UvkI_wBybGKyK_WflV-WRDMt2oeHJOQvSLd2XiUPwuK4cvvqB_VqZtXdNn0qszHsBpjFSul9L66kDHCZ5Vwl993EO1U3tvfPUjCz1M54jSbyD4om_ljqDxlPBMUqiL4-mWOt7EsNGwIlY-QjTB86DUov7C2mrx_5IL4LExv5A-SWSm2tKu1SphwZDFrL9O3VPqHk0RD1HcUBR3cW2sM8_b7nXkUWRXcNeVjRUrzjiriu6bDkzcR_63VC7awiPU7DxhogxhFbipRqL_Ch_VOUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ارتش آمریکا، سنتکام، بامداد پنجشنبه ۱۶ مهر با انتشار پیامی در اکس، اظهارات یکی از فرماندهان سپاه پاسداران درباره بسته بودن تنگه هرمز و کنترل کامل ایران بر آن را «نادرست» خواند.
سنتکام اعلام کرد تردد کشتی‌های حامل کالاهای تجاری و محموله‌های انرژی، از جمله ۲۰ میلیون بشکه نفت خام، در تنگه هرمز جریان دارد و افزود: «ایالات متحده و شرکای منطقه‌ای به‌وضوح کنترل تنگه را در اختیار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78653" target="_blank">📅 02:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T3WU3zCtvM3Qov67hrGZCPkQ7fkUL1V5_CofIR8D791hYpILhEuBubR9aDJKNGSiVOkhPhbAyg7IRHrL6a46mogw2TaigQ1Xe6Xq2pB995qnV_9yqQ0-4iFGY5Q-tnFUnuY1B6_Ha-ZvnQeyaPvNVz7Aed_7LJRPpxMnf3NoIWiOSY_6urJqUnk3LyQMUGlemeCUHGevt7QMEg7vXV1KbWeyGrim7o3TuylqTnooajUMczx_abEK4SEpEq3Y14Ito4ahXDAdP9RZ72dLCOcffscXnD-v3dIZU9RGmapESq2M-JJbW_Cmw3Zq8uo_1nlmlyKBUi_RYg2a0Y6j6-PQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات تجارت دریایی بریتانیا: در حمله به یک نفتکش در شمال قطر خسارت جانی گزارش شده است
سازمان عملیات تجارت دریایی بریتانیا شامگاه چهارشنبه ۱۵ مهر اعلام کرد یک نفتکش در آب‌های شمال قطر، در ۵۱ مایلی مدینه‌الشمال، با چند پرتابه هدف قرار گرفت.
بر اساس اعلام این سازمان، در این حمله تلفات جانی گزارش شده، اما هنوز جزییاتی درباره شمار کشته‌ها یا مجروحان منتشر نشده است. مقام‌ها در حال بررسی حادثه‌اند و از کشتی‌های منطقه خواسته شده با احتیاط تردد کرده و هرگونه فعالیت مشکوک را گزارش کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78652" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiPDkYy09grm-Sq747jIvZxW1i3gzVedC0BzDwYfMPKSPAb9_6MkrQZs8r7_JBv5tN4yIwll6A-ZoREfTcd8O52bUhXznrt2sXtVQR7Xb7qlz8LIMlWHXdIUUV0OteYU01KWp-63e-r1lWB1KwASAnwZ_Asla_kj8EpQrM116Rvzjw9JRmsnscWgRCxLOvwfoaGOArntnRKHD0Zz35PrkdPKS1oNheZghd0SsM9Q5gvPWJlodvPKYTTWmObEi4r85LR5yJOmMB0aRWIBi-k0jhYwm5PAium-Pwnw3nF9VdoQtnpopltSNVMnVwGI9ns2TQTOIl7rW5EUrogFMOC0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع مطلع به خبرگزاری رویترز گفته‌اند جمهوری اسلامی ماه گذشته ۲۰۰ میلیون دلار در اختیار حزب‌الله لبنان قرار داده است تا این گروه به خانواده‌های لبنانی آواره‌شده در جنگ امسال با اسراییل کمک مالی کند.
بر اساس اطلاعات منابع رویترز، حزب‌الله قصد دارد در مرحله نخست به هر خانواده حدود سه هزار دلار کمک کند. اولویت با خانواده‌هایی خواهد بود که روستاهایشان ویران شده یا به دلیل حضور نیروهای اسراییلی در مناطق جنوبی لبنان امکان بازگشت به محل زندگی خود را ندارند.
یکی از منابع شمار این خانواده‌ها را حدود ۵۰ هزار خانواده اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78651" target="_blank">📅 18:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNRJm5iY5TPISELJFwYgp1Jen_DNzgJV8lSfSGrKJ9SU2RrlcxKR69rNqsroV9priM4JQk_ve4BcfvzZNkjjHjavFHpEWOZYLn-l4I0MGypLleX_1eIGllAtfOrb0H2RNpg2KPO2sA5FJcxpVdG1P6w7SB-Q_6nUBoeQnQP1VWgQqszRlAsHqeeFlUj4oGf5RxfY4FhG0gRCwGEctQfUoYRHPJ9vPCB_1EZbMSbrEGTyz5Jh4wOadCZpRcsSy-RUGLuKx9zR7mKF08KVwbrv_MIUv_4lQ205sNs6V8YUXCK9QGzymaK5pD2WDQqxfDRt6BGanEunTltJAoTeJ3uy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهاره آقایی، وکیل دادگستری محبوس در زندان قرچک ورامین، به ۲۰ سال حبس محکوم شده است.
کانال تلگرامی شیرین عبادی
با اعلام این خبر، حمایت از معترضان دی‌ماه، حضور در مراسم چهلم سپهر شکری و کمک حقوقی به خانواده‌های دادخواه را از موارد مطرح‌شده در پرونده او عنوان کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78650" target="_blank">📅 17:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tltApgMGAR7dGAcAlVy8WJMdpKnmS_6adGap4ztQYk83IMWdC_As7wvx9ht0i-Wvn_EX_O_OzUYdTHcCRoJBXmKyUYskvGl6ZrrbXfCxWIPoqG3gDU-KVNVejtV0ZQps9KrmX7NrR2RTpDQfs36hObdELBb0At9OW1BzDvd_Pd5T_NnDS1nSvPGi0F55PzchBgylqztOvX-EHQm2tfNDVyO73HkQBo2-aY-vQJynQY1JzW_HR4-FIHm-9GBv2QqeVQE0I7SVj1J2kDHaqi2iCShy7xh569nYMucnI4byGxkcmoRliNvUrfgQ3uv7pB-mXPVnukxmwH45OcBKKcajjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده آمریکا، با انتشار پیامی در اکس و با لحنی کنایه‌آمیز نسبت به استعفای محسن پاک‌نژاد، وزیر نفت ایران نوشت: «ایران وزیر نفت جدیدی دارد. با توجه به اینکه از ۲۵ اوت تاکنون حتی یک بشکه نفت خام نیز توسط ایران بر روی هیچ شناوری بارگیری نشده است، این وزیر نفت دقیقا چه چیزی را مدیریت می‌کند؟» پیش از این، مهدی طباطبایی، معاون ارتباطات و اطلاع‌رسانی دفتر ریاست جمهوری ایران اعلام کرد، پزشکیان پس از موافقیت با استعفای وزیر نفت، طی حکمی حمید بورد، مدیرعامل شرکت ملی نفت ایران را به عنوان سرپرست وزارت نفت منصوب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78649" target="_blank">📅 17:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq2cI57wawjFEcXGD9eRCooKoAjWCuF5SUw5nAqfUdIG8uEf-w3Dn02iL7m84t9YZ_dsF5O8tJE3DD-rs_JEB7uVIEf1j9vJ2rdac14fx8Tv1_cGmRwTjxP3s0L_1F9R3bAtK-noHCtAZ7tepJzr3uRVO6KZXudpErdnycwV-2MZUVePHXbv5tATLtTI4W_1VcyHxBeu1k63X0zU7QjwdH3PXiciraAwdWuFaLq0HMiNEAFiqaPVUgJlGeSO8dxyshrTigACS_dJwd6ediyRyxsMKXfTRe5A7UqioTPdh7L-16OaqeVKOL0qRUXS2RpsipFrb7Q4gDVFSL-APaL8HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام امید گودرزوند چگینی، معترض ۳۷ ساله، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ و محبوس در زندان چوبیندر قزوین، در مرحله تجدیدنظر تایید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78648" target="_blank">📅 17:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N7lj6sDgtvOI-NvOjs2IP9wGR3BsCEEW0IkHdl3lf0bcFL447jvF4DDI87Y6RjqGD_mwOPX7yxTMypeUi-9Kqt_JSwa42pmisjrzI51Ppp11AuxRVTQs0BA6NblZcn65Ch-Yh0BFDkTJmqDKKTwO7v46GuJJ90fPi_UNWOPfpJ2CbSRqNnLaL3ZF0wd0_XOrlztKzbpUlUjml36W5nf4-F-rnsk4XlWMwYMYfWM0gW0AkjWU9xylEN8c99WzfgXDevmNd9Nb8qE1oAHEbCPMhBr-MmtGbfs-gOlvM5HpmOcEKkwNZ94ncjqswT8nU7wdRWKUWmMik3ydSfXj8SM9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20e0cac582.mp4?token=GVWFLQ4L4-k6jl0-5PHMl7yirBrB7_coJizuEH1XmolAT7yLpu8h-8VFXS4Jkw8Q_FwbmPQ9GC5JXe31gz8GGWYv-zK_3F6-JJ7nobLFtaZgIkQlBCD6oDPaXRst4rgwjBN9mrUDzNLTCm1gZcMd_qiFi-Xfd_j5bK-QaoltxRIrFPC4HLHySfTyPkMXBmug5ZxKetDDbC2Sg42Gt8AHXOYjqhYOOHUQokICGG12kqv3QK9VyAUHkeMr4VEOFW2hQznV06eVZCuXmDjIWBadMx1teHx-DqpkxRP2N04AO1H4EcPCb4mimZ6641glyvx6twrxGzNPYGde-JzYWbO4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20e0cac582.mp4?token=GVWFLQ4L4-k6jl0-5PHMl7yirBrB7_coJizuEH1XmolAT7yLpu8h-8VFXS4Jkw8Q_FwbmPQ9GC5JXe31gz8GGWYv-zK_3F6-JJ7nobLFtaZgIkQlBCD6oDPaXRst4rgwjBN9mrUDzNLTCm1gZcMd_qiFi-Xfd_j5bK-QaoltxRIrFPC4HLHySfTyPkMXBmug5ZxKetDDbC2Sg42Gt8AHXOYjqhYOOHUQokICGG12kqv3QK9VyAUHkeMr4VEOFW2hQznV06eVZCuXmDjIWBadMx1teHx-DqpkxRP2N04AO1H4EcPCb4mimZ6641glyvx6twrxGzNPYGde-JzYWbO4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید ایران فرصت‌های متعددی را برای دستیابی به توافقی دربارهٔ برنامه هسته‌ای خود با ایالات متحده از دست داده است.
او روز چهارشنبه ۱۵ مهر در یک نشست خبری مشترک با همتای یونانی خود در آتن گفت: «ایران فرصت‌های متعددی را برای رسیدن به توافق هسته‌ای با آمریکا از دست داده و همچنان مبالغ هنگفتی را صرف تروریسم، تسلیحات و حزب‌الله می‌کند.»
روبیو همچنین گفت ایران اکنون با اقتصادی رو به فروپاشی و تحریم‌های تازه روبه‌رو است و مسئولیت این وضعیت را متوجه «روحانیون تندرو شیعه حاکم بر ایران» دانست.
او گفت: «اقتصاد ایران در آستانهٔ رسیدن به وضعیتی است که از نظر وخامت، کمتر کشوری در جهان آن را تجربه کرده است و همهٔ این‌ها نتیجهٔ عملکرد روحانیون تندروی شیعه‌ای است که در آن کشور تصمیم‌گیری می‌کنند. آن‌ها هستند که مردم محروم ایران را به چنین وضعیتی دچار کرده‌اند.»
وزیر خارجه آمریکا همچنین با تکرار موضع واشینگتن دربارهٔ جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت دونالد ترامپ توان نظامی و بخش بزرگی از ظرفیت صنایع نظامی ایران را از میان برده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78646" target="_blank">📅 16:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hoTTwUzKpKNBz20IgFW2i7aRu30WX4I0QVaerQCGYdIx3md6ochtca3J8n6uebINaQx5KcVjnqUcP4mY2r7UIYjOdCTKxPX_JQbvwn2xjiM21uOjLcr8DbWrBO3saJdeS-DLkFxL46YjVDlD_Neq84ql2XXFF894IlZmEAYN4BJPxqp6KKoTKmrFJkmL_w6aNkmclopDlVcJbG1vjqHTr7ihkbenUzxtWU3UyZoscJowC0ChADcnKkMUaQz8X1P4cTu95nuxT3UChYi0lLy1-Dncm9BD-oeR6Y7CL6egD61UfGEtpx3wyorBrmR7JHNxpXJ0VyD3RZNuGhm-2XeFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه خراسان نوشت که نجمه امینی، دختر ۲۳ ساله، به اتهام «سب‌النبی و توهین به ائمه معصومین» در فضای مجازی، از سوی شعبه ششم دادگاه کیفری یک خراسان رضوی به اعدام محکوم شده است.
امینی پیش‌تر در یک فایل صوتی از زندان وکیل‌آباد مشهد از صدور حکم اعدام برای خود خبر داده بود.
پس از انتشار این فایل صوتی، خبرگزاری فارس، وابسته به سپاه پاسداران، اعلام کرد که هنوز هیچ حکم قطعی برای نجمه امینی صادر نشده و دیوان نیز درباره پرونده او اعلام نظر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78645" target="_blank">📅 16:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qayLgGaTkOADRMLE6BrPc97mXZYcUNQW2uGNswX30Tp34pAUS23p-pwTktErn2x0fUDLqWWQPwHqqeRojgT37Xye4XJlKQ5K8W5gfXwXuFgML8Ae458aibGgMCJviSwesiJ9zxizmT0kQ72VrR-76OmR_oF4qL_zIJHnnfJXROovmrGMFuZE-0OXNleF3sREEG5bv6UuLa5al9vmEVMJyn6WE-S7XCj0ow-MXAowTvtSrK7o-eVTyfOTVrbt71s0ETgVLXj8X7D6uq67vsYnlQuEggP3yqQ98ExcbgM3URDrURSEKEdj72jgsiBxeAwKAq8e_fgH8vVO8h1ifbUtYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران باید غنی‌سازی را عملاً کاهش دهد؛ میزان اختیارات پزشکیان و عراقچی روشن نیست
🔸
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، می‌گوید حکومت ایران برای پایان یافتن جنگ باید ظرفیت غنی‌سازی اورانیوم خود را به‌طور «معناداری» کاهش دهد و ایالات متحده در مذاکرات با جمهوری اسلامی، به وعده‌های لفظی بسنده نخواهد کرد و خواهان اقدام عملی تهران است.
🔸
آقای ونس در گفت‌وگو با خبرگزاری رویترز که بامداد چهارشنبه ۱۵ مهر منتشر شد، همچنین گفت ایالات متحده با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه، در تماس و مذاکره است، اما برای واشینگتن روشن نیست این دو مقام تا چه اندازه در ساختار فعلی قدرت ایران اختیار تصمیم‌گیری دارند.
🔸
اظهارات او در حالی مطرح می‌شود که تهران و واشینگتن طی هفته‌های اخیر پیشنهادهایی را برای پایان دادن به جنگ و بازگشایی کامل تنگه هرمز ردوبدل کرده‌اند، اما دو طرف همچنان بر سر دامنهٔ مذاکرات و مسئله هسته‌ای اختلاف اساسی دارند.
🔸
معاون رئیس‌جمهور آمریکا در پاسخ به پرسش رویترز دربارهٔ شرایط واشینگتن، خطاب به مقامات جمهوری اسلامی گفت: «اگر سلاح هسته‌ای نمی‌خواهید، پس چرا به سوخت غنی‌شدهٔ ۶۰ درصدی نیاز دارید؟ و اگر می‌خواهید تعهد خود را به نساختن سلاح هسته‌ای نشان دهید، سوخت با غنای بالا تولید نکنید. این یک مسئله بسیار پایه‌ای و تعیین‌کننده است.»
🔸
او افزود: «فکر می‌کنم اگر آن‌ها بخواهند تعهد خود را به نساختن سلاح هسته‌ای نشان دهند، باید در زمینهٔ ظرفیت غنی‌سازی خود اقدامی معنادار انجام دهند.»
🔸
آقای ونس در عین حال تأکید کرد که آمریکا همچنان برای رسیدن به توافق آمادگی دارد، اما چنین توافقی باید شامل امتیازهای مشخص و عملی از سوی ایران در زمینه برنامه هسته‌ای باشد.
🔸
او گفت: «ما قرار نیست حرف را با عمل معاوضه کنیم.»
🔸
این موضع با مواضعی که مقام‌های جمهوری اسلامی در روزهای اخیر اعلام کرده‌اند فاصلهٔ زیادی دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78644" target="_blank">📅 02:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=CasA9qUy6FrLyYDZrh2gBbRmH5SP9bPTMG_vrJs7xtyCTP8oUHS1DZDtx1hb5DvvznmBVeCZU_gvrOzy86nCOFunqW8nLBh_3zeTTwXQkKro7HLdEkEI7lQHZZyVTZEBpQXu--2vvK1FC0B03qwoOJoMdUXhKq-GvZ6CLlgmODdD_JzkAv3fiet7Duwiy5BKVUHi_568AIrCtpycWDyNG3Pg-tralvM7Quj1Fg12VUXpetzcz1j3g61k-JmhZ06wrMVQDtlCyif-vvomUhTjCleyLlSjIm96SZ7y1o3jJjhRA2-UVW2nwbF9vWdQKPvLu6X_lQHWoc901pWXjN0A0gkXdQ5YNfHO3NW5tB79Uybk1P__x_6_6q3pnjp6VmkelWIe3CExu7xl-qxZ48UYwEFC90Ib-j6o7mErBZdf7s5_KTNFF80d888BJCSMtn4iCNJBFGlazYga1F3Kf-AE7uIJrF0rx-soXkGZnSAfrtch7g2_njuj6uj9KiU17v6t5olv_jyBZfZntSFooKC-qCWFS0SUOHybbf_L5Xo0OP9EB8PF7yRouF67Wx-TJw8rvJZPGaydp434Sg4RM6yyzJ_Fk9CofJCOpkZvXxjbNp-_xps6fe4okJe25AZQfHEiSZ4WNiyGb0y-6Jpfc3Mwo4SNOA_jBt-LEy2AxVHJMaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=CasA9qUy6FrLyYDZrh2gBbRmH5SP9bPTMG_vrJs7xtyCTP8oUHS1DZDtx1hb5DvvznmBVeCZU_gvrOzy86nCOFunqW8nLBh_3zeTTwXQkKro7HLdEkEI7lQHZZyVTZEBpQXu--2vvK1FC0B03qwoOJoMdUXhKq-GvZ6CLlgmODdD_JzkAv3fiet7Duwiy5BKVUHi_568AIrCtpycWDyNG3Pg-tralvM7Quj1Fg12VUXpetzcz1j3g61k-JmhZ06wrMVQDtlCyif-vvomUhTjCleyLlSjIm96SZ7y1o3jJjhRA2-UVW2nwbF9vWdQKPvLu6X_lQHWoc901pWXjN0A0gkXdQ5YNfHO3NW5tB79Uybk1P__x_6_6q3pnjp6VmkelWIe3CExu7xl-qxZ48UYwEFC90Ib-j6o7mErBZdf7s5_KTNFF80d888BJCSMtn4iCNJBFGlazYga1F3Kf-AE7uIJrF0rx-soXkGZnSAfrtch7g2_njuj6uj9KiU17v6t5olv_jyBZfZntSFooKC-qCWFS0SUOHybbf_L5Xo0OP9EB8PF7yRouF67Wx-TJw8rvJZPGaydp434Sg4RM6yyzJ_Fk9CofJCOpkZvXxjbNp-_xps6fe4okJe25AZQfHEiSZ4WNiyGb0y-6Jpfc3Mwo4SNOA_jBt-LEy2AxVHJMaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ، به تشخیص و ترجمه ماشین:
ما در جمهوری اسلامی ایران خیلی خوب پیش می‌رویم؛ خیلی خوب. آن‌ها دیگر نیروی نظامی ندارند؛ نابود شده. همه‌چیزشان نابود شده و آن‌ها همان طرف شرور بودند؛ قلدر خاورمیانه بودند و دیگر چندان قلدر نیستند. اما هنوز باید کار را تمام کنیم و فقط مسئله این است که به کدام روش. می‌خواهیم این کار را به روش خوب انجام بدهیم یا به روش نه‌چندان خوب؟ خیلی زود خواهید فهمید.
وقتی به «دیوار فولادی» نگاه می‌کنم، همان کاری که ما انجام داده‌ایم و آن‌ها اسمش را محاصره گذاشته‌اند؛ من اسمش را «دیوار فولادی» می‌گذارم. حتی یک کشتی هم نتوانسته به ایران برسد. تنها کشتی‌هایی که عبور می‌کنند همان‌هایی هستند که ما اجازه عبورشان را می‌دهیم و این تأثیر بسیار بزرگی داشته است.
برای همین کشورشان از نظر مالی شکست خورده است. یک کشور شکست‌خورده‌اند؛ همه دارند کنار می‌کشند، همه دارند می‌روند. به نیروهای نظامی‌شان حقوق نمی‌دهند، به پلیس‌شان حقوق نمی‌دهند، به هیچ‌کس پول نمی‌دهند؛ اوضاعشان به‌هم‌ریخته است. اما هنوز باید کار را تمام کنیم.
نیروی دریایی ما پیشتاز است تا تضمین کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. و این همان چیزی است که همیشه گفته‌ایم: هرگز اتفاق نخواهد افتاد. هرگز اتفاق نخواهد افتاد. این دیگر یک امر انجام‌شده است.
ملوانان و هوانوردان دریایی بزرگ ما قهرمانانه جنگیده‌اند تا ارتش آن‌ها را نابود کنند. آن‌ها دیگر نیروی هوایی ندارند. نیروی هوایی‌شان از بین رفته است. نیروی دریایی‌شان از بین رفته است. آن‌ها ۱۵۹ کشتی دارند؛ همه‌شان همین حالا در اعماق دریا هستند، کف دریا افتاده‌اند. رادارشان از بین رفته است. تمام تجهیزات ضدهوایی‌شان از بین رفته است. ظرفیت تولید موشک و پهپاد آن‌ها به‌شدت کاهش یافته است. به‌زودی آن هم از بین می‌رود. دقیقاً می‌دانیم بقیه‌اش کجاست.
اقتصادشان ویران شده است. تورمی دارند که هیچ کشور دیگری در جهان ندارد. و آن مردی که چند روز پیش رفت، گفت: «من می‌روم چون کشورمان تمام شده.» این را گفت. نمی‌دانم. من هیچ‌چیز را قطعی فرض نمی‌کنم، اما اوضاعشان خوب نیست.
و به لطف مردان و زنان نیروهای مسلح آمریکا، ده‌ها تن از رهبران تروریست ایران از صحنه روزگار محو شده‌اند و مستقیم به دروازه‌های جهنم فرستاده شده‌اند. همان‌طور که می‌دانید، رهبرانشان رفته‌اند. گروه دوم رهبرانشان هم رفته‌اند. و بزرگ‌ترین مشکل من این است که هیچ‌کس نمی‌داند واقعاً چه کسی کشور را اداره می‌کند. هیچ‌کس نمی‌داند؛ شاید هم این چیز خوبی باشد. اما خامنه‌ای را یادتان هست؛ همه‌شان رفته‌اند و حالا ما اینجاییم.
ما داریم کارهایی انجام می‌دهیم که هیچ‌کس قبلاً انجام نداده است. مثلاً تکلیف این کشور باید خیلی وقت پیش روشن می‌شد. حالا ۵۱ سال است. قلدر خاورمیانه. این کار باید خیلی پیش به دست رؤسای جمهور یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم. همیشه ما هستیم. کشورهای دیگر باید خیلی وقت پیش این کار را می‌کردند، چون با گذشت زمان فقط بدتر شد.
اما ما کار را انجام دادیم و راستش مدام از رهبران جهان تماس دارم که خیلی از من تشکر می‌کنند. می‌گویم: «خب، کی می‌خواهید هزینه‌اش را بدهید؟» می‌گویند: «آقا، بابت این کار خوبی که کردید ممنونیم.» و من به آن‌ها می‌گویم: «عالی است. می‌خواهید چند کشتی بفرستید؟» می‌گویند: «آقا، ترجیح می‌دهم درگیر نشوم.» آن‌ها هیچ کشتی‌ای ندارند.
واقعاً داریم بار تمام دنیا را به دوش می‌کشیم. روی دوش ماست. و به یک معنا دوست داریم این کار را انجام بدهیم، چون خودمان قوی‌تر شده‌ایم و دیگران ضعیف‌تر شده‌اند. آن‌ها فقط ضعیف و ناکارآمد شده‌اند و ما کارهایی انجام می‌دهیم که هیچ‌کس دیگر، هیچ کشوری، هرگز نمی‌توانست انجام دهد.
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78643" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/141ace0942.mp4?token=ZeG36YTvrC_M6lbGaRZOHTiifhZLwYDRQVOE_FD-4p-fUWh-2sp2E8IW4pq0xbosdQXrzIi7LZ8GqwtOvTJjJ9R6MiATf7wujB61fvVF00-49MGU7yB5h3HdbLrtXe1_BuIz4934sI_Ti3tmKL0gPqRG6JRVkoAn6KYt9W6LI0TLcP7A40iHI7eln8cpaN8YpnAHU7I1mZCFMn8jgyuNVMwpM1wFmiWSwQQto0szcFYZO5gsS4HXAG8MV0r14KjHGs0RnzOeGQedmHJR4xxNC3AzCHK98B_rcTt5I2mHtrcsFmRSlprSnTh68Yx3hdIrRSoZxxzaBTeiCtAYW_qHLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/141ace0942.mp4?token=ZeG36YTvrC_M6lbGaRZOHTiifhZLwYDRQVOE_FD-4p-fUWh-2sp2E8IW4pq0xbosdQXrzIi7LZ8GqwtOvTJjJ9R6MiATf7wujB61fvVF00-49MGU7yB5h3HdbLrtXe1_BuIz4934sI_Ti3tmKL0gPqRG6JRVkoAn6KYt9W6LI0TLcP7A40iHI7eln8cpaN8YpnAHU7I1mZCFMn8jgyuNVMwpM1wFmiWSwQQto0szcFYZO5gsS4HXAG8MV0r14KjHGs0RnzOeGQedmHJR4xxNC3AzCHK98B_rcTt5I2mHtrcsFmRSlprSnTh68Yx3hdIrRSoZxxzaBTeiCtAYW_qHLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ یک کارمند ۲۸ ساله موسسه تحقیقات ضدطاعون در سیبری پس از ابتلا به بیماری که گمان می‌رود طاعون ریوی بوده باشد، موجب نگرانی‌هایی شده است.
بر اساس این گزارش‌ها، داریا شیپیلووای ۲۸ ساله در ۷ مهر ۱۴۰۵ (۲۹ سپتامبر ۲۰۲۶) به بیمارستانی در شهر شلخوف در منطقه ایرکوتسک منتقل شد و دو روز بعد درگذشت.
ده‌ها نفر که با این زن در تماس بوده‌اند قرنطینه شده و تحت نظر پزشکان قرار گرفته‌اند، اما مقام‌های روسیه می‌گویند تاکنون هیچ مدرکی پیدا نشده که نشان دهد مرگ او با عوامل بیماری‌زایی که در محل کارش با آنها سروکار داشته، مرتبط بوده است.
مقام‌های روسیه می‌گویند وضعیت تحت کنترل است و تاکنون مورد جدیدی از بیماری‌های عفونی مرتبط با این حادثه گزارش نشده است. با این حال، گزارش‌های تاییدنشده درباره احتمال ابتلای این زن به طاعون ریوی در شبکه‌های اجتماعی منتشر شده است.
مارکو روبیو، وزیر خارجه آمریکا، گفته است واشنگتن این موضوع را از نزدیک زیر نظر دارد اما در حال حاضر دلیلی برای نگرانی نمی‌بیند. دونالد ترامپ، رئیس‌جمهور آمریکا هم اعلام کرده که آماده کمک به روسیه است.
@
VahidHeadline
, @
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78641" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e6oZYenhGLR5tP2X6cSJXgD1gvBdYwShQBGOVOeIgFJz8-R0aTWQc-NpxHm0L8qKwSj_9gUTSSDueOt3RajjnfCbMuVitc6TrYU8q6VnpmbFgdiBACWdgZuDKRnb6vLX3hb4L9YFdb7vCStC2tzz6hgnjaxBWFo98Av3AdeCGPC3dZFc8LWg2ySiE6-vt3SNwaoZF2QpUjPS0jSExtnk9ypGJ1txDj7hslrE5lu9X6iTYe0c3jn7qFtBsy7az1pwc_Fb8b49u83_xNBD2ZEsdY_b32kDaRmlfDwBDnj5yIEK7daL4pwqc00HeLN7kg1LGUKhCijEKX7AxiaCsJ_zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: رسانه‌های دولتی ایران گزارش‌های نادرستی را منتشر کرده‌اند مبنی بر اینکه یک بالگرد MH-60R نیروی دریایی آمریکا، پس از اعلام وضعیت اضطراری در شب گذشته، در دریای سرخ سقوط کرده است.
✅
واقعیت: گزارش‌ها درباره سقوط یک بالگرد نیروی دریایی آمریکا در دریای سرخ صحت ندارند. همه هواگردها و نیروهای نظامی آمریکا در سراسر خاورمیانه در امنیت هستند و وضعیت همه آن‌ها مشخص است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78640" target="_blank">📅 16:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BOqynFYfDeL4thNqXIK7M8ERtGi4J1ihEz5GnxfHMx42EkSG8qV2F96gg94AbZ9mRDReTUwNYX7TtvIoYrJHQb0aQ1ozTKjPB-NrB0aGhqw7Mp4RphwZWpKd6TdhVdIRTP8SHsJQJpy45CQFcUP3Eq8DFl8Kh_mnDxqiX5OS0zxLZFDKAu2-TQyUkMlSREW0qKKJCZM23r3r8380L8X2CgIjvx6eh2RFN9s1t4VCLC-14S2kijAhG_99YjonbsOELDQmx3rtI50ZzO7E-B1fz32uU6MCdyavBlDqCcC_78683LrJLeQUIB536mgEeul_mKN95Xy100nyfJm_XEBcRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا بعدازظهر سه‌شنبه ۱۴ مهر اعلام کرد گزارشی با تاخیر درباره حادثه‌ای در تنگه هرمز در ۱۳ مهر دریافت کرده است.
بر اساس گزارش یک «منبع تاییدشده»، یک نفتکش هنگام خروج از تنگه هرمز هدف حمله قرار گرفت.
در این اطلاعیه به هویت نفتکش، عامل حمله یا میزان خسارت احتمالی اشاره‌ای نشده و سازمان عملیات تجارت دریایی بریتانیا اعلام کرده است مقام‌ها در حال بررسی این حادثه‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78639" target="_blank">📅 16:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STWNfhwpAN45T6_jPc_Jdund07QoxS9YstSmP5XrJwlQlGi8H9vvO_If4UMreEgah7bTOfCPvOexx-dk5QwlK8WwfKMa3634e-r3TuH527CQ536WdCX8qgBqz5S1Od5JDZvtTsqxj5d_dsenYQgQn7SdlHqDPzcovYQgpUb_YIYKabbeIKlGKJOn0NuslEwrRFg8mHynaQtHcGS2xElwiTTddzPpxOltD4yytq3VVd2YuLWMGCG5Q5ptPXjs0E_e1583f10Q-N_AefpbY7CPYrnShNp7MGvsoa11ckR_Rb-rCG90X0X35TJmP416DRdAxpQNbMLi-z690TeNrPMuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز سه‌شنبه ۱۴ مهرماه اعلام کرد شامگاه دوشنبه، فرودگاه بین‌المللی ملک عبدالله بن عبدالعزیز در جازان و فرودگاه بین‌المللی نجران هدف حمله قرار گرفتند.
براساس این بیانیه، این حملات منجر به جراحت جزئی سه نفر و بروز خسارات مادی به فرودگاه‌ها شد.
شورشیان حوثی مورد حمایت جمهوری اسلامی دوشنبه از حمله به فرودگاه‌های عربستان سعودی خبر داده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78638" target="_blank">📅 16:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78637">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwIInfF7OuBCiBpSJ2hVu6ZNBfx7FsArfpYciJFw_h5egW7Iui-0iwF4seZSpyzEWLr05VVUKYB49guTXebGxOzdFxhMDVZ8_8D6uxXZ4eLk6LAlte8pVP3Aj1aOjzbTjJ2k5a0uVDtnFqel53czy93q73pyHwvhsOisG9kdM4vws7facQTpngRpywhP-nHx13kaspNyDRqS_hbJts6rvdEfy8JFbKs6V0HUfkmuMo3VhfOITgjKNlYaPwHVSn8uHmrUm7sjp5iMC9tu9s8B1uEMrouYLSgh5lPXcVB0FaUPxVXU7OP-yxRq7yLNjoAKX9cbvy6blERcuY5WMmlLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ کشور قاره آمریکا در بیانیه‌ای که روز دوشنبه، ۱۳ مهرماه، منتشر شد «اقدامات تروریستی» جمهوری اسلامی و نیروهای نیابتی‌اش در نیمکره غربی را محکوم کردند.
در این بیانیه به «تلاش‌های خصمانه ایران و نیروهای نیابتی‌اش از جمله نقشه‌های مرگبار، تأمین غیرقانونی پول، مداخله سیاسی و فعالیت برای نفوذ خارجی» اشاره شده است.
این بیانیه اشاره می‌کند که هدف از این گونه اقدامات «تقویت شبکه‌های تروریستی، تضعیف فرایندهای قانونی یا دولتی و ضربه زدن به امنیت منطقه‌ای» است.
ایالات متحده، آرژانتین، کانادا، کلمبیا،‌ کستاریکا، جمهوری دومینیکن، گویان، پاراگوئه،‌ پرو، و ترینیداد و توباگو امضاکنندگان این بیانیه هستند.
این بیانیه پس از آن منتشر می‌شود که آمریکا و پاراگوئه در ماه سپتامبر گذشته به طور مشترک «نشست مقابله با تروریسم فراملی» را با هدف همکاری در نیمکره غربی علیه «فعالیت تروریستی» تهران برگزار کردند.
سال گذشته اکوادور که متحد آمریکا است سپاه پاسداران، حماس و حزب‌الله را سازمان‌های تروریستی اعلام کرد و آرژانتین نیز در بهمن‌ماه ۱۴۰۴ نیروی قدس سپاه پاسداران را در فهرست تروریستی قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78637" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZHNU4TqamCJSpIttP0Sbh7WFqT9bt7Lf1__qV07qptXTR7mZNNT253GrjZ-2MIekx6tUZXhs2O0yniH00SFd4qWd9iOhiajYnvno8LLMEUt__lssUzTo5pfbLO3asSX3dqJgpafFiIImd4WMI4HqSkmY3WtUVSzxT9MijiaoTMR157UzUaFc2sV-wV4f3Kx6F9cte_WaGqah11UVzbA-GUIvGSKS22Bh01cKpwUh_FNbsG6zjUu_wQpmAYLEHihE6882eiiT5GmN82ZxsQ7R3wspMhuEm7HCMwSt6fjbl0LLb05qbAEczfux-GszEHMZ1CAM2Hrxsl4p4U7a4EfYqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی عباسیان، ۳۸ ساله و ساکن شیروان، از سوی دادگاه انقلاب بجنورد به اعدام محکوم شده است.
یک منبع مطلع به ایران‌اینترنشنال گفت حکم اعدام عباسیان یکشنبه ۱۳ مهر در زندان شیروان به او ابلاغ شد.
هادی عباسیان در جریان اعتراضات دی ماه با انتشار ویدیوهایی از مردم خواسته بود در اعتراضات شرکت کنند.
تاکنون اتهام دقیق منجر به صدور حکم اعدام و مستندات دادگاه علیه عباسیان مشخص نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78636" target="_blank">📅 16:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78635">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGE4UWLu9nr34B1o-HgBsTt2f0UAMsjQtdASOt26rYyYUKgczI_kmFsWGr_L_SHnJE7XRgh0U7AfGBmR97T9_dokqO4mxQfCOOUiAGxKw-ZHor8ttWNy--a_b3FLnWbfKskTrEMAQ-YbO41xsFRmT8j7Hc7OhaF_l6agDySdcK5g8CGoHhaPOctR4n7qcVW4MUs1XNqN_NXwStKhBOmB6h8S_NZttAfh02Gawd4JVojFAUzb6rYa66eaPwF4Hbd981642VA4PPVTaJvX35FJrxo_RGvE2MzOdheqGnf-NbWWTSvLahqC_VDYSNkVMwwR0zvCSvwhb936xYolN4Tsyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر ایران از اجرای مخفیانه حکم اعدام «تورات محمدی»، شهروند ۴۲ ساله افغانستان، در زندان مرکزی کرج خبر داده است. او با اتهام «جاسوسی» به اعدام محکوم شده بود، اما مشخص نیست دستگاه قضایی جمهوری اسلامی او را به جاسوسی برای کدام کشور یا نهاد متهم کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78635" target="_blank">📅 16:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vY3SP_BKeD8KuxvxmFkAiB6QrunuVkcjes9Tra1ppsRsMqMfHwSM9bvEfPHGsdmDyyF7iMt7ZHBAcP9PyH7kAPXcP3jRGbgNU0bfGDhl8k2IgcwWMtfDio3CPw9sc31eLcV1gy5rzb1t0vTKsMSDM7zrOiBniOxkwSfdKSAxltfVeJe2Ub6z3Pmw8lVwHkpey3n7E6vn8I2tfjpdCslhGtkl6eEggDwCr2lqcBKWWDG3UgVSD3dVWzVwIxcUjwDFZ-tCMfEX3nKD9apaE7ZM4AegZT8goPyP1W5BCuW-j-8qIz_U3piHWD6jU2G4MSQ1wfOTnCrn1o8HX1kARxPa7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p0cbCGqpXCgE_TgdG6OvjH1Ftdx4YY_D05yytXGLVG7uSTzFZ9UBlLShWFmYxpPD3vLZ6HKr65zjygYHN5E-mewsVknT1j2quXuBTDhtaXtmjSTVMnMaMKfITJrromDGX_L7Rbev_o2JscomFBBctRlqGaMSr8I2iGWxAj0Kc3c7KKrp-_VUZAtAr86AvhOALZqOYAcSMyfnxY4C2jx3D2_tY7Ns4HrdSsUmZnj6vI6U7FOXdsvuDhXYT4Sn6zLdOUfPvRHlDlD_b1LY74lg6Ce2f5o5xUkLD6CdSz75E6wf9v1an1F7FvJa5npvjO0Fu4P51O8bhT5Kw5DKmPps5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده در پی دریافت اطلاعاتی درباره احتمال حمله پهپادی جمهوری اسلامی، ۱۲ فروند بمب‌افکن بی‌۱ را از پایگاه هوایی فرفورد، متعلق به نیروی هوایی سلطنتی بریتانیا، خارج کرد.
وال‌استریت ژورنال علت خروج این بمب‌افکن‌ها را «نگرانی‌های امنیتی درباره طرح‌های احتمالی حمله به پایگاه» عنوان کرده بود.
دونالد ترامپ، رییس‌جمهوری آمریکا، دوشنبه تایید کرد بمب‌افکن‌ها به دلیل تهدید امنیتی جمهوری اسلامی از این پایگاه خارج شدند.
این در حالی است که مارکو روبیو، وزیر خارجه آمریکا، ساعاتی پیش‌تر این انتقال را بخشی از جابه‌جایی‌های معمول نیروی هوایی توصیف کرده و گفته بود ارتباط مستقیمی با تهدید ایران نداشته است.
@
VahidOOnLine
روزنامه نیویورک تایمز در گزارشی اختصاصی به نقل از مقام‌های آمریکایی و بریتانیایی نوشته است که آمریکا پس از دریافت اطلاعات جدید درباره احتمال حمله پهپادی که گفته می‌شود سپاه پاسداران آن را طراحی کرده بود، به‌طور ناگهانی هر ۱۲ فروند بمب‌افکن بی-۱ نیروی هوایی آمریکا را از پایگاه هوایی «آرای‌اف فیرفورد» در جنوب انگلیس خارج کرد.
نیویورک تایمز به نقل از این مقام ها که درخواست کرده اند ناشناس باقی بمانند نوشته:‌ «حمله احتمالی بخشی از یک طرح پیچیده و چندمرحله‌ای ایران برای هدف قرار دادن هواپیماهای آمریکایی و کشتن شماری از چندصد نیروی آمریکایی مستقر در این پایگاه بوده است. به گفته آنها، تمام بمب‌افکن‌های آمریکایی در آخر هفته از پایگاه خارج شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78633" target="_blank">📅 08:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QgM4jkvKtdo-Fh4iCHEGPSRwtAs8upaa1Ed7fpDh96w7KA_yYpURmVVkSdpt4BlpwEFt_fj4Wvc2vTwIeSCZMedxp00iKyeaHV3qg-YBSU8WuDeNJdH1-1tuB2FbdnNyA5i-xjltdoR6q2Io65n-q3ymd5XlSGjEb0WuB2PEUZJcoSJWD3SuVKSKBDsfn5sV-1HauV90tqU5mZnNwgrUA9BOCQY5YYGMcNyOz_0spcl8tCOOAWdBlM3ih4ro_53s6h7XZ0lLpKIKT2KKVeTgWieDhnTcB3YTpT7CiTRCs0r6atieJUxmreSPleDRGRtmX1leA16qBNiX6bCxOaFQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iT9LPBEvfVOMdYwCxu5BaQm7A19dKYl1UZtVB3IuQKBD0SQsjeZVbo3XycrjncUJFKjqki13W0wG_86RSbO2YocrntrJvVVOjOvivR0ppUMORI4TzDh87fVQnQx9wFVeJmfcCYrwEISVoQODI-h8dQP6M7pLiiZRB7d2UkUKQO2Qim9ejQQW_2nVWAsRx5Jr4qwhGNYkEFWsx0btAoSGKIaTpaAqUXJvFHruzO7EOqn_qeYMRmzVaTzRnBpAZqDbey3Sn8lht1D57pehXCd5HLPxbW9X2Kl68pyMUDplmFh78P_Kt0c5RPn_GOBs8a5rbtZT8ALNCo8hOch-om1gSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در پاسخ به سوال خبرنگاران درباره حادثه امنیتی در نزدیکی پایگاه هوایی فرفورد بریتانیا اعلام کرد که ایران با این پرونده مرتبط است.
ترامپ درباره دلیل خروج هواپیماهای این کشور از پایگاه فرفورد گفت: «ما با یک تهدید مواجه بودیم و اگر قرار باشد ما را تهدید کنند، هواپیماها را جابه‌جا می‌کنیم. این اقدام تا حدی مشکل را برطرف می‌کند.»
رییس‌جمهوری آمریکا تاکید کرد: «ما افرادی را که این تهدید را طراحی کرده‌اند می‌شناسیم و آنها خودشان را با دردسر بزرگی روبه‌رو کرده‌اند.»
@
VahidOOnLine
ترامپ روز دوشنبه ۱۳ مهر در کاخ سفید و در پاسخ به این پرسش که آیا احتمال می‌دهد ایران پهپادهای رزمی را به بریتانیا منتقل کرده باشد، گفت: «نمی‌توانم این را به شما بگویم، اما اگر چنین کرده باشند، بهای سنگینی خواهند پرداخت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78631" target="_blank">📅 00:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=NgLTRkwz5X2BM7u8yfsXXl4upPd6C22nHjTClLhJFHHRGjZACur-H5phKdnAkn9lXM6dIi-O_zOFEGQ2i2p7lwa5yQz28J-UUegfFwaLypavR1FBlGbedYHIPOPnKK68udxsBjR8Os8LpjGcsHxc428aIv9xPlBPUqVqDPqJLb2eSNjN9-Un-SFSv-kgX9eadn0TX9mlBNZFz7Jg2pFOEL54_1sHzeb6gOtZydt17JdqpdXiljlmgWw3AVs9Dh6inJ-xabNwfnaQYfkeESgLxeCYum2QhmD4iLO_EVWf9EksL9oNyxflG3ufrBxLmuUQHcUfaxz16jpVqVQ3AQjBZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=NgLTRkwz5X2BM7u8yfsXXl4upPd6C22nHjTClLhJFHHRGjZACur-H5phKdnAkn9lXM6dIi-O_zOFEGQ2i2p7lwa5yQz28J-UUegfFwaLypavR1FBlGbedYHIPOPnKK68udxsBjR8Os8LpjGcsHxc428aIv9xPlBPUqVqDPqJLb2eSNjN9-Un-SFSv-kgX9eadn0TX9mlBNZFz7Jg2pFOEL54_1sHzeb6gOtZydt17JdqpdXiljlmgWw3AVs9Dh6inJ-xabNwfnaQYfkeESgLxeCYum2QhmD4iLO_EVWf9EksL9oNyxflG3ufrBxLmuUQHcUfaxz16jpVqVQ3AQjBZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ هنگام ترک کاخ سفید، در پاسخ به سوال خبرنگار فاکس‌نیوز گفت: «شخصا باور دارم که ایران مسئول حمله تروریستی فلای‌دبی بوده است».
این اظهارات در حالی مطرح شد که جی‌دی ونس، معاون رئیس‌جمهوری آمریکا در همین روز به خبرنگاران گفت که هنوز مدرک مستدلی بر دخالت جمهوری اسلامی ایران در این حمله دریافت نکرده است.
در پرواز دبی به تل‌آویو که روز چهارشنبه انجام شد، کمک‌خلبان با حمله به خلبان اصلی تلاش کرد که هواپیما را با تمام سرنشینان که اکثریت آن‌ها اسرائیلی بودند، ساقط کند. این اقدام با واکنش به‌موقع خلبان و مسافران، خنثی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78629" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgI13fJingCBLi6-nZavdAB8TevKZQtiK0FEs4kHCSfhHXE0YMWYq4k8as5zC3n5bdH0QX5koNloV3wAojKVPmNz4BZCgUxSbsDT4Cv6xcvW7cDWIHtyht6I2KIFbKIk48_GuIffH6qsDXZe3Aj3prSZ9m3J7wBpyCTNM4HjL5L26f2WGsI7JPcK7qxbIuWKHmsNJeoP4mQNDRaTIKFqjlLQgCFrG0pmneD3It5iLV58aTh23-3b4lPsVFWF9OTsZV4jZJqcaqsbPIsGwh6tET1-c-xfEHfhi7cW-LIST17yxcikZinliEIQcW8TLiB0TF_YjV-EmNR0XmVedmvHvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید آنچه باعث افزایش قیمت گازوئیل شده دیگر ربطی به تنگهٔ هرمز ندارد، چرا که به گفتهٔ او، اکنون مقادیر بی‌سابقه‌ای نفت تقریباً به‌صورت روزانه از این آبراه خارج می‌شود.
دونالد ترامپ روز دوشنبه ۱۳ مهر با انتشار پیامی در شبکه اجتماعی خود، تروث‌سوشال، افزایش قیمت گازوئیل را به «پالایشگاه‌ها» مرتبط دانست و نوشت: «پالایشگاه‌های روسیه توسط اوکراین هدف قرار می‌گیرند و پالایشگاه‌های ما که در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط "دمکرات‌های احمق" تعطیل می‌شوند».
اشاره رئیس‌جمهور آمریکا به گزارش‌هایی است که در روزهای اخیر از افزایش میزان خروج نفت از تنگهٔ هرمز منتشر شده است.
شرکت کپلر، ناظر بر کشتیرانی جهانی، روز ۱۳ مهر گفت که داده‌هایش نشان می‌دهد صادرات نفت خاورمیانه، بدون احتساب ایران، طی هفته گذشته، با وجود حملات به کشتی‌ها در تنگهٔ هرمز، از سطح پیش از جنگ فراتر رفته است.
با وجود افزایش میزان خروج نفت از تنگهٔ هرمز، قیمت جهانی نفت در محدوده ۱۰۰ دلار در هر بشکه باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78628" target="_blank">📅 21:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد روز دوشنبه ۱۳ مهر یک پ نفتکش در حال گذر از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.
بر اساس این گزارش، این حمله موجب بروز آتش‌سوزی در موتورخانه کشتی شده که خدمه در حال اطفای آن بوده‌اند. با این حال، سازمان تجارت دریایی بریتانیا تایید کرد که تا کنون هیچ‌گونه تلفات جانی یا خسارت زیست‌محیطی گزارش نشده است. تحقیقات در این زمینه ادامه دارد و به سایر شناورهای عبوری توصیه شده است با احتیاط کامل در منطقه تردد کنند.
@
VahidOOnLine
پیش‌تر:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز دوشنبه ۱۳ مهر، با انتشار اطلاعیه‌های رسمی، وقوع سه حادثه امنیتی جداگانه را در آب‌های تنگه هرمز و در تاریخ‌های ۱۱ و ۱۲ مهر تایید کرد. پیشتر خبرگزاریهای فارس از هدف قرار گرفتن یک نفتکش در روز شنبه خبر داده بود و روز یکشنبه نیز ایرنا از شنیده شدن صدای انفجار در حوالی جزیره قشم خبر داده و احتمال هدف قرار دادن «شناورهای متخلف» را مطرح کرده بود.
بر اساس هشدارهای رسمی UKMTO، روز شنبه یک نفتکش حامل نفت خام حین تردد در تنگه هرمز، هدف اصابت یک پرتابه ناشناس قرار گرفته است. روز یکشنبه نیز دو شناور شامل یک نفتکش حمل گاز مایع (LPG) و یک نفتکش دیگر حامل نفت خام که از سمت خلیج فارس وارد شده و در حال گذر از تنگه هرمز بودند، توسط پرتابه‌های ناشناس مورد اصابت قرار گرفتند.
سازمان UKMTO ضمن آغاز تحقیقات رسمی درباره این حملات، به تمامی شناورهای تجاری و نفتکش‌ها توصیه کرده است با احتیاط کامل از این منطقه راهبردی عبور کرده و هرگونه فعالیت مشکوک را فورا گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78626" target="_blank">📅 17:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NZkwSLf5bMlF-BN_GkWfyIzHtJlPlkGUaB46UCbYo3Y5goqcmGWP2vP9CmOXP7oa8Vsvlmr3tL-0Hd41jBaK-MQ5T--zVdvouYPOksJBm2hsGyDwEVbV-nrNMJM-aZO5faIOZHi0pK1INF-V3Vnbf10rMYXFNSsyGS38LWWIapVfBybjRl7bJ24jt6kqWd67OK3w5Ctdtu05lctimzH9c0zIeXcc2u_zhBn9yrj6AsclIC3oEYCSGfJvTeeUNd3lSq2o4ArcQwOXkniQdqhq3TRIzjsgqpZHcKk9YhAPVa6VeMJoMGjA6Zytb4wAnyXL7mcyz1qnbw5z0NryfgCDyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا رئیسی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴ را اعدام کرد
- علیرضا رئیسی سحرگاه روز دوشنبه ۱۳ مهرماه همراه با علیرضا سپاهی، از دیگر بازداشت‌شدگان اعتراضاتدی ۱۴۰۴، در زندان دستگرد اصفهان اعدام شد.
- روز گذشته برخی منابع خبری از فراخوانده شدن خانواده علیرضا رئیسی به زندان دستگرد اصفهان خبر داده و گفته بودند این زندانی سیاسی برای اجرای حکم اعدام به سلول انفرادی منتقل شده است.
- علیرضا رئیسی فرزند دختر عموی جاویدنام رامین رئیسی از کشته‌شدگان اعتراضات دی۴۰۴ است. رامین رئیسی ۱۹ دی‌ماه با شلیک مأموران حکومتی در جریان سرکوب اعتراضات کشته شد. پیکر وی را ۲۸ دی‌ماه به خانواده تحویل دادند که در «باغ رضوان» اصفهان به خاک سپرده شد.
- علیرضا رئیسی روز پس از خاکسپاری رامین رئیسی بازداشت شد. خانواده علیرضا تا ۲۰ روز پس از بازداشت فرزندشان هیچ خبری از او نداشتند. او طی آن سه هفته زیر شدیدترین شکنجه‌ها و فشارها برای اعتراف اجباری علیه خود قرار داشته و حتی تهدید به تزریق آمپول هوا شده بود.
- علیرضا رئیسی و علیرضا سپاهی از متهمان پرونده «میدان علیخانی» اصفهان هستند که به اعتراضات شامگاه ۱۸ دی مرتبط است و نهادهای امنیتی مدعی کشته شدن چهار بسیجی و مأمور یگان ویژه در جریان این اعتراضات شدند.
- در پرونده «میدان علیخانی» ۱۲ شهروند به اعدام محکوم شدند. با اعدام علیرضا رئیسی و علیرضا سپاهی، شمار اعدام‌شدگان متهمان پرونده «میدان علیخانی» به هفت تن رسیده است.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78625" target="_blank">📅 16:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78624">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ognXbJ8ZE6VW835-DA70jrhcTmD1F4YeBv_2BEY9chnbTqWb7uEngQzIE91QVyZUv1548_MYzki9qlLZXRa8Sf1pIHUHiqGEZGXxPhmNjfplX5zWiq8vuwPrvkSlR9QsiuVA5KyoGTvBpCHJoq8Mp_psPFHrRc6YCz9R5WJSCQVUdAj8UrBFl6yPcNUbX3-tt8AqvpcZVlpvf4j00VKsoZMR7hbxCNRXbfagiqK9KWTwIt9fkSqqG5YkRA_-E_Axiy0fflZAubHSXuBgIRUoi9SRJBWm7VUvnc1mY3A13-4oGOEZljrTNOKN_G1hBXFC3iWshHpAsWXiD6hUuAjREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا سپاهی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴  را اعدام کرد
- خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام علیرضا سپاهی بادجانی، معروف به علیرضا سپاهی، در سحرگاه روز دوشنبه ۱۳ مهرماه ۱۴۰۵ در زندان دستگرد اصفهان خبر داد.
- وکیل علیرضا سپاهی روز گذشته با اعلام خبر فراخوانده شدن خانواده علیرضا سپاهی برای ملاقات با او و انتقال این زندانی به سلول انفرادی، از خطر اجرای حکم اعدام وی خبر داده بود.
- علیرضا سپاهی پیش از اعدام و به صورت تلفنی با نامزدش عقد کرد. مهشاد کشانی، دانشجوی ۲۲ ساله ساکن اصفهان، نیز در اعتراضات دی۴۰۴ بازداشت و به پنج سال حبس تعزیری محکوم شده و در زندان زنان دولت آباد اصفهان محبوس است.
- علیرضا سپاهی قرار بود سحرگاه سه‌شنبه ششم امرداد ۱۴۰۵ به همراه ابوالفضل سپاهی بادجانی -پسرعمویش- و امیرحسین صفری حسین‌آبادی در ملک شهر اصفهان و در ملاء عام اعدام شود اما پیش از اجرای حکم به علت استرس دچار سکته قلبی شد و اجرای حکم اعدام او عقب افتاد.
+- علیرضا سپاهی چهارمین شهروند بازداشت‌شده در اعتراضات دی۴۰۴ است که طی هفته گذشته و پس از صدور بیانیه ۴۶ کشور در محکومیت اعدام‌ها در ایران، احکام اعدام آنها اجرا شده است. سیاوش جمشیدی خیرآبادی شنبه ۱۱ مهرماه در شهرکرد و علی همتی سیستانی و مجید نیک‌اندیش روز چهارشنبه هشتم مهرماه در مشهد اعدام شدند.
- پرونده معروف به پرونده «میدان علیخانی» به اعتراضات شامگاه ۱۸ دی ۱۴۰۴ مرتبط است که در محدوده میدان علیخانی، میان ملک‌شهر و کاوه اصفهان رخ داد. نهادهای امنیتی جمهوری اسلامی مدعی شدند در جریان این اعتراضات چهار نیروی بسیج و یگان ویژه کشته شدند.
- با اعدام علیرضا سپاهی، شش متهم پرونده «میدان علیخانی» اعدام شدند. عرفان اسفندیاری و گل‌محمد محمدی ۲۸ تیرماه در زندان اعدام شدند. ابوالفضل سپاهی و امیرحسین صفری در تاریخ ششم امرداد در «میدان علیخانی» در ملاء عام به دار آویخته شدند و قائم حسینی نیز ۲۹ امرداد در زندان مرکزی اصفهان (دستگرد) اعدام شد.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78624" target="_blank">📅 16:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78623">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/An-WMq50ArR9GbD_u7odf_74RRrhXRBSwLwSern82OmTlZx96KUiBK2ODhgQ8LmVftXh8JsBOP7jinnHyzRrHs8bPpbawXqANl_MBccxWmVZTeTYvADhilba8L20a9_4o2KiZWL2BxP40fegrMwxeOwwLd8vSt6fAHIkpehz3EIQX87RBCYPPrcIisbs36YPEtaEEm897VhloVgmShu39wUDnHXi4GOWDX6T7Wx8aWW-A29l9ns7YAmRqAYfdLDYLFRZgI2OSgj_O4AdKaMPwuzijGmhqILsukioGPVSqMye3MwdGcLBAVhwtKaeJvxIdMM7hDCSzh-bywIBqMWUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت ایران در پی افشا شدن توقف کامل بارگیری نفت خام کناره‌گیری کرد
معاون ارتباطات و اطلاع رسانی دفتر رئیس‌جمهور ایران روز یکشنبه ۱۲ مهر اعلام کرد که استعفای محسن پاک‌نژاد، وزیر نفت، مورد پذیرش مسعود پزشکیان قرار گرفت.
مهدی طباطبایی در شبکه ایکس نوشت که حمید بورد به به عنوان سرپرست وزارت نفت منصوب شده است. بورد به عنوان معاون وزیر و مدیرعامل شرکت ملی نفت ایران فعالیت می‌کرد.
کناره‌گیری پاک‌نژاد از وزارت نفت در حالی رخ داده که محاصره دریایی ایالات متحده علیه ایران که از ۲۳ تیر ماه دور دوم آن آغاز شده است، صادرات نفت ایران را به‌شدت کاهش داده است.
وزیر خزانه‌داری آمریکا روز نهم مهر اعلام کرد: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت هفته گذشته در گفت‌وگو با شبکه فاکس‌نیوز اعلام کرد برآورد دولت آمریکا این است که حدود ۱۵ میلیون بشکه نفت ایران همچنان در مسیر تحویل، عمدتاً به چین، قرار دارد و پس از تحویل این محموله‌ها تهران «چیزی برای تجارت در برابر هیچ چیز دیگری» نخواهد داشت.
محسن پاک‌نژاد ساعتی پیش از استعفا، بر اساس ویدئویی که رسانه‌های ایران منتشر کردند، گفت درآمد ناشی از نفت فروخته شده «وصول» می‌شود و این روند ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/78623" target="_blank">📅 21:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78622">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSncJbqYEhXInKVZcd-QApBLPVSJfxvR4-lYjcQqkuhtFDjCGdfMVxTvotIcTaSHhq3RPsNGxF6wzJd8g5fMoOph-vksHqtfr4TeCUlsd5BqL9Y8VAYspTNNQfT-bh6tL244eh2DXZlQnLlbMRKnz9qXzP-hOmI4fyRwZdrQPc8MHj16pMsBg3NPrxrrR-VeKsqJNrteP3CioTvO7km5zS2K69p7Gll07fM1XTBs4oXhlOQ8MEfga4HKKoUiecOn_cuav6qgoQwS9yuSJvR3Yp7yBIIWCRsSgOOqYuUO7vZKW9rJ3Mi2ZQi68wHxCnYKWkYv8YPxb1EGPIXW9Ejqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار ارز و طلا در یکشنبه ۱۲ مهر همچنان در مسیر صعودی قرار دارد. قیمت دلار آمریکا با افزایش نسبت به روز گذشته به ۲۷۳ هزار و ۱۰۰ تومان رسیده است.
دلار در ساعت ۱۵ روز گذشته ۲۶۸ هزار و ۵۰۰ تومان بود و به این ترتیب در کمتر از یک روز ۴ هزار و ۶۰۰ تومان، معادل حدود ۱.۷ درصد افزایش قیمت داشته است.
یورو نیز از ۳۰۲ هزار و ۲۰۰ تومان به ۳۰۷ هزار و ۴۰۰ تومان رسیده و پوند انگلیس با افزایش از ۳۵۲ هزار به ۳۵۸ هزار تومان معامله می‌شود. درهم امارات نیز به ۷۴ هزار و ۳۵۰ تومان، یوآن چین به ۴۰ هزار و ۸۴۰ تومان و لیر ترکیه به ۵ هزار و ۶۴۰ تومان رسیده‌اند. قیمت تتر نیز ۲۷۱ هزار و ۶۰۰ تومان اعلام شده است.
در بازار طلا و سکه نیز روند افزایش قیمت ادامه دارد. بر اساس نرخ‌های منتشرشده امروز، هر گرم طلای ۱۸ عیار حدود ۲۶ میلیون و ۳۸۵ هزار تومان و سکه امامی حدود ۲۷۳ میلیون و ۸۳۰ هزار تومان معامله می‌شود. سکه امامی نسبت به نرخ ۲۷۰ میلیون و ۹۰۰ هزار تومانی روز گذشته حدود ۲ میلیون و ۹۳۰ هزار تومان افزایش داشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78622" target="_blank">📅 15:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78621">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS5VN5q_fcCXQUBlC-06jZvMAQmkSWw4D0il1O4uNOj--wuoWJ88PrUDgJelnxyOXpMkymgcmgn0o_5kzluU0O3qGcMY0ouZtQUiZpu7RQ_FyAJ7q4AmLnOw9yB1N4Upwkie7Y45hpgFRVs7q-zoPHoymqKpYMHPOn8Xfln7ads-EPjJLxBeP92NxEaTc6ypq1Zoqwpx00NVsqTbRvlkiIkoA2KwXn-Y_vaKDeO2PuXNzFr0xjFeyWaWs9h88Sjf1l47au-M3qt-sqZ91n_HeWXRSMpF6ROiIPYxLG9aSnhET8w23_rlMIjsCxd9DbFH5QABr6X2xlLYhTQ_XNx01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه ۱۲ مهر با اشاره به دیدارهایش با مقام‌های کشورهای منطقه گفت این رایزنی‌ها «بسیار موثر، محترمانه و دوستانه» بوده است.
او افزود: «ما مسیر جدیدی برای ایجاد اعتماد میان کشورهای همسایه و جمهوری اسلامی ایران آغاز کرده‌ایم و به‌خصوص در حوزه خلیج فارس، این مسیر را به خوبی طی می‌کنیم.»
وزیر امور خارجه جمهوری اسلامی همچنین گفت کشورهای حوزه خلیج فارس در این روند با ایران همراه هستند و به گفته او، «اراده مشترکی برای ایجاد صلح، ثبات و امنیت در منطقه خلیج فارس، با مشارکت خود کشورهای منطقه، شکل گرفته است که اکنون به‌طور جدی دنبال می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78621" target="_blank">📅 15:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78619">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/smMpMdfuVvwNnH0K3b-nl57w9K9Bj7q-fu0Qd-gduM__rVUAOgbgK0xIc3betBCfxY5rZ5mAR7Vc51ohl7BWXCpHipncA3hK33tL-RLt8tFUlhyljrvmZ3nfVd1YRmAnoYobDl-2KV96hkvQPgChMWmUrvsJq-hATcFq_0eSmLzyaE9c57nR9_3zm5dHGC_LoDjiWOwo7rl6OCBG2XhEvcNQBgkqnfKGfmB5MCwT8xPtUzTNB9PJMmfnVm5X-2FHw2RrlTJ20RHAezpRa3QRlaiUhcPGgxOC5NwT1XLh_fA1lGtfJsivqf1q7YYmkt1gDqwZfV6dYeBAmg-u-kT-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=BbX2F4EjJhiA74x0BBaC34LKRTMMy2HBKO995tJIfZkIwWBQ0ERx0E-WGxbY4ZRpXh2MOSkoe5TS0Sjlad8kkzi1m62X8Rpan69BBDJvSRHGsngkn65astQZgUYMb0qsPaF5YKlF-wFQq0ApgrB5Ado3BjKjtYo2M2DmZLAcKYjqAV3OjhlrbpKm5PqOYmdiUThuDoWgdNpqI96nE5a_S4Bz_IW335qAYWDxNaCp5eQqTzIbcCPbzZIpkNAJcJZCHlLlWrpKGa6y7PVStyb2C3byI_XxIiOs7ZJ_nZdX_Da0g2WJ8l-rx0_UxXmmTVhSUCntdMZD_A6LxZA3pj3jnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=BbX2F4EjJhiA74x0BBaC34LKRTMMy2HBKO995tJIfZkIwWBQ0ERx0E-WGxbY4ZRpXh2MOSkoe5TS0Sjlad8kkzi1m62X8Rpan69BBDJvSRHGsngkn65astQZgUYMb0qsPaF5YKlF-wFQq0ApgrB5Ado3BjKjtYo2M2DmZLAcKYjqAV3OjhlrbpKm5PqOYmdiUThuDoWgdNpqI96nE5a_S4Bz_IW335qAYWDxNaCp5eQqTzIbcCPbzZIpkNAJcJZCHlLlWrpKGa6y7PVStyb2C3byI_XxIiOs7ZJ_nZdX_Da0g2WJ8l-rx0_UxXmmTVhSUCntdMZD_A6LxZA3pj3jnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز شنبه، با اشاره به تحولات جاری میان تهران و واشنگتن به خبرنگاران اعلام کرد که به‌زودی درباره ایران تصمیم‌گیری خواهد کرد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه «ایران درهم کوبیده شده است» گفت: «تصمیمی است که درباره ایران خواهم گرفت. تنها مسئله این است که یا از راه آسان خواهد بود یا از راه سخت. ما این موضوع را یا از راه آسان حل می‌کنیم یا از راه سخت.» او در ادامه افزود: «ضمنا همان‌طور که می‌دانید، ایران عملا از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.»
@
VahidOOnLine
پیت هگست، وزیر دفاع آمریکا، روز شنبه، ۱۱ مهرماه، از پاسخ به سوال‌ها درباره اعزام ناو جدید خودداری، اما تأکید کرد که رئیس جمهور آمریکا «مصمم است» از دستیابی حکومت ایران به سلاح هسته‌ای جلوگیری کند.
هگست که روز شنبه با خبرنگاران سخن می‌گفت از پاسخ صریح به این پرسش که آیا جنگ با ایران تا پایان سال جاری میلادی، سه ماه دیگر، به سرانجام خواهد رسید خودداری کرد و تصمیم در این باره را با دونالد ترامپ دانست.
روز شنبه، چند رسانهٔ خبری آمریکا گزارش دادند که پنتاگون در حال اعزام ناوگروه ناو هواپیمابر «تئودور روزولت» و یک گروه آبی‌ـ‌خاکی تفنگداران دریایی به خاورمیانه است؛ اقدامی که در صورت اجرا شمار ناوهای هواپیمابر آمریکا در منطقه را به سه فروند می‌رساند.
وال‌استریت جورنال به نقل از مقام‌های آمریکایی بدون ذکر نام آنها نوشت این اعزام، همراه با گروه آبی‌ـ‌خاکی «ماکین آیلند»، بین ۹ تا ۱۰ هزار نیروی نظامی دیگر به منطقه می‌افزاید. به نوشته این روزنامه، «تئودور روزولت» به ناوهای هواپیمابر «جرج اچ. دبلیو. بوش» و «جرج واشینگتن» خواهد پیوست که در منطقه حضور دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78619" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/assYvle5oENZTuwmxakHeMkgIJuo4MTxVCEcilzP_oLxlWbGJdVjRjMldTn3QJVZGhrqkZXEgrNvxlsmfuIUX_44QPg3Ofide0cQBPfKmgFAtSJ49jRRRZn5QcrUmbB3dPCzqflu-U90QWsi-vBzX_EpvsANxYcloHtMLD8sBpJ8nvbCv3jlJ4ozQY46JTTgPS_FlrUK2_3VZgFz59amvfOpjjXIeG19WvO2fNngzxtSoQUSz6BCm9slWYj54EmGuJNVxySkRZJzNYGMghtHzBsajc4Bra2fA2ddRvl7hj9KOcgIYfHceYKI5UB_T2t6YKu2l0gGjqxDk0rsms-lRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrInIOLrAuvzXJNNKNgfP0KkqcNEVpyw1LATCKo6rDBuuwI0PCk56v4pnKzejSRMXA4i2xO-UH6vVYR8-Po7q7P3K0BOBp6kr1hxRzuL5cJWEx4Kxpd-nHziVeQADsGWkI2D8xWjNIsaHicGCe-yd2bJVr4XDeVxZys3hFwvOnrAAnGcM7PmwciiraJYrxwQqpZdgmanrK-q6K0qtfr4RCiCXQdhaOGeLTvXmFIhc5tMkAjaSWP8OyJ-s1VbwZS5EYd4fi5jxCwYz0akCL_jHukgpFMpgZ0WU_V6zlNEhnqVoUREU08PGZlHGl7-lzLVqafcnXqo1dBFK2LVvx3JZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sc470wskQzRC70Z9kNp1YXi-4KtPgbFzmdWomFicLxj7dIgzN_aWdSO2fZre23cx6KYwvsB4vY4l8McfhXSoEimAZcu_JcbaFaqV20zm7ie-wdQ19mWIXQvZyk6ZtBB815Uc4-f3tbs1G02L9McFrJqehcuWEkfnx5wQd1MW3vR8upYFIzKZMQByvpl21f3jK3IIhk1kD4CJOkKaEBVY1MBdRyn73aDIJJZ2Oa-LJ85yMLvTAYyWAAPdlNk1vvUpQcBLNpdXqIEQ9jfToYBka4aBWqo7ybyr8-FC1K6-iBYElLuL7m6luAGLqUeVonof5bMw93zqRFy2bruiq3BPGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVPIiec5duYS1zT6FqdlhUB28fWqlkuv_8QmoC-XnK4MQIQSUPuBdiD07i6Y_1Pzm4DIs4N26E4-tj6-XrwtFtVKGaXfksUEqeX7Jvi8wADKYyBl27szx81xvoXKj-XN06mRW2dXypvHIVkSgAdquSk9MVfRPCEWAqFtsKBv61XzUIx9I7jSUvWb2VyERbWFHReU1A9e1-VnQjcTWvsHqZm45vFFQg-vFCc6H6p6dJ46q8TtUCU5qslypF1k2BuD5tgjza3hVSVZZXrake-9zkr9bfyq7re5FJTu-yz6iaeJg_fPBOIjxZW5eO2bx99GqW4VUzQQPzK1WEtolZu1xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
صدور و تایید احکام اعدام برای سه زن در پرونده‌هایی با اتهامات امنیتی، نگرانی‌ها درباره استفاده گسترده‌تر از مجازات اعدام علیه بازداشت‌شدگان و متهمان پرونده‌های سیاسی و امنیتی را افزایش داده است.
🔸
محبوبه شعبانی در پرونده‌ای به اعدام محکوم شده که امدادرسانی و انتقال معترضان مجروح از جمله اقدامات منتسب به اوست. مژده هاشمی بازرگانی، که حکم اعدامش در دیوان عالی کشور تأیید شده، از شکنجه، اعتراف اجباری و محرومیت از وکیل انتخابی سخن گفته است. سودا ابراهیمی شمس‌آبادی نیز با اتهاماتی از جمله فعالیت رسانه‌ای و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور به اعدام محکوم شده است.
🔸
هر سه زن با خطر اجرای حکم اعدام روبه‌رو هستند.
@IranRights</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78615" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EHM6mPrIq_AHZpQtdkeDIiK_golSrqVALORUPwRqGIEag_bqsNvueLCfImQY2ZjKu8g9TNW2V9GQIxghNTyrvlifnDOSDn6i8Hp2I921-M1LTSw1Zejl29Rhn9rOH7MzW3HcNXwwSdAZsuepcaTK_GSGpggzWiTdjpHAAsKGP4ARpz8_Iag8SJNe4B3Xz0K3t8SxwRLG19Ui4dv8jikQQG8w6DZTCdfxKCxH9HER9bY52ivX51E0-DwUiGHz1ys8UYqY9KhrjjERmT4WXJpaA9hrrmF83C1NauXJhZ1EKMEc1_jDRTQvHYJ8ud5yfq_i03MtAFyj5GavIpksta08Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس روز شنبه یازدهم مهر از شنیده شدن صدای انفجار در تنگه هرمز و هدف گرفته شدن یک کشتی تجاری در مسیر عمان خبر داد.
فارس مدعی شد، نفتکش «اور وینست» که تحت اسکورت آمریکا قرار دارد، هنگام ورود به تنگه هرمز سامانه رهگیری خود را خاموش کرده بود. این خبرگزاری دولتی نوشت، این دومین هدف‌گیری یک نفتکش در تنگه هرمز در روز شنبه است.
این خبر پس از آن منتشر شد که خبرگزاری مهر ساعتی پیش از شنیده شدن صدای انفجارهایی از سمت دریا در جزیره قشم خبر داده بود و احتمال ارتباط این صداها با شلیک به «کشتی‌های متخلف در تنگه هرمز» را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78614" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNWiqJ2pJ-WQodwKpsRQSJmFH6alGnz2Hyn3wma8jOAh1cT3Su6TRnAAndAl4CU87W1j0FsrilqUpMv1tYqbqXkhhKHqA4Uocyb1h0cwDDF5cUO8lhNklI0_kSA12BZQuCR7HRCge8Xnb0aY3ytBdVk75epTqaXeAJ1ptRA9iIK7aloYBbTJPWmKHHGdKL5ECzqWqRgJgROYtH6vwx8JMNu6RlSSR9eN8-i7D1z1-DyoYEDyHtWB8GA3EkNJB9cAvamZseP8ZgsI4nwvsP3mEssu-HTWeIlr5D3MsZoFmaPRPl662P16IG9qR9jvVeydRwFbk7G3wfIA5kfxl8VqYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌هایی از شنیده‌شدن صدای چند انفجار در جزیره قشم در عصر شنبه ۱۱ مهرماه، خبرگزاری مهر نوشت این صداها مرتبط با اقداماتی در خلیج فارس و تنگه هرمز است.
این خبرگزاری بدون استناد به منابع رسمی نوشت «هیچ اصابت یا حادثه امنیتی در پهنه سرزمینی جزیره» رخ نداده است.
خبرگزاری مهر در عین حال این «احتمال» را مطرح کرد که صداهای انفجار شاید به «شلیک به کشتی‌ها» در تنگه هرمز مرتبط باشد.
این در حالی است که همزمان، تصاویر متعدد و گزارش‌هایی در شبکه‌های اجتماعی منتشر شده که یک قطعه بزرگ و استوانه‌ای‌شکل را در محدوده‌ای شهری در قشم نشان می‌دهد که ظاهر آن به بخشی از یک پرتابه نظامی-دفاعی شبیه است.
گزارش‌های تأییدنشدهٔ دیگری در شبکه‌های اجتماعی نیز حاکی است که پیش از سقوط این قطعه، صدای عملیات پدافندی و چند انفجار در قشم به گوش رسیده است.
مقام‌های رسمی تاکنون توضیحی دربارهٔ تصاویر منتشرشده و این حادثه در قشم ارائه نکرده‌اند و رادیوفردا نمی‌تواند جزئیات گزارش‌های منتشرشده را به‌طور مستقل تأیید کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78613" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MdIQm3FuRPajZrY-vPXBvv9zfyF5vDlAyNAYJH4fq54f4Bfutei13zWwubEn_2tiJr5LABs_rv2PwuCKdWYPpTW7T_RivzYwu2GLdlvUD1WzMw-FRQ3ACPeVKxy6Ejp2USY7sl5BiKCIutlsBxvuz1bRSr1SpRUyxHpf66NcWHJsbpOaqvipmZUwzmRi-dtUXaB4mzwworXVevlSmH0KJZmn39bKqXn2MF7QOk18tL9xpHfz9ul5QHiQ007VLSTTbSpDlOZHJZR4BqZGa5ELumzqJTNn_ePMzSTe9272QB37YdHbNysNcpgIigdBiSdlxGedhAFcoeBoJ1kzdKjSAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از قشم  حدود ساعت ۱۶:۳۰:  صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم  همین الان قشم موشک شلیک کردن  16:34 دقیقه   وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن صداش خیلی وحشتناک بود معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد…</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78612" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lO1omlNY1d-pvvxz7quS2BcsgV83SjMBSX650KotaDPaHLB7TPuddD3nengP4asTQ8oqEmiN5Xx-DumiRbtrGjlgatakv_-i6HX00wswNKjeTVs-vX8LpQEeYnmYIni1QVjn2VRq12oOJ2doxVdHzwNmsqQd00NuCSae0IpDm6P_wAgDiZzDjCDGgxEv6ufnDH9REI4MCg3K-JywBv5ac9kdKk1b52ydqzvohkaGfuFvurfZg453LqL9rseWekeJH9W0HqiYiLmtDRuKze37RBqyBkCaVeqR29CfSTYlhqP52RWrWp9nFybTZBBHBAOOZnx1wEmSo6lAp5sZmQjlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند کاهش ارزش پول ملی ایران روز شنبه ۱۱ مهر ادامه یافت و بهای دلار آمریکا در بازار آزاد برای نخستین بار از مرز ۲۷۰ هزار تومان عبور کرد.
بر اساس نرخ‌های اعلام‌شده در ظهر شنبه، قیمت فروش دلار به حدود ۲۷۱ هزار تومان و یورو به بیش از ۳۰۵ هزار تومان رسید.
این در حالی است که روز پنج‌شنبه قیمت دلار در بازار آزاد حدود ۲۵۸ هزار تومان گزارش شده بود؛ به این ترتیب بهای دلار در فاصله دو روز بیش از ۱۳ هزار تومان، معادل حدود پنج درصد، افزایش یافته است.
افزایش قیمت ارزهای خارجی در حالی ادامه دارد که بانک مرکزی جمهوری اسلامی روز چهارشنبه از برنامه‌ریزی برای عرضهٔ دو میلیارد دلار اسکناس به بازار خبر داده بود.
قوه قضاییه نیز از برخورد با کانال‌ها و صفحاتی که آن‌ها را عامل «قیمت‌گذاری کاذب ارز» می‌خواند، خبر داده است.
اقتصاد ایران همزمان زیر فشار جنگ با آمریکا، تحریم‌ها و محدودیت‌های فزاینده بر تجارت خارجی ناشی از محاصره دریایی قرار دارد.
ارزش پول ملی ایران، از ۲۳ تیر، زمان آغاز محاصره دریایی آمریکا علیه ایران، تاکنون بیش از ۳۱ درصد کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78611" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFf5X9F3gJFx34s6SVSWb9ON0db1jiKqnQwLBGfmyHYAEP9xUXXqNyTABpcU53-z0IYyh6_YMJDFh5B078y3pvV7oDUiR1Ia3MpG0PWxTwTzzHhGhiAOkS9kjFbhE94BGddlcumTcd16faJQGTEkAdZjom9GHxNRma71woWBdqlqDDg0PsiDI7ULTEuMmNOCKltGvrB353LW5gZ4ReasMAzWNjFqU71wHP_0wBpNKbwib_uUkzWk_iK1i_v487jLbcULyGBny05vFShSPDsWubZc5Fmc2Ls6e3Rt8lL840R863AhJoxfBVioVVbHnsB2Ji8AYnMTNaw8fRoKUQTV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با رسانه آکسیوس،‌ با تاکید بر تاثیربخشی محاصره دریایی ایران اعلام کرد، ایران برای نخستین بار از زمان آغاز صادرات نفت، در هفته جاری هیچ نفتی برای بارگیری و انتقال از طریق دریا نخواهد داشت.
او همچنین با اشاره به کم اثر شدن نفود نیروهای مسلح جمهوری اسلامی در تنگه هرمز افزود، آمریکا عبور ۱.۱ میلیارد بشکه نفت از را از این آبراهه تسهیل کرده است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال منزوی کردن ایران «به شکلی بی‌سابقه» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78610" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpbwTWreI9I36kcv17RhaClxYeTJssMunRic_brt220oPxjkE-w6ZfBbyckRLgYF6mg5MDbQQvYTLHzo8aSpwjn9bRKM62IWHdP042xviU9JZppAwHsXxxK4oTwxBL56GgwXmY3rQR7lFHdiVLQP6pJOhRJIyRXS0OODqVvYs_qCxcas3Sdwh0PW59pAoAUD2ZU4i1ryUYJQJeGJlDlM6mv6jKIPlutSh9JtDmBrFwWZIWjpvU0co9QtZsB9sV5wLbBrfRnQAPf_igu8qhCguGzvuo-9Z8mmPXSVoTFMTDgxrx1DBKPk7kGQjEMNL5XHgZpLBpQnF31d-JsN6D9iYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا دو تبعه ایران را به برنامه‌ریزی برای حمله‌ای تروریستی علیه جامعه یهودیان منچستر متهم کرده است.
پلیس بریتانیا روز جمعه ۱۰ مهر ۱۴۰۵ این دو نفر را «سلام احمدیان»، ۳۶ ساله و ساکن لیورپول، و «رحمان صالحی»، ۳۴ ساله و ساکن سالفورد، معرفی کرد.
این دو نفر روز یکشنبه ۲۹ شهریور در منچستر بازداشت شدند و روز جمعه به اتهام انجام اقداماتی در راستای تدارک عملیات تروریستی تفهیم اتهام شدند.
قرار است احمدیان و صالحی روز شنبه ۱۱ مهر ۱۴۰۵ در دادگاه حاضر شوند.
پلیس می‌گوید این دو نفر برای پیشبرد توطئه ادعایی خود با فرد سومی در خارج از بریتانیا، که احتمالا در ایران حضور دارد، در تماس بوده‌اند.
به گفته پلیس، احمدیان و صالحی از طریق پیام‌رسان‌های رمزگذاری‌شده با این فرد درباره تهیه قطعات لازم برای ساخت یک بمب دست‌ساز گفت‌وگو کرده‌اند.
این دو نفر همچنین متهم شده‌اند که فایل‌های ویدیویی آموزش ساخت و مونتاژ بمب دریافت کرده، مایعات و تجهیزات مورد نیاز را تهیه کرده و برای شناسایی و بررسی اهداف احتمالی حمله از اینترنت استفاده کرده‌اند.
«ویکی ایوانز»، معاون دستیار کمیسر و هماهنگ‌کننده ارشد پلیس مبارزه با تروریسم بریتانیا، گفت این بازداشت‌ها نتیجه تحقیقات مشترک پلیس مبارزه با تروریسم و نهادهای امنیتی بوده و به خنثی‌شدن توطئه‌ای علیه جامعه یهودیان منچستر منجر شده است.
او اتهام‌های مطرح‌شده در این پرونده را «بسیار جدی» توصیف کرد.
این توطئه ادعایی هم‌زمان با اعیاد مقدس یهودیان، سالگرد حمله تروریستی سال گذشته به کنیسه «هیتون‌ پارک» و افزایش گزارش‌ها درباره حوادث یهو‌دستیزانه در سراسر بریتانیا خنثی شده است.
دولت بریتانیا دو روز پیش از اعلام این اتهام‌ها، جمهوری اسلامی را به دست داشتن در تلاش برای خرابکاری در پایگاه نیروی هوایی سلطنتی «فیرفورد» متهم کرده بود.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، روز چهارشنبه ۸ مهر ۱۴۰۵ در پاسخ به پرسشی درباره نقش ادعایی جمهوری اسلامی در حادثه امنیتی اطراف این پایگاه گفت واشینگتن در حال بررسی موضوع است.
پایگاه فیرفورد پیشتر در اختیار نیروهای آمریکایی برای انجام حملات علیه مواضع جمهوری اسلامی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78609" target="_blank">📅 17:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M9_R705h6KcJztxxhqEbk3f8XeFEwX7vs_tjW31AI8DYjOIxuHA1dCuN6VA6lK4Zwoldpeh6b9cwAWASyARNsxwoGjV6MV-r6OfIbYkjKzffJ22V-vvA3h2nakHWI77JkpCmb2jeD_f3ef-G6b4WXP_ToDmQrwafkBAELhgTLyacHVRK7vZmTdpQXV5uhe6llOJSd0CTMNZp8TSC8miAfdNgWaEP7z_ITbuCuK0luZ6ngmct5tsUIfzKCFu_ttr_n-ndXQDpHsSbhC4dPqCrNU69Wr00zLhvvlclGXKPIwusofWMNArTQiMxQXwOzbjxGhAxsVnJGC2v6ptiMmZ7MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZN8-lITtqo_Wx_-MIg7NzHhw7ajv3I791Ke2DrKxUESv6t2VKoIqai5VlOXsIomgKgvWmNJyYFbo-CMn2AzfowoysobNRxwKwJxkOeqjERAslEx1moLqx2OEio4VesZVtmBXsWsbszDqfdFmO7FegyRrpom-wZ6EssDsZngyEExGEXBLWa4_5BK_g22uU5vW8d3IRqofASLxBcKWeWhJ5WLyPxlHmgyTpX6gY75ChxY_ZYDocZjLZj5nYJYbNZLSQWcd-IN6opnb9zt8sOVvzjLyZP5ipjQVyHvr2GVRa0a6fp94z1MF8G2fxEJZ3MAURKw1L4DbmyDh8KW_nQT1Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: جمهوری اسلامی سقوط خواهد کرد و «روز آزادی» مردم ایران فرا خواهد رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مصاحبه‌ای اختصاصی با روزنامه دیلی‌میل که روز شنبه ۱۱ مهر منتشر شد، گفت که به اعتقاد او جمهوری اسلامی «سقوط خواهد کرد» و خطاب به مخالفان حکومت ایران گفت: «ایمان خود را از دست ندهید، روز آزادی شما فرا خواهد رسید.»
نتانیاهو در این گفتگو مدعی شد حکومت جمهوری اسلامی ایران در شرایط کنونی «بسیار ضعیف» شده و گفت محاصره آمریکا به رهبری دونالد ترامپ، سپاه پاسداران را به‌شدت تضعیف کرده است. او در عین حال تاکید کرد که سقوط حکومت ممکن است زمان ببرد.
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت اسرائیل با همکاری آمریکا، مانع دستیابی ایران به سلاح هسته‌ای شده است. نتانیاهو گفت: «اگر ایران اکنون سلاح هسته‌ای داشت، چه اتفاقی می‌افتاد؟» و افزود که جمهوری اسلامی همزمان در حال توسعه موشک‌های دوربرد است.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتقاد از سیاست دولت‌های غربی و به‌ویژه بریتانیا گفت آنها انتقادهای خود را بر اسرائیل متمرکز کرده‌اند، در حالی که به گفته او، تهدید جمهوری اسلامی و نیروهای نیابتی آن را نادیده می‌گیرند.
او خطاب به معترضان در بریتانیا پرسید چرا به جای اسرائیل، مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنند.
نتانیاهو گفت: «چیزی که به مردم بریتانیا می‌گویم این است: کجا هستید؟ کسانی که علیه ما اعتراض می‌کنند، چرا مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنید؟ چرا تمام زهر دولت بریتانیا متوجه آنها نمی‌شود؟»
او افزود: «چرا علیه جمهوری اسلامی جهت‌گیری نمی‌شود؟ چرا علیه نیروهای نیابتی آن نیست؟»
نخست‌وزیر اسرائیل همچنین دولت‌های غربی را متهم کرد که تهدید جمهوری اسلامی را به رسمیت نمی‌شناسند و گفت: «این حکومتی در ایران است که ده‌ها هزار نفر از شهروندان خود را کشته یا مجروح کرده است.»
او افزود جمهوری اسلامی اقتصاد غرب، منابع انرژی و آبراه‌های بین‌المللی را «خفه» می‌کند اما موج خشمی را که علیه اسرائیل وجود دارد، متوجه جمهوری اسلامی نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78607" target="_blank">📅 17:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE3ulyrTFMMc94ratkDTXwPn_DDb-KX0rZLqi8qCJwMx3b6sJQ7nMXfQcdKDQw3z0d7rY28txS-yqgr2RBd8Cj_I6e5LtB1ggtQENJn1NkfEfrJthy6sMi0Pw9ajOp5IcxF-yLyQ05QF01Mv1E53m-FG4nF8x2I_s73FPX6c_9w-YjgwYZiND3HZtdSNULNYz466Tw8Fljrb2_LVtQiBF6FRPDEyI-JV8Gd4HUfCe5RWiQifQLCEkhZW834Xil8MjoRwo21FyCm8Y8w1KfCP6Rv6ET-uza66-f5ycH5c0YYeeW_oNasS4JmTjDvCQ-IdjryRcyrF-wSq7bxYytYb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تیراندازی مقابل ساختمان دادگستری مهاباد در روز شنبه ۱۱ مهر، یک نفر کشته و چهار نفر زخمی شدند.
امیررضا رسولیان، فرمانده انتظامی مهاباد، اعلام کردە  این تیراندازی مقابل در دادگستری این شهرستان رخ داده و در جریان آن یک نفر کشتە  و چهار نفر زخمی شده‌اند.
یک منبع مطلع به ایران‌وایر گفت فرد مهاجم که چند سال پیش فرزندش را از دست داده اعضای خانواده فردی را که او مسئول قتل فرزندش می‌دانسته و در حال حاضر به عنوان متهم در زندان تحمل حبس می‌کند هدف تیراندازی قرار داده است.
به گفته این منبع، مهاجم پس از تیراندازی توسط مأموران انتظامی در محل بازداشت شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78606" target="_blank">📅 17:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhYrX-plTIxGHrQEC62KCWEDA0pRLtRBsZqBtetMV4PL2NZcmy3vyWVoLXcFZQ3pGZKFobtwCCNOFWOTelH1IFzk9DAyOlh2utFTRcGtzY0ZNlZmBk_P8DOXQ29IrBhejg-17OTiHkolP-3-uyPt3bTTdAYjWvLb_eZ2CYsnW2BGydTUMJEH4CQZjNoz-0dvBJ2XSxIWUz4nSYdlW8zKaQ-kT1oBPJXGh2VW1qFYwnGe4LXLUcqjHkfmZB6DD5JFhx5NXFJVduofk9GnmTJSK2ewVyjZmI_qRM-uC51RMsgfu-wJ0FWfK-gB5iDdS77FKN1s0ibCGqy5zVq9gJZmOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز شنبه ۱۱ مهر از بازداشت ۳۱ نفر در شهرستان سیرجان در استان کرمان خبر داد و آنها را اعضای چهار «شبکه سازمان‌یافته خرابکاری خیابانی» معرفی کرد.
این وزارتخانه مدتی شد افراد بازداشت‌شده برای شرکت در «فراخوان‌های سراسری» سازماندهی شده و در حال تهیه کوکتل مولوتف و ابزار تخریب دوربین‌های شهری بوده‌اند.
وزارت اطلاعات همچنین این افراد را به دست داشتن در «آتش‌زدن فرمانداری، تخریب بانک‌ها و ساختمان‌های دولتی و حمله به مقر پلیس» در جریان رویدادهای دی‌ماه ۱۴۰۴ متهم کرد؛ رویدادهایی که در اطلاعیه این وزارتخانه از آنها با عنوان «کودتا» یاد شده است.
در این اطلاعیه جزئیاتی درباره هویت بازداشت‌شدگان یا مستندات مربوط به اتهام‌های مطرح‌شده ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/78605" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nJ6fEc11XBOjLfASp7tO_2zvj5M2fgVGgyiUjT06Ij8KxvowIJ6DBcbIpkL-y1xHnSvNlLUlv7E_HtpoA-9vu0eMogWHyUiV6qLKdRs3Dk7GRjXQvdOMeqDkTW_MV9VWo3gvfGyoPYHinz_kQezzwaHCekthR5R7hsqjmiiYW3lHLjj_Q-yY4a5M3WT3Q8MvBIoo6pUGmdFpUO96WYMhWPAnI-vtzXIh2nGB4ToJhHY-GX-B2y5zi5kBsM23Kkcinrg9M4B5eSDpTVhiBJmAgwKueAfq_JpID47lIHYoW6PFkgHWqgW8XAMdZmepxynxMyjiowK7jiIY3lnlCZwqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام «سیاوش جمشیدی خیرآبادی»، از بازداشت‌شدگان اعتراضات سراسری دی۱۴۰۴، در بامداد شنبه ۱۱مهر۱۴۰۵ خبر داد.
قوه قضاییه همچنین ادعا کرده است که جمشیدی خیرآبادی شامگاه ۱۸ دی ۱۴۰۴ در خیابان ناصرخسرو شهرکرد به‌سوی ماموران تیراندازی کرده و سپس از محل گریخته است. براساس این روایت، او دو روز بعد، ۲۰ دی ۱۴۰۴، درحالی‌که یک قبضه سلاح کمری همراه داشت، بازداشت شد.
در اطلاعیه قوه قضاییه آمده است که حکم اعدام این معترض پس از تایید در دیوان عالی کشور اجرا شد. بااین‌حال، در این اطلاعیه توضیحی درباره زمان برگزاری دادگاه، روند دادرسی و دسترسی او به وکیل منتخب ارایه نشده است.
مقامات جمهوری اسلامی معترضان دی‌ماه ۱۴۰۴ را «کودتاگر» خوانده و آن‌ها را به ارتباط با آمریکا و اسراییل و تلاش برای ایجاد ناامنی متهم می‌کنند.
«مسعود پزشکیان»، رییس‌ دولت جمهوری اسلامی، نیز در سخنرانی اخیر خود در مجمع عمومی سازمان ملل مدعی شد که مردم ایران طی هفت ماه گذشته برای «دفاع از ایران» در خیابان‌ها حضور داشته‌اند.
او معترضان را افرادی توصیف کرد که به ادعای او، آمریکا و اسرائیل آن‌ها را «تهییج» و مسلح کرده بودند تا در داخل کشور ناامنی ایجاد کنند.
صدور و اجرای بسیاری از احکام سنگین علیه معترضان دی ماه از جمله احکام اعدام ذیل قوانین «تشدید مجازات جاسوسی» صورت می‌گیرد که از منظر حقوق‌دانان و فعالان حقوق بشر شامل موارد جدی‌ نقض حقوق متهم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78604" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پیام‌های دریافتی از قشم
حدود ساعت ۱۶:۳۰:
صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم
همین الان قشم موشک شلیک کردن
16:34 دقیقه
وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن
صداش خیلی وحشتناک بود
معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد بوددددد
قشم همین الان یه صدایی شد
سلام وحید جان چند دقیقه پیش یک موشک به سمت تنگه شلیک شد.
سلام وحید
دور و ور ساعت ۴:۳۰ جنگنده رد شد
سلام ساعت چهارو نیم بعداز ظهر امروز قشم  صدای جنگنده امد خیلی وحشتناک بود
[این پیام متفاوت هم بود که نمی‌د.ونم چقدر درسته. بعد از یک ساعت معلوم نشد صدای چی بود.]
قشم پدافند بالا نریمان و زدن
وحید
خیلی شدید بود صدا ها
معلوم نبود چی بود
رادار تازه ۳ روز بود درست کرده بودن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78603" target="_blank">📅 17:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78602">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=V6Wgs7ZpwMv4AvgGXFrHg0ttvzXPBcbpD5DC5iQnHNBFeV3hvAASEgJpjQrFmwoofm0cJ1MY6X-z9Exwu7vwlvkKk1QK3b_vQ-E8aSKxqxe41SrwOePAY5lDcKbXBzCHsax3ODEcrdZ-VLN__0RGdL7HVD5TipGcBYiDvsJQXtWQsLg1pTuA48AwCHHUzaMxVHYxPF4HP2Jkwa0OCP4KCox0VzzPJViiPUa3zO7HLt2Fv0y3qAFJzeQK0pWfM7czDu0JVotdVRvZi9RrmoVGz6rcqC4VAcokxdzjsDhJaC1dm-W2dv_0yk23jVbpZwBKHNB_pEZUL1htyfzXEt9BNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=V6Wgs7ZpwMv4AvgGXFrHg0ttvzXPBcbpD5DC5iQnHNBFeV3hvAASEgJpjQrFmwoofm0cJ1MY6X-z9Exwu7vwlvkKk1QK3b_vQ-E8aSKxqxe41SrwOePAY5lDcKbXBzCHsax3ODEcrdZ-VLN__0RGdL7HVD5TipGcBYiDvsJQXtWQsLg1pTuA48AwCHHUzaMxVHYxPF4HP2Jkwa0OCP4KCox0VzzPJViiPUa3zO7HLt2Fv0y3qAFJzeQK0pWfM7czDu0JVotdVRvZi9RrmoVGz6rcqC4VAcokxdzjsDhJaC1dm-W2dv_0yk23jVbpZwBKHNB_pEZUL1htyfzXEt9BNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز جمعه، در سخنرانی خود در آلاباما با اشاره به ضربات نظامی به ایران و انتقاد از برخی رسانه‌ها گفت:  آنها نمی‌خواهند موفقیت ما را ببینند. وقتی نیروی دریایی‌شان را منهدم کردیم، نیروی هوایی‌شان را از بین بردیم و چند ماه پیش ضربه‌ای مهلک به ایران زدیم، نیویورک‌تایمز و رسانه‌های جعلی می‌‌گفتند اوضاع ایران فوق‌العاده است. آنها همه‌چیزشان را از دست داده‌اند، از جمله رهبرانشان را.
او با تاکید بر خلأ رهبری در جمهوری اسلامی افزود: آن‌ها یک دور از رهبرانشان را از دست دادند، بعد دور دیگری را، و سپس نیمی از دسته سوم را. حتی یک دور رقابت راه انداختند که ببینند چه کسی حاضر است رهبر شود، اما هیچ شرکت‌کننده‌ای نبود و همه می‌گفتند من نمی‌خواهم.
بخشی از مشکل ما اکنون این است که اصلا نمی‌دانم باید با چه کسی طرف شوم. هیچ‌کس حاضر نیست رهبر باشد.
می‌گویم در ایران با چه کسی باید حرف بزنم؟ اما هیچ‌کس آن اطراف نیست.
در می‌زنیم، تق‌تق، ولی کسی در خانه نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/78602" target="_blank">📅 05:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f6XQwAbgmnnmtZwCN8fmDPSsQUIWp_5LLe3EOoewpKSzlI8zQ9zpI_pfwbec-OksQIghf8RIUJfW6ejAWF_pNPmSm2sRH57Wj_lcV0IehuVbJKGfh9HzeZMW1NQBpU5i0rBgxBlhWitJqo68cwtYbx5-3qwoDPpXFQPS-dZlon-r38Jf6yLrT6HmU_bpmqNn8KealgQCCi-q-VRa_onKF5Uq455jN33w4l3sOakFunkJQGxFcMQ0b-OtMO01k-jLKxa6MkGEUVGnLr8iGx4VYSTUS1ggwbHYFaFtcoEZsCLRUSufL07SOW6lhnyCNCQ0JB-bdFciDTBrjjnOXkMA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z_rV27D1T1Oklc5nMgPinIslKkmKljSO7K88BTM3MAy7EW9sNYLOkqlMziMrN_K6dAVsBmEPTuHk2sZYjARyfcCOMrHPMCd-7xOW8ZBBqPV51vIq7IeeDhqqshxIJxt-nZJoyJv3LrKV-UBvEeHcxdL-Msf_1PVC4XN4wXNtWzpMiM_0ypw2AndSJbLObxForY-xZa2cYkuwusT3vKG8z8w0zojDup9cLKdXGbgw0_q_D3w7mfEckxr88FqIhXz16jOv-H4YIXr-8pzI2j-I_MXgPC7mCYLWt3cNNofGfdaoOisr5AWwA4Hm3L3M5_f7z469GWoyJ4XILB5LZz3fng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وکیل «الناز شاکردوست» اعلام کرد دادگاه تجدیدنظر استان تهران، حکم بدوی یک سال حبس تعزیری و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری علیه موکلش را تایید کرده است.
الناز شاکردوست، بازیگر سینما، به دلیل انتشار یک استوری مرتبط با اعتراضات دی ماه ۱۴۰۴ به دادگاه انقلاب احضار و به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیزی و دوسال محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/78600" target="_blank">📅 18:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=WiLGjsj1Oj2AKqL2dnDlY02Phx2IKgGSYCknI1tOFZjPcElwNNffkDEvHm7qaMZTMRG-U24kvMLSzUFeqf-rmiO9QXBxe9AXig8IP4vMGrnYstVhxY-mE2CrtcS1-HCOH_YzQH1jVyEj_uLAJ6AI6oV1PnElSOcoPtMtwu9GJKAs6x2JoUzWbOnDJwNLBrMI9oFn-iq5hBpytijTcZ5euGMEJ0Ud99z-2o1M7D6nWtjG9CEHdW7ypSTiEsBSOgyD9bnYFCOmJOIOrHXVlWGVFcVxIKqRb4Ev6Csq49CDW7CIql8Ax9xl1bwlEafdUyRwIuTCkOzGWECON25G6ivhhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=WiLGjsj1Oj2AKqL2dnDlY02Phx2IKgGSYCknI1tOFZjPcElwNNffkDEvHm7qaMZTMRG-U24kvMLSzUFeqf-rmiO9QXBxe9AXig8IP4vMGrnYstVhxY-mE2CrtcS1-HCOH_YzQH1jVyEj_uLAJ6AI6oV1PnElSOcoPtMtwu9GJKAs6x2JoUzWbOnDJwNLBrMI9oFn-iq5hBpytijTcZ5euGMEJ0Ud99z-2o1M7D6nWtjG9CEHdW7ypSTiEsBSOgyD9bnYFCOmJOIOrHXVlWGVFcVxIKqRb4Ev6Csq49CDW7CIql8Ax9xl1bwlEafdUyRwIuTCkOzGWECON25G6ivhhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه پنجشنبه نهم مهر ماه، ویدیویی در شبکه اجتماعی تروث سوشال منتشر کرد که حضور گسترده معترضان در جریان اعتراضات سراسری
دی ماه
در ایران را نشان می‌دهد.
در این ویدیو، معترضان شعار می‌دهند: «امسال سال خونه، سیدعلی سرنگونه»
realDonaldTrump
این ویدیو رو ۳۱ دسامبر ۲۰۲۵ ده‌ها اکانت عربی و اکانت‌های مرتبط به یک سازمان سیاسی خارج از کشور منتشر کرده بودند و گویا بیشترین توجه رو هم در اکانت این مسئول اسرائیلی گرفته بود که بارها ویدیوهایی با شرح اشتباه هم منتشر کرده:
GadbanWaleed
اون روزها خودم هم کلی ویدیوی مهم از شهرهای مختلف ایران منتشر کرده بودم ولی به درستی تاریخ این یکی شک داشتم که مربوط به اعتراض‌های ۱۴۰۱ باشه و نگذاشته بودمش. به ویژه اینکه منبع اولیه‌اش اکانت‌هایی بودند که همیشه کلی ویدیوی قدیمی رو هم با شرح نادرست بین ویدیوهای روز منتشر می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/78599" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین باستانی Hossein Bastani</strong></div>
<div class="tg-text">🔻
معمای «تیم شش‌نفره» در حکومت ایران
مسعود پزشکیان اخیرا به «تیمی شش‌نفره» در حکومت ایران اشاره کرد که در مورد بحران جاری با آمریکا «اختیار دارند تصمیم بگیرند و تصمیمات با هماهنگی آنها اجرا می‌شود». به دنبال انتشار این اظهارات در مصاحبه با سی‌بی‌اس، رسانه‌های رسمی ایران روایت‌هایی را از ترکیب تیم شش‌نفره منتشر کرده‌اند که عمدتا در مورد پنج نفر مشابه و در مورد نفر ششم متفاوت بوده‌اند. بخش ثابت روایت‌ها اغلب بر رئیس‌جمهور، رئیس مجلس، دبیر شورای عالی امنیت ملی، رئیس ستاد کل نیروهای مسلح و فرمانده کل سپاه تمرکز داشته، هرچند نفر ششم را برخی رئیس قوه قضاییه و برخی وزیر خارجه دانسته‌اند.
اشاره مسعود پزشکیان به وجود این تیم، البته اهمیت داشت، ولی این اشاره نه اولین بار بود که صورت می‌گرفت و نه نشانه تحولی کلیدی در ساختار تصمیم‌گیری کلان، یا مثلا ایجاد نهادی با اهمیتی مشابه شورای عالی امنیت ملی بود.
در تیرماه گذشته، عباس عراقچی در مصاحبه‌ای با برنامه یوتیوبی «ماجرای جنگ» گفته بود چارچوب مذاکرات با آمریکا در شورایی تعیین می‌شود که به «کمیته شش‌نفره» معروف است. توضیحات او اما نشان می‌داد که جایگاه این کمیته پایین‌تر از شعام ـ شورای عالی امنیت ملی ـ و در حد یکی از کارگروه‌های داخلی آن است. عباس عراقچی در گفتگوی خود، مشخصا از کمیته‌ای «در داخل دبیرخانه» شعام سخن گفت که ابتدا «کمیته هسته‌ای» و سپس «کمیته مذاکره» نام گرفته و در نهایت به «کمیته شش‌نفره» معروف شده است. مطابق اظهارات او، این کمیته از مدت‌ها قبل از جنگ چهل‌روزه فعال بوده و در زمان‌های دبیری علی شمخانی و سپس علی لاریجانی در شعام، به‌ترتیب تحت مسئولیت این دو نفر فعالیت می‌کرده است.
البته روایت عباس عراقچی از قرار داشتن این کمیته زیر مسئولیت دبیر شورا، این ابهام را ایجاد می‌کرد که آیا ریاست آن، مانند شعام، با رئیس‌جمهور است یا اینکه سخن از جمعی شش‌نفره است که رئیس‌جمهور را شامل نمی‌شود، ولی جمع‌بندی‌های خود را به رئیس دولت ارائه می‌کند.
در هر صورت، عباس عراقچی تاکید داشت که تصمیم‌های کمیته باید «عینا مانند مصوبات شورای عالی می‌رفت، تایید می‌شد و بعد ابلاغ می‌شد»، که اشاره‌ای به لزوم تایید مصوبات از سوی رهبر جمهوری اسلامی به نظر می‌رسید. او همچنین، به این سوال که آیا تصویب آتش‌بس (موقت) در پایان جنگ چهل‌روزه «با نظر آقا مجتبی» بود یا نه، پاسخ مثبت داد، هرچند در مورد شیوه تصویب گفت: «ارتباط ما با کسانی بود که رابط بودند و مسائل از آن طریق منتقل شد.»
قابل تامل است که مسعود پزشکیان، که در مرداد ماه از دو نوبت دیدار با رهبر جدید جمهوری اسلامی خبر داده بود، در مصاحبه‌هایش در سفر آمریکا هم به همان دو مرتبه ملاقات خود با رهبر اشاره کرد، که نشان می‌داد دیدار جدیدی با مقام اول حکومت نداشته است.
به عبارت دیگر، با گذشت هفت ماه از رهبری مجتبی خامنه‌ای، ارتباط تیم‌های حکومتی با رهبر کماکان به حلقه «رابط» اتکا دارد که، در مورد آن حدس‌های متنوعی مطرح شده است. از جمله، گمانه‌زنی‌هایی که حسین طائب رئیس جدید سازمان بسیج را از افراد موثر این حلقه می‌دانند.
🔹
ادامه  مقاله در لینک زیر در دسترس است:
https://www.bbc.com/persian/articles/cr9dw7dvjxj1o
@HosseinBastaniChannel</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78598" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJ45COg5h3sNij_AdA5RmBGaE2YfHk5yuboE6D2uCbdXFmofY7239M-8wfdJurr-apNMcdlFLalYY1Zaw5OH7op3WJqEGhKFu0eb8Vqyvy_udlzasdWE1C_snvzKBxF2x-4Xq6NRk6NTYM-8UGUp7ISQjpyuYczAlRJYKoi3e_EyreNqN1J9VoKSrOUYCewMebJblRiKaggpGa9i91WMrF9Y8KNwlX9XrkTYcCnZS2STIOpnokr-SuLykI-eS2TPcQ_7O4V_GQD8G4sAMAMjoRKOUQ6stj9K4ZfqvALq_bUgv7NoZoAl3SPmkQv7EUDRacOXN8-jvWL4pRCr2jApOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری آمریکا می‌گوید ایران در ماه سپتامبر حتی یک محمولهٔ نفت خام هم بارگیری نکرده است. داده‌های شرکت‌های ردیابی نفتکش‌ها نیز نشان می‌دهد در این ماه هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت شامگاه پنج‌شنبه، نهم مهر، در شبکهٔ اجتماعی ایکس نوشت: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
این در حالی است که برآورد کپلر و ورتکسا از بارگیری نفت خام و میعانات ایران در ماه اوت حدود ۲۲۰ تا ۲۵۵ هزار بشکه در روز بود.
ایران همچنان مقداری نفت را که پیشتر بارگیری و در آب‌های آسیا ذخیره شده بود به خریداران چینی تحویل می‌دهد، اما این ذخایر بدون خروج محموله‌های تازه از ایران رو به کاهش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78597" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATUsvovwuPY-gN3gr7NVGCdqxxG31eRG3ZK4CJharxOozmHNMTX1x4AtGjrHWxm7-r_BP_ffFxagNn-u9Du2WOQmNCWt8Shf6mDryuvMCBcvSANyDbRfnFm5DxmRrN7W8NqkH_2GvmPDHTs-N7EXiJfvP7nlmzeBW50VhmAoW96sT1jwj3JyRKGdb5sMf2CzsDl7qSjgPb4xrs_uAabR-MS53uUYD2g1Bv4uHyHDK11N5jnkjTxrnL9pTXldzGdflDIzFCWPV7UBJqi6aVCgD6ImZVwhuReqyfTuPPTUfvH3GQQoNP1KP70s5JMAOoOiF3GNX7MZeRll8yOVNDNl3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز جمعه دهم مهر ماه، از وقوع درگیری مسلحانه میان سپاه پاسداران و اعضای «یک گروه تروریستی» در یکی از روستاهای شهرستان راسک در جنوب سیستان و بلوچستان خبر داد.
تسنیم با اعلام این خبر افزود نیروهای سپاه «در حال پاکسازی منطقه و بررسی وضعیت» هستند.
همزمان خبرگزاری حکومتی فارس نیز از آغاز «اقدام عملیاتی» سپاه پاسداران از صبح جمعه در راسک خبر داده است.
این خبر در حالی منتشر می‌شود که روز پنجشنبه نیز قرارگاه قدس نیروی زمینی سپاه با انتشار ویدیویی از یک درگیری مسلحانه، از کشته شدن ۶ عضو یک «گروهک تروریستی تکفیری» در منطقه منزل‌آب زاهدان خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78596" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XabmfW6Ta0ebDSe8bwSTi-y9J5lkWsJLExRr3EVB-ZDYGKdH-tPCkJ9nDv0v5IDrZSuMFP3IMRvQ65AGF6BPzlBINOfjnBjYYjMNLVNELrAsA1ITTDs-A_uU5MC7BBPwV8w3bI_V6Qx4erTZQqCPjAJbqXo0o5X2sBlKOHnIdY-m-2I9Q_bzCZJQPamu8VTGXcejVvG6yT-Dop4rmuNa3gx6CG6pWtwZ-BnpGWXQwx5H5SWcOuk-Z47R4fVRNWT5bZPi2xxCQYu5htBigtdgs4yFeqWTwWbdR6NaJ2prrBdq5BS33li8xxBZzc4luiBrsNKg7htBQgFdr6bdoVPCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در دو اظهارنظر تازه دربارهٔ ایران هشدار داد اگر مشخص شود تهران در حادثهٔ پرواز فلای‌دبی به مقصد اسرائیل دست داشته، «به‌شدت هدف قرار خواهد گرفت» و ساعاتی بعد بار دیگر گفت به اعتقاد او ایران «در آستانهٔ تسلیم‌شدن» است.
این اظهارات همزمان با ادامهٔ تحقیقات امارات متحده عربی دربارهٔ احتمال تروریستی بودن حادثهٔ پرواز فلای‌دبی و گزارش‌ها دربارهٔ تقویت حضور نظامی آمریکا در منطقه مطرح شده است.
رئیس‌جمهور آمریکا شامگاه پنج‌شنبه، نهم مهر، به وقت ایران، در پاسخ به پرسش خبرنگاران در کاخ سفید دربارهٔ احتمال ارتباط ایران با کمک‌خلبانی که به خلبان پرواز دبی به تل‌آویو حمله کرد، گفت: «بر اساس آن‌چه می‌شنوم، می‌گویم پاسخ مثبت است، اما همین حالا در حال بررسی آن هستیم.»
تاکنون هیچ مدرک علنی دربارهٔ ارتباط ایران با این حادثه منتشر نشده و تحقیقات دربارهٔ انگیزهٔ کمک‌خلبان ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78595" target="_blank">📅 16:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po1ZV7t9m86CyObmQXtekijev30_Ge0-CC9rrET5BHwBpA50nnJKZQ3uFvqx-jKWbug5ikzHALJiKysn5DCTwBiVBN5rcmME27SsY0ri9PNe-IlKrcW-KADb3Ya_Bn24Ww0ZoomOORKkyj9BCJxEFsayhlq129-o33sccuWpxprvjt8GluifAAf2USv-cg02fHiUG4Katokz4agPPsAlG7GgORa1RKOmVHqVngEzu2ltzErVJ50yCuTvaYDJdjPIKqj1GMYxYCxc0cKrm6EUAVka1jzby3UQD4CX31yWNRyeJOp72bVesVfJW3sp4hPbhMdAT4Sstd0AhXVGiXh2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه شهروند اهل کرمانشاه، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در شعبه ۲۳ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌اند.
بر اساس اطلاعاتی که به سازمان حقوق بشر هانا رسیده، سیروان شعبانی، ۲۵ ساله، هنرمند و نوازنده و سرپرست یک ارکستر پاپ و سنتی، خسرو محمدی‌نیا و مسعود توشمالانی هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شوند.
هانا گزارش داده است که این سه نفر روز ۱۹ دی ۱۴۰۴، هم‌زمان با اعتراضات در اسلامشهر، از سوی نیروهای امنیتی بازداشت شدند و پس از آن مدتی در سلول انفرادی نگهداری شدند. بر اساس این گزارش، آنها پس از ماه‌ها نگهداری در شرایط انفرادی و آنچه هانا «اخذ اعترافات اجباری» خوانده، به زندان قزلحصار منتقل شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78594" target="_blank">📅 16:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EXe_j940mSfuFQxg1tSTPHJ83vtCXbwuwYNE7Fok1yC3h14VSSs-UapVuJI8Fe7L7MZaNl9ifqIR7UG_5FpETfDwv_8V6ubTivJOg9REFyeDfdoNg_8QuL0h2owjI4MokzoGpxYtVbSbGN5amA7kNxW3uFR0IjZJbfE-jRrd61BDDpihvsLixLU9yIDzcd4cpsOIRLkscOCHEE_kA9iPxFT2f46S1zN8nOJOSlUFsAOGK8Nw-C5XWdOC4pCYaHbv0X6VdXVf3imnoaTp9lhoY2p8jXftfn0SkbxqldarTTmWfR_givmRzt0TheYqh37VedfN8SSNGlIdB4E24DrrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
«عملیات تجارت دریایی بریتانیا» (UKMTO) گزارشی از یک منبع ثالث دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته و در پی آن آتش‌سوزی رخ داده است.
گزارش شده که خدمه در سلامت هستند. میزان خسارت و تأثیرات زیست‌محیطی در زمان انتشار این گزارش مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78593" target="_blank">📅 23:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tlpBiant3_YaqDLINgRh4O6wkKRib2OK-YZGEILgi97Vdx6Wj_i3L_PhTlX8DUxsv-al6EZ6V0CJsMy27E5J-RIFKOYUPClmH3Fcenry9TgYOA35RPmgirCHB9PXtyGznED85K0mN5Ca1xsMBlPv9x4VeCS87KPomisgGVG9uLn9G9lw6NNwJNdiC_hIKMZxzktu-FMrXXx8oNpAUWhcFt9glV_XolNvcP65HNBAlciVctCQgmUaeSHohJb2kOJyIUR_Yws_nfy7XRKu0I82i6XSURPHpamGMM7NsKD9pXN_-spbMSmq8RWUVFxVLP5ep2KunnzJqWrJ9NBcVwj9XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78592" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sYp1tMx3QqMMEW4VPmFS4KrBxk7pJXFo0qmgOnKEsF9JK83Ei6AWuOxMf646kQM4jRlvQDbDpTXGL2rljqhIMwMBSOZK8vUoLhTp0PgWI9jvMHmzVCsSv-GJC3Nk5zFbZpbq5_iZAs004YvKvZWdR8p8lzHmTE_ho4nhyNH6QlcHMLyWniQEMI2RTrDPWYrfr8JVELICL33joMkKX5BKFDeX9KJ3nTsSdL7PG7nHdJFZyF1Rb9OI6NGmOwL3igcOQYPD61QO2q9Aprcvrjmc9ZBDRSkzJRtCuXxmdwYCercJdv_kim98VaNPnDEl54eNBXenL-yS6_8Tx1o00uUdkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهوری آمریکا، در مصاحبه‌ای مفصل با مجله تایم گفت پیشنهاد اخیر جمهوری اسلامی برای پایان دادن به درگیری‌ها و بازگشایی تنگه هرمز را به دلیل «ناکافی» بودن آن رد کرده است، و افزود احتمال تشدید حملات نظامی آمریکا علیه جمهوری اسلامی را منتفی نمی‌داند. این مصاحبه ۶ مهر در کاخ سفید انجام و روز پنجشنبه ۹ مهر منتشر شد.
دونالد ترامپ در پاسخ به این پرسش که چرا درگیری نظامی با جمهوری اسلامی بر خلاف برآورد اولیه او وارد هفتمین ماه شده است، گفت پس از حمله بمب‌افکن‌های بی-۲ به تاسیسات هسته‌ای می‌توانست عملیات را متوقف کند، اما تصمیم گرفت «فراتر» برود تا حکومت ایران نتواند توانایی‌های خود را «به شکلی متفاوت» بازسازی کند.
او گفت: «توانایی هسته‌ای آنها را نابود کرده‌ام. نیروی دریایی‌شان را نابود کرده‌ام؛ ۱۵۹ کشتی در کف دریا هستند. نیروی هوایی‌شان را نابود کرده‌ام. همه هواپیماهایشان از بین رفته‌اند. رادارشان را نابود کرده‌ام.» رئیس جمهوری آمریکا همچنین گفت اقتصاد جمهوری اسلامی از بین رفته و تورم آن حدود ۳۰۰ درصد است.
ترامپ گفت آمریکا عملا کنترل تنگه هرمز را از جمهوری اسلامی گرفته است، و تاکید کرد شب پیش از مصاحبه حجم عبور نفت از این آبراه به بالاترین میزان تاریخی رسیده بود. داده‌های جدید نشان می‌دهد صادرات نفت خلیج فارس در روزهای اخیر به‌ شدت بهبود یافته و به سطوح متوسط سال ۲۰۲۵ بازگشته است.
در بخش دیگری از مصاحبه، خبرنگار تایم به اظهارات اخیر ترامپ درباره احتمال «نابودی ایران» اشاره کرد و پرسید آیا چنین اقدامی واقعا ممکن است. او پاسخ داد: «بله، این کار را خواهم کرد. ممکن است.»
هنگامی که خبرنگار درباره مردم غیرنظامی ایران پرسید، رئیس جمهوری به سرکوب اعتراضات اشاره کرد و گفت حکومت ایران طی ماه‌های اخیر بین ۷۲ هزار تا ۷۵ هزار نفر را کشته است.
ترامپ همچنین گفت از تصمیم خود برای مداخله نکردن مستقیم در جریان اعتراضات دی‌ماه پشیمان نیست، و عملکرد دولتش در قبال جمهوری اسلامی را «باورنکردنی» توصیف کرد.
او گفت ایران کشوری بسیار بزرگ‌تر و دورتر از ونزوئلا است، اما «نتیجه همان خواهد بود» و افزود: «آنها می‌خواهند توافق کنند.»
در پاسخ به پرسشی درباره علت رد پیشنهاد اخیر جمهوری اسلامی برای آتش‌بس، ترامپ گفت رژیم ایران پیشنهاد بازگشایی تنگه هرمز را مطرح کرد، اما شرایط آن «حتی نزدیک به کافی هم نبود.»
رویترز گزارش داده است پیشنهاد ارائه‌شده از طریق میانجی‌های قطری شامل پایان درگیری‌ها و بازگشایی تنگه هرمز در برابر رفع برخی فشارهای اقتصادی آمریکا و دسترسی رژیم ایران به دارایی‌های مسدودشده بود. مذاکرات غیرمستقیم همچنان ادامه دارد.
خبرنگار تایم سپس پرسید آیا دولت آمریکا پس از انتخابات میان‌دوره‌ای حملات به جمهوری اسلامی را افزایش خواهد داد. ترامپ پاسخ داد: «ممکن است.»
او از ارائه جزئیات خودداری کرد، اما گفت آمریکا طی شش ماه گذشته ذخایر تسلیحاتی خود را افزایش داده و شرکت‌های دفاعی با فعالیت شبانه‌روزی در حال گسترش تولید هستند.
رئیس جمهوری آمریکا در پایان مصاحبه هدف اصلی سیاست خود در قبال جمهوری اسلامی را جلوگیری از دستیابی آن به سلاح هسته‌ای دانست و گفت: «موضوع اصلی که همیشه مطرح می‌کنم این است که ایران نمی‌تواند یک قدرت هسته‌ای باشد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78591" target="_blank">📅 17:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5YT3-3i9tX2mG-ApbJ13bVj0tuhTUTkJk8xBC1sNmZ0RbRvp4vpl6k2CtKXVpkxNP_GvjOSoFnVmGkVGjFDWhZ-srn0vKf8GLughDU2NtAInZ9YPR1w4_WBsMhTwUlNM5RmkO5d0oGMN0oZFS1eFgfMMaMXwyYjVcEtPBx_hUlqBPXMtQBXqqYHrv3IzcbVqq9mgSL2bhbxOdsinrR40Ng89suC7HeJb7AWOE0naIeoT85z3RIpk-Zugm0qTR9vxGPnOYTL2vIPdFK4Twm5LQ7MCUlM69whKQkedm_gE7V22l4e8vUAI3BfFxm5wscAqg2F05lthGILEWwDssP9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد ایران روز پنج‌شنبه با افزایشی حدود ۱.۵ درصدی نسبت به روز گذشته به ۲۵۸ هزار و ۹۰۰ تومان اوج گرفت.
دلار آمریکا در مقابل ریال ایران طی یک هفته گذشته بیش از ۱۰ درصد، طی یک ماه گذشته بیش از ۲۰ درصد و از زمان آغاز جنگ حدود ۶۴ درصد جهش داشته است.
در بازه یک‌ساله نیز نرخ برابری دلار در مقابل ریال ایران تقریبا ۱۲۵ درصد رشد داشته است.
قیمت سکه امامی نیز در لحظه تنظیم این گزارش در بعد از ظهر پنج‌شنبه از ۲۶۰ میلیون تومان فراتر رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78590" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XQmjDx67UuE3ri8sdABBAxhD_9UNTNAHFQQz_MkGSl_3cK6Xfj-XY92L-Pk0Od7rugfH-FWU7MaFTUbwjRL8I19rdhrfveSIF6yekCysDH-UWP1LkosO4iy7YkdIRROvxMHGOuopXr1YK60NpGb0noIIjUJVzHGkqkBKkJrt3uTCL_sWY7hIeOsFipnRDRh7UwfvzBALwSv4VD60mNE7682SW9m92mueZxBS9yaaJnc2vkmxW8_fImXCUvzo4t9sj2LZeYcLJicIOBT--9hMj__gdA7_XxNhj40DC2RdI5F2vlyp1ztcAwswM0-3JbjMstLKmPt37tAyrHzubMe8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، در واکنش به اظهارات تازه «احسان حدادی»، رییس فدراسیون دوومیدانی جمهوری اسلامی، او را «بدنام‌ترین ورزشکار تاریخ ایران» خواند و نوشت که ورزشکاران جوان باید او را «عبرت» قرار دهند، نه الگو.
فرزانه فصیحی در متنی که در صفحه اینستاگرام خود منتشر کرد، خطاب به احسان حدادی نوشت: «در جهان موازی تو باید پشت میله‌های زندان می‌بودی و از هیچ حق شهروندی برخوردار نمی‌شدی، ولی چه کنیم که اینجا سرنوشت صدها و هزاران جوان پاک و معصوم رو هم سپردن دستت و حالا فاز نصیحت برداشتی.»
این واکنش پس از آن منتشر شد که احسان حدادی، چهارشنبه ۸مهر۱۴۰۵، در گفت‌وگو با وب‌سایت حکومتی «ورزش سه»، درباره ورزشکاران زن گفته بود: «با زنان دونده جلسه می‌گذارم و به آن‌ها می‌گویم تو می‌توانی مثل خیلی از ورزشکاران زن، مجازی شوی با ۳۰ هزار، ۵۰ هزار، ۳۰۰ هزار فالوئر، یا می‌توانی قهرمان شوی.»
فرزانه فصیحی همچنین با اشاره به «ریحانه مبینی»، «زهرا زارعی» و «فاطمه محیطی‌زاده»، از ورزشکاران زن دوومیدانی ایران، نوشت تصور این‌که آنها بخواهند از آموزش‌های احسان حدادی پیروی کنند، برای او «مثل کابوس» است.
او در ادامه خطاب به رییس فدراسیون دوومیدانی نوشته است: «شریف بودن ربطی به مدال و قهرمانی نداره. تو ثابت کردی با خورجینی از مدال هم می‌شه به قهقرا رفت و منفور یک ملت شد.»
اشاره فرزانه فصیحی به «پشت میله‌های زندان»، به پرونده قضایی احسان حدادی در دهه ۱۳۹۰ بازمی‌گردد. در آن پرونده اتهام تعرض و تجاوز جنسی علیه احسان حدادی مطرح شده بود و دادگاه نیز رای به زندان، تحمل شلاق و جزای نقدی داد. با این حال پرونده با دخالت نهادهای امنیتی مختومه شد.
در سال‌های اخیر برخی از زنان شاخص دوومیدانی ایران نیز کشور را ترک کرده‌اند. «الناز کمپانی»، رکورددار دوی ۶۰ متر با مانع ایران، از مهاجرت خود به آمریکا خبر داد و پیش از او «مریم طوسی»، رکورددار دوی ۲۰۰ متر داخل سالن زنان ایران، به آمریکا مهاجرت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78589" target="_blank">📅 17:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kKgzcAIEMVFaiGwbbvWRoenEyK8b1gvq96kc9-9GmI97wZ5UNIbnndib2lx7_TVy4T3CjKinBiIg4dr8IymF67CaWdj4ia1XkulSU9gBDipHhVofrMZUXMIsW6_1_bTLMV-FizWYOdzKwtv9SDK666-LAaugSzmq7xRp1cq1qnANu4KIDhCOfLi77hXvw3tBHfrqozRFVBvhzrxHCt0XR3eiiERMVyynL6ngDXn6TcBfrXti8eGrJQ479NrtCQRk7emvSsSVchB6BoU6k5jvgPoc4suotD8t7MkBEFNPWOo9k9EScBgwSHKizC2oKPY3lbpy4rAGC5JWQW9rpTueKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان صادقی، بلاگر ۲۰ ساله و از بازداشت‌شدگان [اعتراضات دی ماه] در کاشان، به بیش از ۱۳ سال حبس تعزیری محکوم شده است.
او بابت اتهام «تبلیغ علیه نظام» به هفت ماه و ۱۶ روز حبس و بابت اتهام «انتشار محتوای مجرمانه برخلاف امنیت کشور» به ۱۲ سال و شش ماه و یک روز حبس تعزیری محکوم شده است.
«انتشار محتوای مجرمانه در رسانه‌ها و مطبوعات منتهی به هتک حرمت اشخاص» نیز از دیگر اتهام‌های مطرح‌شده در پرونده اوست.
ایمان صادقی ۱۱ بهمن‌ماه ۱۴۰۴ بازداشت و پس از آن به زندان کاشان منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78588" target="_blank">📅 17:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rVR_jV_M7uRXoh9YZECJ_j2g8wxQsd_UKgJWgUOwU3ukO9NfnhrkdDU90inDG_S2IKK-SsMFtuQ10FCpyVkJCJGYVv5cFhApotIfY2yqrFJlutEv-BD6ZF3Siwtp3fBWxuAyAzYdFZ5g3kavL1is_tamqhhffmn3dnVMtkK9aXaXgEi43YAPfAManKWu9Be1rADMUgtfuO9LgWHyCdTA6QBifIyrFMuYSqjLZaa2-kcnlsI86EjLfAieemkzKO2oCM-UaDxi66KV3GPWozJocCBjVE10joB8LS_9TauSjpLmVQ4zciGtPEmdnoAoWxznZ7WPm24jFP-OO8fKVh2u1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه شب، گزارش نیویورک‌پست از اظهارات اسکات بسنت، وزیر خزانه‌داری آمریکا را منتشر کرد که گفته است اقتصاد جمهوری اسلامی ایران، «ظرف دو هفته» هیچ‌چیزی برای تجارت نخواهد داشت.
محاصره دریایی بنادر ایران مانع آن شده است که جمهوری اسلامی از طریق دریا بتواند نفتی صادر کند. دلار آمریکا نیز در روزهای اخیر با سقوط خیره کننده ریال جمهوری اسلامی، رکوردهای تازه‌ای زده است.
آقای بسنت به فاکس‌نیوز گفت اقتصاد تحت محاصره جمهوری اسلامی ایران به‌زودی و پس از تحویل آخرین محموله‌های نفتی خود، در حدود دو هفته دیگر «چیزی برای مبادله» نخواهد داشت.
به نوشته نیویورک پست، بسنت در مصاحبه با فاکس‌نیوز ارزیابی کرد که جمهوری اسلامی به دلیل فروپاشی اقتصاد خود که با اجرای «عملیات طرد اقتصادی» شتاب گرفته، از روی درماندگی به‌شدت مشتاق توافق است و هشدار داد که مشکلات آن طی دو هفته آینده به شکل چشمگیری وخیم‌تر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78587" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOw5rivaIzOseJ9geHNyKU-pZB5H0QMhOphYlk9W6wYhJPEIcm3SYXunQw-d87kMwOYZvHq8NKL6N7QHgohoFKOXbLbqB1h568oZSqzp72KrZMDHrO_3-D2_Q_tGTdiEt3txVK2AYnkdVk5CLatW5VpmxdNO-UPSK_MeeomFrrqUtABUJCOP_bcY4E9hcSMKOTlCHC99W-pByPUSC6tmQYyEjSRWc-lt7zj6ZZZdQ-0rJ6QcenvN2_y2SjuQIkgIUXO5I1jp1SDQniUrVlOgvwONk6pXYc4vbBlkmC-lNIv3yGjtnjRIp7H3haQ6XMTvOpqgyTekvcUnI3zu_p0m1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آکسیوس به نقل از یک مقام آگاه، مارکو روبیو، وزیر امور خارجه ایالات متحده، روز دوشنبه ششم مهر پس از به بن‌بست رسیدن مذاکرات با جمهوری اسلامی ایران، دستور داد هیات ایرانی حاضر در مجمع عمومی سازمان ملل، از جمله عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، فورا آمریکا را ترک کند.
یکی از مقام‌های آمریکایی به آکسیوس گفت: «روبیو هیات ایرانی را که بیش از حد مهمان مانده بود، بیرون کرد. مجمع عمومی سازمان ملل تمام شده بود و وقت آن بود که بروند.» بر اساس این گزارش، نمایندگی آمریکا در سازمان ملل دوشنبه شب به نمایندگی جمهوری اسلامی ایران اطلاع داد که هیات ایرانی باید فورا نیویورک را ترک کند.
آکسیوس نوشت عراقچی و اعضای هیات چند ساعت بعد راهی فرودگاه شدند و بامداد سه‌شنبه با پروازی از نیویورک به دوحه رفتند. منبع دوم نیز درخواست آمریکا برای خروج هیات را تایید کرد، اما گفت عراقچی از پیش قرار بود دوشنبه‌شب برای بازگشت به تهران حرکت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78586" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/poRSJeQKvd6ucAPtjfstrWt1q3yQGW2RdJfN7XaKVyZfooUlyEl1kUinX4LBw2FjPoezorxq3vgaqW4SRIyHxOzESTq-RPSxr7tz2FheGs5Mwl_QqbOWc_KY-2Zscts0k-zien_uRU-RHf7-g4doj5FVhPBl3Xi41nwkvj1r-lQiqNUSB5MWVkBnBexEJagYdiEebW0dMh_muX9V18oFViJA2pwAJwWHuJ_2M9RSbfG-c0y0hlfKCxZk0urfzKLc_R4m8p5U3gL-wg2T7iAOEO7K4a8U-6pPqlkMrhho6ylHGb6sdTEb8rvdxkqx7Yjfp88VOa1_myfFsQypBjJvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، در پاسخ به سوال خبرنگاری که از او پرسید اگر رهبران جمهوری اسلامی به گفته او «دیوانه» و «غیرمنطقی» هستند، چگونه می‌خواهید با این افراد توافق کنید؟ رئیس‌جمهوری آمریکا پاسخ داد: «شاید آن‌ها را منفجر کنیم. باید تصمیم بگیریم. منفجرشان کنیم، توافق کنیم، وقتش دارد می‌رسد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78585" target="_blank">📅 00:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=G5caF0r1eksz190ZRjnom4s0h2pV7beF7cV3NwUZYLFwLIrnKKTwWHRw58bbpGC9_VBTzPBGUMJ3Ug8fh7Tbr0d-nYko1iVIIGq42mlOIhyvSbGmbKz0NGx7V0q73Qk2a9YC7FeJeBmqu85fgpAX-6JXLEs00ymgwmPslZ6gVhyny2hKCoY7Mc-wAvYhz7M0DrEaIKZl6XHBNKw1RkiYqJ4jL-xGudvV0c6CeuIZdCoBYVvPrIcT9EPTA7POgklNJGT3gdTk4UJQD_XgKZ0Rm_g-mHQeM_uiyQjX-WS-1WWW4KqjGB5XBPdxYd7f9s9YNNUrK2jmX54TwaOljNb7Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=G5caF0r1eksz190ZRjnom4s0h2pV7beF7cV3NwUZYLFwLIrnKKTwWHRw58bbpGC9_VBTzPBGUMJ3Ug8fh7Tbr0d-nYko1iVIIGq42mlOIhyvSbGmbKz0NGx7V0q73Qk2a9YC7FeJeBmqu85fgpAX-6JXLEs00ymgwmPslZ6gVhyny2hKCoY7Mc-wAvYhz7M0DrEaIKZl6XHBNKw1RkiYqJ4jL-xGudvV0c6CeuIZdCoBYVvPrIcT9EPTA7POgklNJGT3gdTk4UJQD_XgKZ0Rm_g-mHQeM_uiyQjX-WS-1WWW4KqjGB5XBPdxYd7f9s9YNNUrK2jmX54TwaOljNb7Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در تازه‌ترین اظهارات خود درباره ایران گفت تحولات جدیدی «بسیار زود» رخ خواهد داد.
ترامپ گفت: «خیلی زود» خواهید دید که اتفاقاتی رخ خواهد داد. او در ادامه گفت ایران «عملا ویران شده» و با تورم بیش از ۳۰۰ درصدی و وضعیت نامناسب اقتصادی روبه‌رو است. رئیس‌جمهوری آمریکا همچنین بار دیگر گفت که در جریان جنگ، نیروی دریایی و نیروی هوایی ایران از بین رفته و تجهیزات پدافند هوایی این کشور نیز نابود شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78584" target="_blank">📅 22:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZEaD4iqW-5w5Z2KvKXDBKiwZfAjRZ_ZrrhR9VB36f8OgBUSYg1PQjtgurzYsbMm2um0Lld607AHVdudblGpTb4xoIU0ZWqPVFOlW2PZMWYEXRxhmaGmI9QxFazIWvIEf70f12K4X1MnPcxxS77-xC7lTwxcUedU9TDBNWenZGUJBV8-Qr8Q4itiP--C-MrWAsUUw4HBTqZXQxBiSt1qNz_98OrfcuT5ie1hMsimwkcm2xyQBYD4EU4rsgwFWq1S5gexLAaSD2z31ULnEvmxAI3G-BsEeIaDqqIfc1irA9ItDrdoNn1ps-SB_Pg0lg28xC2edItTAMYqvLsfbOT9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست‌وزیر بریتانیا، روز چهارشنبه هشتم مهر، اعلام کرد که قرائن و شواهد قوی نشان می‌دهد جمهوری اسلامی ایران در حادثه امنیتی اخیر در نزدیکی پایگاه هوایی «فیرفورد» (RAF Fairford) تحت مدیریت آمریکا نقش داشته است.
پلیس ضدتروریسم بریتانیا روز یکشنبه پنج جوان ۲۳ تا ۲۵ ساله — که همگی اتباع بریتانیا و ساکن لندن هستند — را به اتهام آماده‌سازی برای اقدام تروریستی دستگیر کرد، اما آنان روز بعد با وثیقه آزاد شدند.
پایگاه هوایی فیرفورد در گلوستشر بریتانیا که پیشینه‌ای طولانی در استفاده توسط نیروهای آمریکایی و ناتو دارد، از ماه مارس به عنوان نقطه‌ای برای پشتیبانی لوجستیکی حملات ایالات متحده علیه ایران مورد استفاده قرار گرفته است. بریتانیا مجوز بهره‌برداری از بمب‌افکن‌های آمریکایی مستقر در این پایگاه را برای هدف قرار دادن سایت‌های موشکی ایران — که کشتی‌های عبوری در تنگه هرمز را تهدید می‌کنند — صادر کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78583" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c6ec3cef6.mp4?token=Arz8ISTrBPwsN2ZBhXOPgP91ANb9BNMv3XQ00MoSgiVC0dTB7AH73NYlKEQl5kcBvoxtJRKOdI-aHZyhVz6ldFtcjWHMM54oyDnE9qe7iDMGcZjAYaf4Px5IZR5tJIycIYDlczZxeZZTXntRz8n_-s3sYPpKQjJvz4r4qiYUUE3yeIVJOSYdL2zOXzjlvmo7J-w3rJa6pMEpDeYyqCdr9AqBxn69xbJ6qGX6mfvH2PbytopFQc9r2JejWo2brKqVef2jAE52lyflB-BBvUZUm-qhCthHV04uYBf-HnL-dAU1xRk9nDyBiBPMpj2Jys3Ur_awxSU24lXCouS2VbsfPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c6ec3cef6.mp4?token=Arz8ISTrBPwsN2ZBhXOPgP91ANb9BNMv3XQ00MoSgiVC0dTB7AH73NYlKEQl5kcBvoxtJRKOdI-aHZyhVz6ldFtcjWHMM54oyDnE9qe7iDMGcZjAYaf4Px5IZR5tJIycIYDlczZxeZZTXntRz8n_-s3sYPpKQjJvz4r4qiYUUE3yeIVJOSYdL2zOXzjlvmo7J-w3rJa6pMEpDeYyqCdr9AqBxn69xbJ6qGX6mfvH2PbytopFQc9r2JejWo2brKqVef2jAE52lyflB-BBvUZUm-qhCthHV04uYBf-HnL-dAU1xRk9nDyBiBPMpj2Jys3Ur_awxSU24lXCouS2VbsfPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روزسه‌شنبه هفتم مهر در جریان ضیافت نهاری با حضور چهره‌های برجسته فناوری و مقامات ارشد دولت در کاخ سفید، اعلام کرد که واشنگتن رسماً عبارت Artificial Intelligence (AI) را به Super Intelligence (SI) (فراهوش یا هوش برتر) تغییر خواهد داد.
ترامپ با اشاره به امضای سند رسمی این تغییر نام گفت: «ما همگی هم‌نظر هستیم که این فناوری مصنوعی نیست؛ به همین دلیل امروز سندی را برای تغییر نام رسمی آن به فراهوش امضا می‌کنیم.»
این نشست مهم با حضور رهبران ارشد دنیای فناوری و غول‌های سیلیکون‌ولی از جمله ایلان ماسک، جف بیزوس، ساتیا نادلا (مدیرعامل مایکروسافت)، لیسا سو (مدیرعامل AMD) و مدیران عامل شرکت‌های متا، انویدیا، گوگل، پالانتیر و آنتروپیک برگزار شد. همچنین گرگ براکمن، رئیس OpenAI، به نمایندگی از این شرکت در جلسه حضور داشت.
در سمت دولتی نیز چهره‌هایی چون جی‌دی ونس، معاون رئیس‌جمهور، سوزی وایلز، رئیس دفتر کاخ سفید، اسکات بسنت، وزیر خزانه‌داری و هاوارد لوتنیک، وزیر بازرگانی، ترامپ را همراهی می‌کردند. این تصمیم در ادامه سیاست‌های جدید واشنگتن برای جایگزینی عنوان «فراهوش» در تمامی اسناد و مکاتبات رسمی دولت آمریکا اتخاذ شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78582" target="_blank">📅 20:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ST6B_6jaCpL13cXFTPz12kx_y0r8GU9e5QRvJ7Llcn4wKVSFkzrxgQLijLwtog0NZVbkctlts66m6VxNc2NQew36KVOIztxI0u02PuQaxDY1vuLxjpRiemrgpAH_3UvWgcA02uePI3Jw0Avmi485Eex4tRISgwYZHAKbrGzWoMCNziGbZFKm62RzJaBrM_smrQZXupu2z3y0IlTeH2RbpDNj4Xe0z4Zk-uMNepgS22Md25wcsiJJbtfNds6-7UW0m6cVrINOTrZCvB8Y6UbfErgU_acpnWKQDJ30pWqITjY3coLvHV3wZo4_sACcCSyvVWbhv09c7lHQb-4_Myzpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۶ هزار تومان گذشت و دادستان تهران به ضابطان قضایی دستور داد با «عوامل اخلال در بازار ارز» برخورد کنند.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار ۲۵۶ هزار و ۵۰۰ تومان، یورو ۲۹۰ هزار و ۵۰۰ تومان و پوند بریتانیا ۳۳۹ هزار تومان معامله شد.
دلار صبح امروز ۲۵۵ هزار تومان بود و دیروز ۲۵۳ هزار و ۱۰۰ تومان، یعنی در دو روز سه هزار و ۴۰۰ تومان بالا رفته است.
همزمان دادستان تهران از برخورد با فعالان بازار خبر داد و گفت ضابطان قضایی مأموریت یافته‌اند با بررسی میدانی و رصد فضای مجازی، عوامل اخلال را شناسایی و به دستگاه قضایی معرفی کنند و گزارش اقدام‌هایشان را روزانه بفرستند.
نیروی انتظامی جمهوری اسلامی دوشنبه ۱۱ نفر از فعالان بازار ارز را بازداشت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78581" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v7181DRNojNgaMV-i7tnBHC5525aD899sdaAx6Ajd2BPiOD15o1oHivtQA0I7dNOYmYzgbQBZtSHbDVZOPw7ro3zuG7iwhqYfikVv13JOHD4ybQWfFszBY7kUygR95rY_GMN9Gibjf23unLZEmzygNOdmoCgFlZm1pIZI_jpNTGvLq0yXybGL0XFwlGF5kSNL0aiVrWQZKCpv5-3DBJCO51gc6ZI-nMdMZijhsXzvA2RbYF3rZHMJa7p06GD84OLKSP9EmWsngX2Zkw5giAaiiYNzp-w5_8LLsSo4aXJNrlcBu0-QGzW-TFNwaiM38-QZUWDFMfWapD44QBTXgYsEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=XvhUhU7by9peNigy_h7AX2zcPbDyVh2TzuEMJFxRCs1hAklCzB6EtTHtMtU-EuoKZa39WQCWM6Q_Essfedo6y87qoESqJhpZjru3hirSr4Pae7SW3e6p1FBa-bDVb_1YzEmgWLLIa_uTBRx5011gF5x3Ebr0hGQLMGlSgCjNxTquqDg-Oow0d81atJejerfzfVPO2NZDamh9YEMI_RpqNUIimR9yO6N_XvfhJJgKpC61nB-loR3oVnCqgPJHK4XK1ySte225YuQAYqF3286IZcna-CGJ4jeKPdzeQ6D-2v_6s3hlRP_e_sSsWs5gRcObF_agk7V3qYSudnRZRvTwaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=XvhUhU7by9peNigy_h7AX2zcPbDyVh2TzuEMJFxRCs1hAklCzB6EtTHtMtU-EuoKZa39WQCWM6Q_Essfedo6y87qoESqJhpZjru3hirSr4Pae7SW3e6p1FBa-bDVb_1YzEmgWLLIa_uTBRx5011gF5x3Ebr0hGQLMGlSgCjNxTquqDg-Oow0d81atJejerfzfVPO2NZDamh9YEMI_RpqNUIimR9yO6N_XvfhJJgKpC61nB-loR3oVnCqgPJHK4XK1ySte225YuQAYqF3286IZcna-CGJ4jeKPdzeQ6D-2v_6s3hlRP_e_sSsWs5gRcObF_agk7V3qYSudnRZRvTwaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فرود اضطراری یک هواپیمای خطوط هوایی «فلای دوبی» از مبدأ دوبی به مقصد تل‌آویو در عربستان سعودی، نخست‌وزیر اسرائیل گفت کمک‌خلبان این هواپیما پس از حمله با چاقو به خلبان دیگر، ظاهراً تلاش کرده بود هواپیما را با سرنشینانش سرنگون کند.
بنیامین نتانیاهو، در پیامی ویدیویی که روز چهارشنبه هشتم مهر منتشر شد، گفت: «در جریان پرواز، هنگامی که هواپیما به کشور نزدیک می‌شد، یکی از خلبانان به خلبان دیگر حمله کرد و ظاهراً تلاش کرد هواپیما را با همه سرنشینانش سرنگون کند.»
او مسافران هواپیما را «قهرمان» خواند و گفت آنها با اقدامات خود «از وقوع یک فاجعه بزرگ جلوگیری کردند».
نتانیاهو همچنین گفت عربستان سعودی کمک‌خلبان این پرواز را که به ادعای او به خلبان دیگر حمله کرده و تلاش کرده بود هواپیما را سرنگون کند، بازداشت کرده است.
او افزود: «خلبانی که دست به حمله زده بود بازداشت شده و اکنون از سوی مقام‌های سعودی تحت بازجویی قرار دارد.»
نتانیاهو همچنین دستور آماده‌سازی برای مقابله با تهدیدهای احتمالی بیشتر را صادر کرد.
یسرائیل کاتز، وزیر دفاع اسرائیل، نیز روز چهارشنبه این حادثه را «تلاش برای یک حملۀ تروریستی» خواند.
او در بیانیه‌ای گفت: «حادثه جدی در پرواز فلای‌دبی یک تلاش برای حملۀ تروریستی جهادی بود که تنها به لطف شجاعت چند مسافر اسرائیلی خنثی شد؛ آنها وارد کابین خلبان شدند، تروریست را مهار کردند و با دستان خود کنترل هواپیما را به یک خدمه پروازی دیگر که در آنجا حضور داشت، بازگرداندند.»
رسانه‌های اسرائیلی روز چهارشنبه از احتمال ربوده شدن این هواپیما خبر دادند اما بعداً گزارش دادند که «بروز درگیری فیزیکی بین خلبانان» در هواپیما باعث تغییر مسیر و فرود اضطراری آن شد.
بر اساس این گزارش‌ها، این هواپیما از نوع بوئینگ ۷۳۷-مکس کد اضطراری مربوط به ربوده شدن را ارسال کرده و پس از آن ارتباطش با اسرائیل قطع شده بود.
به دنبال این اتفاق جنگنده‌های اسرائیلی به پرواز درآمدند و فعالیت فرودگاه بن‌گوریون نیز متوقف شد.
ویدیوهای منتشرشده در شبکه‌های اجتماعی که رویترز محل ضبط آنها را پرواز FZ1073 تأیید کرده، مسافران را در حال رسیدگی به دو مرد مجروح در کف هواپیما نشان می‌دهد که دست‌کم یکی از آنها لباس خلبانی بر تن دارد.
در یکی از ویدیوها، یک مسافر اسرائیلی درخواست کمک می‌کند و می‌گوید مسافران «تروریست‌ها را مهار کرده‌اند». با این حال، مقام‌های فرودگاه تبوک و این مسافر هویت فرد یا افراد مهاجم را مشخص نکرده‌اند و جزئیات دقیق چگونگی درگیری هنوز روشن نیست.
بر اساس اطلاعات وب‌سایت فلایت‌رادار۲۴، این پرواز ابتدا یک پیام اضطراری عمومی ارسال کرد و سپس پیام اضطراری دیگری فرستاد که احتمال «مداخله غیرقانونی» را نشان می‌داد. هواپیما پیش از نخستین هشدار اضطراری، در کمتر از ۳۰ ثانیه نزدیک به ۱۴ هزار پا کاهش ارتفاع داشته است.
به گزارش این وب‌سایت، هواپیمای بوئینگ ۷۳۷ که رسانه‌های اسرائیلی اعلام کردند حدود ۱۵۰ مسافر اسرائیلی را در خود جای داده بود، بار دیگر پیام اضطراری اولیه را مخابره کرد و سپس در فرودگاه تبوک در شمال‌غرب عربستان سعودی به زمین نشست.
از سوی دیگر، شرکت هواپیمایی فلای‌دبی، مستقر در امارات متحده عربی، اعلام کرد علت درگیری‌ای که «در کابین خلبان پرواز FZ1073» رخ داده، همچنان مشخص نیست و موضوع تحت بررسی رسمی قرار دارد.
سخنگوی فلای‌دبی در بیانیه‌ای گفت: «در این مرحله، دلایل و انگیزه‌های اصلی این رویداد مشخص نیست و همچنان در چارچوب یک تحقیقات رسمی در حال بررسی است. از همه طرف‌ها می‌خواهیم تا زمانی که مقام‌های مسئول در حال جمع‌آوری اطلاعات و روشن کردن ابعاد ماجرا هستند، از گمانه‌زنی زودهنگام خودداری کنند.»
خبرگزاری رویترز به نقل از مقام‌های اسرائیلی اعلام کرد کمک‌خلبانی که این حادثه را رقم زده است، شهروند عمانی است. دولت عمان هنوز درباره این موضوع اظهارنظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78575" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kN9M2j975BYlfl7aKHqfAeMFWSqJG1VnkvSIsCOGMT8nyZ4f_jg1pXpmOMLPBu9qxDlsbMh9_npbL_tY1bAIC83N_yDumGpMHdFtES-3pHunGSLfcnr8I7pq1qykRW_MZQZgfgD3mz4FZ69K-LATsFREIinpTNjtrxYUqa4sO5Ect-rjC54kWlaY7BI3wwG7Ndjd84og-jDa2H7Y_v5CKeTEuDA1x4Z-fJFDZB9vsmRpMNffI7-Z6QVTTbh6iSB3NYX5G4UCuFWgnbq96qV321UgOLcqs2Gp41KTGXz6pYvYLVwkafM7P4OkhrXeUbLZGssD_Ochx4j1lRGtcJmdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npYXRMTUWTxcfqJUhY6_x8BydTmHFsEuLh3ShZgOMlzG2P523cVNJSc3Rf3FNMCiNFuX5tne3WaGMqTDF73KOoqDQbaUqKcmnFMeZR2bIM1PFErLiAZcKzqHo-0N6fqjr-7aqeKkK8L77ggrMCiSw4Lasnq_HIgLDzCuVvQ3OFZdD9WY15DIUyj8Rml4tk4Qo7vXri5_b21jdmwNRnZf6SW-2TYdsc86TqjK4PG_2Y_m4dSJoP4F0QdzMjIn8TPyDmIQuqZTs6aFlweEFd0yfmy8fI-vV-Qnt7G-lDBSN7WfmF1sQKYTEhBLavHIJioA8mbexuiuLh4N4cu4r770-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMFnhiO2hVgF3ctAv3BLzdneRlVEiTVSDioFK5CtsirO8BBc6taPb13N17lCpf4BrpieUXNeLaWeTe2EEx4LGtw_QpA1Qi33fgIS_OD9yhBHbBLXcro4YG8LQw1of7xp6yTnUat5kJWNge-nvYUlGX_GgzOf5TKTEvqShUGJYnZgQu3wPHX0hpzifo3xb_E-HXuycsibRQUSoQPGzhVXIX99hIAK_Pe7gffLfyO__Xd-00e5FFtfFAXFyHpPVm2qWg5XJ3qj119wMoTOVQK6__myXeTSNV6u1XIYKBAml8d59DR1yP8Y1rrP1OuHPFb0bm-GyQLJPrAQTYtRBpXilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urHULVhXr-d0PnKoB6kEX7p3BymgOkNxP6igcOFxw6LdUI7UYwef-1XuFyY-fWikpo99THZhj2SrbF4su8lpLLudQbGK0UezM-FTALV9t9-IVR_qXTwTIEkjXg8ZzM9VKB8L3pqTbcd6e7KBxWjpgNfSeCUjx8l8Unj7uSUqvaW_YG2JEJbaE5wZzeD4I6-soNlTczbiZMM5YgAT4RLecgKuoN3rSYbtSAuNfRhSpKhtol-Yb7Oue0kfJiTFho5lmxmXTcZJq0bw149-KrIpDzXC1PGNywuPuzpussXuh61SwV7BNBRsMpq5sMROsXTe579Q6rvisB0vio-pfifdog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
«برای کمک به پدر مجروحش رفت که  هدف گلوله قرار گرفت»
🔸
هفت روز طول کشید تا خانواده محمد عباس‌زاده بتوانند پیکر تنها فرزندشان را تحویل بگیرند. در این مدت، بارها به مراجع قضایی و نظامی مراجعه کردند، اما پاسخ روشنی دریافت نکردند و تنها به آنها گفته می‌شد منتظر پیامک بمانند.
🔸
فشارها پس از آن نیز ادامه یافت. برخی از بستگان احضار شدند، از اعضای خانواده تعهد کتبی گرفته شد و مقام‌های امنیتی برای نحوه برگزاری مراسم و حتی روایت چگونگی کشته‌شدن محمد برای آنها محدودیت تعیین کردند.
🔸
خانواده با وجود این فشارها، پیکر محمد را در زادگاهش اهواز به خاک سپرد؛ در حالی که پدر مجروحش هنوز در بیمارستان بستری بود و نتوانست در مراسم خاکسپاری تنها فرزندش حضور داشته باشد.
🔸
سرگذشت کامل محمد عباس‌زاده را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-9241/mohammad-abbaszadeh
@IranRights</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78571" target="_blank">📅 19:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGtAZWPMiV4X9QsRSqb-WUv-Zia2Sy73SaCa9Bt0WRT4lMNB3f1x8RXKVP90hFotNuuupHfPEcrrHos3D5BF_WA8xXzMEb5tTuMZvulFbGd8q0dM01JlM94gqK2qbh41JwsXz-gDfegOcf0wfbqmN_fs-yM9fitY2lOTbrkP0ivCckrZqPjB0t6Glyx4bZW69tffzYRtrXk9tPOSTOIabjkcmEtgDM6xf0LjGnti5cobSESQzu5fixmENGyIJnzyTqt4Pe8fGD9a_T1q37dYKaq2e89AqzHpWQFAfZ1-V9wIjvlPkDUAI2s0fM3OBlJPGZ-h5y_B9Ppm0kN2Bs2Gug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد دو نفر را که در اعتراض‌های دی‌ماه سال گذشته در مشهد بازداشت شده بودند، بامداد چهارشنبه اعدام کرده است.
بر پایه اعلام مرکز رسانه قوه قضائیه، علی همتی سیستانیان و مجید نیک‌اندیش پس از تأیید حکم در دیوان عالی کشور اعدام شدند. قوه قضائیه آنان را به دست داشتن در کشته شدن چهار نفر از نیروهای امنیتی در منطقه‌ای در مشهد متهم کرده بود.
در ادعای قوه قضائیه آمده است دو متهم در بازجویی و در دادگاه به حمله به یک فروشگاه زنجیره‌ای، آتش زدن آن با کوکتل مولوتف، آتش زدن یک بانک و تخریب اموال عمومی اعتراف کرده‌اند.
هیچ اطلاعاتی درباره روند دادرسی، دسترسی متهمان به وکیل انتخابی یا شرایط اخذ اعترافات منتشر نشده است. اعترافات تلویزیونی در پرونده‌های امنیتی جمهوری اسلامی بارها از سوی نهادهای حقوق بشری به اخذ تحت فشار متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/78570" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Idvd35g7nJLtB9FMg_ACuHGlTRHMov8xNifv9cM_sBaf6dLsE6XMFgtnImLySPK7GN3Z6lPqL-eaqDlE7sVreQF5mLq3UlTcRLZLGO16SkPQgf-mFpck7z2fbfAjVW65TcuXeV80pz4dTzRa2zBxZNltxHZKumSJxEBt0EhsjBRGLjZFJbL_auxFbYZhtHIULlM7Z2kZ6OaHEbFWdoC6qkqoIC1MQX30I8ZxRx-KPfHEaeDTvIJKhRcvmHDS9HkSsVTyl4V1Lj2r_GUPJSkku7dRZjcNFA-TbjMCUeKDdO-QiRBSzFC4PmuBTOumwOV_1WliXXM-qJVpBFdIKOFi3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v3pMSRItGj0qyDIMqoIlgOFl063DdSSWkkjHHdMexQxD7Pny1bUQgBcT_BuBQDG3nSytUxMvViAakea_FAjQ5TiTFDDdeq9Ry9PVrni6ezaQSqxdQz959Yn3DVzzBXzaaq0hv2mMcnBgbjANVyhVnbSwDnbeVwuGqs_ckIFsr4uItuYsEroP5DJZ0lTi1qVL5Eq0iK8OaNh6AaFjklJ5vwrQ4beFWi3wwMKknWvejhCZ2eJHGcz1f0CuKJ355idlaGOHD4c3HEtRzJ_xfL91A9d7KdC7q7cx37YC6Glhr_onmQ7mxyso2Bf4hF-m4LA9HzEpw7mpD0Ne9W73xxBV2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن رضایی، دبیر "شورای عالی امنیت ملی"، در دیدار با شاهین مصطفی‌اف، معاون نخست‌وزیر جمهوری آذربایجان، با تکرار مواضع دیگر مقام‌های جمهوری اسلامی گفت: «ترامپ در باتلاقی گرفتار شده که نه می‌تواند مذاکره کند و نه می‌تواند بجنگد.»
او افزود: «شروط ایران به آمریکا اعلام شده، اما ترامپ قادر به تصمیم‌گیری نیست و آمریکا از سر استیصال در جنگ نظامی به محاصره هوایی روی آورده است.»
رضایی ادامه داد: «آمریکا آینده‌ای در منطقه ندارد و ایران با قدرت در مقابل آن ایستاده است.»
@
VahidOOnLine
ساعاتی پیش از این عباس عراقچی در آستانه بازگشت از نیویورک به تهران گفته بود که ماموریتش در این سفر این بود که شروط ایران از جمله درباره بازگشایی تنگه هرمز را به اطلاع ایالات متحده برساند.
وزیر خارجه در جمهوری اسلامی گفته بود که «ایران در این خصوص طرح دارد، شروطش، کاملا عادلانه و منطقی است و اگر آمریکایی‌ها ادعا دارند که دنبال توافق هستند یا دنبال یک راه حل مسالمت‌آمیز هستند، ما این راه حل را معرفی کردیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78568" target="_blank">📅 21:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f601498008.mp4?token=gahYiZoE5nimeo-ZJvopWzJ_a9B7Wc1nFcuk-a8hZj4kj35fsMH5zC-UlzRWUion_aTfyJ1aQeKoCelxvRqv1adwVO3iAkCyWNArsUCccm5wr_dAdzMRs0NRtGVmWjXp_y0MXHfUgLF0Aa4YsNEKncVDf1XAkZ1rYs6KTsO969Rh0Hl_Y8zvQkcG0RP3pj_SMQDVWMyQ115TJ_wK5l-E_c8lTufDQ_kpH-FEeM26VbJqUIswpeWDPWRj8ziVLh8T16cuj1rS4I_GlbHBjYQkaeK-h6YX93HUdwCNlf4111HewEkC2LNKp54mRYRWrlrBqxHeKZdOXhTWANKJNUf_wg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f601498008.mp4?token=gahYiZoE5nimeo-ZJvopWzJ_a9B7Wc1nFcuk-a8hZj4kj35fsMH5zC-UlzRWUion_aTfyJ1aQeKoCelxvRqv1adwVO3iAkCyWNArsUCccm5wr_dAdzMRs0NRtGVmWjXp_y0MXHfUgLF0Aa4YsNEKncVDf1XAkZ1rYs6KTsO969Rh0Hl_Y8zvQkcG0RP3pj_SMQDVWMyQ115TJ_wK5l-E_c8lTufDQ_kpH-FEeM26VbJqUIswpeWDPWRj8ziVLh8T16cuj1rS4I_GlbHBjYQkaeK-h6YX93HUdwCNlf4111HewEkC2LNKp54mRYRWrlrBqxHeKZdOXhTWANKJNUf_wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
و ایران سلاح هسته‌ای نخواهد داشت. آنها به‌شدت در حال شکست خوردن هستند؛ خیلی بد، خیلی بد. این وضعیت خیلی زود تمام خواهد شد؛ خیلی، خیلی زود. آنها سلاح هسته‌ای نخواهند داشت و قیمت نفت هم به‌شدت پایین خواهد آمد، درست مثل قبل.
من مجبور شدم آن سفر کوتاه را به جمهوری اسلامی ایران انجام بدهم؛ سفر بسیار خوبی بود.
فکر می‌کنم در سال‌های آینده درباره این موضوع کتاب خواهند نوشت و تاریخ کشورمان را خواهند نوشت و خواهند گفت که این یکی از مهم‌ترین کارهایی بود که انجام دادیم. در واقع، این یکی از مهم‌ترین کارهایی است که در دوره دولت من انجام داده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78567" target="_blank">📅 19:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78566">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MTzoldJRZi1qP7oRviQqNqkKf8se36FG9rUEwbG9TzD6Vv6x0R-F_45IoGteDm1bBYp9GJjTx-rTZsSQYbhGyGfEpP-P-iA-Ov_lY4Ed1hutSqBhmTmqhVcTPoP5utg2hruy83AfNJUzQiJW1PTCyyRZDMQNcY8dsqWaovB8lFQH9EbkSc28ge3WR2ZZtxC9GWIb0Ke87sW9vQp1lm7Sux4xJl6tSEGU5z8EFYe8V8k0T3u56al8OXKAjBWYXp81FVGQwP3-V0XmA8Ntusw5J4ICIv83NCY8iE5aNUzWlqJJae5NFAF7Qzig1rG8K9Pxwkv7mMp_tQ7c5bhDQ8xHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران با نقض تفاهم‌نامه اسلام‌آباد مرتکب اشتباه شد
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در مصاحبه با وینسنت کُگلیانیز، پادکست‌ساز و روزنامه‌نگار محافظه‌کار آمریکایی، مقام‌های جمهوری اسلامی را مسئول فروپاشی تفاهم‌نامه اسلام‌آباد معرفی کرد و گفت آن‌ها با هدف قرار دادن کشتی‌های تجاری در آب‌های منطقه مرتکب اشتباه شدند.
ونس افزود: «فکر می‌کنم ایرانی‌ها متوجه شده‌اند که اشتباه کردند. آن‌ها با ما توافقی امضا کردند، آتش‌بس برقرار شد، قیمت انرژی کاهش یافت و این امکان وجود داشت که اگر ایرانی‌ها به تعهدات خود عمل می‌کردند، از بهبود روابط با آمریکا منافع زیادی به دست آورند.»
او همچنین به ابهام‌ها درباره وضعیت مجتبی خامنه‌ای، رهبر جمهوری اسلامی، اشاره کرد و گفت واشینگتن با قطعیت نمی‌داند که او زنده است یا نه، اما شواهد موجود نشان می‌دهد که همچنان در قید حیات است.
ونس ادامه داد: «ما فکر می‌کنیم او زنده است. البته با قطعیت نمی‌دانیم. من هرگز او را ندیده‌ام. اخیرا هم تصویری از او در مقابل دوربین ندیده‌ام.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78566" target="_blank">📅 19:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cu58FktKBM9eJVuOGN7GTuMpV1iV-YlOxEXWCjQCxE6hZ5d7idUKgv8f_OSrT_Qsmvneyv74AJqMojytedMBxF7fysA-8ySYLKhsEe3KeSq1xkxRlXW8JmC77nVdq3sMcSya_pbSgac3iR402iTVo-tTKRXcDebnGkAKW-8_ATm-9oKehTKa6wkt9aF_1unpPoUeXQ81wr6g525JkW_4B5q8d4DuebURE-G9-LnKPdefmyhAjdeSNt3OLz8_jLojJXf-LtFas5wfObIoZeXC_L1uKtFwz4JdaQpR2qkpgJHLobFbpO9qeg_DfGfSOCZo9AisiC6MQxKOAPocOYULCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۳ هزار تومان گذشت و رکورد تازه‌ای ثبت کرد.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار در ساعت ۱۴ و ۳۰ دقیقه به وقت تهران ۲۵۳ هزار و ۱۰۰ تومان، پوند بریتانیا ۳۳۵ هزار تومان و یورو ۲۸۷ هزار و ۵۰۰ تومان معامله شد. سکه تمام امامی ۲۴۹ میلیون و ۵۰۰ هزار تومان، نیم‌سکه ۱۲۸ میلیون تومان و ربع‌سکه ۶۸ میلیون و ۵۰۰ هزار تومان قیمت خورد.
دلار دیروز ۲۴۴ هزار تومان بود، یعنی در یک روز بیش از ۹ هزار تومان گران شده است. نرخ ارز سه‌شنبه گذشته حدود ۲۳۳ هزار تومان بود و در یک هفته ۲۰ هزار تومان بالا رفته است.
دلار در ششم مهر سال گذشته ۱۱۱ هزار تومان بود. بهای ارز آمریکا در یک سال ۱۲۸ درصد بالا رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78565" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srZ32628SVBqJpsIBmo9Hu6IKDfFtsjD72qg8G0-nA_QFfwd6Psfc5wJx5_mPeCOEidsuHjQ7UJycw81faY8oRBJuokyduQ_oz_kSHaU5HfykLlMDRiJSxQ-5-wMUfwMWR06f6rNjrsczW737BMowk8AjZbt66yoExuQFT33BZh22ZtzzGCy47PFGsSnXOdW_QoYnoQC0bTuT7_5E0UNT9VWbCrYNtS_io0gQYp-MMEjNmXYbI0Eg68oXiBBuZx3-6z5ySDyLZsAN_cEpl07y0_HuzkUdadQp3agLAT3HeeTaIoJo77lYwOv2sRZEuRBiEeJABuJDU90uxvbK59pIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم از توقیف یک فروند هواپیمای مسافربری شرکت هواپیمایی کاسپین ایران در ترکیه خبر داد و دلیل آن بدهی سه میلیون دلاری عنوان شد.
بر اساس این گزارش هواپیمای توقیف شده بوئینگ ۵۰۰-۷۳۷ بوده است.
این هواپیما زمانی که برای پرواز از استانبول به تهران آماده می‌شد با حکم قضائی متوقف شد و مسافران مجبور شدند پیاده شوند.
شرکت خدمات هوانوردی «تمسیل گزتیم» می‌گوید کاسپین حدود سه میلیون یورو به این شرکت بدهکار است.
بر اساس این گزارش، این شرکت حکم توقیف را از دادگاه گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78564" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MBf6FD_oBAIm0aAbWoPrFZq9kC1OQiXy3xWpZ2UPuGuooljf3RQzj7Cn_Z1n_bKm1nOYk7T0EA3e1AB0BBqJuRFQosdHy3suEgrwn8PNa-kjB2-htU1GWUsWXUZa1gBudEI4uLyYK2HY7AP4trbHR3K67kcg1D4ylwLYhOVgX69iQfW__PUBNyFRXaY3JTbholuf0bFI3cjDb9XLa-WIudp6slm3sIG4ZdtVbf6rxYzYP3LqmRsG2Xvg6V2RgHrANXxVkqobcY3Yok_GqFuk-bb_Go4jJus72zj8roGgsRkdvOo4yCBgybyTqulbSPRSbefSx0Hfz9vvjJzbqBZIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H8dJk2PHBMKwocKWOAQJjEX68F_Og8a1CY-8ILf08o-64JdJ3h_MX1GiQGtadEbt3FGaOMEQuRoUmrewIzaR89B7-_tf7-KW55MT8RN_gszPK5Lbn-6kQhScEAq3iGcmQJGMnzfiqee7nEOfaCsTR0YQ9cDH2_r6uXTgrRNVgK29CzL8lgDBiO3EEmpRVdW3AbxcJrDHbAth58Y-1-NjytaXU8rJMkxbCeCuT4hQ58uMBur_eZiIlW9fNmjegyHNOiBmWAlwh5Kw6N5SPge2joZpt3Hun30OV2mXqBGaJYjw62uk8bZgPKGXFDRwzOTfbZQmElR94eJg4XcrlRhzdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی روز سه‌شنبه ۷ مهر متن نامه‌ای خطاب به مردم آمریکا، دانشمندان، دانشجویان و اصحاب رسانه این کشور منتشر کرد.
در بخشی از این نامه که به زبان انگلیسی نوشته شده، آمده است: «حساب خودتان را از اشغالگران فلسطین که خواه‌ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید! ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.»
سپاه که در دوره اول ریاست جمهوری ترامپ در فهرست سازمان‌های تروریستی آمریکا قرار گرفت، در این نامه از آمریکایی‌ها خواسته است «در برابر سیاست‌های دولت خود موضع بگیرند» و «امور خود را به جای اراذل به اندیشمندان بسپارند.»
@
VahidOOnLine
حسین محبی، سخنگوی سپاه پاسداران، در نشستی خبری با خبرنگاران خارجی درباره نامه سپاه پاسداران به مردم آمریکا گفت در این نامه درباره «میزان محبوبیت» سپاه پاسداران در ایران و خدماتی که به گفته او به مردم ایران و منطقه ارائه کرده، توضیح داده شده است.
محبی گفت: در نامه خود حقایق ژئوپولیتیکی را برای مردم آمریکا روشن کردیم.» او افزود: «از مردم آمریکا خواسته‌ایم که نامه ما را حداقل یک بار مطالعه کنند.
سخنگوی سپاه پاسداران گفت: هیات حاکمه آمریکا به مردم خودشان دروغ‌های بسیاری می‌گویند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78562" target="_blank">📅 17:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UyhA8YymH8s8-pAQMgxAP9nSnkt142LSNcZQPSojKDeCGQ625Z2gwCTw6J3aqHifiXflrfkrlvr9NLIZU39yfd25WBsRgS2ZhuLPyNvow3GtJpkg2fnCR_jai96UhJE68WP7ZZWUO37MGDQBMGpRsQMTGuHwe1xtVBRmMtbl7F9Du9OtHLLUC4VjDpofyaj8SBAR9nKLL4Kcwgm4YdDQsO67VT3byb0ySON-Fsq_IrUokbkmQYmSSGI0-BdvAvnjMuI1xysQRlyr_jYsGuEXm5-oPtRlWtTIZH1GbMVyiPm9H3lVXrEKP5nYonylYQbLDaInYyLYUYBeYTfpLLxOXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KkRaPW5RtpDQ1DGj9CS-s9cFZVWpupOWwOP_ZF_Ca5whd4gZ69c8fbv2-t8_bfQmPWNoIs4u29eo9xq0kKaweBXm5u65Pi75e8X2SIswvcoAviKX9DTqLuxOObIBdtqZQFyjzlZV1VfxB9aocYxsl8JHgOJaO6V8M34_6IftSeEPOoCRUaIzgXQ6rcpccFL9BI7qqgRgN9KZJQ40LnE_fOFBUuJASLTZGj6jQARSj01YhDyf-dcYhIL0ieE_BlGI6fY1CrEMNGaR37-lQNRHStLdSOfhrpu1XNbx_cvPGAIwmpMAj2lPueerMnbRFcVKzUMN2qSWf6Rlx7ziaNuRPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سه‌شنبه هفتم مهر در جلسه علنی وبیناری مجلس، آمریکا و کشورهای منطقه را به حمله به زیرساخت‌ها و نفتکش‌ها تهدید کرد.
این در حالی است که روز سه‌شنبه جمهوری اسلامی در انتظار پاسخ رسمی آمریکا به پیشنهادات تهران است که دونالد ترامپ قبلاً گفته آنها را رد کرده است.
قالیباف گفت: «در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت و اگر امنیت ما تامین نشود، هیچ زیرساختی ایمن نخواهد بود.»
رئیس مجلس شورای اسلامی در عین حال مواضع دونالد ترامپ علیه جمهوری اسلامی در جریان مجمع عمومی سازمان ملل را «سبک‌سرانه» خواند و به او گفت: «بچرخ تا بچرخیم.»
روزنامه خراسان، نزدیک به محمدباقر قالیباف، هم نوشت: «اگر مذاکرات به دلیل اختلافات هسته‌ای به نتیجه نرسد، جمهوری اسلامی فرصت استفاده از نقشه دومش را خواهد داشت تا به انجام حملات پیش‌دستانه روی بیاورد و یک دوره جنگ پرفشار را قبل از پایان انتخابات میاندوره‌ای به ترامپ تحمیل کند.»
شماری از نمایندگان مجلس شورای اسلامی نیز دیگر کشورهای منطقه را به حملات جمهوری اسلامی تهدید کرده‌اند.
از جمله علیرضا سلیمی، عضو هیئت‌ رئیسه مجلس، در گفت‌وگو با خبرگزاری خانه ملت گفت: «باید پذیرفت که امنیت در منطقه یا برای همه خواهد بود یا برای هیچ‌کس».
او افزود که جمهوری اسلامی در برابر هرگونه اقدام تخریبی در منطقه «تماشاچی نخواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78560" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=TJQUC3vQX2qdxnu5a3UY9MhGylyIOSO4sE6cqmGFIc0u5h6t2Rf_jYH7wqMDxKPYwSyDZA0AZwbBoQvWGqj57Zivs0mx1NHE3K03VtFJqJi9eri6UOiB_2uWG5SaxtV8n7EP_kphZH3GCoLz0jDoTLzczu3-tWCqf_0DLV4YOAu-sUHUT-k64KG3K5_h2a5U49WfZ71isiyiyhWkft7VMGZOSywd4RGGHcRGRxEs93Ro7jUjnyFmWcHmtFG6i-97mxm34Nq1HxyNTXI0c5Bz5vny8tcUwW_a1xYf_R8_fRqvn2UGdUIto9e3BA1jUNPFXby7lbFctjxXFn9XFMTbuYMKXaibfSn5lBTdZvfXeBLgvPdncYpuRY6s19rw_McAEQ7nxEblKUJzD19YiwIPDHfIhzXzY_wHIAOokXl4FGLkbO2gwql49mtuxNKpx3fi71x5zDM8p00s4naoxcQtEAcqJ8lBK5ilah9vMbdaPziN5YuegRK9kIdsFsxB5S4St7_o6QVIRkOeqwqvSlWMPH0Bb1UEwsSZ1iJ-Pt9zvP00RRQx6iLbWFe_0BDNh6ktehLUQr1m7N6QcK7HK6wGfn0QFOQ_hRrpJi_vIiOFvb3rnYw11Zo55r5cMFt5hRU_YLwRiubYVZbtfglmJur6GySXKkcwM24fFivkE-RBB48" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=TJQUC3vQX2qdxnu5a3UY9MhGylyIOSO4sE6cqmGFIc0u5h6t2Rf_jYH7wqMDxKPYwSyDZA0AZwbBoQvWGqj57Zivs0mx1NHE3K03VtFJqJi9eri6UOiB_2uWG5SaxtV8n7EP_kphZH3GCoLz0jDoTLzczu3-tWCqf_0DLV4YOAu-sUHUT-k64KG3K5_h2a5U49WfZ71isiyiyhWkft7VMGZOSywd4RGGHcRGRxEs93Ro7jUjnyFmWcHmtFG6i-97mxm34Nq1HxyNTXI0c5Bz5vny8tcUwW_a1xYf_R8_fRqvn2UGdUIto9e3BA1jUNPFXby7lbFctjxXFn9XFMTbuYMKXaibfSn5lBTdZvfXeBLgvPdncYpuRY6s19rw_McAEQ7nxEblKUJzD19YiwIPDHfIhzXzY_wHIAOokXl4FGLkbO2gwql49mtuxNKpx3fi71x5zDM8p00s4naoxcQtEAcqJ8lBK5ilah9vMbdaPziN5YuegRK9kIdsFsxB5S4St7_o6QVIRkOeqwqvSlWMPH0Bb1UEwsSZ1iJ-Pt9zvP00RRQx6iLbWFe_0BDNh6ktehLUQr1m7N6QcK7HK6wGfn0QFOQ_hRrpJi_vIiOFvb3rnYw11Zo55r5cMFt5hRU_YLwRiubYVZbtfglmJur6GySXKkcwM24fFivkE-RBB48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"#سپهر_بابا کجایی؟"
⚠️
۱۲ دقیقه ویدیوی دلخراش از مرکز پزشکی قانونی کهریزک تهران پدر «سپهر شکری» به دنبال پیکر پسرش Vahid نسخه ۴۰۰ مگابایتی: twimg  آپدیت دو روز بعد: #سپهر_شکری در پی گزارش دروغ صدا و سیما درباره این ویدیو و انتساب این ویدیو به خانواده داغداری…</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78559" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kvr-dUFTY3q2x7x6KJVJ6sIqaKrVgqE3NdprZfFBtcIY9FGS35m2RQWS-2wINbSuuZFIOnY_kjGETC2srf0n8B8QFX_5kKUDx660mzPtcTfMA1zs_QU43_seNlt5QJz7ZHdDUOcfLwB3U_sCgmzu-7XsuGKiTHtDHQfGxiUsYbM6Ac0cjOK9aQfwGEfs9oyVWCGOdv4RUcDhJAdnzHDwiIc1d3QxdxEYkjhqIzVtL2d68LdQpC4MTfaJxHoJssMmUkdxhqIVNbmQ9QewWT1GNqTxAaxelccbZobq7y0fBhKRqQWAYeWzfeEayuxj6Zp5tvab5O1i5hnRivyYwzvIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jYGM4lb-qTnq9wV0Jymz47EV4p3_lkj_Cu0s9ghkgb0cgOrH-UA5CSmzoECuPQFHjq8QJV4AcYn4l-VtZMBQdPdtHmzTgNQNwu_Gvt7mststMIV_jFd5RBx7BUKOXrtnYx3_YehiOJETaDl0g7CFXG1qlBnQvgAkf0-Z-qU1_-nrXqOo9KgBdwhguK5E8FZcAAfvT5HLaCZitqEWhojsxcMy2GCtBr2cE7LXoeAtx9iRaCXpo4GtSZQu4a4E7Irb70CkJ-kNnVA_ETByV8uKQk6zrYnqTTbABhisWf50ekb0FlEk98WkgFkI9QnFADSLoHPJon1MqkOj1GhLc7pnrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، روز سه‌شنبه هفتم مهر در گفتگو با شبکه فاکس‌نیوز گفت رژیم ایران پولی را که به دستش می‌رسد خرج مردم نمی‌کند، بلکه آن را صرف ساخت تسلیحات و صدور انقلاب می‌کند.
او با اشاره به عملکرد تهران طی سه دهه گذشته افزود: «مسئله صرفا تحمیل هزینه‌های اقتصادی بر این رژیم نیست. پای هر دلاری که ایران در اختیار دارد در میان است. آنچه آن‌ها در ۳۰ سال گذشته انجام داده‌اند این است که هر زمان پولی به دستشان رسیده، چه در چارچوب رفع تحریم‌ها در دوره اوباما و چه از مسیر فروش نفت و گاز، آن را برای ساخت بیمارستان، جاده یا بهبود زندگی مردم ایران خرج نکرده‌اند.»
روبیو در ادامه گفت: «آن‌ها این پول را تنها برای دو هدف استفاده می‌کنند: ساخت تسلیحات برای خودشان و صدور انقلاب. آن‌ها این منابع مالی را برای تامین مالی حزب‌الله، حماس و شبه‌نظامیان شیعه در عراق به کار می‌گیرند. آن‌ها این پول را برای حمایت مالی از تروریسم و طرح‌های ترور در سراسر جهان خرج می‌کنند و بنابراین هر پنی که به دستشان می‌رسد، پولی است که برای مقاصد این فعالیت‌های مخرب استفاده می‌شود.»
@
VahidOOnLine
مارکو روبیو، در گفتگو با شبکه «فاکس نیوز» با تاکید بر اینکه نباید ایران را با حکومت فعلی آن یکی دانست، گفت: «مردم اغلب این اشتباه را می‌کنند که ایران را معادل یک کشور عادی می‌دانند. بله، ایران یک کشور است، اما مشکل ما کشور ایران نیست؛ مشکل، انقلاب و سیستمی است که بر آن کشور حکومت می‌کند.»
او با اشاره به مقامات جمهوری اسلامی که با پوشش‌های دیپلماتیک در رسانه‌ها ظاهر می‌شوند، افزود: «کسانی که در ایران تصمیم‌گیرنده هستند، روحانیون تندرویی با دیدگاه‌های آخرالزمانی‌اند که باور دارند رسالت دینی‌شان رقم زدن روزهای پایانی جهان است.»
روبیو همچنین هشدار داد که دستیابی چنین رژیمی به سلاح هسته‌ای، یک خطر غیرقابل‌قبول برای جهان خواهد بود، چرا که از آن برای باج‌گیری و کشتار استفاده خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78557" target="_blank">📅 09:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J110u55wP1VR271A-cKto1J6gKv3H2Y97zQJ0JBOXR9d0_ywlfgqkEesH0PIhPxRG5doTEy5jBTLULb_aTuEzSF9inLEzROb7GETGCvEtAFV8Z2Xmppx7bCqXbcFJeVeJglSFCLkZY7H5IOpPIk82H3T5_I7suU1LjY8PYw2nnt7ZYT52Aiuc-4oGMlPVHqE2nJzEjX_ksM5RjNXs8ycO9uKREe1VcldFjS2MrPzOyoYsXeB4XdgaoSa0S-4MDmw14Fw-e1cTqbFzcneM_a-t0N2fiQ5wFQEZwCk2hDzsii0GbrYtLiBk8TzK6XPYyZ77SOVD1J38uJ5Zk5FPH0cTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، ترجمه ماشین:
اکسیوس همین الان
گزارشی
منتشر کرده که مدعی است «ترامپ» به ایران پیشنهاد کاهش تحریم‌ها و آزادسازی منابع مالی مسدودشده را داده است. این حقیقت ندارد. من به آن‌ها هیچ‌چیز پیشنهاد نکردم!
گزارش اکسیوس، مثل بیشتر گزارش‌های دیگر، یک حقه و دروغ است که فقط برای ارضای «سندروم جنون ترامپ» آن‌ها منتشر شده است. آن‌ها باید این گزارش جعلی را فوراً پس بگیرند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/78556" target="_blank">📅 01:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=poZXKIYpJfutHzCF2tuZmzkHjZFfyVB87NBJsl_Ha_7TuPQ7A7ExcrIfWpfBt_C9A2Gm4sN_vYeoCjm8f3VwwpBKA481_b9WTKFZn3fiF40w8AdnerrxAagSqEFeltr3D08QCtgfIfD8PNyTYh-lwrCfbUWniMLTvtuA8cD-Q7PPCtoIenT_t6wsI_RNCQj_PfQJRRMOPgd38tURxTy21FfpUfaiRwgIAwsHm2rLNsAaYw9Yc2hml1eC1hNAB4k2qpaIffC-wS-8JzYL9m41SuPXmlYYFTJoNPAHL80lwPxo0hiKbcgi04PhsvHyu36xS9JvGzsTKJ_Drtz33YTYEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=poZXKIYpJfutHzCF2tuZmzkHjZFfyVB87NBJsl_Ha_7TuPQ7A7ExcrIfWpfBt_C9A2Gm4sN_vYeoCjm8f3VwwpBKA481_b9WTKFZn3fiF40w8AdnerrxAagSqEFeltr3D08QCtgfIfD8PNyTYh-lwrCfbUWniMLTvtuA8cD-Q7PPCtoIenT_t6wsI_RNCQj_PfQJRRMOPgd38tURxTy21FfpUfaiRwgIAwsHm2rLNsAaYw9Yc2hml1eC1hNAB4k2qpaIffC-wS-8JzYL9m41SuPXmlYYFTJoNPAHL80lwPxo0hiKbcgi04PhsvHyu36xS9JvGzsTKJ_Drtz33YTYEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز دوشنبه ۶ مهر ۱۴۰۵، در کاخ سفید گفت آمریکا «خیلی زود» در جنگ با جمهوری اسلامی پیروز خواهد شد و پس از پایان جنگ، قیمت بنزین به‌شدت کاهش خواهد یافت.
ترامپ گفت: «این جنگ تمام خواهد شد و ما در این جنگ پیروز می‌شویم و قیمت بنزین با سرعت زیادی پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست چنین کاری را انجام دهد.»
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت آمریکا مانع دستیابی تهران به سلاح هسته‌ای شده است و افزود جمهوری اسلامی این موضوع را می‌داند و حاضر است به آن اذعان کند.
@
VahidHeadline
متن زیرنویس، ترجمه ماشین:
ایران هرگز سلاح هسته‌ای نخواهد داشت. ما خیلی زود در آن جنگ پیروز خواهیم شد. آن جنگ تمام می‌شود و قیمت بنزین به‌شدت پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست این کار را انجام دهد. هیچ‌کس دیگری.
اگر دموکرات‌ها سر کار بیایند، مرز فوراً باز خواهد شد و میلیون‌ها نفر درست مثل قبل سرازیر خواهند شد. این وحشتناک‌ترین چیزی است که در عمرم دیده‌ام.
بله، آنها حاضر نبودند جلوی ایران را بگیرند که سلاح هسته‌ای داشته باشد. گفتند: «بگذارید یک نفر دیگر این کار را بکند.» البته این را درباره خیلی‌های دیگر هم می‌توانم بگویم. ما جلوی دستیابی آنها به سلاح هسته‌ای را گرفته‌ایم. آنها هرگز سلاح هسته‌ای نداشته‌اند و این را می‌فهمند و حاضرند آن را بگویند.
وقتی جنگ تمام شود، دو اتفاق خواهد افتاد. اتفاق اول در واقع همین حالا هم افتاده است: ایران هرگز سلاح هسته‌ای نخواهد داشت. این موضوع بسیار بزرگی است، چون اگر می‌خواهید آشوب و فاجعه ببینید، بگذارید آنها یک شهر را با سلاح هسته‌ای نابود کنند.
فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم. نباید بگذاریم با سلاح هسته‌ای به ما حمله کنند. برای همه آن آدم‌های احمقی که فکر می‌کنند اشکالی ندارد، من با آنها سروکار دارم و آنها دیوانه‌اند. هیچ تردیدی در این نیست. آنها آدم‌های بسیار دیوانه‌ای هستند. همیشه این را به خودشان می‌گویم. می‌گویم: «مرد، تو دیوانه‌ای.» اما آنها نمی‌توانند سلاح هسته‌ای داشته باشند و ندارند.
پس این موضوع بسیار بسیار مهم است که ما در چنین وضعیتی قرار داریم. این کاری است که سال‌ها پیش باید توسط رؤسای جمهور مختلف یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم، اما ما با فاصله قدرتمندترین کشور جهان هستیم. بهترین تجهیزات نظامی جهان را داریم.
و ضمناً، اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات نظامی تولید می‌کنیم. چاره‌ای جز این نداریم. شرکت‌های بزرگ دفاعی در حال گسترش فعالیتشان هستند. مثلاً لاکهید پنج تا می‌سازد. ریتیان هم تعداد زیادی می‌سازد. همه‌شان دارند مقدار زیادی تولید می‌کنند. اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات در راه داریم و به‌زودی واقعاً تولیدشان شروع می‌شود، چون این کارخانه‌ها قرار است شروع به کار کنند.
قیمت بنزین خیلی پایین خواهد آمد و همین حالا هم، می‌دانید، اگر نگاه کنید، فکر می‌کنم پیتر، این صددرصد است.
پس ما ارتش ایران را از بین بردیم. تقریباً هرچه داشتند را از بین بردیم و هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ما بدترین تورم تاریخ را داشتیم. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که در دوره بایدن شما برای بنزین خیلی بیشتر پول می‌دادید.
بیایید درباره همه این چیزها، می‌دانید، همه‌چیز صحبت نکنیم. در دوره بایدن، شما خیلی بیشتر برای بنزین پول می‌دادید تا الان.
و کاری که من کردم این بود که وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاق‌ها برای جهان، برای ما و برای بقیه جهان باشد. اسرائیل الان نابود شده بود. دیگر اسرائیلی وجود نداشت. دیگر خاورمیانه‌ای وجود نداشت. و بعد موشک‌ها و بمب‌ها به سمت ما و اروپا می‌آمدند. و من جلویش را گرفتم.
و این آقا داشت ۱۸ میلیارد دلار در آیووا سرمایه‌گذاری می‌کرد. او می‌گفت: «من می‌خواهم از آمریکا صرف‌نظر کنم. قرار نیست ۱۸ میلیارد دلار خرج کنم»، چون ما یک دیوانه و یک کشور دیوانه داشتیم که با سلاح‌های هسته‌ای این طرف و آن طرف می‌گشتند، چون قدرت بسیار زیاد است.
اما هیچ‌کس درباره‌اش حرف نمی‌زند؛ هیچ‌کس درباره همه آن کارهای باورنکردنی حرف نمی‌زند.
باز هم، خیلی از شما... نمی‌خواهم بپرسم، چون می‌گویید: «اوه، ما قرار نیست این را گزارش کنیم. ما رسانه اخبار جعلی هستیم. اجازه نداریم گزارشش کنیم.»
همه شما حساب 401(k) دارید. لازم نیست چیز دیگری درباره شما بدانم. حساب 401(k) شما در مدت کوتاهی دو برابر شده است. دو برابر شده. ثروت شما دو برابر چیزی است که مدت کوتاهی پیش بود؛ تک‌تک شما، و این به خاطر من است.
خوش بگذرد، همه. خیلی ممنون.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78555" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">"ترامپ در ازای امتیازهای مشخص هسته‌ای، به ایران پیشنهاد گشایش اقتصادی می‌دهد"
اکسیوس، ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، آماده است در ازای برداشتن گام‌های مشخص از سوی ایران در ارتباط با برنامه هسته‌ای، به ایران تخفیف تحریمی بدهد و دارایی‌های مسدودشده ایران را آزاد کند؛ مقام‌های آمریکایی این موضوع را اعلام کرده‌اند.
🔻
چرا مهم است:
پیام آمریکا به ایران در حالی مطرح می‌شود که میانجی‌های قطری و پاکستانی این هفته بار دیگر تلاش می‌کنند میان دو کشور در حال جنگ به توافقی دست پیدا کنند.
▪️
در حال حاضر، دو طرف بر سر مسائل کلیدی فاصله زیادی با یکدیگر دارند. ایران می‌خواهد مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا متمرکز باشد، در حالی که دولت ترامپ خواستار آن است که ایران با امتیازدهی در زمینه هسته‌ای موافقت کند.
▪️
با این حال، این پیشنهاد پس از آنکه ترامپ آخرین پیشنهاد ایران را رد کرد، روزنه‌ای از امید برای دستیابی به یک گشایش دیپلماتیک ایجاد می‌کند.
🔻
تحولات اصلی:
میانجی‌ها امروز در نیویورک با عباس عراقچی، وزیر امور خارجه ایران، دیدار می‌کنند تا درباره پیشنهادی از سوی قطر گفت‌وگو کنند که طرف‌ها طی چند روز گذشته مشغول مذاکره درباره آن بوده‌اند.
▪️
انتظار می‌رود میانجی‌های قطری اواخر روز دوشنبه یا روز سه‌شنبه با مقام‌های دولت ترامپ دیدار کنند تا برای دستیابی به یک گشایش تلاش کنند.
▪️
یک مقام آمریکایی مطلع از مذاکرات غیرمستقیم، این گفت‌وگوها را «مثبت و سازنده» توصیف کرد و گفت ایران «نشان داده است که در مسائل هسته‌ای انعطاف‌پذیر است.»
▪️
اما این مقام همچنین گفت هنوز اختلاف‌هایی وجود دارد و تأکید کرد «تا زمانی که به مسائل هسته‌ای پرداخته نشود»، توافقی در کار نخواهد بود.
▪️
این مقام گفت: «طرف‌ها همچنان درباره زمان‌بندی تعهدات و اینکه چه کسی باید ابتدا کدام گام را بردارد، اختلاف دارند.»
🔻
آنچه می‌گویند:
این مقام گفت: «تردد در تنگه هرمز همچنان در حال افزایش است و محاصره و تحریم‌ها همچنان موقعیت ایران را تضعیف می‌کنند. موضع آمریکا هر روز قوی‌تر می‌شود و رئیس‌جمهور ترامپ همچنان صبور است و کاملاً به هدف خود مبنی بر اینکه ایران هرگز به سلاح هسته‌ای دست پیدا نکند، متعهد است.»
▪️
این مقام افزود که کاخ سفید نسبت به وعده‌های ایران بدبین است و ایرانی‌ها را متهم کرد که با شلیک به کشتی‌های تجاری در تنگه هرمز در ماه ژوئیه، آخرین تفاهم‌نامه را نقض کرده‌اند.
▪️
این مقام گفت: «آمریکا این بار به تضمین‌هایی نیاز دارد که نشان دهد ایران جدی است و صرفاً تلاش نمی‌کند از شرایط دشواری که در آن گرفتار شده، خارج شود.»
axios
🔄
آپدیت:
ترامپ تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/78554" target="_blank">📅 20:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3aba301950.mp4?token=CkBbX2uBlvoF6CrkkVGA-fH9hU4nUAFC5a05DWIfoRbw9tqV2cTYP2AYWGmaBp3_9zndxGON7b5WqOkXrZvceerfhsoFnOtE7sWRJNq5nUw6MbLbP-nYTRBvcZZGfLW6sq_kBlEPA6FHavMO-yExrHcl91SLXLzcUcfBW0jY4aG1D4i01jYmH03S4lXvAHMWcA2iNoZxEHeo0b9ADYrJXrRE1Zq6MfVjuhFTO87nitbU356NnmjCnteRNNCaonw7NjYf6emvCBYnyAdzXiaGnwqikcexjByoAkcslKYNL4tH2wEkux4guqCjku9NlnoMMrkIYAq6FLEzsJWyE2vyiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3aba301950.mp4?token=CkBbX2uBlvoF6CrkkVGA-fH9hU4nUAFC5a05DWIfoRbw9tqV2cTYP2AYWGmaBp3_9zndxGON7b5WqOkXrZvceerfhsoFnOtE7sWRJNq5nUw6MbLbP-nYTRBvcZZGfLW6sq_kBlEPA6FHavMO-yExrHcl91SLXLzcUcfBW0jY4aG1D4i01jYmH03S4lXvAHMWcA2iNoZxEHeo0b9ADYrJXrRE1Zq6MfVjuhFTO87nitbU356NnmjCnteRNNCaonw7NjYf6emvCBYnyAdzXiaGnwqikcexjByoAkcslKYNL4tH2wEkux4guqCjku9NlnoMMrkIYAq6FLEzsJWyE2vyiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامحسین محسنی اژه‌ای، رئیس قوه قضائیه جمهوری اسلامی، روز دوشنبه ششم مهرماه از دادستان کل کشور و مقام‌های قضائی خواست تا با آنچه او «وضعیت برهنگی» توصیف کرد، «قاطعانه و با برنامه‌ریزی» مقابله کنند.
اژه‌ای خطاب به مدیران قضایی گفت: «نباید از هیاهوها ترسید... رئیس جمهوری هم با مقابله بابرهنگی موافق است. مجلس هم قطعا موافق است که این بساط برهنگی جمع شود.»
جمهوری اسلامی در زمان اوج جنگ تصاویر زنان بدون حجاب حاضر در تجمعات شبانه حکومتی را به‌عنوان حضور ایرانیان از اقشار و افکار مختلف، پخش می‌کرد و در اختیار رسانه‌های بین‌المللی قرار می‌داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78553" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
