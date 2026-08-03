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
<img src="https://cdn4.telesco.pe/file/i7uRXO5Zm3iJRdc0qbpZ_Xhr5bCu2_9bzQrLs7-vbIAZ_If_k2lmnPp8CTrV3tZPxONPKEelCGdizfh9Myw-cSZhZg-EueUsXJg1GoWUQEZ6Y_ohLCoXiYvnCze14BYRtOx0lleR7Hx2MwQ9PPoeLAH6Li1JcUo_MG0VmvdmW_y7o8uYTQURn32pJUX3t6ylV9zoTPZlbwd61kSsWsQ9NbU_lPASlUwiKNvR6D-N77BJUn4kAFlOB-5OLSeUAY4Nk3XxbfCIcuZE32ZsgRqbgqD_ehnrnnbSMGI7NmJa7RVE94GRxvoaw-nuOTTKUgz-pbWy0JxEcilXbdlHLYAqjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 17:48:11</div>
<hr>

<div class="tg-post" id="msg-86816">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سماع دوي انفجار في دبي</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/naya_foriraq/86816" target="_blank">📅 17:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86815">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجار يهز الامارات</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/naya_foriraq/86815" target="_blank">📅 17:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86814">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجار يهز الامارات</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/naya_foriraq/86814" target="_blank">📅 17:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86813">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📰
أكسيوس:
الممثل الأعلى لـ"مجلس السلام" ملادينوف التقى نتن ياهو وأبلغه بضرورة وقف الهجمات على قطاع غزة.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/naya_foriraq/86813" target="_blank">📅 17:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86812">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
‏
ترامب:
شركات النفط.. واخفضوا أسعار النفط للمستهلكين، الآن!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/naya_foriraq/86812" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86811">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇶
🔻
لوحةٌ عملاقة بمساحة 2500 متر مربع تتوسط المنطقة بين الحرمين الشريفين، يرفعها الحشد الشعبي حاملةً صور الشهداء، تخليدًا لذكراهم ووفاءً لتضحياتهم</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/naya_foriraq/86811" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86810">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوي صافرات الإنذار داخل السفارة الأميركية في المنطقة الخضراء</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/naya_foriraq/86810" target="_blank">📅 17:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86809">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HG5lklIwhn3QqHVumOXxwyi7rBKRKPFo5LCToIqj73wYDqEYmolxPWpo7tilOvuKChZgrf4OjAlCvvEvmluLJYJVD7SET-3Z45SKSrKaeuECzS0VXwf_m92azbmnixxC8pFfdOCTEMRKNnfwmw7M4BkDpQeeg1aPvKpQAgJvlooFxShkYaQsJ_fleSZebLp7DSJPrZ-4V2Qk3qObf1G23gCmhOdUAmKJb9tAgMC7S9nRRoiYedckB4hxap17uZ5f529eP7PH0vc3ZnOdweLyDaM-kSygMaz6IBmHNaCE9uH6MCB1e7t-WiGbti2qK2E6JBaljCvygmzoFwDb9X-c2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
بمساحةٍ تبلغ 2500 مترٍ مربع، هيئة الحشد الشعبي ترفع أكبر بوستر يوثّق صور الشهداء في منطقة مابين الحرمين الشريفين، تخليدًا لتضحياتهم، وتجديدًا للعهد على إحياء ذكراهم واستلهام قيمهم ومسيرتهم.</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/naya_foriraq/86809" target="_blank">📅 17:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86808">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAI8y9SCyEWsVGrW9zzAQXtz5tAT8Uprv5XSvjFhH8IwloB31OtfI-mSHAYV1WBtCBwLHSLtxBZulMWC3gTxQUKNW68hBYVtMcopjVNqtTfztfManeg0xWkxIavWFofAEsy_CxXoY1M896WxM33uFm-SBCmvkTPGkHk8AAEYI6tdCso6O-Hp-_tqCSzTAJ_yUwZyCsXPc2KPf7YnrgbvEMsRAJBP0dkdJdY_FCgYR14f5MWCzogNZrNhaP3ShWcC7rMuYF-NXOt0_Eyw8R6U_0AS6cRZD62l-0vCrXjJ5ovdQOhl47hTJFwHw2mfyFWles1N05Cs5FZ592G_NzLaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
بعد تراجع شعبيته كثيرا وفق الاستطلاعات بسبب الاثار الاقتصادية للحرب على الجمهورية الاسلامية.. ترامب:
إنّ استطلاعات الرأي الحقيقية التي أجريتها، وليست تلك التي تروج لها وسائل الإعلام المضللة، هي الأفضل على الإطلاق، فكيف لا وهي تشهد أكبر تخفيضات ضريبية وأعلى معدلات توظيف في التاريخ، وأكبر استثمار خارجي في أمريكا في تاريخ العالم، وحدود مؤمنة بالكامل، وانتصار ساحق في فنزويلا، ونزع السلاح النووي من إيران، واحترام ونجاح لا مثيل لهما في جميع أنحاء العالم، وغير ذلك الكثير؟ لا تصدقوا استطلاعات الرأي المزيفة التي يروج لها اليسار المتطرف. إنها فاسدة ومضللة، تمامًا كما أن الديمقراطيين الذين يدمرون البلاد فاسدون ومضللون. صوتوا للجمهوريين من أجل عظمة أمريكا!</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/naya_foriraq/86808" target="_blank">📅 17:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86807">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇵🇸
🇮🇷
رئيس حركة حماس خليل الحية للرئيس الايراني مسعود لبزشكيان:
نستحضر
الشهداء الذين ارتقوا منذ بدء طوفان الأقصى في مختلف الساحات على طريق تحرير فلسطين والأقصى ونعبر عن تقديرنا وشكرنا للمواقف الإيرانية ودعمها الثابت للشعب الفلسطيني، ونعرب عن املنا وتطلعنا إلى وقف العدوان على الجمهورية الإسلامية، وعودة الأمن والاستقرار إلى المنطقة برمتها.</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/naya_foriraq/86807" target="_blank">📅 16:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86806">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_5kicSvig-9lBvKlQhCFTHxom4WljcuMonrY4HidPje83YoNpj_yO95sO8cZz9eBfmebO1sIZRGsEb7zWk3gz6NS1FzisE_69GpKChB-ih3oWHhfvGPq8yLrRDBZZkLoVcDGmapo6e6uktjcUryJlgXkz2JgDHSODXA0KXHrym2P882tOrtP31jl1y5t-qM-QO_BQ4b6kfBUzrXQYv-fnFyWVa41Pqu0TIbe98JFDiMQ_QWJY_G-0TMm_Fm1Yg1IZo17OK_BGW_cedy5dQU6jOWr6vqZxD-HiAq3jM6TW1_cftVKhX70b-UOWxznXWf9dKo1kApGDYieb5KLmVWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
التهريب متواصل من سوريا
القوات الامنية العراقية تضبط كمية من الأدوية البشرية عددها (2,160) حبة من مخدر الأسنان مخبأة داخل عجلة قادمة من سوريا</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/86806" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86805">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الجيش الكويتي يعلن عن ‏تنظيمه تمرين للرماية بالرصاص الحي يومي الثلاثاء والأربعاء لاظهار قدرات الردع الكويتية وسط انباء عن قيام الحرس الثوري بتقديم اعتذاره للكويت والتعهد بعدم المساس بالكويت العظمى مستقبلا.</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/naya_foriraq/86805" target="_blank">📅 16:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86804">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc9490f89.mp4?token=E-gLzOlvXM8-P81sbhPMfsZkVBuxvYSlj2wXpYgEG7ezZf1cRsaX_sySrmWEL8ZYB43JoVuwW_JjT3Hz4nFD9ejBqQf6i2J0cO-VZkSl9shQzBxKQHNpGlzR5xqJm4aUm-lMCA3dkTEtAkOEkozoRbUwLGk57os1AM1pC49C9AsRZx4y4wIgGGAhMGPOJEa7jZB_sv01EAHD9fAwSDP1RE6P90r5QqCaHGZdxDVXjrkfTwjfKMkU0hzofNqv5xqgbz_3VGiHfQ56IFfszZaalz2uzdVVapyOiyk_dc6FrKIV3O74DWmiaEeBJPiWh7eeHSl-rANz_QqTHFenOV5Plg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc9490f89.mp4?token=E-gLzOlvXM8-P81sbhPMfsZkVBuxvYSlj2wXpYgEG7ezZf1cRsaX_sySrmWEL8ZYB43JoVuwW_JjT3Hz4nFD9ejBqQf6i2J0cO-VZkSl9shQzBxKQHNpGlzR5xqJm4aUm-lMCA3dkTEtAkOEkozoRbUwLGk57os1AM1pC49C9AsRZx4y4wIgGGAhMGPOJEa7jZB_sv01EAHD9fAwSDP1RE6P90r5QqCaHGZdxDVXjrkfTwjfKMkU0hzofNqv5xqgbz_3VGiHfQ56IFfszZaalz2uzdVVapyOiyk_dc6FrKIV3O74DWmiaEeBJPiWh7eeHSl-rANz_QqTHFenOV5Plg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اندلاع حرائق واسعة في الجليل الاعلى والكيان يستعين باعداد كبيرة من عجلات الاطفاء والطيران لاخمادها كما قرر الكيان اغلاق عدد من الطرق من بينها الطريق الرابط بين منارة ويفتح والطريق رقم 886 في كلا الاتجاهين.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/86804" target="_blank">📅 16:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86803">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
🇮🇶
مشاهد من الحريق الذي طال مصفى بيجي بمحافظة صلاح الدين بعد انفجار داخل وحدة الهيدروجين.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/86803" target="_blank">📅 15:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86802">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
🇮🇶
ممثل قائد الثورة في ‏حرس الثورة الاسلامية يصدر بيان بخصوص العدوان الامريكي السعودي على مجاهدي الحشد الشعبي:
.
لقد تعرضت قوات الحشد الشعبي الباسلة، التي لطالما اضطلعت بدور محوري لا مثيل له في تحقيق الأمن والاستقرار في العراق، والتي لا تزال تضحي بنفسها في ملاحقة فلول الجماعات الإرهابية التكفيرية التابعة لتنظيم داعش والقضاء عليها، لهذا الهجوم الظالم. ويُعدّ هذا العمل الإرهابي دليلاً على يأس وانحطاط أخلاق أولئك الذين يدّعون زوراً حماية حقوق الإنسان.
‏وكم نتذكر بجمالٍ أن هذه الأيام هي فترة الحداد على الأربعين، وقتٌ يسير فيه ملايين الحجاج على الأقدام بقلوبٍ تفيض حباً لكربلاء، ويهتفون بشعار "لبيك يا حسين"، وهم في الحقيقة يهتفون "الموت لأمريكا" ويعبرون عن كراهيتهم لجميع الظالمين في العالم. هذه الرابطة الوثيقة بين الأربعين والمقاومة هي رصيدٌ عظيم لن يستطيع أعداؤنا انتزاعه منا أبداً.
إنهم يعتقدون أنهم بهذه الهجمات الجبانة قادرون على كسر إرادة الشعب العراقي الراسخة، لكنهم مخطئون خطأً فادحاً.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/86802" target="_blank">📅 15:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86801">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇵🇸
في ذكرى اغتيال إسماعيل هنية قامت مجموعة من الشباب في قطاع غزة برفع لافتتين كبيرتين في حي الرمال وسط غزة تحملان صورتي القائد الشهيد قاسم سليماني والشهيد إسماعيل هنية وقائد الثورة الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/86801" target="_blank">📅 14:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86800">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇶
هزة ارضية جديدة في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/86800" target="_blank">📅 14:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86799">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇬🇧
🫡
التلغراف البريطانية :
‏لا يزال شبح قاسم سليماني يطارد دونالد ترامب حيث تستخدم إيران شبكة الشيعة العراقية التي بناها سليماني لجر الولايات المتحدة والدول العربية إلى حرب أطول وأكثر تكلفة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/86799" target="_blank">📅 14:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86798">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9EJHNZAzQqS2RRsaXHJc9CvoM3rXWHLFIn7-_Gg652RftgwWNWT5s6nD23tAO-HWdjkAINUtKZ3Y2osumEjJgvkc4cLX3_9T0brv2yU-TvLtoL6gJOANgzI5lXlZHZkZeXcX6iV3psU7aEexXFTsTDoHjPyF09LZe15cLwq0F77aFy5PXsNF1nFYRe6kVG9Tymj3XJ88nF58Xk0E6xpk3ryB-fAIH8E6Bb41FPLePJjDm4-TTTF3BFXdfmOGcRDN1V9Aur-IiPjozdBVuepIsyG1P1Hv_3eTRm7-fXwkPAfzBumYJUUyHBuwjaK6BTjn6BrDSNo9WTDS3DQlL7kOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العلم العراقي وين ؟!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/86798" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86797">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5afYDXYuECHv7TySD5c07kIJNMLusbKf23Q5T0RpMfeJea529YmIO2NIWSw0zg-Yqs-a9-PEFM6hOgkGlqZSmJr5tUx3tJjYX6Muo11SgMxuJvAw6OXnsABMR5pieH536sb-qM0c85qz5EsS3YZZSkJKdLUX4oAmKz_iYo4Una2K2acRhlILxGA_OFc0QHvfy4KzS2QLsq9V-jPpReH4OQQZg45cqhC7-7vaVc2B5aYMOABFli01ZV2nP3XFC4lEwtak0NqC1sx2t7ewiaxctFoaZOEdpBnWUon9R_TfJTy-LkUA5pNSup0I6ccDF_ELAHvN1G0ZctA08t1u-1dIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
وصول وزير الخارجية الايراني عباس عراقجي الى محافظة النجف الاشرف.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/86797" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86796">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وصول نيجيرفان بارزاني إلى دمشق</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/86796" target="_blank">📅 14:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86795">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25f2d7dae.mp4?token=eXOxDd0m_s-QNYUMqLLbQw21J1bjRCdcBotCz9IJjGN6fcYXrO4W1616Qw7YcNCM0b6cY9OCrcur6IpCqfe-kxc2FbgyxE6k_rkEFD0Izv4b6UFReGgobzca5h4DzCkWXFI1Fj9yPQzS4VeRQNZtbXk4Yuxjg2K-P47dc0FXD26vpIBkJ36J7GoFIi7yNRf34ffjRfxRe6xNPUJvUPun4MdO6_MkYyKa5PRTdVnZH1UlQaIFJ45wEhDYL7s-LtXjD1H1N868IweTw6MntNXRJdFDV_7WwnoV8S2wt7LKTJc9a9y4X9xKQlfaZlYPjYx2rB97ETuBgoJXkuEQzIHTAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25f2d7dae.mp4?token=eXOxDd0m_s-QNYUMqLLbQw21J1bjRCdcBotCz9IJjGN6fcYXrO4W1616Qw7YcNCM0b6cY9OCrcur6IpCqfe-kxc2FbgyxE6k_rkEFD0Izv4b6UFReGgobzca5h4DzCkWXFI1Fj9yPQzS4VeRQNZtbXk4Yuxjg2K-P47dc0FXD26vpIBkJ36J7GoFIi7yNRf34ffjRfxRe6xNPUJvUPun4MdO6_MkYyKa5PRTdVnZH1UlQaIFJ45wEhDYL7s-LtXjD1H1N868IweTw6MntNXRJdFDV_7WwnoV8S2wt7LKTJc9a9y4X9xKQlfaZlYPjYx2rB97ETuBgoJXkuEQzIHTAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر لنايا: وزير الخارجية الايراني عباس عراقجي يصل النجف الاشرف يوم غد للمشاركة في اداء زيارة اربعينية سيد الشهداء (ع)</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/86795" target="_blank">📅 13:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86794">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔻
اعتراض طائرة مسيرة من طراز MQ9 وإصابتها بواسطة نظام دفاع جوي متطور حديث تابع لقوة الفضاء التابعة للحرس الثوري الإيراني وذلك في سماء مضيق هرمز.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/86794" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86793">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الاعلام السعودي: نيجيرفان بارزاني رئيس إقليم كردستان العراق سيلتقي الجولاني غدا في دمشق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86793" target="_blank">📅 12:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86791">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V99P-UhDlrWsOXiEVw-juWdaL1kOFlxkXQVSWJmDqLO-1H_4iOtN1Ha8uOAeoilv_35OUhBcHvroZHftEkjs4AlH5beVoorl9M1S7rxZOuu0yeiD3hZs5J4quLFUC13x2uqixyTU5_fUuCtnU2A85kAu1Xg6nMN3D2TeeUvTHDMuMt9BQHXGqa_2aKlYQbxlgQjLXjQ099ovJBt9ZdbG_HAk5-Ln5hXktB_aD4ctM7_gF3Zy8AL23N6zrd3AHUR3efgGF9bPsgDhGSWsuK-wjOfRalgWboIAD5f5Fsui4KGUOtQl0fwMDOlYgCySZkM2bC98DOrswV8FiO48D9OzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vok4o7RbOafASw1RSvA44sx9PRHeOVwCBRkKkRDtgai_xFiS0oZe3lco-SMQrXYZfQtm5GREZYHLpt49q21qNlQvSHWYneMeJyYh1D80Lo-cmx5hbvPEX49AIXi-A6repJ4q1JHcW9-cENo7GSClt26-PbaLmW-ggYg5hyNVUVMbwJBzQqAS4ilOMvvSCw20W6Ee64xQtTCbPdvs9lcWe2f5OCgoRfFi78qESLcKmewipgYtGAQcVVcV3OywCFpofc1i7_h_TAGIN4st7b6BMonOwdWp4cc_y8TiWA6LHu1Zha3teA2ARUtjN5Ay3BNRDaWVps7akQ3V0eR4aWVmwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🇯🇴
🇦🇪
طائرة نقل عسكرية ثقيلة تابعة للقوات الجوية الأمريكية تغادر مطار العقبة في الأردن وتتجه إلى قاعدة سويحان الجوية في الإمارات.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86791" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86790">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33c71a96b.mp4?token=noEI01nAzB54LlGyMbBtRC0ZtlPvFwPr1W7YSfbixfPy5nEDP3_XJ3EFY82_XnKDuqcoCmEhayasatspswo9ktjedgc628iDcz1j1xBKIDXyxq0R-0EQU1jXcoZ46ILUa7lpQ4d7ZeAYuhxFTGJK_aC-ySEONZfV6FGfkE3bqi4Lj6HA7ngxSQtDOocfsWgfb9GrgS4eSzo3ce9iHaIeZWYtOiA7iXdQD6KjrQ-G_wgezLHc5toVMmqiMAYK99n4D00YwRrd5Sg8YZN9pgpb6k2XFMYpdZ0kzCZfmqzgD49pEI1JPMiyg0ihq1sjf43I07Yb3jcmh7uH154wtogIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33c71a96b.mp4?token=noEI01nAzB54LlGyMbBtRC0ZtlPvFwPr1W7YSfbixfPy5nEDP3_XJ3EFY82_XnKDuqcoCmEhayasatspswo9ktjedgc628iDcz1j1xBKIDXyxq0R-0EQU1jXcoZ46ILUa7lpQ4d7ZeAYuhxFTGJK_aC-ySEONZfV6FGfkE3bqi4Lj6HA7ngxSQtDOocfsWgfb9GrgS4eSzo3ce9iHaIeZWYtOiA7iXdQD6KjrQ-G_wgezLHc5toVMmqiMAYK99n4D00YwRrd5Sg8YZN9pgpb6k2XFMYpdZ0kzCZfmqzgD49pEI1JPMiyg0ihq1sjf43I07Yb3jcmh7uH154wtogIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
أبو محمد الجولاني: الاستنتاج الذي توصلت إليه من تجربة العراق هو أنه يجب ألا ننقل واقع العراق إلى سوريا. لكل دولة ظروفها الخاصة ومشاكلها الخاصة.  ما تعلمته من العراق هو أن الصراعات والانقسامات والنزاعات الطائفية التي استهلكت العراق يجب ألا تتكرر أبدًا في…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86790" target="_blank">📅 10:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86789">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e9f384c4.mp4?token=Aa05dK5fZHgWpoABM7MV4M4GdoG1W_WMhkeCmOghs4eSFBj65cjVgX4qlvOx-ylwd-kaHuW5H0ZiIGlw6b490kYtZiQc_WNQAb2DRlZtAgAPkNPbh2NLR0dUER-PxlxjnxpbGht0fgRKfQaBVLwmpI5WDWKY7pVsS75Y5rF9p0KaYopb2QKJIY9VjKlwvUCMg2twozdZLf_X7vyRSFbXTX-G41YLiTd14ZXzK3k_A4bU3dTzrlK0RYMU7VV32Oz59_5e34jw9BLin359C0buCfogkzR-PIvRAwNLreLT2ys_ghtIiQdrK97bncisSfleE-3YgZRIPV6JLm62BwWqB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e9f384c4.mp4?token=Aa05dK5fZHgWpoABM7MV4M4GdoG1W_WMhkeCmOghs4eSFBj65cjVgX4qlvOx-ylwd-kaHuW5H0ZiIGlw6b490kYtZiQc_WNQAb2DRlZtAgAPkNPbh2NLR0dUER-PxlxjnxpbGht0fgRKfQaBVLwmpI5WDWKY7pVsS75Y5rF9p0KaYopb2QKJIY9VjKlwvUCMg2twozdZLf_X7vyRSFbXTX-G41YLiTd14ZXzK3k_A4bU3dTzrlK0RYMU7VV32Oz59_5e34jw9BLin359C0buCfogkzR-PIvRAwNLreLT2ys_ghtIiQdrK97bncisSfleE-3YgZRIPV6JLm62BwWqB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
أبو محمد الجولاني: الاستنتاج الذي توصلت إليه من تجربة العراق هو أنه يجب ألا ننقل واقع العراق إلى سوريا. لكل دولة ظروفها الخاصة ومشاكلها الخاصة.
ما تعلمته من العراق هو أن الصراعات والانقسامات والنزاعات الطائفية التي استهلكت العراق يجب ألا تتكرر أبدًا في سوريا.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86789" target="_blank">📅 10:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86788">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f8a7eb0b.mp4?token=uA7Z6krBAQ3oaXEviwHwY2X5G7EupwxSVTjHzMiZ_gLMZa9gIzKiempCIKTefQ3BcaS7LXzqC8NFt00omVPPwsfcfmFX8bZ_6LCshG1HMMhdhK4RlBelswvIe9sA_OWXsOp7uOg6yOEeriDgzekamtH8bAnQEh1QrfJxwrY7CqWL_mjXLD8gecSbPPi7vw9UjVOJDi_QdvYVx7eP3ceuGojp9go8YPEjkBaJZmwsDQtTYSRoCqS2DSWkDMaPbhHGUbAa63quUwPDkc_Lrq9j-KiYZAMu1D_zwqzC9QqyQuzdsesaPQEcmc5NNE7z7J0h25q0yVbqFvS0fREsFqZ3pFw1weuQzcQHmJVfhTY5b6EHipJtYQNoxh7BpEt4Gd_SxnVgss-_6y290NAgYsI0d88OWIClGiOg9cGu2LI_MvhdKw9CLix1HKVVH5IFL4vZmnWPBGS7JEWHDFJ2pbIuX4i6OCoSVU-isDY2_0IROTfM16PnfJdjmqKIxJi86JngjbnOyTzHFbcNiShmxt6APZ1JaNVFZBrPBID7zXk5XLS2ZvDoT4E-Cf31MwFHLTwXScbRQ9DcPSwhOGEedEKY0lUNccmuXnLFYqurYsNIsDPmObKYdE4ljxWnjr2cH5y68LJ0QFI6sBwEWkgfT0w_bg96u57olImzCdpm-i9lXuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f8a7eb0b.mp4?token=uA7Z6krBAQ3oaXEviwHwY2X5G7EupwxSVTjHzMiZ_gLMZa9gIzKiempCIKTefQ3BcaS7LXzqC8NFt00omVPPwsfcfmFX8bZ_6LCshG1HMMhdhK4RlBelswvIe9sA_OWXsOp7uOg6yOEeriDgzekamtH8bAnQEh1QrfJxwrY7CqWL_mjXLD8gecSbPPi7vw9UjVOJDi_QdvYVx7eP3ceuGojp9go8YPEjkBaJZmwsDQtTYSRoCqS2DSWkDMaPbhHGUbAa63quUwPDkc_Lrq9j-KiYZAMu1D_zwqzC9QqyQuzdsesaPQEcmc5NNE7z7J0h25q0yVbqFvS0fREsFqZ3pFw1weuQzcQHmJVfhTY5b6EHipJtYQNoxh7BpEt4Gd_SxnVgss-_6y290NAgYsI0d88OWIClGiOg9cGu2LI_MvhdKw9CLix1HKVVH5IFL4vZmnWPBGS7JEWHDFJ2pbIuX4i6OCoSVU-isDY2_0IROTfM16PnfJdjmqKIxJi86JngjbnOyTzHFbcNiShmxt6APZ1JaNVFZBrPBID7zXk5XLS2ZvDoT4E-Cf31MwFHLTwXScbRQ9DcPSwhOGEedEKY0lUNccmuXnLFYqurYsNIsDPmObKYdE4ljxWnjr2cH5y68LJ0QFI6sBwEWkgfT0w_bg96u57olImzCdpm-i9lXuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بعزيمة يملؤها الإيمان وقلوب تنبض بحب الحسين عليه السلام ؛ انطلق أبناء موكب بني عامر في مسيرهم إلى كربلاء المقدسة لإحياء زيارة الأربعين الخالدة وتجديد البيعة لسيد الشهداء حاملين راية الوفاء والخدمة على نهجه المبارك.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86788" target="_blank">📅 09:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86787">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
إعلام غربي: التكاليف الاقتصادية الناجمة عن الحرائق والموجة الحارة الشاذة في دول أوروبا خلال عام 2026 تجاوزت 3 مليارات يورو</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86787" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86786">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d50a4696d.mp4?token=Gwa1P95Vk47c11JgGplzPgx2k8kigXtT8JOI8ekDfER6EeAGOWWHHRxvawvx10GS6piM0Cmg09dJ3HgG6--Uhzf0lXrW2XJEVpmX71GbxbCpv5XsK6Bs9-R5W5qMVoV-lfWzkFcH1rvDG0p2oAkDG2z_ZjThzZWCiQQdC7Yawr-PxD9UzjE5Vu8LU2fW8itRVx7OdwmJBFyeVXF1NKZ6uGEel8ZNULVE3338W7qn0-wRbAyXm5Vq6VrmHn38WwvRtz8UGLstNPcgq-ehxtc-mUHfMpfUuVG1gc499ZJCcKFbBMS0J9Gvh5ZkgaAM7n1LwqQm-HCmG8nF3CZE7cWI2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d50a4696d.mp4?token=Gwa1P95Vk47c11JgGplzPgx2k8kigXtT8JOI8ekDfER6EeAGOWWHHRxvawvx10GS6piM0Cmg09dJ3HgG6--Uhzf0lXrW2XJEVpmX71GbxbCpv5XsK6Bs9-R5W5qMVoV-lfWzkFcH1rvDG0p2oAkDG2z_ZjThzZWCiQQdC7Yawr-PxD9UzjE5Vu8LU2fW8itRVx7OdwmJBFyeVXF1NKZ6uGEel8ZNULVE3338W7qn0-wRbAyXm5Vq6VrmHn38WwvRtz8UGLstNPcgq-ehxtc-mUHfMpfUuVG1gc499ZJCcKFbBMS0J9Gvh5ZkgaAM7n1LwqQm-HCmG8nF3CZE7cWI2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجار داخل مصفى بيجي وحدة الهيدروجين بمحافظة صلاح الدين نتيجة خلل فني.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86786" target="_blank">📅 07:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86785">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d154890a98.mp4?token=UpMC9fmf5sEhpS0UEOMgsLEK9odWpO-rtm2xPNkbuu7F44adAQdAkBefb6Jh5i07KPVAylBHzm1YNEGvHRhIxNmjcEVxky3sNuD0Ysa9Q64gWj9-RVmlwqyzQqxV7xE2TmQ535FofIgVlpb1yeI8nsbtqlPGvosljZbrMFah_3YqPXuo_AGtRlIjp_pDVkNpUJjQ-GZsEENWQuMJHB5UMJapHEOdtb3lRcPz38ejCRHGtrUIvlcdFYCJ7dNjU2UhZ_5QeEevwp9TBiFLAVEh_Bp3_tP5qBJ9NtGn1izVzqiTT0rB3DGfXgdtCmKB8Xk0Umkw2s1GwIDNgjEK0UZeoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d154890a98.mp4?token=UpMC9fmf5sEhpS0UEOMgsLEK9odWpO-rtm2xPNkbuu7F44adAQdAkBefb6Jh5i07KPVAylBHzm1YNEGvHRhIxNmjcEVxky3sNuD0Ysa9Q64gWj9-RVmlwqyzQqxV7xE2TmQ535FofIgVlpb1yeI8nsbtqlPGvosljZbrMFah_3YqPXuo_AGtRlIjp_pDVkNpUJjQ-GZsEENWQuMJHB5UMJapHEOdtb3lRcPz38ejCRHGtrUIvlcdFYCJ7dNjU2UhZ_5QeEevwp9TBiFLAVEh_Bp3_tP5qBJ9NtGn1izVzqiTT0rB3DGfXgdtCmKB8Xk0Umkw2s1GwIDNgjEK0UZeoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة صلاح الدين العراقية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86785" target="_blank">📅 07:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86784">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة صلاح الدين العراقية.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86784" target="_blank">📅 07:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86783">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇪🇬
هزة أرضية بقوة 5.7 ريختر تضرب مصر وفلسطين المحتلة، مركزها شرق القاهرة.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/86783" target="_blank">📅 03:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86782">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الأمريكي: ‏كنا ولا نزال مستعدين لبدء ضرب إيران بمستويات لم نشهدها منذ الحرب العالمية 2.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86782" target="_blank">📅 03:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86781">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الأمريكي:
‏كنا ولا نزال مستعدين لبدء ضرب إيران بمستويات لم نشهدها منذ الحرب العالمية 2.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/86781" target="_blank">📅 03:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86780">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الله أكبر
🔻
تأكيداً لمانشرته نايا.. حادث أمني شمال شرق خصب في عمان.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/86780" target="_blank">📅 01:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86779">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
ناقلة نفط تحاول المرور عبر المسار الجنوبي لمضيق هرمز، بعد أن أوقفت تشغيل نظام التعرف الآلي (AIS)، وسط أنباء عن إطلاق نيران تحذيرية تجاهها من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/86779" target="_blank">📅 01:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86778">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6452ce4.mp4?token=W-7TFnlbJdJ36XPU1WHVvkwdLS354MhmMI9sj1dRXAMGZmGvshh5vZiaeT3SBoH07ZV1QLyFSfkLsyWGVmU5zPXZv9reKXVFgtI7Z6ak9uey-5GBMAmKiMFiyg3B4TPF6CT8BZFwQ2o7ooToUq5V0MTl94uqjhTK-D7ZQCob1_TBqAh9-gXMiBmarhQllLKNV7AVE72T9u0BuzdlDuaOYCa_xYSrh7J7C75WXMVnKvo90Y4faoRmtW81tu4s5o7a2skHRfNq7w3j4M1FZp60rUbn5seCgrV4U9RBZuOgn6jLPDKg5rP75XJhxsvZ8J_80hT-nYsbCAIVmWJkN_2JlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6452ce4.mp4?token=W-7TFnlbJdJ36XPU1WHVvkwdLS354MhmMI9sj1dRXAMGZmGvshh5vZiaeT3SBoH07ZV1QLyFSfkLsyWGVmU5zPXZv9reKXVFgtI7Z6ak9uey-5GBMAmKiMFiyg3B4TPF6CT8BZFwQ2o7ooToUq5V0MTl94uqjhTK-D7ZQCob1_TBqAh9-gXMiBmarhQllLKNV7AVE72T9u0BuzdlDuaOYCa_xYSrh7J7C75WXMVnKvo90Y4faoRmtW81tu4s5o7a2skHRfNq7w3j4M1FZp60rUbn5seCgrV4U9RBZuOgn6jLPDKg5rP75XJhxsvZ8J_80hT-nYsbCAIVmWJkN_2JlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هناك تقرير يشير إلى أنكم تقومون بسحب القوات الأمريكية من الكويت والبحرين.  ترامب: لا أرغب في التعليق على ذلك.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/86778" target="_blank">📅 01:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86776">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4e6ee609b.mp4?token=ni-aI_ECIPkb_cpD9yN-WdjTiTeFceJEMtZQ8iqrB0czRakuxPHavJZXp8FlmeTYMjc7AweZxsnp2_auWUMoBjimjeRqFkR4V3dDbRgb2wsqOm_fzbWAhZZva8S1yuZB03BbzrCm4FxDY0ZptwsawRM75VDSZanjZSPicarNrhl7uCLe6BdXb0Fd0Fy7qi1bd_5PVloHGgW0DUJ8VuySSJULGzTRhTcyBLcvD6HEcVWzECFkbYStPwVOY3ut_g39bhWP-c5KnJPSMbWdJ8eG17dSS3mSRdrbuvPZh2KStf3-2P3f9iNafa_TbM6bRTz4ZtZ77L42KMB-uxLyQP-YzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4e6ee609b.mp4?token=ni-aI_ECIPkb_cpD9yN-WdjTiTeFceJEMtZQ8iqrB0czRakuxPHavJZXp8FlmeTYMjc7AweZxsnp2_auWUMoBjimjeRqFkR4V3dDbRgb2wsqOm_fzbWAhZZva8S1yuZB03BbzrCm4FxDY0ZptwsawRM75VDSZanjZSPicarNrhl7uCLe6BdXb0Fd0Fy7qi1bd_5PVloHGgW0DUJ8VuySSJULGzTRhTcyBLcvD6HEcVWzECFkbYStPwVOY3ut_g39bhWP-c5KnJPSMbWdJ8eG17dSS3mSRdrbuvPZh2KStf3-2P3f9iNafa_TbM6bRTz4ZtZ77L42KMB-uxLyQP-YzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار توافد المواكب الحسينية نحو منطقة بين الحرمين في محافظة كربلاء المقدسة لإقامة العزاء بذكرى أربعينية الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/86776" target="_blank">📅 01:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86775">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65466746cb.mp4?token=WrD3L72nuL6VzedNiPt_BSug2bBjnGFJ-8w3tQ8Let_ffNYCb5UYA-HfvvCSH5bLLT_AIelniBbFK54eSUSKqVYRio6XWuZ7z02HsPaLthYFnKDjp9Y9bHnOyD1cttJuyDhpK8Jf97AUdUxhiawMjAYoJObJuhaAgFiJrW5IEjq4sEuQiWHGbCfKNxec6ST_kQ6pYksf-elDRQKK1imA9E_kmX0LsktfKtaFc2hDk2Sum8RiX3ZDB_xMtYeDBiH5j0d-1RZK5mJkzEl4QuR9_46haJqSs_F3Qpbt6qnO55Gc3PHXAwpuUOZZksORa_CNmgFka5qz1AXwWnN4KWzbRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65466746cb.mp4?token=WrD3L72nuL6VzedNiPt_BSug2bBjnGFJ-8w3tQ8Let_ffNYCb5UYA-HfvvCSH5bLLT_AIelniBbFK54eSUSKqVYRio6XWuZ7z02HsPaLthYFnKDjp9Y9bHnOyD1cttJuyDhpK8Jf97AUdUxhiawMjAYoJObJuhaAgFiJrW5IEjq4sEuQiWHGbCfKNxec6ST_kQ6pYksf-elDRQKK1imA9E_kmX0LsktfKtaFc2hDk2Sum8RiX3ZDB_xMtYeDBiH5j0d-1RZK5mJkzEl4QuR9_46haJqSs_F3Qpbt6qnO55Gc3PHXAwpuUOZZksORa_CNmgFka5qz1AXwWnN4KWzbRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول إيران:سألت ولي العهد السعودي: "ماذا تفضلون أن نفعل؟" فأجاب: "نفضل اتفاقًا على هجوم."</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86775" target="_blank">📅 01:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86774">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42bd64182.mp4?token=OxjFFH5t_7UgokH-mSTMnxi7HP5wwCVKLuDFmJD7LuZ5vZzu3gbcBCdgAXchoSm0roiHYZHWboUm8IieeWr3oZsN4uWcCj5-5nivRRKdYcvgbC4dry6AnDQ3OQgbFFk1crcFkxot8RjKwPwcamUWMg13xWfE8YX2om57hhMRdxBL7Tqj-PBRB6Q92oxyx4WpWS_HMyi79lB4MKctn6vnqEJ39hk9RJ_3hjq5ts5_kF6GBNAyc_CabWKIqpEJf4XlhfGP4VEyUgMMUfXan_gnHbJDMBQBNHXckaxlPe0fO1gG5odyrYqD1PC7p0xoLVU29Cq-pr9WwlJ9TMLOz21bYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42bd64182.mp4?token=OxjFFH5t_7UgokH-mSTMnxi7HP5wwCVKLuDFmJD7LuZ5vZzu3gbcBCdgAXchoSm0roiHYZHWboUm8IieeWr3oZsN4uWcCj5-5nivRRKdYcvgbC4dry6AnDQ3OQgbFFk1crcFkxot8RjKwPwcamUWMg13xWfE8YX2om57hhMRdxBL7Tqj-PBRB6Q92oxyx4WpWS_HMyi79lB4MKctn6vnqEJ39hk9RJ_3hjq5ts5_kF6GBNAyc_CabWKIqpEJf4XlhfGP4VEyUgMMUfXan_gnHbJDMBQBNHXckaxlPe0fO1gG5odyrYqD1PC7p0xoLVU29Cq-pr9WwlJ9TMLOz21bYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هل لدى إيران موعد نهائي للتوصل إلى اتفاق؟  ترامب: سنرى. أنا لا أسعى إلى إيذاء الناس.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86774" target="_blank">📅 01:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86773">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f191d3930.mp4?token=AooZ9Hu3uX11G6OVAXCIbsmuTYVIYw07vn-K3gUR5MSTk9mnMDXgFMWa6J8IJ8pnGO0ewKgDOd6oIvvzFoNjUBO9JIYQumMGKM6dnsGlAlD6ItWxkHDQXms79MbHv_RH_JZUQMl5xAi5z5Mpjt5w9U53W7HqU-YQGQBWPsJRkna1MDDi1LOK1umBFEmvciU-ZfEF6vwIO0f-s05EmjChH56semv33Y5TSRls7rKdF4ZiQ66g57JGwQGo2UjXC5lsFyPnrHk1am71YWVM5--TSoCKZPFh1um6GWnCWNvKixV6CYKPqMlp_wxXk051JKzenwJBZK0HudgfrIdh2pwd5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f191d3930.mp4?token=AooZ9Hu3uX11G6OVAXCIbsmuTYVIYw07vn-K3gUR5MSTk9mnMDXgFMWa6J8IJ8pnGO0ewKgDOd6oIvvzFoNjUBO9JIYQumMGKM6dnsGlAlD6ItWxkHDQXms79MbHv_RH_JZUQMl5xAi5z5Mpjt5w9U53W7HqU-YQGQBWPsJRkna1MDDi1LOK1umBFEmvciU-ZfEF6vwIO0f-s05EmjChH56semv33Y5TSRls7rKdF4ZiQ66g57JGwQGo2UjXC5lsFyPnrHk1am71YWVM5--TSoCKZPFh1um6GWnCWNvKixV6CYKPqMlp_wxXk051JKzenwJBZK0HudgfrIdh2pwd5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: نحن نتحدث مع إيران في إطار مفاوضات، وتبدأ المفاوضات غداً بعد الظهر.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86773" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86772">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏ترامب: نحن نتحدث مع إيران في إطار مفاوضات، وتبدأ المفاوضات غداً بعد الظهر.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86772" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86771">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏ترامب: لقد طلبت مني السعودية والإمارات وقطر وإيران تأجيل الضربات الليلة الماضية.  كنا جميعًا على استعداد للبدء. كان من الممكن أن يكون هجومًا ضخمًا.  عندما طلب الحلفاء تأجيل الأمر، يجب أن تقول نوعًا ما: "حسنًا، دعونا نرى."  إنهم يعتقدون أن هناك اتفاقًا. هناك…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86771" target="_blank">📅 01:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86770">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51407f800d.mp4?token=gVey0H-8LQ67wTPbvFo-xC3S4p-VJH1GJ5NimXRHESoV15cBpFhT24SPDYwWkcQ1gcmpvAJV31z_ROM0kgFTw0HI0Iut70spaUrNEyZvba_zT-E3Tkm5xVQMCosnQkJJ-sH4l9pOvmziFMrHVLMuQAs6BMU2flTf4lvyLbwj0hifGVsqliQr45X6Zo3s2hTAuJ1X4QpuitP2-g37s6S8e8gTIcvE2ZXnHYVnRyX8DJaDyPhmz1JzoALxpVBklLuzAWcvZP5wJ-nlGufKJAuXpd4Ymel5VYgA5gJ1pPJGui2NARcoZ_JiZNfKfMz-vR7AdHHnXuw5eyd6NLquPM2tlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51407f800d.mp4?token=gVey0H-8LQ67wTPbvFo-xC3S4p-VJH1GJ5NimXRHESoV15cBpFhT24SPDYwWkcQ1gcmpvAJV31z_ROM0kgFTw0HI0Iut70spaUrNEyZvba_zT-E3Tkm5xVQMCosnQkJJ-sH4l9pOvmziFMrHVLMuQAs6BMU2flTf4lvyLbwj0hifGVsqliQr45X6Zo3s2hTAuJ1X4QpuitP2-g37s6S8e8gTIcvE2ZXnHYVnRyX8DJaDyPhmz1JzoALxpVBklLuzAWcvZP5wJ-nlGufKJAuXpd4Ymel5VYgA5gJ1pPJGui2NARcoZ_JiZNfKfMz-vR7AdHHnXuw5eyd6NLquPM2tlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب:
لقد طلبت مني السعودية والإمارات وقطر وإيران تأجيل الضربات الليلة الماضية.
كنا جميعًا على استعداد للبدء. كان من الممكن أن يكون هجومًا ضخمًا.
عندما طلب الحلفاء تأجيل الأمر، يجب أن تقول نوعًا ما: "حسنًا، دعونا نرى."
إنهم يعتقدون أن هناك اتفاقًا. هناك اتفاق بشأن هرمز، وسيكون هناك اتفاق بشأن النووي.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86770" target="_blank">📅 01:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86769">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxaPl_y1RLFyVld5OUPtDv8ZUTDPOVB97T_skLHdFZz0-ylPX3icsaCXx_smv69-9DLQlX6EX4GBZOqoM38K_5Csi6ka5DEpl5f0zFLKJNisaEFXjMjnsCJKVpx7m5QI9T_EipMJ9NU-Hxr6kCU0jEJdaPr2t2VKR_h0JrtE7beW_QwyhhhhvLE_P2KNrM7aJ7TCmoe77-1_WW8gGXg3rUhYeBIEUnZHyxBfGOQ8uDFp2ko8Rzf8tR0XZlCi-gXZHks5vXJfwXP3iUvkwNVWk4ZSd3T_IA1qUNGKQs3swsIcF0kjCHRKdTCZXarhG4nhlPtP5GFrWqABFvAS8Pe4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ناقلة نفط تحاول المرور عبر المسار الجنوبي لمضيق هرمز، بعد أن أوقفت تشغيل نظام التعرف الآلي (AIS)، وسط أنباء عن إطلاق نيران تحذيرية تجاهها من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86769" target="_blank">📅 01:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86768">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإمام الشهيد السيد علي الخامنئي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8bf70aa9c.mp4?token=V1ua9mEv3ZPRLI4Rp_j0heZWzpPy9MeJkVaa_85QfUS5vUGW0k2y8wi_Zol1oF33w8qzJKtJkD4IIPbeYRxwLNpY6AqJ0roecCTLbyNxcFjDE-OEB69Z455K8LoqxR6usuZkddvcU_IeqLahEFHTqTD6JGOSureV6WyctUDtbE3OksRKLs6uRamrb9MqKUrOmK8l8sEGCJ5VJgEApNZDkmCTyncKQVRK7Kw2xOU0FyJKXyoG1fA36yWKBHgAq07iRGrRl2ZkKN8tDFhaczGzrMk18vTzfklmBfRk1-NoO9tsuOYHK3apWh5KF_mEGtP-CwD4wJ5RaOavzfZjY9n5VX3I3hWfjzIYk2jWrjvQOqggQT2QRUv9G4xolrkVtPubFuZG6aagIuBXNn3yWwhF8tl9SadhSCS-5aROaOJvwxExgjv1OU-Lnz6CPyA_hx4xAB6CS8uaWVERj1vCtfHFjGcbhGCdPHJfkQgFEm8IbKtlZ8TpISsrKHGlM29L62RZMZp6tibbxnemhm2pxFJYdJrwVQAiJb_lZzUJ7tiyDrDAwiQBfVht2_a7t0NnlRhI1BtT1a9buJAfp1XF3eGD5Cru9sQ72FJhPq9IkapFUlZ_TTN6zFKS0J6Qd2c68N0zbYoWCLHeFSQIRmzRi-TyAs68OE1GMEr-blSuujdldNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8bf70aa9c.mp4?token=V1ua9mEv3ZPRLI4Rp_j0heZWzpPy9MeJkVaa_85QfUS5vUGW0k2y8wi_Zol1oF33w8qzJKtJkD4IIPbeYRxwLNpY6AqJ0roecCTLbyNxcFjDE-OEB69Z455K8LoqxR6usuZkddvcU_IeqLahEFHTqTD6JGOSureV6WyctUDtbE3OksRKLs6uRamrb9MqKUrOmK8l8sEGCJ5VJgEApNZDkmCTyncKQVRK7Kw2xOU0FyJKXyoG1fA36yWKBHgAq07iRGrRl2ZkKN8tDFhaczGzrMk18vTzfklmBfRk1-NoO9tsuOYHK3apWh5KF_mEGtP-CwD4wJ5RaOavzfZjY9n5VX3I3hWfjzIYk2jWrjvQOqggQT2QRUv9G4xolrkVtPubFuZG6aagIuBXNn3yWwhF8tl9SadhSCS-5aROaOJvwxExgjv1OU-Lnz6CPyA_hx4xAB6CS8uaWVERj1vCtfHFjGcbhGCdPHJfkQgFEm8IbKtlZ8TpISsrKHGlM29L62RZMZp6tibbxnemhm2pxFJYdJrwVQAiJb_lZzUJ7tiyDrDAwiQBfVht2_a7t0NnlRhI1BtT1a9buJAfp1XF3eGD5Cru9sQ72FJhPq9IkapFUlZ_TTN6zFKS0J6Qd2c68N0zbYoWCLHeFSQIRmzRi-TyAs68OE1GMEr-blSuujdldNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
|
«دار الذكر» على طريق الحسين
▫️
مشاهد مؤثرة من بناء رمزي لـ«رواق دار الذكر» ومرقد الإمام الشهيد السيد علي الخامنئي (قدس الله نفسه الزكية) في طريق الحسين
➕
t.me/Khamenei_arabi</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86768" target="_blank">📅 00:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86766">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
🇷🇺
🇺🇦
مصدر لنايا : ‏ طاقم السفينة الإيرانية التي تعرضت لهجوم أوكراني غادر عاد إلى طهران  ⁦</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/86766" target="_blank">📅 23:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86765">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الاعلام السعودي:
نيجيرفان بارزاني رئيس إقليم كردستان العراق سيلتقي الجولاني غدا في دمشق.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/86765" target="_blank">📅 22:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86764">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
ملايين الزائرين يتوافدون إلى حضرة الإمام الحسين (عليه السلام)، في مشهد إيماني مهيب يجسد عمق الولاء وإحياء الشعائر الحسينية.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/86764" target="_blank">📅 22:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86763">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇱
الاعلام العبري: غالبية المحادثات تدور حاليا حول مضيق هرمز ولا نعرف مصير بقية القضايا، هناك استفهام بشأن مخزون اليورانيوم بإيران وتعهدات إدارة ترمب بشأن سلوك طهران.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/86763" target="_blank">📅 21:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86758">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eO-oMn7jVMp8sLMq09DjQXET7sbk1Wu1JoMzr_62PyVRW7l0Ma3qZgHi0wJxnj8c7tUkyIJcLfVbKURoAyVAa1dhtuqpP1Hep1Chpx4RfGabbKWzlsRd4A5wFOWI8iwhEo4u6PzItSO_lpzdsUi3LFqXh84nNSOVppc4xyDrqOZc6IG_EhiLwteQ6H4Gqrepbxjb-Mt3y8yCOJj9oxgK-NeITOaY7xhOYCbFOoHeycNC1ojdCyr-IJclFG14-i6n-RI4oUmSuj12dM10Sl39T5hnWzVEiLaWmRbgk7xVbtQFMe61ZYsOPZwvMfldOGJPAT-LJiWBRnMl9OwtytCzqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNW8T0A75D2wH5P7UPT9Ii0hQXFHez--iXa79pvjk_nifAHemtE6AR3qZN1BEg7LBnRwlnp_GxO5VVBEOg8Q--lj_KEbM99Iq2Qm996VKaTTlwnGaypa1zRqGo7DLUvKWANX6PQSHw2M7h4L79fA3hFuhOLAt8679pfCLahxDEgSydbPCPtTbj96yXZymy7knKFm-EnfMp6cAm_x1umRbXvhgDw7IUigQgcZdHQnfwpon8KR19iesZevFL5bEAV2ckJ4_j4VOX-fm7oSFdjDuJsRFUaJm7n-RAnuHWTWr7pnx-mNUw_wDpPL0c95g4Eom2k4uMrqG-UVM7qYcFcROQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca1353aa31.mp4?token=en2Gna-6q1vKFCupthlZWwJwG_WMyoXynWfZSWXp1T-6TsCvNRzjwEFl2rq9313iSqHi8UAFN0YMXPRya8NjmLJx_kEqHoi8CnguEALo3r4HMTFe61wSc3fu4nPZ4fv-RGjly5YmpFZmZjs9_X-rtkSaHuLl1xlkTIEgE_TKTAu13l6qWpZf9HrjAl7jC4loW1CupgK_9f6RVM2q3LO-89a3fDU2zXBZZ4rhEdhYSC_gEaRJDhsTkpP-b5gpbWv-iRQtx3SB60Yv0gPebWOnPzhNZaC4PLMgVp7kXrJw4IIeh94M2RxZ9dNsXUFqLwwn97NCLXQ-3-2dikFTCiWViA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca1353aa31.mp4?token=en2Gna-6q1vKFCupthlZWwJwG_WMyoXynWfZSWXp1T-6TsCvNRzjwEFl2rq9313iSqHi8UAFN0YMXPRya8NjmLJx_kEqHoi8CnguEALo3r4HMTFe61wSc3fu4nPZ4fv-RGjly5YmpFZmZjs9_X-rtkSaHuLl1xlkTIEgE_TKTAu13l6qWpZf9HrjAl7jC4loW1CupgK_9f6RVM2q3LO-89a3fDU2zXBZZ4rhEdhYSC_gEaRJDhsTkpP-b5gpbWv-iRQtx3SB60Yv0gPebWOnPzhNZaC4PLMgVp7kXrJw4IIeh94M2RxZ9dNsXUFqLwwn97NCLXQ-3-2dikFTCiWViA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
🇸🇾
حكومة الجولاني وبموافقة السفارة البحرينية في دمشق، تمنع الزائرين الشيعة من البحرين من دخول سوريا لغرض أداء الزيارات الدينية.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/86758" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86757">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
غالبية المحادثات تدور حاليا حول مضيق هرمز ولا نعرف مصير بقية القضايا، هناك استفهام بشأن مخزون اليورانيوم بإيران وتعهدات إدارة ترمب بشأن سلوك طهران.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86757" target="_blank">📅 21:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86756">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇱
إعلام العدو:
‏حافظ آلاف من أفراد الجيش والدفاع الإسرائيليين على حالة تأهب قصوى خلال عطلة نهاية الأسبوع، عقب تحذيرات أمريكية من ضربة أمريكية وشيكة على البنية التحتية الإيرانية، قبل أن يُلغي الرئيس ترامب العملية في اللحظة الأخيرة. وانتقد مسؤولون أمنيون إسرائيليون بشدة هذا الإلغاء المفاجئ - وهو الثاني خلال أسبوع - مؤكدين أن القرارات الأمريكية غير المتوقعة تُقوّض بشدة التخطيط العملياتي والاستعداد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86756" target="_blank">📅 20:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86755">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇦
صفارات الإنذار تدوي في كييف.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/86755" target="_blank">📅 20:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86754">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
عراقجي
: المحادثات الإيرانية العمانية في طريقها إلى الانتهاء وتمر بمراحلها النهائية، وتلقينا اتصالات من بريطانيا وأوكرانيا وبلغاريا وأخبرونا أنهم لن يكونوا جزءا من الحرب علينا.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/86754" target="_blank">📅 20:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86753">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509947903f.mp4?token=nlMjB_V9wm-uYFsMmCeAP20T1tMacxFvd0w86AI1RJFEDv8W-KNHkQ8_hvnRwbmT6mBfHZ8s1FQzeNjlxoBNXorYsmLbNhD_1dtDzq3-S-FlHd73JxAt0qmdYcMmCrZT7HbpaLcuKC6Ce8ydwYfqU9vzflvCNrTZ2Gp470PDV1mbJuLqSek2u8Rpn3SsY-wK3IM57gLYI_jklArA5tNl3YK7mjUQIN_EwkAUI6_nlRIovoiP17KSoi9uhpmNS10FUneP743S3CG_FBJU5FYw4kUHOps6tF_Zfhl1zVvSE5Exh1LzY3g7emRWCZGj_nMZpny99CUZRUiCrnfpbWqaJa_VxLQHjBuCk7ohqcaz5HlUASwUdyR4lwXVBeFEIIGFejxDKJsLJWBoO1zAuC6jIIZCwxearzqafofPP7fMunbSETbcdfWXuy2rOCnSoFrqaMXRaTJU6iV677WUZRXF0_C0B1VaGf5wUqy_8ui4JyT7T5VgcK_H3rHVam-1QiViVGGwkiaYptXTC65bkhq6rwMHeFj2v_B4sG22wl-69RSpEVePmWO_uGxdhospsOTVQcORuyrVmBfM1n1o7cRzv7_VQef4n-0YEgxcGANecDT-_QOUqh1fnyRvML3jcMkh4Cc5KyYKH9ZP1tV3H-HGVj4_gInhDYpwogWyPsZeiWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509947903f.mp4?token=nlMjB_V9wm-uYFsMmCeAP20T1tMacxFvd0w86AI1RJFEDv8W-KNHkQ8_hvnRwbmT6mBfHZ8s1FQzeNjlxoBNXorYsmLbNhD_1dtDzq3-S-FlHd73JxAt0qmdYcMmCrZT7HbpaLcuKC6Ce8ydwYfqU9vzflvCNrTZ2Gp470PDV1mbJuLqSek2u8Rpn3SsY-wK3IM57gLYI_jklArA5tNl3YK7mjUQIN_EwkAUI6_nlRIovoiP17KSoi9uhpmNS10FUneP743S3CG_FBJU5FYw4kUHOps6tF_Zfhl1zVvSE5Exh1LzY3g7emRWCZGj_nMZpny99CUZRUiCrnfpbWqaJa_VxLQHjBuCk7ohqcaz5HlUASwUdyR4lwXVBeFEIIGFejxDKJsLJWBoO1zAuC6jIIZCwxearzqafofPP7fMunbSETbcdfWXuy2rOCnSoFrqaMXRaTJU6iV677WUZRXF0_C0B1VaGf5wUqy_8ui4JyT7T5VgcK_H3rHVam-1QiViVGGwkiaYptXTC65bkhq6rwMHeFj2v_B4sG22wl-69RSpEVePmWO_uGxdhospsOTVQcORuyrVmBfM1n1o7cRzv7_VQef4n-0YEgxcGANecDT-_QOUqh1fnyRvML3jcMkh4Cc5KyYKH9ZP1tV3H-HGVj4_gInhDYpwogWyPsZeiWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مباشر.. من حرم الإمام الحسين (عليه السلام) في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/86753" target="_blank">📅 19:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86752">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e92ab1e9.mp4?token=gU9T0Kt8PuoECP0SuKN04TFklU2SQhPGQP9VMVjOX49p4RoAauDTtKry2XgZKDlKgi852IaTO1nuu4YMdtcujf9q7E2X_UhCC9GwoJlShg1SmcAtOYHztGrzpmPHva7Kntx1wmPfYyiPvygX88ZW7jYMhORy_i8veofewPb8q9FZdGbBlz9xClExhslgnle14-9WeGbBFcdkDUrS98aXeRyTyVAckgzlV5RPrdDYmsEJlBp52yVazKHGBCU4k1OII6cd7niOvSJxepKu3vb2iEQXN6T0eiHwX5VmeTcNA6t-4eJ--Y5t9UMqqiNfbNaOdiLhRWiTZEjr96F2wk1YCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e92ab1e9.mp4?token=gU9T0Kt8PuoECP0SuKN04TFklU2SQhPGQP9VMVjOX49p4RoAauDTtKry2XgZKDlKgi852IaTO1nuu4YMdtcujf9q7E2X_UhCC9GwoJlShg1SmcAtOYHztGrzpmPHva7Kntx1wmPfYyiPvygX88ZW7jYMhORy_i8veofewPb8q9FZdGbBlz9xClExhslgnle14-9WeGbBFcdkDUrS98aXeRyTyVAckgzlV5RPrdDYmsEJlBp52yVazKHGBCU4k1OII6cd7niOvSJxepKu3vb2iEQXN6T0eiHwX5VmeTcNA6t-4eJ--Y5t9UMqqiNfbNaOdiLhRWiTZEjr96F2wk1YCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل اعداد كبيرة في باكستان بعد هجوم انتحاري استهدف متظاهرين</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/86752" target="_blank">📅 18:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86751">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84b98d1cf.mp4?token=t3X1PblR8lzHUAR4nQkTl9Gc168g0pNTaU-qaFNcEbKjlFprRW0n8DoaEJE34UrsN7vtWVod-aIZPnaeLw_r2_RcpAcdTHc24TyYRqa-fF-_VSU936jhXwysz0WKbcBdTSHlDZpVLxljn-bKMrz6Dsip7V-ho0tJQf2FnMhqoN5SVPa4lJaLPQtYorqgVEBNt6h_RAdvvn0YIYO8WWSF5dsX1PUAlFSmaTpE9G86WB65O5kE2xGnHtUNll90BIB8j-6-wusJhHFrjB92rQG_fZgU6ZKjlwoLqTHVPiY-7oWyX7Wp2iDhA-B-fFmL_elEfpQyG2SipxP-u2Ifx9HIQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84b98d1cf.mp4?token=t3X1PblR8lzHUAR4nQkTl9Gc168g0pNTaU-qaFNcEbKjlFprRW0n8DoaEJE34UrsN7vtWVod-aIZPnaeLw_r2_RcpAcdTHc24TyYRqa-fF-_VSU936jhXwysz0WKbcBdTSHlDZpVLxljn-bKMrz6Dsip7V-ho0tJQf2FnMhqoN5SVPa4lJaLPQtYorqgVEBNt6h_RAdvvn0YIYO8WWSF5dsX1PUAlFSmaTpE9G86WB65O5kE2xGnHtUNll90BIB8j-6-wusJhHFrjB92rQG_fZgU6ZKjlwoLqTHVPiY-7oWyX7Wp2iDhA-B-fFmL_elEfpQyG2SipxP-u2Ifx9HIQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل سبعة أشخاص في هجوم انتحاري خلال احتجاجات في شمال باكستان</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86751" target="_blank">📅 18:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86750">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مقتل سبعة أشخاص في هجوم انتحاري خلال احتجاجات في شمال باكستان</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/86750" target="_blank">📅 18:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86749">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R53890AeXxxyx-z2WcluDL360Ir1cztlRPIFT3LWnhT7-syvLRU4CwNFPTpxweSuZUZJUTuVjWH6lRkA6intx7RH84plJ3Ofnj7v4cH59EmPdrQi4D2AHFtOYKJqWp32NAf7d9BT8kfYgsefrVwrR0I7BCL4Lhgtjiu2KL4icy9qJeaahNbqc_W_0UtDguUXonhiB1piYkRHn6kbfuRKe-9JgsKbExIgyDUtd0LOcQcYUFzhnbF_4BT3mCESCcuzGzgpIlYYA5-jD4KDIitsSGUIcOyk21yG8EK5RVHc36DXT6OzadvtP6-hfC91McPsax81aXhWK5pbERKMpg0K5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يا لثارات الحسين وأبناء الحسين
نداءٌ لا يخبو، وعهدٌ يتجدَّد مع كلّ ذكرى..
في بغداد، ارتفعت جدارية الفردوس لـتعلن أن راية الحسين (ع) باقية، وأن أبناء الحسين ماضون على درب الحق، يستلهمون من كربلاء المقدسة معاني العزة والثبات والتضحية.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/86749" target="_blank">📅 18:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86748">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
🇪🇬
محكمة النقض المصرية تصادق على قرار يلزم الخطوط الجوية العراقية دفع مبلغ 787 مليون دولار أمريكي مع الفوائد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/86748" target="_blank">📅 18:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86747">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
وزارة الخارجية الأمريكية تجدد تحذيرها لرعاياها في أنحاء الشرق الأوسط وتدعوهم إلى توخي مزيد من الحذر.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86747" target="_blank">📅 17:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86746">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80400fcd3c.mp4?token=CgvJ-FMvQ80ERaegoTN4CmOJHdzgePdvptlqqSygEPHVbZdCPDkGTt5P6zv7kt_LZ3aXzMldN-DM85SAMUjH3IQPU47it7jBQRnGL7CC3GbSU156jTS8rRNtPGAJY5Fj7SNyVpmD6CaC9CxVJxtLkEmCkcQPgclR3yj7CYhnikyILLBBpPekX1HVfAKmBWGcJ6IB4rmY6IgdSEP461uzENq13mEB5dZA0_rM5zEMWaYsSrEogDsRumzlu8GzRAo3VXueVwAHQngoiFA6sl-9YSWRDX66Bv8S3qjSxOEM2WYugjomv1Dp5pjZ_DLZ2DcBPRFp-6klXsWVhxTPBv3wxaCCj8hwYYRqPJIGoljSMupV3b2twGoX3m53krIWFz5m8bXWuVaDj1D8kLl7firo_cSoc3PX0DICO4QiAI5tLgaYc0mxpxR16fsJyrE-azNGIbNWvGVMqCONvfeADVVktQdNwRiiVsthGtLAYYqpDGASOjmAWTQY7Sb43rzk2WtinZTcTfbtRriEpJ9PJPJfGSL8ksRe1pcMLHwRFXZH4ZNYy6nAK8Xsxs3e3QXK7jTTcZFDAy7OMgsFdXwHf_fVlNjz-uWquyvI-iRLRLqVuYUVQKCQTILFS4StVqEeu2uGDMbqx6XDF9ov5mDO4fI2PFBb7YdbOKPWgM2Rw38oBEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80400fcd3c.mp4?token=CgvJ-FMvQ80ERaegoTN4CmOJHdzgePdvptlqqSygEPHVbZdCPDkGTt5P6zv7kt_LZ3aXzMldN-DM85SAMUjH3IQPU47it7jBQRnGL7CC3GbSU156jTS8rRNtPGAJY5Fj7SNyVpmD6CaC9CxVJxtLkEmCkcQPgclR3yj7CYhnikyILLBBpPekX1HVfAKmBWGcJ6IB4rmY6IgdSEP461uzENq13mEB5dZA0_rM5zEMWaYsSrEogDsRumzlu8GzRAo3VXueVwAHQngoiFA6sl-9YSWRDX66Bv8S3qjSxOEM2WYugjomv1Dp5pjZ_DLZ2DcBPRFp-6klXsWVhxTPBv3wxaCCj8hwYYRqPJIGoljSMupV3b2twGoX3m53krIWFz5m8bXWuVaDj1D8kLl7firo_cSoc3PX0DICO4QiAI5tLgaYc0mxpxR16fsJyrE-azNGIbNWvGVMqCONvfeADVVktQdNwRiiVsthGtLAYYqpDGASOjmAWTQY7Sb43rzk2WtinZTcTfbtRriEpJ9PJPJfGSL8ksRe1pcMLHwRFXZH4ZNYy6nAK8Xsxs3e3QXK7jTTcZFDAy7OMgsFdXwHf_fVlNjz-uWquyvI-iRLRLqVuYUVQKCQTILFS4StVqEeu2uGDMbqx6XDF9ov5mDO4fI2PFBb7YdbOKPWgM2Rw38oBEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
فيديو صوره باكستانيين يظهر بحوزتهم جواز سفر بحريني بعد تجنيسهم من قبل عصابات ال خليفة في محاولة لتغيير ديموغرافية البلاد ذو الغالبية الشيعية.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/86746" target="_blank">📅 17:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86745">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9e362b8c.mp4?token=V3fbXHV0zJOMHpaTfp_ICGACzxrbRbSuywJrcGhAdVao_gRmJsBv5rcnEp7V6iNe6FSs4f8ZlqMufYNG1BQMwiqdKIMwmooZlKj2iSSTYDsboyaLlOLdtjKDjfF5_Oateex99oJ3Myuzr9pjI9UCVJCe1Ls1sycuSzJHRiWgCgze0DWuxCLmZnLdQO1wBCTcYdptIL2_GZi5IcQW0J_E_trsjSKLCrC6VRWhKVF-PSfGhLImnTTldmDs_5LZ_DsSpyfAtPFRv2L7nm0Ksmr6K2LGC0FnfCkg3vMXKWLXnN7tllVXb-nl1rolxN1FnjVunqDsAFW-PKL0paShZsEPpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9e362b8c.mp4?token=V3fbXHV0zJOMHpaTfp_ICGACzxrbRbSuywJrcGhAdVao_gRmJsBv5rcnEp7V6iNe6FSs4f8ZlqMufYNG1BQMwiqdKIMwmooZlKj2iSSTYDsboyaLlOLdtjKDjfF5_Oateex99oJ3Myuzr9pjI9UCVJCe1Ls1sycuSzJHRiWgCgze0DWuxCLmZnLdQO1wBCTcYdptIL2_GZi5IcQW0J_E_trsjSKLCrC6VRWhKVF-PSfGhLImnTTldmDs_5LZ_DsSpyfAtPFRv2L7nm0Ksmr6K2LGC0FnfCkg3vMXKWLXnN7tllVXb-nl1rolxN1FnjVunqDsAFW-PKL0paShZsEPpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
تحطم طائرتان إطفاء أثناء مكافحة حريق غابات في اليونان.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86745" target="_blank">📅 17:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86744">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات متواصلة داخل معسكر التاجي</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86744" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86743">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9cfee199.mp4?token=ugHUgS8zgXeJjQGu_WL8ai_983Gc2wIYKnC8YtfeJLJFYoFrNs8bFs6Xi5KCKobouO78nuoD7qO6LLr3dLOwLfkV-FeGY0VVTjGSTgEhYm34rZbxtsB6jyYjrbgpXeA39X_iF1lw_Pln7Y40gjOBby43BDPZz3shklVsAyr5teur-Yr6SCicyS5vzxiUo6Wh2l_gxzWCEE2b2IjQ7f9P1nYcnILXlezzPD0PnR7OAfM_tMmTQ4VcvV15LuqBGXpwwOask5TZi4pbRjnAJfHDWVf2XanK8xhMMxYAshYkR6r-VJB1uCx4HFagXCjTLwFC3xErwJJopmeRZMxbMTfTXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9cfee199.mp4?token=ugHUgS8zgXeJjQGu_WL8ai_983Gc2wIYKnC8YtfeJLJFYoFrNs8bFs6Xi5KCKobouO78nuoD7qO6LLr3dLOwLfkV-FeGY0VVTjGSTgEhYm34rZbxtsB6jyYjrbgpXeA39X_iF1lw_Pln7Y40gjOBby43BDPZz3shklVsAyr5teur-Yr6SCicyS5vzxiUo6Wh2l_gxzWCEE2b2IjQ7f9P1nYcnILXlezzPD0PnR7OAfM_tMmTQ4VcvV15LuqBGXpwwOask5TZi4pbRjnAJfHDWVf2XanK8xhMMxYAshYkR6r-VJB1uCx4HFagXCjTLwFC3xErwJJopmeRZMxbMTfTXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متواصلة في معسكر التاجي نتيجة حريق كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86743" target="_blank">📅 17:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86742">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اندلاع حريق مجهول ودوي انفجارات في معسكر التاجي بالعاصمة العراقية بغداد نتيجة انفجارات كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86742" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86741">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe13b00c74.mp4?token=saEp6v4zN5pEfMlypenxH7ra1t3kN9HsDUtKMASFlofz-NfTXHDLx1nOpPCjpigf_LEDjQbH3zxm-8EoiBC3QGViF4uGVcxOZzQtPwgwjVdV7CwqGyB8a2e_QgTxtVNYegYU7AZWlsxY0z8DfRRzjbBVEBx-n4mDkEsp71goUJ9q6A3zFPLpLPrZK7uSfppiDljkP7ZHF6cCCu0EVmHarcuHdronN7BdfEe-dXywXght6vv0euO41JcRTcI231_SHINszNRke1-U4_Cabk9sp_RGeojjPlPcr-uM4cEKmwL033Wj01oKTU40mseBvpazZoWFmliO6fiocF-tQnfdCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe13b00c74.mp4?token=saEp6v4zN5pEfMlypenxH7ra1t3kN9HsDUtKMASFlofz-NfTXHDLx1nOpPCjpigf_LEDjQbH3zxm-8EoiBC3QGViF4uGVcxOZzQtPwgwjVdV7CwqGyB8a2e_QgTxtVNYegYU7AZWlsxY0z8DfRRzjbBVEBx-n4mDkEsp71goUJ9q6A3zFPLpLPrZK7uSfppiDljkP7ZHF6cCCu0EVmHarcuHdronN7BdfEe-dXywXght6vv0euO41JcRTcI231_SHINszNRke1-U4_Cabk9sp_RGeojjPlPcr-uM4cEKmwL033Wj01oKTU40mseBvpazZoWFmliO6fiocF-tQnfdCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرق الدفاع المدني تتجه لمعسكر التاجي</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86741" target="_blank">📅 17:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86740">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5J0Mb8-_UhL75E4IoY1trIghJWLmJOpsfPg6XT4rlEGUrySVgCbQb3IrsIFfhZWsbT8Znk0zTbEAxGXW5sdunoN8Zz4CXftL_t7XnbRZY0EIrbqNPe6WdSqcRmtyHwronBECV0M1dXGhpsbJwvDtsUXVKy9UbT-1E3WhTxyN3eZ6ioXKbmyb83KG95DicA4r5gtUj2FuajGmvuHhkUtFCiQu9wYQ2TCRUxwcrkaBnvhWMgHxWXZRrlAsDHx5lt3gvbKimVraNjpPVdLrdk61dgnqJfnlSN0T6T1BrPsaNqeEkY207xols6Fv8v9EO2JsZFnb1sREtrAdk1q7hr4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندلاع حريق مجهول ودوي انفجارات في معسكر التاجي بالعاصمة العراقية بغداد نتيجة انفجارات كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86740" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86739">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8201fce1a8.mp4?token=d3em-usMKYwhBz5iV7HqA4TRKoWlYs-i2hgsH5w_XxcUma-hwBDOKk2G25JwQxDeg_C9JOFCd3oN0UQWxyisg3p1sXZ2-zwUH9i5SOBGrIeABrBRh_jksL9QZix_YdJiZUYoUROh7z1uBwPUVF7tGaLPV-vEcdzX3bSAKUkwhgkgKSWA8WKj3Aile8ds0OnUFn_OUJUYoyNZQpG6w1uCKS6Laot-xmRL4eo9GRmaGk8qcWeXgyPxuwVEXDviXRjsENg18hb48E0kgRP5eMT-B5-h3uUNnnwGUDr7n_eaYH6YRPYj9z4sYrpUqbeczyYi9tNPqGqhMIUnBBTHAP5Rzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8201fce1a8.mp4?token=d3em-usMKYwhBz5iV7HqA4TRKoWlYs-i2hgsH5w_XxcUma-hwBDOKk2G25JwQxDeg_C9JOFCd3oN0UQWxyisg3p1sXZ2-zwUH9i5SOBGrIeABrBRh_jksL9QZix_YdJiZUYoUROh7z1uBwPUVF7tGaLPV-vEcdzX3bSAKUkwhgkgKSWA8WKj3Aile8ds0OnUFn_OUJUYoyNZQpG6w1uCKS6Laot-xmRL4eo9GRmaGk8qcWeXgyPxuwVEXDviXRjsENg18hb48E0kgRP5eMT-B5-h3uUNnnwGUDr7n_eaYH6YRPYj9z4sYrpUqbeczyYi9tNPqGqhMIUnBBTHAP5Rzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق مجهول ودوي انفجارات في معسكر التاجي بالعاصمة العراقية بغداد نتيجة انفجارات كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86739" target="_blank">📅 16:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86738">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:
- إن الانتقام لدم الشهيد، قائد الثورة، والشهيد إسماعيل هنية، أمر حتمي، وأن الرد على هذه الجرائم الكبرى سيكون قاسيًا وحاسمًا
- مؤامرة نزع سلاح حماس لن تؤدي إلى أي نتيجة، وقد باءت بالفشل منذ الآن. إننا نوعد العالم بأن عزيمة المقاومة المناهضة للصهيونية راسخة، وبفضل الله، فإن الانتصار النهائي لفلسطين على المحتلين أقرب مما يتصور الأعداء.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86738" target="_blank">📅 16:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86737">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">علاسة 3D</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86737" target="_blank">📅 15:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86736">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مستشار الأمن القومي العراقي يقول انه تم الاتفاق على فتح مكتب لبعثة الناتو في بغداد</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/86736" target="_blank">📅 15:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86735">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682bf59f05.mp4?token=tQCVJOY0IeOrK6dsttT5RjHtKdrbuZwccXWXpGVly1yKK32WGTlFhzE5LVPt9DG_FIKT9Tg5zPFKDh8FQBOl78i1xvdVGF5WjW_SGjNsFAPxWkFECvFrfqYSV33LeeQ4t8X1a6sZPHelxit6-VRGjGUbxBvwfArLoxguqTqWMX3WtoEbrvpEzWgZLsDLkb6GhkmcB94eh2cEKhCioW4xwbTz8JokqU4uAOZjdJuQuWoImh4QCnEB08rV3QhDjvg_LdgQiqEU1UcDRPuSXQV7yAgUjFHPh-QvtJ5GQPxgOFaoGbQRBxLSjnzJeuQh7Tjk_92hPmdaY3AsB5tmabeROQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682bf59f05.mp4?token=tQCVJOY0IeOrK6dsttT5RjHtKdrbuZwccXWXpGVly1yKK32WGTlFhzE5LVPt9DG_FIKT9Tg5zPFKDh8FQBOl78i1xvdVGF5WjW_SGjNsFAPxWkFECvFrfqYSV33LeeQ4t8X1a6sZPHelxit6-VRGjGUbxBvwfArLoxguqTqWMX3WtoEbrvpEzWgZLsDLkb6GhkmcB94eh2cEKhCioW4xwbTz8JokqU4uAOZjdJuQuWoImh4QCnEB08rV3QhDjvg_LdgQiqEU1UcDRPuSXQV7yAgUjFHPh-QvtJ5GQPxgOFaoGbQRBxLSjnzJeuQh7Tjk_92hPmdaY3AsB5tmabeROQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السفارة الأمريكية في الكويت تتعهد بالدفاع عن الكويت سابقا والان وتنشر مقولة لجورج بوش الأب</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/86735" target="_blank">📅 15:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86734">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAVEF8_orepG_yo_KUSBZ8TWhYa2zt-10PVVYGQLnt6CwLempwL0AIBpu1bE8puprMUlcE1j1EJml2KajLdEckwwntR_UkTFjMRi9xyzyu8ui7FIrULzwe0HABaD2QyMd_Re5BNvjLoi8Nikbp8LOSHx8_i6tu5g6dVmXgVdl94qBhMDD103pWV4LGYWcObRz74UA85XST-mYD4I7Y2emQB2zKx37Mmby9L8CsNTfehfv6c3P48fBK9vZlaBIo6yysUkW45uTCwsDJQxHisqS2zdWbiJ6Ib-qu_mvgloQNIsfTApfcPxax3ZwEGMlkXpCn2z3CMbR3Cs5Idd9ru6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مراقبون لنايا:  بالتزامن مع التحشيدات الإيرانية قرب عبادان ؛ يناشدون العراق بفتح ممر بري للقوات الإيرانية باتجاه العبدلي ومنها إلى بقية مناطق الكويت تسهيلاً للمهمة لكن يجب الاتفاق بين الطرفين اي الجانب الإيراني على عدد من الشروط من بينها منح جزيرة بوبيان…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/86734" target="_blank">📅 15:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86733">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوي صافرات الإنذار في الأردن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/86733" target="_blank">📅 15:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86732">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8dLp_PiIbghalCkcUWik31kbio-tABPgf653cICWuprZGw5kwCsm_iRs7bmB5xRtuDU1GRs4b2PD7ERqTNAfHYjAKK3bDoahZ9aC2votjaUcNo7o8Z0yQn-eVHnZYff8LqeBhAXm2nw0a9VCrz9lMHG1DYIL_X4FkCnabiQ_nKeqkGlx7Pqwk6KNjCZCa53tH3zqbJMdqBs8HhlcbujhBjamPXfrfruzaEcbs_f3QQUmQS6_pFW1vme4FUcJyG5MJsI7sXLoaVzH1SQSp0g37q-c-nO23ds15f_Gc0O9kAwxduFZEqhXegcCMWzsZz7Wy4dnDrPgJB_S-A6Wu7xkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مراقبون لنايا
:
بالتزامن مع التحشيدات الإيرانية قرب عبادان ؛ يناشدون العراق بفتح ممر بري للقوات الإيرانية باتجاه العبدلي ومنها إلى بقية مناطق الكويت تسهيلاً للمهمة لكن يجب الاتفاق بين الطرفين اي الجانب الإيراني على عدد من الشروط من بينها منح جزيرة بوبيان للعراق وعدد من الحقول النفطية الكويتية ولتأخذ ايران باقي الكويت
‏ومن باب الإنسانية أيضا يقترح ان يتضمن الاتفاق مع الجانب الإيراني على عدم المساس بآل صباح في حال لم يتمكنوا من الهروب إلى السعودية بالسرعة الكافية وتسليمهم إلى العراق وإذا تقدموا بطلب لجوء سياسي للسلطات العراقية فيجب الموافقة عليه ليعودوا إلى منازلهم في البصرة معززين مكرمين .</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/86732" target="_blank">📅 15:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86731">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">منظمة أوبك:
سبع دول أعضاء اتفقت على خفض إنتاجها بمقدار 188 ألف برميل يوميًا.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86731" target="_blank">📅 14:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86730">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇩
اندلاع حريق في عبّارة ركاب قبالة سواحل إندونيسيا وقد تأكدت وفاة خمسة أشخاص على الأقل بينما لا يزال 41 آخرون في عداد المفقودين.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86730" target="_blank">📅 14:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86729">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
مصدر لنايا:
وزير الخارجية الايراني عباس عراقجي يصل النجف الاشرف يوم غد للمشاركة في اداء زيارة اربعينية سيد الشهداء (ع)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86729" target="_blank">📅 14:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86728">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
نبذة عن نظام حكم عائلة البرزاني في اربيل:
- اقالة محافظة اربيل اوميد خوشناو من منصبه بسبب تعليق صور نيجيرفان بارزاني في الأماكن العامة وتعيين هيمن قادر بدلاً منه
- أوميد خوشناو قام بنشر قصائد ومدائح في حق مسرور بارزاني لكي يعيده محافظا وبالفعل تم اعادته لمنصب المحافظ
- اليوم تم اقالة اوميد خوشناو ايضا وتم تكليف زانا خالد بديلا عنه في مشهد يعكس ان الصراع لم يبقى بين السليمانية واربيل فقط بل ان الصراع السياسي اصبح بين الاطراف الحاكمة في اربيل وداخل عائلة البرزاني نفسها.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86728" target="_blank">📅 13:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86727">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=B7jo6t9vJREKf59WdSiHZjpbTF3oM2aYUzcEOY2b2n1sDkZDIRvOvhMdzI992tlG5RW5e-MInJZ03eeyyH_TFXlT208JL6zwvIpJQqUJaA3EkFGjqI_SsCESzt3oRGIzvSvfXlnzRvLHC9olOEpp48Yju9uacO86ofuY0VgR8nbt0J8LADxJ0pYvbXLY6lCTCUXVfxY4Gxc9dWrs0dGWt80LUwDsK5UJEQlN1Hl2k-r7lNS3uh9PUkzLj90nIvQw0ssRlxcZ1TffVaodDKu8AeuGCZojAfUlfYvM4-Nw7ng_1h8OBIleH4RQ5rX_Bv9xnrWCQIt2P36Uol6xyGP1rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=B7jo6t9vJREKf59WdSiHZjpbTF3oM2aYUzcEOY2b2n1sDkZDIRvOvhMdzI992tlG5RW5e-MInJZ03eeyyH_TFXlT208JL6zwvIpJQqUJaA3EkFGjqI_SsCESzt3oRGIzvSvfXlnzRvLHC9olOEpp48Yju9uacO86ofuY0VgR8nbt0J8LADxJ0pYvbXLY6lCTCUXVfxY4Gxc9dWrs0dGWt80LUwDsK5UJEQlN1Hl2k-r7lNS3uh9PUkzLj90nIvQw0ssRlxcZ1TffVaodDKu8AeuGCZojAfUlfYvM4-Nw7ng_1h8OBIleH4RQ5rX_Bv9xnrWCQIt2P36Uol6xyGP1rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
مضيق هرمز لا يزال مغلقًا.. مضيق هرمز يشهد اليوم رياحًا قوية وتقلبات بحرية، لكن إرادة المقاتلين الإيرانيين راسخة وقوية، وهي المهيمنة على هذا الممر المائي.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86727" target="_blank">📅 13:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86726">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
حريق كبير يخرج عن السيطرة في مدينة سبوكان بولاية واشنطن الأمريكية، يتسبب بإنقطاع الكهرباء وسط عمليات إخلاء واسعة تجريها فرق الدفاع المدني بالمدينة.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/86726" target="_blank">📅 13:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86723">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sa6UjMd_cEZl54hB6p4tWDdl6FZJqfVEMJObgflyI69vh2MMXirXXGkNzGBi8DPWMg6-xseCPh2xnAsgsebeLbYco9MFqUiOOBf4D-bzqdfRL6Vyp48el78Sa-4fvYQaVC8U7x0V-keDmcCWvbyhnkeLEoSMNoaMONWaqKh8Kam6hUy1M2cXbpH4qbhTEuh3sfQvmjPzfMWFJrNwYzUoS2pDUBjn7WK-LnpPjsHLXZNw33liOFXRN5VOaSz0Cdjah9qG_ERrl4XWf22sqWFZEYWk_1au4pOr7-SRS0Azf_cGRQvKvPcQIMaYa-nRQb-ESDbUOx-oNzp1AlweWRA6FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TAa-R1eJCG5w4S9OniGeweXuEDr56LkqXVwoogWMMtvUqmXpb_0PEaEDTdoaEvEZutKPUiz65OxShDsDDlmQDh-pQhmIXkR2_vrcYdDZp1mhyXfp-EpEf5w99e_S2BQYGY2I8k60aIsPFBvtlVXeeNcG3mWDYNYRwHy6P7C1lvOl5PtcRbsi7Ji6ctiIHzCbwSk7IGdez0HuD_DTNFqXVZFx0blc40qttlhXzzChdKcw5odNnr43Prhz-j4iORqr7pc5zrrQNTwRej_sOZOmiC4uKRNuXpw3Xj_xhC_qelWXJq1hDVciZ6OTvvhbMwq9xnwSviaTL9Gz5fyPcUGotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-aGA2hri9VJkaiSj3FrPouoOT8xjWDIWtnqMvIkfkMQJIPtnUr28oYrRHhDAI_WJP8JHxCCkoQu8qtLpEpONKzQwpCdyai-448rhZf-BhMdVFhmK-DndRnCFNIMgaalLnDrJ29BIu-gmCdRq4Vvtp13oQTQnIVI64CLH4y_MqqBTPIdYQ8sSiLq1knhekBUv37DwDi5WUiJX9zdLkWeVrkSS4d1mSd8Dys9iulEXmBpI2ruvSRSjbWT0puDszx6ivXKt2VYvEQxOSJ1QHRn9qUK-c5r1IyKo6FGtb_EFqoV3KW7k9iifQ8cBAhSoav9TT4vM9wInwD_OApT7DIj0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هبوط اضطراري لرحلة الخطوط الجوية العراقية IA248 التي كانت متجهة من مطار كركوك الدولي إلى العاصمة التركية أنقرة لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86723" target="_blank">📅 13:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86722">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
مصدر مقرب من فريق التفاوض النووي الايراني لوكالة فارس:
لا يوجد أي اتفاق بشأن إعادة فتح مضيق هرمز، والأخبار التي تم نشرها حول هذا الموضوع كاذبة. طالما استمرت الإجراءات العدائية الأمريكية، سيظل مضيق هرمز مغلقًا، وستكون حركة السفن ممكنة فقط عبر المسار المعلن وبإذن من القوة البحرية التابعة لحرس الثورة.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/86722" target="_blank">📅 12:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86721">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇱
وزير المالية الصهيوني سموتريش يتحدث عن "اسرائيل الكبرى":
‏وعدنا الله بأرض إسرائيل بكامل امتدادها المذكور في الكتاب المقدس. ‏أرجو وأدعو الله بصدق أن تتحقق تلك الرؤية يوماً ما.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86721" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86720">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌟
شركة كابيتال:
اغلقتا أكثر من 300 حساب مصرفي لمنظمة ترامب بعد مراجعة داخلية لمكافحة غسل الأموال.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86720" target="_blank">📅 12:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86716">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇱
هيئة البث الصهيونية: حماس بدأت خلال الأيام الأخيرة توزيع بنادق على عناصرها في قطاع غزة تحت غطاء أسلحة شخصية، حيث أن الحركة ترفض التخلي عن سلاحها في الوقت الذي يتمسك به "مجلس السلام" بالتزام حماس بجميع بنود الاتفاق.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/86716" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86715">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4BeN-bcJozIkGhku7omCVz7VXlpdaZ40te2N-B46aMRJnazs5qXiyEJmviTi6hToimB7ZRDBor4mmIVE_thoi8Pu7xFFxjr_9OBCh0bCSLCR9PaQMfN0HwsuoKkSikYqkVE48whSyYuqwRyHzlimRPx4U4xZ4Auy4I_gsifR06T9beJmqciGNQobsgpbgy1h1ySXCORVtDsh6NIyggXVSlP8ymEeYgTVD6tLx6bMjIzmnKIjvEbsp8utKL8f7VqfqhUG1b1KvdrvuamJ_gEXPOpObYRtmRLnajIpDn4XfazCilNIn4d3Mwewiz4x-6qKxq_DGiJ796bEL2EgnCO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الإعلام الحكومي والنظام الكويتي يهاجم العراق بذكرى ما وصفه الغزو العراقي الغاشم ويطلق طابع ضد العراق ؛ علما ان ما يسمى الغزو كان على يد نظام صدام ولم يكن على يد الشعب العراقي وكان نتيجة سياسات الكويت التي دفعت صدام للهجوم على ايران ريثما انقلب بعدها صدام وطالبهم بدفع مبالغ مالية نتيجة دفاعهُ عليهم حسب تعبيره انذاك</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/86715" target="_blank">📅 11:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86713">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZowvYlxHrao4QL28LBSxKVyap36owNi0jeALUkZMn3LZG6tblZXWhB318gCZq0zEt-bR4veXxEREh2vROJHkBjmPF7o-pWpcP473X18OSnqEwOuNEyOf1CWxOG_VGnh4HLRU7QFCrnc1jwrvF_MH9YwsnGBTAiIs7v6zcL386KpUoyTRpH2Lh61k9pSwEddj-2Vv3xrded5yVLS6zlVpKkvuo5z9gv0Ofi5u0e4FBlpwUy2Ur7D5AxbzpQX5DkR18HS4QJZigkQWleQ-cvx6Ap5ulawyCyDsAVCJUtDVcbzLdRhlPMp7aYNaJ5fDvurjsYO3cmh67pNNTqoeT6_1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGPYSNHBSBlQ5pvlEc6HN8bXnnX8_XWLbkdOFdyw6rFOwch_NgTgeyT-3sst2VTxELEfvt5I5Rd336IZPt12JnFt_jFuard6R2tccd2QeR8u-SUOtG3GkyHhv00OZ1WJAH6KCGC_SlweXan1tcX4nG75roV-XlrBnsvjSLKhdHa2bBlBSyw_NWacA11R1w5dzol1DAVnjMHZcRZ0Mg9KEdzf8UFd_O7J8ijMbgFz8ww8amzkznaZgltp53e0XW7nvvKDOjGyyVlh2Vye8BPyfqCk2BwrwYDqrDvxT1mWlMyfnTMXFIakWMeeX5zpVtz27TCVHKJx1_CsAVU9tek7Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مصدر امني لنايا   انزال أمريكي بقاعدة عين الأسد ثم انتقلت القوة باتجاه صحراء النخيب غربي العراق</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86713" target="_blank">📅 10:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86712">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇱
جيش الاحتلال: الكشف عن مخالفة أمن ميداني خطيرة بين وحدات "الجيش" الإسرائيلي التي تعمل في لبنان</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86712" target="_blank">📅 10:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86711">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌟
تقارير بريطانية: مجموعة واسعة من التحالفات الدولية تشهد حالة من عدم الاستقرار - في أوروبا وآسيا والشرق الأوسط وأمريكا اللاتينية - بسبب دونالد ترامب.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86711" target="_blank">📅 10:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86710">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcTU58I4CgI22oBd8MjH4jrQVtfkTLpQr7yD6mAUVDtCTMtTzLNhrYjzobroahJf3sM7h3jWIC62HMALfQBjy16akQDC7GqrOuEJHhCnFoYapkl6MKPrUUJiQXUpu7rEfKiogj4fKhmaFa5H8PEBXxcMNLqxwA4pYX9gcnokWfPr2mn-ymy1IDHqYCNanTkghQcAJ1nSP1MXQn1qFx8khUHC_4L7B7v8p7BfDEq5gt3cuJY-QZJWbGyhSqeXkeoHF2KCu4VgvvIY3cgYYVkG7YvM0JvA7J1T-MRUoG4Ozx9RTDKAe-3YP0Pt3IdGbJISHh_zi2uwJ5_0nm_0utphZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇰🇼
طائرة نقل عسكرية أمريكية من طراز C-17 قادمة من البحر الأحمر وتتجه نحو قاعدة علي السالم الجوية في الكويت على مايبدو تحمل بديلاً عن الرادارات التي دمرتها الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/86710" target="_blank">📅 10:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86707">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7f-hR7UqwAE14IJexkLoAU3Vc4hBEoF_1EbEx3ZauGltfqIFGu3WbMJnXPAvPtwawzjjMgNeKkIlKT-T6HPetdcIX79GnuHqbvNLwb0Un_RVl13WsSCkOzUnJrZgumhgU795GxcmtgMcWoZcumj2oRNXELXw6sqFHmFpazuvHqni7ulKyQmg-kJcHKm42_jksoj4PeY1ziJdqG85lHJrso-XCn9WU-npeXAe4R43fWQwVcG4I5B_a_TV1PtKZGXkvqYf2OkC9sToB2BiQS3_CxkPlYveK9DPzoYWqPWEW_VOkHM0qoPvBSq9j9xBpUc6x-XuXxoxb7KulLBqbYjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyUj5cPE9bbzGMZvIXbLoX9KSlnnf1y-61adcrIUw8wFsVEv5UrqPNdwhsPTiVEA9LlVslOwmPaTW3aeRCiZZhMRI5nxGu5qqeJ8LiCa-8aPskLz9Us8etzdDJWX9Em1p2Vn9JPT7QBJuHaJMClGUeTtlAAz5bh4NzDV9q2z847zxFPjLzCcNIFt14LLPPhc81yzcK1qk1xkTqE2h-sVqYatea6-2uo0KuvKRgQnTAOxqNAobSeQfDiB2GceHqXBypfe1eU1FsjcRAiLfzwNsQGAwVaS0KCIg5PE_xK7MAOCw9BgionLHyV3wgM8kS1rh5I2udht_Et_TIkUt_2zqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RuJ52n80yLEs1q5gbfOMRQ_dftDCJnGG4CCNi712ijgNypwbAt9GXrdRF4PhIMNwkblmtiKJos8hFd_93TqCf4Z5Ob765EhcCQRH0bEr9qerVUAi1NmxfBjr6WhG7455d0B0FNZNarDaPO8mKSx9BablchmA8TIOGpbBrfcPVQo7tMH2dJnryeZ89u8mRSXcdteEhzYOyQozh08tPdrqkZdLLTz7nPO146Tx_G1bZakMTJFx7hiYSlnIR_F-sbBm3bG0JWgnfU3voJEqDFP088HwmwIMO_i6ZvlamQHfSnHPYhemf86kmq-OBLoaZcoH9pI3mj5rsJ9CLnW8nfssvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇷
حادث سير لحافلة تقل زائرين إيرانيين في محافظة واسط العراقية مما أدى إلى استشهاد عدد من الزوار الإيرانيين بالإضافة لاستشهاد عقيد ومنتسب في الجيش العراقي.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86707" target="_blank">📅 09:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86705">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MiUnGKrEqy6tCRPLvGgC29X7-PIyQt3dblBtzonCa6B6G3twVHyOCTbdJeiI6yoFZKPvFnm3-fSOJUqavfZLlrlwZk7uzzdMuwQabfpD0ptHumKOxSS91FAAPNEGwkH_3djgyfY6FVVih0LFta4x15iNlveekJkM1ZJaqfqXqXlupf2QpuVa_9-ENsOfJ0WUdfPbNUm5CgjcN2Iqj-5SsZeOugwDGdBv5CzumoqUDjHcRLTEx0D4CV5j6fy1vvZr6HyPNqKDaGC30ld_d7aYpmUzV5s0211j5RrXkqIhn5JmQwL2veIUMwv-J_nmsbG7Ko3KfvyjCO4iTW53Eutw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2UUFwbvTkXkNfl1lawCCh8sQAKWuy2Ij4teH51UK5OYg0oF2zc3j9DH8eoLgr4-0H-U5SbVJvtDdR2rTT8iycoYdtP2SuJa4FUgMvwpmcHcl6oYVeFhueu0cTNmfh6aFynaUg-6n0nJks9As_P4kczYt_kcvIApKHbmDbD12wqX4Yx6IKM5Mb4-txJQvstBnU457ReD5PwA4xncKfo0Ggid7Nc0OI2x8dd6GhIHbO6FrTUc-GAURuxOIoDV709gl6NBJMb9O5A9eGBBZOGf3In_GHx9NRMo7kGlXmxdfqJ4yburNStAQUJ4rMCemk0X7WyhbupGvgArjq_cS5tbxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
ناقلة الغاز الطبيعي المسال GasLog Shanghai تقوم بتغيير حالتها الملاحية إثر تعرضها لحادث استهداف بمقذوف في غرفة المحركات أدى إلى نشوب حريق وفقدان كامل للطاقة والدفع أثناء محاولتها الخروج من مضيق هرمز قبالة السواحل العمانية.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/86705" target="_blank">📅 08:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86704">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
وزارة العدل الأمريكية تفشل لالتزام بالموعد النهائي المحدد في 31 يوليو/تموز 2026، لتسليم الملفات غير المنقحة المتعلقة بمزرعة «زورو رانش» التابعة لجيفري إبستين.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/naya_foriraq/86704" target="_blank">📅 08:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86703">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlbwBrZEGhdAgzb70-KexsR4PG9BFGoDS7Fme7OJtNaNVF25qovoCQKAkR1yKWS8Yj8uN-tXtzS58MgDf97PSeMBIgrnClbEIVQAPJ18vzobWZc7z9q5AO_mEQwNMuFwh0mq1kPY3bo9pWSLImcWgmZ1mtpDmZ8geuQFqHfewlDZWztPvz2n-NMbl1YuE4aIuc9NB3MTMRHv-KW6ohTgHBg1eteu8gKqJWiAtZ7PePpaSKjMMaTD0NCA5gTtdlWKC14i1qQJdx0LBfgPXHjgl1vu7aciB6NxlcDCPLXbCtpnsLL4ZRvAgfVeM8F7miB5zVeD2O87Lt8snJdbbzX7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
خوفاً من الرد الإيراني.. ترامب:
‏"الولايات المتحدة الأمريكية على أهبة الاستعداد لمواجهة الجمهورية الإسلامية الإيرانية، بمستويات من الإرهاب العسكري والقوة لم نشهدها منذ الحرب العالمية الثانية. ومع ذلك، فقد طُلب منا مؤخرًا من قبل إيران ودول أخرى في الشرق الأوسط، تأجيل أي هجوم، وذلك بعد الاتفاق على بنود اتفاق. ويشمل هذا الاتفاق الفتح الفوري والكامل لمضيق هرمز، وإنهاء التهديد النووي الإيراني. وبناءً على هذا الطلب، وافقتُ، من أجل مصلحة العالم في المستقبل، وكذلك من أجل بقاء إيران مزدهرة وناجحة، على إلغاء الهجوم، شريطة التوصل إلى اتفاق سريع. وتشاركني دولة إسرائيل في هذا الالتزام. فلنبدأ العمل جميعًا، ولننجز هذا الأمر. شكرًا لاهتمامكم بهذا الموضوع!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/naya_foriraq/86703" target="_blank">📅 05:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86702">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي "مارك روبيو":
إيران لا تزال تمتلك صواريخ ومسيرات لكنها فقدت مظلتها الدفاعية التقليدية.
لإجبار إيران على تغيير سلوكها التوسعي يجب رفع كلفة سياساتها إلى مستوى لا تستطيع تحمله.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/naya_foriraq/86702" target="_blank">📅 04:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86700">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c9209c534.mp4?token=uYF3Bc1AMFUnmMN0SfM720_Vz1Alc5OtDXafniIwDbJNnhm7BuucpDll7FZmbLLrSsool3xmNlDtfSJKD7002BUbfd-CUWIYaV2MZkOvJ0hqqiwb9EG26Bn5dhB7Ee7qgnTHOhHuLo4kdktexIkEqYkF_mOiaTqBgKNaY_7wpqf5zhGLPqxHZzIbNyBcivekEJeadcxfbybNyzFsu6rrmm8QJSobn6sftpil3tEyu1muH8_CSnsvBh-VHJRheIfGOCQcpKpICsmoUPwl-sRVWwGkO3vkhz1Puz2lohMHXeF-4TY7r8II8Jm7tUc6POM0eMgSHOo4Y9TDy4mGzcxqNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c9209c534.mp4?token=uYF3Bc1AMFUnmMN0SfM720_Vz1Alc5OtDXafniIwDbJNnhm7BuucpDll7FZmbLLrSsool3xmNlDtfSJKD7002BUbfd-CUWIYaV2MZkOvJ0hqqiwb9EG26Bn5dhB7Ee7qgnTHOhHuLo4kdktexIkEqYkF_mOiaTqBgKNaY_7wpqf5zhGLPqxHZzIbNyBcivekEJeadcxfbybNyzFsu6rrmm8QJSobn6sftpil3tEyu1muH8_CSnsvBh-VHJRheIfGOCQcpKpICsmoUPwl-sRVWwGkO3vkhz1Puz2lohMHXeF-4TY7r8II8Jm7tUc6POM0eMgSHOo4Y9TDy4mGzcxqNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
حريق كبير يخرج عن السيطرة في مدينة سبوكان بولاية واشنطن الأمريكية، يتسبب بإنقطاع الكهرباء وسط عمليات إخلاء واسعة تجريها فرق الدفاع المدني بالمدينة.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/naya_foriraq/86700" target="_blank">📅 04:14 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
