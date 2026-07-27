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
<img src="https://cdn4.telesco.pe/file/ndtSLrz1COmALWAWEzqQRhSu4IPiVLMHp8zBgunBsh2FfAhH4YdIx5Fw2wUZr4JWQdw_zFXm_Ypvv-VbTmoczi-9PwEQoJ-2j43sk-tdvKdzdA6ysEkDDt8QJR7G9GGJt8DnjpyGHXrDbeWrV5eDEx0SeChFqg6_a9b55KyndRg3TyLYbubHfINyIlrkpzmvKu680ssIWZnumsCbasDiYBw2C2PVhGAz6tQ4mEUZd-dVATMe2WKoaTNEENsNwmojsCSgg9ixByxOBDKzNXZJOvCQEf3078KsjCfF2wEoe_qj9uRMQSLFzVfJd2GoBZX2M6BX-tl7K2WDZf7FENsFkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 601K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 15:42:25</div>
<hr>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6C032dX3A0m8V2t0N0P5ar5YJwkR8pjwYMXH3TADPq_KmuDWKYwWZbEwJK3zhSPGdahwJyTMMAQd5aNFgVfzcj9Ylo9HnvwnEWwdVaUSNap2JHE-UfkSIJGeHZXr-JhYsLLWc-0n6EvJCtovFnFvCWeUap78RWfZy18qChEnACEZjn8Ddi8YucRutN-E_HkJT-hs2oieGV2tZW0PocFqpQ8UTxpByaMJxyj3LRMpk4T79Si32aZmuRlpdLzP8jkm2i7rOff-A4lPQdGUrd45ojN2wYkyZiQPL3ryrmVHrP5HNNKOQo2we3IHazlaug2nQbLPY1Aa79lTkbHuHwTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr5EDdSDYeyp5EC80AZoqMCsmjVwNcgPvkt6QH4tKi7By1FSpTsE9PyfDUOPQKWZbX0hyXewYhYD57W5Y4rXPyEjTULY3uKg-gc2PkXijHjTq8GWMxEqfEvjYHMggxP1QDSBY3K0rn9U9Yo5jDm4NxUZGMl0-JCaX0soN5hYE0FZiZ64MB9vA6LajzFedplyJbdGmHfTbv-J0Qt0PW5EzoCcH9RuknE7D04q8eq7_X0MeD_3ukShVVE7JNW6zzSQvS84hIk8Nbjn5POEm1JeTP_ElpsLanKFmW0tJubh6uJGMdTTnQlFF5O9XGdCJOp0ZQSac0Lx730oJtUm4F_-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7ORqeEggHrIJXkj-0TWGRl23g_CKcjx2nXuFHA0v_4e01Q3racpbrxaEEkjhOuG-sOUk9VzbmvEXPWvVall66JRKZc8Zzx_bqRxMlfSOudZZp3mIqHK1e5bgG9RLuaR67LQ47n7vPIUeA12MYmdYZhMdJruB6xjscaoGd2N02KkyBVGmXyFwXrsymnJupJwm9zMLI02_LaII_j-fF-0EF3GdX8ucrD49wXdENZ5aTXNvYYxWEtaqnx5hbncKtOQmx_G2ptEpXJrFF5TrO8NkwbhSgpcCiKZefhqyUl9PznojkmN8R0hiJPc0syrqZg-j7TB8miz0mDm3OC_p9VfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcJWwgR8EJolmuAlDRWREtAk3BK_mRhyUTzMTgFdkThE9_gKngU43qBHMKrj-0zyjyWd6ftCLlJX3aHWIVHf5-DbVAC4YzZThgDpu2yQI_psHXQjlRd6CmpwEC8HFfZvvuCmCqCskBGFniyUvTTtjpAcugJPyZXpR9X9azl7wzuAa8s0qdtA7voy-ch7huM-Oalwi7KoNgmB60rp9rmu1pGik4N6bK_PiyK5TPYIQF3CkxnfNf9D5ExrYgeL8icWF_rxhbeagDchPrnQw5l44iLvTjQnY6vXFHenPVRyqao0ca8Ug9jXx4O-ORdoIUjuOtB-Nk9kB7rHhYJc-grItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=k6KpkebIVSnwAeeQdgwaUZCoki6GSJ1a-KZbaSUJfhcwOr1vv1mYBo6eH8WTP_EQLRPAZVbcvYOWZwBix10lVpWwnP1fCtUeKxmg7xsvY2-4W26HqyT2Dc2yIffHnecAZm05h2-1zfzV3eW8JQ3n2Af-HSJlebmWuH_zb6lyG2u0dO6qqy2fBait2k28F7X2-jeLoK-3ZBzvfxJoUOXm0fLXQSIrI82d8omyMyaiOwyV5hMJ79Ns6zTdx1LEWCK02Tetfz3yYUohBxWje0rtfIYXMRe7oxHozdR9N9FI-U5s1TDMn0mP-RFAUpvNerzvlit7bpy3fkY9jW5o2Brr4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=k6KpkebIVSnwAeeQdgwaUZCoki6GSJ1a-KZbaSUJfhcwOr1vv1mYBo6eH8WTP_EQLRPAZVbcvYOWZwBix10lVpWwnP1fCtUeKxmg7xsvY2-4W26HqyT2Dc2yIffHnecAZm05h2-1zfzV3eW8JQ3n2Af-HSJlebmWuH_zb6lyG2u0dO6qqy2fBait2k28F7X2-jeLoK-3ZBzvfxJoUOXm0fLXQSIrI82d8omyMyaiOwyV5hMJ79Ns6zTdx1LEWCK02Tetfz3yYUohBxWje0rtfIYXMRe7oxHozdR9N9FI-U5s1TDMn0mP-RFAUpvNerzvlit7bpy3fkY9jW5o2Brr4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esrgE2-IfiZhg-XvHPQbyBqfbQwRVrffh6PgP2k1eOekn6D770b8jtRzxZW_VUZsxMHuhEMCw3lxq3PNQXlonDYyesfzeAdJhk-rjyTTmC7le5adBDqubVRfDU35f90SRX6cBGEOY2WWb6boWlao3LhN009AXh-XfmB4PbhcwdnCDEasUQSEPA2szCLcgJxgnIjVN2NLKOT3vNfbPXLHz0gUmB_XzhwIMao7BOGy9jjd5gf7nO51PBH_gEEDoR9nVgEsEt4nC6wa-PS6pvvbFhDpvTpkGQHAdCst4Q5XW26wtuPs0WadTjpqBb8L1ij4LdCbLDjVsbHkYijJv2OOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26607">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwkTNWfCjXt2ccv_AAkJUhF963HyogEzS-Gh6aKoPtc8b9S_19SoBa7xgYGFFItBk5qXMzGbMH3xJnZhB73VV4Q4s6qoRwijYqtt-HRy91W-023jliBCu7XS1bVcUedWexKYeqQRZ9RZKz8r1emLX-7fbQi7gfV0_SUC7Ad_JKDfhqVnXOcZ8Q00qcpNbI-k7vvw5B4J6t1jjlCDpH3eFp_Kh-U5dUcbhfALsIXO-YGGCFOhbnZlfvFou2N1_TTuUnGqd6KGD1IxVrmVet-YTNrmiBFH4QzkKaqu_VGv5GuiQ-oWF0M1RoASRcyljtYfRM47w6PTp2TPL9qalO_03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه لیگ‌ های آسیایی از نگاه Opta Power Rankings؛لیگ‌برتر جام خلیج فارس ایران در رتبه پنجم قاره آسیا و 61 ام جهان قرار گرفت.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/26607" target="_blank">📅 14:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26606">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmG6wYVxSR2htEfFgNP8cxVYLAcAaj4yu-JuG0qrQe4xdTAhzPMgGh7MNCyFGRM9A4NR8pJeuVKKTKV2RTksdX9vcY6JJKcen6g-XKwCCO5e-G97pSfRye_c_NBgDBv2-E_Bw4pccOBuvo5v-mbEwID6UGcMe0t6--PjyhYSIonhQbk_TZftVKVHpDPEj5ySlmywj2-BqHKYy_L1dJ02a-awNEpvRAWe1wy71EyxUcBo2GbWgVA20eVxub4Re33MazgFTql4q374IEANa149TMKcykwgLMufk9mECoonhdfoJ6bdNCpV0Kxh3l88F3RIXJd9ehSRP-SnYXIZRz_9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه نساجی مازندران با هومن ربیع زاده مدافع‌میانی 27 ساله‌تیم شمس‌آذر به توافق رسیده و این بازیکن‌جانشین دانیال ایری در این‌تیم خواهد شد. جالبه‌بدونید که ربیع زاده با اینکه مدافع آخره پارسال در لیگ برتر شش گل زده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/26606" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26605">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4u3hrE-OMlRXPWZSYScVWsgO07VkLeZ6UpKUau2NVDZIXNKo8Jtvij8kjmciRnj0UWwSzSGORgxaKT6e2s8bV2rhX_tr_FtvgvOEXyJA0ZIIwF9P8eIc94LdCxyglIOpftjrz2Um9srG0a87Hppc2Sr2inYFf-ftwOwFTRpegVcZRqIQOe-CBC6pUSVe2kdQJkUG-Mw2AFLLd5hv5oyBuW_IDLsXDNxVCWcKnNWdgri3DcUTOaSI6SRRuAluCJoRanshxAjU6Il1qYSAq8kNpa-IwLGD3TEk6yHd4kowW1a9aSpKBXOl3gORO8SqQsWmmS6mXt9xu4ajVzSN5ULvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟠
فوتبال ایران فوق العاده‌ست
؛ داوود نوشی صوفیانی پری روز رفت باشگاه مس شهر بانک پیش پرداختی گرفت و رونمایی شد. دیشب پول رو پس داد و امروز با ذوب آهن اصفهان تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/26605" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26604">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op0_QB1M1MW-jYAnNwRtWFdZ3NrVU8vtd8-Hv4Yx2utANCNjlS8_bNVwcL_5cSpItwPYMsCwUAwpbLFPekN1zRWciQbz2IEwYK2sVO71Vz5IFurcN14njASgGipfqNOmRGLkbUYK06jT2JA-3B7WQh1OVQM21uNFXtIpc9WxItkCz67Hp-S5HdkjVeq-6M9Hl7Qb6oMkmi9bOhjapIcQyKG9JZ4TSRPzns_REIG6LaFoP_BfYyd7nhJ1I7S-mVmyFoBKNOnn85DnCNZPmXKaMOPQghwPvsfkXogtNokjJSnCecTAq7r9_4Qj6Eaov8IeRd_V7o0gIti9AQwvqz7UnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/26604" target="_blank">📅 13:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26603">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=AWR_JtvEP6iJiQwlGjxapojcyjVSUGQYK2CssDkQx72pLMIjC79GAEk-I1jKqItawZfJhe0JyMmNOiexP6Ww_By4oGrKVAHk23JcdvT9ezpRt2XLprvUw2IwmDDgRjRLxnaA0qKWcIvLynTB47zcFw3oTiVhLHdqDcfl8HoZeQgdsi0vSQZjopoSc0yc540i3azeViCO2IH-vmecxvJFN4xnOJ7ltq18WImRPgESIaPXzair3K6dgwStgVhUAEQSZQ8pJcVrldtlUtzwFBgMSJhoA8ZvDy96pzq7Ilbrj-lsmpHseQVLv-QOo_y7HUUnHYmoYurrXn5vXpUOFGTa3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=AWR_JtvEP6iJiQwlGjxapojcyjVSUGQYK2CssDkQx72pLMIjC79GAEk-I1jKqItawZfJhe0JyMmNOiexP6Ww_By4oGrKVAHk23JcdvT9ezpRt2XLprvUw2IwmDDgRjRLxnaA0qKWcIvLynTB47zcFw3oTiVhLHdqDcfl8HoZeQgdsi0vSQZjopoSc0yc540i3azeViCO2IH-vmecxvJFN4xnOJ7ltq18WImRPgESIaPXzair3K6dgwStgVhUAEQSZQ8pJcVrldtlUtzwFBgMSJhoA8ZvDy96pzq7Ilbrj-lsmpHseQVLv-QOo_y7HUUnHYmoYurrXn5vXpUOFGTa3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/26603" target="_blank">📅 12:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26602">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhL7amLJ1lvI_1mzGBDcvHwVF-L_CigGowdnKXA2iB8k7-yj8NK8OB5bgsS7gjfFvZy1eTSXg1l0blAw7k1zftrQd47_QzB4t_DoyCL-snH5APMxFxdBoaF_zr0kZnMwYO7W2hHnQyijlEqQkVEe4xaYBS9a6H6i58x7lZRvgKhOQ23J1K9r3PU_IK3wny8aJMpkohlHg0QJsLBiDlELwH2pBGqHgvx3qQT3XrSL_ZYgXPY9EVtuEASKpKzGvkIhjbXkKSRc2-qGk_EPxvk5e4YctDfkRXpZK3iLixqzoXrAx5367j_mzAerNj8NdKJWR3dQijGybrYc9PDXsJG16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/26602" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26601">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfWbxd5Jpjy4cXY3Jl5rEc8siEmeYnwGLWL4GdbophzwNVtCKUybhhGv963IhhtiE5oTWm8Jmt6aMAu_xxGsjQH9dx6JTAEel4sLgJWKjn9tKprL1mAHyvS0Fy-YWkfgj6AYHChAg8XV-6ADaBeOa4Dg9ddNVa9I2wLY2MA8hje-4GBjiZPM58oT24KxQ8EOXXm-cm7aHTOD-XdEBeO58ns3DoJjw7_D5QdsxU9KteRHC_5TeVSsFWc2Mmn-Z9SmKDZc3nyAdtY_6Ydqv3EFhVPPSy_fv2qoM1xd9B2N-7XPje6vfGfnCSqtDjoQpabFrpfauU6Eppmet-aVooh9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/26601" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26600">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1jfor7dh7YiENEq4GfCZbtvIjv8EHFH8EWCX57uWHDigRD7pJBHiY2guy7EvO95cY5HqAp4mm5btL1Z-cyOrSDN52jQK_8m3Gao_P2K7w_eK2YJEZjaC00ITOcGbW2wXFoydVx3vfyQgsuj8XclO9GCFzsylmuagZelBWBp8liFOErz_Kxt3rkeqcnC2I7cnkrtUjdYGMjrxRVk3UG_0TkJaAnF3d7tStApQWtHAiEhWxqTti3U1e2gcQwaUXJUJU0I2CiNLapzNIwsn4D4CpWZQfUHkAD1YUOibyA9Wuhn8cctnmqDCtiD2rJnCmOix7d_ITt9Y7J6m16dUvZkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس جمهور چک در اقدامی جالب و در حمایت ازتمام عکاسان به عکاسی مسابقات فرمول یک رفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26600" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26599">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLJq2QsWI-7ASYu3QAifBVtfc_W6gc1ArF4C6trmOtYIGjSvxmBqBE0sUFGmqPfJXT9RJZaFX2WsoYoQmN0zPrHvQnwcssGSnBPYYhGcp_4526uUt3WxYWXac1KjQNXZxzEn6ifBksc5wN4Ky7OtExEo7uhhVZ-AfcjCLomnz8q1hJ76Pv8DY1bRnoSojqtrfk7h2G5ZekoU8oZzdT5bbyFo-TO6mdq10GFyQBbba2kQaZka_NGIbRU5lwuupihCa5eIYf_oS2Om-6M3qA4YyeY37T8rtoVP_GHhUNqpw5dIykugeh3BU6JT-j_NmmHCkBhA7S8SyB7KLk9hAHjrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/26599" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26598">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLXHisLts73Dc6cMQnrOpMqb6yUQ1Y16A8NHWfmx3b6g4kziikAlE8mzYNTtck721SGuZjFndLb3GWemhD9OTiEWpILJ2WtT2YYMdNWamc91cq-wFmY_7YYVJZ426kf2cfs5-XI1F3NcbtIJF9wF5SZ7caYCf72LCn2K_4TK2phh24tGNAvkgJsYOmIZeaBkG0feFafYysK_cZ0fu4Np_cCl9chMcDJwL-zjaGgZNp10u6MwCjAkjj9Hb4niwioeEfUNUPUz2z0hwuyZEuELHGt-j0LQblgSWDGb_6BRQK9qzjJTAt7SPJXee_-0fGmkINaq06RytG6_rC2CvuVzJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/26598" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26597">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE4c4mrzs_9Z2tUD32ogxI5Oe_F9sRVks_63tYzjXparFi531hBA7f_EelRyRBpD-G3CWNdTJ_Kko5NgLOBaOoMgneiL5wRQt2l_fqwDXZ8lRZF6hAPcOLDgBRRQSQNRUOhS2xmL8B7pJ_y4jHsI2tw_7Du3TiRPgF_JgXU5bZqt6ICmfNFJHvqJp4iaEMMy0aeVjdgEhhSyy0-yJb7Dy-w6feeR8D5TYY_AgRRqJ2OuQQvCr2fjtGNI3S_tZkKOx9oYuLyK7mhx6HcxfkWOTQ__35z4gHZnuhoyp5-kF9xCEPlHtNBTRLjbVV1GJ75j-mpauBiu2aL1PqylGE_rYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه‌گاتزتامدعی‌شده که آندره‌آ پیرلو درگیر یک پرونده شرط‌بندی درروسیه‌شده و به احتمال فراوان فدراسیون فوتبال ایتالیا قید توافق با او رو میزنه و روبرتو مانچینی پرافتخار سرمربی آتزوزی میشود.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/26597" target="_blank">📅 12:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26596">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=WH2Y8TC87HDJ1B3-Z2jxLbwGG_eRuqPc07AlIVNtAQXliYfBzweYVm2AUXUzMfi0tecMvIiamSjwrrrjU7Rl8vTVqqi2gAIEpw589ukyQBc6jETRIFTWveLDlPrjMnm8p61pODxEjvfhItlgPM8q7QSBzoNaD93CmfuvnIwb8jaQK_5_aFrpCDszS1xqwik_XPKdta4sVG1elTjfTFPlQdzJSPhawIr-aPyZUMc2c2_Ih1vl4nKC_7fAsb9TS0V6-wv-TB3F9bZhp3BSGvzU_pQCCkUke557t1UQCIBDWRm9RJ9KKYr8L6wgvbrsMDbgQzdpHIvA3ssolSeCrFwzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=WH2Y8TC87HDJ1B3-Z2jxLbwGG_eRuqPc07AlIVNtAQXliYfBzweYVm2AUXUzMfi0tecMvIiamSjwrrrjU7Rl8vTVqqi2gAIEpw589ukyQBc6jETRIFTWveLDlPrjMnm8p61pODxEjvfhItlgPM8q7QSBzoNaD93CmfuvnIwb8jaQK_5_aFrpCDszS1xqwik_XPKdta4sVG1elTjfTFPlQdzJSPhawIr-aPyZUMc2c2_Ih1vl4nKC_7fAsb9TS0V6-wv-TB3F9bZhp3BSGvzU_pQCCkUke557t1UQCIBDWRm9RJ9KKYr8L6wgvbrsMDbgQzdpHIvA3ssolSeCrFwzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از تمام‌کنندگی محشر لوئیز سوارز فوق ستاره سابق بارسا؛ یکی از بهترین مهاجم‌های تاریخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/26596" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26595">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpUlVK1JRkThEzdcLmr0fZVBxaxria-bNQPo8Pp9ekwYWvrlfTRWj5FyObImCcXOxSsGFFzbjib4knerWEdzpByRzhLnpljVfWvw8bTkiP6v0D2Trg0ReChfdbMxzkexsRtW5TaytH6D1DBxXzRTdDeZwP9ijCVi-EjSmvsza9BDPR3leChiPNKLgih2mQB2JXq4uTyLA4xVECkwxfW7xB5TlD7oTMUXgntW2VJGsM8wKrOr2cBurL1dNPvr_5SJMRJyMPTDyywq_vDf7ZKZBh4dhKKlOamu1_kqHeXONk4JpsJTBLmjRMhkE59uKVfwUZ9BaD7a4RJ8PF3zDja8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رودری اگه به رئال‌مادریدبپیونده؛ احوال‌پرسش با وینیسیوس جونیور در اولین جلسه تمرینی این تیم:
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/26595" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26594">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0k6y_BLrR7a4B3WsePdT3vCMKbNjAZJ7OzzlcxHPj7gHvU6LxxQ4R7zX3FTtdpu0Artw4INBfy5ul-Gg1OEBve6OBUxEAWdgd-5yJ3LToprTT53AGQJ2cPvOkEavAIanXxwCtqtscWPAJ5pkqyU17exUe4OZ5-VdJJObGO3eBbJ28Bsl1L4qHrydmstQL-u_ZOzPUQguPBymqPaBLXHdHhAzrL2f3MBzMCt_qmP-DVB6EEH6VJMH5Qv0fWIo2KWsVKJztApdH4EE4KfJSwdo_GO_mmGJm_cOMetUsWsUIETDWMsSkhurOC6a9j9iGTE9f0VhZe7pU6TGBlLdaznFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26594" target="_blank">📅 10:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26593">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HslJPvibm3HdxE-aX-pjwEp5-PgaM374jFAe8zFSEUBS9cLn-uIQMRtEYjrtIaGCv3CW74T1zHh3D5l8Dt7q0BdVcS8v0Q4E4LNP8ijSJiMopvEHDQa-LzjzBndYqR_D1j49xNI3C4iKz1HeNoMSei5uZdWf9W8UgLVTthckmEIeffHd2Aw_PRjHOtTO6KNnVtPolv_oBitj1lDWDpvTzq_zTyEOgwyImfbV2sEbf8Vh_QJCbSJja9i2ZiIE5oWBAHr-FEgUBRndgaV9urEfwkCyt6Vp4d7g2tbJ3f9rdFcRfgjTKA6kwuVfu5j1qv8YyQI3hvexDmkC7gsI_x49iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/26593" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26592">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAumU0X3rfvjjN2ECsvyBRhvDItrS59ghaYlx7yuP9sdQvFrJn1b7KnsKHSjcpOKQKeWixPnzcjer_BPqiHg6xZwJOJNAcQb2j4UM-EJ7RiEA95Zmxx7zYLOigTvmC8RQqSs2XkwUe4qDRSTrqHVmoeBb9v7tRfGEBG7IaFjY041SaY0VqTSa90a2FIea57JUzN0No3ZlFFKhcQ_QGQxqKVMZRd3InepyO6Q_hp79vQXpv_RpplecuyRTdK1KeyVjlVsK_Tm6cAKidsEuI1iGW8mVIAmr7YAtKwHiP3DrNogJuaTTjWO6OHbPIufpp6__om3rhM1eEEifmLzgUA68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/26592" target="_blank">📅 10:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26591">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOnZTVqLknV5jGI62p0yFY6ID1GlENPFwDgAvoaNX7XWuMuKyqMeDxLJ2hE1XpWWHcLiinOupy5ZkHtsPn2oR9NPXBGRKLCMISMlH9DBbSJTVE0dz-6wu3Gq4kMxgCD7Bih_WPrYVtr13QwNa3auvTPI6uEhXV4Y9ZSf3xZnhgxWds35ERWHBLhw2SX61c58PBOWWcMClc8QgW8TI0aIGbXhcmbl9ydxvC1I3g_TSojL08quxsbgZbI6YgS_6BM12Gsq7oJqdnCXJNOGRGtaSWqjH37JsVzd_MC6gHayckWLk_xeW5ftB8WsqOSX72WGx6jzQ80QxkRj6USB-Dzudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26591" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26590">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2PrcwgLo_WqXnvQQifbZW_q8DNkBps1L6j2vaDGSs8RcXqYryAQxhzxczUVq5JIpBF4GosGw5xpgIo6p4OSneRIn-ezKTOYN51soMeyh2mesMph2_X0As68E3UQOFMVBZyRUzbKqnKYDh4zTrpJLRZ4k-fHETZLBhMViUHbZr5sqI-I5mw4nGld-e92EVb3TSoe5AOEN8a54_Sev6lEpjyUm3CYkQtnim16Ip4_QFHucAK-1Yy1Lw0MB5mF496U3jIcc2hr-NcI2ngjB1_L0BZ3UYgsvRa9PX65TejYqH1FOzfj3y8KhUjcTqzxJwkrTOflZdZ7dWZNh0mJ7zJtrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26590" target="_blank">📅 09:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26589">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXwD3vQJZQAgS4BWc4lmMdzI68eopIKiVDgXFLjFB3UPYIi3yW_KVGmLE-STf8rBc6WB9IxkhzAJgAdHP3ILe5-7gfiXSsk374q0DiS2SciRkI5DXLI6t8ZlBfscNXahbwFmd46l_I23I_ELK4vPCldY_u5L3NKfudQO5YfgdQad9hu6jwjxGju8dB84j1JdonPt50riUKtHb0q0Tczz-wcaGEN2ydScXYlwzkZXQXhG0IfQgONTWj65BUrNa3n-pLEKzuLTOg1TR_QhySCZvqxu-WIHv_JckvB4s1UpTpRwwUY6-XhX-nYoDu3lBQVkCq91iYeetfy-9j1bWmwXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام جوینده در ادامه‌ مصاحبه‌اش گفته که سپهر حیدری تو روابط‌جنسی کم‌کاری کرده و اونجوری که من میخواستم هیچوقت نتونسته من رو ارضا کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26589" target="_blank">📅 09:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26588">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=jnjYl4_iWO_Pio88DSBKVzGey__kfacrxgS7zCsFiF-S4QT8wjhoaage4nQCu4OE7wqBtSDVBdUq7PYdB6e7A5lVdJjWtnApCBnIk4FC-yzpHz1PQmHEhmZ76RAw1ktGjXdQbxiCA__X7B5Hsh6lPqwkGfuC0IDf8V38PiSZse33T_rK8R30op-RNBxfZ7muJjXpg6lw049e-HZO__xus2esgHtRFDUIVpDmvcYI_XkGiaWCgXB9oVCmvw2Xlf0MKg4BOUSrWneZ8Bv3f7kkV4BL5w5QWbI22pgsF4Vz5s-a32f9gf1hYa-QXWE3e8ZlV9qbX-fktX7ccvYAQ21uCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=jnjYl4_iWO_Pio88DSBKVzGey__kfacrxgS7zCsFiF-S4QT8wjhoaage4nQCu4OE7wqBtSDVBdUq7PYdB6e7A5lVdJjWtnApCBnIk4FC-yzpHz1PQmHEhmZ76RAw1ktGjXdQbxiCA__X7B5Hsh6lPqwkGfuC0IDf8V38PiSZse33T_rK8R30op-RNBxfZ7muJjXpg6lw049e-HZO__xus2esgHtRFDUIVpDmvcYI_XkGiaWCgXB9oVCmvw2Xlf0MKg4BOUSrWneZ8Bv3f7kkV4BL5w5QWbI22pgsF4Vz5s-a32f9gf1hYa-QXWE3e8ZlV9qbX-fktX7ccvYAQ21uCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26588" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26587">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbhINxONW0QDKsxETHIG9vDTXECNUORd1eZvK0n8ilNcj-wyEvNMCuZ2TitmrJPU19R3BuVcqtjoCR7cPt4Crk3TpaSmwl821RFpODXu38z-DmdANLd33ZfBt3X6nttKN9-ggEGuTWoeN241ooxt7Dne0XwsrLLXogRNwD6-PkdOz705JzTOKSZ9GCYZOw7E-Iu7LOf_PquXVy1tL5UFPHn_iGyer7PTmnZxydCnj9CXB2YCtcXnCQBmvlITOrJHMmQDxZ4wARr_9_VkMfvuS3i3xgudBAjjMkEKzZjolRkL4DfxNUPLlwe5B6cWnVzZbtNSjoW6otSUqmH0GwmlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جالب عملکرد رامین رضاییان و یکی از مدعیان توپ طلا درکنار کین و دمبله در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26587" target="_blank">📅 09:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26585">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrEEJdHiieobbyY2zlGx9gcMkQghGk3L8dwPV57PuK6QQsGGdoNZdPnJp1dYEJ8bA20mmEfwi0dKoRmPAZ8RdNSzpGbrkgsg-DmuCZ3W9woDNRWTFljLzXXwkzgdOsp9mbPSJN_7gI2WNPdto5EQq0vNaFmTff4IH1ETCro3D55do_WuTlh8dH8cGNikiAZHdNBV9mQ-ix7QGdPFbLmNHUg9JXh66giu8JQBzgch14QG6slz1jUg5Uw1sSnDmGDq-WxWk9KKf7djRppb33p4d7HdF0IeBtLXdYmVk2xwML_gLXY0V3OB9KTq-mmYfZ8BXM8sLqvCVFKkJjbNejbMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yvj9hnfvbkZfJe7ZeYmldBDU4gh3locHB48hittYNnl0xPTkfXEPqUNhmmpb7CEVOhCn2fu0ZsRfltrEWGb4Ajyib0w2FFM-KH8NKVSjQefe1DPwO5NMPPr2oatNbtWlbRjR8VG1J0Vk3a4JipBwPltOJV4R3GeJQAMp0pWd21A2St2NcKQFsazKGP6KS0i2tKfsTthj77Y_v3EalpRMx7YyUbDruWPB1_xltmSDnUVN-ZeukGiAI0drJ6bGH0zmB_zyuFLkYcjIq1LLrSOux7lrj-2Rg-6inkPvVJp7Ei-11lEjRepE7oV1xyGHcE0UXDvqa0-cd0r-_sdTaAHVWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26585" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXvKIhljfF3osiqqcgZp3v0VVuE8wzNqpPdwSz-XSfGqZ5_olnTSbt-q0daps7OGf0Sy0sBNo44CSs3AqL-qEuS5Ud-C6LnoFDGsV9XNywR6_vzQPwBQL0vFkFoTv9USoL32JEv83wzh1KeQLyOIrjvr8RJ2mt_Jv3tgrvLpNlt8xKueLJNQIBrv49Ui5TZ_r6FwFN6U40immTkttV5frbF0BP_-1Pgfh-k7r6wQks6X_I_MwhnppvdQEcejHoIJZekdum1K4I98xOY0wg_YT3YuQBZPP3cccv8FVn5lI4Tr_oNAmb4QFAc1CL6QVJ4MnM9qsdHsr-9Q6B4_y4MuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrrXAnHJHblEESQTSOK3c65o5dDzR0jDEZw2VYh4BSvig8uXxHxENc8VltWEtl78l-FOWLwPpfYD3vKo90TF9hU38uKlfbY-wMeGQjkSJUGXyd6Awhu_7DufTAeXtOXFmXTvlhZQhVTjFHieK_id0Z57pax7Gz0pgl2dx_oX-rMUUpfEE3NdIS9QFROrr4Y0TU8eyVyFbfeFdwBFtxL9ddC7zLaWrn254VDNmGgCBnHcfBmsYVFYTP1nT_gg0c_SMwli1Iumn3sa7kDCgLtZ9ObFudCLF0f06BeLP4N1p87w4swNZadD5ZxcgiK-3GOhl-hsOhsRIb1eYGVyIX2Yug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ast9oxIBoBFI7lndg3rqxOZBZlSaWb2_yxr-pjz9SeMIl_XXetBSB2fFMjI-VeBsD_Ro7ui_vHDd0--eMPrSwSXEl37v1UmGPNTTC2ayuycj4dOdMn0wFxcMVx08DwuJbS0b4FzXHF8MWzb3R30DDDDBwQjH2RTItjkZeNsKWqvW1XuFQqGENNJhWvpnaeOEWe5quTNE8H11SUQ22TOyGWGTXRQIHdsy8fN65iQWq2W7JK4FVbkDTRLA3fuy4RrEaYWVX9GuQ8J-NjS9VOAlGKN8dRxDaFkDlIXSN9zs56JKShV1b05A30rc2b22K77q0-NMWwbVdzCweqSAcaOfgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rj1oU4P65dSgvH5DWD48xfB6xNWdzVZG-frTD3HVdmcv3KxYmhcvunKwUCFHKlBrGeXLwZ6JuVVOCL_3QYaEvRKg7kW21YuuN5CJI07hoDPDZ7m1jundXF5yJApVeIjP-GuocLstQePvgCzotfDr9LjGieqK0O-haNRo3XBwpiJkF2AconQXTyl3m0zhmi8XPAHDxyuhbF3J6hAoy6sVB_64mpVHbeqS5Ey6TP2Xo6OM7SEd7yDIyqwlbgq-8YT0hVIHF9opQUBvxTxMVczCKEvEXl7ualCPnsbivrwaUbyKZLMeWij_ET0ryTpHzU_p4rBQ8M5_IRu5SSoMXMpTSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5FbuD8lMb3lnqfBlU9RhM8BVyGkxwekF7XBSsHza6WVcLs4AiHF2edwPwv6EUbdRRwBHiL4cFfnGKSsF8C9Xu5YV1lcZ8JSVRhFojM4aCCSOlW1IZEkDh9u83JveelYix9HSQH0MIVedU7IDSNrQKFbWcUuYebPH0ylHY4iVTcezo4q1IdPsh6zLXgk1q5AJwZ7r0yudDictDPPM8x3XeMgCMsGOC-9D0vyOKIDZrk_cK0OaPZHbEA-ctVSVezT_KD5Sv4qZGBa0d7nmibVi0u-z4Y3wsfiwgC15V9OrWgw5M9-VsTyjjkZyRnLh1OArhoqQ2QPZGtlvZQ75_q1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN8dZHPBgxeroA4xzG40NHBQxY1tP-KhhLv8hLyXDJsMuRaU0gbateFXg9ikc26NhF5AsUeOHXpd0xBhOmCaz1LElwfg1XXS0ir1x9XCgVhvpPnwyncGVcEqveo5MTNoWStSmqRQ22_VzMMPv2N0dVDUT9Z_Ph5-7Ang2SNvIRWgthX8e6iCbAQiyhUvNw355TsqQq_ZjGhVt3SShb3TnKalDS0zFVrsxyB3djcIKWEIabE53H4vPT5dBE6_YafDaY2rXzCsPtaqwucxJHQGbf-ZFN0x4HLt_yo1TvsfpQDCrLmXTUVqH5TYVLkILit8OdZGvsTTdmjy_WaBCFt89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26577">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aljPuS93S-XUHGFIWLZO_HmE5_6yttFWrPhdwZR8ewmsl-zot-KnSvofihoqTEeROihOuoKd273sS9LxC6BczfpxSPDhBEn-m7WCcCpKCsR5zT1kKeXEXOi_jMnHjO054_deq3COH7IpaV3RcrMlKXamJn6-pctAX6xO2UXIrp0T8rIrhCcSYiwwgbCdtOC4WHX1O-9ORzHYUEKzZmnuB3Tp1ukCziUci_CgHWE-xuPnuQsWDHVqPOgNqJ55A24Xc6KrcnFDf3KtJnhACMmG-CN9lPbGppMuZUS2DYAQ7Jv8hsmn5OltR-2bfNHyD4IU85PRWo8nZDy1wlwSTQKM5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇮🇷
محمد قربانی ستاره ایرانی الوحده امارات: رقم‌رضایت‌نامه‌من 2 میلیون‌دلار تعیین شده. تا جایی که اطلاع‌دارم 3 باشگاه لیگ برتری به دنبال جذب من هستند. خودم‌علاقه دارم‌جایی‌برم‌که فرصت بازی بهم برسه. تکلیفم ظرف یک هفته اینده مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26577" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26576">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=BRBjbSmLh0TVZ_RULn3RHjCiDRSOMYUalsN5zXvQO3dgCbGGUwhWtZaFG-6WDSdl9mFY6tPQKlrKSljAWchX298sp26Tdk0A4UoadbcllVi6IKHDDXtXOTLVI4emTFKPkWWiOi4hmql2XRFIvvOIX2GkCSS20ELRsIL5O_NWAiUW3w8MknLdm5E0MuvoAKUAhYGdA0MpkLNjp6kXxsm9wQq1kWoRvj5Fi35fi81BeUoARfYS8KkFH_BgkgXPOIY411JHN3cXAhrmo2LTeDHJUVnLIKx8KTxYOP2VDAfiV4Vw46Ca2biGG6iDgbUZ8HZnWDuxsM4IK4u0UbWq6SmQNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=BRBjbSmLh0TVZ_RULn3RHjCiDRSOMYUalsN5zXvQO3dgCbGGUwhWtZaFG-6WDSdl9mFY6tPQKlrKSljAWchX298sp26Tdk0A4UoadbcllVi6IKHDDXtXOTLVI4emTFKPkWWiOi4hmql2XRFIvvOIX2GkCSS20ELRsIL5O_NWAiUW3w8MknLdm5E0MuvoAKUAhYGdA0MpkLNjp6kXxsm9wQq1kWoRvj5Fi35fi81BeUoARfYS8KkFH_BgkgXPOIY411JHN3cXAhrmo2LTeDHJUVnLIKx8KTxYOP2VDAfiV4Vw46Ca2biGG6iDgbUZ8HZnWDuxsM4IK4u0UbWq6SmQNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه نزنی ما احمد گوهری رو میاریم به جات!</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjoYbnzITQ6HGDx_yHXySC_bAmPsJiCBgcrFSBPrNfMzed-cSAqGKG3tC7BkGxULjFtIfVMS5leoNtnPs8YbLgUm4ht7IQzvFuOz7nh3FverschThcGlZ_X--ktG25MdBjjbtTBbbEII4CCyr62-oJEO8bPCihQiB7pTzF1RgZxg8tUE1GVtBzHNm26aqj_QKj-HvOAwPKPjJJpxC9gmXbjyLAElnKx_ZBCWU3VYuUP8MK0f_-xURfPfux5VOoI90oHnagSRwX1VPXdFizocUFGWQjzbpXU7NdemHNJPiVGG5Ml5t9nxnUHyuOp4r3gQoyNadxL-JPQQKMV26XrJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZBHklllXJVRgP1IkRqWrTu4wranN1neJtl5_Srvac8amRaV5QCOGqq0LQwBTsE-7trs-QGU9pRu1ABTH-8YoPKnhe0SR_xMzV-508w2D1L9var-Wg5JYQNzJoyu9LzledjUgZt5wF0VexUaFGAdhtlxLXrI_rRMpDz6YSvG59EN8jZV6oeC8nSy0Pw39ijGiFiL_jte8r38oagcMNTbWcqjoIBEbQNgXlgzgyKQSyQ2qGOXEYmWPdf3l1CZ2fyzsQDkICz2i6CaIsNpjO-lObWrATLi93JMNMdaj3H-5GYSRcCuYl3WUV95IUMR3vJkfgS_14kqi_f83VSIHBnH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1phA5eHD4M8RjU-f9twahW_fLarSwuz81F3IZKkwVVV255x37PjoyzDoxaZt9fLvO4u3-lJK0ofSHGZozqx2AxA9vzF-NxFvIAta3GMbX7xNHEEsDAcp7JjeVzWfWUy4Q-8AJ2U1bLa4W-7StIqWqfTBn3Mb_USjF2nqfsMV5vcOjIApN2et6mi9tieFN6MRtSlpKMC6vdczpNkq5DU6TWdrPN5mKUOP3dDAOToU7N4UCnorXpODOw0Srr_XuPuUBCSYNDs5XQy_YXXAa18wcy8fuLEDAtihiWNu2FbtYEclDhZ9jmhXOP_lSvdedHxOQwfyF49L5_J2H3frLqHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-Up9vtW899DP_H40am-eIvmYxPbyCV5SvMiAAw3ft01LJ2GJuM32P4VooL4J08Jr8ZGOZbiEDMvoPiaoXyMz7uHh_m1-ALmK-JwkhictDwvwGBBAAsWXMZlUNEblmmXTSHEHZsMXeds2aG9asC9rg6hGUOWUH34B5eAAr_sE-4bRKLuY7oo165gy_D5EQhYreRP8iVKC6N6ZS409tmOeL7_we5LVdvXuK4AbFwOPg93lCtdGT8SosYMKXhCCJoBQjp9nG9pSxltsJBYS7S9jG3nDAir3WmJMOKXFw32gqulRZeNMorE83n14v1lJqeccbh65zlP2zQ4n7pfsKQTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4V3-f9qls6IcveVmSeqLDLS9utQO3PDDrHMASUYQAsv4gKUQlM2Noz-gI2Om1ZuDCfOCXf2e6Cmzx-A28cectMQYFnIRk1R6ZGddPZWLrYrKzUt8GTl0bQeT9NtxhjLm-hDNgErHvPcIrjhgvudVKuo8NA9F2VcwHfMtgABIuphfAnEjkGsItMyMRF_DgZ_RQYiQHhLA1cjYgK8AFsLClMDlyms_0s1IEl8CCf1tMqIC3Ctr0EpNnqvhfx4CYS6KBYb3xxJDLPlGZ_fNV-mg36ecoGDlT1EVi0afr2CrLZiT2rZ6P1eDAbsKg4euyniwdGrl9sPqsZGRy0hUMMedg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of-lc810ZmUXVMczSRI8WXPau8QTM6QiKwJG7m4QdLmzyow3MA037TpJSAUqlNnWUYxxtlKnA2q6eHeA38eWl_3mIViOKXlj9OZ1JeWdu4nC7GInD1z5o1N3ntV16kSWIODOPt-haVSteyC-rhdTMW08eS2kr210PoFFzpd0iN6anZbJkLDf51NoxXYrz4WU-SAf-x6arzhiPnCwBA_2fLaGQstCsEyfG4mniRdsO42mgtXRBpKUsDhBVA-A2t8V2d_dXGXj9TdKs80dYy02b1E4WVA9NScxqbo9nj28wqXF8H3ypTDFD0PD_ebuoNc6gL19Zn1r8VD3l6ZnVvwc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSVIiUjBLVeInuNJjS8cw8un2LzdxLxDsXGMci6mLshcoJZBV8Mpfb_peA2YEMgA9MbhvLaRHVz45V9L4Q9Zi1KyyoCE_N8s6d5E1p1PUrc9_YLuWiHe-ZVWM1eCf-yr8vUAc5-iHIwWIYVZC7yaRZ5JoNKKRVP0IUclfiEih9Q3nWGlOHYCtYfNOaam8A_4r0SVc4MjFiDCEUGFqD8sc5trg_YHKS_-5611-7KflCtFqe8NOeu8eSPTOTaMnOZrHIIhmmD8H9NnLc_AzC9Fow_feISYYWw69NJoFIU_-SmQrGXN7VZTrvkakW88yc_yFbJvdoIj-rDH7PWKIJsHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBXicVNoiuzpM2qgL_uU0EQrh2PfIpy6BdiqvNPBU-G85zOj-tLHpIcqtKeGBIloq02KKB1cPwNLNUDKkSGj0DpuovaDN1-WMzw6Fr35eKirHC-wQ9ZVW_Ecr5yUNCFB9cOEzhBsms2qkfVU02cSqcu3q5XY3xgcAYSyztP2ZYWuafSnKPMMvtV9Anz-qWqCP3Pd6RaL-DqP6ppLg-XvH--VArMQvboJRkOJHdnDTcAo0m4lGMh0KBwfRVZDK4u9w2uytLogkJN-g90tx7f6KfoPbKW_Eyc5TqlFM7duc3LX1Z4dabyF5wiXtivqzUljTXtw5TfJ8v3_xiKoP6Mb5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR7_bN80c6qzIt7gV9ZI6CqnMxYsK-nVT1ES6uAJxrEdDh2ZAeNPHOpSw3eGFuy1u1B6-3z7dJAQaMdWRl3CPLqAhDkIVtzqeSrv37dimBLuywD1gvhLkla0wuWLNozSZzCt5TH4D9hqfSiis-C85EefmXX-3n0rMYktDI97-DDeOTkBsZWv1epsHkl7S7PG9128EnluD1-dSbHIKLUSPgql7tSsRP8keSsLbfLl-oPtN1lSdhTNWXNJi6wSFJii-kgHSCMGnn91QKLu_p3Vr_tRyjA6AoDjQ1i39JQGoxpgdLDwtd-nK2QHTsWBu0nm6hasNnr2YQpqGDZPLSBYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26564">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRaeNK1eEfjZBr9kE7oIL-sHqsdXLG-BgpuMNVA39Ps6vyW5Gj3dbansqMQ9dVKWu7QF53tsifyUaenmRibZyM8EPgS3_Xir8LbiDjBktZhu5F9hm2f8THq_FyHbQx1zKRJW7OzLRJ2CQab8TbUpx3VbcEpMnargEUzjlWP_RRvth3XGOn-YLLROdw8ccPD9Sb0SCEUecPZQUJT4UCCxMseSXiZ6nlJge3m5ooE49VH6n7HPl0cjevIgy9Zj-58N5M0IiirTKE_nxroaGVtElQwRRPB3o0Tq51fegu8nbwZnPWnlH91CipVfq7LPZkW7bCnlmX31paqQWOsw8j2VvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26563">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=ebId6j14ohMZHr_2Qwa-f6bd01xSiFSp3-riFKD5GItLFfsjRn3ZmKkhpZIwSa12VBzxM0waPstj8imHOm0oNMhvz7AIYpx6w7E1K-rfdALvAtHR8RcMeiQh9-X4rNf0KwYSXSfjstj524tXRuJUzedWxuM3QhcPu35U6O7TL4yUlk8kqjimgtrGhvtfSV7cXnQpXYSxnPeUDf6cbCQoYzYuwZn0_VlqDS6V11zov2AL5HZeIfcUwutr8tj7IEgPvFuYgGSJUEvQwEM6Wr5KXgNeuqihS9VpdtBJvwnyxGUZ0ibQOv_U2Suhb541x363gdxzlxxPFLbxT0IP7-I1jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=ebId6j14ohMZHr_2Qwa-f6bd01xSiFSp3-riFKD5GItLFfsjRn3ZmKkhpZIwSa12VBzxM0waPstj8imHOm0oNMhvz7AIYpx6w7E1K-rfdALvAtHR8RcMeiQh9-X4rNf0KwYSXSfjstj524tXRuJUzedWxuM3QhcPu35U6O7TL4yUlk8kqjimgtrGhvtfSV7cXnQpXYSxnPeUDf6cbCQoYzYuwZn0_VlqDS6V11zov2AL5HZeIfcUwutr8tj7IEgPvFuYgGSJUEvQwEM6Wr5KXgNeuqihS9VpdtBJvwnyxGUZ0ibQOv_U2Suhb541x363gdxzlxxPFLbxT0IP7-I1jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcTo7ARH6KnQIJpH4GuuWOBUKunlR1e2FuLjNiJ43ohMc0vDia7YudoIoRaM_AJhMTfUqm9eYlYE2J50csv4Gk7XSBI_sIlHQ8a5rhqcJFSwh1BlvZv578vxB46KTFxS1LBB16a9OyYvGrSM8Jmce7vs6dAhgT6vIK1artJ1gKRAuFfSJ9g59YlxSlGxsQU4AZiuzRVWsMDGHnmpyvp9DaWs9I1fnGeJOzBQy51YUoBJjdlOqk9cht4Z4s-CgR_9QfDIkgn61OXqI0qQTYyW83aRPALqPtlwrCQlx6w5pSJ9yJ4FoExglkCrkgBp9ndoWq85xQwWOcwDp1M031U-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=lwlmSnebNRjPrS3NqRUri0S3ATO9aWQjaYkVPg4Og4FEWSCyT-AaYeUtH2E2y04now5yioQ1etNgqZW3TyNCiAT_khpfeT58DG8bB0YDHjhxPFDvesedo1at1i16bi-rAcfqEBJCvCiY3Z14bVoBqnhx6XMVMm4BnXolDNcoN7-npOknSkdC2GYuioD3pP7N3QBxCrts2EB9phTf-VDHieQwuzf2ezdbnak8dcosSfWkEH_RvFSjCteXkKnfRkwaetFq6tnYiNo4o8GQzhJUUOc6HPadLLGvEYudO7BmNpDfqCe4okJOtQ4mcxzTWfUOKzKtY-j_DFWc1JFZsqqMLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=lwlmSnebNRjPrS3NqRUri0S3ATO9aWQjaYkVPg4Og4FEWSCyT-AaYeUtH2E2y04now5yioQ1etNgqZW3TyNCiAT_khpfeT58DG8bB0YDHjhxPFDvesedo1at1i16bi-rAcfqEBJCvCiY3Z14bVoBqnhx6XMVMm4BnXolDNcoN7-npOknSkdC2GYuioD3pP7N3QBxCrts2EB9phTf-VDHieQwuzf2ezdbnak8dcosSfWkEH_RvFSjCteXkKnfRkwaetFq6tnYiNo4o8GQzhJUUOc6HPadLLGvEYudO7BmNpDfqCe4okJOtQ4mcxzTWfUOKzKtY-j_DFWc1JFZsqqMLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcFD22QqUFgVRLyL4dwLK8PDRI7Cdk1FH23QWoXrXQk7GXzC3leK3YyC4gO5GFQcw67FEwLNLXbjajsD0GzPnCtrIYShFQHo7zO49JyN38Z-03OOUvLQbEr2ddjMI0J3oxMcO3vIXrSgHj17sjztQMCo54-hxPiKpatUbTy95_PyENy42EoyxdsmIxIJg8pI8PSUzIBtX28uSTC_ua24v1CdLw1NRMXeq05NbTYokF9OScaJ8_vH-qXh1-FMhhbTUtkc1eOm0ZDzZo3v5k7yWx27vNWyRxhxeW1HbZwC1dtO-xFPjIIoZ4RhTO-rqumHannVhsfvVUw_gVXPiXXNhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEMdeIBn-maZ0KDxpRT6HJg00vIB1tYFDOhRQPcIsSqe60dhGcx-LXxehPjFgwTTkOD4yXlBeLavl78evdJkex07rYu22kHMcGVp1zY27p64V-4H5i0X9ujuzpIY_ELd2mEBj0dOQXCLSaAkt8FEpfbUUoU8nz29x55xNQZlR2EvG3m9HaD71Q5tZh-EUkX9IsD26F4gfHHMQJiJ34U3zLzkje7vi4fSMSCpyAblYSAr8EUll09YigeoHigawQMCJgZMXoeuqQQ-q0RiEcZasHbrK46sV5TvrGLn5BL4ZSI5EPZo97p_zflggCquf7mV6Ec-oRmmv-jmXAepcFTtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26558">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK5nqQEm3yg-eeTbaYVn4uwYjMqikNepKRxb4zGzQhEvt2YrpOQgIAAyoBZFRE2TGVN-0CH2BMxpQPZjoXJCX14eJ-Ea7sBjgyPUNPN6yX9avMes8XmQnwORaWiTCRoK4jm3e4ArNXmPn_vRX00tmYuRi__OtDeLI1OJh0c5dlp8rXvH6jHFL4aZ9lxjnBqXkZV7hoH9mwdxnMFkyNbXjRkDBug-N6o-QjQcPQCKe2ma2QXyGwJ_Y-gjP3ZH99I5dH-9RnQRYLa5O-olBfttIsRN5B9rl_meWRDwkcS9IZpqNUIWKwSAL71mUO5nx7hKZLQ8tMeCLylQ5WlBAIgHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛طبق آخرین پیگیری‌ های رسانه پرشیانا؛ محمدرضا اخباری گلر 33 ساله سابق تراکتور و سپاهان تا ساعات آینده قرار داد ارسالی‌ باشگاه‌پرسپولیس روالکترونیکی‌ امضا خواهد کرد و رسما به جمع شاگردان تارتار اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmYHr4sl9LNCW9YdjCsBOcaU0LuEJ9QQFE8PDxh3C74nmgsyJGovv2H-_bHYRSoRvpLRQfF0Wq9rbiGtmaLFcLs8H1SlDUboh0XHdkpOnYasOXNHD4E_SC9kyoJSUDW0MzQ65pjvJ3u9X5ZPIxI8EC_G4-YAeXGYS-F-lE_sukYfjZpkFdYl7pKiynVJg9h76xoP4UEM3U3fLPqkSKTP4Z3FhCfD_m2w6BK7FAjMDe4QkRIvL5ZmQPWqL6Aqj6ZY2Tkzcl-h_9Od3zQIkjtIBz3EBSrd60Gqde8S4425qmn2SFXybURuZzurGFrbXtGi9ayCcwYUhvzrUFXBGHyx2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJZvMT5BEy9hljp_KsxK9Qumv2Jh9rqz_wga4PqcNrZV4EpeZWst8q1bbxEohhVWj0IW9hVk77aUQcNtbrY-2lFageyAyfpDetOi6Jjwh4r4OygD0Tw-jkoQAgOHzEakviYkrvN47kYVNMWXS-dy7IslFFIA_MVJLETjPvgPe5QJc01QNSGNHamusI8-vEU-MzLlkxkqWe-jKsbFXZS-nNHsSHAJD-KBTPmCgCSlfhceot2fyem35nEnk2TFytno4ZUfmMDWkGBlg8h9oufUbKM47H5PLYP21Q2za0WLY1lmzuFE4uDGle479VS9NrM0dJnPKQsW-2sevFwfkORjew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2kQhEnsBr3_sGdAxw-FgnMU7Ze5_a_IxTOE9H-kfcYqcaz9y5LJk7tOz5o3BPtNd5_jwZybKx5ovpnpL1bgBXyB8F7W1LlC9cfc0olpS71B1WCs3XdPLN2Q9vwVraHIK9jYSBwLtlBAEJz1LI5aA9locc74wGzFMZr0c8ym9k9ZFseqcJN_Mg7_lJYG6EAILDoUHwI5F-nU23aLuTwd8KmqAt13AszwdyV5V705kHU18N5Ibh6zkggWkAyr2KwacuPUGv8qUPlZtfbsVfbYlX1RzqjJSu6_EiVVySTenk6kiZzaLb-lg6-KeFKrpMa3IALJEpr-7pe4o6JedPYvAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=A_Stj8S8y44A2uvNLaDCTAnQOz-qkc8DpGer52YeoFfqUvjWA6UZ9pl7VElh4vK1pVzXdek6wWF5rIe1uvw0-KW3Z86rfeiqE6RMPeUOb48EU2tIknPt4uPTy87iHFwx8HunXZLlbihJ2VW4U_d883OJ0BZCoyntP6rQU62LkbEXikzvNd3n5onvA3YiMvwCi9aVZXLuwDMammwb5vFelXa1Guq10MjRQkXQH-z86mrEI6vjBykzNIDhyaDJqzfmzQz5yZiqIuMqqS3C5brmaeyTcS3oUcVk1F88q5HDMw0uLp7GtLVqpoAuJlrtSDYmq6nPEE07RTFuSB9M-pofyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=A_Stj8S8y44A2uvNLaDCTAnQOz-qkc8DpGer52YeoFfqUvjWA6UZ9pl7VElh4vK1pVzXdek6wWF5rIe1uvw0-KW3Z86rfeiqE6RMPeUOb48EU2tIknPt4uPTy87iHFwx8HunXZLlbihJ2VW4U_d883OJ0BZCoyntP6rQU62LkbEXikzvNd3n5onvA3YiMvwCi9aVZXLuwDMammwb5vFelXa1Guq10MjRQkXQH-z86mrEI6vjBykzNIDhyaDJqzfmzQz5yZiqIuMqqS3C5brmaeyTcS3oUcVk1F88q5HDMw0uLp7GtLVqpoAuJlrtSDYmq6nPEE07RTFuSB9M-pofyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAIbfzGZPT_7VhntykwvhXLW0Q4l9FsxDBU3DzmvPtMH-OL2jCKZIcZVh1M-_FYVoKUN5CzE3M7Exc2MjYtym8rE7b6rcJnSMbDTmz4u6FusEj1Sjf9LB6X-cG2U_00iRCvQFeeqWSOHPSQmL4LDYE_gzNAGpyrPqXkD2Pz-JU-9o7Injx57GeccjGnGrW2gO8U-dqUA9I7QfukVPk5oHbt1hUN8za_UdBXHOXdhVcwFmbRcH7vYGILeWH0F3D_o51US6gXUCcwnpOiYDChkFpNVV6nE_2LPhf3gia3wxUNFTnwO2QGwmuS2Uw8mxK1NxkEht78vp617APWbN5kyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=Q6C9pWmZaP_-GaT-peMUFjf2EUQjnkLykxeRlgd_ydiDigg9XhsNEvW2wTPDpOZN5ifctvGNNY6GWhFZIzDhHa8PcisAII63pUQfzTUueFJAmjMwL02XV_NJS0GRHKitsvzjleAOTUFDrt-BUq-I-wmSOj4VZCw7S9_0j18LXNtJFoJ0XkFjqAQdBh4P0fo_fXQpEy9I5Yu3wTZgcbHf9LV7PKTUHmwqlce1PR0IP-R-SeNRE5WKHaTHfNbCZn3UI08OqjvuiCanNbBHLcHJWQ0V3EBpaFMRmDuNzKBQ9_rzgGG_rSKhSVFJygrz02L9FdAGdmiPbwIf9Nq5FkG2sK1b9IBc80VjCwH6D6vZUpskbV3aPmnLCF6L1GukX09vwufLbgGn_CsxbXB0mS0TaLSYflo8xDQvXoYwmwq4OsRHIEtUHzwqMQf_ug-ArLz3WTgF9grZR-jAJEe655Z_JpAvK559jXp9q5RAzHwh937bgA2ixQMtmUbaKxkbL136lLZBGRBk0jbry0fnHpWxLWFBrEo62OKHmKqnzBIRcPdmqaVkL2RAtowYVYZ9O13NhQkfeTa3T_Bv4tSJwYXbiIchIaQgFIPayy5R2-az3uKXY0JYljZ2_t_EG4srSJlSwT3bwAp_d3UZgt67RHx2Znn-iWPJMeJOP90w725tJ38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=Q6C9pWmZaP_-GaT-peMUFjf2EUQjnkLykxeRlgd_ydiDigg9XhsNEvW2wTPDpOZN5ifctvGNNY6GWhFZIzDhHa8PcisAII63pUQfzTUueFJAmjMwL02XV_NJS0GRHKitsvzjleAOTUFDrt-BUq-I-wmSOj4VZCw7S9_0j18LXNtJFoJ0XkFjqAQdBh4P0fo_fXQpEy9I5Yu3wTZgcbHf9LV7PKTUHmwqlce1PR0IP-R-SeNRE5WKHaTHfNbCZn3UI08OqjvuiCanNbBHLcHJWQ0V3EBpaFMRmDuNzKBQ9_rzgGG_rSKhSVFJygrz02L9FdAGdmiPbwIf9Nq5FkG2sK1b9IBc80VjCwH6D6vZUpskbV3aPmnLCF6L1GukX09vwufLbgGn_CsxbXB0mS0TaLSYflo8xDQvXoYwmwq4OsRHIEtUHzwqMQf_ug-ArLz3WTgF9grZR-jAJEe655Z_JpAvK559jXp9q5RAzHwh937bgA2ixQMtmUbaKxkbL136lLZBGRBk0jbry0fnHpWxLWFBrEo62OKHmKqnzBIRcPdmqaVkL2RAtowYVYZ9O13NhQkfeTa3T_Bv4tSJwYXbiIchIaQgFIPayy5R2-az3uKXY0JYljZ2_t_EG4srSJlSwT3bwAp_d3UZgt67RHx2Znn-iWPJMeJOP90w725tJ38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OErzUMoOZ-LwTQH23sDLPnMD3CYFNdxHhxNApOeBcC79o30gR3OxwOxt_wiBPVuzwYhmOdB6HGvucno37Hc0LTS_WlslxsIpzEg4oBBlYD0hPXztbFeqP0AWCAo2HAYJDI-gVwmvXXoejlDaqYcknTeAgZoc4ij0uK5jBg20Ecp2ViET8ETmNJcBdZ2V9F3RqARLsJGmAgyq0k64uBKmjo7Y9o99JGugSu_UkgmJO5vszsezWw8ZDhI4YWJHDRYq3_8e5h0oxYkLG0kHVcGeRFw5T1itnl8CsXFsbEaHf7dRzwucfqgYW3nrLaiTDDaJxaP5moCtzzTaBBuni9bPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBn-uP-qEASQia3ed-Tz2nTOqvp9Q3NULiF_zvZ_2LaRCBC2XJ0pTByvrlh8RNS_9P_AGTajGab-2wJBINmwiXDUBdp7b9NTQbn_7b2R2yT0zFRcURANFJ8lT9snt6qu-uTPhNN8EPU8KmmWbKd9bpW5M2F029B5tcAkFroFMDB2hMe7qM_Fo-_RtTkwHrGpEi-_Ku6Tq6cm9j-2L06jjY8YBrFuGlG7yCiMw5fsTJ8CiJ0CuMiXSaq77l--YUu0tbp9D9nd-a81BdlZpaBcXw312t3xuZirL-ld1YuUzCFr9tU6NBEuNLKGS84Ae4gPypK3IhcfrLdsoaefataChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSCUQ6OKkOLUmLSoHJ7WKq3lxCHnJPqkBbk_Kggg21AfQQfvl4wqkbxa1-CuRFTxQVmyRa-dVTcP_Jp5fcpydjlpc1HW3vHC_-ow-hNdyfxBPe4jUFCRUy029tdORSyT_KI89m0stUF--2px2Z72qoz1JT_F9QFOaN-7OXWb9d95p3-s3haksK4P6hf0XTfFZxmn7c-hol60t-gCDUZfMU0m5z7U0Z7YJ4-0mr8LOMoY9C5FuEO0vP8pklPfTpStTDsj7LBQRwutN2rzpw_9l9Qj6AHntyzgpnVw7E-D4RMj3sNIJiknx3ADxV1LtLNSfzrHphaA4KSjFNl1_jz2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=LutDKFOpadcvNPAaxTJxnztY61n8ItZwawjjvYv2DtZRgeVAj_8rsO2V32jTrvW1UpVDYkkV0AajE-hj7T5HVwZmgk2fmScxvQnz3w_HlY_92TUVcWZnb-eTbBW58TDZaC56dsoBuZlhrRe6ClLiDvLznm326u3KlMf367-QC8fFNa2ennKyf-vZKh4H94VtdzExxg-PhNVETiqEmI_D57pCw8GG7dCMeNYo3dAWvNKqfbo_15vaQk-JOMxdTTuqhJMYRXf3WXvYMpo28UQpT6A8Eli3qYP60CY5U-dJKGUejoJucV9Wx-sgC1OxgaZTUoO_HSt1dAas8a92QKsIrJCaG7W79VD58BLqJh4zbZK50AZL0ie_ji37UrB4mPovmu63LN7WvRkywAU7uNvhon2pQmoS42MyyVY1e9d6Orm4rdWCuzLGo_yhfk_-L2qfJrcgX4qGTxkt_BqhwmOkfNArw00PrLA5v3JnYduHW6zTi2XMQrNQP_o4jqWvxHom0hNRtp7r31x_xTMNxYAZVFTZcG_QmdoZR66DqBm2jB2DT2-PirWMw9NXWEjvERa3JDR4xrBwottxY7twbjazLCSqe_VNOg08wozT6wsxV9lLxeIgux4ueQGCQWONbh4O6qp1CS8JAOdSsQ-kBWL6BFAHIOityPv8ETSzf3QrOnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=LutDKFOpadcvNPAaxTJxnztY61n8ItZwawjjvYv2DtZRgeVAj_8rsO2V32jTrvW1UpVDYkkV0AajE-hj7T5HVwZmgk2fmScxvQnz3w_HlY_92TUVcWZnb-eTbBW58TDZaC56dsoBuZlhrRe6ClLiDvLznm326u3KlMf367-QC8fFNa2ennKyf-vZKh4H94VtdzExxg-PhNVETiqEmI_D57pCw8GG7dCMeNYo3dAWvNKqfbo_15vaQk-JOMxdTTuqhJMYRXf3WXvYMpo28UQpT6A8Eli3qYP60CY5U-dJKGUejoJucV9Wx-sgC1OxgaZTUoO_HSt1dAas8a92QKsIrJCaG7W79VD58BLqJh4zbZK50AZL0ie_ji37UrB4mPovmu63LN7WvRkywAU7uNvhon2pQmoS42MyyVY1e9d6Orm4rdWCuzLGo_yhfk_-L2qfJrcgX4qGTxkt_BqhwmOkfNArw00PrLA5v3JnYduHW6zTi2XMQrNQP_o4jqWvxHom0hNRtp7r31x_xTMNxYAZVFTZcG_QmdoZR66DqBm2jB2DT2-PirWMw9NXWEjvERa3JDR4xrBwottxY7twbjazLCSqe_VNOg08wozT6wsxV9lLxeIgux4ueQGCQWONbh4O6qp1CS8JAOdSsQ-kBWL6BFAHIOityPv8ETSzf3QrOnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjVVpcSNDHnxHlDb3c9q5JY5dGBlVt42sFXXbEy9bT_YYTEKOyyswm824t5XwiMjqj4w8PG7BT7TsVVrnR4WZp2d4RMN6Ula9jZGqHcKDEhoU8YTQGm2-4yVaSSZmpMM82ejQlo7rEVSdeSFRxAELH8sxtRZCR3JmQ_Dqk9DobF3z7uIYAu9f1CaZ0ruvLUdJIR9Ukf3x-_riF7_y3OEE8Ec_SFcVmqTUxOnv1fdoy5l8otoo7BJz1Rgrp3dDU8bPH6URLOm2i_ZMJqMCQoKuxhaBldekDtxnIMdpIppkAFoJETwfkKl1AKShJX5SKMENnzp8jjlFAT8RlRn_QM_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozkXaXxbc9I2DwHDhdmO690GQK4ACBgsZFv1LniIM2pwvPrdN288UJJ62DtcpVKOzGA0u8pesV42aDWkzzYf71j5xQVfvmb0EkswMFyjyT4MEYg0rO05atrYsjEievgBciatCEilfOQyQxo0Hx4xzKUe2MZqKSJVja7m4B3rCf_ey6osagHEBakqU6wpYC4PI8NQyTRvdvh7qG-BjuLZbDV8IOhx8vFs3ARt5pCAPxavmJf3e1UFuAzeFw9ur1wHivnWX7EWTglbSnGUYH0ppVbjr4ZnkeHJZrYTj7PQIUQAKI44S-xrgRGVPJ45VdqMQcBTOl3rm-vp1L7gMSBtMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxEiEhVr9PFfnNgMHcfOzLmCVb2vraeKhZSUyEoBcKZeWqYDFJ1jSl4C8oOjhRCHs0cIo9ac0DSAk_ih-N8WnDSEDjQITnVV2Bs5vYBcbN4x16_KGJj5gC_aT0JyhbpgOs0IKWl4aXRzotijo0HjloB76OpFS3jWy8x8FbrIWK48RAYjmDDumH9gWzJvKS1CrG11vGNrrqLMgMz5CxRFwLDZ9am77myVi2LogO9Tyw3hOTTG7RYd3QhcMSA-cF2BxdV4vvSHb8A_ot0MQzSfjdi2URUTq-xSA5tLU1FDcSRghsf2USf3adzqGpqoK0kIebYMTmxmtPJ7xE8RNi0V8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jot5uJYVTAjDUNAc6HcQL-CzhcXdE-1vDt90GYzfQFqzTX_t07ahIxpVdf_2FXMkln23DRSLsVT_yDLIyNUkVgc7C9KQSs8Fkj2tBlyyU4jczZA5XhwFWp40mV1LwN0Dbdii4LCeC9RC4UfVsvPqlpLjyShax-kcuRgPim8Ag9KupSJVPP9SLzZ-0HvOhN8xTNSi_YY4K6C3gikT4B0q9xSDA-naBaPKYJYdDTwtgdIt2RH_bxwD-zw1lYnc4ScOmXi1sGr3V2-OKkW-wmOIk0fbN5Tr_gGLpK0kJ7Y8uSWkDL3JqvLQ9reZ5p87zSOLiVHFvj7qgMNTdi3RZJRDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt82NMEGzr6uqocB-CqME9uXmx6wbuGixlVI_TyZFukbODjPoCqNXO8iDENHn3YYAZkSAmFW-nAMbsPm_xH6R1Zgrv3j_AsY2aHhw7ksGRQ-soe6kaSsTrF5mgXJFTx6NIvTtD0fydb6hNbtSXvPDLRdChTjaHWu9bli4R5q0GRp6lKyRmTLxKkyNsREhqPticuIGreELEuYiYdhIUmqtoRSptB6wk02R64X3Y9a2yvzdMoxsItRsKL-Gz3wRVFSmdVL2pfXr1D9vihc41c2vzq7uurHC1x26_KowXQvXr9F4lt8JCz_mlNtnSS7Xp4BWC3ySuDpxNmWH7j_xAPhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=jksuXj8M2Uag07KILH-hyWAvOYPqJd3JpjM3GDJlfl9ZyyaOpJ3jlaLF_3rtU6L-1Wnpo9bQ64cczJceNjZVbgJio1mpLXC_Z7DOdKRjz1FYmArhteqBpvaGz-gD6FXjHe_AjDCstWo1rcwYOmgbxb86W_wqzLviSVdola4j0vRkwr-JqEVZ1ZpUZM7_7S6eH_CWWMny85CWy5cfQIkVJD6ydPXNVZRhAOOLQ-tjUJRElrXdcNOr5UYQSCJJB054jvThmoRiiLPw7NmxsjXn0e6kVb9n86xWWO4qRs33l9lBGzE2mKbNF3F040YmrVsw2gptWfIWwhoWJPyC0qzQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=jksuXj8M2Uag07KILH-hyWAvOYPqJd3JpjM3GDJlfl9ZyyaOpJ3jlaLF_3rtU6L-1Wnpo9bQ64cczJceNjZVbgJio1mpLXC_Z7DOdKRjz1FYmArhteqBpvaGz-gD6FXjHe_AjDCstWo1rcwYOmgbxb86W_wqzLviSVdola4j0vRkwr-JqEVZ1ZpUZM7_7S6eH_CWWMny85CWy5cfQIkVJD6ydPXNVZRhAOOLQ-tjUJRElrXdcNOr5UYQSCJJB054jvThmoRiiLPw7NmxsjXn0e6kVb9n86xWWO4qRs33l9lBGzE2mKbNF3F040YmrVsw2gptWfIWwhoWJPyC0qzQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEn2iN_wIvAbZGIY_ifcM92J6OlDmWQo9JGu-tUKcwSVLUL0bNYQ9LuOt6HChZyuB_wJDrE7KHtCpzs4R1ZB0DwydbxBBGttGMc6cCIDMLmDlPbx4kL0m-G814DQ8QGWIE6ogrXqILQ99cK4NCNu_wiMlu3pNmHT4SskrgWDECAJEB683f7u8Whk9YuiKJ5xdP1L0zo_grPycGGX9X0rc6jH0kS_os7jCQwmJ1Nlp4rAI4ZIJVMDNKku5Xr9HfIeJYHKk93soV7bUh_CqKX2_jXSVPFfUWNIh0W9XaD2H6UM612SMJd_0lE5gFORFCmurAvdxbabogYjFLGYiBUO0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrC52nFNgUsq_OlvkqIQmVPfKptvxbkPJby9dWUILlKWnv8yjX7MRu85M7kxXdidy8xWepCx_osZwzbed248G-WBCvpHVi168oayiS3-8GrXE4D0EMCJ1ginQdHgyBwA0hhhPuFFNfqSnKOXu9A6-KesV3sQjRMiRPvD9A5dU2bTXqHtJ5QCTc1u-XojjLBkX0MS747pJy6B4XZM_RCiaWDFH3kfJY94IGpLxG0xoTyUgzbqXibhB5_grDQjrh1GuKj5NwwAbriWvBowJoMGScJVGxNx5BjUeM6X9XwfXr5vjV5vYD1uG1FQ7oKsWfyduEGRCfcuFOQai-whwLmTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paP7Fk8fGQWbouF2kLbjnKUEFR4pVWWZhhgrj04mF4WywgcczfHlfADybiitjBkz3v8C7OBP-lcU_CX17gkUGEEhblmLcxZotaiEg3XNkoDdHaivjmp_VOwV8M4L0zsqRw7VNb40PwcUpxV3gDhJCmLmn4aN8qpWJBjau2lKLFrSp1GTP_ae5hB5SLm1RBXZ0DPOi6fl5DrR_v6uZkvFWQSSMpCzu9nU3UpDvezNKMe4nzcn0xJoZ2eTDHz1VqjgqDpkP4_xlq-JaO7G_ISUbLLQK9DyXWPaHCJHtJDwYN11fqtPCSpKHC6OKWxD-6p0QIViGA9vj3P9hv1xo_ywaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZwpXDUQPr6iQfJiAYe6VOxn0Ihl-VPXaLrIiNvrxdG98XBuGpZQO7XqnkT3puZxKVtq5Wdna2G0Me84gckijJ6j9DT4dVyp1N6rMd7VHpm943b6KE6nyUF7iHNVxxRFDZr4r8AoTQvP90Z1ktytBrJgZYBR6CW8aKtU65SoeXduGv3ePgfilhsPetQ9hRWQ3BSl6u4Pj1XadLN2cHgCCm-V3Oi2FVyKaLBb-jzTDKhtCL_949TcRcJwMVDU_6uaf0BhxC_sPa8X-4IAYBUNycXFoFuvx53TRXYKmUK_8rnTx3anjQVD0qFU6nZdg9PI3GN4Wc89CEt7cPaiwXPL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PI64DgMtEa5q7KObZZLUmw28jCTtrPt3xhf5kDb4mbTugFXu783yuNqC1U5RTHrRKnlOc2wkcchvKx8gctVBgvS-eFv7qpy9437QKshITCVjAtjKm1SCBJJ_H_5wXJ4euqOCYS6ZvBJ4tBG9qNKeMh90oO8m5juJVIXiO-F5s30_ytYYVrbkO0gDI8bRhwIBtEq2tvl084d8vX6SvSYgrblNWnEqq3kDMlOxcuYme_kE6FcQTLvjCDzLpzsw2JLxk9n_WQJ4-227Z-STVMtfIqJHWA81Nyi_bV3tPvwQBA9fhnEgANlE1Ft34P7OBNLnbR74MPjCSCkrmAz-PY_KOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=CwfzosOTHC9Yi5_dGKjUBzPm-E4GWlylO52CRgd8G9qFuDqDZ2dEB-jE-RxD9hdvnxnBb3yIm8Me0KBCn5-r4YUTuu3UQa6WRoGleTkxZDHHLJQiwjn6YXX-3tckbwHhSYFFYrX2JE1m_gplYHcAanjIKW2pdycu6xG0k8nVrBiCKhu_J8MP8ft-M4mM9zhPrWmzxurY2W9I09M7LmjMQQcbB21I1hiHkGmFoGFfm41aX4Gupwrq1xnBBd5fMhOd4qI8ZSKFtYmobfxCOqXKw1FU1DjLznovJG4pRf2evxrweJRmDDjQmtrlP4e4jQ12C-MPtkF-viOuru77ekApAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=CwfzosOTHC9Yi5_dGKjUBzPm-E4GWlylO52CRgd8G9qFuDqDZ2dEB-jE-RxD9hdvnxnBb3yIm8Me0KBCn5-r4YUTuu3UQa6WRoGleTkxZDHHLJQiwjn6YXX-3tckbwHhSYFFYrX2JE1m_gplYHcAanjIKW2pdycu6xG0k8nVrBiCKhu_J8MP8ft-M4mM9zhPrWmzxurY2W9I09M7LmjMQQcbB21I1hiHkGmFoGFfm41aX4Gupwrq1xnBBd5fMhOd4qI8ZSKFtYmobfxCOqXKw1FU1DjLznovJG4pRf2evxrweJRmDDjQmtrlP4e4jQ12C-MPtkF-viOuru77ekApAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF8ogcEC3K2Tx8LXrlz5SWxuHmohaf1yGOqE9hGv02c5mPjrAcEOqVUTgFM976krFPjpzqt_y6aPgl2X26P93Tsx8qBI08Mp0km7HsKy95AajFz3DfD-zbke49_d1wVDkn-7TsYJpXh2cS86QKpt2ysD5CYmh3xNHNZb8PjF74862uIHzKGmY4c-dScU1czTuDfZVAlZFr_KvPV3b2jW4DyJqahz6rpleC-QFJ-zCxrI9Z9de-lYjHZPfrR2qIdR-cym6OdmHBhJQ72DCRqHRZ9O7y3UXBBu0BO4Re9Ma2zh4hGg1EGwR_SIb8gE4FQQR2lSlkvUO-L_794bW4CHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOTave_v69_LDITN96n3LVnLFqh2rPeYSUQgo7X-s8gNxjNOaaf4CNaaKk645jhxjR5nj5MDUBPaVnLVIZ86JlLK5h5zD2YaKGwbPRFzG83T75B_ExSIpYS30yQs1gPQfw3_8EU_mYya9S8QyryqBWqrrtk0oWAFwKk0TrBepCpqhq1kLcdvgxdx0MXDMXQR1xrbZ6BZVWmo3pfEESpmhxVEXbhGXhsYb5PxNI5PN9OHKtqYRwqawxA9XB5DOwRZuVs0vtpgRoay1UQVXmETKyQkCBpAoGw8GIkBwYkHOPN6Bb5YeJ4npIjHf5ZuQNxZ2DT96YoATBIKyb5gdzk_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9twj9ZzQR_GeJOSoc-ldzayFhCDF1ZPhBoLUXnrty-_ezhi3LNgzZcJzMisxBqPC6w8ofHsUe1mzt3dPYsYpagK3Fc0vVlVeZU28cE8w_PYvN_gwCOqBbZz5jzJb39IIoGvnEfZbzcdEazLdMHAJTKBIGiVaIqah8zAELVP9lqKINvduWjzTRsRBNxObg3XlgRsEq10WVYdQxvxpYobgmmhoKWxKPiEca-R65bJWLsyq_Jl-hMnA_juhIZztBVZB2wPnaXrpAmSfWDKqss5_B2Kxu6rIlSHIjS9BHBIc6KQIIHeE9ugViX6TleLES6pHscIQp4Ildq_N4Aa1oJKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBLcJ8KpNyyNI3oTV6atgLNB8IlQ4xOSAUw7hOtEQSWAzUMsoDQjak5HhrSbmzHVAudJbE_JWvyq61_tgBoZowIG4PuS7wktE0ThtsWOfmTB8byObGxpwED41NuPQ-UfTnrSOs1_7kQkeUXcrq5caCStKASmmqHgXzedOB33ZaBsXScuE-s4hD-_cOCz_xYseRxQd_fA9VrCrR7pF7EQMCsVtdM0CHjdzS0U8rzVTCU-ih6nAh3aJwAhSmiFI5TM02k9wDFTWSG2F7RL8a0LHgU6OWMmnAncjc_Y8avbq6RvchKTauDP08crSIMGlox3g4MzaMyakyV1BU-x84jwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYS5FQGJhhS64rdw984use2nW3ZWj1ekHI0kS0ALWmb-NTAvCdL2mh8txrFp6m9fvG1uQEDJZPAn27GrFfVEbaeiWObBTV9hZagnZZ9QO_I3JB6rjqogzPiXKGRAjripgTEgh4ggNsCgbQun_wiqtgfFsr8_GQufD5F0ntIGudHCobpbmPB0PJ60ednBybzBY_2YIPdEHg7Rp2b4vK0J2LTSuCf7c5sc5CIzEw-kPH0kQemhFjexN7llcqE62UI3cQKJUT74nLT1_NUtu6dRyoc9RCH24YT6GaRy8MOrrBQR1OGQy5fIZmjatwRTblqJAO28_cc5zjNFMcVpIpq6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llNeRkcw6P6vQD7Ai-NioJy1bqPF5i0LOyyGJ6JVpfEUwxU4O5smZM1KmeFUqDnenx3L7xB35l3iCXbEEGfosdn3Ys2MLsWkO4Wn3PlnHhZxYGMavMOlQ-UX5xh2YoZOq0sjQVaqxiU67zbIPFdBuL1ykaSNtI59KK5RkQ_ufgkcb4EDOSiUxXyxCecdy9c7Dymscrky5ngmomoOKqRcbYcsQAvDRhNK53QupowIJwKsDR26ZKxPYPt5-yipQbBYA0p_EqvsrIqGuFv-WxtlFiAD1f0x0reUky0QSeulX7lsIP3JdEcBUdo7mRVOk52UoRu0I2nNBBt9QG00ixtLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26521">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=oCGDh03rIQMiwmtYf_iC9VKhA1X5sGkkw44E_KSWoVJjE35IpsFOeXXQxJpx9DKbPymVa4tAhJvKxXvElRw_ShYo3nb8XLN_OQjc74Gcpabm40BqDIoCErknSKG8HV5mK7gnJNb-T6Dyqi1LGOW3PY9-ZnoA5i84fbviwqmHipbfVFcwQtgzzhV6COoVfe0dioO8kxavPiQxpeY1ak0a1D91Ti1Q2y2Ik5J6HQi_joVGZdBpzew-XyOGsJ9wvMZcKjavyBht8N9QcEjNKXNIx67x0sxEoTsjUvIkUmaFkUWx9D3qRetn2ePWNKiCBbCBvRZgKSIuxZBUrtHArTTyOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=oCGDh03rIQMiwmtYf_iC9VKhA1X5sGkkw44E_KSWoVJjE35IpsFOeXXQxJpx9DKbPymVa4tAhJvKxXvElRw_ShYo3nb8XLN_OQjc74Gcpabm40BqDIoCErknSKG8HV5mK7gnJNb-T6Dyqi1LGOW3PY9-ZnoA5i84fbviwqmHipbfVFcwQtgzzhV6COoVfe0dioO8kxavPiQxpeY1ak0a1D91Ti1Q2y2Ik5J6HQi_joVGZdBpzew-XyOGsJ9wvMZcKjavyBht8N9QcEjNKXNIx67x0sxEoTsjUvIkUmaFkUWx9D3qRetn2ePWNKiCBbCBvRZgKSIuxZBUrtHArTTyOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvKUQd-gIZZENA7EspU1MqaEpvDz1tnenb1yHdgtbIhJCIOo0g0ZNTHwFCbSqn7Oj36hJZUFRjWj12ercagOqM5Zl7ExP7ft-xXbTnWH1s_KV1pPa1G0Lq329-FePlp7JQZR4qRcJayBXNWyhSnVph09XKWLNhdrQDV9UcWVEUGiLf2Ky9eS4-fOIgh97Nme960xHkgsEG6c5Hp4BT0y4D88ljLH5756Yr2eyVwHYnJRq3kFOkSOh4eUryDfcstrp6k6jJI3VWaA4dnX-Wirusl_vuKxcwCWYDksaTo_oj3jawhklhC0clSzEZNWzl9sKx3TTOymL1bb_C6m1gUePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVLQhhBEzsVYkMsnn61k7HlkFNjrfaBaA-mdpMCSaOMYeFE4ZdH_cZ-NMz2MVl0Iw6yixGT4dD-lJ4Y6N3WBwSj8FR30MyCet--5Pjh_qZMcMrod9G4HMbocHNGfjGu1ttFoPNKFR4zYt0NJ4T1aAqnopzpmFjvp7wmXfnT2iR6mKYd-1cOveiWxXPa5urQmRWGqTrIZ5L0o7Dh7zqBmm-O7_jOZKsa3Yr2tvS44anu8OF2gB26j5OzGcGCRg-SetvlMOYkM4IMaAnWxDFpjL4vlSbTBLIYokkd54rD6gsNGJQGQ8FzPK6oktkD6Z5TcqW4szqy5UuYwo5A7rsETEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khOx0GU8UQOlRHYNUpft7Vb0n72NcpY9Dehe60JSMmLzu5qTEOl4Suq0LM5kTFz0vKdCthvJ0e0ukbz1SN6mTf7oTkHQBa0nQEXv3_fCqhcvKa7hEGGrWgwumcnjcJm7ZXmvejf6D8ILakLPg4EyLtJAN2dcR_Siahyj1uu575jwolZEXaGMadeerv0DzTu97_KRkNZaXDKdqFaqkAXOpFpsPt-i0OizJKODH2JPU9HwrVcxS_lXV9VffR3CzoRxR3GJfzUq8MGN8YKoIdPchicUMZkLou76uycy0sKeXPEMbpp8V8bdmVUvMS2KFZwaraz_MwFZ-pijq4As1NDCnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFMobhiUFHSW7bF6ETzFG6nCdySqtF6IQyM5tGnSrurISNZopctrqQpVOMPzJHED3_5Zocqs-BzqDghGlso3Vwpf8WL8HHiBrhud6oYFdoKUFavR4fmFH48DpcSy3_VjxvQyuVPs59WOKGvc6dR-3CCHhetjU3lmtFNxqx3jEu-BJ5NsSD2z_Ku4LxBlc6UcxwfquL35dYE_yzlVSrtGwlx2thpN1_z7OUOYpLT9qayRb9fTwXMQKHjvM8qmSZ59YaPhAbV7kzB15qWXz1tNPTx3GoRt3QXyFfQoBybeUKZXYWc1X0ibCHnE3BP5fRoK2TYlQrYv3WHinFBMGVHzwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDtQ7BKUSFigW2ztSKMmzQb1nFjdZVC-6Sy3_AG8nrFPpl7E6IoH4ckitoKl4huqR05YN_xiWiBcnLDR5qur98Xtw-NaD_f9326vnBlhZMy8E0kpWHMHf7J9U6OIRkiqdTI1moVpDB2i2TneEVEt7on1GTRkg5amnD7S9Bns11oRPhHzdY5f9-ONW1nOp6ibA9zdEk_Z1inOAFwajUSlkfwd_oydLdup3jSHVlgZYSHyQahgbQyIJILEyutwZv27cJfTuBUAtGS7gkZz0ocgGrKB2V09184UGuuP2Wq1kYqauIJdKWSuStnU5WRZL4HIRZ9V2yv1FXGhRtTZ4amH2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGyEhtxsjf96fQdvLN5B-ItQLHMqKKe_c8BJAggdARXpNrXq21Uce6ohBKBrsTyQyethd49LNeJxweFvJ9VJzZxGxqHhSz8Ka4kRpJ2VBXLz2c2ybf6wHndqiyS8ORgr-fobUionw-jdi2eCvTnM-E9JJWYQAf6TKd1Wqnn4ppe7wVJvGtxcl5OTBYDg7_Uhlk58HIbY_-wttIMiZiWQgC_u8rjj9ZreZaltGHsD0OVHSjgNTLxifDKeF1xrFZ2cVOqoDI1dlJzcLdNea-nxBsnCyui1FRxIvCqg-0CSFqRIc81QVcJfBHpfLisuzOHhpi8Cin542JkRfNdht7m6XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOe3DKiIq1JiTtnVz2SW6I8xKuhb8XIDPz8t_KHKA8a32cAbEeQFJYIbISNCVt7wDwzJ7oNVrfTCdwQxE441TH6rv95pP5DgBWXX6oUwXgL24QQtE7KyjxoaXIL6JLjNsb8GdeEkUfCcy4Cw0sQzKVdVIyjW36rTqLXLTOa0PrKYY0ZA1yTIzf3SkNAyW5Mm2YbmTgd1KXditA2AWYRFj-hCqEKiYOytw4t9UFwz5nsXccwUiUrhysdTHS3p2lmIYqkwvq69KnCsLV_k-ZlMyocirueNGjpYam7HINZLtuO3Lbtuo-M5_0-mrr6Tr2uS9TiB-8DkVy4v0VRdx9eP7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUd6idt-eW9wF1TBn85Xin350dKazbYH6SW72LDp1ZaWQsPJIrkHmstcWXpnurONj9qw5pqax6KugJGnjzQaN2uB4H0-ayq2I9QPfa47XDNEpAWoqx29St3r4U9LcxmOrvSjFVDWEsDEJfXvC2AuBUlbGxytVsATwTDdLt97HH03B_2eWsfBE2VJKiIUnGbf2gJmGYLyEc53kHRZn7OnIhfeATIWkwdfCofCT1KE3Px0k2pS0_t7P3-8o0eypSN0pFIYdFTFOM8CzJpPEYbs3cHbhhSefd7M8E_DuuK8g9CFB9nR5u_Gs3k9qSW72rXsYDvHWO_pO-bMoEYsPnv8ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHiHBMGUHqMxklR6EFUKq5t9oA5M1AT5FTSmyLBnayX3Y_PVtYxqAWLWFtO0yNk7CdSOqRJiI0zqCQNnfUo01Z0856iBz2-Nfa86C8rrHGgGw3z_cQUB1WcxNDt9cs9gWbTEqIMPr1CiULVQEU5sfqfURGWAlK6SfN3Wv2apQOYsW_b47pM9BoFnZb8LCc_OkxFk5lr6YC1d7qCJTJFXRsz0Yo6mdIUuk_cRiy2w0AudILL03HhqpW2iSxTpFZppPf7SMz8jB_8O2gdoe6xhGaOWZQx5ZjZ73xO-OnRjkzr0KOFt9ccRiZkdjsidMYMxTVWm0dWUJV5rxV5BvJQwJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul1-aT5qRuD_BGwLADb1PgblyRRPqGIpQOtsUAjdKDYIkAc0UoZgIIlMgkQKsGqWyjwAwN81c0X4sFWlArdA2SyD3LG924lzrs0C8MC6RQ_u3nS_VqYx5aProfutfk1dQ5jAH0ey8CQ9qUwJxv8w96IspRJ7Y83Mlb79prw_-XeqkPWU6stk2_hMymJzEFKmptbL56-GLtEbHHKInFVunrrewpqaFvjgtHyklhqFiz7PiuNluKzqT2iTKbtj0QWESW85wABlcXse8l2fF8L9t5KwHyo7FSKDxi0DvpksymqanZv_iYR8xhslYnuGVGA15AgbnqYW7madY_rtVL_sqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLKBGbEGj1xzczDEvgfK9sSkO1EP7B1jKShLdYUz2LQsoVGcj7aa4gp99h-aWou6-egh2JM5j9SjZqbfW2LeVfMZ0QpsgWStnOo20Lr06f9rozIWiVq6beBdkQ6OE-IaXbC7pcYcLO9vTHDOLaICAgEJZAxT2Mq4BEcrV29rt7HjdbfVtCxHR6eHrm_S9Y_If0U6ArI8mGuzH-EC2Actxv3fJ_DS37Uy_qRk13TKl-KOMWg5N-Qkl1353HbMjRvk0Ez4H8OnDaSQWOmGuc4tP82L_-q3yEUzI9nJgo8EGOjKceVAN0I09yhhJ6BAUgSNLEmdEHp1_iiU3h89N7_DSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-nRbb1Noy1pN2Jq8vl6fDyiY9omZokKLnNbASAsIivWz44GjG1ZtJcuI77uM0iWRTy0zPtaOAK7jwoIn0korQQpyw6yw6wQ0-Arrr45vSyRKQJCybMNOKphhmfrzEBIBW-cIandITMRJTPA9sI0wMArES48JTMaKyeOklttaFqQ4IW8i-IcLuSRhYqkJhyR8ZLVub1i4856Zw0NHCkKm0WyEDuHVNWNWjMY6nk-0qq29mHmGLkbj8xFIe9-H7lPiBeGGGjqxVL0xkr0LjlU8W5uAlt-MwXz2MGmoxdfHvCJoHCjJnPxd-3-zDV_MU6fAUfmmRy-rdCjHeLN0DPAQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toXGN9CpoAYbAU5Xdovu2_RhZIKqia-DnWmOUOvkHvlDT43M4jMDhmJBb9l4AP_nAUSfv-6c8SVAlcqg3TH8KKQP4JoAKESWvreHDTTMjJCpRWvgPfMmibCeOgKSUP1TtEkXWCUDhBm5W2tdOgxVmHcR6y0yzcsNXS2IHwQ-bS6OkDrRC7MUIEK_hP0X8ZEG2OYbCwN1mWiUot4c-WbCm9tYiZvZPyKLOogzKJX425M9484fahZeoI81ubUxqwDK42jQ2yrX0gk51yZBudGcoFLC35MwyE6JQ6y7KqpM-FBdQ_HLuUvNcJ9zwn6WykIjcB1nSiQt0j5qn7xovh4mJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTy8tSDUB7OqVxBQ3RqO_UqyUHpk-4CXE0Pf2emBXKEgJxkUfz2ck12W0-ajN49UuUu0a5ZAmmlIJk7D4pM40kEVXY1P1nnfjNz4OtASsAM-58ta385JV-U9KJ5Se1oVa61gQ-A4x__ivFPMmYJM3K-tWNBJjgJoE_G0u4P8TT7dz4KwEI9pfIuGM8RstE54eIe1nfUQRiH_zQKIwh81fOJZUOfrxBVHqCEc4SNWu9ebQC80n57Ff4eGvJlvaRkIMSRkauIPQIn0C-QZ5PTxrSuIWitS5KEd5D5NjqbA5YJ7vM9fnzz_R7NyEROCEgAqJ_Qz-kp-I1DOZbu0iFas_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URlgZMnijmgfVNXcvoG3tKaO-RPMQyDgC1aklo6TGt_RU1lfm8mY7fdu2LbCnqhkPU2iQE9KEGfsJoIp_Yk4zt-OkfdcvUey91v2ul7IL2wig_sBvKJwpcyHlArhgqYhe9cxlAIsBtRdgMMgEO78JonlKqgegQOeFB2oBxiSVI7dI2otMfTA8RdrpFeABBsL8kYZuWfETGdOOLq4TiMWVNMMSzOUHiP5adxDpOHaW50zSrSfdANGqOR3zXIczEIkqwneF_mF85ms5jW3LlKxs3NDUktGF0dn8mqTLN-Q_o3T7RFjxdYUkWWwnenuCEOyv6k2D7AodSpCcJuxX5fX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpT1eE_1b9dd7deMvoeY_hrh4pnCVmUKODFdhZG85aKD26c1_cZLKcVxKgk_Q4TTo_g_WLm7STz-i6oJWv74GIwM_s2qbP5L3lw6BecDQGIVi75TvbafLhaIc9qYpXjUGJ7DSUSWdvUNOSmtUAJ8Qm04FptYe-TKxhi7OaxNhjYzfXbrgQ91eDhpRQV6yMgJElx6L4-y_wBeBQJGLPmJXl1UCF4pf0Cdla1xABbMS6SeE47xlaWGPaJyoktPyho8MTjoe5L143yk1hq9On-LfWu0n1IMarahxbWz2Ufa6aTWHUB9wZJj11EEda8JTgO3eYDcEPwHFQ5XKKKGfQMmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg24_okXs4iyrEcv-XjXelPissCCjxNzA7ZIabuzKktP_16XFVh-RNEcX7Jc8K6dRDlS9KAsGuT2tJ90s_xpSToV3j504vkUNXHqOj0bqLuMbQfvc0Lr402HS6xQ521eFI8g0Le8rzBhF3LYZ05KbVG25FWfk0AYoPXWKrBIP7c2YpjsgizbQ6-Id9IRnUG0S8v5I-vD_IjGoqotYboPHrvTvJJze9CX_x5qskTDePn3E7ZPpQLrNkm7XlMN2MZdUrlcJs4zROS3DF7m3yFrtGnkq3kGljmqbIqc4xx8zwWZXfP9F1sPGBZuv6HdTV7QU0ZpLe88C8s7NwduInTMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
