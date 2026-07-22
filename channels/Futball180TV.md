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
<img src="https://cdn5.telesco.pe/file/YDgGIKeUES_mT1P4WbRXqIWyVu2jye9MQxJXLTgqJkjohUcaDUc4z1Bghr96k_6trDA9IWW6tq4nYtIy2_0s7579sc4j0aI1vds7jbHKg0AM1eEtEGZKHdTsgZk6aUSSafK6pJKtiA76qG0wSP3NOF8nFiWSo1gCUDFU5ImKjpiZPVcAC8UQGjnPEy2OEReTvd6wZWXvXJerl7sTpqP-1jwHXjgENYE_8fao6po0pzRneDXkdxwofxVHfCskWG9fDgbd165C7fxLXXoe_RVVzlfsOQCaHrBG8kiXGVYp-EMY1mKcC0w46on4BrcjjCMkXmTtGPNkTHgoobanHdzhLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 543K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 18:01:49</div>
<hr>

<div class="tg-post" id="msg-101571">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY_sKteO_GIJdb0JsDS759bK9ve-acZH1oy-GGW2YHjDqRE-NlXo0jBGyHJjupSvrX1HD2Z3StgL3o87M2WEB6EA5wB2yhnWLQP26eSWDON1jGJr5PvFlHyoDBpclAwVd8VbrjaSxRYBkB1v0iQT9HJhvwRKcaiSJk6TPQvwOn9YXsgdIb6hZ1ltToODOrlg6cbVIqGo6qdxyloGOqqVdQmlqgnsD5hXIYRUlUjYiSlqYY1ICBsvJW6E-fifXxEz0PS9D25jRNSWa8m71mHmsGwtwrjix5B3GYKQR9rFw2FMBJ9ofgPt9MINqfnDSWUJrP0HrbvK1vwKYeOEer1ynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول و آرسنال درحال رقابت شدید برای جذب بردلی‌بارکولا هستند. حداقل رقم پیشنهادی به پاری‌سن‌ژرمن حدود ۱۰۰ میلیون یورو تخمین زده شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/101571" target="_blank">📅 17:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101570">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb17487185.mp4?token=R7lIVu1DCdJX5iKG7lxCqQOmLkSGscLyFvlfmJl_qhCGDIYblIgcGZ5HylB6Efmilw4gtxe0Nz-8wJP-Km5N6XTdTdokbygHekcjV_g015ikI4EVRt2IMKbE_8Or_0hEDgERJehe_SpqQYmL_CNTHANdX8OC1oo8vGo5RXO_fAcPSwyIflPFPgwAlGr7j-xJn6mDK-WBxfPx7eOmBGdk2wH8zfQ_p0UfmjHyhEc57DhAqm5sq8zcCsZeXbUXVhU8RfAwAtyhHZfimy4RxhYIFhKYheXGJiYcr6jA3MbkTfUlCPn3Q3Xs8EgmhNubUBVUKFMOJiuQfjLrl6VwoiJG0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb17487185.mp4?token=R7lIVu1DCdJX5iKG7lxCqQOmLkSGscLyFvlfmJl_qhCGDIYblIgcGZ5HylB6Efmilw4gtxe0Nz-8wJP-Km5N6XTdTdokbygHekcjV_g015ikI4EVRt2IMKbE_8Or_0hEDgERJehe_SpqQYmL_CNTHANdX8OC1oo8vGo5RXO_fAcPSwyIflPFPgwAlGr7j-xJn6mDK-WBxfPx7eOmBGdk2wH8zfQ_p0UfmjHyhEc57DhAqm5sq8zcCsZeXbUXVhU8RfAwAtyhHZfimy4RxhYIFhKYheXGJiYcr6jA3MbkTfUlCPn3Q3Xs8EgmhNubUBVUKFMOJiuQfjLrl6VwoiJG0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزهای اسطوره فران‌تورس ستاره فعلی اسپانیا در فصل گذشته برای بارسلونا
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/Futball180TV/101570" target="_blank">📅 17:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101569">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=Xf1riJsJfvHyrseNjwAa4crzaUTelNts0oTOXQE5qgIBxp4pw7fLe2uzr39-6w3wFRNaJuixUDVywdWIQk9Ixr913UaqXkbnvQVWn_fNyN7qNJtHFjEnq3ebuoQ0C0S6oiNiP4jU9vrBzkT0YsIkTVSxUqyAJoEnGbPdqx3R8RMNJgcW3WAHihThnc0RSaHQrgKsRhRXHy_nK7BP0_LcLC87DHlexp4bKfi4X4JfPmbkXufaBZ0HK87bBvMQSO070nAYttNwnBKipASSF49OoyYf85s2eYagKdEzFRSH5BQCQGfjMhBzHZdXJ1mnC_HO2DqZldaDNhbk8neIArtluQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=Xf1riJsJfvHyrseNjwAa4crzaUTelNts0oTOXQE5qgIBxp4pw7fLe2uzr39-6w3wFRNaJuixUDVywdWIQk9Ixr913UaqXkbnvQVWn_fNyN7qNJtHFjEnq3ebuoQ0C0S6oiNiP4jU9vrBzkT0YsIkTVSxUqyAJoEnGbPdqx3R8RMNJgcW3WAHihThnc0RSaHQrgKsRhRXHy_nK7BP0_LcLC87DHlexp4bKfi4X4JfPmbkXufaBZ0HK87bBvMQSO070nAYttNwnBKipASSF49OoyYf85s2eYagKdEzFRSH5BQCQGfjMhBzHZdXJ1mnC_HO2DqZldaDNhbk8neIArtluQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
دسته‌گل استاد فران‌تورس در حین حمل مینی کاپ اهدایی جام‌جهانی از سوی فیفا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/101569" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101568">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8X3oPuD-JOi123iFE_6WNOZXhZ96ccVtDHUTk44_7j4S6g6OOBLevbhR4pWcydCqTIuhP3G1vjxKWLoMDdFZJe_xAlZPaTkf0nC7p3s6eatDoC9tthBY-8C0fzNgys0B7NSpNNBrSeviwQUqoBw2Tl5rYCyQgoZVWfH9w5XrG83ItZ7-le7EpkBQmnK2diFopB-iB5pikw1KYt_Di6dfl7pOhg-Op9EoCecagOAYCVL8ACWhbKSAPgaa6gN6xKGqEwLeQpD0D-ZANil3y2v2Mh9w4le_BUqax7gRi_AWC5IU7FN-sb1YGX_ePxrpPAdS0FjHN5PKAsRBORmKKrDoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/Futball180TV/101568" target="_blank">📅 17:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101567">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=ERAvo72M2FE8nbTErnDw28NMc6cu1I0UNF1EeJqSVxTXxoLLufYzWmYmAeoAdfqH1wmBgzlpiIUeL5QoOnLZn2ttbHx-l52QJfjhaGpwe2wm_8J30Zi7O3xTFGLeVw_oCLpZZAOwLpunnYY0tNC374Y7azugcEEdMWhNj5VwYyaxsMTFcOJp5XX-Amn6md1bbeRED036dNHreerzo7om05y21x0EqrLsVw-G9v8yJbyHhIDMwaFDbHdZ7FdBbEwgmz-KuA4S7XhBCBqsP7aIhKo3BBav6TpYRTHHh1OBsidkBF2RwpYYIvUyCbM7jW_HYBTK9h2NmJ5lHmtBy3bqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=ERAvo72M2FE8nbTErnDw28NMc6cu1I0UNF1EeJqSVxTXxoLLufYzWmYmAeoAdfqH1wmBgzlpiIUeL5QoOnLZn2ttbHx-l52QJfjhaGpwe2wm_8J30Zi7O3xTFGLeVw_oCLpZZAOwLpunnYY0tNC374Y7azugcEEdMWhNj5VwYyaxsMTFcOJp5XX-Amn6md1bbeRED036dNHreerzo7om05y21x0EqrLsVw-G9v8yJbyHhIDMwaFDbHdZ7FdBbEwgmz-KuA4S7XhBCBqsP7aIhKo3BBav6TpYRTHHh1OBsidkBF2RwpYYIvUyCbM7jW_HYBTK9h2NmJ5lHmtBy3bqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/101567" target="_blank">📅 17:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101566">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=c_7EnTaFyMi3n8iqdYvBQcHSfxK7s84JTeGODL9szAqyv5DFZrIqK9h6npdOoOXoiDepXXPc-LfNzuoFsDT67N1HNAIOg9THN9apOH9YLbPIaTAKkPlabI0N5_FSLOVjk0wQdFDwJtAgJAGaet3O5O3zZ7wlTcV8Vempi_UohEhubZuur1GwVEkA1_TMpsqSsIt_aWDnSpi2gzTibumZ3ZbCyVQxMVzhEY5x11zAfY3UHTfcAp2cDFc05O4RNoN9e8MrfHKyiVWKDrPK_z5t_xWM0ao_86silveRyUOaFC1iE-dy5WtkGTV8P02NAMC3X1mK-sNbLNMI68PGp_B8C7s_Xxa4in1b4whwUmD0I-TGIdj3LN4lssZ70edPCHGY_PGhhL-0JBXiz8dGPWXkHbLuCSz7Aeq3zI0SBXPKFjGgOevsi8Yi-74w38sW958YvUhdovCZUcqhaZDbsq8uZhbAUklHT9IWoLdyTGncd9E03huL-3EoOuyQGandJ3lXtlWjrhD0sholrWn1F5r__R8bx1gkjjnV0S85zPmeSbYm3yTX2zWQhaBY9qC2jsEq-UK5W2W8CRSr5ZTMBUEElpMDBMOhjQzDYE4GGauAaveotcc96wELPsA2AlcWz4I2MDO5VCu7I8jdXC6p7LK62meCyENuw0dPhhYPGNRJJtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=c_7EnTaFyMi3n8iqdYvBQcHSfxK7s84JTeGODL9szAqyv5DFZrIqK9h6npdOoOXoiDepXXPc-LfNzuoFsDT67N1HNAIOg9THN9apOH9YLbPIaTAKkPlabI0N5_FSLOVjk0wQdFDwJtAgJAGaet3O5O3zZ7wlTcV8Vempi_UohEhubZuur1GwVEkA1_TMpsqSsIt_aWDnSpi2gzTibumZ3ZbCyVQxMVzhEY5x11zAfY3UHTfcAp2cDFc05O4RNoN9e8MrfHKyiVWKDrPK_z5t_xWM0ao_86silveRyUOaFC1iE-dy5WtkGTV8P02NAMC3X1mK-sNbLNMI68PGp_B8C7s_Xxa4in1b4whwUmD0I-TGIdj3LN4lssZ70edPCHGY_PGhhL-0JBXiz8dGPWXkHbLuCSz7Aeq3zI0SBXPKFjGgOevsi8Yi-74w38sW958YvUhdovCZUcqhaZDbsq8uZhbAUklHT9IWoLdyTGncd9E03huL-3EoOuyQGandJ3lXtlWjrhD0sholrWn1F5r__R8bx1gkjjnV0S85zPmeSbYm3yTX2zWQhaBY9qC2jsEq-UK5W2W8CRSr5ZTMBUEElpMDBMOhjQzDYE4GGauAaveotcc96wELPsA2AlcWz4I2MDO5VCu7I8jdXC6p7LK62meCyENuw0dPhhYPGNRJJtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود شهریاری چه اجرایی کرد
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/101566" target="_blank">📅 16:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101565">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESoAeKjKSMzxA8p1LJLTrc6megQaia5rKxjojBTYBeFA-nju1Slsn6zagVf1fiqEFpqIf7weZue04nmTiA-ElHem7hYdCshjZAFsRnwqMSWqk2HVUedtHuXbtETb3Ehl1J3H9X63TW9dLED30Jxa7XwUYdG-w4pzU8aGYLLQrNLgghvjd3d3Avdi7wzW2RnBb2X-XCqLeVPo1vgXbDdJQ1TXvGTrlRSW2wjldAQ6IbPASUPpqoBhdWyyvMGxq0D7E3n_fhGCz1_42ZekuaLgJVDk5Tjq9RFZ3ZGMq_YuICt1q-dIsdVqvqGJmYLQ_tFiN90yaUY7MO6cXVejutRIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/101565" target="_blank">📅 16:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101564">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎙
🚨
حمایت جالب رضا‌رشیدپور از فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/101564" target="_blank">📅 16:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101563">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=CN699ZVLOYaw6Vgp1wvuvMUgSVkct-uH37kw2_gpkBtVj840Qr_EJn3VNbts59iVGHcU1ohlpAsSFI--S6ijhFX_qzGasEgFxRBS-1Iv9Y1vleAmDh2NCI1PyUwQmf7ZIcohbdPk36INqETRaio-gR7DMM4MLrCcd4_YCi758NBpkVUmPA7YIAo7ongKRz7tD7yLiI0iKh6WwvTsfQfSFaXkupj6fqpXmUEqANpFZzEZEp-I4wxIM99hxlbjbndz6HjxWsnee5SSK3zShmljaul4ckyRhI4ryC8ueW1CaMEPT1Bux2QXT0l3wzATmpHu7Zc28x623sFAP7Gz_S6uGKzymD4Sbo63dcFp4cc0O7xMXVljth6tjBos1Z1cHm1XEwcinTkU5EUTSdLtict-NVfKZ-teI9UUVw8gAXs6rnRddP2xoknh16_UcEHJankNzPwKemLTn-vP1zsZ0uR00dGyCrr7WfUWOk8dLvx6PfFa7L9NqpOsqnCGwBTPxQqokMGEf3iVWVgsmOiJKXdtr3yCbRFmYMOPHgMmYvs9qLLmpJEphvUhFZ--n-Y9UMCqY-N6NRFqkTzuLD_FKS-7BpQqAmF8laL-7uDT7SytSRz9aXfgeigkP08k5fRhvE-6yDTGMbHW7N82_HTlBsyw9FMy6Gpf2vAV4VfC3oDbgNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=CN699ZVLOYaw6Vgp1wvuvMUgSVkct-uH37kw2_gpkBtVj840Qr_EJn3VNbts59iVGHcU1ohlpAsSFI--S6ijhFX_qzGasEgFxRBS-1Iv9Y1vleAmDh2NCI1PyUwQmf7ZIcohbdPk36INqETRaio-gR7DMM4MLrCcd4_YCi758NBpkVUmPA7YIAo7ongKRz7tD7yLiI0iKh6WwvTsfQfSFaXkupj6fqpXmUEqANpFZzEZEp-I4wxIM99hxlbjbndz6HjxWsnee5SSK3zShmljaul4ckyRhI4ryC8ueW1CaMEPT1Bux2QXT0l3wzATmpHu7Zc28x623sFAP7Gz_S6uGKzymD4Sbo63dcFp4cc0O7xMXVljth6tjBos1Z1cHm1XEwcinTkU5EUTSdLtict-NVfKZ-teI9UUVw8gAXs6rnRddP2xoknh16_UcEHJankNzPwKemLTn-vP1zsZ0uR00dGyCrr7WfUWOk8dLvx6PfFa7L9NqpOsqnCGwBTPxQqokMGEf3iVWVgsmOiJKXdtr3yCbRFmYMOPHgMmYvs9qLLmpJEphvUhFZ--n-Y9UMCqY-N6NRFqkTzuLD_FKS-7BpQqAmF8laL-7uDT7SytSRz9aXfgeigkP08k5fRhvE-6yDTGMbHW7N82_HTlBsyw9FMy6Gpf2vAV4VfC3oDbgNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز بازی پائو کوبارسی ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/101563" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101562">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
🎙
کنایه علی علیپور به علیرضا بیرانوند به خودم اجازه نمی دهم درباره علی دایی و کریم باقری حرف بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/101562" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101561">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🏆
🇪🇸
رسانه‌های اسپانیایی با وجود قهرمانی صحنه‌ها مشکوک داوری فینال رو منتشر کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/101561" target="_blank">📅 15:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101560">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4bPC8xxw_EulqoYaNzBvIVyExtZ8nkkurUhCK3SvGbJh4btwrl2oVdWEkyaPmpxXOAPcERKvIGc77iI57Rkc1lHatDPQOtXJl6UijhN9EzJ5tgcKZkjkmr1X3UUAewC1NoGyl03wJ7VPca__HGSUkYRQKKWsmCEcgSm7Rhx-XX3FeBkDql2o_O27De9zVg4SJlPXOOk3dIXChQtlvar1NoLwMVb-_EHgG1-Uv2zFANlvNbKhtuWAIfns8fNwz3xcuXRYwa1vcFOFewmHbki7KlNlVoOowKHiIgVgHDd1uGXcsuu7Z_WDVfFGJXpGnTiLTgYZk3a8kwXeYx5XWQOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
منچسترسیتی قرارداد فیل فودن را تا سال 2030 تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101560" target="_blank">📅 15:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101559">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm7M0mqyN-Z0A8gat8V7iWXVVYDZa76d9gkht9XsKabZwump1Cg1m_HbOYylwkNiAjNCwRHlDE0E8x7KOtOpAf_kTCIPKTL0QJd9lnIpnA0baOdwudt52BsPfrRuj98WYq9QtSW2cIXh3XmkrBegm075etE_zb94ZXUSriu49sTjzQK7jAxCcE9MR38QhSrHea5Fvh7ZjC0NfvfMZrIXcf6aVTV603mGldWOsPY2sjT_zwH6ldjb_YSVKsPQsPNlZhNGyuGgwkI3QDNYSzIgK1mFoNwSSjLMAutnzpnptKHAjLOW2qJz7XZSdLA_Es9WCXmDqVGlDLqo74WFVCqcBXjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm7M0mqyN-Z0A8gat8V7iWXVVYDZa76d9gkht9XsKabZwump1Cg1m_HbOYylwkNiAjNCwRHlDE0E8x7KOtOpAf_kTCIPKTL0QJd9lnIpnA0baOdwudt52BsPfrRuj98WYq9QtSW2cIXh3XmkrBegm075etE_zb94ZXUSriu49sTjzQK7jAxCcE9MR38QhSrHea5Fvh7ZjC0NfvfMZrIXcf6aVTV603mGldWOsPY2sjT_zwH6ldjb_YSVKsPQsPNlZhNGyuGgwkI3QDNYSzIgK1mFoNwSSjLMAutnzpnptKHAjLOW2qJz7XZSdLA_Es9WCXmDqVGlDLqo74WFVCqcBXjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇦🇷
رفتار عجیب بازیکنان آرژانتین در صحنه اخراج انزو فرناندز که وایرال شده !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/101559" target="_blank">📅 15:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101558">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=IbJJh_sVoHTpIdBZ5stoh1AKn5akqmQL4oXVVJks0X347c3_684ZPBjtTPcgA8UAcASIW1iBGCm2whAWaocsuz6X261cnwOdbmjHOSB0tJIkmQX5RwNnV6vVLFBiW3iJ_Q88Xe39Zukhv4ifMsiJhy2-ODOtt1owGV25G0Q1f2FohgWH-9yITRPIcm5xyZigC6Q6C3DQEm1ThAanyEuRvirZBequ2wU6QpHnQNvCWV2aGCFvDghMpmu2e2COQyhsrT4fKQGx5ma55bnGK0M1rxQYWefQiRsdtcTjKai5xCJJAtL7oqd-yWAYaKjFTyFYqykS71dRuhHe75V3X36yvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=IbJJh_sVoHTpIdBZ5stoh1AKn5akqmQL4oXVVJks0X347c3_684ZPBjtTPcgA8UAcASIW1iBGCm2whAWaocsuz6X261cnwOdbmjHOSB0tJIkmQX5RwNnV6vVLFBiW3iJ_Q88Xe39Zukhv4ifMsiJhy2-ODOtt1owGV25G0Q1f2FohgWH-9yITRPIcm5xyZigC6Q6C3DQEm1ThAanyEuRvirZBequ2wU6QpHnQNvCWV2aGCFvDghMpmu2e2COQyhsrT4fKQGx5ma55bnGK0M1rxQYWefQiRsdtcTjKai5xCJJAtL7oqd-yWAYaKjFTyFYqykS71dRuhHe75V3X36yvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علیرضا نیکبخت جواب بیرانوند رو به زیباترین شکل ممکن داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101558" target="_blank">📅 15:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101557">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHs_UZZdbzFIOF6hL4mY96v-H21k7eLU-iXfCtfhefeyXDES9U2lwdOjhfmuRajK3syx8LKG6kTwp8xPpI6PRG5HiSxIpE_JkTzN_eyskb-XoL1tRhUYGFljW_Zk0_Bs1x58O4cemHqYgF1mhlzLtOpdj4cg6SQVpx4fSFPUNiI1LDX9WY1jn1CwTL1PHgHaRzGhMQPcmq-UBcZ9-KnM6b0KnSGtXTZkdkT7Glnhe9qSWZr5valcenBEgzBq78NzBGG7alkZxIjo_BOTqZk5gFn-l5KFXO008v88V5U26nkE0nyNXrXyYu_oIMopEm3izBdA_0g5OZTKFE3Cc3Untg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بازیکنانی که در این فصل، در بین پنج لیگ برتر اروپا، در تمام مسابقات بیشترین گل و پاس گل رو دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101557" target="_blank">📅 14:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101556">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=M7HTVAp4Rj9R-8LVwm5gQs28YcetI4JxhxhfZ19zqnxutc_Zjy8oZflROtmQFTnFDVX9nlWIvSlekYryy820GOKoPpaKJ5OHEUcRPyWy6Dn49F3mgJeHiY00MzqWgBBeHp6wCnUgEk2hqKB8T88v0I-tLmSC33g2Baj4tmhmE3LTAuQWDdt_8a-ZAOSGPPEIUdEJ85Kn00IP3EU44gkbOl5qmff84DV6u5kGKSvAyYpwyRZusF_ZaNDiOTmPE8RgAyCDUVZu2ZYR2fUBj2-xcwMX7DH0L5RwvJmmxlmhH5i_MCMxP0xj9jgK2zC_iBqqGPtZMVR0M88ISRjEM5ihjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=M7HTVAp4Rj9R-8LVwm5gQs28YcetI4JxhxhfZ19zqnxutc_Zjy8oZflROtmQFTnFDVX9nlWIvSlekYryy820GOKoPpaKJ5OHEUcRPyWy6Dn49F3mgJeHiY00MzqWgBBeHp6wCnUgEk2hqKB8T88v0I-tLmSC33g2Baj4tmhmE3LTAuQWDdt_8a-ZAOSGPPEIUdEJ85Kn00IP3EU44gkbOl5qmff84DV6u5kGKSvAyYpwyRZusF_ZaNDiOTmPE8RgAyCDUVZu2ZYR2fUBj2-xcwMX7DH0L5RwvJmmxlmhH5i_MCMxP0xj9jgK2zC_iBqqGPtZMVR0M88ISRjEM5ihjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101556" target="_blank">📅 14:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101554">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUrjYJJIfFzLKTgJuTOgyKf3fLwozNg2qtUIkk3nEPhb4QkGaabAGkU68QpZd8yPiEytGHHMeevDy8oXmBYicXpPPx5Na1rbFwKSrzC4gO-Y-WvNG63OALRDyswiSrvJMPlAjr7nynpEHu-pvHhXjNPil8S8DMQBQpWPhqxAzzUiKB7Wa1iRY_qKZ56f6tNmY9yrRK5dKcWIVVXgsYVO-kWEioOcnrH2XNxmp9Tprt03f8qvJ2LPhfVP2HTJ7iWyIqS5gxDLZWiNh_k4iCUF55sNn6-6Ik7tdXnnp1zxniqj0t8nCAsdxICtHCPNc62OIEXwUv4AeorNI64QqKsKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrvebBrGW5flHk0bAmfSjmQM7oURMVZ3x0PU8fB1sdV9bi5Tzgr6IzO9VFWoEFOQykiaSWfqeBmubuFWZ53CLUzefdGNxFUvYYSAJtL8tJmflckGPfVnEC1nvBZ1GFM-hDRTaoMRoXiNvN0Mc0FzHzcZkkIWN_sLM0Urigiw3kEz2Nr1YZrNt39l2s-0sqUNaLXuZ80Ru_OVGVEKmRIXV1xkfEyW_IQU7grJkn6eXeiZSUQnRgQearuE8jETfgU1OyRr_mZSpFgwATljsOzbeKgoCpd8aOC32eES5vOuVir2xrQjPnAZhWRqLcAhsdWKVQlGxFWN084fTf1Ee4ogVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خوان مونفورت، عکاس عکس معروف مسی و یامال:
من به خدا اعتقادی ندارم، اما این عکس نگاه من به زندگی رو عوض کرد. انگار همه‌چیز از قبل نوشته شده بود. هیچکس حتی در یک فیلم سینمایی هم چنین داستانی رو باور نمیکنه! هیچ توضیح منطقی یا علمی واسش وجود نداره. یکی به بهترین بازیکن تاریخ فوتبال تبدیل شد و دیگری حالا داره جای پای اونو در بارسلونا دنبال میکنه و در ۱۹ سالگی هم قهرمان جهان شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/101554" target="_blank">📅 14:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101553">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI06vnfyh-9BdNnF5ebUAU_wq7TMVkduXHejz7_6ep5D5CWux4XhpWkwWadJJdx9Jm64oJ_-pTgooquvLXa1oo7X1qiougQtQ2OhYAuoWoNNaQa_KJNga28yrItBc23MpeoL3BD3trZHIjs0RXIkFgVf2XkEv6cm-Xu2WEqBI9RhvIVHwqJS4nCdoUTUfrVV4t_donwYgWcyZdFseNpEWijw4HuF-g5SB0v7ioAAh6cmubqzmxf1L4n9LAjKHs-kyvdLm4jf6FKhRSaQ6PXn7bIjX2wnr9PkriS-f9j3zb5m_hcldlq8zv0pV4crSbkCUrs-HjhEUYH76QGQIhkf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد!
باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی از هواداران شدیدا از او عصبانی شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101553" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101552">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB0_MlbDcJWBK-aUJe0qOlywgjgZCsMGFFNdo0e39mIw-FxMnh1bpRKq9m8oewBdTwbQTZz8QY82Vk9jSWsxcwBG3MxGyhAG48D8hP0ho2Gk0hvPGvWSfdn2xyxTBC6_lb6-1ajQAVkPKGrfXMJNygu58fgjjou8cdpacFN1JCWmogdEISkq3unV6mNJ-Dm-UKnaEBgkJaurI8Fi-ogD-x1bMpNHW3VWpQeFTaTp3O9VulfhfD2K5XPsE9jBV5Gcr0q0OaVFR1kkAXzDz5ZQyS8TtgKfqCBQgimwfu8tydZbX7wzh-Yu-PI1HwWUJn0_TAeyLiSPOmJIMnA7w-0R1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
الکس فرگوسن: "بعد از اینکه ایتالیا جام جهانی ۲۰۰۶ را برد و یوونتوس به سری B سقوط کرد، من مطمئن بودم که او یوونتوس را ترک خواهد کرد. بازیکنی مانند او در سری B بازی نمی‌کند. در آن زمان، رئال مادرید نیز به او علاقه‌مند بود، و با توجه به مشکلاتی که یوونتوس در آن زمان داشت، تصور می‌کردم که یک رقابت جدی بین منچستریونایتد و رئال مادرید برای جذب او وجود داشته باشد.
🔹
بعد از اینکه پیشنهاد خود را ارائه کردم، پاسخ او بسیار تکان‌دهنده بود. او به من گفت: "آقای فرگوسن، شما قبلاً با من صحبت کرده‌اید و من به شما احترام زیادی می‌گذارم، اما یوونتوس در حال حاضر شرایط سختی را تجربه می‌کند و وظیفه من این است که در اینجا بمانم. یوونتوس در بحران است و من کاپیتان این تیم هستم. آیا انتظار دارید که من آن‌ها را ترک کنم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101552" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101551">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e870288.mp4?token=rGDXTnmwBQM4syUQl683l2j5Pty2UXJDim5AJ5G7K_xQwTxkDkq3vqL-uOYjVnIDCwJiHmZ8OGHJg6XigbYZSjWPLQtA4y1NJEpjr5HbArDOnKtbLKSibVX5TxQ5RCpV-Z7QoMOemR5bcrDGFCS9W7oe3OcYFlCjLN4R82gAe4BUT2BcsujdWr19hHUn4gtbyunVqIQZROTcnP_nrG2Lvo_bF7sisOLEBFitW1vWpONhiZLT562e33vMhHkycuCNSotpLsZAkc7w82CovqRPetrumc6nxKN_HQR4dFc_kFUWU0gRxQirFJf7yiOhVOHs0dhEg3RFANEnojpDWADgRXGoA1S5USF1yNDQPBuOa8xcQtz5gKFuo2eWvnAMz4FIC6N-OJFpau5oDzrX861QdqkwUNUWmZ7Li6UuDL47necZSe4iJYSbopPoKXwZL3YhJY7-X7-rW591AOJaRIUTLHPiIykeqHphhxqrcdVkgzBq7MwiRoS10qgs-zaOnicaXVyBf6ew25fbViKjDwQK18WDzEECXK6YobE7DYT5CGTQYoy2JTwMoGlVmNPXPX1E3mMzllqZYaXiw2k7SuYPrFiJDoHMduUPLHMUeOMWorJVVL7fWBOAI1R3LyqJG1mRpdb3i-zo6zo7UznMkBsgp-ECc60f32WktoQ7qQWia1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e870288.mp4?token=rGDXTnmwBQM4syUQl683l2j5Pty2UXJDim5AJ5G7K_xQwTxkDkq3vqL-uOYjVnIDCwJiHmZ8OGHJg6XigbYZSjWPLQtA4y1NJEpjr5HbArDOnKtbLKSibVX5TxQ5RCpV-Z7QoMOemR5bcrDGFCS9W7oe3OcYFlCjLN4R82gAe4BUT2BcsujdWr19hHUn4gtbyunVqIQZROTcnP_nrG2Lvo_bF7sisOLEBFitW1vWpONhiZLT562e33vMhHkycuCNSotpLsZAkc7w82CovqRPetrumc6nxKN_HQR4dFc_kFUWU0gRxQirFJf7yiOhVOHs0dhEg3RFANEnojpDWADgRXGoA1S5USF1yNDQPBuOa8xcQtz5gKFuo2eWvnAMz4FIC6N-OJFpau5oDzrX861QdqkwUNUWmZ7Li6UuDL47necZSe4iJYSbopPoKXwZL3YhJY7-X7-rW591AOJaRIUTLHPiIykeqHphhxqrcdVkgzBq7MwiRoS10qgs-zaOnicaXVyBf6ew25fbViKjDwQK18WDzEECXK6YobE7DYT5CGTQYoy2JTwMoGlVmNPXPX1E3mMzllqZYaXiw2k7SuYPrFiJDoHMduUPLHMUeOMWorJVVL7fWBOAI1R3LyqJG1mRpdb3i-zo6zo7UznMkBsgp-ECc60f32WktoQ7qQWia1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
📊
نمره‌دهی به لیونل‌مسی در بازی فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101551" target="_blank">📅 14:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101550">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=N1deeG0fUwev68ahAWeMQdmE5VDayCDG_pxmhIBL6DYdsG0Q6NX_9g5ZDLmdvsayS5fHxDAshONaUrH0d-RlyvtyAWFGYZOdtuv3oFPUg0_uLuL43lAvcLmifnExxwGYKUIUfRb-sDvJZyenEEdUir9RyPOJVnSHkdJd6X0SkYjxSncQ805FnEg07EEJvtyoI7b7ooslDgn8screXalcOvR3C0F7Ugdb18cFQOFixSBOmp6HBdkCSDQiuqMa0gpODxGig0uQiySO2n3LHBUVYR91749GNOsth8cP9jDYWtqg2lCq3dht4TxpYgxh5a30-ngZXKf2QKzh7nAR5HfzTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=N1deeG0fUwev68ahAWeMQdmE5VDayCDG_pxmhIBL6DYdsG0Q6NX_9g5ZDLmdvsayS5fHxDAshONaUrH0d-RlyvtyAWFGYZOdtuv3oFPUg0_uLuL43lAvcLmifnExxwGYKUIUfRb-sDvJZyenEEdUir9RyPOJVnSHkdJd6X0SkYjxSncQ805FnEg07EEJvtyoI7b7ooslDgn8screXalcOvR3C0F7Ugdb18cFQOFixSBOmp6HBdkCSDQiuqMa0gpODxGig0uQiySO2n3LHBUVYR91749GNOsth8cP9jDYWtqg2lCq3dht4TxpYgxh5a30-ngZXKf2QKzh7nAR5HfzTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های مجتبی‌پوربخش علیه میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101550" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101549">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=tzRApRhnnucL9G2lNgbui79nLMnWG9b0BT6pswkMFcWsPZJhdhSQ1KVnlymIv0kY_8x_C2Q1ZOHN61U-lgzIld_JjzUSiUGq8H0GV_fgEUbAX6M3oDaPH6oIBU-JDQsuCIKq2IuJSC8cyVLA_HrVrZ78lmIXtu6umoxPgUqAnemCRgr5ZASgWIBt0QGRWbw2MFWGRk1IqEq8HReC8HMbX82RhuDgq7Gi9LWemebqK7_1ouZ-Pn9akUglPSMXkSmikU5sj9A6zI90atsVsvQK84uPiwmWT1Bmyv0h9ExddpNp-2HCdPcMZGOsWZdBlK8WbNsIj7SbpwS0GytdNP_7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=tzRApRhnnucL9G2lNgbui79nLMnWG9b0BT6pswkMFcWsPZJhdhSQ1KVnlymIv0kY_8x_C2Q1ZOHN61U-lgzIld_JjzUSiUGq8H0GV_fgEUbAX6M3oDaPH6oIBU-JDQsuCIKq2IuJSC8cyVLA_HrVrZ78lmIXtu6umoxPgUqAnemCRgr5ZASgWIBt0QGRWbw2MFWGRk1IqEq8HReC8HMbX82RhuDgq7Gi9LWemebqK7_1ouZ-Pn9akUglPSMXkSmikU5sj9A6zI90atsVsvQK84uPiwmWT1Bmyv0h9ExddpNp-2HCdPcMZGOsWZdBlK8WbNsIj7SbpwS0GytdNP_7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
خاطره بامزه علی دایی از معلم زبان خود و کریم باقری در دوران حضور در بیلفلد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101549" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101548">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=KmKqFpGUZcYaLkG4QJ9YnlSulj9JLUJpuSjV5yv_--OTOOMkjUMd711mERiF8Qn6_O1a63y6slThKJxgOBjAoIyiS9jc5P9jGuJrLjzcmwuIGHJxwTiRLa2Ft4tnkDUyYHrZMNOQ3HFVh7EkmEohZNCS9OBiF_d4ExUdwvy2hMXuntW2A-VBPdy3BJRcRuXEchqBqdQu3Ss6fxO7iJkwYVCqI9_85pGt-BDbyG_DbGe27Z6p-lkipOZoCLAVj4HPH13f3GuZcGh38Se8rzpgS7nIq5GvnjjaK03eoxzTHJlQgzMfzptJj_WEect33CwO8lI6AgBqsp4ovHR44sWvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=KmKqFpGUZcYaLkG4QJ9YnlSulj9JLUJpuSjV5yv_--OTOOMkjUMd711mERiF8Qn6_O1a63y6slThKJxgOBjAoIyiS9jc5P9jGuJrLjzcmwuIGHJxwTiRLa2Ft4tnkDUyYHrZMNOQ3HFVh7EkmEohZNCS9OBiF_d4ExUdwvy2hMXuntW2A-VBPdy3BJRcRuXEchqBqdQu3Ss6fxO7iJkwYVCqI9_85pGt-BDbyG_DbGe27Z6p-lkipOZoCLAVj4HPH13f3GuZcGh38Se8rzpgS7nIq5GvnjjaK03eoxzTHJlQgzMfzptJj_WEect33CwO8lI6AgBqsp4ovHR44sWvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رئال مادرید در این روزها.
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101548" target="_blank">📅 13:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101547">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlPguFKVFnNEQphagBLqSVEu1GPSrs2KKllNfo54giB5oNvEeiB6M4q9eEzxL810AMEh1i6s7OOelSNyuoY2NSTf7msAzPW-dMb79znVFWMJWyekHNgazf2MhICRlv-MgPH1XkhYVUVQQkikPm3zbiFQfZhSS3EFJH-7LNRwsgYWfTt4vp-V_CecTEe3tYIIU2SGzia3CK62E5hi0Rg2dqNX3zsCbK-EHvBUV4qwz7dykgR6kW5iHqHGEyVewjloSaEQohAFQB9kuHIkTTuWf5yeMqorrvAB9K1d63eiVIcgr2i-X0vaVP8ivP5jItMvyicmz-qOWof0L2_4Zn2-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
وینیسیوس و زیدش بعد عمل زیبایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101547" target="_blank">📅 12:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101546">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=EUr45thmLZgb-Rppmqoy0Hfbko_tfPX6AZCSe1LvjGJV2xvWnsyzX-VyYKMJb67LNoZVV7KumD46ZgU5116v7U3igmJuvCr-Rq_DIfxz7vR8-LXEFVY85xwsIc6tjsW9Z_1ncvLRDRtejHiwBDRe2nt-Szk6AWhEOu3xsKaC5mCsukNX-tSEOlGVHoXUmEu25EXfQjmacnk07-RNtVOUI5SwhUgE1HxuoPAzkSAKqJmXeHiAW9EgsxvYOxrajxKYZfK5XY0rqGRpXcHWZEcEYLFsigOHoxmu2mzdMppOJCGG9cB5ylunUJ6jFlL1ybKgZC0bGeH6CRtzQCz9bAZ2f58_KxW3jO7oK1Zti4PWM33i8C_azbm6_q77lCzqacKqRURruxPTrM0fXheIuYwyZIHYplfmYBRa_p-cEAdwQ9XDfZveqgTnLvR4kavwNwjn5v4b6uthZ-B1d1RQcZDF2HdyHzmPrNQSY8cBpJp3ygif6idVBOYL2euvrCPIfcC6QEOBj3LIDVP-Shy-fX0AFHiBwaOIITA64Og_AytehFa6-4lE3X10RRYdZ_XBdFy6mKNf8Yv41DJMvCGtr2356sDTdGQy4m6XwX75zKy3oIpvRQnqZxhOY_IX0oT8nkDvPYHYALEj9t-1ZTYjRHRjlLwX10QhMQjpUk5yH-Cxum4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=EUr45thmLZgb-Rppmqoy0Hfbko_tfPX6AZCSe1LvjGJV2xvWnsyzX-VyYKMJb67LNoZVV7KumD46ZgU5116v7U3igmJuvCr-Rq_DIfxz7vR8-LXEFVY85xwsIc6tjsW9Z_1ncvLRDRtejHiwBDRe2nt-Szk6AWhEOu3xsKaC5mCsukNX-tSEOlGVHoXUmEu25EXfQjmacnk07-RNtVOUI5SwhUgE1HxuoPAzkSAKqJmXeHiAW9EgsxvYOxrajxKYZfK5XY0rqGRpXcHWZEcEYLFsigOHoxmu2mzdMppOJCGG9cB5ylunUJ6jFlL1ybKgZC0bGeH6CRtzQCz9bAZ2f58_KxW3jO7oK1Zti4PWM33i8C_azbm6_q77lCzqacKqRURruxPTrM0fXheIuYwyZIHYplfmYBRa_p-cEAdwQ9XDfZveqgTnLvR4kavwNwjn5v4b6uthZ-B1d1RQcZDF2HdyHzmPrNQSY8cBpJp3ygif6idVBOYL2euvrCPIfcC6QEOBj3LIDVP-Shy-fX0AFHiBwaOIITA64Og_AytehFa6-4lE3X10RRYdZ_XBdFy6mKNf8Yv41DJMvCGtr2356sDTdGQy4m6XwX75zKy3oIpvRQnqZxhOY_IX0oT8nkDvPYHYALEj9t-1ZTYjRHRjlLwX10QhMQjpUk5yH-Cxum4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇴
استقبال از ادهم‌مخادمه داور اردنی(داور چهارم) فینال جام‌جهانی در بدو ورود به کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101546" target="_blank">📅 12:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101545">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UntL7sUKiqjF1WdAMXd-83SJV2repKIwJeT7B0c_K-sD_jjjz6hZo9ydDWxTQ6VyQEiwWApC6t5BLr4AP-8-oNRD5-Es3-ZnFyf59J9ltKNQFZ-4uXvZbpevei2uIt7NkicRblQGLFmHYlgXHDNNTi4qUIKYYuNF_sDN1rkcA7wasvfXlOGiQOeHrAON6S2z5CtXKmyuiXURzapZKdNS5_mtLjKctxBcEgKsGEvjhRH_YKIrS_Rh1vh7ZF1wzQ7YoTe6vixp-JJrCBbSS5WJAs62zmLgcpo2kfx1Fk2Sby_czfLAa1TslCRBVmjdLzjBgd-SxluNyGW8JiffwfCXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۶ تیم قطعی صعود کرده به جام‌جهانی ۲۰۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101545" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101544">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101544" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101543">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYDlz1TAvxceBMDoOZS5zFCmQtT4mFzkDBApSaVoTkjR3YEbEO63gG0YOdORovBKHUjA-AiDqdmqVX-NEA0YaWb2zkOfYQzpZgI8_JY9GG6elBT27seXJdej8pwXZZAZLS2eEz8Md1KSO2SUNHaTqjoC8SEkNiH3aNJagvY5LMICefwXy5oFYViONaIqAAgAcmsKmOfPZIiN4GKvWnbNiJXuF4OxqhfKQocOuZZH8b0SYo6xD2FroQacBdb5bfItzhFRhtADQ6DgivYC4JU9eTO6E2gj9CKhLtWA7S4szdne7k9N5Zlzb6eyKTwqa4eMx5DRKbwkFhpp1UZWypk7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101543" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101541">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=hIQxRA-NyvVxLMUNPpDiwiKixU2SvN_wTd0qvLMRzgkx5cc5gNI-rtmmZDTIl4GlcdGyabpZSbhnyRO9d8-fGMD6LnfVQC5LaIDUvBGa8nBqnERF9O5vkOigkUvpcuLLHo9fRAp8S9TTD5h8DbZB2xs9svJQz5NQohvIIB11zqJpD_5YZcb2kW-AnPgaHGsYdfNHwsHZjlWOmes3mivFkAa-EYpEqH6uKOiDcA_mneZHmm_OyaINZgsp1DB6_KsYZx1HOIMmUkXfbocQkgDnPSlJPqz_gyj7RWs4Qw7fBTZ6O2SMbYP5ndUHpuGOsprzqYHZbtbJ8vPWxR_DlZ1KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=hIQxRA-NyvVxLMUNPpDiwiKixU2SvN_wTd0qvLMRzgkx5cc5gNI-rtmmZDTIl4GlcdGyabpZSbhnyRO9d8-fGMD6LnfVQC5LaIDUvBGa8nBqnERF9O5vkOigkUvpcuLLHo9fRAp8S9TTD5h8DbZB2xs9svJQz5NQohvIIB11zqJpD_5YZcb2kW-AnPgaHGsYdfNHwsHZjlWOmes3mivFkAa-EYpEqH6uKOiDcA_mneZHmm_OyaINZgsp1DB6_KsYZx1HOIMmUkXfbocQkgDnPSlJPqz_gyj7RWs4Qw7fBTZ6O2SMbYP5ndUHpuGOsprzqYHZbtbJ8vPWxR_DlZ1KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بازی‌های افتتاحیه جام‌جهانی ۲۰۳۰ به میزبانی سه کشور آرژانتین، اروگوئه و پاراگوئه برگزار میشه و سایر بازی‌ها در مراکش، اسپانیا و پرتغال خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101541" target="_blank">📅 12:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101540">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=RmfqyjUIPrk_jNYEjgYMaxYJRnQ-DhoWP2M99XTWpzNxeERkMzmGCfPh2_w6cJaQGkOQEekxoTAtr-FxoFYgrEx3tuyVItIZanp1CQBDTYhvRdXG57RY4kSQxKUGmaRKoLBwXU8B0ehIBZz5YJYMB14-wV-UCGtocITKIgNZ6aj7b0SqcH30Oi89vC-MePXTAcT4jcuPPz-1cOVQFhFfIukuVjL8n-Ba48hvC-OPzEym49ii9IMm_xJYWrt4tuLLjVbU_l17QRULWh7sTetRuTCIUrccWzfCigCJVbB1eOyn8xopuC-utKnJM2dFc5C6X53gjebNjKaxkPe3_1UB7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=RmfqyjUIPrk_jNYEjgYMaxYJRnQ-DhoWP2M99XTWpzNxeERkMzmGCfPh2_w6cJaQGkOQEekxoTAtr-FxoFYgrEx3tuyVItIZanp1CQBDTYhvRdXG57RY4kSQxKUGmaRKoLBwXU8B0ehIBZz5YJYMB14-wV-UCGtocITKIgNZ6aj7b0SqcH30Oi89vC-MePXTAcT4jcuPPz-1cOVQFhFfIukuVjL8n-Ba48hvC-OPzEym49ii9IMm_xJYWrt4tuLLjVbU_l17QRULWh7sTetRuTCIUrccWzfCigCJVbB1eOyn8xopuC-utKnJM2dFc5C6X53gjebNjKaxkPe3_1UB7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
علیرضا جهانبخش: به فردوسی‌پور قول دادم که لباس محمدصلاح رو براش بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101540" target="_blank">📅 11:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101539">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glRESzEk3xcRE07uYECnsnZzCJj1BDPeLaWqO6z3oMZOJ1U6BATAAT-dJiOlakHDkjiJr_5zuXtFCxEz2D_N7vgDi5vnHDc3VYhvRKgUrXYDYU5NF6KKuf-y8KsPa0SjNNSTznx93_RJZbqAXsl4z4IKcYvRBpNDlZh5UXQSpGQLCL4VUGwpfO7BpRFUFPGCrtkGuyUGm-bry57MNTQgEve4y-WiaiEpY0H5_nfktWx4SmuU_gvq8a7_mlWxcLc7RroGssSovUqU16ZJ9svA6wJ1S399bjTcGhLugjCrTYVA2B6ztX3yJxsEgiauYHaE5AyTNcEYCVJ5i10JiNATwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم منچستریونایتد در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101539" target="_blank">📅 11:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101538">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovxvhk8mIgsyqcCjDLmAjwJj_1-nWdK-5RT5PcW9vGEejH1GC_-cjxDM-JT3zaJxgtbTMr6CD0W5Dsp4Kg7vEy4fjCB6grPnFGZuLfSv0E83AU2RFs2v5YCbrCN9V92ph7GXyjgUvXc1ESwruZ9HUWDCaYWZ8IQbEblA8sC5gDJbdirhxUNVYfgQTWx7JbufdLzAVzJIEF3l3z4iVlS9R-mrP0k1lpsAu7Jyt5ZW9SrfoSy-pagUnbq0QclepUDPh07844gfj5M8tcwx2bDsYDG7Yo7-JMqhYIq7i92Z3B0YF4zot4i-N9h8cR_Q08cKqAIrLn5o4XQI-oOsAeJx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حمایت یحیی گل‌محمدی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101538" target="_blank">📅 11:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101536">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330d45af26.mp4?token=mjzm0YVkWQMM_lz9FWMn0eTxdyIwNg2XcsBbYzJXC0G_Nq3wm7q3vHPeaaq2OECsJwqfbuUZX7PMuFqJeJzjTNjLIL5KVV484ZPOuslctsAvkid3wF5ODjQy9fbbNu2IB0WqkdF3j6FfZ4UMziO9MvevlxryvtIU3RBZKPZWvkmzz0DB5oh8FODDWpB-o6ag3gMG74Gl1OMI3iAQwYqTzcYejR4NrgnEatp4sr9lyFDvonN7tPh_uzDSKOk3ZEhKXzdy2HVGxvirjyOc89F6qII0ceGfdoqaKh4_2MME9lshJXtrsuZ1DHYuR8cUBTvBRedYXgh4PEYOHXCTBYUDMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330d45af26.mp4?token=mjzm0YVkWQMM_lz9FWMn0eTxdyIwNg2XcsBbYzJXC0G_Nq3wm7q3vHPeaaq2OECsJwqfbuUZX7PMuFqJeJzjTNjLIL5KVV484ZPOuslctsAvkid3wF5ODjQy9fbbNu2IB0WqkdF3j6FfZ4UMziO9MvevlxryvtIU3RBZKPZWvkmzz0DB5oh8FODDWpB-o6ag3gMG74Gl1OMI3iAQwYqTzcYejR4NrgnEatp4sr9lyFDvonN7tPh_uzDSKOk3ZEhKXzdy2HVGxvirjyOc89F6qII0ceGfdoqaKh4_2MME9lshJXtrsuZ1DHYuR8cUBTvBRedYXgh4PEYOHXCTBYUDMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تمامی قهرمانان جام‌جهانی در یک ویدیو جالب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101536" target="_blank">📅 11:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101535">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=NMHbetrcKCoi9EAla8litVSh3F-vaLZi1mPW4SbBL01KE7kS7SxjXJdxddXrQlXcbJWyLXgyEkEr59yv2mG03-6Nspd0azaKFsrsIwL1aV_gsOdWL43oQ-jftcHKP8k0IBO1OiyFNXT_nkpH7m9ntdnsfH7t4kwwhzk7qtk-EDd2Fs3HNx4smdgWUoMxkzbkA9LgBMnyahFDDNo5hXdGqURGipQf7I3SwoKKtKJLya_ILrd1798vvnRHEuReIg1-qomLHvLI_lhWOp2runLybmjbGOCkwtrcSGpCEZqnxm3Tbv46hhuQzNN7cCsdodI2o9TAr1DqUEEhJffMWizAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=NMHbetrcKCoi9EAla8litVSh3F-vaLZi1mPW4SbBL01KE7kS7SxjXJdxddXrQlXcbJWyLXgyEkEr59yv2mG03-6Nspd0azaKFsrsIwL1aV_gsOdWL43oQ-jftcHKP8k0IBO1OiyFNXT_nkpH7m9ntdnsfH7t4kwwhzk7qtk-EDd2Fs3HNx4smdgWUoMxkzbkA9LgBMnyahFDDNo5hXdGqURGipQf7I3SwoKKtKJLya_ILrd1798vvnRHEuReIg1-qomLHvLI_lhWOp2runLybmjbGOCkwtrcSGpCEZqnxm3Tbv46hhuQzNN7cCsdodI2o9TAr1DqUEEhJffMWizAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پول نظرتو عوض می‌کنه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101535" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=XfC-U8aJ0d2lc_VFjAY4wSS7-T8lQcUmaLUBq3mpm2QnQ0rHpYV3kwFYSwG9Yqh6RAs-d9x5-6F7bwASp5C8R_Mx86MCK2FUb5ybPNOgU2LiY2_O2hQmIcdt0ZVqMbJD3L5FB50unpUhdt0UQmdv3eJy9J1V-fkuL0IUFF1iTy6uWkWBCsH9EfJpc3LrcWXO82KXal0JEgRSkb-1PCC5tS8b41NLWhLxmm7cqpRwI3w4Xb9B1ML7WmBiGkejOl7Dj0His3pGNznzD0q0yiz9pCgfEYLao2U8L5KmV2n6qb4YD2pqgfwkrFTOlpuplrOUzJX9cljjH969pjx0sFusZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=XfC-U8aJ0d2lc_VFjAY4wSS7-T8lQcUmaLUBq3mpm2QnQ0rHpYV3kwFYSwG9Yqh6RAs-d9x5-6F7bwASp5C8R_Mx86MCK2FUb5ybPNOgU2LiY2_O2hQmIcdt0ZVqMbJD3L5FB50unpUhdt0UQmdv3eJy9J1V-fkuL0IUFF1iTy6uWkWBCsH9EfJpc3LrcWXO82KXal0JEgRSkb-1PCC5tS8b41NLWhLxmm7cqpRwI3w4Xb9B1ML7WmBiGkejOl7Dj0His3pGNznzD0q0yiz9pCgfEYLao2U8L5KmV2n6qb4YD2pqgfwkrFTOlpuplrOUzJX9cljjH969pjx0sFusZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه سری ویدیو قدیمی از قبل آشنایی یامال با اینس گارسیا دوست دختر فعلیش داره پخش میشه که توش اینس وقتی یامال با نیکی نیکول بود تو لایو گفته:
‼️
🔻
اگه یامال یه میلیونر یا یک فوتبالیست نبود، نیکی نیکول حتی دو بار به اون نگاه نمیکرد!
﻿
‼️
🔻
همچنین ازش پرسیدن: «لمینه یامال یا امباپه؟»... گفت: «بلینگهام»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101533" target="_blank">📅 10:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101532">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">😂
😂
😂
تفریحات جدید اسپید بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101532" target="_blank">📅 10:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101531">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یادی‌کنیم از سوال خبرنگار صداوسیما از لیونل‌مسی که بنده‌خدا اصلا ایران رو‌ نمیشناخت :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101531" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101530">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sukY0xtcSdDJMI0rMPE9mGB9MN3DcVd_dkQi4tjZlJEbW210JXg5bBozPTiwzSYV97lFiezuVLrtcO3UQq_FlR-AgFI9-2_WN8q3sD6uHJTubz4tYrA1ln-IlKovfv9DmQqDNXIiCCvgtzapKOOcKCAo4uU1bQUh0eUAt4VdVZB67tBPABapDSdRB0ON1jcgZqKsGhH9XHTVNBzwaUS8ViC5v1Dc1KQDQmJssisGCzOwwM1Dx896X_PVUWBbwUUObP_-sb8p0r-4aHjsArQ2dQHvr_sQHPJakSkLKnj3RsOuLX4cYP4fP-ltaCtBV8gX60z-t6hICsNBb59ciEPn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📅
🏆
شش سال پیش، در همچین روزی لیورپول برای اولین بار پس از 30 سال قهرمان لیگ برتر انگلیس شد.
🎙
یورگن کلوپ: "این دستاورد بسیار فراتر از آن چیزی است که من تصور می‌کردم باشد."
🎙
جوردن هندرسون: "من بسیار خوشحالم که این عنوان را برای استیون (جرارد) به دست آوردم."
🎙
اندی رابرتسون: "ما 13 هفته منتظر ماندیم، اما هواداران ما 30 سال صبر کردند. این مدت کوتاهی در مقایسه با زمانی است که آن‌ها تحمل کردند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101530" target="_blank">📅 09:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLDUadm019G0v8bPTwmKxi9HD-5z_XSDKxCAIlXq-MDRA2aeSwBHM47TEqmWd3IvHBtdiMC5vEfdJFSg19XBfb4FSDLwVc1mHQel_V0hhLYswI0Og28VpFiu8uSgqrP1naXYRPX00oXh3Z3hotVzYKTCLph_uKB9_duL1Q_DfZeqAmdjLnaqTMZCjjxoUWOm__VhJPnQz6bL-PzFXNMvOJRVNpjYVMHmGpe5PiFa0mNJuuKYh70UcorIFmRhhh0YAqs4n5Sgfbe1vKMw_-iqe2vjOuzDwcpSsSUYbTof-UJWbW5uCvCViIqqpBRGqrM_FRjfGfjReVDza3-YSZ5rnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🇧🇪
🔻
مارک فان بومل به عنوان سرمربی تیم ملی بلژیک انتخاب شد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101529" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=gBTpHTlMJdqEGs8sgtSSUACShtakjkmQac-ClUfj16zBy0Odi7YGinVkraasYBSaBCV7cizfjBtK42hc8Vn9G-0CgZh7bPNJEF0o-kVJa1uqR9s9VyPK8dDGo9fxIEW8Bzy6G5fsp-rDa_oqpea-rhZJu4daj6ig3ktCUfFcqPskQNGXHOt-g7RDe789v1wX_kXXZxbSU3m9qSocslpGsSD3YEYvBg5D__RrWJskQCCv-s3ZpYXlecdFn2pvb7-34FsDzrE0hNQCDxZ7cjTdGvLgOZt2gVYOVXCSlVPzxAzeSEDS0KaJn1U3acmXG6s_n7sss2_9llxTNyHVudfTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=gBTpHTlMJdqEGs8sgtSSUACShtakjkmQac-ClUfj16zBy0Odi7YGinVkraasYBSaBCV7cizfjBtK42hc8Vn9G-0CgZh7bPNJEF0o-kVJa1uqR9s9VyPK8dDGo9fxIEW8Bzy6G5fsp-rDa_oqpea-rhZJu4daj6ig3ktCUfFcqPskQNGXHOt-g7RDe789v1wX_kXXZxbSU3m9qSocslpGsSD3YEYvBg5D__RrWJskQCCv-s3ZpYXlecdFn2pvb7-34FsDzrE0hNQCDxZ7cjTdGvLgOZt2gVYOVXCSlVPzxAzeSEDS0KaJn1U3acmXG6s_n7sss2_9llxTNyHVudfTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
فینال‌باز واقعی آرژانتین در کنار لیونل‌مسی فقط یکی بود اونم دیماریا که واقعا نبودش امسال حس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101528" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101527">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=siybEc3rtSTdlw39L0hC2iL_dvJlnQLwOp-C6uRC6C0M8dlpv67bYPoaOm14f-zin8HfBKBs7g0gM5YKSpTbOuFCmvAtLI-xgyeZmLS2j-dU0VJoEIn33zuMJTDtk8jezvy1LCVYZEr2Hc_g2nA6TQmcy30vsHn7QjjID18SXWHHKH86wMKHv4Ayb5U72tXtc53sy62kmmCxwWUG5cfrmeHKtPxQFoCsVFyUyi6bIga3_6OTm6XqcPWgrpsC_Skdo5SBuk4ZKdcVOGs3__6HuAll-sT3D25kRQmQZED4pSBJWfytDR7wc0qZPxxsL1EAEEvnyr5cLnEtInRP4NAsQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=siybEc3rtSTdlw39L0hC2iL_dvJlnQLwOp-C6uRC6C0M8dlpv67bYPoaOm14f-zin8HfBKBs7g0gM5YKSpTbOuFCmvAtLI-xgyeZmLS2j-dU0VJoEIn33zuMJTDtk8jezvy1LCVYZEr2Hc_g2nA6TQmcy30vsHn7QjjID18SXWHHKH86wMKHv4Ayb5U72tXtc53sy62kmmCxwWUG5cfrmeHKtPxQFoCsVFyUyi6bIga3_6OTm6XqcPWgrpsC_Skdo5SBuk4ZKdcVOGs3__6HuAll-sT3D25kRQmQZED4pSBJWfytDR7wc0qZPxxsL1EAEEvnyr5cLnEtInRP4NAsQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😔
پیام استاد وحید قلیچ به دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101527" target="_blank">📅 09:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101526">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMiEgM-d7vxL0Vz5mnzRELU7AQ5lLDLtGTz27JeMjzJoUdj0og6vxg_uwtqUxLN3cbHu80RNCGuJzAdn2mdT6dZutJyoCLGETy92W5DcLTaAYOEO8xNI0URoTQ3nb7JnB97wfNZWtu9nbDG0IJ6V9gjwKcRd9wfR5MvZsz5NoqTXF6-nkDknX4bMfORWC5iMvV2pJV_PSZBOLq1sT2GWd20CNjz-WeP-Y-TFXDNeS5P773kAchg7qdPKE67beLA4_-gRlkmRbosk0o_rf-E91-qvgxOVAoC5NEvmXbMAphow4_taMMi9O7o7rmlnmD9X2yoGoMiNpC1tFCMXuPqZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مارک کلینمن:
🔻
جف بزوس، بنیانگذار آمازون و چهارمین فرد ثروتمند جهان، برای پیوستن به ائتلافی به رهبری آمیت بهاتیا دعوت شده است؛ این ائتلاف در حال مذاکره برای خرید بخشی از باشگاه لیورپول است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101526" target="_blank">📅 09:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101525">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=EZoQg13Mk29sHWEmIlF8SISgWXs14LfAdZIOYRLfzJwFXZ4VNs3-yG-aJaQqCMZNB5oQaUO90JYX7mKmjsegxJ-S8kzKiW1OYaRFhuJjwJdYwxyJiWuSje6ZfaIuzC1kqByWR_8bA4nu-NLgasHnlcuJ_DmGHWhNoZnBCYe04RmXp9gMazGuAE2RA9MChwHWPSDN2vLgLIGNjhy99Qo4IIWb3I_IelWMEt96o21atPVlymRB-ckQSmJppMRMxtSaXhzcsyHvJ6Ey_OaMBz-A3WS3N8bZHEM6De0gL10hJ-RwSIIfY4Qi8sVHM_ITYG-IZaB6lI11yfGS7QM-Kkl5qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=EZoQg13Mk29sHWEmIlF8SISgWXs14LfAdZIOYRLfzJwFXZ4VNs3-yG-aJaQqCMZNB5oQaUO90JYX7mKmjsegxJ-S8kzKiW1OYaRFhuJjwJdYwxyJiWuSje6ZfaIuzC1kqByWR_8bA4nu-NLgasHnlcuJ_DmGHWhNoZnBCYe04RmXp9gMazGuAE2RA9MChwHWPSDN2vLgLIGNjhy99Qo4IIWb3I_IelWMEt96o21atPVlymRB-ckQSmJppMRMxtSaXhzcsyHvJ6Ey_OaMBz-A3WS3N8bZHEM6De0gL10hJ-RwSIIfY4Qi8sVHM_ITYG-IZaB6lI11yfGS7QM-Kkl5qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
روایت امیر قلعه‌نویی از دیدار با یک آیت‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101525" target="_blank">📅 09:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101524">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-vkBnVhWthaXyJqWTwvCxDUEhi3IxoVFeNUhfc1b2duF1HtkDeMi_dYBH_uSAiqTCD6My_HwI4zYTuDvaSBTdoVaA-3YfHwIDv1JOcKOhm49I5dd7tA8JxbU937oCTr3B5DOmaWEPx_ZYA-B0t-KY9MIpU742yPW3fksoa1GBuQSJP_FMH3Dj7rxhwXXpaC-YpuB8LfPrCURNHVRNeyv2dqgV95WMYSRPKBSYKgsHewwLad6JfH93zcgoIrfKi-oB9QxNxiISFQxBg_0Iya9xEklcfhHqxBpEIAK32gVfqcURP54aSc8uNtc1_3vkzhx_VVamxbqmS6FZGGU46MCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش هم داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101524" target="_blank">📅 08:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101523">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obim39LVcCFd3Nr2BfyRK6W-Inhbbryl_67rMFSXm8EwqUD-l3a52i213tIFU-sMnlL7i67DPtryPvXrzeSoOsabe6P8yQZhZ9aUg5o-JdNSQ8DXNdKu0pxcPxH5p8bQJKCrYwZpCcWRZmLUmo3tUSRmD6-9j37JgZ1ybmLwUvaa9L0UGFQpNjeT9qa_wHcrJVjIO2P2zyWKGgAME-_VCm3nDK13aVVFj8qxmehXntj5K1ESUWavrzCOf1Ftm812BMAOqjEKKdtxPottOREXXT9qq3C_maOaQ7PQXL_Ucr9rk-F_QuyAWqoMYMAu-WIuQODkkmYoS3ZI6TzLbbDsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
👏
دیگه قرار نیست بعد دیدنش بفهمیم که 4 سال از زندگی گذشته و اوچوای دوست داشتنی بالاخره از فوتبال خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101523" target="_blank">📅 08:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101522">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMZ5cfgwCf940Ov2GZHLynfGwQ-b3tLNSYFs6rvFht-58ELx9Rz2Qh_tWD6kzSXGK7nLDKA4jr-0r5BIzXiIAS7Md3U3bxaQF-GD7yWzzt01MAWdtHTtZiu0KVNZU9VwHoBbJePcnvoDOe5VYAq7Q0G5utaGBKzEFIqc8vksiklL2oOmF3r9h9VU-V3Nc6iHIq0yOrTggfYHCxPhxb0mR-XUqPhEyIw0MX-BzL1DQMSe8bRA_uc_wCo9YC2mi9N4fricZAs8ZgZ1nyvfldGp110NNBD1IXoydX-OJaOz4WKD1KrXVGRdg0Rik5HOOZ95BDfHW_qpebOC4nJ-QdELzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">-EURO 2024
-2025 Champions League
-2026 Champions League
-2026 World Cup
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101522" target="_blank">📅 08:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101521">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
⚽️
ماريو كورتگانا:
🤩
🤩
- رئال مادرید در صورت ارائه پیشنهادی مناسب آماده فروش کاماوینگا و رائول آسنسیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101521" target="_blank">📅 02:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101520">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7DT16PZENmHTdTv_d1UzGWG2i89XUYflRi7OL0-E4PgJWr5GOspYfk28n_wQ2p44nxWEvhuL79-lK5v-krGaaNVYJJ3mRHXu5lUZoxW298zl5PN4Yx7ejBu5WLiyzfCFAqlRe-mXpnZYtDy5j3h3gDu6hwISYkQn2Z6McebBJv5AX5VZjeCjmYn2MVjqNGXJqOSMczrvGsKPWxWaY3TA_AyLxmYuXyjE-MYtE_HBAuF9yd_K6Cx3V4_iEe21U02Fw8DBdr0XKvbftQ766MnXN3t0pa8P3jzmahlOK40-oTUo4E2HHDdPyMvPnvLUgOGB9gB7T0FBP_g48-jBe_WCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇳
دونالد ترامپ در یک جمع خصوصی به اینفانتینو پیشنهاد داده که در صورت عدم انتخاب مجدد به عنوان رئیس فیفا، نامزد پست دبیرکلی سازمان‌ملل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/101520" target="_blank">📅 01:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101519">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHDUiLAOA-e_-mL7f3snV7KiTLIyFw7b9LODteljFLFvTwlspx_acYQT1Ba1dQUYsFUXjP8w4DR8_w405hU4bfAsv82fbGYAffbsNzVpeTc6jRjrq_xoGGfPdweLA3qEseA1Okmp8_-stNTNLo5OIi4OnWEvjUS-6h6cZlMXMosLSEVE5mtzInWHy411IXOSHl21ZLmPA3b9nynvl6GKmkGikTs0SoungEiBMlZnRPEirZVot6fhEPQ3CUN9pi7glS9hA0BOdLW5lVPON7lqkCNJOU0RCTXsE4nnQnjBldMPSY59lHZ1Sx3nKBi8lCitW49YZ3YJSI6aa6g_Ugpygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین جذب فالور از جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101519" target="_blank">📅 01:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101518">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mocsea6HIQuGEVQQgOCWw-Pog949eR6dGc3WiAr1HbVuxcnQ5iErGqOCpWP_2pa0tWl2YeEauKkTvQqyr4mAUSb9fDXY0vuk_OebXfpG_lGpCCap_MIsjJgpzb_7duc6EVYjIMxZzoKKBZzRwkDLMZPQOKbMLdzNCZ8Zb1BBIkwuIFA0melR6wbxqlAF7gTnDnC54Y5vGTvevf2AuCKWWtXH32vT47kHnQrnJ-ZKARrjDIOdtWhZsIcZcyrp4krPuwiG1VJVY41Ifb63jFuVRhUEJWh4GsLZsMj5iw61ks_JxInco4rsJVR_macVcJ1zf_oTle8UQbY-bJ-WY467Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییییییی از متئو مورتو:
– فلورنتینو پِرز اکنون بیشتر از قبل، تمایل به تکمیل انتقال رودری دارد. توافق بر سر شرایط شخصی، به زودی حاصل خواهد شد.
💣
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101518" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101517">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101517" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWIK2oQe5MF1shfjF1DWHxa9bC_rHMSEjMgpXbzm5JoXMSHDU-SmqxzfF_H44Lr9CJ3ltXm3FzEohQAseXQvGBFv3NUYkl5tt02hOy8gvhas6kKaYFRPqsElKV_b8jRzLLFJs9TZu2ox56nimCekAM-J4HvTMr42TRlleZCsAJEmrOdg_5y2FCt0utJ9Tw0aHrgv6p0cX6ZCFT6zvxaVoDxqbaBsd1GDGiEN3ljLDTixK1MX04xXuXsc1OfmAePFDkdcPIg0Ithnil6Vq8yrJKU0ghdpO6cZH28oPcjCvviyRMvOEC1FTI8FBu0XYuVwHvWLnyTJLlwiNaOd9TvPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101516" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101515">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVG0NPNbAmhsFr89vLqGfJVEWm95oI6McvtCUiAclUS5LEUT63LqothvarmlfRC_5b1pqRU3k6avb7HBtp0K9dHciPqbRUO0CpCMZzk_fEFUuw0UXbD37LCYjapbkZ0qFwoIfK7b0lq7wYaJW7OdaaxltCC-8dJMuVd2C8JQoP7vRhPws5U8-BN49uDCWhYejzJmUmzudVPf-hmSag6GggIbYXyLUOBYofaReqLW0DhKzz4I6gt9a8w9wfrnlNB-WBfXahgKgN4nicb2z2KvOuF0DuqfLlURnpOECU4fpe8Zo19wStX8cndbqVBLhWdoP5OO_Q7VwAqtz9SlQiIPaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جدیدترین مصاحبه رودری و باز هم خایمالیش برای رئال مادرید:
🔹
رئال مادرید بزرگ‌ترین باشگاه دنیاست و واقعاً دلم می‌خواد برای این تیم بازی کنم. من و خانواده‌ام دوست داریم به اسپانیا برگردیم. اگر لازم باشه بدون لحظه‌ای تردید قراردادم رو با رئال امضا می‌کنم.
🔹
مدیر برنامه‌هام با رئال مادرید در ارتباطه اما بهش گفتم تا وقتی مسابقات تموم نشده، حواسم رو پرت نکنه. حالا می‌رم تعطیلات رو کنار خانواده‌ام بگذرونم و امیدوارم مدیر برنامه‌هام به‌زودی با یه خبر خوب باهام تماس بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101515" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=G2SIIBvWjluGXPfmnXYr-WtcB63ae15pxjxUbzhYSO5AB-LjHp76_uooREyRBhsa-Rdh9xEQ1nvIOBgMA4TJ1ESE775u8Qhw8BSZ9mKtyWj4o9g6_SbjZq5zKvUsBSZejkkmDfRAagPBW9nfni-MoF97nuNMyG1zqTFzHv6tFFMPZslj-9xJM5StJTQa1B-j-nvvym7C959CEbG7y3mpKlgzk-_4XioEWGorC_W9rOyfYjkg4QUFXhG5C2LLNCxywj1x0FTH0nb8AZUtYiMinY4y9RMshKJ-lkksIvbpA1zuiWGwe0gqHVMwP0QCi0JLW0YUA0PrugpO3nV04cfXyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=G2SIIBvWjluGXPfmnXYr-WtcB63ae15pxjxUbzhYSO5AB-LjHp76_uooREyRBhsa-Rdh9xEQ1nvIOBgMA4TJ1ESE775u8Qhw8BSZ9mKtyWj4o9g6_SbjZq5zKvUsBSZejkkmDfRAagPBW9nfni-MoF97nuNMyG1zqTFzHv6tFFMPZslj-9xJM5StJTQa1B-j-nvvym7C959CEbG7y3mpKlgzk-_4XioEWGorC_W9rOyfYjkg4QUFXhG5C2LLNCxywj1x0FTH0nb8AZUtYiMinY4y9RMshKJ-lkksIvbpA1zuiWGwe0gqHVMwP0QCi0JLW0YUA0PrugpO3nV04cfXyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی و فابیان رویز که اهل شهر لوس پالاسیوس استان سویا هستن بعد از قهرمانی با تیم ملی اسپانیا در جام جهانی، وقتی به شهر محل تولدشون رفتن، بردنشون روی ترازو و اندازه وزن بدنشون بهشون گوجه دادن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101514" target="_blank">📅 01:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikNBhMv4ZmWLPfngNjcJ2FrGSxI15EEppBk0k8Gy3Jtdqlay49wt50KvejwZXIkr_4u22XAJ5xly1diMPvdWoB2FpAE-9dcv7MV100Wnw7PjSq0-l9TRPWLwVvVbAibpIeLGqrQ1Hu9poKvEOiNE9OM4osbZ2xlN4iehDwHweuYNrncSv-aY6zkrXbOHMaBs6iOhf_YB7stfCQYe-04nRj5hYGlbsNAeZeifBWkGavf7WhzloE2xAoM8sgbns4t7Yj2ewfzHfNGtITzq-v2rYqRlk6fJ2SB1ucwA_Y-gHapCYKgkD0D5TgXH49i3yadK3kFBpSUbvZMNlFdrS8PYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۵۰ بازیکن برتر جام‌جهانی از نگاه the Athletic
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101513" target="_blank">📅 01:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ArHT6wSn1aJC07fih6HvNjuEYezDdQFyRmUSFDry_GHi6xykDCywQXNGC-u0ZD52w8u0T5IUQdm-LTAtVr22c9OjnTHdWcuEYECKmr92K3a5l1xjT5EjTP4G59hknF1kFYiQxzqgnZJTQYsq9AjcUqga--O2PJXBFjXa5TlxvzypfS7TD7TPSIMPKwrQgp0ZbOHGEy-b_1yh6zAjvF4a7uxpUX0iZzwcRem8I_S-XOVFCaAPiupEu9He37DI46LcKEXfjNBy-nK4ZSHIAxhsNtyX1TcBw_IYQiMCT1JkLp7pfvMjQz_zo6cWKOkby-oXOLlphD1h2IfsmDDxkPvVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
از رامون‌آلوارز: دیدگاه رئال‌مادرید نسبت به جذب رودری عوض شده و احتمال عقد قرارداد با ستاره تیم‌ملی اسپانیا افزایش یافته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101512" target="_blank">📅 00:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
قرارگاه مرکزی خاتم‌الانبیا: تهدید حملات آمریکا به مراکز هسته‌ای ایران جدی است و اگر چنین اتفاقی رخ بدهد تمامی کشورهای منطقه آماج موشک‌های سهمگین قرار خواهند گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101511" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101509">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJZ7CreKb5xjU4HmpwMGRhuVtLtECGMTgiFDM5kRkew5ZiBl-AowIVijV8fQ3ULCgeNZFO9yKhYrSXto73WbIpTh_HFNFA7FoHP2xrWXx0xPXsGoXM17S7RXvFlXoHQjDPotWBajdZAej2-hmfzvG0_aS_uVSZPilKxgP92kdwnobOu9Y6IdUlwHPPc7orODIGJPxUeq4bR85iqzBCVrnWuECEOF_uo2c0LMSZkQPc1HHIMaXMFSPGLOjmnRmlp_hwf0MXa8B2U-5kKgiTgqr2GU93cT9ugjRLkp4tLP6D3UVhCCWDX8B2MOm5o7OglLbsNxjBTowLp82bqsI8-JqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvryqQ3tAq-ex7rKZhRlKtGruYRbcagknVC4RDjUZx8N3r5BUDNTVzhDVeH__2FU7mYNmymPL7hyhokp-_Pg3PJCBRJv0nOWLZtec7j8cJw7vHMWAuZ0-Jti7fchRPmrWwOBqTMpOXmO1gVkOAcK4_MzLo_EYnxS-hnsbgMmTShNrmZ8GU-PV39RNsGyl_IIyuNGZs_A5zM_LblIT-D_XKIxOmyOW8tAIE-gvl9m5Sh_JzKnMH2oyprMwDSo8jZgiICROebRDCLZvyQEmU-zhXZ5QE_zWNDU_mT6JwsrM2w7-a5F5hqiEDiUWY1yjJjGpOQVEKQxAnjjMLN8tIBI1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101509" target="_blank">📅 00:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101508">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deGmcBaWZKlpeVBQ5PKBedUZtXX2_IPpWqMwmgo0TbD5gcZpx0iK-B9vqfkTquJHWSwkFx1Zvbl2VRKMf1t2upinlRMOpxW6eqIqCZqmWLSeHeHshonA7vDvHcKkN_WLB7fG5pGkEUUSNjogigULtVh7BM0u2vivooa0Pb57bPc0LgFaWKS1ON3IND_uHJvkewpuJZWPnxYCg7dH3YoE9vG7uD6rvG3GRsyrfn6y5grWEnWtnOgXV7zjsK128Aw3gErZyHwBpjYodd2Oq0ckb0s7DsTMoSGJjObVOxnbT_DjSfHBL8KixXETGOzyrf1_DgXO1SLGVWaK-_Y-bqIfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101508" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101507">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyIZx5_Rml4fgPnHwaHCtVdcoyPPtQi4iTM7l1MoUSx-tVrMPUzZhq-SFuKXPm231UQFN36F9dtygF_dcd8fXkpK-AN2lAbz4NcsZd5Lb3CL1gVEnECp3UQ2bWZCAM6Du9Dx07gqOuRePFq_AaGee1Jkznr7dOkKYy5HZrQkr_JFy93SspTJ509IBurRB8g0G3ZXgd7HhFhJmjozH7btYiGjnBduE2dD0tq-nRo7aGPsl_E0O7RRgOikEV2eFB9RSNb6dW7iyvnIuB3xvEYUfjmI5FDwfK-iGB0552wljFb2skTjpqhUiAzqHhaWdD40MCbiy39s6YQ474SVjVX9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101507" target="_blank">📅 00:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101506">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGxfwgWXyRjxhUbj2FVSveo_2XbEeFN_TcA-HnHL2_DiPUg1TwwcbJNwQCeBePPVXmedZBH6tkyiFTy-pfDdgdUrZuE0tzM6JdXGf7Do9I9iVUr6RA5oO4TrORrdAwM9e0DCZlNtMNlJ8ZQ5oTbYhp3uCqtgKGXjrckM5m_xx0YS53pUJJqO4KisQELCHhYMrUl4KFIbIkzRljlVLn4pK_e_F8utG9_-K6ZrVcXBGjHUd4mgN6w7t0nQwYJHhc7ggZrF_Uk0SxhoqP6pCcny3jHZ7O-bALhpjNy0-polKIyGMWaEgunor48EsSpGJ8LYBPehoEAbP8q8apFsk_Dtkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101506" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101505">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">راجب پنجره
🔵
🚨
⚽️
امشب باز هم از علی تاجرنیا پرسیدم و ایشون خیلی با اطمینان جواب دادند که پنجره باز میشه و بر این حساب هم دارن بازیکنان خارجی رو مازاد می‌کنند و مذاکرات و میبرن جلو، بنابراین امشب دوباره تاجرنیا اعلام کرد که بهتون بگیم پنجره استقلال قطعا باز…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101505" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101504">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXvG9S5h6B0rAyd7EDYNrf0yVWzWCpEE20d3173Zv1ge-kVzScLgbaJN1VZ4I3U7kfW3N8tP0rjjW6OeorF6qtqpphc0vNJfUv-Qbrc1SydW8u2zqe102Xbm36npwjbEBU3pE8S0o_yR9tGnSGSv2dXVUBRO8spZLR3jePF32JxkLlnF0o2RAD9VO_wW8rz2ZSguZ7DGpKPPpllaC7JDb5K8NDn0M-3gru7m5RmJB0rIThgIpNCnqXWjE9wcFa4XKNkhR9IuhHy3v0DXhWJQvtOFr4Mc-kRkEJuPaa5nhogSOm_I-1f6dK4A4woUaOtQxA6ibuWfQSSDXsWURsdWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان:
پارادس خیلی خوش شانسه که من تو زمین نبودم! وگرنه یه جوری با سر میزدم تو سرش که کارت قرمز بگیرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101504" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101503">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlzMQ3G7p50a7KUiAczKXpEX8ckQ4M9hUyL1T3RBdIFV3G_UTL0t827UM8t1YSdabamUIpJkP9qVsd38nSq2MREReoPBkMn76GUL7lef6N1PIr9o0_sPKkMY26h25AEFgDdmvr0v8TGAYLanzIqh41K4P1wQ5-RGOv31ExgerX2E7cs0UjE1l_oZrO-BLNXPwCjjRbqXLkoF7l2ZscEGJMJWrCXbl4CnkWoI94gGhQF-b0YkAUgPo6dpQ06kLCuezahvUexHpuC_E-eSUBGtWjf08kJMaWoa7Wf13h7VBjpdPwsFwZffXKnscMT86Sry2LYsEA73N206hMEaVV7gAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا بازیکنان آرژانتینی که پس از پایان مسابقه رفتارهای خشونت‌آمیزی داشتند، باید مجازات شوند؟
🎙
گاوی:
به نظر من نباید آن‌ها را محروم کنند. میدانم که این رفتار تصویری مناسب برای کودکان ارائه نمی‌دهد، اما این بخشی از ذات فوتبال است، و گاهی اوقات خشونت نیز در آن وجود دارد. در نهایت، همه این‌ها بخشی از فوتبال است و باید همیشه به همین منوال باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101503" target="_blank">📅 23:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101502">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=WDOjKkhBAaS4QF43XvYZi2AGrMCEJzw8CnPJsyDvF8FVVkPAcrpguJMzOBDlE8Xs1Iv3NQgOWapz4qqsp3vYr5T54HZ_ulHi6Fs57-naecIOlH7maJDv2p9B1w2auR0UqoeYmD23iNdhP2zJoJt1xduBQ6tkjTrSGj7mk7Ub0LYhRVjopIOtuwmN8k-INnCYn15ouZWN_aQWHSyVI7mHsKsX-TxpLPjPemfhY0pq8xT-Er-oY-_ji-3tXUg6Ax6-mmR1S1bA3XPiL3k5efWBZ2Dbm19hjfbFSOU4IB48qo0-f7umiw9YbD7Dt2_bP9NvXcuo0LYpjSFs6cmL56hKrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=WDOjKkhBAaS4QF43XvYZi2AGrMCEJzw8CnPJsyDvF8FVVkPAcrpguJMzOBDlE8Xs1Iv3NQgOWapz4qqsp3vYr5T54HZ_ulHi6Fs57-naecIOlH7maJDv2p9B1w2auR0UqoeYmD23iNdhP2zJoJt1xduBQ6tkjTrSGj7mk7Ub0LYhRVjopIOtuwmN8k-INnCYn15ouZWN_aQWHSyVI7mHsKsX-TxpLPjPemfhY0pq8xT-Er-oY-_ji-3tXUg6Ax6-mmR1S1bA3XPiL3k5efWBZ2Dbm19hjfbFSOU4IB48qo0-f7umiw9YbD7Dt2_bP9NvXcuo0LYpjSFs6cmL56hKrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپی که از مقایسه اونای سیمون و مارتینز بعد گرفتن دستکش طلایی وایرال شده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101502" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101501">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHKzHN9QlgKCtNPZgEooxxyU18XLBshZsVMrX9QW5jfbX4D1Nm03Gj9tVGUHu5xYtbxuN0ITCagj9t5Ew0pRpBYSxwhXRlwfKQM4LYrAfx9isZiPwi1JzFj41BnPeLGL0efuvC2CWs4imL4Awha_7S26j-p3PE5OnzilLCRRXGknvOS7NU_EtMDiA4Enx-0ty0Ljf3RgFnuwPkueLdl0HLI9SznT44M4KCgCqefelE5l3mJOj8klSACBISe1hFs5kCoZJ_CxrjRCryGsgi-YGH0wDtyh_a7qgK7An2PXuYlByV1Uf8WVoeo9w62P6v1LT4RRowByNb_dsa-Mgeu6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
توییت جدید امباپه: من برگشتم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101501" target="_blank">📅 22:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101500">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9116787106.mp4?token=fvbobV8a5rgoLEL3PLFnYDFdHHB_otEvUsVM4lRipAgZYu5ReakJfUsdGNDR6UmHo4WmeTjXIiGgg28Fi62o-Hm4M0zGRc3LlWJxqWfunZUK5-2EPV3Z4yGHDf7gclmlGW-kY4fUTXNx5j5CQnlxMgsaLlbllfVGEl7UauH8-WZ7Rbajy-Xz5AiM9ITY6R_ss9QFn-yNcHQPoewbpuzvMLM6eA7pDXAiEht143M7AN3rh3DcnZRW6QhySopkVakzT2kLe7uQcV5j6LEQX29Uj5rp0OXKu6tdJHo5GQNvgzZV5z9IhcyUwNHy7uicS1-lXkE3EY5KhNA9nhGk9Y1ZtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9116787106.mp4?token=fvbobV8a5rgoLEL3PLFnYDFdHHB_otEvUsVM4lRipAgZYu5ReakJfUsdGNDR6UmHo4WmeTjXIiGgg28Fi62o-Hm4M0zGRc3LlWJxqWfunZUK5-2EPV3Z4yGHDf7gclmlGW-kY4fUTXNx5j5CQnlxMgsaLlbllfVGEl7UauH8-WZ7Rbajy-Xz5AiM9ITY6R_ss9QFn-yNcHQPoewbpuzvMLM6eA7pDXAiEht143M7AN3rh3DcnZRW6QhySopkVakzT2kLe7uQcV5j6LEQX29Uj5rp0OXKu6tdJHo5GQNvgzZV5z9IhcyUwNHy7uicS1-lXkE3EY5KhNA9nhGk9Y1ZtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👀
خداداد عزیزی اومد یه خاطره از اولین سینما رفتنش بگه دیگه جواد خیابانی ولش نکرد و دونه به دونه اسم فیلمارو میگه و اشک عزیزی رو در میاره؛ خداداد عزیزی میگه من ۴۰ شبه از دستت چی میکشم آقا جواد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101500" target="_blank">📅 22:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101499">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4GBDSGrMjuY4PDegbP98Mt1_0ec-Vh85L5ofHG016CjU1EjVDfy1rDWpvOr7_TjUg8DufZx46ezpTRa_sukb4_6UclxwieOIB242pMuAfUg-ftHyJnPDbqBkI1D2xZ6oPgH-hic-wIk_wnNh-AK6zdgLASzPk4EvxnZAjMCFjrKYbyyGyUDPFWfYgfvU3edtjNT8t6U4J84bv7rya-a8M0d9qRVATkVKn6FXVB4S0z_KgUHystzfFHzBv7qKYwWmb9gQcuTFoFK2AUv3iL9hUWdpWqd1h50kfjl_V7PgWPjQGcVujWMOMUpo8b0jfKEfbFLa_ba1IJe9pKfFK0Tog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🥂
استوری جدید راموس در کنار لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101499" target="_blank">📅 22:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101498">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a3469819.mp4?token=NUMUQnbdqa2NCS3OYJw3R9VtjhC8sDdyZV-gRygA12lEvmrcAWTwlQhQ3dRkWktQM0qNO78gJ_cUtwBiyftDtMqjVB4h91lJYBmRxBI8zmlWSIN-rnDrYbXCWSeSQwiHMWPIdBZ2BabfbeS7yKEWZRhLtX8cSiQl7NbSDCunwQycDGAHmlUBbnJIA7Gpha4qY-689aVpOoBVid0iWnLqfJYzFEOJHzRIorK5JUG5uc040qm9Qc_U8aYhmQPkHwjxF_m9iupQki15jjUzgdWTB-aMA5n711BAAx5fV32aVgjj6-y1J3ewoHKtHR__dAeydRk-ifiTDJisHOUEIaEAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a3469819.mp4?token=NUMUQnbdqa2NCS3OYJw3R9VtjhC8sDdyZV-gRygA12lEvmrcAWTwlQhQ3dRkWktQM0qNO78gJ_cUtwBiyftDtMqjVB4h91lJYBmRxBI8zmlWSIN-rnDrYbXCWSeSQwiHMWPIdBZ2BabfbeS7yKEWZRhLtX8cSiQl7NbSDCunwQycDGAHmlUBbnJIA7Gpha4qY-689aVpOoBVid0iWnLqfJYzFEOJHzRIorK5JUG5uc040qm9Qc_U8aYhmQPkHwjxF_m9iupQki15jjUzgdWTB-aMA5n711BAAx5fV32aVgjj6-y1J3ewoHKtHR__dAeydRk-ifiTDJisHOUEIaEAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا حتی سطلای زبالشونم شادترین سطلای دنیا هستن
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101498" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101497">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD7S14CXQkK2WQKm3gKx6P6r5hd0HmPdl482Jv852YqRoc1KzaIXmHU28zoNUBiSPx2_MZgRDsuffer0Q26sFAXCbJphoaH9Y7KxLF6uVuEW2F9UOwI1EtryaFrc7BgblEypofWcslEjkJtDvW35AEdCyoQU-vzGx15jEwO7rvRwWGmynfsnXylxEG6cRl1Opc4cLCtbXuFp6b9Mqfb-xaa4NZ804YkQZX7kdoW78saTyC25XN9n2_VpE56QkUPyfEzxZfWgOPchuTGet0UdZtQZNXhapWs5iF6vuNp-66s8K2pmJ1hRy-EcJK3ENQQbF1gJsmvxl-kLRhFK9nl6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاویه فکو که داری داداشششششش؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101497" target="_blank">📅 22:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101492">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMX7ZOeqJi2idTUeBWCzVXb2RDiXuGO_d1dPEvMhn7f6VYEkqqyjLNZmoMCNeTC5bvdQvVmTH6Ai5ag3KTOKT2IQqrlkLs3Bi2M7s22ox1OtBSz2i7aYoMNd7mxZXMLGPckjI3AZiUOGmaFO4hFkRQCw6tQ15D-XbmFSrCWMguJpdK1Z8cefapR_rCoEZIvbzs7ErkvJ_Lw35GSQQyNPc-13HGj71WSVo6RWM_K8YuXYbE7Rdl0_-nvZ7OpgDb0MRGGCgHeWw3rCd8hlniquRXwi3-BAcAdRS5hs7EsRCo9xLRn37nIm2-vxKGxRQr74m13foPDyY6X4oMbXuBw85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/herWWK5fgbtl04-q7-RG4G00Rh9C71bU_JmZDJp0UiW12sNQGQx982b_pFTiGrnK-aoxLIPh8qLXCrt_bs69EFQMH_uzHoOepNGVKb34mNhQPK5ake37-BdOakda8yZ_4MDuqi0fch4z5PoFn-AGXRx6mCPxPiWF2R8gi1Y17eLBGDl3UikGOFEiVKPzD5G6jZJaXOtot1n5voS2oeHX2FrRXYU1hZ6qaYZRCJVsVoPRFHwJ_amx3PYdTLGtWX_2q_T9KXXk-w4gHowdIS5XexO75w-xj7PZkcqqzNJQHAf9rJimni8FVa84aAwanXNJu_EX1TdmbMXnHf_UieBKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmezcJTyM4qjPl1HeZMAQHx_C0EWPYMBW2KSgNvY_HU9gMh0sRT3JRedhuM8OAJRwvqQE7Wu21rNDcMWKBKThde2IY5to32lXZb8Z19AyactpNO2JOkI7nJE8eGcqe44hKsvULYPNuerqJgNUWBxHheXxqzjbXYyTELcUU_NqlmDucqMYHoQZRKHuHoQTgjNCfxpnCVK82iFyC6aFO4TuCQKTjbumr3ZZxZ5U7Bwhgz7cTFuLLqQ1T_FTmUZzS0HVkTmJJXACQ7k29NUxh34-oy-1A7_RbMpeiWQRYZ21QgUCi48yihZx45hyvA4wbX6xVpc4ebYkeHcOxtrlM8kbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4JQCjbohzMTIFxBljQNnoBWNDLDj5dilk4vfKorugAgRaJX1OWLY7hhWiYQIejZoeg09pit_as0BDQOgSlRJE_1JknIXsu7JGA0FCO54DjQpVmA39ejiosI0JKfA3LQT0Lm3eRULqFp8-sivyftb_DZQvQBl0jyuIg5JCiP-rnITgnxWpzNVtkmVwae6Jrnqca9UbPSjTEGThu6ggnBHWEHemgKnItk75VO5Qez3rhYlvzOtiPuk4gegj7-ASPH5ZpK3k1gqhfsCjwBLw18JhoUKLUkEi6iSLK9wAc0uhk8mJUj_0-ppWqAsWdM_qNinZEnYzpynRMjxNaA283b5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g745Vd-2LgS8lNAhtSlap6ZvNGpgqpdSrVFTBzb_l-4BMcv9P778dRkWFKGOVX9WPVYRpU49oMKMk4Hh7kcmmdixLY35r0bGUrKkJtr5hpqK8VJG4IFdCHNozxcYyb-tdeJTRCMm-JOwWZ832r90TfXOcw18pqqVnBrO-5_aanO2x77029532PZXdqZoWxOd7tJTQOEjMS9mfAG2Fjt9LQktoNPSs9dgbky-hwzZ3faYjXibpYHngrVZhlGc2E1THc3dIglfGjjjPiV5I0FfTiI3C8beHZrZeaVpvWNR8DDoAWnmf0ZhPUlaw1dFuvjPPiLo9PLNWLDyyKUtay5zcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
تعطیلات تابستونی وینیسیوس و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101492" target="_blank">📅 22:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101491">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=MGfRKbf43as_raSbdOR_WdlmFfa5GKsuvkxBmwyk_cTMvN4ZjEXIcJuYtT9erOhztVk1pRuig_pvW46NwoGi_f5d0_7BYQhhFrTdbOB7ZCClQ4UUv2N8rtP1IxHI9u1upauX92Ql_zdD7jOx_cve8_kQCW_Dl8FLAgIV7v1-y5HmfUh1atfNnRVoHcGWtRGvu9FADVMH87RnFg-euq4_RL7cdToTNMfuVJt0z1P2_QZDd_CEiHHbFpa0QU0q6Gs25wJGXGENOlb_mQLkOqKQBqDAYcUQlfajrZO46B9k4dvKK67ofgkONgwsSq2vU097t3X9f8eDWgfGZ3IuUh9hMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=MGfRKbf43as_raSbdOR_WdlmFfa5GKsuvkxBmwyk_cTMvN4ZjEXIcJuYtT9erOhztVk1pRuig_pvW46NwoGi_f5d0_7BYQhhFrTdbOB7ZCClQ4UUv2N8rtP1IxHI9u1upauX92Ql_zdD7jOx_cve8_kQCW_Dl8FLAgIV7v1-y5HmfUh1atfNnRVoHcGWtRGvu9FADVMH87RnFg-euq4_RL7cdToTNMfuVJt0z1P2_QZDd_CEiHHbFpa0QU0q6Gs25wJGXGENOlb_mQLkOqKQBqDAYcUQlfajrZO46B9k4dvKK67ofgkONgwsSq2vU097t3X9f8eDWgfGZ3IuUh9hMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"اصالت یعنی به ثروت برسی، اما حاضر باشی هزینه کنی برای کسانی که سال‌ها از آرزوهاشون گذشتن تا تو به آرزوهات برسی.
بعضی‌ها با ثروتشون دنبال دیده شدن هستن ولی بعضی‌ها دنبال جبران سال‌هایی هستن که پدر و مادرشون بی‌صدا از خودشون گذشتن.
شاید ارزش واقعی ثروت، به چیزهایی نباشه که برای خودت می‌خری؛ به لبخندی باشه که به روی لب ها میشونی و حمایت ودلگرمی ای که به دیگران میبخشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101491" target="_blank">📅 21:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101490">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be44UaKZyUfXbNUTFL14ipzvxeIXB4jWWVaO0n2u2LOMKQNZzlvmfaqaxAY_cb-TAaTGr0wwGDhd_b0K2G7zyiAO-9EcsYS4cjCCit5yKlHyV8PZgDgw0caqxj1icSjd7x9AHKQAdLKhdhPp-lFyvUV58mKcxeC8W4nxoIzUOKKaT4GBcNFciY99K-F5lNDJ1QRzzpSqgaXrDaQQf1ZPEh8CH6DN11rhnpR-awp_D6BWihdSnczF-ZkWRYrZ-B7ukQuNYx5KQf0J8Clj3HyGwItqFJ0fdEfmMu7iwocWNIcfS1Q0PBm_rp7vsHTsTkXsbBOv_yBEsJM8tAEgcpcSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
تیم منتخب بدترین بازیکنان جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101490" target="_blank">📅 21:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101489">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVMmN51SzDw7-lUqeFOEGK1vphoSPZRjkJ1ptxycqBuUaIIa8TdSuXCdk8gaZ7xQsy6MShaaPPDG9FrxRn95LYoVFmV5pk0inPBTqsgld2gxK-kTtE53THmkdnG6hT25-CbK59orUmMD_NpGsqSuE4iaDqFKgGhuBFoIbkiHIb7YMJrPuT-ON0u_Aa726mTw60qvv6bmK6G1lthV4PMRIryuujemmndKsVXSgPLlT3JwoDLfcAQJEa1bfiITMdXEcihSylrs-KtkwCSU3Cbo93mbjASDB0IPaE4c53hR1ofEffHz-FblQsOTGhW4JP7rKPKSZLI9_Ry3VCdLhEyMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید وینی با چونه جدیدش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101489" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101487">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u86LdYyj0SaEqgh2iupSfFzOrvnM2C-CHALOIpGu_Y-NTWyvCz6LrJ8uK9HjSnX29hSF6oXBq-7rmVANIYXRFhWE4n7ZN_yXWquMwUB2vmXp2v84lEmVoiJ40Bgv699yaf2IYx169CFubxTzwDoRPtZOPJO_w14gkapDiznChm8xftrBH6f8e52jdzVdC2rRy7hm1S-oPs2xBdfmAu-N-wsZezQbfHMIsbGZ9Ao60YCQ6A5kW9i99ifTTDjSxC73y2227Pc82xj6uhqIEs63M03pborAy7dx-t_C3iXE_8h-5kk0-fiDwSBFGXbltfhdlAH_wwZI61M-qXfC_g2gZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان فصل 2025/26 در میان باشگاه‌ها و تیم‌های ملی در پنج لیگ برتر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101487" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101486">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/selmbL9mowr-aFGjUPdhd2krJemWsw0gpGqMz9M63wP8Cd2fXpYcuSV6uiGOyzmHyG2rz586WxYcxWxybNgKw0dvQc8egF4ZD3yXfCgMYbCLBPQ1eVOI6KL4z-Wk6jxN0eC9gxIVT15GWaXwp5m9rBP8BO0K-HXjQx0SA9jIHLoG5NUDJmTokknz5f_nnda-0DezMvhLRuf0IDuHbwh2n0TEqB24jQB9MzXoe7RTqje9-DOU9vlRM9tzrTt_r-l71SolhaBECEOYSG8DJeGfSYMlsoXEj6NSFQ5vBj_CDe1rrSwgch_PZfcA1PGRDGAHGrsRapgM6OC1qT_qRzOyDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رادیو کاتالونیا:
🔵
🔺
🔻
لاپورت جدیدترین بازیکنی است که خود را به بارسلونا پیشنهاد داده است. عوامل مربوط به بازیکن با لاپورتا در دالاس ملاقات کردند و ایده حضور در بارسلونا را مطرح کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101486" target="_blank">📅 21:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aji6Id3WbEOtitWInNZ8AukJPZVEqC0uPfsLOaJDbNKmkaebue1M1zFHEDXhWDMvk8coSuk4Ylwh51ZeFZS6ekkRFizZ4vBltKAiqxfFbYZHFpUaB1hnQh8rHypXstQoF1coCEFoxLcs490MtIXO38Cu7IbdkfTKZUhUQDGsT8jujqgbeDgxigcs1IJ1McixQh4g1GogQb4OTrni-HtWP8qIatdTVh1vSMz-uYe8qS-TrsL9NEq-qkORAIF7drNnvIUEBkPjNaP8vfqYChYbVD2DqtOhLCtKwAVENwtWrf_TPq2exL6ubGzuFHnjMvjQ_YNUQJR0ybRIVBczUiqDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWHDkf0_b2bMDQi9UHYV0_H-fG4Jp80QMe9dvAH7zZIT4a1tAt3JNpiLiVrWV2gN6JpD_jtlwERkOeTyK3zNtxuzMnmk-LQSgJf3tkfz0pnLgPZpCunWAtfSHNKuDyYmP9YrJOrtPywMGTRzySE9_-zjXpgr3CWfaEtUOtVWqsQZmCnr4ixqKEVR5zfhT7Ly18vYFuz_oULYCkPOUiQiYNj0VYIEeomrYBkK7YwywtCMTwb72iFzoyZPdBugxsGieD77MSqLmc-c_7tRDLog96Bcu06jIj7bs_HM-Yk-qzPtVLtXFWOMe4FKHn27ZrRgpPaA49eiwKEIVNq7nGuEiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😁
زیر بغل شکیرا از آینده‌مون تو ایران روشن‌تره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101484" target="_blank">📅 20:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkBJdO4JmCX2VrVCjVnf8wtP0kqkDCLDaeekOVLxm5btnlFnc9laUc_jUPkKhEyGtWpKe55ctJEQtrQguylBJPnz06AHru8P7VVAYjgbDVlgGwdGIP-PjTt8v5mJpAxo9sIFWblE3TW3QS5zPTWDooHl8BUjrgV2VfCE6Tqgpedju6IH32T5_kuYjpCHcSBILtLtrkHqBENLisEBQqJaPvQPrO3c1A6MyPRaCZC3AwxF-3Hz9Yczie1THla5UPgC84k3HrVzzbpthLF-qBuqvY5BreJ7HWiVr60J8JExG-Ccyn748T7uIBRAt7Rk5Z4aeK05UbqTDAW8RUVsYxrksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
فوری از فابریزیو رومانو:
🔻
لوکا مودریچ قراردادشو یک فصل دیگه با میلان تمدید کرد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101483" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebxv82z_PHxSYMv_N8s0YBIcPIdbXHjD5Kp-dVg9jXDpqKcjdr7M8-zD6LaKXiJqjKF1opyc0Bm_bG9Xapat9fnaEU_9uEHKu1G9QDx-62MjuosKCJklbqiv75BiU_KqGEo2b6yOLmjRlvKydTtaS-MMBMtdc7cZTjKmlClALgx5KoaEEFiFtmMhek8_qalIEFw7-8ZdCdQeR8bJ_i111-V8937QwFCwB68L90aUh635eU1f7ONPMOFB1i5lC0bYWAdTv7BalC8uBVOdfE0EsSZ1Sbb1T5e6tO-kD2ob17u4a4swXu-gGEaO5n5ZwCXBubURSTWllyWxxnGR36UC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
||
بازیکنان جوان با بیشترین تعداد دریبل‌ موفق در تاریخ جام جهانی:
◉ 27 - لامینه یامال (2026)
👑
◎ 22 -
کیلیان امباپه (2018)
◎ 19 - جمال موسیالا (2022)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101482" target="_blank">📅 20:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pun0ZNeWgXZ4c_uT2yYxQ9E449RWJ2Gb-7iCQsBvyMOtKHW7Qlyos5cb4fomet9JX4FAGfAElMRyBzNwOG9mIA8a253W2xebQYf_Nf2q_4EqkeHo0mJxwN2YYs1sU_csZb4LQj49mPmb4aO9YHwmGvssxHaDGQoBmPinqmIdK_ok4efD2-Nj6D7aiPSoC9FhO-vXUKpJPGCBhMZhbwVVbD5LBiWoAVmnLRKFiUQagK6pNGkQCYULK0CCfo9kaUQlfcXPuo7DBSj7nSBV1545IoxwgJbfn16s9icipNKFMENeo-pdXwYwtod92WvSP_3AhPLmP79ZR22Jl4VGVnsjYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه کاور EA FC27
نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰هزارتومنی برای خرید این بازی خرج کنه. تازه اگه فقط بخواد آفلاین بازیش کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101481" target="_blank">📅 20:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101480">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgYiFgJ9-DmBfL7byrOlwv_vGnO8BxPoBSHM7zxnuD4HInuev1qPjvZ0oQOIDLr_D6XOCXgN5KuAi7B-NZHvNAnumJ6y7B-4bEzg7AccaxwMcKS7-y3b6J3Gffu2C96tKsTU2HgTuHTd51ZCwDnZvxTVnn8Z6_8x6w98skeHyz3c6B3-V1ME39fDHvSgMVGn2Zb5Rx2NJEpdAnY-3-VMR-YH1KkgmezyJdyIU0Iubm-rSiFVnb83chANC5sXoiBnpwPr1vbpOlFcX0dYmYnUyjuOItYzsC4KPMReH8sUXTqHPLwJEC96hLPrCod1zUyY06BYfgPJf1wwdqa6z0hfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
گلوبو برزیل
🇧🇷
:
🇧🇷
• نیمار تا ماه دسامبر در باشگاه سانتوس باقی خواهد ماند تا قرارداد خود را به پایان برساند.
‏• در پایان سال، یا به یک باشگاه جدید خواهد پیوست (اگر پیشنهادی دریافت کند) یا ممکن است از فوتبال کناره‌گیری کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101480" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101479">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=IVzn1dQ0UZUXFQEykBU9QMrLcN16Jq52yD-i8FMF6tCQITIvte3fa1nF4-tz27VPd-O2RRVPpdwqpRwNfBr0cnzbk9X_JjKrS4RId5s7ZCMJcdmerAjoW0j4ONBuaUu4-MKuqRxC0OvSh6FHLRCwPuCqdf8QvqK178dxqKJUwXkb-ZXAzudFPcl1d5GQHVJXr5Fat3KYZIvhNPtdClQF5bkzB3pg30ETnLgj8QhUC5G9ztKodJChh-7QdAmLdEq9SWLC4bN_Hc4yCsW0jIlTO4YdlJsIeRvqq_t4A7V--uY_6iIuTAMrSIqdXdHlULQFTNf_piLKIkJRyzJkD7dq0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=IVzn1dQ0UZUXFQEykBU9QMrLcN16Jq52yD-i8FMF6tCQITIvte3fa1nF4-tz27VPd-O2RRVPpdwqpRwNfBr0cnzbk9X_JjKrS4RId5s7ZCMJcdmerAjoW0j4ONBuaUu4-MKuqRxC0OvSh6FHLRCwPuCqdf8QvqK178dxqKJUwXkb-ZXAzudFPcl1d5GQHVJXr5Fat3KYZIvhNPtdClQF5bkzB3pg30ETnLgj8QhUC5G9ztKodJChh-7QdAmLdEq9SWLC4bN_Hc4yCsW0jIlTO4YdlJsIeRvqq_t4A7V--uY_6iIuTAMrSIqdXdHlULQFTNf_piLKIkJRyzJkD7dq0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
شیرین‌کاری لامین‌یامال در جشن دیشب اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101479" target="_blank">📅 20:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101477">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=rOivgZ8Dwhi7GI2xccyOpXC5savFS0wRqbSG9cNb8P8FxjMETB1oVL5bXsvDadwkSs61kODFDPf1-LDwuM1XN1ja2KrYcFjFTJeglr_MD0hMkwxiazwmti-47Yxey_Z-iXPgO-x5b3tzPfWWkwRr1jnrk2-rk-69x4RfwwWWDE_k47YZejDe4YBRJHMvXygmJJmKyMxAj2Jlkrff2Rh-1zkHZ7PN7CIZPxf-Yom-MNwoKduTmFYIflX3-t5fQnrrj1WXV5uorKZ3fhjfgn_oJNKFfW4sNdLW63Qhnat1hbkpaiW7CKDdwSUAnaxEEkJUwuBTGi-2vWfH0_GXhqvVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=rOivgZ8Dwhi7GI2xccyOpXC5savFS0wRqbSG9cNb8P8FxjMETB1oVL5bXsvDadwkSs61kODFDPf1-LDwuM1XN1ja2KrYcFjFTJeglr_MD0hMkwxiazwmti-47Yxey_Z-iXPgO-x5b3tzPfWWkwRr1jnrk2-rk-69x4RfwwWWDE_k47YZejDe4YBRJHMvXygmJJmKyMxAj2Jlkrff2Rh-1zkHZ7PN7CIZPxf-Yom-MNwoKduTmFYIflX3-t5fQnrrj1WXV5uorKZ3fhjfgn_oJNKFfW4sNdLW63Qhnat1hbkpaiW7CKDdwSUAnaxEEkJUwuBTGi-2vWfH0_GXhqvVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تایید دریافت پاداش میلیاردی از سوی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101477" target="_blank">📅 20:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101476">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIq3VIAwBlikQpCESEx3iz_5L8uatkayyKwzexeLshs_2KoPVNm37RtBwcHB5hgX-Ceq-EhzslYYGxde1phSA7BKGHG9QjVGkW0IcQSZ-GqT86PhZrwfgCRM7TCuywCk4UvU9CRDnRsoNnS1Xxdf2NEQBimsLiboTlgRduXsJcnwGcbE-0pjxQjP_8js4CTR5mj1JbWi6O69m_JlxxAgb-tnS9DrZ2_2IpqGBtH6L8DCB4g_UHRKOc9Xbtn2pvT0suV7RX8E3pf0GccFKrSuR-mn-cqOe6tKzde9nn5pF8cXNnA8ICfM2QC4JrUNFQBq-GeXV2mqiqTt77nVxYkGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بازی های پیش فصل چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101476" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101475">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=QSp0zHfOda6mjhDNOsLG6I8y2zLdPWgkLzoF6yQYj9_NTHsGKzRQsuYcS8qIGt4ccGXlN35-RLN7W0LVfZMJEq5GOgxzoLJuq8IIUTgWCvYsRw87G7MVVqzFY_PGxICMw1S5n2E6F12pHma4Y2-piod1eJDslll2gF_b11VjKGqJawhPoSl19wooMZf-EFTtVOGf7QB6O7kDaIECye2f90fbXvtqNebFBvTLXQXDpTyIsMLbuUTvrNyLjt9NDaSX5MBP7MWSj930WQKUisulERx6YQ8FTrvzGjSVw6bRXQCOOywCXPrvKhWbldfUXfgdiRRGyMn4z-se2StMpOE4Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=QSp0zHfOda6mjhDNOsLG6I8y2zLdPWgkLzoF6yQYj9_NTHsGKzRQsuYcS8qIGt4ccGXlN35-RLN7W0LVfZMJEq5GOgxzoLJuq8IIUTgWCvYsRw87G7MVVqzFY_PGxICMw1S5n2E6F12pHma4Y2-piod1eJDslll2gF_b11VjKGqJawhPoSl19wooMZf-EFTtVOGf7QB6O7kDaIECye2f90fbXvtqNebFBvTLXQXDpTyIsMLbuUTvrNyLjt9NDaSX5MBP7MWSj930WQKUisulERx6YQ8FTrvzGjSVw6bRXQCOOywCXPrvKhWbldfUXfgdiRRGyMn4z-se2StMpOE4Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفتم قبلا یه جایی دیده بودمش‌ها!
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101475" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101474">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101474" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101473">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0xS9lSxAtGamNFv35aRNuQIXH-RZh829LSslGF_UdcZzEKmCCYxzwxz6S12uaEJ1HSgtsKuAXUeq7GDWG5SMZhcaO15aVxV3-4Th4x3Rg6b2QJLc-c8Qew2HwKjr7ClVzqqzYTa8g_Gk-IsgZPRftyal8H6H0HcuCxTrrAV7Bn5OTgmL8Ll6e0h34DlWKabfQo6KVpB_M9BSIwUi2X556X1ohJ3upoZ_mxHXJa5ellFv0xMv1z3BD-c826c0P9rgX8NR-3AWTzgMCfCXqvRrf74cKrm-P6DnSIacRGRTBaYKKMFxssWsId5dVorkPoDA5oNex-DlkARJd-pX6yq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101473" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101472">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=jR0J8ZoaBK804eGoX-DZeSBYoJTvr59BlCORiEl2FyPg_93MgwO_mC-zNx_S6yH9DuUjmNBy1A1WhK2yCarWSD8yF6_wjv0vzWtGegTKruuxJQ-RZdzak-FG_rNU8WQ9yxDVT7Q5Gc1J6B1h6IuFYEHSVp02RHce60WiDNurQhG7yggsRLFo8c9IrkXOwoaN8Bhh2s8lO2OY1rO1ahxAr7BZKHefe3jYDvvnuqmX7KnXBUSpCagEyUv8AnSqkU9fqOj3JS7U4PCoHqQCA_N5R0flNHMNoBKSirEFBAQhgid-MawoAxfK9iDgi8T0JNMRKsgzvlo2yThvDr64TLWhDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=jR0J8ZoaBK804eGoX-DZeSBYoJTvr59BlCORiEl2FyPg_93MgwO_mC-zNx_S6yH9DuUjmNBy1A1WhK2yCarWSD8yF6_wjv0vzWtGegTKruuxJQ-RZdzak-FG_rNU8WQ9yxDVT7Q5Gc1J6B1h6IuFYEHSVp02RHce60WiDNurQhG7yggsRLFo8c9IrkXOwoaN8Bhh2s8lO2OY1rO1ahxAr7BZKHefe3jYDvvnuqmX7KnXBUSpCagEyUv8AnSqkU9fqOj3JS7U4PCoHqQCA_N5R0flNHMNoBKSirEFBAQhgid-MawoAxfK9iDgi8T0JNMRKsgzvlo2yThvDr64TLWhDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
حمایت رودری از فران تورس در جشن قهرمانی تیم ملی اسپانیا: "شاید بازیکنی که بارها و بارها، ناعادلانه ازش انتقاد شد، ولی امروز... امروز بخشی از تاریخ فوتبال اسپانیاست!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101472" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101471">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=snKoJQBrr05HLXLF7hTOWSjqLHasju7sFFfskNCVu-fAOcKZg5C8AoOMRFg5Nk2s2mNutxSmDtU_w35NLW6mfUUf6v39kJwoEs8oKkQ1ZoytMzkZY-7WVGHhVN98XQZQHsLit4CfAnvOfcfGgzkW-7cKN791OepFfQOmWZCwk1C89TIPoK69EVux5zD3I1We_pzXajlMAzcEWht0V3afokuPGEEiB9T-qc4vqLykU_F_nNWXl3aC1M_yZgjkMYoiWvFqQUqg7MZvD8v6uLYc7N5y5t2ooAKEAb7BL9JBbK0zm2PqV7toANqFOsWyykpma0rwEhWRWfj14ZexkyfudQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=snKoJQBrr05HLXLF7hTOWSjqLHasju7sFFfskNCVu-fAOcKZg5C8AoOMRFg5Nk2s2mNutxSmDtU_w35NLW6mfUUf6v39kJwoEs8oKkQ1ZoytMzkZY-7WVGHhVN98XQZQHsLit4CfAnvOfcfGgzkW-7cKN791OepFfQOmWZCwk1C89TIPoK69EVux5zD3I1We_pzXajlMAzcEWht0V3afokuPGEEiB9T-qc4vqLykU_F_nNWXl3aC1M_yZgjkMYoiWvFqQUqg7MZvD8v6uLYc7N5y5t2ooAKEAb7BL9JBbK0zm2PqV7toANqFOsWyykpma0rwEhWRWfj14ZexkyfudQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
امباپه و اکسپوزیتو در میامی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101471" target="_blank">📅 19:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101470">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thQGVdowj-npN-Ea2rqL8gf74wFYJoolDPcT62cG4K6iHCAPnwpJXqi0cYcRQttMOPHeWrX8Ws4HjWy3R0IqX_jJMLJ-Vn3SvEJjl5AXxZVOC2MTomkvr2lB7ajlJuq8tQz4RGGKxgZiqMeR8GChiWWvJgCGREYQy3AfaNy8-kIYDApFMlwGQ9FO6ypwEbHEZ7Lw4mAxThXkHVFs1YgCcOjGgdnDP1izDiPiMGTnPKo-rn_rEx2op0O517p06EujzlB0XEuMMvDT_GeQAOUS8jTS0JIslS_Zf7TNgYtHx0a-VH3bD4YHKqrfi-zl3qXQkVqSUSqF1K3XSHinqDv5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه حدود دو سال پیش با دختری به اسم فاطمه وارد رابطه شد، اما بعد از جدایی، فاطمه باردار شد. اولیسه اول پدر بودنش رو رد کرد، اما بعد از تست DNA مشخص شد بچه متعلق به اونه. با این حال، گفته میشه هنوز مسئولیت پدری رو نپذیرفته و فقط از طریق وکیلش پرداخت نفقه رو قبول کرده. فاطمه هم پیگیر حق و حقوق خودشه و این ماجرا باعث موجی از انتقادها علیه اولیسه شده؛ تا جایی که کامنت‌های صفحش رو بسته.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101470" target="_blank">📅 18:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101469">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=c0rGAnbKWW9M278W9uz6RwKUk0IjGJto1ORumO9SkIpf9H5nqxJXDKqrFvDUYNzraGUdvVFW82ZVuinhQqZAQRkFMLYGfRPkRxJ5OUwWCr_8avkzvjD9Azr_fls51c6QKMIt_8zy1lVMjfcRsHi2TOQDZzJ705WAsRVjknKG1FZbkNPdn8Hlx4MLo0gnBpKHaGxTU2exgBCe0QDeZFaUCWdpUaM24ca1uzSQMsy2fVu8NGBzT6-xhpXrz4Pa-FDXm2d6I75LMG_D1UJ2U-xAcfivEqJdvl6MQ2QBkQylfVboKW-fTSQarJq8dgv8EvIPTZUu2swT-mXWXJZg1kIv1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=c0rGAnbKWW9M278W9uz6RwKUk0IjGJto1ORumO9SkIpf9H5nqxJXDKqrFvDUYNzraGUdvVFW82ZVuinhQqZAQRkFMLYGfRPkRxJ5OUwWCr_8avkzvjD9Azr_fls51c6QKMIt_8zy1lVMjfcRsHi2TOQDZzJ705WAsRVjknKG1FZbkNPdn8Hlx4MLo0gnBpKHaGxTU2exgBCe0QDeZFaUCWdpUaM24ca1uzSQMsy2fVu8NGBzT6-xhpXrz4Pa-FDXm2d6I75LMG_D1UJ2U-xAcfivEqJdvl6MQ2QBkQylfVboKW-fTSQarJq8dgv8EvIPTZUu2swT-mXWXJZg1kIv1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه‌ریز دیشب رضا جاودانی و عادل فردوسی‌پور به محمدحسین میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101469" target="_blank">📅 18:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101468">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDA9kxxDqNXQddJouJoZpZez-wTLGBZr1Lh2Zp2BkPjscduYLcjRV-tbxv5FZHazBp87eQ2kXr_jq06M1Z195YvS0lzMGOC-a2Qbr2vd2atQ42AaHOqJhcvPpJ2lS_F39gjURpm-TeRnvXyl_kywYY1Xi3babqX94iHcqqTa3RxyBZBEV7Oid2tPtv17RKYQazpio9ikpZA5mwdRGm-SMqZ2xTHMJQxVuym8bf4mOomKQ_bkV_oImimT0O0p22XdRZHg8Vhkv_Kw6C7RWkExS9cgvJ2zwvcGRVd5-Tnn6qxZ23HXUgPj0wVRCMdojs6Teydafknl4MJ8pI_sFsqxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه روی جلد FIFA 2027
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101468" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101467">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUFaelTzyNFnHGEDADfq0Lc-69FxCuGt9NpUiJp6aJ5OfskWbAlTQI0Sjs5aOx_iXfillFRUSZZpGJZ45cIwXfrCc2z80OGZPOwNC-oTEOsvWUv_a19HSZ4fuQPmiSs-oDImX4UimD-JttJCvDa21v-rgK5yp-72OWFjBQ4XWjV4LjuOoNPd7HNPHlDlKHyCi70Jw3LGzvdzZhVY0ltxH-aZ1v7uewdEkbrMv3vYod0jTHXo8WeRC9dA3eSO_K2ZizSKiq8n7Ly__6IUYhnZFDXGbmNbiIrh3Jyoa67xh1R9miinOZjvWaHF_cl1nF2B6VSB6kjuWfrEvFM5fLPe6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتونی تیلور، داور انگلیسی بازنشستگی خود را از داوری اعلام کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101467" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101466">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0S5NaZ3UCGmKGLqAFCtBWtPw3AZSsx7vLIakLJdngeSwUnuIw5gIs9F6BBYtdrQcCiju1jJ3FaoTD1uDFNWIpHAgxuilHCNbrbSC3nrerAXJZmgUhq8g8-0maHyVdOWtaOSlcQ1FL1bKbO4S01afvBBsw6U6DKOiNMSABx1k-gakXI1uKSv-VgPxiNWIqNrnx82LyOMdQpdhCs6pcK6X6jOGpM71DHBWzCPpDe88lr3TkB5iXBF97drRFbLY3-0oPdKqkChdP1_OmuIYEn3FOnXMads4TeLM3gpv_6pdmCj4ElxaGCsOkHL5PpNzUlwD6bl126Yccb1PR75-3XjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ماتئو مورتو:
الهلال در شرف تکمیل قرارداد سامرویل است.
الهلال معتقد است که پیشنهاد بی نظیری ارائه کرده است و امیدوار است در ساعات آینده همه چیز را به پایان برساند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101466" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101465">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRVJF2LVrfdebth3LEI_qvipBpu3W6mbD8wXYgOjewEDD3uZuTNoKkibiREGEQkEcX7nwnWX7vMCXJnZnjmM4AyBHanlco1rfYjzUV5f2-9Z5Q6KPD7l75DWMC5zAS86JBl93pj1rSLsUER6-WipEhLsW3pIHvGzxmeFjziLfG-F2MMKLg2qY4YAbJ5FAlhoWn5_v2QiOfKTafWFfcERUS5RHkz_BUY_CHFAN7AFGZWRzGlkIVOMwLklsf8Cc4Esa9VyF7PdbNHsxSiQ7wRq4kpLZZn4kODgJVca3EeRjF0In1w8f5iAM9k7ueslsxQNlZZuvuqpoEzjT9io4oy7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
تیم‌قلعه‌نویی پس از درخشش در جام‌جهانی با دو رتبه سقوط در جایگاه ۲۲ جهان و دوم آسیا قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101465" target="_blank">📅 18:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101464">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21557090e.mp4?token=GkEEHz0cJtkKu0YK8N-wkUJY2vI-5vgCy1YObfGLLTkeL9DBNfl-BdF6W4yLtQ0nIl0MZF6bRPyzfbZGjYHuxDRns6oX7XqeADougXi-vg1YaiozKf2YUSUdJ_tPqd3sl65WWQ7wXMIoA-CDKzlzGoqnI7ER6jh2tH6PLgILxEm_o7ih6zSLLcmzdGcpVG3yMHBoXro23ugm-vsZy1Y1nAz2jmLbyaxVxToB9-ySl0l9l7BcN2RaPMHyCZXgAij1PynyDVGUmurGNWv8KuSjrPgzWLkyyvIXjuvZVC95qff3XM_HGJuF8E8Ibi2VqwBn5tsdCc_YtippKPSzTFvpWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21557090e.mp4?token=GkEEHz0cJtkKu0YK8N-wkUJY2vI-5vgCy1YObfGLLTkeL9DBNfl-BdF6W4yLtQ0nIl0MZF6bRPyzfbZGjYHuxDRns6oX7XqeADougXi-vg1YaiozKf2YUSUdJ_tPqd3sl65WWQ7wXMIoA-CDKzlzGoqnI7ER6jh2tH6PLgILxEm_o7ih6zSLLcmzdGcpVG3yMHBoXro23ugm-vsZy1Y1nAz2jmLbyaxVxToB9-ySl0l9l7BcN2RaPMHyCZXgAij1PynyDVGUmurGNWv8KuSjrPgzWLkyyvIXjuvZVC95qff3XM_HGJuF8E8Ibi2VqwBn5tsdCc_YtippKPSzTFvpWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم چه حرفایی علیه مسی و آرژانتین میگن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101464" target="_blank">📅 18:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101463">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">😢
تمامی سفرهای استاد اینفانتینو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101463" target="_blank">📅 17:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101462">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By6zZNziNObkljSxuYnkha5mRwPg8M-0A5seinx_WzuZKyTAgJjnLsutr9MIkW6Q2biAKrr-wXirK8sL84ppPbTx3abmpS4hqApQ6RqUr52gUvqeZv_oa0EyDX1GnyEme9v75q1gU3Uas2xQ3C_Nvfo6IRBEcN2n4fKCN76RGqm3qiIclmO8kbvoj5V1mfEQju-WqPwq4uzL_ANQSBGcQzgbxN00DBny881qpnR_DSKPtknpnFT7CyeU5G1cxkzWecSPyAs1MePUef-yAI_oPXziUAnNWNJzpRw9Puhm5x4I7vzgs7wlxBWwRcAOLE0uzcaSfnGw_qeKeSiaNFoQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: استون‌ویلا با ارائه پیشنهادی به چلسی خواستار جذب قرضی گارناچو با گزینه خرید در آینده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101462" target="_blank">📅 17:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101460">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QczTk_9Bnyv_bSEdlcSCg0Hst-WSS934m4jthhDAZSODshMg2HYfjYPVWB4oMH-CBzw7XadT5XzujgepRnkVNNnNHR0s-0dRx3WhDpvEaoxePvYeIQ9mlLmNMRCeWXvV27D4yUYHCaukNNwCxMVci369WaR6_zGSfyM4UEHxMh2zuGb5E0dECAcsToBr32DzGhjAvG-fAkhIAHjkwB5RTZz2ZgAYdxYTskkQ2AdiUsC-IUw2YgDjT8YiyvwZroZW5kh-0YaTz0-tHXPohb-Z-aRrX02SAttiItd4daIb4tTRIbyjAstEA18hyWnRf90gaYk_wX9bl-P5vaOtIlYyYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/acQooCzAbKzRXBvEC78krgpUUwXQrW12POSh4xtp3i_HYRxBn9CFwWV3UPok6LjN9TWlVlplam-1n3awWrymiyPyNnvNI8n2hPo4WhoA4qGcFCj4woMuCkPkKqfgHUZsjgbfB6lnlUexpa-UfPXS7uRTbyuTQ27pL_fhW7Sfc7EoZKOh0MCjigqRv5LC2qOcmStBobfAcfR_X-TQxdJAQeH5-6ZZNM3VWiEEPb1TD-N6cC2NptoqDUGd7WON3MXelPLSCbEvgDjtUBuIGJP1Ff43bpkbfGFS1cEayFwUD4Sr2EIm5gI3ScmzC4anfW42U6zpZB5VrqMH4L_qnHLf2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصور کن ۵ سال کنار یه نفر زندگی کردی و خاطره ساختی، برای آینده‌تون نقشه کشیدی. بعد یه فوتبالیست با ۵۰ میلیون فالوئر، شهرت جهانی و حساب بانکی چندصد میلیون دلاری وارد زندگیتون میشه. فقط دو هفته طول میکشه تا اسمت از روی صفحه چتش حذف بشه و جای تو رو یه نفر دیگه بگیره. چند ماه بعد، تو از پشت تلویزیون داری جام جهانی رو میبینی و اون، کنار همون ستاره، تو جام جهانی از کنار زمین لبخند میزنه. اونجاست که میفهمی پول واقعا همه چیزه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101460" target="_blank">📅 17:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101459">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=KfeOgkXsfe4eSdV_-VRmt0PNBDl3WDf4RmvJXzMFOCGM3hB9I35zTTu7tQ5cCqeAAYtmJrU4rtPbQ_5MD7WCFLuz2yZuLxZQoaZ3SRyFbyCqiSwBWSUBJ11I4c9l1gfR7gt27spizHC8NYEFBB4SUCL18dYYqyaCluzun_WJKEGDNahNY_QHbmmshxyE8HioJvrWvDMPOWkf8-k9LZwZRke6M7KZLPRfp0a1XzSKMleb0h_r-i3fK8AzR6222unlRvLdKYf6-FpFmSqAGyP49uqHx6Wr-1TUbMwsIRxq413CWA2PPtTbU3X05kPpn2i5P6yUXGocvVnqrT_jkOme1QE8L8zVBKmMlt2BWCmAzdv7FULkJN8aElucafjc0GTiRNg0BZ-xMo5s-PaSt6TyM2OvbTXY9c-BPEUIR0KmWJ9PXuqeWeWaBEEK5qyrc_aOdIWTQ9C2gnwPZnm4lA6YlYQgBOb5ZvwXHrYX33H5I277Pr855s8TgBYef1DT0whJ55DVTPZEWS5kYr0g8J7S1sVHX_0JKa05Vit3A60jgU4ikRD_dLbSNZyx_ljbBWe1rJw6Q-r4Lc2JTG0UAqp3M63aYFkLHFrjuYugHavH16pNQOEW7gH98Z2zN-Qifbl1JLPa7ReSuXr-A8BG1PVWwbBar19-3VBCrfHlZ1ebmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=KfeOgkXsfe4eSdV_-VRmt0PNBDl3WDf4RmvJXzMFOCGM3hB9I35zTTu7tQ5cCqeAAYtmJrU4rtPbQ_5MD7WCFLuz2yZuLxZQoaZ3SRyFbyCqiSwBWSUBJ11I4c9l1gfR7gt27spizHC8NYEFBB4SUCL18dYYqyaCluzun_WJKEGDNahNY_QHbmmshxyE8HioJvrWvDMPOWkf8-k9LZwZRke6M7KZLPRfp0a1XzSKMleb0h_r-i3fK8AzR6222unlRvLdKYf6-FpFmSqAGyP49uqHx6Wr-1TUbMwsIRxq413CWA2PPtTbU3X05kPpn2i5P6yUXGocvVnqrT_jkOme1QE8L8zVBKmMlt2BWCmAzdv7FULkJN8aElucafjc0GTiRNg0BZ-xMo5s-PaSt6TyM2OvbTXY9c-BPEUIR0KmWJ9PXuqeWeWaBEEK5qyrc_aOdIWTQ9C2gnwPZnm4lA6YlYQgBOb5ZvwXHrYX33H5I277Pr855s8TgBYef1DT0whJ55DVTPZEWS5kYr0g8J7S1sVHX_0JKa05Vit3A60jgU4ikRD_dLbSNZyx_ljbBWe1rJw6Q-r4Lc2JTG0UAqp3M63aYFkLHFrjuYugHavH16pNQOEW7gH98Z2zN-Qifbl1JLPa7ReSuXr-A8BG1PVWwbBar19-3VBCrfHlZ1ebmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
نیکبخت‌واحدی: ۵ ساله پارتی نرفتم و الان دیگه با وجود هزینه ها نمیصرفه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101459" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
