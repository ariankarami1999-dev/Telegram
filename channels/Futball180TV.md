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
<img src="https://cdn5.telesco.pe/file/UbdZzDUhN6YrwJFWDmoS48VBAiyD__74kPyYOIB9zHvCE1N5WBCYy9QJmW8wHmYgRGpjqaK-iWB1AS_VscG_5bHWjIj32zok8JJXo3RgGKT0A5XkAPsu3YHxyQ2JlWFXljevnhF6gEExAbGf6fvaGAHS3_pGrfoarR7QqKB8GvFL9-e1GaKKMEUbW9ND2G42Vp0vsJzkuNaiTFGVQu6Re-T0MgOEBVr-zkFyx4ExjoU5dRg9NGH1sHJAt94eO6773wnZbonD1qOfQjMqQES6fUt9KtaRsmyoecZSK4Ngo6r-iZveeVb5tL9PTMtxB10lU8OEXSHAfzgCLx-TakQsxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 402K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 23:07:58</div>
<hr>

<div class="tg-post" id="msg-107209">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=lmbARgmBz2U2VnhFYhG64wsqdM3iU-V9S7vwHP7Fldq2VbhP6j7-OsqIuqiC9YnTWeBB74xudBkPbdcnN7h7WGhfWsGu8g_HsnDPHnQH2b-tgYFWmnPP8wk4rbd8TROye90E0e_6aV5qP-yTet_TPrCQEeX6voNXAD6iYW7AYja37SQFRE0d7nBnZXzeahumkOpz2DSHZztKNPLUi5V3CsI8Rwg-YTrn14njhzA6C0VZ9ihQb9SxTNa_69z6TSrQJ3QmdOgEV0CZCBaC7aR1U3EymeALlEbVG1IP3mBBum9gJ6zMGmG4kMC9eh7OE6CMCMoR4bwcsc-K4oxp7O-TZXm7Y_9bsasbiea45A3dnKyVHJIAsyPgrBSNAH9ULGpAZFWLdZXl15rl9nSlv3VLH4gW81oJc5AoIxGLIgcwM82KRhwUZZ1YzSIBHJRJsDt_M-hUiMUQCznbnIru7XOhPMtWeW_--b8N9HxH8Ln7NipswSGq6BafoD7Vgrq5YHDUoxZqDqVJXiuE-mADQEjNKB9babAgqzwiBSH1W8PCn86jT1q3iU3DAoKfVO5WcmSYr6-r2-EhfZWqkcGlAONrxVDAouxs4KYAiqw5nHVMS8Em1y2kZQISv5itnVsKsV8fxMfRPWQIrrCvIiEPWELQf39TsvK8A_jclk99qCCFOTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=lmbARgmBz2U2VnhFYhG64wsqdM3iU-V9S7vwHP7Fldq2VbhP6j7-OsqIuqiC9YnTWeBB74xudBkPbdcnN7h7WGhfWsGu8g_HsnDPHnQH2b-tgYFWmnPP8wk4rbd8TROye90E0e_6aV5qP-yTet_TPrCQEeX6voNXAD6iYW7AYja37SQFRE0d7nBnZXzeahumkOpz2DSHZztKNPLUi5V3CsI8Rwg-YTrn14njhzA6C0VZ9ihQb9SxTNa_69z6TSrQJ3QmdOgEV0CZCBaC7aR1U3EymeALlEbVG1IP3mBBum9gJ6zMGmG4kMC9eh7OE6CMCMoR4bwcsc-K4oxp7O-TZXm7Y_9bsasbiea45A3dnKyVHJIAsyPgrBSNAH9ULGpAZFWLdZXl15rl9nSlv3VLH4gW81oJc5AoIxGLIgcwM82KRhwUZZ1YzSIBHJRJsDt_M-hUiMUQCznbnIru7XOhPMtWeW_--b8N9HxH8Ln7NipswSGq6BafoD7Vgrq5YHDUoxZqDqVJXiuE-mADQEjNKB9babAgqzwiBSH1W8PCn86jT1q3iU3DAoKfVO5WcmSYr6-r2-EhfZWqkcGlAONrxVDAouxs4KYAiqw5nHVMS8Em1y2kZQISv5itnVsKsV8fxMfRPWQIrrCvIiEPWELQf39TsvK8A_jclk99qCCFOTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول آلمان به هلند توسط انمچا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/Futball180TV/107209" target="_blank">📅 22:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107208">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=emKt2cHldNGwVeEaVZ2hM_2iDx4_FZbweFmNlo67m442rGLrKmZmrlNgFe3r_HdAZ0rhLgnNecyeYLDgyOsp1pOawBW39AD9rL4NkrztPnxyHelnrgeL59yQbpdqk7Rv7zb16rqI_sDQmqeRPck1d5XTGbZuZwXS7vsdJb-CA0MkypXPOtpdtPN-MgNBETjQDbbkO-ku-SWNbfqcioWjFvRHXKqlAv8FLdw7XXXnAZYLxoi0El3Qhf59XNn-T0JCRH7IR-ql_lzbV8i18eGHoCVhttXI6LpLJooKkmDtQB3uySOotOGAKIKpWVrlPkiDPIQfTK8ciWTbtZnpJClz0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=emKt2cHldNGwVeEaVZ2hM_2iDx4_FZbweFmNlo67m442rGLrKmZmrlNgFe3r_HdAZ0rhLgnNecyeYLDgyOsp1pOawBW39AD9rL4NkrztPnxyHelnrgeL59yQbpdqk7Rv7zb16rqI_sDQmqeRPck1d5XTGbZuZwXS7vsdJb-CA0MkypXPOtpdtPN-MgNBETjQDbbkO-ku-SWNbfqcioWjFvRHXKqlAv8FLdw7XXXnAZYLxoi0El3Qhf59XNn-T0JCRH7IR-ql_lzbV8i18eGHoCVhttXI6LpLJooKkmDtQB3uySOotOGAKIKpWVrlPkiDPIQfTK8ciWTbtZnpJClz0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو وسط سخنرانیش یه دفعه پیجر درآورد و گفت اینارو یادتونه؟
اگه یادتون نیست، حزب‌الله خوب یادشه، چون ما با اینا، منفجرشون کردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/Futball180TV/107208" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107207">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305c017139.mp4?token=vG_HQO55MdDYdczbuIjHjrcIQh89MEeBHp0PAx11Zh6JN9TQaFJX6vZ8rlDv_WSHHhENO8-jWddgNK71M65Ut-iDW99dWCWxzB7nLSeAbIniz9Gzc4W8ukxaHNHiw_J09D4W86wUbQmaskGPwS_abOD_AKAAbvjSGaQ6GAMHZxAwPxD6xhkJirGORGlLpmFwBML3zSNHb9f9FbhZlzhVscLwixpdN289rjeUDGWZi6FfR0Lqjag0PeyIl61yz8HXR-anowdxNLWRmBmo8w0OQzHnsl4qPrU3A_f7_T2pOQwAMGlnFmdOH4LJGnb7eRz4qbuvoHV7SUEvUtfEcD_ghjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305c017139.mp4?token=vG_HQO55MdDYdczbuIjHjrcIQh89MEeBHp0PAx11Zh6JN9TQaFJX6vZ8rlDv_WSHHhENO8-jWddgNK71M65Ut-iDW99dWCWxzB7nLSeAbIniz9Gzc4W8ukxaHNHiw_J09D4W86wUbQmaskGPwS_abOD_AKAAbvjSGaQ6GAMHZxAwPxD6xhkJirGORGlLpmFwBML3zSNHb9f9FbhZlzhVscLwixpdN289rjeUDGWZi6FfR0Lqjag0PeyIl61yz8HXR-anowdxNLWRmBmo8w0OQzHnsl4qPrU3A_f7_T2pOQwAMGlnFmdOH4LJGnb7eRz4qbuvoHV7SUEvUtfEcD_ghjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
نابود کردن تأسیسات هسته‌ای ایران
کار دشواری بود؛ واقعاً بسیار دشوار بود.
اما برای من، این یکی از
آسان‌ترین تصمیم‌هایی بود که در دوران نخست‌وزیری‌ام
گرفتم؛ چون اگر این کار را انجام نمی‌دادیم،
همه ما کشته می‌شدیم!
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/107207" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107206">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22263541ab.mp4?token=Wk2mpeRZI1EytheiAtLUPP6HNOuBnXFo74_UmVqO1gOz2c024oALnvHQctfD1M-i5b4gpocyMcpKt7dLxmogN33wlHCNQzTNdiTRQHs_QSb39chyL3nYzyxHUzEqse0t1sf4R9pjta7MVvgXymmYtIG1WF-BfenrFjorOg6UA2Sny9UqIQsI1unRQ8xPU2VovwCEgSj1UbRvVBsmzVO7UyeQEhr0gCv7323zX4bIFu1myNOCTScUcbKPGAjsvuJTvXIlGJQuHivkX1qqSajugM70k2_8EufKRTCeJRU4H8g-vByywXsst9qLiUwvCjcqHhGk3q_eQe5wNN7f7sFtJomnj8ilZPrIIYBczf3o1ldFPppfPTtFBfD_B7d3E4Se5nCyZERUl9aGCMPc2NHD_nwDnDIN3w0WtNV_IX_PN8nQNqeEUuDlArYu1-2Dene9TAnFIaOpTR14j8q3vur4Or-ZWNCeQjTu7mM0rotwrZvz0nrapMYVYWloTkzdLsgE5JIMWU_H8wCpI_KQB_sRGSGAvz6ZKE-dFbq0mit786L0Dad5M5ExIJjXw8Sze5WhMVZMBlSpVLERVPkWzkoIqBhcitnTPdJgy6YjLpRWkaH7AfHuo0zcyX0hV9LxGdEqqr7QM2CCQn2CwK707o17Mguc4-Px_df99GzIO5gtrGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22263541ab.mp4?token=Wk2mpeRZI1EytheiAtLUPP6HNOuBnXFo74_UmVqO1gOz2c024oALnvHQctfD1M-i5b4gpocyMcpKt7dLxmogN33wlHCNQzTNdiTRQHs_QSb39chyL3nYzyxHUzEqse0t1sf4R9pjta7MVvgXymmYtIG1WF-BfenrFjorOg6UA2Sny9UqIQsI1unRQ8xPU2VovwCEgSj1UbRvVBsmzVO7UyeQEhr0gCv7323zX4bIFu1myNOCTScUcbKPGAjsvuJTvXIlGJQuHivkX1qqSajugM70k2_8EufKRTCeJRU4H8g-vByywXsst9qLiUwvCjcqHhGk3q_eQe5wNN7f7sFtJomnj8ilZPrIIYBczf3o1ldFPppfPTtFBfD_B7d3E4Se5nCyZERUl9aGCMPc2NHD_nwDnDIN3w0WtNV_IX_PN8nQNqeEUuDlArYu1-2Dene9TAnFIaOpTR14j8q3vur4Or-ZWNCeQjTu7mM0rotwrZvz0nrapMYVYWloTkzdLsgE5JIMWU_H8wCpI_KQB_sRGSGAvz6ZKE-dFbq0mit786L0Dad5M5ExIJjXw8Sze5WhMVZMBlSpVLERVPkWzkoIqBhcitnTPdJgy6YjLpRWkaH7AfHuo0zcyX0hV9LxGdEqqr7QM2CCQn2CwK707o17Mguc4-Px_df99GzIO5gtrGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
۱۴ سال پیش
، روی همین تریبون ایستادم و یک
خط قرمز
ترسیم کردم. قول دادم مانع از دستیابی
حکومت ایران
به بمب‌های اتمی شوم؛ سلاح‌های هسته‌ای که برای نابودی اسرائیل هدف‌گذاری شده بودند و می‌توانستند
تمام جهان را تهدید کنند
.
ما دقیقاً همین کار را انجام دادیم.
این کار
بسیار دشوار بود.
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/107206" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107205">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=ddD7bXWAHVq-rV_WpSzi5y0uUyKgzXdqlzjBGJ8kOI7J6Jm-Ygg_p0yqI9sjI6jYfXR0ZH3cfskg6v2JjR_UBuGNOvoVQDWYnpkpRX8wRftBHUStQA6Pb3VFFNYyDYc3Kd-Gyq6TKpRhsxIrn1coMZWyFJYeEHV5tkkHmNmfao2vhMgvZ_-QVU3yZZWqXXcEPnRE467ktQNuSbtcAj2OEWqo-5wke4U5V_OfFkVmJ7n8tmVKfKeDniQ4YD986-wZpvHhMErq2MZWh5s9v843kyHHJGkxTV07FgjrJKmh2b3fTbYOKqelmwf0hAwhG2DcHUJw3G4EZMhR_wCo0SZ5dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=ddD7bXWAHVq-rV_WpSzi5y0uUyKgzXdqlzjBGJ8kOI7J6Jm-Ygg_p0yqI9sjI6jYfXR0ZH3cfskg6v2JjR_UBuGNOvoVQDWYnpkpRX8wRftBHUStQA6Pb3VFFNYyDYc3Kd-Gyq6TKpRhsxIrn1coMZWyFJYeEHV5tkkHmNmfao2vhMgvZ_-QVU3yZZWqXXcEPnRE467ktQNuSbtcAj2OEWqo-5wke4U5V_OfFkVmJ7n8tmVKfKeDniQ4YD986-wZpvHhMErq2MZWh5s9v843kyHHJGkxTV07FgjrJKmh2b3fTbYOKqelmwf0hAwhG2DcHUJw3G4EZMhR_wCo0SZ5dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سانسورهای تلویزیون که مغز رامبد جوان سوت کشید موقع گفتنش!
🎙
افشاگری باور نکردنی رامبد از سانسورهای صداوسیما: بعضی از افراد آنجا مریض جنسی هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/Futball180TV/107205" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107204">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VevRKvRoi9jEML0mIIsYfAvCpQ2S-lBNIXVX9n-HoZ4hDkhx6z2CwvnqxXRIYXpnRfdwcX27ct2vllZh-0UtKw8aaeRdI6x-Ioqx5FQFab5sbby4n93F4PyKGVX616mB1qYvCnAsW2dFb_XfGX_5jKlGq0VJQnfqYjWpTUNGT51s7efoEWYEPnNgUGL82DZZpLGErJKIL3lVBx3AUj2GQUS9pE6IyPe4H8TJaqtmFRXLXezZKd72NN9f7E3kZpDDeBpPhSigkm-aO40HFp-tGDSVP8sS1kthufrQWrp5_CHHWBPDSB0ufsu-ymc6wxB4MQS7KyIBX71pFZs3nXov5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
ترکیب هلند و آلمان/ ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/107204" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107203">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajcqHa4MXGQPo11tEQJaBMoNqdZeGAaG2V37aP_aAILKzJxjdvlUThLoHWFxh7dHMoPFQSsS78IkWhkDKuhLvImfBIaY4tSLxu32U_c8yo8k4Azq3RtWQw4L_vCxHi0-S6Dl4WYM6Uioc1K1M_89Fw3nt11l9Udfm2cvCtCmSAsSKixpnfEL-mRi8_WO8ZWfublLCHd30Ni12sEXRegSuR-Q37f5-jINm89n9uHqy4V6cHEwoXpEaQIoMCfLqRyVEoBA_yHVd4hba2-ZpDXfdzgdlV7EBND37NlpsyfC375wNhTZtrhgAosUJmX9qZE2lriAE54_1UjIrTZXCQyPHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
ترکیب تیم‌ملی پرتغال مقابل ولز با حضور رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/107203" target="_blank">📅 21:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107202">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=SZWYNCsg8_QdGf6XPdQMoFZFWqhMPrB0352GGAnmJyRYiDmLgh-JBd7FBzG1kx4l1cV5J0IvRGsD4vMjA8GwC7vjjQkhwKOfSOTCqQ0ylEsn4uw4Tlxipyw1ei1T45XiYtmyRzNwk78VqB50R4GXyh6k9VdHKPmSwfZdL5xyqij1fe9H2OBXd_pXQ2Req6Q-Fzc0u6Q-2gKeMnbnEFhHxW-jfF3Ln2F29n59MQx31budls6Ofit0-5pm9vxWFvBf4tMJW44_FiC61hv4Lctne897kOzbLkj8hbAVJdd5EoAWS4JmbrnuEpy2PD23uhhUZYKxM5CSL8v58XMms0o9oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=SZWYNCsg8_QdGf6XPdQMoFZFWqhMPrB0352GGAnmJyRYiDmLgh-JBd7FBzG1kx4l1cV5J0IvRGsD4vMjA8GwC7vjjQkhwKOfSOTCqQ0ylEsn4uw4Tlxipyw1ei1T45XiYtmyRzNwk78VqB50R4GXyh6k9VdHKPmSwfZdL5xyqij1fe9H2OBXd_pXQ2Req6Q-Fzc0u6Q-2gKeMnbnEFhHxW-jfF3Ln2F29n59MQx31budls6Ofit0-5pm9vxWFvBf4tMJW44_FiC61hv4Lctne897kOzbLkj8hbAVJdd5EoAWS4JmbrnuEpy2PD23uhhUZYKxM5CSL8v58XMms0o9oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجید جلالی: میلیون‌ها دلار خرج مربی خارجی شده اما برای ایرانی‌ها هزینه نکرده‌ایم به همین دلیل است که می‌گویم قلعه‌نویی از مورینیو بهتر است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107202" target="_blank">📅 20:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107201">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtwCbzLb04FpKGg_laLlz3zUyLvrAakawLjAj3aLp6OB0efRIGRIW5eC6ecS3Zc7eVDEnQOvWoFcem6Kiuf6-uR4Klhl2OeEVVknQ9qG5qJkA0eNBWpaoNDep-tDqtyuKSeOnGMT5WnLW4QuhKjf9xDxc40P3slRneZC0xXMc3nGA5gIPfMkryv_hwzT-4P3CPbKO33IcbaTpoHSvWSwTi4twemZYlC0z71Clvhec17zat81BXGu76epqt3fQEOG001NHnSshaLxvkdGu1dx6jnjRjNCfAV50YYmTLcwjQ1SDt4KqTckNbX4U68uvuhEqCsfBcvFe5YX9ZGL1A6HPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
🇩🇪
اسکای اسپورت: بایرن مونیخ در حال بررسی امکان اقدام برای جذب دنی اولمو از بارسلونا در پنجره نقل‌وانتقالات ژانویه است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107201" target="_blank">📅 20:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107200">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=Ado3XrU9bQp71LdRWylutdzvJmfNgmcSjAJM4x9IPyb_PeBdk0zWo44aqnt7OkXZgA4e12UspJa7GWJXv7Be1GW8tfKmsr_YdlQbiggIe7CxaefXYvsYShAcUnXxmx1IWdqH9xxzsKitizcIpIS89_QEiC-dwY-wYWZM16Yp1Omq3_JSU9duKO6cic0ofdNlPYJ_CX48QZak5SFnF071HdOYYLJ5DYiRgxG7YpzZZBpCSePwQq6-xZ1liDm-YXVv9AXXDKqqELNJP6hnj2Gq_xLhp5UderGgIn0NWnOExBk4ufTALURq_dCEygdfsYcZNSHgzfR_34_S_KGjTUhzmq5b71SgLHxsRbasp6VtjpYrIxI0F7SrTfImbe1TBHAQmqQB1gsg5Ih7wZHpvMwLLnN3c0P21QMAUuXhAvoyth_gZ6SMDH2nYjwQZMady3QXDsyICGMJdOfH2hh7etrO31jkm6T52UeFhoIOsT-ejmeiUdndQW89a3KjzWArNP63cwcgmhnMUZ8rlG8Xv3sVp_7Q-dh5Sr7wh5NKDd25Waa8x6LbcZYcPwEvAgrP0ujo5VxXIv1BZprQpl9_pse1D0wCNj_alvTctWCGKUyQPMEB7044obAP2Qi1DADS8k21CsdOgdC2hSeXxGVMsGrxYYhOgVcgg6AGjTWgBdE8c0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=Ado3XrU9bQp71LdRWylutdzvJmfNgmcSjAJM4x9IPyb_PeBdk0zWo44aqnt7OkXZgA4e12UspJa7GWJXv7Be1GW8tfKmsr_YdlQbiggIe7CxaefXYvsYShAcUnXxmx1IWdqH9xxzsKitizcIpIS89_QEiC-dwY-wYWZM16Yp1Omq3_JSU9duKO6cic0ofdNlPYJ_CX48QZak5SFnF071HdOYYLJ5DYiRgxG7YpzZZBpCSePwQq6-xZ1liDm-YXVv9AXXDKqqELNJP6hnj2Gq_xLhp5UderGgIn0NWnOExBk4ufTALURq_dCEygdfsYcZNSHgzfR_34_S_KGjTUhzmq5b71SgLHxsRbasp6VtjpYrIxI0F7SrTfImbe1TBHAQmqQB1gsg5Ih7wZHpvMwLLnN3c0P21QMAUuXhAvoyth_gZ6SMDH2nYjwQZMady3QXDsyICGMJdOfH2hh7etrO31jkm6T52UeFhoIOsT-ejmeiUdndQW89a3KjzWArNP63cwcgmhnMUZ8rlG8Xv3sVp_7Q-dh5Sr7wh5NKDd25Waa8x6LbcZYcPwEvAgrP0ujo5VxXIv1BZprQpl9_pse1D0wCNj_alvTctWCGKUyQPMEB7044obAP2Qi1DADS8k21CsdOgdC2hSeXxGVMsGrxYYhOgVcgg6AGjTWgBdE8c0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خیابانی: تیم‌ملی با امیر قلعه‌نویی تا دلتان بخواهد به تیم ازبکستان باخته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107200" target="_blank">📅 20:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107199">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=uaY4WGPwnBpq49XNEr3P8aaDYj8-Hrs4APoYIq7vXTyoIiLv3NzNT_rR_P4t1rAmACy-fmyWqebnMJHpcsNfSafFN4CY0qw85nJaDdSM9JzAgxPTee1m9aWatKpzToYLPbQf1k6hh-BtMyVwAfJBbCvn-fVBU1xiyDTRGLDKnemyOsPLAW0jdkkSsKBLxf2FldiyrodL3Fje-9_weeCSXuq3U8rkp6P79iN8_k_i5TC-UpMPXn6ezbvCALtmHqLzll_g9GE26hRTiKUX3qL4X18bLZkhZsbZ589MfcugOyKHpE9UQLTXjLMFe2CK199HxXllMIgk3OgyJNSBv__6vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=uaY4WGPwnBpq49XNEr3P8aaDYj8-Hrs4APoYIq7vXTyoIiLv3NzNT_rR_P4t1rAmACy-fmyWqebnMJHpcsNfSafFN4CY0qw85nJaDdSM9JzAgxPTee1m9aWatKpzToYLPbQf1k6hh-BtMyVwAfJBbCvn-fVBU1xiyDTRGLDKnemyOsPLAW0jdkkSsKBLxf2FldiyrodL3Fje-9_weeCSXuq3U8rkp6P79iN8_k_i5TC-UpMPXn6ezbvCALtmHqLzll_g9GE26hRTiKUX3qL4X18bLZkhZsbZ589MfcugOyKHpE9UQLTXjLMFe2CK199HxXllMIgk3OgyJNSBv__6vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقادات تند جواد خیایانی از بازیکنان تیم ملی امید
: برای کره نه مدل مو مهم بود نه قیافه. بازیکنان میلیاردی دو زار بازی نکردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107199" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107198">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_mX414NWoOK5VVAXxJaVnxaQ1CjOlV5Ofv_Db5DGpSVhdQvMwvV9K3b5gigvaumln1eZZvdo0qOdE4JAeMUHgWZtUMaDzq4fMskJddHyV4iOLaE0ifeHh-HyDZZmP8BMVtWJTiTA5paYg6kQ7sPXlEIlztIm1jBFeOdw8zBZC85XbZg6vCInMw8mngVDeW-tUt7SlBi9iYUVWXTd-crq7wEhbY9FWuS1vZ7tvhMPM4sT5CRCBUGilPManAHL6pUCUe8KC4IoO2O5ZN0TsssnWLQ2yxBa_2LHHL8f9eD62v_8THfSLID9hWuw1Hjh84KHPigvFXXfhrGKzSB8Vhg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
رئال‌مادرید اعلام کرد که ابراهیم کوناته دچار مصدومیت شده و مدتی از میادین دور خواهد بود. به گزارش برخی منابع، این بازیکن به دیدار ۱۰ اکتبر مقابل ویارئال خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107198" target="_blank">📅 19:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107197">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=AU_QrK2UY4JGfu5FknhdbhOoGW7qExvdVVM2acv9CRbGYrdbrV4EValWjPRyw9JS7LCbVmBXUbipsrwAL05SRjpUi3rl9swBkQ7ZdQxWlB0SBQ87GDH-HKCRaa5oZ0KBOGs9cD9G9fPb2QVAJjzx3mOQJZGYZVIeEU6r2Xsg9v8VisvnUVqF8G0abL1qAm_lutckezcmMfSzMis9NfzHRvXzW4wFOMZofbraglemaSAtIEGpOI2TQmHrTN4rug8F5TTRwAkUT1hu8_3uw0zqnw1AP2v9lxkkk8B572hUdQczVkssYxYHT4iWTUFC7Z6q-crgcqSmHRU9UgoVNNoqQ5QcOf4V5JCuN1HBERtoZ9HB5beKBpZ3bioas786AEhkSKkN5gXe25GIm18SNV5vlyPFYYFWQx4eqQib_WCH-tnROX7C106XVZSGBkBQCHuJJ31s-Pqx-Me8XZI8_qC8SR0LFGMZJ8uXquvzloyReGULsO6BhIPaBowJJwOn0yS3X_zUdi-935odeyZGvURNE1CLVnDrsTH-gBOSqZPzF0ajBUwEw2MTU9XQqemNpgTI9thd6kOlguv-bkqW44HkrqxJEKgn8ERqlflYbrtJDr3PpN9LLN16dlhtHeLb0lJ_4GNwPUxtb95wqAzCwdAWkQ78sCPnx1T3EzrC_hkaK8I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=AU_QrK2UY4JGfu5FknhdbhOoGW7qExvdVVM2acv9CRbGYrdbrV4EValWjPRyw9JS7LCbVmBXUbipsrwAL05SRjpUi3rl9swBkQ7ZdQxWlB0SBQ87GDH-HKCRaa5oZ0KBOGs9cD9G9fPb2QVAJjzx3mOQJZGYZVIeEU6r2Xsg9v8VisvnUVqF8G0abL1qAm_lutckezcmMfSzMis9NfzHRvXzW4wFOMZofbraglemaSAtIEGpOI2TQmHrTN4rug8F5TTRwAkUT1hu8_3uw0zqnw1AP2v9lxkkk8B572hUdQczVkssYxYHT4iWTUFC7Z6q-crgcqSmHRU9UgoVNNoqQ5QcOf4V5JCuN1HBERtoZ9HB5beKBpZ3bioas786AEhkSKkN5gXe25GIm18SNV5vlyPFYYFWQx4eqQib_WCH-tnROX7C106XVZSGBkBQCHuJJ31s-Pqx-Me8XZI8_qC8SR0LFGMZJ8uXquvzloyReGULsO6BhIPaBowJJwOn0yS3X_zUdi-935odeyZGvURNE1CLVnDrsTH-gBOSqZPzF0ajBUwEw2MTU9XQqemNpgTI9thd6kOlguv-bkqW44HkrqxJEKgn8ERqlflYbrtJDr3PpN9LLN16dlhtHeLb0lJ_4GNwPUxtb95wqAzCwdAWkQ78sCPnx1T3EzrC_hkaK8I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمله تند خیابانی به فدراسیون: باید چه کار کرد که کادرفنی تغییر کند؟ نتیجه افتضاحی برابر ازبکستان بود. آقای قلعه‌نویی نمی‌توانید تیم را جمع کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107197" target="_blank">📅 19:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107196">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O77XrFq-RmncbTOhM71Jh1YtXAyd-KuYuUfH-ftsKqtGmW5PBR8mcoQsthTl4sAAcLRp5Z3S3h834sbsrZH3dKZs5vzJi7VVKwMFoTU4mA8XDOXT3LSheiJ8ptG9LFaHo-KWseLpXLCdmTS8G0eFm_F0A6n5fyn7Ecw1iWnDmAhuY6axVsR9Z_ey5g7YZ4mr2q_cQkDyuYOJJom-OGWrVxBm6wi1CnNp5D0vZyl2T9jCfxowhAsiaxp4YKj2tL1yVyugNsRWUECGlPVaZYHtkS4wLvPb8epcZsysy51zd_wLrgscyLjjMKbzTu6oPSOn5oSyoagYJUvUPuih94GYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی دوستانه؛ به پیرمردها امیدی نداشته باشید؛ قلعه‌نویی با دستمزد ۱۵ میلیاردی پیش به سوی یک جام‌ملت‌های تاریخی می‌رود!
🇮🇷
ایران
1️⃣
-
3️⃣
ازبکستان
🇺🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107196" target="_blank">📅 19:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107195">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neLDeLNJFmTk3A9j9Cwyyu9RjFKSK2Qfk2WO9VlTeqdzKDD9wwVy7dk2gdKv1RkJ5Qb--r6xhIBl0rO3z9FEHyLfAOmglIS9Y9iU3bss8VUSOzLoUzSXzCXpry_QLUmjcNF7cMtobtt5lWQd5UwqmvDwI7njqtMSPfM-GT5zfTr6Y0qFc5CiTqdaNCfzy0nZSrt3BhqOr7Y3RS7rHy5RneP10lETpidqsZ4EhTsCjYjh29sv7lM4IbSzednKXi95HpGPd8qNSxd5hyBHnMmWee6Aa7lRdAvUhafdgFGFqA08W2jZpnC6s1u0VTisg4M99hO4uVGaB9g8BoUE9gSioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گل سوم ازبکستان به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107195" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107194">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533284b0a.mp4?token=MeCpWK7SBPD1RgsiR3Z0bztSHbnDA-nvg_obJGeYGTQxLUfmcY3U9WWol7m5fX_yFPy8n8PVafOF5ykNtTRs_GWOCNi_Yj4Rm2_b19gLR0Yp4bKn4S_m4g1t6smx3B7pDEfgGdLH25fp72E-bIcklo7q44asC6dPK9o6EwCDEzTe3_rsiNA6PDUTVKwfb4mPrWNl2-RUNiBY6B9op7AAcO1bNTZW2s8-CdSP6aKtMT1Apz1JYyqJJ_81vldrMcHomxc-TRlBC0Z3g5iAw5Q-OQieYOLG0nA2iJZA94umGYS2sjhp0kBA1kRWjpQLtqIU2HMYFOzHy5bNu6YM8Kc2yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533284b0a.mp4?token=MeCpWK7SBPD1RgsiR3Z0bztSHbnDA-nvg_obJGeYGTQxLUfmcY3U9WWol7m5fX_yFPy8n8PVafOF5ykNtTRs_GWOCNi_Yj4Rm2_b19gLR0Yp4bKn4S_m4g1t6smx3B7pDEfgGdLH25fp72E-bIcklo7q44asC6dPK9o6EwCDEzTe3_rsiNA6PDUTVKwfb4mPrWNl2-RUNiBY6B9op7AAcO1bNTZW2s8-CdSP6aKtMT1Apz1JYyqJJ_81vldrMcHomxc-TRlBC0Z3g5iAw5Q-OQieYOLG0nA2iJZA94umGYS2sjhp0kBA1kRWjpQLtqIU2HMYFOzHy5bNu6YM8Kc2yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
گل سوم ازبکستان به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107194" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107193">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=MhzKPh6snCAM4c6_e8faFxCO8TQhF4F73It0RrPvCSI10_t8navketl5hx9a6IOVUN_Yp4cryLGCV3o__Be2dX8gEMALTfKR3O_t_EKj8HRv_lONWSm3Z_J6ULFBAr8bSZvQOhq5hn6L5ziS5jFV4wMQvu6wp7-zdnEX46gbDyDrthFVsjaqzx7x8NcTnVMReYFCRaR0qYrnoBprCtx-X41FImlhLK7znlnE6_FByN-n_vRUxXXMqW6sI7j4GkNSdax6_eNiXFQ7gv4rtyX3f5O3cvx1f6b60dfvQdkFp9UvLZDJ2Jya1kCN4gVC4v3eeMxSH93-iAODopCqDNuGBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=MhzKPh6snCAM4c6_e8faFxCO8TQhF4F73It0RrPvCSI10_t8navketl5hx9a6IOVUN_Yp4cryLGCV3o__Be2dX8gEMALTfKR3O_t_EKj8HRv_lONWSm3Z_J6ULFBAr8bSZvQOhq5hn6L5ziS5jFV4wMQvu6wp7-zdnEX46gbDyDrthFVsjaqzx7x8NcTnVMReYFCRaR0qYrnoBprCtx-X41FImlhLK7znlnE6_FByN-n_vRUxXXMqW6sI7j4GkNSdax6_eNiXFQ7gv4rtyX3f5O3cvx1f6b60dfvQdkFp9UvLZDJ2Jya1kCN4gVC4v3eeMxSH93-iAODopCqDNuGBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌دوم تیم‌ملی ازبکستان مقابل ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107193" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107192">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=P7UZRFp54uuK95P3Izhq8J82BczS2co0LWVt18MtvVtl36b6YuC_5vGsGn9sENHVhps1AGwINMjeW9Xxbv92QhWhhhfFYkagwYnaBHloM3R2WYraLUDQWsg6taLJqMK2f2pf6r0R9aEvbps5W-e_tLSS5fXWRcoP7iUGp1MbBz__xOVWHhbbK9aAgTcgF7dZJmGGu3LIRudahuLU0fnQd-3hbV2UG3RT7sjk4181RRF28ZKZlr8vb3n3jNR5R6Mjxi90dJZ-nq_Fgyj_mwX0ZQn4xpjZYPJdQlsqT_wLvfz-eqqYJwJSdodIkhOqy-VBih8cudB52fiHBCS1-WzJWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=P7UZRFp54uuK95P3Izhq8J82BczS2co0LWVt18MtvVtl36b6YuC_5vGsGn9sENHVhps1AGwINMjeW9Xxbv92QhWhhhfFYkagwYnaBHloM3R2WYraLUDQWsg6taLJqMK2f2pf6r0R9aEvbps5W-e_tLSS5fXWRcoP7iUGp1MbBz__xOVWHhbbK9aAgTcgF7dZJmGGu3LIRudahuLU0fnQd-3hbV2UG3RT7sjk4181RRF28ZKZlr8vb3n3jNR5R6Mjxi90dJZ-nq_Fgyj_mwX0ZQn4xpjZYPJdQlsqT_wLvfz-eqqYJwJSdodIkhOqy-VBih8cudB52fiHBCS1-WzJWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه اعلام پنالتی برای ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107192" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107191">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592ed07452.mp4?token=qdIQ-JHTWNnedxu9-ENa6Mi6U6DEVEXCrofHvNE_YZnw1sUmmy2GHQ3QyjntYhv_u8AMU32FKnHf39y4XUban8VL_yte7VbInc_D3DKdu9n3yeEI_FKko15Y97cuLrhOl8YLqsvOE-8ck6PSiZ64SdYe8YfyR4yTrb8Lbno6dgEdTBKG7OpbILx4Og62yk6F4rRi6yZENRUgUZkaqju8x4huzHtJKYan_h8lUyHdcrI-uuaKzlElmdUkzpFpmsKd0RmeajrlCEreutQ9NKKRb30OzLw89iHPk4KHYWMzKa-Kgq-AcLMixh3CSakT4rAr_e8ROTcJq5MWBw_6f49QDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592ed07452.mp4?token=qdIQ-JHTWNnedxu9-ENa6Mi6U6DEVEXCrofHvNE_YZnw1sUmmy2GHQ3QyjntYhv_u8AMU32FKnHf39y4XUban8VL_yte7VbInc_D3DKdu9n3yeEI_FKko15Y97cuLrhOl8YLqsvOE-8ck6PSiZ64SdYe8YfyR4yTrb8Lbno6dgEdTBKG7OpbILx4Og62yk6F4rRi6yZENRUgUZkaqju8x4huzHtJKYan_h8lUyHdcrI-uuaKzlElmdUkzpFpmsKd0RmeajrlCEreutQ9NKKRb30OzLw89iHPk4KHYWMzKa-Kgq-AcLMixh3CSakT4rAr_e8ROTcJq5MWBw_6f49QDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول ایران توسط رامین رضاییان(49)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107191" target="_blank">📅 18:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107190">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMSNekmPkNe9-cbkgvG3unDZu78KWxMZwNrD3SrWlhgujXfpV_x8XWV28i2PPFSQ3opgU_IoNRVamPUcIj5uLyRCf0waTCM7eqZ7lfOGaPsUha3VnHVFecrpKTKn1ya4mOaY-nCbLIm7XrWBuKQsbv6TJvgbn-RbZtDUsoPEPuHWs4eCYMB0nxT67Cvwr6HKRGV_oIdb0Xz1cT6OeYmbm6b_Tv3r7MkqOhYNTmTf5zO1jrg-euF7LZyKzIG0Yec6kRWSLUufzUZxenc8Uva5A52KKcPRUqNqq4HiJqJTrvuTSDtp6mtr191ZTgPI07QWLZNDv77yib3O7ptR7zmdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا روز ششم مسابقات آسیایی ناگویا کشور چین تونسته ۱۳۰ تا مدال بگیره که ۸۰ تاش طلا بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107190" target="_blank">📅 18:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107189">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyI124zXF8Li1Dua_RRfEq2fFamnI9dHxvXHCEOCjI5qKywx7FM5Rsq9UtN4orWkh0_jfOnSWrUYPoien2td0aUw-1HKDKp4J4BtveNaQTQcuM8U_5TyCOY_Tz_ENzfYfqkcGHsclyELnp4ekgcl3UqwcMMnq6HfHh0_vmbYO0VvJ0EcCEnoRlk4W7oZZBORQ4DUPvhlsyzxVkgxD4r_-O1sDljZh7Aq3mYAdk7kHp9YSv5-Tkm9ONakKoVKpv5Dq6nWMm2k9WOozZBTSZj4D0K5iIcWHRBrvGnpkKgsAnIGvkiVPMJe9gLw1ckG0l7TANt54B_qWwPPCA51yDrpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🙂
واکنش یوز ایرانی وقتی می‌بینه اسمش رو به این قرمزایی که تو زمین هستن لقب دادن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107189" target="_blank">📅 18:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107188">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVOrQYhtvphSiFd_q8aNhcABNUtzT25_T21IbH1NLv6Zin-9Nhm4AUi5KqYcrrjbMbVv0gajDuPES99MAVf_vOrQIt-LBM9CQzF9uuY-c3lFpDzgOtgN6Tm--PuWgMRT5qijuDQQpa3qbnuRI5irNqbXMSUUR0kCp1KVphfYyOxtoMJG8kpGMPwskqM37a91w0uazEK2Ty8dnVnCuzddWQSB8uYu2g32D9JKY6IS1Uf9eVTZtS2wVaJ4nTGEspgsoEOfogu8H3YGM2dxE9l-PWv7Fnz8HmgYAyaFjAzVZ_k_iaEpTqQ9NoFCsYr0T0tHd6p1jiL35g-vRoE3ZvEJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
فلسطین برای ادای احترام به تیم قلعه‌نویی در دیداری دوستانه با نیوزیلند دو-دو مساوی کرد تا یاد و خاطره جام‌جهانی برای ایران زنده شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107188" target="_blank">📅 18:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107187">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz0reSK_lgKex5d6ORxyBXlSRlq4ZXaP_0O3Aeg4wSZlRp_0Dyk9iLfV35JKt8yA9DJJgdU94VjTO8N_wRHrj8RG5RFvYerMAZNrpenNWFwJIPuMEHzF1o5fw0cEi_4Sw7m-fFDgxqocumdyGS-1l33Xvn1DOtBMbsr-HzZdxbolZGGlO_aKlt8Hn7SjQkhyJhKAqO8nRXmFnjdoESc7ykGQ15MQEI0E17os5aYFWOfV3w5fHFuItZtpJi1VuiFi1GQPk5dha2Ej2AOX21RFhbHC1SyPbOJV7clSyFNLmSis1-Xwwnwi8EWnSpV7z4UBuCHECSZP4DPaWLIFkPNVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیب احتمالی برزیل مقابل استرالیا که بالاخره احتمالا شاهد حضور اندریک خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107187" target="_blank">📅 18:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107186">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAglttjaBE3tCxmYoWQN7yDqyDpOEwpm8dWNpBqF8CkCPmSCOWSqudyxYUaRBUhvt3LLyXUQuHTx6h5fexgr-wDKjzX9UQCVP9zw8MVegZ-HwE09bbtXhqsm8RSJWD0FqDZ_QKnWargj0WR_odxN0bPyAhjUHSYFeodiJGueU2lTsB1OU3qUPRJrSpm62IgxT9lPceseBRCsBEBSf6_EDoxJIoOucD_6KoRdotZdIvw4drCKco5pVvuqlJd6CBgwYcQ9-Dvf-09DbGqaIOgM2yfblgHaZwYSzJE2ldayR1yXH0bb0W_COZ1rZd7vYuAeSIor0j2heEEEzADcK28kJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لامین‌یامال: درحال‌حاضر در فوتبال اروپا هیچکس شبیه من فوتبال بازی نمی‌کنه و همین تمایز اصلی باعث میشه که خودم رو مستحق توپ‌طلا ببینم. البته لیونل‌مسی همواره در سطح فوق‌العاده‌ای بازی میکنه‌ و باید احترام زیادی براش گذاشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/107186" target="_blank">📅 17:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107185">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=SxrPLWy0FZWb-I-RKK2jd8_Su1_Kz7XZFyBMghvlhFPavse1tkC3Qza701H4Gr5sco0xxJHZUfN7bKaqSsN4WRUc8wslTF-7ANpDUN0ILzzJWBb75dlWKeAw0TC9S2e9Radro5e2V5iysywIGsRAgXd7bwW698o1R2ZNRYnTMGNGQm-KYNAog2-e09GRlYuXNXa4BOGbhlU_-ZzgG7Pst11IJ-e5iZYknv6pbbKtCkn5CWt8uXDQGy9PxUgQ6g_PxokyVpnRsDC02cR_dZvt8YK9y4ly1uv7hWHAM4aEgx5seqepar6TPAYtnJYRnPoCEbdtgIQ4LnQEbSnfquM1dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=SxrPLWy0FZWb-I-RKK2jd8_Su1_Kz7XZFyBMghvlhFPavse1tkC3Qza701H4Gr5sco0xxJHZUfN7bKaqSsN4WRUc8wslTF-7ANpDUN0ILzzJWBb75dlWKeAw0TC9S2e9Radro5e2V5iysywIGsRAgXd7bwW698o1R2ZNRYnTMGNGQm-KYNAog2-e09GRlYuXNXa4BOGbhlU_-ZzgG7Pst11IJ-e5iZYknv6pbbKtCkn5CWt8uXDQGy9PxUgQ6g_PxokyVpnRsDC02cR_dZvt8YK9y4ly1uv7hWHAM4aEgx5seqepar6TPAYtnJYRnPoCEbdtgIQ4LnQEbSnfquM1dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اشتباه عجیب از حاج‌صفی؛
گل اول ازبکستان به ایران توسط شاه‌مرادف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/107185" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107184">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107184" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107184" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107183">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egh-fpgP70qDOg-bmO4N5oEnOGUc589W9QOW9Zylnxlu_PyRvF7xvTUETBoPhC5751j-WmXav6ufKnx9MPfY1nFKUm2_4sIRoSTLa6jkwVY72cKB848ncusUnW_Z9qgLJABSZhELXuC60Aj_YhjzTKTza87slEMLQm5uuPl95XbKqj9xHYETaHS0O840erOz8D8UkEXpPHS3zdhqyPUIweZXihWlfHaiywGi5QmYJqBeLJwlyDxiau2lRVd32IuzOyXu2J8ldBMES7A_DYfBqHdaJojf-GdnPOWaUc3UNwcX07H6NnZCYbZ5JujJfaJnEGCvfDKj3qRkSpMooE3GQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
ولز
🆚
پرتغال
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ولز: ۱ برد، ۳ تساوی، ۱ شکست و ۱۱ گل زده
پرتغال: ۲ برد، ۲ تساوی، ۱ شکست و ۸ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107183" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107182">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmAsgtqQ6-9x1ibRo61hJbl0d78XzWc9F90BzQtSoFDhRTeoA1m40M3u5tkxOl57sgh2VjkVb9S4XD_oRUXi5jyibnka5ZbNEUa6qx1j-5yTwje3-6YxiIUwh62ski1aRjPbzpsel5rHiUt5odlOvz0oQdIRqd3fu74_AA23nxkUxnYw7yjhGvs-qWCAJKZoNZ9_jTMFvLhLBpQYkO4_67DgYOKIR9NQmQBYs-0fNOtK5_Evvdt39w5WDAZEk9fs6I1_RSmmMWRv6_tCGLe9VVURBxrQCYOpC8TWLuqgAZNOyJpRo4QxzKKKu46XymHbhl6WIn-6X5kyet5hpm3kMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
بازی دوستانه؛
ترکیب ایران مقابل ازبکستان
علیرضا بیرانوند، سامان فلاح، علی نعمتی، صالح حردانی، احسان حاج‌صفی، سعید عزت‌اللهی، امید نورافکن، محمدمهدی محبی، آریا یوسفی، مهدی طارمی و دنیس اکرت آینسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107182" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107181">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be9bc4836.mp4?token=RAkxAV0OlbBHiPzthZBPKgL1RcB5NHbmp5GCl3yTzokR_8a3RLC2mmI1dY9R8xCsdJDvrXp6jC64zDusLgXDolAhLpOVtpfCfwIb5JVHuNvGS8U57GB_HpCFnZ1vNQ9WRnhL_VNHbpVYGRmoTWDiprLBXLodG690V7HuXHGlpoLTDu6GYpbsnRtueK2W550IL-Aw8aj2CfM_fgG69cQV-JHQ7c13YiAgiz29Qq91K5hG-g-sbf_kHnwMA5G7oTVwoDJRsKFh4FvwhXst7yuvj0tTTkIXJTCEhIkUPBjoCFCnltPcrhuAqSg3gsBWjUBOSVepaikznTCXPWnqaqwtCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be9bc4836.mp4?token=RAkxAV0OlbBHiPzthZBPKgL1RcB5NHbmp5GCl3yTzokR_8a3RLC2mmI1dY9R8xCsdJDvrXp6jC64zDusLgXDolAhLpOVtpfCfwIb5JVHuNvGS8U57GB_HpCFnZ1vNQ9WRnhL_VNHbpVYGRmoTWDiprLBXLodG690V7HuXHGlpoLTDu6GYpbsnRtueK2W550IL-Aw8aj2CfM_fgG69cQV-JHQ7c13YiAgiz29Qq91K5hG-g-sbf_kHnwMA5G7oTVwoDJRsKFh4FvwhXst7yuvj0tTTkIXJTCEhIkUPBjoCFCnltPcrhuAqSg3gsBWjUBOSVepaikznTCXPWnqaqwtCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سوال‌کنایه‌آمیز خبرنگار ازبکستانی از قلعه‌نویی بابت عملکرد ایران در جام‌جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107181" target="_blank">📅 16:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107180">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a2786f81.mp4?token=s4pMswPANz7pXpgjyFomgZUeb3BXevsxUplHTQLAlnXShQ-MSKsobbCyLeRjErpCdBSaO_hzGVkHEq9KWshMgDk7dQ-U0b7jte4DReKVGLgc3xxYsCYbZoVOlsT3MIbPjqoEU-Z5EHXxlXSTPkPRvcDIiDCjASOGVgtHPLk8ZUqKf40o1qQFMFGuAIqRwZ-qUDvgR5_uXenVHwzlbzguMBlnfUtaXEI0tSs5pDXENEmxYHdGcxVGlnlemaUiwpNYLsTcOOev7iqFfF4QwDqGNiJpPqYGJtpdR_5yRsMDHmWwPi9HyB-4hwZz5R69eVYZQ6vR4Vux4ixZgcvi7NWWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a2786f81.mp4?token=s4pMswPANz7pXpgjyFomgZUeb3BXevsxUplHTQLAlnXShQ-MSKsobbCyLeRjErpCdBSaO_hzGVkHEq9KWshMgDk7dQ-U0b7jte4DReKVGLgc3xxYsCYbZoVOlsT3MIbPjqoEU-Z5EHXxlXSTPkPRvcDIiDCjASOGVgtHPLk8ZUqKf40o1qQFMFGuAIqRwZ-qUDvgR5_uXenVHwzlbzguMBlnfUtaXEI0tSs5pDXENEmxYHdGcxVGlnlemaUiwpNYLsTcOOev7iqFfF4QwDqGNiJpPqYGJtpdR_5yRsMDHmWwPi9HyB-4hwZz5R69eVYZQ6vR4Vux4ixZgcvi7NWWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👏
🔥
🔥
صحنه‌جالب از بازی کبدی دیروز بانوان ایران مقابل هند که واقعا محشر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107180" target="_blank">📅 15:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107179">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIwtIH63myBroea_PxGxEX56xiJ3Lcgx8Fo9F1XCIp0JA4GDR9_B05lQA_tVNfpfJwm_rQRqFa8ZsIwjpbvKZaxjY1Dq5QQft58n1kPHtrbU8IY9_HYc1yW0z80KDsN2F9qR2ELVqDHMkDZj6SBeafccYqZqqzNYW0O1Il8JUpmi1_reGjPHRNV0YH8pkg00Du_P3lHwVmGWKvhuHPOnxb7ov_t6R0OvibzVAwyQIzB8I9ahIOKWx0RCbUh44Kox2HKV3v9elmSBsnRl_VfD6NSoJ3umy7IWK8EVgVPeoMIxWPaBCIGjwzTc7RlU468RUaxeKL68RI-lEo6z4eLKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری امیرحسین قیاسی درباره لیست جدید قلعه‌نویی و عدم دعوت از مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107179" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107178">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
مروری کنیم بر ادن‌هازارد نسخه جام‌جهانی ۲۰۱۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107178" target="_blank">📅 15:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107177">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773eb10873.mp4?token=Gzcf3mx3RrbYuwhUfcUktLJ1Eik7tSXDjVERTKvxA8ia5iwqDs3h2e8IU3CarlZZkJ0zPHnG3i8XdenNtvH5ZAZLJq0lb1wV1-iKg4krHmQjab5qhl5WvlpEg_jkzDLCZEr2jgNOjMW-OUoRQ8DegeARgG-2_k14i2uDV8H6Zutg3pjw54mMv_Wbn577ZPvQ0eJRJYQS4E5tEph7wud9Bclu-2ivHCqLzw8N96XSVgdI6VVR2_AnElf4fJw-8zInDPBcoV5gtK4cTeYix8La9_KRyJf0n8AJekz8A1Yv734K1SUkir2NEv27ymYAmF8p2gMavrpywKV3xm9KPexut3RmRjbVqG7K0uzc9riOX5xSYwWwGJcYYDp7pHPBHv26iOi0R-ZwGakI5wkIo_RfkU643p2_w8xJs9OiAO_CAwO84zlcECvRpnYUhgbf9LrreYyXCJiCozJtgTLaBjmAXGEmB7Uw9_FUByYCAMAONRTfCe4imsBBSOT_aOelzNxan6bjR25VQ-YPl44HfuIfisJqpnNcCATnlfdrCto494z-lZ6OL88SR-aQCs6J0n5NBoYHrv9lk7iREuDbt3xreTCLkyR-1XAa4ChuaTCaZTe5AMs1NNr0a9y31Ouf6KdiMmlfZ9ylMaWbVlHkTTbGpo0pjZEwuA4c5sbB5ugZwVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773eb10873.mp4?token=Gzcf3mx3RrbYuwhUfcUktLJ1Eik7tSXDjVERTKvxA8ia5iwqDs3h2e8IU3CarlZZkJ0zPHnG3i8XdenNtvH5ZAZLJq0lb1wV1-iKg4krHmQjab5qhl5WvlpEg_jkzDLCZEr2jgNOjMW-OUoRQ8DegeARgG-2_k14i2uDV8H6Zutg3pjw54mMv_Wbn577ZPvQ0eJRJYQS4E5tEph7wud9Bclu-2ivHCqLzw8N96XSVgdI6VVR2_AnElf4fJw-8zInDPBcoV5gtK4cTeYix8La9_KRyJf0n8AJekz8A1Yv734K1SUkir2NEv27ymYAmF8p2gMavrpywKV3xm9KPexut3RmRjbVqG7K0uzc9riOX5xSYwWwGJcYYDp7pHPBHv26iOi0R-ZwGakI5wkIo_RfkU643p2_w8xJs9OiAO_CAwO84zlcECvRpnYUhgbf9LrreYyXCJiCozJtgTLaBjmAXGEmB7Uw9_FUByYCAMAONRTfCe4imsBBSOT_aOelzNxan6bjR25VQ-YPl44HfuIfisJqpnNcCATnlfdrCto494z-lZ6OL88SR-aQCs6J0n5NBoYHrv9lk7iREuDbt3xreTCLkyR-1XAa4ChuaTCaZTe5AMs1NNr0a9y31Ouf6KdiMmlfZ9ylMaWbVlHkTTbGpo0pjZEwuA4c5sbB5ugZwVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🎬
۵ پاس‌فوق‌العاده بیرون‌پا از لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107177" target="_blank">📅 14:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107176">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c32e4ce.mp4?token=s3dxxDl7CYK8JYTeDFI6FP7CEqgNAo4xSAQvCl3gPXgdD83HsSWj0M5xBxHJli-t5FFkrWYQOAC7k0inEgmko7DWMHClXMEjo0GIzkgEdvCTjFt11tQz_A81UuG5QtsoK4CC0Iw4pY8KvsWJxqAkBEgkTiQNXPM7UNwLGxH3T4iWHjvRV-VhDPaeRLsoZYNKREgiv0W1zDBQatgFZqC_U4Sx2hBWRoe20ADqI1CmKzvYjpQiiMN7gy0gFxTHwtbR3vuSYxKGk7e8GUXa8q_ZgD-ODenuJVfr8YnMUQTJ5xBxQjj41UHPBapGIIOb_xDLDmvngckCE15xFze1z7JetYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c32e4ce.mp4?token=s3dxxDl7CYK8JYTeDFI6FP7CEqgNAo4xSAQvCl3gPXgdD83HsSWj0M5xBxHJli-t5FFkrWYQOAC7k0inEgmko7DWMHClXMEjo0GIzkgEdvCTjFt11tQz_A81UuG5QtsoK4CC0Iw4pY8KvsWJxqAkBEgkTiQNXPM7UNwLGxH3T4iWHjvRV-VhDPaeRLsoZYNKREgiv0W1zDBQatgFZqC_U4Sx2hBWRoe20ADqI1CmKzvYjpQiiMN7gy0gFxTHwtbR3vuSYxKGk7e8GUXa8q_ZgD-ODenuJVfr8YnMUQTJ5xBxQjj41UHPBapGIIOb_xDLDmvngckCE15xFze1z7JetYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🐐
جوری که دیروز ژسوس سرمربی پرتغال از اسطوره فوتبال کریس‌رونالدو تعریف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107176" target="_blank">📅 14:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107175">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_9fDMeU9m9MAIiDfVJZHTheArLCh0xoxAU0tQDUnMKbmbHyWZiE1IInGaMGeo6MAo99xUlA_4E53CXPGtVaL9y_scoqb4An3fAUQFgT2NGt_lyacX5u0qpFcKpo3BQ6Hsdc00IRzx8OSM-lv2CX52reRlA1Joa_E2pSZFjdBe0HVZQtYoYWK9S20YI3ztq4768KviJ8WvQqKqu-y4OQj1_1B_T2vr6tZle4TjpamTy7z684K5dlDrnVb7Dn8dfXtP3xgE6zYCXRGnIcwtDCNFLsDhB1JSfuCrAF2_wmNpV_BVpDWUA141mmZne0UO24XC1TN-MXiquUv2NfPooIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🤩
علیرضا فغانی از استرالیا و موعود بنیادی‌فر از ایران به عنوان داور در جام‌ملت‌های آسیا قضاوت خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107175" target="_blank">📅 14:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107174">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=ZTaB1tWBzbGb66SFqs-LoNK7jfhC-brqPXdzhjbSNgO0D2Lr60i6dUF3fCNcBsKfZOdIpmVvY3sm_20InAep-kozuW5bX7fh2aLsD_PTVc_fMRu6DW2Wdl54V4dme60KbaHZ8Rl0Hum6PoPiGBTMcMKUSeX9r4D9KCeXYA8ADdWvik9JM38HwnCoJd5Nh1AZB3kweTSS2Aw5KaffFkHQDs9sk7I5Coco30JpktyNdyVGpzcuTbZIs6INsg0UDFoLbtoOC_8XrES5dw84hhvSQ5yTrdlpUxrKj-VEMwtS3W3fHQrn1tHAR_NhpLgemUFOMQK-QWil3yW2_B0hAiWlpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=ZTaB1tWBzbGb66SFqs-LoNK7jfhC-brqPXdzhjbSNgO0D2Lr60i6dUF3fCNcBsKfZOdIpmVvY3sm_20InAep-kozuW5bX7fh2aLsD_PTVc_fMRu6DW2Wdl54V4dme60KbaHZ8Rl0Hum6PoPiGBTMcMKUSeX9r4D9KCeXYA8ADdWvik9JM38HwnCoJd5Nh1AZB3kweTSS2Aw5KaffFkHQDs9sk7I5Coco30JpktyNdyVGpzcuTbZIs6INsg0UDFoLbtoOC_8XrES5dw84hhvSQ5yTrdlpUxrKj-VEMwtS3W3fHQrn1tHAR_NhpLgemUFOMQK-QWil3yW2_B0hAiWlpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
شاید حق با پیمان یوسفی بوده باشه
❌
🎙
پیمان یوسفی پیش از شروع لیگ برتر در برنامه تلویزیونی خطاب به سخنگوی فدراسیون فوتبال: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
🎮
دیروز: قهرمانی تاریخی پلی‌استیشن بازان ایران در آسیا و حذف تیم ملی امید از مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107174" target="_blank">📅 14:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107173">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=r85YDsrERmsmGemc8h94yqxLL1AzbhiQyqdZP3C00c71S6qYY0XBTNcMmXoB-VQRCvb7EXLMoqzfWePmXiyGf9c_kDiGtZXOqUG41KTfkQBmjfJ48quwMsk_kS9x3V_O8DZxn7VfZ2nCiPiwMLxtLo_YFY-4UxqJywCv70-Qr1_rUg55GkrLkux43_rCSFCvX1vRN06GBZxQ-j9Nt-NnCU3AqybNN4O4poRdotQvn2klPjtv_Uu0yiLTC5WEvDfP69r2vkY7jpBKVksDUVG3bHBKbNkD8BFI1z9PkRmxkNPan44e8OGDMpI0oJzU_UBC4Z1eFR26CPfMYsS08DEhhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=r85YDsrERmsmGemc8h94yqxLL1AzbhiQyqdZP3C00c71S6qYY0XBTNcMmXoB-VQRCvb7EXLMoqzfWePmXiyGf9c_kDiGtZXOqUG41KTfkQBmjfJ48quwMsk_kS9x3V_O8DZxn7VfZ2nCiPiwMLxtLo_YFY-4UxqJywCv70-Qr1_rUg55GkrLkux43_rCSFCvX1vRN06GBZxQ-j9Nt-NnCU3AqybNN4O4poRdotQvn2klPjtv_Uu0yiLTC5WEvDfP69r2vkY7jpBKVksDUVG3bHBKbNkD8BFI1z9PkRmxkNPan44e8OGDMpI0oJzU_UBC4Z1eFR26CPfMYsS08DEhhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت های جنجالی هاشم بیگ زاده درباره ستارگان تیم امید ایران؛ از انتقال به پرسپولیس، ده میلیارد هم نصیب دانیال ایری نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107173" target="_blank">📅 13:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107172">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی  «پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107172" target="_blank">📅 13:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107171">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=oraqsowHlI7xdYxR4bJe1xadZC3F-HXl1u0g2l9zzq9PAlYLSRREibXVE2u1pYUG8dxtKqtV1UTlSCSr3Pa94E1ceGnekIOyuIqrppdTYDiZB2LzTmN84hU-q0QpFXut_xH6fKc3wKX_tPQ1DQsrYusv_V4X0CpfKSDCoYVZVsRy2_IX7SGWzpQYucm8xEGZSqksVQuuF2ZUY3p7qzQn0tAl20eLO78TZ8pq2_lOglQGfY5_m95fE704OCF7aWz5kbDUX8XxugyQLjWDyRJZ8cseVzQPz3uCq8z6nl4Vugwtx-qsRm81GoInqXpXGFf_Sqz2dBn8OGw1miXoDq1Z0H4EYmmvOPkf4QnvAQX4b_PxLckAUqTyktvM6BZPAD12VxzSl4JozX_ofs1kEynjjywvjbuMTY8P7g2kyFl9FvSc9gOBlSogoCYBor_XVhLfqVxFYEqLfoQBbCQ7a5HDlEJDGDjDqhuRgbuYzjqpTZmW-zuaR2NLDzXntS5TdnOx9DL4uTXys4DyiziQbTrLBtjaS75mLOadp7tKghvx3B95b-5Q_oopXl7Qi5De0ftZ2as-CnRsvt00XofXKwZKX3g4smrwiI0lM30PqJBWBJa9Y7PPExpjiT88TjFwCl_6PfuG4XInElGM2hrdj6_YbvMwKok4zMbeKYUgXHqcf7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=oraqsowHlI7xdYxR4bJe1xadZC3F-HXl1u0g2l9zzq9PAlYLSRREibXVE2u1pYUG8dxtKqtV1UTlSCSr3Pa94E1ceGnekIOyuIqrppdTYDiZB2LzTmN84hU-q0QpFXut_xH6fKc3wKX_tPQ1DQsrYusv_V4X0CpfKSDCoYVZVsRy2_IX7SGWzpQYucm8xEGZSqksVQuuF2ZUY3p7qzQn0tAl20eLO78TZ8pq2_lOglQGfY5_m95fE704OCF7aWz5kbDUX8XxugyQLjWDyRJZ8cseVzQPz3uCq8z6nl4Vugwtx-qsRm81GoInqXpXGFf_Sqz2dBn8OGw1miXoDq1Z0H4EYmmvOPkf4QnvAQX4b_PxLckAUqTyktvM6BZPAD12VxzSl4JozX_ofs1kEynjjywvjbuMTY8P7g2kyFl9FvSc9gOBlSogoCYBor_XVhLfqVxFYEqLfoQBbCQ7a5HDlEJDGDjDqhuRgbuYzjqpTZmW-zuaR2NLDzXntS5TdnOx9DL4uTXys4DyiziQbTrLBtjaS75mLOadp7tKghvx3B95b-5Q_oopXl7Qi5De0ftZ2as-CnRsvt00XofXKwZKX3g4smrwiI0lM30PqJBWBJa9Y7PPExpjiT88TjFwCl_6PfuG4XInElGM2hrdj6_YbvMwKok4zMbeKYUgXHqcf7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107171" target="_blank">📅 13:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107170">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=nLERqcPp9tFoPgn2X9st_jguj_ZhMMhhAzk6qzrE0eNCmvg2p_sTzhXx8-ilk8GT9E5m0FRjubVIAyfBOuEqvrB3F90NCmqfXp81zX2V7U99JbhESCks9jlHT51SuBTVMdnMwQ4CJRA07_Fb99SsmwRaGiFbS4BUbxhpRpJ72Lh_iClQGFP2xRLBqQkdFDzPrrehpgaHKLy2ZkISKMqu6GznU1ntNYFR73ib_lsXfKvkpcbrWPAcA2TKxzeiacevZ5UsLe7LOi9Y6VAjw3lG_pcWKy_LWs-mj1J6s3U4hNu1EBuCpNyyyT2HbLrNSzYzOHSsiN2EbvFYiDZMPlHAboO6IgINvlBvF-Htu9dsk15DX9UUAnPpYqnyttdcxN7DVtXwTZKoduqcXwM1omHypeGI2PNs_D3H6B8cv4t8vrJzlmEoQkVNT0WfPNs414JCbih7JZbAmC835ltdCP1U0AGN8Rf_usNac-unStB6YDCoJ77B-L2Rkw-HeQNYD79axhNxvKZaEV0DZBYKWOYp0xV3zfbyPRy8OikVaoZ9TyolU65HPkyv6Kcv2ENYqynZrW-rKkphdRFz-QYmrvayGjysy9eg6tI_shxdGXtGyUGVR4sSf9gLIrGBLY2h0kyUipNlz48r_ylxHW0-ck4NtsGBfrk25UWwjWiCDLiJ3uE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=nLERqcPp9tFoPgn2X9st_jguj_ZhMMhhAzk6qzrE0eNCmvg2p_sTzhXx8-ilk8GT9E5m0FRjubVIAyfBOuEqvrB3F90NCmqfXp81zX2V7U99JbhESCks9jlHT51SuBTVMdnMwQ4CJRA07_Fb99SsmwRaGiFbS4BUbxhpRpJ72Lh_iClQGFP2xRLBqQkdFDzPrrehpgaHKLy2ZkISKMqu6GznU1ntNYFR73ib_lsXfKvkpcbrWPAcA2TKxzeiacevZ5UsLe7LOi9Y6VAjw3lG_pcWKy_LWs-mj1J6s3U4hNu1EBuCpNyyyT2HbLrNSzYzOHSsiN2EbvFYiDZMPlHAboO6IgINvlBvF-Htu9dsk15DX9UUAnPpYqnyttdcxN7DVtXwTZKoduqcXwM1omHypeGI2PNs_D3H6B8cv4t8vrJzlmEoQkVNT0WfPNs414JCbih7JZbAmC835ltdCP1U0AGN8Rf_usNac-unStB6YDCoJ77B-L2Rkw-HeQNYD79axhNxvKZaEV0DZBYKWOYp0xV3zfbyPRy8OikVaoZ9TyolU65HPkyv6Kcv2ENYqynZrW-rKkphdRFz-QYmrvayGjysy9eg6tI_shxdGXtGyUGVR4sSf9gLIrGBLY2h0kyUipNlz48r_ylxHW0-ck4NtsGBfrk25UWwjWiCDLiJ3uE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🔸
مرگ مغزی فوتبال ایران طی دو دهه...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107170" target="_blank">📅 12:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107169">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261876d28b.mp4?token=NM5mvuSKFjAocWyf-S3QkBNPKglSf5X2Khpy1Q5Z7_ooNqBwnFb7djOFip8xFVRiH2pVPNdSg-djAsxEg8M-wATFz4RsTvSv8ZdJfJ_JHaZMLw1wzaXCpKeKcdEAX3l-MWRsH8wHncQ96rb0-F91KbxUdoNskeGhAfDhcm8wbr_CO8Rnk2ActbXGeayy4vJFgEUvNiyM8qJirOgUx0p-KfHs5g4cPwM7M02vXjS2QqdA4RTVnXPPNZj1MslJIierkGNMpkexmXN3ee-X0tkrsH_onSDXzCwqhJjj3eZ4rsxBsVhkVIgp4BN67y3Wi1k0HQPyO0VsrZdfQCtntt4F7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261876d28b.mp4?token=NM5mvuSKFjAocWyf-S3QkBNPKglSf5X2Khpy1Q5Z7_ooNqBwnFb7djOFip8xFVRiH2pVPNdSg-djAsxEg8M-wATFz4RsTvSv8ZdJfJ_JHaZMLw1wzaXCpKeKcdEAX3l-MWRsH8wHncQ96rb0-F91KbxUdoNskeGhAfDhcm8wbr_CO8Rnk2ActbXGeayy4vJFgEUvNiyM8qJirOgUx0p-KfHs5g4cPwM7M02vXjS2QqdA4RTVnXPPNZj1MslJIierkGNMpkexmXN3ee-X0tkrsH_onSDXzCwqhJjj3eZ4rsxBsVhkVIgp4BN67y3Wi1k0HQPyO0VsrZdfQCtntt4F7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
🇩🇪
هلند - آلمان⁣ امشب ساعت ۲۲:۱۵⁣
🔻
اولین تجربه یورگن کلوپ و ژاوی روی نیمکت دو رقیب سنتی⁣؛ کلوپ: شرایط هر دو تیم مثل همه اما من نسبت به ژاوی بازیکنای بیشتری رو در تیم ملی هلند میشناسم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107169" target="_blank">📅 12:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107168">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=Wc3MG__VJ-YbKxdPlVj-D5WWFjqJB_9zefPT66ue4pzZKe-TY0yjSxYNBXYJOHfig8yOU9AJiJpTAqdnujI221r0SYM3oesmNvcHd0bhhxcaqHlEsmfk-87-L7T5JfTwXRf49CcvbEEBzvTWz4PHPo5c1-RokEIVf6rR1b2sniS408FzPzfTMTBoqscMAA9d75k3FStHsS2jHr38_2uvlaORTrBCNz0wT73-CegXOKwthpDlWiRQHkfYXQQ1uWSZdd1cMHSMKNcUdvAHrH4WBl50tr9mKKevT6NjSYFnOJ5l6LHPI3Sz1EgqvK_i0QOM-oPq64BIGTdNrIv-fLUNTy1OcN7l5K8DWVuWop1z8_S1-Z566LdXd-X0fioyCds1b7P8bSBLuf-Qh-BQ0V5UqTpB5SIRGv9oGr-wfDPEFJp9BRIND8rkCF7XMi6ti-DbXNx-q6FYvZDvFJ5IMkjLluhXk5NqmzX6F627tCHZk_SzT3RUz0unozKyEMKqpbO_C0wfTY5yoOV5XxEaRDcQNFEf1ry6oQuSxlk-lKKnjzb8aDdqi8XzsdaIcvvsh_MRkOOK3LSBgY8v8-aZqjG52SO3IifUSVNHIGxSXh_9LfLjBJ03d_R5Js_uDI7y_-gMbSxa5Mg5VxGsuun8SbSrqv3waVYRIxJ3nS9nwAGNBZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=Wc3MG__VJ-YbKxdPlVj-D5WWFjqJB_9zefPT66ue4pzZKe-TY0yjSxYNBXYJOHfig8yOU9AJiJpTAqdnujI221r0SYM3oesmNvcHd0bhhxcaqHlEsmfk-87-L7T5JfTwXRf49CcvbEEBzvTWz4PHPo5c1-RokEIVf6rR1b2sniS408FzPzfTMTBoqscMAA9d75k3FStHsS2jHr38_2uvlaORTrBCNz0wT73-CegXOKwthpDlWiRQHkfYXQQ1uWSZdd1cMHSMKNcUdvAHrH4WBl50tr9mKKevT6NjSYFnOJ5l6LHPI3Sz1EgqvK_i0QOM-oPq64BIGTdNrIv-fLUNTy1OcN7l5K8DWVuWop1z8_S1-Z566LdXd-X0fioyCds1b7P8bSBLuf-Qh-BQ0V5UqTpB5SIRGv9oGr-wfDPEFJp9BRIND8rkCF7XMi6ti-DbXNx-q6FYvZDvFJ5IMkjLluhXk5NqmzX6F627tCHZk_SzT3RUz0unozKyEMKqpbO_C0wfTY5yoOV5XxEaRDcQNFEf1ry6oQuSxlk-lKKnjzb8aDdqi8XzsdaIcvvsh_MRkOOK3LSBgY8v8-aZqjG52SO3IifUSVNHIGxSXh_9LfLjBJ03d_R5Js_uDI7y_-gMbSxa5Mg5VxGsuun8SbSrqv3waVYRIxJ3nS9nwAGNBZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇪🇸
آنالیز ویژه برای درک قدرت بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107168" target="_blank">📅 11:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107167">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-ehimdCifZ0Ca3RR7ZxGEcX8Ade8_VhPq-NNcXgpKk1gvkrQfARLYt6AZSFRS1-q9j4pcqTivFdGJkh1ckgMhrzB0ManxTqC8MxifSTWEs4Lwi4HaJ_XuYUZBpMZ29QXrHwHwXKK_XfVD7pO8RM5l3CJ_GFB8rHVYbXhhOi_H0DAY9gqVP_IzX64Z9yl9DlhT-EdMuTbIFk0E0Z9fJH4T4ZSummVSglzDkiQiCLM1JWgZiVqJGqvWxw39-trxtxlmjU8SVXjhXt4MHvqQpHeM9G0kzVc9ySrYWvqifMdqj7TSBlemoA7GY_Px9Tjm1Tb33bQb02hSCRFx41mJ_a3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
5 بازیکن برتر از نظر تعداد گل‌ها و پاس گل در لیگ‌های معتبر اروپایی تا به امروز:
🔻
رافینیا دیاز – 17 مشارکت (گل و پاس گل).
🔻
لامین یامال – 14 مشارکت (گل و پاس گل).
🔹
کیلیان امباپه – 10 مشارکت (گل و پاس گل).
🔻
مایکل اولیسه – 8 مشارکت (گل و پاس گل).
🔺
فران تورس – 7 مشارکت (گل و پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107167" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107166">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107166" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107165">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmpyqLS2veDegP46-1rnTKlspx58bd6FkFyXyvOpPBceWM9rMVQV6qoh02XFjuh0dVgS3bd8QySgxl2463GxuO3MwmP9l_ObSPoAdNJWa8CFd8yZ0xQphadpoBYpKxzee44_Adf34OjKDisUFjEAHjZYrw-Hyvzz8omt50Tf_7tltpgW2ypjVCUqE8SVIjc9PthuYUBpIM1X-IRf3WlMmIEdBT5--RCCbx19sK4CBW2Jp3i3wqdxdM-furB4owl5VVIG4y6_uitM5Af7eJ1Hzt6JHcJZiHI1951mL3n0raptEyFXGOdJdPzA_7oa1o3rPguL_kSiiug9H1SfEKmZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
هلند
دانمارک
🆚
نروژ
ولز
🆚
پرتغال
اروگوئه
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107165" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107164">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwpcrcaeaXhCrY7ipgdlHZM6VRO7V027AcXIU1GAKrk90JSTfofyVAyY0MK4hd3-PwKYAR0L6WszizBmTlw0C8y0IkOH5iuzIBMAxnwMzBdiWe7OGXFnKP8Xu4FKVmwFD4F9HwmVu2wp4uZvjss-Haw_3qi3veWuPY5okFzeG-VvF4my49TemEKJakXvjjCm4EgANWErYhHSY3q7GJTrvEwgOsWMHwxFjf8SPUgI9fmqLXXj0jCqcMzcjNjbQbMXrziyld4KrItFjzTECnmJNAxb-OceFD3MrYVseHwKQYE9u7zxv39acwrG3DgYAoTtTv0cmLw9IZpUfugp2-EnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🔥
بیشترین تعداد گل/پاس‌گل در لیگ‌های برتر اروپا از ابتدای سال 2026:
🇪🇸
لامینه یامال - 24
🇩🇪
اولیسه - 24
🇩🇪
کین - 23
🇮🇹
مالن - 22
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز - 22
🇪🇸
رافینیا - 21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107164" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107163">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=sq7DQMhwsI71il9hKXx0Fbeeg6t_O2nhrFsBHwE6kKaG93pGSZI1RDrvtVrhMXZ2Ol9ahcS0p0oqJEVsdWdqiYL7Hq4WqDfAf43KoBaMA1CmpIEOzu9wppnuvIPC_Irm2L6X_YwEMgQ1SBsoxzPPwD0CaRytguoL0qIwnPys8-Ct0vhhxkQ9tNB1IjkAEGovn5offSvm9HU4hDqCm_rSP7dTbnzeUwa7m_mVvuB3JSeysQMoW7kaHiYsBHdaVRjUL4R1F02IGMknAKAz9dH1IKynvu9VTXAzv652WpHE5OWM21PitJ0eGO0rdpzC3Ng0RJcYPXPdzegfdshe1_4pFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=sq7DQMhwsI71il9hKXx0Fbeeg6t_O2nhrFsBHwE6kKaG93pGSZI1RDrvtVrhMXZ2Ol9ahcS0p0oqJEVsdWdqiYL7Hq4WqDfAf43KoBaMA1CmpIEOzu9wppnuvIPC_Irm2L6X_YwEMgQ1SBsoxzPPwD0CaRytguoL0qIwnPys8-Ct0vhhxkQ9tNB1IjkAEGovn5offSvm9HU4hDqCm_rSP7dTbnzeUwa7m_mVvuB3JSeysQMoW7kaHiYsBHdaVRjUL4R1F02IGMknAKAz9dH1IKynvu9VTXAzv652WpHE5OWM21PitJ0eGO0rdpzC3Ng0RJcYPXPdzegfdshe1_4pFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های جالب دکتر محمدحسین پور غریب درباره اهمیت ورزش: ورزش اوقات فراغت نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107163" target="_blank">📅 10:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107162">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=C8ZMOk-jkfSrCcstcYuRDVQvz18qPwvdeW5eewEvWd7j6ZSZitR690WiH_3AVIbQcsWS_x3GC21ETt-DmmmBuK75fZXdpFii3iYsMH5QvTpX_5m_ebL7VWghh94kuvXaAd_9pohMVjcE_3A6t_LVdHT0DLUL77NMnWP6IIPXNW0L4kzucm3mEyj9Ej8AYDVtajcMnV4BMnZbf58q3BkZ8W4D3VsQdgBmvIZ06jQ7f7qtzYYwUtyezga5g3zHSWgeUOe7a_Gu31bHLAs3EqvHl9x-qAlfDjj5Cu19XoT1-NsQPGhJDWUjEE1KYUTWE39uOAo2voCgS_Tu5DdoP1E4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=C8ZMOk-jkfSrCcstcYuRDVQvz18qPwvdeW5eewEvWd7j6ZSZitR690WiH_3AVIbQcsWS_x3GC21ETt-DmmmBuK75fZXdpFii3iYsMH5QvTpX_5m_ebL7VWghh94kuvXaAd_9pohMVjcE_3A6t_LVdHT0DLUL77NMnWP6IIPXNW0L4kzucm3mEyj9Ej8AYDVtajcMnV4BMnZbf58q3BkZ8W4D3VsQdgBmvIZ06jQ7f7qtzYYwUtyezga5g3zHSWgeUOe7a_Gu31bHLAs3EqvHl9x-qAlfDjj5Cu19XoT1-NsQPGhJDWUjEE1KYUTWE39uOAo2voCgS_Tu5DdoP1E4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول مهر به روایت تصویر؛ صادقانه ترین مصاحبه مربوط به سال تحصیلی جدید
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107162" target="_blank">📅 10:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107161">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9544f249c.mp4?token=CX5IAZmLeGeKF9EMrH8HxnoVXStZDgQKcLXilRV8xHkq0zJIkQlkQKoSgrd7omHyWgxVy6n_cm3G0UTq1dtVRLTaC5nWREohN00Oyyg9t53OjELvbuVfsp_nnsGiVW75kkPthgaMRrqWXJOo-JQpYw0ZcgytGZFF91R5T3rToZzEx5jJogydR_2CMf-ReqzMXw0i_4giaV58nCGPbIRVElavzD9jUkR_nLSHLN03JCMJFGb7jWnn_b2BlSEd3FR5j3unpyXkRWn505mFFwECgpjfidLdYCXCdgrOcYkpupfih2DEiT4QDQwzNPrijDdgIF3kNBkq_AjfIrphN6ExGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9544f249c.mp4?token=CX5IAZmLeGeKF9EMrH8HxnoVXStZDgQKcLXilRV8xHkq0zJIkQlkQKoSgrd7omHyWgxVy6n_cm3G0UTq1dtVRLTaC5nWREohN00Oyyg9t53OjELvbuVfsp_nnsGiVW75kkPthgaMRrqWXJOo-JQpYw0ZcgytGZFF91R5T3rToZzEx5jJogydR_2CMf-ReqzMXw0i_4giaV58nCGPbIRVElavzD9jUkR_nLSHLN03JCMJFGb7jWnn_b2BlSEd3FR5j3unpyXkRWn505mFFwECgpjfidLdYCXCdgrOcYkpupfih2DEiT4QDQwzNPrijDdgIF3kNBkq_AjfIrphN6ExGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو از یک‌تئاتر با حضور مهرداد صدیقیان و فاطمه مسعودی که حواشی زیادی داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107161" target="_blank">📅 09:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107160">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5567bbdad8.mp4?token=SdDXXZYw0r2GpGaMJcA2ym6e13aWJBgpWQ6Nzyg1hnkXJWu4WQul7kK8oAFPCD1n4Axp6Y2XgPI9fPpklxILeywdGFgWezhpQ4J7NQcz7I0JhFwGylemWC-jHcq7eIFCCM94xj6olbjm2vOL9IYBFHFuL0pitH65cpU0TErH7w0s70I4bQVhEn2Oad-DpVbBRdvUgjqoObEsV7e1YpkURjgdOMTaSkDc98fv2oaBD2ZEI4Y4nw4MpRBjnxMUBk-B8ez-V-cyKl-eFXusrNHC95NdzXI4lhn5KZurx2gJM2tWY7sY63UldLLaW_Tt0jklLp51jJLkkjZpRKQitoaMEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5567bbdad8.mp4?token=SdDXXZYw0r2GpGaMJcA2ym6e13aWJBgpWQ6Nzyg1hnkXJWu4WQul7kK8oAFPCD1n4Axp6Y2XgPI9fPpklxILeywdGFgWezhpQ4J7NQcz7I0JhFwGylemWC-jHcq7eIFCCM94xj6olbjm2vOL9IYBFHFuL0pitH65cpU0TErH7w0s70I4bQVhEn2Oad-DpVbBRdvUgjqoObEsV7e1YpkURjgdOMTaSkDc98fv2oaBD2ZEI4Y4nw4MpRBjnxMUBk-B8ez-V-cyKl-eFXusrNHC95NdzXI4lhn5KZurx2gJM2tWY7sY63UldLLaW_Tt0jklLp51jJLkkjZpRKQitoaMEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«پسر بد» در روز اول مهر الگوی دانش‌آموزان!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107160" target="_blank">📅 09:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107159">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9d6b05a55.mp4?token=rfmtjYp6BnuAMgSIJCyOO8lTtB5MoMsVk19BZC34GHbJ65MDWl6Rr8FVRiF27dZkxP5H8A6gNpAF21CMzpmbo7QQb_0HyHpRQGUp8_QXvWeQmPEF_QEyOfe7puJw9mHQuK3uKE2EYHozALkRC-1HrvAfmw8UvXku_6PvUJKi-7qWxVJG22nA3p0lh7QHRLTtOQ4gJf8UVIXLsQMocOm2Oe6fsIBbB390kOTkObg_YPAZmp-Y3pC6QBzjYnfO8Eq-cCYQR5gJK86q10pWBVzm5FvbHusbQZpRBLPGNITN10cilzcWSe6IR-t4Fcxm_VdkgPfG2m4PfyaxaYMLOcl8tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9d6b05a55.mp4?token=rfmtjYp6BnuAMgSIJCyOO8lTtB5MoMsVk19BZC34GHbJ65MDWl6Rr8FVRiF27dZkxP5H8A6gNpAF21CMzpmbo7QQb_0HyHpRQGUp8_QXvWeQmPEF_QEyOfe7puJw9mHQuK3uKE2EYHozALkRC-1HrvAfmw8UvXku_6PvUJKi-7qWxVJG22nA3p0lh7QHRLTtOQ4gJf8UVIXLsQMocOm2Oe6fsIBbB390kOTkObg_YPAZmp-Y3pC6QBzjYnfO8Eq-cCYQR5gJK86q10pWBVzm5FvbHusbQZpRBLPGNITN10cilzcWSe6IR-t4Fcxm_VdkgPfG2m4PfyaxaYMLOcl8tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
علت‌احتمالی عدم‌دعوت قایدی به تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107159" target="_blank">📅 09:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107158">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKtX1CnBvLG75i3lVVgmubd05odZE6d2Ab2KBYMzvchu_pFwTFiV7ehd8t6EjsI_qxqA_UKTgIpyJR0r3C7-6NxN8g1OJDretzpBquLn6_k9RgohyfDnVDXJNRsNbcSdewGdyBMomK1dgQKopHBvuC41yLJqCeT3uuF8_VLsnukIrRuu6p0tdpBGv3roscLBjn_IAjLgmHpW92poBtY30inkcqqPJK3KDTkphG3V7x9f4urke3WR4mAZQKYvy5cYPDCoR-IbReYXLo3ziprnKbT8Zm9sQnSW1oAeoNuRAYpOF4ejX4lkhr-dUD7bIU_FJyTlUfTLARZrXZcN7NHX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
آخرین پیراهن آدیداس برای آلمان پس از ۷۲ سال
؛ از ژانویه ۲۰۲۶ کمپانی نایک اسپانسر ژرمن‌ها میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107158" target="_blank">📅 08:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107157">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107157" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107157" target="_blank">📅 01:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107156">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NogNAHJ821GyP1Dbve0wQiPpYVoq-lYUDaTbHYaSXhYWznh0tG1shQy8YV4Mo6J_b--ja27dQWbV7nUI-nlLigoW4JF2Iz5pkwTw4DYadOC79MO9vl4_JxB25GcXeYunfEn6Q-KY-NZsc0D4K8ix55bk__9NjCT6r2mQddPirQ013Bes_i_7rVBn8VBJ11YJTlkKwjOgnmChzpN-ig3-W7gC41wXLkoZ2RvLYgLVa1OGjYSYyNKfwKPakY-geBU2lQAvsfGVLHqZqdq8sv9Ddf2oByV9tjvp7eYxO0RrhZQPH2nR8LYkSTgg3yN9g8o-ZtCfeqlDmQyAwMN5UTG2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107156" target="_blank">📅 01:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107155">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E018_kEzcgc2HGTFqX1TxUxbnfEjCCOwoIw9uzyiqI7mmMPEwlvUF7HDyDeGO3iZdJKeGHKtOE2dGNbEoPtROYKbQks7CQgph7PgNqRLw359-kX_SHpyAkkdR94HjsrBBha-zQZlPvIM6rSCGVRemM_sNDI46a9GEC-47ABCiwizduN87OjgflIJij-W3qts34mhnTeCLm6WccQd-8mTJIi66h5VXL5d2MLoshhwOpID7-IwAOYIPSzN2_t0zuuCozfThlWDyerxga1iXSfgVBmLqJc6leOD_bQ7tYh3WSxCng4WkDl_ZUNDd7N9CHbmHLpEiKQijTvUW5R6BEXJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ژوآئو فلیکس: درسته امباپه و کین فصل فوتبالی خوبی رو داشتن ولی به نظرم لامین یامال خود فوتباله و کسیه که مستحق دریافت توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107155" target="_blank">📅 01:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107154">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
دیدار استقلال و تراکتور بجای ۱۶ مهر قرار است روز ۱۵ مهر برگزار شود. این اتفاق احتمالا بزودی از سوی سازمان‌لیگ‌ اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107154" target="_blank">📅 00:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107153">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5h59ca4B6M9LRgnlNnGtRfjdhAmv9VjlOYCUZTP7XNYYVXzLOtKWtCf15WqJXh8VVS1ZJfdY2bwhHPfd0YIADcJbbaFZ-K6XtFFdOUhOruNYykXClcBbwrDlFcZ1DYRPoqWy78iSTXU7NqD-zsu6Gijb6JK1c8TFKoVimWQBpt7PQ8FSJtk594eT6ovql_jG2QbDYt2abBJL2V6eZZk4-N_xHALBNJbSjf-PoGQ6Pdo9jHul41O9TNrELMmVEVY76jD-VanKKDNNvEjxmgY8HBjBvPZiCbOINkhK2GqdDPTFaQjDmkn2gvHSItMzhtoFPhPUezF2ORB2rgJjiUczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
دیدیه‌اندونگ بازیکن سابق استقلال در لیست خرید جواد نکونام برای تقویت تراکتور قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107153" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107152">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=iGkO1tWCJ9Xh3NMwMdsHR8PvsknFh3rkhb1x4_ProVDhFfC5FLIF6JC06FXo2QOj2WDDbSCmLtHDcHZYyOgWIaYcbHLixLgizaUhAI_bP6aDND2eQyndJXgEGkQPnzUG8KWvCieEn42ceduw7wx8eQ_QK9LhHPrqBZX2gSWGKUHMEMrQb_Vpa0ktsU7edbvo-3oEaA7cOv9qrZe3wGukOoO7rLuat5DPYMe6NVb33b6ZjKcfnTKp98G2bU_Z_TEKKEdeKM0IB05yZZIJWa7O6scO-o8lguNSV5-axKmdCYPCmozkV_MTlQ9sB5FSlpRUBt4dcBFa6dQo32p8ZxT88w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=iGkO1tWCJ9Xh3NMwMdsHR8PvsknFh3rkhb1x4_ProVDhFfC5FLIF6JC06FXo2QOj2WDDbSCmLtHDcHZYyOgWIaYcbHLixLgizaUhAI_bP6aDND2eQyndJXgEGkQPnzUG8KWvCieEn42ceduw7wx8eQ_QK9LhHPrqBZX2gSWGKUHMEMrQb_Vpa0ktsU7edbvo-3oEaA7cOv9qrZe3wGukOoO7rLuat5DPYMe6NVb33b6ZjKcfnTKp98G2bU_Z_TEKKEdeKM0IB05yZZIJWa7O6scO-o8lguNSV5-axKmdCYPCmozkV_MTlQ9sB5FSlpRUBt4dcBFa6dQo32p8ZxT88w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسپلور گردی احمدالشرع رئیس دولت سوریه وسط سخنرانی‌ها در سازمان‌ملل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/107152" target="_blank">📅 22:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107151">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCLorjOBuC2RCaE9as2kZNfSytslpWyyC-X_r8WnKKd6x9FABhEyJ3eRt14qITW20czSTD4a_NecGtG318VKdwXcWpfGAGWT26bMb2KLdIDtQ8RpaRrgnOYlnav40VJssD1J0YgPOnbX-DX3GIJPMTQLxt80cRnHbw3_fuXVLH7f28tx4zTN4zRGBpqgXeo6m7NxYnD5RiMzSIpJERhx-Ele5gcE4VUKlZyviK9jfDuzKgajm7NZzD4k9AwpQOn0QvaEr-czllNTlOZHEWjVgcRFtpCgoUa0wylyY7qh_CY1yT_APiyc9LdVZ4eZyW5eIWMLdI-_flX2Rh_tIW9Y8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
آخرین بخش صحبت رونالدو در کنفرانس خبری خطاب به رسانه‌ها:
بعضی رسانه‌ها عاشق حمله کردن به من هستن؛ اونا سال‌هاست که سعی دارن من رو از پا در بیارن (بکشن)، اما این کار هرگز روی من جواب نمی‌ده. شاید با یک شات‌گان جواب بده، اما حتی در اون صورت هم من می‌تونم از گلوله جاخالی بدم.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/107151" target="_blank">📅 21:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107150">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=r5bgt-jnzfdjT3q9TRSE70pclNSym_xtgX-Fy5eYmrokPzWRPvYIEQFVTKW9FfKPn7lRNAtAKC51k-hJKuOk5LMUSntA9Q09xu1uEqm6qmR4ueqnZ-t-cZ6wiBN5skj2KT1JY2ugrdS0hef5Fq2bnrapPPXMcqw2oRM88Msx15IKg16PE9lXakc1fQk_DvW6WHFMTS0nyl5h62r_ckseO_vRC3BYfTWdclAzFPLahXpvCVBQtZEosBBK8nWUDLRQvrxubODsAiAiu5rgmeZgb4FdbPHAoaFtRMFClfrUoQ2pPq-Fjr2gwyZMTVNDq562ZED_q3vBFULDPtZo87cWow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=r5bgt-jnzfdjT3q9TRSE70pclNSym_xtgX-Fy5eYmrokPzWRPvYIEQFVTKW9FfKPn7lRNAtAKC51k-hJKuOk5LMUSntA9Q09xu1uEqm6qmR4ueqnZ-t-cZ6wiBN5skj2KT1JY2ugrdS0hef5Fq2bnrapPPXMcqw2oRM88Msx15IKg16PE9lXakc1fQk_DvW6WHFMTS0nyl5h62r_ckseO_vRC3BYfTWdclAzFPLahXpvCVBQtZEosBBK8nWUDLRQvrxubODsAiAiu5rgmeZgb4FdbPHAoaFtRMFClfrUoQ2pPq-Fjr2gwyZMTVNDq562ZED_q3vBFULDPtZo87cWow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
🇮🇷
کنعانی در دربی سامان فلاح رو تهدید کرده بود، حالا خودش به تیم ملی دعوت نشده است: «نمی‌ذارم پاتو بذاری تیم ملی!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/107150" target="_blank">📅 21:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107149">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLqcU71EiNRuLM3WlS5du3FoCFx260hu7AjQLBwnmJGH0ZRW6q2frgFI7BqCL54jT7rMCOecQ2--nRASBkiHCZcv2yD4rPC-2EPH23yG9YBTTZgplKxdwf5zzS5iSU1IrNLyWRHPZoALZKt3v_5wN5A-Q6v1STuZi_S3PxCCA5IwZYKrkwBQRAbZpz9yZsMnA_fwmQrQks7MS8m-gDLrZFTItUuzPcF12_Og4hr5Ev_ckV0QiPMz03WL1pNxUiwrqNUhiANf46HgTuLJJrEiAK5tTFAyZknA0gYUQjaMgbXsz_AUAZS6R-7Z6CGpdoKidBhhXc84gDgxh6SWv11jHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
اپدیت جدید تلگرام از میانگین زمان سین زدن و جواب دادن به پیام پیوی ها !
اینجوریه که مثلا وقتی وارد پروفایل یک شخص میشید اون قسمت بالای  شمارش میزنه بطور میانگین، چقدر سریع به پیام‌ها پاسخ میده مثلا 5 دقیقه، 2 ساعت یا 3 روز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107149" target="_blank">📅 20:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107148">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=mJKU5IKjJOnDl7Knnw9V2ivHSzVEOYxKpME7LJIVH3mjTcrHmY7oexhco9RoJqPP3DoxZBuGCcjW3qVC2y7t42BYh4gXfNUndsfqq77NWNkCVC7IW9byZ_9HPsxoYvoQ3K1RmWWCq5sNYNInYIzBUKtEyetl-Fey7M-9g69DOrNxyM0thPg1dItpauVbxaC_Fe-8j1lno57POy9URY53A-W-tTwXlmzUBLAcJF-GotHZeCjYgpygWsIGx51e9hFaS_tH86KZY5Szi0xj0sbchbjyEbaNjb6FPLbFcHjLxSdw5fTCGqV4jXWBel8igNBuDarB1xZL2Yu7vOviMhS-SkXCXmR4wJhH7OucwX_N1CciEF7LqjFQDhquVEfXBbWnOXxoMgbvzxgz_--KPu1MxA_yI1JBizMUCIchYQW9Eml4gbYcL0pTePV4mi_mDAGHLePgCH0vLs5NtNxf3yyL06vmzfaIW8gRsN41gIcZUVUWQlRmjog9N_uCzQOULHeqQhtdPC9DmZkCSurkRE6fD8UYhc3ksvk_oRRCYAp73LesK_2OFyXvEbI_aM_vHNmCm9gbVoyOsCM_xfv4VcgUHp5dg1G0WoNUf1x7rR7ELzYUJ1VLT9a4z5R1cfvCq_LRynjhJPP_K86KPTVEmxITHtEBQv5Snh2N3eLLjc5DoR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=mJKU5IKjJOnDl7Knnw9V2ivHSzVEOYxKpME7LJIVH3mjTcrHmY7oexhco9RoJqPP3DoxZBuGCcjW3qVC2y7t42BYh4gXfNUndsfqq77NWNkCVC7IW9byZ_9HPsxoYvoQ3K1RmWWCq5sNYNInYIzBUKtEyetl-Fey7M-9g69DOrNxyM0thPg1dItpauVbxaC_Fe-8j1lno57POy9URY53A-W-tTwXlmzUBLAcJF-GotHZeCjYgpygWsIGx51e9hFaS_tH86KZY5Szi0xj0sbchbjyEbaNjb6FPLbFcHjLxSdw5fTCGqV4jXWBel8igNBuDarB1xZL2Yu7vOviMhS-SkXCXmR4wJhH7OucwX_N1CciEF7LqjFQDhquVEfXBbWnOXxoMgbvzxgz_--KPu1MxA_yI1JBizMUCIchYQW9Eml4gbYcL0pTePV4mi_mDAGHLePgCH0vLs5NtNxf3yyL06vmzfaIW8gRsN41gIcZUVUWQlRmjog9N_uCzQOULHeqQhtdPC9DmZkCSurkRE6fD8UYhc3ksvk_oRRCYAp73LesK_2OFyXvEbI_aM_vHNmCm9gbVoyOsCM_xfv4VcgUHp5dg1G0WoNUf1x7rR7ELzYUJ1VLT9a4z5R1cfvCq_LRynjhJPP_K86KPTVEmxITHtEBQv5Snh2N3eLLjc5DoR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
چهار عمل کاربردی در نسل‌جدید گوشی‌های سامسونگ که حسابی به‌دردتون میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107148" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107147">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=pJtvtyLQTp2ip1nRKZiRjFDw1N6BD_AuPcYUrQI867C13e5YomgJ1M2qA1BlhCxPig_muVvugkEo0L4j6CbEem8TQCSkKs2yaXtCK34-nAM7Gz2h0VlksUAislhHOwilkfrx39HA7GvbaG2pc_FV5K3T3ZkA-a4zUchPIu_uS9c2aB-lqZSrvl3z84dWh4LiRusttMYC3bZtvhy42Wof0nlB4Zl9fgDPz15vZPgvUFKK7lcEc9QN7G937Ce0Acy_lO1aA9fWqVEdCTADdq86NXSyWNw3MYDvMZZNbZKCy2jCVnvCgPO6Fs_1bKr-RWVvsWZ2Ufd9B-7ij8w6J3jNDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=pJtvtyLQTp2ip1nRKZiRjFDw1N6BD_AuPcYUrQI867C13e5YomgJ1M2qA1BlhCxPig_muVvugkEo0L4j6CbEem8TQCSkKs2yaXtCK34-nAM7Gz2h0VlksUAislhHOwilkfrx39HA7GvbaG2pc_FV5K3T3ZkA-a4zUchPIu_uS9c2aB-lqZSrvl3z84dWh4LiRusttMYC3bZtvhy42Wof0nlB4Zl9fgDPz15vZPgvUFKK7lcEc9QN7G937Ce0Acy_lO1aA9fWqVEdCTADdq86NXSyWNw3MYDvMZZNbZKCy2jCVnvCgPO6Fs_1bKr-RWVvsWZ2Ufd9B-7ij8w6J3jNDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107147" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107146">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر  وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[لینک کانال] https://t.me/+fyrt-rnxFjNjMmQ0…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107146" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107145">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuXu8EjO90d0evEc2B__ZoSGsDwr3A4gXjZIq9MalP3iFrCB4HwXiUeGu24blxxLvL9hbD1g7l8wrDc35yqIub1V7Xirs0vvOF7UwsvFxQWtodE-djMNYF3xT4h3s8DjrD6ltw-LE8aIsHmU5WDjOmfz_CAgrJOAxVGsvzyg0M8hDRj7jEVtJcHHbY-iYbj7l4GF0brnO9bwV1wWj1Do83Cuf1RotvfIoVOnCUZP6cqGs-VJY00MCIPWMk6d7M1txK91pGXR4VtybjyWPL3NUtsqm4zOqqhgPZ56jdJvVFS3_aA9G5QD7NknUMD43xtu_LAZFfMW5jIAd35ujTYsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر
وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[
لینک کانال]
https://t.me/+fyrt-rnxFjNjMmQ0
[
لینک گروه
]
https://t.me/+jpSLBx8PcgBlMWI0
#TipsterPersian
#سود_تضمینی
#شرط_بندی_فوتبال
»</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107145" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107144">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=Q4DDrTyUqdfZ6v33F9vgIzcaXuAadN5D7S1aA5kr_Sz6SFbP7fx1ChawGD1VW6ckY0BFaKxk6d_IhTurPTVZM6arIsQ96SNoikBOFTZfWRggP94-q3XDJO05lTp_uaQs8KN0V04RSOetORJ7qMp05CotRdsg0IlApCfFtVSpaA0uN26bQIr8_fOjcT9BruSXAfgL-hX4NPA3Lyt6NExXS6OxC1Ag1DBVKFKUdB__OOwzE41iJXipBtqlOnIWkEKK6rkg69O8tHfL6_tKOEqUQywJP_qYnbrm0xWzTjSrDrmVE2YMbrzXY4ZRkQXEjm4smEq9aZQFFT5fNjxjL_tfVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=Q4DDrTyUqdfZ6v33F9vgIzcaXuAadN5D7S1aA5kr_Sz6SFbP7fx1ChawGD1VW6ckY0BFaKxk6d_IhTurPTVZM6arIsQ96SNoikBOFTZfWRggP94-q3XDJO05lTp_uaQs8KN0V04RSOetORJ7qMp05CotRdsg0IlApCfFtVSpaA0uN26bQIr8_fOjcT9BruSXAfgL-hX4NPA3Lyt6NExXS6OxC1Ag1DBVKFKUdB__OOwzE41iJXipBtqlOnIWkEKK6rkg69O8tHfL6_tKOEqUQywJP_qYnbrm0xWzTjSrDrmVE2YMbrzXY4ZRkQXEjm4smEq9aZQFFT5fNjxjL_tfVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107144" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107143">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
رپ‌خونی سمی ابوطالب برای تیزر برنامه جدیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107143" target="_blank">📅 20:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107142">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=VLysO8NHAzMKhKj4qGt-L2JRDjGAY9meNQwnX_4RLmwMOkzyl8eTAthizkWGYzNYI8ef9Wjwc75kzrRNiltYDQEBi03-tCdsua6B0R9pZd6cyar__erxpSvfwdCVh3RTCO673N5Bzd0wawI9WgRM-C1MihhchXATB2Ef_jvKOGbOZawWWkrJ4lJO0I_zXZrMkDvsPeMDq_1ddln7WuvV2B2Fmcw7i8Sm4JnkpTC5J2YEMt3XzN_P58zV5nzkaX8h2foOFZRB4ObMw1ot8nyjdpKycJ7wDU_8hqURO9psG2AYfWLAgFRY0rA6yBfw0xRK9Rvk2uXSR5F4oeqv-PCMDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=VLysO8NHAzMKhKj4qGt-L2JRDjGAY9meNQwnX_4RLmwMOkzyl8eTAthizkWGYzNYI8ef9Wjwc75kzrRNiltYDQEBi03-tCdsua6B0R9pZd6cyar__erxpSvfwdCVh3RTCO673N5Bzd0wawI9WgRM-C1MihhchXATB2Ef_jvKOGbOZawWWkrJ4lJO0I_zXZrMkDvsPeMDq_1ddln7WuvV2B2Fmcw7i8Sm4JnkpTC5J2YEMt3XzN_P58zV5nzkaX8h2foOFZRB4ObMw1ot8nyjdpKycJ7wDU_8hqURO9psG2AYfWLAgFRY0rA6yBfw0xRK9Rvk2uXSR5F4oeqv-PCMDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پیمان طالبی مجری شبکه سه به شکست چهار گله تیم فوتبال امید از کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107142" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107141">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwrbTu3a8TDgHuRq-jSBHIplltiJBuXtMCf4SPd_LjaTizs2PcrppX1U3RZhMerF-_dFkndoG8PNpOPS6R3LB720Eo3sY5ppw_UR8cgEhnFZlVvjq4B2JSPcTjLZwlP9M0VQr1Y2VMyAA2z5sn5B3SrQKjcAeALl5gfeTARQVbQTYWjcpKr1lyOpfxp1CR4D-NeSPYHvQYp548aRG-T34anoyBhobMGTpcfdiKrsfjA5dU_8P4YpLm9-G3l_Fjq706Fh9i9FRE0CydyUgJw1zg0z91AxcIj7OVZFzivqcVgio_mDE29yGhIMq2POatoPr8k57EJhWyC23bq9lIGnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
استوری‌جالب زبیر‌نیک‌نفس بازیکن سابق استقلال به شکست ایران مقابل کره‌شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107141" target="_blank">📅 19:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107140">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRQUCbrP_FcPsHNEOoZjGHvWuIaPoPPqJT6TSnb2IPfqS87n61583d59ibGX0IyqnPApACIAcOsPs0tc_7-_DVYMPKIP44gqDnB1x4iIJthD1O7URq_PdEUzeLrvlizdSbHuiTwhogrw5BWLUfbLIpTuuWsI21QUAnthxckE2P7vndzcUeJ-V4Rsc7cZaX5vZpt5SeVGk-OHRkONruXY8YOXrZ6ft6o7wJLns53nFNj33PXnlz1i93amJyvjBeuv72JintB2C5Ovycw153A8EYR7Tslu21gPLC15LgtMWT3njPP0CXqKvSxxe3JCN6N1WJIyMFazKkJkkC8V-aTQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
بهترین استارت یک‌فصل بازیکنان بارسلونا در تاریخ این تیم با صدرنشینی اسطوره ابدی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107140" target="_blank">📅 19:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107139">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
آنالیز جذاب از بازی‌هفته‌قبل برایتون و آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107139" target="_blank">📅 18:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107138">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=my6rgPcZcKGsSxW4Kj54E9uAr8feZfmNyPWyxWtvq0BmaA6W5VD_5SlVJVExrvxKut_99EK1uGHejHpVIr7q_0W_W49R4evurvVEMF54thLIKMPXwAqdlIh-KuQndO_cfpAXgGWVpevR_il1mMyKW9oBjo9DDpvcdxtsLQMAGliy4_2c_GldjVurwp4UU2c8KPt6E8kbFosys85BeLOA8D77kJOeO77XXziL-YK4tY1KSPelnT7pcx7GdNT_Oya9Mz91I87sPnxhWpi9mua0rsxZFd0ZT4uKANmPxFnYKGEPV5qOFrQDnLkJmIJdsQtKB4fUawGA574MXDDnF6fO3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=my6rgPcZcKGsSxW4Kj54E9uAr8feZfmNyPWyxWtvq0BmaA6W5VD_5SlVJVExrvxKut_99EK1uGHejHpVIr7q_0W_W49R4evurvVEMF54thLIKMPXwAqdlIh-KuQndO_cfpAXgGWVpevR_il1mMyKW9oBjo9DDpvcdxtsLQMAGliy4_2c_GldjVurwp4UU2c8KPt6E8kbFosys85BeLOA8D77kJOeO77XXziL-YK4tY1KSPelnT7pcx7GdNT_Oya9Mz91I87sPnxhWpi9mua0rsxZFd0ZT4uKANmPxFnYKGEPV5qOFrQDnLkJmIJdsQtKB4fUawGA574MXDDnF6fO3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
تشویق مسعود پزشکیان توسط عباس عراقچی و... پس از پایان سخنرانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107138" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107137">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
⭕️
🇮🇷
پزشکیان: انرژی هسته‌ای حق مسلم ماست و برای درمان و کشاورزی نیاز داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107137" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107136">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=urfr6_TA4F1a8PPSpsznNNmsbBsmdPK3IlWZx8QrIDajrZngOd3rr4r8_ReV8wvQSqFnLcvInYTYngVKsVWjK0fzECKEetIFIZGZZUqP3XYWLmnQe4sziD0ag8WPI2eJrEn53UIPAFkiZsb1SgTh_3AeCgMenMdVdHUhr1z3LQIpzB0VmN4VC2iHpoGcEPWPIJc7TQfBiEoLSqBRnvR4Ex8BhmchbhCIRZYJqZzAf-LrcVSVa5XMBRwzHKC4guloUv6eiGHptoD8jcwY26Ap57fTRAAz27D9gk5U3BtwhBEaGH3tO8Oh3quBztwX9lkW-amdgPwkSDwnWflYkLn2apEGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=urfr6_TA4F1a8PPSpsznNNmsbBsmdPK3IlWZx8QrIDajrZngOd3rr4r8_ReV8wvQSqFnLcvInYTYngVKsVWjK0fzECKEetIFIZGZZUqP3XYWLmnQe4sziD0ag8WPI2eJrEn53UIPAFkiZsb1SgTh_3AeCgMenMdVdHUhr1z3LQIpzB0VmN4VC2iHpoGcEPWPIJc7TQfBiEoLSqBRnvR4Ex8BhmchbhCIRZYJqZzAf-LrcVSVa5XMBRwzHKC4guloUv6eiGHptoD8jcwY26Ap57fTRAAz27D9gk5U3BtwhBEaGH3tO8Oh3quBztwX9lkW-amdgPwkSDwnWflYkLn2apEGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
‼️
پزشکیان: اسرائیل هر محله‌ای را در هر شهری و در هر استانی هدف قرار می‌دهد و عملیات ترور انجام می‌دهد، درست مانند گروه‌های تروریستی واقعی. در غزه، بیش از 80 هزار غیرنظامی بی‌گناه به طرز وحشیانه‌ای کشته شده‌اند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107136" target="_blank">📅 17:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107135">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=T0Tw6QmbBqDmO7_P8qYstP4fOJuoClY5Kq6b9lxuLuEKbFpXjTCQN_R9h6G3chP8m3rRImEbkOlOckS3pTeU-LszVpEkGGZbr10fMps-K-eA2jh3UdVx8saw47USOF6q4sfbMfsQUXwi0zXOTnNOyUX3_WgeQvpvdCpDELYCtbpikgnYadH8Ri7Zwd6POy2eMsCm5yGurIDEVOKlF4lx36hWuQmIpbcV3CMQ3eLemrdQ3YLQ6kKAV2NuBsSNfsjj7jdV0EezfXNHIDQ1tgixcGNTEQo4wMuWDwgSh0cYK_VsRd_T6j3rPeLikXNpO76KmgLidy3M5q4Tm3Ab48PCZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=T0Tw6QmbBqDmO7_P8qYstP4fOJuoClY5Kq6b9lxuLuEKbFpXjTCQN_R9h6G3chP8m3rRImEbkOlOckS3pTeU-LszVpEkGGZbr10fMps-K-eA2jh3UdVx8saw47USOF6q4sfbMfsQUXwi0zXOTnNOyUX3_WgeQvpvdCpDELYCtbpikgnYadH8Ri7Zwd6POy2eMsCm5yGurIDEVOKlF4lx36hWuQmIpbcV3CMQ3eLemrdQ3YLQ6kKAV2NuBsSNfsjj7jdV0EezfXNHIDQ1tgixcGNTEQo4wMuWDwgSh0cYK_VsRd_T6j3rPeLikXNpO76KmgLidy3M5q4Tm3Ab48PCZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
خروج هیئت کشور آمریکا حین سخنرانی پزشکیان در سازمان‌ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107135" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107134">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=AUJjdvQ2tX9dkow1jFJXPgJyg_8DvJrhBg66YVePUhtTgmHQqHpaBy4NWOsU8WA8ihQeaYVKXNqulKHZKNf-vPB60SPzZcR9YEK--O3hXSVwqy7jWj83fBvEN3IDhIq-RXKq5S22sfcr1Cl0AV43tUjnUo7L0qpgzqMtNZLcNQCMrx1gVvBAolKm92n1tp11DXBbLo2uYlYpiaWedRglVGQAatY38xuHk6_iFRufIlz9_AbuRCcfDEIFMN_V9-4dxWOUMiLU9kDBdxd418aAYhFv64vA7sN578guINizmCkjvz_Fe1rQj2ulHb2sDvnNhPN2JI4lVokwCxeruJdTjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=AUJjdvQ2tX9dkow1jFJXPgJyg_8DvJrhBg66YVePUhtTgmHQqHpaBy4NWOsU8WA8ihQeaYVKXNqulKHZKNf-vPB60SPzZcR9YEK--O3hXSVwqy7jWj83fBvEN3IDhIq-RXKq5S22sfcr1Cl0AV43tUjnUo7L0qpgzqMtNZLcNQCMrx1gVvBAolKm92n1tp11DXBbLo2uYlYpiaWedRglVGQAatY38xuHk6_iFRufIlz9_AbuRCcfDEIFMN_V9-4dxWOUMiLU9kDBdxd418aAYhFv64vA7sN578guINizmCkjvz_Fe1rQj2ulHb2sDvnNhPN2JI4lVokwCxeruJdTjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پزشکیان: این بچه‌هارو می‌بینید؟ اینارو بمباران کردند و کشتند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107134" target="_blank">📅 17:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107133">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=Efv2clU7b6LcxsEQoIkQNMbW3JatbO5wuQxt7s0Ug0Zh4gcR4C9-fsqbb_NSAWkqFWmDIY6xjTd0RbF_Ge5KbVxPZ4UR7dL3Yd05uDrT2TKGLMpaPXwHX0jKGk5uBJgm-9SGc5OeFnLflYbxVp8tUN1ySVBOBGuKaV4Vqc9qgJ8l0h9Ffgx_K5QkAIkW5oE7Xa6B0eecIRSCqLasA8dfvltqTCE-sbRib0MWPsRAxvoE79eNAvdw86Fx0ZsjuIPrmT3JoT7ue6IWVLwPvDe-44Jr9iGhgb2QCYLvKiVLr7_Zd8bjmh7KqDpZpBnTUsQBCoq0uAxykhv_qSD0lL5RGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=Efv2clU7b6LcxsEQoIkQNMbW3JatbO5wuQxt7s0Ug0Zh4gcR4C9-fsqbb_NSAWkqFWmDIY6xjTd0RbF_Ge5KbVxPZ4UR7dL3Yd05uDrT2TKGLMpaPXwHX0jKGk5uBJgm-9SGc5OeFnLflYbxVp8tUN1ySVBOBGuKaV4Vqc9qgJ8l0h9Ffgx_K5QkAIkW5oE7Xa6B0eecIRSCqLasA8dfvltqTCE-sbRib0MWPsRAxvoE79eNAvdw86Fx0ZsjuIPrmT3JoT7ue6IWVLwPvDe-44Jr9iGhgb2QCYLvKiVLr7_Zd8bjmh7KqDpZpBnTUsQBCoq0uAxykhv_qSD0lL5RGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نشان دادن تصویر خامنه‌ای توسط پزشکیان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107133" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107132">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHpaU6B_ax2T90D84rZKkNo03Y6mNUrrF6TtmLuaPTO5hgW_-QHP-J-f2iEtnOLF1RxBefEZEoIG8qv-ybJyCEQwINRfQrmMvDtII_1QwrtF0zB0hJptLPEyiHtIxQOEJRQ1U_is_sHedTu-ZTcIeQk4x0R_--flUGVOEC2CqKoYpsQI3LqSnz-NNjNxmMM0r5bqNCtRkbUTGRgh364d17u8MvCxINgfeQHLCYLhz_GrR-3hb6HnV5nSwfWrIOljKi247soWmXqBM4IUJ9jm99N5jjQWTGzqU_RdYRZlyXFrCz-ofxWEpTYF8qKrSc2Heb0euom5G1JwQSg0Xfo6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مسعود پزشکیان در مقر سازمان ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107132" target="_blank">📅 17:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107131">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=iHbAFPPMMoh1K9p4oJ1WQUTXE3LzVv0Lqhe8CJ1TlsEwdjy9y6lMviv7Dp19P2zS7o0Qnhct_4q1XhXvth5xs42sHISYLbJULaQJBdFLavX2xInUq3-yh6-2j8bn33bwl2d6ZeMZzKX3lk1NSajYiI9MZsySzPWQnGFUN_DJcF2RicHQS6UKxPI1S_rl2JsM3Ly1qEw1HiASWNFVnF3xGbN0aMqRK82Pu3guik_Mz38puqZlUEPN4UkPqe947IorUEkEK562Oiz7-DzKNqUzGjXEeAsNQ5iTm7FJmNEfA15z_4leWsslqm3PGmpHroNXc4LZfIdDSqdSPmRtaB6c3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=iHbAFPPMMoh1K9p4oJ1WQUTXE3LzVv0Lqhe8CJ1TlsEwdjy9y6lMviv7Dp19P2zS7o0Qnhct_4q1XhXvth5xs42sHISYLbJULaQJBdFLavX2xInUq3-yh6-2j8bn33bwl2d6ZeMZzKX3lk1NSajYiI9MZsySzPWQnGFUN_DJcF2RicHQS6UKxPI1S_rl2JsM3Ly1qEw1HiASWNFVnF3xGbN0aMqRK82Pu3guik_Mz38puqZlUEPN4UkPqe947IorUEkEK562Oiz7-DzKNqUzGjXEeAsNQ5iTm7FJmNEfA15z_4leWsslqm3PGmpHroNXc4LZfIdDSqdSPmRtaB6c3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید عارف‌غلامی مدافع سابق استقلال:
شجاع تر از آنچه ميپنداريم، كمي دورتر برانيد ، زني درحال فتح ترس هايش است ، ١ مهر به ياد تمام دانش آموزان و دانشجوياني كه ميتوانستند در بين ما باشند اما نيستند ، روحشان شاد يادشان گرامي
🖤
🥀
💔
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107131" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107130">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107130" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107130" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107129">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQeSeVNeZQjCnenbdMN5aRP-AyLWl73egsfeN0vWxJA81RTyC64DwQu7tMrAvVm_aFDR0L_HCizUTja22tqgcQnwT-1vYgl1xBasD3nuJ9Fkx5q-NNqOlh1lCPtaov1vg8OWiXvew9uYsKhbGbw05xUfrlT3KqAJ2Kax8kx5k707yqhMDf9cjrLGl8buTqgO_3MJVs-tf7OkyNx1JFMZXuHxKygPG8Ugo_x429lzPsO8ZU1X_mhiVi-slsxpXjRoyuMapKDt7xaQVFJL0BcQ4Ydc7VhxoKAvsw0Ke-eFdVzA3AW96IWmH9sjGG_VpAu7Sq7JnVY0WoVf9rLOQQ8RbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107129" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107128">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaLaWy_fwgsyZDjE3Ne8jy-WgqgsJdbYIGJgdGBF9-g4WJrBXUa1dUitvd16bqjWwCX2bq3Nnu4JiiDYfqFW67YuvX9XMYUQeQywt8f1ClYKlhwzsgKyjkBkefCkoFRdLwsEIFzfwU-pqcSeYeEATsWbq4Nkip6E7HNVZ4CV6CcOSlCH0L1fMQF6gqQFYXbDn5DPdwV4FKcrt8-L8DzV5wCgBYUPr1l6-WqzgsMDgemrhDL4ek0FEcu26mQDfTtJdi9BXL8I3nsexnoy8UM_xcVpISKU6JUCeXPzxvf_Yb8xND5Y2qom3g5MAy0Db7mxvji4FISOoFmlkeGuXe6m5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اسطوره محسن‌رضایی: به لطف تلاش‌های ترامپ، ایران اکنون قدرت چهارم جهان است و بزودی با تلاش‌های خود به قدرت اول تبدیل می‌شویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107128" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107127">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX7BqwYBI6Ptx3KWqRe9g-ThIHP17mn_uEWNsasSjLSwD6gAjXKnab8g-AaFj2fi08Es2uFdAt-c2zw_uzc8fgE6iydZ0STlxGct7aItZS5VKopCKu4l5AROqG9TppYlHd0JWCbxWsrH1su4955QlYV35Hn7jU8hpW9C-wMyxP4n1Op_YkFIVcxnULbkSQ4Kpui2a5iK1091219s58d0YlOY0soeP5uzowUGTxpqzjNnqxD8J0TiMQSBVex0vLlWtmyj31dWi7VCcuMj1hT7JKP7s7471OWhuZB1Vq3qOw8jsAo-8ueoZDwd8Ke9kAnef9U0ENPv20bgPUvwSFRpbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
کنایه‌های خداداد عزیزی به فدراسیون فوتبال پس از حذف تیم‌ملی امید از مسابقات ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107127" target="_blank">📅 16:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107126">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_aZeLcPCIK1ZGpjA7Og0XSTgEU7a9p9ibgHRrJPvVp6lrEI-I7yKopaM7ih3erLfCsgSyoMevr7uma2WugtLwZ-m4wBjjXoM_ePwzkxTjx7OjYIyVJySWWrHkh5HlhSdYp4z8CPmZl-hATNxRox7zugQwXH4LbGMOUaFhsneE1J_OZ5GyNqOwyzpm15EwcjG9fxV4EOOcz33XzVapA5mKpSOHmqybk7DH0KtQYdp5ErKQ5KPDS7_yRdwZQ2YQOvQKzdnpfoOrd-gvBDX78Zhyrejk5f5LyNsdyrKzzBHsKX5Yr1CBZByF-vdTVYvJFvAsXKlZG3acDTUzsZXJv20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🙂
در فیفادی فعلی و از اسکواد بارسلونا، فقط ۵ بازیکن برای تمرینات در دسترس فلیک هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107126" target="_blank">📅 16:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107125">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=KbaEH1FIUfi5AmqlLIBtLEbO5IAmZWE2fcStMLoVuIMfbwDKvRbKgAAng8bQzUpg_mTm5gqXXJY3WMCLW1q3UYJr0WrPsORwv0dylKYNEwNZjwFyyLvlZhDZ3aDKXifltTCb1h-TUQ6soLm2EOIRUF6-Iku-29LuIfuSxF-3e6rXTGeDV3YlyrfDsCLi2TwIM0BV4nvybMTJuCnBrBb4YLb9RlHjh7RFYEPe9OQgSYRixrnQA7gi1x2D7RHMy9JN5ZMKhsMFFztehYHpRJmXnBgJlL3AW6SV4V6IeN0x1nZ--c6aL7q5gbYmJ_1AKEQR_OWUUcZc77QLD6dG9yFMESrRfu-tiH5aPf97l1anarxkxVtgY5anMu1h6hBNfAhDaE6ROxSwgZhOGskoPbgQAIfp0WrL3R1uwFMRCJgM08_7SPUp5J4FMyETWX_jE0MiRgLodQCVTOz79URSJOI7G6VHjG7pS7Ds8bnSWOS8hsxnhaNNrbmjtwVPnDxWBemceKnAWdA-Ranh7z6UvYVyidPK9YZDjS39OB5kYePZCId909P8q6FJj0F3K5RnlpvIZSB_q4CewFWtQPJpXAIfgubqUxAQQFtZuvlephrEMAxtWRrZdO4IPRsatFeo0ZDoLWRQx4wxSDOnfNhy2pOW4TxSgT15ZzNh6Ds0r1rkG40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=KbaEH1FIUfi5AmqlLIBtLEbO5IAmZWE2fcStMLoVuIMfbwDKvRbKgAAng8bQzUpg_mTm5gqXXJY3WMCLW1q3UYJr0WrPsORwv0dylKYNEwNZjwFyyLvlZhDZ3aDKXifltTCb1h-TUQ6soLm2EOIRUF6-Iku-29LuIfuSxF-3e6rXTGeDV3YlyrfDsCLi2TwIM0BV4nvybMTJuCnBrBb4YLb9RlHjh7RFYEPe9OQgSYRixrnQA7gi1x2D7RHMy9JN5ZMKhsMFFztehYHpRJmXnBgJlL3AW6SV4V6IeN0x1nZ--c6aL7q5gbYmJ_1AKEQR_OWUUcZc77QLD6dG9yFMESrRfu-tiH5aPf97l1anarxkxVtgY5anMu1h6hBNfAhDaE6ROxSwgZhOGskoPbgQAIfp0WrL3R1uwFMRCJgM08_7SPUp5J4FMyETWX_jE0MiRgLodQCVTOz79URSJOI7G6VHjG7pS7Ds8bnSWOS8hsxnhaNNrbmjtwVPnDxWBemceKnAWdA-Ranh7z6UvYVyidPK9YZDjS39OB5kYePZCId909P8q6FJj0F3K5RnlpvIZSB_q4CewFWtQPJpXAIfgubqUxAQQFtZuvlephrEMAxtWRrZdO4IPRsatFeo0ZDoLWRQx4wxSDOnfNhy2pOW4TxSgT15ZzNh6Ds0r1rkG40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امان از دست رامین رضاییان و اداهاش
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107125" target="_blank">📅 16:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107124">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9325345835.mp4?token=EMAkwz430DtPoAedvVETFxXvqPhrOwU4ukNWZ3D-PsvSDFmSX0fVlKSxs3uMSw58MyEgcfWd1oUp0HmwqIStR77nKJk8iAoOUac58Dg-WUMpguCjlbhsQO0Pr42plFZ-xKkjFcXMRNo-mLip8m10ekg4OpeaJMpYbHCKQty-7Q6vo8KA-AAW3z3X7-rDY5gYJ8c_3F57QQeNazz0pQjCVEi2XtmZJc0FS5Arp-nwi3FHC_NNGn3K4rRtwoWzxTOAgYXOolyuQxTa0RzrFKIY7VPg7z-MML6i-P90h4hNNjIZ-wmOAHS2Qpf-7XnwUhI-YMTGKL3W2MTju3G4R8zxNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9325345835.mp4?token=EMAkwz430DtPoAedvVETFxXvqPhrOwU4ukNWZ3D-PsvSDFmSX0fVlKSxs3uMSw58MyEgcfWd1oUp0HmwqIStR77nKJk8iAoOUac58Dg-WUMpguCjlbhsQO0Pr42plFZ-xKkjFcXMRNo-mLip8m10ekg4OpeaJMpYbHCKQty-7Q6vo8KA-AAW3z3X7-rDY5gYJ8c_3F57QQeNazz0pQjCVEi2XtmZJc0FS5Arp-nwi3FHC_NNGn3K4rRtwoWzxTOAgYXOolyuQxTa0RzrFKIY7VPg7z-MML6i-P90h4hNNjIZ-wmOAHS2Qpf-7XnwUhI-YMTGKL3W2MTju3G4R8zxNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شوخی‌های بامزه ابوطالب با پرسپولیسی‌ها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107124" target="_blank">📅 15:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107123">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=bXuhWDbxEDupzLbVFV-eIzQAh33oxPxHfMtyrxRoMY9l_K32cPIHW65FKuv--qWNMFX1ugd7kfgpXDRYqLCaSDIRjbMETj2AQIBdRejXCDug607vm7q4hGK2a3qblUesSclxNf-IzJDuzoPON_iNz8xIsYjjLpcbOvY0yDuQNlX2z8re9M-lKItsS4E2KhP26V0Xss8vMWQSkhtgDaZzfXK7aziz5CyV75mvogGeiRElIBQmGSc0j3qw8jOJ74rb58Sz2B0OP8U8ZuanFXaPq-YcIe_U78XArhDufi7e8OY0521KEJKJp6OhNJ0UFaR2jBxqr5NT-vUDv_y2ckgzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=bXuhWDbxEDupzLbVFV-eIzQAh33oxPxHfMtyrxRoMY9l_K32cPIHW65FKuv--qWNMFX1ugd7kfgpXDRYqLCaSDIRjbMETj2AQIBdRejXCDug607vm7q4hGK2a3qblUesSclxNf-IzJDuzoPON_iNz8xIsYjjLpcbOvY0yDuQNlX2z8re9M-lKItsS4E2KhP26V0Xss8vMWQSkhtgDaZzfXK7aziz5CyV75mvogGeiRElIBQmGSc0j3qw8jOJ74rb58Sz2B0OP8U8ZuanFXaPq-YcIe_U78XArhDufi7e8OY0521KEJKJp6OhNJ0UFaR2jBxqr5NT-vUDv_y2ckgzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
جدیدترین صحبت‌های رامین‌رضاییان درباره عشق‌وحال با توصیه به بازیکنان رده‌های پایه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/107123" target="_blank">📅 15:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107122">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=h-r4V1cmRcI0oj89LXIeJyPqZs7jZQtoAkT1ZRJFgjLuyW1-3bdCMoxCD5vxbivGWjZM77vLOqvXleG4Ff5xTHTqy_px1Omft3__ftbElSskiw97x5fK94vBlWvLxiYX-HZW1BTqvS6hTYvQd3I6ao5CQi21Ac-WlfyaexT67f2YbEkrYjEN7VLMvcReX8oja2lKlz9n6adUCp3wqeWEgE7i0hnPaHujFnom42uNDbiWlJEE-DOIeHUIpwMlgGI84p1RBwGlWsH6OwP9eFm8-bDlAXredKDRQvBNa5BAHU47On1fxKGWpCCqH2c9REYaqGfYIuMcAUOmtFiP_rKWYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=h-r4V1cmRcI0oj89LXIeJyPqZs7jZQtoAkT1ZRJFgjLuyW1-3bdCMoxCD5vxbivGWjZM77vLOqvXleG4Ff5xTHTqy_px1Omft3__ftbElSskiw97x5fK94vBlWvLxiYX-HZW1BTqvS6hTYvQd3I6ao5CQi21Ac-WlfyaexT67f2YbEkrYjEN7VLMvcReX8oja2lKlz9n6adUCp3wqeWEgE7i0hnPaHujFnom42uNDbiWlJEE-DOIeHUIpwMlgGI84p1RBwGlWsH6OwP9eFm8-bDlAXredKDRQvBNa5BAHU47On1fxKGWpCCqH2c9REYaqGfYIuMcAUOmtFiP_rKWYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
مقایسه فوق‌العاده سمی ابوطالب حسینی از فحاشی تاریخی مرتضی فنونی‌زاده و خداداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107122" target="_blank">📅 14:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107121">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=jPsgopL4QkDGa71OeHyQCJqKy1Cijrbgy6HN5H9Vt8LC7lyQfP-Mq1YYo8AdbT1iMTf16OXDDazm44n2wa4oIfGu3rSZSbrgYlUVy6fgN6DG1nOFxC9mqZkRCkfYw5dC3U2iFqO0veqesFVm2r9mjmxUu4NqnQejw8hFz_TjkFBQn1pg2SfyYe6gqUudz6iKkCZEBYDjx5oMgFUrms2SeVm71UZ0xOJfkaYbcnfXCkRSwP5BjMzK1efuaia_U9YAxACpG8VNtUF_mA9J5H7Jb7BP5I3FDT8__wOIXGEP7oqpDSvJp1U-1CgUeJ5-FnsDP2ElA4Ht3mlkOmZIzHVbpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=jPsgopL4QkDGa71OeHyQCJqKy1Cijrbgy6HN5H9Vt8LC7lyQfP-Mq1YYo8AdbT1iMTf16OXDDazm44n2wa4oIfGu3rSZSbrgYlUVy6fgN6DG1nOFxC9mqZkRCkfYw5dC3U2iFqO0veqesFVm2r9mjmxUu4NqnQejw8hFz_TjkFBQn1pg2SfyYe6gqUudz6iKkCZEBYDjx5oMgFUrms2SeVm71UZ0xOJfkaYbcnfXCkRSwP5BjMzK1efuaia_U9YAxACpG8VNtUF_mA9J5H7Jb7BP5I3FDT8__wOIXGEP7oqpDSvJp1U-1CgUeJ5-FnsDP2ElA4Ht3mlkOmZIzHVbpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
خداداد عزیزی مدعی شده که یک‌سری افراد میخوان این یابو‌ رو حذف کنن ولی حذف شدنی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107121" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107120">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=kIhZqMqv2dijAL95BQPSyroCFPNNbjMvt45Mu03NfNT9DGh4zIsYYTtSJRHXa9MQub5GQxM0NTatkFg3f9qzxqJJ1Kg9NwMS_5ZdIM57I6jxpuoKjm6PcgrCvcUB8_kIMBgpfSujpEo66GyPWVUDgf2VSFL1XGWsK_kz4KQhcf4lmCSs57eqkS_LeIwK5Ftev2_Fu5dHi6QHq_FDyv4birUuZ_JkLabc-kjxHfLtzGTC3tm2uTRV-ORnBA_69Ke112xbnb7XrEHb-_GvRu98acZsdAdqvxTTnUTK8UG9NdDrCxEpQAO8Ru-wxYLsppoJRwoge3uNFBrcfeHPj-6daw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=kIhZqMqv2dijAL95BQPSyroCFPNNbjMvt45Mu03NfNT9DGh4zIsYYTtSJRHXa9MQub5GQxM0NTatkFg3f9qzxqJJ1Kg9NwMS_5ZdIM57I6jxpuoKjm6PcgrCvcUB8_kIMBgpfSujpEo66GyPWVUDgf2VSFL1XGWsK_kz4KQhcf4lmCSs57eqkS_LeIwK5Ftev2_Fu5dHi6QHq_FDyv4birUuZ_JkLabc-kjxHfLtzGTC3tm2uTRV-ORnBA_69Ke112xbnb7XrEHb-_GvRu98acZsdAdqvxTTnUTK8UG9NdDrCxEpQAO8Ru-wxYLsppoJRwoge3uNFBrcfeHPj-6daw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لحظه‌ای که سیمئونه شورت امباپه رو کشید پایین؛ سیمئونه گفته اگه قوانین اجازه می‌داد حتی اون‌شورت دومیش هم پایین میکشیدم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107120" target="_blank">📅 14:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107119">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=WlOoS759BXE5ZxJrQHN2KkgrvxT7dodr1n8CgSDiwaeeYhZamqgjxVi-gymvjCGZO6iKLrp8aysHu3f-hRd3FjTCR6UylYj8jtIbrC7fTvZHZ4rdiV94KkpvzwmoEoN2C9rOxaqTnpfwG2LWdMReBJa-i-0itY5KGtyeZgDpW-2xfYmHzG_vEbgS1O9BKuxVNFRBkByZBPtyPfGeT_bDKRHFb9bwba3sK3yF3d4KwDNaMtWxR-Ns_9Ug3rZvf1qR7rgv8AXVk5mxWjYERz4cfUmlP9YCftRnDBOquHrjiiBaFJwdctLVryiGi7fSnJoCpeIy-uUo60f8AB1eNlYROQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=WlOoS759BXE5ZxJrQHN2KkgrvxT7dodr1n8CgSDiwaeeYhZamqgjxVi-gymvjCGZO6iKLrp8aysHu3f-hRd3FjTCR6UylYj8jtIbrC7fTvZHZ4rdiV94KkpvzwmoEoN2C9rOxaqTnpfwG2LWdMReBJa-i-0itY5KGtyeZgDpW-2xfYmHzG_vEbgS1O9BKuxVNFRBkByZBPtyPfGeT_bDKRHFb9bwba3sK3yF3d4KwDNaMtWxR-Ns_9Ug3rZvf1qR7rgv8AXVk5mxWjYERz4cfUmlP9YCftRnDBOquHrjiiBaFJwdctLVryiGi7fSnJoCpeIy-uUo60f8AB1eNlYROQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه دردناک سرقت تلفن‌همراه پاکبان در مشهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107119" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107118">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL8P1nb3OB5-faRwOcpkPyWtf73IWyquakFCXFhrMF7eMc-bLEy0Wr7AfEuo97eQWp-I7bnQ063YhQOgOtEJCfTJgxp_5BEBLP8v2mZ_unpKUWU7vuEOOGC8IR3vHHNYjIibB70bwwBouwVvlfe9tLz9vCyCAboFMg17pEG5vw5P4WXFr1YlFvHyxSNO4z89kaZmnHNz4dwyLquK-Enw7bc_LWEqWjeGGTFoTJtps8lg1kbXqucDYGXfdx9BtRfV1xUzseKiq7fJMUXH0uIrXChqoIcu3P94WQGqPHNZAfEudc65vadMBox3S4WXDK1NPpZY4FDc9NZkJ53hkklUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
📊
5 بازیکن برتر در زمینه خلق موقعیت گلزنی در لیگ‌های معتبر اروپایی تا به امروز:
🇪🇸
لامین یامال – 6 پاس گل.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز – 5 پاس گل.
🇫🇷
خاویر هرناندز – 4 پاس گل.
🇮🇹
پائولو دیبالا – 4 پاس گل.
🇪🇸
آنتونی گوردون – 4 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107118" target="_blank">📅 13:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107117">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh3Mfu_NcSjN9N_mkg0RngCSqMFGCdq8JHivtb1SnhEG9izV6FmQqLLE8lkOMZjX3TJnMnme2TgdvhEFxHdZ5zSu-LAsvTd62QKiUGZtarJ38tQwzV9BPD7XWgTYfpvjmAXc4Y-WF3084At6_dHsDU3RUfcvq8Ow5k-5zMm2i4bCS32jGD6kezADN7yA7d-Ae62yJNu8P-fdLEwibUyB-8rFOTwjWh3p-kT3-NhHpWpN0-IAis6mYAdrkXwfdrPAyNJvjoijs3zKAV8S5TE-f1otACr1WWrmB3TJxf9NL4MBrQSf_3dnadMXS04co2IVLjG6lTxTu_-SIClvXOA5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خاویر آگیره سرمربی تیم والنسیا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107117" target="_blank">📅 12:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107116">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_mXM3JJnE856d_D40NtqEVYo6F2fCLSfx-Ttfs5MklucRUkIUPDfTNDwMyXQuGCiJJjYOA_Qqr5_xkwXfxPzJ2b3o3OmzWWtFdzxJoEb4c4A0VrJRI4Zpc6QfsSZRk6yP6cruLv36R7TIhxvZRshwYPCrRG93KZ5_hU-IP2x3WOAtgGQ3xhExHOeByFIDf8oKw8aZaTpCiAgAItmsJTinukOYATOH914UIhS7L2x5DdaKdvXIlytFOdkvqXSwwtKUTAfQ8D4c6aoNOEDD64EoHV18Ut-jl2sYFC_i1eS5_NdDLUCBTiTvrNo1hmxRu1Xzb5YMZSlC19Je28_TkOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107116" target="_blank">📅 12:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107115">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDZ10hPmsOcwYvqnld2TaBg6uqZuRnm3zRUq1AtN0jJSABC5fuePWnsScZCJVTxbYUeXwfH5HMRlwWUH9uhUxFljT1TzerKq0n_H5PoCch99l-hBj29uIg0kMp5lk1H0_EnDNQAdJIH-Ec6NYmdqEccyh-qKmAB-QDRvU5y8VWXESY8Aj1dLHmzKfJboQ9xxM6cgKdVn9gENoBYS-tSUNK4XYp3z3hUna0tRkF-wWMie7aoBoGdK_bRN2TVtUnQZtOsfX7EMqlr8nSB_ht4lGMtkobzB1takcvhSxhFSqhtYfmiSm-MqDRA-Dthq89vSfHXwlaPxH0VSHsRpQOLfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خداداد عزیزی از اونجایی که خیلی الگوی خوبی برای بچه‌هاست بردنش یه مدرسه تو مشهد تا زنگ آغاز سال تحصیلی هم بزنه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107115" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107114">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1FsTRKAsJpKVdPNiX1HTb_XZPi1c8IZ6DK7XvikCLWuC6oYkrzZrGjEs9tpUotU2dpQbUAuOiKQpykf0qj7_6WDsxIEOpw2Jkbh-48laiNg3P2ofxme2s6_3HUOVuaOE3huZW7ZZhRKHgWXqiBgYonufAUh-WbAE5jDYYHI1-qPKZjkejkpzq-3dzzHlaeMK1BXRb1NEYEZY8fdZIxepBoUxqrTuJkxdkB6WAKUW4H3hGA2V6KfMXBXo-PZbRXOBMa3JGJY4HoDryJ10Z-gFzbWtsqO25GKnBIYZMBK-Gf5PS7QYxwWPNaWgrajuofzPlzyFGLbjTGvXVn3TpGItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
کیلیان امباپه:
🔹
"من نظر شخصی، سال فوق‌العاده‌ای را سپری کردم و این مهم‌ترین معیار برای جایزه توپ طلایی است.
🔹
من نسبت به توپ طلایی امسال خوش‌بین هستم ولی اگر برنده نشوم، ناامید خواهم شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107114" target="_blank">📅 11:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107113">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53478857b1.mp4?token=AuI5MjAoEmdd_ev1JK4KW4jzuv3YXijdulC7XwZgX_d7wpOgtRNNAEdHMgal5o5n5UWjO8kG-BrHmPgH6a--I2GdIis_YD9_e_sJBsW7De50xYZa53CWc95zaFrIKfHYr_Xs9-pJqKrwIsvEhw8R8MVbW1DhusMFXCFl-p2wT0qLK5RqrLaYlbrza098XQ7SGdtNyLUHgIrU9e7xoXvuWT6UT4a-N6wfjFLpahdaOHVBAB9dlIg_-IQB7Ja0ZWCseoJflv40C8qXK1xo8j5jxOU9pnTv-xTDM8jPYpfRMNakZHKW4XYWZKZUVgDl9xGrLLs17BJn9DPIwDX0TZGe2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53478857b1.mp4?token=AuI5MjAoEmdd_ev1JK4KW4jzuv3YXijdulC7XwZgX_d7wpOgtRNNAEdHMgal5o5n5UWjO8kG-BrHmPgH6a--I2GdIis_YD9_e_sJBsW7De50xYZa53CWc95zaFrIKfHYr_Xs9-pJqKrwIsvEhw8R8MVbW1DhusMFXCFl-p2wT0qLK5RqrLaYlbrza098XQ7SGdtNyLUHgIrU9e7xoXvuWT6UT4a-N6wfjFLpahdaOHVBAB9dlIg_-IQB7Ja0ZWCseoJflv40C8qXK1xo8j5jxOU9pnTv-xTDM8jPYpfRMNakZHKW4XYWZKZUVgDl9xGrLLs17BJn9DPIwDX0TZGe2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه گزارشگر صداوسیما به قلعه‌نویی و عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107113" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107112">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTIpx1qOKow_dEirGmsypZCsP5OYqwt_EAU1meDCajzLI4bjstB18zN_DXzNLwJ9xSTjfTgbtj4KyAxlPyre1UOLYS9FpCZ6q-qmhiwP02ZOC1ykz0rDlttqmdw_X6i37mfV1EovGeY9dMetM0Bzor0FWJHPVSMzLM4hRHM-Rfjm6qOwg5fomoJOyvZ8jRJvNhEOGP-u2V9aO9VFwGtuKBd103bNl4GW5O68dE2OvHZlicHMiv_g68EpW5d6LKCZM7s_YIu0j0qbNk6K2JsP8UsG6j3D4pk37WEtTiJZaRZAjGMckUKf1zjyf44XKWuHEtIU_HbLITEmQ6g_GV3YQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
رافینیا:
🔻
"به نظر من، لامین یامال باید بدون شک برنده توپ طلایی شود. او آمار فوق‌العاده، افتخارات، جذابیت و کاریزمایی را دارد که او را برای این جایزه واجد شرایط می‌کند.
🔻
به نظر من، عملکردی که او با بارسلونا و تیم ملی اسپانیا داشته، این موضوع را کاملاً واضح می‌کند و او شایسته این جایزه است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107112" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107111">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107111" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107111" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107110">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHCOjmVynrRnp6K7f8Y4mAmflNSqPtup0PgY045qsvI6H09n-dipYPYOrUmvkU_ZODJjpepd9idM6yMDyM20F0Abp0vbnprpLAdDv-MZUdyAMDT3SsDbfAPplvEjaYYCTo1b2plKwr1fWL1vLw3SpPbiUk3acrGO3wJTyox449XUvLRY6SZVKLSbC8nrJerkJHvqxTIKdVdOWaLOq4ADfHS3nMZKc7tBnsrrDem_PO0WCdvDi7dBSVyBiKXq2v6GzJFAsOJ0h0A1q2rdfgqL5RsDfvuC2tXdnqkLF_Iwdj4I1DchEkqkS_NTXtui69I5isrDuDX9grW6ZG9yFlL2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107110" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
