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
<img src="https://cdn4.telesco.pe/file/I10DwcWki_RFPJ_ovAkZ-_ruQ9qGz6iN3STHfR14Vw8-0BvbvAiwRDTmx_kO_qQNyLZSs28nld20BWRinF7IlDJ7NBImK5YDAuluVFk6jugzyR4LB7T2-CdyXiXP1nCLcly33-f_erSoPKoEZC4mqvQqTVJihH2NbCa2N68UIVBgCMyAx6iWXCudNKpzjEkqtRItA3DrmZ6trvO1u0UUDpSke3nX0vGBtkNig7BIoG2mivmQ8Jle2XFDmrB5bspdYMuHD0AOubzsS6F6OXDZEJoC08HaM7twMQf7WN79qbCxLWP3WYvxEs73bfmTu6syuZa0Em1XdeHA7-7l9rL-sQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.66K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🛡
آیا وای‌فایِ شما واقعاً امن است؟ (یک تستِ ساده و حیاتی)
خیلیا فکر می‌کنن چون روی وای‌فای‌شون پسورد گذاشتن، امنیتشون کامله. اما حقیقت اینه که اگر پسورد شما ضعیف باشه، نفوذ به شبکه و شنودِ ترافیکِ شما برای یک فردِ آشنا به تکنیک‌های ساده، کمتر از ۱۰ دقیقه زمان می‌بره.
⚠️
چطور تست کنیم؟
در دنیای امنیت، ما از روشی به اسم «Capture Handshake» استفاده می‌کنیم. وقتی یک دستگاه به مودم وصل می‌شه، یک تبادلِ اطلاعات (Handshake) بین اون دستگاه و مودم انجام می‌شه. اگر کسی این تبادل رو ضبط کنه، می‌تونه آفلاین و بدونِ اتصال به مودمِ شما، اونقدر رمز عبور رو حدس بزنه تا بالاخره یکی درست دربیاد!
💡
چطور نفوذناپذیر شویم؟ (اقدامات فوری)
۱.
پسوردِ قوی انتخاب کنید:
رمز عبور باید حداقل ۱۶ کاراکتر شاملِ (ترکیبِ حروفِ بزرگ/کوچک، اعداد و کاراکترهای خاص) باشه. رمزهای ساده مثل شماره تلفن یا کلماتِ دیکشنری، در لیست‌هایِ هکِ «آفلاین» در عرض چند ثانیه شکسته می‌شن.
۲.
غیرفعال‌سازی WPS:
این قابلیت که اجازه می‌ده با فشار دادنِ یک دکمه روی مودم وصل بشید، یک درِ پشتی (Backdoor) خطرناکه. حتماً وارد تنظیماتِ مودم بشید و
WPS رو کاملاً Disable کنید.
۳.
ارتقا به پروتکل WPA3:
اگر مودمِ شما از WPA3 پشتیبانی می‌کنه، حتماً تنظیماتِ امنیتِ وای‌فای رو روی این گزینه بذارید. WPA3 به شکلی طراحی شده که اصلاً Handshake به روشِ قدیمی تولید نمی‌کنه و عملاً در برابر این حملات ایمنه.
۴.
تغییرِ دوره‌ایِ رمز عبور:
حتی اگر رمزِ پیچیده‌ای دارید، هر چند وقت یک‌بار اون رو تغییر بدید تا اگر کسی قبلاً در حالِ شنودِ ترافیکِ شما بوده، دسترسی‌اش قطع بشه.
این پست رو برای کسانی که هنوز رمزِ وای‌فای‌شون ضعیفه، فوروارد کنید!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 708 · <a href="https://t.me/ArchiveTell/6682" target="_blank">📅 13:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd8t6vp568EB7fWZ-wLAJa0tHUbW4DHcZplkD-4GMagMcLDOxhZpBcBLc4P77xHmt3rSbqYepLcpnFcKnr4tABD5DzPbNgidKJc0NVSRM-C_FNBza-KPaXsLGyXNIM3EMEqMdPgFA292q70ZNpz6VdbQysLdpg6G_Pw9cGx7xmP03GX37RlmUyxG9NlkDwso51SjBZ4vZGwpeFn5mqWKs3qcErHUuKIpikI5kQRQNf0TSMo-EKkxz1RegiNSc1C5XZ-uSSdDI04H87PPpqpGEkNIKg_-dB4059s_-Rew9YcTumD27EWYmg2ZDN6kW_UYBta6m2mSLrdoBx3MHo_t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/6680" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است. با اجرای این ترفند، می‌توانید نسخه گران‌قیمت Ultimate را به راحتی فعال کنید!
🔥
آموزش قدم‌به‌قدم فعال‌سازی:
1️⃣
ثبت‌نام:
به سایت
gitlab.com
مراجعه کنید و با یک حساب گوگل جدید یا یک ایمیل معمولی اکانت بسازید.
2️⃣
تعیین نقش (مرحله حیاتی):
در بخش تنظیمات و شخصی‌سازی پروفایل، نقش خود را حتماً به عنوان
مدیر سیستم (System Administrator)
انتخاب کنید.
3️⃣
انتخاب نوع کاربری:
زمانی که پرسیده شد چه کسی از این فضا استفاده خواهد کرد، به جای گزینه «فقط من»، حتماً
«تیم من» (My team)
را انتخاب کنید.
4️⃣
تکمیل مشخصات:
کادرهای مربوط به نام شرکت، پروژه و گروه را پر کنید. (اگر با خطای «مسیر گرفته شده است / Path taken» مواجه شدید، کافیست چند عدد تصادفی به انتهای نام گروه خود اضافه کنید).
5️⃣
فعال‌سازی نهایی:
روی گزینه «ادامه به GitLab» کلیک کنید تا لایسنس آزمایشی ۳۰ روزه Ultimate شما فوراً فعال شود.
⚠️
نکته بسیار مهم برای جلوگیری از خطای دسترسی (Permissions):
وقتی وارد داشبورد شدید، به هیچ وجه چت هوش مصنوعی را مستقیماً از صفحه اصلی (عمومی) باز
نکنید
. ابتدا وارد داشبورد خود شوید، روی صفحه گروه یا پروژه‌ای که ایجاد کرده‌اید کلیک کنید و سپس از آنجا روی آیکون چت
GitLab Duo
ضربه بزنید.
در نهایت، از منوی کشویی انتخاب مدل،
Claude Fable 5
را انتخاب کنید و از دستیار برنامه‌نویسی حرفه‌ای خود لذت ببرید!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6679" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...
https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6678" target="_blank">📅 02:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDn0pslniY706ENcjee6InrLC4CraiLp8ikMEuHSsWdZEioEVPz8kPSTSs3xk5H6-F7Whq-F4yCPG4uHQtM9Tt0wtK8HwF5jP1KrDWzX6QXvtjzm1xzKp3Wml66PBp8TmQ894M7ilVxehFtuW0GGyQGLAWNzcjqKKH0aV2-R6D0OMlYGkwrEDZ_Omc3vWQZ0TmRSiOaRgwdhhwsHsicFbz6z2XXjNriBjZhpqM_37T5nEcgcSvY1dIbYJK_nFfyh50H59y8dhfhbd8G8d78sBKVF6CHK9hVuAKoZCxoUFGXj7lWBGik84NjX5TPbxzmO6DaqJrrPWZ1ADtHaLEVHJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توسعه‌دهندگان چینی GLM ابزار قدرتمند ZCode 3.0 را معرفی کردند
😮
این یک ابزار همه‌کاره برای نوشتن کد و تعامل با عوامل هوش مصنوعی است: همه چیز در یک پنجره جمع شده با امکان کنترل از راه دور از طریق تلگرام.
این سرویس به صورت رایگان در دسترس است.
http://zcode.z.ai/en
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6677" target="_blank">📅 01:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN58w0VDbQGTZKAgptbdY-PxEx1ezCkpCyRF6zikCoSFlpP1oUNiPAjhH0DgCFY1cP92CTRxTLOfwdgnbGm0NppZogPKiMSMJqWBNxG5ygtBPV7nS3Q4zcFyI0k_EqYR7t6q9a1nEnVIn3KI46fqfXoAfQ7_AbR9zC-1VcHlskJOqacDsAngIi8kr4QRo68vgsGutdaeOk1ywRttsTdddunxtJHdwakYi4vF-6moGdBqNxrxcqEwd0DCTrM45PonScgoBJMfNZbASb9MgZeNGbeUhd96K1sttcGd6jYM0s7-zb9mdtYDgv3aPC7M1wBPTJ1i79-igIZKFZ3F_lN2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت Fable 5
🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6676" target="_blank">📅 23:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=jnTzFrmMc-rGKVWq4U2DdkpnC6SQ6-_7uPrySOIdDA78Sm-w60SEvRNqfGa11ItjyRRnYzyB3xVsoWYBLFeVs09uReWf6RVa3DEiRc5aCleH4oTnuO8wi9QF9TCOHVvN_gzzm6bCTcg6sKRE4hv9GWkwj0ewX32JRCKJ1wxhjR2FhnaJXPe_KfEfjOqZRPpjA_OTqShoYSamKKubnHnxbZphJXUXK6c7R5T9MiaCxZK4az_757-MzI69vt0_oh0ZSyweZpRIPbuqa7Tj9nkv9RPIVzI1GbQiAomALYdYwy2qp53IslHEfEzvtuaKbZmfG8DnhLObuTiRStBSHwHTCRGYPdNzPRzxFVw64iT2iNt2UUUTH9NpXgCKP9dlPhDHs-GoZS4lEPgzpOYzqn5Fo7VZqI0nrWYZzbOmP0qnHFfefjK-OBPHsh8ldvwHRO1PnZ7c0P4g43MGOymbQl7dE4SPZX21g348jKjQkx3YLC3wD7cfRLwmcInZ-OLpyeUOzVjUc-sRy7gXhXwDw01ZQDJL1f2Wl0sA5L2prIld2-XIoTcM-Ft3KxxWDiG8aurQeDNeRMmJMNSdPQXnyflIaKuv6g4K27rbCkBqnjRFFuSOoklTBFTUDSD0ZenxpqpHXt6v-C31nMUGgP698ey8lfl2_geN2rQjRZcB9Q4p2XI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=jnTzFrmMc-rGKVWq4U2DdkpnC6SQ6-_7uPrySOIdDA78Sm-w60SEvRNqfGa11ItjyRRnYzyB3xVsoWYBLFeVs09uReWf6RVa3DEiRc5aCleH4oTnuO8wi9QF9TCOHVvN_gzzm6bCTcg6sKRE4hv9GWkwj0ewX32JRCKJ1wxhjR2FhnaJXPe_KfEfjOqZRPpjA_OTqShoYSamKKubnHnxbZphJXUXK6c7R5T9MiaCxZK4az_757-MzI69vt0_oh0ZSyweZpRIPbuqa7Tj9nkv9RPIVzI1GbQiAomALYdYwy2qp53IslHEfEzvtuaKbZmfG8DnhLObuTiRStBSHwHTCRGYPdNzPRzxFVw64iT2iNt2UUUTH9NpXgCKP9dlPhDHs-GoZS4lEPgzpOYzqn5Fo7VZqI0nrWYZzbOmP0qnHFfefjK-OBPHsh8ldvwHRO1PnZ7c0P4g43MGOymbQl7dE4SPZX21g348jKjQkx3YLC3wD7cfRLwmcInZ-OLpyeUOzVjUc-sRy7gXhXwDw01ZQDJL1f2Wl0sA5L2prIld2-XIoTcM-Ft3KxxWDiG8aurQeDNeRMmJMNSdPQXnyflIaKuv6g4K27rbCkBqnjRFFuSOoklTBFTUDSD0ZenxpqpHXt6v-C31nMUGgP698ey8lfl2_geN2rQjRZcB9Q4p2XI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
واقع‌گرایی GTA 6 شگفت‌انگیز است: یک علاقه‌مند صحنه‌هایی از تریلر رسمی بازی را در دنیای واقعی بازسازی کرد.
بعضی از صحنه‌ها عملاً از نسخه‌های اصلی بازی قابل تشخیص نیستند
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6674" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxlYVurrk-TZ_3G3e7kk-gdPLwsLQL9DPJLEB9aKNAp4ZsPwO74byGax8579pvESndrxu1EnadnXImHc6S9utZ2l4Ayfi59_l9snxjhDwBBrvK9zv3eUKQRlvuonMh89pN-d27Xh2yQMnHDYKo4_5kG-E8NwN3NMtAZ3A_ToZ6nsRxFPnqxH3toUeRMw0RGEvO6ZwppzzQ5s4xILQofimGYwA9H6XYUiTIRcaNbxZJbfryxMYTe-5WAPyOvGImhwo4kK5ImTmfVpI2sG9j1AxC40vqOZdeW54V07TsVFFXiEvMXnHj67dFqGt-VOrM7fO47pJRz_7hxE26zcMl8RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون هوش مصنوعی مهارت خودآموزی (self-learning) را به دست می‌آورد — عامل یک راه‌حل پیدا شده را به خاطر می‌سپارد تا در هر جلسه جدید دوباره آن را جستجو نکند.
🧠
وقتی هوش مصنوعی با یک مسئله مواجه می‌شود، این روش را ثبت می‌کند و علامت می‌زند که دقیقاً چه چیزی کار کرده است. دفعه بعد سیستم مسیر اثبات شده را دنبال می‌کند، به جای اینکه دوباره گزینه‌های ناکارآمد را بررسی کند.
https://github.com/Kulaxyz/self-learning-skills
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6673" target="_blank">📅 18:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOqzAqOEnFVk9nFJbLoIRspLqYfC3I4_rwWeRxWTYywPgPjisosYoGwbE-v5Kw3FHi8w4_qlTEWrgRrxYana4kryr4eXu6zAjCq0rGtXaZUrs_kCxBR4n3nAmx584UxzP38BJ8J4Xjrq64Yt9Vu2wvaeQ5eCXs9x7tdcEnz-oVVxHcpAoCM6mpk9m1oYISFmvB8ILqggzehdcLkwWkEYt3D1y9tuou2da05wI5WXsP352tGO_i_cowjZIJ2Jkk0Q7usL7O7LOFmU047kV5AwlNlI_bdFJTRA4S_10jFwZalMTT_oi43z__e-DEM0Oh4jTHgpSxH8zb2xBCB8g5zCFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RevPDF
ویرایشگر PDF سریع، بومی و متمرکز بر حفظ حریم خصوصی به صورت آفلاین است.
این برنامه امکان ویرایش متن و تصاویر را مستقیماً در سند PDF فراهم می‌کند و همچنین عملیات‌هایی مانند ادغام، تقسیم، فشرده‌سازی و تبدیل فایل‌ها را انجام می‌دهد.
تمامی عملکردها به صورت محلی روی دستگاه اجرا می‌شوند و حریم خصوصی کامل داده‌ها را بدون نیاز به اتصال به اینترنت تضمین می‌کنند.
https://github.com/Pawandeep-prog/revpdf-release
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6672" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=IeQPGOysnxBPmLyhM2QYd7cFWayOuyyj_678ZwXm7oRXPZT2wwQsPFwShUpCsy1Duga7hHNgThM1uJMl491DqNAe52RtOSRnZ3EN584TqfpmDNXTc_wp0TLMSECNCG3XZmoyHRcp2lXwUDEzMkfqlTPyKKypwBPaZF2vM9aWBaK4C6_FxdXcu5GOec4ddfGKzurXeU8jUQYuMk9xEoNMUx4W1js87LfeNiWBWn9XmISbd3EBrfFiWRtu6ZkKyEzwVtfSw04YoIibBl9MhOiWpk8ZO4EyD3mF1ydkg7m8dnPTVsb0OPPrWhT0S6R_9np7xpLpMmJKMqf7dt_QlKMFOau9i1xQJziW4KWz_YCknM6EN5zM1CgZfXbuPS9BQ3yokRVoH_sURhD-CC5CZ992t8zS7vNm32iC7rNDmiWBo2mPNG96Aowrs7oZVPHkVyUascQV1j9DPlmRMfFXX-yP9SxAumUkToQmv3tDZpDgryOLY1SxdAR1lYM6XcnUyk3Wg4pDL25tju-f3ckFDede58VsmwEPSMgZGaZsa9Ye1CT-GaVJjmnE52wrthCipKUM_reeQuLSw8cISCmnPlKz1NTBQX1bS2Wz7Aj8VD5rp8ZuTt62TlxM__MMz2j1uFjxL3t3Uq_ivmgxa5EpDxm7I57YWY4x-1fjUzXygY-XzHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=IeQPGOysnxBPmLyhM2QYd7cFWayOuyyj_678ZwXm7oRXPZT2wwQsPFwShUpCsy1Duga7hHNgThM1uJMl491DqNAe52RtOSRnZ3EN584TqfpmDNXTc_wp0TLMSECNCG3XZmoyHRcp2lXwUDEzMkfqlTPyKKypwBPaZF2vM9aWBaK4C6_FxdXcu5GOec4ddfGKzurXeU8jUQYuMk9xEoNMUx4W1js87LfeNiWBWn9XmISbd3EBrfFiWRtu6ZkKyEzwVtfSw04YoIibBl9MhOiWpk8ZO4EyD3mF1ydkg7m8dnPTVsb0OPPrWhT0S6R_9np7xpLpMmJKMqf7dt_QlKMFOau9i1xQJziW4KWz_YCknM6EN5zM1CgZfXbuPS9BQ3yokRVoH_sURhD-CC5CZ992t8zS7vNm32iC7rNDmiWBo2mPNG96Aowrs7oZVPHkVyUascQV1j9DPlmRMfFXX-yP9SxAumUkToQmv3tDZpDgryOLY1SxdAR1lYM6XcnUyk3Wg4pDL25tju-f3ckFDede58VsmwEPSMgZGaZsa9Ye1CT-GaVJjmnE52wrthCipKUM_reeQuLSw8cISCmnPlKz1NTBQX1bS2Wz7Aj8VD5rp8ZuTt62TlxM__MMz2j1uFjxL3t3Uq_ivmgxa5EpDxm7I57YWY4x-1fjUzXygY-XzHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
«اودیسه» نولان - تریلر نهایی. این فیلم یکی از بزرگترین آثار چند سال اخیر خواهد بود.
با بازی ستارگان: مت دیمون، تام هالند، ان هتاوی، رابرت پتینسون، لوپیتا نیونگو، زندایا و شارلیز ترون.
اکران: 17 جولای.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6671" target="_blank">📅 18:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuKII0iZSkSlNf1S-4cVDbr5z9rsR2bxvfziaxG3SIMn_uaWxfvIXSW6ONu4wQGafwLcnBKBXgNemaQ0K2ZNsXxJSVeS_E66R23c2LelvikGDZ6FlwQjID2Y4Wbricw-5TsPH67-2c8d2xoJlzgLEHJqhM6hOUBaDMMrlqaSgBEIcG7_Ealb5zqSbGOtUP0MEDdJFZn7ByyZHnmrEUCa0GMciIA1J3RyPly_aSD9j0PTD4d1jQdZuQeQzAfzfc_XoVSFByWT0DScHf9kUpfP6EEGzJvb6wR6ffSSrOAvS3Fi27fY5LKhxE9plwRUE7_hAr3HvcU5i7xtqpjj7FQGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض چند ثانیه هر نوع کپچا را در سایت‌ها و منابع دیگر رد می‌کنیم
• به سرعت بیش از ۳۰ نوع کپچا را حل می‌کند، رفتار انسان را تقلید می‌کند تا هر محدودیتی را دور بزند.
• با چند کلیک روی کامپیوتر نصب می‌شود، نیازی به ثبت‌نام و نصب نرم‌افزار اضافی نیست.
• فوری و به صورت محلی کار می‌کند.
https://github.com/clawdbrunner/captcha-solver
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6670" target="_blank">📅 18:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268d269709.mp4?token=hmK6HJq6XSoXHB8AdZKO8cJ3jOEydJBOxsOcC2clV67fVZ3HIQlcnXKl3Y8DfcI_L155ViBvvKnI5Av4TQ_tKSi8ZioJcJ9Hv5T4OaCBSsa6Bze3SboJNBMkCZLZ1Z4vKf23EIavpGKTZxbdbjhP-lwpBrrH9d1VFOhFI-PaVOJv30WWmnOXWteO2cBXqNVoFAYEf7qN8zY83y692Dtb_gt5Jb63tNiLrE7nrs8B1ufTg9GwXdh-BVvSBP__sGMI8jXDHscvcji1GufSxChke8gh9FxmIdw-IyCsQL35-9MsZy-2C7Ycln_mTqUsFjGXn5A48SVzFzWj7oD66BSeMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268d269709.mp4?token=hmK6HJq6XSoXHB8AdZKO8cJ3jOEydJBOxsOcC2clV67fVZ3HIQlcnXKl3Y8DfcI_L155ViBvvKnI5Av4TQ_tKSi8ZioJcJ9Hv5T4OaCBSsa6Bze3SboJNBMkCZLZ1Z4vKf23EIavpGKTZxbdbjhP-lwpBrrH9d1VFOhFI-PaVOJv30WWmnOXWteO2cBXqNVoFAYEf7qN8zY83y692Dtb_gt5Jb63tNiLrE7nrs8B1ufTg9GwXdh-BVvSBP__sGMI8jXDHscvcji1GufSxChke8gh9FxmIdw-IyCsQL35-9MsZy-2C7Ycln_mTqUsFjGXn5A48SVzFzWj7oD66BSeMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شبکه عصبی Gamma به ChatGPT اضافه شد — حالا می‌توانید پرزنتیشن‌های زیبا را مستقیماً در چت بسازید.
ابزار هوش مصنوعی محبوبی که صدها هزار نفر در سراسر جهان از آن استفاده می‌کنند، در ChatGPT ادغام شده است. حالا کافی است ایده خود را توصیف کنید یا متن را وارد کنید، شبکه عصبی آن را به یک پرزنتیشن آماده با اسلایدهای طراحی شده تبدیل می‌کند.
می‌توانید تا ۱۰ اسلاید را به صورت رایگان تولید کنید.
🔗
لینک
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/6669" target="_blank">📅 17:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvUVfC_A6PYsV21JHqBKNUA2Q1OdMK-ELsQFFCsBc8cYs5imXWOuCfvfLLFe82UHByB-ZX_AyAQLx40HWRKAT3MUpQJy3PDWWitCwExxyRzArxqVyddCyEN029zaUeMei-PCzymhYP9sohDDVXrprTRt0ir7EPdtC7ewilbyPwGRZkfv-c8xB2nkrUt7_DGToVCyCSbJFeL_SwJBNLxpOn8Q5Rl3iUGGR_0TcHVtAKxk_jrV08IwvrPcNQa8DIP-ZWHocUZWf7T2j7DOlMVe4ylwUKmabQSCC1N5VVj6afGmuns3cwHUhRkS9b7WHei6GNHHHrmKbylAg9c4u33l8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دیسک‌های بازی پلی‌استیشن سال ۲۰۲۸ ناپدید خواهند شد
بازی‌های جدید فقط به صورت دیجیتال منتشر خواهند شد. همچنین سونی فروشگاه PS Store برای PS3 و PS Vita را خواهد بست.
یک عصر به پایان رسید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6667" target="_blank">📅 17:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚀
معرفی Superfile؛ فایل منیجر مدرن و فوق‌سریع برای محیط ترمینال!
📁
✨
اگر از طرفداران محیط خط فرمان (ترمینال) هستید و به یک مدیر فایل قدرتمند، زیبا و سریع نیاز دارید، ابزار
Superfile
دقیقاً برای شما ساخته شده است. این ابزار با رابط کاربری بصری (Intuitive) و کنترل آسان از طریق کلیدهای میانبر، تجربه مدیریت فایل‌ها در ترمینال را به سطح کاملاً جدیدی می‌برد.
🔥
ویژگی‌ها و امکانات برجسته این ابزار:
1️⃣
پشتیبانی کراس‌پلتفرم (Cross-platform):
اجرای بی‌نقص روی تمامی سیستم‌عامل‌های دسکتاپ از جمله لینوکس، ویندوز و macOS.
2️⃣
شخصی‌سازی بی‌نهایت:
دارای سیستم پیشرفته برای نصب پلاگین‌ها و تم‌های متنوع جهت تغییر ظاهر و افزودن قابلیت‌های جدید به محیط برنامه.
3️⃣
نصب سریع و بی‌دردسر:
قابلیت نصب تنها با یک دستور ساده از طریق پکیج‌منیجرهای معروف مانند curl، winget، scoop یا Homebrew.
4️⃣
محبوبیت و پایداری بالا:
توسعه‌یافته با زبان قدرتمند
Go
که توانسته بیش از ۱۷.۷ هزار ستاره (Star) در گیت‌هاب به دست آورد و نشان‌دهنده استقبال بی‌نظیر توسعه‌دهندگان از آن است.
https://github.com/yorukot/superfile</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6665" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFhxY7jDfw6dbTMI38muOkPKQQYOp6deH3UcqSHNRUm1PLEmiMOOpmJecgG5gYHKs3BzDohyRmobTy7hYtGhqifdXft1_3NtVc-hZmZO7t73hnGNtVoW3V2SiRp87dgtpxdGVu8kFRkVYtNM3WyFAo2R2XGcyUbOEbq2_n13Fr59LGv0FYWL910JbMsbnZkZk_BM1P_dPDKfhcIH2iG7BpW--b0Z2o0oac3xWWnAcRCzpdGASJGds-HbjZVRd-yJ_XsVGma0UJQ9tAPJrvvI8tL9cdV1UyfpXhf6EmEDLKyiI89zP8xkum4XCIJKTkTweoQM_lhsZo5jPjNewor3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اروین یالوم خودکشی کرده ظاهرا
😐
اروین یالوم نویسنده و تئوریسین روان درمانی اگزیستانسیال</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6664" target="_blank">📅 15:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUyG8zdEG1vciH198wWBqHljTiWW2kYQ2ma8CNpOuVwP1oiewGI4wgWTNQKwP4DTdCIGSWMIcAV75fSLrC6lkldppzRPKUNmZ4jdLQTBNaKRVJkIIPjsPwjJAxLUFYaUCwjePTEaNAqvLN48BgPf_MwncSXHPsLbWaN7fiIY79CTYvsZqHnhw_FcWms4Jjr7CKOkhzX9qG06bCctLCBnfk55UWe_i1Jhn6OboeTN0Wc_ZswU9Xfr1XaDx2-xyZ1qibdsUKO3nJY9TSHUGvJHYg8a_0M0uMT2Rf_utcgFvo0VqpvFsg1RgKQee6UXWlVWzNXJTW161-Ur-rPpqNd7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر سرویسی راه‌اندازی کرده است که پروژه را از نظر سئو، جستجوی هوش مصنوعی، احراز هویت ربات وب، MCP و پارامترهای دیگر بررسی می‌کند.
سپس به سایت امتیازی از ۰ تا ۱۰۰ داده می‌شود و یک پرامپت با اصلاحات ارائه می‌شود که می‌توان آن را به شبکه عصبی داد و سایت را بهبود داد تا امتیاز خود را افزایش دهد.
https://isitagentready.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6663" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJjfv8wvdrJ7FXqANfh39r_tnS3nwJizf3wF93_lcJyZDsMFME1zv8EO7zxGhIdT0x447OnPnYJYfd4bZ3NrNTxnW5P2hHvvIYq51dIllgJ11rxO4Ku01oj7Srke6yqlJwjbVQyBTfumrvWmJBuxMV1jLCWp5v34h1aLf_OISGQ7nMJrXM6STV4j9jwxMTugQ1ntoInBAV-K5-SdJheTTsmjVZ2bhROfoJJTHuKO_ayyd7CcR5lPpWITyX0lPO_9DfoH3ZH6x853kM3nCWqzqzSYcF244UCrKKeaYaHNQAx461ehCpNlbfuJCF4CQOgzUjJPGbxGCztgAStSYCuuCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع مفید برای توسعه‌دهندگان: در گیت‌هاب یک فهرست عظیم از APIهای رایگان برای همه موارد زندگی جمع‌آوری شده است.
🌐
بیش از ۵۰ دسته‌بندی موجود است: از آب و هوا، ارزهای دیجیتال و مالی گرفته تا یادگیری ماشین، نقشه‌ها، موسیقی، اخبار، انیمه و میم‌های بامزه با حیوانات.
🐱
💻
https://github.com/public-apis/public-apis
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6662" target="_blank">📅 13:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dq_OJ7dDgUtVcfGWzW3vUQ1EbwBvO1wbav-jWFTc5y6KjC_tc1VNQnw5adn_rA3HVzfcdn-r2MGPARkgcCuUlAFaBywFBi-ve3p-djbJiz5vZNR6iAQytHtTrx03cf6x7jwtk64tgcI5-AZi8OqlCKV7yUwJxa_wWMP65ZQpjDSMd4Wo-B-qkNtGXchfghENLqGSCpA7yq7emAjHAapYpuInkld46FYUOi3ne47ilIAdORhrT5ANt7N-2eRUvJERfC_A01EeknIcgGARBpWQvEaGCGV5lTbD-149YCiY45Sn-O9WcwMkji5N1gv0fcMraUn3rxJgXwRPZ7mh3KBcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkjJWGijd5iVny95bjzaR-GsoobMQpgaLayGxXVb5fMnbMmQ2_m8OH_9fgPlkkq-Bs7M6pqEHS8-qYRAS1mY_1apmSp_zXbhokiLNSm5DaJ9Pd3MloK7IMsRkR1oSuyhpTBxVBXLbrz09VF4nBbMPCdyJ0TaV3HUNl5Grki1Cr_dyonOxXfr1J4mcYWK9LhGjNe6TXw3S_hULDOsy3R65hSBIBVtuosXcq5fqTipdaDk-m01Tj6fDNwqg5ZvhrTGQVpstutbvbP23BvVB2NPJJ7I2JB4_ydcxILyu2r6sKEIccw4SmzooMare-WboahXjm4_griCyFT32am2I0VmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsWNQQt6dwf6Ngy6igYoNM1mhBjVEhWlZwA3G71y811TZ_K_2MvqIYbaSupzzOMsMmOcodMSN-SY1EKW7IaGelcug6dRxN5afg6XJYYHQVDLkwE7VRZJzY7qxKh6XSyfe0jXXn8oSMEMBGuwGTlYNr64E0rFMTiAXLltMXac2CAVPQIgFZcBT-JnU8BpV-WDW2uMB5Dz8nwTANcoJKKNlMSA0W1u6sST9CuIemIDFs-FPtjozH7chfmrnDImiH4mFy7Qg8_pB1NyGAmiXnMERgmrF4l47P4ZXfA31GqlCRp5Ee11dn6RWCnf-A7IB0X62YHZJaQR62MY3NqmZ-HCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQDoNrEAXQoqbYeXsd-sat_HhyI5Y2I_DQk3E9qCzedP1QMgXDeNoNOe4WhkJLaY_7sH5OV0aj9-jMIIumDrMADbpImdhecyg_7i2Q_3XZegoXAXnCEBwgtbOUPKh_GYvZwucXUdGsK_fAn4kzwpWnj6H0swNg-IYlW_WJo6zcJrTda-vgpzgcxknzt2HDkXkkwV2fuOBHBiL2YQplLEb9Coacr4Z3Gsa3MvZLzfKjOADxjiVdN1g_Zk1GLPjE07GlZ_mmI8y2T2MWPl8LUN95zaNaIVaG2ooYskS0DVwNj9wmSfr2gcKaInUIv5hppSPAYh7OufW54EtCJ8kUHpig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">PlayTorrio
مگاتورنتی که همه چیز را دانلود می‌کند:  بازی‌ها، موسیقی، فیلم‌ها، کتاب‌ها و هر نوع فایل.
https://playtorrio.pages.dev/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6658" target="_blank">📅 09:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUdHdyolTReuy-tAgzH1A0xZDgUqVWceo4Ct_lOHAn4vSNkUc0p00ba8PzXFKVbU_u6SkBhYn_J8EgIV5haq2OZtU4ClIAwT1CQnY3wOFe6X9f2_m1LRpBLn7WQWqZIE6Yzp8CGO4R012fH7Xvr2RkT5C2-fYQhU9bm9LkWysslHlE1j7P0CXHyZE2JvmJmBQZRDuKmfCsCTVLO3vIA6UbPfR64Ip0JpbeKf7wBj3gJ0Y_XEKplGRdI9tqz-SaZGj7Do8eaxnNi5AHXMR9xeLV63K8dLurPPX4UiYeWWq3eV8gPz44LTSipIA-V4ib4_ELxgcBs-HxTE9bPWW6QL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود Mythos و Fable 5 برگشته‌اند! دولت ایالات متحده این دو مدل‌ رو از حالت مسدود خارج کرده است.
امروز Fable 5 برای همه کاربران در دسترس قرار می‌گیرد و تا ۷ جولای می‌توانید تا ۵۰٪ از محدودیت‌های هفتگی خود را روی این مدل استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6657" target="_blank">📅 09:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEh9-NTMrMeKm-TJm2kd_laaVNMkKdPQohlOteMRc_YDco8UC9WWsmOIIf6sfdvB4ESVZYo_fhbqheADxPymnUBC0hGTZpexcg3JMHegBoSM9md77a6EhbIJva9o9_7stjHcNy8XNJQt5YLLhphkPJvd84tvAVEEhZQKOouQ63l00rNOFrU7-VZcb7-NY2XIssPPujLhTLn7PaOjWy7hlS51Le88rmbpWhK5TsH06R10bOVcUiNIhYGoofTYQtYyJbTuoKAdlJfhy8T96WgwoFa0Cj5NhoOWxWiWdLv_JP--rzElNd_NdOEEAsr6t-ba9mqVrnk79EbK32p0POWwvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود اوپوس بدون سانسور منتشر شد!
توسعه‌دهندگان Qwen 3.5 را با داده‌ها و استدلال‌های Opus 4.6 آموزش دادند و یک نابغه شرور واقعی ساختند.
• محدودیت سوالات فقط تخیل شماست.
• می‌توانید هر چیزی، حتی ترسناک‌ترین‌ها را درخواست کنید، اما مسئولیت آن با خودتان است!
• به صورت محلی اجرا می‌شود و بسیار سبک است.
https://huggingface.co/DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-THINKING-HERETIC-UNCENSORED
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6656" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ArchiveTel
pinned «
🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6655" target="_blank">📅 08:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">درود دوستان AssA هستم
بابت خرابی ربات
@REN_WZA_BOT
دیروز معذرت می‌خوام
حقیقتا به خاطر شرایط نتونستم سرور تهیه کنم و ربات روی کلودفلر ران شده
فکرش رو نمی‌کردم که قراره انقدر استقبال بشه که سقفش به نصف روز نکشیده پر شه
😄
خبر خوب اینه که یه ربات بک اپ گذاشتم برای وقتی که سقف اولی پر شد بتونید کار هاتون رو راحت روی ربات دوم انجام بدین
جای نگرانی هم نیست تمام اطلاعات دیپلوی ها و کاربر ها انتقال داده میشن پس عملا هیچ فرقی برای شما نداره
مورد دیگه این هستش که خیلی از دوستان بدون اینکه پنل قبلی شون از کار افتاده باشه یا مشکلی پیش اومده باشه ده تا ده تا میسازن که واقعا عجیبه
🤔
خلاصه که دیگه قرار نیست به همچین مشکلی بر بخورید
و نکته سوم هم اینکه ربات دوم کمی با عجله ساخته شد اما از تست های خودم سالم بیرون اومد
اگر باگی یا مشکلی دیدین با تگ کردن آیدی ام توی چت بهم بگین
@Assa_7788
(بابت مشغله های کاری و پی وی شلوغ به احتمال زیاد پاسخ ندم بهتون پس ممنون میشم پیامتون رو با تگ کردن آیدی ام توی گروه بنویسین)
و عذر بنده رو برای طولانی شدن پیام بپذیرید
🌚
❤️</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6654" target="_blank">📅 05:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الیوم اکملت لکم دینکم
🚶‍♂️‍➡️
😂
(حس تکمیل پروژه خوبه)</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6653" target="_blank">📅 23:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6652" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9QmGZkDurHZwvVeIT-05RmgyvQ7ZpTiD8RLKrYXCt25XDEv91ymI8oP4oNneTIi19tvNdrQHR8sAxoiRDCHURPsmbUTiBB8WfdIL5s5mRZOdV5Bn9HLuIAGN3VNMynvBHolk3Ql6DInQdyEVCo-mjpfXkFU8-aD6oi1MLV9Zoe-0U4SYQVnwX-NUrqn1g2madu-sp_ycgN1tJ4C2ZO0gYZ67cvKAWeKDKtHKsHOlrMJm1Qabc_w4Wq4iB-ZkezLbpIqaltYOiPq0dZtZXw7FK0thLCCpY7TG1oagIIy7M2E8XeIcg16jURQOJ_OUpX3W9lXrgWfbaS7cY8qZZ1t2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=JnpHyg-Vc40</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6651" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFMail@ArchiveTell.zip</div>
  <div class="tg-doc-extra">471.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6650" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6649" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام!
تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک شدن.
تو این آموزش یک ترفند فوق‌العاده رو پیاده کردیم: ساخت یک سرویس ایمیل موقت اختصاصی روی دامنه شخصی خودتون با استفاده از زیرساخت رایگان کلودفلر!
🚀
این سیستم کاملاً ضدِ بلاک هست و می‌تونید تا بی‌نهایت آدرس ایمیل فیک بسازید و همون لحظه پیام‌هاش رو دریافت کنید.
🎥
آموزش ویدیویی و قدم‌به‌قدم (از صفر تا صد) رو تو یوتیوب آپلود کردم. حتماً ببینید:
🔗
[لینک ویدیوی یوتیوب ]
👇
خلاصه مراحل و کدهای مورد نیاز برای رفقایی که ویدیو رو دیدن:
۱. مخزن اصلی گیت‌هاب (برای فورک کردن فرانت‌اند)
۲. ساخت دیتابیس (D1) و کش (KV):
یک دیتابیس به اسم
mail_db
و یک فضای KV به اسم
mail_kv
تو کلودفلر بسازید. فایل
schema.sql
(موجود در مخزن بالا) رو تو تب Console دیتابیس اجرا کنید.
۳. متغیرهای طلایی (Environment Variables):
موقع ساخت Worker برای بک‌اند، این متغیرها رو دقیقاً با همین نوع و مقادیر اضافه کنید (راحت کپی کنید):
DOMAINS
(نوع JSON)
👈
["yourdomain.com"]
DEFAULT_DOMAINS
(نوع JSON)
👈
[]
DISABLE_ANONYMOUS_USER_CREATE_EMAIL
(نوع Text)
👈
true
JWT_SECRET
(نوع Text)
👈
یک_رمز_طولانی_و_رندوم_انگلیسی
ADMIN_PASSWORDS
(نوع JSON)
👈
["رمز_ورود_شما"]
ENABLE_USER_CREATE_EMAIL
(نوع Text)
👈
true
USER_ROLES
(نوع JSON)
👈
کد زیر رو کپی کنید:
JSON
[
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "vip"
},
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "admin"
}
]
🚀
مرحله ۵: آپلود کد بک‌اند و هدایت ایمیل‌ها
۱. در منوی
Runtime
ورکر، تو بخش Compatibility flags، کلمه
nodejs_compat
رو اضافه کنید.
۲. روی
Edit code
کلیک کنید و کدهای فایل
worker.js
پروژه رو کپی و پیست کنید. Deploy رو بزنید.
۳. تو تب
Triggers
، یه ساب‌دامین اختصاصی (Custom Domain) برای بک‌اند اضافه کنید (مثلاً
apimail.yourdomain.com
).
۴. حالا به بخش
Email Routing > Routing rules
تو دامنه‌تون برگردید. اون پایین قسمت
Catch-all address
رو ویرایش کنید، Action رو روی
Send to a Worker
بذارید و ورکر پروژه‌تون رو انتخاب کنید.
6. اتصال ظاهر سایت (فرانت‌اند):
مخزن پروژه را در گیت‌هاب شخصی خود
Fork
کنید.
در کلودفلر به
Workers & Pages > Create > Pages > Connect to Git
بروید و مخزن خود را متصل کنید.
تنظیمات Build (دقیقاً این مقادیر را وارد کنید):
Framework preset:
None
Build command:
npm run build:pages
Build output directory:
dist
Root directory:
frontend
تنظیمات محیطی:
یک Environment Variable به نام
VITE_API_BASE
بسازید و آدرس ورکری که در مرحله اول ساختید را در آن قرار دهید (بدون اسلش آخر).
تنظیم SPA:
در مسیر
Settings > General
، مقدار
Not Found behavior
را روی
single-page-application
تنظیم کنید.
روی
Save and Deploy
کلیک کنید.
ارادت، Bachedev
✌️
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6648" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سورپرایز امشب
اختصاصی
🗿
❤️
از یوتیوب
تقدیم به بچه های گل کانال</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6647" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLz_tLTUhLldryULPG_QEUYK24sj_PD3jYiFnbBvGHGMTz-jmTBSFJd6q8FnNnRputQZ1t21YTXTBds29nT9bguloen6JZQiFOrx6EjasFgENfATDt2CxcIqg9Wx2EhRjZqMuV6dghWA_s2ebhyOBlAnlwzufxTTUiXgEVf2i6kVD6nFHDZNJsw8FY1UGpwEwgxefpHU9GLOCY5cOnb2kewP02BzcT1ns-ZbE33iay_eD4qVv1POWicZpMESY89GJ-tZQjnBeWs9ssk0-wey9D2QsBrZEkJ6rIkIBmhD2aPwUR8CskOzwICkziz3Gv9COGTypzJ4t8raumVotQETQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude Sonnet 5
منتشر شد!
مدل قدرتمندی برای کارهای روزمره اکنون برای تمام کاربران، حتی کاربران رایگان، در دسترس است.
• از نظر عملکرد بسیار به مدل Opus 4.8 نزدیک شده است.
• به مناسبت انتشار، Anthropic همچنین تمام محدودیت‌های مدل‌ها را حذف کرده است.
https://www.anthropic.com/claude/sonnet
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6646" target="_blank">📅 22:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puz4bld2yP-hiX6PM7YuhPuK37E8P446VW1C5KhDk_wSvBR9rTswnumm5or16eZeKWfHBmGcYxQ1k_hNnsc6cGTG2GLRVn0JV1cg185f_ZhYwRT0JCOupBN5lJSDfdp32yJbrE8Oh9nad7dmrTd6GD7HacnOE9DqhQUkqIazU3XK5nvtcbA4vT4qVgXDP27fyidVpoM0KVJDiaexfClXSHjAWoev_8SoByXbXj5V7Y0IlZu_IQedagOyA3Q7KrywB0QP1CxEy619o8C8d4yJLfSgN-EJZ7Dx_CbvGEsTcc-3ucUoVD-FwgssNm7Scu7dMQOvrqN3PUbRaSVTuhdNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgLCIre1rKDqKgZUyd3ib1oNBuA2cXXDwLVu8rFnqwlg0gpCsdX6FOOX1qqLDTouUqxRDqQnOlTsIWYycYiGcmvSD58G54LhdNiyuXEhnMKxrAqgtHxoUxobybmddiEMfGmjoem77U02BUHWtxfAy36mw3pPTaNZmXhRbfJCtiNJBbjKs_Sd_W_y8FDe5yNitLkTu7ZcBX9biNsEf9cBAXNZ1BVyxbg-jWHZ2CiZG793BFTbHfuluCSFNzg4qCyH6y8fDkjtrhROoowFfHRVzOp5gSyJwQz_bh0xBwJ78e6psT7y2tc5AZDGH6-WInJvRS-0C4Uav2FRBWbYScH6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEPCNeH9reSPkQmtgNkz_u_piQl0PljtLal7jAn0Gh9bHjQA5YdMyBLlgjP1piKcBP2NcpRjBcMBmpk9jVJQQC31B85tgP-iYiZsz9HF7jtTpBucjMuuQ9X1PtTp8PIjVf6oFspmfttkMbef2YT3EbnX3SRB_ZVM82gL1vA-6_hlXYRg2PGHz6szMGV1QeWeevjfALUDBtHNesXJYnYWZgY1oQ7OfOs0ZmX2h56QDcKwUFVE548I6uQ0Xx1NUeS368L76WK-IcZrWxu3FrIIkuBUQD89Qq3IDvrRLuXP0YPwCEVk0vHa9-MODOjmcL6oCYscrYKZNSm7FUpj0Aounw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=qXIxV7RHjxGPHz9-151_DSG1yoL1Zrigg17fsYSBpzDDIux-ifWiPfN35DBd2s1IsWJAcy8vDsRyvctL41yBs3lHFTq1cr95BYf2bX6nQyygbXRzF8HQFHeMTNW3pcP6Ff48rIvFsCx5b-DuzHB3GBlcnd1sDrGmxgyi_EX6U6nSAiIqPS4wrg8TjMXITIdfd7KagCvUJqfZJeKzsSmWwiJuMyEB65WMVgZ3L-0b9PJKbePXRERVVZy5k1I9BhGLoQKGbSPDhsYHX6JtpGNbScFlJJ4Cli5jL45LaycsOZ71iky6P7zqis_2bpRRbBEatTqs_HC22v260GiYiCdK1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=qXIxV7RHjxGPHz9-151_DSG1yoL1Zrigg17fsYSBpzDDIux-ifWiPfN35DBd2s1IsWJAcy8vDsRyvctL41yBs3lHFTq1cr95BYf2bX6nQyygbXRzF8HQFHeMTNW3pcP6Ff48rIvFsCx5b-DuzHB3GBlcnd1sDrGmxgyi_EX6U6nSAiIqPS4wrg8TjMXITIdfd7KagCvUJqfZJeKzsSmWwiJuMyEB65WMVgZ3L-0b9PJKbePXRERVVZy5k1I9BhGLoQKGbSPDhsYHX6JtpGNbScFlJJ4Cli5jL45LaycsOZ71iky6P7zqis_2bpRRbBEatTqs_HC22v260GiYiCdK1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
تولید محتوا ارزان‌تر می‌شود — گوگل مدل‌های Nano Banana 2 Lite و Omni Flash را معرفی کرد، نسخه‌های سبک‌تر از مدل‌های محبوب خود.
نکات مهم:
؛Nano Banana 2 Lite تصاویر را تقریباً در ۴ ثانیه ایجاد می‌کند و هزینه آن حدود ۰.۰۳۴ دلار برای هر ۱۰۰۰ توکن است.
با وجود قیمت پایین‌تر، مدل کارایی خوبی در زمینه متن دارد، متن را به درستی پردازش می‌کند و نتیجه‌ای با کیفیت و بدون آثار قابل توجه ارائه می‌دهد.
؛Omni Flash مسئول ایجاد و ویرایش ویدئو است. هزینه تولید هر ثانیه حدود ۰.۱۰ دلار است.
از نظر هزینه، Omni Flash در سطح Veo 3.1 Fast قرار دارد، اما کیفیت بصری بسیار قابل قبول است.
ویژگی اصلی — می‌توان مدل‌ها را با هم استفاده کرد: ابتدا تصویر را سریع با Nano Banana 2 Lite ایجاد می‌کنیم و سپس آن را به ویدئو با Omni Flash تبدیل می‌کنیم.
https://deepmind.google/models/gemini-image/flash-lite/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6642" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E56yQ0S4bASkJiF2bWzNwohREIp_ABGGt-ipYEJsR1dTU72-L6GzKvYMHGo2RBGBUSTPkJwJWFsvjAgbuTZ8HUixC5WqCxcyFS-0aPvHfRI07O08h8ni93QbWaPPUibUgLLDcfAGv76MnqTaTZcwZoRVHS89m1pBGJlSrTYidGGuefU1esBJg8kzx_lEGvZ6Qg3WG6MgzNVV-a8RpjwTr2nKGqT8j8XbEB9QpCJ56UCvy2SYf0hTJw5DcAa45r58G1Z1OeZNmWopMa8UK2Ucxt4zdQ7cw7HuyCmcKmwh0yfzdEZJMO2Jm0v-90L4i7hd_F55j8KeeLT5tit0b-s8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی Opus 4.7
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
http://zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6641" target="_blank">📅 20:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=KOG7j7CZ5rczNJfUeaotOgTsaFhht0ZLQxMMilG9RHmDY0hEC9wp48QoPU77SwDWHrehw7yAbax7RK1qoTy2NIoBR6EpDHE9iLvGeoYQNFmGWT8wCyikK4JfDl5nFvCLvJbvSnImBwgTC99zFSEUpF06n6xINdAnWU2IHzywvxzvumzRbeeDIj8XVD09qFRLRp2Jqq-n-I5vkwAnfUcpVOxBZzZ-CEt9NXtTLRmruGpO9d-vOA-iiyY3AM7rT_8xVl1LDjvaXNtC9HjwVR9qJmRp7hSHY4tdc2Wa44OpO_uekOC7ZRfkfEcYBJi9vHpgH4jgbAjrwWClVUj6vmyBOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=KOG7j7CZ5rczNJfUeaotOgTsaFhht0ZLQxMMilG9RHmDY0hEC9wp48QoPU77SwDWHrehw7yAbax7RK1qoTy2NIoBR6EpDHE9iLvGeoYQNFmGWT8wCyikK4JfDl5nFvCLvJbvSnImBwgTC99zFSEUpF06n6xINdAnWU2IHzywvxzvumzRbeeDIj8XVD09qFRLRp2Jqq-n-I5vkwAnfUcpVOxBZzZ-CEt9NXtTLRmruGpO9d-vOA-iiyY3AM7rT_8xVl1LDjvaXNtC9HjwVR9qJmRp7hSHY4tdc2Wa44OpO_uekOC7ZRfkfEcYBJi9vHpgH4jgbAjrwWClVUj6vmyBOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقیقا همین‌طور در سال ۲۰۲۷ رم (RAM) خواهیم خرید — یک پروژه با جاسوسان هوش مصنوعی پیدا کردیم که برای شما اینترنت را زیر نظر خواهند داشت
😋
ایده به این صورت است: شما سایت‌ها یا جستجوهای مورد نظر در گوگل را مشخص می‌کنید و «جاسوس‌ها» در فواصل زمانی مشخص اطلاعات را رصد کرده و گزارش را به ایمیل شما ارسال می‌کنند.
https://github.com/firecrawl/open-scouts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6640" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-heScUubi1oIcCzCJCJAyCjh6Kk8N4aAUj31-9oCUl3CzDjNJfK8p2oXMW3otEqwSkgeuhqru_6wQ9LN7FybMJYERQKgSmTkNIxQjyYXI_UNJh1cSDQ6RceVwToNW1TsKjRAbbTke1FgKfrLQn_im1Rtc_P5KrQ_P223oorDVDiX_hfbcvdetjc7p9XAp4hTf-07zRBf3N8Twk5KW1meHf4FLOQhjjkh3xfMdtArCsA9vGcxd_6OmYzyrR-GUCS_RMG5To_KyKDHXzpotGXSgWvhtfgmAedB2OLDp8ZDjchob_oOpq85r-2wqoP155YvXPMZW1osr8y60H63VHoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DocumindAI
راهکاری برای تحلیل اسناد PDF است.
این ابزار قادر است حجم زیادی از اطلاعات در فایل‌های PDF را تحلیل کند، داده‌های کلیدی را استخراج کرده و رابط کاربری منحصر به فردی برای تعامل با خود سند ارائه دهد. این امکان را فراهم می‌کند تا به صورت تعاملی و مؤثر در سند حرکت کرده، اطلاعات موجود در PDF را درک و استفاده کنید.
https://www.documind.chat/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/6639" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHUvWxuhHi1kuZNXVKjdA1ZgWOQg_tXNDnNGn1G4PgorCWj-T9phzqI5XrogW-fsE9UCmmyjcwLF1B7xenzKbm6ZqktQcMunRbCghGBKin8a7V8uT3XS8YpSNKGC0ElHApm6woV9W2ocx_eP7tYYIeUtPBD5WP4JBkJQE22YqqOQ2eTIH1SMFp8z5JDveeaDipT-Zh04-fH04FSj6a_9I_HzCurRDdNRG3dTsjO8_zWuuMCevIgoqFI91I8jSGin-DlxiFsVpbR5O9UhWaGaX8_cOseASHYviZWEf_0UOt_2KeOGVq826Ni7F9oBExPePVh14DRRcstQOc5ZLVDdlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
نورون‌ها بالاخره دیگر هیچ چیز را فراموش نمی‌کنند — OpenHuman حالت Super Context را دریافت کرده است که بین جلسات، زمینه را حفظ می‌کند و کار را از جایی که متوقف کرده‌اید ادامه می‌دهد.
🔹
در هر بار باز کردن چت، زمینه را به خاطر می‌سپارد.
🔹
مستندات را مطالعه می‌کند، لاگ‌ها را تحلیل می‌کند، ایمیل‌ها را بررسی می‌کند و می‌تواند آنچه روی صفحه نمایش اتفاق می‌افتد را ببیند.
🔹
به طور مستقل اهداف را تعیین می‌کند.
🔹
به ۱۱۸ برنامه متصل می‌شود.
🔹
با سبک کاری شما سازگار می‌شود و به صرفه‌جویی در توکن‌ها کمک می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6638" target="_blank">📅 20:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjAHyihvDtp0QxJ7UI7MjCV8zpfpdWegKowK6iIhSYhmSa1J7pOp3ukhiPmoNue0BXew8ozo_7FR5FSNp8gUAiUqqaQ3nj72mkPwDr2KCf_IA8LThQ4PjmzoqLdp9Bu1psNNeQ8sKUZhPHx1k9hD4BE--3ynYtfrI9q-dKJOEzh6WzPDcJJgLzdeUWF-tF4t6kf6lWKqWZzGC_mQt7UWJD8RiNSh4Siejd7SfIzE7X9rbYESPYM0JqR9wmg_9BW-oj_s51FM6nx7c4SQmOBha4SarHByXu543w1XImLMyiar6fsp8vz_dckRUiuJS7coWojzoaiU3VMXzP9vFCnlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاک کردن واترمارک، افراد، اشیاء مزاحم، متن، برچسب و غیره از تصاویر، با تکمیل خودکار پس‌زمینه توسط AI رایگان
لینک:
https://magicremover.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6637" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4Wj8M02OyItSyPWVOIMFLBzW3ojsLcYZbGsH76NNrHDx2YVcO6Zg5EfcGC8CGWnZMG28Yr6DWFuZ1m2qUAZlj-K4F_c08P87_cvQwVWE3-V-gZFqV32rKEegzmbHNIeI94Ers2LsxVsTcXKHtjJ_jCKXx6O2oOGQWUK0jx6JkV0qlGjbIkB9Qtte6J7cBx64cR4nvXynCTTrubWn225CiPo78NnIkehpJzWNs2g7C34WruOjJhijfn1K5sCJMwTUXbXwVpELljhR0vPwbnl4cHF9cebpkn-AqgKdp88ddgzlucXAhsoKbD62nNX8KgdcParygclEhLKFWslAegJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
گوگل را دور بزنید! ‌NotebookLM⁩ رایگان و لوکال شد
🚫
☁️
‏نسخه متن‌باز و محلی ‌NotebookLM⁩ منتشر شد؛ دقیقاً همان تجربه قدرتمند گوگل، اما روی سخت‌افزار خودتان و بدون ارسال داده به سرورهای خارجی.
💻
🔒
🔹
چت هوشمند: تحلیل عمیق، خلاصه‌سازی و یافتن تناقضات در اسناد
🧠
‏
🔹
ارجاع دقیق: لینک مستقیم به پاراگراف‌های خاص، بدون جستجوی دستی
🔗
‏
🔹
تولید چندرسانه‌ای: ساخت پادکست، نقشه ذهنی و دوره‌های آموزشی از روی ‌PDF⁩ و ویدیو
🎙️
🗺️
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6636" target="_blank">📅 16:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-7zoBPsL6ZQ_1muaJIz5WlqvCwSoSlNBSwgmrtXTYMqcN9S8tbRhLK-Zb_85CHWFQCviGHhRVV_y4K3LmjXoUMxBWEbz4przmRXnXbpaFIjfqIFHF5F5_9F09_UF7wLpSCZjej-jzdVxBLpUS4xdI730Eqhh9wLodB3NPCAShRtd_ygaCq89K_QuNyrxC2tbCJ6VeaWt5G6EkxxD0WvjXbXJEqbA0Q4Nmq4USsqrnF9K4lWNJdE0yKHHpEbywcF4JPfBKM9Sco5BOfVMGoC9VyVaTvoVsYoLDsrj18G_Cm6dgs7VkDeHDfnOxFnpkrtT3_kvhxdVDpb1pcQExhmNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود فایل از اینترنت با ‌Torlink⁩، سریع‌تر از همیشه
🤯
‏این ابزار خط‌فرمانی، جستجوی فایل را برایت خودکار می‌کند تا بدون دردسر به منابع معتبر دسترسی داشته باشی.
‏
✨
قابلیت‌ها:
‏•
🔹
بررسی هوشمند منابع و یافتن فایل‌های سالم
‏•
⚡
نمایش دقیق حجم و تعداد سیدها
‏•
🛠️
دانلود مستقیم از محیط ترمینال
‏•
📦
متن‌باز و بدون نیاز به ثبت‌نام
‏
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6635" target="_blank">📅 14:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=G2GGc3r7R9AlXp6DGNbJfBc3OS51pp8-CMM79f9k84kLEsuHomuSXaEUwMi2YyBb2Ay_o5eXE7OK86F1xmh9uFsNNVwYKUrznIpybunb7P506sOugapaqAUobWHdtHaUPmiEIpHPG6mdSr9US-r86oP8tP-ZS1PhGRucytw4Y32_nFW-vzoC7dKLo1GC2CYUujudsImR7HoC138-2zFAj9Kgn8uVR64uAAQuP_3zq1Qd4_u3yx2aiEObndD_2x0RcBOsMmQrvZ6LJJSI0B6OwB22orkIokKEHVnEaFRpZK-Ag9aa0xUvMHZ_fThubCuoH1KXOdNKTihwEQBZFDmNeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=G2GGc3r7R9AlXp6DGNbJfBc3OS51pp8-CMM79f9k84kLEsuHomuSXaEUwMi2YyBb2Ay_o5eXE7OK86F1xmh9uFsNNVwYKUrznIpybunb7P506sOugapaqAUobWHdtHaUPmiEIpHPG6mdSr9US-r86oP8tP-ZS1PhGRucytw4Y32_nFW-vzoC7dKLo1GC2CYUujudsImR7HoC138-2zFAj9Kgn8uVR64uAAQuP_3zq1Qd4_u3yx2aiEObndD_2x0RcBOsMmQrvZ6LJJSI0B6OwB22orkIokKEHVnEaFRpZK-Ag9aa0xUvMHZ_fThubCuoH1KXOdNKTihwEQBZFDmNeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل تصمیم گرفته که پشتیبانی از API پلتفرم Tenor، بزرگ‌ترین مخزن انیمیشن‌های GIF در جهان را متوقف کند.
دسترسی مستقیم به کتابخانه عظیم Tenor از تلگرام، دیسکورد، توییتر و سایر شبکه‌های اجتماعی غیرقابل دسترس خواهد بود.
اگر بخواهید یک گیف انتخاب کنید، باید خودتان تصویر را جستجو کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6634" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhdR7EjQxvmOBesL6C8WrXSfqQjcWoY2GjNcEbAvx2BnW7omyFW6_Wr-ZSSofY7Mm0YDU06S2fM4fDr8Cfkj0SbMs7Du2Pw4fkHhMLbOXT9x5hw5V7aFhAe7bNpTt2lJj91c_itOQJFUrXAiDM3dGorLiteL0HCW_qGEKdzK8ReAQ82vtbqm2jNFQqNqoQnFgk5GOB_cyXLcTkCgCxjoUeJlp1qvsVaVa2QtX1cKfNottxqY8e_8QgMznogTQiGIvXNhYDtf9-imDkq1WwHnBggQ2aKFhKDi9Fwe_KEwjq0uaUusSBpypg_V5OO19-NVaoV_ZxaBHFMZJasf7r845w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
غیرفعال کردن ردیابی در مرورگر — راه‌حل ایده‌آل برای کسانی که از جمع‌آوری گسترده داده‌ها خسته شده‌اند و به دنبال حفظ حریم خصوصی واقعی هستند.
افزونه
Fingerprint Detector
در سه حالت کلیدی کار می‌کند:
🔹
شناسایی — نشان می‌دهد که سایت دقیقاً چه اطلاعاتی را از کاربر استخراج می‌کند.
🔹
شبح — داده‌های واقعی را مخفی می‌کند و آن‌ها را با مقادیر «میانگین» جایگزین می‌کند و دسترسی به canvas، audio و WebGL را مسدود می‌کند.
🔹
جعل — رد دیجیتال شما را به طور کامل با یک رد جعلی تولید شده جایگزین می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6633" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3Mwfu2YkTfDUkbaEOJDwBq0lR-6UOyTn28rfosGR3vDHOK46nmCr_Fanfp3x0p-v6phsMqsBZiOAElrGN7Z-_kRpgTHw0MnXlwWvCa0aLHHN0w3Q0_XAOAfRCqliPowZZiMqt8oxjMC_TQKTaPR_NHpuN7r4EoUCUFXXNLdDUFGArPhQa3EfuA6Mbbb2Ta0ni019OA9jv6AIuYFUcJ2GIuxrwdbcS1FumZ-EKEGYqbOWCp7fedy-neU_7zbfkyzI0W_0N1bYDEanoCC6BFdtsiHUG2_mVyaootudpu-ziBHkgnY6CXaI4qlubUmkv8EDmrLxePHjbxuIXiI32pOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
هوش مصنوعی بساز، پول دربیار!
‏فکر می‌کنی ساختن هوش مصنوعی فقط مخصوص نوابغ سیلیکون‌ولی است؟
🤔
اشتباه بزرگی است!
‏تصور کن یک جعبه‌ابزار جادویی داری که از صفر مطلق شروع می‌کنی و تا جایی پیش می‌روی که محصولت را به شرکت‌ها می‌فروشی. این دوره دقیقاً همین مسیر را بدون پیچیدگی‌های خشک دانشگاهی به تو نشان می‌دهد.
🛠️
‏
✨
چرا این دوره خاص است؟
🐍
مبانی:
پایتون و ریاضیات را مثل آب خوردن یاد می‌گیری.
‏
🧠
دانشمند:
مدل‌ها را آموزش می‌دهی و بهینه‌سازی (کوانتیزاسیون) را مسلط می‌شوی.
‏
💼
مهندس:
سرویس‌های واقعی می‌سازی و مشتری پیدا می‌کنی.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6632" target="_blank">📅 11:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این هم آموزش راه اندازی</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6631" target="_blank">📅 05:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
آپدیت جدید بات تلگرام ما منتشر شد!
✨
بخش جدید
Hugging Face
اضافه شد!
از این به بعد می‌تونید خیلی راحت پروژه‌های خودتون رو از طریق تلگرام دیپلوی کنید:
🔹
فقط کافیه در سایت
huggingface.co
ثبت‌نام کنید
🔹
از طریق بات، توکن خودتون رو دریافت کنید
🔹
پروژه به‌صورت خودکار دیپلوی میشه
🚀
⚡
برخلاف خیلی از گزینه‌های دیگه، این بخش فقط از
سرورهای آمریکا
استفاده می‌کنه.
درسته که سرعتش به پای سرویس‌هایی مثل Render نمی‌رسه، اما در عوض:
✅
حجم بسیار بالا
همچنین در بخش
IP تمیز
می‌تونید این IPها رو اضافه کنید:
🇮🇷
Irancel:
52.214.248.106
32.195.122.200
108.133.38.41
🌐
All net:
amazonaws.com
108.133.38.41
34.196.7.222
3.162.112.2
18.185.80.10
23.162.112.25
2.92.189.25
115.185.114.108
18.138.171.15
135.160.210.199
🔥
تجربه دیپلوی راحت‌تر با
@REN_WZA_BOT
💻
توسعه داده شده توسط
AssA
📌
سورس پروژه
⭐
برای حمایت از پروژه، می‌تونید وارد گیت‌هاب بشید و با دادن Star از ادامه توسعه حمایت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6630" target="_blank">📅 05:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سورپرایز تو راهه...
Ren panel</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6629" target="_blank">📅 04:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5oolhfKYFAMRNtyId8Ad-2QLRXN-l7rhBlwnDudcnM54dpHXGR4DgkeZDtsQt1Unu-CZdS-Gvyj1LVsMD27WKWmwe-F66ngcPz2iX-7yowERLnS5v28mCJ51OkqD8ACLrcDg-QtKfItsfKdRPDXJHz-brBRiu-mgt4K-GhdA747aSPeg_Vko8QP9PYNSoUltBH0nnWPASvtW5fTEfx1WtB2bD0PMRT1QsdyYeffDN6Xe7Tovuw3sv9BlpU9fnvlsPRk-SgNeClnU_wTMez4zUxN4HWAivWQOIn2tCsKQtBXqyuIFRl2csDhg8_eWwLMy2Ly95YCEqLqU0d0YriORQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتس‌اپ پس از تقریباً ۱۷ سال از وجود خود، نام‌های کاربری را معرفی کرد — می‌توان بدون شماره تلفن با کاربر شروع به گفتگو کرد.
تلگرام به انقلاب سال واکنش نشان داده است
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6628" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=VsPEcK4wf7MQCzWgeZC_1XyVVb18HjVTw8TK_7d-Vs8p6jFZFUbZ5YOJLu2KTPdUPHaFDT6wsONOQLnvUCZandzueTHf04tE5mM6SPuKjS_WLTU-N-H49SSQhn0vE2v1q2QfS_TGiNZGBHSLVBonOMaDlCXcD0QrdIofg5No4Z__ZSXPvCgahTyAqpatv6OWiBLfO6UDkae1ZNT5Td_Rig0jmKf1OViI6gef3OhZLfk2qu5UKZPkubJHPwra_m4Xn0oKqIoZMR6gY9gWK-6E_lWLMPBJut5dxGEpvHGr0YyWBoCFKxd46PMyng7sSrFUyTZC-FUfZnjWRM_yCfnl2iLDSKV_BRZUO-Jwys-NH1ea3NNEPpGpw1EOIT9WIXGaCM1UQu8wseAluUJ8dp7d8f-UJ0CWrVocPSxt7rkrLocjPxRGiS89O2K55UQurxp3Jo49-GvUQ0EyoDHcV-ndUih6itTc4oR3oTsD_1HOwRIZLcsVHGFqaUjbGTTGTu64SRO18pDauPhhDf1PuvBS6Uhvi2mD7byDPF72DpXmC3MzyxF7Pwq0oAGaf5E2UdkEBa-q3cq2pZpW6-zCQpNr08y2aPQ8-cgbm1MKlklQLC4q7iNgGCDAfw0VGre5Lf9ntLjZL3znqKhqJ0hWZ8JLVqSKXck_ivfCV8ZNSm-S3yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=VsPEcK4wf7MQCzWgeZC_1XyVVb18HjVTw8TK_7d-Vs8p6jFZFUbZ5YOJLu2KTPdUPHaFDT6wsONOQLnvUCZandzueTHf04tE5mM6SPuKjS_WLTU-N-H49SSQhn0vE2v1q2QfS_TGiNZGBHSLVBonOMaDlCXcD0QrdIofg5No4Z__ZSXPvCgahTyAqpatv6OWiBLfO6UDkae1ZNT5Td_Rig0jmKf1OViI6gef3OhZLfk2qu5UKZPkubJHPwra_m4Xn0oKqIoZMR6gY9gWK-6E_lWLMPBJut5dxGEpvHGr0YyWBoCFKxd46PMyng7sSrFUyTZC-FUfZnjWRM_yCfnl2iLDSKV_BRZUO-Jwys-NH1ea3NNEPpGpw1EOIT9WIXGaCM1UQu8wseAluUJ8dp7d8f-UJ0CWrVocPSxt7rkrLocjPxRGiS89O2K55UQurxp3Jo49-GvUQ0EyoDHcV-ndUih6itTc4oR3oTsD_1HOwRIZLcsVHGFqaUjbGTTGTu64SRO18pDauPhhDf1PuvBS6Uhvi2mD7byDPF72DpXmC3MzyxF7Pwq0oAGaf5E2UdkEBa-q3cq2pZpW6-zCQpNr08y2aPQ8-cgbm1MKlklQLC4q7iNgGCDAfw0VGre5Lf9ntLjZL3znqKhqJ0hWZ8JLVqSKXck_ivfCV8ZNSm-S3yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی با چشم‌درد دیجیتال!
👋
👀
تا حالا شده بعد از چند ساعت کار با لپ‌تاپ، چشمانت بسوزد و احساس کنی  به یک لامپ ۱۰۰۰ وات خیره شدی؟
💡
😫
بیایید روراست باشیم: صفحه نمایش‌های امروزی مثل آینه‌های صیقلی هستند که نور را مستقیم به چشم‌هایت پرتاب می‌کنند. اما تصور کن اگر بتوانی یک لایه نامرئی از «کاغذ واقعی» یا «شیشه مات» روی مانیتورت بکشی. جادوی
Paperman
دقیقاً همین است! این ابزار با تغییر بافت پیکسل‌ها، صفحه نمایش را از حالت آزاردهنده به یک سطح نرم و خوانا تبدیل می‌کند، درست مثل ورق زدن یک کتاب قدیمی و دلنشین.
📖
☕
✅
چرا باید همین الان نصبش کنی؟
•
🧊
حذف بازتاب نور:
صفحه مات می‌شود و دیگر نور چراغ سقف روی مانیتورت نمی‌افتد.
•
🎨
تنوع بافت:
از کاغذ کاهی تا E-Ink (مثل کیندل)، هر سلیقه‌ای را پوشش می‌دهد.
•
🎯
هوشمند و انتخابی:
می‌توانی افکت را فقط برای مرورگر فعال کنی و در فتوشاپ یا بازی‌ها خاموشش کنی.
•
🖥️
همه‌کاره:
هم روی ویندوز و هم مک‌او‌اس به زیبایی کار می‌کند.
به نظرت کدام بافت برای کارهای روزمره‌ات مناسب‌تر است؟ کاغذ کاهی یا شیشه مات؟
👇
💬
🔗
دانلود:
Windows
macOS
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6627" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اولین تریلر Cyberpunk  Edgerunners 2 منتشر شد!
🔥
انتظار داشته باشید که هر ۱۰ قسمت این فصل جدید،
پاییز امسال
پخش شوند.
آماده‌اید برای بازگشت به نایت‌سیتی؟
🏙️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6626" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حدود 900 تا کانفیگ مختلف
📶
https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Germany.txt
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6625" target="_blank">📅 20:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#اختصاصی
🎧
استودیوی کامل AI: از ایده تا مسترینگ
۱۱ ابزار برای ساخت حرفه‌ای موسیقی:
🎤
تولید: Suno, Udio
🗣️
کلون صدا: Kits AI, Synthesizer V
🎹
سمپل/لوپ: Stable Audio, Splice Create
✂️
جداسازی/ویرایش: LALAL, RipX
🎚️
میکس/مستر: Sonible, iZotope Ozone 11
🔊
پاکسازی: Adobe Enhance
💡
نکته: ترکیب این ابزارها فرآیند تولید را از هفته‌ها به چند ساعت کاهش می‌دهد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6624" target="_blank">📅 17:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaGBqGIVlSIbTnGoy0st2Bc_1TZbZDAc3vo3I8WwgeqaBYmImD-92_gWMWZ4w97k6ffS32laBk5pFF9E98WoHyn8EW6os6NzRCP5jAQxUl0wL4XMq4JNL5BA1wfVHEtBgWCjIRdRB4VO7BuVYuA2lG_yKQDdsJUjF8ixjmllKl4GNRUAPoRmP98JBKLqDlOetIQOaWi7ROm-fyB-U4ehOzwG6LHoebSqbsjCzEPE8LlL573VtXLUKP75M1IjdavFbES7uA_7rocgSkoCkUKxeK624z5QOElc0Dlhbu2a5NoUiETOkPAMTPk1_iwwDrvvsagj_j78mcUSx-s1ca0alw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GTweak؛ جعبه‌ابزار همه‌کاره برای شخصی‌سازی و بهینه‌سازی حرفه‌ای ویندوز!
💻
✨
اگر به دنبال یک ابزار پرتابل (بدون نیاز به نصب) هستید که کنترل کامل سیستم‌عامل ویندوز را به شما بدهد، GTweak یکی از قدرتمندترین گزینه‌هاست. این برنامه با رابط کاربری نوشته…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6623" target="_blank">📅 15:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین   بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .   irm https://get.activated.win | iex   اگر کد به مشکل خورد و اجرا نشد دستور زیر…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6622" target="_blank">📅 15:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین
بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .
irm https://get.activated.win | iex
اگر کد به مشکل خورد و اجرا نشد دستور زیر رو بزنین ( نیاز به ویندوز ۱۰ یا ۱۱ به روز داره )‌
iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)
Github
😀
📱
@Archivetell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6621" target="_blank">📅 14:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حجم : نامحدود
زمان : تا ۱۲ شب
vless://63b43d54-3bdc-4d9e-b3f3-10163c892936@64.90.7.102:8443?type=ws&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
وصل شدید بگید</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6620" target="_blank">📅 12:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvqjJ11VTYnl_t2zQv_AUy9N8EAAC92prwlaFQJqGQahKP3sSc-Qar2ljCOaepc1kv9y6LRXeP2Aghk5LdWT2dfvOzRYj3aR-gndzOJpv5NZsCTsZmXb_NxY0YOFRLrEav1KKnNw5oZdXvuYRXg-b6FztfJfqpm1MOJfemsvwmeEPgtCzUemV0v8CBpj2x2WB6I_fQLfXqzUbM-eeRzWIKa6wKL2pLPi5c-KJVpTAo_02l3DuNraKLzcFWasquwxv-UDldPneVlX1h6AW9VB17yhmK9S0EJJehhuLurbh_1X73H7bh4XOITPcO3kutHs_c9PMvvQyn5j755Kem2VjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه راه جامع علوم کامپیوتر: ۸۰۰+ منبع از دانشگاه‌های برتر جهان
🎓
اگر می‌خواهی به یک توسعه‌دهنده حرفه‌ای تبدیل شوی، این مخزن گنجینه‌ای از دوره‌های دانشگاه‌های هاروارد، استنفورد، MIT و شیکاگو است.
✨
چرا این لیست؟
•
🏛
منابع معتبر:
دسترسی به دوره‌های دانشگاه‌های تاپ جهان.
•
🤖
پوشش کامل:
از الگوریتم‌ها و زبان‌های برنامه‌نویسی تا هوش مصنوعی و رباتیک.
•
📚
دسته‌بندی هوشمند:
گم نمی‌شوی؛ دقیقاً همان چیزی را که نیاز داری پیدا می‌کنی.
•
🔄
همیشه به‌روز:
نویسندگان مخزن را مداوم آپدیت می‌کنند.
مسیر یادگیری‌ات را از اینجا شروع کن!
👇
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6619" target="_blank">📅 11:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjR7jOr9qo4bBC4vyk10Nztr00bWvyxZcUpY20jZBFtKWdk7deGD_UZezjk45aJbyegBpNqp64inmIQXEVbtYRpIw5Tr4mH377lvaB_SwTBZ082BL_2qYBTOn8-EpCWd46OMiPjB9pM1Kjh_7v2ag0Mh6wQQNKXdqwOV19t_1J3WrYXO7LwJAryWcm3u_9Y477xe0yvCmkf6-y514F7fSrlejnJTezhuQirhhyJIQAFdXc5Imkqv1yItd6CIDrbkDwJkAmkaCRr3ELnNxMwCFy0zPCOs53sjskCDPa6XCvM3gB0L5tA-xLSPV4EpBFhV7C8C9XSKuoWFGiFCpLfhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Anthropic بسیاری از دوره‌های هوش مصنوعی خود را رایگان کرده است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6618" target="_blank">📅 09:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCTELVaUWYtNq72J_k36_pwE1n_Xtgvf6wfDT_i0CxXCSnsDNfpGzvcPZvkms36yiTwF0PZ2rLHNbjV3lVi_lPOJet4-hOadIajSOCFgsmQ1HccokGiOayxnJomcDZby1HdbDXg9vszLCtTmhZ7tWKMD_QovSjBCaSDSFQ3rzw48W371frnKfO2lU2y3YJpElR1npaeV-D4V8Ts_Q_0OLzyMl0PDlZ99WMqRYIyNkjOOSXGzPxDpvTblpX5TOIECTh1-WTLdroB14Ajt2wF0Vh_H-rE60-XVsQccIvsm8pDCiWdWO4ITvlZUUapF3Sv2On88_u0Gci0wVBgMwGnX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">OmniRoute
۱۶۰+ هوش مصنوعی رایگان در یک API!
🤯
دیگر نگران تمام شدن توکن‌ها نباشید. OmniRoute با ارائه
توکن‌های نامحدود رایگان
، تمام مدل‌های برتر جهان را در یک نقطه جمع کرده است.
✨
چرا OmniRoute؟
•
🔄
تغییر خودکار مدل:
اگر توکن یک مدل تمام شد، بلافاصله به مدل بعدی سوئیچ می‌کند.
•
📉
فشرده‌سازی هوشمند:
تا ۹۵٪ کاهش حجم متن برای صرفه‌جویی بیشتر.
•
🌐
دسترسی جامع:
GLM، Grok، Mistral، DeepSeek، Qwen و... همه در دسترس.
•
🛠
پشتیبانی کامل:
سازگار با MCP و مهارت‌های پیشرفته.
یک API، تمام هوش‌های مصنوعی دنیا. رایگان و بی‌نهایت!
🚀
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6617" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">10 میلیون توکن رایگان هوش مصنوعی Mercury 2
🎁
وقتشه ربات تلگرامیت رو با هوش مصنوعی ارتقا بدی!
✨
✅
مناسب برای ساخت چت‌ بات
✅
دسترسی فوری و رایگان
⚡️
همین الان فعال کن:
🔗
platform.inceptionlabs.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6616" target="_blank">📅 02:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=vuXav1mJ4i35ccWHbIV6ibhqnJpkV1oW4rm3MAayzhFKsF8dyf3WWXy019etwKc1VcMsE_Nw09e1NFTqpHsLLnPLilGhFA0uKKJGrP0TIwiFAdNhECrazyvLUY6gXYZipDMf7di5NfjA6hZacJEwG_A3VEkY7HTFXsJSDg11JJLCFhbTrDIooAVCNohqirCn42QMAD3guCqNegmjgVnrAS7s2tPKzQWJthifBleNLiV79FCNDBKkOF48nlPR2uWGD_ZAEE5FlM_0l3uSA1WNFUyAsLUAYbZYcKYBRpKE06pYmvYLX0C9BlF8wqw1SY3gthK7frEdvgekz3xGz8W7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=vuXav1mJ4i35ccWHbIV6ibhqnJpkV1oW4rm3MAayzhFKsF8dyf3WWXy019etwKc1VcMsE_Nw09e1NFTqpHsLLnPLilGhFA0uKKJGrP0TIwiFAdNhECrazyvLUY6gXYZipDMf7di5NfjA6hZacJEwG_A3VEkY7HTFXsJSDg11JJLCFhbTrDIooAVCNohqirCn42QMAD3guCqNegmjgVnrAS7s2tPKzQWJthifBleNLiV79FCNDBKkOF48nlPR2uWGD_ZAEE5FlM_0l3uSA1WNFUyAsLUAYbZYcKYBRpKE06pYmvYLX0C9BlF8wqw1SY3gthK7frEdvgekz3xGz8W7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6615" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده و متن‌باز
PokieTicker
دقیقاً برای شما ساخته شده است!
🔥
این ابزار چگونه کار می‌کند و چه امکاناتی دارد؟
1️⃣
تلفیق اخبار و نمودار:
نقاطی روی نمودار کندل‌استیک ظاهر می‌شوند که نشان‌دهنده اخبار منتشر شده در آن روز هستند. با کلیک روی هر نقطه، متوجه می‌شوید چه خبری باعث آن نوسان شده است.
2️⃣
فیلتر هوشمند اخبار:
دسته‌بندی اخبار بر اساس تأثیرات مختلف (گزارش درآمد، تغییرات مدیریتی، محصولات جدید، سیاست‌گذاری و...).
3️⃣
تحلیل و پیش‌بینی با هوش مصنوعی:
با استفاده از مدل‌های قدرتمند
XGBoost
و
Claude
، سنتیمنت (احساسات) اخبار را تحلیل کرده و روند قیمتی سهم را برای روزهای آینده (T+1, T+3, T+5) پیش‌بینی می‌کند!
4️⃣
کشف الگوهای مشابه:
روزهای گذشته که اخبار و شرایط مشابهی داشتند را پیدا می‌کند تا ببینید در آن زمان بازار چه واکنشی نشان داده بود.
5️⃣
رایگان و آماده استفاده:
دیتابیس لوکال (SQLite) از قبل در مخزن گیت‌هاب قرار دارد و برای اجرای اولیه نیازی به خرید API کلیدهای پولی ندارید.
﻿
⚡️
مشخصات فنی:
*
بک‌اند:
Python (FastAPI) + SQLite
*
فرانت‌اند:
React + TypeScript + D3.js
*
مدل‌های AI/ML مورد استفاده:
XGBoost, Claude Haiku / Sonnet
﻿
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6614" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6613">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=FL8aB9LzoYb-umNdooSyZNL63Qu9Ls8qBNS01KKVk14uSDB-4JftAfLaQfnwWzn4AUhJFF_N7Ji0b62nEmy827tR_ksvcxRMkftfgttH7D1BvMWnI2MMZKMnX5_aHsaRXwd38l3B6jGHcrIv61JUzcn-dvj1VMQJcp3YVwpucDD2pVNLssnhAshMNB0MO3cOsSUNgP_fmYBPgzfDkfD1_tD7K-KAzNjTZurxdXfYorhIlBOkuZ1eZtcHMwdjb6ndJkIi8AkHiJ6ny-9fqYJjLIlGavsEiKEDqSSK1OONluqzc3T4UuUTqvSdTQSBrqDBgywjdwAeZxwgzMxiL_lgrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=FL8aB9LzoYb-umNdooSyZNL63Qu9Ls8qBNS01KKVk14uSDB-4JftAfLaQfnwWzn4AUhJFF_N7Ji0b62nEmy827tR_ksvcxRMkftfgttH7D1BvMWnI2MMZKMnX5_aHsaRXwd38l3B6jGHcrIv61JUzcn-dvj1VMQJcp3YVwpucDD2pVNLssnhAshMNB0MO3cOsSUNgP_fmYBPgzfDkfD1_tD7K-KAzNjTZurxdXfYorhIlBOkuZ1eZtcHMwdjb6ndJkIi8AkHiJ6ny-9fqYJjLIlGavsEiKEDqSSK1OONluqzc3T4UuUTqvSdTQSBrqDBgywjdwAeZxwgzMxiL_lgrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">DewatermarkAI
حذف واترمارک با هوش مصنوعی در مرورگر
این سرویس رایگان واترمارک‌ها را از عکس‌ها حذف می‌کند و فایل آماده را می‌توان با وضوح اصلی دانلود کرد.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6613" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs9vOQxL74E-fqiInzazasW20QE3OcCg6O4ixhOjt3ynhZUdI2iI2aVb6HiYLt_fqp9wRub_Xf6irhSkkeFepynrUL25SUdyBDtu95DTwWw5zTlqujr3aebOm9KEjcCXTJ-TFXU4cFj_I2mn1tG_B4Ps-aV54X0rQZronM-MiNVF5IjqkLpRZZ8v_Hh5UcgnW-T_ZO0ZJKOJxsxqLrS-JxjFzw-sa_CSuGHIIsapR-_TURiglGTxoOnLi2nPKVCT1I_yJi5DXFD-XIYD7oJ6Yflhv1nWpIFK_pp39nc7zPVf73og5vyhhklPR9UsNDo0thngvp0_zYuSnUO5ptZBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از به‌هم‌ریختگی اسکرین‌شات‌ها خسته شده‌اید؟ Trickle دستیار جدید هوش مصنوعی است که همه اسکرین‌شات‌های شما را به‌طور منظم سازماندهی و خلاصه می‌کند
فقط یک اسکرین‌شات بگیرید و آن را به Trickle ارسال کنید. هوش مصنوعی پیشرفته Trickle یک خلاصه دقیق تولید می‌کند که اطلاعات کلیدی مانند متن، نمودارها و یادداشت‌های دست‌نویس را استخراج می‌کند و سپس می‌توانید این داده‌ها را جستجو و درخواست کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6612" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJBpsxbnWZ9dKp_EzIOtenGo7O0CY7PVkTyJPf0zcJABturzaX_mZhsePe0Ge3VTm5znYxFDeDXZixVoEzGPCD2bK3Dw79_JtHehdB_0E_LFnJyKG43XgwdD2QOMj7kMFnaFqdC5Jl0QUFgF7xIlC2KHXR_DpOrKBMjNjdtXJCaxuLHQcRdZR5XJVBkvgr3Qec4Yk4xCTwbFN3bKRgEIaowsmpbzv9pqQ5sbVC8kqGwSTZk7VdJ9yCGZn0usNwicS0nI98Jl3PjGeAXbnfL_rbpDwSLvgmTwKc7c97GFY48kWNcrH2gctKClmIFk0x8wOkHn9rcfWXm-Kk1tea__Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
شورای خردمندان هوش مصنوعی: تصمیم‌گیری با قدرت ۱۸ متخصص
آیا از پاسخ‌های ساده و تکراری هوش مصنوعی خسته شده‌اید؟ با این ابزار، مسئله خود را به شورای مجازی فیلسوفان، دانشمندان و مهندسان بسپارید و تحلیلی عمیق و چندجانبه دریافت کنید.
➖
مناظره کامل بین ۱۸ کارشناس مجازی (سقراط، ارسطو، سون‌تزو، آندری کارپاتی و...)
➖
بررسی مسئله از زوایای مختلف فکری و تخصصی
➖
ارائه راه‌حل‌ها همراه با نقد و رد استدلال‌های رقیب
➖
دریافت نتیجه‌گیری نهایی بر اساس جمع‌بندی بحث‌ها
➖
تحلیل واقعی به جای پاسخ‌های کلیشه‌ای
این ابزار برای تصمیم‌گیری‌های پیچیده و نیاز به دیدگاه‌های متنوع، گزینه‌ای بی‌نظیر است.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6611" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHryxq_BXj8F2fEXZLXfZlaWAYk8cn7kfQ91_ORPfmsv3JrGsZrCWmomZuwAOrh8hflThvryIbZHqdTcUabtOsfkVKPksPO41wWkDzFoNOfKOr9kwYKuOWhQ1B6wNz9VKoeoJtZv7IpUzCs779lR73dt-u9H9LS8ezSv8HsVZ_DWJbjcR3rQwFMZNH59sHdCHkIMtB8QQRryu7m25Hr6DijwXSmCeCwW8t3S1DJCyb-wwhrj7BLi1S-5vxDR_Qqn7oi0CnLN4Wuac2n1azgaWy42GXJG3vck0lbojpafr2jpnmYrcHyYIMhpfpj6ClWG574vgsx7KELc56o8bvieng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
OFPlayer: پخش‌کننده موسیقی محلی و حرفه‌ای
➖
پشتیبانی کامل از فرمت‌های FLAC و MP3
➖
مدیریت آسان کتابخانه و لیست‌های پخش
➖
نمایش متن ترانه (Lyrics) و کاور آلبوم
➖
تحلیل دقیق فراداده‌های صوتی
➖
اتصال به سرویس‌های WebDAV، Subsonic و Navidrome
➖
رابط کاربری ساده، رایگان و بدون نیاز به ثبت‌نام
این پخش‌کننده برای کاربران NAS و کسانی که مجموعه موسیقی شخصی دارند، بسیار مناسب است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6610" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQJSm4pjjLnz5j4KFGx8tTZnaRlpq1ya4DjuJREaNTOg47euWxlpE2yRCjSDFQMJbZ_E_mJlvgBTjSMezgJNRCwA4tGZS4RxMdb2l7dQYIA5nxAEGGmeOsWwwpID_IUHrqNS4iVGmg4UHw6F8jFSoiTvfmeuR5yAyUz5s0mLPD3EwFbj0h0oeO30cyW7IHjnUIv9CJ4QHit75CKeRk25pRby-7qk1uXxTaNJBIrxEf8CQ3eJMa_g0mM2xj1lqZAy3ElenEo71R_yZA81a_OmZkxtKtDgVO9abFLgyk__IrNKYPLsAiYjdw1bKb_FFKp744eeiRYM8ZynDfKjlT6UEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏋️‍♂️
مخزن کد با ۱۳۲۴ تمرین برای اپلیکیشن فیتنس!
اگه میخوای اپلیکیشن فیتنس خودت رو بسازی، این گنجینه رو از دست نده:
• ۱۳۲۴ تمرین کامل
• انیمیشن‌ها و تصاویر باکیفیت
• جزئیات عضلات درگیر و تجهیزات مورد نیاز
• دستورالعمل‌های گام‌به‌گام حرفه‌ای‌
پروژه خودت رو با این داده‌های غنی شروع کن!
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6609" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خب Claude Fable هم استفادش برای مردم عادی کنسل شد
چینیا هم دارن مدرک جعلی میسازن تا بتونن ازش استفاده کنن
😂</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6608" target="_blank">📅 19:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
تبدیل جادویی اسناد پیچیده به Markdown خالص با MinerU!
📄
✨
اگر برای استخراج متن، جداول و فرمول‌ها از فایل‌های درهم‌ریخته و پیچیده مشکل دارید، ابزار متن‌باز
MinerU
دقیقاً همان چیزی است که نیاز دارید! این پروژه فوق‌العاده که با استقبال بی‌نظیری روبرو شده و بیش از ۷۰ هزار ستاره در گیت‌هاب دریافت کرده است، اسناد شما را به راحتی و با بالاترین دقت به فرمت تمیز Markdown تبدیل می‌کند.
🔥
ویژگی‌های برجسته این ابزار:
1️⃣
پشتیبانی از فرمت‌های متنوع:
توانایی پردازش و تبدیل فایل‌های PDF، DOCX، PPTX، XLSX، تصاویر و حتی صفحات وب.
2️⃣
استخراج دقیق جزئیات:
بیرون کشیدن بی‌نقص متن‌ها، جداول و فرمول‌های پیچیده (ریاضی و علمی) از دل اسناد.
3️⃣
پشتیبانی از ۱۰۹ زبان:
قابلیت تشخیص و پردازش بی‌نظیر اسناد در اکثر زبان‌های دنیا.
4️⃣
کاملاً رایگان و متن‌باز:
یک پروژه Open Source قدرتمند و بدون هیچ‌گونه محدودیت پرداخت یا نیاز به سرویس‌های ابری پولی.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6607" target="_blank">📅 18:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7tPlQWO5GCKmvVupK0ndzoVluWeygI0sqGucPOKbiZ43O9VO7Pvlb4xb3XHRcIjBHA3wKjsXMXMsPTLybCxdBgC7ax2fvahB0Mh3tDnhTUEOWC1H7kHnnDe60w6S18yMBlQd4QosDYlw3F1Xeog2oHMNJRC7Cz-gvPoxmyv96hZm4WX6-nC1tncQdKjRZtSvj5FBBPjGpndnYazWPD4dhI2kFFvn2c-JxPv3-WQWSiCMqPhLLFDSpznfaDVP5Yu3PfEStKD-M-zTb4Upl-F5Z-Ju6RDM7-h627_eLY3_baODitIEcjUQ5o3wtYFLgFe0CaADeri61K0nIfyL_AYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها ElevenLabs را کشتند!
💀
توسعه‌دهندگان ByteDance نسخه SeedAudio 1.0 را عرضه کردند که هر نوع گفتار و افکت صوتی را کلون و تولید می‌کند.
1⃣
ایجاد گفتگو با چندین شخصیت: هر شخصیت متمایز است، دارای احساسات، سرعت، تمبر و حتی لهجه منحصر به فرد؛
2⃣
دریافت تا سه منبع برای کپی کامل صدا، احساسات و سبک؛
3⃣
تولید صداها بر اساس پرامپت، مرجع صوتی یا حتی تصویر.
آیا این پایان دوران انحصار ElevenLabs است؟
🤔
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6606" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDPWTwwOlSVW5V5ZA26B-8uGJmMJyjydHqDjObGlLAOMfAY_HNo1W3aeY2rsr5XxVbGlKYhC2YPRjM7BLDlSnRR_TDMpjbywJUUog3aFjHTExltS_0txV2AaZ5csK7ihwciIeTcdsuZ3PlBF1w4A0PcJPoxljg6_oh9VtecJU4H6TQFZIQbiGBWZ098-nnSbJqArFA0c3g-HPRxR1JWe3Y5hwtvMuvv1rPmEQviWMMEPAdBxYz2sYTBreaBcY-t9RWCYm4hjxigmYYnmvS_DN1l0krYTd1tQ0V4Xam_YU6ICTwv3BrsY2lTZvGUHSjbcxwsBvY26VMh6sMvt76Ey6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
تولید رابط‌های کاربری زیبا با پرامپت‌های آماده
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6605" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚀
معرفی IstanPdf؛ ابزار قدرتمند و آفلاین برای مدیریت فایل‌های PDF و DOCX!
📄
✨
اگر از سایت‌های پولی، تبلیغات آزاردهنده و محدودیت‌های سرویس‌های آنلاین تبدیل فرمت خسته شده‌اید، اپلیکیشن
IstanPdf
دقیقاً همان چیزی است که نیاز دارید. این ابزار کاملاً آفلاین توسعه یافته تا جایگزینی بی‌نقص و رایگان برای سرویس‌های پولی (Freemium) باشد. در این اپلیکیشن حریم خصوصی شما در بالاترین سطح قرار دارد و هیچ فایلی از گوشی شما خارج نمی‌شود!
🔥
امکانات فوق‌العاده IstanPdf (نسخه v1.0):
1️⃣
ابزارهای حرفه‌ای PDF:
*
Merge:
ترکیب و چسباندن چندین فایل PDF به یکدیگر.
*
Split:
استخراج صفحات دلخواه با تعیین محدوده صفحات.
*
Remove & Reorder:
حذف صفحات اضافی و تغییر ترتیب صفحات یک فایل.
2️⃣
تبدیل فرمت (Conversions):
* تبدیل یک یا چند تصویر به یک فایل PDF یکپارچه.
* استخراج صفحات PDF و ذخیره آن‌ها به عنوان عکس.
3️⃣
ابزارهای کاربردی DOCX:
امکان حذف صفحات خاص و تغییر چیدمان و ترتیب صفحات در اسناد ورد.
4️⃣
حریم خصوصی و امنیت مطلق:
کاملاً آفلاین، بدون نیاز به ساخت حساب کاربری، بدون محدودیت حجم و آپلود، و فاقد هرگونه تبلیغات و پرداخت درون‌برنامه‌ای.
🔗
دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6604" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uarZM6Xa9DIrcDku7PRk7AKiM-BSsxeQ25XIRlwLCEJ72hgvDnZcTYb_9kyOeEUlt6J2M4tjj7S6ojk70PtxyJcwHti6_ncq2qENrF5TlyC7wunq3wOdq8vAclkEY7X87agIaEIcJpoxKtW8Z56oLvBSLX1kgWHhyWdChWPw71ru4Xb9vPNWkKdIMQkCMBEq0hM85lesSzH9IX802m9hGwqgdIogbu63Cktu5MdhcHlKlLbjkrtL5fqPqd5_RmKXHCcoHMeDLhO2GMRcBohP7tQ7XPMK6LH4yt3fauIzkG8_nQYE7aDkE0aJRtlwPRhm1aT_x3br25VHrK4iPjOvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها:
•
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه
•
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان
•
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب
•
📝
فقط پرامپت بنویسید و کد آماده دریافت کنید
🌐
Site
#AI
#Coding
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6603" target="_blank">📅 11:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=CiYEXBSJR1OkL7PWweX-rJlc8_opIhz2OUzMGqB7Wwh3IklPVDdURbLuv9-NwZqLietC_T2QUjAuf9Y20_7NY_xIZUi6rLZREgbkwisf4wbuFPJP2AKrTjSXF6MruL00Da4CCOSsMHRhrsluNs00vxQVIWsMtp-h6m3AT5PzlIsh_Z-d-uMCxdeqOdtZf7qFtDKibEZ1rkjaVxKOOdQ41W3jD1Wfudi5jl_djoInOVX7STHMLlcZhO81ka44UuYhEy3pbJKGMzopbM8WD7dDD8i7Tha3HAmuGLqYBlKsxGk2CfimxtIi8-dUtXi5B9hx3kQRDZmLc32iW0LnlqK72Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=CiYEXBSJR1OkL7PWweX-rJlc8_opIhz2OUzMGqB7Wwh3IklPVDdURbLuv9-NwZqLietC_T2QUjAuf9Y20_7NY_xIZUi6rLZREgbkwisf4wbuFPJP2AKrTjSXF6MruL00Da4CCOSsMHRhrsluNs00vxQVIWsMtp-h6m3AT5PzlIsh_Z-d-uMCxdeqOdtZf7qFtDKibEZ1rkjaVxKOOdQ41W3jD1Wfudi5jl_djoInOVX7STHMLlcZhO81ka44UuYhEy3pbJKGMzopbM8WD7dDD8i7Tha3HAmuGLqYBlKsxGk2CfimxtIi8-dUtXi5B9hx3kQRDZmLc32iW0LnlqK72Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🔥
🔥
هر نوع رسانه‌ای را از تلگرام و حتی چت‌های خصوصی دانلود کنید
🤯
• دانلود صوت، پیام‌های صوتی، ویدئو، GIF از چت‌ها، استوری‌ها و حتی چت‌های خصوصی که دانلود در آن‌ها ممنوع است.
• پشتیبانی از دانلودهای چندگانه بدون کاهش سرعت.
• قوانین تلگرام را نقض نمی‌کند، می‌توانید با خیال راحت استفاده کنید.
🌐
GitHub
#Telegram
#Tools
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/6600" target="_blank">📅 08:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دریافت 7 میلیون توکن روزانه AI به صورت رایگان!
🎁
🤖
مدل‌های موجود:
• Mimo 2.5 Pro
• Mimo 2.5
• Mistral Large
• Mistral Medium 3.5
💻
کاربرد:
• ساخت وب‌ سایت
🌐
• ساخت ربات تلگرامی
🤖
• کدنویسی در ترمینال
⚙️
🔗
NaraRouter
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6599" target="_blank">📅 01:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Metapi؛ هاب هوشمند و همه‌کاره برای مدیریت APIهای هوش مصنوعی!
🤖
✨
اگر برای دسترسی به مدل‌های هوش مصنوعی در سایت‌های مختلفی ثبت‌نام کرده‌اید، حتماً می‌دانید مدیریت ده‌ها API Key، چک کردن مداوم موجودی و تغییر دستی تنظیمات هنگام قطعی یک سرور چقدر کلافه‌کننده است. پروژه متن‌باز
Metapi
توسعه یافته تا به عنوان «پروکسیِ پروکسی‌ها» تمام این مشکلات را حل کند!
🔥
امکانات و ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
تجمیع تمام APIها (Aggregation):
شما ده‌ها کلید مختلف را به Metapi می‌دهید و این ابزار به شما
فقط یک API Key و یک Base URL واحد
می‌دهد. حالا می‌توانید این کلید واحد را در تمام برنامه‌های خود (مثل Open WebUI، Claude Code یا Cherry Studio) قرار دهید.
2️⃣
مسیریابی هوشمند (Smart Routing):
اگر سرور یکی از ارائه‌دهنده‌ها قطع شود یا مدل خاصی در آن گران باشد، به صورت خودکار درخواست شما را به یک سرور جایگزین، سالم‌تر و ارزان‌تر می‌فرستد (بدون اینکه شما متوجه قطعی شوید!).
3️⃣
دریافت اعتبار خودکار (Auto Check-in):
به صورت زمان‌بندی‌شده در سایت‌هایی که سهمیه رایگان روزانه می‌دهند لاگین کرده و اعتبار شما را به‌طور خودکار جمع‌آوری می‌کند.
4️⃣
حریم خصوصی ۱۰۰٪ و نصب آسان:
به راحتی با داکر (Docker) روی سرور یا سیستم شخصی شما نصب می‌شود و تمام داده‌ها فقط در دیتابیس محلی (SQLite) خودتان ذخیره می‌مانند.
5️⃣
سیستم هشدار پیشرفته:
در صورت بروز قطعی یا اتمام موجودی، از طریق تلگرام و ایمیل (SMTP) به شما نوتیفیکیشن می‌دهد.
⚡️
برخلاف پروژه‌های مشابه که برای تیم‌ها و فروش API طراحی شده‌اند، Metapi کاملاً برای
استفاده شخصی
بهینه‌سازی شده و رابط کاربری بسیار سبک و تمیزی دارد.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#API
#Metapi
#OpenSource
#Github
#SelfHosted
#Docker
#Tools
#OpenWebUI
#LLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6598" target="_blank">📅 01:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Awesome Android Root؛ گنجینه‌ای بی‌نظیر برای روت و شخصی‌سازی اندروید!
📱
✨
اگر به دنیای روت، کاستوم رام‌ها و دستکاری عمیق سیستم‌عامل اندروید علاقه‌مند هستید، مخزن
Awesome Android Root
یک دایرکتوری جامع و بی‌نظیر است که بیش از ۴۰۰ ابزار، اپلیکیشن و ماژول مخصوص دستگاه‌های روت‌شده را به همراه آموزش‌های دقیق در یک‌جا جمع‌آوری کرده است.
🔥
امکانات و ویژگی‌های کلیدی این لیست:
1️⃣
آموزش‌های قدم‌به‌قدم:
راهنماهای کامل و دقیق برای آنلاک کردن بوت‌لودر (Bootloader Unlocking) و نصب کاستوم ریکاوری‌ها (Custom Recovery).
2️⃣
پشتیبانی از جدیدترین متدهای روت:
پوشش کامل و معرفی ابزارها برای روش‌های مدرن روت سیستم از جمله
Magisk
،
KernelSU
و
APatch
.
3️⃣
کالکشن گلچین‌شده ماژول‌ها:
مجموعه‌ای از بهترین و کاربردی‌ترین ابزارها برای مسدودسازی تبلیغات (Ad-blocking) در سطح سیستم، اتوماسیون وظایف و شخصی‌سازی عمیق رابط کاربری اندروید.
⚡️
مشخصات فنی:
*
زبان:
Python (برای مدیریت و استخراج داده‌های لیست)
*
پلتفرم:
Android
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#Root
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6597" target="_blank">📅 20:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سلام
دوستان اگر به وایب کدینگ علاقه دارید یه نگاهی به این سایت بندازید:
https://risman.pro
برای ساخت محصولات فنی میتونه خیلی کمکتون کنه. (بدون نیاز به هیچ دانش نرم‌افزاری و برنامه‌نویسی)
امکان انتشار در دامنه خودتون هم بهتون میده.
با اولین لاگین حدود ۱۰۰ هزار تومان توکن هدیه میگیرید و اگر خواستید توکن بیشتری مصرف کنید میتونید از کد تخفیف welcome برای ۵۰% تخفیف تا سقف ۱ میلیون تومان استفاده کنید.</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6596" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaVGsjfgrov84u_vo1Df-mQ1-8TsMC4dknffuEAyqBqUDRUeB9Y_EmwQmKrsIj9cnddyXO6yON8ogp4XwZO0j3eaAfWisixhi2GirGIbvCiz_zwgBfT7YbDAqX4pgo9VV3FJYLiPR7XwIh27g75hm7u_jDSSS0nNuztwQeGTeOrWY2b83ElH7VQnM5yjfu7fprqnxMjtJRnSEZ-Yu-wqp7iludJ8VRWia4p9uLN30keqsCOe11hkxoEVzQEj8lR28qseKfG-QYURmfDqgktt0zy69yb4EqCj4VjWLHoxWveEs3iz0395gaYB86-4m9VtjYJ0IjAGOGSNlpo67lQm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SY-VIIoSEsZQqGZCNqdPK5G44-k-ekPgMrfbn4-w5VjNtfy7l4NnpSqfLa_ixJzRLEDNJnklgI0BSYgpH0GhhVgvUNhW5XJ1IAmxcSVt--Blwx3mZxWH6oBbQ_O2uwo7Jo_2omHHedKNn_9d_btSAJeoeZ5oMVxjM-KpEEgSzo6QRZqzZDuv25EeQtCRnwlIw7wIQxSs-Pq2XV7IoYAtJaTm63au7rpABXsEGfWyaJE2MjtD4NWWtmGz4G96rE6CGKO6gtfZaKcyD54S-wmB5qd6XAOzbss-z6THs9YEn1M4-poABj6HGRF4eM9Xt_pbzFohstrXrf7QDOoQl9oddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن
Solipsism
یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی با ایده خلاقانه "Rail-first" تمام کنترل‌ها و نوار آدرس را به جای بالا یا پایین، در یک نوار کناری (سمت چپ یا راست) قرار می‌دهد تا کار با گوشی‌های بزرگ با یک دست بسیار راحت‌تر شود.
🔥
ویژگی‌های شگفت‌انگیز این مرورگر:
1️⃣
طراحی نوآورانه (Rail-first):
قرارگیری منوها در نوار کناری با قابلیت تنظیم اندازه (از کوچک تا Super Compact) متناسب با اندازه دست و صفحه نمایش شما.
2️⃣
زبان طراحی Material 3:
رابط کاربری بسیار زیبا با گوشه‌های گرد، انیمیشن‌های روان، سایه‌ها و قابلیت هماهنگ‌سازی رنگ‌ها با تم سیستم‌عامل اندروید.
3️⃣
ابزارهای قدرتمند حریم خصوصی:
دارای مسدودکننده تبلیغات (Ad Blocker)، وب‌گردی ناشناس، کنترل کوکی‌ها و WebRTC، پاک کردن خودکار داده‌ها هنگام خروج، و یک قابلیت بی‌نظیر به نام
Decoy Mode
(تولید تاریخچه وب‌گردی جعلی برای محافظت از حریم خصوصی!).
4️⃣
امکانات کاربردی و سریع:
دارای اسکنر QR داخلی، قابلیت نصب مستقیم وب‌سایت‌ها به عنوان اپلیکیشن (PWA)، پخش تمام‌صفحه و بدون مزاحمت ویدیوها و ابزار دانلود حرفه‌ای.
5️⃣
صفحه خانگی شخصی‌سازی‌شده:
امکان تغییر والپیپر هوم‌پیج یا تنظیم آن روی حالت کاملاً تاریک و بی‌صدا.
﻿
⚡️
این مرورگر سبک که بر پایه WebView اندروید ساخته شده، تجربه‌ای کاملاً متفاوت، سریع و مدرن از وب‌گردی را به شما ارائه می‌دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Solipsism
#Android
#Browser
#Privacy
#Material3
#AdBlocker
#WebDevelopment
#MobileApp
#TechTools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚀
هوش مصنوعی دیگر کدهای شما را فراموش نمی‌کند؛ دستیار حافظه دائمی برای ایجنت‌های برنامه‌نویسی!
🧠
✨
اگر از پریدن کانتکست (Context) در چت با هوش مصنوعی و توضیح دادن‌های تکراری خسته شده‌اید، این ابزار جدید مشکل شما را حل می‌کند! به تازگی یک دستیار هوشمند برای مدل‌هایی مثل Claude، Codex و Cursor منتشر شده که دانش و اطلاعات پروژه شما را بین سشن‌های (Sessions) کاری مختلف حفظ می‌کند.
🔥
این دستیار چه کارهایی انجام می‌دهد؟
1️⃣
حفظ همیشگی کانتکست:
اطلاعات جلسات کاری شما را ذخیره می‌کند تا با بستن پنجره، کدهای شما فراموش نشوند.
2️⃣
یادگیری ساختار پروژه:
معماری، دایرکتوری‌ها و ویژگی‌های خاص کدبیس (Codebase) شما را کاملاً به خاطر می‌سپارد.
3️⃣
بسته‌بندی خودکار دانش:
اطلاعات جمع‌آوری‌شده را به صورت خودکار و هوشمند بایگانی و بهینه‌سازی می‌کند.
4️⃣
بازخوانی در کسری از ثانیه:
هر زمان که ایجنت به اطلاعات قدیمی نیاز داشته باشد، در کمتر از یک ثانیه آن را فراخوانی می‌کند.
5️⃣
پشتیبانی بسیار گسترده:
سازگاری کامل با
Claude Code
،
Cursor
،
Codex
،
LangGraph
،
CrewAI
و سایر ایجنت‌های هوش مصنوعی.
🔗
لینک دریافت و راه‌اندازی پروژه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#CodingAgents
#Claude
#Cursor
#Codex
#LLM
#Memory
#ProgrammingTools
#DevTools</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-YGF8_oy7qtCF3XEkZpzASa5nB-AiqH1jUFHV8OACoKR8wVIWpsL-eK4g0fbZAoRZw4wHMiSaMReRU9h9Lxcste9MNvqVDcKoUZbHpEeIBSKHJJSOgFzVcCehLU30ZF5247jD3XYPEYQNEMuotpLkDZhoGXNYaVU2lhoFKzGn4sus4JkZ8T6zGqeij06-D7hR90-MzLu6PVglWAiPM4v1mOPLgpMy_nOiI5MMnoPN1nBO0CVqxrBxQaJ_goBniDlazSlrBKEPy_8KEcNKN7mY0LtfhUwbjaPv65q0anmL_6RKhMQL3F1vPLeCK45VIYQ86EnEvudN-joPp1qh4n_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 1T کانفیگ شخصی
🔑
🟢
از لینک زیر میتونین شروع به ساخت اکانت کنید :
➡️
sign up
بعد از ثبت نام وارد اکانت بشید و روی
Quick Subscription
کلیک کنید و داخل اپ هایی مثل :
Nekobox,hiddify,singbox و ...
اکسپورت کنین .
به دلیل نوع پروتکل یعنی AnyTls بودن فقط داخل اپ های ذکر شده میتونین اکسپورت کنین و داخل اپ هایی مثل V2ray کار نمیکنن
😬
خط های تست شده :
🛜
🛜
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fp0O1pChou2tP797bcTYhqiRNFpmtyfBb_NLvENn4cwUg064hqFP3DRDeSRhzZ8xZt6M3Xsn0k1xHqtu4O57t0-1Cf3vT3FYsQfpg1m33c6xptzKJcLhwzB7n0nQUZfVVU2pyir1Fbn-18E5-3sZ4utpDQB9Oggvvy95ytoj4osmDWdVck1j2j8yf457-r97GhjuQG5WmTG6XPQwGa3Kjtez0WqYgO1rJrFuhtGojV_ELXc7BBUxBqrS8t1NxOL2cy5Jelm2dXE4SgqrkRJZbx_TSbQW610KZuBnSPsw_3MT1dSnf-7mmB3w9WOoP4RlwbPwlRfScxdnAbbQ4iGH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2V7OmTB4Tgxq9RKtpWS42aceKesTCPbIpz07IsbICbE0jhR1kTvoq18JXcpqvCBlKiXliZoaSCynLC9rN5xYFGa9sUF_onIPejAjorhW0_0NcFj6_fDIkKO18Q4PjSQCM4ds0gy52pyA9PPFYUlpbmmHxT-St1IaOU7RwS77D8cF3RMLm06S2Oz0holUDUR96PgKLgPou3_JzwOQTfuhFGCriXneDqK29UsZDVMKhR12YQNE912GqPcYRl9N6bMNM-_lmbSgbeNFxbiz2RCmq0th0SG4oC6nQmuIJAl-Itm9kcWNftAnUIygyu3cZ4mAxBSO63_vqFIwaOksHG4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUdFdR5LzrsfyF_O-hHhfD9RBMzfVGwEwJgOz-OZoIg-RvxjOAhgGWO6Z9XU-XcT0OkPoaxk2vojK6am13Zf4I0d3E8d3yltsKsoPD5IFVP5UNMEcmhdIKhll4h09-9BPRnPDIugSL0Jy8Ghgk2F-Pw_tqKIx-6tk4YWjuXmRy8-zwg1tWi4VMg6DSPWxvTDdkqWlNUtAuUF5yJ-9GkotlFW9kqF8Fm6JnRqKcNIlQVwyLkaW2RPqQ9BVQ2Ps5FnCDRgJnH6c_qvv_xDABDU0vkeWJXXpFUUDNUjznkgyIqpS7ZC05RDfzfsGzkKs49_INQQsfM-1n5IUAiFevJuJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبدیل عکس‌های معمولی به شاهکارهای هنری با هوش مصنوعی
🔥
✨
قابلیت‌ها:
•
🎨
انتقال سبک هنری (مثل ون‌گوگ) به تصاویر شما
•
🪄
انتقال سبک بصری یک عکس به عکس دیگر
•
⚡
مبتنی بر شبکه‌های عصبی کانولوشنی و الگوریتم‌های پیشرفته
•
🛠️
رابط کاربری ساده و سریع برای ویرایش آنلاین
•
📦
بدون نیاز به نصب نرم‌افزار سنگین
🌐
Site
#AI
#Art
#Tech
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pp_oym3NX8UvOCc2S7trTiFBdrwroF9581GnzcnCF3EV1OHd5Bw8KuEfcMzHKQwUrq6f6Yh3csxAqnBF5UMYU3eqXb_3XF4Vl97kOAoSExCc3kNdwKykhF-fX07GPDJROKOJYAZP9g7KtW8RMIan1-Mf9jSeTUR7BpFeylQUDpDJ8pQOhi9CYcVY8a968Jqe76B5OgWiFYkGgy1eGWOhlzn1V7vDJ7PiR1MKSs9mWeZ7XBn3RN7xCukeqSOooSs8OSFmW1Z0jgt-Ikw-znOsKEP7dSewIHDkNe_XAC2X4hjDSmVvD0GDPvzDYyuLP8VzvKUc0IX6e-QRGNGBI1_7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه
Orcafile
دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما را مجبور کند پوشه به پوشه بگردید، کل یک دایرکتوری (یا حتی یک درایو کامل) را اسکن کرده و تمام فایل‌ها را بر اساس پسوندشان (Extension) گروه‌بندی می‌کند.
🔥
ویژگی‌های کلیدی Orcafile:
1️⃣
اسکن فوق‌سریع:
قابلیت اسکن بیش از ۱۰۰ هزار فایل در پس‌زمینه بدون افت عملکرد سیستم.
2️⃣
مشاهده لحظه‌ای پیشرفت (Real-time):
نمایش لحظه به لحظه وضعیت اسکن فایل‌ها.
3️⃣
جستجو و فیلترینگ هوشمند:
جستجوی آنی نام فایل‌ها و فیلتر کردن دقیق بر اساس فرمت و پسوند.
4️⃣
دسترسی سریع:
امکان باز کردن مستقیم فایل‌های پیدا شده در فایل اکسپلورر ویندوز.
⚡️
مشخصات فنی و
پلتفرم:
توسعه‌یافته با ترکیب قدرتمند
Python
و
PyQt6
.
نسخه اجرایی (App) در حال حاضر فقط برای
ویندوز
منتشر شده است، اما از آنجا که پروژه متن‌باز است، با استفاده از سورس‌کد و دستورالعمل‌ها می‌توانید آن را در هر سیستم‌عاملی (مثل لینوکس و مک) اجرا کنید.
🔗
سایت پروژه
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Orcafile
#Python
#PyQt6
#OpenSource
#FileManagement
#WindowsApp
#Github
#Tools
#Productivity
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=PYSrgoxvLZwwunUGaUB2WUhlZK3z81b5lTUG63-N1aq-3_LqBsuTiBUCC3buXSLpfx_L_T1nonNUXVLNoOrRW6kg4Y1JXfJt0UAb4Xaccc9qZrrguZKUOgYcCzdx_fTAKCEOfGR2c31Owcmiwykxo9r97w19T7rjKlGeA2mHzU4nhpNZGbmx8-pBeyAdf56y0ZumHm90fsBtsPcJnsncPu9R7nWZDKZopeXb9CQuM4AsS7j09HIXh4Mrej0lB2j7-IQGjB_elahrh7esX0Dt2ztL4MGuEPyVEFiitDepjDv9ec6_EZlhoRvNKHyI1KIahpXQrJaQ_mVx0dIukT0OFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=PYSrgoxvLZwwunUGaUB2WUhlZK3z81b5lTUG63-N1aq-3_LqBsuTiBUCC3buXSLpfx_L_T1nonNUXVLNoOrRW6kg4Y1JXfJt0UAb4Xaccc9qZrrguZKUOgYcCzdx_fTAKCEOfGR2c31Owcmiwykxo9r97w19T7rjKlGeA2mHzU4nhpNZGbmx8-pBeyAdf56y0ZumHm90fsBtsPcJnsncPu9R7nWZDKZopeXb9CQuM4AsS7j09HIXh4Mrej0lB2j7-IQGjB_elahrh7esX0Dt2ztL4MGuEPyVEFiitDepjDv9ec6_EZlhoRvNKHyI1KIahpXQrJaQ_mVx0dIukT0OFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💻
JanAi
جایگزین محلی ChatGPT
این برنامه مستقیماً روی کامپیوتر اجرا می‌شود و نیازی به اتصال به اینترنت ندارد. می‌توان از مدل‌های زبانی مختلف برای متون، برنامه‌نویسی و سایر وظایف استفاده کرد.
🌐
Site
#AI
#OpenSource
#LocalLLM
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBnU70mAVTJGxKZENptD97xbnDJI5AdoV1BE3E6hlc2y7Xhzo0af8fvF0IFgkPBIGYo4bz_pgFTmS7nkdzPBmZ-OYNNdwWWBbhvV-sxZrRshx3PhZTyNmfysaRBj43i4uE7PyABdZ1DBXlj7qYeFdzcNdRUo8eE3DgZwvZhckM_fSNuw8Z6dm4H-H7nK1K1bPIz6mzS4TUS6-wu54J8Fydq8o7QfBzZnSjOfKRQFTP9K8gTksHptcAIJQXGGId2sZzih0FpVmHvGW9gGJto4ydYKsb754P27UgsmeygVjTaBnYzttQZhfO7F5IiLStxj_JcU1MlHsN_kUBWMqSB9BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8cVaNvdJB0dzsq2crYCC6hwTY9ebrU6tL0FxvwIOrLqmFgiuo3ialVSRrNQDBWo-l0gDdnvHqyBetAvPbZ2rCb-dSHWlWSs8BWNcuDjrxP5dmKv3s8ijxotdmXDGedtmuINiG7brpCaRf_bpwDQBzbXbPUxGRixRp3Bv86Pk_4yIFaOUXQlZq3IxTxuJU0nmEUqA9CtrZgd2VtNsM5zNmoVMK3R8FF2nhVtWk8dcJ91QSDSlcSw0y93PYT7C1uMmVpdh6keUZBRYJ0-jaw96IK8bn0cKFUo1WZI450mwfkW27s_ZNEd42hth8_SbvFOk-KSzWts1jFdqrfbRzM6AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">طراحی وب و اپلیکیشن در یک ثانیه با ابزار جدید GenSpark
🚀
✨
قابلیت‌ها:
•
🔹
تحلیل مستقیم فایل‌های Figma، عکس و کد
•
⚡
تولید طرح نهایی بدون نیاز به کدنویسی دستی
•
🛠️
دسترسی به قالب‌های آماده برای وب و موبایل
•
📦
ساخت رایگان نمونه‌کار برای فریلنسرها
🌐
Site
#AI
#WebDesign
#GenSpark
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQNnCyCA9RjlWPDgntfirLGuEZn1Td1Tw-HWbc8HwqOIGXxiUXKo4J2dXaJON9JsicGxpyee_Vw9QfRpPh2zJW0Z4BUotMdNNU_oH7wk6M4JFsewey6gyzxGoOSh754kQZQJ3vbKvmLEs8d3t4aSe6wkf-1v49l7cU6Lba5HDsWpKy5N21Toz9_FHjC07PJ6BkV85NRY6PP2Z9Dc94LGRHVd7TZ8vnoSlvDnx_1G6-oS4ar0naVw1NPicWN-cJTvc2yEd-w7Oo1PrSatAA_1_YDIrdJ8zpsmXAAGpDA4K8DmB72zM7oKBqotz86Z35Z9xOEkz85Ke0tYs3sHOaOKlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
انگلیسی رو تو حرکت، باشگاه یا پیاده‌روی تقویت کن!
با این ۵ پادکست، بدون کتاب‌های خسته‌کننده به گفتار زنده عادت می‌کنی:
•
🇺🇸
American English Podcast
: انگلیسی آمریکایی، فرهنگ ایالات متحده و مکالمات واقعی.
•
🧠
English Learning for Curious Minds
: داستان‌های جذاب درباره علم، کسب‌وکار و زندگی.
•
⏰
6 Minute English (BBC)
: قسمت‌های کوتاه با واژگان جدید، اصطلاحات و موضوعات روز.
•
🗣️
The English We Speak
: عبارات مدرن، زبان عامیانه و اصطلاحات مکالمه‌ای.
•
🇬🇧
Luke's English Podcast
: تحلیل زبان و فرهنگ بریتانیایی، یکی از معروف‌ترین‌ها.
#EnglishLearning
#Podcast
#Language
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QB5X_R6jFiGvGGNvWwgZDoFQWKOQWZrjBgNrM6uaWnP7hgZIN7h72Y90vWkBHYaMhD6W5pepNRZtOReljV_BY69I14aTIUsQD0_lIDJf4VWzUPO-a5Rto8OV54639etWpQsGsOQwnBQohBzj-imtV8IHlF0al-zgQUfSVgzzZAIWmjPqYIY7ZLBmFfnxmjyROOIK_Z3mkqNcWDTsytZvKC6xjTr6EGU8hD6n5QrTNTe8st54KY0LT3kUQz1up8zzJWMj1J9Y_5VsSAXv1Lx6dYMlD5XwsjGQh_m62NKr5Ideg4kW-OI0SYh5ReLhKbmzrMdoXfUSLHDT-XwzTJbo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANIV7GRaRLx31NLJCNIcCMRcB0nv7aR1_a6KW1xzkghNA6PurtIYXONB6iRlcUGJWcszcP2scYbJOUBxLfgXQiy76T4Zfb8VdDBw2XjN4Y2oxgZxYtghefJd3pma6r8JJu8xqg1HvDv0FiibXXJZzJ6BQ47Xd0TJEwmSAkMAX7VML29eyk-_a4SLhjWNNUtRV8d2J5_46z01ZfoN7khCnWyMaA1iDfvTzGXZSEayTwU4ulrZJg95FOKJZXn3qTEW1UBvmarIr8WSe6P-HDlW4NrP8pxQCokR0jSiFBm3ARu7_63ZQN034NvyrGDpAGZJEKvQPGvG5uJY1nUaRSk-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlqIo0H80ChLJH0PAYtLWZMeE4JqZ0BV1N6pA5pR1iQ4P4u9OUH6q1Wd1IwEWn-Sh8hx3sRppy3cECaWH5JAfTC80iaKFI6VFs15A_F2h17zLmeJ1MNYCSOfrUq1LbXf0nu2_wur38Y7a3ytvFQsxR6Mmdu0zA3O0Y4HpHaeMWHGtLjwog_gKFger1kV6zaiQb44pxdxXjJ37oykr-ooyufCRNVvwgq6Pkx-17-Wf8qvKNqGhO-_lfyq2ZaIhJj40d5UOjsrq3ifj_M0Fr4eKKVN3wYFcLQqKpzYfy_4giVVqeOSKNVbbQSKpsqK3WyzDzo8v3PcwAzBBokAOf_4oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
OpenAI
مدل جدید GPT-5.6 Sol را معرفی کرد؛ مدلی که در چند بنچمارک مهم، حتی از رقبای مطرح هم جلو زده و تمرکز اصلی‌اش روی کارهای پیچیده و توسعه نرم‌افزار است.
💻
🧠
•
🔹
عملکرد بهتر در بنچمارک‌هایی مثل Terminal-Bench 2.1
•
⚡
توانایی کار مداوم روی پروژه‌ها برای ساعت‌های طولانی
•
🛠️
مناسب‌ برای توسعه نرم‌افزار با دخالت کمتر انسان
•
📦
معرفی مدل‌های سبک‌تر و ارزان‌تر Terra و Luna در کنار Sol
🌐
Site
#AI
#OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الان برای API بهترین
aerolink
هست که بهتون
opus 4.8
میده
خیلی ساده
لینک ثبت نام
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
نحوه اجراش روی
claude code
هم همونه فقط تنظیمات رو این بزنید
هر ورژنی از claude code هم بزنید قبوله
{
"env": {
"ANTHROPIC_API_KEY": "کلید",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلید'"
}
لیمیتش هم دقیقا مثل
freemodel
هست
فقط مشکل اینه هر ip ایی تو claude code قبول نمیکنه باید تست کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=dIv9Vz9rtccb_PSyhafBUmrG_QIW8NwPLlcx_h29zI081o8VGrN4JADC8H_f3lYQ7Be1FycTHXI7y9o7glglnLbCCmAogAZSHc5AA4sA18pabzqTroAT00yNSn99siGTqX6dX-sq6BL3k-bbVFyLQp-DZwbkbLG1MvknAdrTersTscVZCmNXNaQluM9JgHeqjLuAJygFfpmTKIvC434u6pq0Jazl5hRRxIbjQhAj4rKHInGZtJlJKJbC_uoxNJBHBei2w1ygvPfrmzdzHZZmj5ZE_ihUmGYggHBNYw0bh3KEVzHmuRfCqqnIa8K3mLSQFIY5urXBHgqQkn1h1LiCiJXTWADN8tSAJYd57SW4F-d0LwM1hxm7d1h8BNp9CKmD43ouIUMgOxNJR4sweu4uM9Wqg1NXGuWSaqOVRx0wH5tS5zUIP1w4Ao4_zNRiENYrtU6_NPdwrTPRqZsfYjcshsb7L-n7Q11BozuqISoEPA4zUiM3FC9G6aiNcAvX51eoUV4zOsaOXOFor7OAYVTHcSUyPZHQ9pn5vORaRK-LzPh6CyGVVksNGEHdnfFVjY_xEmv5Etu3Rx_UZp_PmoDTwG1_o5rN7Hvru63XldBtOlqma9ha5IuFsH5LZPTQvfECwJx7Z6ZlkH3eq6iuJ9CBkUFG6bCxktKVuyeLhVIPWec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=dIv9Vz9rtccb_PSyhafBUmrG_QIW8NwPLlcx_h29zI081o8VGrN4JADC8H_f3lYQ7Be1FycTHXI7y9o7glglnLbCCmAogAZSHc5AA4sA18pabzqTroAT00yNSn99siGTqX6dX-sq6BL3k-bbVFyLQp-DZwbkbLG1MvknAdrTersTscVZCmNXNaQluM9JgHeqjLuAJygFfpmTKIvC434u6pq0Jazl5hRRxIbjQhAj4rKHInGZtJlJKJbC_uoxNJBHBei2w1ygvPfrmzdzHZZmj5ZE_ihUmGYggHBNYw0bh3KEVzHmuRfCqqnIa8K3mLSQFIY5urXBHgqQkn1h1LiCiJXTWADN8tSAJYd57SW4F-d0LwM1hxm7d1h8BNp9CKmD43ouIUMgOxNJR4sweu4uM9Wqg1NXGuWSaqOVRx0wH5tS5zUIP1w4Ao4_zNRiENYrtU6_NPdwrTPRqZsfYjcshsb7L-n7Q11BozuqISoEPA4zUiM3FC9G6aiNcAvX51eoUV4zOsaOXOFor7OAYVTHcSUyPZHQ9pn5vORaRK-LzPh6CyGVVksNGEHdnfFVjY_xEmv5Etu3Rx_UZp_PmoDTwG1_o5rN7Hvru63XldBtOlqma9ha5IuFsH5LZPTQvfECwJx7Z6ZlkH3eq6iuJ9CBkUFG6bCxktKVuyeLhVIPWec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
معرفی Cloud WZA
با Cloud WZA مدیریت سرور و ساخت کانفیگ‌های کلود ساده‌تر از همیشه شده است!
🤖
یک ربات تلگرامی قدرتمند برای ساخت کانفیگ و مدیریت سرویس‌ها، با امکان دیپلوی سریع پنل‌های محبوب:
⚡
Nova
⚡
Zeus
⚡
BPB
⚡
Nahan
فقط با یک دکمه پنل موردنظر خودت را دیپلوی کن و بدون دردسر شروع به استفاده کن
✅
✨
امکانات Cloud WZA:
🔹
ساخت و مدیریت کانفیگ کلود
🔹
دیپلوی خودکار پنل‌ها
🔹
مشاهده میزان مصرف کاربران
🔹
ساخت کاربر جدید
🔹
مدیریت کاربران
🔹
تغییر رمز عبور
🔹
مدیریت آسان و سریع از داخل تلگرام
Cloud WZA؛ راهی ساده، سریع و هوشمند برای مدیریت سرویس‌های کلود
☁️
🚀
🤖
ربات:
@nova_wzabot
ــــــــــــــــــــــ
توسعه داده شده توسط AssA
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=bbvf5Dlsv0yM85zja9ii6xTfjUGdsmjbJ00_upsbE9e5zV5wBIKxuu-DcRgWJ5DNA7ALRhNbb7SWZOkT49PBek2E58kevnqjjiilBaZGIV1WpWmRoO0psAfDaHYVfxQkHprqSOR-Kg5Tn42jPix1LzXO7D4spg2QEtQ8MnxYukauteSWPb0Mo5ARSu1jT9FkniTeGNNt-HsHGcaUGGz6QL7f63KbiOrNvmqa6LBp2rBKgJj67xw-6SH7yk7hYc74J2SKAbgwd1sQb_ih-S0D1-owxU0gQhnjRgJMcCrolOEWnhepl0nL8YQriex57IIFUcza0_I5Omg6tBfFm1HMig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=bbvf5Dlsv0yM85zja9ii6xTfjUGdsmjbJ00_upsbE9e5zV5wBIKxuu-DcRgWJ5DNA7ALRhNbb7SWZOkT49PBek2E58kevnqjjiilBaZGIV1WpWmRoO0psAfDaHYVfxQkHprqSOR-Kg5Tn42jPix1LzXO7D4spg2QEtQ8MnxYukauteSWPb0Mo5ARSu1jT9FkniTeGNNt-HsHGcaUGGz6QL7f63KbiOrNvmqa6LBp2rBKgJj67xw-6SH7yk7hYc74J2SKAbgwd1sQb_ih-S0D1-owxU0gQhnjRgJMcCrolOEWnhepl0nL8YQriex57IIFUcza0_I5Omg6tBfFm1HMig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KREA.AI
Enhancer
تصاویر پیکسلی را تا 22K ارتقا دهید!
دیگر نگران کیفیت پایین عکس‌هایتان نباشید؛
KREA.AI
با ابزار قدرتمند Enhancer خود، تصاویر بی‌کیفیت را به وضوح خیره‌کننده تبدیل می‌کند.
🖼️
✨
✨
قابلیت‌ها:
•
🔹
ارتقاء کیفیت تصاویر تا وضوح 22K
📈
•
⚡
تبدیل پیکسل‌های بی‌کیفیت به جزئیات واضح و شارپ
🔍
•
🛠️
استفاده آسان و سریع برای نتایج حرفه‌ای
🚀
🌐
Site
#AI
#ImageEnhancement
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR2P4eFsh4d-Pt1unyvn7XS8F876Wawoh3ZFUCX2nR_FHWqPDY8iGO5FtGggEgZu098PPEzA4Qaj-cNVflJ9deMWeo1HgAUeD5-FpOiyICT7lkmBlncDxKzldhlVLFBbnqWoIEd6fA3MH1et7QfmhbDudorFMbtRozlZrFlg4zH1UIBfumbPcYPN1HqFUbAzITZ73O3KD1zlQs-skJZigDa979Rd0m-nLNUuy9Y8lRoeghry7Ks9W4_d1mnDf8mHBoKtgm2hNkxpPqtXfpF32aJXoKrsqqKU1UKcoWM94cxs-RhU8vknACSr6YWNzyiQbzj30mSlxgpPb7xZ-Yfy0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000 برنامه رایگان برتر برای آیفون و کل اکوسیستم اپل: یک دانشنامه واقعی از نرم‌افزارهای مفید در گیت‌هاب ساخته شده است!
🍏
در این مجموعه همه موارد ضروری پیدا خواهید کرد: از پیام‌رسان‌های امن گرفته تا ابزارهایی برای تماشای فیلم از طریق تورنت.
🎬
🔐
🌐
GitHub
#Apple
#iPhone
#FreeApps
#GitHub
#OpenSource
#Productivity
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=T3jwFFGUx9-FQAsgZKnTcD77nmqIpy3C6NEZWDzwLv6CsYzotOhTVMvnVjdAyp1UYPNwuViXCqYAYiQiKzj3OUm3TVOtU-V3Yz31c0g1VXIv4fkXDFJD7g-0tHXJW9B5b2KrHZ9zwkrmnVXtg36ctbDUrC768fOwrKC6ADlxM8L1nkDRLtpt7emHiG4voUZun2k0IVZKer1DzYfg2b7iBupeXDkqM4rbdrTOM5Teofw7MR9bJnVQDrkxO4eZHREuRvywN8b9EOOyW5EGr2gxY6mLe4f0N37-GAc8ZlFJZpYPudIyYoz2jmJvWhGR-lP8I5Wc1d01nXVmKNmawwHJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=T3jwFFGUx9-FQAsgZKnTcD77nmqIpy3C6NEZWDzwLv6CsYzotOhTVMvnVjdAyp1UYPNwuViXCqYAYiQiKzj3OUm3TVOtU-V3Yz31c0g1VXIv4fkXDFJD7g-0tHXJW9B5b2KrHZ9zwkrmnVXtg36ctbDUrC768fOwrKC6ADlxM8L1nkDRLtpt7emHiG4voUZun2k0IVZKer1DzYfg2b7iBupeXDkqM4rbdrTOM5Teofw7MR9bJnVQDrkxO4eZHREuRvywN8b9EOOyW5EGr2gxY6mLe4f0N37-GAc8ZlFJZpYPudIyYoz2jmJvWhGR-lP8I5Wc1d01nXVmKNmawwHJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک برنامه‌نویس جوان توانست با ترکیب علاقه و مهارتش، درختی که با پایتون کدنویسی کرده بود را به قیمت 8 هزار دلار بفروشد. این پروژه از 100 دلار شروع شد و در چند روز به این قیمت رسید
🤯
#Python
#Programming
#Business
#DigitalArt
#Success
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter
وارد سایت
Agentrouter
شوید
با حساب Github ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Token
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://agentrouter.org/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا آماده استفاده است
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
دسترسی رایگان به API غول‌های هوش مصنوعی!
با لینک زیر به جدیدترین مدل‌ها دسترسی پیدا کنید:
🔹
GPT 5.4
🔹
Claude Sonnet 4.6
✅
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
🔗
zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=sytm_Wb2dPMmsw-g9eAG-IK0FkdCn2goDt7mseh6sCjsHxu5Wd_4UAscbHjzEyD--CBBkaKnsHpvJ8nRmCSzVMevv676O9xUEc4ACuqGTA8jv2De4Mrty9L3AWzaiGpohaorWcP1GQNbQKRCwxHGdV5Nh0C_t5s-2QA6cx0vTGJYtV41gShShOyGjmWyOEqz0tGxmJW2xMIT0_MenkvM8dKj8hUOCEnrqOPhtju4ufzVwLb9UigrQGlOOHBBYe7tyCTyahRLdAYAxHECsHawZRjsqKrvTM0jkCO5Znw5qtn2TeVOKkHnSdtUDxRCKXbHZYhz08t-Mk5nrnnu6olvRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=sytm_Wb2dPMmsw-g9eAG-IK0FkdCn2goDt7mseh6sCjsHxu5Wd_4UAscbHjzEyD--CBBkaKnsHpvJ8nRmCSzVMevv676O9xUEc4ACuqGTA8jv2De4Mrty9L3AWzaiGpohaorWcP1GQNbQKRCwxHGdV5Nh0C_t5s-2QA6cx0vTGJYtV41gShShOyGjmWyOEqz0tGxmJW2xMIT0_MenkvM8dKj8hUOCEnrqOPhtju4ufzVwLb9UigrQGlOOHBBYe7tyCTyahRLdAYAxHECsHawZRjsqKrvTM0jkCO5Znw5qtn2TeVOKkHnSdtUDxRCKXbHZYhz08t-Mk5nrnnu6olvRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAKCNol9PXsfblAO_vWGjrNFqJQg62mGBjFR8omD5WWhtSR-OE_U2-NKDzEaio6frYCmahdbAeFFOqc4y-7wK_DaycKxs8Ab4DHvL6fbcgV0FVH2eSlLdUuQ5gRcIee0-FWSWRfnK5LJ3zxaddsPdSvB85K_w9B5sIcMRE045iPJWjyFWDGWMf3nUl4Ksa2hx50jRPeC7uWSnyYnAwzM2AbGFj3DXD73shxTHhWRjQoOrHNzkDZh1l3rT3G3cw1EJiGQRYoAASppslL907jJVq7kPNwO2z9kyXNZ-obndTWC_OPnT_se9723uLGLRLpsUcGkGzBXz6rhG9Le3yW5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یه ترفند خفن برای چند برابر کردن سرعت گوشی‌های سامسونگ!
احتمالاً شما هم فکر می‌کنید هرچی مقدار RAM بیشتر باشه سرعت گوشی بالاتره، اما یه گزینه‌ای تو گوشی‌های سامسونگ هست به اسم RAM Plus که به صورت پیش‌فرض روی همه مدل‌ها فعاله و برخلاف اسمش، تو خیلی از مواقع باعث لگ و کندی اعصاب‌خردکن میشه!
🤦‍♂️
🧐
اما چرا این اتفاق میفته؟
قابلیت Ram Plus در واقع میاد بخشی از حافظه داخلی گوشی رو به عنوان «رم مجازی» اشغال می‌کنه تا برنامه‌های بیشتری تو پس‌زمینه باز بمونن. از اونجایی که سرعت حافظه داخلی به مراتب از رم فیزیکی (سخت‌افزاری) خود گوشی پایین‌تره، وقتی سیستم می‌خواد اطلاعات رو بین این دو جابجا کنه، پردازنده بی‌دلیل درگیر میشه و گوشی کُند میشه.
🛠
چطوری غیرفعالش کنیم تا گوشی پرواز کنه؟
کافیه وارد تنظیمات گوشی بشید و دقیقاً این مسیر رو برید:
⚙️
Settings > Device Care > Memory > RAM Plus
(اگر منوی گوشیتون فارسیه: تنظیمات > مراقبت از دستگاه > حافظه > رم پلاس)
گزینه بالای صفحه رو روی حالت Off (خاموش) قرار بدید.
بعد از این کار گوشی ازتون می‌خواد که یک بار ری‌استارت بشه)
✅
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
معرفی MinerU؛ استخراج جادویی و سریع متن از انواع فایل‌ها!
📄
✨
اگر برای پروژه‌های هوش مصنوعی (مثل RAG)، کارهای تحقیقاتی یا روزمره نیاز به استخراج متنِ تمیز از فایل‌های مختلف دارید، ابزار رایگان و متن‌باز
MinerU
یک شاهکار به تمام معناست!
🔥
ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
پشتیبانی همه‌جانبه:
تبدیل فایل‌های PDF، Word، Excel، PowerPoint و حتی اسناد اسکن‌شده به متن خالص و بدون به هم ریختگی.
2️⃣
سرعت پردازش خیره‌کننده:
می‌تواند یک فایل PDF دویست صفحه‌ای را در کمتر از ۱.۵ دقیقه پردازش کرده و متن آن را استخراج کند!
3️⃣
اجرای کاملاً محلی (Local):
بدون نیاز به اینترنت و سرورهای ابری روی کامپیوتر خودتان اجرا می‌شود که برای حفظ حریم خصوصی فایل‌های حساس بی‌نظیر است.
4️⃣
بهترین دوست هوش مصنوعی:
پشتیبانی از پردازش گروهی فایل‌ها (Batch) و قابلیت ادغام و همگام‌سازی بی‌نقص با ایجنت‌های هوش مصنوعی مانند
Claude
،
Cursor
و سایر LLMها.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#MinerU
#PDFExtractor
#OCR
#AI
#Claude
#Cursor
#OpenSource
#Github
#Tools
#RAG
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljuxP-eJlhQSEPdVojKae52aSqiT2TUWNCON7hSkNUYySd_haEXxMS3uWCI3mOlVO6ZtlvFVP5vBH9OKmJ2uxWqSSH4ua2WIkJFCX0xy-fxgZAWRJz62bX1NxK9TG6ojmR4GnhpeYV_9xCMwxJ5lGvIIvJWjITY5UN9vAeixgDXu8QuxHejPbXxV1eyiaBWqK74biwP66DI-9EFTriHcjePbhE9TwOKxLfLg_43-CZZlpzIuM3hrN80JkFS-GqHtbq6P7T7BKkjwAn47pRBXF354CUqK3PuK5yc6EOSG5gsskA7Shgx8AITb9av9xUgV9jLlFWCJJV1p1cyp8JHhPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Popit Music: ساخت موسیقی با هوش مصنوعی و مالکیت کامل اثر
🎵
✨
قابلیت‌ها:
•
🔹
انتخاب ژانر و حالت برای تولید سریع ترک
•
⚡
ورود خودکار به پلی‌لیست و رقابت با آثار دیگر
•
🛠️
مالکیت کامل حقوق موسیقی متعلق به شماست
•
📦
دو بار تولید رایگان برای شروع
🌐
Site
#AI
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
