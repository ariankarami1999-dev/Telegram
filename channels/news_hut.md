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
<img src="https://cdn4.telesco.pe/file/YY-4eU9szcio3jYsSIK7XMye_jOm4spUPlrh53aQYlFe7ejE6st-wmMG3t7zWAPtrD6i5JUQsT6RtKzCuNhTW363kHclFjTFCoW4I-91UWM-xGK3m0MpXAOXtjqpBTo_feooY1CC_yyLNhhThs6nujWoybJqdUClhDqk8B-ujRkXiGFTFAiLg7b6xHWIHy5R4z5HRuYgqNl39ptnGxBjWCeG-27lynKW2JWmYWUInte4CMsQTTrpAX2IswXKc-1qWoTBqtp50Ci3mgiL9uy_rXsovP4Mv_gqP6PYYZWlrdl8csm2bclFJv9boB6aAacz-bal6nPZtMEqx-MzM4_FeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 136K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 11:56:10</div>
<hr>

<div class="tg-post" id="msg-69457">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=qg_5UzcXVRCXktS90XlIXy2NHWCEvKXEzlp1dBRMvjuQVJn-JvlZP1366oXK_cD-8gvc2EVLUIfKZVQGydIOIsSle0hXweQOHjDGIhgfddhdbevLL2ldiLE2syAlD07hxFCDjHsh7UWqnT4QPToe7ZDcesWvUBECw6QUXArHYG1VZ2dUKn0-MygOWsh4W-rS1OaXNrt8yP7rtVaQLcRRrFJpOtDZtrlizG5m9NzBDmiaG-kz6SazoMFbtqZ_uUknbBnX-jpziBfrSqfbS6zmvrgHXF6lteFGkKtdKjlsjOvdga-z4-or8RUM5dWoeS0YxS89RRn-De0Ek6Ee0Xx1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=qg_5UzcXVRCXktS90XlIXy2NHWCEvKXEzlp1dBRMvjuQVJn-JvlZP1366oXK_cD-8gvc2EVLUIfKZVQGydIOIsSle0hXweQOHjDGIhgfddhdbevLL2ldiLE2syAlD07hxFCDjHsh7UWqnT4QPToe7ZDcesWvUBECw6QUXArHYG1VZ2dUKn0-MygOWsh4W-rS1OaXNrt8yP7rtVaQLcRRrFJpOtDZtrlizG5m9NzBDmiaG-kz6SazoMFbtqZ_uUknbBnX-jpziBfrSqfbS6zmvrgHXF6lteFGkKtdKjlsjOvdga-z4-or8RUM5dWoeS0YxS89RRn-De0Ek6Ee0Xx1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله پهپادی روز گذشته به مرکز لجستیکی عظیم شرکت وایلدبریز (Wildberries) در نزدیکی سامارا.
@News_Hut</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/news_hut/69457" target="_blank">📅 11:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGUpokH7Ij-jtv-FwGsKpEjaEQ2VKd8pWFrmxDhSIODySUd-toCiPCEgxHhd-cSz7zbh5tK3dUbtUL1p6k2B5BOayKmoy8LLhgbqoqrdSGiSzVJ5i635w5K6a6kAGXa84sb2A3WzxMIxqHjK5LuLS21mlSA83aMsGn2YoySGkDuI1bY_xMvMkhnDgmBGVJIoYkllxzcuSCshH1Ct-zDeASshi9rpBVfMFBxIO8evp-m4aXGLvAtNrGBS0rVtzEJMIkYFFF71SVQYreJg9Lkv1a41kOkC-e4PH_VpbxlLQ2OFIChZAIIsHh-BxnNeKEv48XA0Dmv61AvR32PQ5ACUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=NfMJxKI86r_p96HQ7FEYIcVj8ecNwbrQWb63spYYUPHYdHxBdYkceppoPPuG7zxRdBR5u2S_OhEgejHu2RdgmQjbf3_3v31VIHd2jHXemwihnpE_onaQhAsiNOlRby5EGGwi0ufKu4MpGmVDu6CqagSMFwITAMyyaPPcuIWDmzwr8cgrfy81z6XF2A24rPvZghuJQABCnFWLL-eOk1oxHbWhMbZOCwxUbIKXkPgkJCBE5dq8SZWykatMCq2PsC8yhbntW08HzMYX5dY881-jLgbU29O3WbKbEgtdD7oZB1vA5LZn783JOKmcYvXvCFA5aM3QUDgv0Yeav-TSqW87GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=NfMJxKI86r_p96HQ7FEYIcVj8ecNwbrQWb63spYYUPHYdHxBdYkceppoPPuG7zxRdBR5u2S_OhEgejHu2RdgmQjbf3_3v31VIHd2jHXemwihnpE_onaQhAsiNOlRby5EGGwi0ufKu4MpGmVDu6CqagSMFwITAMyyaPPcuIWDmzwr8cgrfy81z6XF2A24rPvZghuJQABCnFWLL-eOk1oxHbWhMbZOCwxUbIKXkPgkJCBE5dq8SZWykatMCq2PsC8yhbntW08HzMYX5dY881-jLgbU29O3WbKbEgtdD7oZB1vA5LZn783JOKmcYvXvCFA5aM3QUDgv0Yeav-TSqW87GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده مردم در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/news_hut/69455" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69454">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=XtJaBmYfF_6Xdio9FJjElrpA5kAAdQM0eeiQM_sLKmAblUKxajjbSpB59AsVJof2HGtrVT78XKn5VhOK-N4J0E8wc7RdTTzDXLNcEVswn_YviXNUD8UJkjaWoR4UFREI0-rIraIdAeGF-o1_Ya-dgNplP0QI4uWihuIdAvwRDqZuCTmHuOvvoRDBUEIcu7twrEo30KwATDVClG0adM0SXemcLMQ7DBecrlgJ2oJoM4jTnJKiW-GhUY0SiqniMnUAX0T9_Lxd-Yd03GmX0IhLoUf18uh5XPubaeTwHkvLJZcH1HLrmyoNPyDHYe0qAnLOUYMdhYiFo6yaUE8Pk6EnGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=XtJaBmYfF_6Xdio9FJjElrpA5kAAdQM0eeiQM_sLKmAblUKxajjbSpB59AsVJof2HGtrVT78XKn5VhOK-N4J0E8wc7RdTTzDXLNcEVswn_YviXNUD8UJkjaWoR4UFREI0-rIraIdAeGF-o1_Ya-dgNplP0QI4uWihuIdAvwRDqZuCTmHuOvvoRDBUEIcu7twrEo30KwATDVClG0adM0SXemcLMQ7DBecrlgJ2oJoM4jTnJKiW-GhUY0SiqniMnUAX0T9_Lxd-Yd03GmX0IhLoUf18uh5XPubaeTwHkvLJZcH1HLrmyoNPyDHYe0qAnLOUYMdhYiFo6yaUE8Pk6EnGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای ازجواد موگویی که توی برنامش داره خیلی شیک و مجلسی جای همه فرمانده‌ها و مسئولان رو لو میده:
@News_Hut</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/news_hut/69454" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69453">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVFmW8vr1PjKY43PaiTvD3nQkELpD5Z5BD6gnXhLqBrtL1-uWe4quTmAeRKaoHcCgzUaMszioy-IFFvmUoBOJTvFo0mimR8hPwicoUHJ0rgqM12u_yMQzLkKt4ZLMsdVEs_OjoJknJ-KFukh_fWwxhRQ4xlUPKzTLpyQ_42q20Y0wB3NagJKOcATzwghn6IAORUXL4ZbNtW0MqzTTZC8KbqUP1T-CDhYFanq0TlIXQ71DxmLau5N7UWpAHstldpPJNAvO3ZPjKc-c4tkuALgsyobP-XkUfZ5c6b2J4OFARqSYGR_djsfR0kM1pbrUpvQCIpmFy7fKKAm5oMFuseUr8Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVFmW8vr1PjKY43PaiTvD3nQkELpD5Z5BD6gnXhLqBrtL1-uWe4quTmAeRKaoHcCgzUaMszioy-IFFvmUoBOJTvFo0mimR8hPwicoUHJ0rgqM12u_yMQzLkKt4ZLMsdVEs_OjoJknJ-KFukh_fWwxhRQ4xlUPKzTLpyQ_42q20Y0wB3NagJKOcATzwghn6IAORUXL4ZbNtW0MqzTTZC8KbqUP1T-CDhYFanq0TlIXQ71DxmLau5N7UWpAHstldpPJNAvO3ZPjKc-c4tkuALgsyobP-XkUfZ5c6b2J4OFARqSYGR_djsfR0kM1pbrUpvQCIpmFy7fKKAm5oMFuseUr8Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مارک لوین:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/69453" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69452">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998caf4317.mp4?token=aIXm5xWibsa_RPwJlHvk1xWy0hmboMDss-87RH7Yexf4WcSulX7IAMh-KFPM0BrtSTvrglh86buNOy3T5nUKTQvPrrx0Kj66DNWWUUPIOeinKC9zIfeu_09E0eTL8WQkfBBQcBFcGsuX5XWIG-tQWd4Wl12_yX43twDZyR3fXmJZiuOTqv5T1hlcDEZ6GEbpShXLr7qp3cmU5JYCmLA7HxuQ9PzmJA8iSS7piLTvCjiordTWyLgHNZda4uQ79G56cXAAMVnJaVl8bU7TBbSKSDtkrzobwCP2NxYz5fdtb4RJLgU82LZuefrbPV9NIHz6-UsPTxUP_5Ig2cDqn2tskXqIS0_oVw7UWkDFIzKlmKkQoVh5VQuVYX3H5UcTRl_bltBA0xLgrZEkwBr84pNLkanCU6D8_9S-Ao3DuPb57x0BjniGFtvw0ULfyPVSQIFqy4TtPNaMMSCHni81RXkdveMO7Ixobs2lsx7vP7asib5WwZ8GycI-jtyJ0OKU08mHr2wt6R8tOLsG4Be0dClFWgjC1SDRAgOdVz2jz9bobKw3fYJBpSOvFXS8qHN_Vq-LYIgLdGgEQvf6vv6C1BGDbp784T3nwXMaCVq6jm1sNRga-gLEWeMjfH7ff3u775AG6U0WsS1i6t4rS1k_9IV5kaqZAWnAMKUFygk6PRYG3BE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998caf4317.mp4?token=aIXm5xWibsa_RPwJlHvk1xWy0hmboMDss-87RH7Yexf4WcSulX7IAMh-KFPM0BrtSTvrglh86buNOy3T5nUKTQvPrrx0Kj66DNWWUUPIOeinKC9zIfeu_09E0eTL8WQkfBBQcBFcGsuX5XWIG-tQWd4Wl12_yX43twDZyR3fXmJZiuOTqv5T1hlcDEZ6GEbpShXLr7qp3cmU5JYCmLA7HxuQ9PzmJA8iSS7piLTvCjiordTWyLgHNZda4uQ79G56cXAAMVnJaVl8bU7TBbSKSDtkrzobwCP2NxYz5fdtb4RJLgU82LZuefrbPV9NIHz6-UsPTxUP_5Ig2cDqn2tskXqIS0_oVw7UWkDFIzKlmKkQoVh5VQuVYX3H5UcTRl_bltBA0xLgrZEkwBr84pNLkanCU6D8_9S-Ao3DuPb57x0BjniGFtvw0ULfyPVSQIFqy4TtPNaMMSCHni81RXkdveMO7Ixobs2lsx7vP7asib5WwZ8GycI-jtyJ0OKU08mHr2wt6R8tOLsG4Be0dClFWgjC1SDRAgOdVz2jz9bobKw3fYJBpSOvFXS8qHN_Vq-LYIgLdGgEQvf6vv6C1BGDbp784T3nwXMaCVq6jm1sNRga-gLEWeMjfH7ff3u775AG6U0WsS1i6t4rS1k_9IV5kaqZAWnAMKUFygk6PRYG3BE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇱
🇺🇸
ویدیویی جدید از لحظه بمباران خیابان فردوسی در زمان جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69452" target="_blank">📅 09:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69451">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHXFvf14gxyCa4uwNuBQqigDbSZzwNcjl1mJFtV7IGcNhqxvC10N5K8IMeXM60ImltRYxepGipdvhht0CAvehqlBLEvZe3KDySK4EMpMxjZvzqYBgPHAi43gb82cV_mm7OzsUf87hX3knls0mVPWFJGXHkRZBjvYyft4vPvrxlcpqUMBG9rTtb-nUywdk81D2OZtBox8_GTnoc3fA2eKbIQ7we4WESep6zLwe_go5Rf2o0KOIiPo4rNe9Y77mVSr5tRu1NTzM7SC59lZrhgTLx2nasRDcqzsFU456llWY44auYqMy2Y8j3Q4t8JE80yRtzx8XdIdQ16B2STBdYelXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هگست وزیر جنگ آمریکا:
واقعیت.
وزارت جنگ آماده‌ی حمله بود - و همچنان آماده است - در سطحی که از جنگ جهانی دوم دیده نشده است.
قفل و بارگذاری شده(آماده اقدام).
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69451" target="_blank">📅 03:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69450">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TCzMS5UUZ1BMM78etqNXzlE-bpbage7ASx2FXjT3jLDmTJmxAkw52oijgqgkKCAgrnMAv9Yd6-Gdz4Kael2sVxKK1C9LQeMkVMA3Lh9Pis2J_nCcLYl8pL_0Oj-iXHVxzEaKrqvoOAa9__c2KTcEwnDd3p_QbIOaXLqEeKRUDKRtiQ-ysXRFdCaIeaQeOAs359YaNGkJiVcu67e2z8KMtIXSu_KD52vTTMF2leN0_UpT_QfHepGBKUlO8Gb_ZQ7J42mUHyboIu5XqeIpa-u8XPcyMkoRA8U17FlPb6LcRENNrM4TmF-brNMQQy3tNPjsF9A97TfApSiRRBzZ0rd0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پست جدید کاخ سفید:
به ترامپ اعتماد کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69450" target="_blank">📅 01:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69449">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQlVjXNY8AM4H02TICyOvXO1FH2DQwXnw5hL8qqGuG0KSTwclleQhVKJ15SYLTLz4ZKwI5ViwirfotJ6J-zhvfkVQvz1E1VwvdI-3eFpe9kAE3uC09FTRB7rMabVcA9zCherditXwJgkJvI031ipfPaINukqX9IESz9HO6PLDc9N1cRnedyVppG_kyzI-ZMvcQVoncgj6j3cGuRBFVNGKQH5_a8LjRYTxo4GPHtgq6xxHSF63pmnVy6imp1Nh19cy77E0VudCLx7ptSSFEEA5xSfr0zH68cqpFkSTO5uFd5GZDscBr9FQGAss0gyK5jX11s8zrYHbirolD2shN2nvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرقی خصبِ عمان دریافت شده است. مقامات در حال بررسی موضوع هستند و به شناورهای حاضر در منطقه توصیه شده است که احتیاط کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69449" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69448">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
وسط حرفای ترامپ یه کشتی تو تنگه هرمز هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69448" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69447">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=AWTRENLFkXwEotFpTmvoNi7qoRMUM5PEUmHMUeH63hLgFxykxZmWMPoQJ0dH1zfLu9RMby-y3cDJKl6fgYy8TiivGaxIq8ODnFKUnB8dpiSF2CXZ2ADKL3jFDJpSJ7xQAEBzE-OHYfpegpEKT_-7ggcCxmSocj0hcXZeK2KPmgwiCobP5yDB9TfXzBOUmdHc74L5khuzfZ4IvYtF0oZZJC7rGdrMuQy549Ru4GZSESdhDzVN67MtR2jPel9TW_FYjO0uAedPm1sNwWSPm2zRoEewgmAfgvAkNJfoyL2bGkUF9qhNoVYYixQhndg8A8JrvlY3YZywK_eOOT98mGEDXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=AWTRENLFkXwEotFpTmvoNi7qoRMUM5PEUmHMUeH63hLgFxykxZmWMPoQJ0dH1zfLu9RMby-y3cDJKl6fgYy8TiivGaxIq8ODnFKUnB8dpiSF2CXZ2ADKL3jFDJpSJ7xQAEBzE-OHYfpegpEKT_-7ggcCxmSocj0hcXZeK2KPmgwiCobP5yDB9TfXzBOUmdHc74L5khuzfZ4IvYtF0oZZJC7rGdrMuQy549Ru4GZSESdhDzVN67MtR2jPel9TW_FYjO0uAedPm1sNwWSPm2zRoEewgmAfgvAkNJfoyL2bGkUF9qhNoVYYixQhndg8A8JrvlY3YZywK_eOOT98mGEDXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
نمی‌دانید این حملات به کجا ختم می‌شود.
منظورم این است که آیا همسایگان ایران با هجوم سیل‌وار جمعیت به کشورهایشان مواجه خواهند شد؟
یک فاجعه. اتفاقات بد بسیاری ممکن است رخ دهد.
ترجیح می‌دهم توافق کنم. به دنبال کشتن آدم‌ها نیستم.
آدم‌ها می‌میرند؛ خیلی‌ها می‌میرند. ما چنین چیزی نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69447" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69446">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=CVp1UQY7NOZO-G5buANGUMaTS6H8ZdCjPQEaXS7JvGT_X7JdaG6J0bGPv3mwCl4y1XM_K-4vXSTaZt0wclSn_xHKegoEIt7vbc75uY59g6BVtPhd80bdTBZ-8hTf-Fiotr19x4prKo9HjrUxs0r4u4mlUl4pK2TkHRr93Ud_wQnnMoOv1vw8YHamsiNcNcmTg4FYoce4OkGUxfXnRxi6wtuapbIZPW_eUOeEoDyFCtiqHyFZ9KDO9q9s_w-JzLcERKLIHK8OA13HrhPJlYfiQW8RfVlCbyb6-9VnXhFit8fy5DPTqkg8hvTiirfHcRvy5Wf0juGU3lDRZnID2eZ6rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=CVp1UQY7NOZO-G5buANGUMaTS6H8ZdCjPQEaXS7JvGT_X7JdaG6J0bGPv3mwCl4y1XM_K-4vXSTaZt0wclSn_xHKegoEIt7vbc75uY59g6BVtPhd80bdTBZ-8hTf-Fiotr19x4prKo9HjrUxs0r4u4mlUl4pK2TkHRr93Ud_wQnnMoOv1vw8YHamsiNcNcmTg4FYoce4OkGUxfXnRxi6wtuapbIZPW_eUOeEoDyFCtiqHyFZ9KDO9q9s_w-JzLcERKLIHK8OA13HrhPJlYfiQW8RfVlCbyb6-9VnXhFit8fy5DPTqkg8hvTiirfHcRvy5Wf0juGU3lDRZnID2eZ6rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست.
آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69446" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69445">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=qU-GdSz8BNNHbwIAeFDz8HzugE1SnQ0hAtURh7qg_bcfmycoLfSXchL9ej53DAa1mzjCGBJOpbmOtJcTCgLx1tQinitxUusez8ybN4GH3rY8g886sclcfbD78mPOFTdwXCJq3QRWJIXgRLolE6-2HTGwoZzfvn7rJCq1yaaDuTAW-7HbQ5bd78e9wW7VdY18YKYaWJ35CM5niyqVMsBIsD_hq18ZVcYm7zfFyuY4xWYQqF1HznYZ0D_rHheD_NR3D9Zhnx0l-Z5bEr4ePzZYHHHZMgDsZ66ThgXv3CGSxvXEtizNy0aT03_zoxFGSx4dxRG1ocdACeIjOjSi06sTDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=qU-GdSz8BNNHbwIAeFDz8HzugE1SnQ0hAtURh7qg_bcfmycoLfSXchL9ej53DAa1mzjCGBJOpbmOtJcTCgLx1tQinitxUusez8ybN4GH3rY8g886sclcfbD78mPOFTdwXCJq3QRWJIXgRLolE6-2HTGwoZzfvn7rJCq1yaaDuTAW-7HbQ5bd78e9wW7VdY18YKYaWJ35CM5niyqVMsBIsD_hq18ZVcYm7zfFyuY4xWYQqF1HznYZ0D_rHheD_NR3D9Zhnx0l-Z5bEr4ePzZYHHHZMgDsZ66ThgXv3CGSxvXEtizNy0aT03_zoxFGSx4dxRG1ocdACeIjOjSi06sTDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایه‌هایشان هم همین را گفتند.
ما فقط می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69445" target="_blank">📅 01:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69444">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=K8ARUyN_azeqFM_MKRHk1okislVINMm99jAacN9ebJ7R5Za3S8fm8rTky9b1JS_CtD0fWWuFD_yFN8loXREr2jfx6dgWM2uuHGdF7bBta4P_qZ0_qVPZun0tmVZiTCbkZeYkiHQCft2MHQjZBMa29aI9_QNwldb8fd7c1ztpzKH3Eks8RLkT92VJLczGZkVzqQWjGQNEwUBxuUVCvIWkeGlKbc-sh9vsIlUSEsPg_9OIQ15ZamM2okjSzBg_aMG4sRU6ZOIIc-vxLKKTOpl83n13NszXEq4_ZP6U0vW8ZsOOh1yIXUJbVbARjaW3U6adWetKk4sBeBBvurywTuiLcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=K8ARUyN_azeqFM_MKRHk1okislVINMm99jAacN9ebJ7R5Za3S8fm8rTky9b1JS_CtD0fWWuFD_yFN8loXREr2jfx6dgWM2uuHGdF7bBta4P_qZ0_qVPZun0tmVZiTCbkZeYkiHQCft2MHQjZBMa29aI9_QNwldb8fd7c1ztpzKH3Eks8RLkT92VJLczGZkVzqQWjGQNEwUBxuUVCvIWkeGlKbc-sh9vsIlUSEsPg_9OIQ15ZamM2okjSzBg_aMG4sRU6ZOIIc-vxLKKTOpl83n13NszXEq4_ZP6U0vW8ZsOOh1yIXUJbVbARjaW3U6adWetKk4sBeBBvurywTuiLcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره بمباران ایران:
گروهی از افراد هستند که خیلی دوست دارند من این کار را انجام دهم—صرفاً انجامش دهم—و گروه دیگری هم هستند که نمی‌خواهند من این کار را بکنم.
🎙
خبرنگار: آیا ایران برای دستیابی به توافق ضرب‌الاجلی دارد؟
🇺🇸
ترامپ:
خواهیم دید. من به دنبال کشتن مردم نیستم.
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
🎙
خبرنگار: گزارشی وجود دارد که می‌گوید شما در حال خارج کردن نیروهای آمریکایی از کویت و بحرین هستید.
⏺
🇺🇸
ترامپ:
نمیخواهم در این باره اظهار نظر کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69444" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69443">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=NomW06NuG-SA8x2-gsb7FqI41deodzj4op0YriP3LENSrGSGUwJ-7wv16OfFkvxVHr5oHvxtWmYVwB9M2l5FyfJZurFOwL_FXeEnTOfOmntUpG1fn3la0Kfg5TkilITrHj7OLaDQyX1bCDW2O0cDzNJKtifcv1FNtiCImvEt_-AzgHVq8bKLcDrTnedSTde75npcSgBZCAUeWA5R0mU8AV0CJb208w2CIY2YMl3c9TpyVJun4j5TcDqW07y0jZGdgjEz4kMrHL_l5utYSm6VPfOcNGSWi2Yr8klKbZY0CL2GqJ9CjgKG4lLezpQLhkAz4GN-hhRFDeHPsIiagmo88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=NomW06NuG-SA8x2-gsb7FqI41deodzj4op0YriP3LENSrGSGUwJ-7wv16OfFkvxVHr5oHvxtWmYVwB9M2l5FyfJZurFOwL_FXeEnTOfOmntUpG1fn3la0Kfg5TkilITrHj7OLaDQyX1bCDW2O0cDzNJKtifcv1FNtiCImvEt_-AzgHVq8bKLcDrTnedSTde75npcSgBZCAUeWA5R0mU8AV0CJb208w2CIY2YMl3c9TpyVJun4j5TcDqW07y0jZGdgjEz4kMrHL_l5utYSm6VPfOcNGSWi2Yr8klKbZY0CL2GqJ9CjgKG4lLezpQLhkAz4GN-hhRFDeHPsIiagmo88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: در مورد ایران، حالا چه پیش می‌آید؟
🇺🇸
املاکی:
ما در حال گفتگو با آن‌ها هستیم. این گفتگوها از بعدازظهر فردا آغاز می‌شود. این کار جان‌های بسیاری را نجات خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69443" target="_blank">📅 01:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69442">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=PPcQndbI2jLrYmbbRkFn_Cv63l1zycGafZy1tGtN0bdvjjXEWwlQGY9e6q2slhE8X-aU2-YLdw8Vj4ioEnQ1ljwYFbdLcOT5kY1G4fLRA6mfR_k_BiOy1lRvpsTzsdPjFyYchUj-n9t4UohvvH60wk6Yo9nmUIS3mRqE2psryiPOWzAs9mGe1syNMQvB_Up49toWCVD1wwO86rrfrhsLHkeiS53pYERPmg1CGg3WS9rrTFv7NB-ShSJdZQc_ojRHDYKZMk9mcRgh9SeVKrDs0DJRL3VRJiqamUg1vPZmsH2y9BGI-BzwdWNl5NrLFXDP7bNVUO9z_B7iAsHjuK1OWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=PPcQndbI2jLrYmbbRkFn_Cv63l1zycGafZy1tGtN0bdvjjXEWwlQGY9e6q2slhE8X-aU2-YLdw8Vj4ioEnQ1ljwYFbdLcOT5kY1G4fLRA6mfR_k_BiOy1lRvpsTzsdPjFyYchUj-n9t4UohvvH60wk6Yo9nmUIS3mRqE2psryiPOWzAs9mGe1syNMQvB_Up49toWCVD1wwO86rrfrhsLHkeiS53pYERPmg1CGg3WS9rrTFv7NB-ShSJdZQc_ojRHDYKZMk9mcRgh9SeVKrDs0DJRL3VRJiqamUg1vPZmsH2y9BGI-BzwdWNl5NrLFXDP7bNVUO9z_B7iAsHjuK1OWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد ایران:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند که حملات را متوقف کنم.
حمله بزرگی می‌شد.
وقتی متحدان خواستند که آن را لغو کنیم، باید گفت: "خب، ببینیم چه می‌شود."
متحدان فکر می‌کنند که توافقی حاصل شده است. توافقی در مورد هرمز وجود دارد و توافقی در مورد هسته‌ای خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69442" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69441">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=gYm8Zwq2tlYclVz707nAiGsy8GhAs2CUEGHYFVi6iPtLynS1I3XR3crZI8ZKrjQ3aOQBPM3nXT8UcQ3PsNhc6r9aHnfHlwOiKozwgyLf7cm7sjETk4fxPK7elk4s3uYhfl62KiTln-2w-CGwfM2QaI1NlTc0XsElrtBEBPM_snWIpb7OMr2CYCk4ImbWiznVFbFT6cQh8wK6oQldzQuvYDqdjO4r0TuQyHXqRORAtbWNuju4tG0SfenWVaXsWyNr9ToSQCpc2diN00Nwnu_-OHcvNCBXA-UGtTqhGEwL-tbBzFSf1LNPQWmrFB6jLlscGHZjYPJ9-kP262CV645iPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=gYm8Zwq2tlYclVz707nAiGsy8GhAs2CUEGHYFVi6iPtLynS1I3XR3crZI8ZKrjQ3aOQBPM3nXT8UcQ3PsNhc6r9aHnfHlwOiKozwgyLf7cm7sjETk4fxPK7elk4s3uYhfl62KiTln-2w-CGwfM2QaI1NlTc0XsElrtBEBPM_snWIpb7OMr2CYCk4ImbWiznVFbFT6cQh8wK6oQldzQuvYDqdjO4r0TuQyHXqRORAtbWNuju4tG0SfenWVaXsWyNr9ToSQCpc2diN00Nwnu_-OHcvNCBXA-UGtTqhGEwL-tbBzFSf1LNPQWmrFB6jLlscGHZjYPJ9-kP262CV645iPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی وقتی می بینه دلار شده 190 هزار تومن و آب و برقم هر روز قطع میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69441" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69440">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93362f281c.mp4?token=Y5NJuv7jOcFx52BWy-W5lW9nBKeO_qRyQ2kjwHvGKfDwcu1KspCPXAnMuaVN926gxkY3ZrEaELfyfT11-ZO2mExiRp4ri_4q7tR4XtuPEGirsGU_air3aGDxeowLRi1rhPn56uVxyd55XjPeD-y9npyX57XKmeklCIT1mf181OqzEY0LXBafYiJvaqM8_HIo4y6ATB2cuSdCHwNPiultJxd94ZE-zxs0NnVn1645QIuC5V3j7ofpBRvH3_JrOjh7wIcyC_de2AYfJoNdAKN9oLHs1SAoVJ_Y5hkSuCsOevYbLpIZz6sG3cI13LiXVVyqx7FTh_53FwD5oX9hzgZ5hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93362f281c.mp4?token=Y5NJuv7jOcFx52BWy-W5lW9nBKeO_qRyQ2kjwHvGKfDwcu1KspCPXAnMuaVN926gxkY3ZrEaELfyfT11-ZO2mExiRp4ri_4q7tR4XtuPEGirsGU_air3aGDxeowLRi1rhPn56uVxyd55XjPeD-y9npyX57XKmeklCIT1mf181OqzEY0LXBafYiJvaqM8_HIo4y6ATB2cuSdCHwNPiultJxd94ZE-zxs0NnVn1645QIuC5V3j7ofpBRvH3_JrOjh7wIcyC_de2AYfJoNdAKN9oLHs1SAoVJ_Y5hkSuCsOevYbLpIZz6sG3cI13LiXVVyqx7FTh_53FwD5oX9hzgZ5hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
شوت برنده در مسابقات قهرمانی باشگاه بدمنستر! از تمام کسانی که شرکت کردند، بسیار سپاسگزارم.
من با امتیاز 70 برنده شدم و از این بابت بسیار مفتخرم، زیرا برخلاف سایر شرکت‌کنندگان، زمان بسیار کمی برای تمرین دارم، زیرا تمرکزم روی مسائل دیگری است.
این را "استعداد" می‌گویند و من آن را دارم، در حالی که آنها ندارند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69440" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69439">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsLd-lYl8htLb5cAZrksQQrvay1Lv9EBY74jh9Db94QYFkh6XjqyKYn0_hdEfzaEwVK7D-lOiVhQTt2fnA_vCzrpA5bvl-gFQ23IWGxaFKKDHqNiIn2PvmfOlx5pfChD1FvtdvhKRAJd1C5VZnl1X-Ywyk0Y0Z-mkkjUNKZtP55aGd_4t46C50r1pY-JoFJ087J727rsB0uLXTlXVJq-4pHTxaS1f_pjps6_XZ99aVciXsHHYCJ_jpACbdtTC_5g3Wt7Qhm_stACSFgTVcML8PJ3K4o8839ZtwvY9uZyMoiHflQIn72mBuU7va0OAjksIc4KO-TXabpxxTEYOU7Q8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پزشکیان:
تفاهم نامه که امضا شد حاصل خرد جمعی اعضای شعام بود
این تفاهم نامه ثقل روابط خارجی ما توی آینده هستش و باید دشمن رو وادار کنیم بهش پایبند باشه
امنیت کشور و منطقه و هم‌پیمانان با این تفاهم نامه ارتقا پیدا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69439" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69438">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⏺
شکار و هدف قرار دادن ۶۷ سرباز روس توسط مولتی روتورهای اوکراینی در اطراف پوکروفسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69438" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69437">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=rK8JWYgmHB_Bs9ViQ26L9b5GNCli_-ulgpQ0PUbNwJQNVT_lPtq6DEDl6VIIvw5lAAljIMx8LzsYOFevIgnBpyPwUJVMn_xDwnJWC-AU-6Jp0Eb-ZuSohxMKcBmxR9ak_5tRXuQ4kqYEna4UclJFOx-Obzp7du3IhhmablvgDJRfjxTrIvFQ2FsM6TrcIlqcuv76rzTFy9BdhfWlxOOjNH9H5uU9SNeBJoEVn1etdhJKArorV1jnWGLnKIFSag2k7mVfmJIOseePrbKjoegqncKAFNpoxM3013spqBr7PtV_zf82ftF6biI4R5BDFc7m-EFWIpO8ZhXokaiuk-HG5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=rK8JWYgmHB_Bs9ViQ26L9b5GNCli_-ulgpQ0PUbNwJQNVT_lPtq6DEDl6VIIvw5lAAljIMx8LzsYOFevIgnBpyPwUJVMn_xDwnJWC-AU-6Jp0Eb-ZuSohxMKcBmxR9ak_5tRXuQ4kqYEna4UclJFOx-Obzp7du3IhhmablvgDJRfjxTrIvFQ2FsM6TrcIlqcuv76rzTFy9BdhfWlxOOjNH9H5uU9SNeBJoEVn1etdhJKArorV1jnWGLnKIFSag2k7mVfmJIOseePrbKjoegqncKAFNpoxM3013spqBr7PtV_zf82ftF6biI4R5BDFc7m-EFWIpO8ZhXokaiuk-HG5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
‼️
روح الله قرهی رئیس حوزه علمیه:
«وقتی ماهواره به فضا می‌فرستیم، می‌توانیم سرش را کج کنیم و خود آمریکا را بزنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69437" target="_blank">📅 22:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69436">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4MEqkCzjjRRxUQUKTk4F5FCbtDXfSFKRCnFGl4cC-sDvN8UXMCxUCGjUPxkepV3cq65zN8CAD2glBg-1-BQfm3w_UH2EcmZ_etJ4r11LNVlzhOH2c43RxzEZRACq8QTIV4IdjYoWEbzYmy_FpHFIr98Y7qhEQ0Kz3CKv9kqcjDBICrj1ugCPZnZDMR4gAQf7mP1aXsD3YmQfJGWv4PylycqG3IxrF4F6VIooIH9UEDcBgBgXZT8KuupQJI0zyJQ1cbXu-FIub4Qt8_v5HBMKjDZwFr0mXmksvWOsNTlg_Co2Svjh86Xqr7KXbr64ZHpHQFOhlKC29ezIVgmNUHQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کان‌نیوز به نقل از یک منبع امنیتی:
رفتار دونالد ترامپ — که منجر به لغو حمله گسترده به ایران شد — به توانمندی عملیاتی آسیب می‌زند و آن را تضعیف می‌کند.
این مقام امنیتی گفت: «این دومین بار در طول یک هفته است که ایالات متحده اسرائیل را در جریان حمله‌ای برنامه‌ریزی‌شده قرار می‌دهد که می‌توانست خاورمیانه را تکان دهد، اما آن حمله در آخرین لحظه و بدون هیچ توضیحی لغو شد.»
یک منبع اسرائیلی نیز افزود: «با وجود رفتار رئیس‌جمهور ترامپ، آماده‌سازی و تدوین جدی برنامه‌های آتی دشوار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69436" target="_blank">📅 21:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69433">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Dd87kvz72qdAtWSt8xWvTqEzo89w9nH7ZQDBJDlP32Aqe0m_G3dNvVZj2STggXDP_oeh_IEFhd89uXhd-piXa_atmFWrgaR8VNWhNKyFXgAyHsCZJ2COa05BszJ7zT4puq3nNtm573s3y7WhpM8uvJ14ZCt34TJzQAI0gYk3P8Dfdj4spXfg8_be8kZVT4pvEvFV2Res_rU98DCUczlZK6qPMJPGYcO39RbjhT10jT3izJVWtNipaRTFieYdqHYqC1uhwxBt4Lx4z_OeCHLT4pjjje-dPOOqBk2bpD6oVecKfKFINdaxAighfzkaM7zKbgyq8vaCbM7Ej3tdfZb5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=XnEwoNsZ03YX0Z-sAg9F95uBj9FOLVnAPJm4gsKmypLsPulKdjs0NcWI-sTWvSHqHoUO0kVUBmADMofhjV3RmYB9ftRTly_LtwtCLRC3QSRFO-eh_0jDMbYO7kxkzORxBZze8Y6SrQl2Xgst2UMz_cuXWo-rkFX1cQAhvc7EJiP5MhsWhhLaU1xxO2RI66ssLZ93ERzWbrMSCE-aE9bu0uMMeBBpAu5x1T40frc8eH-CRIGhWeRXXWlVAOnepJvVoR15dJoj8ChpWy46bgqooHe7Q2YTeKK0AWVx_Hw-TmBQ4zyyOoi1FERNaHFOsEDAjmTVV2Z8hx4z6HeSPjXbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=XnEwoNsZ03YX0Z-sAg9F95uBj9FOLVnAPJm4gsKmypLsPulKdjs0NcWI-sTWvSHqHoUO0kVUBmADMofhjV3RmYB9ftRTly_LtwtCLRC3QSRFO-eh_0jDMbYO7kxkzORxBZze8Y6SrQl2Xgst2UMz_cuXWo-rkFX1cQAhvc7EJiP5MhsWhhLaU1xxO2RI66ssLZ93ERzWbrMSCE-aE9bu0uMMeBBpAu5x1T40frc8eH-CRIGhWeRXXWlVAOnepJvVoR15dJoj8ChpWy46bgqooHe7Q2YTeKK0AWVx_Hw-TmBQ4zyyOoi1FERNaHFOsEDAjmTVV2Z8hx4z6HeSPjXbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انبار شرکت Wildberries در منطقه سمارا دچار آتش‌سوزی شد، این اتفاق پس از حمله اوکراین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69433" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69432">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5208110eae.mp4?token=XbBcsf17yCuz1FT8w_LVkwbVvnseEdycyrDJv0fpQ8BrV_n46Znl5KCqsO9GRS7dNh5og60Fb89h2QzGTNIsdHa2jgkSbRQuvcxadW-DS-MZvyJw3Y89CNDPHc_pes6-TsDytw7qz63JIpybqXm9N49_qLeVK3lh-wYTjYZ9fbnBImK7SYi7bxB67JOGicrKW8sl3z86GGD4eLJbNwXqQ7ivODiokPa3bN8b9pI9U26qiLfkVXr7b2nRGgk3n3bPvD33xTn0rWOM_6qewFhhpyyZfzcaYBANnTe-L6DrdTFJb3f-4c2HI7EuK2lnxJ-l0mon7GilvHxi2BZxP0pdmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5208110eae.mp4?token=XbBcsf17yCuz1FT8w_LVkwbVvnseEdycyrDJv0fpQ8BrV_n46Znl5KCqsO9GRS7dNh5og60Fb89h2QzGTNIsdHa2jgkSbRQuvcxadW-DS-MZvyJw3Y89CNDPHc_pes6-TsDytw7qz63JIpybqXm9N49_qLeVK3lh-wYTjYZ9fbnBImK7SYi7bxB67JOGicrKW8sl3z86GGD4eLJbNwXqQ7ivODiokPa3bN8b9pI9U26qiLfkVXr7b2nRGgk3n3bPvD33xTn0rWOM_6qewFhhpyyZfzcaYBANnTe-L6DrdTFJb3f-4c2HI7EuK2lnxJ-l0mon7GilvHxi2BZxP0pdmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی امور خارجه، اسماعیل بقایی:
مدیریت آینده تنگه هرمز توسط ایران و با مشورت عمان انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69432" target="_blank">📅 20:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69431">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04acf28261.mp4?token=XEcZSALoPXZIAs2oWloLRMOIXAZ1JFxhGQdbUBPLN8sL6hqNEWYMeKS-YFNAzh_N2WKHGZEq58LGH-whfMsF17GhQNDvUgDEvUrDc0TxCUliY-ptJT20WqwtYRR4tyjbov3WSd5XeO6oNwCZPKJDbZFCIQWbjtq8CFhCQRRo0lUjaO_TzfBVWZZ0keSPut9nVKg3-FyqhbT_4P_yxBhszGfOKS7JgksE0jKe_TJoXVydb0R44u84DNo3MLYewCk2QHRP9MhrjIy2jh1oZkUKCg7W-_X9XatKEf-gn0lWKWDC5a4TuQmkcdFbUpW_DGPqhdOVs3yQCGtvghy1YdqGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04acf28261.mp4?token=XEcZSALoPXZIAs2oWloLRMOIXAZ1JFxhGQdbUBPLN8sL6hqNEWYMeKS-YFNAzh_N2WKHGZEq58LGH-whfMsF17GhQNDvUgDEvUrDc0TxCUliY-ptJT20WqwtYRR4tyjbov3WSd5XeO6oNwCZPKJDbZFCIQWbjtq8CFhCQRRo0lUjaO_TzfBVWZZ0keSPut9nVKg3-FyqhbT_4P_yxBhszGfOKS7JgksE0jKe_TJoXVydb0R44u84DNo3MLYewCk2QHRP9MhrjIy2jh1oZkUKCg7W-_X9XatKEf-gn0lWKWDC5a4TuQmkcdFbUpW_DGPqhdOVs3yQCGtvghy1YdqGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی وزارت خارجه اسماعیل بقایی:
توافق ایران و عمان بر سر مسیر جدید هیچ ارتباطی با بازگشایی تنگه هرمز یا حفظ بسته بودن آن ندارد.
مسیر جنوبی از طریق تنگه هرمز با ناامن کردن منطقه و آسیب رساندن به منافع ملی ایران همراه بوده است و تهران آن را نمی‌پذیرد.
مسیر مورد توافق نه مسیر شمالی و نه مسیر جنوبی فعلی خواهد بود. در عوض، مسیر جدیدی خواهد بود که هر دو طرف متقابلاً بر سر آن توافق دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69431" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69430">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=KOeMvZI2E5EWKnN4PlLEZnQlFm33F4zNVCuDhGfKb8KjiQt5n9xeRxal381oeCEoQ1V2zFDRHnw6WK2uxcl4OPSVzNolnf64QwLWtci7JYzd8WsBOkaPvuouAxAr1xbc5cVcMDlEdoLKK6C4iF37Gg_SbnMGu-NFZqbo0Xvq3JhuhmNKDaqmMXcv2HcpXryvoq9d0bjgE2MyWTDUJPv4vJ7ptitcZIVrR6ekByzvoNrVkWH39ACyYB7xLy-YNnfqZWdqpsuNwjMKxPnkw_CWbc9x6yR1ijPmV-MBcWWRe1_FzmFDnWbsf1gRvZqLwU6i6VSa_2ti1eicrWxK45Dj2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=KOeMvZI2E5EWKnN4PlLEZnQlFm33F4zNVCuDhGfKb8KjiQt5n9xeRxal381oeCEoQ1V2zFDRHnw6WK2uxcl4OPSVzNolnf64QwLWtci7JYzd8WsBOkaPvuouAxAr1xbc5cVcMDlEdoLKK6C4iF37Gg_SbnMGu-NFZqbo0Xvq3JhuhmNKDaqmMXcv2HcpXryvoq9d0bjgE2MyWTDUJPv4vJ7ptitcZIVrR6ekByzvoNrVkWH39ACyYB7xLy-YNnfqZWdqpsuNwjMKxPnkw_CWbc9x6yR1ijPmV-MBcWWRe1_FzmFDnWbsf1gRvZqLwU6i6VSa_2ti1eicrWxK45Dj2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کارشناس صداسیما:
مسعود رجوی (رئیس سابق مجاهدین خلق) فرد باسواد و کتاب‌خونده‌ای بود و قطعا خیلی باهوش‌تر از رضا پهلوی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69430" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69429">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=TSC0r0MbQruwXFQj5KKRoyXSJHhBrkyY7JaiMjJfNGYnnEWCkTsCe7eZ1ceobWIk293JwDZMzxg8wkGUv8dncP0_L9gzvJ5KOA9nbdPijd__Xmw3oYh5KMDt61oWyc-DGyUfu4qlRqks13pIE-vkmGO_QkADzmGIHym8HHmlm8QbEvBUSyjOreGlh_C0mf4f7aOrq7h932QjnEdg6n-BsC5EnHZtm-W9grVGQTkUnz6omctCQscz-PV34P-le3GiZ40wEORUWnJR0SqdaEzWo-A8sRl8GsF0bKU96zpXDuWbXdTK_eHfe8hYH3pC3FhyoApZJn1N7e8eM0LTRhfZQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=TSC0r0MbQruwXFQj5KKRoyXSJHhBrkyY7JaiMjJfNGYnnEWCkTsCe7eZ1ceobWIk293JwDZMzxg8wkGUv8dncP0_L9gzvJ5KOA9nbdPijd__Xmw3oYh5KMDt61oWyc-DGyUfu4qlRqks13pIE-vkmGO_QkADzmGIHym8HHmlm8QbEvBUSyjOreGlh_C0mf4f7aOrq7h932QjnEdg6n-BsC5EnHZtm-W9grVGQTkUnz6omctCQscz-PV34P-le3GiZ40wEORUWnJR0SqdaEzWo-A8sRl8GsF0bKU96zpXDuWbXdTK_eHfe8hYH3pC3FhyoApZJn1N7e8eM0LTRhfZQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
من یه مشکلی برام پیش اومد که گفتم نمی‌تونم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و غلامرضا رضاییان، رییس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69429" target="_blank">📅 19:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69426">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=TyfR0YIo30LIG7zScGYGKMHnsvvRo9DkOr5QO18o_uueq3UO4W6lwLPMCRmPoUi0bxfIlPNCvZZmy5D8lK8VR9aD4L6IwJRIa85JpVtJXBBI0FOiwK6AIIdkpQ2JPVaS4c4ukWVjM8r2Vl89EioMShtBbjODR4oU-_3F6jAQlVfAaBOH39Yz6a-6CAl-Ohzxb86Lxe4ezkXNsgHX3Ne8Rx2ozSsLdxpkJVCMnFFlXFNrMaG3_-8-0oPGoA7Lk4NhDDgXiHO26g9JtWE6lzDruyoVkHEo4aQucOuqR4I8l3Ws8-OWmB2-6Sou02CD7t1xK_mMkiZauaMlNCjWl2rS2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=TyfR0YIo30LIG7zScGYGKMHnsvvRo9DkOr5QO18o_uueq3UO4W6lwLPMCRmPoUi0bxfIlPNCvZZmy5D8lK8VR9aD4L6IwJRIa85JpVtJXBBI0FOiwK6AIIdkpQ2JPVaS4c4ukWVjM8r2Vl89EioMShtBbjODR4oU-_3F6jAQlVfAaBOH39Yz6a-6CAl-Ohzxb86Lxe4ezkXNsgHX3Ne8Rx2ozSsLdxpkJVCMnFFlXFNrMaG3_-8-0oPGoA7Lk4NhDDgXiHO26g9JtWE6lzDruyoVkHEo4aQucOuqR4I8l3Ws8-OWmB2-6Sou02CD7t1xK_mMkiZauaMlNCjWl2rS2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💋
🇮🇷
این جنده‌اینستاگرامی که خیلی ماجراش وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های
🔞
عجیب منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69426" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69425">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=pMMvXzjg5EXqNvK-ZDecz1nIgPTGXz2IhTMSP3wGlgpaHsIbWNR-jGOn7WosZKoLdpdyLC69zn3PwUtWD7A_PZ4OZkaItAY_7B7H5ithdnD07Ihj9k3Z18J98XNlU6CUhD2ZDx1tSy9VrQRZ1RNX2Z7vS2PneZHoJI-j77nfy5IdDEgBTfunuLusNUigAye-rXdm--YRRYEqyJUGnmNR78n16HvupcKoLOnWi23IPViJ33vcI09ojeo5sT2XlWGFRTjfkEQhHIJuYrEUW88NpXHR77yX9ccdh-GIjpZfpnLcFqFzjeGUOFBWr7H-YlErHNkiW0t1vBg8jHatuD3zYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=pMMvXzjg5EXqNvK-ZDecz1nIgPTGXz2IhTMSP3wGlgpaHsIbWNR-jGOn7WosZKoLdpdyLC69zn3PwUtWD7A_PZ4OZkaItAY_7B7H5ithdnD07Ihj9k3Z18J98XNlU6CUhD2ZDx1tSy9VrQRZ1RNX2Z7vS2PneZHoJI-j77nfy5IdDEgBTfunuLusNUigAye-rXdm--YRRYEqyJUGnmNR78n16HvupcKoLOnWi23IPViJ33vcI09ojeo5sT2XlWGFRTjfkEQhHIJuYrEUW88NpXHR77yX9ccdh-GIjpZfpnLcFqFzjeGUOFBWr7H-YlErHNkiW0t1vBg8jHatuD3zYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند پناهیان به پزشکیان و قالیباف:
همه پیامبران را مسخره کردند؛ از تمسخر نترسید و با عظمت صحبت کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69425" target="_blank">📅 18:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69424">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇮🇷
بیانیه سپاه پاسداران :
انتقام خون رهبر شهید و اسماعیل هنیه اجتناب ناپذیره
پاسخ این جنایت بشدت سخت و قاطع و سخت گیرانه خواهد بود
توطئه خلع سلاح حماس به نتیجه نخواهد رسید و از همین الان شکست خورده بدانید
دنیا بداند اراده ضد صهیونیستی ادامه دار خواهد بود و پیروزی نهایی فلسطین خیلی نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69424" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69423">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=M0SrIJ2yJf5SAy99gPy0qfJ_vcEuel9LQ0YL4wlMpVNZTwdS8uCS-LNomjozvE-JEyH4Tribhnglt58eskpKIL-sY3JBZLoyME9i971RqdxItsI8akF4oMkSulyN05Bdg8QKCGdWxrf74z7XRVPFAcyR2qiCvA7mELMoRwGsYI2pPT6FXARdWZut3HLfx1XStE-p8tYmHFnSJePcWyIihrUmFHfatIVCIEVhM3YmeQQ48h--eNb0JVW34xu4gDeakuvWAls4zakfRsvqA2KPdnZ3VWYi4tSntA5XzDgmY_2nlpIRsOLeRlWJolRuB1yiC9nIp6QrogNESMkrQ_igxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=M0SrIJ2yJf5SAy99gPy0qfJ_vcEuel9LQ0YL4wlMpVNZTwdS8uCS-LNomjozvE-JEyH4Tribhnglt58eskpKIL-sY3JBZLoyME9i971RqdxItsI8akF4oMkSulyN05Bdg8QKCGdWxrf74z7XRVPFAcyR2qiCvA7mELMoRwGsYI2pPT6FXARdWZut3HLfx1XStE-p8tYmHFnSJePcWyIihrUmFHfatIVCIEVhM3YmeQQ48h--eNb0JVW34xu4gDeakuvWAls4zakfRsvqA2KPdnZ3VWYi4tSntA5XzDgmY_2nlpIRsOLeRlWJolRuB1yiC9nIp6QrogNESMkrQ_igxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو هلیکوپتر آتش‌نشانی در حین مبارزه با آتش‌سوزی جنگلی در نزدیکی پساتا، یونان، در هوا با هم برخورد کرده و سقوط کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69423" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69422">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=lq8g9JmLPkMkC5dALz2WhK-g6boGXBfx2Ft9XuLXIDIqElxw8MZPcgU1QIw42GulsDCeC14VQfsYGeUJG0h9zCYJ4JaaVGIhmBbJ9zUDGdoQN2gpyTaBbY-HpUd-8vp7mCqcYI3hPBV2wyD0lMXzePTZz1EI9iuySS5hzVoQZzRge_CG2l8a5gW-L0HeaFME1sol4ZnviNjuqsONsIFxx-ggfRsmTCKIXZ-omb_T9tXVicuToVdW4X0_bBy7odvuw3shjmylareX-UOk-JfTfQHfZ_MIkK2mA4PInXXVMHbsgDiTgVsXE-l5EiF5Fbg5W7D26IpZULBaxDnJHnk3LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=lq8g9JmLPkMkC5dALz2WhK-g6boGXBfx2Ft9XuLXIDIqElxw8MZPcgU1QIw42GulsDCeC14VQfsYGeUJG0h9zCYJ4JaaVGIhmBbJ9zUDGdoQN2gpyTaBbY-HpUd-8vp7mCqcYI3hPBV2wyD0lMXzePTZz1EI9iuySS5hzVoQZzRge_CG2l8a5gW-L0HeaFME1sol4ZnviNjuqsONsIFxx-ggfRsmTCKIXZ-omb_T9tXVicuToVdW4X0_bBy7odvuw3shjmylareX-UOk-JfTfQHfZ_MIkK2mA4PInXXVMHbsgDiTgVsXE-l5EiF5Fbg5W7D26IpZULBaxDnJHnk3LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی اینو ببینید توی پخش‌زنده صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69422" target="_blank">📅 17:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69421">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McAnzWXW9YMZcmBcKQtDwGdgFGa2msydxyIQxD5L_T5-Ri8ebnWy-nabPnjqCL01Il7wH6pxs5whI9f6vCNPUrG-c5_bPPIAHn1w6Ltzp8d58LrElFNL7vVtl3ePGEAhv3vPSze1XP0XJFc5IcJ2lZocvIHgXTkjh6yjbeVI07yInp_iABvY0gbs5-nnKHLs5jWwHbCwhPaO5MxYaZhrPkqrffbGGGTQJkbBogfBhNAlqFRBXmqozCzjSLelMArapQ77isbL96NpZsfWHuhYZOR4ILcj8eG_LbdM7zyoxv2NLVDFXZHw9iNibIdUsehVX6xqzYG8bk9vKInAVG5RVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
نیویورک پست:به گفته منابع آگاه، در حالی که رهبران اعتراضات در تلاش برای دستیابی به سلاح هستند، انقلاب ایران ممکن است «هر لحظه» رخ دهد.
چهره‌های مخالف حکومت در تهران به نشریه «پست» گفتند که خیابان‌های ایران به دلیل اعدام‌های در ملأعام، فروپاشی اقتصادی و جنگی که بیش از پنج ماه است ادامه دارد، به مرز انفجار رسیده‌اند.
یکی از رهبران اعتراضات با اشاره به سرکوب بی‌رحمانه ماه ژانویه توسط رژیم — که به گفته رئیس‌جمهور ترامپ منجر به کشته شدن ۵۲ هزار نفر شد — گفت: «انقلاب ممکن است هر لحظه رخ دهد؛ مردم خواهان انتقام هستند.»
یک روزنامه‌نگار مستقلِ فعال در جریان‌های زیرزمینی ایران گفت که تدارکات برای خیزش بعدی هم‌اکنون در حال انجام است و فعالانی از تمامی اقشار جامعه مصمم‌اند تا ضربه‌ای نهایی و تعیین‌کننده به رژیم وارد کنند.
این روزنامه‌نگار گفت: «ما در حال بررسی اعتراضات ماه ژانویه و تشخیص این نکته هستیم که چه تاکتیک‌هایی مؤثر بوده‌اند و کدام‌یک نه؛ همچنین نقشه‌ها را تحلیل می‌کنیم تا امن‌ترین و خطرناک‌ترین مناطق برای تجمع را شناسایی کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69421" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69420">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ptkphn8-Et9KcIJ8LiaJV5ea31O7KfEuomSC2REylrdLeRIuXHquO6-jQl2RSElA04rs0407NFlGceb2yhHQ60eg1BObUnel-3Bo2-MNHECGKVjUIZD55iSYXksxPVeurfl7POptFBGk6spjwSkfKyVD1CcIEV-c-JAOuab-FCSebSFBLw7hIl9fy625jzn9qJafpHPFa11S_j_9WUqP9_FxtzQR8UvWNg4X1HQ4WOR8mQji6xzZmCNcV8XjrXv2EAcemE6LmRs2QneA48sKQ_b_2Ss7Eiv348nre2m2ZWOQVdS1gP4m07Z2YkU8V21k5rTCUhf_H_yVobY7gaNPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
صفحه فارسی وزارت خارجه اسرائیل:
هفته خوبی از اسرائیل برای شما آرزومندیم!
💦
اسرائیل داغ‌تر از همیشه به نظر می‌رسد... و ما فقط در مورد آب و هوا صحبت نمی‌کنیم
😉
🇮🇱
☀️
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69420" target="_blank">📅 16:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69419">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=dMQ6gO_6hc2kP5mzh3F4tvEm21XYOjL5yaWNcjKv7_md7Rx0momaFQw_muFlYGz3HwIrU-RtzGQH32D1vz9WzTnYaHf_1nKc1qri8soF8wj8rMJVuXLrGJE4bCcrz1eFcjkoCjbOGwtpPfh0ZcVkayU2lt9pdN3_zZPWqBeMbc5p0VVyqi_gMxFyG2h3Lb1s6Kt4x8DOtsObjkzo9G_0liJY7WBFmNue4P_SdEtEkdBtCHVwd0H6S3l3_317urXklSFwbWp5_Gc47g91tlgLQj1aVFK1HZuJouWyYec4Q65ltaURV67bzKTs9WgDoliujKDyC7m_XitINhMydgbjtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=dMQ6gO_6hc2kP5mzh3F4tvEm21XYOjL5yaWNcjKv7_md7Rx0momaFQw_muFlYGz3HwIrU-RtzGQH32D1vz9WzTnYaHf_1nKc1qri8soF8wj8rMJVuXLrGJE4bCcrz1eFcjkoCjbOGwtpPfh0ZcVkayU2lt9pdN3_zZPWqBeMbc5p0VVyqi_gMxFyG2h3Lb1s6Kt4x8DOtsObjkzo9G_0liJY7WBFmNue4P_SdEtEkdBtCHVwd0H6S3l3_317urXklSFwbWp5_Gc47g91tlgLQj1aVFK1HZuJouWyYec4Q65ltaURV67bzKTs9WgDoliujKDyC7m_XitINhMydgbjtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از نیروهای سرکوبگر: تا تهش پای حکومت وایسادیم، بازم بیاین بیرون بهتون رحم نمی کنیم!
چون داریم دستور خدا رو انجام میدیم، شما اصلا کسی نیستین جلوی جمهوری اسلامی وایسین.
کل دنیا هم جمع بشن نمیتونن کاری کنن، پاینده جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69419" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69418">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f215b551.mp4?token=toi1jcQXLmx3JRwX5YuN_9G76RGLBeSWQvu_SNwQbRveYgV9ubc7k8Gk61vs5QMdYec1OseZH4iZ-IAfkEmraasAn4x6XN53Df9TcYC1at6I2avZTIsMeCM0yMidJu0vXgTLXy994gpUdMr3FdwXZOwQY_FPWwx9_trvkWpSF_UXSNh--n1EcN16drQMbronvJo155jWkiC-M-HyjaB2NxxxBN1P3tpIj1L63TqpQiNMqMeZHCkVQdwicv_J0SCAK5BNKywIpHk-h9WI7KtFxa68plEWCIC2ST7IqRxbErlKE8pWqnLw92642a5003-9UcCezCHFfTZGep0NyNTJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f215b551.mp4?token=toi1jcQXLmx3JRwX5YuN_9G76RGLBeSWQvu_SNwQbRveYgV9ubc7k8Gk61vs5QMdYec1OseZH4iZ-IAfkEmraasAn4x6XN53Df9TcYC1at6I2avZTIsMeCM0yMidJu0vXgTLXy994gpUdMr3FdwXZOwQY_FPWwx9_trvkWpSF_UXSNh--n1EcN16drQMbronvJo155jWkiC-M-HyjaB2NxxxBN1P3tpIj1L63TqpQiNMqMeZHCkVQdwicv_J0SCAK5BNKywIpHk-h9WI7KtFxa68plEWCIC2ST7IqRxbErlKE8pWqnLw92642a5003-9UcCezCHFfTZGep0NyNTJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو با اختلاف زیاد عجیب‌ترین و دارک ترین چیزیه که تا آخر هفته می‌تونید ببینید؛
هربار یکی از این خانواده رو دنبال کنید تا متوجه عمقِ نفهمیدن بشید...
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69418" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69417">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d8743494.mp4?token=IeXBzw4sas3cbIize4-ZW8Xn4tK-hqkN2GCm9DvnCRtbClJhqtNiQg4kkCEjONamEvc8K4_vmyk5y4NeuK3s1wgiBuiiU83rCrhqQsp43k7MpvSFMovFEHvgFOcz8-3h5TGFQaP7FGMukrFS7-WI1KGWmx9Va0gO9C1OIVHbeH2IVtwyF9CvwUcMaa5t6_tQIi5pK2Sf_DzuuMlfEcv2s_QM4AxoS-3qep_zqfq1Oj5tYxRN5EJxPLVirfvE2j0CsYNHu51hzL1DXwmg1L1aE9hRD6OB1ExrdUOdqMk2-c-BhpQ8hK83dYGhDMi9We5OPeSZENGaMMOjSlr5Sgew6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d8743494.mp4?token=IeXBzw4sas3cbIize4-ZW8Xn4tK-hqkN2GCm9DvnCRtbClJhqtNiQg4kkCEjONamEvc8K4_vmyk5y4NeuK3s1wgiBuiiU83rCrhqQsp43k7MpvSFMovFEHvgFOcz8-3h5TGFQaP7FGMukrFS7-WI1KGWmx9Va0gO9C1OIVHbeH2IVtwyF9CvwUcMaa5t6_tQIi5pK2Sf_DzuuMlfEcv2s_QM4AxoS-3qep_zqfq1Oj5tYxRN5EJxPLVirfvE2j0CsYNHu51hzL1DXwmg1L1aE9hRD6OB1ExrdUOdqMk2-c-BhpQ8hK83dYGhDMi9We5OPeSZENGaMMOjSlr5Sgew6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بر اساس تصاویر ماهواره‌ای، پایگاه هوایی شیخ عیسی در بحرین که مورد استفاده نیروهای آمریکایی است، اخیراً تخلیه شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69417" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69416">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=VAMxtv8wEYXvcy9oJ_tnDY658fkRF15sLqv8uL4FYDaZOg2ekAjm6EnT7CAWMfSMI8ylOX24WJAFJtEh_pSH4bfkOe-0QNpE79UMglO2PBvlE4ANawjRe7QmV7N94S_KxA3BrV1VJYNSbJ_Kj0ftMdmp4CVLC67gM06_2shS4e5u-h18Zgmxx7XpUkPmQ1G0YAquam5CHuTz0nCo4QCwZme-TCiftpyOnLkQyIXl0DiipicLqef3nRh2sghi51lKqW2kOzRLXZ7CyBgeKrXDlE22X9anxQLXQR9RdM_Y0Y1i3_PUpiJdIOqPb_nh9lnFGGa0ZkSv88-iIOyA5sLgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=VAMxtv8wEYXvcy9oJ_tnDY658fkRF15sLqv8uL4FYDaZOg2ekAjm6EnT7CAWMfSMI8ylOX24WJAFJtEh_pSH4bfkOe-0QNpE79UMglO2PBvlE4ANawjRe7QmV7N94S_KxA3BrV1VJYNSbJ_Kj0ftMdmp4CVLC67gM06_2shS4e5u-h18Zgmxx7XpUkPmQ1G0YAquam5CHuTz0nCo4QCwZme-TCiftpyOnLkQyIXl0DiipicLqef3nRh2sghi51lKqW2kOzRLXZ7CyBgeKrXDlE22X9anxQLXQR9RdM_Y0Y1i3_PUpiJdIOqPb_nh9lnFGGa0ZkSv88-iIOyA5sLgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر مارو خندوندی حاج اقا دارم پاره میشم
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69416" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69415">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇮🇱
بنسالل اسموتریچ، وزیر دارایی اسرائیل:
رژیم ایران در جریان جنگ سقوط نخواهد کرد.
مردم ایران در شرایطی که هواپیماهای اسرائیلی و آمریکایی بر فراز آسمانشان در پرواز بودند، به خیابان‌ها نمی‌آمدند؛ چرا که نمی‌خواستند در نظر دیگران، همدست دشمن به نظر برسند.
تأکید اصلی باید بر این موارد باشد: اقتصاد، اقتصاد، اقتصاد و باز هم اقتصاد. این همان عاملی است که در نهایت موجب سقوط رژیم خواهد شد.
به گمان من، رژیم ممکن است به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی چنین وضعیتی پیش بیاید، ترس دیگر مانعی نخواهد بود؛ آنگاه مردم به خیابان‌ها می‌آیند، قیام می‌کنند و رژیم را سرنگون می‌سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69415" target="_blank">📅 13:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69414">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
خبرگزاری فارس، وابسته به سپاه:
گزارش‌های حاکی از موافقت ایران با بازگشایی تنگه هرمز نادرست است و هیچ تغییری در سیاست تهران ایجاد نشده.
منابع نظامی گفته‌اند این آبراه راهبردی همچنان بسته است و عبور از آن نیازمند مجوز صریح و هماهنگی با نیروی دریایی سپاه پاسداران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69414" target="_blank">📅 12:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69413">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835653bd72.mp4?token=JrjWFGmaqmlf3NvbAAomY6_zK46m4TklNO5hWZAsAJIGBAcWR65JAAVDi-xaHRfMPYcFusXtqDGM9hpzxAIFVMBhHwlh7RiQfYu-z6DF-MySPPSue1p9WauzseQ7ixHyilg-EKIZXk_zLoBvTyXEsavvFjJGSvU--d9eHrNlGYWmlJIRdKSU8kfN9bB_SV9LRszH_Y45UOjoCP2qAACaGgxbokQnGH28q6OsHQO819kTE2YjFbEKyYILUGPAho5Cq1mu1AuxsCLijbK2oUI7Wv_07p2XzGKVejOx-4upeBiPD0J6r9eW0284Z4Nn6U__pfOUF5gwfdeGbkXymJwEBUXWFcQMmojfKfzQ3c2jdG_kk2Nd5SMrAfTbtJdxAFSUvCz_2F1wbTnItZOx8hUIiMjbJNgoRh3sJxeo215TiWyVOWIruDtCZVEdZ8JMyOAsQNdZ0kfBjuIDSt3MDPtefMI1mpLNeYcEpVbeUx8QhcIHTGQJi8IH0c_5nbMZacMFxmc1yfbi7m8VeU_T0VTKdxEPJcKMQ4bdwjNJvkbKN6kdvGqScCjQbXnbZTC42LsnQux3MojsLBhQYhW6dqr3ANuiJwCYTk78I6Z_wM4VN0hoborH3MI_GQZ6WouF1h8SIcOb4hMsOr4Z32e992O_VH3H8-KCApl5ZPbCSHnDWR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835653bd72.mp4?token=JrjWFGmaqmlf3NvbAAomY6_zK46m4TklNO5hWZAsAJIGBAcWR65JAAVDi-xaHRfMPYcFusXtqDGM9hpzxAIFVMBhHwlh7RiQfYu-z6DF-MySPPSue1p9WauzseQ7ixHyilg-EKIZXk_zLoBvTyXEsavvFjJGSvU--d9eHrNlGYWmlJIRdKSU8kfN9bB_SV9LRszH_Y45UOjoCP2qAACaGgxbokQnGH28q6OsHQO819kTE2YjFbEKyYILUGPAho5Cq1mu1AuxsCLijbK2oUI7Wv_07p2XzGKVejOx-4upeBiPD0J6r9eW0284Z4Nn6U__pfOUF5gwfdeGbkXymJwEBUXWFcQMmojfKfzQ3c2jdG_kk2Nd5SMrAfTbtJdxAFSUvCz_2F1wbTnItZOx8hUIiMjbJNgoRh3sJxeo215TiWyVOWIruDtCZVEdZ8JMyOAsQNdZ0kfBjuIDSt3MDPtefMI1mpLNeYcEpVbeUx8QhcIHTGQJi8IH0c_5nbMZacMFxmc1yfbi7m8VeU_T0VTKdxEPJcKMQ4bdwjNJvkbKN6kdvGqScCjQbXnbZTC42LsnQux3MojsLBhQYhW6dqr3ANuiJwCYTk78I6Z_wM4VN0hoborH3MI_GQZ6WouF1h8SIcOb4hMsOr4Z32e992O_VH3H8-KCApl5ZPbCSHnDWR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گزارش روزنامه همشهری از دلایل عدم انتشار صدای مجتبی خامنه‌ای :
از طریق صدا میتونن پیدا بکنن چون هر فضای بسته امضای صوتی منحصر به فردی داره و از بازتاب صدا از طریق فرش و دیوار میتونن مکان رو تشخیص بدن و ارتفاع اتاق و فاصله گوینده رو از محل بازتاب رو پیدا بکنن
همچنین از طریق تحلیل شبکه برق میتونن ردیابی بکنن چون همهمه ضعیف الکترومغناطیسی در پس زمینه صدا ضبط میشه و سرویس های اطلاعاتی میتونن از طریق شبکه های اتصال برقی مکان رو ردیابی بکنن
هر میکروفون و دستگاه ضبط اثر متفاوت داره و مختص خود دستگاهه مثل اثر انگشت خود شخص لذا از طریق ردیابی دستگاه میتونن مکان رو پیدا بکنن
صدای پس زمینه مثل خنک کننده ها یا ژنراتور ها و حتی توی مکان باز صدای ترافیک ها و صدای محیط و نوع حشرات و پرندگان میتونن محل جغرافیایی رو لو بدن
😳
😳
ویس ابعاد فیزیکی نای دهان و مجرای صوتی رو نشون میده و حتی فیلتر هم باشه با دستگاه هایی میشه ردیابی کرد و تشخیص داد طرف زنده باشه محل حضورش کجاست
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69413" target="_blank">📅 12:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69412">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇺🇸
ویدیو ای که صفحه رسمی وزارت جنگ آمریکا به تازگی منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69412" target="_blank">📅 11:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69411">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=kARPnbgayBSQKKW2fXsnZ6PFJzJX2oH1HGB0CoVImr31wZR1E-B_TX20R39vNZAcjcd3qN_sMLaktL29c5IcToFVYQU5H1gnw7CLYUJl8EiQfgr1Cm6s_XQIldI2ByJ14-gTqK3zzy71_0-qj7kqN9_vHpN-iAlprZBzNHI6zIMbSAFjPytzQ-xUU3FdOM0KqVCoCcYDV6C-VsXU3T9KCxPB0tg-ErQPnlVICLbro8_QKBCtgpekMCHrVWAxl2icIAlOU41IrvFMGc77DR3_lnexLJL9ypenyl065JWAr8LHpQu6P7JzjfdgHn_XgGI9LszZVZh_Z-w0pVqQBUYLNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=kARPnbgayBSQKKW2fXsnZ6PFJzJX2oH1HGB0CoVImr31wZR1E-B_TX20R39vNZAcjcd3qN_sMLaktL29c5IcToFVYQU5H1gnw7CLYUJl8EiQfgr1Cm6s_XQIldI2ByJ14-gTqK3zzy71_0-qj7kqN9_vHpN-iAlprZBzNHI6zIMbSAFjPytzQ-xUU3FdOM0KqVCoCcYDV6C-VsXU3T9KCxPB0tg-ErQPnlVICLbro8_QKBCtgpekMCHrVWAxl2icIAlOU41IrvFMGc77DR3_lnexLJL9ypenyl065JWAr8LHpQu6P7JzjfdgHn_XgGI9LszZVZh_Z-w0pVqQBUYLNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها:
این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69411" target="_blank">📅 11:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69410">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل:
عراقچی، وزیر امور خارجه ایران، شبانه با یک مصالحه میان قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد؛ اقدامی که باعث شد دونالد ترامپ، رئیس‌جمهور آمریکا، حملات تلافی‌جویانه برنامه‌ریزی‌شده را لغو کند.
بر اساس این طرح، کشتی‌های عازم خلیج فارس از طریق آب‌های سرزمینی ایران وارد و از مسیر آب‌های عمان خارج خواهند شد؛ هرچند عمان خواستار تأیید رسمی این موضوع شده است که سپاه پاسداران از این توافق حمایت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69410" target="_blank">📅 11:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69409">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66dc919056.mp4?token=Lr03046b0YVwTqkzZ_1kGq02aWlRqwRu9vL56QFkvM7peQH6FarGrf7XP4CwiQ8brYNxjZkzhxYPA-r2Tqt6Izl5kvB_mx-45s3-O2LT4eXI77fwL75zLylgB7XAd3K2buIAa6bquGwW8XPRr1eAnWWQ5jNDuw3406xldSluBaI32YLsYXHX2AHIdqIHuci9Eab4-X9pM2h1rGNcWjsm6R-xXdjqeNy8J6y1WpyO21IDttIP888kplOqtLQC-kLUcsYeQYF_uWTfnrvmW8VbQUxPrfFkY08KYA5EwTkZo4SVoWLVKp3vHyJ80l8J_KPIKJiSmUdJuPTOmOdFaacVLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66dc919056.mp4?token=Lr03046b0YVwTqkzZ_1kGq02aWlRqwRu9vL56QFkvM7peQH6FarGrf7XP4CwiQ8brYNxjZkzhxYPA-r2Tqt6Izl5kvB_mx-45s3-O2LT4eXI77fwL75zLylgB7XAd3K2buIAa6bquGwW8XPRr1eAnWWQ5jNDuw3406xldSluBaI32YLsYXHX2AHIdqIHuci9Eab4-X9pM2h1rGNcWjsm6R-xXdjqeNy8J6y1WpyO21IDttIP888kplOqtLQC-kLUcsYeQYF_uWTfnrvmW8VbQUxPrfFkY08KYA5EwTkZo4SVoWLVKp3vHyJ80l8J_KPIKJiSmUdJuPTOmOdFaacVLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
با این حال، تغییر رژیم هرگز هدف اصلی نبوده است؛ هدف، خلع سلاح هسته‌ای بوده است. آیا می‌توان یکی را بدون دیگری داشت؟
🇺🇸
مارکو روبیو:
هرکاری که توی خاورمیانه و جهان انجام دادیم کسی مانع ما نشده و موفقیت بدست آوردیم
رژیم باید تغییر بکنه شما شاید تغییر رژیم نداشته باشید ولی باید اینا تغییر بکنه
اونا میخان
انقلابشون رو به کل دنیا صادر بکنن و باید این تغییر پیدا بکنه
ایران تابحال با رئیس جمهوری مثل ترامپ که مرد عمل هست رو به رو نشده
اونا هنوزم موشک و پهپاد دارن میتونن صدمه بزنن ولی خب سپری ندارن پشتش قایم بشن
از روی قدرت باهاشون مذاکره میکنیم نه ضعف
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69409" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69408">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=ImsXXyPllHqOKFcIvHNZgT818jYmDptWwOC0p6Km7ZmgL3ju5wmelePhyyQVqhJUVa9BkTjh0GGSw_DjvbJSpBNa-upGHwwo1dDWkYcHJHVUuQX64r1tpVTpWYNF8ImvyD53q3S65ngdduYH19fmVH-A0liKjyBSKIXO38hfuZXd4GRxy6s-OnGekfwOB5FnwCYZyz_oUDXHAj8Zo5j7pKrF94P4hZL5Q9NgMWNgZ6DpClit0gdORsCEFAc4X_Uhkj95kTSFrnlk4oaMCiFtY1T7EpdlnVBylX68gH4Cv15iRXEPz-0VVbsY69qi_QL3egL5NsGRygbCGAYw3taJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=ImsXXyPllHqOKFcIvHNZgT818jYmDptWwOC0p6Km7ZmgL3ju5wmelePhyyQVqhJUVa9BkTjh0GGSw_DjvbJSpBNa-upGHwwo1dDWkYcHJHVUuQX64r1tpVTpWYNF8ImvyD53q3S65ngdduYH19fmVH-A0liKjyBSKIXO38hfuZXd4GRxy6s-OnGekfwOB5FnwCYZyz_oUDXHAj8Zo5j7pKrF94P4hZL5Q9NgMWNgZ6DpClit0gdORsCEFAc4X_Uhkj95kTSFrnlk4oaMCiFtY1T7EpdlnVBylX68gH4Cv15iRXEPz-0VVbsY69qi_QL3egL5NsGRygbCGAYw3taJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مرادویسی، تحلیلگر ارشد اینترنشنال:هدف‌های احتمالی آمریکا تو جنگ جدید میتونه شامل این موارد بشه:
1. مراکز نظامی سپاه تو جنوب کشور
2. شهرهای موشکی و پهپادی تو عمق خاک ایران
3. تاسیسات هسته‌ای "کوه کلنگ"
4. مراکز نظامی سراسر کشور
5. سامانه‌های پدافندی و راداری
6. پایگاه‌های هوایی ارتش
7. مراکز و نهادهای حکومتی
8. ساختارهای سرکوب (سپاه، بسیج و نیروی انتظامی)
9. مقامات و فرماندهان ارشد باقی‌مونده
10. مکان‌های نمادین مثل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/69408" target="_blank">📅 09:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69407">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=TPLGp0-vMPoLr8V90ldnSiDhaTzwolnJiJen_21MypyWafgqmobOtFek1cK4s6djQPwjulC9eHw5dPvUOnWDShdom1n237fgvODgZVrrc8RjxuqDCFZMUHNLmjJ0DcFl5LuhW2WCKeDp8NCKj5zlajLAo5n8OMxRXa_vDOz-4K4-B7syVifhi21cMfSU4bzVxXYzG89Ef8jQ-BlQ4ITQvMEy1EUIIggfhbDH4H3HjVumb_gmAWOOFIqizbau3w4aHKXqfv061JYELpUkN_Gm49uZnqaYbYldgeKCewC4Q9SUp61amKLbJvXI-XwNyuGxwNHdF7UNviutcCwmtvKWIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=TPLGp0-vMPoLr8V90ldnSiDhaTzwolnJiJen_21MypyWafgqmobOtFek1cK4s6djQPwjulC9eHw5dPvUOnWDShdom1n237fgvODgZVrrc8RjxuqDCFZMUHNLmjJ0DcFl5LuhW2WCKeDp8NCKj5zlajLAo5n8OMxRXa_vDOz-4K4-B7syVifhi21cMfSU4bzVxXYzG89Ef8jQ-BlQ4ITQvMEy1EUIIggfhbDH4H3HjVumb_gmAWOOFIqizbau3w4aHKXqfv061JYELpUkN_Gm49uZnqaYbYldgeKCewC4Q9SUp61amKLbJvXI-XwNyuGxwNHdF7UNviutcCwmtvKWIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
حاکم بحرین:
حضرت محمد (ص) پس از قرن ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگه به بحرین حمله نکنید.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/69407" target="_blank">📅 09:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69406">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIJ5iBXs6Oef8rWNIUdknkTS7lasPt6ftVn6MPSmJRqc3MbnUyRi6Ud1fJ0YZ5zUusTUP-epfIxRN4J_9e8ftPMXlHtarZbCvWI5ch587Zyt2HWfeLTuIxXG55Z4KbUy9BWNGYBBNDpGbKfqLzipWSNnCvFJp8z5s4thD_8kyskgnOQW9ZyOXsHjEKHUkvyeLedhUPZj2-KzUp9KH1sxY31txlpUTH9fy8e22IdEr6rEQ-_aYVppwJCCB3vtCgnWGrMsp_KkHpfpTsdeCcEgWAtR0-fRZftA5sL8PoqJ33IHAqhMKDnQx_U-NDXeHeE178ZYjEfAfWURSaLkhGhUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حمله رو کنسل کردم
!
ایالات متحده آمریکا آماده و مجهز به سلاح است تا علیه جمهوری اسلامی ایران، در سطوحی از ترور نظامی، قدرت و صلابت که از زمان جنگ جهانی دوم دیده نشده است، اقدام کند. با وجود این، ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب توافق‌نامه‌ای که مورد توافق قرار گرفته است، متوقف کنیم. این شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران می‌شود. بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافق‌نامه‌ای دست یابم. کشور اسرائیل در این تعهد به من می‌پیوندد. همه دست به کار شوید و آن را انجام دهید. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/news_hut/69406" target="_blank">📅 06:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69405">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaqDH-6s7HqsjR-Up7avZgE1EW8iC6xZjA8_EtyBQ3kKtsz9WqMbTdNLDIg1YIklZOzyAu9cBOeVIUSjEFUrltR_KLKDDUU63XiDTJGr4qP8H2U0Xub3_UfEqAZf7EJ2QBAWhKodrbOPkUUs9SdFayEg9m3CMSCTTujzR39i0kP0usSes_GiJ6OT8Qff6xi-Yhi8cRA3gtenlNUOLl9LHVBQMDFbFM-Ixwk3uMfQ07oafz2cOpgWRCXb39AEG_p9MG2Q-1BNqNmJcG6dIYgw3Hnrng-wT0SHyCwmcSqyiqYysgE72vuSBWeKZtpdID-kPIfv9_AxmjUljs-JflBuNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیکه و ترامپ چیزی نگفته.
#hjAly‌</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/69405" target="_blank">📅 02:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69404">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=lxlRznhvvDfBMZSHLGeynPrIu8tkdpN4cD5XtsoK92mlDSdclf2IzpXvaTnPZr3o2Cw6111bOdZROJc6FS9e4RalTLD-_K8hx1wEGFqkbZZDgvk973TN9lJPj6KLxzjtN48WgehJOJu54rRtzvT_PraVXge4vHZvYiT9NEbJb6aWwp7USz3WyNziJpOCzzNtCwWi0LoBGuGr6GadUl62984rA5486ecNk5h9r9LAr8SS8qUPwlVPJ4vBg9ofzXhqikvoSzKGOyeG2yOY9m97szPoLzjdwKzotrO42cz97FJQqAestz-co8xHT9saHZ4AOWxe7OrLMvjkES-87uE2cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=lxlRznhvvDfBMZSHLGeynPrIu8tkdpN4cD5XtsoK92mlDSdclf2IzpXvaTnPZr3o2Cw6111bOdZROJc6FS9e4RalTLD-_K8hx1wEGFqkbZZDgvk973TN9lJPj6KLxzjtN48WgehJOJu54rRtzvT_PraVXge4vHZvYiT9NEbJb6aWwp7USz3WyNziJpOCzzNtCwWi0LoBGuGr6GadUl62984rA5486ecNk5h9r9LAr8SS8qUPwlVPJ4vBg9ofzXhqikvoSzKGOyeG2yOY9m97szPoLzjdwKzotrO42cz97FJQqAestz-co8xHT9saHZ4AOWxe7OrLMvjkES-87uE2cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان سلیمانیه
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/69404" target="_blank">📅 02:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69403">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=KPatiCw5Ao0ZSFv57yQT_ZJIA04WMUoyL364BbBvYUa19c_MVv2YyKxHD82B1N109mywXckVVjTDI-kAJnSkid_2s1QQ6F_YzIFa4YYvK0FmZ5STn_q2vnaLAKgPyK30qtLsMOjD_ugwF7d88QCLCxnnSjfO8DjTD8YTib4k1lNsrlLBgqRJnR4psbueWRDCRQ5-PUiuca_70R_EG60dGrojH59sM8i9S2s9weyALo1bkjVxhsx51GclD_rFmL10gejrWu8-qI9tM1fevXog5zThaJoIgvMq14Tjaqu9FmH7NgYrdKL8uXaN0MbpSyw6odZ9sarkSSIhe9ym2bR1AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=KPatiCw5Ao0ZSFv57yQT_ZJIA04WMUoyL364BbBvYUa19c_MVv2YyKxHD82B1N109mywXckVVjTDI-kAJnSkid_2s1QQ6F_YzIFa4YYvK0FmZ5STn_q2vnaLAKgPyK30qtLsMOjD_ugwF7d88QCLCxnnSjfO8DjTD8YTib4k1lNsrlLBgqRJnR4psbueWRDCRQ5-PUiuca_70R_EG60dGrojH59sM8i9S2s9weyALo1bkjVxhsx51GclD_rFmL10gejrWu8-qI9tM1fevXog5zThaJoIgvMq14Tjaqu9FmH7NgYrdKL8uXaN0MbpSyw6odZ9sarkSSIhe9ym2bR1AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات سپاه به‌ سلیمانیه عراق
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/69403" target="_blank">📅 02:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69399">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SC_S6Nwt9CaVIyEb7_e97bogpIy-Lzue_wWRkt5I1v6rjErInHvI4bH7EHxiuRg07Vdp4wO8gwdzDc1yM5Rp3fyQLs81izqMzWnqV503Lbus2zvNplDCaaaMtPi3sbfMGCLfvwwxS1DZfCjNIL7nzUnI54A1is41MsWDfYWPDgs_ARSCl2ie-QBkkkY6fDBS19c1ILP-bdTbMdEP1fwC-6_A7zToC5M-IXZ2AD8l2PM7ZnKWUYMHJ0cNzmkt4FLt3jr2NuV9BgKuBVUEO2YRdw273ClgT_ADiZA6F4sf4uh7T97kmX0DVlf5euYjL_1UCBjpul3KBSMqLE3p6DyuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYB5d2acw2gqCJDIquzyNUvRVJ3Zuh0GuGPQHyJ6vyiKaN-eoisX5QPPfPGDbo6xpPzk2ORqvIUzxSr2NtBtTRcKoTzYqyO0kwja4NtSCymEIXEYWt4HPFAjcDuE0myR6J299VyNTPw_T5f-NNNE24dxEFEyFgTEovii1T1kHlUhT4iNAh50MW92jw5itQtWlXv7M4jWQAJz88PZN7X_e3iShZZYzf5jE73csebFCKbNdrZAXEOHD7Elj9JyEDHZR7MzBUX7CVakp8cNzQlPqsvdzExAVg2Lo4e3Id5AK578yGUw8huZ_VbqWD_rQy6NIWRAvH1nzcIR-gu5GYXczw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=mRfjXFos-PFYtPggdZOUouc2oyc3Rjq_AUWvo41U6qecw68cRs-uHGqOGxd4nVJ87Nj5sOjOgfL4P9cfrYkWhxqEkQ0ESIwssujfgwRHFsVAPQQmV-D69Uo8LR6vp3jDbMhKFqo5Ey6wdidzm3pyRb7N92JAHuAy49deMbF9xFZVAVcFTIIoVoCzdhLkmkADk9tKHTtCthockKW-aOYbbpxXADmaARHiT2GGmqH5o7lX0vyLUAISfS6DTILurPqqlKWDGdfbL-ftqF-Z7uFSJNcaTpc-ag8zE1UXpa9q4xTTnUzEgAOxbJYQ5UcOAjmZ6hgDRnMd12D6r8WoQEPiEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=mRfjXFos-PFYtPggdZOUouc2oyc3Rjq_AUWvo41U6qecw68cRs-uHGqOGxd4nVJ87Nj5sOjOgfL4P9cfrYkWhxqEkQ0ESIwssujfgwRHFsVAPQQmV-D69Uo8LR6vp3jDbMhKFqo5Ey6wdidzm3pyRb7N92JAHuAy49deMbF9xFZVAVcFTIIoVoCzdhLkmkADk9tKHTtCthockKW-aOYbbpxXADmaARHiT2GGmqH5o7lX0vyLUAISfS6DTILurPqqlKWDGdfbL-ftqF-Z7uFSJNcaTpc-ag8zE1UXpa9q4xTTnUzEgAOxbJYQ5UcOAjmZ6hgDRnMd12D6r8WoQEPiEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇷🇺
ساعاتی پیش یه انفجار تو یه رستوران تو مرکز مسکو رخ داد؛
جایی که به گفته منابع روسی، مراسم عروسی خصوصی با حضور چند نفر از فرماندهان ارشد نظامی در حال برگزاری بود.
کانال‌های تلگرامی روسیه می‌گن "الکساندر چایکو"، فرمانده نیروی هوافضای روسیه هم بین مهمون‌ها بوده.
گزارش‌های اولیه حاکی از کشته شدن دست‌کم 3 نفر و زخمی شدن بیش از 20 نفره!
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/69399" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69398">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⏺
المیادین:
بر اساس اطلاعات بدست آمده، گروه‌های کرد حاضر در خاک عراق در حال آمادگی و برنامه‌ریزی برای اجرای عملیات علیه جمهوری اسلامی ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/69398" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69397">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/69397" target="_blank">📅 01:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69396">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=fldfRreF1BA8xHuEv_VxtqMyyZg0y9f_pmSLN9DqewMK--4IGwQrqPT7NAT-AeSmr5CuoqAeJdUauuJUB3Mwxa6z8QtuTiNO8ugKt7kpv-zaXhtkjmUNpE-MYnWK5X6bN2TzX11gneB2c6fmf716nSjcEvk-RXVd5jsEPi0LZ5n5Zkr3ifsdDVrPBKdNwJyCQx0tABUKnVFo8NQnFCPODL__CsAaF4Wx1l0IyscXnIagyLNxsKpW79ex-BEEyZcPDngYCiXiqk8eSyfANsv7r5L4fHyPfWitibjyzIica18AX11xBUbOkgc6KCjBw80DvNEuflYKHB2cht0BqigpYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=fldfRreF1BA8xHuEv_VxtqMyyZg0y9f_pmSLN9DqewMK--4IGwQrqPT7NAT-AeSmr5CuoqAeJdUauuJUB3Mwxa6z8QtuTiNO8ugKt7kpv-zaXhtkjmUNpE-MYnWK5X6bN2TzX11gneB2c6fmf716nSjcEvk-RXVd5jsEPi0LZ5n5Zkr3ifsdDVrPBKdNwJyCQx0tABUKnVFo8NQnFCPODL__CsAaF4Wx1l0IyscXnIagyLNxsKpW79ex-BEEyZcPDngYCiXiqk8eSyfANsv7r5L4fHyPfWitibjyzIica18AX11xBUbOkgc6KCjBw80DvNEuflYKHB2cht0BqigpYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/69396" target="_blank">📅 01:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69395">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpA8tqZ3b5-V6a4OhvX4yeO09wWB9WiOknoalHqQCGFplr7SuD406zR1V6wOxRQlP0Et6SwO6TwSzYyBODtofkKjZ_ejLp56Dl8QjJJw22XvpWnGyYckOojL3wvQP9RA-SxwaBrO-hMRE7DKp5XkXX07DM5O5HMlkMlr-E7hGWB2gGHxFUKKk3PGrMTZo-ua11h_oV_5i4Fb_kbfkm4ompOXFfSTFgHkiWSSxyOBnVVX3oCgC1KvOnOFfHOPO2m_CI6to7B8l5UltslwMMSaY_F5kR7vfX8uhEgnJNS-xjqpgC0K8reAeoYQNUGZVAgXFJ-08GhGBPLYQD__a_bFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
توییت اتاق جنگ اسرائیل و اون ساعت شنی معروفش
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/69395" target="_blank">📅 00:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69394">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=Ar5PxQcdH4avyAwkVZ1L-GS8x7-bfoVfHMN57R_EeozZrfUlGtkLv8-tD-VWIXDi4Ed44rZRcQvvNqBgt3UE6xCGK2mNB_XkqiDzxMtt71oia7ijYhhXIPh7Fgb_8yrcqt8lD3yLjBSXRfeuMVq4h5Pe4UeAAYjymUNdcHjGSWB6hfLmQ3R3QGCBEmXW-rQjkaCprsgfYGoj3dWClV_T8gB52Q0Zqfr5SWELkFrnLmaJXE762vaB2sCEhDjGL8rIuVovZITMMvR7vAgHKG_joq2taMiHIGKY9eijNM-lbHLhicPG0zq3Zi15EpOgsPvA2dc0qtOYiIne5A5a4T-bVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=Ar5PxQcdH4avyAwkVZ1L-GS8x7-bfoVfHMN57R_EeozZrfUlGtkLv8-tD-VWIXDi4Ed44rZRcQvvNqBgt3UE6xCGK2mNB_XkqiDzxMtt71oia7ijYhhXIPh7Fgb_8yrcqt8lD3yLjBSXRfeuMVq4h5Pe4UeAAYjymUNdcHjGSWB6hfLmQ3R3QGCBEmXW-rQjkaCprsgfYGoj3dWClV_T8gB52Q0Zqfr5SWELkFrnLmaJXE762vaB2sCEhDjGL8rIuVovZITMMvR7vAgHKG_joq2taMiHIGKY9eijNM-lbHLhicPG0zq3Zi15EpOgsPvA2dc0qtOYiIne5A5a4T-bVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمود احمدی‌نژاد درباره دستگاه سرکوب جمهوری اسلامی:
نیروهای امنیتی خود افرادی را به میان معترضان می‌فرستند تا با ایجاد تلفات و آسیب به اماکن عمومی، بهانه‌ای برای سرکوب خونین فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/69394" target="_blank">📅 23:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69392">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mB-J5mnXMtISeOqO9RVjY2LX0zc4elwcnt9RCYBZ7BUKCePEb5i91W3m6nTUyiOqs-sUG0zxVKzjCTLhfnIpq3MIXOf4KgyOPo_411tpN4DMgG0Tzxonn5PW_MAK416ldELXo3r5_QWAuVrBkm5T0Tuok3TiKPs3aq0Ugn9DtstDVbnHE0Re1A2XnDWjRnkHTk32MDhJHU9jx3k_Vka3jErgYmpNGthBEE-mRAuHy5y6sYZzg0kJY7xkE4tqObiUk1du-NJCB1MHdbed1acyxB3cGuJHw3YWZVeTnVMG4NO1sKVcQfy43m_I-szb5tqjbG1tBPc1d7Uw18kZUa3fOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=lm8ns4YdFxWz3RPPd2ZdX1R1fIkVGdWjXU78iTMcB-DcezH5e99HgPlF9bXm1p4sFCgUqUY50l-E7myq_Zco308Bmn7ryHzMRBHSJnTwFEGvv01rpnpRFrCkuHkf9bhZrTDJp_AXXrl-djhWVgt8weAua0nPdZ2Pq_MUj26i8luLP_4gS3DAHRSGkWk76_rZV8c50ZYaHfuNeJGdgaJ1fj1m2wwT-pnpWXExFyWVUArTf1_v-9H7kOVTIdw_ZBQgqpjX6Cx88DDvymxpNO23KdHg_eBKx-1edI8_Pt6o3UjKvekCpmnZVV2SwFU55b4jvx0U2RrvsPbsHbXzP6j40g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=lm8ns4YdFxWz3RPPd2ZdX1R1fIkVGdWjXU78iTMcB-DcezH5e99HgPlF9bXm1p4sFCgUqUY50l-E7myq_Zco308Bmn7ryHzMRBHSJnTwFEGvv01rpnpRFrCkuHkf9bhZrTDJp_AXXrl-djhWVgt8weAua0nPdZ2Pq_MUj26i8luLP_4gS3DAHRSGkWk76_rZV8c50ZYaHfuNeJGdgaJ1fj1m2wwT-pnpWXExFyWVUArTf1_v-9H7kOVTIdw_ZBQgqpjX6Cx88DDvymxpNO23KdHg_eBKx-1edI8_Pt6o3UjKvekCpmnZVV2SwFU55b4jvx0U2RrvsPbsHbXzP6j40g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا کاظمیان از حامیان جمهوری اسلامی در انگلیس که کارش زیرآب زنی مخالفین رژیم بود، دستگیر شد.
حالا فیلم لحظه بازداشتش رو ببینید که پلیس اومده بازداشتش کنه، میگه تروخدا بذارین زنگ بزنم پلیس
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/69392" target="_blank">📅 23:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69391">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=QwWgFu4MjVUfHWsEsPuFbdkKyVGlejDAXVTfX8eeuU3PY0EvCiaZ4RtQ5rgs29FRiZZ5HVmBVrUad0SkNbA5sfAgZ6jUtwinf5vEi7NffWlBqfFAw_4MaT6tkpPq_HjYijtwJxFCjOXKDLkCC1aBHfVS7eQz8ccnNQqOJEG1jExlFZPjtGCx3QvpTDGe-OYdCOAySFW4gw7ohtgL7_v-vZQqrlwK1LDUP7YMnFZRIgxikEoxqnblRK5EeNkPIe-xqtbqaBVtXaHS6vKIBt91J7RhsaC_DX1KBlJBiDvvDX6vD2cKvcNrsVUG8hI9VNoU2dLimBBI813jHyD0Pc8cYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=QwWgFu4MjVUfHWsEsPuFbdkKyVGlejDAXVTfX8eeuU3PY0EvCiaZ4RtQ5rgs29FRiZZ5HVmBVrUad0SkNbA5sfAgZ6jUtwinf5vEi7NffWlBqfFAw_4MaT6tkpPq_HjYijtwJxFCjOXKDLkCC1aBHfVS7eQz8ccnNQqOJEG1jExlFZPjtGCx3QvpTDGe-OYdCOAySFW4gw7ohtgL7_v-vZQqrlwK1LDUP7YMnFZRIgxikEoxqnblRK5EeNkPIe-xqtbqaBVtXaHS6vKIBt91J7RhsaC_DX1KBlJBiDvvDX6vD2cKvcNrsVUG8hI9VNoU2dLimBBI813jHyD0Pc8cYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کانال 13 اسرائیل:ترامپ تصمیم خودشو برای حمله گرفته؛
میانجی‌ها که آدم‌های خیلی خوشبینی‌ان و همیشه میگن راه مذاکره بازه، حتی اونا هم میگن حمله‌ی آمریکا از هر وقت دیگه‌ای نزدیکتره.
آمریکا هم از طریق سفارت خونه‌هاش به مردمش تو خاورمیانه هشدارهایی داده که اینم یه نشونه بزرگه برای حمله مگه اینکه ایران همه رو سوپرایز کنه و برگرده به مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/69391" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69390">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⏺
🇮🇷
نیروی هوایی جمهوری اسلامی هم از دیروز تا الان مشغول آماده‌سازی خودشه تا در صورت نیاز، بعضی از اهداف تو خاورمیانه رو هدف قرار بده:
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/69390" target="_blank">📅 22:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69389">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mcol9JE1f9PfZd85-jnKZ-9J6pH1eaElJrQ27kfOkbml_SlFzK8Z_I8ej0WXU38NcnlwLtmGDfIkBgVyMynkhzoywvl1GgwbezMA1g9l0LOQzQVqos0JEi1uO-PTQ1qSt2VTe_vPL018qljxzooMJUXTpLWL0F54Ja0CltxiDYY0wQ-xzRqSlvrfaesaTKqOa9HwtU0E7d38gisWrTzYpK3BRqvl5ijRnhnaGMoDjh-afpBbXN-6zXVK_IvEi1PE89E1e6RTZ5RYXZMT5uuAwnQQkXtTTfbnzo31bdASmk1CxY6_HBk7gMnuXhSIbKv2_dlITOy8uPom1YRnGFEGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/69389" target="_blank">📅 21:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69388">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p22jcH0_wAcjQXFMHEZlWR1Tu8srOHHZeaDGsDz8ZU6MmkFlwA2ME2aqq0FkMSw-OT5r4TtO-6oH2eLjzNNWRfa6JXHMpc2cMARjuRvFEBcYupNz2_2Grbd7fkrFu67ELo3BdSlL_tzX1RBwfvI2vC7hgPqJPqtxu0a_ESGLfZxIXXwntT2EPp2NjRLd-QCMAczRPCSB2myVq49nju33WEjg_xWVbK0r__ytRbjbl30nEnZTasQf7y8gfQJNgbbt0UNA7Mdpv2WWhNuuUsnqgO4oSIdAqKQaBDv-p7VZeJm_paMtAzFol9rw6hkmeTvkUrxs127_vnCkSo91RxjsWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/69388" target="_blank">📅 21:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69384">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjYci-QqH2H8dl0gnp8mqDpA8gScsPJyHL0tBFI7_UwzRXqCXaHr3yJcs8G6ZVFOMw4Y28gW2z9eilAMchFdCbMcAV6vH6wN2BuaJAq26KSxg_dBfypDoUo27IwgcBr_6SGa91stpo9vdpZRJWHOL4hfx8a29R8fN6E9ABvlKJJzklUPp8qcdpTlf0S-dc9VgDTH0X1yTV9KcjLzDG1K106IV3noSGZWLmBSBQ5PK5W-1AW1-E1JS8qhQq6zqM2ufhkxCImQ3tA8h-EgG4-ERmvEreLqeHD_8XIwUReGmg5ijd4J7NHjZUummLgcu9smRuVStRtOGsZHGmIG1OCEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0PJOTTJo58u1fBYm9M9azmQANljw799Czo9zASz6n36XP-iUjpq0FE9sS-s2JXHmQirIHN6QLsV8BmU1Zyp6QLVbuvzpBUKsetezSHBtXKRjpgzXsLEZfMuCJXmJJtsKtNJlJP-5ebgzJKTI14mSEDWAACzG6-2spc4V5eLdersOAsfzCHEHnbiT8ZFwm-gQx5ck1pFczC93C4dpocWVDtrieCuqH4k-N-unyMc6NNJc_Z6zNAWLI1WVpNzMiIPq3CF4BfRPpPqF8PT6gyRBEHULnuGt-Mswkv5CDLz22oYovZastJ8OJH6D4Je0k_aYDiR_gRmEm5nnwiBwSAY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCZg1cvkIfExZEGxkosnJhDNm0VlE316K_ogv-biwURIPWri4dOVjtpaBNLbYx8K9QvrNeTlzMnoECHNrRhfrzH3XtGHB-kG2d3t6EmtQv8lKnu-MYmSstyHKINWVxKdfLAxgposRrg3H3SeA5ex2xcj18wksdlq1jmcnW_2VBExJ3JWDSykXYJDxovYpj7eOUn49Zj7JLEOaXp0F7ou5Hb9tnDHPp0mmd2A1Z15aftfnrvAnwn-mXpmf9SOkwAiKsF1oONXSu9q8AzUp_ZEVkNdzd6KhrL8zQ3tFYn_0bUnCtYi7p0nRPEtQC4G5Qm5CKpwcIefPww4-30QLJSl1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9C5D4pgdOlLFb4R_IwGIxZ-EvExH3cmGnZnG_LDVmWy2aEX8M2B1pRmzMrpu9_nLwXPa-WXsHl1l6t8ERGrnHWC2NPLXd7TwLuIYrJH_Q6J4hQCndjsQitGODe2Ny9FhtkwjJdBLxnHWgLkBt3_dlbFWSOzB7NlrK59t528FTJYvcrGyFbqsNs5t5CRQ9ENRmWWFZNBDAQyBx-Z4h7WV5MjM7LGyfB94C9RGkcDuv-SRCt2QeMbvl4eROje8KpCvX4JQIAij6T3MB8JOmBYMz9GKdBJTA3OrYbeXU9WeWIWr-jEtOuejqfM8GQojbsSLi-NOQh0unZMaIoJ5hZ_-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
پست های جدید ترامپ
از تصاحب گرینلند تا جنگنده و انهدام ۱۵۹ شناور جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/69384" target="_blank">📅 21:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69383">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqC-lO-n7hJSCjDkz1iUOitdiDWh2ALLXm8ChwWNttvdXx6xrGVAe0Gx-XA7cLOxuLEq-tWY25uXR4T5GhJtzZScCYLn7U55xyvzLZ8qrQeGm6FcwomjUj5TB8qbGFCBzU5ChbyIy1dYmlr-cylqEu8SfIFI9b2NOjY22z_XWkgOa3BVtIK2UeStczK60qcmpAT9YKDWVgWMPF8CEY6Dtpd4WAnV-pa1CyK8XgM3JNUhTpVfqcd6_dhdW8zNryuavVITD5dEZ-PtJsu-iFFvvVwUcxTpIbkP_Uy8-Su_l2JrWLF0ktK1LqamG8IUDxTG4KaZ9pc6m3B-V9B9DIXb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69383" target="_blank">📅 21:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69382">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuL50IIi2KOpMpplk_nFWxS_W8aQOZ-ePtek0kerUQxZdXzFRrmh3Hs-zdCFCBl6aTpiiIXKRo9cEUL9XAY_OfpQLiNWCbD0sAg2fsTTtlLKTfhjzb2BLjQCPTdpBXF2uzSCkYAAgBF7qBmnOUFTU0B_jC_-_go8Q6nJWiwxRvXmkhXIHGIUi5T7N6vCF1aBi3CEVQhMQKuxCBJnHJ2ysnr2e8c1-TAmHCgpvPTS_XfN8RzBuEcKFvjFA0MsInogmuKA4szZcW9HLwMuj1ZSI0iU9SSS6B6MwyyhR3hkHto4DFBmG_amhlEkZE4YWhZ0ISsBVOCq4pjcz9jOTnBHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
بر اساس اظهارات رژیم ترامپ، کاملاً محتمل به نظر می‌رسد که پس از ماه‌ها تهدیدهای وحشیانه، امشب آخرین شبِ وضعیت عادی در قطر، عربستان سعودی، کویت، بحرین، امارات و احتمالاً عمان باشد.
اگر حملاتی علیه زیرساخت‌های غیرنظامی ایران صورت گیرد، زیرساخت‌های حیاتی این رژیم‌های همدست — به همراه زیرساخت‌های رژیم صهیونیستی و شاید اردن — ویران خواهد شد.
مردم ساکن در قلمرو این رژیم‌ها باید فوراً برای تخلیه آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/69382" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69381">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل:
این کشور در بالاترین سطح آماده‌باش قرار گرفته و مقامات ارشد سیاسی و امنیتی در طول تعطیلات آخر هفته مشغول رایزنی بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69381" target="_blank">📅 20:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69380">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpsqQb1OqCnCGyoVLheawiAc8f4D9vDYh-lNAxJHgn0ZHJiE8o8GNL4QC0Ef-HVYod45e8jjwi2voA2LZeHud27TplVnuMeqH6bi_E9uOZiUsdJLz4JJfWZVLVsT0bJs6ce8ls_i07IDSU-SXRwYOVc7WxxIUV--wcCKBxSUlnxWHRL3vZDhVvWJad6To7PQcvpqnf-j9fFmdAZW0xg51_nXtoQZTA8Ot3YJXn3oPGlx0DMrb-edsc7sAvp0R6vsAy4c9zMxTmwsJ-fhgZ8-5vYdRspAIHBe9zaClvVoRy2_GoSdovNRJAwstOyjePtzmgt3g5vBxtQnxuoOthruiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
کانال 12 اسرائیل:یک مقام اسرائیلی؛
«تنش‌ها به بالاترین حد خود رسیده است؛ ترامپ بیش از هر زمان دیگری به انجام حمله‌ای بزرگ علیه ایران نزدیک است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/69380" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69378">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799177ea92.mp4?token=rlK7bKc3zkZO772tzPvF_yMheXTwybQPo7v_LzSM-6HGKPn0Vr5ZOFIEm1t_sK4nQi736R8M28yt2evnkXUJg3hxq6RiTnPEB6tXbhktNx5HnfWB4UiA-M3EgdzH1gkbtaeQBym-BfyZStulLK_vwKjIpJlKUBQlNitT1AedlKDIu4v0Nst07Q5a6pTleyhNMqXJmPZdCpub4jsLM5223imyAcSEKVzqbNtffHzrtrBH_Lvj0dY190Bv_fkGQWrwBqh0leu2HUWwYDzmik_hAuIPDmFLkisgmJvA-FnuMTjWlJxsCfWwJAjMAzrGNhEwLa9MtXLQ1XM9YqQ27d52hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799177ea92.mp4?token=rlK7bKc3zkZO772tzPvF_yMheXTwybQPo7v_LzSM-6HGKPn0Vr5ZOFIEm1t_sK4nQi736R8M28yt2evnkXUJg3hxq6RiTnPEB6tXbhktNx5HnfWB4UiA-M3EgdzH1gkbtaeQBym-BfyZStulLK_vwKjIpJlKUBQlNitT1AedlKDIu4v0Nst07Q5a6pTleyhNMqXJmPZdCpub4jsLM5223imyAcSEKVzqbNtffHzrtrBH_Lvj0dY190Bv_fkGQWrwBqh0leu2HUWwYDzmik_hAuIPDmFLkisgmJvA-FnuMTjWlJxsCfWwJAjMAzrGNhEwLa9MtXLQ1XM9YqQ27d52hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تخلیه پایگاه های هوایی آمریکا در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69378" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69377">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483837b794.mp4?token=P5E92QSD2HqCEz0LqvzmxVIkD0cCDDw_cjDrF2jK6s__RxlrH1UItLI8bnDGTVqtKi6lfxjkipDQUpZ1V6HKJ2qjh6VA4pd0SKPVOKehvIOQMSbDtm1hX5GB7fM9A47-HdQHW3ByM6XpAHrEgnc9cHoQW9aPH-F1iy8B9RnPmrYcKMgY5erfJk-SF2DV9jwa4bsEjViCx3yyxidyLv-wSWJslaFnbYOMLqzn4SUpwkVq6rWCcGj-mgNEQPccwZLcetB_Y4EiNjAwfSABH0SL5zjMI5AIpGXhcnZE8HZKP__CTIuPWTZBAeujINr5HP08tfHwzHjK0pcASu6AwcIwcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483837b794.mp4?token=P5E92QSD2HqCEz0LqvzmxVIkD0cCDDw_cjDrF2jK6s__RxlrH1UItLI8bnDGTVqtKi6lfxjkipDQUpZ1V6HKJ2qjh6VA4pd0SKPVOKehvIOQMSbDtm1hX5GB7fM9A47-HdQHW3ByM6XpAHrEgnc9cHoQW9aPH-F1iy8B9RnPmrYcKMgY5erfJk-SF2DV9jwa4bsEjViCx3yyxidyLv-wSWJslaFnbYOMLqzn4SUpwkVq6rWCcGj-mgNEQPccwZLcetB_Y4EiNjAwfSABH0SL5zjMI5AIpGXhcnZE8HZKP__CTIuPWTZBAeujINr5HP08tfHwzHjK0pcASu6AwcIwcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاخ سفید:خداوند سربازان مارا حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69377" target="_blank">📅 19:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69376">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746862829.mp4?token=tAR0LcAGCP1KOIg5TWiy0_TAhuZ594hzZELAuyl9NGlQj4oYnPKcwHnYKa4tZbKARwRodNUTvXBEoc8KIgzJcaD-e0-iCOOzng3iFBQ0KiQ2ndHss-TgHqazQoxZbIsOvYQwm0Yq-1OPUuGi2N-Sa6DQd23z0TlIqhQKPkIqs-6UavpieJ25FgO12tXSLTDM5LnX1jvZQkxYeV7DjKGnC0napd1BlkaorDqEHWwusuP2fjQ2LQbu4USYjVcXDY1N-kCx0fGWa2RwfanuGhJjXDE0MglKh409O3qfIQRXYBIQDgCvNf5PQjuDq1r_B64Pwn-RGWgeBAi_UNZx0UQUmD0ZYIWkpwDxT6eRpGw2tnDuADc_sNtDXiwWVUlPbdrYOTWiq-miY9SJaI-_LnHPLyOSkL6Viy8IqRLuJbzC8_BWRNWPgtU_MNF454NpubdkVofqgd2b4SxYrwUlDkW-X4q5TYLQBeBAPj3u8O0F_5wug1YSgjc3cFMFei2cgOXWpJK9_SoyVGjHPd8o-yhbtSaft35qnwn_Pp4tXG3vr3OWYc_GQpygzuD0GaYCzrR6HuCsU4Td2dhBgxREgxrdavx2ce3isovl95U9w5fZ_1TlQ2Th1Z_FNwP1Ha34hzr8N8Tc6Q0QaC9YMQZZY2HMU_GAeZLgD7MOjQxyzUYlABI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746862829.mp4?token=tAR0LcAGCP1KOIg5TWiy0_TAhuZ594hzZELAuyl9NGlQj4oYnPKcwHnYKa4tZbKARwRodNUTvXBEoc8KIgzJcaD-e0-iCOOzng3iFBQ0KiQ2ndHss-TgHqazQoxZbIsOvYQwm0Yq-1OPUuGi2N-Sa6DQd23z0TlIqhQKPkIqs-6UavpieJ25FgO12tXSLTDM5LnX1jvZQkxYeV7DjKGnC0napd1BlkaorDqEHWwusuP2fjQ2LQbu4USYjVcXDY1N-kCx0fGWa2RwfanuGhJjXDE0MglKh409O3qfIQRXYBIQDgCvNf5PQjuDq1r_B64Pwn-RGWgeBAi_UNZx0UQUmD0ZYIWkpwDxT6eRpGw2tnDuADc_sNtDXiwWVUlPbdrYOTWiq-miY9SJaI-_LnHPLyOSkL6Viy8IqRLuJbzC8_BWRNWPgtU_MNF454NpubdkVofqgd2b4SxYrwUlDkW-X4q5TYLQBeBAPj3u8O0F_5wug1YSgjc3cFMFei2cgOXWpJK9_SoyVGjHPd8o-yhbtSaft35qnwn_Pp4tXG3vr3OWYc_GQpygzuD0GaYCzrR6HuCsU4Td2dhBgxREgxrdavx2ce3isovl95U9w5fZ_1TlQ2Th1Z_FNwP1Ha34hzr8N8Tc6Q0QaC9YMQZZY2HMU_GAeZLgD7MOjQxyzUYlABI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیستون؛
جایی که سنگ،
به زبان تاریخ سخن می‌گوید.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/69376" target="_blank">📅 19:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69375">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=bUqa3MtEpAb6jCNRurvhFWbBkWf4kcESebOlTaJJHwxo50uN1v_SlucFFpQhUA1CulKiyJiSgJZih3Vp60FqVjWxeHCViI4jaVi8kCbpSvWuQXLMrYydsRas5svIextgjxDeT8rbLuD0DYKhzKkCqaZy9lDtcpf2NJqohnjIbcOBBsEjeZHEARUPdsoC2wu5q8ti1Z2QJQS665-mMRrJjyyEUPXhO0qsTmotgXmIRHsgyGfLYUVqVbq601VAwwspQ2t4YwfUyQRrQg9oxFu1B5NfjGqDSQI-DXwyZ0_FQz1icGclx4LGfpatr880M6T-zJZ8oZdvNGM011v-0sYABA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=bUqa3MtEpAb6jCNRurvhFWbBkWf4kcESebOlTaJJHwxo50uN1v_SlucFFpQhUA1CulKiyJiSgJZih3Vp60FqVjWxeHCViI4jaVi8kCbpSvWuQXLMrYydsRas5svIextgjxDeT8rbLuD0DYKhzKkCqaZy9lDtcpf2NJqohnjIbcOBBsEjeZHEARUPdsoC2wu5q8ti1Z2QJQS665-mMRrJjyyEUPXhO0qsTmotgXmIRHsgyGfLYUVqVbq601VAwwspQ2t4YwfUyQRrQg9oxFu1B5NfjGqDSQI-DXwyZ0_FQz1icGclx4LGfpatr880M6T-zJZ8oZdvNGM011v-0sYABA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
دونالد ترامپ، رئیس‌جمهور آمریکا، و ولادیمیر پوتین، رئیس‌جمهور روسیه، در قالب «زوج در حال بوسه» در رژه کانال‌های آمستردام:
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69375" target="_blank">📅 18:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69374">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=OtR9LQZjEkC3Yme4kubXd4q1EWz9lZ-xfOdX36pftOQ3XMRbE1Gv5DICj5PldG1uol4QQ7FHb14wJkLaKSZ_G1Kgpf_lXBBbh-hnvfoR0qrmtVRFbifofqNXuibPqopM2Igx4EOVK7mWrAAHvccT2V2EgaBeCQAikyZtnDhbO6_QXPa8SoD-HgyJ6Jzal54UUuIYMyljkdp9KfaCWolTGBtRuxG-SLHhWsZxNX1Kh2wyAbhVmVbqCpwJz_YNlvm2KKbQMewYndIj7-lMI1qkJCBnsztmem9NkdjshfiVCzkFtp39B81p9CyR8qi0qQTo1iUg-bUeZq98Lhd48fd8tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=OtR9LQZjEkC3Yme4kubXd4q1EWz9lZ-xfOdX36pftOQ3XMRbE1Gv5DICj5PldG1uol4QQ7FHb14wJkLaKSZ_G1Kgpf_lXBBbh-hnvfoR0qrmtVRFbifofqNXuibPqopM2Igx4EOVK7mWrAAHvccT2V2EgaBeCQAikyZtnDhbO6_QXPa8SoD-HgyJ6Jzal54UUuIYMyljkdp9KfaCWolTGBtRuxG-SLHhWsZxNX1Kh2wyAbhVmVbqCpwJz_YNlvm2KKbQMewYndIj7-lMI1qkJCBnsztmem9NkdjshfiVCzkFtp39B81p9CyR8qi0qQTo1iUg-bUeZq98Lhd48fd8tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
فاکس نیوز:
رئیس‌جمهور ترامپ در حال تشدید فشارها بر ایران است و می‌گوید در صورتی که مذاکرات دیپلماتیک به نتیجه نرسد، انجام حملات نظامی جدید همچنان یکی از گزینه‌های روی میز است.
ترامپ پس از دیدار با اعضای کابینه خود در «کمپ دیوید» اظهار داشت که توان نظامی ایران به‌طور قابل‌توجهی تضعیف شده، اما این کشور همچنان از برخی قابلیت‌های موشکی برخوردار است.
مقامات آمریکایی می‌گویند این حملات ممکن است حتی در همین آخر هفته انجام شود؛ در مقابل، ایران اعلام کرده است که در صورت هدف قرار گرفتن زیرساخت‌های حیاتی‌اش توسط آمریکا یا اسرائیل، آماده پاسخگویی است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/69374" target="_blank">📅 18:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69373">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=urN3SzVSyKIeVhAtx6XQ3vvuXVCZlY7wJKiYmkuapIzXn0O8c27JEtxNgKmrTtXhrIkTMtxT4WNXmUEuWSZsJABb3S6NW3MAjydmH7_XE__YeTvyoQtUmLARPhoHdZUAZThpZOYKZHn0av-lhjzPvue0rtlurWd5SJiqVAvqWqreAQUci9ARvIQ-hlQUa3uJh6HvsW02nFNmjiXKBteOsn4rMbJzPf4xw3uBanM_MKdHT2EYpY9pNsEN5qSoJPUdYTo602xL7ct3zeI3bgghNhaWAuq0yVmDcV59FpfPobKyuI5SdUPOx5N56hpuXKa3S5eXaAw6Z0rAvCBeFKkOXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=urN3SzVSyKIeVhAtx6XQ3vvuXVCZlY7wJKiYmkuapIzXn0O8c27JEtxNgKmrTtXhrIkTMtxT4WNXmUEuWSZsJABb3S6NW3MAjydmH7_XE__YeTvyoQtUmLARPhoHdZUAZThpZOYKZHn0av-lhjzPvue0rtlurWd5SJiqVAvqWqreAQUci9ARvIQ-hlQUa3uJh6HvsW02nFNmjiXKBteOsn4rMbJzPf4xw3uBanM_MKdHT2EYpY9pNsEN5qSoJPUdYTo602xL7ct3zeI3bgghNhaWAuq0yVmDcV59FpfPobKyuI5SdUPOx5N56hpuXKa3S5eXaAw6Z0rAvCBeFKkOXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک هواپیمای سبک قاچاقچیان کلمبیایی در حال فرار از رهگیری توسط جت جنگنده ونزوئلایی.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69373" target="_blank">📅 18:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69372">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=DZScPTtTeao10dV3FetS8QD0sDm6imJzTKNu1F2QwqpaRwq4XT83QmNJOP95B7SRZd2m2CLZNeiWW3_Nc7GsIG0GYfO7f7IAybbazNYNJY1ZPSoaP9J11xP4AdZszLnX6Uos5frBBt6N4UC3ARNGbTw91eNeNElK6P_G3Af4Kts_gliF3zooTiSTTRy39SpTIwknmAWEbF5N8SWGQFYxoJmvNJ0MK2HgPI5x0jgTc10bwsKN3JGvvvhub9NKErEDsMwXh6zKaQK_zNnSIl4cSy9N_dGyAyNbFq-e8CVKmix327Ia899a0jDLDM8FoFe7M39M2LUvo81FSwAsAC7hfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=DZScPTtTeao10dV3FetS8QD0sDm6imJzTKNu1F2QwqpaRwq4XT83QmNJOP95B7SRZd2m2CLZNeiWW3_Nc7GsIG0GYfO7f7IAybbazNYNJY1ZPSoaP9J11xP4AdZszLnX6Uos5frBBt6N4UC3ARNGbTw91eNeNElK6P_G3Af4Kts_gliF3zooTiSTTRy39SpTIwknmAWEbF5N8SWGQFYxoJmvNJ0MK2HgPI5x0jgTc10bwsKN3JGvvvhub9NKErEDsMwXh6zKaQK_zNnSIl4cSy9N_dGyAyNbFq-e8CVKmix327Ia899a0jDLDM8FoFe7M39M2LUvo81FSwAsAC7hfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح تو یکی از حوزه‌های امتحانات نهاییِ اردبيل، 9 تا از بچه‌ها مونده بودن پشت در و داشتن گریه می‌کردن؛
طبق ادعای خودِ دانش‌آموزا، مسئول حوزه ساعت 07:03 در ورودی رو بسته!
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69372" target="_blank">📅 17:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69371">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
ویدیو وایرال شده از این هموطنمون که در زمان شاه حضور داشته :
زمان شاه به دانشجو هایی که میومدن اینجا درس بخونن ماهی 400 دلار حقوق میداد
اون زمان صدتا نارنگی یک دلار بود
یه اپارتمان سه خوابه تو نیویورک میگرفتیم با سه تا توالت و حمام اجاره اش 210 دلار بود ما ماهی 400 دلار اونوقت حقوق میگرفتیم از شاه
شورلت کامارو یکی از ماشین های اسطوره ای امریکا بود سه هزار و صد دلار
با یک سال تونستم ماشینو بخورم
امریکایی ها میگفتن کجایی هستی میگفتم ایرانی همشون میگفتن شاه شاه شاه
کدوم شاه شما دیدید بیاد تو امریکا براش با کلی عزت مراسم بگیرن که برای شاه ما گرفتن
چه افتخار و عزتی و لوکی بود شاه واقعا نوع بیانش و لباس پوشیدنش هرچیزی نگاه میکردی لذت میبردی
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/69371" target="_blank">📅 16:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69370">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCaDHvSRJAj-UMglDBeuHeAKpyHrwokTniz9qrdOH14kdQR5qZ9gJej62j2aBOhq1vW8xYVvImVT6IKu6gWKgPxZreOwwps8byjNura4hFFcrK1KBPkYsWGWMZul5M8mWKkluOVDjQpi_rEfWGWSqk-LfRQ3XTTh1O3eZBW8k9NYz8rEidRuTfASfs6C95PNr0ncuQQxz0b5uG8lp4Ybp5mglNirzJblG_GloS1EjIAb4HhfQp9E8rOdTHWhuEqVTatd_92UYgDit-5vMcWLJSJq09jBLnU1U2ZC8ks8DUDPC6Dksjkv3llaA10mfbmr0-JmNaBm-VWRpN8er3mZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سفارت آمریکا در مصر هم برای شهروندان آمریکایی هشدار صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69370" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=kCYdqhzMBdyRVeN-JO-nJnSpK0qbAt7vc7W3jlMxdIV_LU3MT62woOhdZ8qzAZAJxdSAujfpu7ItNLNlVDfuq2d2Yp9KmteIKTAkUjNEhSNVZtjkEed_gq7bqFKh54qcFcJKsLZpHu8zyGdg1-jg1BeqnVrLXLKWf7vFNnjGZdqEP9wzSELS-8Scdfy3E-vQOasLyFsTSWO2q9FxShuZK_Pvsn2b9QTJ5zKyS4bPob8FtMHOsuUfRN21zrX3EJ5DaYQLZNxlYzWUctRDCq8GgdlefSJpyY5nniDLGNUyfczDAai9k-y5Gbk7xBzA48rcBdt-UVIUrUW2axQaLOrFiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=kCYdqhzMBdyRVeN-JO-nJnSpK0qbAt7vc7W3jlMxdIV_LU3MT62woOhdZ8qzAZAJxdSAujfpu7ItNLNlVDfuq2d2Yp9KmteIKTAkUjNEhSNVZtjkEed_gq7bqFKh54qcFcJKsLZpHu8zyGdg1-jg1BeqnVrLXLKWf7vFNnjGZdqEP9wzSELS-8Scdfy3E-vQOasLyFsTSWO2q9FxShuZK_Pvsn2b9QTJ5zKyS4bPob8FtMHOsuUfRN21zrX3EJ5DaYQLZNxlYzWUctRDCq8GgdlefSJpyY5nniDLGNUyfczDAai9k-y5Gbk7xBzA48rcBdt-UVIUrUW2axQaLOrFiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیرزن ایرانی توی مراسم اربعین، برای اینکه از یه زن عراقی صندلی‌شو بگیره، بهش حمله‌ور شد
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69369" target="_blank">📅 16:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حالا ما کجا بریم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69368" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69363">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NepbWXE-YcHq15NCfNGMEoXh6J_ZU4QbQQx-abHFnf_O7XsoeQeB8Ecffic2T9Zu6-zW4MOUdn91HwT6X_o8-7OJ9YLpSslRI8eIHcZyVUtTWTy-pg2U8dpcy2Jqvp4a4pLxkv_GcoP20DBhbTldwp-h-MKSymIkrT6aJHV2QyxAY0At0zzcoamRUDCkkVEAB5HYrMJD_8fwO0F2lXAkUR71fY8sO5ezg_AGCBxkMYYMeOxfGz_ElXgOfNc5-y3lO72cPWsztd8ptW30tYk6B6sOh1z_gDpLTL3Rl5n3uZSdMc5fKkKjOrByLP1AdiP7gGzxWsiXQcuML12Z4Oozlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auwfhAR7cNQO3GYXqStQTizk98e9vDWndRnOhdRnBZVXjvErYQvSBCynoWb8ATxOCT9A7_liU859VRMJQjJ-ws2kyjdycIST49L3ifhcCBdzbydEXhe-nV2po5EypHl1RtgP3WH_wxqme_5A9B4sjdio3w96JHVa5G4iKxPlbvyuBnEnrLLHU8HVYjwPqUlLKTOJwN6BqOkYuXmQ_faq_Wi8bgYvJNKOkoeu7zfKfnT2cXuEj5C-O43KBhjRH_xERnXvxJa7JHpcU133wq9fgxpHGzoXEm_7hXRdHbtkMWwt2d0l6u34Phpr2qIUE1Cq3ymdTAbm8eEB1Z-wNBR2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noanT6CGlQR4Wa7S2nEkonjxG0noiB_TAreDcfLxh9xn5II-waaTU1opVQqQRVdu9MV6BrcAbOgBW7SXc6-ZiMnNyC0zcn4xJ-YylfOUYzPv_ho-lDit4jhM4iZklSPplC9B9UMn-m7yYObwImR9EU_oz8dl1iXhfqeiYgQ8j96FdSeaRfOyytPWTev6DBh3ddBDeBhXETOCumxh-sVESJrz3IqnIBF7mqwuSalPhFXVPSxuIu60j3F-MX9s7AmR3J2iMkJULahu8IH2wqjftjmlyJFBI0Bvy7nMS72vg7N6AkTT6AxKNHElJtXYcSa9qL7HkEUEa3cFpMKDI7lt5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3bLwCCrpbFZQU1OupFhKnbY2OdPqF7hZGOB5n0geTAJRsCFEWHvicUJQAOOR7MPSSk0g8WKlUvqQLpJi8UbTYphOZCBDu3k0pp8VvXt8CAKXvpb2hsIgS7hvWTzAmWvSdGfAVfeMpChEZGbV9Bf6eO9D9xh1AGB0ZwdOukuxi8dpTOPU4LpnwfQen3WSV5fDBaOir4XmqYJV3nKUop_6BDE8WdQ_3HKV9zOXem1XHezwpt-qXbyc9Bl8sf-wKuV_96PDTZDlhIARX5Gc7sOf8gcTj54ihiArzddIn0WDQrV606VcdZHkObgPDIU6AX0_B0ObUXHrS4etPbYHWS9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GExys52fEIbyZCuJ3wK7lcrtVWHRc8pdKqPH8yuucIHnzC93e1NFmcrJNXLoEqScQVHv7-IEuTpkcJhuYZdO8EYW0OWGX2xGljVPK7iKtRN361Lkh79_bLBPWFP9NuQgAJDa4hcCeQ_lKexTz5EncFnfPqvQMiRH-K8pRI7kwf-y-kSldpi5wbG6fECeToIUglat5cV1Li1hYaWRS7XZUn70-82o90IlEtTYebSyK7Nsjj58GjtKQ6f9F_D5p_6IAENm6YSu5ZgdJN2faqdqUxjxKtkHfh61fsVkVyo1gRmZApUMqp9LKEWiLZOy4szUQHtl8XXdingXFuZbQ8dEwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارتخانه‌های آمریکا در خاورمیانه یکی پس از دیگری درحال صدور هشدار به شهروندان خود هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69363" target="_blank">📅 15:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69362">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=geONXhNqYDRwT2Kv_ZxIgwAVgTiq0xFs6si0NJ9eP_Jq0UseEwsWCg72WW_7mew-Ci-BW0fv2swrNoI-eGLHl-RckfTtXv91bA-b4xuDQyoe5XR028fp7-dZbUGvXVbLZ6a7wxwYFvHwAVgWAV3MuBj5ruW9UppQvyvY9XXC3Ddw67pgWdU4_MlHpX0XznGoDA7SnFgxIaC4M-7tFSQmKUkfs0cLX_iJgDgYZrUnrS0rQU1ZDm2lomlq3INgkM-Iam3205kW8X5w_-oXpmEXjPhgmY0LRxizKjyBg3CKmrj5X_CDMCcGVsSsrmjxJnL1cST8OHqz961M5_xNBEHnPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=geONXhNqYDRwT2Kv_ZxIgwAVgTiq0xFs6si0NJ9eP_Jq0UseEwsWCg72WW_7mew-Ci-BW0fv2swrNoI-eGLHl-RckfTtXv91bA-b4xuDQyoe5XR028fp7-dZbUGvXVbLZ6a7wxwYFvHwAVgWAV3MuBj5ruW9UppQvyvY9XXC3Ddw67pgWdU4_MlHpX0XznGoDA7SnFgxIaC4M-7tFSQmKUkfs0cLX_iJgDgYZrUnrS0rQU1ZDm2lomlq3INgkM-Iam3205kW8X5w_-oXpmEXjPhgmY0LRxizKjyBg3CKmrj5X_CDMCcGVsSsrmjxJnL1cST8OHqz961M5_xNBEHnPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده‌یاد مانوک خدابخشیان: دو شعاری که کار این رژیم را تمام کرد؛
رضاشاه، روحت شاد.
اصلاح طلب اصولگرا دیگه تمومه ماجرا.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69362" target="_blank">📅 15:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69360">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xx6dMXmuXbLfDrwG5e48Ky7x4AvXNgMIiHhOU4Rd9CmdS9lb9OzfahNqckp3RfPNe2_G-5Xh655f1-8V_Q7I5PFjGFQ410u482x93Qp5Z4dIkVWYQSmFXtEABHZ0nhU_SCLtzSa89Rpjjema5mbctRP-KwUzn0sUBdeJu9YHtAkAI__JBpLh3GBCjcoB6XpVlROi06GxdZvDyLDZiKRKOK-7FFY5ppOpjQEc5kwoA2tQZ1BVHjVAI-KAZxeeDZRhnTTUF_7C6r2YNNto6MTEXTp1QVMbESPvPRKK8d8uJWhJvLGaTdN1lBkJfz8jMPHPsJoT5UengOviCUkAJ7ulBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekmyi0dA4JyRTQw0ciOj1SHc1k4M2SCkGquiDXY8dGZ8DOIMf_O0SAxW5i1iboirxKsk9sAl54-xpbXRj-Q4LA4Db7wsYologZzCqWDsDLq3y9Bl2Y8kGrdXxZsz6JFfO7hfcPqgkSdaqEihVvLMuhVVYfgnjhUvpgoF5sG7xytn0IZXa8X1vHxCMZZqsThMxeHwBLfouP9DMv5J5pf98RKJTLSV3R-PP6z-b3PUnin2PdACEpJE21Ahk5dXein-CBzDf7H1b5akr3YjmLK5eHUVH8XQ7l6ykL2qYaz97_kE2cllQLgA3ivdmY9JT_x9OwFBU9oegfrdMsEs622LJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارت آمریکا در اسرائیل و عراق:
آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69360" target="_blank">📅 14:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69359">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxfXm4pbRm0z1yaO5y9vGcvO5DQsDjnaBD_yUhVhPj0FOKakdRBpEj7c9qByf3-thLKz0t-U3Ct8fQap57fkIz4GpYaJNKJvgZxFj1ETwXaJC6x0hV3z-yfmAG3FJA6BQffprMApliW2TbiNtYdWya0jxr0bLUZYndmWpspzo6ZE6qT6tFwOQ5C-dO_8WS-0G0L0zSt6PsPbbipLjZbYkd-NFeQ92F1QUoFUSzKXn7rzkgAookVTzAS_-Fke-XjoOOotxmGwEpMDpaXvX1jK2S9vLqJ9WsHbb7nIS7bzTL6seE28RuIfveSUVz0W_Xk9SLBslDAXJaRdjM4yqWGqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:  بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.  @News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69359" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69358">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
تسنیم:
بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69358" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69357">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
دقایقی پیش از حوالی اسلام‌آباد غرب کرمانشاه، صدای چند انفجار شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69357" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69356">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=hHvird2zDCSObHsunr9qL4aVZ0b89U39EZcAnPW0UjjFg2b3hTLjuIFVwP95mguuyhqAVP2iIDhPg3UGKqWsDH58Gn0j10TFJ7rqVejDf2IQsNP03-Un_QYDMuZaX-eFhFcoPaeuHTc7WrejLIA81o-2HcXpXHZyU63UNhO89tzCP7Ii9dARbOe5zu8WQkfBxT2oHwHvC42v9sGIrQGzZwMzwSWmPmc6aCJZcHcHnxfRXPvsB7cPLtyfjplmhqeGca8ml-HcMKg8ar9w0R4uc-MUcrOazgo1aUQDUN8UjprNV4fcj-CWXLgE1ZLXxP0xSOfevO3Y7-AnP-cHSx4B0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=hHvird2zDCSObHsunr9qL4aVZ0b89U39EZcAnPW0UjjFg2b3hTLjuIFVwP95mguuyhqAVP2iIDhPg3UGKqWsDH58Gn0j10TFJ7rqVejDf2IQsNP03-Un_QYDMuZaX-eFhFcoPaeuHTc7WrejLIA81o-2HcXpXHZyU63UNhO89tzCP7Ii9dARbOe5zu8WQkfBxT2oHwHvC42v9sGIrQGzZwMzwSWmPmc6aCJZcHcHnxfRXPvsB7cPLtyfjplmhqeGca8ml-HcMKg8ar9w0R4uc-MUcrOazgo1aUQDUN8UjprNV4fcj-CWXLgE1ZLXxP0xSOfevO3Y7-AnP-cHSx4B0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه جوون عرب داشت به زائرا میگفت بیاید آب انگور بخورید که یه ایرانی رسید و بهش گفت:
آب‌انگور نه، بگوآب‌شنگول
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/69356" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69355">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=t0v4azOJhCOGYxI1Q2I_U-ZGUc7hiFlMUxYNaKRzU89lWW_FnwXB4icQ6WZLzU4u0URv7H9VEs6CR44vhk2RtWOX3S6IGJ4uKAxQ1uppHlYtA88nxQJ-Ak0o7Tvh-bfxOWywQ4dEIdEIMIvsvt_BY157CBZe7ug8wwbS6QhIMVCrRX7iWywNG_5KYy3HVDTsF3j5EgfS1sqztaMcgQ8SJ6Dz7PidVZemz2nMUG_yHzFWpIKCUY4EZTrnKIPFscflLLC7-wXT-UnK5b0U6g1l4wxEpjt5RqfVvx4nDtQn1_lUw3ZWSmVEJqDwAC9iZ3euZQWWkpZFddsyq-17nFtvXRj6jF7PzFQKR-XvHcs_m1HsTXQMiAhYzmW_9Lcv167cc3onIXGstCFuuvgirRps_erDGXSo-wHoO3hFAzovfDEbCuoT_VFpjDJMt-y4my5GlDdwgZSYWwA5h2y-B25bMVl7cb7mFWyB4MMdQ0L9E1u-GR0qLQ1WwXGUj3LYleFJGm1lHMavT075Vw3qWAU2TNoecAiYAjivaCO7M7-HSTknq3mDJUpP4myJZ8QPLjfhXcVbgI_N2dYzpnrRzp-NinOfVVxDAURSFcEHpQcwy2q2QuDKn0m8k3oJQ0gmFL_DQGZOaTvnr3igDxGgFkLiGSP2-0jl1x8NJ8vcGxBl1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=t0v4azOJhCOGYxI1Q2I_U-ZGUc7hiFlMUxYNaKRzU89lWW_FnwXB4icQ6WZLzU4u0URv7H9VEs6CR44vhk2RtWOX3S6IGJ4uKAxQ1uppHlYtA88nxQJ-Ak0o7Tvh-bfxOWywQ4dEIdEIMIvsvt_BY157CBZe7ug8wwbS6QhIMVCrRX7iWywNG_5KYy3HVDTsF3j5EgfS1sqztaMcgQ8SJ6Dz7PidVZemz2nMUG_yHzFWpIKCUY4EZTrnKIPFscflLLC7-wXT-UnK5b0U6g1l4wxEpjt5RqfVvx4nDtQn1_lUw3ZWSmVEJqDwAC9iZ3euZQWWkpZFddsyq-17nFtvXRj6jF7PzFQKR-XvHcs_m1HsTXQMiAhYzmW_9Lcv167cc3onIXGstCFuuvgirRps_erDGXSo-wHoO3hFAzovfDEbCuoT_VFpjDJMt-y4my5GlDdwgZSYWwA5h2y-B25bMVl7cb7mFWyB4MMdQ0L9E1u-GR0qLQ1WwXGUj3LYleFJGm1lHMavT075Vw3qWAU2TNoecAiYAjivaCO7M7-HSTknq3mDJUpP4myJZ8QPLjfhXcVbgI_N2dYzpnrRzp-NinOfVVxDAURSFcEHpQcwy2q2QuDKn0m8k3oJQ0gmFL_DQGZOaTvnr3igDxGgFkLiGSP2-0jl1x8NJ8vcGxBl1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69355" target="_blank">📅 13:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69354">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532a951287.mp4?token=fJhQ2K7WCf5HMMRQAmkTzk-wvbDnxg-vktdoLTmvBacnzUibOwq3KL3WTsTAc-HJlaTqciBcYAZHXzmZqEYZHAORML3NV69xIZL2rj3cV4LKHDaHAprsTgFm9KODKYhEtSt0aKy8zxFqR5QATbLklEdEZ_cBWpCOg0Ciw07Ecvg0pgHkDkHi2W9ptxBhmaNtbmNk203PoJJr0Gw0M3ZPj5zjd7LV108P2CL5JSP6L7NlUGOqgm_Te_8Io9IvMSIjGfNr7kMTxSj1HMt4r9eXKhRlnMRKCw6VXmHzXeBEDJSxhMHvHkK7ftPQqORUsy0UBKjIM7WIg8uDA1UDtdopOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532a951287.mp4?token=fJhQ2K7WCf5HMMRQAmkTzk-wvbDnxg-vktdoLTmvBacnzUibOwq3KL3WTsTAc-HJlaTqciBcYAZHXzmZqEYZHAORML3NV69xIZL2rj3cV4LKHDaHAprsTgFm9KODKYhEtSt0aKy8zxFqR5QATbLklEdEZ_cBWpCOg0Ciw07Ecvg0pgHkDkHi2W9ptxBhmaNtbmNk203PoJJr0Gw0M3ZPj5zjd7LV108P2CL5JSP6L7NlUGOqgm_Te_8Io9IvMSIjGfNr7kMTxSj1HMt4r9eXKhRlnMRKCw6VXmHzXeBEDJSxhMHvHkK7ftPQqORUsy0UBKjIM7WIg8uDA1UDtdopOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه لیلی فیلیپس پورن استار معروف که تو 24 ساعت با 2 هزار نفر سکس کرده بود!
دوس پسر لیلی: من اصلا از این موضوع ناراحت نیستم، چون اون واقعا زحمت می‌کشه.
مهم اینه که آخر شبا میاد پیش من، و اینکه من بوسیدن رو براش ممنوع کردم، اگه با بقیه سکس کنه مشکلی نداره، ولی فقط باید منو بوس کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69354" target="_blank">📅 13:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69353">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26851041.mp4?token=fQ9UE_fYDPO0Ya5y5blsLtyyj0Mc_n18NsxfmtXA0DQvJcMheW2PxTxNc_Q_mFbEZda_w6J8WjfjxP6DxGxuEvk51iuBrz328i-CdIetd95RvRYFNiCXskPicAAoMODcFjzgyB6eJlJO3jmgpZMXX5mheKqNEjo8P_MjcKzq1MgefnxHVIIixTZ9GOY9Xgy2HuOlFu7Fi7ERScwdJbvkkDnRLFxec0fmMOh_lFoNl2fu2reiduBEdopHVcS-A3GIPazjlveoiczdRFV8rLX8yiIhmzZCqylb4RyI0VPabO8eLCrADkdtWtvdgPX3d78JNMGcVbzo5hhYNaqFuEX6Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26851041.mp4?token=fQ9UE_fYDPO0Ya5y5blsLtyyj0Mc_n18NsxfmtXA0DQvJcMheW2PxTxNc_Q_mFbEZda_w6J8WjfjxP6DxGxuEvk51iuBrz328i-CdIetd95RvRYFNiCXskPicAAoMODcFjzgyB6eJlJO3jmgpZMXX5mheKqNEjo8P_MjcKzq1MgefnxHVIIixTZ9GOY9Xgy2HuOlFu7Fi7ERScwdJbvkkDnRLFxec0fmMOh_lFoNl2fu2reiduBEdopHVcS-A3GIPazjlveoiczdRFV8rLX8yiIhmzZCqylb4RyI0VPabO8eLCrADkdtWtvdgPX3d78JNMGcVbzo5hhYNaqFuEX6Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عوارض خوردن ساندیس زیاد
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69353" target="_blank">📅 12:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69352">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=nth6v9e_o-7ylwUYXfqO-hyyn8zhqBVEW8METXyi_0Sca6leGOaF5J7Uc06hAJqTEjebEeHDWxs0HB7Z7xdNh-aLgg9C-u2XNTCVW7Howknt52DqMedw-uh8S4oh7KmZf34ZqzPs-y3fPrM7UrMLSeXqXn2lh4OYXJJ2R-IodRAIbLzKos5OVO1yYLUqOtmsV1SB2LChOL9gYHO12rkjFre7-gmdnqFX1y5LJR1oKwG0t5oBDJVRea9P408mSWqg19dS3Tz8yqQdO0SeFPUmw5DosqVDmCDGdXflki_rs62MfEdZUUSgLBh_VrDPamGjCKt-6eAM8HUVX-LZ59SDMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=nth6v9e_o-7ylwUYXfqO-hyyn8zhqBVEW8METXyi_0Sca6leGOaF5J7Uc06hAJqTEjebEeHDWxs0HB7Z7xdNh-aLgg9C-u2XNTCVW7Howknt52DqMedw-uh8S4oh7KmZf34ZqzPs-y3fPrM7UrMLSeXqXn2lh4OYXJJ2R-IodRAIbLzKos5OVO1yYLUqOtmsV1SB2LChOL9gYHO12rkjFre7-gmdnqFX1y5LJR1oKwG0t5oBDJVRea9P408mSWqg19dS3Tz8yqQdO0SeFPUmw5DosqVDmCDGdXflki_rs62MfEdZUUSgLBh_VrDPamGjCKt-6eAM8HUVX-LZ59SDMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: میخواستیم خبر شهادت رهبر را ساعت ۸ صبح اعلام کنیم اما تلویزیون‌های خارجی، زودتر اعلام کردند
.
در روز نخست جنگ و تنها یک ساعت پس از بمباران بیت، شهادت رهبر قطعی شده بود.
تا همدیگر را پیدا کنیم و هماهنگ شویم، ساعت ۸ شب شده بود.
قرار شد خبر را فردا ساعت ۸ صبح اعلام کنیم و از مردم بخواهیم به خیابان بیایند. اما تلویزیون‌های خارجی، [ منظور اعلام رسمی ترامپ]  خبر را ساعت ۹ و نیم شب اعلام کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69352" target="_blank">📅 12:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69351">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⏺
سفارت آمریکا در اردن:
از شهروندان آمریکایی مقیم در خاورمیانه درخواست می‌شود که برای ترک در صورت تشدید اوضاع آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69351" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69349">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=b9l6UzDjIXTmaKNuWaJkDDel7Ij43w4BitdXPicZL9SQ541HAVs2j7d_jUuVccuWIRHMaq6Y1zVnHzzqaB3FOyXCgOCbZ98OUHjgXJqKj432kQCd70JXKznQE9zTidyDjMwmvuuresYXXmJWNHYtVXLkU-H5LqkplYpgbvhjIv7Ixjo3-ca34x6ltc0ypC0cFCg7Tr7oNMDsa_75pAsX62wYR_wvVKkc1dXySnuSs05Uo3NzCBzD0FtyX1LPfQRjKy9JQ-diwdg4OJ5H6uavRCT8fgq2uiEM-E6uYbZS78gaCS4p7Y61oMH5v5owRtpQ2Uh4o_t6lvbcJoamu52QWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=b9l6UzDjIXTmaKNuWaJkDDel7Ij43w4BitdXPicZL9SQ541HAVs2j7d_jUuVccuWIRHMaq6Y1zVnHzzqaB3FOyXCgOCbZ98OUHjgXJqKj432kQCd70JXKznQE9zTidyDjMwmvuuresYXXmJWNHYtVXLkU-H5LqkplYpgbvhjIv7Ixjo3-ca34x6ltc0ypC0cFCg7Tr7oNMDsa_75pAsX62wYR_wvVKkc1dXySnuSs05Uo3NzCBzD0FtyX1LPfQRjKy9JQ-diwdg4OJ5H6uavRCT8fgq2uiEM-E6uYbZS78gaCS4p7Y61oMH5v5owRtpQ2Uh4o_t6lvbcJoamu52QWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک انفجار بسیار بزرگ در یک انبار مهمات در شهر خملنیتسکی، واقع در غرب اوکراین، رخ داده است که پس از آن، انفجارهای ثانویه گسترده‌ای نیز به وقوع پیوسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69349" target="_blank">📅 11:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69348">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=D9PD5bK4jVY_8Zp9bSaW7hy0_wO8FFHDbuasgH-Ic___dbZp-QbaZq8TpASNmmoNjZm96mx1xuDoec-oKDOhTezD5dYbI1oRbP9fsU_XR11WyneHxegB-1fOwZ0f-ormUlZ79lXlPsdfYlJE0pfeQBDqEUDlENgKH7WW8ET1YojwqhtKvWL-SxY4O8-7yncHcYxZHH8JoR_3hSUFJklkMX8q-lKwQuMxNtOG-3Wzt4eYI68wmGJpuhHpwCapSD6S_r7N20mqA23H6PUsx8sPfKyydvJDxEvy9dpj6TCwa3rEXL8yqF6CPtIXuQDn3ExMdBAZKTJrlVDmqgwIYEAenQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=D9PD5bK4jVY_8Zp9bSaW7hy0_wO8FFHDbuasgH-Ic___dbZp-QbaZq8TpASNmmoNjZm96mx1xuDoec-oKDOhTezD5dYbI1oRbP9fsU_XR11WyneHxegB-1fOwZ0f-ormUlZ79lXlPsdfYlJE0pfeQBDqEUDlENgKH7WW8ET1YojwqhtKvWL-SxY4O8-7yncHcYxZHH8JoR_3hSUFJklkMX8q-lKwQuMxNtOG-3Wzt4eYI68wmGJpuhHpwCapSD6S_r7N20mqA23H6PUsx8sPfKyydvJDxEvy9dpj6TCwa3rEXL8yqF6CPtIXuQDn3ExMdBAZKTJrlVDmqgwIYEAenQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
آمریکا و اسرائیل برای شدیدترین بمباران در روزهای شنبه و یکشنبه آماده شدن و ترامپ دستور حمله رو صادر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69348" target="_blank">📅 11:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69347">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX5UR-GAzrQYoo2q7mN5wM2J5HGMtK4EWGV1EVD7SLW5ZecKzfD-03z5Fo3iSyBOV87sqPwrKT6ZiveDCDglQjmSqtep41Va-5xlNR7vD-DGZpDvAxTh3L2h5GiWstmoXJhxKBCtg5Y9RYPf4pE4sM-n68PW7VwgtL7Owkevrt5DFLO8W8CNvKCkbxvbTieTf8M7-B7Rmddq0twQj2V_eziIsU2IyW_oDpHL8Vk54qEzQz2sG4xkkZ1evrv1d66AwD708jTKiu1xMDbyP7s46MQ9GrIShTJJw135SQEzy4h2H6NjneK_zirJHKSbzqAw2TomHm5bJ3DVAgNsMX7aBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دقایقی قبل یک کشتی در نزدیکی خصب عمان مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69347" target="_blank">📅 10:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69344">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=MFc7v9VWT-RCteB-sWgoRu5fpDUPhWkKt_HzPELTn7oIAPaQrdHTSVcW1c7IQ1jSfJN7ISccLNE-vNu9nVysyi_H_0OHmBAxEQYFRUHp3tqHw4r1mWXepPqrcRhPnAUNG2Us7y88XcEAl7y2UsbstkPP_cnE78yXdFD-SrMztgxWH5wT52WP9bBqlv9e-QoSkJYVuHy6G6cv0Ty21M1CTSZ53AKby1WCNtCgD59fZVdRNrbYk5UuVsKsIJ4kyB6qdNdoFXGGRA4qsqvJnRabiG1dPtW7dyA0OuWl_b3r6gwm7HSV_enHkkVU2RdLNTvv3M7Bx3DmUFH8AhQs06BMPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=MFc7v9VWT-RCteB-sWgoRu5fpDUPhWkKt_HzPELTn7oIAPaQrdHTSVcW1c7IQ1jSfJN7ISccLNE-vNu9nVysyi_H_0OHmBAxEQYFRUHp3tqHw4r1mWXepPqrcRhPnAUNG2Us7y88XcEAl7y2UsbstkPP_cnE78yXdFD-SrMztgxWH5wT52WP9bBqlv9e-QoSkJYVuHy6G6cv0Ty21M1CTSZ53AKby1WCNtCgD59fZVdRNrbYk5UuVsKsIJ4kyB6qdNdoFXGGRA4qsqvJnRabiG1dPtW7dyA0OuWl_b3r6gwm7HSV_enHkkVU2RdLNTvv3M7Bx3DmUFH8AhQs06BMPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
بروزرسانی از اسپانیا:
نزدیک ۵۰ هزار نفر از مراکش و الجزایر فرار کردن و غیرقانونی ریختن اسپانیا!
برای کنترل این مهاجرای غیرقانونی پلیس فرستادن که پلیس هم کتک زدن.
این مهاجرا ریختن توی فروشگاه‌ها دارن غارت میکنن، از مردم دزدی میکنن و...
مثلا از یه مراکشی رندوم میپرسن چرا اومدی؟ میگه توی مراکش رفیقمو به قتل رسوندم، مردم هم باهام بد رفتار میکردن، منم فرار کردم اومدم اسپانیا.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69344" target="_blank">📅 10:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69343">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=FBBiO3AOxC6So7uR_9TU7CeJ3xbwOSUU4xisvjgxvZ9yjq6EBnbGsv19G6ieJLRRpKryv405lZ_Y4OYEsRqxhjQ84s0manU0cvKjisRIJ_v5gp__dURZWqtMTij1d2AkndEsz-toS4CE3eWx6yJT22l6FYiGBzWSEeRUGqNfnB13CY1N1fnQE48HwCnyy7dcVUCvi7tgnGT1rgLXJgXhQ9Vlsbk7aj3VZhwbdBPViFaBx4VvHwNRUEeBbqHANcbHcLJomZO83_EGO2oFpUSMxNXbVr73_I9-KCGl_J4AhSy8u-TLtlPizNo1zFCa-NdHhYJCZ8jWTpiSQ-J9kwfJDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=FBBiO3AOxC6So7uR_9TU7CeJ3xbwOSUU4xisvjgxvZ9yjq6EBnbGsv19G6ieJLRRpKryv405lZ_Y4OYEsRqxhjQ84s0manU0cvKjisRIJ_v5gp__dURZWqtMTij1d2AkndEsz-toS4CE3eWx6yJT22l6FYiGBzWSEeRUGqNfnB13CY1N1fnQE48HwCnyy7dcVUCvi7tgnGT1rgLXJgXhQ9Vlsbk7aj3VZhwbdBPViFaBx4VvHwNRUEeBbqHANcbHcLJomZO83_EGO2oFpUSMxNXbVr73_I9-KCGl_J4AhSy8u-TLtlPizNo1zFCa-NdHhYJCZ8jWTpiSQ-J9kwfJDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
صحبت‌های عادل فردوسی‌پور درباره ماجرای دست‌بوسی عباس صالحی :
تو عُمرم دستِ مسئولی رو نبوسیدم!
عباس صالحی وارد مسجد شد و کاملاً اتفاقی روی صندلی کنار من نشست. به شوخی بهش گفتم اگه یه روزی فیلتر 360 برداشته بشه، همه این نشستن شما کنار من رو ربط میدن به رفع فیلتر!
همون موقع که داشتیم دست می‌دادیم و روی صندلی جا‌به‌جا می‌شدیم، شب دیدم یه ویدیو وایرال شده و با یه تیتر زشت نوشتن که من دست عباس صالحی رو بوسیدم.
اگه قرار بود دست‌بوس باشم که الان برنامه 90 رو داشتم و 360 رو هم فیلتر نمی‌کردن.
چطور ممکنه من برم تو اون مسجد، بین اون همه آدم، بیام دست عباس صالحی رو ببوسم و برای خودم حاشیه درست کنم؟
من همین چند روز پیش هم گفتم؛ بله‌قربان‌گو نبودم، نیستم و نخواهم بود!
همیشه روی اصول خودم ایستادم و سعی کردم کنار مردم باشم. واقعاً این حجم از هجمه‌ای که به من وارد میشه حیرت‌آوره.
من عاشق کارمم و اینو خودشون هم می‌دونن، ولی نه به هر قیمتی. اگه شرایطش فراهم باشه، تو فوتبال 360 به کارم ادامه میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69343" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69342">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=pljAUUK2eg9kGVM16BidYjXhV1Yyxqn374Y64IYQVzYryPusJYQF58UeSub__-vgmVCG8KyXQ--2dc5oDlo22qOAiNgbqORZU2tuxAd5yOX-F7rzfLqbsOS1QQX60TMqORgd2P0kvWN3vLdmvZYLkFLOP1nlHPQU38ZT9_0UAyNKOO8nDQcRKGtruzK8sw0iNjZb8kIzKhU7aT1OyK21hTSK6MSS-R81Eu-oHqiXUipzhsKyNJSS_pVULCUuO6kZbsGF39Yr4bITuwd9SF52ZCiwV99R_v4IOijW8XiadHNLkci0eqxJVHdgVRmsNG8ohlafxfCjm5natC6cfvXTDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=pljAUUK2eg9kGVM16BidYjXhV1Yyxqn374Y64IYQVzYryPusJYQF58UeSub__-vgmVCG8KyXQ--2dc5oDlo22qOAiNgbqORZU2tuxAd5yOX-F7rzfLqbsOS1QQX60TMqORgd2P0kvWN3vLdmvZYLkFLOP1nlHPQU38ZT9_0UAyNKOO8nDQcRKGtruzK8sw0iNjZb8kIzKhU7aT1OyK21hTSK6MSS-R81Eu-oHqiXUipzhsKyNJSS_pVULCUuO6kZbsGF39Yr4bITuwd9SF52ZCiwV99R_v4IOijW8XiadHNLkci0eqxJVHdgVRmsNG8ohlafxfCjm5natC6cfvXTDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سیدمحمود نبویان، نماینده مردم تهران، درباره شاهنشاه آریامهر؛
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69342" target="_blank">📅 09:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69341">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69341" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69340">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=l4D1FwxaMejXh9_UUsuNnnawWEHFKO1pqiEOaP99Ex1dxw5QRShnTHHzRD3E6D4OuSr5D2iMATLc3dr7gzduNx1wLYrUZEdh2zeAEDE9tdP0imG-OXgiXgrSNAq-IAxLfampv9Lxughn2sB2vIundY1lHGs2zx5pdV-Rl8zZPLZic9U3KSbzz4021qEhnS_H4mv2R8nULy7A3ayIeyM28n0IbZYHkZeM_IwFpN2ThbHfkNgpo_7LnkdvmaaUQ3Tosncy-n7wGkmnpqsDAEbGvt3hmb1qJZaXWi8w48BKCIwcE1qfGESeiW9NQ-iuL5Z53ueQYqVCdT8rY_1mqYoy8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=l4D1FwxaMejXh9_UUsuNnnawWEHFKO1pqiEOaP99Ex1dxw5QRShnTHHzRD3E6D4OuSr5D2iMATLc3dr7gzduNx1wLYrUZEdh2zeAEDE9tdP0imG-OXgiXgrSNAq-IAxLfampv9Lxughn2sB2vIundY1lHGs2zx5pdV-Rl8zZPLZic9U3KSbzz4021qEhnS_H4mv2R8nULy7A3ayIeyM28n0IbZYHkZeM_IwFpN2ThbHfkNgpo_7LnkdvmaaUQ3Tosncy-n7wGkmnpqsDAEbGvt3hmb1qJZaXWi8w48BKCIwcE1qfGESeiW9NQ-iuL5Z53ueQYqVCdT8rY_1mqYoy8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69340" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69339">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس لیست اهداف انرژی منطقه رو منتشر کرد:مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی؛
❌
میدان نفتی غوار در عربستان
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
❌
تأسیسات ابقیق و خریص عربستان
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
❌
پالایشگاه الرویس و میدان نفتی زاکوم در امارت
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
❌
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
❌
میدان نفتی برقان کویت
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
❌
پالایشگاه ستره و تأسیسات المعامیر بحرین
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
❌
میدان‌های گازی لویاتان و تامار اسرائیل
ویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69339" target="_blank">📅 02:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69338">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ1S3tovUn4xcZDdGYpDmBR7gip90B4ghqchk5BxBo4MljA6UeIDtg10EBVvuCSwv65aZtY8uOFxreyFsSypWc0Edr9_rFgJiBYfkxA3tFCzEhOUXuBvyJ3lT5ODgust6g4kTdXGLIhHEZZFJTWVzcXpJmXdS-Bh0W2WRmAAFAitmcNK0JuLVQQnLVAW_dQ8Ay6Bt-X6G43AiiJh22zprjCHmSSVL41DR626UrsRp502ngip82Vd4maCtnXL07se9Vzqe9eVnbVWevVLxwmesA_AFuhDZ6QT7Gpa_cN_BE3mqV8ALdLpphnH_Eb42dnUbkxjrRp4z2_Rf3pTedw6eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:یه مقام ارشد امنیتی به ما‌گفته؛اگه آمریکا یا اسرائیل بخوان به زیرساخت‌های ایران حمله کنن؛
ایران از قبل یه برنامه گسترده برای جواب دادن آماده کرده.
به گفته این مقام، توی این برنامه، زیرساخت‌های حیاتی اسرائیل و تأسیسات انرژی آمریکا تو منطقه هم جزو اهداف در نظر گرفته شدن.
نیروهای مسلح ایران توی جنگ 40 روزه و اتفاقات هفته‌های اخیر نشون دادن هم توان انجام چنین عملیاتی رو دارن و هم برای انجامش اراده لازم رو.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69338" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69337">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9hj_DpQrjT4SsoPwth-nFS3R9uPzNAVMh_AiDwEv5IR0fMQkWqI_XrUTv-A8Fjt_I5E3LKIta8dRZCtyJ-Ux-dFbfST0HYCQHMYPke6Cl7ByL-WLdt7jcSgGTDZ3qeoE_Th-P157m549Mp-cvQdxiq11-mdrf0lTBJLDcTg6thB-S9TYcb5zBxzWRpDKKk2GdO20iKfhOpT_DK2xhPiB9GF-V8LnvytLmYawiscCFcqPKaDGbLRboyQqwfR6uqov8nbySjGog1Z_c4OtV90TouGO-TMA8yNLw7XnYxaCB4D6t5jMBCio_oQyXAXcgfJSgd9KSn9HpVHmZV8TAX_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛آکسیوس:ترامپ در حال بررسی حمله به تأسیسات انرژی ایران ظرف چند روز آینده است.
یک مقام آمریکایی روز جمعه به «اکسیوس» گفت که رئیس‌جمهور ترامپ به‌طور جدی در حال بررسی انجام حملاتی علیه تأسیسات انرژی ایران در چند روز آینده است، اما هنوز دستور نهایی برای اجرای آن را صادر نکرده است.
این حملات همچنین ممکن است برای نخستین بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدید تنشی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین بار درباره حملات احتمالی گزارش دادند.
ترامپ در آغاز جلسه روز جمعه کابینه، با اشاره به حمله احتمالی گفت: «خب، ما ضربات بسیار سختی به آن‌ها وارد خواهیم کرد و می‌دانید، بالاخره زمانی فرا می‌رسد که آن‌ها خواهند گفت دیگر تاب و تحملش را نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69337" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
