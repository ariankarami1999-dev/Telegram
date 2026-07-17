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
<img src="https://cdn4.telesco.pe/file/a2To2rU4OGHu5F6psTQpCCJB3kR6F_d95r6UGIGyyOUj7tZooyO9L6A_THi6SsNirkOQKny-dssVH85FGyZDJusGL3rMlMNdvWT6t6VvU6fXalziRvILgwWlEKscEIdrDk3-nPtakxIkwduXXtfuvr_KuNfGMe7CmbrLZlksOWx1lysnddaMalrf5_6J8NFpYzxWtb1Mlig0wqtj8GKXYTQaM7xPbP0G_4BMn7e25J9aE0QIk2R_S938MJJPmIPehrytzU5aXHXufXYtOlAanVjkOFyQkcknNZ5qByTTHaFShSWkOpFeI-8czzsKjJ-j3arn3vctNLEz5eEBYskVxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 12:02:17</div>
<hr>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdWJgw0PLVMOxf50UHNevQWUOdCA1CdoPX_0z9iz-k6WtSxMwBr-aofRD7f9ll804XH6DaZJ1ELPMlMpuhOQnPKs8JyErM6SWhuaCnSujCteOBMVuvkNkNqsxjOXPXySGGOdgs5Wed63LZG86_J18AVtM37nK8R9JL2eln5jndKb_Z2F0Mk6GRCcGBIBmjQI3MHl6PmdvkwKaEc1wqoPtN2NrIi7CnCROH_ihPKlNdTdlLFiPa-EfnTyD2FmHRdh3vsEarEd2154QrYQ6vziE-pVQ7MiObpIamq4JpHZvvkfnLFujZqg-RUS6KcumrSZuy2CxkqlN2y7LDvTImj9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=KeLG4nrvOcrqw-ecUqQOZjSOFgxI5lJUni0cj1I4CP_UmpVt6El2b4Vn5tlOU31g3IOrk0-Z1D97UPEpNklg-SHmFK6ffKyH6yeZikVerP727AvhcXT3H_Rzrhjt3aDOJrWQrXOUU_uTABlVCDUTfmU0WZ16YoDv5GwjB403ZpdvA4qBKYr0CHXbb4AOkeiDt7W10XBJtYLrlq6yKpnplbDPed3A25hY_4wtEZLLCvATOsZTMHJ1mw9I4bBu3Al9cDGz8CbHpWsyJ1-L6Lt_S9mxwk8NRLezuwltOpeIopju7RKYAx7qGxJmxvKsH1BLnygm4M_Z-f7KMSIpnJehi4EroRuWm019d0RI5KVYJ8zkTnauORUvWhE3jsZt6U3dag6wVozCG1SkHLbOwVvktRSWMZQ1CtEcwA2qQfVOuenpO0VNN3iOT2NIiWwA2k88zywPdaOew_zzPpxfx4xWQt3ZeQ35Y2TlX03zqu2uh3bRU86xKa5mRW7o2i8VuUamuXIucXM5u252JvoVGB9WupXSWZsTf1Vhtj9NfVwygQ0lw-O1GSp9L5Za6be25TK00b9gdIblzB_LWSysxnagzjyI0e2_WNsWxWyIInOl03JXnCbJOpZvh1H1xREiUia1rkNRscZmbSLcQRiYbVl_B9RdGspN1nLKsC8VCBLIlu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=KeLG4nrvOcrqw-ecUqQOZjSOFgxI5lJUni0cj1I4CP_UmpVt6El2b4Vn5tlOU31g3IOrk0-Z1D97UPEpNklg-SHmFK6ffKyH6yeZikVerP727AvhcXT3H_Rzrhjt3aDOJrWQrXOUU_uTABlVCDUTfmU0WZ16YoDv5GwjB403ZpdvA4qBKYr0CHXbb4AOkeiDt7W10XBJtYLrlq6yKpnplbDPed3A25hY_4wtEZLLCvATOsZTMHJ1mw9I4bBu3Al9cDGz8CbHpWsyJ1-L6Lt_S9mxwk8NRLezuwltOpeIopju7RKYAx7qGxJmxvKsH1BLnygm4M_Z-f7KMSIpnJehi4EroRuWm019d0RI5KVYJ8zkTnauORUvWhE3jsZt6U3dag6wVozCG1SkHLbOwVvktRSWMZQ1CtEcwA2qQfVOuenpO0VNN3iOT2NIiWwA2k88zywPdaOew_zzPpxfx4xWQt3ZeQ35Y2TlX03zqu2uh3bRU86xKa5mRW7o2i8VuUamuXIucXM5u252JvoVGB9WupXSWZsTf1Vhtj9NfVwygQ0lw-O1GSp9L5Za6be25TK00b9gdIblzB_LWSysxnagzjyI0e2_WNsWxWyIInOl03JXnCbJOpZvh1H1xREiUia1rkNRscZmbSLcQRiYbVl_B9RdGspN1nLKsC8VCBLIlu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0U_EV03l6hN6fSBEloHRSMdXvt-AQDCrioxAxL4daN53gLeS-G7IFuIYwMoYav9-xYxxZ8R0sedGTqwv0UFQF70JII-VgEczb2WO78y2luNQF-gXaJlpsJKT-EgQzhHLg64ATmrbTb6ZjTAB0f0nqgiJWFliHaxon2Q1WooQ0fuXxqZawswNYwktM-TNXowcq8t4w8WABfe7V76bob581Kp0Ptut1kVh4zljFIQS_YZJngZ4mg1vEJGmiU3FKnnzM5LesiOR6Y3EIhmBll4IwvzqweOgWXWBDEyXHXJJYDCN2wJGCZFh6OAJV9Vgy1rhuXzEf9JkeG3xHRRYhMk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYCu8XrF-1WqfnO07o-fr9OaKRkYH1w8FqQMzfE9ZZDlMdXe3zyxME8VlPcIdomEPmFYv6E6wgnaYe7qNwZ1AyBqGhZuogz80itTU6NtXBkS0y3gAjYL9gwZ55u7zFKCD9SOlrEVg1hYxeeZexZNr89hUAV9Ifaeqa2MaFh0Q6F_h8Cp-J3H_r2I_g6ZwkFRUt1kWI6L1SKqFJAv_IbJMHdEt9vwTzRYkyv6bY55NmmA_mcih6bOVpyK58g9LTH4SEY_vNrImKx_28PZV2h7RRdQsvVwPblwpLzBdEeugkG3pRXNeHeyQ1oHW1hZBvzV8IVIABR6U_YGDiHuKssflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=tfnr8iEAbRWO9GfT1g7y8Rs-07Suzc8Vs2HzBlf-976hUKdkcpDQfiBxlwTlt3a-NiNBfNIz6ATLAM5jWm8JaesTXoScKuEtD6TVIPhW_GjZcNfcbJ6Xn-xPhoZ99dms1cEyF7WTyYPOw925smhbVg5bw40eqNbG28u_0vw65O2JX-9g-apoCKn4KBGLmnIgOFDWqMqFwXQjMK3fB58zm4ydRkrPYmzwp-07_7jCdNBTmaaRfhHtMS6gMjqTm3Y1jrRCIcWs_mfyo1y6gmAScqlQ6En5qXyVHcvHipc06Lyo09lqc8R9VA6UyqOd0XzbFY5wmkeN9uG_EeYjcIqryQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=tfnr8iEAbRWO9GfT1g7y8Rs-07Suzc8Vs2HzBlf-976hUKdkcpDQfiBxlwTlt3a-NiNBfNIz6ATLAM5jWm8JaesTXoScKuEtD6TVIPhW_GjZcNfcbJ6Xn-xPhoZ99dms1cEyF7WTyYPOw925smhbVg5bw40eqNbG28u_0vw65O2JX-9g-apoCKn4KBGLmnIgOFDWqMqFwXQjMK3fB58zm4ydRkrPYmzwp-07_7jCdNBTmaaRfhHtMS6gMjqTm3Y1jrRCIcWs_mfyo1y6gmAScqlQ6En5qXyVHcvHipc06Lyo09lqc8R9VA6UyqOd0XzbFY5wmkeN9uG_EeYjcIqryQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocUvZInmXSgxOFR_PkkilUcR6lyDAdV74ZT8NWKgyv1oIgBPLnO_rDXZkuKDAxp4IFbybmmZj22RdK5ILR-kfn97u2bAGkbDZ1RcjdrjgVsMu4mb1eC9Y8_sctIdIhKeDUJdBiEV26gvb0eGq0E5VM1a8jE05TFg-zm4bhFH8F0VtD_fvtQVEZa0A6Fwx0KH8QkXtpbheu3-bZtskLP8O4SJnqgJfZH27xXhOFIDd9YtOCpNHfuEw8cE9J9c5qnFjpAF8S_Iu-HB7VRQoZPQ_0fV_Hx6PpXSTEhGZTnFMcWWRNWNizB18L5VMJ86wZqPPRfOlenrWrUI3w0mESdJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=NQ6Qiy1Bhdewspuscq4b1vDu1heNLjed5DCLGlv3RmIBk2BVoIizo_g-g39BtMKOzzGXSwMk37BdN-5JrtXxfC8XjUtp0pnDvC5ZQXxJLUoZKu7j6wlr3cUld672B_QpUZ_RAx9hc4sKK3e51j_el4RUPuA0oOD7U0rMyge6NhMzcXoKdAhmnKNuOs1jMboMtomQ-rPE09opj6dXBgbmpyeqC3bKxplCvqa_HLf2g_PniT3UUmw4sxWN_flEZhtZCT3XijMDwn9ASn1ke6aKp-VHmpLeWqs0CaWgr_laWxi5DIhEZ7PUdyzosuFCVE9ptP3tRlZSa0H51oMTWaMahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=NQ6Qiy1Bhdewspuscq4b1vDu1heNLjed5DCLGlv3RmIBk2BVoIizo_g-g39BtMKOzzGXSwMk37BdN-5JrtXxfC8XjUtp0pnDvC5ZQXxJLUoZKu7j6wlr3cUld672B_QpUZ_RAx9hc4sKK3e51j_el4RUPuA0oOD7U0rMyge6NhMzcXoKdAhmnKNuOs1jMboMtomQ-rPE09opj6dXBgbmpyeqC3bKxplCvqa_HLf2g_PniT3UUmw4sxWN_flEZhtZCT3XijMDwn9ASn1ke6aKp-VHmpLeWqs0CaWgr_laWxi5DIhEZ7PUdyzosuFCVE9ptP3tRlZSa0H51oMTWaMahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=lXXlwF25D4vSFSxBkC4LuszImi6PbkkRp_acZbSUSbROnMXQ8NmzZVcc5kc_l2f8GszCBG6LDLj3AU06zbae1o3xxCniTQ59Wnz-s4mRZVg8xyBtwAVhIxzKt0LZ7NcgFfbv2c56J_NEkqHT9akcucR_9P8AZG2hde3i4rNONn2Bce9mKXUIMsALQmjwmCofff0mo9nwORImES4xvHGKf5pCDbkmi7A-PvEWZp3A8z2QJEky2ttPEnl-BrGCXX5TEClwJkWQUmaRCbVDS0Ii8WqQiv-1bMDvwdazh34etFigWMg_gLBknuweeCHdmHVTp90COwFD7g8y8MiUQXttgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=lXXlwF25D4vSFSxBkC4LuszImi6PbkkRp_acZbSUSbROnMXQ8NmzZVcc5kc_l2f8GszCBG6LDLj3AU06zbae1o3xxCniTQ59Wnz-s4mRZVg8xyBtwAVhIxzKt0LZ7NcgFfbv2c56J_NEkqHT9akcucR_9P8AZG2hde3i4rNONn2Bce9mKXUIMsALQmjwmCofff0mo9nwORImES4xvHGKf5pCDbkmi7A-PvEWZp3A8z2QJEky2ttPEnl-BrGCXX5TEClwJkWQUmaRCbVDS0Ii8WqQiv-1bMDvwdazh34etFigWMg_gLBknuweeCHdmHVTp90COwFD7g8y8MiUQXttgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiBKy1Q0TRHANsufzTEmKh4ZQa3pEDqfIFZyvbxEq0R3NyTBzs-d-Q5WzXvQGrQTItR_DqfAim_bZcYdmjf02eiwzgii3o9t46E3RCPOIxos5XCCFoL6akBZEdhjhD4eJNB5dNVl3wWPNhLTcl9TCFb-Aa9XOKffh2mAWFm9ax3U-9HsQMFH4bCLz_KOaSN0vW5WeXcMdPGG2xgbJEEZJMux8aGViewbLb8Lh6KDZR1gg10qlteBFTzGYociTA1kRK7KX3qE_EEQrv-G8HzR4-_UU1eVD0ezojSm6v0cJCRjshAi3QfsTyeqUIDJ79zq9q1i3ceL5xlKbjkhCSC7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-7JLKpHkTIKODdtZIfbZf-G4Zr5lfKvMhzQCx3kA9C5g9IdxEnJu7nLM6ZBIqeFmPLkn4JnD2oluQaEB4J6w8aOJMGazbMjoQTJi9r9jo1kwVprCB8D0Cpdc-7Xo8sx_fbJaHRStGUHOY9PdhevBiX4MoH7fKy57ajaRVMXl6-r-v8bHsaUw1dyevWJAi6R9kSQbND6nILx0SErWDV-4pplhym0KwLwdpXuPtOtDgoG-FT6gvQVwwEenNR510x5TPHAwH2g0ejdMvAcnokTM6D-zpMTkdHZG0EkqiWj2lbEXzj3vJIIO6ShVpPxgm4hcKTCsUmTM8bcDkgt_toO5NR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-7JLKpHkTIKODdtZIfbZf-G4Zr5lfKvMhzQCx3kA9C5g9IdxEnJu7nLM6ZBIqeFmPLkn4JnD2oluQaEB4J6w8aOJMGazbMjoQTJi9r9jo1kwVprCB8D0Cpdc-7Xo8sx_fbJaHRStGUHOY9PdhevBiX4MoH7fKy57ajaRVMXl6-r-v8bHsaUw1dyevWJAi6R9kSQbND6nILx0SErWDV-4pplhym0KwLwdpXuPtOtDgoG-FT6gvQVwwEenNR510x5TPHAwH2g0ejdMvAcnokTM6D-zpMTkdHZG0EkqiWj2lbEXzj3vJIIO6ShVpPxgm4hcKTCsUmTM8bcDkgt_toO5NR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=OSC2d6TMY9bVnsYVoHTWa-X9an6-EHfvx6CiEO1e2VQPnteGyXm3lE0Fq_n49CvFbpSG5Zq_7Wds7iZ34aW1A50U7Kpvc2PzNcxPuVQ-VJ8J0juVQLj1yogKjgdayA_Nrs6Z_CWBfKGrQLaT9gFiWAq--m4zyIb1H96GfYvHRbF2eTzqvUj7D0t4V-MuTQpu-5b9lS626yEM1oDkq9sGYZJlrGh6JjlWQ7UCAQaENw4GK_FHK5zh3XuBJ5XiFTrcLWRB-I06rSz5sSl0rf6hL2s_WwR2a5EVxsubYaDV9JOEvlehFqxHORlDfU0IQStqgKHMAEsmxm0iImocFCS3Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=OSC2d6TMY9bVnsYVoHTWa-X9an6-EHfvx6CiEO1e2VQPnteGyXm3lE0Fq_n49CvFbpSG5Zq_7Wds7iZ34aW1A50U7Kpvc2PzNcxPuVQ-VJ8J0juVQLj1yogKjgdayA_Nrs6Z_CWBfKGrQLaT9gFiWAq--m4zyIb1H96GfYvHRbF2eTzqvUj7D0t4V-MuTQpu-5b9lS626yEM1oDkq9sGYZJlrGh6JjlWQ7UCAQaENw4GK_FHK5zh3XuBJ5XiFTrcLWRB-I06rSz5sSl0rf6hL2s_WwR2a5EVxsubYaDV9JOEvlehFqxHORlDfU0IQStqgKHMAEsmxm0iImocFCS3Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=NKK1Xe3lAdnamy8oGjt7Af4xYh-a2Oj9jDiXQbMSoM_4wMA6jhTxCqJhzeuDqdUq55-rQ4xAbb3-rNIGr6dzxvCIdxNuigjF30xv1d6h1oAp5lyAKefSHb2HHplAkbP7cA6IHpr6TEQdR7NNREw13KpjGWiJkdUDsqMmZ80mso7Y0n4SW6NNSTC0K3beVJWAkFIG_QyPJkhMn1VJiT0Nc_6YSM7cDTfchhFSPXyZYX4UtGtlj5r0_KnsSAOPRAR4rh_PaZU5CN9o-K0Ys1y-L_oR9YzOTKgBnjVZB4X5zlaHHAIHAuxd57L2ntv53JtdaGlCEpyS-HPG-V_FYrKpvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=NKK1Xe3lAdnamy8oGjt7Af4xYh-a2Oj9jDiXQbMSoM_4wMA6jhTxCqJhzeuDqdUq55-rQ4xAbb3-rNIGr6dzxvCIdxNuigjF30xv1d6h1oAp5lyAKefSHb2HHplAkbP7cA6IHpr6TEQdR7NNREw13KpjGWiJkdUDsqMmZ80mso7Y0n4SW6NNSTC0K3beVJWAkFIG_QyPJkhMn1VJiT0Nc_6YSM7cDTfchhFSPXyZYX4UtGtlj5r0_KnsSAOPRAR4rh_PaZU5CN9o-K0Ys1y-L_oR9YzOTKgBnjVZB4X5zlaHHAIHAuxd57L2ntv53JtdaGlCEpyS-HPG-V_FYrKpvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZoqXA0AsNtcLHYROAmpbsFTJ5M2ZCgqCah9YlaZr0Na8bUah0IugagHlU2X1kA721iscpz-VQ9ZCQ5QT3B-QBXfBQSp74hASe8lt060nb1CXdpNWye0C6GF-cwQSXt99GcW8NCjKS0zziAFJ5nya73Nwxm9oaTwLqKOK-fNRKEk76TwQnWsRR7cAyVYJV_ScAf1vHfCrHl1EYV3vZELqNlFKuxcYGAiULfABHtn8qkSRs3ZFA6Dg8uhQhg_VeCqHrKcyHKi09EwyFsxwuua-hpwDIeE7OVnTWFBk14cfVhBV3vsikOnJfLi5ZZCbp88us-RW1y5R0TTaxnyNS06uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=Vmaxi51IxZXwfGWqjrEfRF6m36RiYJVpdMi398VqdLfQDqm0y0t-B2en7clDUyejlKisdclp9R93WGcL-viRXvpdpb3sHoAj6OGzh0FeVtUWoedqDnqB6o-zKPOZUZP2qj4c9CL0FGIVse82PhD1eOo2-pqQrlYynoyKKUPVSl4Z4sJO8s3ybKgJirfqjgaSQdPcmxmnOOnOY3He_H3_9Q0DPMi_qMjeZlU40GIkhQLpEpyLHOFbARf7BbVf9b1ZS6r8fckZt9WGZSZwL39rw9kdYc993baDh8L-i4UzvFq2IP-RLCaLNHUgodgQ-3JelEYFKPx5F8MPduCGIMasMmmgNJAarMuWZNuxyPkRwByIcmnSIS1cbNVTMvWNVLrinuROuAoS-UVAIej__gnY01dq2c9D69IF5oUPLjnR6lG8iGoc9JKyQy00OHT56-zVo0Oh3QFbaxukVLvtCBwd3RqBDdLlSmpzgwiwcFpMLedNycnUlwQdynHj6Kx3tFqLLhK4GoM1EHjPqNPweY1LRIPeH8q7KPfJFFir08jsLkvTcAIt2sib6qYtGK7shUGzDvWsSytz5vOXxJqHumi8Aqcx-5FWtKCjqOHJXm6LVjCC3vV_PzCpvpTAGAnrq3HzH6nyngVyac8065D0-tszANVUV6wExj0s6Bem418hJsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=Vmaxi51IxZXwfGWqjrEfRF6m36RiYJVpdMi398VqdLfQDqm0y0t-B2en7clDUyejlKisdclp9R93WGcL-viRXvpdpb3sHoAj6OGzh0FeVtUWoedqDnqB6o-zKPOZUZP2qj4c9CL0FGIVse82PhD1eOo2-pqQrlYynoyKKUPVSl4Z4sJO8s3ybKgJirfqjgaSQdPcmxmnOOnOY3He_H3_9Q0DPMi_qMjeZlU40GIkhQLpEpyLHOFbARf7BbVf9b1ZS6r8fckZt9WGZSZwL39rw9kdYc993baDh8L-i4UzvFq2IP-RLCaLNHUgodgQ-3JelEYFKPx5F8MPduCGIMasMmmgNJAarMuWZNuxyPkRwByIcmnSIS1cbNVTMvWNVLrinuROuAoS-UVAIej__gnY01dq2c9D69IF5oUPLjnR6lG8iGoc9JKyQy00OHT56-zVo0Oh3QFbaxukVLvtCBwd3RqBDdLlSmpzgwiwcFpMLedNycnUlwQdynHj6Kx3tFqLLhK4GoM1EHjPqNPweY1LRIPeH8q7KPfJFFir08jsLkvTcAIt2sib6qYtGK7shUGzDvWsSytz5vOXxJqHumi8Aqcx-5FWtKCjqOHJXm6LVjCC3vV_PzCpvpTAGAnrq3HzH6nyngVyac8065D0-tszANVUV6wExj0s6Bem418hJsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3q3XE8AlrompvY_hYgaNv2B70r5ue6QI_1BPb9ADSGWtyA0tnBex5BsfUNLzgVi_ztE4Mr6UomiuAiys0_Bzw2DqdMO1k1OU7a6NC3hvG6pgXCc3BecRL6uSEji8LfcSmrkv44K8-hpqjXmPpIJARplnlNFA_MpAMoeohpiYvsWvbavrF3yHZHj8CEj61Hh-LzjEbdJIrotlOcb-39NhaeydWPagAUi046SJr6o03Q7IgTN0rtMIkUVfoWwb2bX96soVi7VzOAveXsEEt_hFLGaXl_XWYP27l8LWV1SFuqRk1XwPKmZnPKNnDoPcwCJ0Bzl34Zk2GKMvrmUd_uKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=IvX6LVgLWvqFAwdaSjOSrE2Y7csFP2IqW_9RP5HRlZ-D-VEnC2TaMuFhrfYaBFgoocqIA188KWNI7QBdqdPAvAw9Dj3c6SxXXV74cx5ASwiN8wUTCIZvd-jN5fAqY-ihuB5X3SpL9KbZ2fBELOI-X5GhkM6ywevDcTyWFxKweu2W_76V9--ztO0lCF9qpuCJYbZAwh5RAYyDYpl2Vs2-oTlAG6brEpVSDZn7XmZiE9BUDCzYEKnrq_b-6L-TLUxUNwRR-rvU8Sw0ZKhfW5naBjoED9UtB9swVsNRCtZYnbzCx421VOjdXrv4uD1qoE8NFRTX6lgHGdye3y3IoqDFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=IvX6LVgLWvqFAwdaSjOSrE2Y7csFP2IqW_9RP5HRlZ-D-VEnC2TaMuFhrfYaBFgoocqIA188KWNI7QBdqdPAvAw9Dj3c6SxXXV74cx5ASwiN8wUTCIZvd-jN5fAqY-ihuB5X3SpL9KbZ2fBELOI-X5GhkM6ywevDcTyWFxKweu2W_76V9--ztO0lCF9qpuCJYbZAwh5RAYyDYpl2Vs2-oTlAG6brEpVSDZn7XmZiE9BUDCzYEKnrq_b-6L-TLUxUNwRR-rvU8Sw0ZKhfW5naBjoED9UtB9swVsNRCtZYnbzCx421VOjdXrv4uD1qoE8NFRTX6lgHGdye3y3IoqDFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIVzq1mc17G6coC6wgW6X2-yf-tZ4Pe4mLuF7QOyFN0rLy230Y6uHJbV5Uplxa1Yj-hofHOz-_H5Rx9Ss0ZSp_t2-ypXJvw4bE87XC0Bmp96L2fMLrU-xftvxExW9kCgmqi0vi6RPn-0szTscsDa94vxKUMRAG4iMGmj32Rn9-1bZO5pYDX8uC7t68BFGI2LqOLtxhgn2UwDDuHcdPLmak9FpQUDt3AFuNTGDvhSjVhvBjm49ZnjD3v7jElzemS_rSGcnMHLhauLFiSTt6Woi8nPuRLkiLLCuhvW6GF2v-IeM7xxHAgsOEdQM4BAGy0ASv0NIb-TwS-dPDVbV6S7-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXUkRFveijuExYDT-F44dpCj1c7iEALqZUHTxX_TB-kf8Wies39wNuYaosZS765di6SlOEoFboYntKdnF_bSi4bgopC8f-h9x4v5PhZe6HeFdAVxeJ5ZKJA1eCOF45pt_YpiDAIZRxPBnvEaTKCM2MFgh09HrELcJ4pgaTq-lHdNw56-U5JZsLb0c52Cj8400sGXsMLTjjMyg43iGwBbnZg29CmWymbYcJElQPgnqwe1VY0Ix11MXAh9CgkKLxcIBD20OTjkE6F6h_giBJW8cep2aRxO_3DvMF214NwIChcmNnHynhcrFnjL8oakMopoxMGWDc-bxbs7d1mZBFfQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GH-BVbrYK71sAnfdnNEtguf3ngvi2W9hmKHUa6H6870sNOwhJRWuIENYYtkhUJ7IfcYP2OJc6gh2WJv4OFUjxvqAtVfH5xcYq0Ok1uNgEG-eZ2LDj564oLTbOUYuZgD4qBnAiLxDvnW0BIlByD6N38n00RlSibjpAohaOWke58fkGywd2mjHa8t6A7xp59SGh0Kia4slo1km2usBuC4FRo2-5ifGEsscd9kIlsAMpkNlpCTowsfSciCWlt7iRFrTW2KEkGghYhjAFyTHekaf1aNBTL-gYqOHFTB1iELeVVMvSCZDvwrO7xyIJp3oq-8dLb7mhtzfrvICIC5R5oBCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=cdd4A_MSWPDa8rrDkx9yfRGO3wEecF-QppF8ZNUzE9tMb2qfaEZlLwKecQCFSLQqVtfR36wmI1sgY6GEZ8P-Vufi1z8dTjt40Pf-8wy5ll6woscO913FpjC5qhCMDNnEyfRg_ulScJ2_ylrszmrpLCzAuS8TTHbuxB_FaTHYf6gvle1Pzi5WHJ1QmJjBjp2zu1SB7aBvcXGwBWNbpb7h7uyea3-FQeZBLCaRNjlPTFVFvKF_QVLbcBgb7U5sLiNRfBV-nsLgleNHcyTdniz1ioLgjZpOp-B3tOQ1EqEA-GjghMYlVfExYsBOcNJfZAbYeAa7vX7kxVgbzvV0lGxyhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=cdd4A_MSWPDa8rrDkx9yfRGO3wEecF-QppF8ZNUzE9tMb2qfaEZlLwKecQCFSLQqVtfR36wmI1sgY6GEZ8P-Vufi1z8dTjt40Pf-8wy5ll6woscO913FpjC5qhCMDNnEyfRg_ulScJ2_ylrszmrpLCzAuS8TTHbuxB_FaTHYf6gvle1Pzi5WHJ1QmJjBjp2zu1SB7aBvcXGwBWNbpb7h7uyea3-FQeZBLCaRNjlPTFVFvKF_QVLbcBgb7U5sLiNRfBV-nsLgleNHcyTdniz1ioLgjZpOp-B3tOQ1EqEA-GjghMYlVfExYsBOcNJfZAbYeAa7vX7kxVgbzvV0lGxyhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=iZAcRGEXMeurgVK9kOUHSW1RqnLMbpLXxRReDW6nXsiChaxSXPZhRJ3NZhqLKydOAesLGvFWqbML1lE_GulXrotOszIbEd0XmkiTARb_pH9Yci3ulGnkW_nLtKwG0lTQTMJBxjLLT3umY8ic2Dlm4sieT6EnwiI02A8KWSymkwtG55Jy2FQnfoHNOIRqbtXYG3o5QP7iUCYxwuT34T8NJjRixqdD7TxtnOutPvNWNnWRFv-x8y2i0sTt5PcfaptKIzJnvrBfJGbxBvpIV0G6MvvJAdA3dg2TvqCXNhpZP_aCejLT3xDxRfTF_03vG0UjvwCHDrh8JlwZFdVqKBJwqoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=iZAcRGEXMeurgVK9kOUHSW1RqnLMbpLXxRReDW6nXsiChaxSXPZhRJ3NZhqLKydOAesLGvFWqbML1lE_GulXrotOszIbEd0XmkiTARb_pH9Yci3ulGnkW_nLtKwG0lTQTMJBxjLLT3umY8ic2Dlm4sieT6EnwiI02A8KWSymkwtG55Jy2FQnfoHNOIRqbtXYG3o5QP7iUCYxwuT34T8NJjRixqdD7TxtnOutPvNWNnWRFv-x8y2i0sTt5PcfaptKIzJnvrBfJGbxBvpIV0G6MvvJAdA3dg2TvqCXNhpZP_aCejLT3xDxRfTF_03vG0UjvwCHDrh8JlwZFdVqKBJwqoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upEr0F_uqlNNwsAilMdP57J_lHbV5pboWN8EW87P8bdmaLkEpOucMoPKWhfu9SJFc6UsXkPLvpB5CekEcRwfHiYnBDxkBx-rQGuPnCtiXY61Xv-yWbp-8fb6LYHagk8BIhTPLkZAn4jUQYKSTlvX3FChYzv-IbiWD_Nle3fBvcHonssT1EQPwJKxuJ6CHttVqv0ZaDju-hH50jRg5wV7UIHpWl4Yx0xIfw7d6COEkYnVirlUop9XkTfWCKSNHFzH9m7cRPyd-ttdZyDl6NqA7TM_osWogUDkgRb5O_Hg5CQzq3CEPwj8wDOc-hkZcju7sseYTOgJZag8ePrPayLsnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAbTYAYONG6VEkEN7xvX3IMlEyNqVrwmArfgEB244jfkBo0MUcqpV2j4ZpJpJ2CRZJJRK987QLgGSMGo7zCKhd-OZ2alYMLSzel5pt-C9LBsqTCpeWzyV1A5LfF6pkycK310aYYxtwjd6zaSMdR-5jZMI_n5dWyri2UjLh7OR9IvoKDoxHCSUfs6MpcEwvGS1Zrzq-yZ80-wPI12DWZ_9sMKz22siEksi57h2iekucCwO5z5akM4cjW-qVDwHnXVet6WuUU1MeKsblNSth7okwSkiDcIy4wr-ru9Ei8HFcPgY_-OdrVSIdceJOFq3xazLpEKO4kWJ1T8VlOnf8MtjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=T5P0jQS7LwnCxFY_mHX6w1qEj3rWtoRIsJe90HA2Mvp4CF8mmPQzrnxbeyWud3dJK4kLYmkE1lNelvPXr72ivRbccumClttmzo6v43t9sUD07LGxLF_Y3IwntNWAv6Da1ZHd-Ox2TKPRZA3VsE26mR1ej5XSO5sDHFkSwVw7THeAwJAOTrr5UPPYiR-tHuFXociOuZrODCwkegO_XyswG4eLNTgB7IbItWdvdkGK1poCkJ1bS75zN-sZXrQPCTwr57Yw34IZ5HBsfgeJCR_Zqvb2Ygo-XUKydeUGoqv80E9PHI_cB0PSFBZS80sGipTeIXjJKMRQgE5KojrUye8OfKkZ0kCxscHm7zu1wQoa4F-MYF6kIijoNAjUYzewboUrpI2g58cFyCyMlGB3TM5zPECXZzK0-jBOnLRMfRtl6XmuBdG4df-xNHTX5We2dl_BsnZQMdI_kMnXksMi7BRPWjSpRk3dIUYk7H9AClfee71AsjJYyi6KdMMZZXJctS0Qew70U4oI__pwIWKkV0_1PeAE3L4xOXzqbMTJ36-22MtMT_VtO7SSWBIJZyO1DmLMR4qxcWRY7XvUtdf5VJnDBIgQgTQqLQqn7BTdBWKutxSGHUbi7U97kryYJqjNt8ZiQEWcrni0ZrSDHX2_bfb_1fqwn8kuNlmN7nKZvEHvgmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=T5P0jQS7LwnCxFY_mHX6w1qEj3rWtoRIsJe90HA2Mvp4CF8mmPQzrnxbeyWud3dJK4kLYmkE1lNelvPXr72ivRbccumClttmzo6v43t9sUD07LGxLF_Y3IwntNWAv6Da1ZHd-Ox2TKPRZA3VsE26mR1ej5XSO5sDHFkSwVw7THeAwJAOTrr5UPPYiR-tHuFXociOuZrODCwkegO_XyswG4eLNTgB7IbItWdvdkGK1poCkJ1bS75zN-sZXrQPCTwr57Yw34IZ5HBsfgeJCR_Zqvb2Ygo-XUKydeUGoqv80E9PHI_cB0PSFBZS80sGipTeIXjJKMRQgE5KojrUye8OfKkZ0kCxscHm7zu1wQoa4F-MYF6kIijoNAjUYzewboUrpI2g58cFyCyMlGB3TM5zPECXZzK0-jBOnLRMfRtl6XmuBdG4df-xNHTX5We2dl_BsnZQMdI_kMnXksMi7BRPWjSpRk3dIUYk7H9AClfee71AsjJYyi6KdMMZZXJctS0Qew70U4oI__pwIWKkV0_1PeAE3L4xOXzqbMTJ36-22MtMT_VtO7SSWBIJZyO1DmLMR4qxcWRY7XvUtdf5VJnDBIgQgTQqLQqn7BTdBWKutxSGHUbi7U97kryYJqjNt8ZiQEWcrni0ZrSDHX2_bfb_1fqwn8kuNlmN7nKZvEHvgmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e58WIXnmjxc5wxRKMZKl65KyMFBYslITT7and9PAJ9eE3aFi8V_WMxYVji2aSLtIjWNTtoxDTtnVv9L-ZCcuxzYXB2a25c-mFWwRpoHeIfcVXJP19a3eGK6cw3maLSPde7mABt6tCUe3QTDV7mVgFLHGvHX2RO2AdbPCjAU-tIz7rPPagwFuK5D7T3dGPkb-arWGDiVP4NdNCpP_wztwijWghXQ_0nD7nir2fI4EwqbrMcPxlydW7fWM8bnJdu5EpGUEXS04j847iIG5I-V5IqUJXdZCdjDQhxcNV9h7e3NEQkfLwlYeHzTWwlKn0Wc9gOxx3nBKfLV4f5q4p8o8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlSZnQNYQ9gbE6XBrr6zxSyHa3D_1xt0UlZIzkm3J-EKqm1k8HmiNdGsmtf8cm-Bsrh2WDIYLGSZfO7ugD1lKU6-pVm8moeiYwpcxheigqN5GJYNCibpRPlsgsC7EaNWqA0Jt2rfGsMkSxEOrE-LoLaUmspvhiwel5OugW__lDYKAn3GcmC0PjJRYUOPfZ5tet4lY7q7LG1599yp9mrbINyBDnkQPwT2FNWodNMAdfANZTwssC7Uhvqryd7sa-CXGRULpfHS24pLLMEUAI8HVOxqUvCKkHwlXV0Utx6zNePl-t3ogyOiqk_VBr2k6HOmjgwpn7IOdyVQjXqBYDrmJHDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlSZnQNYQ9gbE6XBrr6zxSyHa3D_1xt0UlZIzkm3J-EKqm1k8HmiNdGsmtf8cm-Bsrh2WDIYLGSZfO7ugD1lKU6-pVm8moeiYwpcxheigqN5GJYNCibpRPlsgsC7EaNWqA0Jt2rfGsMkSxEOrE-LoLaUmspvhiwel5OugW__lDYKAn3GcmC0PjJRYUOPfZ5tet4lY7q7LG1599yp9mrbINyBDnkQPwT2FNWodNMAdfANZTwssC7Uhvqryd7sa-CXGRULpfHS24pLLMEUAI8HVOxqUvCKkHwlXV0Utx6zNePl-t3ogyOiqk_VBr2k6HOmjgwpn7IOdyVQjXqBYDrmJHDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=az441Cpu1vtpkhYgMass9ctMCDvUTYYYzeZoaAv1c7CEjrQbAgl6Qpdt_cGafpTUtGrZDuDwE-BR2zk-fkLNZ8cy3aNCc0frk-Wjnkpyb3GBlbdsDdQmcdnRxrEs9qJ9NWC1u9bBC7G0y4IjXwTZUmjB-tuGz344JwMuDRTjL_GBt5DprKPOCg-26sz-R57Uim4nKqf2Qy1mEOPudJYHF5GUQRKDoii9SnT1NNyU-LgABsjHXl-mUo-CquTLWHbODlZHfnkhGYPbEXrT-pQIjw3EtAltOXOb4mBO7KQP-WQgWSzbLUmrU5mQle5UpB0ms-DknHqiiiiG_ZJk5ZRTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=az441Cpu1vtpkhYgMass9ctMCDvUTYYYzeZoaAv1c7CEjrQbAgl6Qpdt_cGafpTUtGrZDuDwE-BR2zk-fkLNZ8cy3aNCc0frk-Wjnkpyb3GBlbdsDdQmcdnRxrEs9qJ9NWC1u9bBC7G0y4IjXwTZUmjB-tuGz344JwMuDRTjL_GBt5DprKPOCg-26sz-R57Uim4nKqf2Qy1mEOPudJYHF5GUQRKDoii9SnT1NNyU-LgABsjHXl-mUo-CquTLWHbODlZHfnkhGYPbEXrT-pQIjw3EtAltOXOb4mBO7KQP-WQgWSzbLUmrU5mQle5UpB0ms-DknHqiiiiG_ZJk5ZRTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=HPpVIU_jMgumYweRunOKTnlUJ2_W4GvdutIq32rWGwXS6JC_SkkmRl9OqCBMDCfgemaF39dP5Cf9_16DiObNzJY071QwK-EVYXXLtN9kQPWMgBhClSKIdvENkHBlOv_0-oFmcIF9EXIH9FsklZ5zZElRcC0cQH8uh6atYR3RHXQnJXp-DIL5mUDg9KwdN5_onD1rUZERVty1jW4nm-aaN01MC2oZxJFP4KLRY62Qc7MjkuX3rfMjj__PLqaIAjno4IWUBMEwoJpsIhbQmMa9o4klj8lXui9cwWdJUWjB2hBYnXhblIL0Siavn0e_jMIrS7EjSsMGDWEgAg_w88wVmXy-sxHc33o7ojCNbz4sumU58igO8AYWXTKPUN0r7zOptzZ5Kr2YNaa2n9uHFe3_UT-2M5vfn37ndLqL1E1WzmbVkGJiJpBen_qoCpUtKjJ2hlpS8VDcKuVj5AoUeiYPoffmPDswA6anZ9llGa23GlN0jp0yyOvpBTStqumTwC-NEAfN86LoZ1MDInPsywy9VvgGncy1JahN0mWjZpa_Peft9zpgUfV3N-LYQPoROrj1h1uzDfzaGXlNHMj7W23djrfbKsj1jSRjNe7cTSG_cGclZ0LtaFdCOASSRyS3Q_ZOa9kFthtfE20JR49v2ZtxYQwC1Hy-s3k67u-8GYnsdm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=HPpVIU_jMgumYweRunOKTnlUJ2_W4GvdutIq32rWGwXS6JC_SkkmRl9OqCBMDCfgemaF39dP5Cf9_16DiObNzJY071QwK-EVYXXLtN9kQPWMgBhClSKIdvENkHBlOv_0-oFmcIF9EXIH9FsklZ5zZElRcC0cQH8uh6atYR3RHXQnJXp-DIL5mUDg9KwdN5_onD1rUZERVty1jW4nm-aaN01MC2oZxJFP4KLRY62Qc7MjkuX3rfMjj__PLqaIAjno4IWUBMEwoJpsIhbQmMa9o4klj8lXui9cwWdJUWjB2hBYnXhblIL0Siavn0e_jMIrS7EjSsMGDWEgAg_w88wVmXy-sxHc33o7ojCNbz4sumU58igO8AYWXTKPUN0r7zOptzZ5Kr2YNaa2n9uHFe3_UT-2M5vfn37ndLqL1E1WzmbVkGJiJpBen_qoCpUtKjJ2hlpS8VDcKuVj5AoUeiYPoffmPDswA6anZ9llGa23GlN0jp0yyOvpBTStqumTwC-NEAfN86LoZ1MDInPsywy9VvgGncy1JahN0mWjZpa_Peft9zpgUfV3N-LYQPoROrj1h1uzDfzaGXlNHMj7W23djrfbKsj1jSRjNe7cTSG_cGclZ0LtaFdCOASSRyS3Q_ZOa9kFthtfE20JR49v2ZtxYQwC1Hy-s3k67u-8GYnsdm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmdVRykAERfOOs-7IrKp0QMGa1gPgcXZu8S7PRPo9xToGpHsKJdc6D1m2qLBQ_3YOfzA27x9YZUs2dgtTpVGe-UY_5o1ZelRnuFI62yKLaYGhl1TlaDj9bBR6fw0PKZuGHwo3714ZrNJufrICNZVU-UARV896F_VSlFiSja6gbsTle32WAS86bf8sD3fiEJIU-ZoTSJnl4OaAiqU7gCHMw8lpX5S_4vV53Y9Ih9cZmysZcpkyPTFuVNWaU-DEr8rwWNIHGA_gaSScbaOFSY2UiCgwuYc1beiChpy5wqvfBjYI-KeFfrrsYK46pTHBfyG0pziSW8m-LyF74nOTJyR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kni_wXSdUlUBUMZhy5nTtycvSfgzaGNyM324MrzdFv07RdSws-r7vyTlzVjucQkvfqPfL1DHXNXYO2fgjTcOYXxe_U7DSUNogPtXPFjkP81wciuIvJ_334aI1yADbNBfkJtoPJsBNKbcqbhAHNe0olebTm9uGAacWId-Tl5dPZKCquctr_lah7CbzC1xSWomV-sAT4LALy3cGh9WnDIt23Ju-0F3T44VdfL2BEdN4IRvJjgqr9uDOOY8V2FQq--rGbNxbQcn8TTrpIJXfGLg64I3lCiKBGOGMiGNBHRjUQrfMiljFkd5dN3-BzFkwxfeedaEK9VMG7PQM3LBRAM16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=nZLNyR1ibn8CYdLZm1-EtJY1QrgOHXEXs88Owog8sM41K8lF66PGssAMQaP_o_I3stCAJBGttRnGHrVQRx51jLqciBFccABz-junnoK-3nVZCpx8_2HgZojvdn80fxPBdZIYVRhhznLCggzLOuksCPWIGndo6UKrbSHNVzcQV-zB5qZyLfNq7ZdQ9S16LQstKyzhAmh9PKdYLhAVU2fDLeMPYn3dvOGqC0evHCI1UDEo7CvG967n5c3JNDrcVlLP1bsweqAkSVUhQayWKA7oTa_aibezU8YuGcX4JSXyrt7M-s8c3JmVgjcLJoXe8RM54HFDnHBmruBY4qb_3bEQDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=nZLNyR1ibn8CYdLZm1-EtJY1QrgOHXEXs88Owog8sM41K8lF66PGssAMQaP_o_I3stCAJBGttRnGHrVQRx51jLqciBFccABz-junnoK-3nVZCpx8_2HgZojvdn80fxPBdZIYVRhhznLCggzLOuksCPWIGndo6UKrbSHNVzcQV-zB5qZyLfNq7ZdQ9S16LQstKyzhAmh9PKdYLhAVU2fDLeMPYn3dvOGqC0evHCI1UDEo7CvG967n5c3JNDrcVlLP1bsweqAkSVUhQayWKA7oTa_aibezU8YuGcX4JSXyrt7M-s8c3JmVgjcLJoXe8RM54HFDnHBmruBY4qb_3bEQDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=hlizASx7DqLb1IBCZQ3c_pB1hIaaiXbRMRC5RzchMMhu-Vkprks3Yqbu4a3BnXaht_XvFbyztXN97tvCYUsjgrb-Jsy_fREItiNQX62qsCOgublnVYWdl-sYOKf2zm7f2026ez9gfV91YFfdAvcsypdqlxB0mNga9EhFBbHePENywYdnJpwah2EgyQcJ2ta1epc4Whakc6Q22n9coGy9WsBwbug6D62Z8KWfUQLe8Rxmr6UQXF9C-VB-CNIW_0jZ5Ew-K6hs92-W3UTYmyxyDMzuhapR8oA13LGYKHhfv7zNXALRY4nGkNZcbJnNFg8FuXTnLzSynPSMZCuk0autRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=hlizASx7DqLb1IBCZQ3c_pB1hIaaiXbRMRC5RzchMMhu-Vkprks3Yqbu4a3BnXaht_XvFbyztXN97tvCYUsjgrb-Jsy_fREItiNQX62qsCOgublnVYWdl-sYOKf2zm7f2026ez9gfV91YFfdAvcsypdqlxB0mNga9EhFBbHePENywYdnJpwah2EgyQcJ2ta1epc4Whakc6Q22n9coGy9WsBwbug6D62Z8KWfUQLe8Rxmr6UQXF9C-VB-CNIW_0jZ5Ew-K6hs92-W3UTYmyxyDMzuhapR8oA13LGYKHhfv7zNXALRY4nGkNZcbJnNFg8FuXTnLzSynPSMZCuk0autRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=GHpe2JC43lilI2H_NSgiqrkO03k5veISwWgdaxrrwkPfQn6Oa3u3myM7OXl056foV_hOL1Eun5qfBJAdUVfESs9W0QeNGfUr6NWELnbTfRU9wIdEFZGTj1PfUvZx5wB2gwQY3kcwzWNIU5gAm2dyKFFKivwRviAhVmauOhWH4fztRrlrPy1DLdcGm2rfRI2kEGqgvbCF7PBYpjkDJgEuDn6Zq9nQtwcXhXh_c2BFAkf4Wvo4WrgN8_fbHJ9AV4tdu0m9HxhLcHMgLIoh08bueOgKSvveU-u_MzHMAn27YO7S4dPa-iqWQY0dUto73fM_Fz5J41ADMOBpNIm-yb1hpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=GHpe2JC43lilI2H_NSgiqrkO03k5veISwWgdaxrrwkPfQn6Oa3u3myM7OXl056foV_hOL1Eun5qfBJAdUVfESs9W0QeNGfUr6NWELnbTfRU9wIdEFZGTj1PfUvZx5wB2gwQY3kcwzWNIU5gAm2dyKFFKivwRviAhVmauOhWH4fztRrlrPy1DLdcGm2rfRI2kEGqgvbCF7PBYpjkDJgEuDn6Zq9nQtwcXhXh_c2BFAkf4Wvo4WrgN8_fbHJ9AV4tdu0m9HxhLcHMgLIoh08bueOgKSvveU-u_MzHMAn27YO7S4dPa-iqWQY0dUto73fM_Fz5J41ADMOBpNIm-yb1hpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=C1Tplv_qIBiF3GAqkeMCtZJVGqWphzbMjtaeLAk1N8xu3YcE-sFGJt0NVwrl4OazLYRG9lIxunybW4gMhLpCaLWGmpZTFXorZwRyMXv_UOXeMpw48gLroOQlfx9PaQEYmrI6w16MIL5OreyD4OK1swz9ICSItuIkDBArmztFFKdA7V3lGOFpJALYV_yr74KuVCxQelA1Y4n-Tgl1V5HgeC-dNXx3Fikq3mVEPwuIORlwi6sDnCMaOIW99RnaUfI20swlnaF2CW9B3uma8wt9sBxKEUV_0ctbckw_Z9WZumm3XvzQqAtTGGzEnpBdkHds-3CKpO51qv_ebc42EWpmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=C1Tplv_qIBiF3GAqkeMCtZJVGqWphzbMjtaeLAk1N8xu3YcE-sFGJt0NVwrl4OazLYRG9lIxunybW4gMhLpCaLWGmpZTFXorZwRyMXv_UOXeMpw48gLroOQlfx9PaQEYmrI6w16MIL5OreyD4OK1swz9ICSItuIkDBArmztFFKdA7V3lGOFpJALYV_yr74KuVCxQelA1Y4n-Tgl1V5HgeC-dNXx3Fikq3mVEPwuIORlwi6sDnCMaOIW99RnaUfI20swlnaF2CW9B3uma8wt9sBxKEUV_0ctbckw_Z9WZumm3XvzQqAtTGGzEnpBdkHds-3CKpO51qv_ebc42EWpmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-H0xrHK18uEifYm16n7jhrNqVd95TIy-mrUAblY7G4Wl6-0Udm0TeZYVJ1K2aGSiJRcVgcwLFUmtkUfW5UshjTQIohZiqlE2mjE5i-oc9y67WS1O2AF2egjGj26kn7KIBW8HyOZrbAOurcfJ4BJfwSZ60z518YabAtK7f1dM87mrnzF3tXZGOwtRLsr8o4BYkmjnvRY7nATdkXAaeNWq8Y1O1VQWbvfeFz32KKBNdMYtsqVjqQDBkCgRAJhMZ4j27vR4hpVvuDqKLZpysrbxkIlz0WoredZ4oYT0YNXhMTd3FASJlNzNFbiBgEVGaDM6LZJxQJkRVGJXZSofF8XQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdXaItdRFFR-IOCkBwTdlschNSD_z_AcAypWzXJtZQf27yaMLvY4wdRlLMLlKg9bFuyYHeWV3B0Dg4_pLNC5vK_7WvEAVKERuUHH18JbOJssRtwBS-76yx1vtmohHoVKclmHcCUNMTs3Qarbtjc4ZD9JAYZKF_ONYwR2JRasdanwyVzaebnfgPJeAxA8HpT5hwZt0wCuC2497yubFU6svWW2kiEeaKOWB8Ix1RHlmABJuGwWCz-tVTAJWE9t10AfJjQRrTr0P5XqeWN49h7HFTfiK0_3371RCFqnJNdZDeo7D7LTe-0prd49PD43dYGCJesxS7sEI_LB3IX3X1jtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=iNnn8B6LG3h2SbHpASjn-1S7MmrCLmVCGZwvlzCzAawrsBcXw609ADuqwIS3K6sfTuNscbYUjmjkYQ_6vlERZO8pjV5GIf8KSwdt0q3_46Vyai0PvErVGirc-J2OF0H8vV-XKViMMuKiFsacS2R2ui1j86214QauVG67vCELTW10RwxB1aLQoPxTJJvS2t5MzzWp1QHtLdQ10byVdpOI9rao23R7wpMOO5HJ2AO1_zgZ6jki8RW7O0eUL5BOEyq0LNGKMChwU-FWn-SA3yUp8OO-0154o5vckRWdcYCEhnIP7cYVGDutRtcZH4lsO2WYSAkuJo_7gp4iUkiXFTzLNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=iNnn8B6LG3h2SbHpASjn-1S7MmrCLmVCGZwvlzCzAawrsBcXw609ADuqwIS3K6sfTuNscbYUjmjkYQ_6vlERZO8pjV5GIf8KSwdt0q3_46Vyai0PvErVGirc-J2OF0H8vV-XKViMMuKiFsacS2R2ui1j86214QauVG67vCELTW10RwxB1aLQoPxTJJvS2t5MzzWp1QHtLdQ10byVdpOI9rao23R7wpMOO5HJ2AO1_zgZ6jki8RW7O0eUL5BOEyq0LNGKMChwU-FWn-SA3yUp8OO-0154o5vckRWdcYCEhnIP7cYVGDutRtcZH4lsO2WYSAkuJo_7gp4iUkiXFTzLNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=ut7SYATblucWltC2ROk9A3k2ZM1EVgoVkfMBPrDYn8HsRZsoJoLoasUA9APcHA5OWrvr0pWBFldYdwjumsyVfEo3dYStcJur3ggUoX_NU2ddQhyQsyAEQw9H2OdWx3FvdAY6MfvgxX5EA3Z_UncX68F61BiT--uWIV7fVaMMmqTibSY9Xe9puSUaNch10spflmPjNO1HeYuuU4MhjXf7hBySDyZuv622wVcRUl6FCHGQnStbDFlkuMshJcn9BRG3Yey4M9UK2GiUnPo6tPfXWKnG_ZjjN22uZSNJPgKEvJAYFK7AvwEC5h7FH5q7zn1HsF2LT8_h_8sj7E5Cr6WvZSch23yXXX60N6hbdSQS0I9ynApEr7TWJ7pIx8CaTvydtlF6Dp6SXGUVOLdmx9c3sWLeg6h2OZqBh_DY80ctCglC0UpZ1Nq73cQ3uaY9lKxz84E_xT4RAGRDnkoqJxYyWdk61aV6hFHo_OejRmtFVWWHZIDYSMQe-6SKVDQud1qYyWdAkfd1e5AOA5FIe-fvFg5pqF6dedcFEZZ13E-lXu3adgQ-OFWqXUjxtLGr0CvcJbtZwfgbHlW0af92kdKb28nr2p7LOR2hf9FhDPHSzvo8_xY-hOAWi6PFIyvxxAud-6yl6XsKvSTsye6P9orsA9mAJ9_1I3BYUwtp6DWU_0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=ut7SYATblucWltC2ROk9A3k2ZM1EVgoVkfMBPrDYn8HsRZsoJoLoasUA9APcHA5OWrvr0pWBFldYdwjumsyVfEo3dYStcJur3ggUoX_NU2ddQhyQsyAEQw9H2OdWx3FvdAY6MfvgxX5EA3Z_UncX68F61BiT--uWIV7fVaMMmqTibSY9Xe9puSUaNch10spflmPjNO1HeYuuU4MhjXf7hBySDyZuv622wVcRUl6FCHGQnStbDFlkuMshJcn9BRG3Yey4M9UK2GiUnPo6tPfXWKnG_ZjjN22uZSNJPgKEvJAYFK7AvwEC5h7FH5q7zn1HsF2LT8_h_8sj7E5Cr6WvZSch23yXXX60N6hbdSQS0I9ynApEr7TWJ7pIx8CaTvydtlF6Dp6SXGUVOLdmx9c3sWLeg6h2OZqBh_DY80ctCglC0UpZ1Nq73cQ3uaY9lKxz84E_xT4RAGRDnkoqJxYyWdk61aV6hFHo_OejRmtFVWWHZIDYSMQe-6SKVDQud1qYyWdAkfd1e5AOA5FIe-fvFg5pqF6dedcFEZZ13E-lXu3adgQ-OFWqXUjxtLGr0CvcJbtZwfgbHlW0af92kdKb28nr2p7LOR2hf9FhDPHSzvo8_xY-hOAWi6PFIyvxxAud-6yl6XsKvSTsye6P9orsA9mAJ9_1I3BYUwtp6DWU_0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=sWwJb0rZoFmEjL2zwNhyyywtybF5nX9OJLgGYq2_ZqhbrRoFX7TdyVTv7FxTNG_ICB1z9AcrrqO63HM-1UH7x8A2B7tBiMlV5BD7G9jTPSEgdsGQD2gwaX8z_Qa_WVUw3IgSn2fj2rp4YzJQV3sfh5UgUU8aJZuFk8iiudZz3PUCQgafgZ9f9jtVQEcRyFHQTdTJH5IbRIV663E_TzX1GKGl2xEM6THrhCRHUiIXMF7etAukZyTQniEbmKNnURWSC-hi70bBYYddmfINdTlTehoF27otWp1yo69nEL1Rk1DFLVNlY1-l-Lj7CS2VOQoApW32a7CbJe1xwJsUKViXtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=sWwJb0rZoFmEjL2zwNhyyywtybF5nX9OJLgGYq2_ZqhbrRoFX7TdyVTv7FxTNG_ICB1z9AcrrqO63HM-1UH7x8A2B7tBiMlV5BD7G9jTPSEgdsGQD2gwaX8z_Qa_WVUw3IgSn2fj2rp4YzJQV3sfh5UgUU8aJZuFk8iiudZz3PUCQgafgZ9f9jtVQEcRyFHQTdTJH5IbRIV663E_TzX1GKGl2xEM6THrhCRHUiIXMF7etAukZyTQniEbmKNnURWSC-hi70bBYYddmfINdTlTehoF27otWp1yo69nEL1Rk1DFLVNlY1-l-Lj7CS2VOQoApW32a7CbJe1xwJsUKViXtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKzwonvZO27lz-LObLKGPEDLrXs-L4jfIIFywKBGdd9gUIJxpm_XegRlJsanYNK1vYjPamI5nLiFCR7UB4CPAiIvx7_XUGN-IjBsZ2_PMiiZ11ppiotki8U9Cudbn3oKfvZMZYi02iUgY5JpXQTBmq7vjnOCiUoWhVQH3e2-x-k5aiYc1O7fHVnYPff_pvVy-usNrp3dC1Gjc2vZi1ce8sihaEBPFIedjhbhe3lWHT3CYrh2LSqivXkrDg4U48e4DSEEfM6K5PiJ94NINPPT4lAsOXgrpc6s307ABGS1VtQ0Epd0VO1wViohmKDyuTm63aXGbkYZIulKhPRMwpmWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
ترامپ به فاصله ۲۴ ساعت، از ایده گرفتن ۲۰ درصد سود از کشتی‌های عبوری از تنگه هرمز کوتاه آمد.
«به لطف نیروهای نظامی آمریکا و همه اعضای قدرتمندترین نیروی نظامی جهان ــ با فاصله‌ای بسیار زیاد نسبت به دیگران ــ تنگه هرمز برای تردد همه کشتی‌ها باز است، به‌جز کشتی‌های ایران. و این هم به خاطر رهبری دروغگو، خشونت‌طلب و شرور ایران است که این کشور را به سوی نابودی کامل سوق می‌دهد.
بنابراین، ما
یک محاصره کامل
اعمال خواهیم کرد، اما
تنها علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هرگونه محموله مرتبط با ایران حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده‌ای که با رهبران خاورمیانه داشته‌ام، تصمیم گرفته‌ام
کارمزد ۲۰ درصدی بازپرداخت به ایالات متحده
را با
توافق‌های تجاری و سرمایه‌گذاری
که کشورهای مختلف حوزه خلیج فارس در آمریکا انجام خواهند داد، جایگزین کنم.
این سرمایه‌گذاری‌ها عظیم خواهند بود و در عین حال برای خود آنها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdVhX-RR0n-Qs3RNU8CLQy0NGj7uF7HfvkXiel0lZSHOu46AWINzUJMP-g5HsqoeZGtojIoHztQqKOUt35GjUYTg0cHYp71zOE7yvUKwCZLDCcDE4iktxLXnoxXYzkG_hNHH2hHWESL6ycWfHFhkxiiO7VNICI9EyWwPR6Nr_PynWX-1Q6xYvdf4Yv5uz86nL2_bDh06od9aUJ70cAfwMqb8woGCKQizSUF0AJ-o1akTyIPvJ3F9gTY-QPb7QAQw1Z9ECnGH4v1-iKQ5C-GkPhZqjFTP0LvgMqWZtTM2rrtX81vJ1L5RLOho-Q7eKi6QJC5XwuvZqGIyOMS1N7c8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=PGCoURmjIhJj6YszZX8JecC7CryucH3f9uZf0oZuVz0GtDy-IOh2h012GynnC4Hx2Oqa07lYmyxlcudoyMYQiE5vZELDJ9faA9MeNRm115tOoJqXGpW7mizI3GwhTgU_pFCASsEu6CiFl71nHB8kLJeAxsjZdBvbo67VyR5R6gGmNGc3H5Cy6Vb-7BIO5AtuiAs7-3U-vqRptp-7UQwU5uRki3JwBolUFSizQdFRUBxfBCI5plza5lXfx6ffh2JMKqxZkGeVlCT_xHspZtakH7M2_W_Ki8O87NMJ0VETG-Zfr8qCLZqBi86ydrrdGOn6q9o7ZxwEXxAoVnpBjW-SVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=PGCoURmjIhJj6YszZX8JecC7CryucH3f9uZf0oZuVz0GtDy-IOh2h012GynnC4Hx2Oqa07lYmyxlcudoyMYQiE5vZELDJ9faA9MeNRm115tOoJqXGpW7mizI3GwhTgU_pFCASsEu6CiFl71nHB8kLJeAxsjZdBvbo67VyR5R6gGmNGc3H5Cy6Vb-7BIO5AtuiAs7-3U-vqRptp-7UQwU5uRki3JwBolUFSizQdFRUBxfBCI5plza5lXfx6ffh2JMKqxZkGeVlCT_xHspZtakH7M2_W_Ki8O87NMJ0VETG-Zfr8qCLZqBi86ydrrdGOn6q9o7ZxwEXxAoVnpBjW-SVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYgegCSod5jXIHYi_OVqUw6dbK5UMrk4xRfnwG5Qf9qzo8PTW7uRdjPKHrq8DCKWlJA65ncjrkwyY2X3nK07KDLlQCLwv5Iw1PSZ5gxJ1Pxe8v1O2azp9ZD8E7eFmJ0kT8Wfln_jEEG0ZV499FzCBJEs88WCJYnuoTBAPdv5bBZjhcGHiunmIAXZtiytIsrMmcbRJTOG09YGpDsiHcxnyTKKpB7qNCDLFHisYWA1AMaeACbTFywiq69ZcpNTrcC1HSGUPhBzfVp17GMH3O9SsLSBHMrzZa4EMdc8SSnCyeofaGceT9BiYIykwNrx6mXMEn8nRr5jWmEwuppqJbFgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYnaegLCBF523fWvs-6SJ096q9pwDCn3q0mUVzbpR8Y08SsiR0rEVuU7OOLhGwRWUQHbJpfxoBftaTbmu-0fR6Ms5l7Rf7m2uq9OOHmAKNVmsYveUX4D4b6r6cketRuQ8Qe9OA7FGgatRnylpPxjcjEQ5V4xxGXrAdiMB1b4ymEayOeYkxC84ziOncYEPMdOorZA7fh0CiZLafumXl-jdVlgafF9j7p1tM4n1QvyFvFhT6z1WvhxSu_rackt6weDIQsXPsRhh8PG9Sa8xLu2TKoA4nU9jc6O9tSoys5elkRJ_QujhRiTzB0EGq7I4F0cwaIajzi0lZZP2DVDhW_lSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
حمله به آبادان و ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔺
امروز سه‌شنبه ۲۳ تیرماه،
در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان
و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔺
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه
اعلام خواهد شد.
🔺
جمهوری اسلامی در این ۴ شب و صدها مورد حملات، هرگز اعلام نکرده که چه تاسیسات
و مراکزی مورد هدف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=aevlXstpXfGQmXt_gVL6LHPZW6q41zUuNHBO3G_lwaCc3b9bTRJusylK-kcU7wCdHqtTdRrejLsi1Wij45Yu-Ox7oV9a32DyJr_qCg6u9WKm_maGe5ayn1aa2rI0hy8i6kT4CW1MT4dZkFN0-Q2IYKdgTFvkBarr81fk4dJB1k397_AWhtlP09UomjrQRgqM0BnK-Nh7HZF7zcjKa7keaAzUfflZFTy2ZN2BSrpP6KFQPmUQHL9nXfZjIqUPZZ0SmqP9lMceeyiBM-jtvo8ZoESJfl-A8AL_WE0P_xx9s67xCYaZ7CqW8JYFeC4_XdwZxUrGxYzysQtFv4L0kXr9xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=aevlXstpXfGQmXt_gVL6LHPZW6q41zUuNHBO3G_lwaCc3b9bTRJusylK-kcU7wCdHqtTdRrejLsi1Wij45Yu-Ox7oV9a32DyJr_qCg6u9WKm_maGe5ayn1aa2rI0hy8i6kT4CW1MT4dZkFN0-Q2IYKdgTFvkBarr81fk4dJB1k397_AWhtlP09UomjrQRgqM0BnK-Nh7HZF7zcjKa7keaAzUfflZFTy2ZN2BSrpP6KFQPmUQHL9nXfZjIqUPZZ0SmqP9lMceeyiBM-jtvo8ZoESJfl-A8AL_WE0P_xx9s67xCYaZ7CqW8JYFeC4_XdwZxUrGxYzysQtFv4L0kXr9xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1V_aQErSeN3LBaYxlWjqZmb8HCRiiypfweSniQq9aFHavVDGQ4og6pNEnUAwVA3pKq7JVqnLVffuFnJ515SHKjmUX2SSF7JJpiAqfbKDPBQiKS-VbcsJrNkOixWvjN-K9TjqETGlr6J-Q3SnoASejxiP8e8Y4MDRzI0q0r6VhAqPOqY_luj_wLL7P9BiVoyvQt0MDLnbhvqOtlHi79C2JP_Fs_QlYYBEqRuhZ1_uKrODBPklDAleaP6aE6Nm7AQpl6SMfIX8yFBaa8qD4uQdUJiuk5ecIGbySFovpC9rUfKbCk8DPnvxO198S7bhERMBhbUd1hx_KAVc1DkUSJbQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6NWlkqgZrI5hUaLa5HLW3766qIiJFckg_ZH3tebEkzYyDk4IwPIBAldIU2wqNVrY8uCF-R0KTVyCTiZdIywuTVRILPnJHhSVokOjK7kKT4jSkDNjDAlTUCnSOCwVAU55_54b-Ao6CdKCN89l-HcFbsqmALvk6QO6ahsszDU-BVtORLmyDhveDI2iAbr1riEkf5pVOLEELlsfhc2nDRHnOLNqwH_T_kHWXgNmj2TkITN0h3omdsTBdfINK_kU2mvqOXtJxymAybalpZARD-agfjMUlCtFYV9DW-kH2f9lajhWkLYyETOr8iaOf6l-6a8EwOCQFd5PR2_8Ja_-sHvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.
در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!
مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی) نیز در این حملات مشارکت دارند.
🔺
دفعه قبل هم که امارات در پاسخ به هفته‌ها حملات جمهوری اسلامی به جنوب ایران حمله کرد، مقامات ج‌ا تا چندین روز نگفتند که کار امارات بود.
الان هم برخی از این حملات مثلا دیشب، با حملات دقایقی پیش مشخص نیست کار کیه.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=ig-vFxEzGnjFYX9MvSrIeuQ5epOCayaGrqi2iWDabtp0kajSvs5PWXA6ChZjPcw0S5ULlu8XqsfcI6DGHgadCOYCSDRMqK1hE4Tkjdp6fvk0hbV4-c_uUU2_x9jn9j0B1T9_BDFhAGX5s3SfHISbYFHmWjN762vfNmJnxFHOeCO_ZS6Fg7a4dWTcAGfhEjqPHDigFBD6F1JUlbItJO6FeOjx61aHNFIyodmUDhcKfimLk1x5eJIwtH5M_VOWkeoNHnpgVkGjruea_CazgX36ByHrJPOWHL7gGJS7-ipSBIXr1qe01gXvaJd0J03GTmJUF21BfnhvNkWA6416g9yG-2PYG0P8rDTx-oDueKclT7J-7dVFEnqsJ0Q-Ad6Fji_1yyltBRgQV8Mepznqds_OmPqz-C789lbaDo0HBMSeOSxOhbLg3X89U_8TMTLxd8o_i-oA_eIxXCJrJsjX0dom3KnN63z8zJ_lK5L_5vRxGxVJrEbvAJElqNh_1z48oZiBWQUPKMtTrERPyhkZH-6MUO5hwxwJd9vzfXuAgdfMtO8TxG9u1XPxoB39-qzT-fiP_HTNWffGLBlgzsaTdSwa0YaGPBWj-PzNkDE9dRAZaQ2p0k0vn8nReN6Vq_WerEN72EWl0xZrHaOLYQHD_3U2R9ZIViwWWlSEJZ7_88AMVyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=ig-vFxEzGnjFYX9MvSrIeuQ5epOCayaGrqi2iWDabtp0kajSvs5PWXA6ChZjPcw0S5ULlu8XqsfcI6DGHgadCOYCSDRMqK1hE4Tkjdp6fvk0hbV4-c_uUU2_x9jn9j0B1T9_BDFhAGX5s3SfHISbYFHmWjN762vfNmJnxFHOeCO_ZS6Fg7a4dWTcAGfhEjqPHDigFBD6F1JUlbItJO6FeOjx61aHNFIyodmUDhcKfimLk1x5eJIwtH5M_VOWkeoNHnpgVkGjruea_CazgX36ByHrJPOWHL7gGJS7-ipSBIXr1qe01gXvaJd0J03GTmJUF21BfnhvNkWA6416g9yG-2PYG0P8rDTx-oDueKclT7J-7dVFEnqsJ0Q-Ad6Fji_1yyltBRgQV8Mepznqds_OmPqz-C789lbaDo0HBMSeOSxOhbLg3X89U_8TMTLxd8o_i-oA_eIxXCJrJsjX0dom3KnN63z8zJ_lK5L_5vRxGxVJrEbvAJElqNh_1z48oZiBWQUPKMtTrERPyhkZH-6MUO5hwxwJd9vzfXuAgdfMtO8TxG9u1XPxoB39-qzT-fiP_HTNWffGLBlgzsaTdSwa0YaGPBWj-PzNkDE9dRAZaQ2p0k0vn8nReN6Vq_WerEN72EWl0xZrHaOLYQHD_3U2R9ZIViwWWlSEJZ7_88AMVyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ4K1G-yV8xVtpev6UkkkTDqnNCJElYoJqgIqrFqYyLYa-kjos_3rh4WeTeWgNhwyHA4e0DN0F26OlDuuRVjHf-XBaLCv-EIbAKUnWCZIXh81B28dqggo9LHKrujMii7Gx1gCYwYEFMHSESlFGuJqrN46txVVpl7o9z0-S12Ht_4zx7DFGeKKNULCKOyVRPP6-AeYBQ6nhZqTkDz7xXyHmI210w5J_aAbfFqHw35i2F3oumdI5Yqrx2GwK5b-IqaSggPSDE1fhvRMuK2iEqNeOWOpyeY2H6UGXe3E_Pmef6gLGUgOcno1UZCAq5gfaZW0IgDksyX4DRFu4YR6j9GSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV418Rrad35FRBGTEqYjeH8RGij2bNC6ty8TJxL8dtFM5xAEr2JsDh86NUzw484HdCpXeArxYv1z0vbDW6JQ7_Mw6UJ2456KPiIfVtuOxupY9FnCZIpDJgk8aO8MmiWukYgA5Xfs4Mz3JiDdaXEN3yt8Ce-L9XjdfxDQ7t8S8JDhvISL-P8LUZcs6yhAEYgmlaOewESlvF3etf_venXukN9t7oJozrAtiR-7d9v4KZbZuyq_qLfXKdOqvF--mLM9A6tyfe7Jybn2CxUj6qQ4LvzUd0-VAltzGDkLhj6Z9CNDjze7cJfftG_vy6LIEM3t2RqUvp7wjRTNC9xa4IKwpoU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV418Rrad35FRBGTEqYjeH8RGij2bNC6ty8TJxL8dtFM5xAEr2JsDh86NUzw484HdCpXeArxYv1z0vbDW6JQ7_Mw6UJ2456KPiIfVtuOxupY9FnCZIpDJgk8aO8MmiWukYgA5Xfs4Mz3JiDdaXEN3yt8Ce-L9XjdfxDQ7t8S8JDhvISL-P8LUZcs6yhAEYgmlaOewESlvF3etf_venXukN9t7oJozrAtiR-7d9v4KZbZuyq_qLfXKdOqvF--mLM9A6tyfe7Jybn2CxUj6qQ4LvzUd0-VAltzGDkLhj6Z9CNDjze7cJfftG_vy6LIEM3t2RqUvp7wjRTNC9xa4IKwpoU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=VMoZP6cNV7ulS4ouRmB_mIXPxOZ_xTVCvaukOyXG6aCwjD4_ucdxKvL8fl0--bsX_NJbKZl_BXsPYfwX_4yGV2Y1yL2JXqfUPyIYaGUFgEWgJmbBwPI_KcZIoO6LoaoSqKQ024jnnt5Wyw5k0MAiQGZD2Sg59M676RBabKDi-JVdO3Ksjw4D71HEkPUfidGctMjTst-CgYGvkdzHFOOkco0jQ0qthc71R8HTqbM9gpLCph0peZqPvOAyHUbGdWYVIKIboYSP3zgfQ-LVawhR0bHjqYbadMDGGO0XiMxO4pgHTetmmeCyOWgqMtTEAxHVIrZzfDR5ZaGy9-_o3fQHsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=VMoZP6cNV7ulS4ouRmB_mIXPxOZ_xTVCvaukOyXG6aCwjD4_ucdxKvL8fl0--bsX_NJbKZl_BXsPYfwX_4yGV2Y1yL2JXqfUPyIYaGUFgEWgJmbBwPI_KcZIoO6LoaoSqKQ024jnnt5Wyw5k0MAiQGZD2Sg59M676RBabKDi-JVdO3Ksjw4D71HEkPUfidGctMjTst-CgYGvkdzHFOOkco0jQ0qthc71R8HTqbM9gpLCph0peZqPvOAyHUbGdWYVIKIboYSP3zgfQ-LVawhR0bHjqYbadMDGGO0XiMxO4pgHTetmmeCyOWgqMtTEAxHVIrZzfDR5ZaGy9-_o3fQHsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JM150qGztOh1WYEQ-fOJYtZUrnJaC0gCyUa7y4bY0m9FJamJWf_6eTYGSzCK7DNg1JsNQJOe4MH3nFrRDj0XxrYTiAItCru5pU9sYzxMs3Bmv3Gdw8q8U-RDWsU9RIwx_wDwSimqLD9UavBsUaoMX4PDCu1lP36tv1VbBeosvRLVzpXUO-XhmWwWMUOarawc-Aq67nc4pcvAZ4qL2d6Zcv4R43H-nEKEKE_Cc7ijXHDWdk1utlinpksAf2IxpIymxND_w2HlCgNIbFLSix0D1PQQKxdbl5NTT8gDrlbHjIBK6f2gtNwAxKuExIaYcy8sexDMmxyPDXmiLKNR5pGedA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=D3Ajfj3-NtXtJkjj8BlrN9jCQVjn166VpoSviltZN_hkFxw8HtQwwwm0wPHMV8kC_YobociovhWPaDvEhkWOiJQhaA-Psktx1NGG1aia1m19bK7gxyjdY3sMuIcVxea3th8-ebaufxLBRHhoaxeS9Mm4vSbc0oeu2iLSgGdumdDlb0SEZven3F14upVhGAiPP7Mjz3VDtBk13DP_QFOSk7bl3q58Fw7X8WwhcHzv9IGZ6HMRjoF9Rt0HoR9WxLDrZHktPWWoYec-R8yKMjX6ao2g1z8HsYJLolyAkxtjo3TZzxU8r_MChkG_NSlUVyyF735AcuyIkG4huFWlwgb1Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=D3Ajfj3-NtXtJkjj8BlrN9jCQVjn166VpoSviltZN_hkFxw8HtQwwwm0wPHMV8kC_YobociovhWPaDvEhkWOiJQhaA-Psktx1NGG1aia1m19bK7gxyjdY3sMuIcVxea3th8-ebaufxLBRHhoaxeS9Mm4vSbc0oeu2iLSgGdumdDlb0SEZven3F14upVhGAiPP7Mjz3VDtBk13DP_QFOSk7bl3q58Fw7X8WwhcHzv9IGZ6HMRjoF9Rt0HoR9WxLDrZHktPWWoYec-R8yKMjX6ao2g1z8HsYJLolyAkxtjo3TZzxU8r_MChkG_NSlUVyyF735AcuyIkG4huFWlwgb1Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=cO_r6m323ws107QaGJb6sxhzUQc9geeV8TmrlMzwGJSnhvLVRa5cSSsufLISX6-uGzfYCp2srcnp7cWV7eBfU-eJ3FFy9RaHA-C-FZnyNRw8bkEV4rwM0Z1BvHMwtXsF0OrZOFUtwEM_6Y2v4Ksmmy2DFLaaVMPJFonip55T4bcjQU78-owmjnQDBkwsihCD1iP1pqAHnSZlbIi9JRlBBSDVSXDnswEc9qXu__lHBWoPyrIj02onvyk_vtzdccXxT9SVzi_gYyuBJapA07txAOweXvon3O_dNfWybAHxSzktkLgO1nZ38PYfO8tRF5BAwQKAS9nBcdw7SyJctsNKdpQFkHnWcqX9UlZDoAYUoDXdcJxp8r0LjPe1R4iteyvh4x6awIwEkMUHjYnqcuKDZJ5M-13_8cfZ1_z9Dn7duUfYqAiGath76C6Om4a18NECa-PHQxBB96N6Uyr0UgULNkcTCdyG6EKsuCQhWt4D974nEnUZnkX6T_6WBoJ2DTX-ZFSUf-fyaghr1Pn1dc3FJq025m_ihbqlM0LQCa5NJJ4akIIoSU4v1_4ZhRMGbTrdAjULWjkQcozMCpRsjWIzDiwwy8NVXV0vWwjEV2gIBMGHUj4Hm5RVM2krJxU5K-wKCf5LhQzdcQRZyBc8KtXfEpHG8V-tOvKB6z5ZK6tPtcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=cO_r6m323ws107QaGJb6sxhzUQc9geeV8TmrlMzwGJSnhvLVRa5cSSsufLISX6-uGzfYCp2srcnp7cWV7eBfU-eJ3FFy9RaHA-C-FZnyNRw8bkEV4rwM0Z1BvHMwtXsF0OrZOFUtwEM_6Y2v4Ksmmy2DFLaaVMPJFonip55T4bcjQU78-owmjnQDBkwsihCD1iP1pqAHnSZlbIi9JRlBBSDVSXDnswEc9qXu__lHBWoPyrIj02onvyk_vtzdccXxT9SVzi_gYyuBJapA07txAOweXvon3O_dNfWybAHxSzktkLgO1nZ38PYfO8tRF5BAwQKAS9nBcdw7SyJctsNKdpQFkHnWcqX9UlZDoAYUoDXdcJxp8r0LjPe1R4iteyvh4x6awIwEkMUHjYnqcuKDZJ5M-13_8cfZ1_z9Dn7duUfYqAiGath76C6Om4a18NECa-PHQxBB96N6Uyr0UgULNkcTCdyG6EKsuCQhWt4D974nEnUZnkX6T_6WBoJ2DTX-ZFSUf-fyaghr1Pn1dc3FJq025m_ihbqlM0LQCa5NJJ4akIIoSU4v1_4ZhRMGbTrdAjULWjkQcozMCpRsjWIzDiwwy8NVXV0vWwjEV2gIBMGHUj4Hm5RVM2krJxU5K-wKCf5LhQzdcQRZyBc8KtXfEpHG8V-tOvKB6z5ZK6tPtcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
