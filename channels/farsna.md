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
<img src="https://cdn4.telesco.pe/file/YfYmMYGlAljqFMpz_7R2JV81bwOUIDkDdeyey4huGmcQ0afAsCg8QLoi3VayvyQo69aulDPI_lzzPp5dt8uwk0_JBK4TAueq2iadNzoqLCJAA3-rUXCJiZ11HUQjQCt4eK__zrOSazy3-e47cfCfhyuVCDHB11p9DRRfsvoC391PDpAwiUyHqx5Y-xZYO1xatqjcnKyNme8AJUbKWdVT-VLuQUSpfpLrrYD3cwk7zi9-DRDoXelNnvkUwyhA6K_ECiN2UH19lKvt6yNxg52bQJE62M2TeA9p-ZLELDPDJsFIb06Bkov47iybr45KfWBa_xG6X31rhznsnt-RZD-kHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 15:58:22</div>
<hr>

<div class="tg-post" id="msg-445644">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a081ef12.mp4?token=Ca8fIi9gyO-NytP6yZxyJO9B3Eu-gAIIeBdOQ0ZTsfIhlHl2m8O0uUi-Aqz7hiYkXssD9gO4HQ43C1xyuLIeHCOh0FyWwSNVBOfHsf_37eQWwZN32q_7AteUzdU0PgtVkfucZLRiM_fqrwrc6x11nbUS_aBY44uEq0YQa5-KVkEfTbhIV65rMiG5qHNkX5iWugTzRqaucpGMl-F__s9YhQ-0GwQhQmUS-s2efZl_7d1Ji_fRq15aGsshyUdY7lUy3oE2iSdXxLJt84zZwpTjTSrrZjt1roIfTbJHrjIdgkBKvtlwIwPJyGI-fPK-PJBkEsHDEnKWFoXbYGBeM80eJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a081ef12.mp4?token=Ca8fIi9gyO-NytP6yZxyJO9B3Eu-gAIIeBdOQ0ZTsfIhlHl2m8O0uUi-Aqz7hiYkXssD9gO4HQ43C1xyuLIeHCOh0FyWwSNVBOfHsf_37eQWwZN32q_7AteUzdU0PgtVkfucZLRiM_fqrwrc6x11nbUS_aBY44uEq0YQa5-KVkEfTbhIV65rMiG5qHNkX5iWugTzRqaucpGMl-F__s9YhQ-0GwQhQmUS-s2efZl_7d1Ji_fRq15aGsshyUdY7lUy3oE2iSdXxLJt84zZwpTjTSrrZjt1roIfTbJHrjIdgkBKvtlwIwPJyGI-fPK-PJBkEsHDEnKWFoXbYGBeM80eJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آجرلو، عضو رسانه‌‌ای تیم مذاکره‌کننده: فروش نفت ما کاملا به شرایط پیش‌از جنگ برگشته
🔹
ما قبل از این مدت‌ها ارزان‌تر از قیمت جهانی، نفت می‌‌فروختیم اما حالا بالاتر از قیمت جهانی می‌فروشیم.
🔹
همچنین حدود ۲۰ تا ۳۰ درصد بازار جدید در فروش نفت پیدا کرده‌‎ایم.…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farsna/445644" target="_blank">📅 15:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445643">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7sgGoAd9BWURamVHLYLGiHL7H0W27UAWGzrsJVkfkvAqKKZmpzPLg6am0fKyyOYT5f5zS0CWCUD9RrqP7OJKuw0ehf9lgBVsdcEsbW-nSeq2jsqgO_Yc7WRIaU_HuHLI_G5uAOJmtEQvdD8RNMdO_xq9wC3z33j5u6aWOHnrACF0V2G42T6KRiWVKFrsg8JCstGnegGDJp-OtJN1B238HL-MFShEGIfFwDQT9piOTYGPqykztg2YxKuUboSfz1og3wh7-z-E_pYGAh6KsKPxXCnjLzVNx0zUulGGETO6Hw0n4RTrbDgpd2yYnK9SD_5CAIH79dFiNiR6HL-NkXfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات صدور اعلان قرمز اینترپل برای سران گروه‌های تروریستی کردی
🔹
تنهایی، وکیل پرونده تعدادی از قربانیان اقدامات گروه‌های تروریستی کُردی در گفت‌وگو با فارس: صدور احکام قضایی، اعلان قرمز اینترپل و درخواست استرداد برای شماری از سران و اعضای گروه‌های پژاک، دمکرات، کومله و پاک پس از بیش از دو سال پیگیری قضایی و بررسی شکایت‌های متعدد قربانیان صادر شد و درخواست استرداد متهمان به دولت عراق و برخی کشورهای اروپایی ارسال شده است.
🔹
شمار شاکیان این پرونده‌ها بیش از ۶۰ نفر است و ابعاد جنایات و تعداد قربانیان این گروه‌ها بسیار گسترده‌تر از مواردی است که تاکنون رسانه‌ای شده است.
🔹
عمده قربانیان این پرونده‌ها مردم عادی، به‌ویژه هموطنان کُرد و اهل سنت ساکن مناطق کردنشین هستند که سال‌ها از اقدامات خشونت‌آمیز این گروه‌ها آسیب دیده‌اند.
🔹
اکنون دولت‌های میزبان این افراد باید به تعهدات بین‌المللی خود در مبارزه با تروریسم عمل کرده و زمینه استرداد و محاکمه متهمان را فراهم کنند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/445643" target="_blank">📅 15:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445642">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0a535da08.mp4?token=eAaedld3o3SM8CkpQelF3dxJkRE1OaHtP5k9afc_UCkYa_KLw6cSjB70xlKKb9KkKxxdmlvDgWwVBvcXPaVyEm6aS5jepitHt4zyQ7b7sy-esrK8bsFQIiVQBrpqCoQPTfMcAB4ODx8vwtxW1QkkqgTTa63rdprodLbJwRnQgCndHbWH9gbUuM4UqoDrVcb1YLWdGC9axSyEe3t6yqEu23NSivQKchm81XL0L6xJ0N7TBGKb0hCAoTkG_A7mCHdN3zzbhJw5I3qAy0aLH_6u1KOFXkNaRiEa2nXJp2QTaiwTOIAIcCnN06sFwZL_GbkWTRK8U2iek0sxre2QbX2Y3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0a535da08.mp4?token=eAaedld3o3SM8CkpQelF3dxJkRE1OaHtP5k9afc_UCkYa_KLw6cSjB70xlKKb9KkKxxdmlvDgWwVBvcXPaVyEm6aS5jepitHt4zyQ7b7sy-esrK8bsFQIiVQBrpqCoQPTfMcAB4ODx8vwtxW1QkkqgTTa63rdprodLbJwRnQgCndHbWH9gbUuM4UqoDrVcb1YLWdGC9axSyEe3t6yqEu23NSivQKchm81XL0L6xJ0N7TBGKb0hCAoTkG_A7mCHdN3zzbhJw5I3qAy0aLH_6u1KOFXkNaRiEa2nXJp2QTaiwTOIAIcCnN06sFwZL_GbkWTRK8U2iek0sxre2QbX2Y3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: قالیباف قرار است به چین سفر کند؛ زمان سفر هنوز مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/445642" target="_blank">📅 15:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445641">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3028570678.mp4?token=V22q9Zvu8TDc35rwkINbLlpxnX_QFydbzdqcg17ZFH6Dl-JMIC9m-eoCN2gwnKLaHP_Ecyze3B4yRRPZkConQdIt6buexlkAr6_Elh4YwCBuNK0smmFR4nZN0A3c8FW-2cw3dw0eeAQjJW99Eacas5CU91oPh2Kd3QKE38kZ6DME-jq0VstH-bfPl1nM8Ai9DYKsUHdFGmokxE08tj2lOjeIGGQi7qvQ6JI9TP9_SR8YhLVAkstoG1eI9LfWCsTXzd0cXCOiB1Fuw7quGHjCfCt0QUlSWTn8-Bdx7O_HNXqWDSFwXKi46P0jbn2YTICqbeFXiyJvoAvmd5ahWcdh3y03aUOlcMC3_v3r1_NtoBKemEXBk0xoVAf_wgQzcFuWNsl9iW_NM2pyCen1vmpUPQiTi4k7DQGOh1TzQWLkiC3fo21--0XDyeW-CowG6tvTiT_bmGeOtEiw0h_eNGjDde10mt3imsYMFe0kSj0kUxlhiyqHdxQYXCHhxAUKmBc0hs-Xu-jZOP9WGfydOC3nTv3EhBVftQGu0Hi2vQo6AcsmpNSHICEamhx7lYdTnF8j-MU_dz6rovjjQNE4RD_kHNlf7w4SU_qie7n2iDuy4z_C2RZYTEk8dXuEVmxby8W57f69pEVFGk_pbQH929yMRU4C6195LmNBqhJve9MGmAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3028570678.mp4?token=V22q9Zvu8TDc35rwkINbLlpxnX_QFydbzdqcg17ZFH6Dl-JMIC9m-eoCN2gwnKLaHP_Ecyze3B4yRRPZkConQdIt6buexlkAr6_Elh4YwCBuNK0smmFR4nZN0A3c8FW-2cw3dw0eeAQjJW99Eacas5CU91oPh2Kd3QKE38kZ6DME-jq0VstH-bfPl1nM8Ai9DYKsUHdFGmokxE08tj2lOjeIGGQi7qvQ6JI9TP9_SR8YhLVAkstoG1eI9LfWCsTXzd0cXCOiB1Fuw7quGHjCfCt0QUlSWTn8-Bdx7O_HNXqWDSFwXKi46P0jbn2YTICqbeFXiyJvoAvmd5ahWcdh3y03aUOlcMC3_v3r1_NtoBKemEXBk0xoVAf_wgQzcFuWNsl9iW_NM2pyCen1vmpUPQiTi4k7DQGOh1TzQWLkiC3fo21--0XDyeW-CowG6tvTiT_bmGeOtEiw0h_eNGjDde10mt3imsYMFe0kSj0kUxlhiyqHdxQYXCHhxAUKmBc0hs-Xu-jZOP9WGfydOC3nTv3EhBVftQGu0Hi2vQo6AcsmpNSHICEamhx7lYdTnF8j-MU_dz6rovjjQNE4RD_kHNlf7w4SU_qie7n2iDuy4z_C2RZYTEk8dXuEVmxby8W57f69pEVFGk_pbQH929yMRU4C6195LmNBqhJve9MGmAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلی آمادۀ یک وداع
🔹
۳ روز تا آغاز مراسم وداع با پیکر رهبر شهید انقلاب در مصلی تهران باقی مانده و  مسئولان از آمادگی ۸۰ درصدی محل وداع و میزبانی از زائران خبر می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/farsna/445641" target="_blank">📅 15:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445640">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6721e5386c.mp4?token=OtaKt32wloDQ2S6xJW32duKBgNd7tVcK7yJv1gXP0WIfbDF9NRltrKibWxBmUHxmNNaDbi4D8QrO1bq0AUSV_1w7AGOb5zZaVIvky6FjvRFxo9XLzmXm6xoBH1Xe91CN6DG26Eu_P0kQ0yyDgHbqrq1lC25Bu1pG6yaOfsLunfW-oBcPl9ZbdxHdLTXIaoBupTeT9RuEodb21jHYAswhcvUXFy_xVtuLuV2mlrS7pAJQHr48SVF0K5HwbuJkQRTazGJdi2zponZI4HbP3eAiJ_0C7wZQDLBS80h1sfQWqTYBbW1hoNiEIgifeZgP9Apr6Fqfyr-r-4FDy3D2JPMYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6721e5386c.mp4?token=OtaKt32wloDQ2S6xJW32duKBgNd7tVcK7yJv1gXP0WIfbDF9NRltrKibWxBmUHxmNNaDbi4D8QrO1bq0AUSV_1w7AGOb5zZaVIvky6FjvRFxo9XLzmXm6xoBH1Xe91CN6DG26Eu_P0kQ0yyDgHbqrq1lC25Bu1pG6yaOfsLunfW-oBcPl9ZbdxHdLTXIaoBupTeT9RuEodb21jHYAswhcvUXFy_xVtuLuV2mlrS7pAJQHr48SVF0K5HwbuJkQRTazGJdi2zponZI4HbP3eAiJ_0C7wZQDLBS80h1sfQWqTYBbW1hoNiEIgifeZgP9Apr6Fqfyr-r-4FDy3D2JPMYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: ۵ هزار لبنانی در جنگ اخیر شهید شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/farsna/445640" target="_blank">📅 15:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445639">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b27c5566.mp4?token=r0WGaX-DSsQLO5IBbi7Pwqx2pMm9RFLyESx5olPj8-nKvdCmunPO9iCz1sxC6cbcslTmqEUBLOKkDsBfMGnMdCkxMFBEHGc3Lt9bfo8mWdGtwjsXscgljnWmD1QNiS9AroSsy3zlWKHN1zjr8c8TIjuuVZRZ0un2ClrCsxr3ZE0DINiBgM5InvrM5W3dSyv3nkYdXj9GIEglArSSo2dg3y0PTMz4s1lVBuJAvvgJNOBCHQEozKBxFrHStibwPgwBvoQJlEygmzKXn4suzmaLOAivD5AJSMIQiZZ04WAkOOCkl7K1c1qpXEwOF2OmS2-aCoUjl6qrw-qlGVPUK5_fog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b27c5566.mp4?token=r0WGaX-DSsQLO5IBbi7Pwqx2pMm9RFLyESx5olPj8-nKvdCmunPO9iCz1sxC6cbcslTmqEUBLOKkDsBfMGnMdCkxMFBEHGc3Lt9bfo8mWdGtwjsXscgljnWmD1QNiS9AroSsy3zlWKHN1zjr8c8TIjuuVZRZ0un2ClrCsxr3ZE0DINiBgM5InvrM5W3dSyv3nkYdXj9GIEglArSSo2dg3y0PTMz4s1lVBuJAvvgJNOBCHQEozKBxFrHStibwPgwBvoQJlEygmzKXn4suzmaLOAivD5AJSMIQiZZ04WAkOOCkl7K1c1qpXEwOF2OmS2-aCoUjl6qrw-qlGVPUK5_fog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رقص شادی وزیر آمریکایی پس‌از حذف ایران از جام جهانی!
🔹
مولین، وزیر امنیت داخلی آمریکا: خوشحالم که ایرانی‌ها حذف شدند و دیگر برنمی‌گردند؛ وقتی ویزاهایشان را گرفتیم از خوشحالی آهنگ خواندم و رقصیدم.
🔸
پیش‌تر فدراسیون فوتبال و اعضای تیم ملی ایران از برخوردهای…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/farsna/445639" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445638">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993e148d52.mp4?token=SCznZDRYyIdWoDte8aS3nyA8ROkdZwq0LtLcbOGCKEOnF9DoVycRyUFjVwAzp6555_Nn57m4JmCq9T7vPrCwkTyGNSrWhFignF9QciaAgmkCaMPTPxCXnm_jnxE2eOdS131X8KdbWCrSlBbuEHTO0VYs69LU2ncY09L9hiSMPaFE3pPGYZ-cPRnBWq48C-vowuxj5FddZNouBJI3e4HGEZAckYzkZNMgkm_PTT6fFol_Yg85SYlLjMJXRB9OWIcZDqGSrH8M16zmPnEXorAMqZkIbc4JkZcDLVmhNj9VzUmsuAkHf6ziDMMZzPso3MmMOxxhYbe28H6SkayAFGXpqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993e148d52.mp4?token=SCznZDRYyIdWoDte8aS3nyA8ROkdZwq0LtLcbOGCKEOnF9DoVycRyUFjVwAzp6555_Nn57m4JmCq9T7vPrCwkTyGNSrWhFignF9QciaAgmkCaMPTPxCXnm_jnxE2eOdS131X8KdbWCrSlBbuEHTO0VYs69LU2ncY09L9hiSMPaFE3pPGYZ-cPRnBWq48C-vowuxj5FddZNouBJI3e4HGEZAckYzkZNMgkm_PTT6fFol_Yg85SYlLjMJXRB9OWIcZDqGSrH8M16zmPnEXorAMqZkIbc4JkZcDLVmhNj9VzUmsuAkHf6ziDMMZzPso3MmMOxxhYbe28H6SkayAFGXpqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مرحلۀ سوم ثبت‌نام طرح مسکن استیجاری
🔹
طبق اعلام وزارت شهرسازی مرحلۀ سوم طرح آشیان؛ ویژۀ استان‌های گلستان، ایلام و کرمانشاه، از ساعت ۱۲ امروز آغاز و تا پایان روز چهارشنبه ۱۰ تیر ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/farsna/445638" target="_blank">📅 15:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b1316d32.mp4?token=KGbF82PXyYxwB8WtvGnWLwG04ssBauy3BWC2DwgULQjtkwCxGHvrh7PL6NryEEkHDSvion7pq3FMJqt3JgbcQfoSVqtEv_euXmbJpw_j39spYiRKCXrQLCfeoDp9-_PVZs3bGGR2gS-Qx3eT7VkILcJj9GWOWtIF8UNepPUshxTSLKftCm930uY6dAxZgYFPYVo_UZWJcTk4h8mHBRuTUtqxQBNrkt30xWmFPHsTZfsjJmlaiEuv0YSbvmDO01RwTzH-aGU77mJpk8mfeiw569ma5KmFPO3SdtRTJvAP3m7vmFrAtg98NGdstZ23IQR1tCWtAikGvF8cvSVvy-hreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b1316d32.mp4?token=KGbF82PXyYxwB8WtvGnWLwG04ssBauy3BWC2DwgULQjtkwCxGHvrh7PL6NryEEkHDSvion7pq3FMJqt3JgbcQfoSVqtEv_euXmbJpw_j39spYiRKCXrQLCfeoDp9-_PVZs3bGGR2gS-Qx3eT7VkILcJj9GWOWtIF8UNepPUshxTSLKftCm930uY6dAxZgYFPYVo_UZWJcTk4h8mHBRuTUtqxQBNrkt30xWmFPHsTZfsjJmlaiEuv0YSbvmDO01RwTzH-aGU77mJpk8mfeiw569ma5KmFPO3SdtRTJvAP3m7vmFrAtg98NGdstZ23IQR1tCWtAikGvF8cvSVvy-hreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: برای شرکت در مراسم تشییع رهبر شهید کشورهای زیادی در سطح سران اعلام آمادگی کرده‌اند
🔹
جزئیات حضور مقامات خارجی در مراسم طی روزهای آینده اطلاع رسانی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/445637" target="_blank">📅 15:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445636">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7187261dd.mp4?token=DEAo1Fyoupfj7bEKcAgjTHdZUiEjhNYPoD8wDHN6wdhB7dJOfl3UzqqF347XMUfSy9MDjWNkLy-C6zHtmVBbLqIw4IWTtkbT6YB-x91PuWeKeYkbExoSWVWtmbzj006TFWzFAeoIed31hrqrFFiXy_dqHMmugPrWGgfsAnmPk-H1_T2wKvqgSNPzR1HsHKvJuClaESzHFIf1kIECuyBB1BO85g4jZUMELDE9dZhhAz4TsRfSxLuZL-7x2lIN1teY4G_RPvQjJeNAMmYX-xAVC_LRT3qzktE_3ZwNBhpGGv8eF-ubjWdmqTnKezaL0yqoQl04EAkW9sRUa49Duo7Wbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7187261dd.mp4?token=DEAo1Fyoupfj7bEKcAgjTHdZUiEjhNYPoD8wDHN6wdhB7dJOfl3UzqqF347XMUfSy9MDjWNkLy-C6zHtmVBbLqIw4IWTtkbT6YB-x91PuWeKeYkbExoSWVWtmbzj006TFWzFAeoIed31hrqrFFiXy_dqHMmugPrWGgfsAnmPk-H1_T2wKvqgSNPzR1HsHKvJuClaESzHFIf1kIECuyBB1BO85g4jZUMELDE9dZhhAz4TsRfSxLuZL-7x2lIN1teY4G_RPvQjJeNAMmYX-xAVC_LRT3qzktE_3ZwNBhpGGv8eF-ubjWdmqTnKezaL0yqoQl04EAkW9sRUa49Duo7Wbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دَرِ فردو و نطنز چه زمانی برای بازرسان آژانس باز می‌شود؟
🔹
به گزارش خبرنگار فارس، براساس شنیده‌ها از متن تفاهمنامهٔ مذاکرات هسته‌ای، نقش آژانس بین‌المللی انرژی اتمی صرفاً در مرحلهٔ پس از توافق نهایی تعریف شده است.
🔹
براساس مادهٔ ۸ این تفاهمنامه، در اجرای…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/farsna/445636" target="_blank">📅 15:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445635">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyxZq8GIR7GVb-KnIEKH2bKTkoTjg6Tsk-SH36Buo42wCmuuphMsrBjG7SAF25UsY-miUsoIHzt65btaD7SgiN97s0l4fSNQoTh-DvjIvGpK-niPwe2UtplLMxfOfWBZejuXQHMVLGL1h9ySfLOLp7uAoif8ayd47m3vCD8bEvcqnC12GIeMEibL0bgV6BdOz5UrTovwJns3KVRmMmYrjmgdwlzhzZLiwLzGWImUZb8dpkTTKLjJ8IHqcwKF5jqOuAfMVDjscp4kHrLYnU997_vp7u7IIaa5SUPCK7q_b7a3t1YyapS2WIjk6STsYWwPpaHuF3hIIrKzK4tiNQu2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمیل‌ها و پسوردهای میلیون‌ها ژاپنی لو رفت
🔹
درپی یک حملهٔ سایبری به سامانهٔ ایمیل شرکت KDDI ژاپن، اطلاعات بیش‌از ۱۴ میلیون حساب کاربری شامل ایمیل و گذرواژه افشا شد.
🔹
این رخداد ۶ ارائه‌دهندهٔ بزرگ خدمات اینترنتی این کشور را تحت تأثیر قرار داده و نگرانی‌ها دربارهٔ امنیت زیرساخت‌های ارتباطی ژاپن را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/farsna/445635" target="_blank">📅 15:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445634">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ccfea6f6.mp4?token=LnEs3gpPSsHGLs6H22UQse942OnYE1AKfwaErKohtuaiYR5wh3sF9ui5TytOlKY7IWV1krE6u6KiSLUNFkZSkOkZWnQ2AkLvgQS4ZlnQfl3yAwSHaziRXm5URTcp6zJpQHVxponjBTcrkwXjd8o1KMb3GTatu17s-Bu5Hv55Dp9dFepMTGxQ142OgMBL-AZkg6Uaz_MVizZC0sNHmD4veYtK7PAc-Ht0JJ-XFeMA7y9Fs9cR3OCsPa4GF7j-0awplww0ph_DbbmrVt9ZlkqlgGwFtgyzSV8KZPuy3zU5KHbt-Uv9FpI1F5L1NFHiYfktXObHGAfc3RWeUpa7jSiR7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ccfea6f6.mp4?token=LnEs3gpPSsHGLs6H22UQse942OnYE1AKfwaErKohtuaiYR5wh3sF9ui5TytOlKY7IWV1krE6u6KiSLUNFkZSkOkZWnQ2AkLvgQS4ZlnQfl3yAwSHaziRXm5URTcp6zJpQHVxponjBTcrkwXjd8o1KMb3GTatu17s-Bu5Hv55Dp9dFepMTGxQ142OgMBL-AZkg6Uaz_MVizZC0sNHmD4veYtK7PAc-Ht0JJ-XFeMA7y9Fs9cR3OCsPa4GF7j-0awplww0ph_DbbmrVt9ZlkqlgGwFtgyzSV8KZPuy3zU5KHbt-Uv9FpI1F5L1NFHiYfktXObHGAfc3RWeUpa7jSiR7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما تا زمانی تعهداتمان را اجرا می‌کنیم که طرف مقابل هم تعهداتش را اجرا کند
🔹
متن یادداشت تفاهم خیلی دقیق و روشن تعهدات دوطرف را مشخص کرده است. آمریکا به‌عنوان طرف دیگر توافق وظیفهٔ متوقف‌کردن رژیم صهیونیستی در لبنان را بر عهده دارد. @Farsna</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/farsna/445634" target="_blank">📅 15:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445633">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2784e891c.mp4?token=dyy46p5rQNfu6zc49DJ_9234AkbEmkGz9zdnrouH67ANkYdhL72PtzcL6-5sBojCHyONHRzU79QF8i-0QEizazpRUkjHR0fdpObGVyh8StNZz1hpGcYxFGO-A8NRDFgMar0I7baiyi04i8iJSH2MnTa9aYJUvyNewxsQ-FxxFZnDk_paGsNAoaJnPG8Ub1pcXSyUVziBE8LA3qd_oPJvRMYZBB93xvwpk-ukZVa4KkIdEdxeOFTJoo6G6Fdc3ZcJe7xnmawdwGtc5q24lLL4HmHneEdCW29I7VDk7mpmEMgKLoGBotboBzBMBr9v-Lf2DogLt7dsWqzhCeVPJcYjug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2784e891c.mp4?token=dyy46p5rQNfu6zc49DJ_9234AkbEmkGz9zdnrouH67ANkYdhL72PtzcL6-5sBojCHyONHRzU79QF8i-0QEizazpRUkjHR0fdpObGVyh8StNZz1hpGcYxFGO-A8NRDFgMar0I7baiyi04i8iJSH2MnTa9aYJUvyNewxsQ-FxxFZnDk_paGsNAoaJnPG8Ub1pcXSyUVziBE8LA3qd_oPJvRMYZBB93xvwpk-ukZVa4KkIdEdxeOFTJoo6G6Fdc3ZcJe7xnmawdwGtc5q24lLL4HmHneEdCW29I7VDk7mpmEMgKLoGBotboBzBMBr9v-Lf2DogLt7dsWqzhCeVPJcYjug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: اتفاقات سوریه پردهٔ دیگری از اقدام‌های رژیم صهیونیستی مثل اشغال فلسطین و لبنان است
🔹
اقدامات رژیم صهیونیستی هم نقض حاکمیت سوریه است و هم امنیت منطقه را تهدید می‌کند. طرف‌هایی مثل آمریکا که از این رژیم حمایت می‌کنند، باید در مقابل اقدامات آن پاسخگو باشند.
@Farsna</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/farsna/445633" target="_blank">📅 15:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445632">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cbeddcc25.mp4?token=j3aaU9vEeRp99G8F6WlmxsKmJmO8ujEOwSzZpg81Vd7j3nM965Kttb8kMpTRI4al8ad69WIbPWJ0dKeZl0LWVsC6Tz5uwVlr8jIzV8WIAKNRKvbEX1AO8JY4K_zdTyIkFFP0cpBFY89pBkAjvuYFFI4w9F5f5ahWKJXrzUEUIQltnJo5b__7Ah3nL3lItFs_gDb__sGTSbbV_Z8O0307CkOjtQoIIPWSdlG6KNzwTqmAVIFtYM5Nsg35jbRpUdzYc7T71Pk1FpRslEjYsQ5g319w5w2A0VJtkg9wGwkS7zaQSTj_ylUZMOP4TV3R90WmUvt9Ylo7MdIKo1SB1kfvOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cbeddcc25.mp4?token=j3aaU9vEeRp99G8F6WlmxsKmJmO8ujEOwSzZpg81Vd7j3nM965Kttb8kMpTRI4al8ad69WIbPWJ0dKeZl0LWVsC6Tz5uwVlr8jIzV8WIAKNRKvbEX1AO8JY4K_zdTyIkFFP0cpBFY89pBkAjvuYFFI4w9F5f5ahWKJXrzUEUIQltnJo5b__7Ah3nL3lItFs_gDb__sGTSbbV_Z8O0307CkOjtQoIIPWSdlG6KNzwTqmAVIFtYM5Nsg35jbRpUdzYc7T71Pk1FpRslEjYsQ5g319w5w2A0VJtkg9wGwkS7zaQSTj_ylUZMOP4TV3R90WmUvt9Ylo7MdIKo1SB1kfvOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما تا زمانی تعهداتمان را اجرا می‌کنیم که طرف مقابل هم تعهداتش را اجرا کند
🔹
متن یادداشت تفاهم خیلی دقیق و روشن تعهدات دوطرف را مشخص کرده است. آمریکا به‌عنوان طرف دیگر توافق وظیفهٔ متوقف‌کردن رژیم صهیونیستی در لبنان را بر عهده دارد.
@Farsna</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/445632" target="_blank">📅 15:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445631">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a1313967e.mp4?token=hwD4YfFj25KF7gHe3jA6w47Ah8HBXlvDFjMxU75tLrwae3u1MW5_8yfwe9v-llC1gnwFD8hgyMCcltQSnPBtTrEiRYrErtjsHcAMGOQWifriJ3oEspKSuKSPOMLyy_q0wZaRekX8S7ZIm6V7FPLkQd0S8eaYZu_ULpkRttsyMEtnJI-e2Aab7DTH0gSHVfLcMDAGvmH6MqEEdF5i94bVK6Qsq5lq2VzN4OM7Kyb5Lu7du7aNcH7S4rE7_S12It-sQa1nYtLIPmS6VK7TL2LiDeNuplhnRtJd8yDsbPiHeulIZNv1BYTF6qhOdByHkMl7jG7BZPeC7rS-BQ0WCC_Oyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a1313967e.mp4?token=hwD4YfFj25KF7gHe3jA6w47Ah8HBXlvDFjMxU75tLrwae3u1MW5_8yfwe9v-llC1gnwFD8hgyMCcltQSnPBtTrEiRYrErtjsHcAMGOQWifriJ3oEspKSuKSPOMLyy_q0wZaRekX8S7ZIm6V7FPLkQd0S8eaYZu_ULpkRttsyMEtnJI-e2Aab7DTH0gSHVfLcMDAGvmH6MqEEdF5i94bVK6Qsq5lq2VzN4OM7Kyb5Lu7du7aNcH7S4rE7_S12It-sQa1nYtLIPmS6VK7TL2LiDeNuplhnRtJd8yDsbPiHeulIZNv1BYTF6qhOdByHkMl7jG7BZPeC7rS-BQ0WCC_Oyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: این که در جامعهٔ ما نظرات مختلف بیان می‌شود را باید قدر بدانیم
🔹
هر تصمیمی دربارهٔ وظایف دستگاه دیپلماسی با همکاری تمام ارکان نظام گرفته می‌شود و اینطور نیست که یک وزارتخانه به‌تنهایی دراین‌باره تصمیم بگیرد.
@Farsna</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/farsna/445631" target="_blank">📅 15:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445630">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUhU8BT53DDfuvWvHWtXYv9vknlUJU0LAJwHUr75u1nBlVwmvhEZJJketmfRfzIasoMxLx19sY3Dq8XsKWSsD26VKjFl3F5hiLIIvyKuHMZBb9yix__X8xjsvnOhRopkg8WjEiW5kepwVwW4da7oCnFuI235ONkrR4HsKr91X-fdTW35ijnyDtBGlisjMz1DBrX8RQMOdzibZTNgnach4vRwqVObMZf-KuwadWv9NASvET6PC8Y44TYX_R2IWjbMSUph3JWiDLhfNKmNM8C9lHLZwTq0sPi8FZ5apLeYPN4KjTbMecZLyUXL2mVVl5qq1CTQoeQx3dJzxJT5KooT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری تهران: ایستگاه‌های متروی مصلی، بهشتی و میرزای ‌شیرازی در روزهای جمعه، شنبه و یکشنبه تعطیل است.
@Farsna</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/farsna/445630" target="_blank">📅 15:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445629">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d605389536.mp4?token=aqoAAcUAc3q_0Ua-rksxAefOG4Rh9vD_TThS2hQxsDUMHvJ7-Rg93hb9V2c-ji-W--6aE5GMy75GdAPsephMVVOkSr1JvlVoZm2eUizY5cn0r4nLEsRMP-5i-Hcp4gV0Vj3pcZDJvxEvEUV26MlR8SnZLFbXH5k4pgDJfvHf6EoQmYhUZLuuXpVq2K9RfUsyw5lZKaBgsQH3UTyFy-r8hhQsCFi4aWl_j9OVzWfpz47F8-PU1Ub7deJo7ih4Rq5VGKLdSC7QDV9k7cmR_pV3uQ_h7QXDRi-4hBLdaYOeoC6XDo7egkQkPEb61cE9T1LxdAwH7u80Hg8RMA1bWMG-fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d605389536.mp4?token=aqoAAcUAc3q_0Ua-rksxAefOG4Rh9vD_TThS2hQxsDUMHvJ7-Rg93hb9V2c-ji-W--6aE5GMy75GdAPsephMVVOkSr1JvlVoZm2eUizY5cn0r4nLEsRMP-5i-Hcp4gV0Vj3pcZDJvxEvEUV26MlR8SnZLFbXH5k4pgDJfvHf6EoQmYhUZLuuXpVq2K9RfUsyw5lZKaBgsQH3UTyFy-r8hhQsCFi4aWl_j9OVzWfpz47F8-PU1Ub7deJo7ih4Rq5VGKLdSC7QDV9k7cmR_pV3uQ_h7QXDRi-4hBLdaYOeoC6XDo7egkQkPEb61cE9T1LxdAwH7u80Hg8RMA1bWMG-fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: از ابتدا برای ما روشن بود که ناتو در راه‌اندازی جنگ علیه ایران دخالت دارد و این موضوع را در محاکم بین‌المللی پیگیری خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/445629" target="_blank">📅 15:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445628">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Q-HwoDvC7VUh1DBfSNdi1Sxl7N_RDRQqYVFWQiKUprlsBSujkfVTIa3FNxDHwHy8kiwxVl5-s_y8LEr_gT3TGoN_TMsr3RunRgk8us5xKQP-NYf16EFZ3w8vccDyCu5wuUytpl1opZvby_e6r91tmPQaWhmz6gT2DWhFfNQP1T-7CjoHFREK9wqZBHlvjeb828QExt1gq2FfjYJDiBWPcBVUloJoATSgpYBlh068XCxIMcS5arhHt4eNKR_MysITuctP8Zmn27ft1ejS3bup9j3bHwYARQK-Ru2YpXFeWmRSL2atnr-f-DA9mjtLPoY94N8VhrGY68if11r4Eoy7XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Q-HwoDvC7VUh1DBfSNdi1Sxl7N_RDRQqYVFWQiKUprlsBSujkfVTIa3FNxDHwHy8kiwxVl5-s_y8LEr_gT3TGoN_TMsr3RunRgk8us5xKQP-NYf16EFZ3w8vccDyCu5wuUytpl1opZvby_e6r91tmPQaWhmz6gT2DWhFfNQP1T-7CjoHFREK9wqZBHlvjeb828QExt1gq2FfjYJDiBWPcBVUloJoATSgpYBlh068XCxIMcS5arhHt4eNKR_MysITuctP8Zmn27ft1ejS3bup9j3bHwYARQK-Ru2YpXFeWmRSL2atnr-f-DA9mjtLPoY94N8VhrGY68if11r4Eoy7XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت خارجهٔ قطر: اموال مسدودشدهٔ ایران آزاد نشده و آزادی آن به پیشرفت مذاکرات ایران و آمریکا بستگی دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/445628" target="_blank">📅 14:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445627">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tla4tSogDf1kMZUwBozOlSNt1yba9AHHOqlht5kO8gvvPMN-gnupuEmeC1ebWI0HMk5gw_o-3GCRec5CZsJ1EZ7GyteLovg2OV1BpkFJUsvFHsXH6rk5ErsZni6EIJguaYI_G0xY3MP9KaxivbUp-WIjrW_1BlWVtW4m1czYxvXLAfOtZrZQETBhjodSsKqCo8AY64ctC-OGcF4TAzStDwxJ6g9jEAcSdMX7TkkwP0Mt_KwydbVWFRivW8zG_pA20kd1_CFXTM1ZYYmbQE5GiABnGFh47gcz1YBvEUpTFVcTz94CaRadQIS7n151BFj7RBELvNv3IbpMjSgGyYQZ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران یک چهارم قهرمان جام جهانی پاداش گرفت
🔹
تیم ملی فوتبال کشورمان هرچند در مرحله گروهی جام جهانی ۲۰۲۶ حذف شد اما طبق افزایش چندین برابری پاداش‌ها شاگردان قلعه‌نویی مبلغ ۱۲.۵ میلیون دلار پاداش از فیفا دریافت کردند.
🔹
پاداشی که تیم ملی فوتبال ایران از شرکت در جام جهانی کسب کرده معادل ۹۳ شمش یک کیلویی طلا است.
🔹
نشریه آس می‌نویسد که قهرمان جام جهانی ۲۰۲۶ قرار است ۵۰ میلیون دلار پاداش بگیرد که معادل ۳۷۳ کیلو گرم طلاست.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/445627" target="_blank">📅 14:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445625">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95eb2851b8.mp4?token=KH7EhfD8FYVHdDWJ-kY7-d-peqDlyJftlrTVnyONBI4FBIbg87Fuhoio0DmvO2230NzM68r9wqwiK0wPpGwR0Md4r0YD2KKlNpSdvZOxjf6udj90ToNQeuu_TAPkWM9bwVKkkNZhDFuLrVm349r7HF30ScoYHXDN412_xFYyGUGlbImrXivkrml7oPSbrhjKpdMBuyehhL1ap5Ztud3zE9dQeIjs-TQT2lt4jfRvDlwAyZnC6RKisv_l_fZ_e-jxJhfiuZ8gcrujCh_Zd1C9i2_vBen1G9X9cLTkssUwG6kvA4_8F4Gz_WYmF7mhmhuJy8VXOvNUC4jeSeFMkMWuqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95eb2851b8.mp4?token=KH7EhfD8FYVHdDWJ-kY7-d-peqDlyJftlrTVnyONBI4FBIbg87Fuhoio0DmvO2230NzM68r9wqwiK0wPpGwR0Md4r0YD2KKlNpSdvZOxjf6udj90ToNQeuu_TAPkWM9bwVKkkNZhDFuLrVm349r7HF30ScoYHXDN412_xFYyGUGlbImrXivkrml7oPSbrhjKpdMBuyehhL1ap5Ztud3zE9dQeIjs-TQT2lt4jfRvDlwAyZnC6RKisv_l_fZ_e-jxJhfiuZ8gcrujCh_Zd1C9i2_vBen1G9X9cLTkssUwG6kvA4_8F4Gz_WYmF7mhmhuJy8VXOvNUC4jeSeFMkMWuqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند.
@Farsna</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/445625" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445624">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d0f8bf94.mp4?token=BM6rYpgqK8Hq99pDergxNRsNhzwpvFfAOjspqVDilGpIh_OAWZhNa7xL1h5buVPjmS1-iuYhl0fbVys1nF5zPQmRUGu6BXXUbwJtygS8vl02QH1f-SuZ8W0uLq5KFVh_Kr0nGvJYdC8qlWK217pph8KP0_YWGNmMdXIiNI03ABQrnRXBAYF3wLsM9gAc4acigjOlUKOScchKlBSIcSzGP6AIgUd5MEvqmv35sdanZmLSrQ87ZGpsoqeW9EIJsr7gLLLk9XZqaBN0979I9TuGoC_8eO1nNAXxpqBAs-9DkwwhzGc-AWn8S8IwSGvOTLdElwsu1JDyXKZxpehp5FPy8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d0f8bf94.mp4?token=BM6rYpgqK8Hq99pDergxNRsNhzwpvFfAOjspqVDilGpIh_OAWZhNa7xL1h5buVPjmS1-iuYhl0fbVys1nF5zPQmRUGu6BXXUbwJtygS8vl02QH1f-SuZ8W0uLq5KFVh_Kr0nGvJYdC8qlWK217pph8KP0_YWGNmMdXIiNI03ABQrnRXBAYF3wLsM9gAc4acigjOlUKOScchKlBSIcSzGP6AIgUd5MEvqmv35sdanZmLSrQ87ZGpsoqeW9EIJsr7gLLLk9XZqaBN0979I9TuGoC_8eO1nNAXxpqBAs-9DkwwhzGc-AWn8S8IwSGvOTLdElwsu1JDyXKZxpehp5FPy8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: ۵ هزار لبنانی در جنگ اخیر شهید شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/445624" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445623">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781702a3b6.mp4?token=Wn4Jwqj7xsP239roIQJ2zGdvYXN4RBIkKGWxV8ERGMnvKedIxDnNONMBOE5HGhAwXf6-ZV9NM1YWjbiu2vPZOzWiP_q10bJgdR3MVu_DOj3ZzE5BXJBHopUsqU80gxf9zMxBidTqec9JeGoxrBh3zsT4o_AA2H0YoyKGqD4b9kE6WN_Q1JCmmgT1xFxAB4bSiqAf1YTLy3L_an4x3y_as0LaKLyIRlejhQ5RTKdzDJXz1UvZj__NIg0SqZJzL5nkP6KGQ0WOSECCsq7hKNXpiEADnB6j27ByidGew-xktj1oFfAuhDkCLTDi4FFp7x9hGInSU6xnShNoOyt_Zsompw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781702a3b6.mp4?token=Wn4Jwqj7xsP239roIQJ2zGdvYXN4RBIkKGWxV8ERGMnvKedIxDnNONMBOE5HGhAwXf6-ZV9NM1YWjbiu2vPZOzWiP_q10bJgdR3MVu_DOj3ZzE5BXJBHopUsqU80gxf9zMxBidTqec9JeGoxrBh3zsT4o_AA2H0YoyKGqD4b9kE6WN_Q1JCmmgT1xFxAB4bSiqAf1YTLy3L_an4x3y_as0LaKLyIRlejhQ5RTKdzDJXz1UvZj__NIg0SqZJzL5nkP6KGQ0WOSECCsq7hKNXpiEADnB6j27ByidGew-xktj1oFfAuhDkCLTDi4FFp7x9hGInSU6xnShNoOyt_Zsompw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: اجازه نخواهیم داد هیچ‌ کشوری در تنگهٔ هرمز مین‌زدایی کند و جلوی آن را خواهیم گرفت؛ مین‌زدایی را فقط خودمان انجام می‌دهیم.  @Farsna</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/445623" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445622">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXAN_Nwp2A6G5mZLQGuhZ1-Dj-lXEUlF8p-jUhonRLbhgv077RSsM8efUBKeoTVnlkirODAtPyTGu0A3ui0py5By4s1zanH5K-mEgAZGN4z1jOzGn-eYDoYM9XOznWr0yxbJBcpscabYsgCYAAsHTvsBO_uX4wgCEGPxiq3moY7zhrymXz5xFrtitTql75jdguyUzIdbePbQklycA8IxWWjlhu63_4PoaiIXnF2lT2ups2aZmRk9KCqi1expwwivmxPHkDoJk0QIof4aXO4U-lrr5g_hTUML56zurN7iSNs5YH-vQymHylJ3ZPASpHvFKCf_sTaNhY4TYzMKnxfP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ فدراسیون فوتبال: اقدام دولت آمریکا در ندادن ویزا کینه‌توزانه و کاملا سیاسی است
🔹
در آستانه آغاز جام جهانی، دولت آمریکا در ادامۀ اقدامات کینه‌توزانه خود علیه تیم ایران در تصمیمی غیرورزشی و البته کاملا سیاسی از صدور ویزای ارکان مهم مدیریتی و اداری تیم ملی…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/445622" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445620">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6116f4d7b.mp4?token=lz4l_YM6FtEXei7KQlB_P3tH8zqO21qj6EYe2hHGBM7gHnYyTKLhenDUpcXo99DkPWB1CBI4_HBlYh3iiQtZvuBXoEPKlHMA4mKkck2Tx3dSBJsNqMN-jn4KEjb617e1zACy1nntyKyU2b5AXx_bYbbw1U7RJ6LuE-UTx3H6GkJQCjwzyiTm0b_IgPLbgRbpawtryIWY4bvrwOmFK7L7L2xxgDrQDhmZ-FQvccC4iNfpX-Q119K7hZYgWXe0itpM3wybbRDXrAkO4Twy2xliTql8mz2Cf9pv0VdhNwI9ErJYhk8lnD1m4n_kKMoroB-lDijyaBHMHtlun9EVgi5oSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6116f4d7b.mp4?token=lz4l_YM6FtEXei7KQlB_P3tH8zqO21qj6EYe2hHGBM7gHnYyTKLhenDUpcXo99DkPWB1CBI4_HBlYh3iiQtZvuBXoEPKlHMA4mKkck2Tx3dSBJsNqMN-jn4KEjb617e1zACy1nntyKyU2b5AXx_bYbbw1U7RJ6LuE-UTx3H6GkJQCjwzyiTm0b_IgPLbgRbpawtryIWY4bvrwOmFK7L7L2xxgDrQDhmZ-FQvccC4iNfpX-Q119K7hZYgWXe0itpM3wybbRDXrAkO4Twy2xliTql8mz2Cf9pv0VdhNwI9ErJYhk8lnD1m4n_kKMoroB-lDijyaBHMHtlun9EVgi5oSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین وصیت‌نامه رهبر شهید انقلاب
🔹
رهبر شهید انقلاب در خاطرات خود که در تاریخ شفاهی مرکز اسناد انقلاب اسلامی ثبت شده، اولین وصیت‌نامه خود را که در دوران مبارزات نهضت اسلامی در دهه چهل نگاشته شده است، قرائت کردند.
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/445620" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445619">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d7acb04c6.mp4?token=Htz0D8vgTdm4OYXH0ItpAywIxodx39u5G8xVF92zKzoYTQjM0KY0C5Y9s43DWN4DqPlZ7hiWQXn_VlXJiI_BP-kcsb7Xg1KVhcoZwz9d3nEGWQNaPr0QdbOrnkt_QgEUd3_Gfgo6yQO1mdErQTRqI4oMOfckVqM2NJ2wJZlt-JbqkYbDOXLkeDOruQp2YqU4k7lnm9LJBsl3pDmYGPesllQ_mGA_5qqVTmXrilNRdY76nLF8vcKKO_JdAEN0daCIhTGZMwQvbZZ7RHV9DTjDbvjZXrE1k65FfQ73el6BP2d8hqYqaqwsdB14XUT6EJf_6v8yrCmWtr0ZbJmTcYdemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d7acb04c6.mp4?token=Htz0D8vgTdm4OYXH0ItpAywIxodx39u5G8xVF92zKzoYTQjM0KY0C5Y9s43DWN4DqPlZ7hiWQXn_VlXJiI_BP-kcsb7Xg1KVhcoZwz9d3nEGWQNaPr0QdbOrnkt_QgEUd3_Gfgo6yQO1mdErQTRqI4oMOfckVqM2NJ2wJZlt-JbqkYbDOXLkeDOruQp2YqU4k7lnm9LJBsl3pDmYGPesllQ_mGA_5qqVTmXrilNRdY76nLF8vcKKO_JdAEN0daCIhTGZMwQvbZZ7RHV9DTjDbvjZXrE1k65FfQ73el6BP2d8hqYqaqwsdB14XUT6EJf_6v8yrCmWtr0ZbJmTcYdemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلمی دیده‌نشده از نوه شهید رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/445619" target="_blank">📅 14:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445618">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af5efa9d2.mp4?token=kUPmO5AJxBQbu6tbeRBqi07K0IM3wEctUtjPASEiCgwLmXw0WAU7ko0-B2ECPVzvXc7E_6WPATZ8T70SmAWs0Wod09yJqeY_fa2ZGDmVxghJUSeSlD772IN5yqxH01O01dLI_omSrw02q4PGV5DHpYApaqO8WVXmmFNmSa7qVpFU0NlRXaSRkQY7zDJ4EOj3pDA5dAaU853AE0YKMCiLDcgvAcl328CK-O8ogfdha-v34haEJgZlE3ZNB1TuGRqU5mtSGzcSjXtSLOi2GB-59LteiPNtJwWOts5-Ts7KvaI_nqrgIwXZrNtxa48KZtaOxlTadsociT44AuxF0gnzyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af5efa9d2.mp4?token=kUPmO5AJxBQbu6tbeRBqi07K0IM3wEctUtjPASEiCgwLmXw0WAU7ko0-B2ECPVzvXc7E_6WPATZ8T70SmAWs0Wod09yJqeY_fa2ZGDmVxghJUSeSlD772IN5yqxH01O01dLI_omSrw02q4PGV5DHpYApaqO8WVXmmFNmSa7qVpFU0NlRXaSRkQY7zDJ4EOj3pDA5dAaU853AE0YKMCiLDcgvAcl328CK-O8ogfdha-v34haEJgZlE3ZNB1TuGRqU5mtSGzcSjXtSLOi2GB-59LteiPNtJwWOts5-Ts7KvaI_nqrgIwXZrNtxa48KZtaOxlTadsociT44AuxF0gnzyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علائم گرمازدگی را بشناسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/445618" target="_blank">📅 14:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445617">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0vLvLb7HjQKbfzQ5ARiSBrCPHImjzxv2M6dv3GRZCgmyXbXPzXh5nOjBHbm5zJpB3KzPNVJ1ABcSYynAa1_uaN-2hXTxwZ81OAGNwVIbFVKMkj2zCyUtdqz2r-zSnweXeKDYcIdmgOTG2SAdOU9dXv8V8QI0AAdJxiCwJt7QnjGiyRIBhOwMMUx3SI8InTTHjmnReGI81myUPgmbr-nU5XmRJH0XVIq8dIbaDbqZs8lJz1JkFmIfBLBH0FzSbm0fo3Xx8gFqDtrp7qhKYpAKF2dlXnblf4NIJUnDdnZWBU3K46nFSbpZ1QbVtNCo46KjfK3CrtaldGvzA1_oH5GaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: ۶ میلیارد دلار از منابع مسدودشدهٔ ایران در قطر آزاد می‌شود
🔹
رئیس‌جمهور در دیدار با آیت‌الله‌ شبیری زنجانی: توافق اخیر، پیروزی بزرگی برای مردم ایران محسوب می‌شود و در چارچوب آن، تحریم‌های نفتی و پتروشیمی برداشته شده است.
🔹
دولت نیز هم‌زمان با پیگیری…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/445617" target="_blank">📅 14:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445616">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fc779408.mp4?token=rg-_IcdMHWgO1JNKjsI2MR0zFP28n-Gv8f45lor19JxyUKducJbcUiY0Jar6a-KDsCze9SeoA6RDjIgIrO6i9LsTb86wt-Woi8cfK7PoZXMnS0qu3e2H6jFaw2BXG4qzNQQcS_61CHN5aCAyoyZbgjq_UzcTktY8SnPjFtcKh7Y22o8HQrydHuUhC7q2iwPyGt6EP__ScH6nVuJ3_GQ7nYSZHSsinGOgTxzk3HnP412Bdoz8KinF_mRDW3QoMhhRK2eaCYpIdU5U_tOQsZaeOUWVbK4AK8ihhv_h_OOpBITUdnU7kz5egOIunkMQiELdhU_kx7iRxp8caczZzYXgGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fc779408.mp4?token=rg-_IcdMHWgO1JNKjsI2MR0zFP28n-Gv8f45lor19JxyUKducJbcUiY0Jar6a-KDsCze9SeoA6RDjIgIrO6i9LsTb86wt-Woi8cfK7PoZXMnS0qu3e2H6jFaw2BXG4qzNQQcS_61CHN5aCAyoyZbgjq_UzcTktY8SnPjFtcKh7Y22o8HQrydHuUhC7q2iwPyGt6EP__ScH6nVuJ3_GQ7nYSZHSsinGOgTxzk3HnP412Bdoz8KinF_mRDW3QoMhhRK2eaCYpIdU5U_tOQsZaeOUWVbK4AK8ihhv_h_OOpBITUdnU7kz5egOIunkMQiELdhU_kx7iRxp8caczZzYXgGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حلقۀ اول و دوم محدودیت ترافیکی در پایتخت
🔹
رئیس پلیس راهور تهران با اعلام حلقه‌هایِ مرکزی این مراسم گفت: در محدوده‌های اعلام‌شده، محدودیت‌های ترافیکیِ موقت برقرار میشود.
@Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/445616" target="_blank">📅 14:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445615">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22deb930a5.mp4?token=Nx7oIU_y-OkmvKBGjd-P48Q5NyiNmf_wsCV2pLoADgg6NS0yENAN5bpUs-5ZSjffzU-SazeFjUeVSASZ90OmVXSlhD4s7DTrbCKYj1TjlRNCO_Vr1ONqqTgGnDywiCsEugSwkn8LOOvirZL97Xd4KuZZa4IJb0YeeZp6yI3WpRplkxpLDGumBE3KAYOAebhjd2ZtJH85CiGFsC-CkRjtMXYdjAOkLXjO4CHHEunsilApn5Siu9fya7n1SrghojX1quSwx6bJ2F1yTXNa2kzhmrydOE9BGw9aufyKI9JR33BuofawnN0K3PDDc5by6CxTSYaem7Sg4FEL-U_NNree1IzIfL-k6ZijGtehdNdhLCm_RlXJf9sjUJm3Igd1a5FahwEfD6T506llDPZjdaaRKtJqJN_-poeEghc02yWjYVI21vp6yxgVQtJD6yHyeFuPrg0RvLS1149XuOt4_hiLEp9IwEf1nHoq8ahjpAfppdGwOgKo-PjLnsrfVM_s1hCUXWTK7w_rlZ0bYG8VAUHE7esqbi6IY2uefYSRnPFYXHREI3VqC63L6jY-LAskd3bzf6Q3KJ8jTSDQutJPYfS8tIwolYi-dLnG_fBOpw2vArIK2m8zy0Sl9NnaOZU_65KRUCn7ykETWDQQxJw-DMWoRCW51N-tv48Bn4tXRIqoUiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22deb930a5.mp4?token=Nx7oIU_y-OkmvKBGjd-P48Q5NyiNmf_wsCV2pLoADgg6NS0yENAN5bpUs-5ZSjffzU-SazeFjUeVSASZ90OmVXSlhD4s7DTrbCKYj1TjlRNCO_Vr1ONqqTgGnDywiCsEugSwkn8LOOvirZL97Xd4KuZZa4IJb0YeeZp6yI3WpRplkxpLDGumBE3KAYOAebhjd2ZtJH85CiGFsC-CkRjtMXYdjAOkLXjO4CHHEunsilApn5Siu9fya7n1SrghojX1quSwx6bJ2F1yTXNa2kzhmrydOE9BGw9aufyKI9JR33BuofawnN0K3PDDc5by6CxTSYaem7Sg4FEL-U_NNree1IzIfL-k6ZijGtehdNdhLCm_RlXJf9sjUJm3Igd1a5FahwEfD6T506llDPZjdaaRKtJqJN_-poeEghc02yWjYVI21vp6yxgVQtJD6yHyeFuPrg0RvLS1149XuOt4_hiLEp9IwEf1nHoq8ahjpAfppdGwOgKo-PjLnsrfVM_s1hCUXWTK7w_rlZ0bYG8VAUHE7esqbi6IY2uefYSRnPFYXHREI3VqC63L6jY-LAskd3bzf6Q3KJ8jTSDQutJPYfS8tIwolYi-dLnG_fBOpw2vArIK2m8zy0Sl9NnaOZU_65KRUCn7ykETWDQQxJw-DMWoRCW51N-tv48Bn4tXRIqoUiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: شبانه‌روز درحال آماده‌سازی مراسم وداع با رهبر شهید هستیم  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/445615" target="_blank">📅 14:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445614">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0638c37fdc.mp4?token=h5xcB_D4LvYryx555KI8nzzfGqq-aLHOPCBMCTw61eVaXMh74D_59iO_4TFZyeTJzHPPSk5ErrRifxzglcjRv_W11WisT1816iOSf5Xf5jmJHK1jLK3avKp2Z-_rgd22na5awnAxAHtP9p9hPaXoy4Anu0_GiH64lnUwMSHRh4Y9Kw3IDg9tqD_-97h0DFTQyY2iIbnM27dHl9A-yqCCvxoKjFFHZZaLaaZH2TQo-WJHCAcTYJ38xtcCwiNxzuQ_1Rjfrj1VX8Q7fFG-ahRkshnKjZmamzepiyme6ZoUhD3amABaCtBXiwHUsYaW51HYO3DxDmTqtZz2l7qp6uV1kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0638c37fdc.mp4?token=h5xcB_D4LvYryx555KI8nzzfGqq-aLHOPCBMCTw61eVaXMh74D_59iO_4TFZyeTJzHPPSk5ErrRifxzglcjRv_W11WisT1816iOSf5Xf5jmJHK1jLK3avKp2Z-_rgd22na5awnAxAHtP9p9hPaXoy4Anu0_GiH64lnUwMSHRh4Y9Kw3IDg9tqD_-97h0DFTQyY2iIbnM27dHl9A-yqCCvxoKjFFHZZaLaaZH2TQo-WJHCAcTYJ38xtcCwiNxzuQ_1Rjfrj1VX8Q7fFG-ahRkshnKjZmamzepiyme6ZoUhD3amABaCtBXiwHUsYaW51HYO3DxDmTqtZz2l7qp6uV1kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مذاکره در خارج، گفتمان در داخل!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/445614" target="_blank">📅 14:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445613">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎥
معاون وزیر خارجه: در طول هفته جاری هیچ برنامه‌ای برای مذاکره با آمریکا نداریم
🔹
حضور مقامات آمریکایی در دوحه ارتباطی با حضور هیئت‌های کارشناسی ایرانی در دوحه ندارد.
🔹
کارشناسان ما برای پیگیری تعهدات آمریکا از سوی قطر به دوحه خواهند رفت.
🔹
هیچ نشست و برنامه‌ای…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/445613" target="_blank">📅 14:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445612">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4rYNM292Jbc-N4mXnWHYTNejRRiJL1E7WvZWfOKj6HwK6iwjssqEJX-iOfLNz3QQf-rxAOXobswNaisK476gI3Q1Nnuf8ta7F1BaWdM4CgBXGWNkO4GMCoTMLu2_CHULo_Ek8OrHRQKg7hPFBpqrwX8-iPRVlTYDlT3Phh5q9Rr5nhvuzH2YjaKaVlHFdq_f-j9h-hfz34G6vQStE0tNc33GdfP9_uXJ-3BEBkqfAZPUzQcoxTOuUuu-F3N4fVAUsaYcrxkHykLMg3kLMVu2UPjYtlCS2oXgrasLqGYhc3PN30UYlVLIBGWeLazd6BxHGOvRzNwWfnTlsscTCQzGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌پورجمشیدیان: محل تدفین رهبر شهید نقطه‌ای انتخاب شده که در آینده امکان زیارت هم‌زمان برای بانوان و آقایان به راحتی فراهم باشد
🔹
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: برای مراسم تدفین پیکر مطهر رهبر شهید، یک آیین محدود پیش‌بینی شده است تا بدون هیچ‌گونه…</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/445612" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445611">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e58b6322.mp4?token=K2ZWp8ZYAFQBs9U_F_jcmvuM9NQP_5jRzY7tPYKzt4BDTmwdV2XhFMKSAzDirhIfnqBiX27det-soQm7UEsYKaVun6TH-eRK89t0-joPjkLhzayuFnDTEhFKqcp-4j2b7E_aU9952TqoS7X6YtSwwV_kxvM0o8cU9isOfMNCKIl_dCnRqXGHTg0Ka1V-SHd5InAhzRY0p6QN_O2IcWWbSeTFTtXIGkpVbHAwABxhKIVhm9HGG2kI_lnvU8OxlxlhXKkhKK2XiMtiB9TRWceC2aEQb_2tPrZpQe-fXHNoyf3AHLs2bYZaCvnSiImdfIwxVwNIZ3kpk5MMNQBp-HhpoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e58b6322.mp4?token=K2ZWp8ZYAFQBs9U_F_jcmvuM9NQP_5jRzY7tPYKzt4BDTmwdV2XhFMKSAzDirhIfnqBiX27det-soQm7UEsYKaVun6TH-eRK89t0-joPjkLhzayuFnDTEhFKqcp-4j2b7E_aU9952TqoS7X6YtSwwV_kxvM0o8cU9isOfMNCKIl_dCnRqXGHTg0Ka1V-SHd5InAhzRY0p6QN_O2IcWWbSeTFTtXIGkpVbHAwABxhKIVhm9HGG2kI_lnvU8OxlxlhXKkhKK2XiMtiB9TRWceC2aEQb_2tPrZpQe-fXHNoyf3AHLs2bYZaCvnSiImdfIwxVwNIZ3kpk5MMNQBp-HhpoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی جایگاه وداع با رهبر شهید در مصلی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/445611" target="_blank">📅 13:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445610">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2GWgajw-Xg5N2OJ0DWI48mVbe1i1AA5rU3SqxZBAQvGtj_k26LQ-4Zoa-6llRySw2d0CTmEPYftSEXvExu8jX09pMBu-ABjaotE1ZaP5AF0OpzuFTCl4WZE7d6bsiKmxQ0z_YnO56MKiXbBWkRutZ0j2iEuLZe9oPXFED5dOnHcMfYPBJGlmbNrFie4QLsc8Mfojd64qybq4mT7DC9c8umSjOGcxP3A1WkUXAzE6ACdhEhfaQwbGuQaTBgq8_M51YTknmWMiUox2bU8zzuQtKE7GsEEAaIjY1fCFuDRMIZcIvuoT8I-VtafZmDx_D8IwoM11DATscSFDYH8ob0GQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج تودهٔ ۹ کیلویی از یک بیمار در شهرکرد
🔹
منصوری، متخصص زنان‌وزایمان: در عمل جراحی یک بیمار ۴۹ ساله در شهرکرد یک توده به‌وزن ۹ کیلوگرم خارج شد؛ این جراحی با موفقیت به پایان رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/445610" target="_blank">📅 13:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445609">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8Q2ur1TrjKD1PDVwfAE6P3vS9tRK82ViUdl49_g-HzH25sJ46I1gpNWy21FW7jcRBgKwIezI_A8Eyf_PY9fmSjERbRcljDv1F19rcT1olmldRAQ5w1kFsLlR1_f-sx0IAtaF2mzcyDMKz-uB_QC7B2zvJACgT66lXUSpV1RHJFJxb2Gx2XmRDimc6B3ylrvf8pQ1K9kLVq5seYgjNIKqG3ajAOHyXgv5wPGyKbzS1Gp91Pl_4V4ABOP31TaBQ1LNgE_2jizpvxPkkQ3kFxt45KuDiw_fBvp_g3236Wkg9UVwqJF9tMY1LyF4CEof6ojq0Cnt5aVEcOiMWDx0EuT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺️
#پوشش_بیمه_ای_زائران
و شرکت‌کنندگان در مراسم تشییع رهبر شهید
🔹
صنعت بیمه کشور در راستای ایفای مسئولیت اجتماعی و تامین آرامش خاطر مردم، تمامی شرکت‌کنندگان در مراسم وداع، تشییع و تدفین قائد عظیم‌الشأن انقلاب را تحت پوشش کامل بیمه‌ای قرار می‌دهد.
🔹️
به گفته موسی رضایی رئیس کل بیمه مرکزی، کنسرسیومی متشکل از ۷ شرکت بزرگ بیمه‌ای (ایران، آسیا، البرز، دانا، سامان، نوین و آرمان) تشکیل شده است تا پوشش‌های بیمه‌ای لازم را در چارچوب قوانین و مقررات مربوطه عرضه کنند.</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/445609" target="_blank">📅 13:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445608">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشرکت پارس خودرو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGc7mRlz6-hJHu5CAUieMlL8hbNRXxfb6q7lfbTKgC0OlnC86zXOznZVp2N-6MU7NXI388f0nWmWwPdzdhJIbgjxO4VTPPFuJy4nCdvnXGzGGdWQZ1A3i42x2mw3oBc7Ev3yJQK1AdQ509O5vBcu43rebC3lxDJGd04ujDPSRMxjXr5-J4_wWEAbu64_f5pt6JUcKO6pPmY5JVYoScBDOVvq5yoi1EOejwtqBQJVJUEmWdzbfdMQIjPVkTqclGhC2m72b4sfxt9BjvOXsN6gx4ySQDhtPF7n4txH_tfNkw444pYBlgEuo3Fav6130AI9CbuGOkX-P7XqaIJsdSrDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت بانک ملی ایران از توسعه همکاری‌های مالی با پارس‌خودرو
معاونان ارشد بانک ملی ایران در بازدید از شرکت پارس‌خودرو، با اشاره به ظرفیت‌های این مجموعه خودروسازی در سطح ملی و منطقه‌ای، بر حمایت از برنامه‌های توسعه‌ای، تأمین مالی زنجیره‌ای و تقویت همکاری‌های مشترک برای رونق تولید، اشتغال‌زایی و نوآوری در صنعت خودرو تأکید کردند.
بیژن نصرتی، عضو هیات عامل و معاون بانکداری شرکتی بانک ملی ایران، در این بازدید با ابراز خرسندی از حضور در پارس‌خودرو اظهار کرد: «خوشبختانه امروز از نزدیک شاهد پیشرفت شرکتی هستیم که یکی از نمادهای خودروسازی ایران، منطقه و حتی جهان به شمار می‌رود.»
جزئیات بیشتر:
https://news.parskhodro.ir/news-archive/id/5082
#پارس_خودرو_توسعه_تولید
➡️
@parskhodro_pk</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/445608" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445607">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/445607" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445606">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIY4bWDodPzteYmOy4e31wA4HCvTqx9AHQsfFRQtrzyjNMNvkqw3U2NvYLgCXRIMHuwegizAH1m2NytRCL3kAE-TQaK_WX63X_7rl9rfOFjuDJHOXih9WUMDlmX5UefRYihhUk8xa0_5B-osmTyEtzuiqgrO3OGv8pbXx3tZr33Co4qkxg0eUjKN-drvtVXhzRndWeLplU-OdXdk_yjf62kntflt2Lr7Ya_UfpR6RsBClNdwHcOwF5Ce0UYSVkgSRjJ4u9xWPe1R29pAbs9ujk661IplRx470wS5FuemTkq9Mgc1FZnSu8gq7gg8FMKNVRmyZzFtIuM94Zsetwidow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445606" target="_blank">📅 12:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445605">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c15c2103.mp4?token=dcbSgQ2n7_cAAWy5_cirwa7PpcDTn-KzL4oJukrWhv00ph0RaPoxJV29mrLz95OYcNaAHr8Ky4rv2K1oAOUh6jVZAzJpNhaDM3-iDynNu35xtUssLw145ik-HzUyfQVdZ3iivdBB9sf6Sai3EmmVIeiloBTt0VKuml7iWrsEkntmwQLIx8awFf8tkTlrdAi_m463KWEslhbXPvNP9908D-lMnyzHJ5156z_2IfbluRpzOsgsdn4dS_fYvGWMb9NG4jnI_9wgkRAAO8GMArrbKCtEK22Ms0o9qeXp8plG0y_geL1MKsX8UwRh3UOQsV1sF0pYI0uSiK6fj_tCt9LlBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c15c2103.mp4?token=dcbSgQ2n7_cAAWy5_cirwa7PpcDTn-KzL4oJukrWhv00ph0RaPoxJV29mrLz95OYcNaAHr8Ky4rv2K1oAOUh6jVZAzJpNhaDM3-iDynNu35xtUssLw145ik-HzUyfQVdZ3iivdBB9sf6Sai3EmmVIeiloBTt0VKuml7iWrsEkntmwQLIx8awFf8tkTlrdAi_m463KWEslhbXPvNP9908D-lMnyzHJ5156z_2IfbluRpzOsgsdn4dS_fYvGWMb9NG4jnI_9wgkRAAO8GMArrbKCtEK22Ms0o9qeXp8plG0y_geL1MKsX8UwRh3UOQsV1sF0pYI0uSiK6fj_tCt9LlBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور: ممکن است نیاز شود برای تخلیۀ جمعیت برخی آزادراه‌ها مثل تهران-قم یا بالعکس را یک‌طرفه کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/445605" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445604">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a798239640.mp4?token=sBV3WVIgLKyozTSVE63Yac-FPpjEi8nm8uaPWh3jJ0QO4hYhwgcu1JH8oDyaHMH1HgAMpgD3yvmccLVs6Rtqbz_03wWr_b_h2dekuuVJt7uEfSxj2ct-WRP4whL4QCTZPE-MEmD9X_qNj904ACsrpE0JZygtKPwZsXPn5b9xe4awaIufRqyR-sSIGV5fTTH2Nit5BJo4emuK4VPTiwZUJwxUqH9gEIxVVU70hEvam4rul0FLgGug71vMlnlrh3tfTrwlTHUz4zUrw5ZMtv4_xL7I-QuWsL8cZmeMhzIHBWF3MQBGfQK8BwU21caVeU2Xd2YPJUU-Prhu10iTXI4mFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a798239640.mp4?token=sBV3WVIgLKyozTSVE63Yac-FPpjEi8nm8uaPWh3jJ0QO4hYhwgcu1JH8oDyaHMH1HgAMpgD3yvmccLVs6Rtqbz_03wWr_b_h2dekuuVJt7uEfSxj2ct-WRP4whL4QCTZPE-MEmD9X_qNj904ACsrpE0JZygtKPwZsXPn5b9xe4awaIufRqyR-sSIGV5fTTH2Nit5BJo4emuK4VPTiwZUJwxUqH9gEIxVVU70hEvam4rul0FLgGug71vMlnlrh3tfTrwlTHUz4zUrw5ZMtv4_xL7I-QuWsL8cZmeMhzIHBWF3MQBGfQK8BwU21caVeU2Xd2YPJUU-Prhu10iTXI4mFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلیس راهور: از هموطنان درخواست می‌کنیم در صورت امکان از خودروهای شخصی خود استفاده کنند
🔹
همان‌گونه که هر سال در مأموریت بزرگ اربعین با محدودیت ظرفیت ناوگان عمومی مواجه هستیم، در مراسم تشییع رهبر شهید نیز در هر ۳ شهر تهران، قم و مشهد چنین شرایطی وجود دارد.…</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/445604" target="_blank">📅 12:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445603">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twga028AO3x1m9qxm6h2KokxTm6ZHSTD2RlalBM3raG1jmhxQ7mHZTg2GS1triUhedwknyzs6Reh0709udKWahu7NxuWr3axmNy4p5EumM2rcl9g0USEfzoUgwNxSYlzku2mo9ziejPkDzS5fqfKWU0bJK6ETCzFCLXhY4vfgTh1kNc4TCeOW0eb8moJqnUtTMpamK4yU9OmqrgI0m86igRDsMIs4TifSjo5tBh5uHdE855KJwmDrJyJ3hxXYbN8Q9JeQudsPdr9RKDoPRXcVDDRhVtOjwYivh7Q8HFxE6DgV2eizg6yskXi-mwyHOPqKNUdo3dfE1JHGn7iaNlYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با جهش ۶۸ هزار واحدی به ۵ میلیون و ۱۲۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/445603" target="_blank">📅 12:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445602">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01275ed274.mp4?token=Rqnd3nXt5oiFqOGKSu3M8sZZxJdn8jVJ2VvT6Y-dYqUExLzhhuTFvbtL_FwNH_zFXUrSXvrRr5ZydlX97ZdvBBi3H3Ym1NdzeT1lCRJGG36qWsDusD68xEwIol2b0o2m4nCHlL2oE_KJDQmj6UncMDp6v80DKelidkhmOGdUBSLNBMGP__sRmWsMsjAPP-okLHMIJVR_mHf6i2ME8mDf_lmVUrTUvm9PJqS-QN3MLPTkWFEnxo25wW7lf7pHxVR0Q2XBtjeE1a7o1TjQvdycLw6i7PlOppimWU9AnxclARl_GtxxbrZLAEFCLHXlBJjCmuE9wC0SbssAtFMJUxxQNTegIuxvcA5YegJEB5AGaQL8fDbgvYSqY3-zSt1hBp6ycAZuonCiGn1DHvZknt6Oe12lx0mgo8B3MIsQ6CzqFHPLj8SW6zv8rdcLg3Kpf4AlDsKJAjohItwDy5OyVSeyI9f84_GtoRjPFLfNJ4Xo5V9GQC1Tdj5gRQQGPKzL3AyLQTQo3fgT8Zf_za8eM1j-CiFdzAjyElIuazrOe2Dfk7DQl__mUmg8eyHGWc2vSYPGkR5DSxcPC-lWnvhPXlw_2-5foK4WkOLOi_FbBRi7EG9I_7O-kirTi0H5LuXvd0nNFH-LJOKZaahKfYoiclC7Uu_27ahFhzGDwMmwGDZwhGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01275ed274.mp4?token=Rqnd3nXt5oiFqOGKSu3M8sZZxJdn8jVJ2VvT6Y-dYqUExLzhhuTFvbtL_FwNH_zFXUrSXvrRr5ZydlX97ZdvBBi3H3Ym1NdzeT1lCRJGG36qWsDusD68xEwIol2b0o2m4nCHlL2oE_KJDQmj6UncMDp6v80DKelidkhmOGdUBSLNBMGP__sRmWsMsjAPP-okLHMIJVR_mHf6i2ME8mDf_lmVUrTUvm9PJqS-QN3MLPTkWFEnxo25wW7lf7pHxVR0Q2XBtjeE1a7o1TjQvdycLw6i7PlOppimWU9AnxclARl_GtxxbrZLAEFCLHXlBJjCmuE9wC0SbssAtFMJUxxQNTegIuxvcA5YegJEB5AGaQL8fDbgvYSqY3-zSt1hBp6ycAZuonCiGn1DHvZknt6Oe12lx0mgo8B3MIsQ6CzqFHPLj8SW6zv8rdcLg3Kpf4AlDsKJAjohItwDy5OyVSeyI9f84_GtoRjPFLfNJ4Xo5V9GQC1Tdj5gRQQGPKzL3AyLQTQo3fgT8Zf_za8eM1j-CiFdzAjyElIuazrOe2Dfk7DQl__mUmg8eyHGWc2vSYPGkR5DSxcPC-lWnvhPXlw_2-5foK4WkOLOi_FbBRi7EG9I_7O-kirTi0H5LuXvd0nNFH-LJOKZaahKfYoiclC7Uu_27ahFhzGDwMmwGDZwhGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمادگی مردم قزوین برای میزبانی از دلدادگان رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/445602" target="_blank">📅 12:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445601">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjDiMGoC0t18B9LuZIJevp7K38NpHtjcgKWaZO7boFdWsV5cnArzCkgQugfDKoT10Ntx04EvGVfcTGNIECkRkT8Bo2CCPMdRzdEdpSFga_6_ALHHrme-FZd6C9ztGkd5A91yzQBqEatM8rB8jgUKuqyLfbYxDHLvdV5U3s-hwRavRls8yGdKcEMT_HYd2mfD5oT-9FSv9Ckvj5U1I4IC3nTHAkb2nW_qzBAJYOlRgPcw3FP9Y8mnF_Xk0kvSLXXwpyXkuiM8m2DNjmikV33keaDELoS6Tp_neaOCvt6jh_R5TaXdUO5g47VbQPuj-PHcTpaqlAWsxVRgzQ_JMtnNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش‌از یک میلیون ظرفیت اسکان برای تشییع رهبر شهید در تهران
🔹
استاندار تهران: برای مراسم تشییع رهبر شهید در تهران، حدود ۷۰۰ آمبولانس، ۳۸ اتوبوس‌آمبولانس و ۳۰۰ موتورلانس در مسیرها و نقاط تجمع مستقر خواهند شد.
🔹
همچنین بیش از یک میلیون ظرفیت اسکان در اماکن عمومی آماده شده است؛ برای مقابله با گرمازدگی نیز اتاق‌های سرد در مناطق پرتراکم پیش‌بینی شده است.
🔹
بیش از ۶۰۰ خبرنگار خارجی برای پوشش رسانه‌ای مراسم حضور خواهند داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/445601" target="_blank">📅 12:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445600">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334b14fe3d.mp4?token=nO76pfIoQnhY7M22G--WeYIVm_KoexPrifONOXA0hy4SkPCxRNWF2dR7RCSbELLJrOE2_686a4g19AvtqylVQqGbHeEkyHuTDPsFGyU7vGK8oajgtHoxhzcr6fuyDfMSxa3UkuXennAWUnwIUt9vmMTT7y5wbw6bGvBBbv_5EzzD2BWhAVF8oqgAsOYVAm5cm8S3QzPqamGS15TphrWLj5mP41J3VvNJWcisb1cpX2kGYGm071PPOeg6uM03iTBgilOes7PnRHETpho9JkM_laJFQAp8irFmL0OYj0Hw14YFyg5Sw81R6wQgSTKp13v4mZ55vLSwYQN3D8D0tZKzLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334b14fe3d.mp4?token=nO76pfIoQnhY7M22G--WeYIVm_KoexPrifONOXA0hy4SkPCxRNWF2dR7RCSbELLJrOE2_686a4g19AvtqylVQqGbHeEkyHuTDPsFGyU7vGK8oajgtHoxhzcr6fuyDfMSxa3UkuXennAWUnwIUt9vmMTT7y5wbw6bGvBBbv_5EzzD2BWhAVF8oqgAsOYVAm5cm8S3QzPqamGS15TphrWLj5mP41J3VvNJWcisb1cpX2kGYGm071PPOeg6uM03iTBgilOes7PnRHETpho9JkM_laJFQAp8irFmL0OYj0Hw14YFyg5Sw81R6wQgSTKp13v4mZ55vLSwYQN3D8D0tZKzLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/445600" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445599">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7BlMv3F9eHVHpZ2gtL_GIfB3_2oVZxCL3yvDdmmy69zVPtGKxJfTuI6L_hhTYQaojHt1d-lwbZnTPcnGpzdmFsmrBhNBszlPaipzqL7Tt2DeRL9N5mIGluUfO7dIHWVEcCVgQpqtXyvd4MOEVymeKkCjZdAKO7haYT71oLNqG1_Ab3vPtjcIFZpupJhF6LhIF-cEiBgkHyFfn_c_n7L5BkBO8WAkiCPMpNLFbZMy8O-lB00eQAm8bFcliNC3SKz2lvKlBS3V6BTo2O_H1xlYDjynfpBt_ynwrnUxsAkMfs8mV5VPxRL1efArOh1_h9BzklJoYBV4rVPOcm2opv78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متلاشی‌شدن یک گروهک‌ تجزیه‌طلب در مرزهای شمال‌غرب
🔹
قرارگاه حمزه سیدالشهدا(ع) نیروی زمینی سپاه: درپی ورود یک تیم از گروهک‌های معاند و تجزیه‌طلب به مرزهای شمال‌غرب کشور برای اقدامات خراب‌کارانه و تروریستی، این اشرار در کمین رزمندگان قرارگاه حمزه گرفتار و به صورت کامل متلاشی شدند.
🔹
این درگیری در ارتفاعات مابین شهرستان‌های مهاباد و پیرانشهر و با پشتیبانی آتش ادوات صورت پذیرفت.
🔹
در آن درگیری، این تیم ۶ نفره به‌طور کامل منهدم شد و اجساد ۴ نفر از اشرار به همراه انواع سلاح و تجهیزات در اختیار رزمندگان اسلام قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/445599" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445598">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab10b6d9fb.mp4?token=Zbjbdh2varFRsCv3WJxp1vIDJToKrjHEDLdzvvjBIphJ4qlrYnTfyJSSCU44D6wPNkPgj-R02o4M56Slpf37XtLfHlfUV9U_9AJuxVvgxN0NhOovwlJHzv9WMm8hXNf1ed9lm_VwbM-cAtCKEYtEU3oEdAWE-Lj3hfpLQ6GDAEGp6asYT9JTXWhGpdH9gJqqfauUFMjUi5kuxWFjE6SgjJ0rayHShkjt19S5xPc_jRYEkLOFG8Th5WiBW17iLHbW45DTSDVwCF_a5p6HX-LcTEOOVtxFk2v7NsV6NFHHy8o4wWAsiVXI5Y9IS3YUdTaoX8wTV3mQPqwk-19HPFVX_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab10b6d9fb.mp4?token=Zbjbdh2varFRsCv3WJxp1vIDJToKrjHEDLdzvvjBIphJ4qlrYnTfyJSSCU44D6wPNkPgj-R02o4M56Slpf37XtLfHlfUV9U_9AJuxVvgxN0NhOovwlJHzv9WMm8hXNf1ed9lm_VwbM-cAtCKEYtEU3oEdAWE-Lj3hfpLQ6GDAEGp6asYT9JTXWhGpdH9gJqqfauUFMjUi5kuxWFjE6SgjJ0rayHShkjt19S5xPc_jRYEkLOFG8Th5WiBW17iLHbW45DTSDVwCF_a5p6HX-LcTEOOVtxFk2v7NsV6NFHHy8o4wWAsiVXI5Y9IS3YUdTaoX8wTV3mQPqwk-19HPFVX_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
🔹
در حالی که این دونالد ترامپ بوده که برجام را پاره کرده و از آن خارج شد، اکنون مقامات دولت دوم این رئیس‌جمهور اذعان کرده‌اند که برجام «یک توافق واقعی بوده» و تفاهم‌نامه جدید با ایران قابل مقایسه با برجام امضا شده در دوران باراک اوباما نیست.
🔹
کاملاگر داو، نماینده کنگره آمریکا، بخش‌هایی از صحبت‌های تلفنی روز گذشته وزیر خارجه آمریکا مارکو روبیو در مورد تفاهم‌نامه ایران و آمریکا را افشا کرده است.
🔹
به گفته این نماینده آمریکایی، روبیو در این گفت‌وگوی تلفنی تأکید کرده که «این تفاهم‌نامه فقط یک تکه کاغذ امضا شده است که می‌گوید ما به صحبت درباره صحبت کردن ادامه خواهیم داد.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/445598" target="_blank">📅 12:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445597">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8611085f0d.mp4?token=AVNW2ppG3Hp9gsSxHPUCXgXGle_yaSsN71p2dJ_t7L4dNsOJttRazKI0AG12qzBHNTidkQbWCTMGjzLYjuUpK_AVfIfya__EMJWMJa7MoVa1X_xCsB56qp5zAKvFqMUbGLdX-tSPFeVRBOSw3rxvYub5Z2Uqn_c-QC3C8QfwmDCzpvlU1WFrU74w7TNVZb7KdyTzeILHR2Nc5fUFMAmGRpkKc4ex__zAGdQPMB_XWDwkx9HUJCAoDiTQzN0Ru6s4rLZJL20uoQZ8r1Nqp3OMHeMMjqJ9WZe5bpgpGtr1_zCPVUO7hpgFj8TVP_emZzvNO2RE2CTrF2yyRrCOhpQJkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8611085f0d.mp4?token=AVNW2ppG3Hp9gsSxHPUCXgXGle_yaSsN71p2dJ_t7L4dNsOJttRazKI0AG12qzBHNTidkQbWCTMGjzLYjuUpK_AVfIfya__EMJWMJa7MoVa1X_xCsB56qp5zAKvFqMUbGLdX-tSPFeVRBOSw3rxvYub5Z2Uqn_c-QC3C8QfwmDCzpvlU1WFrU74w7TNVZb7KdyTzeILHR2Nc5fUFMAmGRpkKc4ex__zAGdQPMB_XWDwkx9HUJCAoDiTQzN0Ru6s4rLZJL20uoQZ8r1Nqp3OMHeMMjqJ9WZe5bpgpGtr1_zCPVUO7hpgFj8TVP_emZzvNO2RE2CTrF2yyRrCOhpQJkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پورجمشیدیان: مراسم اقامه نماز و تشییع پیکر رهبر شهید در قم ۱۶ تیر برگزار می‌شود
🔹
نماز توسط یکی از مراجع تقلید در مسجد جمکران اقامه خواهد شد.
🔹
بسته به فراهم بودن شرایط، مراسم تشییع نیز در شهر قم برگزار خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/445597" target="_blank">📅 12:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445596">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a4107893.mp4?token=VJ2Mb-zNiC7r34VM-RrX9Hm2aLqolhloT8hv6VmZGNuHNxGyJPoM2M0rGWvrh4XETQleQk_NWWNrxTw-1cvd4E0niDo9obJohuCGq2-Da3jUCdwNa504rBOauy-XFv8dsq0yTIVT2mCeLRQ0g0aw7MfsFfTRh19u4LP7Mh3RS15AwLA2blQQ5HfL5CHYLgOtItI1ycxhv8ddh2YSTP7Ly5YyXE_IVzTK9yuYMqWHSVN4PaO-0panzR77JqQbGMlznPaecmfwP6KyhC6u77SQlyz7AZgimHP1uOUP-WjRzb9RZMVmSbd7FVuf8IW3xrTB0r32WxwxjX9VPA-d3ahXFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a4107893.mp4?token=VJ2Mb-zNiC7r34VM-RrX9Hm2aLqolhloT8hv6VmZGNuHNxGyJPoM2M0rGWvrh4XETQleQk_NWWNrxTw-1cvd4E0niDo9obJohuCGq2-Da3jUCdwNa504rBOauy-XFv8dsq0yTIVT2mCeLRQ0g0aw7MfsFfTRh19u4LP7Mh3RS15AwLA2blQQ5HfL5CHYLgOtItI1ycxhv8ddh2YSTP7Ly5YyXE_IVzTK9yuYMqWHSVN4PaO-0panzR77JqQbGMlznPaecmfwP6KyhC6u77SQlyz7AZgimHP1uOUP-WjRzb9RZMVmSbd7FVuf8IW3xrTB0r32WxwxjX9VPA-d3ahXFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۴ تیرماه نماز بر پیکر رهبر شهید در تهران اقامه می‌شود
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: چهاردهم تیرماه برنامه نماز بر پیکر مطهر رهبر شهید انقلاب اسلامی و خانواده گرانقدر ایشان در مصلای حضرت امام خمینی(ره) در شهر تهران برگزار خواهد شد.
🔹
پانزدهم…</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/445596" target="_blank">📅 12:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445595">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f9544187d.mp4?token=o-2nbfoTUlq3HYmAl5Ltp1TRrwxk6jDq0cQv_hoTPNu_Xsbw9JDkVVb9j5NsM5lRyv4QjR482zbl9-A_rEpf56aaOrBZ7FblzIVq3lwXtrDSbGbAZVB0PcFlcgnFbMGdmx3FEeNfDedpL-bbfAPAf4iYJWudI2LBjLdCSpfXlnIdazSXLlYkt3Y1iEfM5JGtnVfwLSEw4ObqjcAAc-aBfyBNOTKrnLGC94QuxHNR-qxpNGYnQdPwgxFUVDf6IiprsoZ8RzVUMhYa3BDL52t1zLHL8MAuwGMrh6yTIOMF9WLpLqfVvs7jPFsSX48iwtjaN9gqgMTFjGX94eY030wxug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f9544187d.mp4?token=o-2nbfoTUlq3HYmAl5Ltp1TRrwxk6jDq0cQv_hoTPNu_Xsbw9JDkVVb9j5NsM5lRyv4QjR482zbl9-A_rEpf56aaOrBZ7FblzIVq3lwXtrDSbGbAZVB0PcFlcgnFbMGdmx3FEeNfDedpL-bbfAPAf4iYJWudI2LBjLdCSpfXlnIdazSXLlYkt3Y1iEfM5JGtnVfwLSEw4ObqjcAAc-aBfyBNOTKrnLGC94QuxHNR-qxpNGYnQdPwgxFUVDf6IiprsoZ8RzVUMhYa3BDL52t1zLHL8MAuwGMrh6yTIOMF9WLpLqfVvs7jPFsSX48iwtjaN9gqgMTFjGX94eY030wxug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌پورجمشیدیان: تاکنون بیش از ۳۰ کشور تقاضای حضور در مراسم ادای احترام به پیکر رهبر شهید را داشتند
🔹
سران ادیان و مذاهب و دانشمندان بیش از ۹۰ کشور  اعلام آمادگی کردند که در مراسم حضور پیدا کنند.  @Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/445595" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445594">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqgJZH_4XEVhkEjwJTBW0S-3w2ukpliUuEI29FHieFEF2rB7etOVpZWKq_KUyZvfJzC2KmN2nCDUljHKW9A9qs38uv3blJu3OTRGLh_ZY1ck5E9jR8cjyF0rld75vmZ7E7KUa8eTy1n4jdx5-ODK_VzChy0KdpkBYcbV-OZmEzd-2Ydb4SM5EVIOPawqJuj4_tW0zABfisIMjkW40N5_jgkazS2tnlwWyK2uHrBdujcZWx8Pb3y6X2Vrd_sahsofctqU_XbhW5LazlXL0deH3UxAKb9n9IHMzoeDP65oSmmirHhw-a3oNEMCQBaCjalwtXwzfGSFz5l-0P6_i8bO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پورجمشیدیان: آیین تشییع قائد شهید با ملاحظات شورای‌عالی امنیت ملی برگزار می‌شود
🔹
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: مراسم تشییع پیکر مطهر رهبر شهید ایران، به‌منظور فراهم‌سازی بستر لازم جهت برگزاری آیینی بزرگ در تراز ملی و بین‌المللی، با تدبیر بیت…</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/445594" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445593">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzR8mD4y_qnWzm-ZUXEMfd5AkidCTafnjIeNZxN0Mz2VK2pcinhQurCTJem-kAMvJ0jaMP-XxHe36-nphvoLtJVn2DqZ77zreeH2mgig1T_ac6I39r99N4mLwhPfCwm9sheJGozFy37N7bs8n4O35Q4dXGEw2UCYTrnT3XmZ6ejoLsyYUx8xZouRAZDf7HfBXg5yXkPxe7M2zlU5JxK4RSQKtaCFbTTOKdcikPybOA80155XmqlPkvsEB8LHgK-8oJSHvZ4jCD4eGJkQXgwbBTmaniRGtDYwNQTynWEO9NEr19BHnj-lk2U7VdbUVUKoz-URpHOdNWT0Cp4I-ljqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزاد جمشیدی، مجری تلویزیون بر اثر سکتهٔ قلبی درگذشت
🔹
بنا بر اطلاعات منتشرشده، جمشیدیِ ۵۶ ساله بدون سابقهٔ بیماری و در اثر سکته فوت شده است.
عکس: امیر رستمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/445593" target="_blank">📅 11:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445592">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6GA3lw3ZivR-CXmSoYVTLKyF5lG9qRSysycyUQFVVh6BUOMLUFPAh6k3EmbxsljQcYYEFLDb7CpIry8pG_MCIvoxLYWVvk6W6eEXynuOih_KwpQ6no6vIxA2l0-WadILc7TLC_RsjGXhPPkpwEZV9bd6JxWOGRhplUIyLArdF5Zl5Q17d0u-a6uPYD4lxkBwDXSUzduPADk_xDLVkwxdiG4rQjX4ftwK0pOvcEnD7lX_-KbPHVpyg43LJvEljtyw_SSai5JUSsCHwuihZxnZy6mMMqIl85B7gJw_Z5EDkSveGmkCb6v6WdlTZGxRN3VWj5S6h924_lfzxbH_4FEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پورجمشیدیان: آیین تشییع قائد شهید با ملاحظات شورای‌عالی امنیت ملی برگزار می‌شود
🔹
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: مراسم تشییع پیکر مطهر رهبر شهید ایران، به‌منظور فراهم‌سازی بستر لازم جهت برگزاری آیینی بزرگ در تراز ملی و بین‌المللی، با تدبیر بیت معظم ایشان و رهبر جدید انقلاب اسلامی، حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، ظرف روزهای آینده برگزار خواهد شد.
🔹
برنامه‌ریزی این مراسم ابتدا با لحاظ ملاحظات شورای عالی امنیت ملی و سپس منطبق بر دیدگاه‌های دفتر و بیت شریف مقام معظم رهبری تدوین شده است.
🔹
در همین راستا و با مصوبه هیئت دولت، «ستاد ملی برگزاری مراسم وداع و تشییع قائد اعظم امت اسلامی» به مسئولیت و محوریت دکتر عارف، معاون اول رئیس‌جمهور و دبیری وزارت کشور تشکیل گردیده است.
🔹
این ستاد با مشارکت همه‌جانبه نهادهای دولتی، نظامی و تشکل‌های مردمی، مدیریت و اجرای این آیین باشکوه را بر عهده دارد و جزئیات برنامه‌ها به‌زودی به اطلاع عموم خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/445592" target="_blank">📅 11:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445591">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">راهنمای پارک خودروها.pdf</div>
  <div class="tg-doc-extra">1.2 MB</div>
