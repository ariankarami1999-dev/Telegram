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
<img src="https://cdn1.telesco.pe/file/iJGRUo8UodtOG0uSs40uPHuuESwi33zZducNjZtmhHsZeV7V8AqbNHaxdsQ7S4AzGN1i5qeTsNPthZr0fgRUQQ40eYDibdRyKZ119s6kwX32hI6JZf7npxNI9k6tgXwC1SbwXlvb7fpDZ3rSLW36zPQUqirKi-95sFnqvr1J8_5r7U6t93-NZPVfyJFn56rV_NVMLHyZ233LBy8hlKDiJDmlpj6oCOgZr-PBcVtORHQ9YLigrYHCrXp6e_KEyZbfhGSL3r6iE2l2hGee0V8PVh3z_xYZnFbblAXwpdKz1AOt6JiGLuq30zj10rGIy9YoAd8xZOttxHRCnno364l9jw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-4343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/MatinSenPaii/4343" target="_blank">📅 16:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4342">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=QwFnzFtNfmtbwWWA3fAitUwtuM5ONu1eicfzX6Td7WN0zurXJ2jlbkROg90EwjALLRj_4XMDS3ZpCCDIzBHJBpjkDi4Vl15hdmXBjoB3alSQjITp8LscvO74gA4qzYE8DtLmHA5DsdfcYaYAYIP9VT43AT0g-NDYfwTBCYU_JIw7kwiTz4J5i9iz2AsgXv4sO720phvZjxmB0X3Oln3dU2uwTMOH-5TE96D0S4zqDnSyQZE-iLGq142sTa7fuM6b4941j-cPniKWspK8Le5t5wCrytKTflhsaaZY7lsHtqB7mTKScNG0A9MhosGx9aw8jJIBAbog6ijcgxalZDVPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=QwFnzFtNfmtbwWWA3fAitUwtuM5ONu1eicfzX6Td7WN0zurXJ2jlbkROg90EwjALLRj_4XMDS3ZpCCDIzBHJBpjkDi4Vl15hdmXBjoB3alSQjITp8LscvO74gA4qzYE8DtLmHA5DsdfcYaYAYIP9VT43AT0g-NDYfwTBCYU_JIw7kwiTz4J5i9iz2AsgXv4sO720phvZjxmB0X3Oln3dU2uwTMOH-5TE96D0S4zqDnSyQZE-iLGq142sTa7fuM6b4941j-cPniKWspK8Le5t5wCrytKTflhsaaZY7lsHtqB7mTKScNG0A9MhosGx9aw8jJIBAbog6ijcgxalZDVPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مقدار زود شروع شد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/MatinSenPaii/4342" target="_blank">📅 16:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4341">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nYMk5ADsiEdTCtsFgaC3fPQXdr_slosakQZunDBCxzzxPLx_TQxIJodngaKoAYQLIdffSAZJJk-rbVlbyjPKtSDEy0zK-nVUAXyvQuZjaeMEduB_z1tQWk1uexNX4U4Uv_aeroXjNzoGElkMteCHfuShtcV3-v95ogwEYNtrMxY1vP_qX-07eZQ8G6-b93xQ7L_nneecLgUIHE1ycf2w9Wyx_qTIL7UzvzmgIJqawCdgd9w5dnzVmveCSV5LcC6nkg67lovlHpqkMLVJcWIrOH4msKllTun1REg8rOr_U2p8l6gCbLx75u865LpGilE03G3auDIykeQO9EA3A9Njyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارادوکس عجیبیه. از یه طرف انگار جدی جدی جنگ شده باز
از یه طرف اینور دارم آموزش می‌بینم و کار می‌کنم با ai
و نمیدونم همین آب باریکه‌ی نت کی قطع میشه دوباره</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/4341" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4340">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">احتمالاً من دچار "فرسودگی LLM" (LLM Burnout) شدم!
نویسنده‌ی این مقاله (الک سکولن) یه توسعه‌دهنده‌ست که می‌گه مصرفش از هوش مصنوعی در حد استانداردهای الان کاملا معمولیه، اما اخیراً یه حس خیلی عجیبی بهش دست داده:
خستگی مفرط از خوندن متن‌های تولید شده توسط هوش مصنوعی!
روند کارش این‌طوری شده که دیگه خودش از صفر کد نمی‌نویسه؛ طراحی می‌کنه، طراحیش رو به Claude یا Codex می‌ده، کدهای اونا رو می‌خونه و ریویو می‌کنه. علاوه بر این، روی پروژه‌ای کار می‌کنه که کدهای تولید شده توسط Qwen رو باید مداوم بررسی کنه. یعنی عملاً کل روزش با خوندن خروجی‌های AI می‌گذره. حتی برای سرچ‌های روزمره‌ش هم از ChatGPT و Gemini استفاده می‌کنه.
حالا مشکل کجاست؟
اعتراف می‌کنه که با این ابزارها خیلی بهره‌ورتر شده و قصد نداره کنارشون بذاره، اما تو چند ماه اخیر، یه بخش کوچیکی از وجودش از دیدن خروجیِ مدل‌ها وحشت داره! چرا؟ چون دقیقاً می‌دونه قراره چی ببینه:
فرضیات غلط، توهمات (Hallucinations)، جملات بریده‌بریده‌ی اغراق‌آمیز، و
✨
استفاده‌ی بیش‌از‌حد از ایموجی‌ها
🚀
.
نکته‌ی جالب اینجاست که می‌گه انسان‌ها هم اشتباه می‌کنن و می‌تونن رو اعصاب باشن، اما مشکلِ اصلی با هوش مصنوعی
تکراری بودنشه
. مدل‌های زبانی دقیقاً با یک لحنِ واحد می‌نویسن و دقیقاً یک‌جور اشتباه می‌کنن. سر و کله زدن با یک سبکِ کاملا یکسان و اشتباهات تکراری، اونم به صورت هر روزه، کلا فرسوده‌ش کرده.
این دقیقاً نشون می‌ده که با وجود تمام شخصی‌سازی‌ها (Personalization) و پرامپت‌ها، هنوز هم اون امضای پنهان و سبک خاصِ هوش مصنوعی از زیر دستمون در میره و وقتی تو طولانی‌مدت باهاش درگیر بشید، می‌تونه حسابی روی مختون بره!
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4340" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4338">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bqb7DCuWJRuSRdy12a050ctUykki0cb8eN68qaYABeSaD-wxGf6nPOkgObyWzFAmV_aQTPPZ__5YxzI4U0dN1cZZyIWpY5O3wC_6Iq5X6-YeyFE5Gi39g8mEZyFI7wpopnfeevuCoCOtLvbqQUMq1F1bUJ4hcebyfdd0tqrnqYMVswD3tjMtXOWiAfF0bppYNYzC62G3VkefwEOQ5IIXLP_rPoRvENZ9x3z0eWKN0KeC_wwi5RMDH00yhEakt-XuT-fJ8YL1laujG8V7bXSVAyS9dZSHo45LjA0nTfHMACwePmG3NyrkxwH3aPVqGr2n1M2noKPtxkQwQttZ_1j2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r_t-IKasbSwoDRcvW9pKQAVcLKZ3WPYT7xCWzw0OVXwnrt2POlvV3-y-Bk6ibqDoUsfjBabn8Ia8kLNopW_bSBgc6551vsKbZM-KUbRvnNPRGf4Pal9ZE8wUeEJEtioua30DiW-0_0zHknZinTiNCCi6kCFG3sVMslfvVzfoU4wWpTBUxuHhS_wknDNR1iTI7se2T1291BJoz8mxRR0Tu-FROvaAPGMwF6aecLA0Z-Yofs83d7eUApZwpVe6RBwgJI-qH3--ZKmT6TYMx7InyDPnHGp27d0lfynm9uhEO7HqOspNngGmTXXcF2vRIjl98RpPr6J4PnM-2BcYxOYbuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI  مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:  • Kimi K2.6 • MiniMax M2.7 • GLM 5.2 FP8  بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:  https://infer…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/4338" target="_blank">📅 13:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4337">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=XlE9BrFKWn9Aqg6X54jd8im7bSeC-oWVHeF9fe5VpezZilAf5WSWVYWpKzKUY6Qx_IyD8Q8byzShPUNP0oIY6k4uj31onveuetPPoL8cGtwybJOnpuvmBplajGB46FbmfiizuZ48QDb1Kx3YoZIUQqEempp7_gxjGCStUgWCDzRyaycnG8mGNSi9uGME0LYEo78k3aWoCb5hbk26QCCXkVL0mmDgen9F4MfVwkV0YV76mKiDkJKgBTK5FTBnnnYeGBWn765MP1kOu2GJwVRI7vSYOm8nzQw_5Jhksry_PoAKn9yxtiB2x3WBjRcXysCHYKqQlcVzsp6xQp5kn3RaACPT4OVHaE7WtGk_eFAn9Ac4gLDXmlUAk_yCrcINjxNGV7rBx65RKhfwPxabnNYE529JI7i76Kz0CQ92dBhypeLfYeP7Rhxr9z5acDPp9HgrmI2eblkgU8pwE4qE20yrJ4fitZMipIEnmvBraP2v_K-n2uRapgrAP3SmCinC9-59swRgA0U9qHVPHemwvZJezbFCPcMGmdSkkw_sTPYPQd5qqhQh8XjeO7Qi1OyBOtkdILgUK0ljfXX_BoiCmnTOpHOq_UMYeUuogcDX8fZjQ1iVTRQPNi8EGuuFEUi06LvG7l9h4SNx72CW-PSHgB7m0RYZjZ2JW3v7BVU8AYz6AL4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=XlE9BrFKWn9Aqg6X54jd8im7bSeC-oWVHeF9fe5VpezZilAf5WSWVYWpKzKUY6Qx_IyD8Q8byzShPUNP0oIY6k4uj31onveuetPPoL8cGtwybJOnpuvmBplajGB46FbmfiizuZ48QDb1Kx3YoZIUQqEempp7_gxjGCStUgWCDzRyaycnG8mGNSi9uGME0LYEo78k3aWoCb5hbk26QCCXkVL0mmDgen9F4MfVwkV0YV76mKiDkJKgBTK5FTBnnnYeGBWn765MP1kOu2GJwVRI7vSYOm8nzQw_5Jhksry_PoAKn9yxtiB2x3WBjRcXysCHYKqQlcVzsp6xQp5kn3RaACPT4OVHaE7WtGk_eFAn9Ac4gLDXmlUAk_yCrcINjxNGV7rBx65RKhfwPxabnNYE529JI7i76Kz0CQ92dBhypeLfYeP7Rhxr9z5acDPp9HgrmI2eblkgU8pwE4qE20yrJ4fitZMipIEnmvBraP2v_K-n2uRapgrAP3SmCinC9-59swRgA0U9qHVPHemwvZJezbFCPcMGmdSkkw_sTPYPQd5qqhQh8XjeO7Qi1OyBOtkdILgUK0ljfXX_BoiCmnTOpHOq_UMYeUuogcDX8fZjQ1iVTRQPNi8EGuuFEUi06LvG7l9h4SNx72CW-PSHgB7m0RYZjZ2JW3v7BVU8AYz6AL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جالب Amir Hormati مهندس ارشد و پرینسیپال در گوگل در حوزه AI در مورد کدنویسی و Hard Skill ها، اینکه آینده از دید خودش چیه، چه اتفاقی بر سر کدنویسی میاد و به عنوان مهندس نرم افزار روی چه مسائلی تمرکز کنیم، جالب اینکه خود امیر از رول مدیریت به نرم افزار برگشته به خاطر همین!
✍️
Max Shahdoost</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4337" target="_blank">📅 13:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4336">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/4336" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4335">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن
مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/4335" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4334">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXNFxN6ftMD-A_4O0Y_xTosrH_HmrWyUu6_MX_5sR2sW5C9pvcM6uHcht8hADko-HenqCwLsBIArhR9zMUqCgqQUB83ZgXGwlN1dnJgC6UzEsHGy6RI7jbiKHUvmqxmkfYVUs6-tmDbneCJV4-rEhf_HQkCYxQUEiNxF0J4q6H3_VD67UU33V_W5-dseJ_VTIPRNJnAAOvH0SUMguvP9ob3GIV7788Byfv-qJ9IkUO2yP303tC4axZHCEuZf4DirndRArVVkosAAnW7thvDouHyNzgUkjuI1d-CE8Wqa-IZ51VFw41rSOSM7OKclZ-V6hsYovpMJmapZ2cEQS6UBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI
مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:
• Kimi K2.6
• MiniMax M2.7
• GLM 5.2 FP8
بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:
https://inference.dahl.global/chatKeys
💡
اگر کوکی مرورگر را پاک کنید، می‌توانید دوباره یک API Key جدید بگیرید.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4334" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sBBlsLkID0MJcRyIlIuTwvTB-OMVMszIYnvBj0FPhDtKFXKzERNCpLPDdADGZnn3fHIuiqlp3mcOzKbHRecFFX-enBrnkzkpyuKitxbYh3lPavDkV41pL1sk4u0olBZfb4ckuoj7C0CL0CKyytYCHum9kuVEbI-JCw0uOnRUHczipiMzYcOvFTsLrsVJtorCeoXg2zp6_52r5oUbjdqHuXFJDIS4e3EErao6c1Rcw-C-sYEbSGoMb5aZXem4t7_S8AvHL-a2bPN8DUQqtpQR_5DVQq9VxQVWkKG45VT_foF8gk5U7xQ_HAssHRCguxGh8YiyB-kGWP6wLR7SE4Vmug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست، کامیونیتی Rust هستن
😂
😂
زبان Rust برخلاف go و پایتون و... از Garbage collector برخوردار نیست.
نفر اول گفته انقدر سینتکس افتضاحه که دلم می‌خواد زبان rust رو بندازم توی آشغالا(garbage) و نفر دوم ریپلای زده که اگه بندازیش توی آشغالا کسی نیست جمعش کنه چون این زبان آشغال جمع‌کن(garbage collector) نداره</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4333" target="_blank">📅 12:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اگر می‌خواید اکانت Claude بخرید، بهتره بدونید علت بن کردن‌های کلاد distillation attack هایی هست که اخیرا بهش شده؛ و حتی کاربرهای خارجی هم یهو اکانتاشون بن شده. بهتون دوتا توصیه می‌کنم.
1- به هیچ وجه از سایت‌های ایرانی نخرید. و حتما بدید دوستی، آشنایی، چیزی بگیره از خارج کشور. اگر ندارید، برید سراغ توصیه‌ی دوم. احتمال بن شدن داره به هر حال و ریسکش پای خودتونه. من خودم به شخصه هنوز بن نشدم(نمیدونم شانسه، یا چون دوستم از خارج از کشور واسم گرفت)
2- اشتراک Codex بگیرید در عوض و یا نهایتا اگر کار خیلی واجب دارید و می‌خواید حتما کلاد باشه، cursor بگیرید اما کرسر خیلی زود تموم میشه طبق تجربه‌ی شخصی. به نظرم Codex سخاوتمندانه‌تره به شدت. و صبر کنید تا وقتی که بن شدناشون شدتش کمتر بشه.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4332" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نشت مخفیانه‌ی دیتا از ریپازیتوری‌های پرایوت گیت‌هاب با یه ترفند ساده‌ی هوش مصنوعی
📚
فکر کنید یه نفر بدون هیچ پسورد و دسترسی‌ای، بتونه کدهای مخفیانه‌تون رو توی گیت‌هاب بخونه. چطوری؟ با گول زدن ایجنت هوش مصنوعیِ خود گیت‌هاب!
تیم Noma Labs یه آسیب‌پذیری خیلی خطرناک (به اسم GitLost) توی سیستم جدید Agentic Workflows گیت‌هاب پیدا کرده. داستان از این قراره که این ایجنت‌ها می‌تونن issueها رو بخونن و اتوماسیون انجام بدن.
🫵
حالا هکرها چیکار می‌تونن بکنن؟
هکر کافیه بیاد تو یکی از ریپازیتوری‌های پابلیک شما یه Issue باز کنه و توش یه سری دستور مخفیانه به زبان انگلیسی (Prompt Injection) قایم کنه.
ایجنت گیت‌هاب این متن رو می‌خونه، گول می‌خوره و به جای کار اصلیش، میره فایل‌ها و دیتای ریپازیتوری‌های پرایوتِ همون سازمان رو می‌خونه و برای هکر می‌فرسته!
نکته‌ی جالب اینجاست:
گیت‌هاب کلی گاردریل امنیتی چیده بود که دقیقاً جلوی همین اتفاق رو بگیره. اما محقق‌ها فهمیدن فقط با اضافه کردن کلمه‌ی "Additionally" (به‌علاوه/همچنین) توی پرامپت هک، مدل هوش مصنوعی کلا گیج می‌شه و به جای اینکه درخواست رو رد کنه، تمام محدودیت‌ها رو دور می‌زنه و دیتا رو لو میده.
این دقیقاً نشون میده که توی سیستم‌های جدید هوش مصنوعی، همون متنی که ایجنت می‌خونه همزمان می‌تونه پاشنه آشیل و نقطه حمله باشه. حملات Prompt Injection الان دقیقاً دارن همون بلایی رو سر AI میارن که قبلاً SQL Injection سر وب‌سایت‌ها میاورد.
البته این باگ به طور مسئولانه به گیت‌هاب گزارش شده، ولی حواستون به ایجنت‌هایی که به سورس‌کدهاتون دسترسی دارن باشه!
منبع:
https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4331" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4330">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی فارسی، ویدئوی 10 کایی کم کمش 200 تا کامنت رو میگیره و خیلی از یوتوبرا هم جواب میدن و اهمیت میدن</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4330" target="_blank">📅 16:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها: https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو: 1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم 2- با همدیگه…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4329" target="_blank">📅 16:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DuN9OmUBpn7Wug5WoZySV1dj9POXEoDmWokCVp8ofIe-Qw-pD170DBb7gPB_9NemSzNHskxOsBIBwnxgFA0intyf4kLAUPomilVsZO5mODan0LOcT9oSUYYxDO7ILRUHThspN6V-4mvhnt8u0P4mjNkbfqsZqMzqO4h_t9P28tQOtQYvWFFW9ajxIIv3wUH4qjHomkjN8tP4U4eBAfY4g4yJ3MGgTDTOrvtuyXHTjm9lFMBcpHhE6qp6VwnRU1yUKN9eiGkwStHcXz2ijItD5cIdW0il0YAR0sECCShbEyAD9nzXR0G27XQcCNp2FzYs1EVjhoMFl1JZykvBHHihfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها:
https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو:
1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم
2- با همدیگه OpenCode رو به 9Router وصل میکنیم و روش دور زدن یه باگ خیلی رو اعصاب رو بهتون میگم
3- از هرمس استفاده میکنیم که با سامانه پیامکی، یه کرون جاب بنویسیم(قابل پیاده‌سازی برای هر ایده‌ای)
4- و کار با پنل‌های پیامکی رو بهتون یاد میدم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4328" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zombie</div>
  <div class="tg-doc-extra">Bad Wolves</div>
