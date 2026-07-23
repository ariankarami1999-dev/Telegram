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
<img src="https://cdn4.telesco.pe/file/aGa7Uuia01jEtuYV7xOPdB6eiKQG4hZUonMIbsCV6dRXUKGSxpTaezX8-Xop-JP-X6khihyd1mOmivul6FHBI-B1hJFcd95wgbWg1e1pQezBRvJIq5Qsm9tM3U178-tWc8lob7juy3qnvacn0psVOF8-vZ47ujyJ97kqFRYN_Qx1uCd9aeSfw3fHdTP_xY4RrIV6W0yhoXZAwq8Fq0ua11eSrFrYvG39gAtrnk-Ef-8sebNyv_ptckRLtDEPe30GISO9HGs_BsCdiep00hfh8TY2sK3KQ6d1zLYqc-6xlA6_LDBBmJzhayoHsR1LQByqDJ0Uu-dDaAXhLdlc6i7UVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 11:27:00</div>
<hr>

<div class="tg-post" id="msg-674416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac176b643d.mp4?token=iZuxxVPr9Aat6cy6q96rf6iCvxDz1BMpRGmdiy9sMKZ97gGfx7mORECVoAEe76SaqUyoFx02uak_f--eOXs1RdAEdbX84M9wJRx_TY-3krEmHtnQyS93ypbxrGTGvZA_1VJyOwWVxgfNPhreshD_dF_v8-_QXXR94AzZQLDoAILAHvB__8v3ywhL_FPoCaVLxhAkAgfAygXUq0OhGnwOVpRbRvlhS2nhN7rRg32mXhzUE9KhXKkXmcBBSoVzZdQwwzAusr5YflQ8UuRUixY7rI9Nk3gwCU6DWN4GRPmcd1p8C-ACfVYXiOSIQfyiV7lcJ89SvmezAuQ6ixX4b_YDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac176b643d.mp4?token=iZuxxVPr9Aat6cy6q96rf6iCvxDz1BMpRGmdiy9sMKZ97gGfx7mORECVoAEe76SaqUyoFx02uak_f--eOXs1RdAEdbX84M9wJRx_TY-3krEmHtnQyS93ypbxrGTGvZA_1VJyOwWVxgfNPhreshD_dF_v8-_QXXR94AzZQLDoAILAHvB__8v3ywhL_FPoCaVLxhAkAgfAygXUq0OhGnwOVpRbRvlhS2nhN7rRg32mXhzUE9KhXKkXmcBBSoVzZdQwwzAusr5YflQ8UuRUixY7rI9Nk3gwCU6DWN4GRPmcd1p8C-ACfVYXiOSIQfyiV7lcJ89SvmezAuQ6ixX4b_YDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طراحی خیره کننده Z Fold 8 ؛ گوشی تاشویی که نظر همه را به خود جلب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/674416" target="_blank">📅 11:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3f584299.mp4?token=fAmThZYTId1P3h-zdNvsi-LbsH8-T0x4m10OPqw-k3cKqKxKRGosMySnf8216L1O0L70ZCKagUccCxw0bKlNFqb1dTXUbXm7SDj_JAP63yMBHe4obNbl7k--d8TbidqqiwMw5IJoEv6aH0saPYTcpsPs-vPa6-v6Ha0YFjCu4hMqL5TeVVHHNnfi4fKBcqasbu7pP8EdodVAtdrgEBQod-nSmunjZ3JDEXo4Z2SJaqgL90hZzcFQQiGzzQkpjHMABQNbTP0l-sZojMnJVY7Ghp9y0doV7IYOmOpJEqp7vR22gdvFaqKFy_s8I5tc39aII5YDIO-UC0qvz0YVeRnstQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3f584299.mp4?token=fAmThZYTId1P3h-zdNvsi-LbsH8-T0x4m10OPqw-k3cKqKxKRGosMySnf8216L1O0L70ZCKagUccCxw0bKlNFqb1dTXUbXm7SDj_JAP63yMBHe4obNbl7k--d8TbidqqiwMw5IJoEv6aH0saPYTcpsPs-vPa6-v6Ha0YFjCu4hMqL5TeVVHHNnfi4fKBcqasbu7pP8EdodVAtdrgEBQod-nSmunjZ3JDEXo4Z2SJaqgL90hZzcFQQiGzzQkpjHMABQNbTP0l-sZojMnJVY7Ghp9y0doV7IYOmOpJEqp7vR22gdvFaqKFy_s8I5tc39aII5YDIO-UC0qvz0YVeRnstQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویدادی عجیب در سخنرانی ترامپ؛ تقلید همزمان!
🔹
مردی که پشت سر ترامپ نشسته بود، با تقلید دقیق حرکات، حالات چهره و حتی جملات او، به سوژه داغ رسانه‌ها و شبکه‌های اجتماعی تبدیل شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/674415" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0b85691a.mp4?token=kjoPeXtqclVoZPw8U6sh2bD_LmkjTroJPCWlVGWW9Gk5fXzzBbAWr2maMxx0J9q0I2QjB4Ab9jmx4BluKr219M142tMLfl3ckc4RRjgArECQFqlTP0oVbhgfRBN03mB4GOOdOQjk_2aT0xd73Vv3T1iyjlt21kIrkfveHcZamVw9SFehpGh2PrS2z3897ILJHzwcSeUGAjXZzJ5GAhiW01noBu4a6J8ru-OYUpzBpymgqWoZ-q8yCYbXdaspjC4yyogXoEtRF4coPyn7X8qvhAxCf4Z8NMV6ZQ9lCHj7X4YwLWbakJasI33sZW649Iv785DIEoHsnhfnSWGRPpn_Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0b85691a.mp4?token=kjoPeXtqclVoZPw8U6sh2bD_LmkjTroJPCWlVGWW9Gk5fXzzBbAWr2maMxx0J9q0I2QjB4Ab9jmx4BluKr219M142tMLfl3ckc4RRjgArECQFqlTP0oVbhgfRBN03mB4GOOdOQjk_2aT0xd73Vv3T1iyjlt21kIrkfveHcZamVw9SFehpGh2PrS2z3897ILJHzwcSeUGAjXZzJ5GAhiW01noBu4a6J8ru-OYUpzBpymgqWoZ-q8yCYbXdaspjC4yyogXoEtRF4coPyn7X8qvhAxCf4Z8NMV6ZQ9lCHj7X4YwLWbakJasI33sZW649Iv785DIEoHsnhfnSWGRPpn_Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر نفتکش عربستانی که دیشب توسط یمن زده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/674414" target="_blank">📅 11:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
برخی منابع خبری عربی از شنیده شدن صدای انفجار در قطر و اردن خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/674413" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674412">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_ghM3wLM6cbzC4L-XYiN3uhzZUtjnUlysZSsvWAPrRpUhMzEbzEom9npGTXveUTs15vZelGyZjvRBHLLgb22YAjd5K0RcJxVcxFYeBjdu7uT52_IV4g_R8CssXicY6qE0N4_Zy7C36Mz1KP0bs5qrOMa5q0AxI1lANC7FfA4O3LaFDbYg-yE63-d8ZyTXCLHDCV-_zDW-LhyvxDCbYlq4sBNQen7YTQlDKfkqDsYbPWrE5HPq3FZrR1Jz--KyqaQNupsheLhtHeFlUwISDceY3dYqLl_8BMJbrW0aMEcPOHTU7-QERUXaQtmucOg_BdiUBvqG1A8JbIi-JZPPCfaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش قیمت نفت به بیش از ۹۷ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/akhbarefori/674412" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674411">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
چندین موشک از مناطق مختلف کشور به سمت پایگاه های آمریکایی شلیک شدند‌ /
صابرین نیوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/674411" target="_blank">📅 11:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiS0UuV3IEhcw5QFAIY1A2PdshRySWk3lIKAZk8XTh8Kpjv1JiRyh6RHrXcWvpNFM5WhGBcPB8ftKX5Udruvbu2P-_srAH288YE8jNcyA_-Dga8MNEoEZG4Has5YQmoU0voNKy7gC8gqHuxnG_v5pKFn_3hEqAxw_uR9o35cv5q45R-xP_h-0iwZWhfgkjfo1IyPhXwmAN28TmOzj00VAcI1MOMdAIcCYoUKxwq7l0kBmcxAod6pHG_Je2IBhC17GFWjimmTf_Hxb0n_Ee2nixVXhVSHP_uA_N2HqSOgQr9KRce71B6yN9wyAJrKiu8Yndi8Knjr3MObmCDoQ7imag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست‌وزیر عراق عازم تهران شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/674410" target="_blank">📅 11:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674409">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f44763d92.mp4?token=VprS8z-lDLZ_XvQs6bIDu9TK_WvUjDhsJql18CQH2x-rqQjbp5E4embFfc-w0l71C4S9ekq_pvdAKuEdg7tf5pnRPjUvAIL97meynlcjR_HHSX3KYxdVHBI-2hbQPeigYqsa4Q5y3HB1pZG3nOi-iHBqqQgIlz4x6HiTFz4Mih6i3Ak_ZQHcbbJTyDQFtQXdwrSd4fFpG6_OlfS4CzNxzzH4RHiaxJx74HEzIH8EXt7UrOoFhu6vj5cdLA8bbtNGSUb_7k0TYu1PiFVgSNmd9uToLJvti2Hibzg8Tt2k3ky4NfiKx-CrltfNaptYTRpZJ5IjCv08YiFV0cmyORPMMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f44763d92.mp4?token=VprS8z-lDLZ_XvQs6bIDu9TK_WvUjDhsJql18CQH2x-rqQjbp5E4embFfc-w0l71C4S9ekq_pvdAKuEdg7tf5pnRPjUvAIL97meynlcjR_HHSX3KYxdVHBI-2hbQPeigYqsa4Q5y3HB1pZG3nOi-iHBqqQgIlz4x6HiTFz4Mih6i3Ak_ZQHcbbJTyDQFtQXdwrSd4fFpG6_OlfS4CzNxzzH4RHiaxJx74HEzIH8EXt7UrOoFhu6vj5cdLA8bbtNGSUb_7k0TYu1PiFVgSNmd9uToLJvti2Hibzg8Tt2k3ky4NfiKx-CrltfNaptYTRpZJ5IjCv08YiFV0cmyORPMMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاويرى از آتش‌سوزی در پایگاه علی‌السالم کویت پس از حمله ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/674409" target="_blank">📅 10:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674408">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر نیرو: نخستین نیروگاه گرمایی ایران به شبکه برق کشور متصل شد.
🔹
سازمان هواپیمایی کشور: فروش خارج از شبکه و دریافت هزینه اضافی برای پرواز های اربعین ممنوع است.
🔹
رزمایش دو روزه چین با مهمات جنگی در تنگه تایوان آغاز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/674408" target="_blank">📅 10:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674407">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سازمان راهداری و حمل‌ونقل جاده‌ای اعلام کرد: زائران اربعین استان‌های تهران، قم و اصفهان می‌توانند بلیت سفر برگشت خود از مرز مهران را از طریق سامانه سپاس و به نشانی
sepas.rmto.ir
تهیه نمایند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/674407" target="_blank">📅 10:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674406">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSLdcWx1XgSN2SNdn5d9VY7uOlIE-JDU92D0IiEEMlqxQGvRT-Vk9IFG2lqYtqc47Pn5lW-vwva7FlzLTatkLUeoZ1JUdjWLJh-aCiFmCbXV1S-PSBizVKn4-nEnxtS19CVhl8ygzu1TJki2tt6cZvZw5pj6ql7I-Z0OHo3vrh3oiC_BqeB6oOV7m0A0dReuFib19_63x_6L8MOP-t_rFqBScSLOI5_twtQ9blILiPe2xrAR3EmFGYk_eOJ89Fial52-UIwpBJY4WwWlAIk43wQxT0v0jlM9At6RYYkNeyNLsyJKGv3CfezJHz-emlIYAupmeIoYXRjwX9MHJsE4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرعه‌کشی بازی‌های آسیایی ۲۰۲۶؛ رویارویی تیم ملی امید ایران با چین، امارات و کره‌شمالی در گروه B
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/674406" target="_blank">📅 10:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674405">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWaVUgGnIpNBjy_u_koCD1nQ81LGsJVtiIytlQVGgKWD7kgeNRLz8ip1nIx_Xr7cgrUCP49B2AEe38pZbJU03AsTKHPDsfw0SIC1VRqRlLHidNs616uwOXTIHvyGUYjRDJMlk6_IBNmqGRiUkJwxc_c24MoZ_ENh4qMklj3OsWXouTJp5hD0noFRf5BHCAG_1a1ZbGml6_29i7NKm7tWA8jG1w_c83s8qFt3HarABkNIedkHzE3XjkEppaGl1H0328kqM0dWbVIqUxfdEaWeReTKJHWy9DxQDkRanJ38Do3aUgMVByrPtURfeYwBtucbjeyzZpiWi0Gi6_sSLr7ItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۳ توصیه پلیسی-حقوقی برای سفری ایمن در اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/674405" target="_blank">📅 10:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674404">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رسانه، جنگ روایت‌ها و دستی که نباید بسته شود
مصطفی انتظاری هروی مدیرمسئول خبرفوری:
🔹
در روزهای اخیر برخی همراهان و مخاطبان خبرفوری در پلتفرم‌های داخلی درباره عدم انتشار محتوا در کانال‌های خبرفوری در بسترهای ایرانی پرسش می‌کنند.
🔹
آنها می‌پرسند چطور ۸ سال پس از آنکه خبرفوری با حضور در بسترهای داخلی که آن زمان تازه شکل گرفته و در رقابت با پلتفرم‌های مشابه خارجی بدون مخاطب بودند، با وجود همه فشارها و جوسازی ها، به این پلتفرمها از حیث فعالیت رسانه‌ای معنا داد، امروز همان حضور معنابخش به خاموشی گراییده و با بستن سکوهای انتشار خبرفوری در پیامرسان‌های داخلی، این ظرفیت‌ها را به محیطی ناامن برای رشد رسانه بدل ساخته است؟
🔹
البته احتمالا پاسخ برای آنها روشن است اما از سر شگفتی می‌پرسند چرا در میانه جنگی که بخش بزرگی از آن بر سر روایتهاست، چنین سکوت کرده‌اید؟ آیا این سکوت به سود دشمن آمریکایی و صهیونیستی و جریان نفوذ داخلی وابسته به آن نیست؟ آیا این سکوت به زیان نهادهای رسمی داخل کشور نیست که برای ارتباط با مردم از کانالهای خبرفوری به طور لحظه‌ای استفاده می‌کنند؟
🔹
ما به‌عنوان بزرگترین رسانه کشور که بدون هرگونه وابستگی در ۱۱ سال گذشته فعالیت کرده و براساس وظیفه و تکلیف، از کشور در تمام فراز و فرودهای داخلی و خارجی دفاع کرده‌ایم و هزینه آن را پرداخت کرده‌ایم، تمام تلاش خود را می‌کنیم که همچنان صدای مردم و راوی روایت حق و‌عدالت باشیم.
🔹
اما این تلاش نیاز به بسترسازی دستگاه‌های مسئول و نظارتی نیز دارد که امیدواریم با درک شرایط کشور و در اوج تجاوز بیگانه به مرزهای فکری و جغرافیایی ایران بزرگ، با سعه صدر و درک عمیق‌تری از واقعیت‌های موجود، دست رسانه‌های داخلی را در رویارویی با امپراطوری دروغ تحت کنترل دشمن متجاوز، نبندند.
🔹
خبرفوری در این ۱۱ ساله ناملایمات بسیاری دیده و به عنوان رسانه‌ای جوان و مستقل تجربه های گاها دردناکی را از سر گذرانده و این بار هم با درایت نهادهای عالی کشور به ویژه دستگاه قضایی و تدبیر همیشگی شخص رئیس دستگاه قضا که شناختی ریشه‌دار از نقش رسانه در تحقق عدالت در کشور دارند، به مخاطبان وفادار خود بازخواهد گشت چراکه دود تصمیم به بستن صدای رسانه‌های حامی عدالت، به چشم همه ارکان عدالت‌طلب خواهد رفت و پدافند رسانه‌ای ایران در برابر دروغ‌پردازی خارجی و فساد و نفوذ داخلی را در این دوره حساس دچار آسیب می‌کند.
🔹
ما بر این باوریم که کسی اجازه نخواهد داد در میانه جنگ نظامی - رسانه‌ای، صدای بزرگترین رسانه کشور در بسترهای مجازی وطن خود، خاموش شود. ان‌شاالله...
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/674404" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674403">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnYhKAqMVjLZD8wod09dox5nCmmOKgi73kAYUG8vbwEhnTM4Ob8Q8OFl44O8FS6H7L4t2uRni3jszyRuA_TetKZy0xe9LPHWjtPQhaDc_A3OnlX8e4HZLafr0c71-bRXKWzCNNy__RjntUsnxhQVwItiJpxbVtZfWjEGmF5pAe_iM08D_ifmRAQSBezkmmXzv5iG3ydVpiaC0qvUlLqqc4vAAtcp2xO2cQ4O-T64DYphhPo4TAoyBgwBRzEwYz6NGz8cRJYLmWwshtcM9nGztnu-VZu6s2vbPoI3BS-KS04WQ8VAD6GXtgTmEMgyRl-S5c753AY6yCw1VxVq8Rs_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش آزیتا ترکاشوند به حمله دشمن به مرز شلمچه
🔹
تاریخ در حال تکرار است یزید زمان به زائرین کربلا حمله کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/674403" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674402">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JG54JOoJfPrTXhO7X5YpsiXsvceiBHBSndWretj8SEIMAgIpCl4Z5ViTVkTi3ihBBziX7nDegAEfDI5xRoVpCONMOz1v8cRcEY_yiRakUiSJG9aDEYHUh-IVSMKd1QELefefJ6x_T7sDr2NTr33MaxqwvU4NIQsA5QbjbAJmg7K_XRDQqL75WfMni5N5s4IqF9coFBUiQVxgGVAkdYBAvT5z-f67WBzXMd3q7QNKwoHnYwRiWhP5iK2KAkISiOEnfBi4ZVJTdD6hymBAUmE_VPIIy0XGlyePIGTt5c5e9yBcTNjL8EKLmeYqD0KBJZ0C3jUepLcy146hpDgQcUmdeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوهسنگی مقصد شادی کودکان
🔹
اگر دوست دارید فرزندتان اولین تجربه حضور در نسل سوم زمین بازی کودکان را داشته باشد، این دعوت را از دست ندهید.
🔹
در بوستان کوهسنگی، با افتتاح یکی از مدرن‌ترین زمین‌های بازی کودکان کشور، شبی پر از شور، هیجان و خاطره را کنار هم رقم می‌زنیم.
🔹
همراه با ، قرعه‌کشی و اهدای جوایز ویژه به کودکان
📍
بوستان کوهسنگی
🕗
پنج شنبه ۱ مرداد  | ساعت ۲۰
منتظر حضور و  لبخندهای کودکان شما هستیم.
💚
🌳
🎁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/674402" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674401">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_bHCP7GGYxSQDw3PR-N96-y8_QhU-r6qWNy53WKJF7VOOKCgXD7RHLznyJYYAv3Gk48nDmW2-d-cywFXhwUA-GIu5mkYMJl5Dwdrlg1nh8uXMnMxeUq4ydzm0Y1SqZHWwAZk1PAuFmUc6KFtQn-Pc0vp_gAd-0wKa6-0LOZcSpujphOp21cgDOvQjQqAg1Rh3BQ_9uZf1SZLDQusL34e09ttUHEfXHYkGvanlPJXw34mT1e_U6EiJCReH6aYRZjd8F6kNIfQz9lukdZa9H7M1mMG5NBoSdaWV_1kfg-76eMWYrsn1iT_aa9XfMT2IDSFzmSKAjbDX4a0oDEg91stQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ۴ سرباز به هلاکت رسیده جدید آمریکا در جنگ با ایران
سی‌بی‌اس:
🔹
یک سرباز ۳۰ ساله آمریکایی آخر هفته در عراق در جریان آنچه آمریکا انفجار کنترل‌ شده برای انهدام یک پهپاد تهاجمی اعلام کرد، به درک واصل شد.
🔹
پنتاگون اعلام کرد گروهبان مایکل امانوئل سوینتون «در حین عملیات انفجار کنترل‌شده» پهپاد در پایگاه هوایی اربیل در شمال عراق به درک واصل شده است.
🔹
سرباز سومی هم که پیش از این مفقودالاثر بودنش در پایگاه هوایی اردن تایید شده بود، اکنون گمان می‌رود که به هلاکت رسیده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/674401" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674400">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130fef3d83.mp4?token=STx2WOtlCmPNjabSegW6PlP4b4Z7bMg_Ff_Vgo7H6qj-FbtWFSDeWudQI7ye64sN6J0aO4pihunBK5YJh4Y61Wapv1iL95sygmViRXs1zLtkzvccFQA1eSQhx5h71k30ERseNIpMisgzbgkNsHk9gQ9pYMnZ4_Bc8plMYQ1zEOH4Ee7YKw22Qt1uLj5FHldVVpYMiKbx46AK2mEn-muxS5xOJM8nY2fLO6XFogkEPAewqPSTty2_tiFTNWaM7-oNEA6ssVykc5ygSHw9EoXfDCaqd4VpxgwAu36QYcVqkRnqlHodtTptIdkZq40GKFlIeiLB6ga20K696k26aQrGRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130fef3d83.mp4?token=STx2WOtlCmPNjabSegW6PlP4b4Z7bMg_Ff_Vgo7H6qj-FbtWFSDeWudQI7ye64sN6J0aO4pihunBK5YJh4Y61Wapv1iL95sygmViRXs1zLtkzvccFQA1eSQhx5h71k30ERseNIpMisgzbgkNsHk9gQ9pYMnZ4_Bc8plMYQ1zEOH4Ee7YKw22Qt1uLj5FHldVVpYMiKbx46AK2mEn-muxS5xOJM8nY2fLO6XFogkEPAewqPSTty2_tiFTNWaM7-oNEA6ssVykc5ygSHw9EoXfDCaqd4VpxgwAu36QYcVqkRnqlHodtTptIdkZq40GKFlIeiLB6ga20K696k26aQrGRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
این راتاتویی رو‌ به سبک موش‌سرآشپز درست کن
🐭
مواد لازم:
🔹
بادمجان ۲عدد
🔹
کدو زرد ۲ عدد
🔹
کدو سبز ۲عدد
🔹
گوجه فرنگی ۴عدد
🔹
فلفل دلمه‌ای ۱عدد
🔹
پیاز ۱عدد
🔹
سیر ۳حبه
🔹
روغن زیتون ۴قاشق غذاخوری
🔹
آویشن خشک ۱قاشق چای‌خوری
🔹
نمک‌و فلفل به مقدار لازم #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/674400" target="_blank">📅 10:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674399">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
فراخوان کمک برای مادر مبتلا به سرطان سینه
🔸
این مادر که سه فرزند خردسال دارد، سرطان سینه دارد و جراحی انجام داده است.
🔸
16 جلسه شیمی درمانی نیاز دارد و 25 جلسه پرتو درمانی که هزینه آن بالغ بر 500 میلیون تومان می شود .
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید.
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در تنها در کانال خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/674399" target="_blank">📅 10:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674398">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
روسیه و ایران بر پایبندی به توافقنامه مشارکت جامع راهبردی تاکید کردند.
🔹
شیر‌محمد اسپندار نوازنده پیشکسوت موسیقی بلوچستان ۳۱‌تیرماه در ۹۸ سالگی درگذشت.
🔹
انصارالله: یمن لقمه بزرگتر از دهان سعودی هاست، عربستان تاوان خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/674398" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674397">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4172d4b5.mp4?token=jt8LBPMHZNGRKksCMjVKktIVKt75T0ulM1Ed8tvvL5ZlJ8XMbgNoKiFpMHDrO16L7yWD1l9vcJULkir2NonQqfK-IFulHZPtbTJKsFToK13xbOZOiyQj-Hs1vcVX1thk-XLLXrbvVYdP2idIf_1Zo9ts5x0a3GZCm9StS565K-eaPofDQFYwZdmHsvzc9pNNPfUBdfWj9govhNU7x_Z7_nX5tDHc72TrMespVbIHOABQgaahsZpvA1qBVvD06Gr9O-ElQp8lMw_qxBD3kArZAJPbq4nYUaG4x_c4fuYGzfeRqF_YMH3EYGek0MAQlV8KYGw5qsq6uaZqNdvjYN0i5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4172d4b5.mp4?token=jt8LBPMHZNGRKksCMjVKktIVKt75T0ulM1Ed8tvvL5ZlJ8XMbgNoKiFpMHDrO16L7yWD1l9vcJULkir2NonQqfK-IFulHZPtbTJKsFToK13xbOZOiyQj-Hs1vcVX1thk-XLLXrbvVYdP2idIf_1Zo9ts5x0a3GZCm9StS565K-eaPofDQFYwZdmHsvzc9pNNPfUBdfWj9govhNU7x_Z7_nX5tDHc72TrMespVbIHOABQgaahsZpvA1qBVvD06Gr9O-ElQp8lMw_qxBD3kArZAJPbq4nYUaG4x_c4fuYGzfeRqF_YMH3EYGek0MAQlV8KYGw5qsq6uaZqNdvjYN0i5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بشارتی الهی از رهبر شهید
اعلان کردن که نیروگاه هسته ای براش(دولت سعودی) می سازیم...
اگر بسازن هم بنده شخصا ناراحت نمی شم
چون می دانم در سالهای نه چندان دوری به دست مجاهدان اسلامی خواهد افتاد/ سال ۱۳۹۷</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/674397" target="_blank">📅 10:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674394">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
رویترز: ۵ نفتکش مسیر خود را در دریای سرخ تغییر دادند
🔹
خبرگزاری رویترز با استناد به داده‌های کشتیرانی گزارش داد که پنج نفتکش روز چهارشنبه مسیر خود را در دریای سرخ تغییر دادند تا از تنگه باب المندب عبور نکنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/674394" target="_blank">📅 09:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674393">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qp5ocZEjgGO5s_sqNHw_88GssxxFQxb3MJtNjL-dbycRY1cCZ5M7o25Ld8UhVs-Rx-UbRXtGmErgrBinUHPE-53pHbpd472Z2JyOAwBJqjkIEIHIgC9OctbgibEaGkNUnvn74EU_89KpuYzI0AUwKAe4rH_Tq9fsVx1LiWMtV3K4FYk2y9tpMiXBMWnWR2It3kZc1_hxFbTaSnbb8ezZfSitoab80vZ8urCG0Y8cI-3LzScbkqwOmfJpbZyx5Eu9hknJ2OT0elPbgSCKYKuftHfeZu703yB0qSfJLBJ5seuIBcTYAreZUdKKyYHinKBf-PrKuXlj6zkjyq-xrdetHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی هندبال ایران در بازی‌های آسیایی ناگویا با بحرین، کره‌جنوبی‌، کویت و قزاقستان هم گروه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/674393" target="_blank">📅 09:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674392">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNoZKSRa8tjBAjaiJUwVLJ07zZTzlrM8x5MLFWpbzX1ThE8R2eGYTwMVEK_3ntxXd2lmWesCzGM00Su19dTL_Uaw2dmkr2Djdvg1JvB3X5rj5SRZt4Jb8-d3NgQY332dduI73w1kpJ-WMmNaJctA8SmVg1EKr9mlHwq4LFN-udfnlMR1As2rDUyebz8hdKYcRURn4okhMVIm3dVge_yO9eepUIuxGNwn1qdKpEDtMn8R1wflBW2hIMFMsp3Tq5yEVI344GrIKRsH1jwDNVYmh71JbTMcEeOfENTszez2QJiaylX8oDQiKqKa10cVkPKbXuxESYhyB-oId6SjsAc0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیه های غذایی؛ برای کسانی که کبد چرب دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/674392" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674391">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEpNtjmOFCmfPJ7JNO27dhWL_2BAlrpzKPstLlw8qF_6_DjEOvHfzOUdtc8X76wo1BFLMPY2xjoJV7wzp2ph8NGoth6oCUv6cmhWUbIjPtoEA0uaR1Zpqo-5YI7XYVF7CyNOjlu_vcbFvUiR1Hqupfvf4gFa9JoqOfR0ogA49N7Dgpr6TnnuyNH12TcryPB-62ADOpTE_vCuY3s76IrqxMpcf7IbjX6WM91Bqie4EqReG8wzzYe50GubwVal_3fi3uuSxC97_THdMCda6sR6QJ-fZmDlO6rN3fmIr-5yrIUp-P5qK-IjtmHyx-y1yw7zD3iIF3yQQzMlE5c5f-J_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشاگری تکان‌دهنده اسکای‌نیوز/ موشک درست وسط مدرسه میناب خورد/ در روز حمله یک گروه ضربت ناو هواپیمابر آمریکا در برد میناب بود
اسکای‌نیوز:
🔹
شواهد موجود نشان می‌دهد که یک گروه ضربت ناو هواپیمابر آمریکا در روز حمله به مدرسه در برد میناب بوده است.
🔹
مدرسه تنها ساختمان غیرنظامی نبود که مورد اصابت قرار گرفت، تحقیقات ما ۱۱ ساختمان مجاور را که در این حمله مورد اصابت قرار گرفته بودند، شناسایی کرد. موشک‌های تاماهاک آمریکا درست به وسط مدرسه، در سالن اجتماعات، برخورد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/674391" target="_blank">📅 09:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674390">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a11234b2.mp4?token=uFQPd8zzdUPzhpMr5r2DF_1NXeXtiyd6TPGXA_Py_wzk0o8-1gA_3fnDtDvkOtLvwJKgZj5LO6Q0MySYC6tKBBk9NK5xj7TZW_X5hDNp5DezsN4q1ejMb4qVtA4IuuQSWsR_X3RNa2I6Aux9MHc4Ep43ynL3GLFA_HHRqyyylXoL0ad88U3GCYzK23cFsczbj_vSaRKLvIgapCFce1_xo9bON6GVh8oS8J50cHJRRA3r31uy1AjxRlHosbQqa0tlhSSoz7BEEfju1BpFU5OF3IrcXDF9yxp0XXAW2mRHScMVPoNYhh8ECaHqFWE-2xxVjpfdY-t1hbPaCxJCQ4WkWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a11234b2.mp4?token=uFQPd8zzdUPzhpMr5r2DF_1NXeXtiyd6TPGXA_Py_wzk0o8-1gA_3fnDtDvkOtLvwJKgZj5LO6Q0MySYC6tKBBk9NK5xj7TZW_X5hDNp5DezsN4q1ejMb4qVtA4IuuQSWsR_X3RNa2I6Aux9MHc4Ep43ynL3GLFA_HHRqyyylXoL0ad88U3GCYzK23cFsczbj_vSaRKLvIgapCFce1_xo9bON6GVh8oS8J50cHJRRA3r31uy1AjxRlHosbQqa0tlhSSoz7BEEfju1BpFU5OF3IrcXDF9yxp0XXAW2mRHScMVPoNYhh8ECaHqFWE-2xxVjpfdY-t1hbPaCxJCQ4WkWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وطن ای هستی من، شور و سرمستی من #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/674390" target="_blank">📅 09:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674389">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
اکسیوس: آمریکا از یک بمب‌افکن B-1 برای حمله به ایران استفاده کرد
اکسیوس:
🔹
مقامات آمریکایی اعلام کردند که ارتش روز سه‌شنبه از یک بمب‌افکن دوربرد B-1 برای حمله به اهداف سپاه پاسداران در ایران استفاده کرد.
🔹
این اولین باری بود که ایالات متحده از زمان از سرگیری جنگ با ایران در ۱۲ روز پیش، یک ماموریت B-1 انجام می‌داد.
🔹
استفاده از بمب‌افکن‌های B-1 که می‌توانند دو جین بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز حمل کنند، نشان‌دهنده تشدید و گسترش قابل توجه کارزار نظامی ایالات متحده بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/674389" target="_blank">📅 09:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674388">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بر اساس حکم قاضی آمریکایی، محاکمه مادورو به سال آینده موکول شد.
🔹
وزرای خارجه پاکستان و عمان درمورد تحولات منطقه‌ای رایزنی کردند.
🔹
ظرفیت نخستین پارکینگ زائران مرز خسروی تکمیل شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/674388" target="_blank">📅 09:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674387">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brY1qrluMbqTF5JKqgIChOEWjEX7ddFGMGfoUMS_ufxMaHj7hPtMSQTcXxr8YOQwRnz9c4YjOFtMgiOLE5fbm4JcEQaimo-KvnUte2rpxUOc-mG0pAedPq5h8xdguIxWvQ4icDHWgUc2p8Xs9hh5zd5csJ0RWaPht8ZEaIEULw8go_3XGWrv13KXKvRLUp_XWOZUVMvvDRlSW2y0V_0QSRzg8Pxyv3k0MTntM1pWfJb0pmifGdAwNihlaYQyh8FoLJ0CW4NWrksiTN7YKgY0qhTE3Lvlf44svNpdD7QdQo1MZTemRCZ1Jkflq6FGZ_2Xzcj-oFgsuybjkUPIH5GsIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۲ هشداری که بدنت قبل از کمبود ویتامین‌ها بهت می‌ده
⚠️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/674387" target="_blank">📅 09:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674386">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQlurGRXFBwf1CAIqWsH3v0Ze2RCDayWeYnHQmVgU1nhXoMxv2lfAd9aTMraj6ZOutpAWznjT8vbrQU7jt_EMyIhUOdDHjoFJv2sj61wzYWOcC2ZZ0hstAhNX5klxOZiKcr2hRq--_0lChk_HILVan77GKo6LGApLpQ7-jw8cZm7k86qBBkxCbKpgHUMK0e9UI8IeEFup4BEONEH_9TVyVBQ8kbUKqbbNzwAd8FjzbhGL-PiUR1XoaQ43BsMuTcbK0NIQde-WyOIW3cB4VAhJ74ewf5EnAMppi1iQGovMdUXcnr_qM2kaOrQzvaMq6WjAJZ1thUNoWcvkUr3dm0YJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلوهن میزراهی: فکرش را بکنید اگر ایران واقعاً کاخ پادشاهی در اردن را هدف بگیرد؛ به نظرم همان روز ۵ میلیون نفر به جمع شیعیان اضافه خواهند شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/674386" target="_blank">📅 09:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674385">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۴/ پیام مهم سپاه به مردم کویت/ آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده است نه ما  روابط عمومی سپاه:
🔹
مردم شریف و نجیب کویت؛ برادران رزمنده شما در سپاه پاسداران انقلاب اسلامی در تنبیه ارتش کودک کش آمریکا و دخالت های آن در تنگه هرمز،…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/674385" target="_blank">📅 09:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674384">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c060f789.mp4?token=kT5njAIMtiUVq5SzZI-RY8oU3gR_VytjvR-Sv9be0USvS5jjTbIm6VHcNXz3IR8nKuTPXxbhOsJLgYX_RxU5RgZQ_9z7hpjHz6CTM0lZte1dd-qX2fFHTC3XBOHgWjE-ulxnXgQXSWJXptINupLWaBb1XKckGwa7_coJxTVxKSd9rhaE5_i8DTHPEkRKtiKgUZC_tcStYVEu2xSfHkEAhHLUr2tfOXAtbk2SRRTshdMUcuSDlbHt57MM57_lt45MrJDeVxsRBIzfFtP3scFGZfuJ__IVvy6AXmu0kQENyQ1ri7Cudsp5fbNSabwj0lJbpWKUWcpFgn13WwTdbHRjwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c060f789.mp4?token=kT5njAIMtiUVq5SzZI-RY8oU3gR_VytjvR-Sv9be0USvS5jjTbIm6VHcNXz3IR8nKuTPXxbhOsJLgYX_RxU5RgZQ_9z7hpjHz6CTM0lZte1dd-qX2fFHTC3XBOHgWjE-ulxnXgQXSWJXptINupLWaBb1XKckGwa7_coJxTVxKSd9rhaE5_i8DTHPEkRKtiKgUZC_tcStYVEu2xSfHkEAhHLUr2tfOXAtbk2SRRTshdMUcuSDlbHt57MM57_lt45MrJDeVxsRBIzfFtP3scFGZfuJ__IVvy6AXmu0kQENyQ1ri7Cudsp5fbNSabwj0lJbpWKUWcpFgn13WwTdbHRjwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش شهرک‌نشینان صهیونیست به مسجدالاقصی و هتک حرمت این مکان مقدس با اجرای رقص‌های تلمودی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/674384" target="_blank">📅 09:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674380">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9f6eacc52.mp4?token=YraRMNmrzdvkClF3WwgHhIc6n0dS4NQMhIVXV-0_BVaNY2NRmxo_RlvjvhkOssu5o4uQDH-2hUiAKZRUrg0JHx4f3Ac1Ius8ESAGQuP1IrkNhToLvNRLlDbdYy79cfMqoEBSx3ao4QQxmdfIv7OiDk1gyzMEdivqBlvD8bUFEFzz-ck_U3YYs6CYbjRSpzuqkiVeZG1moXtDZpzmkePWTFjMTyxrso3Fu1SuLl0K0S8X2hY5DATb6USeJMcvyMqPRf-E0OQqIgaIZOo5rU5M1XFolfOzPuOt9HBwacIfzON_tD1kdN4X4ZsHLp_DyC5CCU9QNf3NQVopfD-KGJ5_p4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9f6eacc52.mp4?token=YraRMNmrzdvkClF3WwgHhIc6n0dS4NQMhIVXV-0_BVaNY2NRmxo_RlvjvhkOssu5o4uQDH-2hUiAKZRUrg0JHx4f3Ac1Ius8ESAGQuP1IrkNhToLvNRLlDbdYy79cfMqoEBSx3ao4QQxmdfIv7OiDk1gyzMEdivqBlvD8bUFEFzz-ck_U3YYs6CYbjRSpzuqkiVeZG1moXtDZpzmkePWTFjMTyxrso3Fu1SuLl0K0S8X2hY5DATb6USeJMcvyMqPRf-E0OQqIgaIZOo5rU5M1XFolfOzPuOt9HBwacIfzON_tD1kdN4X4ZsHLp_DyC5CCU9QNf3NQVopfD-KGJ5_p4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف تحلیلگر ضدایرانی؛ آمریکا فقط در ۵ ماه جنگ علیه ایران، معادل هزینه ۴ سال جنگ خرج کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/674380" target="_blank">📅 08:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674377">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4wBtbyDWKvNa3OCqwfwJY_7-r_blnu_61FFKOCrR87x9jLXj4hRWA-zD06QG3tJ46k-k08Ct9eFIjnXfZIzjSaTcy1YWycuVbYgXz1pj9oy4BOXEIO7HG0uMCZdSSS9b8LQKVqQa9zTiCnIzkhdwh1jX7yP_YrCYCO3lZ1NCWeeQUxG0fMmo6836t9trnR8V19LiB4UU-W0gpZq4KrQzNAbc3pwoqFMPW3uqp2qNUpORlc3Tnp1n_Otz-MnuCw8X1Har1HaQcJIh_TMaCSUoeYv7QjCYHYGfzV054MO0Vt2tL_lrrZ89lvK4EbNSHQ7SXK1nvlUDkCMf48PS_sInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ شاهکارِ کمتر دیده‌شده‌ اینترنت
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/674377" target="_blank">📅 08:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674376">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874152db1c.mp4?token=SgBsLd4xtnCwQR2Co3s0VwqfWonLLEZ8euy0PynIM6mne2PEiTMp6tES2yR3IsYMi0vK6sp5hDcpFaj46wBsVG8L1i_4hlFgS31uHRYggXvHqDcdh6t9_ymkLViSeWO850sjfcI8chiHazcGgw0N7IIy0ujUZ8UTPVs-YdtWuwGmPGJHyPlOxlv_5BcSzBwZfAFHMt4wKowxUSfvPOMTq23lZj5bhQ4lRXBBAjup2OC4NivUA-P5elxc-GCaxyxvT5bn0hAxbmFxCnfafFnvgFb7lljLZDcnoZZkCXTD9uRnYOibxoZoT50YAZd09XTJfvnjKWGIKuEUpLn5xvnXoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874152db1c.mp4?token=SgBsLd4xtnCwQR2Co3s0VwqfWonLLEZ8euy0PynIM6mne2PEiTMp6tES2yR3IsYMi0vK6sp5hDcpFaj46wBsVG8L1i_4hlFgS31uHRYggXvHqDcdh6t9_ymkLViSeWO850sjfcI8chiHazcGgw0N7IIy0ujUZ8UTPVs-YdtWuwGmPGJHyPlOxlv_5BcSzBwZfAFHMt4wKowxUSfvPOMTq23lZj5bhQ4lRXBBAjup2OC4NivUA-P5elxc-GCaxyxvT5bn0hAxbmFxCnfafFnvgFb7lljLZDcnoZZkCXTD9uRnYOibxoZoT50YAZd09XTJfvnjKWGIKuEUpLn5xvnXoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله بیست و سوم عملیات صاعقه ارتش؛ سه پایگاه آمریکا در کویت هدف مجدد حملات پهپادی ارتش قرار گرفت
روابط عمومی ارتش:
🔹
در پاسخ به ادامه گستاخی ها و تجاوزات دشمن خبیث به کشورمان، ارتش جمهوری اسلامی ایران  در مرحله بیست و سوم عملیات صاعقه، ساعاتی قبل، محل استقرار انبارهای مهمات و اقلام لجستیکی  ارتش کودک کش آمریکا در پایگاه الدوحه، مخازن سوخت در پایگاه علی السالم و انبار مهمات در اردوگاه عریفجان کویت را هدف حملات پر حجم پهپادهای انهدامی خود قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/674376" target="_blank">📅 08:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674375">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4cc78c72.mp4?token=oYrGJSNABVd9FSdXHHezFWUD8VNXdjcdoDT4n6sFZdfVnChCm6hwn6hgd7r3qYjyFyTneG6GYMmqZbJYPuOCtf92ZEeuqeUFpJBhrxHTfnQukx3ai-meOW_lyB8GInZqDmsQJyk364xfa_q06n_CbsFfxS5jiOejyz0250b8rSO84GxTWbGxy8GeuB5eQZHR9_Svy_42lVelqLaKwe6zTPibywrdwTAFww9Fsmw9KUED6oNRD0EZHSIf51kPXSvmXN_DyqyCl5A-qg-bIwQSBqq8aG-GEx_rl3aEwJnKt3zA5FolAYxlFTj0rQazO1m4mFLpHQRe4wycWA14Wer7qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4cc78c72.mp4?token=oYrGJSNABVd9FSdXHHezFWUD8VNXdjcdoDT4n6sFZdfVnChCm6hwn6hgd7r3qYjyFyTneG6GYMmqZbJYPuOCtf92ZEeuqeUFpJBhrxHTfnQukx3ai-meOW_lyB8GInZqDmsQJyk364xfa_q06n_CbsFfxS5jiOejyz0250b8rSO84GxTWbGxy8GeuB5eQZHR9_Svy_42lVelqLaKwe6zTPibywrdwTAFww9Fsmw9KUED6oNRD0EZHSIf51kPXSvmXN_DyqyCl5A-qg-bIwQSBqq8aG-GEx_rl3aEwJnKt3zA5FolAYxlFTj0rQazO1m4mFLpHQRe4wycWA14Wer7qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات مناسب گودی کمر  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/674375" target="_blank">📅 08:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674374">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۴/ پیام مهم سپاه به مردم کویت/ آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده است نه ما
روابط عمومی سپاه:
🔹
مردم شریف و نجیب کویت؛ برادران رزمنده شما در سپاه پاسداران انقلاب اسلامی در تنبیه ارتش کودک کش آمریکا و دخالت های آن در تنگه هرمز، یک انبار بزرگ تجهیزات نظامی، یک سامانه پدآفندی پاتریوت و یک آشیانه پهپادهای MQ9 آمریکا در پایگاه هوایی علی السالم را مورد حمله پهپادی قرار داده و منهدم کردند.
🔹
برادران شما همچنین محل اسکان نیروهای آمریکایی، دو آشیانه بالگردها در پادگان العدیری را مورد تهاجم قرار داده و ضمن کشته و مجروح کردن تعدادی از نیروهای متجاوز، به چندین فروند بالگرد و پهپاد، خسارت سنگینی وارد آوردند.
♦️
رزمندگان همچنین در پاسخ به حملات آمریکا به دکل های مخابراتی در ایران، یک دکل مخابراتی را هدف قرار دادند.
🔹
پس این آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده است و نه ما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/674374" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674372">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
تداوم مبارزه بافساد مالی در عراق
🔹
دستگاه قضایی عراق:
۴۰۰ هزار دلار، ۱۳ میلیارد دینار و ۴۵ کیلوگرم طلا از معاون وزارت نفت عراق کشف و ضبط شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/674372" target="_blank">📅 07:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674370">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWWriAeeuw7GGgK-qxEI-_0LC3AjBgFh4S_-lqHaoioqDy99cXIh8b3pKErmiiXEPBPzgn_AdUCQo7n1tqrwnEmrqgB5HjOMG4OwOFIuOlcADjkPIaZrc2dNeklPi3jgfSDzw23UOmjSDtCaSlmQDJGtyTpqKtt1wXur02qoS8WBvCvq0j6oKYLdMNDJbnSXbUEdjHIeq9WxN91i_E-oCFH1XSbkXeL9gT8FmHJI1v0k0ZA51l_ezZ-iDyvNiwx1HDjZf9mAjclMATolSn1gBp2fDupW5pIcZaLh6mj7wa6deufXZAZUIwNfp0n5NqXGar-QGsmfIS62oHSArZcRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱ مرداد ماه
۸ صفر ۱۴۴۸
۲۳ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/674370" target="_blank">📅 07:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674369">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
مجلس نمایندگان آمریکا بودجه نظامی ۱.۱۵ تریلیون دلاری برای ۲۰۲۷ تصویب کرد که همکاری با اسرائیل را تسریع و هزینه جنگ علیه ایران را تأمین می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/674369" target="_blank">📅 07:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674367">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
صنایع تا دوماه قطعی برق ندارند
🔹
با دستور رئیس‌جمهور و با هدف جلوگیری از توقف تولید و حفظ اشتغال، برق صنایع در مرداد و شهریور قطع نخواهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/674367" target="_blank">📅 07:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674364">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
حملۀ دشمن به حوالی اسلام‌آباد غرب
فرماندار شهرستان اسلام آباد:
🔹
حوالی ساعت ۳:۴۰ بامداد امروز، در اثر حمله نیروهای تروریست آمریکا دو انفجار در اطراف شهرستان اسلام‌آباد غرب رخ داد.
🔹
فرماندار اسلام‌آبادغرب: حمله آمریکا به اطراف شهرستان تلفات نداشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/674364" target="_blank">📅 06:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674360">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610b37cc99.mp4?token=JZMG1Eg8FrIXiMhLvbsGJ8WiexFzSz2TL_h4YXAO8mpiY1DeI_1gZ4yJOP3WdW2nkLW6i00yhmVzVr3tGPbZHwMe2vFwCKo3XZZiF32Rwiy4xqd4DLSZJ8x-ENl3noklTYijkNw-VUXhUfexQQjTysYOl-S16gJQSzVB2YhFnOGNKNXssLpHc-pYfwmf5XdIcQPmwEqTciv8uE-211TtmOAiBUr0SCCl4OEIFXjSnxCG_0keIJkJIDir_KksCdfcV3JJjfr-_Z9hAL0kFug8xSJYd4Ap8SgVyMGGTSU1F_WRsFTXU-j3Ni5ogzdcW-gB14jM82Uubzys2Na61zZtoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610b37cc99.mp4?token=JZMG1Eg8FrIXiMhLvbsGJ8WiexFzSz2TL_h4YXAO8mpiY1DeI_1gZ4yJOP3WdW2nkLW6i00yhmVzVr3tGPbZHwMe2vFwCKo3XZZiF32Rwiy4xqd4DLSZJ8x-ENl3noklTYijkNw-VUXhUfexQQjTysYOl-S16gJQSzVB2YhFnOGNKNXssLpHc-pYfwmf5XdIcQPmwEqTciv8uE-211TtmOAiBUr0SCCl4OEIFXjSnxCG_0keIJkJIDir_KksCdfcV3JJjfr-_Z9hAL0kFug8xSJYd4Ap8SgVyMGGTSU1F_WRsFTXU-j3Ni5ogzdcW-gB14jM82Uubzys2Na61zZtoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲ شهید و ۱۱ مجروح در حملۀ موشکی آمریکا به مرز شلمچه  معاون استاندار خوزستان:
🔹
در حملۀ موشکی دشمن تروریستی آمریکا به مرز شلمچه، ۲ نفر از هموطنانمان شهید و ۱۱ نفر مجروح شدند.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/674360" target="_blank">📅 05:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674359">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
حیاتی: تردد در مرز شلمچه همچنان برقرار است و امدادرسانی در محل ادامه دارد  حیاتی معاون امنیتی و انتظامی استاندار خوزستان:
🔹
تردد در مرز شلمچه همچنان برقرار است و امدادرسانی در محل ادامه دارد، مجروحان این حادثه تحت مداوا و رسیدگی پزشکی قرار دارند.
🔹
این حملات…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/674359" target="_blank">📅 04:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674356">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سی‌ان‌ان: موساد اطلاعات کوه کلنگ را به آمریکا داد
🔹
منابع آمریکایی می‌گویند که «رومن گافمن» رئیس سازمان جاسوسی رژیم صهیونیستی اطلاعاتی درباره تأسیسات هسته‌ای ادعایی زیر کوه کلنگ را به واشنگتن منتقل کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/674356" target="_blank">📅 04:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674354">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تصاویر دیگری از حمله موشکی آمریکا تروریست به پایانه مرزی شلمچه در استان خوزستان  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/674354" target="_blank">📅 04:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674353">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e14d6a38.mp4?token=TDPobinuEVuX11MAUaIQrNVAi71XoRr9XIldE62F4MD-FMZaQ6vRGJJCWqoen8TcAml5l0kDA0-s0ETddRJt6IF7JLbv1JinMWldTaMbV11JWMPcbz-qzJ_Qnyi-LEOuKsl1qhqalS5IY6jJ3yBdIva9F9afFcCBM_e0XKs4wL5IP-zb1GPOM_8TWYWWQrHjOcT8vhiCt8LYvvWICpyoAp7o22E3vIHiGazR6BfIYROavi6PdfEaZTzGGAY54gkuU-H3qLtNl_-n7J94d-0or248jnqr_BKDVwZr13DMWorfPuvKpW0WZiSGt13IgCYWhfuRG0AZRLYni2t26Y05ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e14d6a38.mp4?token=TDPobinuEVuX11MAUaIQrNVAi71XoRr9XIldE62F4MD-FMZaQ6vRGJJCWqoen8TcAml5l0kDA0-s0ETddRJt6IF7JLbv1JinMWldTaMbV11JWMPcbz-qzJ_Qnyi-LEOuKsl1qhqalS5IY6jJ3yBdIva9F9afFcCBM_e0XKs4wL5IP-zb1GPOM_8TWYWWQrHjOcT8vhiCt8LYvvWICpyoAp7o22E3vIHiGazR6BfIYROavi6PdfEaZTzGGAY54gkuU-H3qLtNl_-n7J94d-0or248jnqr_BKDVwZr13DMWorfPuvKpW0WZiSGt13IgCYWhfuRG0AZRLYni2t26Y05ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهادت دو نفر در حمله آمریکای تروریست به مرز شلمچه  معاون امنیتی و انتظامی استانداری خوزستان:
🔹
تاکنون ۲ نفردر حمله دشمن آمریکایی به مرز شلمچه به شهادت رسیدند  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/674353" target="_blank">📅 03:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674352">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حملۀ موشکی به اطراف شهر اندیمشک
معاون استاندار خوزستان:
🔹
یک نقطه در اطراف شهر اندیمشک مورد حملۀ موشکی دشمن تروریستی آمریکا قرار گرفت.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/674352" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674350">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
حمله موشکی به اطراف پایانه مسافربری در مرز شلمچه   ولی الله حیاتی معاون امنیتی و انتظامی استانداری خوزستان:
🔹
دقایقی پیش اطراف پایانه مسافربری در مرز شلمچه مورد هجوم موشک های دشمن تروریستی آمریکا قرار گرفت.
🔹
این حمله هیچگونه مصدوم و مجروحی در پی نداشته و…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/674350" target="_blank">📅 03:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674348">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpS7qXt93CK31N1zP6xCIcko3HAA4ItDFB0PuOPEXMUguaJFaS5KYIIgF2dh47_uCkp1i71Inr34UTb650j8-u-5HmlU8jCLTCiIJn9NsKaVMBvGrmxGC2ry0SCzU6elGi_SzrZcTuQln0YSZmGijk7XzShTu7Bk6qD1ItO1wpHNRwVG25cPaE5WAH-G7W0DH4y3e-6zq_pkkS_h-B1ze7wJhjYpHvF28xxU2sW9PSiOZ_ywbRY9YALcszeROv4K4cbfxu7E6hI9lbwm8953DgHNfluuVXX47fIOJwI7I-AShWV3GIbR5GoPJI7T0jfettVnqEPUOQsalthx-tBVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم رضایی: احتمال حمله آمریکا به تأسیسات هسته‌ای، دلیل قانع‌کننده‌ای برای تغییر دکترین هسته‌ای است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/674348" target="_blank">📅 03:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674347">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8a7d9e0c.mp4?token=Z8ljzzLHBXZSZuvhlEB4kZcYUnyc6EyzE3ScQe0IOx63hcVsPXFF5DeQAGeE_k0OvwDaIepXEyIBGLnIt9eIJ9bVKfhbbuxTkkTIiujXhjMVoQ4asAzpwKl8EqxnietQoxYXWpfmEoXJC6yyHHk1mOZ5iHX0kmpV6emXUarb-H51uLo_wIdG0FEQcRTSZ26WTBCD9xiADS6m_pAhN-X7sccTzV2nuPxofUIStz5eao4Il_vDixgpjA1Y33c_ZL-NpGXSmWghYWazvysPKwQUhnxns4Z8-rsUHdASjpx8oWuJaVBioB6nwjOTXK_Llq_udUXodslHmGilEwKJ095qmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8a7d9e0c.mp4?token=Z8ljzzLHBXZSZuvhlEB4kZcYUnyc6EyzE3ScQe0IOx63hcVsPXFF5DeQAGeE_k0OvwDaIepXEyIBGLnIt9eIJ9bVKfhbbuxTkkTIiujXhjMVoQ4asAzpwKl8EqxnietQoxYXWpfmEoXJC6yyHHk1mOZ5iHX0kmpV6emXUarb-H51uLo_wIdG0FEQcRTSZ26WTBCD9xiADS6m_pAhN-X7sccTzV2nuPxofUIStz5eao4Il_vDixgpjA1Y33c_ZL-NpGXSmWghYWazvysPKwQUhnxns4Z8-rsUHdASjpx8oWuJaVBioB6nwjOTXK_Llq_udUXodslHmGilEwKJ095qmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه عراقی «نایا» نوشت: «آمریکا به محل استراحت افسران پلیس ایرانی در گذرگاه مرزی شلمچه بین ایران و عراق حمله کرد»/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/674347" target="_blank">📅 03:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674346">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
اخبار اولیه از حمله آمریکا به گذرگاه مرزی «شلمچه»
🔹
رسانه‌های عراقی با انتشار تصاویری گزارش داد که منطقه‌ای در نزدیکی گذرگاه شلمچه در مرز بین ایران و عراق، هدف حمله تروریستی آمریکا قرار گرفته است./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/674346" target="_blank">📅 03:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674345">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8cf6f105.mp4?token=MJf3qTjmvYOn0oqAhYH9E-Iw_syzM9cOEICLuiiGcInTV2ABn_AhnWKhBvU71f7YXH5tn36hKtXfcLA5FLRfqOYhAz_EbygFSGcXvzlYe_kmtR_5D0u8KCBgxmvPvv850uIcsfHbbhBJLiuHIW_xQILr6Cu5tKSY3pUVO49RdFqGUL86xW6qqkJX2EzjnKasdpJj21ytwL7PNPY4tR7ZkliFzMiH6msIDTCLO0N0RtF2tqMfVsj3UFfcjz8ZiJmN9bfF6v6Eu5JbKVWF2prkH4aZw_E9poQAsGjZ68IGuIbFm80-o8z_4iD8aAE9AlocbJyiAUwWXFNb_wSpWXJUKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8cf6f105.mp4?token=MJf3qTjmvYOn0oqAhYH9E-Iw_syzM9cOEICLuiiGcInTV2ABn_AhnWKhBvU71f7YXH5tn36hKtXfcLA5FLRfqOYhAz_EbygFSGcXvzlYe_kmtR_5D0u8KCBgxmvPvv850uIcsfHbbhBJLiuHIW_xQILr6Cu5tKSY3pUVO49RdFqGUL86xW6qqkJX2EzjnKasdpJj21ytwL7PNPY4tR7ZkliFzMiH6msIDTCLO0N0RtF2tqMfVsj3UFfcjz8ZiJmN9bfF6v6Eu5JbKVWF2prkH4aZw_E9poQAsGjZ68IGuIbFm80-o8z_4iD8aAE9AlocbJyiAUwWXFNb_wSpWXJUKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اخبار اولیه از حمله آمریکا به گذرگاه مرزی «شلمچه»
🔹
رسانه‌های عراقی با انتشار تصاویری گزارش داد که منطقه‌ای در نزدیکی گذرگاه شلمچه در مرز بین ایران و عراق، هدف حمله تروریستی آمریکا قرار گرفته است./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/674345" target="_blank">📅 03:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۳/ یک فروند از سه فروند کشتی متخلف که قصد عبور از مسیر ناایمن تنگه هرمز را داشت دچار آتش سوزی و دو کشتی دیگر با سرعت به عقب برگشتند   روابط عمومی سپاه :
🔹
ملت عظیم‌الشان و بپاخاسته ایران اسلامی، حضور عاشقانه شما در صحنه، نبرد با استکبار را…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/674344" target="_blank">📅 03:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674343">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۳/ یک فروند از سه فروند کشتی متخلف که قصد عبور از مسیر ناایمن تنگه هرمز را داشت دچار آتش سوزی و دو کشتی دیگر با سرعت به عقب برگشتند
روابط عمومی سپاه :
🔹
ملت عظیم‌الشان و بپاخاسته ایران اسلامی، حضور عاشقانه شما در صحنه، نبرد با استکبار را روح بخشیده است و دعای خیر شما پیروزی رزمندگان بر دشمن متجاوز را تضمین کرده است.
🔹
سه فروند کشتی نفتکش با تحریک و وسوسه ارتش کودک‌کش آمریکا قصد عبور از مسیر مین گذاری شده جنوب تنگه هرمز را داشتند که پس از انفجار و آتش سوزی شدید در یکی از آنها، دو فروند دیگر با سرعت دور زده و به عقب برگشتند.
🔹
نیروی دریایی مقتدر سپاه تاکید می کند که تنگه هرمز در کنترل ما است و تا زمان ادامه شرارت های آمریکا در منطقه، کاملا مسدود است و هیچ نفتکشی وارد و خارج نخواهد شد و هر کشتی که فریب آمریکا را بخورد و قصد عبور بدون هماهنگی با جمهوری اسلامی ایران را داشته باشد به همین سرنوشت دچار خواهد شد.
🔹
به آمریکای متجاوز و کودک‌کش اخطار میکنیم از شرارت در این منطقه حساس و به خطر انداختن کشتی های تجاری و بازی با امنیت انرژی جهان دست بردارید.
🔹
به مداخلاتی که جز بحران انرژی و کاهش کود کشاورزی برای جهان نتیجه ای ندارد پایان دهید، این شرارت‌ها جز بی اعتباری بیشتر و شکست جبران‌ناپذیری که به زودی خواهید چشید نتیجه ای برای شما نخواهد داشت.
🔹
به یاری خدا عملیات تنبیهی برای این تخلفی که کردید انجام خواهد شد.
و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/674343" target="_blank">📅 03:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674338">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
مقام ایرانی به رسانه روسی: برای حمله زمینی آمریکا آماده‌ایم
ریانووستی به نقل از یک منبع نظامی ایرانی:
🔹
هرگونه حمله آمریکا به تأسیسات هسته‌ای، با پاسخی فراتر از انتظارشان مواجه می‌شود./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/674338" target="_blank">📅 02:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674337">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ادعای روبیو: توافق با ایران دیگر لازم‌الاجرا نیست  وزیر امور خارجه آمریکا:
🔹
توافقات بر اساس پایبندی به تعهدات هستند و ما با ایران توافقی کردیم که آنها سپس آن را نقض کردند و دیگر لازم‌الاجرا نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/674337" target="_blank">📅 02:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674336">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای روبیو: توافق با ایران دیگر لازم‌الاجرا نیست
وزیر امور خارجه آمریکا:
🔹
توافقات بر اساس پایبندی به تعهدات هستند و ما با ایران توافقی کردیم که آنها سپس آن را نقض کردند و دیگر لازم‌الاجرا نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/674336" target="_blank">📅 02:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674335">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODWoow3rrf6Os80Z8fjbZB3Nwbfd5t3x5NNK-fheMo19-RtO5jcVhSut57ZRTgJDjIXJqBmrV4uAHQYBPgOR51xcGUP2B5XRyaovLSWKokML5eKGkc2llQbbD3hh6LUh_TBv5WZMqZJq3V-VIYxNZyVCMD9Q3w_mio3gn-qTyXMoHtb_inar9A-LuixOa1Zuz9yL5LSJ0X9ex2Y-o4LopskHJys5j0ATm-efJHbnHfo4ZW5uq0JhUYeV6_7Xd0SUZKP3TMItXCwZND3cxIMugCDERktOCRnCGfF_BTLaL20sbQSJ8XS6BzM5tKEfMt4oBSSo0Cvo93Iml7yY6te7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا از لحظات خاص و خاطره‌ساز جام جهانی با حضور طارمی، رضاییان و عزت‌اللهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/674335" target="_blank">📅 02:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674333">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
الجزیره: مجلس نمایندگان آمریکا در طرحی اولیه، اختصاص مبلغ ۹۵ میلیارد دلار را جهت تأمین مالی اقدامات نظامی و درگیری با ایران به تصویب رساند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/674333" target="_blank">📅 01:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674330">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=BsVBgWeXu37boxOoOkQYp4uk-WXSqjbog1h_VFBOcvJYHMN9ZtvK4Qf46vrhgR0WqKMPijuUDCpNqw8hwRes2l8W75ff8pWtM2lG-Hp8jIVyI-m-Ql6kdTEbvTMgVG_S_Dnh1CPSfwdF1MD7Gzfa8XNv53i2C3c6PyDqb1-CiV3GZzlUo37mHfC3SSWSlJ-Tfo6U6JXx1oLffAaX2WGmeb4ktepPG2gmJNiF1IRhOG9Tizj6XJOF1o3se8ZrScKFkHzqK2tTZZNfB2m1EVgEEchp4CXU6Bqcw8lgzJAoZjI0-Z18wTuGYd1qWEgqlr4M2lxBUoP1FLiN3frLSG1Smw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=BsVBgWeXu37boxOoOkQYp4uk-WXSqjbog1h_VFBOcvJYHMN9ZtvK4Qf46vrhgR0WqKMPijuUDCpNqw8hwRes2l8W75ff8pWtM2lG-Hp8jIVyI-m-Ql6kdTEbvTMgVG_S_Dnh1CPSfwdF1MD7Gzfa8XNv53i2C3c6PyDqb1-CiV3GZzlUo37mHfC3SSWSlJ-Tfo6U6JXx1oLffAaX2WGmeb4ktepPG2gmJNiF1IRhOG9Tizj6XJOF1o3se8ZrScKFkHzqK2tTZZNfB2m1EVgEEchp4CXU6Bqcw8lgzJAoZjI0-Z18wTuGYd1qWEgqlr4M2lxBUoP1FLiN3frLSG1Smw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادی که به‌یاد دانش‌آموزان شهید مینابی پرتاب شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/674330" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674329">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی
سنتکام: با دستور ترامپ، و با هدف تضعیف توانایی‌های نظامی ایران در تنگۀ هرمز، دور جدید حملات را‌ آغاز کردیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/674329" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw-Z9zDXHkw6BoD-kZRDAqmGJllp7EPkf7prPp7ibVy7RSNOtuSNYKzYjPImhxzWclAbfyuIe_HKM4I_TmQ4vz6BHibC47Tz_xjLGzaLurBKFGJvxmL7yZzjJZIjUreyHvgpxPkyVhTg9Jd6_Mzutdt18qadBewc5ir-Wh1oT92MXwER3kyJl19yyps_566Zx7w7J5VwzVwh-oembmtNRTq9c8ZUpnECv6dtwISG2TOW7E-PAyOnySY5RYjXRKY3aob5TwrW-ghzXlB31RQeh2uwsII1fgDFKqSURFXcMtlh-R95p5R8X5ezGgKXCJyZ84fpN8tlCRGxB3rcXpdC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش خاندوزی به عصبانیت شیطان زرد: این تازه آغاز ماجراست
🔹
همین حالا سربازانتان را به آغوش خانواده‌هایشان بازگردانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/674324" target="_blank">📅 01:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674321">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
انصارالله یمن می‌گوید دو نفتکش سعودی به نام‌های «ENCELA» و «LAYLIA» را با استفاده از موشک‌های بالستیک، موشک‌های کروز و پهپاد هدف قرار داده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/674321" target="_blank">📅 01:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674319">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
هدف قرارگرفتن نفتکش عربستانی در شمال مرز یمن
🔹
بر اساس گزارش های دریافتی اولین کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/674319" target="_blank">📅 01:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674316">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
فرمانده قرارگاه مشترک خاتم الانبیاء: کارکنان پدافند مردانه ایستادند تا ایران استوار بماند
🔹
جمهوری اسلامی ایران امروز با منفورترین جنایتکاران عالم روبه‌رو است؛ دشمنانی که هیچ‌گونه پایبندی به اصول انسانی، اخلاقی و حقوق بین‌الملل ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/674316" target="_blank">📅 00:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674315">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
جنگنده‌های نیروی هوایی ارتش جمهوری اسلامی ایران بر فراز آسمان تهران به پرواز درآمدند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/674315" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674313">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2a57c4cc.mp4?token=RrpQEeK5fYIdMP_j6w1j5-93XPoVOOzG6ZnL-AP8RMIhejG3tvwQ1qTljULNsIXrAOzLT4TWo3ciYyV0ewG84ZR5GBfhaOWGAuJYQTYjD5vllm-CU43Tk7mVVU8rT2UYUkMVc9fqW5SVPtlAtJaGyksf3ezMnC00zi37LHDmhL91wmJ5f-nS7p38yoAqws5SwjLmOafk9HAYvPOq0Dm3uShRsxSZ5k4krFApZzELpLKrbQGMPvs1km7AK-mGwlq-GNsu-YGor6KsVT7fZdneDSCIqaQvgU8A0CpE1MB1epfq_lEzhHJQLUhnngtRAfXfnh5FwQj7geqnUs4iDxYFeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2a57c4cc.mp4?token=RrpQEeK5fYIdMP_j6w1j5-93XPoVOOzG6ZnL-AP8RMIhejG3tvwQ1qTljULNsIXrAOzLT4TWo3ciYyV0ewG84ZR5GBfhaOWGAuJYQTYjD5vllm-CU43Tk7mVVU8rT2UYUkMVc9fqW5SVPtlAtJaGyksf3ezMnC00zi37LHDmhL91wmJ5f-nS7p38yoAqws5SwjLmOafk9HAYvPOq0Dm3uShRsxSZ5k4krFApZzELpLKrbQGMPvs1km7AK-mGwlq-GNsu-YGor6KsVT7fZdneDSCIqaQvgU8A0CpE1MB1epfq_lEzhHJQLUhnngtRAfXfnh5FwQj7geqnUs4iDxYFeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف قرارگرفتن نفتکش عربستانی در شمال مرز یمن
🔹
بر اساس گزارش های دریافتی اولین کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/akhbarefori/674313" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674312">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0ipRLQgECld7ylbS1TH1sxULs8HX7HIVDDvs_o1SXnIiNynF7YtbShvrSisLFmJSAieJVN9GrYW7BvphTtAL50n6CnUQLjas3Bn_14KmdbVyQ-UMS5CQWZNEQNurvkgtsWnk3PZQMtgEAR4DjNrkS0YHfQx8PkNQvu7vPVxpFNriw9mveiyj5aMZhKIl-pNcelBavmw84jtd_RRAu0wIBc2TXug7d_2TzYOEL426EQtSYl9AHt0toqXAbcObz9TwAr9ygw3Yyl_ajQhv9q7B3yCqMAK_OFiLK2EpV0kfeDBon1LHZC1q6N3ERgbFSKnoK0LO--YL-ys2HE03H8zQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار الجزیره: منابعی در ایران می‌گویند پرونده کوه کلنگ (کوه تبر)، طبق روایت اسرائیل و موساد درباره این تأسیسات هسته‌ای، با هدف تأثیرگذاری بر تصمیم‌گیرندگان سیاسی در واشنگتن مدیریت می‌شود
🔹
برخی منابع نیز می‌افزایند که در صورت هرگونه حمله، اسرائیل از هرگونه پاسخ ایران در امان نخواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/674312" target="_blank">📅 00:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674310">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
پاکستان انصارالله یمن را تهدید کرد
🔹
پاکستان به جنبش انصارالله یمن هشدار داده است که هرگونه حمله به کشتی حامل پرچم پاکستان یا منافع دریایی پاکستان، «تهدیدی علیه امنیت ملی ما تلقی خواهد شد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/674310" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674309">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما: صداهای مهیب شبه انفجار در اهواز / انفجار در رامشیر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/674309" target="_blank">📅 00:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
آمریکا و عربستان توافق هسته‌ای امضا کردند
🔹
وزارت انرژی آمریکا گزارش داد که آمریکا و عربستان سعودی، یک توافقنامه همکاری هسته‌ای و همچنین یک توافقنامه تضمین‌های دوجانبه امضا کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/674304" target="_blank">📅 00:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674303">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0891f90f8.mp4?token=erWvepTAVjAzxfI8OrYkS7lZkmRqYziQ28pX4XliPyuBx55u6AeHABVPPxj4NQLwnNOe09BUg1OCFA5ftRehtaODaCsaDJq1OANeQrA0P_gitOX5MEznkqgj2ck55T6jjjGqEeRU5OzYFpUmR2YVWQvIhDGoZ7Yt_LTaALb0E8ZM6q_oKhaxCA19W8_TL4upT1oCuweV8suG1JUtXr_bEMMagRQ4yC7TZL1XzXbZ03vy-fBpn6PRzG4HR7Bxmz0Ky2oua9nKLgvvfSRPLH0MKMWZRTybsC1y98TLB1WBQotuSXkGAYtPViIP3f5PToW9DoeHdFBaRuu9dvH9ByTsbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0891f90f8.mp4?token=erWvepTAVjAzxfI8OrYkS7lZkmRqYziQ28pX4XliPyuBx55u6AeHABVPPxj4NQLwnNOe09BUg1OCFA5ftRehtaODaCsaDJq1OANeQrA0P_gitOX5MEznkqgj2ck55T6jjjGqEeRU5OzYFpUmR2YVWQvIhDGoZ7Yt_LTaALb0E8ZM6q_oKhaxCA19W8_TL4upT1oCuweV8suG1JUtXr_bEMMagRQ4yC7TZL1XzXbZ03vy-fBpn6PRzG4HR7Bxmz0Ky2oua9nKLgvvfSRPLH0MKMWZRTybsC1y98TLB1WBQotuSXkGAYtPViIP3f5PToW9DoeHdFBaRuu9dvH9ByTsbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیاده روی زائران اربعین در میسان در جنوب عراق به سمت کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/674303" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674300">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86ca146bb.mp4?token=MpS9P87QWQcsiJZ296XgcRO8DtvQY-B8v9qquMqS3RjsEVYX8ftENdGPRIQIdGyT44c0mXwtQHEwO94VlmN-djCUlPLzVA7qn5yRm7ciuTos3r0k1u4zawvj5bz7z2cZsukeutW_jp1aFSRU7rRQO7wRagWYkjLCMjjBsgCfpgwvq2Tx82tEnKPWj8wCpFE11dWha64aUXwf_EiNNJaNTo8taUb3fLsIZdi0W89151Q0sr0eD6_ePDGqup3rvU_rT7l2cx9J2GX5cr0IHI3hVm7NDN49cjI-Dyr-c-0be0_4UjvN1ay1Mb_OKlmKNPIVmGZfY8__h0XOh1UxAXieXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86ca146bb.mp4?token=MpS9P87QWQcsiJZ296XgcRO8DtvQY-B8v9qquMqS3RjsEVYX8ftENdGPRIQIdGyT44c0mXwtQHEwO94VlmN-djCUlPLzVA7qn5yRm7ciuTos3r0k1u4zawvj5bz7z2cZsukeutW_jp1aFSRU7rRQO7wRagWYkjLCMjjBsgCfpgwvq2Tx82tEnKPWj8wCpFE11dWha64aUXwf_EiNNJaNTo8taUb3fLsIZdi0W89151Q0sr0eD6_ePDGqup3rvU_rT7l2cx9J2GX5cr0IHI3hVm7NDN49cjI-Dyr-c-0be0_4UjvN1ay1Mb_OKlmKNPIVmGZfY8__h0XOh1UxAXieXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده تد لیو، سفیر آمریکا در سازمان ملل، مایک والتز را درباره جنگ با ایران به چالش کشید
🔹
شما حتی نمی‌دانید در این جنگ با ایران چند نظامی آمریکایی زخمی شدند. واقعاً باید از خودتان خجالت بکشید که حتی ابتدایی‌ترین واقعیت‌ها را هم نمی‌دانید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/674300" target="_blank">📅 00:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674299">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW4wiRDUO6pJpfiGOHoAxHAamb-c4W33vA33RGx2Z34PGuL4bSHU9nFaH7hlZKo8bRmDtxuVAainan39yWqS4ZWtyi1vWz74xt3k0GsFdSW7GX_sVboS4cDp5df4-d_1FCWM2PVLjsosfoovRpY9JpO93oz4TVITDEnECZvhKujUVzFz8shuuFxTkx_9nOUTC2mLKUvYiYGbe2_xvJGKVyOVNoMJGI7hggwpSVwsC7EbQNdpcstzqrgZGHqqRWRvaiihrVXnIYNHawyAFD8_0yxvdfDz_Idji1NTAGgQkHQZQ27JnfaXE-yarTlQLmEe2QZ3X2U1mHe1gT2SV2hdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اثرگذاری در کمپین های سازمان ها  معمولا مهمترین عامل برای موفق بودن کمپین حساب میشود
ایا هر تبلیغاتی و  یا اطلاع رسانی ، تاثیر گذار خواهد بود ؟
استفاده هدفمند و هوشمندانه از ابزار هایی که در اختیار دارید و یا میتوانید استفاده کنید مهم ترین عامل اثر گذاری خواهد بود
مشاوره تخصصی و طراحی کمپین های تبلیغاتی و خبری با ما در ارتباط باشید
👇
@marketing_mn
برای رسید به اثر گذاری ، ما در کنارتون هستیم در اژانس دیجیتال کست:
https://t.me/+fZbPfI0dd-41ZWNk</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/674299" target="_blank">📅 00:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674298">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMzs3sV83G7tmUODt4BzoidHJfwiwmdpV0FndA1vHHj46MpPUkfFqJHmSVQzTzfW_VViaB4naezy6c0utYdqDMNj9FpqGFW5DjQ6qF8warSdaseuEg1-FheRptm9q-avO_IWgGYwMa5YCUW3-EZ-_lb1Dwrs7NRri7Wu0UUWLuVThoK9e6pDdIIBtePRxHcht0fFL2IHWCe4FwcVCEwuVi4XiOqjAtLXEpG8kkFh6VDsqxUSElxXlCRZ2dkd4X2i9L0iocIipQ9B8lvwqLqfL74y4Mr1JDJupORRHeC04-oxVIt22fQULIiHRoqHrYtT-wSCC6aeTjy4UlmYwfGFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
خبر منتظر نمی‌ماند
با کانال خبری ما، تازه‌ترین اخبار و تحولات را سریع، دقیق و بی‌واسطه دنبال کنید.
📲
عضو شوید و کانال را با دیگران به اشتراک بگذارید.
@Parstimesnewsiran</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/674298" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674296">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unYgsAD2cPuBmpj8Cstb4pQTBlQBLPMB3RV_rgr1iNebLdhvTRoUZ0-Ne_Nkr54c1z2mqDqDQM2flQ8CLNiCZTNUqeCviKbdLH1eVY1ZfVuZRVjCTHT6cCeCe9k4ILv5oSjoRCFLrWUl6mp9ylN_O3qHaxsruqobPwZvPFr02vb4VEnQyBE6DcRUxBaci0HTt147LM-UZHHaMHEIeURlIwqeyozZwWVPGs1KejaR2y6DG7OvMUoV0m5mj3Ne6NP77imS2Y6zKkbglJ_K8L9p9i9RkriswTgnGdaawOZbzoXwkvYhLzN_h52tIgN3FmRQDRFQTTnL4h7Zq6Z28msLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مگاتخفیف
سوپرمارکت
۴۵دقیقه‌ای دیجی‌کالا
شروع شد!
🔥
🎁
کد تخفیف
۵۰۰ هزار تومانی
➗
تا۷۰٪ تخفیف
روی کالاهای شگفت‌انگیز
🚚
همراه با
ارسال رایگان
امروز از محصولات سوپرمارکتی، شیرینی و تنقلات تا پروتئین و میوه رو با تخفیف‌های ویژه سفارش بده!
🫂
کد تخفیف ۵۰۰ هزارتومانی ویژه کاربر جدید:
6TFG
🫂
۳۰۰ هزارتومان ویژه کاربران قدیمی
(۳ کد ۱۰۰ تومانی):
GD33
فقط امروز
⏰
بزن بریم خرید سر ماه در دیجی‌کالا
👇
dgka.me/Wcjhnscdl
dgka.me/Wcjhnscdl</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/674296" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674295">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afp7JiGwtbAHfQOMyco9Y2ATQ2CeJSIQf2CWtBwQlqZJdqHOFFUBsXdp3_rA5Ix6KiDVxl4VxN2J25TCJ2imcJQGakr_eRVi42ESwrqGkueCtQDyNVx9Ly-CISwYXWvEBPQdpi6x14VX2dfCTw-gCcLUPpNvRxm_Nr_oJmaIRlCAqxvpeTIbChFYNzYCI-2htuWll2ddn6d_EvlKJuwVhPrCJZHpBD2qCwTXSeMflpEh7iRu0WpMQvecFkHawR93R5_AlrzMJ29CEJFn4Id_5jBaM6RFkMtICHlg718C4K8cI-qUSNNz7DX3sNogWT7LxWkcLwZ-YhlvsCdtBKlCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/674295" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674294">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a1a817ce.mp4?token=Laz3p85S1tdIM4ozHeCLemU_OZZge4JpGuUY3JU_EofyJxernwHyp2eQ1RWUpXOBqB6DzJHg9V2-sWkOlQseODRC5SgpI_5nSgSRB7FaF_MjAZu7jK6gIkxED81tOF9UuopH14I8unDbUHAPQhLLfApUZYIgaHvkYGPmy7UQDG0wBV9I-pMbihOtkRe-4T1z0gKNnYeHJfKF4d1lqoWEdhzMbyOm6RXodyC90bh79DKaqiXqCBRbL4Ws46kIEbwuv6-bFAE8Fz0ajAbuIzRNr6x9sI7hevaddpEwHTxgDzQef57iQux9kf3Q1tVivsGA9IoQQt4xSvM89ZyZZ05a5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a1a817ce.mp4?token=Laz3p85S1tdIM4ozHeCLemU_OZZge4JpGuUY3JU_EofyJxernwHyp2eQ1RWUpXOBqB6DzJHg9V2-sWkOlQseODRC5SgpI_5nSgSRB7FaF_MjAZu7jK6gIkxED81tOF9UuopH14I8unDbUHAPQhLLfApUZYIgaHvkYGPmy7UQDG0wBV9I-pMbihOtkRe-4T1z0gKNnYeHJfKF4d1lqoWEdhzMbyOm6RXodyC90bh79DKaqiXqCBRbL4Ws46kIEbwuv6-bFAE8Fz0ajAbuIzRNr6x9sI7hevaddpEwHTxgDzQef57iQux9kf3Q1tVivsGA9IoQQt4xSvM89ZyZZ05a5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سالن رقص شیطان زرد پایگاه نظامی است
ترامپ متوهم
:
🔹
ما در حال ساخت یک تأسیسات نظامی عظیم در کاخ سفید هستیم. این یک سالن رقص است، اما همچنین یک تأسیسات نظامی بزرگ، یک پایگاه پهپاد در بالا و چیزهای عظیمی در زیر آن است... این یک پروژه باورنکردنی است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/674294" target="_blank">📅 23:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674293">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5ed84ef5.mp4?token=TnCf4mKLeqgwRVq44aGJSmvDPZl67coW-Pc-yysb9OlePz19W2FkO5GoREMEgi3UNpvu06GXkV6AeKCqjXX8coreF9E1-UyKQztgRcaoxconVvVZWPyTj34DeRrozPcSFfLWmhxAJs18vXyCSjQDF17XPvFcUWAfi2up_ac-yy8CT98izrjwZT5COzZ97c8SJQKYIB3W2c7CEq-6xu3KQ7WYangTSbNlkajx8700JzXzz2OSnjWpsfwBAiDkhtoKtG97fRnxOKX8t8TlRILCQUT6tVfex17JbzZif0QJ9slS-k8LaxZ4Ra39vV_NU-wUxjifROBZoGg31z2HHiUnbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5ed84ef5.mp4?token=TnCf4mKLeqgwRVq44aGJSmvDPZl67coW-Pc-yysb9OlePz19W2FkO5GoREMEgi3UNpvu06GXkV6AeKCqjXX8coreF9E1-UyKQztgRcaoxconVvVZWPyTj34DeRrozPcSFfLWmhxAJs18vXyCSjQDF17XPvFcUWAfi2up_ac-yy8CT98izrjwZT5COzZ97c8SJQKYIB3W2c7CEq-6xu3KQ7WYangTSbNlkajx8700JzXzz2OSnjWpsfwBAiDkhtoKtG97fRnxOKX8t8TlRILCQUT6tVfex17JbzZif0QJ9slS-k8LaxZ4Ra39vV_NU-wUxjifROBZoGg31z2HHiUnbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: ما به همین ترتیب در جمهوری اسلامی ایران در حال پیروزی هستیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/674293" target="_blank">📅 23:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674291">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmbGeFA7ey6Mibc5JcyMQcvPHFbp_tZ5wT_ibCYZVFHQSRiXj4mBbF9W_NYAlMftb9qZe9athbZT_xDiSg2439-dRrOQUh-EaZ5Dob2IvlxnU9eTvVqSiGhJYAR8-R6fZYpTStgh-AIHUcIyOc7Ob_vix-zpsH0RS4zRfYEeCaOW0QwD_IaGNF1ESQpBG4tatVAawEJ5QEg7imal59_oHw_RzF48x5BZ4Dgz6XLBBHxZx1cHJpzxkoxuZaWb1wVMMsF8HSOlTefHx1hCyTX5LtMqISlkCVEyUQZYTSrd4iz-zFsUDj2bazlqydmG76hQNpJVUaXADpLveuasBajSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه انگلیس اعلام‌کرد که دیپلمات‌های این کشور موقتا از ایران خارج شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/674291" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674289">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKtIA7vbYwuuFryng_X5m6ebghx85hBQN2RKQSqsq5dVxypTWqNikItckcnEG9BfYJhNi59Ojzl0JpoB6PBF4QRTVPbuN-kLNfMBql15XXA7_dmsNAUkNlZ-jeSu5IqqXewC2e_HBj0AgvnXdPttojW2ZsRSxxOhZvcXx93QBrufE3ffrJloG3QOhOZq7FPXNH517pweMvY_vVk1OMUBQI7287JZ3uDAVUZYmI7OqkrJ0alTNDkgqvaAeKrdBDyXluyB5_WNGty6pRanQpJK-HPmE9k_YqhPAxWcssF3LbFkcEIRj1TQFcXHbvBIGYBiBogd4USI5ccJGp5sQEQv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار موسوی: به پل‌ها و نیروگاه‌های ما تعرض شود خاموشی برق متحدان و میزبانانِ کودک کشان، قطعی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/674289" target="_blank">📅 23:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674286">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
با امضای تفاهم نامه حمل و نقل شهری، شمارش معکوس مطالبه گری آن روشن شد
🔹
نصرتی معاون عمران وزیر کشور در مراسم امضای تفاهمنامه همکاری در زمینه تامین و توسعه ناوگان حمل و نقل عمومی شهری کشور: در راستای این تفاهم نامه ۱۸۴ خودروی نردبان آتش نشانی، ۱۷۴ آمبولانس امدادی و هزار دست لباس امداد و نجات در حوزه ایمنی تامین خواهد شد.
🔹
در قرار داد اصلی مقرر شد که چهار هزار اتوبوس در دو فاز ساخته و تحویل شود که فاز نخست آن یک برنامه زمانی چهارماهه برای ساخت ۲ هزار دستگاه اتوبوس است و همچنین با همراهی وزارت نفت و بر اساس تأکیدات رئیس‌ جمهور و وزیر کشور، قرارداد خرید این تعداد اتوبوس و تعدادی واگن قطار برای ۹ کلانشهر کشور که با کمبود واگن روبرو هستند، به ارزش ۲.۵ میلیارد دلار وارد مرحله اجرا شده است.
🔹
رسانه ها یکماه بعد، از میزان پیشرفت توسعه ناوگان حمل و نقل از ما دولتی ها سوال کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/674286" target="_blank">📅 23:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674284">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d71d7784.mp4?token=FztbhDYz2JEvuprso7TdpuH7SADbCzc7brQcDMYZ3GIE2KTLHu9Byrm9Dtp9f1UhZRHNGKJm5eEnYhz6hA-bNUdp7azyeH6maCGtkXH2RsDLoCKzT7t1UboYuymB97tEZU5yYad2oNJ1ON--rhQoNnI2JZcnJJ1ZmwH9JZmwzNop2UiH0sGRIW8nbNVnkK-IZpz4VIy-BLthrCYxhsYuecUmzzMX8OSbJ5Y1XxtTjwZC-gCNsEepsI5Am3FSc1tA86JsypWuo1T5U4dW1F7QLaL_ndDDePs31g3xh5cM8jbgeJu8jRSoA2ukbeCgunEcpLot7tZwPDTEUCMRWzV_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d71d7784.mp4?token=FztbhDYz2JEvuprso7TdpuH7SADbCzc7brQcDMYZ3GIE2KTLHu9Byrm9Dtp9f1UhZRHNGKJm5eEnYhz6hA-bNUdp7azyeH6maCGtkXH2RsDLoCKzT7t1UboYuymB97tEZU5yYad2oNJ1ON--rhQoNnI2JZcnJJ1ZmwH9JZmwzNop2UiH0sGRIW8nbNVnkK-IZpz4VIy-BLthrCYxhsYuecUmzzMX8OSbJ5Y1XxtTjwZC-gCNsEepsI5Am3FSc1tA86JsypWuo1T5U4dW1F7QLaL_ndDDePs31g3xh5cM8jbgeJu8jRSoA2ukbeCgunEcpLot7tZwPDTEUCMRWzV_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای شیطان زرد: من [جنگ با ایران] را یک درگیری محدود می‌نامم
🔹
ما با جمهوری اسلامی ایران یک درگیری محدود داریم.
🔹
آن‌ها می‌خواهند به توافق برسند، اما من می‌گویم که آن‌ها برای توافق آماده نیستند.
🔹
آن‌ها برای توافق آماده نیستند. خیلی زود آماده خواهند شد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/674284" target="_blank">📅 23:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674283">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tObVzKsD-NdhoFB94TOijRg4tdKvmV2xzT_eAtrPo5LQi2oOPt14u78YnkBLhyfLTqOvA5tkBOsni44i07hGYgJoU5C8fyecqn1r7PaIL7bQRNIYmdw-Pp1m5llHydvX3ZUCHb9590WHarDrc_5GUf_3kmsfEph1sPVqaP_jcm3T-ctZq8U7axulnml-0wlH-vQQJJ-YJ2kOlmRmhKn7eoetZVOrcifTuPsjjRZkprWP4oro2O4ipAw_pDTmPgaIabHqthPMi0oGO1NplEVieX6uZiJ6FgOcvLZK9xvDnNR_9T_0CtMtbEMBl28sKy7abB5cC5rrShqFeyY_oud5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار تازه بریتانیا به شهروندانش در غرب آسیا؛ آماده اختلال در پروازها باشید
دولت بریتانیا:
🔹
از شهروندان بریتانیایی که در حال حاضر در غرب آسیا حضور دارند، درخواست می‌شود برای احتمال لغو پروازها، بستن موقت فضای هوایی و اختلالات احتمالی در سفر، آماده باشند
🔹
در جنگ قبلی ایران، بریتانیا، ۱۵ ساعت قبل از جنگ این هشدار را داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/674283" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674281">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b2c33c81.mp4?token=qfD6u9J1L-V7YptJxaKZ2sAVYJPlz6nF-qsaI38cuUOoKmzpuEKUuNjfpRsC7OSrSzsm2hk-wcWYxaIyjd9_X7nmXFyE3X9tTr9ZGGkjhQHmPiYjNBDvJK-NbyIAC96rIOXUVZYNuxgMPR-2vaTjbp6CqderFpZpu7Z16dpBi_oPViitOhJg_Y7SUEi842Z5Qud87NwwCPojSdxa-vuIEi0PkhBLHwLqwDL_lIEplJCyXfWbI5fCGoyTf2klYGt4N02Xb1FQ9I_IiMzSRbeMqcOrsooLI6gfoW6vIWIXKzxRMFdxa3GqX15GJ_2yLbTtk1TuS2a481galmrSs-rSog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b2c33c81.mp4?token=qfD6u9J1L-V7YptJxaKZ2sAVYJPlz6nF-qsaI38cuUOoKmzpuEKUuNjfpRsC7OSrSzsm2hk-wcWYxaIyjd9_X7nmXFyE3X9tTr9ZGGkjhQHmPiYjNBDvJK-NbyIAC96rIOXUVZYNuxgMPR-2vaTjbp6CqderFpZpu7Z16dpBi_oPViitOhJg_Y7SUEi842Z5Qud87NwwCPojSdxa-vuIEi0PkhBLHwLqwDL_lIEplJCyXfWbI5fCGoyTf2klYGt4N02Xb1FQ9I_IiMzSRbeMqcOrsooLI6gfoW6vIWIXKzxRMFdxa3GqX15GJ_2yLbTtk1TuS2a481galmrSs-rSog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال ماریو نوفل از جو کنت، رئیس مرکز ملی مبارزه با تروریسم آمریکا که در اعتراض به جنگ نظامی با ایران استعفا داده بود: آیا از گستردگی مراسم تشییع‌ها در ایران شگفت‌زده شدید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/674281" target="_blank">📅 23:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674280">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
ترامپ به سنتکام دستور داد دروازه‌های جهنم را به روی ایران باز کند
👇
khabarfoori.com/fa/tiny/news-3232437
🔹
پشت پرده اظهارنظر جنجالی هگست درباره یک بمب مرموز
👇
khabarfoori.com/fa/tiny/news-3232388
🔹
قالیباف به ترامپ: اگر ما نفت نفروشیم، کسی در منطقه نفت نخواهد فروخت
👇
khabarfoori.com/fa/tiny/news-3232438
🔹
یک چپِ دیگر رسوا شد | جنجال تصاویر تفریحات لوکس خانم وزیر در هتل لاکچری
khabarfoori.com/fa/tiny/news-3232133
🔹
عکس شکیرا بدون آرایش و با موی بسته
👇
khabarfoori.com/fa/tiny/news-3232381
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/674280" target="_blank">📅 23:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674279">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH7K6UehmwT8nfKNwYRb2i-O5TWHcmQu0L68pN63gUZ2LZJCOM2h3KClTew0PZX5A3lGP_lZ-3tdHPQibKkJJUL6bNgYfmeRSFDJQzyEKQXgm67H6K-_GU8BSp2R-jbxf6XSpXNERFer68cTWnEgBz7AdEvu3JibIfdwwFv8j9UH12_njWFARPezZOPpWIHIVOK2FOZqQTt8eQ-DK4bjn1X_jsk3uO9SKlNpZO2xMt7A3-Y2hoH9kQB8zc32fmZNaUcFrGGNHXQhEhTizFRmWK-s4YoHrFHCsA49OkuHuMQ9F1Ggw8xWDUvyDgqBoh0gKlwlreefh7x9pZ6eZXNodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💪🏻
راپیدو ۱۸۰ NMX؛ از جذاب‌ترین گزینه‌های نیکران‌موتور در کلاس اسکوتر
🔹
۱۷۵ سی‌سی
🔹
تک‌سیلندر، ۴زمانه، ۴ سوپاپ
🔹
سواری نرم
🔹
هندلینگ عالی
💬
برای مشاهده قیمت و سایر مشخصات موتورسیکلت ۱۸۰ NMX، روی لینک زیر کلیک نمائید
👇
https://l.nikrun.com/nda</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/674279" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674278">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPSRx2k-gFrh3a4EBwc41YfvILfbS3Gt292LeFYrmMsvgTG9ouhUCoCzoTFnuONDENRWvKwacr69AzVZ-fImg4mjGiQMhoS9gL9icJynO1_8-J-gg_Nu66T6rqUW8CAwcMfYu58DzoBrUdHtyv-VQ0BNJVrxzbGO-SbNvrBcCZH8y2ikc0gCiV4xRW3x0sGx2Gd3rlREA-No1DkGl7O_iR-I00LgEq5c3y5pfnLjKsU8zHao5iCPYlXkRjkWk0UDhcfQMnzNaQSREsQWrGiPBX61PV75db7CeGYQ41Z6oUNtMsZmpKNz71isO88Gd51BADJ0wTN8mpgqPBJrqfj_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ننگ بر آنکه خواسته، شمر به ما کمک کند…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/674278" target="_blank">📅 23:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674276">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1097566db.mp4?token=pJ-aiXEHQGjbRfsUPwxu-2pSqknNIcdhQnJNEv6e5OPzmP8QX2yFPQGGBJLQY7N8S57AhOwfGmOwECWqVD1Inu9X9AWzOLy6MuQih774pL5cxn61Gp1_9z9SM6DHUSMam0x8pw7jKxrxdchP6VN2kLJS2FNUsZyAhSnXRJrmu0MUa2JdKAycKjZ_FIFUdcAwJEpDVRz8xwxUpC5KiSBlUeP1Zt5IPPmAAWkt9qO0krCSL2-IIwgQ-O9VS4zdSN1_uQ3BgCBMEET7iDH2gmtnvPeAZtfPEadJKjcJY_wbtlpH1_J4FQv5dypbwGvmZf51mVInrNcUAnmeCzCuZNztuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1097566db.mp4?token=pJ-aiXEHQGjbRfsUPwxu-2pSqknNIcdhQnJNEv6e5OPzmP8QX2yFPQGGBJLQY7N8S57AhOwfGmOwECWqVD1Inu9X9AWzOLy6MuQih774pL5cxn61Gp1_9z9SM6DHUSMam0x8pw7jKxrxdchP6VN2kLJS2FNUsZyAhSnXRJrmu0MUa2JdKAycKjZ_FIFUdcAwJEpDVRz8xwxUpC5KiSBlUeP1Zt5IPPmAAWkt9qO0krCSL2-IIwgQ-O9VS4zdSN1_uQ3BgCBMEET7iDH2gmtnvPeAZtfPEadJKjcJY_wbtlpH1_J4FQv5dypbwGvmZf51mVInrNcUAnmeCzCuZNztuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: ما به هیچ‌چیزی نیاز نداریم
🔹
ما به تنگهٔ هرمز نیازی نداریم، اما کاری که می‌کنیم به خاطر این است که چاره‌ای جز انجام آن نداریم.
🔹
نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/674276" target="_blank">📅 23:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674275">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
تناقض گویی دوباره شیطان زرد: به تنگه‌ها نیاز نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/674275" target="_blank">📅 23:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674274">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9c789150.mp4?token=QJVPS-0JuPLOhfpXkQrGQCHEASKrn8JLkBLybmIIp1bQmSDN5o9KqpH1InOJiwGK687mKUMhkz2IvT5g6xlMiQQOgRvx7F1F66hC3wwW8Y8RrrWEsY2jq0JObUuxgNB_h5qrqVwqGkqDRM4sCxwGw68v4NECdqKUzQjvcYHym5KyUT-FbSGEu8l3-MHot2aiDTZpkSmR_Q5GhwrXnAXbMM1ahA-TLJgwB5E_4peTxafesIwOWlKFr9_e1glbqlRGXIh8ujiKZanjx3XDv1yq0d7ndOdKTukmxCyQTNwGFw_zR3Heaif8UpVVm40aG-X3y5vQIXEWcTp4TNAJhWJEWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9c789150.mp4?token=QJVPS-0JuPLOhfpXkQrGQCHEASKrn8JLkBLybmIIp1bQmSDN5o9KqpH1InOJiwGK687mKUMhkz2IvT5g6xlMiQQOgRvx7F1F66hC3wwW8Y8RrrWEsY2jq0JObUuxgNB_h5qrqVwqGkqDRM4sCxwGw68v4NECdqKUzQjvcYHym5KyUT-FbSGEu8l3-MHot2aiDTZpkSmR_Q5GhwrXnAXbMM1ahA-TLJgwB5E_4peTxafesIwOWlKFr9_e1glbqlRGXIh8ujiKZanjx3XDv1yq0d7ndOdKTukmxCyQTNwGFw_zR3Heaif8UpVVm40aG-X3y5vQIXEWcTp4TNAJhWJEWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کانال عراقی «المحور‌ نیوز» به نقل از منبعی اردنی اعلام کرد که پس از ناکامی جنگنده‌های بریتانیایی در رهگیری پهپاد ایرانی، این پهپاد مستقیما به هدفی آمریکایی در شرق اردن اصابت کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/674274" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674273">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
رایزنی دیپلمات‌های پاکستان، عربستان و چین در تهران
🔹
سفرای پاکستان، عربستان و چین در جمهوری اسلامی ایران در محل سفارت اسلام‌آباد در تهران دیدار کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/674273" target="_blank">📅 23:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674271">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD-efVz8-5HyhaFhWm0NZErL4i_scimpTXqx7PMXUrxEaV9hvNvj3ycjpzVxhbLbSGfZBkTAsoQe7Vt-DQAp82-JtOxlIKksYMBhmwoFocF-6gPLMD8gGv53Eb85woAptiFuT_hT50UeAoyTBZ0PrG4vhh384wXmYkMZ4_5Y1v3ftjeOuoCH2hS5_M0Yp1Hn_GjdhRQWudlbsEfnvXqgs3xDR_9v5KyMniuTNitQeN_d3VXzU4eTk_v7QcIXfD5m6089n_KekDUxgYZ9_g1Vw5DoLwZe5XagCTezAbDlqNjf_L0JB5e7A_FR3ac87hPyb9vhYAUsmnU66WAxVU0BAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برسد به دست زائران اربعین
🏴
🔹
امسال هم با بسته‌های ویژه و مقرون‌به‌ صرفه رومینگ اربعین، ارتباطی پایدار و بی‌دغدغه را در طول این سفر معنوی برای شما فراهم کرده‌ایم.
📲
درگاه‌های فعال‌سازی:
🔹
کد دستوری: ستاره ۱ ستاره ۴۰ مربع
🔹
اپلیکیشن همراه من
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/674271" target="_blank">📅 23:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674269">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
حمله پهپادی و موشکی به مواضع نظامیان آمریکایی در شرق اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/674269" target="_blank">📅 23:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674268">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8nsSJJkP0yWui24rAIAJsEFDd3Tur5HqYPq8DYWy1AV0QIGoVrvxOUeLBh2je34Kk02uJwCBqNZycdPirQv4NL2L6ESp6iAionj9BcRKtkQWZWNzBskJ2_DF1FTQ1pxii2cPVhP0uslW9n_k-xHhzOkex0M2ryeNvj63o4bfzN4a6M6kMKYMpwn_bgujq8NZyQlAM77-rcCwB80hX3UicCbAzKqIfvYzkNpnMyX670JQHc7wVqRn4_-uJwCCYWn6VAavabS2aBvBCQBhYcMpvcddWgIScFEPnZzYO6VPAD2xqArzo3q_Doog0dmUxj-yNIvTAoAP0kYTRj-XkhEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفاتر تحصیلی شفق تولید انواع دفاتر مشق طلقی فانتزی وکلاسیک ،رحلی،و....
تماس
☎️
09129318455
دریافت لیست قیمت
@Ghamilou73</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/674268" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674266">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/295a597158.mp4?token=jrWbKG-aFQoxvwU-CAiCtCKpwRwGKim4EoXwGE9DQ6vLFy0SDEY_oNy-uhWFGDbP_UY2vZVo5UriCMa8MT2P2__f29wxuXJIHT2qNznqYtly05OHomX1i4hHOE2N24cMNd-l_BK9P1RsAPjGChgYcw7kWRoDd6r6dq8tsArz35c3gKU2fIA4baUmSedrxqmUQFkyUYym9UJrUlwDGIi0YxmYSyCmk37GVY4uOiUP9cdojsj3SyMAO9UHZ2a3_K9BA80Ge_FY5LdHzXniNk5bMp9KPjLKqB_5JSVSiA-J7ykplY1S5n6s_5B8zw207XmRCvkOvGyI3i55XSjHPYcvuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/295a597158.mp4?token=jrWbKG-aFQoxvwU-CAiCtCKpwRwGKim4EoXwGE9DQ6vLFy0SDEY_oNy-uhWFGDbP_UY2vZVo5UriCMa8MT2P2__f29wxuXJIHT2qNznqYtly05OHomX1i4hHOE2N24cMNd-l_BK9P1RsAPjGChgYcw7kWRoDd6r6dq8tsArz35c3gKU2fIA4baUmSedrxqmUQFkyUYym9UJrUlwDGIi0YxmYSyCmk37GVY4uOiUP9cdojsj3SyMAO9UHZ2a3_K9BA80Ge_FY5LdHzXniNk5bMp9KPjLKqB_5JSVSiA-J7ykplY1S5n6s_5B8zw207XmRCvkOvGyI3i55XSjHPYcvuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به مواضع آمریکایی‌ها و تروریست‌های جدایی‌طلب در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/674266" target="_blank">📅 23:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674265">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10fe99630.mp4?token=FovCBpJPgj_jhzuWGMKiV4RD2jSBfsa64GoYXoxeffE55NNPTBfCrqzaXpfqd38oZ7jLNwecI9UvgumXYUvWml4vANXEJU3vBIV9c6nH1brKqUby8f-ZW-muxdc8LfZrtYSrkMPSbwCBLA5caye9-fIaRDhA-ecbCLd2XCyJSkgJVX9ZmQi0sgmozQP2HniJWoSXIjafAnJrC8jmHkKbOOZJB1oDvSq_5hURrVFBS-TmsY3AK1L6Z6xCsbnI6PO0IKnaSXntW7dMJPBJ_TVWZ5pNcqPQcAlyjNSwm9MvZOFggNP0gaIDp8oaynnGTqotuz6YkNhVSNQMBQsEgrLngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10fe99630.mp4?token=FovCBpJPgj_jhzuWGMKiV4RD2jSBfsa64GoYXoxeffE55NNPTBfCrqzaXpfqd38oZ7jLNwecI9UvgumXYUvWml4vANXEJU3vBIV9c6nH1brKqUby8f-ZW-muxdc8LfZrtYSrkMPSbwCBLA5caye9-fIaRDhA-ecbCLd2XCyJSkgJVX9ZmQi0sgmozQP2HniJWoSXIjafAnJrC8jmHkKbOOZJB1oDvSq_5hURrVFBS-TmsY3AK1L6Z6xCsbnI6PO0IKnaSXntW7dMJPBJ_TVWZ5pNcqPQcAlyjNSwm9MvZOFggNP0gaIDp8oaynnGTqotuz6YkNhVSNQMBQsEgrLngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا در امارات و قطر و... هیچ تجمع و تظاهرات و واکنشی درباره جنگ رخ نداد، درحالیکه آنها وسط جنگ بودند؟
🔹
پاسخ این است که این کشورها ملت ندارند. چرا؟
چون آن خاک قصه‌ای ندارد و ساکنانش خاطره‌ آغازین مشترک ندارند
🔹
آن‌ها در آنجا فقط به‌سر می‌برند. به‌همین‌ دلیل مثل مُرده‌ها بی‌واکنش اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/674265" target="_blank">📅 23:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674264">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8D0HbKKsP2dJcRUE5Ywwj_DfBoKkQP-5H6rxE2ZVSQsmcFZn66iGTCGW9Crt-9Mz76A8Q1uwl9s5E3jWJUBi5BU1rhTcwd0WvMcSBst5Whw1SdZWe6pwwkcv7s8EPiv_f7RnZOw0iLuDvRfftFtZalsDhetztRvN_U4NFa_CdataDigC6tonFyZpYG13a6tzSMaGIapuo3oRec0L0siKvDEjMEpDqw_wqrZZYcV4H0tsbufGwh4omLFtUiOgS1PTrXbN3c57lFlrMMnARRX8jJt3Hqoz5YZyTPY_Y-PnAICQ4iJcjRG2Wl5FabxEL-tC2-lYs7X5wLhbvHCsXQ2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهار چهره جهاد؛ از امر به معروف تا ایستادگی در برابر فاسقان
🔹
امام علی(ع) جهاد را مفهومی فراگیر می‌دانند، نه صرفاً جنگ با سلاح. از نگاه ایشان، جهاد بر چهار پایه استوار است: امر به معروف، نهی از منکر، استقامت و صداقت در میدان‌های دشوار، و بیزاری از فاسقان.…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/674264" target="_blank">📅 23:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674262">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
مهرداد خدیر: به رسانه‌های مستقل اعتماد کنید
🔹
مهرداد خدیر با تأکید بر نقش رسانه‌های مستقل گفت روزنامه‌نگاران حرفه‌ای و باسابقه باید امکان روایت واقعیت‌های جامعه را داشته باشند. به جای محدود کردن رسانه‌های داخلی، باید زمینه فعالیت آزادانه‌تر آن‌ها فراهم شود تا اعتماد عمومی تقویت شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/674262" target="_blank">📅 22:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674260">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fedd684453.mp4?token=DN-w99pqfi27kFAPU2ETE6vOC7qM9G1XUxg0AsVjwIf4Xto0jwpFiOV-hGOEEHfnzSPd5C4eFKGtwZ_QZ7IZ7uWM6P4HNhGht_4ssS5dFUGXYXFM2io4zHke9HZ4184WglTIjY_4RS8R7slbuNbmoZGNrdkNZTmnktcqaCRXGcOSpd5UPgZDWMRSts9hJ73TuD81_LfNpG-PcdN47Xw2Z2dOio_aySC8mzp15q2kO5eqnwlTtXADkXtETMN1w3tlK3nRdZq9jQ3bWCSuJXc8bi2CCp8yh4GCuNNshl3AUjEKW8YNSvn-QLPf31dtUhi6i7Fn0VNNfIICApdkXoyLKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fedd684453.mp4?token=DN-w99pqfi27kFAPU2ETE6vOC7qM9G1XUxg0AsVjwIf4Xto0jwpFiOV-hGOEEHfnzSPd5C4eFKGtwZ_QZ7IZ7uWM6P4HNhGht_4ssS5dFUGXYXFM2io4zHke9HZ4184WglTIjY_4RS8R7slbuNbmoZGNrdkNZTmnktcqaCRXGcOSpd5UPgZDWMRSts9hJ73TuD81_LfNpG-PcdN47Xw2Z2dOio_aySC8mzp15q2kO5eqnwlTtXADkXtETMN1w3tlK3nRdZq9jQ3bWCSuJXc8bi2CCp8yh4GCuNNshl3AUjEKW8YNSvn-QLPf31dtUhi6i7Fn0VNNfIICApdkXoyLKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر همه دنیا هم مقابل‌مان بایستند، ما کنار خلیج فارس می‌ایستیم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/674260" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
