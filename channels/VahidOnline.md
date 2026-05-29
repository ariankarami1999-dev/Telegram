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
<img src="https://cdn1.telesco.pe/file/hCnxSinHjZS2qpWEh3tWhj0Nf_JycfJmMRws3OaQihJGnWUd6Ab3VFBLMxzPdCSBfJPtSVnGxeib0VXJE2ojNpCrOEAdzrV4pYOp_6bCsjehWo8RfF-7R0CEzZ-GDnpusprpvX_y2xkLqJNcKzTCvswx2HXLJHK1HIr4JzdPVhaFgsvCsW6L2qkYLHhlQV1rufBMD9cptjzA-GYZgFwLSeKJMPWPcqUAuAaHAciLtKrtD4YsygfpDNJLJtMbaM_B4BSkoqHQQN_n-fvTTz6yGbd4s-dflcsPuDgGU4VxKwRU5wr94OoRXVs7VGmo-P5cHo1maLDpw07BFlUDMLywWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-75783">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPxqb2ejKHZFWdX0znKaahNrkZnRgfzSVHm8EHEbf7_rZTdY-hbp_eFdteo6D31op1O4jyD6Wv7ZudSQurGWbIFx29tzNQ_MNyHSK8N7ktEJuUpCqsOq4poWB7CODlvgCVF6vPzl5EYnK8b6XZY6187QKXFHCQkEPCwPd2smaFqhQeK6f0Ki4IHZG8_BCNNdkH9M-nWPXPsxUcnEOhszrOKqHxJn8OIBdFkTB7J33IEh2BWfS6VDDURhfwPDbbZJiWr-vatR9rPOFCppFr75rmoodY5RuilVv5AXoJF2FESytTOTMMMTrQ3JlXa-7T5pFT7b_RetTAU99b1ZLnj1Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
شیخ تمیم بن حمد آل ثانی، امیر قطر، در تماسی تلفنی با دونالد ترامپ، رئیس جمهور آمریکا، در مورد تحولات منطقه‌ای گفتگو کرد.
دفتر امیر قطر در گزارشی از این مکالمه تلفنی اعلام کرد که شیخ تمیم بر اهمیت اولویت دادن به راه‌حل‌های دیپلماتیک و گفت‌وگو بین همه طرف‌ها به امید جلوگیری از تنش‌ها و تشدید بیشتر در خاورمیانه تأکید کرد.
در این بیانیه آمده است که ترامپ نیز به نوبه خود از نقش قطر در حمایت از تلاش‌های میانجیگری پاکستان بین واشنگتن و تهران قدردانی کرد و «از تلاش‌های قطر برای رفع اختلافات و ترویج کاهش تنش در منطقه» تمجید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75783" target="_blank">📅 02:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75782">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41d327c1f6.mp4?token=oJnwkS-1UgIwO-B8G6VQffAwiuUFZ9sBAClM2OSKMk0E-GOgjILxC1AzfJiCoWy13YyhPYwLj8hY39g3VZs34WwW_Rt_8BpObmLIeppS0Kbr_NXS50DncxfFLVV7kqdmr4zN4MpueMuiIpz1hiF4RL4prelt5B2QDpFU8tr9Q4vIlJLPfQ0fUz11J7g-HGiEO_Zosh_F8vOT33d25KoYg_xPARTuFT8212L4zzn-ATNRLeJDfEK1Z1Q-s-ib_FpNYiadLNxKqLmJ4ygdnpOY8glnuHTPwIArTURQIpAsLvNG_Fz_1z-byF6COdi8h0WQniYimJibjqH5L-eh2TWTCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41d327c1f6.mp4?token=oJnwkS-1UgIwO-B8G6VQffAwiuUFZ9sBAClM2OSKMk0E-GOgjILxC1AzfJiCoWy13YyhPYwLj8hY39g3VZs34WwW_Rt_8BpObmLIeppS0Kbr_NXS50DncxfFLVV7kqdmr4zN4MpueMuiIpz1hiF4RL4prelt5B2QDpFU8tr9Q4vIlJLPfQ0fUz11J7g-HGiEO_Zosh_F8vOT33d25KoYg_xPARTuFT8212L4zzn-ATNRLeJDfEK1Z1Q-s-ib_FpNYiadLNxKqLmJ4ygdnpOY8glnuHTPwIArTURQIpAsLvNG_Fz_1z-byF6COdi8h0WQniYimJibjqH5L-eh2TWTCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز: جی‌دی ونس می‌گوید ایالات متحده در مذاکرات با ایران «پیشرفت زیادی» داشته و معتقد است تهران «حداقل تا حالا با حسن نیت در حال مذاکره است.»
جی‌دی ونس: خب، فکر می‌کنم گفتن دقیق اینکه رئیس‌جمهور دقیقاً چه زمانی یا اصلاً  تفاهم‌نامه را امضا خواهد کرد، سخت است. ما در حال رفت‌وآمد بر سر چند نکتهٔ زبانی هستیم.
کاملاً واضح است که به نظر من، ایرانی‌ها — آنها یک معامله می‌خواهند. آنها می‌خواهند تنگهٔ هرمز را باز کنند. ما هم می‌خواهیم تنگهٔ هرمز را باز کنیم.
🔸
چند مسئله در مورد موضوع هسته‌ای وجود دارد: ذخیرهٔ اورانیوم غنی‌شدهٔ بالا و همچنین مسئلهٔ غنی‌سازی.
پس می‌دانید، ما با آنها در حال چانه‌زنی و رفت‌وآمد هستیم. ما واقعاً فکر می‌کنیم آنها حداقل تا حالا با حسن نیت مذاکره می‌کنند.
داریم پیشرفت می‌کنیم و امیدواریم به این پیشرفت ادامه دهیم تا رئیس‌جمهور در موقعیتی قرار بگیرد که بتواند توافق را تأیید کند.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75782" target="_blank">📅 01:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75781">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP_5iSpGknZxazjKvvvLwW0vOpNAPt9y_kzpAFqA2TQQ5G5PfG4IBDcYNsN7Y5HnoDNnkloiG1-OnCuAhw3xLgDS66bxprTOe-Zt-UnBEjJ199O2LuEr5RECJw56OjyxCNbPgGlBnc2hvRbLleahCfqvyhMEdMjG4AH_Yy-o22xAqOO1RbDxJkCc8y23_A9oEHPN3DnzbdzhoPyc13UAZB4S14M9_OkxdpvlSFd7mnnyDZBQO3UJXQY640CGHiz0CuqdTkI_BeYglBVA3uRVsLImuhCPRNEjgprISEfc3KkuK8ln62BqtoMSQvqIz1K6MYFGjoymGt2A_Vo-i2drBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که نیروی دریایی سپاه شامگاه پنج‌شنبه در نزدیکی تنگه هرمز به ۴ «شناور خاطی» که قصد عبور بدون هماهنگی از تنگه هرمز را داشتند، «شلیک اخطار» کرده است.
همزمان، گزارش‌های منتشرشده در رسانه‌های اجتماعی از شنیده‌شدن صدای انفجار در هرمزگان و بوشهر حکایت دارد.
@
VahidOOnLine
ساعتی پیش پیامی دریافت کرده بودم که در پست قبلی نقلش کرده بودم و الان به اینجا منتقلش کردم. پیامی از شهروندی که درباره یکی از اعضای خانواده‌اش نوشته بود: الان قشم بود. پلاک موقت دادن بهشون گفتند فقط از جزیره خارج شید سریع
همزمان با خبر بالا هم پیام‌هایی داشتم:
صدای انفجارهایی در بندر عباس شنیده میشه.
صدای انفجار داره سمت قشم و دریا میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/75781" target="_blank">📅 23:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75780">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z4q0I53w7bYAIU_Dda-uNkJRuYiZC9xkHqrYcM1IxWUQGHll-VrZSrvMfLt6M-3CPfxNx86pWzpXPQ2emjo0r0u4743v0dFol2UoHXzrwQKBoKM8Qm2stMgPfoN1I0BjPnfui_ZIkPqKVH0p8sSgy4SPXu5y6zzdiG6ToR5HDcX3NgwaCPdnMo0bMahbZQfSXgHQKLBDNy-6Lb4eixrY-9Hy3Hp27P2XFpOTTBFgWnnSM63SWGI-CpEYGKl7PvNGJWBM7TqMNq__shxgK1nt5oEZMmtfcNILExwCRMB0OLbZgErXa8fb8rtIOpWIp1Z_0rjgdOsuuiGogMaGlQgdLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
#جم
در استان بوشهر
پیام‌های دریافتی درباره شنیده شدن صداهایی
:
▪️
همین االان 10/42دقیقه موشک از جم پرتاب شد
▪️
الان جم رو زدن...صدای انفجار زیاد ۲۲:۴۰
▪️
سلام آقا وحید
امشب ساعت ۱۰:۴۶ ۷ خرداد
بوشهر شهرستان جم نمیدونم صدای پرتاب موشک بود یا جنگنده ولی خونه ها لرزید
[معمولا این دو صدا با هم اشتباه گرفته میشن.]
▪️
درود بر وحید جان آنلاین از جم پیام میدم
حوالی ساعت 22:41 بود که فک کنم صدای فرستادن موشک یا رد شدن جت و این داستانا یهو اومد
صدای مهیب و خوبی بود
🔄
آپدیت:
مسعود تنگستانی، فرماندار جم، به خبرگزاری صدا و سیما گفت نیروهای مسلح جمهوری اسلامی «یک هواگرد» را در آسمان این شهرستان در استان بوشهر هدف قرار داده‌اند و اکنون وضعیت منطقه عادی است.
@
VahidOOnLine
یک مقام آمریکایی ادعای صداوسیمای جمهوری اسلامی درباره سرنگونی یک هواگرد آمریکا در استان بوشهر را رد کرد.
به گزارش رویترز، این مقام آمریکایی که نخواست نامش فاش شود، گفت هیچ هواگرد آمریکایی در نزدیکی بوشهر سرنگون نشده است.
@
VahidOOnLine
آپدیت: تصویر بالا
به صور رسمی هم از طریق
سنتکام
تکذیب کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/75780" target="_blank">📅 22:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75779">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_yqJTjWq6RGm1vIi_VkjEyKaBmeHFECf3yIjeN7HHI5JH3MApSUOTVRgOF4EIfm45E08EElYh56T-qXYEqDkjRK7KejWQjxBxMT5jVGRddPCymZcza-QAMtZbhg4S2Wsr1NtTOpd4SAM50eOilEatP7ukI49FjKhEglTTgyN7lc7yGJ90g6Y3-w0d2RtznlbPINEbSfzGYbWOEfDJcqkdNBeYtereWi0d4FSVO4QPJ5GirgqZ73whYFaIH5uTDPx3oIFqwdaRDYNtvX_NVO9CGV26NJpVNx2zC877X23wP859GnfKa942_WlbLFCk2ZzNBLgewQJDaP7noYV_nimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارگان خبری مجموعه فعالان حقوق بشر در ایران خبر داد که تارا و کیمیا داوودی، دو خواهر محبوس در زندان اوین، توسط شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی در مجموع به ۱۶ سال حبس محکوم شده‌اند.
براساس این گزارش، کیمیا داوودی به اتهاماتی از جمله «ارتباط با گروه‌ها و شبکه‌های معاند» و «اجتماع و تبانی علیه امنیت کشور» به ۱۰ سال زندان و تارا داوودی نیز به اتهاماتی شامل «اجتماع و تبانی علیه امنیت کشور» و «تبلیغ علیه نظام» به شش سال حبس محکوم شده است.
این دو خواهر در تاریخ ۲۴ دی‌ماه ۱۴۰۴ در جریان اعتراضات سراسری در تهران بازداشت شدند و هم‌اکنون در بند زنان زندان اوین نگهداری می‌شوند. به گفته منابع حقوق بشری، بازداشت آن‌ها با خشونت نیروهای امنیتی همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/75779" target="_blank">📅 19:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75778">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a7yMLy3aBJccFmyJ4Mi_qrKXAUW96DndYDhbem3DTsNvalgRpc8CwUx4hqyayOsw4VV7chy-1_Zy9g1_-SNqCws6EpVYsbXEL6u04PVC6FXZDwWuWfRLlDLRW_TgalxX6xK_6RsRfJrHGPVBq9IWnDliyYfUN3TO-w-BiUWqYmuO1GJD3Y3oBAD6Rrj5m6OKDtH8-DJsYuOB8cWd00VLce1X0nR3y1F0PE0MdUXP5Z83HlxESzjXoPPYrVH0XBxuve8teL0oq6i_BNu2yX1X9_Hu2urt4Yl9UIJ0Ak2qL0lc9tvwJUD3t1qD-h1KpADcnFq70EtGUoBHIrODWDSJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از مقامات آمریکایی گزارش داد که مذاکره‌کنندگان آمریکا و جمهوری اسلامی به یک یادداشت تفاهم با مدت ۶۰ روزه برای تمدید آتش‌بس و آغاز مذاکرات درباره برنامه هسته‌ای ایران رسیده‌اند، اما دونالد ترامپ، رییس‌جمهوری آمریکا، این متن را هنوز تایید نهایی نکرده است.
مقامات آمریکایی که نامشان فاش نشده به این رسانه گفتند که شرایط توافق تا سه‌شنبه تقریبا نهایی شده بود، اما هر دو طرف هنوز نیاز داشتند تایید مقامات ارشد خود را بگیرند.
مقامات آمریکایی افزودند که طرف ایرانی اعلام کرده که تاییدهای لازم را دریافت کرده و آماده امضا است.
تهران هنوز این موضوع را تایید نکرده است.
اکسیوس نوشت مذاکره‌کنندگان آمریکایی جزئیات توافق نهایی را به ترامپ گزارش دادند و او درخواست کرد چند روز برای فکر کردن زمان داشته باشد.
@
VahidOOnLine
بعدا
فاکس‌نیوز
هم خبر مشابهی منتشر کرد.
و گویا به همین دلیل هم می‌خواستند اینترنت را باز کنند. پیروزی جلوه دادن با اعلام جشن و پروپاگاندا در جو جام‌جهانی و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75778" target="_blank">📅 19:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75776">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/La7jo8zpY22FTs_GNFMp_m3Oqs9W5zjH5E-Nb1JWIUzhB5-gFQPkn639avq8a_IrG_ganCbEYlD_cUH-PCP_mx_zcwtgll4LBhFNvEBuIMRdQ-KFxprPeg7K5MyGxdVUlFLPWGuK8xeGhF8r4MqtbTVk6ROvJUwBJPKiJTsEolvsfKcuP2YahhnCE6hijgrnDo2oWJrvPQRkz_FcaUOCJvy74YfrqcIJsSrkAH55XH8YD-Ui8q6dJwboBwdtbUmHQKnr9PYeeCjGxa_9QNJexBFWUtKk51rewyXC61Dhk6ePRfsfPI4cUBO6DkPMNG8TgWARqfY-SeiI2eClbzzJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BAR8S0E4GuZ9tCvdzTc4fsb9KspeFQdgwqjgKEeNcWwSX7Xzz3UPpuqYJUVUizVNdQqSmbHFgAZ1pBnwnLGU1sjafrz5SQ_8LpqEmC-gEhxpEa2v6muAtcLJe81SQ65j-rzFjVd8j1G3EdHZabgpmak6zOmo-S1QrTL4chAJif3b4FVr6lKeHbnEq9yCubJ2K5yiyBxX3gzFIkhvuMejNXMb_HCvF8qd-1lArlAAN-vUlVeWCJz76kLKSM0VIstvUBnrvgKHhLMWi6b2DfsC0ePzAEr-S9iBAWC08n3nGQuWhomQT0lbyEImJ2Fgg8jmT6EmKmrba5SSNH-KyMF0tA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پس از انتشار پیامی منسوب به مجتبی خامنه‌ای درباره «نابودی اسرائیل تا ۱۵ سال آینده»، رسانه‌های ایران تصویری از دیوارنگاره جدید در میدان فلسطین تهران منتشر کردند که بر آن جمله «اسرائیل ۱۵ سال آینده را نخواهد دید» نوشته شده است.
در پیام منتسب به مجتبی خامنه‌ای که رسانه‌های ایران آن را منتشر کرده بودند، آمده است اسرائیل «به مراحل پایانی عمر منحوس خود نزدیک شده است.» در این پیام به سخنان علی خامنه‌ای در سال ۱۳۹۴ اشاره شده و تاکید شده است که اسرائیل «۲۵ سال بعد از آن تاریخ را نخواهد دید.»
@
VahidOOnLine
سپاه پاسداران روز پنجشنبه هفتم خردادماه با انتشار بیانیه‌ای به مناسبت کشته شدن محمد عوده  و عزالدین حداد، دو فرمانده حماس اعلام کرد منطقه جز با محو اسرائیل روی آرامش نمی‌بیند.
سپاه در این بیانیه از حمایت جمهوری اسلامی از «محور مقاومت» تاکید کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75776" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/krrn7olbm3BRCfG9y3gf2IjflqDMwH62zCsl6S5Spkqj06VKY0oH0YbyX32lFw6AKnaf7Dr15FzVInuV4kHYlrKugrkFvZdRJwk1whkLzg1nwNi1MEBSF_MmER9ZrvjlArz7TqyBa-_ln81TEvgA_-1MufyxTkZzigYTuG2N13CuTMG9bAuQ59QyZr_r15O3Yy1apTeI7LxalkbOLyiIpEobzEqgplaJ65zxVq4nt__izYorfAYHhBtXEIaGQRIwjsyvdupbTNGJL9BpodACSwqp7gGhinaWB1TB6BbaLxidKdfU1TVeKRU28riZQXn996J5ZblA3Rp-JYiP7w6uqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W5wFk2NIGVsNvFHyvOpnjQ3KISyeoNK8FeOKojL8Aux95c8OFRIr9qev2s7jSkFFPN6-MwJLPvToPpndQrueHqb6S4wypKyGPHGGt_qCD65xdT0_GWEX7I21XFpze9_v81ECumYhEIReciSoHjYhQw9lmwO78q-zFCg3rZ0hxSDBVNQ723qiEqDAmLGdyyKF_dE9nw8JHPHKn4G1Nm7Z7L-8-hbyS35DeZabCvu4zTrP5tCDjq4_1jiV3hQTeRug5aB3UcvDQY2iNacg_SOLDh1xzVoWvNEXRMvQoPUv_ywXVFKn4homyuguWKUIt09fHU263BwwK60fEEVGRKROMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنج‌شنبه در پیامی در شبکه ایکس نوشت که ایالات متحده در راستای افزایش فشار بر تهران و باز نگه داشتن تنگه هرمز «دسترسی هر دو شرکت هواپیمایی ایرانی به اماکن فرود، سوخت‌گیری و فروش بلیت را متوقف خواهد کرد»، اما جزئیات بیشتری ارائه نداد و به نام دو شرکت اشاره نکرد.
@
VahidHeadline
اسکات بسنت، وزیر خزانه‌داری آمریکا، با تاکید بر اینکه این کشور به کارزار «خشم اقتصادی» علیه حکومت ایران ادامه می‌دهد، در شبکه ایکس نوشت نیروهای جمهوری اسلامی حقوق دریافت نمی‌کنند، پلیس‌ها سر کار حاضر نمی‌شوند و جزیره خارک تعطیل شده است و اقتصاد و ارزش پول ایران در سقوط آزاد قرار دارد.
او افزود سازمان مدیریت تنگه هرمز از سوی جمهوری اسلامی یک شوخی است و امروز وزارت خزانه‌داری آن را تحریم کرده است. ما به هر نهاد شرکتی یا دولتی درباره پرداخت عوارض یا پنهان کردن آن به‌عنوان کمک هشدار داده‌ایم.
بسنت اضافه کرد با تشکیل «دیوار فولادی»، محاصره دریایی آمریکا باعث شده میزان نفت خام ایران در دریا به پایین‌ترین سطح تاریخی برسد.
او تاکید کرد تنها یک نتیجه رضایت‌بخش در مذاکرات این روند نزولی را متوقف خواهد کرد.
@
VahidOOnLine
دولت دونالد ترامپ نهاد موسوم به «سازمان تنگه خلیج فارس» جمهوری اسلامی را تحریم کرد
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75774" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75772">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WRBUNinpC6rHAgZM0ERzT9u74yxeUERHPNWBH5r9BtJ5f8TBmx3JG6JUumLoOCkZE5JMhcFMqZntxzN5DE4oyPPBXyZqPF1LN5AuQSSA39BQcVb90fdNz3g0rVS6AWBuES6tss5b0c6yHmmkgXFsmncUOpDrd5nFRqC6nxnLpxx-0WtTfs7q8MBt61ImPAq7dOB_RbWBBS2J-pB_BGqY8GVZnafEkQg8e80SQfPTq4FgAk1U3OVTSRXQ5YXSHTk6MQG5UOF4_EfhsfYpxEDaFqOY75PFa5M_H7U1t-MDcv23nQYSM3YxQIRzxtbDiw1uMUeKBH-XntlCecZwWOXnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QLEOg4FmgBwFhcNjGS2x3JryWHjtVdFRf-F-oGyapDDkFXDa0nsLp30fEin9Y5JSlRJ_-f2BFqmGevDWdbn1WE66RYftU2cTzo-j4LCfLo5RmHlNhPZ0hWXS7cNgYd485hr-QiCHh2Rpa9gjZWgyUsBPhsJhZIjEv1j5X5pglTftzi6-UQ2YL07zMIw84xTcK-fyjO9305TsQIbsFFnMk8IH1OteO0nvNjdHaiKRWpbyAXvWAAoPvo7IUKaoy2ljaOx56Cg43yq20RokzyQLUWywPOswTGMMnGbDVFc7iIfCX5TizyOE_ZCcqFvxMg_4pbspF3PrH-i9rb9uUo_ffA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت خارجه کویت حملات اخیر موشکی و پهپادی رژیم ایران به خاک کویت را به عنوان یک تشدید تنش جدی و نقض آشکار حاکمیت و امنیت محکوم کرد.
این وزارتخانه روز پنج‌شنبه اعلام کرد که تهران را کاملاً مسئول حملات اخیر می‌داند و حکومت ایران خواست فوراً و بدون قید و شرط حملات را متوقف کند.
@
VahidHeadline
اسماعیل بقائی سخنگوی وزارت خارجه ایران، حمله بامداد پنج‌شنبه آمریکا به مناطقی در بندرعباس، را «تجاوز» نامید و آن را محکوم کرد.
آقای بقائی این حمله را «نقض فاحش حقوق بین‌الملل و منشور ملل متحد» دانست و افزود: «شورای امنیت سازمان ملل موظف به ایفای مسئولیت قانونی خود برای پاسخگو کردن متجاوزان آمریکایی است.»
سخنگوی وزارت خارجه ایران می‌گوید آمریکا «به‌طور مستمر»، آتش‌بس میان دو کشور را که از ۱۹ فروردین اجرایی شده، «نقض» می‌کند.
سنتکام با این حال تأکید کرده که این اقدامات «سنجیده، صرفاً دفاعی و با هدف حفظ آتش‌بس» انجام شد. این دومین بار در سه روز گذشته بود که آمریکا اهدافی را در ایران هدف حمله قرار داد.
@
VahidHeadline
فرماندهی مرکزی ارتش ایالات متحده، سنتکام، حمله موشکی ایران به کویت را «نفض فاحش» آتش‌بس خوانده است.
این نهاد در حساب رسمی خود در شبکه ایکس نوشته است: «ساعت ۱۰:۱۷ شب به وقت شرق آمریکا در تاریخ ۲۷ مه، ایران یک موشک بالستیک به سمت کویت شلیک کرد که با موفقیت توسط نیروهای کویتی رهگیری شد.»
سنتکام نوشته است «این نقض فاحش آتش‌بس توسط رژیم ایران، ساعاتی پس از آن رخ داد که نیروهای ایرانی پنج پهپاد تهاجمی یک‌طرفه را شلیک کردند که تهدیدی آشکار در تنگه هرمز و نزدیکی آن ایجاد کردند.»
فرماندهی مرکزی ارتش آمریکا می‌گوید: «تمام پهپادها با موفقیت توسط نیروهای آمریکایی رهگیری شدند و آنها همچنین از پرتاب ششمین پهپاد از یک سایت کنترل زمینی ایران در بندرعباس جلوگیری کردند.»
سنتکام در ادامه آورده است: «فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای کماکان هوشیار و محتاط هستند و ما همچنان به دفاع از نیروها و منافع خود در برابر تجاوز توجیه‌ناپذیر ایران ادامه می‌دهیم.»
@
VahidOOnLine
وزارت خارجه عربستان سعودی در بیانیه‌ای در شبکه ایکس، حملات خصمانه با موشک و پهپاد به کویت را به‌شدت محکوم و تقبیح کرد.
@
VahidOOnLine
وزارت خارجه قطر در بیانیه‌ای هدف قرار گرفتن کویت با موشک و پهپاد را به‌شدت محکوم کرد و آن را «نقض آشکار حاکمیت» این کشور و «نقض فاحش قوانین بین‌المللی» دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75772" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75771">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1QNtFwBh-Razq-S7N1qU81u8Lg-zTOgYCAIrRCocyr4DXsBYetzulqor3LmMQkZhGY3vaNAQW1o9nJksAdLMKXGsc3K3f9O4-9xLDiZdE49G-kJZDVzAvJ55gXLVYM_4113hwEDZpZk35TBXCrNaN5RaYFqlblT8T8jccJa_90mn-qWDAJOYoilcPERqJwAJDbg5rOUHsAIf-oIbZm_pInJSc8U49CJ4nauaV0viKinrhP5wexLxMrDYo8pU7ntZHEHedGAd_r-DmhqkChvvqRowViTrczvJuRSmCW5_e1vaBhznBnJNV25jOSPaKAy6me2YSE9xbEOuzkGG5NVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پیامی منسوب به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، را خطاب به نمایندگان مجلس شورای اسلامی منتشر کردند که در آن می‌گوید «ایجاد تفرقه و تجزیه اجتماعی»، در کنار جنگ و فشار اقتصادی و محاصره، «طرح و نقشهٔ کور دشمن» است.
مجتبی خامنه‌ای در این پیام که روز پنجشنبه هفتم خرداد منتشر شد، همچنین به تمام کسانی که آن‌ها را «جان‌فدایانی که دل‌شان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد» نامیده، هشدار داد که «اختلافات غیرموجه و حتی موجه را به تنازع و تفرقه تبدیل نکنند».
وزارت اطلاعات جمهوری اسلامی روز گذشته در بیانیه‌ای هشدار داد که بعد از جنگ اخیر، «برخی کمبودها و گرانی‌ها» در پی فشارهای اقتصادی آمریکا می‌تواند باعث بروز ناآرامی‌های تازه در ایران شود.
وال‌استریت جورنال نیز روز پنجشنبه در گزارشی به نقل از تحلیلگران هشدار داد که ادامهٔ محاصرهٔ دریایی آمریکا علیه ایران که به کاهش ذخایر ارزی ایران انجامیده، می‌تواند احتمال بروز اعتراضات جدید در ایران را افزایش دهد.
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی از او منتشر می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75771" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i56q8fgaVbmaP5-TmI0neNk5VZ7mU9AVP-zxnF4FP__IJrW2tFf11bk38nVFP2BgC5a5TCEMXC7hJL3PbLN-If3BqKRAU57fi9ptOjNb9YhyaHiwE3w1DHrpTA-AqTJ1XxD0hxrFC744Ed1cy26yMIJdfV8WzGu2sZEVfbtVn0Rv--h3VMQ1x9U7Qb2FppGnMaZaxx387ImPGhgredQe034VRMNC1dy6eG30djjUwzrApjb2gjNfELMSY7jgu_TpsjXmVpLPs6DlVP6Oe7PsUpoyHSx4xDegM-0IAsvw0wl61Fp_6_zfqDTVm-v8oX52xn3n9U4dy8u-iPl3q0je7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دادگستری آمریکا اعلام کرد «جاناتان لودهولت»، شهروند آمریکایی ساکن استاتن آیلند، به‌دلیل مشارکت در طرح «تعقیب و قتل» مسیح علی‌نژاد، فعال سیاسی ایرانی-آمریکایی، به ۱۰ سال زندان و سه سال آزادی تحت نظارت محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75770" target="_blank">📅 18:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75769">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PA7iSJwZdE0QcdCsIQxqPY7xt8I-4h1ak6i90ixpAlDyMf4u-XXvJ6O1t8ozpIcCUkYRaGKY-QV8Y6KJ3KW6Up8A6MUzt4Cmo4Ilewj2pobQ85OjTIRKZ76fHvtrLZCyjMH3tc_-bGKO9-_Ybm10AgwB24CXwfffoF3PRb2g3BqCFcjjPWVMDuk6RwTRrutXxjXm7ymW7yI738_Csyv2LzAA2VYx0AbBJ2LJKy4Xn_bVY7mLG1-AxN5qgT9AC6NVEFAguOClNxKd6YDGLYhj9kslvoKqKgsfhu2e7a0oojLd0aEklaBbcIc0NblXuj-2JlJOSfZ2lcu-bp4AWQuHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محمدباقر قالیباف»، رییس مجلس شورای اسلامی، در پیامی به «غلامحسین محسنی اژه‌ای»، رییس قوه قضاییه نوشت: «قوه قضاییه زیر بمباران و تهدید دشمنان دست از صیانت از حقوق مردم و برخورد با قاتلان داخلی و خائنین به ملت نکشید و خوش درخشید.»
این تمجید از عملکرد قوه قضاییه درحالی صورت گرفته که در طول روزهایی که از جنگ ایران با آمریکا و اسراییل می‌گذرد دستکم ۳۹زندانی سیاسی اعدام شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/75769" target="_blank">📅 18:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75768">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCW4dWfrCO78WQelVFFmzCOTljggAzHBKw1tKBYpPhG6pED7xmd6qATlnGCNX5Uql70tNZnf9Mn1t2anlJtzDhcVHrW-M8mAMGgbLkLblRQoqubsclk-glYwScIlZ_nPXGynQNCdAXe_VdpjiADKcFebDOluxEJpcUIi8Lq4MDje4aBxAdAHhWt5j-ED48g6G-mPbFvh5H_miHWF-kbTVhFRuHYaVZBZBiwNWPUjxmtfmYMP1X9kxkVGcUnFR4OFFZYxgaD3eUfBH28TTXEPi-14Orllte_DxyFc0bRmB_UKQ3dgLXBWBW0G_BmEX16ZWMJfFwoqs1oPfyHpVKDD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس، نهاد ناظر بر اختلالات اینترنتی، اعلام کرد که علیرغم اینکه دسترسی به شبکه جهانی تا حد زیادی در ایران بازگشته است، اما شاخص‌ها نشان می‌دهند که کاربران همچنان با فیلترینگ شدید مواجه هستند.
نت‌بلاکس، این فیلترینگ شدید را مشابه دوره مابین اعتراضات سراسری دی ماه و آغاز عملیات نظامی علیه جمهوری اسلامی، حدفاصل دی ماه تا اسفند ۱۴۰۴ توصیف کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75768" target="_blank">📅 18:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75767">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HLzROFGv8YcqwCqr5aFhUqGXVzK-jee9InL6za30zhXK4SiEVXKxpF5fVVRjEfXjALZL5SZYKLAIRC6rhvCdH0ZticraL_4AxfDBUQ3KWmX8AKy-MGb4amhnmacDki6RGc6ZHWLEwd20qs8wzmk3Eom6gc3Ii5q82DxIWQJi5-3cYUytsuAPsAvKmfEtUgdKJoYXxJkZpN1wZGoBG_tY_IlQgeiTlLVQ5Q0r4C1YhUuT3gqSVCS5mqHmDQZ8YSqmC2FgCnOiyeyvdPQkippv4vwxp-dWPMVC4oiKrtbRDxTOWBacURPd0sB6uQk-kuAzqZaqhZmP2TQHxWJzwReOiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تصاویر پیکرهای بی‌جان و شیون مادر  تصاویر دریافتی از: 'بیمارستان الغدیر #تهران، بامداد جمعه ۱۹ دی' Vahid #بیمارسان_الغدیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75767" target="_blank">📅 18:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75766">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e61830c9f.mp4?token=tq1kk0JXFshBQINWIM-MTJN5jMUhxOfewHlwYNbDkHebWx-mfdIjVCavC-gUj_mwTrjI0NSClZ76fiqJ79ehP3zHw0tbu6ITI5z-1EYJdpUi2YF0EZX5GnN2qOYnE7kEM94rAyIzQwvrF4Cw236R_yufUIrW-f0LhlV1Y40-zAMfKJsbxgOQWj-IfX_s10dVRPfgPUE66NlFZQ03BNI7gWygoNrL8Fpk7PsNgwHvCfcsKJZ9B2150vywMW4-jS41Y2Ux1jRo3PM7ZQvR0Ev4HsWH0CLHiwvcEGi56Z48eyOcPzfS4lujCaS30nSzCLvCq3-7YQkCEkc_xulB3bPkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e61830c9f.mp4?token=tq1kk0JXFshBQINWIM-MTJN5jMUhxOfewHlwYNbDkHebWx-mfdIjVCavC-gUj_mwTrjI0NSClZ76fiqJ79ehP3zHw0tbu6ITI5z-1EYJdpUi2YF0EZX5GnN2qOYnE7kEM94rAyIzQwvrF4Cw236R_yufUIrW-f0LhlV1Y40-zAMfKJsbxgOQWj-IfX_s10dVRPfgPUE66NlFZQ03BNI7gWygoNrL8Fpk7PsNgwHvCfcsKJZ9B2150vywMW4-jS41Y2Ux1jRo3PM7ZQvR0Ev4HsWH0CLHiwvcEGi56Z48eyOcPzfS4lujCaS30nSzCLvCq3-7YQkCEkc_xulB3bPkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'رد موشک شلیک شده در آسمان
#امیدیه
خوزستان، پنج‌شنبه ۷ خرداد'
Vahid
☄️
سپاه اعلام کرد در واکنش به حمله‌های پرتابه‌های هوایی آمریکا در سحرگاه پنج‌شنبه به نقطه‌ای در حاشیه فرودگاه بندرعباس، یک پایگاه هوایی آمریکا را که مبدا این حملات بود در ساعت ۴:۵۰ هدف قرار داده است.
سپاه تاکید کرد در صورت تکرار حمله‌های آمریکا، پاسخ جمهوری اسلامی «قاطع‌تر» خواهد بود.
@
VahidOOnLine
رسانه‌هایی که بیانیه سپاه رو نقل کردند، از جمله خبرگزاری رسمی جمهوری اسلامی، ایرنا، نوشتند "ساعت ۴/۵۰" حمله کردند که یعنی چهار و نیم ولی با توجه به اینکه با دو رقم اعشار نوشتند احتمالا منظورشون چهار و پنجاه دقیقه بوده.
اما این هم عجیبه چون آژیر در کویت و پیام‌ها از امیدیه مربوط به ساعت ۵:۵۰ بودند!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/75766" target="_blank">📅 06:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75763">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uBh1kXMtga0rwYHUM3Wf8rorXE01GJ3N6RIUpn1rZgvA2fVur1VUNwIQSXaBd3rxFc26lNMDvYhO_HNvCVJvBNkBCtvm5pMg4MTTHTncajmkYCQr2peyjPuBbVnjzIy3bbtQj2XWwqgutLIy3o3_st66Dw95r7LeUJ7rNvoewT00BMI38m_VIh_r_HF4kj2gdycIUz5XnftuL1qMkdEFNC6gmle03YC0dRiki4Z0pPP3O7jGnnPYmqjhe_kOv8dJAejUSWJdWvNPeJN9glGpa2U-mjfGJBSP6wu-L6_7y3IGTBhdJrqNsuEF6BA8AWNOG4gLC1itRnV6hZQLB6PfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eNtfAwoi_PQOUgH7CSBQIRKuZ026aQFlzzCvgEe63nu521ZJIOTbHcp_7oENYpXyGTsRbA6mLtiGUQQCxP_RVnS2g8Dl7e9gxPq2RSVoTjzxwVcPsxJ4TOhOv-HpovEXuPZHF3oJldVZwrcK8pC27RmisRLGGHPr1wua8bm8bdE71xpcvb60M8neaBBAIxRr2nIyCAXnMsmXQb6PS7rJWevojw67yFS3ikxiHqPJEscfeYUCiphAT5Cm3mDp821m6A3toCA_HJpVA0r62d2gSuNnWxMz19jBr-_Bz4K807IRPsp9WfX-nLDKAIXu1vbY8u1kxmxGd0xvlnZnZwgT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TZWqkb6UtuqHB2AtNvnlIvWteu1hl97kYTr94OfQsnwO7J--XS0yL9JxeUpw7OaSaitfhepMqLvbTxqUjWNgSiXtj26FY8UaJC3tgYEwh65a0zpw2OimLtrMTvp7VQaLfN99U4fVMJ3xMz1Fpd8j3BYXHyZP_TZPIwxXv8vR5vTfkxsgwylGAZ6toagHzpd8HCBOSjy1LE1BBt05N_B8_zrBHlqGf6959_oSnt2UqElCPQEPRyyBlzvywkWtjiw4UdKOwFxp8NK2ZsPUnF2hv0aC60zC2ywXrTeLR8SmGP9dGIywJvg2s2AwhyM83iMaBJjgVixsMRpXgTGEbjNxYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از
#امیدیه
در خوزستان پیام‌ها و تصاویری دریافت می‌کنم  که میگن حدود ساعت ۵:۵۰ موشکی شلیک شده و سمت تونل امیدیه میانکوه صدای انفجاری شنیده شده.
یکی نوشته لانچر هدف گرفته شده.
دقیقا میشه هم‌زمان با
شنیده شدن آژیر در کویت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/75763" target="_blank">📅 06:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75762">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MYSGcIzl863tPdPrJjVqXxRFcMzH5gTTcYeeK9TOSpIwgexvrBgAF9uNSb0bWE3nbbi1A1h_QBrg8FNFIFwI3YgtRnYHwOnIGdN5QopdCh60GOIIR7WVRVVEEzKb5uYWOPeyO2o-yn00Li5YeQeznOULL-bANKXsPbJIXleZRG3_QNPd_PgJaR-k5qP3x0EGc_7R40Taxlfr7WFniSjhUbMmGb5dEqedlzPp86qTrGHZh4rOW-ztjvPTPO8ZPcQ0ojcUyduNedLpDxvtSL97b4xhPoyUH2GlJiJleiEal4O8HyF7ooR9393uc5khGdtfKTPw1aiLhJHUzl95tMIyQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید الان کویت رو زد ۵/۲۰
وحيد همين الان اژير كويت فعال شد
سلام صدای پدافند و تقریبا ۲ تا انفجار در کویت
درود وحید
🙋🏻‍♂️
اینجا ساعت ۵:۲۰ به وقت کویت صدای اژیر اومد و رو گوشی ها هشدار اومد
ولی هنوز هیچ رسانه‌ی کویتیی دلیل این اتفاقو نگفته
آپدیت:
ارتش کویت اعلام کرد سامانه‌های پدافند هوایی این کشور حملات موشکی و پهپادی «متخاصم» را رهگیری کرده‌اند، اما مشخص نکرد این تهدیدها از کجا منشأ گرفته‌اند.
ارتش کویت در بیانیه‌ای اعلام کرد صداهای انفجاری که در کشور شنیده شده است، ناشی از رهگیری این تهدیدها توسط سامانه‌های دفاع هوایی بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/75762" target="_blank">📅 05:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75761">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mmcfS3IRChxuHqE_cUEsx34kwqeWMiwXkaTqDm2BKCMMpkGGrjx32y6wM4lht5eKkiDeoHTU0KqTqFA2HFud2YQEuhCZR7WotXktWOA3pjyY61Je1Nugs7KJpbwMaSdRZM_vqxb-JsZn7FaygzqOnprU53qD3C9BPgs6i3UHexbChd08oTDldzwySfM8E5Gib4RHXmJymM0v4a3odd8RqOLKSa389Zhf7kaDzfe36jyi9mQkwoMgozK6u1pRD4DK-C7h31ycV05iUp-fxztfEWC5dwme2zBUPgICv4fnPwr50cmwhjNXgT8juRFmYZqLdfCmWVMnWQfLGGZb5C4sPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسوشیتدپرس به نقل از مقامات آمریکایی گزارش داد که نیروهای فرماندهی مرکزی آمریکا چهار پهپاد تهاجمی یک‌طرفه ایران را که در نزدیکی تنگه هرمز تهدیدی ایجاد کرده بودند سرنگون کردند و یک ایستگاه کنترل زمینی را در بندر عباس هدف گرفتند که در آستانه پرتاب پنجمین پهپاد بود.
@
VahidOOnLine
در همین حال، خبرگزاری تسنیم، نزدیک به سپاه پاسداران، به نقل از یک منبع آگاه نوشت: «ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.»
تسنیم درباره حمله هوایی آمریکا به نقاطی در شرق بندرعباس نوشته نیروهای آمریکایی «به زمین سوخته‌ای در اطراف بندرعباس شلیک کرد که صدای انفجارها مربوط به این ماجرا بوده است؛ این شلیک هیچ خسارت جانی یا مالی به همراه نداشته است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/75761" target="_blank">📅 03:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75760">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">#بندرعباس
پیام‌های دریافتی:
چهار تا صدای انفجار پشت سر هم اومد الان
ساعت ۱:۳۳ بندرعباس
درود آقا وحید همین الان سه تا صدای انفجار اومد تو بندرعباس ساعت ۱:۳۳ دقیقه
حاجی صدای انفجار دوباره شرق بندرعباس همین حالا  سه تا پشت سر هم ساعت1/43 دقیقه
سلام وحید
۰۱:۳۳ شب
همین الان بندرعباس صدای ۳ تا انفجار اومد
سمت بهشت بندر
احتمالا باز مثل سری قبل باند فرودگاهه
بندرعباس ساعت ۱:۳۰ هفتم خرداد صدای جنگنده بعدش سه تا صدا انفجار اومد
سه تا انفجار بندرعباس
ساعت 1 و 33 دقیقه بامداد پنجشنبه 7 خرداد صدای سه تا انفجار رو از بندر عباس کس دیگه ای هم گزارش کرده ؟
شبیه صدای موشک زمین به هوا بود
بندرعباس صدا اومد
سه بار
درود. ساعت ۱:۳۲ دقیقه صدای سه انفجار شدید در بندرعباس اومد و خونه شدید لرزید.
ساعت ۱:۴۷ باز هم صدای دو انفجار دیگه اومد
صدای سه انفجار بندرعباس همین الان
سلام وحید جان بندرعباس چند انفجار وحشتناک پنجره خونه لرزید 1.38
دباره زدن بندرعباس ساعت 1.49
۳تا صدای انفجار بعد صدای پدافند
سه انفجار پشت سر هم و یکی هم ده دقیقه بعدش بندرعباس رخ داده
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/75760" target="_blank">📅 01:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bHphx1EIMQbZ4A6cT0O2ZiBAEk6nhLNd5GlRfZw7X8r336OzM5gooLnQHPVRnn5qlDiS9N-HpVHAOxddbzHQvEk2es1QYuW8HiXBu6E5cOj1DyGDM5VGjW91WIakYJ58Pa6LUsaCRThkre-gR9ehCC1BasC82Bwbz1rHaSD9bMufFro69k8IG4EiVCiL3mPNzo_ffxc3PNouM_lQrX4C_-oeqtsVOUJQomyf8VUmI3eFQMxLy0z5r1wblkWbRPA76VXDUQ7c7lfp7WK5hwBPQnM50ur1cOzAPfq6YkZj7HB2lRVGVAzQ40fM68KQF94uMvDPAgkrGHZ-nYtL4suDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c97c6720.mp4?token=fWESTQnOvvmSS5aSi-4BPPmmfLpv2nImx261ma2zZ84YHiWSWJ55GQqBe9B56V8-9yncIfhzKmZRCASV0PJ7U89BQyVgTknSTVzwtY9mvyKvwTryzaB5ZJFvARlO5sFA_iBcBH-eYlQ02cyvp9hsFmhILesPTXntt73ePtyBpj56NRbGAWdD_imp7Ey7_TNdWWJpMHEQamk-tOM7AlUhWhuR37iZrt2936J5AtS48I4wuvMx2hNtDBWcvB4u0TTsUqv7vu1bN-P6c6tDxYBROjYlc3u4KEw77xaD7fCMQgAadJVYaTA97Hqjhyiw9sROiNWA044iVtKcPB5ntE7c8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c97c6720.mp4?token=fWESTQnOvvmSS5aSi-4BPPmmfLpv2nImx261ma2zZ84YHiWSWJ55GQqBe9B56V8-9yncIfhzKmZRCASV0PJ7U89BQyVgTknSTVzwtY9mvyKvwTryzaB5ZJFvARlO5sFA_iBcBH-eYlQ02cyvp9hsFmhILesPTXntt73ePtyBpj56NRbGAWdD_imp7Ey7_TNdWWJpMHEQamk-tOM7AlUhWhuR37iZrt2936J5AtS48I4wuvMx2hNtDBWcvB4u0TTsUqv7vu1bN-P6c6tDxYBROjYlc3u4KEw77xaD7fCMQgAadJVYaTA97Hqjhyiw9sROiNWA044iVtKcPB5ntE7c8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره لغو یا کاهش تحریم‌های جمهوری اسلامی گفت واشینگتن «درباره هیچ‌گونه کاهش تحریم‌ها یا دادن پول» صحبت نمی‌کند و تاکید کرد: «هیچ تحریمی، هیچ پولی، هیچ چیزی.»
او افزود آمریکا کنترل پولی را که جمهوری اسلامی ادعا می‌کند متعلق به خود است در اختیار دارد و این کنترل را حفظ خواهد کرد. ترامپ گفت زمانی که جمهوری اسلامی «رفتار درستی» داشته باشد و «کار درست را انجام دهد»، اجازه دسترسی به این پول داده خواهد شد، اما «در حال حاضر چنین کاری انجام نمی‌دهیم» و «این دو موضوع به هم وابسته نیستند.»
ترامپ همچنین درباره انتقال اورانیوم غنی‌شده گفت با انتقال ذخایر اورانیوم غنی‌شده ایران به روسیه یا چین موافق نیست.
@
VahidOOnLine
دونالد ترامپ در پاسخ به سوالی درباره کنترل تنگه هرمز توسط تهران و عمان گفت این تنگه برای همه باز خواهد بود و آب‌های بین‌المللی محسوب می‌شود. او تاکید کرد هیچ‌کس آن را کنترل نخواهد کرد و آمریکا بر آن نظارت خواهد داشت.
ترامپ افزود کنترل تنگه بخشی از مذاکرات است و ایران تمایل دارد آن را در اختیار بگیرد، اما چنین اتفاقی نخواهد افتاد. او درباره عمان نیز گفت این کشور مانند دیگران رفتار خواهد کرد و در غیر این صورت آمریکا مجبور خواهد شد آن‌ها را منفجر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/75758" target="_blank">📅 21:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rQuOrNISAXxsm-LeBDVtDoSiPqML_DanZYmLubhyp4JHHhG8Ko5qXc5bPUlebqkQ01MwglUi-1T2SpZPD0XYEXPDQmlpXm5y0HPv2_S1so6i-JZUN_U-pp29dig0uK60oF-4o8xZzJU7b1O5fY4OgUBilpqF5G6IGGEZ7NxP8HatDy0QsHAV2sdbdGEqm_h4FS4hqn0uSEOVlR87J-WqOXvOxlwTyYwGLiw5-gM6hqLVMlEYiEezAkEmaUvStPCpmuo7j4Dht-V9TjHRdw4DQz9jITBhhw60pRzZBU5jIxk0ac542GQcl8Piw38SZb545nuABMVXJ9-Mv2pMqtCY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه گفت که ایران در ازای کنار گذاشتن اورانیوم با غنای بالای خود، از لغو تحریم‌ها توسط واشینگتن برخوردار نخواهد شد و از پیشنهادات ایران برای توافق پایان جنگ ابراز نارضایتی کرد.
ترامپ پیش از برگزاری جلسه کابینه خود در یک تماس تلفنی کوتاه با شبکه پی‌بی‌اس نیوز، در پاسخ به این سوال که آیا توافق فعلی به این معناست که ایران در ازای لغو تحریم‌ها، اورانیوم با غنای بالای خود را واگذار خواهد کرد، گفت: «نه، نه، اصلاً. خبری از لغو تحریم‌ها نیست، نه.»
او اضافه کرد: «آن‌ها قرار است اورانیوم با غنای بالای خود را کنار بگذارند، نه در ازای لغو تحریم‌ها. نه، نه، اصلاً.»
ایران بیش از ۴۰۰ کیلو اورانیوم غنی شده تا حد ۶۰ درصد دارد که در تأسیسات زیرزمینی هدف قرار گرفته در جنگ ۱۲ روزه سال گذشته مدفون است.
رئیس‌جمهور ایالات متحده ساعتی بعد در ابتدای نشست کابینه خود در کاخ سفید گفت که ایران بسیار مایل است به توافق برسد، اما آمریکا هنوز از توافق پیشنهادی رضایت ندارد.
ترامپ در این نشست در حضور خبرنگاران گفت: «ایران خیلی مصمم است، آن‌ها خیلی می‌خواهند که به توافق برسند. تا اینجا هنوز موفق نشده‌اند... ما از آن راضی نیستیم، اما خواهیم شد.»
او سپس بار دیگر ایران را به ازسرگیری حملات نظامی تهدید کرد: «یا به آن نقطه می‌رسیم، یا اینکه مجبور می‌شویم کار را یکسره کنیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/75757" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/In5MTg8vmDfPSZ0bPv8hS2TjU2HI7h9at2OMvPIkW92hgCrvx_VqdJKsXVZ1zfoOpOrYQfwg_JF9-vDeWgpcNrT5D-WLZ-4xi0aQcmDKaEU78Ex5ItMFCor1KCN_R6wbYgafROCXhPvPkuFJ49VhKUwVfwkEJ-vfRUYQe4JXZCXW0UvwIx6yQu69pNLoQePp7RYRnAL-rL0UF9zK0N0NQEK9aUZdvMocO7_7PujpAZDTsicjpqEvfxRLSQPenQb05YHeojk5eMp1MlIxp3NeitSSigTJo4xQQUNdihFqTBsU0gVunwmPHxVduZnzJBdzB3yo7_cHt9hxCgV9P4B6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تصاویر دلخراش از اجساد مردم کشته‌شده در بیمارستان تهرانپارس تهران
⚠️
دو روز پیش ویدیوی دوم رو با تردید منتشر کرده بودم و نوشته بودم نمی‌دونم درسته یا نه. حالا عکس‌هایی از بیمارستان تهرانپارس با شرح جان‌باختگان ۱۸ و ۱۹ دی دریافت کردم که نشون میدن اون ویدیو…</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/75756" target="_blank">📅 20:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43dd15a53a.mp4?token=Vp6FUzXQPY2RackoU2A231DwK30YuN_CAzUamItAfIXdCRJWASRLugPXhpq-tUlvVQRBQpHRSVKykfw-p6gD5_WqzzCw4BMRhaiWBTDGo7diLlxC14CWezVzXeoOkmmd0-0Uwasn-aTDLVWKGX2EcP8phEFK5rdz_CFytOX6ndpKyYxBJQzXPb_kbe0jPTBRusM7GAS6QRLSpXEBOqnRP2VQ3bPvK8z-59CWvHaDpD8cpRwzkPGWYyDWgISQkKjllQCX_eYIj2hr8EidEKDRT9H8bp_NBMtwa7wtCCpokcYzFDqQ12lHDCaf9n-TqErFkyqj3obarWlViSPo-PsZ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43dd15a53a.mp4?token=Vp6FUzXQPY2RackoU2A231DwK30YuN_CAzUamItAfIXdCRJWASRLugPXhpq-tUlvVQRBQpHRSVKykfw-p6gD5_WqzzCw4BMRhaiWBTDGo7diLlxC14CWezVzXeoOkmmd0-0Uwasn-aTDLVWKGX2EcP8phEFK5rdz_CFytOX6ndpKyYxBJQzXPb_kbe0jPTBRusM7GAS6QRLSpXEBOqnRP2VQ3bPvK8z-59CWvHaDpD8cpRwzkPGWYyDWgISQkKjllQCX_eYIj2hr8EidEKDRT9H8bp_NBMtwa7wtCCpokcYzFDqQ12lHDCaf9n-TqErFkyqj3obarWlViSPo-PsZ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد‌ ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ششم خرداد، در نشست کابینه در کاخ سفید درباره مذاکرات با جمهوری اسلامی گفت تهران «بسیار مشتاق» توافق است، اما مذاکرات هنوز به نتیجه نهایی نرسیده است.
ترامپ گفت: ما از وضعیت فعلی راضی نیستیم ولی خواهیم شد.
رئیس‌جمهوری آمریکا همچنین جمهوری اسلامی را تحت فشار شدید توصیف کرد و گفت: «نیروی دریایی‌شان نابود شده، نیروی هوایی از بین رفته و همه‌چیزشان از دست رفته است.»
ترامپ افزود جمهوری اسلامی «در حالی مذاکره می‌کند که چیزی برایش باقی نمانده» و هشدار داد اگر توافق حاصل نشود، آمریکا ممکن است «برگردد و کار را تمام کند.»
ترامپ گفت: «آنها تازه دوباره به اینترنت برگشته‌اند، چون به‌شدت تحت فشار قرار گرفته‌اند.»
او همچنین گفت اقتصاد ایران «در حال سقوط آزاد» است و تهران به‌دلیل فشارهای سنگین، گزینه دیگری جز حرکت به‌سوی توافق ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75755" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خبرگزاری فارس به نقل از «منابع آگاه» گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، ممکن است در ساعات آینده به‌صورت یک‌طرفه اعلام کند که توافق میان ایران و آمریکا نهایی شده است؛ اقدامی که به گفته این منابع می‌تواند با هدف اعمال فشار سیاسی و اثرگذاری بر افکار عمومی انجام شود، پیش از آنکه اختلافات باقی‌مانده به‌طور کامل برطرف شود.
بر اساس این گزارش، این سناریو در حالی مطرح شده که هنوز برخی موضوعات میان دو طرف حل‌نشده باقی مانده و روند مذاکرات به مرحله نهایی نرسیده است.
در همین زمینه، یک عضو تیم مذاکره‌کننده ایرانی در گفتگو با فارس تاکید کرده است که تا زمانی که همه موارد مورد نظر ایران حل و فصل نشود، هیچ توافقی قابل اعلام نخواهد بود.
به گفته این منبع، جمهوری اسلامی ایران تنها در صورتی که اختلافات به‌طور کامل برطرف شود، نتیجه مذاکرات را به‌صورت رسمی اعلام خواهد کرد و هیچ توافقی پیش از رسیدن به جمع‌بندی نهایی، مورد تایید تهران نخواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75753" target="_blank">📅 19:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dEKU5uuaKvOgHxtV5m6ajgmfJKewi4osYijJK_pI7XtKjk1Z8NlWPyd9UYOHOFYB7uz2pfZTA8CqGvG3bl0PS-POUVBRzCmyml3QxA9FVOpduhgYTgfnsiP1gw2XoXRmY7wq9DCMaPTNhFggDwk6raES2R0AlsSS6zSPLnyhb9Hktc_rdEBlhQEl-xotaitBNs5T-IxcUDIuurBjvurILfeYk0NSLBnSpQIfrcqQiegZ8CurHYcK48WpSAlvJUwxH-_DzAbmseUrHP7Oo9Dv5ST4rQJDLTN3eK66vY7dGfswBAURal4oDHcXoQ7pr42A-LSsL6ZT17jqC9v8t44siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a77ea28679.mp4?token=gx2M0vnz9lY12AoP77XPCzToAzIC1orJsCSQxUAj7rGXtzns13RAd5G4aZi6EnLVeANF5Dsai64xUjnMCdn360QRLBO2UicMOk7CWKYz8dvuW2kdBYBH5KZbgQFzsMTYoYOyyP81BvUv3kBCnYyh4Y09zUAAL7b9nn41kC5N0Nx-peWnVaSaslcn1L6TSMraPQk5IYoTSWaNjGqSsvaydVtPyJWi0aZFkNocKQwbF9F_1H7haww-UdN2tykH_513m5HL59oPwSQdzpIUPULDocmUofXdOdHl2FK8_MmRzffk034vC53DhY3pjr-Dl7fswrNDYFHEsFk7w8RnMWFK8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a77ea28679.mp4?token=gx2M0vnz9lY12AoP77XPCzToAzIC1orJsCSQxUAj7rGXtzns13RAd5G4aZi6EnLVeANF5Dsai64xUjnMCdn360QRLBO2UicMOk7CWKYz8dvuW2kdBYBH5KZbgQFzsMTYoYOyyP81BvUv3kBCnYyh4Y09zUAAL7b9nn41kC5N0Nx-peWnVaSaslcn1L6TSMraPQk5IYoTSWaNjGqSsvaydVtPyJWi0aZFkNocKQwbF9F_1H7haww-UdN2tykH_513m5HL59oPwSQdzpIUPULDocmUofXdOdHl2FK8_MmRzffk034vC53DhY3pjr-Dl7fswrNDYFHEsFk7w8RnMWFK8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آتش‌سوزی
در یکی از برج‌های مجتمع مسکونی پامچال در چیتگر
#تهران
تصاویر دریافتی + منتشرشده، چهارشنبه ۶ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75749" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOLK2N98bdAaDqznqtcnayIgkJ9PD0-3ik0FNc0N3RHoWSt5itwxV6WJ_-Di3c4gSS7UwTfZ9P7h1VNH4dGZBXdtr7HYA_7zay3tfbYBerC7F6S_hAXs4k3pH3KLZg6H08Zis8HaQNTOPZHE2309oRwDpMQmAL-nZv2VN_YF4GPvbrOHUxXzcu1AZYcU4G6pGn1k5Am-vmFqSqGfEDHmzvom7h1bRF7DjzskU_KYeeQhqaSuYSQHHPTrAyGU2AXi49qtVtXIcBxPOgoZUY6S7TpVoAPldj45zi6yGDXSqt_y8MCvl31z4o-g32UXiAUD9VT8ddrYlUZdlCNludJwYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید روز چهارشنبه اعلام کرد گزارشی که از سوی صداوسیمای جمهوری اسلامی منتشر شده و به پیش‌نویس یک چارچوب اولیه و غیررسمی برای تفاهم‌نامه میان ایران و ایالات متحده اشاره داشت، «صحیح نیست» و تفاهم‌نامه مورد اشاره «کاملاً ساختگی» است.
تلویزیون حکومتی ایران ساعتی قبل گزارش داده بود که پیش‌نویس یک توافق چارچوبی با ایالات متحده شامل تعهد به لغو محاصره دریایی ایران، بازگرداندن رفت‌وآمد در تنگه هرمز و خروج نیروهای آمریکایی از منطقه خلیج فارس است.
کاخ سفید در بیانیه‌ای اعلام کرد: «این گزارش رسانه‌های تحت کنترل ایران حقیقت ندارد و تفاهم‌نامه‌ای که آنها منتشر کرده‌اند کاملاً ساختگی است. هیچ‌کس نباید آنچه رسانه‌های دولتی ایران منتشر می‌کنند را باور کند. واقعیت‌ها اهمیت دارند.»
گزارش صداوسیما
مدعی شده بود که آمریکا متعهد به رفع محاصره دریایی ایران شده و در مقابل، ایران تعهد داده تعداد کشتی‌های عبوری تجاری را طی یک ماه به سطح پیش از تنش‌ها بازگرداند.
تلویزیون جمهوری اسلامی همچنین گفته بود بر اساس این پیش‌نویس، «مدیریت و مسیر عبور و مرور» کشتی‌ها با ایران و همکاری عمان انجام خواهد شد و آمریکا تعهد داده نیروهای نظامی این کشور از «محیط پیرامونی ایران خارج شوند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75748" target="_blank">📅 18:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ec2q_uz46ougN55C7TH2AmHn6iFWvFB9tk3FgNIz7yn2QRR0ZYn0bSzqOtVu-b8GKETJxGu0b3otS3sXCKWA4pw7RxV3_gLjjv4-jFxhMNjn2HeHo6AId6Hc64y2XC4xcfXYieIFMMK0_n0FhTt5Ia5AsbRIZo1tcrA_ijGerhPmeEPRSCpZb0mqhUEcimPL5tIYKzhz-Svuscya1yWiANbvziq5Cbbx3IDYqmlnDbojhq3hx_l3FGX6FFHV6LLTQ8gCxLOY-1UMCR-mwdaNzmnqxRxuwrjhVtlXbP9-X0gqjHB--VtVhh1AyrjccKiqj99jT64xVtFwEiSBn785cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد‌ ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ششم خرداد در شبکه اجتماعی تروث سوشال با انتشار تصویری ساخته‌شده با هوش مصنوعی، از شبکه سی‌ان‌ان انتقاد کرد و نوشت این رسانه نیروی دریایی جمهوری اسلامی را قدرتمند نشان می‌دهد، در حالی که شناورهای ایران در اقیانوس غرق شده‌اند.
در این تصویر، جمله «سی‌ان‌ان: نیروی دریایی ایران قدرتمند است» در کنار تصویری از شناورهای غرق‌شده جمهوری اسلامی در کف اقیانوس دیده می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75747" target="_blank">📅 18:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rdG5ed569aoBTI-i00qNXgSMc3QXt7Bs5_QqJPatdkZhfsKrU8T4mstjU3bHA9wtbEv1wbUROTe87TQ2-Lcdxjlp8C66uGk_9MrlwHnWMC417Eze8ZgxzoiSmi9eFMNolFbpU6GFMOi2GVZ11BA9zS-iHeyIpgIXCSzZpDN6xUHvAv5oOOfJhefm0tOWmYIDly7J3GsBecV1tLQ8WVkLfTcvcJFZuZCrkG9XIGIijKW44N2LioVW0k2bygk-iAGv_XSwC971CooxWy2E6yRuBP-76o2SPTRCtOkoRP-k1sg7YRnxRCEJAfuAE3oRv-cO__rWmtsPU7D9uzIzijFwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏گروهی از کاربران در شبکه اجتماعی ایکس (توییتر سابق) پست‌های انتقادی گزارش‌گونه از تحولات و رویدادهای سیاسی خارج از ایران منتشر می‌کنند، خطاب به شهروندانی که پس از حدود سه ماه به‌طور تدریجی با فیلترشکن موفق می‌‌شوند به اینترنت وصل شوند.
‏این پست‌ها که با عبارت‌هایی مانند «
وقتی شما نبودید
» یا «بچه‌های ایران که تازه وصل شده‌اید» آغاز می‌شود، همزمان با کاهش تدریجی اختلال در دسترسی به اینترنت، به محلی برای مستندسازی و بازاندیشی انتقادی نسبت به تحولات سیاسی‌ ۸۸ روز گذشته تبدیل شده است.
@
VahidHeadline
دوستانی که تازه وصل شدن یدونه «
سلام وحید جان
» سرچ کنید آرشیو کامل از اندر احوالات ایرانی جماعت در زمان قطعی نت رو براتون میاره
iamroyaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75746" target="_blank">📅 18:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d05e2caab7.mp4?token=XCG5ie9xciFKwnsXyUU9tBbpAtdkc7QG7uj2U0GQzFvdPGEeBwDrahu-hXBnFv-Lrs8Yhappm68PuSxG47tFj6aGBHyqnov6LBUDEcxs7cNfQ0HJQk0iR87T1jx27Bi4T79R0eKTWcP2zk-fmrMTScA6GGlsvP-kenAqVAhg7fH5W8E5Wex31EQeVPew7hZV4XXXquAjQ9IKTn7j7zN_m8E0db9hzXXe8DJW9kigVDqB59GV5oD-ugmx_29s2x7UoPwBqtTRXyaP3gtc5d5hjD36fI8IL8q0DlJy1irOFM5vumNR9AMj_wiM9fcM_2fGMkRj63L-zm-b6B0ixhOSZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d05e2caab7.mp4?token=XCG5ie9xciFKwnsXyUU9tBbpAtdkc7QG7uj2U0GQzFvdPGEeBwDrahu-hXBnFv-Lrs8Yhappm68PuSxG47tFj6aGBHyqnov6LBUDEcxs7cNfQ0HJQk0iR87T1jx27Bi4T79R0eKTWcP2zk-fmrMTScA6GGlsvP-kenAqVAhg7fH5W8E5Wex31EQeVPew7hZV4XXXquAjQ9IKTn7j7zN_m8E0db9hzXXe8DJW9kigVDqB59GV5oD-ugmx_29s2x7UoPwBqtTRXyaP3gtc5d5hjD36fI8IL8q0DlJy1irOFM5vumNR9AMj_wiM9fcM_2fGMkRj63L-zm-b6B0ixhOSZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری صداوسیما اعلام کرد به یک سند غیررسمی اولیه از چارچوب ۱۴ بندی تفاهم احتمالی میان ایران و آمریکا دسترسی پیدا کرده، سندی که به گفته رسانه‌های ایرانی، هنوز نهایی نشده اما حاوی جزئیاتی درباره وضعیت تنگه هرمز و حضور نظامی آمریکا در منطقه است.
بر اساس این گزارش، در پیش‌نویس منتشرشده آمده است که آمریکا متعهد می‌شود نیروهای نظامی خود را از اطراف ایران خارج کرده و محاصره دریایی را متوقف کند. در مقابل، تهران نیز تعهد می‌دهد ظرف مدت یک ماه، عبور کشتی‌های تجاری از تنگه هرمز را به سطح پیش از جنگ بازگرداند.
طبق مفاد این سند، کشتی‌های نظامی مشمول توافق نخواهند بود و مدیریت مسیر حرکت کشتی‌های تجاری در تنگه هرمز با همکاری ایران و سلطنت عمان انجام می‌شود.
صداوسیما همچنین گزارش داد که هنوز چارچوب نهایی تفاهم تدوین نشده و ایران تاکید کرده بدون وجود «سازوکار راستی‌آزمایی» یا همان مکانیزم اطمینان، هیچ اقدام عملی انجام نخواهد داد.
در بخش دیگری از این گزارش آمده است که اگر دو طرف طی ۶۰ روز آینده به توافق نهایی برسند، این تفاهم می‌تواند در قالب یک قطعنامه الزام‌آور در شورای امنیت سازمان ملل تصویب شود.
@
VahidOOnLine
🔄
آپدیت:
کاخ سفید: گزارش رسانه‌های جمهوری اسلامی درباره تفاهم‌نامه تهران و واشینگتن کاملا ساختگی است
کاخ سفید گزارش رسانه‌های جمهوری اسلامی درباره بندهای تفاهم‌نامه احتمالی را «کاملا ساختگی» خواند و گفت نباید به روایت رسانه‌های جمهوری اسلامی اعتماد کرد
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75745" target="_blank">📅 17:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZCKNdTPz7RVbMcWpmZe4hPGG83a6VLgzuIvXPlm5aFwh0bmZqB6mDEPR07Ju409twVg0jea0TssWjoWH9N1IzGWLPghFmB_gljELV_Q9g_0H-dcDpbh3rA9wZ_CIkqVWaQ7zhOemRowlqy6ntYEtknLCoISCj378HHFbhynF6RZ7G9YV7sDkit1fQHz-eash5P8ik0VzpWxYS1NM2OfKJRbcv2dwzuESJuPe3FKQ8ikzeY5MEkxSxDWpKBpsHuNCEDoEGdsiHrQ0aAJI54OF6PbC6nPiUXlS13pE5tN5OpJTsLyYbNC380KN0BArIUjrG7h2bX99yh29E8_W2Yadw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در تروث‌سوشال گزارشی از جروزالم‌پست را بازنشر کرد که بر اساس اطلاعات اختصاصی «مدیا لاین» نوشته است موارد آزار و تعرض جنسی به زنان بازداشت‌شده، به‌ویژه زنان جوان، در زندان‌ها و بازداشتگاه‌های جمهوری اسلامی در دوران آتش‌بس افزایش یافته است.
در این گزارش، زنی جوان به نام کاملیا گفته پس از بازداشت خشونت‌آمیز در خانه‌اش، دو هفته همراه هشت زن دیگر، از جمله دختری ۱۶ ساله که با ساچمه از ناحیه صورت زخمی شده بود، در اتاقی ۲۰ متری نگهداری شد.
به گفته کاملیا، او پس از انتقال به سلول انفرادی و خودداری از اعتراف اجباری، در اتاق بازجویی هدف خشونت قرار گرفت، لباس‌هایش پاره شد، با باتوم مورد تجاوز قرار گرفت، به‌شدت کتک خورد و به تجاوز گروهی تهدید شد.
جروزالم‌پست همچنین با اشاره به قطع گسترده اینترنت، بازداشت‌ها، ناپدیدسازی قهری، آدم‌ربایی، تهدید روزنامه‌نگاران و مخالفان در خارج از کشور و افزایش ناگهانی اعدام مخالفان نوشت سرکوب در ایران تشدید شده است.
دونالد ترامپ پیش‌تر نیز با انتشار پستی در تروث سوشال خواستار آزادی هشت زندانی سیاسی زن در ایران شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75744" target="_blank">📅 17:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75742">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z8AFbETIjkS-pDBL-Gq_UPf-7zYerh1T9Iq9sPFnZmRXPgJd9kV9i_ae-mKlc1LHVgBZ2CSXovcy2YlV2ImMiibhdRlqDu8PzXbg9BJgRKzEdnUVv6yULoM1l4DuZTKHwkUH-h7fx263gfBCxIblSILt0xfm6B88PsNwKeF34x3z2TM9Pgln1WpyUQbHKt7AAhuzD3bbtCksg47wDONWLpx5-zz_6ITVqEANDMXzISuJuUQ_GWmaAx1VcuSqPOmAHPypfnOeSyMJTkyeghlhOAW4Bd1MUmnc3rzAGbyNDWtiEKwp2Vbom3JjI6GAu_8L6mAnBzsslNNPoogTkwjQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EZFcSouK5M0Q_y5GhLw2tIwi01Sa6V8jiwTOTdCrLmtDaWAtWMy8tltxCMK1wd71lQUiwtg9kX0vExoduQFJ8K8AAi6owNLMWuJfIjuDcVihGv55LvyQECxq3SBn0a4XXJyIfwHAAivh9JJh-35jvHaEJ1YT_c0aKMZTGfglvg_zd8t_irKSCVJOvjHg1A4x62He63ttnQ5Kds3o96Edp33ovCzDO0H7rVukscpm_Y9gtQ3NS0I4N9Kd_IoYXv24j_8eoxYhBJOCiatdXngeQByqmp8DVoAzLyZY9KyMUM1ku8gaLnRUrCSsQs3RkfudxzzwqwMRxbQOws-N_lSNlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز چهارشنبه ششم خرداد هشدار داد که بعد از جنگ اخیر، «برخی کمبودها و گرانی‌ها» در پی فشارهای اقتصادی آمریکا می‌تواند باعث بروز ناآرامی‌های تازه در ایران شود.
این وزارتخانه در بیانیه‌ای مدعی شد که «تشدید فشارهای اقتصادی و متعاقب آن، انجام تحریکات گوناگون اجتماعی توسط عوامل دشمن و رسانه‌های مزدور فارسی‌زبان بیگانه، با سوء استفاده از برخی کمبودها و گرانی‌ها» یکی از محورهای مورد توجه آمریکا و اسرائیل است.
هشدار درباره احتمال ناآرامی همزمان با افزایش شدید نرخ تورم و و گرانی کالاها و همچنین انتشار گزارش‌هایی درباره کاهش شدید درآمدهای دولت جمهوری اسلامی در پی هفته‌ها محاصره دریایی آمریکا و سقوط شدید صادرات نفت ایران مطرح شده است.
این در حالی است که اعتراضات دی‌ماه سال گذشته نیز بعد از افزایش مداوم نرخ ارز در بازار و مناطق تجاری ایران آغاز و بعد از چند روز با افزایش تعداد معترضان، با خشونت شدید نیروهای امنیتی و کشتار هزاران نفر مواجه شد.
وزارت اطلاعات همچنین درباره «عملیات تروریستی و تجاوزات مرزی بویژه در شمال غرب و جنوب شرق ایران» و انواع عملیات «ترور و خرابکاری» هشدار داده و مدعی شده که آمریکا و اسرائیل به دنبال وارد کردن «انواع سلاح، مهمات و ابزار ارتباطی غیرقانونی، بویژه استارلینک» به ایران هستند.
ابراز نگرانی از رواج اینترنت ماهواره‌ای استارلینک در حالی است که بعد از ۸۸ روز قطع سراسری اینترنت در ایران، از روز سه‌شنبه شهروندان توانسته‌اند به شکل تدریجی و محدود به برخی سرویس‌های اینترنت جهانی دسترسی پیدا کنند.
@
VahidHeadline
این بیانیه که با عنوان «سخنی با ولی‌نعمتان و هشداری به دشمنان» در رسانه‌های داخلی ایران منتشر شده، ادعا می‌کند که «دشمن شکست خورده در جنگ نظامی، بدنبال تولید دستآورد برای خویش، گرچه از طریق جنگ نرم، می‌باشد.»
این بیانیه در حالی صادر می‌شود که اسماعیل خطیب، وزیر اطلاعات جمهوری اسلامی در سومین هفته جنگ در حمله اسرائیل کشته شد و دولت هنوز جانشینی برای او معرفی نکرده است.
وزارت اطلاعات در این بیانیه علاوه بر اسرائیل و آمریکا، بریتانیا و اروپا را به همراهی با این دو قدرت متهم و کشورهای عرب حاشیه خلیج فارس را به‌عنوان «غلامان متمول» مسئول تامین مالی «جنگ ترکیبی تمام عیار» علیه «مردم قهرمان ایران» معرفی کرده است.
وزارت اطلاعات در این بیانیه معترضان و مخالفان جمهوری اسلامی در خارج از ایران را تهدید کرد و نوشت: «مزدوران ضد انقلاب و تروریست‌های مقیم خارج کشور و حامیان آن‌ها نیز از آتشی که می‌افروزند در امان نخواهند بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75742" target="_blank">📅 17:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75741">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U3osAs3_nstZfVSlNBqN1M5XrOIh1uuwuRpQxIo5Fy2_Yt6PkksKfzsGzue3iKYFNyUtI1eEMRUNaJsYeWlBf9x4cpRHVGt855rVGYDM3pYp43LyjvV0Xh7eVVOcrZ1aKnkTlWKU1xR3qEEliUReIqbhz5Se4ZPMRnTtIsgrtkh06SSXntF1JgGxgljD4E9uJEDVI_itSlsZsrMuzzPHLF8UYgUJrBbtbqfJK50nd1a3xry4vNkjgHASlMx7mA-dlms6I3vDSfBbgyrdUP3ICRBh-fIBiW6WEX-49uK5w7SSEYy6m2zgJW6MN_lRVDYH7-24Xi4JbYnQ9Yp62PgOww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز به نقل از دو مقام آمریکایی در روز سه‌شنبه ۵ خرداد گزارش داد که حملات دوشنبه شب نظامی ایالات متحده به اهدافی در جنوب ایران پس از آن صورت گرفت که تحلیلگران اطلاعاتی، مجموعه‌ای از اقدامات نظامی بالقوه تهدیدآمیز جمهوری اسلامی را در ۲۴ ساعت منتهی به این حملات شناسایی کردند.
هواپیماهای جنگی آمریکا دو قایق تندرو سپاه پاسداران انقلاب اسلامی را که سعی در مین‌گذاری در تنگه هرمز داشتند، غرق کردند.
این مقامات که نخواستند نامشان فاش شود، همچنین گفتند که جمهوری اسلامی پهپادهای تهاجمی یک‌طرفه را به سمت حدود دوازده کشتی جنگی نیروی دریایی ایالات متحده که در خلیج عمان و دریای عرب یا اطراف آن هستند شلیک کرد. این کشتی‌ها در حال اعمال محاصره دریایی آمریکا علیه جمهوری اسلامی هستند.
طبق این گزارش تحلیلگران نظامی آمریکا همچنین فعالیت‌هایی را در برخی از سایت‌های موشکی زمین به هوای جمهوری اسلامی در نزدیکی تنگه هرمز شناسایی کردند؛ فعالیت‌هایی که امنیت هواپیماهای جنگی آمریکایی مستقر بر روی زمین و آن‌هایی که روی ناو هواپیمابر آمریکا در منطقه به عنوان بخشی از نیروی اعمال‌کننده محاصره دریایی حضور دارند، تهدید می‌کرد.
تیم هاوکینز، سخنگوی فرماندهی مرکزی ایالات متحده، روز دوشنبه در بیانیه‌ای گفت که ایالات متحده «برای محافظت از نیروهای خود در برابر تهدیدات نیروهای» جمهوری اسلامی حملاتی را به اهدافی در جنوب ایران انجام داد.
سایر مقامات پنتاگون گزارش‌های رسانه‌های داخلی در ایران را که در روز سه‌شنبه مدعی شدند یک پهپاد آمریکایی «ام-کیو۹ ریپر» توسط جمهوری اسلامی سرنگون شد، رد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/75741" target="_blank">📅 04:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75740">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P4sTAq2lmUUs5bgNh4_-Mt10fDsfMnJB-j653T4IEs4rozbBOiT4og3bTftrtQ1PeFZD8wK1C_KUmyiIC6w2WnqD6RD2J4yjAg5UVIkfXcP77TMskCpRX3RjWeI8uxIhiyS-i-eQlHarT-PZWXX0fbcdg5x59ZNl4Ptj2CYhStTCOG7sy8veWq_245m0yP1fe-FhJi6r-QBimPJiN9VVEUBnhm_x83Pml2hPo3a0y8d9SYUOH-WvianEFWPRxoc7OiAJYHLhVotV-TI7E0zQvUHIRCfwEzCoXg0eK2qJxyXDXS-jMdy6_N8ETU-6mLvJL13miJkvGxg2nzFcokRRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
با توجه به احتمال نامساعد بودن شرایط جوی در روز آینده، جلسه کابینه را در کاخ سفید برگزار خواهیم کرد و سفر کابینه به کمپ دیوید را به تعویق می‌اندازیم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/75740" target="_blank">📅 00:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75739">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m8CaWTaD3IpJ5frK9QtFmvzPdCQyu0KelBA43YB1nV4qakXkVZ7kfPbAujtZzX803qzsRjMSHhlSSm1dvYvhzCf1ozDP7yILut24zABJ10vzQSW-6n4ZCOX2hlF4R2Ti49u-9OsSD6RyKXcI2mBwKXqDRjBBNA2ADBNN_IfK2O1OOl1yT9QK1hsXtsc7c82uZMlC2_h-7GJOAYqmGjqiFcaXT5m1jD_ax7hOxf6pm9DPGFObFWhthutEhT-1Ryy7iGvavBldPgHXOiC7QtbaWor5e9Xbtfq9Vi4t6xNPBbDAUOW2yUObrNBX8e_hMxwlG4nsJ1B9IrhMGNA3hrN7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ متنی که
۸ روز پیش
منتشر کرده بود رو دوباره پست کرد.
ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در کف دریا آرمیده، و نیروی هوایی‌اش دیگر در میان ما نیست؛ و اگر کل ارتشش از تهران بیرون بیاید، سلاح‌ها را زمین بگذارد و دست‌ها را بالا ببرد، در حالی که هر کدام فریاد می‌زنند «تسلیمم، تسلیمم» و با هیجان پرچم سفیدِ نمادین را تکان می‌دهند؛ و اگر تمام رهبران باقی‌مانده‌اش همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمز شکست‌خورده، چاینا استریت ژورنال، همان وال‌استریت ژورنال، سی‌ان‌ان فاسد و حالا بی‌اهمیت، و همه دیگر اعضای رسانه‌های جعلی، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورد و اصلاً هم رقابت نزدیک نبود.
دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها به‌کلی دیوانه شده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/75739" target="_blank">📅 23:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75738">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH5yMxJ8Vs1LokC2CJZqEd2LWV0dyaEkvYITm-HUfVGtyrEtNJVZT0UklvzBy4DR7dYKz4wPwXs4ZkwJcc2MogrtiT6x2p82ZMoLgPWqM3MTVImG-H1jes95SegQQCNJMhQORdHCl08lusz-xJ6mmD8yjGyM0pS12qrqFsvonIDZQty7coe0EY5ceGB-Q6Z6b-QWHVFw1WZuh3FAJkmV8GethHS1Bq0BVOzeUxSeVsxb_vLIrQcvrdc3s4h4chhzUdjPOKhL-Otcjje8uejC1c6jWZlxbu6BoCZegr8372Hg2vIDLKEncuUB3SA_in8U5w24-J9ZdN-oF34v-kyEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، قرار است روز چهارشنبه نشستی کم‌سابقه با اعضای کابینه خود در اقامتگاه ریاست‌جمهوری کمپ دیوید برگزار کند؛ نشستی که به گفته یک مقام کاخ سفید، همزمان با نزدیک شدن مذاکرات مربوط به ایران به مرحله‌ای حساس برگزار می‌شود.
خبرگزاری فرانسه با انتشار این خبر نوشت که انتخاب کمپ دیوید، اقامتگاهی دورافتاده در کوهستان‌های مریلند که ترامپ برخلاف بسیاری از رؤسای‌جمهور پیشین کمتر به آن رفت‌وآمد داشته، نشان‌دهنده حساسیت گفت‌وگوهای پیش رو ارزیابی شده است.
روزنامه نیویورک‌پست گزارش داده که موضوع ایران محور اصلی این نشست خواهد بود و همه اعضای کابینه  [
از جمله
تولسی گابارد، مدیر مستعفی اطلاعات ملی] در آن حضور خواهند داشت. بر اساس این گزارش، مسائل اقتصادی نیز در دستور کار قرار دارد.
کمپ دیوید در گذشته صحنه چند تحول مهم دیپلماتیک به رهبری آمریکا بوده، از جمله توافق‌های سال ۱۹۷۸ میان اسرائیل و مصر در دوره جیمی کارتر و نشست ناکام اسرائیلی‌ـفلسطینی در سال ۲۰۰۰ در دوره بیل کلینتون.
این دومین سفر ترامپ به کمپ دیوید در دوره دوم ریاست‌جمهوری او خواهد بود؛ نخستین بار چند روز پیش از حملات آمریکا به برنامه هسته‌ای ایران در خرداد ۱۴۰۴ بود.
@
VahidHeadline
🔄
آپدیت:
محل جلسه فردا عوض شد به کاخ سفید
چند پست پایین‌تر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/75738" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75737">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ejgNWtafqXwu4uNdU9685qq_lKl4Z_K4GCwUnnmOMuPigBk2np7sOMoncCa7Fpv0qgQeLuyWuWa6b61HltAWt-JzJUUcq5GQd8gPU_mJUaOzSFuZGEgFoVg-tBaN8kyYHStgHwlIRVLxrEc7xqW7SgGeC7EWqkkzrcJfDcS-O23_EdCFLahE6ydGM_7N0LLEBYiFGV1syVWyl5tkry0USISuGDyUGE-iPO4EeT88UOKFWsDV_54IFkLPtswX4duqRagqF2ink_VqK8KD4-55vlyB8oS_mDUQyY7f6WaEvC2jf5rtXufvzaUxjhrmda0wA8S0y_gs8HZPgYfhwZsJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش فارس، خبرگزاری وابسته به سپاه، محمدباقر قالیباف، رئیس هیات مذاکره‌کننده جمهوری اسلامی ایران که روز دوشنبه در راس هیاتی با همراهی عباس عراقچی، وزیر امور خارجه و عبدالناصر همتی، رئیس بانک مرکزی، برای رایزنی با مقامات قطری به دوحه سفر کرده بود، عصر سه‌شنبه، پنجم خردادماه، به ایران بازگشت. بر اساس این گزارش، محور اصلی گفتگوهای میان مقامات عالی تهران و دوحه در این سفر، رایزنی درباره بازگشت پول‌های مسدودشده ایران بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/75737" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75736">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPAs9k6Rq-f7viiyde9v1WfQPmBlPDPa_6n_hiPQ8ZNEZpVDGKzwlJFPA61SfVGgwGg-gFK6br5L5HD609GnpVk0RHKKe7QkU2odmRIPqfUeMEijY3h1ZXEf2rRSgdG9ZVa0QanPb__NHPwq1dBI4nIw3IxhXrXrqqk6vgSDk6t0tpSeqjK9-knoboExNgtl15_uTE2_iiYXciIWWNkoHa9CkyoWtRBFfxwrb8Q60N9Aq0xdF4PDJbdQjV75sJ3tHM0SZxeSYrBDXYGp3uQHMpGcrA0soXZUWYUjv0zCVpsNbE8QR9Lxg0_LuMLad5lLWpaUI2SHz1qQs804VH7UNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز سه‌شنبه، به نقل از منابع خود مدعی شد که طبق متن ۱۴ ماده‌ای یادداشت تفاهم بین ایران و آمریکا، منابع بلوکه‌شده ایران، به میزان ۲۴ میلیارد دلار باید در طول مذاکرات آزاد شود.
آنطور که این رسانه نزدیک به سپاه پاسداران از قول « یک منبع آگاه نزدیک به تیم مذاکره‌کننده» گزارش داده، ایران تأکید دارد که نصف این مبلغ باید با شروع مذاکرات، در دسترس قرار گیرد، و بقیه در طول ۶۰ روز منتقل شود.
این گزارش می‌گوید که سفر اخیر عباس عراقچی و محمدباقر قالیباف به قطر هم برای تفاهم دربارهٔ اجرایی‌سازی این مطالبه، و نحوه دسترسی به ۱۲ میلیارد دلار در گام اول و رفع موانع بوده است.
همزمان، احمد بخشایش اردستانی، عضو کمیسیون امنیت ملی مجلس، مدعی شد که چند روز پیش، قرار بود ۱۲ میلیارد دلار از منابع مسدودشده ایران، از طریق روسیه وارد شود، ولی آمریکایی‌ها مانع این انتقال شدند.
هنوز هیچ مقام رسمی در دولت آمریکا، این ادعاها را تأیید نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75736" target="_blank">📅 18:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75732">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ntZmzXIvH-tH14hEW0oq0aGi1Wo8ph4fIG-vV1dMAAWuUgaSYXwZTH9oh3hG2U3owcFpixNzh_JcxHdD4xqxUONne-taQ7Rhk1wzDYaiIr5bSIE9v9AFP0Zjp1zzlwhA35L5iLcIQxZU8hElc77uTBZ6BYSmNHFlIZ0qC2UUfgKQnJRFfz7r6zh82k7j4py-5tYRKVouC8yPEYh2hPZmC0BVoxYqektrWzW7QKoOtteNEN9iJw7UoL7D1OpEUOUR5Pt6SPDOilDq8QSwA82rltuUrMLtdYzOnnS0fOjlNZUtCohhPemQtBK6mjc7TQaFB7e5Tzl2eBfoOT-E-_TMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hqid_Nz6gVXhxPHthtKrOMr9Ye4jB_GNmYKmzW7mmBxPWzhQeJ83YkqQlNevB3-2YH1IJKg11B56yGZSHKpRiISk3lbhiB8rUsQTWlFzyuWicbtM2k-sOQDijwUgDl0y8OhnZBEZoWwARCVwewAC_AafxPJ8k2WDpHQAxqva91UW8gu9SqwUPp4A7pdk4EPOFeVl6wDQfHuWD5q1R2t8eIxwlA40y73UFeNVoDqHE9YaQPVdgLmlyV7T6ZewkHsHCPJ17KGnlyMqX3hzxulMjeFlxhyJEYxWTy58ICzGKxTimASqWtcAgmCpFE-f3Nsl8WCqr5K38QkjPNBsWP1KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eBWcWS-QY7v2ed6QxFVmZqUXmmBM2MhoJZHpKw0qBXJcsnSOvyE1-qEnZh4LKj7A7eL9N4Zk93_5yBFqxXLz1qtkix_5cqF-NVreHpV0Gq5TwiCUQWffqDy2hWoVAkY2Zdf_G8QLC6K9FmWE00rhTzzWd_5yx5scvorTdUiJ9XWKLB2Pd1cCb28n4nzed2N9moIucrVfZ51ogpJfqn-u7heYRYd1IF7pT3Jo3_oJ0diMG9P1WgF4qJJ9yeaEi93YIT8QplNdETep59CL3MnE-kzlCuZOslaFR3-gnUAXyNJCTtmImwiiMK8bYqxD8x6euQpOegyFq7SubpJUydIYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LDpnQkBOwEOMKZV6XHmLjcHIWDZdygiCO2Knn77ZqJHA2sNU0xhEJcO0Nhwy2OsHDDSWbTLESsArB7J0pK4PYQhcJ7CASmGaujjGtn4fdYi2_S6vsWeqOTsf789p0XOjyrVilMDh7oXOXeVtCM-wn7TgNAZPHGS8fT8_qc0kCx86vZU7ymZnJJtvrGokPTrCBj_i9b3rH8co7j0f-JuIrruSW4E8J56Z3gTHeonqpLyzszGSKNp__WxlwkmSlbI0eS338C32AC3ttWkFDoSeG4G9PghsgZDSPjB1LrriHzVCu1rZxj4e136bKmwFblS0jZcEQZGwqIEBJCde4ihY8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نت‌بلاکس، نهاد پایش وضعیت اینترنت در جهان، اعلام کرد داده‌های زنده این مجموعه نشان می‌دهد اتصال اینترنت در ایران در هشتاد و هشتمین روز قطعی گسترده، به صورت نسبی در حال بازگشت است؛ هرچند هنوز مشخص نیست این وضعیت پایدار خواهد ماند یا نه.
@
VahidHeadline
ساعاتی پیش از این واقعه اخبار دیگری منتشر شده بود:
در حالی که مقام‌های دولت مسعود پزشکیان از آغاز روند اتصال کامل به اینترنت تا ۲۴ ساعت آینده خبر می‌دادند، دیوان عدالت اداری اعلام کرد دستور توقف اجرای مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» را صادر کرده است.
این دیوان ظهر سه‌شنبه پنجم خرداد اعلام کرد «به‌دنبال طرح شکایاتی، دستور به توقف مصوبهٔ ایجاد «ستاد ویژهٔ ساماندهی و راهبری فضای مجازی کشور» داده است» و افزود: «تا زمان رسیدگی نهایی به شکایات مطروحه، مصوبات و تصمیمات این ستاد قابل ترتیب اثر نخواهد بود.»
مرکز رسانه قوه قضاییه نیز اعلام کرد دستورات و مصوبات ستاد ویژه «به دلیل بررسی غیرقانونی بودن ساختار ستاد، تا زمان رسیدگی قانونی قابل اجرا نیست».
@
VahidHeadline
بعدش:
همزمان با اعلام دیوان عدالت اداری مبنی بر صدور دستور توقف بازگشت اینترنت، ایسنا به نقل از «یک منبع مطلع»، روز سه‌شنبه، پنجم خردادماه، گزارش داد که با صدور دستور اتصال اینترنت از وزیر ارتباطات و فناوری اطلاعات فرآیند اتصال در حال انجام است و طی ۲۴ ساعت این امکان برای همه فراهم خواهد شد.
این درحالی اتفاق افتاد که تنها یک روز پس از مصوبه «ستاد ویژه ساماندهی فضای مجازی» برای «بازگشت اینترنت به وضعیت پیش از دی‌ماه ۱۴۰۴»، دیوان عدالت اداری با صدور دستور موقت، «اجرای مصوبه ایجاد ستاد ویژه ساماندهی فضای مجاری» را متوقف و مصوبات این ستاد را تا زمان رسیدگی نهایی، غیرقابل اجرا اعلام کرد.
همزمان، انتخاب نوشت که کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری تحت راهبری یک مقام ابقا شده دولت ابراهیم رئیسی، «شاکی قضایی» اتصال اینترنت بین‌الملل هستند.
ایران از زمان آغاز جنگ در نهم اسفند، به مدت ۸۸ روز، در خاموشی دیجیتال به سر می‌برد.
@
VahidOOnLine
محمدرضا عارف، معاون اول پزشکیان، در شبکه ایکس نوشت پیرو دستور پزشکیان «گام نخست دسترسی آزاد و ضابطه‌مند به فضای مجازی برداشته شد.»
او افزود: «با بازگشایی اینترنت، خدمات هوشمند هموار و مطالبات مردمی که این‌چنین پای کار نظام و ایران ایستادند محقق و موانع توسعه دانش‌بنیان و مرجعیت علمی برداشته می‌شود.»
عارف در متن خود درباره «گام نخست» و وصل شدن اینترنت برای شهروندان توضیحی ارائه نداد.
این در حالی است که پیش‌تر فارس، رسانه وابسته به سپاه نوشت دیوان عدالت اداری اعلام کرد که در پی طرح شکایاتی درباره ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»، هیات تخصصی صنایع و بازرگانی این دیوان، با احراز ضرورت و فوریت موضوع، دستور توقف اجرای این مصوبه را تا زمان رسیدگی به شکایت صادر کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75732" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ace_ba3o_sWzkmkJfn7-23FzC8DTCroNaKK1hmyOAxpT5YZ1Y_TcRY8URDIgo9a1yosRxXaG63WaJcbOUTE2UAdNngbfIACzJfQB7R9pY4XA-PKeR5KQpdj2WwExx7ayxj-LGr1gxpYiwKRn4l8TmFoPa_1FEiUZHVdDsehjM_eMoGMAJvGVQ_nHg6A7Awku6qCwBnBYcNNuxwZtVNcjbR_xosyl5ccHR-8HdA2tWc7ML_0QAIrqCVcGlal5teoJlb9Xi3IQl3dAyjOfw-Mop-hXhwRAVWwLKCpEEAjNdVo3kK8AVFG0gygbh4w7JQbSiTQZ6mQ0Qj75_xgIttboGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75731" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d0TmYEPqsHWtx8_hgTeo5fUd_ZdUU40dQs7ViWYI8TV10K-90_ZpvBn7N0v2DurC216Aau-LScQjdbqFklLFZJ0FgmDU8CEnwP5OteYzsRi7JgYdUIHFhfuwqWEVK2YjVeWMNbXIiHBt2tPxINuOxxGuCeicXt5u3VqJCmDw21G7798O_U2Q3R3UoxsC_lcmZ5tAC-HFCBXUDb8ViwfHSfn_6EqSDHrp2M0AvKXKGo6KqqKD2QRKBp2J0z52AwdPvYttpZCdvwuEN-JCojN0dPzNM2JtQE7R8MS9WJ32bIW3Y1dAbuGjZR2A_Fxl5xtvWbSy7zOKiIadnxOFBklVhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e24y2cxmdQRXxyfsvJUkWp2VwX02CK0T_l_LCHI9-XTzZwFdQoQ8cw605q1QA29HGFET_qmhnJ9eS0mCPUWQR3CCyRmGqXeTbjMbMuBZLci5YMJ_PAZWS2fLG7L7eJxRnUXWF--Ixmkl816wh4aa7TLPRqVoz9BF6RPV3WO1VASRlNDVQiZIuLph9I0MGe5MhYw5KRatU-oHzt5dvD2vK8-2z73daVWZgpWMYshRwpuI1x-llqLu80vpBUG6RwaT6EUxBFY6j8f8rluZC-OEnxBfoPyAP0VHbMY-LsERd0dr6i2nKenD3MGLCph12EeFwP7udg60S8RL0Jf3uCWj7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران روز سه‌شنبه پنجم خرداد پیامی منسوب به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، را به‌مناسبت برگزاری مراسم حج منتشر کردند که در آن می‌گوید آمریکا از این پس «نقطه امنی برای استقرار پایگاه نظامی در منطقه نخواهد داشت».
او در این پیام توضیحی دربارهٔ پایگاه‌های آمریکایی مستقر در کشورهای خلیج فارس نکرد اما هشدار داد که «سرزمین‌های منطقه دیگر سپر پایگاه‌های آمریکایی نخواهد بود».
مجتبی خامنه‌ای همچنین با یادآوری ادعای ۱۰ سال پیش پدرش علی خامنه‌ای درباره اسرائیل، مدعی شد این کشور نیز «به مراحل پایانی عمر» خود نزدیک شده و «۲۵ سال بعد از آن تاریخ را نخواهد دید».
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی را از او منتشر می‌کنند.
@
VahidHeadline
در پیام منتسب به مجتبی خامنه‌ای با اشاره به گفته‌های ۱۰ سال پیش علی خامنه‌ای، رهبر کشته شده جمهوری اسلامی، اسرائیل «رژیم متزلزل صهیونی و غده سرطانی» توصیف شده و آمده است: «اسرائیل به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگرِ ده سال قبل رهبر عظیم‌الشأن شهید قدس‌الله‌نفسه‌الزکیه، ۲۵ سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله.»
این سخنان در حالی عنوان می‌شود که اسرائیل و آمریکا در یک سال گذشته در جریان دو جنگ، مقام‌های عالی‌رتبه  سیاسی و نظامی حکومت ازجمله علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، را کشتند، بخش بزرگی از برنامه هسته‌ای جمهوری اسلامی را نابود و تاسیسات و زیرساخت‌های نظامی و اقتصادی ایران را به‌شدت تضعیف کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75729" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75728">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFzG9fQuyY96YPMumc4AyxM-F1CLURlzGCEwTRKWZovHE5-PNjStorz4JeAUCbk_Kgjjrx-8TBA30ADEzbsDXFvl401WIVoy7J57wiwTlaDBcfQR9eA5aZe8JxwUi-UJwld2JBJ2vL-pJddPdsq8SDAks2d6scQFNYn8aVb51KHCVZL57YqVgkhMubLgAEw7DMTq7DGJ6HunHZWdZ-2F77dR-4Gg0BQpA2XBdEPAMhGh1VmS7lCFkFyBpDjg7ZZhkka5BJIqULZa7Htwu2sAXVZbsma36ux1Tk1mq_7PoSdAUh38mVb_99euCSkHVBZZbYOupGP0Hmqm90zaMQKpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر می‌گوید گزارش‌هایی که ادعا می‌کنند دولت این کشور برای تضمین نهایی‌شدن توافق با ایران، ۱۲ میلیارد دلار به جمهوری اسلامی «پیشنهاد» داده، «کاملاً بی‌اساس» است.
ماجد الانصاری سه‌شنبه پنجم خرداد در شبکه ایکس نوشته که این گزارش‌ها «توسط طرف‌هایی منتشر می‌شوند که به دنبال برهم زدن توافق و تضعیف تلاش‌های دیپلماتیک با هدف کاهش تنش‌ها و تقویت ثبات در منطقه‌اند.»
او افزوده که تلاش‌های دیپلماتیک قطر که با «هماهنگی» شرکای منطقه‌ای انجام می‌شود، «شناخته‌شده و شفاف است».
ماجد الانصاری انتشار این دست روایت‌ها را «تلاش‌های مذبوحانه برای خدشه‌دار کردن اعتبار» دولت قطر نامیده که به گفته او به‌عنوان «یک بازیگر بین‌المللی قابل اعتماد در مسیر دستیابی به صلح» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75728" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QcpFB0sZXAbsudMyUWUsSb4cjD0odrMiugila17FSw0YVzlg3eXqZgXRG_hNHzreIc9IBKfWYGEpNyxjWBAfxCOiZ6c-lUX26Z9IgF95oxaJOegTEA1irfqt-O7RpmncWXUXN-ZZM4z_UZ58MJFJeOGCGQzCuAF9GvQux7kFfJ1ZMzN4C2MuQ09shkSD8Nuxzo4g8-hLtCnfD6wU-JCDVbvWJ46JtQQNnnaYLdjMg2wIYHJ0fal8UOETzkCb_Yu2uhnyHDTonWW1gr-FzsReyUNO9r3DF-O_vLxzOfI64R5h-6euyRbJpgXRkj9Qie6oFQT9CChJd7CqnTb6t6rmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zur3w3edAzkdig9ka4fvrMs6ZnTGRTdNAwfsItLaao1Ij8begZJBpk8mYdv1GSQ1ghjX6dtxNvnyEKfyg_FaT3w4Sh4lsQcn2vYj0JQj_w_112TWIufNTvHJIQbcUl70E7d6ePXPVViWuHmlRfLVAriPh1Zj1sQZdiO8wl4aeg4JMpeYnJkp26T-SEhafOsPRHSB0tHMhACUPRPIMu2zdT6BNkn2rB7utg5WArnx3BCHnxnGFyEPrRd9-40tb2fb-qIoVi2fnOVF3bk-XRZ7yx7MgZaBfxOhiJ23WVKSJ-wlMblasOM-pK_Y0PfJi10cJ_ou3FvpzxqV3yu2TIogUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tA3ko4QyQe6U7nfNw9uoOxjKwakciJ3ficxKx6PDcjKA5-agDbrDOSbM7yZd3UtQQvEsW8nWZgB82wTqXsS7xhn7UWb0jvZBrpm2kO_gCdoTQewgibYq5oUZwHsE7c5vKf-RJDV74pQRZ1Dey8nOJ7i0I7wNK4fKfDg-iQWoZFUmF6kc8eJxxU3swK_IpoL4JV0pDvSfj2BSuEltEQUCDRGHVfnAzz7lnT5hNugezLO4j8M1KvjV7LgnPJMY5AlizaYqTwZIey-AZSqc770GLc4bXmdbB9FW360kOYiDjKi2_hQ855n7YIEyVRqj3e_y9HkPZx23lHIUGhom9kGZIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضائیه، اعلام کرد غلامرضا خانی‌شکرآب به اتهام «همکاری اطلاعاتی و جاسوسی به نفع اسرائیل» اعدام شده است.
میزان مدعی شده او «سرشبکه عملیاتی موساد» بوده و پس از تأیید حکم در دیوان عالی کشور اعدام شده است.
در روایت قوه‌قضائیه، اتهام‌های سنگینی به او نسبت داده شده است؛ از جمله جذب افراد برای عملیات خرابکارانه، دریافت پول نقد و ارز دیجیتال، تعرض و اسیدپاشی به خودروهای افراد مورد نظر موساد، آتش‌زدن اموال عمومی، تهیه بمب و ارسال آن به تهران، تصویربرداری از نقاط هدف و حتی مأموریت برای فراهم‌کردن مقدمات ترور یک خاخام یهودی در یکی از کشورهای منطقه.
ابهام اصلی پرونده، نحوه انتقال خانی‌شکرآب به ایران است. میزان نوشته او در خارج از کشور شناسایی و با «فریب اطلاعاتی» به داخل کشور هدایت و بازداشت شد.
@
VahidHeadline
میزان نوشته است: بر اساس اعترافات متهم، یکی از مهم‌ترین مأموریت‌هایی که سرویس موساد برای وی طراحی کرده بود، اعزام او به یکی از کشورهای منطقه با هدف شناسایی و فراهم‌سازی مقدمات ترور یک خاخام یهودی بوده است.
@
VahidHeadline
گزارش دستگاه قضایی اشاره‌ای به تاریخ بازداشت و محاکمهٔ متهم نکرده و در عین حال وی را «از اراذل و اوباش یکی از استان‌های کشور و دارای سوابق نزاع و شرارت» خوانده و ادعا کرده است که او «به دنبال جذب افراد و به‌کارگیری آن‌ها در داخل کشور برای اجرای اقدامات ضد امنیتی بوده است».
از روند محاکمه این متهم گزارشی منتشر نشده و گزارش قوه قضاییه نیز مدارک و مستنداتی از اتهامات ارائه نداده است.
دستگاه قضایی جمهوری اسلامی در ماه‌های اخیر به شکل تقریباً روزانه اقدام به اجرای احکام اعدام معترضان و یا افرادی می‌کند که آن‌ها را به همکاری با آمریکا و اسرائیل متهم می‌کند. برخی نهادهای حقوق‌بشری می‌گویند جمهوری اسلامی از اعدام برای ایجاد فضای ترس و به‌عنوان عامل سرکوب استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75723" target="_blank">📅 17:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aK6ZWZTcScO5Vy3H2UAKgCYLATwvISefZ9u0-1nyP0MlXDY1WOeELDS7mr8UMHvcKZiMlesRK1MiRFnNvdryqsKKNWTj_Qi_dxjU--FzuTpyp36WrugaRRexWJBnS-d1RoG2RjVQxM2yBqlixGSdrhrWZJF4qRlg1gSfDz6o6rxd5dZ2yS6PJRZW5Tk-lZ1ttRp4xvQhq-LdAIu8GU8mUfj4nEOwCaNO5zCuj3MB_qFyOWmnxfzgt6_LIo-0KQcW1TrB6l5UMJCpY3yi-wL0oWkmSFcagOeG3qhR7uFtbx_-XrSkKsTAq_miPLonOh2NW5YEeFAxgskAIVWftDoSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DDs0XHO1sASJShkFwOupavucaq8B_Fzs9XIktcZqcirSwdrojD7zFcORNNgvYesURLBT5-V-BXrozPZ5FPkuZ17Yv9JjC3Uxl7RqczO1UgsdDyWrncQU6AzqzYJgR3AFbmYWFxmzyeLIwagG8qKgBg5u8j6CRekVKuJjufjaLVOLLIxxlu2MsjHKgpIBACjgLcmYlPcdoGdCOSmKq2HoTe3kiVhionVb2DDmvNQyZKmvK77C4KG41PLG7pNVWGu9Xiuwrc4q6KOGv-E1BerQ66BcWrrLrPTx9jm_JwYADZD_ZUVP_O4R3Hluq58viFGJ91iFFsrhmt2RTyawwHB9bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با وجود حملات اخیر آمریکا به سامانه‌های موشکی و قایق‌های ایران در خلیج فارس که وضعیت آتش‌بس شکننده را متزلزل‌تر کرده است،‌ مارکو روبیو، وزیر خارجه آمریکا روز سه‌شنبه گفت که توافق با ایران «همچنان امکان‌پذیر است.»
او در هند به خبرنگاران گفت: «امروز مذاکراتی در قطر در جریان بود،‌ و باید دید آیا می‌توانیم شاهد پیشرفتی باشیم یا خیر. فکر می‌کنم بخش زیادی از زمان صرف دقت در کلمات و واژه‌های به کار گرفته در متن اسناد می‌شود، بنابراین چند روز طول خواهد کشید.»
آقای روبیو افزود: «رئیس‌جمهور تمایل خود را برای انجام این کار ابراز کرده است. او یا به یک توافق خوب دست خواهد یافت یا هیچ توافقی نخواهد کرد.»
آقای روبیو به خبرنگاران گفت که تنگه هرمز باید باز باشد.
او گفت که آنها به هر حال این مسیر را باز خواهند کرد و افزود: «آنچه در آنجا اتفاق میافتد،‌ غیرقانونی است و باعث بی‌ثباتی برای جهان و غیرقابل قبول است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/75721" target="_blank">📅 07:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OqvdJwGquvJE6IsgXxjCEQqps3dMqcykVViHSTjHcNsA97v26L9uWsTCHdGGQcaet7L6MvfVn6tkkr-DV0vYbDM7bY5J6oLrk_niFYyQan6S3tI-ui8DGD8kve1djs0EbjTxaBl0vRx4j99TQVhmJh9F8lsjUsF6X0pKYCcBtVJYt17cLEDZbrF0BcAb0OGN9kwdOSjVpNHCdVU9xUU149sx0uEqtKkSJVA1Bu5pP03WrJsUIWZx9o82r7BXE-Rn7ADF3-sEIL1PqgUI337D8EXIOhwCjKhhmbjlYE6SzfCm2fuw8_rR4RJLPPpneGHBcnIE3zh2MgI9LHkuN0ZfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اواخر دوشنبه به وقت واشنگتن گفت مارکو روبیو وزیر امور خارجه، به در خواست همتای روس خود سرگئی لاوروف، با او صحبت کرد. در این تماس تلفنی، دو وزیر درباره جنگ روسیه و اوکراین، روابط دوجانبه و اوضاع ایران صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/75720" target="_blank">📅 06:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75719">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NodMetqLAt4Ixm7e4y2S9SEI_irXDPdaD02g8B3yHYFVbAI4g3-ZxWKyjLfMKF52Lq0ElS2Gcx1chHxfalZyWcn3HKVKnz-XeohKnurGKf5fEFkvmiiqxdCfmMcn_ZS1y3eKDZFv5scyB025LDHsZ0DkOaHIgRo1ORefyrLgO8N_lh7NVkTX_rwzoONkFX3BQb3xJiEG9UZFaOLw6VKO9JX5qbIiBaLstvp_b9Xi_RiBQL9UV2g_78fT6yult4sH38vVDaiB3ZPVrtQ39sHE-l0JIy9ZwOQpD7lj_66-JZcFUqd80a3VLOXq8V38NhtegVjnlMyLbF4IT5X9Xv1Q_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/75719" target="_blank">📅 05:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75718">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L_o6GY1ygslaszNtyixTVq0nOsdHjtkhLGo8dbm0B8a6ESO5u2BN50bcvq7Q_lfqlP_NG0x0qU1ezg7zM-RSp94J2yTciKMSWIAfNtix-8HiQdZb_OYuP8jyncMp2VMhLDx-JrT2erMSDk3rMzDFDIEZ0vBjOMcsIWKzz0Ys2fdth49zmH6G11GFJ7iFvaCB26uTnNS2-As6fKWSkBaAR5tgKTMSRxAD95HyW10-Y6onYv99H-WUTL5wtTvAqRFVoV4txJyWfm1WlptH446xd4hPzj4LcKukwQn23PXWHq4zGcoGXXHgzwu-wt8w1mZoYVdQNKxubSdOiIoQiDaJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رماندهی مرکزی نیروهای آمریکا - سنتکام - در بیانیه‌ای اعلام کرده است: «نیروهای آمریکا امروز (دوشنبه) در جنوب ایران حملات دفاعی از خود انجام دادند تا از نیروهای ما در برابر تهدیدهای ناشی از نیروهای ایرانی محافظت شود»
در بیانیه سنتکام آمده: «اهداف این حملات شامل سایت های پرتاب موشک و قایق های ایرانی بود که تلاش می‌کردند مین‌گذاری کنند. فرماندهی مرکزی آمریکا ضمن خویشتن‌داری در طول آتش بس جاری، همچنان به دفاع از نیروهای خود ادامه می‌دهد.»
ایران هنوز واکنشی رسمی به این گزارش نشان نداده است، اما برخی از سایت‌های ایرانی از هدف قرار گرفتن دو قایق تندرو سپاه در نزدیکی سواحل خلیج فارس و کشته شدن چند نفر از سرنشینان این قایق‌ها خبر دادند.
نیمه شب دوشنبه به وقت ایران،‌ برخی از ساکنان بندرعباس و شهرهای حاشیه خلیج فارس، از شنیده شدن چند انفجار و فعالیت پدافند ضدهوایی خبر داده بودند.
رسانه‌های رسمی هم این گزارش‌ها را تایید کردند اما اعلام کرده بودند که علت این انفجارها مشخص نیست.
@
VahidHeadline
درباره همون وقایع ۲۴ ساعت پیشه که اخبارش تازه داره منتشر میشه ولی بسیاری از منابع جوری جلوه میدن انگار مربوط به ساعت‌های الانه.
احتمالا
اون پست ترامپ
هم که تصویری از قایق‌های مهندم شده با پرچم جمهوری اسلامی گذاشته بود و نوشته بود «خداحافظ»، در اشاره به همین واقعه همون موقع بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/75718" target="_blank">📅 02:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75716">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qtfrUwARHEzUJ4LG35AQiuj6OOWDxQJxaPHg7b5YPLc5Hvjalinzcm6Eb-O9o3hxZfzm6GfpUlYpQ8HitsO2qHcdf8UqQzu1JDZdbtj0ndKx9mnUkB_YXiXbmbK49A3zKP2aoZnlGLzJrW2l_PSpXJG9xLCSQqmyvwCeTjelgLG_em9xQjdpUoipcjCOiDlXXGXTH-VcH9HHwFz33HDBP3IFlKSs1rIaCjCYsTar9T4DSYhqmIGmJU_zdaYmMV5MUL7dA3yV0fsr0quPyM3Lr7DX_xhVDjJRvmsfBF1EkHMO5mX_eYg3_yWUr72_Xlm50BIt6r3wBOnygqM-i6n1ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q-Fbzdg6MkL6EvKd2wlevhGPkAl-0hDwgaxDOI-wBoVm3Qe3nNz9rEuCBaEzXcqS0m_d6sUTLxAPVbeqztl6jmifjmnwrmZDu5PN9zV9qPGsCuzIQFXxk-da1ZfTFn5EmCVEKBUWhkjUvLQiwzjGCD1jRj-fP4gF4gG629Go4AZG2vyEUw06g5a9oojHgDfZ_rS8KrZpnTxVwvShQ3D9Uf54Rk9mr-s0skZ7qGUcaCCknP6wpyoU4uzUWkRRO-lI8WtEzmHUqkqacn1spJjaqWT9Vq9Rfxo0xjrsxoJJL2pil8dyAnbRGiM0T6GM_LFkmtVEFNYm_RLIx4JcwKD_Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری دانشجو گزارش داد که در ["حمله سحرگاه شب گذشته ۴ خرداد"] در جنوب جزیره لارکآمریکا و اسرائیل به جنوب جزیره لارک، عباس اسلامی، قدرت زرنگاری و عبدالرضا گلزاری، نیروهای سپاه پاسداران کشته شدند.
براساس این گزارش «تعداد دقیق کشته‌شدگان هنوز مشخص نشده است».
@
VahidOOnLine
گویا این واقعه مربوط به اولین ساعت‌های دوشنبه است. یعنی حدود ۲۴ ساعت قبل
ولی به نظر می‌رسه اون دسته از منابع جمهوری اسلامی که این خبر رو پخش کردند عمدا طوری گمراه‌کننده نوشتند که مربوط به صداهای شنیده شده الان به نظر بیاد.
ولی این توییت مربوط به ساعت ۷ شب دوشنبه است که درباره همین خبر به نظر می‌رسه:
دیشب یه قایق سپاه در حال مین ریزی در تنگه هرمز مورد اصابت یک جنگده که از خاک امارات بلند شده بود قرار میگیره و چهار نفر از نیروهای سپاه کشته میشن
YourAnon_Zeus
حالا این خبر درسته یا نه نمی‌دونم ولی مربوط به
صداهای شنیده شده ساعتی پیش
نیست. من هم ساعت سه چهار صبح دوشنبه پیام‌هایی داشتم از شنیده شدن صدا در قشم و بندرعباس
آپدیت:
پست بعدی: آمریکا اعلام کرد که ما بودیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/75716" target="_blank">📅 01:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75715">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VYcYE73bwaVr0GmLj-Hdyg5l_wc59CT5jy-Hfb-R6yH8Cb9kY_X8eK5181aaGRzr6u3tClLGlkLIs5I6jciXN9RXUHg4NxgEHZYwcQj7o2Q4kKDUFzU6SgzGSEev_qxs7UitAwR2VQzhho6iq79wQFnj9cROctl9XTfFp46x6U3FWEqaz1TggPsiNuAjyuaGyce4lfQhAfEx3vr9UYXXkzcrDGOer_bAA77OF4xwpt75jWVtFgXJw0SKYeUF9P3yrD9Mp6o7_g8DTUMmEqIOj6l56t6Y2HTPZtJDO7trBXEyCv-UcWTKVZtQB5rCWUcoJ7iKPOxHdj4Cxsn_11ZKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اورانیوم می‌تواند در همان محل یا جای دیگری نابود شود
ترجمه ماشین:
غبار هسته‌ای، یعنی اورانیوم غنی‌شده، یا باید فوراً به ایالات متحده تحویل داده شود تا به کشورمان منتقل و نابود شود، یا ترجیحاً، در همکاری و هماهنگی با جمهوری اسلامی ایران، در همان محل یا در مکان قابل قبول دیگری نابود شود؛ در حالی که کمیسیون انرژی اتمی، یا نهاد معادل آن، شاهد این روند و رویداد باشد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/75715" target="_blank">📅 01:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#بندرعباس
پیام‌های دریافتی درباره صدای شنیده شدن صدای انفجار:
بندرعباس سه بار صدای شدید اومد الان
صدای بمب میاد.
بندرعباس ساعت ۲۳:۴۰
همین الان ساعت ۲۳:۴۰ صدای سه تا انفجار شدید توو بندرعباس اومد. نزدیک پایگاه شکاری یا همون فرودگاه بود به نظرم
سلام وحید جان
بندر عباس صدای آزاد سازی پول های بلوکه شده میاد
بندرعباس ۲۳:۴۰ سه تا انفجار شدید
حاجی۲۳/۴۰ سه تا انفجار شدید شرق بندرعباس
دقیقا صدای انفجار ۴۰روز جنگ بود
سلام همین الان بندرعباس صدای دوتا انفجار اومد
بندرعباس حدود ۲۳:۴۰ دقیقه سمت فرودگاه صدای سه انفجار اومد.
درود وحید جان
بندر عباس ۱۱:۴۲ سه تا صدای زدن اومد
بندرعباس، ساعت 11.40
صدای شدید انفجار و لرزش
سه تا صدای انفجار پشت هم شنیدیم بندرعباس
بندرعباس 11:40  شب 4 خرداد صدای انفجار
بندرعباس ۵ بار صدای انفجار
ما سمت پایگاه هوایی هستیم نسبتا شدید بود
پدافند سمت فرودگاه بندرعباس فعال شده ساعت ۲۳:۴۵
آپدیت:
رسانه‌های ایران شامگاه دوشنبه از شنیده‌شدن صداهای انفجار در بندرعباس و همزمان در خلیج فارس حوالی سیریک و جاسک خبر دادند.
معاون استاندار هرمزگان اعلام کرد منشا صدای انفجار در حال بررسی است.
@
VahidOOnLine
آپدیت:
کانال‌هایی غیررسمی نوشتند که به فرودگاه بندرعباس و اسکله باهنر حمله شده. منابعی مطرح هم با تاکید روی غیرقابل تایید بودنش نقل کردند ولی منابع رسمی چیزی ننوشتند که لابد مذاکره و توافق به خطر نیفته. تکذیب هم نکردند. حتی منابعی هم مدعی شدند حملاتی از سمت اسرائیل یا امارات بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/75714" target="_blank">📅 23:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=rlBLE0ihYujCBK_b06IHIaNWlrF4ESFVLU88TTO1Vcb-qGF0WpCkXk9joGCsNZjdyCD4ERl7jnXGkyXn4Za93JskQ-nKMNRilnOGl-yXpXYLZvIuybzDjKAX5bmXULaYZ1a6NuUM6tElpk8yyNobClz3ESVMSxHHs4TOcpUqCaHm2OxAwWBwZ3bFsQU8_SW7lP_J2e3RlHK088kCX2rHhy6m3j18aBnBdpFAzO8dEp0V_2Tk-dk6AfucOrXu8fReNXExCHkqCyzGZTrx-C12V47tJ2FT98Ki86MbuAK-a2HThPT2Mz5iCLdgiPOuiDj8OJjON62mKQ3N8Hudp-dPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=rlBLE0ihYujCBK_b06IHIaNWlrF4ESFVLU88TTO1Vcb-qGF0WpCkXk9joGCsNZjdyCD4ERl7jnXGkyXn4Za93JskQ-nKMNRilnOGl-yXpXYLZvIuybzDjKAX5bmXULaYZ1a6NuUM6tElpk8yyNobClz3ESVMSxHHs4TOcpUqCaHm2OxAwWBwZ3bFsQU8_SW7lP_J2e3RlHK088kCX2rHhy6m3j18aBnBdpFAzO8dEp0V_2Tk-dk6AfucOrXu8fReNXExCHkqCyzGZTrx-C12V47tJ2FT98Ki86MbuAK-a2HThPT2Mz5iCLdgiPOuiDj8OJjON62mKQ3N8Hudp-dPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، روز دوشنبه خبر داد که دستور حملات تازه به جنوب لبنان در تلاش برای «خرد کردن» گروه حزب‌الله را صادر کرده است.
ساعتی بعد خبرگزاری‌ها از چند حمله شدید اسرائیل به این منطقه خبر دادند.
نتانیاهو در ویدئویی که در شبکه تلگرام منتشر شد خبر داد که خواستار «سرعت بیشتر دادن» به حملات ارتش اسرائیل شده است.
او همچنین حزب‌الله را متهم کرد که با پهپاد نیروهای اسرائیلی را هدف گرفته است.
صدور دستور حمله بیشتر به لبنان، همزمان است با خواسته دو وزیر افراطی در کابینه اسرائیل که در همین روز خواستار تشدید حملات به جنوب لبنان و همین طور پایتخت، بیروت، شده بودند.
حمله اسرائیل به این منطقه در حالی رخ می‌دهد که در سوی دیگر تهران و واشینگتن از جمله درباره پایان جنگ در لبنان مذاکره می‌کنند.
حکومت ایران در هر دور از مذاکرات اخیر خود با آمریکا، پایان جنگ در لبنان را نیز خواستار شده است.
حملات متقابل اسرائیل و حزب‌الله در حالی رخ می‌دهد که دو طرف بیش از یک ماه است که به طور اسمی در آتش‌بس به سر می‌برند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/75713" target="_blank">📅 23:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75712">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rLGNsZPR3reA1W9hYG438NivacvLet-mtqh2TAMbIRFNtAbp4M3rVtXKMCMkWg5IwRTVTJ0Y9eYSR_TFB9RlJPlFAmoMISQiwo5iZC-ee60-AWT28cNTmIMroZVXiL9nFt5DdVtRi3IxpErNc5Zh8DNZLwfJpZDk_VguNKY3AHMBUv-9XDuakkeLCM28Zli5yptlOsKx3t81n7CR7eN5EnnXQbGVym96A7-jZgazvM7MVWv8omDSYjwK7bMsxwM5RpkFtAK2OlVseaoSQLY1fgzYXQhM7HITpK5Yd_mlC4vXQkYxAn5aVEB5dbR6QlPSa-g56cQXB5L5I8jz9cE2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره به نقل از یک منبع آگاه
گزارش
داد میانجی‌گری قطر به دستیابی به تفاهمی میان آمریکا و جمهوری اسلامی درباره دارایی‌های مسدودشده ایران منجر شده است.
این منبع افزود با توجه به اهمیت بالای این موضوع برای ایران، احتمال زیادی وجود دارد توافق میان آمریکا و جمهوری اسلامی فردا اعلام شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75712" target="_blank">📅 23:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eosoPHsDX4-iM93vrVYGcojWkpBxweH7NckFPvWgRBdqlWsn-MwLbiaUMTAKakcnmIx5s3Rsyn_kWPlqHPPtE7HbOE_RIDTsVhLsi4LceATSvoBrUn1nVk_GzCGydaQFloJgFCareBQ9Cc6BfrTZDwizEVm9NSy5cmtqZBtZoHJQEdI6cAIT7GYqrZDsaiZo8Hx_dGFwNbaYNgfLNJ-OSYw4OZHieniWQaSBTE6xAmjHGKRnB-9Wympig82u8IiR0qTvo9K1ENRz-DvKJpBktcG4gZ4wyWttUuSwaapU6ZwYw0uQT_eVAfuoQBGG9Acpest5sw8kqE4EqM-MwO6ZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پس از انتشار خبر تصویب تصمیم بازگشت اینترنت به خانه‌های مردم، چند رسانه در داخل کشور می‌گویند که مسعود پزشکیان، رئیس جمهور، این مصوبه را به طور رسمی ابلاغ کرده است.
رسانه‌ها در ایران روز دوشنبه از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌ بودند، مصوبه‌ای که برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، بود.
به گزارش سیتنا، پایگاه خبری فناوری اطلاعات، بر اساس این مصوبه، اینترنت عمومی باید «به وضعیت قبل از دی‌ماه ۱۴۰۴» بازگردد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75710" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qx-UqrE18BgUJUhM5ICNmoHwQ0DwBuf1m1aF7x18O1A6tb06sGkQVesud-IeWr3GVjKUYRkm65P59W5O3MuSA6doXmuQzVPAjv2i_gd7ekNvUVuIsiQD4899JW31avgaHnUCeNtKjWxvvhIK-fpyqF_ieYABhi3fEEAB4lP3B8SQaosE7HoGjx44yHp7dhdx1MUcNqKjxUKoil6BSh9ioR8BVEZPaqrfpjQ_RuoYi7FoSzyFWEcmzGVRvbIgGT7XW0Bs3aBHGmwqjfUIIXsPuK6hEP16_y9LiDM64f0rUjLmkq-gJng2S-aEz_fO-bQuFTtNUCaRbOCRLe8KE8tPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از منابع آگاه گزارش داد پیش‌نویس یک یادداشت تفاهم اولیه و نهایی میان آمریکا و جمهوری اسلامی در حال بررسی است؛ تفاهمی که شامل بازگشایی تنگه هرمز، تمدید آتش‌بس و کاهش برخی محدودیت‌ها علیه ایران می‌شود.
بر اساس گزارش العربیه، در پیش‌نویس این تفاهم‌نامه آمده است تنگه هرمز بدون دریافت هزینه از کشتی‌ها بازگشایی خواهد شد و عملیات پاکسازی مین‌ها نیز انجام می‌شود.
این گزارش همچنین می‌گوید در چارچوب این تفاهم، به جمهوری اسلامی اجازه فروش و صادرات نفت داده خواهد شد.
العربیه افزود پیش‌نویس توافق شامل تمدید ۶۰ روزه آتش‌بس است و امکان تمدید دوباره آن نیز وجود دارد.
بر اساس این گزارش، آمریکا همچنین متعهد شده محدودیت‌ها علیه بنادر جنوب ایران را کاهش دهد.
منابع العربیه گفته‌اند بخشی از دارایی‌های مسدودشده ایران نیز بر اساس سازوکاری مشخص آزاد خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75709" target="_blank">📅 20:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FQT_CuGovqOXSJisn00A89BcDrJql8F1t6pM8TKdQDufECj_-CizMSR0XUx0-XJCYNHkKgdMpIGY4i4D-HJfTdIW5yk_1rznRKtlvhPa500ZL000GHAXeRVIFgH3adBMHw1_drIXq8ICzeELCDp5R_3EL-4Ko_1pBRaxJHZaoWpbOJbWGoWatIy_TCHP2tWkgXtpEIvkMtvhekov53r_1BIWoJvG5qBYpOR80VeqIbnDW7aXadqfE5FnOIZwpVRvZwIEWq3C2A2lnev-tmjhQQK2UdAYtCQ3hB0F-g-b4zkeZqnx6ONscM7EEZDhV7MeZsw14m116vqeWuP5lOMXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZMpLzKF5jLeEPIQro0JaiPhUUDRYxYJAdlG76hN9UvqGOXOIKgBd3811HkFCBA9FtcKbDl8TvSq-SsGFIqxawvHP1fJCc-5wkGIItSqzjML6CbdfU2xAZQ9IJrckwUdLk_tvNENBi_-UEl3MrJJBptpZYBy6UPZky8LtTR1J8DJ0L9PQgvnLZea4zH85R2yXTPV-Yj2WLPq-U3hJEVv7LHZb-hAeK92Ka79bKbJPmT5VJFX9puXPsCwU8nkVPa4xEnID0SbpZv2XKaiATTaN1l3QD7QevELIqr8r3EPCoum9owVTMgcf1wPRMbfxieXngf7XsC2-yah2woFE00-AxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، در پیامی با اشاره به «میدان نظامی، میدان دیپلماسی و مردم مبعوث‌شده حاضر در خیابان» نوشت: عقب‌نشینی در کار نخواهد بود.
او تاکید کرد: بیش از هر زمان دیگری به وحدت و انسجام نیاز داریم تا آمریکایی‌ها و اسرائیلی‌ها مایوس شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75707" target="_blank">📅 19:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75705">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WU1h023z3ULxOx0jhSPZRg0TEjqmlArFfJxzTSVkm2yv1vB3WZCK---8xGPHPhsVKA7aPHV_qR_sj_8Pzr6TW9PegpA5YmDsS2_CR-ReZDtlbuEX6a1K-Pj6Pfn5UB0NNebhDzVQD9IvzxqdMJOgq2KR9vcJ8KNgow8nT94GuHAC8UuPw0VLkz34oLKnq4_QoQuh0SLlHLrtuDutH5tlZXu_g_F0QxpMKJfO9Mbnyr864AT-vmAdwzz8UUxrxFJUg5Hj2xIS0CnmnHUyQh5FbNjkZtsmxnQk2kQ9E4yAF0THWqYL7Hv-LIIrmcltSmZpMuBRlQAdyAuzqwGe1dAUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HCknITS1UF00Npx_ThV0GwK4EcbjR8ef-iz7kvQZdTkswsfsYjUAUrWcTtCK7xXIaJVm0vJeIelIPWaiYvgSIqu5BisJ3FicRayZuo12X3PMKOPMGA3Geaujb-PYeHgtEYYnXcajW6MnFuTRkJlOUwHxG0xLHfexqYfVf5s6STVo7KMf6l8fhRpT5HYWC4D3Jb_sSMZKMTY3sSEDZUu4gx_tMyiCj7g62j6PDBQ0LiLgknvfzOlZ4xwSNpmrzYrOt7vS3nWG-bgO_7zIrnjhDnYeE6hwMlUQEiXWaKJ2_mOau0R_OlvVBrPn8Xss1hmditKW3A7Z3_ht0m9QUV-Jug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ از اکانت بقیه بازنشر کرده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75705" target="_blank">📅 19:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DXBJiwHqv-giUiVz27kGU6oN0y43FTg_yO9nlpMm4Z4m1BaBUsQHsI5zN-ukw95GzsY_xnvZRlItMP2ywoVfvZLGmVscaBU9eiW24L8NgZgsEP5PBNivQK7G4IKCfXNfgi7OLDY26xD4idHv1RxqL8wo4LrhtgR0UeRdxWjrusMpqHy2Epdp4nkvTCExlvoNaqaaM9UwOz0dC3PWsMpOuW15I3Mp6IBd6OnfuLEOfhgy4HgIr9Tu4aDz115C5W_bSiv2QMPpMK4d9NMqIUHaxqnvLczBf97nZgY_jCMqbzGItLFNXMEOHodYDu8tyv3sHjgCNUGf6d89DcHsc2ZOtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lbUbYcAPXu0WKJXk1EpiaLODWyykL9cETb3XZ-BtV49i4RkNqLGvBCS3-8DqNmwY2HFX0f-MCf9dBXW9s-u_6TJ4ZmTA6LwPsB7ox5fhk6_VqiWlohmO60C0gQIxrjOfrg7huC_ZXzTYeh0k2GkSFuvsWpSJMw0unEpa5hS67JB2udzCHQquiQqvlTUpB14QUwUt5VdVx8Umv3tzvO8zfl0izJ267xbkHlpP7DG3QG6nd8FFrKHotpyy76nl_NCnLv765nk569T7hjbyS7pzWQH4gO8MVm6epnYxC1UnPYolur3YYoGutt0OIvtq-eNNlWD16rySJjxyK9gHlX3JnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه در تازه‌ترین پیام خود در شبکه اجتماعی‌اش ضمن خبر دادن از پیشرفت «خوب» در مذاکره با ایران، از تمام کشورهای دخیل در این مذاکرات خواست پس از حصول توافق با ایران، بلافاصله به پیمان‌های ابراهیم بپیوندند.
پیمان یا پیمان‌های ابراهیم طرحی بود که دونالد ترامپ در دوره اول خود برای تلاش در راه عادی‌سازی روابط میان اعراب و اسرائیل آغاز کرد و موفق شد تا چندین کشور از جمله بحرین و امارات متحده عربی را هم به این کار ترغیب کند.
حال رئیس جمهور آمریکا روند توافق با جمهوری اسلامی را به این طرح پیوند زده و به گفته خود این «خواسته اجباری» را با دیگر کشورهای عرب خلیج فارس و همین طور ترکیه مطرح کرده که به‌فوریت و همزمان به پیمان ابراهیم بپیوندند.
@
VahidHeadline
دونالد ترامپ در شبکه تروث سوشال نوشت که پیوستن جمهوری اسلامی به پیمان ابراهیم، می‌تواند به «اتفاقی تاریخی» تبدیل شود.
او افزود که در گفت‌وگو با سران عربستان سعودی، امارات متحده عربی، قطر، ترکیه، مصر، اردن و بحرین، تاکید کرده لازم است همه این کشورها به‌طور هم‌زمان پیمان ابراهیم را برای عادی‌سازی روابط با اسرائیل امضا کنند.
ترامپ نوشت: ««کشورهایی که درباره آن‌ها صحبت شد عبارت‌اند از عربستان سعودی، امارات متحده عربی (که هم‌اکنون عضو است)، قطر، پاکستان، ترکیه، مصر، اردن و بحرین (که هم‌اکنون عضو است). ممکن است یکی دو کشور دلیلی برای انجام ندادن این کار داشته باشند و این پذیرفته خواهد شد، اما بیشتر آن‌ها باید آماده، مایل و قادر باشند که این توافق با ایران را به رویدادی بسیار تاریخی‌تر از آنچه در غیر این صورت می‌بود تبدیل کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75703" target="_blank">📅 18:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gm3qTEa4tsn58p4xQfdWujI3BbKP1Evvbk869-m7nTqt8z8ng_U99WHnRQRtym4yuDqh-SThx-5Bc-G40XmwiLna2xr5_Y0G4vgbUp5lw9v0sqOW_Mha4O43J0NyTj64IJPSf8hjg2C3lp5LnyOCcNULZYVeWLhbL7F67BnF_Jcsfa-QBD-2r1HQ-4lxuBOpxCoFrzIBJMxnViVdZvbqVRiZyZsfAZxINs34iieNdjmdiifi4-mcVNiswx3Taab5PU9NnkkFWAbD4-FcQbTrzpnlV7L4bwwh4iTxWf-5GiFc4X1wCF4n4hgYD2k1S0i5HetaWWJ40ZM64W1f9Y2VeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kjOaDrylni9IDk2Iev99UhYzJbJXRXigG0ePCJ2PuBvhwvDGMWYozR0sQEcvSNaLjwognFRUYirKxQsSsJ71w6A-wgMnH45DiGaRjRiC32HeKIsGpOSzbq8Cjty0iYsZChoff8d4B0oLh4db6eMyR0MvpV3wfzIKmZeD79Lfr72K4gYMEuOKmGet18NAyvKAIUq3UFxHEOClje22P6MZSqYZHhBRlBhL-uEoNPBhK7ow9JInpDyfaDQ1cT2BgGIyUqTfhxn9b452-lS5QsnmV9VhUmTpofL04doTKJTV58EgYVl4Z9wZ39hMBT97X2LM7AfqvxW4DgLpwS0Wzqrvow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری‌های رویترز و فرانسه به نقل از یک مقام آگاه، از سفر غیر‌منتظره محمد باقر قالیباف و عباس عراقچی، مذاکره‌کنندگان ارشد ایران، به دوحه خبر داده‌اند.
بر اساس این گزارش‌ها، رئیس مجلس و وزیر خارجه ایران برای گفت‌وگو با نخست‌وزیر قطر به دوحه سفر کرده‌اند.
رویترز نوشت که این گفت‌و‌گوها عمدتا درباره «تنگه هرمز و ذخایر اورانیوم غنی‌شده» ایران است.
رسانه‌های ایران گزارش داده بودند که عبدالناصر همتی، رئیس کل بانک مرکزی ایران، برای «بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات» به قطر سفر کرده است.
هیئتی از قطر هفته پیش به ایران سفر کرده بود.
یکی از خواسته‌های ایران در مذاکره با آمریکا آزاد شدن منابع مالی مسدودشده‌اش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75701" target="_blank">📅 18:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyKAUY_p9U0LnEd-Kkf3W_UpFllKiBG2bCKGSWyiHYltxHW_ytpM5Sm6IxjDgaDca-3UJnINwTqFLzH_TIJb7BIVKiF12jb0vBYq2PofGry9XmReOYuHTupBRfKjsz0eFHhc_VRXj68FmYeeIULnvMqR7xCSg3nwO7K2Oe2qCavacco6Mip9byBOVX9YvjfcA_LpvMQvMbm3oWHsW47xh9FgVjf09Wg1K3AHR09R4KQB5wfRmT8jEK5YsKLcALvMtujNLsIqVlb8APT5QviH_Cter1u2bvDYFpM_Ftkw1-lBBD7mqevod8GmymEcEeO8jhy3zJtZgO_1FX-WexdcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پیامی در شبکه اجتماعی تروث سوشال گفت توافق احتمالی با ایران یا «عالی و معنادار» خواهد بود یا اساساً توافقی در کار نخواهد بود.
آقای ترامپ در این پیام، منتقدان خود در میان دموکرات‌ها و برخی جمهوری‌خواهان را به باد انتقاد گرفت و گفت آنان «هیچ چیز» دربارهٔ توافق احتمالی او با ایران نمی‌دانند و حتی دربارهٔ موضوعاتی اظهار نظر می‌کنند که به گفتهٔ او «هنوز مذاکره نشده‌اند».
ترامپ تأکید کرد توافق مورد نظر او با ایران «دقیقاً نقطهٔ مقابل» توافق هسته‌ای برجام خواهد بود؛ توافقی که او بار دیگر آن را «فاجعه» خواند و دولت باراک اوباما را به گشودن «مسیر مستقیم و آشکار» ایران به سوی جنگ‌افزار هسته‌ای متهم کرد.
او در پایان پیام خود نوشت: «من چنین توافق‌هایی نمی‌کنم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/75700" target="_blank">📅 18:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoeEol6ZUNXWmAP_A61RHQgG7O_PO1yQNBH33cmwhVlnp5uXLnR5gCFztgGvp1drjVBkfcRz19h-cxhP3sFw5G7GoILiHjx5dykNQf0ncwPxqovW37yLDJS8FMIa0myGLJxdL9A_-in-hid95gGfXMr1pUr9bbhJK5oCBAZxqAN3wCfVVxV9vL84p-DE93BADNsYcvkSHx4v35kJDUAX5_qI-w86COhGS5EAC50Q-Iencqlqna6r1vMs40SXmhPuAwCWIa4B9nB290WuvPmOzoGK4lzW29q6EF9NzXvVKlpsaaN0pjbQM_GQS_LgXxq8Wih_INC1mviqGLaECdnf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌اند؛ مصوبه‌ای که هنوز برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، است.
خبرگزاری فارس روز دوشنبه چهارم خرداد گزارش داد چهارمین جلسه این ستاد به ریاست محمدرضا عارف، معاون اول رئیس‌جمهور، برگزار شد و در آن «مصوبات مهمی» دربارهٔ اتصال به اینترنت بین‌الملل به تصویب رسید.
فارس به نقل از یک منبع نوشت که «برقراری اتصال اینترنت بین‌الملل» با ۹ رأی موافق و سه رأی مخالف تصویب شده و برای تأیید به دفتر رئیس‌جمهور ارسال شده است.
خبرگزاری تسنیم نیز با انتشار گزارشی مشابه نوشت مصوبات این جلسه پس از تأیید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات و فناوری اطلاعات ابلاغ خواهد شد.
در همین حال، سیتنا، رسانه تخصصی حوزه ارتباطات و فناوری اطلاعات، به نقل از «یک منبع آگاه» گزارش داد که در جلسه صبح دوشنبه «بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴» مصوب شده و در صورت تأیید مسعود پزشکیان، جهت اجرا به وزارت ارتباطات ابلاغ خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/75699" target="_blank">📅 18:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqIxSE8wZxN8gLZa5aZSy5Jk3zxnGzN2sxX8naUNv_w82n9zNX2ZlNwY1OrBC6QM2C_vE2FlhrV7u9Zqdjld6Ip3k_bDCHfuzTarcqEJmgH9isZlMbU7juMqRgXDd_lzn06ZoSgu8dJJ_UWe3itNsQo-SMKXsZtG69RNHo3oTRWrg4j4ZaW7OCp-zMNGib9nOEYPM7zDMlo__ubx738kyLYvGEfJR6BiGaEeM7QiJ8EexqUa17cKfeOsN6DEsv1_Y2GguE9HcI8GNhY2RzyvkND_xUn-Q07onAGOrEuuCSYC-zIwha7AXoNumbE34P60VTjrUv5WTQb_YuM4Uh68ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران به نقل از «حسین کرمانپور»، رییس مرکز روابط عمومی وزارت بهداشت، گزارش دادند که جراحت‌های وارد شده به «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، در جریان حملات اخیر «سطحی» بوده و مشکل جدی برای او ایجاد نکرده است.
کرمانپور گفت رهبر جمهوری اسلامی تنها از ناحیه صورت، سر و پاها دچار جراحت شده و این آسیب‌ها «منجر به قطع عضو یا ناراحتی خاصی نشده است.»او همچنین مدعی شد که هنگام انتقال خامنه‌ای به بیمارستان، پزشکان از او خواسته‌اند روزه خود را بشکند، اما او تا زمان افطار روزه‌اش را ادامه داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75698" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75697">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f49VObJf9yl2eLUnvUAQFuC4lur8HO-n5moRCu4iCIER-FGVyQT5inQw3FLrKw6OVE2CQbXRhnf7_nyyOG628bvh-UUGTnbrkRaLD2BOmYw-bU4BgnSxOcnK1IXe-KBUCnhDuQiMErC5xuPiIQgVMLArOE8aMlIdimdWTF0z5CyWPeYzmPOgrxGUKhC1PDS7ibm3hYK4Wqz05CJWQOArBqmOPqojS_W9JIkubqH0-ADN9qnAiyInt646oYTJ7raNXpsOskBn9p53qwz_oo_r4veaYON-z54w5jdZ8eNm33wOTiVgH9CGVEHRjkN9MEKcpAOqyObC4uROwAi3RQ_n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید که سفر وزیر خارجه به نیویورک برای شرکت در نشست شورای امنیت «منتفی» شده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران، دلیل انجام نشدن سفر عباس عراقچی را «مشکل روادید» عنوان کرد.
آقای بقایی چهارشنبه هفته پیش درمورد حضور آقای عراقچی در این نشست گفته بود: «این سفر به نیویورک احتمال دارد انجام شود و البته ممکن هم هست انجام نشود، چون هنوز قطعی نیست. دلیلش هم این است که هم باید روادید صادر شود و هم ممکن است اولویت‌های دیگری داشته باشیم.»
چین به‌عنوان رئیس دوره‌ای شورای امنیت، سه‌شنبه ۲۶ مه یک بحث آزاد در سطح بالا با موضوع «حفظ اهداف و اصول منشور سازمان ملل و تقویت نظام بین‌المللی متمرکز بر سازمان ملل» برگزار خواهد کرد.
این جلسه به ریاست وانگ یی، عضو دفتر سیاسی کمیته مرکزی حزب کمونیست و وزیر امور خارجه چین، برگزار می‌شود.
چین این نشست را «فرصتی» برای همبستگی و اجماع کشورهای عضو توصیف کرد تا «تعهد راسخ خود را به حفظ اهداف و اصول منشور سازمان ملل متحد مجددا تصریح و نقش محوری این سازمان را در نظام بین‌المللی احیا کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/75697" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75696">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lujd_WVb8jnsrdVaEE6gAqsY_AOWzuAeF0CKNV3BiYiZu2enkoH9FP6bkQkhwd_C7wovZbQwYalgbs7auCOjsp6yw-g02bcXcX73_X7zNnWyBStmOKcdXMd5g_eSVEm8VvS9t1gaRePTgUQb8hxkQnSYdM08dOHtCYCWCHPhFCxlOiF7BRTnODH7x3PG1dJHLrAXU8c01a8XL3lc0kZGl3qJqrGh1L7m5QvZf5CJbrBOLIQzTAzM53YTAuPQOnaS4gmqH_Gf-gP1XoCI6DB0FzD6xdHUzqKO6hWIeueBdtQ8G4YefJ9BIizoNnrQAigciGVIcDaF4XKJSscGKnK7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سه‌شنبه ۲۶ اردیبهشت‌ماه ۱۴۰۵، «جانا سعدوئی»، زن ۱۹ ساله، مادر دو کودک و اهل روستای تاریمیش از توابع بخش قطور شهرستان خوی، به دست همسر خود به قتل رسیده است.
به گفته منابع آگاه، همسر این زن پس از وارد کردن ضربات مرگبار، تلاش کرده است ماجرا را به‌عنوان «خودکشی» جلوه دهد.
با این حال، نتایج بررسی‌های پزشکی قانونی و تناقض‌های موجود در روایت‌ها و اظهارات مطرح‌شده، ابعاد این قتل و تلاش برای صحنه‌سازی را آشکار کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/75696" target="_blank">📅 18:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75695">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP70-OSPfypmDYj3l8NDViFG3cmI1mxOzUtq3IrYqNzHOZZXPej1RUgjCRE9uZYnqD4dAzTDP4-5O1671iy_jp8fUWlAwo9ohBrAVT5UD-U1Z6FkU-Q8RjlhZLkgW3rRnnub1Xgo4L71YCTl-rhB95ZVB5ce_qDG32RtJXqalnvSLj-eIvmcQyKktEopz_hnhDpGcxBLhK9KqENGjQQCrmrBq80RI2z6630KPw-GrMe9qaV-r9XNuDOYX1oZB3zbi5gIre2AlpZ1yhTNF5S1NRwQD_5DZneOFDwxRAxgq1Fn03z04REoG_N_nGFnGpNOT2JxDlC524S4LPt-MtmVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ایالات متحده، روز دوشنبه چهارم خرداد گفت که واشینگتن در مذاکرات جاری خود با ایران، «هر فرصتی برای موفقیت» به دیپلماسی خواهد داد.
مارکو روبیو که اکنون در هند به‌سر می‌برد در جمع خبرنگاران گفت که مذاکرات با ایران همچنان «در حال پیشرفت» است و خوش‌بینی محتاطانه‌ای نسبت به توافق احتمالی برای بازگشایی مسیرهای کلیدی کشتیرانی و از سرگیری مذاکرات هسته‌ای ابراز کرد.
او که روز گذشته از احتمال توافق با ایران تا پایان روز یک‌شنبه خبر داده بود، گفت: «همه ما باید مطمئن باشیم که یا به یک توافق خوب خواهیم رسید، یا مجبور می‌شویم به شکل دیگری با این مسئله برخورد کنیم. ترجیح ما این است که یک توافق خوب داشته باشیم.»
دونالد ترامپ، رئیس‌جمهور آمریکا نیز شامگاه یک‌شنبه در دومین پیام خود درباره روند مذاکرات با ایران اطمینان داد که توافق احتمالی با ایران «خوب و درست» خواهد بود اما هیچ کس درباره محتوای آن اطلاع ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75695" target="_blank">📅 09:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75694">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrSyREa0vJhs320fqtMJbhGG-tDoJDrbQyUTAb6jLL2YjskjL4vsRbIdnNF7mbQGftytDhX0r3sKIb8FG4t8gIghin5H8m_qT7tQRq7hMHNGsLHkx29FOjAXg83_tzoX4QUr-YOajhMn-lP_hZugLQkjJ-Q9alAo0hZxAF5-qCenMzRmWW-Rk3SjqbVmksM8Nlj2zU9GU5R7OXfCZ3fHRVaqIJxQRZrmgmbj3WAwtZ6FFvJx9uZ23f7kScwgZTlogc01P1xoRvIeR7e5PDNXMAmXy9UErzQvWz8Q3ejKzMqI6SpRYDDv5jrWMnDNZ6jmSNGBwVh_Py5JRfmKW3Zipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» رسانه قوه قضاییه جمهوری اسلامی اعلام کرد حکم اعدام «عباس اکبری فیض‌آبادی»، از متهمان پرونده اعتراضات دی‌۱۴۰۴ در شهرستان «نایین» اصفهان، صبح روز دوشنبه ۴خرداد۱۴۰۵ اجرا شده است.
«میزان» مدعی شده که عباس اکبری از «لیدرهای مسلح» اعتراضات در نایین بوده و در جریان حمله به فرمانداری این شهر و برخی مراکز حکومتی، به سوی ماموران امنیتی تیراندازی کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75694" target="_blank">📅 09:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75693">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ap01bRxQiwxEGc5b7xb-kIvCVoIbqSpUr7YpudinSDVLotK4aUc9-g-hT0y75R7uRXnL5DeFkyCO3wpP9OhE3Dqa3VauN0uY_FBkzrbO4AXIfjOtez0yKy4nWLlexAEgj707ixpI6siskGUfTePPtbfRDPMR8-OXGzm8O4eQVpP2TXUakaRPJ93_Nmr8JBk1mLGUDT5Btuu-8IM3E7zLkc46beCDoMdWgPDt2G9oLeLFErR-u2maBfS24Bxyv0dbyef1w3s2xs3AlZGkg99TyWtk3iHpfbYX7bcaOMGaPeqlfnBJ3lEBdw616msesWZWlMNtrvd15WOF3xYnoZuI3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس: مجتبی خامنه‌ای در مکانی نامعلوم با دسترسی کم به دنیای خارج پنهان شده است.
ترجمه ماشین:
اطلاعات نهادهای امنیتی آمریکا نشان می‌دهد که رهبر عالی ایران عملاً در مکانی نامعلوم پنهان شده، دسترسی محدودی به جهان خارج دارد و ارتباط با او تنها از طریق شبکه‌ای پیچیده از پیک‌ها امکان‌پذیر است؛ این را مقام‌های آمریکایی آگاه از موضوع گفته‌اند.
به گفته این منابع، مقام‌های ایرانی که مجوز همکاری با دولت ترامپ را دارند، برای برقراری ارتباط در داخل ساختار حکومتی خودشان با دشواری روبه‌رو بوده‌اند؛ مسئله‌ای که یکی از دلایل اصلی تأخیر در روشن شدن جزئیات توافق احتمالی با ایران و توافق‌های قبلی بوده است.
دو مقام آمریکایی گفتند وقتی آمریکا جزئیات پیشنهادی را ارسال می‌کند، دشواری دسترسی به رهبر عالی باعث می‌شود گاهی پیش از دریافت پاسخ از سوی آمریکا، تأخیری طولانی رخ دهد.
سخنگوی کاخ سفید از اظهارنظر درباره اطلاعات مربوط به محل حضور رهبر عالی یا روش‌های ارتباطی ایران خودداری کرد.
یک مقام ارشد دولت روز یکشنبه گفت رهبر عالی با چارچوب کلی پیش‌نویس توافق فعلی موافقت کرده و دونالد ترامپ، رئیس‌جمهوری آمریکا، در تروث‌سوشال نوشت که انتظار دارد ظرف چند روز آینده پاسخ نهایی اعلام شود.
مجتبی خامنه‌ای، رهبر عالی ایران، که در حملات آمریکا و اسرائیل در عملیات «خشم حماسی» زخمی شده بود، برای جلوگیری از حملاتی مشابه حملاتی که به کشته شدن پدرش، آیت‌الله علی خامنه‌ای، منجر شد، تدابیر بسیار شدیدی اتخاذ کرده است. علی خامنه‌ای از سال ۱۹۸۹ تا ۲۸ فوریه بر ایران حکومت می‌کرد. مجتبی خامنه‌ای از پیش از آغاز جنگ تاکنون به‌طور رسمی در انظار عمومی دیده یا شنیده نشده است.
یکی از مقام‌ها گفت اطلاعات به‌دست‌آمده توسط نهادهای اطلاعاتی آمریکا و اسرائیل از داخل حکومت ایران، امکان شناسایی و حذف بخش بزرگی از رهبری ارشد ایران در جریان جنگ را فراهم کرده است.
منابع گفتند در حال حاضر بیشتر رهبران ایران نور روز را نمی‌بینند، هفته‌ها در پناهگاه‌های به‌شدت مستحکم می‌مانند و جز در موارد کاملاً ضروری از صحبت با یکدیگر خودداری می‌کنند.
یکی از مقام‌ها گفت: «تماشای تلاش آن‌ها برای فهمیدن این‌که چطور با هم حرف بزنند، تقریباً مثل تماشای یک سیتکام است. آن‌ها کاملاً به ستوه آمده‌اند.»
شدیدترین تدابیر احتیاطی از سوی رهبر عالی اتخاذ شده است.
بر اساس طراحی این سازوکار، حتی مقام‌های عالی‌رتبه حکومت ایران هم نمی‌دانند او کجاست و هیچ راهی برای تماس مستقیم با او ندارند.
در عوض، پیام‌ها از طریق شبکه‌ای از پیک‌ها منتقل می‌شود که با هدف پنهان نگه داشتن محل حضور رهبر عالی ایجاد شده است.
یکی از مقام‌ها گفت: «به همین دلیل است که می‌بینید برخی می‌گویند: "رهبر عالی با چارچوب موافقت کرده" یا "منتظر پاسخ درباره نکات نهایی توافق هستیم." هر اطلاعاتی که به او می‌رسد، از پیش قدیمی شده و پاسخ‌های او با تأخیر زیادی همراه است.»
رهبر عالی در قالب کلیات با زیردستان خود ارتباط برقرار کرده و به آن‌ها جهت داده است که درباره چه موضوعاتی می‌توانند مذاکره کنند و چه موضوعاتی نباید مطرح شود.
cbsnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75693" target="_blank">📅 03:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75691">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FnLwDL5tTFB1E6-0Yktt-IfyF7LemT5RRQPZuLoEvvaNCU4uC2PonyIusDTOU_iQM8MRLqUhl2CmJLEwWCjQ6-zRpDR2mxoZM1k2iIDV9uRziABO09i7-1VnyeuGVwT3LPCJSa7Yl6noZTNSppWAnKLKh9zOv10pkU3DDmPyZZ9t-CYqhWKkIFIazpdujZz-j6WlXTXugsJFO0ycQOBzCWHtZflPTCeaFSeAmT5OVAmjQ_P12aWypDT4R7ssrlP9nvuEkL2WJlJ6rzxIrpSClWYUygy2090RNfP7MARKTyDzOEXFb-uHJ4Fja60QolEVfAuk8SoSUTN3UAuRSoo46g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/trOJ4_HmQ72mAFHlSJvEZEQF_RIC5Ny6r4V-wDn5kftRJO7n9PbP2cEpS4fDKI258k6MnL0mZdf7ZNo2sWO5rZqr7lgupwHlrwKXwoX0kgf8TK5R9ggB4RE2QFOLdm168Xe37KzIM35i0GDZeey0bXrZZj5dY9HyTWb7-yRH6aswQPReD3aikNG6IihTrx0rxWaLUF15xn8h301RaFnrz2_O5pZNDTR0ytbOyuYttCIG1ylpL_0qsupIbhnwWpu7ta0c1mkEe25nSPsku9mOWh-WfXxRoCPBLpDlBiXclrlUTzTmHqaLHWtn0HQ6yG7VNvp26_0B1Iar0crulKtN9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با شبکه «فاکس‌نیوز» اعلام کرد که واشنگتن هنوز به توافق نهایی با تهران دست نیافته است و هیچ توافقی امروز یا فردا امضا نخواهد شد؛ این مقام مسئول با تاکید بر این‌که آمریکا تسلیم خواسته‌های طرف مقابل نخواهد شد، افزود که تمایل و تصمیم دونالد ترامپ، رئیس‌جمهوری آمریکا، این است که یک فرصت ۵ تا ۷ روزه دیگر به مذاکره‌کنندگان بدهد تا توافق را به مرحله نهایی برسانند.
بر اساس این گزارش، یک توافق چارچوبی با ایران تا روز یکشنبه تا ۹۵ درصد پیشرفت داشته است و اگرچه دو طرف بر سر کلیات مربوط به ذخایر هسته‌ای تهران و بازگشایی تنگه هرمز به توافق رسیده‌اند، اما چانه‌زنی مذاکره‌کنندگان بر سر جزئیات و «ادبیات دقیق» متن این تفاهم‌نامه همچنان ادامه دارد.
@
VahidOOnLine
تسنیم، خبرگزاری وابسته به سپاه پاسداران، روز یکشنبه به نقل از «یک مقام مطلع» گزارش داد: «هیچگونه خوش‌بینی به آمریکا ندارد و رد و بدل پیامها از طریق میانجی پاکستانی نیز دائماً با در نظر گرفتن بدبینی به دولت آمریکا صورت می‌گیرد».
تسنیم به نقل از این منبع در ادامه نوشت: «تا این لحظه تفاهم نهایی حاصل نشده و چالش در بعضی بندها ادامه دارد، اما حتی اگر تفاهم اولیه‌ای نیز صورت بگیرد، به معنای تغییر نگاه ایران به آمریکا و اطمینان از اجرای تعهدات این دولت نیست. آمریکایی‌ها سابقه بسیار بدی در مذاکرات دارند که بدبینی ها را تقویت و تثبیت می‌کند. پس حتی اگر تفاهمی نیز صورت بگیرد ایران در طول روند پس از اعلام تفاهم، اقدامات آمریکا را زیر نظر خواهد گرفت و در صورتی که آمریکا در آن مرحله نقض عهد کند، ایران اهرم‌های خود برای مواجهه با آن را حفظ خواهد کرد».
تسنیم پیش از این نیز از «کارشکنی‌های آمریکا» در بندهای تفاهم از جمله در آزادسازی اموال بلوکه شده ایران گزارش داده و نوشته بود: «همچنان امکان منتفی شدن تفاهم وجود دارد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/75691" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75690">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KtLN-yk9glogJqje1VAOnU57tlMdVmd0bhA8klSqnALzxFjc5scb8Xde6qnZv17nJVOx4nugXQWc1KAN13_bWpxxcUP6BrE5jN2fYyE1XqC-JtDodKXz5FjJQNorcL02DnPw-c0cQWOj3HQIVCNDhswARq9zCAqnzo5Qm5nySU_6Ddg8XA6tPIkqgCXcp5K0cSj8a4JuGZqyeR2ggypddkY6NLeVO1ukb36icH5Z2oWldE2JQmiFuiULpRWhtOL7j_26w1ektIopka75sjTVoODMgOGiyBj2YYvWdFLJRK01q-9c-pQD9Yv-Nj8kcxgQzJWqemFiX1avjy_hHcaryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری حکومتی تسنیم، شامگاه یکشنبه سوم خرداد ماه، به نقل از دادگاه انقلاب تهران اعلام کرد، رای اولیه پرونده موسوم به «بچه‌های اکباتان» صادر شده و طی آن چهار نفر از «متهمان اصلی» به اتهام «افساد فی‌الارض» به اعدام محکوم شده‌اند.
به گزارش تسنیم،  اتهامات ۹ نفر از متهمان این پرونده که به دلیل کشته شدن «آرمان علی‌وردی» بسیجی حامی حکومت زندانی شده‌اند مواردی چون  «وارد کردن ضربات چاقو،اخلال در نظم عمومی، اخلال گسترده در امنیت کشور، اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی کشور، توزیع کوکتل مولوتف، وارد کردن ضربات سنگ به آرمان علی وردی، ضرب و شتم آرمان علی‌وردی و فعالیت تبلیغی علیه نظام» عنوان شده است.
بر اساس این گزارش، دادگاه انقلاب تهران متهمان ردیف اول تا چهارم پرونده را به اتهام «افساد فی‌الارض» به اعدام محکوم کرد و متهمان ردیف پنجم تا نهم نیز به حبس از یک تا پنج سال و مجازات‌های تکمیلی محکوم شدند.
@
VahidOOnLine
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی چهار تن از متهمان پرونده «شهرک اکباتان» را به اتهام «افسادفی‌الارض» به اعدام محکوم کرد؛ این در حالی است که دادگاه کیفری پیش‌تر اعلام کرده بود انتساب قتل به متهمان به‌صورت قطعی ثابت نشده و امکان صدور حکم قصاص وجود ندارد.
خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، روز یکشنبه در گزارشی تلاش کرد صدور این حکم را توجیه کند.
بر اساس این گزارش، رسیدگی به پرونده در دو مرجع موازی انجام شده؛ دادگاه کیفری به اتهام قتل رسیدگی کرد و دادگاه انقلاب به اتهامات امنیتی از جمله افساد فی‌الارض.
میزان مدعی شد که پس از آن‌که کمیسیون پزشکی قانونی و اداره آگاهی هر دو اعلام کردند تعیین فرد وارد کننده ضربه مرگبار به آرمان علی‌وردی ممکن نیست، دادگاه کیفری سه تن از متهمان را از اتهام مشارکت در قتل تبرئه و سه تن دیگر را به پرداخت دیه و حبس محکوم کرد. اما در مسیر موازی، دادگاه انقلاب همان متهمان را به اتهام افساد فی‌الارض به اعدام محکوم کرد.
به گزارش خبرگزاری هرانا، میلاد آرمون، نوید نجاران، مهدی ایمانی و سید محمدمهدی حسینی چهار نفری هستند که حکم اعدام برای آن‌ها صادر شده است.
چهار متهم دیگر این پرونده یعنی امیرمحمد خوش‌اقبال، علیرضا برمرزپورناک، علیرضا کفایی و حسین نعمتی نیز هر کدام به پنج سال زندان، دو سال حبس به اتهام تبلیغ علیه نظام، دو سال منع فعالیت در فضای مجازی و دو سال منع اسکان در تهران و البرز محکوم شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75690" target="_blank">📅 00:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75689">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lV73tSPBrLglcet_Te5atxjcqlD5hNWjeQMWSDFRMoDnXDXUeQjYn2ShrpUZITqEcpVP5Ls6xwqk5uU7fwgJFn3gjo51TjW-a3WCbp8zhjiLPKeex5ZESCBQacnm4DqUGf0W2xKqKJZJALsdocbXszIDiWgzAzdpr_Tr__24GejSZmfZsR3_ZmN_i8dUrwKMVzDVrAq0oJJ_a-Te26AxjAyJfCoC2hA8DZ_CfNOZAOGrYvWxrtAVDheTlTlouj9IESs_8dlURAOnboy9ojEIQmn5PiKcdOZ6Ip-rSGz5xmyHfhalFIWw-muVNXUdEP6R85qEOC8IcCMTv3NJs21dgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ
روی تصویر بمب نوشته: از توجه شما به این موضوع سپاسگزارم.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75689" target="_blank">📅 23:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75688">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ail-u0AxtOJDiIlkcnf_yaNHopJz7BZo4s-lcCDigGUexXIAY7OiTlx3zF82r8KewBE1163RrMv41H_eFVAe3aBcgiFTSrz72dYddNkjuQQzhSCmQTyASGZmVdfpEYhpsPOkI8ESFMMrqIOXsMMyk2M7Q2ZJklwBTqQPnOWn0yGeZdHBFxrPV2B0_JUy2GOIjQMq7luOaPrMPTt2dEEM9Tw8nmX0iZswyNcB5nmMwOQHeCgJHP1yy2FNzdAo6MBGLCoRCpVxC7c2XZQGTkEcy8A2WUZpITcGHhYmBOYNfPH60JtkOGn8KgTmH27ZknkN9rwMYWs8QExz3lS452dQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در گفت‌وگویی کوتاه با نیویورک تایمز گفت: «ما موضوع را به بعد موکول نمی‌کنیم. مذاکرات هسته‌ای مسائل بسیار فنی هستند. شما نمی‌توانید یک موضوع هسته‌ای را در ۷۲ ساعت و روی یک دستمال کاغذی حل کنید.»
او افزود: «در حال حاضر، هفت یا هشت کشور منطقه از این رویکرد حمایت می‌کنند و ما آماده‌ایم این مسیر را ادامه دهیم.»
این در حالی است که آقای روبیو ساعاتی پیش گفته بود که ممکن است تا شامگاه یک‌شنبه خبری دربارهٔ توافقی با ایران اعلام شود که می‌تواند به‌طور رسمی به جنگ خاورمیانه پایان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75688" target="_blank">📅 22:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75687">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BnnHy8dO0WOif3vFV-LA-sOiOpVkRtKIEr2sZM-cabzJAeF4cONfKq3UQ98JYYwaRQR12bmdyo1RJ8I65nuhI9_A88TgxTrrV9Jvunis1HOnJMSX2jFwo9EgkG_NnA6oA3jqY-JmTNPv9zryw24cniIIgy9ziaaO560Gr5YP7GZ0_tQbWamOXBxPGmkY08HpsjO-fS9DBCvnH5Haw7MtBMyhI-oC0rhxI92QbGNMAe9vFEpFAjSan4fZCtOYaLi_bD_9iODArhg0R9QL7wap0fl80TTeUKpy3KVFmd98i5_T57T9atW-EfFsapJZMKWXyC4E2p09_SGNBna6ScTuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر توافق کنم توافقی خوب خواهد بود
ترجمه ماشین:
اگر با ایران توافقی انجام بدهم، توافقی خوب و درست خواهد بود؛ نه مثل توافقی که اوباما انجام داد و مبالغ عظیمی پول نقد به ایران داد و مسیری روشن و باز به سوی سلاح هسته‌ای پیش پای ایران گذاشت.
توافق ما دقیقا برعکس آن است، اما هیچ‌کس آن را ندیده و نمی‌داند چیست.
حتی هنوز به‌طور کامل هم مذاکره و نهایی نشده است.
بنابراین به بازنده‌هایی که درباره چیزی انتقاد می‌کنند که هیچ اطلاعی از آن ندارند گوش نکنید.
برخلاف کسانی که پیش از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بد انجام نمی‌دهم!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75687" target="_blank">📅 22:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75686">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF60HmZFA5fC--m_ZB4kx_-wMBhH7fAyPFMht-7RORKnyMl3vdLAys5KMV05oAbVEQcRJEFvKfIx63Vqu3UgB_KMvz8TShOyO1J2YXic693y3nB0tYvcG_7ahm7cji_tYQ0OecfwQKrHt6w8u3b7r3UzNCtS1nUQ6DNWihU9Ci778istLn8kZ3ZfbolK6CusV1quUrlG0mFhwVtx1oRCHQFHKqVl8QiLjBZ5Ui7Tlh7zdajp4dWXcYx6ALEtCP8ONtCcp3kT4W0Az-qk9T5_tJGUnFLuA8H-kk8iKwtkKZNPYfDaF2jnZLVfcvHcqmHxaTqi82wsEXjo-IYJUkHTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه آکسیوس، روز یکشنبه سوم خرداد ماه، به نقل از یک مقام ارشد دولت دونالد ترامپ گزارش داد، «چند مورد جزئیات حل‌نشده» میان تهران و واشنگتن باقی‌مانده است و به همین دلیل توافق میان ایران و آمریکا احتمالا امروز امضا نخواهد شد.
این مقام آمریکایی به آکسیوس گفت هنوز بر سر برخی بخش‌های توافق «رفت‌وبرگشت» وجود دارد و اختلاف‌ها بیشتر بر سر عباراتی است که برای هر یک از دو طرف اهمیت دارد: «برخی کلمات برای ما مهم هستند و برخی کلمات برای آن‌ها.»
آکسیوس به نقل از این مقام ارشد کاخ سفید نوشت، ساختار تصمیم‌گیری در جمهوری اسلامی «سریع عمل نمی‌کند» و روند دریافت همه تاییدیه‌های لازم چند روز زمان خواهد برد.
به گفته این مقام، ارزیابی واشنگتن این است که «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، چارچوب کلی توافق را تایید کرده، اما اینکه این روند به توافق نهایی منجر شود، «همچنان یک سوال باز» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75686" target="_blank">📅 18:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75685">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnvRkX9HpcWlbCyyUwdl8xosleg2vv6DPAUmEvuQPQG9kUxePhCh2JSOVgNVu3SkR7MoBdUjOlePNc5oOvtBsR_TPwwzwqr5KXO4P1v09NEHV3OkrLZO-a18MrOeWKFu518zG0KXYDstcMMtZTQSbTqZ3ALopYiceEMx_6NMDQWhtSCXwWYNBbDRjMevTcqAbfkJb_ZpD_VXxD7W7OICWgpYmkYxguH5aoG51nWT2HD54alQ1xV4jZHlQdxgFH9TuoaJ3MezvrG-JkXBnsWPZOyDHznZgRJVbzWqIBJsHTsne-BABrJQ1sN7y4QAjwtmHZpO0g8Zi1y3H-fnthKb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد او و دونالد ترامپ توافق دارند هرگونه توافق نهایی با جمهوری اسلامی باید به‌طور کامل تهدید هسته‌ای را برطرف کند.
او گفت این به معنای برچیدن تاسیسات غنی‌سازی ایران و خارج کردن مواد هسته‌ای غنی‌شده از خاک این کشور است.
نتانیاهو افزود ترامپ بار دیگر بر حق اسرائیل برای دفاع از خود در برابر تهدیدها در همه جبهه‌ها، از جمله لبنان، تاکید کرده است.
او همچنین گفت سیاست او، همانند سیاست ترامپ، همچنان ثابت است؛ ایران نباید به سلاح هسته‌ای دست یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/75685" target="_blank">📅 18:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75684">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DpoHYo0q0hy6HEJjFpde-I5VCytJmeYzGycDl55fKQCetBq9Uo3nKKsM36oi3A5WpCLbcgV0yEdz2sYEqnDV6MZ-49KI2AWFsvMlx-9ZCgZdnRkshakkNqQ_OhsnAkdUAHSvh_kOBQqT_CQGz6fAtZPDthq0pjAUAGp1Klrvb-bxVnHWco1_sq0gw6NGzW9gh2QCfMVY7qREo6NdV2oxBkqomCfsgDPxNN-V1Lx8ZaPNJZHCIBxgb9FOxw2t_tGEliAPCo5woD3IbxHUyftDx44ehMuYQ0RUE40ZTQgW4DuZEHQ-fdqypqYLKTIBkfqiVjd2iGJBowZu9S-jy7bRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ سخنان پزشکیان را نشان داد: آماده‌ایم به جهان اطمینان بدهیم
ترامپ اسکرین‌شاتی از
توییت
خبرنگار فاکس‌نیوز رو پست کرده که نوشته بود:
مسعود پزشکیان، رئیس‌جمهور ایران: ما آماده‌ایم به جهان اطمینان بدهیم که به‌دنبال سلاح هسته‌ای نیستیم. ما به‌دنبال بی‌ثباتی در منطقه نیستیم.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75684" target="_blank">📅 18:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vr64DAqpDFN1arXYcGd9k9sUCE-lMmMShLg__GzUOYfHgpvpzHwcDH2Dg0baw6SUo9HTcRFnmwrcdcuy5S7gJLpvmib-QKyh3RJYEb7L3R1modJF0Gvm-Jrgpr6mCaiyIEeGPP5MK0BLm5jkL94lGkmjLDtnVA8Z6EQFq4_LH7_Pud5SH6C4HrefPN_-iM7PT6kmtQ2GPO1zCAINHBYj4Fx7j8et1UJtBiurikA_mhw_ZukkPJ7kibEXeERNBMdOX8xA-9uQ348bAtSgFikmY2pXaZyahlvVr9WChU9YCK3EWZXGqTD0Zcx1scs0OC-UlS8WBi8Sx7DrSQXFUg9fuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
یکی از بدترین توافق‌هایی که کشور ما تاکنون انجام داده، توافق هسته‌ای ایران بود؛ توافقی که باراک حسین اوباما و افراد کاملاً ناشیِ دولت اوباما آن را مطرح کردند و به امضا رساندند. این توافق، مسیری مستقیم برای دستیابی ایران به سلاح هسته‌ای بود. اما درباره معامله‌ای که اکنون دولت ترامپ با ایران در حال مذاکره بر سر آن است، چنین نیست؛ در واقع کاملاً برعکس است!
مذاکرات به شکلی منظم و سازنده در حال پیشرفت است و من به نمایندگانم اطلاع داده‌ام که برای رسیدن به توافق عجله نکنند، زیرا زمان به سود ماست. محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، با تمام قدرت برقرار خواهد ماند. هر دو طرف باید وقت بگذارند و کار را درست انجام دهند. هیچ اشتباهی نباید رخ دهد!
رابطه ما با ایران در حال تبدیل شدن به رابطه‌ای بسیار حرفه‌ای‌تر و ثمربخش‌تر است. با این حال، آنها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای تولید یا تهیه کنند. مایلم تا این مرحله از همه کشورهای خاورمیانه بابت حمایت و همکاری‌شان تشکر کنم؛ حمایتی که با پیوستن آنها به کشورهای عضو توافق‌های تاریخی ابراهیم، بیش از پیش تقویت و گسترش خواهد یافت و چه کسی می‌داند، شاید جمهوری اسلامی ایران هم بخواهد به آن بپیوندد!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/75683" target="_blank">📅 18:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NzsrlkoaqbFmnF4FtJ5T9C9jnBVoiQzwgEUk6SzRP4Reyr8gP1kZZ7j_QGZTGAg6fsWIynQAOv8yze_HyCab3APTqpuooN9FlKqxur91AlTMVsjvk6fHc8jmfOdDkiXdVNzEfmnajsF-S01XIa_wAM0xmrc6boZcOL7fA2wq7g7ONA5O2hF-pz_PGuxBTc0UWBEjyMMdHlPEXyotGw5CZoMyzCHXmL8cUZnMFvc63bUlr2xw5ZsNAyiKrrOpt-dKJgKIVVaOLGmaDxG1-Q9FBlZQ5a3VkQlBqt_4u4slj9JBd6u7SMSlTVulwFgniVlpIG7dq2HXk15FymQMipJ99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته با هوش مصنوعی را در شبکه اجتماعی تروث سوشال
منتشر کرد
که انهدام یک قایق سپاه پاسداران  به دست پهپاد آمریکایی را نشان می‌دهد.
بر این تصویر، واژه «حداحافظ» به زبان اسپانیایی نوشته شده است.
این تصویر در حالی توسط رئیس جمهوری آمریکا منتشر می‌شود که رسانه‌ها در انتظار نهایی شدن توافق احتمالی تهران و واشنگتن برای پایان جنگ هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/75682" target="_blank">📅 18:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Njks4_QX0vQyPGoWFI1zAWlW7MmRgRrbyIGXqd0ffAFFeDwAI7i3AlQWejnDRuwS-mvzTqOZrw5tbms3SC117VOaafK2GP088EypUP6qo_CXVTdTHMYz1LUPFn31SmxwzNtzyoUopKU9XrQoOqOrQm8qlCSZhzX8ES-knPY5qSHH1Irjmshqa7_IXoAUsEdR7Ey7pckhD2jrOnt7sb126r2tlg9m_z4l7F9ZIdLbGRsTCJ48DNUjspoxK3SPDNSISUQ_GVL9OovOTx6wiO9P_RZSHPPM0ToDUc9nsiEmGkYPeMhPTgo_FvXVm3vA0scAawQzgvo4LzdpX5wNlxfdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول پزشکیان گفت: «مدیران دولت تا زمانی که مباحث کارشناسی درباره مدیریت مصرف بنزین نهایی نشده است، حق اظهارنظر شخصی ندارند.»
او افزود: «اگر کسی از این دستور تخطی کند با او برخورد می‌شود، زیرا ابتدا باید نظرات کارشناسی بررسی و سپس جمع‌بندی نهایی حاصل شود.»
او ادامه داد: «مسئولان تا پیش از آن حق ندارند اظهارنظر شخصی کنند، چرا که نباید در جامعه التهاب یا نگرانی ایجاد شود.»
@
VahidOOnLine
این دستور در شرایطی صادر شده که شایعات درباره افزایش قیمت بنزین، تغییر سهمیه‌ها و تشدید سیاست‌های مدیریت مصرف بالا گرفته است.
همزمان، ناترازی بنزین و فاصله میان مصرف داخلی و توان تأمین سوخت، نگرانی‌ها درباره کمبود احتمالی یا فشار بیشتر بر شبکه توزیع را افزایش داده است.
عارف گفت دولت تلاش می‌کند تصمیم‌ها به‌گونه‌ای اتخاذ شود که معیشت مردم آسیب نبیند، اما واقعیات اقتصادی کشور و تحولات اخیر نیز باید در نظر گرفته شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75681" target="_blank">📅 18:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75679">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p0Uv_GL5FveuJQI-Gm02NThpVbRs1fCmc1fb39ynaUGVJBXQ4-eSQftll86xOnwn-JlaW-pe-LQFzClxoIzya_HdV7mS1SLCzDfCqlvjE7DVk8Lg1o5OXiY3Qc-LRVuha6qbCh16pxasNr40DOrcx2Mv4FuSWuqqNg--fxjeoooSABrdjYC_uRQzRK1j7asbC9wCwL_RGSPuVr3M5Vmol0vwdlc9-bfd6r7uHjdaXjyu3vw6Y4fUfMCzASMGr-5g4d4E3xVHWvNvMIddM7zhXCJ5idVn2lsH5_VYoLpEDGbpsxkxVrL7AHqsVcafdqJu8QVtmifE37egkuGZ06sgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dUownm0yl4Bls0Ds7aPYDEjCqtgmKj129nm6dkpHsRpXDN3nmfZRe2OAsxnbZahUqhYX89vZEOpB12_gVqBMhUy4fJNQn5KfdWOzUbIbKt621eOOGeZiGn7lIPYSQnLy6t2bQ9l-xM6JGqURey9Od_Z0ZaMzeJVldCFjy7b0Hy6cgf5jLLpMvrWblmIEm60RRsIxdaCsyXJPOSGw9dXlb_luC1XGxm2JeYMJQ4Y7RFMbovrSDkemfD3ZwlTrxfsqDhMnONpI1o-bSu2oi0B5HWq9hc4EqviEGN4hX-IkFZpQRn_l4m_j7P_O7c8CCs-SEGr1p4eL6f7PsUM0jGvlEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران روز یکشنبه سوم خرداد با اشاره به توافق احتمالی میان جمهوری اسلامی و آمریکا، نوشت:  در پیش‌نویس توافق احتمالی ایران و آمریکا هیچ بندی درباره «تعهدات هسته‌ای ایران گنجانده نشده و تمام مسائل مرتبط با برنامه هسته‌ای به مذاکرات ۶۰ روزه پس‌از امضای توافق موکول شده است.»
فارس در ادامه تاکید کرده است که «ایران در این توافق هیچ تعهدی برای واگذاری ذخایر هسته‌ای، خروج تجهیزات، تعطیلی تأسیسات یا حتی تعهد به نساختن بمب هسته‌ای وجود ندارد.»
این در حالیست که نیویورک تایمز به نقل از دو مقام آمریکایی گزارش داد، یکی از عناصر کلیدی توافق پیشنهادی میان واشنگتن و تهران، تعهد آشکار ایران به واگذاری ذخایر اورانیوم با غنی‌سازی بالای خود است.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت که شنیده‌ها از جزییات تفاهم اولیه «احتمالی»، حاکی است که واشینگتن متعهد خواهد شد در طول دوره مذاکرات، تحریم‌های نفتی ایران را به حالت اسقاط درآورد و جمهوری اسلامی در مقطع کنونی هیچ اقدامی را در حوزه هسته‌ای نپذیرفته است.
این گزارش افزود در صورتی که این تفاهم‌نامه مورد توافق قرار گیرد، بخشی از دارایی‌های بلوکه شده حکومت ایران باید در گام اول آزاد شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/75679" target="_blank">📅 18:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75676">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O29rkIIvJNAFPlIL65V3UCmZpNI03M2YY0bKj_Av3K8gLEPGLh-RMTbl6_8b6Cn9ntpfN2bjPyYVnIQ-P6StAXhNg3Rko2nvipuOeJTVnJo499LD3ZM-Mcie05oqiPVjsFou8OSq5er_vwiLLHr6b70i9L1u-SZx8TIfxEVZOsbF9SktENQWZO2CtugVsM_dqALRV_8IFxlwriEJ6z5V6VcZNzTI5qa502a_46qXjVsCnvoOK4nS74kVILZOVtpIGNhrHSAEqL4fyoPHrGsnBWITejfHPUfueDhq7-gMLChoK5Gba_vU8XNYve4IRZhQuXo8PVoTI_7IWultbD7rsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af3f5ad4b2.mp4?token=I4NQp81QzGjvg4iFpJfvHt7cqqzWo_iyI7azb5T-ZwOjuem94NF--J6bueqAfCHGFEVeD4p4oPFM2kukbfPWTOh_RDD0xD_Brus2lAY2SVqh081T3CXVzmNLE1YchihfjXPDye1i8-06JJucwGaGuNONx94j1T_afsgmen8fdPT0YeN8Y0t7ly8nQ117U_JOYtwu_pM3rOeB2Zf4UBt2FVEj2xcl3JyZXap1W0PHjTC_4s39cvIyNKIB0EDrxz26egcLyNwo2qjjJKr7V0choIye1JXZW5qDkDwdX-bUWsHwkgYom0GOfK_yMZ-_yfUA6nK6FWBW2PnbgJWPnqkKBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af3f5ad4b2.mp4?token=I4NQp81QzGjvg4iFpJfvHt7cqqzWo_iyI7azb5T-ZwOjuem94NF--J6bueqAfCHGFEVeD4p4oPFM2kukbfPWTOh_RDD0xD_Brus2lAY2SVqh081T3CXVzmNLE1YchihfjXPDye1i8-06JJucwGaGuNONx94j1T_afsgmen8fdPT0YeN8Y0t7ly8nQ117U_JOYtwu_pM3rOeB2Zf4UBt2FVEj2xcl3JyZXap1W0PHjTC_4s39cvIyNKIB0EDrxz26egcLyNwo2qjjJKr7V0choIye1JXZW5qDkDwdX-bUWsHwkgYom0GOfK_yMZ-_yfUA6nK6FWBW2PnbgJWPnqkKBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز یکشنبه در جریان نشست خبری مشترک با سابرامانیام جایشانکار، وزیر خارجه هند، در دهلی‌نو اعلام کرد که طی ۴۸ ساعت گذشته «پیشرفت قابل‌توجهی» در مذاکرات و رایزنی‌های مرتبط با بحران تنگه هرمز و پرونده ایران حاصل شده و احتمال دارد تا ساعاتی دیگر اخبار مهم‌تری در این زمینه منتشر شود.
او بدون ارائه جزئیات کامل، گفت هنوز توافق نهایی شکل نگرفته اما مسیر مذاکرات نسبت به روزهای گذشته امیدوارکننده‌تر شده است.
روبیو با تاکید بر اینکه دولت آمریکا همچنان راه‌حل دیپلماتیک را ترجیح می‌دهد، اظهار داشت دونالد ترامپ تمایل دارد بحران ایران از طریق وزارت خارجه و مذاکره حل شود، نه از مسیر درگیری نظامی.
با این حال او هشدار داد که واشنگتن در هر شرایطی مانع دستیابی ایران به سلاح هسته‌ای خواهد شد و این موضوع «خط قرمز» دولت آمریکاست.
به گفته او، رئیس‌جمهوری آمریکا بارها تاکید کرده که ایران هرگز نباید به توانایی ساخت سلاح هسته‌ای برسد و دولت ترامپ در این زمینه از همه دولت‌های پیشین آمریکا سخت‌گیرتر عمل کرده است.
وزیر خارجه آمریکا در بخش دیگری از سخنانش به وضعیت تنگه هرمز پرداخت و گفت این آبراه، یک مسیر بین‌المللی است و هیچ کشوری حق ندارد عبور و مرور آزاد کشتی‌های تجاری را تهدید کند. او اقدامات اخیر ایران در قبال کشتی‌های عبوری را مغایر قوانین بین‌المللی دانست و هشدار داد اگر جامعه جهانی در برابر چنین اقداماتی سکوت کند، یک «وضعیت خطرناک و غیرقابل‌قبول» به رویه‌ای عادی در جهان تبدیل خواهد شد، موضوعی که می‌تواند در مناطق دیگر دنیا نیز تکرار شود.
روبیو همچنین اعلام کرد آمریکا طی دو روز گذشته همراه با شرکای خود در منطقه خلیج فارس روی چارچوبی کار کرده که هدف آن باز نگه داشتن کامل تنگه هرمز، جلوگیری از اخذ عوارض یا محدودیت برای عبور کشتی‌ها و همچنین رسیدگی به نگرانی‌های مرتبط با برنامه هسته‌ای ایران است.
او توضیح داد که در صورت موفقیت این روند، نه‌تنها امنیت کشتیرانی و تجارت جهانی حفظ خواهد شد، بلکه نگرانی‌ها درباره برنامه هسته‌ای ایران نیز تا حد زیادی کاهش پیدا می‌کند.
روبیو در ادامه گفت هرگونه توافق احتمالی نیازمند پذیرش کامل ایران و اجرای عملی تعهدات خواهد بود و مذاکرات درباره جزئیات فنی برنامه هسته‌ای، روندی پیچیده و زمان‌بر دارد.
او افزود هنوز نمی‌توان درباره موفقیت نهایی مذاکرات با قطعیت صحبت کرد، اما «نشانه‌هایی از پیشرفت واقعی» دیده می‌شود و ممکن است جهان در ساعات آینده خبرهای مثبتی درباره تنگه هرمز و روند مذاکرات دریافت کند.
@
VahidOOnLine
روبیو گفت: «هدف نهایی این است که ایران هرگز نتواند به سلاح هسته‌ای دست یابد. ایران هرگز نباید مالک سلاح هسته‌ای شود.»
او تاکید کرد دونالد ترامپ، رئیس‌جمهوری آمریکا، در این زمینه موضعی «کاملا روشن» داشته و گفته است ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
وزیر خارجه آمریکا افزود: «قطعا تا زمانی که دونالد ترامپ رئیس‌جمهور است، این اتفاق نخواهد افتاد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75676" target="_blank">📅 18:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uFB8P_2KYIi73LfFnDYLnsapEOhgjajRlpWV9StXCcSkZW668GdJj0LZOFuPGfp0NIv7mePGaL_Y44BG5QJ9rgS1l4F0t5h04smpGUVy7-RmrKpGBwAibyhy1DU_b8cQV7uleIJXPsgmA6m51KbgEz_VnHBi6jdmQDToDPjXWbWHJuFRrLHmN7V14J2CnD6zj9g2cB7oFc3SrovMJufy9aVKzlNuz4At4jKuV-lCJXHCCPC-m0ghh89yAwkFB6Gs9sJANFihiN-KNL8gCRLxkk51Y4o6rUIe81ezRS21_6TJx9ECgKodsEnAsuG8h2Or9ihsmg6BmkdtKqy-efDJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد سرافراز، رئیس پیشین سازمان صداوسیما و عضو کنونی شورای عالی فضای مجازی، می‌گوید بخشی از حاکمیت ایران با الهام از الگوی چین به‌دنبال محدود کردن اینترنت جهانی برای عموم مردم و ارائهٔ آن فقط به گروهی خاص و کنترل‌شده است.
او روز یک‌شنبه سوم خرداد در گفت‌وگو با روزنامه اینترنتی فراز گفت جمهوری اسلامی تجهیزات لازم برای «قطع دائمی اینترنت» را از چین خریداری و وارد کرده است.
محمد سرافراز توضیح داد که در چین اینترنت جهانی برای عموم مردم قطع است و فقط به‌صورت محدود در اختیار گروه‌هایی خاص قرار می‌گیرد. سرافراز با اشاره به الگویی که آن را «سامانه نیکان» در چین خواند، گفت هدف چنین سازوکاری این است که «روایت حکومت» بر کشور حاکم باشد.
او همچنین اپراتورهای عضو شورای عالی فضای مجازی را از عوامل پشت پردهٔ تصویب طرح موسوم به «اینترنت پرو» دانست و گفت ذی‌نفعان قطع اینترنت «یک روز فیلترشکن می‌فروشند و یک روز اینترنت پرو».
@
VahidHeadline
پس از ۲۰۴۰ ساعت قطعی اینترنت در ایران، نت‌بلاکس نوشت در حالی که دسترسی به اینترنت جهانی در طول مذاکرات صلح تا حد زیادی قطع است، کاربران منتخب در لیست سفید، تصویری مصنوعی از زندگی ایرانیان را به جهان خارج ارائه می‌دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/75675" target="_blank">📅 17:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75674">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9232e36d77.mp4?token=iaStzgxslD9boPo-DYtvUWUfpVDUmq8VxMqJMOVet7QOezWrOuA03pF8QPfCUwaGonpjQKWsCbniTHFKNRjzXuI8JyRZjjApXgWMJSuGkTiW7CmjQdZlgX3Aygsk_2XdgxT7Z8hskdbe_C8tsKdoWwLwFIl9RLrXwrRvH8UbQj_qkPOLe9g2PxDNeV7OlF6Vx87DRLPFUO7_a9fwrZ3QuUHSbqh2J5ww7BvyrNBtQCSWlG6gu0eNJL3sRDzPLb5ucqfv-YCi3QrKp34qgLqRc1_BO0D99wEchePMG7EGlqBx3F2kNlOFN5XEWeSDrTDKSm8hlFkPM3Kl_BeNxBe8Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9232e36d77.mp4?token=iaStzgxslD9boPo-DYtvUWUfpVDUmq8VxMqJMOVet7QOezWrOuA03pF8QPfCUwaGonpjQKWsCbniTHFKNRjzXuI8JyRZjjApXgWMJSuGkTiW7CmjQdZlgX3Aygsk_2XdgxT7Z8hskdbe_C8tsKdoWwLwFIl9RLrXwrRvH8UbQj_qkPOLe9g2PxDNeV7OlF6Vx87DRLPFUO7_a9fwrZ3QuUHSbqh2J5ww7BvyrNBtQCSWlG6gu0eNJL3sRDzPLb5ucqfv-YCi3QrKp34qgLqRc1_BO0D99wEchePMG7EGlqBx3F2kNlOFN5XEWeSDrTDKSm8hlFkPM3Kl_BeNxBe8Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجاری بزرگ در نزدیکی یک قطار که از گذرگاه چمن در شهر کویته در ایالت بلوچستان پاکستان عبور می‌کرد، تعداد زیادی کشته و ده‌ها نفر زخمی برجا گذاشت.
یک مقام ارشد پلیس بلوچستان و یکی از مسئولان این ایالت به محمد کاظم، خبرنگار بی‌بی‌سی اردو، گفت تاکنون کشته شدن ۲۰ نفر در این انفجار تأیید شده و دست‌کم ۷۰ نفر زخمی شده‌اند.
تصاویر منتشرشده پس از حادثه نشان می‌دهد که چندین خودرو در نزدیکی خط آهن آتش‌ گرفته‌اند و واگن‌های قطار نیز روی ریل واژگون شده‌اند.
گروه جدایی‌طلب «ارتش آزادیبخش بلوچ» مسئولیت این حمله را به عهده گرفته‌ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/VahidOnline/75674" target="_blank">📅 17:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KeuZMAEDs2hjbH1fSLbCE40-JhoHdsX2Y8XNWjP_BOWHuw-9M-04BdeocOwGQLl8H2ublEYSPJaKJebC9T9RdQxVYbLHQI1FyBT39E6CHjnHTp47I5mD0OgKLQwE-O2EKYVmYuY7maJDkQeaWTVkcNd2BYfosGSkY73HFJ3rK9c_ruzEvnn0uHliKU7ce5RMFbzmwtDm4VEymC5l8f8J0llBbH2mdDeemtxDeOWRxEdU4sRBYq_WTi2ushEGIZ1BCZ83x6CGBoHgL_wNFmKXwzh30DCtyNbhQOH8hus8aIwOXwB0L4BprPgu8vQ8JRTddPTHvKbaboMaHf2urvQejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضائیه جمهوری اسلامی، اعلام کرد مجتبی کیان به اتهام ارسال اطلاعات مراکز تولید صنایع دفاعی به «دشمن آمریکایی ـ صهیونیستی» اعدام شده است.
قوه قضائیه مدعی شده کیان در جریان آنچه مقام‌های جمهوری اسلامی «جنگ رمضان» می‌نامند، اطلاعات و مختصات واحدهای مرتبط با تولید قطعات صنایع دفاعی را از طریق پیام به شبکه‌های وابسته به اسرائیل و آمریکا ارسال کرده بود.
میزان مدعی شده بررسی‌های فنی نشان داده سه روز پس از ارسال این اطلاعات، محل مورد اشاره هدف حمله قرار گرفته و به‌طور کامل تخریب شده است. قوه قضائیه گفته پرونده این متهم در دادگستری استان البرز رسیدگی شد و حکم او پس از تأیید دیوان عالی کشور اجرا شد.
بر اساس رأی دادگاه، مجتبی کیان به اعدام و مصادره کلیه اموال محکوم شده بود. میزان همچنین نوشت از زمان بازداشت تا اجرای حکم کمتر از ۵۰ روز زمان گذشته است؛ موضوعی که پرسش‌های جدی درباره سرعت رسیدگی، امکان دفاع مؤثر و فرصت اعتراض در پرونده‌ای با مجازات اعدام ایجاد می‌کند.
قوه قضائیه گفته دادگاه با حضور وکیل برگزار شده، اما روشن نیست این وکیل منتخب متهم بوده یا تسخیری، از چه زمانی به پرونده دسترسی داشته، آیا امکان ملاقات محرمانه و آماده‌سازی دفاع فراهم بوده و آیا متهم فرصت کافی برای اعتراض به ادله فنی، درخواست کارشناسی مستقل و پیگیری مؤثر در دیوان عالی کشور داشته است یا نه.
این پرونده در بستر موج گسترده‌تری از اعدام‌ها، احکام امنیتی، مصادره اموال و رسیدگی‌های شتاب‌زده پس از جنگ قرار می‌گیرد؛ روندی که منتقدان و سازمان‌های حقوق بشری آن را نشانه استفاده فزاینده جمهوری اسلامی از مجازات اعدام برای ایجاد بازدارندگی سیاسی و امنیتی می‌دانند.
@
VahidHeadline
خبرگزاری میزان هیچ اطلاعاتی درباره حرفه این فرد نداده و مشخص نیست که مجتبی کیان چگونه به «اطلاعات صنایع دفاعی» دسترسی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75673" target="_blank">📅 17:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DH0NSXrV0P4gF1JcgJrDfJ57jnWZnbHmlPSX1p6TYMwaAsbfc-1zSr0poxd7_ItW3FeekXIMwZFLdGsdey2O9aUpJ_c0ESw9hPUK75lR5vZ_NwGeU_evxANHsTRYLET3zgYr2P4m33MAEyzf9vnYwRPeatek_d0jPetbi6mGWCECH99W_oGWidRzm5e0xCOQ6YfPAzd3B6lzDdm-L2zEY27CBSMwZA_8GtnQzxObOLJpXd8EyGw2NfDOPCOmfiVIJqBDhVeoUKQUfxwVFosLtw2kLx0TnVeihTaXrNiN-hY4RC8i_2GseueY0Pesg7p43ceKeqIMMkPHZq6qvrAsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: جزئیات توافقی که ترامپ در آستانه امضای آن با ایران است
ترجمه ماشین:
توافقی که آمریکا و ایران در آستانه امضای آن هستند، شامل تمدید ۶۰ روزه آتش‌بس است؛ دوره‌ای که طی آن تنگه هرمز دوباره باز خواهد شد، ایران می‌تواند نفت خود را آزادانه بفروشد و مذاکراتی برای محدود کردن برنامه هسته‌ای ایران برگزار خواهد شد؛ این را یک مقام آمریکایی گفته است.
🔻
چرا مهم است: این توافق از تشدید جنگ جلوگیری می‌کند و فشار بر عرضه جهانی نفت را کاهش می‌دهد. با این حال روشن نیست که آیا به یک توافق صلح پایدار منجر خواهد شد یا نه؛ توافقی که هم‌زمان خواسته‌های هسته‌ای رئیس‌جمهور ترامپ را نیز پوشش دهد.
▪️
وضعیت فعلی: هم ترامپ و هم میانجی‌ها گفته‌اند ممکن است این توافق روز یکشنبه اعلام شود، هرچند هنوز نهایی نشده و همچنان ممکن است از هم بپاشد.
▪️
این مقام آمریکایی طرح کلی مفصلی از پیش‌نویس فعلی ارائه کرده که بخش عمده آن را منابع دیگر نزدیک به مذاکرات نیز تأیید کرده‌اند.
🔻
چه چیزهایی در توافق آمده است؟
دو طرف یک یادداشت تفاهم امضا خواهند کرد که ۶۰ روز اعتبار دارد و با رضایت متقابل قابل تمدید است.
▪️
در این دوره ۶۰ روزه، تنگه هرمز بدون عوارض باز خواهد بود و ایران موافقت می‌کند مین‌هایی را که در این تنگه کار گذاشته پاکسازی کند تا کشتی‌ها آزادانه عبور کنند.
▪️
در مقابل، آمریکا محاصره بنادر ایران را لغو می‌کند و برخی معافیت‌های تحریمی صادر خواهد کرد تا ایران بتواند نفت خود را آزادانه بفروشد.
▪️
این مقام آمریکایی اذعان کرد که این موضوع به سود اقتصاد ایران خواهد بود اما گفت در عین حال کمک قابل توجهی برای بازار جهانی نفت خواهد بود.
🔻
این مقام آمریکایی گفت هرچه ایرانی‌ها سریع‌تر مین‌ها را پاکسازی کنند و اجازه دهند کشتیرانی از سر گرفته شود، محاصره هم سریع‌تر لغو خواهد شد.
▪️
اصل کلیدی ترامپ در این توافق «امتیازدهی در برابر عملکرد» است.
▪️
طبق گفته این مقام، ایران خواستار آزادسازی فوری منابع مالی مسدودشده و لغو دائمی تحریم‌ها بود، اما طرف آمریکایی گفت این موارد فقط پس از ارائه امتیازهای ملموس اجرا خواهد شد.
🔻
مسائل هسته‌ای هنوز باید مذاکره شوند
▪️
به گفته مقام آمریکایی، پیش‌نویس یادداشت تفاهم شامل تعهد ایران به این است که هرگز به دنبال سلاح هسته‌ای نرود و درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالای خود مذاکره کند.
▪️
به گفته دو منبع مطلع، ایران از طریق میانجی‌ها تعهدات شفاهی درباره دامنه امتیازهایی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، به آمریکا ارائه کرده است.
▪️
آمریکا موافقت خواهد کرد که در دوره ۶۰ روزه درباره لغو تحریم‌ها و آزادسازی منابع مالی ایران مذاکره کند؛ هرچند این اقدامات فقط در چارچوب توافق نهایی و پس از اجرای قابل راستی‌آزمایی آن عملی خواهند شد.
▪️
نیروهای آمریکایی که در ماه‌های اخیر در منطقه مستقر شده‌اند، در دوره ۶۰ روزه در منطقه باقی خواهند ماند و فقط در صورتی خارج می‌شوند که توافق نهایی حاصل شود.
🔻
نکته قابل توجه: پیش‌نویس یادداشت تفاهم همچنین تصریح می‌کند که جنگ میان اسرائیل و حزب‌الله در لبنان پایان خواهد یافت.
▪️
یک مقام اسرائیلی گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در تماس تلفنی روز شنبه با ترامپ درباره این شرط ابراز نگرانی کرد. او همچنین درباره جنبه‌های دیگر توافق نیز نگرانی‌هایی مطرح کرد، اما به گفته یک مقام آمریکایی، دیدگاه خود را با احترام و لحنی محتاطانه بیان کرد.
▪️
مقام آمریکایی گفت این یک «آتش‌بس یک‌طرفه» نخواهد بود و اگر حزب‌الله برای مسلح شدن دوباره یا تحریک حملات تلاش کند، اسرائیل اجازه خواهد داشت برای جلوگیری از آن اقدام کند.
...
🔻
چه باید دید: به گفته مقام آمریکایی، کاخ سفید امیدوار است اختلافات نهایی در ساعات آینده حل‌وفصل شود و توافق روز یکشنبه اعلام شود.
▪️
این مقام گفت ممکن است توافق حتی کل ۶۰ روز هم دوام نیاورد، اگر آمریکا به این نتیجه برسد که ایران درباره مذاکرات هسته‌ای جدی نیست. از سوی دیگر، آمریکا معتقد است فشار اقتصادی بر ایران انگیزه‌ای برای رسیدن به توافق کامل به‌منظور رفع تحریم‌ها و آزادسازی منابع مالی این کشور ایجاد می‌کند.
▪️
این مقام آمریکایی گفت: «دیدنی خواهد بود که ایران واقعا تا کجا حاضر است پیش برود؛ اما اگر آن‌ها توانایی و تمایل تغییر مسیر خود را داشته باشند، این مرحله بعدی آن‌ها را وادار خواهد کرد تصمیم‌های حیاتی درباره این بگیرند که می‌خواهند چه نوع کشوری باشند.»
▪️
مشاوران ترامپ می‌گویند اگر خواسته‌های او درباره برنامه هسته‌ای ایران برآورده شود، رئیس‌جمهور آماده است برای بازتنظیم روابط با ایران و دادن فرصت به این کشور برای دنبال کردن ظرفیت کامل اقتصادی‌اش، که به نظر ترامپ «عظیم» است، اقدامات بسیار گسترده‌ای انجام دهد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75672" target="_blank">📅 07:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6sI5R2KAZi4rgWnbxmMf3b6mqsC-UGAWGhFSO-WHdvvkJuJpYTbRX91B9XLnh-myzfT0HihNMvXFSaAANASlnpV_2b9iH3vbVtQKtUxhg84BBZqtA0So2ObQznyK8OAohH-zsSo9q4iljpSZnp0h3iQdwScE2-F_NI258IUZKhTHTp9mcE0ZQ2GWDig17MzXOYXrk1ughZXwoZP12OdFSo439xCbj_D_Juk4KChobvj-AwJ1cMdHoox_7bPY0-iuLx-u7Ym8kBkkqgiiCgTqM7bhGinZyTAyZfszfwHr5Xb74dub1eVUipYuKr4Ygb5E__Jp5PFzS7St9vjzQbrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaYs9wa1hnO0CD27NSXxJJmqzUEIjIqDfBFUr0407ca4OM4iHyHu7iTSzPdAeXJ4wMoEevrNhTqqSn-jvOhsOTd1oS1W-yfN0KdK_lyfhcnlmKnTz2DzzHeaUy93LQkipCAG45iJD7avHQMxCIICyWSzgF8B2rUPS1n9dIJNIWc3Wyqy37FVrq_prHUuPue2lV_Umk79L7iFD_mh8SG2OrvFqph-GI0UKTdQ2W6X-3pj0PrxtVWAJEg9isjehATl3GkqXNf-zJYxl0bpyeAoKznoFDTW5Yj6Fx-tYxYvLIaHZ8wd0aUoO62vi84HSbm5llTUbrNFBQIh-jZjt3UYFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه، در پیامی در شبکه اجتماعی ایکس با درج تصویر سنگ‌نگاره پیروزی شاپور اول ساسانی بر امپراتور روم، نوشت: «وقتی ایرانیان مهاجمان متوهم را ناکام گذاشتند.»
او در این پیام که کنایه‌ای است به محاصره دریایی بنادر ایران توسط آمریکا نوشت: «رومیان تصور می‌کردند که رم مرکز عالم است؛ اما ایرانیان این توهم را در هم شکستند.»
پیام آقای بقایی که به نحو گسترده‌ای در کانال‌های تلگرامی رسانه‌های حکومتی ایران بازنشر شده است به نظر می‌رسد که با استفاده از سنگ‌نگاره پیروزی شاپور بر امپراتوران روم در نقش رستم استان فارس بازنقش شده است.
آقای بقایی که اخیرا با حکم محمدباقر قالیباف به عنوان سخنگوی هیئت مذاکره‌کننده ایران هم منصوب شده است با اشاره به لشگرکشی مارکوس یولیوس فیلیپوس معروف به فیلیپ عرب، امپراتور روم، علیه امپراتوری ساسانیان، نوشت که لشگرکشی او «منجر به پیروزی رومیان نشد بلکه به صلحی با شروط شاپور اول ختم شد؛ امپراتور ناچار شد با واقعیت کنار بیاید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75670" target="_blank">📅 06:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZOFNhWAqjyGvXGFpwIM1a78COONijWK2H6faBg4ZmCD935AWIvs7C53V6ev3O-JUNvWaq6iNdCHvw3zrwHgrWZInf_yeEUJDGQnsVkpM1w8bNApi878prABfp6_mYKzzcmJn0GEP1jkR7Z0qI_KLDcDifrIncMuWmJQiDt-FtpnLV2jy8N3Xux878c285M08pyXLNGo8tcyASGTa7R4oD83Eq1nAOoXK84MtGpLkMu8eQukUuTRY-7kDrzmxFmuOeJQu_8fTJ9d6nwNXih9JZIbDgmYScQwzSg8T3WrUspl02DAqW91t77HXChQ0scpEdkprnxgvikW701cjmwQEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز به نقل از دو مقام آمریکایی گزارش داد، یکی از عناصر کلیدی توافق پیشنهادی میان واشنگتن و تهران، تعهد آشکار ایران به واگذاری ذخایر اورانیوم با غنی‌سازی بالای خود است؛
مقامات آمریکایی تصریح کردند که این پیشنهاد هنوز جزئیات دقیق نحوه واگذاری این ذخایر را تعیین نکرده و حل این مسئله را به دور بعدی گفتگوها درباره برنامه هسته‌ای ایران موکول کرده است، اما یک بیانیه کلی که ایران را متعهد به این کار کند، که هدف دیرینه ایالات متحده بوده، برای توافق بسیار حیاتی است، به‌ویژه اگر این توافق کلی با بدبینی جمهوری‌خواهان در کنگره مواجه شود. تا این لحظه، ایران هیچ بیانیه‌ عمومی درباره توافقی که ترامپ اعلام کرده، صادر نکرده است.
تهران در ابتدا با گنجاندن هرگونه توافقی درباره ذخایر اورانیوم غنی‌شده خود در این مرحله اولیه مخالفت کرده و خواستار موکول شدن آن به مرحله دوم گفتگوها بود، اما مذاکره‌کنندگان آمریکایی از طریق واسطه‌ها به صراحت اعلام کردند که بدون دستیابی به توافقی بر سر این ذخایر در فاز اولیه، میز مذاکره را ترک کرده و کارزار نظامی خود را از سر خواهند گرفت.
براساس این گزارش، بخش دیگری از این توافق محتمل شامل آزادسازی میلیاردها دلار از دارایی‌های بلوکه‌شده ایران در خارج از کشور است؛ اما به گفته مقامات آمریکایی، ایران تنها زمانی به بخش عمده این دارایی‌ها که قرار است توسط ایالات متحده و متحدانش در یک صندوق بازسازی قرار گیرد دسترسی پیدا خواهد کرد که با یک توافق هسته‌ای نهایی موافقت کند؛ امری که انگیزه‌ای برای تهران ایجاد می‌کند تا پای میز مذاکره بماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75669" target="_blank">📅 05:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JbihEGIHIBBvwrcxA_3YEaThrKmq5qKY-n6sMpr_iImnX_VasQrEDKvB4B1E0VloS_q-EIFR2-7MvecsjYow5IIXvkYg-AZFOyFRHh-0OLY81TE5K-qzu0FPqlfOpakHpcQ423Mk6mzP_nAaQQyj2S38LGF3NzyOieyVSQCPCCMoLNwvByDvuZ6YQF4vtXOrPEv7f2KJauL2WgWzuGcsijtKHgpjHBGCchRUcz5vDQCJPU8DCu7pnSX0uxv5rpZBsUgOSg2jtXk_JrDWd2u0HyM1RoSRBMtLXz07r9cqY-bfxKy7MxmKaFR_OGGYLAbImkZxiA3ua_vEt-TtB2EAGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف، نخست‌وزیر پاکستان، ابراز امیدواری کرد پاکستان به‌زودی میزبان دور بعدی گفت‌وگوهای تهران و واشینگتن باشد.
CMShehbaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75668" target="_blank">📅 05:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75666">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f6izLQWT8KQBB0DmNypCTVcQ3vldBa-G22_KyNSDtplklsabdvcY_L4DDxjKvIB-CQe8siBL6r0MAjzGTv7zfqygCknXiOrE6EnMKsU09y6NwVgvrQyQHFrOM0XXEc9wAR1JBrowipEa7Mb18mquUFTvm9Uq7oRhOKNcRPgh9Of9egUQrw4Jz6FGE0b-RR1LpAYv0g951ajrYNgykeeEGxM5ef87A11UWT6_rwvmOP5bKO7y0fnCN7VCYaELKSh4XL3h3J5WGuVBJaPitfZ8GE5a6JCSBlY-PMbYsCUymK8ddOPjEr6QbGza2LW8D2Lc_Yiygyfuvxq9xri2BmD8xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mviNAzrC9H7iQ8adh0hofCdmwljYzJJKF9xmf9wJgcFOOaxnUtAws8_ga4RdXWa__f46nTOgunwSGMHBYSreETUGqKhiE-uFR6qLsKm_yZR0ICXaxBml9guYniwuzw2qWFboQ3JiPnt-3oOWwS6wjRRy5f3xfklfVlex2zz9mV1IcF8MyWPSFykgYpaj3ctjc-xTWtuvPECrjR9WrV5fWiMHjhlR1ajK_pKFGz_5D2jkxZ_Qjimd2F8BfG6pM0MxdfGSySbNWhZBOzZ3fusDglfZOcXLIpgwsaWbxGdWPzsimF28Ak-W-V4fBv6nFV1a-p5lQYxP4BUjaSlKhC38bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توییت‌های تد کروز و لیندسی گراهام در واکنش به اخبار منتشر شده درباره توافق احتمالی
tedcruz
,
LindseyGrahamSC
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/75666" target="_blank">📅 04:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75665">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7119557db8.mp4?token=hRY4vJn1EbBpfvEk79vJ-FyznvK_UUvI9PiFVPEgrf7jeT9Ir3Aw3dxSQuq5YEpJX-78hSIeP-Ia0DCxOD5c41Hfai_0gLkBj23aOIQKtMQHkN6VcnDfOwES9HQCuVtIM-acoe6MPvtoBvqMHA3HqPWiuUqf2WWpr_9n6Rgo7Z5kC43Z47EZzQlCg4FG6Kn8x7uhvTvE4f50Z-2gL6PwlVng1AvuuILBp1MyJOaMiyUrMJIQzA-YzmoL3wA6aWEhQOaZ5FQxcERkPFZ3mgSZxbmRzwNOBfd33ysIWyfnpfA-SaTaiQJCCMP-v4qgQuixq77OvjWqbe6ld9IMdhGSEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7119557db8.mp4?token=hRY4vJn1EbBpfvEk79vJ-FyznvK_UUvI9PiFVPEgrf7jeT9Ir3Aw3dxSQuq5YEpJX-78hSIeP-Ia0DCxOD5c41Hfai_0gLkBj23aOIQKtMQHkN6VcnDfOwES9HQCuVtIM-acoe6MPvtoBvqMHA3HqPWiuUqf2WWpr_9n6Rgo7Z5kC43Z47EZzQlCg4FG6Kn8x7uhvTvE4f50Z-2gL6PwlVng1AvuuILBp1MyJOaMiyUrMJIQzA-YzmoL3wA6aWEhQOaZ5FQxcERkPFZ3mgSZxbmRzwNOBfd33ysIWyfnpfA-SaTaiQJCCMP-v4qgQuixq77OvjWqbe6ld9IMdhGSEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنبه عصر، یک تیراندازی در حوالی کاخ سفید خبر روی داد که طی آن دو نفر از جمله یک عابر و فرد مظنون تیر خوردند.
سرویس مخفی ایالات متحده، در گزارشی اعلام کرد که اندکی پس از ساعت ۶ عصر روز شنبه، فردی در محدوده خیابان ۱۷ و خیابان پنسیلوانیا، (شمال غربی) سلاحی را از کیف خود خارج کرد و شروع به تیراندازی کرد.
سرویس مخفی ایالات متحده افزود پلیس سرویس مخفی به تیرانازی او پاسخ داد و به مظنون شلیک کرد.
به گفته سرویس مخفی،‌مظنون به یک بیمارستان محلی منتقل شد، اما در آنجا اعلام شد که جان باخته است.
به گفته این نهاد امنیی، در جریان این تیراندازی، یک عابر نیز مورد اصابت گلوله قرار گرفت و هیچ‌یک از مأموران آسیب ندیدند.
سرویس مخفی که وظیفه حفاظت از رئیس‌جمهوری آمریکا را دارد افزود دونالد ترامپ، رئیس‌جمهوری آمریکا، در زمان حادثه در کاخ سفید حضور داشت.
@
VahidHeadline
آپدیت:
رسانه‌های آمریکایی هویت عامل تیراندازی عصر شنبه در مجاورت کاخ سفید را «نصیر بست»، جوان ۲۱ ساله اهل مریلند، معرفی کردند که به عنوان فردی با اختلالات روانی و عاطفی شدید برای ماموران امنیتی شناخته‌شده بوده است.
بر اساس گزارش‌ها، این فرد که پیش از این در ژوئن ۲۰۲۵ با ادعای این‌که «خدا» است یک مسیر ورودی کاخ سفید را مسدود کرده و پس از آن به یک مرکز روان‌پزشکی منتقل شده بود، به دلیل تلاش مجدد برای ورود به حریم کاخ سفید در ژوئیه همان سال، حکم دادگاه مبنی بر «ممنوعیت ورود و نزدیکی به این عمارت» را داشته است.
گزارش‌های تکمیلی نشان می‌دهد که «نصیر بست» دست‌کم در یک پست رسانه‌های اجتماعی تمایل خود را برای آسیب رساندن به دونالد ترامپ ابراز کرده بود؛ او سرانجام پس از نقض حکم دادگاه، نزدیک شدن به ایست بازرسی خیابان هفدهم و پنسیلوانیا و گشودن آتش به سمت ماموران، در تبادل آتش متقابل با نیروهای سرویس مخفی هدف قرار گرفت و در بیمارستان جان باخت.
📷
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75665" target="_blank">📅 04:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75664">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVBnsm3DjBd4f0aIambIG_CTH4_o4M41G9gYeidURJUvDan35pljE93ewaTFFiaEs-sbC3pkN7oIc7sz7ArY6khl4zG88GBovswTo3NLneMs0oHZQ78Vozr8kcfeQOPQRgXj7udqTvgVPYVINpUUnA7eoywkXzSXI5LZYr7yGQoctKUCqdId6TAMepbakFBnCSzf-9D0-HQ6ax_Y4U_q8qRpYgC04-GRselimXTFkBP3i2_7ZRTQ_svPCXAPW8TpGzRy1crdgwiFGSI_nCJs5JYowrC0ghAtArplEAIIwV15DewAjDb_c1c_CU4I_0i2p7RKmCsl5iYAABxyhGNF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس، خبرگزاری وابسته به سپاه، در واکنش به پیام دونالد ترامپ، رئیس‌جمهوری آمریکا مبنی بر نزدیک شدن به توافق با ایران و بازگشایی تنگه هرمز نوشت: «این ادعا نیز با واقعیت‌ها فاصله دارد».
فارس در ادامه نوشت: «برخلاف ادعای لحظات قبل دونالد ترامپ در شبکه اجتماعی تروث سوشال مبنی بر بازگشت تنگه هرمز به وضعیت پیشین و آماده‌سازی برای امضای توافق‌نامه، پیگیری‌های خبرنگار فارس نشان می‌دهد که این ادعا نیز با واقعیت‌ها فاصله دارد؛ چرا که بر اساس آخرین متن ردوبدل‌شده، در صورت توافق احتمالی، تنگه هرمز کماکان تحت مدیریت ایران خواهد بود و اگرچه ایران موافقت کرده اجازه دهد تعداد کشتی‌های عبوری به میزان قبل از جنگ بازگردد، اما این به‌هیچ‌عنوان به معنای تردد آزاد به وضعیت قبل از جنگ نیست و مدیریت تنگه، تعیین مسیر، زمان، نحوه عبور و صدور مجوز، کماکان در انحصار و با تدبیر جمهوری اسلامی ایران خواهد بود.»
خبرگزاری سپاه در ادامه مدعی شد که برخلاف شروط پیشین ترامپ مبنی بر گنجاندن برنامه هسته‌ای در توافق، «هیچ تعهدی از سوی ایران داده نشده و پرونده هسته‌ای اساسا در این مرحله مورد بحث قرار نگرفته است.»
فارس همچنین ادعا کرد که «مقامات آمریکایی در پیغام‌های متعدد به ایران اذعان داشته‌اند که توییت‌های ترامپ عمدتا جنبه تبلیغاتی و مصرف رسانه‌ای در داخل آمریکا دارد و توصیه کرده‌اند که به این اظهارات توجهی نشود».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75664" target="_blank">📅 01:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75663">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNHMkYc1jiJrXGvJpYy-QfaVSdJ7BG9T5R0jJGT7IkPoxmY50hFjc2qB_643CdkjQL8nQ195Cehd9SiP_DPfwv2FEW3ith3ArEypAALttjVIlvLOQ9-H1CyXXKN96AuyaGn71XrbBzMKYFazLyEf2tbn7zAwFLI5bZdtziGCbSSonmx0ODliSN_2_YieyqqO5UKXILXx0HrRSXvVrLeQ7ER0i-d79kykQabBAwPHd5RrRljM2c456OWWqj-V-J3vvquJMjK-pawhiokqnWOAzRgu8j0M18a0kiwTsh3BMEkJ9gv2GT7lFP_UeidSANqNzH_FF9p9jRE6AHBrlonuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار الجزیره به نقل از «منابع خود»، مفاد کلیدی پیش‌نویس توافقی را که قرار است میان واشنگتن و تهران نهایی شود را اعلام کرد.
خبرنگار الجزیره مدعی شد، توافق پیشنهادی شامل «پایان جنگ در تمامی جبهه‌ها از جمله لبنان»، «آزادسازی چندین میلیارد دلار از دارایی‌های مسدودشده ایران»، «رفع محاصره دریایی آمریکا و بازگشایی تنگه هرمز» و همچنین «عقب‌نشینی نیروهای آمریکایی از مجاورت مرزهای ایران» است.
پس از اجرای این گام‌ها، طرفین یک مهلت ۳۰ روزه، که با توافق دوطرفه قابل تمدید است، خواهند داشت تا درباره مسئله هسته‌ای به توافق برسند که در طول این مدت نیز تردد از تنگه هرمز تسهیل خواهد شد.
به گفته این خبرنگار، از نظر ایران، مدیریت تنگه هرمز یک موضوع دوجانبه میان تهران و مسقط تلقی می‌شود و گفتگوها در این زمینه با عمان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75663" target="_blank">📅 01:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75662">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7T0eHprFNPakTy-7NUQ3oTAFBolMOTBLkIbzgQ0-6lepGudG--qmJF6Cnk8gk2llSBya9QIiFjzrDJjKwHTrCeJaS-n4MVjUBGnTxvVodzByrgQ3VqkB4oha7StERawARKgK0mJX9akxvBwA3Nf2nK2MKQs8kW4soyXC6PYXQucsWHsf3iqgsjlKX5wrtTCv8RnRfyggJFXN14fEEN51nsz5IGYn2dUKD6kv7JMOUgcksAy0Vedh3mRLznEz2SQXWemI4qrjWq7gyKgoPGs7LRUmjOOO-WApbT3NkqOqedAZDlvAlWAMLTY5bGReoKDgZlUoDzaUSxRLtHv23RAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یک منبع ارشد منطقه‌ای» از جزییات گفتگوی رهبران کشورهای عربی و مسلمان با دونالد ترامپ خبر داد.
خبرنگار آکسیوس نوشت: «یک منبع ارشد منطقه‌ای به من گفت که تمامی رهبران عرب و مسلمان حاضر در گفتگوی روز شنبه با ترامپ، از او خواسته‌اند تا برای پایان دادن به جنگ و مهار تنش‌ها در منطقه، توافق را پیش ببرد.»
این منبع تاکید کرده است که «پیام همه این بود: لطفا به خاطر کل منطقه، جنگ را متوقف کنید.»
به گفته این منبع، مذاکرات به خوبی در حال پیشرفت است و میانجی‌ها امیدوارند روز یکشنبه یک توافق چارچوب یک‌صفحه‌ای را منعقد و بلافاصله آن را اعلام کنند و پس از آن، قصد دارند ظرف چند روز مذاکرات را برای دستیابی به یک توافق دقیق و پرجزئیات آغاز کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/75662" target="_blank">📅 00:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75660">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H0oBRtRZivReyhIAMGbARmYcFo_61oqbXuFOsRvQuZiI8e7ZPCmEqkfVNWEfVMRbH6Un1M0MfYIQi9VE8dWFn0IV7Bte0d0pSluBsH2rPpeLFCpOA5S907nWVbLngsfZ4Va9PrLae3VqyyrVnuLo47vzonvGNRc5g-Ug3Jsbh2jxj_4tq7yKAChoqIXmQaxoAJ7iCyYFQHeuULDj_JIQjdBVbqwwTPWJbWG2GQi-Fra9dM5S7mUiGsZ8FZXAaFhAuuwoBgcLewVObE_zVPoJzK4hVPydhcUDAKe6yGPRiSFU_1_hQYbPgekjktJ7D0qc5JGlKqlxDaMCSiXpFdxAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: یک توافق تنظیم شده و اکنون در انتظار نهایی شدن است
پست ترامپ، ترجمه ماشین:
من در دفتر بیضیِ کاخ سفید هستم؛ جایی که همین حالا تماس بسیار خوبی با
▪️
پرزیدنت محمد بن سلمان آل سعود از عربستان سعودی،
▪️
محمد بن زاید آل نهیان از امارات متحده عربی،
▪️
امیر تمیم بن حمد بن خلیفه آل ثانی،
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جبر آل ثانی و وزیر علی الثوادی از قطر،
▪️
فیلد مارشال سید عاصم منیر احمد شاه از پاکستان،
▪️
رجب طیب اردوغان رئیس‌جمهور ترکیه،
▪️
عبدالفتاح السیسی رئیس‌جمهور مصر،
▪️
عبدالله دوم پادشاه اردن،
▪️
و حمد بن عیسی آل خلیفه پادشاه بحرین،
درباره جمهوری اسلامی ایران و همه مسائل مربوط به یادداشت تفاهمی در ارتباط با صلح داشتیم.
یک توافق تا حد زیادی مذاکره شده و نهایی شدن آن منوط به جمع‌بندی میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگری است که نامشان ذکر شد.
▪️
جداگانه، با نخست‌وزیر بی‌بی نتانیاهو از اسرائیل نیز تماسی داشتم که آن هم بسیار خوب پیش رفت.
جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بررسی است و به‌زودی اعلام خواهد شد. علاوه بر بسیاری دیگر از عناصر این توافق، تنگه هرمز باز خواهد شد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75660" target="_blank">📅 00:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75659">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HMaaVSDJ0wOg8CHhuHF8SkS1z9hXlIxFmoonXf5GDfmoBK9PLKGZvVDz1lOINFgnTdgqrzR8iI6m50sXKPDpcvc0utcF223aBnjYmiE2Xry_HWdLjb5g327kDfNwbhMN3hBLPVEgAeNR_gi_o4vp6fobXVmCK1GsSgeNd3F-bij_bR0JSYkAHju40yuoiC5QbmEzmDP6BVE07BjOplMw-49jD0LblDzuhodFPxQez671zW7iRDGJMibAhecfp0sm147a2fXgJP_hDodnF5QGKuRt0Z1A9eDGc7_MKf-FvzFY6Dnb7GtIpQjxQ7R-iIL2mmIxulVh_tDlridSmSRfQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز شنبه دوم خرداد ۱۴۰۵ در تماس‌هایی جداگانه با رهبران عربستان سعودی، امارات، قطر، مصر، ترکیه، پاکستان و فرانسه درباره توافق احتمالی برای پایان جنگ با جمهوری اسلامی گفت‌وگو کرد. همزمان یک مقام آمریکایی آگاه از روند مذاکرات گفت واشنگتن و تهران به دستیابی به توافق نزدیک شده‌اند و اختلاف‌های باقی‌مانده عمدتا بر سر نحوه نگارش برخی بندهای توافق است.
به گزارش اکسیوس، چند تن از رهبران حاضر در تماس با ترامپ از او خواسته‌اند مسیر دستیابی به توافق را دنبال کند. با این حال، این مقام آمریکایی تاکید کرده است که هنوز تصمیم نهایی از سوی رییس‌جمهوری آمریکا اتخاذ نشده و او همچنان می‌تواند توافق را رد کرده و دستور حملات جدید علیه ایران را صادر کند.
همزمان، جی‌دی ونس، معاون رییس‌جمهوری آمریکا، و پیت هگست، وزیر دفاع این کشور، برای شرکت در نشست ویژه بررسی توافق احتمالی به واشینگتن فراخوانده شدند. ترامپ پیش‌تر گفته بود پس از بررسی آخرین پیشنهاد ایران با تیم مذاکره‌کننده خود، احتمالا تا روز یکشنبه درباره ادامه مذاکرات یا ازسرگیری جنگ تصمیم خواهد گرفت.
به گفته منابع آگاه، پیش‌نویس جدیدی که قرار است ترامپ آن را بررسی کند، حاصل مذاکرات اخیر میان ایران و پاکستان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75659" target="_blank">📅 23:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75658">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojQ3_eyG1U9okHpgt3i42RGwYRbq6gzF-nM916PPXDAiUL_W3tf8LZsJGSsJHCXK-pesdMiae_wJ8n7SLu1kgYeSaqyltPDP7mgjjxQmuciUq5Jmon-OIbb3Doib18-VucxUfr8bGlD4cL0pWMX7dqlOIPV6ZBt0qxPKQ8fJX1kFQsvoJemdScl9579HMWPGLNKci-R-dQ8cpxxlfS7czN6do5mH5YtLfNQ7WyUjj__nTaly5Aw0ER5PAqXo-37yugEY5xxqzz4zubTuL62vdIgf2-6ejXtvdv04kzFQyqIFDRcfoE6WTC4oNLo_C5uB9miRTzrVP1XOAyTE8BX8Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ۱۳ اسرائیل در گزارشی از روند گفت‌وگوهای ایران و آمریکا گفت مقام‌های اسرائیلی معتقدند ایالات متحده و ایران به دستیابی به توافق احتمالی نزدیک‌تر شده‌اند و گزارش‌های اخیر و اطلاعاتی که دریافت می‌شود، «در اورشلیم به‌طور فزاینده‌ای معتبر تلقی می‌شود».
بر اساس گزارش این شبکه، مقام‌های ارشد اسرائیلی گفته‌اند پیشرفت در مذاکرات برای بخشی از نهاد امنیتی اسرائیل «بسیار ناامیدکننده» است، به‌ویژه در شرایطی که به نظر می‌رسد تلاش واشینگتن برای رسیدن به توافق در حال تشدید شدن است.
این مقام‌ها همچنین معتقدند فشار برخی مشاوران رئیس‌جمهور ترامپ در روزهای اخیر افزایش یافته و انتظار می‌رود بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در پی این تحولات، نشست‌هایی مشورتی با وزیران ارشد و مقام‌های امنیتی برگزار کند.
نهادها و مقامات رسمی اسرائیل هنوز این گزارش را رد یا تأیید نکرده‌اند.
ارزیابی اسرائیل در دو هفتهٔ گذشته این بود که ترامپ خواهان توافق است، اما در نهایت به دلیل اختلاف بر سر مسائل کلیدی، موفق به دستیابی به آن نخواهد شد. با این حال، مقام‌های اسرائیلی اکنون معتقدند روند کنونی ظاهراً برخلاف چیزی است که اسرائیل در هفته‌های اخیر برای آن تلاش کرده بود.
این گزارش همچنین می‌گوید چارچوبی که دربارهٔ آن گفت‌وگو می‌شود، شامل یک توافق موقت ۶۰ روزه خواهد بود که ممکن است بعداً در حالی که مذاکرات درباره توافقی گسترده‌تر ادامه دارد، تمدید شود.
روز شنبه مقامات ایران و آمریکا و همچنین پاکستان که نقش میانجی را بین دو طرف بر عهده دارد، اعلام کردند که در مذاکرات برای پایان دادن به جنگ پیشرفت حاصل شده است.
روز شنبه، روزنامه اسرائیل هیوم نیز در گزارشی ادعا کرد پیش‌نویس توافقی که روی میز قرار دارد، شامل تعهد اولیه ایران به خودداری از توسعه سلاح هسته‌ای و تعلیق بلندمدت غنی‌سازی اورانیوم است و سایر مسائل، از جمله سرنوشت ذخایر کنونی اورانیوم غنی‌شده ایران، در مذاکرات بعدی در دورهٔ آتش‌بس بررسی خواهد شد.
این روزنامه همچنین به‌نقل از منابع آگاه که نام‌شان را نیاورده، ادعا کرد «رهبری سیاسی ایران پیش‌تر با تحویل اورانیوم غنی‌شده موافقت کرده بود، اما فرماندهان سپاه پاسداران با این اقدام مخالفت کردند و تصمیم‌گیری دربارهٔ این موضوع اکنون به تأیید رهبر جمهوری اسلامی بستگی دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/75658" target="_blank">📅 21:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75657">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZcdFg7BMxRpVbVaRXcsjSi7DxXguuONUcG2aysxOiRzjxRlj3SqttRbzSd0rVhVbjSvfaIIAKR8zArZIfVskq8N_ZPWjzEWb5e5BCRGTQ06_qrzX-B8K-Szm0u061nBH2kFrJn9mJe3dQhRuVHXBHvY-Ap4JLMpEjHBgg6JuX7-j4MAWMmQ2IY2ogWQBSPs_EolwtASMuOA2Fo0kCjsIcfFiJNh8ZusOQ0-uWAbwFczHnSDc0B5W2nPVJe60O5IA7zehZsPgk46T2aZ0SWCmBAVZj51GbRqaUlO9jE0oqpg2HSQSrDsVZKJC5MqsDKdcoflBHkXrRVgTCwEx6nG60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه و نزدیک به تیم مذاکره‌کننده، با تاکید بر اینکه اگر آمریکا انعطاف نشان ندهد، مذاکره شکست می‌خورد نوشت که موضوع هسته‌ای، پول‌های بلوکه‌شده و کنترل جمهوری اسلامی بر تنگه هرمز، سه موضوع اختلاف جدی در مذاکرات است.
فارس نوشت که تهران اعلام کرده که در این دوره وارد مذاکره درباره موضوع هسته‌ای نمی‌شود. تنها در صورتی که طرف مقابل شرایط اعتمادساز را اجرا کند، در دور بعد درباره مسائل هسته‌ای صحبت خواهد شد.
رسانه سپاه به نقل از این منبع نوشت: «پول‌‌های بلوکه‌شده باید واریز شود؛ شرط دوم و اساسی برای ورود تهران به مذاکره این است که پول‌های بلوکه‌شده ابتدا واریز و آزاد شوند. بدون این اتفاق، اساسا وارد مذاکره نمی‌شویم.»
در ادامه آمده است: «اختلاف دیگر بر سر نحوه عبور کشتی‌ها در تنگه هرمز است. آمریکا تاکید دارد که تنگه باید کاملا به شرایط پیشین بازگردد، اما تهران می‌گوید فقط خود را متعهد می‌کند که تعداد کشتی‌ها به وضعیت قبل بازگردد. معنای این حرف آن است که حکومت ایران با مدل خود، تعداد کشتی‌های مجاز برای عبور را تعیین می‌کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/75657" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75656">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MA9HZg2B-3IUqgdSmwSxK5_QNq35FJmM5jvTglDra9UT8H0XSWpwA-ZRup64MTKjGgUdD_UKHWDQ2D6w46wc2jIPbKDoFlSDo-YI0kIBb9CBGDdNg7S7H9ljbiqK1nzcSODVLbq23LNdAYF-bdU_sKc-2DgjRwKgZHok4sirVNMfNyyBfCWls8O1JqZT6rVANSBgIAZrkJQvslQCdOTqzBQ9xbu2tPhbcwctrHNN4ZIq4Dv0Cb091wowsUB3NdblZ2sOkecYj6f4KSBRd1YKbano2_euCFMzFsHFCkYg7T_cc_UxgsdSstEQbXl8ekjjJF2ZJ5SZc-utXMvA2IsFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به توافق بسیار نزدیک‌تر شده‌ایم
ترجمه ماشین:
پرزیدنت ترامپ به شبکه سی‌بی‌اس نیوز گفت مذاکره‌کنندگان ایالات متحده و ایران برای نهایی کردن توافقی که به جنگ میان دو کشور پایان دهد، «بسیار به هم نزدیک‌تر شده‌اند».
منابع آگاه از مذاکرات به سی‌بی‌اس نیوز گفتند تازه‌ترین پیشنهاد شامل روندی برای بازگشایی تنگه هرمز، آزادسازی بخشی از دارایی‌های ایران که در بانک‌های خارجی نگهداری می‌شود، و ادامه مذاکرات است.
آقای ترامپ از ارائه جزئیات درباره این توافق خودداری کرد، اما گفت که «هر روز بهتر و بهتر می‌شود.»
آقای ترامپ در یک مصاحبه تلفنی به سی‌بی‌اس نیوز گفت: «نمی‌توانم قبل از اینکه به خودشان بگویم، به شما بگویم، درست است؟»
👈
آقای ترامپ گفت معتقد است توافق نهایی مانع دستیابی ایران به سلاح هسته‌ای خواهد شد و افزود که در غیر این صورت «اصلاً درباره آن صحبت هم نمی‌کرد».
👈
او همچنین گفت این توافق باعث خواهد شد اورانیوم غنی‌شده ایران «به شکل رضایت‌بخشی مدیریت شود.»
👈
او گفت: «من فقط توافقی را امضا می‌کنم که در آن به هر چیزی که می‌خواهیم برسیم.»
منابع به سی‌بی‌اس نیوز گفتند آقای ترامپ هنوز در حال بررسی پیشنهادهاست و هنوز تصمیم نهایی خود را نگرفته است. این منابع گفتند او با مشاوران خود رایزنی می‌کند و با رهبران خارجی، از جمله رهبران عربستان سعودی و دیگر کشورهای حوزه خلیج فارس، گفت‌وگو دارد.
آقای ترامپ گفت اگر آمریکا و ایران به توافق نرسند، «با وضعیتی روبه‌رو خواهیم شد که هیچ کشوری هرگز به اندازه ضربه‌ای که آن‌ها در آستانه دریافتش هستند، ضربه نخورده باشد.»
آقای ترامپ پیش‌تر ایران را تهدید کرده بود؛ او پیش از آغاز آتش‌بسی که در ماه آوریل آغاز شد، گفته بود بدون توافق «یک تمدن کامل نابود خواهد شد» و اخیراً نیز به این کشور هشدار داده بود که «ساعت در حال تیک‌تاک است.»
مارکو روبیو، وزیر خارجه آمریکا، نیز روز شنبه گفت ممکن است «بعداً امروز خبری» درباره وضعیت مذاکرات میان ایران و آمریکا منتشر شود.
روبیو پیش از یک شام رسمی در سفارت آمریکا در دهلی‌نو، هند، گفت: «پیشرفت‌هایی حاصل شده، همین حالا هم که با شما صحبت می‌کنم، کارهایی در حال انجام است. این احتمال وجود دارد که چه بعداً امروز، چه فردا، چه ظرف چند روز آینده، چیزی برای گفتن داشته باشیم؛ اما همان‌طور که رئیس‌جمهور گفت، این موضوع باید به یک شکل یا شکل دیگر حل شود.»
CBSNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75656" target="_blank">📅 19:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75655">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NgCx60Su0DHeRmISQObkPcpp0gA-XtiQND5j4370Er9hozJa2LMq43oujp3MJJWQcz92mdJBjzBbDIINbOL4KNOL0nmEQ-Ud76-xoPVjR187GZ9uo80uQdRCmjwHMcen6IOMrvJCS8VZtqiSEm4QJo7cEhCT7pfj6yA9hEPmbCJ26OdtxHM_R-1HHudskBeHbYNdycgGnuINZv8cIpfC5IkrXIVjoViGtpnYpYZ_zoT3hhYP83lQCPde9PyZtspW29zL1oYEVAzXUSlb24_uEIVF5ElHINlBCvQMAvQCkNxGGXT5fI1lt7UcXPxHMBXmaiAUBM584NRi_7ftA-cZHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز شنبه دوم خرداد در گفتگو با آکسیوس اعلام کرد که اواخر امروز با تیم مذاکره‌کننده خود دیدار می‌کند تا آخرین پیشنهاد ایران را بررسی کند. او افزود که احتمالا تا روز یکشنبه درباره پذیرش توافق یا از سرگیری جنگ تصمیم‌گیری خواهد کرد.
ترامپ شانس دستیابی به یک توافق «خوب» یا در غیر این صورت، «نابود کردن کامل آن‌ها» را یک «۵۰-۵۰ محکم» توصیف کرد. به گفته او، قرار است اواخر روز شنبه نشستی با حضور استیو ویتکاف، جرد کوشنر و جی‌دی ونس، معاون رئیس‌جمهور، برای بررسی پاسخ اخیر جمهوری اسلامی برگزار شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/75655" target="_blank">📅 19:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75654">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BD2bFYtVo-7dabBLGT61bvcd1QG49ic01i0162Ctb6-1oq346FoVgN2hPDX2md8pcnwugKpJpXYx_9GZihmydSsC0vP_WBH89yvtVDu6bS31J0-UMsG0pJKaWV2QgSL5-1Rndh01eFd0WNHtiL6iuXMHD1SUE3RrO1u0Er2lXR6b3M7YLP31n9Ye9YY_e2pzz88GFL3EAOhmFzV7mqTyM66wq4TaKtsLDQ3-gtm8VSMI4qnkvt0l6H1YV_IbdbwjRilkiPlGKbgj-oZFs0OzALqwNGLoj8LLlcoUBu3oMQBpzTcW7_9OzA2pKd26l2bZQipxFzEftoLoINCL5bbV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، رسانه وابسته به سپاه، درباره روند مذاکرات تهران و واشینگتن، با اشاره به اینکه هنوز اختلافات جدی در بعضی از حوزه‌ها مانند تعهد واقعی آمریکا به آزادسازی اموال و موضوع تنگه هرمز وجود دارد، نوشت: «با توجه به زیاده‌خواهی‌های آمریکا، احتمال عدم حل موضوعات بالاست.»
در این گزارش آمده که در صورت حل موارد اختلاف، احتمالا در گام اول یک تفاهم اولیه اعلام شود و سپس مهلت ۳۰ یا ۶۰ روزه برای گفتگو درباره موضوع هسته‌ای (بدون تعهد اولیه جمهوری اسلامی) اعلام شود.
تسنیم نوشت که آمریکایی‌ها در متون پیشین خود تاکید داشتند که تهران در همان گام نخست باید امتیازاتی در بحث هسته‌ای بدهد و موضوع تعطیلی تاسیسات هسته‌ای و تحویل مواد غنی‌شده به آمریکایی‌ها از جمله مباحثی است که مدام در متن‌های آمریکایی‌ها مورد درخواست قرار می‌گرفت اما حکومت ایران اساسا بحث درباره جزئیات هسته‌ای را در این مرحله رد می‌کند.
بر اساس این گزارش تهران بر ضرورت پایان جنگ و تهدید در همه جبهه‌ها از جمله لبنان تاکید دارد. و این موضوع باید مورد پذیرش طرف آمریکایی قرار گیرد اما آمریکایی‌ها در برخی از متن‌های پیشین خود با این موضوعات مخالفت کرده‌اند.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه، به نقل از یک منبع مطلع نوشت که خبر العربیه درباره اینکه تهران پیشنهاد تعلیق ۱۰ ساله غنی‌سازی اورانیوم بالای ۳.۶ درصد را مطرح کرده، «از اساس کذب است».
تسنیم به نقل از این منبع با تاکید بر «ساختگی» بودن خبر العربیه، نوشت: «اساسا تمرکز پیام‌ها و گفتگوها در وضعیت فعلی صرفا بر روی مساله پایان جنگ است و هیچ جزئیاتی درباره موضوع هسته‌ای مورد بحث قرار نمی‌گیرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/75654" target="_blank">📅 19:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75653">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psLjdn4bgMw1wmJRdHlVBSNouTTWlZ3PZtisx7ShsvAsM7lWeEaUScU2YgojQdPRzQmUdgpSDwgBgt0UsK4zXskNXeSwjxfM6aJMlQM8tFupr2IBx4po8_JUObGznTpl-0nGFoONK6QS1NmWdZzSn9QRZSFmYNlfTxom02qd8wqj5U_BDX-s2GE4jHlkI2fjglMOUbZjQvpqhulnGxruX7YTEncFJMT0_aJpo9UmkiSFVsCgzeG3hbz4OGJzMuJuUNdJYlqxuQ1Cggr21ExsYuZ_A6tT-x7s1IOQJbWFHtwYtyuCKOWL2-TOW_h83cNGCrVu7q72gk0ZAi6L85Au4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخش رسانه‌ای ارتش پاکستان (ISPR) آخرین دور گفتگوها میان میانجی‌های قطری-پاکستانی و مقامات بلندپایه جمهوری اسلامی را «کوتاه اما بسیار پربار» توصیف کرد.
بر اساس بیانیه منتشر شده، این رایزنی‌های فشرده در ۲۴ ساعت گذشته در فضایی مثبت و سازنده برگزار شده و پیشرفت‌های دلگرم‌کننده‌ای را برای دستیابی به یک تفاهم نهایی جهت پایان دادن به جنگ ایجاد کرده است.
ارتش پاکستان جزئیات بیشتری از مفاد دقیق این مذاکرات ارائه نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/75653" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75652">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeEVRAHzgMG0DIBfen4256i_CJSWJvBn_fU51xGA_DrSENpSe2w0uEOGc4kDIANE-5p7Rpk7RPtq9XSNPRjXbjxBFNqkzCs67ztg8tL2qg2wRlRtdLzOBRvQAm2sy1k-GxFqtUFzO-S-AdlTd2-8xaKJOc3YVUQvh9DmsoPdEqBCQED7WTntkawH8xlkfJyJMQjU6TvS2gXKGHdBoNUgYSo4zk3SzsYXgiSEHmZBegjPXrdBYhOlF2t0BBC_QYaCbL8xFb9Ay9hLuNLUwiuMyEFsjGMo8RjWFnCxp1wpV_hIaEuQmn7Pe9VmhCqkrnn4N5DyLJCE-fjNZ_vC2qKz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال تایمز گزارش داد که میانجی‌های جنگ ایران معتقدند در حال نزدیک شدن به توافقی هستند که آتش‌بس میان واشینگتن و تهران را به مدت ۶۰ روز تمدید و چارچوبی برای مذاکرات درباره برنامه هسته‌ای جمهوری اسلامی ایجاد کند.
بنا بر این گزارش، افرادی که در جریان این مذاکرات قرار دارند به این رسانه گفتند این توافق شامل بازگشایی تدریجی تنگه هرمز و همچنین تعهد به بررسی رقیق‌سازی یا واگذاری ذخایر اورانیوم با غنای بالا خواهد بود.
فایننشال تایمز افزود که آمریکا همچنین محاصره دریایی بنادر جنوب ایران را کاهش می‌دهد و با کاهش تحریم‌ها و همچنین آزادسازی مرحله‌ای دارایی‌های مسدودشده تهران در خارج از کشور موافقت خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/75652" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75651">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d608f8c4.mp4?token=YWAFz3uW1Iq8wrll5POX_PtmMknwZzxEc6qDp2I-I1vFIj8_rHIuzm5VcbLSsbpcCdZCl83cz45_jQvWHoTEVCmWBEHAkgjI0ALGp6zxY1-KwezebouQN-3xT4Iq-tDvgLcSNTiWVpj8MxyiWL-dnxrhPaY4MLSnGU3Pl7m5co8R0gJydPrb27hHmfAdmsxUtAlft0UXdgRMUBf0_2d7cMKTQ4HO8HDEG0zdihKNJrntDfKPVVzhjVGMdcmUvJKrTwIV13S7U-wyzC-TLTCbAtqT2rNk7FXrHdM_VsA2pjCeuvH3w0k44W5DdnNhSlKL6I_jZqiIQLXNEQO6xEwIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d608f8c4.mp4?token=YWAFz3uW1Iq8wrll5POX_PtmMknwZzxEc6qDp2I-I1vFIj8_rHIuzm5VcbLSsbpcCdZCl83cz45_jQvWHoTEVCmWBEHAkgjI0ALGp6zxY1-KwezebouQN-3xT4Iq-tDvgLcSNTiWVpj8MxyiWL-dnxrhPaY4MLSnGU3Pl7m5co8R0gJydPrb27hHmfAdmsxUtAlft0UXdgRMUBf0_2d7cMKTQ4HO8HDEG0zdihKNJrntDfKPVVzhjVGMdcmUvJKrTwIV13S7U-wyzC-TLTCbAtqT2rNk7FXrHdM_VsA2pjCeuvH3w0k44W5DdnNhSlKL6I_jZqiIQLXNEQO6xEwIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‌ویدیوهایی از اعتراض دانش‌آموزان در شهرهای مختلف منتشر شده است. این دانش‌آموزان به حضوری شدن امتحاناتشان اعتراض دارند.
دانش‌آموزان در شهرهای خرم‌آباد، یاسوج و دورود مقابل ساختمان‌های آموزش و پرورش این شهرها تجمع کردند و با شعارهای مختلف اعتراض خودشان را نشان دادند.
در جریان اعتراضات سراسری در دی ماه ۱۴۰۴ که به کشتار بی‌سابقه معترضان انجامید در بعضی استان‌ها مدارس غیرحضوری شد.
با شروع جنگ آمریکا و اسرائیل با ایران، مدارس در ایران تعطیل شد و بعد از تعطیلات نوروز کلیه کلاس‌ها غیرحضوری برگزار شد.
چند روز پیش عبدالرضا فولادوند، سرپرست مرکز ارزشیابی آموزش و پرورش در یک مصاحبه تلویزیونی از احتمال برگزاری امتحانات به صورت حضوری خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75651" target="_blank">📅 19:05 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
