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
<img src="https://cdn4.telesco.pe/file/Uey9xI1TvSn_7vJSN913eJJ37MSYbhL6W4N8-K6MJAGj0dyzsCs_Z6YgSEJvslBSaJFnw-QJg9x-ayAWWR-hwsPnz_wR2-r_dc-5OgJdR6-DjygIUUu1hTXCj4NsiXmXU6Eporc059gLDmOSKVYAOWDNgx2EUJqgS_dH9nF9e2p02eUXxWTDMpOl3qSd52OI9HsUoSzB6Fev9NZRba8ugLw0wsx9ZPzqkMQyNMdXvAz8B7GnunTTZ7LGwj3SFftjfRQh9Ime4SDTvIz_rNp8ZQ0CrmaM8NPB4LFYkwTc1kjb7klZ5TzOjy8XkkRuCPKcX6FAfMNgj-iXRERpMZHTEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.45M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 02:22:22</div>
<hr>

<div class="tg-post" id="msg-669623">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg9mvXNx2MPKd3PdaSR7MGZjhqZvKG5EixGCPsWu_qpv5yk6f-Mtt392uKA2KIbYB1uU-eZySfaPxW-JRqKaptLbU-pdKBd0EINFdX2USjYBypjKJkiM_JmXtRaH8xeOEN8LO-M1BAka-rFKZVSXCxthuvOrZJLbQdLf6o-3fp-IVO_idgCuAjjcgDOqNW_ZBveEcC3ib00FubvfyCn_aajq6qyjnaKQwnXgHMZGPMfjN217YvSQ9cwnV1GKgij-Cxnu8jZVienEwhhKW2izMvHxvk38Oul_O_V_vMc80gTN0ggWbo1ggR-umTAkKV7UfhCpOG-rXhN00uWf9M2rbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/669623" target="_blank">📅 01:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669622">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUucDoN72ia3PH7Xy0x60z4CrV7GAftqsJJ37vlJfmueVaK0HTQGzMgYnsIZMRBxKS_uMkDUfTkybKO7NYqnNEZ9h165RKo_nVdUAFgf_r6S5swZNnWJBKufGBwErK4Y3F7DoRC9Hy7_8W5ks9uKcltvp7adlQoE7gjx6KKsdGziftPL2UDjCT5VB5LybcYW6Q2_tW6s2HKbfGJGSD1v3JIfV-iWItJ0wq1-LHVwy6XtZT7lKWmNJZni6q0Yl1B0IDTzvXEKFwUsinmgdnuYxE8e2RYnQFYY8UoezX0FAW-TWq2uIQ-i8pam75el8Gx3VlUtzbddeEuMjT2TUkQDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۷ شهید و ۱۱۵ مصدوم در تجاوز آمریکا به ۶ شهر
رئیس مرکز روابط عمومی و اطلاع‌رسانی وزارت بهداشت:
🔹
در حمله هوایی آمریکا به ۶ شهر کشور در ۱۷ و ۱۸ تیر ۱۴۰۵، ۱۱۵ نفر مصدوم شدند که ۲ نفر از آنان خانم بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/669622" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669621">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b443f6dd0.mp4?token=jOZCrwC508d6oU1OvxDbECSSERDY51kY1aXsuYCfFp6kgalYg04pmIxNFtALBoHLMtq3adVZxiF5emYuriqmB3GKYiffer6EFVqE5J7CfQa0Exbw4p6Fd2koAduDNBrVRjb6VnbFNAPa7N3_NWoJ3UX0oFc5n55FruwyoxvXeB07RwtiY27Qn0VfS6GeZ1bYSPFW_Jg_vPtj7YzrM95KaV41AkXH9L_sdzWZp1-51wUL9Qx0HvpHZ6P6pMYtQA4RhmnoLU9ZqtlgHUkQL6OBKX8eom2nep6T4xochDYv-elwCQNYdhOt6HYMs4bgJT8_l1bhWddaiMzETiiHco7ttw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b443f6dd0.mp4?token=jOZCrwC508d6oU1OvxDbECSSERDY51kY1aXsuYCfFp6kgalYg04pmIxNFtALBoHLMtq3adVZxiF5emYuriqmB3GKYiffer6EFVqE5J7CfQa0Exbw4p6Fd2koAduDNBrVRjb6VnbFNAPa7N3_NWoJ3UX0oFc5n55FruwyoxvXeB07RwtiY27Qn0VfS6GeZ1bYSPFW_Jg_vPtj7YzrM95KaV41AkXH9L_sdzWZp1-51wUL9Qx0HvpHZ6P6pMYtQA4RhmnoLU9ZqtlgHUkQL6OBKX8eom2nep6T4xochDYv-elwCQNYdhOt6HYMs4bgJT8_l1bhWddaiMzETiiHco7ttw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خوشحالی جالب برادر خردسال یامال با او پس از پیروزی مقابل بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/669621" target="_blank">📅 00:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669620">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای اکسیوس: مقام‌های آمریکایی در یک نشست توجیهی با خبرنگاران در روز جمعه اعلام کردند که دولت ترامپ از ایران می‌خواهد روز شنبه بیانیه‌ای علنی صادر کند و در آن تأیید کند که تنگه هرمز باز است و متعهد شود که حمله به کشتی‌های تجاری را متوقف خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669620" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669619">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX6iBYGLMdpomV0bHAcBhBQRWRIfTIhBYycmJZsXEkoVJkK_xNK-ED82VnOZXiRJCdCBtdrwJ_LjT-tsDh59UU1ixGpWN4e0F9JYnbCbL8HMVukQ6c-5K5whhIBeIMdg0xGg4xFiPtbPZ4gGfNqESCa2tSd17zM8xaoAUiLVUNGAncLMqdz-RKGeYLatKllsdk-3vlycHOxw8TUwFs2kMBHNfTP9eSlMyTXH0CcZXFCasYeN4O3lE9hv4up8Uohi41bmyLEpsf10emaHcMb9ofIZwb8yf0dDlOrcrELfUm5D746WQRaDRL16vcXBHq-9tmTMS5hpveCjcnHuOGUjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فرانسه - اسپانیا؛ تکرار نیمه‌نهایی یورو ۲۰۲۴ در نیمه‌نهایی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/669619" target="_blank">📅 00:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669618">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0a56bdab.mp4?token=exDPe4GA9fqGnpqEdCh564SCVuFf1rqgz5wtWXnLkfL8jU0HNib2mnEHzdd59EFX_gKV_bEQhHl09lDfAophQeQRm-7cXSRonz0D2L7I7Lb1eMckIq2fBV_mWxO7HBIu4GNNNA6dSZfBlBp6lGiTulz_tlXqkcYc2k1x8faIrToV9jBbX-J1jVpPmOh2GbhC8RkCm-d5v_Q_tHUhMrbuhUmltteSTtoG1UY_GYHeyyQMUORqtUbHgA8nrH6bdjAuNEAHa2WsE7ob-j_u80YSZGpmJRVbgLEx7Ep93mQ_5bEVkfk7BLn7ycVxANzQNJ0YQUFHLusdBjv8NW9LrFAtlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0a56bdab.mp4?token=exDPe4GA9fqGnpqEdCh564SCVuFf1rqgz5wtWXnLkfL8jU0HNib2mnEHzdd59EFX_gKV_bEQhHl09lDfAophQeQRm-7cXSRonz0D2L7I7Lb1eMckIq2fBV_mWxO7HBIu4GNNNA6dSZfBlBp6lGiTulz_tlXqkcYc2k1x8faIrToV9jBbX-J1jVpPmOh2GbhC8RkCm-d5v_Q_tHUhMrbuhUmltteSTtoG1UY_GYHeyyQMUORqtUbHgA8nrH6bdjAuNEAHa2WsE7ob-j_u80YSZGpmJRVbgLEx7Ep93mQ_5bEVkfk7BLn7ycVxANzQNJ0YQUFHLusdBjv8NW9LrFAtlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی‌سابقه عبدالکریم سروش درباره تشییع رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/669618" target="_blank">📅 00:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669617">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427ac3b010.mp4?token=vLY9f5SBvGDKtmrXAKYdcHM2JzXKVO0Ux3XqFNEm3rUUcfAm-xUGAJgeqli7YlBrdADidkiUwGM_YChLwOuL2jDbCH_d73hHNi3cxxBgOKh6himJ2hK1x9rgTZt3Yn__iG8UqdgeA9JwEpUDL7NRaFHrzH2tVH1pHnpUb4H_-9YFvei7MiaJeOUXy1icMkP7n1LedyuNGNeIMX6b4HKLsRvrhwgKUBwWUqUMNoxAL_FTu2C2Z6ggrdhm72o72WOBddHw0K_IcboeyyaMYO8lWYseCB2lNdUvEyOVk83bZ3nl66Z22P1eVFOu5xOx09c6uzse-2GG9aYB5-uipqMcnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427ac3b010.mp4?token=vLY9f5SBvGDKtmrXAKYdcHM2JzXKVO0Ux3XqFNEm3rUUcfAm-xUGAJgeqli7YlBrdADidkiUwGM_YChLwOuL2jDbCH_d73hHNi3cxxBgOKh6himJ2hK1x9rgTZt3Yn__iG8UqdgeA9JwEpUDL7NRaFHrzH2tVH1pHnpUb4H_-9YFvei7MiaJeOUXy1icMkP7n1LedyuNGNeIMX6b4HKLsRvrhwgKUBwWUqUMNoxAL_FTu2C2Z6ggrdhm72o72WOBddHw0K_IcboeyyaMYO8lWYseCB2lNdUvEyOVk83bZ3nl66Z22P1eVFOu5xOx09c6uzse-2GG9aYB5-uipqMcnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سی‌ان‌ان با انتشار تصاویری مدعی شده که ایران در حال بازسازی برخی از سایت‌های هسته‌ای خود می‌باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669617" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669616">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53005e601.mp4?token=m3V3EcazFoXpDJEQWPx96ldie37n4auF7stH3TAK9XEGHcRyUfQt3E7R2fTF0JX8UM21PTeIl81msAeCuvxy6mIERIXIhb_vFCnsM_L6QtPMJZeMq85_kqWtdUkX2NVOsQwecICqssTt6mzE7mzdHy7OsZCbNlM76GSoKlCAK6ci34RzFe2VySzBo9ZqprF5db9OiIzgWBv7RklooJcvplUQsEfpqqKdPG_cV5lCF2re_QtjDjORMynf_9BabqiQKpv37VSa009BlLEDMVhplYslK9FdZCE1oe9yIy3lIUcEeqeZkcQlOc2pBuTXyp7xPeJpUKb5xUnX4qIfHSpOeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53005e601.mp4?token=m3V3EcazFoXpDJEQWPx96ldie37n4auF7stH3TAK9XEGHcRyUfQt3E7R2fTF0JX8UM21PTeIl81msAeCuvxy6mIERIXIhb_vFCnsM_L6QtPMJZeMq85_kqWtdUkX2NVOsQwecICqssTt6mzE7mzdHy7OsZCbNlM76GSoKlCAK6ci34RzFe2VySzBo9ZqprF5db9OiIzgWBv7RklooJcvplUQsEfpqqKdPG_cV5lCF2re_QtjDjORMynf_9BabqiQKpv37VSa009BlLEDMVhplYslK9FdZCE1oe9yIy3lIUcEeqeZkcQlOc2pBuTXyp7xPeJpUKb5xUnX4qIfHSpOeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلیلی: ۲۰ سال پیش یکی از مقامات اروپایی به من گفت این فشاری که به ایران می‌آورند را اگر به کشور ما بیاورند ۶ ماه هم دوام نمی‌آوریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669616" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669615">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3acd0f9ca9.mp4?token=tzJAMJk2UcJ7Ima6A2SXP7F47XqDflec8HdqiVXu8CgLoYdbDnHgJi-cUiS5dIs_hM8-uct6f5Xo9s3_E2taP2bGtJGZUd1qQI-awAbmfyfRxHdXIagN67Ukg0ezNEJaZbvV7k3ULrfQfM9VBWog-jXOOzZYjhhh7HGdmSB8GW6aCDxf_D8-EEXJwWw8vY04xpu5GsztGt4r3_y0twzHJtkt25K_YquVjc2RY6LnKFl7D47hsgu7c9gwsTYA6LBuCuH3Js-Jj_Otw5lyFuW_CYVzThido0liLpJ7Mp4pkE-yLaNzHOOux8y1V5hgpJ4orGBA1L9y4jV8P1e0alQRAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3acd0f9ca9.mp4?token=tzJAMJk2UcJ7Ima6A2SXP7F47XqDflec8HdqiVXu8CgLoYdbDnHgJi-cUiS5dIs_hM8-uct6f5Xo9s3_E2taP2bGtJGZUd1qQI-awAbmfyfRxHdXIagN67Ukg0ezNEJaZbvV7k3ULrfQfM9VBWog-jXOOzZYjhhh7HGdmSB8GW6aCDxf_D8-EEXJwWw8vY04xpu5GsztGt4r3_y0twzHJtkt25K_YquVjc2RY6LnKFl7D47hsgu7c9gwsTYA6LBuCuH3Js-Jj_Otw5lyFuW_CYVzThido0liLpJ7Mp4pkE-yLaNzHOOux8y1V5hgpJ4orGBA1L9y4jV8P1e0alQRAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فاکس نیوز: بر خلاف ادعای آمریکا، کشتی‌ها از مسیر تعیین شده ایران عبور می‌کنند
🔹
فرماندهی مرکزی نیروهای دریایی ایالات متحده اعلام کرده مسیر جنوبی تنگه هرمز همچنان باز است و گسترش یافته است. به گفته ایالات متحده، سایر مسیرها محافظت‌ شده نیستند.
🔹
اما دیروز ۲۲ کشتی از تنگه هرمز عبور کردند. تنها ۱ کشتی از مسیر عمانی عبور کرد و اکثر آنها (۲۱ کشتی) مسیر تعیین‌ شده توسط ایران را انتخاب کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669615" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669614">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aehbyQRWtQZDdYsQXs5b0LMZSHPY_5hYlTyZPQvLtDuzJSkoUAkMJaOcOKTnCGOXeDcC4HoTdr0VPun58ttBMZs59zPg4X-PHfkfGK3WomOwDCgb_viZl4126liDQgT47tONnVjbSORYo3TRJVyX5MFawyO5VlIkJ_2RDKSGYRTFdYb4DaPt6XgG7ZdbV5ManeGVWgMEh8kVfzLvg_HUK7GqQ1Hhts4vL37_XhNRaimLMHcZwIaf70YaZ0lRgGIky6gZnT7yAY4dSbOo1cvIh2-00ix4rjOMQjFf--Zln8g3TyRl5GMT9OzC2-IEBYxed4U5i_LxFWDdG_pUyPDQQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل دوم اسپانیا به بلژیک در دقیقه ۸۸
🇪🇸
2️⃣
🏆
1️⃣
🇧🇪
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/669614" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669613">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4767632a1.mp4?token=kLrs_SUQue1UNhq7kwa756x7rZBOVSK0pLaD3USTQO1R3z970JnD_o0laay55WuRsyCoUzoeZnNMbR4X--KCW9Hc7r7DZscWv7QWHVG3FcaNqysXhjWGioejngYMRrXDOovNX9uLco6e2_Ikxn0boEjUr0tgh7fWGzkXpPnhC6hruzlkpIHHB1WvLa6O-6gu_732Ny2Fkn3FZdqtAIDTxW_NYv9Vk8pG7cNmF3_iM85zK1PLcIj1yVqS2Kx17Vd9gNkCExIc9HA4uWdBMH8zYOxfy0ho0HUQkD1GT1r2a0lPmij39Big3hzctPLiftwFsZg9wV1BTLuiuvalI6uFzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4767632a1.mp4?token=kLrs_SUQue1UNhq7kwa756x7rZBOVSK0pLaD3USTQO1R3z970JnD_o0laay55WuRsyCoUzoeZnNMbR4X--KCW9Hc7r7DZscWv7QWHVG3FcaNqysXhjWGioejngYMRrXDOovNX9uLco6e2_Ikxn0boEjUr0tgh7fWGzkXpPnhC6hruzlkpIHHB1WvLa6O-6gu_732Ny2Fkn3FZdqtAIDTxW_NYv9Vk8pG7cNmF3_iM85zK1PLcIj1yVqS2Kx17Vd9gNkCExIc9HA4uWdBMH8zYOxfy0ho0HUQkD1GT1r2a0lPmij39Big3hzctPLiftwFsZg9wV1BTLuiuvalI6uFzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم اسپانیا به بلژیک در دقیقه ۸۸
🇪🇸
2️⃣
🏆
1️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/669613" target="_blank">📅 00:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669612">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLtqmLGmuV3YZ9kx2dkb7IyhjlCOn2w7U2bEHNniyGCirpNwezKXL9jvoyWVq4tW3ybZ9hPMN_AQ_ObsmfaPxT91HGDmPEW-uOxpVDF0PdHhtSjuFH4sO2bbn9dQdRgGIHze4odfObNVVCfAnysp0nSPKK1zkJE6dhTz8sW1Rm7CT89Espg4o-t1NaTBnLj_L9GzwhJZcf4teuCev9EQyL1GBCHsaAU1DGm6N7flZ70G5d5bWp7QVuFEsDJ3qV5GWORDZsMJA0e01GBaCpbTG_TlsH9AHTwejFsTZSZQhDtvPdubrvfMSFW52a_RFGl3uY3qINnfRarYgDe5kP3nsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدیدی علیه ایران اعمال کرد  دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا:
🔹
اسامی ۸ فرد و ۶ شرکت را در فهرست تحریم‌های مرتبط با ایران قرار داده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/669612" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669611">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2pQkhd9xOs_lbusBGIYoc7GKRF8NlCkszYLCet1K6D6nrb6vV0su0CHEpsVfRHanufW8XFcBeq_-yzvQtT5d1_HnGv4MWyg_eq_CJ2PfO9x96lA9xJuCbcwKpMxrOqdgFGizQGG7jMegAjkA2AlYgTtswNmOJGM0hNbCu072xgn9ALmhVR7YugKT81hfbDZ45eiDF6K6xvOKNnmsnrdNouTR--AXYXRKN4qsQ93x3p1KLCcjU2M5gKJ5IBVUpE5zWQP_MVCsN4UOJg8w44iWKFzUVj1M-aU5rBcTRgio9gnXApDi1V49bDl9KLyBDnci8vG1x-Bla9xdswrJMuhaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی ربیعی: تخریب پزشکیان و قالیباف در این مقطع، فقط یک خطای سیاسی نیست؛ انحراف جهت مبارزه از دشمن متجاوز به داخل کشور است
دستیار امور اجتماعی رئیس جمهور:
🔹
امروز هرکس مدیران درگیرِ مقاومت، معیشت و دیپلماسی را هدف می‌گیرد، آگاهانه یا ناآگاهانه همان انسجامی را می‌زند که دشمن نتوانست در میدان بشکند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/669611" target="_blank">📅 00:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669610">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY1L6ceJkPU-ba94b1P2a-EDPJNQabAbpJ0Ui_YE5T4EeOJ1bOKeeqijJoTrfapBXihLsjMYXMjO0K1NZ8Euq4wfC1vWc1LF-t0_VeM533Zk8VSSXK1cIVs5jxcBcHm9R-83e3p3eRhVnpIF1c2VFpSVGeam_JCHQVwC9IP9l61e4-Nb7a8WnTiu4Q7mm3itpEQ4nZunPNROoaNcE-lnqbPiQi3BqdZw4XfCK19g6dzJ4h2j4XbQn8iwSAHPtR1wFEK6p5ff8t14R3BM_YzwU9OSLNfQArfk2HRC60-cou9iK-6K4rdNqOY8oOepSldT46VKx90Ew0g4mft6xp1PoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آقای ترامپ! روزی در برابر اراده و قضاوت ملت ایران پاسخگو خواهی بود؛ از خشم این ملت آزاده، هیچ راه گریزی برای تو نیست
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/669610" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669609">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPosWiO6X3Z36Z_gwOnQDhHfgsazhYWppoZY8D7-hlMszvTAOM5vRSBfsc38yH3c8zGUjfbMoy7awLXH0_1u4HWggqibQJHfPwZcFoaynH8nqqjrdtfLM9fqBrlXL2OOdnVs-c4QQyIaQlG2d3JlgdTPNjUrI-TYVDqZslUcoeBiGZ1AtTnify6OoknnTje0v9lkcXS-IoPhMeRLb8aUJiQtn7UU5stNW9fpfS2gFkaTdDB75i-gO8DXfeoqsI9IzcjljH0ZLQPba99oiXrakOVOY6oKpApU1ICvB7Hz3pI8Z3A5qkcWnM1Yp3MGA3eEGbL6NyOeTKJ78e4y-MdvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/669609" target="_blank">📅 00:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669608">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
بقائی: نقض تعهدات آمریکا با اقدام متقابل ایران روبه‌رو خواهد شد
🔹
سفر عراقچی به عمان با محور تنگه هرمز و ایمنی کشتیرانی انجام می‌شود. ایران بر اجرای مسئولیت‌های خود در تأمین ایمنی تردد دریایی در تنگه هرمز مصمم است.
🔹
همکاری ایران و عمان برای تسهیل تردد ایمن کشتی‌ها در تنگه هرمز ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/669608" target="_blank">📅 23:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669607">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaca53d8f.mp4?token=j6pnz2ESbcIMWiYPrlYitRPVOmhY2FImfD_iGXTVdzSj8x3OyhE1-ej5_IwtrE3VAOz99jGuN3f7uvNh0tciM6aUJRFQXwpj0j7QMtYAc5E-lkvKpg7QCRvwAj_xSV6Aja9RJrR71BsUJfrkJBRX9yeCf_n0bEjoVbIfInUXQ26mBdionPNjO6TcVSrPP1UairmqxIEb8zYcTkWJvBdMXKfLkOCwsCnxEGd-qTvkfPOqtWDs361CMcrDGJw0UqqI6r7aX5Yoo7zSDPV93khh9VIE0rHdBlzHnNGuD-fA7KUnlbzaqlLMT3wwETzBfbR9dNFm7RXmLF8j3hZx1o2VBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaca53d8f.mp4?token=j6pnz2ESbcIMWiYPrlYitRPVOmhY2FImfD_iGXTVdzSj8x3OyhE1-ej5_IwtrE3VAOz99jGuN3f7uvNh0tciM6aUJRFQXwpj0j7QMtYAc5E-lkvKpg7QCRvwAj_xSV6Aja9RJrR71BsUJfrkJBRX9yeCf_n0bEjoVbIfInUXQ26mBdionPNjO6TcVSrPP1UairmqxIEb8zYcTkWJvBdMXKfLkOCwsCnxEGd-qTvkfPOqtWDs361CMcrDGJw0UqqI6r7aX5Yoo7zSDPV93khh9VIE0rHdBlzHnNGuD-fA7KUnlbzaqlLMT3wwETzBfbR9dNFm7RXmLF8j3hZx1o2VBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ایران اجازه بازرسی از تاسیسات آسیب دیده ناشی از حملات آمریکا و رژیم صهیونیستی را نمی‌دهد و قطعنامه ۲۲۳۱ عملا وجاهت حقوقی ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/669607" target="_blank">📅 23:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669606">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a959e28379.mp4?token=IJqwOdZBh2WixCWIJscXkIqv2HWy--deKfJBwEoJhWDGvRpJopLU_EqPaSRQJS7UhFjyPgJXtacDMaCn71WcWtPzFJZJOh3EoyJWyKBxMG06LAKkFLi9D5cmMiWdLrl062JuLkIGr_o56wsNegunQN6U2FQ4BkXDfOJhYoM6-5gYb1xot1uYRTDnBIVf_15FQ-acH5BI7Zb3xzsqU1qYB54SHeYasCXqmAQUP1Md3MLBLPmZ-GXhkDTPCThmgNTsBHmo3LyPXzhwcjkcOdn0yRNAluBM9WRGpk51DLnC-p8bd-pyTg0LkzGMcufN9km5hlxekMyeE5zw1z6gOoX3Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a959e28379.mp4?token=IJqwOdZBh2WixCWIJscXkIqv2HWy--deKfJBwEoJhWDGvRpJopLU_EqPaSRQJS7UhFjyPgJXtacDMaCn71WcWtPzFJZJOh3EoyJWyKBxMG06LAKkFLi9D5cmMiWdLrl062JuLkIGr_o56wsNegunQN6U2FQ4BkXDfOJhYoM6-5gYb1xot1uYRTDnBIVf_15FQ-acH5BI7Zb3xzsqU1qYB54SHeYasCXqmAQUP1Md3MLBLPmZ-GXhkDTPCThmgNTsBHmo3LyPXzhwcjkcOdn0yRNAluBM9WRGpk51DLnC-p8bd-pyTg0LkzGMcufN9km5hlxekMyeE5zw1z6gOoX3Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما هیچ درخواستی برای مذاکره با آمریکا نداشتیم اما سفر میانجی را به ایران پذیرفتیم
سخنگوی وزارت خارجه:
🔹
پیمان‌شکنی آمریکا یک عادت است؛ با خودشان هم لجاجت می‌کنند. آمریکا چند بند یادداشت تفاهم را نقض کرد.
🔹
آمریکا تفاهم‌نامه را نقض کرده و ما هیچ تعهدی را بدون مابه‌ ازا اجرا نمی‌کنیم. رویکرد ما تعهد در برابر تعهد است. اگر طرف مقابل تعهداتش را نقض متقابلا ایران همان کار را انجام خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/669606" target="_blank">📅 23:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669605">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادعای خبرنگار الجزیره: احتمال برگزاری دیداری بین ایران و آمریکا وجود دارد که مکان آن ممکن است ژنو، اسلام‌آباد یا دوحه باشد
🔹
برگزاری این دیدار منوط به موفقیت میانجی‌ها و توافق بر سر فعال‌سازی باقی‌ ماندهٔ مفاد تفاهم‌نامه است؛ پروندهٔ تنگهٔ هرمز نیز ممکن است به این دیدار موکول شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/669605" target="_blank">📅 23:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669604">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9d9fc2bf.mp4?token=k7u5BDvaKHwkJ4C0Vkjf0DUeIF2kghQJ1Qv2sxJwI_UnQAl5_qpOcRoo7k5XA85q96Wmue6t3_ETfICaHgGRI-nN521uMfNyFY6uLkuH3gtb7kNRnNyM7QGHwWNtZggZKIEEx1eioNPw3dQACryLRe9PNDED5NYCj8ecttkhHU-DIgFyZO7GeCa5q4sz3Nm20PpOqkwx3UdLjQcl_YffoK9fc0glNg46j8Zu7hwa4HJwu8AMIHwB664SnYIKWtSsIUt1hG0RVn_mSu1MD0ZUQcGNTnL58QQeXdLGtegf0Tqk3MVipmCyq28AOhNBGD7cP4I9s36ohRb3J8dDXjg9jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9d9fc2bf.mp4?token=k7u5BDvaKHwkJ4C0Vkjf0DUeIF2kghQJ1Qv2sxJwI_UnQAl5_qpOcRoo7k5XA85q96Wmue6t3_ETfICaHgGRI-nN521uMfNyFY6uLkuH3gtb7kNRnNyM7QGHwWNtZggZKIEEx1eioNPw3dQACryLRe9PNDED5NYCj8ecttkhHU-DIgFyZO7GeCa5q4sz3Nm20PpOqkwx3UdLjQcl_YffoK9fc0glNg46j8Zu7hwa4HJwu8AMIHwB664SnYIKWtSsIUt1hG0RVn_mSu1MD0ZUQcGNTnL58QQeXdLGtegf0Tqk3MVipmCyq28AOhNBGD7cP4I9s36ohRb3J8dDXjg9jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در سال ۲۰۱۹ جز جوکرهای عراقی مخالف ایران بود و اکنون برای امام شهید اشک میریزد و صحبت‌های شنیدنی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/669604" target="_blank">📅 23:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669603">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
دولت وابسته به ریاض در یمن: از ایران به شورای امنیت شکایت می‌کنیم
🔹
عبدالله العلیمی، عضو تشکیلات موسوم به «شورای ریاستی یمن» که توسط دولت سعودی تشکیل شده است، شکست محاصره یمن توسط هواپیمای ماهان را «نقض حاکمیت» یمن توصیف کرد و گفت که شورای ریاستی این موضوع را در شورای امنیت سازمان ملل مطرح خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/669603" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669602">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c645673a2.mp4?token=VLb090RC8MhYF09sbhVo-4NLslQhFIy4GHag6iU_NUHnP17TWbQabwqKLmY8mlE8TfXQAcE8YVd900b12bUdveDzm424KhIVT915K_AUm3q15I6k9jlh5OrZf_93AMbfim6kulVBGpwm024qnGtzZMfP2IN3fR8C1seisPA4CaBm57NxK93Hzj8a9amOVopPKvo5h04ckSxEKOu3BCdHyMpRlbwuoNhT7SADviDt2LNTJRa8Fnt1G_vmi3X3xTK-XYnCHny0Yy6u-KQ0OshIVoy3G48EmWfYSPMBUpzOaLinMv4zLHkTNS0UpauyJtQOwDa1sA3CcSRD5FZBaH8nLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c645673a2.mp4?token=VLb090RC8MhYF09sbhVo-4NLslQhFIy4GHag6iU_NUHnP17TWbQabwqKLmY8mlE8TfXQAcE8YVd900b12bUdveDzm424KhIVT915K_AUm3q15I6k9jlh5OrZf_93AMbfim6kulVBGpwm024qnGtzZMfP2IN3fR8C1seisPA4CaBm57NxK93Hzj8a9amOVopPKvo5h04ckSxEKOu3BCdHyMpRlbwuoNhT7SADviDt2LNTJRa8Fnt1G_vmi3X3xTK-XYnCHny0Yy6u-KQ0OshIVoy3G48EmWfYSPMBUpzOaLinMv4zLHkTNS0UpauyJtQOwDa1sA3CcSRD5FZBaH8nLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت مردان آهنین به تلویزیون با یک سورپرایز
🔹
سری جدید مسابقات مردان آهنین با اجرای آیدین ختایی که از شرکت کنندگان قدیمی این برنامه است و حضور فرامرز خودنگاه، رضا قرایی و محراب فاطمی به زودی از شبکه سه پخش می‌شود
🔹
مردان آهنین هر شب ساعت ۲۰ از شبکه سه پخش می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/669602" target="_blank">📅 23:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669601">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993c03098e.mp4?token=nlCbxjaTYZIaRRa4cuSXlPTIxyAHm5mQLmDxbtt1VAbmHENDL8TuQFMQTvVWmBecyqAke6B23gakBFqTvfiu2aGNbtEUk8jv9EbWXcltXag2WHpTzY3cQ6ktWJN3NiW2tbbTgLiYOx-a1UTdx-sMy6oR2_CKE8ToTFMeoD0F6d4UjInbv2C_Pgh1AnVu3Ga1rgGy2rBkuzt3WXl4IzO5IrVSaubByAlRP0oEU4Tay_xAGZeHXB613QawjtLEpdeWNncgZekS-CVpCnfUz-xZRXKhvh84q2rNrxnRKqh5CM5aNGi1qrvDWqR9nlKXVzDKbLERGzTV_f6smZcMyaImkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993c03098e.mp4?token=nlCbxjaTYZIaRRa4cuSXlPTIxyAHm5mQLmDxbtt1VAbmHENDL8TuQFMQTvVWmBecyqAke6B23gakBFqTvfiu2aGNbtEUk8jv9EbWXcltXag2WHpTzY3cQ6ktWJN3NiW2tbbTgLiYOx-a1UTdx-sMy6oR2_CKE8ToTFMeoD0F6d4UjInbv2C_Pgh1AnVu3Ga1rgGy2rBkuzt3WXl4IzO5IrVSaubByAlRP0oEU4Tay_xAGZeHXB613QawjtLEpdeWNncgZekS-CVpCnfUz-xZRXKhvh84q2rNrxnRKqh5CM5aNGi1qrvDWqR9nlKXVzDKbLERGzTV_f6smZcMyaImkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پتروپالایشگاه پلدختر
🔹
عصر امروز حادثه آتش‌سوزی در یک مینی‌پالایشگاه در پلدختر رخ داد؛ به‌دلیل ماهیت مواد اشتعال‌زا و گستردگی حریق، عملیات مهار با دشواری مواجه شده و نیروهای امدادی و آتش‌نشانی با وجود استقرار در محل، به‌دلیل شدت شعله‌ها…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/669601" target="_blank">📅 23:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669600">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca181b0c6.mp4?token=SrPtQEklICtcuyFf3y1q-9hR8nU_GzRxe6kn8QjH3K-ANkwCmFwd3DTCVo9KgP6JL421cI2rq4qCvVskVgpOaPvwgEXdWVGh96veTLLY9qEtnL5qoE0hNq3pvwPRlkp3ABa3N-Sf0SyRbxaw81RegjLvEXqI2FL3Nsv121UmaYpnUGFpEJtNGFQdF76raa7fFHvRPSx_yclyu7yq1trlaglmIs27REqZGlKK48cXpNo0vDesf8rSYBIF7nK9D1BY0Xcwb0tHx2MLglXJLVaCoKJwLeC3YZYNpGOMrjdTv4QaSNDXPMcnIGzJW5n9SBFx7Xmb3MyNTDaeSZHsUI23gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca181b0c6.mp4?token=SrPtQEklICtcuyFf3y1q-9hR8nU_GzRxe6kn8QjH3K-ANkwCmFwd3DTCVo9KgP6JL421cI2rq4qCvVskVgpOaPvwgEXdWVGh96veTLLY9qEtnL5qoE0hNq3pvwPRlkp3ABa3N-Sf0SyRbxaw81RegjLvEXqI2FL3Nsv121UmaYpnUGFpEJtNGFQdF76raa7fFHvRPSx_yclyu7yq1trlaglmIs27REqZGlKK48cXpNo0vDesf8rSYBIF7nK9D1BY0Xcwb0tHx2MLglXJLVaCoKJwLeC3YZYNpGOMrjdTv4QaSNDXPMcnIGzJW5n9SBFx7Xmb3MyNTDaeSZHsUI23gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اسپانیا بالاخره گل خورد
؛ گل اول بلژیک به اسپانیا توسط دکتلاره در دقیقه ۴۱
🇪🇸
1️⃣
🏆
1️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/669600" target="_blank">📅 23:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669599">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c6e5b928.mp4?token=cZhYZuKs1oRE_osybQekcIW_lF_M1Q7Zhz_wqGx4BUcZEThWo-rowcGk_obalxDi_oiFAvv8n5FAmqmTeREaxIi9lkWBqRDrNQVJ-cIrhf8ol__0Sr1t6XfRb_rvNNzAyF_LJo1_WXTrF_dvCFOp6WAPx4e-gu-aFn-2rFtv7kRIW-yPDH4h1WLxSNbZhyGvjf3LERg3u5CbAk6hf_71Ve_HnZv7Cx4y-Fv5zFR8ULMzl0uYhCicF96X5yUEHDp2sYoZjR6K6Yc5d2hYij-90Wa5mThINRYP8jvAtb8eD7VRH8dWpuCAGK5pcJEsDGPG5lZzfmKuhtkewiyeoDZUAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c6e5b928.mp4?token=cZhYZuKs1oRE_osybQekcIW_lF_M1Q7Zhz_wqGx4BUcZEThWo-rowcGk_obalxDi_oiFAvv8n5FAmqmTeREaxIi9lkWBqRDrNQVJ-cIrhf8ol__0Sr1t6XfRb_rvNNzAyF_LJo1_WXTrF_dvCFOp6WAPx4e-gu-aFn-2rFtv7kRIW-yPDH4h1WLxSNbZhyGvjf3LERg3u5CbAk6hf_71Ve_HnZv7Cx4y-Fv5zFR8ULMzl0uYhCicF96X5yUEHDp2sYoZjR6K6Yc5d2hYij-90Wa5mThINRYP8jvAtb8eD7VRH8dWpuCAGK5pcJEsDGPG5lZzfmKuhtkewiyeoDZUAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جدید عمو فیتیله‌ای: بازی از لحظه‌ای شروع میشه که دیالوگ تموم میشه
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/669599" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669598">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51b25b24c.mp4?token=quQF0OpHy3HKixcl2oTwHFqNTiz2fKmghHmF-xbpO8QHdIS1f8keEodrvZVUPgSZRfzwSyEzBqU2TfAp2uMq-SamvmwJTe4d4IMZFzu9FORTG0prQj9O4HpWeNFc-AU0vyIDpG9qJw4prDyLch1pU7FDc2muYg6U_COZp7NJsXbkoo50tEZJAj_Cox4xzV9zP1JgYn2K3DlRIe9XvA10QfbZFTpe1MwOs-VBUuMWjn25C0ePvdgAIU6_nf9WngwuMWz4Gf_bEQhdAH52otRyd_Ti0jdXHBABEotKiy1WMR0kcMw0QXiho3tiwwMf0uC9hWlEupXbcFZGWepzrjv2zKYVWSs4QkSMqHPTjZQkljdTzeU31SjG-WDU322oublKlIaLgTae1OghR570kFqsfjX76A8p9qbcuyufuULVRQEalL-meROG-JDUmqSxHQ9gKPLs_o_OgumjyJL3ZC14Ow2_obeZtPhmFhMLSSbVi6KlUEmwR65S974QqoIA1sZonIVEH8s9P-Okj1GjeUdR4eV7f6YKft_64qbzAAUJ6n1JsPPEa0xjVrymvCvS50r5a5YqZB1KR0KOy2e62C9pg9dzje8TZ9YNJ23f9u425YyRKGLIF1IU5vL9_lvDbUK3Z4R4zIz1upz34x_NR-lGUSqUWFcAA5zo7mvM5XZGyes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51b25b24c.mp4?token=quQF0OpHy3HKixcl2oTwHFqNTiz2fKmghHmF-xbpO8QHdIS1f8keEodrvZVUPgSZRfzwSyEzBqU2TfAp2uMq-SamvmwJTe4d4IMZFzu9FORTG0prQj9O4HpWeNFc-AU0vyIDpG9qJw4prDyLch1pU7FDc2muYg6U_COZp7NJsXbkoo50tEZJAj_Cox4xzV9zP1JgYn2K3DlRIe9XvA10QfbZFTpe1MwOs-VBUuMWjn25C0ePvdgAIU6_nf9WngwuMWz4Gf_bEQhdAH52otRyd_Ti0jdXHBABEotKiy1WMR0kcMw0QXiho3tiwwMf0uC9hWlEupXbcFZGWepzrjv2zKYVWSs4QkSMqHPTjZQkljdTzeU31SjG-WDU322oublKlIaLgTae1OghR570kFqsfjX76A8p9qbcuyufuULVRQEalL-meROG-JDUmqSxHQ9gKPLs_o_OgumjyJL3ZC14Ow2_obeZtPhmFhMLSSbVi6KlUEmwR65S974QqoIA1sZonIVEH8s9P-Okj1GjeUdR4eV7f6YKft_64qbzAAUJ6n1JsPPEa0xjVrymvCvS50r5a5YqZB1KR0KOy2e62C9pg9dzje8TZ9YNJ23f9u425YyRKGLIF1IU5vL9_lvDbUK3Z4R4zIz1upz34x_NR-lGUSqUWFcAA5zo7mvM5XZGyes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز فصل دوم «سرآشپز»/ ادامه رقابت بزرگ آشپزی در شبکه سه
🔹
پس از استقبال مخاطبان از فصل نخست مسابقه تلویزیونی «سرآشپز»، فصل دوم این برنامه به زودی روی آنتن می‌رود.
🔹
این مسابقه با محوریت رقابت آشپزان و نمایش مهارت، خلاقیت و فرهنگ غذایی ایرانی تولید شده است.
🔹
سرآشپز در حالی آماده بازگشت به آنتن می‌شود که موفقیت فصل نخست و استقبال مخاطبان، زمینه‌ساز ادامه این رقابت تلویزیونی شده و انتظار می‌رود فصل جدید نیز با همان رویکرد سرگرم‌کننده و رقابتی، مورد توجه علاقه‌مندان قرار گیرد.
🔹
این برنامه از شنبه پس از اخبار ساعت ۲۲ از شبکه سه پخش می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/669598" target="_blank">📅 23:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669597">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
رییس دانشگاه علوم پزشکی مشهد: هیچ حادثه منجر به فوت در مراسم تشییع رهبر شهید رخ نداد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/669597" target="_blank">📅 23:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669596">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50cfe83713.mp4?token=ub96Cic6SYtHBDyKm1QE4EYsLoTtF2cxT_3Vh_OeVtQOU9sXxcD3g3QgzGBA-OVpyiZcfZXVQYsxv4Xo9Xd507sshPxRBJtZnXsrRrrF5-6eEupd5F7SQR2ppnDiss2gLeGTOiDJMqXEn-t3TKGhXFMG0ciaXJY0cIx5x_VkKwZ5yNONoxcxKSjnGx0zw8vtV06rdwYElznzsCzPLGw3chY3FgPPTKDWcMa7EIuMsK8OxAbUCXxHWp4lwY76RdLQbmOzV7q-GDzjUzMbC8OW-bhLNPnbspjWU3NhyTtXeh4KEsg8R39xgEy12OZ2MgAcyG5KiAY6p2kT5sQ1xaGtsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50cfe83713.mp4?token=ub96Cic6SYtHBDyKm1QE4EYsLoTtF2cxT_3Vh_OeVtQOU9sXxcD3g3QgzGBA-OVpyiZcfZXVQYsxv4Xo9Xd507sshPxRBJtZnXsrRrrF5-6eEupd5F7SQR2ppnDiss2gLeGTOiDJMqXEn-t3TKGhXFMG0ciaXJY0cIx5x_VkKwZ5yNONoxcxKSjnGx0zw8vtV06rdwYElznzsCzPLGw3chY3FgPPTKDWcMa7EIuMsK8OxAbUCXxHWp4lwY76RdLQbmOzV7q-GDzjUzMbC8OW-bhLNPnbspjWU3NhyTtXeh4KEsg8R39xgEy12OZ2MgAcyG5KiAY6p2kT5sQ1xaGtsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به بلژیک توسط روئیس
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/669596" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669595">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efc7721ca.mp4?token=CWJMkH9pqi0MbNnn5XfS_N1NmHBxhuYwrb9QhDPSekzh6634X7JnBi_sED6o6ncmyS_5km8AlqJOuTAWPvwsIAhYH3XM9A6JIL_DKKv3tWBif0kTlTzD9GoPwdsupKrIO8OhMNLfS8FZewd7yegDqPKWxa1IyiXJHZ9b3QGgVqC484j3e--wZVA1M8xX7vy8m-seIXPqLDIY1YOqaLru_p2a8ojAi9p2Ai1TcPemb6a2GQOSqXNOqflQbqu2_9LcDMJbB_FyH_JLdYM2JFjVsFp66rcToKmMBcEHouQBK30mBZdSYWZi61vm76wrFmwKbP-je1e17Lq9BBhcPuBo9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efc7721ca.mp4?token=CWJMkH9pqi0MbNnn5XfS_N1NmHBxhuYwrb9QhDPSekzh6634X7JnBi_sED6o6ncmyS_5km8AlqJOuTAWPvwsIAhYH3XM9A6JIL_DKKv3tWBif0kTlTzD9GoPwdsupKrIO8OhMNLfS8FZewd7yegDqPKWxa1IyiXJHZ9b3QGgVqC484j3e--wZVA1M8xX7vy8m-seIXPqLDIY1YOqaLru_p2a8ojAi9p2Ai1TcPemb6a2GQOSqXNOqflQbqu2_9LcDMJbB_FyH_JLdYM2JFjVsFp66rcToKmMBcEHouQBK30mBZdSYWZi61vm76wrFmwKbP-je1e17Lq9BBhcPuBo9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلیلی: باطل‌ترین جبهه در مقابل جبهه حق ایران ایستاده و آنچه پیروزی را رقم می‌زند تاب‌آوری یا همان صبر است
جلیلی:
🔹
جمهوریت و همراهی مردم با نظام بسیار ارزشمند است و باید در همه زمینه‌ها ارتقا پیدا کند. معیشت بدون امنیت و دفاع از ملت به دست نمی‌آید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/669595" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669594">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm5PYKl3ZHOnJT2LRagZEfNRLKPXmsuAt1dOWqr38kyLNmw0vSM5MBUP4VUlr99VyEUpkmMfu8a82Z9z5Fd1g8VgpLYOFjUUySUeSzX-NxDVQNjiglilS-o575dihvDIuoYvlEp8058ygTR_gUzaf6ChVE5K1hLwg0Ug6eSrl4Vhyj_8fPLaArs1lAQ8t2ypLez_sr5HQvQJlJarbAgxtWKYTEBIaq9jijipmus5chfykutdNfSTcHUaxb6_X_4PzeUp00nPJ7hzrzRbS1oGl4E40-cToktZ42ejw6a8-P5DZM5J6yJbjbQ5YHgSsEmE8Zh3DfR8aLgzJ5hU0bKqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده ۲۰۰ میلیون تومان صندوق طلای رز ترنج شوید
🟢
این بار، ترکیب شما می‌تواند برنده ۲۰۰ میلیون تومان صندوق طلای رز ترنج شود.
همزمان با روزهای پایانی جام جهانی، شرکت ترنج مسابقه‌ای ویژه برگزار می‌کند.
🟢
با عضویت در کانال تلگرام ترنج، علاوه‌بر دریافت جزئیات و اخبار این مسابقه، با تحلیل‌ها، دیدگاه‌ها و دنیای مالی از نگاه شرکت ترنج نیز بیشتر آشنا خواهید شد.
🟢
به زودی جزئیات رقابت، اطلاع‌رسانی خواهد شد.
🔗
جهت عضویت در کانال تلگرام ترنج اینجا کلیک کنید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/669594" target="_blank">📅 23:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669593">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
حزب‌الله با مذاکره مستقیم با اسرائیل مخالفت کرد
🔹
ابراهیم الموسوی، عضو فراکسیون وفاداری به مقاومت در پارلمان لبنان، اعلام کرد حزب‌الله «توافق چارچوب» را رد می‌کند و آن را مغایر با قانون اساسی لبنان می‌داند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/669593" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669592">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCKnmhgIcXWfh-Ku00vkprN2d_1bPRlk7TBjly8blAP70fe1TUTpnh_fNb0_xmb1Ilbp_wQP-Ghmr5frNn_FullZr8WvX65Snjlbt_SCHnSBUsTFl3XDulwvBsmRDacrabIhIu2D2IjYuIXgXsoqoaRETslJhxdtylsUsmyXUnjCXU-8jXt_xKcx4bVmHe10M4WYZiaPdzkj4VZ74bEPk0PYeur054Lxbv43ck4BCGkPVwcQRbfcd-ER9Ns2tsigplXb3d5Rz_OBt6PrnKA7w99sl69_0sITyK1NwfFFzSrmfHz74By04_Wuqmp1j92DcvZRkjGRVgCPZgRJ1BlqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کیسه‌ زباله‌های عروسی تیلور سوئیفت دونه‌ای ۲۵ دلار فروخته شدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/669592" target="_blank">📅 22:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669591">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
جزئیات آتش‌سوزی نیروگاه تبریز؛ شایعه حمله تکذیب شد
اطلاعیه اداره‌کل مدیریت بحران استانداری آذربایجان شرقی:
🔹
به اطلاع مردم عزیز می‌رساند، حوالی ساعت ۲۱ امروز جمعه ۱۹ تیرماه ۱۴۰۵، نقطه اتصال یکی از واحد‌های نیروگاه حرارتی تبریز به شبکه برق سراسری، به خاطر مشکل فنی دچار آتش‌سوزی شده که عوامل نیروگاه تبریز، برق منطقه‌ای و آتش‌نشانی تبریز، بلافاصله در مکان مورد نظر حاضر و حریق را اطفا کرده‌ و در حال حاضر در حال لکه‌گیری هستند.
🔹
همچنین تاکید می‌شود، از لحاظ پایداری شبکه برق، هیچ مشکلی وجود ندارد و مشکل پیش آمده برای واحد مذکور، در کوتاه‌ترین زمان ممکن، رفع خواهد شد. تصریح می‌شود، شایعات مبنی بر تهاجم دشمن به نیروگاه تبریز کذب و جعلی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/669591" target="_blank">📅 22:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669590">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e36e4e81.mp4?token=SoalG4c92pcyJPSmVsgV8uWmIqYoX3Preh425GxmECg-ii-uez7YI8H0d3X5GYCZrS9PDzEiQ-MXVGFYfVO3Y0rYA2pA5RdHLEoxb7QXij0Jnc6G81YSGH0Iz4nB1iIwlwNaQ_JolE7kB_jt6JRtTcPhbeAAV7meF5cHULMIBXOloHvDZqXasWGQdCXJhlNs6hMNIZhUPpXQlFOTPJY6uIOnZrbF5FfEF1N3K1U172h3AFybCiGRMiL8S8lW627aR3DS-xI6BjS8vMKwiOZQ0gBQLVc2gkSjnxwDGAb8lN7ySESzENToNLX_64UIAzXverStUblcb0lgTSsL2vPYpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e36e4e81.mp4?token=SoalG4c92pcyJPSmVsgV8uWmIqYoX3Preh425GxmECg-ii-uez7YI8H0d3X5GYCZrS9PDzEiQ-MXVGFYfVO3Y0rYA2pA5RdHLEoxb7QXij0Jnc6G81YSGH0Iz4nB1iIwlwNaQ_JolE7kB_jt6JRtTcPhbeAAV7meF5cHULMIBXOloHvDZqXasWGQdCXJhlNs6hMNIZhUPpXQlFOTPJY6uIOnZrbF5FfEF1N3K1U172h3AFybCiGRMiL8S8lW627aR3DS-xI6BjS8vMKwiOZQ0gBQLVc2gkSjnxwDGAb8lN7ySESzENToNLX_64UIAzXverStUblcb0lgTSsL2vPYpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلیلی: رهبر شهید کاری کرد که کسی نتواند مثل جنگ جهانی دوم ایران را اشغال کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/669590" target="_blank">📅 22:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669589">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
عراقچی، فردا شنبه ۲۰ تیرماه در رأس هیاتی دیپلماتیک به عمان سفر خواهد کرد
🔹
قرار است در این سفر درباره مناسبات دوجانبه و تحولات منطقه، به‌ویژه وضعیت تنگه هرمز، گفت‌وگو و تبادل نظر شود./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/669589" target="_blank">📅 22:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669588">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
گفتگوی تلفنی سران ایران و پاکستان
پزشکیان:
🔹
برخی بازیگران درصدد برهم زدن روندهای موجود و جلوگیری از استقرار آرامش در منطقه هستند. انتظار طبیعی آن است که سایر طرف‌ها نیز به تعهدات خود پایبند باشند و از اتخاذ مواضع یا اقداماتی که موجب تضعیف اعتماد و پیچیده‌تر شدن روندهای دیپلماتیک می‌شود، پرهیز کنند. احترام متقابل و التزام عملی به تعهدات، پیش‌شرط هر توافق پایدار و موفق است
شهباز شریف:
🔹
پاکستان آماده ادامه نقش‌آفرینی برای کاهش تنش‌ها و پیشبرد روندهای دیپلماتیک است. منطقه بیش از هر زمان دیگری نیازمند صلح، ثبات و همکاری است و پاکستان مصمم است در این مسیر، رایزنی‌ها و همکاری‌های خود با جمهوری اسلامی ایران را با جدیت ادامه دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/669588" target="_blank">📅 22:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669587">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDo6pfvyu9dVrJ3pEEwINTXpz276QasILlQJM5azmgmSu2ohEupSmm9FSbdMtRGbXOVAxZFU95wIhStit3pAAq9Rem9GvS5JW1BmZnSyH-TeBwfhNI-XGK4TQeET5PXQHLFXEjbA_YKWc_kkpLNbqxXJS4xNTY6U5su6U1Jh7uinoOvTfYiv-V3QtpmyyLxLq1YHV1hos9zxXCGK8QdAX4IThqEtIO17awq-Ck8PPNvx2XVc4-kNo3myTk2szulUVpVus7fj73leBw0k8_KHIc7_qjEllYLiQ88spByV1EJuVIfl-cgOoY9o7uvZYbBOpz0_n0N4u-MytOd3ujWdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش رئیس مرکز ارتباطات آستان قدس رضوی به حواشی رخ داده پیرامون نماز رهبر شهید انقلاب در حرم رضوی
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/669587" target="_blank">📅 22:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669585">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc86peZXjyA0aGN14uxw6tk0Au5GlWxObHfDytLpAW66bd7pOWMK42GsvyTJOGlomq6JIggeEf4DSPu926Qi9LRB4nBlIO-HaGFnk1A6-YVtrYtZoCQVcuDu4h_u-QWm3Xu4u-RaJZrni33YWOGzG_sR_K2WCFh34HuBguHKCsoXT8g5TYpDkV_nhpydLjTUyS2QfxuGz42qaOOxznMRfd_au05LEj2VizJA3_ZFGHHS_AFqL-Sl0mDSsP3Ma13ZADm8WoqVy30i9it43pq99LOJ2PVRnqmnUjxadSzc9g4gg7HyX6wjSjZuF5SdmSgSWGI7ZxfgrRwUwBWMCEmgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار | شروع مجدد جنگ و نوسان شدید طلا
⚠️
در جنگ دوازده روزه و هم در جنگ چهل روزه طلا ریزش بسیار شدیدی را تجربه کرد
❗️
این دفعه مجدد جنگ شروع بشود آیا قیمت طلا به گرمی
1
4
میلیون می‌رسد و دوباره قمیت
ملک
شدیداً رشد می‌کند؟
تحلیل تخصصی منتشر شد!! روی لینک زیر کلیک کن و تحلیل رو ببین تا دوباره ضرر نکنی.
⬇️
⬇️
⬇️
دریافت رایگان تحلیل طلا و ملک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/669585" target="_blank">📅 22:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669584">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
هاکان فیدان، وزیر امور خارجه ترکیه، درباره ایران: وقتی صحبت‌های ترامپ را شنیدیم، برداشت ما این بود که او واقعاً منظور این را ندارد که آتش‌بس به پایان رسیده است
🔹
فکر می‌کنم او اساساً به این اشاره داشت که در واقع یک اقدام تلافی‌جویانه در پاسخ به آنچه بین ایران و ایالات متحده در جریان بود، صورت گرفته است. به نظر من در مورد نحوه اجرای عبور از تنگه هرمز، عدم ارتباط و سوءتفاهم بین دو طرف وجود داشت. آنها نیاز به ارتباط بهتر و مکانیسم‌های بهتری برای رفع تعارض دارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/669584" target="_blank">📅 22:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669583">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu7OVR3B8wIU2j8PBIqsWSoQm-Pts0RJF2l62WnEIxznpnfcca7lJbXj7wy7WpKlw5oKU6P7Vql_nthSyHbOXhiEUcedxX-pPxOnbcI4SwxIG5HS89d0D2lNQqQPX6hVrF1j-rcbRNopSTjytv-VMXu-PZMlCV9X1YQLotbZLj1kK7A7YVCrxpHeS2AIUIhQ-w4jOpDFYACzco5N_5-fWHoah8O2sIAXeaZ54qEsS7NLP89NaNobIRJ6QpflUBN8HxfxvxZWPcIha_Imw-uDuJ373C8qjU2SVZ2U7pv2UqiZwdhhIy19s3mP9s5rq4HVam9YmPUDXD6nMm9MrpQXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش غریب‌آبادی به نقش امارات در تجاوز آمریکا به ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/669583" target="_blank">📅 22:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669582">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
آمریکا دیدار زهران ممدانی با سفیر ایران را لغو کرد
فاکس‌نیوز:
🔹
یک مقام ارشد در دولت آمریکا گفت که زهران ممدانی شهردار نیویورک، برنامه دیدار با امیرسعید ایروانی سفیر ایران در سازمان ملل را داشت که ظاهراً وزارت امور خارجه آمریکا وارد عمل شده و این دیدار لغو شد.
🔹
این مداخله گزارش‌ شده، دومین مورد شناخته‌ شده در هفته‌های اخیر است که دولت ترامپ در مورد تماس‌های دولت ممدانی با رهبران خارجی وارد عمل می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/669582" target="_blank">📅 22:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669581">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a3bb02e4.mp4?token=MkrV3QvwCYw1t2NSQ_OjtXqavEU6jzdSSnoUzx2WHo5_xTKSNatC7goz3XHVTIBLYfDoOjCl9-xGmFK2drUGjeFCr_Xy2u0XZO5SHmTwAgAXfdtSgpESlSqhIwG21ZodVOwWl7hpmqs0OeU2jIYchA4wewq2_mUeOcB6hYo9x5etFrK6JwCCZuE8ArMhV1E-CMJ_yVH_TfhgJC_-CqHlEvJX3DKPdU7jXmpFbnNpOT9aWrx-fEhmPVLpiWRG4_5HXi6ysiW6vATLbdTBkuuUBwDxvU3gkxvL_V83CcoJYW4YeVdfs3akfnyT48-rnCWl0zthvPs8WWqtuqELWdltEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a3bb02e4.mp4?token=MkrV3QvwCYw1t2NSQ_OjtXqavEU6jzdSSnoUzx2WHo5_xTKSNatC7goz3XHVTIBLYfDoOjCl9-xGmFK2drUGjeFCr_Xy2u0XZO5SHmTwAgAXfdtSgpESlSqhIwG21ZodVOwWl7hpmqs0OeU2jIYchA4wewq2_mUeOcB6hYo9x5etFrK6JwCCZuE8ArMhV1E-CMJ_yVH_TfhgJC_-CqHlEvJX3DKPdU7jXmpFbnNpOT9aWrx-fEhmPVLpiWRG4_5HXi6ysiW6vATLbdTBkuuUBwDxvU3gkxvL_V83CcoJYW4YeVdfs3akfnyT48-rnCWl0zthvPs8WWqtuqELWdltEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به رهبر شهید ایران سلام / سایه سیدمجتبی مستدام
🔹
شعار ملت غیور ایران در حرم مطهر امام رضا علیه‌السلام در مراسم بزرگداشت رهبر شهید انقلاب و شهدای خانواده ایشان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/669581" target="_blank">📅 22:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669580">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acad787b0d.mp4?token=J1ybx6KUGCo_LG_nz4qy_pLPbu_qtHmuPYCHEuYBlxUElXApfvtxAqoZzYBgSupsMFKcn6Nd0DACOxIh_FYK1ieGC56EUe9MfF2eHEInFDU2Z7s_7ZwERlCw5ChgqWOYtgb5wvL-EGV3g-f5JdVZZGUgvtCsI9e151dkf3yXAFFlLrmGWibKprYT-Rr_cO8ztbzw5P8qRvtIrOz12ynmX8EpCM-HL4OZA3S-LUqXOKiL4RdMqU3R8KEy1sY_Ac6xDWPFMBGHsOM2pbNgRJKgfaYaF2-xFJ-TtbxXhnK0gN1m_beZOFBwPEndfumaOpk1SH6MSBmjZycbI4WYA2oRWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acad787b0d.mp4?token=J1ybx6KUGCo_LG_nz4qy_pLPbu_qtHmuPYCHEuYBlxUElXApfvtxAqoZzYBgSupsMFKcn6Nd0DACOxIh_FYK1ieGC56EUe9MfF2eHEInFDU2Z7s_7ZwERlCw5ChgqWOYtgb5wvL-EGV3g-f5JdVZZGUgvtCsI9e151dkf3yXAFFlLrmGWibKprYT-Rr_cO8ztbzw5P8qRvtIrOz12ynmX8EpCM-HL4OZA3S-LUqXOKiL4RdMqU3R8KEy1sY_Ac6xDWPFMBGHsOM2pbNgRJKgfaYaF2-xFJ-TtbxXhnK0gN1m_beZOFBwPEndfumaOpk1SH6MSBmjZycbI4WYA2oRWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: تا وقتی که رهبری معظم انقلاب در مورد پایان تجمعات چیزی نگویند، تجمعات خیابانی ادامه خواهد داشت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/669580" target="_blank">📅 22:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669579">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
آقا، دیگه شدی همسایه امام رضا(ع)...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/669579" target="_blank">📅 22:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669578">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4255ffdaab.mp4?token=rLlxTyKrnRY-bwYYwzVVSZOi_n-WwmOZlkgiFdDffr3TWf_iJgCLbyQ79aceJlUO-LhyOLDpCTXYI4ePnIIDcuEao0ukgcxdxH90MTlh03m-7rzBRigNKby8zrkDU9GOymzmVeQmAjzcPKX_2SlUODg0SEUj7P4Fz9Ju_8sH28LCU9aZ5LcLK8G2yoVe_4JLcTvjfYwqdZUOGqWer3cRj827tPjw91yASpo2_OeWQ4olrxR2Qe2Deo-qvMf9CWZqaVMN-lu3cthZSwNzO3MixfV6G6FRS5QEmOpYSYw2EYPgJQd05ojUmFygV5hkXGKMPq0erXecHBhbYAppElT1bHiL4Sq5ACw3TLi1iDPxtzJjF-_d7cqm7c6ettqI7qk5Bk8m_H_Mm6bbXRHk2UhcElSs4R32xnI5mBSglDp_YhPP2CAqPQpMVJCJXr313EwAda0yKsmnnFy-_qufU4hVll19rBu2aLW0yPx1MzOpuh3iTP12V5cOaGBzByDxEQxUTQnAxWSul79d1ZNZnvWvC2HekBUiMLoq1gZMS3ucgz10PuWfqz9531ISod7IBqzRjxchVu88Nu4Pod85JHeeOTgBHgE0zUizLckfFM0KH2hQkQqK17BPtde6Ry-eyKitTeBRv27XX3LTTeHBTPNNFc5ohpM5DemmxVkuupPltac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4255ffdaab.mp4?token=rLlxTyKrnRY-bwYYwzVVSZOi_n-WwmOZlkgiFdDffr3TWf_iJgCLbyQ79aceJlUO-LhyOLDpCTXYI4ePnIIDcuEao0ukgcxdxH90MTlh03m-7rzBRigNKby8zrkDU9GOymzmVeQmAjzcPKX_2SlUODg0SEUj7P4Fz9Ju_8sH28LCU9aZ5LcLK8G2yoVe_4JLcTvjfYwqdZUOGqWer3cRj827tPjw91yASpo2_OeWQ4olrxR2Qe2Deo-qvMf9CWZqaVMN-lu3cthZSwNzO3MixfV6G6FRS5QEmOpYSYw2EYPgJQd05ojUmFygV5hkXGKMPq0erXecHBhbYAppElT1bHiL4Sq5ACw3TLi1iDPxtzJjF-_d7cqm7c6ettqI7qk5Bk8m_H_Mm6bbXRHk2UhcElSs4R32xnI5mBSglDp_YhPP2CAqPQpMVJCJXr313EwAda0yKsmnnFy-_qufU4hVll19rBu2aLW0yPx1MzOpuh3iTP12V5cOaGBzByDxEQxUTQnAxWSul79d1ZNZnvWvC2HekBUiMLoq1gZMS3ucgz10PuWfqz9531ISod7IBqzRjxchVu88Nu4Pod85JHeeOTgBHgE0zUizLckfFM0KH2hQkQqK17BPtde6Ry-eyKitTeBRv27XX3LTTeHBTPNNFc5ohpM5DemmxVkuupPltac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای منتظرانت، صدای خونخواهی‌ است...
🔹
لحظاتی از شعرخوانی حاج محمدرضا طاهری در مراسم بزرگداشت رهبر شهید انقلاب.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/669578" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669577">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
مدیریت جهادی شهرداری در ابر رویداد تشییع امام شهیدامت، جلوه‌ای از خدمت‌رسانی بی‌وقفه و تکلیف مدارانه بود
🔹
شهردار مشهد مقدس، با تقدیر از تلاش‌های مجموعه همکاران خدوم و ولایتمدار شهرداری مشهد در برگزاری باشکوه و بدون حادثه مراسم تشییع قائد شهید امت، گفت: همدلی، برنامه‌ریزی دقیق و حضور شبانه‌روزی همکاران شهرداری موجب شد بزرگ‌ترین اجتماع مردمی بدون هیچ حادثه‌ای برگزار شود و مشهد جلوه‌ای شایسته از خدمت‌رسانی در سطح ملی و بین‌المللی به نمایش بگذارد.
🔹
شهردار مشهد مقدس با قدردانی ویژه از معاون خدمات و محیط زیست شهری شهرداری مشهد و تمامی مدیران، معاونان، مدیران ستادی و مدیران عامل سازمان‌های حوزه معاونت خدمات شهری اظهار کرد: مجموعه مدیریت شهری در این دوره با وجود همه پیچیدگی‌ها و چالش‌ها، با روحیه جهادی و انقلابی خدمات ارزشمندی ارائه کرده است.
🔹
قلندر شریف افزود: سه سال و دو ماه گذشته یکی از خاص‌ترین دوره‌های مدیریت شهری بوده که با اتفاقات متعدد، بحران‌ها و شرایط پیچیده همراه شد و اوج آن، برگزاری یک ابررویداد ملی در مشهد بود.
🔹
برگزاری مراسمی بزرگ با برنامه‌ریزی دقیق و بدون حادثه
🔹
وی ادامه داد: برگزاری این اجتماع عظیم بدون حادثه افتخاری برای مجموعه مدیریت شهری است. تغییرات متعدد در محل، مسیر و نحوه برگزاری مراسم نیز با هدف افزایش ایمنی وامنیت مردم عزیزمان انجام شد و خوشبختانه برنامه‌ریزی دقیق موجب شد این ابر رویداد با آرامش و رضایت مردم به پایان برسد.
🔹
شهردار مشهد  مقدس تصریح کرد: بخش اعظم واصلی اقدامات اجرایی، خدماتی و پشتیبانی مراسم توسط شهرداری مشهد انجام شد؛ از نظافت گسترده شهری پس از حضور میلیونی مردم در خیابان امام رضا(ع) تا فضاسازی، خدمات محیط زیست شهری، حمل‌ونقل، ایمنی و پشتیبانی‌های مختلف.
🔹
قلندر شریف همچنین از تلاش کارکنان حوزه‌های خدمات شهری، فضای سبز، آتش‌نشانی، ایمنی، پشتیبانی و حمل‌ونقل قدردانی کرد و گفت: در این رویداد بسیاری از اقدامات فراتر از وظایف معمول شهرداری انجام شد و مدیریت شهری برای جلوگیری از ایجاد مشکل برای مردم وارد میدان شد.
🔹
وی با اشاره به کمک‌رسانی شهرداری به راه آهن بدنبال اقدام خصمانه دشمن اظهار کرد: در اوج فعالیت اتوبوسرانی مشهد برای جابجایی مردم عزیزمان درشهر مشهد برای عزیمت به محل مراسم تشییع ، شرایطی بوجود آمد که نیاز فوری به جابه‌جایی مسافران راه آهن ایجاد شد، بیش از ۵۰ دستگاه اتوبوس شهرداری مشهد در مدت کوتاهی برای پشتیبانی اعزام شدند تا رضایتمندی مردم حاصل شود.
🔹
شهردار مشهد مقدس تأکید کرد: برنامه‌ریزی این مراسم از ماه‌ها قبل آغاز شد و با تشکیل ستادها و کمیته‌های تخصصی در شهرداری ، وظایف تقسیم شد. در روزهای پایانی نیز مسئولیت کمیته ایمنی به شهرداری واگذار شد و این مجموعه با مدیریت دقیق، وظایف خود را به انجام رساند.
🔹
وی افزود: مشهد شهری متفاوت است و به برکت وجود امام رضا(ع)، هم زائران، هم مجاوران و هم خادمان این شهر مورد عنایت قرار دارند و امیدواریم خدمتگزاران شهر امام رضا(ع) همواره در مسیر خدمت به مردم موفق و سربلند باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/669577" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669576">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b90fcdbbf.mp4?token=RtMs4A0977zC95yNPWtIR5pR7C5jLub91b9SefIrNZFB6H9e6LA6Vu7vntjBhgFzxtYG9g8LyrFQj2MZJuK2lY-XsTPcDtkJQog_v2CGLojLAiTePBykaT9jMqDrJWa4GNV3uLbnDfqreX_ElUZoAQ1PQMSdV0o_ew8-tfqG9iFPoyzStVq-k-6VDjEU25GUAI3ffd7WFnJ7b-A3cIOL4LBWZpCosCp5AtJ94-Sjm5Gn4_mVVoNnOha18Du5YT_j51sATnzsNZ3lPZuOHhHZ7r34WZGR36JBy4vrlvqcj0nFUu81la-N0fcPCBSeOtDBuKfZQtDacxZKZ5YgwqWyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b90fcdbbf.mp4?token=RtMs4A0977zC95yNPWtIR5pR7C5jLub91b9SefIrNZFB6H9e6LA6Vu7vntjBhgFzxtYG9g8LyrFQj2MZJuK2lY-XsTPcDtkJQog_v2CGLojLAiTePBykaT9jMqDrJWa4GNV3uLbnDfqreX_ElUZoAQ1PQMSdV0o_ew8-tfqG9iFPoyzStVq-k-6VDjEU25GUAI3ffd7WFnJ7b-A3cIOL4LBWZpCosCp5AtJ94-Sjm5Gn4_mVVoNnOha18Du5YT_j51sATnzsNZ3lPZuOHhHZ7r34WZGR36JBy4vrlvqcj0nFUu81la-N0fcPCBSeOtDBuKfZQtDacxZKZ5YgwqWyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: هرکس بخواهد مذاکره کند برای اینکه با آمریکا به صلح برسد او خائن است
🔹
هرکس پیام دوستی به آمریکا بفرستد دهانش خبیث و نجس است.
🔹
مشکل ما با آمریکا از زمان کودتای ۲۸ مرداد آغاز شد و الان ما با آمریکا پدرکشتگی پیدا کرده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/669576" target="_blank">📅 22:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669575">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeff1717a9.mp4?token=SPeFG2OZq-_Cfg2fGxXK_MxHrW0RXu7csYImTUAunTCUcnT4SzWW1Iqx_8uRHLLRQTIejIhMz4pxr0_xGn5rDB59h7JpimqhKkPScRJG2dk1ZoqaHsBPSnsFq_3Yb9_XBouTRlii0-P1GzYd8zeqj2m95wjOPkXNeNwqlOUai5S7j7qEPije8jXDUxh04bHJ-PPzvTvv38zP8zA-1pWzIjZNKFpbgJ9utvuEG6R1Gg78gV44wNT3VfqROBGHYMvhFoJ8jD5RBoFstrGPb7VcVs4U02Swe79hmBASYyf3EQD_xjji4uDJOBJPHm-eo2OQh-ryPMPs5QL7UW62Bvc9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeff1717a9.mp4?token=SPeFG2OZq-_Cfg2fGxXK_MxHrW0RXu7csYImTUAunTCUcnT4SzWW1Iqx_8uRHLLRQTIejIhMz4pxr0_xGn5rDB59h7JpimqhKkPScRJG2dk1ZoqaHsBPSnsFq_3Yb9_XBouTRlii0-P1GzYd8zeqj2m95wjOPkXNeNwqlOUai5S7j7qEPije8jXDUxh04bHJ-PPzvTvv38zP8zA-1pWzIjZNKFpbgJ9utvuEG6R1Gg78gV44wNT3VfqROBGHYMvhFoJ8jD5RBoFstrGPb7VcVs4U02Swe79hmBASYyf3EQD_xjji4uDJOBJPHm-eo2OQh-ryPMPs5QL7UW62Bvc9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: هرکس بخواهد مذاکره کند برای اینکه با آمریکا به صلح برسد او خائن است
🔹
هرکس پیام دوستی به آمریکا بفرستد دهانش خبیث و نجس است.
🔹
مشکل ما با آمریکا از زمان کودتای ۲۸ مرداد آغاز شد و الان ما با آمریکا پدرکشتگی پیدا کرده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/669575" target="_blank">📅 22:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669574">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a1e19470.mp4?token=U0sGYlg38D8HOLihdcIm6jeMcbjW4I-HPtnH0axG0_SAxFT0rZzKesbh-CcI9T6X907dTKBCNx01lflQuqMQORHY93gIuQ-UyiEQz2hrVyGAsEM8chT8J7ZPYu8W0ej0TrCbfDwQysMuKN0FPk3KQZzw8LfAlChZnvh9iXMrqUtQXM7NZ6fxYTyTly4vv3vZz05BX-8m-s9w004dus5vIpJ-8rXsUAhdPOBNMrSfnoqlIEK331-JFSQ2ZWvr-ajsQPndyJeulqjGD6NASM_YHeoSiAPDruRvgIeNAxa3-3qSpAe8TOaPxanfXV3TJA0mYzKeL2v4zkv8cn7U4IKkaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a1e19470.mp4?token=U0sGYlg38D8HOLihdcIm6jeMcbjW4I-HPtnH0axG0_SAxFT0rZzKesbh-CcI9T6X907dTKBCNx01lflQuqMQORHY93gIuQ-UyiEQz2hrVyGAsEM8chT8J7ZPYu8W0ej0TrCbfDwQysMuKN0FPk3KQZzw8LfAlChZnvh9iXMrqUtQXM7NZ6fxYTyTly4vv3vZz05BX-8m-s9w004dus5vIpJ-8rXsUAhdPOBNMrSfnoqlIEK331-JFSQ2ZWvr-ajsQPndyJeulqjGD6NASM_YHeoSiAPDruRvgIeNAxa3-3qSpAe8TOaPxanfXV3TJA0mYzKeL2v4zkv8cn7U4IKkaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: هویت ما سازش‌ناپذیری با استکبار است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/669574" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669573">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدیدی علیه ایران اعمال کرد
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا:
🔹
اسامی ۸ فرد و ۶ شرکت را در فهرست تحریم‌های مرتبط با ایران قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/669573" target="_blank">📅 22:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669572">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تلاش‌های دیپلماتیک؛ رایزنی چهارجانبه و سفر وزیر کشور پاکستان به تهران
ادعای الحدث به نقل ازمنابع آگاه:
🔹
برنامه‌ریزی‌ها برای برگزاری یک تماس تلفنی چهارجانبه میان ایران، آمریکا، پاکستان و قطر در روزهای آینده خبر می‌دهند.
🔹
همچنین شنیده‌ها حاکی از آن است که وزیر کشور پاکستان به‌زودی به تهران سفر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/669572" target="_blank">📅 22:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669571">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74c2f8d34.mp4?token=Cm9_66N059UFypTkFvoVQST-4368cggKl7Ch1w8yPauhv3l54R4Y90FGNEeNwhF6i2u-zwAQqqvUtzlsJRbA3ARDyot9lsMUh4JIgyPyf5Q0XqPpYvHawxCmLgfbSv1YwWRpsqnqL6L8eevgmP7g2mOKKSx8oGrKDBbPyrRfCcEfWVtkLZyxTMydDJj-W8wKuXkdWgXzpCgYGPqFAgQf9Z4GKfl8lR4NBU8fQPpa5_kTS0mr_UL74KTa7mqperfF3E9uaGIi4KGDJjFa6tdXM-Cv0agIUdGVCAYDZ7b4-RveFNyshJxg3rty6JCpIivoDTTYO8ztLwDhoiZAG3aiLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74c2f8d34.mp4?token=Cm9_66N059UFypTkFvoVQST-4368cggKl7Ch1w8yPauhv3l54R4Y90FGNEeNwhF6i2u-zwAQqqvUtzlsJRbA3ARDyot9lsMUh4JIgyPyf5Q0XqPpYvHawxCmLgfbSv1YwWRpsqnqL6L8eevgmP7g2mOKKSx8oGrKDBbPyrRfCcEfWVtkLZyxTMydDJj-W8wKuXkdWgXzpCgYGPqFAgQf9Z4GKfl8lR4NBU8fQPpa5_kTS0mr_UL74KTa7mqperfF3E9uaGIi4KGDJjFa6tdXM-Cv0agIUdGVCAYDZ7b4-RveFNyshJxg3rty6JCpIivoDTTYO8ztLwDhoiZAG3aiLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: کسانی‌که از جنگ می‌ترسیدند فهمیدند که جنگ هزینه و مشکل دارد اما ترس ندارد؛ ترس از جنگ بدتر از خود جنگ است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/669571" target="_blank">📅 21:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669570">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پتروپالایشگاه پلدختر
🔹
عصر امروز حادثه آتش‌سوزی در یک مینی‌پالایشگاه در پلدختر رخ داد؛ به‌دلیل ماهیت مواد اشتعال‌زا و گستردگی حریق، عملیات مهار با دشواری مواجه شده و نیروهای امدادی و آتش‌نشانی با وجود استقرار در محل، به‌دلیل شدت شعله‌ها امکان نزدیک‌شدن به کانون اصلی را ندارند و تمرکز فعلی بر جلوگیری از گسترش آتش است.
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/669570" target="_blank">📅 21:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669568">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efaa83718.mp4?token=NxnJFfY-_lIzM-9WnoK9p9hnv3uWOkeJMbiBaQsJpsnKEKtKMbiIJ3DLVuXO0JyLooZL-NXk4ZO4VtYmX0Kg1AYuyBqyJVBB5j449H_HPfwLb-95Ecsx0-xS6bnmOZCLV7JLAwaaVb0aUeFipiwi7eF8DDfDYNnrNzFLiSbwadASPvO6xhuL6vVRLqUrERTc6k_PGYHVNTJ5rt7D3HNG_LMwx3DqjwfrgHNxMW0ojIcP6ncEDo2Nnc_R6s6GrnT43yr4e_K6xwv3PE4ieSqXLkyryhonQEA6SUaps6v8UHsgEmHT_Qdh6Jn6P7Z1Bim4dVRf9pdpjYBGQNdRdmRE2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efaa83718.mp4?token=NxnJFfY-_lIzM-9WnoK9p9hnv3uWOkeJMbiBaQsJpsnKEKtKMbiIJ3DLVuXO0JyLooZL-NXk4ZO4VtYmX0Kg1AYuyBqyJVBB5j449H_HPfwLb-95Ecsx0-xS6bnmOZCLV7JLAwaaVb0aUeFipiwi7eF8DDfDYNnrNzFLiSbwadASPvO6xhuL6vVRLqUrERTc6k_PGYHVNTJ5rt7D3HNG_LMwx3DqjwfrgHNxMW0ojIcP6ncEDo2Nnc_R6s6GrnT43yr4e_K6xwv3PE4ieSqXLkyryhonQEA6SUaps6v8UHsgEmHT_Qdh6Jn6P7Z1Bim4dVRf9pdpjYBGQNdRdmRE2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما مدعیان صف اخر هستیم
از اول مجلس امام‌مان را چیدند...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/669568" target="_blank">📅 21:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669567">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46d096a489.mp4?token=vlpGnLOdDl-budcddYYN1UUXUZ9ttMEXY1kSB8uenuEvJKlXICPnalhNDpXAOs1muzTyYXT2vjgGZFOUsAZs9loV_-xfhe1LLsmz8D9W7MYsIosIebysS1ni7-rmKKnk9kmCvnEndd2yhW2u7CiKuF8WhEaLOD1E5eH8QZHKhuBLjN-Y6raPmE9Mxu8yMRtmicL-sMXhO_DB9ZnRTFzXQnj9rJwK3eOKgORCW6GY5q8PPxHZAxy6gEE06Ck1NsxzjtHRSedTThMn5HcKGqwwfX6HYp_Gf8UKBhP1hx6u5tj_POgjWGjiVuj8GWJ3PBOTxMdWnNiI1_lZspdpDwRTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46d096a489.mp4?token=vlpGnLOdDl-budcddYYN1UUXUZ9ttMEXY1kSB8uenuEvJKlXICPnalhNDpXAOs1muzTyYXT2vjgGZFOUsAZs9loV_-xfhe1LLsmz8D9W7MYsIosIebysS1ni7-rmKKnk9kmCvnEndd2yhW2u7CiKuF8WhEaLOD1E5eH8QZHKhuBLjN-Y6raPmE9Mxu8yMRtmicL-sMXhO_DB9ZnRTFzXQnj9rJwK3eOKgORCW6GY5q8PPxHZAxy6gEE06Ck1NsxzjtHRSedTThMn5HcKGqwwfX6HYp_Gf8UKBhP1hx6u5tj_POgjWGjiVuj8GWJ3PBOTxMdWnNiI1_lZspdpDwRTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: گفتنِ احمق به ترامپ، فحش نیست؛ این صفت اوست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/669567" target="_blank">📅 21:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669566">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b01cee5cd0.mp4?token=hrHZAbKBudGlcSS5ufqT6k7SjM3qrWRyGDIvqXLZYA8MbNlOtksnjtdp-E0NE-MiJ2ScfUrC7M-F4PpsxaEMnyQSqCfyiewTQ4yLr0CvUkPJXfjedYbDk3Tlnf6-GY5QHu_re2aSu20KzgnjCBHDQlDAj9KHlWLc6t5wV_QGiIph_lmTA9uyKDuejBZxFfUICt-_MwMHkMCM8NJRomR2pbxS-bj3837nsWO8pMXHEvDlSuOg1mXD3Ex7zGk8PU3qc-fKNkEEvSpYWrnHMZtroZtRFONyHkpsxV4AHFX0TBVmfmM_nAzJh8P5hXuFY_hTUYuFZaGGyGYFfoaoWObxHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b01cee5cd0.mp4?token=hrHZAbKBudGlcSS5ufqT6k7SjM3qrWRyGDIvqXLZYA8MbNlOtksnjtdp-E0NE-MiJ2ScfUrC7M-F4PpsxaEMnyQSqCfyiewTQ4yLr0CvUkPJXfjedYbDk3Tlnf6-GY5QHu_re2aSu20KzgnjCBHDQlDAj9KHlWLc6t5wV_QGiIph_lmTA9uyKDuejBZxFfUICt-_MwMHkMCM8NJRomR2pbxS-bj3837nsWO8pMXHEvDlSuOg1mXD3Ex7zGk8PU3qc-fKNkEEvSpYWrnHMZtroZtRFONyHkpsxV4AHFX0TBVmfmM_nAzJh8P5hXuFY_hTUYuFZaGGyGYFfoaoWObxHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرآن‌شناسی و تاریخ‌شناسی؛ از خصوصیات رهبر شهید انقلاب
🔹
لحظاتی از سخنرانی حجت‌الاسلام والمسلمین ناصر رفیعی در مراسم بزرگداشت امام مجاهد شهید و شهدای خانواده ایشان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/669566" target="_blank">📅 21:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669565">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e59948529.mp4?token=MsMENoGSwEWJ7idLUaeboamQHzYF-7Xm8PYdGhMBe6PJMC9i9j4tFs70iH6JomFuyIhG6LU08NMd0fbXdZY-f0r6K5_E08WKuBqyk4B2yXTtDYMnwW61DNt6oGx-pBwr3grOPkDU3niN_kCSjcJobGjEDgKk7vd0YsL-HqQK8qUvlkkcFSJm-RrzmZOXye0lQuJhBvbsRdshc2t0EK5D5C4fjUuVUv8u2-vFmy2YXnejRg-MrEzqp8v2TuaPaOX8tCgWEmQG3xAeTrE5bz_qU45LhpHFXLioaEzNvF8QCiCsNrNvYN3zLfPA9hgfpSvCEYPGYvw-arl_gdU3mJX3Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e59948529.mp4?token=MsMENoGSwEWJ7idLUaeboamQHzYF-7Xm8PYdGhMBe6PJMC9i9j4tFs70iH6JomFuyIhG6LU08NMd0fbXdZY-f0r6K5_E08WKuBqyk4B2yXTtDYMnwW61DNt6oGx-pBwr3grOPkDU3niN_kCSjcJobGjEDgKk7vd0YsL-HqQK8qUvlkkcFSJm-RrzmZOXye0lQuJhBvbsRdshc2t0EK5D5C4fjUuVUv8u2-vFmy2YXnejRg-MrEzqp8v2TuaPaOX8tCgWEmQG3xAeTrE5bz_qU45LhpHFXLioaEzNvF8QCiCsNrNvYN3zLfPA9hgfpSvCEYPGYvw-arl_gdU3mJX3Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: آن مسئولی که بخوابد و در فکر انتقام رهبر شهید نباشد، باید به وجدان خودش شک کند #تقاص_خواهید_داد  #WillPayThePrice #خونخواهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/669565" target="_blank">📅 21:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669564">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBO5iTxLNtHt2UpXuhnap-5zUH331jMNEojv0Hjw_7K7Hn7f9_uHIcL4KWmfUQY6cawDV5axrpL6z-smn5toFQI-7VBO2jog9NUwIHzoXsDhZNa3cLmPHFr7DFTyUVdeQk9TRO2xlvkGTNotB3SSAOzKtTCereYqvq71OuaRo6V4C4_PrVGTPu1fI6GEljqi7l9Gx6uuI9pK-es_Teyz8sbQw-grtJ0W0LhdIcFqhulWrFa2YKLZVmWlL0t6Z3x4zIM72q2wDvLhTOw5WI4pph9bdAze1gUiQbeoxN0K6xSB3W2-sGQtUPKccWbho4UrWf2b2J3xGG8BQaeWKXxyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‌
مرندی: ترامپ و آکسیوس را نادیده بگیرید؛ تا وقتی دولت ترامپ به تعهداتش عمل نکند، هیچ مذاکره‌ای انجام نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/669564" target="_blank">📅 21:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669563">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd534735e.mp4?token=dckkyQ1US3BqgL5XhGHnHWOTUAaNGVh-dMMtESDkL4mxQ6bcx_JOlon09XAbmPgar1-BhvQKwJvqtSKl-n9Wv5ORpAWLwzjggrpNjcBj4Vo8OfJZtuR2ZP8NT9LWqbhXQk0Ib_DwA3XDSkjORpFDjgDwuzWJth_TlocWbTWkBM_38jw_Pgi_SmTIopGgu9zt2xsnnaQi2C6Hs4PnOdQmXBNhBkECFRF1eLbtH2QYTD-JQFTRgTON0Hc6CsmbDQQfk6Ybp_9F5Cp-bxe7xL9gyooiXEsRFeGGhIuCEau96DoyBpoybNLwePvF5rDTnA0-o-xCqIYtJjL7AOsTvyPPPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd534735e.mp4?token=dckkyQ1US3BqgL5XhGHnHWOTUAaNGVh-dMMtESDkL4mxQ6bcx_JOlon09XAbmPgar1-BhvQKwJvqtSKl-n9Wv5ORpAWLwzjggrpNjcBj4Vo8OfJZtuR2ZP8NT9LWqbhXQk0Ib_DwA3XDSkjORpFDjgDwuzWJth_TlocWbTWkBM_38jw_Pgi_SmTIopGgu9zt2xsnnaQi2C6Hs4PnOdQmXBNhBkECFRF1eLbtH2QYTD-JQFTRgTON0Hc6CsmbDQQfk6Ybp_9F5Cp-bxe7xL9gyooiXEsRFeGGhIuCEau96DoyBpoybNLwePvF5rDTnA0-o-xCqIYtJjL7AOsTvyPPPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدری مهربان از دست دادیم…
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/669563" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669562">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14cfb7b2f7.mp4?token=FuD7ghnpKKylBsCbiLt-mMn_9gAUdqnHiWY-b_jxbBebIdpKqGwsT-tN6eZqL3IsJMz9Jen3QdBeyk1Ay_aiafsXrGsystDLyeot4By4XwimRqKsZXKBnq2bvDM0-4nkNLh2rxWC9-nrtJubwnLmOqBWbM-mKx4wud6ui_joJ8Bg83JpRhnSyfDnZu3S86A1G5R03T1W6E6Mp4abG1PHt3Mig25SDIJxXfSIhGbMJBdESh4B9SAl-btVZKDTNCqXFWKumImpAuhTv8AtfGouUls_1m_AgIQZepcSKOvDpn5WAb27-kYM-TAoRt5XBQ96nsZ8S1HsIqO7_gHeN7gMPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14cfb7b2f7.mp4?token=FuD7ghnpKKylBsCbiLt-mMn_9gAUdqnHiWY-b_jxbBebIdpKqGwsT-tN6eZqL3IsJMz9Jen3QdBeyk1Ay_aiafsXrGsystDLyeot4By4XwimRqKsZXKBnq2bvDM0-4nkNLh2rxWC9-nrtJubwnLmOqBWbM-mKx4wud6ui_joJ8Bg83JpRhnSyfDnZu3S86A1G5R03T1W6E6Mp4abG1PHt3Mig25SDIJxXfSIhGbMJBdESh4B9SAl-btVZKDTNCqXFWKumImpAuhTv8AtfGouUls_1m_AgIQZepcSKOvDpn5WAb27-kYM-TAoRt5XBQ96nsZ8S1HsIqO7_gHeN7gMPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی: آن مسئولی که بخوابد و در فکر انتقام رهبر شهید نباشد، باید به وجدان خودش شک کند
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/669562" target="_blank">📅 21:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669561">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416316e983.mp4?token=BvGPrBs4sIXAfHpn-NTrFXHwQvmurzAyKbJj_vgKf6OAlwJVIsD0rsPP8wJbEJd1FH1iMYRuChz80FLP0TyMnw6vAhe0gAhR10DblkPfo91ykOBowXmLK68-aVHnoSuix76dxmZ1qXkKab_UCmT4tmhK3Ev4l3kz7K-6qf_T57PveYoImymo1JqauOWCkQP9zy_tOU5udWSM32tuh2Brjn_31X7vkFBFrKt9Q_J-pP60zJeDJw6Ixc2E6RE1b-UgEgV1mlwos--5JMTPasPljUdZCruDWhWaJpLeigYj1CP_WV7zQbYnVIHo5ObUCuMrzwCPu3LBkqhExextdqpVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416316e983.mp4?token=BvGPrBs4sIXAfHpn-NTrFXHwQvmurzAyKbJj_vgKf6OAlwJVIsD0rsPP8wJbEJd1FH1iMYRuChz80FLP0TyMnw6vAhe0gAhR10DblkPfo91ykOBowXmLK68-aVHnoSuix76dxmZ1qXkKab_UCmT4tmhK3Ev4l3kz7K-6qf_T57PveYoImymo1JqauOWCkQP9zy_tOU5udWSM32tuh2Brjn_31X7vkFBFrKt9Q_J-pP60zJeDJw6Ixc2E6RE1b-UgEgV1mlwos--5JMTPasPljUdZCruDWhWaJpLeigYj1CP_WV7zQbYnVIHo5ObUCuMrzwCPu3LBkqhExextdqpVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقا خداحافظ...
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/669561" target="_blank">📅 21:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669560">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0731ae7a39.mp4?token=MYkRUsntqFfHgbRVY5w8Jf8rwvI8GoyOY_c4HhaFjFil2xeOMQv3pHrv6ponlTxZ2TStGbnozriX0io-PRYEfPf2FJH8ksv-Qa_9YmZ1fhYg8BZ8IsncMgFketi3EbhUTxjCT3T6Ay20Xs6S-hpfM4z82QdaklJqbpUlleiEeIFYv65hzDGygUj_Iavhzuv040Sy498tvvgMsZhVZZTi_24Y_P8lwtdSx4dN0LAsJc6tmwSfv6An6iiWQW3VSv-ftozqh9mQj5p3u5pQdRgKQCzW9ZSybsJB8zOGoykogH4YqQlyqzBnwrv_x4cSyGgP2rSQje9kFTu0BYFBog17Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0731ae7a39.mp4?token=MYkRUsntqFfHgbRVY5w8Jf8rwvI8GoyOY_c4HhaFjFil2xeOMQv3pHrv6ponlTxZ2TStGbnozriX0io-PRYEfPf2FJH8ksv-Qa_9YmZ1fhYg8BZ8IsncMgFketi3EbhUTxjCT3T6Ay20Xs6S-hpfM4z82QdaklJqbpUlleiEeIFYv65hzDGygUj_Iavhzuv040Sy498tvvgMsZhVZZTi_24Y_P8lwtdSx4dN0LAsJc6tmwSfv6An6iiWQW3VSv-ftozqh9mQj5p3u5pQdRgKQCzW9ZSybsJB8zOGoykogH4YqQlyqzBnwrv_x4cSyGgP2rSQje9kFTu0BYFBog17Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داغی سنگین در حرم رضوی
🔹
تصاویری از حضور حجت‌الاسلام محمدی گلپایگانی بر مزار دختر ۱۴ ماهه‌اش، «زهرا».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/669560" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669559">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
بنفسى انت، بروحى انت، بِمُهجَةِ قلبى انت
...
🔹
قرائت دست‌نوشته عاشقانه رهبر شهید انقلاب در وصف امام حسین علیه‌السلام در مراسم بزرگداشت امام مجاهد شهید و شهدای خانواده ایشان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/669559" target="_blank">📅 21:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669558">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت بهداشت لبنان: آمار شهدای حملات رژیم صهیونسیتی به ۴۳۲۱ نفر رسیده است.
🔹
یک هواپیما سبک در فرودگاه شارون در سرزمین‌های اشغالی سقوط کرد.
🔹
کشورهای اتحادیه اروپا ممنوعیت واردات از شهرک‌های صهیونیست نشین را بررسی می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/669558" target="_blank">📅 21:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669557">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
روایتی از غم و حسرت در تشییع مشهد
🔹
صحبت‌های بانوی لامردی در مراسم تشییع ۸ میلیونی پیکر رهبر شهید در مشهد خطاب به رهبر شهید امت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/669557" target="_blank">📅 20:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669556">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
تکذیب شایعه انفجار در قائمشهر
🔹
بررسی‌های میدانی حاکی از آن است که اخبار منتشرشده درباره وقوع انفجار در شهر یا سپاه ناحیه قائمشهر کذب بوده و در زمره عملیات روانی دشمن قرار دارد./ تسنیم
#اخبار_مازندارن
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/669556" target="_blank">📅 20:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669555">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf679ab26.mp4?token=aYbhssPmnrVfIJRx6pLHeYgiH3eEjA-FUUtN3TTloNPakKMan0dabAQj4fsPJ9V0ygCXO5ab-c-GWW2qfwQf7oWKDzk9KAaboDczfyzyQkJXUedXcz43T47QffG1PUNC6hWmTSfA6tTyXKmniH4f8PjCZ4IlK6P2aMlIkPxwA-EULDtfICMsvCNiHxs6cnESxIbWneWWhkdfToWInvN4UhteXS65P3xXHZVFGj7EkDCpuhuDeAAu8LoxwGn1PjTKffAWHK3Qd5_fK240taVToTsR8yxoGOLAQSav1YIictYRtlzD43Nm7TwiAnVi4bMueU5q_EEC_uDppr92SoWWhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf679ab26.mp4?token=aYbhssPmnrVfIJRx6pLHeYgiH3eEjA-FUUtN3TTloNPakKMan0dabAQj4fsPJ9V0ygCXO5ab-c-GWW2qfwQf7oWKDzk9KAaboDczfyzyQkJXUedXcz43T47QffG1PUNC6hWmTSfA6tTyXKmniH4f8PjCZ4IlK6P2aMlIkPxwA-EULDtfICMsvCNiHxs6cnESxIbWneWWhkdfToWInvN4UhteXS65P3xXHZVFGj7EkDCpuhuDeAAu8LoxwGn1PjTKffAWHK3Qd5_fK240taVToTsR8yxoGOLAQSav1YIictYRtlzD43Nm7TwiAnVi4bMueU5q_EEC_uDppr92SoWWhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار «مرگ بر آمریکا» زائران عزادار در رواق دارالذکر
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/669555" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669554">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a9bbba72c.mp4?token=ZPjq_Kqdj04Nb5ibr_Dyd0lZUMcmzheVMUZ_Jbz2p8rWhsTr1hG_oHEjjPogurBUusVEUZzUKobWhUAhpmAdrZPCUrHTDUaB8_ld47mtD3U19wZYGnBKYm3GbMFwFzQPDxdZmB9ZTaATeWwUyyrOwInRQu9O0yshfaW0xwgaG7d00H6ugLawcKdyMFcrb9yifPz8T1TPhboIetUsJ1C4CMt3GTjmQXijRnQogpQKYLivduQzfsGR08zgXehjWIOmHrQlPrJkeZ-aiMZ4LTG9hpOKuX5wO96ik7AXRRvmypN6Cwn56y7lM-aNG_hKmyYPzJF4U7yA9t3w6Cmd4c3VEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a9bbba72c.mp4?token=ZPjq_Kqdj04Nb5ibr_Dyd0lZUMcmzheVMUZ_Jbz2p8rWhsTr1hG_oHEjjPogurBUusVEUZzUKobWhUAhpmAdrZPCUrHTDUaB8_ld47mtD3U19wZYGnBKYm3GbMFwFzQPDxdZmB9ZTaATeWwUyyrOwInRQu9O0yshfaW0xwgaG7d00H6ugLawcKdyMFcrb9yifPz8T1TPhboIetUsJ1C4CMt3GTjmQXijRnQogpQKYLivduQzfsGR08zgXehjWIOmHrQlPrJkeZ-aiMZ4LTG9hpOKuX5wO96ik7AXRRvmypN6Cwn56y7lM-aNG_hKmyYPzJF4U7yA9t3w6Cmd4c3VEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان امام رضا(علیه‌السلام) مشهد و جمعیت ۸ میلیونی حاضر در تشییع دوباره تاریخ ساز شد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/669554" target="_blank">📅 20:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669553">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
شهردار مشهد مقدس از ثبت رکورد تاریخی مترو مشهد خبر داد؛ جابه‌جایی ۲ میلیون مسافر در ۴۴ ساعت سرویس‌دهی مستمر
🔹
محمدرضا قلندرشریف، شهردار مشهد مقدس، با قدردانی از عملکرد جهادی کارکنان شرکت بهره‌برداری قطارشهری مشهد، ثبت رکورد جابه‌جایی ۲ میلیون مسافر در جریان مراسم تشییع پیکر مطهر رهبر انقلاب را حاصل برنامه‌ریزی دقیق و خدمت‌رسانی مستمر این مجموعه دانست.
🔹
وی اظهار کرد: «در راستای مدیریت سرویس‌دهی در ایام مراسم، شرکت بهره‌برداری قطارشهری مشهد از ساعت ۶ صبح روز چهارشنبه تا ساعت ۲ بامداد روز جمعه (در یک بازه خدمت رسانی ۴۴ ساعته)، سرویس‌دهی مستمر خود را با حداکثر ظرفیت آغاز کرد. در جریان این بازه، تنها در روز اصلی مراسم (پنجشنبه)، تعداد ۱,۰۱۴,۹۰۷ مسافر جابه‌جا شدند که با احتساب کل ۴۴ ساعت فعالیت شبانه‌روزی، مجموع مسافران جابه‌جا شده به مرز ۲ میلیون نفر رسید. لازم به ذکر است که این میزان جابه‌جایی در شرایطی انجام شد که میانگین جابه‌جایی روزانه مسافران در شرایط عادی ۳۰۰ هزار نفر است.»
🔹
شهردار مشهد افزود: «این حجم از خدمت‌رسانی در شرایطی محقق شد که شهر با موج گسترده حضور عزاداران از سراسر کشور و محدودیت‌های شدید تردد در سطح معابر اصلی روبه‌رو بود. در چنین شرایطی، مترو مشهد با اتکا به توان فنی، تجهیزاتی و سرمایه انسانی خود، توانست با مدیریت هوشمندانه، نقش شریان حیاتی و اصلی در مدیریت سفرهای درون شهری ایفا کند.»
🔹
قلندرشریف با تقدیر از مدیران، کارکنان و تمامی عوامل مجموعه بزرگ شرکت بهره‌برداری قطارشهری مشهد گفت: «این موفقیت بزرگ، نتیجه همدلی، انسجام، مدیریت میدانی و تلاش بی‌وقفه همکارانی است که با روحیه‌ای جهادی، طی این ۴۴ ساعت به‌صورت مداوم و بدون وقفه، در بالاترین سطح عملیاتی در خدمت مردم، زائران و عزاداران بودند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/669553" target="_blank">📅 20:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669552">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dc68004.mp4?token=aZsR8w3xUV536af3d-OW3aiblWHyBYK-gy_0wLLAsmNr-0LlX5146YZ9-PwXJ3TeghJaWVs9H17NBB6_wa5WZ-WOwqk--bYOVIXAlIdsz_7DjGuED5R2zwmKlvNemOYovD_eXU2XGB2FFvn7OnGpD7z7OXvZG6vzfeu9P60wa-JMRernTpwtXYJu0lWtIW5VrPR8eHhQDIELZAlYJkO00PUIVdK7R7W9cwdww27vay8UkmeuBwiXYJeGfVUXuE-JcFuDTFNxm9Hbx2-mBIN6JMTTO1pB_jCHVPt-663YjrH8H_k8snrLrO4b8oioLdPoqBB_yO9Ua0PcwSMCLO94pKWwkRc-y9qpfkkxu98Tpl0yNDuSmW1U-IziIs-Zo2TVE4dAmo2kqFCoK946bdcJ4BlJbV69KIwgLQr_zcm3R0h-nnIm9DasrjQN3tZ6ZokcMoi7PafNzD-A3WCYkFhP6KTXeCS6qnbQRPvPFBNpIOGnzTZwTav4f35mh0cRmCUtKTYES5ZOKELXur2KHknkl5PxX2LdpgkIFpU5QOPFDpngfPjIkbbm4My0lbDWazuLwFnGpJZc_lpP5SfZQvbmZe4JSj4Oh2-qY4Xe9Jtpvug0Qp6hwD7f5eN8IcKhWMEcwqVZbvp-ItyPokNObV4RR8koNIod4obYYD0hlDTwHCc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dc68004.mp4?token=aZsR8w3xUV536af3d-OW3aiblWHyBYK-gy_0wLLAsmNr-0LlX5146YZ9-PwXJ3TeghJaWVs9H17NBB6_wa5WZ-WOwqk--bYOVIXAlIdsz_7DjGuED5R2zwmKlvNemOYovD_eXU2XGB2FFvn7OnGpD7z7OXvZG6vzfeu9P60wa-JMRernTpwtXYJu0lWtIW5VrPR8eHhQDIELZAlYJkO00PUIVdK7R7W9cwdww27vay8UkmeuBwiXYJeGfVUXuE-JcFuDTFNxm9Hbx2-mBIN6JMTTO1pB_jCHVPt-663YjrH8H_k8snrLrO4b8oioLdPoqBB_yO9Ua0PcwSMCLO94pKWwkRc-y9qpfkkxu98Tpl0yNDuSmW1U-IziIs-Zo2TVE4dAmo2kqFCoK946bdcJ4BlJbV69KIwgLQr_zcm3R0h-nnIm9DasrjQN3tZ6ZokcMoi7PafNzD-A3WCYkFhP6KTXeCS6qnbQRPvPFBNpIOGnzTZwTav4f35mh0cRmCUtKTYES5ZOKELXur2KHknkl5PxX2LdpgkIFpU5QOPFDpngfPjIkbbm4My0lbDWazuLwFnGpJZc_lpP5SfZQvbmZe4JSj4Oh2-qY4Xe9Jtpvug0Qp6hwD7f5eN8IcKhWMEcwqVZbvp-ItyPokNObV4RR8koNIod4obYYD0hlDTwHCc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلبسته یاران خراسانی خویشم...
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/669552" target="_blank">📅 20:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669551">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW5YbUXcDZlS8BXNAdbCGtcn8FuVHVGcSpy3EL377CrC9DyH8hLZb2WG812oMWas7H5N5RiK4MnhCv5o2aHmWLnufOBXhmA7XEd4EEB_0nF5q_duidWNd1TVGggom1N_R371Nu1NyPGZF82CBgWNl76tMgsN8-56Epv9UlNM8NVFgYXIJlIpD3GFBZyXnI90OqkqUrES-GHNz4kUt48aY_K7lkkqAW-g75LhffBVfle5gy5EKihSEusmVs1pRLSHhWh_0SYTR0AmJI_NNI9r79LWNe42SrXALOrATYkpR72drAvSNxqDNV6eLUd4QnSfRM4BFw_LFTxYeLBGx54MOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از پزشکیان و ناطق نوری در مراسم ختم پدر محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/669551" target="_blank">📅 20:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669550">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
قرائت زیارت امین‌الله در اولین شب پس از تدفین رهبر شهید انقلاب در حرم مطهر امام رضا علیه‌السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/669550" target="_blank">📅 20:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669549">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
روایت هولناک زنی که هنگام نماز روحش از بدن جدا شد
🔹
00:09:40 عطر عجیب شکوفه‌های چادر روح خواهرم
🔹
00:13:10 القای ذکر "یا ستار"
🔹
00:24:50 حضور موجود سیاه در خانه‌ام به جز حریم سجاده و قرآن
🔹
00:34:30 قرائت سوره انشراح در عالم برزخ
🔹
00:37:30 پرده‌برداری از شخصیت اصلی خواستگار توسط روح مادربزرگ
🔹
00:47:15 عاقبت خوردن مال یتیم
🔹
01:00:00 فریاد ملتمسانه درخت از بازماندن ذکر خداوند در هنگام شکسته شدن
🔹
01:07:50 گرفتار شدن شهید در برزخ به دلیل حق‌الناس‌های دوره نوجوانی‌اش
🔹
قسمت سی‌ام (بی‌نهان)، فصل چهارم
🔹
#تجربه‌گر
: خدیجه مبینی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/669549" target="_blank">📅 20:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669548">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
قالیباف: تنها کسانی می‌توانند با آمریکا مذاکره کنند که آماده جنگ باشند
🔹
محمدباقر قالیباف در دیدار با رئیس مجلس خلق اندونزی، ضمن تأکید بر بی‌اعتمادی کامل به آمریکا، اعلام کرد شرط مذاکره با این کشور، آمادگی برای جنگ است. وی با شکست‌خورده خواندن محاسبات آمریکا، اسرائیل و ناتو برای تسلیم سریع ایران، این تلاش‌ها را بی‌نتیجه دانست.
🔹
در مقابل، رئیس مجلس اندونزی ضمن تأکید بر صلح‌طلبی ملت ایران، از تمامی تلاش‌های دیپلماتیک برای پایان دادن به درگیری‌ها استقبال کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/669548" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669547">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ddc860633.mp4?token=Cq8QEmza7qSZ9z-h7Gydu9dDBiq8ujLZ9CUsstIyyewKGvonZ4hTNzBJm_qbOcswEGmXMtYNh9AthnPEvH3nSw54JOQprK216kSNwwtzVT_GcrfNlwKewA4tLPod8Sgm_WelA0TrEvQtT2ePAbztbKJEWlkST5w8-_MtGu3JkWW3pVsm75cOk4KYxyyZQKM8D5sTtF4g8njeHbEsobvCJd0PG8yhfsn-yznxLBSrvk9LF0sy1pVGIzzkljU0I7W7Bj7J2OqvpNpDx3GqGNQmvFJCBCB2TqpjjePoPjbFWjc-FJtQEyQJxAVGwuBpzY10B8kewGftdFoonfR805PJvR6T_YUvBeL3ScKMZBsE6xl6LWis6CCKgnD7LtUTtXOj_Ut9DoN-TN6FKm5AFsY6iLyEqzBrnUlXs0Bi5PYVa5w7_X5eSO63nnqAHoOV_ytvooiGU4flK-M38A51hAvZ2M3DE4e1ljAxQy8kWKx3JX67QRg9YiKfaA7Nb0LapdVKOfQasWrOr9vYO1aJZK6rmfNvkrakx05MmyeyQgB4BYOAsbH9VzOF3K1wv63GY5B3Jo7U5yG-KNuko4lchE59ngu23kfzjqCbPg0uPIsQjvsCFSCAWj3BIu8RS2VvPOgnNSFSENmU6n3hT7HQ2uFYjCnk2i_4UfdfPGE_GSGvrgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ddc860633.mp4?token=Cq8QEmza7qSZ9z-h7Gydu9dDBiq8ujLZ9CUsstIyyewKGvonZ4hTNzBJm_qbOcswEGmXMtYNh9AthnPEvH3nSw54JOQprK216kSNwwtzVT_GcrfNlwKewA4tLPod8Sgm_WelA0TrEvQtT2ePAbztbKJEWlkST5w8-_MtGu3JkWW3pVsm75cOk4KYxyyZQKM8D5sTtF4g8njeHbEsobvCJd0PG8yhfsn-yznxLBSrvk9LF0sy1pVGIzzkljU0I7W7Bj7J2OqvpNpDx3GqGNQmvFJCBCB2TqpjjePoPjbFWjc-FJtQEyQJxAVGwuBpzY10B8kewGftdFoonfR805PJvR6T_YUvBeL3ScKMZBsE6xl6LWis6CCKgnD7LtUTtXOj_Ut9DoN-TN6FKm5AFsY6iLyEqzBrnUlXs0Bi5PYVa5w7_X5eSO63nnqAHoOV_ytvooiGU4flK-M38A51hAvZ2M3DE4e1ljAxQy8kWKx3JX67QRg9YiKfaA7Nb0LapdVKOfQasWrOr9vYO1aJZK6rmfNvkrakx05MmyeyQgB4BYOAsbH9VzOF3K1wv63GY5B3Jo7U5yG-KNuko4lchE59ngu23kfzjqCbPg0uPIsQjvsCFSCAWj3BIu8RS2VvPOgnNSFSENmU6n3hT7HQ2uFYjCnk2i_4UfdfPGE_GSGvrgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما را به سخت‌جانی خود این گمان نبود...
🔹
شعرخوانی حاج میثم مطیعی در مراسم بزرگداشت رهبر شهید انقلاب و شهدای خانواده ایشان در حرم مطهر امام رضا علیه‌السلام.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/669547" target="_blank">📅 20:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669546">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhrFtoAbg6_ZKemLWdIxF2H0HmG0p4uJ-uYHwTdPAs2nGN1paAv4ng7a-OEwvRvKO0rajMAcHjmUQAx2jr2S0mK5a51k7EDK9znhMFbiaRzYHCXSJaO7Yjbt9GcGhPs77tR_IXTjytPHWWdEsUrN6lvoyE2BSSN3YgcGXFcI5-fQmE8iNGlXtU8ZqFFRjsYisjWsI2I4d6J7Z7JaQqq2hn73XiSciZ7lGq_LVnBJWEwESfoZZIE37LuialATIZ7aEVBEyul5_SLRmXJwSJ-keq_MxwVyX6N4SYDeu4rfTATTx990kcZx0Eljv7vbQ-4n8Fbbc7gqIiChNRULR16NMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با توجه به اینکه پیکر مطهر رهبر شهید انقلاب اسلامی حضرت آیت‌الله العظمی سید علی خامنه‌ای اعلی‌الله‌مقامه‌الشریف و شهدای خانواده ایشان سحر گاه جمعه ۱۹ تیرماه دفن شده‌اند، مؤمنین می‌توانند اعمال مستحبی مربوط به شب اول دفن از قبیل صدقه و نماز لیلةالدفن را به امید ثواب پس از اذان مغرب روز جمعه (شب شنبه) هم بجا آورند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/669546" target="_blank">📅 20:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669545">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d9791b8c.mp4?token=aehq_8Yw2kpSOZw8AaK0_JzIrxcsT9HOHQeOhg5PtXFhYswqXbMVrqknc7nsB9s51gXUnIcqKX4LDfrfoB_ZqpIl2rSPqQl0Yd7Ijm8vnamJZr3RgobhkvUQtMH5LT-1_369nKNIqUI7hiSKfJ3hoLJW3_0toMsHiM8AuWJUOU4WfDsxW4rAfZiT5RWT4rZudn9UcxLJ9hcdZRnpU7rbq3DjBHm4ztBOPMBF9TFl6X6HKTFw5wiKD_R_cR2zSIdWAoMLi7CeQG8Oi5manWY6wBqk7Vjoyvuxv2soLDy104bHI2T_6mBBeR8e0C6mLI1-II9XNwtg6wgu8WKx_E310g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d9791b8c.mp4?token=aehq_8Yw2kpSOZw8AaK0_JzIrxcsT9HOHQeOhg5PtXFhYswqXbMVrqknc7nsB9s51gXUnIcqKX4LDfrfoB_ZqpIl2rSPqQl0Yd7Ijm8vnamJZr3RgobhkvUQtMH5LT-1_369nKNIqUI7hiSKfJ3hoLJW3_0toMsHiM8AuWJUOU4WfDsxW4rAfZiT5RWT4rZudn9UcxLJ9hcdZRnpU7rbq3DjBHm4ztBOPMBF9TFl6X6HKTFw5wiKD_R_cR2zSIdWAoMLi7CeQG8Oi5manWY6wBqk7Vjoyvuxv2soLDy104bHI2T_6mBBeR8e0C6mLI1-II9XNwtg6wgu8WKx_E310g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاوت آیاتی از کلام‌الله مجید در مراسم بزرگداشت رهبر شهید انقلاب و شهدای خانواده ایشان در حرم مطهر امام رضا علیه‌السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/669545" target="_blank">📅 20:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669544">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
این حمله آمریکا به ایران خبر از یک جنگ جدید می دهد
🔹
ترامپ بارها گفته که اگر ایران شرایط ایالات متحده را نپذیرد و آمریکا مجددا وارد جنگ شود، این بار پل ها را هدف قرار خواهد داد. این تهدید ترامپ نشان از این دارد که ممکن است در صورت ازسرگیری جنگ، شاهد نبرد کریدورها باشیم.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3229282</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/669544" target="_blank">📅 20:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669542">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
نمای دیگری از مزار مطهر رهبر شهید انقلاب در رواق دارالذکر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/669542" target="_blank">📅 20:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669541">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پاسخ به چندتا سوال ساده میتونه تو این روزای بحرانی سرمایه‌ خیلی‌ها رو نجات بده
ما در حال بررسی دغدغه‌های مردم درباره امنیت سرمایه توی شرایط بحرانی هستیم. تجربه و نگاه شما می‌تونه کمک کنه این مسئله بهتر فهمیده بشه و راه‌حل دقیق‌تری براش درست کنیم.
اگه چند دقیقه زمان دارید، خیلی خوشحال میشیم، این پرسشنامه رو پر کنید.
تکمیل پرسشنامه
ممنون که توی ساختن یه مسیر امن‌تر برای سرمایه همه هم‌وطنامون همراه ما میشید.
❤️</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/669541" target="_blank">📅 20:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669540">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9075da9719.mp4?token=ZYqiIUnuVaJ2LRhv8M9SSB_qvlQZjeVJxM3Pmtl_4AqCzZl9Bc2qTsdZtPXi0JEzsLuvLfWyC3UNUHhQnxZ3JY3EX4HynVe_hBXVJYK7ogALdCPuhg-zlO348SNV6ZWbJ3_xjTY_oklNSmbIa6qlGhScT9sUquTeQjxG38P_G7ogBGyISSfSKKaruuq1PlS4D0JG4mxjNPrBg0-5thXIIbsJsMU56omsr18CZjXr5d4uLglSm_o-Pu7-ku35T5PnrKZVWWWRmOjoydaYfp8rkUwVGG0xzvQ0khmMAfMZnstSVKzpK6exA23xD5yPt1dXtfyCXMwUd_Z1FPqEzFZntA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9075da9719.mp4?token=ZYqiIUnuVaJ2LRhv8M9SSB_qvlQZjeVJxM3Pmtl_4AqCzZl9Bc2qTsdZtPXi0JEzsLuvLfWyC3UNUHhQnxZ3JY3EX4HynVe_hBXVJYK7ogALdCPuhg-zlO348SNV6ZWbJ3_xjTY_oklNSmbIa6qlGhScT9sUquTeQjxG38P_G7ogBGyISSfSKKaruuq1PlS4D0JG4mxjNPrBg0-5thXIIbsJsMU56omsr18CZjXr5d4uLglSm_o-Pu7-ku35T5PnrKZVWWWRmOjoydaYfp8rkUwVGG0xzvQ0khmMAfMZnstSVKzpK6exA23xD5yPt1dXtfyCXMwUd_Z1FPqEzFZntA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقامه نماز لیلة الدفن رهبر شهید در حرم مطهر رضوی
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/669540" target="_blank">📅 19:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669538">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c806945c6.mp4?token=YURbtgPFqC2VzgFk1s8CN4dFi6L8aOyHt21_Y7UhsYWB470nOBpbM-oFxvX4m1Q2IJPyssDWKpcgyzHpNkQ4S3xDi_nQuhtZARt-Am6lvY6qwE6XIx1Nb_JBENycpD07nA5oHXRHsVZNeGJ2GTeuZsU_eFFPR4NCzpkpYRy6ck38iS_9MZjy9MDENMG-PRWHjFApqzfJCzCI5JJ-MrDmU7P54ATcJafME_nDRy0tjxtxe3e7ESBWZzsgwtuz_K7hvOXReOWM-sXu26GxpsUDfsCqAXjCgo8vq-1z18522p_jB6AMbJRuQ-xMU7x1uxmIUfa2npDCy0Y0hoSiIsPNbz9pzdQGQIlOM2sex5wqLk33ptCZoCmhUXxJUysLCrgju3xq8umts2CPEqrV6xkGQ5T2YWTllrF_P-QoLqEd7IdrMJOnMim2hoEueItJoJ8_f0_8vuylSDJNBPCb6vd3pG6OvJ9sUcKaBcBTELdUKAt0Whb-OWZ-2v2ZBhXhMVZQxwGYWgg0VAxEPKQ_EHXguRwSZUF71NNy4IO1EK6smiwo4zTwMQzn3BHfutA_ImvqFSzWTTaFINOlTw2H1Oej0DkWzzfuodNzzRS5fvG3yT4sAIj7jeO5s-kbHiyrDlFQGGntBamIJI73IfETYj5VaHD5SlWVJh9VFrUzme1uLA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c806945c6.mp4?token=YURbtgPFqC2VzgFk1s8CN4dFi6L8aOyHt21_Y7UhsYWB470nOBpbM-oFxvX4m1Q2IJPyssDWKpcgyzHpNkQ4S3xDi_nQuhtZARt-Am6lvY6qwE6XIx1Nb_JBENycpD07nA5oHXRHsVZNeGJ2GTeuZsU_eFFPR4NCzpkpYRy6ck38iS_9MZjy9MDENMG-PRWHjFApqzfJCzCI5JJ-MrDmU7P54ATcJafME_nDRy0tjxtxe3e7ESBWZzsgwtuz_K7hvOXReOWM-sXu26GxpsUDfsCqAXjCgo8vq-1z18522p_jB6AMbJRuQ-xMU7x1uxmIUfa2npDCy0Y0hoSiIsPNbz9pzdQGQIlOM2sex5wqLk33ptCZoCmhUXxJUysLCrgju3xq8umts2CPEqrV6xkGQ5T2YWTllrF_P-QoLqEd7IdrMJOnMim2hoEueItJoJ8_f0_8vuylSDJNBPCb6vd3pG6OvJ9sUcKaBcBTELdUKAt0Whb-OWZ-2v2ZBhXhMVZQxwGYWgg0VAxEPKQ_EHXguRwSZUF71NNy4IO1EK6smiwo4zTwMQzn3BHfutA_ImvqFSzWTTaFINOlTw2H1Oej0DkWzzfuodNzzRS5fvG3yT4sAIj7jeO5s-kbHiyrDlFQGGntBamIJI73IfETYj5VaHD5SlWVJh9VFrUzme1uLA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت سه خواهر برزیلی در کتاب گینس
🔹
سه خواهر برزیلی به عنوان مسن‌ترین خانواده جهان در کتاب رکوردهای گینس ثبت شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/669538" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669537">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تکذیب شایعه مذاکرات جدید ایران و آمریکا
یک منبع آگاه در تیم مذاکره‌کننده ایران:
🔹
ادعای العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات در هفته آینده کذب است./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/669537" target="_blank">📅 19:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669536">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ce956558.mp4?token=XggMJFY0SOC8c84o-5CXS9TAX_TNBGJb6Rg4V75BEb_WwdoaQPKyDHIa7xmpsRpjOkPNFPWMUmWNlpL2Zz6f0s0hBeJIfUXwUW3hyMWc6YL-No2iwwet1XnrudHna_YaR9vDDBkAkxIadwcflEN0t0ah5n5insfCPATyrHdiXC3v-He29GqJoGhvHBUVWPz_MNjD1sKFEYbmlbFPZRvgCCVq7zChqmFFV__icKaXwkRoRhMMTs0G-Eg_GnNun6PkqNxmZ6Gi0jaMSOGEbhxDXhcW0TFAji5xd0743l2sSSDJ7L8pc2rjIUDdPwRIo3Bnt1jm19VA1OkSgXNvzeAF64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ce956558.mp4?token=XggMJFY0SOC8c84o-5CXS9TAX_TNBGJb6Rg4V75BEb_WwdoaQPKyDHIa7xmpsRpjOkPNFPWMUmWNlpL2Zz6f0s0hBeJIfUXwUW3hyMWc6YL-No2iwwet1XnrudHna_YaR9vDDBkAkxIadwcflEN0t0ah5n5insfCPATyrHdiXC3v-He29GqJoGhvHBUVWPz_MNjD1sKFEYbmlbFPZRvgCCVq7zChqmFFV__icKaXwkRoRhMMTs0G-Eg_GnNun6PkqNxmZ6Gi0jaMSOGEbhxDXhcW0TFAji5xd0743l2sSSDJ7L8pc2rjIUDdPwRIo3Bnt1jm19VA1OkSgXNvzeAF64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوهٔ خردسال رهبر شهید انقلاب، شهید زهرا محمدی گلپایگانی همراه پدربزرگ خود، حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای در یک مزار به خاک سپرده شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/669536" target="_blank">📅 19:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669535">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c832ce6082.mp4?token=NSIF1OpwW7MtkOAx_5snBFkBeKJ3yc81esAN57kmp_0U1vO-i0EpRg0POZVKwz1n92Nw9Ea9d22a6NrmCFHhJSzS9v_rPPFRwaWwUZUl_nGB7ZMu6wcHmL_LeRzZyqT2H0VEvXLNCHpDQxieTESxpxfuqezCMWnhzmlmzDxUBRYHu8RVtt2Ju1a6SEDzGNuF2W0Fsa9DLATStNRq-joNljCKz2xhlmfuVKrcalelrPv1DcMhtP9i0ebkwrT1_2Qyv9UaFVbQjuOlK1e-pUWyw0t_c4rhIRmmdjpXjGCJeaMLiOvkiVzIeb38f776Hxe67MtFuhOIGB-scQ4haFBEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c832ce6082.mp4?token=NSIF1OpwW7MtkOAx_5snBFkBeKJ3yc81esAN57kmp_0U1vO-i0EpRg0POZVKwz1n92Nw9Ea9d22a6NrmCFHhJSzS9v_rPPFRwaWwUZUl_nGB7ZMu6wcHmL_LeRzZyqT2H0VEvXLNCHpDQxieTESxpxfuqezCMWnhzmlmzDxUBRYHu8RVtt2Ju1a6SEDzGNuF2W0Fsa9DLATStNRq-joNljCKz2xhlmfuVKrcalelrPv1DcMhtP9i0ebkwrT1_2Qyv9UaFVbQjuOlK1e-pUWyw0t_c4rhIRmmdjpXjGCJeaMLiOvkiVzIeb38f776Hxe67MtFuhOIGB-scQ4haFBEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای زیبا از تشییع ۸ میلیونی رهبر شهید انقلاب در مشهد
🔹
کمک امدادگر به یک زائر سالمند هنگام نماز ظهر.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/669535" target="_blank">📅 19:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669534">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقام ارشد سازمان ملل: دیپلماسی همچنان تنها مسیر ممکن رو به جلو در خصوص ایران است.
🔹
اشپیگل: آلمان نیروهای خود را از شهر اربیل خارج خواهد کرد.
🔹
قطر بر حمایت از توافق جامع میان ایران و آمریکا تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/669534" target="_blank">📅 19:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669533">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfrXttDWo1LFSr3Kl6R6_e5PJ-3yYTe6u8Lh6T0dngsC0jyDKuknlGggmTlquL6HK3lTblWTYqXy-Ocdnb5bLo0gf6a6qdjJfg0DaVz8g0YKGRbB6u64GJXc749QiMuMi14SDqKaRtD92k5twWsWPP54YLuMbrmezbKgbB-WlthMJMRSBFEESnqu2xyDdSBXShSajjw2mK0Zg0JgTFMAkxw7VzpK1cAPNZIapPTK5zN6BpDIMpraEdkAUPLg6hSnv-yIk_PmCbk43eclEnJLUxdYxqiZpnaD6_MWUzwFtPtcEVJ0IHpdlXHIXl-RsnbuFvvD8WpOw_JuQfXGnRyVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️
♦️
بازیکنانی که در یک دوره جام‌جهانی بیش از ٨ گل به ثمر رسانده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/669533" target="_blank">📅 19:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669532">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnvr0KKcw8E4CqxmxXbs0J_3gxyfydQ6NPPiUn5dRxA7xrVaxbMh6FA2ODyvPonHD4Y4IpkruEoabPSqsh7ZHYsfXqMW3NTrEQCkjz6xMXR8W6VSn-abwqSiqzlcSqbfjrvx2DMqKSTvKKBsQEk7nXTKep3gQwBDGTT5jeBXbYrnkBNBodSn3E4Pi-WnoXAIkdyD19pFz1BPXFvdxmHAYKEZw3FI5phFrCdKPLnvwjO_yshoisXkBQeX-QnQW_koNsrEt0PHszIud-5MEJ6U1thU6j95-CtdOX5QEtGe0F9sfvdLYGBQ1jn1xdlpaOGghHRWEZZIBKT5fHW--rJsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه آشنا به سعید جلیلی
🔹
۵ حق ملت و وظیفه دیگر مسئولین را به ترتیب اولویت نام ببرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/669532" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669531">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
بلافاصله بعد از غذا ۲ لیوان آب خوردی؟ داخلش قشقرق به پا میشه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/669531" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669530">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای آکسیوس: هفته آینده مذاکره ایران و آمریکا در سوئیس
🔹
رسانه آمریکایی-صهیونیستی آکسیوس به نقل از یک منبع آگاه مدعی شد:
انتظار می‌رود دور جدیدی از مذاکرات ایران و آمریکا هفته آینده
و احتمالاً به میزبانی سوئیس برگزار شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/669530" target="_blank">📅 19:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669529">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0W2LyLHqWj9tBnXIQQOi9jwnGCz1rY6zFC7ADRDM3fzGTHLNLXWduMXPD3DS8KVMFeG8vk8CIrCBPpxjwAV-jsWRee1V6Z7TUcL5drwHVazDqZ6DdVBAOerZydlAhr4D5eb-sd2rbLIoYSb014j68DLyF32NE1AdFHGU6ggaaQ8D7Vmq_3ROVHhqbxnf5ofEg2VxDYrK9pXo0Tz7okAWGxIHOHVR9pSrABv6rTLtxP-Tp4v0k73ebo6Yh_-PCCuK68lkIF1EhEx_oElnHd0eYEk0LSA1BgfGZ6UBWu017l5-tOL826ScWswbNvfD-hOzUBMpT33qIZRtcAaYWRIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ تیم حاضر در مرحله یک‌چهارم نهایی جام جهانی، از سال ۱۹۸۶ به بعد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/669529" target="_blank">📅 19:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669528">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q14276Gps1KbI6UkK1Q4zw0xWL2P9uwyIcFpcT0H7dCjLG_koFVKFYJotQUZYUGCYYXgaSeFCuIM278r1LJQKn89BBNGipCb0ejFK243SmvdpXgiYOwAR1v4L-x3Sn-zosk1GD9bodfge5v5U_du72ZM8Ypw24KNmVmRsFSxYDOrW4ltPyY-Kf8Ut5KZgKSBOiQ-li5mCxO1Wto0FfNPNoMN21bvF7On60b_9H2CBfJNYEmnkC4-lwpH62ZnYkrISWLoUXWVlbyEXXHnxGg5wOcPW9DzUjy1zHJVSePDcDszlWgOk7vzlX3PsJVjMr6gmFVEAgle1Ho0zP_2Z48dHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/669528" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669527">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/669527" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669526">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f37a4c15.mp4?token=ZBQSh_MzKj_j1wbOj8ttsL0duIb9aZVHxbNMp-PJKsjqgkYoGTwo2zADso5bCeMREhkdRzBvk_kf68Ta6L4MYxhMm13mqbmMMy1yonKyvaj_FMvnRSB3Yk3cx7iqnZVmCdMfnrPoRNZtJFd-GJ_INouBK-R_O7HCU1CKXRa2fJ-LU5XBDF1N99Pj9CUXthFXuZpwGLUC34l7avtfCSh70cSJsEMgspxyTrZJR0JAEP7m_b7FgM5aYCc0fxIxB3jTghZlwa-RNyypnZTPwhGmFk9nYEpluiEPMyZUhu19tfRjEb32RtUWPH0GgTBAmVc_mugYz-eX45tqOIuKkYbjWRukRi0cJjYojFXWk_WOvPHUZhPWjSChjqF8So4ofB5KOqGMlEJ7933vOlxSd3mRpTpdSd8k1kh1_ATjhqfhhbZvZ6-lghqYPePSTxhoN4kiTi0uwT_NgJxJ5qD_NuP4iSg22vo4Qasc6UFXMVoXkaclCpihNRyrhn_4sSIVIxG5-cFVgkw0y-bpbd5lE7gJers3W2JtciXFE3nyBYnkPY5rtZBsrBi-icfxb0zMSRT6Il9qq7i1cOc01HfC6wXNANFoOqFZgqVWOHGUl6Qij5j5AO28Buyiwao2LNZE5ls14WqL0V4kDVwS9UxejNzJG-1sj265ocnP9KM62NMOf7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f37a4c15.mp4?token=ZBQSh_MzKj_j1wbOj8ttsL0duIb9aZVHxbNMp-PJKsjqgkYoGTwo2zADso5bCeMREhkdRzBvk_kf68Ta6L4MYxhMm13mqbmMMy1yonKyvaj_FMvnRSB3Yk3cx7iqnZVmCdMfnrPoRNZtJFd-GJ_INouBK-R_O7HCU1CKXRa2fJ-LU5XBDF1N99Pj9CUXthFXuZpwGLUC34l7avtfCSh70cSJsEMgspxyTrZJR0JAEP7m_b7FgM5aYCc0fxIxB3jTghZlwa-RNyypnZTPwhGmFk9nYEpluiEPMyZUhu19tfRjEb32RtUWPH0GgTBAmVc_mugYz-eX45tqOIuKkYbjWRukRi0cJjYojFXWk_WOvPHUZhPWjSChjqF8So4ofB5KOqGMlEJ7933vOlxSd3mRpTpdSd8k1kh1_ATjhqfhhbZvZ6-lghqYPePSTxhoN4kiTi0uwT_NgJxJ5qD_NuP4iSg22vo4Qasc6UFXMVoXkaclCpihNRyrhn_4sSIVIxG5-cFVgkw0y-bpbd5lE7gJers3W2JtciXFE3nyBYnkPY5rtZBsrBi-icfxb0zMSRT6Il9qq7i1cOc01HfC6wXNANFoOqFZgqVWOHGUl6Qij5j5AO28Buyiwao2LNZE5ls14WqL0V4kDVwS9UxejNzJG-1sj265ocnP9KM62NMOf7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ تشرف زائران عزادار به رواق دارالذکر برای زیارت مزار مطهر رهبر شهید انقلاب اسلامی.
۱۴۰۵/۴/۱۹
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/669526" target="_blank">📅 18:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669523">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icXXzrL6vrsQBad4asYL5aBUDxKToLhyUfDNmjQH6s9NLeZDulf-xGEsFqXEhSFdHucMoqtDth8poqnHhGoCELoiNYb7wAH_94NL2SRF-UuNlOJLz_N9Wwthvgz7ZT5Nc0N1vhfbXdqzTuNCOu6Z0XfszS0eLN1p6KzwOY2ZppVdDdr0ZICRqs5GptQwAEGSbDaYDF0_Fzv5H88A0JCWIS6tbFDQ1Bp2-O70uJzJTztgo1VaUBxci8-cpGigoLA_zOzPlF8VPNjOqzFqCvqGS6iIIzVSY84L4j0HwGwKQFZ_qqsSAnYoErEkhw1RgNjFmdtE3TwAlj9Ne8mzpHCNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNQe-UHjai5fpqgR_klMT985K7-Ctuc6Jwk4p1LzlGhq38beMZm5MNRpwxQHPZgg0oAS_eRpugPxa6e3zQadsFvqZXEgnwcg49JsNeteHjroVglCw9JLCFFksAX3WUCDo8pQfgCpdUKZNl-IJkhReugEq2TjVsi8VqiDzt_9gWbzve-SkLvFw9aQQC1yGlNOEAfhwHi1qQJVEFo53nHZYLs9Yipx53moGkpNn4ZirqQYfY4g50J9FUJZISECyxGQ0BV7Ug0zZKG49iGlag5GPGhLApYfo82u5NFU631bjV9bDAne-bBfImeQ2-bvlh9t4rDBuQtAAVGba1VejaSLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4SXIUpli_ZS1KIkJpiX8u8Vboe1em501rH13dXrna_ETzcaAz_L-QHe9cMsf7tUswEVJyuVAb_BmIQnehGbjFZuO0tjasCRLxqOJbwo_E1zj9_aRlLQtW_UCwHVI1j2KJQcfq9ZXHNLo0SwSZ5HO4UCi5YH8b_DmoSH3B3miBsTBp5FV5zgXiOSz1M_G98Ts07YEw5BoY0PLWMOoQT9kA7EqGBVh9LYMDcfnLmHCbj6qOvf41TUUce1duOStnQhJjp2bZlF0xTBMf7xHv8_05K40AgPJhoOdcLOeUFGZlGhU3yNp62o30nQJBnErb_STfnoVlYXVNn2VEKwCbfnzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خودنمایی پرچم ایران در تجمع امروز یمنی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/669523" target="_blank">📅 18:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669522">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
نماینده چین در شورای امنیت: قطعنامه ۲۲۳۱ منقضی شده و بررسی پرونده هسته‌ای ایران پایان یافته است  نماینده چین:
🔹
قطعنامه ۲۲۳۱ در ۱۸ اکتبر ۲۰۲۵ منقضی شده و رسیدگی شورای امنیت به پرونده هسته‌ای ایران پایان یافته است.
🔹
اصرار برخی کشورها برای برگزاری نشست درباره…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/669522" target="_blank">📅 18:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669521">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
خوک زرد: من دستور بمباران بی‌سابقه ایران را در صورت موفقیت در ترورم صادر کردم
🔹
هیچ برنامه جدیدی از سوی ایران برای ترور من وجود ندارد و تهران سال‌هاست که می‌خواهد مرا بکشد.
🔹
مدت‌هاست که هدف اصلی در فهرست ترور ایران هستم و اسرائیل هیچ اطلاعات جدیدی ارائه نکرده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/669521" target="_blank">📅 18:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669520">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بندر دَیّر داغ‌ترین شهر جهان شد
🔹
براساس آخرین آمار پایگاه بین‌المللی هواشناسی «Ogimet» که وضعیت دمای ایستگاه‌های هواشناسی جهان را رصد می‌کند، بندر دَیّر در شبانه‌روز گذشته در صدر فهرست داغ‌ترین نقاط زمین قرار گرفت.
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/669520" target="_blank">📅 18:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669519">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نماینده فرانسه در سازمان ملل: ایران باید حمایت از گروه‌های مقاومت را کنار بگذارد/ ایران تفاهم‌نامه را نقض کرد.
🔹
مصر و قطر خواستار بازگشت واشنگتن و تهران به مذاکرات شدند.
🔹
تیم المپیاد ریاضی ایران قهرمان چهارمین دوره مسابقات بین‌المللی ریاضی در شانگهای چین شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/669519" target="_blank">📅 18:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669518">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWXPVWsLx6ICmUck8QR969vzTVUt96TqB8kJRZiITvH_sd4Vuvmg821kPPMHuzhOTG3AYrtpRvgcU2YdE5KpV003K-wO32MYdGo3gVA10qLOlg08KAcqnPK-bL2h2C1ukWIKyuo836xHZBzJL_JC4Ts0KQF-qRv7NJgrKSuoju0taxYpTblNACQmlCI14rXBl3qeXppA1UZSiVgb4i5IBJApny5IzncgtivSF9L4GPz0YcMKZGCCFV9paZR63IMlkl7Fef6LdvE82Y0Ej97E8OxGuW_smH6U64tzK9vhaHYnJiOP1cVnxkCLEVzsddf_6BpwYA0VQ5IXi3ZwIkC2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روی جلد نشریه اشپیگل: محور شرارت!
🔹
تصویر روی جلد این شماره اشپیگل با عنوان "محور شرارت" با اشاره به اسنادی محرمانه به برنامه‌ریزی راهبردی، تبادل اطلاعات و همکاری‌های دفاعی روسیه و چین برای مقابله با نفوذ غرب اشاره دارد. همکاری که می‌تواند بر موازنه قدرت جهانی تأثیر بگذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/669518" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
