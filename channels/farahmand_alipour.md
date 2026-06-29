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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 00:35:10</div>
<hr>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2jXUzua6hqCme7db5HWAsnQpa4fSpg6wrDhaMKcv0NSw4IfhepNxyKTR0VKuswg2bQm6dqIjVuWN9vNMt0tgWoPIa25z3eVX6rx2F3xzLI7YBDjS0ptFM-mAAh0BpkiJpKMZbV61VDsyz92q8qIC6B0UO_5t8MCXWIqH1DYyIsTDXJOLPHRjxQ3t0_qiYmeKCsCn042cC5BM8gBNyDkY1fI9-m1wRB5jeeHkW5p_UyX-OZoRn_nJCNYDrU9ipt_p0JJU8YQy4f3-nH3fXsDN1TNa7RAx8m8XwTzMaqfcLyiSkCEwIgTc9013Shnsp8H96M3EeWlGfE6pzyBze7HHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS5S9d764T9zFk6An4H5s1vCscROBLJiiwGNHZ3PKoNqthjA7EcQ0OEiwVRGC45CrT-B9nfORTMt-zTaBzRuhnwOSAi0N573j2jYXeYHfJjSPJ5MurKlKB607h538uhofhuzsdPrUsKIlOTR0h4fj-UV8LHj-AeaqFVtOq_ia2nYNQcxCdd28v3yIazw3z2Ih453pO2vA11hfz3ufIZ5FU6CWS0lJ0KH_i4U9toPEpr0xUMzz277_Mxdqcxk98bl4rlWjbku7LR-QPbnDZS5NoNMqnOKmnzjRLZ_pskoTfEzF_YClS8gjtIL2KssvvaMGtx2l3EZqqsPISxlkzr3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvztdfVtj9TfByy9vnraHfetouPFFNNQ7M1mSDFN9PsWO9nZmlU-_SU8KSxxzWOvPJHFb9l3sbbzS1vOSYIS3ERYaR0gD4S8VlFBsU5z9VWH5YogCVTsFkKTLwDMXex_hVBP94EaZS5S8t_BkPSsIBS2CuSeRjk6voR6QnHTVTUe7JJ1tMvzQA_5dQqFWLNmo56zzFTsip_AS_jJ9RjDKnC9quVXkR5i-O1-k4lk6-ygBaaN91OuFicUO3JTAWIGPEFKGYKcs0vP-xKBYgkD6PWK1S87hPAUgTzbNRRV0tAwOoDFadfm3ZGhVBKrTMOnUaBvbdap64KhpVAPcxwlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YoA_jkol-01mjn0tXCS0NIBGUESMY858Ks4TjKmXysUaNUQ4NY5DoYZq89DW4Ju4XckW5d-eSPIHckGSlLZvok47mpkbmz03rBF23VulaysoRIC7LYgpg9O8U-Eb7Vo_wU1sp4NENVO81MHPx7dMUMcDNsziWpRy600htyci2PbNbyTNU_jAVw0ortEm6I5iLLgwKKfomdbGnYYrl4nZAbpIwlyqMbAajxGYKEpCfLvM-JzF2r71TEYo4B-a_Pbq01xeSvh991Qg9zzhvkf-lTMseZM4KV_4CAuvrxdTuu1u-CYnVoTOWcCySjJ_JqLW5uFI3fvOQkA-O992h6UXDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YoA_jkol-01mjn0tXCS0NIBGUESMY858Ks4TjKmXysUaNUQ4NY5DoYZq89DW4Ju4XckW5d-eSPIHckGSlLZvok47mpkbmz03rBF23VulaysoRIC7LYgpg9O8U-Eb7Vo_wU1sp4NENVO81MHPx7dMUMcDNsziWpRy600htyci2PbNbyTNU_jAVw0ortEm6I5iLLgwKKfomdbGnYYrl4nZAbpIwlyqMbAajxGYKEpCfLvM-JzF2r71TEYo4B-a_Pbq01xeSvh991Qg9zzhvkf-lTMseZM4KV_4CAuvrxdTuu1u-CYnVoTOWcCySjJ_JqLW5uFI3fvOQkA-O992h6UXDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=BNwGl-041A5NUj0uT6d_Z8xW8bqM38_MzVvadPlWPRDwo2J9rGqAkDmlk48-gP_y17IUuoKCTVwmXFGLtGQJOWyy8FeKu8OygrkUoax9L087_mT8RtQ5ydoawsV-IADJ3-Jso5sc0DRRKYCVw80SgCwiQn7bqV87WWmSdR_hdqqzcNlGcYfVJnyiOYPb1IJ8mFvoLHZgQ5SlewPQN2-IRiCBhdsTsSKXOZrYVd2PlQPmqEgQcEIOL-5sZXgrWcvOe700Z0_4-98X3ckLM-mQlTsZO1lIIh7haw_3sPVySlGeLVJBu3xe37Oon-E1Xb7CMVKVJINJAD1ra2bYXqHauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=BNwGl-041A5NUj0uT6d_Z8xW8bqM38_MzVvadPlWPRDwo2J9rGqAkDmlk48-gP_y17IUuoKCTVwmXFGLtGQJOWyy8FeKu8OygrkUoax9L087_mT8RtQ5ydoawsV-IADJ3-Jso5sc0DRRKYCVw80SgCwiQn7bqV87WWmSdR_hdqqzcNlGcYfVJnyiOYPb1IJ8mFvoLHZgQ5SlewPQN2-IRiCBhdsTsSKXOZrYVd2PlQPmqEgQcEIOL-5sZXgrWcvOe700Z0_4-98X3ckLM-mQlTsZO1lIIh7haw_3sPVySlGeLVJBu3xe37Oon-E1Xb7CMVKVJINJAD1ra2bYXqHauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ftcnLFrMvI0SDIDq4Qa0B7cf4l20EwfEpjTxjmcdvtSHVJTOAVSPyclPocluy912yr7xK7L6LCPWMNKoetPyilUP22fREGwXKUYJPJAaC3jcJU4_GyHPRO4tEBpEijf-8-WSvmwKLYxvDKdzTLyHSYKo_ESNItHCSlkDKoOtcf-UXKbeVAyxkVfilJVax-APDyoOZ-mBGSjzLgWk1h1eyqKId-sSO5ldgPUv6D-EPN2k2nPSPuBysit2gd5J-w_LaHIXMvffj-rwd5f4xs-sFW3ROXmsDvj7PPXO3s-OoLC8dWKB7hNHVxMgnf3d5DVneGV6paRG8IM1ifL9cz-_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ftcnLFrMvI0SDIDq4Qa0B7cf4l20EwfEpjTxjmcdvtSHVJTOAVSPyclPocluy912yr7xK7L6LCPWMNKoetPyilUP22fREGwXKUYJPJAaC3jcJU4_GyHPRO4tEBpEijf-8-WSvmwKLYxvDKdzTLyHSYKo_ESNItHCSlkDKoOtcf-UXKbeVAyxkVfilJVax-APDyoOZ-mBGSjzLgWk1h1eyqKId-sSO5ldgPUv6D-EPN2k2nPSPuBysit2gd5J-w_LaHIXMvffj-rwd5f4xs-sFW3ROXmsDvj7PPXO3s-OoLC8dWKB7hNHVxMgnf3d5DVneGV6paRG8IM1ifL9cz-_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP-lQMgU986XnWqs3EXgKfybzdResUOwuh183IT1GZQ-S2Y89AK6wSVrzUtJTxGv48gkUQyG6PWCR_x1YSjy_C7DAzUdLtPcNwlAEuyjU_gUTJbofQgD4guAXNQ6wClOXgxonRIU03I9aB5-4qzww8CU1BB1XqnUvbNUIEmUIqPlIO0yUdZ8wqWT5b2O5Bfaq9lbeXD70KYEssepfMm6Wx8_bVERkPltZFpHNC7AUAE00Dmiy4ybZV_PA2yxbn8IaNZ74ZFFMAjO2ReKUVPR73rIijR1x6SZcWPwLY7dJ8VlGW3luTCHBg0c0jh8HwyQsRDxCLfnwn_TsNrC-R1kTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=SYgT7iQ7pJWpebSaHrkE62x2uACRPRMz-XlJa5tuqIw4DFgeOWrN5slzM5pVNTLQ8Gy3qlbYJfrhQhfNgRPzRqJFGUN8Y0RAN48kk52P4zPBlxSrek8Ny0-BrqGftOKgramc6DYZqvJqyCitSoF5hKRBM1QiPFwzwES7_Fj1jAukuzdh_kWTOVpyWeAvKlTjQrQKYXhRJV2eaxmMuU3nNkX9F1iG15G6cT_7jjr9UNyEMGkjAySc-onPOhAeDAdq8K88vpr-7BfcPwos5OWCV3wFEZ6T-kcqadbxTNd1nmmWk6VGWP_ySY2fxFO4tqr9x6xJTGIBPdBlkW508rn0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=SYgT7iQ7pJWpebSaHrkE62x2uACRPRMz-XlJa5tuqIw4DFgeOWrN5slzM5pVNTLQ8Gy3qlbYJfrhQhfNgRPzRqJFGUN8Y0RAN48kk52P4zPBlxSrek8Ny0-BrqGftOKgramc6DYZqvJqyCitSoF5hKRBM1QiPFwzwES7_Fj1jAukuzdh_kWTOVpyWeAvKlTjQrQKYXhRJV2eaxmMuU3nNkX9F1iG15G6cT_7jjr9UNyEMGkjAySc-onPOhAeDAdq8K88vpr-7BfcPwos5OWCV3wFEZ6T-kcqadbxTNd1nmmWk6VGWP_ySY2fxFO4tqr9x6xJTGIBPdBlkW508rn0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=lfLkYVROC5lLSGREm75qmUmUx_cIM9Wf9ZRDhkRTBy4wZuFihtT-7D9gabpsdozGEw4mPwVX2as21pV3slyHaLrSHMQHwjHBD5UX1n5oo3QrcnVfb9j1umy6AuhQ01M2jl46k6wxkkDI7nfc8qoTG9wyWp-KIrgeHIx8L05U2Paq173JgENuNxeXh_gT14Da5uwTSmESmxiSxpBEu7D3z2XtTLzJfuJfhdxXVlpVO2xdKSSZcbkH0gQyc4IBJRf5UeEQ7JRu9hxLvXOuZyE_3JZe9Y6hh0MmwNDg8hi8toBgNmfPy9BHWbM3XCvTFl9YF5_z6lbSWN5CfF6a3XNyMDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=lfLkYVROC5lLSGREm75qmUmUx_cIM9Wf9ZRDhkRTBy4wZuFihtT-7D9gabpsdozGEw4mPwVX2as21pV3slyHaLrSHMQHwjHBD5UX1n5oo3QrcnVfb9j1umy6AuhQ01M2jl46k6wxkkDI7nfc8qoTG9wyWp-KIrgeHIx8L05U2Paq173JgENuNxeXh_gT14Da5uwTSmESmxiSxpBEu7D3z2XtTLzJfuJfhdxXVlpVO2xdKSSZcbkH0gQyc4IBJRf5UeEQ7JRu9hxLvXOuZyE_3JZe9Y6hh0MmwNDg8hi8toBgNmfPy9BHWbM3XCvTFl9YF5_z6lbSWN5CfF6a3XNyMDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CsUic0PlN1stDvKwc4fHyi6dOCdPNU9HwQuEdzRmWAVzVFY5RnQVLURZrqtIDiDGqGCes47jvjd1gu0r91GhujkXU0bQSOWzxc7G_81oIicH-WgPiYYB9-RJYVxYaN0PDoIBR2wbOhHqw7pUnF3Fodw0IPxJqwoef1k0w-HGtQT22CAlj7R7ClrOc96RUhroKSxUEwQBFa4PiiIhYxbdaL50XukClxCR4ty0VheF8RfWGI_rppI0gWArCOHlyKeIxBBRiQxGvutLOQ_z93t72mTLuLlZ54meOiVdrCvpocVWZ5-IzWtu6ikxBk4nJkKPIji1if-wOpzZBUGeIagG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XhHqhNwn-1HN4hXtCXauwGsKGsJEEuzybpBdJXm9nsdNHLQddnNekBP9stmUe5v6NbRDsEJfcCU-FpvyTrSxcD42wxWO0JK9WIupoWn1RWBltW0SP9_eEjCWVvQkVjiyYde6nsNt2_kREMpIlwTJ8e63VXQ8ZfOxlr058wg2V4tQgoG06qseUz9UzIR9972OvTbY6tSgrvAo2ZJYT4zlLwvq1BaJr1OkXarPu7M1xhFMDro8Z8lMlrQr3vuxbKJpxGZ4ldOa0PE0bQQZ12SAgG48YGQHGPCB5wCYi8K6ZLAhjQbPBXT7Bp3JWx1Z36X9oEDvwNIaaYIQxIulJkEfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSNf-0ZWvkOIpajNBoPcNJ1Y8M7VV5hQ_ZD0CUl9-4VNLAMcu52_yf4TAYxyvzfHo8RqyFFLluwuAHTRgbbOiPJoDHEgqe1qZyEng_wVIQI7j_uEQM1nYSiVJv5c_jQXDC9XIcsMefwL9QjBVGH1WN0rG0VirIrzy60LqcsDz1DbcmXGFQA8zofcNUosn_StSci56A44nHyzV8h5mTVeGSHKucduxJ8DHFuMwxfI1iRUAzSHSr_XgLZBEtyrw-6cr3HKY-Ilq8j820SLRUqcRGAEagmbaytza1I_4j7gAl4OWtQ27XFu58c07-rM86EhBpwzoDAG7ZyJxoaHJMJBMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=A4-gQZLouIZy_mfSkPg3yiKd1YhoHhSWdIfu_gqe1XUS5vQrbrBYyoEDmC7-CTT30kCenjfp2JMw2rPu7kaUQ8rOda_9k0PzloC5n-JQ-kYDfWOlkVU0Vz0tfb9bnIHdd67sQEBE1EXKdV33mVhqXkODjyC2WxSk6hsZSOtTQiOzosSrbPRRguVkYiwO3ntuBtFaH37AC1iPk4bfzBa9t8ZtOzdoM366bOVCI65zlzWMRgwbzxzJ2dsieVqW1YXhJABwXtmFd6aGeD8IvqH1M7mzEbuhIZyj7THZYnbcT1Fb3OF5btMgSDg2qcQgUU6NkGjrOfu-OThh1mP8S3Iz5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=A4-gQZLouIZy_mfSkPg3yiKd1YhoHhSWdIfu_gqe1XUS5vQrbrBYyoEDmC7-CTT30kCenjfp2JMw2rPu7kaUQ8rOda_9k0PzloC5n-JQ-kYDfWOlkVU0Vz0tfb9bnIHdd67sQEBE1EXKdV33mVhqXkODjyC2WxSk6hsZSOtTQiOzosSrbPRRguVkYiwO3ntuBtFaH37AC1iPk4bfzBa9t8ZtOzdoM366bOVCI65zlzWMRgwbzxzJ2dsieVqW1YXhJABwXtmFd6aGeD8IvqH1M7mzEbuhIZyj7THZYnbcT1Fb3OF5btMgSDg2qcQgUU6NkGjrOfu-OThh1mP8S3Iz5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaVe0pS1aUUv4c9gO03Q8F--uaWSiWwiNHd2GwuOcqCSeU5aukgrkEUXQbaGC6ErcNRCc1xPifkqXi7wnKLx48I_rDoblyEgoGDPwR2UNng2abrzXdimevDmzABKEKJ71ju5ONPuSMQJX5QJnCdZY8VCfF_icBEMjn_yftzMdGpKLhkEv_hZZTet3xv4OaHN4BKohxdpoQW6rbifsLAT_xCoAlmjGKpRA1Tb8QOU5MYqjx0wnA5URv4VDQYLnfajatLwbHkPlRGPImwz28tG_W49ITziWt1ydIzkxCTZ_UdH27fS5N17fZW71jFBkdUIvr-nOMvIVrv2pff8wECHtJOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaVe0pS1aUUv4c9gO03Q8F--uaWSiWwiNHd2GwuOcqCSeU5aukgrkEUXQbaGC6ErcNRCc1xPifkqXi7wnKLx48I_rDoblyEgoGDPwR2UNng2abrzXdimevDmzABKEKJ71ju5ONPuSMQJX5QJnCdZY8VCfF_icBEMjn_yftzMdGpKLhkEv_hZZTet3xv4OaHN4BKohxdpoQW6rbifsLAT_xCoAlmjGKpRA1Tb8QOU5MYqjx0wnA5URv4VDQYLnfajatLwbHkPlRGPImwz28tG_W49ITziWt1ydIzkxCTZ_UdH27fS5N17fZW71jFBkdUIvr-nOMvIVrv2pff8wECHtJOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=Gr2vqtDZs907CwvLFRR6hP2oANiNwk5smHUkq5ak1oIMyDmiEJTo448JpEpmmMsSxaw1JiVXfVy8s_0h6sKyA_t0_Yj3PNpdFzPjPGJCcIi91WI0MF93ySGRw9hz7JSu8R6zcCImEwW_7Hnk7N8ygU724EY6WRe5r8Wvlx3ipfuDBjBbI946u5PhaJloL8K4DsPfRw-aC88owkfSsNdgccxd0Ub-u6K-7UllgnBK-s3yutr_dOxwYuvy2T9lc0SlHUm9fOjxfInyOVeLWGuy59Q34NLeQTzPd5Jb6nsoZoIOEtvEYGpKP6_N7zKfqLiY4NFBf2qUrTi9A3KXkEZEYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=Gr2vqtDZs907CwvLFRR6hP2oANiNwk5smHUkq5ak1oIMyDmiEJTo448JpEpmmMsSxaw1JiVXfVy8s_0h6sKyA_t0_Yj3PNpdFzPjPGJCcIi91WI0MF93ySGRw9hz7JSu8R6zcCImEwW_7Hnk7N8ygU724EY6WRe5r8Wvlx3ipfuDBjBbI946u5PhaJloL8K4DsPfRw-aC88owkfSsNdgccxd0Ub-u6K-7UllgnBK-s3yutr_dOxwYuvy2T9lc0SlHUm9fOjxfInyOVeLWGuy59Q34NLeQTzPd5Jb6nsoZoIOEtvEYGpKP6_N7zKfqLiY4NFBf2qUrTi9A3KXkEZEYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMLME0pNs_EX1qqUMKDL4dqJJr9a8Wcnu6XjXImH6BAhjp99z4jnUEJKAvprnbz2B__hgNHZTbvz5RhrYGOLNechrY5I3ZbChh2qDa_Y53KyVkoUZiJfhR8Ou8KA18n2aow64533seDNhTgidZWMA2pzppdQlMUdaGmdpvAeNTLRcJK9XDawxgjRMfoxdanVyrEOhvoCvej5DvRSwXDB8DNGgTSzDAH-CSmClCtjDm45-LScK0De90KixegVmGw6QGi6_fgyok4WC4LMi_vHE7AsbAEjcCr1id57q_EVP1HTsUDdm_0eksQx5gVn3_foXLmY2vZ-JrJSmZHuRuH02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHD5jou3_LsIXSssD6K_QdI_M_LEV80DMVrdYy0r9x-b_w-l6RYstQOujBjkjLxdcktRFh_qHrCK74Con-VTzhlKcIGA4BIJBL9wqHtNXsTmpRyyaAKfrMOaKCgdMuNaw2E_vU5UtNBiiIusCGkUKweukBtmCS3NC061gv10rFIRNsBxogGQqtx0_VVEcuvBuXm92fVUbUB0EKpqQ9fNXzfjz1wLP5ZAVqq5U1BMLK4u8ooEZcniL0OxaoIeEiS8u99QHS2x6mhAGbWrwmbgY5mXhQNkyxfQ5kbdoIIrOlW2_yqw0V3xPPkqisJZcfIpkt0jXopclqfwIqwRsE3cFBmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHD5jou3_LsIXSssD6K_QdI_M_LEV80DMVrdYy0r9x-b_w-l6RYstQOujBjkjLxdcktRFh_qHrCK74Con-VTzhlKcIGA4BIJBL9wqHtNXsTmpRyyaAKfrMOaKCgdMuNaw2E_vU5UtNBiiIusCGkUKweukBtmCS3NC061gv10rFIRNsBxogGQqtx0_VVEcuvBuXm92fVUbUB0EKpqQ9fNXzfjz1wLP5ZAVqq5U1BMLK4u8ooEZcniL0OxaoIeEiS8u99QHS2x6mhAGbWrwmbgY5mXhQNkyxfQ5kbdoIIrOlW2_yqw0V3xPPkqisJZcfIpkt0jXopclqfwIqwRsE3cFBmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAxBRi3_4VVRioYsnpdxF0HSC9LBigQAo6jT6Sy264CrvSXLHCgUKk5VQZZmcmLm_xJXTBTYyaPU7DasV5cqer79zii0q3oMcMYCscT1zrjPZ_2ygIFTutQWcfviUhep30-2_bAdXvWJHoEo8wRLvuS2iS7rtdyThwuMYlnsdOWsnj1nxkrfI8ABmfhu69VDx31uxtXgJVhp07Dg0yieBD34Qq3M1X6NUJ94EGuQrJvk_Bfh0b5S8j9whnqGATFL2Q_bRESIj3MygKk6eG94xxHRH5C0mC31Cb2E6DH8DgoocbgSuqykq7r936y0U3Ubv19XpJgxLzbGErx1piakRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ff5lIIGRtIR0lqW3LBemcn7l_B7-ETU9TnggNhLU7gIJVsvA0bmI88m8JTuid8xpMWUuD86RI2ZUzgffjszGyTYE3hLJyOf6-MDD4VOFh5B3OLtEqNO3EmXeFm-ovkaKK13cFG8vpCwJPnyN2YlOEnQ4bLb1XX4y6z_Jk_2FKTsJfIDCfILlrnoIjDT27i-SaQBEwFThJomXo82-F_r-5OVoJGk0VDsPLUQSsonBJLhweXH5SWV8el6556wvXH-gX1CDpsNBb4zz0_sZJtP_eFfY56jxRX-M6SRfcEL2m25i7CIOZaz8yYIyK1Ai0UoGK1uTb-XtWzmgruNzSSNcXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ff5lIIGRtIR0lqW3LBemcn7l_B7-ETU9TnggNhLU7gIJVsvA0bmI88m8JTuid8xpMWUuD86RI2ZUzgffjszGyTYE3hLJyOf6-MDD4VOFh5B3OLtEqNO3EmXeFm-ovkaKK13cFG8vpCwJPnyN2YlOEnQ4bLb1XX4y6z_Jk_2FKTsJfIDCfILlrnoIjDT27i-SaQBEwFThJomXo82-F_r-5OVoJGk0VDsPLUQSsonBJLhweXH5SWV8el6556wvXH-gX1CDpsNBb4zz0_sZJtP_eFfY56jxRX-M6SRfcEL2m25i7CIOZaz8yYIyK1Ai0UoGK1uTb-XtWzmgruNzSSNcXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=mtXscXsnrCEBUEaF1K13h9aOtX1UCroacEdhKwctYKldjPpb-wuZk4LEHg86Gbokch7fo1wXIglNUG2S0fJf4sJBWOzHFV6IeBf0tJLfRvTezwmsx_OQeHwQXFazTK9JHK9y51RNZACtkPcN-6rsfv5QTOHg7LE9AkGZp-sQWAkAcb8UfV9B9r-tkLom8toxvQ-momL6Y1OnQIMUdtUm8Y0RdOgKDV6Yrko15iJsTYDgNu56gXA0T13M4St8CcIIAmVA7TfxlAzBJL7Fc--RtIigMZO00tf-cvqdeAz0zVvQYH8q6zmiN4l4DoytAI1wNHg_fWAl3bQgkLgn6xNdPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=mtXscXsnrCEBUEaF1K13h9aOtX1UCroacEdhKwctYKldjPpb-wuZk4LEHg86Gbokch7fo1wXIglNUG2S0fJf4sJBWOzHFV6IeBf0tJLfRvTezwmsx_OQeHwQXFazTK9JHK9y51RNZACtkPcN-6rsfv5QTOHg7LE9AkGZp-sQWAkAcb8UfV9B9r-tkLom8toxvQ-momL6Y1OnQIMUdtUm8Y0RdOgKDV6Yrko15iJsTYDgNu56gXA0T13M4St8CcIIAmVA7TfxlAzBJL7Fc--RtIigMZO00tf-cvqdeAz0zVvQYH8q6zmiN4l4DoytAI1wNHg_fWAl3bQgkLgn6xNdPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=gb5DFQubA1XqpDeSzDuZ-ChOVkJUG9YWKGq7Qaet4oG2o8RTcMIQu2rJTFv6YrmTfQD580R6yrjhwRtPsumFd6y9iE2i-uBn41wrdHXmJLof0e7NKg9_074PIt8VcdjdTw7H1sdhhSBR0J76pkrBt-1hhJIDabmiX8AMXesgozHMHd5_HkpL5z6T_RdxfsM7jOZ8ZfzdYeHxt_vYqh1_WNavcvFuqS6E0pQKdrOUaCJNTZ_iG0CuLSOkgQQeqaCF0hgMp02-iRypMPqsmhIuo-3jCwJP2OlvgFnrnRfg_jMChkaMUBoebcoZFdfAavD9EaZ9MBrMpuULJrgwguNCPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=gb5DFQubA1XqpDeSzDuZ-ChOVkJUG9YWKGq7Qaet4oG2o8RTcMIQu2rJTFv6YrmTfQD580R6yrjhwRtPsumFd6y9iE2i-uBn41wrdHXmJLof0e7NKg9_074PIt8VcdjdTw7H1sdhhSBR0J76pkrBt-1hhJIDabmiX8AMXesgozHMHd5_HkpL5z6T_RdxfsM7jOZ8ZfzdYeHxt_vYqh1_WNavcvFuqS6E0pQKdrOUaCJNTZ_iG0CuLSOkgQQeqaCF0hgMp02-iRypMPqsmhIuo-3jCwJP2OlvgFnrnRfg_jMChkaMUBoebcoZFdfAavD9EaZ9MBrMpuULJrgwguNCPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoA0IELtcFcTzTgnHpufadDnF2GBow1vaB0vn4nB_lJvjcPLI0WKQKie3H94l2miHqrb_Dp8yU1fnyQCBqq-rs55ywq8263_Aakw3DpfzyvWIbp4mOE_iOTTWGAQDfbn9g_cTIhLgMMZsvKa0-A4Fd_nOU5oVrplpapRlbPQcz5NjC-y00fxAdu9OeQBq6hGR4C0sszbfEPyTRsomX7e_Ztopz4two0HWO3x0ww-n-cHafK3l8pFKpguU4DMYtU3a6Ks08hzGgPDXzwQiVcKz0_TVydAHCRo2uumvvddD68dTpXC8bPslh5tbcxGhCZaK7BC_l0ehZ4rQgP4MkgxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy4iTxTXQWzzyjJJX_GBRwrXbdXWWEnsy4v5QP-jZtqyy0Fku_kVk2UVQl_hDmFtMH_qSejlCyujKSYBU-pl_f3FRsyxizKDNd6zzfdiltNfF2WW3eRgX1_CNCoAc5yHWrDGfEPuKBYuou-ZSEsozuFQqvbR5UrfTj2FavzuUAqic8jqFSV54yxIKAtcWF5O7l5J86owLAP4r9t-DP3DwYwRBCY1V_dKob-R5ke9y2jLH1-ksbhW9YDQ2xg4GnxjmDbDnI_PY6AUeNZANLQb4fkyJQ0jT9duT_JHDmTmkzA-EUZ6e8d2jLH4Nju6CjtRwQTwvodVnfKom3g4g65tCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=XIaaPeDR0RA9CWe8J2TDbw_s0ahAF3HwX8-2PwQLng9cMIrI0xb7pWdGShdYKI9k7rUNtGZVIiUxHoxY1iF9ibzZWtv5Nm2vgINHd2yL5VS0BCHUGS_rgOdDly2r5GluXekDzA39Kp8SrzUc4i3saRQ_7uM4y-cfVz3eXjoCZWFgDvnsoOR1JWcf9pORBLlpegbCuYXMx5ZDsxTLmd0w3bXYq9u03ZWuI8oPmnMnMVRbSjaacKAGHGQSWaK1DudOU499RH7calJTnlB0sMW29tjBzfyE8TE6zgF--wGa3FE1dhG_BmDxNjyEbT2G8OpgI8BvnjMgh2-RWij708cgWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=XIaaPeDR0RA9CWe8J2TDbw_s0ahAF3HwX8-2PwQLng9cMIrI0xb7pWdGShdYKI9k7rUNtGZVIiUxHoxY1iF9ibzZWtv5Nm2vgINHd2yL5VS0BCHUGS_rgOdDly2r5GluXekDzA39Kp8SrzUc4i3saRQ_7uM4y-cfVz3eXjoCZWFgDvnsoOR1JWcf9pORBLlpegbCuYXMx5ZDsxTLmd0w3bXYq9u03ZWuI8oPmnMnMVRbSjaacKAGHGQSWaK1DudOU499RH7calJTnlB0sMW29tjBzfyE8TE6zgF--wGa3FE1dhG_BmDxNjyEbT2G8OpgI8BvnjMgh2-RWij708cgWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzRrda4GFH5gmecKNJPWg8u6vik21HKnIY6IegsyFm1KHO-UXa1oZdsHTh9aBgZAYjCZ-iSuYEezW83t__TBLJbGfKrsZqFf2aRYVsFl1z9KfHP7tcoFHaYziWLHdYcrA6xfa3GOTyqBT0m9wScezREpImHSOwXlj0mQ5m6LOfRBo6L8sFMiVBHbJ8UdkCeThWMZBkY2YX2YdGHAiw7BjwmuZ_CnD7ClnrojZNByeFQyJ8sOQp7a_DNgveclmiUJW5bSpzFZeicuqFN4_tt3w7uMAqHIx2dY_R-RkbgEiZ3ikpcy3g-6Lavd0W9XwKKhyIkIpyzLbZGOA8rKamTQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouY78m9gyNCfD3aEx7A-lJL93mGBOJYsKcdtsYnvjEuzNJc1fK34UWnENdd7ziiRej70_7WyQI0Mv3dibcy4vNsj2wlfY6LpPvfmUGo2fxfFEXvqeXmvraK4rX2aYhDrNW5SpEQFUVw66VfD0i9ItsLluAZxJw_Dgk_805IuWgEaLaZAZhD7aY-MB5LeJUO9So7dAYybqQ6G4CPuMshwFsOiSD11O1p7ReL_PbaVJ7heqOBOrb7bQKXZ4xuP0c2-4FySgDx0mTS1NGxZbRCnz5hliIWu0_4ibObRLrd209IhsGansNqrScnEF9UjCQW6udSGaOVs-wzxuO0uL4O0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=aa5ghvlJo61NGw_zoHqZoSabA4rB6mBtWUL34Bql3bTOM0nMtaU5njiOD-62l-c2UzBy4wcINlLSITXPqJQ_O3_Y1Z3VppxiB8N2Wz-EOQw3d4NzJ12fis9bJrdbedEpyH0NYCLefawT2r0I7Vw-H6vKj-fxDpap4D_49kx0lO5BCoDOR-oSOOwcJVvRop8tBzvTRZsxT7sfNiyq6_d59LI_tesW7LSIDv_--WjrvEMLcYV2jldru-Riw03RDueXmhoTj_U3vxrK_GtFLJKvBxrCStNUHrhnJ2eBEbi_LXrpXV2tEOEWzfeNZYTj74f0kvsAF2dYPBLCOiZujCDwMi1lp_01MHjrkeKlW88ze5KSnwaMugeJG9sg-G9PyspwsUDhix7D79bltw3iPdUgt_zrBmgrvdpbuzrLOG6ox6wJkNvIQLZgWmjZBxDljyvNHwfxXsNyIS6dEgBCErQHJDqDTktgyglr3JrlQFvUBVaOe1lPdrayJ0zRfLCj4g6SHOe-8CG4HYXm2goM0PcGY0b2HyRXAqpJaJAgniQbZFBBHbryQMNUsuc9zcEOa_myTCxsf4gORWRccqnC8eH9oMD8IAKq8VWe3Yvt0qlBdpC4AiJF8iNBwwJ-LGlB6p0Jc6ph9p3EQGSTJUUWRWjG8l-GH4pmyW71GrRC7y-mQyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=aa5ghvlJo61NGw_zoHqZoSabA4rB6mBtWUL34Bql3bTOM0nMtaU5njiOD-62l-c2UzBy4wcINlLSITXPqJQ_O3_Y1Z3VppxiB8N2Wz-EOQw3d4NzJ12fis9bJrdbedEpyH0NYCLefawT2r0I7Vw-H6vKj-fxDpap4D_49kx0lO5BCoDOR-oSOOwcJVvRop8tBzvTRZsxT7sfNiyq6_d59LI_tesW7LSIDv_--WjrvEMLcYV2jldru-Riw03RDueXmhoTj_U3vxrK_GtFLJKvBxrCStNUHrhnJ2eBEbi_LXrpXV2tEOEWzfeNZYTj74f0kvsAF2dYPBLCOiZujCDwMi1lp_01MHjrkeKlW88ze5KSnwaMugeJG9sg-G9PyspwsUDhix7D79bltw3iPdUgt_zrBmgrvdpbuzrLOG6ox6wJkNvIQLZgWmjZBxDljyvNHwfxXsNyIS6dEgBCErQHJDqDTktgyglr3JrlQFvUBVaOe1lPdrayJ0zRfLCj4g6SHOe-8CG4HYXm2goM0PcGY0b2HyRXAqpJaJAgniQbZFBBHbryQMNUsuc9zcEOa_myTCxsf4gORWRccqnC8eH9oMD8IAKq8VWe3Yvt0qlBdpC4AiJF8iNBwwJ-LGlB6p0Jc6ph9p3EQGSTJUUWRWjG8l-GH4pmyW71GrRC7y-mQyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6wFYnyJQLm79OGMZDbPRgzW-e4nSjGbaprx4u5442o9JIe9Tk-W1N15JO5C8lOTTRosuFVY7dhh4pmra8oOa7QRGEniF_IDlqfTj0npJCbPa5GPa_aaOMjzJQSTokXUwG6Krol7qHGjxoMB-PTEwHbENCNQ5xj5wYa8yYr7WgElU50QOfAf2n-5aIjFtb_EVW3zlfwM7vs9oLRAyteizq48rNmo8GYNEOaczNrhaKcqNrQjKaVbzfsVN1-S1gyroRTkiAP9br2EDaE3VTx6DnDl8zA98NqtKHz2whjqzle4HvhAvME0ZNKFamcPy2ndBkAl879ZKZ8ZQmYR8Mz9ysTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6wFYnyJQLm79OGMZDbPRgzW-e4nSjGbaprx4u5442o9JIe9Tk-W1N15JO5C8lOTTRosuFVY7dhh4pmra8oOa7QRGEniF_IDlqfTj0npJCbPa5GPa_aaOMjzJQSTokXUwG6Krol7qHGjxoMB-PTEwHbENCNQ5xj5wYa8yYr7WgElU50QOfAf2n-5aIjFtb_EVW3zlfwM7vs9oLRAyteizq48rNmo8GYNEOaczNrhaKcqNrQjKaVbzfsVN1-S1gyroRTkiAP9br2EDaE3VTx6DnDl8zA98NqtKHz2whjqzle4HvhAvME0ZNKFamcPy2ndBkAl879ZKZ8ZQmYR8Mz9ysTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=uCpH4Oh2niGc4YnNP1OZiyboSqwXi63QVV9VjSIe1ei3MSL1i7AAiMxEwT4mCkN76LRIUoEXTUXEY3CGX7BDD1OmC6LrWWZje2m6RD4itVzISVVhcPBBVJKeC_qgezibkhFbpEfiJgNHuG1RBiOl4rIcCfSaGQ9t562Lz3UY09dHX8hozltBS66U8njFJ9rJ0TfWmYxd8m9uCn1X8e6ztwZJ-LpRToYmW6OqWeyOJGr4kDdvcpzAP1PtVV5ypd0h44934k8eEkJGyXvluR9Re9HGRTC5hRrWEi7nHiy0TynxksPSN5v95pCaRYMjn1sNnNVCI00h6ZhDbCdO2nQQA4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=uCpH4Oh2niGc4YnNP1OZiyboSqwXi63QVV9VjSIe1ei3MSL1i7AAiMxEwT4mCkN76LRIUoEXTUXEY3CGX7BDD1OmC6LrWWZje2m6RD4itVzISVVhcPBBVJKeC_qgezibkhFbpEfiJgNHuG1RBiOl4rIcCfSaGQ9t562Lz3UY09dHX8hozltBS66U8njFJ9rJ0TfWmYxd8m9uCn1X8e6ztwZJ-LpRToYmW6OqWeyOJGr4kDdvcpzAP1PtVV5ypd0h44934k8eEkJGyXvluR9Re9HGRTC5hRrWEi7nHiy0TynxksPSN5v95pCaRYMjn1sNnNVCI00h6ZhDbCdO2nQQA4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=P4NEVX6zpCyatZvBJWvPmtAZDbvh-f9Z9Od0WVx0LTTLPuzXgpArcGzI1SFgivywrycBILORksxTEHLuvvC-PVKOTtICLSHUve2J7xmPRr0TYGEcQA9pCP1Au8nyVby1D9Tt7x7LaBLWAtZf8IOsW4m8VHTf8usRhkyL1oSRYZIc6XFNZbu69qoRna8G4KvKeX55hjMRr1PxB2znQcWoHamzjKv3uiBMt4tCUHhHctBFgShu0cnCqkhOLTFa8VLDztz8d1TvTuNVWF4WWNX76UWF4s9XNZNRgv8b1jb_hTDFgBrQ7Ksa1Bt9c67J3z3EKjlysgTt8a7ErDy3PSr7Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=P4NEVX6zpCyatZvBJWvPmtAZDbvh-f9Z9Od0WVx0LTTLPuzXgpArcGzI1SFgivywrycBILORksxTEHLuvvC-PVKOTtICLSHUve2J7xmPRr0TYGEcQA9pCP1Au8nyVby1D9Tt7x7LaBLWAtZf8IOsW4m8VHTf8usRhkyL1oSRYZIc6XFNZbu69qoRna8G4KvKeX55hjMRr1PxB2znQcWoHamzjKv3uiBMt4tCUHhHctBFgShu0cnCqkhOLTFa8VLDztz8d1TvTuNVWF4WWNX76UWF4s9XNZNRgv8b1jb_hTDFgBrQ7Ksa1Bt9c67J3z3EKjlysgTt8a7ErDy3PSr7Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rbmyj2ObowkJpuNbp5uM2EkotjwG3WLxV0_31inYfZoUFhdDbgWHrZSi4mZ7DxxtPEEju7Uh93j2UE7dwhyqWo5tadCcz2T1Zvzwk6QA44YghoODZPJjnFfS4ycpPoE4aFN2ddVF7eZdsSvQQpwMe1SN7YNZ5phGiHNKclFh3lzkPGkxtqfcXs0IYAujl876ma9zy6gUSu9vcFcGnvG4DPb_bbI4axjEXX-XhE4mHVOvh-Yuj_yfRbrza69O720aqDgHstL4hFNxGQGPi_yUemVrCCI8nr29PejukjzremqkuDhAfSm-n8eUTv5SZYaRa-BfChYCBZz2AkvZeq-5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3ySjWEltb08TujwWzxHxqnxTOSNWiRUbz4xFjWcS3sM0dV4id0qy9YNV0GXP_1A3lwhrubcrrASgcK5nFR4ptQaPXg3Dj02_Teckf59_hvnciUr2Cr5mdG3zKmhtIhFSz1b58miw8BWFbclr_p31jJkpdnnQhCA0cMGa2JorYAdxzp-MRB_bZOMTDNlhqvmRQuEvr4ailtqRVKRWQSmJbZ8UL7z-wkqvyk5uuym-nRw6pSxiYFZFUScIMlcYisj0IUJ7DEQpHLojtvKW1_geiudNrxNXqgnv36UJdU_8E4nYKQv0MPZUji8AanL6mchSt0jVrwhyjlNpSNX8nqSiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1TVg7cCAbE5elqJrXYYeJ9ZL0ahLg-Ni2pZrEohWrkYmI7YH-z80ChvVRUWXnS3v0ikL5nJGqzOHJa8lMBvODNAoHxX6tV0vBkiceXbkXjHfDvOI7Ao42OYVpSwKcpDbZKTKvst7r13fEVRKDrw9Oq1XMmopgdO1ZqQkqVOwC9UIuUrYtuKiLg3KsDgvZBqfbX5ILRuiuu9JY2A3whEimipAlOTBJIPCaoHTRjtCMd_snLFzpbF2jA-cyNIeIm3zWN2Duf-fz7G6FBhtZVdRiK2h4AdseBh-yo71C8LGC0Khb7ja7shbQn8Je260ZPZDaY6Olz1taq6ipHj7lCUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtrABdJe8Vp-7AjY23UBUm3bwlFoliq9APVcVjyTa-lv3YWU0L7FnwRSlKL9WKI5JyVWTcTVwLjH0pQxebc1cIKcOhTYnvDIUoFhKCrsLfa1xfe2vAY_nUHCtsMY2VbHW8dhvy17jGCENMXgFFJoq2o0mSHbV8cb5VZoYxf-fC3MIlDUyGhULCcgT0Su_h7CCXslaBrark-o5suH0JZMMVAM8dhUeEirDtZkVss-HQ6mbvVUE5TgWirFF9hCtPyW7YTS71WBc5H9sGC-zR6IKrlgkHy7wxIPmYMOGVxPjq3OaQqIBgIfHD7ENWK-fNch6uLslGEWEAWXlaW9sd-_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3TU-5bSLebKn8lqQhCjgo0i0fnlzxFH3jTkWa00p8_Q9VZ7OuCLbg8grahZzmYfjIkaQUdK_7dnISuIQNUDg6WfyLUCGBL_29qwi059Pice4BJsUL7mUsDxQ0n42VrtXluJxrQGzpX6SRNYw5PzXFXSUQYt_bItzl0kTTA8ZAtZuZU0PYxCI_dvwJ3w-e9vqjGpSrGkGdVQMhMVTAqDvObEd0zI15s76Nid9O-AePqtDI3ra-Ripo8ZFALKyJtZc4eNcDBED8mygo0RwOhxTWx-e5aItbhlv-HjABZzJr8UwEYumVkqU7OS7YIXHEGwXNpN_7N1eSlnUZ-nDNcLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=ltQRYv_ORMrqLEX4IHi9yk4m5nvi4VQ-eYcX9A8LrPjQ7gDoLmaQMR04PohTHkzqVt_NX2psdmpRQGAqpM8uOpfw_qLnYTNdcaTHIAOGSmCt-qc2bnrK_b7d7JBloWxn1IZQKwjOZ70SwbbDni6KJSrIa1rqRhnYixFJ0KgQJmet9hrOdkoEiRZyR4iyEYDJs03cVRMNgcqdTG9HkkMP2vuVvMXusGiLFecbszcz38d4Op4oSlVdEMV0hYHZqe1oWgMm2UqBkKG8KNhKthSqbSqUcClRhYM3JbV47eP86B-3Wn_j4f0s35N-E8k0inlZoxVyY_waTNMD3pP53I41ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=ltQRYv_ORMrqLEX4IHi9yk4m5nvi4VQ-eYcX9A8LrPjQ7gDoLmaQMR04PohTHkzqVt_NX2psdmpRQGAqpM8uOpfw_qLnYTNdcaTHIAOGSmCt-qc2bnrK_b7d7JBloWxn1IZQKwjOZ70SwbbDni6KJSrIa1rqRhnYixFJ0KgQJmet9hrOdkoEiRZyR4iyEYDJs03cVRMNgcqdTG9HkkMP2vuVvMXusGiLFecbszcz38d4Op4oSlVdEMV0hYHZqe1oWgMm2UqBkKG8KNhKthSqbSqUcClRhYM3JbV47eP86B-3Wn_j4f0s35N-E8k0inlZoxVyY_waTNMD3pP53I41ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=mVymug-k77kPe02jGC5G_Z0Eo7dTbhMQYdIuIBKipjShLQZ9ByBHlFXu-WcfDG3acPMWWrdJBjLaajKv-a1vUMOjq5HL6FKAD8lZUwejXtu_B7ZFZtqja_Kt_vbdXVbtiiB7ytVYQz7DPCPaTvydJ0e9Vi_5GNyxdbb3-dlKunHBbmeSstExD1mvHk4U3qI738WC84JwguAEcK7Ymq1m8K0WIIhQgK5xL1hVZbGTtERgvvJrS5SQeJbokrHmOMA1mxVWdAA9e6TSsFn73fw0gDonAjLTtGwTQPiBzp0PMz1LeY5fUjZUBCBW9zoLki2s3WHgIUFpXZ06jHIhnM4eRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=mVymug-k77kPe02jGC5G_Z0Eo7dTbhMQYdIuIBKipjShLQZ9ByBHlFXu-WcfDG3acPMWWrdJBjLaajKv-a1vUMOjq5HL6FKAD8lZUwejXtu_B7ZFZtqja_Kt_vbdXVbtiiB7ytVYQz7DPCPaTvydJ0e9Vi_5GNyxdbb3-dlKunHBbmeSstExD1mvHk4U3qI738WC84JwguAEcK7Ymq1m8K0WIIhQgK5xL1hVZbGTtERgvvJrS5SQeJbokrHmOMA1mxVWdAA9e6TSsFn73fw0gDonAjLTtGwTQPiBzp0PMz1LeY5fUjZUBCBW9zoLki2s3WHgIUFpXZ06jHIhnM4eRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFFOnVv6ckN_GFOxs10HxcwmOzTz8Rs2_tull4l66UpyFTiVHcZKuyf4ZsSadz5l7K2SlFH8VhsNjb7y8GK7eKeJCVcO6dBj3cze_6z71cPnmu249mRMlzpBgyWULSUVbUw2QOS7A5tXrTB4SInFixhRUKVB6N4oXVVhIY3_odUZoxnEjQvdYUN6okDMEguVwlgS3nwPUUg0k4c_eHuXc9mXDuerIp7DUC3MyQR0ToCvOAYImX_g14gbCqGfoayiG4HqXp2j4QKJz_GcHwn863e_FPpPcdjcPDdbKm25q5HCGhMg4Vnq4JPCSrfgNX865dn9CZFAy4w5Ji7xVwlvJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bs5xVGxJmd4QVB7-NIG--3l1yw_v_Xicieai5Z88sJ1T0HOd1BbuK6UrBdDngh8XJ1nMBk2mVw8VlF7fotYnWG8XdVXiyio3a8PKrmH4pybwWZcYTYXZlU_PHZw2uDdAQ3ysPIbuQ1D_N99FADZ3rkjC_tb-2OATjRVtctP4Jn9xGKXz4iHs675696ezVs4kzKGYQdGTI0rT2kSmrU507sQ9NYHxNiwK-jFw3hiEd9o0IUqkM4kwjNj9Wi4S_CImnZJ24PJp0CZ0SgvoMr-599cegz8pyW2eRZBudKzZe5aLAF0XQ81bOzS5iwxnQoLXr36RlzIx3WtWHkf0NRBHug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=Lx_Z92pyBtk0Thh1EO2xOEPmmer-rSaUY-z1UTjGe5NzBzLb75jMJSUyyKxGphX5nZsKRQM7MZXdR8ise6i1fP5rKCYITH3iLMsWfH_u0lCVMSkx7ALhJW49tqVcD1pYcL6e5ensRo9qc_nwRTXbskDKE36ksVWTrObR7OBqOq4kQOBY7-lQXZKe5d2QeIwxnBiXfUwzlKkevICsUDMuPo_4HP-aSKyUk_7NpSA4g6Od-OzO-8jHmAjoMXSYi73V0tWox-5LOX20lWqwFy7uZNGOWOeisTYnwfMHAkQS-KFiMYnz0MXdAL5txwLFDrD9v2-xTtqRPCCumzJQTMcaww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=Lx_Z92pyBtk0Thh1EO2xOEPmmer-rSaUY-z1UTjGe5NzBzLb75jMJSUyyKxGphX5nZsKRQM7MZXdR8ise6i1fP5rKCYITH3iLMsWfH_u0lCVMSkx7ALhJW49tqVcD1pYcL6e5ensRo9qc_nwRTXbskDKE36ksVWTrObR7OBqOq4kQOBY7-lQXZKe5d2QeIwxnBiXfUwzlKkevICsUDMuPo_4HP-aSKyUk_7NpSA4g6Od-OzO-8jHmAjoMXSYi73V0tWox-5LOX20lWqwFy7uZNGOWOeisTYnwfMHAkQS-KFiMYnz0MXdAL5txwLFDrD9v2-xTtqRPCCumzJQTMcaww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=nshPdgCrizlQTh8uf-uDzMLo9m3jOgNbDMyG9tsMag4_fBvxqucxRwoX2mjByQPij-IZLnDtAqLFSfyH0UF6CGuHVoR1NQpfAKA1cpT6e5k_PMuLtSJvHXMvy67pP2lsZPWvDHZKjJ_vNmpvN_rUZ6KEeG-mMor37Q3g_NY6ZmRm-0H-DGKXLQDwkTyGnvepObb5XzyYBRhZRKAQ3nmRSfaVyvExMAmBcgP9VFV6O-4hfHwbUgsL1v4QTSYOLHzcCx46lKmf-gQ7xwwXCk3YsZM5rMNN51kMxVGCzhUuluH8PgZKPV8PjO278ELvQ5kp6SrvJwLHvyGT2vF-Eigp-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=nshPdgCrizlQTh8uf-uDzMLo9m3jOgNbDMyG9tsMag4_fBvxqucxRwoX2mjByQPij-IZLnDtAqLFSfyH0UF6CGuHVoR1NQpfAKA1cpT6e5k_PMuLtSJvHXMvy67pP2lsZPWvDHZKjJ_vNmpvN_rUZ6KEeG-mMor37Q3g_NY6ZmRm-0H-DGKXLQDwkTyGnvepObb5XzyYBRhZRKAQ3nmRSfaVyvExMAmBcgP9VFV6O-4hfHwbUgsL1v4QTSYOLHzcCx46lKmf-gQ7xwwXCk3YsZM5rMNN51kMxVGCzhUuluH8PgZKPV8PjO278ELvQ5kp6SrvJwLHvyGT2vF-Eigp-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTkdjwE4iIApFuV0rFb5KZJJA_M6NeLiOoNCLgmZa9URq7WT0WIoU5qmkrDMR9NcvN2ChdwEIXn4eseWFEIsdHDWcvggxgsICg8dnWZe288Eo2MwSSB08OZy2EhVgudL7TYkUjMtF4R0zftXS_QjLO5liEgjNiQby4DiJanjuO36Kxa7fb8BiLbjonMdM6X3_6G_ba0hoPexmgJYVEyKKi98F9a3nR_L57Rv28712jreQQvrwHyDS1q2uQZIzZxBpPjhyOlBE3pgqlZ6XSHKM-1S79tTRGu0hWiZGmS-Vn2-9gvEDAb4y27npTudM1XRCbuk1y2TJaiOGRVhaXChwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpJsyTvvvJn5Ja5MErawIJAVyO0htVoDOpOnjyrSsWMjtpihytPHoENU0aMRWDkCpoMFZYSrDmBzQoBNh704BjbbVniKbe35O-7y3CkcnxDliOsc0MbZBpxLpxVNXYgXXgqm7nHabuG_IHBaZMVvS03-38BJ6049pZEDPgdvRGFVDz2792c1Wa0HlUzqqgTmsZ6SI5RcGoeDUp0qyPDZg0QWo81LLcgcND_Vq34HHn0zeb0q4ic367mRuSI7S6VsNTknmCbDre5MeqmSpC6QmrVlLfNui60w8ICRW_8dK7WVhR5uofHtiu6Jn6pgfpJ3j19Y_4uJKC5f4H5pbJ7HLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZX-vzeGtO2s3GHxecZpqvIKWRWBp7mvfDKVrcAWjaJ97HnWbEOKslYXVUlJku-z8mRlW92f5JiAbTgVcEKtwJMN_Msqum1CjyYEu5e4zpnn09dEnvZ4TUjeXwFq_pI_i6MKA1NyRRg4gQYqqMVW5WKCzzMbxYSjntMwH7dD_HpR5CncAdsu0MXpd-PGV5ljuUmyZY4vck03_kt5u0qalah4ylDFTkGnebc7v2aiOvJSbSpZSSvc3QS4T_X4joGw1wqUEis111y8pEXBAfzENZrorMSzzpZehYE92eIyK8oTn3Op_8wHsR3yM_PVhDdEzP6UFz8hmscnRnrbrW5LORg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=PURdN4O8h6XosjAus7nAVsw7YRHJD-Eumtkm6xirClaR4YKVxPpRv12ZAx9oHQri6d4ahEFJCScOAiVWDfKN20Fz4l9VExTvR4JJIv7rLdotYhYd4yvllYqT430_6Oq04KTpnjtsoFkqHjUEyhtC2Mmq7j1P3AW0R7W2O-ecBddiKnoSRdozpY5lvSIX8jaGgQWQb0IasvZ0adp76RKRtwFxEdmhKUHf5ic78HlXoZ6fyw4qomCG93bNvFIuDFlABWyb043iSp1kEacU9LTdR2q3OF1etEukKNS2qg2i2Zuf9yCHBRTruaYZKx3XrlvmfEhhMwNUA1IxfLpPUpH-tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=PURdN4O8h6XosjAus7nAVsw7YRHJD-Eumtkm6xirClaR4YKVxPpRv12ZAx9oHQri6d4ahEFJCScOAiVWDfKN20Fz4l9VExTvR4JJIv7rLdotYhYd4yvllYqT430_6Oq04KTpnjtsoFkqHjUEyhtC2Mmq7j1P3AW0R7W2O-ecBddiKnoSRdozpY5lvSIX8jaGgQWQb0IasvZ0adp76RKRtwFxEdmhKUHf5ic78HlXoZ6fyw4qomCG93bNvFIuDFlABWyb043iSp1kEacU9LTdR2q3OF1etEukKNS2qg2i2Zuf9yCHBRTruaYZKx3XrlvmfEhhMwNUA1IxfLpPUpH-tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDzuECe5sG0nFYT4pxx3rty7rwaXBZfaolsUIOg2eDuGufMxPwWuB9q_8vz1K5V_OncOlxPG2cR_kJGOedHDOxQJkvUjNDw-MhjedfGg8FqpHgrE4B8UMJ166Smdoea4L1r0Twh8xRS2sJDhns8fn9RAyKPN1X9AVBPeQiRpi4Tkc71r5e1I9H_AKxB_3-j_q5W5FAtBGx9tUgeF95jhO8Cy9sJ4V_Yb4o5w9wwfRDjjgGQhryTfU4peNM9bDFENbeetD5mUeG3bJeDpKv5V01HO2BvsxTBc76e9-STn2Z_iVOkBJoo_ezYn8lRMpApIjyCw8d8oDIvzJBJm6uIF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCwV9JOVZjoFzDLLofMaEQxFHQjq_6Ic5d-4HBMG088a2f6RgEGOe8EtmCcinwB0rcCubgjRXmAFWOF9FJ2jjlengSOSEXuJsuCyG1dxNc1kIdinHj2oQqqH6_TeBxXa8RpCu6sNmnEmM3N9MCkGO_hvrKcEpR0vJ54CTuxwtolDq7eeXkMFf638t6g549dxOEQfFle_iNPtB1Cjd5WKo-irH48uRYQVJADNak1wZE3gzBf7fhHC8Q9i07TiQldKKXm91LI1fDQlXAfwN4-sDBYbhmegacACdxAKBngMZbDcZ-fa2RMqnQJPU0JPmWDrfSOS9Z0pAqPT_Ga5qBPVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaZlirMNItmKC-G69OM_0UCYAl7N7Kzc2HmomOc7aTL8DiAWgGpGQauXR6bwsiWWcxLktgyQgJtD8c619a8ZQfYiye6cvXQFoLxkKgVm5wN0PTcQCCITUMxfTzSw_Q4pyuD-towdP-RxguyonYf3ATAftptdE2jywzMuW1GE7Gp616ClndWhgcySdS-4s2xWkQXc2qSXZN88P8t1uFIUBw9jonl-w_BKMaxrVOimM4leRj8TXCtoxDpysU3zcz-c23BpOV8ecbxX31MEJbowWTI3kU8K8J6_LbAxvY4Rvr06vfFLgvMbHRhEC71CREjDaqvdHRkQaiFKxzJPxOd4rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh_-lTMkLfviY1ZmpcvU95DyCrMZpaIFJDXfRQ-dooI8xSZDbFco3qEK0N9-1xvBiZGU3opjXJI7JbZISVgo4v4q_Rm5JD9rosX95p-D9a6hoj87xeyqbYQfvh24caTKzv72G4CJyrZz_AQtp0afAmDKKc9NMLTVi7AYkePH55fr3RzpzZE1d-WcsEHe3O4-44NoHkkG1Ro85rgl_0EzkvWRIuuxZAGiyh11-rEgQPIHlcJO2PZqH28GT5hD-F2YpngeqlW2o7qvZNI4FbZMAfqWzbNdnLnX5MJNA7IR05bKYsXoUstcxuuu98KOb2Y3Vx9_9Iky49KOy6nkjZX3Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=X8y8sCJDEICuSeJUheWmm7PHg0L6jnM1oFd8ILBbZn234gPwKADbsdqyEx0U5vsB5afGv2gKTKVLa2ZZft1td7Mb6OzJy22d3JQnUxPZ3gcMt_-wD2c56Fp_ZpgD6gCXnPvDJgBnvuzGF9S1KIGBggxmf3eoTfHG0CyOQyv7m_pppVgTX9awa5EKi8F-ME_FahF_Tk0jXmxDz5i0tFDEt09CwFU4ef8qO4E4-Y7P0EtiQ58xfhM5pHMf5CscCQ-uEtK0mscrmYx255wJVs-YcBZ6WN-PujzYosFkvzT3-AJRRpjKqPxDOz76tRIE0FrHEdi5YT8kYsbVdv4p947B-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=X8y8sCJDEICuSeJUheWmm7PHg0L6jnM1oFd8ILBbZn234gPwKADbsdqyEx0U5vsB5afGv2gKTKVLa2ZZft1td7Mb6OzJy22d3JQnUxPZ3gcMt_-wD2c56Fp_ZpgD6gCXnPvDJgBnvuzGF9S1KIGBggxmf3eoTfHG0CyOQyv7m_pppVgTX9awa5EKi8F-ME_FahF_Tk0jXmxDz5i0tFDEt09CwFU4ef8qO4E4-Y7P0EtiQ58xfhM5pHMf5CscCQ-uEtK0mscrmYx255wJVs-YcBZ6WN-PujzYosFkvzT3-AJRRpjKqPxDOz76tRIE0FrHEdi5YT8kYsbVdv4p947B-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-9x-FutFksDs2pCqLBNGKiPfW0aMsYA2jNq8w1qikaSUq1qZ1X3DUKCgTtAWCpy3agzADh59cdw1TXFXrPasewiMywE71Kp_JHzkplY0dAHokP-CP_0bnWhONoHdLVQS3OAtTDAW25Akq74i76ofiOFqa-SG3Skeef90Dg6nw5tvP8_7OiifWQ4Iy1erlAjhTgyCOIAUyTn-GYFcQZiIKR-Im67SLt6j_EYxP1e3I4FVzrCvUoaTsZpWlhBRMx4zX_Sqsbalby7YNAc4CW1qiQHYpHmPau6gPB22ENARKG4G4HEDDfyP0iP7RQTMyzgFcbScFMDjAo7H2s8T29MMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu3Eg9vfW8cwAIkHipIZNl8NXyQBpwFcSSNJajibRokPTbEcv-NSmnAzs358WJC2x4Upz6lTQkpzFZ_ucW1fR5SScJXDxU-A85ZzMgzOcRi8OK7zzoUEprhFn_57Gkx_7Cbu9sBaPhh8RYiIUKHkokRvfTjhU3th_Fq55UwwjON0nO4fE8HAvo1nJBOrjrGas_bCoAaAMD6Lqh_ZSQqdScE2EYdY7jA5viLZr6v_3go4Cmum-V3BhH2HRXDVZhdQFHGlEAPqNJRNYO9wt6rTfc9P7dmRRxQoyMWF19T1OXFB5ci4s3QxsVs164o1WYg2FcCZO88etzqSEMuCozhexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlPxQJjsV7ElBiXGEITac2jtmZX_nFPFsZZQ0zaYSEZZFq7K4leNvRo-2FpUCDF1GgCssQ4gPRDi67vWhw9VhT-4H2uFE5RYxNK80dqMi2KO04S7EaY_quOmf4beIDB4k4KApxA5WYhpdMWk6xTTVJBMEDxvZGo8hNL41NoHIDalJY3IyCVqtnQ_Oi9hRp3OiVyXTZ2v9pTPar310ZsHyTTtKUnoua4TGKFgnp-hlqLj_RdjoVWEObWAxkgMmUHaaE9-mUXv13IxmuE_azAl5wffoZChp3HN8R9qSrvc0Im4Hp_bDessoIKsCb0kOiIot1xImZY9_-VgsnXcKOobIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=F9umL_49YSr9CXgO0PmYU2YjasFanRtJ-TeiZ7Pt6qTzawiF0i3aT-GH665OudW0ZAU7gdB1nLTrZfezsV_VQZC7UfZfXCD4VbUuxVK68nBq5z18ILTVhbezxmMfAFBRwBoWUxKLoMFXvynrWn3If2G9ILMW2Vn9r8yJyzmDtHsN8hwUo015J9gGYPuRbKRtft1M5Zw6fyHz4I3wABs3HwYuHD-CfJ8MHzbazyEGRaUnzqm5u6ligjhp61DSwoyO_nnwey_-EmQiZr7QvM68Cz06BAgGU73_ZK9wSXHABb4VpaHPqxlLPdRIrTwFpwfAzkQyMKU91rK8sLETo663QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=F9umL_49YSr9CXgO0PmYU2YjasFanRtJ-TeiZ7Pt6qTzawiF0i3aT-GH665OudW0ZAU7gdB1nLTrZfezsV_VQZC7UfZfXCD4VbUuxVK68nBq5z18ILTVhbezxmMfAFBRwBoWUxKLoMFXvynrWn3If2G9ILMW2Vn9r8yJyzmDtHsN8hwUo015J9gGYPuRbKRtft1M5Zw6fyHz4I3wABs3HwYuHD-CfJ8MHzbazyEGRaUnzqm5u6ligjhp61DSwoyO_nnwey_-EmQiZr7QvM68Cz06BAgGU73_ZK9wSXHABb4VpaHPqxlLPdRIrTwFpwfAzkQyMKU91rK8sLETo663QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=oZy3-tuLhhj3nkU8aG6wrUMwyxK3Jj1A6GcB9JxcjkG4u2CpZWcyFs9-hrxQL-LFi1Hig0mLGQNfkybbktXveeVVK0ji22fP3TfkfcXJ4nAZ5_OIpHsEeEoYnhEChscdNyr9IJqg4K4RpbK_tcmUh6ZXDC7Gfn2PKaCkHoO77Nap6Ue-yH4Ht1MvJ8iao7LlEDUqMqdXoIpSCRRFAmMF2XR0tOPd9qjpax85UDLzYX0LEmGelp72QMiSzV3T6NTa_exwYkKBJqmja-qipfu8C0SXMKo6XKjS6TQjoiyRzCg-gfrcZHkjbzYFU_r_kuMpLRyc-ywuAMZX1xeLORn4Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=oZy3-tuLhhj3nkU8aG6wrUMwyxK3Jj1A6GcB9JxcjkG4u2CpZWcyFs9-hrxQL-LFi1Hig0mLGQNfkybbktXveeVVK0ji22fP3TfkfcXJ4nAZ5_OIpHsEeEoYnhEChscdNyr9IJqg4K4RpbK_tcmUh6ZXDC7Gfn2PKaCkHoO77Nap6Ue-yH4Ht1MvJ8iao7LlEDUqMqdXoIpSCRRFAmMF2XR0tOPd9qjpax85UDLzYX0LEmGelp72QMiSzV3T6NTa_exwYkKBJqmja-qipfu8C0SXMKo6XKjS6TQjoiyRzCg-gfrcZHkjbzYFU_r_kuMpLRyc-ywuAMZX1xeLORn4Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=ewdZD2KPTkzBtR3zWhGhofq8imIwtrP8xhN8eIo6V6xcwZAWHbr0cTywhBsZLeK-5DDVfwdP2uZ1_b19R7HLbdnuv7LXoP2VxHFRQm6B61SxkpkoC6cwtEm8indtvLpAD4jSOzvuobDXpssH4qDWsaZAgM8Wn8MjIjJCc3pQsr1UE4J71UER4o6RYzGxJEkIq7yIIan5Kg0nlc6nsHj-oSKblWGB_9Dd2acuLtNKYV7wST_4vK9V_TZxmSKHGwHDjxM3_US8S0Dc5JCJlhcPYEcEqb_6oFO4WIC3YT9lZVburztWFJpcsxTT-9qI0NlYxtUFKzDSzvWPt7o3vm3mYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=ewdZD2KPTkzBtR3zWhGhofq8imIwtrP8xhN8eIo6V6xcwZAWHbr0cTywhBsZLeK-5DDVfwdP2uZ1_b19R7HLbdnuv7LXoP2VxHFRQm6B61SxkpkoC6cwtEm8indtvLpAD4jSOzvuobDXpssH4qDWsaZAgM8Wn8MjIjJCc3pQsr1UE4J71UER4o6RYzGxJEkIq7yIIan5Kg0nlc6nsHj-oSKblWGB_9Dd2acuLtNKYV7wST_4vK9V_TZxmSKHGwHDjxM3_US8S0Dc5JCJlhcPYEcEqb_6oFO4WIC3YT9lZVburztWFJpcsxTT-9qI0NlYxtUFKzDSzvWPt7o3vm3mYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZswMkqy6URZ9m8YKOgyRJDKxaxFO06QzZPSfsWHoaogmlIvB8MFWaV8Kt3Z6ordAeo-KqPQEAEFKy6La9Muem99YRI9oGpNlaUUZNBCRye73PCjgzsCl8k7TalwSwTtLD-h6qd4ylmSLJabVpomxnHWGGHDpIx7NA_5Sq8cwZnhcQcjWswY5jn3Y-bVEw1nlhX9NrV0acKaheP608-aF4rDiwMjN9tsgt2BCq3iH-MaAM6wjS8FFd-s3bPApr7I6qm6x6vYocn0meDu7sO34x-cdgkbLzPW74Q4QUvqmDsFm5D_V8B_yaPDNOOUOchlS1hWns3UMZLmo7AWA8OwHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQYeVnLGQ8W3_FT5KLU2OVCJ-WFQ7WM6qUi2oNr4CZVtz3QGtk0XoToj79oyO5JK_zGmo3XJpem7M4-2Zp-owrA1ySF1hC1l0W7B20aeKGNbz-5E6G_WC_c442fOWnDyWCX39VaaZADd9nX6BWtSTxJ20ErZStS8chBczKM31h6EaZ6uWqkCoR-nnRE6-SH2Ep-yLpZJOcz2jOjtUNH7E60BvT0lxw_e-cmJmXRaiIBF-Pmljsyxga3ayM90EEvjPRnMI17QJAitY1XnBbTCbnOo22wz3U7wNVywxgkQTFEArla18xMHf6Nym1Cl5P3_NNBs85RBEgrKxCFzlwKZyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ult4oBUZinJoa5i2QWfCDKc1S1RPD9KDoB5ODatIodOw7L23etZc-PGitkvxzMSD8ZCWJGvUwpx12TA5c7xbSrKdY5wCPPlQPihu-69omSDmqwU07EJ77ZAqGX-fKfUBW8oO-uBUbj7389d7pNn2rnaaDgZiUDve08Oq4fLmMUm6UlzBfEgMebqXa1ARFdkrorFANUqCcDtjQMUAgUMHHDmS1ct-rbRDzSUcsJrm1swP0PGYgwV4nOb8HpLNzIYM8fN0osC2CE2cKBv1VsaCtQ6-cg-sdLrbM7XTAn4pVMp39fN1Dqfo30lqfELqlOKoAGlLy2yXU_oZYcTDGx4j-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRmIa8IpeGDeahWYr89-EemqZZgtiaJCVPmcZNiBSqaCiN_o13xZ_Crn6_-Jq6UyPUYSWMX7qmuVpCYypqvxdzR4yoPcaLh8jX1Qohhc7BxMx1yZsMszjrcHpL3SHC0r6vCKhvandaCQyvSpdrXFY4afoCD-aFhVJheXnHloTPnb7QmrJ2UX22lIg3z1CAphZe0SvWVc7n00jiiA2d5LH4IMxGx-laYpL4F_z2a9GyW8BrtBz2QsOA3f4yPlKgJ4sbpN6ogCbxvDBbWXN4NS5Tb8LmoOz2NZ3YQSP9zzcKxzhD1ajxWyTolcfXlbpDKDtt-sYaFxIQM6a7Ny3b7T7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuNXEQ6T7-vv3JDgQhPwGYhO3KbBfpQqBR0zJw-qmtgoE6_LnKHS8Iq9XLEY9qZcp12upAx8sWupnuCyAgwRZrZa8yQn-gglfiydSUkAdQjYWG6aHJBgb2H3VFoRUcjkVJOHH3jobY2fFO_a1YXCE_PQGdfuSVKGrJ2amBmi07INt8yUZ53B3xaEyZ2dAeOBoq1DPKmeYp5dIwTQngq4ur8_f-CX6rgKVk3u-__7HxLAswzl8qTxQFcH1O6cFV--0piFrr8C1aF26jRRiklLq53-pUdBu98OuO36o-E6jZtpUK5Z5AE4DQoD9qhb5IWw-tlKcDLncO0TaCjaMcWINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjWFA_jqCFEaElBe8RCUi-dsY4FcuqYCANyqxDAAcQ_1t6Qt0mJIt-hcwUzRWexc_xJ7gIggQcZZKWDaJSUx51NUJYUUkM_70Y1xKAT4bZQZ1Fayy0y3MAZZGNEdKZgswx5glNbLmwqPqSDFRpnz9sL1hj2T0ITRiIjf2Ih5ySWRaD_ON0zEJxD9ZgP1WBvUJOIqn6CoY_x5M4YJzwl7EovHX5SwZNSQZzKQuY2FpuqUGEcxE8xSLBl9rH0szOVVdWit4fr2y70pWyX7hGYF4YZUtMNYsMqEZxLY9GL263XdNxlIT9p8wA0C4lk8GA193Eb8VAP-S_A2j7dvpWVfKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bliZNLA06NwL5-9d46TpSqFiJk1Az7enKdnmsPRbk_VdFuGeA2DiH0xsacfO6PLkGrhWwTJa9RJGz06vjL6jXXhYj_q0ySVPfr_kQ7ydrDvDQ1JiFb1d1CX67W4iazMPdqNbwYZoaJlFkPHP5IR6xNVA-TLhvalGMaeleEI9V1hG5K3Ho0BWd4uhCfxiDJhg5GKtRlzPpufW9-5cF3Fch4JClPfsBiimdMH95KfbfrYqhGIUmuXvmhblgHy6qWfBU2jHRDga9uN0Y-jJSLY3qCrytcaqA6yX8CcIYbe_XPa7hSxb1u7MpKsguBUkc5npMhqMD5hoFXfzMAsNDvrVmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bx1kOsdCiuCmuVjnMn351BpWGEJfZ-F0yPTlhlhcN0LoyvsAAhX1ifAz9CqG3ZTI8PgTsEOGo2EB6Kv2347T8ZQolUMmo9QdszJrQzn6CgUiNWRdaMPF2CXfJIpodXy_7h4PJWdOvx4hpI6HSqe4PwmcSiXHfAHsxUgBfdMH7IlQZHSyssBT8il299coa5bR8Bn6SZriWsGPseZ5UlXFHaWQwL_akkjCobFsusgSkz3kNOE0MrT3vHEaUtLayEuSjgNTs2NJtuzxdKVv_wmElP7yJwyc4G4vud7vdjyow3eGqkmjqfgloMbsd5Ds8bqZ_Ug3LDsQrtDuil8Pzoza2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6MIB7uPQHlSjAt7Hxc41PF6A8OSduEBOwIx_xiVgHiKeV4NiKzSBz-o5wQ1ummg-SG1hgJTsZS-98nSI5S_FAcqG4U8FDmEOsQeCCyumTHb6fVrOGF6Q-OWGNSIwBv7TpdFGM39k1tpyr5kQG2YGCeqCszl6tqZxj5BMrSYU_709xPF2GuaiJZTK4clwFL4t90yFEoE4paDFli4gCxRY_CbIG8VupM6Aqait6r_xpAEs4gVEUpeiHjZkLT6yIYU1Psz-r9m_YSHywUKtwTVlSaA5UAcM6Ty9caTaJoYtri6aiSXqm1r9Qxd7izRRt4nO8EA6JfDPWX0XvBdSxG5AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhOsHiRyLhSZ11XFv6RETENmOyv-HEwrC2_4OOZrzaRwzkBfqTUtRIAxMJ2szSPstDaiRxwnZnLLDLzXnFnkVWHCFNfJdhifP3JAq4zcwDF7bNjlHAnW1W7AoXlbWc-FYHMrazAB6oGHAgKH884G-udsygWkjYx2hcHseoeKOzmAx2nM7jWxm1pjDl2BPPi0Dh3LX0gguPh3Mz4vttKNqU2L4Hf4EdQiLhuNQ_poldaFoqG5T9la85wxRSofcTnlLHs9syEnIdfa3UGlw2S-BfOw7v1zSA7jwVuHBYeRfJYMDBPFclJ3gFv9SS7LM0AQyMmk1RS4BP678onFw5KZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGjBj2OcA561RquCCW9oQwWIb88oGF195JIYGEqQpOUIZ1l3kEXLuaLhQyY2jy1R3zHnZGiFnyU-o4hAgRrbRfpxLa1gpmsE97pD5bjsdqdy8PVLTWrJpm_kAAjqi5HnXB3C1q8Yc8QjT_rKRr5pQmGcbl5ZjdYemVtygJvMCENXiOBoXussDX_POg2Pl0R9aSVviApVHs8H8I_4gTz1ZW_FpgSrLuA7_fOtmLmS9EXaXbhrOd1D6go6jUrD0NC8UQXg7dqZX4-QhR7ELtKOT9goSjRLicbAjolbeeOcfz3d1ouV7WB-9kmG61fJUwIDoqfxNBWEixMcqpJvPvHHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkKRGAvzgSHpjuiowthfzm60Pl1tL-SgwcmGezC8A9NuQIUMgdkVhYKvdkqTeNCjhPUzf36qEEjfXB7NCGW34ysEpYIYjLuAAP83uVM8SdFnklpkHws9OL7azwwVeFO9k4TsAMYgdzQbi6WgAJTxYbwAMxtQcb7QcnWpGjBV6r4xo9ZfL2YXPwbPVtZMfUISwa0eQiI-COeq9Kg6xs5e2BzEFkYQVIW19pHqLxSorlyh4cIlm8oFr54xgwVAyzb6lroTkJC8ZRJA8xOLERaoU-Yl7HOk3BCdTEb6pCpbfR8K5L0BH7avFclUreCvtcvG_2tdXcX6BMRYHPVpDkc9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF40wbT-G0GnOqvHZRtGAH4hOJ6kOa0cNsPNmBko5nsrJ_t4C6LZDEGVwq-Qy2Z7vlJwAJZoa4PC5jk9FgQT0JZIhR9eZky9OinPeykaMfL38shc6XX9Cc8RpIQ6aY9ds3zzyRj42z1YuQ_-CpgF90OC3Tg_cbg00pRljU3z-lI86ihgss3YyJyMOLbXDBGK2V_XDMnLpNBogO9L0GNJyhlraQn9-CBknhaiOCEv0BbfxnsJT74ZF5EyNM_Ez-HLT6DEGZRU8TsdOFWJ6KpqvVxJDVpbLA7mtNAzZhkcs-_v8hk2F09X1stAnPBg29q2r2yH9uXwJGqdMywXekE_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At0gBbRXAq1C6yBhRGfjdc9WgUdRs33QM22TVbMPCZgxpKW2H5XughHcJCv614JDn4Yvao6RCqbWLf4uY3Q93g5kPcaYG1BUD4cFhJ5SKifkY-4A22XXy7bgnIQyRr4ixj3gNxFNJbhecKUYCWlt5Ixe5OOPH7QJvAwgF7gkJfEysIL8uxy-MOYdi-RhvNWaEB6JCmbjN55-PfnhNgfdSI8yg3HJAJWUJmbWZDSgiJfoE3AySkPc6BhSpVUNxKKg3zdzuK09HjmtmnW85mOPbLsWfujT-kSPfff7QBA3F5pdDYgujh0exdvoYS6NCp8IJvTcQLF-9n0GVxEwqJk4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
