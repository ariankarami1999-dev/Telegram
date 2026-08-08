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
<img src="https://cdn1.telesco.pe/file/SJtBdOZ_5JwiOEHEncUZTdr0om3C76KbxobJUVlzEJRCU0xkSMMKMagHQ1VV0FfT-g8QEC_tjgEVm-iYkVfBe2Md7ek6Gg3jC6_HYrEnFNekxz8PPwTbbA4o7fXYyf6TUx9_phHrDE3de6IJPXGoXvyDOh7BuDiqIcLf7yh6MSYAip_SpnVCI0h8FnB7QIshhug7UiUWEizcYzMd2qtvN0SaAydUB-Agi9UPD8_JlCmljqhSfOsN3NpJF5su4I7ZcPBNfpBho0XIc6fsr9aRo-MLABwK0Ra8qQVMLPGFXsksDlAP0CNfMwmNEUC8wtMvHs2e4Y_Qhdjh9sqzdqE2_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 15:21:45</div>
<hr>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QPFFHvwCD7UR2iAU5TbY2lBl2a--m5kRw0Z-69lzr8R_YxjcWe1U5_F_ZGjBZqP2pPOl7I08oM8sGqvC9GSBIwTaCcRsl6m0VtAc5FKKLPTCUkCKO2Buty-i-ZwQ7EsVRJYWLscaEKRP8XPV9XTbApFf-NW57PMDEzeLAnr8gf3SH8RiJMfuq3Bz93pMTaKwlErpMC8u1OogJsupWtUUyTAZ6brbuLMg3t-RPMG818WiM0tiEx8-XaYra_r7Zx97GQf8lUYcc7_qxlFvhLdOODY-2UI8sgIeUbww7i_9zhqplSl7_knCc0o32TYxsAH2jPEbBUH2YXq1EySDhaAc8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OJ6yDeYFfV4ws4AezgxzQ0MlVvZ2kHRTeIof4gzEtC5IgVEwh_lQswotJvsXgYCiYpbUszcb3qXq2CoJ76t2l4XZlbzZEozQJIwZY7KAYhkC6liklFdkVEWf14pcmC_YSE9wt6YZJXJouLG5MyO3sx2JCb_Flvf-zuzoU0C_xLogZHFxUi0vqtBJnLLy9GHQuPQoFMrDIO1ZHL3i35G_6tU-ABDvFGL3ty36HJB2heSDmcIM--wa5XirW-aEmN6MSy2Zhhc4Lld4c4N8pFTcIGKvh_ymYkwnBxbo38KirnlULsDBNFK6nJoM1JH9xjPb5aOHRMIVcC9-Nwuv6UP9QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oJ5CDRROo0HZ-TvfGVFAFNgZ7NunVeBCTFsuC0hVJQj-Ch-w4ovHgm9jQNX105cmLSbNXfurnwnOxHoW6__TPBJ7tOWWukbF-sOH9E02b8hTeW6FDVN7hGJjHszJyt_6wjjhXstplSYeE04btXB48GKzKUQMtuVPIdPCbIODNFUgPqFL-gEIH8tic0EgsolEy_dAUW1F8HF4Sr2uKqEapgddFy1GTEeokfWQqhZr0QoTaqQPBZv2jESiGuFRLcRtBUKRJFQTskB4JrbEeNGicIu8FhgU36_ov-DTEA1huMGbrrh6ypxygK0EluczzS--qwmkSOR0oQdUQtpb_G5k6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دسترسی رایگان 14 روزه به تمام مدل های zed code
ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده!
​مراحل دریافت: وارد سایت بشید تیک Free trial پلن پرو رو بزنید
zed.dev/pricing
با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
✍️
CypherDeveloper</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QWydbBoODPfECJoI1aiTGtKoZyV8iz1NVQHhqsKPm1DQqJLGr_7PSMEObC2Meo4bC68Iber8lCfh8x4M4_wmuGMOMdF_0zGpnK2lH444sO6waLpYu8uziZypiGVt9RCAdN9XhTLXkh7qUmpTspLlH7S0bZIsEEd0Tp5uPmetfX0u5XajxGeYnDsHKtsgnJ0QWzqCSQuFKh8NaIJTHWw1c0JUZF0NCGcl-0dRYc3v3A9wCSDi6EFPJtTZ0Rsr3hiPyY0lr6N-6shAXcIUsf78pbnE2W_8GQwxK17ehQo5n6ro3IaN7rf4umwaQWgvp9KxPOOlXTu7n2U6VIWfa6Vr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=ClK-wMA9sw0dQQccdSsIlZWIyFsnAGlnw_hkBgLNWFNpOjfjVcs6XztuVN-MUZc2eHg191Tl-gFdspQdj_guSwLfgGjRkjmpGuE2t2SzAMMGC57yRmbJJbS4hV3k-KTpMpTXZNirXDAx_xUzfZ-XXlN8eHqaG8nGKPaUtXuwUKmpZgyvn_Md90x5CuYkIGcmosCSr06Pr8syca-8fv8pxO8N4zWuR2syDyc9NffVxj3_psevL8ynTRweszPVdp1IbxdnV2F7PJ9UuTJVm8Qa3x8SOS4MuezKGMzg1KV2riQq0IgSMINtvct7pbIN9NsrwpwT-2YEyR88ANz37P8cRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=ClK-wMA9sw0dQQccdSsIlZWIyFsnAGlnw_hkBgLNWFNpOjfjVcs6XztuVN-MUZc2eHg191Tl-gFdspQdj_guSwLfgGjRkjmpGuE2t2SzAMMGC57yRmbJJbS4hV3k-KTpMpTXZNirXDAx_xUzfZ-XXlN8eHqaG8nGKPaUtXuwUKmpZgyvn_Md90x5CuYkIGcmosCSr06Pr8syca-8fv8pxO8N4zWuR2syDyc9NffVxj3_psevL8ynTRweszPVdp1IbxdnV2F7PJ9UuTJVm8Qa3x8SOS4MuezKGMzg1KV2riQq0IgSMINtvct7pbIN9NsrwpwT-2YEyR88ANz37P8cRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=fOX_zcHYMqZy_62OXyx97TzMyYclcaiu1l3eJFORk1QUqqBneRL9MgNuI6AQc_06Ng_T1bwo5gqmp6O6TSmSyOWymqZ6QGbQ33jR1cnL0Pab4ubEI8HlRvsmJ_8ZqPFngh1hmD4OdG6rloQN1kJ4-Ygp4IaH9HHDe8RL7eXHfOZWKnYYIgyoZlUKtwOkjhUPsqVGJScotyoZeJ8JB0gGZtAF28NDPH01tw28YkonS-XyXz_nVIGbHwsZ9-i3KPvYDHoMtGTjhD2VhqLfotMeS-ocuzdAIn29fIC8LWxHaBGilZ5fQdpiIPjs44XYQ4k0ODQBv2i2bFHbKcdC3ar9uA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=fOX_zcHYMqZy_62OXyx97TzMyYclcaiu1l3eJFORk1QUqqBneRL9MgNuI6AQc_06Ng_T1bwo5gqmp6O6TSmSyOWymqZ6QGbQ33jR1cnL0Pab4ubEI8HlRvsmJ_8ZqPFngh1hmD4OdG6rloQN1kJ4-Ygp4IaH9HHDe8RL7eXHfOZWKnYYIgyoZlUKtwOkjhUPsqVGJScotyoZeJ8JB0gGZtAF28NDPH01tw28YkonS-XyXz_nVIGbHwsZ9-i3KPvYDHoMtGTjhD2VhqLfotMeS-ocuzdAIn29fIC8LWxHaBGilZ5fQdpiIPjs44XYQ4k0ODQBv2i2bFHbKcdC3ar9uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s5YESl9vT4uP-0ZxYEp_lfSzSQuQibwytqw-0YkcUjQo7v4wxLxGbBTtDHJ2vbVsGK8YDQRcyubduW4JAOABlxYU9MyZR0G3vIO2Svinn_2PYgS5NGoa9LS-0yynkKAAwUUiFu4RJIR7vQk90MdPIven1rPuKSfBs85aV4xz_fz1znX-DhQvr6sYJmSXrrHhZGLOavOwLcOpin-3-Ve1DgzCdAi5SAera9DLMuun_rNJ2bg79S-JDxLj9kW4BZzOYrYnHZ4tr-zv7ZTDCnlU5OC8UhKDHqDJaFjD5ROZ-EEGmXm7TQF5dOpzJ84XoIBQIzEhtU4XKP6yKr80S4E3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nFoH28lsucjHG_91YlrMYjIi6AZC8gUypxKxhyVHrZu0QTvSz77FmVBBdHHlHMVcRmpIfIvbMT5yzjdJrA1Oh2DIBm5zKz4cd4N57QfzMsvvPjuzMrf00MthYeXJNPRgNdcFyp5fHwi9YKaqdO3rgkMkbMUY544jXGtjy2Xn3VttyAvP0CwmaUxwYfm2cYEgKLsHTBisjuz0YXbysfAmXcH1sJN3ro_ZOiLqx-1YLD3Lsqf-493S57kX-vAg1IAIZoZqZYrPgvlmPuunulcBQuV6btm5bWsePpt1pJcP7nNfH5trHEQq8p9zZtsy02DTEwrmUwbGfzlHKBnV0S1qXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sTs5eKJHKWCJWUD8SHA9892UWnSVgrvTgPaileiM24WE-Pp9bANbz7a4_bRfyZI-G8y7yS1HMmSXfwxdPhCF465kZs5H-1kQqrZFAMBB0UhqNu-OnkDIc_np8xFRmlQPRZImB1-lMcHFTJXw8eKCdn4hKqvhB-Md57mw5n7vMBW2bwoSvxw1BjyfR-bOyaWAXaC92nDYWrG0sHu_7PB6OHZ7dK7rLzZp9qWBzDBJ-0Mbm27qx99BQNwI86mtt9l8q8XLdperyAzWBNYQi9hqmlMu96AGck01ZGVnOLTGKHsxIgln_ASqluPSVeiS_eYhJvCa4Bcn5e_FJU6l317Vdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hunc0nu6TF3jaosSdvqL5SqfUq8t2R2IYDCoKNaHc6x0xxUzTTer10UV-ovbYneZB_XhGfMU53a7U3AIBqwIX7KDoJ-R7eixDH-OQ2jhn9zWBgiYZNHuqO_iSadG7aI3xsa-vuT6yC-rj4-J7vYj9FaBk3-OeJbjscHrWZqNYiiYCTSgAyM_3h_qPL_scyyKj0yQbjhPrtws-WGZVP5lJsCCFtcLJxicjA87hYMzZ1PsNiUejQKQapDcWQh6snjgWuA7azr3uBSqgfANMgcKihUjcdIxILllHlt_QjaPYE1sSInoLW6sJ8faRq9_LS74PPSUY3V6xEFh4tYpK0OC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ Hermes، ایجنتِ دوست‌داشتنی ما، نسخه v0.20.0 منتشر شد!
📊
این نسخه که بهش "The Herald Release" می‌گن، کلی قابلیت باحال مثل ارتباط صوتی زنده، سرچ با منبع معتبر، وب‌هووک، اتصال ایجنت به ایجنت و بهبودهای شدید پرفورمنسی داره
🩰
تغییرات و ویژگی‌های اصلی این آپدیت:
1- گفتگوی صوتی زنده (Talk to Hermes): پشتیبانی از استریم صوتی زنده با قابلیت قطع کردن حرف ایجنت (Interruption) و کلیدواژه‌ای که باهاش بیدار میشه (Wake-phrase).
🎙
2- منابع و استنادات دقیق (Cited sources): توی کارهای پژوهشی تمام ادعاها رو با منابع واقعی و مستندات و سیستم راستی‌آزمایی (Fact-check) لینک می‌کنه.
📚
3- وب‌هووک‌های خروجی (Outbound webhooks): فرستادن اطلاعات و رویدادهای چرخه‌ی حیات ایجنت به HTTP Endpoint‌های خودتون به صورت امضا شده و امن.
🔗
4- ارتباط ایجنت به ایجنت (Agent to agent): پشتیبانی از پلاگین R2A v1.0 برای شناسایی و واگذاری کارها بین ایجنت‌های مختلف.
🤖
5- سرعت به‌شدت بالاتر (Faster everywhere): سرعت لود اولین توکن (First-token) تا ۸۰٪ کاهش پیدا کرده و پرفورمنس اپ دسکتاپ به ۶۰ فریم رسیده.
⚡️
6- پلتفرم دسکتاپ: قابلیت پیش‌نمایش زنده آرتیفکت‌ها، کیت توسعه پلاگین (Plugin SDK) به همراه تسک‌بورد Kanban و پنجره دسترسی سریع به دسکتاپ اضافه شدن.
💻
7- تاییدهای هوشمند (Smart approvals): پیشنهاد تایید دستورات ترمینال بر اساس تاریخچه استفاده و قطع‌کننده هوشمند برای لوپ‌های ریجکت شدن متوالی.
🛡
8- قدرت‌نمایی در CLI: اضافه شدن ابزارهای اسکن پروژه، مهاجرت ساده و اجرای مستقیم کدهای شل.
🛠
9- هدایت بهتر ایجنت وسط اجرای کار: قابلیت اصلاح مسیر و دادن دستور به ایجنت وسط کار بدون اینکه پیشرفت قبلیش خراب بشه. نسخه‌ی قدرتمندتر Steer که داشتیمش
🧭
10- ابزارهای خودترمیم: توانایی خواندن خروجی‌های نصفه‌کاره ترمینال، تشخیص خودکار خطاها و بالا رفتن محدودیت تعداد تلاش‌ها.
🧹
11- اتصالات جدید: هماهنگی کامل با پلتفرم‌ها و مدل‌های خفن جدید مثل Buzz, GPT-5.6, Claude Opus 5, Gemini 3.1 Pro, Grok-4.5 و  Vercel AI Gateway و رفع باگ‌هایی که داشتن
12- قابلیت‌های جانبی: پسورد Vault داخلی، فشرده‌سازی خودکار سشن‌ها، لوکال عربی، فایروال و مقاوم‌سازی امنیتی روی ویندوز اضافه شدن
🌐
این دستور رو توی ترمینال بزنید، آپدیت میشه:
hermes update
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VYzZep6FD3z9Ulad2gTWhHSe3q8dpyTKoiDFyiYILx2U-4kvoCszj7ZL9K2A3sGiGUJbapFu2aovqXFQ0z_B2JajWaijCqgC9K9eise4I_zDur-wVe5GRrCuzIPnf4cz8Axf61g_Bzh0Ttdn1BfXZteunTfaxpAuSuA6EUXyd8HpD-qo547Tn_XoSaXRw4uA7Mk2KTpCEw2P-IEBsOgxlKVqVYuRVmX4guVCCe9pTqWNw-Geq3mSHm4R-Zb9cHyw8gQJSiwsQBmkPr5Ylkl5Ibo4Ynurjib8J4uuM6s5-Fmk-uvNKcjKuaqF0AXBlVKy_8xFbu6uTEr9tkkCa37BxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ntOLzbnKkAJNXUwWRJlqZt5T__NtTRBCwb8zGF1LJ1VaaBm2lJ9CZXBMcXAeCRz3z-C-nV5J7Xk5wNh9Cusywrqn1ecgpL3FMbrVkNoxxk0u-RQ4Yu5kqEmpcp9QHu869FZfrHgFCWMtiHCH5YRXi_2c_KINdsconSGh8BaUl0Hf-XEpxWnrhHltK7kCcUJoFovn776RPoE4wbtwHFc1XMLdVfIPnzIuotD8NUGay4tlMsZA24omntwbVjNa-BZ_Hvi8uzxnnDYBXFrokllhkPMTOUIlICzQGbkE9VsxMzaAnaDvuQZv7jB_WLYEl42f-Y4DvVJoUr4PM7sQhb3wgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cTj_br_38H9N_RZ2bb4SrM5vHYUvCKAz73x37FWj3C_21F4lIuD-TWqqjpwFkxheccVKloUqpyV0mdFu-0HiMVVTTX91tbuAsJfEBxZ7rKUimBKGpVhDw4XcE9_wuCqM0d4QzMvIGxgP3F9-_roqUSubie9Yx5pYdUcJIVoEC1kjg_qivoRv7nMG6mV6rwvwFN8EIJNBiR39gC23tiv9XXT5hICFF_f0d5SMcULvqC66ZWyZQltyqshUxDykD2F8RHa1nwqxIiriMfbwB2QfgdlVokiiJpzAd-EMDefw8SkXXpg2S_WvFCfCdO-RTCw0D_Lywo4iYzdjvm5DD2jj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WC5a6Vp8Wb4LxkY_r0llm1UjqrA8qwLDNB_wrZSHH6dsGdUDouLt2DzXL1DHnPtLB6xJbz7IT8-QvFIxVSYmlLAYfW7iJsV6CczqRllZuA3HYRzm42rdE2S-l_mGFARuhKITGabQtQiIA3yPGP0Gpj2cIyYsQPbhihLXEkimUTVno15xVKLv9N7gwT4wOQ5HAvSgmYGM1dl48DUEuIBvmCEBTlGLGRXQ3CJnaY83dvxYtgtuYo2CtJ-Xc01ZAmue14-h2v-ai-qE6LI3NL3u-Zc0YZCe4QM_ryOhF74o-df0XsfUrYKtxp_G79tGnAf2hROTNqtGy53f6D91CFD08w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wkhb6yyyiJ00bm4L5ReTkfV5CQCZBAj8jbAJfkNVGTcKEl1sxYH7y0waLTvfnD-nEEH8S6_ezMdoMRYzoAgB0xlFCBOcPcIVXKj5l93jN5qMttWzWrHALz8BF0GgMV6i3FBuLgSfBFk6wVXdTbOTI4g4r2M4lOl92mFCz0kRnTGVcpG4RxI-RDeGyGWJJPQ-AlOTNe3K3NzUorqvx4xfsOy9-pVPgu_Ew8LEKkv1_6i0sok3jQJfFth6OO6NG8VA7LQ0iwB8KojjdSj05hOirP1kXuOvb4RXOIUCWExQtYSo65XqcBs4mUOLoCa7muUsu9ILyZelsy1IpLKnbrtTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/isPEM6Z6Dgwjjogbvr1JzrPcEX8hFi6XOCB4sPpRtUxrQIAXeHBwj6sClufh5UuI3KDhfi_UUogqacLZXjtgRcN36m44oIhffpRO8oId_ftd-uMx-yQD3ATG0I8tkaptBWzwye2eGmq0XjJx3ow4UPzMiWTtEHYDRZFnwtlA8DkcY7d4KzcSsfNtdRzdfkKyIr8bT3OddhUwq8dtH1PToNMIXxiIp47752dSWYGdlxE5FL4DkHu8vkj2P0k38bN6L7WW3l0-1n37jEhF3kZxCvb--NXstsHTEWLI-tYS_q1Lg3spaSB_SXuxbi-GaVnrFO1scc3YSZAVtXsep08tbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JrXz9GdhvBoJpMRbozu10VLPLv0-EZyRNbGQz0UDn-IyC6UIkZItd_X53pgnBLeMOpHIrOBOyqI4n32VSFN0OtZcqvy0QP15PKqxgc7vTwsXo33yvRDZPSmOcf1YEWdmfWP-IkoLOJNonfdCqNf3gHku6_9cTNPJjbDxQb_cx0BN9Mg-jqOhijG0C5jyttwsaFbZfS0lXevmkylxBAww4DNP7uPKeuFPuTQRkt9sEVeqWSJom7Ttzy6M-cqiyiHgZaIuiNCDNE-8bWNQbSoGGE8ZTmNqmxxgjg4DDPL6IOoryApa1gpRngXIZOJua_4nWJ0zys4vBNGGNWvikpw1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R85uo0F9345kelWjNulQ_eVJ2bkqXWPwK82MbkTrxKqxBYEFpDVvAGLgwo4ifDK4uDrScRwCySdmLIWuQXK2xlOg8pIbqh2opPvYkEtU9Je0OHGMkCgoYs0gHg-OIPYM-Tn1BbGS31IXppru8tp8w-tp2fDkVuxuZGnWzbBls20EYcNdUk3ryJ6KJbZZjNZ3wRZg20svpZ0to-3L7Fk90u3jFSJBSIXhzSrID1XassUPXJmZFKerNYBUuWn_wVNtd3GiW2fS8kkRsfyds3uDNZ91Rk1TLzJEytEQo1tAyHrgVZTD1hah2VbVV5VG4a7_7wq4ariWZavxeGjEK1YSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIY7S0g2fhSo4F6tlMDiZCJLfkVF9hVVA2mLY-7GyvxMwql_a1kWKdUocarK_tRQCiRjVQAOBYqhjpxuTFuQRP-do2oQ_GM7m4CdHAp-Fp225UTRcu8E7_jqtOs-6jHJOincSPQgaWfa5WMKmEYLrGw82YA4eQMHzcbJZSev_qaDpUbfNYpHIpjWpNZuGDE_uVcu4BxbBQuFKaBnogG14xSzf0A-nLlWanzoVw9Oq9Rll86a71BY4FxapE8kw2so0TIXfEylPBsz5BefIViznWemFKwy9eX0owKUzlL9tJjYsbRKWuMEgORDyo-KEmgahg0kkPXA0YuwpO8vCnnb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gHFOCYnu-vC_NScB1rgMAr5e61ZnY9Gsi7g_1AByt0eH7NJ_22z7GR26oVBSo2OPr6v5A_P1KjyitNZ3I4sC6-EnHT1bFcWiDXOxni9LoIXFvs2kBCnsUgdGVgNM25s-ukdmS3R2asj7QamAuZ0jEL3K0l5gzTtB5bnPF7U_bzfbDFltlhQ1AU8kAxikvnt-WKbnT8p9TcbZJPlDpDh58uP80gzvyG4y33sy3CkgXaFDR1-OVUp8Cy7e4IIsEU6Fm2dwe83v4wgJDr1yQ3fmJcKFVDFOknBqyCCPXp0TUz8FjskWSdRZeq-VgeBm07WZrhGi_ZT2rZhOajrn9_0OpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pd4lGygL8BNlpUKft23TOCb5rjfGyFx6XlZyOpscrMKx2CBGFJrWPO_bQPUjtEKgJYJ621MyfDwNTGQNaQcbuICx-gwNcaRQBjzAHznqYG2a_qeQbeRgs4E-26OYZyVKSd4dKWx55WmAZA7l5M--HTvH2vn-Zx5PFXlBw7G2mHXfmWXM1JfSALs9yqlVP5E9FQqmYgj5GJdwktH-NnFSBP6m76fY83x8IbgkXtLGmsOSpRLQSTqcGHQUbLT884p_p61NXo7W5bk65ZvObR_fFPc50A4QsIOutaKHQnoZH4Nr_Teb-KU2goZYOk-zkGqi897WVDjjN4t9C0Qn6pff-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g56SzKyxHxhxNzAysP6cisKf2cJUbkMJmcsRu1vMgCACUHeI8a6dHDMeZ92bGHYBmOGl6ovCWhEZ5Fzb6qvTh6AO5jKdWSV9_rotDtd8gj2Q6oDo4P0XQeMvVKshzh6IqleG89J48h6ld105egAyQkV2ot7Hc-EWgwX_eBaR_C6SbfOXme70XrLkTfH2nLgVksoiidIWNzwpTh9d9tpPQxJoXttNIpQyV47nsdkD6LezdKQ63EFSwjAVDJ3pM3QxR3i050mJmXQljkndArREhhx7WHoSn4IdC9Fbb8elfX8YlNACaTkvHGL4F4G5UDHXiyA-BkEiD679o61d0Nt62w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cdKzgJxT57Jov7fGn8TwTmkLIM7DwLKb6UHqIvBJB0VzS5WPWDUvZzokIvC_lhAqVVBf3QPwCD7WaRvLSv0xtSfYj1QETbKUlLH0j44jGtMeSopVpnBXkVa5yNAfPGHuGwhlwwvLQ5BeGQilB_cz4CuFsQfDTGQ3-j3WM8JbSLvAeh9SSkvkKd-oSbChQl569lAG2LMBdAwUta50ULtQHdaZe1veYKnayYlPeN47oJCTVr3CYbBCs8cZClDmADDAWzaVRVgkPvNs_bbTZcJc3qZ_XLzxBR-hMIumQ62xHeCnLEo7ojPXUUqazYZDDMbA_chlJItsyyaq7DuWBM8bOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LuQ0-LqqX7BUbrC5vUBQXPYsX0Zxdo_AzjmGHqsTEyu5y8SrVhJtDM3MvydjrJ4rf0iBjGtKi0c00ppNaUtfxWG5EcNF6WWIByYEFhFOWlocjEdv9btu9sL6lwu4MnNdMkkxYgaNcUsU-hEDE7xdszun1aAZAtDo_kYAtMTSR-av-aSB7zDxVQp2Eca__fGYXHlWlgB0KIibA-1CaE_MeeJMSVakXY567ebFxaJAaxviWArTGS7R_VEmamsDBE7xJBl-MyeZLlTDho6TGpj1HHNlpNYPaKGg8W8ktI7zYQT3kSeZ6CL4igOfBePgwG2CAiBo9CGoJVoj_5ojOCRIzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n4z9uyoc3mz0AVTyZIx_GDib7sm8Z-rmf0fvfOHVGw0IJP57OcrhKscrp2mwVa6hYh6Mfao3HYW-FiKM3MsoTtoLZRTvqai5JAPfP0HGFYroBDgIdUoS7ErN4fFpKDSxqFxxu7Z8rc7KMhNJD8oBrR3ZIxMjR61_dN3XjbEc_e8kLDlQeh0NyTnFuPPQfnyX2XYr690ncXy7XDyakOBm9CJS76TIjUYFyNSsNVFjPG8XqQgcd9w-8VGy-N1yxRkukWkZfLuvdXMAjF2opwD94Qmr5dhPNHtdec1R0JFoQoIR6WUcrqHzHNMhCkqw5A5U-DK94766SsVvyXZoq3dZbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPavel Durov(Pavel Durov)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUl9k5Ck7pMvRIMw4YW54Cqsk7rqrug9Mt_7Oi3J0Slclo8qEUHDG9yLcW6blTnDGfDTYu3vZQ2Z0QoJkmnAdR7lZaYVQni9WPDb_H1QhsRjcjxqvL8aSx_4zqElG3K-yQxvv9_3ubx5lz3DJnWEkn9K4Yiw8IX0_wdZraZV0AE3nfltr9_raJ9ZLyZcWLHVdqIjGanLapdqDRfxe8UL-HBYbmnvPaOoBPb5Y4YCa3swwCMzaxSl_LHTkJAFZCGjiFFWMXtY7hui3NcgnW4WftASgHNGFWWwDw7u0ys7fEE22fUl5-Pds_lZMaJ90H_jbXZdSIy7UuVe2CMZ-vhNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
The 2026 International Olympiad in
Artificial Intelligence
starts today.
As a token of support for those who will reinvent our civilization, we'll issue
🏆
240
exclusive
Intelligence Cups
to the winners.
💵
We guarantee minimum buyback prices ($
1,000
per
Gold Cup
, etc.), but the cups' limited supply may make them worth much more on the secondary market.
Good luck, AI coders!
🍀</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGUi9X8YCHXj-Fl0OPGC9geSpAR6RRQnsCeOc76eHuadblwAF0XhVNxxezqFg5zpINf7sDE1mwwX0Ha5spmBGljjkpPGZRpLAP69qFynlOt73wNK_iJkEknaV0unQp8l_woWRTBGc8VPXfzD5-ATL8fvlB4CvyASgqOe5t8U8E6G5xWb4t5Pq2B0e-Ez9pvDOSPFaeggNhKSNJEgJCt9yhjAZVeJgDiS-Mlz1jSyFZceAZldc-ZMDkb3dCuQdf7IA5oVpnHTW4EUvKlfMlTHA1Z-gcUvNwHEAuFoqpW8cTZeAde6TJij8VTGMK-YCIlsr2oOdCFmf7JpOM43MR2hYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی گوشی VPN دارید، دیگر لازم نیست برای لپ‌تاپ هم VPN جداگانه تهیه یا تنظیم کنید.
ریپو
Relay
یک ابزاریه که با اسکن یک QR Code، اینترنت گوشی به همراه VPN فعال روی آن را به‌سرعت روی ویندوز به اشتراک می‌گذارد.
اگر زیاد بین گوشی و لپ‌تاپ جابه‌جا می‌شوید یا نمی‌خواهید روی ویندوز VPN جداگانه تنظیم کنید، این پروژه می‌تواند گزینه‌ی کاربردی‌ باشد.
https://github.com/Mahdi-mortazavi/relay
⁠
@RepoFA</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BhnMMuB8bUhwiL-gaPmq3-OtYr-_rASb5nKNAXraHW6nD4OFVgw0Vt602TmrDXg3i6o__InT8pddCzqkWvM_0SNltVDQReqGRGfqIELeH6Ch_S4zXJxytSOYgoS_fXQM6DdWKkSs0jOWvmfv1Kliuzo2DCMeoJ3N1yP3g0N7WnQ-6qZtRD282oh_oipBXkmuvONMs-QAVzSaOR__2_BgdK3jDHi3_xNiLVoBHPd7dkHksGgTCF25BQyeRHtEMeeT-Mg9pIKuQMvWGfT20Rz9-DkvYq_vfQmJbhKxeWxtf5clsJ8pXO5zifgiBzNyRfXFB5TaeuP8zcspP1IcPNTOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=An5-KCjozhL7CE3W5Kf_CrvDi5xJX9-N1ZA8vLWhHDBM3xiXCVOf75QMUu_Ig91oijdAA_6r9vR4jVpZ6u7CvqTGscdOBT3LsqWd-LsD1A8Pp5QoW1wcxupLz75TSonJGqpZwGIk_J0r9fZ1q9uA_dk_9GALOPkt8mm-jQRwOwfjnL_m22YrSrcz2Rkrw-xKNnNi6M8NcPw5vqlxhQeeRtC6Ff5srOoZFi3vNNcHwySnwzXyJmTinatuXYml1w_NfAHvKvE5sLG4aw2oFw_ZBBdSgSz_cy84jWQLLLITbj8OTOc6QdnBEOrwwtoRYFMERAJtuk3Rajq3pXfGdcjsdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=An5-KCjozhL7CE3W5Kf_CrvDi5xJX9-N1ZA8vLWhHDBM3xiXCVOf75QMUu_Ig91oijdAA_6r9vR4jVpZ6u7CvqTGscdOBT3LsqWd-LsD1A8Pp5QoW1wcxupLz75TSonJGqpZwGIk_J0r9fZ1q9uA_dk_9GALOPkt8mm-jQRwOwfjnL_m22YrSrcz2Rkrw-xKNnNi6M8NcPw5vqlxhQeeRtC6Ff5srOoZFi3vNNcHwySnwzXyJmTinatuXYml1w_NfAHvKvE5sLG4aw2oFw_ZBBdSgSz_cy84jWQLLLITbj8OTOc6QdnBEOrwwtoRYFMERAJtuk3Rajq3pXfGdcjsdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش
سا
خت کانفیگ Amnezia VPN(وارپ)
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
💡
نکته:روی تمام اپراتور ها متصله هست.
لینک ابزار(ساخت کانفیگ):
👇
https://darknessshade.github.io/Amnezia-VPN-Config/
دانلود اپلیکیشن ios
دانلود اپلیکیشن اندروید
@xsfilterrnet
👑
@ConfigWireguard
✅</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q9sooqYncPgcrMZFuvHLjDnFvSBEsRTJQXUFoFySY9yO0kjG4FaIdzf7f4Aa9uLFCd6BUmh7-wJ8fDswaWLRW2-ObS2ig_cLTY0Uovpu4Qgc_Y15_zkMgZ6cfmqYAao4DbpGLGAaDVa6I-pJCYqi-hifxYDQlz2JfmkUZfARjJReRj5SriYI-WgVGzaVvcGo-ZQUBx9vOUiOfkHaRSewcKj-QmqlvX3JRWaf_E0xXVjgPTNuOtDGMUs-UmcGsq-_Ixx0czjuBNnuQ2nw7zUsTwRs8tl5JZX0Jj2_-tyCuKmkh_Fkkqn1VKvaGv5a0a6Z5011P1ijG2ank1HGwpEeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VEOaPkXfqXXPQwBtUSBCs5i-66YqKYuZdIp3PZBiGQUTJg_VlB9j70DVuPi02EDn1FERMRqoUZTD0ti3KWRNNH9Uk2U5t1lZDSLaBdg7nRYnZiRUHpIjmKAOQxD11WeYLtkwL1vaErkAwW3K7_yjiAoy-D6natq1SXPmAwqPKV0Th3h5YSion2bmCkMFYY2PTUhMJ_jJlvT5qyJ1FWyX0T1HvLN2-38bIKnthf2MTLwReP59GPut8gVxqn6jmVb0sozDxtApOxg_3jCWxG3bSSNXaYDFJpIVrcMaxq9_lM6Ex_uXY2532nceG-s7r_S6brJwVd3Qc2uHKCbIXvpUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)
بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.
مهم‌ترین تغییرات:
🖥
یک GUI کامل دسکتاپ برای Windows، Linux و macOS
📱
اندروید از نو بازطراحی شده؛ Kotlin + Jetpack Compose + Material 3، پشتیبانی از اندروید 7 به بالا، APK جدا برای ARM64/ARM32/Universal
⚡️
دیگه لازم نیست منتظر پایان اسکن بمونید — هر وقت IP سبز کافی پیدا شد، متوقفش کنید و فقط از همون‌ها تست سرعت بگیرید!
📋
امکان کپی نتایج (همه IPهای سبز، ۲۰ تای برتر یا یک endpoint خاص) حتی وقتی اسکن هنوز در حال اجراست
🔎
اسکن همسایه (Neighbor Scan) دیگه اختیاریه و به‌صورت پیش‌فرض خاموشه
🌐
تشخیص ISP و ASN چندمرحله‌ای با چند منبع (Cloudflare، IPWhois، IPinfo، Team Cymru + دیتابیس داخلی رنج‌های ایران)
🛡
اعتبارسنجی واقعی کانفیگ‌ها با هسته Xray؛ پشتیبانی از VLESS، Trojan و VMess
📦
خروجی مستقیم به IP:Port خام، Share URL، Base64 Subscription، Sing-box JSON و Clash YAML
🧠
موتور اسکن بهتر: الگوریتم weighted-random برای رنج‌های Cloudflare، جلوگیری از IP تکراری، پشتیبانی چندپورتی، خواندن ورودی از IP/CSV/CIDR
جزئیات کامل و دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O15Fz2jZCOJtr9XL4n_-rgDrLBkNE3CAXXTLoCia5tvR6Bv9oJ0InT5qT3wF6mCzx8QbZM5ipedftCJg-iL59pJA066bQ86-PIhlIzj8w7M54szmuRrV28neyetAkeTFYyzyh3Z_fL7tgkwrfzb4vXZmAP93RjaT-8dB0HaaBXjUa7NUA6hZSYO_Gwr_RuRiOZh1cdVn_pL8Lsgu7ifjI4SYkkRbER3YnvAcPmDtrKhkMvD7hDa9bTlbELUaJBISvoPYUQUxWBqX8XZc55-AyLmkvWQbtJrZt5e1CWB1u9if5JQVTNBHa8TaRVG8oMJFllC1EjYWKhWJesiQOdJOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qk3yVf-NQlLDIuU_wEmxamgCm9GJNYjpv3eJP_xV-ryk-n_Eiwqr-eGdybtF83SKkzleWy-alsQulQ55t-a0oE3Bt-MM5D5dhZHRBGm_LZ8o9JTRakVynPs6oUPc8ldgauioCgpX4ak4j6lph3gkyZYHy6hFwT0saZfB6DydKqJh14VIorpITQOcUO1O5Rd3KpUun6EaL5O_kBROUMb4AL_7y-7h9zV4vwUzzmsII1b4G6nQn27jGn9mWEDQ8F-78EvPQ2jhfX0QDGSIH0iRFKERuDFinBbyfwqMUXrvwDFJO1CaNHuwi3rwWnBJGw7dtyc0MjULUDIY1aInbWOycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gDoyA3wanua2OSxCcCgA8Tp1J0h2JXAzRwQV2RZoXZRBAhu-E2mg0XHaFhsCacBVFXJk88W1B1t9wzMOc0vgYZA-a_dPg0aselEcB1UQQWlHMSOT6VyZpOLP71woWYcSKskZ8_OJUwKiA41IpoKprPTYca8Q44jJ_CNGJjg9MwM_9O72l7DY0ERUn49YuGoYrmqO5hn4rkYkedad2cq-D9Mf3BB3dDGQiHO1jEwpF7lfvMnOnml7jfbmKqWUdMg77vZLfmb9eQGii6DR1OfqToYkTYy5-XNGlryIBzn177D0JSXPY-Aifgb_JgOLPuLhe2UxJzhHqf-sziQpLgryVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iVnQ6dpOfe8vtPYil5LZ-wBqXnPkWN8XkexJS-KlTqJbfyWmGkweItMR45SdoqugRUZ42eeQtf2x08whnEbq09lG3DUTnps7KZGOKEw4oRg4KBFfEON0DKpcGErYrLUkFCHQwryGCC7Q6AIAkxfvaOwJSga2uA59kuya8h3e-MBsOWxBXSlSvG7fTOjGi8-Dtr7ZhYApipxa0u_cuaZOnikAxCCm_tijI8hD-uIPaNOUbXO0e_EhZhG4dbfJ9tl5MAzSwZmKkzal5jNudHfV4KkPLN2wb3DsBhOL200cUKLPioEpymEhLPUzfQ-gTuW24DuIMLpA3LwHLuilReAuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DVjOwNdeGPMWhaV8dmqp3aeJZGxmcZ-9Sm5t1z083UzoEUDAwrV_GqwxKtK1RDjT6orF8rr-1QGDUbbogeKMtpWaFKllRFCQY0WYL_DROi856o3cyTkCI_ULw7HeX3GnRbS_23YVz4ELH_-b7TZxTHL4ATeQia3HU5B0XeI0-IdPs1tpAm173hOHFcQ0ZTkOwcBE-0lnhzqU9Iw0Yh99kuHnDmirerAoB9i5Fmj0XOosOJRKImqk10gQdMoYBkUCkE0jw1oDK9fSZ-KV8xkZ6dxEgWoNOEyeGIf2CfUkg2lqALjknqIvDhvCRzy72H8WF2-Tj2Gs5naTw6e0tEOE9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون
اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه.
همینطور قابلیت ip fronting هم داره
و سرعتش عالیه(حداکثر سرعتی که اینترنتم میده)
دم بچه‌های WhiteDNS گرم واقعا
❤️
🔥</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U175-pHqQ-tWqmD25yYZ32Uv3RqHS8CNugquez6ff-lAjubyrgx61gWTj3mmEVo3xys8LHwf1axYdkwSHE-0hO25P_GSzD28SEQokcHWSTQhB8vuZWQku8ROzXIhlvaOB4XwUiqIQ4saC7W_ltRJsFiPwtngCSs9V5X9q5iSFTJj21CnYZdp_toz0oBdff46ARzC9ARkoS97hwgkd6Wd7UMShNwd2oD74FZewkLXXh0d1PaByFZlDznidfrmgxRQSUPJmmWnQ_fh838QYneQu5FW7avVBed1tO486FbsGdmgTGEi7g4G6xM30_J8dlHt7TFgNuptdtqqZsv3CF8R_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JvLnZtlHZVfVEXPqBoTyzEY0AE5gKFgdH3hd_B2VlyH1gdFcon4mhzjzPjpjy8E-4HYulf4opuitYyTZr0uGNbdqIAx5GkSfpc8W7xN_LdsuaeYVlRJcIO3HfQyDO9ONvsmXH-Q9NFn8QWViHP4dUvF8emDw2XeEN2pBHMQZ0rTYhXiufaOGpZyn5wdc27_gTkR-M1YAMUNFSdHCUBHdaT6S83gkY4-UJN3BN0sjWQiKsVfYEia83Jps13q2sRuPynUgrg_dMUlRxIPYKdoP2NX_y-i1vUGlxOAQ0YmZDBqJbQnxb8kfMFpR7jBkCmmWyuHBT0hlMPOYzult2k3cWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kf7njQFJOQJrGj4Q_EyQzELoofWtW2JrWP9ggZ2ciUV7NaOosLsjzR4gywuQ-Srt67D-jaHQv3UyIRcDwqh23lZE6uCTuD_9i5JntepUG64h-ntn268OiSV_cMQeu4liutMsYa0BELBFBl-CL36klJs4y1QtgQdUtC2yr89iJa138OOGZIZZzRTwhcafQ0Syx8yO0g8OchLfDjCHoxqff76TzuJzYfh_DJcUxOB4SEB2V-WkzBIV4YNy4Noyu7CRNGFF-pNGN2blApwzuDK53SRyo3kRuvQmoVD_YDsZZF0eeN1bZbkvrNjd8AQfvTAs9VgHK1Vw4QBESnbwYEeRTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KawyVjnTkcaQy9kAq0HJMrufCQD1J7dS9Kfp3EvngjeDpD4eQFeMLUa0HNr5l0MxgLPZAq3cI8o3t_3MxvbliJ9rprlydpc8R7vAlq4W4YiM_Z6kndmlAVXNhBTz81N8csnwd1FDgVw0qHGQ-JoYfI8RSy8jlejJPBNwGzjsCB8RTKE26b_jpMLCVvQ9wmy2HxUKNaNuVPE1SmH64Vq9Ox3qTxyPSicABei6YtVWxK2Ni8V7luiLrWlXjNDmV7ostqYctGMIR30Mf5GcQk9v2VGtRrqhZQ1bEqZE7tZzqtiPlLIH7Gnnp96JhRymliwL_I4lDQtqqEDAax8OOEZ3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Puazo5zrArV6mqBkEImh5Llm3dvNjm9EX3XIConPArqkRl7BaUcG6U0BXS2E2IJmdZxUHPlZ_I3qKWVvZHVb49lbhz8WlnNHan1kGZgLfVUyNmk80Of9rptEc3OOiU4B8kZ2iBM3i0doFb1Yopxt-mIE0i4v3B0CwElZd2mU0mtft4kaRYxl0caAQHAsXz0s11UvI67ZBC3l5qwBMndAx-3wFEtqtIKu5yI-RkVu2MRksA6zq5yS6sP3ubj9183fUFXqxp_uq2StXvaTXNfR8fLZ-BBYT2FHjRU2j6b1p1eWVJ48ZpLFOp_4aGHIurc_jCUITilznI7fmVIDpOKxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVBAd2Ewrw0cm6Uh4iV-6geHJ-Af6zVzJTg0_RKaIXKvxXYJW3K2StW0_YWj19QmimbWd3EE_rn1qrthu48uxn0A4yhLbkKBMLAgn_OSPvb1T3pNgmLLqqFbLvjfzJuhvreqdvK5-xhwVdHaon-ndlJx-3QTrVxnuHWQ-aQ3IcUCnW5qegATsLbhLi9M12yCczRj0zE-XnZC0XSC3TCnPADTkEe_Iraue3uuzeausXMq4RDAUvt0uAFe3UpmqZkcnunVfyjg6Nz2IwRCl82kTaYBS_5Eqjds1HEEuZjp3hqEyNGSjBCE-mKvfQu1yf1ogI0-HPXyPtH2belfANqViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DKL5nY5gwxMNrDBFQOHVMgR1iOoUOLHbMfgBxt3AVXzI6DLDgxvx1Tz5LXZzjbdkLsZEdt9DAor2IvvR9R9aEjVqujmllfGnQa1pcPEMMEka0r1ecC9CkGlFEVBfCxF4Ns09G6sniRhdSFgWI3XECp5qQ9rT1ongMmw3ozevuxsPI2JC-ogYF0ArgOAkZCgOzdd8EUWmDdRAPd-uRlLE3blls3PGesU2MQqYGrBOcA4g8muYtSc0dc02kB5oNH5n-mpgdelbid-3nX3R4EoVhEkGoZyMGYYaaSkLcai_wYcEqTHHvELqsyxKOfGJ757hMZk4hEfrUURUywJVASnQOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ot9ela6rrcLqzhnhQNOAqeudlYRC3cm0PaLmwJjCytP4erfEodFx-1J1UEN0H170isMWbkcDvFgL_YCxJ08OKNYA_tnh9s9do5Pn__dZfF1nSUoCg5AxsrOwZS2AOHm5vlkGLB_2Y53Fy-m-UTBwR9ZzU2r7HvG2OCH7OugPIhT3t-1CA5baGvcWxmR0OL7uPYPP0c49nSkrYqvMdolyD1IM60j_y05L23At1Cqjz7pgQZwKK7O_n_mETCRE_s4kqIa3oxvNC4TIgLBNjD0LPFQufPGe6oTQaX8IxmjY4b633P8LFZ_beF5nZsNTioc_HpDf2ZGbecWFZgfd7PFEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p-6LIjxfD8y_Fb5METVg0XMDmYEPBrObpHZKo7t0OZE55AuYrLSKrmn5UisXMErhdY6LDdDkwZxzf10S3fV-uutGPqQPSRs_6Rd3P2rHIIvS1UC0O0WEAjbJwuKjCnRKkWZqJM-Vsn4qcACGpOQtEz5Q7y9uobCXbSokczFWKFkpNgu0UuRaslkCrDpdN_-xtcMa7VZ6Q9qttCWtykStUZyL_4BbX60IOsZospQbpvS1xzi-b2VxVcnhkoLpTTYrn2BHQWv_fR3FQ7E85Ej7xCNPInH8WHsx371modgz46RqsfTrF4Ttq-lly1iXNNjWwri9Nr-P5ABbKdW1fufJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iEgmC8e9QyfAYqLGQBXeoWwgYKJdEXYWrgn-MmNCwcvxnd1NLPOM1PvvR6xSwzXIjordHj27FRZK4oidrdswc6odeCsZz_D9TpSzM83JXVBumuthqk3adeS5XyRXJHw2t_xkpMhLOiFvULTCXkjstzsXVvqHeBfaA31GAYyIi89GaLYLQ0jmKXTR5EOZuiAHlWWVD5CEyEnBqrWgr7RE5Vex2I_80T0z6b1HtaSkqZ3x0T7KyTwzHRca_o5KqiRZMikZpX11h3cjh0HOQx07eJVY0ouRXFseBH8FOqpJ6RO7ICXLFAtFxi89tQMuSo9WiiVgbwRm962aEs4UipEx-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4781" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4777" target="_blank">📅 00:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4776" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4775">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">با تینا پارتنرم مشورت کردم و یه سری تصمیمات خیلی عالی گرفتم واسه‌ی کانال و چند ماه آینده
فعلا لو نمیدیم
🎨</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/4775" target="_blank">📅 16:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود مخصوصا راجب این Demo های وان شات https://www.youtube.com/watch?v=LmXU6SEH3Ks  جمله‌ی کلیدیش این بود: The Demo is cool, but not actually a game این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/4774" target="_blank">📅 04:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GrJd-tUIBJXhQ3W-Mss2raVRX3ajRw85z2PUNM9RAFssQ3w_VjnNyJ2CH9CDYYAt36wheciKJox0mZLQLRbqL-Ahncmhe23EmoWDGSxz6Nj84nsxfW2b4apwNYVdfYBi_J3sbdPJ2XyFDKd7YTbAuO9PStPvBI4Mp0hbVjpxRIDrXPoYRTELp3pKfrxS54Na9Ch-XJW5n9rk8Qxdd8XXJSNc8-uaQN3BymidW_lpVDSRaVv9oiwKLkCKLlQwAOSItXa1iUgw9LojN2zcmX7RvEYljUTdtTUmv2VUADVmGAfDXF8laKcdXBNU_fA8v6OtDCyrs5nRxj5B5UDCi4xkbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود
مخصوصا راجب این Demo های وان شات
https://www.youtube.com/watch?v=LmXU6SEH3Ks
جمله‌ی کلیدیش این بود:
The Demo is cool, but not actually a game
این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم رو داشته باشید که می‌تونید همین الان(حتی با یه اشتراک 200 دلاری کلاد)، بازی بسازید بدون هیچ دانشی!
طبیعتا کار رو خیلی سریعتر می‌کنه، اما باید مراقب این باشید که ai، لااقل هنوز به این درجه نرسیده(و به نظر من امکانش هست که هیچوقت به این درجه نرسه که دانش پایه حذف بشه از این چرخه) و خلاصه، یادگیری رو متوقف نکنید. حالا توی هر حوزه‌ای که هستید
نه جزو اون دسته‌ای باشید که میگه ai به درد نمی‌خوره و Anti-AI هستن،
نه جزو اون دسته‌ای باشید که ai تبدیل به بُت‌شون شده و می‌پرستنش!</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/4773" target="_blank">📅 04:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سی‌ان‌ان:
فرماندهی مرکزی ایالات متحده (سنتکام) در حال آماده‌سازی برای یک دوره دو هفته‌ای از بمباران شدید پایگاه‌های موشکی است.</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/4772" target="_blank">📅 03:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یکی کامنت گذاشته بود، بعد کلی که تایپ کردم راه حلش رو دیدم کامنته غیب شد. رفرش کردم دیدم پاک کرده
😭
خوشحالم که خودت راه حلت رو پیدا کردی مشتی ولی این رسمش نبود</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/4771" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Claude-Free.txt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به ویدئو بالا</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/4770" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tZPQe-7b6fqIm7Fel9ZSyy5PzriCTEfnei15OoQmjZojh_YIcrVt7Ap7KbMWtEh2xizQ1jgNZXUU05yIHXMMW8HtAc7jZrG19UmdhwJTJDcYew-J0lxxOhVtsVi2KNKCoz-YrBmfFW7jGkltD9iDc8crLE2dYuHZY7rTXu5poPmJvte0nnR61_kZkneh3pcyuQq1EKn15tSUdhUJ9fgVZtt1fHyxakvrDxVK4AiKRDJXFooYP-tBY5kxseu6QLCglINNUzre9dZNsSRYNgwDgU61y4djz1hcvCUhnjlDMVUtndyFOLDoB1YxvhBdC9uDTJzKKJBLUozANcgBynZh6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی:
https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو:
1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت زدم رو بهتون نشون میدم
2- کلاد رو نصب میکنیم روی سیستم و به روش استفاده‌ی رایگان ازش رو یاد میگیریم
3- با استفاده از 9Router، بهش Mimo رایگان شیائومی رو وصل میکنیم و استفاده می‌کنیم ازش توی Claude Code
4- با استفاده از API از Kimi3(مدل قدرتمند Moonshot که توی بنچمارک‌های فرانت‌اند در حد Fable5 قدرتمند ظاهر شده بود) هم استفاده می‌کنیم
5- با Hermes+Mimo و با Claude+Mimo و با Claude+Kimi، و با یه پرامپت یکسان، یه بازی سه‌بعدی می‌سازیم و خروجی رو مقایسه می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/4769" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/goRpKDYfHyftXU49Go0vSF6RUkBeRobVRHNVBnkCapFnNsIq25euLoRqWJ6Ht6sAjwL-oESNccqRGRytDx00I2Fzlr9rEMt1WSQEDj5LDuUFqMkJHt_QTCdWvTnLg54Mg1rRhSP6lh1F2BpQvpEOzEKK5Kw4CwfrLMBmS-8bQdPKkO1nOb_CH4mlQXDk8I2AN-VRWsKgWdMOI784UR25LV6Dgobj_mImOMLg2i8yXnsCYqpVAIzr_InBaUIWSzn-JAORS0sXgTvApkfr0zWeX7bxbwTyeLoozWLUmJWNgV4OOmDfjm2QK9EmeCLdOwtBL-M81aVPJvqI6H5Fm3sWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/4768" target="_blank">📅 00:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه آموزش باحال AI هم سر همین سایت ادوبی داریم</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/4767" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4766">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.7.0 منتشر شد!
➖
هستهٔ Aether از 1.4.0 به 1.5.0 ارتقا یافت؛ شامل بهبودهای اتصال مجدد، اسکن، پایداری و امنیت SOCKS5.
➖
پشتیبانی کامل Zero Trust اضافه شد: Team، ورود با کد ایمیل، Service Token، Access Token و Gateway سازمانی.
➖
DNS سفارشی…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4766" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بچه‌ها اگه خواستید شما هم توی هاگوارتز ثبت نام کنید
من نفر 37 هستم
🥰
https://potterhead.ir/?ref=WL-1B24AC#waitlist</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/4765" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">(با کلاد رایگان زدیمش ولی)</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/4764" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OHndvmR0Wzh-VyfMm3fLHb-vY5Y-t7qjje03uZL96k5TI6Gtvz6ijS9eXO3HNjbcml1b3bms3fXxlkedu0xMPdyGuKJzXDHA4D7Xn9ZOlIg6cP2AC6ZXeGSmp1j2y8S7ggcbKA8brbQBfP8Yg6bvwFeCMba_6y6dXkpERRn3m3rlTokg84Y3VQlMoXk9FV1HN2sCOMJIQWC9HMdAcuYaNozuQRqSBuRJGT9fC364ngNktNFcjNZU3ETHmBZ65-NMW8zp0L25c_73OFKLLWfwwShk4PLGGbVD9nZr9DZs2GSaib8tmDFK_nW5dVlIGCtAzUgVXGKALb_184mU_r6hbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/4763" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4762">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4762" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gRmCQl6At9pmqOcb0b7Ykf6I33_6aH27r7F-FkR65ZdHPjnqtT4S77Ag3c7CF0srgTLnNtPqbQiCvWhhKVy4XrsIaDdVTjF9ggqb2ulx5s9mLORR5pssSB7G6qTQYz34Vn6HmykeSes8rltwgnTUg2G1h4BUpj0fuQkdZa38uLBldFBpAkHPQF7xXgfF7MqjtCzXkCq34RVTE8fes2Y7iVRYGFlk35y7bROq2BlUJjPB3InfJkLVPeROl3kOR8d4ppie5WQYrV0cl-6dqOja772PoN5p8WZYvOJRGmNjNp9J7HnuZ6FmrBSaHZYu1Pbby_UNVaBJz5ZQxaRZEEt5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4761" target="_blank">📅 23:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eNNSe3Lpie4YrGU-0XGO4ZXeHRK7IYBFqbG7GwKuWqoqbj33ubOcW3mr01ySauqbZNXG1_IpiqKz2ncsj9bOhJ8KSzMfJ0ONHsKzi79xbX1BbPeLcLJW7-APennlq4TYr8Td091f9h1jjmx4Jd92sxv9gwYlGo7HXA7qK6LlnNdl6Wyypj0hHQS7ufqHryTBv2KfVE43CN99CLs8EUuJ91urBRNuCeZdGyn7CYIRkvsKzuYTspSQqulW9tMadyJvO1Ckq4FpkcqLgakKPo7pk7sY34yZNPR25CMB5M97Aa90lXgILDiiwSG2wrXAoXLS363dgdzl4GVMVElYrbw3UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پرامپت دادم به هرمس که تمام اتصالات سی پی یو لپ تاپم رو داره میسوزونه</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4760" target="_blank">📅 18:26 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
