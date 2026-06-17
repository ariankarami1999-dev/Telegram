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
<img src="https://cdn4.telesco.pe/file/Wb-Ss0AqSTsFYj58dPUV2mO2qoM213g3lwYFUifnSBumLlKDHE83DeGHfF8TFnAFKOrm6PPcb5YO7G011Hco2jdosLJ1D9HGzFljKNFJ7Pgwt-5tB66NiQyyLxNZQwEmpsPeqn48j8nIDGYDniNTAsJwMoQFFiYGW0xXTzGSk7fjNEmkPES2h4Mw1D_kaAliBZ2tJ2XUOUBM02AdhatrewoRlligoo09ekpDESD_9J9LXsrRfwQvLhHaUlRPTNKcUN_Gv9IvS65waEpurPWt-89mvOHkJH3aSxeRZatOcczToWPfXq_ybKdVIRLrXAL3FxAqngUELrNZEx9ZwGOW2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 170K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 20:57:42</div>
<hr>

<div class="tg-post" id="msg-78119">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مارتینز نیمه دوم باید رونالدو رو بیاره به بازی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/funhiphop/78119" target="_blank">📅 20:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78118">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نوس با قد اندازه کاگان چطوری با سر گل میزنه هی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/funhiphop/78118" target="_blank">📅 20:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78117">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hxh9wQdzZ1qROUAzkOQcbxFgnnNMN3Jx20kh3REqX1z26FQgDdTDfPIEvaV9-x_NG2_VgyNNoTXLOXBLnZtDfhqY9g23X5-MQmCccrVxas02JRB90wPgYAz_7CH-Mev9f147SaD64oktRTbTHQm7T_BfFERkPRQZFKV3rRzUicrgHuwamBndEILivmAXgAZtZ6ifW8qNgk8DG2fZ6Of29TPLHPHK52E6D76e7x5ZuvcuYAlaLqGLrrQPJHQnyFxn5ezbX4JeQBSC-Sn7pnr2irFbzziyQ1KPyOmn10WC8czjzt56020jZT5eQG3JlcYPwjuDxabtIFOkKhDP5QDBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا عارف
تولدت مبارک مرد بزرگ
❤️
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/funhiphop/78117" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ایت الله جی دی ونس میگه چهارشنبه متن تفاهم نامه منتشر میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/funhiphop/78116" target="_blank">📅 19:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نه داداش پوری خایمال نیست اینطوری میکنه فدایی باهاش بیف کنه و کیرخر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/funhiphop/78115" target="_blank">📅 19:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مسئولین جمهوری اسلامی حاضرن هر کاری بکنن ولی نرن حضوری قرارداد رو امضا کنن چون اینطوری مجبور میشن با قاتلین آقاشون دست بدن و روبوسی کنن
فک کنید همچین عکسی پخش شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/funhiphop/78114" target="_blank">📅 19:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=chXD5j2tGqL6fvmFxLi83C4Ap5mO7mb-WydEpGb8FDf-nF1I34gWG02CVtS9OYChtcBzZ4UKHlEPT3zVKTvNCVobL62HPDgltFA9JpGoc0Kloao426KbaTML8dBGJFFppVLXaq4kQDF3h53lSVU_UEoa0ftlKpUeAeYg1BrlfxFtg0NajLnulwXH4rSSRddI_W_XSeYfjZmLHu-OAzoI8PnRrD1vZrgurB73LFTDVKdEecmt4vffCTFwJBZ_15wFxfRYuhgoc4pq5KIBBvUli_aQL5v1V-h7JpNUvDof3i3QNlD57GFUq9iMUKDHXTYOgXCUsqCOXvTolzeaolkhLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=chXD5j2tGqL6fvmFxLi83C4Ap5mO7mb-WydEpGb8FDf-nF1I34gWG02CVtS9OYChtcBzZ4UKHlEPT3zVKTvNCVobL62HPDgltFA9JpGoc0Kloao426KbaTML8dBGJFFppVLXaq4kQDF3h53lSVU_UEoa0ftlKpUeAeYg1BrlfxFtg0NajLnulwXH4rSSRddI_W_XSeYfjZmLHu-OAzoI8PnRrD1vZrgurB73LFTDVKdEecmt4vffCTFwJBZ_15wFxfRYuhgoc4pq5KIBBvUli_aQL5v1V-h7JpNUvDof3i3QNlD57GFUq9iMUKDHXTYOgXCUsqCOXvTolzeaolkhLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/funhiphop/78113" target="_blank">📅 18:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/funhiphop/78112" target="_blank">📅 18:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pGi1LD58bk_FJeQnEl61GaSF67HUWfwkQXhXSEYPYH0qjGRUq9ImtzIcX-C1nZpnmg-41dpKJW1PZc5DtzAQ4gchpg11TdppD0BooDPGdYtenOSucf2e6S0A0-T7EW27yRCI3ku6B3sUpuDaXAbb8p8KI0EEFhvPIHI2SRmeRPBte8xRNcWXEbvN0CobOJJ_f9qjqFbjZ0ybipCtkstePBouCWQG86OFB690Z9IbDH-4e0ZKhN2vB1k7YhUdXSyayNL5xRlBRpOpnpABvhfJGl9amuTm9U_ib0-0ayPKMZpMaVsEpxRISHOHArLsFdgdF-ogIoYPufgjJLhXhLwQCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uXGCy0mRrRF4M10r-Eju8A7c4E7rdNhEBlm9acvlRcnpsk3DZfRlvtrbVpbFqkxlwWwI-6YitAD7vbXZ7TNH0AhJDo5sikO53llTL-FnNrcYhX1uTIHtNkog1t4Y4IKqbQQvl2yaZCgcCPiCRBGdEIoNCNbIt6zBS54EqlL8XlHc36ix31xOARBkGNdt2JRdDIUgpkFwrDwYnOPPkgksuNZSUOgwISb9cjVeQ2Lj4OEhWUzhO3zrzJiW0wOkRFxSHKlH9JqRIDHwaVDL0MdZZomYBwS1vXhWdWzxL05hbDjO8eaanek9yghtZsaP43nuzBZGv0bAbSm7T80B3VZ5qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/funhiphop/78110" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/funhiphop/78109" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6YRmjF8AAjAbhHl4ieTq0w7bdsenJqYLEp_5vk0zzlX5_uGumaTa-3lKPppYNO8inbMGAlIBuAP8Rcbozj5PyTL7pfUHR3x9O-CDhJmZnVPbVxPv5bEmfCvpH85RCt7jkvvspJy_w-I25XuxTYWQokvfsGGQWC1Ax3MnYxqaS-U-arlYG_L9nnU3mMjTteqkeR8hO-3cxeDR8vG-xJPy7EdHU7WPD0lLQ18NGJx9DfNrp4UR1hHzQwPZCyy3L28-MGBs3LT_GIRF8LJxqVXzXynecnxVnaR5Yj1D87QasRL2b2MxGx3If2k5T8D6yVJvGKDnxWzlpT1lx9047GqYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g27
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/funhiphop/78108" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78105">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/funhiphop/78105" target="_blank">📅 18:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78104">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz0UvxgReRtumq6fTC95HzPilUzqp0s0kfyBpFABTavzTBhA0P_ECfBqH-bSMxENxG-ktRloZ4ae9Ovwrk4sON9MOm8JqREp9JsArpxGajAyFPX1X91xvmP5ihqkFFPCvKtgtb_CWrZTDOz-mXI_nujzT2r2s7-0awRndsFxDnTNOGIY8warRXosanWr49w7XwhYIvWFSfor9PgLej0RCc3ylbxoax9UdhErdsjRh76BpFDuPq2SvjAEyoDWos0cQWR819HoYXEw5FENPaZbb3Dephbg-OKMzdlEUfqBGKw_F-rNiznm9pVWIHCbl-FboTrXSZ66KYgUNSYVW7ac-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/funhiphop/78104" target="_blank">📅 18:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78103">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=Ixy6RVZ-xuG9x2ke03wEVdwYDMKcgaSfTuEUKLZFy5yW7YeBdEPjhxLh-xF091U6_UF6RUnm_rwNO_XLI4X5zBpNSNFg0rQYVb3CMnq_M0hLBNnQ4nLPCPpT_aeAVYPqgjUjkGKAToqUrveMzzvl0onj6SFs0haXbezG2a1B9QabEpqzfEff1mOqleNqlpGaQYVwQd43V3cmaUOzpOtro_qlmsCt9ajUqE22SkIb8g8Et-rrocj74JuWqVhT9L_QmmPUd91qb2lLaC2K6yaunkc6DEc_M95v1Cbc2xmPmBFwvmTMmze_eLu2GUgloA0SxbilPPb6vrd-fbbInA4KvzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=Ixy6RVZ-xuG9x2ke03wEVdwYDMKcgaSfTuEUKLZFy5yW7YeBdEPjhxLh-xF091U6_UF6RUnm_rwNO_XLI4X5zBpNSNFg0rQYVb3CMnq_M0hLBNnQ4nLPCPpT_aeAVYPqgjUjkGKAToqUrveMzzvl0onj6SFs0haXbezG2a1B9QabEpqzfEff1mOqleNqlpGaQYVwQd43V3cmaUOzpOtro_qlmsCt9ajUqE22SkIb8g8Et-rrocj74JuWqVhT9L_QmmPUd91qb2lLaC2K6yaunkc6DEc_M95v1Cbc2xmPmBFwvmTMmze_eLu2GUgloA0SxbilPPb6vrd-fbbInA4KvzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسخوش
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/funhiphop/78103" target="_blank">📅 16:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78102">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مثل برج میلاد بعد ترور سران نظام هنوز سرپام
😂</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/funhiphop/78102" target="_blank">📅 16:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78101">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ابوطالبو بخاطر این که گفته بود تیم ملیو دوس نداره چوب تو آستینش کردن و مجبور شد بیاد معذرت خواهی بکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78101" target="_blank">📅 15:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78100">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترام: توافق قطعی نشده اگه هم قطعی نشه دوباره بمباران میکنیم ایرانو
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78100" target="_blank">📅 14:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78099">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: بخشی از تنگه هرمز باز شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78099" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78098">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: گزارش صندوق سیصد میلیارد دلاری کذبه و آمریکا چنین کاری نمیکنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78098" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78097">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ: ایرانی ها به ریش اوباما خندیدن گفتن اون یه حرومزاده احمقه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78097" target="_blank">📅 14:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78096">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اندروتیت ۱۰۷ بار تو یه صرافی لیکویید شده.
الان دوباره رفته صرافی و شارژ کرده رو بیتکوین لانگ گرفته.
اگه لیکویید بشه و پول از دست بده، میشه ۱۰۸ امین باری که اثبات میکنه تریدر خوبیه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78096" target="_blank">📅 14:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78095">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/827713cec2.mp4?token=L4yL20JmJDWTQIARB-Na1I-fL0lDvnrML1HpeMbzf5AU0X0eu-yBCeWEZtJsyFL540eUt68GMjmVKz7toUqlJEXama7GC5V5CMFYn0_o3ZO1M3Dc0vkC1TRgvE-GUmz3AyH-0M7GiA-BRyLSb5vHjV6zlKhcbAiWp8x802VTraD5c3-LFOsVF9fZid7IfltCwxz6GPI51JFmCAn1bdRSSCWeVnSOELrFmZ8A4La1v1bRsw4U6aZXKY5YEajgIcpND5Bc1k92duM0dpGxl_FjJ1KLrAz0ES8TJXwpK4dEb8fR8LsoY4ELw73bPBUPhfZqozWP4sBE-TwplXCljKECvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/827713cec2.mp4?token=L4yL20JmJDWTQIARB-Na1I-fL0lDvnrML1HpeMbzf5AU0X0eu-yBCeWEZtJsyFL540eUt68GMjmVKz7toUqlJEXama7GC5V5CMFYn0_o3ZO1M3Dc0vkC1TRgvE-GUmz3AyH-0M7GiA-BRyLSb5vHjV6zlKhcbAiWp8x802VTraD5c3-LFOsVF9fZid7IfltCwxz6GPI51JFmCAn1bdRSSCWeVnSOELrFmZ8A4La1v1bRsw4U6aZXKY5YEajgIcpND5Bc1k92duM0dpGxl_FjJ1KLrAz0ES8TJXwpK4dEb8fR8LsoY4ELw73bPBUPhfZqozWP4sBE-TwplXCljKECvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاااارهههه تو موهات بلنده زیباس
کلی شیک و پیرییییی تو شب کلنگی نیم‌ساز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78095" target="_blank">📅 12:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78093">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZDfxx1x0MBHFawQPFtvVuMGuivm9TTc15Pl8DInH4Qkp6Hhh5cH4d3xDuF0IeXdumUmC5gDJsnZSWhvWVNJZ7TrOXftJpAM1EjRpL3J1Fg8mwEnBagCQzYWPcllsx_bp7b6Rj9QIVRKYNZnIh9MD_b179AntoaCnQp50eNV9EnBfcFH_qxtylAl7soqkNTrLLrX1sHc-BiIO9ZsJYjefmIQzF1wnUPP9keSZLPFGlULuC2TF392zhJWbfo1B_ISaI-xc0vqUV9Us53KqQ5Lt-Q87YVdEGdeRSMVItkcW4PAxxDglr9BI6CLHtn3sYPpLthWURqtC6-1gv7u6FebMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmJ3pG7KNt90IN6WfhMFedi24jEKuu_g6rUusdsadcS-T4h-LG539jhTtR9DJ5hCynJxljWer73eWZPD5xdk4VM2QkHgHti_7rJ10YVtQsGgGhqEgjCRrTKIojs4deoOsJqZ6XA-v8g9jLanUOvFCpWB4Ry1dRvn9WTlwp1kOUFVSqOFHHXFvXRhQogzXbAhRwUpMsnfsuLYecrt76pxbWXH_URfiInZkLHQcWdAQ9wD_cz3RK096Lhdf2SBIVYh6cOct4c-18V17Uwy5suxnDOr6gajhTRL_-FbZPcd2shfOerm5kv3cNexh45rG3jYPzdGkPx8zRcFIC8ht3kzMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این داداشمون هم به دخترایی که فالوش میکنن بک میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78093" target="_blank">📅 12:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78092">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA5e39gem9C6fC_YuRNr4urG2hxh0oGJhLOsQDUP8KnUPW88VuFMap2XjJFubW-GKkXoLYG_kLC74N6eKJjPyOwQn04JBiE7WhmRfSGPhMEFzSJqWRC2oKp-0XuzcY4H03ZwFIALnHdMQJ0FCjsFKt_skNiF3kA2hNPFCKzyQkCi0GHi3vnxcM333OB86vdBOkPn0aGtSxX5U1nDoz4o-OFVXG2ihFCcvO5y8gUa33wIEDst6n_Y6W2TeBff9tTzwbW6E6rOJmU5j67Ed_eE4_jXhN1s3jXyEvEm9Bkmb2gOXsHDNDMkD7PdgcFSrRkHtEE6qoIJKnOqfmp9KS_uVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی چند روزه زنشو نکرده اعصابش تخمیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78092" target="_blank">📅 11:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78091">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4Va2fyssAhQPwN6bzTb0qu53cwi0njJlK4t9cg0tR3PbCikENzGH7fONpB73a6WRJzPLo6DsUwO_DxsmFS3M23p4T-FuHFOPvBJyeOZ2jD1TzNaehETby3CT-suuVBk8jyGyd4rSMBxKgbRFIIVdZzCyCIVvztQuVN_xh_z4gUsHg87aSW1Xv2CrA2xjfEgRtvXabaTWvWGwhYxxBeywRP8b8Yh-kXh2_IINym5YsQMNtIetJgJTMOoHcYgKOUaQt_Kp9HXIlrmnHZj4Y8Bqrs3_g-7t92UaVX5VF5sPKB02PMsIq3nvBblMYFnsFvU_m8jezy0rK7P5SuTAMby7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت نگران مصدومیت نیمارن
واکنش خود نیمار:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78091" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78090">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78090" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78089">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC35lJKy-vuwGBUsa866sf_5YzrazZZW4NpKshLG5CMwzm3IJbFp4UxYXmOW7qsi3t-UwRyE94zTqBKHAYJCDFKEqFqrijoNhA3kfTl0rUKoXRcQ9myo0eLKxg-lZuawxAImDTHWpaBNv3RB471G-mYR60g9fWREE_W0dRGIUyOkKNF9n1zowBvEkoffi_bHkNpQmB5V3FzvtupOMl6bQ8Qkt1HqsSB71B87UXsiPBAPLAUwbma90y7-TRPuP86VJjJU1b9kTozetVRR3Y8CDcrPawe7fGI2CAAAVXIuOKcMbYF6Vbch5ZONlyN339z2i2gYqJXQBEkBYN2CnnZS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r27
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78089" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78088">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdF8VDkTJWpN--KXolwMVuGS9EwPFnqingotffNF2j5lulKwpBFZa53QrDSSNwgHRoMQQf_wK860F4Vmjp6OaWH_sTpbI23RgToy8721JU_tDmFljKgtA4YKu_DaoOgmVRgcD0BsZwOQsXA8iG3fLpTYRCGpxbT-04hJz4jmVtBy7QrcfdXVrG81TPtWVO7FrQcEAMcAkN1tGeggHK6D9vSzTIfsaRF0tR4HsD_NjOrs0ELS6VRNXKeklSoRXnbimyEzRie30OZPW_I6o_83qbsfUuyLJF3coUdh0wT1-Da6CXWC8YozZHRN9x-z1oJV2ReZwsqk9MGETv2Bra0kyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت پدر از پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78088" target="_blank">📅 10:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78087">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYx81fIi1ds0Aq46P3vslxSua8OUP9eDDF-Ou2fMsGeG4XwUgi1FDIKAMhmssBOoXTzaRSCfcDky1X9Xn-8lCtp6Kc6AUdu7HtnJAIkq2silaLPHDrTVGg5zIuuf3-rY3QxYn2fhR1HIowgtZuYx8zQvXO0dur_VFFqsiymDHY2VTVGdMgzaYmuEZCDVQhc71x6XelrASw9Go6poxvy16WvEWTNHZjS1seAjtG_WSMh_l4Tg-dgEPP6KNx8KwinLEdZZ0navWnDEElQnXzxixeKPjsuJOqgwYyFFP1k7w9kPzFfpZLLDMuDXjZUJj1KAMGVPZKCi7X9W4Y3ZuOG3OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو دریاب پسر، یاخدا</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78087" target="_blank">📅 06:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78086">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حالا رونالدو مصاحبه میکنه میگه نه ببین گروه ما از آرژانتین سخت تره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78086" target="_blank">📅 06:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78085">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پادشاه فوتبال تعویض شد تا استراحت کنه و برای گاییدن بقیه تیم ها آماده شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78085" target="_blank">📅 06:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78084">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نویسنده کتاب فوتبال هتریک میکنه
🔥
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78084" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78083">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گللللل
لیونل مسی
کارگردان فوتبال جهاااان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78083" target="_blank">📅 05:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78082">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بهتره برم اول وضو بگیرم بعد در مورد خدا و اسطوره بی بدیل فوتبال حرف بزنم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78082" target="_blank">📅 05:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78080">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بهترین بازیکن تاریخ چییییی زد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78080" target="_blank">📅 04:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78079">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78079" target="_blank">📅 02:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78078">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خوار عراق رو من گاییدم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78078" target="_blank">📅 01:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78077">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هومان بدبخت یسال موزیک نداد مجوز بگیره، تهشم بهش مجوز ندادن دوباره شروع کرد به موزیک زیر زمینی دادن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78077" target="_blank">📅 01:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsNYvwWKrOAdFvNZptdUMmej7DdkUwJqegrLj37tB7_qCbg_GZRLxV2cd_5Cyv3P6wV6GtuwZ0hEN1AxAIvOqfwbvdPbb-7GY40Dp3zDbSkmz2pZe13cnpMzrQ3lQQVcT8H22ObNXJp-21kNRIkf_t_-1sxjGLMPNJyApQs6Mhon1uTjGTA7TDFML3zBBPDLCkZ0QPQ9hYUri9p0FN07e1pl2euxGqdZ7_oreMWdQY0_kQ8xm0msTt2J2Wj9-ED_eY02-09Q4Zt6m2G2JLwPcyLWmlhepK8qhyK5spXFJ_wuq9UBrfQaS90lB4qreYSO3x3z2HFDhHYDTQ8BZiEIsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا از مزرعه‌ای که توش کار میکردین خجالت بکشید، یعنی چی صفر کارت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78074" target="_blank">📅 00:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78072">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قبول دارید کسایی که جلو اسمشون پرچم گذاشتن زوال عقل دارن؟</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78072" target="_blank">📅 00:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78071">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fsb0Z--eu8nYhvSsbUszHK3fYjSo_Sx6SjG_wqaO7sdTUu9j-hpYT8Bd5XBQg4BhwqTAM4eciHuuXPoP9HL7pvUAviPO0lHCsdcrdqYHDpmTWWrUXd7bPq3DUM_rqASJI3T0vOqIgJaAYJ_aLhHrrBU1IuEE7pBUwDK21kojhqm4Ud4cM66IvAvU3axGhJrwf89xe_N9GngbdFq9vmQI2z03RdFMrGom4oZT2lFAKfLtJa6APpIR-GXa8rMmbTU02hMRw4npEclbwjG_w7SbPCO6YSyROMYJ38TvITdjDSFDAlJ-JPnCy2fgQ5z5WW_dykFiscmc7uWnUOL2VKedgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78071" target="_blank">📅 00:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78070">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78070" target="_blank">📅 00:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78069">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78069" target="_blank">📅 00:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78068">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78068" target="_blank">📅 00:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78067">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گل دوم هم زد فرانسه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78067" target="_blank">📅 00:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78066">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این جام جهانی احتمال زیاد امباپه رکورد کلوزه رو میزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78066" target="_blank">📅 00:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78065">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چه‌ گلی زد سنگال که رد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78065" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78064">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امباپه زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78064" target="_blank">📅 00:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کیت فرانسه چه خفنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78053" target="_blank">📅 22:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78052">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پسر اسکوادو نگا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78052" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrI2CvQtHtQxp1wDyDcVvYTyzW8JJBRFZqgNJ_xRPiKRMBMN3qRxaeTdheYCtmrmTJ-1ssiMXpg3F9u6wL8jfV0XcbEuLLsV2akBFPQJXyDEgc77pIk8zQOdY4SqvLKXJIBnhM-tNsqnqDclQOnWCd6Yi8DSW3Kew_IjRWCCbSBw1mESNYXogg5zTA5_tW35jKm1vuLsJTPbyEWY0Hki-ePLrqqXw10Li1js5Ndtv6STiXCpo4hFjBWPPgkHLBsFp_Ru9aw8BJ6n1RJDHV9io-Nlbzi3XlX8ywv02hdPnkXCjbBP2mpgqCZxcYDnvXdhxrjjHJ5pAyEaqPbVQnd0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اسکوادو نگا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78051" target="_blank">📅 21:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نامزد های انتخاباتی در اسرائیل تبلیغات خودشون رو شروع کردن
و جالبه که همشون از طرح هاشون برای دشمنی با جمهوری اسلامی به عنوان اصلی ترین تبلیغ استفاده میکنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78050" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78049" target="_blank">📅 20:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbSKcDh6gd4QQYZ0-u6Y876okXJwjhNnL2FTrsODuOFg_N3XiPs5MYTy6ENbFcgoSe4aT9mC02qJchhIIlA6Dz2vfy1Whivm0S-9ZJqUYO1JdBKzS-YvntrhnbWCeiZvS5nRNrI48aOtZarOuqFno6MHD9i_NUyBHac8tgK7wiijQitIMnIakQ3D5T9gQv3BgMnV35C8ldCVgW7RpKGXReAyyZdxAmypFv8HXSPDSIRjPdVyNK6NnCSG7KLbrQ2oFS8ISzufOaiVOkLckr23agyti3oFgp5ykMuezQBhQEmPN2wU108buGIs_ciXhJaAMFAKWWgiusel-_T8OgjEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78048" target="_blank">📅 20:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وال استریت ژورنال:
یادداشت تفاهم آمریکا و ایران به ایران اجازه می‌دهد فوراً فروش نفت را از سر بگیرد و ممکن است تحریم‌های بانکی و بلوکه شدن پول‌ها و محدودیت‌های حمل‌ونقل را برای تسهیل معاملات مرتبط لغو کند.
طبق گزارش، این توافق تسهیلات تحریمی گسترده‌تری نسبت به آنچه قبلاً اعلام شده بود فراهم می‌کند، که احتمالاً صادرات نفت ایران را گسترش داده و امکان بازگرداندن درآمدهای نفتی که در حال حاضر توسط تحریم‌های ثانویه آمریکا محدود شده‌اند را فراهم می‌آورد. (لبیک یا اوباما)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78047" target="_blank">📅 20:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78046" target="_blank">📅 20:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqDGjkli96ftPFBpVEE2cyBg8ElFe8cvN5cIirQw0NYrOW9AWpf1SlJyd4VKQ8Inj4oYsz1qUwXLKOdkLaO1g_-RA93njxbxbACXdEe6F36r91Kntj2Q8BSovDlHHEneI1EzHai5OnDHGy1fdTIHFRBiZsY2er59NBSPIYw3UaGhKI2anqpTSZGHVM9Ezk5Zknhdd38j8L2JCmxZW17aM3pryisBgCeWaMEXkD523QRPdhnZL4YCV94EpSFVelN6uZUdjNwgp6HjtPGgURY01h5Zh66cvXc_1hZbeuWv9ppRhF62uKhyshcVd5TXXtFYcpjX-I1YweEVSZelOFPhLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله شهربانو ازت میخواد همین الان یک لیوان آب بخوری
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78045" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjVI5tbQZOS47cLQYAuVBy-KTzoOzavLB4Jyp1Z3Bh1w8ACQPsh1my6dzYoxMQUi8mV8YzKvpFOpItFPgBz7BGktJkZu3uBrjD-Xdv5SUZh729GlPkbeyd3hfjQGwgqF7TZMfBF3CCvnqz_V-HNArlb8tgcHYUyy4-3EgFrunL9roUFXku5mzK70YyKaHZJInsLiGjwK1Bsx7kOPU-AY5s-41YJJmCRlCNRV1FaSXJutUCsdCWf7s4foea_GarIqXXVhjsHSy5Zq0o0w-Nl2hA4_dhKFGT3Rbbl6RqX1WMPo7IoNMb2QXGT9ECZQ_jNsSE1Z4OqffiFkKRto7nX5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوکو خدا به دالگت رحم کنه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78044" target="_blank">📅 19:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9rEs3f0Z6P7XwTEcgcdqBGkSwjzy0U_Lgg_i_B89m_uWvWShVwPItIoSwnUUA6mD6v3EO1YEGOn14QqmBL61cpMyoESz9UNu-vNSwbJgeZnZWAoa5tGr1R6mah_aAqNqS_uwP8Smj7FV048ZTVT7EChYcN_WsxACA2eNrW4SGl4PaYmrglYIybV8hmHYyh9AsYpBBBBJkuocaBLdGTCJSqRg5g_AZFz_5FsYfOM0SahTIYmX4TEgkAQd3JHY6bVJsgSToH_XFDfjpFXICJS3Bq4cGZJP-yU59Pet8AtMRmJK1D7ifbfKVoaKY0OmJLp2vmxCXycLmzeZ35etGwjrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78043" target="_blank">📅 18:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSQ2C3N0r7jzLnFEl6__KdCYLGHvospU9bqyTjFyrcxwz0suQP3Lp8kdUU1TYCg81woZg-dm1ZQmBi4kSnJxzXOK5HJF1c2L-7cJ9r1O5P74wh4SmQBXtrKs1Hm6lhyFIcXdDStNAawO1kAM0y5-7I73esdUHZgtISrXBbcPSYyw-083jqXj_a5URAU2f8lavQ19isyUYbc_OFRJRE_a86nd7noxyJ59J_NjYQEeGIr_P2Fzuqb21Tgo6BfdIlr0sETxWjslLpJYUfEgIM5EHkWxsnQqlNJWURVMzenfyswIg3l7eR5ytpISbdOVTlppajbRFDGjjV0qX1p6tIVkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همیشه تو قلب ما میمونی
🥲
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78042" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78041">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78041" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCin0SrFjojjpIjysRggcKeLX80iM2FWzB_VbxpPgYMoAHQEUtWrAE1k76p73pbDRxTsQGbgrPiQ4av0qQEoBrkZFSZ15to9pA_UHheUoaQpw6CyKnyz3AEgSLszJF-h0ePURCrc-c-Rzuu2ApRsYGdeJcoEFdVpyQHS33xt351NfhFBoqmtlwNHPUGmfY0Ccn-KB90KR1EVKNzcBOIk9PQchNNH0W1mibSKe2JhxRCnRiPNIAiWu3XwrZKXY6uHN_e7Vfw24K_n_hmmrWLGU5l1BwApapoLpNsV-NMHdtdd58kV7UyLeTK0CALBqci-u4wBh5RyCd4zNy6pY9RRxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g26
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78040" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده  باید ببینیم تایید میشه یا نه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78039" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78038">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بازی ۳.۱ به نفع ایران میشه اسکرین بگیرین
👍
😎</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78038" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78037">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78037" target="_blank">📅 15:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده
باید ببینیم تایید میشه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78036" target="_blank">📅 15:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=TMOziWvV9gm5CUsQvb-mtI2fq5asTP4qzDd627ftlnwjgtCZVFTxdE8KUE384Uqya7paBGO69woKYszbdzE4nhX_S3i_BL_VnGWhyIifJa4Mke3eVDu_lKiLBFOTFy9jaHdDztcOf7qb5R115mXQy7Jsjf5g5m1QaVjxr8Kmd4aTcBLgiDpfZVP28FFH8pQ0OLVHurqQZYGtaiBpjS3FbJTw1XbYpvI3ic61-dMk8fC5EH_l2Afu_2uFxIazDtsAE-LJVXI7b7gYLLeEhqsYCOyDcniZiefndAfiX0KKRrnZFZQbJesLBVg3-GoDpEKLKPW6rJ2lqq2yDqttkOAZhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=TMOziWvV9gm5CUsQvb-mtI2fq5asTP4qzDd627ftlnwjgtCZVFTxdE8KUE384Uqya7paBGO69woKYszbdzE4nhX_S3i_BL_VnGWhyIifJa4Mke3eVDu_lKiLBFOTFy9jaHdDztcOf7qb5R115mXQy7Jsjf5g5m1QaVjxr8Kmd4aTcBLgiDpfZVP28FFH8pQ0OLVHurqQZYGtaiBpjS3FbJTw1XbYpvI3ic61-dMk8fC5EH_l2Afu_2uFxIazDtsAE-LJVXI7b7gYLLeEhqsYCOyDcniZiefndAfiX0KKRrnZFZQbJesLBVg3-GoDpEKLKPW6rJ2lqq2yDqttkOAZhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78035" target="_blank">📅 14:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-DKxB0kcUOSqyF6yB8wpVt5w_TYNiEuWzZNidJl6DQuV5q1SXTVO6G5XXdeT8DfSNspOqRBxbY_pFoC5SQhMG4DxYGFIhggCTd03lK_vN-7fhm0fiyVhvcm8fmXzLrLFQ2BbbM6p42zJWTbR-xkcNXPMbqjkDMRLs1GpU9ziolvK30mtTfZ_rUIzQKKDNFgNl5dwP69cCuxe0Hq5mcvhkjnVtFS7dFZDKpe-OFNG5AjR5RfSqQR-VBpuu2UneZfwe3lXFYGR9xef2tmpQ23zd5gXRcWlQayyRwI71kxiyD0iGbuyYae97jxF5MkrUNWp8v0Re_2eBrqI1SqlBkZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=bAAcFsEaHnOK9AVcPnK9sELIApQrqXZJY19lxybMPLjaJ80ecYmwNAs7bTLvRSkWC3fiRStrxI2CHiFWlpgFQKwWUmPWIuV69TG0G4IT-q0394kdahoDFidJb73pHp4YYAFbkvadAEnvEsuJtw-tV1v6RZ-btR9f1AwNvJnKipasmHrnxOt6wsR1Q344uumBC0edGYWsmci9-9--tGD2Awa3xRbXnpoCpk9vVSJzRtpPscyhNQ--IFubOufVwMmxCJTSAnUkjzk5mgkH31sKW-UoKILs4bQ8MjrYbLEoBAGT6XcAuGc86VDOKia8v1lEed6rr6Qfg9AiPRshWLjBEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=bAAcFsEaHnOK9AVcPnK9sELIApQrqXZJY19lxybMPLjaJ80ecYmwNAs7bTLvRSkWC3fiRStrxI2CHiFWlpgFQKwWUmPWIuV69TG0G4IT-q0394kdahoDFidJb73pHp4YYAFbkvadAEnvEsuJtw-tV1v6RZ-btR9f1AwNvJnKipasmHrnxOt6wsR1Q344uumBC0edGYWsmci9-9--tGD2Awa3xRbXnpoCpk9vVSJzRtpPscyhNQ--IFubOufVwMmxCJTSAnUkjzk5mgkH31sKW-UoKILs4bQ8MjrYbLEoBAGT6XcAuGc86VDOKia8v1lEed6rr6Qfg9AiPRshWLjBEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون وسط محبی هم داشت به در و دیوار شلیک میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78033" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suid5jwqZt8kI578t7lb-yW2LqK9aCuLcrf4aHfW6vYcqN2wpHFSrtN-UyPEbeWz0osLQI8G_E0oQYU1c5z29fLfYg7TmDOZklZa1IZQa9f-LcEJcele02a2aWACpN4QgTSHN-JR_59g1WF2RJ7zY2DudqEtulXD6i9vHqeZGyoc2F4imIk_egTh4NRtEhd9pWJ_xFlJ4h92tJ3TapPG1ZV01FDkQOGLq5D6zqhH1B03Q-r8f7OhG1u_us3hAFPlXt8zNFFGf6nFUO28RIjX-lSjqmoLZNfH7NBRWxCkReqOXBUSP_D_FjnG2s24jQKyhYmcjUwkqMjmVWSYhO7kew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78032" target="_blank">📅 14:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78031" target="_blank">📅 14:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78030" target="_blank">📅 14:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78029">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
@FunHipHop
| دونالد ترامپ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78029" target="_blank">📅 13:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حکم اعدام جواد زمانی و ابوالفضل ساعدی از افراد اعتراضات دی ماه اجرا شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78028" target="_blank">📅 13:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حسینی با یزیدی صلح یکساعت نخواهد کرد؛ قالیباف و ونس توی مراسم امضا حضور دارن.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78027" target="_blank">📅 12:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn3ypvJReIhhYK7sdsF_FtamU-FzP0oFHwErVpEWt60ntrQ4IL61qdYUwrbZUHo6dRnWsS12vUfY8Ws8mF8KiEDzKsBWOf-Q2-BepwgrJ3HC7_272ejyGnKldfd8rIwK1X6HaAk86w0KmgYWjWt-W8iOXThTnRwotLDsINfI7dH73uQE57JOk2SvV6ckzASWq_xsf-Xp9YPdTz4EVRhGALjIxcWOdLYlBmaUdf50XZf5Scuja9J3VtaZE9BYihPTC7xUSGqS6h29TWqkGG952g4GWseA-VLEZ7un4FQNHDuFqjgO0KRI2G9SzwPew1MfPFzXcn_IpP7B4lFPfNiRLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دلیل باخت تیم نبود این اسطوره بود....
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78025" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78024" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78024" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5XS08m4jBsII870DOFoRAXUs890_sGJ-W6CkyZbXsXNOLHF-xZdvvH6zRb1gQQFlfZWCNTpgn3Lb7AUdZb9aI0I93PLmqJo7y6RUTkKSqDln8erqm6nLOSASAa17U9TL0ygiTw9l2Xl3CBgCmcLF4Lt7j5RatAQc-l9gU7IJZZ2jqgFf5BTDN1Eih5G_CtiiXzgDJF1Qjt2dh8OUD3b7te_oKv_aCYToV3wLjyozA_AREU-jmj9FhnCWrHk4_mh_9yqQHsS0nYFDcKqe9rDE-QCLgopElHkCG-at4qCIxSzuDvFZBWq2WH02IV4Ev1j8u0NAMontzD2zh80bF08zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r26
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78023" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بیرانوند: اون دو گلی که از خط دروازه رد شد متعلق به چین و پاکستان بود و عوارض داده بودن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78022" target="_blank">📅 12:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بمب افکن بی پنجاه و دو آمریکا تو رزمایش سقوط کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78021" target="_blank">📅 12:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78020">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">۲۰۱۸ بود ساعت ۵ صبح داشتم از گل خوردنا تیم ملی حرص میخوردم، ولی الان تازه از خواب بیدار شدم نتیجه رو دیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78020" target="_blank">📅 12:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RncYqpLHtEUGca5yGZKm9Rs-j7F9Uu7OImac9H_967zyFkvO6RE5FzL9vZYbcMpgc0WTbyVH25ypSQM91f4FUU02PwGSFMbcg81BmZTQS0yL64dl6mciWsfndBSr2E6y-n5fql6XX6YDS3TCU1D8qhSTW-UkicVzcT1ApUtixcHpHu2nYJD78KWCcIobZtTnBD4NYN9Fd9fvquwTovrb7B2MeEBN-Fsfo7kmbQAz6L3L2z_KdNTVdXFQOCIxwsg3F3z2p_Opc6wT2O2F1tKgIl075cPYTmwLWUmlvxIMKYICZAypvTQ6HwhT4NVNYowBKd-JUDW5VPOS9YgjH5zraA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Playboi Carti
📌
I Am Music (Deluxe
)
📌
I Am Music
📌
Whole Lotta Red
📌
Die Lit
📌
Playboi Carti
📌
In Abundance
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78019" target="_blank">📅 10:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duLQB80GMY7e80z3t5zB97EjsXKhDL_s8qWomkmht1EHAuKCX_GofENsAPstmi3EX2aMFrET5H-EERTA9QAGYyY_Xd0AQWKHu7T7VHtYhvlLmTrwdPqNdjo6d3hC7NX6ynO_jGALigKg-LxQy_h439JGemYAZ2YRb3hcqm_YEINo3zaBJTqoDapZeqtDPz7F9MH_sHL3hCN5M2zhU-r-Kd_C05sKVi7SYb1JfJw6D2hYmh9rp5mg248XfO70YncMC089LuCoUQlMdj6THPKdcLdV04dS6t8ApLGA_igoIw3oYepUVmw-b49R3Y1nsfWuhPc3R7L_7GiWlL3uXkhTBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sieTr2udgg47aSlfiPHi_cPZL1BJzHe1njJ_Rfley7BjTmcRvfNBbjzXWKvu6-jAPIAsekChjT3HUGOFSuwSSyTSNbpvoOiMhQeE2XV12OxI_hPYNKzGc4ef_24hqt8rApoi07yK4-Cii9e1J0pcjPC3FFMD3mCyRZsNN670RWyJaZDaTl19J1qoJ-UhN54AYXwD59lVK6gplUGYUl1q6NpYr5U99WEqT5UtW-HKKh0BdMPrPcnOzvSyIxi86WRZz5esj5X9Uhmk5do5SByZajJI3GYu0E_K7ItBQzevrQ0NRalBvsK8hQgxoRf4V0yfVnI4vWekKXcyawllKCeBUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78015" target="_blank">📅 08:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اینو یادت باشه که همیشه تیم‌های مدعی قهرمانی جام جهانی، تو بازی اولشون ضعیف بازی می‌کنن که تاکتیکشون همون اول لو نره. صبر...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78013" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78012" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78011" target="_blank">📅 06:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شوت سعید عزت الهی از ورزشگاه رفت بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78009" target="_blank">📅 06:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حسین زاده جا طارمی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78008" target="_blank">📅 06:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نعمتی چقد دلقکه
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78007" target="_blank">📅 06:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیوزلند تحت فشاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78006" target="_blank">📅 06:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">منو بگو که فکر می‌کردم ایرانیای آمریکا از ایرانیای ایران آیکیوشون بالاتره
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78005" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">محبی گل مساوی رو زد
۲ ۲ مساوی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78004" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">از توپ لو دادن محبی شروع شد
با ریدمان شجاع ادامه پیدا کرد
و با جاخالی بیرانوند تکمیل شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78003" target="_blank">📅 05:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">واایییی گل دوم نیوزلندددد
🤣
🤣
🤣
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78001" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">علی علیپور اومد کارو دربیاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78000" target="_blank">📅 05:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چرا سکو ها خالی شد؟</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77999" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آقا مهدی باشرف (
😂
) جای آریا یوسفی به بازی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77998" target="_blank">📅 05:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77997">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فوری از سخنگوی قرارگاه خانم الانبیا:
به زودی به تجاوز نیوزلند پاسخ میدهیم!!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77997" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77995">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYOuW9EmTQ58ZVodZY3QxOnn2SRTzzdm42irbiHvyj565KheGnBe_ZUpDL8zncWJrrLNWDOZUiezVWsuxyB9wct4CBMkRxi8U7QjD4Hu9HyRzzbWfYiVCxXXD2_ZzledtM599npLvRQi5uFxHOSy7zEtqYjFWPzxfSit-eyojc1BEBxod1cEuOzG-ngFXVOrX8VsdKqXxqykKSd_Py7qw4jTFPZc4Y1nHLbJxFYiMeyeynusHcTsirennwsBbYmE_qg4rql2lU2LPJvapk2emjR0Hk4q13O5JFXbA7iTQA1mqnjG7JTTMmkuTLgCkpUaTdTcbJmAjKaIHePu7QKZKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77995" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نیمه اول یک یک به نفع ژنرال تموم شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77993" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ریدم علی نعمتی زد ولی افساید شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77991" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