</div>
<a href="https://t.me/MatinSenPaii/4327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4327" target="_blank">📅 15:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4326">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خب انگار فعلا خبری نیست
نت منم اوکی شدش</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4326" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4325" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=rKb3InbWINSFTbaMYzcamB8MDOeoHVrl2byb7IneRV7MsIfg-NF4xcHp1Zycw4EoYz40Ypwxp-qtiTBpzqoYcjQi289QZe2upoC8-SZhPebHljm6Uw1fXxW-5gMDNzJaVNuWPw1TU8Aj-43lQ3AELxwpefZI2K2c7R-R_IapFh_q6rPc3aj6_Eej8r5gzJDiF_GVux8rResJ5eUXRgHJeoDCUUpSELm42QUiLX8Y3dl3PikLjUa8kP5JUBj1ES3VJbU7a8mLOlHHGvowLEwUyq7nxqG3cEJ2BuvJvowSKFTKPydT_oprSSRGUxbS983TLAv9S-KLd_Q1jlOFxFapRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=rKb3InbWINSFTbaMYzcamB8MDOeoHVrl2byb7IneRV7MsIfg-NF4xcHp1Zycw4EoYz40Ypwxp-qtiTBpzqoYcjQi289QZe2upoC8-SZhPebHljm6Uw1fXxW-5gMDNzJaVNuWPw1TU8Aj-43lQ3AELxwpefZI2K2c7R-R_IapFh_q6rPc3aj6_Eej8r5gzJDiF_GVux8rResJ5eUXRgHJeoDCUUpSELm42QUiLX8Y3dl3PikLjUa8kP5JUBj1ES3VJbU7a8mLOlHHGvowLEwUyq7nxqG3cEJ2BuvJvowSKFTKPydT_oprSSRGUxbS983TLAv9S-KLd_Q1jlOFxFapRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The Return of
قدرت مذاکره</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4324" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4323" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4322" target="_blank">📅 12:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">روی اینترنتای خود من به شدت اختلال هست
همراه اول که به زور چیزی باز میکنه
ایرانسل 4g+ اما هیچی به هیچی. آپلود 0
فیبر مخابرات هم از صبح 2 دقیقه وصله 20 دقیقه قطعه</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4321" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4320" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4319" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4318" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4312">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4312" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4312" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4311">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4311" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4303">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4303" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4302">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c0SB2Co6DNEjhRKBWApe95UBXZV9-ZFH63cBjANoOOzWpGHFCslLpwrmEjcw2BjLL3BpkMyYbEqX4HFT_6WeTpIpuisX1S6qH6d5PklZqme80zplyXdIZRXGrf_kEF5xHburc-JyLAXfj8BrrQ3wkDkHKpNCtWh5TL1PIlIqwn57JVcIlNwM0CbddUoKKTa8yk4UGr0NOOZnFzr_wk-w0ZT7ooAa9zj6EtsP-Raqh6eDI9BaWRkpRpdDV5dkp7eLiOS5nZFU_a14JzM3TM9-z0b6SmtHGfJDnsswIZUr7EuLB_6ytlUT_ByHEiqy3PDhwA5hrAPLHSn-msw4No2LkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4302" target="_blank">📅 11:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4301">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اعصاب و روان نموند برامون. نمیدونیم درس بخونیم، کار کنیم، کارگری کنیم، لپ تاپو بفروشیم و دلال بشیم که بتونیم زندگی کنیم، چیکار کنیم</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4301" target="_blank">📅 11:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4300">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">میترسم پنج دقیقه بخوابم ببینم نت قطع شده باز</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4300" target="_blank">📅 11:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4297">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l3yjSmzCzGepjLbEYlU3-ZKN2st3MD8E5tI8LdDKiGXO4Tn4zWpETEBH5Ii2dEEf_164hWzQA5uK3mBUOil3gIzNlILx7cBQsSMhafimEv58LlY3wKtHFq7k78nO170lsBFR5dPWmBK5cP4Lcxa0yWPL3WHtAPWxSD2fGv4GE7smQtFDoAwCxf8YPldXC5l4Wxljn5dsRwOR-1HdvqAmNHNqpKF5FVjsJW1zmQPFCqO9iU2XLGZY9MOM8QPFX-LV7xugl67IieSWfCuQKc3T74v-pqinIRFVNldll4pkeU21d-iV5K_pXQHL_8KwL4WDwMyOYMz1P8WitIt4Z2RU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VnLCUGb8T5EnwRjBeyOVfO0eVroqCDd6h9sToER26tAFK3g_wnPsYnmL6icAv7LGwMkDYfDJMXR5iXrZE3R1uWYVls_R4_B8zh59U64CI7UsRrUnpHpOKzuWD2Ozpj48zFcjlZZtrwHZqP9jc-giuiSFA5tVXK1pJw1EQhS7B7rjdVlIeMMk-3ilqHD-9M1gCN61bwYdrL47qtS0hnj3MOJWn_cQdo8rJS9RgffbDVeHTIM78qfrVnpZvhF--ZI2EKmOwIh4OozSXJTEZCPF7x9ykFvHNQlDWIeIelH31E41pWd-oy1DlFsu3Wq8V4M_GmRBf83T1WXh2Fq8KEtSCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uUriDRH9BYcC5s4uyvOHZcnumYEGTB_mz9A57Nni0AohUdbc-_4Ul7RutoUX0S3sngC6xt3STL39Yoa7_4j9Su2jOL5JplZXX2QZp4ZVdHBRkuK1n3oEuBNRV3qL22zL1Sa3PSU3LHKwOECxLskfn0omvoJEcHZQzTdPMrAEztP3zoG86EUCQzslDUpyRjG2e4mKep23Mnw91Twl-vVCT0-eR-uwWOxA2NB_UdRg67IHbTdrvk-EnnRgbKbcX60UFM6LXJX3TCsKWZdFrfDkkhdI42fiGXkwC7wurlM4ZsPNVBD2raj1yooop59M929_6a1pLDXYtDf_5DhWlUj5bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی هزینه‌ی هوش مصنوعی از حقوق مهندس هم بیشتر می‌شه
خلاصه:
شرکت «آنتروپیک» (Anthropic) حدود ۲.۳ برابرِ پولی که بابت حقوق و دستمزد می‌ده، خرج زیرساخت و پردازش (Compute) می‌کنه! یعنی با حساب حقوق سالانه ۲۲۴ هزار دلاری (با احتساب تمام مزایا)، سالی ۵۱۵ هزار دلار به ازای هر مهندس خرج پردازش می‌کنه. در حالی که ۱ درصد از برترین شرکت‌های نرم‌افزاری فقط ۸۹ هزار دلار و شرکت‌های میانه بازار (میانه آماری)، کلاً ۱۳۷ دلار خرج می‌کنن. حالا ۳ تا سناریو برای سال ۲۰۲۹ داریم که نشون می‌ده این شکاف عمیق چطوری ممکنه پر بشه.
همونطور که اشاره شد، آنتروپیک ۲.۳ برابر حقوق پرسنلش، در حال حاضر داره خرج زیرساخت و پردازش می‌کنه. با حدود ۵,۰۰۰ تا کارمند و تقریباً ۱۰ میلیارد دلار هزینه‌ای که توی سال ۲۰۲۶ برای آموزش مدل و استنتاج (Inference) می‌کنه، سهم هر کارمند سالی حدود
۲ میلیون دلار
هزینه پردازشی می‌شه؛ اونم در مقابل حقوق و مزایای کلانی که برای هر نفر احتمالاً بالای ۵۰۰ هزار دلاره!
بقیه بازار نرم‌افزار خیلی از این رقم‌ها عقب‌ترن. ۱ درصد از برترین شرکت‌ها سالی ۸۹ هزار دلار به ازای هر مهندس روی هوش مصنوعی خرج می‌کنن؛ یعنی ۴۰ درصد از یک حقوق ۲۲۴ هزار دلاری برای یک مهندس ارشد. این رقم برای شرکت‌های میانه بازار فقط ۱۳۷ دلاره! اختلاف فاحش اینجاست:
۲.۳ برابر حقوق
در لبه‌ی تکنولوژی
۰.۴ برابر حقوق
در صدر بازار
نزدیک به صفر
برای شرکت‌های معمولی بازار
حالا بقیه‌ی بازار چقدر می‌تونن خودشون رو به این سطح برسونن؟ جواب این سوال توی ۳ تا سناریو خلاصه می‌شه.
(توضیح نمودار خطی(عکس سوم): نمایش سه سناریو برای هزینه‌های هوش مصنوعی به عنوان درصدی از حقوق مهندسان تا سال ۲۰۲۹؛ در سناریوی خوش‌بینانه، این رقم به رکورد ۲۳۰ درصدی آنتروپیک می‌رسه)
سناریوی بدبینانه (کاهش قیمت توکن‌ها برنده می‌شه)، سناریوی پایه (رشد ۱ درصد برتر بازار کند می‌شه)، سناریوی خوش‌بینانه (بقیه بازار تا سال ۲۰۲۹ به نسبتِ هزینه آنتروپیک می‌رسن). هر کدوم از این سناریوها، هزینه سالانه هوش مصنوعی به ازای هر مهندس رو نشون می‌دن(عکس دوم)
توی سناریوی خوش‌بینانه، فقط هزینه هوش مصنوعی به ازای هر مهندس، با کل درآمدی که یه کارمند توی شرکت‌های معمولی SaaS تولید می‌کنه برابری می‌کنه! همین الانش هم شرکت‌های آنتروپیک و اوپن‌ای‌آی به ترتیب ۱۴ میلیون دلار و ۶.۵ میلیون دلار به ازای هر کارمند درآمد دارن، که بالاترین رقم توی لیست ۲۰۰۰ شرکت برتر فوربز (Forbes Global 2000) به حساب میاد.
ساختار هزینه‌ها، دقیقاً جا پای ساختار درآمدها می‌ذاره.
موتورهای محرک توی سناریوی خوش‌بینانه:
قیمت مدل‌های پیشرفته ثابت می‌مونه، چون هزینه‌های آموزش به ثبات می‌رسه و تقاضا از عرضه جلو می‌زنه. فرآیندهای کاری مبتنی بر ایجنت (Agentic Workflows) نسبت به چت‌های معمولی، چند سر و گردن توکن بیشتری مصرف می‌کنن؛ طوری که «گلدمن ساکس» پیش‌بینی می‌کنه مصرف توکن تا سال ۲۰۳۰ حدود ۲۴ برابر بشه. تازه، اگه شرکت رقیب قابلیت‌های جدید رو سریع‌تر عرضه کنه، دیگه پرداخت صورت‌حساب هوش مصنوعی یه انتخاب نیست، بلکه یه اجبار حیاتیه.
ترمزها در سناریوی بدبینانه
: قیمت توکن‌ها توی سه سال گذشته، هر سال ۱۰ برابر کاهش پیدا کرده. مدل‌های متن‌باز (Open-weight) دارن با کسری از هزینه‌ها، شکاف کیفی رو پر می‌کنن. از طرفی شرکت‌هایی که مصرف هوش مصنوعی رو بر اساس نقش یا حجم کاری کارمندان سهمیه‌بندی می‌کنن، می‌تونن شیب این نمودار هزینه رو خم کنن و کاهش بدن.
نظر شخصی: اصلا نمیشه پیش‌بینی کرد:) با اومدن ایجنت‌ها، سناریوی توکن داره مطرح میشه. از اون طرف، چین غوغا کرده و با رایگان عرضه کردن مدل‌هایی مثل MIMO و GLM-5.2، واقعا نمی‌تونم نظر بدم.
منبع مقاله:
https://tomtunguz.com/ai-spend-breakeven-2029/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4297" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4296">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یه مقاله از نیویورک تایمز(با اینکه ازشون خوشم نمیاد) دیدم که توی هکرنیوز بحث‌برانگیز شده. داستان در مورد اینه که با پیشرفت سریع مدل‌های زبانی، مهارت‌های کسایی که فلسفه خوندن، چطور توی بحث‌های اخلاقی هوش مصنوعی و Alignment مدل‌ها داره به شدت کاربردی می‌شه. و انگار یه بازار کار جدید داره برای این رشته شکل می‌گیره =)
لینک مقاله:
https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4296" target="_blank">📅 23:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4295">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4295" target="_blank">📅 21:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4294">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4294" target="_blank">📅 20:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4293">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ft11FrXkG-bTNbWh2DoNny1TDb59FLYwiFm9g7AzD4eEjpoi8w0Bvpl95G6LiRJngzTqxCsN5Xcx9IcVHbXB7KIA95-EpIk-JfEXbZPg3Ts-l5xEam5_9n5oWMAggdpug9AYu2FvkqTBY5LLwTwzyWtKqPVNhL7_xycP8u7-vGY_7464pAB490yg2024JAYlRpfSpTErUDbaj7V-C3VHlzBbccGJzAANWPXc2mFfJg7hDYgb80mw0ZIQO5sSV_A66xEng6cVR3FyuVFANfVV4o9puv0pRUdNtSt6o7DMul6DH8eNswx7TIOiizKZTK2ilGLlXhab-yhZuu7w2Xu29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زبان برنامه‌نویسی Cyrus(کوروش) چیست؟
سایروس یک زبان برنامه‌نویسی متن‌باز و جدید است که برای ساخت نرم‌افزارهای زیرساختی و سیستمی طراحی شده؛ یعنی همون نوع نرم‌افزارهایی که نزدیک به سخت‌افزار کار می‌کنن و به سرعت و کنترل دقیق نیاز دارن (مثل سیستم‌عامل، درایور، یا ابزارهای زیرساختی).
فلسفه اصلی سایروس این است: هیچ اتفاقی پشت پرده و بدون اطلاع برنامه‌نویس نیفتد. یعنی کد باید همیشه روشن و قابل پیش‌بینی باشد و برنامه‌نویس دقیقاً بداند هر خط کد چه کاری انجام می‌دهد، بدون رفتارهای پنهان یا پیچیدگی‌های اضافه.
چند ویژگی مهم سایروس:
بدون گاربیج کالکتور
: بر خلاف خیلی از زبان‌های مدرن (مثل پایتون یا جاوا) که حافظه رو خودکار مدیریت می‌کنن، سایروس این کار رو به خود برنامه‌نویس می‌سپارد. این یعنی کنترل کامل و دقیق‌تر روی مصرف حافظه، که برای نرم‌افزارهای سریع و حساس خیلی مهمه.
کامپایل مستقیم به کد ماشین
: سایروس از فناوری معروف و قدرتمند LLVM استفاده می‌کند تا کد رو قبل از اجرا به‌طور کامل به زبان ماشین تبدیل کند؛ نتیجه‌اش برنامه‌ای سریع و بدون واسطه است.
سازگاری استاندارد با سیستم‌عامل‌ها
: طوری طراحی شده که به‌راحتی با نحوه‌ی کار سیستم‌عامل‌های رایج هماهنگ باشد.
سینتکس ساده و مینیمال
: تلاش شده که نوشتن و خواندن کد تا حد امکان ساده و بدون ابهام باشد.
قابلیت‌های پیشرفته بدون هزینه اضافه
: مثل ژنریک‌ها (نوشتن کد قابل استفاده مجدد برای انواع مختلف داده) و چندریختی (Polymorphism)، بدون این‌که سرعت اجرای برنامه رو کند کنند.
ساخت افزایشی (Incremental Build)
: یعنی موقع تغییر کد، فقط بخش‌های تغییر‌کرده دوباره کامپایل می‌شوند، نه کل پروژه؛ این باعث سریع‌تر شدن فرآیند توسعه می‌شود.
هدف کلی سایروس این است که زبانی باشد نزدیک به سخت‌افزار و ماشین، اما بدون این‌که خوانایی و سادگی کد قربانی شود.
این پروژه هنوز در حال توسعه است و به‌تازگی نسخه بتا (Beta) آن منتشر شده. اگر دوست دارید بیشتر بدانید، امتحانش کنید، یا در توسعه‌اش مشارکت کنید:
مستندات:
https://cyrus-lang.ir/en
گیت‌هاب:
https://github.com/cyrus-lang/Cyrus
کامیونیتی:
@cyrus_lang
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4293" target="_blank">📅 18:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4292">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4292" target="_blank">📅 16:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4291">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دیروز و پریروز می‌خواستم ویدئو بذارم، اما با اینکه موضوعات زیادی دارم برای ویدئو ساختن، حس کردم که کمی عجولانه‌ست و تایم گذاشتم که هم خودم کمی بیشتر با ابزارها کار کنم، هم وقت داشته باشم برای مطالعه‌ی شخصی که محتوای باکیفیت‌تری ارائه بدم. برای همین تا وقتی حس نکنم کافیه، ویدئوی جدیدی منتشر نمی‌کنم
❤️</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4291" target="_blank">📅 16:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4290">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OK-6FfCVNAEDn9Nv9Gs5RAaZVk_zd-i1yrmxxvNqozCsBpzWxDpADZN3NzzGgnPQw324QJDEjZP9Gq3DJ3vYMc3B17ujFw9u-BWQ6fjbsSyu4jUY82cAiIgzKjcZN_N1poTLxlJYG5sxlpmR3EISUDsUgvJTEU0cAk_72Ynv9ktwN1oOwhFNBzTbVh5dqhu5dVhqV35gkzNYo2be_j1Rqp91iKSnfVdCjYBRLbQ9UA-F9_-F7pAgIfXCu2RwEaTNP3Yo9tQIPHJM5apDrjeVZJww6XR4UcGqbEnVqU745O0R1GC188OStHxj-YnEIHDJrfNLNdfghYufNhb7_GoVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا هزاران پست سیو می‌کنیم ولی هیچ‌وقت نمی‌خونیمشون؟
🤔
اسم علمی این رفتار
Digital Hoarding
(ذخیره‌سازی وسواسی دیجیتال) یا "
پارادوکسِ بعدا می‌خونم
" هست.
این اصطلاح رو اولین بار
Van Bennekom و همکارانش توی سال ۲۰۱۵
و داخل یه مقاله توی مجله‌ی
BMJ Case Reports
مطرح کردن؛ اونجا یه مورد بالینی رو توصیف کردن که یه مرد ۴۷ ساله هر روز حدود ۱۰۰۰ عکس روی کامپیوترش ذخیره می‌کرده بدون این‌که هیچ‌وقت سراغشون بره.
از اون موقع، این پدیده به یه حوزه تحقیقاتی جدی تبدیل شده. تحقیقات جدیدتر (مثل مطالعه‌ای که سال ۲۰۲۳ توی مجله
Journal of Obsessive-Compulsive and Related Disorders
منتشر شد) نشون می‌ده Digital Hoarding با الگوهای شناختی و هیجانی شبیه به اختلال وسواسی-جبری (OCD) و وابستگی هیجانی به اشیاء مرتبطه؛ یعنی حذف‌کردن یه فایل یا پست، همون حس ناراحتی رو ایجاد می‌کنه که دور انداختن یه وسیله فیزیکی.
چرا این اتفاق می‌افته؟
👩
هر بار که پست مفیدی رو سیو می‌کنیم، مغز دوپامین آزاد می‌کنه؛ حس «پیشرفت» بدون این‌که واقعاً کاری انجام داده باشیم.
✈
ترکیبی از
FOMO
(ترس از دست دادن اطلاعات) باعث می‌شه به‌جای مصرف محتوا، فقط جمعش کنیم.
💤
نتیجه؟ انبار دیجیتالی از Save‌ها و بوکمارک‌ها که عملاً هیچ‌وقت سراغشون نمی‌ریم.
چندتا راهکار عملی:
قانون 5 دقیقه
: اگه محتوا کمتر از 5 دقیقه وقتتونو می‌گیره، همون لحظه بخونید؛ وگرنه رهاش کنید.
سقف هفتگی
: حداکثر ۵ تا ۱۰ آیتم توی یه هفته سیو کنید تا تلنبار نشن.
دسته‌بندی و پاک‌سازی دوره‌ای
: هر چند وقت یه‌بار Saved items رو مرور و پاک‌سازی کنید.
اگه واقعاً مهمه، به‌جای سیو کردن، همون لحظه یادداشت بردارید یا اجراش کنید.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4290" target="_blank">📅 16:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4289">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4289" target="_blank">📅 15:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4288">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WuZcC_2R2afiFNzsOa8lqIqiSe19FbALnJjWeulbEtxldjwmgbda7XG9herYHwW6AhbL0V3ft-sG7elYS88gz8s5Chl5MfDdpju2lksnCeER95pNVqXxZDMZbTMunl8Zwr_i3yYWJc2jnKPxMOIT9G44w1G3B30mFVQManUqmvVWxWhsMpIaQiVGidvyPykcxMF5muZDxWij3Ei0-5NBsqW50R6OiYQ7zkufyWvjeMsG1B724Jd7UB6-KP0KJgQqc-wcSKk8yHpuNtg3GMrR6AyMdq-e-SteoxhnRjICTs-b_0kdY_6oggWdleb-q4STaRgoMpCrHu5sxR74NOdygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر، خیلی راحت با قابلیت Browser که اینجا: https://youtu.be/_30_ng3Hyfs یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4288" target="_blank">📅 14:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q9Ff3lDvxilG4IDpiKnjuqOS44j7tlVR6CqtJv1g5xHGr51UkPRJbZgUSr6TpfCZYLwmrJhDVNxUeHq_eZSqvKW-wDXn2ByYXlKo3_pbqjVmplijjQ2oOzuvM44_87-6hjWdGUxxwX6OVZm6jTI-IP2PzByTz8A4chQKVHPMVrCtP-BGpL2BZs9SSXCmHO7yhOY9tnPydpdvHC8kBkU4FcGfzVIk2qMOmOHmjbq_t4GQFyh0E1t6eq9uAx-IarAJP8xGA4hDv9W1boq8cFC3CYFKb-41XWWZauNwXtrqv_a_PWMJ1YCfrZyKh2Oxua9Q5QB4DdD93cnkKU5SGfCVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HlOxzRVOFgKAlhT0V3cl2apirHoDjPp-L4GpDT7iRxcRZ4Ui00duhkhLoH29bmVlMTK-zSMk-qkm4nWyIme-LOLAuoNdTB1VpIcvzi-C2R95uGcWYWFW-5dQOsegJzLYVTS1a_QmdMd0z3XXnhATy0tv3zAsnGTIj1x3OY_lq6Wafgx0vRe7FF4s5wC3e2UqmEkEvR3lsTIHjj6yCB39-aEv6yUUPXSV5lgzffpj-Kz-gNNn6sV033BBc4pB5SnMIOxxzly-QU0U1t5K3qXNkplUWBLhF2-Ekh-B2-83MfjyFoacZOgasvvZmB8xH7tLZiEv_BuYl5GFYGEUj1wy1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر،
خیلی راحت با قابلیت Browser که اینجا:
https://youtu.be/_30_ng3Hyfs
یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4286" target="_blank">📅 14:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4285">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cpK_4bN1ahDFnen8R9rE05vISjVWtmpxBs-3uZkqMuwqYHl4gsucb2qJGsxJHT9-F3mP70lZWJyFBHTEJ5GM4AE2r21NGkVBIyHkgvuieEVRR3SUeG145yR7Exn0TvUP3mt05t1gWmzuXkSubm7HUytWWEdOCH4t2BI1gM9uzmmcrcpIDSSYkMPwOHFqZgSL8T9WJViOkKezVpYIKlTJB0iCUGwac2xZ8qSqHduHhR4BnGoQXri0SuMRjBhvoN5sVw-2i7oSkACQt6HYKCRbq-mB4exaUardTNr4SrkgzJNE0mCVEoaPvOR6Ewx8zqr0l402Q9gaXycAnOtf52fdtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با docker کار می‌کنید، احتمالاً درگیر زدن پشت‌سرهمِ دستوراتی مثل
docker ps
و
docker logs --tail 50
هستید تا چندتا کانتینر رو همزمان مدیریت کنید. این کار هم خسته‌کننده‌ست و هم ترمینال رو به هم می‌ریزه.
ابزار
Lazydocker
دقیقاً برای حل همین مشکل ساخته شده؛ یه TUI برای داکر و داکر کامپوز که تمام کارها رو با شورت‌کات‌های کیبورد براتون انجام می‌ده.
-
بدون switch کردن:
همه چیز از مصرف منابع (RAMو CPU) تا لاگ کانتینرها به صورت زنده توی یه داشبورد یکپارچه نشون داده می‌شه.
-
سرعت بالا با کیبورد:
لاگ دیدن، ری‌استارت کردن یا پاک کردن کانتینرها فقط با زدن یک دکمه کیبورد انجام میشه (بدون نیاز به موس).
-
پشتیبانی کامل از Compose:
سرویس‌های داکر کامپوز رو هم به خوبی می‌شناسه و مدیریت می‌کنه.
-
بدون کانفیگ:
با زبان Go نوشته شده و فقط یه فایل اجرایی باینریه؛ نیازی به نصب سرور یا دیپندنسی اضافه نداره.
و خلاصه این ابزار سرعت کارتون رو چند برابر می‌کنه.
گیتهاب Lazydocker  + آموزش نصبش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4285" target="_blank">📅 14:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4284">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید: https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4284" target="_blank">📅 13:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4283">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:  سلام متین خوبی داداش متین به خدا شوخی نمیکنم همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا من تو گوگل سرج…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4283" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4281">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MfYtbmyoKdQZ8CsGJPHys8cE11XLwZG5XGuMhmJXmHIgv53PUp7E2V96DiSZqMho_9gliCqH2yw9WAoLWJa7BvTs5QNQFhJLULiDx_hwqzswbP3vIjldsB7v9onMTCVYOd2rKfKbV-XFR2MIX_KietR8oDjVZ3hmz6JpAgAS6emKpUeUdx9vvL92_hjFz8FSMrvPlFNpKn1IeEvfD6nxK4rzFw7EvD-lq0cJLCDEhfZCHRuWCK7dB1PLQyvVXCOiZc-HjFKn5r9qlsRCHudoqOz1bsA_yiu06u93c_uHWvJD-qzesmTLEybAUIMQr9Jwd8tE1r4g05E4riGmORFRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JR1hvjwBDV_75baDX6D5xlBFKOTarvlwGJHYzwo0HPF5gZfAJHuVR5i2YDYn8JfJJ7TQ6QbrYheMs7PqBD236q--raVg3YKh8Gww4-29Vbq8p4CrDjYK0mD7O9XYtOz5xXgeAJ043t5DRrugSFboirggYuzR5nZ-R3eY0EUdsARVHu17Gf3i-zFUVyFvoYsKMqPcu0fYsrEogec0ijNHVZicHAMTnVBsWvFXy63rCmxuBNumSbSEeLoVHP2Sh6Ma46CUpk_A8YhsJ0YJoPjqCxmBJwetYMB7agRMj-2jmQb9VmDId_tWAkN0F6dniSfPQA6m5FHvjYaiBFONIWWCcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:
سلام متین خوبی داداش
متین به خدا شوخی نمیکنم
همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا
من تو گوگل سرج کردم و هنوز هم شماره مجازی نخریده بودم
https://build.nvidia.com/settings/api-keys
ببین دقیقا ادرس هم برات گزاشتم
تو گوگل سرچ کردم Nvidia Get ApiKey
بعد سایت اومد بالا ازم ایمیل خواست
تازه atomicmail وارد کردم ایمیل گوگل هم ندادم
بعد که وارد کردم منو برد تو یک صفحه ای یک کپچا داشت تایید کردم و رمز عبور خواست اونم اوکی کردم
بعد گفت نام کاربری رو وارد کن اونم وارد کردم
منو مستقیم برد تو صفحه apikey ها و استفاده هم کردم
با تشکر از محمد عزیز. نمیدونم انویدیا وریفای رو برای ایمیل‌های شخصی برداشته یا اینکه کلا برداشته</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4281" target="_blank">📅 11:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4280">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید:
https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4280" target="_blank">📅 11:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4279">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یه پروژه‌ی خیلی عجیب روی گیت‌هاب (با اسم Pon) منتشر شده به تازگی که تونسته پایتون ۳.۱۴ رو مستقیما به کد ماشین کامپایل کنه و دیگه نیازی به Interpreter و مفسر نداره. این برای پرفورمنس پروژه‌های پایتونی می‌تونه یه انقلاب باشه
👍
https://github.com/can1357/pon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4279" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4278">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یکی از دوستان رو اون روز باهاش صحبت کردم، برای یادگیری فرانسوی داشت از Hermes استفاده میکرد در کنار منابع و ... دیگه‌اش. و به شدت راضی بود و می‌گفت حس میکنم بازدهیم چندین برابر شده
جالب بود برای خودم</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4278" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4277">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست. فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4277" target="_blank">📅 00:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4276">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست.
فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4276" target="_blank">📅 00:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4275">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=htMoa-N19ZR7tLJB6ooKcTannvk0z0PE0fXTYmUDQSIaFOZ5zoXgcZvfvNwZGUvQ7uQ-1KCCic89xo-UQamyOZnLALiSYjV1_Rby19e3UUheadv4oUqOOORgeNbsaD-PcXCaOYPuKe6LasvR4AwUZ-hx-4qvplVcsBqiIm4MvkoRL2CxPvjtN1gYft3YCBIjrWUYFi13fCO--U1hXz3b4uhuOqBRbwijyAZ_s1e2t5PQnjB5RPg0-9X__JZvNB9UYfA3ZxoH18MSktm8bU4ZWt8mVAz-ZoGbD7vyKm2qbW8GMEK3bgOpLFVFmiEh8LSJhM7ffveYbjhMiMROu6DTYbDgxnnPlbOtvIilwFjWiLq0po0iJpEppjq2kfq85f-r12fru4j1T9u744GkfNrAFccbDO3PDKmYE4ImJqFeFQI2h_2bZdCVVEzLpiIfAcUDst1WZIxwb2PCOhiBRsb7hy9THMtFM9CHcB0yoA9KUifQkKTDDOhktgWj1iUnMtOWgFkREcV4fQOXW_2VfP2x6NCdRF4xmnkhWPeKzQujJ3-A5qMg0Qd6wq7jmGeJBo4Oek6vtg359vh8qjG64W2tJdsXoYDGf6oJr3ZbUmMRbjHgrdx1MgLXTVAAnblg6CU-PZiPa2OUYgUx754wk8hgfM3NXu_lPN-SC-X6wZEKUCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=htMoa-N19ZR7tLJB6ooKcTannvk0z0PE0fXTYmUDQSIaFOZ5zoXgcZvfvNwZGUvQ7uQ-1KCCic89xo-UQamyOZnLALiSYjV1_Rby19e3UUheadv4oUqOOORgeNbsaD-PcXCaOYPuKe6LasvR4AwUZ-hx-4qvplVcsBqiIm4MvkoRL2CxPvjtN1gYft3YCBIjrWUYFi13fCO--U1hXz3b4uhuOqBRbwijyAZ_s1e2t5PQnjB5RPg0-9X__JZvNB9UYfA3ZxoH18MSktm8bU4ZWt8mVAz-ZoGbD7vyKm2qbW8GMEK3bgOpLFVFmiEh8LSJhM7ffveYbjhMiMROu6DTYbDgxnnPlbOtvIilwFjWiLq0po0iJpEppjq2kfq85f-r12fru4j1T9u744GkfNrAFccbDO3PDKmYE4ImJqFeFQI2h_2bZdCVVEzLpiIfAcUDst1WZIxwb2PCOhiBRsb7hy9THMtFM9CHcB0yoA9KUifQkKTDDOhktgWj1iUnMtOWgFkREcV4fQOXW_2VfP2x6NCdRF4xmnkhWPeKzQujJ3-A5qMg0Qd6wq7jmGeJBo4Oek6vtg359vh8qjG64W2tJdsXoYDGf6oJr3ZbUmMRbjHgrdx1MgLXTVAAnblg6CU-PZiPa2OUYgUx754wk8hgfM3NXu_lPN-SC-X6wZEKUCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش کامل Mahsang VPN | تنظیمات جدید CDN Fronting و اتصال پایدار
اگر می‌خواهید با روش جدید اتصال Mahsang آشنا شوید، این ویدیو را از دست ندهید.
✅
آموزش نصب و راه‌اندازی
✅
تنظیمات کامل CDN Fronting
✅
روش جدید اتصال
✅
بررسی تمام گزینه‌های مهم برنامه
✅
نکات افزایش پایداری اتصال و رفع مشکلات رایج
اگر قبلاً در اتصال یا تنظیمات Mahsang سؤال داشتید، احتمالاً پاسخ آن را در این آموزش پیدا خواهید کرد.
🎥
ویدیو را از کانال TakTarfand ببینید و اگر مفید بود، برای دوستانتان هم ارسال کنید.
لینک مشاهده ویدیو در یوتیوب :
https://youtu.be/35-GhIi-egg
@mobamoz_channel
⚡️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4275" target="_blank">📅 23:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4274">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4274" target="_blank">📅 22:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4273">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">توی همین 5 دقیقه شد دو میلیون</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4273" target="_blank">📅 20:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4272">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IqRboS9tGN393Zm_c9UMkBFkobqONQGh0-qgT3XLFrgB5ZBKDSFd6M45ZTo4rShuO004Bxzlk9tYgDwKTRBMtsYXTisV42YVzNO5-xGbXCy0rQkLDoNYSLqVHXlJe-Mnqp6kMh6jzL7mtLdPc5eNBuUgRwDn9GXsRUiUhjB7r13hl-xtcJWF64RllfottnOf2jDN2uqZpOKZlMx-pvOO_kcWDLwqbrQn5S5v3sKvEPG5kre3pjwLTGe80x6ywkx3ppteE-W4TPX0Fw9mbZqyEj-vIkGiSXSMFZyLwr4Yk4ADJkqPcR7Bf5LCGbShTRhuMioxNz1CZMV0aJFh48-FTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4272" target="_blank">📅 19:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4271">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sgQVxOjpJK-FXNJWN-WPZ4bDTw6-9EwvcRLgNZDfIU5WH2rCAH6LsBY56DgrlGedO3xEHELBb9GLyHNymM6lYT0xFXPxA7VYibti3bnMGlfZa7JFyAjccBdBtBANOS_t_1_peUiG8hZyeJ79H1Kc3p8GA8UF0yWfe1etosF3NzFPGWrlP4e-jypqTy9YdW2hGW7X58zRtltnQQeVP7dVAxIOC0Wg9AKTDAAUTs1y6x_I86NhXuKDQA41OSBAtYOjSH1zbSMBI0miXMYSTk15CxxXhMQQgRTuLXobDz_WIyX3-fMBVG4T6o2WQYyD6pFLz32HuPpxmptGlbQJFToHAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین
درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4271" target="_blank">📅 19:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4270">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6PdkBen9dMj9SQVpr4IXJKOm1BrR-b3zct2p054-ktccfGC4e4mADo1e_cTSunp6Wd4VfYRu3sbCH391kmkZiE8Iyvk1KkhNGOsbtIYSVyEJ5Ij8IIP9CHa4GGiJhRcTxpCadQ7gFO0V1x0ihkzaXjGjRvd7vvxJxG-Hjv_W3GtKT8FHRvC6NNj7EBmmEW9bXlI0l4eIKNBTYlJlKPRaSMiTR5I3zxvSJhYMWivw7dg4fN2LTYzovQGmjjdtQGK4M3_32t1uW23b8uBQldco81K-Hdv19YJK4Umt1fR4bVmC5irSovJRs2j-SVr3kF7rlH_fekAP6aezgEUSUEPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4270" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4269">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AT-jAoSLv8yOrqfPt2nM-HGk9IOvnDDldgJJwBV57IFzel37b1S07RvDRRx8mrULWMFCUVMBBxauJBfA9j4Vx3jCkBMUdhIGyKtGiUWdtslHjqNH9hwWoxTJqQqGs34lNZgD3Ll2R5pSAApXOxl6klj4xgEyt2lwpLMq7fSZnBXGipqj-TaJiPtZXLiUMSE1h2xAhWzd64ZtUPs9zah3FYv4CoFOgr-XIclNhe81lCEpKh5lMltSCV0BCxKOJglEouwWZfICFJ8jDZIbTy2Ge_9ej5FoOf1FKfnoGolWV8KJipVwXZi9g92cxAkEVpmO7uQTVp43w5h2GCOwHHG-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4269" target="_blank">📅 19:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4268">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PbZTSghV1j4ibdw7OVBmSAFVyG-1DXSTyre61woWh-PxgtNRcQsWGukivyz52SPjivKApVkEVh9IA2TymJKs4lEXPIW7cGhHMhD6mSdrNORSO_jf9EFSokMszp-D7h7tAJK2Q8vlvQPw7zaY6TX4SVNWbDLNWB-z0j8rtFPFF4QuQ9X_UtTpuXVjJnumxextKj2WDRUJE_v-nPr3vLw-NOxHmX-ffGopPberxF7PFFsx_pG7yZzc6D3PYDFm6Ebl8vIOU3ZhN1J1mLQA6ROO_a7z_3amhLi2mWJQEzU0Pcu-fu429aLgZcN3gtx993wrj9Wl-BHyfyHgiwtXAPQtPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی احتمالا به Hermes اضافه بشه برای کارای روزمره
😁</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4268" target="_blank">📅 16:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4267">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4267" target="_blank">📅 07:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4266">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=XmOaKDZO8fFCblmsGvEs1w3vtsXX6MBOmjOMKzcDVKToSLAhU-Nd6JbRLRVHFys8B20fYNBy34YZmqu7krdK3aPUzr959cpO-z4zg92XdWkViMikzNMhJVHTwtUOZDqVsgnhp_XX8gA9W74rAu68GSqB3OQ3-anJ5Ie9CiOW5nU_lmeOPc1QpgyLmVwxZZyxrd6ZBW2wshU2m5ywbL4Qqhh7keGlkWbNGGbeQ-p_bgMWXVc9Ey2trGs-_u6Pqamv1TkCd9cV_czZW9rPCiuoX5cF90zb6l0mEOiJFbnnwSXIhrgwNK9aX4d0DE7Jy_qD_MK9q6j84uy95tFf3Nxdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=XmOaKDZO8fFCblmsGvEs1w3vtsXX6MBOmjOMKzcDVKToSLAhU-Nd6JbRLRVHFys8B20fYNBy34YZmqu7krdK3aPUzr959cpO-z4zg92XdWkViMikzNMhJVHTwtUOZDqVsgnhp_XX8gA9W74rAu68GSqB3OQ3-anJ5Ie9CiOW5nU_lmeOPc1QpgyLmVwxZZyxrd6ZBW2wshU2m5ywbL4Qqhh7keGlkWbNGGbeQ-p_bgMWXVc9Ey2trGs-_u6Pqamv1TkCd9cV_czZW9rPCiuoX5cF90zb6l0mEOiJFbnnwSXIhrgwNK9aX4d0DE7Jy_qD_MK9q6j84uy95tFf3Nxdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4266" target="_blank">📅 01:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4265">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رفقا
freemodel.dev
گویا api رایگان از claude opus و اینها میده، منتها به هیچ وجه سایت امنی به نظر نمیرسه. استفاده کنید اما نه برای پروژه‌های حساس و چیزی رو در اختیارش نذارید. روی هرمس شخصی و لوکالتون هم ترجیحا نزنید.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4265" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4264">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">متین واقعا باهوشه اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس. بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست. و همشو هم باید تا جلسه بعد تحویل…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4264" target="_blank">📅 00:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4263">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">متین واقعا باهوشه
اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس.
بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست.
و همشو هم باید تا جلسه بعد تحویل بدم</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4263" target="_blank">📅 00:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4262">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Matin SenPai
pinned «
خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4262" target="_blank">📅 23:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4261">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4261" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4259">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jsjDrTuEvmcHBA7vr57W6q0FGObk6cq6c4YLg9qY92PjKrh11qBvE5-IKrTt-NA3xYdFhGIDhhl87xpqg4yX1wGOzlP3MA3YRDHdeY0LxycRRRepvVlTnRVBgvh1dr2f8yFIWSwfVWyggVUTWBGS_rMwHK_BtyEUmpMvyJeOYZ1j5_m5eYP0SDeqY9JWej9GH9VKdC4SMvcClyoFvInxHhm_LaXspl4WcRICRiEzSscxmqAjHfiAs5uNNY9ix01ZG1ARIjDCe5KTZEbxCnfh4vOoxzFHSLapm8QLTcN2ntRVV0e5yjqev6BeucZjoSUx9RGY_FWDyxBuHhfau2XoYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fZ4btPi9SPK_Dmgu9AjdzAsYjmnAaAYAJS_h2nlZA3AsEx2xsx3H1_GJGFDBJ1DLrkjM8RfRFWK3cTwd7gV9G3CcnadyzxuF9TYgaAbttw46sxhQTNrKa2yuyRZZ7ftG6I3C3a7bkWXIGyoht1wzAb3l91m4w2DYWIk0LC4pHkuBLxnEg9WhSUAAyalTmxY_jxUbCYcNMJun983FZqIutHh2BkTn53XZ7ClEWrk7hj78xEk9wGQxRA2yWm8Qd5kbQfrSU3O4w_vuT1KsLT-e-S9V9Xrdfik1I0VLmgfqofsrEaJ_0D4Ernv60GYvCdV13X8TJhaBRPsqMaN6xresBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4259" target="_blank">📅 22:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4258">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4258" target="_blank">📅 22:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4257">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4257" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4256">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟
اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر شدن شرایطم، راجب خود برنامه‌نویسی هم ویدئو داریم) ولی در حدی نمی‌بینم خودمو که بخوام توصیه بکنم جدا؛ دوما در حال حاضر، فعلا خودمو نمی‌تونم هنوز متخصص هیچ حوزه‌ای بدونم. که اصلا بخوام راهنمایی‌ای بکنم توی هر حوزه‌ای. خیلی افراد بهتری از من هستن که بخواید سؤال کنید. اما یه سری نکات رو می‌تونم بهتون بگم که خودم با تجربه بهشون رسیدم و شاید مسیرتون رو کمی کوتاه‌تر کنه:
۱- دنبال پرسیدن مسیر از من و دیگری و این و اون نباشید. اگر توی این چرخه‌ی باطل بیفتید و هی دنبال ویدئوهای مصاحبه‌های آدمای معروف راجب زندگیشون برید مثلا زاکربرگ و بیل‌گیتس و... یا حتی پادکستایی مثل طبقه ۱۶ آقای علوی، هیچوقت نمی‌تونید اون چیزی که دنبالش هستید رو پیدا کنید.
صرفا برای اینکه گوش‌ـتون به یه سری اصطلاحات این حوزه عادت کنه این چنین پادکست‌ها و مصاحبه‌ها رو ببینید.
۲- شما الان AI رو دارید رفقا. می‌تونید به راحتی بپرسید، Roadmap درست کنید برای خودتون، شروع کنید به یادگیری، بعدش هم توی توییتر بیاید و وارد کامیونیتی برنامه‌نویسا/یا هر حوزه‌ای بشید، تایم‌لاینتون رو درست کنید و مشارکت کنید توی بحث‌ها، اشتباه کنید، یاد بگیرید، و...
۳- همیشه حواستون باشه که علاقه‌تون کجا ظاهریه و کجا واقعی. خیلیا هستن که دوست دارن «از اینترنت» یا «با کامپیوتر» یا «با گوشی» پول در بیارن، اما اکثر مردم وقتی واردش میشن تازه میفهمن نیم ساعت هم اعصابشون نمیکشه پشت لپ تاپ بشینن. عجولانه تصمیم نگیرید و راجب مسیری که می‌خواید برید، خوب تحقیق کنید
۴- توی یوتوب خیلیا آموزش‌های خوبی دادن؛ با ترکیبش با ai و مشورت باهاش و کاری که می‌خواید بکنید و هدفتون، می‌تونید به یه جمع‌بندی نهایی برسید و اون موقع هست که تازه می‌تونید نظر یه متخصص(مثلا بکند یا ai engineering یا حتی یوتوبر یا دیزاینر یا فرانت اند) رو بپرسید و اون هم برای صیقل دادن Roadmapـتون هست صرفا، نه اینکه بخواد صفر تا صد آموزشی رو بهتون بده. من هم خودم از خیلی از دوستان توییتر راجب بکند پرسیدم وقتی برنامه‌ام کامل شده بود، بعدش رفتم راه خودم رو ادامه دادم. وسط مسیر هم چند بار چرخید پلنم با پروژه‌های مختلف</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4256" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4254">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nH7oQXOKuv1XJUey16j4_87nV7wiKlj7OHjU_4-U7Njr9E0osS32ATYj1H6mOaeEzgudShvSs5hE02Gpuc7KMG_d7uCvC-YJFSitPKsjpxj3olD7Jj7Hfh4Owmkzxvc1FM7fBzKPVzgaAuFZZAhguYj2nrStY4y45hKOutmLPu74tNx0NiNutAVzu4TB-MwbIObEPIALM8rb1BMX9nxpnxOy_9SODt5CCEACIc0Vrih5HJRSg39Ap19Dzd9aI08rf1WMjrUDaWxkClw6lfUsXckfYxXbDV5AnPJKiiZ2DBui2i-vHwP1o3_kuYOjlcG85VfrXu322Eb9rjPiyA0FFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uixsDnPVG26ajLkWtVw2yy5XfvSn12r0eROICCI4WZFdgk1mEkSQxNu1vH7i-apAUWzYgOaCq2_9jFPf7Krcck-BDj_kP5MJrlkE3_DA3dn9ckMIhNcD9uyv1YeQxgIJ_k44LuWJ7TjMIyFzXaufK8UpwVnSHouC4kEdj--ciZ08HP7DUPjhNncg3qgbi35E7avtfg2hlbRzj-aWiVH1xLuqaZZ8Q-1GaEu595sijmRNmpferu0JuQLcuKHRjTjN5tNTze33loTfc5_MVsPwfrYWh4iJ5lCW52V8VMfTOwiSBFZ5vsAmrHDTE8z7Dn5wxu5fHzN4FEuRB4ipApyo0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت
فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4254" target="_blank">📅 21:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4250">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4250" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4250" target="_blank">📅 21:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4249">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بهم یاد داد از این وبسایت‌ها برای جزوه‌ها و تحقیقاتم درست کنم</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4249" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4243">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UVoJIbHh2bSERofeFORJ9djDDoYM0LBM7CK9omFMrNeErbMcDhz93eXoFChVwA-zmm2xHayhuhIDADWSJnQuDyadUV2CKmD5sACgkUqPAy53BPa6LkLZ1m-Z9D2H1Krw8g9y_zDneHRuzilGGWsnmS9_NzLMZgFp5TOEAWFPLLqXzOf3i_NJLKfeeTuGh6Bz3zRsVBMjyYfwA8kNWlrSOjXu3U-J4gPWbxr91O-3T9YjOrweDEkD-PvIHOxROblivzYNf898Tb5o-vAtMC8hMoGRa2mO_VXDljk5bWlA9A-_q6g-JDiWlXLQl6b9X6qgQCaZseS8EVM1PK84KtiO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hplLHbS2UHnOAZCuU163QweA4xdbermB4Bv1ZsBC_uoqB-sveAu0qnjgA6uA9658GdcDZXWZsF83AdlIoz16XPXbLveiDME9D0Kxx1khWSe79e7KEkwQdus38fTUeEctww55QUC6_HdD1aSBvRFAEa60r7nrRYIieLOIouEMufx8ABnp7Z_4ZAz5ag9kT2PTjDe__qm75HTvp3ITTwsBVgzkL8x1JQF0BQjmMi6TzyXDv-WOvkxuqgGANEVSv0oApS-PFc21E7HcafhID8pPg9rztGy8thRdoBWJURFPQU58kw8f5AAxOb14k4xEzTfQnP6py_ZLGbpg3Hl3ZtSe3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ogpzbLBKt90DiVCM98Ecr4gTC0DlUzXi5xoZYABaZKRhRCiR5cPFyeEBFKrXeUZvqugbq9f0EAvruta4jKafdZWJQLzrt9JQtLfkKagRL7ctH38zMnXi-6Zl8WnwX29ufjmrIfvZgCfl7JrdXkRK7ATtzuuFspR5CUXV8kZBF79ey6SYUr-g-PeWYBWlQ9YVnFQIcx4zwEx8eLv1ZVdZz9Xw-JYwYxJaBci_U4-8iSF_k3tu2-jJHqCbb-2rxJoFhDB8WFxgM1xxilglerw_hCdWH-KmBmiMtpfPne-MX6r1JEzjIlF0fA26Zobj0VVzKTIVQhbW6QLVW6mtyts9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P4CKwWdVBZd5d5IC1P-8iRmkGlU6KM3V57i3Isr5PlPCVwDdz10wJljJWw0f_zfa9c9JwSIqrKJtJN31fFwsVPdwQNHLLImcgTA069tWs9PAh61lm3-0mpkNahqStpUC2wDIUuTHhzML1E5c2sZJnNwIuC8ub_mpVqLDDmatDxcRwYVgl2sY2JRfWch5KUPFNwcaQxOnAVPz7G5dcl9CxQwPZ2OKmkAKQy9I_NreOL6lws160e-5SZ_GksSfnKUpSgKIf12ya53n2jPTo7YuNx2WxaVPv0jOOUPl6-sRvBniMYKeAII6f82caUEH_j5ydELNwQjd3Mpj1DqunwyL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZYXIvrBtCCvR_ZWMtzx3W0IquOEnrh46bhlkr5LYQvhYk1MXQjg89WjD1Bzsbfm1QHDTLOzSKbhfkWyFWHK4Yg3Y_0zYqrRgGm5Gp7Req80muuGE5hlwBZY438E0erUjW9s3LNaKlmlYdDaC1cjHgnkFEDCOuw9CaFP6aby2RBYh8NdtmGPVLrREVqCaXLSK4yzMXUGozXEyCrqaGxXCpfLA1vokauzqeZ6VQ2C4B6CqZ0HcrAeb4BEgR14X481Xv9EV-R8ic0tX5S5o5H32PRm2NFep9ddNeLcUOlsvjDHqBFtbI6v9MZmWJz6xZLBXisjCbbdp1ME5o0LAiErImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VSbcsylVvEyf-caBN-1Fw1svZ0nQHeSEuMpS2S_sw1AEB0HJWGzV8pueq3yK0iRI3wrYORTtW3OvNjRHyqHCUaDy0Yd2osld4ogCylBUSLPvjQwcJHCtHEJT9XwQ7p6_qdfzhPBYcCg3fGiwC25Y0OPaDBd1mdYa9kko1RDwblisua1bvpPuuz-1cCgydBkBLljVtNzOylfT8kJXNn-eD-fxiP5oHTXjV1plGY5vR8rXRvnZpb2dbfNIlRSiK1cOhh0mI0V6N1-C__p8_Ry36gNwrKy1q9B6jZQ1hbb1grhJL4h13rwPDgl6wVGTAmhWcuiLRzl02loUboy-d65Xrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم مهسا توی آپدیت جدید، یه صفای حسابی به UI دادن
😁
اما UI کوچیکترین بخش اپ هست که عالی شده.
۱- هسته‌ی سایفون برای ایران بهینه شده و به راحتی تمام، وصل میشه(الان با همون پیام میدم)
۲- اسکنر قدرتمند اضافه شده برای اسکن آیپی cdn_fronting
۳- الان میتونید از سایفون+آیپی تمیزتون، کانفیگ بسازید. مثلا من اینو ساختم با لوکیشن آمریکا:
psiphon://?region=US&protocol=cdn_fronting&aggressive=ON&cdn_type=any&cdn_ips=
104.16.73.68
%2C104.18.180.6&cdn_sni=
pypi.org
&no_sni=false&skip_cert=true&proto_tls=true&proto_http=true&proto_quic=true&builtin=true#psiphon+2026-07-05+20%3A26%3A39
۴- یه منو کامل برای Chain کردن دوتا کانفیگ V2ray(مثلا یه کانفیگ آمریکا دارید که کار نمیکنه، یه کلودفلر دارید که کار میکنه. با کلودفلره وصل میشید به آمریکا و آمریکا VPN نهاییتون میشه)</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4243" target="_blank">📅 20:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4242">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کتاب کامپایلرها و طراحی زبان - Introduction to Compilers and Language Design
اگر دوست دارید بدونید زیر پوست زبان‌های برنامه‌نویسی چی می‌گذره و کامپایلرها چطوری کار می‌کنن، این کتاب آنلاین یه منبع رایگان و عالی برای شروع طراحی زبان و درک کامپایلرهاست. خوندنش برای عمیق‌تر شدن تو مفاهیم پایه‌ای سیستم‌ها خیلی بهتون کمک می‌کنه:
https://dthain.github.io/books/compiler/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4242" target="_blank">📅 20:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4241">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تعداد پنل‌های وی پی ان بر پایه‌ی کلودفلر کم کم از تعداد کاربرا بیشتر میشه
همشونم شبیه هستن تقریبا. زیاد فرقی ندارن با همدیگه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4241" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4240">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بالاخره کار مقدمات و آموزشا تمومه
کم کم توی ویدئوها میریم سمت ساختن پروژه‌های واقعی</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4240" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4239">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pXzaArE2bIImZNMJha2DXxuGa0Tn3aKo-vNXRydl_ywozTeaU1pUY5jnt5F8V2qzavCWURrs-SSqpeUtceZnNpSc7vR5Sar8Csc4J9A7vDfIHQFH4leLqbhNv9LStgL1hSvnoKHjSr5VTEFvCr_uEADhc7GcKETWEi33dlbwXUWWfr2Sm5Z1uWXERS7E78L7GJnH-iVTSyQcqBCzwlzvPyl02irkP1TVqgo9EU7RNrkFvBwBYYUrjHeNamr7kiXtlnHQWLXt6hBK4EfutoOkVIbEz2KVseLv_6T_-TKce9wQf5ZnmA-g_8fNIHxQ7G1uWqF7ZEhmFoIBRBCzAg031A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز Hacker News رو چک کردم، یه سورس تو گیت‌هاب ترند شده که پرامپت‌ها و ساختار دقیقی که برای Design System با مدل Claude استفاده می‌شه رو افشا کرده. برای کسایی که می‌خوان از AI برای ساخت سریع UI کامپوننت‌های یکپارچه و سیستم‌دیزاین استفاده کنن، این ریپازیتوری عالیه. با دستور /learn بدیدش به هرمس و تمام.
گیتهاب پروژه:
https://github.com/Trystan-SA/claude-design-system-prompt
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4239" target="_blank">📅 17:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4237">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qk9r5VxO8RLNeoQyoVlEM9A9XCFbV90dDLO5LJ0zVDjFTDszwWfc25qJ_S-lt3cEDL_m4BbpYfoVzJkJD8P7w4AqAhReu5F3Ub0iixjgfg7xZn83Mpz7-M70H5TvziNd40rJgSu3ZmESia6eNvziTPT9WQSVGLgfFdy5_r5mb3AlPgox0mO8vaPikpRVLDEs2AsWecL8Wr8dpx5KRw97qoN8aSnj20yTar0Eyk-LV3ejbqNuB1G83F0JcKsGUee99tbGjFXI_LpBbmMcrA9Os5ZaUPgMd4WFop2gC9vmJs5rA2YJR6EN8wahhN1smgmhkK1WuRqbAQKc2qItyBUBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bEMoNGxb9IUGRfo0sfEvwdRz4_Rff5AW4iRZnLndHbwt1jZLSi8YOfci_iSXiZzBlL7hqFX0h3crQyR54YGCJlmeNnydoSPfHzfriY4eaQWq68auKmZIQwr2d4WX4oKHRQbYKxG6tTwqLq4yJgM9kFwiSt9X4fscOKhLKoAE5Z49AXQYxoJdDWcylCFXOt20uFqmvcAUCc4J40UJmShAh29lhu369JFq_M3cHQZ8IQl7pihRBL9Y8tr_w4s9JHBAYaf56AABT5ApcdP3zhwESwyvJNeXbV7GekngtY6rxAO9STvX_vbnVCLJU3N3Rcv91PZJR3SRO03GUXZ2T73bYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سری از دوستان کامنت گذاشته بودنکه این api nara که پولیه و کردیت می‌خواد و فلان.
سایت Nara چندین تا مدل mimo داره
که همین الان یه اکانت جدید ساختم و مجدد تونستم با api key اش به mimo 2.5 وصل بشم
شما صد درصد از چیزی غیر از mimo 2.5 (mimo hermes , ...) استفاده کردید</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4237" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4236">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-Commands-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات استفاده شده توی ویدئو، با توضیحات کامل
سایت ConEmu برای ترمینال:
https://github.com/ConEmu/ConEmu
سایت Nara برای API رایگان:
https://router.bynara.id</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4236" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4235">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kzXkoDAon-agc_zZ8cM-vguD-exQEvrh8ayRAoNmMijaHYSR7PAFTof2nmMEcFvFHxlNTQI1dfI8YJmniKbnLEHHLD8LiloNghc_w6hWpoYXw5Hf19s5-jS8sl5kSCwUvmVhXcoZNgyYcJlUKLBKWT0aMwz7DKSxt3AMY3WF0fhCMau_EsxROObF4BOPJVxQd4pz7OgbgDfpYfH_tIjVtNeH8nYfMkd--mdvJpKjhpXSNuLYnqbXKGmItdJFNyPKnWkiLJFxezQJP1xjJWSkmlHlIwdYFM3IpsSZE-jYEGJGS5R9dN1uhjJMCFDOwtZxtl2LCiw3eQb_Ua5yLrWP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
مثل یه حرفه‌ای از Hermes استفاده کن! 47 دستور مخفی هرمس که باید یاد بگیری
⚡️
فایل خلاصه‌ی دستورات:
https://t.me/MatinSenPaii/4236
⭐️
چندتا از چیزهای باحالی که تو این ویدئو می‌بینید:
دستور
/learn
: با این دستور به هرمس یه داکیومنت یا سایت رو میدی، می‌خوندش و کامل یادش می‌گیره! دفعه بعد که سوال بپرسی از همون دیتایی که یاد گرفته بهت جواب میده. همینطور ازش یه Skill شخصی هم می‌سازه!
دستور
/goal
: یه هدف بلندمدت براش تعریف می‌کنی و اون توی کل پروسه‌ی توسعه یادش می‌مونه که باید به اون هدف پایبند باشه.
دستور
/snapshot
و
/rollback
: دقیقاً مثل سیو/لود کردن تو بازی‌ها. یه جای کار رو سیو می‌کنی، اگه هوش مصنوعی گند زد، با یه دکمه برمی‌گردی به قبل!
دستور
/yolo
: خاموش کردن ترمزهای امنیتی هرمس!
دستور
/suggestions
: اگه گیر کردی و نمی‌دونی قدم بعدی برای پروژه‌ات(یا زندگیت
😂
) چیه، اینو می‌زنی و خودش کارهای هوشمندانه‌ای که میشه انجام داد رو بهت پیشنهاد می‌ده
دستور
/moa
: ترکیب قدرت چندتا هوش مصنوعی با هم (Mixture of Agents) برای حل باگ‌های غیرممکن. با چندتا مدل موازی و یه مدل تهاجمی
دستور
/browser
و
/bg
: دور زدن محدودیت سرچ تمامی مرورگرها برای ایجنت با CDP (Chrome DevTools Protocol). این یکی فوق‌العادست
دستور
/pet
: این رو دیگه باید خودتون ببینید...
😂
بتمن رو تبدیل به ترمینال پت می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4235" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4234">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند. اما اگر ظرفیت پذیرش در ما وجود نداشته باشد،…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4234" target="_blank">📅 02:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4233">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند.
اما اگر ظرفیت پذیرش در ما وجود نداشته باشد، توانایی درک حقیقت را نیز از دست می‌دهیم؛ به‌ویژه زمانی که حقیقت برخلاف باورهای ما باشد.
در نتیجه، از جایی که گاردهای شخصی و تعصبات وارد میدان می‌شوند، گفت‌وگوی علمی عملاً پایان می‌یابد. علم زمانی رشد می‌کند که ذهن، پیش از هر چیز، آماده شنیدن، اندیشیدن و پذیرش شواهد باشد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4233" target="_blank">📅 00:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4232">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=OVRCHWKYry3rscRxe9av0-54yC6fh72A_A93M4xEfzU8iZApUQL_uvFQkzWVa3dO7L1jHLbJC1c0rllyhPZMDDxGousoHS2L2ZA-0f8fBDuOVJf57hbJ7V8X5uB2L_Tn_RI-44QdSNFNASOUVhj1BsSEUUoPOcHTVYbMJ5pdTJdmAvI2rvAy9aHsCZYmVDDdr_zHVZAWUiQOpS9j6-ctFLYCwfywatoVjw039SCf8lUwF07g_H5Cq8Mo__wn81gceKHBvtTst6VEElMNjWFohaLF2skee66XtfNICWgO2rHXueUHt0yKljeNOtLC2qHNb5CoSX3bOLmiJVWvUqNg0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=OVRCHWKYry3rscRxe9av0-54yC6fh72A_A93M4xEfzU8iZApUQL_uvFQkzWVa3dO7L1jHLbJC1c0rllyhPZMDDxGousoHS2L2ZA-0f8fBDuOVJf57hbJ7V8X5uB2L_Tn_RI-44QdSNFNASOUVhj1BsSEUUoPOcHTVYbMJ5pdTJdmAvI2rvAy9aHsCZYmVDDdr_zHVZAWUiQOpS9j6-ctFLYCwfywatoVjw039SCf8lUwF07g_H5Cq8Mo__wn81gceKHBvtTst6VEElMNjWFohaLF2skee66XtfNICWgO2rHXueUHt0yKljeNOtLC2qHNb5CoSX3bOLmiJVWvUqNg0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون عجیب باشه ولی من خوشم میاد وسط ویدئو به ارور بخورم و بهتون نشون بدم که ارور ترس نداره و میشه خیلی راحت، راه جایگزین پیدا کرد
👍</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4232" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4231">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/raP1YMK7Y6bK0cXco6-60pz20x9ryjATvFZ9YpeqtGImbzBkyDiYRSwX5Bt6QH1DM2H5_4GKrXRpfxL2n7GWKQqTRNKqdf5XfIQlztftLaq4_19ub_ZlREHh87AyMD8D5W1BO1oEUM0pjd0G6qRACuJyP3cdBulyke1CSmw5DkVpT3esFVuCEiC12KG-ROPMM4cciKYOvNXJZB00tV8WSCgrrRBPLwW3UX6Vr73Kz9FogTo-AQoez_8mlrAggNmdUDKLJjPVla0_oxH6Bx2R4C89PVglluiRXp9AWU37_dZZd3cIenEwFxFdvaWixvlq2O1kkxekC2aF1MlMB3b4JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.  با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4231" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4230">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/auzZ__JBz_aTlWGsiu6v8HJWKf_ftpxG1S0AdDUvTFW3FGiCvt9MrE1EXShQdokINBPba8473k7a9m0nhUwBN4keC3MVyj8ZJIn8y5RtmunxcspgyscEI3yTZ7Brv20ErFBWU5pdiThsGC89hdDodsDsPO7yGBKsFd1Pc5k9OG_sQhVpiQ58X6w5DylptGP4v6qDwM942mMH7KYn5f7GR7O5Wzx-HV6kpyy01TPxocuHNvOKWIZ8ldCQ6AwhR39l8PKfdEo9OnJI-Bio99v1dmbkeTrhaQRMjiQimsqe1CFy1q2WBJLNG-ALoWINGFsuww2omnLyp-X152oxoaUZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.
با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4230" target="_blank">📅 22:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4229">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">روش فارسی نوشتن درست و حسابی بدون به هم ریختگی هم توی ترمینال یاد میدم توی ویدئو. که یکی از دوستان عزیز توییتری دیشب بهم یاد دادن</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4229" target="_blank">📅 21:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4228">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">توی این ویدئو که دارم ادیتش میکنم، کلا با cli پیش رفتیم و از اپ دسکتاپ استفاده نکردم برای هرمس. علتش هم اینه که پروایدر شخصی اضافه کردن روش هنوز داستان داره و محیطش پر از باگه همچنان. با اینکه آپدیت هم کردم الان هنوز همونه</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4228" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4227">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy  فیلترشکن قوی و پرسرعت برای تلگرام    https://www.youtube.com/watch?v=pyvB6VSPhwg   @WhiteDNS</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4227" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4226">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4226" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4220">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v6vMW5mV0w_wFFpoSOnDWmmMx5yJVpiBGj8L1qIc1vvtiGtYGl9pb5dxqPSJhf0w-Ns-raOj5wAsdKMtSTuDakYGkh6n5f6YQRtT613HKzUWC5O2iCVTx6b6nRUlbuZFHpmZF-wmeAzCdArm_vWTnAoqWLvlgJRNqk4gVlahsARg58Xafo0CtOjR14bXmlvHceaJs3LMoSsuc1hIkKP8MH91cq593psb9DAYT2E-P5Oy3BzsKUeF_Pjvu9NwjJ9i10wWf_Br2SZpiiafwAVNf1xKgo7RzRIaiLRhuHUiRx3FAl4sb4Ntd4MdeYYp3p8ELx5hPpWw452XHyquT6O-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AJo7p4mAFmqT1c60fIABkq1QgcZIqQ0R-ikq0adedpPwEoPWQJ25fRQdX-wdRHOoflTLJmAxaaAaN_s-3KPRufbyd-QTTuYfJcbTqU-E5x0YuLasncimLWzCFkbjESZmVMZarXScHI6eeYTH-P_QXIMsd6Y4GQ0V8whkpruQQisYngGPHpbcPM1c3sz4fHS_mPnSChtxTsbUyXK_5Dq9PfFeM_BjZs9G0Cvsp-nIoVXtmLPJnZI7JCo10kGmrD3GdPljtSeFYbpNOMjl79emOYqtefNr7WEeN8oUslD4OjQhhVcA6Z6nQ5dSrODBS61Qj787e_2iRzbie6M7-GjhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ORFUiGRiKbUqTpQMp2OOuCcMpNC24Hy6j0RegTuZ46TQ5oT-63bZMbHz1XH61s_fWrjbvWOjF2fnAyvzOuMrGVXQUIMFiiGWvTpIF71DMOZ0L8hB5f4b6U78fStPob1plien_jGa60srqNWGdKGgH4NMEwKr2zG79YCmPrcAULNCPN3nE9ki8dVJAlOae8X7nx5OA016nQm_2DYPmGc-pak3jmIZf8PCQbMPaYX80zgSaDMu4F8VN9GIPaqLy_UQPmNSIzEokmUjcBqWYGWFhxu-QmpKk_ul8tCEQtA2fJRoieKJNapRDuAt6yZnyP-owJGYdHwLp3zvbIwN3oZyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ltrgfmx7bhCORX9HVATekLhkCNH0CbDSJ9Ilu_HgE_9bx14pVTBY-mBk4gy6Wmt_5619YwWI-3uen-NbPI2Ape7IoGSlB5gO99-kKm55ZVticFi0VHkEAueAQQYxGmeQp3FVnfxom_LqxZUkAEOpYO0Qch_Y9_BRkrwJt6zdXDFV7q0hm1MeubHonh_0RpVcDS3LOuVMIlzUvNNmPjiQ2KW3jPOtcgkCancoD4zbBuwCaRocV4CRG9nEYpGfhD5bQTSjdmYKwSMVa_1HjumaxAs-p0q3ha-yJHft3H5H-msiX0U2hmz-aM9vi2YS4MBsrixvW7OkgS8A3f-muqi31w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HuxImDJ3rce6DPV1fqcZwYWkD9vze6zCQXrmAHYLvvvX7Mr-mrESAEbhcvPUaz_lMqXn9OW91GszmeM2zOc8ikznIcqh6lQ-tEKe6UaBP7xBvf5oTUncrDcqXkmyYIX5L4gQ2xdNVytIkRAkkIPXUUoK9Q1cnwyh7LDL2WrakZeGaJa4Tp86n0xLwPojN2pFYmtCQbcoILeh77GBx5dNHwz3bb4c4wj6m-jumrN6YplV08G4bo2PUSrn3mmMDOuGkithf3VqKCGIdU7K9-fZ6dYdhWxXeby0O1WRWjb4w5JTujzmF-eAGqBS4bFFlSwNr46q48GjZI51-_a4C8xjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pkEBWVImk32R9kD-Fmz0eRhB0HZbqB3VEAcba-R8rlDm8w10BKaPW1rgxr8p7qt16TcyPKi4b-X6pQIzJjavmczJMH_2474VaUI9_Bqm0ty-5jzl0yjatizY01Y-uwOatd62payQQ19o-2l9s_O-bFhb68JkkNsYsDxMG5M2h4inb8_Cyjp7KA7OXG_g0s6Qx5kAqN9nDptqHYBT9v0x4S1Qui0YdDHlfL54JV_fRvGxXw1m_EkMwtOERXLg5QPXTQFTtxYEGEMLQIJ1Lxoj83SyyRKG2Cmi6K9tP69_U6OwL1JJfI2Za46KJSUa7kmcHXZ0_wROLJ3eD6y-WeEflA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:  1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم،…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4220" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4219">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ue239MVoW1HgS1u5gQUUxsdSyaUmtHdqYMRx5gsucFIWvJiwUcXDRN4kpPdIoReZBMj4RxgxR-RaSR8zuxRtHgU0siRSpeTe4MbSHEJyWmYIyutSxVD2WLceDfNGgsJBVcjUc8EHogDL3NWNjiXNza1OT6YHsyjxScYocDWUSkRQpJPr-zXIpFKYF5QVVN75H87pTAvc9rNPjFx-KlZS0Ou1l93p25DvyZr8wAvPkdAau1AX2usX3zUyTJzq0ID2tdxAMHQI5OCCEFVBjTuwncy__89NkPEhC6ZX-LirCsFkmMXzdW2Aw0tAGGOVX5Y9xZnAYYfEjtWO4drVzhGVFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:
1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم، بدون اعصاب‌خوردی و بدون زمان زیاد اون کاری که ما می‌خوایم رو انجام بده.
2- چیزی که من از ویدئوهای این دوستان عزیزمون فهمیدم توی یوتوب، اینه که میان با مدل Whisper و یه انجین شروع می‌کنن به کات زدن(که همون هم پر از اشکاله و نیاز به ادیت فراوان داره) و بعدش شروع می‌کنه با یه سری mcp و یا پلاگین کلاد کد که اونها هم اکثرا نیاز به api key پولی یا اشتراک دارن(کما اینکه خود کلاد کد هم نیاز به اشتراک داره) یا یه سری ها هم با Hyperframe، واستون موشن گرافیک می‌ذارن.
3- حتی همین موشن گرافیک‌ها و... هم باید قشنگ و دقیق بهش پرامپت بدید. این نیست که خودش متوجه بشه و این کار رو بکنه. همینطور توی این ویدئویی که تام‌نیلش رو گذاشتم، طرف برمیداره کلاد کد رو اگر درست یادم باشه با Opus 4.8 می‌ذاره روی Extera High effort که خب توکن بسیار زیادی هم می‌بره و فقط ۴۸ ثانیه‌ی اول ویدئو رو باهاش ادیت می‌زنه(بقیه‌اش رو داده ادیتورش
😂
خب مرد حسابی، واقعیت رو بگو دیگه. که مابقی ویدئو رو دادی ادیتور خودت ادیت بزنه)
4- هایپ اطراف برنامه‌نویسی هم زیاد بود، و تا حدودی تبدیل به واقعیت شد و الان ai سرعت برنامه‌نویسی رو بیشتر کرده. پس شاید بتونیم انتظار داشته باشیم توی آینده‌ی نزدیک، با هزینه‌ی کم و یه اشتراک معقول، زحمت ادیت رو از روی دوش ادیتورها برداره. ولی جایگزینی رو بعید می‌دونم</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4219" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4218">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کاربردش می‌تونه اینا باشه:
۱- وقتی دوست دارید هر چیزی رو بگید و در لحظه کامپیوترتون تایپ کنه
۲- یه ایجنت لایو با Hermes بسازید
۳- و کلا کاربرد عمومی. مخصوصا برای کسایی که disability حرکتی دارن و مثل خودم توان تایپ کردن زیاد رو ندارن</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4218" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4217">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه. کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه. github.com/cjpais/handy‎  فقط کافیه شورتکات…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4217" target="_blank">📅 18:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4216">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gi3FaFnHqiE-sDzJzZu5K-xBAG6NwArB9OcRS0bZDwAGN1f5RtD3rPFKkXB5tnNbya3X1WYo_Zml2lfS3bcAc4boMTb47CG5FXAxgwuz9HuUaPnoW42c801jGmdKaybk_bkIbuaobcpPohcvIbkvwsCnO8jye8ogKJBppZ6niOjmQ9bFNpl-lEoTcT4j_2ab_G6DU-QSRVLh077_ryloJyLcMxDpkj3DyBHTDHs-r75xxZr2shKQVNBqbCLLf-COvNz9oSkB52mP4dj9zFkYK5rhuIznzVjrKC7ZQiDTPVVjFXErgNLHUrC8lgy1MDgIo5N3XhMDRZd3vyxYuxeQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه.
کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه.
github.com/cjpais/handy
‎
فقط کافیه شورتکات رو نگه‌ دارید، صحبت کنید و رها کنید تا براتون تایپ کنه.
اگر دنبال یه ابزار STT بی‌دردسر و رایگان برای لینوکس، مک یا ویندوز هستید، حتماً تستش کنید.
✍️
apt_hq</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4216" target="_blank">📅 18:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4215">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VSd2cgyScHUXM_IywqGWCTKhORtGJ_kn0SsSE084VA9EEcaJpx_zOAPJUjEy_W8pEUox9PugzhmWZz4b5_S4XujyrPsIG_JSvfz2_3uy1yCIm6aK_WikgMPRRxDyuLXVEbM5T4yQtS4TynSVoeKS6aBy-ZLdIiGR8yf1K49jYbTW2mApCFOxYyM10t72Z-igQrYdRAEnlvtwn1gfpv6x_q6sMAyyNBi07wxamYdAm0neA6cXl3rm-IyoctXI7nhwVT6A0vRqw3C97TDHBu2ftjSzHS0xYgZHycYnjgohYjvyQmND6tcrhJi82HN8FRXvl5pBVp5eXS0379_Iy28Tqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دادم برسه
3 ساعت و نیم شد ضبطش
😭
😭
از بس دستورات هرمس زیاد بود یا طول میکشید(کل ویدئو رو با api رایگان رفتم بدون سرور و... و واقعا هم خوب بود) و قلق داشت انقد شد
اما ادیتش کنم ۲۰-۳۰ دقیقه بیشتر نمیشه</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4215" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4214">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">برای مثال کیوریتور (Curator) که توی ویدئو توضیحش میدم، یه جورایی کتابدار هرمسه که تو پس‌زمینه سیستم بی‌سروصدا کار می‌کنه.
و Skill هایی که خیلی وقته استفاده نکردید رو پیدا می‌کنه و آرشیو می‌کنه تا سیستم سنگین نشه.
ویدئو پره از اینجور دستورات و همه رو هم تک به تک انجام میدم و تست میکنم و صرفا روخوانی نیست</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4214" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4213">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هرمس قشنگ یه کارمند تمام وقته. ویدئویی که تا آخر شب می‌ذارم رو حتما ببینید، تا بتونید از تمام پتانسیلش استفاده کنید</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4213" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4212">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4212" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4211">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4211" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
