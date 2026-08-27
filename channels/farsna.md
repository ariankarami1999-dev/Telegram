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
<img src="https://cdn4.telesco.pe/file/AvBv1WDOjA-Tdzre853p6XtM6MerS3tgkE0-F_Tb8JyjOTdW0NyqgRhPKo8jdckQtIjH8WmeYPZ3rHOOEkJrPiUIGMa1hUsQtLhl-QOHPhr2WRDTJG9AfLO4IUlT9_OugJQBLy4oUbc5CBaa2HU45qn07SLxyhaRd8RK-yBsWtPHVZqDAdy8axthzPStVBmv2aDBZysWzVTMUWBfqKfRaAT9TWekADyYoBrZhf01NtPpWYpSOI6cUr_pgR85-DbI-8qwFVATSbBPNuW0Eamrm8pyiCzZyqWOToK77EerTYmmTm1h_UQXGG8-Ys7bkIM4CHs_I6wprhaqTSamiMEO1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.86M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 09:25:37</div>
<hr>

<div class="tg-post" id="msg-458472">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbE85uVH-dZWuoV8FoZ1bOo8e96CKDin9HxwxMHvV0sKzUIhuC055_Pn_aH9e0Myz4yMZBSBO_GxK1cyXjWL5ZGMn1buQugKIeXi620at_2dYtIRD-BRj3BaGg_QUN3nL-DKV6TEOjqO4iGd145A1JXBIluPrQ4TTVSurd-l28QaGe8Vyz2papCwtywBsq_HwDHds_d_Wkl-Rve8k_63IW7UwXCsrfDcgEJcTaz7xx-UTArtzceNpVC1iTv-6rHymRopkdM44rKo3T-eRE9YSLELbig2xFJgdgpdXxCTwjb-gRTkKtyOXA9mGTAMGpW-VK7NKsRfNey2E2SVxQd34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ چگونه جنگ اقتصادی را به آمریکا برگرداند؟
🔹
نشریۀ آمریکایی «امریکن پراسپکت» در گزارشی با اشاره به سیاست‌های اقتصادی دولت ترامپ علیه ایران و کانادا نوشت: فشارهای همزمان واشنگتن بر این دو کشور می‌تواند پیامدهای قابل توجهی برای اقتصاد آمریکا داشته باشد و افزایش قیمت سوخت و کالاهای مصرفی را برای مردم این کشور به‌همراه آورد.
🔹
نویسندۀ گزارش با اشاره به اعلام آنچه دولت ترامپ «روز D اقتصادی» علیه ایران خوانده است، همزمانی این اقدام با تدابیر تجاری تلافی‌جویانه علیه کانادا را نشانه‌ای از رویکرد ترامپ در استفاده از ابزارهای اقتصادی برای اعمال فشار بر مخالفان خود دانست.
🔹
به نوشتۀ «امریکن پراسپکت»، برخی تحلیل‌گران این سیاست را روشی انسانی‌تر برای مقابله با ایران در مقایسه با اقدام نظامی می‌دانند، اما نویسنده معتقد است تحریم اقتصادی نیز در نهایت می‌تواند فشار سنگینی بر مردم عادی وارد کند و تفاوت آن با حملۀ نظامی صرفاً در ابزار اعمال فشار است.
🔹
این گزارش با اشاره به سابقۀ طولانی تحریم‌های آمریکا علیه ایران تأکید می‌کند که تلاش برای تغییر رفتار تهران از طریق فشار اقتصادی، سابقه‌ای طولانی دارد و حتی در دوره نخست ریاست‌جمهوری ترامپ نیز به نتیجۀ مورد انتظار واشنگتن منجر نشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/farsna/458472" target="_blank">📅 09:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458471">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۷، ۸ و ۹ فردا شارژ می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/458471" target="_blank">📅 07:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458464">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mk0w7ptapdoBb_bWqrxKUUWjNotuRN1ZFDrw43ihpj6jFKD92oW1-RYIyD6VIj6eEu92gvaxYju-PUDVouZp56q0Ac2CT1YfqYZCWC8ATsWQPcbbANIuP2SWb9T7eYPiP7fu3u0JJqhzEL-PCoMaVaMgOrw0GGO2WsmmS3I8YLazIiZd1Wi5r2h35uEP-pgap24YLA-aXcXcY41SF4tXCbACiBdn3TK1u-K81ar5xkYEZctZ85T_FyN7EjjYyQ5ruRjp3_C8IkVNRiM0QjkrbdbC6tt2loj1qOaUQnEPwDeoOmmoDhndE5pBL4iD0WQa6_jMXJ9a8iMLmyZxU5b57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyBy9pIxv3MftPMZCE2KpqcrrYVglp1FnJ88SvKNJfzqv95ggmdcZQjqDtTIe9ybvCx0J4bCz04-6ayTTyTLLX8XRio_7Dsp_ecnTrbu3ZlVCQ8B8XaTREIFZfrSFv5ezkYJJYlexhMvzK3MPTylf31LJiZmNkokHr6MtA2KatMMk-MR47zXNwhMLWrT1Uh9-ThgyQf2TDgNNBeZ61RdEkaemp_ZNQdaF6db7E_Q0BQ7zxeC5_UkRsGkOoW_kfI8fWfJR9_7IsBFcRuX4XLrFPJ9hkqAU6u_voDpIKtH-3Yjb0etkeFTCCwVFC6SeI46-_SJqvAIHCrCxYWHzg-TUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JoqBdHABoHHv3_XSzqYH7eWLxSm6V2cIyFXz-Q3uF4kIAKAuhjBPvo0Gq_PqLbiRD_x0vYAZbNa9dy003axWeRh0z6p1QhtTDFaqQ5IHkvnUsnaunsziIsXegCy3Xbvcl_040YgdIurQYKtrWF1_Z_ysFGCxhuSfT6lT_x4mk1khIiB1EQ-IJlsmSRlaHcmX7tnMs4dMSgKYR1qLzSu1BrJZl9mIAbnkr8sQAzrSzcduQ3g8X1jWAGI2L6F4ku_rgrmvjZ98Q4Jbo3SY-WdGV3YZiYgtqlneX4xWgy8JwhjANfXFyqmDkhC99Eh5wG2LfIq-IrlJAmsEyaQErWh-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRSstY4UQBCVyQ6BMeO_6ApoTMV85rImQ4oDiYteqWi94mmuJ1YNqW2ozmoOlymhuIeVMT86VjUzlZdyQGE4B86O6UZ0kp79oT47alxtpd-OjubvstDW_xKC2okTYg_Lxc2RJhsdQLfR0lVdjanIRPaB0uaepm5OXqOTfV-78YFHBAOhhsl2VOjUL6BiszQmF6dJvwJU7gmfEgPFx6cCszgD4EvNEvHUoaI32KjZWWdDtKlmFrPICz32FDc7PeE-dzVKsl45FpzHeSz9DkC_a9aOHo7AmLIcGoBYuHa8iEQ03iLHPC2q4qEJXFlid9Rm8rmfjz2LtmSf0v2SuSUaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCM2x4mFQh5jUbkR_7AHTII_tflN0qJHO1BzSrLtJg8Kncl9HpsRKB9VLVlk29QLH-I3N8VZGH3xJZMqDImfJr8k-epwkS4ZHqqj8hBo-kBFoxKwFDVQDizWZCQGovrf-Z9ZXd3txQEeqiNFGEkIvGcK30sfy5reHc_WfRGwIwF_1wvH8_9lipytVpXMn2zgjQvl78yZxdtkKP-MRWYSYpqI8XqDoq9kuJzJUTymOLJyYQxXBmfePzOKWK41LDc14PKpNgC5ZPMVguh6Tcyx2iAjG5KvQkZd21gzRMlimX68giNUKVVwtfnFlHUH8FrZn57X5FI2nnzB_qnx9ozwUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ak1M5P_eYkBUeKV17OqyW8xka6x9SHNWDhsa4cM94O5Ql5FiBCrwXSXh2rz5Kw-yTtisuPw0tKTijtYPLWW0yOfKC2DuQukdhrvZnL5q-lzd4sGZNjql0dYz2EsIFqPUBMVfyhTfzcXBm4AWhiWk5trHbs0i415W5kwM52vWTp2cWYCjw7CsfIY5VISPGeBwDJE7ll5cP4pWGZ_u7YY148lMcAFxLdgws2hwIL6hnbn88aPe7edNX9fTvsiM-UVhDDPx28glcSTlhzL1teApwOPmH0o8orf6Uc4QlsvLuJsBvrwiGETIPWap_TB0eBBdKVeKuz4KMJSU9WxyHlCLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhMQq-J7X98sPKgm95KDGr4HrsA8AWj3kbyoAoi68BNfNO9U61CAEl5BJsgLq2hIJqQ2ZGjuMKPk9hKE-uVqMbgrv1hjOyl_WZV4KIs9L-YlBEZqDZKsVVmUsGITCgYvImFSS0PAzEdWE6Sh2NlysryXslbOF4DqU2FWu7nnHpGcYLn26M8ZLk2G_Fm_IKeIiiTjCRz3FnJnqtgNQu3m7V6ezL6ywWmGYmh4Wb1VIVdlvg1UuukBnPoMDy_Wo2nz3_vSWJyDsbDfPXrgze2kf_LAMzXj3immiUVkPHRXPq0Bucq8_2x4isv-p3Ux9O1gqiw1cTneAyzZ-MTnNUCO2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
المپیک ملی «ربات جنگجو» در قزوین
🔸
این مسابقات با حضور ۱۸ تیم در سه سطح دانش‌آموزی، دانشجویی سبک‌وزن و دانشجویی سنگین‌وزن برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/458464" target="_blank">📅 07:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458463">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-hIsbO5L3O6eGMr44Y1kD7fqFve2860qliUPsC7h4kNPTQ03KUUjgl60E-6ZyS-ZPoduejmFLqp9d_8-zVk5Yyn_3EfpJaY6LFPIx6PdhMeae0w8o3LgLWK0J-gPoWlybiTgKoRrVsNTT0Yxw8VFUg-RTyEo-A1TNcWeieKt-_4_IPBlbrtQ1y9ybrJVKr-iPMlgQNVD927cwLnbAzIr4WbmjNVxCZlTxtJ2I_xBX592-22EOA8PZvNwZqOczF9R31At0sX4E4L-6wMIpMIgLMyxpEisg01XlUaaz-_hW56M34YFs3FOGEAzeFLzJhfWif9NxXqbQl9xE7UyiIcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام باند سارقان ۴۰۰ میلیارد ریالی در تبریز
🔹
رئیس پلیس آگاهی آذربایجان‌شرقی از انهدام باند حرفه‌ای سرقت در تبریز و دستگیری ۶ متهم شامل ۲ سارق سابقه‌دار و ۴ مالخر خبر داد.
🔹
اعضای این باند به ۶۰ فقره سرقت از اماکن خصوصی و کارگاه‌ها به ارزش ۴۰۰ میلیارد ریال اعتراف کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/458463" target="_blank">📅 07:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458462">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زاکانی: کالاهای اساسی را ۲۵ درصد ارزان‌تر می‌فروشیم
🔹
براساس بررسی دانشگاه تربیت مدرس، حدود ۵۵ درصد خرید در حوزۀ مایحتاج عمومی از میادین انجام می‌شود. همچنین قیمت برخی کالاها در میادین حدود ۳۰ تا ۷۰ درصد پایین‌تر از قیمت پیرامون آن‌هاست.
🔹
در شرایط فعلی، گوشت…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/458462" target="_blank">📅 07:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458457">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leN2V91EzRZytcMeVlUV9KinqKb-fgA-7ysn0q7eJwIkRSOzr5lB-yuvW7EF77TQMBgpAjXQzY1UFgzcKq0f8WB_vvPmcfze49RiX2tMYo5JnZaxgj_n5Gn-HW79dfihRC92XC-DzcSxHEAjfer243cf_kNlzCDj1ua_xvoCCCDIOAmro3JGbsY253Yk1hF8GOACEB3lLsbeSa5bbUffJeVpsPeMtOugTDF2_Y26l53RY3DcG1Lu3AmyLsD5gpfkxuPyCCXxj-O_ne2PQUAeL7Y08CXTK6OLzjdkqpc7NYAMEfhn0kagVJzwKdNuqYNSaC22dKDpUfjXHN15gSmXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z9z0jR3E0vMPrx-UQGT97ICeBx9qarkwskEing3lHrblX8kGST5oYl5Dlq5MWrI5Wy_6HzAk8vyPe6q8LbNHJ1vT4BxFKeyjD2A34F8cGUwQtP8hV6UnTo11gkUDbwJwy1grlGAbXs0ANO1y_s7RLpi4GLu2CHVw1icb8BfRFRGMPOLf0ivlsZY95VJRwAQE6p180aOwx9xNzlJSF4Mx6-tQsuybJyzS8B4TS8ENwYaf6WvpNpq0cVmmebdftN-xnH1OX_vRGonAdzHa6rvl1spdvjH4ZIJRDJlXEyVmsbfWuceWEiyq5GQfAuqS8-2xtOMVO-X4n0Wkchbxy-imOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ka5GND-chvzDHIH6C-PBdQ0xn_ElcXYctP98BY2LXrsM5IOkoZEKyemEiPZGDR_WoNlyvzK6ybuNDy2lvqpuc1cDR_XFu-yJUW7ayrzWua00HS2XyN4LYIm2xVxClCwwilzxjH0T-OInk6ZNMi_vnA4InJjTkmcIwK0DNUmCWezNaeQAPnexeKu-_A1adQFir24bVENiWPQwfK9IiBmHmoOXAwIdagLLbkUsDqI0cITnt6iz71xrEdnzx9a5D97iZGXaiK0p8ImBLO9tlUhJ0fLaWN1tAlPMZq8hfUH0n7P7D587gc8LfIE47J1xPYlD3YWk4SdzzM41nWwvKfCilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jzbv0YHCKY7NOr7taDFvvG5uQASW95ljBFvsHOuPbszuJ7IJ6WV2V00F_SmY51-VCEJLa6LRfgGWC1fB9Fk_LwZ6NHPJVnzVmSznZbTp1RlkJXRghI9sC4Xsfkn0H-GmP9jUnW2CVSp9IMN8J5-ZzKYQJAmV80ZQ1hnoDKExBb9DmXjenMcdDB2hk39tR7jJcN6l9WHHgowf_sdpZNXQrk0NauWJNU_My1UJaQccGvGpoQBWZLZweBkQI82Jg8cMpERypZlnXuj6U7HYC4GDHxdptIuJT60oRQ5DUWshRcg10smbWYjH6bZAl3_axY5eKGtY0FVd-TqHas2SqqniKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UaHDZiA_UhlUo3g-hdjZ7vQ5kM6T3Ov96pPuc9WrBjCvBrqXzyIfNiANho7J_BXObWFl9B5FPw9cI5eb3QDBT06beWdKMeilWaBKrY5z7YP8gdt1g0vH1z32kJQN8zYQ96PFC3-iGO3NWiVswTU2PzjCX4Ond4qnil_lhs4QfGTEhTsF-Weq8sJKSbh1j6P5gH9pAM_INQV77FTxlxcVOLJHyjbsAjFscQ-xHD0CcXIEscvt1A4vhJcGCAu57VPr6i5ln7dy_DAmq7VBymiECz5_1zNtTnUsvQI7oj-XZH_cNCz6lUsha7LJiKvpR2K83r_DnnJNqokqUKaarWjDlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هفتۀ اول لیگ برتر وزنه‌برداری دسته‌های مثبت و منفی ۱۱۰ کیلوگرم در سالن فدراسیون وزنه‌برداری برگزار شد.
عکس:
هادی ه‍یربدوش
@Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/458457" target="_blank">📅 06:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458456">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLY-gukM1wocKPj25l8aBtScBYaZQ-PL3FIPBN9k_RCX80U2LxjFssEBipv8LNwLl4Oi36AjrCUB6HGfPDLk9M4MT67RcUf9jrO1foRtYgRTwJH1gjVbbwjML7HYeq_mIcTvPQGxQx3qhkOoAqttB7XMoFdaf8Tv_obcVa2eJ4xCda2Mx9Z1AeGD1-9BKHmt6a34mNAbhPTIRSWQ2verAIeCLnGndV4O05K0YMEBO8EFhRb1Ca81Ewii7-5V0Ci2_lWemVu3pGVyQBJWdxlQHIv3lnWC1uF41khTTLKmdHRanyF2qVadNmxyxg5is_QEOibgFqYZkWmtWRwjCbbu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمع‌آوری ۳۰۰ هزار انشعاب غیرمجاز برق و ۱۲۵۰۰ ماینر قاچاق، از ابتدای سال تاکنون
🔹
مجری طرح کاهش تلفات توانیر: طی پنج ماه گذشته حدود ۳۰۰ هزار انشعاب برق، و ۳۲۳ دستگاه ترانسفورماتور غیرمجاز که عمدتاً برای تأمین برق باغ‌ویلاها و چاه‌های کشاورزی استفاده می‌شدند، شناسایی و جمع‌آوری شدند.
🔹
همچنین از ابتدای سال حدود ۱۲ هزار و ۵۰۰ دستگاه ماینر نیز کشف و جمع‌آوری شده است.
🔹
مجموع این اقدامات تاکنون حدود ۷۰۰ مگاوات از بار غیرمجاز شبکۀ برق کشور کاسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/458456" target="_blank">📅 06:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458454">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yba7lO_rfoksFhix9ABp7En0vYJtleshjmv00KjjjWuBXZ9mO5EEDz7XCsfGCmPokLg3iKJ1w2ExmytqBBDNF0Ufk1cD6kYst7cNfhw4lBg0noJOvchfCRsoPeL0O_UfUgiyaIl7njdflTxnGKn-nRCJeEZx2BclBSIs1NYEoXNFBD9Ilo52uObUD_P_aoW8CbW2-dgWjtAfDpjUy0wlIW4r2WVbhsbscDXKx-iK6XoN26RYnX-fg_bj4SUWh4BqaaFScBPyd6Un1AEtN2jBzBXpCjBNfhCYIz3Zutj73yG1U9WkxGkGBAObpp6yiGQ6sEaehtu5H1LV6L_MCypqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c2a029ae6.mp4?token=pNzV4piSegfrc8A2VX6M9xQR9tJAWjwiR8j3BtJFCdB8KKdfoZbCnlJ9dKIrSwM6GXaC4fbWWQsNNkDG55K60scl7-nFBXvF9cROzu_HnaP0C5VhoygrlJMD9k2rjgmnyc342Q-1kkGNVutCURIP4xGxokorY10JYXXygLRJGgclukfL8FfXtsxyRaz6-K82EtHdgFHlEdLC-DQ0hYxDqPAr8HvKFT5PACLkw4dXwYHiSRr3_t4ytP4B3jPzNZxniPAmeREM8bCaZEc06D7CStGrO5RTPvGPMN0tcG9sp5fG_2fgQv3jJrRrBIdc95vNMeoXZzYE5eF3W9302DXAHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c2a029ae6.mp4?token=pNzV4piSegfrc8A2VX6M9xQR9tJAWjwiR8j3BtJFCdB8KKdfoZbCnlJ9dKIrSwM6GXaC4fbWWQsNNkDG55K60scl7-nFBXvF9cROzu_HnaP0C5VhoygrlJMD9k2rjgmnyc342Q-1kkGNVutCURIP4xGxokorY10JYXXygLRJGgclukfL8FfXtsxyRaz6-K82EtHdgFHlEdLC-DQ0hYxDqPAr8HvKFT5PACLkw4dXwYHiSRr3_t4ytP4B3jPzNZxniPAmeREM8bCaZEc06D7CStGrO5RTPvGPMN0tcG9sp5fG_2fgQv3jJrRrBIdc95vNMeoXZzYE5eF3W9302DXAHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از شایعه تا واقعیت قبرهای میلیاردی در بهشت زهرای تهران!
❌
در روزهای اخیر، انتشار آگهی‌هایی با قیمت‌های میلیاردی برای فروش قبر در سایت «دیوار» باعث شکل‌گیری شایعاتی درباره قیمت قبر در بهشت زهرا(س) شده است.
✅
شهرداری تهران: این قیمت‌ها رسمی نیست و تعرفه قبور بر اساس مصوبات تعیین می‌شود.
✅
معاون خدمات شهری شهرداری تهران: در قطعات روزدفن یک طبقه قبر رایگان است و هزینه طبقات دیگر طبق تعرفه مصوب دریافت می‌شود.
🔎
اطلاعات خبرنگار ما: استفاده از طبقات اضافی در قطعات روزدفن، برای هر طبقه ۲۱ میلیون تومان هزینه دارد. سایر هزینه‌های آمبولانس و کفن و دفن نیز کمتر از ۸ میلیون تومان است.
⚠️
خرید قبر در نواحی دارای تعرفه اجباری نیست؛ بنابراین قیمت‌های میلیاردی آگهی‌های اینترنتی، تعرفه رسمی بهشت زهرا(س) محسوب نمی‌شود.
@Fals_News</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/458454" target="_blank">📅 05:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458453">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnqIuKS5TZonLOK5PGetzdoMWCuLoQU40yY297GbQGmHkuiECkD4yfHkOecu-lVdWw2iUSpi0d2HM0oUKGmsSkmu-Gurrj9pxxfybJimi8SspU0gpCxALMWSzv4B4PbX-DbcQ8kn23gqtLzuABmT9-8g3mUlF_Pv7NVHm3PEUGwTa6UuDUFeqTmwtx5x-q-5Fi-qVGltVhkMHsEZAjPhHxnPGJwyyaZJbgQJhEEU_zhny0F2KG94Utscu0pkKOKyPaq_jWOaT6bsUghYlk3O-ff_UETg6xV3qDP_AxGEidz-_pHNGDCnehyTrKcyd73JdnfHB6pSXQRVKGy8cSA1Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای دلیل سفر اعلام‌نشدۀ رئیس سیا به روسیه
🔸
رسانه‌های آمریکایی گزارش دادند که رئیس سیا به مسکو سفر کرد تا به مقامات روسیه دربارۀ حمله به کشورهای عضو ناتو و کمک نظامی به ایران هشدار دهد.
🔹
وال‌استریت ژورنال ادعا کرده ناتو احتمال می‌دهد روسیه حمله‌ای را علیه یکی از کشورهای ناتو انجام دهد تا اتحاد این ائتلاف نظامی را در چند سال آینده آزمایش کند و بین آمریکا و اعضای اروپایی ناتو شکاف ایجاد نماید.
🔹
از سوی دیگر، وبگاه پالتیکو ادعا کرد رئیس سازمان جاسوسی آمریکا (سیا) در این سفر از مسکو خواسته تا حمایت نظامی و اقتصادی خود از ایران را کاهش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/458453" target="_blank">📅 05:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458452">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnVJAHev_3WyjbrE0BEb6o3aHb_gHXJbX4cUpTa44O6IW1Qfw8W_2Ov9nxSn27u7hrBpGQe4_X-5pw5CYSo1xsensRATf8u4ST5yptKvwRis5zQIUGpKVjFARPnrpArOmrDHFwOQ8c9_NhOAxNc9F2ebzsuRfjg75q2f1dvfL1Q2Nfo1rkslzATmY1-zJKWFyRexZipqyFSiX_bHl5oqe0x9OEYpTvsGSKJi6Du-ypiuCCNgrou5xtKDnjwRb3JkQTvjSVPdemHERW01Xs6zNCvfspQh05ROJefmD5-uSYBjEJnjMRwqoAPRaB_zbJiBsrVx6-IE0ICN-AZo10O1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در تنگۀ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس: گزارشی مبنی بر اصابت یک پرتابۀ ناشناس به یک نفتکش در تنگۀ هرمز دریافت کردیم که منجر به وقوع آتش‌سوزی در این شناور شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/458452" target="_blank">📅 04:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458451">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf6v40A_5yi2tgxk0_-5ZR5OrszVovs6dsSrDV4_vrA9zRqlIGWS3HtZY2zKoNA_4p_AXzbdXJPlDeem72S8FT7l-TtkzKcMlR2FxC0L45isJ0zN8LJYteO2CJldja6djLkJ5-M5MREAYMMhNFxTUC-HYvXI5tJFrQ6mzFyXzLGZIE5MhMjxRBM9lcNIJPMmPqKF7fM70KhRDZoqc0Uq1qfuq6Y0jbaVKw35ZtzstyDy7DjhMgJZC3qYBeyS5bn3UP3yquqelNbL3NIcc63z-GOAj9pFdCPwTA5yJtGLQCHe5kXGx0O5qjcHsQeeW9DaRCjB9Jl5lt9m0uZkIIqY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام شب‌ها برای زیر ۱۸ ساله‌ها قفل می‌شود
🔹
شرکت متا برای پایان دادن به شکایت ده‌ها ایالت آمریکا دربارۀ آسیب‌های شبکه‌های اجتماعی به کودکان و نوجوانان، با پرداخت تا ۱۸ میلیارد دلار موافقت کرده است.
🔹
این شرکت همچنین پذیرفته به‌صورت پیش‌فرض برای کاربران زیر ۱۸ سال روزانه دو ساعت محدودیت استفاده تعیین کند و دسترسی آنها را از نیمه‌شب تا ۶ صبح مسدود کند؛ والدین می‌توانند این محدودیت‌ها را تغییر دهند.
🔹
متا گفته اگر یوتیوب و تیک‌تاک نیز به این استانداردها بپیوندند، محدودیت روزانه را به یک ساعت کاهش داده و بازۀ ممنوعیت شبانه را به ۱۰ شب تا ۷ صبح افزایش می‌دهد. این توافق هنوز باید به تأیید دادگاه برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/458451" target="_blank">📅 03:54 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458450">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBiOjMg9F669TAZObtVnzPJurmQGP6xM4JNbSNIR9fKuKEwzgMt1UlE4dBvyfVIhPUpE43lPPNeXmE0-F8xesHxIh76Rj-KeBqEcrzbN-fR2lNhqMcIt-Wi8hrOdUJi9xfptueUKoWVyV0012AFuCnuoIGBiBsdCvxSQ4YQrQgDXKZpIZMQIeWt_R_5ReM_w2LjRhmYwvdGEvOiA9_GhpyYu0VtSa_vKf_eSvjSwszqJofJVnLknWe7Ua7tlyMcFCKZg3_zamRLjhKFgdvNItPZO0gtfmLsvnw6Vo-1w7M4B1OcTEeYruzXYa_-xgTGNxKXPyHKpLBytVGNjuYTc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفوذ هکرها به ناسا، فدرال رزرو و سنای آمریکا
🔹
آمریکا مدعی است یک عملیات هکری مرتبط با چین به شبکه‌های چندین نهاد حساس این کشور، از جمله وزارت دادگستری، ناسا، فدرال رزرو و سنای آمریکا نفوذ کرده است.
🔹
مقام‌های آمریکایی می‌گویند این عملیات فقط به نهادهای دولتی محدود نبوده و شبکه‌های زیرساختی و حساس دیگری را در آمریکا و سایر نقاط جهان نیز هدف قرار داده است.
🔗
شرح کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/458450" target="_blank">📅 03:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458449">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCEmCkcWVfhgop__3mMUfBj-ZFpaLhxOJ9vTcIBZN3jQCnl70WrRRZqY2BpqMvAhjBPFHGQFo9bFVojg5s9h_YUzbVgQsE_WjIpkV0XKoHH-R680IzMi6SANXZ1m8sXnr84nOcI0GREVsu9QAv1T-U91lNC0uxazB0p83DlJYtbTO3M5EM4XrGOJqd7DEAAuB_pDGtIAvMLIf2SGS9v3GlenIQh9v2ac88nm9aZ3zxFlnz6jdcJTNgUA0R0NwCu_ZCEGnd6EDGYcxieSmd9Og6RJUnk91U3KzIqZMeYLpC0kvBL6XFXN-b6HmEDHtrW6mWXKaHsyyrVLronSvZ4SDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔹
کوروش اژدهاکش، بازیکن تازه‌وارد پرسپولیس قرضی به نساجی پیوست
@Sportfars</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/458449" target="_blank">📅 01:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458448">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">منابع محلی از تکرار حملات تجاوزکارانۀ رژیم صهیونیستی به مناطق مختلفی در جنوب لبنان خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/458448" target="_blank">📅 01:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458446">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a681aaf99c.mp4?token=AB-3FWSV2t4wHz0OY4fCkj_ii5WFAC3h8_FfdTxZclH_HQUVSdBG5t9aWGaie99hxNyn0IAG6hchBHuCV7FHXu2_UiGRl-n-HuWxwKJDf98k0htO2cQt6Tq7IfY63Aa4qsPH2yVCKJmenXZb5cPfLqFQfY3mtLpuCr7REN4ZWWIkfPEn4kW_KWluF7XrcU97Aoxg_HBYb0rA6vUUtW_IGVhTyGIapf3gCOCgXxBOjjzbDU3t4x27XL1IVtVFM-sVybHzgND2oTOYQ5KYkp9OgDL_EQchTSdJLcl3_V9B4LVERe97kFAgoIk7AFZK6pq1LdYtojEs-absW2-eszw9bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a681aaf99c.mp4?token=AB-3FWSV2t4wHz0OY4fCkj_ii5WFAC3h8_FfdTxZclH_HQUVSdBG5t9aWGaie99hxNyn0IAG6hchBHuCV7FHXu2_UiGRl-n-HuWxwKJDf98k0htO2cQt6Tq7IfY63Aa4qsPH2yVCKJmenXZb5cPfLqFQfY3mtLpuCr7REN4ZWWIkfPEn4kW_KWluF7XrcU97Aoxg_HBYb0rA6vUUtW_IGVhTyGIapf3gCOCgXxBOjjzbDU3t4x27XL1IVtVFM-sVybHzgND2oTOYQ5KYkp9OgDL_EQchTSdJLcl3_V9B4LVERe97kFAgoIk7AFZK6pq1LdYtojEs-absW2-eszw9bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنگونی پهپاد عربستان سعودی توسط انصارالله یمن
🔸
منابع محلی از سرنگونی یک پهپاد جاسوسی عربستان سعودی توسط پدافند نیروهای مسلح یمن در استان «اب» گزارش دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/458446" target="_blank">📅 00:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458442">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgG9jsEnP4HBRfUxDheqEx_QJgAmbWEE1vVmXj3qqeVrtMtarZzuJZJDrOzbpvzjWqIxcMhHkiLevH3T7DybM1k7Uk_dQ9DlgTyE2Q8FAPARTsCTXoAfgrZs0n1VkOxL4orZDoRxAWCyhC10AH2otuMRwWCWCvf1sdHTMcluHtA2Af6fawjlhHU2HYo8ZrFXVAPIIbralgcZZA47pNYFuOmakvQuuZP9C-zBgIWbpOBgfyEA-LW8IsdtcmMTCmyJcA5zPgPHDrlMXKgXzqRMPYIAgtAJiGKcnZ0Z1_iKyRm0g5zFXr9-vZlILHJn87PNhreBdIzyJ2i3I6m5GG8ARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkrFl4CB4I_U_wMUsKTlFtzLhcPDr-icoD9Yr2naJDbw35295_1ghSAMcl_uvJ0E0xR0VFltG7Tn6QXeQRUrYfBmGn6Gvn20nHmTanCDeo0Y7Rcral9GDZ3JInnaf6VZ0wFH3AEB09wO1JOCPkfOyyXwKAnRRsD7VwEKovbnXiTSeZT3njic7aKsL9GaEV3KIdKQ_KL7_EKliCvXafXQZINqIlpJxZof5l6s5avMDNqYfouUKLeiVd7zMbGKTKW7w2Q13tgxIVZUT4l5yhiIGhj0pOTbkKxeBTdhXWQWGYL4NwDBHqLxaP4GOoJVHz1sAtoFXt0OQaFffkaPS2XtWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAm0FOPTeFVSek_Qzy3f_-HL-LYRbbfJCvYg4y-iQmtE9hN-zWTr1OWshT2XSrutOcl2z7GnrFhN-CJpIZYstYLX1TQcU-12X4tM13QiA7gvojDSRUp4EaEyATyzAMTjUlbPJJuMfi1mgfnU4_nvOpuJNAZpftvByPowu9T08ImAJEKvWVR_mwcjkCbjpYmHzC2LTX27RLyysBl0Pa-V4zNxOAMu-Fn54qzcP9Ymt1JFwbz_OQzxpcErIlPLFoIvLiovlM-_8JuGqxhehXUn8IdgbtFjUyWKd0XAZvi9d9jFX0-b2tH1lTcibeykOgr6DmssgSweBa_Owf1OenQ9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuQ87T5bktTrQ6TK3ezFobVebtKWIA62uQrL4-88wHzrHJo8SrHQyhRFvJh0ZvHFkhH3A0X81_K1g7NGCEoLEA2K2rA0XbgfjKXLC-HGN4-i-vWTi9ICXQYsnPRIEspDVts6FWQmRfSgh_VhSz1dqhKy0Pu3us4CqFBU-V4qfNnaZfyaN7X-xofr_TSbNhs75wsa1c9qDQhDZrNFu2dQyZMtHl4tz34h8rmZFOtZShB_a6X1e_HX5PTZAZImqxxyLQl7iF4F6KUtFUitkF7frdz5xDgrxH0_VD_MxTpnyv4NnbczJQdDCWh45-GGAadqgwAXgeoGo9wlkGEa1WrqIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۵ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/458442" target="_blank">📅 00:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458432">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_h2hDYWmfEmzjKehSJt_H86aumbELVRG83a0iRItEGiValVWG8i81ynFoAavesO2mf14nGS-MVVixmwkBJguJW0gz0ZlVRkVOoH40Ps3fo3aN02a5MTlD8oASo0s5vE_12MOIIt15Gvio3dFUMwxS1yG-gOoQaLe7PsK64E8dP9SVwCmBSGJj3rzXOzzgihjsOMiFlLnf_Ref2sAi0p-w_7L0CqprVoQgAVvXkJKRVaejvF6shlBcCBa1X_D0jTY8l3HuOsiJLe3B0tCEd6Dbqj77YcCs0hSi0KFRxLZg5aejj7KuUjrIgIP1H5fs2mpn9QhmwJv0HW7_wVcBhWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cd2UBLGyXxUm7LMGuT_QKQyjsvMEdlgHRSkBP8-0-G3a_Z7XIGaMz0Yto3bIqotzu2O4VMgE8brKx2u2MqpXyOMq63sQQuBOMSPrFJriUl9B_ALscMFbbzecqTHkjWY1JrgvrRAfPhDQqI-J7kAnWZGeQDistu6lWhXaOxnQ4I7corvxET3nqAr8-tJqiVQwMV-cvM4E5AyG7tkALNBA2mKbMpdMyqtfC4ec2_psdm81TdwSKTAHCFbO01DNSC3Rl8-S4Zz55YwWmUn0VzmhRr1vPgXTH8alAYYgRpZFXlSzCCc8rFGchqMmXhR4VK5sIGg26Mc69L23eZfJo87XBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CE8UsOmcAA4lDefYAqRa7y92h-od09riRI3mSk3VE4maXf55Q_asGPC1gsbsYnX05p12lXxc-lons4cHyrqtBuP8HFa6DysABM7gI_RzVa1AX2l436AI5s2-IwHzcn6YhoPPCHrAwaI5is7br1KRU4WwHDiJtJ1I0V21PNKxNjplctXkFdNmeqXRrRWFfFVVKQ_vnX0jmFqP0iay8cKFiCiY-WMv4SKSK0yfkmLfm0txOzh7ABUdnDL3IRX4-aLvFG905jfZH2nxAlfHq63PVQvHnZv1g2BsWHX65pJGiWY5KEnmb7WUMCjPxiLc7MAPj5jd_kviqH3LZjz_F98O5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxPNFVx2DdvsihiLNswYs9ENacItnhL9JCr2QX7Um_-maufbqZipT6Wh7vfRsG_CWcLJvBDj7iCJgP8Qzghpt1b0FRgLH_xU728nVcV5xr6XmGz2EoBSSXl8fPgqk84Xy2HE2PhljMW5jVBXFJQGp4oeEna4ATvZXjkrvSVOjyqTByRtAXsSX5h6AopD2Y499MJQYIzyWHOD_DcnkWbldFZ4tmMhcR66wQgucjuXZ3c6IxmV7cnEFZwfqq9gy4Ro-0xz8SDSNHC3MN3BqvA7CjQLsLu0bgcR7ulZvxw9KCBWOZAE89pHRdcp8WLImcZTlHie9vsjA1Cm3iN1wVzkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tj7S-p4OlKUOZUY17nSEJXkOveesshc6PJ24Sx2zXcAa6mQQuLmTvN_FQEt69emBn-ImdVmvr8UJ3-6Edx0BVyspSvuZmHbsCy7GHTOePALTkmVMLBDP2_v57HNdlbRcTWy01VMrTEvOIM1PoGVMYviDOLoliX_E0xmm04Lju_3huUIWSwcbLxTycRHBbMKVHH4RagoYzv-JjYh4nKzDkSCgupZ1qNKkbBgStwoqYH_Jw36vdhRzW-EY87gjkdxzN0wJxGyalgtu6jFn5GlurZdpWJHh5vSsI5FR2nDoxEoQOl4A1MRjiXH4Og2_XmJXLubBVR-HGpcuzk6ZIBqqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9j2OMpIFByIuIFKKjMlx0AcgaU2MEnwYfpNz1sRDMz4UC_hEO5-EkOifZ2ucf3smXEZg8ritBs1bEqusqrame8E7rme6TFcydmYPQ2Nm0ewsXdpIvAOdPKfQsU1b5nGfEKRUqZouIt6wkGFtG58oJiMkPui4XY52jqhlkhP9JpdE00abzNjHhXvR0KMm7Bio0rDgEL65qJawX2-9Ya2_mVpFXatokaBSJZk_4V9AgxyH3KWPEUDaxieQE3tDIS1FCwzu2fAd4zzjrWfMooMElywU311rjWq4f5y8Rm7sEvulAr07h79TDwBVxG1QxloNfwALepcRr4VeRdfeur1gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0wa-tFBPWjfi_MAeUIke_h3QsBnrB-Wb4IIuPBg5UX_SxZ7yvSIVnTW9y1N0PDKwY8o3BgLyiOL_WmzGw6uE_yQAh8Gp71M5qbVwENxiUjSIWGfltvVlmsYdtac5SwxuyWlHpBYW41kWUSjzTleSgAMOI2fIUpwekaXoJ37Re5HTR3OAbN0rHUhkbQdtwaaK-RZ3P60DM0oyTRlvIpcBwTXsz6EsKp5co6izV_VjHCjzPxh4SgFUMcK-1d2GFil5KFQfhCZKa9qNlUEEvHRyWNdDYtQJkjy2jqO4cuPjhXYQW92Sn835SwZJipohtHA4JzpqGGoFIaPZ9Wfo_vcgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQf5hqloWCEYTxcyoO5jz74vBiIsri_8npUqpqGq9oxGwaLK0n9kUg67rItb8AgLq-I1nfP8RXbJ983VFM7f5vDc8pjt5YL_8S5WnXbn3R4BvvBynwy6sID_Nr8JV0VWEXd8hUEfc9bv8gidrWpO6-TReresilTNQBo45Wu9ZqGMrUZ4Qo9QbmF5hWkBsl4MBqy_FcsOigUFkWNLjCFF8hncEFhzm9Zg7BeciVHUpf122uNfP7C-gH3XxmQDifV4_vXAJIOXNWyGs_ZTVNdmfQe12PRAWf4gDZPmZtU6hqJ4u0FWlA9wwogjm2cFEyOIfaE21mfAWPiuSO2hPDvFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LHQG6_FFroiKHqld5k4zHHICjFHhTjz5EHgUgWHiTm3wzXWNam0HVxJpRAxArutkDbCPnGtsEHcaONzw2I72h-zQP6T9dcWZUEMAe4tlp8GyHju53a5LejN9VOUbvQhhZ7Cgr7PT2_LnKKYHfxaVl3E2Y8WtVmXUwzBCDhHVn01kToom1sF4Fms9NiAzOdiQdU3Om3uo6k3GTXUgEUP78fVAc74tzf0S4Exp6qge-xdv-7u9exb3l4hcldJ4QyGjdt4UAepDPhfOMfhyuTAZXN5-htSXyrZtngWxcvKkQaFpbqT4OnAisKHCYDZz5YJMNvjODEgC5hjnFIPiXQST_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqVGHIB72yS4c2Q2lNnRNjKUlSm6W4LJCDShtyh5wU1wsyX_YrqviCQjtwMkKaYNzF7t-ynfJrc-eseFt0QEJ5Ul85actApzj5ycWl4wMIebBSr9pV-BtlRr8hlYSfdy77VajoyupDV10avWsfs_4OinG-tZYk2lsGECe53EWwY2y-Mk9J3HBwZz2Kb3EIoxs8ICSrBnBNZXtMM5_vHIet1-Q6DJSR1bdahcKVmqQJjPU1IEWjBwvPaG0U6dxyv-SGfxtZT2oq3LJDYNDNV82X6-vb2Cp_uYnLlj9A-qrs-fo4bChkzcTxZU_Vn8Ecs2GhMwdBx1nbxaWTCtsoxv3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/458432" target="_blank">📅 00:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458430">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5216002f80.mp4?token=ITLzh91UhVZVN-sLkf99BkASAP_Mz73yeEaMqMcsb8uxOUJ7rPtIZdpP4IdXid9wtAaXKZdsgRZ8oRghy5pUr3DRIMLtzbQcb9AF3ytRhHt7eUhkn4CgkrKDtCyaUwacThEymFbYp6cRi2h0xosPU017TqL9FxvBs8u_e2vwUH90-7u5lZ9hpVmMkcq-3mzUWpkI52YL1ErfdkbuxKikIscP-1WthNstiVm81V8nFKYvLYXESKp_DJWMkEawsIc87ABY8hqVy_YBXgrEO2Yt84YhSxPL6OuadOBmjHF6aQB8O8ht_RyhyEkPyF4teKnuDIKYqBX3gvs0OVsR6Hu_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5216002f80.mp4?token=ITLzh91UhVZVN-sLkf99BkASAP_Mz73yeEaMqMcsb8uxOUJ7rPtIZdpP4IdXid9wtAaXKZdsgRZ8oRghy5pUr3DRIMLtzbQcb9AF3ytRhHt7eUhkn4CgkrKDtCyaUwacThEymFbYp6cRi2h0xosPU017TqL9FxvBs8u_e2vwUH90-7u5lZ9hpVmMkcq-3mzUWpkI52YL1ErfdkbuxKikIscP-1WthNstiVm81V8nFKYvLYXESKp_DJWMkEawsIc87ABY8hqVy_YBXgrEO2Yt84YhSxPL6OuadOBmjHF6aQB8O8ht_RyhyEkPyF4teKnuDIKYqBX3gvs0OVsR6Hu_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع عراقی از حملات هوایی به مقرهای تروریست‌های ضدایرانی در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/458430" target="_blank">📅 00:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458429">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">منابع عراقی از حملات هوایی به مقرهای تروریست‌های ضدایرانی در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/458429" target="_blank">📅 00:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458428">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">طعنۀ یمن به ائتلاف دریایی عربستان
🔹
وزارت خارجۀ یمن: امروز برای همۀ جهان روشن شده که رژیم سعودی بدون هیچ توجیهی، آغازگر تجاوز علیه یمن بوده است.
🔹
رژیم سعودی، در چارچوب سیاست‌های احمقانه، با صرف میلیاردها دلار مجله‌هایی خریداری می‌کند و با پول بلاد حرمین شریفین، در پاریس و دیگر شهرها شهرهای بازی و پروژه‌های تفریحی می‌سازد.
🔹
ما همچنان خطاب به این رژیم تأکید می‌کنیم که صلح، کم‌هزینه‌تر از برباد دادن اموال مردم این کشور برای ایجاد ائتلاف‌ها و خریدن مواضعی است که از اقدامات جنایتکارانه‌اش علیه ملت ما حمایت می‌کنند.
🔹
شایسته‌تر آن است که رژیم سعودی، اموال بلاد حرمین شریفین را برای آزادسازی مسجدالاقصی و دیگر سرزمین‌های فلسطینی، و نیز احقاق حق مردم یمن به‌کار گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/458428" target="_blank">📅 00:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458427">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cb43c720.mp4?token=afmu9wWjo25XYY0xZqRY_azHe0mMsFGyGWBqfw8MG_gVI3RMnEkAtfhkYM3nDxd-4J1qtYmaBfniFfsvHf7KnFK1c6nL-p4ybyUNTSRpMf5QXj0GeEESYOetw5_noCZzJDBGyHH7vsuEkxfe3MlCncFC-Hv6S4gVXd_x4nX68yDscpuQc65ZVTPzWV3GKNkjl6_sBJisHKdgIhUKmVF4em900cM3f7LttaFnI2avnReY8V9cMJEePzxyZ-blO99yuUfEH24BUkwwqhYSYs6z810Dx52tY4vEYUrpjnbFbwfjwVQjUMMXCiDetU-FaF1qgTxcoJDJqZmsL6rv306bqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cb43c720.mp4?token=afmu9wWjo25XYY0xZqRY_azHe0mMsFGyGWBqfw8MG_gVI3RMnEkAtfhkYM3nDxd-4J1qtYmaBfniFfsvHf7KnFK1c6nL-p4ybyUNTSRpMf5QXj0GeEESYOetw5_noCZzJDBGyHH7vsuEkxfe3MlCncFC-Hv6S4gVXd_x4nX68yDscpuQc65ZVTPzWV3GKNkjl6_sBJisHKdgIhUKmVF4em900cM3f7LttaFnI2avnReY8V9cMJEePzxyZ-blO99yuUfEH24BUkwwqhYSYs6z810Dx52tY4vEYUrpjnbFbwfjwVQjUMMXCiDetU-FaF1qgTxcoJDJqZmsL6rv306bqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
عضو دفتر سیاسی انصارالله یمن: دشمن سعودی در کشور ما جای امنی برای مزدوران خود نخواهد یافت.  @Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/458427" target="_blank">📅 23:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458426">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWsCNM5dtAcjHYznUGH7SHHHSnx59xwdCoN0OFf5cFv9Qa8JsAebsihkvGrNDaflI3QqRz7Kc57cWbDZnp-_-qrfnnNIh7cTL87KoJ5J5d5xaUpu2ofR8B28gLpN0EIsEsDhgUGW7vqzsFsKousXQ9WbnSCTkOfoMMkv_D-6e2YykcjIzpSD5TXVZuVAN4jcL2AzGz9Ac1ueyaN_f5QQ-HfWmlWytMkm2AcK_IUBvTTa_hmE0LG07EC8CbPwgyRf7jEtTheXZHw8dqEX5lOrD-aALNJ7jNoJ-pkB0Nhw73fjjrsf-IbdpxGaJ6D2-cmAE6SclDw7IxXy8y1Vzuq6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عضو دفتر سیاسی انصارالله یمن: دشمن سعودی در کشور ما جای امنی برای مزدوران خود نخواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/458426" target="_blank">📅 23:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458425">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJ106wOkdVJG3udkQol7yalYrdSSNyW8CZY-w4i6Kh2S9cRS85BS4vFc2lEsvJkrTSexP0wwl7hpxCBhWZOOJUkjBgq9yT5m-Tlos7oqmVpalH6BaEFUc2VGP8AeKzfpsNUYyuMU2j7sPtZ-uQfVTILx-b5nJFC32RgzyFoYVbzXeXffKwzq0PnH-hgtbCWObbXi3srnDxPQlFpqKSRX-XRQLY7OnqAkzEmEyxwAR69zZmlW5duxo7RJUA4qjCmJCZsROyloDmSmDmb9X84MznZcyKs66Ofb8m2X8vB-jjEv0-xy3gEq9aP1zv-EAx2n4aGxE8iscqrKECIZw2LZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقایی: سیاست آمریکا علیه ایران به یک نمایش کاملا مضحک تبدیل شده
🔹
واشنگتن به بحرین متوسل می‌شود؛ کشوری که عملاً هیچ مبادله اقتصادی معناداری با ایران ندارد، تا ثابت کند «ائتلاف» آن در حال کار است.
🔹
سپس مبادلات ورزشی و دانشگاهی ایران را «متوقف» می‌کند؛ مبادلاتی که سال‌هاست عملاً متوقف و بی‌رمق بوده‌اند.
🔹
تحریم‌شده‌ها را دوباره تحریم می‌کند و خلأ موجود را «ائتلاف» می‌نامد.
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/458425" target="_blank">📅 23:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458424">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peL3SBZoERx0_eJFOcYH0aOfyKocrMBpfIBnlz_K3vwYQSJ8dqBODvrS1JaGG-J2AS3XXaxt6AmfyorvzjhieZsS29NgY4thQqIifBPejVDuVD_1N1G5FeMSNzMEKm_g68gTZ25vEhQAFCVYi4nKob4rexaoyb5j6XlUvMzzfiJzi6nQpOSmzTq-3y3_4MMroANTIbX5vhp08zm-FSizz0bSNR_4-jUk9f9DBVSpjSG1je1FKUbME0-81OvzY2-gxTfpjocasd3EoHD2L8BVR6bsJI5oY60cAQqGCNXkBchkbpiUt2-WGZJ5d00oTRUBziEkMXQyoYuhgeQmfY73Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
موشک جواب بادبادک!
🔹
پاسخ «کمال شرف» کاریکاتوریست یمنی به تهدید صهیونیست‌ها علیه غزه به دلیل بادبادک‌های کودکان.
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/458424" target="_blank">📅 23:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458419">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IkWZdiH5zZR35UMuQP7J3DfolxhrRpTfsNpV2tRULaoPWCk1cXmM8_Fawfl_3EjTbgGdgi3JmSw34sNJZpS0rxDVqOeGj0FaunB-HL5lxCG7bZjMF6d3FULzyoHdJCYwzUvgJgwEgd-N5s0iBt-03UAT__Nx1nkLFzOFbzdAM4BE4ID7LYqTbTsJito5dMP3jihosM61kLr_C_DecdkbnbDIbCUmrC4OfkfaAwizHJ80lAGuG2ggXbH44VxH5q43W33sVIr1_U6ukf2XdhwH6uysJ85vvSWPymWKuexk4gIV63TvqdPt1fQ-iMSDbZV_q3VK6Ks2icR1XuAITmFuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNN7BJFN2VAfb5gbvN3QdM40UrJkVNuiCV4QGEvvLYZig7TNbRtsglMyaQfFyuD_YSu__15pZfuJF1PCjz6pck__0j4LDSEwn-OT9inO-retPFAH4bmYFMi05UMl0oPOKl-iOXYofTlIsWUndKN9wkD_ba6OD3rIQVC9eN3BQYsahxZ6PRLDHV70yiAGbIf1C23Ce7d2s2IZBgIh33M9PpoO6pxe2XTZVIHW4bGFgakSn3gSpEulyaayLhfh8_HyhugPCcTVmeHFIM8dmTog5SwLsI5IE38U8Btp7vNTu9Ey8JLC8x-yxXeJ3x4xBcuCeRlUeHVRohWpN8O_BzRBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGfqB6uFdxnrX2x4-XAW0yt9gPyLC0BIqDVVD6-dvirrBS8nDKOPaImkpAXxvzpRQ4vqjZ6Nj5HCSGzbqRQD_UlasAP-fLMGBQhoJq5BROhGG-MDjYgXsOooCjXcut7VwdC9R_DcfdlXsKxbqxqeQyKykTt3jjPrIgvM8DlbzNtCVI1CxqZovca_Qc0pAF33jTKCFVn1l00sYDKkh18ZTbBaQY9dO3uL1HtZzs-6Kd8xpKy8qJG5PJSY6GxUzme5kC-j1Q6MkRr0uO9yN7ZnaQjwsB07u0Yn5rFkhoDxHu2CL3Q5hp2ZOs7UsaKVos07adL1SVxg58j47iD5jSK7IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EguxQI3GTSCxj_P9cKXroDryCsdyArghBqmc0hD3CDPN34P6pj84qNyQFCdKC3HNNg93SHhaw6TkKsNgSSSfxL2ry63xMFjjW9ZRDMWp8V7sUwQYHjYiAqmetYKhjLNAVALygxsNkRlYmvqWm_Nhshk-32aE3tmMy8fVbGM-PqqyYmfOXbhL_rD5CDuD1tcsdPEvPqRNXs3zsENL3eKTDpauLcJWA87HtfasQTssGm1vFzNTYMAq53xRjfAtOchi54GtDBLb4Fz-uagWtjsziUdVtK6LmR1ZmGyQX_BCFGogfiv94BVj5Wj6gbKZGNF9e4ju6vjPSnhEp3WsKP9KnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رقابت شطرنج‌بازان در مسابقات اوپن ابن‌سینا
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458419" target="_blank">📅 23:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458418">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf7a035dd.mp4?token=ct1nOwWC9qQecEaBVP9SZfrua3ZkhU-FYAEtI-40IQ1wSWlwrhaDE0eNKvNjoA33i63ZyH8BXE2HUzZHDGLQ2TqZCHHDXYnR26DQ1dleBMtllXIFAX9OzBCSnSd5aaGHdjCbFLpp8TxRMUv873qaMxV6kBgcUCTOJTfTbPoiDAWYxHWPFAS1h4MqfKLoUr1-SiEfkykP7s06PryApEQayw4Yyw7WfRA9k1LaWd8i-LT4wtptkO5JOCVwbZWPNKyW3x-bUTEQVyHHbEWx6VPtvCP0Lw5eFw-W0TiGMA0bi_O3LS1MPRM4lJRnBgE3uE5vimb7UaGHved492Imqh9ooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf7a035dd.mp4?token=ct1nOwWC9qQecEaBVP9SZfrua3ZkhU-FYAEtI-40IQ1wSWlwrhaDE0eNKvNjoA33i63ZyH8BXE2HUzZHDGLQ2TqZCHHDXYnR26DQ1dleBMtllXIFAX9OzBCSnSd5aaGHdjCbFLpp8TxRMUv873qaMxV6kBgcUCTOJTfTbPoiDAWYxHWPFAS1h4MqfKLoUr1-SiEfkykP7s06PryApEQayw4Yyw7WfRA9k1LaWd8i-LT4wtptkO5JOCVwbZWPNKyW3x-bUTEQVyHHbEWx6VPtvCP0Lw5eFw-W0TiGMA0bi_O3LS1MPRM4lJRnBgE3uE5vimb7UaGHved492Imqh9ooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط جایروکوپتر پس از گیر کردن در کابل در نزدیکی سدی در شمال ایتالیا
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458418" target="_blank">📅 22:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458417">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/962f8ad5d2.mp4?token=amJXDRps-jT4uCXCdGPgm8T0N2-qUiSfLDEJujCVMQ5ucjCfX52gmPe9QaXXEB0b1NgSFLDCzow9uXJjCwTE00mR639nbJIq3Mcx3Wfvf4sMOW-3FbQy77IOJyITnvkXhuphuyqFvgQiHFwcUPuHSelfZm6gBa-w-0rUogOl7Ik0auEClNBjF-H6_bEqICLUaEJhG1KinCDaO8V1kfqgWQky-tkqWhrqk_hmTqkWW9umwBwpic8om6LD18vXCjtV92i0O5XRU51LI6bMcFfmBryhOTcFJFZFF2GEM8pQbnSp_8TPnYDL8F-lx3sO7YJpukzYgYk3wodcmhN2Boxfow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/962f8ad5d2.mp4?token=amJXDRps-jT4uCXCdGPgm8T0N2-qUiSfLDEJujCVMQ5ucjCfX52gmPe9QaXXEB0b1NgSFLDCzow9uXJjCwTE00mR639nbJIq3Mcx3Wfvf4sMOW-3FbQy77IOJyITnvkXhuphuyqFvgQiHFwcUPuHSelfZm6gBa-w-0rUogOl7Ik0auEClNBjF-H6_bEqICLUaEJhG1KinCDaO8V1kfqgWQky-tkqWhrqk_hmTqkWW9umwBwpic8om6LD18vXCjtV92i0O5XRU51LI6bMcFfmBryhOTcFJFZFF2GEM8pQbnSp_8TPnYDL8F-lx3sO7YJpukzYgYk3wodcmhN2Boxfow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ وقوع سیلاب ویرانگر در مرز چین و نپال
🔹
این حادثه تاکنون باعث مفقودشدن ۳۸۴ گردشگر و مرگ قطعی ۲۲ نفر شده است. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/458417" target="_blank">📅 22:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458416">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42adedf52.mp4?token=Bfpg1zBlu5IQ_4YMfFz2qLc-cP_6UAsmXff8VNuB4uHpzmV6IEDqYivgxqpXAChcpjxEqJKI-iwq1nIhMX15FU2QnqRgaZ9BjN-WuHpYDkFze486obFeW3jtMGIfGm59DRxjGiLMj-Y09u0b-Yie0dFWVonhCmsUon9PhI5CEHHZvyJzi4SOr9otRetLo4lop4CQ-rb0jfSOtqJVqwhdyfJxIJrcGzyVqzu9CPoejriDrszLEexoSGbrAYuzHKLUYs0E9__EedjosrxSKzZAVcq4QD0C0cOrjYHaTSHJ1HkqE8DxH-1cs2XcusU8uWsY4CElQ4CJjB8nBMmKZnVhTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42adedf52.mp4?token=Bfpg1zBlu5IQ_4YMfFz2qLc-cP_6UAsmXff8VNuB4uHpzmV6IEDqYivgxqpXAChcpjxEqJKI-iwq1nIhMX15FU2QnqRgaZ9BjN-WuHpYDkFze486obFeW3jtMGIfGm59DRxjGiLMj-Y09u0b-Yie0dFWVonhCmsUon9PhI5CEHHZvyJzi4SOr9otRetLo4lop4CQ-rb0jfSOtqJVqwhdyfJxIJrcGzyVqzu9CPoejriDrszLEexoSGbrAYuzHKLUYs0E9__EedjosrxSKzZAVcq4QD0C0cOrjYHaTSHJ1HkqE8DxH-1cs2XcusU8uWsY4CElQ4CJjB8nBMmKZnVhTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تداوم مقاومت در شب ۱۷۹ مردم مراغه همچنان در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/458416" target="_blank">📅 22:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458415">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79725ea990.mp4?token=SrP6I6GG-76eIb0lp7_LE08Ham8rA1nSvj__TjAReC0C-H7R_--sa1lmQtdhROPxiyDkAG6OZCKnp_gJsRDY4tzpfH6xCnTCS3kMzd2p81o0AkiXaY-jyxoX20G2MyxyGc4Oqcgj5rL1BYph9SNSNKQsLZ7AgRXtDheYzWyhdCeKy2JsZpZ2cJ-06V10xquPTOejnhtM_-FrjLS2BOeW_0dS-ApNMvbV5Yy41hFKOzPGiJVkYsuvPadwg401IGlyR1RlRrFXcJuvlzi6dSyddEryScibCoi4zfINLDq7dcYuWqHCihWmZJBBxE7h3CO6euI_uKQ0UgdrwkQeJbE1SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79725ea990.mp4?token=SrP6I6GG-76eIb0lp7_LE08Ham8rA1nSvj__TjAReC0C-H7R_--sa1lmQtdhROPxiyDkAG6OZCKnp_gJsRDY4tzpfH6xCnTCS3kMzd2p81o0AkiXaY-jyxoX20G2MyxyGc4Oqcgj5rL1BYph9SNSNKQsLZ7AgRXtDheYzWyhdCeKy2JsZpZ2cJ-06V10xquPTOejnhtM_-FrjLS2BOeW_0dS-ApNMvbV5Yy41hFKOzPGiJVkYsuvPadwg401IGlyR1RlRrFXcJuvlzi6dSyddEryScibCoi4zfINLDq7dcYuWqHCihWmZJBBxE7h3CO6euI_uKQ0UgdrwkQeJbE1SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگوی سخنگوی دولت با بازمانده حمله به مدرسه میناب: همه دنبال انتقام هستیم
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/458415" target="_blank">📅 22:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458414">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca671053e9.mp4?token=b0B1zSs1uGSvhXwwbu68Z5fihMPhPU5VGoAKljw7HyUoXOjih3YrTl7mQU0t0pH_0E3UlSbHCDnF1pvKMAMsB6EZtFdBRAk_m48_ZW8WGxMr-5H0_4n3M5kXOFUbz9XwgGJ0TlRMmjZRcN7hQPp5R7sLIucXl_qQLJ5ughTWqqqe-vjjZNFrE8YFjAkEvK8DIthH5nQSlBZbd7vRyF_WXIYQFEoLdy2PMkBt6VUwe8VRSwVqZsC_Z7aD4YuwUBz4vI_7nYFuzXIYuVLr2F7LJR1Tp90K4YaEpqP5WfCEDNo3fzMAq10jUD9KAYAo52bgFKiJyNw_0pR2U9oPs8fflA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca671053e9.mp4?token=b0B1zSs1uGSvhXwwbu68Z5fihMPhPU5VGoAKljw7HyUoXOjih3YrTl7mQU0t0pH_0E3UlSbHCDnF1pvKMAMsB6EZtFdBRAk_m48_ZW8WGxMr-5H0_4n3M5kXOFUbz9XwgGJ0TlRMmjZRcN7hQPp5R7sLIucXl_qQLJ5ughTWqqqe-vjjZNFrE8YFjAkEvK8DIthH5nQSlBZbd7vRyF_WXIYQFEoLdy2PMkBt6VUwe8VRSwVqZsC_Z7aD4YuwUBz4vI_7nYFuzXIYuVLr2F7LJR1Tp90K4YaEpqP5WfCEDNo3fzMAq10jUD9KAYAo52bgFKiJyNw_0pR2U9oPs8fflA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌پرچم قرار است به‌دست نسل فردا برسد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/458414" target="_blank">📅 22:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458413">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5YgyZoqZDHwNmmztJxSu4Hxhyi5fYUdBXihyBfHTXlhG3IkSNeisJQ1et65vh82yaoE-NDInPwZAPx5jjq2-bamYXPKFIV4_SfeUeMQGs7DehFB-mEtD61J-2-qxzKEt0xrpMizhT6SrcaXH7gOde8JvtBFXZ1vUwNGQvqM74jJCHD_n_1TrmmPxqdbcBsdNfHj_Ltz1IDtzQBUaH_2g0ZS5rmlRopv6Rx9--MfUg-Cb8XOrIIvfKuigzdVfoIsP_yFNgb6XxuINsxSrgranyNwMbOfwbZtluYNhQ-U5b2jaGYLDpKpD7RzPJ_lx-BvtlI3sWFUoqwLaq3kLnl80A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر قطر به تهران سفر می‌کند
🔹
سخنگوی وزارت خارجه از سفر شیخ محمد آ‌ثانی، نخست‌وزیر و وزیر خارجۀ قطر به تهران در روز پنج‌شنبه خبر داد.
🔹
این سفر در چارچوب رایزنی‌های مستمر ۲ کشور برای گسترش روابط و تقویت امنیت منطقه صورت می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/458413" target="_blank">📅 22:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458412">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/680415bf29.mp4?token=r-yRg6Qa6TCZwliUD___PeUHRLidS473Nf2mg3lGTQXquviCVBn-yVNo9g8i0m-GTO_zvMP6Jo8JdkdGLke0g7xL4gl9W368tdSxKHAka1npK4Oci_i4Iyc6zxVzTFf8j-KA2Otth4gdiSH6Ar47D0e35QzLviSSLn1_c9cAaBf6j58UGCZBwoF2QnVRJAGua95QxvNySXXJ3V8cZy4CDIECCLO5bakMbeEB5ca6N2s4XXXO0vAVyR1kzmYBltqqP1FoE-__Vy-svuM95YVL0B2WBp7rsP8KStWqKyLXV8ooI6-cLdO9wq38KXAAfkKo-bFl43qmd030ASJOHLNiMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/680415bf29.mp4?token=r-yRg6Qa6TCZwliUD___PeUHRLidS473Nf2mg3lGTQXquviCVBn-yVNo9g8i0m-GTO_zvMP6Jo8JdkdGLke0g7xL4gl9W368tdSxKHAka1npK4Oci_i4Iyc6zxVzTFf8j-KA2Otth4gdiSH6Ar47D0e35QzLviSSLn1_c9cAaBf6j58UGCZBwoF2QnVRJAGua95QxvNySXXJ3V8cZy4CDIECCLO5bakMbeEB5ca6N2s4XXXO0vAVyR1kzmYBltqqP1FoE-__Vy-svuM95YVL0B2WBp7rsP8KStWqKyLXV8ooI6-cLdO9wq38KXAAfkKo-bFl43qmd030ASJOHLNiMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید اسماعیلی بدون از دست‌دادن حتی یک امتیاز قهرمان تورنومنت کشتی لهستان شد
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/458412" target="_blank">📅 22:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458411">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e776ed28.mp4?token=ezrVXfOhQwobSQlobccycU7BFqR1tTFZkMUZUVPtH15yRQWjC9uoYaXmhFQAUIkljjqSYsh8rUaYsNivgHQcmvHO7ZOFh5HdV8SDQy3zXOXUf4aSKepSup4HhZkx-ColjP5DclcbeIREd0earbqazxqiyJuvK7ToPj4_1UmSlsxAw9JAB6h_XwFZzgHaFSIS5WS6xo_pipWCMGwiL5aZM20VOgHxu2YvVOe4ezIa1dGSdki7GP8dwCcGSXrhyI2x3On4xEZJTYb5AphtBm5sgZYsjvec5JEYP1amzOe_sT8FfpRjODKjOKovSuDvdFtugmGdg3vpUicX8hTaes0dgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e776ed28.mp4?token=ezrVXfOhQwobSQlobccycU7BFqR1tTFZkMUZUVPtH15yRQWjC9uoYaXmhFQAUIkljjqSYsh8rUaYsNivgHQcmvHO7ZOFh5HdV8SDQy3zXOXUf4aSKepSup4HhZkx-ColjP5DclcbeIREd0earbqazxqiyJuvK7ToPj4_1UmSlsxAw9JAB6h_XwFZzgHaFSIS5WS6xo_pipWCMGwiL5aZM20VOgHxu2YvVOe4ezIa1dGSdki7GP8dwCcGSXrhyI2x3On4xEZJTYb5AphtBm5sgZYsjvec5JEYP1amzOe_sT8FfpRjODKjOKovSuDvdFtugmGdg3vpUicX8hTaes0dgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تخریب منازل مردم لبنان این‌بار در شهرک بنی‌‌حیان
🔹
ارتش رژیم صهیونیستی در تداوم سیاست تخریب خود، چندین خانهٔ مسکونی را در شهرک بنی‌‌حیان واقع در جنوب لبنان با خاک یکسان کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/458411" target="_blank">📅 22:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458406">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OX99yWhPAi8gbctPmLhKAVE4qovY4tXUzENEH_yer3p8MlNDkbTazsRlYoNTIg85o61v7sMFshFjooceM3LlW7ILcOOUsC4nqT5EsVjjeNqTIU6_iuTxl5u_149sZ_GvJH6FQs4wawsT_egpAsNvdsMGBGhpQEug-r9ioEQPGwoyreRRcHGz3vAWRtOdA8GLAO2cmBKUi7Jz3yGX0rQmXSCsV2cw1imaqqSkORA_ri-iSPpURlEXrqVH0fTcB0GfwM5IywJRjio-i_1118caxeSDH7Rwr1sseVMHuMyO2-HdRMcyko0WY78IdUQImvi16jet-JSsP__kgYmjCb-ung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PEpR0pYyN2dSTLRvcaFYeBLFIj7XGS4qe8jtXh4W1ZSaqtCzDGuuv036aGg9K1TOEWl2-pwNHE3GNztQt72I-CLbRTf16pNnDBckMXWJ_utJ05984AcNfkRUijYeNl9CDiUW47neSdKal7NMK1w91-EhMe7vQa15VjhymWm6eD-pjPNpDZwygGlzmJbp6FQsW7JGmYoPItLxYSI8TVVEyrrHHMECTHcd55iiyzOf08KMIY9rxUebKsMnXeZeFlLatwbQjhJn_e42LSeecsp8YJZ--2YumaFUINKT3YYtDh66Y2R-Z-dDozDxPUBwUogN4NKDW2mVoqg0X_vavs4ubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqTOk3pLlCxI-NoKxa3oKxwWfXAxgkUm0sGfF9xbyasm37W1YzrVliVEgM34LTU54tLY5aGY4MVjpmwpKVbqdx_d7QWmPWxvdI6LMBBcyc5XhIN1kV6hGq820e2mZorDjrdh5B49pRo6YJGLSg08KG0c4oX01tT8JlM5hQ6MTZNAoyyCJZ4uT12JSPLbyFFclgloH0kPr04fsmUPPewbsVw0YC30oMM7LBMKwBqE3uH4pz0GKig0gIvUN4sBoWtqTfnLoBOUTNMViW3Y86fU3isIBMLjt-L48rE8fQM6YctyZGZJi6Tf3RpS1Stl4_c71jzTmJKqwdAOZ_S_CcbNlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CeVESB7SOQCs-uT387DsoY9-W7DviqVoDkNGvFi5oKbDUpMXfuKIE-9yiW6QCipumraX463SYCnElkBzPnOxGy5ApaKnStdoZPppxYORLrGbiX0pLR4T7Fct9n5IyO7A-62d1qHaUYGWAlAHLblppqg05ksJYcQXSUPXdYoM55ZxAB0Q3wY29nh8Wm2wx9-gIdqQdgX4tEVgYh424viUuBsSLlPTF16yDL6-keWQIlqF_fAPFO16ExQlj3Rf8lj2LnjSTnosJee3Xrnpvg8Gf3C5OqZHb85O1jQR-Ymv62F6oUSxJe6lPCfxysgkMdGCvw0JAlZbjtICPgG7QRWONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDdC0QTccbGmZQ1bNSenaZuIRdPEu2R_fKFtXIUHAFtBKUJeSqKGlolY5Z4DCbde3cRlg_n_UHlwKTqBZkk3E02H92mdR519qYGNRVboqGRlZzkDBmVGCmAe_AQ3rib2Tnp8ssUdiBHBLaTEvH365F2J84XtjhyCTu7-2zg0wSJUCjcbNAsXWZy3Yh6zVA_lSh8L7aHQmDVQ7zCBYX9EFRC4ccsSeJe_EjLogWvuug7qbKeUpremKS8afSRyg773lPN7RdCbeDaK6cJU6nv1LpMOLOO0Fm6rHcP7P0ySf7eYD6liKYKfihfm2Fn6nBtMNU1NrAXFmlkheZhMkwDlsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
تصاویر دست‌نوشتۀ شاعر معاصر زنده‌یاد مهدی اخوان ثالث که سال ۱۳۴۱ در دفتر یادداشت رهبر شهید انقلاب اسلامی نوشته است
@Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/458406" target="_blank">📅 22:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458405">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c667f381.mp4?token=wB7hb9NiwTeKNCfDydK1BJHwYfjgOQB4z2hwuQ-KK4gMeLjhtfdJzDvYYHMiWxMZFeOeKhXR1mVG2-OKXzMcv-P5dqGR0q_QKX3wRO7c278jLZFRHjeTu7D38PZUDmvQH3NpIJjPnUDjyF4KAXBscMVhRSVu7bAsO0yIbvjG9EEQMTSBbO0m0R884MKgrag4lamL7DJ4ggt5vPAtgOxZRRo0qVHRfV7kD1Xh-HWa4psXTFyDfwFpvMMkOSQ_gfZGK-CwTxDQAAWQ-p_Yj2BmDh_7syveE5KfJHmgiKICDF06oFSU8-qXcowLq3rWyOi54wXOUX8efYSFdDrBqMx8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c667f381.mp4?token=wB7hb9NiwTeKNCfDydK1BJHwYfjgOQB4z2hwuQ-KK4gMeLjhtfdJzDvYYHMiWxMZFeOeKhXR1mVG2-OKXzMcv-P5dqGR0q_QKX3wRO7c278jLZFRHjeTu7D38PZUDmvQH3NpIJjPnUDjyF4KAXBscMVhRSVu7bAsO0yIbvjG9EEQMTSBbO0m0R884MKgrag4lamL7DJ4ggt5vPAtgOxZRRo0qVHRfV7kD1Xh-HWa4psXTFyDfwFpvMMkOSQ_gfZGK-CwTxDQAAWQ-p_Yj2BmDh_7syveE5KfJHmgiKICDF06oFSU8-qXcowLq3rWyOi54wXOUX8efYSFdDrBqMx8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چراغ حضور مردم در شب ۱۷۹ هنوز روشن است
@Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/458405" target="_blank">📅 22:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458404">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijf3Z7JLBu9QoZUP2rIH6PpZmemH5YnoIMZ2TQ6tyFOxT6As5wTnf9G1pZExaflsudSz3cK0frGhbBt3TWPwsd8O2vH-iOYPNGP7KfiVq_fr4rN1fPoIKSpuwqwrHd1WvhA5HMaOn0mGmkndcrrK--0PCG38p3FZmrbZleY19AC7U1iSvzImnuGRfCbr_RG6D-dfIiTaNwBCmCo1XwJE0wOcB5vAnPswIsQRrgWr01kGRf2hce34CLDgQxKW592Vs5qTt8_vQBivRNzWWURVoIfHijLr-Ch0Xnbpi3gYPWSpGIBeO35aJbBdMAehNE5dY4s5H2lfFQc17AqzH4BfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فولاد شادگان تا مدرسه نابینایان شیراز؛ روایت ۱۴ گام بلند «امید امروز» در گوشه‌وکنار ایران
🔸
۴ شهریور ۱۴۰۵ را در تقویم امیدهای ملی ثبت کنید؛ روزی که خبرهای خوش از ۹ استان کشور، یکصدا فریاد زدند که چرخ تولید، آبادانی و عدالت، حتی در سخت‌ترین روزهای تحریم، از حرکت بازنمانده است. از افزایش ۱۸۵ درصدی صادرات خراسان شمالی تا واریز ۲ میلیارد تومانی به حساب بیماران خاص از جیب نفت مصادره‌شده آمریکا؛ این، تنها گوشه‌ای از ثمره شب‌بیداری مدیرانی است که شکر نعمت خدمت را با عمل ادا کردند.
گاز گرم صنعت در خراسان‌رضوی
🔸
گازرسانی به بیش از ۴۲۰۰ واحد صنعتی در دولت چهاردهم، یعنی نفس گرم تولید در کارخانه‌جات مشهد، نیشابور و سبزوار. این عدد بزرگ، نوید اشتغال پایدار و رونق بی‌وقفه کارخانه‌ها را می‌دهد.
جاده‌های همدان، محکم‌تر از قبل
🔸
با حضور وزیر راه‌وشهرسازی، ۳۵ پروژه راهداری در همدان افتتاح شد. این یعنی ۳۵ گام برای کاهش تصادفات، ۳۵ پل امید برای روستاهای دورافتاده و ۳۵ مسیر برای رشد اقتصادی این خطه.
آبادانی «پشتکوه» در خاش
🔸
۱۹ طرح عمرانی روستایی در بخش پشتکوه شهرستان خاش به بهره‌برداری رسید. از آبرسانی تا مدرسه‌سازی؛ این خبر امید برای مردمانی که کویر را به باغ تبدیل می‌کنند.
۲ برابر شدن مشترکان فاضلاب در سیستان‌وبلوچستان
🔸
رشد ۲ برابری مشترکان شبکه فاضلاب شهری در سیستان‌وبلوچستان، یعنی گام بزرگی برای سلامتی عمومی و حفظ محیط‌زیست این استان پهناور. از زاهدان تا چابهار، لوله‌کشی زیرزمینی، نوید زندگی پاک‌تر را می‌دهد.
رکوردشکنی فولاد خوزستان با «شادگان»
🔸
افتتاح فولادسازی شادگان، ظرفیت فولاد خوزستان را به ۵ میلیون تن رساند. این یعنی ۵ میلیون تن استقلال صنعتی، ۵ میلیون تن اشتغال غیرمستقیم و ۵ میلیون تن قدرت صادراتی برای ایران بزرگ.
جو مطلوب کشاورزی
🔸
افزایش تولید ۱.۵ میلیون تنی جو در کشور، یعنی نان دام‌داران تأمین‌تر و سفره ملت محکم‌تر. این حاصل بذور اصلاح‌شده و مدیریت هوشمندانه آب‌های کشاورزی است.
سرمایهٔ خارجی به کرمانشاه آمد
🔸
جذب ۸ میلیون دلار سرمایه‌گذاری خارجی در یک سال در استان کرمانشاه، یعنی اعتماد جهانی به ظرفیت‌های مرزی ایران. این پول تازه، جان تازه‌ای به واحدهای تولیدی این خطه خواهد داد.
مولدسازی اموال راکد در مرکزی
🔸
۱۳۴ ملک مازاد دولتی در استان مرکزی وارد چرخه مولدسازی شدند. این یعنی زمین‌های بی‌استفاده به کارگاه‌های تولیدی و مسکن جوانان تبدیل می‌شوند؛ یعنی گردش چرخ اقتصاد با دارایی‌های خفته.
صادرات رکوردی خراسان‌شمالی
🔸
رشد وزنی ۱۷۵ درصدی و ارزشی ۱۸۵ درصدی صادرات این استان در مقایسه با پارسال، یعنی بجنورد در مسیر قطب صادراتی غیرنفتی. این عددها، نشان از همت بازرگانانی دارد که از تحریم، تونل عبور ساخته‌اند.
امیرکبیر، مرکز تبادل علم جهان اسلام
🔸
افتتاح دفتر تبادل علم‌وفناوری جهان اسلام در دانشگاه امیرکبیر، یعنی حلقه وصل دانشمندان ایرانی با همتایان مسلمان از قاهره تا استانبول. این دفتر، پنجره‌ای رو به آینده‌ای است که مرزهای دانش را برمی‌چیند.
واریز ۲ میلیارد تومانی به حساب بیماران «پروانه‌ای»
🔸
از محل فروش محموله نفت مصادره‌شده آمریکایی، ۲ میلیارد تومان به حساب هر یک از بیماران پروانه‌ای (بیماران خاص تحت پوشش) واریز شد. این یعنی لبخند بر لب‌های خانواده‌ای که هزینه‌های درمان، دغدغه روزانه‌شان بود. نظام اسلامی، جبران دشمنی دشمن را به خدمت محرومان گره زده است.
هلال‌احمر در میدان خدمت
🔸
از هفتهٔ دولت پارسال تا امسال، بیش از یک میلیون و ۸۰۰ هزار نفر از خدمات داوطلبانه هلال‌احمر بهره‌مند شده‌اند. از کوه‌پیمای مفقودشده تا زلزله‌زده دوردست؛ خیریه‌ای که همیشه در بالین سختی‌ها حاضر است.
۸.۵ همت برای هنرمندان صنایع‌دستی
🔸
پرداخت ۸.۵ هزار میلیارد تومانی تسهیلات به فعالان صنایع‌دستی در یک سال، یعنی سفالگر لالجین، منبت‌کار اصفهان و گلیم‌باف کردستان، صاحب چرخ کار پویاتری شدند. هنری که نه فقط در ویترین‌ها، که در تولید ملی می‌درخشد.
مدرسه‌ای برای فرشتگان ناشنوا و نابینا در شیراز
🔸
بهره‌برداری از آموزشگاه ۱۲ کلاسه دانش‌آموزان با نیازهای ویژه (ناشنوایان و نابینایان) در شیراز، یعنی عدالت آموزشی در معنای واقعی. این مدرسه، پلکان ترقی کودکانی است که با اراده‌ای بیشتر از بسیاری از ما، مسیر علم را می‌پیمایند.
کلام پایانی امید
🔹
به قول مولانا: «شکر نعمت، نعمتت افزون کند / کفر نعمت از کفت بیرون کند». این خبرهای خوب، نشان می‌دهد که در میان هجمه‌های خبری سیاه، صدها دست خستگی‌ناپذیر در گوشه‌وکنار این سرزمین، مشغول روشن‌کردن چراغ‌های امید هستند.
🔹
ما در خبرگزاری فارس، قدرِ این نعمت‌ها را می‌دانیم و به سهمِ خود، این قابِ درخشان را به شما تقدیم می‌کنیم.
🔹
شما هم اگر خبرِ خوبی دارید، برای ما ارسال کنید تا منتشر کنیم. ایرانِ خوب، خبرِخوب می‌خواهد.
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/458404" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458403">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a762289db.mp4?token=rx7Vg_g3Z7kiozh2zTTTPBN75TnY09F17s8sIir5EydEP1gWeVfOhvXvohv2h8g8lxlxPPE2R0m7-FWMYHDwyGS-6n2xGN6Ah1ncCwT_gBx3cu1gOpmN1I51Zv5K0yIdspHB5jVWMpK_q9FbC1JHLB0tVCCZMaoNlMjwGJAy05bUMXbu-XpunY6b8SpZNluHcJwqawMuGUcOvoBGoAet290KoBBCew0o8jpuP4gTAkaBri-HWe9nQgusSJ9_pkP3w6yi_TaixrqVmS09DN5Sk3mClEgfXaEuPnOdlPqHGwEYUm-5co4b2DngHgX1-oKjKReXxj6Ry_rh759WkKsV9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a762289db.mp4?token=rx7Vg_g3Z7kiozh2zTTTPBN75TnY09F17s8sIir5EydEP1gWeVfOhvXvohv2h8g8lxlxPPE2R0m7-FWMYHDwyGS-6n2xGN6Ah1ncCwT_gBx3cu1gOpmN1I51Zv5K0yIdspHB5jVWMpK_q9FbC1JHLB0tVCCZMaoNlMjwGJAy05bUMXbu-XpunY6b8SpZNluHcJwqawMuGUcOvoBGoAet290KoBBCew0o8jpuP4gTAkaBri-HWe9nQgusSJ9_pkP3w6yi_TaixrqVmS09DN5Sk3mClEgfXaEuPnOdlPqHGwEYUm-5co4b2DngHgX1-oKjKReXxj6Ry_rh759WkKsV9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک پلیس به سارقان موتوری در رباط‌کریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/458403" target="_blank">📅 21:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458402">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53f1e4c1e.mp4?token=tj6mtAj5690ObNrHeQbCUe27SMfg1U8vqMYQfO1tXqDRrn-ezcWd_T3DVLr8y-ZfjfFufUaDe-9pSzZ7TEvb6pX0dEM10dt17lIrYZZETEjrNKuJ189ODQdgm3kM8H1ekw2ADpDqdy8Kws-azBN85Uj974S6aqtVfDPSohjkf6yync7_RWOgJTTG9D_j1RnS02yDW5H-Y13Gh36xyLNKSgm1ICV0aR_VRjemqcptLLbSJdreNHPyA_gKQ5UcLd-d9x_FClind4H5uCycFV2Aixx6IxmlQ8ogzmZQ22iwM2PSpZbFuprLi9F7EdDkxm-0uVI6SplEvcLcrOuOqgeSiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53f1e4c1e.mp4?token=tj6mtAj5690ObNrHeQbCUe27SMfg1U8vqMYQfO1tXqDRrn-ezcWd_T3DVLr8y-ZfjfFufUaDe-9pSzZ7TEvb6pX0dEM10dt17lIrYZZETEjrNKuJ189ODQdgm3kM8H1ekw2ADpDqdy8Kws-azBN85Uj974S6aqtVfDPSohjkf6yync7_RWOgJTTG9D_j1RnS02yDW5H-Y13Gh36xyLNKSgm1ICV0aR_VRjemqcptLLbSJdreNHPyA_gKQ5UcLd-d9x_FClind4H5uCycFV2Aixx6IxmlQ8ogzmZQ22iwM2PSpZbFuprLi9F7EdDkxm-0uVI6SplEvcLcrOuOqgeSiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان انرژی هسته‌ای: در زمینۀ گداخت هسته‌ای وارد فرایند قابلیت‌سازی شده‌ایم
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/458402" target="_blank">📅 21:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458401">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1JnJMpKHpSaEWSqKrh5VkW7WcaToYSmccPFdlBbkVIe8ea-cA4AZtanf5y-9Q7EsYIz4ym_avN6iOp-yb-KRdQ416CaqLvWXOQMt6KegKkg3B_rTFbYGWmroACigkFhW7a5fQFtX-4UJa7vek2q4-ySVN2mneHWu6f-EABvnY6nmNuWEx9AtYyM8Z4bWKeF7Adb6Yt7x_jlivBYargwj7TJk0QYFXdnm5UA5WB17MtukzXeW1tBV62DuQGFr-OBe3NIO9xnXgT7_eIAMpHpHZP-_n4GD8b7DvW7BX5DplciInwh3XhCPZE6Puig_qLeoXdLSflD6CaPF7Emvik4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: رابطهٔ راهبردی ایران و چین به اجازۀ هیچکس نیازی ندارد
🔹
ما از موضع اصولی چین در رد تحریم‌های غیرقانونی علیه ایران استقبال می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/458401" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4xryspUEpPOzg_WiGV9XHRs_YaNFXUBJIek_Ka6nWN9GB6gt_2fz04TaxpCU74xp2udP7BTSVimAVbYDY8oYje466DkctQA7qjeayumrnP297G-QbvcVPir2dpJd9OjYPI0_uvz5pb4R6xN0vS0NpROsQXV47uXMr7lWbADDS-Y6_M5IMK2Sj_ar6Uft6ca7qSlwsZTF7pgq9RXURt6HTkrhlNL9TWo-cMJD3vLmZLOaBvYE5FsO2DpwDfRVZfvcj3QAzcAQxq9lcI9_8blqlrbE-Uh2THT0w1mEihUWJn6v8avgN9fEurvJz03ElEMC9Vpvtv6C-JPa_ddOJb6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حراج بزرگ غلات در روسیه و فرصت طلایی برای ایران
🔹
بحران صادرات غلات روسیه درپی حملات متقابل اوکراین و روسیه به تأسیسات بندری دریای سیاه، صحنه‌ای نادر و متناقض را رقم زده است.
🔹
درحالی‌که قیمت جهانی گندم و ذرت به دلیل اختلال در عرضۀ این ۲ کشور به بالاترین سطح خود در ۳ سال اخیر رسیده، بازار داخلی روسیه با مازاد شدید غلات و افت بی‌سابقۀ قیمت مواجه شده است.
🔹
این شکاف، فرصتی غیرمنتظره برای ایران گشوده تا از طریق کریدور شمال‑جنوب، نیاز فوری خود به نهاده‌های کشاورزی را با هزینه‌ای به‌مراتب پایین‌تر تأمین کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/458399" target="_blank">📅 21:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458398">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c442925a09.mp4?token=ZbcdUc6UhsRLmJA9HC7a7FwU2J9amEMjaWJcy5qI4XKZ2W_bax8JtN7w2TipeMk2FsxeqRvsCg7GzAkXB1xsUea9F8ktMcGhhYCX0cnkFNUDY7tG9ClLbGrJ6F0TySe5oTFIxy-NJbf3IGuOpd-puoU0SQsVCCnlSbOYZModq1bNYB0EklaVq-wJA4lRzCfnEgsQDYsV8cJHSMYxdkUNdzeKHQKw1KlyKQmKLLRMPRNwgILre6f5aIoaND8fYfzjQJYe3wbb_lZjMQyPfYH7xUL6n7qRFYfGwV8sUb_B59K9bkV2VBD3g2H4r39Qr5wLtv2s3QYnPufQyd1_XsTBGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c442925a09.mp4?token=ZbcdUc6UhsRLmJA9HC7a7FwU2J9amEMjaWJcy5qI4XKZ2W_bax8JtN7w2TipeMk2FsxeqRvsCg7GzAkXB1xsUea9F8ktMcGhhYCX0cnkFNUDY7tG9ClLbGrJ6F0TySe5oTFIxy-NJbf3IGuOpd-puoU0SQsVCCnlSbOYZModq1bNYB0EklaVq-wJA4lRzCfnEgsQDYsV8cJHSMYxdkUNdzeKHQKw1KlyKQmKLLRMPRNwgILre6f5aIoaND8fYfzjQJYe3wbb_lZjMQyPfYH7xUL6n7qRFYfGwV8sUb_B59K9bkV2VBD3g2H4r39Qr5wLtv2s3QYnPufQyd1_XsTBGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از ۴ دستاورد صلح‌‌آمیز هسته‌ای
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/458398" target="_blank">📅 21:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458397">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a4a84f53.mp4?token=q4DOyludtbU7L4N8I3VOO7H68J3FYiLddUE9DMrXR1-Eye4-b45HOlTuwk-3MDQksPhOyJmIG0W6kTKG8P_jcZJZcEI96glWwlnzLeH48aLmxZu8ve_BWiSVuGBZejRFH1cecGwD9GhHAH0PKQdvd0UsBjGFmHAk5sv0ExgyXyd1tCe1b-tqbOmPQwpVUmeyE4NA_iHuw7_zXstt0eSyWuykVVrgrFBtUQVeV9mkYIWtMmjSyzTRRfV2BjPbv5Xkf1PMYK1WSpqyexecHDsf27FOBqa_U9dx3M6KwpNmjrYK-gF_wIJJs6L6EK_Pq1qrU3h5oaE7s1y_XR-qB-QFTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a4a84f53.mp4?token=q4DOyludtbU7L4N8I3VOO7H68J3FYiLddUE9DMrXR1-Eye4-b45HOlTuwk-3MDQksPhOyJmIG0W6kTKG8P_jcZJZcEI96glWwlnzLeH48aLmxZu8ve_BWiSVuGBZejRFH1cecGwD9GhHAH0PKQdvd0UsBjGFmHAk5sv0ExgyXyd1tCe1b-tqbOmPQwpVUmeyE4NA_iHuw7_zXstt0eSyWuykVVrgrFBtUQVeV9mkYIWtMmjSyzTRRfV2BjPbv5Xkf1PMYK1WSpqyexecHDsf27FOBqa_U9dx3M6KwpNmjrYK-gF_wIJJs6L6EK_Pq1qrU3h5oaE7s1y_XR-qB-QFTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فن گلادیاتور ایرانی اتحادیه جهانی را به وجد آورد
🔸
اتحادیه جهانی کشتی یکی از فنون تماشایی کامران قاسم‌پور را به عنوان تکنیک هفته معرفی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/458397" target="_blank">📅 21:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458396">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tmyuw7yV12TYq7TXj46LKvIREYWVxynzBEZnBzUmqM5raBnr33e-wqQa8CD3GSvI5J6Z1w7yghEDXHVzHS0_uPLASmdMNbCKsBcvdxUGiSJVQLzIGOlKbFRtn5RzO0o_tZhjqrS7gdh1khdSp3qswJ6Qp8ZM5rARAfcMiEBesFjSYJhmvh9hDVbq1OHWvcgGG5yPW_i76BSP09gPbEE2PaU6uMWyvHz9nNqiGRvBSQbFP6qD6pbS-iZ-xPvjfsZiDt-PpsY_Oa58M3H5HXZNXfOsvtHlfFvvw0YfmYA0DBdZZ6-NXczKtTpNimz_rSdFCFGbiDBPlqYCH60qXg-XyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور: توزیع بنزین در کشور عادلانه نیست
🔹
قائم‌پناه: طبیعی است باید تغییراتی در نرخ حامل‌های انرژی انجام شود اما میزان و زمان آن را باید در گفت‌وگو با دست‌اندرکاران تعیین کرد.
🔹
توزیع بنزین در کشور عادلانه نیست؛ فردی که چندین خودرو دارد از یارانه استفاده می‌کند و افرادی هم که خودرو ندارند از این موضوع بهره نمی‌برند.
تداوم این مسیر غیرممکن است زیرا تولید بنزین کفایت نمی‌کند و با محاصرۀ دریایی آنمی‌توانیم بنزین وارد کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/458396" target="_blank">📅 21:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458395">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/292d37aefa.mp4?token=HXKtC13iR9A995OXKx6XmQouL0oqfA8LstO7mN25xjFFrdmli2NAbkhyANdDfQ8_2eKC4PJeyEluMSM4C0t8orZd7J038xRMNc-hFJxQfHuESHWMul-XJE7ROLs0Bz_lbm3iOyD2KZjFzM6Zf-KcgAM7mWhhz9CS9HuknlC_-h84g7BPO1Mg-5EF5pURI1gJ3KR9n41ej2U90LZSfqMySFdIRaaeernSkegUvNa9kfTsEPtshaqFlS1lePYvoS8oYOJdS0Gnl2zM0-q8lJOMwT27GeL_FE2WJHD7mX8AUHEyqjPBarWj2xRA9W_NGCWajtyecDvWDdPRJt9wPtLPfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/292d37aefa.mp4?token=HXKtC13iR9A995OXKx6XmQouL0oqfA8LstO7mN25xjFFrdmli2NAbkhyANdDfQ8_2eKC4PJeyEluMSM4C0t8orZd7J038xRMNc-hFJxQfHuESHWMul-XJE7ROLs0Bz_lbm3iOyD2KZjFzM6Zf-KcgAM7mWhhz9CS9HuknlC_-h84g7BPO1Mg-5EF5pURI1gJ3KR9n41ej2U90LZSfqMySFdIRaaeernSkegUvNa9kfTsEPtshaqFlS1lePYvoS8oYOJdS0Gnl2zM0-q8lJOMwT27GeL_FE2WJHD7mX8AUHEyqjPBarWj2xRA9W_NGCWajtyecDvWDdPRJt9wPtLPfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون علمی پزشکیان: مسکن حدود ۴ هزار نفر از ۵ هزار نخبۀ کشور را تامین کردیم
🔹
رهبر شهید سال گذشته از ما خواسته بود برای نخبگان مسکن تامین کنیم. @Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/458395" target="_blank">📅 21:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458394">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfOOrVcQO15uEOZVIVhbmtBAtS3XGS-fzNUaerY-VcBoByxJ2AM0W3Pz8Fw4J5a7KazBPqd3iMWKPiupbfAM2wBK6MSouleYxHf4BB2pnTeR99rWYOI9BZW7swdnWsjUtnrC_k4v9dYuOmS47KhX5TZPAvAP5VHfvzlxdMn70y-zDbr8kVYF6CTH5BmHs7TfvPgxZ7zmV1OyagVTI6uVzVVzm40IJEocSZi09OqyLK1HNVHiESSs-jnFf1CVUggsfsCJV_6hy4IZ_E7hSF_o1eIPdiPHny9txKMCi8FgQY-2zvx2ExRKIKc6p1sMpoOPhq-QtW1DpN8qZgpvnr-Fsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: مذاکرات اوکراین به بن‌بست رسیده است
🔹
بلومبرگ به نقل از سه منبع آگاه نوشت که روسیه در حال آماده‌سازی برای تشدید حملات به اوکراین است، چرا که به این نتیجه رسیده است که مذاکرات برای دستیابی به توافق صلح به بن‌بست خورده است.
🔹
به گفتهٔ این افراد، روسیه در حال حاضر در حال بررسی تشدید حملات موشکی بالستیک به کی‌یف، پایتخت اوکراین، و همچنین اهداف زیرساختی در سایر شهرهای اوکراین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/458394" target="_blank">📅 21:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458393">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fc5615cd.mp4?token=tWwtaRqk2P4u0_Gmr4_Lh0R-Z4tc_5NX00Zkj54kJe03ULOQALCTo1OgGJd5hYQvKJO-8ECQ3zb0oksPrK1M3ZSa0G4sjJYfODiuPHl4qqrVIpkVukzpYLBr4NqbpOyHeiOjnDQPJJ2TelJPls13g8c7XFHz4-cKk1KmVQnRLxVBWQalVJbHZynKgJ-8sstrizd_aKiBkC6eyUWsT5dMncBM4TIXrvncaDzu9YEOK55jtvq4TyS0rYWWVFIyzhB9dI_46YATPZWV1jYD7-vwYW4uP27dq5RCXGyTSnPRNxQvc1Ez_72gFqtaAyHgePFeJzeL4RKrqNwK7bJQF37RiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fc5615cd.mp4?token=tWwtaRqk2P4u0_Gmr4_Lh0R-Z4tc_5NX00Zkj54kJe03ULOQALCTo1OgGJd5hYQvKJO-8ECQ3zb0oksPrK1M3ZSa0G4sjJYfODiuPHl4qqrVIpkVukzpYLBr4NqbpOyHeiOjnDQPJJ2TelJPls13g8c7XFHz4-cKk1KmVQnRLxVBWQalVJbHZynKgJ-8sstrizd_aKiBkC6eyUWsT5dMncBM4TIXrvncaDzu9YEOK55jtvq4TyS0rYWWVFIyzhB9dI_46YATPZWV1jYD7-vwYW4uP27dq5RCXGyTSnPRNxQvc1Ez_72gFqtaAyHgePFeJzeL4RKrqNwK7bJQF37RiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون علمی رئیس‌جمهور: سکوی ملی هوش‌مصنوعی که توسط دشمن هدف قرار گرفت را در عرض یک‌ماه بازیابی کردیم  @Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/458393" target="_blank">📅 21:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458392">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0f86b5a4.mp4?token=px2q1EgNK2oegut7iH4kmc3PJ8BZhAToZrKuQ4Rh7Ttv-uhBEcU1O8pRb6DWGeCtMpinXnsDoGOaoXHy32JUhvcSd4xqbeuFB3M3wQhVq2LngOdAxFzXrBlY8th4_R9cDThkGMHjN6abfynnmYXjyhFI5SQZYg_K3qSU7cwQFYAaQ5pO62ZPZsolu401cIH0nP0-G_Na6eG35A8kKb72srUpP89j2fi0YZrUuA44Y7gnbyUVlj5L0ltFnU4g3WzZlF9WHdV2vYamkZXcHujAdrTO8oF9qJkaCYLxm7k7tK-09TQD4VJ5kD9q_JCbG8a6P2eeDaoIPLCV7neoLbtbKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0f86b5a4.mp4?token=px2q1EgNK2oegut7iH4kmc3PJ8BZhAToZrKuQ4Rh7Ttv-uhBEcU1O8pRb6DWGeCtMpinXnsDoGOaoXHy32JUhvcSd4xqbeuFB3M3wQhVq2LngOdAxFzXrBlY8th4_R9cDThkGMHjN6abfynnmYXjyhFI5SQZYg_K3qSU7cwQFYAaQ5pO62ZPZsolu401cIH0nP0-G_Na6eG35A8kKb72srUpP89j2fi0YZrUuA44Y7gnbyUVlj5L0ltFnU4g3WzZlF9WHdV2vYamkZXcHujAdrTO8oF9qJkaCYLxm7k7tK-09TQD4VJ5kD9q_JCbG8a6P2eeDaoIPLCV7neoLbtbKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا تحریم کرد؛ چین راه خودش را رفت
@Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/458392" target="_blank">📅 21:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458391">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
مصرف بنزین خودروهای دولتی زیر ذره‌بین
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/458391" target="_blank">📅 21:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458390">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20b3dbec1.mp4?token=CN8VrOB_RXnt2MWb-JusLzCi_x1zz2ZG7RalpwH3hRA1mcWGihK4sy3Lnq2rz4eejQmSdglV4it-Y0cehswBjffWPP4-FBVZ4Sdz6DbmmM2wfTk3AINs-vx2uEXICH5e8kCKLBwrRj6I_x7ei9b9nDX2as5tjf4EnhkvwFJafAmHYMukNyHxxXe5EQ_pb6dqU9VuTHlAg3fBs_374U188GdH5lphrq5HK-Ajh08obbz4ZTs8-ub7TxNacaAlZKZOlsKYFiZEzy15BiqUlPOYT7MQ3dZavLZskIjGrLUJCCJWrvlyZHAg31AEiD6JMBGuSkZGMW9HWbs-jMvT-b4A5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20b3dbec1.mp4?token=CN8VrOB_RXnt2MWb-JusLzCi_x1zz2ZG7RalpwH3hRA1mcWGihK4sy3Lnq2rz4eejQmSdglV4it-Y0cehswBjffWPP4-FBVZ4Sdz6DbmmM2wfTk3AINs-vx2uEXICH5e8kCKLBwrRj6I_x7ei9b9nDX2as5tjf4EnhkvwFJafAmHYMukNyHxxXe5EQ_pb6dqU9VuTHlAg3fBs_374U188GdH5lphrq5HK-Ajh08obbz4ZTs8-ub7TxNacaAlZKZOlsKYFiZEzy15BiqUlPOYT7MQ3dZavLZskIjGrLUJCCJWrvlyZHAg31AEiD6JMBGuSkZGMW9HWbs-jMvT-b4A5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاور راهبردی رئیس مجلس: اگر از تنگۀ هرمز چند میلیون بشکه نفت عبور می‌کند، چرا آمریکایی‌ها همۀ دنیا را بسیج کرده‌اند تا از ایران بخواهند تنگه باز شود؟
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/458390" target="_blank">📅 21:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458389">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/306bb628a8.mp4?token=t0X6LyOLscEGfLr7S1VGONuQUo2eZ1aHmmy7nzT5luZMWBI0-1sC-4BdveO1-bAQ1DiNLf8ZWdYM2fCczKj2uQxQnmltijx1b0cfQxOihJYcm4nzr6_fCfihKQP68Zwm7dg2CDMEDIqxR3cn5pxSn_nhcmzvcKWg5702ExnJ3ZUgKdIr9_0O4xhCRJ026VV3LJZunrRT_V-FWf9lkyevQ6IleMJjEMZKWANNzyVlMRSFvwz395lY5S0YUgdBIiG55AJ-oWvgoQ-40ef873bfkFonM3RqapMk2TmdU6F66Dubq0IQhOwZhPjMDnypDdyX6nmTIdCThABjjTsoKk4BpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/306bb628a8.mp4?token=t0X6LyOLscEGfLr7S1VGONuQUo2eZ1aHmmy7nzT5luZMWBI0-1sC-4BdveO1-bAQ1DiNLf8ZWdYM2fCczKj2uQxQnmltijx1b0cfQxOihJYcm4nzr6_fCfihKQP68Zwm7dg2CDMEDIqxR3cn5pxSn_nhcmzvcKWg5702ExnJ3ZUgKdIr9_0O4xhCRJ026VV3LJZunrRT_V-FWf9lkyevQ6IleMJjEMZKWANNzyVlMRSFvwz395lY5S0YUgdBIiG55AJ-oWvgoQ-40ef873bfkFonM3RqapMk2TmdU6F66Dubq0IQhOwZhPjMDnypDdyX6nmTIdCThABjjTsoKk4BpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی دستاوردهای دفاعی از نمایشگاه به میدان عمل می‌رسند
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/458389" target="_blank">📅 21:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458388">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7f0a4a3b.mp4?token=RMrBmxasHAZ8vlr9xRtZqPAWQ7C4DN6pS8ObL4gcxepXZyA0nQZmWmQcZeq-WMi-V42L6EQVS1dT6EFWPlL3rl92lHufi1DEpk-PEq3QTa0VsXeZHjdthk_wK3Tv2okvJMp25JxL6MIhwAyNn4_rFdUb6Ym6tEGeFazbtplwyqiNRd1jD8X8WKgYm5f_Mwl51xpfdtJs1g2z-LEtYB-2qMkDT-t-BlLxC8w-qEnp7g3WckCMdF-1Hnrfxhk4uqyWcik6NFpfF89o8fg8NsH60Bh_2nAdEvDPz-b5FQZoOYyTdR79gsHrFq3XEmqYZpL9VmhYQ75yh9t8PmJv-aOpj576rE59N8QkvUu5Gw2uYnAm4wDGWcaVoUXhxJN8Azp4U3JzRu7cimigC7ULeTv3F8D05LY4NYRMC92RP5mqCUDTjuQT7gA1g-SLHWMymNMtG9uor2Z05M9YSEyCpVpQUOrfdFtq3S8uMugXwPJfeNHGPkKNyViG4x3vys2EYoMBrCm8fKo30Qx3GwGo658Q59541hzQSwJGcsseb_WJs1MibQhkHi3oTLPqlFn92ZoBkM1X7jkKjuUihaskepgQ6_UC09ETPfHo344xB_yvojPuVccHKHQGKnFnUOtY_hhFnFBRjWckoiRQm_lDx1_xOycBBHXAgsenqKg9F9TGB9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7f0a4a3b.mp4?token=RMrBmxasHAZ8vlr9xRtZqPAWQ7C4DN6pS8ObL4gcxepXZyA0nQZmWmQcZeq-WMi-V42L6EQVS1dT6EFWPlL3rl92lHufi1DEpk-PEq3QTa0VsXeZHjdthk_wK3Tv2okvJMp25JxL6MIhwAyNn4_rFdUb6Ym6tEGeFazbtplwyqiNRd1jD8X8WKgYm5f_Mwl51xpfdtJs1g2z-LEtYB-2qMkDT-t-BlLxC8w-qEnp7g3WckCMdF-1Hnrfxhk4uqyWcik6NFpfF89o8fg8NsH60Bh_2nAdEvDPz-b5FQZoOYyTdR79gsHrFq3XEmqYZpL9VmhYQ75yh9t8PmJv-aOpj576rE59N8QkvUu5Gw2uYnAm4wDGWcaVoUXhxJN8Azp4U3JzRu7cimigC7ULeTv3F8D05LY4NYRMC92RP5mqCUDTjuQT7gA1g-SLHWMymNMtG9uor2Z05M9YSEyCpVpQUOrfdFtq3S8uMugXwPJfeNHGPkKNyViG4x3vys2EYoMBrCm8fKo30Qx3GwGo658Q59541hzQSwJGcsseb_WJs1MibQhkHi3oTLPqlFn92ZoBkM1X7jkKjuUihaskepgQ6_UC09ETPfHo344xB_yvojPuVccHKHQGKnFnUOtY_hhFnFBRjWckoiRQm_lDx1_xOycBBHXAgsenqKg9F9TGB9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام مردم در تجمعات شبانه: دشمن در جنگ اقتصادی هم شکست می‌خورد
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/458388" target="_blank">📅 20:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458387">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733998fcbb.mp4?token=q6-XcUfowyYaZawgAtW4h-XfsWiqg7iF6Zv-DaWktD_5g9mGktQnL4-bWvi0qSoWZJEFuiSctRrKaTXAg74qPVRZ2tqyxhrCnrtQ2CYQc-3bbV6Hh1aac5jobf2jQmgHYlOlPwmgKOPHWmWGEYJ76CynGgvohDmhomt-RuP4gn5ZBIbrG8GDAOWL7XlixhlRH36ysC_svdTwXaOGyADRe0dU3pogbfWJqekD-P3tCigHP3jViSxz1zQp3ceMSAV2CNTidjwcWny0YICcViQMWBEWGMrXCL33ASzvaL0xUVQsQtXqkeQbieDlLug3bRnw0tYFReZTlKNCFPkTIyxopA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733998fcbb.mp4?token=q6-XcUfowyYaZawgAtW4h-XfsWiqg7iF6Zv-DaWktD_5g9mGktQnL4-bWvi0qSoWZJEFuiSctRrKaTXAg74qPVRZ2tqyxhrCnrtQ2CYQc-3bbV6Hh1aac5jobf2jQmgHYlOlPwmgKOPHWmWGEYJ76CynGgvohDmhomt-RuP4gn5ZBIbrG8GDAOWL7XlixhlRH36ysC_svdTwXaOGyADRe0dU3pogbfWJqekD-P3tCigHP3jViSxz1zQp3ceMSAV2CNTidjwcWny0YICcViQMWBEWGMrXCL33ASzvaL0xUVQsQtXqkeQbieDlLug3bRnw0tYFReZTlKNCFPkTIyxopA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس حوزۀ زنان: خانم‌ها باید بیشتر در سطوح تصمیم‌گیری نظام حضور داشته باشند
🔹
بعضی مسائل جامعه مربوط به زنان است که در این مسائل خانم‌ها بهتر می‌توانند مشکلات را درک کرده و تصمیم‌گیری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/458387" target="_blank">📅 20:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458386">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7ner870cgzTzlqPtTjrZVjGSMpUYObKe0bcET93x1nAeDw80bAvlsM3aXyDTMSXz8rMAFfhVtZMOMfBY4EpmpeaHzfymmc7x0lI781pYRp54F31bd1qVMYE7lqNEcJSCojTZYX8FeGnjdGUDlRY_vwKcS7rJpRlSiROSV-kGIv1BqzMjWfSZaf835KFGbKHHiF-WhtSqcobAKaJGYu7viBPxH_ANCabIFplaaRMh0Kudky56DFn1_GDywnmZkw_OHK_x8AmZONth81dNEV4ukL33C47mPd4g1yINz54ye95hokHqwnzWTOdcC65Fa1B9Q5Jz6b1MIu8Hl0oB3i8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رهبر شهید انقلاب: زندگی و شخصیت بی‌نظیر پیامبر اکرم(ص) برای همه‌ی دوران تاریخ اسلام یک درس و الگوی همیشگی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/458386" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458385">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBnc-JC3yo5dQ6qxfIwSr77La3d8iL-PHyYjzUscKLHTcRUZxYGsCztib5JphQyisRf_O2SuSPkD3wsOFjBVqwqCRaaUBspLfjRjESZijd4Qxm5xaRGuV31vmcD1VdIbrywHYYUXoVBKM9c9t0z7aiXeet1Df0HGNiGpUMELzz-HibwiGcwq0PDU_4CS09TUc-hj0h72MO1XMWbv6tLrUhr_VAFgg0E317EA_-BJU6aEOzK_bkK0nDX0M6KGIhetFiWbHr4UnTvf201Tkn7xMavhYttV6GaZfEIW5rkAwRVAFRY05SYN2safDkcYZxRZKoSw35uK2sbqw_-UtW7CZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: آمریکا برای اقدامات غیرانسانی در جنگ اقتصادی علیه ایران پاسخگو خواهد شد
🔹
وزیر خارجه در نامه به دبیرکل سازمان ملل: جمهوری اسلامی ایران حق خود را برای پیگیری تمامی راه‌های موجود به‌منظور تحقق پاسخگویی، جبران خسارت و احقاق حق، محفوظ داشته و حق دارد متخلفان را در قبال پیامدهای این اقدامات غیرانسانی و غیرقانونی پاسخگو نماید.
🔹
فعل متخلفانه بین‌المللی ایالات متحده در اجرای کارزار تروریسم اقتصادی از طریق اقدامات قهرآمیز یکجانبه، واجد مسئولیت بین‌المللی آن کشور، به شمول تعهد به جبران کامل تمامی خسارات واردشده، اعم از مادی و معنوی، از جمله اعاده وضع سابق، پرداخت غرامت و جلب رضایت، مطابق الزامات حقوق بین‌الملل می باشد.
🔹
آمریکا مسئولیت کامل بین‌المللی و در صورت احراز عناصر قانونی مربوطه، مسئولیت کیفری فردی در قبال تمامی پیامدهای این اقدامات مجرمانه و غیرقانونی و خسارات واردشده به مردم ایران در نتیجه این اقدام تروریسم دولتی را بر عهده دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/458385" target="_blank">📅 20:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458384">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dfd8818c.mp4?token=rM0kdKVA3U0gvFucNYiFjOJI4Os1KLRTN16cUakB-xksy443zLfai-E9Cv9k08XZRe9ipJ9J_7ax8wOJhlGngMn9vxSRcWXUwK6kNUhwezqpEi6YEjjpHZizvdAOihmdUqfKHc48uVft917v2Ai_HQ9jjgi0zpHOLR6Ax-YY8aD6MrsqsJAOMwPBN8-fpyrQ9nImbvbsPMXPY3H0RgD5mQ1j_VVlKQ77nigsrJY5n1rqzKDAaRb6YvSJBpw5U3Y7D0Ncic6H3J62ShsVej5CBoVeDQ4M6a_reNfNN2e4nsbpwau1zE_l3vxzagOiRr9Dmx02HfQptj0DU0d46OgPjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dfd8818c.mp4?token=rM0kdKVA3U0gvFucNYiFjOJI4Os1KLRTN16cUakB-xksy443zLfai-E9Cv9k08XZRe9ipJ9J_7ax8wOJhlGngMn9vxSRcWXUwK6kNUhwezqpEi6YEjjpHZizvdAOihmdUqfKHc48uVft917v2Ai_HQ9jjgi0zpHOLR6Ax-YY8aD6MrsqsJAOMwPBN8-fpyrQ9nImbvbsPMXPY3H0RgD5mQ1j_VVlKQ77nigsrJY5n1rqzKDAaRb6YvSJBpw5U3Y7D0Ncic6H3J62ShsVej5CBoVeDQ4M6a_reNfNN2e4nsbpwau1zE_l3vxzagOiRr9Dmx02HfQptj0DU0d46OgPjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک پلیس به سارقان موتوری در رباط‌کریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/458384" target="_blank">📅 20:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458383">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075b1f1ed3.mp4?token=Mpte2kCAXcKlfoPKtvH0EKVeRg4W3ei7svV91uHLbx58pZk39cVU0cdiOyTKh-k48btPW_gJTF1NgerHxuTOaAJIKeWwvfsey1n6_gi9oOn0R1tHS1X7wDr3OXpFT4Rn5oepNEayn32n-KwDzPCwyPe1b121JxW3mq0SFuSOk2xBGsTAiGYSwe7hABIHHBF8NEXoKeAgLOabtLzatL1aI2bm8qACW7smKPxUIW0vCo6fc5MxZtpbvD_tU-0u9PcEuE5wdHjcld3O8-gf9kOodC0rH-YMwx89BV61iCe4YR3FFugMP8ICpns--4ebe36H3-YGAOrHPl-WeLcCV5Lt2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075b1f1ed3.mp4?token=Mpte2kCAXcKlfoPKtvH0EKVeRg4W3ei7svV91uHLbx58pZk39cVU0cdiOyTKh-k48btPW_gJTF1NgerHxuTOaAJIKeWwvfsey1n6_gi9oOn0R1tHS1X7wDr3OXpFT4Rn5oepNEayn32n-KwDzPCwyPe1b121JxW3mq0SFuSOk2xBGsTAiGYSwe7hABIHHBF8NEXoKeAgLOabtLzatL1aI2bm8qACW7smKPxUIW0vCo6fc5MxZtpbvD_tU-0u9PcEuE5wdHjcld3O8-gf9kOodC0rH-YMwx89BV61iCe4YR3FFugMP8ICpns--4ebe36H3-YGAOrHPl-WeLcCV5Lt2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوکر لژیونر ایرانی در لیگ مالزی
⚽️
شهاب زاهدی مهاجم ایرانی جوهور مالزی، امروز موفق به ثبت ۴ گل در برتری ۹ بر ۰ تیمش شد.
🔸
زاهدی گفته قصد دارد باتوجه به حضور تیمش در لیگ نخبگان آسیا، با تثبیت عملکرد خود زمینه را برای بازگشت به تیم ملی فراهم کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/458383" target="_blank">📅 20:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458382">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rb3kx5umcwaKPPOmhPNKaQhvvcQEldxjuxhpcc_6tknd3Bm_YdF4GBlcBpv8lEAHFmweKguR4my-iGYnPEdrqNpSL4H9UBgQTojSVar_4aYvFFdqD5X5_GQqJnxlHD5Yo1sKlFRIf7abHhUdsgRvfPVGoH7twSblU2jjJ1CaoMTAu8j7ldRbqeWSfFBnhvywuT77TwgWRxgaCtX5uU6Q5DFghLu4ibXnYBhx-WsmA07zqe-8Ra18MfeO-qMQTdfi7_jZxaQu1j_V_AWtjbLtfBpMKkCj4dBLUOowGNr3I7fjQBB5xLbyORawwIFu9fM0jPrxEhIbtCBTTBOk_n_0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی: تورم مردادماه نسبت به تیرماه یک‌دهم درصد افزایش داشته و به ۳‌.۷ درصد رسیده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/458382" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458375">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aC9j99i0W5zxlKDdiL15r4XBvvdbRXfJq67Gel-EBCA49uFuuyYkWA82wbg1AVRp77KLgYfqRCJXwnYPtikYiZ02PN7XyQlLYYc-a-7tcoALbpJFGGuF1vKLON1DVBB7_tMb8P_kmjJ4Vbr7ELVtPXPlkX0ZhsrcYQWXkKLAKy96YqaZRhWc5GRDQS4OIu84m1YCCV_qUmQdhPb7zpNJ8qjc5yXRuviO6fgeKD2tI237MbeWppKGCMNnj9kaHbXRoUdPSeXyS0Z5K3CPT02NIqpCbVxYnfXyy5S0t9fS1aphm4cCR3X38oofBXNNuM0oPIBPxyKbdqeYPL-stqxGIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGgroDgIfusKSHHyjTrPtMRDyM8XecJnApZBOxAoz787Kr8W0M7tjCpXGu99e_ZXtL8tWnk_2ZTK2lHSVWgxVfez1VAfYken5Ycf_MG59TfqEG7abJtu4HvY8vYHbrrO4xvhpAH0K6sK-ect7KZWbs3SUdTI5Itj9-G5Z2Mo6QjWD822pwlrk2r25meBAYy3mdD9F_cKJENt1sxjXyTS9ejVauHkv0XOAEkIZuV5SBdVRni9ONo4ue_LOkGeXCrfbXs3RzMqMtOnT-6XeApvo4qmtQJEXp2XlMwIyG2zpNA-d2JC8X94WESzirDPtyKhyHvFSi4_RZBOJgw6lRbSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrEUB7E6Tl3pG0Z4OsC8Oo86aiyh7Sk9b5TYyitL4knb5O2w8NSrA_ceGdGA1DWpSCrVPWiwSNMHxb9xxRusTuQo5mSxPsLeBgzT86xmAeNEsoINZHuEoqfhzY1e380JjRqlwaiGpSy0S8TDV1WGXPKHs-EDwsUi_7HHXYhnYMh-PkxpyAHrIKQpYN2YC6Dkin3Ou7H9B1sDa6EuGG0xsfzuxvWJ021wVc7usoTKhfWgDONg6P2Cz5OXRvdvphsz16AV5PftyhkhaHi2120e-sGDyHrmtk5tBREh8jVjVuEYw5dBwyXWK48bjDtApJ7PgJCPtK6Uln2xCKBjeAwn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUucuSzmaXnvljUxYYy5Q3y0Afc_m8_6BBL4cnBu3ksNUkfHM1jBQXXCpk_7eS5ZXJMQTL_WAnVMKmB_E8s6hV9f4KZAFp9yD9IBJ42-hIVWygnmYdONb_iyaY7UOVpjX2Gn143hymYl9XCcXoa0wQUoAJCLmXyhnU5eMIIuveSRf9ufPUCqggNGOFAvgUL5Dtjw7XczP8DyVVWkgxQJnnYYuggTYtl9xqUmNkAXHnEjqKiU1EicYJUQ__bQW0AVUBxM1C-P1VsYGzew7NNcHqunsDEidHx_rXVZygUuyZ9qPxMlqPeYj5GAM8nn7ACPRqWYS3aueFziIAsGL5tQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAFEvRDs0enKu0nTL6eK0Wc6uGmNCMB4YCldXOtgFzRrXDc1B7oAAxTUjkOmPgjXMP1DLE8MdquvC5IWYFGHydWXRHdxS_mOdDiSkHcjtoPSNTlA2K1SI8iVsAlWx-llOkvP9OuOhziwnGuQaU1dwuZ6yvFa0J22K5pSjLkJf2OHHcbLbfFa4SlJ8IqSy7rEkVq0Y4hNA_zVbBRnBABmZtV_6rxCqkFfyXmUjrCOOgDN0FK2t9_jggmOqWlLbPcL-M1XjFjQ1EsoK9jBRbRAhz9-6TwJDhiAk3T_Z4giWaj6iYSBoqw7Au4B9cxxW41A9VqeithdXshdDLgi08Fmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVBYxXZe09wM247fH9w9FTyDyblE3kaXA2-xNOVLcmyjzh-a3x-KVwXRF4SPodlNSyG22SYeSP4lV_5GXhDacOg4zpOMMuVEIiItHBziD-N_EGu3gb4F-Bckmlc5YgO46XmLfZUN-hyD1GoP6CpEXHMKRZB0ArkFqIsi6vsLU78nO0aRlAj5eycF_hUn0EXXkp1uxdZNQWvxU8OOroPn0EHkKbiijGpDkBiC-pJCiW4Rui-zIlJdKQl6B1PJLYgUy08W8KZqQBjDmDmaXq-nPRi4LYc7NXyypG7HfMCVGhGd3N5jtF-6iircCCnP5OBcQ2rQL9aWg3eQz319i1WsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8kX3I29uwycTEzpQHCGu7pkae3OEvF4SchG-OIl0k6sAsoB01Hunm2og8vSkb6zmVED90mlISItzTtF9Gkzfyd-8Y6wROvUyJLNKFyd9MWdIkqRQeTAOwlt_2NBVUbW3xlM-lSa8QLzg4aKVs9fN_GSg2yy46wZcQ_NFk7putAsItHN-w9IHs2qTpT0UVHe1T6r2kh8__B6ZWJCOF7LYb3YOvM7rL28T5uvHcfzAztxBw3YUuVDUrsTmnPk1pB7c1Bnmxxh8EjQdPKsxsr_wADsesFlP_mbdbmH1nzQIkzZ8lwE0U3hPXfXkcyf8lCnP2rSRgnzHq_gtaQTV4cL2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات دانش‌آموزی ربات جنگجو
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/458375" target="_blank">📅 20:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458374">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab762c3416.mp4?token=GLX4wqNvrJ7r-5X2qGSAwpSIOa73RJM8ioZMibmtWaRchAnIncyOrl-zTMX3Irn-tY33q8umKgk_h246q0G6rfFAD2MRD0niXQFpLSZQsw8LdqsL2Q2lDqBuphaYtREO84-1fPzcnYyC2IPEKwZEDlV5nXbVzS4osKchEAC-a4ANTtJbgGqHMyB1BVVXLxo3GUe7z_lEvhbZ73hIruqqo6SqTaDG70ZctBGUt8EwrMzJW4Q2H5G4YjvxSxhGcwajV8TR20O5e_0vq0lbnwuXKNqs-xHXC7e8qCLV8rC2iUuSAwiOGRvdhrHn2ugBsNq-frcA2JGmlHMfE5aOS7vVUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab762c3416.mp4?token=GLX4wqNvrJ7r-5X2qGSAwpSIOa73RJM8ioZMibmtWaRchAnIncyOrl-zTMX3Irn-tY33q8umKgk_h246q0G6rfFAD2MRD0niXQFpLSZQsw8LdqsL2Q2lDqBuphaYtREO84-1fPzcnYyC2IPEKwZEDlV5nXbVzS4osKchEAC-a4ANTtJbgGqHMyB1BVVXLxo3GUe7z_lEvhbZ73hIruqqo6SqTaDG70ZctBGUt8EwrMzJW4Q2H5G4YjvxSxhGcwajV8TR20O5e_0vq0lbnwuXKNqs-xHXC7e8qCLV8rC2iUuSAwiOGRvdhrHn2ugBsNq-frcA2JGmlHMfE5aOS7vVUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون علمی پزشکیان: به استعدادها در هر نقطۀ کشور توجه می‌کنیم  @Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/458374" target="_blank">📅 19:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458373">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ffaadb724.mp4?token=kHmkzoyu1Ni7VI4UhdzWfhlncMwm_Qom-0zKmoT7zIIhjnEiC5SRtokSGn6rRf7o-WEYUIWS7PCF-0EsE6oahQEejTA7qLSxjWfjiOSSPadsODiy1JkOTY8WvUzPZKhip4x-F5BhAhu2IN29OeTtZt0_OqByQ2mp2vPMzAC_CK2F1mAz2EufRgl4b8KSBDqbm7lKJCv_0nOj_vP9dxvhzkxDXwu49VS_ZaFu8iCP1jHqg63t7FzQ1sE18ySGEfdnNR5Fh1f0Ynf83rP7IgkRBQjIcy3aFPa-05OCA5TS4M8fcXNuoArMMCvwajv5J6qgFqRga2bJQqqjIjgINuaD7RfG9PHUA_XmXMYU0fPxt_ovG8U5NRBX8Qgef7b3KDWKVouCApMsNAEiGML-r-ohVM3CdHWnje8JantAgQPcU3EsyEWevkXwZ2uiXzisnplYkNI3JE2vsE_7aMc9G6Yjjrx84IAmoQx6SKb5T4mH5xUSYcIgi4y62DUQSUEeS932JDnzgwjLt41jVM9g0qGc8ZSKtv8ggY8DgFzVr5qheSbZqgP8eYSnOkM27G1TLBcu_mzzPdwign2FwDE5w3_KtUgQjeUt7LX1OdZY8C7EIEtZJCV4Tdj8Zzmk0NR2a9DEF2qcgpT8t7YB4wEF12F0THup1VHAgqOVqloy-zsYXLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ffaadb724.mp4?token=kHmkzoyu1Ni7VI4UhdzWfhlncMwm_Qom-0zKmoT7zIIhjnEiC5SRtokSGn6rRf7o-WEYUIWS7PCF-0EsE6oahQEejTA7qLSxjWfjiOSSPadsODiy1JkOTY8WvUzPZKhip4x-F5BhAhu2IN29OeTtZt0_OqByQ2mp2vPMzAC_CK2F1mAz2EufRgl4b8KSBDqbm7lKJCv_0nOj_vP9dxvhzkxDXwu49VS_ZaFu8iCP1jHqg63t7FzQ1sE18ySGEfdnNR5Fh1f0Ynf83rP7IgkRBQjIcy3aFPa-05OCA5TS4M8fcXNuoArMMCvwajv5J6qgFqRga2bJQqqjIjgINuaD7RfG9PHUA_XmXMYU0fPxt_ovG8U5NRBX8Qgef7b3KDWKVouCApMsNAEiGML-r-ohVM3CdHWnje8JantAgQPcU3EsyEWevkXwZ2uiXzisnplYkNI3JE2vsE_7aMc9G6Yjjrx84IAmoQx6SKb5T4mH5xUSYcIgi4y62DUQSUEeS932JDnzgwjLt41jVM9g0qGc8ZSKtv8ggY8DgFzVr5qheSbZqgP8eYSnOkM27G1TLBcu_mzzPdwign2FwDE5w3_KtUgQjeUt7LX1OdZY8C7EIEtZJCV4Tdj8Zzmk0NR2a9DEF2qcgpT8t7YB4wEF12F0THup1VHAgqOVqloy-zsYXLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تحلیلگر امنیتی آلمانی: جنگ با ایران بر همگان ثابت کرد که این پادشاه (ترامپ) هیچ جامه‌ای بر تن ندارد و درمانده است
🔹
اکنون سایر بازیگران با قاطعیت بیشتری الگوی ترامپ مبنی بر قلدرمآبی و اعمال فشار بر دیگران را پس می‌زنند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/458373" target="_blank">📅 19:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458372">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teORk6BKKMdF8YUOaJ3-KEC3Z9guSHwtIf5jQkdJtgKgSu_NWs0JqGIZnIOvwC6ru22QNOaSnTMhw9MqNKVLJcTU5Vh7tWCTRyqjPrWbln0yoPZSozrP2unSp58-lu51ZfnMcS77Jqd6S5_wZMXVmuNjJYc6oAad9EbXYvEzFRwT16MyCFZdUvca0WWh-P1gtkV7JQ1T9FdakcIgIjsiYso6uvKacTOxXjcqvzGSP8G7qnCulBkyeKYJYx2T5Xe0__T3BwzBIWmHzqTAjjs95exwGhgJS-fR_CgFM2tLxHJpmR74SJA9o9O2vLv8eh3aeSO4P_YEbe1z9gO7wVWrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک قابلیت پولی دیگر چت‌جی‌پی‌تی رایگان شد
🔹
انگجت:
چت‌جی‌پی‌تی
استفاده از ابزار ارتقایافتهٔ زمان‌بندی وظایف را برای حساب‌های رایگان هم فعال کرد.
🔹
این قابلیت که پیش‌تر فقط در اختیار کاربران پولی بود، به کاربران اجازه می‌دهد درخواست‌هایی را برای اجرا در آینده تنظیم، پیگیری و ویرایش کنند.
🔹
همچنین امکان اشتراک‌گذاری وظایف زمان‌بندی‌شده با دیگر کاربران فراهم شده است تا افراد بتوانند از تنظیمات و ایده‌های یکدیگر برای خودکارسازی کارهایشان استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/458372" target="_blank">📅 19:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458371">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGD9GZwWoqwUMAjtZResc4U3E9Chvv2JOg-uHB_qFf6DG7SjJ4vqrfm2KGUC6xyOWQlomSZ63zWArjQREwDguuOC7Uwk8bZjKVTwMolXwEYQ0amOLFGioIMoMbrb7d0e4GcXsdJ4xxqx5fvB126Gf3fVcOfiklZatOiYTL1UknqNqWwU90GLvxbpgyczS9YBJ3RhbgeL-Xgb7jOMMVVU2cR-w6cAHArwjsJCeXT17L8YvPvWqrFhqTcDe5ZtAoCMl7eYdMRoq7TwsRvmv2nGmfTl_p_8Vn8vidkUAiPIAVylJ1LKs4KgagSma9Uj5f4jzxP1wsMShC7a5LRYD6eWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی نامه ضدایرانی نتانیاهو را منتشر کرد
🔹
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین در حساب کاربری خودش در شبکه ایکسی متن نامه نخست‌وزیر رژیم صهیونیستی که به مناسبت روز استقلال اوکراین صادر شده را منتشر کرده است.
🔸
نتانیاهو در این نامه نوشته که اوکراین و اسرائیل با «تهدید مشترکی» از سوی ایران مواجه هستند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/458371" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458370">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e065bec9c7.mp4?token=SQ_bCrVKDhJIsVLvR-kegesqr8GL9alzbuQwenCJAEJofNFsDQ_kUUgR0axt1aw0kT_5ukvh9X27A4qGOBQkI7znVEP7dB0wnn7y_9v6Sga267qbNBQuulj5BVAdCtvjCcM12eD6eotujfFpTHuxBv-R9iFIuV2_aNwotCU0oeME5L20ilPSRMnc7BfpgnNWSUPAmBxz1DiWFC_KRm0lBEAX440DteNkLEic-xYnVjgHCM9trKeL9xwoukMaBlEfQh2NDVGIIB5UFIsG7F2WRGm0mEXymMmLWs8Duua7t_PGdabyM2zoslEZ4ml3G6Q7hQTiYi2eTPHGT0b5oq3gwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e065bec9c7.mp4?token=SQ_bCrVKDhJIsVLvR-kegesqr8GL9alzbuQwenCJAEJofNFsDQ_kUUgR0axt1aw0kT_5ukvh9X27A4qGOBQkI7znVEP7dB0wnn7y_9v6Sga267qbNBQuulj5BVAdCtvjCcM12eD6eotujfFpTHuxBv-R9iFIuV2_aNwotCU0oeME5L20ilPSRMnc7BfpgnNWSUPAmBxz1DiWFC_KRm0lBEAX440DteNkLEic-xYnVjgHCM9trKeL9xwoukMaBlEfQh2NDVGIIB5UFIsG7F2WRGm0mEXymMmLWs8Duua7t_PGdabyM2zoslEZ4ml3G6Q7hQTiYi2eTPHGT0b5oq3gwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون علمی پزشکیان: به استعدادها در هر نقطۀ کشور توجه می‌کنیم
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/458370" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458369">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lK753ReJeMxl71fycR5-CIYm59Kkfn1lLHPJpnoOmHqZ3dtfg0Ilfl74pa3pCXebs_6iNScjRD53ECYZVu1Z2FOV00FpNEiyapiJJCFjT8HuUJtYkTXLeGxy-9kOgoiLmVOLbGtT9pLxbJPI6xg17SW74LuzawNP_obXtJxkhO-uwZOSKao0eaNOmINdAOA02zQ1gfbzLKyXTZH_E1sSlzvnh8NFdEIywzO74dDJ4kFM5xpP2-uJ-SGZw9dUNzjiihrSVv_80jQ6qkpmnoeeWHtriq6Rn82cTLfwxA5C-fR_NLr6-0pNx4mcfbcq8P4FMBMkPnV5da_iqgad9hAwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودای رئیس‌جمهور لبنان برای پایان دشمنی با اسرائیل
🔹
جوزف عون در دیدار با ترامپ در کاخ سفید تأکید کرد که هدف نهایی، پایان دادن همیشگی دشمنی بین لبنان و اسرائیل است.
🔹
عون، همتای آمریکایی خود را به ادامۀ حمایت از ارتش لبنان در آغاز اجرای توافق اولیه با اسرائیل…</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/458369" target="_blank">📅 19:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458368">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6kCQBQOaQLDHgjYKF-ySKDXTB4Y__rOliltuhQfiTi7bZAs1-34-clQEfhLgPzoC73L5Ff4cAQbKgUy0fYvFUjN5c0I93eAdffNf3lCRa7uXb4vWUEY5RZgK2I7knEh_c8NUkIJW3GxeJc2x2EFnBX13VX7cuuKclBV_ybdCQy_xcfJcjTh-kn-ZRufRS5xxmmJIEayECTVT01oT0PuD6KZ0WL-LPc2xQytC08FMtj1M4YZ9Z3B5G1upbsOyN8QwGYRQynMuRzRR7ro8KdDY4MMTogdcQwY2Ju4VIo1bAZid0PSucz-d8HYwzwAqXDucbXR1-aCTi9Kmy0rbed3Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان انرژی اتمی: تا تدوین پروتکل بازرسی از سایت‌های موردحمله آژانس نمی‌تواند از سایت‌های هسته‌ای بازرسی کند
🔹
آژانس با محکوم‌نکردن حمله به سایت‌های هسته‌ای ما صلاحیت خود را زیر سوال می‌برد.
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/458368" target="_blank">📅 19:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458367">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f1845034f.mp4?token=jHt_Q1aW9dT6pwhtKjXRXGCoDpRI4CgMyOvJ_pybboGbHfFP--XKtLPF5jyx8xHAPlMffHs0xdVp2ZcPQR5r5Gxk8aUQKmVQcyp8jLTBz7UtwVPu5ojGwmxPe1nBLY59QJ_sRulfnaLvOSKObENnuBF4mRc7FpZwuCwItZfV1M8Epyl1fhsBb2AGQlHCMom4RH5xAB6Wrfd3qPF9_4Su28ELwTKjtCq7rbUpIcb5FPdDtRtWUORaJsoEwp_3Pj5ffVpAMbLLC-wbW8ARrmkumF9sCT70HWpRoDuPmCdinP3MtoLcUPYic-syZAZRc3AYCniJjbp34w56_7EmfKs1YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f1845034f.mp4?token=jHt_Q1aW9dT6pwhtKjXRXGCoDpRI4CgMyOvJ_pybboGbHfFP--XKtLPF5jyx8xHAPlMffHs0xdVp2ZcPQR5r5Gxk8aUQKmVQcyp8jLTBz7UtwVPu5ojGwmxPe1nBLY59QJ_sRulfnaLvOSKObENnuBF4mRc7FpZwuCwItZfV1M8Epyl1fhsBb2AGQlHCMom4RH5xAB6Wrfd3qPF9_4Su28ELwTKjtCq7rbUpIcb5FPdDtRtWUORaJsoEwp_3Pj5ffVpAMbLLC-wbW8ARrmkumF9sCT70HWpRoDuPmCdinP3MtoLcUPYic-syZAZRc3AYCniJjbp34w56_7EmfKs1YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ما قادریم همۀ مشکلاتمان را حل کنیم
🔹
من معتقدم می‌توانیم خیلی بهتر از این عمل کنیم، ما قادریم به سرعت تمام مشکلات خودمان را با همدلی مردم حل کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/458367" target="_blank">📅 19:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458366">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmBVeQ09E4KUb9BRigP98u0QRrZm51oG8L9TN87-6zcZyv9xrMCijm-_pjr9qDrSd1mBRMZpsSnM9x72xhs1zeMuPMAaFFYCJfqyRZT0-xFeS0ZKJWtUclP7xbb7PTsD9ihywawenY3UkLfYpVTJfmX2AdMw_apN2h8oGaFPY0ZrJ3K9z9mIDDHYH5mzvqM3gfeTCJ_ZyLl9fXenA51Spym6Mlrgw1ogBupMpR8P5Si8HAgWV8fFDnhIIIqCtSpS_ll_np_tDNN6E5zstSLFFx53eBQGefuhJtZjtm_kaI8HLminHtFSNO6D8N-zw6lrvTG9ceB85PmqaJY4_rrJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایست بزرگ مقابل کشتی هندی در تنگهٔ هرمز
🔹
یک نفتکش هندی به نام «HAANA» لحظاتی پیش قصد داشت تا از مسیر جنوبی تنگهٔ هرمز موسوم به کریدور عمان عبور کند اما با هشدار داده شده از این کار منصرف شد.
🔸
در ۲۴ ساعت گذشته هیچ ترددی در مسیر جنوبی تنگهٔ هرمز مشاهده نشده است.
@Frsna
-
Link</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/458366" target="_blank">📅 18:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458365">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30e0bc9c28.mp4?token=gOi_phsxcLgZdME8I7Fk1WXluqlZ3j3u7pRAc7e_sQuygwOQ7N9lof8E_5OiGZv8opasnlm2NfV0ioPgJ-Sh-ZcQjXQFcv5LJngj-92eVnuiKxRK8Wa_5jMaJKRxCpZo99S2INwnow3JC8NSPvfcCsdE6Z78EmMw6nvDPbAVhXf-FEJW5-7X2MZI0EKop3IRWM_CNxnBBXWFxSataYKxqEllh9itu2WTsED824xzSLjZ-JNINrTAJ3n5bdnjO61PD3L9QX1JTLeEfAPcr0OQr6dJ178kdOE8af8C8IeVYoaxGM-rFbrG7goUZWKa5igZiUN40HUEDyiSh9Az26Ej0zTzym9vKUdrMhrLBQPctfeoCEjvi5h05oLQETjc5GFVH-EmKreWEd5EJhhOjSPxfLQzb3ysG1JBRZzF5SfYX7luv2CxrSwxSLPHHr60PKd-KJ64SGcsxqbEQoc4mIkBm4Qk0cHs3vERHGRuaMy_32yxAHMs0rZ-39Bwz_lubP4ainvRgU9yJEKMhYMAsVVQnyk1yVLj5ZUizw2btzft-62vcQM5USevJihPQdhkQLtTQBBwboPrYfRe67i8St7RRsPVQd7VD8znTyMxRfFzZv9QYFL3QNGVEFlZri1qKRFXGfV8UqAzfr16GiUVjuV1rSngqATflDReyCCNXw4mvpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30e0bc9c28.mp4?token=gOi_phsxcLgZdME8I7Fk1WXluqlZ3j3u7pRAc7e_sQuygwOQ7N9lof8E_5OiGZv8opasnlm2NfV0ioPgJ-Sh-ZcQjXQFcv5LJngj-92eVnuiKxRK8Wa_5jMaJKRxCpZo99S2INwnow3JC8NSPvfcCsdE6Z78EmMw6nvDPbAVhXf-FEJW5-7X2MZI0EKop3IRWM_CNxnBBXWFxSataYKxqEllh9itu2WTsED824xzSLjZ-JNINrTAJ3n5bdnjO61PD3L9QX1JTLeEfAPcr0OQr6dJ178kdOE8af8C8IeVYoaxGM-rFbrG7goUZWKa5igZiUN40HUEDyiSh9Az26Ej0zTzym9vKUdrMhrLBQPctfeoCEjvi5h05oLQETjc5GFVH-EmKreWEd5EJhhOjSPxfLQzb3ysG1JBRZzF5SfYX7luv2CxrSwxSLPHHr60PKd-KJ64SGcsxqbEQoc4mIkBm4Qk0cHs3vERHGRuaMy_32yxAHMs0rZ-39Bwz_lubP4ainvRgU9yJEKMhYMAsVVQnyk1yVLj5ZUizw2btzft-62vcQM5USevJihPQdhkQLtTQBBwboPrYfRe67i8St7RRsPVQd7VD8znTyMxRfFzZv9QYFL3QNGVEFlZri1qKRFXGfV8UqAzfr16GiUVjuV1rSngqATflDReyCCNXw4mvpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات: سیم کارت سفید مصوبه سال ۱۳۹۹ بود، اما در سال ۱۴۰۴ رسانه‌ای شد
🔹
پرونده فیلترینگ باید بسته شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/458365" target="_blank">📅 18:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458364">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBU8nIvIzhNbyeqmHcHRXkiUUNnQ0o7zCGJzjVPcaT-_7pGq8dX2FhPhFgIDfFMvd2sBalhiFkGmkalyF5PqzntOlG3eGAGOc3w00Kvhc5V9OpcX3qHr_rHU7UMxTh8nAWzyFjASCV-QRt0mJNSsYN2D6U1Fkb2biC3-dUwAm8NNraNaBguK4XviuausTg6b573ggM96TiJn_-kaMd2X7QngpLm0GyI_kwD6_cBlryWF3HhQNFCVAdwnxL2qlaayLautKeXZmDeSA1eci2sG5A707-0VrWuF1dV1dwseFyJ8TxVkbjnMeUSFzMoMepuMeG_HMUFAp8CMRjL6agxngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاوضۀ لحظه‌آخری پرسپولیس در خط دفاع؟
⚽️
ابوالفضل صفرزاده، مدافع تیم خیبر که مورد توجه تارتار قرار گرفته، در آستانه حضور در جمع سرخپوشان قرار دارد.
⚽️
گزارش‌ها از مذاکره برای معاوضۀ او با حسین ابرقویی حکایت دارد تا درصورت وقوع این انتقال، ابرقویی به خیبر برگردد و صفرزاده سرخپوش شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/458364" target="_blank">📅 18:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458363">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e992600fd2.mp4?token=toiwjDMgxzR2xyYeFQ2ojBBco9iThaCXHhYjAXbExM_ydqXTIZhDQ7txUt1p6rYO9VcB8mTesVSUiVKpJpGpxVOitELIDbDKJsnVoizge4x5JvOhpFZ4P3ZRpYFRSxIbfGITJlREPUbVJYPY-12AVVUT5URcEO7PAumIELdY2N07Y5HbZrszuaiHk0BMDZSzpQdN2dvciwn-Mri_RdWTghxlvlzFwn5P_FTYMd7BjL84_I-eC_DOm0upCzPXkig6fPTlxey96CKOCZ-4QZy6_JpNvl0riVAH8oivspIq2h3mUAXExAdFFe1GYjbZK9qNOfHofqqbjobW1qTECtccHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e992600fd2.mp4?token=toiwjDMgxzR2xyYeFQ2ojBBco9iThaCXHhYjAXbExM_ydqXTIZhDQ7txUt1p6rYO9VcB8mTesVSUiVKpJpGpxVOitELIDbDKJsnVoizge4x5JvOhpFZ4P3ZRpYFRSxIbfGITJlREPUbVJYPY-12AVVUT5URcEO7PAumIELdY2N07Y5HbZrszuaiHk0BMDZSzpQdN2dvciwn-Mri_RdWTghxlvlzFwn5P_FTYMd7BjL84_I-eC_DOm0upCzPXkig6fPTlxey96CKOCZ-4QZy6_JpNvl0riVAH8oivspIq2h3mUAXExAdFFe1GYjbZK9qNOfHofqqbjobW1qTECtccHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
سخنگوی دولت: سهمیۀ بنزین با نرخ‌های ۱۵۰۰ و ۳۰۰۰ تومان بدون تغییر حفظ خواهد شد
🔹
تاکنون هیچ تصمیمی برای افزایش قیمت بنزین گرفته نشده است؛ هرگونه اصلاح ساختاری نیز با رویکردی تدریجی، شیب ملایم و بدون واردکردن تکانه به زندگی و معیشت مردم انجام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/458363" target="_blank">📅 18:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458362">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGZzKjcqu_Lp3RUw03Ljf6mHuOjg7yfwivuyaDIRaeEX_lYiQ3MP-YdW-ZEbZeA1StLOApscHIrXgwdL_CmUd4CYtfvvNMRygQP7seyqjY7d_H_226A7kKNF9juLW2p7wKDOKMy2blK-NOv5VqEAufX3iRut8lsSf9hb98h4JGIomGPYeUOPM6OEnmvUPfGvub_XsvSrazzE0rXLWyuL8RWjwMXnbuq3fqysjmBuQUHd2MEfMhIdJG7gFfTpgOdgVFF8n0ZjXzetH2YvHTGj4GOEeC5vyW2gz5WikXoqQAvTB9CNNk0CS5w6jxoDCmscYwrCqRhS5ppZmLdmEUqtag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت بی‌سروصدای نادره رضایی به دولت
🔹
نادره رضایی، معاون پیشین امور هنری وزارت فرهنگ و ارشاد اسلامی، پس از پایان حضور پرحاشیه‌اش در این وزارتخانه، بار دیگر به ساختار دولت بازگشته است.
🔹
او این‌بار به‌عنوان مشاور مسئولیت‌های اجتماعی معاونت توسعه روستایی و مناطق محروم ریاست‌جمهوری فعالیت می‌کند و بر اساس اطلاعات موجود، در برخی تصمیم‌گیری‌ها و موضوعات مرتبط با زیرمجموعه‌های این معاونت نیز نقش خواهد داشت.
🔹
اعتراض هنرمندان تئاتر و تئاتر عروسکی به حضور رضایی و عملکردش در معاونت هنری، حضور در جمع‌های مختلف مخالفین کشور، بی توجهی به حجاب و پوشش رسمی کشور در تعداد زیادی از برنامه‌های زیر مجموعه و ماجرای پرحاشیه کنسرت همایون شجریان نیز از آخرین اتفاقات مهم دوران مدیریت او بود و پس از آن، رضایی از معاونت هنری کنار رفت.
🔹
با این حال، حاشیه‌های او به دوران حضورش در وزارت ارشاد محدود نشد. رضایی مدتی پیش و بعد از اعدام قاتلان نیروهای امنیتی که در اصفهان به بدترین شکل تعدادی پلیس را سوزانده بودند با انتشار استوری «نه به اعدام»، مخالفت خود را با اجرای حکم اعدام شماری از محکومان پرونده‌های امنیتی و تروریستی اعلام کرد.
🔹
همه این اتفاقات در حالی رخ داده که شما با سوابق و نظرات رضایی شاید امکان استخدام موفق در یک شرکت کوچک دولتی را هم نداشته باشید.
🔹
نام نادره رضایی همچنین به عنوان دبیر کل خانه رسانه‌های دیداری ایران مطرح شده است؛ حوزه‌ای که در ماه‌های اخیر خود به یکی از پرتنش‌ترین عرصه‌های فرهنگی تبدیل شده است. توقف و بازگشت ناگهانی برنامه عادل فردوسی‌پور و همچنین بسته شدن صفحه «آزاد» وابسته به دبیرکل خانه رسانه‌های دیداری ایران، نمونه‌هایی از حاشیه‌ها و مناقشات این حوزه است.
🔹
همراهی و ارتباط برخی چهره‌های فعال این نهادهای صنفی و رسانه‌ای با رضایی نیز بر حساسیت‌ها درباره فعالیت‌های او افزوده است؛ به‌ویژه حالا که او بار دیگر به ساختار رسمی دولت بازگشته و در جایگاهی قرار گرفته که می‌تواند در تصمیم‌سازی‌های مرتبط با حوزه مسئولیت خود اثرگذار باشد.
@Fsrsnart
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/458362" target="_blank">📅 18:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458361">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آمریکا یک گروه حامی فلسطین در انگلیس را تحریم کرد
🔹
وزارت خزانه‌داری آمریکا روز چهارشنبه اعلام کرد که گروه اقدام فلسطین را به فهرست تحریم‌های خود افزوده است.
🔹
واشنگتن همچنین یک گروه حامی فلسطین به نام مسار بدیل، به علاوه دو تبعه فلسطینی را تحریم نمود.
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/458361" target="_blank">📅 18:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458358">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnk91txzRB8lXXvGN-GqQaX-3oOgrRyAYFg4S1u1VaP5Mh0qCj38oWJ18BcZ8R7R7jfy54oxdQcWKJHUjZJdL0xo7DW0jLK78LEBrpJpKZMRMWjEMfNGXfER3pivLnjm01FcoAbsJBAhuJlPdwM82BsI6pskBjnf7VWmnb-YZd7WlR3Ib9mHXE0ic761cwbieWvp6pf5zBkzvqZLq-F-XsMnTWI15wisFto_9WFyuhfbMaBDGMedDM2IjDgpSu3ZB1bsrxcdjdLY-i9xiRI3ymloiVMd_JfUb6qOe-S4QIkCxv1zMqM5E46BYwN6eH_R2gsB4eWO7fGNpGxeOZTXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعات
سرنوشت‌ساز برای بیرانوند در لیگ برتر
🔹
ساعت ۲۴ امشب پنجره نقل‌وانتقالات لیگ برتر کشورمان بسته می‌شود و تنها ابهام باقی‌مانده وضعیت علیرضا بیرانوند است که طبق قوانین از اول مهرماه سرباز می‌شود.
🔹
بااین‌حال کنکاش فارس نشان می‌دهد که بعید است بیرانوند از تراکتور جدا شود و او از اول مهرماه که دفترچه اعزام به خدمت بگیرد حداقل یک‌بار می‌تواند تاریخ اعزام به سربازی‌اش را تمدید کند.
🔹
به‌این‌ترتیب به نظر می‌رسد بیرانوند تا پایان جام ملت‌های آسیا در خدمت تیم ملی و تراکتور خواهد بود و بعد از آن این بازیکن احتمالاً به یک تیم نظامی می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458358" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458357">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ca08c30a.mp4?token=eznwAv00xSgiZBfS1RiJ76PXn5B_tBGTNKDy0SbUMOhq0zG5ayAnJuteU7YmAeHhSM8v-EIEbxvaxo8U_0bt9zsHF88LQpzB9dm6CpN0byQUse1_HhZhX2hpRCALMLicuZ8qxG9ZDEWIGrO_uu--fGUlJisP8i3IFhfAf3A4zfMh9H8CzM-3ZrvQnFdiqTMYsJHS0nlfFcgS0BCTty7UEIv3NCD_lNid8f32cuTR57G5G3W71urhG2JG2Bv9lcrAn9c491D3-G_3V0_WhJiIov34pyQimIc6yCZkA7brdOfKcsFto2_H1xSoEVug-PWpF5m_vyrny2D57pBFBGQepg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ca08c30a.mp4?token=eznwAv00xSgiZBfS1RiJ76PXn5B_tBGTNKDy0SbUMOhq0zG5ayAnJuteU7YmAeHhSM8v-EIEbxvaxo8U_0bt9zsHF88LQpzB9dm6CpN0byQUse1_HhZhX2hpRCALMLicuZ8qxG9ZDEWIGrO_uu--fGUlJisP8i3IFhfAf3A4zfMh9H8CzM-3ZrvQnFdiqTMYsJHS0nlfFcgS0BCTty7UEIv3NCD_lNid8f32cuTR57G5G3W71urhG2JG2Bv9lcrAn9c491D3-G_3V0_WhJiIov34pyQimIc6yCZkA7brdOfKcsFto2_H1xSoEVug-PWpF5m_vyrny2D57pBFBGQepg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: شرایط امروز نتیجۀ تلاش‌های پزشکیان است
🔹
بیشترین جایزه را باید به آقای دکتر پزشکیان بدهیم؛ با پیگیری‌های شبانه‌روزی ایشان، پایداری مالی کشور حفظ شد.
🔹
شرایط امروز نتیجه تلاش‌ها، صداقت و دستورات مؤکد رئیس‌جمهور است.
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/458357" target="_blank">📅 17:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458356">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uy3HplBhOE5XyvoUZ-4HuUZaQd4AiQ1L3-pQ9FqoKy8unTa8LSIoQT-jHHc7c3KFEEEnNkEpMO4QfN3Yb6Rm39Rg1YMcgwIK8IEiYV_YaS8FnxXgrcvUEW7x61LNYQdPkvGuLxGjw4Tpadzm0J_tqgp--j2ogLibUunYk5KltbyNqJM8hyt_7xwD9K07zwVbZrqGs0luVj-Eo0yAnJcinWAbpTw-lmFYmhl1p2awdQ__IPS-gsGxhKCx8vn-hpIZbKCiztmhLjhD29s3INxtj66BxXASBdTOp5iLE9InsLg_YFbc_jrql8mP9ouqauNgcTKoOtQD082yEAkuSOaVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل ۶ ساختمان و یک مدرسه نوساز را در جنوب لبنان تخریب کرد
🔹
ارتش اسرائیل صبح روز چهارشنبه با بولدوزر و مواد منفجره دست‌کم ۶ ساختمان مسکونی و یک مدرسه نوساز را در جنوب لبنان تخریب کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/458356" target="_blank">📅 17:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458355">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac73baf88b.mp4?token=h95qN6utgRv-t6dLyI4UXcMrew-UNtnEtlCJ2XVbQZW0VlVhq3IO8gu5SZ1PmHTXoh_46cb55-c6tbb4YfnNrhyj173LeX-k75STg9Ljr8e19ckxdBn_tbvrjZkp01Gy97nTeapXEmgaOdqwiRsroM2lgBvAzmtKOSCEPDwxZZa8j8IbgT5g_xbqKSPQ6RoIgV-r6O0U5q7iOnDBtqjsdOjfya1re_YmdOf55GdXG5OTB4zsHW5ns2NEZoH_D8T85KKAw6BV07mxlmxwaHMnOczJXVVeeI3EfJlgW-Eo599pfNUIFhu-A3VMfR-MlUq02tPp0qazGtUoJdvQkJ2FWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac73baf88b.mp4?token=h95qN6utgRv-t6dLyI4UXcMrew-UNtnEtlCJ2XVbQZW0VlVhq3IO8gu5SZ1PmHTXoh_46cb55-c6tbb4YfnNrhyj173LeX-k75STg9Ljr8e19ckxdBn_tbvrjZkp01Gy97nTeapXEmgaOdqwiRsroM2lgBvAzmtKOSCEPDwxZZa8j8IbgT5g_xbqKSPQ6RoIgV-r6O0U5q7iOnDBtqjsdOjfya1re_YmdOf55GdXG5OTB4zsHW5ns2NEZoH_D8T85KKAw6BV07mxlmxwaHMnOczJXVVeeI3EfJlgW-Eo599pfNUIFhu-A3VMfR-MlUq02tPp0qazGtUoJdvQkJ2FWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیلاب در مرز نپال و تبت چین، ۱۷ کشته و صدها نفر مفقود برجای گذاشت  @Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/458355" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458354">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
زاکانی: قصد داریم ۳ ورزشگاه جامع در تهران بسازیم
🔹
قصد داریم ۳ ورزشگاه ۴۰ تا ۱۰۰ هزار نفری در تهران احداث کنیم که شامل همۀ ورزش‌ها باشد؛ کارهای تملک زمینش هم انجام شده.
🔹
آمادگی داریم که ورزشگاه ۱۲ هزار نفری که در جنگ موردحملۀ دشمن قرار گرفت را بازسازی کنیم.
🔹
۴۰۰ میلیارد تومان برای ساخت ساختمان جدید فدراسیون وزنه‌برداری اختصاص دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/458354" target="_blank">📅 17:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458353">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5OGDBXsPSFbJKgJKakGT_D8DBtbXWQZoAkfic-ATUGRp87xv0FX71v3qYgLO3zr4K_3GVCL3ZSzbYrA-gOB44llDCBwZVEV4ygLO0u3vLT2Dqmhxg4KgKI59qRT-9AU1DOzNzc8EW96Kpwukvbjme6i4OtJZl2qRMYQS4kqVlGCqJnJUrFfBCQAvJYOXHwLTYcyyA-BsIdnt60A9T5Vu_kjA3ZNjLOk_dwSYZ6jiwZl3oxm5ZfYNq4asPvWZISVQpHyjCs8DpASHsjr6pAFkz4syv2HshEyhABE_33Wwi6_3DPusKImc_RxePd2wgSD8tk_Uu5RRJy0MqfsLU_C0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هیچ برنامۀ زمانی برای مذاکره با ایران وجود ندارد
🔹
هم اقدامات اقتصادی و هم نظامی «موثر» هستند و عجله‌ای برای مذاکره با ایران نداریم.
🔹
رویارویی آمریکا با ایران هیچ جدول زمانی مشخصی ندارد و هر چقدر هم که طول بکشد، ادامه خواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/458353" target="_blank">📅 17:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458352">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2def08b9.mp4?token=oKbh1Y497ugmFb6qaeNiSFJ8A2a5oiVNxCfj1CKPJD3O0bULYCuFd--4xYfkJny-264XDQr1bh5shnTW8POvqJwjGzAUDwbTLylmqs4U6YFN_yiY-K9H-ZoIqDn9POUFESeOcyKkZLeBkxSgw8dpi-dXl1NcZ4Xa705bzxISJ6Z3YRjGr44AEW7D6Dh8ZPWg0JZdsxQcwf_tGaSu6aeSwFLz6JrzUGTM3tY9z_p-FGU1LDDveKU4JLzbiP2BVb4Ai0YRUCg2k4ou3koZ1igm9u8sf6qbCjdBEUHQznSlRLnR-Bf--4WiNteoGEWl3Xmfi69W58cC0IEqnzclhS6M4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2def08b9.mp4?token=oKbh1Y497ugmFb6qaeNiSFJ8A2a5oiVNxCfj1CKPJD3O0bULYCuFd--4xYfkJny-264XDQr1bh5shnTW8POvqJwjGzAUDwbTLylmqs4U6YFN_yiY-K9H-ZoIqDn9POUFESeOcyKkZLeBkxSgw8dpi-dXl1NcZ4Xa705bzxISJ6Z3YRjGr44AEW7D6Dh8ZPWg0JZdsxQcwf_tGaSu6aeSwFLz6JrzUGTM3tY9z_p-FGU1LDDveKU4JLzbiP2BVb4Ai0YRUCg2k4ou3koZ1igm9u8sf6qbCjdBEUHQznSlRLnR-Bf--4WiNteoGEWl3Xmfi69W58cC0IEqnzclhS6M4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ اقتصادی آمریکا و پدافندهای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/458352" target="_blank">📅 17:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458351">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGBgBAxr6kOo_hDemANXFrztAz3XmtttAMm4ImjVWMZyIYZzv5Kv3l9njQZwQM6msRglt9TouuvPc9cL1Ihw7d1dfa1Zd74v9MJbOrWO87SyJmZJkigaPmSKiysH4bprYc7F4kQDlA8l8fz9vbL2PNHRGnqak7Ytnfkiv940WSdCRb07Atb6FrbVOTCIj8Jomr_EXrqu-w2327z0x8JYq75Ug5KtmtTXbpRA3ZvUuLA5c_9ri8rBsODSypDSOYKMWqLM98tsxP1VW3AiKX_zKOdnmHUN3BTkxmNS7yWvfj3peueY1c3CeBn_W1NkMGJbv1Wt7S2MY1tW7JBvLePd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت قاطع رأی‌دهندگان دموکرات‌ آمریکا از تحریم رژیم صهیونیستی
🔹
نتایج یک نظرسنجی جدید که توسط مؤسسهٔ یوگاو انجام شده، نشان می‌دهد که اکثریت قاطع رأی‌دهندگان حزب دموکرات آمریکا در نخستین ۶ ایالتی که در انتخابات مقدماتی ریاست‌جمهوری سال ۲۰۲۸ رأی خواهند داد، خواستار اعمال تحریم و توقف کامل ارسال تسلیحات به اسرائیل هستند.
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/458351" target="_blank">📅 16:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458350">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptKUQV-ZvmQYYaKRmzmpzbn6lsKtSi30R7YGwsMV5lwzlXpojT0YIfbIhCAaWQsfwmy5R0zmFmDOJB7aBX_46L4b_xIcG1_Q-1iOiYE5iApuAT0cZ-zzoNTiRieubJbmNVgfmECr-UClANF1qIHLJEC6jteWzLlYwSb-lzvL3MN9mrV_QGMZK3fsUPdrz4eRLTzBoU_2OhIblGvUbm3dU7_2M6hQiEuMHm5VBO3Ek3ZW_jkssuNZN-BIJm1Pdaoi3eU5Mi4Ua3Y-EVB92aNaa8Y03XJwz_TTaMKHoI-n1961jGLDo2_FAJNLpD47yFhBofTT0cI9DOzD7YKRRdh8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار شکارچی: می‌توان رسانه‌های معاند را در بانک اهداف نظامی قرار داد
🔹
سخنگوی ارشد نیرو‌های مسلح: رسانه‌هایی مانند بی‌بی‌سی، ایران‌اینترنشنال و رادیو فردا مستقیماً به موساد، سیا و سازمان‌های اطلاعاتی دشمن متصل هستند و از آن‌ها خط کاری و پشتیبانی دریافت می‌کنند.
🔹
افرادی که در این رسانه‌ها فعالیت می‌کنند، سربازان صهیونیسم و آمریکای جنایتکار محسوب می‌شوند و حتی می‌توان آن‌ها را در بانک اهداف نظامی پیش‌بینی کرد؛ زیرا از نظر ما این‌ها رسانه نیستند.
🔹
هر خون‌ریزی و خشونتی در عالم با پشتیبانی این شبه رسانه‌ها انجام می‌شود؛ این شبه‌رسانه‌ها منشأ ترویج، تبلیغ و گسترش خشونت در جهان هستند و روان بشریت را برهم ریخته‌اند.
عکس: محسن باغستانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/458350" target="_blank">📅 16:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458349">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjROvNzaGTxLeKkdgclp7x29asLD1F6qW_oLEOreQM6a1a_EBAJDMILDpgyrNb6bcrTT1gZL2J9DdPAf6o-hBzxnznVW0Ur3JXU1J9rzTKUMyf_qNQNuMqdfJV78wMhDjx-gPrw6uh_ichoOpgiO3cRCC3nLAIXnnTzbdxv3sFQDjTwoRVa4ydHotqJUjobLVOIxAjc-uV4A3jiPdclM4xOaveKFKYIASWikguUMJ8dqYQPKDIXRfa7rUWz_3KlxhoFou-pyHoPcu8GP2la1DQVDAGsCpLzHY-omWq3wOAkr5g9MF4FMOODjxLapbLbmM3fY5g71nYr46Npf5l7FAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریتانیا در آستانه ممنوع‌کردن تجارت با شهرک‌های صهیونیستی در کرانه باختری
🔹
رسانه‌های بریتانیایی گزارش داده‌اند که اندی برنهام، نخست‌وزیر بریتانیا احتمالاً طی هفته‌های آینده ممنوعیت کامل تجارت کالاهای تولیدشده در شهرک‌های صهیونیست‌نشین واقع در کرانه باختری را اعلام خواهد کرد.
🔹
روزنامه «تایمز» گزارش داد رهبر حزب کارگر که در پی اتخاذ موضعی سخت‌گیرانه‌تر در برابر اسرائیل نسبت به نخست‌وزیر قبلی، کی‌یر استارمر است، «تحریم‌های جدید و قدرتمندی» علیه شهرک‌های صهیونیستی اعلام خواهد کرد. بر اساس این گزارش، احتمال دارد تحریم‌هایی نیز علیه وزیران راست‌گرا و شهرک‌نشینان اعمال شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/458349" target="_blank">📅 16:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458348">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7088b0e406.mp4?token=BIOBT0ERwClltgcf09kK_qce46g2oWTzibybUAw0yPPqEwi-rZ-ZxAIX1xeRbiC31T_RrsXsza9t8ObBrLMGV8oa7zitkWqwk_1q7oNnM_hF2A9opMYBCwUk6dj1s5NMISLWV5B2WXyhZfgVQE2FyDTDCRMmZ2XMbveoPL1Xi5dXj4w_2UcSmLVwSJRT7XpTVTb7ZQAMJ_UMZPzKkfFd8WGrb6RS9v7CuI3Y3GqWH5wazA2kywYq-9TsoDP8KjIgLG_WnLdH8NizuJcN_HkGKuQ2_P_2hxAJNO73lZc9H8WiokXSGS7obS5515xg78Q1sxmeOn-ba0jy3uoDQMOziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7088b0e406.mp4?token=BIOBT0ERwClltgcf09kK_qce46g2oWTzibybUAw0yPPqEwi-rZ-ZxAIX1xeRbiC31T_RrsXsza9t8ObBrLMGV8oa7zitkWqwk_1q7oNnM_hF2A9opMYBCwUk6dj1s5NMISLWV5B2WXyhZfgVQE2FyDTDCRMmZ2XMbveoPL1Xi5dXj4w_2UcSmLVwSJRT7XpTVTb7ZQAMJ_UMZPzKkfFd8WGrb6RS9v7CuI3Y3GqWH5wazA2kywYq-9TsoDP8KjIgLG_WnLdH8NizuJcN_HkGKuQ2_P_2hxAJNO73lZc9H8WiokXSGS7obS5515xg78Q1sxmeOn-ba0jy3uoDQMOziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی چگونه به درمان کمک می‌کند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/458348" target="_blank">📅 15:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458347">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XA9EBF_aOjy5h2bDXr66XQvB4Lt5_Wq_dp6YEa9DPlahmn4Y1jQaP5zzFT4kRluBEEiLa8DxEsOQlXsoJrX_0W23jesh2zRn9pjJ6TqmINJ15JSGJEU_Xejt0ymB8rAMfyxBrN356JsZ_lW_sGEi133rbyBh52jFK9Ir7kw0NotMvgt9WMTX3yEPZYYXtkhYII5RrU_ND-CaBN_4fLmAgnZmoB9XFsRLeHs8KQMFTf0geXaORDW8K2n7A3t6swom8xJpxsmAupsmXlp7Hgj4B6xryv_V3fJ77KFWbRAEr1jSO1CNDXP9Tu2u2DKqMMIjVS6fZ-iZikkz83-2sY_M1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروندهٔ ۹ سالهٔ جذب استاد روی میز رؤسای دانشگاه‌ها ماند
🔹
رئیس هیئت‌عالی جذب اعضای هیئت علمی: دانشگاه‌ها در جذب، تبدیل وضعیت و بورس اعضای هیأت علمی اختیار دارند و هیئت‌عالی جذب در اجرای پرونده‌ها دخالت محتوایی نمی‌کند.
🔹
یکی از آسیب‌های فرآیند جذب، ورود نگاه‌های سیاسی و دخالت افراد خارج از دانشگاه است؛ در حالی که جذب استاد باید بر اساس ضوابط علمی و بدون مداخلات سلیقه‌ای انجام شود.
🔹
حدود ۳۷ هزار نفر ثبت‌نام کردند که ۱۷ هزار نفر واجد شرایط بودند و برای جذب حدود ۱۲۰۰ نفر مجوز صادر شد.
🔹
شکایت متقاضیان در ۳ مرحلهٔ دانشگاه، وزارتخانه و در نهایت شورای عالی انقلاب فرهنگی بررسی می‌شود و بخش زیادی از افراد پس از توضیح درباره روند انتخاب، قانع می‌شوند.
🔹
حتی افرادی که در یک دانشگاه پذیرفته نمی‌شوند، نباید از چرخهٔ علمی کشور خارج شوند و می‌توان برای ادامه فعالیت آنها در دانشگاه‌های دیگر، مؤسسات پژوهشی یا شرکت‌های دانش‌بنیان مسیرهایی ایجاد کرد.
🔹
نیازهای آیندهٔ کشور باید پیش از ایجاد رشته‌ها و تربیت اعضای هیئت‌علمی مورد توجه قرار گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/458347" target="_blank">📅 15:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458346">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce73d744a.mp4?token=vULQoSk-bt8U_oaHvA2F4a4FjKa7fm7XWA2dZGoeE2oNGzVNWp9mPrjyYdSOE76Aqi1XROeJV9wrMD90L2O0zKLjkenXlwo9pJvYjImvK-5QMl5szTBUJE7pzcTubEHf_IsC0kheDctVKI6pGvlHgx7EOHGFOWm3So0gMJn4Kpmuz5uG5iJyWpXL91CwGAa-gkwm6yaLksyLZ8-mttQQA8T1leIRSZp9SaIcflwbIUu-73DvmEAh_DIGR8P9vqaq52cZGP_BMAJ3HotHdJY3nWv9rZPRngYSYk7Z7_5saTWJEAJeabgCF9vXPvULzu_otTyp9_40CUZTZizOL9OBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce73d744a.mp4?token=vULQoSk-bt8U_oaHvA2F4a4FjKa7fm7XWA2dZGoeE2oNGzVNWp9mPrjyYdSOE76Aqi1XROeJV9wrMD90L2O0zKLjkenXlwo9pJvYjImvK-5QMl5szTBUJE7pzcTubEHf_IsC0kheDctVKI6pGvlHgx7EOHGFOWm3So0gMJn4Kpmuz5uG5iJyWpXL91CwGAa-gkwm6yaLksyLZ8-mttQQA8T1leIRSZp9SaIcflwbIUu-73DvmEAh_DIGR8P9vqaq52cZGP_BMAJ3HotHdJY3nWv9rZPRngYSYk7Z7_5saTWJEAJeabgCF9vXPvULzu_otTyp9_40CUZTZizOL9OBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وعدۀ تازه مدیرعامل شرکت توسعه: ورزشگاه آزادی آبان یا آذرماه آماده است.  @Sportfars</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/458346" target="_blank">📅 15:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458345">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Suc83JkeckUduFe12OIUhRzLy17LOekWoyKy38G2SiUoYCF0b5iwSBgoe76evQHt9okqGIDEo8eOjCXOSShCVvr-hQBlMXFpswFm3cOe1iZlF2DtgEKsbjU1YaEKkAcDXpMgfrNUBssywDgKhSaHI6Vh_lb5onlfx9BmwDuIrPxfauDDrtYhUTEZ8xg0u4pHenV2c1CgDo4OMMG0wL8I4DNuEjPLsekbeYSTLnQ2PejXhX2-td1HXIKIackBwhMpNQVVgnSF5Z82ypdN3Ova-haQJyD7cS-sbapZkuzw7CTEelJnTcyEm0C8-bNSCGBzUb8uTUTYZBm2tnsFMBk2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ایران در جنگ رمضان آسیب‌پذیری آمریکا را آشکار کرد
🔹
سردار محبی در نشست تبیینی دفاع مقدس سوم ویژهٔ اهالی رسانهٔ اصفهان: ایران در جنگ رمضان توانست در همان عرصه‌هایی که آمریکا قصد داشت کشور را تحت فشار قرار دهد، آسیب‌پذیری راهبردی این کشور و متحدانش…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/458345" target="_blank">📅 15:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458344">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/347ead572c.mp4?token=o2_jIvkSk4RR7WvPR7tHUkIatWC_nhp4Zyw8DBKFHdxeKWpWlx1tti6t6ryUZnzLUrCUHZ7ximEdzuXB5Y9MHM63BrJsyPepf3gdO7xZDc16UqHaQ-_Jw-aJAmA3EZ1P82oFLGTX0jexTalOLWJ36zEcIavgirIpTL107xgVc1Ue4QeaIV5-bVFw-4sNNPufuLwxK9OfNjL_vSNhB6YL5mN88jRYHqJPIvtcH47Vr4_B2W-qi_eV0l_51FVHwsEK7l0_BHVyg07uVKLIlQd8bUkeaXZNbvT1HdxzcFQ1npOjgAF0p8oPuiGviIh7bgZRY6L2e42nkQrb0LBRB8EDsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/347ead572c.mp4?token=o2_jIvkSk4RR7WvPR7tHUkIatWC_nhp4Zyw8DBKFHdxeKWpWlx1tti6t6ryUZnzLUrCUHZ7ximEdzuXB5Y9MHM63BrJsyPepf3gdO7xZDc16UqHaQ-_Jw-aJAmA3EZ1P82oFLGTX0jexTalOLWJ36zEcIavgirIpTL107xgVc1Ue4QeaIV5-bVFw-4sNNPufuLwxK9OfNjL_vSNhB6YL5mN88jRYHqJPIvtcH47Vr4_B2W-qi_eV0l_51FVHwsEK7l0_BHVyg07uVKLIlQd8bUkeaXZNbvT1HdxzcFQ1npOjgAF0p8oPuiGviIh7bgZRY6L2e42nkQrb0LBRB8EDsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: بیش‌از ۳۰ هزار نفر از عصر امروز خانه‌دار می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/458344" target="_blank">📅 15:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458343">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPcrwpO0JhKFf2bJjd9c0Em6BfS3F2aR1ze2MTk7u2rwXkE-ans7rzsaHFohU9FV_iV3Oe5kL5tfTCzYngAhPaC_ZtvJSo6BW50v9XdJJ7LDgrAsml4H6KuIh8SzzkDBwLJ7ngUjwNHoLUilc4VWSZgTltmB1EUZhVlTyKBJb4s4Bap-sVXgtGDY9kVvd8jrg2_UE66hIZd9eiln4L0as64lHr3B_V76Xy_SjQ-s_hzhoM7gBDeKIHakAf7qjIXSrTCKPXF1zysbTrugPwsdtsWaPjS0dkjncv_rHdRQWKsnWltYPDHshIzb87Ilt59v7RuoKUWhDvyCEgKM-O_ijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ایران در جنگ رمضان آسیب‌پذیری آمریکا را آشکار کرد
🔹
سردار محبی در نشست تبیینی دفاع مقدس سوم ویژهٔ اهالی رسانهٔ اصفهان: ایران در جنگ رمضان توانست در همان عرصه‌هایی که آمریکا قصد داشت کشور را تحت فشار قرار دهد، آسیب‌پذیری راهبردی این کشور و متحدانش را آشکار کند.
🔹
دشمن با استفاده از عملیات نظامی، رسانه‌ای و فناوری‌های پیشرفته از جمله هوش مصنوعی به دنبال تغییر ادراک جامعه و ایجاد زمینه برای ناآرامی بود، اما انسجام مردم و همراهی نهادهای مختلف مانع تحقق این هدف شد.
🔹
آمریکا با بهره‌گیری از شبکه‌ای متشکل از ماهواره‌ها، پهپادها، رادارها، حسگرها و هوش مصنوعی توانست سرعت شناسایی تا اقدام عملیاتی را به چند ثانیه کاهش دهد؛ اما ایران نیز با ارتقای فناوری موشکی و هدف قراردادن اجزای شبکه عملیاتی دشمن به مقابله پرداخت.
🔹
کاهش ذخایر تسلیحات راهبردی آمریکا و آسیب‌پذیری زیرساخت‌های این کشور و متحدانش از عوامل عقب‌نشینی آمریکا بود.
🔹
پیروزی‌ها و دستاوردهای این جنگ باید توسط رسانه‌ها برای نسل‌های آینده تبیین و ثبت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/458343" target="_blank">📅 15:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458342">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
سیلاب در مرز نپال و تبت چین، ۱۷ کشته و صدها نفر مفقود برجای گذاشت
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/458342" target="_blank">📅 15:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458340">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP0IJr2i_dRilWVRnKNKf8K8BEvwi0g1BRsZE9-t14TRK-RsecPnED9XmxyXz7HRHMaRbwiwT7JRtgpV580sRO6EYN4w0GctK5x9cmDr0QV2rh5tCcOsSHVBayCJFyXuZCQoghixix5QXAomtK5tce6na17W8PYq0vrQP4mw0nM0mKRmRUe7ZYfGoGXaGett0DKHS2_zk8WLh5lB5JgaFsCV9sNIQ_g1M2LrT5atFC3KONQX18IPm-UGNtKt1Iyo47b_Zz0liKkKHX_JJR2ar2jtnsV2qWM5WcdcalfWYn3yDaierg4qpq2xl0-0Tk87gNMQa_j-L5lkMLMNuVQlcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۸۲ سلاح قاچاق در ۲ استان
🔹
سخنگوی ناجا: در ۲ روز گذشته ۳۸۲ قبضه انواع سلاح های جنگی و شکاری قاچاق و ۴۴۹۵ فشنگ در استان‌های کرمان و خوزستان کشف و ۱۲۸ نفر دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458340" target="_blank">📅 14:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458339">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egLE_KOYefNNgmORyZATGeef5iEvbRQNkrpuOkmZz1jxCFoTt2hvNW6VOmLra87e752Do22UxfLNSBoB0jqZaKApYXkB80qDe7hsmkh891nm6i07YXnyIm_xCnsqVDVKvdvzpxFvDjHwOMZst9-z9iDMp0vy6hRWbKWAr599bPeEzVFM4yHtVO0UFuGqoXUJQD4hzVS3vgGaPFXJm3bmeXDhEMlEskmaJr-_CPouR0CNeUR6PPjrhybUZ2iI78c3yaK0s4u2u4G_QZNcQEXqAwkH_3rZE4cKn2lfNvfLngSpGvw5NW6N-ySLLfWhTjBufkyDEBka-Vok8Z5R0uPGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن داروسازان: واکسن آنفلوآنزا هنوز وارد شبکهٔ توزیع نشده است
🔹
به‌طور متوسط سالانه حدود ۳ میلیون دوز واکسن وارد کشور می‌شود؛ اما امسال هنوز اطلاعات دقیقی از تعداد واکسن‌های واردشده، منشأ تأمین آن‌ها و زمان توزیع در دست نیست.
🔹
اکنون زمان طلایی واکسیناسیون است و واکسن باید در شهریور و نیمهٔ نخست مهر تزریق شود.
🔹
با این حال، هنوز واکسن وارد سیستم توزیع نشده و دربارهٔ تعداد واکسن‌های احتمالی واردشده نیز اطلاعاتی در اختیار نداریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/458339" target="_blank">📅 14:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458338">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igvqeQjeviqqe-dewpTK31JQgP8hYvq2fLEWpbDyY8xCazIXeXgVuAYWvRBVtN5S7iXRES_TDgSMHpn82iRhVLLppSHY4wzPoFCpM2g0C9meLIO29FjxqE58kVz1t6Q2fHeHujMViH4IRrb7Dpij9J1xQTuhUDrmb37al2cZmKmwftCPSZ5b2396LEdx1S7O1nzfhy0TBa8oFLyI_e90NWgNoJNv5Cp3-1Em1F5k2fhZsFlWmQ450lcARBE6jvuxG3zuF9xSWccvCYDg0XQHPnZKfFXO2WkvkreNTkNzRzcDjXJPjstAnAqxjV9OB1uIuTR6kNZ92TScuE-WlirCMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار با کارت ملی مشخص شد
🔹
نرخ پایهٔ دلار برای خرید با کارت ملی امروز ۱۹۵ هزار تومان اعلام شد؛ دلار در بازار آزاد نیز ۱۹۸ هزار و ۵۰۰ تومان معامله می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/458338" target="_blank">📅 14:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458337">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHeXwfQ9wJZ78ETr1o_lqRit2ZJJpnDxG3H78Zk6-Vs_gv_4634b1TqzsZXiCRotoR6xwRH6y3vWKWXnhLXAGXcctulWaiaw5cqRueWpgoxWW5RwOgLkv6bE_buK7ZPmtJl6e_gosjh6_ocfxMefRwwh2F0npvocyvll9zdSy3KUUMjFcrzvq3xPiNIL1q6BmziqbOSWInaHS4oLWQMOdaBYkaQjQcA5RiUVxEemyY31-WT5Sew-smvLL6PS7W-WkgJV9pQKOibr-xN-e1s1E7gjavaIXlkuAtaT9qgqiM5HhxAxxPv-H1CUQAOsBpwfb_dDZ8DQZCD9b1yyaCrJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ میلیون لیتر بنزین بیشتر در راه است
🔹
شرکت ملی پخش فرآورده‌های نفتی: با بهره‌برداری از پالایشگاه‌های آدیش جنوبی و مهر خلیج فارس تا پایان سال روزانه حدود ۱۲ میلیون لیتر، معادل حدود ۹ درصد مصرف روزانهٔ بنزین، به ظرفیت تولید بنزین کشور افزوده می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/458337" target="_blank">📅 13:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458336">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1ea55ed6.mp4?token=ZgEdfQkhIj5OjjLY-tJpXx8iai5IU4XArtyEI6uZE0ATsnt_-479Q_uHujLEacDv1Qt05OgAB-nwuMoGh4wG6v9ceUSG9fjs5a-lB1mH_raZsZuujn7F2MypTkbWeIPxSi-_IY5cxS8pGGBEQAB6piDF8dVcAozLYa2EZbUQgEQFBWoprIRNhxgGGFh_HpjpXDzH6sWjYJa6j_70DHqsskZDVsGYIKjyHiNrOSKJOBzgXujwNmGqk6uO_Crb_FoBPTWsjgjDnJ8F6iBLu_cofqF7kj7OTzlA_A2IeP6SpHdz6pVPGlGqdSTFJznSUhUqg2iEhgg-FJHQV1Kf_JX5lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1ea55ed6.mp4?token=ZgEdfQkhIj5OjjLY-tJpXx8iai5IU4XArtyEI6uZE0ATsnt_-479Q_uHujLEacDv1Qt05OgAB-nwuMoGh4wG6v9ceUSG9fjs5a-lB1mH_raZsZuujn7F2MypTkbWeIPxSi-_IY5cxS8pGGBEQAB6piDF8dVcAozLYa2EZbUQgEQFBWoprIRNhxgGGFh_HpjpXDzH6sWjYJa6j_70DHqsskZDVsGYIKjyHiNrOSKJOBzgXujwNmGqk6uO_Crb_FoBPTWsjgjDnJ8F6iBLu_cofqF7kj7OTzlA_A2IeP6SpHdz6pVPGlGqdSTFJznSUhUqg2iEhgg-FJHQV1Kf_JX5lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: ۴ نیروگاهی که اوایل جنگ مورد حمله قرار گرفتند را بازسازی کردیم.
🔹
بقیهٔ نیروگاه‌های آسیب‌دیده نیز احتمالا تا تابستان به مدار باز خواهند گشت.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/458336" target="_blank">📅 13:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458335">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0y4bn_9Ft2WsVfCeydtaijT-OQPXzXhYEEoY5Ij6p224boXwF25jYm_ooGm5DstQs2YLP_AWme4xeE9cB721dIHeqzy5U-BHoYxcfB_4u1XA5ykNa_SRHp-0GiMJqOlOwp1QQ6Ayxw53xOol3K8vLCtXi_uwdILeELTE2Fty61YvgDZFoTDAI5AvZGVftG_5MiNa2grqTrhwA5yd8IwfCXi8CPMbxH8Vzy7qnstEGVIMUZx1rovpzoOcwxMk_nVljjF2-7KqoyjPKeTaFS2imTKZkZxmUYur7kO0qnmbPToPipLnQUKOyASe4G5zrgvnqDojykFyNn3WeeDwqLN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس هفته را با رکورد جدید به اتمام رساند
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۱۶۲ هزار واحدی به ۶ میلیون و ۳۸۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/458335" target="_blank">📅 13:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458334">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pW6l6YC-oAlcga1Fg1UcdHZVNaIfI2LrI98y5ADAxr60VmdzOmubyjZpPRKEXYAUC3rS6Xdm55Hu2ENQ5KO00HDJ5AK_JYQlYHzQauylFhXTEjwqKY9NXyhw_12Sc7Cl7FeCAt3ddbxDZbU5aJZmiqxwAlwmBq8gTsVJjm2zhUg1tgijV-0mOrbz9DnJcPsPldwzqD_M1woU7yTIcJkkWDQieXhAgts5sYAUR3M83EPeWUfQW8wZooVNIN3EVCVL5Zec6YTt-jJL13LlePCyG8ZypHOHHWn35yKD5-ubg811Um5oWxtFVItWXk9EtCYU2rrmiJ38AHckymOW9EWCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی فدراسیون فوتبال: قلعه‌نویی تا پایان جام ملت‌های آسیا سرمربی تیم ملی است.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/458334" target="_blank">📅 13:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458333">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b345137d.mp4?token=vtG1zXXNYgAJLzXTwft74j5L2jhzHLADo_eUTKa0Lonx9gvIAQ1PbsM9cQH6e2F9R9rhAkUEpuMEmqgWUTrtR_18bH4k1VDeFl647DTFD8gPWyAo00mfgMAkbeTX9-Caf_D87lUTi2CRluMImKj-S1GC2ySglwURgnAU1drkHOFNx696NB7lqIG6KJvLhx5TL-1Sxax4ftRac9sN8c-vtiMGdfKHc4vIcltE1-vQbjj0G6tQIdP9pi6lx45HkNIVj86Hgbv8GE6sfL9Lo5B76sVXSPlLimnzJXezYpbfaIurJvMGls95ugynlXecsT8_4GAEYHnB6L4UpJT3WTMt2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b345137d.mp4?token=vtG1zXXNYgAJLzXTwft74j5L2jhzHLADo_eUTKa0Lonx9gvIAQ1PbsM9cQH6e2F9R9rhAkUEpuMEmqgWUTrtR_18bH4k1VDeFl647DTFD8gPWyAo00mfgMAkbeTX9-Caf_D87lUTi2CRluMImKj-S1GC2ySglwURgnAU1drkHOFNx696NB7lqIG6KJvLhx5TL-1Sxax4ftRac9sN8c-vtiMGdfKHc4vIcltE1-vQbjj0G6tQIdP9pi6lx45HkNIVj86Hgbv8GE6sfL9Lo5B76sVXSPlLimnzJXezYpbfaIurJvMGls95ugynlXecsT8_4GAEYHnB6L4UpJT3WTMt2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: آیین‌نامه برای سهولت در کارهاست نه ایجاد پیچیدگی و ابهام
🔹
در نوشتن آیین‌نامه‌ها دقت کنیم که خود آن‌ها پیچیدگی ایجاد نکنند؛ آیین‌نامه‌ها به گونه‌ای نوشته شوند که کسی برای ابطال آن‌ها اقدام نکند. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/458333" target="_blank">📅 13:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458332">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb90b20a2e.mp4?token=tQS2AO2b2URCM-bnrPL6ZNCDwRGOBVxm3hyt5I9l-82C_VDFSjqhTjgtHySE3zHzx6PtAxa6fTkRU0xsQbhsSACzqXxi-1NEByCThhDWZiT_Dua80N1iCoHvCJzQvQh49pgXl5_dxoA1lRlYnDPFnlHaKaXTFCeLkxYDmEmP7_904WBUx29SFD8H6Sw65DOQcNz_Voaxr16MLHBs2BoW-YsPrmuKcwTbxHAi49SqOOV89U4aoMEIlbdFehVm3Pv7o5liV3SUq8o3JnCV8DXEVfrGZh7U1sTgVcvD2fiss8_QpIIb5HPuvxulv-GSu4AYg_ooUwYc4DALXw5k_rOw8G3QoTJuHfsMNuayzDj4H1VWxYl6Wc4E-UAC4iPk0ZgowXbvXSQuJPKWCmGotPrVSAYxTMMyngO5M26XvG1z6ftLarqMxHMLHhs94Rp1Ej1NhGmWsaxhD2UG3Z7FtWFxDwVZplc53YT9Ve4qhfDOVEDsbQd7QKBOaJrzv5HwVVIt-vn9xEZFxiSzBJFrTe2ZZGZhENt0nGhUCo5XSPBuGAfW7G_EUFsovL-HIUJlN_1eE08vjBNEidbhaBWEoQ0sfqnRkKGNH4xnlA6EOntjCvZ-BizqwOFePc_mUpvhBeueyib33BnoVo54qQhTTdP8AJ0HgnBRbPFN2TGz4FuaHO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb90b20a2e.mp4?token=tQS2AO2b2URCM-bnrPL6ZNCDwRGOBVxm3hyt5I9l-82C_VDFSjqhTjgtHySE3zHzx6PtAxa6fTkRU0xsQbhsSACzqXxi-1NEByCThhDWZiT_Dua80N1iCoHvCJzQvQh49pgXl5_dxoA1lRlYnDPFnlHaKaXTFCeLkxYDmEmP7_904WBUx29SFD8H6Sw65DOQcNz_Voaxr16MLHBs2BoW-YsPrmuKcwTbxHAi49SqOOV89U4aoMEIlbdFehVm3Pv7o5liV3SUq8o3JnCV8DXEVfrGZh7U1sTgVcvD2fiss8_QpIIb5HPuvxulv-GSu4AYg_ooUwYc4DALXw5k_rOw8G3QoTJuHfsMNuayzDj4H1VWxYl6Wc4E-UAC4iPk0ZgowXbvXSQuJPKWCmGotPrVSAYxTMMyngO5M26XvG1z6ftLarqMxHMLHhs94Rp1Ej1NhGmWsaxhD2UG3Z7FtWFxDwVZplc53YT9Ve4qhfDOVEDsbQd7QKBOaJrzv5HwVVIt-vn9xEZFxiSzBJFrTe2ZZGZhENt0nGhUCo5XSPBuGAfW7G_EUFsovL-HIUJlN_1eE08vjBNEidbhaBWEoQ0sfqnRkKGNH4xnlA6EOntjCvZ-BizqwOFePc_mUpvhBeueyib33BnoVo54qQhTTdP8AJ0HgnBRbPFN2TGz4FuaHO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: آیین‌نامه برای سهولت در کارهاست نه ایجاد پیچیدگی و ابهام
🔹
در نوشتن آیین‌نامه‌ها دقت کنیم که خود آن‌ها پیچیدگی ایجاد نکنند؛ آیین‌نامه‌ها به گونه‌ای نوشته شوند که کسی برای ابطال آن‌ها اقدام نکند.
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/458332" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458331">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW87AViHSh5IfRpqKgLZhi6C-v7WsWRQ51FGvvl-AkLHQOK0ETt5S9RMFG6CFE9fZArOg3bGtZ-QNLviLBhsg-PrCSHIg03Jdkllpth3XK_XIGPlMLz8_l1E05_YnhffFPpiPkRSoCmsURRXfB4EzoELdL4-EqwC6NdBZyitHcu9YhgSKp5UmTquS1JQKcciyn99abZ62Ar4B3a2Lgf1deApEGMo39L_FiyeY298Uuut4Y4YqsLNcHQ_jOZQdZGAk2B2C7BdlCeXWYKX08S9UXMgLHmDyjfgY05_jI7cwqwJgBn_XnZ8RrMlP3Xpaexh9K5Zwhzbo-SfwDNdCKWSwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی در تیم ملی ماندگار شد
⚽️
دبیرکل فدراسیون فوتبال: به جمع‌بندی رسیده‌ایم که آقای قلعه‌نویی تا پایان جام ملت‌ها سرمربی تیم ملی باشد.
⚽️
انتظار داریم او تیم ملی را در جام ملت‌ها قهرمان یا فینالیست کند. @Faresna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/458331" target="_blank">📅 12:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458330">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W14I42kLGVkeStxHa0HC3YrN3TrmNbJJ26U3oZB1_fKN4h5-akquf_oW3KMP-K6QpwXGkFdj2dSF_0rdOVZaFoQIYgyaqgyLy4_HFAC95BvxJVPB1kNIOZePRxQYDeLwzDyFnGaQLJt_9FqtiDVrlhGCA5g2kC2Fkb5HolO631b5i_CciXrc5M-vR5rL8GQXWH-PX-XrHKy6uCo8zOIVU-JGMsOSVMJL8oJrI46aK8aO1jPgtTXYxFgF4WBGWGi72SZ32MSSpj6gcjnVpE5SYF2Kw-Kg3yoZBTd9rUedssghB_8TbdoudIOJUr7BMn9A9xQ8ksrX9iAHjqZCe5oqEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن داروسازان: بدهی ۷۷ همتی بیمه‌ ریشهٔ کمبودهای دارویی است
🔹
رئیس انجمن داروسازان ایران: کمبودهای دارویی کشور ناشی‌از مشکلات اقتصادی و اختلال در گردش نقدینگی است، نه شرایط جنگی.
🔹
بدهی بیمه‌ها به داروخانه‌ها در یک سال گذشته به‌شدت افزایش یافته؛ بدهی تأمین اجتماعی از حدود ۴ ماه به ۸ ماه و بدهی بیمه سلامت به ۱۰ ماه رسیده است.
🔹
تأخیر در پرداخت مطالبات، توان خرید داروخانه‌های خصوصی را کاهش داده و باعث شده شرکت‌های پخش و تولیدکنندگان نیز برای ادامه فعالیت با مشکل نقدینگی مواجه شوند.
🔹
پرداخت بدهی‌ها در قالب اوراق نیز مشکل داروخانه‌های خصوصی را حل نمی‌کند؛ چراکه این اوراق برای بخش خصوصی نقدشونده نیست.
🔹
درحالی‌که بیش از ۸۰ درصد خدمات دارویی در داروخانه‌های خصوصی ارائه می‌شود، ادامهٔ این روند می‌تواند فشار بیشتری بر این بخش و در نهایت بر تأمین داروی مورد نیاز مردم وارد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/458330" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
