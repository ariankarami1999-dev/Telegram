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
<img src="https://cdn4.telesco.pe/file/gJQfLE1ObTYugu6coPDEtmI4T1wK2lBUZ2fCCR0nfpWzrVIID7RAWMTxZaIVfAUzFXGTjeAi_PVDYTfST4MzvAuA5Y4eA061t7PcWUOAacqYLx1WB-bdpgfN53anaD6stYg-JGLk0wI43ly0Tm7CVlxLHCwo2BHjyjJ3Yaoa4HFM2OZUn2MZnJFvZ2-w4BDUgVlGDWoDxI5UjV3AhUhQMMtv4EjetPDAfPfgGFNNX60yn9Rq9LbNouwRBg_3_1dNJCWAuGJoU7mfDPaUC644Er_YPdxbFkWOcWLNi2RHXwqcyvyVmEgI7RUoKZA-ZgdmB_gPIM8dwGqHaOIPffyCUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 194K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 08:43:32</div>
<hr>

<div class="tg-post" id="msg-67484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/67484" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67483">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fYpHLO-yAwtIhIUFUbUe2GZkQwoAupbym5_pwAtsHmFEPyMU0zIqwk69Ck7mGlbvs___hmXLNcyEX3rrZgeIjJPzFgsnWkajOnNtwNXnUzW_aoPkx-EDcFn4pdbNPLXp6HFqgyMX2S3VEx1Rs7aHQimtKM6eg8QmQUr1JTn5zFHbADZVj681usel4U_q9mHL9UX4NGhsZK3SlLYsgABuLujNhc6hRLkrFCqr6coR8ahIzrF3iSaf-WPkFrgsXlh-MCwew4TiEU3ZwrGFsubHztAvvypxGQe-YH5Ytlf9Paq_GG6ksViD_F8ClFastev9XE-NMygaY7kogn1F296pgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/67483" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67482">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHN-axy_0M-fYRbHglWa6AGJoKfJWo4p4txMru6biCUWeEiOGMZWXGNor2jVV-oJv9sTw8wNDQMSJj4FZ-OttPNJvWnz8SwBgIbjZZpP8ocEfwkkQ-VeXeJuO5J4pNNTJ3oyahRibDGIt3Miqhzr1fW2Xdrmv192H6vJNeZeQSywgesxGBZ9DbIoEZQQuytYWrvT2IA2DP_Qaj4AWxSF8Au1D-YjTAYF-QZebofjxp0k5wSlduRjDfp9vIRf1DI0UiVdgwJDmUcSODv3H_E9Bxo1kS5G8TlZNbekqvSb6pyEF71lfozTzu1tTDdbWDuuLU7ifhj1bwtZo1b8NTyWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پسرا فحش میدی واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67482" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67481">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMGFHSHin1CWgMh90X7WZ2gopoYZeEMuQDot-9uKTRYm6EvHVBrFwmllr5cl5W6cpxka87sJa1QDzBlSROhZm-OBA3pf2Fospc_BxjRgw3XzGRukij2s7XB3XPz-BkvcUuvm1e1MQ96S8rO4cNxXFpPE05LYBS9syYX7yz8uZDaNSsDMJYImRerGJm3kmA22BAxH9zFqxXwIaf8Z6JZI4ZKdJpbtynaZgW9RYQgXP4VK8IWrx8t_nHPsgWta4OGEJiIoyFfsULOpAPGQkIq3KyGx1DUu3qInUk5kkn__r9pIpOLz9IP-74CMfY7QonUVSmAnfCbksVOGQY9BcjktEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداوسیما: وضعیت بندرعباس کاملا نرماله  @News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/67481" target="_blank">📅 02:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67480">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بنظر من زود تموم می‌شه</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67480" target="_blank">📅 02:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSor60</strong></div>
<div class="tg-text">به پسرا فحش میدی
واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/67479" target="_blank">📅 02:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEydeuJz_lPL6REKt6uG13r4OgVZ4WWn2JKgxhRfGCgZHnHP-63QGa5BC-1aTUl2HOYy9Me_lucUwW3C6xo2sNW4ioSTj9phQmQ0o_uVCU6AqrSlUIDi8Y_aM99S5VqXbIsojaFc8GtVWWa5XXO5VfozXBKw7d39fGZ-92hjN0pHy2PJezWd8kq7Xtc-yGLrpWm8X-mgwOqs8N7dHperln7-LVfblooEpU-Rlxq3T_PI1jGETR_pxezyt7uyei1z0CIgXnVkhXTK47_cdirJl96MMLs6c24BeqTmW7YRgeEEtcnxZsR5Id5FZOhxwqsTJJFJAnh_TvzATxKDsv4KkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اومدم بعد مدت‌ها، و تازه متوجه شدم این ادمینا تو دایرکت فقط جواب دخترارو می‌دادن متاسفانه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/67478" target="_blank">📅 02:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67477" target="_blank">📅 02:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67476">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67476" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67475" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67474">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67474" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67472">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=mRTzFErg6Esf6xWUDglLYAlnyMqEI8iXbzWLEn_-wQbfz-KvlFHZUq4curdYI2ddk_XpiYK88FnfteMkYBbHzGgygnPdTnMBtnPCZVQpN05bCtTiYFCSdsTR9zofWE4oFJulnHgAOp9yqvzVXCG42zLEZ9VzitvAjmSUzJuBjo4N11_MfGphEBRxHPyx90_xu3s09K5n-guaJlHJtMnVdl35-1ElrAj9C9jTja8NE-DibAZAWkVymlaAVcxypZJpZO4Grcy3WuuZI5BCAdeDQQz-MH5J4Cyhm5Dx26HWVUknmGWBfr6SVme1XfLcCKEKB8bOQ9D0R3DBG-2xuf4w6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=mRTzFErg6Esf6xWUDglLYAlnyMqEI8iXbzWLEn_-wQbfz-KvlFHZUq4curdYI2ddk_XpiYK88FnfteMkYBbHzGgygnPdTnMBtnPCZVQpN05bCtTiYFCSdsTR9zofWE4oFJulnHgAOp9yqvzVXCG42zLEZ9VzitvAjmSUzJuBjo4N11_MfGphEBRxHPyx90_xu3s09K5n-guaJlHJtMnVdl35-1ElrAj9C9jTja8NE-DibAZAWkVymlaAVcxypZJpZO4Grcy3WuuZI5BCAdeDQQz-MH5J4Cyhm5Dx26HWVUknmGWBfr6SVme1XfLcCKEKB8bOQ9D0R3DBG-2xuf4w6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67472" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67471">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
پرواز جنگنده های آمریکایی در نزدیکی بندرعباس در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67471" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67470">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
انفجار مجدد در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67470" target="_blank">📅 02:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67469">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEouIJbfPNLRVsoAiKGSUYyHBOyK1EXsq_nBT4rC4EJn_2quDINSKUr8akbVFS6CYXr5zuY6UAvZF4eaCZlyGIRvXTm7VtEnR4qas830QudmUMQCkIJov29fOPculs69HNtVwmYw0uW0jqkt0tHwvCEWsFwl3fuAa3KDMJE3fDZvZNokrrmp2NcwShYSJAIylW-k05P4QOoE4MJLrig2kpewjF3wHKzToouF8VaIhlb3n9JNjhhcGniu1NdHeo7DDsOT6ERf5Si8-EjKBQUricC9MZnyJQLKNafrtzOaF4H9N_sPTxnc-Vaoeg08khunqGaKKPzrX91K1wnXd6BIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
مقام ارشد آمریکایی به من گفت که حملات ارتش آمریکا امشب در ایران چهار یا پنج برابر گسترده‌تر و قدرتمندتر از حملات اخیری بود که حدود ده روز پیش انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67469" target="_blank">📅 02:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67468">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmQzLijl6-MWybeuasyOLJubHsI5xxwlyG4pM1bs_GD1DOl7kozm-gD00cv7XudprC-YJqhrXyEivzPEVXxesJePLur9o3gB7vZbax7O6FzLc7MX3B7_UC32eHjv4h9cFy21680veFtoIKWoeCrvVKaIFfaza4PlkQcP5EktdvetGS4PcAn10H1qbN0JelQyuE3OCHVvCXT0Ggnx6o28mKi9M84qxbO0R1S53QF_cEwcl6dhLvtlkztr0vLXjoVFmer2meu46m9F6ERBFdOz98Q0-uYmtbbrqd-hceyLFXWeEcjxOozrqrbyP5xsBF83b6tkiZaFfAZjF_jnq6uEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/67468" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67467">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
قطعی برق در کویت و مناطقی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67467" target="_blank">📅 02:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67466">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
انفجار مجدد در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67466" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67465">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=pHIL9-RLCAEwMpuO2SnW8G_CMFdAsGqz5r1thkaDisgsCHT3e8sKBi7rSp-KAZ1FoarGGwHFld3w7AGLp9dL4eofhf0wSDtiWKqWz8g-ciOywLGnktRlAPe87xrQHOPX_fGHFci-Efto7PTgKQ3dDduz3FsVFKfMnBaetsyQwLKegNQPn_llTEfv4Ui4SuNHEzuMoyBooejf-gv6YBy4Qc976HbzYMokCx6m6vEPyjv50vC8F69F4uVZzKpn3qB70vKSs9QFG7WzAzTnVjKNwupHt4QGEQwoFCZixDbHQ_IFPdK0EMHqAgTn8Y5lTlHpRxpTLI45cFIZChOxn979dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=pHIL9-RLCAEwMpuO2SnW8G_CMFdAsGqz5r1thkaDisgsCHT3e8sKBi7rSp-KAZ1FoarGGwHFld3w7AGLp9dL4eofhf0wSDtiWKqWz8g-ciOywLGnktRlAPe87xrQHOPX_fGHFci-Efto7PTgKQ3dDduz3FsVFKfMnBaetsyQwLKegNQPn_llTEfv4Ui4SuNHEzuMoyBooejf-gv6YBy4Qc976HbzYMokCx6m6vEPyjv50vC8F69F4uVZzKpn3qB70vKSs9QFG7WzAzTnVjKNwupHt4QGEQwoFCZixDbHQ_IFPdK0EMHqAgTn8Y5lTlHpRxpTLI45cFIZChOxn979dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67465" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67464">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHkPuOBvm2pcp4wvkDkR0AYEinFcPQy0dTzwElBzhzMQELX96htq4juR99ea78DGRG13l6OwlEX8BE6MOhsBbC6QYKXWlzGVMDCcxQ9OIZHB6FEIWEAl7emLzuxUYaKkc6UpvM4sbGuXrDdmQkF1jC1_Im_OoaT8-HZhLx3H_TAnNzwkjCy-8MtFuQDMRMdpaLthB2NanYlA2Xe15wBptm7vGPFSzNvkgc6pUdpW8iGOfVFl8aMeBNmKo3zUVV-ahnLLTc1tNdc3bjN6giKr-9XG79LoiHk2rwrwl8z78-4EpRQ5APZUaK5QqqWl_9vcH-SSIvrWzLA_54ugFzE86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابوالفضل ناصری، عضو فراکسیون مجلس:
آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67464" target="_blank">📅 01:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67463">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
کان نیوز :
در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67463" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67462">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=TzU4Dhs9tDD9oriaW9sclyELJI7dBjBHrbj4gb7m8ZcTUJ7fBN02Eh7qPbs-RVt2Dmnqxt1t3TEd5caFbpefjEJxpAD52burYL11x4ichrZn12ToqB-7Kfg_rE1oYVf33xr4-lTFTDGFTLvJK1TpLEAGRDHESWujwV1B-p6aLB-0D8c7yMtWyrm5hEnNvTt2DLnxTBn7sKr6g03zRHpoS14lkg-UpO0AxysXs82hBDz01e4Fk24Oo4aJ4LNObHh5dq6F_ETouDYgjOQ49SG9H-TJpACCGir1L48eh571Fri4tiHJTVgIrExySl9yxW8O4f4k1xqxqOkFGNjDqkPlwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=TzU4Dhs9tDD9oriaW9sclyELJI7dBjBHrbj4gb7m8ZcTUJ7fBN02Eh7qPbs-RVt2Dmnqxt1t3TEd5caFbpefjEJxpAD52burYL11x4ichrZn12ToqB-7Kfg_rE1oYVf33xr4-lTFTDGFTLvJK1TpLEAGRDHESWujwV1B-p6aLB-0D8c7yMtWyrm5hEnNvTt2DLnxTBn7sKr6g03zRHpoS14lkg-UpO0AxysXs82hBDz01e4Fk24Oo4aJ4LNObHh5dq6F_ETouDYgjOQ49SG9H-TJpACCGir1L48eh571Fri4tiHJTVgIrExySl9yxW8O4f4k1xqxqOkFGNjDqkPlwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید و آخرالزمانی ارتش آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67462" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67461">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=enYnH10M76f5W_U0Gn6w_rrxFazaKCyeyP2YNiMt2ZyZUxzCDqBkqY98sLfhuI4_anL-qzy2rM2fjOZtYSujmtt4p0VqigEzBqhbdE6osaktNps5p212NfFbJNbDAL7LSZgk4eWQTNqbevqoa0JMtrzwIjeufSAveff1YBiqHk-JB82NN6eQnJK1cxskmH2103BPFklApGe4Ppuz7qxNGGfA61FBhluLBB6Pw3pytuToC4KBwqyt-4_cdRVIbGedbQM2xpZxe4BKeQekQLQLj-ib48_Wx-1dpwysfAqCDl7noAX0ya-rrOwJcRJDVnsqUkA0sSA5j540JPEY7Emr3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=enYnH10M76f5W_U0Gn6w_rrxFazaKCyeyP2YNiMt2ZyZUxzCDqBkqY98sLfhuI4_anL-qzy2rM2fjOZtYSujmtt4p0VqigEzBqhbdE6osaktNps5p212NfFbJNbDAL7LSZgk4eWQTNqbevqoa0JMtrzwIjeufSAveff1YBiqHk-JB82NN6eQnJK1cxskmH2103BPFklApGe4Ppuz7qxNGGfA61FBhluLBB6Pw3pytuToC4KBwqyt-4_cdRVIbGedbQM2xpZxe4BKeQekQLQLj-ib48_Wx-1dpwysfAqCDl7noAX0ya-rrOwJcRJDVnsqUkA0sSA5j540JPEY7Emr3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67461" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67460">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در بندرعباس سیریک و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67460" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67459">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYHxXe4q32nEEucb8YbJHuGQ-uPPAlbEnnY77reWv45sIsCE2HGpGSlKxUgOjOjENk9xAs4d7_k5BADEzBADgc7KFAeXW4lu1jaz92kPx9ZDEc14tsq_KWBpgINNWEzNl-4_XFpfZ_62dyUv52esMnRJ-jnWrAyO_pe-C0s-b43amYBd-gtek0xX2a184ob_sc_IVvS92SA9_wAi_9_yH8xxGiAOJ98nyMl4Ir-5jP2Y97FXlDmIYaonkRPyrKS7HV-mWLSVBnUol5XG3Hrur_IXj4pxeBS9lBvokyZc4Yp1hoYxzegCg3Njr7wg7UwAcktjOSGR2YrOAHkFrytsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تحرکات فشرده هواپیماهای ترابری نظامی آمریکا در منطقه رصد شد که شامل برخاستن دو فروند هواپیمای C-17A از پایگاه موفق سلتی در اردن، یک هواپیمای C-17A دیگر از پایگاه ملک فیصل در اردن، علاوه بر یک هواپیمای C-17A از پایگاه شیخ عیسی در بحرین و یک هواپیمای C-5M در پایگاه Alhairates در پایگاه الحائراتس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67459" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67458">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761109e119.mp4?token=iZGm4XDNnABDicFxJwbX0whAOUhK23smyCYwoHV5MROjOSMV1dHgHpveNNm5Fn6MFPm_D1EgbpuhnOtzlpNBW9XgmaDJtLw2P4iPQFqsZ5-Juf8bsluegrNM0yka7rqS4dtxlMH__kd5fO4B1_dKGXs0nPiXWj8n1H7YXgb9be_CDmtnw7mK3znxCQvDW5M_cNoImB2Rs5BqSgx2R8KF_cxwJOwY29TL5QolB_mnPKqSWjjDsILly6kLm-CGv9z_dX70otGWsIqsCWfa4rXLku6L0DJzdVJlar5IYsp28D-AG1lEo9JzTNjzBYvUcaLJwWmUqBBrorxPps09nGk91A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761109e119.mp4?token=iZGm4XDNnABDicFxJwbX0whAOUhK23smyCYwoHV5MROjOSMV1dHgHpveNNm5Fn6MFPm_D1EgbpuhnOtzlpNBW9XgmaDJtLw2P4iPQFqsZ5-Juf8bsluegrNM0yka7rqS4dtxlMH__kd5fO4B1_dKGXs0nPiXWj8n1H7YXgb9be_CDmtnw7mK3znxCQvDW5M_cNoImB2Rs5BqSgx2R8KF_cxwJOwY29TL5QolB_mnPKqSWjjDsILly6kLm-CGv9z_dX70otGWsIqsCWfa4rXLku6L0DJzdVJlar5IYsp28D-AG1lEo9JzTNjzBYvUcaLJwWmUqBBrorxPps09nGk91A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بامداد چهارشنبه؛ بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67458" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67457">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=ZgSQ4A2a_rvIC41DZXCgz9gmkjLAuJpqlZYqH-Ou7xjHUyB40mqccAl7FDXV2YMszlGhfKrJ92tiJVns9cT0CcO32kdJL1H0wb25k3k-6ovVLgr1XFe3TQaBU-iIXMGwrzkEVMdUf-5842RtSBt0dHTH3hXIvhEs-DlkRBbllX1DkZb_yCCQMXVwtoPE2XktV3mVlEKgUX5UYsIgwLXAIzVBbjh-vV0rbHu8iF-YDMwBzoNvoHLccyVM6bV9t8RrNo42kscXl6nbmjY8ORCOnDIJgNsnYEOTBUeVY5xt5tY1YtGCYObkbW8VgEr4hbPIkNUcLYN0Iz332-mTTwgshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=ZgSQ4A2a_rvIC41DZXCgz9gmkjLAuJpqlZYqH-Ou7xjHUyB40mqccAl7FDXV2YMszlGhfKrJ92tiJVns9cT0CcO32kdJL1H0wb25k3k-6ovVLgr1XFe3TQaBU-iIXMGwrzkEVMdUf-5842RtSBt0dHTH3hXIvhEs-DlkRBbllX1DkZb_yCCQMXVwtoPE2XktV3mVlEKgUX5UYsIgwLXAIzVBbjh-vV0rbHu8iF-YDMwBzoNvoHLccyVM6bV9t8RrNo42kscXl6nbmjY8ORCOnDIJgNsnYEOTBUeVY5xt5tY1YtGCYObkbW8VgEr4hbPIkNUcLYN0Iz332-mTTwgshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما که نقض نمیکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67457" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67456">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=RsoZi3mmkET4Z-xShgv0QNAwP1GMRVjlsRZEN1xZ_oEJpdi11EsUl2RXwH42R0GQEkJHw-8Pdzi6EEvsrCA8rbeIuTy4Chv5qGQxM9TtFqQsipa7q6aUQz3eBq7S66EtcoddA75yzHxpUOAhffplR7XOC4rUVeqozPS-y9dqsLONgGHAvkf5wyIYP7oeTxxnC9WLw8pTCS8iIHeVXwp6SyrbMtOHXywRumIpEJetzcxuI7oWHds5EhDBKLoVdEga9mIozc4LCKonLUe8yBIwxKWGXsYYoJggz2JVT4WujCUztvnXgdRQdpC0KZjstOl22yZ8D7qVEDd_DIRZ98o9dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=RsoZi3mmkET4Z-xShgv0QNAwP1GMRVjlsRZEN1xZ_oEJpdi11EsUl2RXwH42R0GQEkJHw-8Pdzi6EEvsrCA8rbeIuTy4Chv5qGQxM9TtFqQsipa7q6aUQz3eBq7S66EtcoddA75yzHxpUOAhffplR7XOC4rUVeqozPS-y9dqsLONgGHAvkf5wyIYP7oeTxxnC9WLw8pTCS8iIHeVXwp6SyrbMtOHXywRumIpEJetzcxuI7oWHds5EhDBKLoVdEga9mIozc4LCKonLUe8yBIwxKWGXsYYoJggz2JVT4WujCUztvnXgdRQdpC0KZjstOl22yZ8D7qVEDd_DIRZ98o9dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بندر عباس دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67456" target="_blank">📅 01:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67455">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=UxnVaYkh1JQuFvQYmmxHX2fP9h4yTr-jgxGQfLMEHcCvLb-xR08MrndXftsbuIQyttakwry6OdDT26Q-th6ET8XUHde0zpEX4wf_-8UqtBw19eZg7VJIAxtrTOm5BAE9XATSgwAryPb7tJVGcdmqESLv6ZYBiXknsoo_JJABmdw9X1sOdYMjQ5LoJJC3QSTLFZf_uCKN2lc3NBAsCdV6Yv_pmPHs7BfLQgBiCEmWb3pP0NYsELeyR7EkaJqiZp48zLIRmum7gHONi6nfidxw-Q-tF71N42OMKyzlPM_U_x_teYN1hXh8PoHcy4jsZQ4tWbKtBS5WVAY7qU57XbbEnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=UxnVaYkh1JQuFvQYmmxHX2fP9h4yTr-jgxGQfLMEHcCvLb-xR08MrndXftsbuIQyttakwry6OdDT26Q-th6ET8XUHde0zpEX4wf_-8UqtBw19eZg7VJIAxtrTOm5BAE9XATSgwAryPb7tJVGcdmqESLv6ZYBiXknsoo_JJABmdw9X1sOdYMjQ5LoJJC3QSTLFZf_uCKN2lc3NBAsCdV6Yv_pmPHs7BfLQgBiCEmWb3pP0NYsELeyR7EkaJqiZp48zLIRmum7gHONi6nfidxw-Q-tF71N42OMKyzlPM_U_x_teYN1hXh8PoHcy4jsZQ4tWbKtBS5WVAY7qU57XbbEnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندرعباس دریابانی
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67455" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67454">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال:
کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67454" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67453">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=X1Fgzq--qdmyIGv3uLRmNxVXx9st9RL2WInJrbaok41Q0_9AulW_E4vUmMwc3_sEM4HLGxj60b-ShtB41ugigQ9IHC8xOVvgmaYZzBTBowquCzDkSVDbjbHRZbUanOYTwaJIpdNajvI3OVNskGXcRIsd5rPShXB2DOELxCX1Gaa8chG_a7J4aEXDDbkSTHEtNnDDAiHrCpbZudBq25NrjCOyZgCbp14j346DPm-DW934br_ajFAYcDlzl9MsM6rV4_-M-3b25seVrue5evZw0NcwrkZLIMvP3Up0Qhs-v6X0_4Mhdt2khLK7V1FFrAHy2sgYH1if2rk75RE91Sp4uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=X1Fgzq--qdmyIGv3uLRmNxVXx9st9RL2WInJrbaok41Q0_9AulW_E4vUmMwc3_sEM4HLGxj60b-ShtB41ugigQ9IHC8xOVvgmaYZzBTBowquCzDkSVDbjbHRZbUanOYTwaJIpdNajvI3OVNskGXcRIsd5rPShXB2DOELxCX1Gaa8chG_a7J4aEXDDbkSTHEtNnDDAiHrCpbZudBq25NrjCOyZgCbp14j346DPm-DW934br_ajFAYcDlzl9MsM6rV4_-M-3b25seVrue5evZw0NcwrkZLIMvP3Up0Qhs-v6X0_4Mhdt2khLK7V1FFrAHy2sgYH1if2rk75RE91Sp4uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو ای منتسب به پایگاه نیروی دریایی سپاه در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67453" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67452">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ckVu4k7auW6NY0LUnRH33lAjPyiqPM-GGUej_qe97MeNZSEQ5Tc45zwfWDmUV7N4kOO4As2TW7iOesTlJOvlGE0jYP48nMlNRqoSczH1McaSqCrSv3wNtX4lICCeZyZ1O4-3S4QDyC4PF3xOwKk-egma3erUpzd_jTit0UxSOuq2bRO8vkOaydaUfUFxDJ-kYR7Nh0PmqD7rHiDeAvZKN1YTb_r4E4tqUBpPvBcCINy8Ho9GIZXyQupMsKU_wkXK-w-hCb7bBIMqPd-K2_XyiFqL1VO3yqnTVm3eIB13pD35qa2EyMnvAp-U6_O75J03feYzQ1K_to3HZ5cvQEs30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بامداد چهارشنبه؛ مشاهده ستون دود از سمت پایگاه هوایی بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67452" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67451">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVDUEFND2gJRMgMJ351RDgRDwf5ZX8-txZTeK9TJMetvb-WctRMhWcSiMG2a2IRGT4p2nq4sBvIgoobU43KRktIhTIYSZJn2b2rB3RWqqt-oT4UC94kWRi-DfvElo7dwO3ytDhiZCzAvHQuRzVOXctvdISx7sdVhX16aNwb_ejAbN6wgqa9k1aVV3Igp_bZ9kuxy6HxpAOkHpSkvEMQVaWCj_VT01Ny1a-wHmkIhmN0eBuYfqGzdDdNjcf1zTAVPmIR_8UA58RYZ-zSt4ANHmQEmKjKHKfrKUEAoqGIdxHOxpg96W0duEusSJUUeeAT5pqH9dYsrCsX2MHwrIKkn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67451" target="_blank">📅 01:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67450">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3qPXmYLn8wGNo5G2KF9O4UadVwLgwXwjffURIUCrs85uz_eKTDKE-U3zO07oXhQsq7cAAW7saFyOwkETyjj_UzfwLGcSwREhj0X3FjJfeajCaQ8SJWL7gLvhk6SXFvJcUjE6T7zLP0NXMqUpEyBJ8ACZ_bxydGWdSEp9knHofr21cdsM8sfmOCe4CB97FK2EQfsi9SE9gjPyatzwvjSHoZtIgGIg0X6TMb6a4ZtVdLUaO7xeipPDVKI9xF0epl9EcHSCMOqXWXNxnAUsy3uQI2MsZbdI5g5Otmap8GL_de6Sgdbf5GFW0FRSecA-lojnWloHhMnLtaDAhjzjWcABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه حمله آمریکا به یک اسکله‌.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67450" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67449">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0JBeGYjSXWthkaKRvUTgROvAYqpBRVI2UxN5EX9Mn1ZDchyyU7xrWR8t0yH7mO8StHG9jO_nyAfKqY6N0cz4g8EWGZxKHAvYQyshQNzW2iRFhwIb1OIRWOWX0_yod00Km6A5fb90KbptOJZLB31aVK7D3e0zhp67aWmGJx2uq3EXpTmDvF1Aa_ailBKu8pFt0lXR6CEPYw_41sc2h9WKyYNtyLX2g99HeJMa38HZ9MPMTK77qhA4IYgZ-XYDEuG6vj71bsT_XH-qkC0E5u3-1cCdzKx7TGTgKSaXo8PNow6Rvyejj2FHi90NPX75V967SQT5Q8kg-vy_fv71PtMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری منتسب از سیریک هم اکنون
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67449" target="_blank">📅 01:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67448">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VHaWR7886ClfBYTKg6277_e4_o_mllZbtvCNkWG-4iv4SYt8zMWvMuFXd0p_CLASmMazJsMT0TQQHAiwYWSzq-djiUOJIbHAag99ZMgC81nhITLaTjrb_J6rrT4ltaXvi51fQHbLH-4YaPqydosPqgdKHPqewtacAugWcLtgFccfeG4w8PXPCUAmXlpuJ5vqdx47xBtrDLMiquZ_HMvg45sGTSPcaT5L51RmUJqOPDfkdBgJ_rTVtYTX-Xl9halvd3cInyZnkvGnULLSyfLoMWAZi8HSOob_KBYIugM3KZnoICVqcPuIlwPSsXc1s_2M-tDiRsg5DHwLGpau16kdUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسکله‌ی سیریک، شناورهای سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67448" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67447">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtjfHXwC2La87OjMXas6FTsZH3UZx4grRbMqM6DDOASeGwphVA2Y7Y79fzsnTcSGASdMesLVXBNScljDAA6m145IJPXf_GCjefgq03GspOMffofNUE3vz7g1tLRQsAWBYdjEjXqu1yrRKEDyHxqkxn8ys86T01Vr_INfICtvfIt-RGmHorhwrMbxrUbxhJX4Ye2D3_BsgZS6TE4QXjuRap8nP0hT9rMc-VxIOFMhjAH9wyIH1luLKgKsKIJhoZn3olcgiF9YQkQnK8OyDlT6o8NK0zZzLkeHOJAAi6mhSi5JcaFyIRSi10jxJ--SHJqO_nndCTv6hjxQymohg_jXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید آمریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67447" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67446">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از هدف قرارگرفتن فرودگاه بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67446" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67445">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=UtjpD6Kt7YhBiifBVY2w9Iri6jmjHBIuZmXOgv18A6i5GNeeiyEKlg0S_Gs5tJYNlubmz0YDcE9GUn5v9stOXlrOh-CQj6OLuWkMpkbfJ4zQrAgXmmP4buSz7jQZKfF3jwjNQCf3av3rI_I4G7_esW2MJXy760Vx2bq3nScwT1p6kIm2ONjyv3f60n6QQ0X3aN1nJetVwrc59erEBLmdMBpVLQiRpqhGA3FxLCz7_CfDo5RCOe8fuHQn7LsixitxsyD0QoHBu0UC7sxdWstoeswsPCdsZpA-1vfqVYeaHnIQm7hB7H2UgCc02EiVoaKthDb5A1HE2i79iD5ewYfb_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=UtjpD6Kt7YhBiifBVY2w9Iri6jmjHBIuZmXOgv18A6i5GNeeiyEKlg0S_Gs5tJYNlubmz0YDcE9GUn5v9stOXlrOh-CQj6OLuWkMpkbfJ4zQrAgXmmP4buSz7jQZKfF3jwjNQCf3av3rI_I4G7_esW2MJXy760Vx2bq3nScwT1p6kIm2ONjyv3f60n6QQ0X3aN1nJetVwrc59erEBLmdMBpVLQiRpqhGA3FxLCz7_CfDo5RCOe8fuHQn7LsixitxsyD0QoHBu0UC7sxdWstoeswsPCdsZpA-1vfqVYeaHnIQm7hB7H2UgCc02EiVoaKthDb5A1HE2i79iD5ewYfb_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
جنگنده‌های اسرائیل حملاتی را در مناطق باراچیت و بیت یاحون، در جنوب لبنان، انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67445" target="_blank">📅 00:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67444">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ از ترکیه و بیخ گوش ایران، دستور حملات به ایران را صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67444" target="_blank">📅 00:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67443">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
حملات مجدد آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67443" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67442">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBNy96DAGN8zQsWtX0XqIMaayhualDAR9Kf7UgSo35-s_Df8Q-JeG0Lu78jpmavCpWCuc1x64CgaMmr0ujuk8xYu8Y3Zu7qdPWwYxKQX76jh6TVPqLYyhj9-Ue-RLDU1BsMOjuoe7abB9QMX3TpQNfgpfzFKVNDF-JOVrTWfWUURqqELJo1jzCfR6ZXdNIEKc24VFUQZPEMeP7BimnkPaFd8_A3IzIM2vodxe5M21j3_N0ia2Qngl1q3EQPX1Sq2MaM4wi8fjTwNxGaBFVwka5H4AtxhM9T7gxeanRXlDoKnD1cHw1-NProveNIzAkcBOUOc5biU3Woa-zxVRMI-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای فرماندهی مرکزی ایالات متحده، سلسله حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه‌های سنگینی را برای هدف قرار دادن و حمله به کشتی‌های تجاری که توسط افراد غیرنظامی بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنند.
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در تنگه هرمز در حال عبور بودند. این اقدامات تهاجمی ایران غیرضروری، خطرناک و نقض آشکار آتش‌بس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67442" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67441">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
#
فوووری
؛سنتکام هم حملات آمریکا به جنوب کشور رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67441" target="_blank">📅 00:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67440">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با حملات آمریکا به جنوب ایران، حملات اسراییل به جنوب لبنان از سر گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67440" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67439">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
انفجار ها در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67439" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67438">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چندین انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67438" target="_blank">📅 00:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67437">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67437" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67436">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=nP8_Jqk6FrMdDTwx3BlAuj_IhLfMZnTzS5yu1H-GHc97fTpBOaio3r0EERoMhC5baTvLpUKMfHZZb_kY7zGwNtjwmTUuK85073-ssZ3nmzHEm5paF1Ge2eF3_joSOPfwcLQ6oNxMhFOWokaY-BFu0P2s2u117DLSQpS9rL_Gsmyiyp4x3Krvyd7DGRkYOF7NyNQnkFVWq0MxElFlfC9ehQCFYXvdkhIKP9O-O0dAwOr13jg8yuj0qWvLVRQpv8PnLuWdQk3kV6yHzl-RVMYTEPK63XSytwOTSvW1-9ibftQGrx9zMJ2uHcIul3TwfwqiWOVPKciplyrPdWkS2O_KqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=nP8_Jqk6FrMdDTwx3BlAuj_IhLfMZnTzS5yu1H-GHc97fTpBOaio3r0EERoMhC5baTvLpUKMfHZZb_kY7zGwNtjwmTUuK85073-ssZ3nmzHEm5paF1Ge2eF3_joSOPfwcLQ6oNxMhFOWokaY-BFu0P2s2u117DLSQpS9rL_Gsmyiyp4x3Krvyd7DGRkYOF7NyNQnkFVWq0MxElFlfC9ehQCFYXvdkhIKP9O-O0dAwOr13jg8yuj0qWvLVRQpv8PnLuWdQk3kV6yHzl-RVMYTEPK63XSytwOTSvW1-9ibftQGrx9zMJ2uHcIul3TwfwqiWOVPKciplyrPdWkS2O_KqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های رنالد ریگان درباره جیمی کارتر و نقشی که در سقوط نظام شاهنشاهی ایران ایفا کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67436" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67435">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
مرگ ژوزف استالین و نمایش سه‌روزه جسد او در مسکو، اسفند1331
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67435" target="_blank">📅 23:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67434">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOewilCjvA7mmZaJKSKlLTEOZBBoeon41HF27mXIQw_DxOkbqN7crag11I9_pBsP6GlKbVplz0GzESlx2-gvVBYTlUmRcPFV-CPRfFWn-ve2k6P4ocfTtmgSJrAjJmITMTW5JrqoFf24kjtk0lBMcKK7Uol5JEp7FlSqNXsUtVw-Rp-Owc4RQIjZ_svORG5ei33LdtQ7xADrXj4Ugh4faXZkso87rk-0ZUIcL_kDx9kTz3dYxiCiR3hJsGPFJZkqZCiMNOgQD0Zko319olvkdmgo6fTBhb-llXgxDXZj6KFSgFdBbMUe1eoZZD4pWITcv5fkkAfyCjq-wFAFm5yQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا چخبره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67434" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67433">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد».
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67433" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67432">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
طبق گزارش ها یک نفتکش بزرگ دیگر متعلق به امارات نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67432" target="_blank">📅 22:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67431">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfyhFX9D5znAsE8eNpgIQ7rnhS7O3mLvFFjMpit_DKsYJjcAo_5oTl7QiXHRa5AcV_BrimWMfO89YrA3fgQGyadtHUTgndBDLOZtpkqKhTOpyNaQRbaFtzzdT6moFztxUwpiZnW9UTZV_gX6VPjRQv8lCB79gO1x2t8FDg8ZRezQS14_VpumiWh9hsfIkE0MsSt_CH4M3haX1kVSq18bz2UJvSdLsb6jKdpww3F3TeEyBr_aRf0uQFba4ru5pbmMpa0_dlmfbwgvY52D1ztL0DUaW8px4Vk9SXq4G85wSf-Davwn4ejav-O5YaJQlvAGcm3DiwZgwj2dHef5yRjJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67431" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67430">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99630c1014.mp4?token=cCGQDMf7msqb5HQTGRpvf23oq2n765gSVLG-_iPPzN_crXRAYwl-MDVd9CwxSv3yH5pq2f1VXe4YfUYE-1ZpsTLSYxNHL1Kx4Ti2G5a5RnNpjZB-q7SEvm0XR4ZRQxxZoqMN2eq8_-CkFiPoYKl4u9QBm5ly68WRHT12LAhr_pNarV376S9oTdiHjU3SlXZNOJ3If_jwNccNyu8hWU4ROOy-PjWdd8FNPzCfbPSLow1vY_QUx0kh8CdLLqw86LHxioEqlfcG_W7u_HQdSIYyB9DrOM-UzC5oskDKI7eijjuczQrRZzjwpA81G5J3rQLZOeVCMJVYN995aZlcsDJauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99630c1014.mp4?token=cCGQDMf7msqb5HQTGRpvf23oq2n765gSVLG-_iPPzN_crXRAYwl-MDVd9CwxSv3yH5pq2f1VXe4YfUYE-1ZpsTLSYxNHL1Kx4Ti2G5a5RnNpjZB-q7SEvm0XR4ZRQxxZoqMN2eq8_-CkFiPoYKl4u9QBm5ly68WRHT12LAhr_pNarV376S9oTdiHjU3SlXZNOJ3If_jwNccNyu8hWU4ROOy-PjWdd8FNPzCfbPSLow1vY_QUx0kh8CdLLqw86LHxioEqlfcG_W7u_HQdSIYyB9DrOM-UzC5oskDKI7eijjuczQrRZzjwpA81G5J3rQLZOeVCMJVYN995aZlcsDJauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ترکیه:
من در واقع چندین بار با ترامپ درباره فروش جنگنده‌های اف-۳۵ به ترکیه صحبت کرده‌ام.
به نظر می‌رسد همه درک می‌کنند که علی‌رغم دوستی شخصی که رئیس‌جمهور ترامپ با اردوغان دارد، این موضوع ترکیه را به یک کشور دوستانه برای ایالات متحده تبدیل نمی‌کند.
برعکس، این یک رژیم است که با اخوان‌المسلمین آلوده شده است که از ایالات متحده متنفر است. او حماس، تروریست‌های حماس را پناه می‌دهد. از آن‌ها حمایت می‌کند. آن‌ها را تأمین مالی می‌کند.
اردوغان دقیقاً یک متحد الگویی برای ایالات متحده نیست. او نیمی از قبرس را اشغال کرده است، یک کشور ناتو دیگر (این یک کشور ناتو نیست).
اردوغان تهدید به نابودی کشور من، تنها کشور یهودی می‌کند. ما یک کشور مستقل هستیم و قصد داریم مستقل بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67430" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67429">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUP2BOpSR0KD9442XTCpCSm3G27ahAcY_U8PmAwJ7e52EHHwX_lX_80uLEiZZ3rmGHMB3TBaoF2zQvJHKzDW-eQoOTyt7B7Hz1qIrCp4WkPC_pbwSPcRcp2KVeapHE86Pek1GUh0sSssRLFGkTm6xP1XdQ4xXvDUpnuFRjZbmIWQwU4mdhQjzDz5OByzprg51ZJtnMB_Ae9RCEuPCD_P-SNqnlNcFrN5WxqdRRwgmdUi3vvxrVhLE-GsFfW08LrcI12UN24Qv03tNuqOvTGdqiH-nk5e7WadI9uENG-Gc3jaAFe1u2h87pMM9avENh4i6fYwDsJbRdtgnqcG2RMMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه یه دختر ۱۸ ساله از فشار کنکور و امتحانات نهایی و بخاطر فشردگی امتحانات رگ خودشو زده و خودکشی کرده؛ این پیام رو هم قبل از خودکشی منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67429" target="_blank">📅 20:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67428">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDbMvRfgkISvMuZd03tzaAkrLA5Dlacc_A5GcI1WksB8aPUrkqbS3g-7UIXRuLgQevU4xNTX0M0PyCB6bAqQV5BvoByLaO_Or1ATnNuhggC0T5LYhIot4fiQ1QFLbccNbIlOoSn1IJ7rCOnxYihgfhrKRT2lce321N0VnhXJP_cLdlbhagDYiYyZil1QMW-lr-kSj9KgPLxdud-gww4XkBemRC6kUuCpj2vpsI7FXjLoadWLAV_SQ_Zpb6qxgw_oV0HBhpSPeyVazUA5dFCtIHwolCyXwOOns9XKaaPtOJlzoroScl9wHjTpCDA84iA566RMMb2S0WDX_a2tPMwqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ان‌بی‌سی به نقل از یک مقام آمریکایی:
ایران شب گذشته با استفاده از دو موشک که مسافت کوتاهی را با سرعت بالا طی کردند، به دو کشتی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67428" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67426">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfhizeVsJzVQdz2yQfZqrxXKgbLGU9vRhmopaGumRUz5vv-vLzl6Rof0azfsq5BJdtYyafeon4XHYigwltaH6Dx00YRlPw4qKWQ92VpHusFFuVpu59-KCyFEzf8IwZYAmCJy6T9S9geMRDZ4qebHT0LWBh9zpKsguu-OKcJHJEeaeaXEZJFgF6-4MUNZsKW_vqSCoBrz5nBQ5od5x-Lbmwtr941g6ZIQkiOd_HWhrNoqXmTzjYQ_4duP_0OC8eSlOBn6QjEF_Ig4LMctP5EDEMHo2yNScOdIa1RrI15uhhkVfoPkBsh5dwwdXE89A_RDnn5etPSo9ej6H-kwl7SQ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwpTn48p5YWN0F18hZI4Z6_9xJQNoUmtkPKGpnclLhnme4TieAUywT8aZ0XWXnIGoWfCq5T67XFtwpB_yyMVuYmH48AlUGblLoe7-qbnpPyBlZqN81tXaZVi9E63SvzVtzxWM0D0CLKaGNcZfP-exn4NxUqPNEyEe0YIr3fzS2FwqVkXes9vxsk69mu0YCR8ikcKSzEpETPhtSaeLwxbTAlWYKBvqDkxCLxD6jCl-fNFCp946zpVb2NyVb4iPlaO-SbkCiIdsM9wZjO7h8rcJR3IlNr6oNGrrcxL8RDvCasH2P2Hnd3wi99YisFrrRdOt9OO_SmJ50P3BZWTK5Al5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صدا و سیما این تصاویرو با زیرنویس جمعیت میلیونی مراسم تشییع منتشر کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67426" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67425">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=bPvHUzwcG0OHpxxTXwVmJRT8z8x6iyX00cUaguXq_zsoyZMYC24VXG3ATZoCekZcmOsofIfSNBIwMZ7WQ4j9KUNfesfrPakKNSsD5U-NYW-ET--2CLquxcCVkGsmlhJVSV_HQXuUhPBfXRqUvl4cTlSKM7LqbBfXsmEgtI31TIc9SGTFa9JbZu6yEbW4-N6EwGp3RZ7g8x_UUQ9o9QFeLNMX-p-wTB1EfSIJhTDt3xW7wb74ZBqK0QvQ401yvUkW7l8VbT42NFnw-8WW4sHcaCwjy2oFS5nw1DOuaP_HIX7F8K0F1wYcfuys3CwaNAJeUUYpWqsSNCk_3FJdvIMkRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=bPvHUzwcG0OHpxxTXwVmJRT8z8x6iyX00cUaguXq_zsoyZMYC24VXG3ATZoCekZcmOsofIfSNBIwMZ7WQ4j9KUNfesfrPakKNSsD5U-NYW-ET--2CLquxcCVkGsmlhJVSV_HQXuUhPBfXRqUvl4cTlSKM7LqbBfXsmEgtI31TIc9SGTFa9JbZu6yEbW4-N6EwGp3RZ7g8x_UUQ9o9QFeLNMX-p-wTB1EfSIJhTDt3xW7wb74ZBqK0QvQ401yvUkW7l8VbT42NFnw-8WW4sHcaCwjy2oFS5nw1DOuaP_HIX7F8K0F1wYcfuys3CwaNAJeUUYpWqsSNCk_3FJdvIMkRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی، تحلیلگر سیاسی و فرزند یحیی رحیم صفوی، از فرماندهان سپاه پاسداران و مشاور ارشد رهبر جمهوری اسلامی:
🔴
دلیل اصلی ناکامی جمهوری اسلامی در دستیابی به اهداف هسته‌ای «برتری اطلاعاتی طرف مقابل» است و مسئله اصلی، نداشتن بمب اتم نیست، بلکه ناتوانی در حفظ محرمانگی و پیشبرد برنامه‌ها است.
🔴
برنامه هسته‌ای جمهوری اسلامی یکی از پرهزینه‌ترین پروژه‌های هسته‌ای جهان است که این برنامه «نه به تولید برق منجر شده، نه به ساخت سلاح هسته‌ای و نه به کسب مشروعیت برای حکومت».
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67425" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67424">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6z_DcRfiCuCNaGKzxrK48Ie2Bty1eKkumD025K8qyFIhXkM4kB6ZfuK8xaY1GiMk1-3ivgh-jxxcyazKG5XBhECv_vpV0DQlpnC1ponAUFNewSWKkJSn47kA9DNNiHpU0fpscmrmabEtLsIAmpXypS7MGtNpmXu8vPYe5HH3mnXWW04XdllMp1HtWP6RWlkzYMDMjrlSQuEp7EL7tLz35ZgpXPvlDhtZ1zwEDbbJZ2YB7M9MnCWakNirqWuMAQIRdfJFnaYfwdEZhYOfFRijW3k9Qo8BvRCP8ldUR4hlgS5_PZw8LKLYeLM72YK_htc3-XagRAzsy3Axmjq2gWTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67424" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67423">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=nWlRxbObS-ll1bGe7UCxVDiUdwiblWip2h042MqwYsuGRUYQIJp2vwggRQc2ABZyFZjfU6fHybG94DHtAyu3hbV8PAab3ZKmepRGXmigDKvzxHbk7jIDKQWMDV-aYNImJAHvt8y4MncfzBvulfSzJUPDmkT5yR5YNtvVK-hr_7dqYjYnL_QHleCihZxM9QCl9lXurv8uKwzNsAbpShHxoEnt-3nTNYb6fBj1o2B1-zzLfR8gtuVY-TiFpFKROwPewK0CcgTySLw_29HJbus9z0250bIiQEqkZ4UVqV7d04achmEk8i19XQ78_ylgRcs7y5FKwfk--QePqpQQkAMBNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=nWlRxbObS-ll1bGe7UCxVDiUdwiblWip2h042MqwYsuGRUYQIJp2vwggRQc2ABZyFZjfU6fHybG94DHtAyu3hbV8PAab3ZKmepRGXmigDKvzxHbk7jIDKQWMDV-aYNImJAHvt8y4MncfzBvulfSzJUPDmkT5yR5YNtvVK-hr_7dqYjYnL_QHleCihZxM9QCl9lXurv8uKwzNsAbpShHxoEnt-3nTNYb6fBj1o2B1-zzLfR8gtuVY-TiFpFKROwPewK0CcgTySLw_29HJbus9z0250bIiQEqkZ4UVqV7d04achmEk8i19XQ78_ylgRcs7y5FKwfk--QePqpQQkAMBNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تندروها عباسو گیر اوردن دارن بهش اشیا پرتاب میکنن و بهش میگن بی شرف
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67423" target="_blank">📅 17:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67422">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=LDZCoM8BLIYPIG8HdYjbu8NOt2hfqyh-gho4Vb8UiaeAlRo7gPkdePbJpkxg04PvpizIeX83o3oPrZeI9Ttf_8SCZjsgPGNJUKzWRUOm6ica2ypuc3jROEb3viLomntN-uU2kPqv-1Xp2ByGUWRw6fdhz4SgbouefD6QVtmvaUCcw4llkr33je3kAWYIjG1gTdCSrmdBJApKYrW7HTcgo5bbuup6dELCwGPj6mNXa6hR6tZsCWVcabErPHt0rlQS7kx2PUhrwih50ZvvB8bxDCZIPs_WDtupGsVJnEmeKcp-MIy3Lf8DdBDKPstkOg51Ot1QVTDxb_L14PnijRMP-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=LDZCoM8BLIYPIG8HdYjbu8NOt2hfqyh-gho4Vb8UiaeAlRo7gPkdePbJpkxg04PvpizIeX83o3oPrZeI9Ttf_8SCZjsgPGNJUKzWRUOm6ica2ypuc3jROEb3viLomntN-uU2kPqv-1Xp2ByGUWRw6fdhz4SgbouefD6QVtmvaUCcw4llkr33je3kAWYIjG1gTdCSrmdBJApKYrW7HTcgo5bbuup6dELCwGPj6mNXa6hR6tZsCWVcabErPHt0rlQS7kx2PUhrwih50ZvvB8bxDCZIPs_WDtupGsVJnEmeKcp-MIy3Lf8DdBDKPstkOg51Ot1QVTDxb_L14PnijRMP-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توضیحات واعظ موسوی فردی که تصویرش به اشتباه به اسم مجتبی خامنه‌ای در فضای مجازی وایرال شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67422" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67421">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=NldDL-16EPmKJNAVqX5V38waOqZ5ktZ6Rm6Jd5KJqKrybtm1ecappoJQcphmyEyo8iC0nJK5N9yzK2E_mOLgB2DD07fHewgjkdB0cHrntx3GItr3y8q_eJZmgwZ39qGHyXRwSQG0OhDjwUv9TQp5XqQVdF-TA2USO8Bboi_bxzzMirDWFx70JER8hqIPuzfofc8KZqJMbmSCMeFdIojyo_Omb1DMaWMG_3JGVQzR9wKbvaX6UlEX_bW44G_97WhORKZ3bUxD8Q0DpdKjbf_D-j0k7vL-LZZ8a2X8ssJYvyo301trLmZokESDf-W6p_q7OzsBwfL4mRc3eMXz-MgWMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=NldDL-16EPmKJNAVqX5V38waOqZ5ktZ6Rm6Jd5KJqKrybtm1ecappoJQcphmyEyo8iC0nJK5N9yzK2E_mOLgB2DD07fHewgjkdB0cHrntx3GItr3y8q_eJZmgwZ39qGHyXRwSQG0OhDjwUv9TQp5XqQVdF-TA2USO8Bboi_bxzzMirDWFx70JER8hqIPuzfofc8KZqJMbmSCMeFdIojyo_Omb1DMaWMG_3JGVQzR9wKbvaX6UlEX_bW44G_97WhORKZ3bUxD8Q0DpdKjbf_D-j0k7vL-LZZ8a2X8ssJYvyo301trLmZokESDf-W6p_q7OzsBwfL4mRc3eMXz-MgWMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های اخیر علیرضا فغانی از ظلم‌هایی که فدراسیون فوتبال در حق او انجام داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67421" target="_blank">📅 16:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67420">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCWDW5__JM4pbX0qOlB-QCvz9RaDVVXWM3-aOs8HLkM24LUdIGGQCL2xyskLsNT1wXwzBviu_XBFAu1RKfKlwGLNvurfsbbQofzAvxp4FJa5P08dXeHcDnUl22n4DoWMuoASNmtJx4NjFaqBW9iexqVegiZ4RjwNLcFnNxV0xMN6ZH0PbTkif8qFo4JW8DdNxugOb_gNs3hAaY3QCmWlFawCoY7yC_03tlx_LS7eUpXMNxnPfusYwKtSud1GlQf3KryrUobcGpAguLjr_RZ7bTP2xaOJYyNxAOdP284vn6leB962W-ZoGq5gwi0xps54KSR3RZ71B7-3pxh6w2BbwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری
CBS:
علیرضا فغانی قضاوت فینال جام جهانی 2026را بر عهده خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67420" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67419">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=Bcsw8LYybXsBqVZk0PXDR7afLjqFpykcSJoLnVi6aHWFMZSJGkp5m9t6guM4o6N1EZIUEWZijBVxsXmnHnOnV_Rsnp2o8fAHGJH1LZ921MRN2f4BJP8cD94JPTAE5BOIvRPWJm55DgdzjG5AguRtwsg7DwBx4FH93s5uGHK1g-y1gzRJlAivzERsqmyHID_dzL81nhXB6xMplRdGhJMbG5DcXR90JdwE11yiOpNS0QAlCzzm3QqYRb2KCGIQI3xbG-OM7HsopiK4HkI1fvZun2il9tYs-N5zW9yftnE-14piBdlL2-zA7WWwQYrxZn-plqOvZ4noOg1ybQQhIVGO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=Bcsw8LYybXsBqVZk0PXDR7afLjqFpykcSJoLnVi6aHWFMZSJGkp5m9t6guM4o6N1EZIUEWZijBVxsXmnHnOnV_Rsnp2o8fAHGJH1LZ921MRN2f4BJP8cD94JPTAE5BOIvRPWJm55DgdzjG5AguRtwsg7DwBx4FH93s5uGHK1g-y1gzRJlAivzERsqmyHID_dzL81nhXB6xMplRdGhJMbG5DcXR90JdwE11yiOpNS0QAlCzzm3QqYRb2KCGIQI3xbG-OM7HsopiK4HkI1fvZun2il9tYs-N5zW9yftnE-14piBdlL2-zA7WWwQYrxZn-plqOvZ4noOg1ybQQhIVGO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ برای شرکت در نشست ناتو وارد آنکارا پایتخت ترکیه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67419" target="_blank">📅 14:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67418">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g930ny0PgcNtK3CRZzzLzJBUuIxA0Ti-u3_LkxvE33lSAvM2-x3OoKRATQ7J0f7ACoQHYxzaq9rfabqYTg6rTE580-bAk5PUeel6aO3rxacUhuTrc8_eILEnKCq3NYgxX9R7J1nHkouj569StzIDQb83zxB0grEVnd60DppR5Bl4YhfIbqK6U_HzznDG8sdsQN2Y5kadKO3H3Fy0gpVxawDAsVm0IA145kFPMeXdn1uuOTuF7SCvAvlHzxqFNDfLRzEjQqiGrsMwglZHGpgGKBrp83KYvDhKoP19HQdwKn_fNOhgdTVkNG-JmSC64odvfkurse1Ck9gDMFMPs6Nd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری رویترز به نقل از چهار منبع آگاه گزارش داد نفتکش حامل گاز طبیعی مایع «الرکیات» متعلق به قطر، هنگام عبور از بخش عمانی تنگه هرمز هدف قرار گرفت و آسیب جدی دید.
🔴
به گفته این منابع، این حادثه پس از گزارش‌هایی درباره شلیک موشک از سوی سپاه پاسداران به کشتی‌های تجاری در حال عبور از این آبراه رخ داده است.
🔴
بر اساس این گزارش، پس از اصابت به سمت چپ کشتی، موتورخانه آن دچار آتش‌سوزی شد و دود غلیظ امکان ارزیابی بیشتر خسارت را از خدمه گرفت، اما همه اعضای خدمه سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67418" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67415">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNbS0wqUxn-u8L8c55twZz4N7hBe1svFsmnD430-gsKdo9aXJ0ftQyp1cQ_hllS5hfIYlfYq1ZOWAmCRN5hZ4ZUAUwKGZCKl095zFPxodsgV51rKH82OZwDnaHLR71dBBXbD6dQy8UWt5QkXy9tw3VAZS68kvSK4yYl-mxk1d_gMD0JQjjCixGL9wFQToWhw1ZcDewEf_Hg19cfXkLTWSxpd1ORp4IuFZ7yzclYMBxE-Cb5fHSWISjtno9_5xZWIjH6decqnzvN_Djf1Vvsz3F01tYgSDT_-VteUCdV3kimbFpqiHWJ3WiMCOJmpRZvPR1TK2IR3Z2PO56Q4B4GROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=qu5GWdEUNZVbu5uXRIO-OEC8iS-oXlR30ZQvLJIDg6sXhqNToVGHPl6A77mMaa7RhoAgqTjJ_cf8Rz-2rMdZTpx5S4Synu2kUhoxCk9oMSL8tLQDBt9j8aYn5fD05NhWLhGPKSYyDeOobpyETLexxNqZtZxEiUhpcneGFNKh8RhgIh_D6OeTGuwPXJI2xz_mdjuvnzdEnw0WB-t_ZtZRwWFRLXKX0oqm_S1n8wtgdxNMWoo9orAgp34uzfmOAkCknB9PJjvqTYBvF8zP5RUoqCKZ11rVkhsTrWMJJcIkjSQ6rsuuXzAQ-uxfxupt3gTDqWGpxW9p-vxCU1gcAJbZ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=qu5GWdEUNZVbu5uXRIO-OEC8iS-oXlR30ZQvLJIDg6sXhqNToVGHPl6A77mMaa7RhoAgqTjJ_cf8Rz-2rMdZTpx5S4Synu2kUhoxCk9oMSL8tLQDBt9j8aYn5fD05NhWLhGPKSYyDeOobpyETLexxNqZtZxEiUhpcneGFNKh8RhgIh_D6OeTGuwPXJI2xz_mdjuvnzdEnw0WB-t_ZtZRwWFRLXKX0oqm_S1n8wtgdxNMWoo9orAgp34uzfmOAkCknB9PJjvqTYBvF8zP5RUoqCKZ11rVkhsTrWMJJcIkjSQ6rsuuXzAQ-uxfxupt3gTDqWGpxW9p-vxCU1gcAJbZ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رویترز:
تصاویر ماهواره‌ای نشان می‌دهند که هزاران ایرانی برای مراسم تشییع پیکر علی خامنه‌ای، در پایتخت گرد هم آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67415" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=DqEvApWqKSY-QGMNjWUqdQhpw41HdDQ3WexAOisqHjzqCDpeMCC_qObkTAGLDLOKLAqDxL5yuk5dTULQyOZu_GszDExR-StV-YWXI8LSjnGCBpsK02oiiYXIKO3gaO3B0ODsHxCd6xY1Bwm6MLuJBM6jXLhtbEkBSu2ngzi8WzzFb-1sQH-6EkXq0OBl5_Z9oO1nu2SMpeel-lKyDHePchVg9ZYk_a3_ELFpCWaO6t5zKFC7htxblAIU1j1k4WMMTbJHTY30ttZdvdUxhs1CTqjV5RA2CSQ04sPCeekA-nnZaqByy-PaLZUHikWEkT53cdru7Fvj9uGokTb325ryfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=DqEvApWqKSY-QGMNjWUqdQhpw41HdDQ3WexAOisqHjzqCDpeMCC_qObkTAGLDLOKLAqDxL5yuk5dTULQyOZu_GszDExR-StV-YWXI8LSjnGCBpsK02oiiYXIKO3gaO3B0ODsHxCd6xY1Bwm6MLuJBM6jXLhtbEkBSu2ngzi8WzzFb-1sQH-6EkXq0OBl5_Z9oO1nu2SMpeel-lKyDHePchVg9ZYk_a3_ELFpCWaO6t5zKFC7htxblAIU1j1k4WMMTbJHTY30ttZdvdUxhs1CTqjV5RA2CSQ04sPCeekA-nnZaqByy-PaLZUHikWEkT53cdru7Fvj9uGokTb325ryfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جکسون هینکل فعال‌رسانه‌ای آمریکایی رو بردن میدان انقلاب و خودش داره شعار«مرگ‌بر‌آمریکا» میده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67414" target="_blank">📅 12:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67413">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=ZxqxFRLEyE_2kjJMp__x1YqZnoO3mHw7kYX9_9lQcZjJl7RquANDNgzH5xqlEnOA3D6YM5Hy8AT12hCT5jm1TojF_RiaKUEU4HwNSc3BDj67SdcM3Ij7ofYXR-MwaGQjpdyPmmvnt2TBTE36XINzqo0K_j2_uHfQEltYSq18zryyQcUK80hO6RpZh8vxY_LPw_1NtGExRc283ESth8K9OjJbpSnxE4Lc0BGsbF-Gg1ZWUOJIx7deb1nDUcctKK6YzJ1iA-OpPw-5oYaBDtIU-sKq5XYW4hqEGGg8YJNGSUE5CYEuZyQWa2VKcwSpo_r3xDPAKi7PbX4qZfuBzZcwYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=ZxqxFRLEyE_2kjJMp__x1YqZnoO3mHw7kYX9_9lQcZjJl7RquANDNgzH5xqlEnOA3D6YM5Hy8AT12hCT5jm1TojF_RiaKUEU4HwNSc3BDj67SdcM3Ij7ofYXR-MwaGQjpdyPmmvnt2TBTE36XINzqo0K_j2_uHfQEltYSq18zryyQcUK80hO6RpZh8vxY_LPw_1NtGExRc283ESth8K9OjJbpSnxE4Lc0BGsbF-Gg1ZWUOJIx7deb1nDUcctKK6YzJ1iA-OpPw-5oYaBDtIU-sKq5XYW4hqEGGg8YJNGSUE5CYEuZyQWa2VKcwSpo_r3xDPAKi7PbX4qZfuBzZcwYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در حال دادن شعار «مرگ‌برآمریکا» (12بهمن 1404)
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67413" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67412">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3FvpwHv4ckBizbGQ-oxobU_qu-S3-fn2z2Xm5VFREqJMSAjBqsKD9ABmVg6FOyz9kP79vJP_DMA1x3iWpoEB0LTmNW5u6D4iyghijhhLrbGpBVaIRZz5vXbC3AxUxbQUZIjMs2KBM24oS6_bKRmqd3AqUm-RqTOD6SuJ0TPA2QR0rXrCegNUFjT54yqXTBFVeX1NpjcNo8EBbTgR8EJIpPn8vcMssC9pyjv9pJPiTdE7a7VtjL9ObTEZcSc8TJCJVQ0qkvH16VcZAa6hblq40YLQelKEEzq96vGQb-lLYoR8MOzyyDlI8LWVps9-QvRmQ1AG28GLJMIq01MnOCh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس:
دو مقام آمریکایی به «اکسیوس» گفتند که ارتش ایران دوشنبه‌شب دست‌کم دو موشک به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است و دو کشتی مورد اصابت قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67412" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67411">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
احتمالاً نباید این را فاش کنم، اما ما دو تا از بهترین نیروهایمان را برای محافظت از قاآنی در مراسم خاکسپاری فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67411" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67410">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64666ae825.mp4?token=GO6ldPAFtoA6wdqDjmd7xTsDfmE61HplOuhvbGo27J3a8c_I6Kpv2DVDLyCfzpZnxyiQoxV0N8dX5fLE1Anqs0hY52shBzcot7Q_B8B43Y8Y5-m4etgVxn2lKBtqRu0hczTKWmc4f9E3h9LsB4Avrze2fdy9hR-e7w3WoYarmUaU5vBPm4pz2mjXqqT6jzdzNY440f_IzQuwx-t1vEKQAy6eul2BkS0ZAyNgPxFgL93p-J0UsBo6vYRHLVYdSc7QDVe7GAL7forL4VWmVNdrxUCvmE5iDtEjUi7JM9LzzQW-rrRZ8V9MOVFBb-b80Ok9rJNrzZpngszzhVUswutZ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64666ae825.mp4?token=GO6ldPAFtoA6wdqDjmd7xTsDfmE61HplOuhvbGo27J3a8c_I6Kpv2DVDLyCfzpZnxyiQoxV0N8dX5fLE1Anqs0hY52shBzcot7Q_B8B43Y8Y5-m4etgVxn2lKBtqRu0hczTKWmc4f9E3h9LsB4Avrze2fdy9hR-e7w3WoYarmUaU5vBPm4pz2mjXqqT6jzdzNY440f_IzQuwx-t1vEKQAy6eul2BkS0ZAyNgPxFgL93p-J0UsBo6vYRHLVYdSc7QDVe7GAL7forL4VWmVNdrxUCvmE5iDtEjUi7JM9LzzQW-rrRZ8V9MOVFBb-b80Ok9rJNrzZpngszzhVUswutZ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته میشه این شعارها علیه عباس عراقچی توسط تندرو ها داده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67410" target="_blank">📅 10:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67409">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=vH8DZ3Ozuz-jhDetEeQcpixVWwH9Ka3MQlENiWcWoVl4E2cSSRgdsdI2AIju5UQiX28eXTSNMj1ZigRPp1VKsJJOCazDhAU7v82FopWuPM4eTBygdXFUPybsQ6-Se85JjEBCwa3Crwjcbh3IPOeQq-60yy5w5gp_rNb_b0PRebYhz-8NWeVx1zXNWqRDdTyc4Hbny_BQzkMECZyuvcdvWVSpytl_kvsLdsAMrdgsCiuNMxK9LBIlzD6Xg7uaLU_jm2KgsA9truZrhJejmwxSVVEhttSfbOEk9qMsqjxjrl_tA80saVLh6rk6etEQvnJW1g_4A7GVETD4Jhea8ZwEpQgOBaSoIoegyZLjSxQyiufSkBSvkpBxklj5OfVyzz7FaCd3lLzJz4ZGMMidpaelBxu1wO6G_bbsRROve7ErJ_g2xSFpdv6VUWWVkbUMbxYVx5jPg5phSNg7p_vWCDDe71KL8-AMbJLSPQ9Y2lbtJSxIcS5dpI4Vm-jeCzEyUDIbJzKkYQRsdqxFclzJ4Tbb8xhZ3QzXGgSLk7T49hFZIYa_bvREwhgRbIOsiFwc7CJeUrRMctv3kPYcwnyF66wfx8uLtB3tjv4lyOjuWsKTBLidp6qSkI4vY5WcPTza5Am5K0-sOd2SwYEsGH9ZyLrWTwzZysyNVqK7h7DRjWjMytI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=vH8DZ3Ozuz-jhDetEeQcpixVWwH9Ka3MQlENiWcWoVl4E2cSSRgdsdI2AIju5UQiX28eXTSNMj1ZigRPp1VKsJJOCazDhAU7v82FopWuPM4eTBygdXFUPybsQ6-Se85JjEBCwa3Crwjcbh3IPOeQq-60yy5w5gp_rNb_b0PRebYhz-8NWeVx1zXNWqRDdTyc4Hbny_BQzkMECZyuvcdvWVSpytl_kvsLdsAMrdgsCiuNMxK9LBIlzD6Xg7uaLU_jm2KgsA9truZrhJejmwxSVVEhttSfbOEk9qMsqjxjrl_tA80saVLh6rk6etEQvnJW1g_4A7GVETD4Jhea8ZwEpQgOBaSoIoegyZLjSxQyiufSkBSvkpBxklj5OfVyzz7FaCd3lLzJz4ZGMMidpaelBxu1wO6G_bbsRROve7ErJ_g2xSFpdv6VUWWVkbUMbxYVx5jPg5phSNg7p_vWCDDe71KL8-AMbJLSPQ9Y2lbtJSxIcS5dpI4Vm-jeCzEyUDIbJzKkYQRsdqxFclzJ4Tbb8xhZ3QzXGgSLk7T49hFZIYa_bvREwhgRbIOsiFwc7CJeUrRMctv3kPYcwnyF66wfx8uLtB3tjv4lyOjuWsKTBLidp6qSkI4vY5WcPTza5Am5K0-sOd2SwYEsGH9ZyLrWTwzZysyNVqK7h7DRjWjMytI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، کارشناس مسائل فوق استراتژیک:
باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم. کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم. این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67409" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67408">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=VpXQbxBgkNJ51UNFCS-l31ZZi54CpPqZC_hONf710BJGWnN_olc0dS5aiHjv_qMoB10pKYSH9LsKilzIWHX-W5I9mn0OokcEhO4I7ccVArWGWXkVjevOW9dtrupBNe9bPrWCv0YMErwndBpPcsARznxSJIWEbnZ2KKjh2pAUm8XkzE18ZOYHnS10WtLPLsdtAn8qHp6UEp9V5j2IGGcHTMmzp5qN2IPLXa9QCqzdKMgiPmEelINm3MXGA166D_S1POBGb-KPymbPABEUXFCsZDGjkmn0rLGNoJU-QUd2MkxOGpz3AOV5oNQnv2kHAGF2qcp-M8VYps78Iqd_u67CUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=VpXQbxBgkNJ51UNFCS-l31ZZi54CpPqZC_hONf710BJGWnN_olc0dS5aiHjv_qMoB10pKYSH9LsKilzIWHX-W5I9mn0OokcEhO4I7ccVArWGWXkVjevOW9dtrupBNe9bPrWCv0YMErwndBpPcsARznxSJIWEbnZ2KKjh2pAUm8XkzE18ZOYHnS10WtLPLsdtAn8qHp6UEp9V5j2IGGcHTMmzp5qN2IPLXa9QCqzdKMgiPmEelINm3MXGA166D_S1POBGb-KPymbPABEUXFCsZDGjkmn0rLGNoJU-QUd2MkxOGpz3AOV5oNQnv2kHAGF2qcp-M8VYps78Iqd_u67CUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب یک مازندرانی به حضور سعید جلیلی در مراسم تشییع علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67408" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67407">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHdDZVKbv-ILrp2_fl8paRfpojlEWoM2bIGG6nesbVjtxlB_vQeXFqHEefFVCMzgGh9On3CkOugEyr767hywgIJJZ8TtHImMJjEvxleSlu_rYCfroLGn-tMO5bHUVuyiH79j2NVUVdjQEe6ecOQTRvRVqa5_QI7QTpK3yEgPvzez_9gzFfcpBOJpAIUUOqxM5j5ffSz2sOZ3tArbSCLwE_0NR2_QlJPqRRTmclXoLGepfvVgB1dGuu_dQW9Aa1OZQ6qQ1n-nkXgtUJOsubOyROE51K3MfpveA8oH_gk130cmsRAXxwMRh7e0Q4-iLlofmi1oXuCT-r7r1FoKMzEJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
مرکز عملیات تجاری دریایی بریتانیا:
یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
بنا بر اعلام UKMTO، این حمله باعث آتش‌سوزی در سمت چپ کشتی (port side) شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67407" target="_blank">📅 09:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67406">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67406" target="_blank">📅 03:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67404">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dYYJx_fTRErgkXWz45eJSvAKiIesE2OVYm4P_ib5me6cMBZqA3bliI28P4enzjtppgUmet3f6aAXYtZpbP4oyhffGaKtzNaH-VUoUyt13K_nT7eapXm4CnWOL3PDMrRP5ZwNZxa4jEM7HsMkoDvnwVCaePRc1mE7-tyUl5sCrF2UBSEezDejA5iodOlxWYNv5OJpUkKQDva0twHvQeQP6F-0a3wENNAGeemlmDmkwQD1Gv6WixZrfWvtdd7K7e9ROu0bur9z-lJhM2ZG2zaPGMO4nMQh8QklhBdNsuQqy6KfCkO9QCua1RiV2-O970qVOF5V3tU2_35OMtfho2slvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67404" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67403">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVVbc3XzAuUTJtIZFZqYbxSC596KPpu7oEprm2SwoOdB61yGi5mY4Dx7aiq6f7C-QlFl6E__JXcOQGcFCHzelT9iTBTBScoU_vQnrW4sMRimLzkK5gWHAN7nNPtnjQzFcrPMxk3M7Ed2FUBrV6I4p3npDYaqoNH7TIdmO1_e1AJE0d-2ouFj3qkmdmNgtGVcZwmP9jzH2FgWYZTwX0LNAbEErMk1xQzWuqvd9I3PAFjEinB5HKPAO56gn3Cs6eJWhDv6-8KQhy5xg7msMY78JexU7iq93HdkB4jDuAFDS3fgJBsyN0FH0yN6sP4-OwUu2nmCIfZ6WdBTEtk5YHdGIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026
| حذف کریستیانو رونالدو و یاران با شکست مقابل اسپانیا در دقایق پایانی
💔
🇵🇹
پرتغال 0-1 اسپانیا
🇪🇸
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67403" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67402">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1Z3D6uDvAGkTzI7MItqs08nAsolMq_msqCzudSx3SIF0Cnbo7FaDgp1nWNMRWF78Hc5lrC4zfw3Tq3aVCM7P1N9aWVlUko8_T-4rdXOrGL2wvPCTWN-NVqQVrc9ZXPC5rcPqJDX5prv8CpreMUBSQCEZvBLdvyd4nll7ZlA8OO4lR4UWuP3M0rENum51fV53OF-M6Xm5y-u8a6HwIUHXNWPp8oWKOnzSbOCf8sB1_Ffql772jDh9_cPpZvgJhtwWBLnkXSHsx9qz0bJqtYSqzkNuJTWI854EeJjrMVdCeDuTInigZfD6hrg1_fjy2WDCcgbYyAb9sNoV_JOiNfW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ادعای کانال 14 اسرائیل:مجتبی خامنه‌ای در مراسم پدرش حاضر بوده.
🔴
حضور مجتبی در مراسم تشییع تأیید شد
🔴
مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
🔴
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از دانش‌آموزانِ حاضر در جمعیت، تلاش کرد از ردیابی بیومتریک بگریزد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67402" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67401">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=PWIsLvjWWMdpdWScHk-taXXs1-0ZH9SVyPOJxCtElHkljVglGxRrTJ6Cxq1F2GtA92WhCXnOZ8v_bEInqELgcwEe-k_N7pIuuQiYkciLuAm_Xj-wowHorJRX_f_PHCERQSeIAhHbXCa3ezdvdnebgMKzW9xkhBTTpp4wZg9J6GVD8PU6RIw_Xd5iSLt_l0v-B5B4Z3RBNWK6MkLotvsfIkbGfeslUXmqWJTdM01MPYbuvRdau0grIyd0rV4erfoflPlEibhEUUSB8_D6-qY778RZ1rlPN1UToKPCuIb0-NYHZa_Th2O9X5ZfrwUcV2lEFRf7IbMMYOHb3ssDbPHKLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=PWIsLvjWWMdpdWScHk-taXXs1-0ZH9SVyPOJxCtElHkljVglGxRrTJ6Cxq1F2GtA92WhCXnOZ8v_bEInqELgcwEe-k_N7pIuuQiYkciLuAm_Xj-wowHorJRX_f_PHCERQSeIAhHbXCa3ezdvdnebgMKzW9xkhBTTpp4wZg9J6GVD8PU6RIw_Xd5iSLt_l0v-B5B4Z3RBNWK6MkLotvsfIkbGfeslUXmqWJTdM01MPYbuvRdau0grIyd0rV4erfoflPlEibhEUUSB8_D6-qY778RZ1rlPN1UToKPCuIb0-NYHZa_Th2O9X5ZfrwUcV2lEFRf7IbMMYOHb3ssDbPHKLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارها برعلیه پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67401" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67400">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1Ow4Po9KMUybKyVVDgEf4b403jPux85nI6Fy_XrVrAWphCQtUE-Y-5xP0422xmXs6g4AxK9Ut3AtvCkghZxnuLs5z8qA5Kk9_RivwlFKbMdd0HqJ3Fp1oQUn4gvW8QRT7WBBigDQ6JkcM8MM0JMY6owKMXxNv1ocR2lUzOV6eBYqCsJb20vGM9lDPZyG_dZ3WzQQzK2GgCHCMxVycmwermwcT_5S8GjEHWK8KY-fMoN4K-5aEXKhWLuU7Sm4liC6CnYzeyeH9hd6vggqUdV1ADJBbhwPT8qiA5i5ZgB8gVSfxxHLNhQBT5qJwqBsIDbNOhETiWEunCxHC_3lBh6ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اسپانیا یا پرتغال؟ انتخاب با توئه؛ تا از رقیب عقب نیافتادی از تیمت حمایت کن و پلی‌استیشن ببر!
🏆
👇
👇
👇
👇
🔗
همین حالا حمایتت رو از رونالدو یا یامال در لینک زیر اعلام کن و با بازی کردن پلی استیشن برنده شو!
👉
Https://tcup26.com
👉
Https://tcup26.com
📢
این پیام رو برای دوستات بفرست و به این چالش بزرگ دعوتشون کن!
🤩
@telewebionsport</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67400" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=ZWIiyjYTnWXkHSAuuqGnoGEoK3MDdGwj9JLzSCFA0V8QIyH_UYJmPGO0daZPWOpq9-WHWaXAPe92-VEEV7gT2lCrU9q7MyZx0kNlV_Kh-45ySO3H1RNgxWn051VDkSRIwoFdLeOlJ3bE1YlH1EDsMaCmGR0jbuKC7k6eE4AwPqy1OkeZxhUb5HKJXb8_IwlnKjknv9OOusAXE1NP1QITc4FplQopyumytD3N5smG1k2IRCKkD-Dh8fJeyPKt8TE-Vr3FwOdlIR5Z3kWV7Ffu5oUOK5bqA-8qgdMQgLq3BpBNukcjTbiMjrdiKCgovI3dwcLQMDFQoxjJYwbL8jfYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=ZWIiyjYTnWXkHSAuuqGnoGEoK3MDdGwj9JLzSCFA0V8QIyH_UYJmPGO0daZPWOpq9-WHWaXAPe92-VEEV7gT2lCrU9q7MyZx0kNlV_Kh-45ySO3H1RNgxWn051VDkSRIwoFdLeOlJ3bE1YlH1EDsMaCmGR0jbuKC7k6eE4AwPqy1OkeZxhUb5HKJXb8_IwlnKjknv9OOusAXE1NP1QITc4FplQopyumytD3N5smG1k2IRCKkD-Dh8fJeyPKt8TE-Vr3FwOdlIR5Z3kWV7Ffu5oUOK5bqA-8qgdMQgLq3BpBNukcjTbiMjrdiKCgovI3dwcLQMDFQoxjJYwbL8jfYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=NobM9tE8krZE6TxpwY3wNFJSZYYnCMtsn3V1RzK7wn-pW5wpYtucqxcc3Sv-7S5IIf0y1v1xWezvYP4uQP0hLiBhCNiz9QdYacrgusI31AXJo4JQQBdhJM7usRZJfHghUGdVPEBDq_i4e21MOX0iyhVZxAzFJGsEOYSDx2090rTED04oQ9tEqvdAjvEqRWe9warOuPBfvKQBNRDZkH7836VxVQE1VqRF9jA-NmxJ9oroOXDvT2VHQF5Ip8Ft1ru8iMlk_PaPhcm4fv4qucoxArgdtjzVRpFJsrgxHHFPWC-Tkyye77-b11eHqu8M7rSXqCE2-fiUp64kaYAGuUd5KTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=NobM9tE8krZE6TxpwY3wNFJSZYYnCMtsn3V1RzK7wn-pW5wpYtucqxcc3Sv-7S5IIf0y1v1xWezvYP4uQP0hLiBhCNiz9QdYacrgusI31AXJo4JQQBdhJM7usRZJfHghUGdVPEBDq_i4e21MOX0iyhVZxAzFJGsEOYSDx2090rTED04oQ9tEqvdAjvEqRWe9warOuPBfvKQBNRDZkH7836VxVQE1VqRF9jA-NmxJ9oroOXDvT2VHQF5Ip8Ft1ru8iMlk_PaPhcm4fv4qucoxArgdtjzVRpFJsrgxHHFPWC-Tkyye77-b11eHqu8M7rSXqCE2-fiUp64kaYAGuUd5KTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnrLBuSefF6Oq7Jc6N5kzMrleIAjb_CLaOayKiEvzdIqM2z8mYABhlJ0ooDvZSgSEMF4UyRXk0akbPYdoWWC6-2w_0tFJQz4Oz1KT4kYczuBtgvVyvzmFhOl07bGSWBH-bbmmV2OuGBH9YNcnL71WpJh7tzAvfdBDHt6_kQ13W9ulC5vQojeqHIkZu689MqMFSgzr3TGCuZlhg8aakrdX8VL42HfkTAx5RVKni3lxQfUIVtJBhARdNtk5ulW08GYXjdHtcjztvZutxX5mfA1q0N4obDj-mrQ5MPK0DnmWe5PDOCTIQ9RROB2ujOf9YIdmDf4K_Fvsx3jFanN7onrHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjC2DKcoI2DQynG6SCp6Nhx7p5FHE8Y41-bo9kJEBVsYxVVHBYzNP1gxCOTkjPtSIoIFdr_hBrsEBN6rbVL6B7vn2P4Gea1TiwguiIEcFBzhX3BQpjzoxZaVoFrbURw6i8V7B0aZ94Lej6OV7w0YZ3WMcuwz6mfLjKvNMltdT4vGVg2LHzdIqLK3WLCcm_PjUhmDqDFfXsFTosSiMzPWXZG0b9Iqq1dTMZBZS4HXqOZvLPTLkCJtdxD7xvn7At1XcqSPTYcKddjXzVWIKwWd2J3oP6tmJ-Z0rMmo7IIO61Zq4MdEAxOxnu2Of9ztusnZAl1bQxpaWeYd0b0pvCS1Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=GUcv0ZU8XNNF_vvxQ8VTwSx8Eld1-n6nlhIvE3alWVnNFop6IJIjkOb6r0xSCkHAfAABRuiTKHJwIrXmnfTBF1Usgd7eCKEUfjzBG2YhUpqraHaUoVIfcOAIEINR05c8Xu03FvVlwErk50ojFKCc6Z61M0I84AJZSvzOeGoKwAouwZ01DZojf7W-L9VX_4EqgcKvXT8oNp5qY8mrR7pH7fe6fDiFN8wLo10KtHoMJiLolQ67SVwg67zlt1lEQI8DOCRU0AD9DWUtiSOQzlgRk5PVYUvShQPsiPdIhdzoyHk8U-7PMMFmdACTHlKC5-Yf52mZb4cYsTaku-bk5Z_36g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=GUcv0ZU8XNNF_vvxQ8VTwSx8Eld1-n6nlhIvE3alWVnNFop6IJIjkOb6r0xSCkHAfAABRuiTKHJwIrXmnfTBF1Usgd7eCKEUfjzBG2YhUpqraHaUoVIfcOAIEINR05c8Xu03FvVlwErk50ojFKCc6Z61M0I84AJZSvzOeGoKwAouwZ01DZojf7W-L9VX_4EqgcKvXT8oNp5qY8mrR7pH7fe6fDiFN8wLo10KtHoMJiLolQ67SVwg67zlt1lEQI8DOCRU0AD9DWUtiSOQzlgRk5PVYUvShQPsiPdIhdzoyHk8U-7PMMFmdACTHlKC5-Yf52mZb4cYsTaku-bk5Z_36g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=tdNfo787KRFdfBvkOU2kEH-3s1LVl-ZH8W17psf-Mf6kSkwVx9cNJi0nY6uK0hdVEzXLwDgPgSk1kiSzcsnpYpkhMMsnMwpfpk5PHuZUGpcMjuoDkIQzmNnvXtWgRb-IWK1BKxO77rBy6RjyUzl-QylgwxOTg1WutQWYqIXknAXsGDCrrzFwm05Np1pebPVfVODAm1x_PxRU3T0IZICGA48psmbddPslhixOa9iRaaUCn_Vvv3idU8bCjXs69zotEG5-Roe-e09mJiPT013b4PU92_fInmO6MiVbO2e1qjMD-QTjfRjfkPBNgcsWeGrd5q3AyjFapfX-VGl5vEPjgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=tdNfo787KRFdfBvkOU2kEH-3s1LVl-ZH8W17psf-Mf6kSkwVx9cNJi0nY6uK0hdVEzXLwDgPgSk1kiSzcsnpYpkhMMsnMwpfpk5PHuZUGpcMjuoDkIQzmNnvXtWgRb-IWK1BKxO77rBy6RjyUzl-QylgwxOTg1WutQWYqIXknAXsGDCrrzFwm05Np1pebPVfVODAm1x_PxRU3T0IZICGA48psmbddPslhixOa9iRaaUCn_Vvv3idU8bCjXs69zotEG5-Roe-e09mJiPT013b4PU92_fInmO6MiVbO2e1qjMD-QTjfRjfkPBNgcsWeGrd5q3AyjFapfX-VGl5vEPjgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
می‌شنوم آنها میگویند که«بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=P37mJKEW9zjpN98z529P5X_v-iVS-AGykuMC6DJ4K3plYc43au8CQvwAAGgu_6SPhPj96C5d0SybXdpum0HJyUVTPbqcSR6bg_Sfws1PyKn8n561S17s4q4IqQP8h5Sx3Xc2mm_9iXs5uO8Pv_B1AfQN-iHdunMxG8A-gJewMjRFFFEO8kpbNjZhu1uDkqsxKJcHOqNCPaV0-KuTkWj4l0QpqdG-rlI93e6TzhuiSy_ZPxlaDG1MyO26ijknQ_jOrp13pFnTsRTdzniS8X00og66D0tPt0O56ZXnsg_IQwjDOXGQqNr2-_HnO6ETqfIZpzxzdIEiNT5CIUxMJet4rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=P37mJKEW9zjpN98z529P5X_v-iVS-AGykuMC6DJ4K3plYc43au8CQvwAAGgu_6SPhPj96C5d0SybXdpum0HJyUVTPbqcSR6bg_Sfws1PyKn8n561S17s4q4IqQP8h5Sx3Xc2mm_9iXs5uO8Pv_B1AfQN-iHdunMxG8A-gJewMjRFFFEO8kpbNjZhu1uDkqsxKJcHOqNCPaV0-KuTkWj4l0QpqdG-rlI93e6TzhuiSy_ZPxlaDG1MyO26ijknQ_jOrp13pFnTsRTdzniS8X00og66D0tPt0O56ZXnsg_IQwjDOXGQqNr2-_HnO6ETqfIZpzxzdIEiNT5CIUxMJet4rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح عقل عرزشی رو ببین
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AH_U7rJNN0jVz9JTEF4qg1k7nBTYs0q1KEyox8f5e_mi4BbseZWjBFeJSZFf9E7QAiXVUNqYhEd0j-BUpmFC6DBTHSORbouK4j0VUViBOwhrL6fgpo6zM5iYgmyeZvdnxCjfgKTUZ0tLfvucfXRymw2bSUahk9sGhqnx6qSkU-6YHQQbqlWdlF8uf4vmlVtgj7_tCKtGgBHK8wfC4hF2SwGBr639qBa9NOi1jxgVGV3M6SEpkj4tfcUdFB7QQEQ4ORK2gDfubYOJb3kCIWGRchTQtehuQivZFIeu3b0mrFqOprNseTOOaLuRyh1I24Vd81cfOedzXg7SyQziJWiSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7ByN59jUB_6F2L_H-EW-R4KdKtc5yQcIguBLIYFehuNMgw2gxUEMzpF7Kj4QCmV4y6VHYl8hREr4tYiQ4n-gNBs8lAuG661aNYofvrZ1EeHKBd9K-DnOUorpe0F3-g4p6t7zbYxldLHBKQBlrAQileliluFiLkmfHWFQG3sIqody5HISGsQ0g8eDzz6-CdKKQjwDJZPXOjTZb3TWNLZDSBm4MWUGKt_64aff0a92Sa8OBd3UaZD3PGqDVrhbcKF7Tt4bT_N5k9870xTgOrIKS2ZX52hsTYBQwRG1LL_GYl54xdT-mSwpWhsQSmWO622hlCefF57cZyGDxxZjwGAtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=iCbGOXg95rhERuswNG1VbqKYrBTzeaUUawSGy_z5qqDjZNymV_cRmkoXJvOI7aAumZxGwWvYYzJJtCvDA8110IaRyBelmjj5IOXBK5tfxz2eOTwNFgWcMUXE9hSosdXZzfZJiBjFCauIoksgEzik9KhSNuphaDeUyeLx5uGT92fumIpALWDFwfO_XSudBZE9apFOZEpSbswABlKoTutrsu3wBk800uMIEPRy_vTUX2o5tvZRG7i2DuZYNYSoVYkbVTsOMIENnWkN1JAukbuTwniGa4ER590ILoR-qtQuVq3YXfKpYeQZyUfMFepXH-pg6mW3f7Fo0FgESg_8xqqx6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=iCbGOXg95rhERuswNG1VbqKYrBTzeaUUawSGy_z5qqDjZNymV_cRmkoXJvOI7aAumZxGwWvYYzJJtCvDA8110IaRyBelmjj5IOXBK5tfxz2eOTwNFgWcMUXE9hSosdXZzfZJiBjFCauIoksgEzik9KhSNuphaDeUyeLx5uGT92fumIpALWDFwfO_XSudBZE9apFOZEpSbswABlKoTutrsu3wBk800uMIEPRy_vTUX2o5tvZRG7i2DuZYNYSoVYkbVTsOMIENnWkN1JAukbuTwniGa4ER590ILoR-qtQuVq3YXfKpYeQZyUfMFepXH-pg6mW3f7Fo0FgESg_8xqqx6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=mt7mm7Cv8WkxJO_oAGhRSLOpvbqm5_XbpbCYYCcC071v5X7s15oNz_Y5YyVOnH1J1fZfkv2cja_Vg7_G-MXYw3F0GP9CduSJ4-rYn_6zx1WgBObeJHdRVA_KzGBKJRGAO3GKJvObaRignfuaxgYgSQGwZleY9PsYxQX4MJqkxZzpCoVxXaWGEuDvwJtLCmyieejsm6xL9QpT6nkJ6cROoTjqNqXSPHurGkkE5lwYbKJTtRzVHbbTxdWneD8msOpIVt7DAc6K19yyBJMx44rN2JvaU5ptt2pkNUrOj7X7f6Gmqy57_jRFB4WicrNUWrTFgFGBotHX4xTk9cYqbSs60A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=mt7mm7Cv8WkxJO_oAGhRSLOpvbqm5_XbpbCYYCcC071v5X7s15oNz_Y5YyVOnH1J1fZfkv2cja_Vg7_G-MXYw3F0GP9CduSJ4-rYn_6zx1WgBObeJHdRVA_KzGBKJRGAO3GKJvObaRignfuaxgYgSQGwZleY9PsYxQX4MJqkxZzpCoVxXaWGEuDvwJtLCmyieejsm6xL9QpT6nkJ6cROoTjqNqXSPHurGkkE5lwYbKJTtRzVHbbTxdWneD8msOpIVt7DAc6K19yyBJMx44rN2JvaU5ptt2pkNUrOj7X7f6Gmqy57_jRFB4WicrNUWrTFgFGBotHX4xTk9cYqbSs60A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=ipSilxh4l2hfN3-OUmy-BiUyfagWl49WyIlkolIfqJFykf-YBogzyntYd6ZyF1m-j2wQyELstoKoeBDS7yojJ6AXxIHEBFLTZ2RA7nLw8yBufjAwMbLr5PXHyobh6kTszD9Ga5PaxX3E3DBhkU1LagyqK_bFyTRKwT8OO9pc6Kf4fJKYT6g6eMA6oIORp7g2iDY8EMRuX2_0qhPPC4Dugdcshy0DvsbwlVBnC5Nb6khRqte3TpBY7u0lGJx6AKAbB_zcZ5IgsW9SnkJSEzEjWusay-6ihcMELO_S0-JI7eTnZnUN1BDYE8Uyjdr7PzzsuWRJp1iHyWK7rDjpJ4nflQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=ipSilxh4l2hfN3-OUmy-BiUyfagWl49WyIlkolIfqJFykf-YBogzyntYd6ZyF1m-j2wQyELstoKoeBDS7yojJ6AXxIHEBFLTZ2RA7nLw8yBufjAwMbLr5PXHyobh6kTszD9Ga5PaxX3E3DBhkU1LagyqK_bFyTRKwT8OO9pc6Kf4fJKYT6g6eMA6oIORp7g2iDY8EMRuX2_0qhPPC4Dugdcshy0DvsbwlVBnC5Nb6khRqte3TpBY7u0lGJx6AKAbB_zcZ5IgsW9SnkJSEzEjWusay-6ihcMELO_S0-JI7eTnZnUN1BDYE8Uyjdr7PzzsuWRJp1iHyWK7rDjpJ4nflQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=gx-nMCOVhQiqVxqwy05hSsPVDxBUXtJHEi8NzW4QKj0YP9JzSO1zKYf12bZ_OBf0K94vGYsHT0SP3So1oMH-yEYV_9zfbI18dek8TD1GB-qBaxHQ36yCilavd9EGnfmoRtxSMlpkpsg4I2I9W4qL-dP42tdN77W9KM4bWgSno8ONkgEzHO-5KUUZa-V8EJJCE5VzwRB6xbbqqMtwaZdsUf6cRrYew4y7IHiiF9WaODVkLC9Vz2alJj2owgqI8HunZkLdlfsOKxCq0f0-kRy0SCpR4wSQ8CdpUsNHr7leeFQKhw_BE93mE43ePuCK-zBt6CxF0srTsI7yrcqtJsHRQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=gx-nMCOVhQiqVxqwy05hSsPVDxBUXtJHEi8NzW4QKj0YP9JzSO1zKYf12bZ_OBf0K94vGYsHT0SP3So1oMH-yEYV_9zfbI18dek8TD1GB-qBaxHQ36yCilavd9EGnfmoRtxSMlpkpsg4I2I9W4qL-dP42tdN77W9KM4bWgSno8ONkgEzHO-5KUUZa-V8EJJCE5VzwRB6xbbqqMtwaZdsUf6cRrYew4y7IHiiF9WaODVkLC9Vz2alJj2owgqI8HunZkLdlfsOKxCq0f0-kRy0SCpR4wSQ8CdpUsNHr7leeFQKhw_BE93mE43ePuCK-zBt6CxF0srTsI7yrcqtJsHRQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=ZTfCfJziAxmtaKBVgXJM6VNDLvk5nM3-L0qc4x8loM-PHIZBZetdCFXcUQ04mUGr7iJgdbUCpJQiVLK6BOGlNF9hZAdmnRpY6htNhY3wm_qgKmHT3G5TK7LS8JpXLHVfGipb1zjNvirju0Fk9B4Y31oQRPa0IESk4caVgT-vY8LqmwUdnSIL9RGCH0d9nw14dZ14-25RktUpmSXnN8eJOGnz_0O35uH8MdsZf8e9plKbQZgYc8SJ9aPdlCLXLAFWBhWOMzgXCjXg-XW0J-i6c25WbtMn0ow-KLK6ph7_xbDHISTn4s3nG8gi4npR5pHU7N_h8LnyQMdF1DaqtyzgFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=ZTfCfJziAxmtaKBVgXJM6VNDLvk5nM3-L0qc4x8loM-PHIZBZetdCFXcUQ04mUGr7iJgdbUCpJQiVLK6BOGlNF9hZAdmnRpY6htNhY3wm_qgKmHT3G5TK7LS8JpXLHVfGipb1zjNvirju0Fk9B4Y31oQRPa0IESk4caVgT-vY8LqmwUdnSIL9RGCH0d9nw14dZ14-25RktUpmSXnN8eJOGnz_0O35uH8MdsZf8e9plKbQZgYc8SJ9aPdlCLXLAFWBhWOMzgXCjXg-XW0J-i6c25WbtMn0ow-KLK6ph7_xbDHISTn4s3nG8gi4npR5pHU7N_h8LnyQMdF1DaqtyzgFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=EitIVzKhmOTa4ZjQi6Gatd5ZpSBuKAaQo821b9tR_4BfJgHO37mSSnd781-VoZ9Wnrcmf3x3l99buXVl5vjqG_4nn6FDg2UdYxF_wabKLpxIK1-tN5vYHOFniurD49AzZ4O3wVS2YtZktq_dvJz9tS-WTWvvOAaWqbblsNRmLdWJl7K99Ny7LFxFTIriZ4XKtIh9OdNibvkO0b4Bq1VKD77U73QUiPXHNUHKIlLJaJhN_30yYlWJXLacx1zdba5OW9FzNklUPq5neYRAFML4iT9QJxlbg9qrgcrbLhdVl7qSOgxjs8dQms1_oA7TbDFfF2RpJ6Yc_27DZXXGYFkfmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=EitIVzKhmOTa4ZjQi6Gatd5ZpSBuKAaQo821b9tR_4BfJgHO37mSSnd781-VoZ9Wnrcmf3x3l99buXVl5vjqG_4nn6FDg2UdYxF_wabKLpxIK1-tN5vYHOFniurD49AzZ4O3wVS2YtZktq_dvJz9tS-WTWvvOAaWqbblsNRmLdWJl7K99Ny7LFxFTIriZ4XKtIh9OdNibvkO0b4Bq1VKD77U73QUiPXHNUHKIlLJaJhN_30yYlWJXLacx1zdba5OW9FzNklUPq5neYRAFML4iT9QJxlbg9qrgcrbLhdVl7qSOgxjs8dQms1_oA7TbDFfF2RpJ6Yc_27DZXXGYFkfmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=muSBg17Rx6sW8DHvNk2_Hk4DHej7HQCp2UD7KCejftzeblaDw1VrEKHwggbHk12GLjbiA37NVEuhCDX2VTbqhP07_vSX3R68_3I7y30LfKSHxMkeDtFUIeBgBOs9b99WwtZMpNcjr7HMC8NKfJlRKAwoicbo2HVm6vmlndbW8QMRXN2sgbiYaw8w89dVFp7Y_46ES_d2qV1svk1heTIE4lNJG25gH8ReBYZ5CV8CFFHs34h_LZgjtpvMqcjuc-hljiVnT_-AM-DWFHYxQhFxBqvzSAf7fmYxrvwBBESC8oChQzDOQ3oEkhKGbKQnPToP7Z383F8u4egQur_gajurMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=muSBg17Rx6sW8DHvNk2_Hk4DHej7HQCp2UD7KCejftzeblaDw1VrEKHwggbHk12GLjbiA37NVEuhCDX2VTbqhP07_vSX3R68_3I7y30LfKSHxMkeDtFUIeBgBOs9b99WwtZMpNcjr7HMC8NKfJlRKAwoicbo2HVm6vmlndbW8QMRXN2sgbiYaw8w89dVFp7Y_46ES_d2qV1svk1heTIE4lNJG25gH8ReBYZ5CV8CFFHs34h_LZgjtpvMqcjuc-hljiVnT_-AM-DWFHYxQhFxBqvzSAf7fmYxrvwBBESC8oChQzDOQ3oEkhKGbKQnPToP7Z383F8u4egQur_gajurMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=V_eZ1WosTo9-0vEzziuqZPRzdf7K6-aK-DZcVnMqGeaSPa-G-yM7nZg6FZlh4RNx0eartpSwF677wj3u6nA6rSpRvN_42G-imduyV_PXAZha1E73U317iLhS4PUqf_C2qc_aQ5Z4t0V8zYObIChsmz2aINv-VCnJbm-XwrQCbhCQAASRvbvKhjb_tjHnMBKUUIN2Rz2T7_WQImcVjAdoCtND_fK-WJEySOv9kSNEOa8W0uCxnZVFxgBerx_MONVibztOgWr4fuNYd2or1RH7qR7gvbKLhOD_0JN4n0ktOybydo4S-b4esGKpY3QWQvFe5AHq5_CQ3xbyruZ70UEixQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=V_eZ1WosTo9-0vEzziuqZPRzdf7K6-aK-DZcVnMqGeaSPa-G-yM7nZg6FZlh4RNx0eartpSwF677wj3u6nA6rSpRvN_42G-imduyV_PXAZha1E73U317iLhS4PUqf_C2qc_aQ5Z4t0V8zYObIChsmz2aINv-VCnJbm-XwrQCbhCQAASRvbvKhjb_tjHnMBKUUIN2Rz2T7_WQImcVjAdoCtND_fK-WJEySOv9kSNEOa8W0uCxnZVFxgBerx_MONVibztOgWr4fuNYd2or1RH7qR7gvbKLhOD_0JN4n0ktOybydo4S-b4esGKpY3QWQvFe5AHq5_CQ3xbyruZ70UEixQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=SvVPVpeTHy-bnTLYVcX4ftH-GwMJv7LIQH7DQ7BEJXJLzkG6s5X-OGrBuQV7cVBcWCfSsjponEmrSSbN7trq5R6ZCdN3Haj55ppuRR9Ob1-hvSvouaQbvXOfIDuPbuBxl0wXRYxW8vR4cy8Zug-WoTlB-LFIvFwKnio3-7hHLwvC9YkJFVdvzgaZV_gNpV8zjAgUxxppGnTtlkeJaRmysbQRBvPga8xNfEIyDBrMmv_-GdIWFZKxUNlkH9rEDbI8IfEQEhEQtPOLGQwMtEbxhxprkYBTn5ewjvPyBvUmrPEu0SHeaq5d1uOje8D4Chf53_XnSgbczNkwTS_DapWQMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=SvVPVpeTHy-bnTLYVcX4ftH-GwMJv7LIQH7DQ7BEJXJLzkG6s5X-OGrBuQV7cVBcWCfSsjponEmrSSbN7trq5R6ZCdN3Haj55ppuRR9Ob1-hvSvouaQbvXOfIDuPbuBxl0wXRYxW8vR4cy8Zug-WoTlB-LFIvFwKnio3-7hHLwvC9YkJFVdvzgaZV_gNpV8zjAgUxxppGnTtlkeJaRmysbQRBvPga8xNfEIyDBrMmv_-GdIWFZKxUNlkH9rEDbI8IfEQEhEQtPOLGQwMtEbxhxprkYBTn5ewjvPyBvUmrPEu0SHeaq5d1uOje8D4Chf53_XnSgbczNkwTS_DapWQMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=Md1-rrBzFh5qT5Dn5zVw8SERUJ7xHCYrZfs3VW-wd1iHca_lWTvGGIidNfjVX9aLQ7xUte29umcvxXrPyp8nDzb4hbwRdKPNroNvGRTxIo6BilvhfPUtbU-9ohdjebs355pMyTUC_icri0gyEoIQtaeh-a8oszI8iPFxqkZdI72Ec93uuDGZHWAZoRyoYvhMXDXuT-H_guK6V-NB2TYLpUGdl7gF5rsZ3oZcNR8aTVZYEhCfT8e3RiGC-W6x7xRzlUDq0TyRDNQWQefWbUH1VgxoRAFZuAhHXNPyYbRp8pkjFJJwqcI12VaEgPvEBhCGJajesUyiT_VlDrcPl3ySJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=Md1-rrBzFh5qT5Dn5zVw8SERUJ7xHCYrZfs3VW-wd1iHca_lWTvGGIidNfjVX9aLQ7xUte29umcvxXrPyp8nDzb4hbwRdKPNroNvGRTxIo6BilvhfPUtbU-9ohdjebs355pMyTUC_icri0gyEoIQtaeh-a8oszI8iPFxqkZdI72Ec93uuDGZHWAZoRyoYvhMXDXuT-H_guK6V-NB2TYLpUGdl7gF5rsZ3oZcNR8aTVZYEhCfT8e3RiGC-W6x7xRzlUDq0TyRDNQWQefWbUH1VgxoRAFZuAhHXNPyYbRp8pkjFJJwqcI12VaEgPvEBhCGJajesUyiT_VlDrcPl3ySJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=T3rzK8gbZ8RWSDnfScMkegcbl4fnCyctlBVtJx7tAmlymGvjZRZMwM5rGsC7Vh8kDbw7FW98-tesYWCsrcVrOj7ysRuCa_H5GbwD3CBJlzhZvm4Is_-BmUQvMXBTsohdrTWlRdIl5o_zEX3zv6mq6qTkx1_JSvGHDMBGSs_bMgMRYOdDZluEYj5J5JqK_x11NtUIDxzld8xF-MH8BRjtpi5xmgJHlxAtqmiRNLdkGnRFk9bjfaeDUUUXlccJ8CVHcIvinrdgf3FZle_rKXkquWqlLmK9g7WD24ovyYwrKbt_niN98yuZYGcKO9stKaelUqpqPzIYStg7r1GACSRwPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=T3rzK8gbZ8RWSDnfScMkegcbl4fnCyctlBVtJx7tAmlymGvjZRZMwM5rGsC7Vh8kDbw7FW98-tesYWCsrcVrOj7ysRuCa_H5GbwD3CBJlzhZvm4Is_-BmUQvMXBTsohdrTWlRdIl5o_zEX3zv6mq6qTkx1_JSvGHDMBGSs_bMgMRYOdDZluEYj5J5JqK_x11NtUIDxzld8xF-MH8BRjtpi5xmgJHlxAtqmiRNLdkGnRFk9bjfaeDUUUXlccJ8CVHcIvinrdgf3FZle_rKXkquWqlLmK9g7WD24ovyYwrKbt_niN98yuZYGcKO9stKaelUqpqPzIYStg7r1GACSRwPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=GYMRXGD_SgNiuGIG7MWH3Ayrf3Pg32u6rbtEsXyPCzeNtD-zbaa6LZIob24joMSlUrr8JjYcMOK4_bP7CB23c-qPUtdMd4N60_RlNEdPdlxl_AeHVZHvX5OKv7zGy6LbQg1WXm5xqTbVYKPzSKLEqFrpL1FFn1xDuI76Hg9QpnkckWxbYplHRxnitm721zApzhIbEdkTDE8GMXWTA7JG1u8dUVXMObIKS3r309Sifk5fg6Sn4PJyEGwgCFi94p-lCca3k_dlOvvQADzsFhlDGDyLbns655WPyI7qbGAFDTC2Z61JgWAym7OiP2xT7qSR64-a-0RcsMyQRkDpYJZI6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=GYMRXGD_SgNiuGIG7MWH3Ayrf3Pg32u6rbtEsXyPCzeNtD-zbaa6LZIob24joMSlUrr8JjYcMOK4_bP7CB23c-qPUtdMd4N60_RlNEdPdlxl_AeHVZHvX5OKv7zGy6LbQg1WXm5xqTbVYKPzSKLEqFrpL1FFn1xDuI76Hg9QpnkckWxbYplHRxnitm721zApzhIbEdkTDE8GMXWTA7JG1u8dUVXMObIKS3r309Sifk5fg6Sn4PJyEGwgCFi94p-lCca3k_dlOvvQADzsFhlDGDyLbns655WPyI7qbGAFDTC2Z61JgWAym7OiP2xT7qSR64-a-0RcsMyQRkDpYJZI6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqSNlO5HvKmOJ6UHJoBmG_fk0eXDHkMZfBn_FECW-cCoSuJYamL4AA3vBji-SQ0j3aCGrxvUtgUkAgbmnAxFLL_UqXBJFcmL7Z45IEVgB2b1q7XUKJNX0eIy3GaTNBJwiSBY0Ol4bV7wmGrOqOq4j0aitz_L7y83yHIem9-YZaD7w4OEs0bLpCgMBgG0wOTezsyQzLmLPl1RsU_GoLWfzQ_xnxQY0DkpA-f4x3qqFQKAiQOGOrmnbR60w-BGgk9-AjGpeHe4UcUNVDG08JYUoHdzR86yRbMQbAW1yxwLnDr3auaIpicGYwdX10DMn03YMUdp8-F6d2JKXNnpuujUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI8Kc4y8EYuC98DcTibh1Ny7myFg7zrcU0P06ZS81c_L0aUdDIByrFqv_e1Lm5Te4EKPMhfpJ4gi4Yri2WWUooKJtiVK_NIDffCuTr5ZHjsHwdlbOHr2SCdIBDeNUKN5pPRnumHQQQXdA-NmYkQV2EkpvEdLaQGauzGdPrnliRz25Jj-2by5oceWMHqyWgmohuoYIf7GArI63xiFzpu7PBxxd-yA_zb5tHFlQlC8zMidEGlBJTi5T0tgTjJXFquleR-ChWmdhl_IPsexXWzG_8Jj44n9TXOwwrZIEJ887V7Xe2_gLh50GdPK__pcPoEMlh_k_MTtLayUOQ7yCWKa6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGLReDa09jIf74300rioulmtO47wV43nzND9D_HXnQdkNzKjLJihUz0Vs6ECEUH9tnQuTOEKaYihZVAvBiU_FbeTDdq3Uk0ujoGnv_xX_f7B_bEajg5EI9Y8dKllPJWaKH7jQngQIx33IMw0f-q-84vwQK1eAqbA-tRxL_POlPmumg5pGuh7_Tnh_UcFr82cgM8Wvdfkmv7Z4dliJIdWPi8Ebsb0thjLIYolu5ElAl9Lr0Jlp7K3_veWjwHRt8sb6gyx8mu3y5Lu9PlVSU63mKizNcamh8dZH2IL2HN7cBoqLlCRuCxgY5-_5KT4_6uxmAFvmAxuDxh6s5JYuF3PpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
