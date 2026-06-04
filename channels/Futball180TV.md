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
<img src="https://cdn5.telesco.pe/file/Q9ju-4Oqm_lw00WxzMmgyUZk5Jeo7lqM-ZDBghPgnkcQWI0S48yKFphb9NmxOFi88r2_UaEqKM89SrnTAi7_L5ZIqO5WAXulhtSFVz5wbngaf3myJMBLnXeYRQWGDnYk98crWjMW_aCUeUc94BkyQsqfCMZbdsm34RsaKsckLMqk7Dk8VjOWkb0k73uxK-41Z93f9YtyyfKeDvICh7BOJyawxI8GFNyuoJcneqpCK03vtovT6JbQm1GrpYjPARbPskhMv9gu_zRSL0j1Rz_tLR379R6RxKwbmqyK3tjrjr6LHyKCe0a8XriGEIaiL1VMakWOSi4HRvzJiI24b4pd9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 176K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 20:17:37</div>
<hr>

<div class="tg-post" id="msg-90922">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2ecwLDiiVVXe4b3BnEKXn2R0zqk17c0XtikQK7BZqqnORor4QV0JPhoe1zMh3FRxKB-iw6nP7Oq1SGQYHDhLavWlw7l2OEZ_WQof70tn121lHzhK4X1IiNaaLYbI5PeyIq40OrmvzeIVcwu93GHacyTjfXngffYjSy7Sf7jorYLVFpi6ZouJOPA_3MkwL3YERf7VCX7B8jkEipA1ypxq03uo8NBdKARxNqa-IPY9z_tggVXO8lZTHEHHon7CikQpw3qpsc1sQ2LlYRXi7Qb13jtHRHb-dTW_rbtYemFvhb335BCemTj_vSh9gsKYZk5sJwKr3nuZUeWvpDxPjarpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔟
بازیکن برتر زیر 21 سال دنیا در 5 لیگ معتبر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/Futball180TV/90922" target="_blank">📅 20:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90917">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9qIbISXkPJg03gu3aKR9pLEaDDx-1_WGfnopdO23ZooaIOA_WPB3pkW_ZCC_M5-_is_0u0JXvegjS5CytEh-hLP0BMDYD4O1VhFXQ20FJwRi6-K6_c03u16a-qKJnwvO0lfXSUpkXVJJwngP2nnDHZH_OuQySqJq3MiuJcUmWrmrk8bz_Gwd053-fHerH7RckX9DreSM3uMndYR3qD0ox4VY930CksZavULht_cfDDnB77nc2tE0Dew-n4iuhhocd3-rXeAUJMfLNu9ZnC_3qF4gm9yTd62H-52Id0YZPSjPM01x7hOoV0fyWZWftvMDzh19lnNo9EJrvZ43JnTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب تیم فوتبال ایران مقابل مالی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/Futball180TV/90917" target="_blank">📅 19:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90916">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad596a5f1c.mp4?token=PjwnOlvtnVsR5y4lZmpfaUqu-T-I7CHyBOxPTp8K5m96wnNxf_e8AkepP2MYWobwqU3k5HFHbnuChGkw-L6VoKXuSNjOkHeocU_vixvl75LvhCVUuZdYO3mvJNsMeGFdjWyp3V3CbzMimZgPEYvAf9tOfelaHh-9tT_E6cVP7xqSQbpEM7s3jQVh5BwG4_fg4zBln5eOQU2pytS93clxKFQGrS_Rp3RQ1niM4f046aQ06WzXK4WFBhkOdCvUoDxSMLnc_OZEdpf-3TzHtj3H29uCzl4BBLdFOxEsKfzVT3oyU1uuamNNeaUkrwkldzKuggl1DrLaUSY0h321xdwP2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad596a5f1c.mp4?token=PjwnOlvtnVsR5y4lZmpfaUqu-T-I7CHyBOxPTp8K5m96wnNxf_e8AkepP2MYWobwqU3k5HFHbnuChGkw-L6VoKXuSNjOkHeocU_vixvl75LvhCVUuZdYO3mvJNsMeGFdjWyp3V3CbzMimZgPEYvAf9tOfelaHh-9tT_E6cVP7xqSQbpEM7s3jQVh5BwG4_fg4zBln5eOQU2pytS93clxKFQGrS_Rp3RQ1niM4f046aQ06WzXK4WFBhkOdCvUoDxSMLnc_OZEdpf-3TzHtj3H29uCzl4BBLdFOxEsKfzVT3oyU1uuamNNeaUkrwkldzKuggl1DrLaUSY0h321xdwP2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های فرانسوی میگن دزیره دوئه و این خانومه که از قضا بازیکن تیم ملی بانوان فرانسه هست خیلی بهم میان
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/Futball180TV/90916" target="_blank">📅 19:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🔵
✅
تایید خبر 3روز پیش فوتبال180: تاجرنیا رسما اعلام کرد که با هیچ شخصی برای سرمربیگری استقلال مذاکره نکرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/90915" target="_blank">📅 19:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAqmtTJA2_bfZdBEQSAoZAKWdrJs74Q545UPaR6C01U7n1lZydnD7TauIwg7I_EIRsINhfgsCjJlI4cVciYiv4Tjrc90zJI1lOmJD87guEyyUtPA_h6KnJxVGDXK6MVDGoGYsPUPXIf7SyeXCjmep14fd97VRgeYcmW11p0aNROGlqQYTR0XHfl7OEymDYvkhucvzd15e9dmxXP8t8u0pJEz9FR4IkUSyJPbLnkvqbARdj_CfXIslXa7WlXBq6yxyfJgy4L9wfEXyC1pwpyfcncZsFtVfAs--_NzNWJT6B4PUYO6Eu7cbjJusFzkdHLrS-XNY-nUR1mrBZJ4mFYmCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180؛ #فوری
🔵
با نظر کمیته فنی استقلال، سرمربی فصل بعدی آبی‌پوشان سهراب بختیاری‌زاده خواهد بود اما برای این مهم، یک پیش‌شرط مهم قرار گذاشته شده است. اعضای فنی استقلال به ریاست تاجرنیا از سهراب بختیاری‌زاده درخواست داشته‌اند که یک الی دو دستیار…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/90914" target="_blank">📅 19:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90913">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH6aGj6ZomxR566cAMSnB8Zx5hcDU2EK9NarniXXjO-U4x31SZ_SXWQKWLI5uf9rOO21cuQKye87sE_cSCgzPz4nujatAZH0MYhiAKjsf3kHDJIaQ_JN6uU70FA1EdcTKWywExfvZxK7L4OZGG_cMj62N5SewmaZmNU9L22knTdHZ7T8CvNsrtaGlqQFnIwAXQAtSdyWzwbu58t4s6AqcNfy_JRTlVrWrPb36bEByvdsQnA1KwePlktaTEzeBgAYdhJwtNir1bIEghffzN0AHGroFpiaY6k4AqecSZqOZlpL7skU06A1ogqknizGmZQwtkW3Upt7Zuuc1bOTsR1LCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری: بنفیکا رسما تایید کرد که رئال مادرید بند فسخ 15 میلیون یورویی ژوزه مورینیو را فعال کرده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/Futball180TV/90913" target="_blank">📅 19:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90912">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZlcz2jkBIvym6eQsC1XcYb4pntS16nK5HMiRGrSkhbJo0woG3v0vvOfFkPKnLhZ_ndNL3_B82iKV3I6VEkpJIHWAUaU5u2REzw7hbB86H4kxNYEy28sWtNfQX4gME7Nn6uinELzotnRvO9bBGlcZMOCKFHkgLdXUwflqfiiX0STSRS6VszkW-zKnWxgC_IAvz-PwspETUmsyK3V-Ik2BEIz3KPayMbCGvsghRQ4KBqo3PcT3jsMaLe5Lx4GDXMOsg0dewy23gftRnzA4gOjebVCx2rtFGRzcKFcK5aX5sRyXv8TyOAazu2V6hTsxLJ6jpl8qVoz5Zs09i_i3gAvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکلاسیکویی که فصل بعد قراره ببینیم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/Futball180TV/90912" target="_blank">📅 18:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90911">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjBeXBETa0dLzQ6yKPBokqxBx_RaXlQ0apAVzj77n7g6HQoLKSFB-LKn7ecgdiSJP3q8UZANAXOElUk7PjHiNM9Ou8jLw2Y0RtsnOauqbvgzPXNk1Yb8aOWnaSZmk-gyPuhnM0KHP8wU8C1m3VfF8mHybGJs4X-GTM7lYsmt0uKIVWpMV5w1S_pgQQWVXVC5gk5PRlHGQaccdDV7_rbz85MJCC174Nz2r4in_pzR5z70Jb2bjE6hczUdB_F4aUHY0vb6XTtp2I0qKt-6WN8IDR4wbik1S4Gu8XXigi2-IeBLPdcVuGGY8H28XyLku-xQdU3e1HfFQXg02Cadu1pzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇫🇷
🥶
وزن عکسو تریلی نمیتونه بکشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/Futball180TV/90911" target="_blank">📅 18:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90910">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJRzL2fkmSKP36Gc6O3SMnkxTr8FukusCdjg0GTgUuQLXBPjmJoi7JfcxKimAX9wJewDkxcJIVfAVWy2ZSVOuCCqRf3Ep2qhelqFJsOTPOH2apCceRdmJ1fR_BZ_73UGnvavvN0HqsCna1opDFcD9Ck6PlS-Ew14sgA8yAa2nFhvAvOyaiJsgNUhsE4y4lJt2x7VAOy5JNntavdTy9wznuK-srxtaC81OZy0tHAf_1CdZc43yysmtTnonMMpgSnk85B27v4TTRUNTzRpWJMX4gxR6OAN1ea4gB_NWXkJPs4tWKFN8uohf8ov-iM7R1UfB6gmIWL80mjAdadouIQ1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
خوش چشم کارشناس اسطوره‌ای و حرفه‌ای صداوسیما: به نظرم جنگ تموم شده و دشمن دیگه تخم نميكنه به ما حمله كنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/Futball180TV/90910" target="_blank">📅 18:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90908">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfbdfd3dd3.mp4?token=MWr5kcgfPp2kMBMx3Sh__dPHNA4dmb8iF6IyQ3Y3vKq1HG0GK9Ul5V_dV9KGiMCBYq86MaXPGdvS4Y0hg62TCh9qXt14ZEMwcoNKeVNXPpyvPI0vra9M7VFxXhzJpgqf17xvubyypbqy3I92l-wALS6vRm9vML1MFTMHuGa26GG2iJQfAZbxC15KT6sKdwPCYxBphsPlmRnL5XwUyrqYdgeyQH1fADrJATURAe0FQOPqjaIn890veiqHZH-8WPGZw0qVjtNB_UZDoSFpbA6KmJfwJKtxHgGeUpbF6aKHzwlYd3K1lZXURQ82NLUFmzgT9787gJt36fV9jQ8aLqqqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfbdfd3dd3.mp4?token=MWr5kcgfPp2kMBMx3Sh__dPHNA4dmb8iF6IyQ3Y3vKq1HG0GK9Ul5V_dV9KGiMCBYq86MaXPGdvS4Y0hg62TCh9qXt14ZEMwcoNKeVNXPpyvPI0vra9M7VFxXhzJpgqf17xvubyypbqy3I92l-wALS6vRm9vML1MFTMHuGa26GG2iJQfAZbxC15KT6sKdwPCYxBphsPlmRnL5XwUyrqYdgeyQH1fADrJATURAe0FQOPqjaIn890veiqHZH-8WPGZw0qVjtNB_UZDoSFpbA6KmJfwJKtxHgGeUpbF6aKHzwlYd3K1lZXURQ82NLUFmzgT9787gJt36fV9jQ8aLqqqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو زیبای حمید سحری از اخرین جام جهانی دو گوت
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/90908" target="_blank">📅 18:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90907">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laUEZQW0mFK7rmKL7X68rHk96rL79o0aTD1cJRG_kQB1bHD6QPOI5uw3sNMqULR6cXmKFLEKO_ySJpNINbBsh8dexZDcskgzJ2U0dLzhcu3JmeeHcyZThYTKrmOcVXZmFgHxTjAkZlWZ8NFhaG4vn9C4lMEDpHUczjB1Rs613gRELVGf_RxKs7b5XPKiasyhPL950C7GGGo6SKbHaImQPONI2N4rsqUz8cKRblZT8AzGoQyp9qu-GXus9vPyJWVJl28UwEti3jkhGOcIHMhizi3W9di1aWt9booBYYt4blXZk9eJKN8_qagss6vaZmSdk_zik_0W3xFQeUr-uy-Umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرائولا رسما قراردادش رو با لیورپول بست و بزودی توسط رسانه این باشگاه اعلام میشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/Futball180TV/90907" target="_blank">📅 18:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90906">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXQ20yjmACcSkZxmEGvAzxwDUAGQfD5s_YgY3MyDW7qqx0w-R9gVChPYPXVtC8Bu4nw_RdjmkicmPwbe-1q1MejFHdaLP2rYiYbvZaLPqnolcIHycH_sx7tTZPkJFiU3ecna0e6DFhRBH0EZBnk0J3Mlp9F_Q4Os1X_ZDZoBT7sJQgbGighry1IIFKQWO5nn0bXxvYA758kRU1mpTR7BMVsq2YvN8X9XHEU2ZE4hWU_Y5JnivYxsuoh5MWt0Z7hGQTjeXdQO8OiRB5X0MqqyOLIWFMBfuiJIg_dR7VGwyBlAte0Q654mqkvBQmdzcwVhtMM_6DV5tAZzUM1gkWLMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕
️
🏆
لیست شبکه های پخش جام جهانی در ماهواره یاهست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90906" target="_blank">📅 17:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90905">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQeoov3KZ6R2cHkNwkrseMUmHQZ5rBqwcnr56KKot-N92SnEZhal6to40JOdXSTZUoW1oubWIiqMs5IGzOdf8mQ7WoeU4Md6TBPNqznmAfqZlxiwBuK5d8c0dASYb7RcUgrkwO6LiOsIQQN8K-TPn0ZpBuWMKXa1WpIQ2DVOI5SFp9BqJBPWIu-MgFJbTtpiGYPt_4MY8Uj1XyJFEu8cLFZiCOFLDU773CcmjHselU0Hs7zAOkSefzTUYNBVBm4ZtFp2i0RFhgI-JQmqLOiIkqfkIOmmP5_hQw3rA3YTaDfbEnuGCfJU3t-1NB2WDd5_PFOhwvIacTTOIbGgdsktAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕
️
🏆
لیست شبکه های پخش جام جهانی در ماهواره یاهست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/Futball180TV/90905" target="_blank">📅 17:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90904">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e1409299.mp4?token=U5dxOf8Y2quHfZrQkAa04I4saQ8T9_JTVrHjbG9T7k2imTestgj3e6NkVub7KP26oagrjHrPTCs4sPcbFoZyQQFfzm-4VgloivBsCVeyz7CWqynRRQ7DwYkB_WDxa_HsKaya7x3mzwZdycNcMHD2r1eIhkR3PaCYunX5hkuQ_atG0T4tdlfoBZ6ATDM8ZsCTsWOJxsDo659qzRQAKnnPbruEfdySon8Jv99771K9lmqylfbi_VzU1LbBTgTe8HFN7nxEkXoOB_lBK-mnyPcqK9fQ9EX-gncWH_ZzlJzm4tCio-5atrRPlQPZxwe-_5EA1ermZoG7SohSm5pv4DMGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e1409299.mp4?token=U5dxOf8Y2quHfZrQkAa04I4saQ8T9_JTVrHjbG9T7k2imTestgj3e6NkVub7KP26oagrjHrPTCs4sPcbFoZyQQFfzm-4VgloivBsCVeyz7CWqynRRQ7DwYkB_WDxa_HsKaya7x3mzwZdycNcMHD2r1eIhkR3PaCYunX5hkuQ_atG0T4tdlfoBZ6ATDM8ZsCTsWOJxsDo659qzRQAKnnPbruEfdySon8Jv99771K9lmqylfbi_VzU1LbBTgTe8HFN7nxEkXoOB_lBK-mnyPcqK9fQ9EX-gncWH_ZzlJzm4tCio-5atrRPlQPZxwe-_5EA1ermZoG7SohSm5pv4DMGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازیکنای فرانسه وقتی تو جام جهانی به سنگال گل میزنن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/Futball180TV/90904" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90903">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ab6aa38c.mp4?token=UVNtp3FFuqn_U6PROxuPv-KQIkjB0A6ykNeKWB_O-fYViG-zdWdO5bqTP1pt7jFPZWlJRkbN1ZgeF27ZjW8exuPQjFa3tC3x062E5MoESuR9nXltnlrigWBFF6PO9rNnrFCP98LYiVw67fCpEWBCA-EkShlD2S2w-Pp9cuvT7XP47cXJED1pBK84x5aVyNqBQsZhwijdolTfCjgrYUyN1e9RMx3cPMOApFeElxMC5tCSkS8tpFaKQRxTPhlqUvBxuBMu23G5erZ6Ew_g7rtvTbR-g-zOgPrPzJHsbHXbK2i21_52BGjCpcW9X48rzOXewK5ejrsxaahxfdafV5q-9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ab6aa38c.mp4?token=UVNtp3FFuqn_U6PROxuPv-KQIkjB0A6ykNeKWB_O-fYViG-zdWdO5bqTP1pt7jFPZWlJRkbN1ZgeF27ZjW8exuPQjFa3tC3x062E5MoESuR9nXltnlrigWBFF6PO9rNnrFCP98LYiVw67fCpEWBCA-EkShlD2S2w-Pp9cuvT7XP47cXJED1pBK84x5aVyNqBQsZhwijdolTfCjgrYUyN1e9RMx3cPMOApFeElxMC5tCSkS8tpFaKQRxTPhlqUvBxuBMu23G5erZ6Ew_g7rtvTbR-g-zOgPrPzJHsbHXbK2i21_52BGjCpcW9X48rzOXewK5ejrsxaahxfdafV5q-9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفاع های تیم حریف مقابل فرانسه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90903" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90902">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCOdbfrkQZcCPsuZF7_zSaYhv037Gki8CWhEYhQajqzx3fX2m8M_Fbjw_vronNJ4oPLxsrGBeWfAajaRusiyy56s0VXvIlvT0KKaLlBTfHzlgp9ve-BQKvwe6YX3rkAKfJNUa5_8dweah_Sg2PJgMuf-ZfTgM6-b2oppUN6Bvy4YF_DfdeBKp14qpN-isv-_UgneUJaP61wk6aTynb_dkDujgB73vLZfcTQLhn_vxav4uIbmw9agvKySKx9fsPPOnfE7XTBUinXXO6Kjozb18DNovjDrkbfBjGoxA6EUnMOv0GEU9E2b89tW372KFapky0qiacKqqFkOJPs1gOCknw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/Futball180TV/90902" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZnxL1njXk8RyJACnn8B-tG6Otcq0UWIa_Kp3zx6Gcr4y-ChJ7IRC05VibRE5Q2xbq9dPIAi90E_kAA4RshQe1xUr6R49CbLMb8axDzaKiQ5IQRBbSKQAEM4qntRBWZOY3ogwCwxpKt3FNGcLjt3pGIOOGzJqmWqL2ca8OG2aiO7WJqqGf1hIFr2x6UNXP0CTWUwM9oQTx6zJQVLvYCkSkZIU_MBNmbGMIQS65-MsN9GBQO6hfuHwrtZqtsIdT6kDlgl_9ojWmC9FezvhutC4vWskhUBRsMPkmKmCnmO0KHrqDig5h7oPukwc1K_j5ObS_GKO73aekAfHlN5r-4FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Out Of Context Football:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/Futball180TV/90901" target="_blank">📅 16:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1ebbd4911.mp4?token=PPQ1FwURlPksKxxBvw2i6fQeDmhz5sQPDJLar52w1iM8Tl0PLmx-8Iu-YyNos4B6oZ04eMt9Ul1li8azEP8pN8oDdC-uOJ905ICJUuamYhudG4fD5FvTZ2JVHpCDd8gBQ3F83s4aDoDY-ElNK8PNVsECCq1EChwwjdrSjQ7e0_w6l-Wbc9Xv4PXuDW3TYjpKfXL8zIUZ-F9eSsW2cxSo4TTv_t6T0vLNsC-BVV6uKbbV1dL1gVhYAbIpBgpn27RfTy6_u8a151D_nMGekZUsUrdr2lzceEHRRis7iOML0R7aonojNKewki_yywme1o5PNvFrLtjnYijrHfsshNz-ZWkTY8YPrXtmZEEbsorYu-kKnoGdj4MHlF8kR19Htu3z3bS5bd1u2ii10i3ObJE6Xeoc-52AZjSxL1a-JNWRfuvMHOSW22DEQ2TYqE9V7Hi65CmeFnskhs_5keg_y3m8FVXqPyPx906Mr1xI0I0YxS-_A8aZ3-z2ib_aTaWiPo8Sg3wtOjYamKaXFSD9MOA6tH3fvllitCD4TKWyEER7-2OsVQo_lXiSxGA8GJN_at3_NFYcCklr8FrqxGJpmjVoHLAplNQDTElKAwpUExH0XESJ911bu92JEctwi_pzhgahEVDWi2zCwW3hjqkyUKlKVx9JtdRaIjfJO6ILYGrv2ZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1ebbd4911.mp4?token=PPQ1FwURlPksKxxBvw2i6fQeDmhz5sQPDJLar52w1iM8Tl0PLmx-8Iu-YyNos4B6oZ04eMt9Ul1li8azEP8pN8oDdC-uOJ905ICJUuamYhudG4fD5FvTZ2JVHpCDd8gBQ3F83s4aDoDY-ElNK8PNVsECCq1EChwwjdrSjQ7e0_w6l-Wbc9Xv4PXuDW3TYjpKfXL8zIUZ-F9eSsW2cxSo4TTv_t6T0vLNsC-BVV6uKbbV1dL1gVhYAbIpBgpn27RfTy6_u8a151D_nMGekZUsUrdr2lzceEHRRis7iOML0R7aonojNKewki_yywme1o5PNvFrLtjnYijrHfsshNz-ZWkTY8YPrXtmZEEbsorYu-kKnoGdj4MHlF8kR19Htu3z3bS5bd1u2ii10i3ObJE6Xeoc-52AZjSxL1a-JNWRfuvMHOSW22DEQ2TYqE9V7Hi65CmeFnskhs_5keg_y3m8FVXqPyPx906Mr1xI0I0YxS-_A8aZ3-z2ib_aTaWiPo8Sg3wtOjYamKaXFSD9MOA6tH3fvllitCD4TKWyEER7-2OsVQo_lXiSxGA8GJN_at3_NFYcCklr8FrqxGJpmjVoHLAplNQDTElKAwpUExH0XESJ911bu92JEctwi_pzhgahEVDWi2zCwW3hjqkyUKlKVx9JtdRaIjfJO6ILYGrv2ZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاراگوئه هم وارد چالش معروف شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/Futball180TV/90900" target="_blank">📅 16:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvulhqin7OwujodyuJcq9vNd9ZCLUzqTfwylYvSKY7NCGfqUqlsUTHPRPKb1b2H6aRfO30-pFjwy0NoOYbh91P_2EzPaRDaVhMYhTSpcw-Cei1L-xd3xgrQteL7E9wnN62A3wUdaabW_7Jynq3k5w6bePk1iu7Vj7wEZ7X4DESh9yWM-bBIJO6agCh3SJ6anABz7Wituo2xgZDq7khxk6I5m5lNyxEqYTOugKR5VQF6NOXNaY2Q60ysfaD2raj6HqrAX7ldq_Rlbex6OGGOFfrznE_wnNCIKp1-dJzoDr8pTHBBF4gy5qeNM-yXr-VJOzlqpBac9fI_f_OOf_iZ7Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
👀
#دانستنی‌های_جام‌جهانی
🇨🇻
فقط یک یادآوری که کیپ ورد برای اولین بار در تاریخ خود به جام جهانی فیفا راه یافته است و چیزی که این را حتی خاص‌تر می‌کند این است که آنها دومین کشور کوچک‌ترین در تاریخ هستند که به این دستاورد شگفت‌انگیز رسیده‌اند!
🤯
👏
🇨🇻
🌍
کیپ ورد کوچک‌ترین کشور از نظر مساحت زمین (۴۰۳۳ کیلومتر مربع) و دومین کوچک‌ترین از نظر جمعیت است، با تنها حدود ۵۲۵٬۰۰۰ نفر، پشت سر ایسلند، که به جام جهانی راه یافته‌اند!
👀
برای مقایسه، هر ایالت در چین، آمریکا، هند و اندونزی جمعیتی بزرگ‌تر از کل کشور آنها دارد… با این حال کوسه‌های آبی در راه بزرگ‌ترین جشن فوتبال هستند!
✔️
💥
و این اتفاق تصادفی نیست! کیپ ورد سال‌هاست که چیزی خاص ساخته است: دو بار به یک‌چهارم نهایی AFCON رسیده‌اند (۲۰۱۳ و ۲۰۲۴) پیروزی‌های معروفی برابر غنا، مصر و کامرون کسب کرده‌اند.  بازیکنان با استعدادی تولید کرده‌اند که در لیگ‌های برتر اروپا می‌درخشند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/90899" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3257da74ef.mp4?token=i27EqXvqWBD55WV7s8WClOyyNhPRhK37lNl4TYcQq_XjV5UCZN5SlpP392GFTdtkeUz1gf5zbmcwY6EzOPj9ghej3ufKfBu9Wn8L0sUzxYMLjzynhqt8kWZ4912brTFH_Vpp_DeuvXqaknX1KjhB6TsIhEaJi0blS8jPptmVtCUDHclHn6mOo-Sck0agw1sLJhE7sx7j7m5Qa2f2QdnhcPlYqfJ26RsW7znSk9hE44lg5p_FUuA9waIWPiNdkIyg2E1J98rUbOzFs-1m7sU1TD5KLSj_XY5GdubfIuLFmg7eot6sCnDPl4thngJGQrgTeGJ8o5CrT9ZYB2krfz6gZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3257da74ef.mp4?token=i27EqXvqWBD55WV7s8WClOyyNhPRhK37lNl4TYcQq_XjV5UCZN5SlpP392GFTdtkeUz1gf5zbmcwY6EzOPj9ghej3ufKfBu9Wn8L0sUzxYMLjzynhqt8kWZ4912brTFH_Vpp_DeuvXqaknX1KjhB6TsIhEaJi0blS8jPptmVtCUDHclHn6mOo-Sck0agw1sLJhE7sx7j7m5Qa2f2QdnhcPlYqfJ26RsW7znSk9hE44lg5p_FUuA9waIWPiNdkIyg2E1J98rUbOzFs-1m7sU1TD5KLSj_XY5GdubfIuLFmg7eot6sCnDPl4thngJGQrgTeGJ8o5CrT9ZYB2krfz6gZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
رضا شاهرودی: علی‌دایی به مادرم فوش داد منم باهاش دعوا کردم
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90898" target="_blank">📅 16:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb836e7b3.mp4?token=qo09oWIUx1v08m4CD4KeT6P1HwwG6RR3ogmbISu74Eu-mGNpiquRA5CzcLWFUGUOPM6_ogJyKNbFoadja47bE50vAVGvvgS6VIaJXvmHXPelApLa3gKDhWTW62_kHMbeSL0l00gkvOgqq_brmX3v40UHDdFtnbdMbYvbx7Z6uOKlUJDh5EX8gPHKN75zpT9s5i0mQ-6iBVjuNtd2C0Gnvu0Yh5khtGz6cKPicRWxOCmJmF_PceEZpUHNyvxgxhw9qpLMe54dCVJfnx9IsmYGSU5dLvX2D0niHi2npDR1l2o_NPKzGHO-s5sRrkHpI3r3netqzC9bp8HVaeX1nGKCjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb836e7b3.mp4?token=qo09oWIUx1v08m4CD4KeT6P1HwwG6RR3ogmbISu74Eu-mGNpiquRA5CzcLWFUGUOPM6_ogJyKNbFoadja47bE50vAVGvvgS6VIaJXvmHXPelApLa3gKDhWTW62_kHMbeSL0l00gkvOgqq_brmX3v40UHDdFtnbdMbYvbx7Z6uOKlUJDh5EX8gPHKN75zpT9s5i0mQ-6iBVjuNtd2C0Gnvu0Yh5khtGz6cKPicRWxOCmJmF_PceEZpUHNyvxgxhw9qpLMe54dCVJfnx9IsmYGSU5dLvX2D0niHi2npDR1l2o_NPKzGHO-s5sRrkHpI3r3netqzC9bp8HVaeX1nGKCjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇬🇭
حرکات موزون و عجیب کی‌روش سرمربی غنا در تمرینات بعد ریدمان‌های اخیرش
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90897" target="_blank">📅 15:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guzzSlEWr6yxK9YELKj47kNGpoism0ll__4FC8c-oZarMMQt5SapUVDUcaYNcIeg8Qord_IYpLPePhTrWjWZU9yB8id6KhC1bxQdIkiNevx1ZpVDISw6hSdtyStE7OUPK-EBlsv_4tlw9gwwDfMN0spFElsrkP_6FOaLTMc-OTqpz0oNgQtVQxha0CC7VYykcQqdcQvg8X32Ui5m6y0w7H4DzW-_EX4SFtIWfJdS1zjUCC8sUMd_HW_iLk7U23RANmfJ_twTwRjG0SMB7iXkutno5RUGDUCppgZtafMhR8x_YtaSO21AOjdA8Q4-quIcDwjWR4ZcPnrSH2mZtT4T4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه ادوات بازیکنان نسل فعلی فوتبال و گذشته؛ واقعا نسل‌گذشته چه کله‌خرایی بودن
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/90896" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49121b221.mp4?token=kv7YA0_ioYwznGAGL8vZytJMOSHKqrIZbxDLqTIvApJ4fYcneaHal79TdwwwdSD7NyMm5kl_X5QLt1NswqfMIsdYTyG2d7V7Y9RTwlxQTCp4aQnr3hWyVe_y7MfztiuOxTl2HEOzUOEEYFjT-5SXOAphkOP1p-c_PhcIoYgvg809eUNsY3SPmwp_kdNTcXT9bHTarr2Mi2u10hjQ2exuW0Nlc3Nl5vJvpFDHG84BNdYbUbgx7FbhdCXAGBofv7GOao66J4G_6PMV1DwMAamb7LpWEqpGzJSBh1k7DG_Tx2KSRVLqpnj1QkJTQXVSP6aXp1LI9PApRgux8owSStO-8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49121b221.mp4?token=kv7YA0_ioYwznGAGL8vZytJMOSHKqrIZbxDLqTIvApJ4fYcneaHal79TdwwwdSD7NyMm5kl_X5QLt1NswqfMIsdYTyG2d7V7Y9RTwlxQTCp4aQnr3hWyVe_y7MfztiuOxTl2HEOzUOEEYFjT-5SXOAphkOP1p-c_PhcIoYgvg809eUNsY3SPmwp_kdNTcXT9bHTarr2Mi2u10hjQ2exuW0Nlc3Nl5vJvpFDHG84BNdYbUbgx7FbhdCXAGBofv7GOao66J4G_6PMV1DwMAamb7LpWEqpGzJSBh1k7DG_Tx2KSRVLqpnj1QkJTQXVSP6aXp1LI9PApRgux8owSStO-8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
شهروند لُنگ پوش اصفهانی امروز کف زاینده رود: بنده را به ریاست کل بانک مرکزی منصوب کنید تا مشکلات اقتصادی مملکت را در اسرع وقت حل کنم
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/90895" target="_blank">📅 15:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90894">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👍
از معدود خبرهای خوب ممکلت اینکه پس از ۱۱ ماه آب در سی و سه پل جاری شده و مردم اصفهان بسیار از این موضوع خوشحالن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/90894" target="_blank">📅 14:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90892">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6039725c3.mp4?token=KQRncou7pudzOefVGTT7Hnfovt-iQrm6X4lgDTrgC4vFMFVhn4eVeQKgfVJxuLd3dGWx8lXiSe-NYD7XVwT7pvDbppBifXz9dgC2Bq_MIg-6RY75uGGhXdyhBIKXWC1gRUdU8Ps5GYS54Y6o_jI3MEWzwNlqvfUSrK_X_GNgO6gEDFvM5-eV6DWBE9zxX4FLcTVREr3cD47-df2wmsnzPWf51vvcYAj0OMREy2ONdZV9su4TL_-9GKoWX-vGIbGpCNU9QW7Mn7sdif4doiDOyRreHSVZwAv67EqQ3VaK2B4n_eAFNjV5lgX7cjsR0MorTMD_fiFnBEW1iwV3jc_VhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6039725c3.mp4?token=KQRncou7pudzOefVGTT7Hnfovt-iQrm6X4lgDTrgC4vFMFVhn4eVeQKgfVJxuLd3dGWx8lXiSe-NYD7XVwT7pvDbppBifXz9dgC2Bq_MIg-6RY75uGGhXdyhBIKXWC1gRUdU8Ps5GYS54Y6o_jI3MEWzwNlqvfUSrK_X_GNgO6gEDFvM5-eV6DWBE9zxX4FLcTVREr3cD47-df2wmsnzPWf51vvcYAj0OMREy2ONdZV9su4TL_-9GKoWX-vGIbGpCNU9QW7Mn7sdif4doiDOyRreHSVZwAv67EqQ3VaK2B4n_eAFNjV5lgX7cjsR0MorTMD_fiFnBEW1iwV3jc_VhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش بامزه بادیگارد مسی و روبرتو کارلوس
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/90892" target="_blank">📅 14:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90891">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuPQjtIsORYffOqFAHqYsQv8S8rf2YPPP6toAIswEwAYwxKRnxFBNOjuRPg55F-csAaf34mxsZlNmXe4QnunY0v99B8ZHmguLUrM4TSghqNAW0NoHpBbDhqWZfSsFpRbp5scw680mAGfRtfE121zF6wzOe0up1KGa1E7PF0QxHTnYa1PXHTbDjJ3jNO22ktbGH_4qRvul1S917ZDndMumix0-Q8y5RCxp1t_vENi3AnDSjiMb7mKkotYLh0zASZ1Kt_je17u0vrK1PmEgIEIoOo3suR4R45g50RlCTa5rgUQ5aNfHw5NSwcksKIDMIXej8qoQBC6Sytkk6mMppaMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب در حالی ما با مالی بازی میکنیم دم گوشمون عراق با اسپانیا بازی دوستانه داره!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90891" target="_blank">📅 14:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90890">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔥
🏆
فرآیند جالب ساخت کاپ‌قهرمانی جام‌جهانی در نسخه‌های کوچیکترش؛ خیلی دیدنیه از دست ندید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/90890" target="_blank">📅 14:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90889">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49acd8fa4.mp4?token=MCB2NHjqCi3Hmhkvj5VFNBspjKVweCkjuVgbfKuvNkgFx7uiIJe3-xLwA-uZMe37OnAmGW1195VIVvHNep0w7IwsUTTWWDq9IJga7ffCO1otrWKQtfnnhCJRIs43H_K21w_BDzvEguHHw0rexZGk85g6YbsVTDBqDQfpKyV-PBn9Rpxic__O0cUhFts8OxJeZrcfpXBE3WSVOOGK51LYS2x6CD618t8w8ZZThcFslFtzXFr9a_-su7oPqtgP7Xl-yt-0oM_8_t8C-sezqQ0i4UXtEi0wRCmN8AFPNPd0AcJaNhg34To7cWcA70Gx0uCuQy29Kll15i8-nq5eE9FdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49acd8fa4.mp4?token=MCB2NHjqCi3Hmhkvj5VFNBspjKVweCkjuVgbfKuvNkgFx7uiIJe3-xLwA-uZMe37OnAmGW1195VIVvHNep0w7IwsUTTWWDq9IJga7ffCO1otrWKQtfnnhCJRIs43H_K21w_BDzvEguHHw0rexZGk85g6YbsVTDBqDQfpKyV-PBn9Rpxic__O0cUhFts8OxJeZrcfpXBE3WSVOOGK51LYS2x6CD618t8w8ZZThcFslFtzXFr9a_-su7oPqtgP7Xl-yt-0oM_8_t8C-sezqQ0i4UXtEi0wRCmN8AFPNPd0AcJaNhg34To7cWcA70Gx0uCuQy29Kll15i8-nq5eE9FdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چالش جدید هوادار رئال‌ با موزیک ترند شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90889" target="_blank">📅 13:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90888">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C31pbG1yvUtARG6ADVJ23Fr6G5IWEMPrvmzS_dgNaNZM-fk4rpxPMmivhcMrYs2_1ItNsH_uFJLzUanaDb_Vzo_Dfa8rOy9tOeGz-TvXXI8_R8YAiIpeXe1AgCypypw72ZihIvA0Wo6XqZutywuqsnyM_Z1qlSSv7DamfGCbqUp8_WLYAYKUuiAHHl_z-HcGJ2UeOdJYVA_3pE51OEg75UQuKzKKz9vNH2PlTkvZAK13YIlodX1Xary1Qt-TbbGPvU23APJUACfYxrTY4zSTMnb5sQ_ZJsw09sK8DCk1SBfa2S-MsOnF55kIYxJKStvG6EI2GtP8MOjsUX7havEwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
📰
#فووووووری
از اسکای اسپورت:
🇪🇸
بارسلونا نخستین تماس‌های خود را برای جذب آندره‌آ کامبیاسو آغاز کرده است.  این مدافع چپ ایتالیایی در فهرست گزینه‌های باشگاه قرار دارد و مذاکرات اولیه برای بررسی شرایط این انتقال انجام شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90888" target="_blank">📅 13:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90887">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ با اعلام نیکولا شیرا خبرنگار سرشناس ایتالیایی، قرارداد ژائو کانسلو با بارسا دائمی و تا 2028 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90887" target="_blank">📅 13:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90886">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvCJQV0Eu5jhrTINrGJ8jR6oYulJ1W5hLSUgZA8Uo8szKt1N7l8AAIrn0AJA6XffMZTWIYhdpAP4nnuXv2lzADbBeyfDWsOIllcOPwtxhqYqZg7eXxh_kEzsBY1UiLDJtqVhFewICysGTm0fMSQ2YX8hOI1PCiXGV_AcpQjGQwowF34iNuzDstuFcaki8tzYODAEuBldQddvBbMybbS0eCSu2V2DJQNB4iiyomx9as-fABy57LpXn_8IBqK9UttIMmNwPgmJoIcQSIr5IXg0N3hj6s56ZluuejdgsZZaFT43i1AInK2s5R-1rGcGZZJs26kf4qETjYUzof33LCm_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جوانترین مربیان فعلی جام‌جهانی، نکته پشم‌ریزون اینکه سن نویر از ناگلزمن بیشتره :|
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90886" target="_blank">📅 13:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90885">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
اسپاتیفای رفع فیلتر شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90885" target="_blank">📅 13:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90884">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOTn2tQg_whUJcSHLgjKZ0gloB5FRTWTwCgKXlihuJ4YRe-nFM-oK0z34nWZUGWEo6rQSHxMoR3KG1Zby_lteo12-1SwWoEuHsOJDmR5Fk5W7S6z0A9TxINi6NvO37IAcPDIkyCjWT_xSHdl_OQBVKoCgTEpjMIuWqvvSAJmHkDqwQtSZ5pyesB46VDXjkYENSDtLW6lnU63fnoG0-kYBaCfvBQrjYsGR8LWOF3EFCYO0EMio1e0DwYF8Zqsa8BwX5NCp9IawMun3rUz30aPCkbcWQCvEYvwmNGDhrRhzodEzG5T0h8Q7M-p-YaDNo6XW07RJLpjaELvyQqO_QHCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تاتنهام بدنبال جذب ساوینیو بازیکن منچسترسیتی رفته. گفته شده اولین پیشنهاد تاتنهام رقمی نزدیک به ۴۰ میلیون یورو هست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/90884" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90883">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0d6510.mp4?token=KKP9SJILye4g6LGhuS4ppCLSM2xWte5CjGN_sx9mqSkjNb1tfI1vYh229SauyZpiDUhdSVIKZO5Ifx24c2RPWdkMJ86_Dsfup8nQpPJF3whLJy96omjZr7eXSalTXkJvE_v43uO_tkc7hcpRGGdtsmy7S1W7pPoqnPgZFot9kMNG8dvEc9-g4FKZkfqshD9zpso6ShnayJtrzNWaDejCELbmVeyd3_1G2G9GC2iCmAzR1FPUUGpwaP9kQwfPb6mtDKXgYGo8EtCJSLwxjtSCvjTG7N9rPQIRVGqzi9j1ZCyWjNjE4UUQcY-9zVzwvmSOb3iF68NGXdtdS4CrIKwL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0d6510.mp4?token=KKP9SJILye4g6LGhuS4ppCLSM2xWte5CjGN_sx9mqSkjNb1tfI1vYh229SauyZpiDUhdSVIKZO5Ifx24c2RPWdkMJ86_Dsfup8nQpPJF3whLJy96omjZr7eXSalTXkJvE_v43uO_tkc7hcpRGGdtsmy7S1W7pPoqnPgZFot9kMNG8dvEc9-g4FKZkfqshD9zpso6ShnayJtrzNWaDejCELbmVeyd3_1G2G9GC2iCmAzR1FPUUGpwaP9kQwfPb6mtDKXgYGo8EtCJSLwxjtSCvjTG7N9rPQIRVGqzi9j1ZCyWjNjE4UUQcY-9zVzwvmSOb3iF68NGXdtdS4CrIKwL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
چیچاریتو مکزیکی تولدش رو اینجوری به سبک چالش ترند شده فضای مجازی جشن گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90883" target="_blank">📅 13:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90882">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6tl-Jp4OvMFvZ7fAQztMCY8UVuoSUPfgtg-eRIApQ-xBvfzA8zQbtTvQNlM6720vfVAh33k3Yi5tfHcjM9GPoEzydlr1Nn3ZtKxajp6VIYNYzNBW4F4vDXDUBDzKZFA7uBIC3FD7Q19iRGuF-hLvoUA-yFTO2i3eXasNxX4npMICqLG5tg8fZ0S32nowQ12GY9kA8WcgF77NF-Og59fPPD5HPYo1AeHvwmZL_ICObaZeRy1D4_Ef5yQi_BXFmTGulHXky5EoRvtgnAD18-2nrsucOLrX66hIt7cg85nNrrxwIfZVXFM4o_jsFVxAPlOgJRPp7uLxwdsPC_fuCn-Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رتبه اسپانیا تو ادوار مختلف جام جهانی‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90882" target="_blank">📅 12:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90881">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/017a14deff.mp4?token=YJMQQSW4jvxVSk9p_z15-uyFk36kZcoR9JZsayRNhv7p377M9BVNyjsn6aGAhYcAWDm-031P3X_c9rnGImqFpgf8U2saLrfD1-gO_-05t7CubdSVPl52Rs1yE1pVlKxlgHAJVAumTIaVZ9s3lSUzo8La20rS2AqEIP_6-4QoJY-zSc_zrCgOXz3PWPp7RcadHCL3OS0n2i0NgKCQe4eIiL1dhcLm5YXjC0WD9mlNK9z_tbFmzXpMX1sx_fpzMCZfC7OhuBwfhS-QtN5ihq1XAcWVM2Oa4vD52VwoGBBfmkbbft8lUP_S5Cc9m_AkYtvjwsvmj_TkHkeAdmAv715t4iZDprrBdl_28q5Dp3W62Fq-YfKG26ZlEq4OgbI3LjzXq8JzfmoKZVq8_n0j4poAkgpDjYDl7xF8-no0uW2QXBwHyPZOfexENIXXzv0RJknK2LDI-L7xpHVYPHFDa2IB269UHIyZhNSWSclRTfAlk29_pqC5CJzU4mP2DrLW9_8NL55MEaXXX3Jit20JG2_7dbYASBcH86VY1IuSC3u8fvegmfhwve8BqN4T2zUGaDH8LbfMrD1xpax4Aabjasge8fqw6yjTvsqOWfQJmIT_HUidBp-VqM5kKMfUAa5EyWcK64YmLurSohriEoKjamNAg0tMppwOcDWhtTbLTVyq_JM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/017a14deff.mp4?token=YJMQQSW4jvxVSk9p_z15-uyFk36kZcoR9JZsayRNhv7p377M9BVNyjsn6aGAhYcAWDm-031P3X_c9rnGImqFpgf8U2saLrfD1-gO_-05t7CubdSVPl52Rs1yE1pVlKxlgHAJVAumTIaVZ9s3lSUzo8La20rS2AqEIP_6-4QoJY-zSc_zrCgOXz3PWPp7RcadHCL3OS0n2i0NgKCQe4eIiL1dhcLm5YXjC0WD9mlNK9z_tbFmzXpMX1sx_fpzMCZfC7OhuBwfhS-QtN5ihq1XAcWVM2Oa4vD52VwoGBBfmkbbft8lUP_S5Cc9m_AkYtvjwsvmj_TkHkeAdmAv715t4iZDprrBdl_28q5Dp3W62Fq-YfKG26ZlEq4OgbI3LjzXq8JzfmoKZVq8_n0j4poAkgpDjYDl7xF8-no0uW2QXBwHyPZOfexENIXXzv0RJknK2LDI-L7xpHVYPHFDa2IB269UHIyZhNSWSclRTfAlk29_pqC5CJzU4mP2DrLW9_8NL55MEaXXX3Jit20JG2_7dbYASBcH86VY1IuSC3u8fvegmfhwve8BqN4T2zUGaDH8LbfMrD1xpax4Aabjasge8fqw6yjTvsqOWfQJmIT_HUidBp-VqM5kKMfUAa5EyWcK64YmLurSohriEoKjamNAg0tMppwOcDWhtTbLTVyq_JM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
بی‌بی سریال متهم گریخت پس از ۲۱ سال
🥲
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90881" target="_blank">📅 12:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90880">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225f01016d.mp4?token=VUm-SgxMCTK7D5FJE4wvKL6Wvh-Kn6tcAjB3Und4kRcXJMpzWc5JvNFmy4boW3iUsUqc86GgPoztoNPI96FcmZJfDouLkCxuU_tENci9WRPGTjEe_bkJeAdAKQGbZjaZjcH_07xxYNTglz3aZaoa5hdReuqpIfoxVW2UcVlhYq4Kb5z8jncjDOiq0r_9knXQaZR4aASsXfAy9sq_wlf7RGrfMBrlh8eewNUktEXuxjKkNHtBA23cEFCshcRQx_hmdC3iybr89pMQb3lY5aghkA615P5MrpjF_NQLppHd0OmrqwhZ7Zurr4DynERCiEGL6IxCTAbQ5sVpHTtEnRH8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225f01016d.mp4?token=VUm-SgxMCTK7D5FJE4wvKL6Wvh-Kn6tcAjB3Und4kRcXJMpzWc5JvNFmy4boW3iUsUqc86GgPoztoNPI96FcmZJfDouLkCxuU_tENci9WRPGTjEe_bkJeAdAKQGbZjaZjcH_07xxYNTglz3aZaoa5hdReuqpIfoxVW2UcVlhYq4Kb5z8jncjDOiq0r_9knXQaZR4aASsXfAy9sq_wlf7RGrfMBrlh8eewNUktEXuxjKkNHtBA23cEFCshcRQx_hmdC3iybr89pMQb3lY5aghkA615P5MrpjF_NQLppHd0OmrqwhZ7Zurr4DynERCiEGL6IxCTAbQ5sVpHTtEnRH8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دهن سرویسا چی میسازن
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90880" target="_blank">📅 12:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90879">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d81d6976b.mp4?token=bkCIwODZA8xSxDI9rATreXZMNKVVVlT8RLCVG2qtw-JVdfDR_c7Fv3Zg9Y2JDpJeAUgmo0k5ajcrf5wJNYkdJagoV7N2SPSBxc4GSZ1UM_Itss4a7KAwpFs1eFYNPnnalz2E6qNvtdrsmHw6Env3KTaKQVNDolF8RTFZXKQHj5Z-soviSXm0nD4F-FjT0C-hOa1Xzd_FEeDCbGUaw3LThp1IqUTqEn5Yl2_BrxS7F7ntZpWLUqyjz29RZF2O2m-gLek8x9S14nnn8Ysf7g-7o7MWix_Yg2d5QOhO7QBANk_7FLtYkk55Hhu5UrFzPfpYKTybv2X0KbBo7mdtaxWgVpZt3KiwxjGNDH4390jAjVrwRtqdmTl5-G6533Ps_z11xkAaDBE-1uODF5sJtt-cG356QhRpNX1i6AXB-3UKt9hSbU6c7Kp46XpsiULrMMTbsFHZ9I5aZg6pFfblXaPWVYsYO1wPuH1QxWhgdsdnz2ECKyjHGG2W01SJX2_L5oR8o0DhUnu_0wuVmFdzSCmaO82mf3N0t0aoJlv5QmOZin-XsjLDRYgI5BmIIMQhno-So4-jxbmaDVAQgNWLqtFWCfgJ3pfuZl-AOjX6CBxjzlmXw4HqCdN0BUfTQHSnszUCm2O2LsHGCSDUgbRJTlB2kSWwJxuA9p7_8B62rvTGMS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d81d6976b.mp4?token=bkCIwODZA8xSxDI9rATreXZMNKVVVlT8RLCVG2qtw-JVdfDR_c7Fv3Zg9Y2JDpJeAUgmo0k5ajcrf5wJNYkdJagoV7N2SPSBxc4GSZ1UM_Itss4a7KAwpFs1eFYNPnnalz2E6qNvtdrsmHw6Env3KTaKQVNDolF8RTFZXKQHj5Z-soviSXm0nD4F-FjT0C-hOa1Xzd_FEeDCbGUaw3LThp1IqUTqEn5Yl2_BrxS7F7ntZpWLUqyjz29RZF2O2m-gLek8x9S14nnn8Ysf7g-7o7MWix_Yg2d5QOhO7QBANk_7FLtYkk55Hhu5UrFzPfpYKTybv2X0KbBo7mdtaxWgVpZt3KiwxjGNDH4390jAjVrwRtqdmTl5-G6533Ps_z11xkAaDBE-1uODF5sJtt-cG356QhRpNX1i6AXB-3UKt9hSbU6c7Kp46XpsiULrMMTbsFHZ9I5aZg6pFfblXaPWVYsYO1wPuH1QxWhgdsdnz2ECKyjHGG2W01SJX2_L5oR8o0DhUnu_0wuVmFdzSCmaO82mf3N0t0aoJlv5QmOZin-XsjLDRYgI5BmIIMQhno-So4-jxbmaDVAQgNWLqtFWCfgJ3pfuZl-AOjX6CBxjzlmXw4HqCdN0BUfTQHSnszUCm2O2LsHGCSDUgbRJTlB2kSWwJxuA9p7_8B62rvTGMS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای دوستان گشادی که به هر دلیلی باشگاه نمیرن و ورزش و سیکس‌پک در خونه میخوان
👆🏻
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/90879" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90878">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARoW9lAPbEdwnj79tDLFsouuX8u3t7Gyw5Wp2wJvv4H4bTiWEPCiRs09acXUnRDqVE-FPtP3fxXjvYJT4Kevdeo49arcBT0x0CTM0dxxpbPm3SSsiGSOLoLVFIMWt6i3cLQNkzvdyX62Tm_3usH3lmEb08ESgR_CBxokX3xml_I5-VwPuFgQ5i6qd9q_GegBf15FVOWC5Pg_KZu_ecLhqYxqGv80ESFl6_7Gjn55boqQUiylbW-V1PtKhrEVsQDzfS-VcnmLfY8lyAfSRvvnqXucfWMAiGS5IsRXEdn7dXYJXAMiKTDcIa_OOedo6XxRav5iQYkChVwWboc2Y6HqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتلتیک : اگه تو جام جهانی در فاصله 13 کیلومتری ورزشگاه رعد و برقی ثبت بشه بازی به مدت 30 دقیقه متوقف میشه اگه تو این 30 دقیقه رعد و برق جدیدی ثبت نشه بازی دوباره به جریان می افته
در صورت ثبت رعد و برق جدید شمارش 30 دقیقه از اول انجام میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90878" target="_blank">📅 11:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90877">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da40b1eeeb.mp4?token=v0Q5LKcNJ4vI-9z1uVEhghU7Skh4BhH5MeEomy9J3ihqjnJwkDjsjJ0OSvDPGYhcdboVV8uLLCVtlsC9XdI1MTyMEirqchg0bdjVjpnPI2hHeliiMaXWBcbHvqygd8xVD-IcGGP0Kbo1-68KN8yPhsIMokevm7g0pNHfkBbkDypLL2UrjkLZeiOVtCzKQY4xG5PxZ6Zl8BWhkps2AQxSDCGkHxWIo7wY7TkTyK0EgtKX6TyFiXpZEisfHBd50dUC5hyao7dF1rJA-ZXnzE1R3HdLxIDKgZQtNaxo3NDgsxPXy11KVKVZ-9IL8W7pPvXjB0Vhuzf7GsakVhwigGjKMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da40b1eeeb.mp4?token=v0Q5LKcNJ4vI-9z1uVEhghU7Skh4BhH5MeEomy9J3ihqjnJwkDjsjJ0OSvDPGYhcdboVV8uLLCVtlsC9XdI1MTyMEirqchg0bdjVjpnPI2hHeliiMaXWBcbHvqygd8xVD-IcGGP0Kbo1-68KN8yPhsIMokevm7g0pNHfkBbkDypLL2UrjkLZeiOVtCzKQY4xG5PxZ6Zl8BWhkps2AQxSDCGkHxWIo7wY7TkTyK0EgtKX6TyFiXpZEisfHBd50dUC5hyao7dF1rJA-ZXnzE1R3HdLxIDKgZQtNaxo3NDgsxPXy11KVKVZ-9IL8W7pPvXjB0Vhuzf7GsakVhwigGjKMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشمامممممممممممممم؛ اشتراک تصاویر جوانانی که در کالیفرنیا زانو می‌زنند و ۱۰ تا ۲۰ دلار برای نوشیدن جرعه‌ای آب‌میوه از انگشتان یا پاشنه پای دختران جوان می‌پردازند، در فضای مجازی سر و صدای زیادی به پا کرده است.
😂
😂
😂
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/90877" target="_blank">📅 11:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90876">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برای توضیحات بیشتر: قرارداد هالند با منچسترسیتی تا سال ۲۰۳۴ معتبره و بند فسخ ۱ میلیارد یورویی داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90876" target="_blank">📅 11:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90875">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ax9vu1EzfENjOMmRPaK95EJLr7r_2Fpo2H5p4uOY0veZW0A9UmvYzozP3ILm5FocbwWn1AzbJM1OZ2qUm_XvMFjvfz9HRgrtOFtOe7GuPZ2pXa1k6-E38WMTLfmP8aX4gL1-Ve-2BsoKcR78BEykD7w16adzkpzPjc1S3NZfsMG2DwQ5uW3YV-NlapdjKK9Mhf71c1Vg7UIaQabwrSV5io89aFmaEREegHUMemNuqIVHC3SjVJaVAAuoJ9Sl53Rtb-4vj5I-w9DO48EL5s-2T9oBIWTXcBMpxI7qbsg8lpPsqjgc6KzzcVLviovuKgk82Qx0XTC0WWDWWA8M1b_8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/90875" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90874">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dad07bd808.mp4?token=SjZwS0w0pLBh_cY5pZ0YtIfUftoH7ddb560LJ6imWWU1n8u454j7ngRI47WAqV1gqi14XpB5YrLHmdNgy8NssXLD5BUUjcP0LhbKqmVbjmtrEZxvy1akGlvTfpQ4Pu_AJgLMd-j7-C08v1fugB7UvQhyMzRKVeGzqZAZvkfB4scS0neSVQpxFteitRo1OjrqKm9U8BqXJVAs8pUcirdGf1GKUTfE4KIqLWa1dN1Y9HJcAm95o4RYjLcRAu4RKrMF2vKOL-vTc57IsJf5Cxzb2kfiMJ9Rcv6yYdNt_Fg-rewUGgZzKy-SiBgjCuHYsU2iT-TO5s0aqeW9oiW8ElOCgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dad07bd808.mp4?token=SjZwS0w0pLBh_cY5pZ0YtIfUftoH7ddb560LJ6imWWU1n8u454j7ngRI47WAqV1gqi14XpB5YrLHmdNgy8NssXLD5BUUjcP0LhbKqmVbjmtrEZxvy1akGlvTfpQ4Pu_AJgLMd-j7-C08v1fugB7UvQhyMzRKVeGzqZAZvkfB4scS0neSVQpxFteitRo1OjrqKm9U8BqXJVAs8pUcirdGf1GKUTfE4KIqLWa1dN1Y9HJcAm95o4RYjLcRAu4RKrMF2vKOL-vTc57IsJf5Cxzb2kfiMJ9Rcv6yYdNt_Fg-rewUGgZzKy-SiBgjCuHYsU2iT-TO5s0aqeW9oiW8ElOCgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
مازیار لرستانی: از اینکه پسر شدم خیلی خوشحالم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/90874" target="_blank">📅 11:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90873">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM7WIMrlwvVNx8CtILQZHJ9iidvJx1hDXP_8UBDUenXkyiL39TPGJM2OIsV7v7zDsxRbbVCqNs3nd-Sq_Mqsn4UocKIsAGRw_BOlnm5vM1uvr3IRa6UNlWU9K97Ee98CCVoBl4YZGdkjGQ4tILnCPqGqYIjC4h6qK4zFG6Ee73vczYcnKYxYx_oVBY7ck4EV8aCQJaTPRjybxSsKNO_5i-5-nYMtnw5Ml8x_of0ld5p2G_SQzmUp-0TXaOEr6Jg55wxYPJL_ZcQsF72G2jvFgmaFyfemTlu0FNpM9DRElOZWneYCjWOjzRREOmwwR8igKmbGiFuRM4pWM3w8CF5QIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنا د آرماس با کیت رئال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/90873" target="_blank">📅 10:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90872">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkHCdge2XeP1diTb8EnSoRb5YY72itzjkzeZaiY3ZfN2esC47Dfyqe8LxWLdW-PtMIGbjbfYu_pk5ZNx1CrKUYEGIrI1pPRuBzghpvZ4bWCoWoOFSYh3nanz3v7A5stMNMHqMxtEwlV7OPKP_GuVoEbCgIUeTFSpU7FNEF9UjMAXJzMzfr5H3JEpPUgS7pMrJJJ9SJZyCf2Giglm-djjv7NaDLbIXzBTfwrA3ZPRlZh-WJfYcvVkk2lTS6xGVJFhZmHT-Uz-ORJEuGAyIRs_J115LunR21Cw3w7pbrYw5hs8XvWIgImqPQy9oQy4WIn-ISuQ1zMyzWCJUvvxxLX6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بی‌ارزش‌ترین تیم‌های جام‌جهانی؛ تیم قلعه‌نویی در رده ۴۴‌ام قراره داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90872" target="_blank">📅 10:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90871">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljKUcsUAeL_8oJvZcqWg7auIEgIaYmD5-prCQ_9RVkfDWcsgHy5w4izhJ6Z0OZ-S0bjcCDY6e0ZeYqL5fBKRHBumYG-FRZQBfSK7g3-gOeKVz9hoQXgLgh26NnFfPKFnzszAcgti9oY7WzzklGsGudv63iYbEkT708Cs3Kg_lS0Zl0qjlGVTuB86I326Yp-wVVDsPbpVbu7O-_o_o_Y5v33J8_5QIDr3MXK521eDuhH4Su9w-vEG71eASDmeCzt6ytif3wu4mVQOg4wwnyY4yT3ROOlQqH3QFR1XP_EpgrIOdIw2Win_LE2xlw8gzJi7yU_6ezKmQDzDMumYFzj99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇲🇽
رائول آلونسو خیمنز، که قرار است شماره ۹ اصلی مکزیک در جام جهانی ۲۰۲۶ باشد، تنها ۱۱۶ دقیقه در جام‌های جهانی بازی کرده است. او هرگز در یک بازی به عنوان بازیکن اصلی حضور نداشته است. اگر بازی مقابل آفریقای جنوبی را کامل کند، زمان بازی‌اش در سه جام جهانی قبلی برابر خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90871" target="_blank">📅 10:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90870">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn449nsOAIevUxFpsNgKHoOkVTi55c7U7qT0dm_DATr4YMzxjZWTP44nn5OIoATLjqNR-d3_N5CWzmDsE8V5CtQRewV18BN16_Zvb_0Yc552xG4L2bwpqloKd0kdeDuKjym2MD-fY4LbgAVOXI2iZHvvMOS0Hvt1389pMdvjlbSZk8WxoefT-K6982xs2LABeZGmMyn4Kr7mHPUidLj3ZtmeZ5WQncMF5f0p4v6THFeMyu5FDwVNar45NAfZpigT_y6NFYV3lOwGx09zl3hJk22I7TwqiRHFQMe3Le9oni4YLBOTiOKWF0amz5U8JY5D5qtmnGADyKRFNBSIHXormg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد ریدمان کی‌روش با غنا در آستانه WC
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90870" target="_blank">📅 10:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90869">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfbdee815.mp4?token=Mkllnj5ii2mceeHoFf7rxcFNPbfUyKQYK2mR0unhN41hWvFdB9IPPv6x-aJ_NxCoSo10vw1TvTt4d0lIbMv3rBZa2G_loRzIoivZIPkyoIWb_fUf6cTmQpqfB-XrWQ_kORLEqkXJ5XDrBREWqkJz4uEVdaGrApWmsTTbY08DJwAacjVBMTIpKi2YVl47XUxF2XWapoN4V1GWeeR_qp38Pu4BJYl6QGAh00g5rNbU5kTlMaiE8eyibdNWKsTRV1HnDxdpdzSz5qQnQ9XB6kjLNjmooMIhLlPQidEl7S7XQo3Mq1mN0q0G2gOg7GNnZ3NYCcRyOe1MZBDHlx73dbow8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfbdee815.mp4?token=Mkllnj5ii2mceeHoFf7rxcFNPbfUyKQYK2mR0unhN41hWvFdB9IPPv6x-aJ_NxCoSo10vw1TvTt4d0lIbMv3rBZa2G_loRzIoivZIPkyoIWb_fUf6cTmQpqfB-XrWQ_kORLEqkXJ5XDrBREWqkJz4uEVdaGrApWmsTTbY08DJwAacjVBMTIpKi2YVl47XUxF2XWapoN4V1GWeeR_qp38Pu4BJYl6QGAh00g5rNbU5kTlMaiE8eyibdNWKsTRV1HnDxdpdzSz5qQnQ9XB6kjLNjmooMIhLlPQidEl7S7XQo3Mq1mN0q0G2gOg7GNnZ3NYCcRyOe1MZBDHlx73dbow8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🏆
چالش بلاگر آرژانتینی با موزیک جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90869" target="_blank">📅 09:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90868">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇧🇷
مردم ریودوژانیرو این‌شکلی در آستانه جام‌جهانی؛ خداوکیلی خونه‌هارو میبینم حس خفگی میگیرم
🚬
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90868" target="_blank">📅 09:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90867">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce3254dd5.mp4?token=kTihEAnZ8lKfm2nO-eEmbX8Gib1TprvriEeRdhmWaOgoTqn_iFmoMnIz_Q2DXwaEtZwESnZwNQKJZ2tPaAgS2YCwhTGDDHMDSoCwz4Y0c2dDW08MgK0h_LKNmZzZgM9m5qDhXT-YDdXf9567OK1DvPWzIp-ca5HWRAnfuUqQYGTelo6WoFxa5wod_RFii8AQJv5izeB8HFoDKSC9HWxrZcY6RXX_AcFwOjqcjZHEZoDOc7RrP9ufOnj7lDWG5IPBvncKG5S4l67mTRnufOn0qrwj7HI0ORm8eK_XYngcXoehbOzNJXgc8U1KD1dqXjUGe52EL86Gir25TrzjwOOlpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce3254dd5.mp4?token=kTihEAnZ8lKfm2nO-eEmbX8Gib1TprvriEeRdhmWaOgoTqn_iFmoMnIz_Q2DXwaEtZwESnZwNQKJZ2tPaAgS2YCwhTGDDHMDSoCwz4Y0c2dDW08MgK0h_LKNmZzZgM9m5qDhXT-YDdXf9567OK1DvPWzIp-ca5HWRAnfuUqQYGTelo6WoFxa5wod_RFii8AQJv5izeB8HFoDKSC9HWxrZcY6RXX_AcFwOjqcjZHEZoDOc7RrP9ufOnj7lDWG5IPBvncKG5S4l67mTRnufOn0qrwj7HI0ORm8eK_XYngcXoehbOzNJXgc8U1KD1dqXjUGe52EL86Gir25TrzjwOOlpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بلاگر کانادایی تو استادیوم داشت ویدیو می‌گرفت که اینجوری مامور امنیتی کاسه کوزشو شکوند
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90867" target="_blank">📅 09:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90866">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/90866" target="_blank">📅 02:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90865">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX9VYtxIm-DVqANp1E2qlORM5EyuVr1Tdd9vjNWZlfFk--P9V4_O8dq19PMuRm2bVNxOYdJLYykBf-b1XU_UPj4SI_TtMw5FVUkKq_r3tcKqjsoF9nJWhlaSY5IYuz_COPJeC_4PSFTQ2VDbq4GiE2vX1ZU-esw2h0bptjpKFvKOmq8vkATVMwjbmqEksxJnimj0v2jkuJNsfvm99I-SLQ-g5Gr0KjKlfM9J2aekUPbfh0E_4A2DgiI25skPPCMTf10V3rGiCpc8zvasINGqARNLRYJM4wz_pUegWJJZDUNL6srfEomKpYENqR9h6T_oADESo5ovW1Z4UXLBFMHKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووووری
؛ با اعلام رومانو، کوناته با قراردادی چهار ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/90865" target="_blank">📅 01:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90864">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/90864" target="_blank">📅 00:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90863">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری؛ ریکلمه: ارلینگ هالند با من قرارداد رسمی امضا کرده. اسنادش موجوده و نمیتونه بزنه زیرش. فصل بعدی شماره ۹ رئال‌مادرید در اختیارشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/90863" target="_blank">📅 00:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90862">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/90862" target="_blank">📅 00:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90861">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1rvJdG2wGLYqHOuBQtcn6faSdcq5AaKyJpLyS2fYSizzQFapudOAbY_XRlvTmYGRB_Jie0KxTCqcMY7uuYK51tRAOLGSa6k1yilk7_0oFAKdmVTe5LRoPEUI-Jz1jJzB11z9BBosNLmSULsmpaCHkAi7EkLCHx6xYpEsXp-9C7EqQbzCwd5DBgAlKth2yxXgi0eJQAzEHOZ7fprMAcGG-1C2RzkqI6cJh6ze8q7kVlh1KtG4ESH4M9s4g9PFZ0sRgrWGD7czFHpWkbmddVFYYKBXTVK-83MRm6HvCyDULiMQG4UJvfQLf9KM9btLnfUAVFVDjiBlzKk1GRkUdLD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قرارداد بزرگ پرز: کوناته.
‼️
قرارداد بزرگ ریکلمه: هالند.
⁉️
با ریکشن بگید شما: پرز
🔥
یا ریکلمه
❤️
؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/90861" target="_blank">📅 00:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90860">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpfo6iuTTlZ3qXS20eKzihK8XkIyceXYDwEXPh0-4JGhRkrRY1APcj1UmIhO3RAAijAzAoDzOzymom7cehKWmIm-SPY7eBHKf5B_bR-btEWheFtwFGB7zKGzxHepsp1obvyxQL6PeLBG_QptR49gKOZOJpGFVw9-LrlgFk9L_UILLWDz48qHgeUy3jM-SdBDOoftF1_AVeKXm4Y7vqayb4Fc3SlZ6gMvXCql4DyDy3Uelbo3AWlX20Kbi6ae0Wf_84_0zTkeOaq6N_dXOW0AP9XWNsytjbWbPtwwWxVYVpvF3GdvFkq5pJA8bDFelya-r_h4ij2_ZELmKEpc3yWYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/90860" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90859">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">😂
خب دیگه کسشرای ریکمله ارزش پوشش دادن نداره. فقط اینکه ۴ روز دیگه انتخابات رئال برگزار میشه و احتمال ۹۹ درصد پرز با اختلاف این کودن رو شکست میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/90859" target="_blank">📅 00:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90858">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkwHQthhFXNKkDQ5Y9NF0XQyNi0M0Q28adCQXoXHgWCN9b_RRhavmW5r3q3MGPoNhlLuBgnkN9JlCaPiYVdR1bCdlJWPiR7EaUCQj_hXvMrMMlx3CvS9DTaroycwVivl3sbzMRZdwQWVJz09QfBK3PS9XAzNebJ9SyAMs4ApdnjMKNarqQ4Y5X38w3Hp3APKk5BTW6j5udwte9H4J4jSZf61d77sbYllpSyr8S_6Hqap3F0wwvTkop5g9TA2NpC7xA3BkE0K4CsFxjy0iKJ-IR5lWu6KMjNMDMvl48BbxpwlMU-70vy0tKji8nJvcLsrqQQXmJ6RvsnPRqZZZ4e26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤲
🚨
👤
استوری سردار آزمون برای مورینیو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90858" target="_blank">📅 00:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90857">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">😂
خب دیگه کسشرای ریکمله ارزش پوشش دادن نداره. فقط اینکه ۴ روز دیگه انتخابات رئال برگزار میشه و احتمال ۹۹ درصد پرز با اختلاف این کودن رو شکست میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90857" target="_blank">📅 00:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90856">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8fa88ed9.mp4?token=tasphuqEgue9bG3oZ37ww2XADbrimaDgo6B1cO1a5foAf-pXkmpaDaXHF00cUG6pfxolliHP0NY8O0s2I2uuNdCVCr2Oq3XQcUdlzj1qDKx4SFgrL9p6tywufJ3TmXu8s24lYJwdpclclFvWsML_CPIrXcYAoJXSrRFeo9xf1_5irKOGTltms9G_tTKFdyKK7n4RilMCXwb7PCG3by0hSyEIWj48jJTRw1DWOkP58hwGzse0xjiE8zDoYF8WxHCpDTEbyYaKVCD1Kov5OHI0e3t9_m9RIADnbwWxvJNM2COEat0S_NL-5JS3F2UaqIgHPyZIiJ-yqLWHo2Ck0saXrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8fa88ed9.mp4?token=tasphuqEgue9bG3oZ37ww2XADbrimaDgo6B1cO1a5foAf-pXkmpaDaXHF00cUG6pfxolliHP0NY8O0s2I2uuNdCVCr2Oq3XQcUdlzj1qDKx4SFgrL9p6tywufJ3TmXu8s24lYJwdpclclFvWsML_CPIrXcYAoJXSrRFeo9xf1_5irKOGTltms9G_tTKFdyKK7n4RilMCXwb7PCG3by0hSyEIWj48jJTRw1DWOkP58hwGzse0xjiE8zDoYF8WxHCpDTEbyYaKVCD1Kov5OHI0e3t9_m9RIADnbwWxvJNM2COEat0S_NL-5JS3F2UaqIgHPyZIiJ-yqLWHo2Ck0saXrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خنده‌های عجیب ریکمله به انتصاب مورینیو به عنوان سرمربی جدید پروژه فلورنتینو پرز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/90856" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90855">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام ریکلمه، رودری ستاره سیتی در صورت برتری در انتخابات به رئال می‌پیوندد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90855" target="_blank">📅 00:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90854">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZlFeJMIn88-sMpaB93ey2nGkSsGxgLYt2kZp1FHDaxb62QDqq22OqCqQ70PEy3-WF6b5amVekUc6rMrYe5PLxki58CSy6A5lbANf01xW14WEBNBSIRQjhushkDrIlWe8oTBeGUCzZaAnOjeqVUPl1ftd2NPh1ftua3CvCNt-GOqizS-FHNztBIMA4aAcgxtylKN7DyK9wOkeuaQBN4I1LG76tcwIl6CCaWPhnBSPkzhpFgas22UafPtbu5esPLNaTkYNJCKGQFlwzePxpeWAoSVTnsdAeJBmLHkE_kAvJZQwKl4YRE_LiQKVU8i7tjLRRjwVg_m8x6vwhokjUQ5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته اجداد ریکلمه رو بگیری به خمینی برمیگرده
😂</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90854" target="_blank">📅 00:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90853">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
انریکه ریکلمه: سرمربی تیم من بزرگترین و بهترین سرمربی فعلی جهانه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90853" target="_blank">📅 00:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90852">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
‼️
تیم رویاهای ریکلمه در یک‌نگاه:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90852" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90851">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeJCL384wtXoGJgOuv0lS0Y1Z59VoQ2InFYcqEBm4zDxwHL50hqR_RJdZy5gSP9z-2m49egIs-d34SK3ibZylvxvSDZ9iya9gnwfxaG6mZAu8zHZKCqEJekADvlZVylSpfL20oHi3pBDut5KkENt59rsUCQ4gnVQU8oB_VS6wOnh6UPfWeJdCOJeC9MhTY482vzpb6hUmb1MtWz2QcctVqH91J7nh9RUKGJvE3ZUowfuCZFAgIxxtZr49rTU12LkWG9bjAnYYuPtbIaTlD1NmUmQoWwlPHm3iaWeAYwv1RUB-Pk3Xyqc7sF30eNty9upLu9O4Z5SKYa4muRZ1JDzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
تیم رویاهای ریکلمه در یک‌نگاه
:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90851" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90850">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
‼️
انریکه ریکلمه کاندید ریاست رئال: در تاريخ ‌فوتبال تیمی به شرارت و کثیفی بارسلونا ندیدم!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90850" target="_blank">📅 00:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
‼️
‼️
🚨
🇪🇸
🇪🇸
انریکه ریکلمه: بارسا تیمی با ۱۲ بازیکن است. یک یار آنها همیشه داور بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90849" target="_blank">📅 00:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90848">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
‼️
‼️
🚨
🇪🇸
🇪🇸
انریکه ریکلمه: بارسا تیمی با ۱۲ بازیکن است. یک یار آنها همیشه داور بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90848" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ با اعلام ریکلمه، رودری ستاره سیتی در صورت برتری در انتخابات به رئال می‌پیوندد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90847" target="_blank">📅 00:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90846" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90845" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90844">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90844" target="_blank">📅 23:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90843">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irukLMAlEZ0pOnFJpfDDMhVq6RGH7CLKWNYdvrGlSRSjWOBxFqcfQ81iPEo4FMR42pmuR_xzkU2LF7UCSaEUIxnPVKNP0srw6kMQMWVWrHtoctRSnHUv0JobF0lxJ3kwBJexO75LxackPXjpuoxpUBdUy-V8q0slgVFdbkz0TBLs2W6SX4zVjrMxbkuU7xWwy65m9NVoy6Bh9nVYXu1iwqDdyCRXaVw6eo1rWBEYmyTlBlMWUzt6sEOTH2ehSw9kCiyuyJLD49zojLKoFJMwWiDKBIIqzbwt_LYHMbHf3dy2356XOqirBYdnqZh5j7gPen2nXw9rOKDTQNIu-m9Hyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ پرز فردا از کوناته رونمایی میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90843" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90842">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCXb32te8djzyexX9lACcn_PaqXwuCjIBeMZmnRqMG19aa0YwF2S_1B78sgHVGzRDQGXyki5n4Jpqj4FYlqS6SvwYbCbcwQj789dGzeea3s-L_LrKvzlf0JYf_NvYRMFxyh67HUauFtbaYHO70QHlsgSuC5GfAiCa_0jPREqIAxQ2ptpaDPMexsrbO3tLLi-NcssoqgforK2Ea-Wp_WyprVbBHjb0YNWf2T8dTivTxg_I_DBCftC2jJe6dC9O6LEf3IqSmuQOz4j7E4OP-gOWQ7CtqukIGIXI7AYM-5vgp8nFpegAUNAaoJdICdC5BO6QmjBKTzunq54yBZSWSqyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90842" target="_blank">📅 23:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bI8ypzcih3CkOd1EpSLdAS5i0Q09C7bTh7dW9WH2ixtGlDxG-mhGtb5iCMNwZ0FurZOHsudpRzaBe7pkV8qW7mepCGTYOWrQQ7NWtLeos87UH0X41euWrW8fgi97R-Xgi2scuT0H440EnR5nu2nB2oLUlqhQSizfvHQvu7HV86N-FNkp28OZprz6kiaDhgwHJJEanNVqe4R2Nmze1pY5GRdtNXePadebp22xYD-N4T7TkIbGct6y4JR6xbLFbXVdFOmAUcqiU_qXDRj1CXOWIfrYSEJ1mOt2w7Ne-AdH4SozGrduIyE3yHl82SDpY-tuYAOQxXTl-iafdol86-WXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
14 خیابان در پاریس به افتخار بازیکنان پاریسن ژرمن تغییر نام داده شد
عثمان دمبله تبدیل به بلوار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90841" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6EXwUlv_h2yvrSreGRONOdL5y2Go4HtH7w8DcTbUhgzwXfpKDUWqPNJ5Q-u3KkZoBBs2aYosQzAblcx_hgvys1SW6aRiyqy6j6grBSyU0P_xYCYyCCJlxDl35n7BqUeNspHtA9hD9T6zaiNoPRKU099EOqGQrBLHzzaSSUpt-1MCp9gYsrcoC_bdn7mCNK2I8Nb1FPgW2-DsMqnOHypUvc5xTtT0SecaH3-nDkS5bNXUKKZWLg-HG_3yJ8gxNDgOsDJlCvO33dBoGfTeis1y7JBblc4IJt63XHMNdPNTZrwS7pp84zSJtXYTfcwIG0wr60XzEAfaL4cLz1XsvVTTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHag4xAK41fdmRgzmnupCoRyjm8XHJ4_MSXWQPLBd01hftVIi23tD7WGFHxlzy6NEKdI0Ie7RKcPABMRn93GPh6z0iDXQ-1lwwQQizZ3TYjQ_DxhVdLcAo4zpsYjTy5JBg3TPIoX_EWGqAGKaOGpt3Y1KygXEh48JptHHdVVHDerayRbOg7BHebnd-v39F3rnTlFKfG2H62BICNajbgBslVhcebmbXEOyxWp5Oz-DeCzW5iKNM_uGOQpom-X3E8gZiLA2IdMDyJpxCnlySxPi4_IN0f8yYwh8vVZjuuRVFCmKzXDu2vQ-5NdEHBHb3tvSjE8RRtMvYf3If5iFnjaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mw0G6xOfimv7uKQpYbA5fKRQpgpcCn6pCD3D7bXVF4ipgVPUh-9yszqI3vljh4ei36mkTRTMphf4MNo9WDpgzO6o_f-yrj5pV0RSdSPk5uBSfuY4EHypbzx7ny8HqA9-SiQrF7_5IhZZ0RLxJVPFTfHM06-ojLd5y1Xw3Q7768_ecqDeZiN4P5NNkxkcOX4o_Mx33IXf108vtqxyjReNcZG81lFCu1og0qaQUaRXRIwkfr1pu9pO38MC993Uz39BfR9lIpu2w6ZUzf32rawzMXcYi37Atvnk0SPfTttVYvybuDiwiIO7ZlMmFh4D9Eb286vGNvX9CyGG-emlhQPLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dbp1s2PZ5Wt_GPgtPM0HmipgnNT92Oa-0eAOGVznb0gM9GSUucEPC1sGv8wZ62jSrEvONq2FeZwRdMVWc7Ec6LSP9p-xdCNSsd-SIo_R6zmwLzfA_6sAQZAB_ZpBBAhJKs8OY7dmlLkHEZwnjd86GqM7RV1oRgR56mVvNWfatVAlXmip84ymVAeRG6jn87_VP0_LYpNfBMhu8-b0Sr6Ka0P6gtdHVkaTkkOkp0tG6jKDAN6XczhA42_5XHeVJ58b6fGDmDr13dO8crdMk6_mKpg6Lywb3zhQ4u6kt-pn4lGJDyEEoXl2A8rurBemCUTGmewh88b_Y5halXg5e8xn2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IN6MhqVBDez_IzhVjXwAB4ftQkN-3RG9MK2wtE_CroIW887LNSy4K0m01vA4YrcXBU_EmmFzK1udHlmo2n6PYr2pnJ1RPka_Ls51KJAOqDd2wFrafkPuaBcm9RQF9okK3wqCWVkk0O7_YZPI2hm478Gtk9HAToycgYH7Z-wOkuxfU1VGFL9MG15jzfV9kIpLUyorN9zk8IgzzhA291u7fC7LYt0PESQ3DUaw6dvcJxMkrWRfaGMooyKpFLrOScYh0Hd_iZOtaln9zWirt0zAks_Dc6iy2xM_CYHg5NW_jcbXqpCuAvuq-2vaF0x8grgaeXjAyRj9BaXN1TUhTfJV1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">8 روز مونده به شروع جام جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90834" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90833">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFdkbpqrGJzQ6kBY-MrN54SZC0fpIK8t8tsrvgUbaJcmmyJ2xaiU7VFk2vx_QgWB2oiGkWpkn7RgpE3ZznzwqK-yMt0ExlBG6SEPV7-LPFsV5_f1VXY6GpBjEy-PTQiqoNmPaQnfkGbUCPkMV0G8d9LbG565_aXQ3I9wUztBirUPmTN1LpescpISqVgda74Usvfsu3t6qjtoZkF9G6sYbIdp-yfUuMv4J8zxBOOtOWZ48x4kQ4pp4ZuvmPs2d4A9JkuCZRklUOBx8AQQbjQhJjwCLbUAVWkrZpVNf-F1xUFIclA2Cbbff7eybO5MHMtUiijaoHaw7KPakCSyU8TBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شجاع خلیل‌زاده با ارزش‌ ۱۰۰ هزار دلاری، جز کم‌ارزش‌ترین بازیکنان جام جهانی لقب گرفت.
🔥
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90833" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExMMszbyhYvJu3suRoV5HKdhFPLg-5WPo9nFguNoVWLYKBCS5LboXu3Qqtyu4xryD00hETWGgC8vS6L5nmkxa-jw3-AxM1YPtTFwl1AHFISxRYrPtmS9ejsiGEWiSavLpChzoNiOX7EIDZhMduZEJVTxmeU6V4IvB9jpR63XFno0meZG6yq5nQNAuN6GXZ3Z3EW47sN6wLYHRNgijZfApp9EWomhHZx5QNjYuJ8d_dInPVwTVYUlip3E-bufFhTTAQBakFQR34EI95Db0ztTyWO6Vd140pz6aTZqC3gYuF-OMTNot39oYwmQdjlETaZfbFFqfO48viVCeYPMHLo-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری باشگاه استقلال برای تبریک تولد فرهاد مجیدی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90832" target="_blank">📅 22:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90831">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9cHEDt-xxBDs6D3dCfutVBwEaeDgyo6pz4x15wvtyzFn46TjW4EzlUiO-IwsEj8ZJiMBIXbQX4hbJuCseKcN3lbCInIrCoe1HVJo1YXZStCt8wi-ollSGlJFIvmXsoOvbcgk9E34n0J5FHdkhDGdOqrpw_uIlLvXwYWD03DN3zMZ8yyYe0GA_ZOSU9HzbUba7QZLlyVz2EeSK_TcxuyQpY6R1e0Ua5Q4kX1YddodULDJka_qUgyewntly1OX5o6yXiClc0DCFol7WEkRImtthwrLuy7eAVw07a50IAhY_WUBXleKL1_epRJnCDyJhxSrO7HxQPjNcPRCBAL7NxT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در
۲۸
بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در
۷
بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در
۱۰
دیدار اخیر اسپانیا
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر عراق
۱.۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90831" target="_blank">📅 22:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90830">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLW9PjRALkVhjVUTWTrkXGEJDranikWTvPQKFlAGOgVtTF7f8Hx1z9ef3ySxu-u1IIhBi85V54wanFOT7CHI7merpcOHzlEdsD62zLWZTJr_DuPjEhxQapC8ZqPpH7r1DDJR3nGbw2Lcwdw3FjoDLoHLneQvhfqMROvUDren93ri0wVDCYnAj0uqZSKyAHxKnXbzTBdy1Prye6SiiW5zEDuPZGf3FkDMq943IqOtNKU3j5eFBCbQGd_XZFUVAF2t-sAPUZwYMAduVxw-uB66DFK3T7X0IeFZt8BnLCUB1yrMGWCU0A8Hh0e0I21pO0sAhB2qoHLvETcekz7qylRjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TOO FUN🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90830" target="_blank">📅 21:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90829">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnVoBT-6VnBLvV9hShLQ6Xx5j8ra70aC0ui3xRzmaja1_h1l8y13Ue9aF8Qscs8-nuFpc8Ilpq33Mv-Z7_-9rlLE68Hl_pkeommbnB3ZxSb92lI8R3YKGGxeHHKcA2g1nXhwfkGv6B5XCjE59nPCv31ZhWEn8WeCO3GnupvnMXnNOrYOKosrYV3J8fC_apB7d2mUKNrkMutjjStd4Tm96kjuAvhNBXk1p-Kq3jT4qKy4Noks3CODNMi8_H3nSW5aUjk0YpHnywdbInUx1ha2M9mppSKD7lvAMe_vh2qNu-hj0Kn-RhgZ7-Iqm2VR7fgeuudx2dD28cVZuv4NXMvfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو: برناردو سیلوا تصمیم‌گیری درباره آینده‌اش را به بعد از جام جهانی موکول کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90829" target="_blank">📅 21:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90826">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bFMPjc6IIS2yKq20UX2l8GAahQqLX9CKLmBO2dBkQbzcRAEOPSWZai-W1BEEYXgk7nsPxC-WZRZqPWY_G7mBiHcUCRVWGkAXITmMZOWhOsncdpJUBF5E8W0lYA2L2M6jCSxXQY3TtGoKYSi2J14kD3d3hB1wzzqnsRuBo5JSgNxqh4CXRiu-JXD7ICqXz_Mmr43XpmNZGDb9KrsBHi6gmrIkwD68uN2Ef6fFnv6eUn5FUfRdotS5GaMNhwv8zX-llJNtg7hE86FV8_DkHBZrrUDw0nvN7vPI1pbyyOEhzVLITuaR6yhnh6qYeh4AvsCOgYo5UED_Bas0cprDv15WgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DS37wmmNZgT9I-jtbyJ8JdxXC8hyrLDfsNeFJmiwfWg0LOr8DEl0BIbhJvyKbu60cZGJe_pX6MHjGHR61vgkKGkvMTRxEc-TtziaW_dkVqkhPVxBjWhsOG7lPRjGTb5D3MJ60Sra7zQ7OCXzdeN9-1mxGXldKPUSC5xyMIXnCru6mjaIawdMW0c9TI7eav8tSrPS6sM-tIG_Aco3vqx-isuTBF93_4BxPxAsSpOtc7JHtxhB_Iw8jd-THM8PiuLOuxXkzbThqPg9eJDFgtxV5Rt3xdoggnjeVIOGdTFP7lfspdDMNR6afBb-bboRFtagjhU-V74nAeM13e0W_vbV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zte5c0tUSfhOCX1qi-rUuTgDSnF5jOEn9gVv9dSHItVA7RmyFYyTSvO0bNyjKSWeAlpCQeO4biCvOCvx3c8lX0S6Ey-xFHOrP6dpOeBU7tqFF9ueQw-Qt47waqmD-ax9MCy8fube6DZbMkQvcyw7XrG_xv-WgLAWp_KCkqVxXWaRTej6oZwh3KVlxd1uZbgDV84xFlmjl-VrQXUbiajNRthBDPp7FzRBp3ITMl7Gfwz89Qg7XmYuGEBbMpVuPH2hY4yqtvc6wVRQnMjCfLJMSSAxEL8dKnQDfwjq1aorNldU5--pTUxHHaDvZTqE6QDFxKsm4FNeI1z7vwtlYdBFxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و حال امباپه و بانو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90826" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90825">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
موناکو در آستانه خرید کاسادو از بارسلونا است، به محض قطعی شدن برناردو سیلوا هم به بارسلونا میپیونده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90825" target="_blank">📅 20:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90824">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbIu9yHtecQVxlJ932QykSsAEyABRMxTGlDeWL4IAKwSC_r8zqRTMGpEZZwXb7tG_fMk-Q7XFHK_phP-lwdugjajfCkt_g8NVP-dpfVm3AeDYo9c4btaLjnBRtZCQbHNF69QDOizTZbvDcnp5lpGyrs5auPLg-B9Ke2mhoRmffCsEQvT0X9uzM1F33j8QWO0ZqtPvJOLVvm4MzS9kPCml8GhFTfZjebc-MXTTw_3hHrpu6BSJ8XuSZnwUlUJjeRXhOH7Sq1cVctuBSCqy7s19Bgbvz9p3EvlUaSMSSq-zvg2nBWGs1k9ZnyWw_k2nfZLeQr0RwfvUm0AUk4IFlcwdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ در صورت منتفی شدن جذب گواردیول، رئال‌مادرید با درخواست مورینیو بدنبال جذب کالافیوری ستاره آرسنال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90824" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90823">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=LJIIVuVANSQaTA6gyymFviz3EOJTj4ciU6KFmLCq5ccyvAXN534g3NoxH6uqY_OWqXtdHPvSz6M-xQflbjt4-43E98HVy-rP9cAzfYXAhIsG45-5v_RQ9F5MAhh0xBlQZDOJnsToa4UldgIbTfWpe6E4fRgk2PfAtCXjGWHCTqbv32H3dX9DmJM78Qx2hrwQWYqYyuUE--nAJuKjA_gH4-_tri8aPZyArhqfHdXJ_poH2nKpN2TkhsZlzPBQfj3VofLcIT8nqCLNdBx6V3Yoc0OCMZpOBOfYHZc8txHJikv9JLTJWTYbFD7sq3kqDih5bHZeQSOvpc0ejlUmJ4RiE3LIv5Bw-bNwWeCct07GLuXWga9isJZk5HpbbbbHj5OQn3XMSF14KZENChBhGKEhKwcI9x_8LCIfDrXDVUZpP0fr_5lo_U78XfMr9Q4tySb-2g2_D5DKd_MYc4zFgBgzvw5bvHHVaZM4BK-cJOeSGKWjAMSSuM05ruq1Elr6oL5fQAeo1qANEhmYuAMbRfj77kgMqnJbPMAFTr8CONWmYHMEoxKIPsCTOl_xpLPNm4mYpIG6J6edOlx0e8I7N0LtGTEr-zd5djQ4RsjMxYkjmF4TDtbGhw9k2jhOMxcaP4Hfyf2-gFHuusBjemzwy9y7BJcFznXt3Q4_CG4-0WGNIR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=LJIIVuVANSQaTA6gyymFviz3EOJTj4ciU6KFmLCq5ccyvAXN534g3NoxH6uqY_OWqXtdHPvSz6M-xQflbjt4-43E98HVy-rP9cAzfYXAhIsG45-5v_RQ9F5MAhh0xBlQZDOJnsToa4UldgIbTfWpe6E4fRgk2PfAtCXjGWHCTqbv32H3dX9DmJM78Qx2hrwQWYqYyuUE--nAJuKjA_gH4-_tri8aPZyArhqfHdXJ_poH2nKpN2TkhsZlzPBQfj3VofLcIT8nqCLNdBx6V3Yoc0OCMZpOBOfYHZc8txHJikv9JLTJWTYbFD7sq3kqDih5bHZeQSOvpc0ejlUmJ4RiE3LIv5Bw-bNwWeCct07GLuXWga9isJZk5HpbbbbHj5OQn3XMSF14KZENChBhGKEhKwcI9x_8LCIfDrXDVUZpP0fr_5lo_U78XfMr9Q4tySb-2g2_D5DKd_MYc4zFgBgzvw5bvHHVaZM4BK-cJOeSGKWjAMSSuM05ruq1Elr6oL5fQAeo1qANEhmYuAMbRfj77kgMqnJbPMAFTr8CONWmYHMEoxKIPsCTOl_xpLPNm4mYpIG6J6edOlx0e8I7N0LtGTEr-zd5djQ4RsjMxYkjmF4TDtbGhw9k2jhOMxcaP4Hfyf2-gFHuusBjemzwy9y7BJcFznXt3Q4_CG4-0WGNIR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدمممم ینی؛
مصاحبه شاهکار این مرد وایرال شده؛ نزدیک خونش رو زدن و اومدن باهاش مصاحبه کنن
😂
😂
😂
+ خبرنگار: شما که خونه نبودین.
_ نه ولی کیرم دهن اسرائیل.
+ خبرنگار عع این حرفا چیه آقا
_ خب الان چی بگم؟ بگم ببخشین آقای نیتینیاهو کصکش؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90823" target="_blank">📅 20:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90822">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=hZXidUBd1B9offbjnNy5kuERSd59F8TKKNctgavFkt-6fQgQM3GrK9V1K69oOpxHXvTYyhkn_7knuEyF2TOmRcHbIlEz1gPDDKcuyLO82ONzsruzwLdob6_LcozE2IvPKupfNpfx6dg-9zxQQQsRttwwmPM3MH5Ms1LmhT6jyHsJa5IfRiB_YA-1TIeiWJx_QqijIKAjTr2kdhSsPfybQZ8seV7mE8oS9uqK6XOKtLNokHxGaGyo0Bi9eB4uqHSrszOi1_6GWhe1O8NQyp6h9zZPUV5KDS0784mGzvqEgOyHy3HvPV_AslZLEdWMUjorMFvYpoinfgLXIzNOLlolAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=hZXidUBd1B9offbjnNy5kuERSd59F8TKKNctgavFkt-6fQgQM3GrK9V1K69oOpxHXvTYyhkn_7knuEyF2TOmRcHbIlEz1gPDDKcuyLO82ONzsruzwLdob6_LcozE2IvPKupfNpfx6dg-9zxQQQsRttwwmPM3MH5Ms1LmhT6jyHsJa5IfRiB_YA-1TIeiWJx_QqijIKAjTr2kdhSsPfybQZ8seV7mE8oS9uqK6XOKtLNokHxGaGyo0Bi9eB4uqHSrszOi1_6GWhe1O8NQyp6h9zZPUV5KDS0784mGzvqEgOyHy3HvPV_AslZLEdWMUjorMFvYpoinfgLXIzNOLlolAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ گواردیولا برای پپسی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90822" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90821">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=feLWmozFtiJl1JURmfThcYd5Uq4pi5AUbduK8NSf3TxKnZXAv6a19gfSMjmPK1ozWpjYt749eXrcQ94ZEeCBQvoTQ7rkzwvZaUzZ6u_k70Mt-Ywk2kxgKJDuYNNxi-q_tg1oL9J8FCbzcV3I1lFLYQkKiO95m_qjbg8Eh9yK-YCa_MIwz0oSkVIlwPsPi2Jc6fmTga7I7VeErzIAalF_1t4y4Xs5nVgzNA2YLs9Z4YlyHs6Q7yOy4JK3lSfa9SwdJaZbWIscVMCnNJWKHhLwsdfm8yMKZG447vyYe40R9U3qY6qug-i_x_CGIKM1i3rbM8s6fP4x2bNuwHrj7MLikA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=feLWmozFtiJl1JURmfThcYd5Uq4pi5AUbduK8NSf3TxKnZXAv6a19gfSMjmPK1ozWpjYt749eXrcQ94ZEeCBQvoTQ7rkzwvZaUzZ6u_k70Mt-Ywk2kxgKJDuYNNxi-q_tg1oL9J8FCbzcV3I1lFLYQkKiO95m_qjbg8Eh9yK-YCa_MIwz0oSkVIlwPsPi2Jc6fmTga7I7VeErzIAalF_1t4y4Xs5nVgzNA2YLs9Z4YlyHs6Q7yOy4JK3lSfa9SwdJaZbWIscVMCnNJWKHhLwsdfm8yMKZG447vyYe40R9U3qY6qug-i_x_CGIKM1i3rbM8s6fP4x2bNuwHrj7MLikA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف عکاسی با رونالدو توسط بازیکنان زنان پرتغال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90821" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90820">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=h5mWIPKAC_VHHQnBd5-R-1mm5CdMzFyuNz2PGYZNgBUKDRN0eWq-kigZYBB7UyQ7jXO3otkHfeDo9At_jOVW41b-GVudv4LjIj8Ccs-dKb6g3M-zN7FDbzxI8YuTf_C_QmwYShqDvhx0UDzemvD4Jcux0CCQc0sgo2i1QDF2Vxcr-rda-V6e9CL2FgI_apcrA3K58UrXtx-Mlp8oN1uBrZajI1wEPqMiivH7BYCFdqnox53XLePl3jOy2hMASR661iqlc__cTd2ezOPYA2MZ1URDSQu835nFggarrT94vEHa95A31ye7iO4pZhZXnawQN6Wm2j3QlIqxq7EPml_zbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=h5mWIPKAC_VHHQnBd5-R-1mm5CdMzFyuNz2PGYZNgBUKDRN0eWq-kigZYBB7UyQ7jXO3otkHfeDo9At_jOVW41b-GVudv4LjIj8Ccs-dKb6g3M-zN7FDbzxI8YuTf_C_QmwYShqDvhx0UDzemvD4Jcux0CCQc0sgo2i1QDF2Vxcr-rda-V6e9CL2FgI_apcrA3K58UrXtx-Mlp8oN1uBrZajI1wEPqMiivH7BYCFdqnox53XLePl3jOy2hMASR661iqlc__cTd2ezOPYA2MZ1URDSQu835nFggarrT94vEHa95A31ye7iO4pZhZXnawQN6Wm2j3QlIqxq7EPml_zbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
ویدیو منتشر شده عجیب از دولا پهنا شدن بازیکنای تیم قهرمان کره‌شمالی با حضور رهبر این کشور
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90820" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90819">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNEX VPN</strong></div>
<div class="tg-text">⭕
محدودیتی که لازم بود برداشته بشه برای پایین اومدن قیمت کانفیگ برداشته شد
❗️
گرون نخرید
⭕
طی ساعات آینده قیمت هامون به قیمت های قبل از جنگ برمیگرده
😇
منتظر باشید …
آیدی کانال :
@nexphonevpn
آیدی ربات :
@nexvpnshop_bot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90819" target="_blank">📅 19:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90818">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
#فوووووری
؛ باشگاه موناکو فرانسه بدنبال جذب مارک کاسادو هافبک  بارسا؛ احتمالا بارسلونا از فروش این بازیکن رقمی بیش از ۲۰ میلیون یورو درخواست کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90818" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90817">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90817" target="_blank">📅 19:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90816">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cylhf5cFwfSga7P9NXcuAoQx-9SRnC67jTOn6o0RWV8W3b0ZZUB9zjueXFCV9LoeplAK-hHZvWTclPd7KOCoGn0hF1JCbuPYa7Qj7J_miF1BK5HYb63TYhD9tM_voCjMEPWbUzSXneE4FGlkYLNO6_ibzA6l9-b0ln4EKZR4h_F4vcjvDnmfPT9TV7nPigrgr-DReOB2hjG3cJWqDCRX140yj1ulsQVdIVpSPSoXHUxpjx0JymFhvSnd125iGI1O-Ha7pqH04uc8FqSvKlgXqj_-b7nZnk8FVRWyW5DeElGTHFglsUv-VCJplo-6pCBR3AO2gFsyZB-w2D4Ud0xHyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کونده :
«تا سال ۲۰۳۰ قرارداد دارم. در ذهن من ، موضوع تا حد زیادی روشن است. وقتی در اردوی تیم ملی فرانسه هستم ، این مسائل در حاشیه قرار می‌گیرند. فعلاً تمام تمرکزم روی مسابقات است. من در بارسلونا هستم و امیدوارم به حضورم در آنجا ادامه دهم.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90816" target="_blank">📅 19:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90815">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تهیه کننده برنامه پاورقی: خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90815" target="_blank">📅 19:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90814">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNVhwUwHZs-Z5QR-5vEUKQjCKhEKI5IpfS_jQZorw5Bh8uympipVebGNHDEtB3L9k9Z9qg9LvqWUL4VfM3A1p5amT2TIu9aZBN4cBAEsnC-c4SFeeGP3LHYfC2gIDHFEoymEsK8XpVYqnpbZmykRBGEJ0zlpo4T0aI36ZNI4vTTFEpKMKWJLX3wdGbiswNKSi8WhpeuxTCc0WdCSPoXVarkZkgWSKUZLOMO-cuJ0j1OEnpOcnSFiT4ZCAeslMERTEc9aS-NE-HRUsHGN9pnuqmbeCBf3QpEcIcXDWUdNQQIK_Ci8yy-UfDuOTzF0ylFbq9QXF4qsNXnC99XlcyrwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز هیچکس نفهمیده چرا زبون ویتینیا آبیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90814" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90813">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تهیه کننده برنامه پاورقی:
خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90813" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90810">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX2IVPzdgXbG7i9LCkDlf4DyDo1li2Q-wmtgJb1T4VA8DhpaoTxt7y-QGbYzG-IxIh6bsmu2UJc4goOhFUoHsLc7-ap1j6MJbhti9Qq6YvKt5RYLy_lOfPiYeioDcVCPvwhIujdRrVRiA6pddXA89p2QoMu2ZqFQPxOtPpMTikLFmTzTXD4d18Y_VNxowtS3pYL4pxtInW9Fg0UcSS8E3aS20flsuxE5KuXsotbHAG2C7v2k-77QM-5lDResmefRlMbAk7UkVB5FeShZFTTB9YIO6jVWVsU3ST8eX4XN9tdYbk4ehgd6gpOEStoBuR85cJoj0PW-TgOJs7hg37EXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90810" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90809">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaKvRreD3tYGosCippIoKuAvQip5miOLYGNJoHsfHT4nzo9Hc-w-FM8SyYG7y5fihEyP5x_x6XBqI12AmF8ukpfEhEdrZfl1tzSkVKIjlsx-ke_b0ZSyuq3-p6USAdSzVEHedMaC6CU8s2rHO3Ib88jPkEjl3GFnx2B7lwVdsk5i0OVIFRxSZn3nXI86lxRg3DbhOIH6MPnoL6dN7IroA4YRUQFYrKNzQq8uLcWGajaM4Swbnv1tzQF1pmLVSZGHIslWBuU2KoNNYNET1GtoZYpNNKf0-svLQ7kNN8m1Z_ey-_Hn34a-OebDYqd0F1IMEjEcBO2E-WcG8VjkSrSxqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل کمپ ۴۸ تیم حاضر در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90809" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90808">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEtRzrGQ04WDZIkuCUnqNy5O9MoV-Zb4zr2Hw_TUvGYNEHwHFdtDdCIE0h8U57mt_s7tJ8uqRDmlj8yaDQjLX_6otLGTTBSSWkCI2IveN-5bO2n7LXsi0gFk4tRoljC_YcHdeR5uvarUs-VjBb3HyiDhCQX7NRro0UIrUI1CBlnysaVs8MHCHVObzLwwU6GOK75-WXLIbCTJoIIqJYEtobI3Phj32AlMP9IuzO2X9fyd0O0juXxBx0VvjBP5s-sMq6eQ8UbaezJTSiQIYFHJDxGg49WD2VX00_0FENaRTJGc4mgxUG1XbElSWQtZ8_twlNmIcy1CLhJd-5cbtYSetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی و ثابت تیم اردشیر تو جام جهانی طبق گفته رسانه ها:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90808" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90807">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjIAw8PzxHz3nq6cXCWykAVF93AWxr9D8-D7oW3XAXgUTxq95aqlnSB4ffUHhrtVqcID2_4MOS2X-GyKeBRcPMCd_WHOr2QTMSOaXu9oW9G6MB1mNCnpOwW1tQWoAECn08u1aak269qpx_RDn-KZp6UwjXuE-7CTL96FchOVCUuzq9hxCm5okGqWcBoqYHBTA_JhaPyASd146-TAlqEw70Ox6_53ZdDdRMjCbfvpm_RnrsTVPA2pygILQXjlmeVyMN9rhXzblaqEma1ZIvHAS2iF-GKRnhMWMyN1afT4gjVwk2-a-8l1h4g3ULxaMRhF4vtWNA3cPdVkPNJBaJnOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یحیی گل‌محمدی در آستانه سرمربیگری تیم دهوک عراق قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90807" target="_blank">📅 17:44 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
