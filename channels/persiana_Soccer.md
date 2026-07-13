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
<img src="https://cdn4.telesco.pe/file/BeLSskF5GDFEfoeftmQ0aCWSxrsQ31UgjHXCXaY0nEdiz6N_AHst36mPCFvflWGfT_sKxfd0M1SdUXMTwMOYxOG32_sCyBDEyM0DsnZe3ejmQaXDJ-XitrhcNCma3EddPN5CbKH3Xg4hM54nRn-bIw4wj6dHgAw32DZRNkeMgsIxJFDPWDzrIOCxINE7dVQkVWIi0oOo_2Ef2-CGobgzd8Pc3MfNDoBw7YHiu301sczTvW_fzSvilswaJ5WBKE4Tc0fYW8glcBG2s_-1h00Srg4Z4ULxm3VKKtdrJrJ_axQxZ5bgH_FzVdUnyu46SfELSRPyKGvDfE673w2k0-IJhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 450K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-25595">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh5H3yez0WNGrgpbCRpFPKYBtkbC_sPHiGjf9gdFZz5xJnj9PpaqY7sz608H3aS7ldxqLPLKMeO0ttnKzQ23Hu0fM7ulIgcamYIlB6gmDADHSfyqwsKepSBikG59QvgDsnJ8zy2TIaWt9xyWOFV8qGAPwOyG7pxG4FL6yBXVKWMgdzmCv2sMyhyiU8ykRCwWOu1pygqA9yDJR0Ksw2QkNU1e60DpM-RF0lKmuaoAYXZZmnIncSoTJvAP8H6IOG433izsEA4G2vkAoVLEINebxV4t6JJ5LK3CAk24kiy5peVHHGG2xxuuBuQ1VAwQ6Am5wzg6rYjtx-MLfsHgrijZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇮🇷
بااعلام باشگاه سپاهان؛ سید حسین حسینی دروازه‌بان 33 ساله این تیم قراردادش رو به مدت دو فصل دیگر با طلایی پوشان زاینده رود تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/25595" target="_blank">📅 15:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25594">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5PgRZmrATEznrWpun0FyQbGZ-iEZ3EN2dztDCNXG7FX0QGt6SXd5ySIbvf9egwfPAZ4FOMWbcqRN6FYbaTfR_sk3xbuorTbiHRwxiWqr0uD_YHgONIKJdLsSPEey-RXaC6E-1pShOzlLeVKxUVPewmKuHT3X7CaXZnsj7h2v1hXtn8kn1_mqFLFLXfuQU9vrYQAhieln-CHgat5SaQMyvsK2SK4A2InDUTBNpAXNzJydmipnjcxvjklw-g2Aci_UTO57hFUsmzP0CdKjQGqUWVxwSm6qrFiJcwc_SuutTxOwI61e8dyJe0nLsrFuNL5Ucml06gY-nj4T2uZarO3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/25594" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25593">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olsbtqf4QTYK4Xy2q02mbWUca8rN2F754nYHqwnR4ogB8o1Uuv6ZBOhOK3pKlK6RwQSvUFWTNXvOBV6N5KVmdoFgDXSM7D3clbVV2hTdrelarg8jXhH9xv7S_4mhZ31A6FNml06OXlHb4sBGuTbP5x_QgWK6plU028XKQg2ykEYxr-j9EGXp3MlZW5LRAw7nAXgoFSE2XuFKeu9es-IZEvUmJ1lhRTlSJ4BT-mZWiEQdwtjxQRfdgk7zrzLPRemJ--jLoilaP-fjIgkGEkpT6AytzRrYEP5KiKCEHCwHfTpxDLZupg_WkY7udMLYrErptOtytPSJu0jO5ycvCFnW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حسین حسینی با تخفیف 10 میلیاردی که‌به‌مدیریت سپاهانی‌ها داد در این تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/25593" target="_blank">📅 14:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25592">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLUwz7T5sdKaYIglJcasOA7eQxE4OWeD7POKdoLzuvG2L_eT867gLISV7ipgSXKxWjOOoKjGx1ij9nDyax2E4338r_5jWyNUbdq6TdjXJiVxgFfKUaAob3afONm9Yfyoj9h2VrRhyMEJp0jUM1UnEcawQhbsMGhTmYvzPEAzbbTIax-cdCg26x0K9sdrJVJ9ENT21x2FiIU4ApKAHpLDUMt7rrbShXMYSht1zRh0gTMDGEDyPeO5zPK_Qn8-1iCzs_JVfItbuNaq8YVdsNtniLyur8Tb54U-sGqjxJ9U0QuhX05ybWVabxIQEWh8-iM_EgQ4SnDAqaUyFhDdx40qxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/25592" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25591">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYbUQ_GvdhH_yRMXsVDPznNWd12XIGxl8bxuGvc3qf8Ak4tkWUzCugOEjMKgpkMqfBi2ocXJ2Iao1H653XHxDlNlmpMJM8H-9JgNhwhP_1O1kk1cIkiAA7Y_JO7q5dnkA7MN4EfTlUJu9NJel-7hr7t6fxvG3TyZR0H7ff5UUhYSEGd_IBCGeC9FVYNGtXxcTC-dWXDWwS4peJWPE_O3pdCQdUCxOB6mKsUgbETycLlhDg34IbYbVI9vIB22JwIGnNYlMy6Y04F3JVm_rkL7zQc7iFSMR2Khxe1CDYR5peGPa_ltTC0Gffr9qXxUjjwN2DuoTf0-FFQfvTMDlaRskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی سابق دوتیم النصر و الهلال با عقد قراردادی تا پایان جام جهانی 2030 بعنوان سرمربی جدید تیم ملی پرتغال انتخاب شد. دستمزد سالانه او 1.8 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/25591" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25590">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilg1B5694AOsv8sSxMvm6LY7HeXfNcp1k2Wa67jEx-na8rvTZIn-2SahcpkFV8ctnupzXtTSdHeFYxvilUGLcazWmKoWfSif9UC7c4NsTN_GJ-AqtiwT_SGKrViCsx5ZzD-YRY6Om_v3U40MmFH39ehY0dXpCBqfSR-eDSvHSX0TSP59HwxxDW98ZPAmb19vCO-lwdInMxaBes_dsGyRoVKxg8um4nbp08s2VxRA1YcqgFulwvxMWcYmSJxnlah5Ysy3nFdJvm6A_FqzosPadcxRRDSb_-fss8wp3DHQKnsoV0ZPOhGft7TpvGeS74Grcc1dZPdH07osCLV46AzB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/25590" target="_blank">📅 13:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25589">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DS8MJkJgzIYw5YolAHcb5kefhhmVZOmgRHK9dNZ5hdzwFOcGflQauagnssqSx1Va0SjRb1wWdzd7ZUuu1htsRXx2Ko9NHrfuFS_lhw1rFew4pRMFYboNrJLjkxu6yVXfPQer6iu1UDE4DWfOcPRKPhiWvYKqPUWuegSOnOX-I5ykmQ2GPylqXG8KWtCopXX3G5ITwWQ08lpLIAjyaRy05UX1oXJiqlBMzu3YUUUhXOKA0fCX-0NRintU-Sv6ut4AG807-TyvF-ZbvSQXBOd6zdF9jqLoFOyG1JV2lHoVylGmv-kA8KHofDUATZo_VcqiVWGdj-PnFKdbvrtBMh0c2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛
یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/25589" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25587">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSKNbaDvhEFOuhM9gZuZ7zng8s8k7QJACki0AplsHglZS_k3sSD6L2E7xFYxnvQb3RFTJ33nImOlLSBw38TyoQnCTmHM7xL0jELDf68X0ir8-yakr1QdVavu0VeRmvE9NLzZLKoDczpY_n4-1ppSGvegvGXcQ-13OlVFoBYMWj3xyml6QlNv3pMHUsor0n2iHHYaNQzkOzVxLDNtG64xm3GK6uy4X_lM1zUFvZm6A7jUlsai8kO-k0GR1fR4yKt5h9yio1INjeG22A6gp0tAl4V5liqd-2iZ6v14vlz1qV-4QivRmlw-WLD0hW3shQYn8dR3ok3ya-EqSOEjRu68cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIM1P3OOkMl00T0QiKRymx9BfpQAJKIk4IJL8-gGULtCxNefNN5EG-8nYRkdZIegYqoYoVbO-N5obII_MxKu2D9UjYqmdbb2xaKwhcSMBIHyMU5eI-rtNN1C8PjdGGiZ2LNpI33VWIF2J5p20I-WPwbRZOVs6q6EuAVUba8jdWY8wDGscxo09Aq171PUrSC3Upe96zhGpHhEZ5g16dyWO-47sZCeUxrtRY5bmEVdsOIyNa_MsHi_cRNOXy1CCpbubjcYOoraITQlzXmKagvHkWcHPbrUfEKK9n-CV_-bQy5gXBLkWLqHjuXgELMeoA9NoiQ9M4OLcwFRyExRwMAG9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امیر سام دلیری مدافع میانی 23 ساله نساجی روز گذشته ازدواج کرد. جالبه‌بدونید که همسر ایشون مدافع میانی تیم بانوان پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/25587" target="_blank">📅 13:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25586">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIs9PQQE95zWrfIe4RrinkNLX89ZdYTEW79BITeYKFX6nz1pDDpsV-Xi4YjdG9sP9Ds4W9OY_yc_f5rcdAT8_ng5pYYJwE5S_Jc1nXuV7MhjlJnO7AU810FebHD4owEjWJe53YFnsm5VpOpYmU6p93KhaY_D3CBiaaUi1PZ8D4OUGPQL-WJuHf46CJkZg5kJgxRVv43F4ed1yPIhtAScqbdiji-ZK-qEF5A1K4zHBW8ZUuiZsVLu18zXYEl6JS2w2W38IN5jLVctsnS96xuS1mp9kgIU28iB_sbITUPsGtd8DcKSMVJn8WXJMviCSA1u_tk3VfW_AI7YSTmaNOo-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/25586" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25585">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=XwF1yGhUoMiEXoWPN0alhJ8DMdvXQSoZVO4PVTD_3n4K6BRys7qUDyBzdKAvIQRJRVdVOncqsUw8j0H5RQD6d7KLscmq3ilfYdfZtrKKQDDqJJa7Pr4zohJd4H1GCyjMj-pbVptIlMFX5rB8FtFOM8CfsP3Em5TLWSQHn8YVcgdMGGnI1vi9o_321EAGUlz6ryr96R3dyI-28MOXRR5sFj3oJKV1BknuH5X-3tclunRcdN72c8tX4YF6NRNZ_J5IRSsfEZHAYv4kfjTnyreq08H64MhXT2xsRibbElerh1rGMQk9k-Gej8kM3JUKfkCIpBH8W0IHv6GiFobGIRC4Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=XwF1yGhUoMiEXoWPN0alhJ8DMdvXQSoZVO4PVTD_3n4K6BRys7qUDyBzdKAvIQRJRVdVOncqsUw8j0H5RQD6d7KLscmq3ilfYdfZtrKKQDDqJJa7Pr4zohJd4H1GCyjMj-pbVptIlMFX5rB8FtFOM8CfsP3Em5TLWSQHn8YVcgdMGGnI1vi9o_321EAGUlz6ryr96R3dyI-28MOXRR5sFj3oJKV1BknuH5X-3tclunRcdN72c8tX4YF6NRNZ_J5IRSsfEZHAYv4kfjTnyreq08H64MhXT2xsRibbElerh1rGMQk9k-Gej8kM3JUKfkCIpBH8W0IHv6GiFobGIRC4Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/25585" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25584">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMPxev_mPqMWodIVT_4xgkUT-Nibvq7aPDTLl5YwQ1dKdXC7kBrjZ_u4N5o0twLypWaxI7howh5I-6VdrCHakqDVBaCd67XPkjd9eom58-R4twiLzRXRQqYqSOfYfvY4lu7NF7NYM07gxXlD4R_4PBGP9nAS-lh3RzLW7isoEiJKzx8VRffUSCR9dXvD2Bm-VvoUjc1pnQtWI5QzKXYR9ZWdOtljTMA6W3DgY7pnH4LaZeKUkzeL59_J-b0RGwNiz-o-mrgFa0DzJYq_STJKq7YqChtB_wxATPP_g7kPbHHSzQqFdg-GLrJKGBqWPnuB5bDy2Jn08S2aKIj8XUFivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/25584" target="_blank">📅 12:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25583">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL5DVswHqCNkrdF6PXhHQdO7pxalIyxIzUZSs_0eiu4voedysE_8n4pnzxPBkkOIYAuyW5sIQr23j-tUt6OaxHadVFFBX4nI09CKtn60xGtqLSX3-SYEFa0j95Av-WgKacEzPsx603R_YtjcEnTL0pgm8209sZteicC0CfSmGbcFjCV850kEVU-W0ta_i9AONZ0zxHbnDndqa34vDuhifHHICOtjAWsB0RvxKAfgbjqsxTnf8QrbfROFICqyJHubFbSiIsWKE_pdH-YrA-8AJmcoHFRVy7eLHR4Rb49wrqJzRauHjR9wQ2VHfz66h0nxGlVky6hXEk3ST009y5R3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/25583" target="_blank">📅 12:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25582">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-24x2mdOMOZuo-NZJKF5N0NwQZIVDKLkAP5zWwNl01c-iasdfo-Qe1U2XTUCrjBnyKk6BJBdZAv-dfENj8z_Y9qau-w8vi5NBqlefGT8bpguB8S5c4JDRDEjbuQg13CxSxyu-wespRSIRLtv16QynsXb7tOc9FKZdADpVi9NyomTsHoKYtcLpLYpIwnyRxrvXaaBKf-ZCjWYFhRDGVyvtmMyLLZHPcmUj1x_UcQfdh56IkmLzEbOOAsR_0-mG68_FNyg9YsV1nEG5UAzjtzfcdluV1vXGZHIkV9pNV--qrXw--ZIySdZ7IWWKtQAPGJFfuBByu0LU3njnHNJ64CIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/25582" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25581">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUkBX7IL5_zofvk58dZbVvGuN-UJfXvnzKSyQtYj9V-fzW6PrAeW-7p0hSnPZnBpDw260hRmHc2mkQIUIUgqhxTkddJjihE-k2-gE1D_ex8MPb69A70RXhJCfGpb5H6ncFHnelrRolQKSDVHpBdy5kyM7G3QlgTTf5PsieeSAgG80TvrvKrvyg8oTPSG25BCqH4G97CWBH-9GP12nvqPp60-Ri3euAyLPLFIW_ip9Y_CqYTsGS1VNXQ43qBGtHrYDeSei4r3ryMbs2_IYs-HSZGwHUVMK2r7jbWRjkPFTbzGGey193y7BgHqelPdrxobqLKsogQBPtMYrGZyojU-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/25581" target="_blank">📅 12:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25580">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjpNRrEB5DmFwZUbWnjCxQ2aJzXtWBK2JhJ113iXcJ2D4nxgpBG_lKCmZanL5V6iUZtHJpII9xjPftPsnAmzj0x_Y39VcQHoqPg_AovyA-7wKeyKg9SKQQXB-TFEjq8QbKcRnYbFd8EtY-lQmm33iU7Ormh0OvZeWoKqVMtVbSrP7s9jesBIYz2hFhYzo9kntwedRYIvT9_XCsMS0SChmlwxgDGmOnkyHqrchHqhu8mXjEPa4SR2ea3XWG_CwOpQFHmr6xNJow99wbpPxPPHL4nJq6D0ayPPROHtE6oJgaaVvFnEBoI2_kngOZwvwfMiQJtV_GUuE1cK8NmdiKVujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25580" target="_blank">📅 12:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25579">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-ZbnaWVTskLm0Lim8ouDuZqxBAk04g9vzxWHfN1YI0N2fYON0_L2O-8SIroZMcuz-9DajPu4kvsLxvJgjjak2nGNl4gZ6-bSsbC5NqkJNnF7pdHVBxt7rSTcIjsKHPApVjdgytqE7AlIogcjQuy-A4n7_aer6ACNOqNsMy255GlDukUpuSihpvc7Gq_pN_rGTiNm0bEisC_mZSQsn1gVaukTbZCvm-36f4dlZ5dqtTBoKX6LsKTYlavkFKCJd_S9dOxdSuqoIGR7nT9Ud85nNl34gUVtvfYcYYYjcot2Dj5VKx9sR_KSG_2mWLuNPH9INkVIsU3jPz3VQkmGGtGyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/25579" target="_blank">📅 12:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25578">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDqCNGni-9-u0xPzHJlUR4QTpIW2cvP9_QwGpj0c3m5w9ySpBZzKZrEPk6sQOZIfoc2hZeKqhGOliruemJOq7Qhk0A8jWTxXYwhji74VOODqCR_3G9-nKUIf63WMN9KMrHqRUtXhblBStIUs3Fsjf5B1DhBrHK5FQs7NkBTUZxPwJY0OsF49t0q1q1gZ4SDt1Eh9LgClrGdv2OqVtS6elAUPYHeav7QLdzj2bzlLdz24JWEjsIT9T-fCmnxbP1cYpiXQ5b96Cs0qVcKaktY2sWbB5DZieXOzFd7ZQ2qyCnfrTVn9YfGcMkGFm4AHzgjVpKKgM8KRih-ynjBIhHM7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25578" target="_blank">📅 11:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25577">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adLfmKCIWhqV8KNiQubEGBeuKgl5qEr9aW3TvXZqDux2dVStNCKwzM63zaxfbq_k1lB20jxQKxy2pvg21iFP8UEsPTda123b9QaXgQX87zpQwJ-kP7RP-vlTe1n16UuHepL3oV2Wpx171q3AvHrcrieUfD1E4bT-J_WfOP59waVoLuztaWdqCkklaEwkUoQLyvMt30_TLS1TQlQQB-k92EcC_WJPfaJiFiN7jijfJUACBuuOJVgUfhOeDaBY6XgsPEUSiBEkWqG-UMgdCzLYDRsssHbe8XAS4Zcvb1DWJXjFyeoC8ooAfHBtHt0poebpcHkk_3xhtAvoWRKLjlibMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اقدامات لازم برای زمانی که مبلغی را اشتباهی واریز کردید؛
این پست رو سیو کنید و بفرستید برای دوستانتون. ممکنه یه روزی یه جایی بکارشون بیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/25577" target="_blank">📅 11:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25576">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io7_0wthx4KFQ3SAEJee7896oXhJGA2hlPvFrscDR5EqkxlequrWMZ1BQnAbQ7qjS8voNX1m1lACf8NnEtqbypB4FmrEKuekvGbMgh4mZcUfG7obYupm6WwpC8DywC2VNh72X8RdY90PyV0iI6-fmbbf6Qnne-FdkWHRmgN8MQWVSXgTylOl5QWLcdauP-_1XnOpWQ1qm27K_nm1TVIZNCAb2DPfz4svTRX_qlHL50esqEnstVENxGXgfR3gE-xuX4zJ50iFiY0iJ8-p01aL0bGNGilDcFdI8Fgm-KfhsRIBTsnb-nPCawfNLBJH69l-XkEiP8wK6YKnuFmooTBk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25576" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25575">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMEsq9fCfJdWmKrrv4rgscncz4dxe-lwcGiitrkHt6LEmenk6SObPg4FbVxlO1qWs71Ybt23YwZ6l7ALX_sGafNnnn3zSktS3O3DVTnibeTiwp92tDi1CwFUDmFaAUrsoeywiXK8f3WSXml_ksmLKUrgwGSKHHnha-VjsoJXiNUQYb0mGnHZNwxLv6be4BqER9RyFM7ncWvW6JlE7x7cHw2yb7rKltoJOvcWOfB8wgA3yA2ZUOFUuSCzjF6DYSGnMQeo4uYeXfOfaUp5k2wwzIq7zEyMSCieTDNExKCsSa_RYkNIao9wK54tyfTP_LAJCN8oF5VC30aXZ4-JE5YMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسپید و این بلاگر آمریکاییه که میبینید در مرحله حذفی جام جهانی طرفداری از هر تیمی کردند بلافاصله از جام جهانی حذف شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25575" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25574">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYNVEJKifLMmDs7NToHaPOtaXkLwPcpcQguCwbx_rVmcKZo_D6xH37nPjwzI6xJlDpnS9F0IHO5RD9kxdAlNbDSvRUKgK-AMrhdCB_6jDIm_JJGlydtUqFiF5HeC0mvCySk7PqAfuCeMw6iPEy884L7eXyTiEOq9yM3mxmXNqM7iv09yy3yjbSpJR6Wq7TFxXo1N_IcWSlKxsW66kVnZhz8jBksEFlcN0uVXuPWr9lIrZxY-II4zhLaDQ1pC5HPnKtGo1adRdEnM-eWSfU56YmkokNm_jkbzVpZZkJp_m_MKT9xHQkt7MAMYXtg0MDALj1qIY0DB6quIy97flIIIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
امار فوق العاده ی کانال ، کافیه هر روز با یک میلیون شروع کنی و اخر شب حداقل 15 میلیون داشته باشی
💵
اگه نمیدونی تواین‌روزها چطور بازی‌های فوتبال جام جهانی و والییال و تنیس رو پیش‌بینی کنی با مستر تیپستر همراه شو
😍
‼️
میتونی راحت حداقل 15 تا 50 میلیون تومان در روز سود کنی
💎
کسب درامد انلاین ینی زندگی راحت پس این کانال از دست نده
✅
لینک ورود به کانال :
👇
https://t.me/+HOIRMsG7xT4wMDM0</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/25574" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25573">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=lGOY0WjGu7_2cIt0eU-o3ZwuhuHy1pHJ1njCHz-5B5r2I0gCASZqIfm45TNP_3TkNOovt6fpag7Kx_xPOt-8ueEYEAs7xCKzj8HflN5-Zfsv-9HPgyhhyjJug3UiufR-kBr6JgbisdvNPPujm4glaylluWe58KKhPEAxidfHkera2cQVs2MJsMlairaX8QKm3BLUfED6zcVlJIunBiko93R4W2V-BdJBlK-E0C9biLMxK5n95lapnubzgd3g9pbF1HgWUemCSuai50_Y8LGd4PboP6u_4nYDIT9DfsDaj8QtDh46cqHx0eCU2ge25j72eeRPXG7dEKWajkW1veF70A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=lGOY0WjGu7_2cIt0eU-o3ZwuhuHy1pHJ1njCHz-5B5r2I0gCASZqIfm45TNP_3TkNOovt6fpag7Kx_xPOt-8ueEYEAs7xCKzj8HflN5-Zfsv-9HPgyhhyjJug3UiufR-kBr6JgbisdvNPPujm4glaylluWe58KKhPEAxidfHkera2cQVs2MJsMlairaX8QKm3BLUfED6zcVlJIunBiko93R4W2V-BdJBlK-E0C9biLMxK5n95lapnubzgd3g9pbF1HgWUemCSuai50_Y8LGd4PboP6u_4nYDIT9DfsDaj8QtDh46cqHx0eCU2ge25j72eeRPXG7dEKWajkW1veF70A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25573" target="_blank">📅 10:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25572">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpyjoizA-j8tBK9nUIK7T4TjnQJvu6jMKsiC-Ze9XennvYQraGUCWNUH4ncHLoMTaW1FsLvoYIVgitFyFiT3YrWUhhHZOcAbq6xgG4MoMxf2DfPvW_q3IY6yQ0dv5cLHvzZ9M7-fV7iL0g6Ht9FFW57VrbyU_hYVBJf900bJlh6b6gAB8m-c3gpBtdARyroWJttX-1ZPO7uJUkRS2o1PBmjhWGoE51BKD_JdnhZ8hhxGsXYdBBAheQBXszdSCuNoc4hDvrr5UHkgf70N_iwMNzSxbp3mkR6dfCpapA2yGdIJEKrYFPH3uSyF4Zqod_U9DR7vZ6e3tFaq-pQeJRrbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25572" target="_blank">📅 10:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUcrzcI9cQRLaMVS9yoMKGMJsl2NiaWwHTzkONSb1uSnUX83jZ_bw_insSuv6xnp1zpdUwRKweKGwNV-tmEAy-MEwKL6vnM5zcicgmblx--qQMgl4Y1uRcwYJM0h6qrwB2QHcVrrUl5b3X0oWSrGnsb4tG1OG3I4swhWRDCV5bShbX4Em9FKE41iN5l3esoXvOd0_15INdTK8tk8vt7-WRIRnGRlYN1Pgfgw56PFMqrtQSa_ZSqnosNVkrxywYZIH-Jk01VAFRl1JJ4PMlE0SP1YYHOkSkQLJBQB_UslQMJSJ1PDpHKm_N4er4Di6hV6_9tAAVzN-oc60S3NBLOUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25571" target="_blank">📅 10:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25570">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=kCfu8gKR4_woIKJddEp7W_nugZLUj584ATf3xJW_2t4rSUFuc_bJhZir80Aou2uxoHfLkOF_GTMPsTuzHss8CgTX8Cut8APkDcKnLZ8pZdifOKAutBbind3O8a4pwiJHqMVCwQG2L4lgLmHdvlmB_2VJK6eij-xJzu9zlOkuSYREzydpw6vDRn0ULjMs6NGowHD0gKzLZVzQNw9MvCulAmVJ_x5ZTVr2Z1SpoCl-2OZKJtMbJepo6yaIq3g793DmkVisGK8BAnYzyZIJwYbNZyGQqPtCZK5MLnk_41wX-v-NRXQWpIMHL5sAUm8H2dZ1sdouHjM0-bGSkSwMSPc-Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=kCfu8gKR4_woIKJddEp7W_nugZLUj584ATf3xJW_2t4rSUFuc_bJhZir80Aou2uxoHfLkOF_GTMPsTuzHss8CgTX8Cut8APkDcKnLZ8pZdifOKAutBbind3O8a4pwiJHqMVCwQG2L4lgLmHdvlmB_2VJK6eij-xJzu9zlOkuSYREzydpw6vDRn0ULjMs6NGowHD0gKzLZVzQNw9MvCulAmVJ_x5ZTVr2Z1SpoCl-2OZKJtMbJepo6yaIq3g793DmkVisGK8BAnYzyZIJwYbNZyGQqPtCZK5MLnk_41wX-v-NRXQWpIMHL5sAUm8H2dZ1sdouHjM0-bGSkSwMSPc-Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25570" target="_blank">📅 09:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25569">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqvJCOoCQqm0t-Buu-WGl8SXcCrICcuPDXuU3LlDjDQkozlI37hQuDVexoZjwnTKBt2bYfWcPSweUmVKQnEbWqk_hMn1dYf5iVAJ7yUHQS_cNiept493CDSHXcKCd60qVo3iX-LtHkovQaX9EK0RnEFk5sz6GUQ1A64a4jCpSqafYzO9tRmPi-IihCLEd2BK4RXcB_CsxG3nihJyauEpf_Musql8LZrNGFFz5_ss_PO0BkxFs0_wimf72ZEujIyljVz4syTtWlFM2Q7lttbR6hDkUbN8DQjn1pJdeJzW183ai3HwvajzBgoYBOxL78HvJIQdpB6U3-wx3EmXX-xa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25569" target="_blank">📅 09:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25567">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iit51OLH6yRtsqADh795Jztamu1YIR48zNET5rPKlv64tNQB8thNjh0TEIuvrWRLNXMaaezBFkFuid-5D5yiKoTixpRJ6p_VslKUxinKnoidhui_xg6ff7I0BC_hgKFtYQEXNanwx7N-Wc_Hstc24EOnyO_M5hY6g4dwM32p_-H324T7Gr8UVk_8faj8AEIlY4AvoKBvJoxF0W0MQR6WwYuAkTnBub7gV3Du1pWqGblGfZBnmU3rx44HSRRc00dmO6a0TAllfyBcW3yXNXtySZHCoGIBsv-PG6T3ZbNBx7i7u0D4SI_UkH_IUdSUVcmBc4LDd-Gl9Tr-Zx38we3nOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giHJa5-mjiHbKnnkTbXqM3J0OZJ15vZYbGcTSB20zK9GtDGsJTnPrtDXPejm59Hp6g2wZFExrIIlpTA54kNJoxPGofjcaX8ABzwn9k2YzJZz7Tn_9BoeI2dw1y3ezMS7iw3_k1Kvq3xkRJAp-WNK3mNAaiEpbsPTedzo4dLcXC4p59Hc_v5ciV6v4QHj4iMLWPYUVvwx7sXCy9Gpx2wf9dJIHhAQGgZCVrRVBxZn12w-pIgIAn-VtfDOW8w64P22ohOTL5Cm0hm_aTUNrfn2Tcw9b17MoAdEVBZ8cbZJaHH-UeD2c-7WZcRZoq_UvtVPQ9BiClSgo6i4JOJilPMDTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25567" target="_blank">📅 01:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25566">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfa-oitmz525IyDyuTHT9vpUomW5S8oeumiu3-4De7AeadTNFiZ2UprMoWGPXFbpw2YYI9fVQ-vAjUoVhscx_T8R26qpDGLpO2CQco7DcVv86KAiU4FYj0DEkQD9ebR8YcCqCEYqHkDJgSwMuqoPDqLgIgj5Aj4Keb09SRrMxke0QRiZS6C_X5KawdyazkIoqR1D4GpksZzApcfrzQTa7B66KYlEJDlfeNcNOnDLzBfK5_xKJ-N6uyr8IUZ1W0IvtHpibXwTopTrHOuv-p-bDdzgrzvGlKx2srP6Gk4ga6J0yGfaLtN1Zr9r51Ctse1PC3gF-n08UKZ4xH3m7MqU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25566" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25565">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=JYFGsyrU6qIWvvzJN7u6_-d9Vk2mjqozm7mghcOcirIagEPzYTl6a_qj4l6TlZXlXwVj4vYxr9yyG2KRdRINuFM41ngv9nWkoubaPurbl81cRhrVKOVu7AXk5NplcQXYxU6GA-IPOkvgLCrJonvZjY0sCwNO2C6WB98v8XIF1g-gzE8--17HyGVq8swddEKJgU3FTEqNOBSNbBBc_7fZ3dbn8sSCytXzP7iVHxuzmVom7rgwGLdF2KYsngrkqRUABOmZ-YQWJbaNFI3VQpLmk8GX8t6L3mxPqB7qqDtfnEUqD5BPeCAfu4NiKpBJhIUtfFGdMurSDaiw4pOu4QohDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=JYFGsyrU6qIWvvzJN7u6_-d9Vk2mjqozm7mghcOcirIagEPzYTl6a_qj4l6TlZXlXwVj4vYxr9yyG2KRdRINuFM41ngv9nWkoubaPurbl81cRhrVKOVu7AXk5NplcQXYxU6GA-IPOkvgLCrJonvZjY0sCwNO2C6WB98v8XIF1g-gzE8--17HyGVq8swddEKJgU3FTEqNOBSNbBBc_7fZ3dbn8sSCytXzP7iVHxuzmVom7rgwGLdF2KYsngrkqRUABOmZ-YQWJbaNFI3VQpLmk8GX8t6L3mxPqB7qqDtfnEUqD5BPeCAfu4NiKpBJhIUtfFGdMurSDaiw4pOu4QohDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25565" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25564">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=bCggAcMYdbTfTl8RoXs7_hQAYFzXgXnydjDRjWdKfi4KeJ9OBMBbuW9ElE5WIrL1fyaLUgjyJuZRPK3uHH3k6t5mH4L-8G6YtHrA4Mf8NPqPDOtsTNQrZKkjb5D-oyi3y2hBlHgdBQgL5b8CKdh179UI6Mis0mN-xqtuyRTYSoiYDuFoMnFASpzMnbh4YBev0_efa-ZVDXSy6AFih-iP_PZoVqtoFONf991rCbcQ6U-b80QzV6evhWGIWR-MOk1Y0WmUK1CpWKD1OWWtHTWxJEvf-xgaCucRc_kEttXAdlwrLv09Ep0WBoQ-gysCmOFOxppbEECgG1xVloTLru4M7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=bCggAcMYdbTfTl8RoXs7_hQAYFzXgXnydjDRjWdKfi4KeJ9OBMBbuW9ElE5WIrL1fyaLUgjyJuZRPK3uHH3k6t5mH4L-8G6YtHrA4Mf8NPqPDOtsTNQrZKkjb5D-oyi3y2hBlHgdBQgL5b8CKdh179UI6Mis0mN-xqtuyRTYSoiYDuFoMnFASpzMnbh4YBev0_efa-ZVDXSy6AFih-iP_PZoVqtoFONf991rCbcQ6U-b80QzV6evhWGIWR-MOk1Y0WmUK1CpWKD1OWWtHTWxJEvf-xgaCucRc_kEttXAdlwrLv09Ep0WBoQ-gysCmOFOxppbEECgG1xVloTLru4M7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تکمیلی؛ علیرضامنصوریان سرمربی‌سابق‌نفت تهران از بیرانوند خواسته‌قبل‌از پیوستن به‌تیم استقلال این پستش‌رو از حالت‌ارشیو برداره و تو پیجش پین کنه!  علیرضا بیرانوند از چندپیشکسوت‌استقلال خواسته حمایتش کنند. منتظر استوری‌های حمایتی هاشمی نسب، منصوریان و مهدی…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25564" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25563">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=iZCDb6K1-6pu-lUZa1d1AwTdoB5wSMPaXTum2G2Y5_Vb2lMn6fqKyJ0pkcz95weGYcfg3hUcqYVyA0cvmye_ZRc103VXvc1IjB314yTjYplb9Fo-Z0DI_U49-ScjcO_64N-skZJVBOW89uUcWk65FHeLaJmwWA0kTAD5KSIQoakyo30jqsJ_H_eE06S2OJN608rOjlfk8zwXbIFp705RI407xbrSoJ09VTLStB-gbwFmjCq3VVwFhBS4_-zFGtvvT7bmZYcrC2vbo8hApDO29zl9G9AL8lO7WSuag4WNBjjC7J-RBIb5Gbzl9YUBSxI--_H8-fJAkbrXPiS0_R-Qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=iZCDb6K1-6pu-lUZa1d1AwTdoB5wSMPaXTum2G2Y5_Vb2lMn6fqKyJ0pkcz95weGYcfg3hUcqYVyA0cvmye_ZRc103VXvc1IjB314yTjYplb9Fo-Z0DI_U49-ScjcO_64N-skZJVBOW89uUcWk65FHeLaJmwWA0kTAD5KSIQoakyo30jqsJ_H_eE06S2OJN608rOjlfk8zwXbIFp705RI407xbrSoJ09VTLStB-gbwFmjCq3VVwFhBS4_-zFGtvvT7bmZYcrC2vbo8hApDO29zl9G9AL8lO7WSuag4WNBjjC7J-RBIb5Gbzl9YUBSxI--_H8-fJAkbrXPiS0_R-Qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25563" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25559">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIcOzAo93kW8ifsGHXXAp9PGkMKx1BqRdOq6bbprvB_WCyp_Q2eZpzLLcN0ZPoIeVxWmp1u_GUuGa7E1gDn6ukPYGgIxOYnOSbIKF_XYwTE6AYa_Ssk4bkOhi2TnBUWE2e3RrXwM3sW3w6tM0J8vYb35C49hLh6LRNkZnUTvXWiLYxdEcjbvzSQLYliKRCUidbwYqiBQtYFgTmXNAXjz3jghfSImCyktqsvG4SL7L8m4x1gGplyvy-4juuFRwIAMZxGX3Z3cg2xBgBvzii4F_7nLmML2HcedMSK62pjCkUDvfJEKPhB8O2I-TBy583VRgUn2HzhccY8HQj04aowTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25559" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25558">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIJnXuks6_U-lN_uLyJNSdZUyisSDiY9LMeI8FhkHBNcIREgLVuQTorSumM4C4cI9eTehMZqUvqjxq8VcP3zA0YufQV_C2Wqy-tSKtuE-NhMEKmbz2q3kS1Ljtalq8Di-TFLnkjpImcluR8dvmiG_8TWhhQAxpda34ti83d1ydw66F3VvbV_XUXuwHHBNGLJDUdCBz7gm-8TsahoVTMFLGPGuWXXRIXbuDgaXNAzDt0qlRzXhCZaXHJBDG18WmZ4p8QZJN4Gb1QLkJ5VFfymAqAhbUMBUsMt1LO0zxx-_8quv5AA3zpEmfPvqedMhY94NCEpA5KWN5UECHExvs0rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25558" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25557">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpJPnXdQ8MxpFGAtp5BPVEvC09GXYZ7MTFeJmInBe3LW8KfGMr53k6GUgFiW1hyJaML3ZLL3ZebA1lmxE4VJrtjyqzi_LG10Bg2lOoteli2cDRDRRYAmLOrzLKzSTsj7UhRNzoujaQdRjAA9YE7p-d4woABlVIUW-Wf3haLWF_zz63ZrYFT8aAHe_fyfft_uS_DQBm0f2TjSO-UcbGibmtudCzElGp1LPfYXp9cS_j4p6bbC-jlNjPUGlCJmCzBdNzhTYAdKhr4BQPb6G-og4NMglFuzMOovavDflxojewupm-v_55YlPY34h6EBsxk5plIB7Pbdn-vWrinGrTit0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کسری طاهری مهاجم جدید پرسپولیس: ظرف 24 ساعت‌اخیرکارهای‌رضایت‌نامه‌ام از باشگاه روبین کازان انجام شد و فردا باشگاه از من رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25557" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25556">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JynSYoJJOdg4vnG_LXmMQX08mHqtq2MpH3-7Y5AQSChdTcVRP3CXqvQ4TnQhk7GR31Ro7mJil-WnzkZTQgMhPbcY-1XMD0lfFtK3SJIhSyx1JhbfiQDBZQastgd5QlsQUgThcIewd7D37S9cB7_7V3etsfzPl2tYgmhQmEY6Ugu9aqm0XOFasI5xuwBT5lSsZjSGDM35p_z_stqQcp3SgOkzCrWaO6G5SfcaVtzhbLrpwqoQP0CgZdtVrTaTVc2X2bZDLar23wKS6M5tMdUfFOrIdRTWyeuD6b3vpTsozJmhkObgvbMzF7RSdb2YO-YbLy5jZKyaOyFG1Y_JKIRpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌عجیب‌ زیکو بازیکن تیم‌ملی‌مصر:
لیونل مسی، بزرگترین بازیکن تاریخ فوتبال است، اما بعد از کریستیانو رونالدو و راستش را بخواهید، حتی حس نکردم که لیونل مسی در زمین حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25556" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25555">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=YHUyvdH1JoZimsC0rneIcmlo445oaGGO5yDDsdGcy3CnWMpVr2d5nEtjeDRUl4wMpErk2D5-Z4YedRpxoIVOsfJKSbKSzqGb6Ug60JO3GuiidErBX8QQih0eQrAfflPcYRBp94cjmmgaSkHMBLtm4G4NHOEf4k1N04LG6jjFvTrfbKRvargmTF0skSHczQ_RzvFlDMso7AU_kaRrHfEhoPwfM6TMR9y2AaBHuJcN5aPpQq6-x8yrjMyOzsEwV-2ilJ7MZyg8ei0RML0TLQvmVI8AEnf0rsa0ivuIPAi0Gypftm-tNxHYxLOO9fjKPlyR5KEWyZBSIpDGSFFITb7HPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=YHUyvdH1JoZimsC0rneIcmlo445oaGGO5yDDsdGcy3CnWMpVr2d5nEtjeDRUl4wMpErk2D5-Z4YedRpxoIVOsfJKSbKSzqGb6Ug60JO3GuiidErBX8QQih0eQrAfflPcYRBp94cjmmgaSkHMBLtm4G4NHOEf4k1N04LG6jjFvTrfbKRvargmTF0skSHczQ_RzvFlDMso7AU_kaRrHfEhoPwfM6TMR9y2AaBHuJcN5aPpQq6-x8yrjMyOzsEwV-2ilJ7MZyg8ei0RML0TLQvmVI8AEnf0rsa0ivuIPAi0Gypftm-tNxHYxLOO9fjKPlyR5KEWyZBSIpDGSFFITb7HPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب فیروز کریمی کارشناس شبکه جم اسپورت درباره صحبت‌های طارمی در رحتکن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25555" target="_blank">📅 23:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25554">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDzh2d0ypJFhMq5CuyuyLhCQMe1LmZ2dprUioCnyhTQ9Bw_3gZIIsuXB1lRJ9mv3AbOhnGbefttGCj6RbmW_rYV-DjLTT4IxE_VAVDtk4X0LxNEx_pLBJhndaWA5liX1DJ2j09W_fnA9EXJYegfDBwtRMcwCG09s23KCkay3HpjmuYPdIVhJC0RVyva0rEVVNMCunc9n9mbjiD6wfcR_cl4MYgxsCwlYE8hgcfxy7xsymKa_DmAD4oOFFF2XAkOTIgQY6qYrtiwVE7KmUMheN5SjRuLnLpArKvoj9xSWK65sO_uxW6s-CNqW_oPRoPA3uxdxfvmJmHj6YTTdg4IGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
رنکینگ‌شش‌تیمی‌که تیم‌ملی آرژانتین در این‌ دوره از رقابت‌های جام‌جهانی‌باهاشون بازی کرده؛ به هیچ‌عنوان‌نمیخوام‌ارزش تلاش و کاری که آرژانتینیا کردن رو پایین بیارم، اماازحق نگذریم آرژانتین اصلا مسیر سختی روطی‌نکرد و سخت‌ترین حریفش، تیم ۱۹ام رنکینگ فیفا بود!…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25554" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQMammMSGbIEN0zu0eXYpe7mH7S0vEW6UMyjsJ0OUsxHDvNoOEjdtKa7VQkw7VABwUkpQoFJDYfnizh2IALb4a8gB-NBY6mjhG88bCab3Ijph7Tw7d98NpmGklarHVux-Mf-ejh6HVDAclM7nK3fLorfbEIgRWKYaZIqBujmTQGaiOm14CEGC--UQiMW4FsrSfuLPMXFkgHI4hrT3lS5vxpViIr6cR4-GTd1Sakc_2YYpNFvfT6FEeRCMAxzXf01cl0Pc4UUimzMDwftXEIUttmXTJIYHujSplwaIlTwU9NpRPWFX6eN9N7CuhP4rF2TpxDsBYVVaMwv5UAiEMDAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25553" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcFgNrvzTPws02Iigu9fSoxh2CHi14cV2aZbNEV3SD_a2zSIoKIyMkJe0KY8UqyNzNANCGpC1atT64hd2agJEPNrmTWjyz5FOiErYcHmQYNMsA2iLfiwyHlD7unooqQ6Qf36I2uZuOIhesPnmvERJaA4IpDSvvUjOeqpwk8KbQ00u_nFvVuM8p0k_L7PXfmlNOXM02HTSAaeMTNb-Oc2qQAsJ7_DkVZwM2xwrRFA2hHF999ZMntBhTJ12-Xf3JVQQpWSm_2gXhsdK_zeT7I1pXItrcopaJFmyYqCpAv3n_iBg2y2ARiz2gjOQKxRvlQ7sPCbGD6iqFoY8qfsp8MMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛ جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25552" target="_blank">📅 23:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📊
🔵
عملکرد مهدی تیکدری ستاره جدید سرخ‌ها در باشگاه گل‌گهر سیرجان:  ۱۳۰ بازی، ۱۵ گل، ۷ پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25551" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25550">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP9VVbBkx-rFjbAwESiLHmm2PtNAl1UJrjYrFWWRyeFa_1SfluVsrAPEAuwwTxsqkLPcFtktRmjpI-aC6d0FuUwiGlKxnx19qQkkZVIrS9P2_yDkoqx5oxn3sqtgUAdA7-y9tP21IFXwvAH9dhQ4unhTv6ObWJypLkUtwFagBurdrFCeuL1y7xSFWNezL6Ymc9d9v5SpbRa2DEkyID1u9riUDUWniMpVZ3cu8KaMgpfUJYBsrLkObnhssmiK1MGpfFX02NLfQU3URAJ1G5v1LPsLx3XZTKhRGv2uIeri91jB10-tzG_t6L-0io5BEKaj_es_74bEaV29W-DMUyWPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25550" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu5ai3V-NXiQ3DUxdCQDTPMi-B7QzA5GiO4nUGtYoOiJ7CwcBSWVMXLR3JlVKa-IZCMbfDalHWOYeim-EQP5zW_26v6n8YZdudJRXbWozB26mIScS2Jngo6rG5OzzyixoNu-ZjFYeVPD5XVzc5rQBxg8AuyYGUKHLuWFK6CjW6m1MGrWxBZroLkPk6N23QeNrapwIK3i6Y6rQBw_xB_t2YsAVoGLVjy3b2K5FsyVOEnvCW7oxwHEk_uTK6380j38nIyV9JGl6q99wBQ51jEEQKHUTJgpMEVN57ZZWyJllHPG4_IEHI09IUfEr5uHWL5n3G7z7jlu27vYVX5uXWiByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25549" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOxRsFHU7YeQs87JnRk7B7M1Eq5wJFPTCmAL5RoSw8LV_epny_Xcd8J39cUczYIJvQn44NsD0TmZm1hU7sZeI9Yi4gXhirgv5qxanD7XjqC6B5Kh6Jxz-shs_3VXRaneFes6OyBrD6qrzeOLl35eMpQ3__n-nBxQVNH5-bD1Khx8Q8mxeKdhcdUUK9Hqo8R062kWp9wFdVX3U0cgU0UxMgQhiKrPyGboSWrW6iAL6AIWoOmfmIqScJiT5UWUgymbSfs64foqwZ2HiYnzvKzrRqCSUOdD_jcvVkp5nYU8MqC8iirnbl43Hduu2diJszhRurRtrKV-OmIJcOYTFUYULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇱
فرانکی دی‌یونگ و همسرش که در تعطیلات بسر میبرند از چلسی پیشنهاد رسمی دریافت کرده. ژابی آلونسو درخواست جذب این بازیکن رو داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25548" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_047MukWGK9ZPk1dnYqlFbgXcMu0OLN4f3eSVPMmu1BafLykX0gthqYvDbwcJofFYTfz6H8kqjU1NR1ClpKMk_gddcPbgxsATad-jkbH7gv_DA19DNdO8YwIWYHdId24MS3NprjaZPA28eQdeFvuMCSe4oK3nYFwiyg41j8IsDZHCfHAPJZ0qmiX0TVbaqEM6f7UJpnkF3W1Ibt7rUjs_PYhCtYM95BrtuKsbHGI-4Tfva4RHlfGkyWoMaaFHr0hYcCw7GlPQ_Gvd_Zu87HXMk3osdvR8-NDo0Jw03rJm8hq3AX2rituDWtbfkVbzDbUqm7utM2UySksnhO5WiLzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌جزئیات‌ عملکرد لئو مسی فوق‌ستاره تیم ملی آرژانتین در رقابت‌های 2 دوره اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25547" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6WDUJczfrpmgVnVtRGMdF1-kCMxafljduDXei38X8Ekhe1kgH7wkiMjoZD4bEhaZ59weBEvQJWgwo0PyX_AOrfsTibIH8br4K0npTY1v6pMNf0ob8Mk7yqC5MfQgWA0W8AU7rYEIj3sq-CZuckOVv8IFjPJHlZ31wj7ljYxrPTk-slWr9Z6v1YyS5_MJaD3XUFhbc4I98JQ0ABnK_DhoRgTA1BEMBMMds5hJMCaBJ1VIvF7SAOB5WYIceZutN8pfWhfVPZhObqYyEUmMianY9Z9U2avfOSMuuLJM0E33m1B2e1knTJ6EeHT0IHfEkhPFDSQh8mvHv_Y8Am8tqfd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اینفانتینو میخواد فشار بیاره تا جام جهانی ۲۰۳۰ با ۶۴ تیم برگزار شه. و ارژانتین و پاراگوئه و اروگوئه هم یک بازی به شکل افتخاری میزبان باشن. مشخص نیست فقط برای یک جام میخواد این کارو بکنه ولی ظاهرا عزم راسخی داره که این پروژه سنگین رو در سال ۲۰۳۰ انجام بده. جام‌جهانی ۲۰۳۰ با میزبانی سه کشور پرتغال اسپانیا و مراکش قراره برگزار شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25546" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yy0ud4eAJQCFlDFOoYZe168Zr92PyvaTCuZMBXXAgM-6h_pa8UghgvSrZ7OhHJoGjjKuKtjO0RCbMf2Os3JW7_u-woPitD_qHRnJTtiWLephnjFkoVuGBMHwVxDrmxUr5mzbn9rIUvC4KR5DIGSWDPDebBRo5AfNOJpHZO4YlmW6mNQ6sNOYDHfBo3xX-h5zITAzS_MRKJv97e_6FgYgfvMv3gmn2NJGRPHZ6B0RAhKJZULaqcTDRlJf-m6AOa84ETfFi2RIpHcjyRJL4SqaqOPptzm70GUh2b_38o1mfAUkqiEnwa8qVZFmIjVYk8GkHqFiufAEV6oDUqiRcTKMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25545" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=A2ES8ccNZkLE84bwmYAhSCFZ55iyicKA6xNOmd5LpNxH8qRDW9SKbR4srPUZT7IT-za4_6bgU93YBup9CzIaLeYW9hJfIG0ksmTAERrbA3q52RNyAOx15v93aOXu6E2k320d1JmIhapRWV7n1f7SfsEA58eYW_e8ZEHgLkrE5W7TFkeSl-W6lrBWgkrOMw7_6xMLWlmp9VgW0mLq_-1E6-lyKT2dH1vyXv2ozr_XJjur04TVUmeZPwcykVxDoSnE49ImZtZGanu5XD_464a4ZlM974ICf5pD0-2WBVgIuwnKObP9GPtAEzuwBT5nPLas1muyzS3PIGZFPm0ym26Hjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=A2ES8ccNZkLE84bwmYAhSCFZ55iyicKA6xNOmd5LpNxH8qRDW9SKbR4srPUZT7IT-za4_6bgU93YBup9CzIaLeYW9hJfIG0ksmTAERrbA3q52RNyAOx15v93aOXu6E2k320d1JmIhapRWV7n1f7SfsEA58eYW_e8ZEHgLkrE5W7TFkeSl-W6lrBWgkrOMw7_6xMLWlmp9VgW0mLq_-1E6-lyKT2dH1vyXv2ozr_XJjur04TVUmeZPwcykVxDoSnE49ImZtZGanu5XD_464a4ZlM974ICf5pD0-2WBVgIuwnKObP9GPtAEzuwBT5nPLas1muyzS3PIGZFPm0ym26Hjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIjkBqwe19ILC8b6zVcb7ySjegeZd2O0CzXlDUi5W8qrSeoBRcmER4W87kttXqb01Li1PKYPmZf_gcCM3cvTDNfT_StLZRsdN-uINmY0Zc_7j8HJa_74ezb7dz5ZmY6cEnWEszhZfVk1Nv1xwdaAfLWLE_u9rzAlKATdI8qSS7bYaMOXyDvP7bI6ATBneUW-pWor6_W1Rmo31TpkBueJKGs790H_aLFplkIA9vnuWvTFRDqMJn1qDZF2mubK29yGirUTyt0hXtHlV6dN60IFMXS64cINotoDjmDUd-YS57kzsTWBJBgEmXXsAgVhfoBwjDwsgKBEkXzExQIoJswIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liNAazDPu1rC367Zdx6mFwosgJEzuY_c14HjZoW0tYbEl3xgshsrFwkvOHBrnvAhYUVXGQNLa8ZBNIFwzjb4z_sOz_Iz1M39JO67L_BCm4yYV1St6tFtk1iIxH02zLLJC_N3KwdKH24x4z_BGJw4iwORTy7mwCNw1Hr_iZK6AItkPpZmnh2Qp0neQh3tZl_hgLn5M94TI5ZOJLLXKYefTSrMNzrhxMs7z8FMT6G5pb0A-qC8YLvJsQGGqRFn1DaI374RFBdMpJgegXjAT5sDwgo7ysQgegNF6zF7O5o0dbsk7W0KxwKcaO1uKtDegHaD0XWlPWZ8FWJyjnDFARLidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104d086276.mp4?token=pn_OcDl3t8MjpCXWENlNvHtz66Xru8pBHoDX3g171xn55vg04YHUUSfCNUyKks0zOVpYTSLf6mnNpp5vJnYi_L66rr6idU4yjSXdX3qhJuCRBdB997DrfNmgOf9SnxrZQ_srbw4P-VfpPxP5PnQbBcKUgoBp0-U24U3pEaJHmEqqfklvpbavICfZaymw1_weZq5ByIick1FZtA4mCLbzU5dnJX6CuHs0uFtJHcMJMk6oihw7i3D5W08WF5-Q70kpbo-hMYil4bDF8jPpOxmRDOS9mClPxipv8G8stm2xPFDNU-UxSxpo6gKlhKl25-DtY5qx03bfkg0Tc8gRBwN6EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104d086276.mp4?token=pn_OcDl3t8MjpCXWENlNvHtz66Xru8pBHoDX3g171xn55vg04YHUUSfCNUyKks0zOVpYTSLf6mnNpp5vJnYi_L66rr6idU4yjSXdX3qhJuCRBdB997DrfNmgOf9SnxrZQ_srbw4P-VfpPxP5PnQbBcKUgoBp0-U24U3pEaJHmEqqfklvpbavICfZaymw1_weZq5ByIick1FZtA4mCLbzU5dnJX6CuHs0uFtJHcMJMk6oihw7i3D5W08WF5-Q70kpbo-hMYil4bDF8jPpOxmRDOS9mClPxipv8G8stm2xPFDNU-UxSxpo6gKlhKl25-DtY5qx03bfkg0Tc8gRBwN6EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه جواد خیابانی به قلعه نویی و کادرفنی تیم ملی به‌دلیل‌عملکرد ضعیف در جام جهانی: فکر کردی منم عین مربیای تیم‌ملی‌ام که 180 میلیارد بگیرم؟
‼️
هومن‌افاضلی‌خیلی‌جدی‌داره میگه فکر میکردیم که میتونیم تا فینال جام جهانی 2026 پیش بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJvC9PdJYJkezA0dlwgwncoWR97xreEqihzNKCPP7gZcKYz78XacufEgwgVBtGWReLUiXdQfQSYrjnT-hztchZ-Q6QRSvj1HUOter3kgRmanhx9MIqeOcNARDX40JuzkY0jSTkGVKXKQVDHIT35TbYaigwtGx67RHT1YRt6Cq75zh5-To2JpDIQUwZaKnDrQp6L__0hHBdiiinYmpya9b1CV3gmjAtmAHeJjvenwMjW5VH-MzCDNMJFyH9z9IWPOueWM1ebyTI9E5BR69-Hw-1rlzGsqgaW7rvhorV0Z4cbwqoj5cjyUMWgyKSrHPzjwOcIYv-h56F-NwO0YzT631w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8BWQvlhFmvgozhL1zTyhH9uPS0puqEgM7NYN5z0vRsBHzhIkDBUnjkyXJ2ZCZgLzXpo4-47hpPeOyGEkqnaYVg0AEEsxChrhf-TvOOB_WylX-j2PNqloYImOYVVsqXH2xujLcKes6ODIeNV9YOBT3FoZvzi3I1umhqo23cVDu-2IU0warDiVG-HzIMRQVK3sfZ-3-OKVV6PbpnEe13iy2xnkEBR_oPcwY5isrkof99LgUmHSJ6ww90YzU2pBT4OA-_YOWU8SleKkR6XFX9TnGvvYdjTxUF6_M6gXDTXWxUUltezSEqI0vC3kwuWWFYFvmun_oEManjAWc1Ru3NkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwkV75-z44kJI0PMgcblAlNSqytHkJS_Kd7MYFt9g9x4ajAqfsjwyEjH56WsWetAXJsW7O8rKP_wh-EberBpgtKaUxByH4lnsdR1lbgwzfw_8di7bpvt1HjgVlTpFqIBaD4MWtxFhzxKzelpLZ3p1QGL2e6JHCxdZuSKXWdDcXBx8QeFpmEoxBbvPmEckB0d65UND5HMQFZ5VoEUm9Y92G6vanTdSzX6KAmJTa5PNjlNzW9vPdV4GhHlPZeLAiIjs1twPTuq-lKBJCEV_hIOqRf2BvMcfu9A8Xxh8id_f46IcTQDmnyexfTRemrqBJvTeRHojZNK0jtv-9avTYwA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=p84Qh7aPmb3f9IQwJ2gMpWKgMuH5BuIOx2wrOEZce10C0WmCm1wlVqNVq2OAcEcBpZInIl3nSHgEXUr39y6y2y3TbpZI7NKgJ3GJI3DEsANrZVzijeq33M7KR5W2UIvRV10g7IvXjgE0wGg1vP1x2aC8tU3hkY4e-vMtXqiBqq1KUYAIg0nNKr7Uh2yBHSfO9zV9_9a1C7elEAfHpQERWIKFsen3Xok0DU2mhioV-TEKvCpzbQJlAYUDzoPJV0tpqkuchr7H7DyHQx_5y8-qdhRGvq7SuFJTqOcW2-gXrBufeQwZR5X-zwRIpLovSDqSsefFkcDRWDJoYHZ25P1V1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=p84Qh7aPmb3f9IQwJ2gMpWKgMuH5BuIOx2wrOEZce10C0WmCm1wlVqNVq2OAcEcBpZInIl3nSHgEXUr39y6y2y3TbpZI7NKgJ3GJI3DEsANrZVzijeq33M7KR5W2UIvRV10g7IvXjgE0wGg1vP1x2aC8tU3hkY4e-vMtXqiBqq1KUYAIg0nNKr7Uh2yBHSfO9zV9_9a1C7elEAfHpQERWIKFsen3Xok0DU2mhioV-TEKvCpzbQJlAYUDzoPJV0tpqkuchr7H7DyHQx_5y8-qdhRGvq7SuFJTqOcW2-gXrBufeQwZR5X-zwRIpLovSDqSsefFkcDRWDJoYHZ25P1V1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگهام ستاره انگلیس در پایان دیدار با نروژ:
مادرم یه هفته‌کامل بهم میگفت مراقب زبونت باش، نه فحش بده، نه به‌داور گیر بده که کارت زرد نگیری. آخرش هم مثل همیشه حرف مادرم اجرا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVY3V1HgLOdziZxHLk1H85N0uUyzIMDJfIZ5DePRScp3QhPNrpCizr98pLkov9zvaz0F0MV33Qa7RGRTpV5u549PAwSycsAWGlW2CUo5p-zigTU3wNKU3IlteeJOfNWYOYa8XAjwpcLTC-2U_x07h1A2rLjV42xYsFIuQi_-2cNO3dQWQIU30lX_F_hVT1u0QUoCzuuCxdH0cMNSE5rSR9lxyjPoZTX_B4bInj-zGdoN1i8MnTJ00A7SpbxiDrAqoCpC8zap7Jv5NBza4nHotdbenOewN0XWBogZuSm5xUvKMVdXp3iSr_sthLCFeJDjfHnJKLRORwKGqfafqcNzTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C64_otRMQRhGPi_yYzrDmTzWssAs-3RHAET9xgk6so29V5FN_cP1w74zz0GV2-4GWQwTYPaAwodVUjD2yvR_Me3ifiQB05qLz0L1NTFMfsZh9gzzHK731OFt50IbXwX8YMlENYUCpVnEVRRg_93AGR3Ar1m0z4MH0tnfhXSIflZnNwpIEAwjCvvqHPULtYLwPsyvyWzqG9TTuVtpbVumvzAgQtHI9t9-H_DSp9DqcBajM3Z6IcLd11VnfFPLgb5cpy0-bE7dli4dLMlOXRrBEZ9FVbwVJCWa9pi_PBM2HlNiu77FbHoYx6W3uCnTrqXPfUPmRFF0GZLQ9m4U9gb78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jkp-o4VCKIt3aj_fcj1lodxceVAW6GSz0_XLauU0634vUKIeV57y5g_eTTlgf_o5QMLQGtlI8gk3jThnNucXHhl7PG82Jt-Yf9miNgsd_2EfX2zkYQLBon6zGYTLtSPsuZdtQ5VO6AhBkx04keH2LVgqIT8LW7yWDQkjAEigAP2SY1mPClBUMUFc-o9Phrb_DQJ_seEHxJ-H47zP4A_HOAtiZHj4kDwdrgXABcCwoeQSVCb_0U5xCPsFRihmv1EdWo6v8pKW5dbPWTpuWd1Uvi47YhLq-cw_p9F1hkTQUr_QGoxVYPuUNyO8kGEmbbe3pxPuDC0-3TssgXaEWVOMFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=meUwt5dgRQ8kE6iTzd1oxGH0JYOUbRJQd037vGZISfBKVZPCHLkedR8gliOHuQJc21i4eLUr0N_eRCH_LGgGLVslZz4RA8s7AfEhAdq_RtAbL-uv83uhQXhasynQlP0vsX6G2GZgF_kyWgkWBZlXSRbWOswUIxGwipcrGnYaNS-0Ce8fTFLvTS5BVKXSZH7HThYLoV6NxdjdZzDAKfw1tuqr6hDLzXigf6Ybxu3kRPJ1kxaMi1zDPgW1WZ_owfZnRCYgDhfNaNKodx0VIh7N0Hh_fM1trNx_gkRCWGWwqfb-Mq831IUoxWwXyXIdK78nz2bXdaoEvZA0-pzv_RHN5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=meUwt5dgRQ8kE6iTzd1oxGH0JYOUbRJQd037vGZISfBKVZPCHLkedR8gliOHuQJc21i4eLUr0N_eRCH_LGgGLVslZz4RA8s7AfEhAdq_RtAbL-uv83uhQXhasynQlP0vsX6G2GZgF_kyWgkWBZlXSRbWOswUIxGwipcrGnYaNS-0Ce8fTFLvTS5BVKXSZH7HThYLoV6NxdjdZzDAKfw1tuqr6hDLzXigf6Ybxu3kRPJ1kxaMi1zDPgW1WZ_owfZnRCYgDhfNaNKodx0VIh7N0Hh_fM1trNx_gkRCWGWwqfb-Mq831IUoxWwXyXIdK78nz2bXdaoEvZA0-pzv_RHN5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=ua_t8ZsMaDul69qTEhGKs5IB_fxIhFk8YFjGL2xQwYHfLqIhN1uzVKy78dMZlcHfZYXGgvdSVujrGAx2SgVxyoM3-16o3JluBbg6-MGKddW-nB9uSjSdTo6997TWEm4e2o4aIGT6B_UJiYn0JoMgdgT5IykYsHuAZpvJBPvV1K8_fbIneR-iKJEABHwFM4XrF_euvuNYUq6fuPMqBpSaIPEkgs5n5QbxP6x_EMZ8_edYWiPNtr-i2mddkMceDsaCmI928eK36aK-eWJR9apf5t3PW9COZTf6fqT3t-lPN28gcQrkg_PufsyXmDLSfjWT9w8rTK7qN7S2OnoWzy1stA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=ua_t8ZsMaDul69qTEhGKs5IB_fxIhFk8YFjGL2xQwYHfLqIhN1uzVKy78dMZlcHfZYXGgvdSVujrGAx2SgVxyoM3-16o3JluBbg6-MGKddW-nB9uSjSdTo6997TWEm4e2o4aIGT6B_UJiYn0JoMgdgT5IykYsHuAZpvJBPvV1K8_fbIneR-iKJEABHwFM4XrF_euvuNYUq6fuPMqBpSaIPEkgs5n5QbxP6x_EMZ8_edYWiPNtr-i2mddkMceDsaCmI928eK36aK-eWJR9apf5t3PW9COZTf6fqT3t-lPN28gcQrkg_PufsyXmDLSfjWT9w8rTK7qN7S2OnoWzy1stA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=HSbxNAy0p3wJbhZv_DLruf7LciTI4pxmesDuZNdhI-nxjwdWxOR8sLVgctPWJAFok7xaGzgu7R5NsZ4cVU0Se2VU5i2OntMR1Ejx8Z66wITFOegR2EfsczLVMRDQIfyN5KXyAo3zK5nYiy9Rzq-J6slqNyEhrv65CNwte8MOTKxbvSA-GgQ8uiPOr-KB2npWfG6X9NUtxjH1AKchY7__ruR1rRoiPyuUw2iTZyefwJQKfKogiIdZkpUYsnavDU2g5ykPxDaXh6IuqA5Utq_a8Fs-Buithnujww1r-KtMApKlKr-yPQ6fDRrapEmPb-EcA7TC1FFwudGvBpa6RlC2UTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=HSbxNAy0p3wJbhZv_DLruf7LciTI4pxmesDuZNdhI-nxjwdWxOR8sLVgctPWJAFok7xaGzgu7R5NsZ4cVU0Se2VU5i2OntMR1Ejx8Z66wITFOegR2EfsczLVMRDQIfyN5KXyAo3zK5nYiy9Rzq-J6slqNyEhrv65CNwte8MOTKxbvSA-GgQ8uiPOr-KB2npWfG6X9NUtxjH1AKchY7__ruR1rRoiPyuUw2iTZyefwJQKfKogiIdZkpUYsnavDU2g5ykPxDaXh6IuqA5Utq_a8Fs-Buithnujww1r-KtMApKlKr-yPQ6fDRrapEmPb-EcA7TC1FFwudGvBpa6RlC2UTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQ1G0-KB4IKdcyCEfNNN5hCu-_syRzgXcBq7Y3yN7U6BMKNDxLuloWv2b9barpq0Oat-KLMYsuY9LKdMjPknrEPoyh1MsaQXr1MGCHeKTrrGrUlTuMjPyaxZsnsE4wkbmQrsXO76pKwvXf97Nu4WhPYdaOUBqHJHzpbuJyvixOK4aTqvj1eTTbxYeEF7fr64ZONyHH3MZAno5ftKBXk0vg4mJhsaaZDAoMln-o98Ww1NtwMAPEJJImFZjRHcHFwrAdfUPYZA6k6Eg1cMOU4fKYRIUCBYkzW9L_vh5GxRXO7Z5kfB5BDMCV80MGmUUrSPrAbRs_i1l5LRSXEFoyRYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyO2DS0fAyJRRcBxG0RLHHeHo7YCDwl0IWTtJ9EEOW-VhQe_gM39nMVh3wpitwaKVA3vHzvpBIPdbtmMJDJ3z_OjA7kr23_Gws_g1ZR_tM5ktG_8KTTSm5TU9pIDZLZI01Ur4nsf5MMinTt5aZvPhj8x2Q0ADE7QQMpiN2mYVtBsixmYw92q3roKxE6vY6kd0x6JNpaTScL0rVbSfJKoHtRseeBMTu5HBIhsxV2Od40JgkVhgfou4nfBW9pSQe75yO4V-DBsiZWYk-FGLn3rYT80qKHLl4x7QwXY_PChmE6RDXRbQH-mgNY1qlpAh5tu9O6ejwUD-eGUwJy31z9CHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lo5mDAvvpMEz7_f0IVqEBWMQLTZ1QDSNbMoMzGwslD2fgkl1KvfLsx9CgzpTLNOaUA9ZcfTBQ4a3OQIrpNLxmS3YGNW9DXompECyDuunzblGGY4RXcw1l0rwf0ZP-rOBIz_PAkPC-OqH6xU7fCfyLrYXKIh5iTdjZ54N8MrVnrFhgvni9a_Eo677gcDQABiy_BzlKZbXUtvk8dmYbG4fM-WBGJzBhzOAhsCUTOp-J3ztMY6u8lpL8lgDbHuATLE_HaotBv24k5zdU_NQeRZpxtbmmvRLFscEvbpzMH_JmtiKNV1GHYrnbGftRtUbVdpXxXm7tjZV7hCHDVMJNy5mDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fevxzuWT_AFLdyCBnrYlX8NRdOyejPSq33oscZ8uLxsqBKL1LbuuyllCOVybI0YwuJJ90hneoLIWF9XZHHOE-MkCkorlnrc70TnFSwhrypILv-m6oksXwbbxsgW0y7C1rXPXk7zh8Qy4-6XItmyedvBcdm2ou8yR_i5UCifls9H2vKb-ONie8bnhunAHK9WavKl2ZkrKfLXjhoBPNBLFfEFYCP2KPgHkjQjnMjWZBLLfkPSUDnRHcm1ynXiBDRpS8VaIHSf45zXYkxIPvRNcz1_1fHqgKGeGeF7YElnu5Luhxn4FW3zKLT1R96qE7LKpcUZq4mEFOnIpa9KGB8MWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=E_E7Cs84ngLqBTTJZ6mDKRsVfQjk7r_kpx9W6ReImt6ql52WiuEDukNzSNNPzzmyquFG41A_YeMmzLAbz9Dfs59x1Bk29fCG59b90be11rlyGVziHKTgvUmSXmToC4i4vVOWmj1-aBglKEb-uJ0dy9oAVIUraF6EfA_L_R9FyRWdEZ15WnPLiNDlVGlCgMFvlgN8NZppray6BNwig8dzQNLUoedcjrT_WegISEiHKd8pC9LevZqJQNs6W-CqrWfO8Bu_89UvWlLTygdSFP9qOkxpk6WJroKmMEeYgAumaG6yARgOgZXzgjI8IJBznUDsNLVV7uYaq62_C6W9aVfoiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=E_E7Cs84ngLqBTTJZ6mDKRsVfQjk7r_kpx9W6ReImt6ql52WiuEDukNzSNNPzzmyquFG41A_YeMmzLAbz9Dfs59x1Bk29fCG59b90be11rlyGVziHKTgvUmSXmToC4i4vVOWmj1-aBglKEb-uJ0dy9oAVIUraF6EfA_L_R9FyRWdEZ15WnPLiNDlVGlCgMFvlgN8NZppray6BNwig8dzQNLUoedcjrT_WegISEiHKd8pC9LevZqJQNs6W-CqrWfO8Bu_89UvWlLTygdSFP9qOkxpk6WJroKmMEeYgAumaG6yARgOgZXzgjI8IJBznUDsNLVV7uYaq62_C6W9aVfoiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=vChPPdzlehrtAC6fvUNB8Wf_3nLuvLmUawDr1PQdQX-5PGaoawr4jn23pS1VVtXN-erd0hoWXCHyXVuK79M0mhL-YmuCbGdWyde9Y8b9BXZoMapzlWtLuEhpPS7hViSkwq2uBpkNyKpPpVC5zLxKQqUNR-KGlCQ5adU8KgsYJC9WkURvHC1Ml79WRPuTsJm-y7N4NosNu3Hn_5dNS1q2-9EyglwxKSkhl4mfKGUniHii-ENt5O2v0SImwmRMPhIIlRFyw5-tFY61vYdbT2h8x75isbYzRIWcjkN5kzD0_cx5bqBrP6I2W5OvXeKahVeVvL22wa70sUNQ-kwkAiJMKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=vChPPdzlehrtAC6fvUNB8Wf_3nLuvLmUawDr1PQdQX-5PGaoawr4jn23pS1VVtXN-erd0hoWXCHyXVuK79M0mhL-YmuCbGdWyde9Y8b9BXZoMapzlWtLuEhpPS7hViSkwq2uBpkNyKpPpVC5zLxKQqUNR-KGlCQ5adU8KgsYJC9WkURvHC1Ml79WRPuTsJm-y7N4NosNu3Hn_5dNS1q2-9EyglwxKSkhl4mfKGUniHii-ENt5O2v0SImwmRMPhIIlRFyw5-tFY61vYdbT2h8x75isbYzRIWcjkN5kzD0_cx5bqBrP6I2W5OvXeKahVeVvL22wa70sUNQ-kwkAiJMKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=vKzHAzoAYmZ_edkCMrZSb0GDfP1Z6vIsrH7hfH-JKS2-DC8uIEF8lxsSz0aUSFsulUj812JTKyblu_wqUqf_7WyJSCAUpyzFoRqiMF7nrHPzRP-_tazP12uDxURpfZC48czverjczlNsZxOqRpPMgFkFe_avfbMKCdP_VUKtDWhmNOJFYAgJN_W_Td7-GYc6scKPCgQWi-ynv9FB2tpydAxsyj2fCvaEleJwKQZldjXnu4_Rgb4eiSHiwtPPyv_Gq0vlqxKiveU6yHo1EmVqFDxnP-jL6aaJ-r7MuTysoC5_FKWUs3NYnIewzgeLM8fUWr3cRFGyHqlK5rruuw4Scw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=vKzHAzoAYmZ_edkCMrZSb0GDfP1Z6vIsrH7hfH-JKS2-DC8uIEF8lxsSz0aUSFsulUj812JTKyblu_wqUqf_7WyJSCAUpyzFoRqiMF7nrHPzRP-_tazP12uDxURpfZC48czverjczlNsZxOqRpPMgFkFe_avfbMKCdP_VUKtDWhmNOJFYAgJN_W_Td7-GYc6scKPCgQWi-ynv9FB2tpydAxsyj2fCvaEleJwKQZldjXnu4_Rgb4eiSHiwtPPyv_Gq0vlqxKiveU6yHo1EmVqFDxnP-jL6aaJ-r7MuTysoC5_FKWUs3NYnIewzgeLM8fUWr3cRFGyHqlK5rruuw4Scw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehzVX1kC-qgq2cOb9WfryObzpiIoaZ9g05-6L7ogpvo6tRahPGi807lDaidgsekRrjD51dBSwdIzVbitE3eMu20GhCnpH5ByqV6JTI7yPNwlbfJ6l7OlVIha3HO9lQu4K06GguDF66a9Z8bZljgti6PwhJGi2kSdYiU4lYYNGhEwSpzbu3a_wlfqOTuApUACG4kmhffjqMgeofXP80bLWjDVo37ki656YyugphSr6q6p8eut5FhXp5HHwJsMORWnbm3Ym2R_eJRSXd4bwjhKPYGcyhDDtwIQgURHv0FGPLKmnEYKtN4dmzLSdSu4EYBdL4c_BSE5etpPbc8wyByTmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSouVQFgiLpIPknJaQgRIud5BfkwsA1R8lo7gw1-VrI3p8tf05yj7MD94fhRBmaJU2nh0TF3-Pk8OxU2pZifLfE1fATNkAq4CTT2V00TKmKUMR1LFjO_IRYe1MoOh1AGlOPWJbKFXB4bOJcTQnP-HL-n6uVK3AHcm8CdlHq-AAHI2hWrcOsEXCxzu3MZDgVw2MfmugEY1m8ajw_hiVJ8GCupnqx5_PziAegR18FNvflPPxebU8vPVkwqwumVqyFO0PU42d6k3o5Q58AnAWpAZlrN5Q2508yfEKN9JyEkT5rkf90kLylxJAds9YkCG2O3MYrWkeKYJ1zMfBulU5jrHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laPeoukNCRUzuYK0bPrYHxpwqUIF4BHuQ6ph1BNKD5Th8WN3ao4mb_dVpkGJ8LysWsCFVULeYF8WmbqkZ0uA8iBFkKt4XfqApUBw9mxsN6wi9jONyDE596xL4VYI6mWTbpThvM2mJsoiSxJUxRON3A966ynhxG5WdvZeICUT-zA1VLkpFrJ0L8q1X6ai-zntieSau5FL2V4zx9rZsgPCxnf3oItBugu6exmSoz4fmRVOouqvOJMFpZr_5fWGdK0uWsLWHcTn8coICYh0UQRaC_z7qbpGYwPrk-eb7wtik0Z6C2FsviiaeaNTvk_MbihE-_35763beJhSB1Dlxn79vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQ1FWY1bBZhE_rqwCy3Na8g2XwNFL9tZilRxAya1bDHIWdM82Rvf1Gi3-fcYfC5ASoAAN8MFK-vJiMSJ8u42IxGOK033YdXBzcv-dY_CXzGWJvUTlWYSMX5UD-RJS13zx-6LCnSY5qRQ4xrMuZrJanI01LAaSiMR2cQRURdSp9Jx1QJLdaD7QmetYuCK03dqhtEleQhiSEgxSLNiDvJlL7BrlocALdLOKxko_bj2MOGeg5LkQVxpXnsySLzVvWL2mTBDJd68hjckaH5fTU4moELjpn1Eq3DKq1-4rKDuLNoqt-PrRz-tpnaUxHhV3br4uEwFrBVlo_gsjIftyMZxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9kC_HQnbwg0ciQrSb4pP4C_0L49j74TCSKPQbcIL_QNvUrA4fmDuDTHodgrdgxZPH7yCoRBeSc-Nsi8km2bSYcoNC06B-00vVrF-i5bD4VDUHM_FbB2Z8TXWoSOMvdox8Tbdysemo_dnXa5NK9mUWOnV62WlImwXStOOv7DhWBxCqGc9nnQa26Ugoge74rB_8I1J7iE1uYeyusVeL0nyVoSK9suVIDo3JmdSJ2urZvrE3HcSbm5OPoJXE-UbywjQsgpzRPXeHPphNjDiGlXlUUT1bug_R1B67JEBjhBHfh-Q-bXsUBQYwsuoJSjCcYuUAwQJ6V_MBrf3uBRC4KYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=tVizQq7pIP-hgyB8q153Wgou47v92piilLqKngeNdTn-NejG6vZMpb_PblcbetTSljCbRi6X8Zf1Ag8TVcfcUYQIYD6OYbq6ToyG-__M_8g9nuyj4mYy4IHb1Rf6dYwJGVD9JViBwB8j5faTlx1ymhiA6O93t2tZOFU8MrAm2gKdX0v0tPSbcjluZODQRONZYWjg3krcmiscV3Bj4qjsVgW2ehpfTxrIvAdFNAzRhVzbAA6--wd_7l05MBBoxPNUs4ZBKkxoZP6FRwQq5t9ZkHYaqWIiAmm3wm_F4vziT3XHuNbiHbjNtlKbTj3AxJeHU-WWBOZFQ4A7c8oFlXgRzBPXRByU2StDqoXHZIIVGnKCozzIqOpvVmAYjDINmcxGr16cA1WzqVo05Kmz1KHmbWQuq3TVEEJCZM89Go61aYlUkCPcUJzRaWFxGHwaFnDEGS5ur8QlYuUK0NHKB6EGKQGR0tDfO3jSQEb53mOVrBiBx8dp7bLSjp62ayTnn1dJTDQ6eZ5g4FgSVHl3n0SYuDMY2lhh0BuvO7lwoh7IvINLMiDcGUTtp9s_-gV4slVK_pTn7a7cI_t6CbH0qJDfemqxUbtOoXIQjH-DrBhKkiDdPyvUiumYso84XBzoR0GrC7oi37YtrXFrFawhi8E0-AJnNqhGc6hR1ZTWVjGJdA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=tVizQq7pIP-hgyB8q153Wgou47v92piilLqKngeNdTn-NejG6vZMpb_PblcbetTSljCbRi6X8Zf1Ag8TVcfcUYQIYD6OYbq6ToyG-__M_8g9nuyj4mYy4IHb1Rf6dYwJGVD9JViBwB8j5faTlx1ymhiA6O93t2tZOFU8MrAm2gKdX0v0tPSbcjluZODQRONZYWjg3krcmiscV3Bj4qjsVgW2ehpfTxrIvAdFNAzRhVzbAA6--wd_7l05MBBoxPNUs4ZBKkxoZP6FRwQq5t9ZkHYaqWIiAmm3wm_F4vziT3XHuNbiHbjNtlKbTj3AxJeHU-WWBOZFQ4A7c8oFlXgRzBPXRByU2StDqoXHZIIVGnKCozzIqOpvVmAYjDINmcxGr16cA1WzqVo05Kmz1KHmbWQuq3TVEEJCZM89Go61aYlUkCPcUJzRaWFxGHwaFnDEGS5ur8QlYuUK0NHKB6EGKQGR0tDfO3jSQEb53mOVrBiBx8dp7bLSjp62ayTnn1dJTDQ6eZ5g4FgSVHl3n0SYuDMY2lhh0BuvO7lwoh7IvINLMiDcGUTtp9s_-gV4slVK_pTn7a7cI_t6CbH0qJDfemqxUbtOoXIQjH-DrBhKkiDdPyvUiumYso84XBzoR0GrC7oi37YtrXFrFawhi8E0-AJnNqhGc6hR1ZTWVjGJdA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKpH98UCbG5RCT_7cltj7XUsrJEeAWZEIUd8ZvBa4a6ZjAEO7okAwe_hpjL7_jjjVCiya7vkQ5g3Fidex796dq4hCv85GOy2pwB6DwuW-eee7V08Xq_R15hdijFfH3fWXA7LjnH5FfSwIZO3WO01Ve1LrF1HSPNNXh7W3ZhQ-wii3CtEH1pp2tGk0NVjCxBxi-8TlIBN4nMSdVaE5gFHMEHk_Xp-Z42BBnlhfIukCD6_-TbySYsz-QiUzt0KwhzMYWw29x2kOWSYyE51qI4lpL7U-oUNKwTbrtGoV-SWmtXmpS89239DkfwNlenV7lXZMdXswwKuc2ck9rqbN5q6sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDBaTQnWZtLqZ4msikZsPL8Z5OCnXUtkx3oqXK8ju6hcuHCfKcNM6cMg_hUoyPNYjGGGTvIYmfDGGv-7Swq2Wj8jPw5LsZ5T2iJ-PLivf9dpBAZEN5h1jNarufBmYnZUSPllivky8C5axtlEMCmHs_h_-V8OPUDgQZ6RvBwZD1GTJktvT9CKElDaS1wH8x-SJV3GDKwo5eemUwKfAG0zFI4XU_U1EefhHD1s118yEi4DIGpXXNgS_5yuZPFMOgPnuSGYi15HVwR98kHRhbE_JIi0E_aGfaakcTdArOCGBSHdVS_6X9IjDLGuA_iHfhijtJ0nc9RxUoJJ7095uQRkOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyTub5XzAGbjUeMy-QQ6OpSuUonODJquzBsHqrLx65FTDZnSj1oEF_CkKYQf5iqeqntzTOvOq_fK7JeqHn-xmbtSoFUk4gzmyB981CqScaANlwlLwv4psQ8Y1icGoBtUw_T28C3qpUQzG5T7sMf31BUkg7dXrflAQdSKOVLvvM6sJ-6ndEGZC-1tixEnne90eZT5eqYUcZFiP3bdwYHE5QY-TlKuxy5tHlIEJGPwzanzjNihV7xt_dt2IWzZjmnLZMNoMKN8ITX1RM57ifT0iWJeBHBFps0lOg_jgy_g8bLY5wW7n5WlIztg8sDcdk_3w4wdAgFeYZBVdVFxkhEjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIzE50HiFSrlUlSK8sH7vUGwTcIhYHcmwNiPhdlySdZme1Km9fSDqQxUzq12_GVnl0nObO3iHninYVqOIJic-OFDQckmQedzxK1N3iI0Ek0DX3ZFigmCL3IEPspd2M_dqAsEZz1o_JoQEfCZ264HRpC2iQFpD9_XJNDZjpKMdvxHbsOKAYy9GCNR7paxt4A0Yagp01kwouq7icOQu2d6nv8VwxIjrt8coMUPKWbgI562hlgLKH3dh-S78aAqwnlx5qiRtbYurSisNkSAo7EZPJhPJGkN-T8mlEk4gNp-9FxorLLpIpAgwbZKbmTq8skeY1Rqgrdqp_f7yrjIgJgvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELlQWoEVQW2f4UXDN_Vp36zZ7Z2IEMw7bY9GjRjWOETrn4wXYA2HsXDBY-S_h-xwgRjBxi_TR1lexy6yPKc0YRFK-6EiQ8guChqSPz90IIWnTJtUA__DtOPyOjsoPB2_gcDV71f9-jWqyvwXeO9YET8YiGV977JlSUtiMeQ8jRCW-VvjUrR7uWBXBQPIdNZIFy9ZhGXu2AP3A-xHMDRcLKWnnQagnvIW2wG9u6rUYcd0PX0iICQKGIcNZ1pJmBjiXU07kDl8QpEeOb7OlT_HcBKln0eWHj9XFxAmOqTE8UUbDuYIuQ_Mn0c4JjURqVwHh_Yk9rGyLe2hEtSnTFlnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY2bvz-0LXGdgUW3otW2I0oPdbvh6oWPEzVP0cBmZ304MZcx-KL5kW_f9F_nsaR1tVs9VN9k6u6y_MSHgTKlChj1y0IBkoGQllQtYkgA1v-UQihJzTyy0XIwvB89i8VhTdgGREbC5jLCHod7c08yQdXaUOACyFXbN3QRLPvvv8YQNhDqtVuEBQznTG4IJwFrhlC5EPReUWMGJ6v_csSfuO7UHg5HzQhLs0NzoaitpkO88mj-84VH0-9pQgwTknZS-cB5kLaEYUHB8MuTdjbIAFK1sbhp0Vf2nyxlpMQ5Rc90vfirUEo3nrXlwUcn0gWErvPRrgzHR3tgcG7oHGksig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=MDDWe6zzkdbaBTnzkMnLXvUJugomgI9oL5RlUVQhc-qqR3ZFzv2mJR2cV42pJaEtXkeL8PZ6_P3otsnzybfvj6dW5Ty2cF7sBx5hOr2L4qxUh5OieCkbU5Z5u6HHgHSnWjDHTYANWccC-7udqoiqlsUQkFEJCZnrHNt7_22J2fTlEHK1lcRD4h2VX1GM-tgLyriVLU0rMFHFY0-ww5EeFkfkux3cMkhoZyxMG9Mb1pt5whuHHR90-DnQynJdIMJrn86e4scF6IJz9OCxbpQ3YEraLwIwLPJGdYINE6inIfBC9zcWTmqSH1ltOvoRujuxbSjHg7fLaR5aCr5-_4HZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=MDDWe6zzkdbaBTnzkMnLXvUJugomgI9oL5RlUVQhc-qqR3ZFzv2mJR2cV42pJaEtXkeL8PZ6_P3otsnzybfvj6dW5Ty2cF7sBx5hOr2L4qxUh5OieCkbU5Z5u6HHgHSnWjDHTYANWccC-7udqoiqlsUQkFEJCZnrHNt7_22J2fTlEHK1lcRD4h2VX1GM-tgLyriVLU0rMFHFY0-ww5EeFkfkux3cMkhoZyxMG9Mb1pt5whuHHR90-DnQynJdIMJrn86e4scF6IJz9OCxbpQ3YEraLwIwLPJGdYINE6inIfBC9zcWTmqSH1ltOvoRujuxbSjHg7fLaR5aCr5-_4HZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAZia8gdPur-gCAql4Tncwbn0cSt3SMqLhXObx4H3EoQu6DPMZ2vdsismZoi1tdVoyWk7Pg-F7bmfCwJgkF2JTLc0m-iYMAhP82DZYSDY-dJzlCwzyButnzOnv3BQA87Ufe7rRpja6ggQTG03v8_dMMdD0kyGO6bIacEG6lCjolBFAs8JWyRjNz1BFqZzq6QwNXPx1fLrrpYSFDwuii90lMJh6Xn2idoACPMTeq65Bt9LV06cEJMaW5uYJSUnYXeeodUblgvzMtDFeEibcXxbsUgfu0ZgTtTcM2RUhyHTG7Hh6dmPpWZdSUHV2ED_x0Qi7omh1Q6UG6P0Z6y2jkdLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxFiIQKRVKh-8pKzKSxGk8C9_PUUVI0YMsogjuBRyqbmpf_rUhOiVBYgmlUVkgB1i91UiRcN6fOiRkCJ6sYTIxO_JMnRtrz1Ee4qttQOkmhZESIEbulurKFc9Ai7Kg5nbbHlYc0OrArjPa5_FxdXBRdUWW8-8F3JcC6YFTt-3V7ocOS0IyDuZ0pDYxt8a_GdbxGPlDPYWQELwkdTnw505rw2D-GyqdMJwUdGmTLXObkBMi5tdXMgJU2Gq8bqdnP6OnZExLDGcrXx6Oz_Ynla8Jru2xQ1PO8g8bpyzaD8qItaNHvhIWBcbfhKSc_chaJL8Z-HbrR9gmF-s-ZO59Wydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=fRd8U-8bVNxhcTjxoeiVWsTj5047VCtBwia9gFmHSLfrQpu08YYfxD_-c7igNwgAy3JFsjhJcFH4WDxyqBeVb15HQcJ8WERQFXaOMfaaAmapI6yEUMmUYt9VNfnNqlqWZbNct7Swx4LP88D9vR_iY3CtVNGCADEMSOAnnaQJgC2uwAL9kw6rcAh3jXv9gY2pxWH5xhb5cBzh1qeTNtk7EvDRzVcClTPu8zgEsxSXzlqzNY73MaVNGzoxCitISGCp_2AtZ6bh_8XG2chuk-6VXy9OSlSk7Fz6x8HYkTfMyqEKgPP81JP7nkN4xqvQJl6CejqSlNiF700gdnLtHhIOmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=fRd8U-8bVNxhcTjxoeiVWsTj5047VCtBwia9gFmHSLfrQpu08YYfxD_-c7igNwgAy3JFsjhJcFH4WDxyqBeVb15HQcJ8WERQFXaOMfaaAmapI6yEUMmUYt9VNfnNqlqWZbNct7Swx4LP88D9vR_iY3CtVNGCADEMSOAnnaQJgC2uwAL9kw6rcAh3jXv9gY2pxWH5xhb5cBzh1qeTNtk7EvDRzVcClTPu8zgEsxSXzlqzNY73MaVNGzoxCitISGCp_2AtZ6bh_8XG2chuk-6VXy9OSlSk7Fz6x8HYkTfMyqEKgPP81JP7nkN4xqvQJl6CejqSlNiF700gdnLtHhIOmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbZyPESfJNek8sBFLqmx1faBY1-GCFowauyRptROmHMjNOVJQS3Uvset6Rb8liVeeEOFmLKwi5qLgC2fqp87cFvPxBygv1E4atCZ0MfERyZNT1KzmMxFqtyqpMFlfTUp8ni3wWUQJkzToazr3SwmywCOxlVR_APkrxkOH6JD1xStF-XpCN8otNjhHQqlSQI8ZXZZVzN42Zm4PNqqtK-2b_aAabaDJRNgdYfQtR4Ff6nNbFdmmAF25HEimuHWX_uko7_2l-7bSRHEoDkFwDpppw6uHrWnwnPGcn_wSbpcqp64I2nx1YUHG-AKUgp3UKVX3eVWaBap6OL0Yyb3g2_q0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=EETg-GUkoKwAqR3g84Jptnqc_Hf-RNM_ARH7Z9h-3jw0sg1BAHOYJu7XJFDLF5dJAU20m3eLQvlXaJWNDxSWRWwNl3PvOS1OusQWaG-M1Zlof6GcMaP-EVhWmiNh9zHpaXYvb8qNinLGZHenb3rUxxWyrQbd3fD-JyUPjclmP139Al_duLu4CwDc29lczhFiaElSNIaJfy0n_mjQbQF5ZUVpMt4dDpDBpOSpMAiUPDYgXaSJJugHVBzSgrtQYpPK-xWKPZOLV2jjyZJRrvUyvy86OgTeWwhx74cw3Ejy3o_xYJXnMjEXX6gCh4Zs284qEY2ggdl4W26A423a0CVt4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=EETg-GUkoKwAqR3g84Jptnqc_Hf-RNM_ARH7Z9h-3jw0sg1BAHOYJu7XJFDLF5dJAU20m3eLQvlXaJWNDxSWRWwNl3PvOS1OusQWaG-M1Zlof6GcMaP-EVhWmiNh9zHpaXYvb8qNinLGZHenb3rUxxWyrQbd3fD-JyUPjclmP139Al_duLu4CwDc29lczhFiaElSNIaJfy0n_mjQbQF5ZUVpMt4dDpDBpOSpMAiUPDYgXaSJJugHVBzSgrtQYpPK-xWKPZOLV2jjyZJRrvUyvy86OgTeWwhx74cw3Ejy3o_xYJXnMjEXX6gCh4Zs284qEY2ggdl4W26A423a0CVt4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0OzrGGpfFu4GdD47r6YJWS4sVaopcLyzxFot3WcMzGBYikk_NS9FWYCC3GQ_asEjF9gYVEQOrondThj7YQqK-5WXUgrEEsF3N4UPTrJKKcA3pDvuLX8NcUHB7GvoSaciRadmyGH8YkF8zwg5wYTcOBR1fAySC41PL7yxPTqHbNfL6k10wcoXvCtHMTvpiVA7DHkxAgJPb9BNp50VNHamlPcVtJ4o7E8YBqj_xBG0j-qNv0fzykrzUckZ83jPlek9OEliM8S5poGDfdzh_2wGByixWF1_YEfycZzEkoekERzHOQLtvTj9wPN6xPDHj4VIxVBYhXQ5YfeEnW2ehbgaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN4ulD8oz74gAz7wB47k03Bsj3qJ_XSgl2zpLAyWC6U2mw-YXotPbVVPmeE_scdkCS7HLk1CeqCCHSw1aPbqCzqp0Tjlc3--Fj7fBWNISx34qBdpwt4UZAA-YAP5ofLVqGE0qYEQFjgas1eKZV7LN9xfOvnofS7fKCQVw-IJwBJEq4QD-vyyxOSLQUyhdpYK2f4YkaixhqZhM1wBwjlRnFrOGpy3zMuIWzAoICA_wje8pjzai26zlFFe8Xjt-VbEUkLBH-erGoi-n0ESMJtcZvDXO1rK3DF6rWd_ZOAGjiXCL5hrAAZ6T0tKzqEPBDyM9HXi7_otpIWFkKfC5I3vRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=PZLqaZyCkbrBmTIaStbi6mrFDjLU0KXhBOSdGR6QxAaqYJld-TLqAnZU8caUgoEht1SBW3SyWCUbtEmkFxf0tVg4oX8zVi-zl6eWuJ9Pxg9coCZabi7l-n2h3tiwtfJRj8_SCdpV13PE0iCJbedvJ-5IuOjLfX2ADPBBiSPUpsIZeSsB8Xm-DPtSlvVY83MNg654Edt8vxzNJN5pCjZ1CF30LajEpyQGhqwE9HVnSaswmgKQmdt25RP4a8a2U6ffRQHR2o4NWs_A06WrJI92GCuFMGDQTMTWORnWWVTVg4FiCLpsVUqGr1HvSqni5vhRdnhXzt3FfH-HvdVDy8E8tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=PZLqaZyCkbrBmTIaStbi6mrFDjLU0KXhBOSdGR6QxAaqYJld-TLqAnZU8caUgoEht1SBW3SyWCUbtEmkFxf0tVg4oX8zVi-zl6eWuJ9Pxg9coCZabi7l-n2h3tiwtfJRj8_SCdpV13PE0iCJbedvJ-5IuOjLfX2ADPBBiSPUpsIZeSsB8Xm-DPtSlvVY83MNg654Edt8vxzNJN5pCjZ1CF30LajEpyQGhqwE9HVnSaswmgKQmdt25RP4a8a2U6ffRQHR2o4NWs_A06WrJI92GCuFMGDQTMTWORnWWVTVg4FiCLpsVUqGr1HvSqni5vhRdnhXzt3FfH-HvdVDy8E8tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=YacGMGHIwwHgodF6Xf_68mKgOwOZB7Z6xxFS6HLYZKV8cdN1EEGnrZTZdt234m93yCPh9MN86LYX5wM844CMuS0rCi4E8jdlyZcy7_CgaFQMQLleF9YEnRv1RGDZUt9mIur4D84p0oQfBaptwNXeAumWplpqvxVsw7f-Hv_Vo305Flls9n0OySY39vpax-tc46FLrPBHG1J6X-MfFloWuyqJIk_TzEbk2bLwnDMPZvvSogwejwzXZE34ByOPpBLab2112RMq2Ta9LaNpZ1zKuopgZc0R3h64jhEEJWJ5-ZaHkmARymqVLp83CuJsv6PM3uru8wEzqPOP8ZXs9Yceww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=YacGMGHIwwHgodF6Xf_68mKgOwOZB7Z6xxFS6HLYZKV8cdN1EEGnrZTZdt234m93yCPh9MN86LYX5wM844CMuS0rCi4E8jdlyZcy7_CgaFQMQLleF9YEnRv1RGDZUt9mIur4D84p0oQfBaptwNXeAumWplpqvxVsw7f-Hv_Vo305Flls9n0OySY39vpax-tc46FLrPBHG1J6X-MfFloWuyqJIk_TzEbk2bLwnDMPZvvSogwejwzXZE34ByOPpBLab2112RMq2Ta9LaNpZ1zKuopgZc0R3h64jhEEJWJ5-ZaHkmARymqVLp83CuJsv6PM3uru8wEzqPOP8ZXs9Yceww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCQQGW2j2dJKnuYc6yOso9yOUNNqKHMILNwbNOKzY_A-4vvRXm145FGq0pkV26CegRwNe1Awrcg7DU00V03dROShE_PX64TgIZcarxpVZPjMwA4CvY0QiO_pCLSJHlKIQYxC8n0S3mv43seHpAhknqKyTYSDTjE6P54SmWSrTVJ-LmFtZGrDsmP2GnSXGiN5W9EkWGSNZBQfIxUg_rozs36h7nWxpjZhyLQcTppFxG_LJivlKdNQK2652YebbHI3qt9q9ZyqvnZFEEWmXEMjrDAL_NXt1c0vmF5cyWRwrSNdt3ManRmoHAZUmu_uQ72GWeGETD8WibK2gc8MYPhN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZkb8uKq8hA4aVT_NAN1SdI6w8k3PZHLBug75wl-1V0A-H7qbINBL6H8bNVqtX-8HW9rJbGGcV1-eLGNlQNdQ2PavssQgBV--mWAsKfUmovcBhMHCH-y9FuATCc015tDlarjXdV1weHxL6h4zs9Y2TH2Ya5ihSYMUlVmSDO9qevQpXzAIJ7j9UYUcZ_zUBTENwHh3V1khvXXBb7mw3M710yIy_Srw8YTYRPYjeq1KuMnGotwCMvUPCSfSXH5E-wgDJR0559bE-otI6Vzb1LEM4KDV2XyYv9T8WID1eEdvrjgEuE3CUn5FmzW5u_b7adWCo4YR0OPfY3lY4iy2xg8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=XFjopYvhYfR2cyX_1lmCRE_6aerv9UhLUQ4-F5vIChQdiH1xmnxyu3dAFU5Rp4cr860CMmx_sdLrkcx5IuJq0J_plQQFysUQuy4Bisg9duOPLTyre009X7S7bGhCUD1wiRbcEo8tuBGZPU4nY-ANyDYYaz87KTwnvIoxthgPG6yEWJjubZ6jUNqaoR4JigtZpTjikDFZyoOkWyjoQdkB3NsDiFGN_m2Vr5vHNwZa76ypT5prTwpdXKVS-6QiAcylsmbwHTBRQpqExNoW5Oa6AXkm_PaWoSkdeRT574Ryxhs0Au5LeBQiYb8zWwNLde1LUV5IZutbgovizMI0iSSuyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=XFjopYvhYfR2cyX_1lmCRE_6aerv9UhLUQ4-F5vIChQdiH1xmnxyu3dAFU5Rp4cr860CMmx_sdLrkcx5IuJq0J_plQQFysUQuy4Bisg9duOPLTyre009X7S7bGhCUD1wiRbcEo8tuBGZPU4nY-ANyDYYaz87KTwnvIoxthgPG6yEWJjubZ6jUNqaoR4JigtZpTjikDFZyoOkWyjoQdkB3NsDiFGN_m2Vr5vHNwZa76ypT5prTwpdXKVS-6QiAcylsmbwHTBRQpqExNoW5Oa6AXkm_PaWoSkdeRT574Ryxhs0Au5LeBQiYb8zWwNLde1LUV5IZutbgovizMI0iSSuyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUjAskMTALJCVGBQdH75F8qD4pORdl9iC0fL11OIoSHzZi8e5ywU7TDeeeuWHXqFDt7DkdtrVXEvE5pvtrbxQ-tmtRCqOzLrdQMAb5g7ewi93xPDVNlJiaF61C0GpFLuAKmjIeZov_p3T65iXyEL5Xv6MNqNnVl74Bdnb6E_jLOvFuIYrNlbhSAlitH9fKIn0TxDisybQRfu8gi2iIpJkN5nEzCpB6OQhSmYhn3zMaZTiwQyz3gtLiQAuAH2ta1UKDPmuD_NTwwx-UYiTaGWril_t2WVEvci5pdzm4TpPMVTWC2Q2MJGb6XHNTukJzJ7Csbc8B-YhC3n8cFmC_pZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVM9zHv17QYtM9k1d99QqtenISjlEvFvjcnRynACcQcKVy3u678Yqvrom1rmoqyzGkef5nyjM3YfRU5ph1lpNHTW4lSZSMphUJojTYs1VAt2jq_wxAFAtEYLnSU9iPqJmf1tRKipIKxM1deC4D_NrOAdc4rtZuzoKDdbAjOsE_eWgEfwZwOi7VttTDDrkIlmx86N6uL-mSYz1kyN5codFSXjwIYu_a7lOruNl6-8Jl0Zu9Rchutj1r_RUNFSUlsPH9BkRIhoqNp4hZyQ6R7uoUyg9o9Tya69Gs2kQBPq31T5ut_OnSR98BdIE6ImqvIRu6AbF5BQkKYccNezVDeOWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYzZLCEcWjvnYZgQG-UHYkZDUr6dMJb-AGpEJLHtJqxp8A6Zuf0Y7RAlyIPPy8F3GKr3V82R0mngjJyYtq9ipO-Rkc0kGjtnDilHdQo-Kv_CkfVRLliWRpdhVx51LslNdkeNTKplE0atrOhG7djOd4uT1mJ9ZtyHdYmaofvpnY8GsROdd7mx29tilumUndjJ_l4AIX7iryPJZ89UfmfCmQF0NANdLCjw0AbiYGnQQ2_RLN0mcsgFtMtPMwGlGBNi6fwQYpDVVb-qudtnYG9iDBIAeCI7d37UhebA2pgFYCabC-kaC1U0tX-jJ_6tnmTuwRcxaf_A8SDXU9Ho2l82mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtgY7iC_azgQU8dVw-fFzn1QMIVxpnU8_g2LK3DM-65T8JMze7jTX_ToaM0VMbsVdUffSqbf0ORPJydfKwj_cS_kGtAxloyvHE36eX7Iy8NFYrxO0cyuWW8Kb4TQJfAUqLQzMPcy2XXm7kTiL7ctqmbwz5es_HGvd0Yikjd0d-oBDgnfGg_UfpeyaQMUV1rxSo0xrvfsrixIAygdFIxPOHVC7TZOb9z5p28umQinSYV_gbaA_Ga-r4ztXeBOozqz0a0T7mlNWFn2vsumqdQYUvopKTp_jsJNL9Pu_844TMeyqhLAO7V9TkbaQYLE4BWw46XfTr5qM9ochA72Dum2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK-qN7JZgEGeFX8wZ9Cf3DmDwa-WeoBMGwYB_HklBsUUn0mSgzY6I3fKgmfVvsHYEc32uuLU3cdG1w1DQOSE7-nMMfmDDUzbZo4nI1iHhTYuGpEDGc0l85BFpvqxB_joKyn2SW3N_A3fagNYxml-uiLNHWUw6GWHCcFOn54jbv-jjMrB2TQYCeBgDUrUZG9UzWvsbrWUrPamhWk6OyoqzLkt8sAwmdNR_yXbt82gcBsW-PHiNgNRRJlY89D7Bg6AyoOAaCk_ikNYQkvC0KJD5KIKgsgZB9-jD25H863d0dHE4cld_0KhwvUNYyvO-es1VWJUaesYfGqecKqIcbpDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvNAGFaSnQlIXmaB_VhKtrYdFGkVbYSctif499by37wW5YoronoWzAIrtPLXTN_Eq_7NEndkuPLlBPtPsjbRRBZkQQm2mub2f8Aphv8H4QIuDzOLYRo2zQB_2OqY6ZOk-ZyVUKSRs9AIC3yzDU-8uPdNsUqSn3bT9joCxp-CSgF9pUVFGggAHrqv1dQGdW1Xv7Sq0HA58MUuQGWSEarUP9OZY4BXJeBpQmG5d_MB44PvjzbsDlp9vVePIXRRWsyoqm1nGC-DGA5Gsf4a0e2K8-5Vno8fP4anay7z5MaWfPwKJhIWsJjaeqqcOsFmSFhWwon2BJCkcg7NC-McFKSXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=tKAwIUBI_woEaQtvTceAnZRnxNj63YEO3cU417QPETPPBqxmaWw88TjMexEgzNoBO4AHxthxPBc1pwdjzn-3HTQIR8z5ugIVE1xY-UOVG1659D_wRDq1YXVc3JS1DRk-lWdcjMuvVuBP49vC5RuqBpFSMwSCcMDgOVIdPEIFLPAIa_Rfe_tqnAD-Mli90vdLE6TcZceUNdUZfyhIJi1nlJeddquGO4LELWR2jUoamWqf4pzVvqizX3X6a_bVnEqGampuZE7nzk1EOXvssMd1fLXGqeEzjguiayYYeWJq-zf3N1TYCTOkfT7NJcS5vPg3tV2NfTR9mj0apkwCL75Sag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=tKAwIUBI_woEaQtvTceAnZRnxNj63YEO3cU417QPETPPBqxmaWw88TjMexEgzNoBO4AHxthxPBc1pwdjzn-3HTQIR8z5ugIVE1xY-UOVG1659D_wRDq1YXVc3JS1DRk-lWdcjMuvVuBP49vC5RuqBpFSMwSCcMDgOVIdPEIFLPAIa_Rfe_tqnAD-Mli90vdLE6TcZceUNdUZfyhIJi1nlJeddquGO4LELWR2jUoamWqf4pzVvqizX3X6a_bVnEqGampuZE7nzk1EOXvssMd1fLXGqeEzjguiayYYeWJq-zf3N1TYCTOkfT7NJcS5vPg3tV2NfTR9mj0apkwCL75Sag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfDrohpmZ0Xq7P76WDihJzttlQSWts1kY7IeLMk3mpYKx7dEtJp2tg9KpaU6iTIuERr7GFb5TRbB8Nar2d3uXFvbEivjKPZVO1rMG7d4jrlqRa6XOmg8KUdmrqtumYiSokK4FEkHseEvBDsiYFvL5dp3AkH7CbJCAvDQbCe_YLe96mCCssIhvFifGdvHl90c8uHbCMhAGFHjw3exgecRZURLEXu04ptGW8yxYKnWvRfS7YU5mZSSJJa93fG7F5pXh15KdONChJP_r9IKcQ36FEqk6v4OtNElGLkVzG2BLkt7AnhmjjgJyfQtwqhcr6CPFsgTd7dpcFbFUy8NyLO3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abtZHbwlOYZZpiCP3CshkJ43E8QmcuYhw2bcIhDLa0-wBl9M-PiO9F_DpR8pdc9W4DifQBmM9prn86qZnH6kzcogOqT5XwlIaVGNE6DfibiNLVmlrGKlFWErEWO16rDdgPRJ80XdNUEOGB0b2hMJPcukYHC-8KC6JSc3sI_sMTnb9OervlPZU5cVNke2tUhqYszyCYyZDBztagzqy_PX9-ijrhVnji4-FkTTMzWP36D5-DGQSxQ95URtIa4fjgnX5xk_fdn6Zvv1YIFTmxexJcj0FmH1OaMtHxm4TO3N4KTfSQFceOGvI-sNaTTYF9vNUhnhmx-uT8T5XqKSb45z5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
