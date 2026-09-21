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
<img src="https://cdn4.telesco.pe/file/e5yBaKnljrCZL8f-XmngXq-2B2E1Q0NSSzMSzE5PcZ8g1-NzrM1iZ3Y96Yt1J3sek7RqP1Vkw-ssWEioNf54qZ1zg17LrPuUz0R4NwCGduwQV3Ex-_IrpZE5Rw-83-Mt-zKp1iFM4VDdtWkbcWsOpOKOvZQgse7NURtVyPr_Vt9pweyTqO6dl3QYiPJhoQexCfTjMwcKkIaNPEWDD-WkhVA-axK1c4p95axa2MWypfRCVc_efsuCKJ22dvvj6VtpfywzR7Cr96YWMxzXmlJMzwCPntGV5fmr_rOHTnlqzMEnaozpICU_aiPoVw0l-zUCJJBh89_Ptb3mRGZXSx4GQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.02M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 15:01:28</div>
<hr>

<div class="tg-post" id="msg-691691">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddca2fcfd4.mp4?token=NMVIny6pI6uOEbjYBk998BphZILx1t2hD_1qqfvzFAcrbK6by8FSxTW-Q4ouUhNWDkdJhGGJXx8_DqCuANCTfiUjnhwsw2hht5Q3DV5-1fRlfmUyBUttI_g3eqkQYsSgOCqMWhZtsCujSjL-QYQ3U_c3McVaqM1v5MnIlJhBbHvGCsbhywIHz4dUSqgm2J7IZ86ZeTPtUaXjqpk7peCo6jazER4aGGCtgxQWNkWPxAK37mX48DKgyGfv-aqceS9IohuL07OfG_8Lxnvfawn-en1n_NKVzVZgi8FE2p7z11gwc6GzbgKmFJgd4_FYpi1eJXwgNL6ZTpT3VJvs14_hjBHyLoJmfGTkUxh9mr_UZrIccvZO4yJM73bii-woQ9oxZyn7fxgNrbhSOl3tY1RTxq1R3Zwkns8mViGDmL1HAJK3fD14-hBjiGqKjD7IHAM2FV3ktsk5_FWStudXqlztnV9s0bxzATTaFQFZIQ8WVYRhqtFJem0foGMjsilZQHz1O-hNKlkwS6l4elJ9hSZEaiQKlb3yvK8owzf_k61hiqOLOpykKf54HZZo7qAJ6FvjFUsMa8qfIt_iD63oCoGEvvS8Q2ncsUxlefdgIMH-D5uACq6byTk2K3ca4se5u5bM8-QvXzPc1J0M8bObpKk0nEtNkQtS_8cW9h6BCGFbX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddca2fcfd4.mp4?token=NMVIny6pI6uOEbjYBk998BphZILx1t2hD_1qqfvzFAcrbK6by8FSxTW-Q4ouUhNWDkdJhGGJXx8_DqCuANCTfiUjnhwsw2hht5Q3DV5-1fRlfmUyBUttI_g3eqkQYsSgOCqMWhZtsCujSjL-QYQ3U_c3McVaqM1v5MnIlJhBbHvGCsbhywIHz4dUSqgm2J7IZ86ZeTPtUaXjqpk7peCo6jazER4aGGCtgxQWNkWPxAK37mX48DKgyGfv-aqceS9IohuL07OfG_8Lxnvfawn-en1n_NKVzVZgi8FE2p7z11gwc6GzbgKmFJgd4_FYpi1eJXwgNL6ZTpT3VJvs14_hjBHyLoJmfGTkUxh9mr_UZrIccvZO4yJM73bii-woQ9oxZyn7fxgNrbhSOl3tY1RTxq1R3Zwkns8mViGDmL1HAJK3fD14-hBjiGqKjD7IHAM2FV3ktsk5_FWStudXqlztnV9s0bxzATTaFQFZIQ8WVYRhqtFJem0foGMjsilZQHz1O-hNKlkwS6l4elJ9hSZEaiQKlb3yvK8owzf_k61hiqOLOpykKf54HZZo7qAJ6FvjFUsMa8qfIt_iD63oCoGEvvS8Q2ncsUxlefdgIMH-D5uACq6byTk2K3ca4se5u5bM8-QvXzPc1J0M8bObpKk0nEtNkQtS_8cW9h6BCGFbX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: علی لاریجانی چند ساعت قبل از شهادت، افطاری مهمان پزشکیان بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/691691" target="_blank">📅 15:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691688">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXS-6dZDu9Np8SJBTuAHRkjUdq2CFQqRucX6H9y8h-mSBNkBQoeyCTi5QTKFl09ubdYpn_MXF-pGryHIh25yIRZ3jNGT76xd4CSH6hkYdSgQs9CDRsj9cqKLRBZmhHPgWTEUozQFjJcSSJhQwNKk7lqosHsUmxCQseellPpP-YJzN6rWrNZf1VwiIk0o7Cc6_fqHyaSgcMbEYf5UN_WqXuYxyn04FSL0-JlHt_jM_4uQgPvL5io_1uuli59USymiEU8IfbbT-H5eVm9IE2SSG5nwFbpXFxlVphLLv0cX6wTQszg4wI7-aycHdHydv-b2REicbNuvSr8KqZrbBJCR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4RZZgjJY9dj9vrPswR9yE8riYGCJsAurabfFktazg9w4I_3y8FMIKZFpnR3Br9HVat7cemV9XkqM0mlG3mxXS6CvtpFH2I9-dZMSAKcWV3m07wYRqtszwQiBCjte-cGqcwQyzgtETvEIYA9j5-_wBOBcRh_5R8M6ZL8e0nLUVhoCeRfwBUbx_0xvkcQhp5wu9vkVkCqboDBb7D5dgmFD2520x8r3FnZBweqncMncRDij_TiiGn7699_5ujf8aNITUKLGxPUlblKRLcUT4-4noOoWGuiFupNqTbHcttsaXUTW1Yg51wzA3rh8sOhj8XvvjBO2B7Am56j9Ga2D6LDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6OwC_1YtGx7emKo7tz9LrlsIuToEFjxHZhqmMzXplDyiMcW_zjzLpWA1hEtJzXCZ39lC92r0-9CSpZfr7Okg8kpUxUslTLpYHzH7ZhCB6_enpUkT9a_3Nmn2gatDlJwtjpeVzu2JubWdVxlXmDW1g99bGCbZsdmhDWpT06xy6gyK-8_tk1hx4_vAhQcGOagbKZHgJApO05glYKxm05-gXcqSEyDT5MILCTHT442CJTYIg2fi8LsgB55zIi86NvWUO1CEz7IM6HP2w4nn7iKxdWa6aNr18CyMMOCt1xJKnroHIjQq2s6q_Um5HDtEoApdYZG5BMvi2yBXlQTs9tBHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از یک پژوپارس که برای قاچاق مواد مخدر استفاده می‌شد
🔹
این خودرو که حامل موادمخدر بود حتی با شلیک پلیس به لاستیک‌ها هم متوقف نشد و راننده با رانندگی روی رینگ به حرکت خود ادامه داد تا وقتی که با شلیک پلیس به راننده متوقف و ۳ کیلو شیشه از این خودرو کشف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/691688" target="_blank">📅 14:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691687">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
پزشکیان خطاب به دانش‌آموزان: بچه‌ها سلام! می‌دانید که شما گوهر هستید!
🔹
آدم، مفت به جایی نمی‌رسد؛ باید تلاش کرد.
🔹
من از یک خانوادۀ معمولی به اینجا رسیدم. شما اگر ذهن‌‎ و فکرتان این باشد که بهترین شوید حتما می‌شوید. ما تلاش خواهیم کرد که شما بهترین شوید.…</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/akhbarefori/691687" target="_blank">📅 14:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691686">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
پست سردار آزمون در واکنش به دعوت شدنش به تیم ملی: خوشحالی امروزم مثل اولین‌باری است که دعوت شدم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/691686" target="_blank">📅 14:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691685">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بازنشستگی رونالدو کنسل شد؟!
🔹
نام کریستیانو رونالدو در فهرست جدید پرتغال برای بازی‌های پیش‌رو قرار گرفت؛ این در حالی است که شایعاتی درباره خداحافظی او از تیم ملی مطرح شده بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/akhbarefori/691685" target="_blank">📅 14:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691681">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFwy5WNzC2XSKeJwO3YH5mrh_clVFJGQcLgIpJ2f1nF-I2nzIE8t8XxaZnykaPAG3DGnwjiw93-wB256HLjZIpOY5NSmsYXx0ms-yJx1ZirRACn8nQSuFd861YZ8BMeCr5NhPr5sR9uYIbegFZEaI32eKEHSU70uMFcDp98GVgdCkodYREtFR8BMvpAs3k-Z01m9LtJLQfdUpzc9GcXm6T_S1XCbjFr_Qywv8GK97VhUcwnYfi3UTGaTmgbkEakKNm1FRjhcY5BZsTQfWIhun29OTobyoGAOfREth845-nioK5Exc0fwfv881z4GmgHDsOZNrlHqRGf_zh99iTe-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s4Qn93HcqV7PGCFRBwYd8AlAyVp577zdm2hkLaNpjmHfInXs6E6ZPn2aV5ctJCBqj3if10iS7jmnzlnLlvepJygAy-twV_e6yrMO897h0bBFU32HBduGLf2CmQv7_8Hu78vKekFFlznOCwh6iqjkXwbro0FblxGQs7QdUEIQ43Eb3bgcF5-DSNCyZPKDGEScvpcDse_wGU1gQEDJobBQnOxocCDuNFDKb83fSGXujZpCsAZsjiwdflFXnu554T5YGPjefu2-A0bu0Asq6CDKCnOB29z2FNaJIE8OsDxHTHroNCLkaa_JSoUnXkEZmZ084tMtQAPifaOqIVBQ0LM1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owQhW7mqVgTdVHUNQh4C3btXZZO6R3iWPs5K8itlXSc5xPBc-1PDhAYEQfUY-CA9-VxIQIurnTq-gAodYZJ0qKXKWOKrkPTM_HrCid0eFuvlS4eczoIRqEvImtZOuezZuIrV51KhBDRABTYGLPR5TaBQ5TNNf-VKcNPMaT1w63Lgvlf0DqPsX7Dz7ChI4gbyKguNUosDcU0sdQdMn9FyJureSvNCvg4imHjgK52svMjTVU655TFwxYovxh7_jWSilmnY3R-lh9wz_hfJcbyszhrJ-R8LYUKwTViD5zsD_J7_OgG17gNmY85ffUXZYnj5p-wwECVszAs9uZLwkXadBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/As921LqzIjKrQXgb93K-X0tebX5w5Y-SloKpFbbgdrBaZGUb97gjh-e9Ju_KSKX3XmIQ2OcKz1JS7CsXqJkArYKzg38lno1rluE7-_IHKTW2dG6FJxn9C8eOfY9UiRqsPpIJkdslWhey07EbC0Ssv2KqXTJVbylSyczHQbayC-Fb-l74Vc850IUFpElXlKcryyx3s-GzD0n9DH2yHBg5JtIGScD6EC5mzgPUlgiIJs1kQx2LauPoLPU67N006MLrAgxqoi_RYRhFYHXgD2aGWhOjvh1eQWm2FJu9CWObk0O2ZCnWpxn1ttBCo4xsq4vzQMPO20szDRkNRWJgjp7L4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نگاهی به خواص درمانی میوه‌های محبوب
🍒
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/691681" target="_blank">📅 14:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691680">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96c752487.mp4?token=Xjl2qN-OvJ2HbtA5AhMpZByql8pWebRm8APeJ5qe0PBmG9U0021XXAc4iQrXIEzhvvPdFvCxK76JFEPuNDwNUjd7CdS40bhCewMWnrvbVD0PJJfr8i9Fj8__J5B1ZUIcDud3y0pHec_8okqVE65eTh1ppy4C4r74_Hv2KgVZ2Q-JuvJjXNyfFJUap20l8gHnpVdp0zcfFdhTIiipa_T2qQjzAe4Y9vUBfx-4MYvfZ0n9sC3WC0vzzbOIpXRAiraD_MekGkuHmmR8Cmv2OY4TCBRplF9LBJ2GZqHw0c2QSQIylMGrPryHf10hG8PpnFuong_l84QByzVKAzJdwiR_0Y_9BitesrAsdUh5z629fFOMXmcDH33jZAMed5cnIGZuOF_U3CqqZEc9qUHxQVEdygY2MPTaECDOsNr8IN_bRFkR9C30L7oqnCkI4KXrmZAVjkY1IbzUrKsqLRy5hbrs6NskzNnOIfjmGJcfG5KJwZmu6J2wXiHzqzH_nRO_FdGHPKA2b-mZF1qPJ9LD3dP116yS5pHAzuGz83fDQse05rW3a3k9s0bG4XWhS0DPKetx7zNZjXC7kLCwXgTgVhGZMDdjzF3p9yHzaRd9P_eGjwqjtVUfI6ITSNUPSx2Pf-qGpUzf_2fJZ4ADxK1YQZI948kfUpEQSYw_KL71b_CS1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96c752487.mp4?token=Xjl2qN-OvJ2HbtA5AhMpZByql8pWebRm8APeJ5qe0PBmG9U0021XXAc4iQrXIEzhvvPdFvCxK76JFEPuNDwNUjd7CdS40bhCewMWnrvbVD0PJJfr8i9Fj8__J5B1ZUIcDud3y0pHec_8okqVE65eTh1ppy4C4r74_Hv2KgVZ2Q-JuvJjXNyfFJUap20l8gHnpVdp0zcfFdhTIiipa_T2qQjzAe4Y9vUBfx-4MYvfZ0n9sC3WC0vzzbOIpXRAiraD_MekGkuHmmR8Cmv2OY4TCBRplF9LBJ2GZqHw0c2QSQIylMGrPryHf10hG8PpnFuong_l84QByzVKAzJdwiR_0Y_9BitesrAsdUh5z629fFOMXmcDH33jZAMed5cnIGZuOF_U3CqqZEc9qUHxQVEdygY2MPTaECDOsNr8IN_bRFkR9C30L7oqnCkI4KXrmZAVjkY1IbzUrKsqLRy5hbrs6NskzNnOIfjmGJcfG5KJwZmu6J2wXiHzqzH_nRO_FdGHPKA2b-mZF1qPJ9LD3dP116yS5pHAzuGz83fDQse05rW3a3k9s0bG4XWhS0DPKetx7zNZjXC7kLCwXgTgVhGZMDdjzF3p9yHzaRd9P_eGjwqjtVUfI6ITSNUPSx2Pf-qGpUzf_2fJZ4ADxK1YQZI948kfUpEQSYw_KL71b_CS1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افسر سابق پنتاگون: آمریکا توان سرنگونی ایران را ندارد؛ تنها راه خروج از این فاجعه، عقب‌نشینی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/akhbarefori/691680" target="_blank">📅 14:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691679">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کیش و ماتِ استراتژی پنتاگون؛ بازی خراب‌کن آمریکا کیست؟
🔹
از تحریم و انزوا تا فشار نظامی؛ آمریکا در برخی بحران‌ها پله‌به‌پله پیش رفته است. اما یک‌جا این نردبان تنش به مقصد نرسید؛ جایی که محاسبات آمریکا به بن‌بست خورد.
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/691679" target="_blank">📅 14:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691677">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
وزیر ارشاد: ممکن است در صورت آماده‌ شدن مقدمات، نمایشگاه کتاب به‌صورت حضوری در آبان برگزار شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/691677" target="_blank">📅 14:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691676">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای رویترز: کمبود جهانی گازوئیل احتمالاً تا سال ۲۰۲۷ ادامه خواهد داشت؛ ذخایر رو به کاهش است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/691676" target="_blank">📅 14:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691675">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
شبکه عبری کان: سران سعودی درباره نحوه مقابله با انصارالله یمن دچار اختلاف شده‌اند؛ وزیر خارجه عربستان خواستار راه‌حل دیپلماتیک و وزیر دفاع حامی اقدام نظامی است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/691675" target="_blank">📅 14:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691674">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgfm7W1oog1D_fn4dAJOyFXbpNcUtWYO-k1TaKvhfg5IFx0pZUzTjmnYo_DxboU02-jidEy5Pnxe1M2WzXqBNOTKt7xKWZohwSZAyUFiIYPrmRe17x-uApWE725dCUXF6djYLUobZR2IC-tLIirlZMkhKum1LRg8O99eed2M2oxbmEGmwE1vzzKeYmvcyKBhicNhOQ1Qoz_ZYcl9thvkWZQ8d363WVff9Aknijn5PY_i7p_rY1F-iydIpqUHoQdv3HtDcrXkzClNx5KCf1fXTMuUC1Cadib2C9l1dq1hxdAMmz3hXAPO58jRHiDtweWs6dk__jgneGRGFE8KIBxYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست لژیونرهای تیم ملی اعلام شد
🔹
علی نعمتی، محمد محبی، سعید عزت‌اللهی، محمد قربانی، مهدی طارمی، سردار آزمون، دنیس اکرت و شهاب زاهدی هشت لژیونری هستند که به اردوی تیم ملی دعوت شده‌اند.
🔹
قایدی، سامان قدوس و جهانبخش، غایبان بزرگ این لیست هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/691674" target="_blank">📅 14:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691673">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای الجزیره به نقل ازیک منبع در وزارت کشور پاکستان: محسن نقوی برای گفت‌وگو درباره تلاش‌های میانجی‌گرانه و پایان بن‌بست موجود به تهران سفر می‌کند/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/691673" target="_blank">📅 14:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691672">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNXXs7vU6aqnk-DbtxfarptrJ7JlKCDn19OlGMrTk5TWwn6i6KCGK2ZmrQOP5Ez8oPgiJ7HDZzx-DUroVGvgoY_W_K2gkTf56O7EBi294USLlynQ_Ac98oTCnudUBdUFXHLbfuszHOMUXnwq8DthDc6GnGJJp2zePzecPivQdTj_yxxGiD-knlTTfq64qKV6ICWeOlk3MGG1XleO7r50zVzoPNIyvzuKhjdZdyHz9RsUwTl8_TJ6J8BYBXQ0K9LqD_ZkOkwdKl65_GUD6otLgQvYK_xonjidNRyg_oiiW4KTxxxzwAjrTP083Q1NVhlkrEoW5nAg5pQl-3pjoIGX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حضور بانک کشاورزی د ر IRAN AI 2026؛  گامی در مسیر توسعه بانکداری هوشمند
🔻
کنفرانس و نمایشگاه «کاربرد هوش مصنوعی در صنایع و کسب‌وکارها» (IRAN AI 2026) با مشارکت بانک کشاورزی و به میزبانی دانشگاه صنعتی شریف؛ با حضور مدیران ارشد، متخصصان، پژوهشگران، شرکت‌های دانش‌بنیان، استارتاپ‌ها و فعالان حوزه فناوری آغاز به کار کرد.
🔻
مشارکت بانک کشاورزی در این رویداد، گامی در جهت تعامل با زیست‌بوم نوآوری کشور و بهره‌گیری از ظرفیت‌های هوش مصنوعی برای شتاب‌بخشی به تحول دیجیتال و توسعه بانکداری هوشمند به شمار می‌رود.
🔻
این رویداد تخصصی روزهای ۳۰ و ۳۱ شهریورماه در دانشگاه صنعتی شریف برگزار می‌شود.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/691672" target="_blank">📅 14:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691671">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1b70ad80.mp4?token=AF22bweI2y1fPBhYe-N1sB98QcfrwyB3ZYKVKbyWkzRZECydjZxuXRUKtTHOPmfcmpI46a7geSYbrDF6kdj7ku7VS1Xh53VXW8sRU1Z7W5iIVCmjgOAB8njGHMDlb3wWmZJrfIZ0A27MvY3mIPhf6J9zssg0PXsiLK0vw35F3BXuKQkFPJ2QGw-5lEXTbOaHXGdHPlQaevbpayeEvlYpKcSCXUg7tRMw_VI0-BDFkpt80VAxV2G2f0Z4yGPBNlB-pmcrzRNxUfnjBu1UqnF_SsUKNyuL5nuZdtCuYQURGPxB0V64zHecQTaND2nIh2IfJU66yZnkBVvNm6i0nnICvl2T-L7druJHEyTLg-1asXpg4Qz8YYLIMDRPMXcFYP3UxUim3nZYN6RnH-Csn_4xSrC4jyAZvLzW5LKO0SHAK6xkFZigO1lgi-2VHxFm1oyNfi1iRxyf0ecT4udha20iaD4-pwHO2BDE1e0u0nAQ24WGFPGxnaGDl9sTRaVPDJgJZDfOapMclQTIidV-vCGYddHC7eQNDNQHFRvFyhiHa598WpeFhFXmFj4a0pb-rTDb0osPxsn_IP0OGE5f-nN5kn4eeG4pOeogbuqu0vDb_skWrmk2elQ2bo4puqkt9jiwlUHELuw-E4XeXvHzBaF9SHCfQM_FjwIkoVQEjCERFY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1b70ad80.mp4?token=AF22bweI2y1fPBhYe-N1sB98QcfrwyB3ZYKVKbyWkzRZECydjZxuXRUKtTHOPmfcmpI46a7geSYbrDF6kdj7ku7VS1Xh53VXW8sRU1Z7W5iIVCmjgOAB8njGHMDlb3wWmZJrfIZ0A27MvY3mIPhf6J9zssg0PXsiLK0vw35F3BXuKQkFPJ2QGw-5lEXTbOaHXGdHPlQaevbpayeEvlYpKcSCXUg7tRMw_VI0-BDFkpt80VAxV2G2f0Z4yGPBNlB-pmcrzRNxUfnjBu1UqnF_SsUKNyuL5nuZdtCuYQURGPxB0V64zHecQTaND2nIh2IfJU66yZnkBVvNm6i0nnICvl2T-L7druJHEyTLg-1asXpg4Qz8YYLIMDRPMXcFYP3UxUim3nZYN6RnH-Csn_4xSrC4jyAZvLzW5LKO0SHAK6xkFZigO1lgi-2VHxFm1oyNfi1iRxyf0ecT4udha20iaD4-pwHO2BDE1e0u0nAQ24WGFPGxnaGDl9sTRaVPDJgJZDfOapMclQTIidV-vCGYddHC7eQNDNQHFRvFyhiHa598WpeFhFXmFj4a0pb-rTDb0osPxsn_IP0OGE5f-nN5kn4eeG4pOeogbuqu0vDb_skWrmk2elQ2bo4puqkt9jiwlUHELuw-E4XeXvHzBaF9SHCfQM_FjwIkoVQEjCERFY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تست ایمنی فولکس‌واگن؛ آزمونی نفس‌گیر برای سنجش ایمنی خودرو
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/691671" target="_blank">📅 13:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691670">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bda6f6e69.mp4?token=iyVVqD3QQZ1LZaBTfw02CF0UzMQAbNUJ2Jl0U3K1US3M6-tdoiCDZbC_ykD4ZqnZDvvGYq-OJn7uTl9MSbpkPC4p2VKrHC89Xuy-jPyDWiZYjj5mtmCcVeBOQXCWprSU4AMhdJ6mPxFSpJuHTP4GwRoqlGVYammREfJXDwIMJnVZBTcfa8gwD4iSTjXARm2jZCRL3MXUbKyNUcQUZpLFhLm0Wst2gNzYdn0puAfPjAmRaxHssivSip98OlkJDPXwvzw6TwKt9Fu5Ze1MxZzCqXRSWvXsdavgcNF5ekFSEDQcs3NpHZ6Sx3H-zU0qkd3o3yUdvJJ7KjF9KdS4tRnyzoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bda6f6e69.mp4?token=iyVVqD3QQZ1LZaBTfw02CF0UzMQAbNUJ2Jl0U3K1US3M6-tdoiCDZbC_ykD4ZqnZDvvGYq-OJn7uTl9MSbpkPC4p2VKrHC89Xuy-jPyDWiZYjj5mtmCcVeBOQXCWprSU4AMhdJ6mPxFSpJuHTP4GwRoqlGVYammREfJXDwIMJnVZBTcfa8gwD4iSTjXARm2jZCRL3MXUbKyNUcQUZpLFhLm0Wst2gNzYdn0puAfPjAmRaxHssivSip98OlkJDPXwvzw6TwKt9Fu5Ze1MxZzCqXRSWvXsdavgcNF5ekFSEDQcs3NpHZ6Sx3H-zU0qkd3o3yUdvJJ7KjF9KdS4tRnyzoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان وحشتناک شن در جنوب الجزایر، روز را به شب تبدیل کرد
😱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/691670" target="_blank">📅 13:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691669">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEVnS6csDv8Ocd-WqkWiJ_-UCUVLCDjjx0FEhChBE1wMHkiVDHs4NSSu94JpVqIjgH0omqjlG-84lJS-5x-1zsBTiONDZmFtE8PGRLVqt9XYeYGqSxn8BwQsFqEW52YC2ysAFryNk72S9NbaceP0EdxdjDIVSj9mQXae4cVcBQSBYzwobBlQMhlLUacQ3uWfhKA2V09H5QUD6U94t9iDzeWno9VmgNIBlMkhd-o8NJjoDyStBEJpdhjncsHXIeXuauKTdq7b5j_1C4UHjQzYEIQMYgU5pVg3BthyGBj5MFzWh8P5Z8cfdU4Hya6J32Yjr7IoeeNZ7HkEZojExfNJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/691669" target="_blank">📅 13:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691668">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
آموزش مهارت‌های زندگی از کودکی در ژاپن؛
حتی خرید کردن هم یک درس است
🛒
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/691668" target="_blank">📅 13:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691667">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLGlNGwiTCh5eNfNADVNFKmnkjq_CnrOxxYXeGKg3vAKjQdYsyl0d8q6qe98RYc69raX2JUTdwHAltdj5KFjnXezQRVGpbDmybYq6vz5mWaIP6OTvogIESNXJ6ZRDffDtmspSyNWroWq0UxRX48oB3fSMpgeYOXKbOABN78_lwKY_9hfCVkWyEwQm9BwfJcNhrbrzAzYOgXHPRwVfopcViFVoqpwe6xRqPkp_fylmQ2pvTn5AtjOk3oxNAW1CmvoAiCe28MhJ9NoiWEKSNyRtxkRVXp3V6B7bKPI0XJfcm50qeVjWsepyppt2BDjPkg0feDAQghZD4blJxmfglCj6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت سکه، طلا و دلار امروز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/691667" target="_blank">📅 13:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691664">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b630b6a5d.mp4?token=JB_WqeynRnVXXPEfpJ8w02LJyN_AoIBO3U3VaXB810-USCew4nXMnsvAwzKLZNm1Xpf5eJ81_tZACiVXmPz87qaS6cpHRCEBbyVszTnlmYtSjqSbD_3KwkWLr6g46ksTwnZ86bTmiEB5LulPaigvyoo9Zp5XXV1rMgBsGe5DuiBL711h36zQtvbez0OUXJWgp51XdtyH0z2LzwqnmpXj9HHua2Ody8NGRQlBNQ1ro-nZikXb6XzNnC9vqL9_i4-3ybatXzXJe1W3H8qaX5O2a_GU4yUxoKNR8zhwe7MRJKSCBqekI6QR5iXMrOfG_L7lGCa4oCQ3erveWhM-1-wpkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b630b6a5d.mp4?token=JB_WqeynRnVXXPEfpJ8w02LJyN_AoIBO3U3VaXB810-USCew4nXMnsvAwzKLZNm1Xpf5eJ81_tZACiVXmPz87qaS6cpHRCEBbyVszTnlmYtSjqSbD_3KwkWLr6g46ksTwnZ86bTmiEB5LulPaigvyoo9Zp5XXV1rMgBsGe5DuiBL711h36zQtvbez0OUXJWgp51XdtyH0z2LzwqnmpXj9HHua2Ody8NGRQlBNQ1ro-nZikXb6XzNnC9vqL9_i4-3ybatXzXJe1W3H8qaX5O2a_GU4yUxoKNR8zhwe7MRJKSCBqekI6QR5iXMrOfG_L7lGCa4oCQ3erveWhM-1-wpkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا به ایرانی بودنم می‌بالم؟
🔹
حرف‌های شنیدنی حمید شهرابی مسئول تحقیقات خانه آمریکای لاتین در تهران. #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/691664" target="_blank">📅 13:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
بیرانوند: اول سربازی، بعد استقلال!
🔹
قراردادش را با تراکتور فسخ می‌کند و از نیم‌فصل دوم برای فجر بازی می‌کند. او قصد دارد فصل آینده به استقلال برود؛ جایی که محمد خلیفه را هم جذب کرده و رقابت این دو دیدنی خواهد شد./ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/691663" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: آمریکا تاکنون شروط شش‌گانه ایران را نپذیرفته است
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
تحرکات اخیر آمریکا و هشدارهای این کشور درباره احتمال لغو پروازها و بسته‌شدن حریم هوایی، لزوماً به معنای آغاز یک عملیات گسترده نیست و اگر آمریکا اقدامی انجام دهد، توان آن محدود خواهد بود و نیروهای مسلح ایران نیز از آمادگی بالایی برای پاسخ برخوردارند.
🔹
آمریکا تاکنون شروط شش‌گانه ایران را نپذیرفته و ایران نیز بدون اقدام عملی آمریکا وارد مذاکره نخواهد شد.
🔹
تنگه هرمز و باب‌المندب همچنان بسته هستند و ایران بر ادامه فشار از طریق این آبراه‌ها تأکید دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/691662" target="_blank">📅 13:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691661">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L49alU10fmipaEOba5W61z4fbMJ9n8QFuKHGxU32EULs9u3v4QUL12-VVSRGdlgA4F_7AzxBsibjIaHV57vUPxhN9DUDfEZot3IN0Dqt7LXVvxtXZWroVOzJHnqq5TUKkU0kLVLFBDAn2NL9urlsCpCqbfsyBLfbUbsv6f8ZUhSmIBoW8DXG8ti-3j1_IMA8OWRk8OKaVy1jrzO7fq7UXqSZWbBZsu2J2Osm8d0iVT2k8wbtzu2D_Qnf1RngZR3EvFNfv-jkqJ3ciYAgzSNr69s2ozjhGEZ36ZellBzDV-7mYf1uuthM2TSouGMqpeijFnHprp8ITzO6jRZrKJZxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مسابقه تلگرامی هایپراستار با کلی جایزه
💰
به ربات تلگرامی هایپراستار بیا، رکورد خفن بزن و
بدون قرعه‌کشی
جایزه بگیر:
1️⃣
نفر اول ۵۰ میلیون تومان اعتبار خرید از هایپراستار
2️⃣
نفر دوم ۴۰ میلیون تومان
3️⃣
نفر سوم ۳۰ میلیون تومان
4️⃣
نفر چهارم ۲۰ میلیون تومان
5️⃣
نفر پنجم ۱۰ میلیون تومان
💚
به همراه کد اشتراک یک ماهه
فیلیمو مدرسه
برای تمام شرکت‌کنندگان
شرکت در بازی
👇
@hyperstariranofficialbot
@hyperstariranofficialbot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/691661" target="_blank">📅 13:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691660">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
اداره عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که اطلاعاتی درباره حادثه‌ای مربوط به یک نفتکش در حال عبور از تنگه هرمز دریافت کرده است/ الجزیره
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/691660" target="_blank">📅 13:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691659">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9248c71c9b.mp4?token=Q9zYTfdDwBRCYE0PKTRs-n1AlwB7Y1EmjYQnE2nZzuqiTO_7B43O2fMQDi-hHYefERgbmpOJ0aDgtQ1aDPb_PzUOIIcqy-eaJs_WcPa331A0y9oh6vXk7LczVvKyc6Cqkql2Dd55A-CgIMU484M3JP6lDJ69Jjz2aUA_6HBkSwL0otBWoEVEtxRPGOqptYYOIRDLO_1--b6OkgXqhNk8e7zlAe5c3RXJlJCzoFl5vFa-wjn8OYL5C6MLAka0U4HqvtTFKeUROJqR2nuoTkzdxF8cPHTOPlN3DkI4nkoEkZxDVm3YmLK5DAsKgz8IdSYRSCMefakxnFyHJqLLf6NDTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9248c71c9b.mp4?token=Q9zYTfdDwBRCYE0PKTRs-n1AlwB7Y1EmjYQnE2nZzuqiTO_7B43O2fMQDi-hHYefERgbmpOJ0aDgtQ1aDPb_PzUOIIcqy-eaJs_WcPa331A0y9oh6vXk7LczVvKyc6Cqkql2Dd55A-CgIMU484M3JP6lDJ69Jjz2aUA_6HBkSwL0otBWoEVEtxRPGOqptYYOIRDLO_1--b6OkgXqhNk8e7zlAe5c3RXJlJCzoFl5vFa-wjn8OYL5C6MLAka0U4HqvtTFKeUROJqR2nuoTkzdxF8cPHTOPlN3DkI4nkoEkZxDVm3YmLK5DAsKgz8IdSYRSCMefakxnFyHJqLLf6NDTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحکانه نخست وزیر قطر: ایران صلح طلب نیست!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/691659" target="_blank">📅 13:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691658">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
لیست لژیونرهای تیم ملی اعلام شد
🔹
علی نعمتی، محمد محبی، سعید عزت‌اللهی، محمد قربانی، مهدی طارمی، سردار آزمون، دنیس اکرت و شهاب زاهدی هشت لژیونری هستند که به اردوی تیم ملی دعوت شده‌اند.
🔹
قایدی، سامان قدوس و جهانبخش، غایبان بزرگ این لیست هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/691658" target="_blank">📅 13:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691657">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
اداره عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که اطلاعاتی درباره حادثه‌ای مربوط به یک نفتکش در حال عبور از تنگه هرمز دریافت کرده است
/ الجزیره
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/691657" target="_blank">📅 13:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691655">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
کاهش قیمت طلا در پی تنش‌های ایران و آمریکا
رویترز:
🔹
قیمت طلای نقدی با ۰.۵ درصد کاهش به ۴۳۵۴.۳۰ دلار در هر اونس رسید؛ قراردادهای آتی طلای آمریکا نیز ۰.۸ درصد افت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/691655" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691654">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVZs-yUpdUjHzUlw3e7doKdw4tNCGbq9vGikpAm6jyZ7muXH6e-OTgb5X9aU-bO7XQzG0joQE2TSWo3uVcAEDB1E_NYIO1IzlP3ztxALiCiqyN8bwZeo4H6gpKobtl4vyssUwActtXVqdhHfreSl4zU2yr_CUQ7GIPKCxm7ZkzY1twtWea0IMkGimihsjo38nFFSYg8ASnb75-DEwmrzfArTu1IbWz9VmTL-9fsXjmVECehyyOuPCqWLKNxSlZ_6927-fI8elQJ_4JJZE9YxY2y2EWXbIydXc1ZQ4jg0Q7s88MelQQsxdAwYc8X-3PM-ODBxUj8YaMD-K9VodesF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمایت نوبیتکس از صعود ۵۰ دانشجوی دانشگاه شریف به دماوند
🔹
۵۰ نفر از اعضای گروه کوهنوردی دانشگاه صنعتی شریف با حمایت نوبیتکس، از سه جبهه مختلف به قله دماوند صعود کردند.
🔹
این برنامه با شعار «بیش از پیش» و در ادامه فعالیت‌های مسئولیت اجتماعی نوبیتکس در حمایت از تجربه‌های جمعی و جامعه دانشگاهی برگزار شد.
🔹
این صعود، پیوندی دوباره میان نوبیتکس و دانشگاه صنعتی شریف بود؛ پیوندی ریشه‌دار که یادآور سال‌های ابتدایی شکل‌گیری این مجموعه توسط دانش‌آموختگان همین دانشگاه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/691654" target="_blank">📅 12:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691653">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5d47a6c0.mp4?token=EykrBByDMYhWrzDrGexoBVh1ZUy_FTtRlDeC4smzlXayGDMDl-4UGnqRh46ba_RlVA3x72JHl5MjeGp9c-4I7PXIVzLDvvCWoD-5gFljuOiDB5rx4zTmU-oVyCW-clw0lW-DhWY_V7Ss43t681Y9hT69VBOTF9RFUCXppg4rIXga39SF78kTlXoJKzByWlJ5Iyz-s_61GksPbPo1fOWHR8HksKNlqa6MDV2y1AtZHgVr_uMZUWz3HSNtcmofDMfO5UjJhX60v4IjnFMq_Gq0z_scvxREcoGnBWEPYFTiVF7-zW5PJIGBjy8e2lfvdUVq3xSUMvlVW7DTAa4rY4haL0lDK_UG8hkMJD9JgL-4eNu_jGH0PEX-SYmoMcQs4BChHKWpItWTtBJTT24G3R4ZlnRnE4Inj3x6REKf8QyyXTJiZa2cpwAez-pZQIheB6TPkrbZKEEzpTMOwHm6N2rdTVu9fUYyAVq2CipkBAH9o2KeZGwBCVNPhdKNwOHwt4oMhbB7Zjm0mkDMjZkLDFw2PZGWtTR94RsBB6jmgh--j09oOqJB0N_UYw6luP1tMfODRLj58rqhAwLauyH0BZZDe8uECzcWOhIPBg_7syZeSRRfSBzm8P6WBVU_zjEeGBLZcT8btcqNLXT9ZFFRjOZ9CrXHD_x5FqlTIUBrGuUzpmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5d47a6c0.mp4?token=EykrBByDMYhWrzDrGexoBVh1ZUy_FTtRlDeC4smzlXayGDMDl-4UGnqRh46ba_RlVA3x72JHl5MjeGp9c-4I7PXIVzLDvvCWoD-5gFljuOiDB5rx4zTmU-oVyCW-clw0lW-DhWY_V7Ss43t681Y9hT69VBOTF9RFUCXppg4rIXga39SF78kTlXoJKzByWlJ5Iyz-s_61GksPbPo1fOWHR8HksKNlqa6MDV2y1AtZHgVr_uMZUWz3HSNtcmofDMfO5UjJhX60v4IjnFMq_Gq0z_scvxREcoGnBWEPYFTiVF7-zW5PJIGBjy8e2lfvdUVq3xSUMvlVW7DTAa4rY4haL0lDK_UG8hkMJD9JgL-4eNu_jGH0PEX-SYmoMcQs4BChHKWpItWTtBJTT24G3R4ZlnRnE4Inj3x6REKf8QyyXTJiZa2cpwAez-pZQIheB6TPkrbZKEEzpTMOwHm6N2rdTVu9fUYyAVq2CipkBAH9o2KeZGwBCVNPhdKNwOHwt4oMhbB7Zjm0mkDMjZkLDFw2PZGWtTR94RsBB6jmgh--j09oOqJB0N_UYw6luP1tMfODRLj58rqhAwLauyH0BZZDe8uECzcWOhIPBg_7syZeSRRfSBzm8P6WBVU_zjEeGBLZcT8btcqNLXT9ZFFRjOZ9CrXHD_x5FqlTIUBrGuUzpmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک معجون فوق‌العاده مقوی که استخوان‌ها رو مثل فولاد محکم می‌کنه
🍹
😋
مواد لازم:
🔹
۵ عدد انجیر خشک
🔹
۷ عدد بادام درختی
🔹
۱ استکان گلاب
🔹
۱ قاشق غذاخوری پودر سنجد
🔹
۱ قاشق غذاخوری کنجد
🔹
۳ عدد خرما (اگر خرمای دانه‌ریز مثل خاصویی استفاده می‌کنید، ۵ عدد)
🔹
۱ لیوان شیر…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/691653" target="_blank">📅 12:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691652">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd9b485f6.mp4?token=lBV72PwxGxvXQUHN5AjvfzqtQtOn2sO6NGXswaHAYf12tTZQRVpb6q1dBxOAETsijScvZaSm3APAGAzan0TecgJwCmFVXWLyIwd1AkV1BXhZGKE8osDWyfq4hz-MtTqOdJU1g1RqJO4VtDsIhoIUIykK9NFFmand5t5RcyuDBkcv4yNUZ2xPCVzC2TdKjwgNO5L8_ZVDhPwQToIjrprqoMnilnpHKHdX99OeQyRooR13yN8aZZsLIpyTSE6czes_KzXgcvuOVjZxtFWCWsBMZhAUxmQGlwh-mCa1TFHhyi-WWu8qXrhAJIxp7tLehRwIKzKqheeeRYD0cM7LH5kQag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd9b485f6.mp4?token=lBV72PwxGxvXQUHN5AjvfzqtQtOn2sO6NGXswaHAYf12tTZQRVpb6q1dBxOAETsijScvZaSm3APAGAzan0TecgJwCmFVXWLyIwd1AkV1BXhZGKE8osDWyfq4hz-MtTqOdJU1g1RqJO4VtDsIhoIUIykK9NFFmand5t5RcyuDBkcv4yNUZ2xPCVzC2TdKjwgNO5L8_ZVDhPwQToIjrprqoMnilnpHKHdX99OeQyRooR13yN8aZZsLIpyTSE6czes_KzXgcvuOVjZxtFWCWsBMZhAUxmQGlwh-mCa1TFHhyi-WWu8qXrhAJIxp7tLehRwIKzKqheeeRYD0cM7LH5kQag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قیمت کوکائین در تهران چند؟
🔹
پلیس مواد مخدر تهران بزرگ، یک بار بزرگ کوکائین کلمبیایی را قبل از پخش در پایتخت، کشف کرد.
🔹
این کوکائین‌ها بیش از ۵۵۰ میلیارد تومان ارزش‌گذاری شده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/691652" target="_blank">📅 12:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691642">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3eKqCP5vlH8RWryrZ2h50aDer_7LKavLcjQk4fmczwLsoxhyFS5GKhkY51lpXHQKnSMiOthL272UVV-BL3kdLVRgE4rfZTTcKa4I-JciGTCA5klUunTlKXt6-HHV6V1DIic2xcDXAxQbh5h_MehJhAdS1xxW73HXBklccqcMnMI5ffgsMyhdluecRWbSb6M-c5mUCk5_BplF6HilVfVcH6VPIuzU1hsS38TQYUIgxBscor_I5OODfgCvfM_l9f6UjdRvIErNZapSn53tZJgQrp6YfbCUdh2L-O7Mh_9UjAty693ctQD02xQWNKGmYZaecyU4F7QUyy3mNbvhYOw9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C23_K02nV7R9hPz9McexpTMbN70LmaZtqDQwSnO7Dk-SsQFabTLY27AwYzNLtm5OKEckP248E5D8njZMV6RsgvENQ8JpmFfUU0GY-n6W63-5nt0lM2Fj2G6XYngKaXQYOErH6j-hZSjFuBJNG_Qv2jHfESexdaNEC_9dU-JYqqjmTwU8S_KwrDbMLaLaa2Gp06KZzsVzYQApALjhdD0SswcSpT1WiruTwzHVfWYVnGgwhwYDqT0WApnF4d80nBMlGfYPGUbbCItw5yz1_7dH1jAss5F3P5EBMmLvPNqGdGni7M-R1C5eNAyl_4ZVQ-dEZfgcpYtmW66bLbw1k0PEhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLQRtivYlv6VMOJhwfogB3nXl4cdzz_tsuNO--e7IVjUmPdhVO4D1EvBEi5ARB2Y_CAessBATaOjhQWs4AiH_SYVE0CqdI1aYA-VcRBIsK2QPiQCAOYmP_SiDwP5fIhLfrGglRSNSGwHPiVbbcgiw0lOY5aStFEmt4mrp9cuOWK0ROau58SJhdZ-vyF-YUucZ6TbGBBBm5LWnDARJWUxrIQ4DnP0Y9VdYXLlT_92LdYWLF5HMs_ByZq0MOER4y4bgqVZUYlKCD4x4Say0_KQwhdAvCPC7G-FjN4eRPjD7HyIBqnUCe5SbbR8W7ESZKtFK74boPdNU2W9oRhNyfnqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPdn8J4FT8uOyaeJc6u9pjVP0121X9KyWMY0C3gVgk3PY1nHTXCTE2GW7MxLlM0F_EygIupTauC1siNFUp0YNKlfNTMzVEyViBmmyRc1iMkhVGTP54aNVg2Wl-_kYBoIsVZiXo6PCHn9c-rlxJI-qbXmOz8MdDrKSvatwrOB6cQtjIWmgem-XOwtbUEMuF0Qr5YnThjLcZ-6V-N1XT6Z1YrD4faLlLqE0nBP0XP6qeMM1qxLG71zSxiYuH3Q8Bt8He2S6PJn4nvmxJeUMhTpg9-iy7u9lyawX8SMKUkQMgPnqseQGc9KdP3vqr5ScyMUWV1rEDyqeai3DMt79jvaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFcr3JbM7f633MAajtgIWJez2jgdxqJ-I37NlTUY7EKF-eqaLbQelytH_jBBUItkssLbI064Tss3PKOLCIkx6duAcAoBO-pFioDvEevJKARLXxPsA36_AtKVAjf36UrWBwlLx_WNXyyGKQNXhSowYyqFJToojzWp4Tnz4hegE7h0ewWWcoy9fzWN_EUg0bk9i0B7LEBBUj1P0jTMiU_IgXJbBZOJqj3dtK0IqC8--kLtvDi4d33_PXI225aHg44dUwdrBW5t_--5215vRYYVl4u-zAXd4iITfiS8jMDw18uKjF-h9EFJGivs56zvFRde-P0MDOsQDrK4URmN0khxFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYYalRC62bOzPSAtPdiynCjvfFq2_kV7rJ1C7ijzX_eE51IV0dIg-_tarpSaWPMvRNIFazaz7_2z2bS5hO14fhrll0PQDN7sq45R9JQpKpUUQ0AkVZzWEumnJP3nhArNG2CnkUcboAxyDM8yuMPBCRXzZVkPk-xHzSBs4TemF8s-g6OFTFnwQOLRfi-2ySW_Ts395x02ltGfnJvY2wWyHzTV3dzH1JdXikqT61hVVZYYNC_jmBdXWsoqkFWtCVL1If4CAq9kzhL_Dm8Qm5DUaVhPXvY4Lkp8qBsA2h-UBSAEUcsaXOGmX8nmytPZFoWuX9pytJGEvCVwfpeRYYcEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuJTB25o8G3b2xteh1rmB5HRIsmriMECRz0qDR6N_ppKbsxNtnbFfSU3-tARWZNLla44_FeLrJ7ud--QUhCbDXyRrURt3Vd4a7oJRT_4UrFOT1csTdoVARUWgWHddjw5SRyGfUdOLjFYH2BoNVaQOAueD79ndtyiLkLK5eoNsaZyn6UBWoW44ND-Dznrd18DcV9CcIBUuZ0oeO7LKKuCU5_75ZCup0w2EWrlrR8xui06suoagxhQxbNqMj_inogNQS_MZ-ww2VakbosQcuhKqQKJl1H7T8Lb6wGxlmcUQSVM9U3kN7UjmeLp5tiMJWPCcQJ7QPNlEYVLKywOyFNUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtifjoIyfvMtqRPHbp1bCTfnAZ6A7V3Zz2DIMkwupyrXBjPYGPMncvskj4k8MTXWxf3k22VWNNT1nPv7_ZKfMN44FXY8XENWBnUtlCxFK0loxm8DEk9UyxyREfOxJOT_GHqG7SdZ13cjKHReIsa9BMc0o2SWdPZ5h_mWZUB2dcZs9k0-Z8LpaTgYLx4Pk-V7zt_OE_Us3lOb_TQ9Ohp0gbP6AmF7FU8miGuBjrJ1LWO5XN9LkRJIWNZsMV1PhEWxnNPXnCIBuQfYXjh4DfyjuZrtvDlH98vwPcA4YlBRREh9iYvuoHJrgMsV02qZVwLu0r9XkDZ2OVY6oh00UE-oLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qkmp6mtxnhn20aWCai4854nnWsZTckzl-ByCa3kO_RMEleYCGLF0_aekAEIyx6ysDTo0gqbNauqI9TMdYmPh-y7OL2XS3l_74P-TtL24BJfpcfKf1LKNoNgWDpubdZK3NyLg6lLyahzlZQ4fWuOApVGRw84cQ2WGB5TlhmrR1zHlyuHBnKvCI3quKCZ6V2rfwero1uRrWnfqzBdbDr7fr6D-Ya6fXwN9Mw8JMscsmV6d0gtDZo0zYJ95_nY0YqjeZYeyb8L66qy4ID5NES33L6DeBHfuKE2tBSKBojZoqZl8yLh65A6JDx0FP2eovgYTykgEn0lauAhWbzC4t2WAzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kj0dAEKwslqOV8YE5jJ-_dPqY06YGHqZIZXW4vq8-duOqMkxIY9XN1mbOIgPcB3PpVakxO7DWn9NP_-VVgV0aVq168yIyKBP4ovbF7mtGjbMwsxn1QqsSdayfVSEmQRWPI77t39loVFR9lvLradRSScBi747JUFSiRFoy-DJI-Xw7ICJdI5OYEr_kh7689-f44CIoFfmTWioXK2QSX0qXM94EWkkyBQ3B_fZSIvBCe3Q9izj-jUQ6m9yie98fovOx0YdV3fHtc5cerccr-rxnhO_pKg4-xrzVNBZVTzTwzr7FJNUs2BnW6D2UknjrUy8g5JAGqdk2OKwlNPMZF9dCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
چالش های شما  مخاطبین عزیز  در تهیه اقلام دارویی ضروری.
🔸
در چند خط  روایت خود را همراه با نام، شهر و نام دارو برای ما ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/691642" target="_blank">📅 12:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691641">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
سفر ۳ روزه رئیس‌جمهور چین به آمریکا
🔹
بنابه دعوت رسمی دونالد ترامپ رئیس‌جمهوری آمریکا، شی جین‌پینگ رئیس‌جمهوری خلق چین طی روزهای ۲۳ تا ۲۵ سپتامبر (۱ تا ۳ مهر) سفری رسمی به ایالات متحده خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/691641" target="_blank">📅 12:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691640">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7304b14c9.mp4?token=WzQtUQonCPJGFiERaPmPEPxWKeVGdj8faft_-0v2dEfdG3iSX4B77yAdCETRMzL4cToQa1NrCndSUR3ofaURvYkgD-wijiETQt9FKVHoVV8H0NQvs6_VfIaeukBzsQ_wQw8U2mn1tfxHXang7OjtQfOX6UIYRzvuRD9LDjZ-F4ZH6FdMi5huTGkgL4T8I_afU-CXatCGWgwKllrUxjGKvonVF6llijPlwEkHHAH-nn38GJaPfFt2WDMi6SqJzWB4DvCWNbMmeL0kuYv9KtIsazK4AkbIR7GfjlKqLJ8uHVYKcJVIqPm1pl-drF6RC5Yi6R5o7Z1oe9xp8yt7-J28Z6EdrT-u9W6y8on6g2votHBuA1fHzw3oPkufFP83BT5wfXRaKVJLHxNY_rUGuIQhTj2uPe9izYYfXf_Cmhx4dt4G5wh56tdeqnr_3EvWC8AO0Osy0DlfVEwkCAv3_NjzlCl-0I-yjwo3RXIPKWCTm6z_EoX8ZqivY6CU_F7PEjthdYswT8E34mTZWYOHu7ItmPXrrhE03QUAmSSPIzggId8b5IUl_aHMPfj3Whpc9mmrGyCdYhbLd2Rjb0t-U84pL9gBflMW1s87LAGsgY9mptKGf5eup5deiLJmen466bHeEKc58jQZd9Es-xZ5JGxCXdjG3wkwr67XIgFjUHSA1yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7304b14c9.mp4?token=WzQtUQonCPJGFiERaPmPEPxWKeVGdj8faft_-0v2dEfdG3iSX4B77yAdCETRMzL4cToQa1NrCndSUR3ofaURvYkgD-wijiETQt9FKVHoVV8H0NQvs6_VfIaeukBzsQ_wQw8U2mn1tfxHXang7OjtQfOX6UIYRzvuRD9LDjZ-F4ZH6FdMi5huTGkgL4T8I_afU-CXatCGWgwKllrUxjGKvonVF6llijPlwEkHHAH-nn38GJaPfFt2WDMi6SqJzWB4DvCWNbMmeL0kuYv9KtIsazK4AkbIR7GfjlKqLJ8uHVYKcJVIqPm1pl-drF6RC5Yi6R5o7Z1oe9xp8yt7-J28Z6EdrT-u9W6y8on6g2votHBuA1fHzw3oPkufFP83BT5wfXRaKVJLHxNY_rUGuIQhTj2uPe9izYYfXf_Cmhx4dt4G5wh56tdeqnr_3EvWC8AO0Osy0DlfVEwkCAv3_NjzlCl-0I-yjwo3RXIPKWCTm6z_EoX8ZqivY6CU_F7PEjthdYswT8E34mTZWYOHu7ItmPXrrhE03QUAmSSPIzggId8b5IUl_aHMPfj3Whpc9mmrGyCdYhbLd2Rjb0t-U84pL9gBflMW1s87LAGsgY9mptKGf5eup5deiLJmen466bHeEKc58jQZd9Es-xZ5JGxCXdjG3wkwr67XIgFjUHSA1yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر رمز گوشی‌تون رو فراموش می‌کنید نیاز نیست فلش کنید اطلاعاتتون پاک بشه، خودتون ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/691640" target="_blank">📅 12:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691639">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqgXe9FjBsJ8zXSFQnXjh5TvnD5mO0J1swUluNebZVj6fkoIbK0R48L4wNme1BT6kpzDCfo5c-OmnnveA4O_t3c4suCxdjDA1a7tl1MNfrMiaQFhJCkkbQ7rxQ28QWxtG_v2qMWXjvcs3d5PW6mNi8htCv5J7z7pgubNj1mzAJD1qnkX8zfhT2hH2ll3zUtnA1h16VTuPCwc-pNzBlBUOB9biHomFixiTZakuZMkY6RovXIT-l2pfnzEqIxY8Ic1gPgdaDhJ5E0m8mu32oC5ZFPStUlFEg1QHoFbtz9C6glWPhydrzgYTQkOwgML8ODXpnPoiN1fT5PcEZOJfaX5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
محسن زرندی مقدم رئیس هیئت مدیره: بانک اقتصادنوین در حد توان و ظرفیت خود، مشکلات کشور را حل کرده است
🔹
رئیس هیئت مدیره بانک اقتصادنوین با اعلام رشد چشمگیر شاخص‌های عملکردی این بانک در بازار رقابتی، گفت: بانک اقتصادنوین در حد توان و ظرفیت خود، مشکلات کشور را حل کرده است و اگر این ظرفیت افزایش یابد، حتما سهم این بانک در برطرف کردن موانع و چالش‌های کشور بیشتر خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/691639" target="_blank">📅 12:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691638">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مدیرعامل توانیر از محرومیت یک‌ساله محل‌های دارای استخراج غیرمجاز رمزارز از برق یارانه‌ای خبر داد؛ برای شناسایی دستگاه‌های غیرمجاز نیز ۴۰ میلیارد تومان پاداش در نظر گرفته شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/691638" target="_blank">📅 12:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691636">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ekl5JyRYjyXLHnaX4-effsGwxPcHFwoKYrrGmdrK9Fu6bYJ8MyiTYd7qJzDTkYEPwXVvfgLa_dSvoBk9y96TqLmPmvceE_BPxHY6iWbFkCa-lhJ7nVs5BbCXw7o3O7pKP6K-XodybhvIEo6YMzgtKQU5XsFErF7_makW7Dp0BU8vsTQPoilIya9QErWALHRhS6iJQjhecMuGutTtu9InHcDfgYIOE2GgtQ4U0_QD-Z3A_t9F0wOXFPNWonDIesOSKrSPN9I14-gYNFLiApf-Cw_gVZ1I3nov3WTsIhGuwjWJSOab1zz_oTbUC15n07wtUvjq1HEuhYfpPDGWzid-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4685bf9da3.mp4?token=p008AKW_COU7Flsw6lmbl3jZBXyjL4cLq3H4ZB7SMiS1eq2yyswR3nsL1RlEgqT3cv2_-xv6yXFwb1a7z2LhAtZiPMd8pnxA7ZlUAJR0TFW4nC-EJTMriOZ6lks69MZZAmzBRWO8a1Xnu5b7IEqEPl9Oe5DtJSxJmJ-kHdDnBQPlnStxosxutmpT7UIwHyqBVcW2JRMFEkzDAZxKAw9GKrUZG0hSt5MVg4i1_MTEVddbPHhDAevJLQ1yrf1hc0sLHscfY_yi3TRH03TpKlJwEKZcYrNlQvqDvFUPmuqbzReUlrC7IHINKYYibeXsBPNUGVcKQT2BHOX2wGFz_bYR1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4685bf9da3.mp4?token=p008AKW_COU7Flsw6lmbl3jZBXyjL4cLq3H4ZB7SMiS1eq2yyswR3nsL1RlEgqT3cv2_-xv6yXFwb1a7z2LhAtZiPMd8pnxA7ZlUAJR0TFW4nC-EJTMriOZ6lks69MZZAmzBRWO8a1Xnu5b7IEqEPl9Oe5DtJSxJmJ-kHdDnBQPlnStxosxutmpT7UIwHyqBVcW2JRMFEkzDAZxKAw9GKrUZG0hSt5MVg4i1_MTEVddbPHhDAevJLQ1yrf1hc0sLHscfY_yi3TRH03TpKlJwEKZcYrNlQvqDvFUPmuqbzReUlrC7IHINKYYibeXsBPNUGVcKQT2BHOX2wGFz_bYR1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشتباه گرفتن بادبادک‌های نورانی با سفینه فضایی
🔹
تصاویری که دیشب در آسمان تهران دیده شد و برخی آن را سفینه فضایی تصور کردند، مربوط به بادبادک‌های چراغ‌دار بوده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/691636" target="_blank">📅 12:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691635">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46aa0c1f6.mp4?token=MEtIaIUSCMkg6idvK-woTeplY8kzNcw1fwWVTfnksADiopYXWUoHjpn9-iJ_QgnnAbLj3reE4JQZHFxphSb6WhBiVtJS-9Z7-lclU4toTtPXojbOa1pU6_kauOCn5cny1SMUANWhC9pVG6RUlB66X0xbgqubJOoAeYMyXNaR08kY0f0miRPdSfjfic64Psd8WD7ilPPeyfShIibiOU1gZ6pWRt6vGlkOUaFOtuzMDst-m4nOTzLb4Knm0CHFtXmrwLyRcYeGYEYtv-fD-wrUChu51LPN5is-9HJ_91rSS66mFjSkOcbmB7ACC1XQ5JlPdgNiftKMxCJ05SQwa_sIsF9TIvMWA5c2EpPp4akDuEFplS5gQxhWQRizLmOLaHBycTQbda4LUwXwkoQUoDRYikk6XeAQPJCHtJi4Y3TTjPnd_6wnMwq7e5yDm_gcakC1Kcl75Kxhxukzyeyne-XbHlNkOKNqSZx4aZnVS7LiXkwW-v1Od_lZbmxeVY8uh3Zmiuu2S7NrliDJntvf1EDt46UJjPennE0SeTCYfIFhUOOL0ZPXH_787UmsNNpyutjPZS_dbLhQjveEcWBa2TRyhtJyO_YE8QTIqDASTZTP81NJvTIrUcBRgHZDHN2XIdaV7GQAswQkFQ4JtgzqLqKCTN_sf7J-Y7ZutvqTuk-Iqxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46aa0c1f6.mp4?token=MEtIaIUSCMkg6idvK-woTeplY8kzNcw1fwWVTfnksADiopYXWUoHjpn9-iJ_QgnnAbLj3reE4JQZHFxphSb6WhBiVtJS-9Z7-lclU4toTtPXojbOa1pU6_kauOCn5cny1SMUANWhC9pVG6RUlB66X0xbgqubJOoAeYMyXNaR08kY0f0miRPdSfjfic64Psd8WD7ilPPeyfShIibiOU1gZ6pWRt6vGlkOUaFOtuzMDst-m4nOTzLb4Knm0CHFtXmrwLyRcYeGYEYtv-fD-wrUChu51LPN5is-9HJ_91rSS66mFjSkOcbmB7ACC1XQ5JlPdgNiftKMxCJ05SQwa_sIsF9TIvMWA5c2EpPp4akDuEFplS5gQxhWQRizLmOLaHBycTQbda4LUwXwkoQUoDRYikk6XeAQPJCHtJi4Y3TTjPnd_6wnMwq7e5yDm_gcakC1Kcl75Kxhxukzyeyne-XbHlNkOKNqSZx4aZnVS7LiXkwW-v1Od_lZbmxeVY8uh3Zmiuu2S7NrliDJntvf1EDt46UJjPennE0SeTCYfIFhUOOL0ZPXH_787UmsNNpyutjPZS_dbLhQjveEcWBa2TRyhtJyO_YE8QTIqDASTZTP81NJvTIrUcBRgHZDHN2XIdaV7GQAswQkFQ4JtgzqLqKCTN_sf7J-Y7ZutvqTuk-Iqxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی می‌گیم یک نفر ADHD داره، یعنی چی؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/691635" target="_blank">📅 12:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691634">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMSH7ptKAtVMTSRqZfKwyTJc0d-Se6e7Lx0Xs0fsBPOBCGAqJ0Uco8K0p9hooCJlrB0y9dvljjBeHj-PuAbDgrXq6RJQjfgQsxWmiCsjr-4ew1IQQm7ZuBdCHnkDgLwlbf6AqkiW_b0I9SACG4ZyTtE6fUTRe-4xkp_d9ZMGtbr48jXzb1m38Hl8EBp15qUHhJ14WyoUA4SK3uSHXSazXX0ZW8HI5dpPkkfi53KEPuBxlCO050q3fWXdqbPFRV53AbOH5AZS0wVmXwYf7JUdRug86qzkW-oY8z9naOtjwqO67IurqpOcyBmjuhM082_ObCqU95ReyMMiO86aEPcL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهایی که بیشترین دریاچه را دارند
🔹
کانادا با ثبت بیش‌از ۸۷۹ هزار  دریاچه، بیشترین تعداد دریاچه در جهان را دارد و با فاصله‌ای چشمگیر در صدر این فهرست ایستاده است.
🔹
پس از کانادا، کشورهای روسیه با ۲۰۱ دریاچه و آمریکا با ۱۰۲ هزار دریاچه در رتبه‌های دوم و سوم قرار گرفته‌اند.
🔹
چین، سوئد، برزیل و نروژ نیز هرکدام با داشتن بیش از ۲۰ هزار دریاچه، در میان رتبه‌های بعدی کشورهای دارای بیشترین تعداد دریاچه جهان جای دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/691634" target="_blank">📅 12:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691633">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih2a6RsGNatGB1Sxsr3v1-ZTsr3e7hc-fvXDpYQwFjMUTyK_OaqgTOvYTEDONH--J3jJR4zQHxe9vfZoAgNs9j64Ka2dMTOmAWmw7ltno6n12VHmp6QeaxaFLh1pod7Wc2lCC16Ker4EYrGh3b9d3xRPZCO5qMk-B8bu_DhkMFvLnLU87y5A4QnsdOx43fi6Ry06JQbotfke7mvOULsDblYa4HMpa35fG_Gqy-25TeCLiV88hai5HQ4XBnXc94WEyNqSkJtplZfbwNrmVvHz75JY4jiy7tEYo_TctdEUYFFS9U0brfV9K3TFlNof2qq79gXKRJ29gzYPH6XrAFlQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موبایلتون فقط یک گوشی نیست؛ بخشی از زندگی و کار روزمره‌تونه
از شکستگی و ضربه تا آب‌دیدگی، آتش‌سوزی و نوسانات برق؛ با
طرح «بیتا» بیمه آسیا (بیمه تلفن همراه)
می‌توانید متناسب با نیازتان، پوشش مناسب را انتخاب کرده و با خیال راحت‌تری از موبایل خود استفاده کنید.
🔹
انتخاب طرح متناسب با نیاز شما
🔹
پوشش طیف متنوعی از خطرات
🔹
فرآیند ساده خرید و صدور بیمه‌نامه
🔹
امکان دریافت خسارت بر اساس شرایط بیمه‌نامه
📲
برای بیمه کردن موبایلتون، همین حالا اقدام کنید.
بیمه بیتا؛
یک انتخاب مطمئن برای محافظت از ارزش موبایل شما.
@bimehasia_co</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/691633" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691632">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
خداداد طلبکار هم شد: دارم میرم مشهد به یک زمین چمن سر بزنم؛ فردا از باشگاه گل‌گهر کسی ویس منو ضبط کرد در جریان باشید/ پسر بده فوتبال ایران هستم؛ شما خوبید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/691632" target="_blank">📅 11:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691631">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
آیت‌الله شبیری زنجانی دار فانی را وداع گفت   دفتر آیت‌الله شبیری زنجانی:
🔹
روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/691631" target="_blank">📅 11:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691630">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce356ef5a.mp4?token=REBI92zhKQ5p3GOeSlIglLmAXzSnprHIx13DF9HQZIeZGnhK1n71nCQyze84b9desRlQHBqavnF2q2g4Gj6s0qHRNgemUS7YFbAxE4FhjbrFLmea4BVrQsyWJz2Fx6fmv2mI3p7tlxN6MkD-NFVZemiSt0cuXCv9b8mxCO0wllIz0UOntDtJVkzXxH650vR_Zak8c92jrEhKhB2LMifFxWkHyK_oS6fSrvdlA7TrcIjTstnLeT5CseuflAM9ctwqAbJHnaSdKuclNEh9ozHOHJWKlyepnssVZo_Q-6lss0lurHemKvV3JmOSPL1c-D0MLfBxUKT_9isrA7W74TGTDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce356ef5a.mp4?token=REBI92zhKQ5p3GOeSlIglLmAXzSnprHIx13DF9HQZIeZGnhK1n71nCQyze84b9desRlQHBqavnF2q2g4Gj6s0qHRNgemUS7YFbAxE4FhjbrFLmea4BVrQsyWJz2Fx6fmv2mI3p7tlxN6MkD-NFVZemiSt0cuXCv9b8mxCO0wllIz0UOntDtJVkzXxH650vR_Zak8c92jrEhKhB2LMifFxWkHyK_oS6fSrvdlA7TrcIjTstnLeT5CseuflAM9ctwqAbJHnaSdKuclNEh9ozHOHJWKlyepnssVZo_Q-6lss0lurHemKvV3JmOSPL1c-D0MLfBxUKT_9isrA7W74TGTDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحکانه نخست وزیر قطر: ایران صلح طلب نیست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/691630" target="_blank">📅 11:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691629">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f814630249.mp4?token=uQWHdS2SDh6KA2h4ShfgWWuE9IUlSQ8wovN1TOyYTiri403TNXnJs_EbPcOA9p1nXHWPiSEOE4sEUdr661ND4d-m-x_atI8gEXxVNY-HPUFaZkeIvpGURxInqIMR9v-s0HXdJQIqZTz0kGLSab1qOvQfYqW8v8z9OS9YCy3vgkY1RkZA_7SbDDYc-RSV94EPYW_1hBddvBxUJpKbvED80WV_jD1HTi2pLSRVUxHdGZXJv6NDkRPUlemYqXTrt0mAT_gJElsXuKXEsMxgHblQ1yejO2dO6j--lUOOqPyfIFRryFdykxgKHFNAVOQg9gBB16_XMql6I_0BqAB1PC7CLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f814630249.mp4?token=uQWHdS2SDh6KA2h4ShfgWWuE9IUlSQ8wovN1TOyYTiri403TNXnJs_EbPcOA9p1nXHWPiSEOE4sEUdr661ND4d-m-x_atI8gEXxVNY-HPUFaZkeIvpGURxInqIMR9v-s0HXdJQIqZTz0kGLSab1qOvQfYqW8v8z9OS9YCy3vgkY1RkZA_7SbDDYc-RSV94EPYW_1hBddvBxUJpKbvED80WV_jD1HTi2pLSRVUxHdGZXJv6NDkRPUlemYqXTrt0mAT_gJElsXuKXEsMxgHblQ1yejO2dO6j--lUOOqPyfIFRryFdykxgKHFNAVOQg9gBB16_XMql6I_0BqAB1PC7CLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در برخی مدارس آمریکا که استفاده از تلفن همراه ممنوع شده، دانش‌آموزان پس از خروج از کلاس با این روش قفل گوشی‌هایشان را باز می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/691629" target="_blank">📅 11:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691628">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
کنایه مجری تلویزیون به ادعای ۷۰ درصدی مخاطبان صداوسیما
🔹
پس از ادعای رئیس صداوسیما درباره بیش از ۷۰ درصد مخاطب رسانه ملی، یکی از مجریان تلویزیون با اشاره به تجربه خودش گفت: «۴-۵ سال هر روز در شبکه یک برنامه زنده داشتم، هیشکی منو نمی‌شناخت!»
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/691628" target="_blank">📅 11:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691627">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌹
فایل‌های صوتی تفسیر سوره محمد
با سخنرانی حجت‌الاسلام امینی‌خواه
🔹
جلسه اول
🔹
جلسه دوم
🔹
جلسه سوم
🔹
جلسه چهارم
🔹
جلسه پنجم
🔹
جلسه ششم
🔹
جلسه هفتم(بخش اول)
،
(بخش دوم)
🔹
جلسه هشتم
🔹
جلسه نهم
🔹
جلسه دهم
🔹
جلسه یازدهم
🔹
جلسه دوازدهم
🔹
جلسه سیزدهم
🔹
جلسه چهاردهم(بخش اول)
،
(بخش دوم)
🔹
جلسه پانزدهم(بخش اول)
،
(بخش دوم)
🔹
جلسه شانزدهم(بخش اول)
،
(بخش دوم)
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/691627" target="_blank">📅 11:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691626">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ9ZboCFQtOLPmBEh_evOU4TwKaM2jYDHuu7Wbcb82ekdsYD3jxogiDAm4XYgktAS1zh2bqiMtUEOZkHxK0pX4ISLa0-VjtIxkNDAw2XU6hwDCt4sPw8_EP-DpMJMrIkQZex6y_t1Lh7zWi4Wgvo8lN07GGJaIIeQmQDtdMqSeKZBx65UVOctEPxwq55KPLghLE-nJw0K_2jAo4bdy4SjRnWNF3yeWXhG2cj2zXmdD2QeKDwxxQPzq2rRnBel4ehD9zoi5ZeL-AOqLD-SA5Aaam2CNkavbNh6Z-4Q9Yi-MB49BTZcbU0U6_wiA36Y0iiaCllkiWTpoBNRsKHK7sA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از اسناد حسابرسی فدراسیون تا مشاورت مدیرعامل پرسپولیس به گزارش ایسنا
🔹
حسین شریفی این روزها به‌عنوان مشاور مدیرعامل پرسپولیس فعالیت می‌کند؛ فردی که خبرگزاری ایسنا پیش‌تر در گزارشی، نام او را در اسناد حسابرسی فدراسیون فوتبال و در ارتباط با ابهامات و تخلفات مالی مطرح کرده بود.
🔹
براساس گزارش ایسنا، پاداش‌ها و حق مأموریت‌های ارزی، سفرهای بدون مجوز و تنخواه ۶ هزار یورویی از جمله مواردی است که نام شریفی در کنار حسین قهار و سعید زارعیان در آن مطرح شده است.
🔹
سؤال از مدیریت پرسپولیس مشخص است: آیا انتصاب فردی با چنین سابقه‌ای که در گزارش رسمی به آن پرداخته شده، در شأن باشگاه پرسپولیس است؟
https://isna.ir/xdLwnn
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/691626" target="_blank">📅 11:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691625">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyVoRPEHWA01gwvhGEtL2Exkd7v_X92Pt1iQFSX5XkXEtEO7kYJoPs0CNNk2taoSRL302pyntlwX73Ymx28riAkaLhiiNGuVv3bcpirHjgQoRglhIR40ek_H9WX9VY3WLrYQB56d-P105JaIadB3Zl0DYAUfK3UEljZXMtJiH13pEWP_e5mRK4P3vrDOUghr14ppcbz26ErPh88sQhbetALaoviCraxeEsTiZtE7D6gVqsBfTKcDTsVEhAaKiZp45Fh6lHhLf_bBQS7ffbSTp7nFJ0Njj-rHXGyavluhzVYcilVgUVyMBf8YHz4y9ogm3A-6xo6AplqRHM7Z-9I_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدترین کشورها از نظر توزیع عادلانه ثروت
🔹
امارات متحده عربی و روسیه با کسب امتیاز ۸۲ در شاخص جینی ثروت در سال ۲۰۲۵، بالاترین رتبه را در تمرکز ثروت دارند.
🔹
ایالات متحده با امتیاز ۷۷ در رتبه ششم قرار دارد و بالاتر از هند، مکزیک و چین قرار می‌گیرد.
🔹
در میان کشورهای نشان داده شده، شش کشور از ۱۰ کشوری که کمترین امتیاز تمرکز ثروت را دارند، در اروپا قرار دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/691625" target="_blank">📅 11:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691624">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سفر وزیر کشور پاکستان ارتباطی به ارسال پیام بین ایران و آمریکا ندارد و در این سفر مباحث مربوط به روابط و همکاری‌های دوجانبه پیگیری خواهد شد، شروط ۷ گانه ایران به صورت صریح و شفاف به آمریکایی‌ها پیشتر اعلام شده و تغییری در این وضعیت رخ نداده است./ تسنیم…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/691624" target="_blank">📅 11:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691623">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmV5CIstFwcHIwK_PXP8hQryzBbn5JFB4jy2NuQmjAKXTHwu3WI4NiGyJA1s-Oy4rwRAJZWme1kTsKZh-BuJm9YCeVQo0l6-RgU0k7TGsEtQ1sLe-AhigLptEHgdTBsBBT_zfh8EckjMfOpo_-fOw0llmAy2nFS1gMmju87NqsAW-E8uvcxHr5wyXfZtlkx27bBy3LCUxiirn7TRy_TPknwwcVb2zct8WDi3147eTX9Th_7Gk18QUbOF3wCmVy00EGFFhgDR5oHMGtIld02TvmfNCxKyPAzfLdu8rD0O52qE3kqZwDbmebSSIUuGEWbnFBueAa4lR-AfbaOHcwKBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانش‌آموزانی بدون مدرسه…
🔹
در طول جنگ ویرانگر غزه، ۲۱ هزار کودک کشته شدند؛ از جمله حدود ۱۹ هزار دانش‌آموز، ۴۵۰ نوزاد، بیش از ۱۰۰۰ کودک زیر یک سال و ۵۳۱ کودک زیر پنج سال. همچنین بیش از ۴۴ هزار کودک مجروح شدند و صدها هزار نفر هم آواره شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/691623" target="_blank">📅 11:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691622">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
مجتمع فنی تهران - نمايندگی استان البرز (کرج و فردیس) در حوزه های زیر دوره های آموزشی و تخصصی برگزار می نماید و می توانید ثبت نام کنید:
🔸
شبکه،برنامه نویسی و هوش مصنوعی ،ICDL
🔹
معماری،طراحی لباس و خیاطی وگرافیگ
🔸
حسابداری،معامله گری ارز دیجیتال،فارکس
🔹
زبان های خارجی و IELTS
🔸
عکاسی، ادمین اینستاگرام و ‌تولید محتوا
🔹
نرم افزارهای فنی و مهندسی, تعمیر پکیج و کولرگازی،برق صنعتی
🔸
برق،برق خودرو،تعمیرات موبایل و برد، PLC
🔹
تربیت کارشناس منابع انسانی،مدیریت عالی کسب و کار(MBA)،فن بیان
🔸
مراقبت از پوست، آرایش و پیرایش،دوره های زیبایی،تکنسین داروخانه
🔹
دوره های کافی شاپ و آشپزی
🔸
مهارتهای دانش آموزی(۷ تا ۱۷ سال)
🔹
عمومی و خصوصی، حضوری و  آنلاین در رده های سنی مجزا و مختلف
مرکز مشاوره و ثبت نام:
☎️
026-34127
@mftalborz
✔
كرج پل آزادگان ، فرديس فلكه سوم
🎯
آماده عقد قرارداد با سازمانها، نهادها، شرکتها و مدارس
📱
صفحه اینستاگرام:
https://www.instagram.com/mftalborz/
🎒
ثبت نام اينترنتي و اطلاعات دوره ها
🌐
www.mftalborz.ir
مشاوره تلگرامی و پاسخگویی به سوالات:
@alborzmft</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/691622" target="_blank">📅 11:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691621">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
وزیر کشور پاکستان راهی ایران شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/691621" target="_blank">📅 11:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691620">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
بر اساس گزارش‌های منتشر شده، دقایقی پیش انفجارهایی در منطقه «العيس» واقع در حومه استان حلب سوریه رخ داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/691620" target="_blank">📅 11:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691619">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پزشکیان فردا سه‌شنبه عازم نیویورک می‌شود
🔹
مدیرکل روابط عمومی دفتر رئیس‌جمهور از سفر فردا (سه‌شنبه) پزشکیان به منظور شرکت در مجمع عمومی سازمان ملل خبر داد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/691619" target="_blank">📅 11:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691618">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
دستمزد جدید قلعه‌نویی افزایش می‌یابد
🔹
برخلاف برخی گمانه‌زنی‌ها، قرار نیست سرمربی تیم ملی ماهیانه ۱۵ میلیارد تومان دریافت کند. رقم قرارداد جدید او از دستمزد سالیانه ۳۰ میلیاردی گذشته بیشتر خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/691618" target="_blank">📅 10:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691617">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وزیر کشور پاکستان راهی ایران شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/691617" target="_blank">📅 10:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691615">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9be34764bf.mp4?token=jfs15qb29Fhxf1N3d6BGcoS-2R0WTrpSV4hFpVfVOVlqjYhA29dc6LsXbxwv4ccRc9iSH2ccW6fLTzyDbUWwyAB2EQDbc_3MffvdoG6Q5T5nnt7dAGgadplRlr3XJbtw4x9r7LS3GyrHgP__FI-k2pSQEJ-4AYNJpDAyCK_xQGeDFeLhVaG5EACAU4cvrcLL9C5NVnprysOEpK_FBDRxBGAvZf7co2LyouFckAfOEpWzx3OX6JJorkbk0AwXK574wDfD60lcgkV37N13GWMzjFrx7tQt4KEREER11SadEyG8zh5a955gxY1zX6yk_zqZNsSKHSJCxlJDOm0PvkOhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9be34764bf.mp4?token=jfs15qb29Fhxf1N3d6BGcoS-2R0WTrpSV4hFpVfVOVlqjYhA29dc6LsXbxwv4ccRc9iSH2ccW6fLTzyDbUWwyAB2EQDbc_3MffvdoG6Q5T5nnt7dAGgadplRlr3XJbtw4x9r7LS3GyrHgP__FI-k2pSQEJ-4AYNJpDAyCK_xQGeDFeLhVaG5EACAU4cvrcLL9C5NVnprysOEpK_FBDRxBGAvZf7co2LyouFckAfOEpWzx3OX6JJorkbk0AwXK574wDfD60lcgkV37N13GWMzjFrx7tQt4KEREER11SadEyG8zh5a955gxY1zX6yk_zqZNsSKHSJCxlJDOm0PvkOhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرول؛ مراسم عجیب انتخاب همسر در قبیله وودابه که یکی از خاص‌ترین آیین‌های خواستگاری جهان است؛ جایی که مردان برای انتخاب شدن آرایش می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/691615" target="_blank">📅 10:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691614">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfHiWMLzTnD82IYwgbLT0ZP5_xfwN4mXtmy-z5L3T5eWXy-4eWf4Br2OBSVu2AfUv78DAZsxSrpxdFNP79saANc0ahH5Q2pE4BR7KGK96l9Y-qiPnJGG1CNHj0lsPDlbySsRSqHyuK7gOgwlnS0eurtZ5VQ6Q9WayQrM-L8DvlsOgVom5B1s6pPApNOAguat-pUolr0UQsuJg7343HPcNznPe_eIHDGUdOFK9x4S7F8g7vN1o_InTzWmQlrrG-xzWinFpw3_SPAaSqpBgNuG-b0w0pkKFnI7oOdaFMZHaCU-zzF6q8LgCicP_C8wIxH9kBsbSHS80OXjEemxtAjPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شمارش معکوس تا انتخابات آمریکا و اسرائیل
🔹
انتخابات میان‌دوره‌ای آمریکا ۳ نوامبر ۲۰۲۶ برگزار می‌شود؛ از امروز ۴۴ روز باقی مانده است.
🔹
انتخابات رژیم صهیونسیتی نیز برای ۲۷ اکتبر ۲۰۲۶ تعیین شده و ۳۷ روز تا برگزاری آن باقی مانده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/691614" target="_blank">📅 10:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691613">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d308d5b983.mp4?token=U0yRF_gFxKZgCNX19G4xbBetbrEE3P_Oi1HvlEzt9_UYlbyivCcGApn1c2E_MP_hcyGjBMdM0BxuSC-PcuCjrzyZFSPL7B5TatyqQNlrOUlZCdFs0Owj7aDxQEheCF3pPji90JHq29-YYt08truqfDBrRRdj7FPGHytURNiVl4c7WnPQw134ZOYJcQjrnHJAT1s0XzthM2dufMBHPQooFV1UdTZPvAbesOJxYrLhwPYat0o1WX6weGm6vJlkI7IV0y3-CQY7WIWSy-qbcoOXVaCIZxxwxtmLhby7pyQamrm6bGM7am0fvcs-IW4kwtrW0RDJdsxhSc4NEHC9NkMqsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d308d5b983.mp4?token=U0yRF_gFxKZgCNX19G4xbBetbrEE3P_Oi1HvlEzt9_UYlbyivCcGApn1c2E_MP_hcyGjBMdM0BxuSC-PcuCjrzyZFSPL7B5TatyqQNlrOUlZCdFs0Owj7aDxQEheCF3pPji90JHq29-YYt08truqfDBrRRdj7FPGHytURNiVl4c7WnPQw134ZOYJcQjrnHJAT1s0XzthM2dufMBHPQooFV1UdTZPvAbesOJxYrLhwPYat0o1WX6weGm6vJlkI7IV0y3-CQY7WIWSy-qbcoOXVaCIZxxwxtmLhby7pyQamrm6bGM7am0fvcs-IW4kwtrW0RDJdsxhSc4NEHC9NkMqsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوگل سرچ به یک دستیار زنده تبدیل می‌شود
🤖
🔹
قابلیت Gemini 3.8 Live به کاربران اجازه می‌دهد با دوربین گوشی چیزی را به گوگل نشان دهند، درباره آن سؤال کنند و همان لحظه راهنمایی قدم‌به‌قدم دریافت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/691613" target="_blank">📅 10:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691611">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15bb42655c.mp4?token=KAfm2F54KrPQVOr0eAbO8oaoBTrx3TkXyeTV6ajl_QwGnjxpC3fW7_eR5Fa6r4KqhfQkpSy6hLM8RjTVMh17Pzmz03fMAa16zoVmtz2EiJtJfdGtx4yCuq9_QQAYRe8y-9M3aCVClV2JVGfLEcJA_MIc-AUKPKHWcacDkT63GrTfbZozIAwUvnijWVpuVd4VsuGzVPID4mZl6_jeFhIz5r6xr3LvcVqiMINe-cmLculIZ-3A3f-2_PWOAMofdzmiuHuqp3AS65H2QFun7ZHUrXP_RucqwvFTpiN_H9RHw99n86ejKgqwGQAgIAnqbCCKfIpZKxVlSKlqtqNo4-BMRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15bb42655c.mp4?token=KAfm2F54KrPQVOr0eAbO8oaoBTrx3TkXyeTV6ajl_QwGnjxpC3fW7_eR5Fa6r4KqhfQkpSy6hLM8RjTVMh17Pzmz03fMAa16zoVmtz2EiJtJfdGtx4yCuq9_QQAYRe8y-9M3aCVClV2JVGfLEcJA_MIc-AUKPKHWcacDkT63GrTfbZozIAwUvnijWVpuVd4VsuGzVPID4mZl6_jeFhIz5r6xr3LvcVqiMINe-cmLculIZ-3A3f-2_PWOAMofdzmiuHuqp3AS65H2QFun7ZHUrXP_RucqwvFTpiN_H9RHw99n86ejKgqwGQAgIAnqbCCKfIpZKxVlSKlqtqNo4-BMRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهاره رهنما از روزهای سخت بعد از جدایی: بعد از جدایی بی‌پول شدم؛ فکر نمی‌کردم جدایی این‌قدر تاوان داشته باشد؛  فکر نمی‌کردم یک روز درِ یخچال را باز کنم و نگران خرید پنیر باشم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/691611" target="_blank">📅 10:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691610">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcVduMIQxbRmav1xAHLvWqvy6aPb6-rRtAFYvHyjrPN1hGy_iHkexlnElxyR-Yo7oAdf6xxRMTrD6gjKl4wGP5-bMYL8gOh8jahdQ7VQu7V79lG5xX8Lm3sxlMCBS_QDL6i0T-nyfGFT_1MbiAoTqqUy1rz0NVtKn6jlLwXpv-gmupXRcVuT-aMcQjJIhJcKnRliHKjYdLDsZADmwW9NLjdKPGOZZdaG7N5ftSdNlFCdwey5BcFj8WCwU_xmgCIZy7F6hH5SjCiehew10HNtD1tNrxdXmuTmpL8nIXOufUwC21fFohi3uJ1sWmRBunfD4ty_tGd8DERvUoT5uB04Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پل آسیب دیده جنگ رمضان بازسازی شد/ بازگشایی پل بیات در آزادراه تبریز با حضور وزیر راه و شهرسازی
🔹
پل بیات در آزادراه تبریز- زنجان که در ۱۸ فروردین امسال در حمله هوایی دشمن آمریکایی صهیونیستی آسیب دیده بود، طی پنج ماه بازسازی و با حضور وزیر راه و شهرسازی افتتاح شد.
‌
🔹
فرزانه صادق وزیر راه و شهرسازی در مراسم بازگشایی این پل گفت: این پل در مسیر یکی از شاهراه‌های ارتباطی کشور قرار گرفته که سهم ویژه‌ای در ترانزیت کالا از کشورمان به کشورهای اروپایی و بالعکس دارد.
‌
🔹
وی افزود: این پل با همت و تلاش شبانه روزی مهندسان ایرانی و راهداران طی پنج ماه به سرانجام رسید تا به دنیا اعلام کنیم که اراده ما فراتر از خصم دشمن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/691610" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691609">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a508c6f9b3.mp4?token=ukOtn1TrgkUSx0tethYDhF8fN1QUWXtmvDBfhgkjuJ2zvo3M4EUZR_bfmIZAj9_vn_6Z9C5ukFeN7tk5ZU7KuY4PH6NfIPClDge_Ugqq2IGr5EBXHiG7G05d6xXlZO904aAyNmIGtf5RRlR1H_cph-awD80Exv-Ue5Yx7cghMc-QJcT99ORFU7oJdf1NsTXnJJpHK-o5rmwrhmdI8d26xTS_xxFYDEaDCmZKomWWJweBLQsosfGEWOleD46Ik-bsSryVY2RCC3FR9QlbykHQ4Yc8Pg-PxgJTQaF8aNyqETZz2GTx57w8p8eOshQXDkG8bnclmTgOJ4RjpaVvvKjChyX4eGyGcWkpJnPFOhPO2OM7SJ7pBMHP5cczEzAUAPKVjCUEjbwilAzxmLOxIB3-ZQ8_syYnsZjEZqKFFVmCiIQB6Gu66ExMigH6cOdUqpqQJ9Ys-YmcQ1WrCjbmQycCTWDQ_3Uh_tjZUcgZsCK1LidtCsXNr8ru7015TN0cTPTUWGKCuHjpQOlm2M6LTvpeSIInf4Kyg2EkiCSmcmEDPasuwHKvAIi4QvfEoCAvCQuzDQCHTyJ4LJ4eYaRNDwp1U2CXDpBSKeQ_ZeShz0Y6c2vQeBPPqJMP3YRgmjPFPktqcczqAOSlNgEyx4onRrYSPX7Y1rMl54q0101TYylLK6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a508c6f9b3.mp4?token=ukOtn1TrgkUSx0tethYDhF8fN1QUWXtmvDBfhgkjuJ2zvo3M4EUZR_bfmIZAj9_vn_6Z9C5ukFeN7tk5ZU7KuY4PH6NfIPClDge_Ugqq2IGr5EBXHiG7G05d6xXlZO904aAyNmIGtf5RRlR1H_cph-awD80Exv-Ue5Yx7cghMc-QJcT99ORFU7oJdf1NsTXnJJpHK-o5rmwrhmdI8d26xTS_xxFYDEaDCmZKomWWJweBLQsosfGEWOleD46Ik-bsSryVY2RCC3FR9QlbykHQ4Yc8Pg-PxgJTQaF8aNyqETZz2GTx57w8p8eOshQXDkG8bnclmTgOJ4RjpaVvvKjChyX4eGyGcWkpJnPFOhPO2OM7SJ7pBMHP5cczEzAUAPKVjCUEjbwilAzxmLOxIB3-ZQ8_syYnsZjEZqKFFVmCiIQB6Gu66ExMigH6cOdUqpqQJ9Ys-YmcQ1WrCjbmQycCTWDQ_3Uh_tjZUcgZsCK1LidtCsXNr8ru7015TN0cTPTUWGKCuHjpQOlm2M6LTvpeSIInf4Kyg2EkiCSmcmEDPasuwHKvAIi4QvfEoCAvCQuzDQCHTyJ4LJ4eYaRNDwp1U2CXDpBSKeQ_ZeShz0Y6c2vQeBPPqJMP3YRgmjPFPktqcczqAOSlNgEyx4onRrYSPX7Y1rMl54q0101TYylLK6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارگاه ساخت آبمیوه پاکتی در پاکستان!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/691609" target="_blank">📅 09:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691608">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
هشدار وزارت بهداشت درباره واکسن آنفلوآنزا
رئیس مرکز روابط عمومی وزارت بهداشت:
🔹
تاکنون واکسن آنفلوآنزای معتبری در شبکه رسمی سلامت توزیع نشده و از مردم میخواهیم به واکسن‌های خارج از شبکه رسمی اعتماد نکنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/691608" target="_blank">📅 09:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691607">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تصادف کشتی فله‌بر پانامایی با قایق چینی
🔹
یک کشتی فله‌بر با پرچم پاناما در نزدیکی تنگه سنگاپور با یک قایق ماهیگیری چینی برخورد کرد؛ طبق تصاویر، قایق پس از برخورد به‌شدت کج شد، اما داده‌های ردیابی نشان می‌دهد شناور مانده و به اسکله‌ای در نزدیکی محل حادثه رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/691607" target="_blank">📅 09:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691606">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887f7c5754.mp4?token=ASwUuyeuYcZAYsws98QvthxsrzbJiXwM9sV2bSXF5EtjomXu5Ih6zbaVV-IrZSyL-BmXJ9nSxcYBCdjD5dPAijyZVD87YxHtHiwRMFk7qbp6EjRWBq8Zh9zL0gQ4qBLztc1Sa8j5P2fUb-CBG0Qt0pyd1FbYqkupqpyonSYJJPnf8vc77hSTUDbFfKNSMKpZo9vjCVK9WPD-BapcKWhalt1T5KK5d0RYZ-fLpOQPSsmhgwAEyRB9fOHRDpATzyjO2EKx1lFe78jQmh5FF1YtM6esfWvH4oSSKHuwi-OKvGB35xUCPDEjtuRFSmdT-FUj2uI9KBZLpyMeqnS19g3GCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887f7c5754.mp4?token=ASwUuyeuYcZAYsws98QvthxsrzbJiXwM9sV2bSXF5EtjomXu5Ih6zbaVV-IrZSyL-BmXJ9nSxcYBCdjD5dPAijyZVD87YxHtHiwRMFk7qbp6EjRWBq8Zh9zL0gQ4qBLztc1Sa8j5P2fUb-CBG0Qt0pyd1FbYqkupqpyonSYJJPnf8vc77hSTUDbFfKNSMKpZo9vjCVK9WPD-BapcKWhalt1T5KK5d0RYZ-fLpOQPSsmhgwAEyRB9fOHRDpATzyjO2EKx1lFe78jQmh5FF1YtM6esfWvH4oSSKHuwi-OKvGB35xUCPDEjtuRFSmdT-FUj2uI9KBZLpyMeqnS19g3GCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان خطاب به دانش‌آموزان: بچه‌ها سلام! می‌دانید که شما گوهر هستید!
🔹
آدم، مفت به جایی نمی‌رسد؛ باید تلاش کرد.
🔹
من از یک خانوادۀ معمولی به اینجا رسیدم. شما اگر ذهن‌‎ و فکرتان این باشد که بهترین شوید حتما می‌شوید. ما تلاش خواهیم کرد که شما بهترین شوید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/691606" target="_blank">📅 09:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691604">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0670c7ca65.mp4?token=R-l_k2nXmjwKsqxH2dik4-YDbQ81ixbaztQg7FN5lCejWS2O_lcjykSGV1QY7XBC9-WUQALLPynlGRCF4ASRAjncONTI7o_9b43iFHCWhsl5b4Gh9zfp77QlX48GdoOxbG7Wk0rH7T2soHUVXKGOfdA6hY6SaUeELZyF1xL-6OyEhqdhjEGDX9Dt3wzSQ-x3PMiNQ84ZYG7mDQUeIqXnO6cHgZbxzYuQIIFHwdNkOVpRB4hMx97cAjygBzf8jq4UmEJ51IsPyNclgc3zhNBL8tItXlJb5fwLiAsCdF8SjrjoSrt0ssIaMoOPE3gUrF2F_mXNUqJG8w4rBZZNmKEu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0670c7ca65.mp4?token=R-l_k2nXmjwKsqxH2dik4-YDbQ81ixbaztQg7FN5lCejWS2O_lcjykSGV1QY7XBC9-WUQALLPynlGRCF4ASRAjncONTI7o_9b43iFHCWhsl5b4Gh9zfp77QlX48GdoOxbG7Wk0rH7T2soHUVXKGOfdA6hY6SaUeELZyF1xL-6OyEhqdhjEGDX9Dt3wzSQ-x3PMiNQ84ZYG7mDQUeIqXnO6cHgZbxzYuQIIFHwdNkOVpRB4hMx97cAjygBzf8jq4UmEJ51IsPyNclgc3zhNBL8tItXlJb5fwLiAsCdF8SjrjoSrt0ssIaMoOPE3gUrF2F_mXNUqJG8w4rBZZNmKEu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدراعظم آلمان: مدل اقتصادی مبتنی بر جنس ارزون از چین، انرژی ارزون از روسیه، امنیت مجانی از آمریکا و بعد صادرات محصولات پرارزش به تمام دنیا، برای آلمان تموم شد و بر نمی‌گرده!
🔹
حالا باید خودمون از پس خودمون بربیایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/691604" target="_blank">📅 09:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691603">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
کیهان: اتفاقا همین حالا و وسط جنگ باید موضوع حجاب را جدی گرفت/ آیه حجاب در میانه جنگ به پیامبر نازل شد!
روزنامه کیهان:
🔹
ممکن است این شبهه ایجاد شود که در بحبوحه جنگ با دشمن، باید مسائلی مثل حجاب را رها کرد!
🔹
از این منظر، جنگ نباید به معنای تعطیلی سیاست‌های مرتبط با حفظ مؤلفه‌های هویتی جامعه تلقی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/691603" target="_blank">📅 09:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691602">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم‌النور4_ جلسه اول</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/691602" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه اول
؛
شرافت الهی
🔹
انسان به‌طور طبیعی با فقر، ضعف و رنج آفریده شده است که‌ این نواقص به‌عنوان موتور محرکه و عامل اشتیاق برای رسیدن به کمال و اتصال به غنای مطلق پروردگار عمل می‌کنند.
🔹
تکرار اسامی الهی، سرعت رشد معنوی و توانمندی‌های ذهنی انسان را افزایش می‌دهد و رنج‌های روانی او را به آرامش تبدیل می‌کند.
🔹
کتابت نام‌های خدا، موجب تجلی نور اسامی در عالم ماده می‌شود و بستر حضور فرشتگان را در زندگی فراهم می‌کند.
🔹
وظیفه‌ انسان، تنها دعوت به شناخت نام‌های خداوند به‌وسیله‌ی قلب و زبان است و نتایج این عمل را باید به حکمت الهی سپرد.
🔹
نام مبارک
«اَلمَجیدْ
» پروردگار، کلید گشایش برکات مادی و معنوی، شرافت‌بخش وجود انسان و افزاینده نور دل و عزت است.
🔹
تکرار نام‌های خداوند، انسان را به «نورالانوار» متصل کرده و نقص‌های وجودی او را با کمال الهی پر می‌کند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/691602" target="_blank">📅 09:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691601">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7b4e169b.mp4?token=Re-hnQ0NC7wcq22jbYA79C6b_bi2-mQsbCG9VybD5nN5Rw2eLVZipBFivVdApB34qSz93tyY4dk6OuTgMsvmvHXBF_t42MGzYpGOqQA14pq4msmJv45lxrlTorIUR6GABZigUH4mUNxwkX1Bh09a5byEE5odoxhWAW22yI7GAVuM-UHPfgSt0ioFR9Ev8SF4w08P7JFhdNIxMkBBIsLqLEylu_A88Qd7uXpy9SBVVEdmQlnMk6xknZNzEnc8ywk6OjZA6V8iPoy5BoT6-45s3aAIjB-jBCjf8xgoCx3mVbJr4mqO-kR7VLpMSdDXuVjkxax5dKHv3krnTVbJRAvvbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7b4e169b.mp4?token=Re-hnQ0NC7wcq22jbYA79C6b_bi2-mQsbCG9VybD5nN5Rw2eLVZipBFivVdApB34qSz93tyY4dk6OuTgMsvmvHXBF_t42MGzYpGOqQA14pq4msmJv45lxrlTorIUR6GABZigUH4mUNxwkX1Bh09a5byEE5odoxhWAW22yI7GAVuM-UHPfgSt0ioFR9Ev8SF4w08P7JFhdNIxMkBBIsLqLEylu_A88Qd7uXpy9SBVVEdmQlnMk6xknZNzEnc8ywk6OjZA6V8iPoy5BoT6-45s3aAIjB-jBCjf8xgoCx3mVbJr4mqO-kR7VLpMSdDXuVjkxax5dKHv3krnTVbJRAvvbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاربر ایرانی: ایران بدون پروپاگاندا داره نشون میده غیر نظامی نمیزنه، ولی آمریکا با پروپاگانداش هم نمیتونه زدن غیر نظامی‌ها رو منکر بشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/691601" target="_blank">📅 08:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691600">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
♦️
‌سخنگوی سپاه: سپاه وارد عرصۀ دیپلماسی نمی‌شود/سپاه پاسداران نه حالا و نه هیچ‌وقت دیگر هیچ ارتباط رسمی و غیررسمی با ایالات متحده نداشته و اصلاً ورود به دیپلماسی هم پیدا نمی‌کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/691600" target="_blank">📅 08:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691599">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
سخنگوی سپاه: برای یک جنگ طولانی آماده‌ایم/از نظر ما جنگ همان جنگ است، مقاطع مختلفی دارد، ولی جنگ همان جنگ است و جنگ هم تمام نشده و ادامه دارد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/691599" target="_blank">📅 08:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691598">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سخنگوی سپاه: برخلاف تصویرسازی‌ها مراکز اطلاعاتی واشنگتن قابل‌دسترسی بود و این مراکز در حاشیه خلیج‌فارس و شمال عراق مورد حملۀ ایران قرار گرفت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/691598" target="_blank">📅 08:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691597">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioTc_H_bAkAGKhl6B1TZg9_55rB418i7EbeETqqdOuCVdxQLntDOjMOYL1zB5-k4g-xGrVrbYx-8k7yOJJElgsxCNvTn-HFKhlbJcKbF4RkilWbBozEmIpKCWSt5OdVY5i7zWQh98dY5R18H30GOZ5A-5KVuRlCYpTOcynb7mWtU6zSdLve0u0I9gbIfazHXwLhewPcWjjaqbBREtu1x8oqdQUnBVYdsLoUQWYii119J8kpmG-PGCPotZTeUsMRABz2PQHJHgj5eBzmJx-aFz8O5ECjstlJz0OoXwiKlkQqzLFf99Yht7tDWRieqO-CwZhh_arFEieGu-07TysXr_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال و مفسر سیاسی امریکایی: آمریکا تحت دوره بایدن قوی‌تر بود
🔹
اعداد دروغ نمی‌گویند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/691597" target="_blank">📅 08:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691596">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaacc35503.mp4?token=ZIEslVuTAm7njX0kS9U3Fxme0u0DeYmtAQJBSN-kN6x3ty9ZobAc5Rs-qeQhrD4rI5ul0mrBGxWhD-6w0dryooJsfFwLvgqTSwvNA2EXdVdSmJVLsAz0rXUp60J31m6mUrzKd1UVWfz_hoHhNgeEFnfP1FfO52asN_9sEe9iqQF3ATtULwbMvGBivHlBRj1tkVB1P9SxcTscSgv4p5hwIy7qp6BY1wYkj-qlnY7dNOv8t7B6bPNvERMpl3ewykWCEI0sNSMsjZ2I3kQvVsjO2TXMndU4O274lZuxqO9dE1u3ir_YOIHHVRmWDoWM0d4sT4WlMSIQk41VNpc-hUsHmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaacc35503.mp4?token=ZIEslVuTAm7njX0kS9U3Fxme0u0DeYmtAQJBSN-kN6x3ty9ZobAc5Rs-qeQhrD4rI5ul0mrBGxWhD-6w0dryooJsfFwLvgqTSwvNA2EXdVdSmJVLsAz0rXUp60J31m6mUrzKd1UVWfz_hoHhNgeEFnfP1FfO52asN_9sEe9iqQF3ATtULwbMvGBivHlBRj1tkVB1P9SxcTscSgv4p5hwIy7qp6BY1wYkj-qlnY7dNOv8t7B6bPNvERMpl3ewykWCEI0sNSMsjZ2I3kQvVsjO2TXMndU4O274lZuxqO9dE1u3ir_YOIHHVRmWDoWM0d4sT4WlMSIQk41VNpc-hUsHmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غنیمت‌گیری یمنی‌ها از مزدوران سعودی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/691596" target="_blank">📅 08:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691595">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d2f454f3.mp4?token=PjkeHMnXY4XdM4A4D5j8_elk9o9gusNYpgvbZFwQgKEJZQprwAGOqV8fFKBDogiK2KwCaLuJdyDIIuf5-AW5yGvl0HLb0XPz8xc7FemfVWcWEOBSL9Ve2LkCN9t6eB3n7DEWno_uUp1ojWDuykRmg3HferQy7VvmMA3k9RBgoXXf30ZcBPUBHvALBAL8fm2BUz9KcN4yA9KPuxGdIrUeTNqAESVnRfxfPfBwd9U0fbz_otAH-PMwzhkIg8-FuzfLDatiWRBCKGJm1rlK0qX7VgUjQb5kY95CH37EgmcTHA5cWwduxsh4Re9kF7VGIYJs2oWc9YsMrSglH67byBGICw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d2f454f3.mp4?token=PjkeHMnXY4XdM4A4D5j8_elk9o9gusNYpgvbZFwQgKEJZQprwAGOqV8fFKBDogiK2KwCaLuJdyDIIuf5-AW5yGvl0HLb0XPz8xc7FemfVWcWEOBSL9Ve2LkCN9t6eB3n7DEWno_uUp1ojWDuykRmg3HferQy7VvmMA3k9RBgoXXf30ZcBPUBHvALBAL8fm2BUz9KcN4yA9KPuxGdIrUeTNqAESVnRfxfPfBwd9U0fbz_otAH-PMwzhkIg8-FuzfLDatiWRBCKGJm1rlK0qX7VgUjQb5kY95CH37EgmcTHA5cWwduxsh4Re9kF7VGIYJs2oWc9YsMrSglH67byBGICw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این تمرین از شانه‌های افتاده و قوز پشت جلوگیری کن #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/691595" target="_blank">📅 08:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691593">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRCzjerYVAuK8OfM4ZYUnWCtMFCkpozqbH0YGttgY-8YnnfE5Z1pmu9_WsmWxco6PHVqJKkA5un0djkcBZ_LqmzwvY5FLrkTHbhpu9_zkRwaIl82i3_yMpT5KS490y6rwkNrDtFxblXJTL_2mkjzO-wM_2FW3f66qUsJ9hr6lpI1PRxbf2ESiyrIaMV00iKGm-hSVRsdKDhED4NarV7hf8hoVAryHIK0fCFbuIjC_9vsIYqaxtk-8EqrOUjaHpQxldV_50BmgUzkgSMPHYr_vjfNd3NHsAqB0nIVXgKQO5HbUJ5pGOn22EKTsi7gkvpSvgcPsfguq67g4XlvRmMaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انصارالله کوه «راسین» در غرب ال‌تربه را تصرف کرد
🔹
نیروهای انصارالله کوه راسین در ۱۵ کیلومتری غرب شهر ال‌تربه را به تصرف خود درآورده‌اند؛ پیشروی بیشتر به سمت ال‌تربه می‌تواند مسیر دسترسی به شهر تعز را قطع کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/691593" target="_blank">📅 08:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691592">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سخنگوی سپاه: برخلاف تصویرسازی‌ها مراکز اطلاعاتی واشنگتن قابل‌دسترسی بود و این مراکز در حاشیه خلیج‌فارس و شمال عراق مورد حملۀ ایران قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/691592" target="_blank">📅 08:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691591">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
فروش نفت ایران در شهریور امسال از ۳ میلیارد دلار فراتر رفت/ این رقم بیشتر‌ین میزان ماهانه در ۲ سال گذشته است
🔹
طبق آمار سازمان برنامه، درآمد نفتی کشور تاکنون بیش‌تر از سقف بودجه محقق شده./ فارس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/691591" target="_blank">📅 08:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22e97a268.mp4?token=iz2hRnX-47EuRsRU653mCrR9I0U8ChksHdAN09Ma-EWTBLRL1MZDjhe_hY_P6E7W1UlJFC94sIRjNJcq-APrsh3pKT7ETZuptFuVzPN_0YCi6-uoFh8HPW4MwFVQpZDyNyC1q2XVKVLSfNCucMnrDHtpNQxySxsJpXz4w17ai7VMzKuv0Fr3WlPyOGfkCxK2pRIPvLPB6npxPgy7KonujjYnB0z_eSNLp2jPtI99-cl2PDN1omnuuAZ0JBro2Wcpw7_iB6LA-dJbyr090CIxNNxM0Z2lhRn5mi3jRTuehtC12h5oJythgLhDQLCMGpfL-ZDaSd9eGzW42pHFC6j4-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22e97a268.mp4?token=iz2hRnX-47EuRsRU653mCrR9I0U8ChksHdAN09Ma-EWTBLRL1MZDjhe_hY_P6E7W1UlJFC94sIRjNJcq-APrsh3pKT7ETZuptFuVzPN_0YCi6-uoFh8HPW4MwFVQpZDyNyC1q2XVKVLSfNCucMnrDHtpNQxySxsJpXz4w17ai7VMzKuv0Fr3WlPyOGfkCxK2pRIPvLPB6npxPgy7KonujjYnB0z_eSNLp2jPtI99-cl2PDN1omnuuAZ0JBro2Wcpw7_iB6LA-dJbyr090CIxNNxM0Z2lhRn5mi3jRTuehtC12h5oJythgLhDQLCMGpfL-ZDaSd9eGzW42pHFC6j4-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع انفجار مهیب در شب گذشته در یک انبار مهمات موجود در استان حلب سوریه گزارش می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/691589" target="_blank">📅 08:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVea5NeaRFY67lADXzfodbiAUaiY6olGW9CM97tNJ5vUgNcaTP3gDS_dtYhoGL1oMS0I6S8YTGqtHwoEQfS0tNW3rWD7qj0WU4blFfTw7b6Cnl42ph_nJ51VCxcA0cXGCNrsMrm2O846pZE847Olt3SQQE8Y-zUMmJ5iRZcIwL7SQew9TJNsfRUdI1bpGUX_Zc0hOAAJBiJUj3xWlLR-VMZMupUDkcaQyLiqjai14UpmyWUqs_JM1WOcqth2s_zo9AgZWyiAzPjZKq4YFJ2kqZabQICYZmuX3995GbedRCJ0Di1t_6jjB4McE43P185VPSq4DEh6eQnr6H6pVtQCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر پاکستانی: تنها دلیلی که بچه‌های مدرسهٔ میناب و رهبر قبلی ایران الان زنده نیستن، اینه که ایران سلاح هسته‌ای نداره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/691588" target="_blank">📅 08:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691587">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ترامپ از حمله به انصارالله منصرف شد
🔹
ترامپ پس از آماده‌سازی پنتاگون برای حملات هوایی علیه حوثی‌ها و تأیید فهرست اهداف، در نهایت از آغاز عملیات منصرف شد. طبق این گزارش، برخی مشاوران ترامپ با ورود آمریکا به جنگ عربستان و حوثی‌ها مخالف بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/691587" target="_blank">📅 08:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691586">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
قیمت نفت در آغاز معاملات هفته جدید میلادی صعودی شد و نفت برنت با رشد حدود ۸۰ سنتی به محدوده ۱۰۴.۷ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/691586" target="_blank">📅 08:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرفوری
pinned «
‼️
خبرفوری/ انهدام یک پهپاد MQ-1 در آسمان تنگۀ هرمز   سپاه:
🔹
لحظاتی قبل یک پهپاد MQ-1 دیگر ارتش تروریستی آمریکا توسط آتش پدافند پیشرفتۀ هوافضای سپاه در آسمان تنگۀ هرمز رهگیری و منهدم شد.
🔹
این مدل از پهپاد آمریکایی، چندسالی است از نیروی دریایی و هوایی ارتش…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/691585" target="_blank">📅 08:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
انتقال سهمیه بنزین به کارت بانکی از مهرماه
🔹
سخنگوی کمیسیون انرژی مجلس از اجرای آزمایشی طرح انتقال سهمیه بنزین به کارت بانکی در پنج استان از ابتدای مهرماه خبر داد و گفت این طرح تا پایان سال به‌تدریج در سراسر کشور اجرا می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/691584" target="_blank">📅 08:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691582">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYRsh4e-AjFwerONiBP5O0aX78UisEPMAfbrNgvncXxz_aU6XL_oJcaekUXguL9dJDRl1Yxg8NC8S8ZmdVP76bGA0h3Gb6ACZRjuagf9hXcMsMNYBz3JLhmGVVJyrH-560rDNBU4AfhIs0uOsN_BCMFLb5CEf79imtuUsphMp5OrSi2qfOUIYQRFc3hP7q1-PWtcq0gzf2NRl60RwXHsmK-d9bF4jmlzyxcNS3_4SdMelKcDij9iXFPBZxcim9z-VexumbUXyZtcRo24lWne5WmBjLdPcUXIR-BtCReLxdjzx2Vic21l8OaHUIqQC-y5wTINZJWf6gLZIzJ_YGv6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت‌الله شبیری زنجانی دار فانی را وداع گفت
دفتر آیت‌الله شبیری زنجانی:
🔹
روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/691582" target="_blank">📅 08:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691581">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
خبرفوری/
انهدام یک پهپاد MQ-1 در آسمان تنگۀ هرمز
سپاه:
🔹
لحظاتی قبل یک پهپاد MQ-1 دیگر ارتش تروریستی آمریکا توسط آتش پدافند پیشرفتۀ هوافضای سپاه در آسمان تنگۀ هرمز رهگیری و منهدم شد.
🔹
این مدل از پهپاد آمریکایی، چندسالی است از نیروی دریایی و هوایی ارتش تروریست این کشور کنار گذاشته شده و جای خود را به MQ-9 داده، اما حالا با توجه به انهدام بخش اعظمی از MQ-9ها، آمریکا دوباره مجبور به استفاده از این پهپاد شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/691581" target="_blank">📅 08:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691580">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNwGb-aUIY3J1etUk7i8E02gQR1p3OBSAi3jaF95xfVs6qJDPhk2lCibDdJY5XadTQVQlIYT0Z_swkefgBCg4p-FecOEYTF_06RLmduwsSjSJeJcWgwLimQltr-9jcH3sjoQ8MSqDN8r8lcK9b-NLZq73GnTBDJf4zzvs5_EshfK2kgF0ox3QP0dgsOLr8eNpKz7_peC5D5fYn_L1E1A8WRu0dB8J8NWJOLBuDPAH4ZCJAFD6ZpAWKUnWDfoXHCiNJoRHUDgnwyKe--7lhRS4tc0icfCj4pUoy28L-A4SitAbIC2BiVuZ9hIXnCwx7m6pJSpk31KG_K6aW5k0Izj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۳۰ شهریور ماه
۹ ربیع‌الثانی ‌‌۱۴۴۸
۲۱ سپتامبر ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/691580" target="_blank">📅 08:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691579">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qA_8VfFWL29LP7aIsZzqOP5aqkUjQvgnLBpDU7zi6Lp5YySP9YF20VntqIwZYJHzsdMBBbZrmzp7qodfx1Nc0b9fwTATA820nATfrbhoyz8uje_MLWRtXxasoShfy3J0Fwp7PiH5DZcx_Ce2wVlt6lnqRjef_CVYO2j2Q4kpMltGmxjUNynjJ3RbybRqIbYR3g20xsvv4XRurytiYuLhzlgfgJW9glZqbhGtSl2737zIM8D2v8-iMnvkheAT1CCtj5DS9ZrHanVDwJXDwE70Jhtth5KvIHiXLPkbJJ-AyX54Y-oJAmP-jeiwvXP2_3FR_j_eMAibILPdCLV5j5fuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥾
نیم‌بوت مشکی مردانه مدل Sorush | شیک و کاربردی
مشکیِ همیشه‌ست، مناسب استایل روزمره و رسمی
👌
✨
رویه چرم مصنوعی
✨
زیره PU سبک و مقاوم
✨
کفی پرسی و دوردوزی‌شده
📏
سایزبندی: ۴۰ تا ۴۴
🖤
رنگ: مشکی
🔴
قیمت: ۱,۸۵۸,۰۰۰ تومان
✅
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه کالا
خرید تلفنی
👇
https://memarket24.ir/product/fast/63746/180124/</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/akhbarefori/691579" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691576">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6c245cce.mp4?token=XNgNWqUK8lVV0ezNnbQxvsd1huPF_1j9rMbpAuYueuoGNxDc0_NkVyl17Od3nvyvICfqP1as9TOhmO5OUWtSqt9CwtQIW_2lfN9d8_WF8lidI2X7s-idHpPUVXkY-Q-oc9ZaaMKSkBn1ugH0gWG1jXQg4uncQD73R9GG-wbnWSTa9s_gUw6VwApQ1spEYbwL1y41Q2K7EyIuNpPS3_8i6PBMrJDFEg_QeArHl3qvZw5cS_rhCEX_nu7hQyS4cEDNSFfmUdaeBfEqB-HoGT7OvHrcMGXwnJHM4IGYZfN9ofMZZcG-ZBb-imzmlYlusTVO5og1O-yEZu8Gxj5skE3qEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6c245cce.mp4?token=XNgNWqUK8lVV0ezNnbQxvsd1huPF_1j9rMbpAuYueuoGNxDc0_NkVyl17Od3nvyvICfqP1as9TOhmO5OUWtSqt9CwtQIW_2lfN9d8_WF8lidI2X7s-idHpPUVXkY-Q-oc9ZaaMKSkBn1ugH0gWG1jXQg4uncQD73R9GG-wbnWSTa9s_gUw6VwApQ1spEYbwL1y41Q2K7EyIuNpPS3_8i6PBMrJDFEg_QeArHl3qvZw5cS_rhCEX_nu7hQyS4cEDNSFfmUdaeBfEqB-HoGT7OvHrcMGXwnJHM4IGYZfN9ofMZZcG-ZBb-imzmlYlusTVO5og1O-yEZu8Gxj5skE3qEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برندگان مسابقه عکاسی میکروسکوپی نیکون ۲۰۲۶ معرفی شدند
🔬
🔹
رتبه نخست مسابقه «جهان کوچک نیکون» به ویدیویی از تپش مژک‌های ریوی یک کودک مبتلا به بیماری تنفسی نادر رسید؛ دیگر آثار برتر نیز تصاویری از لارو عروس دریایی، کرم لوله‌ای، تقسیم سلولی و حرکت میتوکندری‌ها را به نمایش گذاشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/691576" target="_blank">📅 00:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691572">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K7ieKk6qDO_IV9E3QM5QQ5Vy-L2bNR0ub5J3455LPQbuxa9amzzceQmFgpNlP5UsN6VQgxVYt0FIJN064BsNQNKoxSWoXDjmsLoGk6Y-WMUT_NXimrxWuR9UWtugiOJHqhnAiKKt8tDWYEZJdndZh_nmAC4GK5H7PFIZCmXwTw5qpDfo3_hZXMamrsDK-vScgeCZr8MaVLDzD2f2vtBC8pD-ZOUhLI7YaB0lO6nYGx1Dzn9b2WYLbgvNP4xEn9DiSqa8_o0qzyxO_QnusoVAmLWFhWGMDoA6FZofZavUnyfltFsDocHNXYZMQaT-TFnH-orTB4SaX8ax_-ZbNeUBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8kOhv3LtihkvshZ9maRMSOXybh4Vvw3cANjGXw9G1ggg4kJTyus5xxAIPT1qtibYbuRMJNcTTvMDm97C3-MTjxsZIlZiWwQiZR2yhqxt7K88hlrDuA_yOPxhifsxbFjoXxehT3gBgv612Enpk9FD603Dmx8oxwGiGEGqmAxtLloO3xK_5f_UB5cMqIFJRSzKozHZdavyqNua-5ZWQGVuKpiG3M5AwjbCuLFeTJwgxVUP_bYvSoQbwKj2V_hbwMZb0VkDDb59LH14GbTdFvCpGNK8n7PO5xcDzyxQBJHaz1Yi451vZq9WFrPxFVO-kdcFHg98e35p_39vu0Gk1s-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PtekfxAVAEPo98PZiO1RzaJQwcPOflmD3Rly-EHPGfPcMKANiVsmGz8TV-36lnEnlwi93eimwVFqG4i7xy6sLwEcsvo5as6BE2Zy4RmR9yrOpHvGCaK9l1d-KgMUctBng3FTJ09m4RCEHLtCk4axo43SLAKWYfJhGixUgOBLb2V_pcpXFx-p23o3WgRF-oBsMUGBaHosFXbzrVWE-tiSx_hS1y72PJ1DlC8TRYXpuoNacBUqtnpLJceKtra2oC6xPNpk3NGxwXmJz895VQKimrSERKm0q3t_esGSdGkBfhZHnW12I8RjW7FUAwcDsthZ7xyuua4zJvigWDRKfVppDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4_fnlutyXN4wI9dZFgkb6jHRV4VLuNISaAFuy8g2TiR8OuXxmT6B6A3Q1nrI_cnhQGbZZW7NsEm9OWGWe6OAaAy-0GZpBaLNKsYitUQKQCi-crry1hX-rQL9Ycj-DahyPKu_5jxBip2S0yjHmiRqSQvDKCvcprzZhsfgDIH9270wyMnrUrOnbIpl765IxYpH6WK8fmnnAPsEQNcind5rHgQ-3KXlXVRoA0EsoQacM7brhEtZOzeI4rmiYNe4SDrl-tCpfmkrywgFwg8D_2wNqOxV-WFKrj0WItEoTVtX8Bp3AhacwgK_2cTG15dlgiwDU88DC5Th7iCcPlqEkA20g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
خبرفوری/ انهدام یک فروند پهپاد شناسایی پیشرفته اوربیتر بر فراز تنگه هرمز   روابط عمومی ارتش:
🔹
ساعت ۱۸:۳۰ امروز، یک فروند پهپاد شناسایی پیشرفته اوربیتر با آتش سامانه‌های بومی نیروی پدافند هوایی ارتش در منطقه جنوب شرق کشور، تحت شبکه یکپارچه پدافند هوایی کشور،…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/691572" target="_blank">📅 00:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691571">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری خبرآنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2064b90d.mp4?token=qmIcTAj_Cy2L7_M4cCUyjai5XkXyAhTZyuiQ400VB7MiuKYSFIwdzRZ3lEaAWSauFcc8dbjKqliZk8KvhQPfsFWHe8wNu-uJ2js7tlFBRGb_TuPL1ydPTX8WYI9OHJfuhM5Q39YeIZ97wTDunnOOeWyVxpLw_dheQf8Y1P9z2M-C9zL7ZC_frkqgp26DsODXjTwg_eBizxudXnsT2k0Mz8A1aHCAXtwNIELNrV4rHAeb2it81V3jGUC-mWVmY-pVVN6D58dPwsHJLnjf1UE3NHwb4jd1wzkKFAfZYASZXFKkq0noquQwQNZhMtTyoOUC2gAqqHCRgjL1tvJzH2UAGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2064b90d.mp4?token=qmIcTAj_Cy2L7_M4cCUyjai5XkXyAhTZyuiQ400VB7MiuKYSFIwdzRZ3lEaAWSauFcc8dbjKqliZk8KvhQPfsFWHe8wNu-uJ2js7tlFBRGb_TuPL1ydPTX8WYI9OHJfuhM5Q39YeIZ97wTDunnOOeWyVxpLw_dheQf8Y1P9z2M-C9zL7ZC_frkqgp26DsODXjTwg_eBizxudXnsT2k0Mz8A1aHCAXtwNIELNrV4rHAeb2it81V3jGUC-mWVmY-pVVN6D58dPwsHJLnjf1UE3NHwb4jd1wzkKFAfZYASZXFKkq0noquQwQNZhMtTyoOUC2gAqqHCRgjL1tvJzH2UAGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
رئیس صداوسیما از همکاری قوه قضائیه برای محکومیت یک پلتفرم خصوصی تشکر کرد!/ حکم علیه آپارات بی‌نظیر بود
پیمان جبلی در دیدار معاون قوه قضائیه:
▫️
با همکاری قابل تحسین بخش‌های مختلف قوه قضائیه توانستیم حکم قطعی محکومیت آپارات را بگیریم که حکمی بی نظیر و قابل استناد در مجامع بین المللی است که برای احیای حقوق بیت المال صادر شده است.
درباره این حکم بخوانید:
⬅️
رای علیه آپارات مبتنی بر مسیر درست حقوقی صادر نشده!
⬅️
صداوسیما می‌خواهد رقبای دیجیتال را حذف کند/ امروز آپارات، فردا کی؟
⬅️
انتقاد قاضی دیوان عدالت اداری به حکم دادگاه علیه آپارات
⬅️
بزرگترین ناقض کپی‌رایت، شاکی کپی‌رایت شده!
⬅️
صداوسیما به‌جای رقابت، رقیب را حذف می‌کند
@KhabarOnline_ir
|
khabaronline.ir</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/691571" target="_blank">📅 00:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691570">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvCp-UXKgApCoQw5yMe7KgpiFAkimEhvqvHE9lzshPgFI9hZ-IK1ke4nBBbbXEEe_RXXj6VqcXcXEXgEOsgZq_g6lP7JUqQN5fHbZ10Zh5RD3QQqNAaGmxTtonspqQ0J1bHAT1XD_mgQgg8FAi-hEaAeImdVKlHEabTZje-ZgHac9LGiwTdVf2oOoi76mhn7bkkqN5dON5_Fi4vCsO_1uRJP6rFsPrBMkyCS3T7Tmy0OMs1kT3Vs3CLVDmXe7ZSPlx7WXpb6J_KeBfxGUOHp0QZY6EOkReNknf2RSbVdfBKDw5CfIPC6D-OYa6EL5AR6RAMmiP2zEAwn2DoA7P7UAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/691570" target="_blank">📅 00:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691569">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/addd96b83e.mp4?token=eG1db3-YLu_7W3nbvC0DclEvSPGgoEO_rE0bZ2mZRztfl9BESgTWu5jq8QZZjdp0LRWR7c9iC09siFFuN_bGQe6YSkfcs2AVBm-4HjPKmz_G4nyMI0LSr_i4JHe9VTVhY4jL6iKvQUbSNJTAO08Mjg81jqWP7YaUBSzVGyyxFA309L3BNCDSXk8ddnu0gkNIs5DzudIMlKDdt6b9YTmpJg5sE7xNbEMuBpCkHWivUIqNmeHMypxrO9Y4tmwPEGLialkNQkImUaLFOQj-ZbOLQabogc8L-2yv2vn44Vgrro6vkMJVoxnpsG7AFzS_qK-WIOsO0m9NvwDR-5TMAgvmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/addd96b83e.mp4?token=eG1db3-YLu_7W3nbvC0DclEvSPGgoEO_rE0bZ2mZRztfl9BESgTWu5jq8QZZjdp0LRWR7c9iC09siFFuN_bGQe6YSkfcs2AVBm-4HjPKmz_G4nyMI0LSr_i4JHe9VTVhY4jL6iKvQUbSNJTAO08Mjg81jqWP7YaUBSzVGyyxFA309L3BNCDSXk8ddnu0gkNIs5DzudIMlKDdt6b9YTmpJg5sE7xNbEMuBpCkHWivUIqNmeHMypxrO9Y4tmwPEGLialkNQkImUaLFOQj-ZbOLQabogc8L-2yv2vn44Vgrro6vkMJVoxnpsG7AFzS_qK-WIOsO0m9NvwDR-5TMAgvmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعترافات بهداشتی که هر کسی باید از آن‌ها اطلاع داشته باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/691569" target="_blank">📅 23:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691568">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
پلمب مرکز زبان وابسته به سفارت فرانسه در تهران  قوه قضاییه:
🔹
مرکز زبان وابسته به سفارت فرانسه در تهران به دلیل فعالیت بدون مجوزهای لازم و پس از چند اخطار قبلی، با دستور قضایی پلمب شده است.
🔹
اتهاماتی درباره استفاده از آموزش زبان در پروژه‌های مرتبط با امنیت…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/691568" target="_blank">📅 23:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691567">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5344568a53.mp4?token=JjwPxqkl59rCXV05Q8izyLD2sM9JFPVhxd7lDfeRN67_34QaeEBTnHfW3W6RMt84YH9qYi_U82l4IRp3i7pd677bITOl4A0_Tgqj1fgIkNuhIGpTzGjNzoFiVXiSzb3wD8p75bgFw0OQ6-CtLUf6X2HKr3lPWjOVXrIy6PQT1OyesXWz1uVIPDL8mXjz_DidG6aYMYb5bZZdBWXaUgT0oK7fdH_keQKaJlz6rjb0I-ivKlsGvEZuf-e8RiSUmop9QgUib1HjBjV8FqpY-nuda4IdcedqhkNPaw9c4_DpfeDVRe5jzQ1zFIKhVm9z1oMONP8FdpezBaz9CZuFr6dJ4WlzIsdHWyXXUJpePjAE4snVWnIubVRZS0pHrZU7t1rjf2g1EovXeXbugPymw416AvZ7QN4kaqw08RrmMaOvkCKeGnuuN_lo9jNGsScBOWJepA6J8L5Fnj9uJq8qSWCfFzqS4KbPlLp_UKmXWZ8yLY7r2Rssdy73iChShXf_oem15zMH5SEVMg_5gd9wEZT6s3_12ZHCuwCR7NTBNFr3gQ6UJ8F7dJ93xR2-7nDxp9wI6Ouiwp6Hw419dmU5VLzM9S8niQtQvOBR0z7vcyAz8LhcBynbV943a1Xw7ossPZ_pxvBxwI9MvOdYNnecgGke3OZtaO7AVrksax1NUNCccSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5344568a53.mp4?token=JjwPxqkl59rCXV05Q8izyLD2sM9JFPVhxd7lDfeRN67_34QaeEBTnHfW3W6RMt84YH9qYi_U82l4IRp3i7pd677bITOl4A0_Tgqj1fgIkNuhIGpTzGjNzoFiVXiSzb3wD8p75bgFw0OQ6-CtLUf6X2HKr3lPWjOVXrIy6PQT1OyesXWz1uVIPDL8mXjz_DidG6aYMYb5bZZdBWXaUgT0oK7fdH_keQKaJlz6rjb0I-ivKlsGvEZuf-e8RiSUmop9QgUib1HjBjV8FqpY-nuda4IdcedqhkNPaw9c4_DpfeDVRe5jzQ1zFIKhVm9z1oMONP8FdpezBaz9CZuFr6dJ4WlzIsdHWyXXUJpePjAE4snVWnIubVRZS0pHrZU7t1rjf2g1EovXeXbugPymw416AvZ7QN4kaqw08RrmMaOvkCKeGnuuN_lo9jNGsScBOWJepA6J8L5Fnj9uJq8qSWCfFzqS4KbPlLp_UKmXWZ8yLY7r2Rssdy73iChShXf_oem15zMH5SEVMg_5gd9wEZT6s3_12ZHCuwCR7NTBNFr3gQ6UJ8F7dJ93xR2-7nDxp9wI6Ouiwp6Hw419dmU5VLzM9S8niQtQvOBR0z7vcyAz8LhcBynbV943a1Xw7ossPZ_pxvBxwI9MvOdYNnecgGke3OZtaO7AVrksax1NUNCccSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قزوین؛ میزبان یک پروژه راهبردی ملی
🔹
طرح دانش‌بنیان احداث کارخانه ۷۵ هزار تنی آب اکسیژنه با پیشرفت ۵۰ درصدی و بیش از ۶۰ میلیون دلار سرمایه‌گذاری بخش خصوصی در قزوین در حال اجراست.
🔹
با تکمیل این پروژه، قزوین میزبان بزرگ‌ترین ظرفیت تولید آب اکسیژنه کشور خواهد شد؛ طرحی با ظرفیت اشتغال بیش از ۲ هزار نفر که گامی مهم در کاهش واردات و توسعه صادرات است.
🔹
حمایت از تکمیل این پروژه، یعنی حمایت از سرمایه‌گذاری، اشتغال و توسعه صنعتی قزوین؛ یک ظرفیت استانی با اثرگذاری ملی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/691567" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691566">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyiDAQ7kIgj2x9j1EdgyE3k-15OWZtC-c0zDoqZNo1PogKGD4jQ74ZwRjET4g-zPJGXc_KV4-wghTMj1Lc0PM2H19kELF2QHYT8_70vNua_tcGqKU1IK4nLhhHchd1ggBmP4UI9ozQyjXQDo1ws5n_aorz0kWrBxRkfsRigpiWPOlKiLIKzB76_Dyu58RYFy99EreBSsaB83iKfdxkS3uYofLgxVni7Bu5J-sT_o_CibVH9qfGs4f3gnUUjfauwg1-vGuGq06uDbeIwucV79vSQjSRfxLoLVNz05OgyBKCJxRpjZjQOHgRJdyxIZKpxfOcUP_idx51Fblg06Eh8agw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
احمد ایراندوست (بازیگر) از بازگشت شادمهر عقیلی به ایران در آبان امسال خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/akhbarefori/691566" target="_blank">📅 23:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691565">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067fa96a68.mp4?token=dCR0gkqHz1Nule7zxoRm3yzQ11sMBL6pXjPqG6dxvN41MoW9cOucik9_jrYK2U4ha3amSFMkjlNm7dOnhSn28wApnd6kTHUEGAZ_ZNpEZjTTlHXMAV0GlqtEdcf5aSjnAF9RhNCOZAexgcNIG0HPp0o5S3XCq6nQw3mDdjmLbmpI83gcWm2Bec0p8MtMGnVL6KoLg0lQFuG-SG9TgdRVg_LjUZlJzfOZ89vEhWdciNwSX1w8vtpUpQVoMtq1A_Pylc92q98H1xemqlr0L46TeAsefr5JDCt_Cdyzes1E6HhQy_UdlBtw4e4nMuY8Nx8Wmagonxp7TvOb1Pq67ZJBRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067fa96a68.mp4?token=dCR0gkqHz1Nule7zxoRm3yzQ11sMBL6pXjPqG6dxvN41MoW9cOucik9_jrYK2U4ha3amSFMkjlNm7dOnhSn28wApnd6kTHUEGAZ_ZNpEZjTTlHXMAV0GlqtEdcf5aSjnAF9RhNCOZAexgcNIG0HPp0o5S3XCq6nQw3mDdjmLbmpI83gcWm2Bec0p8MtMGnVL6KoLg0lQFuG-SG9TgdRVg_LjUZlJzfOZ89vEhWdciNwSX1w8vtpUpQVoMtq1A_Pylc92q98H1xemqlr0L46TeAsefr5JDCt_Cdyzes1E6HhQy_UdlBtw4e4nMuY8Nx8Wmagonxp7TvOb1Pq67ZJBRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: آقای قالیباف تمایل به پذیرش مسئولیت مذاکره نداشت اما با اصرار پزشکیان قبول کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/691565" target="_blank">📅 23:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691564">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای علی قلهکی فعال رسانه: آمریکا اصرار دارد ایران باید تا ۴۵ روز آینده وارد مذاکره شده و همه موارد از جمله هسته‌ای را توافق کرده و امضا کند؛ تنها امتیازاتی که آمریکا می‌خواهد بدهد «رفع محاصره» و «آغاز نکردن جنگ جدید با خسارات زیرساختی بالا» است. باید دید ایران از مواضع خود عقب‌نشینی می‌کند یا نه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/akhbarefori/691564" target="_blank">📅 23:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691563">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
آمریکا رسماً از شورای حقوق بشر سازمان ملل خارج شد
🔹
وزارت خارجه آمریکا این شورا را متهم کرده که به ترویج آنچه «ادبیات ضد آمریکایی» خوانده می‌شود، می‌پردازد و در برابر رژیم‌هایی که به سرکوب مردم متهم هستند، رویکردی مماشات‌گرانه دارد.
🔹
این تصمیم آمریکا یک…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/691563" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691562">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک منبع آگاه: ترامپ در گفت‌وگوی تلفنی امروز بارها از زلنسکی خواسته که حمله به پالایشگاه‌های نفت روسیه را متوقف کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/akhbarefori/691562" target="_blank">📅 23:24 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
