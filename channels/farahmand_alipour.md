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
<img src="https://cdn4.telesco.pe/file/h5YAyUuFU2gx8IEElS0qQZl0qEaMdMFt6_mUa9vv7GGhLHHLqRLcWjT5sfMT2hHxIEWYmGFCmPLOul3M8dPn1rmR4kT0UPNVvx7nuvpP4gQ0vnmLLhIscnLiNQm2gjAHeV1Ys0lnpjQS2SBHsKxW_74pj9PP6AO605ePml__bJOKxJV8E45XtAkRfOB65Y1jTL7sM4B_Pyf0mC4CV4NHc8guXpdVXbLXsiUZdrQQd-JYNNP937I76RoMlJmnAFv-RHX6_VyU6GZSXj0FuJaYQXfj1uMcnMGf467Cm5W9RdPlgqHzAEkvPAYLs-YJuxxRkcj1Sq8cMetnuNh3whq-og.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 20:58:30</div>
<hr>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2jXUzua6hqCme7db5HWAsnQpa4fSpg6wrDhaMKcv0NSw4IfhepNxyKTR0VKuswg2bQm6dqIjVuWN9vNMt0tgWoPIa25z3eVX6rx2F3xzLI7YBDjS0ptFM-mAAh0BpkiJpKMZbV61VDsyz92q8qIC6B0UO_5t8MCXWIqH1DYyIsTDXJOLPHRjxQ3t0_qiYmeKCsCn042cC5BM8gBNyDkY1fI9-m1wRB5jeeHkW5p_UyX-OZoRn_nJCNYDrU9ipt_p0JJU8YQy4f3-nH3fXsDN1TNa7RAx8m8XwTzMaqfcLyiSkCEwIgTc9013Shnsp8H96M3EeWlGfE6pzyBze7HHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS5S9d764T9zFk6An4H5s1vCscROBLJiiwGNHZ3PKoNqthjA7EcQ0OEiwVRGC45CrT-B9nfORTMt-zTaBzRuhnwOSAi0N573j2jYXeYHfJjSPJ5MurKlKB607h538uhofhuzsdPrUsKIlOTR0h4fj-UV8LHj-AeaqFVtOq_ia2nYNQcxCdd28v3yIazw3z2Ih453pO2vA11hfz3ufIZ5FU6CWS0lJ0KH_i4U9toPEpr0xUMzz277_Mxdqcxk98bl4rlWjbku7LR-QPbnDZS5NoNMqnOKmnzjRLZ_pskoTfEzF_YClS8gjtIL2KssvvaMGtx2l3EZqqsPISxlkzr3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti8Uz9ARcybXL0HKjBVxmxbf7kS8YOBH18zWqzQl7OOmnOhajooddGtQiqH5K8rmIy_W97Svteux9Rgheqgg7hEYWTVtNyK-aP2yiQ8MbPIvIBcbuMSgDtO5RjsKzznju3mQOAMDeu6lJ-q11twyKlwsSla6sd7d0g37yzLmiXQsLvvJLJHRQbyyY7uw17pNKrSLA0yXcDi7YaUQf5kk-pOD0ZMHSFFcqCpvN0ag4_TPhyaukyIzoS-Xs3Bc9GjKl6Uilf-1C20uhnyx3gXxUEQXXSIkN7RVTOpb4fWwBgTgf99yCp-8LCuhRwHj0aPDT8xSiL5GSZAZmUtBYUsi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vbxhInx35vFu0JMUt4IUIzodAnxhF2MWmPAajg0GqW42xgmayS-ES3ciwQciSScDKBPeZFrztt3UDKqLS4G5ogCQCgrogz7aiCa_bUfFRUQWTmozTXpJAkJQt9rxTQI1UcZFS5thU5vH3jfOU31hsLugPfoiQurzgD6tO6NceMChq2UXNE2gXjaFs5z3yyC3u9m88Sb7ArSjM4qsAobICnkdei4nyLRon7vT_ArqseVTk5joxKLOPxtu4XZ0E908EerRYowcMjguzhWOFq_BxKoo6C3e8D3HX4WLx4hfHygV0--Qmk4_gcAsxL5DfuqtVVVWHnV5_gD2t6fRHmNo1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vbxhInx35vFu0JMUt4IUIzodAnxhF2MWmPAajg0GqW42xgmayS-ES3ciwQciSScDKBPeZFrztt3UDKqLS4G5ogCQCgrogz7aiCa_bUfFRUQWTmozTXpJAkJQt9rxTQI1UcZFS5thU5vH3jfOU31hsLugPfoiQurzgD6tO6NceMChq2UXNE2gXjaFs5z3yyC3u9m88Sb7ArSjM4qsAobICnkdei4nyLRon7vT_ArqseVTk5joxKLOPxtu4XZ0E908EerRYowcMjguzhWOFq_BxKoo6C3e8D3HX4WLx4hfHygV0--Qmk4_gcAsxL5DfuqtVVVWHnV5_gD2t6fRHmNo1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TahEAJjyzkLcwG_A_tgJ_nSwAK0ogmhz3o9DzS74uyJDrht38vN9GU_I5wKvhtsC40k-B0xio9OiadKyIbtP_hqkpsRf1qAbJ3Fw9vAZlWrHnRqGmXy-2ypZ12THdwfQmHSgg7MeFDYZXwYyZUBvf_0xAzx0trY_6H_6uMUpD0fc2FE-stvKNQzHzbF6GgkGcZ4rgq9gGABscl_9jH-QDsLGeNoTLhcH-ldhbsof49sFIdldqw3IiHGIqeMHIqx3b0t6dnpxCJxow5VxovrFfnbUOgQx2rTOJNDs4gVnBc6mgTxygOM6RnjA9YbjMyDJUcmhnCN_LNHnJFCDSd5Qg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TahEAJjyzkLcwG_A_tgJ_nSwAK0ogmhz3o9DzS74uyJDrht38vN9GU_I5wKvhtsC40k-B0xio9OiadKyIbtP_hqkpsRf1qAbJ3Fw9vAZlWrHnRqGmXy-2ypZ12THdwfQmHSgg7MeFDYZXwYyZUBvf_0xAzx0trY_6H_6uMUpD0fc2FE-stvKNQzHzbF6GgkGcZ4rgq9gGABscl_9jH-QDsLGeNoTLhcH-ldhbsof49sFIdldqw3IiHGIqeMHIqx3b0t6dnpxCJxow5VxovrFfnbUOgQx2rTOJNDs4gVnBc6mgTxygOM6RnjA9YbjMyDJUcmhnCN_LNHnJFCDSd5Qg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvztdfVtj9TfByy9vnraHfetouPFFNNQ7M1mSDFN9PsWO9nZmlU-_SU8KSxxzWOvPJHFb9l3sbbzS1vOSYIS3ERYaR0gD4S8VlFBsU5z9VWH5YogCVTsFkKTLwDMXex_hVBP94EaZS5S8t_BkPSsIBS2CuSeRjk6voR6QnHTVTUe7JJ1tMvzQA_5dQqFWLNmo56zzFTsip_AS_jJ9RjDKnC9quVXkR5i-O1-k4lk6-ygBaaN91OuFicUO3JTAWIGPEFKGYKcs0vP-xKBYgkD6PWK1S87hPAUgTzbNRRV0tAwOoDFadfm3ZGhVBKrTMOnUaBvbdap64KhpVAPcxwlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=akq5WJp14bhlbIiyUSA1FdCVD6vLGnKvXUQtfdXoKKLSJ0ORsOyG-WUHMzi_d6STDOaTVEYxGGPHUx7jplmxKv8oz2APedwqgKaDxqd5w-pV0Kiv9fm80VT9q-rjklPYzii_nEJwhLIusJj70JLQHTEgUPfHakT7ZeTE04ShNDq8pM4LwT8gWOKTtOhcHMr7mGxphV3dutlKCp9ZayrFrQyOW7gCWmZOk2cSZ7D2n3Z9kskpsyHjOmxxtixWE4R1pPio4kDkfdggw5_3pXRemzK-ZaiSJDf0mWAohyLHOWK-6eLpp4uYE3SdU-SUhNZ34mpWIeljHCA49kc3iyNaSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=akq5WJp14bhlbIiyUSA1FdCVD6vLGnKvXUQtfdXoKKLSJ0ORsOyG-WUHMzi_d6STDOaTVEYxGGPHUx7jplmxKv8oz2APedwqgKaDxqd5w-pV0Kiv9fm80VT9q-rjklPYzii_nEJwhLIusJj70JLQHTEgUPfHakT7ZeTE04ShNDq8pM4LwT8gWOKTtOhcHMr7mGxphV3dutlKCp9ZayrFrQyOW7gCWmZOk2cSZ7D2n3Z9kskpsyHjOmxxtixWE4R1pPio4kDkfdggw5_3pXRemzK-ZaiSJDf0mWAohyLHOWK-6eLpp4uYE3SdU-SUhNZ34mpWIeljHCA49kc3iyNaSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qDIoFiL5DR8OV0FJLUDttEVA81pgYbLyE5zz61AG9sa-fAuGXTvXKxMaHPv62F1HP-uOhqwqqbZ91dLsQ3zw5tmPzJbTHccNcLg4JPROZ3mtBaHyVO66oWKjSjiQ4tTklGOjLprq1f72VCw0n90FJNGJAd6PoSVuL6cV2goDHkj4yETKD5cZ0rhYHWhfMs7VaOuTBKqL3B4bjVzEYq6Te_qWazU3SdvMqnnQhPwWYiGXcyEQKw33mZF4IDuj8Hj1gI0STka32kOYr9FIi-N3WfDatdjYWH4i2ps5OuxH4CulE7QVIs0KHF_W8lyw7wfVWuEVJxEEHbKgeZEPjOY2cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qDIoFiL5DR8OV0FJLUDttEVA81pgYbLyE5zz61AG9sa-fAuGXTvXKxMaHPv62F1HP-uOhqwqqbZ91dLsQ3zw5tmPzJbTHccNcLg4JPROZ3mtBaHyVO66oWKjSjiQ4tTklGOjLprq1f72VCw0n90FJNGJAd6PoSVuL6cV2goDHkj4yETKD5cZ0rhYHWhfMs7VaOuTBKqL3B4bjVzEYq6Te_qWazU3SdvMqnnQhPwWYiGXcyEQKw33mZF4IDuj8Hj1gI0STka32kOYr9FIi-N3WfDatdjYWH4i2ps5OuxH4CulE7QVIs0KHF_W8lyw7wfVWuEVJxEEHbKgeZEPjOY2cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YoA_jkol-01mjn0tXCS0NIBGUESMY858Ks4TjKmXysUaNUQ4NY5DoYZq89DW4Ju4XckW5d-eSPIHckGSlLZvok47mpkbmz03rBF23VulaysoRIC7LYgpg9O8U-Eb7Vo_wU1sp4NENVO81MHPx7dMUMcDNsziWpRy600htyci2PbNbyTNU_jAVw0ortEm6I5iLLgwKKfomdbGnYYrl4nZAbpIwlyqMbAajxGYKEpCfLvM-JzF2r71TEYo4B-a_Pbq01xeSvh991Qg9zzhvkf-lTMseZM4KV_4CAuvrxdTuu1u-CYnVoTOWcCySjJ_JqLW5uFI3fvOQkA-O992h6UXDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YoA_jkol-01mjn0tXCS0NIBGUESMY858Ks4TjKmXysUaNUQ4NY5DoYZq89DW4Ju4XckW5d-eSPIHckGSlLZvok47mpkbmz03rBF23VulaysoRIC7LYgpg9O8U-Eb7Vo_wU1sp4NENVO81MHPx7dMUMcDNsziWpRy600htyci2PbNbyTNU_jAVw0ortEm6I5iLLgwKKfomdbGnYYrl4nZAbpIwlyqMbAajxGYKEpCfLvM-JzF2r71TEYo4B-a_Pbq01xeSvh991Qg9zzhvkf-lTMseZM4KV_4CAuvrxdTuu1u-CYnVoTOWcCySjJ_JqLW5uFI3fvOQkA-O992h6UXDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LndJz2xo-eldmWGJk3dOkz9uOpTn1b6vjxJ6LW1mpZqHGcRwPDi_4OevapX855JLg5aCyPdqBcQA2Dt7ZvHwR3CGBV1ek4YkN24pOQgDft0Jn6ubCtAAelrzqQiJnEb6bzNwIWqYz2Uzxaqa_U1vsyhyAInHpGKbFdzaBSu805kmPWyr1St6dYWU-QHcdGT3oIau-ts55w6kO3tMsGkpkXs8bNc_NoozG-vAg2oaALDag1EKPrlTZSEpEnS6tGNKc_OB2sUtPoniTsBH7QjDMKNWAkedZ6Cg6rWTzAOJotOhBqZ2QCOToKUE2C60D4xOqiyr9109ui8HTCK4qLAaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tTZzMplzaWAoi6Dbiifgg9cv5SryPq3XiuVsjrPVdxWZ0cfxb2vVu4pfqUmfJelmgV8b6-t484nCwJtA8w6rjMVauABA4Xar52lID1jQrSAnzBKbgo04RlJxKRDRbtWQDBMCICCV6SSBk3IR_O1RpIlussrMn7ggyCzEYhrdPGJMTzuNxjzdRhkTQqi5E3HiHgvpQkVHQshT4eSLhEPL5pnofhh54GtMDBLIlX_1IGLIGThnvj7PQ0yvsGo8ImwmUGzdOozUmv5L3hAJWJjc9xjamogbnPBqHscfMKfHAzFN4b22JiOGHIya2zzMvsudSu1wIVEBUPmJpAG-YoaTZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tTZzMplzaWAoi6Dbiifgg9cv5SryPq3XiuVsjrPVdxWZ0cfxb2vVu4pfqUmfJelmgV8b6-t484nCwJtA8w6rjMVauABA4Xar52lID1jQrSAnzBKbgo04RlJxKRDRbtWQDBMCICCV6SSBk3IR_O1RpIlussrMn7ggyCzEYhrdPGJMTzuNxjzdRhkTQqi5E3HiHgvpQkVHQshT4eSLhEPL5pnofhh54GtMDBLIlX_1IGLIGThnvj7PQ0yvsGo8ImwmUGzdOozUmv5L3hAJWJjc9xjamogbnPBqHscfMKfHAzFN4b22JiOGHIya2zzMvsudSu1wIVEBUPmJpAG-YoaTZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iER6FA9e7nxY9M8TSdTlwo6h89qYM33Pu2lej9RROyZFpcfKBQaJid322sv359nmrQk2kTS3aKgUbOl9bZ5Jl2o3g29F26nBaFK64A4iwOU9yU7zItl1yEDyttjcpQdjrjMPy0e8n1sI1XHS63ok_XgKQXn0c2AUXbziOQsnAx-6X8Cl_SPoTrRGEPFnxwrOaxMn4JI8_LvvZ2aohf72RqZQ59WThVorvEo0dbWl2M13g5WUDyODI9cEZ9n6wRF3u3yZ4X4lDcU8remAu08Biy6lfvoGTdni_JhnH_UifP_lOCq36ngnuUlF7KnhPx9kxaL93qtb7owDnhSYMYYrZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iER6FA9e7nxY9M8TSdTlwo6h89qYM33Pu2lej9RROyZFpcfKBQaJid322sv359nmrQk2kTS3aKgUbOl9bZ5Jl2o3g29F26nBaFK64A4iwOU9yU7zItl1yEDyttjcpQdjrjMPy0e8n1sI1XHS63ok_XgKQXn0c2AUXbziOQsnAx-6X8Cl_SPoTrRGEPFnxwrOaxMn4JI8_LvvZ2aohf72RqZQ59WThVorvEo0dbWl2M13g5WUDyODI9cEZ9n6wRF3u3yZ4X4lDcU8remAu08Biy6lfvoGTdni_JhnH_UifP_lOCq36ngnuUlF7KnhPx9kxaL93qtb7owDnhSYMYYrZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDXw-HneTrVY13TWizkwwQCPnxfNLijJ9VZBQQ52pNJEH7VP6qElnQ_pSDSRg2LioXDYWilzz4j-IAmd6OynxWrKSRTY3HRSJCGOrbLSDzsNzOMA0eF1slXshz393FMUVxzSaVTjKKudv1jquYJ6CBw4XraauJSDtUxh2NUSDrNPRnLmG2ZjvY8xmFYoK42qNnghqC1eZpx6ls58s4z439av52eHt_vZpXPYgtAppvq4oNcY65ZBkYFDNIjr9fdHdeoGRLIxPA-r_ft7avQdmFUEZiGZZExGSOmqEslL4V-updz3YK-pN7OYgjqHcQzSAFeNkw_z2Q4G8GXtw31oHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=MW8nk1iiOKI5oRJSTf0sRhgfCozVkHxqjg2gTJx7i0PgcuaJ7V7MP8EjvGxFQAqAmGFjw2SgKgB2UQkSffNMVAmS07IFR-nnx96XKHfk9E2Tna_EFd_tejJUH3pN-3wIH3JLRpvoc2mp6eBi2DD2BfT0Q5wiNkkSA7T-ib3ebK9jrH8Ebj03RKY3MCVfJfOTR_ue6EJlXnaby4DeTcB5A2Y5sUMu9oN4fW8BeGsJuGKYb5NJ95WPYTYdYRMXToP2--DFmyBIp0NrfJcAqmYcnVFcO1CX-xDEL9VDVKFD3NHFkX3rgN5Am89iC83u0tHqHuELtmXPoClBu_eN2EYR-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=MW8nk1iiOKI5oRJSTf0sRhgfCozVkHxqjg2gTJx7i0PgcuaJ7V7MP8EjvGxFQAqAmGFjw2SgKgB2UQkSffNMVAmS07IFR-nnx96XKHfk9E2Tna_EFd_tejJUH3pN-3wIH3JLRpvoc2mp6eBi2DD2BfT0Q5wiNkkSA7T-ib3ebK9jrH8Ebj03RKY3MCVfJfOTR_ue6EJlXnaby4DeTcB5A2Y5sUMu9oN4fW8BeGsJuGKYb5NJ95WPYTYdYRMXToP2--DFmyBIp0NrfJcAqmYcnVFcO1CX-xDEL9VDVKFD3NHFkX3rgN5Am89iC83u0tHqHuELtmXPoClBu_eN2EYR-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=rdL6ppGwPeb3aAWCi4MiZNYK8-ng1ZLxwVJnVqDthO1zj7Xex9LDCWsEc8tD7Iw-hH_-vptLEqAuEhQiIRZ6DWkKSAmbvG8YsRp7zo85AmNA08q7XJVN02_H-II1STX4SD8TMaS-mt8mGt-YoIXKsIZQIiwtg-o9olAR70bsdWFVAFe-Mc-3v72sXjukuX6C0dSUAbNP-lCA5y5eeNgR2KV7_UP96rADcwqQ5E3OPc1CY_PZP_aquSTzEXeSQ2Zke4CNzTW-6AOj8_0FbwVuV9f9MIwuLkbjxQbsuSwO6-W-UkFTUwx6Dro-XsLRIH_7cOzCkrhKxQ5GoY3rZLnOnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=rdL6ppGwPeb3aAWCi4MiZNYK8-ng1ZLxwVJnVqDthO1zj7Xex9LDCWsEc8tD7Iw-hH_-vptLEqAuEhQiIRZ6DWkKSAmbvG8YsRp7zo85AmNA08q7XJVN02_H-II1STX4SD8TMaS-mt8mGt-YoIXKsIZQIiwtg-o9olAR70bsdWFVAFe-Mc-3v72sXjukuX6C0dSUAbNP-lCA5y5eeNgR2KV7_UP96rADcwqQ5E3OPc1CY_PZP_aquSTzEXeSQ2Zke4CNzTW-6AOj8_0FbwVuV9f9MIwuLkbjxQbsuSwO6-W-UkFTUwx6Dro-XsLRIH_7cOzCkrhKxQ5GoY3rZLnOnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=M8pbLuGWj1sWXtuBRxEU5qbVhSkGLBhx9MOmVVINzuAl96bz_wj14fNs8j8gWzRaIo2obMXzz7stmmu9UYRO1FV33M66yZyHx4KFmhRSDX7vrRF2uQBe1OeWUIlp6PmKaBocmlHB2PTdX1HMViZnmNGOpj6fbZKH8_uRnijN7milQoyZo_V4PWF2daVIcexylgzgcmX7B33h91p5s_YM69SsjoU-V9uBgdn1-u_n_F41fIKEyF7MNExDKE8lj9qgV88-RZaAM7zfPs6BILoAeaCvCh3yRkpu1Y4jVoIMdgMrhm85Nv-J94mJrCGTXqGQivNrAcUfmYVv4vQslTEqGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=M8pbLuGWj1sWXtuBRxEU5qbVhSkGLBhx9MOmVVINzuAl96bz_wj14fNs8j8gWzRaIo2obMXzz7stmmu9UYRO1FV33M66yZyHx4KFmhRSDX7vrRF2uQBe1OeWUIlp6PmKaBocmlHB2PTdX1HMViZnmNGOpj6fbZKH8_uRnijN7milQoyZo_V4PWF2daVIcexylgzgcmX7B33h91p5s_YM69SsjoU-V9uBgdn1-u_n_F41fIKEyF7MNExDKE8lj9qgV88-RZaAM7zfPs6BILoAeaCvCh3yRkpu1Y4jVoIMdgMrhm85Nv-J94mJrCGTXqGQivNrAcUfmYVv4vQslTEqGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H81s6wwb0MJCNcjVby8C3kyf0_k5h3I-TxYN_wKIyta_IPsoRF9Kiezhaa8BnLz2_DXtOXwy7jyCEQ9sPA1GxE71WIzSA4ILQxtMdjvrB_-hAgumM1OlmowtEFGcbXKtQnwqp29CoP76DElWh-k5JE3q87MXZ5S4VnLrC6qOP-KJVnuDZhUxfjyPosx8ARB_9poxf6lv2qHlsOQtYb9XZVdNFw5p9-SOba0MwKI0r4V1h5UeCOIbL2vKTfPfKV27vPxvU_rdMJ9EJ2Da89S6rH9UA9HChiBu3Kx_GJ4mab2pWISPoLUUxRJqsAvNCKnQ6wXK4OCapesvfb7U6qcyYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQq6KDNRPf1wKdrHQ2EImtpbN50fDB3fg0eoDyWaxR127RolxAjyJIOIBnry00ATnuZlM08b1JJC-Unb-N93p5hOwelGGiN8oggoqbuhIpR3HWT6YgnfXj0jpig_T6lyDxZ9MJhzhTVWcDBLjLRJdnjiLhbUk6N0EnxzdmXzl68NSSgvKV5JjJofkMXZhiRJW6dWJGbWMjVqS9lIGsh2J1avT3IWE_wQddGHtoCepVbexxTfxLWwe01q8LOw3BLHZJqWMvIRwrjmWNqlTXZjzklSng_lZKcpijw64D48Gux58HkC6_onyJbx5trpHTl3fP831LGPtl0q9fRF8i4s6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZgFm2LP7YuGkFaFmdSk8w480ffQN80nEfArhdu-9HJRXWQWWGNu5MOr5Nx8JJ5zkIutOQASz3haat5y0R8pp42-aMs1dfmytx7KwerIxmbtjXD0VnSdcAbF2d1dQNitlN03AyZbUB8mRiqZ-UVFZ4cBRZaaoopZMGnLrcscsh1lqnuoODSr_tLhUq-xiw9puuZTKodnix_g_nwvQmFizH0BeXMRdKssm2RisX0fO1cg1ANDkNIlXCtgORreogFcFeyB8Z9Pfi-d_tXal-9rDl4QzcPWyE-WMlznumuqHL_bC0AEWHuY0DVs7adjzIg4znxN6gjCfxhJ3KoKbRbDB6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=noCgkSxJjKlvrARwjc4hiN6A9g_IsOoAcb4Zg9fqK57dN-NBXVT0mB5ENwTiktyUVdeBDFyAzdOOp8jRrcgFErdyDhaJQTQsBBfwLJnGcWfuDwJJNgdXieRBLpwhbvjmr7nhjlBGQyAqOVmSFyi_7S8zNo5Bybk60OC1KSB1CFg-ppIVmtF9jbCOyZifiLBXMzV4MSZ-qhlV6nQEVm4-mBOfJJEeQXx1rEg_EmjanP8hqp_f5okRuGe8YlvxRSuPAOii-3pXwOxFY1FY7wCoR64hOdyXFu2xReAa3DZ4rzw6yo_cDaWRUjRVWH215JCwz60KWlOgLtW2GQRWO_P32g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=noCgkSxJjKlvrARwjc4hiN6A9g_IsOoAcb4Zg9fqK57dN-NBXVT0mB5ENwTiktyUVdeBDFyAzdOOp8jRrcgFErdyDhaJQTQsBBfwLJnGcWfuDwJJNgdXieRBLpwhbvjmr7nhjlBGQyAqOVmSFyi_7S8zNo5Bybk60OC1KSB1CFg-ppIVmtF9jbCOyZifiLBXMzV4MSZ-qhlV6nQEVm4-mBOfJJEeQXx1rEg_EmjanP8hqp_f5okRuGe8YlvxRSuPAOii-3pXwOxFY1FY7wCoR64hOdyXFu2xReAa3DZ4rzw6yo_cDaWRUjRVWH215JCwz60KWlOgLtW2GQRWO_P32g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaXg9zZP7jfG4Y-WIsv2e0TPZLTf_HeCEWHVKWJJO7T4BQt6tVAdNKkfJU1LvMTGUzRwWmNkTTEDdbEhX7zwDsAEDBZDfNTw0wx1UiqUmDCIqkH8TBUA5erCndrTj6rncwk2gz76bXABEtRicQAWqBUbfB-pZb67_WQrz_Agxbs17ORofN7p4j46b_sIBTu1Gfn8Pk6Bfz9kvZ3GprWLFpFHOTyD-4I7z4Z29jDcSwe6dVc88gjmRZL5IWLOF9nJ9IiMA5qp4E5dee0K3Ygh3kTtajinEja4S6-VW01R3qSfYXCWVGWlSYenMrQ1e1uWGXehS-9mVToCZtLMyk3s-4TE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaXg9zZP7jfG4Y-WIsv2e0TPZLTf_HeCEWHVKWJJO7T4BQt6tVAdNKkfJU1LvMTGUzRwWmNkTTEDdbEhX7zwDsAEDBZDfNTw0wx1UiqUmDCIqkH8TBUA5erCndrTj6rncwk2gz76bXABEtRicQAWqBUbfB-pZb67_WQrz_Agxbs17ORofN7p4j46b_sIBTu1Gfn8Pk6Bfz9kvZ3GprWLFpFHOTyD-4I7z4Z29jDcSwe6dVc88gjmRZL5IWLOF9nJ9IiMA5qp4E5dee0K3Ygh3kTtajinEja4S6-VW01R3qSfYXCWVGWlSYenMrQ1e1uWGXehS-9mVToCZtLMyk3s-4TE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=iwkZy0UbgJWxTbv75cW475kTKjQOzfbYLzyyezfFUsy1PP9dN0QY7pw5GP7F2L20ZqBLiQdWz851EahVhF9Dc-fijvCGxs130_kH5fDSC_Md9CG-QrAQfSuchJAsum5Vf4ueFoaHUaErg09zrhGBMHYtAUukLciEm_uTUCpdMvYBnhBNCpSOq6dJD7HDdTfPCFoageSsBZQqZy0sI9nNhBvRsvjz3j9ftQVVcVepELOIA2pbq7uT_ickES0QsPKeuCxuhkzNYjAnxPZgOMeajdEEpSlpT0vPm30z_SAHPkKuT0BF66nMlc-BBqdFLNnXH8jAXdTxsRrc7X4ctnAkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=iwkZy0UbgJWxTbv75cW475kTKjQOzfbYLzyyezfFUsy1PP9dN0QY7pw5GP7F2L20ZqBLiQdWz851EahVhF9Dc-fijvCGxs130_kH5fDSC_Md9CG-QrAQfSuchJAsum5Vf4ueFoaHUaErg09zrhGBMHYtAUukLciEm_uTUCpdMvYBnhBNCpSOq6dJD7HDdTfPCFoageSsBZQqZy0sI9nNhBvRsvjz3j9ftQVVcVepELOIA2pbq7uT_ickES0QsPKeuCxuhkzNYjAnxPZgOMeajdEEpSlpT0vPm30z_SAHPkKuT0BF66nMlc-BBqdFLNnXH8jAXdTxsRrc7X4ctnAkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOq8lX38J-M8Vj4pPofONIQn3wLht1rZJ0G9_pywbnzC69OWwZ_ydV5w7Q90YKMK3jR7rI62Oy80-0SHK28mLfPIt1gTdSC8Xf1mJO8CrwQcPJ_kN_oM13NITZKcuq3vTh3z0zy7bcpKYUBWDCbbWwaWBCz7Tb3jkkjqiaiDfXcc0rRCg0n-14lLx6o9cPKzW70dUj0dGWPjIMl2a6jl6DKaaXc8jdW7nx6FlaPHzqrJ7HfAq59VoPwNt7b16UFr1ZkyzqccbWmHwF5jtCKoHF0mNuCFRbbi82UDuRW5DOGWV6myMDwqH7chklSy3KPnzeJaNVHHnyK1x5q1C1vLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTpQkmYCkHaVfytSx57ZxIMhLoqHemelw8td1u8cRegoJmY7hvZosyPubelufWaGWStyR_sYcniuCISn8db6NHvAYCWGVK0dvA1eLL1NB68NorJvDK3s1FRI1oyB3A6valzr8oZMHV0rKgkPNikutZYHmFqDQ_uTFOyXt1mN9QqD96hYlVaytlEriu1vrmZB6rfWYpGk2A1YX1x9HWK8i94qro_IwNicHiPd9T5Vgc3VDY-SS4kGUKQ2BKdR_oDIDizk-_PYBzEOgbLFq0fmMAr9bQgRAudWurMpHRLaa9tYabsO-QTX6TqFt1lu_llO144a_gGkdF_A4balJc6hJ66E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTpQkmYCkHaVfytSx57ZxIMhLoqHemelw8td1u8cRegoJmY7hvZosyPubelufWaGWStyR_sYcniuCISn8db6NHvAYCWGVK0dvA1eLL1NB68NorJvDK3s1FRI1oyB3A6valzr8oZMHV0rKgkPNikutZYHmFqDQ_uTFOyXt1mN9QqD96hYlVaytlEriu1vrmZB6rfWYpGk2A1YX1x9HWK8i94qro_IwNicHiPd9T5Vgc3VDY-SS4kGUKQ2BKdR_oDIDizk-_PYBzEOgbLFq0fmMAr9bQgRAudWurMpHRLaa9tYabsO-QTX6TqFt1lu_llO144a_gGkdF_A4balJc6hJ66E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a70TshJ3J9Z08tmgktIgZEwiAvNwYfo8xWtxenR3-y1saRM1-oDCS-8CUpqu7uta7niv6qqIKZ0P6mLwWCrILAXdLM41SmYI_0jphm2QrgFzFEJHnZVrYSN76eccLgrqsxhy77mYJkSnEGPkbWAFCOGnWrc5iUTbBV0oUGgSZ0F_hX1qCbNcpJJnn9BdGBYKmurfwDwLSuDJL_ozO3SLf4ccrWL5E06hFhMPqwo-dl0skQ5bnm2QH0UuFJLQQATx-7rAiOz4cS1DRQSz-fnEifTqquanZLeVNab8pp0myFa9CTh3Xs5kZIb_72hjrCHMCsOOJfzz12VeUdmUjILTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=EH_7ucJxCtZU0UphVz-xQhXOFI-Aj1cW5GWqCAe3Jaozrv-uGw1-TtmsR5b7YQLO0CtxYCoA9gg9vM4XoMqImCahw9Jw416agc50VOIKHhUDZMP3TF60XqNWULS2dBE7jo8YwX8xIb_COHuJDdfRStZLU675AOGAx1bmQwtE0StTUubg0NaGYhjvjxXZYjIz-sIMVhnDZKK3SUwz9G7mjYh8gkXwpi27Q3ilSPK-4139yq4YrwulimvmDahjTeXgrVbF_nuaVj6BmfCVgyiSw8rryISyOUqd70AuIN4wZfB7Ay_m4_j_RBTt4iLwfIx22jQUDngI12Di-GpI-9g3mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=EH_7ucJxCtZU0UphVz-xQhXOFI-Aj1cW5GWqCAe3Jaozrv-uGw1-TtmsR5b7YQLO0CtxYCoA9gg9vM4XoMqImCahw9Jw416agc50VOIKHhUDZMP3TF60XqNWULS2dBE7jo8YwX8xIb_COHuJDdfRStZLU675AOGAx1bmQwtE0StTUubg0NaGYhjvjxXZYjIz-sIMVhnDZKK3SUwz9G7mjYh8gkXwpi27Q3ilSPK-4139yq4YrwulimvmDahjTeXgrVbF_nuaVj6BmfCVgyiSw8rryISyOUqd70AuIN4wZfB7Ay_m4_j_RBTt4iLwfIx22jQUDngI12Di-GpI-9g3mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=oJ42PO-iORvkPU9bBIQAmIjDbVF6ZkDrBHMgSdJbYRWbYsZJHDqpY98tj9jNYH7kn3_54cC4CWM3ezc8XETFAMfjFTk6QUTNQ5E4fQbvAj-8vb4nafD9keXCsh82cjZPBB45oIXADx0chiFHghgnzSLTQLwMj4wIR6rrRjilOiWQhh4N7NrTbUJ7puWFVLQ5jteRaI_n3fcrFVrpqISYBBJuLEx-4d-fR4xm9nBebTuDAMvxa__-CIAuFOZB2ASfWuCPFSUYra_d9Q02YAWJwPb-C7J72TpgEeA4Dtm8bP9K-c-fPrP_JtgubC2iQGi8lIuLQmdXld-duYEbDb4Rkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=oJ42PO-iORvkPU9bBIQAmIjDbVF6ZkDrBHMgSdJbYRWbYsZJHDqpY98tj9jNYH7kn3_54cC4CWM3ezc8XETFAMfjFTk6QUTNQ5E4fQbvAj-8vb4nafD9keXCsh82cjZPBB45oIXADx0chiFHghgnzSLTQLwMj4wIR6rrRjilOiWQhh4N7NrTbUJ7puWFVLQ5jteRaI_n3fcrFVrpqISYBBJuLEx-4d-fR4xm9nBebTuDAMvxa__-CIAuFOZB2ASfWuCPFSUYra_d9Q02YAWJwPb-C7J72TpgEeA4Dtm8bP9K-c-fPrP_JtgubC2iQGi8lIuLQmdXld-duYEbDb4Rkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=T8903qwHqNqMPyIN4psl2YR_Svby9-gISoSnchN9z9oTEEOFObbKFXUMyqMAr9uY5hoocObI6w1Tynqyo95dxvPcIRcgW_VFn8jSeSXUZTyrWxEmxdNvzo-Y4Y2A9rox94vL0kMLuAF6vRkgCluMszoM-Sz3gqhi-Wy2AfpQT7lxPot2MRlYKCQ8sSP0cgfOA1V9c--skmth0DlO_Ls9x4efT7zouRGKkfQTHv0zkUoBvzdSmLuSPCr_F973O00wb_KgrmIui9wenClEQDUnn8KmGkQ5xE85cUTWga_dAnQtnjgoymvTzw4RsP6OKpKZoMkTinK9u4k63a_6_2fSCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=T8903qwHqNqMPyIN4psl2YR_Svby9-gISoSnchN9z9oTEEOFObbKFXUMyqMAr9uY5hoocObI6w1Tynqyo95dxvPcIRcgW_VFn8jSeSXUZTyrWxEmxdNvzo-Y4Y2A9rox94vL0kMLuAF6vRkgCluMszoM-Sz3gqhi-Wy2AfpQT7lxPot2MRlYKCQ8sSP0cgfOA1V9c--skmth0DlO_Ls9x4efT7zouRGKkfQTHv0zkUoBvzdSmLuSPCr_F973O00wb_KgrmIui9wenClEQDUnn8KmGkQ5xE85cUTWga_dAnQtnjgoymvTzw4RsP6OKpKZoMkTinK9u4k63a_6_2fSCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KI4DwKvsdJCUy9cbFpJJH9vbdsOJaRah6oThB4eqc7vGhK6PWuDPRyjat46KCZgdlQsRO6RznVLdAHUIlJU9VuBzyS5TEW8Z96utsh8GDQyoLtMeIICAsUQO1-xlqBHgjNgsU2FmJRwVA4bXZGmhHSnrU0PRoTvWpUKXfv1j0AR2nHGqnkds9LBbim3oOcMeLo8jesjikQE03760MtUP1NEpzIIGimPLo4hjsS3PCE7ccmaDoYpOURFWJyuhu0zNtqiCdyY-cHVVE5UW-beVUUEV9eiEZgxzvm8mU98A_o9f0-XnaX5_z7E11V-5JEO1mnCL2d-ZdjxJ_cSkhw1PYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyBVGnzNvhuIXtPs9Mn0Ga0dUH1WmvDN52jnZlWV2tMdcWwiJ8OdTszXzTUCDCaz-tvfPV6YMccOCAIwgfn3MqmY-0AAmAVl5toSlwuplK8_pS-AGCx5HLF8hqu3ugCVaayMUF7AjYfqvhk0pcRXWufkuGp7YC8UlSFOFHlLgpt2ZzSottt6D_RvqzDzyNU8xB-xpqc6BUW-njajYOjOoxkPJ1aMexqYoKpo_vgjkmfhX8lky7KTvOye3ah8UXvdEmanCk7IrEbKth_RfbIVSjGJg0DxIXCpSC1Poe_pFQqdA3JSj0VuIkDUk7dqfUsAqSfZXFPP9Y_7dmQk4W0Deg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=T10kTYy6S4bi2Oik47GXKPexQxOy7VuRjSL0w3O-5Tl7FDvju-gVY7-yVlZhDUKF5fmSYNl1NBEUrIGLEqffHi6w2i5Y9bHNLdUYiZh9jeIaFSp-ORza2KY7UcIOJM4fwoZ7OpeTzPgo00aSDtAZ3-MjcVTEwxLlRQA9rmykbwcjXkrcppiZXh7wvbF-QiUeV4kGApLJ87gF1ehXan8QR70pkzFxbk-D44LS6-VwjFXWQc0fYFxv84QluVW7_E5SELYrcKjOp6VJtcJ_EbNV0mjjm9Rb-_ZZgLXrmvcRb-nWiP_9m_EyZhJniYHu1YNyrDamn17FZjrJD1q48tlaTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=T10kTYy6S4bi2Oik47GXKPexQxOy7VuRjSL0w3O-5Tl7FDvju-gVY7-yVlZhDUKF5fmSYNl1NBEUrIGLEqffHi6w2i5Y9bHNLdUYiZh9jeIaFSp-ORza2KY7UcIOJM4fwoZ7OpeTzPgo00aSDtAZ3-MjcVTEwxLlRQA9rmykbwcjXkrcppiZXh7wvbF-QiUeV4kGApLJ87gF1ehXan8QR70pkzFxbk-D44LS6-VwjFXWQc0fYFxv84QluVW7_E5SELYrcKjOp6VJtcJ_EbNV0mjjm9Rb-_ZZgLXrmvcRb-nWiP_9m_EyZhJniYHu1YNyrDamn17FZjrJD1q48tlaTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOv2YGTyWgZRPp3qGQTcg7miHDBFsNkgEOxLdt-H7AUCaN0Qj03uvxXKkM1ObBSMVyAe3KKtkEFXBBwpFhwP8ypD8Q_672KMSEoDge3_ixpF3Cl44-078vxqlW26H-xnrlnUw4XoKMmTNpY0fW7WobFEJ_qaOl6moWLtUxl-oD9oUlp1meO9h5pLk3ZPiwpwsteSPfz2JIMTFeCnyrWOay8-LD-5fP2DPDtLJ-G-NCAS4f1IL7Lz03u1fNlhxM0RP7j8vcTpOQ9Qm_oQRjm4mTRV1rt5yC8UmWbJCLJm-DXaVIn6qjJblLs2wAN-tPO6bFuhQ_jW7E2HK7DBaMPy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoOdp2wjkPYL8CaGzr5TslZsi-Q9Rpq-YHsMO0ZPr5o5L2QeZIppb5jw6OyzK7Vox9trUM5avb0pfevSuu1A3vQwrHSnVVmc9hgifuPqV075OjbPGtjGNur5MAaBh-z9ImYcnrhkpp8mm6t9hpfuk9HT3TlEAQmUwggtWT4oeOHjEHSH1HuUKC2a0R1LqwGhMulHfn42N8K5XT7JQ-TcgYw-4rXnFBTKdSWCPD5lzzOtbMNAQhaVZFi5diSha69az5CE_cfmLpVIyrmKDHfCYWH0cTHS-Cj0-Iefv7KGwo-TBM3lGIC1MqIWnpuL4HnZnh3GOfR4iG6F1fpta_SZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=DEqJRho7ED05Gdyit8PD-TmHS62ET0aftfM_0CQOXs_L-UnyXWrpPln0tmo36sIPzkOBy6fWkBFKTuDV-c4RQ7NCa6k4_7Zv7cLxc2nkz3IvR9zwcFNyTBRCCOE3RsK3r4c5MKeDZh1M7OQW2p685JX0AZkc3olxOFZQrhy2o5klFatRpN6f3n8K8ZL_earCKRdiggY3_NySNHjMP-mvipPN9W8-0iQFnUOn2F0dSpKjGfBF3HR5mUcn_6VGusx9Ngpf86IByNUOi_tSd41BfjnvXZDM2boZwKDPaoH60626eCbGbIvFe3uHR0CRCBc8D3LOVztQxTd95fPmru6FMUWBGGcI_tfpoZ5QAI9cCKEAAi3fiNtYsZAJyWQSHbPZGmM_o_vAa7BfM07CkW5PJKT3vWHU5-eJAd2B3efltDbHlVBMSRE1A_r88RGPDAF4b7803etLQB_x3XuoPt9DwJl1MeCZKKXtV6Opv0iejaXZAbhFzmt0UJxa-BRscZmuSKZ1SZJbsKsrRgVHZt4ZnqbG6FoCY9dPusIdBnoUsfB9f5_dyjunteNoew0eyLbFK6PiRYU2VpcFf9CJ3whuLRMwcN-h_Fi3WNiZ1r8bh6sjsjGeXnuik_yjv47R2ywnZK0NYRsEsb4neB4er5cJ3wTBPaP0MRRqOPsMepx0ygI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=DEqJRho7ED05Gdyit8PD-TmHS62ET0aftfM_0CQOXs_L-UnyXWrpPln0tmo36sIPzkOBy6fWkBFKTuDV-c4RQ7NCa6k4_7Zv7cLxc2nkz3IvR9zwcFNyTBRCCOE3RsK3r4c5MKeDZh1M7OQW2p685JX0AZkc3olxOFZQrhy2o5klFatRpN6f3n8K8ZL_earCKRdiggY3_NySNHjMP-mvipPN9W8-0iQFnUOn2F0dSpKjGfBF3HR5mUcn_6VGusx9Ngpf86IByNUOi_tSd41BfjnvXZDM2boZwKDPaoH60626eCbGbIvFe3uHR0CRCBc8D3LOVztQxTd95fPmru6FMUWBGGcI_tfpoZ5QAI9cCKEAAi3fiNtYsZAJyWQSHbPZGmM_o_vAa7BfM07CkW5PJKT3vWHU5-eJAd2B3efltDbHlVBMSRE1A_r88RGPDAF4b7803etLQB_x3XuoPt9DwJl1MeCZKKXtV6Opv0iejaXZAbhFzmt0UJxa-BRscZmuSKZ1SZJbsKsrRgVHZt4ZnqbG6FoCY9dPusIdBnoUsfB9f5_dyjunteNoew0eyLbFK6PiRYU2VpcFf9CJ3whuLRMwcN-h_Fi3WNiZ1r8bh6sjsjGeXnuik_yjv47R2ywnZK0NYRsEsb4neB4er5cJ3wTBPaP0MRRqOPsMepx0ygI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETrloI5IybpbAK_zlPudpSw9NMfT5AUtl7QaJIegtCV-Xy-6WKwoGfuVh0jKiQzV8fKHt2ykVW3NmvfvodrPJ4TJz9UXiTBu5YnZJYB2iq1fxSs1IYO9xtS20CVBB7iW66RXHgimm1VLxYyyznz0koX5GLFLK-T-OtYhu9x0dekEb-N-d7TsHTjPrtf2ZhKr3zOtH7U36feoyPoEUh0tsrBkygR7rOtVo7Yogjq8wm6itzfXdYWfVZzfnVuGSNhkMdMExmlsDMcLn8jQndpes3UAwrd7QIhpffsGM07HFmAiU-XV2LQzN5rGVvmwu9cbz_ae89VXJqA3_WiJwq2QXxgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETrloI5IybpbAK_zlPudpSw9NMfT5AUtl7QaJIegtCV-Xy-6WKwoGfuVh0jKiQzV8fKHt2ykVW3NmvfvodrPJ4TJz9UXiTBu5YnZJYB2iq1fxSs1IYO9xtS20CVBB7iW66RXHgimm1VLxYyyznz0koX5GLFLK-T-OtYhu9x0dekEb-N-d7TsHTjPrtf2ZhKr3zOtH7U36feoyPoEUh0tsrBkygR7rOtVo7Yogjq8wm6itzfXdYWfVZzfnVuGSNhkMdMExmlsDMcLn8jQndpes3UAwrd7QIhpffsGM07HFmAiU-XV2LQzN5rGVvmwu9cbz_ae89VXJqA3_WiJwq2QXxgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=oQ9r7iuNWeJlHvjzTuXMoW2ZSwZHRigmzKZ_qFMG7wrX31a670S2ncrBSBMxN2AzKkjyx-uZfDwtIrG8-FcrWHhy5c9hvED8Fgi0gsT18r3mffCIACEK3Gjfln-I1UeXGnHcBzunHuzMIMuIEqZiCqMHgNXik14mjUHl9C6uuz4-dJ85-Qyl12xZmGan5-R7cuEosYEgc-4DO46WTw4aDShECCTABJyTcJd5Thl47RJ77akm4jv_-6nHRPE8YTmC1stl6s7BxJTTwDseAZAC8wlH8kJTWYvlCGzDgfapufytFsd6UKo9OXBl1s0enJu1lg20XU-xRtv3JJOHUcqh_Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=oQ9r7iuNWeJlHvjzTuXMoW2ZSwZHRigmzKZ_qFMG7wrX31a670S2ncrBSBMxN2AzKkjyx-uZfDwtIrG8-FcrWHhy5c9hvED8Fgi0gsT18r3mffCIACEK3Gjfln-I1UeXGnHcBzunHuzMIMuIEqZiCqMHgNXik14mjUHl9C6uuz4-dJ85-Qyl12xZmGan5-R7cuEosYEgc-4DO46WTw4aDShECCTABJyTcJd5Thl47RJ77akm4jv_-6nHRPE8YTmC1stl6s7BxJTTwDseAZAC8wlH8kJTWYvlCGzDgfapufytFsd6UKo9OXBl1s0enJu1lg20XU-xRtv3JJOHUcqh_Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=MjiRFjYkyqdSYGylO2k3q8k70HfKgHeeWvJlhu3_wS4phVXprcOsnCIIMh0qxUgxP8a_GTVtwim2OhuNvmYtDXOLf8_9A6k8GcBWYd8jbvYlv0obknU1BPJ_0S9GA4_xyZADbtcpnquXio7Wd6v3TrbPsWpTYBZZRYD99j52m8r5OEFYPrMEJ8rtG4vu6XsTG1gAhwucsRRgW9_dZ_tdvvfyfrHUwguvvCi39dSDTTKueBdGB40vZ54X58o_lwPLe4dPNWsURlHpr5Ga5LGwjI1_iOmMSbtPpOYyc4CWt_GAkj58lf2dDMJmHZKOP51zZKbsL0hu0lCleKmDmsv6hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=MjiRFjYkyqdSYGylO2k3q8k70HfKgHeeWvJlhu3_wS4phVXprcOsnCIIMh0qxUgxP8a_GTVtwim2OhuNvmYtDXOLf8_9A6k8GcBWYd8jbvYlv0obknU1BPJ_0S9GA4_xyZADbtcpnquXio7Wd6v3TrbPsWpTYBZZRYD99j52m8r5OEFYPrMEJ8rtG4vu6XsTG1gAhwucsRRgW9_dZ_tdvvfyfrHUwguvvCi39dSDTTKueBdGB40vZ54X58o_lwPLe4dPNWsURlHpr5Ga5LGwjI1_iOmMSbtPpOYyc4CWt_GAkj58lf2dDMJmHZKOP51zZKbsL0hu0lCleKmDmsv6hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbu6Y5-3TMDPh8dV_8q3BbWOxIfLyfaeMLtOAjnSDVeR7jzHensjGZDwTy7Feahvdv181bv-IL5bstrm4GK1WK-hZlkFzE-CgCo6j_qHC9c8Q_EkWS-2DQKGQ-USoIVVLqwYLkPTdXWRv5mZCfjmsEZobiR43L94Z5jod193fm6tpjwzs10158JKWCOQXYtGL_LZ3XhapMWUjYjRX0uxKe4H2CuVXovRLHFtUTNk84pZNgQeeT6ibF8fb8MifDfN5-7wRI8gjkK6vQrsV737gYrQOdrmfdJ0JkT0ChkpKqrYiUCerX17VDL7T7Xyaf6hn9xV3Ui_Ml_Rk_RnVeI8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsQRzbnv9XuY0jHkoKZQboQlXR7tawPfmI-axoilpSQA_MeWVYn1iW92nvDYIxWmXJYCTXBZbwmcNM_6tSCsy0PWYwzciNVimtPDOlF9VlE--28uT3TNmksue6U-051tnNN20iR4su2xjt-kRFGiH30jtB5Q_h79ZbWT7rTYz9gT2FrjQk0BTcuUO3_CI42t9cvA6hhIF1tzdyBA7Pb61gIkUfsF0l4Mmx7auGLtUgH2Qx4e4P6IK6ArtjrpSwxW6P9rKuFf-PT-lfHY6I-YfxiqyRRYsa_ZdXRVNWrpCz10hEUPQsdxzIo2jkOIiKiLxwXH6F2y4Xxsiw8UpB2JUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRD92zY9KGBn_2nEJ5eFiMjwFxqWzqjVFtQpN8REWyWGybJH49lXM5D32ZxukTbYX4KaAj0VCihzFxJloKX1AtQ8ZxvnlTJYa0_YiyNG4HxkhX_mATWmgvUNagS4822UnmolfLxcAUQMDnoZpAUn0N6ZYBhz6NsrXaNiHjUNFfXzBj1vw6enmKyr74rX0rbH0rfmtd_lUWcr9SgZYyXaVm5D6Mf-Gq1mjYB5HXP3UWwNpbSZHZ3JBQ2rtEeZrjMCTWcdsPO_WJogITQSUlQpQGkWOtQYeieTdzGD4YFSzgaIRIFQBT4kP13Fk8KONMJ5BbR9nuCcxk56AfBDujvmng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUS85CXtsOPjnuuiKQHu0gFzUZf5awYMTcDoc2Bj1iKnmlS2H1zhrSKGzjbhS5BZivAVZkrwFwkZjA_nZyuxf64tbnN-4itPWIfj-yG1xAqXNQXm0M7KnD5e4TMyRWPPanbXu1sk-fbv73UbwVpkmNcMzGo3JGdAC5aL_pY3n9bBhT9fpyLfARTGlB5-IhphWsLXqQ8XREfsKH5ZikPCM-HNOsSG4z5xfEO2aN2EC7050YrBmlu8qf_LqtUhX014ViIMYSqRkRBL7qqbpdheU02i78aZXXeRwzKctbV86mN9Unca4ILV3uwwVS-eS20Wm6nriYgd2zcCUKZg-41HQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOfoaC03QG4Fk-9YsFe6YyKxZeCW40VAsnjrNdW1hIOCqyMk4RJjzOlv1HxW0xtiEXZCZvYG4Jdi8u0FfLTiH7GHQ9YooCg_fO7nsYgHL0hDUWHWVIkHGuonYvR2xjBHPSuh_vA2IYr3DQsZ0vY31R8oPueZRSHiUB_vdIW7IOt2ZouX6dVYZF8uF5IOdhn6lfCM-A-xweb1eZYTlevfD2V4avRKOwAtWW2NN7T8yBUdY5CNmDyRAReowXjwh6iQajUKXoypiG589YYcWAS3-w4ufyz4kqsohwJNKDqE2U8Q_8VNEHhkFJnI-P6aNcDnX_pAEyRebgvz1dfB9hnXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=i_S1A8WkZ497_J5UqnAtqExHHMzjYZzl49BafMil9rTqjqsVNbMhoycYZCANYI_Osg4vHJGYwvMvVPTdscEbQPodt_JGyl2bORv00DiEhQD7AobR-qij0YIkCkmzbA88IzRUeJIuhgOyDQ7htcwAM9zeOQ4ETmWg92Imxll5hbCMapr-GSO5Hy5oUCMNAvY0N1EdpeWWV10wX-hSeyFd8jxRy1aY--fuurSIL9yzWWmsCUmViwfFx4hVjY2jTpI9AzJ92yiJ7A_1eM3uzpglQ4E_IK5qf3jmoUsZQX-NALvjvrNZ-WSPPHbeEhy_7FDCEhjESGTqecvqBEqR3zU8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=i_S1A8WkZ497_J5UqnAtqExHHMzjYZzl49BafMil9rTqjqsVNbMhoycYZCANYI_Osg4vHJGYwvMvVPTdscEbQPodt_JGyl2bORv00DiEhQD7AobR-qij0YIkCkmzbA88IzRUeJIuhgOyDQ7htcwAM9zeOQ4ETmWg92Imxll5hbCMapr-GSO5Hy5oUCMNAvY0N1EdpeWWV10wX-hSeyFd8jxRy1aY--fuurSIL9yzWWmsCUmViwfFx4hVjY2jTpI9AzJ92yiJ7A_1eM3uzpglQ4E_IK5qf3jmoUsZQX-NALvjvrNZ-WSPPHbeEhy_7FDCEhjESGTqecvqBEqR3zU8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=ZTyWC5lyILNXSmWTA8BhKCC-_RI1sGiw7vman2Z-OA3_ZAmp5yV4rxgIP5zgy8aGhp6h2lPLetqWBksfmSCZCCRoX9t0Z1T7tvrcswMp1ioo3LKL9ahXuwqxtY6jQNL1kbSJhxxUip4wvDAXeR0D2mQ7OUUPxj51U4RVoC2QFK19g3wukIarW7U0eTD69mzZIsry6obBnZudyMCMZaODHUXYk1wQ-u52IVFAWI56umQQMLTLhoQmi0S9wonKREXhxxODMT8t-U9VgbKFc78tF1hkzOUBJqF9A25vwv4g3t7lj07FuAQo3MYbSbnl3D2v_QY37ukHGeztdu9wi3Jtlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=ZTyWC5lyILNXSmWTA8BhKCC-_RI1sGiw7vman2Z-OA3_ZAmp5yV4rxgIP5zgy8aGhp6h2lPLetqWBksfmSCZCCRoX9t0Z1T7tvrcswMp1ioo3LKL9ahXuwqxtY6jQNL1kbSJhxxUip4wvDAXeR0D2mQ7OUUPxj51U4RVoC2QFK19g3wukIarW7U0eTD69mzZIsry6obBnZudyMCMZaODHUXYk1wQ-u52IVFAWI56umQQMLTLhoQmi0S9wonKREXhxxODMT8t-U9VgbKFc78tF1hkzOUBJqF9A25vwv4g3t7lj07FuAQo3MYbSbnl3D2v_QY37ukHGeztdu9wi3Jtlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwA7HBOsmdIxUDNFB1uWuYu5wY8BaPsRPPk5W2N5WiSxGslUf2m5GleFWYpeMLWU_geuz3-Hj_Rt5FXTo2RYG5GVPQOG3AyTGMjf-q0cR8jqSTUswnlKSqSEJIx7QIu6-OTx5AoPLNky2BR4B6Unu65WHEIgbqv3gQ_JVcHAeag_Q9L7XBGwaCK1POtir_ii-82oExaRZVw_Wb0lQyxxGGI9kPO1x5NXoMDecKy8XGMKH4t1kQqS-Qx9lKHsWrD5ESYU4_r7R-hwPXwj84jx3JtOer8_MZKMmQB5lq_e0IEpeLM8G9QMS41BSrMIn9VFW76DMahi-Qe8gmEAiACLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-izEiYdXhpIoxBxxX49B1N5EeF655_cyHWFBecjSZ58zb7EHPEPXHBmsbR1bia-82hsRRZ1shs19vSk8_YE90KA_U8kmXr2XQmj4yIk4chlvYtAdia5MwkL_cOnIEH8F_Yo6rQpRqPzyoD_voE3_oY_Ysxeet1IeK2lKfj4rFPxRupHKGIffHbMbebzN1BXncsEIzBI1U-ymScUJ8nnAwOR6CmBtwXolhnkbxbD7I2Sh6nkbBis7S2eX-gaG_U-5NLve4s5msu_GitgdVIxxrVyZk0NG8utX2C0io62TUe-Ysab6ef7xSgTqEkqN4QRH0CoM0PXPQSCdSU_3Y3VjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=ThZQldsFBuu3sF6FJ1FgnCpkhg4ENh06F0kpT5V3FKv0E9J0HVLC0uWoJjDO_OZAWn3AiGqY_13Lhmu8CHb8Do8ZlEcPhOlUsyac3c5XPlNTG4tXETMkwbYDHnYKqrj5-codfTXvIaXS-2EkUczZNm7LE-GOjKjSiLYVXF4blbjAMVePLgqPceiBa5njHFvG3NgrZTIkHYE69W4nK4MJDLFy3ouo2Ygv9lnjO6KOwCF_y4zwbkjcuEt1yqINkVh1CGAA2tnl-PKiNOC3AZWqhtSELlGYx_W8dIzrAqcNesBK158C3aRc6PYYsU8_vTD5SSD00HcnFdo2Yg7iwWaF_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=ThZQldsFBuu3sF6FJ1FgnCpkhg4ENh06F0kpT5V3FKv0E9J0HVLC0uWoJjDO_OZAWn3AiGqY_13Lhmu8CHb8Do8ZlEcPhOlUsyac3c5XPlNTG4tXETMkwbYDHnYKqrj5-codfTXvIaXS-2EkUczZNm7LE-GOjKjSiLYVXF4blbjAMVePLgqPceiBa5njHFvG3NgrZTIkHYE69W4nK4MJDLFy3ouo2Ygv9lnjO6KOwCF_y4zwbkjcuEt1yqINkVh1CGAA2tnl-PKiNOC3AZWqhtSELlGYx_W8dIzrAqcNesBK158C3aRc6PYYsU8_vTD5SSD00HcnFdo2Yg7iwWaF_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ikmzwsO2I1rEewjuOULljFnT_caILgZLlAsytqhNpP1Ue1uAOlCqtGMsbgkw-NkaKtUKHLRQS6uXBO2BsfLGhLnv2EwCzVniZZy0JoSd9L2o2bCgEwwwUBhJ6Bplro5Izu5ngkBr9FfYAz-Ol7B7S7jCPl3m6-7WF-owAFz6NbawmufboYtJY3r3ZAM9lc6EBgiCyNFm7cBSmFL2Nvm_WwFCCvMjFf69mKVTsxyPbpkxow2yWMIOO5Xyv2s5i2vg4Qx748GkORb0PzgoVMO16pOSFOMuMiwOw9y11LL1Ns6Fo6Ia1pCf8N2hNVYmPqInYqlyty3XuFS9vPytDClCtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ikmzwsO2I1rEewjuOULljFnT_caILgZLlAsytqhNpP1Ue1uAOlCqtGMsbgkw-NkaKtUKHLRQS6uXBO2BsfLGhLnv2EwCzVniZZy0JoSd9L2o2bCgEwwwUBhJ6Bplro5Izu5ngkBr9FfYAz-Ol7B7S7jCPl3m6-7WF-owAFz6NbawmufboYtJY3r3ZAM9lc6EBgiCyNFm7cBSmFL2Nvm_WwFCCvMjFf69mKVTsxyPbpkxow2yWMIOO5Xyv2s5i2vg4Qx748GkORb0PzgoVMO16pOSFOMuMiwOw9y11LL1Ns6Fo6Ia1pCf8N2hNVYmPqInYqlyty3XuFS9vPytDClCtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsPFkfavvdxg-m6J23_Lb7OdKxSvubRwVS_9RyhvcM0-NdQK_fQqA_NyuzZoSJhpu3FvmCx1TehcXMfxymQIiRTzFgN-Hj1qSDxe5jKTKNRvP2YpJ3lAYsbGmkrvU5vWoZfu9-FsF4tStGNz7wzgLXJQKMSbLNH3t5LG6JDFVJeSrIWjaavE-b8kfhdKX1j7BeFOaLc9s_hWkjjioAMqPIMG5fr8fFeGBxdBece5hCHZVqLaXKAHUV_T8-K-Wrv3eBkgHqlL6nI5Vfohp_UCsRJjcYqFh8ihvPQSIaxjVU_HgBDkRrW1skiK0A8bPu6hai3s7eftgdDK4oHfhU2Liw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QPoevqZsWGciFITC1YcyCLgc2LwIM_8QR4M9tI3Sbr178VZAP9orKX6VC5yyKTO1RgNkFOKhWjaNEKVIDlsez3Si0tf8YDZeBnC6V7qe9eMfzO1-BhYIRwf9rZUPQ4sMsm_EucwBFWZAd4tiE4d4GdIG_lF8zCEd-1LjN9HoNGY46SFHoABuD9vrFFwYXjsk0Kd0qYRnnSDp3iupHu4LNPNdkYy6l0nLShzAFN3_mefCgyko17yEx_otaqGVZTwPWXwEUCzX1kfkse-fbPfsV8ed2gnoe83FkFKZ0Y5uVdiFC8ZFGmDZgFTaP0yJaT6OXztDfQRRZQjbmjkF1JAplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6sImDz30oc4M6vvrkFgr2vYDuEXOnJiiWXQZ9TYwZcB9Aapv8Z10w_frWm3I8Zxz7bej92s0xrfBQfDmD0sIfaUjaG4Pb-o8ueNF4J-9iKSMDmXiTsBXkyDhVu22GOxCmUgNJaAlTuraCnwxFmTGS-lFwiXn019Tc1xHk031Xc1IYgtTXzbH26sGs4CIkNhM_rQnWOqTqcUhyFs5bparNAqiZA6twC1bJkAxoK_ncoanE4fy2Q8KDK6z5yxmXyaFU06B81Z8WB3SesCMLM4Iq-pywf5iEDfH81nuvCiiSoQ-1J368ckAgERpB6DZET689p25GXPrhk6Gd58Ll6xHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=KZvJKWXLEF6sygJo4oATOD-WtwTy13AGbSz_0yXd42prmVrDaZZHVX6IKwEwib8UzH9U4t6LDvqwFYnTY4xDxQlxY_nmt_rJrH5YAGPSZrbdn0pJiX76Y4nurE76lfpam2731Xr6fygxfvqy1zjIeRBpQ2jru9QFJmcFTgmNaa_3rJazDj-pCDqCgeVR5suHHnBMIMTMv6wOCflT_q0eLs2az6oSY9RH-SPp9t4BXHafnZYkg-nhoZXvpKXLgT1Ba_ewIdQwb9bs4xXHFS9Js-RtlF39C0gKfx8n7nOZO2KNozzazkmUqNXK9rA0DHsAtHFa4BeKpzy64w8x0CYztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=KZvJKWXLEF6sygJo4oATOD-WtwTy13AGbSz_0yXd42prmVrDaZZHVX6IKwEwib8UzH9U4t6LDvqwFYnTY4xDxQlxY_nmt_rJrH5YAGPSZrbdn0pJiX76Y4nurE76lfpam2731Xr6fygxfvqy1zjIeRBpQ2jru9QFJmcFTgmNaa_3rJazDj-pCDqCgeVR5suHHnBMIMTMv6wOCflT_q0eLs2az6oSY9RH-SPp9t4BXHafnZYkg-nhoZXvpKXLgT1Ba_ewIdQwb9bs4xXHFS9Js-RtlF39C0gKfx8n7nOZO2KNozzazkmUqNXK9rA0DHsAtHFa4BeKpzy64w8x0CYztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPhOqgT896pVATxxsufMr6QNLS3oBwwHsBNdq7NciM5oxJsoayaBV5epSJYEYJrqUVul6_fbvEWMl5L8_2SyxRpR0HgNA331f7mhSHX1j0iTjUpkJgRVz9OLkig-vqey7X6x-10TxNS6GOeK-zLxcTOeg20HGvLEOT-1Z2tcFu3g5Ck_yuH2Fgazm4L4KtB4OHV65AS69cM7LrP-Uv_Y-g_cBGfoXjoNljmX_X7roDNco016S6u8xReD7PFMW0l6d82YyDWgvw9WgXWDnfdENw0cdVh_KVakU6-lclHQvuWxmDJ7qMA1FJHfyPOQJ2nQgEvZd-YD67fVCDyrL8xdag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkcSRdBk-Mh5gtu7T0Z0MD071TaizvAa_fkllodxDwfQ7QobB6rkYULo6mz91dHGqrhm-LbVQ5-phNpoUJRyS13BA28sJxiMFCxJDwCoNTZMPJWZ0jqASSeJopwldSM1fq0P80X1xlucOvD0PIjFmBTJGmzNUEQSLwt5HeM2ngqJWEsi_pKZEJgd1Go6V2UjmY72yXS3XlHoD3vGmLhNGsqipyFEGyPqBRgwDkmOwyAEAcJHqLkZq1be3bXN-x5U3Z3C-Ml2AGqwd38D2usYWRFQgjyHk_2xZaZVEA79yxGLLfD4xycqnc9XdDm0eSlXrpVSIqEiZKi4lB2Vqcn1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxazuLH5wReWvnMKmwajPn49q4H2O81BO1Bs4ZMWISTe0j1Z9DJcLoHLhpN9Vc2H-pAdwj_3YjlucAW1xkREKP9rxcOLLxZJOdCAsrML5lAGsqUb6hiK164mmDTV-oUgQ_IP2ae-VFQ_3O6a_3AQBfLtzIvzeM5oJi0D6zK1QndMa2XDVkgM_kBTjzAbf0al8Drukdyf2C4BEI_ClpKu40uNTvg0KzhmG-xezWETxcUQlAZh2AAuVDZj-Vd3l6nIDeFMjLt3icNbKwDQQD_s3po4SR_V7OH-VUpvywYSGW_yDdWpIYI7F1Fxu-eqj1WHxR3LwjHH9aS-ZOCfYVsylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1LXpDuOWdIpMHTUJbn4iMKpo_dbDFLIAIxfxkNqWj4HpKnGJ_f0a3lIpxLw7EfWvtlBP_wLROB-dVnTewUeDiA0uUjSNSX_hXszxy9P8tH_BLmgWBdQD1cfKsOwEL2Hw0lxPLy0AZkYJF5Ft2dNiob8clDevc_C4J6-iOxx5p8zfllzVQEs0aUFYnNnK-iPFxHCqT1Gj1iTZwJcqpIOCbefnW-3vzwB7QfevkOn_c3_DoG9_blF9NLr8WTkygboTVCWw2B4Ny6Fh9SxTs7S2nxFkfRmjxX8R2hh4kc8BuKEIw3FrG5oUQaRYDJs_xJksAgGjxhowUoWxcEYbhPxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=TMlS7kefmIqbjuuo0a2H84ffnsOMCjNlUnao6JqzeTdZccuEWuiVWoFON3KSWy4D_BTiKyK72p-9PgdIKP5WFSf96XOx04SiEwph_UqHDtod5jRI1fbFtqhGK6iJmGeMwlRHfOVgeBuTLqYQuzw9iKbAN9l7UghhxCiBpniRkfA87LTDK0rM6xcJu1NkT_WXv_je1pphOZ-sGfpFeBrTfHiiV4wpn5s27-kwikrp1JExbtCmh4F02gbUhoH1waWxAX1EldW7ZS34KgdauABYaSlcFOStHQFoRzD6IvZl537bB2W6tEfS8YrIYHCR8mQIvZZzijA7nDEsSg0EchYIXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=TMlS7kefmIqbjuuo0a2H84ffnsOMCjNlUnao6JqzeTdZccuEWuiVWoFON3KSWy4D_BTiKyK72p-9PgdIKP5WFSf96XOx04SiEwph_UqHDtod5jRI1fbFtqhGK6iJmGeMwlRHfOVgeBuTLqYQuzw9iKbAN9l7UghhxCiBpniRkfA87LTDK0rM6xcJu1NkT_WXv_je1pphOZ-sGfpFeBrTfHiiV4wpn5s27-kwikrp1JExbtCmh4F02gbUhoH1waWxAX1EldW7ZS34KgdauABYaSlcFOStHQFoRzD6IvZl537bB2W6tEfS8YrIYHCR8mQIvZZzijA7nDEsSg0EchYIXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvOK1VDJzBWI1o60SVbIoDm97MxbsO1mTZcq4oioseT1ZnFOZKyjoFOB5Ky-IqBSgnS9hKZndY4kK8Zq8KBMSO9QiqtZPf40CV4ZbXWOIz8jCr9uNh3v9xeYrvedM32c3sxcVL24-GA8qmAXAXMtNl9_DpILTk-svDbdhZBqOgkLed9I63z1FyWfysvrgq_ErYI6ymqyrZOh__sTz6TE4VQJzq_72aCzBKI3ektsyaC-Y5CTT2osFBIlLX9unqb8ddAtK3YOIT_ZYq5uNRGpq5UiBSICCdSzwSgRYT7n68cBdWJU8N5xAKGIu2L77cmf6Fw4KdvsKcfO-0OiENgapQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qglCXlGfamrWieT6-hfydLlSP-3926EHVMb_Ggehay29tAK0Ht3-N-ByDE__WfDTotWTYF9YfFCBZLrKhUeU5Etu68tmXpQKNYGHC4VtLSqCyKi2nxah0kijEUlmj4Zan0USWZw7eF6liSLWiZaF3h-AymQnkXipzC2e0cC16eFhjhhKoczpLB2uRALW5t2UAxdbnTnepdUy03h2Fhh4KI3DCZlTy3VIxdz38A5RzEPqbovQ9i7p4GDw1f37gmnoSrqF7VY5hkrodDrKbK4dIxn7zSojWslcMRWPKcXWT68wlxvo8JL8flP1nni22AVlMERVB3pUH1Lxi0D3X5EJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY1-8-cwfxEkVozJhWJiLuqhtkUD_9aIqcQ3kw9TQDtJoQslMbaeQhBInzOkV2fYyL4Hu7xHxxEojhzCXRVshX8GuhKtbSKwP0gqxVaAskoiRn9EFUZDcJpzTo4mkRaEvhow1y19fn5v8zV-YJUwGLPpMlLhho9fT-O3zZdk9PEr7bOO7mI4GMMWulAwgCEz-uAysrvM198f5dCCg6EzTAztt4zLdmrxTe-R-tRjMjMBAHGGM981dKVjCMQ9ws3RQiXnEjLAmciLSPLet0S_tBxSZrqgxZyBjmpnPCY1OpsIz3JEwA2zln21cbjyZ2Hlnf6ctwSuDaqpD3KIDKuVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=eUCIO0ESRuK9MYOqgUI4a6xlg1a5Q424kQgbVP0kkulp762Gwhp7PjLkFe004_0x_3uZnQ_C3opehrR3r6dF5lvBcN9JT_w3QunIVhaDnPS-FTYln1S0afh-CWSsS395slURTaOq5kQwzbM9WYCkrf5SrWGTIQLCzkHkRb5P5Y6lbUPGbFFWeRh7O26ultsm9MBtnWrj_PBfsOx6e1m6AvoDNY0_hJ5WPRNSeXI3L0TsNptv28ruTJIbdN2lfE1q-CAuQfH86OclgxJt0y0F0RALbrzYRh_SjlntB7MdJnMU9X_xd2mILx5TODn6lmaKvnSliD1mMNUroilJUpTvKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=eUCIO0ESRuK9MYOqgUI4a6xlg1a5Q424kQgbVP0kkulp762Gwhp7PjLkFe004_0x_3uZnQ_C3opehrR3r6dF5lvBcN9JT_w3QunIVhaDnPS-FTYln1S0afh-CWSsS395slURTaOq5kQwzbM9WYCkrf5SrWGTIQLCzkHkRb5P5Y6lbUPGbFFWeRh7O26ultsm9MBtnWrj_PBfsOx6e1m6AvoDNY0_hJ5WPRNSeXI3L0TsNptv28ruTJIbdN2lfE1q-CAuQfH86OclgxJt0y0F0RALbrzYRh_SjlntB7MdJnMU9X_xd2mILx5TODn6lmaKvnSliD1mMNUroilJUpTvKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=qER6ixgbHar_NPZSM9d7VkacOsyjvjpmR5ZOoBlKtG-VEl6ZjbLeMyFH1f1vXLsQazGPPL_ryznYUNDY1JYPPHhob4p3kWuwrip-oxguPDzmyCXLPplDDTIdfK6faGD5qMV0E8XYojQCkqSQ5glGUuqfiDM8eC09OqCp2vQmnfeBsgDb1CDubNMmWcd5V6ybrznSRgY543d2fjMsz0hloyIN44Q-hTzktnkGl8nEnrX6TZAEcJEtGUNMOFtrLf9J_B5j2SZYJrAfxR-E-O3bSsN-pfhXPIQvx2vs3nCaqqC_HIbNKMNzvE1W3hpXFWOQVQOt9zJ3a40BAzFDM5uOJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=qER6ixgbHar_NPZSM9d7VkacOsyjvjpmR5ZOoBlKtG-VEl6ZjbLeMyFH1f1vXLsQazGPPL_ryznYUNDY1JYPPHhob4p3kWuwrip-oxguPDzmyCXLPplDDTIdfK6faGD5qMV0E8XYojQCkqSQ5glGUuqfiDM8eC09OqCp2vQmnfeBsgDb1CDubNMmWcd5V6ybrznSRgY543d2fjMsz0hloyIN44Q-hTzktnkGl8nEnrX6TZAEcJEtGUNMOFtrLf9J_B5j2SZYJrAfxR-E-O3bSsN-pfhXPIQvx2vs3nCaqqC_HIbNKMNzvE1W3hpXFWOQVQOt9zJ3a40BAzFDM5uOJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=hn2kiZpEr8QEM3gW4IG-Shy1PKCBqg77wMjn8GtjIZ-eMY5r3KdK-ohxgYvHoEwF1yE7YTCv3wkwOa_qfQiewtBvvXIWcJY-5GzhOF0MaPzvf1R_NsTnBC2I_owtVFS0HxWx8IWA3uaF-9iwlhQhAlaQcSu2fnAcpDzpbOtLUwlVXqGjgBRrxyR1ntuH_N2IouxE3IS-kR8hiSp7RLH3RKsoM2zOrthSwVjSz0yOHrxX1eOjC-0cTObqowbAeEciohkEAlm712qAFzAO25yhO_AgztpZ59q_eglPoYjBAAmlQDavnOjmf0JNZHobvFsOuZPDugMFMfuBrHR68Lu6MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=hn2kiZpEr8QEM3gW4IG-Shy1PKCBqg77wMjn8GtjIZ-eMY5r3KdK-ohxgYvHoEwF1yE7YTCv3wkwOa_qfQiewtBvvXIWcJY-5GzhOF0MaPzvf1R_NsTnBC2I_owtVFS0HxWx8IWA3uaF-9iwlhQhAlaQcSu2fnAcpDzpbOtLUwlVXqGjgBRrxyR1ntuH_N2IouxE3IS-kR8hiSp7RLH3RKsoM2zOrthSwVjSz0yOHrxX1eOjC-0cTObqowbAeEciohkEAlm712qAFzAO25yhO_AgztpZ59q_eglPoYjBAAmlQDavnOjmf0JNZHobvFsOuZPDugMFMfuBrHR68Lu6MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-AOXB-9uHUDe9ymtk9jK126WyWqXw3d4opyHrSmJM6rvCzSEYu_YGfuVXk-DezcqA-z9P4d4UnZf3Nd2DsG2LjyuASWJGiTB-ugcfW-HkU6Ux6i3MqVJfL3irTMtSFfeTnSUmRuraaO5-DjQmUhbhegfqxfKdSYyVMqXi0aWzCPJSJ4ZZNLPXCguD-DJAboB6dp33GXQB3IJIqdjBNDzwh78eBBEEdQAAjklrDuCPputUg224SaMYIa1JLSA6N6pr12Se6OHHkpY815xHmH7KPV1jwzsWsD6wZzF1fc3SUUdeXiKlW3nBCxSCOerZ43lR0xDnKIM7FGUaQsW10zyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqmYvcBB30yIXkO9W1rCW_lVi94QkB0b21sp59XWnlKfZQFIxyXSrGGoobq-BRnthgJBbWJrE_RyFwcFUiwd51km-fWHXenV3CiA7LsOLukTOye1MJeReSh3r-CWOQZ02J6Reum8buWYcLjKorZGPbLMS698mgkw1fkRfVgBNLE0UmdWb7UNU6Ff1CEwwroBSlGhcOJOiPrKHvQNXPlvDogkhrFIZ6mVHLpEWW-SDMEeMfyV4cQj4baVCjASVbto8ESZFqlnl5zmgEIRPRKW5KxHTjBIsI-lRvHbm7R6OnSZJTimAiXZrpiMKOQDEwkv5Bj6rimyFfVBNhWQxvFCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDrydslLRwI9MVxw1q3gVkDdPtHb4eYWRKwq08tcLehJk4OMVL5LK2EZvZXl421A9U0oEP5Qcz5smRb705yjAeP73W4mqYrQJn3zLibos7dURpc98ByjwLpQ_kKGQB1Hq3Y3mQ6SIQF98fcZ_edC7hnFAL8euHUsJK40JcqN5VEzffbuf4vjJLEaEYHtK3c7Afqhspd6p2sddiuBofWjBBt6vChYRxAbX945gj1xdwd8JVKNujDEA6T_cV5HDqBjdYl9thCDwtAGWWPs6NqxhOL9JtKkFqw5UaPGuDSqFgVV3UOyHCYsMvvAPIQcL25aAkXKwCRtzUqTntWUsnxcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uw_Ih1CAuR4elZTDKcpCCOt76-hIDmYuKS5tW6Opwo23-w12ndFvllqWyBfuArrm3P-_Y9ClPSZkwdqcjd1dbPCFdTNJo0C5xyR_CuWbQX0y_iyy4wxEZCRC0aHsFCdV0DQkcqYSslONxuxBcRgYNP7B8SUgYm8ZoAPGh9dyEEAlGX3AzBK74Gx_sYno8LsQcKqLgn2YehQUR1KMISk--4pIKNop315MTejqqRA8rcPiUT-LVOcboRb3iIB-B4xfqrFETU-k4VYNhvpfeF0-0ClTu8VWqzQkFx-_D6RyWbXoAO9HalR8ztHztZyz75y0dwnQ5lAmS0rKE_jT6Um7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBzcXuXfdAzvkWQft0FH72JuvqN6eKRKNdV419x6fsCQa29DrA1ByQPWw4LQm7xRlL8680TgKHC3bMRaHpnnEUzmDcdX4dIiCtOtiwa9hG0DM_eY14QcHBzMzfzt89Btx0l4f_uqfbQCZue7Q2dVBFbNgxbKjY9HXUqyJ0oBoppMCys2sOiE2ogil-tTHnQ8DMSxMhCzO7hW2Z5yMEvVUYebVWYmuv75s56sjsLmHwfODh2vNXAOtWS0eP9qvfYPOXN7pEa1r8rmVkMMtvXDp7HWHwaVl7nnz4IL_BpfB6MrfgTpv0FzxsMu79zHNak0mbq0QOoRjmBUj2zFC3N7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogZ2s0m98EoMUZyfas_iLu7p26eDs1t-Y1WjeQJKLQfFEAvEafF6z3xpc0qfYkMJbX93iB-Tnl-ZexYPygmTMy-H7NcKrqUOTrdPnf7xiCvXm3kU6i9Shhu5cXvlXoBA8dui4deWzKN-3uW3RONDm6ipuj7PpSDYswVrAuNZDQkgApJ1DK4O_AhyCCtPHLMtBN2gaX2Cm8lzP4SPz6b9MVmow1HIZ49EUj8GJVHInmHqF8ry_oH0zholJtE475HZmuVajMf_aNlQTikIBxXCz9kzCH4cJnRG4KxqRf6I3iYEU502DYuFfn4gh4Gg0eF0fZTkixe55EHL6biII54x6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kn0-WXi3-fV-ykpeXV7wx6rBWJzo1Rx_YhfM4LQp93zPZ0wqX5f_oJo2dYo1z9Xy7bSmo4N0Tdz8hLklMyMBsv8d7dbqGn-wupkMTu-EpMtg_WMWMMiXgJ7kgBLHU-MJt-QShWJg7nlmEamKcPKwZgn4aUq9WmmUzGVGK0qyrpltsrQyvVtJIotW2bYeZ3gSNSMN0nF8352bCaMl9gKVgV1Zudtr9D0Fuwr-lFiSw54CEF08XxFFm1aGf2Fh4LJrzbJt_m7zyjO8JOc-bm--um4BCsuSJ3Ap0itjgvMxaN-d722Cn3NtVG93CWyu3l0MgafzdTeAAQ9qXhXKg20Raw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvEiBkavLVret86GMe0uTzq6xsNW8N9Ascxv4Asy-fjkWnWJ1CSbKlPrkMetcKNAx8zKcxxAWjpk0D3gwvR6U6Uvd9XrUpxmV_Q4dGcRBe04OuPs1ttdbKyKxDl8bsFgcrBqpG_YkcdEzvXbTbRmfXqFNdh7U-dwlHMPnZ80jqkVHWl1h8SvTfBYokTfemj3Upmhxn_VhH4SCsFsCkBixabC9MlOeER66E2dvZ2tqqoBbINdkeYijJxj7i6I9shavLtRg-DCVrKmRcMChhC97079Z-m_Vz4noEMQSfW1bbYKg0UcJjRwxppKEngzJZ1fdcYmt5fq5A2TPcbdA1SH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwB88vi15L0Nskheny8QD1dN8adeOtjphE0zSxkRJYX626KtGgQv2TJJ1EQh0h4W7V0TgVPSxLc_7skJWrHnxH23dRIHIHih7CEIg3Wuhs-e1-k4IMhdzBrjfYT6w1V-Bnov1fVBlwNiECMmw0M_FXv_7gUGnCuXtOAVBFoy9A8o0T-ksoh8baaZsVUd5fZ_B5IV0T6jUCsVPWk2ucQjpct4uVIqbOyyBrHdeAU7lyDPNUVE7EaiX22zmLGdJSujdHAJaavYN7lgjIpZU1ztOyvwL4ZFRfcGIuMgMbWWgntCU-_ZM4WamQLOvcFvqAUNJRYELccjY_SnrYkDidxRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7xcd_qo5BecZdkd3gz3IDea_125zTlU2db1MbQjYr_2j0bK6MGEj13wNmEUm4cgrjn_ofsPi_XfxzJfUDQqRY4x0IX-6uvlxoqJHiFv6PyQJ9sfHfNbTlCVdoUba4tu6pIT5xu5LsnoH4GgbOXpDWH7KVhU1pjyJ1qvwl1UkwfOxeJMnaJ87y8HCoFMvVa4KHt7LaphgBIMnA3ivNLh_KXX6PDwrrqbPmxz1uyfJQEn2ppJz-l1PnxzfKx_FOKH0XeprafQe_vmMU-yNKcvnZFRUu6nAumkb745PTHP5jJEPfo4iNZFBRujhpW6dHIzOgSSmfNB1AcQMVV4LioVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ6YerrBmuBewTJ69XgObglZeJQuJkQHISP5ulkDXc6EMzSESWGh8hxseie0sz4A3SDB8MDbC2ufaAUEaOiMNW7GpdbKoRK31dQAFHSwny1ZmRfxrwzqIgv2lm5SvYINrDPz0ssoSPWwM3iXwaX2iL000KFviEA8TVB4uIYpK-FsVGOlmBN20dFHOnLmb99bZWqY6SKOBVYKZpgQwjJqTrksyGcBPaFNvdhMQN6VzhA03-BpTc1wRjrbQ-9aUV2kO85S77-oZy1BNBDjwvfl_k4661uVHK15eiQYGhvw1DBtLuuSaJHj4uzNOuwMIDKLceXyd2oKwXL8zc0XI-JJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJRb4wjjVkQQc1mtjnmqdqoHjM7hkFVEWGQtALA4LpgX1jp2Sd-u7osfz64a-QrATrHtFBGslKUdw6ywE6pmAqLOV0TGSdwpCYJTRJqzCiWRd8YXxQDJr89qwFpIDZl93RVxPEZIjpHI3ATNNte4C0R2MQxrB5EVZac0ufG7YacCdHb0lYAEjsVTnKC3BUN2UfomENEdTDdYmpON5qi8t6FSejnbCf99_7QDRJGIlqZmpnYNH1wPsUarYbFV48B2jz0Szyg7b7K5VyxvaYlc-L7IQhoHd_5H6fiEluhqKhAv_7fdFpl2G8HmaAQVgR55LqweCwy1_OrfpxJmarLKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhbl72yaZbRagXUop4JwUhD5IqTS8QK_H5Mv0a7nTRnpvQNHjqVAFuGOfTdaDnwWID6sWXLdg7yH2Af9Qx5I8lW-xxBvnJAvkOq0--WI21hDtrgoBZnWmPSYL7jORsb112La7car3J6-QU1TgwvcDQt_l5v73x3uSrK4MQZLZ4yupA63As4Xl96TS6ZvG5MndgUlnRe5JaBHp7hX5lc5cenTTTInbHLarG_wqsGxuhDmoR72bVydjRs7E4w_MKO8fg93L1RxVu3VmDK4lKRfw8fM244cW7zX8k3IcEOI40lMz1FrAADscfafD5_1J6lR30KjnkdIKKj_y4PLJ4gp4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud-asyeztHCYH_aObB26A76mVaLHQdx-E0aCxUcBQ9LxJ6D1RIhwdoVDzu1IaZe8jOetzdb-SuloZoAtqaCEbU9KuV3l1kXaq6jPlHLplwL0aAUUerMWpktAQKmix8M2PtFN5EFS_Kk1cetA4IeVnYH9SJSj16Oo0-730CRF_7CZ-CIbxAWStOyU4PlhPqh4uKFf8mN2wAK878zYh-lUumiCEkfILmT4KzE_ND72tobmBHikppKXDNYesTK78eqH4_lYUW6HXaeJDzfaRHyi8-FRZ9b-7iPdyjEg8xmjM7SP1iR-V35ZYiHHakvD1WlHDPaI4L7tBmPEMHc7RZXRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXlT3jI65e0aYZQwZWRfFS5YthqHFvazHti0G0xvaLdEGeXZHchWF5BerniezFE0tRum05mFPmQjPphFVsyVZyoQPp7FvuLWNeppY87-auFJb_qRmatXFbFL4AsW6lY3YlKPHNtbViC-FavsiIsFIk0PVhVPipINLLnFEEAGF_gozhhJywozCs1k9Y6Yi23sGh0RtBuZeGRcR6Lz0ceO0K53SbXIspHv6PEE9EVpQ9mCwphCGqSKmXqEk49Dfeat0CDRdQ0zaisdeHZkFCfAes1-q_wUQ_7M9SQyLriye7WKudi36xAVxjUB9jIYLp_CIwSYz4i_SeRpPXGMEZccPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
