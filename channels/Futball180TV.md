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
<img src="https://cdn5.telesco.pe/file/UFXmewFz6qrOO05Si9vO9AO3mISN0q_I0dmegawcwKTzy9aAvSWmv5q3vjGfA_LLgIC2zWexCbKYs5FuPSTigErLQMe8oRqSulMXqJ_elp58EN-cPU5syjIh2zre6QfLWAwcBSQdyWHddcsOIGJcekg4YKT_LWaWSOGRW87HbuLJJLLUJIKft0Yq0n7uhl0UNIMhcvbvJt2YSYXXFzlWq7lzP_XcChLJfE6ZYz81Eq0la7TI2-0_OLH9r5QPtAoss23lJ2zKyA14MhqnxOD77R1zHi4wNROZ5ATH1Qw583JRGwYZz0-HnBxg5sShLqwg7JWNh_fUJLFyj20wh3jj5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 661K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 09:53:06</div>
<hr>

<div class="tg-post" id="msg-97592">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpAQRu7wIHdTlcIrL0EApDDu46WnBsp3y-dfghUxUdiZfGSqbjJhjhCjZMkvFbFT9EVHhmB1tBYZKV38pnVkKXklAtNNDaakI5l6Sg4FnTL2_x_1T49CRtgAfaoAYoMUdTw_CQasIOAbuxod7CKtjcg2O_BjZlz9HQdSWCpXCRHyPI58f4azwodLk-LbTmwMAuzGiG-wnUWE_sEttsrnVhP5zNwTd32lmcZxP_BJ0SrXWbOiXmiVZAaqWvMs5jXSfstBovKj08wjXdfGjL6LN3lcxJKm7O28EvXZ55PSetGYkOT67teBK-x2lFiJKaBgxOLpL9WADG-aw6Vv4sCz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
فلورنتینو پرز حسابی عاشق بازی مایکل اولیسه است و رئال مادرید هنوز هم دست از فکر کردن به جذبش برنداشته. توی باشگاه، خیلی‌ها اولیسه رو «خرید رؤیایی» می‌دونن. با این حال، فعلا بایرن مونیخ اصرار داره که نگهش داره و قراردادش رو تمدید کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/Futball180TV/97592" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97589">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQzQ8lK9rEs2lyQJmG3igN8gOuIV1hEpWu3p6ctQEv-gRnRFH3GRRDB1E_O7cxX6iELCpoyD5onLusaS7mxgPiq9eeUduA_Kg9Hd2gceQTb8n7qX1lBsNBQRj_VO1irrIBTmbzgyuoCqz15swxaQjwG7WKJoMSIH2JRmDUbYWg9o0ph03hfoUZFKqEw72DpcUJv9_BvbXGH6jlEVtzcdX9E3WInK0rP9FLJa2incD2_610e6S3OD_XwqNyj3MWdfY3nyr6nhAXjh2xl1T1moknzg-2nWK90hehaTpnC25OlOVfRvLE1h5nSqKao4VTyppP_X29nwbSEANyn5dTaXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRgkBVFYiBlm_tlYknGRMzJXdl8ws_OM9_HPHy0o3Hl273yVAL2S3MwSLpBGpPq5u2XvA2iKwofd6vo99wez8bOVMj8svCZgPgz0dsSo6zEFJ8_T6ljp7_UMlp07C7NzzNZ5yGhznkKf3LJ7fIJzQeR2rOkqjX7AUb6UIPJ0s-XMcUlxlwd2nulTfEAsxDeHqnNt5ieT6_Xiw_9sd3HPxhiq8vN5HEtGlXw1uIIgz5fB-WZIh6v9LviWJnRE6XCcRKv8FH-caLOA7pPBcG0X7wLusJdKa7Ec3MOZW7Rycoh3SvropVq7CuZCtKkf54ovs17LJyiXpaMtKTQced2WMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szjbpVELhqTUHgDyl9aQ_JEmqm3h1-VNG1RocZVyEQyL82ncYEuKQPYMuTmY0NuyDBsuCq-7tyeS8YNUoMkQcam1NMfC9bAgEqWeXdgRZYR69uwD6xxnYd5LFMXB-p6tRQLB8oolnZMej4yQV74yMsmItq3-DAUo2ERL2dIMYEcwoh8icD3UYux0Y1Lsu_V8DIbrHEvYYcoqdYknWp69nM_rlCrwNTyYVUjRuOsVsQgH8XUUy_klgDIXGnmYpg3IjQc1ZxCVnxnbxoaz31HGZBzX4q6DeMm5a6xJ9eet41voHRgC4_oPg_5zNZ_68IUgVGLpgUaoTgin_IrOvJxdKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تفریحات تابستونی خانم آلیشا لمن ستاره تیم‌ملی بانوان فوتبال سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/Futball180TV/97589" target="_blank">📅 09:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97588">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxuLmJhRY4HrSOEXGe6LMylK_7Vkgpy5SR-WDaoM5_P7HJ5R4wRg1TYzn9faKe2lxICq6zjN0rlhFdtb0CKRb4yNDIUtbrWlxXxhuTmURo7dMdkh78lhqCt6Iezkcubrnhptayr0dmv1tUzhnP5vTjta-wGpBBtHPI-_UhgOLQGpVQXL3BHNj3WcM_yWIkIib_0Ijv1s7PNEy1CYysc8pdenAs-CXCdkj4NB-4BbwX3rDEadHf3EbhaM1F4t5054xie0lqkXf1K8kDzGjljgQVPc6hMb7SMcETyGn1vvULMLqAn11m1ThVWqmOzpZzNsBmjjIZK7giweCRSx6dBjjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
چیزی که وینیسیوس از هالند میبینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/Futball180TV/97588" target="_blank">📅 09:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97587">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=H_8-Y-ZloMQ5RsVie3fLFKuWYdM8IC2ynOMP8Sl7ve3A29J3N_UkFOZPtHkT886y1V99LMheIeTXFl0E_L3Y4ff1w6crpATFlwAyG3brXsk7Qb0-iLPvGGpIFJcPyTZKWu8an8Ne3JXQn9LZiAizcXuvQbWX65F5xkP3-fAIkVGcxdoYVvBgApPT1QWxx1XvM9neW4noXqpu2nnnv5XcR5lBZ7BgEO3xvgCo3D6vYcjkaj2xh2bFBN8eAytJzr626K173rDrfb3GF7LnDSXLe08qJrzNatTVo7QULvANidVKgkNwIeCIBPGucVK5yURtcSLASZ41wPDHjDs8xXPFFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=H_8-Y-ZloMQ5RsVie3fLFKuWYdM8IC2ynOMP8Sl7ve3A29J3N_UkFOZPtHkT886y1V99LMheIeTXFl0E_L3Y4ff1w6crpATFlwAyG3brXsk7Qb0-iLPvGGpIFJcPyTZKWu8an8Ne3JXQn9LZiAizcXuvQbWX65F5xkP3-fAIkVGcxdoYVvBgApPT1QWxx1XvM9neW4noXqpu2nnnv5XcR5lBZ7BgEO3xvgCo3D6vYcjkaj2xh2bFBN8eAytJzr626K173rDrfb3GF7LnDSXLe08qJrzNatTVo7QULvANidVKgkNwIeCIBPGucVK5yURtcSLASZ41wPDHjDs8xXPFFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یادی‌کنیم از مصاحبه سمی سوشا مکانی با خبرنگار برنامه نود که فوق‌العاده وایرال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/Futball180TV/97587" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97582">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUoj_SadaY4JffP05KxIe_Z0j-fk3BagRTPcaAPbnX-40RarU75-taPuGVN5Jn1LEmav2jo0XzgtWJ6HC3SErPglghwwQWWF469jWTYQX8JVpx6XqHOusY4WU6hs9dKFVEL-bM2Xo3uUh5Ews16pXk5XZAg0KnHvJ0vaGWL-E6oY8lm9P9TN-SWJcJqoANlhcAUby4S4tn1YCLWZP1AirX0_GQ3Wzii6BuZSVVxCTTQ1KmxKweHbhztvBZ7_ANujhAiopC_f0GPkdVeszeiRxvjgkV2u-YrZN031wvSqMhQNcGnMjsyQ38RUGG3fQPwa_XCgRTTXYEJSQeDuBt6BKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZgIk-cRKqYIMRLc2so5s_3I4Dg3GAZZXBkk1dW7NMNkqEJD8IZdQbnzvIBPMvz_7wcIzFUAPqaPw2L7yCGTrI4jF9MMy9QY1YzRao5pWEqqNqiKHGkuvBOxIQysnQa3XAGHdmwV4tvZARHBoUEzxrZBqsw71DXqDKyEM3mCvvP415WK_uUr3NYoDonVazY5ZCJREwoK1sv6qjYHyzdy0BS4yK4PTpNpxPQ-3wCHQajlU1PZPokF0zDrFU0BGVrGhNR0hqII7OvsoW2W7ndlSqWsPHmyHZqGUzKNhCPrBnkSzh9I49nqkujcvK9vrUMh-K4hwL0D_BmK1M6ANTdDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leDA68D_HeosmhNIijSTPVztnbDiYPA4cvaNTahLZpQv2HGhaZjPuFP5T9EOViK1emgxAr8jkLJmri5KSmpNWJ75wwxkBke8fgSuQn2niWyl_DYl2Yu_Rv92qecGWIYZEJ1VjPWpWx57Du0TEBwU0OebE0dc2tC0rXlPn9FknDefnPaLEAUfypuuipwkz0ebNRv6BuzafGFdHMA3CMFTogQ_6JP8E1kT9ucK_9kax_Mk2-IEP3crh7-vqlHDSajuJ88JOlSLfcFkMNfn9P6wiVwTt9iAmKjDWnwAjXRRQrNqwC9Dg821zS-p4-78xeIxh33VPQudB6kOe71kvze4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rA_rQ8HqirnhnpgQlFebkfVjHcp8fqtUEJ_t5Ob1ngK6T3TfRWT2EvOuw1F1bgg13bS7pknXy0WltuKgtXo-hGQ4wTujZfA1Ndh71MsLdtdZjqJr054GbiWtqc3TxfjGgg_W3LWwIu-yREyHYR4TydZeVAouetzk74V36kJea3YwG_a9ZqFFejNWI8KXiiFyP6XC7t8naxn3tyksWiKbjRv5b8bUwVTV1OnBEBw3bslNXZAEIMc7LOWMtqfzLJZ6ONWbeLjMXAzCVnXrnCD6uxYaL8uyec33StAchMU_voU4aSs9OBxtqFSk3KLyPLvnJ8erQHh7iM_4gwIE3xZToA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfeNECkkUSduoJjdQh_JbKEHqNAl0wSeHXlE_3wDIfnw158Ex7vTY7oSW0GWDHZpYTJ2K6aK27pVrvH-xTdgCp8kDaoN8amIhXPHGiTxhuv3S7IMJqqL0OlLDoTojV2ICXr8TpK0MMzTMblg4jmewCpUErB-JpKwUhfHPPjctg1lLajy5Ft8h-JykRJV1mOAratZbFSdhqlxs9GuIHCjYWPw5PzvSqzGGPiutXDkXYH65llHFMudPAeo05EwYn9o6I7WVNmV8_L056Or-fD-hTgYHVmC8kM4iAFLvMKoVpQROtECVyIhItxMj502AyENQF3KStVIf-zLNAxTgmC_rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیت‌ بازیکنای انگلیس با زیدیاشون بعد از حذف دکتر کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/Futball180TV/97582" target="_blank">📅 08:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97581">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=e4qb_ZZP7VsV0SlpvM0ex4MvryOVuWy0funwKmtS8scS3H6pCatfPQlAmMIU8PXzY5aKUtg603nPqqqgccUFmXd_RuRcp6Y-TomDN2999PhN9uDIuj2WjBLMtoqyDxSxsu5GhjtdFK97N-3OodKpdOaf9FRWyeSnqnebymR1sBRQtVYm4XG2djH0hUGQJfnAY7RRPIf1n-KTP6CuILZJbHAUzSv-NHhfdZV-QI22IVIR8h3dvW5NZ6ik2rjtd6n40YvEmIXwg5exKpY0WDQYIZ-ohuck63_PBFTfLgoUeZbSsO4EmPd7-kqm1vke1TfncLGIhG-4AeaVgdpdrPfBqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=e4qb_ZZP7VsV0SlpvM0ex4MvryOVuWy0funwKmtS8scS3H6pCatfPQlAmMIU8PXzY5aKUtg603nPqqqgccUFmXd_RuRcp6Y-TomDN2999PhN9uDIuj2WjBLMtoqyDxSxsu5GhjtdFK97N-3OodKpdOaf9FRWyeSnqnebymR1sBRQtVYm4XG2djH0hUGQJfnAY7RRPIf1n-KTP6CuILZJbHAUzSv-NHhfdZV-QI22IVIR8h3dvW5NZ6ik2rjtd6n40YvEmIXwg5exKpY0WDQYIZ-ohuck63_PBFTfLgoUeZbSsO4EmPd7-kqm1vke1TfncLGIhG-4AeaVgdpdrPfBqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
نعیمه نظام‌دوست: روی عابدزاده کراش داشتم.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/97581" target="_blank">📅 08:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97580">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4lv7Jqpi101Go83wvWeV-uYTH69_cSOc4ZNHblLuqx6rlT6bZAEttavtmqn_kcE0TnS8eM6kGg-HKm0fTZtQ1wTGWIaZRrG-7TTiECmpChjAt8_Mfr9Lsk1vJmn_WP5hwnsG2OsZtoK_p1_-TO-ESjv2agAMNzahyqvSdF59NS-sXn3HqxDXhPNUZ90me16tfYrwEes1QaQ-UhzIKAgZi60ogHfKBIUbrPnKDOwVUhPD4TOfxGkKd981Op-aXZRCxGXsXI2QHTt-FSrnriiKpDMotAjFxXV-Sv1Rp_3XplWD_yKhFOLzE1UEIzLG9iybi6t4uIwLPwtqDT7wu-idA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
ادینسون کاوانی 39 ساله پس از 3 سال حضور تو بوکاجونیورز به صورت توافقی از این تیم جدا شد.
🔺
کاوانی از اون مدل مهاجم‌هایی که وقتی توی زمین بود، حتی اگه گل هم نمی‌زد، جوری برای توپ می‌جنگید که انگار آخرین بازی زندگیشه. از اونایی که دیگه نسلشون داره منقرض می‌شه؛ با تعصب، جنگنده و تموم‌کننده حرفه‌ای
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/97580" target="_blank">📅 07:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97579">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=Htb5Z5WAEzJ-czR07Q4DKSjWQ4OI6Gf_V5umWiZnh-rvGfJYI-MSqbP4P17DzY_BEfDfTNHKdStmhoDgp6xoP5rHS4av_sRmHqTTArmkiZy9bK2CvoN7cpR_mXGgSx3ZM42JoIW2aPoxUb4VCAB5c5nhSKYxKnhUDXKqHruKYBSovEe1agahAruvt-s4yy6lDRPY0-1o2mZalZKn7EcIm-Zjx_JIFkG2LIrR3TZOCs5Gfa9yZ5eogGV5m1sWquVGfO0xmtJYrpaOnWxt9jrPPN8T62Pd0HrLn2SVaSA1-8O2e73nxM1dXdHj36lhwtyndGPqYgWWUl3XLorEuFg8CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=Htb5Z5WAEzJ-czR07Q4DKSjWQ4OI6Gf_V5umWiZnh-rvGfJYI-MSqbP4P17DzY_BEfDfTNHKdStmhoDgp6xoP5rHS4av_sRmHqTTArmkiZy9bK2CvoN7cpR_mXGgSx3ZM42JoIW2aPoxUb4VCAB5c5nhSKYxKnhUDXKqHruKYBSovEe1agahAruvt-s4yy6lDRPY0-1o2mZalZKn7EcIm-Zjx_JIFkG2LIrR3TZOCs5Gfa9yZ5eogGV5m1sWquVGfO0xmtJYrpaOnWxt9jrPPN8T62Pd0HrLn2SVaSA1-8O2e73nxM1dXdHj36lhwtyndGPqYgWWUl3XLorEuFg8CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط فقط بدل رامین رضاییان رو کم داشتیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/97579" target="_blank">📅 07:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97578">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=V6OpHXiSOb6wnYCCI7J9sCHjRSfVOcI1fC3P7zaws6E-vemrhNt97GZyL1pqjpwEcw2tRzj3WDPHZ-56Uy3AJM7yNcZ8Ndxn-t8pImimpKvn_TfDPr6uHsYOqCh9VdBnNc8NeWkW1MIWX2nBr5_YJARQnCQFTFhghCZn6NtCblUopEkBigJH7ji9n8Jq-kmkRiiHYtzK2CgwTDytuEKYTueyfqd8TgHGhCOM3RIDE4FemmZPvbYmWPSEOasJLInYSNsSBRP-fb1vAslsGB_z-gxcHhCnj8-0mWuSv_a6_FTlQWTBjjwmPLtjmBf1sTemMv6mmHAWo88PesVPU_OSqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=V6OpHXiSOb6wnYCCI7J9sCHjRSfVOcI1fC3P7zaws6E-vemrhNt97GZyL1pqjpwEcw2tRzj3WDPHZ-56Uy3AJM7yNcZ8Ndxn-t8pImimpKvn_TfDPr6uHsYOqCh9VdBnNc8NeWkW1MIWX2nBr5_YJARQnCQFTFhghCZn6NtCblUopEkBigJH7ji9n8Jq-kmkRiiHYtzK2CgwTDytuEKYTueyfqd8TgHGhCOM3RIDE4FemmZPvbYmWPSEOasJLInYSNsSBRP-fb1vAslsGB_z-gxcHhCnj8-0mWuSv_a6_FTlQWTBjjwmPLtjmBf1sTemMv6mmHAWo88PesVPU_OSqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی میفهمی بعد این بازی باید اشک‌های رونالدو یا مودریچ رو برای خداحافظی از بازی‌های ملی ببینی
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/97578" target="_blank">📅 06:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97577">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXP6q_kRdAteJXTJnmurhj90GFm0WqLZHRjBmbceW1ZqmNu3YVywtUCjTFUkxw_H317kP7Ae70aYg9V-HVetF15WK1aQSEVjdjgD89a1SHeGp-uVK60WANM5N7DEhdf7ZZ-WrEuD00J7jxCpcTOJtS26PWa2aEF3DZBUugnN20T925nDFnnTS8wST5IL5jef2xFa-kbDoo-rINf4TXvLaUgmcc37wc-dV6xTXY3MnZqL6ReULxgQBjEZkqzXAqSN-1M8Sl0nmDbwt9qZZy5aqAwF_PeAxTxt838HFrjRrrErGpH7sLDuOfGg0c_RnTtGwcAZIsClJVS4dwyWQRDUZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🌎
تنها ۴ بازیکن در تاریخ جام جهانی در مراحل حذفی هم گل زده‌اند و هم در همان بازی اخراج شده‌اند:
🇺🇸
بالوگان (۲۰۲۶)
🇫🇷
زین‌الدین زیدان (۲۰۰۶)
🇧🇷
رونالدینیو (۲۰۰۲)
🇧🇷
گارینشا (۱۹۶۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/97577" target="_blank">📅 06:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97575">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohf4iTyU9ojotMlFzPiYIVsl7Ssr4yKPyha07eYJL20e0WVS7HEy0uqvoM4ee7Aia0ddlBmwUjtvUC9CXIQLUIuNiFMw42X2n0K9IjT1-uJXh8__n20cOc-2ZMRDfRe_ufK-MOBPsfJwfIBFblvkmXt19fNQ8DnSpgZjo4qB5Tx__F_O0rGpNS-BQGRcMOLkTBuqciySnYBUA0-iz1psCX7_7hsG1zt6EfeYpXck-0uhWIHIiAARQN06tK9ePuHoOkgEwG0Tusu_2PnOzah1mDa0ycgTrkwJY6JhyzHv-BmPSfA_HJri_FGgPIqQXe8tjkJ_mMuOpOMROrMFxLzBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdmN-FiYLmcI0pdrsHlnV9MBi6gRI0TwAO97H2M70k8gx-bnpHZCroRkMr8PacQnmVVz3PwtRNgC0O3kju60PtW6FPwxw8096rHBRzYHxIKaPZiGKSYOeOPqMhpuI4vVaQ6UAeD6DTe1D4M5MRdlpdIWzFiNel5ZCmDsc7Exi3MsG-HWqFWV41WNfmtW_hdLfeHMaP15RKc25N3szsCuSm0tEzL_P8FMFtHnfGOrQeuDk6OExt-o90WglTAkN8cPL9JMdPqJ5vQ2ef5w2eAFTLkanel366y_d9Hn-zym-ZwtyA8alj3Zo3u1pDPPVgzxMO8uaay7Qir5iUHCKBLbSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔺
پاپه گی در اینستاگرام:
🟢
بعداً درباره دلایل حذف صحبت خواهم کرد. اما امروز اعلام می‌کنم تا زمانی که این کادر فنی در سنگال باشد دیگر در تیم ملی بازی نمیکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97575" target="_blank">📅 06:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97574">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kur5vj6BPftoSKdefLoNq0lS-0pQzkHQMgscoB_pUK9-PWx4qDXZ2wP2VRHzx5Mzbu9cDVrptXHfEDxQs_n5dP1YA_9wkj2JvePhn_aQGZAb8P-FDN420bhRdJaB6ENUn_8s9_fOkV6vmdBPUhPlMLamifNziI3ERBtDfGkeEUfLOpTgIl2aU26rjjpa_wl3Szh7ZK0Eu3urnfpxKyDl7dviF7-wcWxnXAFa-wlPOxV4d7dWNwRYnH5wgJJVN9jJqFfN0V7VJbI1lQVX8M9QPdaUXZ6wE4MevJYhuCmKEZItnuS0WWDOQoqTRX-_hNjUyD8B2O-6Quiv8A2sSOKj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97574" target="_blank">📅 05:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97573">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqiNFChl7eQgmSc4W68m-cmUk1b-nieKW0_MFeHOdXFsBpH3EvGTJ7TUkPmQRpOdLAKrlkMRyi575IHrRZAwVbpoo0WoKo86v1rfaMGMn-k-gXy7FXe-VVfDACP9zcedVxDF0YPE2VpydBk6eOnhMq-6PImY34RatE7ewTn_XH3oopSVhH_j_W_yfeDf-bfGvI52vmAQxwFWEQdCUM46dkcwiY2H1hhsXWjDaV8ekF9HxkFEoyuF7M-uMSUKEgQAronUAm-VWFhDyhgrz2_IkxCsLkOeFyE6zPdeQd9Cai0ddi460DnyOKSNsG6EMNO0wKjvm8Syx3ePg-Ndmv-Oyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇧🇪
بلژیک
🆚
آمریکا
🇺🇸
🗓
سه‌شنبه 16 تیر ساعت 03:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/97573" target="_blank">📅 05:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97572">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhP9lU6Uo_ALZwp7j6QbTjJcjfOHZNRFmYBusiibCRVo6ZBulZ5eiTRqk2V02wUN_YwNOhrt8xeaO1w2BnSDvfvl4c-1lOUStsbVJCt0JoiS-r3uuvvC5JjMO_FxmlA0pmrvGKJVdqmx5SFiNnjGSAxbvs7hGxMTytA0PKQ_71hVWy-pmEVTeHFYh5gRz36E0STtmvDSOxfYJS_ekaM8DvuUzE_r4yIjVt3v5GApJoFA9Sy22uVMKzlp_TPbZq2t1WeQt7lf1NCq4NDM1r4hsoqAnRd_Gj2cnYxvqr-NEK989ZJ1WRaKDJ_Opf4lk2WuBsrB8FO7W5krjZmrAJP4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | پوچ بدون بالوگان در یک‌هشتم به بلژیک رسید؛ ژکو و یارانش به خانه برگشتند.
🇺🇸
آمریکا 2 -
🇧🇦
بوسنی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/97572" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97571">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMiDm_OgeJziEEeE4cYUSfDjrYk-SetCyrOSWKLSGPxKWsZZ_skjx22RvPJlMjk8DdQp4UYVn_KY2puv3XOfyQ6D7vqqSLlDM9gIb6ouiKh8yytrOSSufSub8Fd2lauxOYlK6CsNEyb_SFPr4QVHjrYRdNVVvAxpOW5NKQzcwMTRXoPZb2Pkti1__ybtw3XU0UsXfvv_d98nQ7Xd5aFWrtAu_kuhN1kBtmzJJzrP_WF7SzKr_gZQimE7JgcCrpSIeryGTl3JlUzNiCdbG501-9wDqDuP7KOEavnejGDugLIA5G3E-iUfuCNuTgiNY1jQwauu34fONa6fKa6-sf9edA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ آمریکا راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97571" target="_blank">📅 05:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97570">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ده دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/97570" target="_blank">📅 05:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97569">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=JWzeW2AJ6t12Dz8-JehdYBfyKfpWM2YQIHwKKKzyMy-BERs-5G-ZOcyGt0AStqXYlaEIjQQ9PFHt9Cyp3dJxzZPGuF2GHjUAFew1QNvtzb-VI911KbSLn5BQAWSAzRr-tm5W61P6n20S77G42JIoSbUtxAlmRi6dry3_i9ZvXY1xh8eD7aDd28deYXV4dfn8DaUHc8H3J3fVQHJ0XrWkquwAxvXQv5P8_4xJkwknIfhT4hZGs_zMGLoMWhNiSuc4vzl9UcRQsKyjlCsUzB9o9mEqmEl0ha8tU1KqFpLtWoO7sx0gFwDbbY84ChP3al4EWogxvZYr4Q76hcz6CTWcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=JWzeW2AJ6t12Dz8-JehdYBfyKfpWM2YQIHwKKKzyMy-BERs-5G-ZOcyGt0AStqXYlaEIjQQ9PFHt9Cyp3dJxzZPGuF2GHjUAFew1QNvtzb-VI911KbSLn5BQAWSAzRr-tm5W61P6n20S77G42JIoSbUtxAlmRi6dry3_i9ZvXY1xh8eD7aDd28deYXV4dfn8DaUHc8H3J3fVQHJ0XrWkquwAxvXQv5P8_4xJkwknIfhT4hZGs_zMGLoMWhNiSuc4vzl9UcRQsKyjlCsUzB9o9mEqmEl0ha8tU1KqFpLtWoO7sx0gFwDbbY84ChP3al4EWogxvZYr4Q76hcz6CTWcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل دوم آمریکا به بوسنی توسط تیلمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/97569" target="_blank">📅 05:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97568">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">عجب تیمی ساخته پوچ
🔥
🔥</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/97568" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97567">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ده نفره زدن</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97567" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97566">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دومی آمریکااااااا</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97566" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97565">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گلللللللللللللللللللل</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97565" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97564">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4zHfmNKLRgOLRnwKggD3VYC3BXje_mZawTffn08R2AYPPmQjMtjyzTAoibzYvIZQa-ADkvTHs2Qx18WX3j_l5wVlen8NSV3yMnRu3nGYcRIpVKjkii6A-dnOt0U7zwFVYsmfTPSehR2dyJPE7s1Ski37EaipQpppc8YfHtOEIAWFdVGyK5epIvpNegj0asxFSYNyV0_MsEevsHAb6NUDw_b3usXmF1ET7dgZt_YV3KltQEh2Ijm0_MQAIauygpuGNuCq0LkCDL8dyTaUR_sVm4r5483FqTBAlSCwSzi3D9mFBG-TSCGvwWYkAcKy3YhmpHpIAo_ILncTPNizccthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97564" target="_blank">📅 05:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97563">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دومییی آمریکا که رد شد
❌</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97563" target="_blank">📅 05:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97562">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6OdY9lA6JzyMsXaILGGrxWLkM2QWFIsF9FIwZg5AxdLrNrRi2yAEP7wl1UMTNAK5Pqk4bFr3IUyX7PA7SBPBoAGSo4PI53dIJLf4ZqkEHT0aIDl6okFttpT9ZFLp8k4QvUhcUiJYV3IQBMhL28ZinZY1QtM5hMl77F9Mr15PMXSuCPm6jaP2emtRArMU89fO-wITEgCWt6Am5urv-pJFp57GW6kMpqhmN_3cqc_bDhXkLHUxO_H36VxiOzbYM7DQQl3MvGtMSIc0qzy0V-4jyjkHM1kbzg9HHXflwyd_ch2GI36Ncn8IxiFqBSKqmou0vnGJmqdqiEoOMCpsY5Duw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/97562" target="_blank">📅 05:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97561">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/97561" target="_blank">📅 05:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97560">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دقیقه 62</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97560" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97559">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اوه اوه رفت کارت قرمز برای بازیکن آمریکا چک بشه</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97559" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97556">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQ4NzZ8zQmTgIx3wpYaySfp7FUF28bvoDYZlNYtuy6dJ1kKSBEQExl9Sh1nPZiJC-OcB49BpdtmSKZ5lCbjppbWKlC_f43li4HDyCFmlzVfysKL96pGxkogi37E4RPOzQR0ftUSMnFjI4_MRV7NCvuWfhDxjKj3gJFz5sWn3iaMCgQb-z8Trx1IHn2UI3BtGSLbNDG5T8Op0G9mDQcsNQs2BWk8_9HWf00C26KdkGsfCh8UrgWDBFyVleuUxafFjE91q7LoDvctzFFNaeo70FQ40vkGOoDhza30rKTSzFbzjabfJVxketr1J1TWCpO4eQVM81l5FB5DP-skI1aue_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bm0biyx8TG4jVYnunv6vGrJTgdoQtATJHnNr43Ec-Cp726O7mIet6WZouwTAfr-7puqGHNxOn7elbLuh6fUlfOeFcRc8Vubc0IqKvjH6IddOstHxw8PSozjECccA7fqubMgYNAxcSd5I9j72HPKbG-H-Kp5Dd2ZsIiVipthI2atihrLnlX9xg5slsgE5fKW3ibvBgj2sIxOb0HjK3ZZJb8M3qXWyX5BEx1kfQn1RQWiE24zk2rg0XhuWt41D8RCziCz1I0DHZd0hM9aAgBLsO_1Hktnl9NVxnfgW2L3IBOwfPF79yFC88mLeECj72X8pfWMwfOkxYRuRl1N8Ktx9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaDyBLvndWTOKAmnHbxLFuVAF6Ad6fWGzeP1dDfp3YqRFOgu9q6s1fddBeQJjuz--Uq07kwpfEn89FAk2qculob1oZNtzFukOdcrgeEzQbSUV8Ii_fnDVToGhnOYWDUFEV1Wj3dk142s9q3tNhZJr5zyzZt80zTm5DKMkxlhOpsdBysQBXEhWMYuGEPGLaQRoPGJT_qlt_zyusbt7scTmUGr2EoOnxQG8NP_0Q7kLmLhqiKD7Kbz76dhYLQ9OBoWwno_ukHHTLGU5Zt-qNU3bh5gHubaQq2fq_qWWWBBCJ3iM1WqEjfs-F-qApoocBlewNh_pgOlsmkPU2Ajy0pZmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
بانو میروسلاوا مونته‌مایور مجری شبکه TNT اسپورت جام جهانی هستن
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/97556" target="_blank">📅 04:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97555">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_OmyihyEFJPV3aWOUAJ52o0ttcvUsd2zXSXAhe94uoQRmakufLf4G6ZMJDb61n9hEMtBnXzi8KoZoQRoP8bfGcZ_RwtzT4FbAUyZMxbmFDJLiRQ8qMg__pA5z809G7iy3M8cnxPJhiT-3v9icsmnHrAtAXK6g-UDd8Ky9aoCzjTXxpvlQyPSKD7YH8-SL8Stc0y_EBcmKJoP-2aWsp21pklbfIo8va3OZfLYTfjAHGTb4pfkCpem6DqHUguuYQRP_iph82RujcrqUQI66eRdea4nd46Bq-KcNLksuYEWOqvlWeCH4VqqYg3VsHBXvhiVmZvkUdoi-wo-wWMzahkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تاریخچه دیدارهای تیم‌های اروپایی مقابل آفریقایی در مراحل حذفی جام جهانی:
🗺
اروپا: ۱۴ پیروزی
🤝
دو تساوی (که نتیجه در ضربات پنالتی مشخص شد).
🌍
آفریقا: 4 پیروزی که دو تای آن در ضربات پنالتی بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/97555" target="_blank">📅 04:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97554">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN5H_L4yvCtEkr90HDODyrdS77qeomgp95lCKyok2i80fM7ZEcI4iWXAR8mAPaOS7oQeKrxAwSdzKEgoaPplSXLbIgL03DJqPxbHMXdHhJrmxdur3hyieQngvIKhlG8Jsd8L5rqnz0t9LrQicXxh0ileVCHFv0AvQM6FNFdxJdu02_7X0AG240JVav3NAN2BGEM2Sg6Cp3AyF8H0TNvIoIsVTaHH22vvwBqAFmFECdOTH4LIosyaCBxOgjS0u188SPxJEAHlZYosFBPcPfBg_RX9BZAUXTYYXksIkgG_PDIP0Gc5XT7x89e2MxVyCbrZkzAX93gwGZ82T6u50GzfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخ داد پرز بخرش
😛
🎙
ویتینیا : لوکا مودریچ برای من یه الگوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/97554" target="_blank">📅 04:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97553">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=UKA32oZiwdKPnGsLEQROfQ_e0kpnsXkMZ48D_KfD0JW9t_VV9xiD6dRRQT38sC4bOWhzsGAJuVVor_A5wbkxrYjqpi1kQpEh5bfqjY_VtzTzBp1gcmSu5c5bluK1p-4KRtALJi3vdijEcDsVZ0OTr3q0fI_TVqZzCs4Gi0_lphqXDCXelEuGsSUn31e6ivlBqdh-3fEUeG0DhNx7znMri-CnyGYFWMJkS_22XteNSNBqt533w2GjqfJ0MUQx4mruxu5U4GZ_DbpJ3rOzMn_p-DKg_3IekCnOQt6i4eRE1VQAINIXioeKlbeHA0pjnzTLJquNJU_998FwO_Yl6cFwdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=UKA32oZiwdKPnGsLEQROfQ_e0kpnsXkMZ48D_KfD0JW9t_VV9xiD6dRRQT38sC4bOWhzsGAJuVVor_A5wbkxrYjqpi1kQpEh5bfqjY_VtzTzBp1gcmSu5c5bluK1p-4KRtALJi3vdijEcDsVZ0OTr3q0fI_TVqZzCs4Gi0_lphqXDCXelEuGsSUn31e6ivlBqdh-3fEUeG0DhNx7znMri-CnyGYFWMJkS_22XteNSNBqt533w2GjqfJ0MUQx4mruxu5U4GZ_DbpJ3rOzMn_p-DKg_3IekCnOQt6i4eRE1VQAINIXioeKlbeHA0pjnzTLJquNJU_998FwO_Yl6cFwdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللللل اول آمریکا به بوسنی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/97553" target="_blank">📅 04:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97551">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMz9BT4M1RM1RjoTWrpe9sE1P4FNMM1MvT9eZrGpR6hp6igGjnAe44PrcKpxuU08_ouYuBWM6Zw6aNhLk6DQHex3ogEa31XTiln9GYS4QCOpRZdS_beDlEDNZoC9IZCP4-tSejqmHZx2fbj6GR0TmiT5L2z341c1fm7eRunoGSi6q_-XA_tbHXa2Y4rJ3y-OBWrodhJGCYSnrj8D6Q0_V-fe-jVUX7esCsfTs2CCa5FQN9BDCyQFCwz3sX4sb-YOGD0vptg2-fhkqrAnOAYoc_lj4HCPOK9GU7qnZL0pHmmEm1p2llIhk3MlwrhAvtfOPrccz8PuCIbbTBB8J2FZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇸🇳
| تیم ملی سنگال اولین تیم در تاریخ شد که پس از پیش افتادن با دو گل در دقیقه ۸۵، از مراحل حذفی جام جهانی حذف می‌شود.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97551" target="_blank">📅 02:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97550">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yjq-TPgkiR4pjxedA-tgXN-clenkML-QqgcltawjP-5YX2tFJAVd2w9x7-qr91-SvCcuyxJfiOW-XD6Pgr0ePxoaiPf7FIN2TMpn9Bq_pz_rxdEOwhQCm8PKmrFWN46cHflsF6kn7ykShP_nGfOwlOFJyNnfmvgZYA-VDo8FvZcFBc_syLjQSVcNi8DrJ9N_ZGPs_j9ue-H3yLzpISWt0TH_GlN0VUNI0bT2b591wped5OW_4T2TdZ5zMpmtAWogrGpaJZprk6Ij2FekdMIAQjZ8R99aYSKmX0pEaHkiToQrc_E6LG8ogsp-VbNeJBaZamiXL1xFXEyVRLLKKlcrBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
بلژیک در ۱۷ بازی آخر خود در تمامی رقابت‌ها شکست نخورده است:
11 پیروزی
✅
6 تساوی
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97550" target="_blank">📅 02:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97549">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNE_4keijOAGWcnq7nZ8ZQBiHpPtsq9TDQqE0oXWVgETrySkDqiF6-qw_TYDWZnZgFTDZ8I_XtNHGKirybG0JdtzJx4YGXmR5ZgA6h3kwZtrsM1LtAWpwcd9lxCozm2CZjdjoah366LCd2v1yMrKQCOcqvsAH4OIcskugzCprt5wdXyNnjpmT9SirWPjW6aErBdPpPE7Hrn63SR1_I_6e2HioXC3kLpInppR2PB0F3nMH50ITJzx67ETytmuIGBd0DQ4oedfz9mmyltobTt4AlKWlblz0TZr1ahzYy871-aujZGclyDb7SRPAt1233aLXoPTNJm0VMt2Yk-Zw2HNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⁉️
🔥
🏆
بهترین بازی جام‌جهانی تاکنون
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97549" target="_blank">📅 02:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97548">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzhj44-GI3cNanrxffLW8rudmAXd7PSB7MnOQ3li0A06nvfPIhOxLAyczgp3bltkClkD4NSdZ6PvAHJUBXkqivxYYDi7Yylw10XNSKjMFTIr1A3cjnaunXq4PTy98uavHiRZIoOq2JH5sedyzzfF9yxnGiy6Dvqc4Vk93EknkcF-BIFJkmzDc4dVV5lKT5aDgELNUglFpDGPq_pufSKyFJ8ZjQOgr-nqG6vOsXrSa14YJsR4TDIN8taoAX5VT2YICN-JMxuErVO0M53XwQ90WzcRpUnroC2_FgO2dtm8cfqtrIPUxCnvTlucHgCrqGZMTYsOhB1CpMylHzfVr0fc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇧🇪
| بلژیک برای نهمین بار در تاریخ به مرحله یک‌هشتم نهایی جام جهانی صعود کرد:
‏— دوره ۲۰۲۶
‏— دوره ۲۰۱۸
‏— دوره ۲۰۱۴
‏— دوره ۲۰۰۲
‏— دوره ۱۹۹۴
‏— دوره ۱۹۹۰
‏— دوره ۱۹۸۶
‏— دوره ۱۹۳۸
‏— دوره ۱۹۳۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97548" target="_blank">📅 02:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97547">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB6H3spm_zBKrP9F0Svlq5dCSidDfZwTv7JkrOo5wrWrXe_3YCdBvYn8-NDK8mxm89-KDepD_77iN1nnF8gdjK_dKiR37rWI8qyQFEbbK8mwtpjH0wiUxcLZo0AyzmPyGnNxUN8WraPW1idLzhyObdlJOVk22EC7qVqHrZnN6-VI3Tjtm_C1H9X97xxBEU4Udox9NwBmwbZz2_pkX81E-wLusqLcAN33CMbU33NsYZKXBuy3PTvUJd5dOWHtbjKj4d8wO2G7g6JVc5Riq1zeOqzbNtWUf2HYUd7Kyuerv5M2CaMvEX4cQrZVAKK0_FOtQsjSez9STx6rAuaGxI_FHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
| سنگال چهارمین تیم آفریقایی است که از مرحله یک‌شانزدهم جام جهانی ۲۰۲۶ حذف می‌شود.
‏ــــ سنگال
🇸🇳
❌
‏ــــ ساحل عاج
🇨🇮
❌
‏ــــ کنگو دموکراتیک
🇨🇩
❌
‏ــــ آفریقای جنوبی
🇿🇦
❌
‏• تنها تیمی که صعود کرده، مراکش است!
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97547" target="_blank">📅 02:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97546">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxNY3Twov77PGwGjFtc967LNGJuYDuexAP2sc46ft13SHF1oqyKTDbXyfrhXYOTh43WGOjqY2ga45usWKEAHqA1c_gH0HaREFQAjtYbvuyE8TC3YUrleHDo9evmX0bVNvX6TdiRrvQnlZ1-R_mVYUkAqyVVRP7sVv4TcW-pAIemoctUSIq7zOZ5wZJBduN6YAfct9H2u-P7LqTmGNb4b7Aet0kbh_AZB8qTW6sPuSKIWE6Cl3NsNJ22zH_C3O55E8ifTov3zccp8_p0cTOXY2lTD1o3khROyVSh6aym7mMa6eknKVi_jm6_N2lD95LM634iP2oKiXud7ewukmJD2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تیم از بین آمریکا و بلژیک تو یک‌چهارم بازی میکنه. بعد هلند و ژاپن باید حذف شن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97546" target="_blank">📅 02:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97545">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_pOuWUO9KOs1bJVgaT7nBBhR3Vm0ieJMPrhF8N8zAWY4BOIuJ-5JDb1z0SenB8CBVUqveSSqWOBp0DYfpvVKKMR7Mh_nTM58MfAsXL_SNPaB-BL4-j2UCaugi8vXC0-stj-YGAPt_gL6RIuN9nbSQcacqd3pK7BgrAj-tI9sO0T68y_sY37zZXYhw2VTYI29XQvH3EjtPqrckO8QDVElCf7WJLDuDpUv1YPd1sTePZS2eL4sc9D1bxjL7jz_vlPi8ystHzWdJz2BNrTkDFcAGAR4qc8c57ZsosqzcqbZRIW0jCXSDCcDScwvsjcuNetgXKdEDydFKkVB7Xqm6_wYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/97545" target="_blank">📅 02:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97544">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtmwdztcF88VQOvzNn4Z7eixaKJlFTep9mmJbmvydgH_o849x6nZoGqwkv6eBMktc-AZ4iK2tA1u2gUXT5TJ5D00aUBim3c_NAGgpixVlzZEqxRWgNkNwfJxPDtJTmLwlycfldCOSrefMVoGJXTtzZcfr1rwB6yR2CvroBCtAxomdFVANtixz7YbuEpFnpax-CnY47lYcdj_cMisbwn6pman7bHxrmrZQOANVEs4jndmrJ5RyzrxpFSGUGWTev8yPKUiAXfCZ6SLzB1b7Z4lz4LzJfZ3PThU_kcviD8hgkjGNOURr7t571IzfamiIZ_lo275PQmqHj3P4-leq3prcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
گل‌دقیقه 120+4 یوری تیلمانس دیر هنگام‌ترین گل تاریخ جام‌جهانی فوتبال لقب گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97544" target="_blank">📅 02:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97543">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJj6-ibqI588kVscxmdiLUHozRPyrKTcV-rKTKuk-hO9qOeizSnEd7bDdSjw6vh7wvEMUHWmqV6Xn8Ub_06JTLtHQpZtEymzXT_EF4XfcDUOEDVkPof0LS8A0cCOGOMOK8fwj5Saf4Ghu2JQM1up8I1K5CCvakhjHiTYZolpjWNA84TK5i5fS85emAlOC2zXGk-S5PWN0an08G00QItP8MDVWNhM8InOF_SeyRtIaYAvpBKVrBT0rl7P9PhHUATSOvocRLbpETkoosRkCx6llxrZ_NlKooBRsIicc3OfLCKOvUbk8nMAN3kHyH-TqAJwESOKZAItm9Wx9bcirShffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
آرشیو وار:
پنالتی بلژیک درست نبود و به اشتباه گرفته شد، بازیکن بلژیک خودش باعث برخورد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/97543" target="_blank">📅 02:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97539">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-fzd86ku4ySltq1JbnCehQ9l-J_R4XbGHZQdA_uD2gkBnjAqQNDH0ZLjQOogf9DwI1lMzuY_6LsLZjy477auNCWx5yEw-5pFpOVP-5fatWUQ_BbAeJpVuSIyMybO5qfwn_poNN9ZvP4xAUVsJH_xaonha9voKU_WOXythvQRnJ5vISraCjA3EaYxRNt2MKByGNsFS8t25chusBfdIvkK_BUB0VmfyF1qQ49JqCa9UN7GLzQML8Oh6RsStLxA9N96fO0GTR_GE7RqHlpBtwhHOH_fNOuAKj2TWr8id-Gn3o30hc3kTcz798tVqqOOXctFb7J1jTAEd_NBc0nf66PJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-fwXfk7fbCuQwB2JcLpRhXRgmzLigKdVuJpMuNAzTqj28vD9oXRxdnOc0oCmNQnOgXbKuQraHd6NABaIzxoYkiSONH1GhU6aq7N-dIhpoHe5Cwc6tBkfqrZsR7eOCByPz2F6Rl8XBJ2b_OaJNJ4vcUsZ1PzX-QKyWjFYXDkKAB3uqufHaT55xDRy1nHHtmP-jlnk_3KnteDFKcTdBqaVgcNS4kqSUmINVBX251yeaCK8x8Y7XdFW74JPzXjVp0sVFLE7wF-SuZJz8ZlHJDKMXtgJmsBPOLLRzWHfA-fZINY5vEQzzD8YnO4WjT3IuyCNiRrkcqeEjZws8Fil7Zkkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🏆
🇧🇦
ترکیب آمریکا و بوسنی
⏰
ساعت 03:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/97539" target="_blank">📅 02:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97538">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luqk9cVrvp8iQI5xI9RGqZGADZRqfV7gHhU_MYAi3QzPDiluA9FC7LQO8xVz1ZBedkt6-zzlXwWlKpJ-QVteFOx4TRgj-kC7ls5LdK-uMZrSeWgrPqtwfYarrJ9fnvJLdZeQOFooJhHmxdvXGrDC_v5YW4TbpqsL8mQS0noXymfGRGPqZvUG1MmCMAUstGuhaXLgjNmTTSpbCMw1K-6monXRHvxY1HK4kc6R8V2KIr2CvsSjNxonp2VE-xgHcH3lXPu41i9MK74joNPabjt-8p92t2zmUJjK88-gcrCvBAt0Fjqc99WbD6hnaiImVCm9g-CrWOhWQHQmMoZ90JWH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇧🇪
برنده دیدار ساعت‌دیگه آمریکا و بوسنی حریف بلژیک در ⅛نهایی خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97538" target="_blank">📅 02:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97537">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O80UA9W5lnqQsFo4gQH3lYcgmrXbO0897vXTA5_sKE4t9T4NJZV8SlT7wS8wditZfMmgUrwzR9sun4CaIfkQzOo1EO3oM8K5_CKWnC6tkDVBkLXNwvnu5A3SHisI3NpX3CQw1LK9XaXi698GE1c87Hfa_V_NsqPJxMHN1QhPrRd5RV00E8maooicTKjqIoGtYwc2_5yKrxOkbXEEomLPwHGcpeabXJWPD2Xy27t8P1_kmXhFOPzL_Vcl7qJkkbDx7pD8ASJ72ZqqGo58A_jVsJPnLc_NkHvwy2ly74P1YAROflt1UhFythv6rvtwo0v5TqgYE3uqw0leyRwyYEpMWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های فعلی مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/97537" target="_blank">📅 02:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97536">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLMXXHN6Ql7wUAHDVVvxtApuAlqqm3mCuRwK4wheNzc0ZYXNDDovzJ6MQiq7r39Sok9w9JnC9HqEQo1qPq5c1idK1NNcYNNEsaOzgwT-HFdBLesg6SkmrudTgqwjPl1_9blSCzIBVatIB6zMaej-YzL5kiTcacg86zdi6onlJMhKnR6F2J_gJqykssADOqyZSq1yXU9pqaXOLPUZXOdyYjFpDdpaetve6gwiq2N-bke0CQhDtHsIBn6BFCnMYDU0X5-SgOh8UMYzPM2EjILc9efhD5OPLx0_lVOr7KiE6fE_o6JUDPsEEm2z9B387JhXDneH-GpxlERBKqoDz8i2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
و تاریخ که باز هم برای بلژیک تکرار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/97536" target="_blank">📅 02:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97535">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i11h5z2V-dne8AOabimSfiA74F4Ie3-TVa6fCqLx4pIIB6alsslA5GM5I2zyvPHyPnm_TWcGQXzrKThdAYk7hOUQ7Pu-FgqIQtIYm1r6aHLZJAgmBaeNIhU9DPuNv-3xvSlYBbVAtw9NOfPcewwU7CJoaLnWW3EjzVmnb2TjhZnnO8QKUWo6uaOOonOIu3idIpCFHFDjAtF-_slDvPM45iJJkpgsQ55f2ydsNrVXrimkhxiffLOcVQoKLoVhEiF--8lXspQT7YR1KHxHoUfSWNZPFnVvn8W8hi1Vmx2lD66eq9axvl7gE0MG33jR1nA4c7JWm2p55eZ3L8pNTYvkkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک بلژیکی‌ها با پنالتی دقیقه 120 تکمیل شد؛ بدون دوکو، بدون دی‌بروینه، با تیلمانس!
🇧🇪
بلژیک 3 -
🇸🇳
سنگال 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97535" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97534">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بلژیککککک صعود کردددددد</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/97534" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تمامممممممم</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/97533" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97532">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تسلیت به هرکی گرفت خوابید
😐
😐</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/97532" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97531">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دقیقه 131
😐
😐</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/97531" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97530">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">میگن پنالتی شدددددههههههه</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97530" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97529">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چه حساس شددددده</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/97529" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97528">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سنگال فشار آوردههههه</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97528" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97526">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0db93ce7eb.mp4?token=BIdrZH9br8VwgIM4DpyOTzfUbgVPBJ5JLvxak9i0tkKXpq_LT9jYHNg0qgwHMkm0xMwWYYF95HlVqkDX25ah6qSJY4pUZXiPSPZ-l6oMXPFnHVeFrPkrrjAMt7AC4aGPGDojiINXsLfWUt_eUCyYbSnwLGG7oyvnenAsYh2CgybyO8ptxgWvLoaSIGnnn2mAKUV1D8t9VZNPddhbCk6mxlwynW77EqzDRVjYW5W3GnWSgwXbVB6Kaxki8u8vg7fDMk1-tWZAXUSsV3lpd5w-aFR-GCLI9cr_hJUjComwt5vO92umvI0NbRxsZlnGVERrP8kcfSoXmo82q8mL6K5I5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0db93ce7eb.mp4?token=BIdrZH9br8VwgIM4DpyOTzfUbgVPBJ5JLvxak9i0tkKXpq_LT9jYHNg0qgwHMkm0xMwWYYF95HlVqkDX25ah6qSJY4pUZXiPSPZ-l6oMXPFnHVeFrPkrrjAMt7AC4aGPGDojiINXsLfWUt_eUCyYbSnwLGG7oyvnenAsYh2CgybyO8ptxgWvLoaSIGnnn2mAKUV1D8t9VZNPddhbCk6mxlwynW77EqzDRVjYW5W3GnWSgwXbVB6Kaxki8u8vg7fDMk1-tWZAXUSsV3lpd5w-aFR-GCLI9cr_hJUjComwt5vO92umvI0NbRxsZlnGVERrP8kcfSoXmo82q8mL6K5I5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇧🇪
گل‌سوم بلژیک توسط یوری تیلمانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97526" target="_blank">📅 02:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97525">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MErExgKpX0J9CsgguTxpuu_yeSsysQvWXcfPx-lN6bqOcGYt_lhl5-2HSk4lM66i9GaDTOoR4wD8_H247WF2UbvVVP8CgyM2KC2e09Tj4LlhzOJNCnixMYHdTR8uHR1IfA6rln21T91svSySjCAdLDLWgn8ueLBkvH6wZL8nQOo_6VW_6LS3QNL9ag8INHyOlxJERNDb7-jD3vqOnDm6v8QntGCs6ThHfrzdSYwTT1xqX1rpoEzmXd6XObBEl2pb8jSWM8nOzDFzYJdj8DLgJJDU7T3xNWI_2v__Iecu8uEcFxuCOcDqLsePSurz_W-BrUsuoj_bs9etISoDv6_hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب کامبکی
عجب دقیقه‌ای
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/97525" target="_blank">📅 02:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97524">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عجب کامبک تمیزی زدن
یکی از بازیای قشنگ جام بود واقعا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97524" target="_blank">📅 02:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بالاخرههههههه زدننننننننننن کامبکوووووووووو</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97523" target="_blank">📅 02:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97522">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کامبک تکمیل شد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/97522" target="_blank">📅 02:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلللللللل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/97519" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97518" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">لوکاکو رفته پشت توپ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/97517" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8J_l-N7hl6S9uFv90GeFkt0NWLRCDQeQizXicIiKoC0DcoFD9h7Sbb8_YFjbG5fklG1bcancTSbnJvPGz1-o8BabEhCbldth2klqpcjbsb15_gBFCQxr8BQSVtUR35P6RWuhQf9l81kPDkHigwGXio-4HbLievtTmnWXV-PH5S21Xk6CCX8VcK0IzDkdPtb86ZRfqD4t6XRlahZLmXUfGKE7U2zN2PJB_yp8UC-3BbY3fyjXYStHjlPtvvOvHOTawxFIGisbkVldddRzAE0FctFq88BihIG4_iHWET6Kb4HGG8TYyA23vpYEzopUPIUSZaNsCSjgM_ZpcOB28phow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کااااریههههه ناموساااا
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97516" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خوابیده رو نقطه پنالتی بازیکن سنگال
😂
😂
😂</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97515" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دارن کرم میریزن تمرکز بازیکن بلژیک برینه</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/97514" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97513">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دعوا شد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97513" target="_blank">📅 02:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سنگال دعوا راه انداختتتتتت</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/97512" target="_blank">📅 02:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پنالتی احتمالی برای بلژیک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97511" target="_blank">📅 02:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97510">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سناریو فینال جام ملت‌های آفریقا برای سنگال اما اینبار تخمشو ندارن تیمو بکشن بیرون</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97510" target="_blank">📅 02:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97508">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چه دقیقه ایهههه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/97508" target="_blank">📅 02:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97506">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDHCbDFNFbPBKVtCovH4WWAzAUzsGg9aOhiFrA3M8MQjPQFwJ7PjGHu982krVUzCFcBaOEtkLnJQPDZVGXMco-9Bq7x1P70V3ARR-3wo9ujxy2IqCfLLZWOFd2BqiaO-oKzZpeAqVlv5ivnQ24IOHKj-VCVTWqoRT02Q2T_UqAMzJ8oHqRyhOffnVs-kcBI1kzwdN6pAYz67P8XBjo7uipM12qXz3mD5kX3UxbOBO7jg8_phhCjlWGz1vI2bKVU8dVW4DJnyMXIYrU7kTsxSlQr-zzY9D-jSDgxynPiRkIoaAUSKBBuALLZxCNJHhIYmAjd0h1_YWG0YE7LovwmFKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
پنالتی احتمالی برای بلژیک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/97506" target="_blank">📅 02:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97505">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اوه اوه بلژیک زد تیرک</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/97505" target="_blank">📅 02:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97503">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsmSVazViV6p3S8bnmqC2w3LDnkLbYCcFQgrzb_bQT22-EyG6EEHF2Iqr_3zgyYMWjTckrRwnXN0VVFgRVETpsLpAiPnYcapyfLk76N3NRsPTAe4Wk09sHoHPMkA1xF5Y4oRJTE0lE8KmcXYOxQVWgjkJfyorZIA0eW17WPrWkShiDRFLB4lck0vhyXbBl75GkTenmnKnYw14Uo4nv-Fs-dcDj51cOkZYoXEMvqDMLmIQEuxsu2Qmgf6YG7uLT_MjymwGrS9SRQJpKF114Aj9rXFldlKJ8sL_mpJEJcgxjLheQevGOg21DfGjTk9MyIHPuwl5Y89dAtpkqSzEEFX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GkdDb0ebYBJd-2ktsruguDbAb9p89k93PPrRErd-jBFu057fjJPN2n6-R4GCFk-waYHqptI44LyIaIyyGZ1-po7aPJbJ2Maw7AYtvVPWhdE-V01ySITM6scs1Y0MsvYFPhg1GI2l2B5cXZkAlBvhQxBCRg62iG-9l-woQPa3iwIK1NaxM6AWYLkTYWfGVcTrCoI0FbJmqiRCIjrBP1ACkuBADXmyoPRItVwJBD761bpz_sW4DGoMJaiCTYxh2EMgigxx3PThmPULSy-omAIAFMK0zqMJDZX_JOXVZ9B9Apxb2cjc1LGZhiIK1xlreI9K9WnPDdck-Ir6_joiQv2Adw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو  تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/97503" target="_blank">📅 02:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97502">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItzKnGWXybFJ82PdsN-y78oYKzmRK5_uGK-Pn0FTnmc0f_SIoFefnnMAG_xR24jGRUhIFfdW6NY8YeC1dNfi2pWJrqZymZbGIAg9w0rE3l2UNOEo6Zwa95ir39D2f6zXjX1VOfWSg7fLQafWZD5s-22ugltjFGftrCEGEtZb_kSqGNqKivd8jVZvGUhJFtzgm5P0N3M6G4FnKTdG4AKNi3Dcu8iQSAo2Rz4B5ZhPr-T_8fbWgKtQ-WxPCshaycl-IbpwU42dxAD2K29gZ1VDpamaFS7LYfr4thD6BSxFGlPZyT5sEgfHmQn8XUqYknlEXDia_XCzsVAzOB_3wPWeNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
لامین‌یامال: به کوکوریا گفتم که اولین الکلاسیکو که جلوم بازی می‌کنی جوری میخورمت که تو بازی‌های بعدیش خودت به مورینیو بگی بذارتم نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/97502" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97501">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0badec474.mp4?token=qSgc7PNm6FthOCuuRwiN-FCwSNFbUTqY-CdFFTONWa_Wf6-vJpF_zwvIyui5xPxKmm5o6pPIe_MLxLYYO0vLdwdOiyCIdcWkIIC31WWAxUb4nqpcIZN-pz-2Or4SFnyONPhVKA6IXJBnp1Dv2aDv_B8Aq1-lTU3OdKtd3GayUG4HJyX7ALSqODYxM0RHaWJOMXpBsk2wyXutTt1xrP9vLS1MTYga0R7MuMMSGV-7jzFi9hyXSf5z4v5F0KfmT_OdCXOjx7JWkZMPxB6NeOMLEoGF4YpWITZcL2R_PbnTJPanxBUfOrDzeV6RhhbMQMjSmp3TZH9d7AV35kAhYk-9cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0badec474.mp4?token=qSgc7PNm6FthOCuuRwiN-FCwSNFbUTqY-CdFFTONWa_Wf6-vJpF_zwvIyui5xPxKmm5o6pPIe_MLxLYYO0vLdwdOiyCIdcWkIIC31WWAxUb4nqpcIZN-pz-2Or4SFnyONPhVKA6IXJBnp1Dv2aDv_B8Aq1-lTU3OdKtd3GayUG4HJyX7ALSqODYxM0RHaWJOMXpBsk2wyXutTt1xrP9vLS1MTYga0R7MuMMSGV-7jzFi9hyXSf5z4v5F0KfmT_OdCXOjx7JWkZMPxB6NeOMLEoGF4YpWITZcL2R_PbnTJPanxBUfOrDzeV6RhhbMQMjSmp3TZH9d7AV35kAhYk-9cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
هوادار پاراگوئه و سگش‌ موقع پنالتی های بازی با آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/97501" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97500">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/97500" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97499">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nd4YgHkbspugGli0Gbal7MOCVsnMSxBgrbx_jQUz3R1Tkt5Vc6XGuGT_949fubR-GwKTHriMLncQiUlxPiMkoTLrvzT8ObJPw6p-uAKGWiHSVeVbraokjSqr1realjzUaX4MIbvf0UPuCqM60L40qfm5SadlM83QKvNqebVT886Xc2WXu8ZrZ-of8pAbbzwOt0qlLdgrNq98hKqlvPqkzqMPacql7VQBA2TSzIfcTseZa2i_0Jv6LTJFjVZrbY0HS_3mm5pFCoj8pAbbsl1IZZ683kJzYVGhpjrTqEpi-A6sOblPwCC1RkxmmyvfEzUfigenz9HecZYb8mx9JyYVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/97499" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97498">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیمه‌دوم وقت اضافه آغاز شد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/97498" target="_blank">📅 01:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97497">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2410738935.mp4?token=EeiDhiHi751xvdQ4UOalBuPTekP-oEClLqYztUyuZhLImX1cKwJANZ1Dv5udAxVQCHVc5TZkJDbQQ5wKUlBWtUBPLXZUzB0UUIRc6gkAjUaUQLI0DpBuTpBpS9hNDDPMTC02HI3_jQVMdq5CF0I0MKhmqdW3Qr4onFoU9oAWwW560wIdSqlEJi8EYPpoHYQsgk2tUzZskE4n09NzN8j6QIJs-Ggm6blt2bfYGyBjc6leUtiWXAuuvSVBdSy3NfbwbuTpn_FwV6EA2I7SqzIAFD_Z8g8yhf4zGvNPRrRThjcj9p0XMM_k4FHRYTXPE-bC1mhTuaD8QjxmwwZSGkzNew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2410738935.mp4?token=EeiDhiHi751xvdQ4UOalBuPTekP-oEClLqYztUyuZhLImX1cKwJANZ1Dv5udAxVQCHVc5TZkJDbQQ5wKUlBWtUBPLXZUzB0UUIRc6gkAjUaUQLI0DpBuTpBpS9hNDDPMTC02HI3_jQVMdq5CF0I0MKhmqdW3Qr4onFoU9oAWwW560wIdSqlEJi8EYPpoHYQsgk2tUzZskE4n09NzN8j6QIJs-Ggm6blt2bfYGyBjc6leUtiWXAuuvSVBdSy3NfbwbuTpn_FwV6EA2I7SqzIAFD_Z8g8yhf4zGvNPRrRThjcj9p0XMM_k4FHRYTXPE-bC1mhTuaD8QjxmwwZSGkzNew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤪
اشتباه نکنید اینجا اروپا نیست. اینجا یزد خودمونه که ملت از گرما اینجوری رد دادن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97497" target="_blank">📅 01:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97496">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بازی رفت وقت اضافه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97496" target="_blank">📅 01:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97495">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e236b4c020.mp4?token=dx2-fSvTQRMJzOXfVldjyhhCvuJqdb9ze0mdSR6nVAh5Cw33daI2EDqoQKDLwiCVINQRzSzhpSuKD_4yZWArzWyk6hnry35R2oAdlBMHjK-WzidiyaHaspHcN4BzqbxMqaOYPaq3MuI4Vw_YE5Zi3Y-c4SAj4WE_kU7m22tt3hkAMPRmO6W4JqC2ukEsHwjEha1qVDiiXgiCMpFQGuIZR2T6cAFrZX-pJY7FPjyu79K-kos2Y7ljFjJhDqiVTlzKGPqGfncmRjRQ3Gpl5g1InME0n7sSxCLiKR8X7uKCzMKZM0iGmwxcdhlCNIt5Fl2DQt4e94e8OJ-CeqkD6a0Mrb0lQpzrVQUDNPPlvpHMlSenmd_Ybw1s9Po9kTJp0jck6LeCvhooAl783c6Acped0HrIZoZF7NwFLYjoRjwbW12uuMkXrSYpK_MNb53wrYWcNAFV2PS2bVMd_-abNNdvjjfMhw2lGor7Vb2aVSzNPFkDY5uNmjscITOuIGUZ6s3O3eoH0ja0C2DitUFPreff_MuskfSv718asp81XnhKWSnpx8mozFX_iGLusyynHirv7LC7SPT53srWsOFR4KPE3CGHsjeEvlPO8YTByTmctIat5sioTIz48aWWRVrww2tx_8fF32qVB-B9hTosyriwQ9fWHD8q5pQIGoSH_C0vRgM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e236b4c020.mp4?token=dx2-fSvTQRMJzOXfVldjyhhCvuJqdb9ze0mdSR6nVAh5Cw33daI2EDqoQKDLwiCVINQRzSzhpSuKD_4yZWArzWyk6hnry35R2oAdlBMHjK-WzidiyaHaspHcN4BzqbxMqaOYPaq3MuI4Vw_YE5Zi3Y-c4SAj4WE_kU7m22tt3hkAMPRmO6W4JqC2ukEsHwjEha1qVDiiXgiCMpFQGuIZR2T6cAFrZX-pJY7FPjyu79K-kos2Y7ljFjJhDqiVTlzKGPqGfncmRjRQ3Gpl5g1InME0n7sSxCLiKR8X7uKCzMKZM0iGmwxcdhlCNIt5Fl2DQt4e94e8OJ-CeqkD6a0Mrb0lQpzrVQUDNPPlvpHMlSenmd_Ybw1s9Po9kTJp0jck6LeCvhooAl783c6Acped0HrIZoZF7NwFLYjoRjwbW12uuMkXrSYpK_MNb53wrYWcNAFV2PS2bVMd_-abNNdvjjfMhw2lGor7Vb2aVSzNPFkDY5uNmjscITOuIGUZ6s3O3eoH0ja0C2DitUFPreff_MuskfSv718asp81XnhKWSnpx8mozFX_iGLusyynHirv7LC7SPT53srWsOFR4KPE3CGHsjeEvlPO8YTByTmctIat5sioTIz48aWWRVrww2tx_8fF32qVB-B9hTosyriwQ9fWHD8q5pQIGoSH_C0vRgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل‌تساوی بلژیک به سنگال توسط تیلمانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97495" target="_blank">📅 01:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97494">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هفت دقیقه وقت اضافههههه</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97494" target="_blank">📅 01:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97493">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو  تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97493" target="_blank">📅 01:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97492">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تروسارددددددد پاس گلللل داد
😂
😐</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97492" target="_blank">📅 01:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97491">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کاپیتان تیلمانسسسسسسسس</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97491" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97490">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اللللللللههههههه
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97490" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97489">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مساووووووی شدددددددد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97489" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یا خدااااااااا</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97488" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97487">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گلگللگلگلگگگلگلگلگلگللگلگلگلگلگالگلگل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97487" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97486">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">لگلگللگلگلگگلگل</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97486" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97485">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0dcdf5a8a.mp4?token=JMcebbkfdElwGohqEDNIOlv9NU4L6sKv4ARGO6K9tNCLAYpAyue0kWQ18lhOehrvgehL_sQjp0wpyRcPFBbN5uM55I5zVhM_nOhHPW1r6-2N4r0k4u2v-6TzaN93TK8Uph54uBgsZwUPyzi6CPyqifYOYh30kqoDlybd5yes8ZL7QaxXqROfPhDDoGfXmEOkHvXBK8UcabomsPDxjjTi5IKrjBq-1l3bvR0Ubv013RXZaKwBA_cjVeHKpKTLT5C0pfQ-UpsCKV38_13VgXyPyZ1cXlHGgdvgGnc0UuUP6VqJ_xbcYJvg1DylzMFsHmw_JzZ9ODXeoa2fkCnxs7ZZT0J9XtivpKF8MN_g3pLco8tL_fLgdmpvdRhnGUhh10Rm4C93xv_H3elOdHI7XpquhHzyy5hnnZRsv_NYCYdDjIY6zhwDYfOUoTrXGGpvObmF5n9SnT-wlosBowoKtiRudYn7ElQGgh3fCs5NorViCNF_L4DSSwEqIwF9U501WLzIbtVyG0WhYW8HVclCwR6C7XMD30jNCTxhROmjUaIuRWRENuIoYm8UpKom9uZmFhcbco2LlHMF-OactQSQmJzFxRHZjmmDqheCy6iVb_Kjaw4OwLMZZ7a3zXXgl1Tiao-obCbAJyimz6BDh0pWfNzZqp4XGWpvOTb_ie37GlnNxMU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0dcdf5a8a.mp4?token=JMcebbkfdElwGohqEDNIOlv9NU4L6sKv4ARGO6K9tNCLAYpAyue0kWQ18lhOehrvgehL_sQjp0wpyRcPFBbN5uM55I5zVhM_nOhHPW1r6-2N4r0k4u2v-6TzaN93TK8Uph54uBgsZwUPyzi6CPyqifYOYh30kqoDlybd5yes8ZL7QaxXqROfPhDDoGfXmEOkHvXBK8UcabomsPDxjjTi5IKrjBq-1l3bvR0Ubv013RXZaKwBA_cjVeHKpKTLT5C0pfQ-UpsCKV38_13VgXyPyZ1cXlHGgdvgGnc0UuUP6VqJ_xbcYJvg1DylzMFsHmw_JzZ9ODXeoa2fkCnxs7ZZT0J9XtivpKF8MN_g3pLco8tL_fLgdmpvdRhnGUhh10Rm4C93xv_H3elOdHI7XpquhHzyy5hnnZRsv_NYCYdDjIY6zhwDYfOUoTrXGGpvObmF5n9SnT-wlosBowoKtiRudYn7ElQGgh3fCs5NorViCNF_L4DSSwEqIwF9U501WLzIbtVyG0WhYW8HVclCwR6C7XMD30jNCTxhROmjUaIuRWRENuIoYm8UpKom9uZmFhcbco2LlHMF-OactQSQmJzFxRHZjmmDqheCy6iVb_Kjaw4OwLMZZ7a3zXXgl1Tiao-obCbAJyimz6BDh0pWfNzZqp4XGWpvOTb_ie37GlnNxMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل‌اول بلژیک به سنگال توسط روملو لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97485" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97484">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وقت زیادی برای بلژیکی‌ها نمونده</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97484" target="_blank">📅 01:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لوکاکوووووو</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97483" target="_blank">📅 01:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بلژیککککک یکی زدددددد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97482" target="_blank">📅 01:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97481">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگللگلگل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97481" target="_blank">📅 01:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97480">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
‼️
نیویورک تایمز: یه شهروند ایرانی - آمریکایی با تهیه لایحه‌ای علیه فیفا از طرف 90 میلیون ایرانی از ترامپ و اینفانتینو شکایت کرده و خواستار پرداخت یک میلیارد دلار غرامت به ایران بابت حذف از جام‌جهانی شده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97480" target="_blank">📅 01:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97479">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو  تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97479" target="_blank">📅 01:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97478">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prlowC0f-Ap3aOIfBGlRfGPFpxF5iiRN7of2xVEYXGNZKYpBCtADnInRhM8lEjI4l6OSDy8eTBtJT6I9KnvygHel4QPuA-B0sTKv-g5YwJmvKhKvFIphF61RZkYNx9wm3nBB_0Hk_ghAXzHjx42sOpHfz-j9l7ECaF7V__9HERMgKLNOwAj3IL-3wqdR3GxRGhWVlsgrIrsXOafGlKPryAUQ--86Lz0D8xhYKpv5kmsRwqTqkNriNDEOx5g7sOx2b2OtmQ2arPpZY6HM19acuLOUQGbvCCwaGsbtOjUfyAJWtgRqLaUma32IS8mT7X-cmL16ToHxO2d5DCBn8JhoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو
تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97478" target="_blank">📅 01:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97477">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52150cb58.mp4?token=KlL_4g1kPZPC9JNyG9AXLahswgqSGEleTcYmpwpTnofZvqt7uAyw8JtwDzgLfvg9B2UXomjb6TBS7m2t5GUSSeBZOIGA3BKBJdiQ-ranFuJ86QPBb9yMKGIMPZ8aezehQip6IWeLIZ2SR5x3AoXyU7zGAL8qzpRLIYgxDnT6krvyX4EoZWNZUdKbtByFN2ryZAnsagVyVdEaN-FsZ6nmSNiW07baJZfe8pg7oNLIBPiLiZw8v9yrIg0nIeVL1C_LYd5P56YhS_g1PKknxtX_piIpzzl0hrwSaekdM08S8B1WPDyKhTfnOdpJxCLGbgG0GyKML2EvGhN77iPuOLV1Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52150cb58.mp4?token=KlL_4g1kPZPC9JNyG9AXLahswgqSGEleTcYmpwpTnofZvqt7uAyw8JtwDzgLfvg9B2UXomjb6TBS7m2t5GUSSeBZOIGA3BKBJdiQ-ranFuJ86QPBb9yMKGIMPZ8aezehQip6IWeLIZ2SR5x3AoXyU7zGAL8qzpRLIYgxDnT6krvyX4EoZWNZUdKbtByFN2ryZAnsagVyVdEaN-FsZ6nmSNiW07baJZfe8pg7oNLIBPiLiZw8v9yrIg0nIeVL1C_LYd5P56YhS_g1PKknxtX_piIpzzl0hrwSaekdM08S8B1WPDyKhTfnOdpJxCLGbgG0GyKML2EvGhN77iPuOLV1Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇻🇪
آسمون ونزوئلا چرا اینجوری شده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97477" target="_blank">📅 01:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97476">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به بلژیک توسط سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97476" target="_blank">📅 00:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97475">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به بلژیک توسط سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97475" target="_blank">📅 00:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97474">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به بلژیک توسط سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97474" target="_blank">📅 00:45 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
