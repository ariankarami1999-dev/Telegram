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
<img src="https://cdn1.telesco.pe/file/ZhdMPQFEqEe1Nrn44BNJSD_2_VzT8t6K4mHPmQu2XL8JVhrFPP96S5lRktvUGW7aUHgkWi3EBIFJuaHX38FXDlxnpsDLQp-86KiuFVLuJsexOSEROzIIek6C1j3NNSc4U2vEXjX7K_vUkrmUDmomlOfZtBazLUniaU4BwzQg7BndaFBR_xlfGvz_nZx5d-1DQtxVipFYjc3sLeFVjTeXgm4WcJiDcqDVnaOfz30a4ttAqLOvrRvm3oMb2rTbiPzWlLI_oKtKELRaxCn9dgIgeWLNlbGyo1KrDDclIKpVR3koAaaySDx5Q8CvEnbeZYDU6-Ro5--UgNxIghUik6TMjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 20:59:37</div>
<hr>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep5MOP1VtTBow0182xuQnec4MLjWJVBXAlW83_FhZrT2TPeK3drzX3iHq-_WGQlKWgmA5c-E-KgI9Yi4hq6YAagQbcSfCN_b8cmPttIN8vedg01xAlsEwn-gKWWzO4UPJbFKkYUL6GH3-LSnXNbPiIWhLrA2ZL0v-HBNXQzAwjm-GnpAP8OwZa8IcRuyR86Je-XWXY5nVP2_Hfu3TSn7B8zlpBr4SyhgOQpvrNzYJ0ohtZ3r1umkr2QkNmCPaKg1OGsDeYLiC_4rN7MT1dvB_Lf23PHOx4okRIgvDlPFSBeHOngwJZptC-8_-MJfGINNqEzKy-JzKbnUFtGmQGvMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع دولتی عراق به خبرگزاری فرانسه گفتند بغداد در پی اعلام وزیر خزانه‌داری آمریکا مبنی بر اینکه شرکت‌های تحریم‌شده ایرانی ظرف دو روز در سراسر جهان «تعطیل خواهند شد»، پروازهای شرکت‌های هواپیمایی ایران را متوقف خواهد کرد.
یکی از مقام‌های عراقی گفت: «عراق از بامداد سه‌شنبه، مطابق با تصمیم وزارت خزانه‌داری آمریکا، ممنوعیت فعالیت شرکت‌های هواپیمایی ایران را اجرا خواهد کرد.»
منبع دولتی دیگر نیز این اظهارات را تأیید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/VahidOnline/78477" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZplnmrfayLE0NxKU9FRKiPKpwEBJvPoyrY29stUKSlDxr9ptxqV-hxGv9oNxihtRwRJVYDd07gx0IBeEANvT1G4_TVMKDz9YjBTkMF465ygklixehSJardzEHGn609PxWgE3bkNe8VbnbKrZXBcFFBA9WWGWgwgnnTOwH4ELJ5-pVUN3qEJzgIGTRt_8vcv01tzIF_K8n2qV6AzbGLMJZcHnTzA4dgYDBYEr-_cSIjNppwpTiVp9nPF8NbyNk9E6Gt_53kbS7MSKPTf21jCfBbTs9r7bTPCL-OY4DdXie34NcVtHgq-TJhxwwxJHCd0PJDGCRW65KJYHQ7hHtwwTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز، روز دوشنبه ۳۰ شهریور به نقل از منابع آگاه گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، آخر هفته گذشته حمله به شبه‌نظامیان حوثی وابسته به جمهوری اسلامی ایران در یمن را بررسی کرده بود، اما در نهایت اواخر روز شنبه از اقدام نظامی منصرف شد.
بر اساس این گزارش، ترامپ ابتدا در جلسات چهارشنبه با مشاوران امنیت ملی متمایل به اقدام نکردن بود، اما پس از تماس تلفنی شاهزاده محمد بن سلمان، ولیعهد عربستان سعودی، در روز پنجشنبه به پنتاگون دستور داد برای حملات هوایی آماده شود. با این حال، با اکراه کاخ سفید از گسترش میدان نبرد در مقطع کنونی، تصمیم بر آن شد که فعلا از اقدام نظامی آمریکا خودداری شود.
رویترز نیز گزارش داد که ترامپ روز دوشنبه با رشاد العلیمی، رئیس شورای رهبری ریاست‌جمهوری یمن گفتگو کرده است. حوثی‌ها طی هفته‌های گذشته و در جریان تشدید درگیری‌ها، توانسته‌اند مناطق راهبردی مهمی به‌ویژه در امتداد ساحل دریای سرخ را از دولت یمن تصرف کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/VahidOnline/78476" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=BrJ20hSd98q5XUUpwtTkq4NceN0uBgt5KXXESDbzrSDlGLynpMZG-J9J0a9W14HJCz6-lUHzVx1zIRBU8F5Ps3F9Cg1zERqZQcsxSH2cydI8iouZ8ULkBbI8Z5SUfrSwaiI9AmOnq4WSiBfDaW1u9h7afLg_8LOg4IFpI7IEoWFvOWFPxPXgRtkFJh0iMV_OmRlOHBtDBiP4-F8gd2KE05u5fYMi50FAA8LdUyWE1UAI6ceXTXNpUkQxyx9A87V-NZlIDMdoW5Bj9GWsnDQWxaNDfNn2J2DY43CKdbSqXUXsZhrMi9EnfMHL7z4FTsp7qDRlXH-VfuGVveE0dwDfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=BrJ20hSd98q5XUUpwtTkq4NceN0uBgt5KXXESDbzrSDlGLynpMZG-J9J0a9W14HJCz6-lUHzVx1zIRBU8F5Ps3F9Cg1zERqZQcsxSH2cydI8iouZ8ULkBbI8Z5SUfrSwaiI9AmOnq4WSiBfDaW1u9h7afLg_8LOg4IFpI7IEoWFvOWFPxPXgRtkFJh0iMV_OmRlOHBtDBiP4-F8gd2KE05u5fYMi50FAA8LdUyWE1UAI6ceXTXNpUkQxyx9A87V-NZlIDMdoW5Bj9GWsnDQWxaNDfNn2J2DY43CKdbSqXUXsZhrMi9EnfMHL7z4FTsp7qDRlXH-VfuGVveE0dwDfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره جنگ ایران گفت: به دلیل اینکه ایرانی‌ها در حال ایجاد رعب و وحشت در کشتیرانی بین‌المللی هستند، قیمت انرژی افزایش یافته است. ما هم، طبیعتا، تلاش خواهیم کرد در برابر این اقدامات مقابله کنیم.
معاون ترامپ افزود: وقتی ما برای اطمینان از اینکه ایران سلاح هسته‌ای نخواهد داشت اقدام کردیم، آنها در واکنش، با ایجاد اختلال در کشتیرانی بین‌المللی، به این اقدام پاسخ دادند.
ونس افزود: ما، البته، تا حد امکان تلاش خواهیم کرد از جریان آزاد تجارت محافظت کنیم. این همان کاری است که نیروی دریایی ایالات متحده انجام داده است.
معاون ریاست‌جمهوری ترامپ گفت: ما همچنان شاهد عبور حجم قابل‌توجهی از نفت و گاز از تنگه هرمز هستیم، با وجود اینکه ایرانی‌ها هر روز و به‌طور مداوم برای کشتی‌ها ایجاد مزاحمت می‌کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/VahidOnline/78475" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F8HqTMSf-41UzkH4jK3Zdr36cQNqL6AwOROw0LjzIQH1nE43zRKEwVDupO9ZIj0jvx7ebYdoxuN4MmKPO2C43g0Xfp_ZT99fJi-OCh4FiVhu-fbLPXKz2GOcn2-8-57MLUKmC2WMQ1MRlfJaLSxZybgcwLXlBB5i9cgKfMJoVKOzT1nFFZDUus3VRGYbF0i6xSbFx1piMnifStp7N6enb3K57PQHV8_uy2vCH3K4XEwRo39q1_HwuqS6oKOMmizog31wSiFbwXCfMQSBqBGkLuZWrGee82FrECUXSu224QSdd1qhMNuPrE3gGdTWxp6dD6RBC4xAf9BJVI2hoFVSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MlhAY50Hr3dKDlvnrdclbOUnWEaLSh23WSjw1Sn61wgNKV7Oxkg_-_sXppjhbbEJp_Qw5MteK6L3n8yHclRI8Q895WxRSa5ZWyPUlw33tg9zbZhNy6OOv1TbimOmruu5hspFSo2XL3YY9PZm-SRs22OYGT2gN1pFrnvRUQNu7Iiyw78U5vWVGdAkgdAUfa5Bw8D-83GvRZKBAxyLTifLfm8Wm62nU0lx8HwMeAtGRrAmkusT-9yfU6PoWipTZ09dZdXnnisz4NXqOrljMXEaveyHJ2LKz4wiDt71L7NF14OoYr_AsV3vZJ2bo7olRSQquGEzVFq9th_1ur1Y-T0FHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fndFjxKNjZCAjvpjvSNcGVbF2M6Sge5ilR8pvaUSeiLFZu7MUDhxxrvYlFKorduwBFBoH1wLZzeg8JyOi3JwQr80Ctrz7cP0sOuVnIRtmXtntFuw4fuhMfmIVeuzsP4o_3Y16PUCZOh8TzEL4Vt2nMmUm5N7hVSDeaHHltSkoPZGghoEkXWHJjs-Zi2xTJMtikhLF14QAsnPk3Y0-qQinX8IlQb72oqRDWoj6RGj6oC7ZpMId4EzuBaWmUNpSOsTE65ETutkFAt3ZXd_l1cIlNEGiTRctPkBGsOjHz18dT4VtQ1t5WIGft6BtSvJzPHXmciaNVLkLtYVQPcxqcc5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PD1LTaELv17gjTavWKMU9UNe4tgFUx7xi0t98zN9nzEe-IbjdRI6RuAVrntAyoq1YR4FNIp_1spfne7eXrEEBLqruLmdkNcU9d8Ey3UJMEVgpk2UL_P1iZIDiu5ntCmiN1INLCBcwsp28iVP8RP5nGiI_TZkmhbhYr3LucDyWqOgoNlMb8PXF5qrvYW5UdJbWljbxQgFizHfSFaoYXjI1Bq8Qnk1BEnQ6bYeBzxF6Npl7RqXZG9G5g-Au5x0M_hI1I6VtAHLS61IsjD7qTLHHK0H6Q7fPRPpn9WMeFjyQr4NKV5e1ap3MJdbpH08fM3wH0fOKywqYVdw3XGqjY0msg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هواگردی که توسط ارتش جمهوری اسلامی ایران در نزدیکی تنگه هرمز ساقط شده بود یک موشک فریب آمریکایی ADM-160 بوده است که به اشتباه پهپاد اوربیتر تصور شده بود.
آمریکا با استفاده از موشک MALD به دنبال شناسایی موقعیت سامانه های پدافندی ایرانی است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/VahidOnline/78471" target="_blank">📅 18:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78470">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NSyQQxOh8NdlCjMxzf-MIby1PvjUzi_GmDU3bWwQ0JgsPtGOHE7yNC6ewTxjlHRAvXCk40JoOvV36rtUeldSY4ocyORNNNq7kRpQ9yxZ89_szC4jKIh1RU2FTWPVCFxioA_XySZdXBOPqs8WQOYnBvsVKG-eVL16CwkTW929wv1oTu7ZB1mBK2sDe9EW2cu2Lln7DZY4OuDIUVFRrp73kfUEzsTYelG1j4HY8jxdXksBM4Ma3ybGqndsRrnBUhdNcr1LchUPUoHNm2ET6doHipPtSAbtmVJztB1yix1FecBe-r-d3UXCgmNjl7e5nTgjP66SyrSoizGOmF14Rlbn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، روز دوشنبه ۳۰ شهریور، در گفتگو با شبکه خبری «سی‌ان‌بی‌سی» اعلام کرد که فشارها بر جمهوری اسلامی به بالاترین سطح رسیده است و از ۲۳ سپتامبر (اول مهر)، تمامی خطوط هواپیمایی ایران در سراسر جهان متوقف خواهند شد.
بسنت با اشاره به اقدامات جدید وزارت خزانه‌داری از جمله در حوزه‌های هواپیمایی، دریایی، ارزهای دیجیتال و طلا، تصریح کرد که طبق این تصمیم، در صورت نشستن هواپیماهای ایرانی، ارائه سوخت، خدمات فرودگاهی و فروش بلیت به آن‌ها ممنوع خواهد شد و هر نهادی که این مقررات را نقض کند، از سیستم دلاری آمریکا خارج خواهد شد.
او همچنین از برخورد با حامیان مالی و «تسهیل‌گران» منطقه‌ای و بین‌المللی این رژیم خبر داد و افزود که سه بانک از جمله دومین بانک بزرگ مصر (شعبه دبی)، سی‌امین بانک بزرگ ترکیه و دومین بانک بزرگ روسیه به دلیل انتقال میلیاردها دلار به نفع حکومت ایران تحریم شده و فعالیتشان متوقف خواهد شد.
وزیر خزانه‌داری آمریکا تاکید کرد که دولت این کشور با تمام توان در حال بستن منافذ اقتصادی حامی تهران است.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا همچنین گفت مقام‌های چین در گفت‌وگوها درباره کارزار فشار اقتصادی علیه جمهوری اسلامی حضور فعال داشته‌اند.
به گفته او، آمریکا مذاکرات مثبتی با مقام‌های مالی چین درباره رعایت تحریم‌ها علیه جمهوری اسلامی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/78470" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgw25lXRag2YU56qNURME__qRy0pOYQznk0oznl-C0tvAsPNecYpN7zZgI5-u3BU5Ip8uPJhKBwjJ_8sGzummLbpBuJ1ggQmdWmMhN9kk0g6HlyrDGDxoulYW4vuuiBQv05RhtCFXU4bNa8iyw10x6tvYSr-aOdN3mPzj6ZsCX1AetNyYeBONYSXWGbHHTAEStqubErxeWb8zxw91H0S9KHev0WJo7enXSKcGMdd1_yLMvOv-_noa8IUtwRkML_-eMljQHMqsgmNUo5UiXSOZQcrIfrtGyL_J7DmnnHl30dl89jzAK2Mjs24xC_dWSwHQrxKlR8FpGxkQDBhOrIB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه اعلام کرد در واکنش به اقدام حکومت ایران در پلمب یک مرکز آموزش زبان فرانسه که به سفارت این کشور در تهران وابسته بود، سفیر ایران را احضار می‌کند و «اقدامات مقتضی» را انجام خواهد داد.
پاسکال کُنفاورو، سخنگوی وزارت خارجه فرانسه، روز یکشنبه، ۲۹ شهریور، در بیانیه‌ای گفت: «این حمله جدید علیه حضور فرهنگی فرانسه در ایران، پس از تعرض به دو کارمند سفارت فرانسه در ژوئیه گذشته، غیرقابل توجیه و غیرقابل قبول است.»
خبرگزاری نیمه‌رسمی تسنیم روز یکشنبه، ۲۹ شهریور گزارش داد که مقام‌های ایرانی این مرکز آموزش زبان فرانسه را بر اساس دستور قضایی دادستانی تهران تعطیل کرده‌اند.
مقام‌های ایرانی مدعی هستند که این مرکز، با وجود هشدارهای مکرر برای دریافت مجوز، سال‌ها بدون مجوز و تحت پوشش آموزش زبان‌های خارجی فعالیت می‌کرد.
روابط میان دو کشور طی سال‌های گذشته بر سر برنامه هسته‌ای ایران و بازداشت چند شهروند فرانسوی توسط جمهوری اسلامی پرتنش بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/VahidOnline/78469" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOX9nLLqw-hfORzmoJPkDRWdPzIP5WWK6YNdMtFg4-4FD0lMf-AGQJdiBHABYMJX8Ssu0KdyfYiyLB1npY_RtEzXxl4fJsxF-VwTtqcd-x5j62nWwhHkCpEedG0QmFpJlS-ROU9FSnD-GD-AtalW0bPaQjYcwt_WZOE2As38XRM3Li-x_Ayvs9rwdvSluYP-Jt3KVRyhNplwJSAvOqZd1sDUGdlPA_zidEnAJBRILeAAnKqFrzZzgVr_n6DuGamM2jODpp4iH4AHSpvn_PoUiA7YHcaetN-NwALEtFI-EQbpwMVtMXGAaPuTEUK2QZoa8E99L9xLo1cuB8hJ0RV6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «تسنیم»، وابسته به سپاه پاسداران، گزارش داده است سفر «محسن نقوی»، وزیر کشور پاکستان، به تهران ارتباطی با انتقال پیام یا میانجی‌گری میان جمهوری اسلامی و آمریکا ندارد؛ روایتی که با گزارش شبکه «الجزیره» درباره هدف این سفر متفاوت است.
تسنیم امروز دوشنبه ۳۰شهریور۱۴۰۵ به نقل از یک منبع مطلع نوشته است که سفر محسن نقوی به ایران در چارچوب همکاری‌های دوجانبه تهران و اسلام‌آباد انجام می‌شود و ارتباطی با مسائل میان جمهوری اسلامی و آمریکا ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/VahidOnline/78468" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG3-MEuoSt0Uqmx9ByCZOlEcmUUctyHsWHHYmpDjSzbf9Jg5sGLw-XoymM5UPlfhufJyXdjZ0_GJ3H8o-crSoUHv-KhhRkzqJ-wW3_asHqt5NQ93GeMnlsCdI2lpxdVTqUwLP5O2yk0Cv09oHJpcnXEILpi-9THSEe-NdIsJAAEu_IhkVEMacWyG9HO9JaCO6qu8hK_K-gxGuviwCmXxW7DUvT8XEsB1cAEqFrDwV3EyTiwgY-wGltqRIVHsV3eQdzZvX50lPc5EQtoo9Hhr7aen9jn9hp78SKBRCdGstm8uuhE5bj9tB-ozPJj6PGl3J3S80gGzUfyLxzIV0OkkVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌های منتشر شده، امروز دوشنبه ۳۰شهریور۱۴۰۵ یک نفتکش هنگام ورود به تنگه هرمز هدف یک پرتابه ناشناس قرار گرفت و دو نفر از خدمه آن زخمی شدند.
«آسوشیتدپرس» به نقل از ارتش بریتانیا گزارش داده که این نفتکش هنگام ورود به تنگه هرمز هدف قرار گرفته و دو خدمه آن جراحات سطحی برداشته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/VahidOnline/78467" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtsoY7DQo9lvK92utWX2IbK0W2wR9iTQzqsjnOO2XqBDzGcoeqB-b4IvqyrjLoqpqsWuPIULE4vspsURkC2TRUav_YXhiq2VST6Ic3lI_Zzj7e37s-jbLAt8jEb7q74jNMjj8Uqq6DCmitu-Afv0ps6KxywouGnr6Gmx7fvTm-btVrtKySlRhK4t3JP-aNu_zPzXI-TTM1deNkBBfYfotCBpiwif5NIogIkbE-fW0mZMMGLIu0JP81rJjaE-Wty-h0ryuV0uwwWiniB6ZFyJuRPETwTyV91zQtChfyzhlBcFc593P7tX5dsqAcqfxHPUdFpYadje1YM9tYheDSIr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aH3Hs7OCLgi7iTl5sKvuDJBsgEJpkA6qXLTgJrfybX0IpSudBcZnDR0u8Qaj_kAPefDtdAuPSGlxLb03HfU_-MSP50DuwEV4XPwBMl5kd3QU7e0MsPhW9WaKX9QmuAEQF-1M_Ufvg2E2kD_wemsij8yVRjO_g1FzhqS9NNVwXqPOJXLLyCQu_HSd0shDf_VdH49ebzJJF2a4-8d802YZnfMPNAXmP-wNoPUXKEmIuIqP0OCEcE7Umbn8NHbHPjq1EeDdnLaOBJboC8orl_6L53k4cflRFf2-BIQNEqfi9Haba9Tp_aHscMwvVlwN71ExkqXK9wG91t6GeGsUvxtcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHoIDm_iX9FRCkHl3h4u1HceDYG8ZBFrNGNlJZhiIVlnvPrzS8RsLGDsEQEsGJxyhIp9DXPXJNLifFWt_H7l5gMge5ShY-H3EC32hhkkIOhoPVwEunD6LVooJIkkc4Gc9hC6th7PqbpRhSGeSxN_EiOcAXIkfb1xsaRGNI1gMt2h8QFF985Ssy5UkE26wV5RGWqtah1uF3sMWTNdoZMDLfKVgBtcxBJapA43QpXUtEi-8BbzB6Fu1W_etbjbvrYJ9paWXBfQYit4z5DQFJW5xYMWrKaonyXMuRXOLCVErsdX-tJmaNT-7kFks8eW8PbaB5hf_AVs-Rgz7KeVyWEvdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hotn4ySsX-EFuhz64aYRu3kdw_2t0Oh5TDsRrh6m5oicte-i_ITesyIASt1eARYCwK_ZEiMgkr4Zj_ajtW0rDll7sSV0FJA7xKhTmX4iBHvO2d-KjAl80HL1ZHMahbGzrs7Vg53iSbx-rPSk7aTpFEervR7-_DKq83rS-ZOqQf-qjfNEqmyYG-oqV5gpQ7Kg4xODGwrivF3aesBcZ9472NqcFXGzPoQ5c7V8J9hIIWb7VfxZZFagAlyPjXjosFzheUHOfshS-h4zKbRryGgTV-9zEkvuXbxhjWJUadoutGPQUOsKJ3djeHYHl_7HOutoQzkL-Y_Rs0r31OuNzdYyfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
پدر و پسری که قربانی قتل‌های زنجیره‌ای شدند.
🔸
آقای حمید حاجی‌زاده و پسر ۹ ساله‌اش کارون، نیمه شب ۳۱ شهریور ۱۳۷۷ در منزل خود در گلدشت کرمان، به اتفاق با ضربات متعدد چاقو به طرز وحشیانه‌ای به قتل رسیدند. آقای حاجی پور با ۲۷ ضربه چاقو و فرزندش کارون با ۱۰ ضربه چاقو کشته شدند.
🔸
خانواده حاجی‌زاده در تمام این سال‌ها برای روشن شدن حقیقت و پاسخگو کردن عاملان قتل حمید و کارون تلاش کرده‌اند؛ پرونده‌ای که با گذشت نزدیک به سه دهه، همچنان بدون پاسخگویی و اجرای عدالت باقی مانده است.
🔸
سرگذشت کامل حمید حاجی‌زاده و کارون را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-7014/hamid-hajizadeh-pur-hajizadeh
https://www.iranrights.org/fa/memorial/story/-7010/karun-hajizadeh-pur-hajizadeh
@IranRights</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/VahidOnline/78463" target="_blank">📅 17:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPt-hpdWeLFJCMJ5SUPC9_gcHVxLDK24Ff6AI59BeChKGYe7M76ELkCI8SasT1YszKPmO_rc3_uL00ydoHaUsKTd1fYyeuAnooNC-61DrZQhp2Xg-4U5PMxqb1dXI1wkK_ixr6V0Y1Q4hAsqZBTi9DdXpiPgZuupVfMRDIxV4hDEOQqmLN7M7kMwYjSe3hlfedbjEHDJpiMqYN3cEeYi4a0-Wi_6Y4XdZ1WnBJQFQBip7YCWf_OPWI_2bPlS0ANJMHke0eMF-IGp67nByIUJeF9cpQflvGoW8odJZSqqhxLuFAcIArGmeavhQdaKmormmeavIVBJ7LT-8UAZqb1nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز آمار ایران روز یکشنبه ۲۹ شهریور نرخ رشد اقتصادی سه ماه ابتدایی سال جاری را منفی ۱۰.۱ درصد اعلام کرد.
بر اساس گزارش این مرکز که در خبرگزاری جمهوری اسلامی، ایرنا، بازتاب یافته است، تولید ناخالص داخلی کشور در این سه ماه ۲۱ هزار و ۷۹۵ میلیارد ریال بوده که نسبت به مدت مشابه سال قبل که ۲۴ هزار و ۲۵۵ میلیارد ریال بوده، بیش از ده درصد کمتر شده است.
کاهش قابل توجه رشد اقتصادی ایران در حالی است که نرخ رشد تورم در کشور نیز به شدت افزایش یافته و بر اساس آخرین آمار اعلام‌شده به حدود ۸۰ درصد رسیده است.
از سوی دیگر ارزش پول ملی ایران نیز در شهریور ماه به شکل مداوم کم شد و قیمت دلار آمریکا رکوردهای تازه‌ای را ثبت کرد و از سوی دیگر مقام‌های ارشد دولت نیز از محدودیت شدید در صادرات و واردت و کسری انرژی خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78462" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78461">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVzQ0Jweg_-xdJPkIsiQvneeviosP78TxmhkWc5ONXK1-VXsfbXOOaod5OK5M9rwWLLbCANr-xNsxqtyR7Plyv91ltMQfxl7PXzFUM8dKjtGOX9GmYFIYUx0N3KlBuX83LWiiPk4ObiXy69nojGosD-nfgVjyl_vzO-C0PqP9Yrser2q0meamkw7OGBKqNbdbm0k_FuF_iIqBYcWTO53hQT2fRBEE5Qy4k0cBnSeQQdOW7ETdVtPY7o5d5E1ZXkjTCzFp9U2l4CckgoXSj2O_Cb04VJqxVBptIXcMSFzH1o6rK9AJFLbUK-l4YH6lkMmdYxDbOrlrmvyq2d-2wK7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید موسی شبیری زنجانی، از مراجع تقلید شیعه، یک‌شنبه ۳۰ شهریور در قم درگذشت. خبرگزاری فارس گزارش داد او از روز جمعه به دلیل خون‌ریزی معده و عارضه ریوی در بیمارستان بستری بود.
شبیری زنجانی متولد ۱۱ اسفند ۱۳۰۶ بود و در سال ۱۳۷۳، پس از درگذشت محمدعلی اراکی، از سوی جامعه مدرسین حوزه علمیه قم به عنوان یکی از هفت مرجع تقلید مورد تایید حکومت معرفی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78461" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78460">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=usPNhVeyAlDy-E8qIrFz8a8fpGKQNIH2sbUUlIwtmNSF7-3RRsnpOVujtxYDlXv3M1vETCzmEkvIslnOiH68kji3LYhlQ93ZNghH2raXjDyMwTPFPFs7L3TsJZk0cL5PHUKX9QgFNEWvbb4c7FNieV-z8vZ227XdMGGAB0LlpDgB3yMtWO17ZmX8auAED7Ox1JKV9M5XG6Z68QSo5rIOaQ4DpWZDFs1iewHHs-6pPzFg-J0-ugeMUSgTg9A4MRUsPWz1n2urcfKKSS_gxbFWZpbCyU9IJozMvXTgy9Ns5nnvCBKjC014najg0I93Ui4AwHoXnQElvFrm8NZYAmxI3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=usPNhVeyAlDy-E8qIrFz8a8fpGKQNIH2sbUUlIwtmNSF7-3RRsnpOVujtxYDlXv3M1vETCzmEkvIslnOiH68kji3LYhlQ93ZNghH2raXjDyMwTPFPFs7L3TsJZk0cL5PHUKX9QgFNEWvbb4c7FNieV-z8vZ227XdMGGAB0LlpDgB3yMtWO17ZmX8auAED7Ox1JKV9M5XG6Z68QSo5rIOaQ4DpWZDFs1iewHHs-6pPzFg-J0-ugeMUSgTg9A4MRUsPWz1n2urcfKKSS_gxbFWZpbCyU9IJozMvXTgy9Ns5nnvCBKjC014najg0I93Ui4AwHoXnQElvFrm8NZYAmxI3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: ۲۹ شهریور، ساعت ۱۷:۳۰، اربیل عراق
هم‌زمان:
رویترز به نقل از منابع امنیتی عراق اعلام کرد که سیستم پدافند هوایی، یک پهپاد را در نزدیکی فرودگاه بین‌المللی اربیل در اقلیم کردستان عراق رهگیری و سرنگون کرده است.
@
VahidOnLive
آپدیت:
نیروهای ضدتروریسم اقلیم کردستان می‌گویند که صدای انفجار شنیده شده در نزدیکی فرودگاه اربیل ناشی از «تمرینات نظامی و فعالیت‌های امنیتی» بود و «هیچ خطری ایجاد نمی‌کنند.»
این فرودگاه میزبان نیروهای ائتلاف به رهبری آمریکا در اقلیم کردستان عراق است.
رسانه‌های محلی کرد گزارش دادند که ائتلاف به رهبری آمریکا مهماتی را در این منطقه منهدم کرده است.
یکی از خبرنگاران خبرگزاری فرانسه گزارش داد که شاهد برخاستن دودی خاکستری از نزدیکی فرودگاه بوده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78460" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQMl35INXTbWmeUW-q5pM544sf_kA2pa88hUzQHmgoCKDDiws6EBZXUx7hB_Bu8wVdtU8ExcSCzx1i4-CHNCephDqMAEvfgkF_OPjlmYtcqCTKT5xaqKq61KvhgtaEtLC_z6GwoqPSYoy2iFMht2b9OjZcwpQ1UG4uoPQQqcknOcAlEZLlMlIi8E9sguZDSW81YfogyvtmXV12yB67s_kDqEY09Zhd_51b7hiRmlUBzA-u1WpBqYmCoeTXOAA2tt2l3eplGcg_rGH4NK-wqKnbCLDFe8V1tx6bfjqm4H9vO1s4IWGMBm6yO6r09mDAgYasIE9_D0_8nX8e49N1jGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز یکشنبه ۲۹ شهریور ماه در گفت‌وگو با شبکه خبری فاکس اعلام کرد که در حال تصمیم‌گیری درباره ایران است و «در آینده نزدیک اتفاقات بسیار بزرگی» درباره ایران رخ خواهد داد.
ترامپ گفت گزینه‌های فعلی روی میز شامل «محو کردن ایران»، «رها کردن آن برای فرسایش اقتصادی» یا «رسیدن به یک توافق» است.
رئیس‌جمهوری آمریکا همچنین گفت: «سؤال من این است که چه زمانی و آیا قرار است کل ایران را منفجر کنم» و افزود: «بهتر است آنها رفتار خود را اصلاح کنند.»
ترامپ گفت برای دیدار با مسعود پزشکیان در حاشیه نشست مجمع عمومی سازمان ملل متحد در این هفته نیز آمادگی دارد.
او در ادامه گفت برخی مقام‌های ایرانی پنهان شده‌اند و نمی‌توان افرادی را پیدا کرد که قادر به دستیابی به توافق باشند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78459" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DE_M7maeL0ZCOFJkuuCTQTgqtzBgFcQyuCY4bVvv75vwWi3w1oKAwcpagPkPntt40FRNZtjuU8kSUSqT4KKo5o8jdtbjT76pdSjxsN-k-MzB1RRtaJXU8egNhXMo_tqE5gS-fwrDeS0SiSwjJHbWQpywB1QP1iDbJC35SboYuBn2UQ_rET_cxrxJZqOsFuH-Vrep2pWy8wlPaRnlhDvCEutw3rxIOsGQ55Jv0OUB89Z5WiZ1QqpiJ-0hmfbX3BG4LLW_fYbYfMTLXcVY5CumcBk7thYtTkmfBeB-o3y33fQDTOo2hCLq3uBORt81I-gILN8qexFLJ2L61nGL9caDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا با انتشار بیانیه‌ای نوشت به اطلاعاتی دست یافته که با آمریکا با حمایت برخی کشورهای منطقه، برای ازسرگیری حمله به ایران آماده می‌شود.
در این بیانیه آمده است: «براساس اطلاعات دریافتی، آمریکا بار دیگر تصمیم گرفته با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران را از سر بگیرد.»
قرارگاه خاتم اطلاعات بیشتری درباره شرکت‌کنندگان و یا کشور اروپایی میزبان ارائه نکرده است.
این نهاد عالی نظامی به کشورهای منطقه هشدار داد که اگر با حمله آمریکا «همسو» شوند، «همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.»
قرارگاه مرکزی خاتم‌الانبیا همچنین به آمریکا هشدار داد در صورت حمله، «تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78458" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dq5tx7f0x5n3BrvCbHpn3TMfOn7W0hu5vlo8YpumkEnjlxqBXsgPMsslirOX3GsDSd8Gge3QI5Zdn3Xm_CGgY3BG3vb6Gcs4qJrAMWcLZI3OMiGbaGjoBuENCwh2SfmX3kaJuvyFlJLU0J0PfZ_IRecoNgXtLqIZFfW-epyYBO57ciIV8dGxCWvpIMADCgqJtjifiHSwgd8BaVoq3fdz4mMBBVlIlAoXLQySZI_jNncz5JdV2f3cG1Bsqgylvoe82Pv0eQYYJUgFLZ6-kyASXlF5Y0cA1Gnv7Lwph3TLgLTuzPk6N6WW6FHwh3_HvEGNCVKvcdyjG9QFB2cFL5ASbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی از جریان‌هایی انتقاد کرده است که با رد هرگونه تعامل و دیپلماسی، ایران را به‌سوی «فرسایش و جنگ بی‌پایان» می‌برند. او هم‌زمان تایید کرد که تهران شروط و پیام‌های خود را از طریق میانجی‌ها به آمریکا منتقل کرده است.
@
VahidHeadline
محمدباقر قالیباف روز یک‌شنبه، ۲۹ شهریورماه در نطق پیش از دستور خود گفت: «انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده... و تا زمانی که این شروط محقق نشده و حقوق حقه‌ ملت ایران به رسمیت شناخته نشود و تعهدات آمریکایی‌ها اجرا نشود، هیچ روزنه‌ای برای بازگشت به شرایط پیشین مذاکره و باز شدن تنگه‌ هرمز وجود نخواهد داشت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78457" target="_blank">📅 16:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojIZy1oYycjvHvFCirTFIqx8bPKd1afxyM8qWFs_9M2EiefNIzkLp_TwDYE9eNLfQwMti8oZEjBMQU04VZBofga30rikGCem93_YM53Am2DhxGv5I1CHBfp_VMqST23GXBj-GZlc2JjFYcgMrkCRDP_fXsVHPcKQPqtzDM6r1htOqTJipqkhctaMyUYueC9NntqmoHqQT3v1EqocmyeC5AVddkfLGcLAiWA3ZYbKYWqXeiGRK8t7uChEPfZOh8CcNHmMOAcBSL3ovP5IzV8S8OMF18wykFPQhBNaLuU0mGVMUcQ3-yXZ26_dzNfi7vxwXx6SjCBuNw11yv3-3-kvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه یک دادگاه تجدیدنظر استان البرز حکم مجموعا ۱۸ سال زندان «منوچهر بختیاری»، پدر دادخواه پویا بختیاری، از جان‌باختگان اعتراضات آبان ۱۳۹۸، را تایید کرده است.
براساس رای صادرشده، بختیاری با اتهام «تشکیل و اداره گروه در فضای مجازی با هدف برهم‌زدن امنیت کشور» به ۱۰ سال زندان، با اتهام «اجتماع و تبانی برای ارتکاب جرایم علیه امنیت کشور از طریق همکاری با یکی از گروه‌های مخالف نظام» به پنج سال زندان، با اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به دو سال و با اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس محکوم شده است.
تایید این حکم کمتر از سه هفته پس از آن صورت می‌گیرد که شعبه اول دادگاه انقلاب بندرعباس، منوچهر بختیاری را در پرونده‌ای جداگانه به ۱۰ سال زندان دیگر محکوم کرد.
در پرونده بندرعباس، او‌ با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «تحریک مردم به جنگ و کشتار» و «ارسال فیلم به شبکه‌های مجازی بیگانه» روبه‌رو شده است. این پرونده با شکایت دادستان بندرعباس تشکیل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78456" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=rbwbXmIiWNRmNtsRH-4mKQOlCokysfu_yNsAHBR6zftJ-k1dwwyPpUd9lpe7QQsgccag2flM3v4wpkyVptycHf80FvZlUgITewMT2CLf45Iug4VSzOeBdmSASRPMmNz29tjxkqf750CXNxFTt5AdkS-sVRRRPmlDeqQqyObs4NeGBDDr1rydlBsgU2FXiKTF5bz812fSh3VIWsuQlknnDLJ6INFigHeWswbsa_P8IjvHPBmPh8d3q4Nwt2hLEnh8Q8XA2QIVTXSjjpIBURVP8Lq1OjvQu1OLEs4eJauvGjKieMZ7OJrIKqkKUu_vwWX_AGC79LC85ENZnv7y5Zr4fg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=rbwbXmIiWNRmNtsRH-4mKQOlCokysfu_yNsAHBR6zftJ-k1dwwyPpUd9lpe7QQsgccag2flM3v4wpkyVptycHf80FvZlUgITewMT2CLf45Iug4VSzOeBdmSASRPMmNz29tjxkqf750CXNxFTt5AdkS-sVRRRPmlDeqQqyObs4NeGBDDr1rydlBsgU2FXiKTF5bz812fSh3VIWsuQlknnDLJ6INFigHeWswbsa_P8IjvHPBmPh8d3q4Nwt2hLEnh8Q8XA2QIVTXSjjpIBURVP8Lq1OjvQu1OLEs4eJauvGjKieMZ7OJrIKqkKUu_vwWX_AGC79LC85ENZnv7y5Zr4fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«نجمه امینی»، دانشجوی حسابداری و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در پیامی صوتی از زندان وکیل‌آباد مشهد اعلام کرده است که دادگاه انقلاب  روز ۲۵ شهریور برای او حکم اعدام صادر کرده است.
او از سازمان ملل متحد، وکلا، فعالان مدنی و نهادهای حقوق‌بشری خواسته است پرونده‌اش را بررسی کنند و برای برخورداری او از حق دادرسی عادلانه اقدام کنند.
هرانا پیش‌تر نوشته بود که او با اتهام‌های «اجتماع و تبانی» و «توهین به مقدسات و ائمه» محاکمه شده است.
نجمه امینی روز ۱۱ بهمن ۱۴۰۴، هم‌زمان با اعتراضات سراسری دی‌ماه، در پاساژ فردوسی مشهد بازداشت شد.
امینی ۲۳ ساله، دانشجوی رشته حسابداری و ساکن مشهد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78455" target="_blank">📅 15:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3x7Njq0WoZnbAoYfW7VDC_xlRdkrS6xWJWjcIHsGMwhOEiAkPQ6c00bXEWcl7SH-vrl1ozSNRTxtiCF_ZyMrOKArjpDKnWPHCOGa_cg_NBylY64mLCfU-XHPRuOdqlltFDM7vvNOP8XiU4G-sEomYGITpzifBKEgR6B41JXf85a7e4lTCuTybOw4pYUmiYSOD2OjSdSQBTex-EhylUM285K0OZdf9JFnANdP8nALk7uyMKA8-wPtgfwEJ-Nu0cMEFNkgs0ufGibDLKzc48gju8f5KO_8ix1QASlq4ybgG5262T01lc3Vq9HBc_jkNxO161gByQ09oarS5-3z5TWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی جمهوری اسلامی، شامگاه شنبه ۲۸ شهریورماه در شبکه اجتماعی ایکس نوشت ۷ شرط ایران برای آغاز «هر مذاکره‌ای» به دولت آمریکا اعلام شده است.
رضایی در این پیام نوشت: «پیام تهران روشن و بدون ابهام است؛ اگر واشنگتن می‌خواهد از مخمصه‌ای که خود ساخته خارج شود و بیش از این در آن گرفتار نشود، راهی جز پذیرش حقوق و شروط ایران ندارد.»
ساعاتی پیش از انتشار این پیام، رسانه‌های دولتی ایران به نقل از گفتگوی محسن رضایی با شبکه الجزیر گزارش کردند، ارتباط میان تهران و واشنگتن به وسیله میانجی‌گران قطری و پاکستانی ادامه دارد و شروط تهران برای بازگشت به مذاکرات به کاخ سفید اعلام شده است.
رضایی با اعلام آنکه تهران منتظر پاسخ واشنگتن است گفته بود، پایان دادن به جنگ در همه جبهه‌ها، آزادسازی دارایی‌های مسدود شده ایران و پایان محاصره دریایی شروط ایران برای آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78454" target="_blank">📅 23:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BRj2PcUt4cO0LMAaJ_f52QaD7FTS-Kdrhe1-LFsx597f4yieWPSb549xVs0RoHNL74IQWiSu0gu3y9zQtkgnnP0t2vEatE8Ely3xkKT97APU2kUJajmEQeFnrq-VshF0uoovjJIfLKbSFn4EY476mVM_669UafRnL5PcJNT-U3XY2c_zVr4zMeYM8xtWxx9eHexISpCrjJsMxVjc4H0v8OxJsh49Sgl9GzQ32cKUYFc8EQkPJjjqIheFv8bNX9YJSohSQEsMR_PaxsutLyaY6jeFv6bIJyv1PZ7iOl82-yLwk6U5l4jHTBVUl4jSrUk5Y5rbS_DROzAnyVzI7kNVgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاکان فیدان، وزیر خارجه ترکیه، گفت در پی حملات حوثی‌ها، عربستان سعودی ممکن است در برخی زمینه‌های فنی نیازهای نظامی داشته باشد و ترکیه برای پاسخ به این نیازها در چارچوب «ائتلاف دفاعی مکه» با عربستان سعودی و پاکستان مشکلی ندارد.
فیدان شنبه ۲۸ شهریور در گفت‌وگو با شبکه «ان‌تی‌وی ترکیه» گفت حملات به تمامیت ارضی و حاکمیت عربستان سعودی جدی است و ترکیه در چارچوب توافق میان سه کشور در کنار عربستان سعودی قرار دارد.
او همچنین گفت عربستان سعودی تمایلی به ورود به جنگ آمریکا و جمهوری اسلامی ندارد و کشاندن این کشور به این درگیری «غیرقابل قبول» است.
فیدان در پاسخ به پرسشی درباره ارزیابی برخی منابع اسرائیلی و ایرانی مبنی بر اینکه «ائتلاف مکه» تنها روی کاغذ است، گفت: «ما به این حرف‌ها می‌خندیم. ائتلاف مکه به یک سازوکار بسیار تاثیرگذار و تغییردهنده معادلات تبدیل خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78453" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/205953bb15.mp4?token=CxZovaiybIbhrPUugR9fJp25edqZjneJMgLh8yuNr3SjEgj5-JqrukJ_Puxx0LV6k521x0D0ZN-cZSpwRm6-eC0nlGUa0zE6_hsZtRd2Gqs1wFantKfLtNx84rRIsfuUBdnBfYfDb_03cs95VvMDGHqvpsKpYtxTb2DaS9Gjrsm-lj2f-sh4pWVNBSkcTTCM8p5zifickU5RQ1BVC-82WAcEVIbwalorbFhBb2Slnq2SV7Z-aekK3c1n4-9GAwpzREvhUOJ-8E9zphq01nhQDbU0Iw4Nj3L4v9kU3e8PgfzRo1BOueTcR5csyOQ0wnH1y6CdNlGIVbpqj90tzlqOOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/205953bb15.mp4?token=CxZovaiybIbhrPUugR9fJp25edqZjneJMgLh8yuNr3SjEgj5-JqrukJ_Puxx0LV6k521x0D0ZN-cZSpwRm6-eC0nlGUa0zE6_hsZtRd2Gqs1wFantKfLtNx84rRIsfuUBdnBfYfDb_03cs95VvMDGHqvpsKpYtxTb2DaS9Gjrsm-lj2f-sh4pWVNBSkcTTCM8p5zifickU5RQ1BVC-82WAcEVIbwalorbFhBb2Slnq2SV7Z-aekK3c1n4-9GAwpzREvhUOJ-8E9zphq01nhQDbU0Iw4Nj3L4v9kU3e8PgfzRo1BOueTcR5csyOQ0wnH1y6CdNlGIVbpqj90tzlqOOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، روز شنبه ۲۸ شهریور، در پیامی ویدیویی خطاب به شرکت‌کنندگان در «مجمع گفتگوی جهانی ۲۰۲۶» به میزبانی انجمن سیاست خارجی اندونزی، با انتقاد از رویکردهای مداخله‌جویانه در خاورمیانه تاکید کرد که دهه‌ها حضور و فشار نظامی نه‌تنها کمکی به ثبات نکرده، بلکه چرخه‌ای بی‌پایان از تنش را رقم زده است.
عراقچی گفت، ریشه بحران‌های منطقه را باید در یک حقیقت تلخ جست‌وجو کرد؛ چرا که سال‌ها مداخله خارجی، فشارهای همه‌جانبه نظامی و درگیری‌های پی‌درپی اثبات کرده است که مداخله نظامی امنیت نمی‌آفریند و اعمال فشار و زورگویی هرگز به صلح ختم نمی‌شود.
عراقچی در ادامه این سخنرانی ویدیویی خاطرنشان کرد که در شرایط کنونی، جنگ به‌جای آنکه آخرین راه‌حل باشد، عملا به ابزاری معمول در روابط بین‌الملل تبدیل شده است. رویکردی که نتیجه‌ای جز عادی‌سازی خشونت و تداوم الگوی درگیری و تقابل دائمی در منطقه به همراه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78452" target="_blank">📅 16:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvdi_c_QuezErjDqAr2cOwCF2uYfCScuBA2UMxdjGrCrB_1SMB8dxqidsfFMD9cxPwjS1sy6xBC7Lfb7qSy3fO7-GO6I_IXF8e4s6unegwt4TReNTndy7Vmo3q9btOHehB4aZOTvwVMyAx_lshmwWjJQ6KQVT133mxZroO5MJWKL6phy2bOYoXgDUK6vUw34XroPQ4J4ik8FebDcmACnjVCsmxhPGzAv1cVl9erQQmC0sBOc2GqlJFZ5hsVUyOw0V9Lm3zTH4XPjmeMCBMG2NWbozvYqgmr2y1lVbkSY_TEbbIo_VmcRmEqBexReHPRpSYOV3zWG0gKMET0ETbzv1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است. دادستانی مدعی است که در این رقابت «موازین قانونی و شرعی رعایت نشده بود».
مسابقه دو ۱۰ کیلومتری بامداد جمعه ۲۷ شهریور با حضور زنان و مردان برگزار شد. انتشار تصاویر شماری از شرکت‌کنندگان زن بدون حجاب، رقابت را به موضوع بحث در شبکه‌های اجتماعی تبدیل کرد.
بنابر گزارش خبرگزاری فارس، برگزارکنندگان اعلام کرده‌اند مسابقه با مجوز وزارت کشور و هیئت دوومیدانی استان تهران انجام شده است.
هیئت دوومیدانی تهران گفته پیش از آغاز رقابت از شرکت‌کنندگان تعهد کتبی برای رعایت «حجاب و شئونات اسلامی» گرفته شده بود.
حبیب ستوده‌نژاد، مدیرکل ورزش استان تهران، به خبرگزاری تسنیم گفت مجوز رویداد از شورای تأمین استان صادر شده بود و با ورزشکارانی که «خاطی» شناخته شوند برخورد قانونی و انضباطی می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78451" target="_blank">📅 16:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx5D4zxCl-FbQ7ogzPpkuB4-L2ErcbKuN2MirGb0p0DzV-Ls8tgK3TmpuoCLuCm95A7srpo5h2SlLLmCUe-SFa5okdXXKGVzD_pyIoAhJ1ArToiQwsUNtaw8oHvo44hoYcikUXwZyPcJ_9GN7IX3olRshvSg4H4LdBvZrAkWc6F4XUrGYroMrIduUcP_AKeo2vEKk5nNgKoE1kuQqVML_7Jbi-DCR5FcM83aYFf0Dd8H00esdHUZAB3oooxjz8iZEw_4xZ-VDanEomkllbRsZDCmTiPV-dnLpUlGStT2c98-ygOQQF1oanamN1uHftN0jLTEPVWDPoztYjMHX1u4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد تنظیم مقررات و نظارت بانکی ترکیه مجوز فعالیت شعبه «بانک ملت» ایران در استانبول را لغو کرده است؛ تصمیمی که پس از توقف پروازهای شرکت هواپیمایی ماهان میان ایران و ترکیه و مداخله نهاد ناظر در مدیریت یک بانک تحریم‌شده دیگر اتخاذ می‌شود.
براساس اطلاعیه منتشر شده در روزنامه رسمی ترکیه، هیات نظارت بانکی این کشور روز جمعه ۲۷ شهریور ۱۴۰۵ لغو مجوز «شعبه مرکزی ترکیه بانک ملت مستقر در استانبول» را تصویب کرده است. این تصمیم روز شنبه ۲۸ شهریور در روزنامه رسمی ترکیه منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78450" target="_blank">📅 16:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNkBnYcrEI53nhTZxwKeok3rENNRcECrnlBXafl-iExqVks5naIUnXwFXTo5TNDV235IVCtibSWYGjl58ohyKHE8EG-rLZlcHlWNBcIwnjq9BbP5Sjsueh7y30Z-MQ08RC2ea7MTj-0YqximcEGOnjSIk-1RfHrlTdUC9WO-kr3SgA6qmpNiD-yKpEWfEz2ZLyFVbHj_ozwBZDtDcqT3C0ountlWgyS0W9qBj2LQUiQhajQN3ACEYX-86q4NOhyT4XoRbOAKtZakWIpWsdbo5otBTsuTY27KNAgszqgEzDCK5dROxj11lcGgOqLWglJdGULLz8Tn_uW95GWVZyPKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز جمعه ۲۷ شهریور و اندکی پس از تایید کنگره در هفته جاری، لایحه‌ای را امضا کرد که مجوز اعمال تحریم‌های جدیدی را برای تحت فشار قرار دادن روسیه بر سر جنگ در اوکراین صادر می‌کند.
این قانون همچنین تحریم‌های مرتبط با ایران را نیز تمدید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78449" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LShePYWKPet7U84zM46JkTmTiNCgqU3EJIE0R1pnoF6iopdFlV1sxi6XfdCwALPBC3DsnRXi8MTNh1i7-JY_anu74fhuWdjb-IcTVzwq8v4jrq94LPic0tdtZTmF56rYcq2plYo5lpvL_DtvQZrGE6ekJhasnQ1g6m1FE-IX2TbOqHA5z4DxKtEQqdlOWkUDwHYe_jeS3LjAfIInak5n0DEu65jiPp4I6yxbn2tyURf_csJBjo-JXVSFLlU5682TYndeZ3EjqOxWhkdBI5CFaeaR31zZMuodZZ-yrpeaEvbjjPMZE4J52r-Bn4xLc2Jz7lbVx903D72SoXnB0roxZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اعدام «حسین پدران» با اتهام «جاسوسی و همکاری اطلاعاتی به نفع اسرائیل» خبر داده است.
براساس گزارش رسانه‌های حکومتی در روز شنبه ۲۸ شهریور ۱۴۰۵، حکم اعدام پدران پس از رد فرجام‌خواهی و تایید در دیوان عالی کشور اجرا شده است. محل و زمان دقیق اجرای حکم اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78448" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEblbWWan9gJtpIGzureLNSB95epM1y8S636fZ6wZaa43t75S-MdgDAm956SJQxs4sxGIySVzLzamwF3NfOT7zGyL70pXQitGoVGI-KGhRaTZBjSjQifgDfsYX5e5DwcbbXDEgn-5YuyuDKGjLAoiVKgX_hnYMVtrQPTIrnCNrYKVZEX1OAFM4z-D27Y78DWtSm8igLUOj2SoEm0IOyAdjukGQjoHar7A1_J3vdmDJq_86bj2Vo2zBa4gIVSaRsbJU9zhjOSapTe6C_9pAhPJxaBOoPnyov7LIVCsAjNBMpO1nLsUbB8ztIp4MkscjUp0Le7JQweKDNsTKVxIP577g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌سوشال اعلام کرد آمریکا با دانمارک و گرینلند به توافقی دست یافته است که کنترل دایمی امنیت و تمامی نیازهای دیگر در گرینلند را در اختیار آمریکا قرار می‌دهد و به تمامی نگرانی‌های متعدد ایالات‌متحده رسیدگی می‌کند. او گفت این توافق هیچ هزینه‌ای برای آمریکا نخواهد داشت.
دفتر نخست‌وزیری دانمارک نیز اعلام کرد انتظار می‌رود که گرینلند، دانمارک و آمریکا هفته آینده توافقی را برای تقویت امنیت در منطقه قطب شمال و اقیانوس اطلس شمالی امضا کنند.
ترامپ گفت: «از این پس هیچ دشمنی از سوی آمریکا نمی‌تواند بدون تایید کتبی صریح ما در گرینلند پایگاه ایجاد کند، حضور نظامی داشته باشد یا سرمایه‌گذاری‌های حساس انجام دهد.»
پیت هگست، وزیر جنگ آمریکا، نیز گفت: «ما بلافاصله روند حضور نظامی گسترده در بخش مناسبی از گرینلند را آغاز خواهیم کرد؛ بخش‌های مناسب زیادی برای این منظور وجود دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78447" target="_blank">📅 04:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=Z4BE4RmBh9L2xlmplTn4f65EXl41hkMWf5Wi_IEh3JIj8rJxw4pqCkv0xtelpUPfmrZbKM6YLMrgZLejTwEsfKu_uRnXbUy9ujqOZqp-fwWXqquaE74d9iRGg0IxKTz4VJnSG9zrkL2EZjygFT8PfE634KMS_vdU5K5mPeQC94TD87OFArptKFBy4BzZ8I9wUrbqfIIAgDiWcZth46uLrkbI1LhC2VvYhiLQ24fspe4ByVhn5bEBMWQYbiWlwYnWLVTqadGxBTZfi4zYNrJDf2ZFrFNh3c92dYxdy5VG-HM3jw4-vxX4dlHZnQes1d_cd2oZFT1MGVQMEtD5ZlyhIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=Z4BE4RmBh9L2xlmplTn4f65EXl41hkMWf5Wi_IEh3JIj8rJxw4pqCkv0xtelpUPfmrZbKM6YLMrgZLejTwEsfKu_uRnXbUy9ujqOZqp-fwWXqquaE74d9iRGg0IxKTz4VJnSG9zrkL2EZjygFT8PfE634KMS_vdU5K5mPeQC94TD87OFArptKFBy4BzZ8I9wUrbqfIIAgDiWcZth46uLrkbI1LhC2VvYhiLQ24fspe4ByVhn5bEBMWQYbiWlwYnWLVTqadGxBTZfi4zYNrJDf2ZFrFNh3c92dYxdy5VG-HM3jw4-vxX4dlHZnQes1d_cd2oZFT1MGVQMEtD5ZlyhIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۲۷ شهریور در گفتگو با خبرنگاران در کاخ سفید گفت جلوگیری از دستیابی ایران به سلاح هسته‌ای موضوعی است که به آن «بسیار افتخار» می‌کند و ایران دیگر سلاح هسته‌ای نخواهد داشت.
ترامپ با اشاره به افزایش هزینه سوخت گفت تحقق این هدف ممکن است مستلزم آن باشد که مردم برای مدتی هزینه بیشتری بپردازند.
او افزود: «اگر مردم می‌توانستند بین قیمت پایین‌تر بنزین و اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی بدهند، فکر می‌کنم نتیجه با اختلاف بسیار زیادی روشن بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.»
رئیس‌جمهوری آمریکا همچنین گفت انتظار دارد جنگ با ایران «به‌زودی» پایان یابد و پیش‌بینی کرد پس از پایان جنگ، قیمت بنزین به سطح پیش از درگیری بازگردد و «شاید حتی پایین‌تر» برود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78446" target="_blank">📅 04:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=PXOMKgGkOGXKNhTUwu1CixxNT0zEahIyptDbkBAsUg0CtVqTeA6i_YXKSkUxL4brUTHpMrxZEk3OF2giGhEwz6ORPFVJypaARsf0-aAVRRaAD1d1yYOjU7bn8Pm6A7jpKYkOfjDADalgJ6hDb_087wyP7Efd0dqOduoJN737xxfosehdEvlmQb1qb3Rmvzks5d4S50nEEqEUrQsJd1UkrDQ97QBLmIc5y_sUSQ8esfeuZ0zDlUzgtfyc7McnUwXiguyYdDbE-LpESQZNq4MrpwEfz70y1w5KqWzZtMFbyogl0SX4l8xKx2-012LFGTMOLW81gkg-4-uQlbdb0Zjp4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=PXOMKgGkOGXKNhTUwu1CixxNT0zEahIyptDbkBAsUg0CtVqTeA6i_YXKSkUxL4brUTHpMrxZEk3OF2giGhEwz6ORPFVJypaARsf0-aAVRRaAD1d1yYOjU7bn8Pm6A7jpKYkOfjDADalgJ6hDb_087wyP7Efd0dqOduoJN737xxfosehdEvlmQb1qb3Rmvzks5d4S50nEEqEUrQsJd1UkrDQ97QBLmIc5y_sUSQ8esfeuZ0zDlUzgtfyc7McnUwXiguyYdDbE-LpESQZNq4MrpwEfz70y1w5KqWzZtMFbyogl0SX4l8xKx2-012LFGTMOLW81gkg-4-uQlbdb0Zjp4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با برگزاری
رزمایش "جان‌فدایان"
تصاویر بالا رو هم تولید کردند:
مسابقه دوی ۱۰ کیلومتر تهران روز جمعه ۲۷ شهریور با حضور گسترده زنان برگزار شد.
در تصاویر منتشرشده از این رویداد، زنان با پوشش‌های متنوع و اختیاری[تر از قبل] دیده می‌شوند.
رقابت امروز در «بوستان ولایت» و در دو بخش جداگان زنان و مردان انجام شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78444" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J2gLXC2PFGdgx0vOJ0aDRz7dYmXBI6-Z7psI844Od3HrDZkGUX9M_gSuPA9evavFWOcvT6MyeMjIbZd77byerd1ZPftxpH2JE9FYvO4LaC6NREMGYko3U5USWTYan4IVkvJm7XIPu7Q39r4-ArOMNz__OgWn8A7Th-uTHaSBv8foi_LZ5I_CV6_82tWmmrLNIHEjf3TvDOlqL7TqMcfV53yopkTJRw0WkdkQ7PV85PNZuPytT1_A0vovqVzrrEGfHMEGviANbO5HYBKOkWfyKWvLpuXdIfd3XG1DpI0Cb7p8TOeez5yK1hojm9AHIt2alLiaIOPDgfXM_Je8zQzdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nyVnbjxx1AIt9wA2L93vaquIERVBwMMoX91qLAicxT40Cf8ft5eXtXb8ynhMCIpYCBc81Y03TaXOSOpYzN7DGOusJRsoII1r8nvE5IqaSSwZEADr4J5f1WsKmdUt6XAt2XjunWEgxDkcsEM65_yVSJI14-lXrb1hPXUuh1COrnHphwOOuddzqEaIfhTdKJ9hFgb37HVDjRvZk9zxqXeuIRd8DSglrSiTDzdx1Kx-RhNJfZwtu8T9G7lBQ_gu-LFudG1X1I8nHAO4QeTf3UDBMB7PNz1fMHgulPt8uh8s6B6bCCSSrt2-S0QqDg2FMdoOr6q5M1mmzJY-_wLHBIuM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BsXj7Lgth2qK6IQL89gGON96XeAjsU7kM8Krp72JfN3rIWEhA3clzBU8sAABzLC9gY-K3alfBKOEnza9dFcqYQjByenJg_xQVQNVbvdsMxsT3mMLzNzSEzJcvxpVgiVAuR6xYE3QJ0c9fVJc9-7UKeJsBNxlC84YYo4GUemrToBZOVoTar3UKYP-UTjoMuYIS69c91T5SiHQ1C8TSSdu2jWT7YMqvjcuy4wYzToqoTM6QhOKM8WffZjLcyn1jFGBNVtGy2pIFZz0flfvKHLD4JJfi_vgiOZvuAJrQIha1byVkmbqVXjRaNRDYDDHc3k00xHwdQyEsXoVrGTw3VpT2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q6aUhMrLwPG1awzR-pmL900m8NiF5WY-zqvkSC0etdU-th223TZ_P1eH0rVCGjU4ngyAmiJMzL_fizUgdMVj1lIHTfOWLiMizEhcXmjuQTKttllX6-PI2p4UXXpIh4RwaEKEKzxmSMI_KkT7HSJCY9lNnBz4j6Egcl8k-AO82WnNKFB474OZqLKkSaG-xeGMQ-SnTnSXvD9h68Vw47fNqeKq0BFko1eArFrZscUIRDlGPCE8XGBfZYl0LAoz_eH9QOavuqKVV9r5Uwt-LfIyal3f7qBHBQXipL3Db8xNc_jWJM5JuFUlNywAiN3STNMUZF37UedDdU0PM4ZsIkFUUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ym0JmfenUvM7Htj24IAMfT-jAbtRwAZArKKEHfDoPctPx3-mEG9fQN_scC_YO4FftZG55xtGFfw8dMzW-DoT_fATm07SOp_gyvsT5LbWJieORfyUpfujogQtCwvWSWo8veSn7qB_eTUKN_AGd6clAR4D3xIrRlu-MlGa_vm8Nc4d7RLJS2w5JQKmGUej2hvdka52biZlaLUFhGx0Oam7t8ohGJ-cY-IuR3uVqdZsFiZFV232nTtuUun3ZrDLJa47oXv694B99uN6A_FJN-H6nWL3TUf5zFB6PBGlYUZ8h2yaET79CCwtnMAGPwX_u1fS6CcOaS37zd2P5WDodu2bbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=DjM2YEow3GTIeE_vh-2wc6eY4-xaB-fx4eOi2k_2u0DyUTyuq9RluknG_otl5rYFyYZWOERdPrTvUksBS344i8f4ZWG76zQQDs8XboAxDMJ-ImsHEgUQuzsLBZhAJqlNyvK2Jr4MBEZWq7ZoaVCVqYw6Gz9TjzMNib8W5bWEDlYTQtZUWohM0-jTJuB_Ykn69EIMrLyhD62h7r1jJnzsYCFcK1UIi1AEkemWAEatqDIMRNylREr8_AhpYD-D-G7r3sw9RAiLsEzx03-eG9SZ-Oq5NkWVGC3C-tHoHDRWZfjBwT969d0DeIPinUdkMEo-iszPY5wD3zmGjR10bpjfpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=DjM2YEow3GTIeE_vh-2wc6eY4-xaB-fx4eOi2k_2u0DyUTyuq9RluknG_otl5rYFyYZWOERdPrTvUksBS344i8f4ZWG76zQQDs8XboAxDMJ-ImsHEgUQuzsLBZhAJqlNyvK2Jr4MBEZWq7ZoaVCVqYw6Gz9TjzMNib8W5bWEDlYTQtZUWohM0-jTJuB_Ykn69EIMrLyhD62h7r1jJnzsYCFcK1UIi1AEkemWAEatqDIMRNylREr8_AhpYD-D-G7r3sw9RAiLsEzx03-eG9SZ-Oq5NkWVGC3C-tHoHDRWZfjBwT969d0DeIPinUdkMEo-iszPY5wD3zmGjR10bpjfpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین طائب، رئیس سازمان بسیج مستضعفین، اعلام کرد صدها هزار نفر از ثبت‌نام‌کنندگان پویش حکومتی «جان‌فدا» در تهران سازماندهی شده‌اند و روند الحاق آنها به گردان‌ها و یگان‌های دفاعی جمهوری اسلامی آغاز شده است.
طائب روز جمعه ۲۷ شهریور در جریان رزمایش موسوم به «۳۱۳ هزار نفری جان‌فدایان ایران» در تهران گفت برای این افراد دوره‌های آموزشی مقدماتی و تکمیلی در حوزه‌های زمینی، هوایی و دریایی در نظر گرفته شده است.
این رزمایش از صبح جمعه در مسیر میدان امام حسین تا میدان انقلاب تهران برگزار شد.
@
VahidHeadline
حسین طائب، رییس سازمان بسیج، جمعه ۲۷ شهریور در همایش «جانفدایان ایران» اعلام کرد نیروهای آمریکایی «به‌زودی با شکست از منطقه خارج خواهند شد.»
رییس سازمان بسیج گفت: «جمهوری اسلامی از تمام ظرفیت‌های راهبردی و تنگه‌های دفاعی خود، از جمله تنگه هرمز، با قاطعیت حراست کرده و دشمن را وادار به تسلیم خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78434" target="_blank">📅 16:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMBQ8MZ1idms_As1eFlGWfRAACrZrkji5czp9pQaSGvjxpltNPgG-5TgATs5OWzYh_32sfKV7EFQUiMtqO6NsvLOMMnLuZRX7s_lbGlozeAuyGfdddJ1ATX0VxkMpF_9p1hnSrq4gNmMN8c4ierkl65KyQwJbLxFpMfow4OU1cw27DkZzxb4MAc6XaQf8m6gin0RgbEGBh0_gDT6g83PGXDN5p27gjPDEMmBw-zkmI0mSv7DLejRf_LdBDyc1uAFrBfq9CQxJWhV1C5QicYxwJ5wmzb4X6ab00bTKM8Cv9gbK1qhNstbvypdW2Etp6Ud-QY4_MK8Pxsr9tT_goLNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کره جنوبی اعزام نیرو یا تجهیزات نظامی به خاورمیانه را در صورتی که به مشارکت سئول در جنگ منجر شود رد کرد، اما گفت کشورش ممکن است برای حفاظت از کشتیرانی تجاری و انتقال نفت در منطقه نقش بیشتری بر عهده بگیرد.
لی جائه میونگ روز جمعه ۲۷ شهریور در یک نشست خبری گفت: «هیچ اعزامی که به ورود یا مشارکت در جنگ منجر شود، انجام نخواهد شد.» او تأکید کرد کره جنوبی برای چنین هدفی «به هیچ شکلی» تجهیزات نظامی اعزام نخواهد کرد.
او در عین حال گفت سئول باید مانند دیگر کشورها «حداقل اقدامات لازم» را برای حفاظت از کشتی‌های تجاری، انتقال نفت خام و امنیت شهروندان خود انجام دهد.
دولت کره جنوبی در هفته‌های اخیر در حال بررسی احتمال اعزام نیرو یا تجهیزات نظامی برای کمک به تأمین امنیت کشتیرانی در تنگه هرمز بود.
دونالد ترامپ، رئیس‌جمهور آمریکا، از سئول به دلیل آنچه حمایت ناکافی از تلاش‌های آمریکا در ارتباط با جنگ ایران خوانده، انتقاد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78433" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LxcS_3LWCC70e3Rx9ASM22_s7FJ2mpDjFFJMpjrpmM7Z3RLw5-EngVnvchW4edfoAcH7UrtTgwmD0emNRt2SY0QMzruuOYNoMa_qMe2_dOUhAbut_QukxQGd03jz7nHryxh2JfGfNzUuNeFlqIhf44Wybvv-uUMoVK4JEjPP54ogKZ2MlfMe-lFkUobyIkXjDGG6xbLrMatYy_2AtJohDDA9TpzBnPhmhdzzmKkOjhZOc9lAenHsuI904-JzVRFNZJDFmuUPiHRlHO_vgazsXluAul5nPJhb1BZRODAcseoRJGQmsYThmhGeXCf23XkjX69V3UC4sSiYpfDMUW9-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد یک نفتکش با پرچم توگو را هنگام عبور از تنگه هرمز هدف قرار داده و مدعی شد این شناور پس از اصابت و آتش‌سوزی متوقف شده است.
@
VahidHeadline
UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت (CSO) یک شناور گزارش داده است که یک نفتکش با پرتابه‌ای ناشناس مورد اصابت قرار گرفته و این برخورد باعث آتش‌سوزی در عرشه شده که اکنون مهار و خاموش شده است.
گزارش شده که همه خدمه در سلامت هستند و در حال حاضر تأثیرات زیست‌محیطی این حادثه تأیید نشده است.
UK_MTO
در گزارشی دیگر نوشتند:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) یک گزارش تأییدشده اما با تأخیر زمانی درباره حادثه‌ای دریافت کرده است که در ۱۶ سپتامبر ۲۰۲۶ رخ داده و طی آن یک نفتکش هنگام خروج از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
گزارش شده که خدمه در سلامت هستند. گزارشی درباره ارزیابی خسارات و تأثیرات زیست‌محیطی منتشر نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78432" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWnUDSz88P-6x5A7gmusIWM6uDda56a9SlZoL4qPvawD8-dzpQBuRkPPqIWb9YFK_YPpoFWbXGzmg1rh43TywYvOY1kOmySBQo3IZWxMcojBU9cKH7ZNpvJCZ-_sDubxiHnIJbWjVv0ZlIWMKCDp4I7MsGGObbJfJfGIxWej57sB8WbrNESo27jdS8IZYZVOYTnCrfgvr4YB57sdIuDjNA_kEmi217lK_DtnvuaHAGbdUb2xSTx4SxXqy-Cyu02RG9EzZ1gbLzwZ6uLRT34wsqY9f_RMSAPpYj_1BI5WzpCDMAkIdiA6j032R7VzNwLLWtakwrGLK40sqtUHj-HPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد کرمی‌اسد، جانشین پلیس راهور فراجا از جان‌باختن بیش از ۱۶۰۹ نفر در تصادفات جاده‌های برون‌شهری در شهریورماه خبر داد.
به گفته این مقام فراجا، این آمار به‌طور میانگین به بیش از ۵۰ نفر در روز می‌رسد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78431" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VfXbbUQkXTFwozcz9ys98NpbuLfeYSd2_TTgpkuP87tZlIgRutcsTpLzs-w_0FfhRz_VJpauCIuA03p_PU6km4s3kvVBUomNnmul-m49M3YM545FaaFxmstpu7r_IeNYtUyMQFODSw8TDi3VNc23CLcZ8UtIEFJCQMkvsfnlsXoCtVunVUGNR-xB_pqNtp9ien82KgHGbsjJexZQM6whzpoOL3tXiG4INsimDSV9E76Gm5nFhtF2DReX48qtmHiS6E9M6DxcRO6csEy0BnfKuv3PDZEBjVAGO6xyF8mwXLy1NHBrEZmOr59CDL-oqOQkRYrgHPowmNesGm_Qqy30NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=kwB0WBi_zqkYL3MWLuq6zfb1HrHXvOIelpNDupzA_Rq2_9IcnakkCS7p32Uj2BfF6RV1lTQ8Wxuqp1xCJXuYCMJGp8tUMDFSRxbIn1AVsosRDCMJcmpXHLVqsIDMBdNb0nZ7hT2vtPW4Fa1zNHmD7nZAdiMYN7eIS0P5DsB8m6VlkQ0K0Ms2xPwKGGku0dspmJkU8YAXD955lWGlKcTcB9OSgOCZ6IpkZnIOhJEEGej3Zzv6u7gWL_LRH60uDhNPY6L6i1UZZlKd7Nz86FJDFIWwcgvjL8kWnt3OEsjpURou9V7yWxwJzSiPmfjtBh4uTK2piOpj_x_Wh4RT5QVNGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=kwB0WBi_zqkYL3MWLuq6zfb1HrHXvOIelpNDupzA_Rq2_9IcnakkCS7p32Uj2BfF6RV1lTQ8Wxuqp1xCJXuYCMJGp8tUMDFSRxbIn1AVsosRDCMJcmpXHLVqsIDMBdNb0nZ7hT2vtPW4Fa1zNHmD7nZAdiMYN7eIS0P5DsB8m6VlkQ0K0Ms2xPwKGGku0dspmJkU8YAXD955lWGlKcTcB9OSgOCZ6IpkZnIOhJEEGej3Zzv6u7gWL_LRH60uDhNPY6L6i1UZZlKd7Nz86FJDFIWwcgvjL8kWnt3OEsjpURou9V7yWxwJzSiPmfjtBh4uTK2piOpj_x_Wh4RT5QVNGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با انتشار ویدئوها و تصاویر مختلفی در شبکه‌های اجتماعی از وقوع درگیری مسلحانه در بامداد جمعه ۲۷ شهریور در شهر زاهدان، خبرگزاری برنا از کشته شدن یک مأمور نیروی انتظامی در این درگیری خبر داد.
ساعتی بعد خبرگزاری فارس اعلام کرد که در جریان این درگیری دو نفر از مهاجمان کشته شدند و یک نفر از آن‌ها دستگیر شده است.
وب‌سایت «حال‌وش» هم که اخبار سیستان و بلوچستان را منتشر می‌کند، می‌گوید از حوالی ساعت ۳۰ دقیقه بامداد جمعه در محدوده خیابان دانشگاه و اطراف خیابان دانشجو زاهدان به مدت دو ساعت تیراندازی رگباری رخ داد و سرنشینان یک خودرو پژو ۴۰۵ هدف حمله قرار گرفتند.
این رسانه به نقل از منابع خود همچنین افزود در این درگیری «یک فرد مسلح، سه نیروی نظامی و دو زن رهگذر مجروح شدند و چندین آمبولانس به محدوده خیابان دانشگاه و اطراف خیابان دانشجو اعزام و در برخی خیابان‌ها ایست‌های بازرسی برپا شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78426" target="_blank">📅 06:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GduHUD6ozjgY7I30303EGgqmetbz2_0IhMmZrZcFg75xoa7emjo_A-GUPsFqDMMwss5kqsRWdkmdz-iEIqp66RIox-KWsgCbMnyDOcHBPHyxeEQgNRlWZv_XkJ-YDgM3VbGqJLEh78Lb9Yx531D1qpfvazeQ2ypMm82q7hYncq6XOGmV9QxTd6sN66szZeAumlNZBt1cleDlla8N6IIL5zez0mi_a1eatF2UKw0it6Xd1UURPZASIhzZEZJx_5vyhjiruEHbniLKP8s60q8by3Gr68e4SZbJHvGsv5YwGtdDRU_FtpH1qymm3lIv4m_akP6wwmS9lOJTdpGDBaT0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران بامداد جمعه ۲۷ شهریور در بیانیه‌ای اعلام کرد نفتکش «ترند» با پرچم کشور توگو، شب گذشته هنگام تلاش برای عبور از تنگه هرمز هدف قرار گرفته و پس از آتش‌سوزی متوقف شده است.
سپاه پاسداران در این بیانیه گفت که این نفتکش قصد «عبور غیرقانونی» از این آبراه بین‌المللی را داشته و هشدار داده است شناورهایی که به این شکل عبور کنند، با «نابودی» روبه‌رو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78425" target="_blank">📅 02:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g25DkdONs9r5ZgHTVA2DjMItmIkExHy3XL96Ep_N2hNmQ6nPbIwYfC-5bvgFsPwvz-ck1ppD685JxLKtA22a4S-NzMgjEN4PkdMejs752sAayVPOHq7u1A25xPaZoqAmeNCa8N77KfgNO2-m3L0c5c7L8mhRxFjjOsPviJABqSlNemtkSLbysbLkPE7Ch2p8cgOSzsN16DOp0uXF7np1U1oNAYYVK8-XLK7_UzZEy4Dew4j5aos0XbaiBU_NqHW38UWLZpfmzIplNf9CgiHZQmK64GIFF5VxP0xNjMuPt54lvbFo0O60R0ObjMXIUhEuPMLDsIYkO5Aow5_o9FwQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصبِ عمان، دریافت کرده است. گزارش شده که خدمه در سلامت هستند. تا زمان انتشار این گزارش، هیچ پیامد زیست‌محیطی تأیید نشده است. مقامات در حال تحقیق هستند.
به شناورها توصیه می‌شود با احتیاط تردد کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78424" target="_blank">📅 23:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kc0NghXDd5GbmO9BgaAGBE-NxNM9DRrM8c1yAoDRqDRpKmMVHPJ-UzXN_dxaTPircOhonkFbJT3rOv9Hr6HnSuQ6EIDmUnoHq8n013-fATXcj3FjSlglUvIJ4qnhWyJ4feOhCb0sG4Ye3YQz8w35k_bR_ERL56vtoZQaqyp7eC7Zw-YtYUvGpXV5YA3N_O_j-SslDETzMPfxnEit92vUdyVaykxHFxjExbm3mIyiNL21jI8Cq5esF0UiwZgbRKoRc1eyjVItUlkiZHvLFQGdqaFHJ9yWxRF_3UgKRvrCYAvGyT45STahflSJnmkGwMX4cyH81Xv604EB-45_cWtHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس می‌گوید در جنگ ایران به یک دوراهی بزرگ نزدیک می‌شود
ترجمه ماشین:
رئیس‌جمهور ترامپ روز پنج‌شنبه به اکسیوس گفت که در جنگ ایران به نقطه‌ای حساس نزدیک می‌شود و باید تصمیم بگیرد آیا برای پایان دادن به درگیری، حملات گسترده را از سر بگیرد یا نه.
▪️
«تصمیم بزرگی پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر اتفاقی ممکن است برای من بیفتد.»
چرا مهم است:
اگرچه ترامپ پیش از این نیز تهدیدهای مشابهی مطرح کرده، اظهارات تازه او در آستانه دیداری برنامه‌ریزی‌شده در روز سه‌شنبه با رهبران شش کشور خلیج فارس در حاشیه مجمع عمومی سازمان ملل متحد در نیویورک بیان شده است.
▪️
این دیدار می‌تواند مرحله بعدی جنگ را شکل دهد، از جمله اینکه آیا بار دیگر برای دیپلماسی تلاش شود یا اقدامات نظامی تشدید شود. اگر ترامپ بخواهد عملیات رزمی گسترده را از سر بگیرد، به همراهی متحدان منطقه‌ای خود نیاز خواهد داشت.
▪️
رئیس‌جمهور در روزهای اخیر چند بار گفته است که جنگ به‌زودی پایان خواهد یافت. برخی مقام‌های آمریکایی هشدار می‌دهند که این درگیری به بن‌بستی ناپایدار و «نه جنگ، نه صلح» رسیده است و معتقدند اگر تا آن زمان توافقی حاصل نشود، ترامپ ممکن است پس از انتخابات میان‌دوره‌ای دوباره به عملیات رزمی گسترده روی آورد.
آنچه او می‌گوید:
ترامپ در این مصاحبه روشن کرد که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای درباره گام‌های بعدی جنگ استفاده کند.
▪️
ترامپ گفت: «می‌خواهم بفهمم در چه وضعیتی هستند و اوضاعشان چطور است. ما خیلی از آن‌ها محافظت کرده‌ایم.»
▪️
کشورهای شرکت‌کننده عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان هستند.
▪️
ترامپ از گفتن اینکه تصمیمش درباره مسیر پیش رو را قبل یا بعد از انتخابات میان‌دوره‌ای خواهد گرفت، خودداری کرد.
زمینه خبر:
در اوایل اوت، ترامپ پس از آن از ازسرگیری عملیات رزمی گسترده خودداری کرد که عربستان سعودی و قطر ابراز نگرانی کردند ایران در اقدامی تلافی‌جویانه تأسیسات نفت و گاز عربستان را بمباران کند.
▪️
از آن زمان، ترامپ رویکردی «کم‌سروصدا» در پیش گرفته است: تعلیق مذاکرات با ایران، آغاز کارزار تازه تحریم‌های اقتصادی، ادامه محاصره دریایی بنادر ایران و متمرکز کردن ارتش آمریکا بر بازگشایی تنگه هرمز و افزایش جریان نفت به بازار جهانی انرژی.
▪️
ارتش آمریکا عبور نفتکش‌ها و کشتی‌های حامل گاز از تنگه را به‌طور قابل‌توجهی افزایش داده است. با این حال، ترافیک همچنان پایین‌تر از سطح پیش از جنگ است و قیمت نفت نیز همچنان بالاست.
وضعیت فعلی:
به گفته مقام‌های آمریکایی، ترامپ و پیت هگست، وزیر دفاع، به ارتش دستور داده‌اند سطح نیروهای خود در خاورمیانه را تا پایان سال حفظ کند تا برای احتمال بازگشت به نبرد تمام‌عیار آماده بماند.
▪️
این مقام‌ها می‌گویند ترامپ باید به‌زودی درباره مسیر پیش رو تصمیم بگیرد، بخشی از دلیل آن این است که ارتش آمریکا نمی‌تواند خیلی بیشتر در وضعیت فعلیِ انتظار باقی بماند. یکی از این مقام‌ها گفت: «بالاخره در مقطعی باید تصمیم بگیرید که هدف نهایی چیست.»
▪️
ترامپ به اکسیوس گفت از اینکه محاصره دریایی مانع صادرات نفت ایران شده، بسیار راضی است. او گفت: «از وقتی شروع کردیم، حتی یک کشتی هم به ایران نرفته است. تلاش کردند و ما آن‌ها را منفجر کردیم.»
▪️
رئیس‌جمهور افزود که ایران مستقیماً با آمریکا در تماس است و گفت ایرانی‌ها همچنان خواهان دستیابی به توافق هستند.
تصویر کلی:
کاخ سفید همچنین در حال کار روی یک راهبرد پس از جنگ است که خواستار تلاشی منطقه‌ای برای مهار ایران و هم‌زمان گسترش عادی‌سازی روابط میان اسرائیل و همسایگانش است.
▪️
هرچند این طرح هنوز در مراحل ابتدایی تدوین قرار دارد، هدف آن هدایت رویکرد آمریکا در خاورمیانه پس از پایان جنگ ایران و در دو سال پایانی دوره ریاست‌جمهوری ترامپ است. دو رویداد بزرگ بر این برنامه‌ریزی سایه انداخته‌اند: انتخابات ۲۷ اکتبر در اسرائیل و انتخابات میان‌دوره‌ای آمریکا در نوامبر.
چه چیزی را باید زیر نظر داشت:
وقتی از ترامپ پرسیده شد آیا هفته آینده در نیویورک با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد، گفت: «شاید.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78423" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9Gt60Mxu0Q50m76DYgoetpxqwuL7VDdOvCxmJjfMZeniXdRZAjBfJp54-2y3V8W8lD_TMW-1UTeMYJk1WZkMFhyerhZ-z6O_A5nVKhi-0sdXcR24gIILjGFoMPXuzuT6ITmeu26cCSKP15Jn2uethB23DfzFIA8PBKP8pecbv1-mRzsV8sfwfg0H1MzyLS4AzwHstaja9ZGnUz7ZFTDUjT-n2n9lTtmS4lldV-FeOtPg9c9zydsqHjzGUEXHsIwQYWes4bRtQ8ToCCyVVYsjoQxiJRAt9DQSWTrxfK3EkR3kf0pWJktgINk8d0toypB20xCA2NBvXOyRfTF7R_geg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز پنج‌شنبه ۲۶ شهریور به نقل از مقام‌های آمریکایی گزارش داد نیروهای جمهوری اسلامی در روزهای اخیر دست‌کم دو پهپاد ام‌کیو-۱ آمریکا را سرنگون کردند.
مقام‌های آمریکایی که به شرط فاش نشدن نامشان با سی‌بی‌اس نیوز گفت‌وگو کردند، مشخص نکردند این پهپادها در کدام بخش منطقه سرنگون شدند و از کدام مدل ام‌کیو-۱ بودند.
این پهپادها برای ماموریت‌های اطلاعاتی، شناسایی و نظارتی طراحی شده‌اند و قابلیت حمل موشک‌های هلفایر را نیز دارند. سی‌بی‌اس نیوز نوشت این پهپادها در تنگه هرمز می‌توانند برای نظارت مستمر بر آبراه، رصد فعالیت‌های نظامی جمهوری اسلامی و شناسایی تهدیدها علیه نیروهای آمریکا و کشتیرانی تجاری به کار گرفته شوند.
بر اساس گزارش دفتر بودجه کنگره آمریکا، از آغاز جنگ آمریکا علیه جمهوری اسلامی دست‌کم ۲۴ پهپاد ام‌کیو-۹ ریپر به ارزش تقریبی ۷۲۰ میلیون دلار از دست رفته‌اند. یک پهپاد ام‌کیو-۴سی تریتون به ارزش حدود ۱۵۰ میلیون دلار نیز منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78422" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D0t2wDy-Mnoudz65fEiV9F7CJPdKaV8n077kbCxnt2IgXbNyJAkxmvUTypdk-mA0U_UzZpkUsHMQlDFEpVpg1GrEJdshsCdMyftR4b2MT4VjkyvMEnaxwhmCVMTwYBYVK1PzFs6Z1K57zn2o4FTY9I7sW8HI3S3IjIftOEQ_ftW1PCwTSc2pjsFqFnVOTT1JLmkI3AvMSWo_rJqOcG-1HD6XU-HpRjrW87ZSfUwWliq_-Q37cO3-gdgh6YZ-6VXFOeYVw9U0e9O708O_aUUAdw1jFjsZjyWH_niuofMGd-tmjUPnqeT1rAQQmbHTha8zAokm73gQu-qo5pFCHbVvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=XYQ3MilZTuTX2vP_AUuK8Z4o-x3ZTBwJGc1qCfcec2V5c_90fFXLbfJ9r8z-ZRw0lVH-2zzaVHOzzi92sP9HO3_xPz-kElyzBaj-EoPO6Bt2Vj-yj28On-0KUJZA9PqCUASRqutz6cBVIpbXDHVKWKO8_wqC0SQhq8e5eKm2k7mIxxONoZ247mq5eEFYol3tFiuVmfMpOyNT1cbJvE7VfJtbNkpf6FtGCJxTxwkDwUVJC-GyGAiGepPgHlGQyDgw20E1Cf5-nzPWLfEuTTu0I7K_k2nSdyA5YisEZUfTrptOpiEUkQXant2SG8L_dgmfvNIw0Wp0E7UZowbjtW8R5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=XYQ3MilZTuTX2vP_AUuK8Z4o-x3ZTBwJGc1qCfcec2V5c_90fFXLbfJ9r8z-ZRw0lVH-2zzaVHOzzi92sP9HO3_xPz-kElyzBaj-EoPO6Bt2Vj-yj28On-0KUJZA9PqCUASRqutz6cBVIpbXDHVKWKO8_wqC0SQhq8e5eKm2k7mIxxONoZ247mq5eEFYol3tFiuVmfMpOyNT1cbJvE7VfJtbNkpf6FtGCJxTxwkDwUVJC-GyGAiGepPgHlGQyDgw20E1Cf5-nzPWLfEuTTu0I7K_k2nSdyA5YisEZUfTrptOpiEUkQXant2SG8L_dgmfvNIw0Wp0E7UZowbjtW8R5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز پنجشنبه ۲۶ شهریورماه در مراسم تقدیر از کارکنان برگزیده شاباک در بیت‌المقدس گفت اسرائیل بخش عمده ماموریت خود در برابر جمهوری اسلامی و گروه‌های متحد آن را انجام داده، اما این ماموریت هنوز به پایان نرسیده است. او گفت توانایی ایران و متحدانش برای آسیب رساندن به اسرائیل به‌شدت کاهش یافته است.
نتانیاهو با اشاره به ادامه عملیات اسرائیل گفت: «هنوز کارهایی برای تکمیل باقی مانده است و ما آن را به پایان خواهیم رساند.» او سپس تاکید کرد که اسرائیل حماس را از بین خواهد برد و در مورد جمهوری اسلامی گفت: «حکومت ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سرنگون خواهد شد.» او همچنین گفت اسرائیل به اقدامات خود علیه حزب‌الله ادامه خواهد داد.
نخست‌وزیر اسرائیل همچنین گفت خواست ایران و گروه‌های متحدش برای نابودی اسرائیل از بین نرفته، اما به گفته او، توانایی آن‌ها برای تحقق این هدف به‌شدت تضعیف شده است. این اظهارات در مراسم تقدیر از کارکنان برگزیده شاباک برای سال ۲۰۲۵ مطرح شد که با حضور اسحاق هرتزوگ، رئیس‌جمهوری اسرائیل، و داوید زینی، رئیس شاباک، برگزار شد.
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در شبکه اجتماعی اکس نوشت کارزار نظامی اسرائیل هنوز پایان نیافته و این کشور «اهداف مهمی» در برابر ایران و جبهه‌های دیگر دارد.
او گفت اسرائیل برای دستیابی به این اهداف «با قدرت نظامی و تدبیر سیاسی» اقدام خواهد کرد.
کاتز روز پنجشنبه ۲۶ شهریورماه با اشاره به غزه گفت سیاستی که همراه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دنبال می‌کند بر سلب توانایی گروه‌های جهادی برای حفظ قلمرو، زیرساخت‌ها، فرماندهان و تجدید قوا متمرکز است. او افزود اسرائیل این رویکرد را در غزه، لبنان و شمال کرانه باختری اجرا کرده است.
وزیر دفاع اسرائیل همچنین گفت این کشور فرماندهان «سپاه فلسطین» در ایران را هدف قرار داده و اجازه نخواهد داد ایران یا هیچ طرف دیگری حماس را دوباره مسلح کند. او تاکید کرد اسرائیل به عملیات خود برای تحقق اهداف امنیتی و جلوگیری از تکرار حمله‌ای مشابه هفتم اکتبر ادامه خواهد داد.
کاتز همچنین رجب طیب اردوغان، رئیس‌جمهوری ترکیه، را خطاب قرار داد و گفت اگر می‌خواهد به همفکرانش در غزه کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما «قدم به غزه نخواهد گذاشت».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78420" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVvshbQz09Frf-lWPO9M75MVWSDYnoeUBUIirW-b_-UZ2Inie8i-jLynv10XPzfyTrWFgxgcphoFjmy-DYU0-QDHBxkox2Herogou2vJ6qQZL-UXgBlg5He7hHWWRROIrTr7PFW2KSnZLqzmZxbAnPTbo9PWp3CpPvJ2MLxID37e1eHBi4fk4Lq2DmkPHM-RS8B-SJQf2BrgDi0Ilz6VNLhXPysdmgLnBMsHLowMRQaLV7IEhzekzmE-pMzQDbDjCUEHBpN5t9OCdW1_z_jqvsEYN6X-ewWNnaFL0RCM_x-tknGBJDYdUQ8wlG6Tu3y4LcPhD3zVuG-0YGw9r_e9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیات حقیقت‌یاب مستقل بین‌المللی سازمان ملل درباره ایران در تازه‌ترین گزارش خود اعلام کرد دلایل معقولی برای این باور وجود دارد که آمریکا در جریان جنگ با جمهوری اسلامی، در دو حمله هوایی به ایران مرتکب «جنایت جنگی» شده است. بر اساس این گزارش، این حملات دست‌کم ۱۷۸ غیرنظامی، از جمله زنان و کودکان، را کشت.
این هیات در گزارشی که به شورای حقوق بشر سازمان ملل ارائه شد، حملات آمریکا و اسرائیل به ایران در ۹ اسفند ۱۴۰۴ را بررسی کرد و به این نتیجه رسید که آمریکا در دو مورد حملاتی بدون تمایز انجام داده که به کشته یا زخمی شدن غیرنظامیان و آسیب به اماکن غیرنظامی منجر شده است.
بر اساس یافته‌های هیات حقیقت‌یاب، در یکی از این موارد، موشک‌های تاماهاوک به دبستان شجره طیبه در میناب اصابت کردند. این هیات اعلام کرد این مدرسه به وضوح قابل شناسایی بوده و در این حمله بیش از ۱۵۰ نفر، از جمله حدود ۱۲۰ کودک، کشته شدند.
در موردی دیگر، آمریکا با استفاده از موشک‌های تهاجمی دقیق، ساچمه‌های تنگستن را بر فراز یک مجموعه ورزشی و منطقه مسکونی در لامرد پراکنده کرد. بر اساس گزارش، این حمله ۲۲ زن و مرد غیرنظامی را کشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78419" target="_blank">📅 21:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOAh-6RpMw3V-kFKmv5TmOVz8TKiZDLi7E_IA7Wp37Cd-FJbPLZt6Cj1e5l9Ow7810xR5ptOV1td0DIGE8ydeGp0hTuZsxm8HtW8a1Ln908sUlLzkgSBfkFTtQOxMckNxiZ3nNIt6jbaSm1j1UAOePYmkG9j6xDMZuunBlJ4Spj_0koAUoKmZe4nOzo9dKfGpu8pPdh9Oa2vcVAK47Ybq341R-1chS_vQFkBfPTdHxU9T5pkg2g9Bq8NgQD7znv6FavhRURbmElKTZYp_YeAgWNkgOZ63avSlALV4h3KM8jnooiv0sLYopNj9mydzXOumCYV0wjg7AKmaz3ppneyPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه و چین روز پنجشنبه، ۲۶ شهریور، در نشست شورای امنیت سازمان ملل متحد، پیش‌نویس قطعنامه پیشنهادی ایالات متحده برای تمدید ماموریت هیات کارشناسان کمیته تحریم‌های ۱۷۳۷ علیه جمهوری اسلامی ایران را وتو کردند.
این نشست با ابتکار فرانسه که در ماه سپتامبر ریاست دوره‌ای شورای امنیت را بر عهده دارد، در چارچوب دستورکار «منع اشاعه» برگزار شد. در جریان رای‌گیری میان ۱۵ عضو شورای امنیت، این قطعنامه ۱۱ رای مثبت کسب کرد، اما با مخالفت صریح (وتو) مسکو و پکن و همچنین رای ممتنع پاکستان و سومالی مواجه شد. برای تصویب یک قطعنامه در این شورا، علاوه بر کسب حداقل ۹ رای موافق، وتو نکردن اعضای دائم الزامی است.
دیپلمات‌ها پیش‌تر از مخالفت قطعی روسیه و چین با این طرح خبر داده بودند. مسکو و پکن معتقدند که با انقضای قطعی قطعنامه ۲۲۳۱ برجام در اکتبر ۲۰۲۵، تمامی سازوکارهای تحریمی پیشین از جمله کمیته ۱۷۳۷ فاقد هرگونه اعتبار و اثر حقوقی هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78418" target="_blank">📅 18:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/caed21affc.mp4?token=E5SgRHZCB5oWEgVvyoSZq14P8bKADbHAJD2ujNa_j9Qxq9vEE86u8FxpV6JJ08JFU33BEJdeeq1YX2QBwU4uLtI9bM5l46dmm45cf0Tec5Z4a-yZ3CfXDuzCeb3aDZ7MrDAT5QT8Ufw6pLupfe4BzHmAP4Iudbxqnp8GreQ4d4E7fODnTeyjHucxGQhA9dwn8P1OGXvDti0ae7N8z7bMxDKtR0VGVLg6GCEcB8kUZCmDvZ2ATCns9QpRPblksL_6BKtblvkJ5GgNT5dGWKNDvov0MZAHXND7xxm-VmLwFhGd0liE14RuKAh1NkQQroZ2j1mO9GfsD35GrRwmwoKBbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/caed21affc.mp4?token=E5SgRHZCB5oWEgVvyoSZq14P8bKADbHAJD2ujNa_j9Qxq9vEE86u8FxpV6JJ08JFU33BEJdeeq1YX2QBwU4uLtI9bM5l46dmm45cf0Tec5Z4a-yZ3CfXDuzCeb3aDZ7MrDAT5QT8Ufw6pLupfe4BzHmAP4Iudbxqnp8GreQ4d4E7fODnTeyjHucxGQhA9dwn8P1OGXvDti0ae7N8z7bMxDKtR0VGVLg6GCEcB8kUZCmDvZ2ATCns9QpRPblksL_6BKtblvkJ5GgNT5dGWKNDvov0MZAHXND7xxm-VmLwFhGd0liE14RuKAh1NkQQroZ2j1mO9GfsD35GrRwmwoKBbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خشونت و آزار جنسی)
ویدیو نشان می‌دهد ماموران فرماندهی انتظامی جمهوری اسلامی ایران یک نوجوان را مورد ضرب و شتم و آزار جنسی قرار داده‌اند.
این ویدیو خشم بسیاری از کاربران را برانگیخته است. برخی  گفته‌اند که «وقتی پلیس مقابل دوربین دست به چنین کارهایی می‌زند، معلوم نیست در بازداشتگاه و پشت درهای بسته چه به سر بازداشت‌شدگان می‌آورد.»
فرمانده انتظامی آذربایجان شرقی گفته که این اتفاق ۱۴ خرداد ۱۴۰۵ در جریان یک نزاع خیابانی در تبریز رخ داده است.
برخی هم با اشاره به انتشار این ویدیو در چهارمین سالگرد کشته شدن مهسا (ژینا) امینی در بازداشت گشت ارشاد، به تداوم خشونت پلیس در سایه نبود قوانین بازدارنده اشاره کرده‌اند.
پس از پربازدید شدن این ویدیو، فرمانده انتظامی استان آذربایجان شرقی گفت که ماموران حاضر در ویدیو «تنبیه انضباطی» شده‌اند.
علی محمدی به خبرگزاری فارس گفت که این افراد «تنبیه و انتظار خدمت» شده‌اند و «اقدامات تنبیهی تکمیلی» در مورد آنها در دست اقدام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78417" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJMsni5YtMHkbQI3YfHRe7zWIMjkdBoA-xFoAIAIDFAFLUnY5gzVq1XHE3WZ0-LdGOF96GhcMYHt10iDk5yThTQxrobksvQhnqjrP6uqzslJGUrgKLu-SDAuFwmlXDLFWfezyEFWeF2f84t094bA_f3iOFBrKZQKGrjLmONTwcAASLIqwDZEVUR8F2EIv4cTaW5h9iPrFZUc_F_d7bhxFjUOzcuVSKXrYca5LEeTqvFV-QDABx2_gSKhdBYYcahpxlsh7b9zTk9-L3dWKUERHQyMz1nW2zJoYSXhOmQyb_bSg8NM8kNm3U7_tnR7hwRUpwdZ3TXUnRSZVAx2ZkI4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، مدعی شده است جمهوری اسلامی مستقیما با دولت او تماس گرفته و «بسیار» خواهان دستیابی به توافق با ایالات متحده است. او همچنین ابراز امیدواری کرده جنگ نزدیک به پایان باشد.
ترامپ بامداد پنج‌شنبه ۲۶ شهریور ۱۴۰۵، پس از ورود به ایالت کارولینای شمالی، در پاسخ به پرسش خبرنگاران درباره مرحله کنونی جنگ گفت: «امیدوارم به پایان جنگ نزدیک شده باشیم.»
او سپس درباره احتمال دستیابی به توافق با جمهوری اسلامی گفت: «آن‌ها می‌خواهند توافق کنند و خواهیم دید چگونه پیش می‌رود.» ترامپ در پاسخ به این پرسش که آیا پیام ایران از طریق میانجی‌ها منتقل شده یا تماس مستقیمی صورت گرفته است، گفت این تماس «مستقیم» بوده، اما درباره زمان، سطح و محتوای آن توضیح بیشتری نداد.
رییس‌جمهوری آمریکا ساعاتی بعد در یک گردهمایی انتخاباتی در شهر گاستونیا در کارولینای شمالی، بار دیگر گفت جنگ با ایران به‌زودی پایان خواهد یافت و «پایان واقعا خوبی» خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78416" target="_blank">📅 03:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KSdcfWNf6e2Z79QXgOiCScc8d3_W9LddYV5WLuu32IZFXECsliwh_QY6TtSA4w64i598TgC7s2Eg_L4Po8p715leDCEEvZFTi-zj83htx6xBx-n45VW6wzgPi3gQC4TZjl5zj5Lb2QFo3i6t1GoYJcEZBIV9vEbxzTMQJpj93gwltQ0U_8GgdvluEjDuB5DPDxkW2pKDKuRiA_qwfRZ9HOOEsKezhHOlhlYeFtotZJALPwESYHP38x8KiRt-b1kPS4u2M38QDjsGL0b4GSvZm5QpLzNHHAlF6yGdTvWHodiyzpHydqL0wLd3Gw9V7CEcN24nZ-zhS0WCMJuKIyTSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی ماهان چهارشنبه ۲۵ شهریور در اطلاعیه‌ای اعلام کرد پروازهای این شرکت در مسیر تهران-مسقط-تهران از ۲۶ شهریور، برابر با ۱۷ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان دلیل لغو این پروازها را اعلام مراجع هوانوردی عمان عنوان کرد.
این شرکت همچنین در اطلاعیه‌ای جداگانه اعلام کرد بنا بر اعلام مراجع هوانوردی ترکیه، پروازهای ماهان از ایران به مقصد ترکیه، شامل استانبول، آنکارا و بالعکس، از ۳۰ شهریور، برابر با ۲۱ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان افزود آخرین پروازهای این شرکت در مسیرهای تهران-استانبول، تهران-آنکارا و بالعکس روز ۲۹ شهریور انجام خواهد شد.
خبرگزاری عصر ایران نیز سه‌شنبه ۲۴ شهریور به نقل از یک منبع آگاه گزارش داده بود دولت گرجستان در پی تحریم‌های جدید آمریکا، پرواز همه شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه آینده متوقف می‌کند.
عصر ایران افزود بررسی این رسانه از چند آژانس گردشگری نشان می‌دهد فروش تورهای گرجستان نیز تنها تا یکشنبه ۲۹ شهریور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/78415" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lKg56DSjwcUsGHsKneZz8G6oUb3x9N4YLf2nxmfiq9abTQq1Vk29hLJ_-aQJfO3FGpwJJRUuZ2Rs5xzMvO58cMNia8OTijuThU0mZm-c3i9RGf19V9V2zbFxvG5xyTM_rcOAoZu2ueTEnCIPNFzmIQ1eKjtMGUZFu0NQEwS9kuIgsBHCEpziAkbonNqgJ_E2iTYflAB7jI53oyHbSf0uKrFlWqcGs7Cs6sJIfJq-P7L6Nd3E5-CmdzJltXvUof67koW8_yRt6qQHZzEGXxxtZEahF3OJmjPLv1gLDNjDQfn-Ygms7O_JBiIysA46sY6ANkI3-AmrlDMw61bw-fynyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل قدیانی، زندانی سیاسی محبوس در زندان اوین، روایت جمهوری اسلامی درباره نقش «تروریست‌های وابسته به بیگانگان» در کشتن معترضان دی‌ماه ۱۴۰۴ را رد کرد و نیروهای حکومتی را مسئول «قتل عام» آن‌ها دانست.
قدیانی در بیانیه‌ای که روز ۲۴ شهریور از بند هفت زندان اوین نوشته، با اشاره به راهپیمایی ۲۲ بهمن و تجمعات حکومتی ماه‌های گذشته پرسیده است اگر عاملان تیراندازی به معترضان، آن‌گونه که حکومت می‌گوید، «تروریست» بوده‌اند، چرا در تجمعات حکومتی که در امنیت برگزار شده‌اند، اثری از آنها نبوده است.
او از رسانه‌ها و نهادهای حقوق بشری خواسته است درباره این تناقض در روایت جمهوری اسلامی پرسشگری کنند و نوشته است: «تروریستی در کار نبوده و نیست و قاتلان [...] همان نیروهای [...] حاکمیت‌اند.»
قدیانی همچنین در این بیانیه علی خامنه‌ای و پسرش مجتبی خامنه‌ای را مسئول این «جنایت سهمگین» دانسته و نیروهای حکومتی را به تیراندازی به معترضان متهم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78414" target="_blank">📅 17:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyIIhxSIOs2-7NNSfxFzLVJm7EiHN5QGTv3cDJeLypzDQHcVDqNng56ypjWM2Yi_rtPspCFWKMgYhrhyBUNsD1O3mg4rmmd20D_ep4RtNbgAmkKjXbi4ZFXFJqOuz050LzbQad6a2WJTx628eV_UX8-6rna0mpykqoPPFb5rWspfojEmZNnAiYrThPJNCKcKoe9u_9tx9dK5kPqqNTjrxYElDyMOTzq2OM6dyTVqh8tzIVtJ1VJi-0FWFmPP5WH_1sVkl03_7X5fmgxt_uYXIPipo6AhkI1slX4iNSn8-Ki8z5Hs_njsuWpJOZoBDnAqZvFyG8iye_fzc7kC9FXTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین با صدور بیانیه‌ای اعلام کرد که وانگ ئی، وزیر امور خارجه این کشور، روز چهارشنبه در دیدار با عباس عراقچی در پکن گفت:
چین، ایران و ایالات متحده را تشویق می‌کند تا عقلانیت خود را حفظ کرده، خویشتن‌داری نشان دهند، به یادداشت تفاهم اسلام‌آباد بازگردند و «در گفتگوهای ماهوی درباره مسائل مورد علاقه طرفین مشارکت کنند.
براساس این گزارش، وانگ با بیان اینکه چین «نمی‌خواهد شاهد سرایت بیشتر تنش‌های منطقه‌ای به یمن و دریای سرخ باشد» افزود: «ما از همه طرف‌ها می‌خواهیم اقدامات موثری برای بازگشایی هرچه سریع‌تر تنگه هرمز انجام دهند.»
وانگ همچنین گفت که سیاست چین در قبال ایران همواره ثابت و پایدار بوده و چین مایل است ارتباطات و هماهنگی‌های خود را با تهران تقویت کند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، چهارشنبه، ۲۵ شهریور در سفر به پکن با وانگ یی، وزیر خارجه چین، دیدار کرد و بر گسترش روابط تهران و پکن در چارچوب مشارکت جامع راهبردی تاکید کرد.
عراقچی شرایط کنونی منطقه را ناشی از حملات نظامی آمریکا و اسرائیل به ایران دانست و از مواضع چین در محکوم کردن اقدامات این دو کشور قدردانی کرد.
او گفت: «جمهوری اسلامی ضمن آمادگی کامل برای دفاع مقتدرانه از حاکمیت ملی و تمامیت سرزمینی و صیانت از امنیت و منافع ملی ایران در مقابل متجاوزان، از راه‌حل‌های دیپلماتیک که حقوق ملت ایران را تامین کند، استقبال می‌کند.»
عراقچی همچنین گفت شرایط منطقه پس از جنگ ایران تغییر کرده است و در نظم جدید منطقه‌ای که با گفت‌وگو و همکاری کشورهای منطقه همراه خواهد بود، جایی برای حضور و دخالت نیروهای خارجی وجود ندارد.
او با اشاره به آنچه نقض مکرر تعهدات از سوی آمریکا خواند، گفت جمهوری اسلامی خواهان بازگشت آرامش به منطقه و روابط دوستانه با همسایگان است و در همین راستا گفت‌وگو با کشورهای منطقه را آغاز کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78413" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uKjATLo9UoxwzmXiCA5n8x_vDgWp-un5mt7akA368sDbyTpyoNbvLeN22Tjbdl9Bi6qRAbmzCigFUwNjZN9So-a1KIFsQY3Gg6cH4eHsgAnWs1YxlUOPFe3VS7FPG3uq02Fn3Oia_KEK47pMvtobWETDaJm-gRniVpOjKsiOxyomgGUctuzjeOCAf2jfa0i-7JpsT93lWPZntZQHdqBeOv526V3eY5GvcD-trXvV957FzcV9Bsipg00FyAisl03jsO86aGKYtnVx8wg1teqT6wiEFeDbdEhgqda0ukmHNjNWA8nEUH3oBgL9RT2f-sYbJ2q_lPb9EfaoVJ_asrVNtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز چهارشنبه ۲۵ شهریورماه به نقل از پنج منبع آگاه گزارش کرد که مقام‌های ایالات متحده آخر هفته گذشته (روزهای شنبه یا یکشنبه) با نمایندگان شورشیان حوثی مورد حمایت جمهوری اسلامی ایران، دیدار کرده‌اند.
براساس این گزارش سه تن از این منابع که خواستند نامشان فاش نشود گفتند این دیدار که رسانه‌ای نشده بود، در سفارت آمریکا در مسقط برگزار شد. دو منبع دیگر نیز اشاره کردند که دولت عمان، به عنوان میانجی باسابقه منطقه‌ای، به برگزاری این نشست کمک کرده است.
دونالد ترامپ در سال ۲۰۲۵ و پس از بازگشت به قدرت حوثی‌ها را در فهرست «سازمان‌های تروریستی خارجی» قرار داد و هرگونه حمایت از این گروه را جرم‌انگاری کرد.
ترامپ روز شنبه گفت حوثی‌ها با دولت او تماس تلفنی داشته و از ایالات متحده خواسته‌اند از جنگ یمن دور بماند. جی‌دی ونس، معاون رئیس‌جمهوری هم روز دوشنبه بدون ارائه جزئیات تاکید کرد که ایالات متحده در تماس مستقیم با این گروه است.
دو منبع آگاه اعلام کردند در این نشست که به گفته یکی از آن‌ها روز یکشنبه برگزار شد، حوثی‌ها به مقام‌های آمریکایی گفته‌اند قصد حمله به شناورهای آمریکایی را ندارند و به آتش‌بس سال ۲۰۲۵ با آمریکا متعهد هستند.
یکی از این منابع که یک یمنی است، گفت این گروه همچنین اعلام کرده‌اند که به کشتی‌های اسرائیلی یا هرگونه کشتی تجاری دیگر، به‌جز کشتی‌های متعلق به عربستان سعودی، حمله نخواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78412" target="_blank">📅 17:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plBRUZvHbDWEvY7_OX76nH1N2QM3AVg6A8M-NCmKxoR2hycIAMLNKEvwZk5R2SrT0xJXqIiFqf2tbaMEBaqbIxBQT34zLkHTc7rNHk9mRqCPnH3phXKq1f16YdkF-M9g3yZHIyQ2RM--ASdP1JF-vW7dLEg8nlOomDHXl3rg8kFoeUVCpaw3gWG8WdUSuen2J5mp8_dSifa_eYxcg5FqbMiSs9IT-nafOxcfZAs_AnPVHGF3SYWSSmq2VMMOiDqqPFEmfiOXq3J-ZDd8OviJHwZyg8MkRO0bD8bUXPyHRPBW6pEy58LSIApPBzqDx2nq1-bOY7hhRQi09CVv3qHXSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جی‌دی ونس‌»، معاون رییس‌جمهوری آمریکا، گفته است جنگ با جمهوری اسلامی طی «یکی دو ماه آینده» وارد مرحله‌ای کاملا متفاوت خواهد شد و واشنگتن در مرحله بعدی باید مانع بازسازی توانایی‌های هسته‌ای و نظامی حکومت ایران شود.
ونس همچنین با پیش‌بینی «دونالد ترامپ» همراه شده است که جنگ پس از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت؛ هرچند توضیح نداده منظور از «مرحله متفاوت» تشدید عملیات نظامی، کاهش درگیری‌ها یا آغاز روندی دیپلماتیک است.
معاون رییس‌جمهوری آمریکا در گفت‌وگو با نیویورک‌پست که روز سه‌شنبه ۲۴ شهریور ۱۴۰۵ منتشر شد، گفت: «نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم رییس‌جمهوری درست می‌گوید که این مسئله طی یکی دو ماه آینده وارد مرحله‌ای کاملا متفاوت خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78411" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rrOQOTwz34nUD2rFGoJHgaA0QYJOV-0CZf2LZSnTJwnNDgqulqO27fCJk8p5PXC3URwPyhBLvIwP_EcLjHzJbO2RxuJ4Yi4xxb049gzvZps6HYakCJ6Yxbxie3O9IzBk81AKNAlkBAydQlC9Rk4C3G3lgdgjbUs1IDxjF5Zp5mIQoaRfkPBDYKy-HqlCAXx_-Jhktruwz1omxv80xrc2smGXl2fEDsoEZYc-KCTZwOypunlv1ZYaD_dB9Zqnp13s1yuPjbuyJe3h9IpWQq1rdr_LnwDWrhHv1GoatCkWSmPRkMjkkTfwwwEX_8TCvVNiKIy9-7YKxaCx-E0rno0rEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین قشقایی، همسرش سارا شمسایی و ابوالفضل قشقایی، برادر حسین، از معترضان دی‌ماه، پنجشنبه ۱۹ شهریور بازداشت شدند.
حسین قشقایی و سارا شمسایی در لاهیجان به دست نیروهای وزارت اطلاعات بازداشت و به اراک منتقل شده‌اند.
محل دقیق نگهداری آنها مشخص نیست و احتمال می‌رود در بازداشتگاه اداره اطلاعات اراک باشند.
ابوالفضل قشقایی نیز همان روز در زرندیه ساوه بازداشت و به اراک منتقل شد. به گفته یک منبع مطلع، ماموران هنگام بازداشت با خشونت وارد منزل شدند و گوشی‌های تلفن، تبلت و لپ‌تاپ اعضای خانواده را با خود بردند.
حسین قشقایی با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «اغوا و تحریک به جهت برهم زدن امنیت کشور به جنگ و کشتار»، «نشر اکاذیب در فضای مجازی» و «اجتماع و تبانی علیه امنیت ملی» روبه‌رو است.
درباره اتهام ابوالفضل تاکنون اطلاعاتی به خانواده اعلام نشده و پرونده این سه نفر هنوز به شعبه‌ای ارجاع نشده است.
از دی‌ماه، سیم‌کارت‌های حسین و سارا و حساب بانکی حسین نیز مسدود شده بود. آنها ماه گذشته به دادسرای عمومی و انقلاب زرندیه احضار شده بودند، اما در مهلت پنج‌روزه تعیین‌شده حاضر نشدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78410" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=LrAfc8goei2yknwXsc0nbzA9vSsqLf4jH2EGePyPAkN2SYPV7l1yi_PMJm6OZJSF2KllI2IzupvkJMmmt0KuEhCJ5gu0z8-_7r6v6mp8EDJWSlofPXJMTK5BUUuIPl6lyARwTqUF0zUu4JTAJu357uxwFy7x6y94i0EamheibwpSYCUCkcNIAzzsrlp4l0I06NqRtk94tKbxAth5R-zq32K4elujaYO8r97sZ2-zkVQ04K2vLwrxlF4k2_SO1LpPLG6Y-Zu6gf1_GnhVnGFSWSjka-kyeQb4eKCpm08JA2y3oYewVgwhCjQVNK2fIGkAOwQN2EkGuTLgKCEbt7FXiUOqfk7HqEZL0fR0niPhbiMPsOR083M9cf8N3L6eX7PJtVYtaphi_HctWd7FtKA7TxAy_zDXHg2vaB6N0cHlU7QDSBD7HNlswg0oWllse0rzIZH1sYXBnN3i4AY3myXDrVYuvHeVVLv6HMxh1GjFGkLwladsdjvEaLOFgQDQb872KdIuuH7YeP1boIwSFSvP4g16tU6emwR6jW6YFoMjuXZGwqiJYeKvyjw1ZT_iz9a9SXeH5aGXjlPyf_Qsqsc3ll0NdrMI1wG7VharBnl1JIetHDN2LvEzE68uOW0TLfHte0LSNuduKd5KJ2i2C9a3xMxVy3WzcPnJ3PY6CkVBNu8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=LrAfc8goei2yknwXsc0nbzA9vSsqLf4jH2EGePyPAkN2SYPV7l1yi_PMJm6OZJSF2KllI2IzupvkJMmmt0KuEhCJ5gu0z8-_7r6v6mp8EDJWSlofPXJMTK5BUUuIPl6lyARwTqUF0zUu4JTAJu357uxwFy7x6y94i0EamheibwpSYCUCkcNIAzzsrlp4l0I06NqRtk94tKbxAth5R-zq32K4elujaYO8r97sZ2-zkVQ04K2vLwrxlF4k2_SO1LpPLG6Y-Zu6gf1_GnhVnGFSWSjka-kyeQb4eKCpm08JA2y3oYewVgwhCjQVNK2fIGkAOwQN2EkGuTLgKCEbt7FXiUOqfk7HqEZL0fR0niPhbiMPsOR083M9cf8N3L6eX7PJtVYtaphi_HctWd7FtKA7TxAy_zDXHg2vaB6N0cHlU7QDSBD7HNlswg0oWllse0rzIZH1sYXBnN3i4AY3myXDrVYuvHeVVLv6HMxh1GjFGkLwladsdjvEaLOFgQDQb872KdIuuH7YeP1boIwSFSvP4g16tU6emwR6jW6YFoMjuXZGwqiJYeKvyjw1ZT_iz9a9SXeH5aGXjlPyf_Qsqsc3ll0NdrMI1wG7VharBnl1JIetHDN2LvEzE68uOW0TLfHte0LSNuduKd5KJ2i2C9a3xMxVy3WzcPnJ3PY6CkVBNu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فراخوان ائتلاف نیروهای سیاسی کردستان ایران، همزمان با چهارمین سالگرد قتل حکومتی مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»، کسبه و بازاریان شماری از شهرهای کردنشین اعتصاب کردند و مغازه‌های خود را بسته نگه داشتند.
از صبح تا ظهر چهارشنبه ۲۵ شهریور، اعتصاب و بسته بودن مغازه‌ها و بازار در دست‌کم ۲۰ شهر، از جمله ارومیه، اشنویه، بانه، بوکان، بیجار، پاوه، پیرانشهر، ثلاث باباجانی، جوانرود، دیواندره، روانسر، سقز، سنندج، قروه، کامیاران، کرمانشاه، کرند، مریوان، مهاباد و میاندوآب گزارش شده است.
@
VahidOOnLine
وب‌سایت‌ها و منابع خبری مختلف که اخبار کردستان را منتشر می‌کنند، از جمله هانا، کردپا، کولبرنیوز، زاگرس ۲۴ و شبکه حقوق بشر کردستان نیز گزارش‌ها و تصاویری از تعطیلی مغازه‌ها در شهرهای مختلف کردنشین منتشر کردند.
در همین حال تصاویر و گزارش‌های مختلفی از برقراری فضای امنیتی شدید و استقرار نیروهای نظامی و انتظامی با سلاح‌های سنگین در شهرهای مختلف کردنشین منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78405" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o8bpBsuG4tGNoekt07UpehtKXkoiuCmV1b179D6i69iTlEEV2j56RpdhoO-b9wRaR5CmQzG5s2gvH6arPMSv2u5LJoh4VNGef5wZQoA74A7ZgC72pPeqZr3dH8FApyr-J6i7YkZYIP-Omguud92wj3sXdWuyNJ8LgshhBEM3HHrOpLHFCsK5O1nAx1ErQET7Akt1P9RTUjP4S70vWZ8sQlqRYxdTWmG4Z1bUnAE51UJpeDDL0YRu8GKprZzFmNQlVqxrakGCsItxJu5NAIu6lC5bQcGrJD3G1HfeaSb2ZWDbS09l5I-d33qb8lGTMHjv1rkbg877rA861RDHqg_ntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J3fu9_g0SkAkwEsK56n64SwazdFZwascDO72jpNfF-H6c57BNw9zuwMXQe2jyUTMLed_p-dl9XCL3l4yC1SC-YYovtpFrBn_U1gwW24SYcJxlaD6TkhYcpe_Xl_lxaT6iVvxgMlhXsX03k2brB3i9G0rvZoV1_OlnhhoVS-XAPgt3MfTCCepg5Vs4K9RnIlzIVrrzMVw4uTOCw0xNGGldHVrrXapPeWjul0OAW3nZgqggyLsqoNH9hNtXQ5Xnq9aZfUXZz2X-TBqwtjI-LitcrWTHqpqJ0FFAZFoUnGigCKlDVdIkI5hJHBQhL6aT0g9k9Ne3zTGrNYoBbaWE6PicQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QW9n2n14WICaJ-SExho0lPyREKQP3yXyw2q9K_M_cC8ogK9Nf3J2Xliqa_ved63sywxhuW4hdkgQ7VNCvsLIuFmO8WLNnuUU_SzNLQEPv_mIp_Ch_OKaO6RsuCNhaYakPsIW0lB68WrRLHbtsHRqo2ZCuDXR1payA3lP045fvFkx33p2bP5edTQSvDssqmL6SHDCPgDxzCDHdbHaxDTdeWyAmmyw8jNL5T844duQahitOmrSvRqnA1hatPNGRhtDiwsjlxqhXl1IldlYjhICcHEIsEFrtf8tMUMaXgd1ZOmX474YVUFgCv10XTBV5MKLgDPqzmt9FfFCT4UFwPicTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G-XkkQCvqucW9GbB7R8NK78TAmSKLG7O6KFC3D97u-uDsb9fv6V-WC8r7RawKiNkY9WLzPQ4l0XFj1_TM-kAnQw9X0oYkGaGhQfav62yMF_qdfEUXP6px-VZcgXtgmME1Q9yPTGr1RZSH5qibLhnicXrPn1QkuZAfF5IOf71_bj1cDodCjz3GZWjVCGfVCiJR1vfkT5PbFCQcOnznQpW4777vEbxDh0qfYCFSjoALe8_fPCtK9FtF8B51Zhdj9SoBIT0ZX9CYm2g90mw_yczLoZCe0cX-mzKD0gh5Cl3ucEARqqIYvcOePG7kXV2UelfcdLh0wCScDvTO8AczPL4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SYVLkbhDvlht3lafAMptEzjYvUrINoEYamB16An0dnMhy7zh2hDdgLyzVGfvO8nZc4uW9kUwf4Ca-o9QHz_XYT_Rb79EMfSAewFz_s7XmSYlvooaNt8eMzWYFwmH3OgqwlgrZu216SHVwNteKHyvMNGevK4O9o4n4E-tYmd6gTXibGS1LThSGMwUykYcDrfGuRNbQijm1HSjdidk1DZu0DQ6sYnTjh_CExb8fSM74y4DoBs41XYQBvfMDSNUm31ELNuVl9xxy3JgyrDgyuWXyZSOHkKyX8H7iXTtpWf2rtnN5m9R8cBlnZBP6UrvhsTunAO1UalikO4KOyLQ-4HUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ib839oqMrvoKzHYZMAYH7IcWoU7edtTIP-avOwFYp_9MuBeaUrdnwACcgnKo4fLJ16wHzxYdxaBleXZqBcXOWC396RyHCWsDHDDCM230y0FA8iLwY11OfEMNQqod0jSQYNbEW237FIBZR4z-gwOTt9PCI59bUi3miNacIBcRgNckRKgrdjd-TeEvmyKIzOPeONzYUzT1HFSOW_EGGxKP13Y7k4zc8Q2NCRUTeb725UmF4k3BWEK_V7AYbueEFCarTdXVLY4ibWXjKV7pG6g8mOLnVJH0Bh6Xg-5tj0F3P3cNINg1pHyZYuEnf8znySTFVV_VxB8nyaZ5R_XXL8oYJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌بی‌اس‌نیوز گزارش داد تصاویر جدیدی که به‌طور اختصاصی به دست آورده، برای نخستین بار گستردگی خسارت حملات موشکی و پهپادی جمهوری اسلامی به چند موضع نظامی آمریکا در خاورمیانه را نشان می‌دهد.
این تصاویر را نظامیان آمریکایی در اختیار سی‌بی‌اس‌نیوز قرار داده‌اند. یکی از آنها گفت خسارت گسترده به پایگاه‌های آمریکا به اطلاع مردم این کشور نرسیده است.
در تصویری از پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای چهارموتوره بویینگ ای-۳ سنتری دیده می‌شود که موشک به بخش عقبی آن اصابت کرده و دم هواپیما از بدنه سوخته جدا شده است.
تصاویر دیگری از این پایگاه، ساختمان‌ها و آسایشگاه‌هایی را نشان می‌دهند که بخش‌های داخلی آنها تخریب شده است.
سی‌بی‌اس‌نیوز همچنین از ثبت خسارت‌های مشابه در کمپ بوهرینگ در کویت خبر داد؛ پایگاهی که محل استقرار و آماده‌سازی نیروهای زمینی، خودروهای زرهی و شماری از هواپیماهای ارتش آمریکاست.
پنتاگون به درخواست سی‌بی‌اس‌نیوز برای اظهارنظر درباره این گزارش پاسخ نداد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCTt8rRu9s0eA-nxYRGJnRHrJWOZ94f5v1dU00YRyFEO_lFg52nNEl_5CzTIT7kkAOuPlavXvelI9dYqKoDPIOEEe3r4mWOrIJcfcyVHihm1PI7c-QRxdHY4qMqosMts7FbhyNUGKCh4OaNWvNgivUVyJfdSvpgCnUuOAgWyd6xUNsdejPQ6WgTJAB0TsxVRYIyDIKv8Q9DObt69Grxu49zI1fxXoPqkBX0TdEaA7vyrIAD23_AWFTVwxcZcDpa_Rracn44I99OKgUgHrnbwZ7BTVrgEkVpsdZ-vfTcdUfT74-RY_7tApfP_hZNt-SescVW1rWP4b7f6u32BXnI1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد پدافند هوایی این ائتلاف یک فروند پهپاد پرتاب‌شده از سوی حوثی‌ها را که قصد ورود به حریم هوایی مکه را داشت، رهگیری و منهدم کرده است.
به گزارش خبرگزاری رویترز، ترکی المالکی، سخنگوی ائتلاف، در بیانیه‌ای گفت این دومین تلاش حوثی‌ها برای هدف قرار دادن مکه بوده است.
به گفته ائتلاف، پیش از این نیز حدود ۹ سال قبل یک فروند موشک بالستیک به سوی مکه شلیک شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78398" target="_blank">📅 03:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u327HQZDMXdFKJyrGQD33b1kjcZYOjtEykIenQhfPJGQSiWSPncjmWUgOrOZSEn0afGxK8V1crAcAxoh4SbX29cDKDfM0jOj3jc_hOMToumDcWlVpxK9Xi1U-6voyH-1BgLbykkosZPW1iK7MpUgLyqJi4_noLQ43fCqWqsZSpILZlgkaQgIQHRqhAotmkdZeY3Y41u8FN_YK3_-HqNrtvyU60_8yLlALyeI_t8qrsMO_j5kDBRwxKibSPpRIv71fK15vIZfjtiL6yJMJOc2F-toDnobb_OfrQ8f-c3PeS40QPe4MD8Zsdz3hlYSZQCBP8BNV_cHKkSBzuuvVEjCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو مقام اسرائیلی گزارش داد فرماندهان ارشد نظامی آمریکا، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر هفته گذشته در نشستی محرمانه در آلمان درباره جنگ با جمهوری اسلامی و تنش‌های منطقه گفت‌وگو کردند.
اکسیوس گزارش داد نشست محرمانه فرماندهان نظامی در آلمان به ابتکار برد کوپر، فرمانده سنتکام، برگزار شد.
به گزارش اکسیوس، برد کوپر در نشست محرمانه آلمان، فرماندهان نظامی اسرائیل و کشورهای عربی را در جریان برنامه آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78397" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=B8gjiXCpwbsACtCfjMcBrUwTeVPRmmO9CVklFbeiMkKr0KF1Etj8mKjV0X4YKt6-tuygre4_hC5MqjDFNop-oG7BEzVvCFsr74MmZAxlM-ckNKEqR8nwevLZ9HgjZ-QLNIy7H36Ot5EIqJe7gLAHD2KFGDaQA55QeG_SOVEpAScQRoQtRCa0VgwuhyBcBFZCOiHV6o3jdiX-93-3Wnk_NAeEeWm4_J0N67FLiRoyTSuXsezMqMXA_7OAqxAs5QualZqMK1h8x7GvJU279S729vR20rvFJPWXvRK-NRzRE-c-MTas6Hesl1HGWTFZ2Xgd8l8mIjEv2AeTwX1yFVmskA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=B8gjiXCpwbsACtCfjMcBrUwTeVPRmmO9CVklFbeiMkKr0KF1Etj8mKjV0X4YKt6-tuygre4_hC5MqjDFNop-oG7BEzVvCFsr74MmZAxlM-ckNKEqR8nwevLZ9HgjZ-QLNIy7H36Ot5EIqJe7gLAHD2KFGDaQA55QeG_SOVEpAScQRoQtRCa0VgwuhyBcBFZCOiHV6o3jdiX-93-3Wnk_NAeEeWm4_J0N67FLiRoyTSuXsezMqMXA_7OAqxAs5QualZqMK1h8x7GvJU279S729vR20rvFJPWXvRK-NRzRE-c-MTas6Hesl1HGWTFZ2Xgd8l8mIjEv2AeTwX1yFVmskA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده در جلسه سالانه درباره وضعیت اقتصادی آمریکا و سیستم مالی بین‌المللی با دفاع از سیاست‌های دولت دونالد ترامپ در قبال ایران، گفت رئیس‌جمهوری آمریکا اقدامی را انجام داده که به گفته او، رؤسای‌جمهور پیشین آمریکا سال‌ها از انجام آن خودداری کرده بودند.
اسکات بسنت با اشاره به جمهوری اسلامی گفت: رژیمی که خود را وقف شعار "مرگ بر آمریکا" کرده و به‌دنبال دستیابی به سلاح هسته‌ای برای تحقق همین هدف است، اکنون با سیاستی متفاوت از سوی آمریکا روبه‌رو شده است.
او افزود: تحت رهبری رئیس‌جمهور ترامپ، آمریکا دیگر صرفا در حال مدیریت تهدید ایران نیست؛ ما در حال پایان دادن به آن هستیم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78396" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qriH-sbJPE-UoxQDwPN3-N2RBZ6nSkQW-SwYUIh8_gfGF57Gl26qVGeSQhxPjYFIE_o-LbafHQSY03ydJ7B7clPNAm88TMtcbBtnAjWx5Kf_PgQ-jdlrh4uf1hmZRSNH-uV5dH3Xl6J7nRdSPVSs3B-juR091vqpoM0V8j2ZSnkvq534bd3AeSbaLupXNZuMuyQr1sJL0pItJdB3rlUXTGHKviwFRKeFlslwQgR_s3Tnk_WyHr88NOzXiIkVsNN0z5xRKNw-ckgoxqEx6X1clNwdCPo5FTTTQXWmTRt_GB3_PpejlxbWE0mtRJrbzQNoB11IYuWc5OKNqDIrV2xpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره خبری که تسنیم با شرح
حمله به قایق‌های صیادی
منتشر کرده بود:
وبسایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده روز دوشنبه ۲۳ شهریور ۱۴۰۵، دو قایق کوچک ایرانی را پس از تلاش نیروهای سپاه پاسداران برای تصرف یک پهپاد نیروی دریایی آمریکا در تنگه هرمز منهدم کرده است.
به گزارش اکسیوس، نیروهای سپاه با استفاده از این قایق‌ها تلاش کردند یک شناور بدون‌سرنشین آمریکایی را که برای گشت‌زنی در تنگه هرمز مورد استفاده قرار می‌گیرد، تصرف کنند.
پس از شناسایی این تلاش، یک پهپاد آمریکایی دو موشک به سمت قایق‌ها شلیک کرد که به انهدام آنها و کشته‌شدن بیشتر سرنشینان منجر شد.
تیم هاوکینز، سخنگوی سنتکام، تلاش نیروهای ایرانی برای تصرف شناور آمریکایی را تایید کرد و گفت این قایق‌ها «تلاش کردند یک شناور سطحی بدون‌سرنشین آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام موفق نشدند». او تأکید کرد این شناور همچنان تحت کنترل عملیاتی ارتش آمریکا قرار دارد.
این در حالی است که رسانه‌های ایران حمله به دو قایق را به شکل حمله پهپادی به «قایق‌های صیادی» گزارش کرده‌اند.
به نوشته اکسیوس، این دو قایق در نزدیکی بندر کرگان و جزیره لارک در استان هرمزگان هدف قرار گرفتند و احمد نفیسی، معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، حمله را به ارتش آمریکا نسبت داده و از مفقود شدن شماری از صیادان و آغاز عملیات جست‌وجو و نجات خبر داده است.
این حادثه در شرایطی رخ داده که ارتش آمریکا تلاش می‌کند با افزایش تردد کشتی‌های تجاری در تنگه هرمز، عبور و مرور دریایی در این مسیر را به وضعیت عادی نزدیک کند.
یک مقام آمریکایی به اکسیوس گفت ارتش آمریکا و کشورهای عربی خلیج فارس در ماه‌های اخیر تردد نفتکش‌ها از تنگه را در طول روز نیز آغاز کرده‌اند، در حالی که پیش‌تر این عبورها عمدتا شبانه انجام می‌شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78395" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=XyYrANU3sOg-Y7Ba_UmVw1mHz7vbIUFKZ1MaHoV_pAtEUtB3aE7jaDKsK-nsmr7XAz5M0GNpdRD0260Bq2DJVhmuhRmsvseQGUQAVder-J7KENcx93yc5WSaBMLSWVJXzNuA_tvV1KfRmh3m48opo_rYri4Bmv4gnBBbes-Xw_BgyOXOdmc9LWFeWy0YUQbnD86cfKwb4GkF0EbPSoKj2wSUD8VMQsWmZ2cdftZevsUxWZba-Nm4zyAj6XrbT3uzbmb5DV5fkou2EUTDmTBNkxeQaIs7Ow0iVELBQ4gD_asqFEMAZaJhmtwevc2aZjjF7d1sTNptxN1SNG1kBoxLBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=XyYrANU3sOg-Y7Ba_UmVw1mHz7vbIUFKZ1MaHoV_pAtEUtB3aE7jaDKsK-nsmr7XAz5M0GNpdRD0260Bq2DJVhmuhRmsvseQGUQAVder-J7KENcx93yc5WSaBMLSWVJXzNuA_tvV1KfRmh3m48opo_rYri4Bmv4gnBBbes-Xw_BgyOXOdmc9LWFeWy0YUQbnD86cfKwb4GkF0EbPSoKj2wSUD8VMQsWmZ2cdftZevsUxWZba-Nm4zyAj6XrbT3uzbmb5DV5fkou2EUTDmTBNkxeQaIs7Ow0iVELBQ4gD_asqFEMAZaJhmtwevc2aZjjF7d1sTNptxN1SNG1kBoxLBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیوی منتشرشده در خبرگزاری رکنا، لحظات پراضطراب داخل هواپیمای بوئینگ ۷۳۷ شرکت سپهران را نشان می‌دهد که دوشنبه ۲۳ شهریور پس از برخاستن از فرودگاه مشهد به مقصد کرمانشاه، با ترکیدگی لاستیک مواجه شد و با گزارش آسیب به موتور، مجبور شد به فرودگاه مشهد بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78394" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oQxsHWL-tpngHT75cggZx4-R7rxNOgrTNgctWJgtjC90QFDYPFr5PNixZ4qqIOsfuSb1tTacOjQPbNbbfQ9NupzC_l4URwpUe9AjJyuYr9pdAC8t3HXHURVvFpmpX3u03JBLP-XaFvYqa_Y65Fo9ihdqkg68b3NA4Y1RW9n66PKvGTVKzYSWB9fB-IRW9XcINDceyBUUzDeC1tQNlmu8PibZXvQk1YBSPhM0KIRvnjaE_7amQ77_gGB3Ta0sZMq-uAzmWhd-pRnKiQBpxAuV6oC9ouLPTNl5JNjl1YVDDHj1AkOxzY5Ea87SkNg8T4ltlrAS78fLABOvNfC3GIVzZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل دادگستری روز سه‌شنبه ۲۴ شهریورماه با انتشار پیامی در اکس، از تشکیل پرونده کیفری برای رضا درمیشیان، کارگردان سینما و تئاتر ایران خبر داد.
به گفته رئیسیان، سپاه با شکایت از رضا درمیشیان  به اتهام تبلیغ علیه نظام پرونده قضایی تشکیل داده رسیدگی به شکایت از او در شعبه هفتم دادگاه انقلاب تهران در جریان  است.»
رئیسیان با اعلام این خبر گفت در دادسرا برای رضا درمیشیان قرار جلب صادر شده و سپاه پاسداران به عنوان شاکی، تقاضای توقیف اموال او را کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78393" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8g2WC7dtMiHF-2e53yUXQ7yae1qPIk6VWNeQ33g5ZsST70U3nsZGG7RGzM_iby4pXYb5KRh0YW_DZZXKW_QU-U_YjqqfR4Gze2oVIR3GUu08Y1pbBWbRUu2VFqfGlxuRN8oXdpVD2ikV57jn0kIdgDMgGNh24-Ko97UebBXlQyHONM73eBcvAjx8faJsrv3S6ZuvmA0CBuEtaAzehgAxmmWYx4_pal7YXcO5pdUWR0EhPjBGA7bqjjyC6S2pSXAvfQ_YE2K1Sy0uyz9PO_aslfwRL50wT4jKRV2ZcTApB3tHZFcRDt3tu3oofQP_03EcmY67V9oYTuuDcHaBcPCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استودیوی «کارگاه» با انتشار عکسی از آزادی «آریا کسایی»، طراح گرافیک و یکی از بنیان‌گذاران این استودیو، پس از نزدیک به دوماه بازداشت خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78392" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jUnRaspD8TAcJdPbWNnXXN2c2BzWKxmifn9Nez3mty1lZp2YU7IvTagCayS-C-UwfwJXFA_s-Hr50TUrhu5zga7Y-_Ctp7dWaz3hjtCUvq4m4ShvsptplZqrdXknRBppV2NPM6fLkwWeQdsRjqjTZMGDQAkkxmplD9TWnx1luk5b29FgQKiL8L73nEKbsq_9YI1j8QVkHrwBALRvVUtMWDXzmhhtVw7SjuEnCZ2qRKdfJhcAOrZAh3iI0AEKdg_qH3r4p6vAMALlzNF0BM80P-aB46h3wuoa8BjLiVQDh7bmp_j_xBgzjWpqLEb7q-GTMN87TY5JY1jG-azP8ydwLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس تهران می‌گوید فردی را بازداشت کرده است که شامگاه دوشنبه ۲۳ شهریور به سمت «جمعیت حاضر» در میدان پونک تهران سه کوکتل مولوتوف پرتاب کرده بود.
میدان پونک از جمله میدان‌های تهران است که از زمان آغاز جنگ ۴۰ روزه تجمعات شبانهٔ حکومتی در آن برگزار می‌شود.
بر اساس بیانیه‌ای که فرماندهی نیروی انتظامی تهران منتشر کرده، «این فرد حوالی ساعت ۲۱:۳۰ از بالای ساختمانی به سمت جمعیت سه کوکتل مولوتوف پرتاب کرده و پس از آن گریخته است».
در این بیانیه ادعا شده که این فرد «قصد خروج غیرقانونی از مرزهای غربی کشور داشته اما ماموران با شلیک گلوله از ناحیه پای راست او را دستگیر و به بیمارستان منتقل کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78391" target="_blank">📅 15:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lfg8SIejLeLyJijLzYPXDWkpXcCqr7cScWWCCRaXz97W6algzZeqD3p4wLSZAFF9H08QUPMEpQESUjc21I9Q8SVlkmrggdu9NjkqkSUfsLMNXxcQmTMtyJTZO6A6K0Tczr6Dod4D2tysysIWrz56ckR0c6GikFA6DYV2FKan4ua7D7o8I0N9C0WW9Oni1aW0SpuBidV6wFkm5fkvFeOmekxREkMTk4tl8DzFio2dbB6br7az4RO-rjieEhVCyRGka4C3PMgwu20b8LnDv-aVKsXKBvhiHBolIyPsWpAN65_4lI89u8hOAhKnSD4Dmvz_V4T2nLyFsu-pkdpGV3MQsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش رسمی آمریکا از هزینه‌ها و خسارت‌های جنگ با ایران منتشر شد
یک گزارش رسمی نهادهای نظارتی دولت آمریکا می‌گوید جنگ با ایران به «کمبودهای راهبردی» در ذخایر برخی تسلیحات پیشرفتهٔ ایالات متحده منجر شده است.
نخستین گزارش رسمی نهادهای بازرسی دولت آمریکا دربارهٔ عملیات «خشم حماسی» که روز دوشنبه ۲۳ شهریور به‌طور عمومی منتشر شد، می‌گوید مصرف گستردهٔ تسلیحات در جنگ با ایران «به کمبودهای راهبردی در موجودی‌ها منجر شده و گلوگاه‌های پایهٔ صنعتی برای تأمین مجدد مهمات را آشکار کرده است».
بر اساس این ارزیابی، پنتاگون برای مقابله با این مشکل در تلاش است روند خرید تسلیحات و زمان تولید را کاهش دهد و ذخایر مواد و قطعات حیاتی و برخی مهمات را افزایش دهد تا در شرایط اضطراری امکان افزایش سریع تولید وجود داشته باشد.
این گزارش همچنین نشان می‌دهد آمریکا تا ۲۹ ژوئن (۸ تیر) حدود ۳۳ میلیارد و ۴۰۰ میلیون دلار برای جنگ هزینه کرده است. نزدیک به دو سوم این مبلغ مربوط به مهمات مصرف‌شده بوده و ۳ میلیارد و ۷۰۰ میلیون دلار به تجهیزات از دست‌رفته اختصاص داشته است. بر اساس این گزارش، ۷ میلیارد و ۴۰۰ میلیون دلار دیگر نیز در ردیف سایر هزینه‌ها قرار گرفته است.
پیت هگست، وزیر دفاع آمریکا، اواخر ژوئیه (اوایل مرداد) هزینهٔ جنگ تا آن زمان را ۳۷ میلیارد و ۵۰۰ میلیون دلار اعلام کرده بود. شبکهٔ ان‌بی‌سی نیوز نیز پیشتر به نقل از مقام‌ها و افراد مطلع از برآوردهای داخلی گزارش داده بود که با احتساب هزینه‌های گسترده‌تر، رقم واقعی جنگ می‌تواند به ۸۰ تا ۱۰۰ میلیارد دلار رسیده باشد.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه و همزمان با انتشار گزارش ارزیابی «عملیات خشم حماسی»، در شبکهٔ اجتماعی تروث سوشال نوشت آمریکا اکنون بیش از هر زمان دیگری در تاریخ خود تسلیحات پیشرفته تولید می‌کند و این تجهیزات به‌طور روزانه در اختیار نیروهای آمریکایی در خاورمیانه و دیگر مناطق قرار می‌گیرند
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78390" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJzf1jzKMOVO2LcgykCjyzsGOOfPVmcRzYQ6nSkKU4irgQJvsTUv7oUTtG7gDKDu5xsvIuzZauYodtlqPM9ZHGhSL02IspkO4bDaSKDcJYJLe7ke-gM3qE7EELfX73Jf7HTkPkd4DyZtm24MKOkNedE9yBSReB2gI031s6u-CkLPZniJaMC50HA9VZO3WfLaHib2guc-I80cYw1uJd0CIFLJu6XZNQRXatnlh7q6qGCYwZdOGVVPVjsXN012i_0SwW8DH-clPljoIAvm_3bRhQg0rmm5xL1-fFZp-6g1_pgbB44ZPqOD3rwH_ddUDKm8MFsdlAsrMgVe-4sE2V46Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژه امنیتی با نام «علاج» با انتشار اطلاعات شخصی شماری از ایرانیان خارج از کشور، از شهروندان خواسته است افراد بیشتری را شناسایی و به این سامانه گزارش کنند. صداوسیمای جمهوری اسلامی نیز به تبلیغ این پروژه پرداخته؛ پروژه‌ای که مشخص نیست چه نهاد امنیتی یا حکومتی آن را اداره می‌کند و اطلاعات هویتی منتشرشده در آن از چه طریقی به دست آمده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78389" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o79EtWMfjS84bhrUxHr7K-ye3glhMY5Zsw91fwkKrSC0R4oo_UQ-gxqJ-wKLgGljEAE2dE9Iy4Iv9rKV_-z9XDF52U0nGJk3HcvCUSjk0Zn-R5moSKlk1wqE0wR8Xqut0-_tPMCXMd4xpDC5uY0XjOjqt5Uho__oLbHaZwJtH7vkAaqrZQJwf8PQiRMWb16SvntXFEpQ2A2ApLzk2pCCK-KrDjzZ5NYZzM-4xZ_Y34r_9XsBnlMM68t947YIwreaLy4T4Os-3u8tRU-XxGUP-LZ-7nm3eEd2eRHKcPX0zBRI2C2YTrgTGtKnWYUOxXf5JBCophv4A2ZyzktUVXh1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZCkZXGkKgKR8nru0W5JQhSJSqoGZ8p5zY4y4pDcTZMtcRqdzUvFEl9tEqduwJJV-w473_WVfaRe3PueLt3AqfBeY9gQV4YrVXvKTa6ExO-aLTk2yHJKo9d1krOlv4dzP862J53sp0fi7cvAAvv1-H91rn6gkD8qMK2zaSSFIJmNmoVPR3Wcua1KlzCIKJRDMfL5SitAMEZFoHmneC_nfH1Vwe-pDlfwzQyEW880GSs5j54APPh7qyy8E6oLHbZANig31nyulQlE4IpcKNduhqt91_gP9VZDZMBeNquxps34m170MEpPzyeODvXGYPY3TpRLa2N5gZKS3BVQIxdFW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QnlTR-86HBAYgq-qJdwrB3tfuGKOHR4D-BqIYaCbadQb3nhK5CN9paQhA969tGnVCxEKLDKF9b19Ac2EcvF-gfaPU1zp5R8chG4YeSIMnggX9UYQzLEOg57WhLvKmDQ3jtWpCiQ4fVcfM35HnH46MX_RMyEEN_WSwYb4Y49iqRoRp_0mOx2Nx9OENYGfKYdegRlbwxljf367QV-cxMj59qIU3MHsjPnvvGw_saMUReOolyHvJo--qsJV_K_5V-lfcFcxBebitBR5dRC0mO3GGs8c-3Zcxn6dX05yGWfSBD9pfjBuITjs0qFwpLKb7DFIsNs_sUhd5zyWzjrSA639CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MyA_pjZJ18_2AK2AVIFga8tAAjzQhDxNrGG7Z6AxE5jnG6JVSXyZBWfvOIpEFJO_OOASK1celMYcXlx4XxmuVqP6eA3RQVEYW9SKr5T6QmVImjhOCFQrZajgGKsXTz9I99LxiZUIOAEU7RutSNZkdhdRkbCbaaVuVAqo5OOLlgDUW7luaO93GqGPvhwxlbD76O2aJqUCrqw6iDsE2U2IC_CNryDcn_LXChdyL8C3bxZqHtxG_Ue_OB34Ru5Drwma1zSGzCsq-e9MbP7GKDUFkvY0bBRdvM9CJDEMHug57L9AaZqgosTkxOxLREEJTfSpl9Gs4DUlYj1AnE9RjEdYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gpp4_0u-grIL-YDDS1kDDmnOTdgt05OEEOyqpvBNS814E-GrmzkJK9EfZHaXLdsAmj_ginzA_AkXTbold0uKsK3P2xMTIb4jpQ_4Y_FjLyzX13NW4X2BMYNuTJkwm-8frC662-aKo9Ff_hUIuYlH8xXJSfpc4rlrJrBcMJvH-1kVHdOIVUhZywHYAsMEQD8CNLUoc_CGBkO99WngolWJpTKsqeRilNJbUO6WtMpKDHN7IRRmDEdaP7d3Tf_DA-CUYjFrl8PKwlQTvtjI0ckzSjq8KR8G9lxPvxVNiH358MOuvq-vbFDelD3d8vc0Aq0tzad0x3oSM0eV-EyVyW-sMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L97YaGH7nndEwf72V4uE_jg4vpbZ8nIm_kzuf2BIcyWi06bGM8q9L397ISLWIe8t20KDK00xynPaW36Bs4pgHE9k5_9OL2NaYlHwtFUnjn-bIdlkT3Sy0YGsZ28yCfh9bDyFHOdoOkDIxCuvnxwu4pItCm2JjwFTr4GdK9W45NSoG3lUvabjGaD-gSwHo9eOjRuIlpUEiDJyZtnbbDZ7rRLRkUa9Oey4fXuLLagD1jN3cpt0YV2tOpW2N4Y6c7Rg_8LqWNBonBVSRdpcnWjjq6DeFbOJfgUw6OdsMfgBnGVlpcCqJdMVJ7hUkbbzVHIwM9EgISywhTuJ2IDf8sPm9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«پویش جان‌فدا»، کارزاری وابسته به نهادهای تبلیغاتی سپاه پاسداران، ارسال پیامک برای ثبت‌نام شهروندان در دوره‌های «آموزش نظامی و امدادی» و سازماندهی آن‌ها در قالب «گردان‌های مردمی» را آغاز کرده است.
در پیامکی که برای شماری از شهروندان ارسال شده از مخاطبان خواسته شده از ساعت ۱۷ سه‌شنبه ۲۴شهریور برای شرکت در «دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جان‌فدا» ثبت‌نام کنند.
پویش «جان‌فدا» از ۸فروردین۱۴۰۵ با محوریت «قرارگاه فرهنگی و اجتماعی قرب بقیه‌الله»، از نهادهای وابسته به سپاه پاسداران، راه‌اندازی شد. سامانه‌های اینترنتی، پیامکی، تلفنی و ثبت‌نام حضوری برای جذب افراد بالای ۱۲ سال در این پویش در نظر گرفته شده بود.
@
VahidHeadline
دیروز کلی پیام دریافت کرده بودم از شهروندانی که می‌گفتند در این پویش ثبت‌نام نکرده‌اند ولی اون پیامک براشون ارسال شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78383" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI9C6st8xe5lLKbEw_r1jZZTbbnv6Vvowec_SWeOpu26VrKXP5Ev--6412CgjE9mgu-Lq1DDmk92eMzMVw_WZTzihu4Jp9VN55-nlCrNFyw50nmRA8R1NaP_VKFzIN5jMf1yam8QSEPJhAozFfDkehY2DxmarAGlmiTLmB6Symxj4n7WPbuYN4Av7LJwxGvgk95r7qZNG_pUQZrfxbgOJiXpziN2M3Q9o8LzduT2wtq0s5aYn8XJm5fyBdSNpcS0-zBEKfy2MnueBiIZEBfuhvWLqNGYUB1iOp4CGbWTWLLha2xGewt0GMX5zndFoJAXZ9pOEDgztlV5W19zu3z00g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دادگاه فدرال آمریکا روز دوشنبه، ۲۳ شهریورماه، به عدم اجرای دستور دولت دونالد ترامپ برای محدود کردن مدت اقامت دانشجویان و خبرنگاران خارجی در ایالات متحده حکم داد.
‌این دستور که به گفته قاضی دادگاه به دلیل «استدلال‌های بسیار ضعیف» دولت صادر شده، قرار بود روز سه‌شنبه به دست وزارت امنیت داخلی آمریکا اجرا شود.
‌بر اساس قانونی که دولت ترامپ سعی دارد به اجرا بگذارد، روادید دانشجویان خارجی و روادید افرادی که با برنامه‌های فرهنگی در آمریکا اقامت می‌گیرند، به چهار سال محدود می‌شود.
‌این قانون همچنین می‌گوید که روادید خبرنگاران نیز نباید از ۲۴۰ روز فراتر رود.
‌هر سه گروه، بر اساس قانونی که اکنون دادگاه جلو اجرای آن را گرفته، برای اقامت بیشتر باید بار دیگر اقدام کرده و روادید خود را تمدید کنند.
‌به گفته قاضی دادگاه فدرال، اجرای قانون جدید تعداد دانشجویان خارجی و روزنامه‌نگاران و خبرنگاران در ایالات متحده را به شکل قابل توجهی «محدود خواهد کرد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/78382" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1AEgEUI8VLZ-g24yGzpzlQjWu-7Av0NWsyqoVySUQEFuOseNz03W1XBp6yT2Dc1PS6T7koVDBHokput_h5SZ7lPChvHrD6MzA3WzZnAzseDnNrUJ5BJGWTCwhG65z8-I4WZbI-xPEYlgC1AmDM_rxPU5na9u-x75Z7ZUc1B8_VuathGU0dddZeuD2qeqw9obmt6HdpXrhrmotpbaE2t4FVLOn6Za8vy0hq9MtQCc360LqRv4NPxqPaVguZIXBth8UtbvgO24pxeupypjClCIfAPPhDpuJfZfKek1fAiVZzBseFGAm2zAj6x44gn9X9aQ6Bk_zeRjZZHC4Fr29I7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه اتریش اعلام کرد برای سفر محمد اسلامی، رئیس سازمان انرژی اتمی جمهوری اسلامی، درخواست معافیت از ممنوعیت سفر سازمان ملل داده بود، اما درخواست رد شد.
بنابر اعلام این وزارتخانه، رئیس شورای امنیت سازمان ملل به وین اطلاع داد که درخواست به دلیل نبود اجماع رد شده است.
وزارت امور خارجه اتریش افزود با توجه به تعهدات بین‌المللی این کشور، ورود اسلامی امکان‌پذیر نیست.
اسلامی در راه وین برای شرکت در کنفرانس عمومی سالانه آژانس بین‌المللی انرژی اتمی بود که اجازه حضور پیدا نکرد. او از سال ۲۰۲۱ در همه کنفرانس‌های عمومی آژانس شرکت کرده بود.
ممنوعیت سفر از سازوکار «اسنپ‌بک» ناشی می‌شود که تحریم‌های سازمان ملل علیه جمهوری اسلامی را بازگرداند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/78381" target="_blank">📅 15:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mIqYDapOfIzQrbt5aaJYH8BT7EV7oRNlcN1Imf1wKHAHOlU-XXlwVhn10d7ZlxhYrgTtEu_WfKecbB4j-jc64GZuACmqQ5bVynYdZ8QAASFkd5pAoT2YEDyxbSO52iVObjUYPcT3YQDnisYy34oUT_vBB-n9ytcb305RI7rKk1p90EO2RShQWmkDrrnw5f5JBeRagqnHHGlvKNnXjOqShizYnyVi7BjSJ3R5XkwiR053xpTwoe1_TsIOZ1RevXo3LyefD-btLbAQp5563q_FDDNQYqIP1RD4Y9hDfN2C_dMke72MxGh7kn6s0W6uG2cJNoOuth_6wNt99loJhnfy0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش الغایا پس از حمله در سواحل عمان و آتش‌سوزی در موتورخانه، به یکی از بنادر این کشور یدک‌کشی می‌شود.
بر پایه گزارش رویترز به نقل از مقام‌های عمانی، ۲۳ خدمه از شناور تخلیه شده‌اند و دو نفر همچنان مفقودند.
روایت‌ها درباره علت حادثه متناقض است.
سپاه پاسداران اعلام کرد الغایا با پرچم پاناما هنگام عبور از «منطقه ممنوعه» جنوب تنگه هرمز با مین دریایی برخورد کرده است.
فرماندهی مرکزی آمریکا ادعا را نادرست خواند و گفت شناور «ماه گذشته با موشک ایرانی زده شد و از کار افتاد».
سازمان بین‌المللی دریانوردی گزارش داده بود الغایا روز شنبه آسیب دید، بدون آنکه علت را مشخص کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/78380" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/godzZbBImqo6WPqUMhCs70pjrrtxyasv9FVidmh6YRKG_FzaG-k3FNaSZEWXp1_5zhOWlUbpqReYrCssCC1m_o1lV7amsVv5JIa5Cp009oraBagnfVHPd2jENEJ3kc6N953wNEiPOKuR4mH35AEu9pWcAtP4sHrgOC2nZF03VYoH4QowO6fZqBjL7FV3-TfTXzAUhl98RTA1G0QK4WbLtxPO2tIuC8y3OBBy8Vqy1P9T0V0tyqVQ6uFnWGroU808SFc-wy-OwghKi1MFyCr7Tn2blyi5suJ94kMeSYGXRfY4fiRAlfR5-VGu0DQIhW4aLbfmJ_5tBP0YM4D5RhdOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۱۰۰ معترض در ۱۳ استان ایران در خطر اعدام هستند
سازمان "حقوق بشر ایران" اعلام کرد دست‌کم ۱۰۰ نفر از بازداشت‌شدگان اعتراضات دی‌ماه در ۱۳ استان ایران با حکم اعدام روبه‌رو هستند؛ بیشترین شمار این افراد با ۴۶ نفر مربوط به استان اصفهان است.
بر اساس فهرست منتشرشده، پس از اصفهان، ۲۲ نفر در استان‌های تهران و البرز قرار دارند.
همچنین ۱۰ نفر در فارس، هفت نفر در خراسان رضوی، پنج نفر در مرکزی، سه نفر در یزد و دو نفر در سمنان در این فهرست ثبت شده‌اند. در استان‌های خراسان شمالی، گیلان، اردبیل، ایلام و قزوین نیز هر کدام یک نفر با حکم اعدام روبه‌رو است.
این سازمان می‌گوید فهرست منتشرشده تنها شامل معترضانی است که دست‌کم در مرحله بدوی حکم اعدام دریافت کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78379" target="_blank">📅 15:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tu4SyaxjkMSpj4MKlegmcxa5AO2pY00cBx4LKtieb02T69o7E1zpAhoG8OSlS7sZBNccxjp6gEiBAx8nZhzOLP1jccmcLEi4Ms-pYMvkP56FbhdUUhEn-pUoqD0a5Tnghzfgc9GHGVrgngFkd3XnULwToX3daxmm78iStvw_RI5Uqh15S6qI84Ha_Wup2hmuMM1Lg1-FJQG0TnnFxy_9XX2dfhb9wAT-uoYoTQ4vcG5CHfNM8xqzl5SoWFzH3PjBJ9BfEOU7fvXlTdr5eFMwXydoj_rleNtq310njlRCpxm0tzr36nznafvZ1JfMogjkMg6dv4EXcxgKmf6Hys6zeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، شامگاه دوشنبه ۲۳ شهریور ۱۴۰۵، از حمله پهپادی به دو «قایق صیادی» در حوالی بندر کرگان در آب‌های خلیج فارس خبر داد.
بر اساس این گزارش، در پی این حمله که تسنیم آن را به «آمریکا» نسبت داده، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند.
عملیات جست‌وجو و امداد رسانی برای یافتن مفقود شدگان آغاز شده و نیروهای امدادی و دستگاه‌های مسوول در محدوده حادثه در حال جست‌وجو و نجات هستند.
تسنیم نوشته است جزییات بیشتر درباره این حادثه و وضعیت صیادان پس از دریافت گزارش‌های رسمی اعلام خواهد شد.
@
VahidHeadline
آپدیت:
اکسیوس: آمریکا دو قایق سپاه پاسداران را منهدم کرد
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78378" target="_blank">📅 03:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gTJAlSkyuUcB867PDklV2XoNnJCxHhKeNcp5yY__NRP8K4bjTQDZ4Xnq_JNAaQFW-iUJmXyYFzoWT98h48miX9lo_oirFnpd-Y3q2rxUP5jpQIbSk27JYwwpuSp3R6za-SX5olCuqZs-sa4nDJv2yXpip0ZN3kPCP1JV15ULBV5vrAosMZj5Pz2WG5uiwqajSNi8oY-MAElskMf1TebjlXlayNggPEcqJ2g_zInU0jU4f-Zn3CXdQ6LJLclz9QrSJ3aTpGi_xWbyYvbspf9_WURKa3yx2T5hGOU8OqL6O8vLEPZAqXCdyi67cP7Gp367xMpyvBkrOfULfVeGWHRqvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی نیروی دریایی سپاه می‌گوید یک ابرنفتکش که به گفتهٔ آن قصد عبور از «منطقهٔ ممنوعه در جنوب تنگهٔ هرمز» را داشت، «بر اثر برخورد با مین دریایی منفجر شد».
خبرگزاری‌های ایران شامگاه دوشنبه ۲۳ شهریور با انتشار بیانیه سپاه، نام این ابرنفتکش را «اِل گایا» به شماره دریانوردی «۹۳۲۵۳۳۶» اعلام کرده و افزودند که «تلاش برای مهار آتش بی‌نتیجه بوده و کل نفتکش در شعله‌های آتش گرفتار شده است».
فرماندهی مرکزی آمریکا (سنتکام) این ادعا را «نادرست» خوانده و گفته که نفتکش «اِل‌ گایا» که با پرچم پاناما حرکت می‌کرد، ماه گذشته هدف موشک ایران قرار گرفت و از کار افتاد.
@
VahidHeadline
پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است یک نفتکش با پرچم پاناما اخیراً در تنگه هرمز با یک مین دریایی برخورد کرده است. این ادعا کذب است.
✅
واقعیت: نفتکش «El Gaia» با پرچم پاناما ماه گذشته هدف یک موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، ایران بار دیگر این نفتکش را در حالی که در آب‌های ساحلی عمان قرار داشت، با یک پهپاد هدف قرار داد. این نفتکش در حال حاضر توسط یکی از شرکای منطقه‌ای یدک‌کش می‌شود.
ادعای کذب سپاه پاسداران نمونه دیگری از دروغ‌ها و تلاش‌های آن برای ارعاب است؛ آن هم در حالی که می‌کوشد مانع تردد کشتی‌های تجاری در تنگه شود
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78377" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S0uKcC-hqjS6JaLP6wHLxvGdcGR4VaUvfJHIo2QZulHo8g4ihvzYrpAIBOaEjfdGwVqvUv2IKeg_rMr1IMc5aZuYR2vKgNAKpnkmKNULOTJValcG9_uovHqoILWNkF5Z-UkWt9SZjjGx1jWWpDVD_baicS6jQrymRsPoDUarQBtuu_9vPjZzwDKK3kv0v47Zlb9DRZaTQeygEyCRMzCe0_-F4OJQ4JUE5TH942uEOU0xXHqtT_YMHeHJsqUK4YvzWJGzYj6go26Fh3cwh6n7A_NQ856BkpO4rQwiskguQ2ocxoAavZubJZ2lqC2Ie9THNvECU9GQ4XQBaNFUWG-naQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vpyoZ0OdM20vfDv0A1PgzB7b5XxZ9WqWC2AqeYmJWDHtJ-1Z2uTZy3dfCeaBAhtWWz-q4dMZtk9vdhloxyyL2MSd_bWunh53Ixy-Gaz9X5Gjg1wVR0RmWdzYpQINIqPOHx-rx5vnTYvezHwYbXf93X-eB62XEcORXy6GcAkkN0tkoGjeHVW7AfgRGeLPFZR-qtD6av2Mu5zMcd1XmHC2AyReB7K0JNQ2VV1q03sZK1AmPvuxzhxbGolwsJnLwbe9uKXqO9qrFd1S9cqPU3VG2JWZBJeMMM7Ki9iLndKveWQxFhSRe47dAIlZ_nQG1MsIHfU6aft4LwOzTeJ0uc2mxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پیامی در شبکه اجتماعی تروث سوشال تاکید کرد که افزایش قیمت‌ها در سراسر آمریکا ناشی از سیاست‌های جو بایدن و دولت او بوده است.
او نوشت که حتی بهای نفت نیز در دوران بایدن بالاتر از سطح کنونی بوده و دولت او مانع از دستیابی جمهوری اسلامی ایران به سلاح هسته‌ای نیز شده است.
ترامپ با اشاره به اینکه قیمت سایر کالاها به شدت در حال کاهش است، افزود که بهای نفت نیز به محض پایان یافتن درگیری نظامی با ایران—که به گفته وی زمان زیادی تا آن باقی نمانده است—مانند یک سنگ سقوط خواهد کرد.
در دوران ریاست‌جمهوری بایدن، به‌دنبال وقوع جنگ روسیه و اوکراین و بحران‌های بازار انرژی، قیمت نفت در بهار ۲۰۲۲ به بالاترین سطح خود رسید؛ به طوری که قیمت نفت برنت تا حدود ۱۲۷ دلار برای هر بشکه افزایش یافت.
@
VahidOOnLine
رئیس‌جمهور آمریکا در شبکه اجتماعی تروث سوشال از کشورهای جهان خواست پس از پایان درگیری‌ها، هزینه‌های ایالات متحده را برای حمایت از کشتی‌ها و کمک به عبور محموله‌های نفتی از تنگه هرمز بازگردانند.
ترامپ با اشاره به اینکه نفت در حال عبور از این آبراه است، تاکید کرد کشورهایی که هیچ کمکی به آمریکا نکرده‌اند، باید خسارات و هزینه‌های این اقدامات را جبران کنند؛ زیرا واشنگتن این ماموریت را بیشتر به نفع دیگران انجام می‌دهد تا خودش.
پیش‌تر کریس رایت، وزیر انرژی آمریکا، اعلام کرده بود میانگین تعداد محموله‌های نفتی که با حمایت نیروی دریایی این کشور از تنگه هرمز عبور می‌کنند، رو به افزایش است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78375" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/llwAY2MiD7zA1zAE8DTfHoiL7mu_PSNReJpuxUGaAwGNMFlJGMQ1tJzj8AeL9WhMz1gn6YVbuZTciNxLToE3pnbIgjvReaYLgt98czRHeMo0Hmze7BWyRefKMDh0P-EbsXSOMcD7urZsffYFJNUpOIfGk8YqaDwJwQCnrA0-Vu096vjMO1zFSA6vbi4kcPCWbz33_fOScF3IeEYaKxIPbUAl6lH9jwVZXb0Xzd9-t5gsuLZ40DcMgBYtIiEFG2T0zZS6j1bWPLq9_XR_ICQxdU0biqvxQtKzPmJaMCEuh-zrviUja6sdM_U0b04FhjSlPTQYwcYRheguJROE9yl5qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایرانِ شکست‌خورده می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
من تصمیم خواهم گرفت که آیا ایالات متحده آمریکا وارد مذاکره بشود یا نه — ایده‌ای که نسبت به آن آمادگی داریم. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
ترامپ نوشت: کشور در حال ورشکسته‌شدن ایران می‌خواهد سریع و به‌شدت به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا وارد این داستان خواهد شد یا نه؛ چیزی که ما نسبت به آن نگاه باز داریم.
پس از انتشار این پست قیمت نفت اندکی کاهش یافت.
اظهارنظر اخیر رئیس‌جمهور ایالات متحده در حالی است که ایران گفته برنامه‌ای برای مذاکره با آمریکا ندارد و شروط متعددی را برای توافق با واشینگتن اعلام کرده است.
در همین حال، اسکات بسنت، وزیر خزانه‌داری آمریکا در راستای برنامه فشار اقتصادی بر ایران موسوم به «عملیات طرد اقتصادی» از همه افشاگران خواست تا چنانچه اطلاعاتی درباره «تسهیل‌گران تروریسم ایران» دارند در اختیار وزارتخانه تحت امرش قرار دهند.
او با انتشار پیامی در شبکهٔ اجتماعی ایکس خطاب به کسانی که در سراسر دنیا اطلاعاتی درباره شریان‌های حیاتی اقتصاد ایران دارند، نوشت: «این شانس شماست. اگر اطلاعات قابل پیگیری برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت جایزه باشید، صرف‌نظر از این‌که کجا زندگی می‌کنید یا چه کسی فیش حقوقی شما را امضا می‌کند. اگر چیزی دیدید، بگویید».
او همچنین بار دیگر تاکید کرد که وزارت خزانه‌داری آمریکا عملیات طرد اقتصادی را «برای قطع تمام شریان‌های مالی رژیم ایران و حامیانش» آغاز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78374" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=FzzycOX9p4K8_TbwPz4GxbUtDjn_Bozoot5mZpA87UUeTy0yc7youX1v7uUuXnkVGaAGOhixms25oweqIdtAmHb7RzLvPt1rrlqk1KtlZ5_pcOBbkJ7BPWY9jDNtj7DaYJaO9_OWlsQvt14zskIYrQ0BDyR5fF-j0zj8fOCts0NWLt-5Qhz7sLSwwzvOjiXP64JecopU_p9FGjPREpS9mVOe0Un6B8_hHW48EbLldCME6ATrKJp9r9sBOseDT02wKvPftaM4ISd49vX9an7WHwI6wOCzHfwJ6mcpp6TbjbNSCAe-ErqCFR2WJugJchzWer35aTIYd-lsW81RRUjMOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=FzzycOX9p4K8_TbwPz4GxbUtDjn_Bozoot5mZpA87UUeTy0yc7youX1v7uUuXnkVGaAGOhixms25oweqIdtAmHb7RzLvPt1rrlqk1KtlZ5_pcOBbkJ7BPWY9jDNtj7DaYJaO9_OWlsQvt14zskIYrQ0BDyR5fF-j0zj8fOCts0NWLt-5Qhz7sLSwwzvOjiXP64JecopU_p9FGjPREpS9mVOe0Un6B8_hHW48EbLldCME6ATrKJp9r9sBOseDT02wKvPftaM4ISd49vX9an7WHwI6wOCzHfwJ6mcpp6TbjbNSCAe-ErqCFR2WJugJchzWer35aTIYd-lsW81RRUjMOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رشت، حامیان حکومت شبانه به آشکده سحرخیزان حمله کردند.
در ویدیویی که آشکده سحرخیزان منتشر کرده بود، عبارت "آش برای افراد با حجاب رایگان است"، به دیوار نصب شده بود و در چرخش دوربین، چندین مرد محجبه در صف ایستادند.
همین بهانه‌ای شد برای یورش و تخریب مغازه.
این اتفاق یکشنبه، ۲۲ شهریور ۴۰۵ رخ داد.
دادستان بلافاصله علیه آن اعلام جرم کرد و مدیر رستوران بازداشت و خود رستوران پلمب شد. ولی انگار این واکنش از نظر لباس شخصی‌ها کافی نبود و دیشب ریختن رستوران رو تخریب کردند.
via
pkhwshhal
,
yaghma_fashkham
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdLxaNcarebhYWN46WxRrH21msgkF4Ap1krr5nphkarSVqdcqBMYaKOLISyS6fcTXVP08DMg-eEwZ6V6ZSROu9zE9-BJ0A1AE7qYCD5iDWSplbdWU1cWb9hxFk7JuAG7IPbSHcFAAV7zr2HLdf421xh3tqsTL2YpRgAN5d3eL_C0rAkbAaEY3XgbkabdWtK7MOFqpoSVxCdA4G1AhIv-Ft0PZXv0DOMgeEb2djlWvVyqL8uNRGgKzQGTPKQZjzPrLyJABeDZAhpy-qTGrUR48jvMxvAKf5RaBJk5ZlEST2MGKvErSlFXCv83Zm186Zj73l-UqajT_l_9Ct3vB7W6sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اتهام «بغی» برای محمدپارسا گلچین، دانشجوی دانشگاه تهران و دارندهٔ مدال طلای المپیاد!
بنابر گزارش‌های رسیده به تهران-دانشجو،
#محمدپارسا_گلچین
، دانشجوی ورودی ۱۴۰۳ کارشناسی ادبیات دانشگاه تهران و دارندهٔ مدال طلای المپیاد ادبی، به «عضویت در گروه
باغی
» متهم شده است.
همچنین، «اجتماع و تبانی علیه امنیت داخلی» و «اقدام تبلیغی بر خلاف امنیت ملی» دیگر اتهاماتی‌ست که به این دانشجوی نخبه وارد گشته است. او در جهت دفاع برابر عناوین مذکور، به شعبهٔ ۲۶۸ بازپرسی دادسرای عمومی و انقلاب مشهد احضار شده است.
محمدپارسا گلچین، شنبه ۲۲ فروردین ۱۴۰۵ به همراه جمعی ۱۸ نفره از دانشجویان در جریان یک بازدید دوستانه، توسط مامورین مسلح و به‌طرز خشونت‌آمیزی بازداشت شده بود
. پرونده سایر بازداشت‌شدگان نیز در جریان است و در انتظار دریافت حکم و احضاریه هستند. درصورت دریافت اطلاعات تکمیلی، گزارش پرونده‌های سایر دانشجویان متعاقبا در تهران-دانشجو منتشر خواهد شد.
#سرکوب
#بازداشت
#دانشجوی_زندانی
دانشگاه تهران-دانشجو
اینستاگرام
🆔
@Daneshjo_UT</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=OZntf9UtGpty2RsCEyKFLkRG-GRrpeltLlVkKCSejuLiGCwMKYG0EBOuQ_qSM2myeOvC9r2xZDuWnJ15e-b0Ua7Jm04sVXPQSknUlzt9EygHV3j6QH8QdSL8MaOZKVpYwYLmTUaefOA-4d70EXXMlgF6GzNBB-2yDklfy3ZEvki94qD3RSNLAEguHPqCt4oyrJSSvlV7IsYmJ4mTLwTZiruyrtFOG60NwTy_RTXeSZGcyd1NlWdcS8m7We4gJUufPBIvlS_LxjQ4YgMf33Rtm3GtryJlPWlDbJ3LbgWkhiuoSc3f0MUli8ldGAOwNsGb-quor46EB4NycglF9RCSmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=OZntf9UtGpty2RsCEyKFLkRG-GRrpeltLlVkKCSejuLiGCwMKYG0EBOuQ_qSM2myeOvC9r2xZDuWnJ15e-b0Ua7Jm04sVXPQSknUlzt9EygHV3j6QH8QdSL8MaOZKVpYwYLmTUaefOA-4d70EXXMlgF6GzNBB-2yDklfy3ZEvki94qD3RSNLAEguHPqCt4oyrJSSvlV7IsYmJ4mTLwTZiruyrtFOG60NwTy_RTXeSZGcyd1NlWdcS8m7We4gJUufPBIvlS_LxjQ4YgMf33Rtm3GtryJlPWlDbJ3LbgWkhiuoSc3f0MUli8ldGAOwNsGb-quor46EB4NycglF9RCSmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dQrU7bCC0CVw26iD6kXTAdkQE1iYU6VYdDftKNnZtzTAPB54iSClao-ZdJ1iO_WZLT059GduHiSlbHa2_UQL2_JgFLxUVRCgZEmHUr4lSOLQJYePcwUpePwkYDkvHxG_-GaS8zCNRlvrhodGE6ffwGTKe2Vc92fX2A0eHfwFnF8OIxDbgOkr1GqgyBMh3iEVEwsCAdKQPfo8JQZ8spv4JFmT_1-pwofxOOs0fdIH_iPBvkO4aRKTaEJhAIf9yVZqWlDy5JehjF38EqkHhH582FYhfoYILtwGYYNdl_6gjd9FUmDdtYcYHxA2BFMaxuOioC3BZThm3oxt-pwXtSux2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/erouctiBpTdlAPOsUfbxOPUggPjhCYqd0MombMXis79BuMXcbCm_hlytTPLvaUVGN3fVwI6z03vZqFpUazbHCvAK0tZPI-jGQ5WdNkfIt4Reqk-vhHVfTJb2aP1RzUpEYNtqOUow_Z6hpAUH5KSJLcOUYvzL1xjAutI-VsZlXz8wxefkX2uvFryvfv1XMfKCBo76l82wXU0LvVtvZSpkDHcJ8pfAaMdNt7m1fxTiWFYUJd7sKOnpMkYOMG0mr22tgtYc1rvmaIX_oRAuh-4fWLcRO8H8bAnVy546dQSNicT54Ts4wPsE92JdSIDLlpavBV88iVeaViUG-2_G7jP9zQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«یحیی سریع»، سخنگوی نظامی حوثی‌های مورد حمایت جمهوری اسلامی، از انجام عملیاتی گسترده با ده‌ها پهپاد و موشک بالستیک علیه اهداف نظامی در منطقه خمیس مشیط عربستان سعودی خبر داد.
سریع گفت پایگاه هوایی «ملک خالد» در این منطقه هدف حمله قرار گرفته و آشیانه‌های جنگنده‌ها، رادارها، باندهای پرواز و انبارهای مهمات از جمله اهداف حوثی‌ها بوده‌اند.
سخنگوی نظامی حوثی‌ها این عملیات را پاسخی به حملات هوایی عربستان سعودی به یمن دانست.
@
VahidHeadline
«محمد بن سلمان»، ولیعهد عربستان سعودی، امروز دوشنبه ۲۳شهریور۱۴۰۵ در جده با دریاسالار «برد کوپر»، فرمانده فرماندهی مرکزی آمریکا، سنتکام، دیدار و درباره تحولات اخیر منطقه گفت‌وگو کرد.
خبرگزاری «رویترز» به نقل از رسانه‌های دولتی عربستان سعودی گزارش داد این دیدار در شرایطی انجام شده که درگیری میان عربستان و حوثی‌های مورد حمایت جمهوری اسلامی در یمن شدت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ3BAYzgRKQBGlCOj4bXGxax2UeNLj2MYYvvM6mKmoWtN7tgmysP_jFK2vuGdLtrHuzxhGZ6uzNIp5rhN4ifJ26FaEdw8bGDymgUWQfHq5rkHH4ReyXpwGR4foJpdzvkPgHv57G-K92usn1PkclmgtnnhM54GZfmbbBz1OaHa80Pjn56ZucYr4ROELA586rp2BuRHcEE116tDjwr2ZouGHLqxo8QcYxU2ryg5rGeMRQF1xzR6j6csOxIEnKNzXb2J8aJ4EaBVYM7EHiYm9XAhr9vjInl5JqvhW0wkcfUrGVniGPP8PRFYOTMNPwQJc0vxhbqXWdx_JV3dhgkFsfmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین امروز دوشنبه ۲۳شهریور۱۴۰۵ گزارش‌ها درباره کمک نهادهای چینی به جمهوری اسلامی برای هدف قرار دادن یک پایگاه نظامی آمریکا در اردن را تکذیب کرد.
خبرگزاری رویترز به نقل از وزارت امور خارجه چین گزارش داد پکن «قاطعانه با این اتهامات بی‌اساس مخالف است».
این واکنش پس از آن مطرح شد که روزنامه «وال‌استریت جورنال» به نقل از مقام‌های آمریکایی که نام‌شان فاش نشده است، گزارش داد جمهوری اسلامی پیش از حمله موشکی ۱۷شهریور به پایگاه «موفق‌السلطی» در اردن، تصاویر ماهواره‌ای این پایگاه را از نهادهایی در چین دریافت کرده بود.
در حمله موشکی جمهوری اسلامی به این پایگاه نظامی آمریکا، سه نظامی آمریکایی کشته شدند.
براساس گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی نام نهادهای چینی را که گفته می‌شود تصاویر ماهواره‌ای پایگاه را در اختیار جمهوری اسلامی قرار داده‌اند، اعلام نکرده‌اند. این مقام‌ها همچنین دولت چین را به مشارکت یا دخالت مستقیم در این اقدام متهم نکرده‌اند.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، نیز روز یکشنبه ۲۲شهریور۱۴۰۵ به گزارش‌ها درباره دسترسی جمهوری اسلامی به تصاویر ماهواره‌ای یک پایگاه نظامی آمریکا در اردن از طریق نهادهای چینی واکنش نشان داد.
ترامپ گزارش مربوط به دستیابی جمهوری اسلامی به این تصاویر، پیش از حمله‌ای را که به کشته شدن سه نظامی آمریکایی منجر شد، «کم‌اهمیت» دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/un726JWjWwbhbg2dVe-omeTOWmYj90mhJNt3C7r2MhjyKbd6hc8HXpEBRgLvBZB8wwsSNldb7cjvGCR1owrx8wTTG3NPLzsLiUranVRovtypKVxj2azdAsx2B-a_MeuTBySeJok9WfCGcflMxhq80lSVprWf4XGV-Syqa36IRHPpXkzMUHgL9-AnF6K3wR3UxmQ0wM5K8_d5uDBch-q_tdp9RuCYlE15KGUcQmlPOwkDHw2yjnLiWaUgrqhCDnPKLH7OWqGIh6l-f4LuDAfJewSPxDq7bNccpjuAqIV_L_SeKvba8KXtbK7q6pmMOCqzsbnk1AfYwv7VlCulOPHNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F9NQrGvm2VKp49AY3MagqesRe-USGQwi7kv0Ci9J4E8UKiVZPRMS3UbSyGSijfq2UEjn_8bqEwlXJeciI-Brz56bYAdyfMvhYRp0tud66hgFFj9aMlsd7csCoFcVSTBCczPjrWA36RXsqom7rZsgmgEP5-3ucbD1tlcuZRi2VehM9RW0oZ2xtmJblNF2TZXK-95YwBAQdsiCIevMrpwPdluNoXqPMP0-bkRLF8liVw9dqzThsqtn6y3ANcPVGHGyH0GVFTy8A6cNYeYybpB_eOT3BWiODc1FXpmgrXKI8e94ihruPbrelrvy5iSDN3-LtUPfoYBcFiR7HCy8zk-toA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه و پس از اعلام خبر صادر نشدن ویزا برای محمد اسلامی، رئیس سازمان انرژی اتمی ایران برای شرکت در نشست مجمع عمومی آژانس بین‌المللی انرژی هسته‌ای در وین، از احضار کاردار اتریش در تهران خبر داد.
بقایی با اعلام این خبر گفت می‌دانیم که این تصمیم تحت فشار آمریکا گرفته شده است اما این واقعیت، چیزی از مسئولیت اتریش کم نمی‌کند.
@
VahidOOnLine
پیش‌تر:
به گفته یک مقام آگاه که با اسوشیتدپرس گفتگو کرده، محمد اسلامی، رییس سازمان انرژی اتمی ایران، برای نخستین بار در چند سال گذشته احتمالا در نشست سالانه کشورهای عضو نهاد ناظر هسته‌ای سازمان ملل متحد در وین شرکت نخواهد کرد، زیرا از سفرهای بین‌المللی منع شده است.
این مقام گفت اتریش از کمیته تحریم‌های سازمان ملل خواسته بود برای اسلامی معافیت از ممنوعیت سفر صادر شود، اما این درخواست پذیرفته نشد.
این مقام که اجازه اظهارنظر درباره این موضوع حساس را نداشت، به شرط ناشناس ماندن صحبت کرد.
اتریش به عنوان میزبان سازمان ملل متحد در وین می‌تواند برای مقام‌های تحریم‌شده درخواست معافیت از ممنوعیت سفر کند تا آنها بتوانند در نشست‌های بین‌المللی سازمان ملل حضور یابند.
به نوشته این خبرگزاری آمریکایی، حضور نیافتن اسلامی در کنفرانس آژانس بین‌المللی انرژی اتمی نشانه دیگری از وخیم‌تر شدن سریع روابط ایران و کشورهای غربی است.
از زمانی که اسرائیل و آمریکا در جریان جنگ ۱۲روزه به تاسیسات هسته‌ای ایران حمله کردند، جمهوری اسلامی اجازه دسترسی بازرسان آژانس به تاسیسات هسته‌ای آسیب‌دیده در این حملات را نداده است؛ این در حالی است که تهران بر اساس تعهدات خود در چارچوب پیمان منع گسترش سلاح‌های هسته‌ای، از نظر حقوقی موظف به همکاری با آژانس است.
آژانس همچنین نتوانسته است وضعیت ذخایر اورانیوم ایران با غنای نزدیک به سطح مورد نیاز برای ساخت سلاح هسته‌ای را راستی‌آزمایی کند.
تحریم‌های سازمان ملل که دوباره برقرار شدند، شامل ممنوعیت سفر، تحریم تسلیحاتی متعارف، محدودیت‌های مربوط به توسعه موشک‌های بالستیک، مسدود کردن دارایی‌ها و ممنوعیت تولید فناوری‌های مرتبط با برنامه هسته‌ای است.
با وجود اظهارات این مقام درباره احتمال عدم حضور اسلامی در کنفرانس، خبرگزاری دولتی ایرنا روز شنبه گزارش داد که اسلامی تهران را به مقصد وین ترک کرده است تا در کنفرانس آژانس شرکت کند و با نمایندگان کشورهای مختلف دیدار داشته باشد.
مقام‌های ارشد کشورهای عضو آژانس بین‌المللی انرژی اتمی قرار است از دوشنبه تا جمعه در مقر این نهاد در وین گرد هم بیایند.
آنها درباره بودجه آژانس تصمیم‌گیری و آن را تصویب خواهند کرد و درباره دیگر مسائل سیاست‌گذاری، از جمله پادمان‌های هسته‌ای در خاورمیانه، گفت‌وگو خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78365" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VK-V1x5BleYVeibc2Ti6qzp3U_YRBImRZRtpUjNEfsznK-9xZs8BenlzTTOy4sarlH-qsW826hT6hk19HxFowREsUBadm7MG6Of15L9Sr5QBpDKZBVTYIj3tZadHDEuqPWPwWb9DKgOsMTXVQRVrBllwKzQnLSfRcv_j9TxxJnXVVZwhAkY--VmPw-wJFTEx-LVspfCxZ8ohXwohf3tH_Th1Se8sTJ4S8ffo-CSkmpPvuPiAHd0mMPb0beMWI7fm_3NVIhngSjT7CkMObRsBLJkhwBhNBfr_1Ku4iaZYUALR49Q8ik6Qmm7k4kzs8BWGe2I3aubChL6_l7uXr69JfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آستانه چهارمین سالگرد قتل حکومتی مهسا ژینا امینی از اصفهان، رشت، فومن، مشهد و نیشابور ‌خبر از تشدید فشار برای تحمیل حجاب اجباری و حضور دوباره گشت ارشاد، حجاب‌بان‌ها و نیروهای لباس‌شخصی در خیابان‌ها می‌دهند.
یک شهروند گفت در میدان علیخانی اصفهان ون گشت ارشاد مستقر شده‌ است و ماموران «بدون تذکر قبلی»، زنانی را که حجاب اجباری ندارند بازداشت می‌کنند و با خود می‌برند.
شهروند دیگری فضای اصفهان را «به شدت امنیتی» توصیف کرد و گفت نیروهای گشت ارشاد در مناطقی چون جلفا، مرداویج، چهارباغ و میدان نقش جهان مستقر شده‌اند و با زنان بدون شال و روسری، برخورد می‌کنند.
یکی دیگر نوشت: «در اصفهان دیگر ون گشت ارشاد نیست، اتوبوس است. با اتوبوس دختران را جمع می‌کنند و می‌برند.
...
در مشهد نیز شامگاه ۲۲ شهریور، نیروهای مسلح وارد پارک ملت شدند و به زنان تذکر حجاب دادند.
شماری از شهروندان از رشت گزارش دادند برخوردهای قهری درباره حجاب اجباری در این شهر شدت گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78364" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=o_D-Re7eA0YkhsZlKPyFFBNaic3jYWL7SWwr2PdwR6Wub7IA5-z8YhbvotqAlLGCj9zCKTj9o7sXZS64Ltcti75g-vh4JdRkw2tjIdsTzlykOjGNzeKoGatDqfrtcoN0boGjYUwzoohfCGngVVVIddYBxUjgfs1KfQEapKRAdxMF_dIxm2FVEiMu4tSVX9gBk87NoVxu1oixSbPf1NtrGBZhfWVbT04aAge3lAWqDjgBXm-rpswl9oYJhbpuvNmTpRawJHQROUQZeyehpQkOua0t6AmP16s5CNrv20_sBG1tzIabGOJ9g_bOL2OIYUa1osvCLr8Wx4Y0y0YN2iJC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=o_D-Re7eA0YkhsZlKPyFFBNaic3jYWL7SWwr2PdwR6Wub7IA5-z8YhbvotqAlLGCj9zCKTj9o7sXZS64Ltcti75g-vh4JdRkw2tjIdsTzlykOjGNzeKoGatDqfrtcoN0boGjYUwzoohfCGngVVVIddYBxUjgfs1KfQEapKRAdxMF_dIxm2FVEiMu4tSVX9gBk87NoVxu1oixSbPf1NtrGBZhfWVbT04aAge3lAWqDjgBXm-rpswl9oYJhbpuvNmTpRawJHQROUQZeyehpQkOua0t6AmP16s5CNrv20_sBG1tzIabGOJ9g_bOL2OIYUa1osvCLr8Wx4Y0y0YN2iJC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ویدیوی نجات خلبان آمریکایی در ایران
۲- یک نفر از ۷ نفر سوت موشک که داره به سمتشون میاد رو می فهمه.
سعی می کنه به نفراتش خبر بده اما نمی دونه کدوم طرف بدوئه. در نهایت یک انفجار هر ۷ نفر رو می بلعه.
A_z_im
سی‌بی‌اس پس از پنج ماه با یکی از دو افسر ارتش آمریکا گفتگو کرده است که در نیمه فروردین‌ماه هواپیمایشان در اطراف اصفهان سرنگون شد.
این افسر که براوو معرفی شده، لحظه برخورد موشک دوش‌پرتاب با جنگنده اف-۱۵ آنها را مانند برخورد یک قطار باری توصیف کرد و گفت به همراه خلبان که در این گزارش «آلفا» معرفی شده، تلاش کردند هواپیما را نجات دهند اما خیلی زود دریافتند که امکان نجات هواپیما نیست و باید خروج اضطراری انجام دهند.
پس از خروج اضطراری (ایجکت)، آلفا و براوو در حالی روی زمین در بیابان ناهموار در ایران فرود آمدند که حدود هشت کیلومتر از یکدیگر فاصله داشتند و هرکدام تنها بودند.
آلفا سالم فرود آمد، اما براوو خوش‌شانس بود که زنده ماند.
براوو گفت: چتر نجاتم در حمله اولیه آسیب دیده بود. یک لحظه به بالا نگاه کردم و دیدم چتری وجود ندارد؛ ترسناک‌ترین چیزی بود که در تمام عمرم دیده بودم. همان‌جا مکث کردم و دعا کردم: «خداوندا، اراده تو انجام شود. اما اگر قرار است از این ماجرا جان سالم به در ببرم، به کمک نیاز دارم.»
او در پاسخ به این پرسش که «فکر می‌کنید هنگام برخورد با زمین با چه سرعتی حرکت می‌کردید؟» گفت: براساس توضیحاتی که دادم و جراحاتی که داشتم، متخصصان معتقدند با سرعتی بین ۱۱۳ تا ۱۶۱ کیلومتر در ساعت با زمین برخورد کردم.
او افزود: یک معجزه در روزگار مدرن بود. باور دارم این اتفاق گواهی بر لطف خداوند در زندگی من است که باعث شد از آن لحظه عبور کنم؛ به‌گونه‌ای که هرچند دچار جراحت شدم، اما آسیب‌های فاجعه‌باری که می‌توانست توانایی‌ام برای زنده‌ماندن را از بین ببرد، متحمل نشدم.
این سقوط باعث شکستگی کمر براوو شد. او همچنین دست و شانه‌اش شکست، مچ پایش پیچ خورد و سر و صورتش بر اثر بریدگی و خراش خون‌آلود شد.
براوو گفت، مجروح بودم، اما همه ما آموزش دیده‌ایم که با شرایطی که با آن مواجه می‌شویم سازگار شویم و بر آنها غلبه کنیم. با وجود جراحات، تا جایی که می‌توانستم سریع از محل فرودم دور شدم.
براوو به سی‌بی‌اس گفت امن‌ترین جایی که می‌توانست به آن برود، ارتفاعات بود.
بنابراین با وجود شکستگی استخوان‌هایش تصمیم گرفت از مسیر کوه بالا برود و خود را به خط‌الرسی در ارتفاع حدود ۲۱۰۰ متر، برساند.
@
VahidOOnLine
چیزی که می‌بینم رسانه‌ها و کاربران فارسی‌زبان دقت نمی‌کنن اینه که این مصاحبه نمی‌گه که افسر آمریکایی با دست و پای شکسته کوه ۷ هزار پایی رو بالا رفته؛ بلکه می‌گه خودش رو به ارتفاع ۷ هزارپایی رسونده. بین این دو تا خیلی فرق هست.
در نظر داشته باشید که خود اصفهان بین ۱۶۰۰ تا ۲۰۰۰ متر از سطح دریا فاصله داره. یعنی ممکنه ایشون فقط با صد متر صعود خودش رو به ارتفاع ۷ هزار پایی برسونه.
Ardeshir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78362" target="_blank">📅 08:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GyHyHZWI4UFRsdJ_mY-TULBO_VOek_ApYDgkm92FdyEm8dKf-5JDgx4iSMu9f_CK8sWWyUTxxi7NJduFTwklJrrdws_VOxKBdVN5Vjw-7o0KKtpobdMUNP9TXPlZAoTe-EBrNAvKDREsjEyhVYAjivqdI2h2WWtkaWHI3RpfzH9gxbHF5_iltpL7DD2Oqpifx2hVZQ-4MqRoN0eiSi2dWnjzZaJMUFs9mVShiZPVCJPnnB3UbcnqcwWd4ANFPHhz819xXz4xDo2AyTyGUX7DeRUvaCwvoggofzyFQOSleffrP7cz8W6spUgf5bFVCfUygX4arlM2gBl017docLzpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه عمان از تعویق‌ نشست ایران و کشورهای حوزه خلیج فارس و منطقه خبر داد؛ نشستی که قرار بود روز دوشنبه ۲۳ شهریور در شهر صلاله عمان با محوریت وضعیت تنگه هرمز برگزار شود.
بدر بوسعیدی، وزیر خارجه عمان، روز یکشنبه ۲۲ شهریور در شبکه ایکس نوشت که این نشست «به منظور دستیابی به اجماع» به تعویق افتاده است.
او تاکید کرد عمان همچنان به تقویت گفت‌وگوهایی که به «ثبات و همکاری پایدار در منطقه» کمک کند، متعهد است.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، پیشتر گفته بود که روز دوشنبه در نشست هشت‌جانبه وزرای خارجه کشورهای ساحلی خلیج فارس و دریای عمان در صلاله شرکت خواهد کرد.
قرار بود در این نشست درباره طرح ایران و عمان برای ایجاد سازوکاری جهت تردد امن کشتی‌ها در تنگه هرمز گفت‌وگو شود.
تعویق این نشست در حالی اعلام شده است که آمریکا پیشتر تاکید کرده بود در مذاکرات مربوط به تنگه هرمز مشارکت نخواهد کرد و هرگونه مذاکره مستقیم با جمهوری اسلامی را بر پرونده هسته‌ای متمرکز می‌کند.
مقام‌های آمریکایی به کشورهای منطقه گفته‌اند واشنگتن درباره وضعیت تنگه هرمز مذاکره نخواهد کرد و موضوع اصلی مذاکرات احتمالی با تهران باید برنامه هسته‌ای جمهوری اسلامی باشد.
مارکو روبیو، وزیر خارجه آمریکا، نیز پیشتر گفته بود تنگه هرمز نباید تحت کنترل جمهوری اسلامی باشد و آمریکا برای تضمین امنیت کشتیرانی در این مسیر اقدام خواهد کرد.
در مقابل، جمهوری اسلامی و عمان تلاش کرده‌اند کشورهای منطقه را در گفت‌وگو درباره سازوکار تردد کشتی‌ها در تنگه هرمز وارد کنند.
قرار بود نتایج رایزنی‌های تهران و مسقط درباره مسیرهای امن کشتیرانی در این نشست به کشورهای منطقه ارایه شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7b-NqDmrVfuY-8dtdrnpheSOJLkAf3_g3sA-wyZPHF6AqwnZU2AkYOhPAxuP9vjpUVfosqp-CtBzhsMvkGz_NPsvwOo56oDjVXuigG7rPtesdN81juUOzLwbLvhxST46dKKMt0FBcawOL4gZx8q6YvQj7_IztTZzXAQKYoIw0-KgAfstah0U_cSFtmbsuOpkkKVagOskD9HTc6NJOSTrbGSKRdBWGppRZmykoa5O4QwirMvZIxEapwrDJZ27y75_qgNmvc7elg6wIl9iEGzsycFtkv258OFxMoY_WVfmWF0Kh_FPXJ2CmajCvsIKsOHuwfJqHHHJs3pWwjR58yFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/930e263d13.mp4?token=LAR2QZlJqBBT8eB4N8UTOaF3xd9H6jfyd8QPpQ0SIBmHJ3V_y_nAYD2JebUq_oP0cLBGBVyKATthdaSyy58TFF0l4oSyl8dS33l3cBHM4hziCOmYuRZRYb3_M6HGLAl_O8ylYK5DHvC2na7_drDuVcyQH_ztAsMqf70oDu5e_FDInLNMcx54wJtpPFkSzjFYQITizZxIg9KX3tXyTO2paNeDFWEImwfAXsmd8eX26pVkKIy55zfK1tUfR2HIWUa5qqJwlK6HczQHIcakpOQdI3DK0TjG3jME05jUF1FzHdq6fOrVHlUCfKIvcuHkz23odTvVS45dmatgaDDVHa7Mjw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/930e263d13.mp4?token=LAR2QZlJqBBT8eB4N8UTOaF3xd9H6jfyd8QPpQ0SIBmHJ3V_y_nAYD2JebUq_oP0cLBGBVyKATthdaSyy58TFF0l4oSyl8dS33l3cBHM4hziCOmYuRZRYb3_M6HGLAl_O8ylYK5DHvC2na7_drDuVcyQH_ztAsMqf70oDu5e_FDInLNMcx54wJtpPFkSzjFYQITizZxIg9KX3tXyTO2paNeDFWEImwfAXsmd8eX26pVkKIy55zfK1tUfR2HIWUa5qqJwlK6HczQHIcakpOQdI3DK0TjG3jME05jUF1FzHdq6fOrVHlUCfKIvcuHkz23odTvVS45dmatgaDDVHa7Mjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش، پس از اعلام نرخ سوم بنزین در ایران، تصاویری واقعی در شبکه‌های اجتماعی منتشر شده بود درباره اینکه بعضی از تلمبه‌ها در جایگاه‌های سوخت (پمپ بنزین) امکان نمایش همه ارقام بنزین ۱۰ هزارتومنی رو ندارند و مجبور شدند در ادامه نمایشگر یک صفر بچسبونند روی بدنه تلمبه.
حالا محمدباقر قالیباف، رئیس "مجلس شورای اسلامی" در «ایران»، اون انیمیشن رو پست کرده.
ولی درباره قیمت سوخت در یک کشور دیگه:
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHktxx5z4HTNPBncPJPvB8MpFBiZ-6ntRfzIH3Hj-jA1Y_aNyTiieQ8AOssbV3cDcpU3fA-36XHGL59p6e6QBDW3FVDSVsyMDlJisaLpO0LLCPHwThdL2lehENcU7J_P2YFInYla1ApvjgLLeD4pm0OqBvljvjbezfmhUCcRGBSCQKffDSsYDb3TrLAtAZYiZUeHBSp0YKU2OqMVEWQVBs3y916djCXKl7dmTj3sDgLPQ9IrV3ApW09i6NbC7V2lzfqswtpDh3a7B41NIxnFk4TxuEHD8Vjh-D9PWpftGOPxRotCOkuJgAnRm2PVexgi2s7KJ9fBlHErGF-h19USNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OOLA_tZgATLkK4nrLGqkXDGT-6DVyTCB5hcB1v0eElJJ-giEQSs5OgPlHRnGrkgj6gl0aFi_uvNaPhokcH937Sh8UN-x42l6yhPeYS0nO5NMJ9GOWiz4tOtipW88Bd99xQg30DN8l2MyupoDZunQrCMLOq0S7cpL0AFcyT1vVKrQPgE6aU29vc5RIiiPjTl_-bpGnu-8Wp0BWr44lcd69UAV7D5lCJ2EYbdRVoslIBXivqZN2cM8CICFSbxqC3nO04yIsHvGmuqPJddHKEuxzj9IfibVOaCGYaWGmCQ2DDnI3jdzfzLbB31bSHnmbAo6LTNQgi3GjQxMG5sIdiyL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PmP1E54PL3blEws7nwozCX9XgDXPFJCUlTMIWVzxcbMBxWQb58ri5pDPunhDR_zB9ZUJ3-3hP8ocQ7TqXWa8p5IJ3DNR8tyWAMMmQFauuzNJNez7w0Onf_5DY7MsRk1vjT8b-Is5GMmxaq1DlRf9cyLYDE7JTd-EmxT2gcorJc_TEzwefTYbe8R2XQsk3-eFhteypEBshSPRzKh7Mb3y23L2U5b0KMAnWmmC1opEEJQDVWv-SWa4FaMqBeBoNAI-wDH0z-MAA6VfxLB5QvvakPMm_ZmZcr-oA268XWu5Zm3pk0PaH-mQBGoxUuClBtd5_zvFdC9Xvnhcl8VOZghh6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78355" target="_blank">📅 18:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/knQLeRQ3YWUB1zIDQhXtE-_D-xqQDkUAPH3ZsO2BnYqPeJDJFKss64NehmNwY9ibH_ihlIixPS9gh7qaDFu0MTFGec6hM4Yq2EB3fZcHjaY67SQiCOPHLnSNSsJ94t0sJycjyri3T3hDx0Vu1Nr4jXq3i7EuLU_KJwCi6fchTKhjjsUrHwABl3lc3PHmcCNKj2jVI490wL6TRFad8XkpKFeWeejoQwGTtZ-c2-A5y9SFCsrsh7OdnbKcM4I3KcSYJ9sFPKQmbbl0qYR1ApzyE5n5esqkBtWObNZLDnBxtuxtKF0kaXERVoJAcjZmaeW7PFeK59QZ8-_agmAroc20bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز یکشنبه ۲۲ شهریور۱۴۰۵، گفت «موضوع ایران» ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا پایان یابد، اما در هر صورت جنگ با ایران بلافاصله پس از این انتخابات تمام خواهد شد.
ترامپ در جریان سفر به ایرلند و در حاشیه مسابقات گلف اوپن ایرلند، درباره احتمال توافق با جمهوری اسلامی گفت ایران به‌شدت خواهان توافق است و به‌طور مداوم با آمریکا تماس می‌گیرد، اما واشنگتن تنها توافقی را می‌پذیرد که به گفته او «درست» و مطلوب باشد.
او همچنین در پاسخ به پرسشی درباره دیدار وزرای خارجه کشورهای خلیج فارس و دریای عمان با ایران گفت این موضوع برای آمریکا اهمیتی ندارد و تصمیم درباره دیدار با جمهوری اسلامی به خود این کشورها مربوط است.
قرار است این نشست روز دوشنبه در عمان برگزار شود. ایران می‌گوید یکی از موضوعات مورد گفت‌وگو در این نشست، مسیر جدید تردد در تنگه هرمز خواهد بود.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز بار دیگر گفته است شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78354" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VqrDifaeTyCBYLqBWDb2ZmBm8fypPLDV-o8x27hOf3_sIKGwGqbWcVPAxBMa7njDi2Q1RpxKOzRbdCref1iCpzjrOIMElvtY8SWH8JaQoikSNV6XqXXVdxPEwvHlZ4in0V8wzrnVLUFK1dSev4JqAYgbeCyl7GBNJ_K5bS0G2Gc4uULYOKnYuc4Yct5LudxaDbcNBhGd5PjMK43WAADBc5PR7vHHgXGGhl_F-M-Th4SUc1pSsnDtqrgKWOr8N9tKP_s9In_m8GqbCGkj-iuuxfspN1ukdKwf10FDN4iuSnXZmvm6wO1cUU2FWkhHQYLSAyz1veIRNrl9HfvrRP7n5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hgShoOroQRkqgqiuBCrN7rz5DI-bVLXXITYYibCLhiHw1rDpV8oiolOz8OPwhROELrsmDZ_RlwoTv1eGNzegb0lCMiG1-LYT3ICJv7fPwSrKMS-L22Tygq6MyW_YMaeRmwXqZlSzH953kG06A7C_BU2Jo9U9T1TB8X5ygeQ0RCsBr5GzbMzlgIMs7W-mpwbozxCHVSDSgT89Ecm8sAYPqmhCKS84L5qpfDwCL9cYK3X3WKU0Q_q6dtEqJwUDkvvDO1ejJsyH0r0zwYDkCkq-GTYwdmrgqLzYPF1XuF8OssVdiznfVo-oU75tsxweEpYhv1s5an7XQWTV9dvm9cLLMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز شنبه، با صدور یک هشدار امنیتی، از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر داد.
این نهاد نظارتی دریایی اعلام کرد: «گزارشی مبنی بر وقوع یک حادثه در محدوده تنگه هرمز دریافت شده است. یک کشتی هنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.»
@
VahidOOnLine
امیر تیموری، فرماندار شهرستان قشم، اعلام کرد یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب‌دراز جزیره قشم هدف قرار گرفته است.
به گفته فرماندار قشم، در این حادثه یک نفر کشته و سه نفر دیگر مجروح شده‌اند.
تیموری عامل این حمله را آمریکا اعلام کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=RuHrnWX92okFpGJVS-u3z3r5tU4qJVI6vGV99xAPwyz9rWNjqa9R_qz8vNPT-9iMsbkYwxzxlWHZ5WdoMOkhjTHoa9KJ5TziwRB0wXPC8MJ6qxb9Z8jJgWUg6W4UgMedVjPyi3lvdSHBw_gDeITO7Py08AXPjOM9NXW5KcMViYI3p7jB1F5_GDv4VWvMqu1iAAGUNxH7d3Q-YpkRWDFW7ZtL2oYWbtdHstc2CidhzXyP7TkUAcUX-GXMyoinHH4-IWzvc4NynzhbCVxrFM4WTzAooI4xtOij4T4_fOJknIJVSbW_FdKit6pY-4IuD5jE8TI0L0Bi3lWQLiKiTlz0ZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=RuHrnWX92okFpGJVS-u3z3r5tU4qJVI6vGV99xAPwyz9rWNjqa9R_qz8vNPT-9iMsbkYwxzxlWHZ5WdoMOkhjTHoa9KJ5TziwRB0wXPC8MJ6qxb9Z8jJgWUg6W4UgMedVjPyi3lvdSHBw_gDeITO7Py08AXPjOM9NXW5KcMViYI3p7jB1F5_GDv4VWvMqu1iAAGUNxH7d3Q-YpkRWDFW7ZtL2oYWbtdHstc2CidhzXyP7TkUAcUX-GXMyoinHH4-IWzvc4NynzhbCVxrFM4WTzAooI4xtOij4T4_fOJknIJVSbW_FdKit6pY-4IuD5jE8TI0L0Bi3lWQLiKiTlz0ZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=Um8YPGHj0MFNChOB3rjsV59XmEyZ7JcKMwVZU-MHB-7Jfcr3n-GNn-xU_mJDOmxv_NyQJVVIpZkvHrgwQ37_g2t_MqKzAeS8DtATne5QQ-B_8h_4aEjvY5Vkpn6MH7eccSC_WRTxwOa5HjE-tqwwFIutBEr7k_GmUtxY1AJJz8XMfZLikOhRp9aU3dIKImUgvZchqt0zQ4xRy-1j6a-4odPNqJJPTfoLSnRSmlsfgDD9bkx_uaThULbxuvebPkOcT0v4NB9nD1iReMoV-mAIChlImCU6GW_nnhkun_MVEtB5NerBoQ_d6Sv_QH1axxBupErpk9fOJuIKG00WZzI9aA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=Um8YPGHj0MFNChOB3rjsV59XmEyZ7JcKMwVZU-MHB-7Jfcr3n-GNn-xU_mJDOmxv_NyQJVVIpZkvHrgwQ37_g2t_MqKzAeS8DtATne5QQ-B_8h_4aEjvY5Vkpn6MH7eccSC_WRTxwOa5HjE-tqwwFIutBEr7k_GmUtxY1AJJz8XMfZLikOhRp9aU3dIKImUgvZchqt0zQ4xRy-1j6a-4odPNqJJPTfoLSnRSmlsfgDD9bkx_uaThULbxuvebPkOcT0v4NB9nD1iReMoV-mAIChlImCU6GW_nnhkun_MVEtB5NerBoQ_d6Sv_QH1axxBupErpk9fOJuIKG00WZzI9aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهوری آمریکا در جریان دیدار با مایکل مارتین، نخست‌وزیر ایرلند، در دوبلین بر اعمال کنترل مقتدرانه و یک «محاصره دریایی باورنکردنی» بر تنگه هرمز تاکید کرد و گفت این اقدامات مانع از جهش شدید بهای جهانی نفت شده است.
دونالد ترامپ همچنین گفت نیروهای سنتکام به‌طور میانگین روزانه ۲۵ شناور و قایق را متوقف و توقیف می‌کنند؛ اقداماتی که به گفته او بیشتر آن‌ها در تاریکی شب و در جریان گشت‌های شبانه انجام می‌گیرد.
این در حالی است فرماندهی مرکزی آمریکا، سنتکام،
امروز
اعلام کرد طی ۶۰ روز گذشته و از زمان ازسرگیری «محاصره دیوار فولادی» ایران، مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpbASzy_VTBFhfUb0qUQg5zkdv8aoIEgmgJ1M4PcEJGXIPTiqDTpdDmmI4NBHHNvfv-WLtZ4MQ1EubVpKYL_NSFoKWsE4nKmeIITYeZqiYQqQRAPw9lNni4Om9m6Dentp_bXNwssBQPxaRC-cXb1TQ7WBrFsxyWyTmIA2LSMnMD8_0Pg7rUASh2CIXmYzcpnIgqb6CkK-jioa2nx8AohzKuH4pMdr-GW0kWcqtQYM3NkqoMWcfkLBYrcouqDqAC08HrMx_HfHib5pXCwsuhp2Yvhl2l_r6htCs9vxBoC7ICerFrLcRFYxB7N-f-X6Peg0QPpiWaQDY0cJKGixpn8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kduEGUK6gkOtwCA9gKtGRUo1b6vQWdl88UbD_tHe_1RuUTQcssgnE5HqCBLRwlBakKdwzQvRsuQBWWpLNYeIprxgzKTEc2Tf3_sr9KwrahieTSGgvFQWZlAUcgWyjBZ5pEDwteLMPD-bSiuNV5aNMA7RaVjkhBtPktYPDSbdGxOhS4uSDCfogZjG0OHRV_FIY8jEkiS5Gta79u5y3yl2YL1PvoO620VWTkbzvjmAbxf5c_l_8qwSyGIpnVeXZHYA33jlbGWPWeaCTCZ3ecaw-C2yW3e0Hh0guNCtmgGx0NPLVQTEpONRFwP1MNIUyr7lhTR7-TsqjSJ9dzJQRxQBFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUAul4v3OLFl9YtZ1r9-J39B0wAv422yY8jMcwgDOFXn9_E4MkN4Hy4B935iCGOauVOiXDVeR5EVsadLCMm4ur9VLifdFjsgA5CEW4geURiV_FFXSQXyQN6sNmTrdj3JEthBuysQ2O-8Lcim5xu2IMgj26Tmkm-PEvvkZS8NKfiUtG4cLE1stPrsFVE8G7Dw0MsvVB8MIQYNxfmR59F3LXcnRqY6BrEjX4ci_gdu08MPDYYYnHs2t3ou2zoWGlvhAxhYlEcdUBehLVJfk6VGs44Q1mdz2SioUhDLu42mc-bsZj_oJB7kGX2tW1pjEblWfWA3QJmKtrKYybiyX1_pNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=M7Jk8hhcC95be51zyWRnGFPomGuxa_-hNCKlWT5D-i8GbL0ygBIt-EK83fZtpNC0x-n2BkwgegMvLqCw69pT6QbCJy7f-MUZvbaZpN1ePqLuQwjEkNn1qvdnPseX8RYvvxdelK1D8p4Gch3IXXcJQJFZXD0dX_jJgH3WO03n-ZA-2x2raguk0Lh4f-QCKHEeArKo5JagQ2u-553e7jF8byKtRGUuspIKDu4xD9pQxusFwdSKKFVF5Ar8Pr64qdnev_Yn7RPVw255G9j2AoIlFIi8jN-5s9giYvoF46386K29JMUs1_KfTYHUgrGXdxChThJScg0Qk41bKLLxYVSTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=M7Jk8hhcC95be51zyWRnGFPomGuxa_-hNCKlWT5D-i8GbL0ygBIt-EK83fZtpNC0x-n2BkwgegMvLqCw69pT6QbCJy7f-MUZvbaZpN1ePqLuQwjEkNn1qvdnPseX8RYvvxdelK1D8p4Gch3IXXcJQJFZXD0dX_jJgH3WO03n-ZA-2x2raguk0Lh4f-QCKHEeArKo5JagQ2u-553e7jF8byKtRGUuspIKDu4xD9pQxusFwdSKKFVF5Ar8Pr64qdnev_Yn7RPVw255G9j2AoIlFIi8jN-5s9giYvoF46386K29JMUs1_KfTYHUgrGXdxChThJScg0Qk41bKLLxYVSTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، روز شنبه ۲۱ شهریور ماه گفت اطلاعات تهران نشان می‌دهد حمله موشکی آمریکا به لامرد از خاک یکی از کشورهای حاشیه جنوبی خلیج فارس نیز انجام شده است.
اسماعیل بقایی در گفتگو با رسانه‌های دولتی ایران گفت این موضوع نشان می‌دهد آمریکا «برخلاف همه قواعد و اصول حقوق بین‌الملل» از خاک و حاکمیت ملی کشورهای دیگر برای حمله به ایران استفاده کرده است.
او تاکید کرد ایرانیان این موضوع را پیگیری خواهند کرد.
بقایی همچنین گفت برخی کشورهای همسایه، برخلاف «اصل حسن همجواری»، اجازه داده‌اند از قلمرو آنها برای حمله به ایران و «ارتکاب جنایت جنگی علیه مردم» استفاده شود.
در نهم اسفند ۱۴۰۴، یک سالن ورزشی در لامرد فارس، مورد حمله دو موشک قرار گرفت که منجر به کشته شدن حداقل ۲۱ نفر، از جمله ۴ کودک، و زخمی شدن ۱۰۰ نفر شد. این حمله اندکی پس از حمله هوایی به مدرسه شجره طیبه میناب رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RE8zJDBbeNZzknbHVNsgVdGPsRPyMrv4N8nURFT78pz36RhcQ1UfxHlsk6Mt3SS3GIHxu-92oC2rrN08BmUj-TCMeqW3PhfUl5vnTCKTcgPbid5NiKwha0ASzdPAirHTNo511c0q-ddvjyJk-evTVIJrlL2S7aafKBtPF_GEiGocVUrDm_u9xYRkzWmeHXHpttJWOlOFZjxDLM-w2DInIXYEw6ByECdGiEMtVXqeO9qg1sx0qE9JG4VNbhjiI2xp9ZBU9XaODbW7wwH3fkA6wShAKFoQ_5CSzpiFHABV-2tC-w0v1uDoX5KDOMvECnkTC1pY4JFX5T1138RG9TUYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=vTjKtKYH7golD6afwJgNQmqt2M-zuuTDmeI1G_IyW6gUrxTrb0NQ8izED_xsJt2hJHbIY1VBTelj4ggWs883NkXYDGlyGR03mDpm9-q4bcYHwp8flN0HuaWIPm52keamW_L3JoN6XPGnpWQaqHu8JVWTz-rax122UQ16mxmXm8i1YFi_Ks5N81WssVRFVICkvd-Bf2KNJDNd02ERRaK-DBAIgDjLfQjp19rGIQvMQ5qOhzorQJkX06PE0gUeu-RV2A6UPh4IZa8cY-eclnjKMzgS63wT-yJkJjP7UKj1x2m6HbBYiXcM7C7dZp2Dol4uk6gDUbAoLoA_0dVrgKSiJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=vTjKtKYH7golD6afwJgNQmqt2M-zuuTDmeI1G_IyW6gUrxTrb0NQ8izED_xsJt2hJHbIY1VBTelj4ggWs883NkXYDGlyGR03mDpm9-q4bcYHwp8flN0HuaWIPm52keamW_L3JoN6XPGnpWQaqHu8JVWTz-rax122UQ16mxmXm8i1YFi_Ks5N81WssVRFVICkvd-Bf2KNJDNd02ERRaK-DBAIgDjLfQjp19rGIQvMQ5qOhzorQJkX06PE0gUeu-RV2A6UPh4IZa8cY-eclnjKMzgS63wT-yJkJjP7UKj1x2m6HbBYiXcM7C7dZp2Dol4uk6gDUbAoLoA_0dVrgKSiJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXFXh6p30VAGOsJhj_jAptw3wFucKmu0eeQm23MRjpuhjhqHkqDEpvueUZdbEhoNjGgw-1SSNeAi1nCcU-GdQISYk_fr9pZGeemjro5Q-awtgBqbHSjzfDE8-wILnTMApOFdmC3uSslY-2UK9ymt5RjXS4WlWjbbXGMrsFgOU_AzBhRGig83phE_fA-gUcO6bzCSlvgXjN2ZSZpttLfoo8iGSc4rhr5XDvi_fNgjHqqrNw2usUw0ByeBA9Wu4d_rhkE09St_AGrZIhldrl7s_XiuelUvkIEgpdEBYFGSNa16_vGOkrAPWU57nGtYi6HiwcAG7v3zO3fdkDci3K8Ojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ows88lE5OR0WCHHDVhgZ5WI686YkiBubZkzkPrfzFQLsj5-D8ppSSRGblrakqkNGLU8C0Axjw4sD7AA0nOSMcpqABIx-jXUc-o_KONG73QeMoRNdWzcAUEpXBuSEgUKvH4dgBbdMHykK3MQYF_VoI_id5KEL4e-UaejLZDHqhxRqAW3LNtVQ7wm2nv1mN_E1hhlGkwJBD94SXyR7L47gEHcUNvy0n8v7Qgfmw6IMKS6FDpwCiNJ__zyKb2f6TESG0SBsNeQrgQxxn8ZjA5NNm7kBlVABFWSAs9NSX8ZtgoJJOOTDsfJ9yHlND0bUczOPuN4B2400ERtpRTpoRXGm-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DXClwOU10zgU-suSLhfrOdPP-5J21iDybRmZyzGrWDTS9Q2Gk3e02DxSOJdrqj1ADE71_ZFaDtvgx9cDAok-qoy2UTiLGyHnu1ijb9KNw6IcsPU98DMdaBMDZL88q_fj6svtEbPRo64qiI4rEuvYcel75qe69BqzaxwVMlWBM5kMi18_3mK5yO9qfGT7LzaRdn1-R4seqKxhLWzNBZ2d11cCe8OBPKEfj6oBvTKITKpHCSscNMjsV0-FQp-xwqeHb-sP24h0veh5jco--dslDDGWUmiMLnoLur9dJ4qLjs0OoB4qLGfRF9t8Lq56Wvipvcg1GKQ48YVVvFrR2HXYMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درگیری میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح در منطقه «بخشان» سراوان، پس از بیش از هفت ساعت همچنان ادامه دارد. «شیوار نیوز» از حمله به نیروهای حکومتی از دو محور، شکسته‌شدن بخشی از حلقه محاصره و خروج شماری از افراد مسلح از محدوده درگیری خبر داده است.
این درگیری حدود ساعت چهار بامداد شنبه ۲۱ شهریور ۱۴۰۵ و پس از محاصره یک خانه مسکونی آغاز شد. شبکه اسناد حقوق بشر بلوچستان پیش‌تر از استقرار گسترده نیروهای نظامی و امنیتی و استفاده از سلاح‌های سبک و سنگین در این منطقه خبر داده بود.
براساس اطلاعات منتشر شده از سوی شیوار نیوز، نیروهای نظامی و امنیتی پس از آغاز درگیری، محدوده حضور افراد مسلح را محاصره و مسیرهای منتهی به محل را مسدود کردند. بااین‌حال، در ادامه افرادی از خارج محدوده محاصره، نیروهای حکومتی را از دو محور هدف قرار دادند.
@
VahidHeadline
قرارگاه قدس نیروی زمینی سپاه پاسداران اعلام کرد در جریان درگیری با افراد مسلح در شهرستان سراوان در استان سیستان و بلوچستان، سه نفر از نیروهای سپاه کشته شده‌اند.
بر اساس اطلاعیه این قرارگاه، این سه نفر با عنوان «پاسداران گمنام امام زمان» معرفی شده‌اند.
قرارگاه قدس همچنین اعلام کرد که تا پیش از ظهر روز شنبه، چهار نفر از افراد مسلح ناشناس نیز در جریان این درگیری کشته شده‌اند.
این اطلاعیه جزئیات بیشتری درباره هویت افراد مسلح، گروه یا سازمان وابسته به آنها، محل دقیق درگیری و چگونگی آغاز درگیری منتشر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YozbOpFWPay1xIhPUV_OZp6s0YRI6cuIBNT1R6PiJehyIYILJyLqpICfMylDbU8WgkACFYCVYb2QC-ZVZV315kv_2se7oRcJbXCvtnlYVXxNyph35BreCpCkURMlTESeLOJj-J4T4gl3D6GPDEhb3VJpMOs-UpVqPZnieu7xdGEyhuKihY4RMk4XmgDe9z8C996wbPdCItwDEjO7a8PiY20xLFMPOKEnfkv48_UDAc6UyISzj_U73RYWpv3o-m1YdYtk5vZIIN6WBf1p4O7uX39VLAjxX6v0aREkv00p7W_SeoC6NrqWWMG4mkifh9J0LC-4-39OSWLIVaJPRy9ltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودا ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، که از ۹ فروردین در بازداشت به سر می‌برد، به اعدام محکوم شده است.
بر اساس این اطلاعات، شعبه سوم دادگاه انقلاب بندرعباس به ریاست قاضی خواجه‌حسنی، سودا ابراهیمی شمس‌آبادی را با اتهام‌هایی از جمله «توهین به رهبری»، «فعالیت رسانه‌ای و تبلیغی برخلاف امنیت ملی»، «اقدام اطلاعاتی و امنیتی به نفع دولت‌های متخاصم» و «عکسبرداری و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور» به اعدام محکوم کرده است.
دادگاه همچنین او را به دو تا پنج سال حبس، محرومیت از برخی خدمات دولتی و مصادره اموال محکوم کرده است.
حکم اعدام سودا ابراهیمی شمس‌آبادی روز اول شهریور به وکیل او ابلاغ شده است.
بر اساس اطلاعات رسیده، ابراهیمی شمس‌آبادی در جریان دوران بازداشت، به مدت ۲۰ روز در سلول انفرادی نگهداری شده و در دوران بازجویی تحت فشار شدید قرار داشته است. خانواده او در این مدت از محل نگهداری و وضعیتش اطلاعی نداشتند.
قاضی خواجه‌حسنی که این حکم را صادر کرده پیشتر در سال ۱۴۰۲ از سوی مقام‌های قوه قضاییه در زمینه‌هایی از جمله صدور بیشترین احکام و جدیت در انجام کار مورد تقدیر به عنوان قاضی نمونه قرار گرفته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RtgqbhAfmQkptoyZxr_-uMre837yDot6tIpFjDztRL1bHUbACFSm2DRn1x46QhohGB2w63Hxry3L0-kv79SHp1va7uZ9OrfRP_l1jz2Jg7I-zJjMIgJFdqqa2y7lDsfHfWw3yXk_ojD0DMNrUAr-NdqkNU4nIEl2pP2V3iBUAWhYp7w5wtsWmuQEJE6RlCgw2gMqBHSEhwaRud9o6kmnAj5HsuENbvwXlAG2C9CoUmIm4vwjbbu42WSQ2fzXhN6vPsDPKcqsxL8DJv-Vfdl8IksP4L8xW_6jMb0r9deAlfGRFA0wTB3vCBjD1rZiHBDgxcijYjfLoWa-QD_tKFFA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n0wxNOWijImjqPBYNOyX2mKZ36lyBbv1D_W39sg6SK7ngWiIT92VUbCQH4EFQZ1m_zi5nY1bUCLEE4tS6rvHFfHpJvlVPklz5DISWtdPvrDHffQg3W5aQ_OStcp_r3ePsAUh4p-Qolf0OIOiIxeoiEnN_MrRpZzNHYguCJH1CzfVmzK-HepqgCP4Nf9InyGuslexzA8wUygFpnWwapvMZzcZJoNUqC1paPKjtkMQ_p0abKLf-SOi-0FNlfoK1yBCpT4yhxgzikB_W7nQkSLYzMzecDA5HkIGbFTA-gCFRUcCeQri8SQQT5VQFj3M8iv8V1Shv7Wne_eJpfigJ9EQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J9co3Ck9QN8BaBAp3jLlX5KKMf9TrB6v8ydbaNCVYvellxhLlBmoebITcQJOW0veIwcGKIxKmSUzj8kqD0HnMX5_Wds5BRZAzIxjKN9QsDa1JgzwwqZHlDN_68h2jp1hR26ud_z89cEKWXyjF57bt351w1xFNK_4WAmpxD_BOnfpI5SdcIuOt3gzt4gaqJc5VOBBo6zr7NFo_2zbc-jZQ1992MwNt3k-dtzzm5MazHQ_iciLyOGdD19c3N7Obp9OJUthB25GedIDRTIwLbiv3pf99yTQ-mOTV6SKF-wlbKcMw68ZCCcDV69DGK4xcCsTNWPuQBDdtTHzQvMkl_SSsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت انرژی عربستان سعودی روز جمعه ۲۰ شهریور با انتشار بیانیه‌ای اعلام کرد که خط لوله انتقال نفت «شرق-غرب» (واقع در مناطق ریاض و مدینه) صبح پنجشنبه هدف چندین حمله قرار گرفته است.
در این بیانیه آمده است که به دنبال این حملات، عملیات انتقال نفت در خط لوله مذکور به صورت احتیاطی متوقف شد.
این رویداد همچنین منجر به مصدومیت تعدادی از افراد شد که خدمات درمانی و مراقبت‌های پزشکی لازم به آن‌ها ارائه گردید.
@
VahidOOnLine
وزارت خارجه عربستان سعودی اعلام کرد خط لوله نفتی شرق به غرب این کشور با پهپادهایی که از عراق پرتاب شده بودند، هدف حمله قرار گرفت.
وزارت خارجه عربستان سعودی افزود بنا به درخواست نخست‌وزیر عراق، در این مرحله تصمیم گرفته است اقدام تلافی‌جویانه انجام ندهد.
@
VahidOOnLine
خبرگزاری رویترز گزارش کرده که بغداد دستور تعطیلی گذرگاه مرزی شلمچه میان عراق و ایران را صادر کرده است.
دو منبع امنیتی عراقی به این خبرگزاری اعلام کردند که عراق این گذرگاه را به عنوان اقدامی احتیاطی و در پی حمله پهپادی از مبدأ عراق به خط لوله نفت شرق-غرب عربستان سعودی، بسته است.
گذرگاه مرزی شلمچه یکی از مسیرهای زمینی اصلی میان ایران و عراق است.
براساس گزارش‌ها پهپاد شلیک شده به عربستان از استان میسان عراق شلیک شده است. این استان در قسمت جنوب شرقی عراق و هم مرز با ایران است که مرکز اداری آن شهر عماره است.
@
VahidHeadline
رویترز نوشت: به گفته این دو منبع، عملیاتی گسترده برای تعقیب و پیگرد عاملان این حمله به عربستان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5kuWz3nWIctI-1VsXAQFb9muVlkTzYImbfRHzeOBgp7pYMgaKDE61eXsPC2b4NujIWcrAgii7NM4i-smsru2SDTb2p-u7BxrdiSwc4dTkVX8s4PBpjYnGUHoBlOZmktJHDOwdB60S71EC5yRPb5zQEZxF-PFk1WTQEwXtkUW6BiqDw00GDd-e8g_S2cHf_kqwkXSPqjXHNRhcqzR1qQmP3ngOozCSheQJU3AWZyML9WTCDumgqTVw-El8hnD87CJMx-S4FDPK1Kmz7DlINBusL7DMv6rbJVqduAWUT2TYaVhEEWZB0OGRvBGpYwujP1DDMEVhEvlyWgCoufJOi-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=ehSmWE0gSMfeQ0yn1lvh-hsrnLJCBysBbKjboOk7t21c3DMqH3Ua_tPIsz9OXGZqXl7PTo7K0QvPMD7SHzxtr7MDYkjga6bJFKR0OoKzp_Bpn3H3E_S0o1Cvj6qXpF3vrsQEkrk-UivAValO8L6MTJN15BACs4GqrWZU-2ZydzmFkHJSQjlHFA2N5oz0g0ota-wpqlHjGe28joZwtjRZRCQbmPxry6-EjIM2_VR6JbIMDcwbftCC1DZ46rGzLbyn5jF2J5SJOFIj-LYcYHvVJbgDf_XC8uA1NQGr27U8BOQxpxzzHIslLyM2JLH-UiMQdxjuKFfcIrZAQqAU77PjRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=ehSmWE0gSMfeQ0yn1lvh-hsrnLJCBysBbKjboOk7t21c3DMqH3Ua_tPIsz9OXGZqXl7PTo7K0QvPMD7SHzxtr7MDYkjga6bJFKR0OoKzp_Bpn3H3E_S0o1Cvj6qXpF3vrsQEkrk-UivAValO8L6MTJN15BACs4GqrWZU-2ZydzmFkHJSQjlHFA2N5oz0g0ota-wpqlHjGe28joZwtjRZRCQbmPxry6-EjIM2_VR6JbIMDcwbftCC1DZ46rGzLbyn5jF2J5SJOFIj-LYcYHvVJbgDf_XC8uA1NQGr27U8BOQxpxzzHIslLyM2JLH-UiMQdxjuKFfcIrZAQqAU77PjRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=vznQsLdiUyVxouu7JreJcEMMBkZL809kPmSLVRQRge1wBEqgFTWdExclm4mnKwsXjbape5YxB_Vd4LcWuN7fTJvcpMesG7NZCLLSDmKGvVGsHzxvQakFauooWxYyNjJ2Zd72PLB2aHK3xJwaCAbjIQZW52JjQ6GxB4jNPSShZhvljINc0DUTkB2ELPncTGKrh75WmPz8JrDUCW1UugDCxTHZLhWTqhfhKEQA_UyTLSbSbSus7wSEDBhwmFE6BoX6yVkE42BFM99tRx73UQlO7m7jlNhDBDbmbf1BJz-JlwsoR30Gwzbvf_elzh5_Ms3ssxwFzQiaO0N3qJyGTy_kiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=vznQsLdiUyVxouu7JreJcEMMBkZL809kPmSLVRQRge1wBEqgFTWdExclm4mnKwsXjbape5YxB_Vd4LcWuN7fTJvcpMesG7NZCLLSDmKGvVGsHzxvQakFauooWxYyNjJ2Zd72PLB2aHK3xJwaCAbjIQZW52JjQ6GxB4jNPSShZhvljINc0DUTkB2ELPncTGKrh75WmPz8JrDUCW1UugDCxTHZLhWTqhfhKEQA_UyTLSbSbSus7wSEDBhwmFE6BoX6yVkE42BFM99tRx73UQlO7m7jlNhDBDbmbf1BJz-JlwsoR30Gwzbvf_elzh5_Ms3ssxwFzQiaO0N3qJyGTy_kiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoGZqikRZifcD-jFyTzkXMvRR54cgy7ni6HzDTLj0kELCG1WbBI4atZRDH7hrLFucIYbXiMRAvm0gxEXEjpWThNarwyWbuLSl4qwDjziZfTII43izGrSOa_jcg6aANVUUWKU3UKb9snFONLuTDN3E-kB3xwe66JHW7yfsW3BBdkc3Hz6He3Uejp4P_n7i9ZrwgwXILdKZXupjrbLENikRmUTjDtK_9gVime_-zMhuYsEViiprz5f8ZD7pVOhfUxTx4iS83Rv4_jG5FjEI_Z7Ehg_y_wLymjQQhn7_INITYEskUKn60h_1u6pG16Fd6wLnobnw-vZ867v9YguSfqdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گزارش‌های رسانه‌ای مبنی بر آسیب‌دیدن هواپیماهای آمریکایی در جریان حملات موشکی اخیر جمهوری اسلامی به اردن را رد کرد.
او پنج‌شنبه ۱۹ شهریور در مصاحبه با شبکه نیوزنیشن، در پاسخ به سؤالی درباره این گزارش‌ها، گفت: «نه. هیچ خسارتی وارد نشده است. هیچ اتفاقی نیفتاده است.»
کمی قبل از اظهارات ترامپ، شبکه خبری فاکس به نقل از یک مقام ارشد آمریکایی نوشته بود که موشک‌های بالستیک ایرانی در جریان حمله گسترده موشکی سه‌شنبه، ۱۷ شهریور، به هواپیماهای جنگی آمریکا مستقر در اردن، آسیب زده‌اند.
فاکس‌نیوز این خبر را به گزارش جنیفر گریفین، خبرنگار ارشد خود منتشر کرده است.
شبکۀ خبری سی‌بی‌اِس برای نخستین‌بار این موضوع را منتشر کرده بود که در جریان حملات موشکی ایران به پایگاه نیروهای آمریکایی در اردن، «چندین هواپیمای نظامی ایالات متحده، آسیب دیده‌اند».
ارتش اردن روز چهارشنبه ۱۸ شهریورماه با صدور بیانیه‌ای گفته بود که ایران در طول شب قبل، ۲۰ موشک بالستیک به سمت اردن شلیک کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
