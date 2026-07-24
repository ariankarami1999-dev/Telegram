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
<img src="https://cdn4.telesco.pe/file/nrpSN10HLcftzlyOmHlW0YFm-bAsj5Htns0A75yny8FP5OhbCqbNZSrqvorwEMnqnK1ABsOOkBIewo9qdTmfcdvTKEJlQRblYQjfEPI46OlhmAgZuzyP4RwUVAIP-RRucVwmCWcD8Sqn-vNNdEsPFD4tjdek8C0_69446Qo9dB2Nd5KNY2bnGOqVhEumt25eMjLuj2Yv_eZxqwPYYG08s8r4l4GOs2KN8ZWk86rsfYR_23eySVFpfq8rvmYncICNr0EejpG4oRwwJ4L3a_18BoN5pfi1TKomtV_Z2pFh5dYR89vd2ZAqZFvJrQjoOVw2TdPmj0mg8e-TfDQtmfmCVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 05:23:21</div>
<hr>

<div class="tg-post" id="msg-85241">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
🇮🇷
مسؤول أمريكي:
ترامب لا يرى خيارات جيدة سوى مواصلة الضربات على إيران.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/naya_foriraq/85241" target="_blank">📅 05:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85240">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a00b3eb82.mp4?token=mrDei35rippTtapYdE7Ri2uxbCSlAFezqDgNYnLUnWismxjl0pP8c-nu639EI55v-sa6NKGY4jdl-LcjBMcHdrSKv8hdyI7UrRNcMON2qtDNX2oHFJolhG9Y99BwvhRMbBiz5iL9RIwCemOI_RlfGCXj-hATYRfWqUekmOhxf7ZGt7QVxJeFht_2ywIffWZIvYABylfdWXFSkUzOmDJtFRREpn7WkPIygrOWOFT8tz4_GY58BFda1qToUn9HS7i8lxrZxWZs1CXgYKpPJkTzme4L_gKPyNtV3KxrwW9c37Nyma4WIcrbwxiy57IHOYyoZdA0ZWejNfS6YMiRt5X9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a00b3eb82.mp4?token=mrDei35rippTtapYdE7Ri2uxbCSlAFezqDgNYnLUnWismxjl0pP8c-nu639EI55v-sa6NKGY4jdl-LcjBMcHdrSKv8hdyI7UrRNcMON2qtDNX2oHFJolhG9Y99BwvhRMbBiz5iL9RIwCemOI_RlfGCXj-hATYRfWqUekmOhxf7ZGt7QVxJeFht_2ywIffWZIvYABylfdWXFSkUzOmDJtFRREpn7WkPIygrOWOFT8tz4_GY58BFda1qToUn9HS7i8lxrZxWZs1CXgYKpPJkTzme4L_gKPyNtV3KxrwW9c37Nyma4WIcrbwxiy57IHOYyoZdA0ZWejNfS6YMiRt5X9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الامريكي:
أكملت قوات القيادة المركزية الأمريكية (سنتكوم) بنجاح الليلة الثالثة عشرة على التوالي من الضربات الجوية ضد إيران، وذلك في 23 يوليو/تموز، الساعة التاسعة مساءً بتوقيت شرق الولايات المتحدة.</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/naya_foriraq/85240" target="_blank">📅 04:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85239">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات في مدينة خرمشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/naya_foriraq/85239" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85238">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارات في مدينة يزد الإيرانية</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/naya_foriraq/85238" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85237">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات في مدينة فيروزآباد بمحافظة فارس الإيرانية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/85237" target="_blank">📅 04:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85236">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7cdfe133.mp4?token=HKlPzKOm8ofmI0-aF9hxoWxod_1rV33exLSz91Pqn2B38frsPxGhQG9ogCI95DgvWeZ9I6aCXTkg0Bz9UPcq-aXeeNtrm8K424uefBue6s__TGZbJcR45WRrFzGHRNqlMG2jfTwbG7xmonQCLWl_4R6MLckK9qBJPp_eY3M1um3Q_FhIi70nDSlqIhEUZdFXsDD7y6b78cOpR0krvKFFAJSdPR4OWf40LD4tRcrTVsBq0OaFqLhIdLKrqaVkPiCGNZaakDyfCcprOwDermab9cf5dzOpoUGb2zpwCIz3JGgwf3ku4_iZWdnE5sVvMdTTSFxo6eR68R67q9xkXmNrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7cdfe133.mp4?token=HKlPzKOm8ofmI0-aF9hxoWxod_1rV33exLSz91Pqn2B38frsPxGhQG9ogCI95DgvWeZ9I6aCXTkg0Bz9UPcq-aXeeNtrm8K424uefBue6s__TGZbJcR45WRrFzGHRNqlMG2jfTwbG7xmonQCLWl_4R6MLckK9qBJPp_eY3M1um3Q_FhIi70nDSlqIhEUZdFXsDD7y6b78cOpR0krvKFFAJSdPR4OWf40LD4tRcrTVsBq0OaFqLhIdLKrqaVkPiCGNZaakDyfCcprOwDermab9cf5dzOpoUGb2zpwCIz3JGgwf3ku4_iZWdnE5sVvMdTTSFxo6eR68R67q9xkXmNrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية في شرق العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/85236" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85235">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تفعيل الدفاعات الجوية في شرق العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85235" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85234">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0d03f058.mp4?token=gDV2Ki1oHVVA1uCslwpWbydUb0ksqTt9P1JBcvHdrBkaO1u9nzvmvJfmL8IURROo6aya-byyjbYGegBvdxrHPEAYlejPeZljjUhlErKXY8z99DwGyR49oHcO3fJU7taWjeTtdlVeIBuYlGCTwPSMaSC9pb2QcdkH-hArnBXwKj4FvmD-mg8WpdW9_CreNNVU0rcGpjldQGt23EAFmpBdHX49FO5WEFSgFDT84oN1R2hn43hAxg9e3nxy_JpGWX8n8XiIGe0yzJp8n97fAhkI1XruknxYzVExFWfEyvEs_4kMdWwV5oPXw2BTM48cIGBFx8ALCNiopU9rx3R1YIL-wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0d03f058.mp4?token=gDV2Ki1oHVVA1uCslwpWbydUb0ksqTt9P1JBcvHdrBkaO1u9nzvmvJfmL8IURROo6aya-byyjbYGegBvdxrHPEAYlejPeZljjUhlErKXY8z99DwGyR49oHcO3fJU7taWjeTtdlVeIBuYlGCTwPSMaSC9pb2QcdkH-hArnBXwKj4FvmD-mg8WpdW9_CreNNVU0rcGpjldQGt23EAFmpBdHX49FO5WEFSgFDT84oN1R2hn43hAxg9e3nxy_JpGWX8n8XiIGe0yzJp8n97fAhkI1XruknxYzVExFWfEyvEs_4kMdWwV5oPXw2BTM48cIGBFx8ALCNiopU9rx3R1YIL-wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في ميناء جاسك جنوبي إيران</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/85234" target="_blank">📅 03:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85233">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">😆
Bahrain and Kuwait, now</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/85233" target="_blank">📅 03:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85232">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca971c5573.mp4?token=m4eTC1dXMyxQxsmvQ6vU1hmXpz8LTeg2vX04pMgR2jx79fDEr8oWBCdaSf5xOgqgMoUoxTlIqZ-Ou1EnZFAvQVyMFt1Kk35sPFeY-Rv5H6HkqY2jZxU0x7HIEYrQMU5GnsbxRDY6xIQn27MUgSsa4vhrfFGyxx8au3yDv8uw4rdNUQfeYmSYtQdJGy8W9SjrCjGnGVLjrHckYD2Q3IUxqsUtVb9Y7q8qMj9pvVr-Da9_9_WFtr_lzRYUrooueSZ25ok-XE-1Wkj-74dq1YQHCBBha4o5Cz6tEhB1tDV-DDVv5LXDPzdSxKOxhKSO9E9pKiuUMBD22qeR-_0lXnJ7Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca971c5573.mp4?token=m4eTC1dXMyxQxsmvQ6vU1hmXpz8LTeg2vX04pMgR2jx79fDEr8oWBCdaSf5xOgqgMoUoxTlIqZ-Ou1EnZFAvQVyMFt1Kk35sPFeY-Rv5H6HkqY2jZxU0x7HIEYrQMU5GnsbxRDY6xIQn27MUgSsa4vhrfFGyxx8au3yDv8uw4rdNUQfeYmSYtQdJGy8W9SjrCjGnGVLjrHckYD2Q3IUxqsUtVb9Y7q8qMj9pvVr-Da9_9_WFtr_lzRYUrooueSZ25ok-XE-1Wkj-74dq1YQHCBBha4o5Cz6tEhB1tDV-DDVv5LXDPzdSxKOxhKSO9E9pKiuUMBD22qeR-_0lXnJ7Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي يجوب سماء العاصمة بغداد ومدن عراقية أخرى.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/85232" target="_blank">📅 03:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85231">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e36721028.mp4?token=QF2q17oIfAcbvr5U75h19jAyxzebrNwccHwbAg2ta85s6nejRmSR6LA9vvtNvo0bU2b1zNk87yn4NVopegZ7aN8RvDYfgEE0ziM_FxuD6lS-InHfb_T18DNRrt6q3pJPRPo7g8dqqbQuIFub7PzKlKJJ0eYYi29OZYOSjoL0xU0O41cjOsAnk_ObNATeZzEA2QLVUDn2Y2oCnrBek827NN_BoP8JyyJ-o9IRXeREDpH_LZZ-Dblq5QjUHBI09QWEaD2XOjcLA0ry37ZDyBB7h85YGej7deVlWI_uv21zkEkzv4uRDwa7iQr6-MNKOv7utvjOkujEKd5W9K04t9YZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e36721028.mp4?token=QF2q17oIfAcbvr5U75h19jAyxzebrNwccHwbAg2ta85s6nejRmSR6LA9vvtNvo0bU2b1zNk87yn4NVopegZ7aN8RvDYfgEE0ziM_FxuD6lS-InHfb_T18DNRrt6q3pJPRPo7g8dqqbQuIFub7PzKlKJJ0eYYi29OZYOSjoL0xU0O41cjOsAnk_ObNATeZzEA2QLVUDn2Y2oCnrBek827NN_BoP8JyyJ-o9IRXeREDpH_LZZ-Dblq5QjUHBI09QWEaD2XOjcLA0ry37ZDyBB7h85YGej7deVlWI_uv21zkEkzv4uRDwa7iQr6-MNKOv7utvjOkujEKd5W9K04t9YZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي يجوب سماء العاصمة بغداد ومدن عراقية أخرى.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/85231" target="_blank">📅 03:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85230">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات في مدينة خنداب بمحافظة أراك ومدينة بروجرد الإيرانية.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/85230" target="_blank">📅 03:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85229">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات في ميناء كنارك جنوبي إيران</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/85229" target="_blank">📅 03:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85228">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مصدر إيراني: لاوجود لعدوان على مدينة دزفول حتى اللحظة.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85228" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85227">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USCVL5ZYfCezyxExQGExLu46Wl3SSHz0KjgngO77TcS5_0ZFGAsvzUAE2wKzRN9q55LUughYqHcTN5Ean7SMpTxq10nqN3iIh4iNjFzQYJ_8_i7TZR_KX3-RPs68zqyq2cZB7B2jJ8BkEpliX7PFPl-sJ-07InkcM8XfkO3k9rDy6pSGP1BrmT4fZNvYowHuagZYmVIYIVKOB9NuKmozkaj7sRuXTUPD2ZANuGZCg6mXDZi3CyMJvV3Bcq_7t4WiHITKukmB_2lK1pFOpk4-yoLleW6u9q1gcQyniqaZsASzEZpIUQAPY0X_RAtvMY3Za-ZRdTS7hKd6lMcLaX10Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
طائرة تطلق انذار الطوارئ 7700 بعد مغادرتها قاعدة الملك عبد العزيز الجوية في الدمام بالسعودية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85227" target="_blank">📅 03:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85226">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ba4c5527.mp4?token=ev4T1kPcDplzOu2WLrXG5RZi-9L_TA1t_f965lAgdieZTVrLsfMUTy1bcVHuPp0aHj6RfpIbqD7B50MTEYjwRz6ktzkQes4fcx2gKz6jXEm3Cd_z8AdpZXirL-N3BB3hoOIljVf-Tp0YESbRG3jAK_zcTdVv-0RTQ4pRHB-Lle51MzWRITnDqQbstkv8GNNZeUEhuNmYtWcPTp9vMStBLOob8yE3-cqMEMpVAjnqHYGOfNuZe8NWbs6P_nFLsF-vF7OoNiRnjovSay4MaI7HiM1rlaMjQuFqAP_boliKnCsQZhhWroUwWkMGUbRxOP72XYEMgCt852kATzEd7C4s5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ba4c5527.mp4?token=ev4T1kPcDplzOu2WLrXG5RZi-9L_TA1t_f965lAgdieZTVrLsfMUTy1bcVHuPp0aHj6RfpIbqD7B50MTEYjwRz6ktzkQes4fcx2gKz6jXEm3Cd_z8AdpZXirL-N3BB3hoOIljVf-Tp0YESbRG3jAK_zcTdVv-0RTQ4pRHB-Lle51MzWRITnDqQbstkv8GNNZeUEhuNmYtWcPTp9vMStBLOob8yE3-cqMEMpVAjnqHYGOfNuZe8NWbs6P_nFLsF-vF7OoNiRnjovSay4MaI7HiM1rlaMjQuFqAP_boliKnCsQZhhWroUwWkMGUbRxOP72XYEMgCt852kATzEd7C4s5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مناطق سكنية في مدينة الاهواز جنوبي إيران من قبل العدو الأمريكي</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85226" target="_blank">📅 03:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85225">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات في مدينة خرم آباد غربي إيران</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/85225" target="_blank">📅 03:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85224">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات في بندرعباس</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/85224" target="_blank">📅 03:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85223">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
🇮🇷
🇺🇸
نييورك تايمز :
رفضت إيران مقترحًا لوقف إطلاق النار قدّمه ترامب، ونقله إلى طهران رئيس الوزراء العراقي علي الزيدي، وذلك وفقًا لمسؤولين .</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85223" target="_blank">📅 03:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85222">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ed624ca2.mp4?token=sc0QeZyg68C8T20T-1QNSVJzu23byjRNF3S5vEgHZRNJyB0IJpm8fZlqHJlPZ1NBMpE5D1wgc5McqG7pAduQgrSlxLJPXaUCYL9kbE-f6yVPtFjC3u4LapLpCcgzsZzZXwJXLoChsb02SYljC-J24Qynl3Z_dPsxwt3p-eJE7FaRvCBoeq3KnJ8Xscbz7V0dq1jFxAN8ZksTyBc4Hjhi5v9oFL1eEOYfZTm1Ifc39oix24aMyyr4c8r3XUPRyaMmy9bZwkFvBN-LV7nsFfNRH1gl2-u-SIQ6SK-1-pkvQWNw5JTqCR_XleIftoCe2YFBTVpwIWL7LTIEpD60nDhJtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ed624ca2.mp4?token=sc0QeZyg68C8T20T-1QNSVJzu23byjRNF3S5vEgHZRNJyB0IJpm8fZlqHJlPZ1NBMpE5D1wgc5McqG7pAduQgrSlxLJPXaUCYL9kbE-f6yVPtFjC3u4LapLpCcgzsZzZXwJXLoChsb02SYljC-J24Qynl3Z_dPsxwt3p-eJE7FaRvCBoeq3KnJ8Xscbz7V0dq1jFxAN8ZksTyBc4Hjhi5v9oFL1eEOYfZTm1Ifc39oix24aMyyr4c8r3XUPRyaMmy9bZwkFvBN-LV7nsFfNRH1gl2-u-SIQ6SK-1-pkvQWNw5JTqCR_XleIftoCe2YFBTVpwIWL7LTIEpD60nDhJtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من العدوان الأمريكي على الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85222" target="_blank">📅 03:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85220">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbeb67552.mp4?token=O1qhISV_XsoTUpuZWrnpBYV9-gvGPnq72bSzcAPHYBmbFy-KMao6hoZrUn--w2nCs0LnBDEbayCq4iOYaKvrcNBy3XvC1RpPsSeQygfYzxyG-a278bUJT0TiftgyspGvzfxVeBYHxLv4tnJFSOMvg2r8T2ZMb31_8q-yX1if9XridnEauzG-SGSChjBEinPy61b6XHpFdz_RDcCQXDL8RezDmyg-wJH6bBQccx4MMtcRx5dnEi45BksibW4G65A1X9CoywBKTekGuf7mxRLvvfOKAf1UO0ql07tMoPoAuSbiAWNVuA5U6YNXm9PSAjorINWhbr5kz9kX8rYqQLbGfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbeb67552.mp4?token=O1qhISV_XsoTUpuZWrnpBYV9-gvGPnq72bSzcAPHYBmbFy-KMao6hoZrUn--w2nCs0LnBDEbayCq4iOYaKvrcNBy3XvC1RpPsSeQygfYzxyG-a278bUJT0TiftgyspGvzfxVeBYHxLv4tnJFSOMvg2r8T2ZMb31_8q-yX1if9XridnEauzG-SGSChjBEinPy61b6XHpFdz_RDcCQXDL8RezDmyg-wJH6bBQccx4MMtcRx5dnEi45BksibW4G65A1X9CoywBKTekGuf7mxRLvvfOKAf1UO0ql07tMoPoAuSbiAWNVuA5U6YNXm9PSAjorINWhbr5kz9kX8rYqQLbGfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي على مدينة الأهواز جنوب إيران</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/85220" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85219">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e893b05ea7.mp4?token=stUzvR618bhU7Pm9g3t-Yt8mt4Uy5SQTXvhEncRffJQahXUj44OZI-tnUdLFdWgOVDHxcvc2mWADO-_VqMh3px8RGqizpUGhne9Zklad5aEsiuLohQU7hb_hgeBTBUkQiAfAmNjOTDxU8dRBCEOgHbjszFu_04tiCKofQ-pwNEUTLIpCHJ8gw6ItosLTMwfyysgutWIkNeRJFw6TvUG-52yy8_Pc-P2kkwQLlzqKL175WF1NxpfHzPtClFPDCoHDfJovJVSWJNkdnLIGwMefeujS3zHvcRLcFoV8OdjMjgKz4Uz2LBopZImrZVV6EBbbYMSwP3eMyYOdWETy2eqn7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e893b05ea7.mp4?token=stUzvR618bhU7Pm9g3t-Yt8mt4Uy5SQTXvhEncRffJQahXUj44OZI-tnUdLFdWgOVDHxcvc2mWADO-_VqMh3px8RGqizpUGhne9Zklad5aEsiuLohQU7hb_hgeBTBUkQiAfAmNjOTDxU8dRBCEOgHbjszFu_04tiCKofQ-pwNEUTLIpCHJ8gw6ItosLTMwfyysgutWIkNeRJFw6TvUG-52yy8_Pc-P2kkwQLlzqKL175WF1NxpfHzPtClFPDCoHDfJovJVSWJNkdnLIGwMefeujS3zHvcRLcFoV8OdjMjgKz4Uz2LBopZImrZVV6EBbbYMSwP3eMyYOdWETy2eqn7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في بندرعباس</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85219" target="_blank">📅 02:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85218">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات في جزيرة قشم جنوبي إيران</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85218" target="_blank">📅 02:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b99c419e82.mp4?token=NXfQ9VHwV-3EExULqtLDzWIUEW7wqZM7qApC4KarqxwKkeu9oNxgbEHICjlvzf2hb4RzJheDQ1UsWcK0pPg42eyGXacFxjTXV8ac6f7zCDpXf7rEde4eT-iALLC8doYG0jvfJHK_VNXt_u1CFXAXfuJk5QD76SR2PdMu3C4FUKAPZWnfc9-0V4XGX7428XN8hGxZYTlDh31RfmIb4I3Mb8hcV66gvVPh4LeZmSwlLnjA82GrFkxWYMvHQMYVTzSbrcximiZpgPhtVI2LvKPDsx097-Ld6RjbYTmDa-1ptdgzlWq7vxO_GM2-kbwG-lsZ8cvCnI8cDGf1DK-AHHqh-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b99c419e82.mp4?token=NXfQ9VHwV-3EExULqtLDzWIUEW7wqZM7qApC4KarqxwKkeu9oNxgbEHICjlvzf2hb4RzJheDQ1UsWcK0pPg42eyGXacFxjTXV8ac6f7zCDpXf7rEde4eT-iALLC8doYG0jvfJHK_VNXt_u1CFXAXfuJk5QD76SR2PdMu3C4FUKAPZWnfc9-0V4XGX7428XN8hGxZYTlDh31RfmIb4I3Mb8hcV66gvVPh4LeZmSwlLnjA82GrFkxWYMvHQMYVTzSbrcximiZpgPhtVI2LvKPDsx097-Ld6RjbYTmDa-1ptdgzlWq7vxO_GM2-kbwG-lsZ8cvCnI8cDGf1DK-AHHqh-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تكبيرات أطفال مدينة الأهواز وسط العدوان الأمريكي الغاشم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85217" target="_blank">📅 02:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85216">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=TyH19MPFGFFDQrZQD26ERbiqtu19W8LcYyxvWDxFPbLEaIjCkV0XqLzyPMwA0JgsCDP-RcpLqadTWC84hJF0B-xmxVf5SPwvGcbQXc8jx-Ap6_EzaSsON7upwj-JtvBGuZHHSo8dsc7Zf1KtdK1UyeaSt8xw8GZhxFPrzdOen17Fblo1jkeMO9Nn1qkOYSRurd-DofTMvhb3fNigUZCwbnbdimjRzjz2luxkp5oRmZDtbVRxedXPhtTikXljsGPF9Rn1V-0T1O0zKfP_2nofNlJn-84D3syofq6d_UXIkyPNwdcV-s3qeubE8UTDahJo_IGJJAvsL1dNGqjwBP4n1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=TyH19MPFGFFDQrZQD26ERbiqtu19W8LcYyxvWDxFPbLEaIjCkV0XqLzyPMwA0JgsCDP-RcpLqadTWC84hJF0B-xmxVf5SPwvGcbQXc8jx-Ap6_EzaSsON7upwj-JtvBGuZHHSo8dsc7Zf1KtdK1UyeaSt8xw8GZhxFPrzdOen17Fblo1jkeMO9Nn1qkOYSRurd-DofTMvhb3fNigUZCwbnbdimjRzjz2luxkp5oRmZDtbVRxedXPhtTikXljsGPF9Rn1V-0T1O0zKfP_2nofNlJn-84D3syofq6d_UXIkyPNwdcV-s3qeubE8UTDahJo_IGJJAvsL1dNGqjwBP4n1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری دیگر از تجاوز آمریکا به اطراف اهواز در استان خوزستان ایران.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85216" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85215">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=pc3HAe9XYdRLzXWrVdQBBf1kZ6ebdCeA8RXOH_oRRSXTvvbEUaSWyyeRQN-am-ocxx6T_6L1wEqv3mKhgo2uDe1RvFpsljlfZqUuyDqLq4EG8amYVfBu6J5nEvC9a3K3uOKRCaS5v5YKKzGo9JZGhun97EXKZyvg_BONNSIYuZUtVnYZxnWFeBxh3W0oTHjWuMgBmhgWN-wd-TwAmW1HiyVjJqWfdfHClCO6GLp1A4_H20eFCFkejaLrPHaHPMF-6bBoquneLyCYAuOOGHUlJV2gMVzCDHwp8d4qc8vOZ6_DY_oK9EXv6OuOLqLTxsZBvf31cYcimcGIVO8N_AUnAbkbhxOoFN5T-y6tIb38VTAPCTBmJu5WSMkVKyhlFq6cJP0vse3qlZn-3ORIrxhOHm87wVXzLTk8jcv-q20HTmJnPQbOrUUfm8echpqFJYwKyhDKSg2A8NZjcRCVj29j_tKMuDr_H6ml2md2nTVaTY4Ge3z35sQJrOEiJaEMrCjSe5BDADpqp2RaFFZVpU04b78y9tsa5GCYDZpHu7FWAr-wZkj-9mavLiYzTOEkZprVEiLUO81nqw6cXu5luMWdVDZIPDqvxXhlxphFwWJyGm3Cgo5kKf_HQ1R4QpikTHLm4iLbLHOsDxpj4qKV_k9pWKCHDOWqJwMBeI1HcGYFj5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=pc3HAe9XYdRLzXWrVdQBBf1kZ6ebdCeA8RXOH_oRRSXTvvbEUaSWyyeRQN-am-ocxx6T_6L1wEqv3mKhgo2uDe1RvFpsljlfZqUuyDqLq4EG8amYVfBu6J5nEvC9a3K3uOKRCaS5v5YKKzGo9JZGhun97EXKZyvg_BONNSIYuZUtVnYZxnWFeBxh3W0oTHjWuMgBmhgWN-wd-TwAmW1HiyVjJqWfdfHClCO6GLp1A4_H20eFCFkejaLrPHaHPMF-6bBoquneLyCYAuOOGHUlJV2gMVzCDHwp8d4qc8vOZ6_DY_oK9EXv6OuOLqLTxsZBvf31cYcimcGIVO8N_AUnAbkbhxOoFN5T-y6tIb38VTAPCTBmJu5WSMkVKyhlFq6cJP0vse3qlZn-3ORIrxhOHm87wVXzLTk8jcv-q20HTmJnPQbOrUUfm8echpqFJYwKyhDKSg2A8NZjcRCVj29j_tKMuDr_H6ml2md2nTVaTY4Ge3z35sQJrOEiJaEMrCjSe5BDADpqp2RaFFZVpU04b78y9tsa5GCYDZpHu7FWAr-wZkj-9mavLiYzTOEkZprVEiLUO81nqw6cXu5luMWdVDZIPDqvxXhlxphFwWJyGm3Cgo5kKf_HQ1R4QpikTHLm4iLbLHOsDxpj4qKV_k9pWKCHDOWqJwMBeI1HcGYFj5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي الغاشم على مدينة الأهواز الإيرانية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85215" target="_blank">📅 02:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85214">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جسم غريب يسقط في سماء قشم بعد إطلاق النار عليه الان</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85214" target="_blank">📅 02:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85213">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6297da3bb.mp4?token=FEGbEZyg1exgRUwvKgZcH3tunlq6jdMYJqWBkNPBgAgR-90cOku9T59hVHcR3jK6F_3tGA4oUzvIB6GPRgzaqzA7mugTDORAlGrqk_0qw66q4pclNbLNsQcRWFRk94ZWBX-NIlWciTTyjRaLrAsK2lEoacIZZgul71hpl8J_Tl1floYpwbJ6dFGePy4Po74i7tP25kjUEFstRiNu2yXh1ot4c-o2Mg-sx4oZJ-oChP_85GUMXZWvxYZjlfkf-DzupcqsxnfPhpRY7pJSkA8C2O4IMr4Jlh6cBSzANoLe-J66LBTm8e06-GhLlzP3wAP7SVRFjNT7hBfg01JgWKJzDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6297da3bb.mp4?token=FEGbEZyg1exgRUwvKgZcH3tunlq6jdMYJqWBkNPBgAgR-90cOku9T59hVHcR3jK6F_3tGA4oUzvIB6GPRgzaqzA7mugTDORAlGrqk_0qw66q4pclNbLNsQcRWFRk94ZWBX-NIlWciTTyjRaLrAsK2lEoacIZZgul71hpl8J_Tl1floYpwbJ6dFGePy4Po74i7tP25kjUEFstRiNu2yXh1ot4c-o2Mg-sx4oZJ-oChP_85GUMXZWvxYZjlfkf-DzupcqsxnfPhpRY7pJSkA8C2O4IMr4Jlh6cBSzANoLe-J66LBTm8e06-GhLlzP3wAP7SVRFjNT7hBfg01JgWKJzDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
Bahrain and Kuwait, now</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85213" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85212">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=fhNOlA20WaBytcTmz4HYBSQxUB0irfXDUalLBFOI1_Y-6HB9N8zbVda4XvgG6y_ENEuSkdT5B5IqBqtkqlhwvimEQS4KpG3ATCzrrk8CQPwseq4V1jxOsfgene8fNgQP-ZSJHoaSXzXgPPGSZYeO2ovgC9uELBRgyAtNEN_bmBKkxcAH-Z_t2UJtjVzdTnJA4PkJ7n8oWTP3KAri_MfMPtzGyt5rtttC0jBb4qb9e1JFMImwvDpqODVDdYtr9BzmFCAwQJoCdnnY7B5P3K9fZj09Now5i70FgSUGTvujB2mCysUYVEPbn08UnZaWEjj2phrCaotWRviTsP8tVc9MgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=fhNOlA20WaBytcTmz4HYBSQxUB0irfXDUalLBFOI1_Y-6HB9N8zbVda4XvgG6y_ENEuSkdT5B5IqBqtkqlhwvimEQS4KpG3ATCzrrk8CQPwseq4V1jxOsfgene8fNgQP-ZSJHoaSXzXgPPGSZYeO2ovgC9uELBRgyAtNEN_bmBKkxcAH-Z_t2UJtjVzdTnJA4PkJ7n8oWTP3KAri_MfMPtzGyt5rtttC0jBb4qb9e1JFMImwvDpqODVDdYtr9BzmFCAwQJoCdnnY7B5P3K9fZj09Now5i70FgSUGTvujB2mCysUYVEPbn08UnZaWEjj2phrCaotWRviTsP8tVc9MgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبيعة الانفجارات توكد استخدام طائرات قاصفة ; على الأرجح B1</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85212" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85211">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بيان للجيش الامريكي:
بدأت القوات الأمريكية ليلة أخرى من الضربات ضد أهداف عسكرية إيرانية في الساعة 6:45 مساءً بتوقيت شرق الولايات المتحدة، وهي الليلة الثالثة عشرة على التوالي التي تهدف إلى محاسبة إيران والحد من تهديدات الحرس الثوري الإيراني للشحن التجاري.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85211" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85210">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=PxsZOhVUfDxBasLQH5L4ZY977wS4KS2IAzle0oChNWrbIsCDIe9P2MeAznyAetItm-gBTD58V7Tlt9bFih_-i3uOyHJR6U2nmuCJFoUVXw-PYdl1qv-dLx_ULpWlaD3OYHvgycFLL9KDylEn3kxKfBAHDEzL2HrHzvQ3xcdEe3uI2vyp6LK3SvIL3eBfBq42L6rg8FBTtHQMNK7O0jABZJeIBw2Qhb05ayWwMxtUtyXYouO8x6Yzzhhm52usntd3UCtS-NE20Az8bHvvjURr2siAkkVVISKMYA6ZfaIywVdXlBzt8UgarjarJQ6xn030Bet1qhb879ieYHx0_eVLBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=PxsZOhVUfDxBasLQH5L4ZY977wS4KS2IAzle0oChNWrbIsCDIe9P2MeAznyAetItm-gBTD58V7Tlt9bFih_-i3uOyHJR6U2nmuCJFoUVXw-PYdl1qv-dLx_ULpWlaD3OYHvgycFLL9KDylEn3kxKfBAHDEzL2HrHzvQ3xcdEe3uI2vyp6LK3SvIL3eBfBq42L6rg8FBTtHQMNK7O0jABZJeIBw2Qhb05ayWwMxtUtyXYouO8x6Yzzhhm52usntd3UCtS-NE20Az8bHvvjURr2siAkkVVISKMYA6ZfaIywVdXlBzt8UgarjarJQ6xn030Bet1qhb879ieYHx0_eVLBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85210" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85209">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارات في بندرعباس</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85209" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85208">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85208" target="_blank">📅 02:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85207">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4fc23b50a.mp4?token=tB8tTLmiamgqkgdTVfnG8H3QyytInlXAX4DJ0bw38TnEjl9QTMN817THxiNXTswzkOeRL8DoRXflcRoiyBM33eLldSOQ9J-Dkp7qphEmomvhKC3PzC_sfToIPfuy2Nf0lUbqAjcG6NPf9RmOab_35tXFlBu9THX-8LC8rO3itTXpHt7X_kGcQXzuGBxjDMiy254vogiAmmrc3PSbt6zAj6oXZWd2qF88y69IG_jG_K5A-hZvNDgDppingve0_C8BaX27SNN4wNtnLONxIyU3iNmkkUjqNIoBvMSIWhT9iRmHbjJbWNfZ3bM4mZxQhttSztJrUdZoDfLuHb6-m-PTlm91czWZy-y-3B5AntpxuVfOccPFAAhIdNgw-cNaLafUbOd2Futumyt_45xjqoXsrgHYFq7DbXJIgo39qXtkIMRft1jf68ZnFK5VdHIqYtbIyPE0HjpNSTRHkT_blvxbRxXcuocsq7NSJMxaT6RWMjeKtojoFBpWrbqOMJCWGjfLkpxxh5xqd67GNo6phTA1PYe8B9zVj3dhzntfU7AVDdc4TVWwzHTt6C97DMxMG_XkyXtJ-NFsap6eFVw6jHziT65INi6zrPTYaFIXThNBX52l-p9V_aixYbxOJVuyqsKzZGFMLYRCabl4C3S_b5GKscNa7bKgTn7iuuAOBkUR1Is" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4fc23b50a.mp4?token=tB8tTLmiamgqkgdTVfnG8H3QyytInlXAX4DJ0bw38TnEjl9QTMN817THxiNXTswzkOeRL8DoRXflcRoiyBM33eLldSOQ9J-Dkp7qphEmomvhKC3PzC_sfToIPfuy2Nf0lUbqAjcG6NPf9RmOab_35tXFlBu9THX-8LC8rO3itTXpHt7X_kGcQXzuGBxjDMiy254vogiAmmrc3PSbt6zAj6oXZWd2qF88y69IG_jG_K5A-hZvNDgDppingve0_C8BaX27SNN4wNtnLONxIyU3iNmkkUjqNIoBvMSIWhT9iRmHbjJbWNfZ3bM4mZxQhttSztJrUdZoDfLuHb6-m-PTlm91czWZy-y-3B5AntpxuVfOccPFAAhIdNgw-cNaLafUbOd2Futumyt_45xjqoXsrgHYFq7DbXJIgo39qXtkIMRft1jf68ZnFK5VdHIqYtbIyPE0HjpNSTRHkT_blvxbRxXcuocsq7NSJMxaT6RWMjeKtojoFBpWrbqOMJCWGjfLkpxxh5xqd67GNo6phTA1PYe8B9zVj3dhzntfU7AVDdc4TVWwzHTt6C97DMxMG_XkyXtJ-NFsap6eFVw6jHziT65INi6zrPTYaFIXThNBX52l-p9V_aixYbxOJVuyqsKzZGFMLYRCabl4C3S_b5GKscNa7bKgTn7iuuAOBkUR1Is" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85207" target="_blank">📅 02:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85206">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7123743603.mp4?token=nvM1SLtHTlwRL1FzlJYiaAKYLIuweA_QpEXOzSfr5Km44IKhicaelEcdBO5ZmlHWzQ1O6p3UugXm7yYdpVfEaUiDdEwuWCBF98HTj6-7j0MC77lVDtMOOwNMIGxFLE1Pb9iKIHz_d5r6VtMqRrOAvoVll_pbWBOJ7E6211tZ9VjsJPdedTTzwO6gD_9y8e5QgX76giWXZOuCW9jmfp04eYk0DWgZEZ1XIIYkJh0PxpxYj3SVzJKvy0wFk257C1ePdyC6aHx9FH5MFXK2EFcyXsiqBKn2vftahfa6HIZijvevnxr2DPNzSxwDswqQlLH646lMIpUksB8nvs7zAMdKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7123743603.mp4?token=nvM1SLtHTlwRL1FzlJYiaAKYLIuweA_QpEXOzSfr5Km44IKhicaelEcdBO5ZmlHWzQ1O6p3UugXm7yYdpVfEaUiDdEwuWCBF98HTj6-7j0MC77lVDtMOOwNMIGxFLE1Pb9iKIHz_d5r6VtMqRrOAvoVll_pbWBOJ7E6211tZ9VjsJPdedTTzwO6gD_9y8e5QgX76giWXZOuCW9jmfp04eYk0DWgZEZ1XIIYkJh0PxpxYj3SVzJKvy0wFk257C1ePdyC6aHx9FH5MFXK2EFcyXsiqBKn2vftahfa6HIZijvevnxr2DPNzSxwDswqQlLH646lMIpUksB8nvs7zAMdKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي أمريكي في سماء محافظة كركوك شمالي العراق</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85206" target="_blank">📅 02:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85205">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
🇺🇸
55 شهيدًا و 629 جريحًا في هجمات العدو الأمريكي على إيران حتى الأن.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85205" target="_blank">📅 02:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85204">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇷🇺
🇺🇸
اكسوس
: مجلس الشيوخ يستعد للتصويت على العقوبات المفروضة على روسيا الأسبوع المقبل</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85204" target="_blank">📅 02:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85203">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جسم غريب يسقط في سماء قشم بعد إطلاق النار عليه الان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/85203" target="_blank">📅 02:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85202">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/85202" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85201">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جسم غريب يسقط في سماء قشم بعد إطلاق النار عليه الان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/85201" target="_blank">📅 01:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85200">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18fec637f4.mp4?token=oR-ryJVmPCPg2zutUAcOBkzFDJ2bwPhJuJj2G7z_WIYglvzRya2GZA7JyeSkA3DA8_qVXGPSDs0cOXrJDbzSUl73vHT0deveMVTAK_KMXXcrgPJz-v50ib1b_LUyNQ0X5PHnMor8BawdtqWezbk8qZ4_5QweQXuJtAlOSaDyyy4Qxqozrcwru_0KXTEGzXP40D-DIe4TTMimnQ2QC1eoKG8M4uYNLGQfmyCmLlVHL5BAv91bK5-9ckbTbofdZArNvntdPGRKy4q9jZLIkRUaX2wkEOYroslOVzEAn0oP2vJ5-k4geQ8WlDaO7_rgL7__As4VIRLlGJokO48l2oUuwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18fec637f4.mp4?token=oR-ryJVmPCPg2zutUAcOBkzFDJ2bwPhJuJj2G7z_WIYglvzRya2GZA7JyeSkA3DA8_qVXGPSDs0cOXrJDbzSUl73vHT0deveMVTAK_KMXXcrgPJz-v50ib1b_LUyNQ0X5PHnMor8BawdtqWezbk8qZ4_5QweQXuJtAlOSaDyyy4Qxqozrcwru_0KXTEGzXP40D-DIe4TTMimnQ2QC1eoKG8M4uYNLGQfmyCmLlVHL5BAv91bK5-9ckbTbofdZArNvntdPGRKy4q9jZLIkRUaX2wkEOYroslOVzEAn0oP2vJ5-k4geQ8WlDaO7_rgL7__As4VIRLlGJokO48l2oUuwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أنباء اولية عن إسقاط طائرة في سماء جزيرة قشم</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/85200" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85199">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">أنباء اولية عن إسقاط طائرة في سماء جزيرة قشم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85199" target="_blank">📅 01:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85198">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/85198" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85197">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7726b6f71.mp4?token=mVL9utd1gIl8QaOhpcXvuicPpaeEsGBgwyLuWnpuow0R67tShfJW3U3tv4K-66iNIopTlYyu1sx8DZzk666OxzP-CoDztw2Zya1J299UkjgkzrlkLCOmsU5uPWTOUVEnGJDx8ELwkcVlTuBxnniCG8WYUg95GtBVNtK5bSg6u3dtbQmnTmjkMUUxLXjNIUnjfzk34ZoY23cMyCy_gYfH0l6NhzmHqPEctd1SyzzOzWg_Z-gJIdgo96yDdy8QvwQiZ2rjD7R5yujtRtF_8uda3hXOMS6eKDYJJAwP79f0hTgwWwiRimJ4obv7rRyvCDQEb4SsmvS83TLa4vZf9kdxOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7726b6f71.mp4?token=mVL9utd1gIl8QaOhpcXvuicPpaeEsGBgwyLuWnpuow0R67tShfJW3U3tv4K-66iNIopTlYyu1sx8DZzk666OxzP-CoDztw2Zya1J299UkjgkzrlkLCOmsU5uPWTOUVEnGJDx8ELwkcVlTuBxnniCG8WYUg95GtBVNtK5bSg6u3dtbQmnTmjkMUUxLXjNIUnjfzk34ZoY23cMyCy_gYfH0l6NhzmHqPEctd1SyzzOzWg_Z-gJIdgo96yDdy8QvwQiZ2rjD7R5yujtRtF_8uda3hXOMS6eKDYJJAwP79f0hTgwWwiRimJ4obv7rRyvCDQEb4SsmvS83TLa4vZf9kdxOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: "يرجى اعتبار هذه التصريحات، حتى إشعار آخر، على أنها تعبر عن أن أي أضرار تلحق بالسفن أو البضائع أو أي شيء ذي صلة، سيتم تعويضها من الأموال الإيرانية التي تملكها الولايات المتحدة وتسيطر عليها. قد تكون هذه الأضرار كبيرة جدًا، ولكن على الرغم من ذلك، فإن…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/naya_foriraq/85197" target="_blank">📅 01:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85196">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏
‏
نيويورك تايمز:
"على مدى ثلاثة عقود تقريبًا، كانت الأردن قاعدة مهمة للعمليات العسكرية الأمريكية في جميع أنحاء الشرق الأوسط." ‏"والآن، الأردن يدفع الثمن...".</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85196" target="_blank">📅 01:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85195">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snajLzPN_GuJq2RlmTnHzL_ICFI2hXaCD3l7pA3FfB5vEYuheevt4O3wb_N-rhPLFJqyy26zkEb8vxzlreyG4_LdBLJV8w6OEVByKGTqvu2P4zB63RaGLY6Le-TcWlL8X0RxK46V-oTc8U0G9pMswvAZMCfw1h4ybX3rniuzai4FqCjK6xQ2w1ecudQJ4JqNvE1mVtEbpmr-SoxX5UkPBP4Su1ZQjoTviriBEFl_HQFJ_qJIn7z3SUHwwItCGWrzwZg3mTjFEFLwiw_xT9HErkTWSbfNkQ-btJ6FS4zOjjO5yG3SqfQIBWVl3pZ4d-47I8BGSS918kgMoGTWyx4DZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
"يرجى اعتبار هذه التصريحات، حتى إشعار آخر، على أنها تعبر عن أن أي أضرار تلحق بالسفن أو البضائع أو أي شيء ذي صلة، سيتم تعويضها من الأموال الإيرانية التي تملكها الولايات المتحدة وتسيطر عليها. قد تكون هذه الأضرار كبيرة جدًا، ولكن على الرغم من ذلك، فإن هذا هو الإجراء العادل والمنصف. شكرًا لاهتمامكم بهذا الأمر."</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/85195" target="_blank">📅 01:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85194">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
سي بي إس:
‏
إن الوتيرة السريعة التي تنفق بها الولايات المتحدة بعضًا من أحدث طائراتها الاعتراضية للدفاع الجوي وأسلحتها الموجهة بدقة في الشرق الأوسط تُشكل نقطة توتر كبيرة داخل إدارة ترامب.
‏قال مسؤولون أمريكيون إن الولايات المتحدة لا تستطيع الاستمرار في استخدام الذخائر الدقيقة بنفس الوتيرة التي استخدمتها في بداية حملتها ضد إيران.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85194" target="_blank">📅 01:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85192">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
وول ستريت جورنال:
صور أقمار صناعية تُظهر أن إيران تعيد بناء مواقعها العسكرية بوتيرة سريعة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/85192" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85191">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUE2KRAso_-00IUu2rg2zomBe8HLPeg8hcSPsU77E7usZzHOjmPfHronu6w3cbKtkql0q6BKW5EIKJ73o3EjrxJPNUPQvfS_dldysP5Az_6wPi3kX5sUdIO5354V2FMUuY2l5x4b3tAyYJJQPd2nj-V_kSE_8AIdLykNaSabCpFyekOXVk6NaBPsmpvPB4W9P5RnEl9roKeO_0XhYWx8XWmldCxu-bPtAQX4NkmmLyG6YcYGvUOTxPFszrNYD0dJnwG5xgjxV0nUhbLxH9sj_IA1sGKMOBmnzZjndgurf5hi4RBHfJW1sssk0tfS2T3p80bzST8k_3h2sIVcg_xYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
مواطنة كويتية تطالب بالغاء فقرة الأغاني في التلفزيون الكويتي والتوجه لنشر الدعاء بسبب الأوضاع الأمنية في البلاد نتيجة القصف الإيراني
🔻
اتركوا لها تعليق جميل
https://x.com/sarahalnomas/status/2080376158214877597?s=46</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/85191" target="_blank">📅 01:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85190">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله أكبر
🇮🇷
🇺🇸
الدفاعات الجوية الإيرانية تتمكن من إعتراض وإسقاط صاروخ أمريكي في سماء مدينة كرمان جنوبي البلاد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/85190" target="_blank">📅 00:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85189">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac0f2cc539.mp4?token=LjZFqQRHKgtazvTLxfR9WXBDhtifaibwQXcavB4GilvY6QAqtTlxihw6oUjozFckfVgK-g381FYUBs4SsqmbztTYGIVEKZkHVf0j9JoC_3R2kVe2Gwlmjxu5GEjNrYnZhbOWt6zADoszHlhvIkpaaflSSA_RjTVPZmraoXebdspgD5euT4G7wtSQgI3Qm_vKO784lVtffbjx8P6uh_KIvBWWpsWgwo950iqnj2dwJiXbR8TPC0JNySTNTBpumZiLJhyA-tXsrYY_gEoz6-maDvwpeuytkHmBhrPzh7VWMs-nYQ2oiK7ivE_CVLg2A3XoR5UUtxnZa8LkiABMYzW_7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac0f2cc539.mp4?token=LjZFqQRHKgtazvTLxfR9WXBDhtifaibwQXcavB4GilvY6QAqtTlxihw6oUjozFckfVgK-g381FYUBs4SsqmbztTYGIVEKZkHVf0j9JoC_3R2kVe2Gwlmjxu5GEjNrYnZhbOWt6zADoszHlhvIkpaaflSSA_RjTVPZmraoXebdspgD5euT4G7wtSQgI3Qm_vKO784lVtffbjx8P6uh_KIvBWWpsWgwo950iqnj2dwJiXbR8TPC0JNySTNTBpumZiLJhyA-tXsrYY_gEoz6-maDvwpeuytkHmBhrPzh7VWMs-nYQ2oiK7ivE_CVLg2A3XoR5UUtxnZa8LkiABMYzW_7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أبناء البحرين الغيارى يستمرون في مسيراتهم الداعمة لمحور المقاومة والرافضة لظلم عصابات آل خليفة المتصهينة.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/85189" target="_blank">📅 00:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85188">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8547a511bc.mp4?token=dDcFL9__rjAKDYTAkrbS2dzmt-puCQ-UPwL8vjwVjkfIOpd4zvpPmoAWHKOzZ0TLCKEKh5XKM-p7llujJuS87mXUvmrMyyYWMIyFiR6Qw4RYxnyYmIa7wGfTPo_ofCF4Qy8NePJ2qcgirITPyRqZEt0LPUnoq9H7-RnHQG5R_mHIal3i5BJ2g73NcXtMd6uiJCBBiGHX-6vaR0dLdi-a0NhAYbIHAbBusCtQQMiQXCExI49bWOJPxOyLdj90VxvjbRTZL6klgR34lOFLvwCOrod0cs9xs_GdrwKlLyOj0cHx5UhI8lddNhs5ZKLx1bHP0tTwLz1S-91z1zsMlekTZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8547a511bc.mp4?token=dDcFL9__rjAKDYTAkrbS2dzmt-puCQ-UPwL8vjwVjkfIOpd4zvpPmoAWHKOzZ0TLCKEKh5XKM-p7llujJuS87mXUvmrMyyYWMIyFiR6Qw4RYxnyYmIa7wGfTPo_ofCF4Qy8NePJ2qcgirITPyRqZEt0LPUnoq9H7-RnHQG5R_mHIal3i5BJ2g73NcXtMd6uiJCBBiGHX-6vaR0dLdi-a0NhAYbIHAbBusCtQQMiQXCExI49bWOJPxOyLdj90VxvjbRTZL6klgR34lOFLvwCOrod0cs9xs_GdrwKlLyOj0cHx5UhI8lddNhs5ZKLx1bHP0tTwLz1S-91z1zsMlekTZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
توثيق من جانب العراقي يضهر محاولات الكويت بالتصدي للصواريخ الايرانية عن طريق اطلاق عشرات صواريخ الباتريوت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/85188" target="_blank">📅 00:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85186">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
عدوان اميركي يستهدف جزيرة قشم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/85186" target="_blank">📅 00:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85185">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
‏يوم الأربعاء تمكن هجوم إيراني آخر من اختراق الدفاعات الجوية الأمريكية وضرب مستودع أسلحة بالقرب من القاعدة نفسها التي قُتل فيها ثلاثة جنود أمريكيين في الأردن، مما تسبب في تشكل "سحابة فطرية بعد أن أدى الهجوم إلى انفجار.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/85185" target="_blank">📅 23:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85184">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
تم نقل ما يقرب من عشرة جنود أمريكيين أصيبوا إصابات خطيرة في الهجمات الإيرانية الأخيرة إلى مستشفى عسكري أمريكي في ألمانيا.
هم من بين حوالي 100 جندي أمريكي أصيبوا منذ أوائل شهر يوليو، على الرغم من أن وزارة الدفاع الأمريكية ذكرت أن معظمهم عانوا من إصابات خفيفة في الرأس وقد عادوا بالفعل إلى العمل.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/85184" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85183">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1XFOHBkppMyyYzBoYaMunOkpNO2l7L5qNnGBySZ7S4klKdA-kUkOj7LfLpfkuErV2oJWGNUqNI6BNlP5hcj2UYBCmFKcykEfS8ejJRLS4EaDByBmTvO1lNBUDE8c7gXRnQKs_npgAk6083qlSCGsypsNFVsqvZoUdQH_yEdMsDI9nOwYDznA2AnANF0PSvct1E-eozA52JlKcQSTEpIGO3Yq0mPUXxuG3yFoL1-XcJ2xzGZaqiQMOyz76qUVvd3DrO25qc9JaZwc2NHjGqwx5iP5uWQkbMvGyh2UsIb-4PYwK4k_bPk7mw6PimcNEYQOhE7a77GF63c_eklru2ZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توثيق من جانب العراقي يضهر محاولات الكويت بالتصدي للصواريخ الايرانية عن طريق اطلاق عشرات صواريخ الباتريوت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/85183" target="_blank">📅 23:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85182">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الصواريخ الايرانية تنهل ‏على معسكر بيورينغ الاميركي في الكويت</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/85182" target="_blank">📅 23:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85181">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انتشار قوات الخاصة مع قوة مدرعة في مداخل مدينة الصدر شرقي العاصمة بغداد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/85181" target="_blank">📅 23:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85179">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a99a0a78.mp4?token=qfuu3tYrzec6lU55XszEpWxXiANv__6iVpyDubZZSnyMClfJ5ad8WUwnXKqpUui6Cje-2n_dx16QPskjKTqhCIkXqUXsUT8pBS-05YR-eUU-I5ozFMFLgRXc7u5a0UWhb4sYwPMlIsbr3kQOD79JlADL7U2WSqEOHXBHEqPm9hRGhdLqisEAKGxJFwLrOLS7ESxaVLPu1SeEX28UNeB93yGR5c5JFbahtJwH5vClJIdxJKQbh2taoHeWfCvUzyw-5cQ1rwl_AW69hN37pSNdWHn-B2FqnpkDa__H-6_BcCxKRx8KwRV5saXYiXpc3ke8p4AGBkuOjlbxPn5t_Pe84w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a99a0a78.mp4?token=qfuu3tYrzec6lU55XszEpWxXiANv__6iVpyDubZZSnyMClfJ5ad8WUwnXKqpUui6Cje-2n_dx16QPskjKTqhCIkXqUXsUT8pBS-05YR-eUU-I5ozFMFLgRXc7u5a0UWhb4sYwPMlIsbr3kQOD79JlADL7U2WSqEOHXBHEqPm9hRGhdLqisEAKGxJFwLrOLS7ESxaVLPu1SeEX28UNeB93yGR5c5JFbahtJwH5vClJIdxJKQbh2taoHeWfCvUzyw-5cQ1rwl_AW69hN37pSNdWHn-B2FqnpkDa__H-6_BcCxKRx8KwRV5saXYiXpc3ke8p4AGBkuOjlbxPn5t_Pe84w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دوي صفارات الانذار داخل الكويت</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/85179" target="_blank">📅 23:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85178">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae28f96254.mp4?token=acX5M-_OrqLkExpwSSW4fjjeO9STF4-1CdzMsvf-Cna60teyeLFXYJTTbhb1fq1kC9K2e9-Nqpf0YacUJJckBMWnH3MPcM5cMNmP6jazbQa3j3qxIp5zycKpNgzO4XEB2fds33Z6wOW4fCIJ-IpwQrI_nSx2xPzRtgWBgJyJD5CojfHtpRIhwqPkCEjI439ieR75gguepBcMY4hBjAZdAaDh2zkQ2Qn3tUsqJf6TKZ_cRR7Cy9R5hCJOt9HojuNzfz5vM-AC1F-uFElKCpMPnkRpef1YrY1nzFcfmBOToOiQdRdg7Q9AElrYUl0aHF3GM46HkVJM0q0H0hxbPTU_GI0wjuSuWrE9sA_NR2S1vk2Cc1Vfott1wrAecD4nHBtuZKchI5DXWS9W_o-HsWg4O_pIxUYcMWao2lPgVN3fNuqDmMjCdnFsonF-PQg5-yLTt0CWwX13yH8fiseOGbndLhHp4_Qf_r1SUIHNi2qPigIEzdX4-FznEB4GdacFgS8GHk3wH7nLfPrLaNoDnXE8FkLWhktQGvlnyzDAhE1LIRIKTi187J-raiI75z1jm37q5-2RomiIPZub75rZ5pVvvPIzeMN7fu04ix2R2P07nlylLwrwbJA9_MVoLPKEcWw0ORYDnTCTGgBrAOwClGeqcCor-st3dQIcpmh1opdDtBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae28f96254.mp4?token=acX5M-_OrqLkExpwSSW4fjjeO9STF4-1CdzMsvf-Cna60teyeLFXYJTTbhb1fq1kC9K2e9-Nqpf0YacUJJckBMWnH3MPcM5cMNmP6jazbQa3j3qxIp5zycKpNgzO4XEB2fds33Z6wOW4fCIJ-IpwQrI_nSx2xPzRtgWBgJyJD5CojfHtpRIhwqPkCEjI439ieR75gguepBcMY4hBjAZdAaDh2zkQ2Qn3tUsqJf6TKZ_cRR7Cy9R5hCJOt9HojuNzfz5vM-AC1F-uFElKCpMPnkRpef1YrY1nzFcfmBOToOiQdRdg7Q9AElrYUl0aHF3GM46HkVJM0q0H0hxbPTU_GI0wjuSuWrE9sA_NR2S1vk2Cc1Vfott1wrAecD4nHBtuZKchI5DXWS9W_o-HsWg4O_pIxUYcMWao2lPgVN3fNuqDmMjCdnFsonF-PQg5-yLTt0CWwX13yH8fiseOGbndLhHp4_Qf_r1SUIHNi2qPigIEzdX4-FznEB4GdacFgS8GHk3wH7nLfPrLaNoDnXE8FkLWhktQGvlnyzDAhE1LIRIKTi187J-raiI75z1jm37q5-2RomiIPZub75rZ5pVvvPIzeMN7fu04ix2R2P07nlylLwrwbJA9_MVoLPKEcWw0ORYDnTCTGgBrAOwClGeqcCor-st3dQIcpmh1opdDtBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دوي صفارات الانذار داخل الكويت</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85178" target="_blank">📅 23:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85177">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏
🇺🇸
الحكومة الأمريكية تسحب مذكرات الاستدعاء الخاصة بمراسلي صحيفة نيويورك تايمز في تحقيقها بشأن مصادر تتعلق بطائرة الرئاسة الأمريكية الجديدة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/85177" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85176">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7986b0253e.mp4?token=NXbOAAsAvgPjgm-or0hzJJ0JNi_8YpjJ7JDG1cnETnZ5JeimHirKmpcSo3deJncEIpEJo3kXHLwI1-XT2qfRTd93PvG3UoTdRW7Aq-7g8g9Mm4avVTVhTEcjt3gi5I_ugETdYlb-sCfQ73Jd_dX8cLGvXLk217tXGKDnpP2ZpfbNUc-BMMHTK8BkO8BUVkppxEPLwx6m9DXPPM5hvX-ZxxTm1g0Ul2e3il5P3oyM-RGN65UfyCFDOlZ8VtuZ8SRqZrGCElWJ9PcW5nics2hQD-QF6BH2_0C8uVDP2i2gKAbJM_g6iF88SznRQ_dcwoqg1VGHM0BLlfpIiEKZZkLjqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7986b0253e.mp4?token=NXbOAAsAvgPjgm-or0hzJJ0JNi_8YpjJ7JDG1cnETnZ5JeimHirKmpcSo3deJncEIpEJo3kXHLwI1-XT2qfRTd93PvG3UoTdRW7Aq-7g8g9Mm4avVTVhTEcjt3gi5I_ugETdYlb-sCfQ73Jd_dX8cLGvXLk217tXGKDnpP2ZpfbNUc-BMMHTK8BkO8BUVkppxEPLwx6m9DXPPM5hvX-ZxxTm1g0Ul2e3il5P3oyM-RGN65UfyCFDOlZ8VtuZ8SRqZrGCElWJ9PcW5nics2hQD-QF6BH2_0C8uVDP2i2gKAbJM_g6iF88SznRQ_dcwoqg1VGHM0BLlfpIiEKZZkLjqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار الانفجارات داخل قاعدة علي سالم الجوية</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/85176" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85175">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجارات قوية في الكويت</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/85175" target="_blank">📅 23:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85174">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/85174" target="_blank">📅 23:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85173">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجارات قوية في الكويت</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/85173" target="_blank">📅 23:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85172">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات قوية في الكويت</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/85172" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85171">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
اسماعيل بقائي:
لقد صرّح قائد القيادة المركزية الأمريكية (CENTCOM) براد کوبر صراحةً بمشاركة عدد من الدول الأعضاء في مجلس التعاون والأردن في العدوان العسكري الأمريكي ضد إيران. وإذا كان هذا الادعاء الأمريكي مجرد كذب، فإن ذلك يستدعي من هذه الدول أن تدحضه بشكل رسمي وشفاف.
‏وفي ظل هذه المعطيات، وحينما تمارس إيران حقها الأصيل والمشروع في الدفاع عن النفس بضرب القواعد والأصول العسكرية الأمريكية القابعة على أراضي هذه الدول، فإن التساؤل عن "دوافع إيران" لا يعدو كونه استغفالاً للمنطق ومحاولة تضليلية لا أساس لها.
‏لنكن واضحين: إن حالة انعدام الأمن والحرائق المشتعلة في المنطقة هي نتاج حصري للعدوان الأمريكي الإسرائيلي المستمر ضد إيران.
‏إن توفير هذه الدول لأراضيها كمنطلقٍ لتسهيل العدوان الأمريكي، يجعلها شريكةً فيه بحد ذاته بموجب قرار الجمعية العامة للأمم المتحدة رقم 3314 (المتعلق بتعريف العدوان)، كما يمثل انتهاكاً صارخاً لمبدأ حسن الجوار والمادة 2 (الفقرة 4) من ميثاق الأمم المتحدة.
‏إن ممارسة إيران لحقها المشروع في الدفاع عن النفس ليست إلا خطوة ضرورية لاستعادة الأمن والاستقرار في المنطقة بأسرها.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/85171" target="_blank">📅 22:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85170">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0960660f1a.mp4?token=RSRIbXKSm82W6Eb7Y6Su_8C4_ALvwiNCAnICXX77GDk00MV7EsWDjwZA57mwXSBD9k7rJp4VLiY3UTwkxwgQ4jhFrUS28pvnNoCPdN4NAQ2wOLXiv9Ld29LEiiwASP_Q9xMJvIF3sNJx84wyZ6d84NT9hzYJbnd7UBBz73kkBmNsduqQ89eZpvN_T8rsBW3nxuBsuctwl1Ef6WY9hh58XlUuYMxfc9aXGZydufxAAbTyEsKPqcytjt8Yr4DJjTReHWFoxSPkqxVU5zzXg5nktM4PlzhNDFDPYhl1_4IZ_NhbsIbRanLQwZN8iA1EScasUWPubO7WEKok2QERawfvAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0960660f1a.mp4?token=RSRIbXKSm82W6Eb7Y6Su_8C4_ALvwiNCAnICXX77GDk00MV7EsWDjwZA57mwXSBD9k7rJp4VLiY3UTwkxwgQ4jhFrUS28pvnNoCPdN4NAQ2wOLXiv9Ld29LEiiwASP_Q9xMJvIF3sNJx84wyZ6d84NT9hzYJbnd7UBBz73kkBmNsduqQ89eZpvN_T8rsBW3nxuBsuctwl1Ef6WY9hh58XlUuYMxfc9aXGZydufxAAbTyEsKPqcytjt8Yr4DJjTReHWFoxSPkqxVU5zzXg5nktM4PlzhNDFDPYhl1_4IZ_NhbsIbRanLQwZN8iA1EScasUWPubO7WEKok2QERawfvAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
تضهر صور الاقمار الاصناعية تدمير مركز البيانات التابع لشركة امزون بالبحرين على اثر قصفها بالصواريخ الايرانية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/85170" target="_blank">📅 22:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85169">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇱
اعلام العدو: جاري تحقيق بوجود حادث امني عند الحدود مع الاردن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/85169" target="_blank">📅 22:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85168">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHynhznJR91RjQKTdmWa3M4jF-tgH4T0BYroqHGtZ-D6Bw5aKa6Bhq6SzjClvSR6Se-gECBhFRjpY2wj6SuAucJY__kGuiVCvFx-1RSF9UpJCIZVdFbrBTRUumvir72LLFiM7PAu21Hr4DQKx_Y0TuV6lZP4wAPpGDTT-WesHbFnuX0NT_vz0YBecgOSedXUXIbpozqvU7xn4MS6_KSY3bIpGYhS5adSu4BhGUheAr2-HRfEb9uUthUnVGPsNIRZ5cAwzoEQuLOE5Zyi83bCXSrivol-3IdBt2c9y19aEOc-JgeWiwr0F-HOgSvI7IDKJFv2X0j4ajfH-3KHGP5xEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
مواطنة كويتية تهاجم ترامب ان تهاجم ايران وأحنه نأكلها
اتركوا لها تعليق جميل
https://x.com/q8mahaal/status/2080319421759819938?s=46</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/85168" target="_blank">📅 22:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85167">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇱
‏
جيش الصهيوني:
سنرد بحزم على أي هجوم إيراني علينا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85167" target="_blank">📅 22:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85166">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇱
اعلام العدو:
جاري تحقيق بوجود حادث امني عند الحدود مع الاردن.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85166" target="_blank">📅 22:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85165">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
🇮🇷
حركة الزائرين الان في منفذ الشلامجة الحدودي بين العراق وايران ..</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/85165" target="_blank">📅 22:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85164">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbc6b9e32f.mp4?token=snMvxTZCcEhfy1_KmzH1W5AOjqf3376FBlQyezMDsIxVp3FJy93dPs-oSJgyTrSGGC7hREMypn5lMKtpHyE73GQTHGQXwskX4_PlSd1SQUFgkXwCErmHCf4pGqj_s80WcXjUcLL7PjUApOT0cYwgO1JZMsollBI4_Q_RaJkhrVV7NnVJfCOf44CLSdvPMialn1act52O2d5Qttw_WWxHCcO1xKAPryZwxWVUjytzHV7nlz9IGSaIF8kfpk6UyuTJRFGXGAaV2XLZVWO2y36vBFY9Mtc_KO9uQimQKZg06xL7ipgVg6qFgUHx049zRLfZxkM6xg_d0_de6MfRMWJVCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbc6b9e32f.mp4?token=snMvxTZCcEhfy1_KmzH1W5AOjqf3376FBlQyezMDsIxVp3FJy93dPs-oSJgyTrSGGC7hREMypn5lMKtpHyE73GQTHGQXwskX4_PlSd1SQUFgkXwCErmHCf4pGqj_s80WcXjUcLL7PjUApOT0cYwgO1JZMsollBI4_Q_RaJkhrVV7NnVJfCOf44CLSdvPMialn1act52O2d5Qttw_WWxHCcO1xKAPryZwxWVUjytzHV7nlz9IGSaIF8kfpk6UyuTJRFGXGAaV2XLZVWO2y36vBFY9Mtc_KO9uQimQKZg06xL7ipgVg6qFgUHx049zRLfZxkM6xg_d0_de6MfRMWJVCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: إيران ليس لديها جيش، ‏ليس لديهم شيء سوى أنهم لئيمون وأذكياء، ولا يزال لديهم بعض القدرات.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/85164" target="_blank">📅 22:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85163">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇺🇸
ترامب: ‏كنا في فيتنام لمدة عشرين عاماً، وخسرنا آلافاً ومئات الآلاف من الأرواح. كنا في أفغانستان لسنوات. ذهبتُ إلى دوفر. قُتل أربعة من الوطنيين الأمريكيين العظماء. هذا يعني 18 قتيلاً في حربين. 18 قتيلاً فقط، بينما خسرنا في فيتنام 200 ألف قتيل، ‏استقبال الجنود…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85163" target="_blank">📅 22:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85162">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70fe84e6b1.mp4?token=nA58VFUfAJWeJUUJOFv5GPOVJzMpCD9PmBg1hHFszA1cFgEjf7SUbLuzVCstSPNLMSRtPqHfYKkktrC8xevuH1_0peUoikzCew4WfZnKtr5IMddI-vRnHf0u1eZguZcJtn5hcDJBuxlqeb6nhboI1mRTekhvEmbG06HX1m9DpD5fXxyCCWTLCa2Jq0XF9IecJMypX4YCpePEUYM833aNQqMWk2J7tW2QaY5hAQI_NYwelO2qpcBjaxyF_mis6IBUeGORJB5vqJ02J5dkjwGwrhDAXzHyy1tN94V_WcvCDXztCrmeWVTPjviXHRwBMWeu8KzirKuigOZW5wH_7TNYxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70fe84e6b1.mp4?token=nA58VFUfAJWeJUUJOFv5GPOVJzMpCD9PmBg1hHFszA1cFgEjf7SUbLuzVCstSPNLMSRtPqHfYKkktrC8xevuH1_0peUoikzCew4WfZnKtr5IMddI-vRnHf0u1eZguZcJtn5hcDJBuxlqeb6nhboI1mRTekhvEmbG06HX1m9DpD5fXxyCCWTLCa2Jq0XF9IecJMypX4YCpePEUYM833aNQqMWk2J7tW2QaY5hAQI_NYwelO2qpcBjaxyF_mis6IBUeGORJB5vqJ02J5dkjwGwrhDAXzHyy1tN94V_WcvCDXztCrmeWVTPjviXHRwBMWeu8KzirKuigOZW5wH_7TNYxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يعلن عن مناقشة قادمة حول الحرب مع إيران.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/85162" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85161">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4D3X0VUSAZpmdqcLfMLWpwquJSKAOSyFKmUVkoyihzYM30ixFtYylSNOWy3c48GWFL99CIujBOJ90WPA9otxGuArN-2cVrFclHIVFaKIaZ6o6Li38KWzeeFuHewe4GG9aCcfI5oZPwxCzA-CylWRBcvOs5SPq3-jmd8WzistcWDPky5g4idnt7En6lvJI8BuWxHfLJj_rgAOQ98bUq4wJDnP1o-I586QtQWdu5NWEoUJIO2gbDRCoUPL6qaiJHdDjjQENMcLc2plDaIalHeWn4_9JDBlfyF3GIEL9wrwxh4qBZyD5GkQwPfUOqQaYaZ38F4rSt0cUehBzH2OcrgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاول مرة
الجيش الأمريكي يشتري صواريخ باتريوت PAC-2 القديمة لأول مرة منذ عقود
‏صواريخ PAC-2 GEM-T ليست عموماً بنفس كفاءة نظيراتها من طراز PAC-3، لكن الجيش يحتاج إلى كل صواريخ باتريوت التي يمكنه الحصول عليها.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/85161" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85160">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85160" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85159">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
مصادر ايراني توضح انه لم يحدث اي انفجار في شيراز</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/85159" target="_blank">📅 22:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85158">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامب يعلن عن مناقشة قادمة حول الحرب مع إيران.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/85158" target="_blank">📅 22:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85157">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">يا قائم الـ محمد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/85157" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85156">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/85156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/85156" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85155">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔻
مصدر خاص من فصائل المقاومة لنايا   بسم الله الرحمن الرحيم  العملية الأولى  تقرير عن عملية مسیرة بتاريخ ۲۳ یولیو ٢٠٢٦ الساعة ١٤:٠٠ استهداف معبر الحدود الكويتي ردًا على الاعتداء على معبر حدود شلامجة  إحداثيات الهدف: 38R PU 60460 31042</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/85155" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85154">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
مصدر خاص من فصائل المقاومة لنايا
بسم الله الرحمن الرحيم
العملية الثانية
تقرير عن العملية الجوية الثانية بتاريخ ٢٣ يوليو ٢٠٢٦ الساعة ١٩:٠٠
الهدف: مبنى قيادة الحدود الكويتية ردًا على الهجوم على معبر شلامجة الحدودي
تفاصيل الهدف:
38R PU 61239 32037</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/85154" target="_blank">📅 22:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85153">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔻
مصدر خاص من فصائل المقاومة لنايا
بسم الله الرحمن الرحيم
العملية الأولى
تقرير عن عملية مسیرة بتاريخ ۲۳ یولیو ٢٠٢٦ الساعة ١٤:٠٠
استهداف معبر الحدود الكويتي ردًا على الاعتداء على معبر حدود شلامجة
إحداثيات الهدف:
38R PU 60460 31042</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85153" target="_blank">📅 22:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85152">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ربما يسمح بالنشر بعد قليل</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/85152" target="_blank">📅 22:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85151">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
تواصل أسعار النفط العالمية ارتفاعها عقب التطورات الأخيرة وإغلاق مضيقي هرمز وباب المندب ليتجاوز سعر برميل النفط حاجز 101 دولار.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/85151" target="_blank">📅 22:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85150">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a796ffbbb1.mp4?token=JfUgA3cX_IJIsP5Z7qnbHVYuI4pCu8IU1bXpuHRJjgQ1QHhqA_8qmJkv0RMPnMv4Y254bYdYwb2mauQhLp1NA36-c9bLuAfSQRvlNgJkkn9ld-SBTt9UzEUCx1EYxTn2yrYmdXEd4JYmoiT4vdm1I65CTvD_aQjU0320wQclgzteSDkKt-SK-1K5qjZDWoorFbnfby2-Xh8C32QXa3KfTDHZXHJoAU2oW8TfC72iIyO3EBsNveCK0Ky60eGi-d92_F16rHepME50HY5SY8m761E_MrIGKsi8FZAls3A8AtoDahbHQgnI4mO-wR2bG7og-y3N8VoxESfQCRSrDh0CGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a796ffbbb1.mp4?token=JfUgA3cX_IJIsP5Z7qnbHVYuI4pCu8IU1bXpuHRJjgQ1QHhqA_8qmJkv0RMPnMv4Y254bYdYwb2mauQhLp1NA36-c9bLuAfSQRvlNgJkkn9ld-SBTt9UzEUCx1EYxTn2yrYmdXEd4JYmoiT4vdm1I65CTvD_aQjU0320wQclgzteSDkKt-SK-1K5qjZDWoorFbnfby2-Xh8C32QXa3KfTDHZXHJoAU2oW8TfC72iIyO3EBsNveCK0Ky60eGi-d92_F16rHepME50HY5SY8m761E_MrIGKsi8FZAls3A8AtoDahbHQgnI4mO-wR2bG7og-y3N8VoxESfQCRSrDh0CGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الآن، صاروخ «ذو الفقار» في ساحة آزادي (الحرية) بطهران.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85150" target="_blank">📅 21:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85149">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZcSQcs45zDwNY1RXoX6cO-mIjyIEcyDWWrahjAFxTlU-6htuhmRZRY35DTpdyTZ6F4x-bhgw7U78PYlpiQErCij_mCqy_kwG9v_OaSKthuQAfrze3q7AXuhUxgHQyzNedkgUl-Sm9MQoWlQaiqlKlG20Ohw2CS6_D-0ZUIqic3NMwumqZTDzhnCF4oENk9C3nzbWu18bOQAj3BBRWZ0UBeyoWlpw0EjOoEv82WgRztr2Tuy-F2xaN4arj4EppkDpdVrMgoSTdBggYfw2VaVqKRbsVm2Q4gXDrTavW3lmiyLQ9IjvORoSOHbOaTT1-yvBGkPrmu933VZUhUSi2QwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
يتقدم أهالي العراق وحركات المقاومة الشعبية حول العالم بأحر التعازي والمواساة بوفاة المناضل الياباني
كوزو أوكوموتو
أول وآخر لاجئ ياباني في لبنان المعروف باسم
"أحمد الياباني"
.
لقد جسّد الحاج أحمد نموذجا نادرا في الإيمان بالمبدأ والالتزام بالقضية مؤكدًا أن طريق المقاومة والحق لا يعترف بالحدود التي يرسمها الاحتلال ولا تحده جنسية أو لغة أو عرق. وستبقى سيرته شاهدا على أن الانتماء الحقيقي هو للموقف والقيم وأن نصرة القضايا العادلة تتجاوز كل الفوارق.
الرحمة لروحه، والعزاء لكل الأحرار الذين عرفوا فيه مثالًا للثبات والإخلاص.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/85149" target="_blank">📅 21:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85148">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe18daab7f.mp4?token=Qnh-j_aWFUYEc3sk807S9n6voxZVsVFIiLT5quzzvJANgnBydtRlCRjlJhrjTHDcCqYYgv1VQXvun1ZEsJK5mumGNlbZBBizg3zgUiGO7iaKUkaCpQjzKx2DdSbFqwJjhSlgWBXDCuGRjQuvdpUAWwq_akbGHsm7dpRqvyp_YP1K_L2KZfsr_-lh0VvJfQzoCNXACu3nyEDAMEJl39HuA3-Uy3wn--U0L2QWsJ2aXLSOCz0_Clvk9TQsQWL5t8weyFutHj7DNG8wC3LOXyTUJpuyLRk2rFyKPGCSKRACb08ARNQ_T3-cY_B4gy5fSqk1CItBPqBMnIbyJynnYFWuHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe18daab7f.mp4?token=Qnh-j_aWFUYEc3sk807S9n6voxZVsVFIiLT5quzzvJANgnBydtRlCRjlJhrjTHDcCqYYgv1VQXvun1ZEsJK5mumGNlbZBBizg3zgUiGO7iaKUkaCpQjzKx2DdSbFqwJjhSlgWBXDCuGRjQuvdpUAWwq_akbGHsm7dpRqvyp_YP1K_L2KZfsr_-lh0VvJfQzoCNXACu3nyEDAMEJl39HuA3-Uy3wn--U0L2QWsJ2aXLSOCz0_Clvk9TQsQWL5t8weyFutHj7DNG8wC3LOXyTUJpuyLRk2rFyKPGCSKRACb08ARNQ_T3-cY_B4gy5fSqk1CItBPqBMnIbyJynnYFWuHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مسلحي العشائر التابعين لحكومة الجولاني وعصابته يعلنون بدء الحرب ضد ميليشيا قسد في مدينة الشدادي بمحافظة الحسكة السورية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/85148" target="_blank">📅 21:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04132ae88a.mp4?token=l864y5Gxu5oqZ2PWQCPUcc4UnyjPI2ghzq2wUXG6-tHwlODBRe8Vgv3G-SL-vz29VIQ4194AVPWTC8tOjf1E8fNoFapekvF9wtbQzG96TihfxtyhmZnY907cksYvWT6k0LAJdWxyiwLwVoVGi1Od-I1EQDIbVBw4J5ky5ZRxS8661ZacKx_EgcAJ1cz9hOxRGMnpdeWQmDGVr19YT50JlRYI79RJ5f01csY_iXxHWysBr6FisZ9jOP28Q3VJ0Ngvz7whyHXWUP_UCW2-eSre9p5-pbbkYMcDf0-L43PQWS8yQ55E6_EUwOCK6Fk6Z0ul2v6d3F9i4UZnraKHMB9VcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04132ae88a.mp4?token=l864y5Gxu5oqZ2PWQCPUcc4UnyjPI2ghzq2wUXG6-tHwlODBRe8Vgv3G-SL-vz29VIQ4194AVPWTC8tOjf1E8fNoFapekvF9wtbQzG96TihfxtyhmZnY907cksYvWT6k0LAJdWxyiwLwVoVGi1Od-I1EQDIbVBw4J5ky5ZRxS8661ZacKx_EgcAJ1cz9hOxRGMnpdeWQmDGVr19YT50JlRYI79RJ5f01csY_iXxHWysBr6FisZ9jOP28Q3VJ0Ngvz7whyHXWUP_UCW2-eSre9p5-pbbkYMcDf0-L43PQWS8yQ55E6_EUwOCK6Fk6Z0ul2v6d3F9i4UZnraKHMB9VcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مسلحي العشائر التابعين لحكومة الجولاني وعصابته يعلنون بدء الحرب ضد ميليشيا قسد في مدينة الشدادي بمحافظة الحسكة السورية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/85147" target="_blank">📅 21:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85146">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzLZD78xymQc58MVHsh3zme_YV__4wEIVXDnCoPlJzRryAq_TFFs_Jg-a4QqLaI5zqvzZWEynwPQ0Pu1C-hO4n7_5HNoqWh-W_oFdaAhdoLTVYAfDvhcVNE5yuUHV9UHwIIIAAq4IPDRpLCtMF-2wOfSyczoQkxE0TJBFB954att9RZui-4hw_jS9F9kJrxeqdgeK4FofXaVhCE0Iitf7eaWZ39hmFTJQXQYJaDqx4j1Nn2BxzjOPVHsfG7asC-yCCJ4_qCzVmwvFxWui1EakL9-6z9czoMbh-rKIU2gLdTtI57eJt5HrZUDXx_8Bz1D3GjmLqWmYaaP8p86-kYNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الآن، صاروخ «ذو الفقار» في ساحة آزادي (الحرية) بطهران.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/85146" target="_blank">📅 21:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85145">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇶
اشتباكات داخل احد مقرات الاحزاب المعارضة الايرانية ومقتل العديد من افراد المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/85145" target="_blank">📅 21:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85144">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcFTlpH8ALwGCD_LUsRjgcKCEaaY9mPAXcLFQFaEI711qIwpkAUBnpnShOOI1hgaMu1PfohIeHKD2F0keTRmCgsmXJPDbXWGLqo-5E2r1FjvlH9-4N1F9SXPqk-dt5E3_KYpmfTRwCLvXP4hueo4qG_XhjJa_Sy7iiH2-gLqWQUwd803jSVKNvGgZ895Rc7igVTaZJ_0_KtHC99rgqWyK70bBA3oby6G6mOcXlKl3m2vryRIPys7qCnwMhXjMsCXTMfl2vkf1ifBQ1VNp_0UlVkQxHPvxj4bTFZ4Mqq7uR3vcA93GRPkI71JIT1BK3pvCK_YBxUiaHAYN1gqRMklrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
خريطة للعمليات التي نفذتها إيران منذ ٢٣ من شهر الحالي بناءً على البيانات الرسمية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/85144" target="_blank">📅 21:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85142">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رويترز
": سفينة تجارية خُطفت الأسبوع الماضي قبالة خليج عدن في اليمن باتت في قبضة قراصنة صوماليين.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/85142" target="_blank">📅 21:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85141">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d399ccf44.mp4?token=BmSoaDL9LSFShJpdymks5fU2zMq5xdfV-XtcDN9kKdJYXrtUvZlHFr5WNIQeQtqeD3ho2ClyX62qmqtCvyxUr-t2hr6VUxDFUzR7jjRZ8rc0jMnFRLOczNTZMM9N60QTLRMIaxo5ATCfYE7hVHseJAusdIp0cLZ-m84P4Gkals_1d2pmTHjH-c5ZjrYfZA_AsYoV3Ji_U8cyjEmR9FXa8sCcEjzhOOwuGPmHGtquwJ8DjLXh6q5QnXNqlAjnH3TvafUkKW484zNOu5_sEUJeabJlbmubKN15vV-9lqd-IeLhOOJTBE3Hd-vU_Ylxvu-_jaf87CrzZE1bxRAxPz9HDKnQC3bcbi7dBUMpJ9zPjLXnKkxN2CWBC5H_Pjj_upgUL49DP1GbdyFzd1BsE9D6GlbcOx8D7FImrnV8aArzbKa5IwHNLknZorK9R44h7gde9t-T0x6rLlf3Im3khOA7oCs22Pfv7Nj9tyOiDPUmapOKG5GI8t5mxbiMcDwM5EtfyvPZngsskhGNOjUW1FsLnVYsm2vGjKWuQ2sR2MHYwq0J4VpjEQXCd9wimmFwRXHlwuwWSFiVCmcJYS9N4PjoeA-febMypR5SEEGZNmAA29g8rzB9JcOCBl16b5396KVM_SRqK4iJX7rJGsNo_m9OVTYDSFrkhxbhgnTXnKssmHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d399ccf44.mp4?token=BmSoaDL9LSFShJpdymks5fU2zMq5xdfV-XtcDN9kKdJYXrtUvZlHFr5WNIQeQtqeD3ho2ClyX62qmqtCvyxUr-t2hr6VUxDFUzR7jjRZ8rc0jMnFRLOczNTZMM9N60QTLRMIaxo5ATCfYE7hVHseJAusdIp0cLZ-m84P4Gkals_1d2pmTHjH-c5ZjrYfZA_AsYoV3Ji_U8cyjEmR9FXa8sCcEjzhOOwuGPmHGtquwJ8DjLXh6q5QnXNqlAjnH3TvafUkKW484zNOu5_sEUJeabJlbmubKN15vV-9lqd-IeLhOOJTBE3Hd-vU_Ylxvu-_jaf87CrzZE1bxRAxPz9HDKnQC3bcbi7dBUMpJ9zPjLXnKkxN2CWBC5H_Pjj_upgUL49DP1GbdyFzd1BsE9D6GlbcOx8D7FImrnV8aArzbKa5IwHNLknZorK9R44h7gde9t-T0x6rLlf3Im3khOA7oCs22Pfv7Nj9tyOiDPUmapOKG5GI8t5mxbiMcDwM5EtfyvPZngsskhGNOjUW1FsLnVYsm2vGjKWuQ2sR2MHYwq0J4VpjEQXCd9wimmFwRXHlwuwWSFiVCmcJYS9N4PjoeA-febMypR5SEEGZNmAA29g8rzB9JcOCBl16b5396KVM_SRqK4iJX7rJGsNo_m9OVTYDSFrkhxbhgnTXnKssmHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العوائل الكويتية الكريمة تناشد عبر نايا العراقيين بالسماح لهم بفتح المنفذ الحدودي مع العراق بسبب النقص الحاصل بالباميا والقيمر العراقي والنومي بصرة والخريط الذي سوف يتسبب بمجاعة كبيرة لا سامح الله إذا ما استمرّ الوضع</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85141" target="_blank">📅 20:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85140">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
بحرية الحرس الثوري تستمر باطلاق طلقات تحذيرية للسفن المخالفة لقوانين عبور مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/85140" target="_blank">📅 20:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85139">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErKFOoGDytsdNj3wLFm93EG0e4b4xgWETTvejuUQ46tz53DQsrM23LQe33tjDn0x39iUu-VmRNiFmehCAGqfiyDfwHKiGU523yStOYvG1yREuFCVA08N9Okmi7VJzyruOJYACI4ilMZ4BbRnwPQd4qBfG3zuogg6I28y9A8k1y93hvLEeQGkGEAXAXW7Pcb9UZEfs46LosSRWlzxGecK-HGo-eGfB1uoW901gNrQr1gB0Y212XqtrGVqBzllE1YZm7m0tWn_pCdLvVnSEPpXZLb2AvM_3s_ihaL4s1LsQ1Y9u_T7l_0JO8mPvtXzTJAVl8kWKIhgOUqjMVna6_xAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط تتجاوز الـ100 دولار للبرميل</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/85139" target="_blank">📅 20:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5kAqIcn8Eyf0SIXAe0cfoDH_Earl3TilflsEvslt7xhaA-Ki7BY69RI7flAdG2aRAEgV8URYWROXHZsx81BMzY4pVd6MLI5IwWg_K_IooR2kNwcqYJM7bRJJnXMfGXhd8k9KacQZZOFONehMBHQk8xYkfFHQ-F3f2oYs7B-UQzys20Bs6oFUyEn44pY9PogJiHf9L-lJE1TnthXUYcTXWYGAfOZULIxkEL28quJ-HowkwOnG0wyMj26GpCnAM9KUqK5K_knbG_agEPyCZG-IUEMQKPsHQYo3lzU5owGiKub0e-5UXfqFD2c_okxq5mkmQwLt9kWFhqaANPZOedCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇮🇶
هل ستحاسب هيئة الإعلام والاتصالات العربية السعودية ؟!
تحاول دولة السعودية عبر إعلامها قناة العربية تخريب العلاقات بين الكويت والعراق علما ان ولا جهة حتى اللحظة تبنت الهجوم والعراقيون يمتلكون من الشجاعة والإقدام ان يعلنون ما يقومون به بلا خوف ولا تردد ! هل سيحاسب بليغ ابو كلل العربية !</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/85138" target="_blank">📅 20:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
بريطانيا
: قواتنا جاهزة للتصدي لأي هجوم بعد تهديدات إيرانية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85137" target="_blank">📅 20:39 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