</div>
<a href="https://t.me/farsna/445591" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
خودروهای خود را
در مراسم بدرقهٔ آقای شهید کجا پارک کنیم؟
🔸
۲۴ پارکینگ با ظرفیت بیش از ۲۰۰ هزار خودرو در مجاورت ایستگاه‌های مترو و اتوبوس برای مراسم تشییع رهبر شهید در تهران در نظر گرفته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445591" target="_blank">📅 11:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445590">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0106a9c18d.mp4?token=CtuxrbpOnjmZaoaOOCWcvKGyFPVJps3hV95tiJi11_TwM0sW2IIdkIT8RE3Ft94HuO2husLrSS4uRSx8dQVlIWH9xC0Q2EFAolsnOIpiEG7uW8sTs-dVs-RFXuxZeC7e69g4aniNPdXewxbeYZTowD9TtnXkE8Q5tIZcHseOVtCuyEdpHfAt03koXU-x2CF9p7wlGA-EvrC229haEq8Cm8ghceZBRUyn327AGsqkAPUT9kW7Z34G8r6iZdyAK_Y873FHue8FgJ_4smgWERRjKwOdN203lJvoGKQ3-BqoYJ0Ff-OsWep0ZZqGpw4QGLyEpAtQA3-mOMPtjfU8zP8UBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0106a9c18d.mp4?token=CtuxrbpOnjmZaoaOOCWcvKGyFPVJps3hV95tiJi11_TwM0sW2IIdkIT8RE3Ft94HuO2husLrSS4uRSx8dQVlIWH9xC0Q2EFAolsnOIpiEG7uW8sTs-dVs-RFXuxZeC7e69g4aniNPdXewxbeYZTowD9TtnXkE8Q5tIZcHseOVtCuyEdpHfAt03koXU-x2CF9p7wlGA-EvrC229haEq8Cm8ghceZBRUyn327AGsqkAPUT9kW7Z34G8r6iZdyAK_Y873FHue8FgJ_4smgWERRjKwOdN203lJvoGKQ3-BqoYJ0Ff-OsWep0ZZqGpw4QGLyEpAtQA3-mOMPtjfU8zP8UBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی قوه‌قضائیه: ۱۵ نفر از زندانیان اوین متواری هستند
🔹
بعد از بررسی‌های دقیق و آزمایشات دی.ان.ای مشخص شد که ۳ نفر از کسانی که فکر می‌کردیم از زندان اوین متواری هستند در بین فوت‌شدگان بودند لذا ۷۳ نفر متواری شناخته شدند.
🔹
۵۸ نفر به زندان خودشان را معرفی…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445590" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445589">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda7967e79.mp4?token=Avjn7ptl79YI20puZExOJiU4IWK6eky_rJNlC_9t_16NNMaUPme6OtGycBDyGUVk7PbRrHNwwk8pwwALoOn6thomUH0HPl7n1Le_YOxR1C-khNftSrbGZK82e8TDUIQGpTf8J-K23bHF1wQ1-8ilTyIjC3uy3f1skCsVls9D1-gRwqkKka-OXQZcT-bFZbcumuUVnLA0qLU5swLYdyR7Tiz2xH2QX0BazoPNvqo6QqcivDxBpGS5mfLfD3o4Ol3YJDMxH5gH4N4BBAAhQhjyzDZCzEUQm1eD7-OixoDa5wFxstwTfyJ9NCSdS-VWmP2yE3ZYF-Aw8ZhXS9LDjNX7Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda7967e79.mp4?token=Avjn7ptl79YI20puZExOJiU4IWK6eky_rJNlC_9t_16NNMaUPme6OtGycBDyGUVk7PbRrHNwwk8pwwALoOn6thomUH0HPl7n1Le_YOxR1C-khNftSrbGZK82e8TDUIQGpTf8J-K23bHF1wQ1-8ilTyIjC3uy3f1skCsVls9D1-gRwqkKka-OXQZcT-bFZbcumuUVnLA0qLU5swLYdyR7Tiz2xH2QX0BazoPNvqo6QqcivDxBpGS5mfLfD3o4Ol3YJDMxH5gH4N4BBAAhQhjyzDZCzEUQm1eD7-OixoDa5wFxstwTfyJ9NCSdS-VWmP2yE3ZYF-Aw8ZhXS9LDjNX7Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: سختی کار پزشکی‌قانونی در جنگ باید در تاریخ بماند تا آیندگان بدانند این جبهه چطور در کنار جبهه‌های دیگر ایستادگی کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445589" target="_blank">📅 10:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445588">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e864848c.mp4?token=NP4qmURpvF-BN0XxTvD72xehLOJLGqXMBS517Ag9DTNOEUWAlWkHcVWjMBRKRUtExEBMW2wvpvJ-M1N2p8DKE2R0KdMKn1wiAydsb4bckcA9tzLr4v8HzPaIR55UkrMJmY7PjZi7mxK1BkBIxmL9nAB4alr689csE6mgzhLECJPQermywn_n18mSU_hlWXaiKGXspte6dWwp3dxvRFMTNbjOiNkxTMl_w9GyBvRDcVy9lHRHZpuv_MAOUef-I7pa-I_eWnv0sHFTbXyldPPE4z7SlzrJYk-zKYv6K2sktspMqcxWrRHRQc-k7bjRX1b8xRekqKKx06DFeymJ9th6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e864848c.mp4?token=NP4qmURpvF-BN0XxTvD72xehLOJLGqXMBS517Ag9DTNOEUWAlWkHcVWjMBRKRUtExEBMW2wvpvJ-M1N2p8DKE2R0KdMKn1wiAydsb4bckcA9tzLr4v8HzPaIR55UkrMJmY7PjZi7mxK1BkBIxmL9nAB4alr689csE6mgzhLECJPQermywn_n18mSU_hlWXaiKGXspte6dWwp3dxvRFMTNbjOiNkxTMl_w9GyBvRDcVy9lHRHZpuv_MAOUef-I7pa-I_eWnv0sHFTbXyldPPE4z7SlzrJYk-zKYv6K2sktspMqcxWrRHRQc-k7bjRX1b8xRekqKKx06DFeymJ9th6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: سختی کار پزشکی‌قانونی در جنگ باید در تاریخ بماند تا آیندگان بدانند این جبهه چطور در کنار جبهه‌های دیگر ایستادگی کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/445588" target="_blank">📅 10:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445587">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ارجاع پروندۀ تخلف یک بانک دولتی به دیوان محاسبات
🔹
در بررسی عملکرد شرکت‌های زیرمجموعۀ یکی از بانک‌های دولتی ناتراز، مواردی از عدم رعایت صرفه و صلاح دولت در اجرای تکالیف قانونی مرتبط با مولدسازی دارایی‌های مازاد شناسایی و پرونده جهت رسیدگی به  دادسرای دیوان محاسبات کشور ارجاع شد.
🔹
بررسی‌ها نشان می‌دهد در فرآیند انتخاب کارشناس، قیمت‌گذاری و تصمیمات اتخاذ‌شده برای تهاتر دارایی‌ها، اشکالات موثری وجود داشته و در یک مورد بالغ بر ۱۰۰۰ میلیارد تومان انحراف در قیمت احصا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/445587" target="_blank">📅 10:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445586">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce089e9c7d.mp4?token=cRkCMn5Y027Ts6_Oe2cLdb-SFQ-WTbgTSCb_epGZehF1egVMeJXieTC1lZgZ_DCHELzaWvOCWvNe_qac03c9ImOqUEOVH7H1SqHN8KLBpZJYj8Q-hSyrZyd2rElZx47MvPC0VhKdB4L9RZ7dpSWwdnaUAiE-5IxDvmMDSVoAJD2QOwJ0q4vYjuKfPew1h7TRT6CIJ1yh7McsPt-HG0xkr1U4M0mV0NE19HOpOEgkniS0eZrLD601lygDIgdqM_Vv72vVMmprUN7zmAfruSaOOl3Co2sGmzU2wABDI7COddY5pE3x80GiykHSvdGzcSyIpIoftrCwhCKH90B1cz47rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce089e9c7d.mp4?token=cRkCMn5Y027Ts6_Oe2cLdb-SFQ-WTbgTSCb_epGZehF1egVMeJXieTC1lZgZ_DCHELzaWvOCWvNe_qac03c9ImOqUEOVH7H1SqHN8KLBpZJYj8Q-hSyrZyd2rElZx47MvPC0VhKdB4L9RZ7dpSWwdnaUAiE-5IxDvmMDSVoAJD2QOwJ0q4vYjuKfPew1h7TRT6CIJ1yh7McsPt-HG0xkr1U4M0mV0NE19HOpOEgkniS0eZrLD601lygDIgdqM_Vv72vVMmprUN7zmAfruSaOOl3Co2sGmzU2wABDI7COddY5pE3x80GiykHSvdGzcSyIpIoftrCwhCKH90B1cz47rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی جایگاه وداع با رهبر شهید در مصلی تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/445586" target="_blank">📅 10:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445585">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCZUHxq4WWJMZ_q_96WHn-9qyTkNZonfQLxkUjqDOKPsaRoetrVhQMw0w8UjJccV2vKKsYv4ZB_qWuecd4xg6k-ATNVyOEr7q7We-uExlmOxS89esA81iLLIOtF5p1E3QTyntsVZnrn2vuybzLkTGSIovqdIoi9PWSFxjD_H0qCgx9Uyj0Z2QvQvoAu4xc-9iEdbJiUqCC1BgWwXeGnaQowuTEMpKJDwuwLqOiN8I02cN0znQP6VZpAYFRZh3dbJ864Z4xl9Jsn9r2dcjxK7QlCyaGNIFr6P05OBuOkt5Fk-JBWt1rJTuhrAQ9LIY1XPDogfxfaAoB_p_NjAA2dLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌ شورای‌شهر تهران: شایعهٔ مسدودشدن ورودی‌های تهران برای مراسم وداع با رهبر شهید صحت ندارد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/445585" target="_blank">📅 10:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445584">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZw9AF6XTjt94GcU3yot5gtuAVb_eAnMfFhyXTsNC_J5ch7DUFMS70YXna2q6bddlj6U0boFmsANn06207fkRop1DPqVvPyV1w1uYJlhLza0ToRwn7cMOYXY5TiAPAtXj7olzz_G1XqfgFXm-CwOpJC1iClDe94xZ3FDCgm6X1fHJzwL2YhHBNHQAal41ZhNo1exf52MHYmaDhebfhzNWbm91a8lIqCk_tJCCr1clgQtv2cKO87YOtfKosMUAHEJs4_QLxA-qSBR6mfCu1t7YZzYsW348yyyygGzsL8YsfBj4fyw_sXCsedXl9z2vP5zFIvoA93ylhNbmusf_FQWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: بدون تردید به نقض آتش‌بس پاسخ می‌دهیم
🔹
سردار ابن‌الرضا در گفت‌وگوی تلفنی با وزیر دولت در امور دفاع قطر: با اعتماد به برادرانمان، به دشمن اعتماد نداریم و دستانمان روی ماشه قرار دارد و بدون تردید، در صورت هرگونه نقض مفاد آتش‌بس، اقدام و واکنش متناسب و لازم را خواهیم داشت.
🔹
تنگۀ هرمز نباید مورد سوءاستفاده کشورهای فرامنطقه‌ای قرار گیرد. حضور نیروهای بیگانه نه‌تنها امنیت‌آفرین نیست، بلکه موجب افزایش سوءتفاهم، بی‌اعتمادی و ناامنی می‌شود.
🔹
حمایت‌های آمریکا به جنایت‌های رژیم صهیونیستی در غزه، سوریه، لبنان، قطر و ایران موجب تداوم حیات و گستاخی این رژیم شده و موجودیت و حیات آن در گرو ایجاد بحران و تنش در منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445584" target="_blank">📅 10:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445583">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a10ae23b8.mp4?token=tdctmrX3AZJW3fJjMgVsNRmJfq3v_YvAYhp6nAy3War61cU3zhBiCyaBaRpQJgAdHQ_djSzrtPLjkDwyJ9MX9wXwK5Um0Q4uOsLRbBc1IloyXQW767i3_R6tuvVsQSDXvnDa6cUE7EQriXl91ZirndY1DWpBRUTd1MEKIXMQ2q6BAT51YYazshjQ39z_AIYYnFHXUf2f2DgJZO7D-cxMJLE4ZFb-4QL0v8NWHxA21ycWFhkkFjRmq5qTATabdkKE-sJlmHhaT-OSaH1y2t7z0eVl-iiGEYgc4fsqkiHMak7vmznRC8-IILWcia-p9sWyzURsC3gJZrlWjhqhHk-O-i9hAUev1zYQ4V4NLc4FWDoKMbZTjJ_1K9CIVSQWMhPxZX5EYdHtYg8H-OrtXRVR-67jFGPoqF2Pt30wi1tAtLJ6J3fBcZxZ59f828USRaClA3njDdS0-8tbRJzNbV0tXLfbE5WnTZkRNzxE1hCOCAZvxUgEyXd7EysmgWmaZIftrG9fph4Y-jti3SYjZXKuylp8rKzm9KS1SbKOGja9fHpNkJnCk5m_7_C_OaPf4MMXYwi9b7TQdmWz1IX71UM_Keeg5H66gKXbBGTmMSQ9jH6NhQGOmeaX3LzRTT-7TP5woZlAl79oUV1Dn8GgsscT3mvmM7zxSlElwXzkUb8o7TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a10ae23b8.mp4?token=tdctmrX3AZJW3fJjMgVsNRmJfq3v_YvAYhp6nAy3War61cU3zhBiCyaBaRpQJgAdHQ_djSzrtPLjkDwyJ9MX9wXwK5Um0Q4uOsLRbBc1IloyXQW767i3_R6tuvVsQSDXvnDa6cUE7EQriXl91ZirndY1DWpBRUTd1MEKIXMQ2q6BAT51YYazshjQ39z_AIYYnFHXUf2f2DgJZO7D-cxMJLE4ZFb-4QL0v8NWHxA21ycWFhkkFjRmq5qTATabdkKE-sJlmHhaT-OSaH1y2t7z0eVl-iiGEYgc4fsqkiHMak7vmznRC8-IILWcia-p9sWyzURsC3gJZrlWjhqhHk-O-i9hAUev1zYQ4V4NLc4FWDoKMbZTjJ_1K9CIVSQWMhPxZX5EYdHtYg8H-OrtXRVR-67jFGPoqF2Pt30wi1tAtLJ6J3fBcZxZ59f828USRaClA3njDdS0-8tbRJzNbV0tXLfbE5WnTZkRNzxE1hCOCAZvxUgEyXd7EysmgWmaZIftrG9fph4Y-jti3SYjZXKuylp8rKzm9KS1SbKOGja9fHpNkJnCk5m_7_C_OaPf4MMXYwi9b7TQdmWz1IX71UM_Keeg5H66gKXbBGTmMSQ9jH6NhQGOmeaX3LzRTT-7TP5woZlAl79oUV1Dn8GgsscT3mvmM7zxSlElwXzkUb8o7TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع رهبر شهید نگرانی اینترنشنال شده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/445583" target="_blank">📅 10:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445582">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JamW718f-oLttuZHx4KnSsnou_rMsH6ZQ7eZgPSsjRA4fRhdchkPQdLO_OXR3IqeiRLDASBRrpqt-HNjj2oium6YXqIThm5uqWT1VDjZ6tHD0RHQ2ToT_Hbu3LFvvzxc9tE32c3D4_ekFJQT9P8CG2zgHsCWc0UnuSQWiv__gFJBjI8rtoEBvZMpWb-Ztyw8TlNWmrRkxGtjpBrNu8aIZceH_1GiqCnxiRAA6CBHqjdMxgQvkdOi6WqZhRYxVVxQTdMXXzP1twiQYl_NohBqnJ6HIdv7fBWFlXyi6Tr3xqrOLwzoFA76aAjZ7jVhaP8-uBrp4v-OdIRWVp3S6xNDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌ به جان پالایشگاه هندی-آمریکایی افتاد
🔹
آتش‌سوزی در پالایشگاه شرکت هالدیا در ایالت بنگال غربی هند به دلایل نامعلوم، ده‌ها زخمی به‌جا گذاشت و حال برخی از مجروحان وخیم است.
🔸
شرکت پتروشیمی هالدیا یک واحد اتیلن با ظرفیت ۷۰۰ هزار تن در سال را در ایالت بنگال غربی هند اداره می‌کند که بخش عمدهٔ سهام شرکت متعلق به شرکت خصوصی در آمریکا به نام «گروه چاترجی» (TCG) است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445582" target="_blank">📅 10:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445581">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حملات جنگنده‌های اسرائیلی به جنوب لبنان
🔹
منابع خبری گزارش دادند که با وجود توافق دولت لبنان با رژیم صهیونسیتی برای توقف جنگ، جنگنده‌های این رژیم شهرک «دیر سریان» را بمباران کردند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445581" target="_blank">📅 09:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445580">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNM7TORR2Tee5LaCxaEO5wpxQB7Z4B68pD6h30OrpDaPtSfksvDPzXrW7ddrCOGOFpPkmIepjP0bZvNzajrPzfccB90C22_87Mr1t_FH8NaqNa8iUdY6NZOJD11dMcnLv_OVrfBE7yj2KFyauvY9RAlguMgiJTTivfpzTOaMXT7UPxfn0wYJNuASqvgJGXGfOPO303gyD-_nv6-VSmr4Ldgb_Tpk0jSBGz8LKO2htBN56HxrZECcmOKOJfTaZX6yakDlcexhXSw9lYfoLiCqr2bz1fE-eCh02oUCr_hJW0-5sVbMj8ghYjVfe3GfslvG7rJ5RfRq92coALffwovfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با همتای فرانسوی
🔹
وزیر خارجهٔ ایران و ژان نوئل بارو، وزیر خارجهٔ فرانسه  در تماس تلفنی آخرین تحولات منطقه‌ای و بین‌المللی را دربارهٔ یادداشت تفاهم اسلام‌آباد و روند اجرای آن با هدف پایان‌دادن به جنگ تحمیلی آمریکا و رژیم صهیونیستی علیه ایران بررسی کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445580" target="_blank">📅 09:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445579">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فردا؛ آغاز ثبت نام زائران اربعین در سامانۀ سماح
🔹
ستاد مرکزی اربعین: نام‌نویسی متقاضیان سفر اربعین حسینی از روز سه‌شنبه ۹ تیرماه در سامانۀ سماح آغاز می‌شود.
🔹
زائران باید گذرنامه‌ای با حداقل ۶ ماه اعتبار داشته باشند.
🔹
با اعلام بانک مرکزی، به هر متقاضی ۲۰۰…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445579" target="_blank">📅 09:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445578">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شهادت ۲ پاسدار بومی پاوه در اقدام تروریستی
🔹
سپاه نبی‌اکرم کرمانشاه: تروریست‌ها با تیراندازی به درِ منزل پاسداران بومی، ۲ تن از نیروهای سپاه «شهید برهان کریسانی» و «شهید خالد خالدی‌نیا را به شهادت رساندند. ۲ نفر دیگر نیز زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445578" target="_blank">📅 08:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445577">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c169c30dd.mp4?token=Dp0Jz96xYFZVljEn5CAEZV7e2_fH79ZfIM7VDGte5JeeQH3QTB54YpsbFRtBun9o_68wdJ0WYnFvsAcUQ78D2OyKhzitcgyrT4HwhDEnKbeW6Zgpx27y9M6R4OkFNfnVDc_amATRoEOTcbp3PoFPe6zg-8Y6pj9gZoCbnMwl0J-vVnOoYKQ9C0UnSbv1g-aBtgrYF6RWfx8MVnfb5nCBm5cssXz-vu9AFlIMtWjQ5WdfcZgsN8sQrnEaB-VCvnMGbATK4wrubKoXuEM0oeKQ03gVFokoSoSAuA7BroyK49X4kESIRtnAJpPfa2axuT7QUHQg9FSHTuuttHmps17uXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c169c30dd.mp4?token=Dp0Jz96xYFZVljEn5CAEZV7e2_fH79ZfIM7VDGte5JeeQH3QTB54YpsbFRtBun9o_68wdJ0WYnFvsAcUQ78D2OyKhzitcgyrT4HwhDEnKbeW6Zgpx27y9M6R4OkFNfnVDc_amATRoEOTcbp3PoFPe6zg-8Y6pj9gZoCbnMwl0J-vVnOoYKQ9C0UnSbv1g-aBtgrYF6RWfx8MVnfb5nCBm5cssXz-vu9AFlIMtWjQ5WdfcZgsN8sQrnEaB-VCvnMGbATK4wrubKoXuEM0oeKQ03gVFokoSoSAuA7BroyK49X4kESIRtnAJpPfa2axuT7QUHQg9FSHTuuttHmps17uXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی قاتل سیارۀ سبز می‌شود؟
@Farsnatech
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445577" target="_blank">📅 08:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445576">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9120781946.mp4?token=YZ7p7L_VDKLHHSY-o2SukmlPRY82ztvbPK_9dDu2NcbG7wyIrio2KnighFm16W53ZLxalKY9Df-dFe7MSUrQ_0mmTP6sNV-pzuMXGs4R5kINnz2U-7oBxqp1kwtraIZ-VNo8xC0U9vEsQs5J67-JDGvXBo_Chmt7FdmG7stzb8rcpSiNV0RH0-2zHUAkJUHoEHnYZVLAdYboLpNu4yFRYAh-QAp9NQydH-qCmjguhPtV2m4gauWftyMLEs1mibk5vcw7gcv4SQKxM3MKUBHTFVjJ49othM-hh_vUZirue_KkOWbkLD-f3LkiKl2aX0G_BIcukCcCw9EwTZ6fAfABsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9120781946.mp4?token=YZ7p7L_VDKLHHSY-o2SukmlPRY82ztvbPK_9dDu2NcbG7wyIrio2KnighFm16W53ZLxalKY9Df-dFe7MSUrQ_0mmTP6sNV-pzuMXGs4R5kINnz2U-7oBxqp1kwtraIZ-VNo8xC0U9vEsQs5J67-JDGvXBo_Chmt7FdmG7stzb8rcpSiNV0RH0-2zHUAkJUHoEHnYZVLAdYboLpNu4yFRYAh-QAp9NQydH-qCmjguhPtV2m4gauWftyMLEs1mibk5vcw7gcv4SQKxM3MKUBHTFVjJ49othM-hh_vUZirue_KkOWbkLD-f3LkiKl2aX0G_BIcukCcCw9EwTZ6fAfABsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمار کشته‌های زلزلهٔ ونزوئلا از ۹۰۰ نفر گذشت و ۵۰ هزار نفر همچنان مفقودند
🔹
عملیات جست‌وجو و امداد در ونزوئلا چند روز پس‌از وقوع ۲ زمین‌لرزهٔ ویرانگر همچنان ادامه دارد و کمبود امکانات و تجهیزات سنگین، جان صدها گرفتار زیر آوار و هزاران مفقودشده را تهدید می‌کند.…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445576" target="_blank">📅 08:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445575">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌ استاندار تهران: مردم زمان حضور خود در مصلی را مدیریت کنند
🔹
در مراسم وداع با رهبر شهید زمان ثابتی برای حضور افراد تعیین نشده است، اما با توجه به میزان جمعیت و شرایط فصل گرما، توصیه می‌شود مردم مدت حضور خود را به حداقل برسانند تا فرصت حضور برای دیگر زائران…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445575" target="_blank">📅 07:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445574">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbVZx8XYEgvHj5BNtEdVGuX1KfcxTNLmuVI8EIr2o2z9eTe4MP2W-0kex7pZW2C30rP8B9KnmN9JZXwEIerx0geCoPT_TM2zlxePS4HUPO_-zom-297OBGgJDy4Fbl8VY2RnlGcp0I8PzKeQecfJjBXTIyuDREy61hoB1cZShiflgE0-boRHsGiUFLfkYAWRyBUv2sRdyQ9uLOm2yCe2H2CrIkmFSp0VBALNqMX220NGEP8mT_2Fsj1qA49yRHjtnyn8lWpwXZGy_4b5KFg9MAmxPwgOCmrDYROCwsY0Q633lQHf-GYc08NR-XZummfBb7NfVUH6q5_WykQpTjJOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
سجده شکر مراکشی‌ها بعد از صعود
@Sportfars</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445574" target="_blank">📅 07:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445573">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgPRhq2OMsSTnH9QOIZzsTSZvK_SrBCWNyl7rNSR9LcOcGrg0Wqwy9a2JvHYPdhOWUKC0BuguApwxHPfvpPgeIwEa_02lAZOXAzLaCQ1hC9goU1g2OiaQuCdVGCqAiW42w3oDh92QCzEnzBPiqZilz0zCC9qVR_Mhd8tYH9OYxoAQB5KGd6FVl45HCKEd237BGNJ0-totFzi-Miqno91upCD6c5nSPqnoucCkNcdSgn-hUYehJIRa9u_JBLbdnK_RnxIydSa7r9Jn9TIonFYAJDtV8pB60FYqTRPyL7r48GDzrCska2tPdhwACGvcbJx4dNjgPhGCC_XoecCr7UE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش با برتری مقابل هلند حریف کانادا شد
⚽️
نتیجۀ بازی: هلند ۱ - ۱ مراکش
🔸
نتیجۀ پنالتی: هلند ۲ - ۳ مراکش
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445573" target="_blank">📅 07:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445572">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اسکان و فعالیت‌های تفریحی در حاشیۀ رودخانه‌ها و ارتفاعات مازندران ممنوع شد
🔹
با فعالیت سامانۀ بارشی در دامنه‌ها و ارتفاعات استان مازندران، از امروز تا چهارشنبه ۱۰ تیرماه، رگبار باران، وزش‌باد نسبتاً شدید موقتی، کاهش دما، رعدوبرق و تگرگ در مناطق مستعد پیش‌بینی می‌شود.
🔸
با اعلام مدیریت بحران مازندران، اسکان و هرگونه فعالیت‌های تفریحی در بستر و حاشیۀ رودخانه‌ها و ارتفاعات این استان در این‌‌بازه ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445572" target="_blank">📅 07:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445571">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرگزاری فارس
pinned «
ادعای وال‌استریت‌ژورنال: مذاکرات این هفته ایران و آمریکا لغو شد
🔹
رسانۀ آمریکایی وال‌استریت‌ژورنال به نقل از منابع آگاه خود نوشته دور جدید مذاکرات ایران و آمریکا که قرار بود این هفته در سوئیس برگزار شود، به دلیل درگیری‌های اخیر لغو شده است. @Farsna - Link
»</div>
<div class="tg-footer"><a href="https://t.me/farsna/445571" target="_blank">📅 06:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445570">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7963c2a9.mp4?token=NECkxalbnwu5zH3fFM5xJv9vaPA4JgYrNbN0IIWka6KBPEvhNlClXOvl90qq7DApUyAPEWjQhpAsXL6B3BaD3_1GLgsGb1gHUIXQ5FoAuubSTLuYmY7rPBxfnJi8MjVNtcOMDRg4-0RqDs9mAiTuoBBCtwmGlMlH5MKT3JQ6P5qzhq_H04J-3O2xWr3rKW7JojEITzrJaRNlzKZ7z-m8vGq9bg0uf3x0DQxhfCSM2x7b_lyaKx4M8exMfIMrLckA6lLR94JMnFpRnJzYDo2Cs-M_on2SukGPjrTo40Tnfm2R_pKlLGaDBXBeKB-qpI-rDPOV9iCoBYqMAi9-UC5bxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7963c2a9.mp4?token=NECkxalbnwu5zH3fFM5xJv9vaPA4JgYrNbN0IIWka6KBPEvhNlClXOvl90qq7DApUyAPEWjQhpAsXL6B3BaD3_1GLgsGb1gHUIXQ5FoAuubSTLuYmY7rPBxfnJi8MjVNtcOMDRg4-0RqDs9mAiTuoBBCtwmGlMlH5MKT3JQ6P5qzhq_H04J-3O2xWr3rKW7JojEITzrJaRNlzKZ7z-m8vGq9bg0uf3x0DQxhfCSM2x7b_lyaKx4M8exMfIMrLckA6lLR94JMnFpRnJzYDo2Cs-M_on2SukGPjrTo40Tnfm2R_pKlLGaDBXBeKB-qpI-rDPOV9iCoBYqMAi9-UC5bxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار یک بسته در موناکو
🔹
در پی انفجار یک بسته در مقابل ساختمانی در موناکو، سه نفر مصدوم شدند. به گفتۀ برخی منابع خبری، مصدومان تبعۀ اوکراین هستند.
🔹
بنابه اعلام مقامات محلی، انفجار پس از آن رخ داد که فردی کیسه‌ای را روی زمین گذاشت و سریعاً محل را ترک کرد.…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445570" target="_blank">📅 06:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445569">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">پایان مأموریت اوسمار در پرسپولیس
🗣
طبق پیگیری‌ها اوسمار برای جدایی از جمع سرخ‌پوشان با مدیران پرسپولیس به توافق نهایی دست‌یافته. به‌احتمال بسیار زیاد او امروز، توافقنامه نهایی را امضا کند تا جدایی‌اش به صورت رسمی اعلام شود.
🗣
طبق توافق صورت‌گرفته، باشگاه پرسپولیس متعهد شده بخشی از مبلغ قرارداد این مربی را پرداخت کند و در مقابل، ویرا نیز با امضای این توافقنامه، از دریافت سایر مطالبات خود صرف‌نظر خواهد کرد و ادعای دیگری علیه باشگاه نخواهد داشت.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445569" target="_blank">📅 05:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445568">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlE2WRN5zK3aUwvrA_Qm7Fv49H_cZXTEfdb8gAKKFiKyofiD5fxaQYXeTWZIYXDpsSMNaRva6ixBj2fJGC7DBiEgdo-sc5TfbfdCVE2FRXlpYB0L7HHNrf8htrLv2WjfuBMVul1ynACj9cU02WtUSEpleBZlIH3y0_E1oN_iNIvpeQNA7qcxm11MNPt2gHWbpkUZBVeIbpqJyIy_ONLTL1iYrnBVvMmP8b8cVJrI4T4I0uLgve0w-GmAkr2GEIxgodcT7fx4Yx1iREW5o25KDLkSBCs70PvnCTlUK3gvhtfNuyzRk2QYEAeAM-N-1N600UWvyRo1yHicP_YeogntcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ستاد اربعین: هزینۀ بیمه زائران اربعین امسال ۲۰۰ هزار تومان است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445568" target="_blank">📅 05:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445567">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez3nOuTzlSWTOfePlUhwePb0xSNxZQES_-9uLNucCBKGRiGefUKnFC2So3O4k1G6Zi309cNIK_4H-d6RcO8S5tdJzv3C7s4nzZEowwfsiSZatT32Q-En3sFCPmV-L7JFTYn7qjWBhV-X6EPuds-yG9ntn8dGwpq4IzL9y9kvE_DsHBtBRCe7KBakYo_YOmvOIKwMlJuwyHyVC5ohGSMqbu9Jk2QubRbmXnAkTCNF2-gfjGK37_WzwebAGRfcBVERh76FeZbtTaHsQI4ZpKc0oalDfYkjo14S-k8tt7VNH920zLRIDvz9IABIbxGXHIstofJQ1vPklVH9TgWWUnV0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده‌سازی ۱۳ پارکینگ در حاشیۀ آزادراه تهران-کرج-قزوین
🔹
راهداری استان البرز: به‌منظور مدیریت تردد در ایام برگزاری مراسم تشییع و وداع با رهبر شهید انقلاب، ۱۳ پارکینگ در حاشیۀ آزادراه تهران-کرج-قزوین آماده‌سازی شده تا ضمن ساماندهی توقف خودروها، از بروز گره‌های ترافیکی در این محور جلوگیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445567" target="_blank">📅 04:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445566">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815edfc035.mp4?token=DQO1XA3IoRKkzVzI4QCHgX5c3nRZ2YExFJRK_eovBRldctpyJhLSJSWlIT0nyhAoyddqOo0rXKTJBdiNsfq_9glJYfXC3nrj-i7EYH-ovU7NVPtjJuDFoNRZpMbiVSkfxoI1mJuiBT-mtGnAT5vS9QTxRiKVd2MLrqD3XBZ3BcvZyBIM97T2kAMkvE6qADo07wWjVhdd3HrMaOMgftgWlvrNnJVt-ZJiHqAVR0AdfB05XpD-P5pwOc20X2LDYrHVldauZ4XgJNlKfI5rSNoWwjrXhg6IVZYa8nxLGV_GLuhpc6fHahcqjI62vNYYUO9Z4MUT6_gGLperypJRyvZcFIaGGCZ3k1pk3EJ4GbcJi43ToyJzrPRcRfZACLSu2QB2DnqHHtcU4BBxmU8C0VvsxEjf8Sw1nKee0E1DpdqAB-RJaxk1zAY1boeAXKbiiZ-gqt0UdyHP7kaWXtSKa2XD5Ws3cI4Po4WtYj6Xpx7rxOqbdfeOanhTo8Cr-4NKaNNVxuUArLNnY0I9DYphFg-julynodRg739vOThwY887eT5fGnebXxz0ZCqz0N1kFp3v36M_SQmJww9k7DBtBjvrJtUr0Wjf-rLBn1fhxatdWFo9HEGNlm3qgIh_BtZtEiqAZ27UftexYE56XuuB8h5rXblmlRPfQxj9Wuc0TSsbzmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815edfc035.mp4?token=DQO1XA3IoRKkzVzI4QCHgX5c3nRZ2YExFJRK_eovBRldctpyJhLSJSWlIT0nyhAoyddqOo0rXKTJBdiNsfq_9glJYfXC3nrj-i7EYH-ovU7NVPtjJuDFoNRZpMbiVSkfxoI1mJuiBT-mtGnAT5vS9QTxRiKVd2MLrqD3XBZ3BcvZyBIM97T2kAMkvE6qADo07wWjVhdd3HrMaOMgftgWlvrNnJVt-ZJiHqAVR0AdfB05XpD-P5pwOc20X2LDYrHVldauZ4XgJNlKfI5rSNoWwjrXhg6IVZYa8nxLGV_GLuhpc6fHahcqjI62vNYYUO9Z4MUT6_gGLperypJRyvZcFIaGGCZ3k1pk3EJ4GbcJi43ToyJzrPRcRfZACLSu2QB2DnqHHtcU4BBxmU8C0VvsxEjf8Sw1nKee0E1DpdqAB-RJaxk1zAY1boeAXKbiiZ-gqt0UdyHP7kaWXtSKa2XD5Ws3cI4Po4WtYj6Xpx7rxOqbdfeOanhTo8Cr-4NKaNNVxuUArLNnY0I9DYphFg-julynodRg739vOThwY887eT5fGnebXxz0ZCqz0N1kFp3v36M_SQmJww9k7DBtBjvrJtUr0Wjf-rLBn1fhxatdWFo9HEGNlm3qgIh_BtZtEiqAZ27UftexYE56XuuB8h5rXblmlRPfQxj9Wuc0TSsbzmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام کاشانی: اسلام دنبال چشم‌و‌گوش بسته قبول‌کردن افراد نیست
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445566" target="_blank">📅 04:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445565">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGHUE1okRU37Ta5Z3G6h1weTQiTRqvGPZlvcwkXPO6fvd25YSbOutqAENGeh22UEI0E0as1doOn4Ca2F3S0kyXiVKixBvCSL-5zp6iCvfjXBFAqmAnhw2JLbkXdILeHYxGnQ8kahCaX_SkLtLpP5opZZCViADzRITBcDNAmJtrNmcjmrYXBVipSEhj0y-E7ESIicnGfnua5LaQvhhWuKSpmwii4QRpuTCVR9KpXRAyNgvX4KVoOjjWMyY-yafFzB54wsnJ1hm31-oK87I3PWuJy_ecOKF5JlhTymmVNkl-w-j3oR_wMtcMT2BMKHkqTYbWnwFPSxkMaJWaC1I4Z9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات زمینی و هوایی ارتش پاکستان در امتداد مرز افغانستان
🔹
پاکستان از عملیات زمینی و هوایی ارتش این کشور در مناطق مرزی با افغانستان و کشته‌شدن حداقل ۲۹ شبه‌نظامی خبر داد. @Farsna - link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445565" target="_blank">📅 03:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seHapIieHXctRH2y5Pb7EIkB2pq-RQSMaA5dG3oifNNPbhZTSo2wHu-UTmljrFkL2qETomq5LNRt5D4hEvZ0a6CvWf1om8h1YrCfuvYv6HpJ5-DJdi-qz-dRm0zBZbFHMFLOt7yaOdMK5Wl_J526cESPdrzx_HVi35w4kH1p_14k4fIWc2BuWczI6wuYatWBZeKnU4tyuPHR4VIzhgUCmnaFvDdfIF20wLmsNZeLIoJQMo8NaeGGxHRa30GiJh0XwpYylsZsXsj8oJ2iiYf9yS8ZthqncNb9zLsS7QfjlGUAjZtiPiaVPDb1Mo782pXZtlWPdYbJnMJ1AaqioydGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: ناتو، تسلیحات دوربرد را در اوکراین آزمایش می‌کند
🔹
وزارت خارجۀ روسیه اعلام کرد که ناتو اوکراین را به میدان آزمایش خود تبدیل کرده و از آن برای آزمایش تسلیحات پیشرفته جهت حمله به عمق خاک روسیه استفاده می‌کند.
🔹
به گفتۀ سخنگوی وزارت خارجۀ روسیه، ناتو در حال کار بر روی سامانه‌های تسلیحاتی پیشرفته‌ای برای اوکراین است، که جهت از کار انداختن فرودگاه‌ها و پایگاه‌های هوایی روسیه، ازجمله آنهایی که در عمق خاک روسیه قرار دارند، طراحی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445564" target="_blank">📅 03:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445563">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDRQ6Oa1Uv1Koak0uZ8XBt20GcfI5mkGA_iKEaNh7hCiKmO8JwV8PvGmVbFNearF2dXm0HdrQCxyUcABm4MXemOgWmS6nPKCDW1146INADfRa8T3BzatBeHqmTjJGhnp6h4v9YfTVGYcCJ4YrBZFiLGmgyrMpty4lovfIBYHfW0nCAxEcYbttYgxJS8psqvlCv1Oi9TKixj9q7W0384S8UFEk0ch8DK5DMoRhei3XwdznO0t3SxVEbhGecdYpsEMFdr3JqF4Dhz9IzJt04i4RJxyDAhNwmy70640pSMc56DA22CHRYKZD7aii24uiwDWM1lQdEnqLEtclZTjXrXK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شگفتی رقم خورد
حذف ژرمن‌ها به دست پاراگوئه
نتیجه نود دقیقه:
آلمان ۱ - ۱ پاراگوئه
ضربات پنالتی:
آلمان ۳ - ۴ پاراگوئه
@Sportfars</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445563" target="_blank">📅 03:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445562">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSV_aLPuJIxIatRC5EF3FMeoPQEn-OSsVMnBS8H_Koft-bnEI-rWMSNGvLuv5JBwS8LYNCGWKLPO7-t6KtNCQoRieIOTuLAQgWpZczhXZs9iSYRj69011ldB04MGHQDh-Ts0-rw691dJYkaNrjCzng6sgtLc9sigT2F-jLiMn_rGuFEz81R6GCMEgyrzsy8uT1bBww_NguAEDLQuktk-1lwR_nsB7vDvclkGPNLLOWAkURk-OLmmUQk1xIqRjbpqjNRn3INZe4u04lXdWI3SjXG9mr9MBttxpY_-sLU_Tnr_38Oom20IYlWOJe_o67xwYujwCQFx3ZCa6SIlw7GePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقش محوری پایگاه موفق‌السلطی اردن در جنگ علیه ایران
🔹
منابع مطلع به یک شبکۀ روسی گفتند که پایگاه نیروهای آمریکایی در منطقۀ «الازرق» در اردن، به‌عنوان یک پایگاه اصلی برای حملات علیه ایران عمل می‌کرده است.
🔹
به گفتۀ این منابع، در مراحل پایانی جنگ ۴۰ روزه، این پایگاه بود که به نوعی نقش پایگاه منطقه‌ای را برای عملیات آمریکا علیه ایران ایفا کرد.
🔹
در این گزارش آمده که واشنگتن هیچ چارۀ دیگری نداشت، زیرا نزدیکترین متحدان آن در خلیج‌فارس یعنی عربستان سعودی و امارات به آمریکایی‌ها اجازۀ استفاده از حریم هوایی خود را ندادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445562" target="_blank">📅 02:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445561">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLLaHBf6u2Rt8iYKRxym721fN5db4kBa-gShZAPw7pbGNXdI3L2ZU2y9BLA7zHZH5qnnBglmqDhFRrEpOxQ3dwsZKWuaiCJrhvc4IqmpkcNSJjhLhDeE9j20ZGoST0JrlOUYuPAHzmI6JP2XV03bwpFpXPekZlEACePCbAnaliUsloipp0-8NajTE_RP615DACoHW4V8vRmMH7wGp9pxnOQ4Io9H2kSPT-qR-mGCxk1-RwlPmVZERX9hdcpy6huXWPae_dNwt8bIxCjp2AbICxO4dScmfaGi3Sw6tt346TohrCu7d8PlthgkXQi8JENL5SYljV50EcGDBiiW6Cgxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر عمانی هرمز با اخطار سپاه از کشتی خالی شد
🔹
بعد از گذشت یک هفته از رونمایی کریدور جدید عمانی برای عبور از هرمز، داده‌های دریانوردی نشان می‌دهد که به دنبال اخطار سپاه، این مسیر اکنون با توقف تقریباً کامل تردد مواجه شده است.
🔹
بر اساس اطلاعات رصد شده از پلتفرم دریانوردی مارین ترافیک، روز دوشنبه تنها سه فروند کشتی از مسیر عمانی در حاشیۀ شبه‌جزیره مسندم عبور کرده‌اند.
🔸
این درحالی است که از زمان اعلام مسیر عمانی در تاریخ ۲۴ ژوئن تا پیش از این تغییر اخیر، حداقل ۱۲۰ فروند کشتی از این مسیر تردد کرده بودند. اما به نظر می‌رسد حالا اوضاع به‌طور کامل دگرگون شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445561" target="_blank">📅 02:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olqLIrP56sSdqpajDih1sL_igOxAtAh9iMmo7pxL8ZqFt2QO4C2wIsCZS3Npe5nIGFr1yaefCMj8ILjwsyhSA91dWh5vwc67MjR5kvp5bdEop4Tl39TRn6DKNKqiZKjzk1u8qLziCEkcyqFSwyxITQGZ6YaDIVBrOilP1x-cnJJJbkwXRzdx91ZqnVNzD_3hnRH5A8wxtF338FEdnpO2-hSjXtsE0jt3p09SoAaH3VZOA0QXe9gAsrrv2ivGz2jzoG4GMh2N3hwsSlB6gNIU79IiaK_ijYtj8jVorlUaebbqW20yzSjSf2J47LDePiAUuPx6b2sVc78TtwFOk0l24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این سلاح‌ساده، سربازان هم می‌توانند پهپاد شکار کنند
🔹
پهپاد رهگیر روسی یولکا نشان داد که می‌توان تهدید پهپادهای انتحاری را با سلاحی بسیار ارزان‌تر خنثی کرد.
🔹
یولکا با سرعت ۲۰۰ کیلومتر بر ساعت، تا برد ۳ کیلومتری پرواز می‌کند. این پهپاد با سیستم قفل خودکار، از فاصلۀ ۱۰۰۰ متری روی هدف قفل کرده و آن را با ضربۀ مستقیم یا انفجار ترکش ۳۶۰ گرمی نابود می‌کند.
🔹
برخلاف موشک‌های دوش‌پرتاب که به سنسورهای پیچیده و سوخت جامد نیاز دارند، یولکا با قطعات تجاری در دسترس ساخته می‌شود. این یعنی تولید انبوه سریع و ارزان برای مقابله با حملات فوجی، بدون نگرانی از اتمام مهمات که مزیت نسبی بزرگی به این سلاح می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445560" target="_blank">📅 01:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nxbsri2LWJhq9E-9EdgBHTP62Qrt64utEFCgr7W-yY5Q_EWSHBA1J5O1MbVDCumNCKjX4TiddQQDr7gQ4fGTo652CWcMQqY-WCOOvNO46GQ25myVqj9SD54JjMJPo9tLUlLP_XOGo_frTop-4z16Ih62BKvZPtKjcbU6hBo-HWUs2Z8s9AOwJZqIwHgw4xYQtKLLpS9E0vR4YNcZ6nw8d_JMiEZSwvUtEXArlZymVPDsigiywMsgv6Cz-AyEswiZu8hQZOPVk__bniLpGJpmyCxaaxgA9nYIHCBEdTR3_4v1YUpNLMkiPO2BXt3dgnb6qDjvgzUFOPB0ht_8ClJc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPAiAQj0Y47Bkgijv79fbHzxsR84othD6Lx4VLvLg8vAPPz6AUc-94Ph8d4tgTt5D_SMQTZUpXosUYq6Z0r0Bq2QzyewiLI9FJMR9nZtY1_rH_H2OmOo6ktWnzU3eGWuoseIf4EGbI4kMLRZCMNI81qTCUOT-uuuTNaxS9gKUzsXs8f6S8sUMLTzcCmzUc-fl70FnnMaN_sdOgEvKcL-JmaotMecMUyiypmVQpGQVCFvWVPtN5LwCGuLnHp6TSuD3GPu5umaKYvIjguQ1dXpfgyLCOFav7ZD4ai-4bCWKMEwjAIeO_2hAIHOLvCJVQJbv6z2Ck46Zgh_264PyhfEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImYCPq-0D1Fl_Z_xGsWWjGaPm8KDUZEbGYa6q_wWPrxf4rSOGc8ZmF-JVK7gh8Y51hNFJJCI_yt4uZYCN5lJr0QYkcwQvrMtM5QnxYmvc0TtsKCxhuBrMPp_LbmzIc2fKBtXsmRpCxS0RvHyBg6ExFi899KWOAdRr5TjtWQ16St754ooFjXi0AUilyQXzFW2KSODbYd-r-7nogZWIcsE_YeRnGfLlZcxQAPP88Ma89aCCNixDeTWR-5uXdT73BZN5TTcaIeE87ogcjHTNDBnatdNXizV_IqlIy9pO0JRuDY5E2Kv4DkTP043y_URdyMUtqJ1YqOIawWh0q4H14qyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feLAmCUIE3Oi-dNIM-hK9RaaziOEETRksix1_A6Q8-9JzEb1aBMEwDDSIg8ipXuV8Idqq9pODMOeSbW6SoAFUmZ2uIqV4WeJaA36h4fo1YdY-LuBaGlsdlDztmg4y5Ya-1Pz-sWPj_T3GmOfoKitNN8bYxBSpQTSpBQ9llUsTp9mxBsxVnzJGmjUsf-2FlPdkV9XykHtFKPpwb4jha7GUoULvioZUBCSKNu1K76D7D6_4xE7TL9Y8JXPWgHw0v7Ex5yg9HdgoOaX39NhYbl_YfZb31AqzP1l3dR6DXbSxMrHwetWVLJIWziEerTH8WeqtxRtpeopw1Hul3lH9YckCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGCISpwTdCIDzH3WL3L_GtSLrI0S9vwFad7VD5kLD-p9mW1TOboRlNj13NnAA4BAqVKR8Ga2MG7bue0-Vf94YHGI-n8eq2_hY5pNfAdUBVKdirAEsjjsLdjMbeLan4JMCG98bicoNtlHH5oOwPIKN4ucU-SdJdZJ8OlkW1zVHHiTUn314cdD7MiX0YJQifw73MUOYnyMGykUXtBe1npuCHP_MD91hgO2KfK6Iy6pVfj3deIbUvcu1izgV0-htuvlX2CMc0bs0kLQkTyCHVf-fbvmC3XkwCAS1pEll-4mUa4kQQIvJCxgHxKAXib7fA7LuKcTcdY-tECVdOLUkGABpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۹ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445555" target="_blank">📅 01:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445545">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IS7MQJZDSjSRMLmeLEn4kr03LzQCip037gBoZ5nl6AbXmp-IiK95YDu5_eLXS72w-3d6ACHxNGgvBKYYqA6nT40FNBVw6yugYW2oSQ4ao3gsnaVESIXyzkeWYCMGsHH26RghHL9Ku1RDNYcgJfk8byIIEOnVypnHn26QYNsT3V7e5c7N1tOQYoM88Ht4JWQz6fwgM3osjssMuRrYtZM6T-WPgiwGI9zAo_sRl8MTUrRYPbvqYK4viYGyVj-DNhbCe9IMsjQaNKdUU7GewdMI9QcbvRB_4IYLQSAzeA1gw02eu98_W7xl3eYDq29c7htKwLbVC57_s2zgnE8gq-Okdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HksCLHyjxsi5SE9o4bGEzWtAb-Y9eWuIBKlgmqTA_xfh906s1CHuke_pbVl44xiMY_ofJARMDXyF28o-41ntfpsm6yBagtFytGD-Yb5FQzx1tjY1ary6FLkfJ3__yRLO_CR1zFaqhcwdyhlhVthbBERBfsEkFUPxrNfzo9cis0W7G89up6alUfLBZEKC2xVsQS-dNmUzoR99srMU_YAgyah0oFQEIaWuyREH_izE_dxgxOAMMfYbkvcU6aC-vJhsb2SX3oyf1MGAwbi5JOS7o3lSJVupZkJfVL6_LQ-T7zxqD4m64B62O7jHEX4T4JO-H3AKtpsGk9qM2R2m0OUshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYJl7Fh2iJsDNbOGj_y8urquy8yCqQXmp7u2HCzZPNIVhU0L-cYKSq25tyxGr6DrvCOhzl7y6nMZA0IyczqBAgt15afBeHZCNIWcsI8v5Fg70LDJ-j-GWhQUH45Lb_F-L0CDRE6MoXvuS_7a3yDAwZO7AqPrGjIM1QrxNYb-9aNvxfZvSUIKpotPBoLcRXZfHbAzE201qjMTHvdk8trsw9Z-yzCLa5qpIHtLBktgK9abmYjBkRc6PbnKgeUgOw3Ijxu-J2NOjSmEFhJLN2uAEBP4sM6LnPKfpDvR7G-GFxw9CB95SHHorSaMG3h62DN5zMfaTTB0ZoydoQjscDxidQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJiZRtLVj2ZufKAJSZdDFnArqh8WF9qVqiKO-fKvUOOrRtzHB9MSuYSl1IAuLmFAHBw_yZK5GfHrby3xhMujXO9_3b8vg_zmHlp5ueddss_KvOml8e0NTjJW5gsCu8g-C-J5wjb3Q6Orn28v-xun8ScUu6GJBtKyFjz2g970FNNa_j3pTMVu7_gyYu-mf2P4KQjnoGn2x4YxohK1pDQe-BdQ3Rj9D9v46bfDLFOY0ZObWsoSJVKZqKQN6KGMhf3ot109NsH0xW8y8yKJL-0v0uYhPWhpgwNErD0zDsOr9Au3joY_0In7ZnC3Zajix13Rj0xbCcBndsXdg_1NYH-h2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbipsB3ja54ZUL4XJd9NKVjfanmSEfJwmT99lt2L1M7Spf2YnBpBVqYiKbcO_zCg7XBZUvIsRUuYxq2QAVsXIyhbJuI1RJ6p7GwTDQWKEKZ9AFpf6IDQh4XH_9RYECkipgSbBonstqLEit0DBYl5ajD6vwU0tILIfbmJdOGtF6M_SU3e0SpUFNAbc5_UXHocgz8bbxV0Rew_ut7rXGX4Q1q5b4MkguWUZDERToGAoMnElOP8StbJVYTk4sQ08EVOs1OwqnOFCc5F_X-hnnc8SSyZf9DSa_DmXtyVey_5uSKwTr4U-PJg68WE2fyE6MM-gML__yr489NXOMb7GoYRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GP0FMUXGyB3tubQ7vihFTDF97pfVMBRu8K4ZcS8Hsf_4ETak6on6_eWKmH0xPCmyJbsBoUeOwFk3kCrdm8L2qzh_lJljDOwQksjX7hZSV-qt2eJ81hhwX5QN4tRjtsezTaOIH0OhXmxVwd8_xXld1nxZJu2J0PgVng0h-r8amKc-3QwqYGQvaTc7FTqDd8BG27KSBIYfiX1TooBkes55w3NYS2ONMYazWs3zDl1Vh0giwoCnG4hFSX2UT2mFCTBtIQvMp_XiJTCit7lcOGtR4tlQVwb9OqgAJwDs9PqjI8xFbaobbDPqYjw6FzAIzdLc0w5GBK2s7lusRLqYlvhdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhCZFHoGg5129TIz_UQkCdbMZV3w1J7DsjjQo0exmFeA3rBu8IkThd-D5NNC6mNs6kO8OOvgRypwARgysqS3cjGMMmyXObm_Eoy0oltaX1YlcQXIN0VGjWpaQBb_ruXiGZb0eV9MlzVg8aAt2vDGFrDo7a-Y_vGmh0Tuy5rUO5vxvbx5kOHQcqi9kRnQiK1uXGtHvEzjSkA-d1qWLYeX28eNot_Y5AyYv75f4hw0JXTVSOrQc7h6hFCdzhG_ZP4D3XBZgI_ecs5NLepHPomGT1eX6GgVsJpd2R7IS365PFzurGOsZBQXos2rJLbX70FW5mqkZH1gQgGGQYFyr4qEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZAnoi1JM6fdQC_ndoxNiLtZQrDVc7psugg3VdqaBYFMDvlY46YwuXnhncXZphbKcVZiRPmyKDHDWlRSNWQ8WB1QTI-dk6KLTWDB0lF1bcOk9LUANtI7PFsyCFVP-zA78q52qIYrXYHlcjv0GRyL1_gzPk533enTCnBFx0DEyRkMqzhK8UMrIcxmt6rwUVjDFOtNLOqQ42k15kyJgUgaaqMKiPdvKwmwBSqNX7zqr-cn5drKT5zcVzvDTBMEASjyw8Jy498vov3s0-hmDLkIZ9mzstjvfcyPUJPkQG72GfAPpUIPezCR8OFJD5x-agp7rEZvPs2SlVHnaP4pevO82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTpKHpo07uIn9TsoOYaXQxoZ3CpcN7i8q4OslBwwP_uxSuStaC6fstR7U-3QL95IZ_V3oJLjped3--5mPQ3O7Jl8x1lu6B-vJa_e9_ZCIIVSt8U2KHqtuisy6HrLF5CKHuGtzSHdXZTdovcdCPaqowlrG2Y0D59MGAOWLRxh-FyxBgmP9Z-pCOmC6ZspJ9NoIi4l6eI_r-PoHLgLtPqvVRzBrazMnbFz0HIZowpvytOQZQEu7mP_SFG2ohe8ZiQbg-TW2P09LWqwYoDh2s17xNvoSBadLC7RjtYR05nku-bb02NWhDLqyWzCE0k4ocUr-nNw8PHvL9BaJH9jlMJ4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbuzpAWkEt1tbSFiG8fPr27mjZwE_ybOUCHgosLz3RNUjnN_krIm-my3AArlx_p78k0IvXfdmWkQSGbmcsJSXjTrUT35BQuziBT2ilq1cvxsB6ygUpfRqCJUMOUaAJ6XJcYzVCKywXZAfbitOioRcnAnMEg6bsCzLS1szXdzqnHazFayVvhF1qPW4GK5xQdkE86zQa8mOfLoiQGfD7HtAxAZ6MHTI7MnxXuvDd-V0HmAxZdLXiWVYzpvwe5OoowvITYUz3SMPm34pu_BLv_v8SaeAihZlEuFk-wf-FUnb2c9_2PVbAf1EGeXAFUSQdoMAvK4uPsEugRp1_Qic2N8yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445545" target="_blank">📅 01:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445544">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1956d75e.mp4?token=D2LB-pwgFwLPe29cyMTdtwmrSRQy9nhrxWymHcKEUVbWd8DBjM4UOYX2BMwYunxWVNiuHR2xuquxbspKi6KsDbLLpN6-T3NVad4abxd6pEVLELU4sN8D1whUjm36hIJNDgg0tZHXAas_YkK14upwKVfSs9St-utqParggxmFvoSaCDuQjmE9VbSJv4iOigx949UPKQkjb-Cf4U4WFAnxQknNNJEh5Fsjmxw54hzEWAU9tMKyCCGnUcoVWj1FgjTumJfpjKi1m9SoSVF_rFMHJOdEDI_g5Mxt-2Qu2C1duZWaRP1VaVgsMsCa9ubT4ggRG6W1zejXqazIO2nQpKdGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1956d75e.mp4?token=D2LB-pwgFwLPe29cyMTdtwmrSRQy9nhrxWymHcKEUVbWd8DBjM4UOYX2BMwYunxWVNiuHR2xuquxbspKi6KsDbLLpN6-T3NVad4abxd6pEVLELU4sN8D1whUjm36hIJNDgg0tZHXAas_YkK14upwKVfSs9St-utqParggxmFvoSaCDuQjmE9VbSJv4iOigx949UPKQkjb-Cf4U4WFAnxQknNNJEh5Fsjmxw54hzEWAU9tMKyCCGnUcoVWj1FgjTumJfpjKi1m9SoSVF_rFMHJOdEDI_g5Mxt-2Qu2C1duZWaRP1VaVgsMsCa9ubT4ggRG6W1zejXqazIO2nQpKdGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات رژیم صهیونیستی به چادرهای آوارگان در منطقۀ المواصی در جنوب نوار غزه، دو شهید و ۲۰ زخمی برجای گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445544" target="_blank">📅 01:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445543">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfde88a6d1.mp4?token=K4T9tP0jl9xIM_B5otcfaqragJAfkyZ7YrIpVioyi6ojAhHuyHObfm-A2q9m_5byU1t0JJazFfFOGWSO2C_RaGVLO8zSiln1H56RHAWpBXaQ9zfYVAxTlu3Ca1sdjDCnY0OvHB5ZdJ6E6S667gJszSVXoydjMQ-g6N3ZWwitpgTgBWF0CyIgRzLrj6meNakXiPWCh-LwmhmcHc-mkfL5jPrmJYv77QEQ3T742jZOzgYOfSRJtMuKUWJd88WNGT7hGktWaOqSoCnAZoYfRag3AzJgq_GURixWr2EvP8_5K2XSx1M2tghYlA7fyUjxS9GxJQoxmDAp6in0ZEMCH2xktA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfde88a6d1.mp4?token=K4T9tP0jl9xIM_B5otcfaqragJAfkyZ7YrIpVioyi6ojAhHuyHObfm-A2q9m_5byU1t0JJazFfFOGWSO2C_RaGVLO8zSiln1H56RHAWpBXaQ9zfYVAxTlu3Ca1sdjDCnY0OvHB5ZdJ6E6S667gJszSVXoydjMQ-g6N3ZWwitpgTgBWF0CyIgRzLrj6meNakXiPWCh-LwmhmcHc-mkfL5jPrmJYv77QEQ3T742jZOzgYOfSRJtMuKUWJd88WNGT7hGktWaOqSoCnAZoYfRag3AzJgq_GURixWr2EvP8_5K2XSx1M2tghYlA7fyUjxS9GxJQoxmDAp6in0ZEMCH2xktA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرح جایگاه وداع با رهبر شهید انقلاب منتشر شد
🔹
سردار حسن‌زاده: طراحی جایگاه وداع با پیکرهای مطهر امام شهید و خانواده شهید ایشان بر مبنای چند محور صورت گرفته است.
🔹
از لحاظ ارتفاع، جهت و استقرار در حیاط اصلی مصلای تهران، از همه‌ نقاط صحن، رواق‌ها، پشت‌بام شبستان…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445543" target="_blank">📅 01:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445542">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۵</div>
</div>
<a href="https://t.me/farsna/445542" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۴ – کتاب آه</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445542" target="_blank">📅 01:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445540">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجار یک بسته در موناکو
🔹
در پی انفجار یک بسته در مقابل ساختمانی در موناکو، سه نفر مصدوم شدند. به گفتۀ برخی منابع خبری، مصدومان تبعۀ اوکراین هستند.
🔹
بنابه اعلام مقامات محلی، انفجار پس از آن رخ داد که فردی کیسه‌ای را روی زمین گذاشت و سریعاً محل را ترک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445540" target="_blank">📅 01:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445539">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH5JxljXYLhRPlyuGCaqQQey6CALgZnP1onxS96sfU9JGNDsVXJroMcBcMvdXVOaChSY4hoBIXPuZb_N_OB0HnpQBxnmPl-gIYx_sfb6IAzzlbV9gjWwOG1bsNwhfgpgMrnyInD7ozKADkc_FNVMOQuVikkPBqiKLFOtQbYmOUzKj9eIf8UBmcC0R5bnhqj3eV8duXcrdJZzJuYK7aJ9ckeepHyr47ZVBNsnoAN61etyC0aoQCc6jWIuvpfrSBihGVhDTUNrVEYZ4ofYNZJorkBLYDrq3OhhHBEv7i9lRJCmNCBIlYVwyJUjgX2psvKB78t5Llduztqn-g0FATBQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریشه‌کنی درخت آزار و خودخواهی
🔹
در مدینه مردی از انصار به نام «انصاری» خانه‌ای داشت که در گوشه حیاط آن، یک درخت خرمای متعلق به مردی دیگر به نام «سمرة بن جندب» قرار داشت.
🔹
سمرة طبق قانون حق داشت برای سرکشی و برداشت محصول درختش وارد خانه انصاری شود. اما مشکل اینجا بود که او هر زمان که می‌خواست، بدون در زدن، بی‌خبر و ناگهانی وارد حیاط خانه انصاری می‌شد؛ جایی که همسر و فرزندان مرد انصاری در آنجا آسایش نداشتند.
🔹
انصاری بارها به او التماس کرد: «سمره، وقتی می‌خواهی وارد شوی، حداقل یا الله بگو، در بزن کن تا اهل خانه باخبر شوند.» اما سمره با لجاجت می‌گفت: «این درخت مال من است و حق دارم هر وقت بخواهم سر بزنم و اجازه نمی‌گیرم!»
🔹
مرد انصاری به پیامبر اسلام(ص) شکایت کرد. پیامبر(ص) سمره را احضار کردند و به او فرمودند: «همسایه‌ات از تو شاکی است. از این به بعد وقتی می‌خواهی وارد شوی، اجازه بگیر و اهل خانه را باخبر کن.»
🔹
سمره قبول نکرد و لجاجت به خرج داد. پیامبر(ص) فرمودند: « این درخت را به من بفروش.» سمره بازهم قبول نکرد. پیامبر قیمت را بالا بردند و حتی وعده دادند: «این درخت را واگذار کن و در عوض، من ضامن می‌شوم که خدا در بهشت به تو درختی بدهد.» سمره بازهم با لجاجت گفت: «نه درخت دیگر می‌خواهم و نه درخت بهشت را؛ فقط همین درخت خودم را می‌خواهم!»
🔹
در این هنگام رسول خدا(ص) که دیدند او از حق مالکیت خود به عنوان ابزاری برای ظلم و آزار یک خانواده استفاده می‌کند، رو به مرد انصاری کردند و فرمودند: «برو آن درخت خرما را از ریشه بکن و جلوی پایش بینداز»
🔹
بعد از اینکه درخت را جلوی پای سمره انداختند پیامبر به او فرمودند: «حالا برو درخت را هرجا که دلت می‌خواهد بکار.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/445539" target="_blank">📅 00:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445538">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0841fac41.mp4?token=DRChtGcEuTHYJ61rCRIB8TRnKjxprU0U-lnpfIZHv_Cz0CEFQNrkes7CDTBnRL8x9e2yFIT6cvfBy5aoqp83S0ugzwIMpD1srBJ3wjk2a-bNhEkGx584hz1YoYcAyaBzXkhApSxdkMbmWE5hAv7D-hr0GuOHh1wW-Oao3vCh0ac57igWaa56v8_E08E8hBvKlNOcKFqu2svKQbiXSuv1bJPkWQ7D2tf-UqV44adzHUeF_1gQFlvc_PglpLeU2vjL4FbP5_LlvvOG77eiUQVyZ6KO28rI_7JchwtaieowrXuNvuC-pOHveIVfnBryquKrMHRMs6zX7zJCwFG0QYXHIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0841fac41.mp4?token=DRChtGcEuTHYJ61rCRIB8TRnKjxprU0U-lnpfIZHv_Cz0CEFQNrkes7CDTBnRL8x9e2yFIT6cvfBy5aoqp83S0ugzwIMpD1srBJ3wjk2a-bNhEkGx584hz1YoYcAyaBzXkhApSxdkMbmWE5hAv7D-hr0GuOHh1wW-Oao3vCh0ac57igWaa56v8_E08E8hBvKlNOcKFqu2svKQbiXSuv1bJPkWQ7D2tf-UqV44adzHUeF_1gQFlvc_PglpLeU2vjL4FbP5_LlvvOG77eiUQVyZ6KO28rI_7JchwtaieowrXuNvuC-pOHveIVfnBryquKrMHRMs6zX7zJCwFG0QYXHIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: در طول هفته جاری هیچ برنامه‌ای برای مذاکره با آمریکا نداریم
🔹
حضور مقامات آمریکایی در دوحه ارتباطی با حضور هیئت‌های کارشناسی ایرانی در دوحه ندارد.
🔹
کارشناسان ما برای پیگیری تعهدات آمریکا از سوی قطر به دوحه خواهند رفت.
🔹
هیچ نشست و برنامه‌ای…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445538" target="_blank">📅 00:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445537">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bedeb4c3.mp4?token=OogosuUwJJyeYJ4yKoZMSloH8HDLdwiJA7sr5VV7KX5vyOZ-uhDNbrkraA4gIAD31zffONR-j52lGhpXmNHeMd9MulC7zmVjQ6WlWFwYXRhgmF-d4iCZ7slpFFtae_OligK-DlXgg-s1UF_ZjryGA-5CwX-z7dY3xYgg2AedAXAee3sW0F4YCJEsqEtnx_UN2sqo-Fe7dVJQC7Mxu92HKLjeg1N2RaiUqvipAJsa4HnluUDQOfdy2wpmcskS-J9nr9x9J2YkNj6BurMu2Q6qYWz5EqFo77OUdmn8Q_wObfAZbW6ZRONTjDxpfBhgd77L3vkrNCF-MdRq7PSQt7wjQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bedeb4c3.mp4?token=OogosuUwJJyeYJ4yKoZMSloH8HDLdwiJA7sr5VV7KX5vyOZ-uhDNbrkraA4gIAD31zffONR-j52lGhpXmNHeMd9MulC7zmVjQ6WlWFwYXRhgmF-d4iCZ7slpFFtae_OligK-DlXgg-s1UF_ZjryGA-5CwX-z7dY3xYgg2AedAXAee3sW0F4YCJEsqEtnx_UN2sqo-Fe7dVJQC7Mxu92HKLjeg1N2RaiUqvipAJsa4HnluUDQOfdy2wpmcskS-J9nr9x9J2YkNj6BurMu2Q6qYWz5EqFo77OUdmn8Q_wObfAZbW6ZRONTjDxpfBhgd77L3vkrNCF-MdRq7PSQt7wjQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: اگر با عمان در مورد مسیر و ترتیبات تنگهٔ هرمز به تفاهم نرسیم، در هر صورت حاکمیت و سیاست جدید ایران را در تنگهٔ هرمز اعمال خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445537" target="_blank">📅 00:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445536">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f482687e8a.mp4?token=gy7bS7GIKfCa2117SPyaxevTTabQ3SWd14ufjDLyS2oanv6TADHL_PROIStwey9mfUCPxbkWpCtkDmZeoQTFeJeNtmHwALRfnVO5ZP6mddTLKCsRbzY2sLbO2xELJ1c3kELY_4tcVUznp3ZEa1rHsKm1vMF2XcKWDk2JkR9nU9WJghBJq26b6MoftGE8vR_QKybC9Q1viJhxB6IPy3dRhsUF49z1BiXIhkbFXHhJiGm-CD335gXw6UzpZlIt2uqp47Yi7yYTXGYisxRKVJVTAJEN48VfDP08BKbA7gXt29m2SRlLR55q32i6zBqQQzTPKE30b-GDibgNAkpS-y89ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f482687e8a.mp4?token=gy7bS7GIKfCa2117SPyaxevTTabQ3SWd14ufjDLyS2oanv6TADHL_PROIStwey9mfUCPxbkWpCtkDmZeoQTFeJeNtmHwALRfnVO5ZP6mddTLKCsRbzY2sLbO2xELJ1c3kELY_4tcVUznp3ZEa1rHsKm1vMF2XcKWDk2JkR9nU9WJghBJq26b6MoftGE8vR_QKybC9Q1viJhxB6IPy3dRhsUF49z1BiXIhkbFXHhJiGm-CD335gXw6UzpZlIt2uqp47Yi7yYTXGYisxRKVJVTAJEN48VfDP08BKbA7gXt29m2SRlLR55q32i6zBqQQzTPKE30b-GDibgNAkpS-y89ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادعادل: رهبر انقلاب دائم مردم را به حفظ وحدت دعوت می‌کنند؛ از «علی‌الاصول» برداشت غلط نکنیم
🔹
بیانیهٔ رهبر انقلاب باید همه‌جانبه خوانده و تفسیر شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445536" target="_blank">📅 00:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445535">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c425e5a737.mp4?token=D1ITrrh6STRtTtFVTnehnn9HG8e5pHnfIIyaJdZPjg-jnDT7WM0WTpd4NiaLggjPLXeVdC5GURR8lY7EQj7InFTSfY-wsj1y87M-xGuWiUKnuvuKLFMNL0YSsk6_lWIuhMC5w_Z22WTYiTnHQTEFHSlmLaClo2bux3qjl_fR5gsxNrhDyLrG1pbDnJE1iIlrFhwBDqUxzI1-JLa1grd8oTgE1s1x02JWtpSmiCCs1z6U3y9YuH65hJjMabSdFjv3bPBKyDMi1VEX0io0HFvQXSTQAZ5hZrJbkpC09kEm4jdIV94AXG4aeI6s9AYZTkUulg6W_dO_kcd1wzrmH39-Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c425e5a737.mp4?token=D1ITrrh6STRtTtFVTnehnn9HG8e5pHnfIIyaJdZPjg-jnDT7WM0WTpd4NiaLggjPLXeVdC5GURR8lY7EQj7InFTSfY-wsj1y87M-xGuWiUKnuvuKLFMNL0YSsk6_lWIuhMC5w_Z22WTYiTnHQTEFHSlmLaClo2bux3qjl_fR5gsxNrhDyLrG1pbDnJE1iIlrFhwBDqUxzI1-JLa1grd8oTgE1s1x02JWtpSmiCCs1z6U3y9YuH65hJjMabSdFjv3bPBKyDMi1VEX0io0HFvQXSTQAZ5hZrJbkpC09kEm4jdIV94AXG4aeI6s9AYZTkUulg6W_dO_kcd1wzrmH39-Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: ما ایمنی و امنیت کشتی‌های عبوری از مسیرهای موازی در تنگهٔ هرمز را تضمین نمی‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445535" target="_blank">📅 00:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445534">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3aad4ef7.mp4?token=VdFkGrOMC317xiJxEgriaFAqROJfJ3bQy20ZTix3UD20YcB0TTeDbjREZhpDSJzfXhWec8S85QkspNQkysHKIeFMlX4zAFqCPFgIrB4mHnd7kXnMxbvuIC1E3ZMvu_NaFQggbZz-J4Nz-Jw7UXpvYwrKTz4dinad7AYL4ikW3Bk9NBzuV-glOE338sICZxoSajTCHqo_RCDYCUM2N2n0QYNaiQliP8aK_m8aXDbus6PK7B1VmpPffI5Vcc2BrDTbXxR3cn54qd-mTCbrzi9vw2qxlfX-bN55-Nsos3n3XBOp92yLAuK1Dbmv1IQ4d2jf7nhsGFIAapUHFqrmmEGzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3aad4ef7.mp4?token=VdFkGrOMC317xiJxEgriaFAqROJfJ3bQy20ZTix3UD20YcB0TTeDbjREZhpDSJzfXhWec8S85QkspNQkysHKIeFMlX4zAFqCPFgIrB4mHnd7kXnMxbvuIC1E3ZMvu_NaFQggbZz-J4Nz-Jw7UXpvYwrKTz4dinad7AYL4ikW3Bk9NBzuV-glOE338sICZxoSajTCHqo_RCDYCUM2N2n0QYNaiQliP8aK_m8aXDbus6PK7B1VmpPffI5Vcc2BrDTbXxR3cn54qd-mTCbrzi9vw2qxlfX-bN55-Nsos3n3XBOp92yLAuK1Dbmv1IQ4d2jf7nhsGFIAapUHFqrmmEGzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: ما ایمنی و امنیت کشتی‌های عبوری از مسیرهای موازی در تنگهٔ هرمز را تضمین نمی‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445534" target="_blank">📅 23:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445533">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uImYkW63G6j-EcHxi6wcob23hC_f_2lwtVKhMkXAfmDzvYfxqUV9l53ioIuHdl8GfKhQ4--c8wdWloq3DnamJ76aoc7fmFeoZM7ruVd64ZcWbz-c9jPNf-Lm0Q-LnC67AEkTtYt2saEQueTUaAr9lbXmT7I5EZClM-5CRdTtg6Ohk1y6Q1ATERWneCRL2RDpw_LM2j18E4qHpn67YDhExpmak-NaTHaP8ubxjHFtpeCH0uX6hj2Yg6-PB1oWS9L6tYOH5GCwuNXgri66rHXL7XGxRnv9yWy75crCLViIAcO7r8sReXsS0K4PbVF5haOh2vHopWnjvNV5o9YpI-jYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: اگر طرف آمریکایی به تفاهم‌نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم
🔹
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445533" target="_blank">📅 23:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445532">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a156660ccb.mp4?token=RlLm1VUVFLRP14CEMGgzzzvbax4rGH9K0i2qrYZg7qqN7j9zex3e2Wmg3a1TMCS3gqKMEQm5MAlzn0F4t3w4y49I9pNAwVI1Khy686ccBeVxvibOOOwSlY0Jn7FI1Bjk3_Y45F0s6DRqJvxCpvvlKwDBv_6a7bMg0pfGeaPoMD0eJcdEg7367w6KYJDvGxg1STUD8MwLE1Tw_6jYl8Q_lMPQvgDrI6q7ehgMcNuxJbQ2K36SQyFGTtErYSqCltvy3cwgdXVyqw8mS4pEBP6gqpHdwmSf70c84qxfvHdqkUOM74rGXZ8gbpUJA2XhFf5NTcFBpmjdGPjgYAaxbzfvQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a156660ccb.mp4?token=RlLm1VUVFLRP14CEMGgzzzvbax4rGH9K0i2qrYZg7qqN7j9zex3e2Wmg3a1TMCS3gqKMEQm5MAlzn0F4t3w4y49I9pNAwVI1Khy686ccBeVxvibOOOwSlY0Jn7FI1Bjk3_Y45F0s6DRqJvxCpvvlKwDBv_6a7bMg0pfGeaPoMD0eJcdEg7367w6KYJDvGxg1STUD8MwLE1Tw_6jYl8Q_lMPQvgDrI6q7ehgMcNuxJbQ2K36SQyFGTtErYSqCltvy3cwgdXVyqw8mS4pEBP6gqpHdwmSf70c84qxfvHdqkUOM74rGXZ8gbpUJA2XhFf5NTcFBpmjdGPjgYAaxbzfvQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۱ شب ایستادگی هرمزی‌ها در تنگه هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445532" target="_blank">📅 23:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445529">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrJz9knxI5LqF8R3RegdCLkrHTtk-3AVaSwP6NEoY8kzgTYLscvNAWIm2N4BR_DSLvVpHgLezg6WMqVco6T9Ej03m2nJoOV4dZnjnWICxfKbmexBQ7Zu0DZnfQJ6jOVFSoAoNueXo3Uc0PvGF1rrPCpJ8mRBrEw_U2tqZyIzIxMEBtGsEdq2IjJJKpAxtOvcgWeb5OfvCU0tpEACU34ydBKIevGWGnKT-2dzXskiQkG5CtCtfZ9TUIRx7uq8QdbHo1FkyxW_PWjIfcwBpWctVv72BQY4IpML2iEI3ETPTwaPqCaeqM2HBqXBN628i7TU0i-jBH_CVOCUL7DYfIQ34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عذرخواهی بازیکنان ژاپن از هوادارانشان پس از باخت
@Sportfars</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445529" target="_blank">📅 23:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b43b289a4f.mp4?token=KKEHMEVlcR6yV74MFwfQR5RekFQFUKZ_4UfFYwDMwFgdFBxS5JnO3VOnZII6IVx8UrvgPEbv8oLIVMni-sJKVGHmT0cfTkkzCbSdLfh_5L53KAqNzDPQ6E6cu_4iPAZpqvRmAL5_Om0V9SZf_qrLy12AxRGIXqIpgTrHvV28q2HUR8nTIqydzPbb7qNxied2CiPeZYhegNfMMAJUDROP3ysCOPbGaTK13Upu0bI6ckDjuZIWAQN1muxuaKilEx70-zW_SnbPpwcqsEnqM8ZgaSWQ09HNP4Gcu2e3snSOmAo47gAlhx97nGvzfmDhkq0p_Tasry-94yKDiQOLuEdi5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b43b289a4f.mp4?token=KKEHMEVlcR6yV74MFwfQR5RekFQFUKZ_4UfFYwDMwFgdFBxS5JnO3VOnZII6IVx8UrvgPEbv8oLIVMni-sJKVGHmT0cfTkkzCbSdLfh_5L53KAqNzDPQ6E6cu_4iPAZpqvRmAL5_Om0V9SZf_qrLy12AxRGIXqIpgTrHvV28q2HUR8nTIqydzPbb7qNxied2CiPeZYhegNfMMAJUDROP3ysCOPbGaTK13Upu0bI6ckDjuZIWAQN1muxuaKilEx70-zW_SnbPpwcqsEnqM8ZgaSWQ09HNP4Gcu2e3snSOmAo47gAlhx97nGvzfmDhkq0p_Tasry-94yKDiQOLuEdi5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانه نیشابوری‌ها به عدد ۱۲۱ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445528" target="_blank">📅 23:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzOBXu9Zp1ozTGE7ppiWL6F0xhaKCaXBQpK31OTCSr8C15ulO3LO-fAZCo5bJO-0YU-bLWM_-XHdz-ht2P8p-Z-poPzYBpaobfDZO2NEEXKSw_oFBFkwXaEryRc4Y5yIhU5E9U_uo3z0Ir_m-yYkl8lVPdOy9elMUsew0VpeATAcBb9JHiTngRuG3EK09xyLAuWV9j3qah9I29iFxmOxpEYB2affQFoH3zdqNoRVyCeBwIe7aTdsctF-wRA8HCL79c7ADrgU9qHJR_cbWRltdYI-JE-SBlJdEru9hEO6hPFw0i81VU0nqxMUWTatzsW_nn_S2DwoWunKhOslydYM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا توکلی شایعه وخامت حالش را تکذیب کرد؛ صحیح و سالمم
🔹
رضا توکلی، بازیگر تلویزیون در گفتگو با فارس: من حالم خیلی خوب است و شایعات مطرح‌شده درباره بیماری‌ام را تکذیب می‌کنم. متاسفانه دوستان در درک ماجرا دچار اشتباه شده بودند.
🔹
مریض دیگری داشتم که با شرایط دشواری رو‌به‌رو بود و باید تحت درمان قرار می‌گرفت، به همین خاطر برای پیگیری روند درمان او به خارج از کشور سفر کردم. بحمدالله با لطف خدا و دعای مردم، حال مریض‌مان بهبود یافته است.
🔹
این هنرمند در پایان از پیگیری و تماس‌های متعدد دوستان، همکاران و همه کسانی که نگران سلامتی‌اش شده بودند، تشکر کرد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445527" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
