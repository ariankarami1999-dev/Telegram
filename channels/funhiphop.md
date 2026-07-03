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
<img src="https://cdn4.telesco.pe/file/ZC3v3NThZD6RgR-NuyWjE4jMAyd4EvuyzbNGXtlMJ8YcGe2hh83uwuCEk6COmBeiDWGmxeNPXCGMXjNgMOPDCqMzAc6N06XFHbERfW__uxDY3_OwlNiNNajLQLXQuaMTL2Kjace7bE4JsKqQASATV3k6COjObcmwamn7EnEHt5Qk6mUSutyOnfuNYagkX_KDxjyF0xHQ4A1f59oz_or3vVsRqDJsw3lYioNbmancI2eplE0ZlPFp_V_8kdBIwnWs2LuvYwi_nlmLahAzvMQTT3Lx_670-HqaqSxmsAQU_eYsTxQ82nMPSNnab2mjZKCcPrk5pz4dw9tf8HuXWaZRmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 184K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 19:49:21</div>
<hr>

<div class="tg-post" id="msg-79285">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLFNvhtt79UikRaCqSMsLgUmdZGFFFRkKBBku3laZbxvjt9TM57J3TYwJ1mUkA5eR9En9--7tIvYJbdnwMPSD4CFTNdt4HEd-e_1AOFIeuII8W2aKGvJpn3YHE97qf95fjjcy06WzHbLwQNiQEAqvzGM98HO7IP1utcCfZAdwgo0ufQMt4350dZNJcp62h25Gj-Gr7W2hjMfxq27-amh6Ua7dNK80PGlMyJAxMkqc9Oj4wD4QEpkahakjR27cBouheGppiZVZzrHAXADrNJwVXOedjsordgTGENGu3eHbBUkiHbM7GVSyn2W9bObp-ooeln86a7zqSbevORN_TS9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ژنرال مرحله بعدی با چه تیمی بازی داره؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/funhiphop/79285" target="_blank">📅 19:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79283">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayNShIhUf-nt5s99AzHOqtSEeuMRH85K2KZn4hE3ZyBELNeXiE1ns88df3ANMAfrCesdfBs4jhD6ApcKi-5KFXn7fcsj4CSrpWjCZqOaS3rI_FhiLvKG8DapS_T--0Q7dKzzyk0MsmQPjgeulsInpyHb2ypaBhDmSS8_80jsSGcwqLZTeBBtTOlheksbqjyedZFpF8SiGDCdtF05PBuZXgjB9eRAuwH5kX_SMf5HVpBCotQyYuoVfuPXiu2Taz5trjLQ4RB0xuEllq_R6nCSOUJ4SnOxs6smQyA4kGYbiMj6B5QPS5yEyPvq19TM9nOJb1VF7XJXKY3firL8N6z1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😭
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/funhiphop/79283" target="_blank">📅 18:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79282">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF84PAdk_S7JQZh8LzVNb4lhokzzjCzxL832c7TWj8H3WeswQNrk8qnyBpwmO5pLPm7L9mTSdKLyJpq8nWlC0xYgsTUTA_SrVBOR9hLieW97bTrZ2v941RjPIQ8fpidCHwxwrJwHldfZ7t457qkLFOzIxY0i3y2osv_pYIOb6sQBh6iKmYFKfIWc2BpXnZb02sShTHmWW9TUDc0KzDPX7e_HOD5lsyv9t5C2PexrXafN-nwSh0B5zI0u9WbkfBsFJ1jyF7HInqYoC_UM91BFFbxiUihi6YVgJ9t_sozVXvKQAoWEdhLB4D2ghw1aGjT8KQYSFWp2cnGEAeXoD6Nc-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهر حیدری و ارام طلاق گرفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/funhiphop/79282" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79281">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqDGXnIpfyHSGRF1EbcMMzbMml_45CKKqXE6wNgAEPr7NaMgRSd4_Vd9_NebUg73A1D--Muu0KB1kOPlGU2uyx0-tfMGADlMMxr1sS9edPW8nlXVHbUxU1ZGPisLYKtCy8vK2Qcy0-5IXTjfY2bGdN4eHIuSjxXK6df8cLOfLYPbNrpt4gM-9y0tnfDaFWjBdUqAzpxku6cHb6Y6oWGlZ0__T9ALB2CUsRqZ2L0GmSEUm1C_YO6UkL64Ev9x3JXLXiXt0zoPA8MhGNXP9yG7Wo-19ByIFUeTPbIk1qEQkRMSesviXDWiE9-z4IKrkWihVbMeOHfk1Gn-Vre5gQasPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇨🇻
کیپ ورد
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد شنبه ساعت ۰۱:۳۰
📍
ورزشگاه میامی (هارد راک)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- آرژانتین با ۳ پیروزی (۹ امتیاز)، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- کیپ ورد با ۳ امتیاز، به عنوان تیم دوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی استرالیا و مصر برود.
- با توجه به اختلاف قدرت دو تیم، گزینه پیروزی آرژانتین می‌تواند انتخاب مناسبی برای پیش‌بینی باشد.
🧠
روند موفق، نیازمند توقف‌های آگاهانه است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
G12
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/funhiphop/79281" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79280">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhTHNqsAGso70bZjzj8wo46MQ6Ne6S8VFNz58lL18-9d_VmRgz59_sArsAV8TI7zytjUb0sk58QTrB2mQdQsSL7GaCjdD4pc6KXv8VvXuzxiez0xt6a7JXRE0IgTi3tl27fbfmr10_LmuWiFKFzJdENn9L5WBYbarGP4AAGmkWWZOU061qkg1nJSuTiieGh89v5rAdIyko-367jjaF_QekrlmJv0Br4dRixHvyI5VsNXxrKmHv6nEisj96sRwiURFCXOwu0DjywFvEMjouo26BEdiZsugrotRyEbQUfHCfkxKa3ZMVCEma-3AZ9WzHhTZgkqvUtWxjEjntSegs4tQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه پاشون لیز میخورد میفتادن چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/funhiphop/79280" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79279">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBNWFCCRjo-vc2LXtWOw3x_smyFEgLzZutbS0UKb9TJs6hsQeXgnT6kK9wT45GPN1vDaVIs6704NOGDoJ63eA9rz9ymAWY93k91WTmyaB3qQXbOWiUiFWA1pPzUzPnMakHg0FwdvItRkI9hJzBk97ZkGNfhP6F7I-CqXfHEG0da-DuhjmZBVHw8P7Kl_Dxxw2lp3oYNwYH1iz6OurSAon7p2MsnfWwAEaiMSOTGIkcSMnrTMKiht6MGMhe9cFPoPZNskU6ZaMzAf9l3_MlxTydhIGSEc4pr_fyB5QRsg75S_0jgsx0p8X2dc03K6sQd4Xz_Pw5NNRLCTtkhD_dzWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/79279" target="_blank">📅 16:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79278">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4c7250ff.mp4?token=tJIg43xVpHICxD19cuBTVf_xxR3EhCOHMec0BA6X1Jt5esOMo-urLlRKSSQGrJW6jnFoBuwtFLjdAYpERWoCBeaz10R4JIA3q0dHc6itnbibPz12nBF87H_AoZi4C6aLQ0AUKACrrBOWvd-_zL1H3yIyE4f3bQX5AGv4Lec6bNgbZpYfhYR-rXekAFXHp8CNmrTXK-L7yKOVy_1TBeBmv5O9e2fTow80zk3K3N5ZT7MdmWZ3Xw8NK0efW7Gwoo2vVLhHiOD8l9eRo9u449o5ecRJtVL6DDyqWVY83WFizdsjFdPi6kOsZlEkENYNQfTtjxI8dKek6b5rHy3h8rk8xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4c7250ff.mp4?token=tJIg43xVpHICxD19cuBTVf_xxR3EhCOHMec0BA6X1Jt5esOMo-urLlRKSSQGrJW6jnFoBuwtFLjdAYpERWoCBeaz10R4JIA3q0dHc6itnbibPz12nBF87H_AoZi4C6aLQ0AUKACrrBOWvd-_zL1H3yIyE4f3bQX5AGv4Lec6bNgbZpYfhYR-rXekAFXHp8CNmrTXK-L7yKOVy_1TBeBmv5O9e2fTow80zk3K3N5ZT7MdmWZ3Xw8NK0efW7Gwoo2vVLhHiOD8l9eRo9u449o5ecRJtVL6DDyqWVY83WFizdsjFdPi6kOsZlEkENYNQfTtjxI8dKek6b5rHy3h8rk8xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کنم دکی پولو زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/79278" target="_blank">📅 16:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79277">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینستاگرام مادرجنده من علاقه ای به خداداد افغانی و خیابانی ندارم، دست از سرم بردار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/79277" target="_blank">📅 15:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79276">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0TaQy1IP0zfPDfCsXVAxdGWi1qsYGEK-Q-FbmSBY5HDtzeD76T7wuwT9GoRRhKVbzpW2IGKxRS5ev9rlIH242jH3S2JcYVPqNqVkxTSYonaOS0wvXpU6FsI4poz4rPNn716b5zfMQt8NdmljEjCe1yc7ohL_33tbGlb_JqksJgbdSpni3QxBh9DTFYNQFneh5MXKk9qXqezb8YN8XMtiGEPGCeQUkB1o7AZVyGLBnryCul9wcbML6vzUetHlFE4-GXe9oT61EX560xcihfMO4wbspdJcdTjwGLd1CVxOm8R1BQwvuZn8OlCLEzEPqFI5yIqLDV-SG5116wYwh3YqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا تمام مقامات نظامی و سیاسی امروز تو مراسم بودن به جز اسی کوهن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/79276" target="_blank">📅 15:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79275">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاش یه مقدار از پولای بلوکه شده رو اهدا کنیم اروپا کولر بخرن باهاش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79275" target="_blank">📅 13:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79274">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دیروز میثاقی اسنایدرو دعوت کرده بود، بعد میگفت آره ما سه تا مساوی اوردیم شایسته حذف شدیم، اسنایدر گفت خب کصخل وقتی حذف شدی چه فرقی داره سه تا باخت بیاری یا سه تا مساوی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79274" target="_blank">📅 13:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79273">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr2pQUHBdWJAjE1ULyPE0iTgllDr5j-JrmJRQ0NJVX1qB7Y7JMqZ5nRup6BVqMW8E4VTKTDPj2cIcPXC9skIKtddTyOhYo_DKWWLuXTpN4BJ5fegyOu8GXR4Ex8L_Ckg3Avurv_JTM6zFrWvaskePRO2y6Cbj-d_iS25wDuJhEFx8CA0-IBxAg30Za1tl43kprYsc2TZIOmoPTjuj84PuZJGk556Ui4n9vAYvKsBlKykKuh09dHx4lHZHCnY9lsqR3aVoYR0zxV9bO8TqFcLiAOVw83upNuQ08gdpurX52Nczuihhve_XruA6i29G6c2daaDbojrZEs9IZyGyWBDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سروش سروش ببین چی پیدا کردم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79273" target="_blank">📅 13:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79272">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">درار از جیبت بیبی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79272" target="_blank">📅 13:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79271">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu9TC1RGKcfEOUhNiCYqex4xNW7LyS2jgYvlzPxqyUp5BuV_3SxCAxi7nBGSD7W5MHUTqcMv6jy2QOtfkHzSQjYFTq9PFLiE1Veo_9dUElCnG7dn7UYAjGUfhRlOHb_CwCYhIsPU0oympnJtS-xf7i_bbFL21bRTGnbJMZOCpiIT9N9sUV_EaFY_-iEF3G8VZn-OrXUftdnpwaklRM9QxKv0L8qxHHXchrEpmFUYoaFdleyo8peXk2oCYbie0pBpmeZi3WtGnMHwFtjLc_qsAOLcsmI7h0dfofk19_mjhuToN4XE_XSrO224jGH5MQXcxmEPbt-UzJmT1UwxIjOnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امنیتی اسرائیل  در گفتگو با i24news:
هر زمانی بخوایم کسی را حذف کنیم اینکار را میکنیم. هرکسی الان در ج.ا زنده است یعنی هنوز زمان کشته شدنش فرا نرسیده‌.
همه مقامات ج.ا در دسترس ما هستند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79271" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79270">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAbCfNTHJKtJt01PVJuXJu-4q8pxJsToxJtADyJsjJ1Vdt43wjHGZJYcQTHD95hgEQjmO8LGP8DXchsP4uYt3eJJ8FsIQpNSZfyour4GvT0F95fUqFiDM6xNZ6NU_yjihgMGBOiIbj7vGPhqsLq7DFeEZhCHSYADjm9pwDRMpOHJVKhVq-f_G3vc9oeIlZ_wDCpkZDi0wHgAM1KENh6pzm1cuWwAKFNUjDc3FLi-AWX3MLwSk-fbaiABgsWiIae_egYaeVsAlX4G30muYXML8Z2UU3s3qJrR-VjmuqW3RLPJrnCzVz8eAS6Z8QJF2NqwKxqzfrJ6TNcBR8u5J5iDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">که گفتی شاه ساندکلادی؟
😂
😂
😂
😂
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79270" target="_blank">📅 12:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79269">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skZd2AngH2Nw5IQid2TivXInEei1u-aNg2AM0M50JR2ydYeDeAVCZXWdAQo5sp9o5QcPrItS4jTOMUXfLleJCzp6zXjdwJDtVkYphiLwOmJvF2hIoaNVEb0HLLFQr1nVcBmjgoPaq5p2bmIy8YByRS5X6Dpynxz6YKqVb3AW0qqe8BB7BkW5geGdsnkI04cyMIb_xlG-stWBpmUcl0TEYYECPE1n5AyVrojseMROTjJrn2ZChnUa-Lazn-ORritk2BXK9uD8M0LJX7c4F3gSCYFWmnPUnulmEM6Id1muSowzxVcP5Nazlv5k91PhSeFbYqC3IsT_5_1s9NSl_nSMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇨🇻
کیپ ورد
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد شنبه ساعت ۰۱:۳۰
📍
ورزشگاه میامی (هارد راک)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- آرژانتین با ۳ پیروزی (۹ امتیاز)، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- کیپ ورد با ۳ امتیاز، به عنوان تیم دوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی استرالیا و مصر برود.
- با توجه به اختلاف قدرت دو تیم، گزینه پیروزی آرژانتین می‌تواند انتخاب مناسبی برای پیش‌بینی باشد.
🧠
روند موفق، نیازمند توقف‌های آگاهانه است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R12
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79269" target="_blank">📅 12:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79268">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSW0c_o3krIyuZhjsBmnRzaH39_qJdtkyqXlN2u90j3tzO8d3LqTcXuq5JFLm42irnnZIvNdKOe1AzpT-PgJ8HpLTNA42eWkilO8qWvtewU3d1H4kmZarKscSkWJ9-7UOr9dgTmR2dA9HdgUZtTqvNvomI7oiAbHdpumaxx-ve_zSQosmTLiCYv7naAQfh0ppVw76eLIx1GEuICvv45GIMATyvgW5HznLV6aftCayz5qbsiORm1xinl87uunXCHtysfKO6UfPhclh3JIpMT5mRKAs4gs6xFNSzNc4qVPTTxAeR4RlyglI9yGUx8ho7zxSuNzYlPpkeUBKRLK1UyQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی به این بگه همین که نشستن مذاکره میکنن یکی از اهداف آمریکا از جنگ بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79268" target="_blank">📅 11:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79267">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه پرامپت خفن میخوام تولید کنم که توش کون نیما بزارم با آهنگ ترویس اسکات، فقط برای ساختش به خود نیما و یه دوربین نیاز دارم</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/79267" target="_blank">📅 11:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79266">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoxuP3_soFvbSv_1TjpNAShdis2NHz5gSUP0gpDt2uCj1hrKAb2YEwfI6rqidZnk7NPzRmeNAmAVo64UdxNV3Rr74J--ZjoO7IBZJsl2he5Hqet86oGV0aSzVHT669mLhGmvOrerVj5lMgyfyhUK5scCyT2q9p_-HnXXlEIOBG0JG5pHbwydBfUMsitdPwXyzQPH3ELqljLsFKVMNu3ZCRt7LkdOnyjUVHhhdoZol2D9S8DRHTYlAw82EuC3UvLkX_jPAcbLNMng-XzdYzqHSSn6XjUQ-kHfMhHW8H7HNvt7V7WQFcGvUm_xQNvW31wAZ0wZM6HiAU1EBjaI4XIx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت خفن اوردم براتون که تجاوز پنگوئن به سیاوش قمیشی با آهنگ دلخواه شما
(به جای **** اسم آهنگ دلخواهتون رو بذارید.)
A medium shot, front-facing photo of a middle-aged bald man with glasses wearing a plain black t-shirt. He is bending forward slightly, his face contorted in a realistic expression of intense pain, anger, and physical distress. Clinging tightly directly onto his back is a full-sized King Penguin that appears to be straining hard. Both the man and the penguin are staring directly into the camera lens. Photorealistic style, studio lighting, isolated against a solid, put **** Cover's music as background.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79266" target="_blank">📅 11:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79263">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iysKI3K7iywL_MpI8_mDkcBjhXgKdr7esIocfu3WRVRdMy3Odd_b5UdCOJs-5xKiCZ06Zd4nxT_9_UY2hEUSCWxRmcYrCC7TiBxTDHRdhysq0loMkOLr4av6ieE9rL4dBe7_pVGkpWi8Ye_jucTYZJ9H8C4zb5iNjZGpwpRle2v33dAnpobH8Tqoan-K0sWD9trNh6SL0EC1769SAfLdVE8_7N-jiC1u-3wE7W64z09HaYY2OjxXvq9eNcARSJrTn63BfEibA-kQAf9B0ojuzwUChdArUAaaAnunvZIgLvq_-Qv0O1ojJW9tA0bUQtWqpsk40fAo9cvQKPexhWIW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJ-gYwp9Geqvgr8MCzxeAmhVdwz5apWBRfWjjrUPKbXe7tEKLpd1Hf8QNuFqihRuGIhVqV_IYzhq5dDHTmpemJpWcoWzvYfg1EqR4zFPGRa8V5w1Vuu1Z__viPsZTZ_mj_rn4JrtzcGy30nYo3GYZuPZjr_qqnjIFhX_g4u3BL1dixA3R13mFQnKwLXU5De5hJxzBFhNo5b21eSJLIq4GZGbjkQTeyqpNdVW7UDCqLuiyLtQnldRW7gNw5S9o3ckD-VSiXdqNWoBYHbUtSMB1NYk1HVojKifRlNzVogWTihjHgavxZ3avDJhzVS5kuqgglV2oEQA2aGBBgIETSFJtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پشششماااممم من از الان طرفدار تیم قبرستون اسپانیا و یامالم دلیلشم به خودم مربوطه
😂
😂
😂
😂
😂
😂
😂
😂
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79263" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79262">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دکی ۳۳۰‌ میلیون تومن پول ویناکو خورده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79262" target="_blank">📅 10:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79261">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">زنوزی: تمام مردم ترکیه قبل این که فن تیمای خودشون باشن فن تراکنورن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79261" target="_blank">📅 10:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79260">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e68880fd.mp4?token=fIgs_xQhVFCrVcbDVgsHk6Z2DjOVgj7Tpjf8Z3joMyEpB86T0ECjx46Y5Umk3cNA4tp7pHtJhi6vSCFmAEzvlw7ATOsd8XTndhriBDe2NrTOuvcmn_rdTvSEhDJFeSThhfmA6xoimDuDay7EGlJ1Q33wwIUWwMJY-9v_rt5YqI4pkWsHdXV0_4tInMYuUBENy6UZcgynkrsdsxZDl91O9brl_B0iWJml-HhgGrQ46G5NbDce0kReL-MoE2GkcPhe5Y70tcnV7ci91ugfRIzco3r6e-ekoVLMfWLnuQfNbtHZe-OK3hnKPBJOe9mK1OCrKLyEMMijdYyTID6gRMlk0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e68880fd.mp4?token=fIgs_xQhVFCrVcbDVgsHk6Z2DjOVgj7Tpjf8Z3joMyEpB86T0ECjx46Y5Umk3cNA4tp7pHtJhi6vSCFmAEzvlw7ATOsd8XTndhriBDe2NrTOuvcmn_rdTvSEhDJFeSThhfmA6xoimDuDay7EGlJ1Q33wwIUWwMJY-9v_rt5YqI4pkWsHdXV0_4tInMYuUBENy6UZcgynkrsdsxZDl91O9brl_B0iWJml-HhgGrQ46G5NbDce0kReL-MoE2GkcPhe5Y70tcnV7ci91ugfRIzco3r6e-ekoVLMfWLnuQfNbtHZe-OK3hnKPBJOe9mK1OCrKLyEMMijdYyTID6gRMlk0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79260" target="_blank">📅 08:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79259">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پسر خوب فیفا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79259" target="_blank">📅 04:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79258">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79258" target="_blank">📅 02:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79257">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79257" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79256">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رونالدو بعد از جام جهانی از تیم ملی پرتغال خداحافظی میکنه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79256" target="_blank">📅 01:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79255">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امشب یکی از تلخ ترین شب های فوتبالی برای رئالیاست
۱: یا شاهد گریه مودریچ و خداحافظی احتمالیش از فوتبال هستند
۲: یا شاهد گریه رونالدو و برآورده نشدن رویای قهرمانی جام جهانی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79255" target="_blank">📅 01:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79254">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79254" target="_blank">📅 01:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYoNEKSC5NHoGB0KQ392WFKvDIOX4yLI7UpjS1eIclcrOdFhbSAeRLfx9Mg8XCa8XYarZhvOkKT-eo9I-BmjhcozAsOto3o5GHdSx91gSZ_eET9TQr-t3aBqf31zGCm_9uFZaXZmhoYDLfBrR98QjHVPidRj-lpgvP3-ocf1Eme-g_tHZnw7NUUt2YFl_xcQ4SjON1K3wgKv1r9JgoTv_BM_Zn5374aRWAOUE-X94ABuyu_HOS3jMUfgdVPiMtdqRNgMwt0TH52GJqvi4vOpmoFN22ZNTT4XbbI3EF7i9zCojPzJW1pGA1TDYrh1ZQzUTQfrywxiv4Ahah60aPgRfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاگرد سیجله دیگه، زیاد سخت نگیرید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79252" target="_blank">📅 00:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مطمئنم یامال کرجیه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79251" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJtwW34lBwRmd-90rQRgMN4b_ZCL6w_KrY1hVWWd2AnMGgfNgfvuAzqI-Gdl49SR3tFbr5P5ZPSjSc-aqVtXp1RnchFAlToJMea9mj0n4HAkH2cigl-8jY3Fh6Psdg2hXrI13Y9UoOEirj4bpO9xKiHl_s6LLP4CnjJO__K2UB3vIDsrJLv5hr_L1NJn4Ssg9_PVRlyWjlGMruVbjZ14XR-ABrKGK7obgU8v0Azx80Wd5n3VFRV38nXqb3PdEFYluzvPPNectNYVwF6ii2lL5WoxYL20bio7KKHETpkHtgWU7ZKk4gB3PF0JGTi613Tn4rPUAAlvEnBjjsSmylx6dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و مشخص کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79250" target="_blank">📅 22:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79248">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKL96AY7OncicItw3GZ4T_D8YgD0wIjf2ddWqteE0tM_lyljlfIL3zzGWQdfuNVnZ48GxAM6FFKLU60xWVmX318cbBy1GvuTxbSlJ-7cw8EkIPVrFO9iXsE8kWE7HamO7M2ffYol-QXjDETIVIs0sLS1xApPPZj3qm93yTWaEND02i8JUzaTtumlnTO9meDvkBw_peoqlh0GHxIeDPjH8ZjjEiJv8ClRtjouAzy4FMBysKH4cbvalu6743rMosOt6zce_5pKoCjJHEyhGLDSu5nnO4QAnsW_kpO_i9z7tdoGZvsl6joPOGnPvySehwN2TsZJ0jo8N-s1c-sYPOH1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری به نام “به زندگی اعتبار نی۲” ریلیز شد.
Youtube
Downloed
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79248" target="_blank">📅 22:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79247">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP043PskMWkPxNibP6mdu-yJdQebnKlhbnT6WCNosNfJjdFU1ycARuwL-eYDeuOES67poji6XBoI1ue-dq0_wTef45TNyqkw1fKX_Bz73ERc32UTrDMxKN3DcdQv3sQqfh0BhN1gFuHq30kNhF4sHeW0yxz4n1A15IyWeZDKQ4RbhGo7G8nuPsLXT1yXPmCmSjQHvpKwYhShTCDvpcERXyNq3Gjlo8CFl3Q2cmg3-ihzkSP1DyRNS-I6RCG4gFyxsRZEiIlxNgt0ncF7SY3KsRJZVZ8NIWI8tOu87kgehzrPSFMGPWgR--5ZMJyN0t2Ke7DwdnectTj8YzaVfz5Zmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلیوم جان قلب خیلی بزرگی داری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79247" target="_blank">📅 21:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79246">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR07VIJqnV12kbGh_9tHGhdgrtvXfw0TDnCoVZp_1e5Ev-HmzsvGMYakv6TpssltetLGjwQPxxwifrmktGBDY9n9y99HmgKy2sg8oAIGjUeQHUJARAh7ZYnBfkGrV4MCiOrbZxIunYkurziGRCT6cr1gT0BODKgtkWO_L-2Fnha4Xc6JPM8kVMJcmDaKg8rgfrMiU2G8fcyka0sal8KUR9JFML1Andg35H65JfxZJCXpYNDqWbN0v9q6Z56KYt4vRYGL_IiqsLcKEvEnQCPdf0LNQxu68W7Imhxs4YfGGaUs-1UocJUsdepGR4Ej5-7THXHC9mTYv03Z0oD5EAzNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
با Legovpn وصل بمون، همیشه و همه‌جا
✅
سرعت بی‌نظیر برای استریم و گیم
✅
لوکیشن‌های متنوع از سراسر دنیا
✅
قیمت‌هایی که نمی‌تونی رد کنی
✅
پشتیبانی ۲۴ ساعته، ۷ روز هفته
✅
کشبک ۱۰٪ روی هر خرید
🤑
کافیگت رو بگیر، دنیا مال توئه
🌍
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79246" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79245">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">لومر؛ خبرنگار نزدیک به ترامپ:
مراسم تشییع خامنه ای پر از هدف برای تروره. مراسمو بمباران کنید تموم شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79245" target="_blank">📅 20:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79244">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آفریقاییا یجوری تو جام جهانی با دل و جون بازی میکنن انگار به برنده غذا میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79244" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79243">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه خبری اومده که خروج از کشور واس کسایی که پویش جان فدا ثبت نام کردن ممنوع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79243" target="_blank">📅 18:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79242">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxGvHdsXj-_an4LQVCG5sZgQpSiDvpqclCvNo1AYKJ8GYfeyT1bCBo5VzLKjsJrlQPkshKpgHYQtHpOaqgqiRUqLhhznrFQ37GyzsjbBu53LEEpSwmVjJK1obCuuyYwDj3n5ScC6Dn3sYDAD6ooNIfzzdAe6QLned-J0VRRsfpZfcrfzvG2h5SVq6bRgrkxh-dKQsWZ0RZAiHsFDSHvDiElbyX76OpjbJ3m5NkNZUWZUJpo4sC2P4RBzQaFfJ75v3fhxix8zBZikbT7wZjVsCqXQcLWk2kNElEo1BxnubUd78XzJdy6H7i4SWkYkNexNWUejNgs45FwilbSH83Q6cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی سه هوش مصنوعی واس مرحله حذفی جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79242" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79241">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAY5FVTo6_EEiRbIyT6A8ZyoTVFt9Bnv2XwJqtIlxD2eDhKmce5x2RnlJDK-CcdMnknZg-j7CqTNQN150fENBgmfAa5HLpaKsQyzUi6BJ38X8scVJ9aqISpjuwsHXqiVusN5A4xPWzO8JQMzJa4BemRJRsjwcImqyNEmuLFaIvafAGESC7JXUDYYMrxwfyfJYL7olFvzY_BaayZ-LHU5xTEj04LC1LPT5wA3r6DqxT5hGXpIv3JFSNwytOvClIKI16NYFYKBIO21C6hUPHLjJrTo29QHJaCoOn6ViS9ih3bwNb6d9yAn-EQNiHO2XxSLEsmWY8Q57MgbMurJCFI0Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد کشته های اروپا به خاطر گرمای ۳۵-۴۵ درجه به ۲۱۲۹ نفر رسید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79241" target="_blank">📅 17:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79240">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsCEBpfKWNmRIHI1mAqzn98RlAUSOWm8uEqw5kIn4m0iDrqONin9ZqxSdxn2S_e58TlkBS9CUN10Guc9I4I8f5keL8yL0cTVfSb891-tDpl9mFyVJOnuBeBHL0G1YxWIbjydWFXZEUViu0Yvt2vzEPEqv1a6ngtfZxNxAGZ_QzdXqM-NL-XGnoL1FCcHu4BBHrB64gb_GlkIYgTl2g0cFEpBTGyj2l4cv3OFw_54pposMLqzDMjHa1VgPyA6G46TKOkKoa1IaIsf-Z1fOhWoIGRss77eaIJsbdnuxQv4b6A6VRDPgVvID3ECcVdUCPAEp3ljIJm6zfnAZyxOWwN4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر منتخب بازی سنگال - بلژیک :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79240" target="_blank">📅 17:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79239">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeiERD9Mx4NFMimY9h5SYAn7t1erb7jx-CCYmr20VidRrc5b3JhmVcmiNLwrG7jd1ByzKfXC81_1dHQC-6MORl-ldKk6BahfP6Sd7Y28BXlAAGPG8OcDvOGc1Ql4oUw3PsQC221yPV_oS0XSo_KM-FGa80zm-pBn4zIzjjQ9bjBOJIJWWWbmfoRSNFzjKFRR59gSM5NBkEGLmtw_UPaILaeslYhvocQEj3L3nyLmE502QrY-HGOlzQ7L-1NZ6jykeXa9_gXZfT8Ch-gzPRZMfdZP8UBAy59l0VgEzQeR-9u5nDe9-zKhFxoCdZXBhWviXfBrYJoOgXsJG_DDXIKGaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇭🇷
کرواسی
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد جمعه ساعت ۰۲:۳۰
📍
ورزشگاه تورنتو
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال با ۵ امتیاز، به عنوان تیم دوم به این مرحله صعود کرده‌ است.
- کرواسی نیز با ۶ امتیاز، به عنوان تیم دوم گروه خود، به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی اسپانیا و اتریش برود.
- با توجه به ستارگان و قدرت دو تیم، گزینه صعود پرتغال می‌تواند انتخاب مناسبی برای پیش‌بینی باشد.
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R11
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79239" target="_blank">📅 17:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79238">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مامان شام درست نکن نمیاییم خونه
ویناک شام خریده برامون
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79238" target="_blank">📅 17:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79237">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwDmsAFGRL6evK-HsfMvVPJ_c2tY51V_xxrBP3E1wOh4gOlzXmQ0bX3SKD2byf4unkaAmZyAsHi0INUyao60Cb33sRO5q8xzYjxfo5cnSV-Tc0zrMU1j8B8LoVQfulg4BB4C4nfpetfehoCCkUn9usN0r1_YkfyDOt3z9bioe36nZ0hH2zEZQk5am5TW1TtZqNbvDRi_dpQlXNdtEoPavubJ-dlp69eKO4-rpGpr5adReOrz9zpeHc6PbhB99PsK6nDJ3hN3aTCy0xJ8wgmAS0tvmlCvkt6Hdg0CDBj8nOgrfo2X9DYOWQfg9SuNcaT88kysT5aYwfn6rE4xx-dNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب مراسم وداع با زن مجتبی خامنه ای بوده (دختر حداد عادل)
پ.ن: مجتبی تو مراسم زنش شرکت نکرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79237" target="_blank">📅 16:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79236">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">میگن ویناک گدا گشنس بخاطر پول داره این کصونه واویلا بازیارو در میاره، خب اگه دکی نیست بیاره پول ملتو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79236" target="_blank">📅 16:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79235">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بذار جیبت بیبی از بلادیا پول زدم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79235" target="_blank">📅 15:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79234">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaGBHZZZQ-NlQsEtuXUonWmEA5bxgwhVGxTjs9s40__DbrLpO34d1534f9AObk-BXnA9Jwjcuu7bM4RW2l6b7ddc-Ap-MJ7y5Ja1gZM2_ma5gotROqeIRY_TQgxZt1uQ-iRTOd0gy63CNKZQsTLvr_AKLm1o2VETbB_yqJidFyRiiPxb4skk3zYAd3IzFBGY-I9h8EnjK4dXc1avg2e2KVEB49l7mPdAqBLcOV_5j2VRfpcsiKaUNk0xLd-jueVGYLuUNoBGdDpZMkcmSRvl60Fr0sEm6AGEmP0o4viFD491_IlCRr0XuoAs8eeQBkF1Mun2H5o9aVN01vItwKwjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به اسم
ویناک فلو
ریلیز شد
Youtube
Downloed
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79234" target="_blank">📅 15:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79233">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نفهمیدم پیشم بودن سارقا تو بلاد هوس</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79233" target="_blank">📅 15:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79232">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ویناک عجب چیزی داد</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79232" target="_blank">📅 15:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79231">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اگه فان هیپ هاپ نبود بازم تلگرام میومدید؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79231" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79230">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">رفسنجانی این بی جنبه بازی هارو در نیاورد
که خامنه‌ای رهبر کرد
بعد همون خامنه‌ای کشتش
این بخاطر چند میل پول داره خودشو جر میده</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79230" target="_blank">📅 15:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79229">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این کصکشا بهترین ترکای دو سه سال اخیرشون فیتاشون باهم بود، ریدن تو همچی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79229" target="_blank">📅 15:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79228">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79228" target="_blank">📅 14:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79227">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">درکل کل رفاقتا رپفارس سر منفعته، همه اینایی که میبینید تو رو باهم رفیقن پشت سر هم تو پیوی اینو اون ناموسی میکشن به هم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79227" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79226">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">چمن کونی پاشو ۷۵۰ هزار تومن بدهیتو بیار بده</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79226" target="_blank">📅 14:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79225">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79225" target="_blank">📅 14:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79224">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پول کاگانم نداده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79224" target="_blank">📅 14:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79223">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/79223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دکی ۳۳۰‌ میلیون تومن پول ویناکو خورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79223" target="_blank">📅 14:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79222">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کونکش برداشته به باباشم زنگ زده
😂
😂
😂</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79222" target="_blank">📅 14:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79221">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🗣️
چاقال چاقالا چاقال چاقال
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79221" target="_blank">📅 14:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79220">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بابا
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79220" target="_blank">📅 13:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79217">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/79217" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79217" target="_blank">📅 13:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79216">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhYwT0Jh_WnZz2i9nr4bWgWubIkxrnjzbQ04wdmfk2VSKIeH-qQkoIZEZaOtcIo7UL0xya0BiI7dS41j0LhxskcISa0NV5yB2mXICBk5ivHqNOjnqykhF3MqmyrTwrYXVywI2e2w3kUkZJpjzBnV_Pxv5gsAsJ2zFSmpZ9izpJP7q3JMI9gD2v9wB7Nq3SIwIld_yWD4nmBal68U3IASBXBMvrHI8OKUKgaJawc4mP-tMAwTv2KaLZCAmnXlkZCjboYtiavDNaokrTovACqS5MVFYusOiQP7tBvjscbYxGxahlwcpz-sRaVUr9Mxb5kCOg8hmsrwEf71RWwcKG2jzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز تا قبل تعویض شدن مادوئکه کل موقعیت های انگلیس رو مادوئکه ساخته بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79216" target="_blank">📅 13:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79215">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تاج: پیگیر هستیم به پاس افتخار آفرینی بازیکنان تیم ملی کشورمون به هر کدومشون به عنوان پاداش خودروی لوکس یا خونه بدیم.
- جوابش با شما.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79215" target="_blank">📅 13:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79214">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بهترین تصمیم زندگیم ندیدن سریال و فیلم هاییه که ترند میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79214" target="_blank">📅 13:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79213">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj5g8E8f---_Ld5x69TlkYBQ4pOp62rMXdA0MDpaWmx8LJNi1bbaMydyN99rX3K7jPc7hPPtUeRZuQYUyUzhIGVgMcQ50IN73wdgDTGTZ-OlDS5_ALq4ZCqme5Aq5n8NkDpbZZfyZS5WZABZkpfNhqVRNYwbCbDQPjlcyu_RN9K5MgzAtgw8GnGCIoCD2Xbsh0mzl_ihu59NkKEyNM0XpG3sGk0pvfIVYZzkHJ42fpt9ly5J_W0oT6N7YSTJliDEOykDW0ESv1MHhFy6b_uOgj5aBaZ7DV2E_WZSFueqMsmvU5hAyFxF97oG_iSi27SV9_RBAvdDuF0_X2epdgdE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجشنبه ها با محمود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79213" target="_blank">📅 13:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79212">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJXRKV9HOZ8kz0wWrI8kdjJABhqF2-2iAVOrK934cMj3BcMxul-rUb-_-o2nR8GO-lcujPaxtHXxvCxePugBiwaSBq8ZcQ2FiWB6FIR3hgWGEBo005gIKXbZunSLYTDkj3sqzcG2NWKpPFRc6VWbgmTYH9EImPNIjmEnrgn63wpJu_ulKVwBBHn6Tg5_PHGLVJxoUkdicY3GfFFM7jkkukLXpx21D7UqEAv0hO01tm9qGqbJic17-_WcAdkAOlchhJIrCT9XwLolis-6fdkTPwc31Zap9kRERW92XPpdj8etkiyxJCswNTZzVvo0ikDCOLTOG1PWNtm5F5MDxQnPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇭🇷
کرواسی
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد جمعه ساعت ۰۲:۳۰
📍
ورزشگاه تورنتو
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال با ۵ امتیاز، به عنوان تیم دوم به این مرحله صعود کرده‌ است.
- کرواسی نیز با ۶ امتیاز، به عنوان تیم دوم گروه خود، به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی اسپانیا و اتریش برود.
- با توجه به ستارگان و قدرت دو تیم، گزینه صعود پرتغال می‌تواند انتخاب مناسبی برای پیش‌بینی باشد.
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R11
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79212" target="_blank">📅 13:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79211">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVfiSt74-G_qtFWDtrW5kT9SPV0tin4gW-EH7mzCWjr1aRzPv3-DGyfdd-RTuBdJmvzWVN5acm0Bbc12Xc5EUZ9ECbIp3SqeWeQmv-o7hVc-iIrPUg-oU9Qwdy-U4ZGaiMcPPHaJq93hfhbCxmRY4-MhS_IdUDn6AfhE1AhHENK6zoi06zMXjd2D0MhrJ39UPLNt627LzWEvcz8m4BZCfNS4AgxTtGVDtL1nStAdpQF7TxzuLLN6jkV4pn1bPyaz6hOYdK1HHWkIFcpBy7XZ801SHr-XYclRQN4NxD8S72WGt4lgzkB5iO3st3BEDiTacjt7ZoY0p_cwqmJvRyfvoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاج: پیگیر هستیم تا به افتخار آفرینان تیم ملی خودرو یا ویلا به عنوان پاداش داده بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79211" target="_blank">📅 11:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79205">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تتلو زندانه یا استودیو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79205" target="_blank">📅 02:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79204">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gin2R2f6lf3HDxA0MJUSjtuVcDfzBdwF2vHa0SS418vMISEBZFh-TVLJDvPH1hUwq3RaOlZ0I8KgE-7328pZAMlkA0yM0XTr3Pc8sigoWXcJcXDznAQGoxmICQqhFnhgsDPYCgNilxV9dcLvEpO7SKrHFFUlsJJm7ToIAWX-BOjdK5dV6UGgbCh9rqlIWxSktVoLvPyTlRArs2n5ZZH1-UZuQody6uzNmM9eaHy3n_o3XdmyrEoq9noT_JCSCM8xKg2vtl5GG53Y83tPmAzk3kZpxf8o5G7cIRs2fL1eawxbesUAsQx0vS7fpDMlNqKZOm3r0mUmRq-AkcfPGnLg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تتلو  به نام تریلی ریلیز شد.
🔥
Youtube
🧃
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79204" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79203">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سنگال عجب تیم کثیفیه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79203" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79202">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0EbUewHemLIXt-x4Yz30-Jnc8cZtjfyxyl47YKLS4XwaQqPb_VPp2nL6kSaRN3lpVjTkteGL2sVNLlnWHLzdrwJ6C75y-CVcejoWDSN4Yau_o-ASM0HQaQ9zM6YpKQBrVQBnzNhn7ypVEzdrK8kRfllOc3AcxTkiDCk8U6VG2_NI3Jeckz0YjJYUapoz8AQV4WQqx44aUD9B8-vMVk4fBNVNKO_6vCP0fLyCl3wd-KHYKueHxVdK2rbrnrJSBafKJpEXpcj1gnT96ZBiWflfwIYFHigKlRAbPu9-POEVOjpYwUaxexXzU0gA7e0_NIWycz163dLvVQL_QkI1epiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین فرمانده باقی مونده حماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79202" target="_blank">📅 01:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79201">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یاد ژاپن بلژیک ۲۰۱۸ افتادم</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79201" target="_blank">📅 01:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79200">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79200" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79198">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U27yPCO7bv6t4hbF3npg7AGB1OQKI11JUC9El6NNZJAD8gXnYz1ajSiUQXum2x8vLF2WUkx5barYBkUViejR8c4oDemPNn2ZWVIZA-Ddmm1nbqEfREnHZf6_1yW1_mMrCi7F7if092Of074EJEgH12UnyOdKRAr-dYeTLdBvd5n0FFCPXm-WDU0j1YSX1SZTFVfI0WHmKAc6GXJTbCFkOWOWYKpeZ18RgB6xXJGuE-QY4J-qOqVQw3eOkhThxdn2D1f3gdRDr4yviz5GW5OpIOEeRPH4nZrvK4N1R0haDB7aGs43Ewyurdr0qzrim_FKI5CqXwmy4hRR3DeQUFUZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJxjXlF6sfsNy_0TmWfw_zV3EvKPMKpUehHkdHbcXbi2ucJQ6I7sbDM1fbyQyyocL3DD7TuMwrnXs0QUvuHCblg3rFsaSTa30PBPTlXZ2HpFE8gpedK3sFuawXPgBtV0EbVF-vdQvnJIBfB_Hyg9ngnIUaowjuX9rURu_bgx4BWKT3TSWoeWXwLZO4QatlpC4sD_xtKyQit3n_BxtY8cMdvxdQhWWWeAQ1MBY0iFKpxvaLDDFMCzC41bwVKOuHihahcUrtmZOPjpSZOAJIRaTS2I0m9-GH3u3kbCzLeWaIaI9tpePqo4-e0LWDq87Z4FJkRPqO_4PiVreGoTSwN9Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احمد الشرع می‌خواد برا سوریه یه مجلس گذار موقت تشکیل بده که چند نفر از اعضاش رو هم خودش مستقیما مشخص می‌کنه.
بعد لیست اعضایی که برا این مجلس مشخص کرده رو پخش کرده و این بانو هم توش بوده که خیلی سر و صدا کرده چون بانو تخصص خاصی نداره و صرفا بازیگره.
انگار احمد الشرع با خودش گفته ببین می‌دونم یکم ضایع‌ست ولی مگه کی قراره جلومو بگیره؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79198" target="_blank">📅 00:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79197">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAlprrpv_KhEPfcJKRi-CYxLH_7xpCZdlvBDkFttm4e8FZqVD2FJepcVFyzmx3M34mxN4zNya8dK867qQhMpn1-OwymXAI3AY_4SFLD5w72uLziFl1OYCQ6NNgjp04fjDIiqITC89vAW_ttHyx7cUoroPmXqZotbsC21M0K6kDwUAPwc8U-VVExhORsqf6V8slJeJfDzbg6ofdbJLrr0HwXuJlvGqlvRwV7TBriIj21Y9Ovq-eZdXSf73X8eyA-RMse7LFbLa3z84oVplZv8GARkz8Y_mzF6yGJrLWVal_Swhb3T5CPf9CSUMbkiQYm5mgkqUz9IrC_zEQ2QeIMbFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخجون میم جدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79197" target="_blank">📅 00:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79196">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUX58KHPDrKT-GJKaPxNgX54AlhnvvxDDPCC2mklU1_sNlox7HuOEGNzm_nQFGZxyKxI5z0AJ1mcv8ehhb8qDDUvSVNqoOOrF4UDnUa1HWj9It9d_A81W4PTQcko8p4db4MG5xjTie-H5aw7pM7WlugjGC5bQdaAP823ZkKqAUTrKtPWgl_K-Any6vj3BM8aPQX0ab8S4hBGzrHu1PTkc_4qP5NW7JYO_lFXd9umKKc-hjWXE2oXOqs-75Xcgm8W8x1YGQH0XjK03KTSTxsQIjnN4JbPhypRvU948c6DxQnn6NLfLD63yqoHTVrBIkO9X8tzzAS3hJ8JE0eaIuabvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد گی زیاده تو سنگال  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79196" target="_blank">📅 23:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79195">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">چقد گی زیاده تو سنگال
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79195" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79194">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حسم میگه سنگال صعود میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79194" target="_blank">📅 23:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79193">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قهرمان جام جهانی بنظرتون؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79193" target="_blank">📅 23:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79191">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">قهرمان جام جهانی بنظرتون؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79191" target="_blank">📅 23:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79190">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbHw9V5OyMOdHilitKr6myKpxZ1q77544n3hMOzORqiHSJeYFqScetcZxnD6P7fBSTqiIAmySX6zzQys-9bcNsCMnkSjbsmHSa-WQz8SXr3ay0Qmr5LY5laDaN5ozVvxOE0YZmqns9WNMhsQI2bieHMJtW4tcBDPbQ6v1kpzhATE6aojgfaSzK2x9NbV4b5bvKM9YsteQZNamIsSJ-nQuolI1PqqysVVJHTjYZg31n9_5RSD3w3_WGctkV7bSonAKOXy9AUlNhzV616EJd_LfOmv-P5p72VtF2SDjnsxyL-yYIPqGeQgkIWhAu3tL3Vr9wfV8efbhpU2BPNGU1BZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی ام  به نام “اقاقیا” منتشر شد:
🔴
Youtube
🧃
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79190" target="_blank">📅 20:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79181">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خدایا با حذف انگلیس یک بار دیگه فوتبال رو نجات بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79181" target="_blank">📅 20:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79180">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Parvaz</div>
  <div class="tg-doc-extra">Arian</div>
