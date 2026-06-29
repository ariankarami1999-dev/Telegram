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
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 18:01:45</div>
<hr>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvztdfVtj9TfByy9vnraHfetouPFFNNQ7M1mSDFN9PsWO9nZmlU-_SU8KSxxzWOvPJHFb9l3sbbzS1vOSYIS3ERYaR0gD4S8VlFBsU5z9VWH5YogCVTsFkKTLwDMXex_hVBP94EaZS5S8t_BkPSsIBS2CuSeRjk6voR6QnHTVTUe7JJ1tMvzQA_5dQqFWLNmo56zzFTsip_AS_jJ9RjDKnC9quVXkR5i-O1-k4lk6-ygBaaN91OuFicUO3JTAWIGPEFKGYKcs0vP-xKBYgkD6PWK1S87hPAUgTzbNRRV0tAwOoDFadfm3ZGhVBKrTMOnUaBvbdap64KhpVAPcxwlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YoA_jkol-01mjn0tXCS0NIBGUESMY858Ks4TjKmXysUaNUQ4NY5DoYZq89DW4Ju4XckW5d-eSPIHckGSlLZvok47mpkbmz03rBF23VulaysoRIC7LYgpg9O8U-Eb7Vo_wU1sp4NENVO81MHPx7dMUMcDNsziWpRy600htyci2PbNbyTNU_jAVw0ortEm6I5iLLgwKKfomdbGnYYrl4nZAbpIwlyqMbAajxGYKEpCfLvM-JzF2r71TEYo4B-a_Pbq01xeSvh991Qg9zzhvkf-lTMseZM4KV_4CAuvrxdTuu1u-CYnVoTOWcCySjJ_JqLW5uFI3fvOQkA-O992h6UXDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YoA_jkol-01mjn0tXCS0NIBGUESMY858Ks4TjKmXysUaNUQ4NY5DoYZq89DW4Ju4XckW5d-eSPIHckGSlLZvok47mpkbmz03rBF23VulaysoRIC7LYgpg9O8U-Eb7Vo_wU1sp4NENVO81MHPx7dMUMcDNsziWpRy600htyci2PbNbyTNU_jAVw0ortEm6I5iLLgwKKfomdbGnYYrl4nZAbpIwlyqMbAajxGYKEpCfLvM-JzF2r71TEYo4B-a_Pbq01xeSvh991Qg9zzhvkf-lTMseZM4KV_4CAuvrxdTuu1u-CYnVoTOWcCySjJ_JqLW5uFI3fvOQkA-O992h6UXDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP4vT26DbMfIlfgLMivVG7lutp701B9ejeapkLI0VrzVKU8LB7Rpp-MYYvHCktEgy4TwPnuSREmON4Wgqnpg6e94h0JY4LkYOnXPMN38jKz_2CxCvBFyMVUv5IqKYHIOzI_iupWrldaIQCXB6B3dJ_1nmo1ISta0JCFR6TuCeRLpsT2FxwY-Cs__7LdOwJPjdg5OhJo-vLfkb4KDFDmmR0c8r7vByxc-jJQ0sbH-anD6KNOyB0dAep2LXVaWTZQKuX5ov48GOGDHNaA5KTuY-9ndEiIVOpMPW7skJsiSszP25K61fdyg0ON5xH1NR0p3yNkRHfuewrO_X29ytGiHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=MW8nk1iiOKI5oRJSTf0sRhgfCozVkHxqjg2gTJx7i0PgcuaJ7V7MP8EjvGxFQAqAmGFjw2SgKgB2UQkSffNMVAmS07IFR-nnx96XKHfk9E2Tna_EFd_tejJUH3pN-3wIH3JLRpvoc2mp6eBi2DD2BfT0Q5wiNkkSA7T-ib3ebK9jrH8Ebj03RKY3MCVfJfOTR_ue6EJlXnaby4DeTcB5A2Y5sUMu9oN4fW8BeGsJuGKYb5NJ95WPYTYdYRMXToP2--DFmyBIp0NrfJcAqmYcnVFcO1CX-xDEL9VDVKFD3NHFkX3rgN5Am89iC83u0tHqHuELtmXPoClBu_eN2EYR-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=MW8nk1iiOKI5oRJSTf0sRhgfCozVkHxqjg2gTJx7i0PgcuaJ7V7MP8EjvGxFQAqAmGFjw2SgKgB2UQkSffNMVAmS07IFR-nnx96XKHfk9E2Tna_EFd_tejJUH3pN-3wIH3JLRpvoc2mp6eBi2DD2BfT0Q5wiNkkSA7T-ib3ebK9jrH8Ebj03RKY3MCVfJfOTR_ue6EJlXnaby4DeTcB5A2Y5sUMu9oN4fW8BeGsJuGKYb5NJ95WPYTYdYRMXToP2--DFmyBIp0NrfJcAqmYcnVFcO1CX-xDEL9VDVKFD3NHFkX3rgN5Am89iC83u0tHqHuELtmXPoClBu_eN2EYR-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=ZFIX5t4jrKDnvoXPC0lQb5Rg-J4lpUoiazeBGmajiDCBzG22o7SYthkXQsCWD314UVsve1tLVUGSBJZmnR17Khz5JFznXp3cG8TBejkkLuVCOvtLlREcz1dDeHMdctBbF6MwRVYLTwuDZ8yaKzPhAjoKIgCBx5B0KSGnwVryyazslzyD-zufk2Zx5QOc_x1fmEcoB5A6skMbJxQAQFHsfsUwAwnNE4Z3ieH05eOcmSgEsKxTdEbBdw8hRD3Hkbvi6dRXUTAWUWEculbLSuBfLZj771ntjYnz2jnnQ0SgYTpRTI8BMoJkLdQqcRBzR4mGrGaqqaH6wIti_Ieqpk5MTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=ZFIX5t4jrKDnvoXPC0lQb5Rg-J4lpUoiazeBGmajiDCBzG22o7SYthkXQsCWD314UVsve1tLVUGSBJZmnR17Khz5JFznXp3cG8TBejkkLuVCOvtLlREcz1dDeHMdctBbF6MwRVYLTwuDZ8yaKzPhAjoKIgCBx5B0KSGnwVryyazslzyD-zufk2Zx5QOc_x1fmEcoB5A6skMbJxQAQFHsfsUwAwnNE4Z3ieH05eOcmSgEsKxTdEbBdw8hRD3Hkbvi6dRXUTAWUWEculbLSuBfLZj771ntjYnz2jnnQ0SgYTpRTI8BMoJkLdQqcRBzR4mGrGaqqaH6wIti_Ieqpk5MTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=EawzLfmnnhkO1NvKBNpilZLzY0MpGeEXK6ng3Q9tw07liC6BCXRdwzGJMY0G_R0RpiUpJ89-6lVX2cizkHHpAMyzzhKaN6EE8UvKKEtlKtKzpoNIYUrc0JEvHexdWxaPFfOqTbP1Pr8vZcd_n9eVB9gro7QbDO_1p7Z3jAhkagJI1fa4OFivaFWQ1qR0fxd2vxmFvmQGxaFRASzbx4iH6rfGqqgybr45DJUGiFhbO0iR41NfKCkbaYiftmOddPJJmIQVVR7fDnYIBgLVA1EHi8mUKRWCcwOv0fuylgxQlKw9Laq0aKCCY1RzSK9Nhl-OHy1n_HsZlivoxM348Vu9LjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=EawzLfmnnhkO1NvKBNpilZLzY0MpGeEXK6ng3Q9tw07liC6BCXRdwzGJMY0G_R0RpiUpJ89-6lVX2cizkHHpAMyzzhKaN6EE8UvKKEtlKtKzpoNIYUrc0JEvHexdWxaPFfOqTbP1Pr8vZcd_n9eVB9gro7QbDO_1p7Z3jAhkagJI1fa4OFivaFWQ1qR0fxd2vxmFvmQGxaFRASzbx4iH6rfGqqgybr45DJUGiFhbO0iR41NfKCkbaYiftmOddPJJmIQVVR7fDnYIBgLVA1EHi8mUKRWCcwOv0fuylgxQlKw9Laq0aKCCY1RzSK9Nhl-OHy1n_HsZlivoxM348Vu9LjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_UxmDd4i6rWFga5Y3jH6gL6zSB79aIQUS_4TF4c35uGCHXY4z2SFb7s550j13fj3tfEmEJkOnBsAySN3m8q3ocR65ukT4uuu0AHrE_3aVKTaDZTB309mzMISI_6B04inobD9oKBvb8fq7aD1FG-HmLgAxyIXwLEPo5M2ZKRHAfG1DvtipRxA9RYyaMkalrBATb60BzUfKy7DH2us7-YGRmHOv1sQjzMnt9SqNTeVlEQuspmNISj_nwl78v0Y-gkQ3q2kaSMcC5fNT4Uv5x1JSdY63hUs0_KObZXNsMAP2EXesV70gnWztosoLDCK3XgVH_LJ3N5Re3ZAMZQF-qDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsNPpN_H-kay-fxUee76M231nFEJfKBJ9WK8Vh8p85shEvHdsFpsG6_8YqxUVT-4RyzzIFVDzTUciqsE2EM7x3YZa0-lSTFS18WHzaO028pCWOxJtB4X_oIrCMHATGz9CTPU4trC5c4Io7MS6q7_CMlVFFETi7Ep9uFc6R7jL_wB-shXvU5DLdHaBsXCDEb0qBycVavFNJBFw36NV59IdahMXmlsy5mDz4ILtpOHB1ZA7Q_e8pEEvsaq7V1BAxtk68hghIBtOvczBv4PCQqTNTPzYl_7aYeTalJv3XB3ckdaGohs604aStIzLQoq-KsvLLnIhGnJZy6Ypi39X94Y6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUvStLJEoQ9PSh8Ojb55vhlSYG92YvddikEJ5b27G3lAigDnfKoxoSsGFbapjydTGfC5169RDAdkNI3k2dYKGfovbaHss55j5eZMVtSKDB39LBvgduAPL5UyI3PTX7sbfbP_ucGW0ZlI-2XZ3JlT2jHU6lxLtku4j_Di6_-dZgMQR-LciKFhyDVv5iave32bORFEGPZ5NjVu4HflupPVEk29HK3LjkxI2qry5kdBuWZf1eWHGg-MF__-Z5irTMxYgYAkmILpusmbLd2RileZ7fssKtj_Mu-Rq6XE9NhwFVbIuLHf-vM8cBZ3PAWjdLbvPfXx8f1MMMOR61FDgv8-dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=Wr4_otdIjfYBoSe1Qnw_9_AbdlO0EhWp1W6bUUnd0gfSGWUHsohBim0l9s8JnQ2dqhJ32PARi9nvh2ueXr14VazOlv2b7ucIrcompg5WJIthY-r8brJC1pVPfcvvrOPYceuSgB0YWU1JFuO2JBe8uoGObIFtz5F3Zipe9V2DCLAnsOdtyx21tJbIyGDO4OBqZpgSnGC6dNNjxVIqkmJlk_wZNFzxfAPpzsaXH7A_4r__QQ_VJDy3anW44vechNjU9dZm-uc9fcqCJx7-rBiA2hnyf5aQZofxXeQeV3GMkTDV1BAIoNxLEtk_RAXCJngib9ET4eRRDqJWlGDmteo3lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=Wr4_otdIjfYBoSe1Qnw_9_AbdlO0EhWp1W6bUUnd0gfSGWUHsohBim0l9s8JnQ2dqhJ32PARi9nvh2ueXr14VazOlv2b7ucIrcompg5WJIthY-r8brJC1pVPfcvvrOPYceuSgB0YWU1JFuO2JBe8uoGObIFtz5F3Zipe9V2DCLAnsOdtyx21tJbIyGDO4OBqZpgSnGC6dNNjxVIqkmJlk_wZNFzxfAPpzsaXH7A_4r__QQ_VJDy3anW44vechNjU9dZm-uc9fcqCJx7-rBiA2hnyf5aQZofxXeQeV3GMkTDV1BAIoNxLEtk_RAXCJngib9ET4eRRDqJWlGDmteo3lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYCUaWjaL6fhp28DQIeIoZJrMa9PKqj-uBHedzFeWkol9Z8yBF2bdiBUTmK2yzff_8QuL6PFaiNvE1dX5lXZq2C4fT-w_R0xZoZ-FurueyOAYuplTkXKgfifLL2tLrUWsXThYB44t8HSQd9vPFQYzGvDG7Cfb3AGfwnFUZlHe-AxASXwBAn1dyJMUEj6yN47bOtsAOnb9ye8nHCr0kKTH73vLOUljbk6ICHrFEhytus5P8L88ITGJtPGP6Z3KbZfun2tIPeKNww3p0axNXWJEfP3PHiiAbkrI2dHKHoHPecbzL_MWJIn5gjnep0FUcnVJZRUREWFjUhtawkLCAf7g6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYCUaWjaL6fhp28DQIeIoZJrMa9PKqj-uBHedzFeWkol9Z8yBF2bdiBUTmK2yzff_8QuL6PFaiNvE1dX5lXZq2C4fT-w_R0xZoZ-FurueyOAYuplTkXKgfifLL2tLrUWsXThYB44t8HSQd9vPFQYzGvDG7Cfb3AGfwnFUZlHe-AxASXwBAn1dyJMUEj6yN47bOtsAOnb9ye8nHCr0kKTH73vLOUljbk6ICHrFEhytus5P8L88ITGJtPGP6Z3KbZfun2tIPeKNww3p0axNXWJEfP3PHiiAbkrI2dHKHoHPecbzL_MWJIn5gjnep0FUcnVJZRUREWFjUhtawkLCAf7g6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=cnNsCLTlUFzxbDy4En-pjeSejIv79_dv9KCt1b0HO4yhk-mZ7jHV5y2BTVf1ZSfBAVdac1R4_0VZF-A7bdteQydzNaJM6mFSml2z0vjV30ZfIvJGjJ2xG8JnH_VBu80w1P4ow7Db8gTIEh2eXGCbGCWZHt_bWQd-Al00rfP53UW7YpX2KlKKS3SVRpgCUJXDxIl8bqYMbyf6Hj343y4Fj4dKZ1vGaBfHHUSG6_xRFHbiTMWOKEkw_X9Ns8Im02UJZ_dMW5ndiMfiGuLle9XrQiQctNRZnfVhKcgp_OYOJxIuWBZtbUUFlyWO5quF4zB__IYbOw4BdVLEV0nsou_8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=cnNsCLTlUFzxbDy4En-pjeSejIv79_dv9KCt1b0HO4yhk-mZ7jHV5y2BTVf1ZSfBAVdac1R4_0VZF-A7bdteQydzNaJM6mFSml2z0vjV30ZfIvJGjJ2xG8JnH_VBu80w1P4ow7Db8gTIEh2eXGCbGCWZHt_bWQd-Al00rfP53UW7YpX2KlKKS3SVRpgCUJXDxIl8bqYMbyf6Hj343y4Fj4dKZ1vGaBfHHUSG6_xRFHbiTMWOKEkw_X9Ns8Im02UJZ_dMW5ndiMfiGuLle9XrQiQctNRZnfVhKcgp_OYOJxIuWBZtbUUFlyWO5quF4zB__IYbOw4BdVLEV0nsou_8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLjAxTu9rpg5-Q-CwE9XjRU3B4GujVPWStTddUEHfMh2wSvyW_8NcWGAD7T7vPQHPE8_iLgeLIVr-1PJeKV2mVUC_gDAQwrZAyQeW9kDQGeNazEZXWXwgUzGZ154llvOQKLLJ7BM8AbCnEoWxSGfq6vs-KuIF6Zv6DKsxo1TSaWKqiluS-d-595VXQu8DjqpeTsQ_voiB4ID-PsRWwAW50Jt6vPiyAoFH8pxT2KyZOLXWkb5534atG5C02WDDGrmFjCjMrStomhBCEhadrQTubt1KZk2OvxWc71FRvjhSC4OFj5MNZ7wdp-K_M-IZA9XMUnGy0K5ti2kWPu2-btEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuToYPFPFAqyOyKlXpZO4JVBVObOoE9SmNa2iYiUUzv7BliNHaS1w8D2qunZpn9hYTYnQGxShb7evvOKF7Rh8HfgTMGnQ6Ah7X-eTbrNj_kaW3m-HJ6zfEJxfyvDQ0IjYFne0tj_SW3gjI84CfNbFbfW58IqlJjDc-DWpQEFZGidJTZU0jqI3_Lia5iwyBAvUJH8RzC6tEg_Bm0cuWGj1E9EQ4ORT9YY-BWNsTqCj8h6KwrQICjrg1RTFmiEjIqcRSniCFMUEI-oAiFrM6vJN6QhNh5mentUbsSvqyniKmnUseQWgqkEM4Y99EBaSwbvqVDtb8Y-dg2WQq7COYNcj0CCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuToYPFPFAqyOyKlXpZO4JVBVObOoE9SmNa2iYiUUzv7BliNHaS1w8D2qunZpn9hYTYnQGxShb7evvOKF7Rh8HfgTMGnQ6Ah7X-eTbrNj_kaW3m-HJ6zfEJxfyvDQ0IjYFne0tj_SW3gjI84CfNbFbfW58IqlJjDc-DWpQEFZGidJTZU0jqI3_Lia5iwyBAvUJH8RzC6tEg_Bm0cuWGj1E9EQ4ORT9YY-BWNsTqCj8h6KwrQICjrg1RTFmiEjIqcRSniCFMUEI-oAiFrM6vJN6QhNh5mentUbsSvqyniKmnUseQWgqkEM4Y99EBaSwbvqVDtb8Y-dg2WQq7COYNcj0CCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGcfEmKRs6iC0KVT3O8CupBswFT-rQ-w5E6ijyFHykc2c-Dj_2aKwnREexFGq1fCKGdMP87eMuwevCqsnw_48Qw6DT1ImIPMwMkzMy5twxD4RVYZ7YaYwz_2-OOknm9J_DEsVnyjpfigu0OgEcRPO-09CrZKuYniZriBBIsVoiP4P_IisTAAF_sIZdZj_RF24Xds4-a5oT87KEfr7X3g93b0zRiqsbAC0H-ITx4yaKjWac21iDRzDOwaFsQ89S8GnabORoYiYWtuU1UOwFalpjA-2R9pe1eyoEuqpmALXFYK5gL7MEIA7ho7u0BsyXiGSjjEhBhS1UNh0vhqtKqlLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OUShO9IGzb_BwITRSMzDloBdk4u4f2HO21WaPUgfny_dV_DiCafjEgVlhWtjO5onMqC07CetC_Rc1IDwGfBgHvBvZGgfihv2BhAjotBq5OYSNa-97AYfjNDHnOf9N_TD8G5y49RB7gF4x9-5aHGcYsE8dZwm0Qmk1tVgPeswWGvUDhXzqSrcjDtArRLEx8QF-kmeReDrD0kmKfrhYfdnVCx53-NJAuFTKXg1BQXLIPMWkO4tpzbiJl0xZ8FGe66TYNYIERmXCeFaZZSoyHaDzvJPO2GnwMswm-6ZiP54DGvJP5Woc2V3GopwptvKQmtl6NzT2_kzbv5ty-6LdRicfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OUShO9IGzb_BwITRSMzDloBdk4u4f2HO21WaPUgfny_dV_DiCafjEgVlhWtjO5onMqC07CetC_Rc1IDwGfBgHvBvZGgfihv2BhAjotBq5OYSNa-97AYfjNDHnOf9N_TD8G5y49RB7gF4x9-5aHGcYsE8dZwm0Qmk1tVgPeswWGvUDhXzqSrcjDtArRLEx8QF-kmeReDrD0kmKfrhYfdnVCx53-NJAuFTKXg1BQXLIPMWkO4tpzbiJl0xZ8FGe66TYNYIERmXCeFaZZSoyHaDzvJPO2GnwMswm-6ZiP54DGvJP5Woc2V3GopwptvKQmtl6NzT2_kzbv5ty-6LdRicfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=q_tE-2-wTlc5C1njzUp2u0HAjI24MgeYZMKqGhVtyXIHji2AAGZLuvEGTtIrruhHLptS03fe5-O-J2i871ElCy0CEfgCSutjC_6VMLGtHohudMujTZh12yLeuVQjrYp-_IS70E3ur8CyuAg_R42kin6Ew-pIH2MuQQbeP2niqF-AacnKpdrZ58QoRzeWaRzzxJeL8QPMNKsSqb3GJsGbPDnKYt6BdXi1ThLPxPp6DkAdhoCkEtTCbHEXZXZKVwQVxUVbJTGyMpAi75B4CLvpbIEJVbfOaeOjqVaoOf59-LIpEHQ2FoTviJLr8WNZbtZR7RvUKtHxnSiqFOerxmpzag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=q_tE-2-wTlc5C1njzUp2u0HAjI24MgeYZMKqGhVtyXIHji2AAGZLuvEGTtIrruhHLptS03fe5-O-J2i871ElCy0CEfgCSutjC_6VMLGtHohudMujTZh12yLeuVQjrYp-_IS70E3ur8CyuAg_R42kin6Ew-pIH2MuQQbeP2niqF-AacnKpdrZ58QoRzeWaRzzxJeL8QPMNKsSqb3GJsGbPDnKYt6BdXi1ThLPxPp6DkAdhoCkEtTCbHEXZXZKVwQVxUVbJTGyMpAi75B4CLvpbIEJVbfOaeOjqVaoOf59-LIpEHQ2FoTviJLr8WNZbtZR7RvUKtHxnSiqFOerxmpzag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=MWx9ErPtXT-NTbIp3EYzp7iYyxgayKSf9pt4RQv9vufUrI4NcCGJqspc2z-mFOkOKFfSD2pDDjf_oNlQb9iWQIR-sHCWiNVDG8gQSA9hRwh2dWBoG-i_1Imep5fI49TYqTxN0_RWqFqM4-_T0GiP95JysHFQjUTPN1AcPc3bDJ35Z-9ujxpOda7vFEQRxJ96VJOst626Y8p3JC9sJCtJPGmLdY6lWNs2kto5WsKP5G8FngNmUMycZK7G2MBw1wGz1AZDkUhrDvhL-TCyUBDbe1MhkAb29yYuek4ezz3nCrVK2nBsg9pP6A0udAIzOO6AaSpi17PcEFpzREL7VZH0ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=MWx9ErPtXT-NTbIp3EYzp7iYyxgayKSf9pt4RQv9vufUrI4NcCGJqspc2z-mFOkOKFfSD2pDDjf_oNlQb9iWQIR-sHCWiNVDG8gQSA9hRwh2dWBoG-i_1Imep5fI49TYqTxN0_RWqFqM4-_T0GiP95JysHFQjUTPN1AcPc3bDJ35Z-9ujxpOda7vFEQRxJ96VJOst626Y8p3JC9sJCtJPGmLdY6lWNs2kto5WsKP5G8FngNmUMycZK7G2MBw1wGz1AZDkUhrDvhL-TCyUBDbe1MhkAb29yYuek4ezz3nCrVK2nBsg9pP6A0udAIzOO6AaSpi17PcEFpzREL7VZH0ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJjW8fJfTMRrv05yYS4NyyWMOeWialA3x7sIR8IsOT_ooE0VXtNjK0mDrnz6_ll7tEWDSWQiZjdQrclYSh4uvdtIbuStEFTGlAFKqtZ0oOTTgf2GvdA0FJ7jhlrjQFLGtbJiGPyyz7pZ5gnwY6CdEMWLCbeWJxiO4IEGWvLJr3fL6i4J1fAnfIhrRnEWksvTKMP65X7Wd5OmBSRAZpD3gVSf37uP-8fGkfRmsmWQ18pawit7NSXg-mH8yh3P9dWygpWRRYCE23qIptHDTQubdrxtKf1ybp2ATXRS-CldqV5MEbfqE4PaJNH9w3e6ryqV1OP9lI0imPzhsL1iyb43Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTWqhwpUtTXJOTQ4ChhQqsL2C-oGAgAx9bl6BniZAC3BJfhRCdrBf-kKL8c7DeXqJes6PBigpVp5K4k6VtFJLCD2IeZflngSt4M9e0vlRQ_sFKBBpmLFz0u9yrGhDVL_G9Xi1fde3OR7L8gtXvyDoJtVlyCXRDOJO4Lw4O3ot9OI4FbBzTLzS272VHA_ilx8XR8DNhEDerg0UUziU-km4rbJk-3zNlZ3sdVaaa3zQNtsMhmdPzi0K3d5cqX2Dmv-Yy0gLbOutWgg6xMi8OdzuQbDziLqbELuzBGchZuIAUXXbpsK1Oh6uhQBchMV1sMG5eGIMn1-0E9n-gyVYWBDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=BCuy9iebf3OJI-9gifdVSokUiZ7FyzkuZUcic1QuMekWYyPpyTczk3zbSu8og0U0dn2SGhT4JzZfFS4LSvzSXIusGSQTNvRAJp8aEmYCIUqzBE94ApthgSQ5wdSXxPDEcz6QbRVL_Hfj0IsckvHBwWy0jNgMWdCVWQnGNtmEPanuNUHkPwS58LuAENU_FHe7tfN0AWWeKs5lRmv84iIlVgjvzwBm3xAqk_l0WpRmUgVT9AAKKXkvdp86QMB8eZ7Zz4z7kdVhcpZ6zdlTeETBBPGLt-KTi0m0lIasAHBmglMNnyosFHEyqABc_ROGVIHZFn6yjl1jmxBKcwHbu50OIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=BCuy9iebf3OJI-9gifdVSokUiZ7FyzkuZUcic1QuMekWYyPpyTczk3zbSu8og0U0dn2SGhT4JzZfFS4LSvzSXIusGSQTNvRAJp8aEmYCIUqzBE94ApthgSQ5wdSXxPDEcz6QbRVL_Hfj0IsckvHBwWy0jNgMWdCVWQnGNtmEPanuNUHkPwS58LuAENU_FHe7tfN0AWWeKs5lRmv84iIlVgjvzwBm3xAqk_l0WpRmUgVT9AAKKXkvdp86QMB8eZ7Zz4z7kdVhcpZ6zdlTeETBBPGLt-KTi0m0lIasAHBmglMNnyosFHEyqABc_ROGVIHZFn6yjl1jmxBKcwHbu50OIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0V5af6mNQPRX0tNwsUKhVB2s9VftQm3tzYz5kYFH2dFbNcGI2HoIwD5hOTIpsRgRHTE8191B_CU9UnGvcko1t2R3vl5xC-a21Kdm7X6BZZUMU4dn-b47oVTXZ3MwbU56ENvKrFKOwje0M40g8vZ3A4vDTd88sW7AU_k8HvYqUdYAeDzkESTM4spaMxsju0qSjxbh9YjrBwupnJuzaxgjMiv_jSGlH_grOUNo95nWB9koHeA2yF-sddoZYn0L3wxGy5hbJwIj-_mYmGUTCjpDHDScrltbljXK1DUSQ6W2GGCHaqEiwQD6Fbaczs1B8K0ece61LXGt5ZLOvhf2ERATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFEmrz8p3cHis4dwNmhSW0rMJ54MtFayyuxqraEkFd4amp3bV1pVB2V_Z2OJ9y9NqZwV32lnB_MZ5qtMh23czp780YiHdh0smclYQpafhFD_lknUf25ipM3naM_AgPRcyfhjRGqvXhi5DuB4Vbb3qaHd17Lcu6MGy_z8rTQkeW5h0ww_FZRH-AK3FKaEdacg6FDZuNvqmsHccRs2lchJHDscJyD_G8aOwJ2PR2Vpz4b3muGpimcysSKK3flYL1EyK0jLcQlhM5LSuj2TPFx_FPCe8pQNN7RCTp-GSSMfFlYfEWWJN4fJTRDL6mCgowd25lOYfF5NulhMFWcphDpDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=lw2HsuyzqOKJ8LWSRy1CetGqo_7vC6GhECBvLCg5hotjzCByfkAXS-VoHvzAUyx0-fPQcQpiSV749SmlwPEdSrrkjw4pmtqagmYiTp4ZPPUO1HcNwMRAa-QLOXZUH8EBetTHJB5TVQ5MBsi1RDmAUk1CRWwGzYV-LeE0zXIBgd_zI6CKMu6HnPjbwnjwDe_qupoeNkxAaRp_jmiIukArT5fOFg3rLdFAY9-JB8WO-AZK8Vf7x__n9hiHqq6_HdKtxJGgOcW5zwV04UpY1LZ6oIw_6If-G-AulBr25E37xTvsgS0ohdNNnRdlOfdMyibTCZ2z_SNkrhnxsJzpAy_Tu77_D7mGl15JTDFbwWsDew_vjGN5sR3p1poCGCq25u6yajzyKUusUq5zvmF8wfbXawvSynrL45k4kbq8_bH10QEfH8HM7PmWg5RLoU8cDdX_Z6L_vDpmETu2iYhZ7_vw3k6bpybcM_CV_LgZlTDBcYej-v2shBVH8wGLb4e9NxsV0OvoFNJh-ZH8FIc4AURgNlK_Ok3e4_x1mjwWQivmTqM0gFvi0NS20xAaKQg7MLV3FCFQwA-BQ8URBrZM68KfYn09wdG1t0D--miGoXEcfvg3X2gYFz4e3vf2Nl11ue2xj242x4o3wnorM4Lm1U61MFKtVYPepKnsS3D46Bqbcuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=lw2HsuyzqOKJ8LWSRy1CetGqo_7vC6GhECBvLCg5hotjzCByfkAXS-VoHvzAUyx0-fPQcQpiSV749SmlwPEdSrrkjw4pmtqagmYiTp4ZPPUO1HcNwMRAa-QLOXZUH8EBetTHJB5TVQ5MBsi1RDmAUk1CRWwGzYV-LeE0zXIBgd_zI6CKMu6HnPjbwnjwDe_qupoeNkxAaRp_jmiIukArT5fOFg3rLdFAY9-JB8WO-AZK8Vf7x__n9hiHqq6_HdKtxJGgOcW5zwV04UpY1LZ6oIw_6If-G-AulBr25E37xTvsgS0ohdNNnRdlOfdMyibTCZ2z_SNkrhnxsJzpAy_Tu77_D7mGl15JTDFbwWsDew_vjGN5sR3p1poCGCq25u6yajzyKUusUq5zvmF8wfbXawvSynrL45k4kbq8_bH10QEfH8HM7PmWg5RLoU8cDdX_Z6L_vDpmETu2iYhZ7_vw3k6bpybcM_CV_LgZlTDBcYej-v2shBVH8wGLb4e9NxsV0OvoFNJh-ZH8FIc4AURgNlK_Ok3e4_x1mjwWQivmTqM0gFvi0NS20xAaKQg7MLV3FCFQwA-BQ8URBrZM68KfYn09wdG1t0D--miGoXEcfvg3X2gYFz4e3vf2Nl11ue2xj242x4o3wnorM4Lm1U61MFKtVYPepKnsS3D46Bqbcuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E65Hiw621E1S6p-Gm6z3nFVhVDbD3_UFhxWQb0L5jP1HurCJhaPAJQ-v26eNRW-jcY_mN7IkDhQ1Gu5EQVbxx-t2-t2FOdwzzxmOmRsOCel1TGIDNNWJsRHHmzXB9tuHdstniqrLrP9xP9t5RBWl4h2U8VZWo8_QdHlDnAnoFWlx_DURZ95Ra4Grrq07RedGhk3Ube8VVrGYq6jGFccHzQjTP9AXDv0ylds3cpbHT1PtU9tf2ivn-J-ZZ2Rl--5_H6WBGWdDO86PxMM_e3Yq5UcAi-U9ND_365bvEajhuuClp0XFJ_MKApvfYEmqDUlQ9yt3zsvFvaxkMbTpR_t__Iuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E65Hiw621E1S6p-Gm6z3nFVhVDbD3_UFhxWQb0L5jP1HurCJhaPAJQ-v26eNRW-jcY_mN7IkDhQ1Gu5EQVbxx-t2-t2FOdwzzxmOmRsOCel1TGIDNNWJsRHHmzXB9tuHdstniqrLrP9xP9t5RBWl4h2U8VZWo8_QdHlDnAnoFWlx_DURZ95Ra4Grrq07RedGhk3Ube8VVrGYq6jGFccHzQjTP9AXDv0ylds3cpbHT1PtU9tf2ivn-J-ZZ2Rl--5_H6WBGWdDO86PxMM_e3Yq5UcAi-U9ND_365bvEajhuuClp0XFJ_MKApvfYEmqDUlQ9yt3zsvFvaxkMbTpR_t__Iuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=nobHQ_lqS3badr3aRNREef5Vg40F_o46wgd3U2oUs07JZCXMdeSfGYtdQdwCdSAyMYT_3HmDZuCDCFOhUZiI693B5pwGsMcfLDPT-4LDEoTCngy7rtFlVtl7j9-YeKNswbaHF5yZ5R7ZPGvHFdI5nFZMSDumlLr6d6-7yZF6LrNSAuGp7kTt1nQpSCUEmQ645Xa0xB0-IVfzfJfw6vzf2AkJ_rWak84rN33gr9nRpxuciFXTd6nSIpn7xEVrz1r8OxpR562mHJQKdG-v6-WrxmHtCyBi78OFgIcukn0ukavIZSEiO4sYXbm_MCmjP9gmnV3wK7bwoStM2Wc9IYLvwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=nobHQ_lqS3badr3aRNREef5Vg40F_o46wgd3U2oUs07JZCXMdeSfGYtdQdwCdSAyMYT_3HmDZuCDCFOhUZiI693B5pwGsMcfLDPT-4LDEoTCngy7rtFlVtl7j9-YeKNswbaHF5yZ5R7ZPGvHFdI5nFZMSDumlLr6d6-7yZF6LrNSAuGp7kTt1nQpSCUEmQ645Xa0xB0-IVfzfJfw6vzf2AkJ_rWak84rN33gr9nRpxuciFXTd6nSIpn7xEVrz1r8OxpR562mHJQKdG-v6-WrxmHtCyBi78OFgIcukn0ukavIZSEiO4sYXbm_MCmjP9gmnV3wK7bwoStM2Wc9IYLvwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=gdXXoak89V9HSTtA5KcWinp3KGArgdRobWOZZdBok1Df-8WI4ykCdb6zveCZ3AHCV2vOJ1vRbzqwFrZ3RswQX-Tc5UpTGlkg4_V760ay_NWqW1SQzzLLYNmF8UiC_0sHoD0lfa9huA-iccjSV2nQ-aAgcPdHnOm3hFrwX2EibHTdh174fFgXIpS-EsVew4ryrgBO8a6InqtY_VDcdmRMYEj8z1oDQ1eeTekK_Th8leCyblWPdQZW7gJsfYDCj0t1uYCkUI-ekfekOCXWmCoSqY2KaMKApPlxIWDZlmnDUktt4N9YZWAPyHusbkMGgMEFSZKcUHR_zb7Ho6ib4xijFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=gdXXoak89V9HSTtA5KcWinp3KGArgdRobWOZZdBok1Df-8WI4ykCdb6zveCZ3AHCV2vOJ1vRbzqwFrZ3RswQX-Tc5UpTGlkg4_V760ay_NWqW1SQzzLLYNmF8UiC_0sHoD0lfa9huA-iccjSV2nQ-aAgcPdHnOm3hFrwX2EibHTdh174fFgXIpS-EsVew4ryrgBO8a6InqtY_VDcdmRMYEj8z1oDQ1eeTekK_Th8leCyblWPdQZW7gJsfYDCj0t1uYCkUI-ekfekOCXWmCoSqY2KaMKApPlxIWDZlmnDUktt4N9YZWAPyHusbkMGgMEFSZKcUHR_zb7Ho6ib4xijFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIo5Grnj-1U7S_-_liZ3OdnCjjWes0QOL1rytSIZRUb4gFsWtwBm9VvqwsZe6Gk6Y3Wk6cZBqza5jmjI0r8qxqZkrJqnbKH9mpSFJ6wzY2xWuCFQAbUzOSQN_zJUSqfx3_v5X3kHKqPvqdr3n3xTQ0lTZp8EQapRT7KzL9X1nwTAZXKratqIG5fi1d4KVPYJ63P9ZnwIwmQfVjeavctg4brUXFFTeN1MlNJeIjBAPuR2jl2Dp313GYGyitRK6Ovefjb0Hpp5KnqMcFZIjRJ6zGHIM0rOzPbN50Khk5UObxTqLkbz9s_ETnidao5qapUSwmW5vgEgz_OXqao2Ud4yrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-F0oaSW9vqFOL0pGUJyRFaL_tkNJMTJpvONstC0nacK8i4388hGaEkQ-6pqpYKQEKR426oqkosT-fyEiYTd8HC2tOhMFBQpyY1eHcpxHjrWaPX726HsEeyNmQMNi8IxmQM_kIQQkACiPnmaW1A1c_IlB_mwW0zc75tRQwpLKvIXaURwRMSFMCffeFsr-gsLCOm4Kxg1XNYaHlPKzn8ijJxjT7Xnp5rxdHfLdkZCkhUZXH254q2sl7vcJYQzzHmIrZANGLWTKP67yIV2wgyMSukahtFVhBhLdPwbpnblUYYes6eICRzNb_HlzxO1CG-pGYaM-e-ZNlG1TjZGgU0tTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwxQLNQgnmS42AMI_1C9a5dLVrsGL6vVugBgLavEs3fl2Gu1QqnROzQKV8BummA8XfMU6DE3NNlthRf9GlY7DK9R5PMpyFC0ho1M6rlif5C4BB_IIb2-xaqPJZuDryBUzq1erUK6IF_TB1whq5LVK2mpCr9uuJw5KCFvdIW8m2eiGnaBdzlG0AQXkhQMycdEXdX7ggevJ49DRS-Soep-Mq93oe5S3p3f6bNeKgXv-ldWdWCA3Yt6k9ABpGijibIN7REJtKqZC3TUpOBiAP6Mkp6nF8smh1IDmYXeql2mY9G1Gm8akbcH7DoL3Ba9kWBmcfWGP51aHkWcDr0YdEmQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXo1vnuYzWm2IukGXYkkGT9QsuIPExW5Q2MMdrirjPOYuuJqsP8KIJ-WnIlJQustnU2zDX7tj2KBGAmWskL7sU7WO5fljuzQj_Ax2_aNCzcdUP84ZUsdQf676X21knvKFpIifwTP3-ThsE527yrdhFpkt6g0aCuHbemiPv5H-By-r_dFSycuRKWkd4r5ORIQSY7SJamaHC1pabjhtiLMq47aejjWQD2Fx-QtkDbd60n6tc2g_hnHFDsBEh9j6L9Z4EVP2A_PgTeN0PrxFoNXvE3fdfUfGaTxukyhV43VMlj_fVlVfsdQSy_vcBSy_taWUkihe7RLRMOLoN9fauNRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJwxWpd23IvoMrn19-NJlAz8WhH_KOattml_e6oSdW-GvTy0K6kw0lfdozwHQBkbcNNdJ3cLDcRA73piXtoga2dBk3dtajdrgDPCP8-4aIIA5akuYib4rT5kth2DHjLvg590itTaPbFtBxF83T39L-hB4mjQlp06Zxkmn4u2FvKIjn_MqHvMgswR4hwAZJXkIhLcykG4oJjQ0bjf7yLk1-GEq9Clu_35VehhMlflcufNPRsh5F7tDg6MQGmj46gmJ3h_LyPMP2NAvBuog1un6oV-wf74issWPoFlm3QXdaRtlt6J0ZL4JDWWa5tIBRmz99duDQVwul1gZ9nibsljpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=HD07xBFnuDCQ-ABSStsnOMaCDkZ5pwGLGmqi8Z6nXXq1JydO-QkbJEMgvadhye7Ks7Jz3hVJGT6OVMBU5n8RTRKH76G6VgZKiGVYbyOM345YKEjt8Ix87awN2iN29pTUyr6JLfr4lAkcSLdCaK3JPmrFpqMDAFHPZE3nCZn2tN3eApXz6tvuYzPCXbGvfNXURgzMKi8JaYoWGBTZ2PyRzIn2o0l3cULhimRrm4Q4uKA3yNbQdQ0j9AVz3bo-MJaAKYGfhOOYOGr72xVsWValZZOSTvMvfy7iEZMoMsrR7m3TB86f7n_A9ySNDtyw5LslFlNTGFBYXwN1QrI0idcRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=HD07xBFnuDCQ-ABSStsnOMaCDkZ5pwGLGmqi8Z6nXXq1JydO-QkbJEMgvadhye7Ks7Jz3hVJGT6OVMBU5n8RTRKH76G6VgZKiGVYbyOM345YKEjt8Ix87awN2iN29pTUyr6JLfr4lAkcSLdCaK3JPmrFpqMDAFHPZE3nCZn2tN3eApXz6tvuYzPCXbGvfNXURgzMKi8JaYoWGBTZ2PyRzIn2o0l3cULhimRrm4Q4uKA3yNbQdQ0j9AVz3bo-MJaAKYGfhOOYOGr72xVsWValZZOSTvMvfy7iEZMoMsrR7m3TB86f7n_A9ySNDtyw5LslFlNTGFBYXwN1QrI0idcRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=nVSlBTqZ5f41dvtKTUyGQgKS9x9nDtbTB9bxFzQRVycf44n0qAgJlputmXQ-VIDEawYnxny6Z3o6NubvJ0j-WJXudU63QiCcrRIKihx_0kfTbp6rodXpjJXY6avM2i7khlwumT0wcyt-Ra4DPi1Hs9jFU9lKMx4AokXEts5j4OxhA8q99UiYVNc-HnA9nlxCSvuBIGEEzmXoSPQhyXdQK8M5b99EOyoOv-udNw1upgBBqSMwHshGxI2V_yy4QJfH9jA9dzlF7J2tFU1LhHcZ0KyZPx8gT1CcYbuBzJuHEikL3g_SJtNgqRPctAolcXvuhcLfWFyQGAosh_jZQ6Z3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=nVSlBTqZ5f41dvtKTUyGQgKS9x9nDtbTB9bxFzQRVycf44n0qAgJlputmXQ-VIDEawYnxny6Z3o6NubvJ0j-WJXudU63QiCcrRIKihx_0kfTbp6rodXpjJXY6avM2i7khlwumT0wcyt-Ra4DPi1Hs9jFU9lKMx4AokXEts5j4OxhA8q99UiYVNc-HnA9nlxCSvuBIGEEzmXoSPQhyXdQK8M5b99EOyoOv-udNw1upgBBqSMwHshGxI2V_yy4QJfH9jA9dzlF7J2tFU1LhHcZ0KyZPx8gT1CcYbuBzJuHEikL3g_SJtNgqRPctAolcXvuhcLfWFyQGAosh_jZQ6Z3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSmP_IqWbaFWjrHItYtTlHduVcvn3GsV80QgM9C_YxPSI5Yd771IhCMEaJgs3TkHVA89TdlMXbf0LwrO2PmU_QcWHSATEL_ggGLzTJUQlfvh2f67c9xD6fPxFTWhzqnt4aRl0altKWWYy7cayMLFkdIp-piFhnuHm3PxJ-4sEl9DZ87JcIFLM02u_NmKPtTx-Cv5qDOh5Jzyl9g-8pDeoHrjyGOZOmT5o3rGgnDLKh_YvWh1sVVutjaajBCGHESWtbgdAS4HYsW-VbnHy0zAsQGBdE9XdoxniJ4bwgrUOKS62dMuclnl5jhHqkEHhkPMJKFDCBb7VCY9VFcBzl4MSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfK1aZP8QhYVBsDGZnwiFSdqabxOmXYH9D-SMnrEg1F1CkNMju3fOJGYSbxq3pXKDzsU1Q5aW2sxr1sdgpvh7zVG-bVFWAg3Kgc29nFmp9sGMS6LIOXosODzeZDhIblWRivE72GRJvG-v82G4Fwiugwigckl5V4EmF_kcgGtDbAlkx_0kQ6YSSfzqkwsgFsCpcn-3maNwM_wdp_uYGhD8SNbz0JIb89zvaB2B_ZBc6LhwXPLBgB-Byhkwp3PLYwLm35CB1sz7BUkG9Inf0iEY1Fn3wam1kn4N5tb9qhxel1IW_llaMkC1Z8QAtbPvlzpMN8eW7X3KFZxLOijHXmxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=nfjy8kDzbdvr8jFm2BV7IpyB7z1oVqiNGToj3OKiAuEQX3n1LAcbSFb6XqbOsPtrUTu0T1_pNKWv9Gyaed5fp9fAxOdWE4OSqf9SK0Sm0pjg_-Sxs005QC0gHySgQ3_B72Bbni8HjMv5F_dYMnEjXqDSU7GPPS2n4b5w0aosfF-RuAao_I1c2xPGZmmo2dZlrVf75KmJafjAYc3Fd8E1a-8O1rClCdJrXidihdt2TjO61dPu9c0TyozSaBP0-mIfkc2sIcqgIfYX8PWW4COrhnWYBafmu5t3B5ImkLumyJbK5MkXv7UyJpRBMmBroH5FxIQV0LfQs_jvQ56267KP-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=nfjy8kDzbdvr8jFm2BV7IpyB7z1oVqiNGToj3OKiAuEQX3n1LAcbSFb6XqbOsPtrUTu0T1_pNKWv9Gyaed5fp9fAxOdWE4OSqf9SK0Sm0pjg_-Sxs005QC0gHySgQ3_B72Bbni8HjMv5F_dYMnEjXqDSU7GPPS2n4b5w0aosfF-RuAao_I1c2xPGZmmo2dZlrVf75KmJafjAYc3Fd8E1a-8O1rClCdJrXidihdt2TjO61dPu9c0TyozSaBP0-mIfkc2sIcqgIfYX8PWW4COrhnWYBafmu5t3B5ImkLumyJbK5MkXv7UyJpRBMmBroH5FxIQV0LfQs_jvQ56267KP-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=tKFo0W8C7p7GbkuFTIi_6x7uFBzd2Cb3AHDy9oB20QlhuXS9TizWl_YlNmphqZ_YaPhy4Gw89YbKdt8XOZ3wuszJLhps56WipScRcYi-TX_gX3O9nLMng4VcvFXg9NOGyfjYPwlhmBWa10XFQlZ0TNxUynszmmwBJBdTN0Y_PldUsRfS8VRhXBJ1fJ9LV7e7DcolhBu1GOu1o1xz71rq8mJ50fr4i4Mfc0WiFOjW8pyF9R5laNrmqE7rCabK83xAmAbh33EXjEpX8AXowcxbXzBwlyL-zEO6eNlq9mlCyMFnkwE-PY4clXb0KN7TfmFru9e5wW-VIf_HQnblW1eb3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=tKFo0W8C7p7GbkuFTIi_6x7uFBzd2Cb3AHDy9oB20QlhuXS9TizWl_YlNmphqZ_YaPhy4Gw89YbKdt8XOZ3wuszJLhps56WipScRcYi-TX_gX3O9nLMng4VcvFXg9NOGyfjYPwlhmBWa10XFQlZ0TNxUynszmmwBJBdTN0Y_PldUsRfS8VRhXBJ1fJ9LV7e7DcolhBu1GOu1o1xz71rq8mJ50fr4i4Mfc0WiFOjW8pyF9R5laNrmqE7rCabK83xAmAbh33EXjEpX8AXowcxbXzBwlyL-zEO6eNlq9mlCyMFnkwE-PY4clXb0KN7TfmFru9e5wW-VIf_HQnblW1eb3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKbXpY3aD5vVicPLYumBU9NVT41649d5_xM5Ns0t1oSjFpR7WQnVqPpMrOW2ih4WT2ZroE3iyfK_DkRkIHrVA-odGKMwUcotw-aD0hqKq4w-aOypWrIG0GuAZQqu1jLACvhZOwQt-VSLb7-uun4R8mhU_Z4CsyYMJ-PHc3PG3_oY-ArzGsOn4VVgTwrrbfZhjqy6z3En7l9rBrm5xsPIs_44xlD2uONi8qUkeW8cQV8qUrSF1uo2HwugUQHWoOh1L3YPGZe422kEBIHfx8WtydED5cHTYY9i0SgDq3AbbS9sGs6-B73lKLqaZAmkh9iuD222Ze-Z8sSnkleCMeO1pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDkB1bZJB5_8IyDzBNb69u0GpfAc9vHbk7le4Umh-kW9vc8bMwFjBIZa8nx8BPbmfbkdSjtwIzo2iyNJOSUGzn6OiFHMWzMSg9PA6qcP2w_T5pM2JstPb-tARHzAi2--ZtPYre_K6-UVRxuouknIEcM1qx2eH2EcAkASc2ogfEZ72GxCTZmOgGA24xF3oIDaYjFpeVfLJAfxaRNv0oo096js0jW1PSGabwXqLm0Ix2pxI2AznaM7hBvFx1pPhR6gznyeWN6NhwfO4HcTF4nTt4GzV4OZHNAMXAknlcKJMS76fd_MOnq4nF3w53mQasWnItzYrDePujYdv3GS43MXZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCoaa55UyvInATB6lnXO5YZ4zm87NQLwthOQ31avpl6O2uxg6qquF7pKQAuQ1AY1aRzB9WTMrSkP0qA4dcPP65iYjmoZaMO9ggwthUkNkmYRNUcWMiKFRqd4kWuutViqDsLriIZOQHhV6vcjkev62y6zfXBTC7qqy5k4f0GRpCjzVuUbmZ8LeC7hHbhYmOrFLA68QwxK3Dlz_Hu5tScDpKuUZIkNlyORT_jlbZFD4xsamvax6vOZuE8hWDgzuRH3xUVFqIujBJvWuuu0AjFcZ10UNl0UbtL0tPJGdd0NB0U1g4TbioIQUH7Owyn2KKI5rNZmf0cDbyuQRzFPCqB55g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=dW0pbMHZkaiIgCn0frJGCG2epdS6fqxFOYx2p1KQ40Ten-Wdli_UGFoaUoF9NDLE9-7OjXJcOqOlffDRwqYtg_VRkNSNGenHrntygTvcoumAEGd3DkkmjclZebCJYYCCf3lXZKMjwQBJHlJZaDaIkNn72dFulB7VeaX4ZcOmrsfMwryrwu05OYuOz673LeTb_ha0lEpDQPL2-_jVCa2WEyn8Ze6ArqC5MtIxNvu7TCLRLkQVlGy7NObIvOZ7aXE7Tde8flQmIASyarbSb5rsMW4XfpQzK-obspySPtmLKDSWZzCNYmLGqKfaASDWq3zChyWAsloqrTIbstRsgpmBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=dW0pbMHZkaiIgCn0frJGCG2epdS6fqxFOYx2p1KQ40Ten-Wdli_UGFoaUoF9NDLE9-7OjXJcOqOlffDRwqYtg_VRkNSNGenHrntygTvcoumAEGd3DkkmjclZebCJYYCCf3lXZKMjwQBJHlJZaDaIkNn72dFulB7VeaX4ZcOmrsfMwryrwu05OYuOz673LeTb_ha0lEpDQPL2-_jVCa2WEyn8Ze6ArqC5MtIxNvu7TCLRLkQVlGy7NObIvOZ7aXE7Tde8flQmIASyarbSb5rsMW4XfpQzK-obspySPtmLKDSWZzCNYmLGqKfaASDWq3zChyWAsloqrTIbstRsgpmBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcfmCzdkY6CX1Uq2Qrr091zcBBGgzvwDw7u7DVC20ONxmuyJefiDcUhjTEXRY47HZb80kAVBaO2QKjWqqcO8vvvOZsaWfNSlgNaBXLFb6vpX5NWCqpcdFn5Itjq6FD7xevCdWPrZ19LWTdfp2ZAsomZNGHrU0mCFCfcQFM7ToJ6divMTh20erYSqMPeSdsRYc7-C0i3UNjluJdA8jM8X0K6UiLe5EwdIGgmQxxVUNWdKM9LUZTsz8hT7S5D1cWygtDbHosHfI_fzBWAFBq7NG-OPOs67irWuyXreLdZUtsrqRQBo32igfmHZ5oZFS1W49r_zwsIK8NzrFVEPNMh62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnP8Ym0q_Br6HoU9FmjwZSS_hn2dhCXvSGIm89gjUtjnROy77fhyXUbPH4L44mPB5wQ-eNNGzU21885rHvw0vDRKiJAjqR8Y2WFYQNMSNBBMo5Lp1KN3LXUAAUij80_zSjvT6h1PNg2L2zQT2-4E42hl1tzquog8LbEa0wwAPnhv4Wa7fqujkcqlv2LvixBRk60BvOkXJ-M6ZdMKbpMVrlXoTu358aMcr6wqd1-J4LgIDdHEQIUVJo90nuc6rgH7mfAh7ZjjTLHllnhNVHyFEvkzx_3nP0ahlZpsSaM_oXRE_sbFf8okctu87_oI4vDlj4rh4X-TfGLt8eHssAEWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiF658R-Db_50F4MsaDup6163qzpkyJ4iYhALCmoJO1AHi-y6QQs24HK7_ubQ53C5na6kwEjrrW3-tZO21NgjAkVTxpIdHuBpFTGD0HnbdBPjwjjGKglWuVd2PjKcXFrKsQ2xQJSlJrVFfJJod2rkovhDsn49GbTUpFYprjitDnI3INvubEpONwKJw7VWVW0xBe84njhxgVOVTodO3z8kFMI0t8B1rWZXZyv_wcWpyStYcTbURyESzgse-jtRDgNErscT08ZlT-i0BZVXpepnzGWxYbMbHJB-CjGwmr_GbeP0MDIk-j_8SAjYftiB16Ys1NzfX06uX1angQFKacrew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYp8yIHfLTH48SYN660TduMDZCwc9WBDRzPMY5UUEDLkWV3XS014cxYn1MCcUwsuyDbVcqwCCJ3kZR8_tpInDeVBlMJYMysPcnoSsUCVI2IhZJFvZ7YCS_eunieBObmPHnafbpXowmwdEKyBPflg-1NirmwiErkl9g1NggviAUjZYNB-lg-OJLtJWK3ZhuLLgiQOeyOcmiRphZQUmkmwHRa9vBHclhhGGTg7lZYBj-3RM76FxAMiheG86pYM5LunRLqfM_HcfSSxocqWdFilQRJXPX5NiQWaoE_5YpJcoOSQASxMV76DUHUxEqyvRFKPCkO13nQvQZVrydP0rWaRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=khk5ZV4vCVzDK5H6c3stpXPDH_aA26xUHsNo9aIiTELGsPyvRD1ytZ9FV36Ymw7kuCtopP4cxaJSe9TAUccxY7CI3kQEDHEqcirZ5Cdg5wKf7PCV_nPWCF9Ty54FZGOlTILsF8gy0Tz8KyyAV33sH_Y7K7CFG4LrRH_0wkSR7fpMhgpSr-yZ7QmRqOyeG8lL4_ksHohdK-u2MPPwq0msR5hkJLgI1bYc2W6sdO9LZS88w7Ejt21_B_zFujiI6uEAcfd_bsn1xdGNoRPLue15wZXE5qmgb75QSPNbILxFr0u_9AsBSr9C0kdq3Nfvi1Pf1NehbdVVGVZa69dPWhl6WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=khk5ZV4vCVzDK5H6c3stpXPDH_aA26xUHsNo9aIiTELGsPyvRD1ytZ9FV36Ymw7kuCtopP4cxaJSe9TAUccxY7CI3kQEDHEqcirZ5Cdg5wKf7PCV_nPWCF9Ty54FZGOlTILsF8gy0Tz8KyyAV33sH_Y7K7CFG4LrRH_0wkSR7fpMhgpSr-yZ7QmRqOyeG8lL4_ksHohdK-u2MPPwq0msR5hkJLgI1bYc2W6sdO9LZS88w7Ejt21_B_zFujiI6uEAcfd_bsn1xdGNoRPLue15wZXE5qmgb75QSPNbILxFr0u_9AsBSr9C0kdq3Nfvi1Pf1NehbdVVGVZa69dPWhl6WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr3qYRXG_tCBO4R8zgaiU3XNGkJ8Pja4bbrFpbW7svgv1kynFA1Lx6y6xXCLD67JlZYTO5BFys3saXXQG844GWqBnL2Gmp-yjQIQRTM06Eq6HMt-zOtoQDyK8TO-Cq7VFdqvihtYVHg5ZzxHk9iArkQ6WZ40fmDeA0YjUw8uFIin1CJbqsaagG0E8Dt5ShvPCyZVZjPjoqndgbXS8QDMVnEs_67mrdCHOtLRHaA5C13J4M_7ZyZ91xPrSzqaK_NjCqRPMAxKM8F80nlJCRhIiLBPue_ig3t5idtVhOhqr0ru9YilzZ8QCRhNb7r6rHFYebjZANc4iDZRIK1W6Wj97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBUKDJilC2YFuPH3ha10bV7TisYtPMe1Uo_TI-_uDKjICv1b4c84onoDhZZlFQkdjpwFOI0SeTLPi_95SURRqS53Kq1aUEIPXnDoaUAwweLwnnUxFupSLXscTcY5LqZyN4YNsM4RbN6j0lpSPWQjkn95VHYKTwwg0NVwru2EXaovOqa4RD0MOWwKdkv69FEwMa2qlG_JXimEgDFNdLhh4vjlXdQ1D71OutWY4_hL_GP-XaLk2Rlm5AXAsY3DWA3YXYKbIOMFB1R-bwSx-EMNmUlvjP3Qm0h4Hry0nEuVC2-y_TEGzy49FfH6J6bq7zugUWTjfkY_oKaXrMho0WQ_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJutEJrPBXPqmcnRYbS-PeAMbM9o3vFibpfai9PAmXxzAql6rfIL3DkcGT1UipRcfim7PlOtA4SWRIocgW8lHv1MBK-NIc3NzeDoyvQAlDtZXfKjxDbG1_Lp-UxOtMFTBeSGJPB2sZiwIje_lehusyhV5b1RFtboaqQWz4-10UsauxgDsZHIiWm-3mP3vYxz5XrlOsfw5fnYJ1JXoyjXfzVsJvFuYxeUy7w9-nYjOVkAyaLrcw9Dg8PXhbypaxXW09Hfp4Cz2RfZPZupk-Meh1MHSVDEuMnHdlL1-huzgaxGkxyRWt7fzWZOwRQPw16LzDG33x8WwR40FCc4WcMSYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=WsfXjoLHaiv4ymBUGkaugELqwrffA-yeDu27HB1NXvci_RR57kv6EO1Ah7hQya2DL03npHHxSOHoLAnhC5sM2a3NFwaIWGweKp2QBtMkcleDT7fqnO8V58tX4miLjr_4yEAEtdiXG5awQDwvAHzuyiM518GYdZAbrXwIMZVEiM6l3hSC2tzxaMzSgS1Xko2aLPbKkv3H0AvJIiSCpmOw6wAWdQA4-MCErYLq0CLxnqTb5UvMzNzwH67G4auv4xBZY50urwQN1oGSB3JP1kYpM2UxhUQ6YsnEPqcqmDj_wpdTW8X2LMfN_GE9nNpHVR4CdOGwmom5JhfNtnxmnvU3-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=WsfXjoLHaiv4ymBUGkaugELqwrffA-yeDu27HB1NXvci_RR57kv6EO1Ah7hQya2DL03npHHxSOHoLAnhC5sM2a3NFwaIWGweKp2QBtMkcleDT7fqnO8V58tX4miLjr_4yEAEtdiXG5awQDwvAHzuyiM518GYdZAbrXwIMZVEiM6l3hSC2tzxaMzSgS1Xko2aLPbKkv3H0AvJIiSCpmOw6wAWdQA4-MCErYLq0CLxnqTb5UvMzNzwH67G4auv4xBZY50urwQN1oGSB3JP1kYpM2UxhUQ6YsnEPqcqmDj_wpdTW8X2LMfN_GE9nNpHVR4CdOGwmom5JhfNtnxmnvU3-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=eo3lvoTQMp72wj6BFViwufT5AQTVwVyxYc2jACu5KiuigaC4z_iLtAOL0aRW1Iwl2jOsSN_j9237U0u88sNaLpoRh52y_rU-yOKZdrqOx--jbP6sqaoy1Ym1DkV-665DRqMNvZwzHnzmnmvCuS3NZh4mxZvHks-GXuk9EepvatY9FjAx6U2Qzc6H6UOU1y2pR0--2cPSxwVFfRc2RenkxB54vutOo82iwscC_561RxNsHo-J6X1jaknhrXB2tjhAKNbGnpZ_vAstl7Cu1eUKZQfG5_BQPUxgQikCRQpYUpV-3iANC9uhckwjtQkGLtlIXSUigvNpG1iFLhAznMHvQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=eo3lvoTQMp72wj6BFViwufT5AQTVwVyxYc2jACu5KiuigaC4z_iLtAOL0aRW1Iwl2jOsSN_j9237U0u88sNaLpoRh52y_rU-yOKZdrqOx--jbP6sqaoy1Ym1DkV-665DRqMNvZwzHnzmnmvCuS3NZh4mxZvHks-GXuk9EepvatY9FjAx6U2Qzc6H6UOU1y2pR0--2cPSxwVFfRc2RenkxB54vutOo82iwscC_561RxNsHo-J6X1jaknhrXB2tjhAKNbGnpZ_vAstl7Cu1eUKZQfG5_BQPUxgQikCRQpYUpV-3iANC9uhckwjtQkGLtlIXSUigvNpG1iFLhAznMHvQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=dBkAL6fdhFebjnhMuDnwX-5bUd9jNQqUkaKuWvPjKop2OKKJcVgRrucVbhP_bygs77_UQuyXfaG5wvzf4aBcNot8qTZJPowG8zUwciNYet6VPicBl631PYGdUVifQNzuac0mnnYUf9G9TWHlp6Sla-IKhJLLYwHFRaEm4SoHFAED5ta9cVQBU6FUjB9k3LcHu6tJNas-MjPb-FIg_VLEbhE1f-Y3QYjHJGLIYjT2c97zSqTSC7iQsOOJ4TkiVH-fu67E2CwU4YGU_Cvi05j2ssS-FP2fmW0SMppapl6Z2RVaXkPTPHK23MkiSm2ZIx6iKdgOObXkYZEwkUER3lZ_Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=dBkAL6fdhFebjnhMuDnwX-5bUd9jNQqUkaKuWvPjKop2OKKJcVgRrucVbhP_bygs77_UQuyXfaG5wvzf4aBcNot8qTZJPowG8zUwciNYet6VPicBl631PYGdUVifQNzuac0mnnYUf9G9TWHlp6Sla-IKhJLLYwHFRaEm4SoHFAED5ta9cVQBU6FUjB9k3LcHu6tJNas-MjPb-FIg_VLEbhE1f-Y3QYjHJGLIYjT2c97zSqTSC7iQsOOJ4TkiVH-fu67E2CwU4YGU_Cvi05j2ssS-FP2fmW0SMppapl6Z2RVaXkPTPHK23MkiSm2ZIx6iKdgOObXkYZEwkUER3lZ_Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v51qiyIMLHA9VhDUpAHjxAsL6FIU8Gbfnhujs0QxAJmeVUZ3e48BjGzsQKlo3biEAYGsfRlrzXdU6vlRnO6dUHjDkH4cPOzfUbh9YzfnMWnBDScTqjN_eQyH6Co7hG3wFv_CyOejv8uiI82ELT-rl1JwjZJU7GubkPp5bAKSJ_Y-FIsfqzWBIMoe6KWHUhIlwo_LlDkw8wLPo7FY8I74Rd-uYGK9kRXD42z8pZlwJx-cEgkTvta0ocIclvE2k_vljJaAVSCv_bYsBgPUMvqYWxSwLf9GO4ownD4LhRLM_WFhlzzT-lKnYyV2WyCI3ZGt5rVEsWUVR9-huQsM4GqsJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gj-eWKI6Aj-liNuC3KtuIAJc6Gmh0Nmfgxe4c8mo8N8LAy3YpmZ-8s2t2vqOh6-1KZcJrVez9Vq-ZabELoq-PIABLE3MpIfFu7Ai943EAoZ3gEUhVvXpr11SNqzl31yWP0cP7DFwBLX_Ba1AcatknRu0H8oUyM3rwuBbtfmUT6a5uy-U-GWk44_og3WJq0Kc_qvx2qPlVjoNws6QrUpSJeXF6vD8CqlE8C-113dfrrt8BllCdb1s6oFk30pQxNUKD4m6rTTv7BO9FvYkReshrxiqPawyrqp8PROoj7pia2XSCS0fL_a_n2AJoS-_Wnbv8TdUKSYxYc7dBqze96Dt3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwJOL6zq4KFaq9kXk6DX7pedz5_CeFzI65GSnreLgyeezvoyCcvUse8X90zMK6mtHHuOf-Y9Z3nXrSa8n7PUd7v_dydhySw78IP_XOgjqbeKHUBL1TlylMWD_cqcKZZwEzR7SYTcsux7yBRsc-ReFiPX42u_1v-khcn3yIxVVLh3KBjV9FtwFIB2PsbKdkA4UDsfNe9wHc09AnSEJykE3al2lOFB-yDJvABTnjqHZ9QkTaXgbIX1iJtiH19jFEyWpw8h0ELAXzRwKnD3jDN7lMvItjFPZZp_R8r8VNRnwd85Fn6ZhBrKxnEpOROu3YX86BDOYakBjHTL0cBwpcycew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGtXMbEd6RMPMV7df9BKyVRZmIylGQrzo-P0B9v4IYkujPVNH0XfVdqlgPEpS_RO4laSMx6d212N6kWukPaD4mXmOpTRWTB02TtjbX6_r9FpIld2xZ2bX4f5jY1z9RWLgr2YAtGwhjgGv62CNuA3EkXm7yRqdVPO8mVOB0k7zcW2KgTY8iKk2BoKmCVtbpurEtJAEvWtAaERQt6200l-kfRx3rNKb0bEMmTuwj_3njuaoY0kHLOMpCDyo54Ab9DGV0m2th__xcgML0olMc5z4yo2n6O--m04-5ziMXWvB5lQ4so9Xv_0zqhs_1L-w9AqW48fBvege73OsSkqnC7q7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vR29cdJtoUa3zYR7vyEzv8W-mFVrn-ZZzdZ9ZP_siqKiSmLetKtEeZ_mIfQ_lJi98Ji-nGoshg8blDJGVBlSyLY5SwnnNMscBksUMCpmj8F9PVu2k9QYBhDOmAJqcXsJd1KQIfBSZX3-luK1fj67lBKgSenw1d_ko1pHkXs9MEmOyf2VusOgePFmSNBOJYxC51VCJY_1tI_xCGlMBkF56ldECh5e1MqnCE52XMkAMi9g7v4szvlq4u1W6kr0wEfPEktwAJCUbaEPlVfSXmNtu3Hrx3-TRR1oBmfloj691Wa-B1sf9TxuFTHyGY6UCFat1N-ZZyU82m7Ozg-gq9-1tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TevlDSDSB0ScWHVLF_2IEuOeOfSpdB7yAiTRCEpRVwHPxSC6SgS-cT2ri1JYMUhGmVY-lf7slx9NWGyZuhddTfDFSjLL1e9bs8IwLE-eHhYBVp-VNVdb37iDn3fmlhZluErwZw7BrfTynjPnoX1W-6OZNRBeQxqPtZHijV07l8m9e9V4ujJHbJ6C5H7-44lbryJoNsMXoTRtaG8pGY25jPOOBEuiZXaQAysWIJ6DajaxJmfZPOcw1cp_SWYUOM5pIRYHNDFSzI1D-OP4USzZl5HwhBXKpfxCV8jzaW3aahL7aSAhGWv85aEkIYoHxWkLqO8a13TtJaEytPdhBg_xHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ToHZgHFxpObLxPiGwsLKzxZZxkSD4vt_XNOM9dDWLfM-jtzPmG-QzbzW6gSTt6OEKDP3zb1dCPJaDoRk5_6nJh13eJwaM4harvSKKCTcTvVbeGMBQlvDx-cSB35u5TxOxXymB1wTNov1l18v2GZmPS7h_wxoubQpewRvm6FNha1XISYpRvD82IKb-gSyWuM-N56kb-36GtSWwbkRMyZngM49Tr8BUPzcjJ9VO8lLMRPN-DJgo50GhNfQtkb1BJ4fkq6Olar3p2vl76gozkokknO8Cgb6826LFt6IrYCGkWKoT1gsmu6ruffozvaULunyUZJjUfzdvWPDezc8azodLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGVJq0IoBvu-pUiPqTuo6_LS9QvXvuFiizsQ-E6BvICsxSPIdBMeJ4wqUKbcJtevBVAJ_4l25sYf6eTy0nVYnnwvffKYZHzYleC0Ei8oYygC5xK-G2aT85KH_0XQE24L297iQdrCy-_-SSYDKjq-jFdmWwSIOXR3u1RpPFV2ZWGlJ98m1KU8bmKiB-aYRvJmWz-jephun8MO7NdAHyc-glKVXRL9bNmj3V_2y22R5Za0uT2I5_Ppa3YJx1Uu1oBEN64ebX3fWkY-Idjx7kLYZUYLKW6si2yEeT77Q_87UnqaXw8gvgz2QbLNzNrM2yYqeF9x-u71Mi-xHLPaF_8JLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_iB-HWE-P8q0vCbXQO2U03wMEb0IWkDlFg5OLf7UhyFxuaaFzPYUyKqIQkqlDw3Ro4OIFfnyspPx3MphYYP71kyVg02rPTgvhlNe_zYnagjS3cj41Fd3yjtkKMIZpNYS6_ZZIuAtDJfj4q7vRhiysnRFv3pY5JRB_7fYteIFGjihEI0l7zlRZ4kqvONe7QFVa63xWFq1wdrrtMe8F3zHWPel_zimnU6ZmUGSdX_ST2XeN_sa71MyFsHKtuHYPlem1SIUGKAYviByCVFYtpQp-RjlQx_RKTqMCCjvd27_Qtv_nZZHxuE9HESouEct_X4Q_ZKUl98VDUKe783nPBulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZUEORV1ndEq5mBjrw8jr6NMYt6v-lWK0guhQCFOTmU5PaNtkzx0rFlGZWCZUrFJiJgiI1fVPz2eS4HoP87vIRFQNVgadD9fLl7r82jXtleqIcpjlrtX4tY9w9yby3t6h8xNAXSjzV4wrk3YXe2tp-x-iLsomWFeTQQ9UHZqPdlhzVmyrnTVtb5tzIaIyOelShBfd73vTfcLTI0nic5Kb-mtuWx8Z9qW_eQXVUOw7iSjBcHzrj1WXdfJU5ZNtqeDRe6xk9hLH2UgE_fJcEq1vV6yogtBcsepAVy696BQoNxpvzAAAZShhenJMOqGb-XZF0u067fobCS8Bz3vBHJ3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqDvy2Jb65_59wyD71LNQbglDA89HeTorufz8qeIH4qKCHRa9RTy1mhs2I0Z_Ps_JKR0a2q6tgcXr_SyXiF90shgwuzy01ktj2hnNw1Km_o03QaUocqIAbT9fBQ9nywtklKPJXV3HTnUEu0YiIHzry2zzHXHuJ146z5yIyCbSCpw92eKMb9qqdJBBNJi_W59Zrqro91vyBRvE4ANcvmun5MEyQRpr8DfnFPZrcOQ_PFixDXwUz9epV6yUfFrJrFAq4FuohmUnb5NIO0Dh-Syhtm_HQz3cidlExeLPRtrbFA01bAH7tqpTvpVJshLPpNwkOdX3WjUrXNFepSeZjXMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcxMdXfsWMIvYSegEauW-rLlSveYj0aS1TclDLoGHq_6Qn6M6hD9BWwh750HrYBlfUM2-6lnjIGBCt66CzC7RCqOKWGFcH8TRZmUmoPXdDZZufKalt-baLVC3_L4IaGdfUkDMGvjKgSxaNXOu_M-YvAgSokarPPUYknsfUzfNqq9tdtTYphI9f_8QEW5bhxxDNhML9fVQM0KWHH_2ft02S3lRJEZ_KydJdjSbw0HEHByOQUkef8ZT_LjORCYKmjoslz2M1KkR-f75F687QIT1So0q8AZwgKuWFK1iobvWjvBLQ_FWItkjTO02pyj-vP7fkka0MDhjKejg_MgF27M2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ7vTdIyHaijnhOwrwYlnCptkOA2btvLpkmms2rh9QzQTiMoiwfWxosifXel8rwHfvPPpkkUFYG7QiJ6MqUADa0jPeZlVW3wQDRyFEMpFzu1bnsuyaDPEZYUPbvlvITlsf8nwlWR-XTYWBFOdgGs-otS_C8rm4_8tmdEPxUxjPkOH1XasUR2VxeexlR3hbU9vR_xODhYlPEWhx13xhrrQHsXeqES1qUpLUnkPaJBsev3zH3MGp35ucJY3Uu0PU-3TbGhu2jpH4tj3h9vaB0AkjkxaxVQgtyujlM_8oZpYop4Fp9_ycK5IOCw0dDyP-T5madUzU2e6_zkyGLlBYcXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIfpgW4WsbVGutDh0cpJM7oVthzhmK-wqYuZ6WarpLMe0NqdB6IQfpn30_aW67m2jiqU9LCLvkbONcFNEbE32gY4t2qvX_PMR9PdvXKDiV93XKBQu58vrbRmtI8s07xA0h3fjR33P51ECFmHAPPBnlZhqky9sKQol8TlhffcWIgcQVtB06EM0TSHyER-_BFlwfe2EOFv0EQ-7dsK6r_xGG200pIqwt547ip-IrrFRZpHZb4mmg1IMSCTiKoQIdBNUep6-Zk3flUUR22fD3QMjT0r8g2NnsVRJFinYeqkFyOnGm1sHZXLqn0M-1o0_Omw4en2hbTLKH7Gh8j8PRB38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6KVjhUsW254r3CyowBBmV7pVsP9Pdl8Q9s3Dj-RSrfrx39PQ31cGhWfZxppinn8IEd7sAw0VBOww_rzquRxFIJKUmVvhYIOxnpRvlWfWfPqMQ9c4sGmGi-VTiVEWYXlbsKAbDqTSL2gFLkR8WNeMX7_ZlafNLlkNeNF7LuLh3R1Ln9h3u7x7nP6F_ihUyqiEldNhRDX-UykD0R8p1UMTz8uODH-yh2G5zTNWTPm3_dsdbKJNVklT9hOBo1RKRzSpA8aAlVfaXkAqJ3fuObjurrvRU_Vb4tcAXe585q14APlGL-JZB_5_5voJb3lCJsWxQLqwPm08pXc37b675HOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=wCNNrp0BlAEiWTujoziE8O_klBAZ_6PFEeyif6dxV-TRzXNEsgh2QOGX2DR3CiuB6YGoum6a0Zq2nAoRTERUvjtuty5TpGf7mMS39HiZfG2hosz4gJ6FhkviFzsi6QHZS6zyPoHL9n-3vCVnP8XpjuI3Zi9Ony_U3vR4ArbgZ9F3wUxQLFfpdfPDHTG6BdKkLClV7xd6C3LUejgxWEA6-6_83sjsrXZESKnynWUc3W1W4g1y-x8vcrqE1IMA7u8wTs_EwXnwJHa6ZIzuZWqrJCdMVEF-CeWLOBABHecw3HgPgnEI6MwgQbouTaLSDhDTPYjyiUoL6LJhd4Ob76qvUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=wCNNrp0BlAEiWTujoziE8O_klBAZ_6PFEeyif6dxV-TRzXNEsgh2QOGX2DR3CiuB6YGoum6a0Zq2nAoRTERUvjtuty5TpGf7mMS39HiZfG2hosz4gJ6FhkviFzsi6QHZS6zyPoHL9n-3vCVnP8XpjuI3Zi9Ony_U3vR4ArbgZ9F3wUxQLFfpdfPDHTG6BdKkLClV7xd6C3LUejgxWEA6-6_83sjsrXZESKnynWUc3W1W4g1y-x8vcrqE1IMA7u8wTs_EwXnwJHa6ZIzuZWqrJCdMVEF-CeWLOBABHecw3HgPgnEI6MwgQbouTaLSDhDTPYjyiUoL6LJhd4Ob76qvUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUhK8hi57_3AVLAMJ1Z-ieemv91uQeqy22Oj6kh9cZwa_OaEv_E8-p4wyIQKHymvqARF0duecd7NK8Ek4U9Ej3wrO-cP79fTf_Vp_OVYHnbgo2DK7x7rCtpehvvWAFl5iGLYJEf9MHRIwmlnFCUYKnZmX1U2kCLF2kgnUjoxpwNSdq6ddcB4ptSh--hk7t8zXWolRI4bJvW8GV481a_qyUr3ATNd7PPDie_JunpCprpDe5TkKPI-E6rGzXJa2HTqmVP7H5tm1fPImxsZYiTWFKtoCf4oJp6bzhWdy8e0kK-kjLW6y8KDVN_n3kQU9I9EMy9QiyD3dHHY3tB_DWXHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=sG4tToBRVlzYw86EmaleUftgYX23bcwRx9VLfHwuS5qP2ywVqPci8uDwf5dftqflKrUUN-FJuTXg33gof3eOeMsyX5VzeWeQocXMY9HaSc2HceYB2wd3LiorlTMMoDZpBEAmo7d3fbDTb2IdZLbVDbY1k4WPZRq2hWOeV3_FTIL84WtUSlOAtKJVcPRbmVm6QjzAO7PoPNzEfp0dYxJR8BCtATZe03SkqTr5R3xbca0nVFOy9-R5WvB6LBW8pnKCRW_SRRj52m12AeMDi2J57BYoekIgPWpgV2A_cJOGt3SwLhuC6wf2vf4tIbppx8HZhqpz3fHY3773moG1qLEUWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=sG4tToBRVlzYw86EmaleUftgYX23bcwRx9VLfHwuS5qP2ywVqPci8uDwf5dftqflKrUUN-FJuTXg33gof3eOeMsyX5VzeWeQocXMY9HaSc2HceYB2wd3LiorlTMMoDZpBEAmo7d3fbDTb2IdZLbVDbY1k4WPZRq2hWOeV3_FTIL84WtUSlOAtKJVcPRbmVm6QjzAO7PoPNzEfp0dYxJR8BCtATZe03SkqTr5R3xbca0nVFOy9-R5WvB6LBW8pnKCRW_SRRj52m12AeMDi2J57BYoekIgPWpgV2A_cJOGt3SwLhuC6wf2vf4tIbppx8HZhqpz3fHY3773moG1qLEUWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=ARO9xRJAo9Z86k7QmtEUstPDkVPBAsrNeHO9IguftBg3Mo7jlth2izN9gJNGTqpsPMk8jNKZ3SSiDWDREKAtRYiZp5NhVH8J8V2XE03ahRElIyipzulqKzYeOzzxBVr12xJKTkkr1Y-ZdFUfja5_Uo7rGlqRLdhjCrdnmfk7H_aXrraQV4bHpgqDYJZHIhkBC9h2GFThE0sEdiaimHD96jojWkGJRQBmQRA5B9KsGd-JJGjjkNsM-bm6_-CHvptwqbxOodWvrj9slbE5_ReRPBU-wu-qitLbiYo3j_9IWZBKdyCbK7wC6puqT9kJJUymyMFoiZTK77yE-hnC9c4A7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=ARO9xRJAo9Z86k7QmtEUstPDkVPBAsrNeHO9IguftBg3Mo7jlth2izN9gJNGTqpsPMk8jNKZ3SSiDWDREKAtRYiZp5NhVH8J8V2XE03ahRElIyipzulqKzYeOzzxBVr12xJKTkkr1Y-ZdFUfja5_Uo7rGlqRLdhjCrdnmfk7H_aXrraQV4bHpgqDYJZHIhkBC9h2GFThE0sEdiaimHD96jojWkGJRQBmQRA5B9KsGd-JJGjjkNsM-bm6_-CHvptwqbxOodWvrj9slbE5_ReRPBU-wu-qitLbiYo3j_9IWZBKdyCbK7wC6puqT9kJJUymyMFoiZTK77yE-hnC9c4A7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
