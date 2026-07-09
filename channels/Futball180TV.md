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
<img src="https://cdn5.telesco.pe/file/vB9xIVf5gQy9DFHWlrxQGSLgXICoMtY-_OIHsdOUuKFBkZi5FEvDYR_uAaOyk2-9oAknWfvh5H2js8m8Nh0g48IY078UpPx7wLJKm34v0ZFz5CEUxbeB33Vqfi7A0xso5oh0gjN3myLD4VCJsfaIc1BsTjkZWDC8d5TjcA71SeMjAjH_7u4Eeyu3-we2ZxMKA18GkrWrTfTKqZ36nGuScbyC1iZhseEu4zkB7j82Bkmp2jpwz0Nkiy9m1UOwi8A7WN_CyadCNp9a85ziJ37L8x4RacNhdY_2QLyoNTa-KyKbPtPOg5beXGs6DYxk8uWjLyG9OgLBL3ENtcD8JMlvqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 608K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 12:21:09</div>
<hr>

<div class="tg-post" id="msg-99160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d77513fa.mp4?token=snsRb-C02aZJAq85aRBTzcstNFYlWHrPJYBCE9OJUvzrmz34m5X0wAQ-Jt4MUGin-ja1CeaN5ZYfE1KMZ4C48V13gWKLLsMajHEJHCXVDNwHtWjq0gDXgZr5uWsJf2D4cCMnSJUa5mTL78AnzWpr-f9syQGG-bjs3KdRUbYw52ZfeKJQWLAD3ne3FxZU_czue8yeI35PQj8mXuaDFLhPCO57lcoKBcvNoGSUouC2hm2vWk_7uchXfBjL9TkTPVJCLl5qmcIWKWrNaG9cfVar97-FiGuCS3279h5q1V4QRgMM6Y73Ln_jszKdqW4IfqQPjaK1J0JbK06GcHnL-eXUwWslRIn3EVZmKugNv_HGH8SPrZBV5pZ-sDXNd36rjpELAG4MDQYJwvsubUr-h40k4WsjaHYZXMXkk9Y1nIg1SbsioHus97UksDaAHFKfuFazIBS9BD3q1vXgNagPyR2k6CW0FGcNe_zt_tPX5SwcR9AAv0--rmP27EvuJiNK-WY9bmbLqubhYoLxzerBnVP_XiwY9aQzYEtEPlU2PFUVySk9SYQF9aAWR3_QNd-GpJ5CPwCN6e3POll578vpaKJwu910Z9k0vT7xvoN3FiaOfxPDNqefeliaXLNbAGgyTA1op26nyjXcwcJUmSugV4j6QyTltGNpDnhwZGKxdJb6-Mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d77513fa.mp4?token=snsRb-C02aZJAq85aRBTzcstNFYlWHrPJYBCE9OJUvzrmz34m5X0wAQ-Jt4MUGin-ja1CeaN5ZYfE1KMZ4C48V13gWKLLsMajHEJHCXVDNwHtWjq0gDXgZr5uWsJf2D4cCMnSJUa5mTL78AnzWpr-f9syQGG-bjs3KdRUbYw52ZfeKJQWLAD3ne3FxZU_czue8yeI35PQj8mXuaDFLhPCO57lcoKBcvNoGSUouC2hm2vWk_7uchXfBjL9TkTPVJCLl5qmcIWKWrNaG9cfVar97-FiGuCS3279h5q1V4QRgMM6Y73Ln_jszKdqW4IfqQPjaK1J0JbK06GcHnL-eXUwWslRIn3EVZmKugNv_HGH8SPrZBV5pZ-sDXNd36rjpELAG4MDQYJwvsubUr-h40k4WsjaHYZXMXkk9Y1nIg1SbsioHus97UksDaAHFKfuFazIBS9BD3q1vXgNagPyR2k6CW0FGcNe_zt_tPX5SwcR9AAv0--rmP27EvuJiNK-WY9bmbLqubhYoLxzerBnVP_XiwY9aQzYEtEPlU2PFUVySk9SYQF9aAWR3_QNd-GpJ5CPwCN6e3POll578vpaKJwu910Z9k0vT7xvoN3FiaOfxPDNqefeliaXLNbAGgyTA1op26nyjXcwcJUmSugV4j6QyTltGNpDnhwZGKxdJb6-Mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
احتمالا بهترین تیم‌ملی تاریخ ایران :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/Futball180TV/99160" target="_blank">📅 12:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d456e6fe3e.mp4?token=vj_kKk183YMMe4j-GhPGc_a9tzYRiwoYzLXWbZW5tog_kVfy8cTqpNexkpCpcqSY8dpe7rUJ4hEB49RdvbAD6eOuUvuY18t_WZx6UEujEzGnOb5S3OOVkwvaOFJ_-qKeNzNR99W_fE9ZL3eNLu_JDgzocR3gC7tOS_GJVKpmUc1VUIYZEr8cf0sNVHa9ut9e7Q63ng0ZuqLCDae2UWeiAsvtNFO8V_A0UDc1nL8ZnmYWv8jj65IkiwmA0MPfr_AOmAcm5JhgQsWqkRbX1520j5TWLqOF_ARTwH8ywtseX8ccjLN9BWMELEOB9JCrmIs02PSi4y6kYvb6zs4dF0_UVYwz9mtpj4RI_JldJnSFFKjxoPWmXpXxABlltQbXl7mPqpsiA9hKYLyFLmjbsvgPzNTPLkP4pdDnT6MjrWsmE2XYQv-B90N7QwGOjepYOlT08xgS7XcrCcRe7q05T0X41fyz4OWC8bU1qxKrTBQQX8fqK4BSWNXm0WvIZ7f5Kg0JHlFhbq2BkMg8NcKF56Nv6jvoMKHbVVg68iw3j8lcKtLwMAKtRNFDsCaU965JH030CrPsf_hlNYTKW2cVz-P_SnATQxs7G0CyooJQuH0JD-csnX3z_8CTOhnv1lXwFHLHApXijAnEj9FELKh9QyKHtZwHfQh2HdNgWwNNTsQY_qs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d456e6fe3e.mp4?token=vj_kKk183YMMe4j-GhPGc_a9tzYRiwoYzLXWbZW5tog_kVfy8cTqpNexkpCpcqSY8dpe7rUJ4hEB49RdvbAD6eOuUvuY18t_WZx6UEujEzGnOb5S3OOVkwvaOFJ_-qKeNzNR99W_fE9ZL3eNLu_JDgzocR3gC7tOS_GJVKpmUc1VUIYZEr8cf0sNVHa9ut9e7Q63ng0ZuqLCDae2UWeiAsvtNFO8V_A0UDc1nL8ZnmYWv8jj65IkiwmA0MPfr_AOmAcm5JhgQsWqkRbX1520j5TWLqOF_ARTwH8ywtseX8ccjLN9BWMELEOB9JCrmIs02PSi4y6kYvb6zs4dF0_UVYwz9mtpj4RI_JldJnSFFKjxoPWmXpXxABlltQbXl7mPqpsiA9hKYLyFLmjbsvgPzNTPLkP4pdDnT6MjrWsmE2XYQv-B90N7QwGOjepYOlT08xgS7XcrCcRe7q05T0X41fyz4OWC8bU1qxKrTBQQX8fqK4BSWNXm0WvIZ7f5Kg0JHlFhbq2BkMg8NcKF56Nv6jvoMKHbVVg68iw3j8lcKtLwMAKtRNFDsCaU965JH030CrPsf_hlNYTKW2cVz-P_SnATQxs7G0CyooJQuH0JD-csnX3z_8CTOhnv1lXwFHLHApXijAnEj9FELKh9QyKHtZwHfQh2HdNgWwNNTsQY_qs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
فینال جام‌جهانی ۱۹۹۴ میان برزیل و ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/99159" target="_blank">📅 12:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجارهایی در بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/99158" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99157">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sja9WFgEO3EEbs02qOW4m5wmR8RUsMkUIYBVsCjBEQ62P_7Re0MsjGWF3hMhYk2SF1cJxMjvAc4MbxqrqSV0L9nv6bX6PTsc9Qwe-zbfeFFoG-0anXvFmvhwrbrUqzLOg9Ii9A9jQAge5UmpvY_DB9Kc1WaNcBYFDygFPQEnSOQk9YzUbLLgsGs42ijFB_nca-vBVvKXXEHg5wSHo-vG177gJrmn00FxiQP_63ZQl4KoPqksw25lZQXsUEmIWV-T4xDapMdrP4Ymrpc8IVfmeOZCkYfWAsbUg9Lcmd1rvKqFEAEoIHJuSn8wb_l4y3zqCSDO0EoVBMtbNho0NAm0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
❌
#فوووووری
؛ اسماعیل سایباری ستاره مراکش بدلیل مصدومیت امشب جلو فرانسه غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99157" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99156">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجارهایی در بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99156" target="_blank">📅 11:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99154">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5cb5d89e5.mp4?token=djQ5DeLIvwhmyh5au8nV8uHUkwY1e6NTEbr2cUCWibjqs08BIJccSLTU52AL7aTYtUzPt03VVc4PS4z_0GHRxgZxgIWE6zyln-PNWovCMudWcR_KV-QkzSboxV2UNJaIJcfKG4uBR2ph_IbQBjDdoF64YsfDtVvSZ9jA05cZNciGPmmX3GPyu8Hd72idOSPmCXR3obtyEo0T5pT3sCDvDLmPH6Zd6k1c78pW3k2UxYUEcTk6k2Z-af0mflvwvC1OSqScFPWa3bXH4EZLtY8xiraF-q22eze_D5xiJ09IWGCNV6EnGIlODVYAlGoFaxWeDJONST4UUahaPOy0A5oRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5cb5d89e5.mp4?token=djQ5DeLIvwhmyh5au8nV8uHUkwY1e6NTEbr2cUCWibjqs08BIJccSLTU52AL7aTYtUzPt03VVc4PS4z_0GHRxgZxgIWE6zyln-PNWovCMudWcR_KV-QkzSboxV2UNJaIJcfKG4uBR2ph_IbQBjDdoF64YsfDtVvSZ9jA05cZNciGPmmX3GPyu8Hd72idOSPmCXR3obtyEo0T5pT3sCDvDLmPH6Zd6k1c78pW3k2UxYUEcTk6k2Z-af0mflvwvC1OSqScFPWa3bXH4EZLtY8xiraF-q22eze_D5xiJ09IWGCNV6EnGIlODVYAlGoFaxWeDJONST4UUahaPOy0A5oRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇦🇷
🇪🇬
حرکت زشت و تحریک‌آمیز بازیکن آرژانتین در مقابل چشمان محمد صلاح!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/99154" target="_blank">📅 11:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99153">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfbfdf007.mp4?token=p-f2DCHU4oNp4mjdMAQJshOG1xiTsuvVqR1seoXSE3rotf7UmADETeizSkatNIlt4RzFEYMOXpLIyKjgf3bIrojnwEo73s_HfP2TtT-KHL6KW9qCa75kDwvi5qWJl7mWmoLpqOG7kcTemA6hVk5BCnUbvIyJb5oY176OutTiRCfLLYb56x4s7iNdh0lXbuDW9Qvauos4rd5_VsdAsoKQS8GNqHBcbbuy0zCqvLoHeNTEvsYHlG-vaBnEZ4OBJ9UfNZjOI5tP9bIGe1orTQEv2t-Ul2npJPW8p5BLOf7kRnC_wPgeWQWYqKJvJXuAPpGP66Kod_Xi0O0XHTNieV3X0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfbfdf007.mp4?token=p-f2DCHU4oNp4mjdMAQJshOG1xiTsuvVqR1seoXSE3rotf7UmADETeizSkatNIlt4RzFEYMOXpLIyKjgf3bIrojnwEo73s_HfP2TtT-KHL6KW9qCa75kDwvi5qWJl7mWmoLpqOG7kcTemA6hVk5BCnUbvIyJb5oY176OutTiRCfLLYb56x4s7iNdh0lXbuDW9Qvauos4rd5_VsdAsoKQS8GNqHBcbbuy0zCqvLoHeNTEvsYHlG-vaBnEZ4OBJ9UfNZjOI5tP9bIGe1orTQEv2t-Ul2npJPW8p5BLOf7kRnC_wPgeWQWYqKJvJXuAPpGP66Kod_Xi0O0XHTNieV3X0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو فنا در حال امضای قرارداد 10 ساله با تیم ملی فرانسه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99153" target="_blank">📅 11:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99152">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEMKX-Y54gMPQLSpGxlrpdgsGBCCEDCAkjjvJQksEYaPbERIPbB26_hceLKtRZCcKLhONlf0RcwtYVAC4_52ZIqV88HzL1Ud-xvp444nuRXWMOzOHDqKBSbYVSJFgOyWQBjrdHIyKNAiUAWM89kpwpyxucuvBgwwvLOUEkc8NoMAn6zSUtVcpb74dUG4-hdQCmwzYhRP_m5czKSHtmrtD-3XnT36xXKyg437rGBTTZvpmrQ3P3_sxUkNZUuIW_kEhdwTzW852gAKzosOEFSku1YCW14klHvPTPkSqmJDXDE3TBEtEABOd9NSFhykqUDq2z6U8qSs2CxdBhkvvpVSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
#فووووری
؛ هانس یواکیم واتسکه، رئیس باشگاه بوروسیا دورتموند:
"ارلینگ هالند علاقه زیادی به رئال مادرید دارد و این را پنهان نمی‌کند. به نظر من، او ظرف دو یا سه سال آینده در آنجا بازی خواهد کرد، نه الان، اما به زودی."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99152" target="_blank">📅 10:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99151">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WznEtGxYDWmG8ZJzzXe0mAOKebp54na5OriVxcQbFHW1qmQU3_hidomJKucJs0PvT0-BA3UPdN0J673YfAH8img7NCtI6Js2cKlLv6b4Q3QguxLIcSYOk9J9VIHLTfzBCNZO9AkvKvKer00OFDGmUoMxSVZY7zx6cmgSJa_dlyQf6RZ9hdUtWn27ri3ox4L0NKDN6o3Ie0udbqUfDlJ-43HX16Z2pnteAAg7jCP-LHCXyvRaYT8PJFLsia7b07j3ygUMvYzBx7hjHXRTfna_0dPi7BkeVsJzkm14Tt7iQhWB1eVmznZx2w0gygBqbM-t1DE6pseyvzWooKPLTLnDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
— نیکولا شیرا:
- باشگاه آرسنال و برونو گیمارئش به توافق کامل در مورد شرایط شخصی رسیده‌اند. قرارداد پیشنهادی تا تابستان سال 2031 اعتبار خواهد داشت.
🔥
󐁧󐁢󐁥󐁮󐁧󐁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99151" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99150">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔥
🇫🇷
🇲🇦
تنها چند ساعت تا بازی مراکش - فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/99150" target="_blank">📅 10:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99149">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔥
مرور ده سوپرگل تاریخ مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99149" target="_blank">📅 10:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99148">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9ed1c618.mp4?token=Wvmu1QArre9ZARW7fX_SKPKpHwniZS1FTebgHtUBdKApfdcdLByeqFoI3NpD2eYkuB2QwZVuD-8ME32Maj4_2pnhVrynTuSSTwUyArHgo7pSbV4Z0RTbEUSrS21h8GUilKkTBJNaPZN0qRwtIAYDFiGen5-4Ehmj0U_ENchPxlCVsCuWUN_WdkLlt8uI-C2MfRzwowvmxg3ZKrLgeSz5ty6MV3h3jjLOQp44WNf6EVwAPUBI3TtdWnw1IByao1X4knPxp2So8k_Zfy_yfMHa0FZef2Vyl-TrGP6b9gyBOUXY0X41z2yeeSbVs_8UnWIjUot2gCimmv__33wafWda8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9ed1c618.mp4?token=Wvmu1QArre9ZARW7fX_SKPKpHwniZS1FTebgHtUBdKApfdcdLByeqFoI3NpD2eYkuB2QwZVuD-8ME32Maj4_2pnhVrynTuSSTwUyArHgo7pSbV4Z0RTbEUSrS21h8GUilKkTBJNaPZN0qRwtIAYDFiGen5-4Ehmj0U_ENchPxlCVsCuWUN_WdkLlt8uI-C2MfRzwowvmxg3ZKrLgeSz5ty6MV3h3jjLOQp44WNf6EVwAPUBI3TtdWnw1IByao1X4knPxp2So8k_Zfy_yfMHa0FZef2Vyl-TrGP6b9gyBOUXY0X41z2yeeSbVs_8UnWIjUot2gCimmv__33wafWda8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
آنچه در بازی آرژانتین - مصر رخ داد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99148" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99147">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frpyZswgjM8o4U2hbqnrW64NLij21bv-ew9FVm0bN_2n9g-pJrq9vkifJM6JdmKsAEcSeTBcEaRT-m36QxILU04ijOVTLcrG1rCiOQpaHwy170jfjDZmbMmwxCrNcxI4N-dTdJxdPHE3krlguSXK6N5qdRHTG2pMdQEMQoBbnmrBE7SxtTet29CtUyyGznxykVVgBqzFFMvQ2JXvamd_49tkZWQdNw4HTJbj713bElvzDdH_S7m2SNxvtR8R0Iub8fVdUATDQo7YMvm2W1MhKPqcxf4BCaLI7aQX7PSxmf7aNrjRgnaURi4lkXzz1QFGXOVTY4_jdUToI5p0kGct0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99147" target="_blank">📅 09:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99146">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e88795bc.mp4?token=KU6LeBb9nQCFDyw2LEzZVI01EpupbsAvbIr-kl_ljl4pzqQTG3NJkAUDNxp-yeKkjCejdhk8qaGNr2woWagLrf6KK1vcpFyLgL4qccIFt4LvPAYYg2E9F2wKgQ-LAuagXouALHA9ZozRLayCvxXrDX-oWRV-xOpxSoadZibscJnI3GIYknzdytvfIyqjNbucIZQUT65k3lcfhjVH8mxiig_fDU6Z09c_q6DfUw6t4H7Y3lbtoMdJtgOTV0U0O60y0Pz6Gvoasv0p3Z-H5sSPTxwjKEpzRbAwKX2nj21GVB2ZVCffCvtbjlR02_4W3yLP6yg6qgp3SbIrGhCbHr22vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e88795bc.mp4?token=KU6LeBb9nQCFDyw2LEzZVI01EpupbsAvbIr-kl_ljl4pzqQTG3NJkAUDNxp-yeKkjCejdhk8qaGNr2woWagLrf6KK1vcpFyLgL4qccIFt4LvPAYYg2E9F2wKgQ-LAuagXouALHA9ZozRLayCvxXrDX-oWRV-xOpxSoadZibscJnI3GIYknzdytvfIyqjNbucIZQUT65k3lcfhjVH8mxiig_fDU6Z09c_q6DfUw6t4H7Y3lbtoMdJtgOTV0U0O60y0Pz6Gvoasv0p3Z-H5sSPTxwjKEpzRbAwKX2nj21GVB2ZVCffCvtbjlR02_4W3yLP6yg6qgp3SbIrGhCbHr22vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
شادی عجیب و غریب خانواده آرژانتینی بعد گل‌ سوم و برتری مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99146" target="_blank">📅 09:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99145">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395ec83e2c.mp4?token=EWWlVdcm4tNcopGGskNmBwN4h51VLqJxmNHtg3x_0Ub1Q3W3Pb-F52h-dQl7tvxQAVfOflCMIRUvX9D8nmO2Ajb6UPrcoxYhhD2BL10Qn6ZMBF8zF5EHhme2mXlEUhPpsd32CTETvdCnBpT_NZ_9wN9DHgvsjvWoZQN7wjC4Bjl2a0DyJirLb97GHQXwlAqwpLrd1sSSHJ9n5ujTxVa3O1qVHmJJAsJip0aKhwWTOjNMQMEq7ldX38aE6ccg6Wlv7kmxXIIBZbxQ7WKWd4C4rfdfHy9i_UW1K6EigQpKDWJEk1YY7wwTmXGpdLnEQknZg-rCdNIf0AFWK7cJbrBHtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395ec83e2c.mp4?token=EWWlVdcm4tNcopGGskNmBwN4h51VLqJxmNHtg3x_0Ub1Q3W3Pb-F52h-dQl7tvxQAVfOflCMIRUvX9D8nmO2Ajb6UPrcoxYhhD2BL10Qn6ZMBF8zF5EHhme2mXlEUhPpsd32CTETvdCnBpT_NZ_9wN9DHgvsjvWoZQN7wjC4Bjl2a0DyJirLb97GHQXwlAqwpLrd1sSSHJ9n5ujTxVa3O1qVHmJJAsJip0aKhwWTOjNMQMEq7ldX38aE6ccg6Wlv7kmxXIIBZbxQ7WKWd4C4rfdfHy9i_UW1K6EigQpKDWJEk1YY7wwTmXGpdLnEQknZg-rCdNIf0AFWK7cJbrBHtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشتباهات مشکوک داور بازی کلمبیا و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99145" target="_blank">📅 09:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99144">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
به نقل از آکسیوس:
مقامات آمریکایی خود را برای یک جنگ چند روزه یا چند هفته‌ای با ایران در تنگه هرمز آماده می کنند که بزودی آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99144" target="_blank">📅 09:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99143">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox08oR1_FcrKXDD-NP-PwE65dbQ2_uITGVj6y4M6WOkBEgKzudZQNjIS4Rkj-U2QZozZaIu-2eUDIOR_WwDotDruH923TZi6ayS7fQIWEew_VXo3P9v-8Q4UM69czouOPFQtL2K6x5JNhxmBwgzK_nrC8cG5GJz0kl0BfiN1RGhfXesDE3557NQxXQyb-AMdsoCSJdDDiwI2C1CCXrbTUdiOY6QTpRa5mS6-lZErGWw6OC6p1JtOMK_I-10ytRypCNj2CESAaNkyPmbSg-Jy0X1wmJQl6PvGI41_a0kMMGaQGl1-WEQecDxCq6LbgNlxhVhx3QJOHjcGEKhumL-BQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
در اقدامی عجیب و برگ‌ریزون؛ دولت مصر ورود لیونل مسی و خانواده‌اش رو به خاک این کشور ممنوع اعلام کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99143" target="_blank">📅 08:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99142">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
بیانیه سپاه:
زیرساخت‌ها و تأسیسات مهم پایگاه‌های عریفجان و علی‌السالم در کویت و پایگاه‌های الجفیر و شیخ عیسی در بحرین را هدف قرار دادیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99142" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99141">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSIF0GBAJ8EDBNmVZjhkDlCFiusMpWUBk5WILJj8ipd303cmtUBtyzaqscKF3L-bP7F78KHi5_MDwrnVgrCxh9owObhsPvcZjkxkoDlzM4saji4P6G2R1GoBQ9ADf_0eoQY10kzPSAy2flEYTWy5X8ZLvwgeLTwU8CwskS748E3uwMETlzUXsu126XqJenm1EkPIvM4zfr0FYCuqSqaUIiucBtdjJcXEiW_a8Gtso7wvyFxDZFZhf9hURmQhUltAmnWJgEDeUtPoSmuDlVjaHtDdkUFULN3gaJoa8C4CZAfuzuKZAas8w0ABVDCMnVpoMKc_8jPyBMHwRTX2fOXxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
🔻
دوست دختر جدید لاپورتا
: «من بخاطر لبخند لاپورتا عاشق او شدم و نمی‌دانستم که او رئیس باشگاه بارسلونا است.»
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/99141" target="_blank">📅 03:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99140">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=eR0LMA5IwQ-VgELPkYZd8IwsdcKsN29uuD-0Pbxd6yCs667ATltIsfuE9IeiPAtlRZAn3o9-4MkffkuWgf9ZEMXERp0vshM3gRfdFXMXUiDggwEoIsGUuVWvmSdU73O949H7qYRayJFBMnYI0pSc6uao_-hT2BsnydVBoMmdnYEGFDH580t2aTCEZo3xurVVQ2fq_TAw4BNrB8wNsl-fhDXJpsfkNVwyZpkDtrw98DYht7mm2_Kf7teLaVihhaoa9_LPe_Ovgl6GzXzQ2q3lxxXgeO29myHLapzPuI6YUKLVE_E_hhnj6emGOr7ofwiLLPU6OuH8W6QjU2r8iWCjzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=eR0LMA5IwQ-VgELPkYZd8IwsdcKsN29uuD-0Pbxd6yCs667ATltIsfuE9IeiPAtlRZAn3o9-4MkffkuWgf9ZEMXERp0vshM3gRfdFXMXUiDggwEoIsGUuVWvmSdU73O949H7qYRayJFBMnYI0pSc6uao_-hT2BsnydVBoMmdnYEGFDH580t2aTCEZo3xurVVQ2fq_TAw4BNrB8wNsl-fhDXJpsfkNVwyZpkDtrw98DYht7mm2_Kf7teLaVihhaoa9_LPe_Ovgl6GzXzQ2q3lxxXgeO29myHLapzPuI6YUKLVE_E_hhnj6emGOr7ofwiLLPU6OuH8W6QjU2r8iWCjzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تعجب مهران مدیری از درآمد علیرضا فغانی وقتی در ایران بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/99140" target="_blank">📅 02:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99139">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aC-FfBGGuNwWHQ5Vplgb3vAzBrXGhGB3_4Wa559YiAXn08LxeAsDmdnyjRo5TKXa66Ino_ZXG4XTOh9uLv9jg105W-b3-sGFyOPzOhvzd4XixsnXVCMEWAEaCHQWA-jEUrVhTgYwy1776LAZ-CW3r8QybXqnXG6ydXv8WIfXZPLfyjrnq3rTGtxYE85LB8bbM04kTZ0Ik4DlqlMFWg23Sq7UOLFREkEjESGk3V_ZMleP0yWrpevY43FVefGaC55k3Orbs7Amj595MAPORqjHdcQ7S4wX1parW3RM2mwqmJoRPhe7_wyNU9kwDM-lmRLqJN79e5xaYhImkkbsmVoOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/99139" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99138">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv0X3x9lqCuQYFPJe02fVxAjIA6xgkl5HLgmudPfVF5F0H2Zh9OBonlj8BKeMBBDMaImSu7zzKHLt8D8w1MPnTA1yNxBkYGuOdDDdz5sAX2J56ltzH-qgIQ6DGERRjvyHPpc5d7ykUayMZoU-HrmsO1xuUjujpzPCOw1eOVVUzorOpc7CVBUuQlP0tqIW7XJlpcPbne6VX0Iak-5hARPfYaMUoDxj1JxyE0ZZh14A52aC2nuwZEdf8imHb21vNq5ayJpXFKyWu5F5mzOhm5QJFXAzMwBUFcC5Tq13nrSXcfmC5YQPl6QnI4JmgTlgvQcX5H20YV-JWFwIQxmJ29B6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تفکیک 3 هزار گل جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/99138" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99137">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99137" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99136">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LgRzkMunuWmUhth9s7DSa90NbKD7PdrJnyyspnYjhdb4xLNxFGS9e3GaGAk1eDtqORnvT7mfngVjAo4d6vbxqUQLUu5EleLV0Yk2e6ofIFavrt6D-onQyOmXt0pX0N7nAL-yveJftvzVaq2zAw1dGefG-4JS0n5R2wID3fKwdqxZj96h4Ei7lqT3MPfALW-xd7ynSM1P5VOfyELS_mdKJyHW_4iTpKrTrI5GSdIBLzo4NBKvk-fCKZAMCvTIFa7DZ_Yj7iUChl1m0-2UTj_mf7UHW5mN6rHSS-vYeBnV0xieh60OZSWq8FQiahMEu7F7CaFijT6FPNyNjtQRmiXSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99136" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99135">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
رسانه های برزیلی:
ممکن است نیمار در روزهای آینده از فوتبال خداحافظی کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/99135" target="_blank">📅 02:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99134">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYeictgruHL5fOmHNhgEe7qXSmiN2J3_G7um6Z-ehw7KAG8IqGlHC1qdXKG3PgVxPyy0l0BJSbV14HUBjCFWf1QQ3ngkWoSZg05zn-715VRONNumD_7RYoFnrFhEcQMEUmbOWnwnGgaZeQACACaJM-TXWUbyeaa16srIad4mEs-paUGpTnHMFv_dCN_19mJclreBKNMIu-ox2rZQSCgOIppxCPuuU9FbHNoaBfgDRDXSJcLvHX4GBqZovnCm5G6tyCmHF77TKBkkZCDfiTOiS5wCpso1OEIe9lR2pLEk8cC_Fx0gD9oT0Xvzq2d_Le79c7iDTqHPlJw95qjGjVxxeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو:
بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/99134" target="_blank">📅 01:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99133">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8ZNe7bL8bQ8IDiLUNSWpIZQLbhLNIgAwp0ikgCiecHBOeKy8AqN2_weviK8o2w9AmeyyIE0qY1zKxdzqSvbN9X2Ss601Jvfzx5wmYE-LApXV-Pega1MC9KoTPe03UHECn210GxCZAYqUlW6pYrwAjCmjmIorHWGmvPITXHXEOZWG1d5ec2UCWDFZDNDIP7LUGnYlZx3yJmx3ZXAqgg6a7hCguOV5ymtT9VX9fE8wPXqPVZDgF4IV23A6KQy6gHLN2lmGLfqnI41fbEkUnqQX9KX3SUfru-60yYth9H3EVonGcgM5jtDSSXSFNzcsJCKpBX5UJQbxuk4tDE1CIc2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب مورد حملات آمریکا قرار گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/99133" target="_blank">📅 01:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99132">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
حملات امشب آمریکا رسما به پایان رسید و تا ساعاتی دیگر حملات سپاه به مواضع آمریکا آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/99132" target="_blank">📅 01:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99131">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpuWvVLTgQvr-tiZqqWexIUdXfJc6b6JSn0XTTGp9ATm4MkHEEOsMhhfoSqsOrgI877M5oI2Ykxi4S2GTuRPKBijU7Q7QVWcyR3l3GO9PYrf80MRSz0YtImb5SN0-CDxzDNZRwdmio3d7bThQGx8c7BRrVOLTU-47S0ckoUsYYREvcZNBaUpUVVnWB0QpHV0YE7iFrPHXMZ5NzhV35rLRVQyqBrs6joJx1R0qvvCngtLO5DVknuQmXZ8elzhDiG4dbDcRDKbN1aPRiDLYdLGNzBQcJDBDtR-IGlSnBoX_cadHoH0xhL0X3WFw6uJl6pkvAGDhlkOl-1XFbAMyrLIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زیدان:
لیونل مسی بار دیگر ثابت کرد که بازیکن سیاره دیگری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/99131" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99129">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE8X5QZqoHJsNBr8W5qlEPVSAPlyTrEjTf2j6YY-tMqhy8lXhl-XjWZ1HVUS53J8PCjJQoqMGDVRSKwpDJag4xUOOLoEEnmfOfU4AYWr_jg53t7sba8eGzJ01LwQVIi7YoR8QK2z8vsoKECkkY5wE7yh_f3VLFOt15N8tKXjz4J0s___uM20-U22TYaws2WPthkgS9XnUhaxl-9cG_hgQqpEsZVDolPM-kupigON2XArYFbOIUkELkBZcSN83AgyUqXnJNA9Bx6224MzgPA6FLtTHx_TVD4r5HwbnFGMpDF0kEswKw1bbRQT3hbKdGuvGnCp0EsoYtZ4qWuseeaM_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/99129" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99128">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ شنیده شدن صدای انفجار در مناطقی از کنگان استان بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/99128" target="_blank">📅 00:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99127">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8JM8jFJcSFPOeop5pAYPfByXpI0HdPAAx7yquGVQSC32VLqGm2jPhjWryssPrwt66npyhPl9Yk40TVzNLhpulK7B4--fndpJts3yUt7ecTo3sfCIvQR0GOQQqpdNhiSTB0lvGEyJUPwDGJLsm7xgMZlL7vIXF1stDIPm_GTU8Pq41B4XAmN4ALmSZDKIvMOCkjJjio66mAuXEWL7kqcWwzOKpqTcXbnHhq3dhVjDhnnnTxnH0E59k1rnCQkOqupJuHz9JTKRMN6GU9qWjJv-A6pxyVOUEzqsPtF9eq944WFBdX2Y86F8emaTGFXxPUtGZksMEG09xA0xXeHhLlVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
محسن رضایی: دشمن متجاوز و هم دستانش به شدت تنبیه خواهند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/99127" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99126">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
یک‌پهپاد آمریکا در جنوب ایران هدف قرار گرفت و سرنگون شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/99126" target="_blank">📅 00:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99125">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
فارس: دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/Futball180TV/99125" target="_blank">📅 00:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99124">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgZ2KrkxEbzgYhTV6HU5phssQH_NTVVsN19uEbOAsTVPUF-jw2gYxBmAU6olTso7crBhs5qKHwG3MWcnC81I45N53ZaUbQP11NXRAflf2XHPhxXyeBGAukxY08iru41pGKlqhj9hs8u9Y0jo3owBtaqTc1VDBDFAzI2ZIoaXQ-1I1HRhBKCkFButHCQfgF0RD-BWLIn_yMHSmbxcxH_jcslHObzJ9q0NnhqdtLS82Ze9QpBEHxJzk9R4bBFbkBchJon8rnVf-qZpLtqfhE5vZxDuCRV2HVbkeT1rR5MnqNQFsiE9z2XPka0_7SXBuaQ8pL4IjywAV3nT635a9zFLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
پست جدید کریستیانو رونالدو:
‏"پرتغال، همیشه و برای همیشه."
🇵🇹
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/Futball180TV/99124" target="_blank">📅 00:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99123">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
مقامات ایرانی: تاسیسات‌نفتی در حملات امشب هیچگونه آسیبی ندیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/Futball180TV/99123" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99122">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
انفجار های مهیب مجدداً در بوشهر رخ داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/Futball180TV/99122" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99121">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ انفجارهای شدید در جاسک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/99121" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99120">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوووووری
؛ اسرائیل هشدار شلیک موشک از سوی ایران و حزب‌الله را به شهروندان خود اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/Futball180TV/99120" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99119">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مقام آمریکایی: حملاتی که امشب انجام شد، گسترده‌تر از حملات روزهای گذشته بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/99119" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99118">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ شنیده شدن صدای دو انفجار در جزیره ابوموسی/صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/99118" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99117">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrkzHn6VOkdGxqkcYbgznv1IvbX5OvhpIdQ1BM5s88j_c1ZRZO4OPqXN7ONMLa8Iy8iNd-hLvfJqA9aNimx4eO_hEwxrfP75E4D_6MxRBH6nfDTyU_9Nt8_ZPHb-ssrb5FGy1FNsKcPzu27VklMUC0LU94kyN3HRj3EwgJPNp4nbFmo806a940MYu9OzJENCRkowecEThGgfuZiz1WbmK7a_h84c6CiUOXM4j4YH9cWtypqYdkbc2x9tjztOBElGT6cXHYRsk1YWg2HQrEQET8SapKpmXZ_LYmCnRPiL_abVfswCSUSu7NAtF1gUtvspKQvsZ9krRAIBXWnFTfwOpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
تصویری منتسب به شهر بوشهر
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/Futball180TV/99117" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99116">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
کمیسیون امنیت ملی مجلس: بزودی پاسخ قاطع رزمندگان اسلام در سطوح بسیار خاص و ویژه انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/99116" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99115">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
منابع داخلی: قرار است نیروهای مسلح ایران به زودی حمله‌ای گسترده به پایگاه‌های نظامی آمریکا در منطقه انجام دهند..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/Futball180TV/99115" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991a36705c.mp4?token=K4sX6oRSf4HkuFbXgfH_KZwsBhYrQolA0rm8DobpVrWEHWWV7DDsg_RSxqdkkYKBcNl0Q2d4Q-XyNMfFIIMyOllAmMuNMjzk_zA2-QklCMxtUrbRxORqKfzQpnT4u6ZimZaPO9meT0ucgl-EFOlM6q0hdWF30hcWYApG1tJuLrIqlQkbfyXa-sBN-9leJ8c4wTxGTmqqaK84YPKDExuAvu6hgmnh8hPJq3HRMhppkF8Y0oW8uwmbGDCfq3AiWfaAVP5k1u02K8L5c2UP0gryZF72IvJ2PhNGoOfN7FyNR92jN1Kcn_YeNc4IIImQgaGPa7qkYMKHE1P012g2vuJFag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991a36705c.mp4?token=K4sX6oRSf4HkuFbXgfH_KZwsBhYrQolA0rm8DobpVrWEHWWV7DDsg_RSxqdkkYKBcNl0Q2d4Q-XyNMfFIIMyOllAmMuNMjzk_zA2-QklCMxtUrbRxORqKfzQpnT4u6ZimZaPO9meT0ucgl-EFOlM6q0hdWF30hcWYApG1tJuLrIqlQkbfyXa-sBN-9leJ8c4wTxGTmqqaK84YPKDExuAvu6hgmnh8hPJq3HRMhppkF8Y0oW8uwmbGDCfq3AiWfaAVP5k1u02K8L5c2UP0gryZF72IvJ2PhNGoOfN7FyNR92jN1Kcn_YeNc4IIImQgaGPa7qkYMKHE1P012g2vuJFag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
؛ ویدیو منتسب به حملات امشب آمریکا و انفجارات شدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/99114" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووووری
؛ پدافند اصفهان فعال شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/99113" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به نیروگاه برق پایگاه نداسا در چابهار   @News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/99112" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRUCjEh_-KXT-IWN2StjDdq4-3CvE4ALs9ZaCGmNbT3Y90eIsLTB_zzUygU0oCngN4VaufjmiQ387QkPuhKufdOjl8kr6ZeAbdORFpEP_KmPCS2lxxBYPjjekIaAw12NqdrVb4R5TbWTfsTGL8q1jrZgEhg0h67p71MuPq2y6tSUhOIDfKR73ZAXTft-aMY058OU-l1fU6pClJS72rfKUawTIfA42tYTET6A0p3qHpuEPTjp0mhZCsqHuiPv9aTV90_x1Iw_GkLXHTyU_PO8c7xjtR4hl0gWvwKSj9SoXkabuAvKheh7AyKw5spr7k63yILeJyPCAAyPfKs39Ru4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
چوامنی تا سال 2031 با رئال مادرید تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/99111" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=JpNosWpeFCxYTHk8HHCNWEC3jyRn5AAWzKtHWgpBvouQR0YNBTnJoOIcGW9y7ufijLhvz7R3J0Ez0DchCRe8o-Gfl0tP-xU-6odWZhSHlOmb0HA-AjVc_gnd2AlCTrQxtMjFAfzOmDbD29xAxJIs0qof4WjiJFnArL2gZZ07Y9mq-7yuIBMBf3dw3A-K_K19k_-CAO3tbXac-BAYWRrjR3QZQRrBA8Pj_vFlD1QTDW0z-xtn7qcHu2WNYJM-7ZWJ-o1ZnQ6PWON5v1tIMPCWZ-p2O1EtAFmcLihdPj_wVOHMjzQ5etDInRM8btE0tQ_JhuZj0B6G_y1X2646TeQqkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=JpNosWpeFCxYTHk8HHCNWEC3jyRn5AAWzKtHWgpBvouQR0YNBTnJoOIcGW9y7ufijLhvz7R3J0Ez0DchCRe8o-Gfl0tP-xU-6odWZhSHlOmb0HA-AjVc_gnd2AlCTrQxtMjFAfzOmDbD29xAxJIs0qof4WjiJFnArL2gZZ07Y9mq-7yuIBMBf3dw3A-K_K19k_-CAO3tbXac-BAYWRrjR3QZQRrBA8Pj_vFlD1QTDW0z-xtn7qcHu2WNYJM-7ZWJ-o1ZnQ6PWON5v1tIMPCWZ-p2O1EtAFmcLihdPj_wVOHMjzQ5etDInRM8btE0tQ_JhuZj0B6G_y1X2646TeQqkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات متعدد به جنوب از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/99110" target="_blank">📅 00:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=JAt63_Y_63XderMzyd8UrYJompoL7rLOQg8OcpKVn02TfChpLBSfDEZUUgL1Oqm33KeLUi6Pm22Tg8GHAU0EFQ2s6gXH4_NoV9d-V2zqP6NSDNGhLmHowixXYNXzKOkPe2Zdfn5UkC112ZqFfwljVOAuociSV4NlehEoya_HDyWRxm0u3r5OC5Y0PNlhgADMZD3If5N7tOR0revszkNd5GdmbVzNbeTkJclUAm_dOOtiH1z7ayPbzQARceqetXdsTFirU3AwcOTy-hdQEbBrzB0Cf-tALlL96mhVi6L5is56HtKWY9J2ya6RgMrIKunen_1U7kYHL8qABUdlK9lToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=JAt63_Y_63XderMzyd8UrYJompoL7rLOQg8OcpKVn02TfChpLBSfDEZUUgL1Oqm33KeLUi6Pm22Tg8GHAU0EFQ2s6gXH4_NoV9d-V2zqP6NSDNGhLmHowixXYNXzKOkPe2Zdfn5UkC112ZqFfwljVOAuociSV4NlehEoya_HDyWRxm0u3r5OC5Y0PNlhgADMZD3If5N7tOR0revszkNd5GdmbVzNbeTkJclUAm_dOOtiH1z7ayPbzQARceqetXdsTFirU3AwcOTy-hdQEbBrzB0Cf-tALlL96mhVi6L5is56HtKWY9J2ya6RgMrIKunen_1U7kYHL8qABUdlK9lToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نیروگاه اتمی بوشهر هدف قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/99109" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
ایرنا: در پی حملات امشب برق بعضی مناطق چابهار قطع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/99108" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
ایرنا: در پی حملات امشب برق بعضی مناطق چابهار قطع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/99107" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
بیانیه سنتکام؛ فرماندهی مرکزی ایالات متحده:
‼️
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، حملات بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند. ایالات متحده، ایران را مسئول اقدامات تجاوزکارانه اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/99106" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=ksldxW4dPOp80aO_zSoKihOv-1xPk0kKtlpk4yKs_gOWamiGEACjvKmwznqjQ2MUAeMGrAIpEhgZZPSuxyUa91KeZwCkP1e4h4S6Gk8eQlKs7lq5qW6A5nlpgUhBMEmMv7X_KlpsMvz566Fvrtn6PC6UKM2R_4lBlNVUp_1ZOFpO2CvajcWWzMd87IWNMSohf6R6JDIYQoAZnZsKSyUAs67Y0B7r_SDCCzKHfFKXOd0R5_Sr3zVSCKAEq3ksm91zcGu5WbtOEULk0e9iJ-T-O8WCRYI7mjDU3aaYlbkwb05L8yxObnOC0WnShW-H1T4d2d4Jld3d6aGgsBNIUStRSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=ksldxW4dPOp80aO_zSoKihOv-1xPk0kKtlpk4yKs_gOWamiGEACjvKmwznqjQ2MUAeMGrAIpEhgZZPSuxyUa91KeZwCkP1e4h4S6Gk8eQlKs7lq5qW6A5nlpgUhBMEmMv7X_KlpsMvz566Fvrtn6PC6UKM2R_4lBlNVUp_1ZOFpO2CvajcWWzMd87IWNMSohf6R6JDIYQoAZnZsKSyUAs67Y0B7r_SDCCzKHfFKXOd0R5_Sr3zVSCKAEq3ksm91zcGu5WbtOEULk0e9iJ-T-O8WCRYI7mjDU3aaYlbkwb05L8yxObnOC0WnShW-H1T4d2d4Jld3d6aGgsBNIUStRSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/99105" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99104">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
موج جدید حملات آمریکا به جنوب کشور آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99104" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99103">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
موج جدید حملات آمریکا به جنوب کشور آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/99103" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99102">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpCzMdVA8EWB7663braKpcGaaP7naQott8BR3qhTJJeifh8tDkQl3HwAnmvoEry3BhTWaGFe_Q-cRArEIcDPPg2KEl-8eOGpDhgji0xzmfIIE5tx9j_13GEeC-me0f_RQFJqwDDIuNU_ftGRaJV1ImLgKJIH_gkobOxoC1o0EhJXkA0i3KpcB9rpqrFkdj12DDbuWWhIowXcoUQqPl6-t1_nFHL9dWuyzm9elC5MnolksemwoARQBo663Uy-8bZGobB73A0FC4Fpv22Tiy9KG8Or-PKvuAZabgQPSD2q9qcxd2LwnGSD9rNhhDc2mRjR9maB5Br-VF7TmQvryq3KkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنژ پوستکوغلو:
چه سال اول، چه دوم یا سوم باشد، تمریناتم را تا قهرمانی ادامه خواهم داد.
میخواهم امسال با باشگاه النصر بهترین باشم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/99102" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99101">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2cb709e88.mp4?token=F5fCSNXtIobIEajYWUhHDbSLjbJG9WMMOeGvBRN5VwsvS6WqwYVYC1a2E7yHD5wR83JqZrYswisCtS_tXjWVnMLh_Dl-_xQCoz_aTI1H4HmZ5ZtMrCo-aoKGXTFuEiitI3JC2iZF8lMoK_JP-wlp4T07IDKv3lR4CsZ0g5rOKxOdvN3CvNjLNT83oOzeidvOzN1o7Ln1Rl7Ct3m9zL56hVMp8u9fep6zGFuJBsSPzd1VmKTb_DqOK62cNUdAqaKAqeQ9vLiwtE39XxgJXWWN95NQujz3057v-tNwCJ-xH5vjra8_LstbESPvIV8enwjzbCUcIj2t1MyssC34makVLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2cb709e88.mp4?token=F5fCSNXtIobIEajYWUhHDbSLjbJG9WMMOeGvBRN5VwsvS6WqwYVYC1a2E7yHD5wR83JqZrYswisCtS_tXjWVnMLh_Dl-_xQCoz_aTI1H4HmZ5ZtMrCo-aoKGXTFuEiitI3JC2iZF8lMoK_JP-wlp4T07IDKv3lR4CsZ0g5rOKxOdvN3CvNjLNT83oOzeidvOzN1o7Ln1Rl7Ct3m9zL56hVMp8u9fep6zGFuJBsSPzd1VmKTb_DqOK62cNUdAqaKAqeQ9vLiwtE39XxgJXWWN95NQujz3057v-tNwCJ-xH5vjra8_LstbESPvIV8enwjzbCUcIj2t1MyssC34makVLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چی شده که برنده توپ طلا اینقدر با ما احساس راحتی میکنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/99101" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99100">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UECkmi1NJ2fS1_CyIXVi-RT6U5JqCJhtG10NwcByRNa4rQuky2r26PrRx-FQkGp9lZmAJ3hOnd8m4hYSb2nSzzi__s1nVY8LrJI4cFaDl0W2Ta4mwgZWMPE37DDFLb_MuZbK9J56tFC8D6LCl0Xi03ogsHC8mMRvySNQ-1qoz29i_5bC5nPBubNjYGbw8VxE0tSsVcSxv78cFGuVfXKXb6rHak6AU_l15mSsfRYPMQ1zJj1CKH2Nz05tVZdkEjDYImZ1e5Wx2k9v6Gh8oOr86dYW80CniiXQfBEabySY8mh4fVtKwZDTXTUf5RiNskWm8C0_4F3KqT8YuVefBxUU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاستین بیبر بین دو نیمه فینال جام جهانی قراره اجرا داشته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99100" target="_blank">📅 23:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99099">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_jNYl1E6T8mBUSEj0IXvMPgNTcrpsi6cBbNP10is-GJKe5WQ37dOnKo4NoUX9SUdnQFxiBvQY0o9ZT4Y-Q3r_meWLlHK-E4HgndUCVO72BNPdhbrRlbbFDeGUtpfoQIi6bPDFWMPhjx5w8mcOxAJ1EospR_1ikyWykbJ5m0hRt2SffvgSSbXNS_Rdq12QBvnD20NvCCAajRWeUI-GrM1vgZ-3Tr7pEY-zptsJupBXcwvMlGi8rb9jzRsZqIq7pR_a-VuFW5fEuJWB5AAH7BHnNNk7ecZomgFSfn0ks_bgJ36nBwOrOcIZ0QASE_Sb1cklq493TGHgIZ60CR8Xu1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رافا مارکز به عنوان سرمربی مکزیک به جای خاویر آگیره انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/99099" target="_blank">📅 22:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99098">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR9wKhU33jrldD37F6BDpL253LMeG-1kP-xbw0Db3fQqXMKOON2fbDN7lPgwIEaWuB2hyTT365zBEXyEk8v0j0gX18-qOcVd1kG7xMWp1QwcE22nrD3lq8LzcsOjyuPd8QwiqlhHfGfJ_yD-qrVq7AYkwPERZ0Uwse8DLjcvk5KYQhzSIofT1iDxRIyKTHih_YIkzg60X812S4-iS3aNPEj7vntr_qSwoyOlEHPYaNBvgFv8eeP01kHjZqM1JioVSazkr4kM67fQk_Ne-NPQ21339FKLJQmbqcwQmtK4vd5c_0B8rLPzU5ctL9hcjMD4ORCXcP1SdUGXYuQ-4heaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلسته آماریا بار دیگر به کیلیان امباپه حمله کرد :
"این حروم‌زاده فرانسوی نیست."
سلام و احوالپرسی یک رسم همیشگیه؛ صبح بخیر، عصر بخیر... این یه سنت پاراگوئه‌یه. چیزی که ما رو عصبانی کرد این بود که وقتی اورلاندو گیل این پسر جوون، با نهایت احترام و فروتنی دستش رو برای دست دادن به سمت امباپه دراز کرد این حروم‌زاده نه‌تنها دستش رو رد کرد، بلکه سرش داد هم کشید.
این رفتار، رفتار یک فرانسوی نیست؛ یک فرانسوی واقعی هیچ‌وقت همچین کاری نمی‌کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99098" target="_blank">📅 22:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99097">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRq1WBCvQFPARYVoaz76dz0MBO0Z6EMtTl8G4oxbgB4idNxRVn6eUJtubQZcckBbfPRoITKjspYiRkEh7czIioEB2XaU1VhfeJ_SSqvsqJBAHbIbFPm6OPR_dh92VHUXBPuYI7b4Pcgv2f2oa8edO-Jy8dPjwQZrSZRP9q4Jgm_S2K8Djn-TbbV1sH55oXxbKWNoPNu5EE6Eo_WyDDAt6303WfWbkk5grgjBri_G90ZRUqpCpyfF6mWHKNbMAlWSyZ_8d6YztqOGzUuoSyVkLLo6zsEpeApMhCric1bvegr-11bPiG4Rcv75kCZ6PyGLLs5JF8eYFAsx_wWZrSjv3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در چنین روزی در سال 1990، آلمان با بردن آرژانتین برای سومین بار در تاریخ خودش، قهرمان جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99097" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99096">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC-AB-nCn4cn6WJF90GoV-AI6_r1vW_PmU54PZ4p4Fj8ROmA0lzN4bU9zD4wFMTqLvqhH1PKnRKY3sSaYJchzkQTKj5OI2JTfNnsXSkhiyHCDAEXe4tOyaAP6-W5Z2UaLdlDpfLHzm6dLs8Tlm_fhSMzXMpeQLxUx7Zl8NLGD4V4GNBWNMHjEVYxC6y77_Laa6zXViBRiG2_g-fymImKM06RYs60qTRhX6o_Eq2sm4aeJHWVYDB20wxD1H83mN7NEwfPoGYbA4N3uZNAiQIC5Z9Oop3lzJqQCzdKDAFWGMW8p7TW_D10gna0OoeNfTh5vun_qWyx8uk71DWOq3VX7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
شانس بردن ۱۱ جایزه ۴۵میلیون تومانی داری
فکر می‌کنی از بقیه سریع‌تری؟
😉
⚽️
وارد این چالش شو و
کارت فوتبالی اختصاصی
خودتو بساز
⏳
فقط ۴۵ ثانیه
وقت داری؛ سریع جواب بده، امتیاز بگیر
و ببین
سرعتت شبیه کدوم فوتبالیت و ماشینه
👇
👈
شروع بازی
👉</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99096" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99095">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3rOQ15k849MsC7Rrj-c_eX4ozKcR_TYKGw8u3H-_bCzl20PA5X60i38qNkAXXlf3-rH1Pv4Rg_H2vpPb084ZptCu8x1vyJjTH78qH3oSPzH-nyhB675du040dRAfwych6hyEZrTfxnHm_UBf3qfnuTv65o53bAuxzogceID7ZkMrI37Io2_iM3sLgV7GhYDXsZol1GXh10bfukqFr0hJojkQ5CRGgjnQ2gvWctPbeUBbgp5lS0nPh66CaytB7-EbM-dzCUmWqWgx2tBxtwS7TCp7gdm6_uVNNyXYb5QNrVCJQVLC1IVHzZqVeQ4-tiHjZWcpKhWoKd8wvJH5xJpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
فران گارسیا رسما به رئال بتیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99095" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99094">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm17WxRlT_06coXtfiySHDOFHc2QGQwCNV8WCEVjiULFE_G1hYFS9TOaSPVQmu-GwYE5efHSgean3VA9y-MxjsDWbL8vqWJ_IVXcl9ahO1BanSE4d6pKQJEPuwjnd8wnCphziS9PkNMQsypzHZyKEoWVCla6_2AJatGMO_TjuDapyfwXAqq7pdlC5lLw7G88LLT2kpwPCC3OhHYgoeQat-TgVqsXauWDZgurhyuA71_70369teygaVMfydVs9RhP3wPk4jACQJLq_3VBHuzjxOFAiA92bTPIDAZcvIOS8EBkWmAfjrzURLv-_2I-ZhHLkle9GyM6tY7QI37goccbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هوادار یونایتد رو که یادتون نرفته؟ هنوزم بعد 634 روز منتظره تا من‌یونایتد، 5 تا برد متوالی بدست بیاره تا کله رو بتراشه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99094" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99093">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv63Z50OJaG7oIdwNwCNLliYt9c7YV8bl7e1s7XOfFhnVdBGQ__HxakOCglBryGngF1bPvQec2L6_Okpt8BFyXLqdWAfHe3Z7poLnZekCF00sP0CJuXeWvT6jxCknVht3jak2kPbjCM2ZKglCrmCiW5iIWfmySo6VZpxlWVe1TZWgConlB9_jouZdAvJtbK18vwQjOe5nBP9stVu2g9cj3TCnSm-84ymSEFc9BNJTlmEJLGN9EH0xJO5mcZ_JD6Ml-vKOOYoSoKbyfVLPIR8mNCOen0cyXTQMYZQFLIf3iQFShYTMRJrSgcWAWONvbDdAWcoGq0WnQYdWgvaxEjIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ژرژ ژسوس رسما سرمربی تیم پرتغال شد.
🔻
ژرژ ژسوس رهبری پروژه لیگ ملت‌ها، یورو ۲۰۲۸ و جام جهانی بعدی را بر عهده خواهد داشت. او این فصل به همراه کریستیانو رونالدو در النصر قهرمان لیگ برتر عربستان شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99093" target="_blank">📅 21:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99088">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwnWtawvf9g-xfO35-banavz_LpBc3d8Uj0VRLBDN_aSZTq5yrZdNH_dKqPWyP6G6AKWojD0UvYem6iyH-PyTzc3ENnSR8ThxyJUrlcxokObV5sdTjU6q8sNYXY6fNAt4KHPeBySqHpOTB0xAF8Qt7HbIjrojnN7FZLpi5VUbCvOutvqtShA0Ff10FqkMEgHA0KXADU_hZt0Gf72-Pbd5u7FVSdzPcVpWY6YlSIGE3XbGoP-XnGrUy5jWHrILL7sd4PBbg0T3WKWvOlyEpVM_xBLbwxrLGPRtAzRPAWx8-FK0ljY7UrNHLX77ndc2W0QBS7p_Z8ga54zsapdrPnZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLSg39Wgk5oFdGKxCH9ifqF841LQEyAMQMHqRl5IRlAITAMNw7qYaQnvdBZ7TsXLzEq0cjH1QRKsqKAsk9Iuo4QAqbH1PA35eTXvehB2hPj99jhLXdik_MKgdW8F3WrqwWp14KzzV8xYYtEPhRWudT0oau2m24Iu_OVdm8CX9eC1uD_c_XkgOI7UxG-KCRsM9errIXl4CaFsErOYhEBHl7mWQIuNvLisupdeDwR7zQVm5ZMTorx63JtS1MXr2_4Jk2PuU4tZv-aHUWOtD6M0fYd7Hq5zkOKMucOQoeh5JgoksshsjDw-Ap2tR40G5pAHQ9onRQiTcVtyjjNQ8XB2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8byck5qxRDSeKtFgSY1c7VbnNB9tF-8Do-cE_ewheLtL_MvW4OhOiBqtQqOmO37W3SseeEuz_Nh3kbdGSU0VnJY1zGjsHZzmlZuW79hQnHwLEB2xqYAraR1-yjLYLd81E6GCvvcewv4EJHnCYwdtv6OkqBkTMI5Ukj8mwC5_mbTgVhwr_FC276H8Fy35yPAZRRFwlcPcSRxn0NXiIdKbaOgoaE8Cbwwu9QW3VdMEqU8nz7VqIUnjOfG8yj1kVnPwvMs7-OYfcn38uvZI9FaEQhiJnRamur2dziZp8KuxjjsBd7yX0YZ0KyWNPEY9DxUgyTLig5Tpr4jX7F0tdoiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axYActrO5jPlXawram3fgEaMe1gopKsMyQGq9BH_z1TbSuQRPMlG-phPyX8qHloOJG2iyPOzeo5dzswnAJMmy8NRf7fR71wpVgHbI1PHwMYEBJcYs3DWrP7uhaMKg2GGdMDMvF3FEFtupi7FlulBUM6VtoIH_SJFMQtT2N_LmkrBUNZ8DBDlBhg1YM8RiPTy01fWrIhWZQk8Q-lDKUFnNsYVLWJ75Q4Zc3Dun0w4mMLatv7rEf7P5XHp3KXzOi1hC4I3PhAWMHZbaADIyaOvR9AxrRNdON-eFpe_F7qbr2fCesKJAOSo3erxr-86Ut3IyONU-VNUCmOUZI8uPsaa8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDtFzkq0vXWXeOYNz5jY-LMYOAOygVHAoTQwDf7j5G263cTKs0ZdRW30GpIOqZuNz6XRiXWf1E5g3ExP7wQDTzdDIP7WYikJ5Vovf9EoTys-m1fmjp1P4XyVfuacawb4EO8AAbpvWQKQgjnT_7GHJ1hhd_j2Z2oxws-Jz7yZZfZRVwA8XIitqVi7kRFb2rGKBLy_39Uwine249ApgTNmOccRJYJ5KszJUGRqZHYjmzWVJ2tdKTR28Sj0JbD_RGTq3E1nJvHoKhdYcBE5ZPiuLjr6Nrimclt6Iwwhjshdt3lJBuIgt6OJf-yL3zZj0WFGQfkfP5hpPLzibHUi_OHseg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
والپیپر آوردم براتون :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99088" target="_blank">📅 21:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99087">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_NA3pIlOhp9CzP4E8UWb83sb6XkPfsdp_Y2_dOASgfquN1-kizupdrWS_cjdh2R_oF3720HbyB5M6zmclP_QDYe9Y5BQFiqhcEVghAEzG-WPhmI-QBLJEalGcvXuMZqfPnYvc9XdtpWQkAb2gUUJoUgKMtoeaaE9cdnJ73m2u5aFAp_k0412fzFEUGOZ_1UniQ3v55ZTinN-VgbkwL-gMbtKpob9Uusvwnud1xs37HdTpVrJlGTsink1Vysgo5f-wr0bzLHH4EWoqMqF2xRRmxW4Lk-vOKQG0n3vgj1bFHkYoer5kyTyPZ2Ja0XDXUuaKGew4u0nndESdfg9k0g6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوووووری
؛ رسانه‌ UOL برزیل: نیمار احتمال بسیار زیاد بزودی از فوتبال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99087" target="_blank">📅 21:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99086">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG9wBplnFA-xW9zeirYZR4nCEsZrdKAj4S542Wx9nJ5b330eD4fAsngN7APUQAxAcYoZfZ1xC8glP1vGpu649SzIWQziBPbtFMB9SLolHwoT3da438obHFN9NkBquL-MEeAOG2vqebxN97LKbfSYufLgw1reDJi5dPWYp1HwOE2uprzxs0JTF0qTygPMD_H-wPsinNRrgQAtdJ_6h9D87ANGD4nVXBFkz0hy8kopwmhwc4YZJHEM2VllhjGsZWRRShT_VXn91ESK7Gdi2Y6XJUoKujwqHHoFN_BHIxCAIZPgwg8OizG-6l7ejHlclrOPq_kRjBBpMgevPpUfgnwhJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین میتونه بدون بازی با حتی یک تیم از ۱۰ تیم برتر رنکینگ فیفا به نیمه‌نهایی جام جهانی برسه
‼️
🔺
علاوه بر اون اگه آرژانتین سوئیس رو شکست بده و نروژ هم انگلیس رو شکست بده، آرژانتین میتونه با شکست دادن نروژ در نیمه‌نهایی بدون اینکه با ۱۰ تیم برتر رنکینگ فیفا بازی کنه به فینال جام جهانی برسه.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99086" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99085">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXWjQJdfhoPUn1PRlsXRg8qaBD0Ch3zu0RUHW3TPvROT1dGIgGpuPAgV0ul6TmdoihW4d1WPXq7AQTdvuYwthsUn0j0nXU6GygvewyNdjBR2yk7p4mlRD4XSgwhpBKj0DvEkQ0olUJahDdTB2ZFvhbbsrPl83sFAyx-RdYh1v_Z0kAoOPP8RkEaCLO0NLBdJERodCR2tWSYWxqBBuOImuAEPTqgq-2QHa8zpM_zEHYPIJYHTjR3c8kGjCttYvgalwHEEKKJyQyIbUACDjPZM0qc5i5WYCeQF-7aIavac22CWgTmLk1NTxXSn9CgdrudA_6Mlf3M_8A83pYPA4th0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
؛ فنرباغچه ترکیه با مارسی به توافق نهایی برای جذب گرینوود رسید تا این بازیکن را از تیم اتلتیکومادرید هایجک کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99085" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99084">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8kd1sm4Lf2isZfKfhbpA9inMqBJohnQqAg6xho4jRyOZJzLlPeEf8NHM0KOCpv-3ckdI3S1C9gTBupU7dpPDsUEYoKtR2afU06AZMNTUjZOBCpexspjhAfctTcOJxs6Vpi04vt7RHl8_vieDnFsTbEKN52h1awazwYidECdRF5GeXMHr2ppKcoaa4x-p9xHIvntMCCqDnKxuICGEWQll5YCgFJS7AnTjtDErpWdrYYzdcGoseRTuQArVJPBRPQiGcxr0_rwLXqlAQa65ZN7XLDnj73GlMau7UxLqxFmybBPl9kO5wMHr4lSLpwsTdbxmxr3murM7al2viCfF_T2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی خودت را ثبت کن!
🇲🇦
مراکش
🆚
🇫🇷
فرانسه
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇲🇦
مراکش یا
🇫🇷
فرانسه؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99084" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99083">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6UGNGRcFR7Ku7eQQqbr5f6fG0jmHr7T_bcJpjV86ASL7s47pC9jjgUOWppgw6CjRTsFFXClKiauNtsgE4D0qiFocV-A4ABfEAsQpy3KAA3--RoylvLH3MAgZ_5Z_suihQyi4c9AS2_Z-NEWXZwyqHsjf9ZoEn35jZMlBpWRU00SpQShj_hFwH6qIZcpjxa_jwzRzH20HJ5jZs9jiNdc2RhiwYHtmMLXn45zIBUazr_zomfJWST_6D_-yBUhycoYj0tyysArJWAPTB4YBfBrpw_8sBkqk3kpQhjO17q6O3foxcQpqUjq8n2LuYhjZJjDm5c2Kh39hrxX158LncSuyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁳󠁣󠁴󠁿
#فوری
؛ روبرتو مارتینز سرمربی اخراجی پرتغال گزینه اصلی هدایت تیم‌ملی اسکاتلند است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99083" target="_blank">📅 20:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99082">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncAt7DPwu-zTqypIjfG2Zb7d767b52Wbr9CqfEOLTBXg0FKWEjA16gabetqleKBgw-GDSZDLx4vunI1Ly8PHOHGu7OtWwbrn7LTclZbRhklVSOjGaXWzDml1thF8OXjCwh-2URbGTd4zAicQL14_mxOOLLilouMxDvGK3wSEdZN1H1K32lOdCRC-3P_12MvhejoMnUQ_cQIVgVRpQV6Bz4dOwlOdKmkilYF1LzAiqMrEa1kSpwv09Ov-yk0GFmiS824HzUO3Tuy25_mHkhpPrJK7QTd7GY_pbqy969FguGIKHMRAbahMFs7axdLz0KuogHhkRCrXxHLtLIdfIcCbrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
الکساندر نوبل دروازه‌بان بایرن‌مونیخ با عقد قراردادی به بشیکتاش ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99082" target="_blank">📅 20:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99081">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeAgy4NLUP5QNYp0fy-5U3-CEoXXKqGJNZSbsaf89VOS7JhipsUmUh0Hw4A4uPlrUllbQhZpM68l20ZbmwZiH2YmCVfdS4w9v4gmYXJzIp0pEbloFL7eZc6UJlC5qqUoWYOANtb1DuBMd5RioOF9OyrnDFOzEAGdQryCgz7ZMsZ5McDrq5iTRmICYp0ii1la8UpgbZEyrAXfXfvTNj_DdORU5ait4VDyqbTUK4ai2N1iLrnqbkMv3CRX9tdunzyR2IIl91GNzkeGwY6cgF9-56NgcW5gvhsfGwxNzUaQ6_k3BE1gpSZR4Ao9r34HXa8PwiyQyHqFPqclUAhI3qdRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی به رودری اعلام کرده که ستون اصلی تیم در فصول آینده است و هیچ قصدی برای فروش ستاره خود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99081" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99080">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ ادعای برخی رسانه‌های انگلیسی: رافائل لیائو برای پیوستن به تاتنهام به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99080" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99079">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXVnbzVywZwRVg-leJsFdgRzicDsNXwK7h1D7VGrDzvMAPYPE4jU3SmtOFLYA-polU5pBdeoMFrJglJ7PtmwISvG0gryr1tuC7DdJcRhogVm0CWtjBf8zoPtvDbr4ZQrUjjzHb3U4A_yuNR2eZVtHRXZDdtKb1yDjCugcHBAMgDglXtKCC5SZa8GfNpAPGWdNMgG1EGappE9OnWPVohcIEa8Yppt6oqzoYoxrwcSC0LS4xXqU2_5IKotjHniavgteWER0X8jn70aCAYgVt2S_IPcOyw4jPJag3-xkFdipYlMUa3u6Sc-MCOVn-GjiDLj-1hJTh4q7uiJjUxtzvao-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتاین:
برونو گیمارش از تمایل خود برای انتقال به آرسنال به مدیران نیوکاسل گفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99079" target="_blank">📅 20:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99078">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18362372c.mp4?token=uE2oKfoOEgNf2bJrdVKmLv62qSc7j2x5_RHrm23eVexBgixZ8gkhutu7VCuU5Y-haX9srJXHjhzYO6yeMRkYEuwToo3sq-unLU50FRWNqlKcSFLhbGjIdMoHxaDMQ2TjD-_JjjhRq3FJY97aWob8pPhPinYi0URFNmiIUIUKnrl9jQMNx6izbRzlb8XpQTFJ4z1yypIS-IiIv1zySMi7QUvZlw-Vj2ArU_0_BkOXof6Yg5iQUPN3pJiOBuEk5qo6fH0q7B8DuMYu4LozcHsFjRMtf0WUtSmIVN24YhIoGKooqFkEiREnrL3YNHUQzTVTdiMvCdNiJe6T7eGX-mdGkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18362372c.mp4?token=uE2oKfoOEgNf2bJrdVKmLv62qSc7j2x5_RHrm23eVexBgixZ8gkhutu7VCuU5Y-haX9srJXHjhzYO6yeMRkYEuwToo3sq-unLU50FRWNqlKcSFLhbGjIdMoHxaDMQ2TjD-_JjjhRq3FJY97aWob8pPhPinYi0URFNmiIUIUKnrl9jQMNx6izbRzlb8XpQTFJ4z1yypIS-IiIv1zySMi7QUvZlw-Vj2ArU_0_BkOXof6Yg5iQUPN3pJiOBuEk5qo6fH0q7B8DuMYu4LozcHsFjRMtf0WUtSmIVN24YhIoGKooqFkEiREnrL3YNHUQzTVTdiMvCdNiJe6T7eGX-mdGkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این چه سمی بود خدایا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99078" target="_blank">📅 20:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99077">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1sEPwZE4IkV48gGc57Gx1XXwolJMWpxYk9_ermwXUOqwKs-gazyvqam9P-12eRJ927pxDcqs1iza7AIJmkqA2zD8SPmnwkABi1YM-leYmKScX590DN8cMT0KpdJTzzEpueY9pslm7VWoge4j8OvmrCmjQHlkNtuGpOgBnGpMYJ-pRvD51ZOOu_0xx3cBs4Cb36iFxW9CKtZGpYMVZEKx6o9J6k5y5Q5qF_o_rQCmF9ecGjuAnpJwe62FiHy7TqFENSmKTFC9B41zsMQBPxy_HtCvKXRly9x2dlyHVn8FkjfdYiwqsQl4Swrw88w3yAQDnpOAdF5zJwKluE_nFV08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
🗞
روزنامه رکورد پرتغال
: ژرژ ژسوس در تماس با CR7 اعلام کرده که مایل است به حضور این بازیکن در تیم‌ملی پرتغال ادامه دهد مگر اینکه خود این بازیکن تصمیم دیگری برای آینده‌اش بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99077" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99076">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2n-6MpTislo6Vmnqkzc7a72of2b94CwbVdEuHLFIFcO_XGj7UJwk2azA0tgoGgaGqDr9bBIgUXBXGe-7yIoc_XAWZ9jZppaDzEvP86VAxMvc7Mbnr1Y5mQ2wL-eRZmvMT3n5g5jiqD-AahXoE4bs3GLS9cPLmL52d6J1LjAGE0v2fVb6l_c66PM_1QlNxDplngKdM4MJ6BFkfsXYK0EhtJYHd4IWYH2hWxFwakR2C1yzgGB7vUSSalcrfAaUD8LBb51-zdcPnoqJhjqeSdUiPFqEDHnQsru3gvQW_0pLJmSngTLxiKvZ3Ne13wQzNg975Q2_Usqhlq5-0EF6-h-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گلهای دقیقه اخری جام جهانی تا این لحظه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99076" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99075">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf2OmHvLbPT_VBzSfG3mXeLtNaLoVZdW5pefWrVhziJROArtwS6ZV5rJfVwLxm5xUU-9nwTWltCzhVP5p31wUAqWf3K8k3HvVMUI8Ru0mFrrkTUYmVT0XTSqHdio4U1MNnBQ99N7sfh08DYQdVZRMxAkGwrB3o187KnsdmAFzSSXUIoowgPNldLEVcWD5ilOZa9Z0FgArBVGTIrpAyjaJ2k6X7kOZmPMwVNjPwFKH5GzdwLCvW4GPwS-c3Av_blkAMa1Pfxo1bHAiYLuELThhv_fILFc22hDeHUwuysWPOvLWAThIIEHPouwQP6c-g7-F5eBFVsgZEn-HayZwkBtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا: موضع اتلتیکو مادرید هیچ تغییری نکرده.
❌
❗️
اتلتیکو قصد ندارد به جولیان آلوارز اجازه دهد به باشگاه رویایی‌اش منتقل شود. این موضوع چند هفته پیش به خود آلوارز اطلاع داده شده بود. اتلتیکو تاکید دارد که تغییر موضع در این پرونده غیرممکن است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99075" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99074">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99074" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99073">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kfy2oeOaiv8O3oQfVsBkDw5vU8JMO8-cc9cpeCkxSq7smMggN-DYLWfowfyhAxvOciQC-Xobg6KpgsbQuqJxSFFjuGYxbwbkXpmfJ6A0M0ZgZieSXHBVBnb5HPquDjGR88PuAN7Rc7wxgNgDuW87Xyyu_UzRjI_kKC55c0YFUh5UnW5CrXurRqTGLsQQ7V_ac9wz85tXW1iBmNXAiMrxgqlKghE5GX62-0xbX1eSxRpjwZo92ZPuQEzpV1jPmXwGhWpOKsFVQ7dK4EAAXd4tGXBhJVwswY-RzaBphLqM3oJFC2PIq63JIXqCJSKqbQvvffXQgfx3UNh8c9MdVebmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99073" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99072">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745dbc9962.mp4?token=cJlcv0V6FlwPToDTfqteis0AH6ihtWX3RaA_pldqCEy0E5TgLmQoPepSB_VGvLdYnSCUEqjqyRaRS3qMnvOvkjbxKm7uIIkqCvPyYP6IkWOybj8tmRRDeUf-dJgPNY1FpTLodcYFW86aO9sZxY6J6y9c5wvOpEUFLZzMy0nrBpXMCRZf7AYdksLQuncfTtN8AvOY46GnA8iKkUJFt7qPjhTAOKWKylQS88YFHbSgxuQjh1akGzgATMYQo-RqTjMupnb_zodehtXgNWBUllTFHYQkdfa4J3mXNV4aXcUNtOvSrKHaa484ryUGBMliYCN2r7EjbNcnYwlzaELrSDAdZJ27FRkP6YJUOUB3C_8UA1W_62MoNNqy-AT7HisvpfoiCYxtKTqpkfH-EMOfuF0hRwKw89tEi1v5l4LeJ5wdQvnJM5VslTuKLcwikYEPaT1UEezCipc-O0zGoyNiRrZTWTZtITZA_ssOW8nA_pIa94WSvwz__-pirvrk8JVcjH1-xCgQdZT82ob-LDv50xyrsivfDcZvnnzGxUktHMtEbF8ispUAR9I6sCtgJNa7SRdPa5qv4XOs8xjvnqWVN0i6JaGP_Do0X0kdxsKc-JscrzYOLMy8K7F-wW0z_Q2mZHQSMxQUbYGV7AJa4BvHmNF1Sc80o4vcb_FeQrRJmTpzyrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745dbc9962.mp4?token=cJlcv0V6FlwPToDTfqteis0AH6ihtWX3RaA_pldqCEy0E5TgLmQoPepSB_VGvLdYnSCUEqjqyRaRS3qMnvOvkjbxKm7uIIkqCvPyYP6IkWOybj8tmRRDeUf-dJgPNY1FpTLodcYFW86aO9sZxY6J6y9c5wvOpEUFLZzMy0nrBpXMCRZf7AYdksLQuncfTtN8AvOY46GnA8iKkUJFt7qPjhTAOKWKylQS88YFHbSgxuQjh1akGzgATMYQo-RqTjMupnb_zodehtXgNWBUllTFHYQkdfa4J3mXNV4aXcUNtOvSrKHaa484ryUGBMliYCN2r7EjbNcnYwlzaELrSDAdZJ27FRkP6YJUOUB3C_8UA1W_62MoNNqy-AT7HisvpfoiCYxtKTqpkfH-EMOfuF0hRwKw89tEi1v5l4LeJ5wdQvnJM5VslTuKLcwikYEPaT1UEezCipc-O0zGoyNiRrZTWTZtITZA_ssOW8nA_pIa94WSvwz__-pirvrk8JVcjH1-xCgQdZT82ob-LDv50xyrsivfDcZvnnzGxUktHMtEbF8ispUAR9I6sCtgJNa7SRdPa5qv4XOs8xjvnqWVN0i6JaGP_Do0X0kdxsKc-JscrzYOLMy8K7F-wW0z_Q2mZHQSMxQUbYGV7AJa4BvHmNF1Sc80o4vcb_FeQrRJmTpzyrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
تاریخچه تعداد یازده بازیکن در فوتبال از کجا شکل گرفته؟ ویدیو جالبیه ببینید حتما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99072" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99071">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
نکته کنکوری: اگه بازیکنای یک‌کارته در یکچهارم کارت دومشون رو بگیرن از بازی در نیمه‌نهایی محروم میشن. اگر کارت دوم رو نگیرن، تمام کارتها بعد از این مرحله پاک میشن و تیم‌ها تر و تمیز میرسن نیمه‌نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99071" target="_blank">📅 19:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99070">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIsy1g4qn8or1fOEydsBMeNw-lZ-BAcPFWu021M4ZgCe_3YUTLVrXKZ5J70B320W745OfI9zGSP6Lpf5dtIkV2tiLXEQ4aySu_r7M0QEKhJ0Tcq30PDNh95UM9lYy8JlOuLqUsEvCrpnTPINyAXc-R8QXqTXhOBHLfyfX7jAY5MbzTnwVR87GiVdEPHZcbo5oouDQaF4yVKa1_VEgR2YvKGfG5MlCmMDIL6vwuY0W7hs9F6VACA-t80vRd5_Kpk8GXEJaCVSkcr6ifu6Lqmnz0IWWC3fl8jEahT-LD078D7cio_eUmv_DkOhJrfu_5KqMmzT3U-rOGryEkbF0ug4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نکته کنکوری: اگه بازیکنای یک‌کارته در یکچهارم کارت دومشون رو بگیرن از بازی در نیمه‌نهایی محروم میشن. اگر کارت دوم رو نگیرن، تمام کارتها بعد از این مرحله پاک میشن و تیم‌ها تر و تمیز میرسن نیمه‌نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99070" target="_blank">📅 19:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99066">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNWy2W3ent0yjSxELyulz1tRyx8zuF7W9JYPV-phA5TaNA-WA7ICjg1oYpzJ-v_4Wc-8bYbo1j8y9iLQU-0BYBLfb9IwOxVh-CSKRD8WaqijvAEuZOucPL3GgKPCyEySvUj24vzb-GpK2vY8vff_l2ReWv4DqskrGtz2pkVdnSZxd2MDszNcUfQpVz5OU0tkCT7XrmkxaOcmRa9DNzqjX5nz1qM0g7F274gnSN1jVemTK8pgdW-YhouB6Ws9FOAx7wrMfpA8kzyZS7OnSjsZ2PZd1xyrb40D2jV8HDgr-_U_PrEUmE7RG23u_cMxLhFESNQ0PxZZJk3axZANiRHlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrnMDS01_vtT1fDbPYmlC-VkHXQU1rdx6QvU-PCZoelKXc_z85pVTjo8sQLA_VXpQRTcLJOWEOOaAAexfiF9dyg9aO-i6KQMUAP5pEFOZCxChuehqoWPlOX7kPtqLlq7Wxs3sFFhAL90MQ66Dy7InDzvAN5heHhzGShVIk-7d3e7XTt3YXkoQ8paS7Xa--KBvyIQ2zCCdZQ2MfKiGgw_2QDkIzPy7tKOcbb-8n2cRX_jiwU58XrSvLqvPi7hPbLSYxbt9sGqGApcoxuOIutnaEKvzfH_GV-SULU5ZlCRnaD5hSC-8DmlRXllNimzHthbc-EOUe8Su2H_iToeVTqmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXTQMNJdfAOzmiNgsm12ce-pIIo_OGpRt5fGfrv0J6XOnn-diyXXBkX-yRsshxSvD4Dv9XylTS7lvXcbdzNgPqna2n8GWbHUcID7Pc_2Q28jzalAe4-GW1WPPbwG7SNs5fV4Xgvq4U2DUhw1urAPJL1Z2u20vMpwreigkwDw_ucosL9B-S18iAsUi7ukbvpNydQS8p-tNnbX66WDN39gSGlHrAY445UKvj7RS4YBaHmTF8mFVHkciJ6QmYb60hgWYhrb_UCd_ZzsuHyx_p3vOz06ZFghyyFJgsywrEkYibk0EtYowf7iOCI_YtE8vfQnRBnklqPz3Pd_zL4mnufKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6a39ZbesRc2rokTM2zPwh8Y8Y9WyToHk7HRgGEvi5qYaVbso1QIBTLBnTEWK7TvoQJayyY-G0aMVgvPBktUe5PqwEYU50w9MivdTlT2TwjWdXJCn0D6J8_jbQHVQpHiT7GJhc-EYPG1pZ24PTOZI9U5yuTQVxfLYibaTxwubURCQik4MewxLCpLcqjF2j1qrrTWS-2Yuuv4LDFO4-AaviWZVUoOhMBXkzQFg6-JyvD0EmauhWGk-Vv_2frs9kByjx6OuJXtYTiAO9WFRTo1k2fhoXyXNupnAuPgr2k8vYdQYyrxYN_2LJa1bvVWNh4bz57P4TWzC0koIpZITJqFvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇧🇪
همسر جذاب کوین‌دیبروینه در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99066" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99063">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANIfffM6F_wMsJz2FygCS-Yt5t41mduXux8ssCX3MmHkxmx6QCa-3TJo5GWGgdgWzZt8bQqJN24jXKLvLMURf_EwGHzEbA-byyJ5uo1W0qnpKIUj0kDqnT4uyr7kMmcxYg9zgHs4K6BnYDj7rirp6ngxZHUomo3FQ6p1Gfj9hIzRByb-3NfSIdfVPd4ylCbYyv8WLw6wa1anHPVRT9t97j2IMCXsdDZk5Q39rFvbybZYLhhkpp6SdZQrWi5DfFaKcS0n-cwllMA01841zRRo54ntnqKiaZQxk3ul6Fsfi6AmXXZSAocS8IaPomnEYS9d7oJP4KkQr7TA6jontkxYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIU_4wCXEZZsALIYUunvbIdOg1rNmmmxUgAgnoIEvMqbGSUC1ZN4JniEw20PCdGA5gZ93jBW6Ut_qq4NHCJI9i9Ud_RnfoqX297LcuAVpFwNy51kOCIjl_xRWOKqH80ndbDtHkBfMXhpsyQ_Qo0JgFpYO2J5VtMv99dujkJGH-IWyrH2Wdd8PIbs6t_AJEG6yW9IcyaS5vZpKPaDOgRsTmBHOhGKeylF21eJ7O1cqmu8lDzBlObvfWicsyB_8K7ZSrBJTZ6w-xfroEapfVdgjZGeNWZF2axOAvB82AdwquHSKRw5uAbPiS8t8Akx7UvDccbgeicotucrYsRM3l2a4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXst3YRr9u4Hggy6DBIYFrLSkad3K_dwfrSBvq8Ajj8ayca4C6AIMw6ooh4O1iSEfl734wUBnuD0y9KoCMz_KXXWhOIwTWJN8WbBSW6XVClfI5TA7oetlmX6xoGfzA9hzSLJuy6PcRRdM6S2_X9SV2KQqVJv6lKpLF2nZtzJbid0jjP_9zmm00IvtohNBiim7NSiktpn9geNsvjemHTeSr23Q_GI5UZu9dwiliF8fr5eAvWg52nauuyI9USjLU0oj7XYr2rCKOTbHEcc0XDxFRz64vhN3SeTQ6e0U_tuU2XOvE7fWcEVQJp5oCd_twqQrrwbOWJUVDvjZjvjV4wrjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسپانیا قهرمان جام‌جهانی بشه چه چیزاییو قراره تجربه کنیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99063" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99062">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fafdc23a54.mp4?token=mHItQPihh6l5h9ANvDmFCIh3rsyxtzRPESBM6Ng4aEkcRv0LRpKgBiGmWtRokNG_J4cskIduc1g78xifivDD7K6o_mVDH05XDbPIlaQqncYNGh1HF9-KjFqHXnt0IwaHoZmUxGaqGfRz3C2aMDgMUwIgOHSJqcKlV3K40iLYGrnC5Fy5Ghqa1mU4WmIvtmcQQudVwZvE6-y_kKlvPMRYQwSeDEPjgGfIGVu8lqOUSFgkPxppf4ULMUASJ4smKdjWHRdeLeZSCUJkaHKENrwPI-4N4NemtLSpxZHBbYekftx5myqH11kgJicUbR2_er3D_t5b4SsGKqkgNxqOSewIYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fafdc23a54.mp4?token=mHItQPihh6l5h9ANvDmFCIh3rsyxtzRPESBM6Ng4aEkcRv0LRpKgBiGmWtRokNG_J4cskIduc1g78xifivDD7K6o_mVDH05XDbPIlaQqncYNGh1HF9-KjFqHXnt0IwaHoZmUxGaqGfRz3C2aMDgMUwIgOHSJqcKlV3K40iLYGrnC5Fy5Ghqa1mU4WmIvtmcQQudVwZvE6-y_kKlvPMRYQwSeDEPjgGfIGVu8lqOUSFgkPxppf4ULMUASJ4smKdjWHRdeLeZSCUJkaHKENrwPI-4N4NemtLSpxZHBbYekftx5myqH11kgJicUbR2_er3D_t5b4SsGKqkgNxqOSewIYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
صحبت‌های جالب علیرضا فغانی درباره چگونگی آشنایی و ازدواج با همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99062" target="_blank">📅 19:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99056">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mvQG9iRTC6TSbZIo3VcCZQ7EufqjFFl4sLk506oVzgMDNRiVT526VcesZkwYLYrIswCjSHdAEkJ94y_qtl2J0qy5d_GxcNAGf61r_h0Jj_huqKzhLULQzwVH6_-vXrJPZl8YBLT6JZ_eYgBqF5aWiwFLQNkfsnar-Iibmq1U17AXkFPaGs-Dodi-EHOdrSUvZ4gn_dN101mkJjGSFLWvJCDqJq8kxvBGpa9Tc90eUzFpYWBtAp_YnM4zG5iT86hqPHBjUxXurMfiVuIMDj4s7WF4U2tq4QQ6e0ZUg5G3R7vdpsBQLTYstHvn9XZ7pn-nHIqEIIY4XIcgPM50v-9RzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jC_UBkX5BlIpgm7yMsybrjndxHfLme8V3awW4Wq7iscbVvnEfWHWkRfgKWdgq-Rmxs20bokvAvryOOjO2BtURRVOzfhseo2XCGHH1MUvyv92jlgmVmh2GelHsf2tSatCqwODdrtSY6zYMStrxI9dhu0_rsUCI7YuzafgMXTLFw9t0cVluOrcl6hjPUsLOCFR1qM0-fITFZA4g60WJB_ojMdom1oCfE6pSPAVPrrJApxCRvmaX48umXj8B-sK2bEmzfDfm6H6m6ISHUrnYmZpeuMj36x06gDxChCqpq1w5fjaDQvxF7ZyHiP99ib_Bw7zdh6CXuWPzBrpq287ap2BMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZt0K6wtvJy7TL3Ova87rhMacisD7bK0UrHXDV3qKM_ClGyP70T2fmGCng83ddgoDTUFmjgSGwtoRnjF3r0Bz50glfxeGsxaE0569Gsmy0nx1B2cay1FPZUEoCn2kV1npECrwZWcGDnLk0HsNbDxz0_M7gl-g1-r4vYRfHNrIlkUU7C7U-KeOQRa3cZEnZIgtCzk82TnPGoZb_ga4lOWqc4S_pUPUGenBnvUdFMu5ZaSH-XpxUPfI5J020yu-orhB-6UOzjP_DWDWaWtJ9MlHUzrybTzE3Cm1CocZYCgPcrlMAdn17jGhqFpcahr9e9nHFa2dpEo6nvzR6r7HH1BqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mp_eZss8S2jVmk4tnXvUNWOzKFs1qQAkMpejHOxQ2N1EsR9eh30QDIR-72LIoQE8H6YSl69cwMR7AkaAfVr86LF9jOj67P94XOo3qgHiXfFMioy83NQ_ovVPzgjELfoOqzXDwh2Xho4gi59bE7YSjqxz5DRnapbcQ0s6FvHGzn9AZafU5ccnZSX76lOFZoKnPnEUfqe0ogKGf1XJM4Locg-ml1dzv7N-EuJ94iAooUj5k1ALGbznSBp5Z0oUB21fmQUdqpXD3M9tYijOL-VO_6qbcD3t0BEoNb4OHmdlJh0PWWqR0STUw_zKomA_wzT0uuTgQlikztdfXbp1HkPQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceXrSUBgAJVoY6QY4ElcOeLrq6IS_eOke1ONynowKZagtEf0VM_YQi0lpQdKao9dSfZj2YnU9JlnSfiIZWdNnQN2eckI_ThPt3yF4KWN3Eeo5gE4n8sqnAffsqvdTMBl3QVhlLoMSzFKR24mLXQJJnR18O0PozzAsZ8uPWZoQRQgy-SgUPYG1GwQgY_FxsJdAamNoMaqbsG5OiTkWAc6GpthXi0DZxVGfC-guRMtzolLq6pOt9YD118_9d8oZKRdbGKtdDaqItr7jk9sxlF5V2EGFXj_a7GiqYuqflNFyuR8GwFpxnL6bP0TbgzEKiyqiNvBKuD_idGhYA_yq9TxGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
همسر باردار فابیان‌رویز ستاره اسپانیا در محل برگزاری بازی با پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99056" target="_blank">📅 18:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99055">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sshz5xZxAKH832zoUWf7pNM_EfPWapiH_FHkqo75RlfRkf8W-pTawaQowOSXDgTMJvHyryx4Db_d8-LslytZniu5bedYBRteJyYYQFXVsk4-tMBvYwa3qM3TquSamAUk5XpwIdL86vqlDIj2VKKig5qN3nwkNJby1xGqBf3XzbX3CSOP774Nai61mOQVV0b09GFMzguDF746nV4s1_RSsU7QYIbj7zuhgI_qecgv285x-No_RClq7LbTjqSLkOo5cXOWBGDrEn60z3dIVZ_FG3PyFW-YAi_Brw4Ama4a63Ak74yCR_7bGgaGJzn0qASrtj94qmT5IcoQCgeccRIEjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رامون آلواز:
اورلین شوامنی با اطمینان 100 درصدی در فصل آینده در رئال مادرید باقی خواهد ماند و از این تیم جدا نخواهد شد. او به منچستریونایتد نخواهد پیوست، این موضوع به پایان رسیده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99055" target="_blank">📅 18:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99054">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe9I3n8AHzDYauif6nwsJ6LybBt7aTYf81AIk6w-8J0VLygY7R5VVsP9XcENZm3GHiaVVy1rx6Oe_6yQQqwdixddrq6nCehwQ-eGvMOEKKpQPtHvW7u2iOWlzLoZzXj8xR5zHZJiRsEYCTx14vH5NEjkdZp3wtoAx85xRqxYKKHMwzy77b8LHHv5XA6bKrDY-E8zyK3Jyw_DDakau4hhDW2V82S5Rwl5SV_sh26AasW-yo6gWrnlGyrEa4glSi2uFUgI14S-eCHU4wRihXZOAJ4NNT4M_AVUQlj5J8_0hj91Qqv2Qd2zUiZD1WYWtE122HKKMdA3QEo7RNbAAzr93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🎙️
دشان در مورد انتخاب داور آرژانتینی بازی فرداشب با مراکش
:
"انتخاباتی وجود دارد و ما باید با آن کنار بیاییم. من به داوران اعتماد دارم. امیدوارم داور ما به اندازه آقای لیتکسر در بازی آرژانتین و مصر، کارآمد باشد. رقیب ما مراکش است، نه داور."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99054" target="_blank">📅 18:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99053">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRh8LKSw7ZCPijBmdVhsFTYtojHaafBotc_AT1DqgAagtVQVM4VeH2HGCwfBgDQYAq6eawUiVTBnJKQZUgLqog5rt65c34O8DHtQ0nhkiXYnSRkvT_yV4G39yG-EM-iJ-h8TcYSlNdpBF0qjT6kN3MdhCZqBLEYyxjnjFax_c9T595gpbUOwySM2Nn0h333b2FSXwsvaQyYU9gOrMYsIwU6I9GuIsjF74eqLyBkz53peX9Dlphr14eHGYueU0h0RXSfh9C2GmBHpVZS3glPbgcR80jduv8A3_Yhsbkm0Ps7Fu5KIs5tduSuSeP-6y4BW0QAGt_B6l4orIC3Muz5gOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
عملکرد لیونل‌مسی در ۹ بازی اخیر جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99053" target="_blank">📅 18:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99052">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhH_2hRo4PUZE-F8Q8W1HdqTUyIOks6e5DI6ry2TcJtJUEdJJ5cqU3qdEP_jk8OJDI-03i1pcnNlD-cTjNWZpuNFQCo8eYlJ6B84VxQsRzLybReyZRfyB_Gfa2RFSFuQNFnSLHRGXDUxi9aGRN275fiM05Ovtg9TIf_gHwjBWSeQAGyT4GXRl9z_EVOq9z0N9yP0GqOJBboA60X40cNRB10lBOPGARDMEwPz7HATrQVq0QdeaZXmoSXeB33kiCfWcnwy9mT5OwDXFwkS176wauzTM6ylLRXvflkyhbcWrbuc7UyfuQzl1S2oQElwxF7L4TmKoly8BrWTFfvFPTBm8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇬
ابراهیم حسن مربی تیم‌ملی مصر: هدف فیفا برنده شدن توپ‌طلا توسط لیونل‌مسی است درحالی که همگان می‌دانند لیگ‌آمریکا را نهایتا ۳ نفر تماشا کنند و اصلا سطح فنی خوبی ندارد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99052" target="_blank">📅 17:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99051">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e25d8855.mp4?token=m-QjOaxgeO2HE797E0W4f8XQe7m2C8xHcNILZRbkhzfHcx4ZQtxYP__grv-_mhEStXp-qztzUeuzMXKwjkDUlFdiGnrl5RtX1i1Y2KQjEuBMTtbpca-BWQsQoQxkstoz7Kq-cf6qnt2WZXaB3-ljuqhPLWzvXASGk0BqP9CCodvWX--8GHKNONWccXutXitzG6qV5GjzJGhG8mnOtgFT9fhkHdeDnTaFcr3XnixPkuPtcrNbE40RwiupWU5N03F3mBcYurzrfAsPb5BGS1Civseb3ab0G_4BzLnUqeLOSN16B0zkjvKbNmqRdvLdnFwnbDBHVgRrT7zumabD3Yar7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e25d8855.mp4?token=m-QjOaxgeO2HE797E0W4f8XQe7m2C8xHcNILZRbkhzfHcx4ZQtxYP__grv-_mhEStXp-qztzUeuzMXKwjkDUlFdiGnrl5RtX1i1Y2KQjEuBMTtbpca-BWQsQoQxkstoz7Kq-cf6qnt2WZXaB3-ljuqhPLWzvXASGk0BqP9CCodvWX--8GHKNONWccXutXitzG6qV5GjzJGhG8mnOtgFT9fhkHdeDnTaFcr3XnixPkuPtcrNbE40RwiupWU5N03F3mBcYurzrfAsPb5BGS1Civseb3ab0G_4BzLnUqeLOSN16B0zkjvKbNmqRdvLdnFwnbDBHVgRrT7zumabD3Yar7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🇦🇷
صدای وحشتناک شادی مردم در خیابونای شهر بوئنوس‌آیرس آرژانتین بعد گلزنی لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99051" target="_blank">📅 17:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99050">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44599c3a8a.mp4?token=tx7eH-1D9MyvBzRkDH6VrJK0XfycvZQ4vLSHza8l3IZe4g1600E9hqTrJKEpiKkjlXggwSdSHe_M1y-yX5a7mTiC0eeOs_lh8ATu8qMznuVh1YL1_dArhx3rUwGrHwYQtXNXFHOZ8NTjUxoBE3sP1_WH7mS1-w_k5-20BhEK0mDFlnFjXX7glIAPyjYwIbGSatQRWBbu9r5eeCbNve-ZLN5vvav_B-j5Cfx3bu6u9skOnsfDMexMBo6s35h4OPqCdSYVhHcw1Cym-tbwpghqsnkc3o84rrBB-0_khLONUxOLqm_rM-mC0RdP0xkcdvEhrfBEZy3i_craZ_icqlnx2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44599c3a8a.mp4?token=tx7eH-1D9MyvBzRkDH6VrJK0XfycvZQ4vLSHza8l3IZe4g1600E9hqTrJKEpiKkjlXggwSdSHe_M1y-yX5a7mTiC0eeOs_lh8ATu8qMznuVh1YL1_dArhx3rUwGrHwYQtXNXFHOZ8NTjUxoBE3sP1_WH7mS1-w_k5-20BhEK0mDFlnFjXX7glIAPyjYwIbGSatQRWBbu9r5eeCbNve-ZLN5vvav_B-j5Cfx3bu6u9skOnsfDMexMBo6s35h4OPqCdSYVhHcw1Cym-tbwpghqsnkc3o84rrBB-0_khLONUxOLqm_rM-mC0RdP0xkcdvEhrfBEZy3i_craZ_icqlnx2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
آغوش گرم‌ لائوتارو و همسرش بعد بازی دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99050" target="_blank">📅 17:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99049">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
؛ ترامپ: پیت‌ هگست از ایده ترور مقامات ایرانی در مراسم تشییع علی خامنه‌ای استقبال کرد. ممکن است دستور یک حمله تمام عیار به ایران صادر شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/99049" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99048">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b20b4ab0.mp4?token=vqkOfKpsEOVvgi02bXGwCdPDXgPop69cP4ZKwX_tIrmA04IrW-T87P59lVhxlraK5elVVD6P7Vk-8enzS4imnNqt8y-Mt05rLAg78rB0HmHzrTknQlgVn80bD273poIftqd2ERpEvlXlUvD5nYeH4j8jJUPzpQ2lDV4KE3Xe-AiG3Fl5ah-9TIliNHf7jL4vX0rdLPio3oGZhUEDFlk1dq4fmWoIAV8BvVG6WUHhnfZFCVAZqdx_y0usZxPmVqOTBbW7kPLxQur_d6U7w4owb-3lUSHDlZNpaAMvIBoa-pWWaJrphYimCzgy2wtoV8VGnRNJ-H8MT2_AmidN1tpfwr7ZtVx5iejiqC8pGlF5xBHJ_7ytKYAVZ5W81z0eqAOMg82EIxO1iFRQ-p6emDi0E7lb-UhnOafMJ3pN3c6sTd4y9g2m5t-x2WqmBw_YTJxWSOa6J-4TtI3qiUdjqyuhNQzXVtPBoZbki37UnTZY6zw_ZMiAV9Ad4V8HfGEGeYu8xv3VYkRAbVus6Mvwcj00MvKgA7q_o0UdDiwHm3RxGOrREgN_jXFl_dJ_0YadMERBc2_ZGQl-8QS6PBDIm0nfYhlFT4lkj0ApQNeW61DvF7pghRKap0IoFpqA4PNTEZ1_nJFMA1w7X7svMFqHGSHVAN-0pKe7lVM6V2l-N6HDNv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b20b4ab0.mp4?token=vqkOfKpsEOVvgi02bXGwCdPDXgPop69cP4ZKwX_tIrmA04IrW-T87P59lVhxlraK5elVVD6P7Vk-8enzS4imnNqt8y-Mt05rLAg78rB0HmHzrTknQlgVn80bD273poIftqd2ERpEvlXlUvD5nYeH4j8jJUPzpQ2lDV4KE3Xe-AiG3Fl5ah-9TIliNHf7jL4vX0rdLPio3oGZhUEDFlk1dq4fmWoIAV8BvVG6WUHhnfZFCVAZqdx_y0usZxPmVqOTBbW7kPLxQur_d6U7w4owb-3lUSHDlZNpaAMvIBoa-pWWaJrphYimCzgy2wtoV8VGnRNJ-H8MT2_AmidN1tpfwr7ZtVx5iejiqC8pGlF5xBHJ_7ytKYAVZ5W81z0eqAOMg82EIxO1iFRQ-p6emDi0E7lb-UhnOafMJ3pN3c6sTd4y9g2m5t-x2WqmBw_YTJxWSOa6J-4TtI3qiUdjqyuhNQzXVtPBoZbki37UnTZY6zw_ZMiAV9Ad4V8HfGEGeYu8xv3VYkRAbVus6Mvwcj00MvKgA7q_o0UdDiwHm3RxGOrREgN_jXFl_dJ_0YadMERBc2_ZGQl-8QS6PBDIm0nfYhlFT4lkj0ApQNeW61DvF7pghRKap0IoFpqA4PNTEZ1_nJFMA1w7X7svMFqHGSHVAN-0pKe7lVM6V2l-N6HDNv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نمایی از نیمکت مصر در صحنه دریافت گل‌سوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/99048" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99047">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1dea537f8.mp4?token=hzubVd8nc4rIifkmhr19bHlwV68TjCYDNRT7_mQteTW9gG5bJAYhfATYsf1h4gEdSDMOswBC06IdhmFA-g486CU5gedRxu7Jo11blx21lE3Hx-EqvU1mmzfyRC2z8nPeqZFzaUolS4wHp2Z8hX8g6G-QFjZaWv_NOATF9y73ELK7xyCPoCbbu8xgWj81x4zy_XrDeXw2s0GLwhvrRLAi3T4QTM9lMMW-0w686WWes7Vnkj5AdzMDr7F8PVU4YX0ieVK8I6lhniFgLBW5nb0qYjGJtwKIDDHMOROvB2Q5x8scRY0KVZjtdjnT1FNSEL9jgVBXWW80F9jEvYzAB9Tfyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1dea537f8.mp4?token=hzubVd8nc4rIifkmhr19bHlwV68TjCYDNRT7_mQteTW9gG5bJAYhfATYsf1h4gEdSDMOswBC06IdhmFA-g486CU5gedRxu7Jo11blx21lE3Hx-EqvU1mmzfyRC2z8nPeqZFzaUolS4wHp2Z8hX8g6G-QFjZaWv_NOATF9y73ELK7xyCPoCbbu8xgWj81x4zy_XrDeXw2s0GLwhvrRLAi3T4QTM9lMMW-0w686WWes7Vnkj5AdzMDr7F8PVU4YX0ieVK8I6lhniFgLBW5nb0qYjGJtwKIDDHMOROvB2Q5x8scRY0KVZjtdjnT1FNSEL9jgVBXWW80F9jEvYzAB9Tfyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🔥
آنالیز‌ گل‌سوم آرژانتین مقابل مصر؛ چه ضد حمله وحشیانه‌ای زدن و انزو چه کاری کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/99047" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99045">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-sVRO9we0tC_NXjIZNTbIRoA8LjGjASHq-4tgAxIwxlmwwLflgbvY_7tlnybx8dsJfvWghCe1H1cpr5tuvDxZ77vFJ53KOQ3VjU_sprNG0xNuvFo7rSZu78dd3CWVlurZkUi8ZbW8YJ8l4B-aPgBZEnewpzV0H6BnZiCxeTXNkCy-WXYjlXoANO66dtYEnF8_Mv9F89czFe0i711c49OJWKITLIVdVJQlJ2ueoVy4Tsuv5A08PornrT-ODHYs9w5yM0kQqY2fYjIfvx4y68nu7q7hyrQ5QhBRv7pHEobee0ZOEELTYwkcYf1gD7Rgz7bLaGhGVlcDt0no8gCXpxTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AcrbDYZTf-MXEgP4hlu4AOKnZyoHkl9NSR8ivus4OgqhkCsjuyEOVVwWgS7Tn7aFx4ISIVko6uiumbR-tU4gM5HagNySdEYbl37k6HKgxLAVyoVAJBPvOCxgxdkhHtsRovaHtjZv0lNkR-hE3KegIRx_wFPyiVgB2jNeFxSNtxAeWwQ7Pnc02jeSyG7CxeWIkNr3-lj6SboIjB6UW112KaNGz3R-Cevu-w07_4WQeRLppy9HXmY9f131nFc9H11F7w8iAMotLfN-BsMcvIrsFtXlJDaS_3oh9s0cqukJhrGZnnhARoW4Khcm46rEIJp7Gfb1SqzY9js4JmYWJyN00w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بازدید روبن‌ آموریم از موزه افتخارات میلان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/99045" target="_blank">📅 16:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99044">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔥
🇦🇷
هیجان بالای گزارشگر تلویزیون آرژانتین در صحنه گلزنی مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99044" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