</div>
<a href="https://t.me/funhiphop/79180" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@ariansongs</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79180" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79178">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بنام خدا گل برای کنگو</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79178" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79177">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oePRYo09MYFbMHmKyFDn1cEn9DaziG8-OUE-G62MOBAun4f8Ik7IGG0GyEe23ALF_IbA5_WmL0_vP95CdZFtFg95YKjui-ehZ3JIF0IzSSkCMlWn3NrwbZDU0x4YRoMb6llntkU5VUUCLrxpnYcDf2byeaqAKYgKEFMr4XSRaUCHgumVK1aVvSgZZ8-pM9U4tMgBtNCAjfhN055oyiMlREmBm0O9Mcq-lY0Vmg37yPDkZm6jy3XmjZK6Nh0ZQI4-xtR7NzX3eiTZeKT_vz8e3JuEqCSYkAO5QOhZ6MnpzmedI8zn7xfr9w2PzH65AM84Y6Tmx9FNiWkYamRRmcW_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال: اگر قهرمان جام جهانی شوم تتو نمی‌زنم چون‌ تتو در اسلام حرام است و من مسلمانم، الحمدلله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79177" target="_blank">📅 18:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79176">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3f4634aa.mp4?token=KpcjrsBtURBagfOOnmQpTcvGK7Tov5DMR6gi6zYUIifVgfk5nViyaCQTw-eC7Ws5WpY03i8lTNbgyfPajqcJiKzt3V0NKwg6mlQKkbN0VYaNQsWMdcFVZRwJB4fTeIcWEK98E65rwDD5ZgTWKqmREYdZMyBlvo5Q8PcPPHOMLlKMOXPhTdhZeH5r40v6ASjyeBUawnFYTSFBX-0xUVB9ft3T7Svzj5XHy8Tpmf4qb1sw1MD7eetgg3HQvkO7dd6GgDDDI6A0_A0fKOEAVDmbZ5OuHBDZp6l-QaQpMAvaP1ulhcmpBn1YOnuEAUN-dumXslFXpDyorTGMJfC8tgmXXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3f4634aa.mp4?token=KpcjrsBtURBagfOOnmQpTcvGK7Tov5DMR6gi6zYUIifVgfk5nViyaCQTw-eC7Ws5WpY03i8lTNbgyfPajqcJiKzt3V0NKwg6mlQKkbN0VYaNQsWMdcFVZRwJB4fTeIcWEK98E65rwDD5ZgTWKqmREYdZMyBlvo5Q8PcPPHOMLlKMOXPhTdhZeH5r40v6ASjyeBUawnFYTSFBX-0xUVB9ft3T7Svzj5XHy8Tpmf4qb1sw1MD7eetgg3HQvkO7dd6GgDDDI6A0_A0fKOEAVDmbZ5OuHBDZp6l-QaQpMAvaP1ulhcmpBn1YOnuEAUN-dumXslFXpDyorTGMJfC8tgmXXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارههههههههههه شدمممممممم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79176" target="_blank">📅 18:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79175">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ویناک فردا ترک میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79175" target="_blank">📅 18:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79173">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNkHtjZkoUQ229l-8Po6gabfb1aSKeZ3tSecEcZAtWkox33fMC0rnKj0tNjiVCP2w7vH-lzdk2VApRhJCqLWSN4y3Tglx6v7Ockvx0RohZZ1sJ8X2w_NETcuJAHWdf7TLfL0NZ2Z9KiF4Qq3Vs2V_PnCJFPnIK_tZf5vQ7Mo4VlhnEsO0qqUxWbBUCM0f8xJ5j_s4XSyAKPudzy7DdnxNUHK7eUk02-wYoeCkQnUmDpNSNGPRhYJbaNH60PoUGAbeg8WXiJVxcjdlKFekbX3f-u7kNyEIzXHPwQ7PXCCnTisTaW2Y0grKMhu6A2rW4vqIzdbmDpE_SCCoABkjbi2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHUhyf5NnuHwXL0CxGVIJbCkW-gTbwH0Hq7UvIt3bwBIhg7_kG_Qin-7fkCNJNdHaQuhq_fptmEV4g2Wx3819_4PlZWmEKhJ2F5tej5j6h9PiNnAG2Gbh5EbPszQXWnCHz-XzP6dNElxGTm8IBc89KuINWMhyp4rj5YMFGyuaMGwmuifw1wltp5PzjX-KbNSJrksaGn-pg7msljqInT3HD3k4O7znFKxl70XFdlN7b5eusAqDYPxr90kIkwJ51IRUtY2riPvUGV5TAKlTtq7Men4Yvhj-yEq4moeIsG9mg_R2r0X77L3DrpGwEfTmKaKmLUKQHfPeeINdXreWyyXoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خلاصه حواستون باشه عمو رو بازی ندید.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79173" target="_blank">📅 17:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79170">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqAglK_SXAS5UAlsbPYIyTdEchEowmz4girjv4uUwXgiNC8B77xygKeDe_okJ6rAbBmYLzjPj_FePy5n-kzhc5dUyXj6_qi2ytOmgbcFQ3ri_bkq7ItJ_2PXhb4Z157iOuby3F1gFbTIrNysHgUFOWUFCH44xAORzdzO9JdgIXHEUh6zwncGJJ7OXgFI67YvJGqlBU_wjRENU4zBvmxmtJPC5c_iVDzMiadi3eoUBVxYej-Gv19kiZ3kK3zwIlZD2GTwTergn7up_TO3U99mBI8Q0CQvzumzSf79JREEeb-Fxy2GSrGNFet80QI7wiKjPVZFeUgIUH9YHZWnZY8n-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4Ct28ftl0opmNLNMjizKQ9Lpt3Qla1mzz0qANgfDi9hEi4D3PYAAOZZ9uudwi50bFAAD5XQub_BovQjb_cgBcbzp7Y0wveughwmDZnt23KPfXAEnOnhSgxRXJ6tA-lnMDXXCGnNem4sIftn3a56tdJ24FXRbF8FyMGRganPzGnoX2BqGZEpYedQZ5wePArYvC7di0PncT8oBUHURIAge3DK5Ha8tbnEaPMWtKJIxtSjIxD_XbUS92WkjoJHHk0E2TS0xZCPeq1DlyO_7H9gmddXMBiKlIzQbnAulwiBeb74LV0cndwDM0ykfHuV8C25OgkkwhHwgL4rogM9l2blSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امان از این پرتقال فروشا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79170" target="_blank">📅 17:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79169">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO7UDViThw9XmpU96v8zWMebpx9h3Urmfo-zz4IyAgB82ijq7_zZyDb6c-5Vn58KlVlvsD-lljtDhPL9ylbK45J8M3UVKy5f6O7pbMjfRj1ZrPLIE0aga20eDTGYaLFTkxtO4hNs-ASrJwLjCKVr_pCwMx7xKqNHkNyWnE7mngxYgqbCYZy2r7uYnommKu3Hg6aKKyvhFjzMmLedo_BElLWZtYel3mV14DezlaC5Rh7nD9LGkRhqiDx-gY_oaKC00Xjn5pzFUp6ELb_P0c09U0OzIvq3p37c7SBvwGGawnjJPZ9A5sIZvEw4CHvqPgf--k8Hz-umFOpuQB7vqkxE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعید آساره فعال مدنی اهل شهرستان ملکشاهی امروز سه شنبه ۹تیرماه ۱۴۰۵ توسط  وزارت اطلاعات بازداشت شد. تاکنون از وضعیت و محل نگهداری این فعال فرهنگی -مدنی  اهل ملکشاهی اطلاعی در دست نیست.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79169" target="_blank">📅 16:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79166">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10d6b449f.mp4?token=Al5ltHpoJp0d8WZWkdkmWspcEoCBHF13Qd_79IP1EUcsxhNHkaYgbqfehW4j7ilTjo2--baKSmrzFEJdBp5qYKpYupud8_muMl9TKaKEqyv7PCgTo_kLsOCq1IhigzUNnem8AGhgvo1NEA44NaKKO8lvrRKbuCNAd-KmUnfsloYFNv0LAcCewpDq8pN0vsTWEwREll9CrB8cgEhf4i067yQaGvo2r_nLbF82_4s0uOcAKIKOGviQc6a4ZsYJBAB2QyY64mTU89Nwimt3yYu6fKS-yphZwckaD5AJgD5_wS0n4Mwhd7HZFF2BGN6NvROKUc1-qirEJORiotJVGO9RFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10d6b449f.mp4?token=Al5ltHpoJp0d8WZWkdkmWspcEoCBHF13Qd_79IP1EUcsxhNHkaYgbqfehW4j7ilTjo2--baKSmrzFEJdBp5qYKpYupud8_muMl9TKaKEqyv7PCgTo_kLsOCq1IhigzUNnem8AGhgvo1NEA44NaKKO8lvrRKbuCNAd-KmUnfsloYFNv0LAcCewpDq8pN0vsTWEwREll9CrB8cgEhf4i067yQaGvo2r_nLbF82_4s0uOcAKIKOGviQc6a4ZsYJBAB2QyY64mTU89Nwimt3yYu6fKS-yphZwckaD5AJgD5_wS0n4Mwhd7HZFF2BGN6NvROKUc1-qirEJORiotJVGO9RFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی صبرانه منتظر ترول کردنت هستم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79166" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79165">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHFWHO_c6ognm3dTYDUGA72Z8c0aCtZfpHZkzOghao_Wxmtvta6BdG6biQBUg9FzRtBMIJJQ9MBchYcODrXOJLaAuPX9cwY4QMRsONjRf9jp0ExiGW26OPnwDhEt22KqaFLKA85_WKAZrLfE0jjcScd4NJ4KWBUQjL67M7808u3QXiURxTcbmeh07MpemqaSOtMT1PV5ac7V00oZidK1C0HA06mvShGVnv-MzWLVSk6fH9ElqOKqz61y2IVuCIrJz1fnNQORFielFk-JiZ6wqdKL28HXWrvSBY13ZEVl67oMyLCeb7lzt2lOQqT4F98izkThQieMQfHjDq8LOwDAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79165" target="_blank">📅 15:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79164">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وضعیت جوریه یامال مراکشو بعنوان تیم ملی انتخاب میکرد شانس بیشتری برا قهرمانی داشت تا الان که اسپانیا رو انتخاب کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79164" target="_blank">📅 15:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79163">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بازی رفت بارسا و رعال تو لالیگا افتاده ۳ آبان تو نیوکمپ.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79163" target="_blank">📅 14:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79162">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ترامپ درحال بررسی بازگشت به جنگ تمام عیار با ایرانه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79162" target="_blank">📅 13:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79161">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تو زندگیم اشتباه زیاد داشتم،
(یکیش ادمینی همین چنله)
ولی هیچوقت عشق ابدی ندیدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79161" target="_blank">📅 12:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79160">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6094ff0128.mp4?token=baY6SMQPlek5mERuCgXQvJqlD5X2E3KFVHp58CxaIrua34mKAeOa3TPw3xtOtfD3yq0xgB-l3B6EdqpCTWvILhlZm0E6gh9aT7x6iZ050KMh1ZRLcmy-vv3oChwxZRhZ0G6tHq2pgoRBJ-VsoMkNTv6WzTUchTccIqkqir53Fcfo0Gwny2is_caobmz1nzlo16fgs347u61zcmSzTcuw-lltmJTTmPbureJb2reQq1fqOLGATRNNm7--k_9JHGsDJ4OCKuOVZUJ1hMnzTnZsfuqE6ayZH2uParCUn0CGG-pvXe6k24I7moQnZNAkuU5birgeG3p0hvhf39B1MHhZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6094ff0128.mp4?token=baY6SMQPlek5mERuCgXQvJqlD5X2E3KFVHp58CxaIrua34mKAeOa3TPw3xtOtfD3yq0xgB-l3B6EdqpCTWvILhlZm0E6gh9aT7x6iZ050KMh1ZRLcmy-vv3oChwxZRhZ0G6tHq2pgoRBJ-VsoMkNTv6WzTUchTccIqkqir53Fcfo0Gwny2is_caobmz1nzlo16fgs347u61zcmSzTcuw-lltmJTTmPbureJb2reQq1fqOLGATRNNm7--k_9JHGsDJ4OCKuOVZUJ1hMnzTnZsfuqE6ayZH2uParCUn0CGG-pvXe6k24I7moQnZNAkuU5birgeG3p0hvhf39B1MHhZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرم معکوس با فان هیپ هاپ
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79160" target="_blank">📅 11:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79159">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7R_NLexBOgSSutGhdaP2Te0LiekXGC2rRKbOBXpUJ57kb5nr2sU6MzaEghxVfPtEmytBE-xAo3cgH2cbH_NTzQ613Kaqnx056SzgVpAo_yFQBSVIZLkpeGb9iebgPU-HrGZAwnrMWy6zTG7mtunXgqHP2SzQlGU4fTiQF1_9oVGerCASuzlzyRVEDnwQ19CrW9iGDj1g-F-llKAeWPMb2cqapbL8ww4Jl2yh9HQHBZhUU4q9v2XduXpjTPX373unPhtRxmfacp03Re1EsgnZAiLBrua2Cr_Yba1b0P9yEfilu332DItHmqqOPcIzE640Vpqc5-eseV8RWpbG-CVrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت صندلی قدرت تو ایران
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79159" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79157">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">۰۲۱کید تورو خدا یه کصشر جدید بخون هرجا تو اینستا میبینمت داری میگی "فیفا ترانا بن مای فلگ" خسته شدم گاییدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79157" target="_blank">📅 10:51 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
