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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 06:06:21</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS5S9d764T9zFk6An4H5s1vCscROBLJiiwGNHZ3PKoNqthjA7EcQ0OEiwVRGC45CrT-B9nfORTMt-zTaBzRuhnwOSAi0N573j2jYXeYHfJjSPJ5MurKlKB607h538uhofhuzsdPrUsKIlOTR0h4fj-UV8LHj-AeaqFVtOq_ia2nYNQcxCdd28v3yIazw3z2Ih453pO2vA11hfz3ufIZ5FU6CWS0lJ0KH_i4U9toPEpr0xUMzz277_Mxdqcxk98bl4rlWjbku7LR-QPbnDZS5NoNMqnOKmnzjRLZ_pskoTfEzF_YClS8gjtIL2KssvvaMGtx2l3EZqqsPISxlkzr3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvztdfVtj9TfByy9vnraHfetouPFFNNQ7M1mSDFN9PsWO9nZmlU-_SU8KSxxzWOvPJHFb9l3sbbzS1vOSYIS3ERYaR0gD4S8VlFBsU5z9VWH5YogCVTsFkKTLwDMXex_hVBP94EaZS5S8t_BkPSsIBS2CuSeRjk6voR6QnHTVTUe7JJ1tMvzQA_5dQqFWLNmo56zzFTsip_AS_jJ9RjDKnC9quVXkR5i-O1-k4lk6-ygBaaN91OuFicUO3JTAWIGPEFKGYKcs0vP-xKBYgkD6PWK1S87hPAUgTzbNRRV0tAwOoDFadfm3ZGhVBKrTMOnUaBvbdap64KhpVAPcxwlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP-lQMgU986XnWqs3EXgKfybzdResUOwuh183IT1GZQ-S2Y89AK6wSVrzUtJTxGv48gkUQyG6PWCR_x1YSjy_C7DAzUdLtPcNwlAEuyjU_gUTJbofQgD4guAXNQ6wClOXgxonRIU03I9aB5-4qzww8CU1BB1XqnUvbNUIEmUIqPlIO0yUdZ8wqWT5b2O5Bfaq9lbeXD70KYEssepfMm6Wx8_bVERkPltZFpHNC7AUAE00Dmiy4ybZV_PA2yxbn8IaNZ74ZFFMAjO2ReKUVPR73rIijR1x6SZcWPwLY7dJ8VlGW3luTCHBg0c0jh8HwyQsRDxCLfnwn_TsNrC-R1kTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=AyKoiwCtByHSE39EnlZoSPgy9yNBVYzugpWYVTc0m-vsGCsxeVS83DQ_9iNuDwZtfPXqeW9SmypfSrhZucssXUTTOmV7TxO0PIAjcsoTOnH6Kyw-egByp8d-ahAmL5rwPsBMa7ZLdYmO_ZKkF09GuUu3R3KBEX_LqiYNxMMjZo1pZjCuwQf3uKXM9BgCEebW0qZX9PxbmLwYkwLHhhuEA56rfR-2-Ra0m4CWvfFPwcZFxB778OBQXkdVYUqVtYX5cb37Xh5EU99LMR0dEfdCFZ32kQhUC02bltArnUvAshoVN0Zyx8lz4cjPGp91eZa_r7ZLMMve5hKNtgy9Cf5xxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=AyKoiwCtByHSE39EnlZoSPgy9yNBVYzugpWYVTc0m-vsGCsxeVS83DQ_9iNuDwZtfPXqeW9SmypfSrhZucssXUTTOmV7TxO0PIAjcsoTOnH6Kyw-egByp8d-ahAmL5rwPsBMa7ZLdYmO_ZKkF09GuUu3R3KBEX_LqiYNxMMjZo1pZjCuwQf3uKXM9BgCEebW0qZX9PxbmLwYkwLHhhuEA56rfR-2-Ra0m4CWvfFPwcZFxB778OBQXkdVYUqVtYX5cb37Xh5EU99LMR0dEfdCFZ32kQhUC02bltArnUvAshoVN0Zyx8lz4cjPGp91eZa_r7ZLMMve5hKNtgy9Cf5xxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3COGPDukrVbqp3_YROkqZ0vlHQDw_x1bNduAfce7w8A8qokySOuxnukIr9_FzxvVeQGjr1QCTa3a6DjPfi724DcwAkWT53urEZC_FKdSaci6H1PgtGGuoJkQsjDzUNvXd67OTt4-mVy7YW8tUd6Fv_qxUrlbtHhijJJ4mhwMHqOSjOH3KjY8CoaQAQ6adQrRk5GZcluuZwNrI5XKU1Rdeh5oIpYZsqRxb5TKmmVMhMW4d9loTK2L7H-ZdTejiMOOBrvda6lDDwNr9VAT01KT_Lb1v7xMC0z7fUQj0mJpBObjnluIAYBO592Jtq-rZtL7j0QLNkfDpl95Hakr9JT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XhHqhNwn-1HN4hXtCXauwGsKGsJEEuzybpBdJXm9nsdNHLQddnNekBP9stmUe5v6NbRDsEJfcCU-FpvyTrSxcD42wxWO0JK9WIupoWn1RWBltW0SP9_eEjCWVvQkVjiyYde6nsNt2_kREMpIlwTJ8e63VXQ8ZfOxlr058wg2V4tQgoG06qseUz9UzIR9972OvTbY6tSgrvAo2ZJYT4zlLwvq1BaJr1OkXarPu7M1xhFMDro8Z8lMlrQr3vuxbKJpxGZ4ldOa0PE0bQQZ12SAgG48YGQHGPCB5wCYi8K6ZLAhjQbPBXT7Bp3JWx1Z36X9oEDvwNIaaYIQxIulJkEfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSNf-0ZWvkOIpajNBoPcNJ1Y8M7VV5hQ_ZD0CUl9-4VNLAMcu52_yf4TAYxyvzfHo8RqyFFLluwuAHTRgbbOiPJoDHEgqe1qZyEng_wVIQI7j_uEQM1nYSiVJv5c_jQXDC9XIcsMefwL9QjBVGH1WN0rG0VirIrzy60LqcsDz1DbcmXGFQA8zofcNUosn_StSci56A44nHyzV8h5mTVeGSHKucduxJ8DHFuMwxfI1iRUAzSHSr_XgLZBEtyrw-6cr3HKY-Ilq8j820SLRUqcRGAEagmbaytza1I_4j7gAl4OWtQ27XFu58c07-rM86EhBpwzoDAG7ZyJxoaHJMJBMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUQBCtO4QVe8nZL_8OYWc-iQLtB0WHgJVx0CdmoHW85JPm9WnVlPnf0EeDtPVIxBpokdwk8d6cNgw7-nMqDLWgkMbMkEKA7ltNn1mr4cvs6AdloOp_3Ajq5BojQ-UXQ61hpjVuTo680rsRskw22M79XtPhV62vWi-P9SwX_6CPUSoLI8MIRemN2cQWF8ol577OUupk0kbG4Wdx-ADhlcFA7aY9wIZT4OXR9SmjdF0t4a-3QvLVIudyKSv-CCYyDGZUYvIXhwPL2O7vrS4rnuGaHXcmwqY_te_mUx1Nqzez5MTozzJCbKkGgLypq56mvdReQDB9OWwvaqJB2Sw7ld98k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUQBCtO4QVe8nZL_8OYWc-iQLtB0WHgJVx0CdmoHW85JPm9WnVlPnf0EeDtPVIxBpokdwk8d6cNgw7-nMqDLWgkMbMkEKA7ltNn1mr4cvs6AdloOp_3Ajq5BojQ-UXQ61hpjVuTo680rsRskw22M79XtPhV62vWi-P9SwX_6CPUSoLI8MIRemN2cQWF8ol577OUupk0kbG4Wdx-ADhlcFA7aY9wIZT4OXR9SmjdF0t4a-3QvLVIudyKSv-CCYyDGZUYvIXhwPL2O7vrS4rnuGaHXcmwqY_te_mUx1Nqzez5MTozzJCbKkGgLypq56mvdReQDB9OWwvaqJB2Sw7ld98k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=X-K58r-ol0TePuFP1u8KEoXf5SoC-P9iSoV8v4LC8eAFYL4nmMSGYErxpP_PLIxgSp-fOXCuaVS9kdDMT73PlIBn3YtFa826paL9DnQtyvDFjeWxK_F8wTdeQjc-E09pFKBzWBEyzPW1NmjkrHuDX_rEVLFPpP8lNxk9VF_9s-wvYjIwdkP4iF3P9aJ6tCsYBnf91tadtenu5LlnRg1wS37CUL4ZmK3r6I6lI2gn1rOjMej2xe7qtMLuwnZRBH4V14nS0OgjG91KFZTtJAX1FxECMx6QAljvPPf8aL4gAnYVEAhND3QGUO5rHVpudUVoNVUfpkd5LYWW5rZywbeHUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=X-K58r-ol0TePuFP1u8KEoXf5SoC-P9iSoV8v4LC8eAFYL4nmMSGYErxpP_PLIxgSp-fOXCuaVS9kdDMT73PlIBn3YtFa826paL9DnQtyvDFjeWxK_F8wTdeQjc-E09pFKBzWBEyzPW1NmjkrHuDX_rEVLFPpP8lNxk9VF_9s-wvYjIwdkP4iF3P9aJ6tCsYBnf91tadtenu5LlnRg1wS37CUL4ZmK3r6I6lI2gn1rOjMej2xe7qtMLuwnZRBH4V14nS0OgjG91KFZTtJAX1FxECMx6QAljvPPf8aL4gAnYVEAhND3QGUO5rHVpudUVoNVUfpkd5LYWW5rZywbeHUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=YPCbmqnUyj_cmXCuLpPcGvFMCS4sSF0xJsmFgH6n5fzUkzTdtPxBNa0DzorR51WZpnPU8ciLoD243kuqy6vp13MOZXJrULyopWAiLFnKm8LO4q4BcAgaGE-h3TWD5reY1jIxhloRCjPjbckBAl-4Vsd4XhdsyQvuNgUNw7E-cZeQLKBZd0bNL20Q0kkisiQtoCSsUxCZb4ISKRMFGZYMIQGwyPMnx4dmGXRM_x09mC2jfoPTzRLVsQucZ6rs_cW-yHpVbsrNF6riA1liH_czPcJHYxIXbEKOdInmQ3RKLgZqOBMVUOU6EV3oGnHkOnDz3e51PKOrA-AwCy44XeGZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=YPCbmqnUyj_cmXCuLpPcGvFMCS4sSF0xJsmFgH6n5fzUkzTdtPxBNa0DzorR51WZpnPU8ciLoD243kuqy6vp13MOZXJrULyopWAiLFnKm8LO4q4BcAgaGE-h3TWD5reY1jIxhloRCjPjbckBAl-4Vsd4XhdsyQvuNgUNw7E-cZeQLKBZd0bNL20Q0kkisiQtoCSsUxCZb4ISKRMFGZYMIQGwyPMnx4dmGXRM_x09mC2jfoPTzRLVsQucZ6rs_cW-yHpVbsrNF6riA1liH_czPcJHYxIXbEKOdInmQ3RKLgZqOBMVUOU6EV3oGnHkOnDz3e51PKOrA-AwCy44XeGZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofbG4fEWPgnonh698zMyBj-nexwGgcOnyC2JA0A3oPA1zeDbTWMYAI2u_V54uy-FUZESsqy45KHtsUAo5VC0_JNpmFjai7JWlxHsOb0hdoGH2zP-lwQqbyhIjPQtYDD8rahR7xuqx21RNONPSRNTFezJxnAl_INzzXmbo88gj8LV1nhtwP_rZ4Ec0G8l6Hqj3bzKAepLX5XgDQCsYMw10d_aMKOsspufg-OdE10eN54aiFnwFhpb2iR0HAKxBvXzj8Mhr4giFy4M0i9jxSbB1GM6C6tG3zbLE4Y6UQKMtccz-4pkbNnkIXsz6yBGPMC0QQ8JCuzjodLXrH3rrmB92Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqhzZaiRAbWTGtqC1PfXIhb_RvpMqZPOhFewFlsRu7-FrxeX3nxphOL4KD3TK9TgUaklaMv-ZTQoFuIUNvOm7Wmj42aeIAxJnyGqxzNPIAxCks6UEj6QYQ39ZTRfHmnrU-5jFqvXFKSjd7CHxPHo7pCtqB3EmjgrW3wYm3WKtvagacO9tlh6jvUiuC0LLBYlw30VkTuTKxuxrHWg3RGgzyVatkX650qyQWdrOey9pDa49W8D7oA2bjUXgKUNUAgHiV54VZtr6p_jOh_Yn8O_oKtPEhltSsgyPnOOsltj7AfMNxk4mgk3OfM_M21p5dkTjBrrDq3nN-Ec-0Bn5it5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0OOCOKq6v9uny0rfXaLKffywddFewvCWatpN1zvU7NWNQa371quJaPrIsDAH7uQzBUvVV1x9-FYKGnXC8Kh1IQH6ZT7iIdhwGuzvo9tToknrLLxcqos1mUOGU-CeBqiMFkLe1luydacX38AyO5JH3XI0wUEVqaPKJQf_NQLnEMHbFNOolMi0jHUkAcLE0YwHPYr-3u3WZO9VLcCrKpB6w_aubETQycrMuyl7EdBN8Onu1iMXGO-zUcukNlOPVUCFZT9UQh-oFPthPqpgbuZFm6O8YBNm8Buwt_IgnFc2zgQbQBXA5W5v0LZOjScPDQgh9RIBx62nzI_pjRZ-0Aejw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=thjrFMlcfVljaj0EspQiPJcy9Rxqm65TVxUPv9wWeiLWMM4iMWJdpA7FYG1rm68Yd8WoHvvFa5AWhFMtDwgI-1sH6ys14lgEqDvTZhHQA4IGXZ9OUrA5CdXauqsGtvKoe-OglC0Tay6PSN73i2RBAHwaSOXrIDSUp7Mamxpg_HMZbQUwztl3-IkPllQxpe8LlnHlYOPMuqvmMZLs96jMRDDec-zV1U1u4mD8B1BxjZjHMas86V3U2gOwMZCAQcIfBwXGlQDPgsaQJJe9YR5YVs9-AMfMdn3bXQy36dZC4CJtBYVIzpj51Wrm6eNWGZN5wIUmqbctlw_ziP0zkpUaXxxXVCqcN58Uzn3bCMDUEeh520wJetNpJK1MwvBjqH1YQCJ61HO0sBuodibCUfhp7seA-h_zkXcw8tTAr9aSagmHhYcnoHYi3PKV6mVYQix4bN_yAwSadTgx4kMa0c8ooa8zenuJ7bCl7sED8sJhr9Y4jHWJKbpgSq-_zO_m70_oalcA4395jo46ZyH7dArypXEVAIgyGmR3STPdv_igBDrT1OXapSGGBaz8uAVYVUdzcwiafyob_nAveztVDevqnvtY_ty9uA46riBE4KeU89fohvN9-3y-2apm0RWP-TE6gGVYEdh5xgiar15BAJEU2oFt8_p98_9MFqS4snG-iO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=thjrFMlcfVljaj0EspQiPJcy9Rxqm65TVxUPv9wWeiLWMM4iMWJdpA7FYG1rm68Yd8WoHvvFa5AWhFMtDwgI-1sH6ys14lgEqDvTZhHQA4IGXZ9OUrA5CdXauqsGtvKoe-OglC0Tay6PSN73i2RBAHwaSOXrIDSUp7Mamxpg_HMZbQUwztl3-IkPllQxpe8LlnHlYOPMuqvmMZLs96jMRDDec-zV1U1u4mD8B1BxjZjHMas86V3U2gOwMZCAQcIfBwXGlQDPgsaQJJe9YR5YVs9-AMfMdn3bXQy36dZC4CJtBYVIzpj51Wrm6eNWGZN5wIUmqbctlw_ziP0zkpUaXxxXVCqcN58Uzn3bCMDUEeh520wJetNpJK1MwvBjqH1YQCJ61HO0sBuodibCUfhp7seA-h_zkXcw8tTAr9aSagmHhYcnoHYi3PKV6mVYQix4bN_yAwSadTgx4kMa0c8ooa8zenuJ7bCl7sED8sJhr9Y4jHWJKbpgSq-_zO_m70_oalcA4395jo46ZyH7dArypXEVAIgyGmR3STPdv_igBDrT1OXapSGGBaz8uAVYVUdzcwiafyob_nAveztVDevqnvtY_ty9uA46riBE4KeU89fohvN9-3y-2apm0RWP-TE6gGVYEdh5xgiar15BAJEU2oFt8_p98_9MFqS4snG-iO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETmjfBRUphQ_1Z8XDC9mZOjQoAiPF7tKy6hjNTFPddh1mLtj0AAsfVFBQrrfA1nkCrHsO6sw2UtF_5Xt-aVwpliSpItov5ofVSc7xJ9kHvvADTcdwGXufgj_wVM-NthsPUJZZlvdKnhKV8LlB0uwQs7JeAwXUNUp_N9DFDOO3iwahCnHcjy9qJ_rch45_6dcEGnMxka20hekDK1pgP2siniVpBtoSbqrUYo4igYtwI170imY7HTfyEI1LJWe2EgXaip5iAc72eFRJ60_CXK2_Dqqc6-lOjtVkQmM1vALctBH-484xmzs83aiAsDfEykR4SxAKCm4BsgJIQdm27oP0BPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETmjfBRUphQ_1Z8XDC9mZOjQoAiPF7tKy6hjNTFPddh1mLtj0AAsfVFBQrrfA1nkCrHsO6sw2UtF_5Xt-aVwpliSpItov5ofVSc7xJ9kHvvADTcdwGXufgj_wVM-NthsPUJZZlvdKnhKV8LlB0uwQs7JeAwXUNUp_N9DFDOO3iwahCnHcjy9qJ_rch45_6dcEGnMxka20hekDK1pgP2siniVpBtoSbqrUYo4igYtwI170imY7HTfyEI1LJWe2EgXaip5iAc72eFRJ60_CXK2_Dqqc6-lOjtVkQmM1vALctBH-484xmzs83aiAsDfEykR4SxAKCm4BsgJIQdm27oP0BPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=nd4QhtCxVch-KQdZVSFNz2Wfdws_1Yi85-gVzHceIg6t5PwrdvwTm_sbejUro01WPzjg3nDC13IbjsDUREyCl-7a6g1e80WGzzXjBYawnTrRFW8tNltOSOzHwhxh0PQJKzBq03uc2qsqkooj--ZgjdMi8whu501KvIKdEcrhJjcyWyKSx3yUN_o22AqMI08PcJwktnbHSCBg0XoqzJQKV9HJOCCJiW3Sr9iYdE0wWmU4L8zwECph1UKKgg9X83jFdgVKytsRiW9WATY8QADh-VrLX8cb6eA-_eyYUG6hkw8QZ79_iBWvCufEPS68H4ILIeSuv_n0x7S3uppajkgO2oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=nd4QhtCxVch-KQdZVSFNz2Wfdws_1Yi85-gVzHceIg6t5PwrdvwTm_sbejUro01WPzjg3nDC13IbjsDUREyCl-7a6g1e80WGzzXjBYawnTrRFW8tNltOSOzHwhxh0PQJKzBq03uc2qsqkooj--ZgjdMi8whu501KvIKdEcrhJjcyWyKSx3yUN_o22AqMI08PcJwktnbHSCBg0XoqzJQKV9HJOCCJiW3Sr9iYdE0wWmU4L8zwECph1UKKgg9X83jFdgVKytsRiW9WATY8QADh-VrLX8cb6eA-_eyYUG6hkw8QZ79_iBWvCufEPS68H4ILIeSuv_n0x7S3uppajkgO2oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=rV-TwoodRwoeHNTRKmJ7WaHnZ8ETsL3I257U6khqf6kYBKeiplV_DSm1MFW4twNXjNw6psyuWEelWoo6GqKcV3s4__T7mLRzvMImukMQ6DbkkkdNfjeA_eYjTrBqpX6LKDns0oH9cvHaPvZMRG38oXTjw_RgcjHlkq-Jsski5xrY7fki0Sf0JbWa-5fUwRMXlealWYrve3RkE79Z-8R8YW18VBUrCaNwtExRxow87q5BZBzhFtSROygV2gA956qUIJsEh4dO_xO0-7nkvDOz0vWEFyYC_bx3G2cLwaS3qjzGZ2GX2_82EtO59NI7uqs1hBxoYx9e19mE7om7dkbRow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=rV-TwoodRwoeHNTRKmJ7WaHnZ8ETsL3I257U6khqf6kYBKeiplV_DSm1MFW4twNXjNw6psyuWEelWoo6GqKcV3s4__T7mLRzvMImukMQ6DbkkkdNfjeA_eYjTrBqpX6LKDns0oH9cvHaPvZMRG38oXTjw_RgcjHlkq-Jsski5xrY7fki0Sf0JbWa-5fUwRMXlealWYrve3RkE79Z-8R8YW18VBUrCaNwtExRxow87q5BZBzhFtSROygV2gA956qUIJsEh4dO_xO0-7nkvDOz0vWEFyYC_bx3G2cLwaS3qjzGZ2GX2_82EtO59NI7uqs1hBxoYx9e19mE7om7dkbRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcTqGw1BkSogGUFfE0bfp-Xyyp7_e92D35brpW-1Wgf8fqTZNG0mIjg6FKPDJ4EisfNL7n-rdWip_ePGJ8PCqbAo80XoMvTuk29Hxo-66fKboed7Tm27LbUvZHCc_6rU1-TvSCbopvIHPl_cbHimqziNLwXBn3DwBywBWgitWuOdxR0Xw2_whBFGAKDiz2_0IJX1NBoSM4EoTRHicODr3lBIynN_XzAQjHIvPkZYdoAatBIg_1aFx7sepPmkMRSg_BjKnAJMWIQSghojOKqG_saJUM2Je3T6dbhYJQL2kK1-Aba02MpSSnmJO5VNZiWXacKALSrzkPdV3bTpqtMuIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4p8y4eGJXou1QcLk1qvV5Ru4PxVfyoMHTGIl-38bHNe-INJ08biBpcRu6a4HplZPYlxbuMVhlxymUfBmXiwKLC3rRd7Kw9lI3YGzZUQcbIhwo2VkFdUsS9qcneszWEwIBZ_T8dsYjaK9oQO7M5yegcfTZDMWZRjS-BrjR8MPHeKbiZ3v3OHHcmfUALMUlj1JzW9FAdkaxKdukLsz-TJVGfeApqiRxYMEco4RKxjosYEoignruq0y-eE4qzepyB_SvQv39V12yzrBextfxpcQa6X9GbzXkYWdekReUo9Nvd4ynoDcC7_ra9HbTbiNAAWMZAMB8ZGKGewKZTkPI4Lew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ9ECip5ZNC4MDloA0xMJT-FA2Iq4KnJzngJgziCLrk6NGMqfj24_Zop4scgLXIb_OSUMoe_8l7vZJuFtutaio541Lu5nNBTueBeiEGEn1p6h3C1Sb8hBsvd7yEU3UCD3n6xNY6rd6I-UxXDM0zYgS9fJrUAXEMHhLcPxb2itDKzPrMYLj3DQHANV3gGOGTb84u7W93mLHp1FPD4-ShNVxxqzyF1xgCgQEhlV0-MPcHhqK9YGcCdD_UbLMV9IvGkT18fCVIPgNbYVKJ4y4dLYY7-q2E5Gn_lVR1XyBFwT7_yOWAEPsZWxpbCRb5sjy50D5DyKrj2Gdfcak5Fx1b_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1xp_HZOWRI3Wn8_5jqXvfyQ1SpuRAvNJbP1-0o8xY8mV25YyztIeh82abG9OgkxwnqPNYU36AndC6pJxkN_6vzyX0JAYpHz23SUm32pLJNP_jFP0kAEvkLK32lLpdSCBlLCWWL4B7xy-Pgi-9vqs4c4p_gDTewbF1_8jewb7LsFOm5CxQC4-dxc3RsglzlB0eXKi7Btmx0AkltwBk-_2vsiT00eUXfpcvmiWquqeAXAiaaE_Kjr46DWSkKuHJtLEr_lmFS8FW4XF4XITBBeqw1BuDJViYWrpieIDJQ5z2js6SRgwy7-vrxVpkW6o3wfsY0YP6U2B-EZl4xmDPTUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8-iI6hxaVABcKbQHYlRaWLc-o1paEk-2qL437FEVt9sbMgkRA4NCY5lZASDC7Wf3or1ZvMWhOZGkpNjz_7PrWADkXB3ffiFdnRripN9JFZeVGtMbJT_9z8ETgpXyv6-Xg1POrlNanIBaNKnAHNZ8iVPkKOqBtiP5_ax-o2vqCSnnVpDgVe3yx_1SnHHmgYd_OipHKX8N7xzb08fN6PSVwW3NNd97dCsBxzAaLhJtKPvhmm2JnTvb-fqCFng4_EqVkI43G9Wwcaj4jVc9Jk4WaM5HYHKbxwBu5DBYKWP7YhTBV-CCEVDcQLO9efi0ukQDCVzGGVjgpAAxCXZ_wfKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=IZYs_oQ0hnIp2b3amFEFUAwY5xjw3PlZTWZx6R0UDBoLNKwXC3yGo2oHBLLZ_ZX7x09chsC4fGjQp49yRAUFODvB50eaJ-ezggb4ls8G_2sZ6mLfw0AfueZBMzolcAkxcMY1C2nDMRmL6fr7asrY1QOJUK9TPqfx1KjpRaEAvuDZ2jSnTslk3vkM_6VM4GbT2UEVm6aXloUM46ZBMebuC2FVz4GMsD60ZnsdpPBygQ-slbZAwi5CgLQXOq18lDtxyZlFwTECViy_l5ZPkp0XJ06lCKH_9S1vk3kQWcwA88fNkf9ktWEn7MPOvtrOPZdwdCx5cr4HWURr1ikhkG9tsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=IZYs_oQ0hnIp2b3amFEFUAwY5xjw3PlZTWZx6R0UDBoLNKwXC3yGo2oHBLLZ_ZX7x09chsC4fGjQp49yRAUFODvB50eaJ-ezggb4ls8G_2sZ6mLfw0AfueZBMzolcAkxcMY1C2nDMRmL6fr7asrY1QOJUK9TPqfx1KjpRaEAvuDZ2jSnTslk3vkM_6VM4GbT2UEVm6aXloUM46ZBMebuC2FVz4GMsD60ZnsdpPBygQ-slbZAwi5CgLQXOq18lDtxyZlFwTECViy_l5ZPkp0XJ06lCKH_9S1vk3kQWcwA88fNkf9ktWEn7MPOvtrOPZdwdCx5cr4HWURr1ikhkG9tsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=qCl5tH3HUVJXX2ztGvm-IL0pUZptbUxDd32AxQNW1_1RsvDi9JLG_N_4wONrEL37Pk9bqNQ-edvs-Qyk0SHy-jLKXyaYP9efMtDGjPpwLoB-bATRTOcD4tSpWJ-nzj3ZRw2NoigZaJ87LNPpF-CNAc-cAEX2IRHCmh-RKf2do5AcJm9TG5Xw-n_FobKJQ9ZwDxKysZmrrPIRUr1NAATZMVEl2A_NOvyI-aA_K3f--595cLOCxD04cxxhcAJv89qvgKkXT-tgVZMUFBD0VxmVlh24B0MeiWgIgCbNCWasbUaDaqCv51gNdDLmUqgE6JA-Rfz93b_x01HRrJxkxBrp8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=qCl5tH3HUVJXX2ztGvm-IL0pUZptbUxDd32AxQNW1_1RsvDi9JLG_N_4wONrEL37Pk9bqNQ-edvs-Qyk0SHy-jLKXyaYP9efMtDGjPpwLoB-bATRTOcD4tSpWJ-nzj3ZRw2NoigZaJ87LNPpF-CNAc-cAEX2IRHCmh-RKf2do5AcJm9TG5Xw-n_FobKJQ9ZwDxKysZmrrPIRUr1NAATZMVEl2A_NOvyI-aA_K3f--595cLOCxD04cxxhcAJv89qvgKkXT-tgVZMUFBD0VxmVlh24B0MeiWgIgCbNCWasbUaDaqCv51gNdDLmUqgE6JA-Rfz93b_x01HRrJxkxBrp8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKkfmQ0HGEDpItf9Lr26dego53aehTFFnESxICzqv0Ny35RtPb7oCh_izQK9UyxB8XlUokgKS0UOA2PAlum2acX9RkxYd_U8QT5dbj6SByL866JqftKrNQYYHOVZ_9-yX4lyRQEpuw5TjQLuzZ28JyVGj34AtXVEEG3D5sOPqW8WcPIunXjM3tStuIfndX5CSVODuxJ2UtdZ9z6Z6AEB31VvQXns3n9yrga-kcllNLqOpD4Dy7CnXlbp0lj3svSaiPGqpAaxvctVBjIqmRwtwPzUY71qcwMDOSNUtoWhnnenYrO3vk4Rmo3bOwh8iOJaSmNkg3yiuscrvB2isq--3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQdDwu7I1aMRxeWrzoUfv4ySvV-aX620QrVmL1foo94Q8PcKctcI1j7LtRcsfNaynyjyBMZQpBEIp5eR6kV69v4ZBlt3OZP1DG-06L9G8aFlkMrzExNIEaRDeIE4CwZMS6da_mQavXnlK3ufMxYr8CobcaNn4nFqGGHUdcbTMghV6s8nhI5n-uIbJeXVDjcATqRqpBJk8m9eX0sMALk6OiYmhQqVlWkrMrfRB3bW25_sFnxaoMJyaXe5UB2Ix1SQajnzCu-GwqwRDZUbiBVpuUN76WfA7pR4DG4ctaAfEET8_1n7I1SIKq8DWe1_cL0surv8JW4dr_oBJ49NWFfC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=ayE_TLyWs5hqtY7kN9Pbaf7DNRZ0B5oD-TC_GXOGYL1qRmf2sv9bUyxXJ7atLfED1jSmyMCT9IFaiatQYgUAKfgLhm2oD5UJz-tv9_dEs263UO9SG8huqOII4AaYEOf9NrjWFVCo34tiog0R7CcS_v7R8ODADHaN8C8OvghRPkjKzyb1TE1OysaToyNZR1Z-cJwsYBF0s0JdgGd2Oz05KT428Xi2DFYwn3M4vXCVbOHpUs1fL3ouHu6N6CA0pjCUe9ppJWypLGF9LOJIjG8cVKxBuDtKKzTqlQuVXoxPcNtE8Jyr54HGKGmSrIGmbPHugG67RTtEPloiziwIiHBU2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=ayE_TLyWs5hqtY7kN9Pbaf7DNRZ0B5oD-TC_GXOGYL1qRmf2sv9bUyxXJ7atLfED1jSmyMCT9IFaiatQYgUAKfgLhm2oD5UJz-tv9_dEs263UO9SG8huqOII4AaYEOf9NrjWFVCo34tiog0R7CcS_v7R8ODADHaN8C8OvghRPkjKzyb1TE1OysaToyNZR1Z-cJwsYBF0s0JdgGd2Oz05KT428Xi2DFYwn3M4vXCVbOHpUs1fL3ouHu6N6CA0pjCUe9ppJWypLGF9LOJIjG8cVKxBuDtKKzTqlQuVXoxPcNtE8Jyr54HGKGmSrIGmbPHugG67RTtEPloiziwIiHBU2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=Nr0DmyV9cSS15ljxMzdFZUiTOV0Fc1e-ADTEgqkZibkX7swedOpk3wYWc0jUrE1GEXwmZ1dJLmDqsRO9HT2cyO8gb5CPs5HL-I4-dbzSTfQf7M7Tlwi0PSMNYaaTsWGwnOSzZrQvrOvsQFcF667SzzKh8vJDNOu-fEC8DI-BKjGTN5NtVyf6j2Zga7j0lrJZ2S0u5qllUC6M3lQio0pJzLFr6ABOepypMXpVnkUdeSCordTrlFXzqGr83wtZW9drLdk-EX10YAmzsuoy6ZMt3Ag4CJjlgTggSJySOnVPqx92rcHNg8TYHB731Y_mtpQTkdQPBeCk5ez6J9i75bkNew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=Nr0DmyV9cSS15ljxMzdFZUiTOV0Fc1e-ADTEgqkZibkX7swedOpk3wYWc0jUrE1GEXwmZ1dJLmDqsRO9HT2cyO8gb5CPs5HL-I4-dbzSTfQf7M7Tlwi0PSMNYaaTsWGwnOSzZrQvrOvsQFcF667SzzKh8vJDNOu-fEC8DI-BKjGTN5NtVyf6j2Zga7j0lrJZ2S0u5qllUC6M3lQio0pJzLFr6ABOepypMXpVnkUdeSCordTrlFXzqGr83wtZW9drLdk-EX10YAmzsuoy6ZMt3Ag4CJjlgTggSJySOnVPqx92rcHNg8TYHB731Y_mtpQTkdQPBeCk5ez6J9i75bkNew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGvlcE5zylKDJi1Td9g-ZYRykseT5AMviDVEZ9UVl9-fQgeruh8MVUMzZcGBnNmlNEeCNOrscsun-FhQ1vp7OR25ZUaM2aPLwpJpyfPx0XoB4wy_SFeTwcLuhvu72htFwgSqyzwtk-XLuwYXfG3M0zWzuOpsSOly3ymlBQ3sq7Topxl33P4UuuzZ5YhvymZXtDtPryZyWgw-X92TMYE64FALC-Q_ypRyehJFYtAvjUfPuqVtSZguX2Jab6Z-QDI0jFS54gs3aZ7OSZ35bPcAzY6Z5Pv2jEZGnD4vO64EJuXPrrQFNFctLx8kLp3SY1P19YKb-cZq88IRk_sK9kLU3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ll4aIxg34U_v8MPb_0gfMI3BOBD7y_lSMJsFYT18VhILTlAMgMk7suFYwwvhNUOiqgEMdKFR_z0a6FeQ8CfaMfLKp1KaJ3VIlHVjpezlw6_DYf0VlYtOAwCE57wY8TPYyw5loulM3r4EVDRUHi3mcG5vTwmcXVamEAXo_bJsxT0f6PivWdx-puWtrgLsk0EyflxMr-snSTZK865cJZy7fXiuwy02Zv_8vfPuKGoXC6pA-XNEYOhGZDBYOUbsdzWHol1mlFo29XHN7-ZIlIuABkZAigKEVW-ZWnlgzwvT1-jVDNz-to5jg2L5eMAGP1hZyOmkq2tO_cEUfAs-jlGgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gy1uVZji_v8pIx8xevQu3A_V9v52JOvAne9mavL87PhdzLjB713VeQX8NdfDAJ2LlF7mZFKA61QlMFPmBuXciuHjxSOZ1hPYk_mT5D7vDozfY4V2096zzx3B1fmCKVduYVHtiJj26BUf-KEbCklh3EVsayAcs-wWogmczekkcJi3N7TA4Tuof946lqQ2HY-Hkj7sej2oPgePa-eqGX4y7wHTEpS5jmdzaJWhNMFIU1Krwzv7KKNkEW3iHFZvaRiJysmPAq4P9v9bp1hddgteTEhP-4cgGG7tElQ46p7hBxkkQIVhWexG3VTE_xcNJ5Hu88ShhNbbo7gG8Uow1fbDBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=ho2zrCZyhh-_qSkT8aWOXdnxk16SZ4MqFicsFLDZjGtfY2ussVftOAQmJEUsiWCi0mFh9Kpkm_lnaFrg5YgIIb3b1Mgnp5_iBSfRCWByFOAMxUYffBYSoHJjvUJ5RLJvSn7tsv17ClG68a11Js1ydWKglNjWtuhZ3VuTN0790d7Pd3Gxq4c8T9skYRlTReuSufrOvM86OBS0ckG9Oh02frjsnvb4OVjlbv4ouEnFEnV6_djIzdJ8HLskC6juyOvzgnLRc5Cnxd2njtTpoFvsuGf5h0PJ_RBmG2_GHyf_sAXepc_19BKdPSWTZYDkXsITne9DECzYDq_lxYg5jWiC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=ho2zrCZyhh-_qSkT8aWOXdnxk16SZ4MqFicsFLDZjGtfY2ussVftOAQmJEUsiWCi0mFh9Kpkm_lnaFrg5YgIIb3b1Mgnp5_iBSfRCWByFOAMxUYffBYSoHJjvUJ5RLJvSn7tsv17ClG68a11Js1ydWKglNjWtuhZ3VuTN0790d7Pd3Gxq4c8T9skYRlTReuSufrOvM86OBS0ckG9Oh02frjsnvb4OVjlbv4ouEnFEnV6_djIzdJ8HLskC6juyOvzgnLRc5Cnxd2njtTpoFvsuGf5h0PJ_RBmG2_GHyf_sAXepc_19BKdPSWTZYDkXsITne9DECzYDq_lxYg5jWiC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjcn7EMZGGs8dxCy9wB0fs3ygeIG5d-vvm0xf4Go2G642yVOPSw9JpQpF18Ef73LvV7iDD8x5MhxI9CZMnrBqmKxmK5kQyy-kibrieFMeNHnO-K176BsGCpAouNPyBQStkXCTWNJzotXfTk7JfXhSVWJmd72On4xGNOynwnCY-gHQtFxLRne5BMOQrEMAo2OEt4wGfANRkopJ_UoTEPy2hVa9hAZmEgscTX03doAmfHjyrAhvj2P4JRDOtLkSDyVGhhkNPJ6QwikIIbgssRIAoBgkTDY-cfXRiPppLOYotihBpdilOdNGZ7XGUrIzKTbmo45Q0PEMY6mmQzjMYRNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCwV9JOVZjoFzDLLofMaEQxFHQjq_6Ic5d-4HBMG088a2f6RgEGOe8EtmCcinwB0rcCubgjRXmAFWOF9FJ2jjlengSOSEXuJsuCyG1dxNc1kIdinHj2oQqqH6_TeBxXa8RpCu6sNmnEmM3N9MCkGO_hvrKcEpR0vJ54CTuxwtolDq7eeXkMFf638t6g549dxOEQfFle_iNPtB1Cjd5WKo-irH48uRYQVJADNak1wZE3gzBf7fhHC8Q9i07TiQldKKXm91LI1fDQlXAfwN4-sDBYbhmegacACdxAKBngMZbDcZ-fa2RMqnQJPU0JPmWDrfSOS9Z0pAqPT_Ga5qBPVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBxUTFJXjjrAeYNanB7OzkpOw9LP2xIJQvpb2XSNskUmJA4q39AbJZBalfVLFEQmGZfpZ6AjlKi4T9oTLcAfUtuNPbKSjYWUetUZPnhP-2cNiKhwZ7Y5-tMppBM2ejLI-uAvtJPnftmRTV1Es_6_XVBKg9QZA3dpGRFjv3aWl4l24PsJruDmYvALPTGtP9nR-EZ5P2UgQXKhRcJxv76RejcoP-cqIWEPdqr0eiiuLlN7766isxDzCWRdQLTx4bOeKod__-MDAAcgrSdf13uVBKuTVVFYA2Cx0roCVoxkP-N538LxFZOn2-FS_QrsGhziEGkWKFUfkj1tYOuswpypnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAe5vM08JuG9w3GIUXs-qEaPHRkabH_-fhSFJnIM4UFuGbKLDxB4qWbeXHrob2n_EW5krw9iSOLjSeiTztL10Ba5feTG0oN-h1ihT8kvZa8W-gtLDbrZcUOEZopTEsqnsxxbeLWktin7gtRpp4N_3EqKTTXEq-ydaA2SE4zPp6UDKmmSK0QEOI3Q66sG1oK5QfpOdrH8uR1TdEMwY2S3s099f_mky-vtrlqbykdGDLiBfPnqXBKXxhWz-DBzNsJI-jo4JJ9C_3d9R2cgu8H8ZqKWMe9BQOuoSoM6J48JeDt00hQrF1cn5ZJ-Uvc53LaMRq4ahAOX-vpFqZ6KR3k-uQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=AROOt7utO4HscS95S_9aY49VkVSYMWEzmePvI0bvCH992AduXCvqHSK0yJwwbbe3f02WoVKRRQw2j_1BZWViFoRdINqWO_6Zj1zzxLPF-7rRizL-qralpBnXtLm0munmi2Bn0YPdHlIWVBR41Ova5h_1Pqelj0Hu_D4V195idqYgv2duyKWJRFOlrzcWgvX2hz5kB7a6X7Scn7ulIwHgBS92_jgtsSfnbYk1Ilffi_Wsu_yd80JQ4ukq5VRUvxzJouHffadb2ir41F7POboScGq2xBTHdqud3x0lUnHVwp1lxwy7dOby1ONEYkAXl0gPI97paP1dCt2-8hr-wCcrNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=AROOt7utO4HscS95S_9aY49VkVSYMWEzmePvI0bvCH992AduXCvqHSK0yJwwbbe3f02WoVKRRQw2j_1BZWViFoRdINqWO_6Zj1zzxLPF-7rRizL-qralpBnXtLm0munmi2Bn0YPdHlIWVBR41Ova5h_1Pqelj0Hu_D4V195idqYgv2duyKWJRFOlrzcWgvX2hz5kB7a6X7Scn7ulIwHgBS92_jgtsSfnbYk1Ilffi_Wsu_yd80JQ4ukq5VRUvxzJouHffadb2ir41F7POboScGq2xBTHdqud3x0lUnHVwp1lxwy7dOby1ONEYkAXl0gPI97paP1dCt2-8hr-wCcrNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUxJZA0xZ6d0mjIChz-ythTYl0W3EUdFRcUO3dlWGSQvBSAt3fH0iOkS7QyRLVa1iMIksoyaWaEgZNZp__-1gHfqigjxWWSi5zwXrv5nHz5_5eio8uGjIccHO4MZw1OIQ0h6VxpTYwSi1AzvDCTLsb2yeGn85Mb5My8KhBpyDQL63UZkRJ5n77jflFEwjJY-4TA6MBjuTFQnr7958RDI8SLtU1ll63WEIkHFk6RpDFgfcguNSyUk6qM2tQ6q0D8VTwvmtRZLj-bTfM0y5g3aA5oY0tqOfIUri-w2quGq8TDL0iXBLS1PM5AJwbS7yZgR_YNmPOjpWrCFexiqwWNyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ub_DV9wTMl63Ofxro3E3jYfl8zjzoBvurW4qeMQRwPlObNMjLF-a-2pm5kLrdSEhLJlXPxaun-qHI7z4VzpW9XtPw5KW-UwStqce21t814LcQ-doYixABpFZ96amMsqp-KDg9KMB9XRzYOW4I0YAtsp6P3Ky-y56vBepluvElEL6ORjj4pLbTf-lR8bU6NAd7EfGP6iqK0E0dT5BPb3H9LggMuX1ifYD13ZyOkNvwSK0UT1xASdYrefe0UBup1piau87whBA5iT7wQkf_SOJ8zbflSxjVrAvspSrlrv47z_UaY43upKVDQrRqOtKuNwk3YeiJmF6VYNl7ayWW0xA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CICkBcp234yRKgx3W6dk-F0FXPh68t4mjUhNme9d7mxwpA_A2uoAX-RipKa18ksDKHCYCFcWoxd0uKhyeldZD4ByK9cVoMThHXU6wzeON1AIKfVikL4Tr28CXBAdHouWC-xNUHWG1ER_yxytG_8R51MyT4L2VUT5YPM9N20yCLteEAMQiGFbFUbQP8VXORQF8RGB-mg36i4tXNrm6Su1y59cmtf9NVbvh2DPrQjFRXOCuYe0oXEEggPy78brmmzNEASg9Cfv3TLPiFb0p4-gP53lB62esxRUGawV8nyZ9tUqUdxmHV7eSwRCMJAiubxtN6_GBYOqvTir7GxepdFlvA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=shezmz32HWdR8vSfhtKoGSeHD3-RO5EDw7aA9QaC7ro_JG4Ai_wOMtd9nufrZ2KkkQ6Oc40m80hnhgvR_vEFnGhms1EJRS5OxbajG00PSuJFD84nSPHaU_pe_ldnhaCw6ZB0cL-zQpVQEMXvwZOLWfsoIVZ3Em6ePXuMZEjsUPkb-wklqMrjTy-qu7uFs58UqjK-nVKUM19iF9Qe83fZODi4b43lovV_bzDo9Rc7MvsNpsbLRWWSe8trJlK06C2z_jU-D19ZotnqSEeHZea9HZCa0zUxCgG7LXqZWcgM1F6T5nD9aYmnP0aUQH7O8JbdliVIL7EuQXai-hSFhYuReQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=shezmz32HWdR8vSfhtKoGSeHD3-RO5EDw7aA9QaC7ro_JG4Ai_wOMtd9nufrZ2KkkQ6Oc40m80hnhgvR_vEFnGhms1EJRS5OxbajG00PSuJFD84nSPHaU_pe_ldnhaCw6ZB0cL-zQpVQEMXvwZOLWfsoIVZ3Em6ePXuMZEjsUPkb-wklqMrjTy-qu7uFs58UqjK-nVKUM19iF9Qe83fZODi4b43lovV_bzDo9Rc7MvsNpsbLRWWSe8trJlK06C2z_jU-D19ZotnqSEeHZea9HZCa0zUxCgG7LXqZWcgM1F6T5nD9aYmnP0aUQH7O8JbdliVIL7EuQXai-hSFhYuReQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=BnA18IHZAcZ3Mszs_BTQ9VKmLgurfDJd9cItKfV-c7oI8Vf69_GO5gJaJZk4-1ynDjf6w5uORif0Psh6yc9zWBdgdEVnZOcd4ciZeZfQ9tWEzsNNOZ0RfJaNFNTusWWis4s7xmhnsjr0d8WSBvRSpchJxxErf2RY1EFEYpco5j1cWbr6xiy49QENoQtGCw1sj1x7YH9BZtH84Syoo0eDexo5jQTgolM5o-jRZqzfDhvoZnCfCRGu-wWmCAy2QgTPrznUtYD3eHNkhXl5Q5xVOvcy3phZDNaCm6gwgEgVjna7VkSEnl7rRVL_6AIOyk86hfZalX6Hffs62o69Qc9w0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=BnA18IHZAcZ3Mszs_BTQ9VKmLgurfDJd9cItKfV-c7oI8Vf69_GO5gJaJZk4-1ynDjf6w5uORif0Psh6yc9zWBdgdEVnZOcd4ciZeZfQ9tWEzsNNOZ0RfJaNFNTusWWis4s7xmhnsjr0d8WSBvRSpchJxxErf2RY1EFEYpco5j1cWbr6xiy49QENoQtGCw1sj1x7YH9BZtH84Syoo0eDexo5jQTgolM5o-jRZqzfDhvoZnCfCRGu-wWmCAy2QgTPrznUtYD3eHNkhXl5Q5xVOvcy3phZDNaCm6gwgEgVjna7VkSEnl7rRVL_6AIOyk86hfZalX6Hffs62o69Qc9w0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=eN9g4Npo-hIv8sePANxcG5qunk0cyKrYL2KToJtigOVtQY1oMbseJS18sQi06GhSQgo9tRP0yULt12iFTENyfd4SEpIiB1KTjEqDqa1CDcQlJX2pmcBFMHfmaCKM_xi2b6Broj2rbLwvs_h-THSzZhWS1UtaMoLxBkm7wDmWxGX0_GtE8LpdC7O7NHImjIBrUv3mvGxc_1DUTnc63bPNo-SvocyUdq6Hy0SU5gCkrqud3W3u45jCPhFzrcInmFLl-bJSsaIvDVZV_yW-qTg5Rz92ec78i6lFwj4RpHobB56KSQZAIaGYIEEr2oBkL8Zp62on8BWCCrM7xX8nM5ewNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=eN9g4Npo-hIv8sePANxcG5qunk0cyKrYL2KToJtigOVtQY1oMbseJS18sQi06GhSQgo9tRP0yULt12iFTENyfd4SEpIiB1KTjEqDqa1CDcQlJX2pmcBFMHfmaCKM_xi2b6Broj2rbLwvs_h-THSzZhWS1UtaMoLxBkm7wDmWxGX0_GtE8LpdC7O7NHImjIBrUv3mvGxc_1DUTnc63bPNo-SvocyUdq6Hy0SU5gCkrqud3W3u45jCPhFzrcInmFLl-bJSsaIvDVZV_yW-qTg5Rz92ec78i6lFwj4RpHobB56KSQZAIaGYIEEr2oBkL8Zp62on8BWCCrM7xX8nM5ewNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejdkm_TADBJ1CYPOt-z3Y3gq_7QgVTmd0IkK7rjSpRTiMKJlaD_fWBkorm5hguiU2do5BOfEf7GFgRG1GsThCcB5GTg7k8wCOc6BO95pQEqJ0jgPEf5OlP1mFeS9ilr1z3m6dLLoQZwvNp0CLTTtcZND2rnkHDLDsJuQWnvybKBWTJgc-CSzxOulwMwoHsv2dZTlAv7pm_9yetoqVtigIvoBCukgIfX2WAEizPjBDflRPg9MbCFUu6S-yWKMk9KDo4ZUN5O3TmJsoD3Gj5TUp9jlOEkt4ImDNNkI8IOGULsH3eol3O5X6zcH_hUUiJnebI_LLCCt91EGSJ4efkqvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuOlJ5NNAN8BinoJFwf7UHTyeTslj1QtQBfOkENJAlHDBq6DRopokZkI0i-dRDCadnQUv12SUFcv6OLRZLmupFF-7-kxRMgLxXckZf5cw9BgbjANTPF107stbA3tDOj7n8le5zRHY8NV7OrcbH3qDJfBhnKHpiBc97YXPLOmQHSBA67gl3aooW4RIsAYnxpHBs1EL2_DC79jg31ic0ngQQP4FcZn6dpiHwb24DbaOPYGAWHsop1wo9yuii2jPKHzlme-WW1ZHET8sVxvg_gy6TBJ7DqvXUk1zoRSr_YF6JF1S61kpksemqGADMhbgDk3XexmBbnE8MCy5tI0l13V0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9qovhTnLxEyUnbTaSzTs8lRinEEAFf9uBaRtfHy135nlxAtbgjlzg24KsBL9IbuzDJwLjOmv4lCz41rBjM90EsE-cpd-5KDFvYsB3HlGQfLceh-Yw_VyFLJLOGTkcBIZ3Ac9s_aA7n6y0VNU49sxCf3wUwBrFQhpnh4QkVd7MNPl1ZGLa3LmM715ZTP83MGhoWJh4GJBkKfEe0vI68HbICuJZIAp-VZhCGfVHtKFE2tYaUF0riN5wKPYaVEM0RGfe61MjuQKoYyTdNosZ4YfS-n_QD1S9z07NgYJJPCH99x1Rn1N619E0hoCKHb2h2qDk6jq1Yo8HA6cSp42LFwgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTa-Yw4fZZMtl44iaV4I8-cgAUwp6Ekxg1AkxcRuAFkiIDUbFGJXUdLmGG5quaK1DASqesT2MF2f3HDOGqb5IXabAcnXBwFIrETYh8ayvqnxxKcmGbOxp2Jj7G24yHRZ1mBAm-7Ux437r9tFmrV-aLjDjJgOROyUVbe8byqfq1Sf0YAgTs7fitzLWh1evVDVmFCfVlxFUn9wWGq34CzUN3trG_f5aMCQVdaoANbP-L5IeUvRD76gLgp9kJrsScJZ_U8ZuccsTylGgbvXcuDfm7J7eDCdw4eJGZut33BSp2SDLESS3oq0hPu-JdnlXA4tvYidNn_6Ps5tuFxTW5_QOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htiwaSsqWzsFI6U7R4s_dFPkBfOoinnMYMlLrbJEEoha2bzCezdWHAubSs3IA5BmmKvBnY3L5hAomR6AY_W-9fvfgqL_HJ5nfyNZOmDu9Gsc2OhXHbSZHmjPejQiF6j8lUc2hcfUUD0_8XeEzhXES3bprHVp-QOpydAEv2blU4LUH0biy-iUbWNEnBf0R_FXm_uHblCYYt5M7dHJraZiMR7tdskhM_D0zfhHfnDlemOaCvOOhVMUbMiB8-yx1W12160wSWAmRpcEGsBuART-N4FkjH-v8Cj2G2v9akM63v4ei2OWVNbZa_ogHpqH-qw7r-8aQaeUEjs_UVvVTbkYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lt9XXryqOGvhtLMBOfXUmjxHTW1B8C84RCBP5xhargQfkHUQAWTyeHmyss3iphpybr-0fh8tC4f-uBztj4roXh5OegY5RsjBgKB9y2euwvElDhJsLOQvrruEOBLaSApK2UiNfwZbSJqub7w-mAvoo7aAzvMjorBVJ-3NdJZn3biAp2qzZu2XAKt-ZbwpfNY3XfGRAZ-2xAB4GhypRFUHiecmOq9pbfOqUMeSxGh9rPLP7GVBkvahHtGyGkND9a-ug1SnDoc3ulyRmYt6t0NzeuKsLX9ZfaO64ZzeyB5z3hU8rWtzogeo_Q1T1zucPTDYmxpnyYrnezc75ENiNy9VEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wq83-GlmwIfRXW5jvmcQFR6moqalWO7dSSLPLwoHwOWLrv9q1GuB5z7Hjk77kUkN7tq9zzxlS9GFJefiyik8Gp2tjHJBo-PT5I1SknGzwCWIAByYLUwYvXq1WO4jqYqfMwspwXZv-3lBX-HUUPb6JpCvBNDCxrPvGTGgNuuhKdi-TMKc45VoQJbJbszqzSUMr1Kav-QboGHWK2ryGhs329UzkiRXOWSk6DClffaqB7GW_jXx4ZSWQDt0iVMvJEYQIxEKBtAwPh5nORD094AGBgwEnc-R-EFPiqSGCTO-AquJgK_YPcY55tMyaO8-uE4REOPjPCqtlJwxkapZnjOehw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JADkbUjR8rB5vZT1DDDnC9NlllssRypAx5Ei04JkhZqW6KE4Skx0hqBSFevLkz4gbaoHCUK16MCR19kK4wifRll7KcCXeGQm01uKiZmv8c-8JLvggy-yNHW9OntCFb6nDq-4AAl5aZEFHiDRYHsNfQltdm1lcxIML88C5LdLL-CEjMNogKRoR251AwlmOAy2x_ZGJKdM5Z95DUTpxZx_1tSgkDIXIFmOFea-zrEQaZjoCvYRiXS56jTW9Ow-Aj5D4uAz5TBQfl_cZxGfqyss4RH6SbGHaHDxhkXscOar2uHfeOd_5XznMXphCRwSjte6NmwzQ67qOFOiZKUyrXfP2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNSr9ftBAETxApHzxKZXUNEiUspYFYfaauXOLVmd6ifsxKSyEXmAQ0qtGM3-th5vgp22anSSfC62SBuyK72gQzZqsV1DGp0D68Cfo34c5aGnq-45_OgsdhA7UsVrMIGdQSb_7WR7NNULcCx1ckizJNN_HXCvom2gqbIMf2yJIQ440WJ9XYgAF1Q7ZDmVMBmVUR9jD0l3NEN5oQiERFB6Emdjb-8FRaVPtNNq8111C9uF_nhywEv_bFNDImxKLNH2-XJCbdDXKNAD8Ys8B0GcCUovcGCDIFGMG7YGaBX8-qTN58eqTdubGyzjtmZlmgGCEf7Bn-W8o4ZcMgsyHd24Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhTthsHOUuJKc8925ny22YkJi9atskGAlITerwoLgyfOF1kpejUF_O9DuZSaAQ18ULBXpVYc0OHm8zIl-K0QTKrtYnua5pzZuCooGjX8aFLrpzeHcumjt4ASiIGJfUGgRQzLj6f_Fjj2WleFLnvSyluh4f6UzAxqoZDQIiHiOa_DK13OUtpyWBVC4VLVAjErCIvo38ugWHum5WHjyZKLNrKTmmxWc528t-h_UN0ElUu5JGguTFGdleptdSci7W_29q3XQ01X-WEewd_KXC2laTHbYNsltNFFXhPaHb9L_EgSVIfSLYKj67-6TlSaj6_YaMAvC1Onq4e4mI89heXd3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoI_NoP3qgbYJp3anqhWI_oqOxhLHCBVHXfKUTZ2lxH-m1gob2YCwxDslbWaG8WG69HKErXyGSvLfvf7wexmiVOhCy0zHggfSdJJO3C039Vs0-MDhvSDmK-b2pxC18Y71cO_5gPjJrVtpv48QJUNuDP-IaYMxoMdH8-LMsgF3aPveZ0dNmxGR9CLa5AhmZIxAvmytB-0AOppdiEtSfkC-ikMJkjYDAFkemJgDZBxUW62WDwKPf3xvp95IPv72TbgJB2sXJ2ITwcBbStSrWhkrz_aknOtmdoAmo2-SOq7VtcE4J8PANwUxuaVQDg_iY_Gvcc0GlrY20uwvepRM8Ajwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-T9cTpc-kzoeLESViX0eY9FXV6fNjCo2sNA3n84P4PjSgRKU3PCzuP8BofXq795sJtKctEi9u0uXBXTvS5B5BBUUX0NbCcNLrtYRLyR3U9TS0OhLfZkoXMtiD3jCMJXn6IVVBChj_qz6CRVQ0EntnLIc3AJGP9koSYplzxTN3IcbF6uFIW5zyk3e6nrSVsYVqQC_02xQbe7rJkbPyr0kSUG44VgOD3tZOwFe1BrWDwYYzdc2UVGYmRZlwp10f-G0k9QYYvgYuWIZo75OOfJsBYhh1X1bqemKBBb9Zt6E5c43vZMA9ZZNJ-jVh1g0ykRZiQD5k7lwF3vXV2fsmjRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqMlj4ll7rT43g-nEVbzVFwS3lvgbA9YYnFp5sqfDCIf_17nao3-qlk1_JUkUk62EV92wKmXYoAWRMMuI0QN6dh2U_da0SyIPWER1TbzL2DMxzh5bpjBvYxpzvystq_oolM2UrgEBsC3qtdJm0E_ROPScCxRM4YjAiXglAwhNRe_RJkeM1OwjEH1mLRDw4PniSfGv2FAUxwbhp8tqS2Bptn7Gf7tOQUlQBOS1olQjs_p8XFixnb4ahzUhSH9PvYmVpiFd4M7iFGzSwTjmSjIeLzdIU6wexNYUC9HF-dLCHn7JLZKkNKV8PYhpLHldg-RZn-WDM0jCVzDsejfxC6TUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2RFkd0ERlmWoE_pdrk2zV2lHTnEtZFx-j4ftkseXbP-jKvBjnyGD8O1rvx0nERupwhwboZztCKqcnhgwo6lCyfsngtpbVt7bJ2s9rtF-rX7i3XCBb-Yjnc-vF4OxJMUeJ5DFt-vc8XHyyr7BHjq4iV7pMWijMCooqp2-ZDsTveFVxIyu7HVfA3joE6jovnSXzZAwXV0U__Qw44xt9x-35XRXY8QmmkA1L_EuzKqhlbmOy8SQMJ8fJ7i61mn5gbxZ_ii3IGCeScwgZE-ISXBK0OmsbEdp1IsFrRman7hSIk9MIDx3DQXKheilfxEiicQsgeFvVCDGoogHTmp8lbTwQ.jpg" alt="photo" loading="lazy"/></div>
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
