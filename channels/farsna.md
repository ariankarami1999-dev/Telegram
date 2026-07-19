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
<img src="https://cdn4.telesco.pe/file/r5kromcne9Nj0cZiR-SZRkIKjSK-QyDxwMynKPhCn79eqt8lo0uTxd7vQlbPbkgjVZw9hfWzZHXd-mRXl63H4WQBinBEa1rEa63r7J9wtik4DMJq9kLlLgpeV6aXN_JDk65mBeIQTW41s9MF3hkJzgBO7HPNaT-3MPiCEesuHt-vm0GGDHOfzeOkyan-orJvTiblcR8_3r-i31kcBl_8lAGGAIFmhEsPQkGVg6K50AG75pNXqSkNWYN0jFfNGBOqpzsYyAHR29d4ASHaOlbTisb_uwk2ETqkpJXjWi7CZJ-Lu3RqEUPt003Vm-ZK3_ZR78ucdrcffkFpVoVaQaMyqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 13:15:04</div>
<hr>

<div class="tg-post" id="msg-451082">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Flo3Wdrx9CEKyW4Pz2fobBlGJd6FlJtK1D539gN79WqiDsEy_0WS65ahh7-oFDuasV4V8kFtMO5h2i8HIsgK7zdslkCfkgyv0SmLc9lhwbWucAEMvBhSsT9AyCz9KZeYLysr-0pfU5kJOsckt2dJcs-r1y_kx2gaDQRi3NOsNfEgRU_Tecy1TSzerOEEDNWSEctDRVXOHVUadAqd00hjaHjmyVxdXnVeu3pAV3Yhu67MBAT4V7Qvx1tkhq9g-y2LUXNnKRtEQax0StxxvwW7g0gjT7EKdlbOENueaYZxPbxKt_md6w7JSGKYOEKG8vW1k-SCquLXDc9gFV_nMjjtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: از اصولی‌ترین امور، اصرار بر اتحاد مقدّس در همه‌ی سطوح است؛ پرهیز از تفرقه و تنازع وظیفۀ همگانی است
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/451082" target="_blank">📅 13:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451081">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef42aff8c.mp4?token=mWd6NmHc_Pu4FafrmB-kGdhLPJRcFpKb8vy3wVnWsR_qSoa53xKWeysO1Wp34RoSXiGD8tJW0_oUypjFLjeozZ4v2n0Iy_5w-XQlr8JvU1hgzEirxxtIRcprVsrkMOOxrxz_0OuLsYjI6-rfjdWBFVI8fDYI9xxsyC6wzK-KhOklNlksfe729UT-Cs9QM4NqZiyRH_llrrACnAEXH8Qps0e5isOQmFssDTQOR1u1WJKdgXa_GHyb3LkVxYWK7thcLGlk6Xu8vUnbVSswOYYzDSRcc-A3LKhn8t2IYwyHLfkc7f-pbHfFqHH_3uEhyO3WxWkEneoc9zOdkCWU6ATTFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef42aff8c.mp4?token=mWd6NmHc_Pu4FafrmB-kGdhLPJRcFpKb8vy3wVnWsR_qSoa53xKWeysO1Wp34RoSXiGD8tJW0_oUypjFLjeozZ4v2n0Iy_5w-XQlr8JvU1hgzEirxxtIRcprVsrkMOOxrxz_0OuLsYjI6-rfjdWBFVI8fDYI9xxsyC6wzK-KhOklNlksfe729UT-Cs9QM4NqZiyRH_llrrACnAEXH8Qps0e5isOQmFssDTQOR1u1WJKdgXa_GHyb3LkVxYWK7thcLGlk6Xu8vUnbVSswOYYzDSRcc-A3LKhn8t2IYwyHLfkc7f-pbHfFqHH_3uEhyO3WxWkEneoc9zOdkCWU6ATTFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: آتش‌بس اولیه با آمریکا در جلسات کوچک‌تر از شورای‌عالی امنیت ملی پذیرفته شد
🔹
وظیفهٔ تحلیل وضعیت برای جنگ یا آتش‌بس با شورای‌عالی امنیت ملی و وظیفهٔ تصمیم‌گیری دربارهٔ آن با رهبری است. هرکدام از اعضا وظیفهٔ ارائهٔ تحلیل دربارهٔ بخش خودش را داشت.
🔹
جلسهٔ شورای‌عالی امنیت ملی برای تصویب یادداشت تفاهم با آمریکا از ساعت ۹ شب تا ۳ صبح طول کشید. آتش‌بس اولیه در شرایطی پذیرفته شد که امکان تشکیل جلسهٔ شورای‌عالی امنیت ملی وجود نداشت و شرط آتش‌بس این بود که مبنای مذاکرات، ۱۰ بند پیشنهادی ایران باشد.
@Farsna</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/451081" target="_blank">📅 13:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451080">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">۲ کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و ۲ کشتی دیگر از ادامه مسیر ناایمن منصرف شدند
🔹
نیروی دریایی سپاه: ساعاتی پیش ۴ فروند کشتی متخلف با شیطنت و حمایت تروریست‌های امریکایی و با خاموش نمودن سامانه‌های ناوبری و بی‌توجهی به اخطارهای پایگاه کنترل تنگه هرمز نیروی دریایی سپاه، قصد اخلال و خروج از تنگه هرمز را از مسیر ناامین داشتند که ۲ فروند از آنها دچار حادثه شده، در جای خود متوقف گردیدند و ۲ فروند دیگر از ادامه مسیر منصرف شدند.
🔹
نیروی دریایی سپاه اعلام می‌دارد که کنترل تنگه هرمز در اختیار کامل این نیرو است و تنها مسیر عبوری ایمن مسیر مشخص شده و اعلام شده است و یک قطره نفت و گاز و کود شیمیایی همانگونه که قبلا گفته شده، بدون هماهنگی و اجازه از تنگه هرمز عبور نخواهد کرد.
🔹
شناورهایی که تحت تاثیر صحبت‌های دشمن آمریکایی قرار می‌گیرند و وارد مسیر ناایمن می‌شوند مطمئنا دچار حادثه خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/451080" target="_blank">📅 13:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451079">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24b3ea8cb.mp4?token=TmMIQV9mWVT4lUdvi9Ab1nv7GDusCL4iKQp8OZnak1bp3VPC3bnbfzNCH6RvZ02uwU3Tk1lxlyNy5n5y79pmMKjOgRNRy39qz1UUqfP8bFHMPMd4dGr8t_ufqp33hsIc5fOw0cvRawXweUfPIcV5pYPww9jRSTsMfQCPvjYFqnxjYvN60PMzB5WuoiPc6UKaQef2f4t31l7tg9eh0WsJd55WuRLx-59Y3mLnuPiSiXA9K5tCMlfhwQiXFmIVxUdNa-wGY9YHXqPhldOrLmhtIoaNKeIEB9lA6FM3HUcbchPnjwMNlGTg1OPusGxCkdYKy_Mff43IiuUJJ0QmYTfdtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24b3ea8cb.mp4?token=TmMIQV9mWVT4lUdvi9Ab1nv7GDusCL4iKQp8OZnak1bp3VPC3bnbfzNCH6RvZ02uwU3Tk1lxlyNy5n5y79pmMKjOgRNRy39qz1UUqfP8bFHMPMd4dGr8t_ufqp33hsIc5fOw0cvRawXweUfPIcV5pYPww9jRSTsMfQCPvjYFqnxjYvN60PMzB5WuoiPc6UKaQef2f4t31l7tg9eh0WsJd55WuRLx-59Y3mLnuPiSiXA9K5tCMlfhwQiXFmIVxUdNa-wGY9YHXqPhldOrLmhtIoaNKeIEB9lA6FM3HUcbchPnjwMNlGTg1OPusGxCkdYKy_Mff43IiuUJJ0QmYTfdtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی: کویت بداند وضعیتش در پایان این جنگ عادی نخواهد بود
🔹
حملات از کویت را حملات مستقیم تلقی می‌کنیم و بدانند که به‌صورت ویژه ادبشان خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/451079" target="_blank">📅 12:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451078">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=j-Q_0c8W5Bkg-v7xfpatYyVfO7MMiM21RF_rdjUV-ZmriQozShP1Pb_SaEAFX4lEjZmzsAGckBGGTjzYuVS-M7qw68L_VLklu_4LVA3Pc_gWJk-5sKlzjCX2EyUfsiAyrH2ZF5mWYPGz9UUDBNOSv8gnqxwUNHbVHnZL_oecpw7oUzi086vMiYwd_JD2HU_lbeRLU552N9NXppxV4tnbSOkgjj7Rf3_lLFGQG-tOm-y31un5j44PimDd8No3jHaj-PH5jOYv35bQUzDMCNwe-dDd2R8kiPWswK1fpICZe_bFZthnHOAwfJoJgPwgXgJFSb8CjE8EbywcNF9LY29CYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=j-Q_0c8W5Bkg-v7xfpatYyVfO7MMiM21RF_rdjUV-ZmriQozShP1Pb_SaEAFX4lEjZmzsAGckBGGTjzYuVS-M7qw68L_VLklu_4LVA3Pc_gWJk-5sKlzjCX2EyUfsiAyrH2ZF5mWYPGz9UUDBNOSv8gnqxwUNHbVHnZL_oecpw7oUzi086vMiYwd_JD2HU_lbeRLU552N9NXppxV4tnbSOkgjj7Rf3_lLFGQG-tOm-y31un5j44PimDd8No3jHaj-PH5jOYv35bQUzDMCNwe-dDd2R8kiPWswK1fpICZe_bFZthnHOAwfJoJgPwgXgJFSb8CjE8EbywcNF9LY29CYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی: پاسخ ما به حمله به آسایشگاه ارتش در چابهار برابر نبود؛ بلکه حداقل ۳ برابر بود
🔹
تلفات آمریکا در سوریه بیش از تلفات سربازان مظلوم ما در چابهار بود. @Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/451078" target="_blank">📅 12:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451077">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3595950301.mp4?token=t-szDELbs81mJwHLuX_9dZtNsZZUxCbcwGgRZZbDCBJHA1IH_Z4mGwNaHJf7wdJxMsYrUK_WT5NToArLSCRhmRw8bpbcLW4PRRvaJayziTwmw_2gqeYGzatsJlOEchcFE_NOfcmrQyeoxPFFwWzHrJjl9opyNhjBnKxVkk_EuI7rwNOcivRtIZljUyNvSL5_jTjAz1wtSYq_KF2Q4kLQP5GEVQld8qm2vaKYME7oANSAk_SeO8c0Qlvyp09XqL2l8meYyn6PPsX522QO8lM6cHPm8rSmBW7qcm5tIdz2s_ASPOwjjg_12X_zhkV6GoXfy3e6C6Evwy6vXAyfsljQUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3595950301.mp4?token=t-szDELbs81mJwHLuX_9dZtNsZZUxCbcwGgRZZbDCBJHA1IH_Z4mGwNaHJf7wdJxMsYrUK_WT5NToArLSCRhmRw8bpbcLW4PRRvaJayziTwmw_2gqeYGzatsJlOEchcFE_NOfcmrQyeoxPFFwWzHrJjl9opyNhjBnKxVkk_EuI7rwNOcivRtIZljUyNvSL5_jTjAz1wtSYq_KF2Q4kLQP5GEVQld8qm2vaKYME7oANSAk_SeO8c0Qlvyp09XqL2l8meYyn6PPsX522QO8lM6cHPm8rSmBW7qcm5tIdz2s_ASPOwjjg_12X_zhkV6GoXfy3e6C6Evwy6vXAyfsljQUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی: فلسفهٔ حضور ما در جنوب این است که به آمریکا بگوییم «ما آمده‌ایم که پدر شما را دربیاوریم»
🔹
حضور ما فقط برای دفاع نیست. طرح «پاسخ پشیمان‌کننده» درپی حمله به زیرساخت‌ها درحال نهایی‌شدن است. @Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/451077" target="_blank">📅 12:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451076">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7n1deLXgs-R9m_dTFq3mVFqo3BEJhO41DfTbRZxBZGgawYILHPFygWts60j3NWPkcFwnjoVrGSbvJQV97KNVlweXiATWAvGMUZe3EmNAdPZUn12ct_Voajp7zteCiluMVEMB27qT_XJMy0IXhvx4uYg4mun4vtqrtStguIeZaPRTYmSJSdbzue5qZGRN4_eencH3C9X4Hj8gLYGxcNj3L1iGItH39OQL1R7TVPE7mJvB9-ymzIa6QRDjl-l-0nsqWusFXv2znRjUf7pVLrBK5pnihk8-x2zKFGlo1afQ_y-t7R6qZ2QtEAuLidWd5vnfxDkKrdaskT5JtchcyEyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۲۲ هزار واحدی به ۴ میلیون و ۷۵۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/451076" target="_blank">📅 12:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451075">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b7a1178d.mp4?token=eCkjRPWpNVeXdMZb0z2eC_d3iq_OQVdIMkm7Oay9rBd1MNfoeYMiUF4lMViH7zueKIwW242KZNWYW7VtXMGauaP-fTuYAL3LMXMLz0cCDSTFMhp9DI3fcBQ67ERtSfzyZPFiQVSe9lFUUCSSn7d4l9jzTbJZ5Ku3redfGkSucuPnx0u9JdjOvdyH2Xb4cIikIATSlY-AKHEOUrVa3BUL7jSeKsnTkOiMGTCch1GM3uUGItkESx5o48VxR6pvhP2Sq6oY8u3L6NSd8XYmp4m-L5jDsghG0UWHEbKpY5HNfuj-3RM4mVEy4qTF2GMVh0k-BIxUeGrG_Hv5SMOzboCxjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b7a1178d.mp4?token=eCkjRPWpNVeXdMZb0z2eC_d3iq_OQVdIMkm7Oay9rBd1MNfoeYMiUF4lMViH7zueKIwW242KZNWYW7VtXMGauaP-fTuYAL3LMXMLz0cCDSTFMhp9DI3fcBQ67ERtSfzyZPFiQVSe9lFUUCSSn7d4l9jzTbJZ5Ku3redfGkSucuPnx0u9JdjOvdyH2Xb4cIikIATSlY-AKHEOUrVa3BUL7jSeKsnTkOiMGTCch1GM3uUGItkESx5o48VxR6pvhP2Sq6oY8u3L6NSd8XYmp4m-L5jDsghG0UWHEbKpY5HNfuj-3RM4mVEy4qTF2GMVh0k-BIxUeGrG_Hv5SMOzboCxjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شریعتی، نمایندهٔ مجلس در مناطق مرزی جنوب: آبادان نماد جوانمردی و حصرشکنی است
🔹
پالایشگاه آبادان نماد حصرشکنی نسبت به تحریم است. آمریکا نتوانسته و نخواهد توانست این کشور را محاصره کند. @Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/451075" target="_blank">📅 12:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/451074" target="_blank">📅 12:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9704386c34.mp4?token=tZJVR2N9UyPwH38zItcS_cTz-jaQZavFiv3tnR1HE3yWuMfYJU-cjYiWo3CKOEJTzfOouGIw3BooHDo8fP_eiNDLc8voAdLjQ2J3j-x5UCkeoxJ2bK8L-hm0XanpZTVHyUKB2bfX9mxAiASUeXCpo6oHflIlBl8W6PbSadmHwCm7dLXRAea4Rm5ZW3RuNAdwwl33h7VY7iHeGOr3cHXMprVL7IVpIsDldutNA3u16GXZ7aEmKumWuysVH1jTpbqSpOmHdIjqqLqpjTH1PnbsIkOAde94p1EQc1kMXMx7Ksci36d5LibjJn3LggyIDvIlL2Kq63K1e5trPUBrZHBLUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9704386c34.mp4?token=tZJVR2N9UyPwH38zItcS_cTz-jaQZavFiv3tnR1HE3yWuMfYJU-cjYiWo3CKOEJTzfOouGIw3BooHDo8fP_eiNDLc8voAdLjQ2J3j-x5UCkeoxJ2bK8L-hm0XanpZTVHyUKB2bfX9mxAiASUeXCpo6oHflIlBl8W6PbSadmHwCm7dLXRAea4Rm5ZW3RuNAdwwl33h7VY7iHeGOr3cHXMprVL7IVpIsDldutNA3u16GXZ7aEmKumWuysVH1jTpbqSpOmHdIjqqLqpjTH1PnbsIkOAde94p1EQc1kMXMx7Ksci36d5LibjJn3LggyIDvIlL2Kq63K1e5trPUBrZHBLUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاک، کارشناس جبههٔ مقاومت: وظیفهٔ ما حفظ جبههٔ مقاومت و پاسداری از خون حاج‌قاسم و شهید نصرالله است.  @Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/451073" target="_blank">📅 12:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451072">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a85689b0.mp4?token=ChGRRTw19gZJYDz5wHXaPcH4XVIosWNU_8s8A-gXlhLO_jZ5E1c8ajG49-eZviKkfmFAdWygdbxBlDSeToljBhbDPgAmSlKZkizEaQVSyNAdaL1-54bw--i3AUO8CdRZIiRsS_xi_OPF-NPTdYqvFvFutGBJ3-KBkeYSSoP7Zqmr6lcx9fvIfGmfIC057XR6Y3u9CE3icDOF2eQy9aDb6BYgooPIHtDIBku6iqzR3OfdtMXDtEjATy8FvzuwBpdSW86L21T6Qo-2UUXiU1uyTL3AoJQYzjgMD82SUdhM9666F8qwqF4LVx97RCz5mNZqBOOY0bOCurcn5cJixAWCCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a85689b0.mp4?token=ChGRRTw19gZJYDz5wHXaPcH4XVIosWNU_8s8A-gXlhLO_jZ5E1c8ajG49-eZviKkfmFAdWygdbxBlDSeToljBhbDPgAmSlKZkizEaQVSyNAdaL1-54bw--i3AUO8CdRZIiRsS_xi_OPF-NPTdYqvFvFutGBJ3-KBkeYSSoP7Zqmr6lcx9fvIfGmfIC057XR6Y3u9CE3icDOF2eQy9aDb6BYgooPIHtDIBku6iqzR3OfdtMXDtEjATy8FvzuwBpdSW86L21T6Qo-2UUXiU1uyTL3AoJQYzjgMD82SUdhM9666F8qwqF4LVx97RCz5mNZqBOOY0bOCurcn5cJixAWCCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانعلی‌زاده، کارشناس مسائل بین‌الملل در مناطق مرزی جنوب کشور: آمریکا که قرار بود امنیت کشورهای عربی را برقرار کنند، امروز توانایی دفاع از پایگاه‌های خودش را هم ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/451072" target="_blank">📅 12:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451071">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e2f40d35.mp4?token=g2T6R9B_1uEBM9x-DIh6vtkMJI-hWCMLxykpc9OkiPTVBQ_YvhzFN6L3EUf1O7mF-usdbJaVdLewRwO2uidPDV6HCsZzdGHgFqx1jgwHkPYsil1YOx5T9GoxPqdkgl81Yghzx-XMlWHLsqxLfPeWqrDYYCosT44E1vXgh3rT44CxUVPzz29wiGz7fedZWkrb_-AR097JaFogHztb8pIuAYdRfDJUHiPtYk0uw1oa92blTjh0XcdePOCuH5z7y3M5owjzv5FyN1gjJxpxU1R1qoKRilcvVVmyoQkx6RrYQLS66SemVe5Bgfcp6o53smwN4wvOHw6XRT914eYPWqUYMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e2f40d35.mp4?token=g2T6R9B_1uEBM9x-DIh6vtkMJI-hWCMLxykpc9OkiPTVBQ_YvhzFN6L3EUf1O7mF-usdbJaVdLewRwO2uidPDV6HCsZzdGHgFqx1jgwHkPYsil1YOx5T9GoxPqdkgl81Yghzx-XMlWHLsqxLfPeWqrDYYCosT44E1vXgh3rT44CxUVPzz29wiGz7fedZWkrb_-AR097JaFogHztb8pIuAYdRfDJUHiPtYk0uw1oa92blTjh0XcdePOCuH5z7y3M5owjzv5FyN1gjJxpxU1R1qoKRilcvVVmyoQkx6RrYQLS66SemVe5Bgfcp6o53smwN4wvOHw6XRT914eYPWqUYMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادیان: رهبر امت به ما وعدهٔ پیروزی داده
🔹
مردم‌سالاری دینی در دورهٔ رهبر شهید به بالاترین حد خود رسید و کار را به ملت مبعوث شده سپردند. @Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/451071" target="_blank">📅 12:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767f04b69b.mp4?token=oH6hwtBuIiiGClSfEgrwJR9T9Sl3OstAYSlXX4BXjxafBbslyAP9f0yqyERmNSh2p9vlAeiX-1rHCKLicvYyUmMkXfcLa7mAhwfROEu7lJrsjHk9xQ6BjqR5MKjDCq7dB19hdu4bi318KaNrAbv4cNJPsVd9jnyRCPyvL5YCEf6Z6RpyMC25KxSQqqZNZePMxwsVYqW40Kr9T5ZNE9Vw_NbesLp7eVZVpmNrE7JIjdm_X5SjizwStvip-jbjaCNdaGecTl2UbJ3ZgQ1_O0EG1SQ0aGNBMKGc0s_wyjIW__bj7saX6a38f8L4UEh9rOmyimN0GTrPaiCAP1RZRZd8ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767f04b69b.mp4?token=oH6hwtBuIiiGClSfEgrwJR9T9Sl3OstAYSlXX4BXjxafBbslyAP9f0yqyERmNSh2p9vlAeiX-1rHCKLicvYyUmMkXfcLa7mAhwfROEu7lJrsjHk9xQ6BjqR5MKjDCq7dB19hdu4bi318KaNrAbv4cNJPsVd9jnyRCPyvL5YCEf6Z6RpyMC25KxSQqqZNZePMxwsVYqW40Kr9T5ZNE9Vw_NbesLp7eVZVpmNrE7JIjdm_X5SjizwStvip-jbjaCNdaGecTl2UbJ3ZgQ1_O0EG1SQ0aGNBMKGc0s_wyjIW__bj7saX6a38f8L4UEh9rOmyimN0GTrPaiCAP1RZRZd8ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعوت حدادیان از سربازان آمریکایی: پایتان را به کشور ما بگذارید ببینید چه بلایی سرتان می‌آید
🔹
آنهایی که می‌گفتند «نه غزه نه لبنان» خوب بیایند جنوب ایران!  @Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/451070" target="_blank">📅 12:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451069">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkZ7aBkaLt7fv4Bwgg9JGRqpCPlu-XCJFIfVsUdXBtjTpc3PNr2Sw8N-3O6Ah_YX5i_vpb1Mu2ck2YPghU7WXiSL3NAT9ZOcme18NkYsWJC9QHcDJOEkN-G_O-lSSbb5Tsk5I0Mh7CsIfWVR-XubFUKhTy7IR4q6M3x3ld07kw9eW8CD1y8MTyjxE8_EsjbzkH0h173vstiNSxLSB_fiLYX6hFBlHAiC4m7NpD0nCqkJxQdRkVXZ8M1K9IMgaD3FKPLkCsmX2GiRRzer0ikSX1g5evLeN0_CsRmrXXie3K6UTET9ev38MLVQtvFeZWVyOwiBai_8Jom1HLc17-l_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار فرمانده نیروی زمینی ارتش با خانوادۀ شهید موسوی
🔹
امیر جهانشاهی: اعتماد امام شهید امت در انتخاب شهید موسوی به ریاست ستاد کل نیروهای مسلح اعتماد به ارتش بود. امام شهید، شهید موسوی را یک فرمانده بزرگ می‌دانستند و در امور نظامی او را تحسین می‌کردند.
🔹
یکی از ویژگی‌های شهید موسوی استکبار‌ستیزی بود. در تمامی توصیه‌ها و سخنرانی‌های شهید موسوی نسبت به مقابله با استکبار تأکید شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/451069" target="_blank">📅 12:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451068">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZecLq3yddwsPMvCZkdB3Jmdb1yrp7DOYwdVzU365f_c3BlhKSOYjMBDBKWNqmzOw_icLF3Y9DeUuZypV1m1KP66uvXMa-auqF493XL_NNWntRJft43zIWcRdJhW15_NR8PPb6D6otcPSgu2GQruMTKDsXAp-IP2LeK6XpgeA5AoDtmxkwa-O2hPC3gUOmHw2e5SsTjRZa6M3kjb-8ptluhcF1JDeozMmKsSlDzvhGM9uIo5CcQHqfl-KmfJvhXNCjocRY2gYLPkF6XZiKDCmDBSFGs4xs_eW7wKmQT3dPIW7Sslizf5kz5U6tekmWV0Xb7XrSkADr3CKoqrvyFxXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب آزادکاران ایران در بازی‌های آسیایی مشخص شد
🔹
۵۷ کیلوگرم: علی مومنی
🔹
۶۵ کیلوگرم: عباس ابراهیم‌زاده
🔹
۷۴ کیلوگرم: یونس امامی
🔹
۸۶ کیلوگرم: محمد نخودی
🔹
۹۷ کیلوگرم: امیرعلی آذرپیرا
🔹
۱۲۵ کیلوگرم: امیرحسین زارع
🔸
بازی‌های آسیایی ناگویا مهر امسال برگزار می‌شود.
عکس: رسول شجاعی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/451068" target="_blank">📅 12:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451067">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLkbY9SCGHilqFtACyS9U_RWcHQ_b95foj7tieRUtKH7kFgHenvJCKqX7Z-1Bqk7F79rtQuY893gqps6r-xeKhyZyZS64skZNH-vjVNEE2U9KP3h2qivIdJX1eEnHxDGkCD9DIKEONUK7B6spKZGmWclLBR0kSGMLl17nQQJkdmFfFoYjuXSYcNscy3Ao-aVTmRyX3TVJXRKutdclKORiOEN5ZksqFQosJ1TdIXImou1ISgmAYxuaMevFpK-iCVvq3oYo4YhN74v47xPw5Q0_EAkw0PoOE1SbU8yEphuxNuEhBS_SOd33LHNkBs9nGU4z4FcfuokPh1MesZQB0l5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین برآوردها از میزان شرکت کنندگان در بزرگترین تشییع تاریخ جهان
🔹
مراسم وداع و تشییع پیکر رهبر شهید انقلاب، در یک بازه ۶ ‌روزه و در ۵ شهر تهران، قم، نجف، کربلا و مشهد برگزار شد که با حضور حماسی و کم‌نظیر مردم، به بزرگترین رویداد تشییعی در تاریخ جهان تبدیل…</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/451067" target="_blank">📅 12:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451066">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06a001e7d.mp4?token=uoIP5Gm2b6yqhlsXhkSToNtXcNNDnJ8HQAA3tzRwzNhynn_JbmRdPVjiQDSe2U9DwXG3_eUzLyNbmAuaqZ49ZhakHgZHrA9OjhVZml6avl5PMGi4z4oYZwAEKX9N-Q5-9RuL645kAaxjkAfnN_nh4Tngyzibg4FDrSh2zBr61MLl38kyR8Zaux5PWLtUPQ87VHUT4n9U-fjtzmrsom_MJ_7dsGlof3naOWl7ji1Gz-l0UfRqgQ3IDn24O5DZ1iBRwXf-ADMjsFDYz4ga5opfYXD8N0H_cBhzfp33FyJzyBj_OZBV8wHV49o-lo76GEX7ycADK4ujr8A53_gY1_NpdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06a001e7d.mp4?token=uoIP5Gm2b6yqhlsXhkSToNtXcNNDnJ8HQAA3tzRwzNhynn_JbmRdPVjiQDSe2U9DwXG3_eUzLyNbmAuaqZ49ZhakHgZHrA9OjhVZml6avl5PMGi4z4oYZwAEKX9N-Q5-9RuL645kAaxjkAfnN_nh4Tngyzibg4FDrSh2zBr61MLl38kyR8Zaux5PWLtUPQ87VHUT4n9U-fjtzmrsom_MJ_7dsGlof3naOWl7ji1Gz-l0UfRqgQ3IDn24O5DZ1iBRwXf-ADMjsFDYz4ga5opfYXD8N0H_cBhzfp33FyJzyBj_OZBV8wHV49o-lo76GEX7ycADK4ujr8A53_gY1_NpdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انهدام یک فروند پهپاد MQ9 در آسمان بوشهر
🔹
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانۀ نوین پدافند پیشرفتۀ نیروی دریایی سپاه در آسمان بوشهر رهگیری و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/451066" target="_blank">📅 12:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451065">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHS7FVrytWnDFDrakJsnj5ns_hCqWg1s9qiUU_zvE6Dn-XRq6XTDjT_zqLC5-XPD_2EvshN6mI1ZIafwmrOOwK-LaPjI51Ddk8fQ_BO6vEYr2fPJVgJjFiwp0BvvGf97owcIQ_F66QxyolW1BiS10UYejX8YtqwztQeBSG9-rTFlCWAASMDocgnT9Hu5iENb9UGrjUb7hQuY018pvpivSO_bFUOg8t8m7vZjzVG6Ippve8nWTilaGnXIzxzgC-L5u8bMpQjFpQQ9eM58vCNTpxGxK7KqzLWzNyfX0gNJFyXtTJXdA3sA-YON2X9ME1bE4p4F2_YaoODyiXuzfEyLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا فرانسه ۶ تایی شد؟
🔹
شکست ۶ بر ۴ فرانسه برابر انگلیس تنها یک باخت نبود؛ این مسابقه به یکی از سنگین‌ترین فروپاشی‌های دفاعی تاریخ فوتبال فرانسه در جام جهانی تبدیل شد.
🔹
تیمی که تا قبل از این مسابقه در شش بازی تنها ۵ گل دریافت کرده بود، در یک شب ۶ بار دروازه‌اش را باز شده دید؛ یعنی بیشتر از کل گل‌های خورده‌اش در طول تورنمنت.
🔗
دلایل فروپاشی خروس‌ها را در
فارس
بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/451065" target="_blank">📅 11:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451064">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1f69b8faa.mp4?token=snLnGI3W08Ib94Tv7XMfY9sUyl3xdTE8vcAm7kAkrKQsfiIplQzd2TEZ4g66m6A5SOb6TmfQFgbmULm4TrPjoQqAscYJHD-DPPDc_VYEKBk4MMdcb2ZOxbo3M2aS_qLjqELEHdrT1t1SqBg9AEcVe3zUnOOzNbXQMvAYSUDSHjjpQEzq6zqaOG0wGz1EGfDaZbNgzSf4-P9SlsVAo6208f7I8YFNdv9u-wA8NOirH5YpEUP8_mAEES_quhPG-GxEh8765YOeSFBsQR6zXg-4P5egSfrKc-250SvKeaDz-CmDz3z1UcyWjVG4CeC6lLEpl6r2darDpWRV6G69B-u76g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1f69b8faa.mp4?token=snLnGI3W08Ib94Tv7XMfY9sUyl3xdTE8vcAm7kAkrKQsfiIplQzd2TEZ4g66m6A5SOb6TmfQFgbmULm4TrPjoQqAscYJHD-DPPDc_VYEKBk4MMdcb2ZOxbo3M2aS_qLjqELEHdrT1t1SqBg9AEcVe3zUnOOzNbXQMvAYSUDSHjjpQEzq6zqaOG0wGz1EGfDaZbNgzSf4-P9SlsVAo6208f7I8YFNdv9u-wA8NOirH5YpEUP8_mAEES_quhPG-GxEh8765YOeSFBsQR6zXg-4P5egSfrKc-250SvKeaDz-CmDz3z1UcyWjVG4CeC6lLEpl6r2darDpWRV6G69B-u76g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ثبت حضور یک قلاده پلنگ در گچساران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/451064" target="_blank">📅 11:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451063">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/451063" target="_blank">📅 11:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451062">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167d0f36a1.mp4?token=Af_p7uTEj1ZDtSgB2ska_qzdvvCPZPZQFF8oqSB1V_-0oZxm_LTojRAXyqEA_SXoaXqdzpXKbNwO6g0s1I4ykZquMYv_RjV99KtrkC8UC-XFbzMxgw7F5c1a-s-VR3k_V8OjbPL4_Fzv4Kf_Z4tWL73A-XgSm_AxsMBCYnf2lLfh6njZUBufdwmoy9mnppNXE0EB01JJu8w_S6DkTwmcTnuHiTHu5vjhXUS7MN3YJdaO8fe7LtqDQzdrir4N8Djsxeh-yXrfn9YqBq65tr3WPlZnsKDuZeZV6cT_hTyDVAAWmMYeHyhLyCuY7aM0ACbP3cWnyxnmxQ1n2S6u7vBeYRFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167d0f36a1.mp4?token=Af_p7uTEj1ZDtSgB2ska_qzdvvCPZPZQFF8oqSB1V_-0oZxm_LTojRAXyqEA_SXoaXqdzpXKbNwO6g0s1I4ykZquMYv_RjV99KtrkC8UC-XFbzMxgw7F5c1a-s-VR3k_V8OjbPL4_Fzv4Kf_Z4tWL73A-XgSm_AxsMBCYnf2lLfh6njZUBufdwmoy9mnppNXE0EB01JJu8w_S6DkTwmcTnuHiTHu5vjhXUS7MN3YJdaO8fe7LtqDQzdrir4N8Djsxeh-yXrfn9YqBq65tr3WPlZnsKDuZeZV6cT_hTyDVAAWmMYeHyhLyCuY7aM0ACbP3cWnyxnmxQ1n2S6u7vBeYRFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعوت حدادیان از سربازان آمریکایی: پایتان را به کشور ما بگذارید ببینید چه بلایی سرتان می‌آید
🔹
آنهایی که می‌گفتند «نه غزه نه لبنان» خوب بیایند جنوب ایران!  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451062" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451061">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976711c4e8.mp4?token=CLD4nXtQ0LbcezWFCKYE8XmHBHKa5np5L-AjfE-h6q3nEzJfqHHpGb2SiG6WCFrvS4VeUtidnsmaQt7SDI7-gnNbOZB-aK5993PGof5felOKlEvxZzgqbOPD-OkVwrwwnKofZnaR7bvLwD8PoaCK9Y2SZwuGmA3433V11S1zOm2maRAIsqnEf6skVQLxKW_HIkzi_b1abPkYbBcrrKk6r6y-tuotmckX-v5Fwde-zayjtWIP3f8UZGgAJf13-iVb9iBgAP1tjwTLGSmlfT-baYHqRMyuYx0A-RhAYTjzrpOF5OOuZhyhhUfSDHh2leiWvw7Me3LFS6VAj7_JyKMmyJi7WeXfmnkP9kFFpFE2MOTKA7XAJs8UIox-lxMj-Fto1dSaepWsJkePOTtdzl5FHuNJ9WksXkaygwV77yfG1dfni8oqJCtTUNSdJYqbd0EcrPy1TtngpLhOPz3wo0iVCbAJfQFFKdia5rbr2T4S9wSmoxmwYq-_O5MZG6qWgrAp5PIoB9tdhhXidbjYtAUWLFbkB1sf2dYSViDMuiv_HsuvQlb2WqZpdfxLWVo2g4M5BOe9UoOS2dcFh-bCNj6hnGQXs-HZSC5-v1l7qMK4_pUm8Oqux_aaH69rJzTnXe51HqS5StUhegyLE2SeYW22rVye2QyZLoWgaZJ5DIs-IMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976711c4e8.mp4?token=CLD4nXtQ0LbcezWFCKYE8XmHBHKa5np5L-AjfE-h6q3nEzJfqHHpGb2SiG6WCFrvS4VeUtidnsmaQt7SDI7-gnNbOZB-aK5993PGof5felOKlEvxZzgqbOPD-OkVwrwwnKofZnaR7bvLwD8PoaCK9Y2SZwuGmA3433V11S1zOm2maRAIsqnEf6skVQLxKW_HIkzi_b1abPkYbBcrrKk6r6y-tuotmckX-v5Fwde-zayjtWIP3f8UZGgAJf13-iVb9iBgAP1tjwTLGSmlfT-baYHqRMyuYx0A-RhAYTjzrpOF5OOuZhyhhUfSDHh2leiWvw7Me3LFS6VAj7_JyKMmyJi7WeXfmnkP9kFFpFE2MOTKA7XAJs8UIox-lxMj-Fto1dSaepWsJkePOTtdzl5FHuNJ9WksXkaygwV77yfG1dfni8oqJCtTUNSdJYqbd0EcrPy1TtngpLhOPz3wo0iVCbAJfQFFKdia5rbr2T4S9wSmoxmwYq-_O5MZG6qWgrAp5PIoB9tdhhXidbjYtAUWLFbkB1sf2dYSViDMuiv_HsuvQlb2WqZpdfxLWVo2g4M5BOe9UoOS2dcFh-bCNj6hnGQXs-HZSC5-v1l7qMK4_pUm8Oqux_aaH69rJzTnXe51HqS5StUhegyLE2SeYW22rVye2QyZLoWgaZJ5DIs-IMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شرایط اعزام به جنوب را فراهم کنید!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451061" target="_blank">📅 11:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451060">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7Zg6eh9Fymx3012fGxPAl8KwQNfAgsHQufje5AVSHgYW6Fe9aYkxFAPL2e-sHjvgA2e0GlQJYVgWJXSjlQ8LKkQykoGEYEf9QXQTb87SYCzLlh8Zsw8O38PmKOQgrJ5-wwC_63ZEx8N-kjfXJ7IGo_eL_1epWtv0aHmuD70w6imT8ONm0O1ODjwkD0cmHUJdoWrTXn2nwZD2hQGeJKkbtrPfNgWCx4iJ-7ewRUq6nhywISl-cU-zVqpizjOuzZZr16Wjv5U2opRZHmqMxZf9OdYgQwWRpDAwaYFX9dbei1tX5-tTyRW03gmolAYx14m4zZnXV57s3clncdjjIkCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ انهدام چندین هواپیمای نظامی آمریکایی در حملات ایران به اردن
🔹
روزنامۀ وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد که در حملات موشکی و پهپادی ایران در روزهای گذشته به پایگاه موفق السلطی اردن که با تلفات گستردۀ نظامیان آمریکایی همراه بود، چندین…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451060" target="_blank">📅 11:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451059">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92f76bf7c.mp4?token=OkopyrOA37r9IH8QPh7jUSkcUFNdcfDEE3dBftd4DMyto4Dgd14sFA2fW9nlG9wDuHqbrCF5GeQh-MrwWH7OeHsLeW8GCA3TEvzZL_ZrPScFXzOLILWTr8myJgJKHJFJoMFw0gylSAtpcZOMCEE1rP2EB7rj1pPpLAOKFzlb9LxQqPgBAu5f8zMQGlIBcWXV3Qa-A_DM7FJGKdk0gELW7YvPALkWED-GJKwaxxm2brp-7-BKZhRpIfXWFikvxQc0HwW4IOQyxuU1OKa1Vb02RaYUGJGF1cQUa3iyqLvPTfAVW-Qmb2QqRuAMuaHrH_LrrUYxCIfHHlMjBaoO_XpQZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92f76bf7c.mp4?token=OkopyrOA37r9IH8QPh7jUSkcUFNdcfDEE3dBftd4DMyto4Dgd14sFA2fW9nlG9wDuHqbrCF5GeQh-MrwWH7OeHsLeW8GCA3TEvzZL_ZrPScFXzOLILWTr8myJgJKHJFJoMFw0gylSAtpcZOMCEE1rP2EB7rj1pPpLAOKFzlb9LxQqPgBAu5f8zMQGlIBcWXV3Qa-A_DM7FJGKdk0gELW7YvPALkWED-GJKwaxxm2brp-7-BKZhRpIfXWFikvxQc0HwW4IOQyxuU1OKa1Vb02RaYUGJGF1cQUa3iyqLvPTfAVW-Qmb2QqRuAMuaHrH_LrrUYxCIfHHlMjBaoO_XpQZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا دبیر: ما به جنوب کشور آمده‎ایم که بگوییم نوکرتان هستیم
🔹
من جزو کشتی‌گیرهای ایرانی هستم که به آمریکایی‌ها نباختم. آمریکایی بردن خیلی راحت است، شومن‌های خوبی هستند، ده‌شان را صد نشان می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451059" target="_blank">📅 11:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451058">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ_SztFPMsWjXHcIzcSIyrtU_NuaSWN6lSOWqhbwRPg7DaY8Bs-LggNGhx3JCmA2nQcVyF7mwcN3Ag9noeiouqRw79bSAmGD6HMCQe0ac5mXkEeIu159rCD6WzUycme0td5YdaWsfor2LREtPm_Z7hLUjMADoRcd33e0E4i2ePCHpHvTsyjDaNVjHtjJNQAHqPvy4hYhu0dhhz6wmH1bbTSOsSFHt0ElU3vDixEwiCoTZALPlYT2FHQv3H8FRq8Yp-r-uApYdNxlR6ZrJ5NDwUOtEYBHAAuYugQSnRSJAmOIN0iduQ8TRpiB8rpE2sBQn3x2luTItxQ9E3yTvvGjSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به‌دنبال ممنوعیت پرواز پهپادهای شخصی از ترس ترور مقامات
🔹
کابینه سیاسی-امنیتی اسرائیل در حال بررسی طرحی است که بر اساس آن پرواز تمامی پهپادهای شخصی به مدت شش ماه در سراسر اراضی اشغالی ممنوع می‌شود؛ اقدامی که به گزارش رسانه صهیونیستی اسرائیل هیوم، پس از هشدار مقام‌های امنیتی و با استناد به خطر حمله به شخصیت‌های ارشد اسرائیلی مطرح شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451058" target="_blank">📅 10:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451057">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38efd958d1.mp4?token=A3cgmdKUrYAkp3LcQfQ34Adbt59FT4D5pjxqEn1LPyBjWQYNE-i7s2yu6FsNWI1_uXOmp-VdAeW8h0WNzPYkTfzrVUehn6PZXLSGa94QJeQlT7WgJnPyeuwYT48LGv4EKGUdGlApqW7WaVN_n5NfXgXS3W8gwSWph6j0e6uK8Yg3KmIiQVMtQibWM-kF8bXzZlK16zns6C9y5SfPaXfpWjGsSkQ2MhwDyKEo8X6Ep2tvJN0UX_nIxc4CV_TiQ3in0-CX4v8pHo8oTiSLh3ySQVQqFwmA3KDd1FNRASms1Q2UhcZbQePRE4jfSKXPuQM5ZIt144lgIpCz8zseGwopbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38efd958d1.mp4?token=A3cgmdKUrYAkp3LcQfQ34Adbt59FT4D5pjxqEn1LPyBjWQYNE-i7s2yu6FsNWI1_uXOmp-VdAeW8h0WNzPYkTfzrVUehn6PZXLSGa94QJeQlT7WgJnPyeuwYT48LGv4EKGUdGlApqW7WaVN_n5NfXgXS3W8gwSWph6j0e6uK8Yg3KmIiQVMtQibWM-kF8bXzZlK16zns6C9y5SfPaXfpWjGsSkQ2MhwDyKEo8X6Ep2tvJN0UX_nIxc4CV_TiQ3in0-CX4v8pHo8oTiSLh3ySQVQqFwmA3KDd1FNRASms1Q2UhcZbQePRE4jfSKXPuQM5ZIt144lgIpCz8zseGwopbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا دبیر: ما به جنوب کشور آمده‎ایم که بگوییم نوکرتان هستیم
🔹
من جزو کشتی‌گیرهای ایرانی هستم که به آمریکایی‌ها نباختم. آمریکایی بردن خیلی راحت است، شومن‌های خوبی هستند، ده‌شان را صد نشان می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451057" target="_blank">📅 10:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451056">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تردد در جادهٔ هراز فردا و پس‌فردا ممنوع است
🔹
پلیس‌راه مازندران: جادهٔ هراز در روزهای ۲۹ و ۳۰ تیر از ساعت ۸ تا ۱۷ برای اجرای عملیات لق‌گیری و ریزش‌برداری سنگ‌های ناپایدار به‌طور کامل مسدود است؛ رانندگان در این مدت از مسیرهای کندوان و سوادکوه تردد کنند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451056" target="_blank">📅 10:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451055">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e97d26e7e.mp4?token=QhSW7y4j4vw-YoIGmoovWRrePSExnAVxidOKvzJz9I2GjLlzBnrdslEsZkYhtNXM1IJy-P3PwkGGTtGHe-PAquJFFp6v1UwoLmiSYE6lOPViSX5zlEwZ4biMzI55pW27FtsZVg32gsZ5egrKh30fLOHGA_fJ071px5ij7lvvFvPe1PMsqHWN63BrLrx5zQoW390HVDFehnXs-j_iSyOXu_-bAOQpbb0egqxQTshg2JNN9CEMSiPtJUd7oMLCAt5712zxWmLuhUo4KrjXsWY66DccsU9-ZsWHQ0NE8oapNzRUss44sYtFJjlKzBATuQlG3X0ATajXjY0jbmH-l1Orxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e97d26e7e.mp4?token=QhSW7y4j4vw-YoIGmoovWRrePSExnAVxidOKvzJz9I2GjLlzBnrdslEsZkYhtNXM1IJy-P3PwkGGTtGHe-PAquJFFp6v1UwoLmiSYE6lOPViSX5zlEwZ4biMzI55pW27FtsZVg32gsZ5egrKh30fLOHGA_fJ071px5ij7lvvFvPe1PMsqHWN63BrLrx5zQoW390HVDFehnXs-j_iSyOXu_-bAOQpbb0egqxQTshg2JNN9CEMSiPtJUd7oMLCAt5712zxWmLuhUo4KrjXsWY66DccsU9-ZsWHQ0NE8oapNzRUss44sYtFJjlKzBATuQlG3X0ATajXjY0jbmH-l1Orxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی جبهۀ پایداری: مشکل ما اصل مذاکره نیست، طرف مذاکره است
🔹
متقی‌فر: این جبهه اصل مذاکره را ابزاری قابل استفاده می‌داند، اما مذاکره با رئیس‌جمهور فعلی آمریکا امری بیهوده است.
🔹
مذاکره با ترامپ نباید صورت بگیرد، زیرا او فردی قابل اعتماد نیست؛ انتظار مردم این است که مسئولان این موضوع را همواره مدنظر قرار دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451055" target="_blank">📅 10:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انهدام یک پهپاد MQ9 در اهواز
🔹
دقایقی قبل، یک پهپاد MQ9 با آتش سامانهٔ نوین پدافند پیشرفتهٔ نیروی هوافضای سپاه و تحت کنترل شبکهٔ یکپارچهٔ پدافند هوایی کشور، در آسمان اهواز ساقط شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451053" target="_blank">📅 10:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سپاه چهارمحال‌وبختیاری: به‌دلیل اجرای پروژ‌های عمرانی، احتمال شنیدن صدای انفجار در امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451052" target="_blank">📅 10:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451051">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvGLv_0U1JcNpgQRYIYcHJ9Trln_xANV0u_u-IlMoIWpjn7oa4EYIxXZTea54WuxgPZoHo14xO6H9YSX1FGt6J40g20l1S75HcOstpVsNDv-I0mW5eCWB9jNekbmYxdR2gw7t5ojmJcA8ZLxnKw1b9t1kbSGBPdinhi-KZjTBPhKLTuvHShWSkYaaFMUYwEQ08YAC0gzLw2wtOd1h3ERO6-hYoiS-jbLLlLCnEPrefqHj7wo3HH6d6imU1dYQ0tEWxJtuufca6EkOAvN9lEVrcdm-UDIcs0lG4vnr0x16C1ths6KnSFjtyb3aLKcQn5KZQZt_2uk_QQ5bPNv2Um51g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درس‌های فراموش‌نشدنی</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451051" target="_blank">📅 10:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451050">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌
🔴
ارتش کویت حملات موشکی و پهپادی به این کشور را تأیید کرد و مدعی شد که «پدافند هوایی با حملات مقابله می‌کند».  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451050" target="_blank">📅 10:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451049">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
منابع خبری گزارش کردند که هشدارهای حملهٔ هوایی در کویت فعال شده است.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451049" target="_blank">📅 10:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451048">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
منابع خبری گزارش کردند که هشدارهای حملهٔ هوایی در کویت فعال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451048" target="_blank">📅 10:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451047">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfa2v_hODkcrKbfJWQdlH434BH7mYwTLpdMZQQaK-i4wyj_A2hsvIhKNfFeltPHWg3y6jJFblSHfuJs6CH7SA1ki_-L97d_WrazppfE30314FxDKEyYEEVsiApLeBx-DD2CKn3Nu_PZvVTmYXnT929amwcZG8PCfInTSdP1qeP6j8YlvprunL0tqNyx6KdtSO5uc9uR-zjgHr1TPFI2AM2BYyESckRr_Lyr2-wLBiMIHeDttbV7HboqKwwVEOvmWrnW0Hp3cEt3Z9S9KwIOqsnRbIK0KciKE_amLKhh0jcuicF9Gls6R1ppXrUTai1OhPYw3sF628slYDXNEHHkz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۳.۹ ریشتر در عمق ۱۹ کیلومتری زمین، انبار الوم گلستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451047" target="_blank">📅 09:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451046">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4d127f77.mp4?token=ZhhLdCthk21afIxnf4jBjI4IWZMd92uVZv6XDVzYrIUxVQgRdDhwsZL-AGF__Ynt9Kn9oZ6oLDchxdKXFkA1Cu0Ri7ztAZ8HCKIG-1ci8dFGcYVaSD_dQIRiPwm24iHbqv7k1_jN_SYgR5LIQAW8Rhv1rXIVsbCwk_UQ7hTSfi0ERl5iLhOFdmMwPiianv_J6m-UUeCo2hGSqxZ4NdGfIFHriIlhTKk-C6s6nMXuWhoI19YLymIshh7NXOnhUiyKo3zr5YM9cRc2ttsW50CWJ1oHQXLqddc_DEgZ17ObpzR7q0ZRIv21VHIoZ_QFoOPGunQuwCF8ne-JkJolWTzDOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4d127f77.mp4?token=ZhhLdCthk21afIxnf4jBjI4IWZMd92uVZv6XDVzYrIUxVQgRdDhwsZL-AGF__Ynt9Kn9oZ6oLDchxdKXFkA1Cu0Ri7ztAZ8HCKIG-1ci8dFGcYVaSD_dQIRiPwm24iHbqv7k1_jN_SYgR5LIQAW8Rhv1rXIVsbCwk_UQ7hTSfi0ERl5iLhOFdmMwPiianv_J6m-UUeCo2hGSqxZ4NdGfIFHriIlhTKk-C6s6nMXuWhoI19YLymIshh7NXOnhUiyKo3zr5YM9cRc2ttsW50CWJ1oHQXLqddc_DEgZ17ObpzR7q0ZRIv21VHIoZ_QFoOPGunQuwCF8ne-JkJolWTzDOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات موشکی شدید روسیه به کی‌یف
🔹
مقامات اوکراینی اعلام کردند که روسیه بامداد امروز «یکی از بزرگترین حملات موشکی بالستیک خود را» به پایتخت اوکراین انجام داده است.
🔹
طبق این اعلام، پایتخت اوکراین با حدود ۴۰ موشک بالستیک «اسکندر» و هایپرسونیک «زیرکان» هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451046" target="_blank">📅 09:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451045">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY_XSj7qJWaHiDwo4PYoZ3CzgRkVfSRtPPdTBNdp_xe4lHsvDKPf_gljo-43RpZMqK2mQFBqbmNYsOEjxHqQA-XplY_RuzZXLX-FvobSIlgcAvdV801KyZVkQrwJ5xiAh-lxD14blNFWh5JmFlkvocJ7xgR0R2CSEeJv3IBERVTJ9JKRmqzGIyVm-v4gtZE8ftB7yR9NWcJVT_0o5qRdWpGU6NVs7nm7rX0QQ87hsmlyePfXJd3kQJvBf_MNy_COJ1C59giXXxgY2wQqs2dTDbvPgnvHNwpm3qstxlXQdj-H5Z5NDdyVDuxsEYhlaou9Fc631-i_LSdHE-Lw-oS6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی بوی سوخت جت می‌دهد
🔹
جام جهانی ۲۰۲۶ قرار بود جشن جهانی فوتبال باشد؛ اما حالا آمارها نشان می‌دهد پشت ویترین پرزرق‌وبرق این تورنمنت، ردپای سفرهای بی‌وقفه، هزینه‌های سنگین و تناقض‌های بزرگ هم دیده می‌شود؛ تناقضی که شاید بیش از همه، رئیس فیفا نماد آن باشد.
🔹
جیانی اینفانتینو، رئیس فیفا، تنها در طول برگزاری جام جهانی بیش از ۱۱۵ ساعت پرواز داشته و نزدیک به ۶۰ هزار مایل (بیش از ۹۵ هزار کیلومتر) را با جت اختصاصی طی کرده است؛ مسافتی که تقریباً معادل دو و نیم دور گردش به دور کره زمین است.
🔹
این آمار فقط یک عدد نیست؛ نمادی است از جام جهانی‌ای که بیش از هر دوره دیگری به سفرهای هوایی وابسته شده است. از تیم‌ها و هواداران گرفته تا مسئولان فیفا، همه مجبور شدند هزاران کیلومتر میان آمریکا، کانادا و مکزیک جابه‌جا شوند.
🔹
نکته قابل‌تأمل اینجاست که فیفا در اسناد رسمی خود وعده داده انتشار گازهای گلخانه‌ای ناشی از جام جهانی و فعالیت‌های مرتبط را تا سال ۲۰۳۰ به نصف کاهش دهد و تا سال ۲۰۴۰ به انتشار خالص صفر برسد؛ وعده‌ای که با توجه به حجم گسترده سفرهای هوایی در جام جهانی ۲۰۲۶، از سوی منتقدان با تردید مواجه شده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451045" target="_blank">📅 09:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451044">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سپاه اصفهان: تا ساعت ۱۳ امروز احتمال شنیدن صدای انفجارهای کنترل‌شده در جنوب کاشان وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451044" target="_blank">📅 09:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5895571f9.mp4?token=A_ZJyqj-ePAs_3zenUqk5crz_LuqAzLcTDNPYxi8BfOkMh753cDAF7xVDZ5OU5nG0XPdfLMIoRFopvF10IasJEc5ReMxGdsEecVdBJDXWHnqpnswRsnxtfNG4dwhIMJ4PXkuOxUxVQ4A6UYVXUyPgCs7mOTSMHQnnit2DNXl1j6OJ-uEoHw8-1oftU6ARAlc5bgKJhvZZ7oFbxRkUiCxjOi4EyRvzvEAb0SbRvORn8EIZn9Rm73ICkkIa9zTJUV1by-WNDDvVqJoJXNRGqEobewazB4nf_vr85TNdQ7tS5_Ta0fHiH1CHgjrjkQZ03VTKZ7TZxHkU7NiJdHjoW6NAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5895571f9.mp4?token=A_ZJyqj-ePAs_3zenUqk5crz_LuqAzLcTDNPYxi8BfOkMh753cDAF7xVDZ5OU5nG0XPdfLMIoRFopvF10IasJEc5ReMxGdsEecVdBJDXWHnqpnswRsnxtfNG4dwhIMJ4PXkuOxUxVQ4A6UYVXUyPgCs7mOTSMHQnnit2DNXl1j6OJ-uEoHw8-1oftU6ARAlc5bgKJhvZZ7oFbxRkUiCxjOi4EyRvzvEAb0SbRvORn8EIZn9Rm73ICkkIa9zTJUV1by-WNDDvVqJoJXNRGqEobewazB4nf_vr85TNdQ7tS5_Ta0fHiH1CHgjrjkQZ03VTKZ7TZxHkU7NiJdHjoW6NAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنان منتشرنشده از آخرین دیدار سرلشکر موسوی با فرماندهان ارتش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451043" target="_blank">📅 09:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451038">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCrmc83wIkBl7FqzX7usp2EB4_wtyvhPk8OqK4wfc6gmUjulT0_A34TAhE7Or6Yt1BE_r2_gmh-yNRPbUq6_mcudhrkdPomNFsANfpTk3DJIaRrPl9j8i6lp-yMz8kGmgt3Hsx1p79rE8lM5jFv6v2wvaamIWb5wxnVPilV-UOTIt9KLgiptsI2UsTxUsKVORDDp1ilgVCII_SK2x10TbhJJQBlb3R7AetGpSCpf0qqnEh45vPZjA-CxGAISF5-s8jvxOM5tSIJGUs6q1CW-uz5qhbN8gYwJCqdNC_pBYCZI1DSs_i2ctiyVLaZRJERWMWg9auk3376CEaNeISCVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTN1S6OGPGgjQgRknePRc-1RbCWSdc6-IZX3EWCNVFJvva0bIP-ja4NJTOQpxz7BOE7ZWFs8txUMQOgNtlX-V9oT3JvTbxm19j1qSB9dCBPawWfT9qg2F7G199rSN0Sj0Ha2WPbeWcHKOezPk7eEZII5_rA7JXou3_TUNlirEZRZDYMFZ1V9xlcF-yiVqjYdMstYPRO19-Gnk6mNd42yfXDkqinbSE1JfNlI2fgn_FO80CY55DmR1sZnLJDrPcltjF07HMgalPPvyTDGuqk54Ye42wWElXNG2X8Oy9xifAkveFiKkfjvlUr2XuizSqFWdAkMu6G44N5Qktk5B8Canw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xpz7EK1I301BRIEXjcAfp7-TknSJgEyBVP2TR9erVrDy6hAcqJ6hYKAiAyV3ZCi9LbjeVR6f0srrhNa5um2AN0sVCH6EdoJlsErAo0E-e4r5yxTUHWtgCuD_kEX7SMbDlAXa3zOMsPjxyZP_HrLa75WatFtGvfA4mszCSbv-AUzjgAy-geRPPK4KaHMhYagVyAD_iV6o1QRdFb38gW7fg31EGQXoiMlE_UXjDcmNLxZ2alz1tk6IHCt9nHDZMGZis7W2rgs4W_fVEUWGPTJNRnqxaWTCiOJoZwa-uQUpddy5wSM9zyfvaduhOZLArMnVjUx-VTzJdzMFzcrY0a5jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phvnruPvLd4TIeJFNUQY7zaJYAe1U1dcUTE9W8rZ5wk5fwfQHlYy_JbiEDpmcrlKASzfFTiMFsiLBCI0vQCna8cfQ1Rx0tVOphfvxDYdQJhZg5OPLbREQivDnQBmReSSBSYrcmirRxl4QSNhxGf9vwO-OlnwtESGus-A6YwQJiq_QTSMxpBKlmEtvO3GuJjlS9lRsk6MMRraRRnRteIiRiNkoFVUOOcZNmWuJB1bMkAjjUvrZc0iRPcZrzjKb60G3_l4ZV2UKx5aEuT8LxYc5deBUcf3yA2E5pnm1Q8E4s9EvKcIdPWJmdFsuWvvHZ7hRsaxYOKm6x5e6kuUtFlN8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWE48xAPGazxMIdPMPhhbTjR8iBnPrLttnk74gyoWR0J4jejdR20u4F-fNKBCO8WEKC5hDWwdenMIn3_5E6SGyXTDHY6YAUEPDdpDS2zCVYS-4v3TTme3NZ9J87rTuzM3DuBC8jEqruqmitsxhZTRY5RSJin--Rn9pqPbsE7PH4iX3zcYkK0aPQBmm4i7Ta4tNQIajlHA-swP_fWI2CkGoQKW9DmhetTKsyxQns5lIgxSm30Nam0uJREth0OIJankhIDzOUL8VQEcMcRNNqCu6kOuGrm0zE3JWVbCD71tH47xCXshzjCqXmquDV7nrxFaNp37hQaRwwU1HIsrhTWYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
فصل برداشت رُطب در خرمشهر
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/451038" target="_blank">📅 09:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451037">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0cdc8e19c.mp4?token=MsPdwh0-Zq_34DBD3Wgh8qQfUArwBYI3UxBPk_BJh5PSheHJfqa2Xqe-VIEa3sBM7C7MHcHWOaLIvFN5H6NiVjeH0qoHzIKDL7nabwGdvreKD27yKcLTUL2pvPIlO4TFN1GpFqnzh1WEzo68Czeh_kH_TWRqzggHpncKoL3kARIHtVlUKolztGwUeovPFhHaQhaC4iWJQRokHN9-1jZAvJeDruvpBcwPPDqwGbZP01n69nubUaoIs0DZTJnPFT_uiHtGvyNWpin4iUntiIHGFzckMnTFsVTaH886ysZX9J5crYe30I10uGdFlqI28y56uZ25c6V1L2jxLcx2bJL6pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0cdc8e19c.mp4?token=MsPdwh0-Zq_34DBD3Wgh8qQfUArwBYI3UxBPk_BJh5PSheHJfqa2Xqe-VIEa3sBM7C7MHcHWOaLIvFN5H6NiVjeH0qoHzIKDL7nabwGdvreKD27yKcLTUL2pvPIlO4TFN1GpFqnzh1WEzo68Czeh_kH_TWRqzggHpncKoL3kARIHtVlUKolztGwUeovPFhHaQhaC4iWJQRokHN9-1jZAvJeDruvpBcwPPDqwGbZP01n69nubUaoIs0DZTJnPFT_uiHtGvyNWpin4iUntiIHGFzckMnTFsVTaH886ysZX9J5crYe30I10uGdFlqI28y56uZ25c6V1L2jxLcx2bJL6pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادامهٔ حملات پهپادهای ارتش به پایگاه‌های آمریکا در کویت
🔹
ارتش جمهوری اسلامی ایران: در پی نقض معاهدات بین‌المللی و جنایت‌های دشمن مستکبر در مناطق غیرنظامی، ارتش جمهوری اسلامی ایران در مرحلهٔ هفدهم عملیات صاعقه، از بامداد امروز انبار مهمات ارتش تروریستی آمریکا در اردوگاه العدیری و سوله‌های تجهیزات و نفرات این ارتش کودک‌کش در پایگاه ‌علی‌السالم کویت را مجدداً هدف حملات پهپادی قرار داد.
🔹
ارتش تأکید می‌کند که جنگ ما، دفاع از هویت اصیل و تاریخ چندهزارسالهٔ ایران و مردمانی است که در پرتو تعالیم اسلامی نه ظلم می‌کنند و نه ظلم می‌پذیرند؛ بر این اساس، رزمندگان ارتش با اعتقاد عمیق به این آموزهٔ الهی برای دفاع از مردم شریف در مصاف با دشمنان ایران و بشریت محکم و استوار ایستاده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451037" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451036">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">زلزلۀ ۵ ریشتری در سالند استان خوزستان
🔹
ساعت ۵:۵۵ دقیقۀ صبح یکشنبه، زمین‌لرزه‌ای به بزرگی ۵ ریشتر حوالی سالند در استان خوزستان را لرزاند.
🔹
این زلزله در شهرهای مختلف خوزستان از جمله اندیمشک، شوش و اهواز احساس شد.  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451036" target="_blank">📅 08:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451035">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQtbiyxbxFsFGdqJ6hWzWnfzpSB03e0LcVe6XUXhpMgPHJ0-IuiMe47QkweWWuQ1K10oSF6b48ca9niP0R2D7pDYCWYchjMeSJ8rZsjASgsYyV7FQ8nR29moAZA34Qo7KgYhPXtcXYcZZq-DwOEFhRkx1GTg9m2rGjeZkaHWg6bGQ0VeI-mzb-jYmPmnHhLDZ8zd4XacAf8vaQeW3KoVxhlJfC2wElqW1G5G01ObyFg8ZySmbwVEIMvB-B8NS01e6SCOri3FBsSdB2yGhFI_CsYkrqg-xxZf-tNkXU0Xc3_bZXmrRMn-FHfTeXo3nKekQ1XRFNeGHWtlA_w4imwt1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایپا دوباره محصولات خود را گران می‌کند
🔹
مدیرعامل سایپا با اعلام قریب‌الوقوع‌بودن افزایش قیمت محصولات این شرکت، از مردم خواست منتظر اعلام نرخ‌های جدید باشند.
🔹
در این نامه آمده است که توقف نماد با هدف جلوگیری از ایجاد ابهام در معاملات و حفظ حقوق سهام‌داران…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451035" target="_blank">📅 08:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451034">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حاجی‌دلیگانی: با مدیران دخیل در ماجرای دانشگاه علامه باید برخورد شود
🔹
نایب رئیس کمیسیون اصل ٩٠: برخورد با فردی که صرفاً در چارچوب وظیفه شرعی و قانونی خود اقدام به امر به معروف کرده، اقدامی غیرقابل قبول است.
🔹
وزیر علوم باید توضیح دهد که چگونه به جای تقدیر…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/451034" target="_blank">📅 08:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451033">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mqu6hBAw2VibuG7fvActj6ECsr13GpUybqJzHVAH-Zn9t8TNFtyw2_VtJafuT06Kvaz7xkJO8AIO2gU3lEaEhjZIiQHde6HkS024vBbf-WIF4V39Og8XQK4hddrCYo-s-Qmio9JwmugkqiJZJK6hSU_a170-URXLL6u8iwUTw3ek5kmhy78C1opiXsAX6fDRYIMalqyweTq6rqArg9ExmbNF8psXMUtvN4jGZ31jyYguDkxMaJRKRKypZOQWhzLgwUk9COf3TCPkHK_SZqGTC5mELYb6wqDTSTKjtg92AfNssJxc7zeAK-AokHqBkBqurb_Uw_gx8hRzVICAgL4eeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
با پیشنهاد شهرداری و تصویب شورای‌شهر تهران، مترو و بی‌آرتی ۲ ماه دیگر هم رایگان ماند.
🔹
در صورت ادامهٔ شرایط جنگی در کشور، ادامهٔ این طرح ۲ ماه دیگر در شورای‌شهر بررسی خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451033" target="_blank">📅 08:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451032">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هرمزگان از برنامۀ خاموشی‌های برق خارج می‌شود
🔹
به‌دلیل شرایط خاص استان هرمزگان در وضعیت فعلی، وزیر نیرو دستورات لازم برای خروج این استان از برنامۀ خاموشی‌های برق را صادر کرد.
🔹
بررسی وضعیت سایر استان‌های جنوبی دارای شرایط مشابه نیز در دستور کار قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451032" target="_blank">📅 08:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451031">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9-6SywSLZtbkGrXH1Qs_2cOZ56e9BeMofV8JMxkThaeuyFXD6-JROo8FhDB-KY6zHt224C0329-fjsopqsN9Z7dh-M3m7g2YpvO58X8_9nYpUxAuqT6YoS_r6JBoTocccFTNmyabVrqyUOZ0UGbsPxX2uFjBrQRJ4gO8h1doBaMUroePUWvn2Y96HZfQj9AvesUceYfcafPy8iNqy040_F1p_M2RFebnxUM-VaPk1VYY1wDSzamMwUDBapv_IHpMcn7I-Q9d-7ry9Xn1f_KkGnASAErVXKvZw7zknZr0pQcrkF01b3NevLwUygHyJSH_eJ-_znzL5Q3_Ayy2pT7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزبانی فردوسی‌پور از کسی که آرزوی عصر حجر برای ایران دارد
🔹
«قرار ما با شما، نه دادگاه، نه بخشش، رقص و پایکوبی روی گور تک‌تک‌تان» این متنی است که علیرضا فغانی در دی‌ماه ۱۴۰۴ منتشر کرد؛ اما این تنها استوری‌ او در دی‌ماه و حوادث بعد آن نبود.
🔹
فغانی که پس از قضاوت در فینال جام‌جهانی باشگاه‌ها عکس ژستش با ترامپ را منتشر کرده بود، زمانی که ترامپ ایران را تهدید به برگرداندن به عصر حجر کرد، باز هم در استوری‌هایی هم صدا با رئیس‌جمهور‌ کودک‌کش آمریکا شد.
🔹
اما فغانی جمعه‌شب،‌ میهمان برنامۀ عادل فردوسی‌پور بود. برنامه‌‎‌ای که در ایران تولید و پخش می‌شود، میزبان کسی بود که طرفدار بازگشت یک مملکت و مردمانش به عصر حجر است.
🔹
البته پیش‌تر خود فردوسی‌پور گفته بود: «ما که با فغانی کیف می‌کنیم، هر کی خواست نکنه!» اما اگر این را بپذیریم که همه در یک جغرافیا زندگی می‌کنیم،‌ کسی که آرزوی نابودی‌اش را دارد،‌ منطقاً نباید این‌چنین مورد استقبال قرار بگیرد.
🔹
حالا اما ظاهراً قبح همه‌چیز آن‌قدر ریخته که فردا اگر علی کریمی را هم دیدیم نباید تعجب کنیم.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/451031" target="_blank">📅 07:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451030">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8cda4d17d.mp4?token=uz4TmpikV9mSXG3yqQk4eoKrW-WxpKt28P6DxEsNqw23Wj0sRv35CXXKtDEq6QYP_n4OxeAAsUPrP7Oz-fRXdyYmTQdIZtXc1cpGiMMFcOUcCdZXBVOSIamUYobIxZev33aUKNYVgVA0RIUypmEwL9c7p6Zk4Z2B__GjRLqT5izXv5myqtkFg4UK8tzFtdzeg97MMjf5GVJaLUh4zlRVS7NTklUvQqFnI7LCdwsPQgqNYlTy_Kt1xX64uMHKuoMb_gJvZIG7MYflnjgHusEzkkfSkORduL1RRP4fU-clNWoH8Myjc7zaGgCnVybeOBdz4hxSJY0Kq3F16Q3kMY1npaZ14C51ytg5C4S6jNWarP0RCc20L9x8n9yoGmD2qQYWZJXVQyIugpRkaqeyxWi5MQyfKOd0s9zZNgn9t7PCRiB5fhktdbVw_QYKBcXAPaaBOhaov_dB_hA7jYZKtvEKMYD3VojuvS14SPCAQvCh3s0l0ssxUUBtrqTYN2kNHYHp470trUsNTzG1YqN1QfK8BkpWE3HdDs0KE5YK3o5PkMYYua_PQp7Up7ABCWTJm0S2B9igKpZOkPNGZEMn1SIR6myGSDE7wnDlhs5GJ6eplLlaJBpw0aGLF_Vmc6l3pNZsZ3k-kSQ4WjCSm68omKpsnc5Z1b9HMVaxeKxkmwgbE00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8cda4d17d.mp4?token=uz4TmpikV9mSXG3yqQk4eoKrW-WxpKt28P6DxEsNqw23Wj0sRv35CXXKtDEq6QYP_n4OxeAAsUPrP7Oz-fRXdyYmTQdIZtXc1cpGiMMFcOUcCdZXBVOSIamUYobIxZev33aUKNYVgVA0RIUypmEwL9c7p6Zk4Z2B__GjRLqT5izXv5myqtkFg4UK8tzFtdzeg97MMjf5GVJaLUh4zlRVS7NTklUvQqFnI7LCdwsPQgqNYlTy_Kt1xX64uMHKuoMb_gJvZIG7MYflnjgHusEzkkfSkORduL1RRP4fU-clNWoH8Myjc7zaGgCnVybeOBdz4hxSJY0Kq3F16Q3kMY1npaZ14C51ytg5C4S6jNWarP0RCc20L9x8n9yoGmD2qQYWZJXVQyIugpRkaqeyxWi5MQyfKOd0s9zZNgn9t7PCRiB5fhktdbVw_QYKBcXAPaaBOhaov_dB_hA7jYZKtvEKMYD3VojuvS14SPCAQvCh3s0l0ssxUUBtrqTYN2kNHYHp470trUsNTzG1YqN1QfK8BkpWE3HdDs0KE5YK3o5PkMYYua_PQp7Up7ABCWTJm0S2B9igKpZOkPNGZEMn1SIR6myGSDE7wnDlhs5GJ6eplLlaJBpw0aGLF_Vmc6l3pNZsZ3k-kSQ4WjCSm68omKpsnc5Z1b9HMVaxeKxkmwgbE00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهید مریم حیدری‌پوری شهید حمله به تپه‌های الله‌اکبر بندرعباس</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/451030" target="_blank">📅 06:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451029">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
حملۀ دشمن آمریکایی به شادگان
🔹
معاون استانداری خوزستان: در پی هجوم دشمن تروریستی آمریکا به خاک کشورمان، یک نقطه در اطراف شهر شادگان مورد اصابت موشک قرار گرفت.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/451029" target="_blank">📅 06:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451028">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrC6wp56c9dGwEiLwfiEXxJsXIyGrHCXg2kUG2p37AoMpDByKP31OlcKvxKMMglhDQeN26dbtBH--1ep205fher0gcQnhWfKPLw61pUmnDmtz0_S0Z22ORtxDdK7VAEuFhfXUpZA8AyiYTmkgAKUx4V_Oplsg30joz_i8h8CCf7yxDjnD_hOb_b0RNmiMdQY9ZULRg5V4lXhZU3kd4Bfh18pHGUQkUwPt3UZHlFqf_eKtKnhic7xJ-wFP49VFsyKAU_1pfSz86QIfq2EEfVUB07lhN6D7O-6D3vevDyrcFR8US0BPqoG9fhwqvu1TEGRckk0xN5OQBNvqobb8Q89sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۵ ریشتری در سالند استان خوزستان
🔹
ساعت ۵:۵۵ دقیقۀ صبح یکشنبه، زمین‌لرزه‌ای به بزرگی ۵ ریشتر حوالی سالند در استان خوزستان را لرزاند.
🔹
این زلزله در شهرهای مختلف خوزستان از جمله اندیمشک، شوش و اهواز احساس شد.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/451028" target="_blank">📅 06:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451027">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db885829ed.mp4?token=V2JOKQQPLpa-zAAFptVI7LmgIAro28NU9eMPePQ_98HoLFPl2XRYAS2aBiOOYD0a3k9Jo2cUotdWPP_0EPa8zuD6DbeQ18kRa3uEt_T6ZkifEAZSy7WtkofiRavowD3I2b6lEgvfZRfLga-xvNqoKgo6vooBWcJ0GAIGRMoM8cqvPghX71GfQMNe2jBZ-tBF7EzpzSmRkdFATyHF6jgmIESpg78rgq2onvOp9CasKsmK167YKyzMsT2NrfryLpN4oR_S9ZX329pllcpLZwwl53hNGE0ceLjkbdvBt7SBh6ZUjFXAz6cYZkb1mlwdbCwHmF_GJ4DtNDsMzYYiY2Zntg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db885829ed.mp4?token=V2JOKQQPLpa-zAAFptVI7LmgIAro28NU9eMPePQ_98HoLFPl2XRYAS2aBiOOYD0a3k9Jo2cUotdWPP_0EPa8zuD6DbeQ18kRa3uEt_T6ZkifEAZSy7WtkofiRavowD3I2b6lEgvfZRfLga-xvNqoKgo6vooBWcJ0GAIGRMoM8cqvPghX71GfQMNe2jBZ-tBF7EzpzSmRkdFATyHF6jgmIESpg78rgq2onvOp9CasKsmK167YKyzMsT2NrfryLpN4oR_S9ZX329pllcpLZwwl53hNGE0ceLjkbdvBt7SBh6ZUjFXAz6cYZkb1mlwdbCwHmF_GJ4DtNDsMzYYiY2Zntg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ارتش: دو پایگاه مهم آمریکا در کویت، آماج حملات پهپاد‌های انهدامی قرار گرفت
🔹
در پاسخ به تجاوزات مکرر دشمن، شهادت هم‌وطنان عزیز و حمله به پل‌ها، زیرساخت‌ها و مناطق غیر نظامی، ساعاتی قبل و در مرحلۀ شانزدهم عملیات صاعقه، ارتش جمهوری اسلامی ایران، انبار مهمات ارتش تروریستی آمریکا در اردوگاه العدیری و رادار پاتریوت و رادار هوایی این ارتش متجاوز در پایگاه علی‌السالم کویت را، آماج حملات پرحجم پهپاد‌های انهدامی خود قرار داد.
🔹
اردوگاه العدیری یکی از پایگاه‌های مهم ارتش تروریستی آمریکا در منطقه و در فاصلۀ ۱۰۴ کیلومتری مرز‌های جمهوری اسلامی ایران و ازمراکز مهم پشتیبانی و تجدید سازمان نیرو‌های آمریکایی است که اخلال در عملکرد این پایگاه تاثیر قابل توجهی بر عملیات‌های پشتیبانی ارتش در منطقه می‌گذارد.
🔹
پایگاه هوایی علی‌السالم نیز از پایگاه‌های مهم، مرکز اصلی ترابری هوایی و دروازۀ ورود نیرو‌های نظامی به منطقه غرب آسیاست که نقش محوری در راهبرد نظامی و لجستیکی ارتش متجاوز آمریکا در منطقه ایفا می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/451027" target="_blank">📅 06:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451026">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هشدار قرارگاه خاتم‌الانبیا به دشمن: نیروهای مسلح به هرگونه وحشی‌گری پاسخی ویرانگر می‌دهند
🔹
سرلشکر عبداللهی: با تبعیت از فرامین و تدابیر رهبر معظم انقلاب، به شیطان بزرگ و دشمن جنایتکار، عهدشکن و حیله‌گر آمریکایی یادآور می‌شویم هرگونه طمع‌ورزی، زورگویی، تمامیت‌خواهی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/451026" target="_blank">📅 05:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451025">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هشدار قرارگاه خاتم‌الانبیا به دشمن: نیروهای مسلح به هرگونه وحشی‌گری پاسخی ویرانگر می‌دهند
🔹
سرلشکر عبداللهی: با تبعیت از فرامین و تدابیر رهبر معظم انقلاب، به شیطان بزرگ و دشمن جنایتکار، عهدشکن و حیله‌گر آمریکایی یادآور می‌شویم هرگونه طمع‌ورزی، زورگویی، تمامیت‌خواهی و وحشی‌گری با پاسخ قاطع و ویرانگر رزمندگان مومن، شجاع و مقتدر در نیروهای مسلح مواجه می‌گردد و هزینه‌هایی سنگین‌تر از جنگ تحمیلی دوم و سوم بر آنان تحمیل می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/451025" target="_blank">📅 05:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451024">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
افشاگری نیویورک‌تایمز از حملات پی‌در‌پی ایران به پایگاه آمریکا در اردن
🔹
نیویورک‌تایمز: مقامات آمریکایی جزئیاتی از حملات ۵ روز گذشته ایران به اردن ارائه کرده‌اند که پنتاگون هنوز به‌طور علنی دربارهٔ آن‌ها صحبت نکرده است:
🔸
حملهٔ اول: موشک‌ به یک مجتمع مسکونی…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/451024" target="_blank">📅 05:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451023">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b78212fc.mp4?token=opz_jCmNOJBYYJHaYMx3RyzXPsSBk-5KpnGsZyOVgNW645jGmYR1mHsnvpUq1fcNNlRMnldsuVTVc7rFi7P3bwTWx0kD7fnFcPPupeNG_Y0NP9dD2jrhuYre82KI5zER7cbXoSfj03iX2UW5ddIgRR0PUStMDkXyEvMfWaO19FhKo1D80aHKzQIojHCuSMGJ3MPNREhuHscFF2YP_presNpxopzrwDmXm9NnHfYveStkF31jHruAnoH8CvuuIPMIYcvE5L3ecxu52fKTKNAFwG60wHNc8BWM-Z0P432DqZVvLygqXjpk65Tqw5FOijH4URYkN_QMf_fI9saEkNzxCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b78212fc.mp4?token=opz_jCmNOJBYYJHaYMx3RyzXPsSBk-5KpnGsZyOVgNW645jGmYR1mHsnvpUq1fcNNlRMnldsuVTVc7rFi7P3bwTWx0kD7fnFcPPupeNG_Y0NP9dD2jrhuYre82KI5zER7cbXoSfj03iX2UW5ddIgRR0PUStMDkXyEvMfWaO19FhKo1D80aHKzQIojHCuSMGJ3MPNREhuHscFF2YP_presNpxopzrwDmXm9NnHfYveStkF31jHruAnoH8CvuuIPMIYcvE5L3ecxu52fKTKNAFwG60wHNc8BWM-Z0P432DqZVvLygqXjpk65Tqw5FOijH4URYkN_QMf_fI9saEkNzxCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شرط قبولی ذکر به نقل از آیت‌الله بهجت
🎙
استاد فاطمی‌نیا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/451023" target="_blank">📅 04:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451022">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
حملات نظامی دشمن آمریکایی به حوالی قشم
🔹
استانداری هرمزگان: در ساعت ۳:۴۰ نقطه‌ای در حوالی قشم هدف حملۀ نظامی دشمن آمریکایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/451022" target="_blank">📅 04:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451021">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufWrCrw6zT7Wckge4HvxLZ122CGZThN2ImN3BbQzcZesmucXAQnMCtkrk17Jm2ZVnYJNA7SORVT5DtTEf7E8Ug8f7pxBFHOwaaLfPw2DtHyfWHYQDwJgGzT3YBYPS013VJkm5Mj0Cgi3r-3KdnGpztvxuyerq7uliQLqjml-yyd0Qe8rXEa9b51_RWMZ98bkh5ZnAC95AJWQPPKwOFWrkh-N-k6u137px--tRUUTFSwqnQd403udFW5E4DWsrxdmop32srSlaQk4IGy13SoU4eGbvpIOuuBaoGlDiE6ip0nWR7ayZeIKnp0RJT0uPAUp7Cgebl_H-sPZeYP0avaIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ ضربه تا خاموشی هاب امارات
🔹
هرگاه سخن از قدرت اقتصادی امارات به میان می‌آید، معمولاً نگاه‌ها سمت برج‌های بلند دبی، مراکز مالی بین‌المللی و درآمدهای نفتی ابوظبی معطوف می‌شود؛ اما پشت این تصویر، شبکه‌ای از زیرساخت‌های حیاتی قرار دارد که ستون اصلی نقش جهانی امارات را شکل داده است؛ بنادر عظیم، فرودگاه‌های بین‌المللی، مناطق آزاد تجاری و مراکز لجستیکی که این کشور را به یکی از مهم‌ترین گره‌های تجارت، انرژی و حمل‌ونقل جهان تبدیل کرده‌اند.
🔹
از همین رو، پس از هشدار یک مقام نیروهای مسلح دربارۀ ضرورت تخلیۀ فرودگاه‌های دبی و ابوظبی و بنادر فجیره و جبل‌علی در صورت گسترش درگیری، توجه‌ها به اهمیت راهبردی این چهار نقطه جلب شد.
🔹
اختلال گسترده در این مراکز می‌تواند نه‌تنها تجارت و اقتصاد داخلی امارات، بلکه شبکه‌های لجستیکی منطقه، مسیرهای حمل‌ونقل، بازار انرژی و بخشی از زنجیره تأمین جهانی را تحت تأثیر قرار دهد.
🔗
اما اهمیت دقیق این چهار زیرساخت در چیست، و اگر هم‌زمان از کار بیفتند چه رخ می‌دهد؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/451021" target="_blank">📅 03:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451014">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZKtGRzrQPpMhlOohbu5iEhd9AXsCByIb2A14kEVrr9fi30gDqy0AyI1lJncEYzds4uxAXCxZJFcSwpnMgmvQWMiOoqPYjEEudwnHR-vj-UjUj_hDxTzXcHIzsMt8enQQCH-UuUQaOPimPKfg0bnUsLbHdrN9PjhiyAsEcorfqO2CFQ05ADM7kreVTGquXYTnbdJHX94rh9Qy-40hQFwo7RigJzJaWz7GlRsNa1qQmowrZl8j2BsDZN6hTJYJURq0rSgUu7t2MSfFFo888VcKLAcRS5pMchi-eVXUZLzqf-3PSeCvZKqdaLMhwd8fb5ms0bdZD9IFYOWW4ZIzQdE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxbmzlPfDvlci7bmnVfC0ywT_d8rMqGYL0MzL0VWCBVat5y6ydbgPLB6_YBwtvY-ccVmlfUBV2gGvLw7vEDAAT0iFOlkmOE0B5NmNC1mhBqFYY3vwWMrQBFdgHiV3m06MnbLVUWmJEaa6b9BjqN0Dx1eQKjb14HtYHAOhQgRa-sO1qdAaNFoX240ZjrIn6LaLwT5mvDKbALi2A3Jpo-74rpa5W7nxDnDKn_9Ft902bfiNdHiw7tG7jYG2JWmuI6HjD01mxygY_As8cAnHIbk8PJBKFZXW7cH9bjCBtug6xeUH-0_HFQSPeiZC8NH_2gMAJ-kmnKKC0FR5TPOJI2AzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5iXfTb1hFvZPrrAb9ZYuGBtdSY1OjT_K-jiqPPdIBkIdJe-TIYCCL4lYtRvh3tG1RHMFza4lud805-tHbhk3ndYY7_PONV3yennrfwzssMwb_mvir3n2F-nPjkj66nt2Rs0Edhso004dz-xZXohqNLufQp5AvucQM935x6jgjXuNHcBJayN0phDgwlb2FtMv6HCIFzMZ4uAVmpN5JbPIzregxMJAMiVgii6wH2ZJWzKZ_7GmQALdR_I4HP-bjGtLyXTwCKCFI1F0fvNaB7BJBZHi8fb78slCWa2NzNRadHDvfMU-54rxPBeUlsOIr9HUwOy6MEwyblXxuVDmwcyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYbwCzo4F9Lrxn-ySUi887du3ajyWW1cXv7bC2YGl_ZPaVZlSI-CL2yehEJeYf43vZQY4zXILLNyvXIup3tvfx2ZNzSIgkD7_hj8Epjgnalapv27xKHH36cn_ktLAtCtFpwvAhTzNuAWqVIrdRxHJVwAHymDNzV5keuvRoY8yxjET8mAQZwR0mlY6XeXwI5e4g32FKd0ZL1piJgPT9bVTRuZ0krEopnOEOKXy7mCkDVOrcdFf8HvmxxpjewAdopDGYWL-mbSPuBH-fiVpZ7JAhvUzlUIfvu_dk171tOufjcx1I3VaR5NvvM2_DXd4GeWgh1QcDkSlSFMmw8J9ySDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbtmWY7DmT0bb7FvKu8Sld4SZCTQEuNM2rQjKWVwC42Ep1rAC447hjDsGqa7IdthhsGlKzQwD6oIUJtrfjeh6rIIru_ac1byTs6GVg3cwx2DsnwowV3YsQGby9XDS12D4N6T0GQj10EgXKQ8-iEuNUs3aV5zpB5dtfFPnZVDfWOHDFMnC3hKGCIHgMNn2bhRRQHB_Cd93ZZpedYYF3z--Xe4QG8g68nmmpDiZIzHkAom7MkiLMn8BD-vnpZ8kov9v-iaC7iKrTyJReQO6BJ3Olz-XKkGk8iGJZrJ0Ri5IA_MesPQ3hKTcalyCnIC049oooShcMqbkyAgJ1pkJZRgAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJRpxpxWXBhhEDyExhvStyOJaZ7Cx3DPX1Oqpk3NTuhMI-oGPZxvhNPQqUxGZjdjAJ4b49WXNgaPCu7v71XEGDORJAU5oVcBbcu8NlnDQT8KeskPktSYLzbHrnsyO9ZiHH7qvM1I7iZbaeK-Bj0Esg1jh6bAM_ZKRxMR1yPVPtJDWR6R4hINVHOFmK5HC8YNVp-5BVWb1SOESh2P0jBvWIJZHZrdpjoqR1aY-OSeQSm2qnX4HaHY8Ja-P3hOkKWWnnmSyCmw5NW3OW7LFWvK-SgHSN_1sAo-aVP68bo0yhgR7zRMeVtyWywPNhW0KL6JEqqv8hYahJdhID7VRrE3jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSG0Qo5je13Vyk1g2G7Tckwa1i5SMRkl96dhOTh5hVAfp688FFegIEHQMX7Wbv0i9Seo4iYXhyvenF1DqN-oslnewf6lo-w0MNPg-H7G4TLyNg1Uk5pfEOuTTLSa2pxnGPnSYIQD45lY-Lk-BOO95AaMB2X-OspQ9zdskASODrsSY69JgxqBI_LTm7LgSDc0DP0HxUW4jcJrBxjY9Jn700UgRXuOgFUWqj1hQ2XmLaneY6XvyaGPyyIkosDyjG5-zdWvuBFsm9RN0b_3bRL7_N4DENwAZwsqoG7dSiy4yl8s_KT7uvgOo3kyrEtQDCGlxr3-AxtLSzC-SKZIWfbX3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تنگۀ هرمز میراث ایرانیان
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/451014" target="_blank">📅 03:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451013">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCaYEcXMgUCg_7qRSd-I5GVKfDNdSeqCJpY7O9a9rcP829cDxpVt5HOT2kW5sE9ppJ3UlaXlFBKipz7FVOA5lcRA1cV-QZY8qtGO6NjjCGt3T-j-YzO2eRKHd8zQn-KdP3U3b5G7j6Eqkq-DQRNIuHvf7c2ZPSko6aUQBwipjPd6CCtH5A3CiuxjRSJE-trseJ6Ik78hVtgx-AdkTW-VR53S-i7znJN53pH6dKeQmA4BhfT5UazxzNF_2Q-4j4P63N98-G3xSzQXaaP0P8diBOoK8bZ8siBF1-KAYxyIXYWN43S14pdeQoY7VkWLP_wA0zc3EBkhDhJF29kbVaQvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
انگلیس با گل ششم بازی را تمام کرد
⚽️
فرانسه ۴ - ۶ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/451013" target="_blank">📅 03:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451012">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275437ee88.mp4?token=ewqu3ABAl_sCltCYA52U2lN3G4D40TG3FIgYn28gsqlNo4ZFOpKBMLkAKIZfE8fGdXbI4OYJ3wmWUJu5tU1PEUNl4m3xDrsCx10rBNPtf2nWZiDm4LwiFFFdJyeO3TWyD0Fs6z17dLstitDMjnJDJpUWyJ5WDoTy4Caa8wZT0bGJVT4bDgaENW8onooPyDwPhYe2xI0LtTTZYr8h_N9lcprNtQVh0iFwK53BOVWrQT4QzMCEylVIdS6Pb3uiVz29gJeNxpEj_VObdfJR42aI9ZUDw3UC9angIlomoVt8CJ0nWfX5um2QNvRP1cv75vHN6xhTRnpIgGX6u8ynVy8LKwdVSc58dqNX70tXdO3eHafuqWLi-W4AKss1iAWtEMxL5psCy_aI3B-a-3diAD0_-5Qk95Rte31hSlZQjriJNXqHCNDg_VeIy9ecdh-Smqie951djrsy-FAK-8WCuMlWJ9nrPdRRh4Ib0ECXV2Uphvn7ODwS6b7u0GILaLs-PEqKnDPs_oulCjtH4xo2Ov7UjhrwYapSGFKGSDj0Iv30d3psCWfhiJVX2vH2EWTa8J9bl5HocdIGJMrbp7qArbxPhA8TVEN67BAklb2A1RRohNHl_LAENdf01vZ8ibKlqBrzD1ZQ3hwvzzqH9YmuQbdStuFQjmK0ZFW335GRtixX-28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275437ee88.mp4?token=ewqu3ABAl_sCltCYA52U2lN3G4D40TG3FIgYn28gsqlNo4ZFOpKBMLkAKIZfE8fGdXbI4OYJ3wmWUJu5tU1PEUNl4m3xDrsCx10rBNPtf2nWZiDm4LwiFFFdJyeO3TWyD0Fs6z17dLstitDMjnJDJpUWyJ5WDoTy4Caa8wZT0bGJVT4bDgaENW8onooPyDwPhYe2xI0LtTTZYr8h_N9lcprNtQVh0iFwK53BOVWrQT4QzMCEylVIdS6Pb3uiVz29gJeNxpEj_VObdfJR42aI9ZUDw3UC9angIlomoVt8CJ0nWfX5um2QNvRP1cv75vHN6xhTRnpIgGX6u8ynVy8LKwdVSc58dqNX70tXdO3eHafuqWLi-W4AKss1iAWtEMxL5psCy_aI3B-a-3diAD0_-5Qk95Rte31hSlZQjriJNXqHCNDg_VeIy9ecdh-Smqie951djrsy-FAK-8WCuMlWJ9nrPdRRh4Ib0ECXV2Uphvn7ODwS6b7u0GILaLs-PEqKnDPs_oulCjtH4xo2Ov7UjhrwYapSGFKGSDj0Iv30d3psCWfhiJVX2vH2EWTa8J9bl5HocdIGJMrbp7qArbxPhA8TVEN67BAklb2A1RRohNHl_LAENdf01vZ8ibKlqBrzD1ZQ3hwvzzqH9YmuQbdStuFQjmK0ZFW335GRtixX-28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌خوانی حسن شالبافان در مراسم یادبود مردم کهریزک برای رهبر شهید انقلاب در ایستگاه ۱۴۰ تجمعات مردمی
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/451012" target="_blank">📅 03:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451011">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efef3f4c7.mp4?token=CLRAMTpASqA8RCCOmNe4ElxJjsDolPW_fux-vAD770XcmvOK8bG-pp3-h36m5jrnK2r-YKyH9acKq9pQqeUjGu0oVJBqipJ53_loda77PuuDsbxBNdQFsAbeQD9dRhI3VMs96sYbsnB4m4v3GRKRkyhaXV-gtTK0DhnB9GQnlw-z1yj-k9UPRjvY-AbAPrtItOQ4dfuYuwGK3PGY0KAR7dj9eC7mxZbrCWZ_wEdVlG4V86N1pBUeVUsPjcayVEO_qQbG64WKD3AvOI49563mvcMbOBRa-NqNTx6ZCcgIx_aAD6I_A247JK9bOfelnV9z4VVxR2jtF1pmExtjc0bevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efef3f4c7.mp4?token=CLRAMTpASqA8RCCOmNe4ElxJjsDolPW_fux-vAD770XcmvOK8bG-pp3-h36m5jrnK2r-YKyH9acKq9pQqeUjGu0oVJBqipJ53_loda77PuuDsbxBNdQFsAbeQD9dRhI3VMs96sYbsnB4m4v3GRKRkyhaXV-gtTK0DhnB9GQnlw-z1yj-k9UPRjvY-AbAPrtItOQ4dfuYuwGK3PGY0KAR7dj9eC7mxZbrCWZ_wEdVlG4V86N1pBUeVUsPjcayVEO_qQbG64WKD3AvOI49563mvcMbOBRa-NqNTx6ZCcgIx_aAD6I_A247JK9bOfelnV9z4VVxR2jtF1pmExtjc0bevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی گسترده در مقر گروهک‌های تجزیه‌طلب اربیل  @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/451011" target="_blank">📅 02:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451010">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تکذیب انفجار در کیش و بندرلنگه
🔹
استانداری هرمزگان: تاکنون اصابتی در کیش و بندرلنگه گزارش نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/451010" target="_blank">📅 02:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451009">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
حملات نظامی دشمن آمریکایی به حوالی حاجی‌آباد
🔹
استانداری هرمزگان: در ساعت ۲:۱۰ نقطه‌ای در حوالی حاجی‌آباد هدف حملۀ نظامی دشمن آمریکایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/451009" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451008">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4714689b1f.mp4?token=Z-4jqI03bUSPw1JnN5wwlAEmEXlGKRRbvYgCpMsGM2ttB8m4qQDV5KRl9udcDANg_NDvVXbl7gu96Vn6N0kGCv6Ef22dVdSOICltiFdgubF6OCIWhfsK48QhTEyFMtXQ5q5zTQBAPlItRxbIQmxFg25PU5lBSe3Ycg7j_Rj6RdNtc_IsOQcy9_go9XF9-nKpUDSL5YhME_qe5OSni5HwsJFV3r4tm26TKuOWLRi7M6uc21nOcnFI4t2DQIJYOVLbs_SBeErNX-hvDAkyGk7S8QIWNglCFE-TQl6syIro8V5uAL44bBUgu0nwoKQzsBuV4gMGOTiLDwxN4QAk95gCCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4714689b1f.mp4?token=Z-4jqI03bUSPw1JnN5wwlAEmEXlGKRRbvYgCpMsGM2ttB8m4qQDV5KRl9udcDANg_NDvVXbl7gu96Vn6N0kGCv6Ef22dVdSOICltiFdgubF6OCIWhfsK48QhTEyFMtXQ5q5zTQBAPlItRxbIQmxFg25PU5lBSe3Ycg7j_Rj6RdNtc_IsOQcy9_go9XF9-nKpUDSL5YhME_qe5OSni5HwsJFV3r4tm26TKuOWLRi7M6uc21nOcnFI4t2DQIJYOVLbs_SBeErNX-hvDAkyGk7S8QIWNglCFE-TQl6syIro8V5uAL44bBUgu0nwoKQzsBuV4gMGOTiLDwxN4QAk95gCCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل چهارم فرانسه در وقت اضافه
⚽️
فرانسه ۴ - ۵ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/451008" target="_blank">📅 02:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451007">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6bb19483.mp4?token=SdHxw9U4gokpkRSU-6CMaFMXSxQCX_fpV1jYKcQTBbbVfWEpcbJ7XZZYVHKVLrxBz8SwQljYKRtZIsIy7ld16eCpzfXtw7Qo1rPXyswvQqYUUQ3YqQDXZJtlNilRWOIS9r3fRaT8penTKqslSJO16ThAzXE5B1wxKJMfisv8vaE6Ct4OjQoeDoufuiTJ77Z6AHnBmPhFiq3iYTSIXorF4JZ5tS3RDTpMMdfabGpdN7gAUEFxE2bHslpy5u2ZGHSTxNbEA86gP21BveFgvA1fQLj7JlNAKacu3InmxHebwhEFXgj4_a63yi7uLaJpy_DnnqmAEjWRujvSBw6nfxT_TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6bb19483.mp4?token=SdHxw9U4gokpkRSU-6CMaFMXSxQCX_fpV1jYKcQTBbbVfWEpcbJ7XZZYVHKVLrxBz8SwQljYKRtZIsIy7ld16eCpzfXtw7Qo1rPXyswvQqYUUQ3YqQDXZJtlNilRWOIS9r3fRaT8penTKqslSJO16ThAzXE5B1wxKJMfisv8vaE6Ct4OjQoeDoufuiTJ77Z6AHnBmPhFiq3iYTSIXorF4JZ5tS3RDTpMMdfabGpdN7gAUEFxE2bHslpy5u2ZGHSTxNbEA86gP21BveFgvA1fQLj7JlNAKacu3InmxHebwhEFXgj4_a63yi7uLaJpy_DnnqmAEjWRujvSBw6nfxT_TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هت‌تریک از روی نقطه پنالتی؛ گل پنجم انگلیس در دقایق پایانی
⚽️
انگلیس ۵ - ۳ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/451007" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451005">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63191114b9.mp4?token=IgeQhisV3EUGZyGTEBEJRwOfGA4-DqULhiiYp2BaaK0wGG9r9SIAkdE4L7-0Gi3-7_7yZylR_yWUD7ltitO_KrN_Oxsh4AGP3wzKWubiMHQsKvX5L6Qaykl9qWjkgBBK74vK05TUVoiqOM5i1Fu7XnJFojlV2E7jGySkeS8rz5RdIUjCi4r9oAtNpVah2uYQneYOJF9nVJb200-Y_suNF5Q9JI0Z7WlsZ3awuEMPrMrzpwkNonDX6dbjkktsbD1kPgeXEjRbjqsQLR917fVlAr1UQgV8jnTArAizO3nxk1GcuJqvNu0-pkJQni_R-Uyt8OvHR1O60XAIxwiAFoHQ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63191114b9.mp4?token=IgeQhisV3EUGZyGTEBEJRwOfGA4-DqULhiiYp2BaaK0wGG9r9SIAkdE4L7-0Gi3-7_7yZylR_yWUD7ltitO_KrN_Oxsh4AGP3wzKWubiMHQsKvX5L6Qaykl9qWjkgBBK74vK05TUVoiqOM5i1Fu7XnJFojlV2E7jGySkeS8rz5RdIUjCi4r9oAtNpVah2uYQneYOJF9nVJb200-Y_suNF5Q9JI0Z7WlsZ3awuEMPrMrzpwkNonDX6dbjkktsbD1kPgeXEjRbjqsQLR917fVlAr1UQgV8jnTArAizO3nxk1GcuJqvNu0-pkJQni_R-Uyt8OvHR1O60XAIxwiAFoHQ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امباپه در دقیقۀ ۶۷ گل سوم فرانسه را هم زد
⚽️
فرانسه ۳ - ۴ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/451005" target="_blank">📅 02:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451004">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b93e8cca8.mp4?token=CdafwyezIIzp9tmteHSMYuy36lI489ocA3sEOeBk4UIuBsp55P6B7OosI_iDdRPbOPU8O_7TM9Nl6XR_SspIxbOGAw22ldr9GIRWimhdgOA-bRCgjiCZVmp7ocONZVOcZvY2C_nBnS1_FnTXYUWP7xYWR5MY2VKbD9RvsbxIQfZw_r6ULgbUmsOIp4eFcmYRzdacu8p2webM_KN8sDAO46loS5PuTlfbG1i_7pJ5RxMovp1KgjjukpfveuTBDQJOSLoVfBUcE2a1bvrysbFFFd4dwbrGQNffsRpvAqssCwtU1tXP48z3gW4Yy-f754tKUGHgGrk5cWm_kqj-8IKEBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b93e8cca8.mp4?token=CdafwyezIIzp9tmteHSMYuy36lI489ocA3sEOeBk4UIuBsp55P6B7OosI_iDdRPbOPU8O_7TM9Nl6XR_SspIxbOGAw22ldr9GIRWimhdgOA-bRCgjiCZVmp7ocONZVOcZvY2C_nBnS1_FnTXYUWP7xYWR5MY2VKbD9RvsbxIQfZw_r6ULgbUmsOIp4eFcmYRzdacu8p2webM_KN8sDAO46loS5PuTlfbG1i_7pJ5RxMovp1KgjjukpfveuTBDQJOSLoVfBUcE2a1bvrysbFFFd4dwbrGQNffsRpvAqssCwtU1tXP48z3gW4Yy-f754tKUGHgGrk5cWm_kqj-8IKEBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع عراقی: همزمان با حمله به کنسولگری آمریکا، مقر گروهک‌های تجزیه‌طلب در اربیل نیز مورد حمله قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/451004" target="_blank">📅 02:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451003">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNFHaLCHA4bIi8z3JRn0VWhUGMrf10pHRnKjdP3WkJJwJM9vzlU7zGdil5S9okYQ10EZtnMn6DkFgxpqFjeEG1_UTmvZP4lC2rBUvpcOsJvDC5WpytBeVgEiGiu3UHxxFj7rq3hLbVbt7DLj5yeK_WpnZDWF7JLSU3Enh6LJ1fncxQYo8QassY4MnAEU624BnGvXw58sx-Wrep-_zySwL0rdnzoy7LkrDcR7A4DdBiynJiyMlIqDoqNI5Hkmp9gjkthh4UqauloOReBWXKeSPCPYdDGJ-D_3sr61e2TeyW4z38IUQx5uYTmz0GXOSUs7a1NPKWlQJhsc6wSrjB7bcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
امباپه با ۲۲ گل بهترین گلزن تاریخ جام‌جهانی شد
@Sportfars</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/451003" target="_blank">📅 02:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451002">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/131b049251.mp4?token=FmumSF7Ji8GGbFyM8wBq92JfLCifUjLvDRcuP0TGvO2ff8VJ1mk-jndZwMaDB8HCFli_-cwsw0aYRxxdjF0LQFXSeNsC3OatF0VDjtsBPzffERvhSQVYo4MIpwyVfZ_oXnKIhN-fvAWFHZsJveEBPafbXsOLrrPRiKl5yOQIPl8MNKusdZqCQMhsBzP7mwVoIrots36ANQVifYEkWlyLC8khFhHzeWy7oHi7T7iAZVsgG1HsibxT5kvnAih7C24eTd_SnjzoS4pR2djE6NuqBxI-PzCKvYC5fvkOw71AQqPTr00AKwWMbsWMqy219MC6fwmouixUS5BKMyj_Cjq2PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/131b049251.mp4?token=FmumSF7Ji8GGbFyM8wBq92JfLCifUjLvDRcuP0TGvO2ff8VJ1mk-jndZwMaDB8HCFli_-cwsw0aYRxxdjF0LQFXSeNsC3OatF0VDjtsBPzffERvhSQVYo4MIpwyVfZ_oXnKIhN-fvAWFHZsJveEBPafbXsOLrrPRiKl5yOQIPl8MNKusdZqCQMhsBzP7mwVoIrots36ANQVifYEkWlyLC8khFhHzeWy7oHi7T7iAZVsgG1HsibxT5kvnAih7C24eTd_SnjzoS4pR2djE6NuqBxI-PzCKvYC5fvkOw71AQqPTr00AKwWMbsWMqy219MC6fwmouixUS5BKMyj_Cjq2PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم فرانسه در دقیقۀ ۵۳
⚽️
فرانسه ۲ - ۴ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/451002" target="_blank">📅 02:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451001">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
حملۀ دشمن آمریکایی به حوالی سیریک
🔹
استانداری هرمزگان: در ساعت ۱:۳۰ نقطه‌ای در حوالی سیریک هدف حملۀ نظامی دشمن آمریکایی قرار گرفت.
🔸
سنتکام دقایقی پیش از آغاز حملات آمریکا علیه خاک ایران خبر داده است.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/451001" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451000">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
🔴
منابع عراقی از حملات سایبری علیه شرکت‌های گازی اماراتی و آمریکایی در اربیل خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/451000" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450999">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
منابع عراقی: حملۀ پهپادی به کنسولگری آمریکا در اربیل ادامه دارد. کنسولگری آمریکا مورد حملۀ گستردۀ پهپادی قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/450999" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450998">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933f021d4e.mp4?token=jsxQJpFlOPnsEIiWn9rZzxRkLqw7syJE0XX7b8GpAiUbfaBPpghNwwWWVazv84dlsFJGawz5DgdMjggmDOEqEb0IfoCOnJNaH5CVIGrCTqx5q0tDQjTLmAb3dD9ePkXit17HXJ6-mLWlTRTxVsqOvKHRrg6ZLFjIyrNYfiM_LujHF4mxAQCOz36VvTrJFH-ya99bIivBlyHzC8FBNm4J4R8obk_LCHx-06folo14hmvWMF2ps2YU78KhxlMghYZmzCAjbPO5Wj-ccBNo9hwaOb_i9AM9vCFj_J80RfIY8eOKRhQI8fVam8k9Y9EmQi4vefOp1wJABVPVsbpKoYH8bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933f021d4e.mp4?token=jsxQJpFlOPnsEIiWn9rZzxRkLqw7syJE0XX7b8GpAiUbfaBPpghNwwWWVazv84dlsFJGawz5DgdMjggmDOEqEb0IfoCOnJNaH5CVIGrCTqx5q0tDQjTLmAb3dD9ePkXit17HXJ6-mLWlTRTxVsqOvKHRrg6ZLFjIyrNYfiM_LujHF4mxAQCOz36VvTrJFH-ya99bIivBlyHzC8FBNm4J4R8obk_LCHx-06folo14hmvWMF2ps2YU78KhxlMghYZmzCAjbPO5Wj-ccBNo9hwaOb_i9AM9vCFj_J80RfIY8eOKRhQI8fVam8k9Y9EmQi4vefOp1wJABVPVsbpKoYH8bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امباپه در دقیقۀ ۴۷ گل اول فرانسه را زد
⚽️
فرانسه ۱ - ۴ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/450998" target="_blank">📅 01:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450997">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73ab28dde3.mp4?token=A22qsxF3vKdn9DSW4M_jaRLIZSm6fjvre7x7EA55AR9xRZElMAv59hy7Ie7JRU3vuA97TVjhZbnoZ-IF_CnK5ikOIfJP6fgMs61Rek8nihyKAkkAGw1yKnJMexPVA5uqgpuXOARAYxKPRtT7mShmIbGziVpLtE_niVNkFM4OL3_bJG_G8jQcENKYyO8Vl6MPvyN0di3Lk8meDpwAIhP2A3THOarhEqsAwxFIcy-ZR47uUMa7TLPJSU2GhVkazcCnxF6GGzXovwpd9YJQ9hiI9BQYOPaGMqqZkAqsrOoSdUNaBvGQmihPTWQM-iLka3dSRwHVQSB4RZA0mhpg5Ud5bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73ab28dde3.mp4?token=A22qsxF3vKdn9DSW4M_jaRLIZSm6fjvre7x7EA55AR9xRZElMAv59hy7Ie7JRU3vuA97TVjhZbnoZ-IF_CnK5ikOIfJP6fgMs61Rek8nihyKAkkAGw1yKnJMexPVA5uqgpuXOARAYxKPRtT7mShmIbGziVpLtE_niVNkFM4OL3_bJG_G8jQcENKYyO8Vl6MPvyN0di3Lk8meDpwAIhP2A3THOarhEqsAwxFIcy-ZR47uUMa7TLPJSU2GhVkazcCnxF6GGzXovwpd9YJQ9hiI9BQYOPaGMqqZkAqsrOoSdUNaBvGQmihPTWQM-iLka3dSRwHVQSB4RZA0mhpg5Ud5bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
شرکت نفت کویت: صبح امروز یک مرکز نفتی مهم توسط ایران هدف حمله قرار گرفت و خسارت‌های زیادی به آن وارد شد. @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/450997" target="_blank">📅 01:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450996">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🔴
منابع عراقی: همزمان با حمله به کنسولگری آمریکا، مقر گروهک‌های تجزیه‌طلب در اربیل نیز مورد حمله قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/450996" target="_blank">📅 01:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450995">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fded8ed20.mp4?token=twR3mB58iD3mgzWQdfVkk9Xt8NUBQrrCX5kkwaGalawUeW5MHw_lfyBwPv_plZWnA-dXfKXDu6FObF8_xVYakpx8hpItEdGPYCKzwXe6xOFFyMkZ33aW5SRg2tF4BMtHMp4CWDuTjWIGUql1kG5K6KlA1O5-0YZN-S3WuhtAL3P5_oiUG54TfMsNwCwTM830ctX1xz9kkmDSWI10ccdndNVlx-xJxGhYtZDAF92P87ot4WUkxIPuzNX9H3YoSEv0bff-jNEZtbvpaWH3LYUh3Evu_CPaQgMG00oRHgVrGf96yCovHEPX7UdrQEM1c4asrA3YS9HJWoY1jYmHpBm2RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fded8ed20.mp4?token=twR3mB58iD3mgzWQdfVkk9Xt8NUBQrrCX5kkwaGalawUeW5MHw_lfyBwPv_plZWnA-dXfKXDu6FObF8_xVYakpx8hpItEdGPYCKzwXe6xOFFyMkZ33aW5SRg2tF4BMtHMp4CWDuTjWIGUql1kG5K6KlA1O5-0YZN-S3WuhtAL3P5_oiUG54TfMsNwCwTM830ctX1xz9kkmDSWI10ccdndNVlx-xJxGhYtZDAF92P87ot4WUkxIPuzNX9H3YoSEv0bff-jNEZtbvpaWH3LYUh3Evu_CPaQgMG00oRHgVrGf96yCovHEPX7UdrQEM1c4asrA3YS9HJWoY1jYmHpBm2RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل چهارم انگلیس به فرانسه توسط ساکا در دقیقه ۱+۴۵
⚽️
انگلیس ۴ ـ ۰ فرانسه  @Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450995" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450994">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
رسانه‌های عراقی از وقوع چندین انفجار در کنسولگری آمریکا در اربیل خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/450994" target="_blank">📅 01:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450993">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
رسانه‌های عراقی از وقوع چندین انفجار در کنسولگری آمریکا در اربیل خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450993" target="_blank">📅 01:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450992">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWcFYKF_-NVgceVIDhANR1wnNUuICRO0hg7Di6SkjhbSjdQgANS0kHIPlDSb029R0y9F1J7EWtou0F1Ut6WWH636MtP4FHjk9qXkVyRVKhVEN9-jQOCdoxuwKuS74C5JZib3WVYJuX1gN5b4crXDJyU3x9cQKwVdo_5bt56H-v8lypShQuvZybv_qJ9pHMVomonnPkExnTy0SQz7INkViVa_ri4phXUg07kKsC4Ie7CcfRIbRInTPtHpc9Ny0D_70NIMVHmAz8UukNWm-QLXC6eQArsGR60JvFNmKrisMLz3yNLF5hBzh1W88D5WL1549vkRWFuUiID0sl7ZKe04nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آمار نیمۀ اول بازی انگلیس و فرانسه
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/450992" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450991">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4302423563.mp4?token=OtIWlcIU3YufEXBIW7tZvwsQeKZNDk93of6xmFa3eAvkh4HYnhk9bL5OvlYN9shiq7CMQvr6qMvVCHUn6tHM3Ab7kdigWCpKabuwAS1eYgo5P6KUXDqM_kC9TLMtoUn0k6vP6BS1DwNTV4u2WwL2rfK_dlt0VbInd_HFtKSG1NU_4BFPaS7BB420US6fzkEqlHx-Y7WtDAOg33u_V6lGz6IShhvYlG5-_QBOQGmJLX4K6EXTy-MXR-jCznAjJMjceNHItQPiTg_z_8kDCz9XlQbXy-GWRY31nrediNgfNz8PY6sOgB-560-1dTBjq6qpwLJPYwcK2VAtgr-FQy0eaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4302423563.mp4?token=OtIWlcIU3YufEXBIW7tZvwsQeKZNDk93of6xmFa3eAvkh4HYnhk9bL5OvlYN9shiq7CMQvr6qMvVCHUn6tHM3Ab7kdigWCpKabuwAS1eYgo5P6KUXDqM_kC9TLMtoUn0k6vP6BS1DwNTV4u2WwL2rfK_dlt0VbInd_HFtKSG1NU_4BFPaS7BB420US6fzkEqlHx-Y7WtDAOg33u_V6lGz6IShhvYlG5-_QBOQGmJLX4K6EXTy-MXR-jCznAjJMjceNHItQPiTg_z_8kDCz9XlQbXy-GWRY31nrediNgfNz8PY6sOgB-560-1dTBjq6qpwLJPYwcK2VAtgr-FQy0eaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرانسه گل سوم را هم خورد
⚽️
انگلیس ۳ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/450991" target="_blank">📅 01:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450990">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f8764ea6.mp4?token=TH6nMAdbYyFN4hpN30SB2uFCqabWfehQWbAKOI3vLVgevo6ASEiaSoB0CWZSS20AfhHPKL9x_CTRJL8ooZM_yedMPkLcPHP66qRwr3_9LECH0lhyM03_jLUjI7GMaiSiWIa422I_LIaHaBFL-7TpiFGJGvpG3XzZ7S1OathFHF5jqI_NPpr7dOUPPkQWLv1JrLTE5bDVSvvPAWzdfCMXTvQMaXCbTQJrlQg1F0q3EVmhJzvoejiZ2RIen3iMjwVbuTdoYSEoWux_1n5X7zOzLqfG_8TsaJs5x08eckyud2_0wN8jzRacm4wG588FC4JKvMjRUuI9lyo-3nCvhXrumw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f8764ea6.mp4?token=TH6nMAdbYyFN4hpN30SB2uFCqabWfehQWbAKOI3vLVgevo6ASEiaSoB0CWZSS20AfhHPKL9x_CTRJL8ooZM_yedMPkLcPHP66qRwr3_9LECH0lhyM03_jLUjI7GMaiSiWIa422I_LIaHaBFL-7TpiFGJGvpG3XzZ7S1OathFHF5jqI_NPpr7dOUPPkQWLv1JrLTE5bDVSvvPAWzdfCMXTvQMaXCbTQJrlQg1F0q3EVmhJzvoejiZ2RIen3iMjwVbuTdoYSEoWux_1n5X7zOzLqfG_8TsaJs5x08eckyud2_0wN8jzRacm4wG588FC4JKvMjRUuI9lyo-3nCvhXrumw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انگلیس گل دوم را هم زد
⚽️
انگلیس ۲ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/450990" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450984">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CYBfhUP2yGq9oLIucrAJd9VB5ABWK3j1IuzmgI3ERUlaQTwaYj9uid0-ewEYYgm5VNMqTP0a55T4huBQQXuPIlj4iQtRYUd7MlFXhZSgLd8uILWu-XCKgrGmGmTW8kqmc7mn85JfmZrPMm1HD_hg93pVdjXHxB7ab6Eyc7dZ6X38gJC2wMzRHLzY_2fTAhdv-Oc893-8bB6Ep-QE724R_tGDUBPS7ap_OBNS-7VbfNt1yL2yQjPxdzgXdTtOmfNx9vBgFF-xIx3LKm1kAszrgmMzH5_DyWPvKB7rKDbfy4HeXD3POPkpwsdlGQGa96nFqzRG05D3gZgrLRy4ebnrLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbii6J8WfaWhCcW-fV1TJOF7KLCVz7kWrTarv4Ch2vmQO2iT33UjPaELCSznHSIK8VcOfsDWdEZfzUS91BF5mGnzFhzEMHqCt5S0An4_5_GaFnSTnbjofqRIge6mu1LH8Sh0yclgcr4upCu8dpXa6kBjelgOro5s-To9819qle90rTIB9NIIhq_66NUhyawEv5kcWnS-QDtt2HMYzHCwE1TNFLQ-Fr5hTmS7jx1pFV31_XQHxXdl-eIpS-0U3if8h046cUfejRE4v6Z_Yfh3wM684UiMm__LXg77huWS0De2vbpkrK7LJ5vHRICK9Wz_-yl4zrps-QNu3NFRwTo10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TO7N782eZ3Uj5_0wiP9p6olp0cWwc4vS5mUHNg2Jhjp0roHem9s_VZF9K1hcBZqHVipCHtQArC0Tbj0-VHGJRevs8_Dz8D-aQYZzLFJ3Axe96b6ifpY8zGYngiYkn3aLDftrQ7YvefdUoeUtte43gaMZq8ITHMdxd_AbHZRRFgjF-S0aAithTvivpfdje5kX5xVehcLuYqG8srVd_U0U5rdYfyxWhovfRg06NgIpXmDWF85mO5QgtZwdMlKt2i0hXvMMBaaVkNHxwr2FEWn7KR0h23JzDLnO2NpGSzJv-_0ZsbxCcFcpmOJ0G8W8ImcFNjPnUPZMKm8bsr14Ar1UtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwyDQk9xLu5D877u39zWqz05UuDFZZJ0s43F0gmf9WYAnlFgHHLEdjIFtmw6MLCsVOYEOhUjBg0zohf1TXfdP0PT1sXd74EuKTr1FKVx_8eI15XnpXFbU7KOPfFJUFFcWn70POnbru7HeV3T5X20su1_1KLDGKZda_4Q3-fo2bXlrZZ1owNIbRULru-e2jNVu4zlS0v-U6K4imrutwfn1HyAaSQrlyf-I2oJHjzQUMMp2GPqtYHX7gJhVvyzY-K0K8we07V1fF-NY4MLxGqI4lepkCWZJsTSEKu8Lx3QpmjS6pkKz6GMwazs3Arp9FnFji5k3hYKINR_x5IesJ-kUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slUFXitHS4K6RxWOM1PHcW9MxjRNujCY5pBNkk5IYQYDQowpJj1pnVm6Uksp_Lo9IIW6lAMSvKvtxeWZB4-kKW6NMCfLg4evjN2TaH3WjFEEmDtv_QBc-rv0tDfnR-_0CQRjN7IOE76H_646dnnsduov8WfFlaWVXb7aJA4hjtp2aaNrbgdNGGb6ieFW9kL5qHT8f8p1cEX9Wnc6ClCGeznbea0--4puPzn_XeHWseJhop5LUktOAeacdnbMXG4uTHwEtxp-Ju_rXD4yl5TK3XaVQ2fyvorLERO9l55IOV_m7FcBW_PuMR5U3Vf4iGKX2c_bcoCiZzr45if1M5eZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anoMxaCaxuYMSTpg9AVg2j22IPwkl-XD-aS3WmNu7451a-YjZVaPIcmeLEkDi3z0rEbUsn9zk6XQP1FSqvFYqZ9GRv8Nm8UPWX_dV08hmWwcM02RFwBu5mBhhFRWNL-V5eEj66dGQqZHgmKeymZf6cWHow_t_3cyS4KuVOWUSSf8U2snocbKts37WxdVxQIinXyA5oxqD4sfK1TkfZIPcqBiefJIgb_lm5xEjgU-5rJG5in_CT1oyBnPpDrMDp-zQPMnMblf6vGg51qdpoAiph80lGVcJkyuIf72lXnHpoqOkPXVKfs68BNRUvsOObVASpNsTprXxj2_lacxq5SM6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۲۸ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/450984" target="_blank">📅 01:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450974">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqVIRwfcU2VDyYe4Vq3EqU1e6PyHEpB0EQBBhRHZ3g3WJQO_O2JhRzFvseygvMuxbh75_GnHMScEdRSpL7ZJ301wEsxsf_j-pDtyiod87iUZ87MZsI3rsyLiOGmvCYHFKr7jlmXq38H8KkyNt1smGswTrFvRdJDBisON0BaqMN4PkBwFBMZH0OX_vZhGiw6NWQSnNBffYmgEDZ50FXh2wse3Rh5sphW72vySAjl2wl8Bt3MIq3DoTOj0-sBoWgis68lcQdGf4lVXiAPZtIzkLBvx-QSS1Pz06fKSk3lqS6wBcrbyZ8mYzSZzXfGpR7NRj_9FzBsCBrZH0jk93qxmwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2l-p8Ta-OJUu6kEWlnnNHTCFHnjTFNS5nAj07r6rVVXxvfxxQiSeP6VU0iGzSyzQrGRsUkjn18EXVzLuDVdx-OdVwFjl0Ix4rH7AlePtVmexBX3pO2Cck7CGX6y8u4zXezrqLApunOOXQZ1ReFTTfw7mRQgplXRZ3R-T5VWmy2cMUkQT_UZR245FyUSxkL5p70nJzOw4y-9HoKq3Rm-IscluvJmgYTyTYcwG1Yr48K9ylKNZ6HaKYoy7ObkkxG5zK62xAZe0EwehEd-m-8jp0s7biHMZewNUgf1GtE-LHn4EGUmi58SgebziL3TPqZWyWyGJQjZJ_GNwQTJDbefFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v81gZaj2aQuRlGM4QwqEbx8EGUZEvr7KuRI-W3WZn_TGtNq2rY8IJOwyLRhpe1VgATHyeiTjcp1E2cVzZ7MWjKi3OLhTGtjiHhXWCf5silqKiyGbf16AxGyESSC5TalzY8NLnBPEhhvlpuC3ksVwqci28Rt8peS5W5QuIyeCvtxvf-fbB5G12OvHiI7Kmuk8Hmwm4gyWAoaqCX6432BdsEVmmMIaI3MZRNLbz0rkRGWkaPZzT_5_YvvX8w-Zu4ZBCNVehYGdI4dZDI_uMuy5K4nczqS8Fp1AEhwj1dJza7ACg5rsbsDl81InlTJ0HmMbwvDQB4UTPh3tbmCHrjenuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egQJO_gdHSUaHyjT75sdBSRn-4HmFcrSJdDK3ZZgn-SxzyaB5sw-N28m3Y3EIHl3FeQPf3XCXO6Zm5qdsu-4oUeBEsVfyErWx3ysgRbHZ1LtdVMaUgCQXtM0S6OKrbwBDKOq09OUq-ZENEr7huwv7MM3qQH0T6DHWJQ0VNzzjmkm963-IG9hvC1LH6yXYdFa-5cRG8e-kLUGVLmeVNYi2gtioOz_iZtaXMwi6HBpE6w2yVllqMhuwPMs3XNhARQVTLsa3i3s3bLoheSkZollAWOgCr3hcOZeXDm1IsPpgCUdCGbaTNDnEF76NJ6V0u6DzSO_WqJMh0BTRqDdwCU3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E255wLxMiqioI2l0hVUBhZcZ255tYtUZ2gpcqT-QiKZQLj31RwFlYDT02Av4ZFGikMPdYS5G-FfbOWg0BMIHxVCpu6RGMPnLdxxEUdnAM_NzXeZklq5aLWCtLNwlmBYWv_x69S4WHJsoCek9ruc8YBp3I0foe4Ia8930Jl4oMV-1fpClwqXjrbXzWK2sxVjAQ2lqb7f_UZpf_1DEdbX4hFbIDhBrBVoXyy6tAANiNw61vUPJ5rBNW6bBVVIFOjpWmy5cmimrA5Zhn6XxzvOOu1kYTOsMLn2eMHsxm_w1bP11Gkel814NPfChd5N-AcuevcisFQZoosmWBrBHryyEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVS5VBSFglgQ2qPZsRhCNVv0cP-4b2SpHH1TwUOHWDXAhDYxTzFdff0BpNBvJHgGQDycuHlYZu98ROiSdEeZaJFq4CINyM0zdVwJ7-Yr4VzfdXiOJfs16nem4DhIsla-NcEEijOi_qDBSS94gCemSjWpLHeKLlhpnGZXmFtxpjfMu0AsAs1H9FqFtileiF-_VfrEGoyHXRRRo_48gBe0FOLiTF96TZZ5BWlxZXHfAaPiFnxbrmJHN2xcY28BPMDogqpMBKomHi10axdRz2OQRF_ecS87_L9l6gLOplKqV0tjUsHpMWc84KFM3vzLTxWji0ffb7I4K1-6-0GlvSvL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cCVI0Kf1L7ovuQP3KcIwyYgrZRw7jzgCnspSfs7-znWsQ0rUfTM6O-qPeMiRcVmKDkzvCvjnQd4v97BrhUEvkAYSd4PndYOhKkyp-rs27z2hT2pfv-yTXWWRWB08bYwpsuVasgRR3AjheEecEW-_dzZ1rBePD7J7SKZE4jFYkHM4fckI7j_i7vdPjI9CnI_NznVkGkwRXjxciBW0_u0rWF1DsWoPrLQPyDgKKFbLElTx912vK2z7iQVEpDZygF6ENDTHgasmvTB1gIKZeXnVQNT3QTZ5wGGAry80EDAg2ngGk1QuYHQeK5hmHy7fGAzbj0hrL33ifzsmcxXIf5N64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xtmiubv5XHKuZSw5fPSNzuD-oSJ0HnE35llTSTiiHiDVg-n7bivH_B3KJ35rZZEBxlwk8t-m2Te1uBwrVqXbpc9-xDzR2ps9A_G0-BnoX5Ch09zSANaEa6e8wjQb_1XXOa00X6HPEUKKIha7iH8C5R1xnz8HCkwB9iOnlw203wewjlgE2LBZAEWkHxqYO19toproEjwD3HoGSnjDwm0ieYrTiar-8BlMKpP6pyAxct2ZvtEdGipFmGCxga-38Fj42eAywnl9RRVzHeJ2P93-mD6qzDdTY2a77FKdE9NbdoBj3ll3qBS-DxnUNZe3LjjQ8pj6OP3JwyqkIntlEezD8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vheqp6KWLro8-AylXXURcD9WrCA48NzwVqqb9FCB5c_vmRuTtTwdYz0_sm8dLCL64DI3XYqpG_82jqljk_1H-wBFaizkPP9D2HEo8L_WSqRx6f2rjI2k7_3r2SksQfHv_1j8tDVLQK2lTtbUOPSCk6VosbFC9keNj4I2-7ymaq9E-8yP_aNZj8Ds4fi-d7DlBQFt-AB4ifXHEoxA10yu8LKKnJhg68WlKm4zh3RV6CrbRFx7OOZP6BE_fQ-SKlsbnhupclXSIKAtmv21Gm9P_zazd0876LeiMmBxtaVzFmYCf45SBGQmagbi1kjdrCTk_JM8Itv8t1pUnsAB14f5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Klp1ji2vHBw1Z9MkghTQ7KcxCaPgKoURvYdvA5LAwvNhVxE3h-NMpX40_7FKI_25HlK3qH4OlZscgGcxNFt99VIym3Mqxu2vt_FYi23E00EMJiMcZ7z05LJubE3fut8DbAIwqEYSfJR0sWSSunxzPffvKM1_PTf5Og75wfV9sG-KFscbm1eSbqI-Vd9V9c6fu5okrNv7OU7Rk75qGFRUW9EO0_iMZO-o1oY9ojzBEuQS9p8Ihdpw0rVeVHNad97aiqpRXhzoJW1QDS-nfbUHVPk03cO3VwnPWZ66F8bdS7djQO9k9C3z9OnsinByLn6rrXI6YCArIvzsq-KFFT82lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450974" target="_blank">📅 01:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450973">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f62fe2e92.mp4?token=vpIs2_OAjmjUo2S2NMo6djpgpxWEDyHRm48tGa14rFIKJjlHOzNaEOr8VO_cdhyehU0tEKDa6KPr_lh4n-L3rXh_xX9MRrRotIo6xh1IeaWJ6nkjt3fezuNRs9mIs7hrVlBmcb9elswvZKOFFWyXEh6siRZUqrHwvNazb_cg5MwlWcnkc2_HrdyTnZ4lrXRcRo6pGmRtTz-CXmZZwlW8eaP8VxEp4eDNWs_M6ytuh6-8dNn7ujk6nggTq27CamyNbhm9Du3OHa4G2FaN7gOM1G57DOg6t5jybeKUnKzEi041acP0oZScgbYlvNlOTswzyRa2gMROVUBJBWk39yxu8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f62fe2e92.mp4?token=vpIs2_OAjmjUo2S2NMo6djpgpxWEDyHRm48tGa14rFIKJjlHOzNaEOr8VO_cdhyehU0tEKDa6KPr_lh4n-L3rXh_xX9MRrRotIo6xh1IeaWJ6nkjt3fezuNRs9mIs7hrVlBmcb9elswvZKOFFWyXEh6siRZUqrHwvNazb_cg5MwlWcnkc2_HrdyTnZ4lrXRcRo6pGmRtTz-CXmZZwlW8eaP8VxEp4eDNWs_M6ytuh6-8dNn7ujk6nggTq27CamyNbhm9Du3OHa4G2FaN7gOM1G57DOg6t5jybeKUnKzEi041acP0oZScgbYlvNlOTswzyRa2gMROVUBJBWk39yxu8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انگلیس در دقیقهٔ ۳ به فرانسه گل زد
⚽️
انگلیس ۱ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/450973" target="_blank">📅 00:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450972">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMDXUOn-xlEb-xrCzwaJeI_xVF3mpfZgV8E87gvSS9owQmaWJmDZ_aqsGFdYlD15fFsliA_IMFlQ8Tpb6-XuBHGWR9Iky--PMiv9JqyND8I-0RTxF3sZawvhVrj87rvZNv2FW_fHZlkTIIK5vXFzzGrJA35EsFwQ906Yt-fTD22kpKSHZQrHQjZKMGQJvTxj9iUL5cwaxluH12hro9VeCRbX1X-nVfjmHiGy6fPSVI0fWEsAzuBQbXNW2IxnAwdSyYR_U9S91k9J8NsPWL1-p7OJlc98H_mw9LDhrbm-tSIKKYnWChP76c4kNUW2MxLswEviC4dXafBWVB0KCucLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۳.۷ ریشتری سرگز در استان هرمزگان را لرزاند
🔹
ساعت ۳۰ دقیقۀ بامداد یکشنبه، زمین‌لرزه‌ای به بزرگی ۳.۷ ریشتر حوالی سرگز در استان هرمزگان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/450972" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450971">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎥
الیوم یوم‌الانتقام
🔹
فریاد خون‌خواهی مردم بندر دیر در صدوچهلمین شب میدان‌داری خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/450971" target="_blank">📅 00:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450970">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1a55d0ee.mp4?token=nJpWm95tWVSh1OmDJvOy8nX8cNZDQ2DoE9UoI8Uh0M7JpmLV8ObMYQw0ziTW0NziY-GTM16cym0CnXHby9y5CMx-T1mqyAgZT82iVtIox3ZskRlW9ecmhBiy6f4nsGAD1rNJ0xaR3hmTxptEI4k61ODpYxbnqKqzJnNcFbY-DF5DTxxAJpmNx3cgx00zMfyHX6i2eJ50mYl7qjR0OszYOL8F22ESUEfrgpuF6hj1iHzidev8UFrQQzCAr4y1rjdd-Bi6tZJ9eGPQnN0ZUKz3GTWmYdx5ZFihYp1atp1SGw5orhuINvRyrobpQS2JERqvW0Y9tmQPYu7E4Bz2ysXlRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1a55d0ee.mp4?token=nJpWm95tWVSh1OmDJvOy8nX8cNZDQ2DoE9UoI8Uh0M7JpmLV8ObMYQw0ziTW0NziY-GTM16cym0CnXHby9y5CMx-T1mqyAgZT82iVtIox3ZskRlW9ecmhBiy6f4nsGAD1rNJ0xaR3hmTxptEI4k61ODpYxbnqKqzJnNcFbY-DF5DTxxAJpmNx3cgx00zMfyHX6i2eJ50mYl7qjR0OszYOL8F22ESUEfrgpuF6hj1iHzidev8UFrQQzCAr4y1rjdd-Bi6tZJ9eGPQnN0ZUKz3GTWmYdx5ZFihYp1atp1SGw5orhuINvRyrobpQS2JERqvW0Y9tmQPYu7E4Bz2ysXlRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انگلیس در دقیقهٔ ۳ به فرانسه گل زد
⚽️
انگلیس ۱ - ۰ فرانسه
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/450970" target="_blank">📅 00:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450968">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiVVGtboj2yV-sgjjIwKwfKaJkKvC7AMKfTW1-k8_jqifwmK34PRTTLxYugwWVrL_mngQeMj38Gbv-1uOdJe8DcBFA3dg2ZWXRqFaehp6Cg5Q0ywA8-DmJKWTd8pux3vPRXaUvGsRGO6x38tjmiCRgNCavvcVn_tUvtrZKMVayo-_89UbLURayl8WMR2zYSOL3B5Vf4KM8AjR2If7r-nTkGpy_M0tmnVC9SDuJlltWZYHdvVZkwa3qWlGA7DSvGj35BXuVPYYp9gCQoG78-v5GPrKf_Y16UGcDk81I84db1XF1M5DTkw2-EcFz6ugi7_AJ2nsbTjkdDQAz9yUIzp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه به شریان نفتی جایگزینِ هرمز در عربستان
🔹
در حالی که عربستان برای فرار از بحران تنگۀ هرمز، صادرات نفت خود را به بندر ینبع در دریای سرخ هدایت کرده بود، گزارش‌های غیررسمی از خسارت به تأسیسات نفتی این منطقه حکایت دارد.
🔹
هرچند ایران یا یمن یا طرف دیگری مسئولیت این حملات را رسماً تأیید نکرده و مقامات سعودی نیز جزئیات روشنی دربارۀ ماهیت حادثه ارائه نداده‌اند، اما منابع غیررسمی از خسارت به تأسیسات نفتی در این منطقه سخن می‌گویند که می‌تواند زنجیرۀ صادرات نفت این کشور را با اختلال مواجه سازد.
🔹
بنا به تایید تحلیلگران هرگونه خسارت به تأسیسات ینبع که اکنون به‌عنوان شریان اصلی صادرات نفت عربستان عمل می‌کند، می‌تواند قیمت‌ها را بیش از پیش افزایش دهد و ثبات بازار جهانی انرژی را با چالش جدی مواجه کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/450968" target="_blank">📅 00:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450967">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌
🔴
نیویورک‌تایمز: حملات چند روز اخیر ایران به پایگاه‌ آمریکا در اردن باعث مجروح‌شدن ده‌ها نظامی آمریکایی و آسیب‌دیدن تعدادی از بالگردها شده است. @Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/450967" target="_blank">📅 00:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450966">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‌ وال‌استریت‌ژورنال: مقامات آمریکایی می‌گویند ایران خود را با سیستم‌های دفاعی آمریکا وفق داده و موشک‌هایی را شلیک می‌کند که با سرعت بسیار بالا حرکت می‌کنند و هنگام شیرجه به سمت زمین، قابلیت مانور دارند. @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/450966" target="_blank">📅 00:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450965">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
پنجرهٔ متفاوتی به تشییع باشکوه پیکر رهبر شهید انقلاب بر دستان مردم عراق در کربلا
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/450965" target="_blank">📅 23:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450964">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آغاز دور جدید عملیات روانی دشمن با ۳ محور هم‌زمان
🔸
ارزیابی دستگاه‌های اطلاعاتی حکایت از هم‌زمانی ۳ جریان در روزهای اخیر دارد: تشدید القای فشار اقتصادی، تحرک رسانه‌ای هماهنگ برخی سلبریتی‌ها و افزایش مواضع انتقادی چهره‌های سیاسی.
🔹
آنچه ناظران را نگران کرده، شباهت توالی این رویدادها با روزهای منتهی به وقایع ۱۸ و ۱۹ دی‌ماه ۱۴۰۴ است؛ الگویی که در آن زمان نیز به اغتشاشات انجامید.
🔹
در این میان، آنچه بیش از پیش قابل تأمل است، هماهنگی زمانی و محتوایی این سه محور با یکدیگر و با تحولات میدانی منطقه است؛ هماهنگی که به‌سادگی نمی‌توان آن را برآیند طبیعی فضای نارضایتی دانست.
🔹
تجربهٔ گذشته نشان داده که شبکه‌های معاند و سرویس‌های اطلاعاتی بیگانه، همواره با طراحی سناریوهای چندوجهی، از بسترهای معیشتی و مطالبات به‌حق مردم برای پیشبرد اهداف تخریبی خود بهره‌برداری کرده‌اند.
🔹
بازخوانی وقایع دی‌ماه ۱۴۰۴ نیز مؤید آن است که آنچه در نگاه نخست، اعتراضات خودجوش به‌نظر می‌رسید، در پشت‌صحنه از هدایت و پشتیبانی فرامرزی برخوردار بود.
🔹
شباهت‌های ساختاری این روزها با آن مقطع، ضرورت هوشیاری مضاعف را پیش‌روی نهادهای امنیتی و افکار عمومی قرار می‌دهد تا اجازهٔ تکرار سناریوی تلخ گذشته داده نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/450964" target="_blank">📅 23:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450963">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📷
نمایی دیگر از حملهٔ موشکی دیشب ایران به پایگاه آمریکا در اردن  @Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/450963" target="_blank">📅 23:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450962">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPpRPJM6nZVc5_AUVeIIk4gFllQHfU0yYKutcbBeEc1f-4ABlVvUkRmmmcq5My6lutAP5JsL-6upL_J9RNu698cDFkF2iMLKGQ1Lm_B8xUDDCI9xIuOgP3vOvlLmHfK_LSGtKzRblAUlI8krhtenrDgqBluiVzu6tfizk1TIuLDR1LL1ahfC6EM5xoC63gZHTEXkkOXVPUG4oI0d-KZsIn1see-xAcUxLIHYiWU82Lbad-MR276-lxjtfFaCaMJrwKs0ioNGNSGfXLN4F5YGjMAldFWY2s-683E7kNzJFJ4H64fkiBhXHKqjd6N5rB4zkUrfn7QT1UDcKVEck7IpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از حملات سنگین موشکی ایران به پایگاه هوایی آمریکا در اردن  @Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/450962" target="_blank">📅 23:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450961">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
هشدار یک مقام امنیتی در گفت‌وگو با فارس: در صورت حمله آمریکا به زیرساخت‌های ایران، فرودگاه‌ها و بنادر امارات باید فوراً تخلیه شوند
🔹
یک مقام آگاه در نیروهای مسلح در گفت‌وگو با خبرگزاری فارس ضمن هشدار نسبت به پیامدهای هرگونه اقدام نظامی آمریکا علیه ایران…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/450961" target="_blank">📅 23:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450960">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgUe_fIfevEXpYDhsLNutS2p9cmOX1Vf9BV6WeWUmKZUwbcO21fGRikzCznYnSAQFsbP3yScll5ldb-4Ucl7XUhwu8eC91zWHXNDqj0SfS4yXzMo09myzwlKVgLTaLrRbsq28D4rpniTNXlc_kAficUyRHBbQuVcXV_6iPoXwi925n8waUQHF_dcBxSrY4En_5ElWHTBY2VzThZkzElp1DbKXQANyJ13gj_PVjj9MChpu7SDrDkSOczIesYQ-fh24G73IsNl3jT8hksG6n3fv5F1Qa3t_z45ptNxez6SxfLggAATkOqjw-6LWfyzESTIut_t3yJZ1vJO4DkNPzRNrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: مردم مؤمن عراق در استقبال از قائد عظیم‌الشّأن شهید حماسه‌ای عظیم و پرمعنا آفریدند
🔹
به محضر شریف مراجع عظام، علمای معزّز و اساتید و فضلای حوزات علمیّه و دانشگاه‌ها، اندیشمندان و نخبگان گرانقدر، اُمرا و سران قبائل و شیوخ عشایر و سران طوائف و مردم…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/450960" target="_blank">📅 23:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450959">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_XNZvFbm8YiB3SQ7leq1cAp_H-N3OdcB3zPaCYaddLEqSq__Hlo_J8-c9a0RvmXp6-4VuWPwcBVQ63uF14JriWNmyKWcuOnfpSKRoj7V2EDnd7YVuP7qrfeLTljIEeW52_qvZpeX1VuJ7a93_zfAID939XBOIcrQyPkKi7wauoZ4F0iHlXT1T7Z11sUK3aIBP7c2O1O-xZFvnNWvC4ppy_MnhV8Zi_HIomjVcIb5WA5OP311ukSvdhSxt1aSDNO-WHvHkpiKFP9xPdqBbePagnFbY7sQAVEzFohih42htV6xYC1b8DNlnZib2ujavZQuItpdrm0wXyHsSt37Xjumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر معظم انقلاب: تشییع میلیونی و بی‌نظیر علمدار مقاومت، فصل جدید تغییر معادلات مستکبران را رقم زد
🔹
بی‌تردید سران استکبار با دلهایی هراسان، تصاویر صحنه‌های باشکوه این اجتماع عظیم در عراق را مشاهده کردند و دیدند که چگونه سرمایه‌گذاریهای کلانی که برای تخریب…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/450959" target="_blank">📅 23:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450958">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrAZZQ952VgU2fcVHAuLj3h9zVZt2h1w3uFdCamWsS0RABQ2JRhlZHwfEUoEzDxI5LXQfS1QnmRVvXW6gmNXUne-oSTUl6T8fLZJQmxJgEoHyxYsouiHlfazgz71-713ZbgYGdebLTdcqPmPshM1gkcvdtIzLFBlwJqd0zLkMkV75JqhRiEPBFy4vn3S4dPR4qnybIR4eYpWSWqUcM_pa28-aZV7irsgkX_-A8He8X6v503OpnwUcTOqZk-fThYyxlIVDXjorw5-c9glTDVBWTXowyXxdR7gz2goO7EbPFBztH03PcsBhIbu0pTNTsbMWpBYUVrG8NajZfYvC-5oDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام قدردانی رهبر انقلاب اسلامی از ملت عراق به‌پاس حماسه تشییع امام مجاهد شهید منتشر خواهد شد.   @Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/450958" target="_blank">📅 23:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450957">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-text">🔰
#یادداشت
| هرچه فریاد دارید، بر سر آمریکا بکشید
📝
تبیین مضامین و نکات مهم پیام راهبردی رهبر معظم انقلاب
🔸
پیام امروز رهبر معظم انقلاب در شرایطی صادر شد که ملت ایران هنوز در فضای حماسه‌آفرین
#تشییع_میلیونی
امام شهید قرار دارد و از سوی دیگر، بار دیگر با نقض تفاهم‌نامه امضاشده میان رؤسای جمهور ایران و آمریکا از سوی ایالات متحده مواجه شده است؛ نقض تعهدی که با اجرای دوباره محاصره دریایی، تجاوز به خاک ایران و حمله به مراکز غیرنظامی از جمله بیمارستان کودکان سرطانی و زیرساخت‌های حیاتی کشور همراه بود. در چنین فضایی،
#پیام
رهبر معظم انقلاب صرفاً واکنشی به یک رخداد سیاسی نیست، بلکه ترسیم‌کننده نقشه راه ملت ایران و مسئولان برای عبور از این مقطع حساس است. این پیام را می‌توان در دو محور اصلی خلاصه کرد: حفظ انسجام داخلی و
#ایستادگی
قاطع در برابر دشمن متجاوز.
* حفظ وحدت، وظیفه همگانی
🔹
نخستین و مهم‌ترین محور پیام، تأکید بر حفظ وحدت کلمه و
#اتحاد_مقدس
ملت ایران است. رهبر معظم انقلاب، صیانت از انسجام ملی را مهم‌ترین سرمایه کشور در این مقطع دانسته و آن را مسئولیتی همگانی معرفی کردند:
«صیانت از
#وحدت
و پرهیز از تفرقه و تنازع، اختلافات سیاسی و برجسته کردن تفاوت‌های اجتماعی وظیفه‌ی همگانی است» ۱۴۰۵/۰۴/۲۶
🔸
این تعبیر نشان می‌دهد که وحدت، صرفاً یک توصیه اخلاقی یا سیاسی نیست؛ بلکه یک
#ضرورت
راهبردی برای حفظ عزت، امنیت و استقلال ایران است. تجربه روزهای اخیر نیز این واقعیت را به‌خوبی آشکار کرد. حضور تاریخی و میلیونی مردم شریف ایران در تشییع امام شهید، جلوه‌ای از همین
#سرمایه_اجتماعی
بود که نشان داد ملت ایران در بزنگاه‌های تاریخی، اختلافات را کنار گذاشته و حول منافع ملی و آرمان‌های مشترک به میدان می‌آید.
🔹
رهبر معظم انقلاب در ادامه، نخستین لازمه حفظ این وحدت را
#اعتماد
به مسئولان دلسوز و حضور آگاهانه و فعال مردم در صحنه دانستند:
«ملّت عزیز، با تداوم بر اعتماد به مسئولان دلسوز در هر سه قوّه، همچنان برای تضمین صیانت از منافع ایران اسلامی،
#هوشیار
و فعّال در میدان خواهد بود.» ۱۴۰۵/۰۴/۲۶
🔸
در کنار این توصیه، پیام به یک مرزبندی مهم نیز اشاره می‌کند؛ مرز میان
#نقد
مسئولانه و تخریب وحدت ملی. رهبر معظم انقلاب ضمن ارزشمند دانستن نقد، نسبت به دو آفت بزرگ هشدار می‌دهند:
«باید [منتقدین] مراقب باشند تا این رویکرد، اوّلاً ظلمی را بر بی‌گناهی روا ندارد که آن خود منشأ محرومیّت از برکات و عنایات می‌گردد؛ و ثانیاً موجب شکست در وحدت و
#انسجام_اجتماعی
نگردد... دشمن نباید هیچ علامت ضعفی و از جمله این ضعف را از ما دریافت کند.» ۱۴۰۵/۰۴/۲۶
* درس فراموش‌نشدنی برای متجاوز
🔹
دومین محور پیام، ناظر به تجربه دوباره
#عهدشکنی
آمریکاست؛ تجربه‌ای که به تعبیر رهبر معظم انقلاب، بار دیگر نشان داد امضای رئیس‌جمهور آمریکا هیچ اعتبار و ارزشی ندارد و ذات آمریکا همچنان بر پایه زورگویی،
#وحشی‌گری
و فریب استوار است:
«امروز شیطان بزرگ بار دیگر چهره‌ی واقعی و بدون نقاب خود را آشکار کرده تا این تجربه‌ی تاریک از جنایت و بدعهدی، سند محکم دیگری بر
#دروغگویی
، غیرمنطقی و غیر قابل اعتماد و پلید بودن آمریکا باشد.» ۱۴۰۵/۰۴/۲۶
🔸
اما پیام در این نقطه متوقف نمی‌شود. در کنار افشای ماهیت
#دشمن
، راهبرد مقابله با او نیز ترسیم می‌شود؛ راهبردی که بر تحمیل هزینه به متجاوز و تبدیل تجاوز به شکستی پرهزینه برای آمریکا استوار است. رهبر معظم انقلاب تأکید می‌کنند:
«ملّت عزیز ایران و جبهه‌ی مقاومت،
#درس‌های_فراموش‌نشدنی
برای او دارد که رشادت‌های رزمندگان اسلام و غیرت مردمان شجاع خطّه‌ی جنوب در این روز‌ها نمونه‌هایی از آن را نشان داده است.» ۱۴۰۵/۰۴/۲۶
* فریاد واحد ملت ایران
🔹
این پیام، در امتداد همان واقعیتی است که امروز در
#میدان
دیده می‌شود؛ از یک سو، ملت ایران با حضور میلیونی خود، انسجام و ایستادگی را به نمایش گذاشت و از سوی دیگر، فرزندان ملت ایران در نیروهای مسلح با وارد کردن
#ضربات_سخت
به پایگاه‌های دشمن، نشان داده‌اند که تجاوز بی‌پاسخ نخواهد ماند. از همین رو، روح حاکم بر این پیام جمع میان وحدت در داخل و اقتدار در برابر دشمن است؛ پرهیز از تفرقه در درون و افزایش هزینه‌های تجاوز در بیرون.
🔸
در حقیقت، پیام امروز رهبر معظم انقلاب را می‌توان بازتولید همان
#منطق_تاریخی
امام خمینی(ره) دانست؛ منطقی که در برابر دشمن متجاوز، جامعه را به اتحاد، حضور هوشمندانه و مقاومت فرا می‌خواند و اجازه نمی‌دهد اختلافات داخلی، سپر دفاعی ملت را تضعیف کند. خلاصه این پیام در یک جمله تاریخی
#امام_خمینی
(ره) متبلور شده است:
«هرچه فریاد دارید، بر سر آمریکا بکشید.»
@rahbari_plus</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/450957" target="_blank">📅 23:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450956">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678ff98030.mp4?token=AuyRBFs84sFDzdbf_K374YYZ33d92d6FSBlJvG04OlNvzBKvICF5NAiPuGl1iSVhrizwT7CKOj18TfZe6ZnL8lTv38l-Mb6r0lu7Rrj2C6PdHhQry8yyKor-KSMR2VGkiENv9Zw-KrwaXrlZZVskRAXlFb2qyi2EwBZt1CwWmbgawfLLLi-uy21Xsny53tf-dU0xLTBLxMOXEU-qfIYhcpys-393rbfOwS32aeUYG-mbifi9H_fs8WMmwW5bSIaLBROeyWrRdJ317EaT_G5p5NchvLULf6FbtKpYrkykwtMKUEkIXkdTGQhUFHxw_4l0P_ON18pzudyaGG75TeFsjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678ff98030.mp4?token=AuyRBFs84sFDzdbf_K374YYZ33d92d6FSBlJvG04OlNvzBKvICF5NAiPuGl1iSVhrizwT7CKOj18TfZe6ZnL8lTv38l-Mb6r0lu7Rrj2C6PdHhQry8yyKor-KSMR2VGkiENv9Zw-KrwaXrlZZVskRAXlFb2qyi2EwBZt1CwWmbgawfLLLi-uy21Xsny53tf-dU0xLTBLxMOXEU-qfIYhcpys-393rbfOwS32aeUYG-mbifi9H_fs8WMmwW5bSIaLBROeyWrRdJ317EaT_G5p5NchvLULf6FbtKpYrkykwtMKUEkIXkdTGQhUFHxw_4l0P_ON18pzudyaGG75TeFsjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری که گفته می‌شود مربوط به شلیک موشک‌های بالستیک اتکمز توسط نیروهای آمریکایی از کویت به‌سمت ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/450956" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
