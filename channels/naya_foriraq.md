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
<img src="https://cdn4.telesco.pe/file/N_2p63R1q3m-48b1e8m6_qd8DexEp9sLSvmHbwYn9WC-8Ifg3MHm4dZZjVdAMjhT7Yd68iK6p-ictP8BTrzt9cqQ70D4CsHWbPSY0WWmL1b3qol-4S0SDdxQPvoXEa7FgVNI7XQB550MWNozg9Z4vqEIE-P_oSDMD0GZsrhmxLnoZ18ZQuzuFeoBaPsqQd08a40Er-NoRASyqY2OiVDGK5buVB5Cjt6UuH-eRg14fdQtWcMNwpB3Yp1yFbAPI8VusO0cj_AA8lg-bOE0uCfeAT6UAWoUGhnObmohjxUK73KLm5F6DNcdUXvaTv75m0ucxoPpA0Zmm9OAaw6kYRZgNg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-91082">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2a9c2ef40.mp4?token=aQVEefQ8_Jo0llud59BEq6izKCkRixDtvzrmfG0RVyOgITO9LNoLmR_KXXsUpI9ap_WTEMKxID2XRWutpE4IBr7jnTpWMUVAmdfVpB5id6ZjZORVghmiy_HyyvJ2OjsaNHwy5OPQde3WNmb0Gh5fcdxGtKqABrtHvJPOy8re9XPP3O0VjZYtRpies0MN0MEidzti27VfCI8RwRGZeUG_69h3v5CARhyAzVmOwmAGhXbQYD8mLEpgFySLBQlRyFysUy0EgOY37V9WDrhYhQVTzC94DRJOgxW43NXMydaLnrzuPfUTwpzaIuUtrql6GVaFPr1eAXDneSnJJ0pZuX53fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2a9c2ef40.mp4?token=aQVEefQ8_Jo0llud59BEq6izKCkRixDtvzrmfG0RVyOgITO9LNoLmR_KXXsUpI9ap_WTEMKxID2XRWutpE4IBr7jnTpWMUVAmdfVpB5id6ZjZORVghmiy_HyyvJ2OjsaNHwy5OPQde3WNmb0Gh5fcdxGtKqABrtHvJPOy8re9XPP3O0VjZYtRpies0MN0MEidzti27VfCI8RwRGZeUG_69h3v5CARhyAzVmOwmAGhXbQYD8mLEpgFySLBQlRyFysUy0EgOY37V9WDrhYhQVTzC94DRJOgxW43NXMydaLnrzuPfUTwpzaIuUtrql6GVaFPr1eAXDneSnJJ0pZuX53fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الإنفجار الكبير الذي هز محيط مطار أربيل شمال العراق</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/91082" target="_blank">📅 17:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91081">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1de0d9f90.mp4?token=vBoRCqCqvCF9ZlQnRnJ7Q87br7fvZfocxr-kc96O12rR9dV4jyV_EJNprSimkkorNnolzXP-9_JefVJ7aqjidqEc4M93yBkubWeT_scFL3Ndpx5LVonefFZTLu6ekA5SheLNMkucrYCI5lH1AUUXq6zw3RVCb3WXi0XG36vJCANWXjKoKx9pd2iCcfVoQ3Xahxia5xu1MS3CwGctc9qz2P4_UY9Iq0sYAGl5ISzVvukG5oiFlPfI04g3VrH6ME_ME6XZh0MR76NE0b2-DN7Fxk6GqqYE1AwB8_cCKlSe2L7BV9po4xM0l23B76nEGxbBReKOkZo50nMEOd2Rw2X-ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1de0d9f90.mp4?token=vBoRCqCqvCF9ZlQnRnJ7Q87br7fvZfocxr-kc96O12rR9dV4jyV_EJNprSimkkorNnolzXP-9_JefVJ7aqjidqEc4M93yBkubWeT_scFL3Ndpx5LVonefFZTLu6ekA5SheLNMkucrYCI5lH1AUUXq6zw3RVCb3WXi0XG36vJCANWXjKoKx9pd2iCcfVoQ3Xahxia5xu1MS3CwGctc9qz2P4_UY9Iq0sYAGl5ISzVvukG5oiFlPfI04g3VrH6ME_ME6XZh0MR76NE0b2-DN7Fxk6GqqYE1AwB8_cCKlSe2L7BV9po4xM0l23B76nEGxbBReKOkZo50nMEOd2Rw2X-ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق أخر من الإنفجار في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/naya_foriraq/91081" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91080">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2917e33c9a.mp4?token=R8Q0cjLQlDXCri7i_dt5MwtWgeMjFJHPwy0kvrDMZzpuqJQBA8hRN1OUjgrUI0YFVekYp1dbefL3NEf3wK0RRZHRL2XfvzgIwU66nIIzmdDz_kveQcSKnNVwyW-oFRuZGwOsMXUA-uX5nMm-70E_KPe4ICuhuY0zkfXTNw4fROj3Wwn82evtUWZWsFL7qFzt_1yo8Rq5infQGCJUcUgix6-aFQaDcQSqV7Pw8gLGCqBRloxDHrKcwiFruX-d2b-Cf6z9_GaZ195XELgb62abkXA64bFDn3696qpaGYYPOhQ2z0yAudJsVcMq_maIVTRl5D0XDDF085sWGJ9SNBtGYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2917e33c9a.mp4?token=R8Q0cjLQlDXCri7i_dt5MwtWgeMjFJHPwy0kvrDMZzpuqJQBA8hRN1OUjgrUI0YFVekYp1dbefL3NEf3wK0RRZHRL2XfvzgIwU66nIIzmdDz_kveQcSKnNVwyW-oFRuZGwOsMXUA-uX5nMm-70E_KPe4ICuhuY0zkfXTNw4fROj3Wwn82evtUWZWsFL7qFzt_1yo8Rq5infQGCJUcUgix6-aFQaDcQSqV7Pw8gLGCqBRloxDHrKcwiFruX-d2b-Cf6z9_GaZ195XELgb62abkXA64bFDn3696qpaGYYPOhQ2z0yAudJsVcMq_maIVTRl5D0XDDF085sWGJ9SNBtGYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من الإنفجار في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/naya_foriraq/91080" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91079">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dda549321.mp4?token=R_ltUYCiaftk7dhF8LX3pKmB97-Fs0pPSf1jiLELWCNUmDcAfcqk4IdaFlgCA5AeD6eL0Bp8_baubjhOnvZCFyVNihbPYYQ4MfMgO1XHOnYChgmLUdQ9f1w8OdxvV-iux1dWZnSRMG3GcLUzmmBITNRR0XL8Ljs1_Nw-QQMAq7RfRyhfgsCgT_nap7vwAA8VjxwQZepIUsGtBSlgE5i8_DJUtZRLayRBtuxFJeGG3iva-5WOSG2WluqCxJ2VyUttgVAv4n_VeMsQ6Skkp-1fw91mKpDn0uZ-6aEK5KaAyk65DMihXuaGwTuvnPDeQaXQ2TjEaaVuQlkFO3s8ZWma3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dda549321.mp4?token=R_ltUYCiaftk7dhF8LX3pKmB97-Fs0pPSf1jiLELWCNUmDcAfcqk4IdaFlgCA5AeD6eL0Bp8_baubjhOnvZCFyVNihbPYYQ4MfMgO1XHOnYChgmLUdQ9f1w8OdxvV-iux1dWZnSRMG3GcLUzmmBITNRR0XL8Ljs1_Nw-QQMAq7RfRyhfgsCgT_nap7vwAA8VjxwQZepIUsGtBSlgE5i8_DJUtZRLayRBtuxFJeGG3iva-5WOSG2WluqCxJ2VyUttgVAv4n_VeMsQ6Skkp-1fw91mKpDn0uZ-6aEK5KaAyk65DMihXuaGwTuvnPDeQaXQ2TjEaaVuQlkFO3s8ZWma3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من الإنفجار في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/naya_foriraq/91079" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91077">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO84mzWNYLuQxyIhphpxdOAPiLKSXAlGEtUHBQ0KU-j-8qZ2Y8Ot03O-mt3oecuXVbaBpQgbyYcOI4_CzrcD6RUxqwRuEZ6EiIFmUV-ddIBYRRQ85VPC_ym9w6IE_oRWGGBuB_R4ZxQy7DCzhUfn5thSjtUZ_zw7Bg2VBU2WCdsTYKwoNgVBfHLtBNpNFMf1KgM8-1C-oIiCoSSFjQTUVjO-BJvK58y80-4SAqJT6bQxainImECedt6d8eX_u3tskYn_y6Nzy78xMCW4XaHLzDP6tqHWf_YTYeIlRAaFr68SSj9BZ15RShvurUVdfMCXD72nOBgXP6S_rDsKGSXcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be83492421.mp4?token=AiLp9PIYUU60jfDkR4poh7CsfBgxe0Dnb6ClBAO_KLo5vbGRKKlcRY8Xilg_TlDmFoT4NRkRnd2rvKK20xwbv7laWSiE5x4NJnWTYgIzUxD2bELnTv_cJI9uwkeIZ2IRnitddv3Znw9PhSEHnvuMHzLHMuRaM2T0RaDftiS2N39YDd3HeplWVesbNYmOl8ZfuVs0ikPSFSotvGtpjHaGpXh760nSZRjgnZ416-TQViP4fhNA5ZGDVSCVjGIwTDVdwF57BiW-NSVvWXH753cPED4kwTLE3P4mtwnES_wWkihvNPAUsI3Qi-vuA24wLL89I9JKBSoa_FiejeWKobsXiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be83492421.mp4?token=AiLp9PIYUU60jfDkR4poh7CsfBgxe0Dnb6ClBAO_KLo5vbGRKKlcRY8Xilg_TlDmFoT4NRkRnd2rvKK20xwbv7laWSiE5x4NJnWTYgIzUxD2bELnTv_cJI9uwkeIZ2IRnitddv3Znw9PhSEHnvuMHzLHMuRaM2T0RaDftiS2N39YDd3HeplWVesbNYmOl8ZfuVs0ikPSFSotvGtpjHaGpXh760nSZRjgnZ416-TQViP4fhNA5ZGDVSCVjGIwTDVdwF57BiW-NSVvWXH753cPED4kwTLE3P4mtwnES_wWkihvNPAUsI3Qi-vuA24wLL89I9JKBSoa_FiejeWKobsXiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد لاعمدة الدخان من محافظة اربيل</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/naya_foriraq/91077" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91076">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6703af01.mp4?token=i6bcqh8TVVgbnc2aqQ4m4IHFNQH_2WC5TVJdOoaXIgdJ8TcX__U1nSWrDUVGcv1TCqSUg2NDhOE1io4cJK2M41gCEhgskxOHU5dXsKPox56FFEIBORI5ijhFp8S0dJLeRyEKJx76kdFRwldGFWAL2xcmFlF9hTzrfCysTrdkVjOjKW6BGN21OcF065q9MC7ZdKe1H5326ufW-s9WnvK1mzxPNSkGuVZDUZQ5Xqeo6KBexvYenMHCaTz31S3_wp8RDYjdkYD6vTnJxSG0pE61sQDj-h4ef8BY-a4_GB8WmWbVX4oekcgoSTqAOnvpJYOFijT9A04jg52diXjAfzDg2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6703af01.mp4?token=i6bcqh8TVVgbnc2aqQ4m4IHFNQH_2WC5TVJdOoaXIgdJ8TcX__U1nSWrDUVGcv1TCqSUg2NDhOE1io4cJK2M41gCEhgskxOHU5dXsKPox56FFEIBORI5ijhFp8S0dJLeRyEKJx76kdFRwldGFWAL2xcmFlF9hTzrfCysTrdkVjOjKW6BGN21OcF065q9MC7ZdKe1H5326ufW-s9WnvK1mzxPNSkGuVZDUZQ5Xqeo6KBexvYenMHCaTz31S3_wp8RDYjdkYD6vTnJxSG0pE61sQDj-h4ef8BY-a4_GB8WmWbVX4oekcgoSTqAOnvpJYOFijT9A04jg52diXjAfzDg2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اربيل بعد الانفجار</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/naya_foriraq/91076" target="_blank">📅 17:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91075">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21390d35ac.mp4?token=OB0HtHc7kmdCfmeM6_WtMHHNQ0lICnStVpIq3_I8tfb-IbKakIWjSxbU0Whzv9jTWN1LTD_LmJouTek770ay6_E3IezQ4pKP0OuvW3k4Ny9rb8KtvewAgUSraUVkHSS6PdZ1QzPAJrf6u21Cl7oWVL1IcXVVRZmiBGRCfqEJlOU0U2J-Jt32bl_41zjuQV_ZuLyWNzrM2XIV_ufblOXEIBQNpzlJfOjSHfxEjp6qtw9vSTLTbHvE310Fx13vU83NZhHDqZO7UxH8vfLAoIcchzEtV9Epqh5pRo9HUjiIiHJpSOgGQjJ3dFSvKbBvTUAFtJlGJS5uQS8_A7t_c2LKKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21390d35ac.mp4?token=OB0HtHc7kmdCfmeM6_WtMHHNQ0lICnStVpIq3_I8tfb-IbKakIWjSxbU0Whzv9jTWN1LTD_LmJouTek770ay6_E3IezQ4pKP0OuvW3k4Ny9rb8KtvewAgUSraUVkHSS6PdZ1QzPAJrf6u21Cl7oWVL1IcXVVRZmiBGRCfqEJlOU0U2J-Jt32bl_41zjuQV_ZuLyWNzrM2XIV_ufblOXEIBQNpzlJfOjSHfxEjp6qtw9vSTLTbHvE310Fx13vU83NZhHDqZO7UxH8vfLAoIcchzEtV9Epqh5pRo9HUjiIiHJpSOgGQjJ3dFSvKbBvTUAFtJlGJS5uQS8_A7t_c2LKKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لتصاعد اعمدة الدخان من اربيل بعد الانفجار الذي هز المدينة</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/naya_foriraq/91075" target="_blank">📅 17:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91074">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd255f2cee.mp4?token=Z68OFjSSe-LcW1xk9w5jHfkHd3l2jMz-1uu2mqWljBRp0VXTyh3jGFQl-7MmMIvMqiq_Jo8FayoMJ9AUHWo3JWpvXiDY4_uLchxfzsk1LUU8EMPej1WWfPE_8ZfR_-6CB7EI2UeCO_Uw7hVXW1Qbz89o6O7ond0iFpbAkVp8CjTS1me21MwvxoollUEdKqufsERyhCx8tzXw3QoKd1hSqcsWoeHQCjk9MR_qq49huSCb_Brm2R_nCdB2W1LEqR0lGbp8SOM31P4kRzAEORrLzCp6PKfzVfVLvaayYyaLb8YLURphrjlcQcTQ4VUqlpFzDW8_xZtLjbyY7tVNglPOJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd255f2cee.mp4?token=Z68OFjSSe-LcW1xk9w5jHfkHd3l2jMz-1uu2mqWljBRp0VXTyh3jGFQl-7MmMIvMqiq_Jo8FayoMJ9AUHWo3JWpvXiDY4_uLchxfzsk1LUU8EMPej1WWfPE_8ZfR_-6CB7EI2UeCO_Uw7hVXW1Qbz89o6O7ond0iFpbAkVp8CjTS1me21MwvxoollUEdKqufsERyhCx8tzXw3QoKd1hSqcsWoeHQCjk9MR_qq49huSCb_Brm2R_nCdB2W1LEqR0lGbp8SOM31P4kRzAEORrLzCp6PKfzVfVLvaayYyaLb8YLURphrjlcQcTQ4VUqlpFzDW8_xZtLjbyY7tVNglPOJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من محافظة اربيل لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/naya_foriraq/91074" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91073">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896895a5d7.mp4?token=mCKCsUNcbaAVP8lWGcc_PRXFWuPDSwt2iR-u-XbHfxuaARGc8c6OInZo7Ht0exbvb3mWIHAaiPpD7oIfTOPopy4iqmfS-N56RYPa-R-dnl9_98pKaBwwP0h1QLKiQEGd8LsnjeUMY5zF-mcLEU97vRkZHTzUtzk7Yc0WUkTbvVuIQYA2JkfQnXBHZ51-ehTJQ0CPurOFg9eniuy0-ivHGs4wRnZu3Sp3YbmssU8HuTuKzqsLbrrLRkIGXIn9hPrtAEh-l3nQcGo8htcNU2CwPQ49wW7nRSu_vTBt_oh96rkm8zh6vRQy2mxrH5Ilr3B75zVI2O-anwiOhOnCxhhIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896895a5d7.mp4?token=mCKCsUNcbaAVP8lWGcc_PRXFWuPDSwt2iR-u-XbHfxuaARGc8c6OInZo7Ht0exbvb3mWIHAaiPpD7oIfTOPopy4iqmfS-N56RYPa-R-dnl9_98pKaBwwP0h1QLKiQEGd8LsnjeUMY5zF-mcLEU97vRkZHTzUtzk7Yc0WUkTbvVuIQYA2JkfQnXBHZ51-ehTJQ0CPurOFg9eniuy0-ivHGs4wRnZu3Sp3YbmssU8HuTuKzqsLbrrLRkIGXIn9hPrtAEh-l3nQcGo8htcNU2CwPQ49wW7nRSu_vTBt_oh96rkm8zh6vRQy2mxrH5Ilr3B75zVI2O-anwiOhOnCxhhIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجار في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/naya_foriraq/91073" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91072">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سماع دوي انفجار في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/naya_foriraq/91072" target="_blank">📅 17:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91071">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed213b5b7.mp4?token=DqPV8Jz0Eg4bzxV3KiUWAqsbJkZO-CiCF05IRG03HC0jnxCGFjWC2oonEPsG-smKC7yDgGL2ituWYvImWZwd3H7aNDddDd2kqFBu68vLaJ3quhpbilBPU4f1D9mvE9XfJuspkAYCo9vNC2dBor98mhBSOeRwH1khR4UX2Kq2MCHrGkciLJou8cfdwuXimEaGAza4_eaE5BSir0PHNII4773RR4aXUVPpJy1ofeFnEeQnDir3ROjsMTlrZdLcLC232TddX8pohEkCaqbmAgC9v47RGKnjm2Jk06sToOLY-AUAxOg6Mku-KAwEsB3pkW9K4OLTD6Z0fP_uq40otFFh4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed213b5b7.mp4?token=DqPV8Jz0Eg4bzxV3KiUWAqsbJkZO-CiCF05IRG03HC0jnxCGFjWC2oonEPsG-smKC7yDgGL2ituWYvImWZwd3H7aNDddDd2kqFBu68vLaJ3quhpbilBPU4f1D9mvE9XfJuspkAYCo9vNC2dBor98mhBSOeRwH1khR4UX2Kq2MCHrGkciLJou8cfdwuXimEaGAza4_eaE5BSir0PHNII4773RR4aXUVPpJy1ofeFnEeQnDir3ROjsMTlrZdLcLC232TddX8pohEkCaqbmAgC9v47RGKnjm2Jk06sToOLY-AUAxOg6Mku-KAwEsB3pkW9K4OLTD6Z0fP_uq40otFFh4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب معلقا على تحذيرات السفارات في المنطقة: عطلة نهاية الأسبوع هذه لا تختلف عن أي عطلة نهاية أسبوع أخرى</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/naya_foriraq/91071" target="_blank">📅 17:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91070">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c67f0dda7.mp4?token=MFsNK16UJeqr8ToFSubb1aAq1BFYhP2pd-IYVxOy47P_goI5vnzXfn3sXdd_DAcP3fEQKkU5Albd62aflFt1ZMy7R7yfo512AiP-qvN0PQ1Uck2oLY9oHotxH0Nd5_LGGjqq_59-EeLRMu7GDOG_nB18W1xiaWOy8Y5UNpm4hsuhTqqtuDZ3lRk6z4zvYKXaG_nMjpa5W11B-xs_MBBiXwirQzVaghsyrVquTJf7k1jD1Npk8tNdMTw7l4-pqxPZDoORTogMhp61blfsnGrVs2CEYdg8_frpDnsQdQeWGWp79dMjbYERJdmcBWiFHCT9fDYw2zzkIjL-wd-DE9kmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c67f0dda7.mp4?token=MFsNK16UJeqr8ToFSubb1aAq1BFYhP2pd-IYVxOy47P_goI5vnzXfn3sXdd_DAcP3fEQKkU5Albd62aflFt1ZMy7R7yfo512AiP-qvN0PQ1Uck2oLY9oHotxH0Nd5_LGGjqq_59-EeLRMu7GDOG_nB18W1xiaWOy8Y5UNpm4hsuhTqqtuDZ3lRk6z4zvYKXaG_nMjpa5W11B-xs_MBBiXwirQzVaghsyrVquTJf7k1jD1Npk8tNdMTw7l4-pqxPZDoORTogMhp61blfsnGrVs2CEYdg8_frpDnsQdQeWGWp79dMjbYERJdmcBWiFHCT9fDYw2zzkIjL-wd-DE9kmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: ربما ساكون منفتحاً على الاجتماع مع الرئيس الإيراني مسعود بيزشكيان في الجمعية العامة للأمم المتحدة.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/naya_foriraq/91070" target="_blank">📅 17:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91069">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146653f4e0.mp4?token=TmYXFHqTtUYWWpFcqy3fmdOPk5fgFxTGyBD_ezRttWiopwLWxoAvKayXmsOCnv2yDiyd_hw0C0tBo4pk3lwEDwpCk6kYUiHius8-jgELKRyoGXbMjUcZaXgQuYmrihYBVyfsjybcRwQv8X9GoHkZyRrATU9vzkNgynyOuGmoLSiGh9N2ClCafdBj5cA4HnLoMFTz8ONGbZl7s3X-GiI3Mrl2Fz3-S4CQC0-AxOjq_Fa_3-Fc348V_66ocopVIWGJsWg5ChJkFl8XpIcFwOTM6nWcs74iS-GuEmM-JzOZ4l8rQNTNSd--DYU-4IHLmquSE7jajMln_5RqZwDJ1XfYTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146653f4e0.mp4?token=TmYXFHqTtUYWWpFcqy3fmdOPk5fgFxTGyBD_ezRttWiopwLWxoAvKayXmsOCnv2yDiyd_hw0C0tBo4pk3lwEDwpCk6kYUiHius8-jgELKRyoGXbMjUcZaXgQuYmrihYBVyfsjybcRwQv8X9GoHkZyRrATU9vzkNgynyOuGmoLSiGh9N2ClCafdBj5cA4HnLoMFTz8ONGbZl7s3X-GiI3Mrl2Fz3-S4CQC0-AxOjq_Fa_3-Fc348V_66ocopVIWGJsWg5ChJkFl8XpIcFwOTM6nWcs74iS-GuEmM-JzOZ4l8rQNTNSd--DYU-4IHLmquSE7jajMln_5RqZwDJ1XfYTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
ترامب: أنا في وضع اتخاذ القرار وأمور كبيرة جدا ستحدث في المستقبل القريب.. الخيارات الحالية على الطاولة هي محو إيران أو تركها تتعفن اقتصاديا أو التوصل إلى صفقة ومن الافضل ان يحسنوا التصرف.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/naya_foriraq/91069" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9962201aa8.mp4?token=koGCGcAMoLl0xIyiAQX_tABPE6JHIsVTwT7THmDN8X0h8Zklqp5d2-5lUVtvpBVjg2qpAo-WXyU0thR25wTlrDY9Z9rxXI4y1IUkp31eSDm_o8YFtsWxaF3QPdOeVMzTA36bpW4EDHaD0AvqPDjYEhb--jHG7XscjfHAJ9F0KRr6KKCimd9H5Q-symitA3sPoN8lh9TDop95b5NZ0mMH5fUCUpnEabDy8zCjmkiu68h1-n-7uLvYidMuKfRWBVh1RmbgK1uw3zwFcySNrBsjElNCkPieDAIiFFzEzUl-WGONLWrEgfkIbioSt_qPFArCGr64kskHK_koFk2GvyYq-bipQnG8fpbdyp2D5NOqhRNDXihxTCu0OaPDvvcppohbdnPyaF0u3lIZVmzg93sGVJgwV7tw7xd1iCkT6q-iWiRS5phUA8SGgEPmJaHhz7LBza3QOQU-5E7ASfOhmtHphIBghMsjkLHrAf77onG5faR6l4pfZ7DukidFbyxcQMOqEmg7gkY1ZrysYSAoudNhkrrz0loNud9qWQtn06Jo6N5xz-994sD4CkUjIoDBUpKwML_xCyeBXRJbmCq0ATkJyWYToDPUtFIGCgeroC1G4XXESD9iVBqnJbzqO-1xGtNoa4cVTPJkBuce5M_VfiBFdbsHnt2bhPVilj4uilV_S5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9962201aa8.mp4?token=koGCGcAMoLl0xIyiAQX_tABPE6JHIsVTwT7THmDN8X0h8Zklqp5d2-5lUVtvpBVjg2qpAo-WXyU0thR25wTlrDY9Z9rxXI4y1IUkp31eSDm_o8YFtsWxaF3QPdOeVMzTA36bpW4EDHaD0AvqPDjYEhb--jHG7XscjfHAJ9F0KRr6KKCimd9H5Q-symitA3sPoN8lh9TDop95b5NZ0mMH5fUCUpnEabDy8zCjmkiu68h1-n-7uLvYidMuKfRWBVh1RmbgK1uw3zwFcySNrBsjElNCkPieDAIiFFzEzUl-WGONLWrEgfkIbioSt_qPFArCGr64kskHK_koFk2GvyYq-bipQnG8fpbdyp2D5NOqhRNDXihxTCu0OaPDvvcppohbdnPyaF0u3lIZVmzg93sGVJgwV7tw7xd1iCkT6q-iWiRS5phUA8SGgEPmJaHhz7LBza3QOQU-5E7ASfOhmtHphIBghMsjkLHrAf77onG5faR6l4pfZ7DukidFbyxcQMOqEmg7gkY1ZrysYSAoudNhkrrz0loNud9qWQtn06Jo6N5xz-994sD4CkUjIoDBUpKwML_xCyeBXRJbmCq0ATkJyWYToDPUtFIGCgeroC1G4XXESD9iVBqnJbzqO-1xGtNoa4cVTPJkBuce5M_VfiBFdbsHnt2bhPVilj4uilV_S5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
ترامب:
أنا في وضع اتخاذ القرار وأمور كبيرة جدا ستحدث في المستقبل القريب.. الخيارات الحالية على الطاولة هي محو إيران أو تركها تتعفن اقتصاديا أو التوصل إلى صفقة ومن الافضل ان يحسنوا التصرف.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/naya_foriraq/91068" target="_blank">📅 17:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">إغلاق جميع البورصات الخليجية على انخفاض بعد هجمات انصار الله على السعودية</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/naya_foriraq/91067" target="_blank">📅 17:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حدث امني في منطقة الطارمية</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/naya_foriraq/91066" target="_blank">📅 17:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91064">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حدث امني في منطقة الطارمية</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/naya_foriraq/91064" target="_blank">📅 17:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91063">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">عدوان سعودي متواصل على المحافظات اليمنية</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/naya_foriraq/91063" target="_blank">📅 16:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91062">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5245333b1b.mp4?token=bvAMJDJrOZmDgDpX8J6_7_x5iVhxSUj_WFry-WVT7jsKPdAKoIyMAyxHMw1Wc0o0LJIhbV6UWMU7NrGTRwin_ELgdUAVO2Sr0sqi_eNWyQk2CKNGbvCy4G8FYdx_qtE7g_es2-X6jg5lYh4fZgisDBDGchr_OvMSfZpAICe103j8K2ivojAN2e61feZRhKiSotFFeW9LOqMbBULdXxwsxQPcvFnGx0xLMeF3Oydcy5acF8ZFtT-UqPC0rYGOWCgY2ZunNZIzf75HlFANPdmlILCvF0Z9UAZsEVa6CVGgNSPZNrOXz9vVBj0Nfdx_BG7dI4l7M-noZHnKtdVLQ1Yh_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5245333b1b.mp4?token=bvAMJDJrOZmDgDpX8J6_7_x5iVhxSUj_WFry-WVT7jsKPdAKoIyMAyxHMw1Wc0o0LJIhbV6UWMU7NrGTRwin_ELgdUAVO2Sr0sqi_eNWyQk2CKNGbvCy4G8FYdx_qtE7g_es2-X6jg5lYh4fZgisDBDGchr_OvMSfZpAICe103j8K2ivojAN2e61feZRhKiSotFFeW9LOqMbBULdXxwsxQPcvFnGx0xLMeF3Oydcy5acF8ZFtT-UqPC0rYGOWCgY2ZunNZIzf75HlFANPdmlILCvF0Z9UAZsEVa6CVGgNSPZNrOXz9vVBj0Nfdx_BG7dI4l7M-noZHnKtdVLQ1Yh_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران العدو السعودي يقوم باستهداف برج اتصالات رحوب بمحافظة الجوف</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/naya_foriraq/91062" target="_blank">📅 16:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91061">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
القوات الامنية العراقية تحبط محاولة لتهريب 700 ألف حبة من مادة الكبتاغون المخدرة وتلقي القبض على متهمين اثنين داخل الأراضي الكويتية.</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/naya_foriraq/91061" target="_blank">📅 16:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91060">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ac8dfc41.mp4?token=Uv--8NvsP-MGCtTb_ZICDBtFWP0cMOBwrxNJIIsYCKJGRCKdRgb44hTqOPia2pIahbaBZ8wtMbIv8anL7GGLPeXh4LGtzc5MLG3F5fkb0242wg73IogA-gg46Ssp7GB-D2kLQ4H1KB7rjZKuwjbNyhx3IO5Nk9bnLi1mIqC2U1dHWHcah94vRr0nscRDnXvU1QpWDe8u84OtnkZwu9Bfw2D4fLWOxqt43JKhTk2juRqiHSH_07qTaEBhj33mzEjYDrO9HspPdZxAH2XWT54SzOigH6LiQ2RSoXYKaCTmWYW799CJdgPt2yUMJaCa7egqUy964DUasbzh_xwJr5Lo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ac8dfc41.mp4?token=Uv--8NvsP-MGCtTb_ZICDBtFWP0cMOBwrxNJIIsYCKJGRCKdRgb44hTqOPia2pIahbaBZ8wtMbIv8anL7GGLPeXh4LGtzc5MLG3F5fkb0242wg73IogA-gg46Ssp7GB-D2kLQ4H1KB7rjZKuwjbNyhx3IO5Nk9bnLi1mIqC2U1dHWHcah94vRr0nscRDnXvU1QpWDe8u84OtnkZwu9Bfw2D4fLWOxqt43JKhTk2juRqiHSH_07qTaEBhj33mzEjYDrO9HspPdZxAH2XWT54SzOigH6LiQ2RSoXYKaCTmWYW799CJdgPt2yUMJaCa7egqUy964DUasbzh_xwJr5Lo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان سعودي يستهدف عدد من أبراج الاتصالات في مديريات الزاهر والعنان بالجوف</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/naya_foriraq/91060" target="_blank">📅 16:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91059">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wndl2QRzPfoPgIfrvqVW8VH0M8hNMsUd1IOnIpODfKTn_TLZsgvFo6Ep7XVUA3hAL9R69rHoO3LrWWp96B27rTxmtMNe9HeZ8rw8ASKCWudj2lFEJ4kJhsBhQQo5jHp5nkjO0gqnZrdpqjYzoxbgDL5xVXCGZ938jmfaQxjZrlpVPdQvEZGzKnzjEXHiLVPyU2vuhCIgQrXQEta7xZGmEYHK07Xp_GEXdHqwFpEfoSYb8qP2R5zCUmJKGg8CG8KkJZ8GvGH2Dh5PifduyKWw0RBmcMJp5sUZQrzzS0iVgns5ijUG9QP7WfLDV2sfAnyhxlxmJrbx75cRvUeFFTZsbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسم القتيل: نتنئيل شكرون هو القتيل في عملية إطلاق النار في نيفيه تسوف</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/91059" target="_blank">📅 16:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91058">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9093761133.mp4?token=LlfIPilBeik8j61t9r8Msi8_kpEoROzN0-EY5laiTfdH-Zo6-xBkJU32s996lYj7ZjEPNtZ4BskDVwpVO7U8FSoPi0S2RE6_IqQbMLyeJXmecX5JNvyWasdrV09ytibSSENegzN2-LexQz8uXP8AEYNYPmv6aH49CEn4Rj2YD8Ve6K2Nb1ADdv9rhb2xWS6YC_y_qnJ89NAN3M5gfxG_4EtptrKRV4iD051U_Ia3eU1QhIma5bXgvFq5OWpcJiHpdmWV1QMDRjL_Lm7e17cfM1yv9UVUlmOissEwGF9BbiXmR6LWRSwQGqOiKPKnRd_EevLPPYU8RFhJ0OogplahlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9093761133.mp4?token=LlfIPilBeik8j61t9r8Msi8_kpEoROzN0-EY5laiTfdH-Zo6-xBkJU32s996lYj7ZjEPNtZ4BskDVwpVO7U8FSoPi0S2RE6_IqQbMLyeJXmecX5JNvyWasdrV09ytibSSENegzN2-LexQz8uXP8AEYNYPmv6aH49CEn4Rj2YD8Ve6K2Nb1ADdv9rhb2xWS6YC_y_qnJ89NAN3M5gfxG_4EtptrKRV4iD051U_Ia3eU1QhIma5bXgvFq5OWpcJiHpdmWV1QMDRjL_Lm7e17cfM1yv9UVUlmOissEwGF9BbiXmR6LWRSwQGqOiKPKnRd_EevLPPYU8RFhJ0OogplahlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان سعودي يستهدف عدد من أبراج الاتصالات في مديريات الزاهر والعنان بالجوف</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/naya_foriraq/91058" target="_blank">📅 16:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91057">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تصاعد حدة الاشتباكات بين القوات المسلحة اليمنية ومرتزقة السعودية في تعز</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91057" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91056">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
ترامب: بناءً على طلب قوي من الجيش الأمريكي ولأمن البلاد، الموافقة على تحويل قوس النصر إلى مجمع عسكري عالي المستوى. سيتم تجهيز المجمع العسكري لاستيعاب وتخزين ونشر عدد كبير من الطائرات بدون طيار، وقناصين على الأسطح والساحات، وتخزين كميات كبيرة من ذخيرة القناصة</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91056" target="_blank">📅 15:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91055">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/md4UNB721eUFnyt6WgH6h0JwB5ZoEpficNA3s4ojsE7VzU27kaJuob98aw_g0p2T3H2ONyALU-1KwipfZoIX5ztlM7ulLKElt99FatUnk-FeFvGy_8bQHtdqD7EG1DHXHjXyRg-IXZb-wj4T7KD1X1VDq-Uj8CE-GaeQ0GGV9yZ1AbqJiHhrH6OptKTmMzXQhJv1PG-cyxqU1xiIg0CRWhkGx9oZ-lBZgGYDkkRpJ2KMP7MSKayfaMPZ_R4nbsyBxeF-MqMIEaIw8pUYh6nNiP0tVUSM_X9TZR_P1QCyJTDOljroBd6W-m2eONP9Lw81hGZGDqg5ATbbzqm9Qntt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن غفير: حق المستوطنين في الحياة اهم من حق الفلسطينيين في التنقل على الطرق بالضفة. آمل أن تصل قوات الأمن، عاجلا أم آجلا، إلى منفذ العملية، وإذا لم تغتاله، فمكانه حبل المشنقة، وفقا لقانون الإعدام.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91055" target="_blank">📅 14:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91054">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91054" target="_blank">📅 14:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91053">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
محافظة الانبار غربي العراق تعلن الحصول على موافقة لإيقاف الإجراءات المتعلقة باسترداد الأموال من ذوي الارهابيين الذي تم تسجيلهم كشهداء</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91053" target="_blank">📅 14:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91052">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اسم القتيل: نتنئيل شكرون هو القتيل في عملية إطلاق النار في نيفيه تسوف</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91052" target="_blank">📅 14:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91051">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
تحذير مقر خاتم الأنبياء المركزي إلى الولايات المتحدة ودول المنطقة:
بناءً على المعلومات الواردة، فإن الولايات المتحدة الإجرامية وفي محاولة للتغطية على إخفاقاتها وتحقيق مكاسب وهمية في الحرب التي بدأت بالاعتماد على الأكاذيب والمشاهد المفبركة الإسرائيلية واستمرت بالخداع والمراوغة، قررت مرة أخرى، وبضوء أخضر من بعض دول المنطقة، استئناف إجراءات ضد الجمهورية الإسلامية الإيرانية خلال اجتماع مشترك في إحدى الدول الأوروبية.
نحذر من أنه إذا ارتكبت الولايات المتحدة أي خطأ ضد الجمهورية الإسلامية الإيرانية، فإن جميع مراكز تمركزها ومصالحها في المنطقة ستتعرض، من دون أي قيود أو اعتبارات، لهجمات مستمرة وفعالة ومؤلمة.
ونحذر من أنه إذا انسجمت دول المنطقة، من خلال استمرار سياستها المزدوجة تجاه الجمهورية الإسلامية الإيرانية، مع «الشيطان الأكبر» في عدوانه على إيران الإسلامية والقوية، فسيُعتبر الجميع شركاء في هذا العمل العدائي، ولن يكون بإمكانهم بعد ذلك انتظار ضبط النفس أو التسامح من القوات المسلحة الإيرانية القوية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91051" target="_blank">📅 13:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91050">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
اعلام العدو: تلقت منظومة الأمن مخاوف من حدوث هجوم على أحد دور العبادة اليهودية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91050" target="_blank">📅 13:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91049">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله أكبر
🇵🇸
🇮🇱
مقتل صهيوني وإصابة آخرين جراء عملية إطلاق النار في الضفة الغربية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91049" target="_blank">📅 13:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91048">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af57537bb.mp4?token=c4XNK5qTVotcgciICkh8UBjzVjUOBn0cd-0ZmUaMiSHyo3SjpDhxQQPBAJT1VuNh3_3j1_bvMryS55Dz2hwWCXanfMD_wTXadEmFGgPkvtgsOIgOhQIOjrgl7eiZGwKE3N7gpF0THuuMLcB4Zg3nxuFTt13WGxWdCgjprFQTWQgjiAd1LGycJeqamkEnRDH9j0J1EeG__fRKmEP3xtQI8InlL3R8iZ32Ug-yqWLCvm6oh3SzKppSWrWggrn0V_-l94Yhfd41dq3jgAEyH4mZ4X3vtAXyo0aGVq8t5snYQp2BARNsOP3_ZbHDdY90vL4-zFmb1qLaNAK0lq_YBFEmRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af57537bb.mp4?token=c4XNK5qTVotcgciICkh8UBjzVjUOBn0cd-0ZmUaMiSHyo3SjpDhxQQPBAJT1VuNh3_3j1_bvMryS55Dz2hwWCXanfMD_wTXadEmFGgPkvtgsOIgOhQIOjrgl7eiZGwKE3N7gpF0THuuMLcB4Zg3nxuFTt13WGxWdCgjprFQTWQgjiAd1LGycJeqamkEnRDH9j0J1EeG__fRKmEP3xtQI8InlL3R8iZ32Ug-yqWLCvm6oh3SzKppSWrWggrn0V_-l94Yhfd41dq3jgAEyH4mZ4X3vtAXyo0aGVq8t5snYQp2BARNsOP3_ZbHDdY90vL4-zFmb1qLaNAK0lq_YBFEmRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مسير يحلق في اجواء جرف النصر (مدينة النصر) ضمن محافظة بابل العراقية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91048" target="_blank">📅 13:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91047">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇵🇸
🇮🇱
توثيق لعملية إطلاق النار التي طالت عدد من الصهاينة في الضفة الغربية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91047" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91046">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTAQX6zTQTUJVqsqE-X4iI6C5bg7je2NotlugLZTOZ0JOI9c0R4-9lckqd9sm3IO-zfOlUpi3nb8yt2OV5trsoUlM03eDRXHqF_ydNPcYLGc8UYIqcB3AdkgW-3iEoIG0sIHNwaoPeKTmykoFzFO6o7MvP1AR0jAcgyHwclU-q0XKt6kuoHYA1qb4hB4URr8R4mGHlWURIJPfH9BaKGR-Cuf_6_W_O5ZHUBIsQKwScXbR-SFniYqGZ-8Nxmj-oWW-TOwWig4MCliIRSlCzlcCj0fzT7J1xQN0v6Rh4Yk4BzNv4dp_HxWF2QkSpJepDLfaRGjW0cbz4otED3Zovb8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
خلال عملية أمنية لقوات الأمن..
مقتل وإعتقال عدد من العناصر الإرهابية في 3 محافظات إيرانية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91046" target="_blank">📅 13:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91045">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
نائب في البرلمان الإيراني:
تم تقديمه إلى هيئة الرئاسة في مجلس النواب مشروع قانون عاجل بشأن الانسحاب من معاهدة منع انتشار الأسلحة النووية (NPT).
بالنظر إلى الظروف التي تمر بها البلاد والهجمات التي تعرضت لها من قبل العدو في مرحلتين، فإن بقائنا في معاهدة NPT لا يجلب لنا سوى الضرر.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91045" target="_blank">📅 13:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91044">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇵🇸
🇮🇱
توثيق لعملية إطلاق النار التي طالت عدد من الصهاينة في الضفة الغربية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91044" target="_blank">📅 13:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91043">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0828525c.mp4?token=Pb40PT6JhR1GIJ2jbuGtXK-9EB9VX4g_E1t1qjynNENodREeJhbhpmGfjNH5hYeDm7PHREHCQVyGHpYulby-0erpzuTpejH4j2lza2YXZkUeQPooBQz7utmFH-cLEc5Qh6z3WW4j6Ff0zMGtcR2eNiG3Fy7nGjx5U5_c6xih4g5r2Qz7SYSTKuYUHJ2qzxIHnxUwY78FQXUmZaxeMQEd4ACp6jxD5Bm8DYzj7wUkVEaiiJlletdubZ7dSPM03aMRkhd0q2R5D85N0X0s2yjEi5cbeYRsAoIa98aUlUmcfcO17iD-HasV1B4r1TzDulHd3N1kXIYJwUMWYtMLSsDiwAxvraeUCGKGQ2RRW6uadvwB3x7NItPzjiu8a-t1ObdFcrw5qlEdcgYxNCo0bjbBWYgu5h3T-cqPTEu1gMN8aYSBsmHIVVhrmJlxkgeY5QvA5hKWFgYepj1cbU0Jvv_5CwnabzOVSKQBmLnq7PK79Pq7WlFnRvn5y49aXsRYQmU-aeftu-DiCuxP6bHISzxF15wVzNPer1jpR5J3Wrj8e6x8evSkUtrhaGMeuYiUQixcj3Wp0etgisOS3WyJn2iu1t_o9ambSHdw7pg-JAGfg0IpYI51YKy9ReQBEkcu5hyBy8Psf_kuWItrvgP2B9oVotmXLLyX2vMVIo0CHb_JPCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0828525c.mp4?token=Pb40PT6JhR1GIJ2jbuGtXK-9EB9VX4g_E1t1qjynNENodREeJhbhpmGfjNH5hYeDm7PHREHCQVyGHpYulby-0erpzuTpejH4j2lza2YXZkUeQPooBQz7utmFH-cLEc5Qh6z3WW4j6Ff0zMGtcR2eNiG3Fy7nGjx5U5_c6xih4g5r2Qz7SYSTKuYUHJ2qzxIHnxUwY78FQXUmZaxeMQEd4ACp6jxD5Bm8DYzj7wUkVEaiiJlletdubZ7dSPM03aMRkhd0q2R5D85N0X0s2yjEi5cbeYRsAoIa98aUlUmcfcO17iD-HasV1B4r1TzDulHd3N1kXIYJwUMWYtMLSsDiwAxvraeUCGKGQ2RRW6uadvwB3x7NItPzjiu8a-t1ObdFcrw5qlEdcgYxNCo0bjbBWYgu5h3T-cqPTEu1gMN8aYSBsmHIVVhrmJlxkgeY5QvA5hKWFgYepj1cbU0Jvv_5CwnabzOVSKQBmLnq7PK79Pq7WlFnRvn5y49aXsRYQmU-aeftu-DiCuxP6bHISzxF15wVzNPer1jpR5J3Wrj8e6x8evSkUtrhaGMeuYiUQixcj3Wp0etgisOS3WyJn2iu1t_o9ambSHdw7pg-JAGfg0IpYI51YKy9ReQBEkcu5hyBy8Psf_kuWItrvgP2B9oVotmXLLyX2vMVIo0CHb_JPCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
عملية إطلاق نار في مستوطنة نيفي تسوف بفلسطين المحتلة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91043" target="_blank">📅 13:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91042">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5c5d0fb8.mp4?token=a4GkZC5WqXDi9zordkY2c_ntm8aaWgCKBWi0_pZfvIwEQGc7t9cb5o4RBqOLd4PlyBsVxXFhwHBJh_z-hMYkecI0NnfIe4okur5jYftsk_ce1ZsxEDqYLWS7aHr_qV38APMCSw3GUn7knWWMaba_RyQ1WqB6FE-GxKbiEGnIfjmv4-VGqKKcDdtCQYSVeMkxjWUBp9avJ0cytQe3jEMr6BsHrTcw_VltF9yVW99zVN03WSQtDmVQMp5Jj9vTWkLicUiC6gsxUDz7bilKRficJpUo7cPnRH86gIoqW3FmCoQorDEs-JER7eVBQWQxW1TYwRHuFSesmiFik01D0VI6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5c5d0fb8.mp4?token=a4GkZC5WqXDi9zordkY2c_ntm8aaWgCKBWi0_pZfvIwEQGc7t9cb5o4RBqOLd4PlyBsVxXFhwHBJh_z-hMYkecI0NnfIe4okur5jYftsk_ce1ZsxEDqYLWS7aHr_qV38APMCSw3GUn7knWWMaba_RyQ1WqB6FE-GxKbiEGnIfjmv4-VGqKKcDdtCQYSVeMkxjWUBp9avJ0cytQe3jEMr6BsHrTcw_VltF9yVW99zVN03WSQtDmVQMp5Jj9vTWkLicUiC6gsxUDz7bilKRficJpUo7cPnRH86gIoqW3FmCoQorDEs-JER7eVBQWQxW1TYwRHuFSesmiFik01D0VI6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
سقوط اصابات خطيرة بصفوف الصهاينة والمنفذ تمكن من الهروب وترك مكان العملية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91042" target="_blank">📅 12:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91041">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇱
عملية إطلاق نار في مستوطنة نيفي تسوف بفلسطين المحتلة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91041" target="_blank">📅 12:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91040">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇱
عملية إطلاق نار في مستوطنة نيفي تسوف بفلسطين المحتلة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91040" target="_blank">📅 12:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91039">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
القوات الأمنية الإيرانية تتمكن اكتشاف شحنة أسلحة مهربة في مدينة مريوان بمحافظة كردستان عند الحدود العراقية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91039" target="_blank">📅 11:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91038">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔻
خروج محطة التحويل الرئيسية الدوحة (C) عن الخدمة وإنقطاع الكهرباء في منطقة القيروان بالكويت لأسباب مجهولة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/91038" target="_blank">📅 11:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91037">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553d2a057a.mp4?token=jcYNJurq7mlhSboYJmt91c1HgiUrgqPnTkmx-LXgF0G2eI5e0GJCUFyIERqAKa3J-cRB64ADMPJ5cf6QjKbKVFzA2cG1l6OSNINE547L_crC_sC4fn8dsaRl64rJ0a88VpKR9eSC5vxmrPnZc8kOZr0HWCsvlIm9K_X4JsIEzwVYSx9JUk8yc1f0w_3dpH8nFEmlms8Duzwvhn776M5xY9Ao8EMJu1gqAgKGta5uOKS0hUll-yNoufTzvI60BWxxQtyNsEnxxGuS95X7O4E_EhAComIsUkAJjtdRO1bTM9VFZqOjZZmQw5zqZ48oubtwCD1UdD_ZpTjJZCDpt_d_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553d2a057a.mp4?token=jcYNJurq7mlhSboYJmt91c1HgiUrgqPnTkmx-LXgF0G2eI5e0GJCUFyIERqAKa3J-cRB64ADMPJ5cf6QjKbKVFzA2cG1l6OSNINE547L_crC_sC4fn8dsaRl64rJ0a88VpKR9eSC5vxmrPnZc8kOZr0HWCsvlIm9K_X4JsIEzwVYSx9JUk8yc1f0w_3dpH8nFEmlms8Duzwvhn776M5xY9Ao8EMJu1gqAgKGta5uOKS0hUll-yNoufTzvI60BWxxQtyNsEnxxGuS95X7O4E_EhAComIsUkAJjtdRO1bTM9VFZqOjZZmQw5zqZ48oubtwCD1UdD_ZpTjJZCDpt_d_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمد باقر قاليباف:
لن يتم فتح مضيق هرمز إلا بعد تحقيق شروط إيران.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/91037" target="_blank">📅 09:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91036">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee2088fd1.mp4?token=SwHe6PC_p5FweqQq-CdEgyZWkWsRD-rbD-jPvC8PE3pJXEmxDhtilxyAxNnNKw9QEWGYr1p_DUXU7K_RAQGJH_djNb-l33OdxBGZBK3LRNmuVIz6IH6ucQCgq-6GLIb6CZBTh4sie9-ItHUR0hcKROA0h2ySA5_J7XmDPciIa055oM0DwfjCTKO4UfFgRC-TJKPOt_ILNDSq5Qcj4eCjALtUgqgzF-mZ7iZCtYbBTfB2QKjIR2dtab7Drhh70A8RO7zPN7Uf2ee13hn6gpRysqc3oBheadl1n9PkvaMVsO2wFXYJHSOm9HJcmysf2fb1Ev7mfoj4Hl1Xe-SCoHGr4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee2088fd1.mp4?token=SwHe6PC_p5FweqQq-CdEgyZWkWsRD-rbD-jPvC8PE3pJXEmxDhtilxyAxNnNKw9QEWGYr1p_DUXU7K_RAQGJH_djNb-l33OdxBGZBK3LRNmuVIz6IH6ucQCgq-6GLIb6CZBTh4sie9-ItHUR0hcKROA0h2ySA5_J7XmDPciIa055oM0DwfjCTKO4UfFgRC-TJKPOt_ILNDSq5Qcj4eCjALtUgqgzF-mZ7iZCtYbBTfB2QKjIR2dtab7Drhh70A8RO7zPN7Uf2ee13hn6gpRysqc3oBheadl1n9PkvaMVsO2wFXYJHSOm9HJcmysf2fb1Ev7mfoj4Hl1Xe-SCoHGr4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
انباء متداولة عن تفعيل الدفاعات الجوية في قاعدة خراب جير بالحسكة السورية.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/91036" target="_blank">📅 03:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91035">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
مصدر امني لنايا   التنبيهات للسفارات الأمريكية والأجنبية يأتي بسبب مخاوف من نية تنسيق هجوم مشترك بين أنصار الله وجبهات المقاومة الأخرى بالهجوم البري على السعودية .</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/naya_foriraq/91035" target="_blank">📅 01:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91034">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انتخابات كنيست في " اسرائيل " فلسطين المحتلة
خطاب لترامب في الجمعية العامة للأمم المتحدة
هل سوف نشهد جولة جديدة مع ايران ؟!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/naya_foriraq/91034" target="_blank">📅 01:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91032">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc4py_TtCB0f9rxafpGYpuCMdLZOrxoTMAix7a55sSep_xJQLM8BrQiesasTmNUBNtD8tSyrekpfV-XT76AVrSMnJJZxEfUiuCq7Z_ejKkZ0NdWgLDAjl1KXnIPzHNh5kb8CyTpqwLi4wDzA2leQ6dHpV3m0D9saPPZS9R9cT-gMrn7n17vZcVefeBAsNPlbBYzuxV7DGTAkrRqEAANuJB9k-AGMuAYDEgFObjJxpNzT7DjCF-AgLvkXwfqH1aOTY-0OveaaHl61f7n4m6RIngovbAJwhLnOtwvb2t4GNzIwmCll7raADyImAlqnFpz957dddNf7wkcxLnnQK7rb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
USA situation in Middle East now</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/naya_foriraq/91032" target="_blank">📅 01:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91031">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
التحذيرات وصلت لكل السفارات الأمريكية في الشرق الأوسط كما وصلت تحذيرات لكل السفارات الأجنبية في السعودية مماثلة عن تطور الأحداث في العمق السعودي</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/91031" target="_blank">📅 01:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91030">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">السفارة الأمريكية في بغداد تحذر رعاياها من إمكانية إلغاء الرحلات الجوية وتوخي الحذر والحيطة</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/91030" target="_blank">📅 01:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91028">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
مصدر امني لنايا
التنبيهات للسفارات الأمريكية والأجنبية يأتي بسبب مخاوف من نية تنسيق هجوم مشترك بين أنصار الله وجبهات المقاومة الأخرى بالهجوم البري على السعودية .</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/91028" target="_blank">📅 01:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91027">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U26WA20ZRfdsEicuijj6bBssJC4qvdYuf65CSaxZGDX708KAS0aDag_pS3t3Vj8L77bzvm8T--XjHVs9nXkZWDiw3x1ljggtPceuJcyidO1MHRNff3hW160Ca6l6hL6wfr2OTwGpyYHZjHmKiwVwmFs7aq7I4Oc1jjbOQcAZzrVFSkLBXDAlA55V-aKy5eEOBmSkmc6Rbmw56lvI-8_cruIArv9exPdh0e5hMIlLBBjtxdDVm2ksLBLe5XFN6bFjsVuU60OubyrMVtu2lkudaOGR3x_HzgnG1k5loXAViuC3-ExzcqEUg-osccoMRg9C1brl9LXViUcPkWjN8e4IJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السفارة الأمريكية في بغداد تحذر رعاياها من إمكانية إلغاء الرحلات الجوية وتوخي الحذر والحيطة</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/91027" target="_blank">📅 01:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91026">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huTDRkbG_JyunyqMNHXDKCHD3ycfNgUuGiRgy_O83KIZLuWpzYo4BOLizcjEuTvpU_SkmjhtlccIjmpb-1TtF1UJxdcXBabrjCQ4p4ie9LfQ_N9DQIv2n68xRxnl6MRKaAgYv7xQoEulh-_QnTrpNGcuRYHADhk7wbA8z0IsoqlsmCL1uB-VdEEr080kPgqfy-zjSaHOJOcuF1Hl3FwGdUw_0Qh0d3DMxiA-osLoTVXBXlErfJQv93rtC8xx18zI19REjQR_h1AumOXIRNXzjmvjjjCTUyMkcgx5NptCY-2w29wW-agVx5afUzeVx5wUEc-WKtnVtcdAQGAI33Gsgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف الحركة الجوية في مطار الطائف السعودي</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/91026" target="_blank">📅 01:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91025">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات عنيفة تهز سماء مدينة الطائف السعودية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91025" target="_blank">📅 01:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91024">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">السفارة الأمريكية في بيروت تدعو رعايا لتوخي الحذر !</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/91024" target="_blank">📅 01:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91023">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارات عنيفة تهز سماء مدينة الطائف السعودية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91023" target="_blank">📅 01:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91022">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات عنيفة تهز سماء مدينة الطائف السعودية</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91022" target="_blank">📅 01:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91021">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91021" target="_blank">📅 01:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91020">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUcKTUpnxBHkbzJLvXicaAg1yCHY6ywzQweZTCPzu0D71d3_7RTaSEgl2rw90lLkd6ij0PQiIA9yStPFYPh2K8ujwhFhOMBn62g6N7vs-gNT0qdD4w2NgHgnhmuCRBXk3INgjEJqjjNVswIu2_PsO64lATqN_y0f_hhhQ49isKdl2AGBnmSY5D616RaGgBQ4KQ4LRWR7UejNQCIziN0ELGfh5ymu9dc9Ha12qM2PLy2QhQRvcMdEfsuZlrRplpyX1PxVQagfLtqbcQaqBAX3CVWVizEjJbvj-_AKhUTBsR2mLnUHusDbCazzAmdxXawTD1btwn5Ajt1ZEarfhuDjrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إيطاليا تحذر رعاياها في السعودية بعدم التقرب على المنشاءات العسكرية السعودية
لا تسافروا إلى جازان خميس مشيط ونجران</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91020" target="_blank">📅 01:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91019">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏أصدرت السفارة الأمريكية في مسقط تنبيهاً أمنياً عاجلاً للأمريكيين المقيمين في سلطنة عُمان، تحثهم فيه على توخي مزيد من الحذر في ظل التوترات المستمرة في الشرق الأوسط. وتنصح السفارة الأمريكيين بالبقاء متيقظين والاستعداد لاحتمال إلغاء الرحلات الجوية، وإغلاق المجال…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91019" target="_blank">📅 00:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91018">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏أصدرت السفارة الأمريكية في مسقط تنبيهاً أمنياً عاجلاً للأمريكيين المقيمين في سلطنة عُمان، تحثهم فيه على توخي مزيد من الحذر في ظل التوترات المستمرة في الشرق الأوسط. وتنصح السفارة الأمريكيين بالبقاء متيقظين والاستعداد لاحتمال إلغاء الرحلات الجوية، وإغلاق المجال الجوي، واضطرابات السفر.
‏يأتي هذا التحذير بعد ساعات من إصدار السفارة الأمريكية في إسرائيل تحذيراً أمنياً مماثلاً للأمريكيين الموجودين في البلاد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91018" target="_blank">📅 00:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91017">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
🔻
🇮🇱
محسن رضائي عن علي الطاهر: تم إخلاؤه مسبقًا ولم يكون أحدا فيه كما تم إخلاؤه من المعدات أصلا</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91017" target="_blank">📅 00:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91016">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇸🇦
🇾🇪
‏
التحالف السعودي يعترف بتعرض الرياض بصواريخ
القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/91016" target="_blank">📅 23:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91015">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6CtzWdZ_WXUIciXTqcUZdFiUTGnzLdx-opJ22rtSbYyTzmHsn7S8CY-NXmr4QqzUL9SJf5wr2_sOZ1ncRNmBUZaZ_l4npLDEhfKQPnJAm_tviGVrzei8f_1tjraxiCei48OIUZ_lIdWnCJUCipzvAYR9zAQZ8vhfjCQ47GYa7eHN0t--3qXt9MaQVzyMuvsGjTNAuJgJboZoC7TVLBFUeHrJKrnPJQ4HM3piXhF1kKGBucJRzuqzj5a0vjGdN5HpprpV_BwA72viEncL5hbNCt8oYGqsFyAlTQiuatVqi3LmfyrHrLsQ5L1DgItiOnP1wCF5PITPMaiDZC0odayZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفذت القوات المسلحة اليمنية عمليتين عسكريتين نوعيتين بعدد كبير من الصواريخ الباليستية والمجنحة والطائرات المسيرة
- الأولى استهدفت أهدافاً حساسة في عاصمة العدو السعودي الرياض
- الثانية استهدفت شركة أرامكو في ينبع</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/91015" target="_blank">📅 22:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇹🇷
‏
وزير الخارجية التركي:
تم تقديم مقترحات إلى جميع الأطراف لإنهاء القتال السعودي الحوثي ...</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/91014" target="_blank">📅 21:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91013">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e6c9d1b7.mp4?token=RdluNoVV8FIKL6c_jItcKi4XrLYOeN9BZoBDU3hj-Ck-IOoZyXgv_GYcVXuwdjJEYuCrxL4JoW20cooFuR6woFc29StUltNEJiLO9MEYr3nA7Sh8DEMJJSr38QWNPx5SKJUJzXR9JSTImqOBzWVOsqJWHBEqJq_sn1qwISp0Z00utN43ZXK82ZR-kqALJE6No6u5q60QjK1gcqtcXpQqYEonuJ3o0ITObiqN38CedhAtba8ca7GZvfDH_zfM4n4VKPctm-6BTT-senvE466l8xBD9qflyAoiL9BGyWiQOZHeb4Z2tRgnKRGoLXK9JZr8ju9Skbywuw0c1IXTDXARsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e6c9d1b7.mp4?token=RdluNoVV8FIKL6c_jItcKi4XrLYOeN9BZoBDU3hj-Ck-IOoZyXgv_GYcVXuwdjJEYuCrxL4JoW20cooFuR6woFc29StUltNEJiLO9MEYr3nA7Sh8DEMJJSr38QWNPx5SKJUJzXR9JSTImqOBzWVOsqJWHBEqJq_sn1qwISp0Z00utN43ZXK82ZR-kqALJE6No6u5q60QjK1gcqtcXpQqYEonuJ3o0ITObiqN38CedhAtba8ca7GZvfDH_zfM4n4VKPctm-6BTT-senvE466l8xBD9qflyAoiL9BGyWiQOZHeb4Z2tRgnKRGoLXK9JZr8ju9Skbywuw0c1IXTDXARsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية بشأن استهداف أهدافاً حساسة في عاصمة العدو السعودي الرياض واستهداف شركة أرامكو في ينبع بعدد كبير من الصواريخ الباليستية والمجنحة والطائرات المسيرة - 19 سبتمبر 2026م بيان صادرٌ عن القواتِ المسلحة اليمنيةِ  بسمِ اللهِ الرحمنِ الرحيمِ…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/91013" target="_blank">📅 21:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91012">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇾🇪
سماع دوي انفجار في محافظة عمران اليمنية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91012" target="_blank">📅 21:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91011">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
المتحدث الرسمي باسم القوات المسلحة الايرانية:
إن إسقاطات قائد القيادة المركزية الأمريكية وادعاءاته الكاذبة والسخيفة بشأن مرافقة ناقلات النفط وسحب مليار برميل من النفط في الشهرين الماضيين ليست مجرد حقيقة، بل هي عملية نفسية فاشلة لرفع معنويات القوات المنهكة والمتعبة للجيش الإرهابي الأمريكي في المنطقة، ولتبرير التكاليف المالية والبشرية الباهظة للولايات المتحدة في المنطقة، ولن تغير هذه العملية حقيقة انسحاب جيش ذلك البلد المعتدي من المنطقة.
لا تزال زمام المبادرة في مضيق هرمز في أيدي القوات المسلحة الإيرانية القوية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/91011" target="_blank">📅 20:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91010">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtttE6eWC7uFBaIOFWxTmimIc2R7N6iCrbqYKhI7NS9TqkhEJytncdNc93HULoXakYgfVSOJ3r1BBrJHfD06DuUhZnEL4_izny2HsnKyvi3uwgdVloCt762aDdM7yXxiQJBDDTGTnHX4ZmSfI_8MtOZeDzsG1E4TrGwR7UrC5olcxiSjZWkdxFkhXzlZWfo8DvyXnuhmkm8A5F1q3usAbBeoew4ii5Y7lLyWkRPQ07vdqpvAnXmL8Gb5qLXOgPejM0NNdqXSTSiOt97etmF3zNuDXVftIEsckUnEGZ5c-z8qR1SRRlW_MVBYQ-awTsAuu5a66ua8k9f7R8cj1afXPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: أنا بصدد تشكيل "قوة الذكاء الاصطناعي"، على غرار "قوة الفضاء" التي حققت نجاحاً هائلاً خلال ولايتي الأولى.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/91010" target="_blank">📅 20:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91009">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91009" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91009" target="_blank">📅 20:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91008">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇾🇪
‏بيان مهم للقوات المسلحة اليمنية للإعلان عن عمليات عسكرية واسعة في العمق السعودي،  في تمام الساعة الثامنة مساءً.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91008" target="_blank">📅 20:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91007">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
الخارجية الايرانية:
من الظلم للشعوب أن تقوم بعض الشخصيات الإعلامية بتحميل إيران مسؤولية انهيار التفاهم.
نحن نتحدث عن الولايات المتحدة؛ وهي دولة دأبت مراراً وتكراراً على التنصل من التزاماتها على مر السنين.
إن لوم الذات يُعد إحدى سمات الحرب الإدراكية التي يشنها العدو؛ فهناك حقائق واضحة لدرجة أنها لا تحتاج إلى تفسير.
ستركز زيارة وزير الداخلية الباكستاني على العلاقات الثنائية بين إيران وباكستان؛ ولا توجد خطط لتبادل رسائل محددة تتعلق بالوساطة.إيران وعُمان توصّلتا إلى تفاهم بشأن تحديد مسار آمن لحركة الملاحة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/91007" target="_blank">📅 20:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91006">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
ضبط 200 كيلوجرام من لحم الخنزير خلال مداهمة مطعم في محافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/91006" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91005">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇱
صافرات الانذار في المستوطنات قرب الضفة الغربية بفلسطين المحتلة خشية تسلل مقاوميين.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/91005" target="_blank">📅 19:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91004">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gujV-lfnpcYSXebrGrlM4GaXQa_We-It7W8WBrKyQBZp2FAEr6Rnjw-Hr5zH_oCrtxqBUapdg92Qje-nyfFdM_mCpvTYzxheLVVkXZSRYra5b5JtXVWVuHhfeBX5HNuq25s522kiKITR0nSvFwCHvYPl9q7quf6J27cLpz7roXaqPGO-_PF-Qq7xsba1pxGwqX_Ig37CFi1RFSuDj5bQjrNWl29kcqI_-H8M_IiBgL5Ab6gGTImUm6Vf9WNA-Thib4Qc5cyMABZiPxfLSaSZ_ohaNfDCX73sSPgmR1a_fbH7Ukoj0zywnU9Iw0vsQB3wBD6JGyVvsritNgl8RSrODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
عرض عسكري سعودي في سماء جدة.
جدة تستعرض والرياض وجيزان وابها وخميس مشيط تقصف
😆</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/91004" target="_blank">📅 19:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91003">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
‏بيان مهم للقوات المسلحة اليمنية للإعلان عن عمليات عسكرية واسعة في العمق السعودي،  في تمام الساعة الثامنة مساءً.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91003" target="_blank">📅 19:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91002">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYBW_Tf5RKpvCEgM2ZZxLoXmqDgNX9u59tGG2QJksqWB22MtS4UOzMrwKe1bOH7lNRbO0ED5gV3KiGrfwBjFzMMSo0o3zI0ohDrFz3nhHrJe95ZUIucbB6KxJ_nLmGXyMQ040Wq3YqV8vgfqVVHYZCdp0t293bpfniCtZ0m8ih1KjvLaF2QC7jVcbc0MyQHttPfVIdFTm5yWXau8qqKxGnNkzFp16tur0PFB0tsk_3YtSJNAuFBQsN6H-s57uQoSTXBwpYM6PR9ael3OSGfzsPk6cNoBZekwBUp8M-OwrovR77MXEKV9aMOzCoEsbkkYz-BvXK5p91zGLadYswX4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
يبحث ترامب عن اسم جديد للذكاء الاصطناعي.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91002" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91001">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
رضائي:
من صالح واشنطن القبول بشروطنا للخروج من الحرب وتهديدات ترمب لن تحقق أي نتيجة ومستعدون لحرب حاسمة، يجب إنهاء الحرب على جميع الجبهات، وفك تجميد الأموال الإيرانية، ورفع الحصار البحري.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91001" target="_blank">📅 18:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91000">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48bd90ce61.mp4?token=BUSrj9KK13K7NtEhssxr2UvASo7_34n6vp8kfLkQeSXaj-lM8cpogLMDl9M0kFYXTlpoAr7AO0SrcQ8i7o0tDMY2t1wKNnyUKKja9Y5EkNpRbLwUX6HRDTE81aUjQrBNgdXi76nlkN7cLUVX-2ZMSQbU8SGvO15Ha6adfyg1IE-LRGopXTvLFawvRx6jNXK9iQ5Z7uGwaewNfJ0LQTQtirlkIWzAX2JlvFz97phjTcoL24z7Ww9CSpG_1lsYGkhfwzHhyeUDcUjgqjfUthqAIuRKlFjHd95wyM2TYsRXROJ1jBDecoZOWMfT8qhshnl5AtAKSma3ThuRWrRwQr4Liqq9UENjse2CnRpwFQITVwhkGSnlIge9eAXkdriTFmH_78a6pT6cvtHCipsLHdJS9ce3q9CRg2ICV_ncY9npiDrNPypgwroWHsMnJ6OFv1IhgCiRbT-3O89KvjO0Z6GEEjX9luMXcbXEmYNIJVsBiIt7r59Urks3MtlKhRLZsCkBozztRFwlvmOBDwZKLuZuK5D_HZiSymB5xkKSj9rEUgIdHKCkWhly45ndi8XU8tUzwT_6WKwvlt26jI02nxyNVwA16nqVkR5REPY5wixXzf5nSdyPglgl0kR930YuaNW3AQmCB9jNa51lba49tiSx7gKpTrKeJZFz2N_Qc8n7Uss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48bd90ce61.mp4?token=BUSrj9KK13K7NtEhssxr2UvASo7_34n6vp8kfLkQeSXaj-lM8cpogLMDl9M0kFYXTlpoAr7AO0SrcQ8i7o0tDMY2t1wKNnyUKKja9Y5EkNpRbLwUX6HRDTE81aUjQrBNgdXi76nlkN7cLUVX-2ZMSQbU8SGvO15Ha6adfyg1IE-LRGopXTvLFawvRx6jNXK9iQ5Z7uGwaewNfJ0LQTQtirlkIWzAX2JlvFz97phjTcoL24z7Ww9CSpG_1lsYGkhfwzHhyeUDcUjgqjfUthqAIuRKlFjHd95wyM2TYsRXROJ1jBDecoZOWMfT8qhshnl5AtAKSma3ThuRWrRwQr4Liqq9UENjse2CnRpwFQITVwhkGSnlIge9eAXkdriTFmH_78a6pT6cvtHCipsLHdJS9ce3q9CRg2ICV_ncY9npiDrNPypgwroWHsMnJ6OFv1IhgCiRbT-3O89KvjO0Z6GEEjX9luMXcbXEmYNIJVsBiIt7r59Urks3MtlKhRLZsCkBozztRFwlvmOBDwZKLuZuK5D_HZiSymB5xkKSj9rEUgIdHKCkWhly45ndi8XU8tUzwT_6WKwvlt26jI02nxyNVwA16nqVkR5REPY5wixXzf5nSdyPglgl0kR930YuaNW3AQmCB9jNa51lba49tiSx7gKpTrKeJZFz2N_Qc8n7Uss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أصوات طائرات حربية كثيفة تسمع في سماء مدينة الطائف السعودية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91000" target="_blank">📅 18:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90999">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇨🇳
السفارة الصينية في الرياض:
نحث المواطنين الصينيين والمنظمات الممولة من الصين في السعودية على تعزيز إجراءات السلامة والبحث عن مأوى فور تلقيهم تنبيهات أمنية من السلطات المحلية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90999" target="_blank">📅 17:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90998">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqKXZ6Mt71nBf5-k0vP0qKX-0gd_lX1i9qOI1IMyKK4Wx3qVzEtFSKlZIoSi4s4XxbxHbpEzXkLsGqmoe9-O5hfke8fdicQE7mIOMP5bMHm22Zlg6eVO66CHLr0FGb258tnj_ZGZKx0NuXHkCcUK72VWuZAPkhtLYCRAbrVlbisDr8aU-_G9ZmJddNTB8mujZh460TEqSxhOI7CVTTzzbeYdL_qqnSstvtwW1940yHFJlKpBcGnCc4ElVJ2xClfykSj0s_WUM93e3iQcYjPvkG7oUB0YtlqTjGbMMyTPePlpTGOvb7wb_o7Ikd_wZc3BIMCqskipGWUdSf3UgmmhLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرياض لحظة هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90998" target="_blank">📅 17:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90997">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
البنك المركزي العراقي:
الارتفاع في سعر الصرف في الأسواق المحلية يعود إلى المضاربات في الأسواق والتوقعات وسوء استخدام الظروف الجيوسياسية في المنطقة لإرباك الأوضاع الاقتصادية والمالية من قبل بعض المستفيدين من هذه الحالة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90997" target="_blank">📅 16:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90996">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922e790775.mp4?token=NXKZE34vfjGD5441jeVY8i4CDydj6u9X-MIYnOok5MTeUv19x0j0X-kApMeZDpnMh5tgcQr9eD4vPtx5WC5qtYjrOuF8T7F10C3ZW1S45yr2BeCgcRQ3NB7CoyIdZk10Ydzn-zr44ubUTBVPZzch5-LA7-VSjtvpp5mL7rpyeOq9W4WDEHB7De3FRAxp2B1K2biyFG9Ds2GQdHd46RVY7BszsAbzMcAU9PrjpyWdazs8NmWqpacPeo7tMNGow99ULJ5kiHB_YGV1OE34PNv0N73seCTs02Twuc2EtIkxVV53bxXRjO3JX--ObyZjBe2OSeYIPl3j2GhwENFLrnWOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922e790775.mp4?token=NXKZE34vfjGD5441jeVY8i4CDydj6u9X-MIYnOok5MTeUv19x0j0X-kApMeZDpnMh5tgcQr9eD4vPtx5WC5qtYjrOuF8T7F10C3ZW1S45yr2BeCgcRQ3NB7CoyIdZk10Ydzn-zr44ubUTBVPZzch5-LA7-VSjtvpp5mL7rpyeOq9W4WDEHB7De3FRAxp2B1K2biyFG9Ds2GQdHd46RVY7BszsAbzMcAU9PrjpyWdazs8NmWqpacPeo7tMNGow99ULJ5kiHB_YGV1OE34PNv0N73seCTs02Twuc2EtIkxVV53bxXRjO3JX--ObyZjBe2OSeYIPl3j2GhwENFLrnWOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة هجوم القوات المسلحة اليمنية على العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90996" target="_blank">📅 16:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90994">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3773ef6e7c.mp4?token=oJT8a_MSLW4UVt8_Zez5uvmPErv85tC7gNrI7cu6riVSPOg81xgMFsxjSW9tC1f_CpEBWUEt5g04NkeuY_lFdbWGDJ0w6ep0rQlKcnuom2Pn-9JUREZOgo8Et3LE-Soiho45sxXAxc_hgaO-V7X7u3Nj-nyHw7PUL1UfZrqkpTaUbaroKxI7eyAuenq0n8TZXXRn4bGGgPSNORCP6hnBjbDGaJgy0wj-ief9ptP3nhHbSAwMkGRoF4RudTN9sIt0Ydfxi02DnhuV7ifCfWrpF_A2LG3yKtqhMKsra5NW-Vcwvzg0sSrhntB_gko1_88nmJSiUVUpPwiG_778hu6cEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3773ef6e7c.mp4?token=oJT8a_MSLW4UVt8_Zez5uvmPErv85tC7gNrI7cu6riVSPOg81xgMFsxjSW9tC1f_CpEBWUEt5g04NkeuY_lFdbWGDJ0w6ep0rQlKcnuom2Pn-9JUREZOgo8Et3LE-Soiho45sxXAxc_hgaO-V7X7u3Nj-nyHw7PUL1UfZrqkpTaUbaroKxI7eyAuenq0n8TZXXRn4bGGgPSNORCP6hnBjbDGaJgy0wj-ief9ptP3nhHbSAwMkGRoF4RudTN9sIt0Ydfxi02DnhuV7ifCfWrpF_A2LG3yKtqhMKsra5NW-Vcwvzg0sSrhntB_gko1_88nmJSiUVUpPwiG_778hu6cEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية لتصاعدة اعمدة الدخان من مطار الرياض الدولي بعد الهجوم اليمني</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90994" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90993">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234fc6665a.mp4?token=Gp4P7-8gB3-UvI8mhNwtNN-Ia5-thgmMjLYC-XzPow33UFCQlB-tmCZzJpDwSm9EaCI4BwYKu9Z9a_XYp79_3ttXwME-JLut4_0qZUO0IRr0nLxDuRmZlX8J1O0utuJ-3-SbFMGKO92saU6kLZHT894wm5HzWyzX88CpnUprnVts8xnv0X1HwBD26oK6ggr5e4a62js8-BCDE1jA4gP25TtvyhWoNrztinhCSPW_l4urTn9-KYkMNnzoC-FXyiyBNRrHw8ofcRJ60os7BoVkYgyHROaF6mitzEKxfrJ1m85D64BBqXdF0--PnCubZWr_Il_Ybx4S7hKQJFEp0YrG2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234fc6665a.mp4?token=Gp4P7-8gB3-UvI8mhNwtNN-Ia5-thgmMjLYC-XzPow33UFCQlB-tmCZzJpDwSm9EaCI4BwYKu9Z9a_XYp79_3ttXwME-JLut4_0qZUO0IRr0nLxDuRmZlX8J1O0utuJ-3-SbFMGKO92saU6kLZHT894wm5HzWyzX88CpnUprnVts8xnv0X1HwBD26oK6ggr5e4a62js8-BCDE1jA4gP25TtvyhWoNrztinhCSPW_l4urTn9-KYkMNnzoC-FXyiyBNRrHw8ofcRJ60os7BoVkYgyHROaF6mitzEKxfrJ1m85D64BBqXdF0--PnCubZWr_Il_Ybx4S7hKQJFEp0YrG2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاعلام الفرنسي عن مصادر: اشتعال خزان وقود تابع لأرامكو قرب مطار الرياض.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90993" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90992">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزارة الخارجية اليمنية:
- الأعمال الإجرامية الداعشية التي اتجه النظام السعودي إلى ممارستها في اليمن، توجب على المجتمع الدولي تحمل مسؤوليته حيال ذلك
- هذه الأعمال تُعيد للذاكرة ما قام به النظام السعودي في الفترة الماضية في كثير من دول المنطقة وفي مقدمتها اليمن والعراق وسوريا
- اليمن يمتلك الحق المشروع للرد على أي نشاط سعودي داعشي يستهدف أمنه واستقراره، وسيتخذ التدابير اللازمة
- حالة الضجيج التي تظهر بعد أي رد يمني مشروع من قبل بعض الأنظمة تشكل غطاء وشرعنة للأنشطة السعودية الداعشية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90992" target="_blank">📅 16:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90991">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مشاهد قريبة من موقع الهدف المستهدف توضح حجم الاستهداف والدخان الناجم عنه  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90991" target="_blank">📅 16:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90990">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏
زيلينسكي:
وافقت على تنفيذ عمليات بعيدة المدى ردا على الضربات الروسية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90990" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90989">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_JmuxcBDJohoniMKGRNrww1I2_2GZ30dJmNO3oVVk2DvZngglMZaxLrIzMmJu8tM-B92DuU4CcuuuZ1Kr20NebUp1wgt53_yUsNwQTL4wk9oK7sUwdRa_9bC_Qdd_Y4pbK-i-R0TG7uv170fJMQiBvxqNYoKhuj6CZtjqn2BfSRpD0-iZa5y_5AT7OKZPBBSugRNlnlO86GJMnvH9pUX2XrOxEskEFfDbMdTviCfNW8VxNKu9bUxMQuOasXc7htkmOIgGmLZIuKTzUxbWjPW9elNEksmJ1I4plU7mffjshpkkiKCNx19IxvTFmxh5f6GuaNQRsGS_n7LrSEPHmuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصار الله يدكون عاصمة ال سعود
النظام السعودي:</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90989" target="_blank">📅 15:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90988">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702bac9acb.mp4?token=cHTslQ_F6ZHBqt2eIFrrxvTXYWUJ_eCbry28JonMB3bjNRC833m9N-7muE5b6RJVrgLpvyGSvsgwYgERx9yk1M27oSIN_9gCUHtk91OyYX8Vng0Pwqb995qooNs3RpC-tLJxGtPnlzUoXjB9ogCPcFc0bsMw7tVFqY4FmQPfy9gTMORzwGRRvmgeUqKbnJ5tMbM1lt1uWWKmzviQmt8G5bly9mb2oXiwnpjTmpikDhFQPn1F8sHVQzay5n4GJraF8FpjM4okwnOjAytuxqF6Tq_bk-BorbBeJFzXpGJHsLSpykn_KMlC3opYb0RAnXjWtgH31pINi4Geu2KCE0Ltqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702bac9acb.mp4?token=cHTslQ_F6ZHBqt2eIFrrxvTXYWUJ_eCbry28JonMB3bjNRC833m9N-7muE5b6RJVrgLpvyGSvsgwYgERx9yk1M27oSIN_9gCUHtk91OyYX8Vng0Pwqb995qooNs3RpC-tLJxGtPnlzUoXjB9ogCPcFc0bsMw7tVFqY4FmQPfy9gTMORzwGRRvmgeUqKbnJ5tMbM1lt1uWWKmzviQmt8G5bly9mb2oXiwnpjTmpikDhFQPn1F8sHVQzay5n4GJraF8FpjM4okwnOjAytuxqF6Tq_bk-BorbBeJFzXpGJHsLSpykn_KMlC3opYb0RAnXjWtgH31pINi4Geu2KCE0Ltqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدخان يملئ الرياض منذ ساعات والدفاع المدني للنظام السعودي يعجز بمكافحته  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90988" target="_blank">📅 15:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90987">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e8fb5d2c.mp4?token=GFOndLO1F9eM9gqCcAKS46wh5rsDcWoXRkGNx04sJ9TmLCUnl1QngBf1ZeQuvgX2EFauhBTMUcca0BHD9dr_vwNd_i2HRgtyxZM-F-rrF0kGPy-Qn_3wYwNHP1nCuIkMHS_KUsgAmpBSrXxNLsUkRYY8c4qvUC5_mcyZ_lXj21iSOqnEsFXLI3RGFQuIh4188zXKS1wgnvXYFoVWmiIasMnjfTIXObT6L1MYchze66F9DAF7OPWWeFqUMrWRReoYP3bQoPwq5Cdmku7ll2R6U-1_bDTDO5QnepDwk6wkUyJk8X0UbFUaTrUp4f99yvoY2cdWHFfZhxVSH1H9iBMBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e8fb5d2c.mp4?token=GFOndLO1F9eM9gqCcAKS46wh5rsDcWoXRkGNx04sJ9TmLCUnl1QngBf1ZeQuvgX2EFauhBTMUcca0BHD9dr_vwNd_i2HRgtyxZM-F-rrF0kGPy-Qn_3wYwNHP1nCuIkMHS_KUsgAmpBSrXxNLsUkRYY8c4qvUC5_mcyZ_lXj21iSOqnEsFXLI3RGFQuIh4188zXKS1wgnvXYFoVWmiIasMnjfTIXObT6L1MYchze66F9DAF7OPWWeFqUMrWRReoYP3bQoPwq5Cdmku7ll2R6U-1_bDTDO5QnepDwk6wkUyJk8X0UbFUaTrUp4f99yvoY2cdWHFfZhxVSH1H9iBMBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هندي حزين على قصف النظام السعودي وسط دعوات لارساله لتربية الماعز ليعود لصوابه.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/90987" target="_blank">📅 15:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90986">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/90986" target="_blank">📅 15:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90985">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f64ee0cf27.mp4?token=LZ2M0fzEcbSvlFt_h_0jU5aul1UmvmEsG8mS7uYlvWrXdaT_oj3aKvJ79oVr5mHSm_LLPI9DABJkfxflUdWdwnKklBY0f5AlenXuMvgRunsow0LTA1NKvTP-vsg6kPiCURypwBmeVhpEubkzUSBkcGSd4kkszfjkbUIxXQSufjlA3IrWYymEG_3sreymNURrqizMvxgdB_xF6sbGBxAZ-lCnDe8hUYy3y5u36b4iy8RS1hf0UBOOlApbONVLinR1KRLhidPOc6orBqzupLqVZVMiGR7sUVtCEGHvZjsh29sCp5xbHJdE7K0GDY-_4lmMY8pZvoC3d-gwhxSOhJMehA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f64ee0cf27.mp4?token=LZ2M0fzEcbSvlFt_h_0jU5aul1UmvmEsG8mS7uYlvWrXdaT_oj3aKvJ79oVr5mHSm_LLPI9DABJkfxflUdWdwnKklBY0f5AlenXuMvgRunsow0LTA1NKvTP-vsg6kPiCURypwBmeVhpEubkzUSBkcGSd4kkszfjkbUIxXQSufjlA3IrWYymEG_3sreymNURrqizMvxgdB_xF6sbGBxAZ-lCnDe8hUYy3y5u36b4iy8RS1hf0UBOOlApbONVLinR1KRLhidPOc6orBqzupLqVZVMiGR7sUVtCEGHvZjsh29sCp5xbHJdE7K0GDY-_4lmMY8pZvoC3d-gwhxSOhJMehA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صنعاء مقابل الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90985" target="_blank">📅 15:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90984">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الإعلام الأمريكي :
انها المرة الأولى منذ عام ٢٠٢٢ يتم استهداف مطار الرياض منذ وقف إطلاق للنار بين اليمن والسعودية..
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90984" target="_blank">📅 15:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90983">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f7d44463.mp4?token=dU_zNCN14ZxnjxbJFI4LC632IMnK1bRUM1i6EZo6O_xFMNfwtIARTGfCvY95Uy12OTnpfJvh5hnur2Vm5WKpPkeIs2yjNz4hsP84ABzWs-JcNJk2RJjSJc5hVuQoQyrU4E6Kvuffu2LIpkGLLl1uh-EeJ98zlGwl4JIAtpexeav-XVEjQ_BI2tawlihKhf7VFmrrjNrg_jCj5DHqOc94jOLsTFNcdjKtSl2TlvJMzVPj-losWLxV5rdYmwckWDJK8OCTuZIoDoLM5COD375h16mi2A7JI5oiCt2h8OPlZfqfeNrY8mO4CH_vxCow3scabYm0sr3fZiUv6pxAZYXc0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f7d44463.mp4?token=dU_zNCN14ZxnjxbJFI4LC632IMnK1bRUM1i6EZo6O_xFMNfwtIARTGfCvY95Uy12OTnpfJvh5hnur2Vm5WKpPkeIs2yjNz4hsP84ABzWs-JcNJk2RJjSJc5hVuQoQyrU4E6Kvuffu2LIpkGLLl1uh-EeJ98zlGwl4JIAtpexeav-XVEjQ_BI2tawlihKhf7VFmrrjNrg_jCj5DHqOc94jOLsTFNcdjKtSl2TlvJMzVPj-losWLxV5rdYmwckWDJK8OCTuZIoDoLM5COD375h16mi2A7JI5oiCt2h8OPlZfqfeNrY8mO4CH_vxCow3scabYm0sr3fZiUv6pxAZYXc0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاخوة الهنود يوثقون لحظات انهيار النظام السعودي العنصري باغاني سعيدة  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90983" target="_blank">📅 15:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90982">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f2127ef7c.mp4?token=uxT1t4rRvtoRXLhwQoZJ-SSK4DHNaryvfcV5oEDvPcKxPwR0vHQzqsUlfBDOjsYOw0vSV9-4XRwbBPYmbjc__eBOW4S8Vx8kqczTewNe0DACOlYDJMrreIT0i9uIpiv7Jy_ekrfzMagoUa1zpZVFWUXnawsgy5fzLKXykpfAyE78IUkJGPUoId3JCWy9Y2Bljk5ZXAVyVWbXcp_Dgi0h2P4_UmpU0VSJeZ4mHEN44N4H00QsE1qSt4DD4DeV2z_ytxs4fJUORzw8qRbtsCc0LVdzHSkwFzwwOSsiAWeX8_kvEUg_WSRMVe0UQmE9yHHjlL46JqENDyz8VW3a7i0dfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f2127ef7c.mp4?token=uxT1t4rRvtoRXLhwQoZJ-SSK4DHNaryvfcV5oEDvPcKxPwR0vHQzqsUlfBDOjsYOw0vSV9-4XRwbBPYmbjc__eBOW4S8Vx8kqczTewNe0DACOlYDJMrreIT0i9uIpiv7Jy_ekrfzMagoUa1zpZVFWUXnawsgy5fzLKXykpfAyE78IUkJGPUoId3JCWy9Y2Bljk5ZXAVyVWbXcp_Dgi0h2P4_UmpU0VSJeZ4mHEN44N4H00QsE1qSt4DD4DeV2z_ytxs4fJUORzw8qRbtsCc0LVdzHSkwFzwwOSsiAWeX8_kvEUg_WSRMVe0UQmE9yHHjlL46JqENDyz8VW3a7i0dfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الهجوم اليمني على الرياض ردا على المحاولة الارهابية التي طالت صنعاء  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90982" target="_blank">📅 15:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90981">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fba06ffa5.mp4?token=My_AKGhIi5kMJ7qo99OfBNJZYyoX2JfWrwi85erF1Q9uVcLBI_uzllKPLSGB71fp80PaD-U70_TymvSgDHbPh-DsQNdj-Rn06FcksxlJY1zKkfM2RSVtvpGb9ay1XeLrDyyuOFm1UAdOkIOjJUmYboV12W3FaZ7dqJXgfT1YFynHsPJCnmVsc5qu18tqPgUtqDHwof6GJhrXwaspO6tWqQhmUfu3tmgOjJdavqu5sZY3ChbclXUUdMIikhBKKyl-4bBQ2r8bBnWVJxKwafcCX9fuBzwphhwSN-V3opV9jDN0nPKEHPN5cu0g1rQ8reqK9MwYbDa7zdciMCo9uCuXJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fba06ffa5.mp4?token=My_AKGhIi5kMJ7qo99OfBNJZYyoX2JfWrwi85erF1Q9uVcLBI_uzllKPLSGB71fp80PaD-U70_TymvSgDHbPh-DsQNdj-Rn06FcksxlJY1zKkfM2RSVtvpGb9ay1XeLrDyyuOFm1UAdOkIOjJUmYboV12W3FaZ7dqJXgfT1YFynHsPJCnmVsc5qu18tqPgUtqDHwof6GJhrXwaspO6tWqQhmUfu3tmgOjJdavqu5sZY3ChbclXUUdMIikhBKKyl-4bBQ2r8bBnWVJxKwafcCX9fuBzwphhwSN-V3opV9jDN0nPKEHPN5cu0g1rQ8reqK9MwYbDa7zdciMCo9uCuXJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد توثق لحظة الهجوم اليمني على الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/90981" target="_blank">📅 15:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90980">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53c7108005.mp4?token=SeWlwkQsbJUUFyPs9vFcVBwzmiGKvk05-TFoqBCs37bnEX6gbGVrgNngyFIJkH84x1f_ommcbCcjE0c-zyX5EngoDuGVe4VIAt1bIszcG-DVFS07wfVoxAr1YBUHxpF2Cs_pmVIXU32_sl3OvMT1n0aqzhypDJORxMmX4H4GC3c17x5Eyv2sSFXM-evvud6g5E1AqYausqLlGhWibaeM3THNeW8jH57P69nYiIT4iuaTV8W4HLWIvqM1iq_Y7wxeEeEXnovSTGqOio4mfAMF5LMZAi1reuGZoP_ZAHhKz5gJ2tIwQSd7YVi2ArS37dONF9Nomg5Lm-0sQ1B_WNSftISzgZcBM_OCd95ATY7AWbUemf1CbOrTmXyrkLFI1QagHfPGurz_OVoGBwfvAVXQ4X_Xt7q6oNm7TuODPJERp_5jmVoiHI29muA_j5IRkcPqRxpyQt0ANDCL-N1c73fWRisuPrJ73X5CuId9MhEVsIJpl54y7Wb6xNa54jCtKJ-yCCC_OLIeOIP1TpLFCH1wR9D48YvmJ2c6ECKeVE6bkRHjdQ3HQWSLZtaaxFUXs4ZLqjfcRf83Yxp-NWq8WAVwoXjU3NsQzE4aFcy0teKQuXLxgVfaIEbUHwLfS4-phAfF1pt1Xtc6RDCDXnwS8M9Jp8TLQyxytlBsDqWx8ndTzTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53c7108005.mp4?token=SeWlwkQsbJUUFyPs9vFcVBwzmiGKvk05-TFoqBCs37bnEX6gbGVrgNngyFIJkH84x1f_ommcbCcjE0c-zyX5EngoDuGVe4VIAt1bIszcG-DVFS07wfVoxAr1YBUHxpF2Cs_pmVIXU32_sl3OvMT1n0aqzhypDJORxMmX4H4GC3c17x5Eyv2sSFXM-evvud6g5E1AqYausqLlGhWibaeM3THNeW8jH57P69nYiIT4iuaTV8W4HLWIvqM1iq_Y7wxeEeEXnovSTGqOio4mfAMF5LMZAi1reuGZoP_ZAHhKz5gJ2tIwQSd7YVi2ArS37dONF9Nomg5Lm-0sQ1B_WNSftISzgZcBM_OCd95ATY7AWbUemf1CbOrTmXyrkLFI1QagHfPGurz_OVoGBwfvAVXQ4X_Xt7q6oNm7TuODPJERp_5jmVoiHI29muA_j5IRkcPqRxpyQt0ANDCL-N1c73fWRisuPrJ73X5CuId9MhEVsIJpl54y7Wb6xNa54jCtKJ-yCCC_OLIeOIP1TpLFCH1wR9D48YvmJ2c6ECKeVE6bkRHjdQ3HQWSLZtaaxFUXs4ZLqjfcRf83Yxp-NWq8WAVwoXjU3NsQzE4aFcy0teKQuXLxgVfaIEbUHwLfS4-phAfF1pt1Xtc6RDCDXnwS8M9Jp8TLQyxytlBsDqWx8ndTzTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوحة يرسمها السيد القائد عبدالملك الحوثي في الرياض والهندي يصورها.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90980" target="_blank">📅 15:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90979">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لوحة يرسمها السيد القائد عبدالملك الحوثي في الرياض والهندي يصورها.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90979" target="_blank">📅 15:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90978">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6156c7481a.mp4?token=mDIbIk_TR9h-k80nRIYfOnPoO1OQLKj6GiAHYzXAXuf5kKcdUjIgFGJ7iT0vWfLx0i2c3nJwKD1jOVFRsXrK87WwFOuOX_mt0Rs8I3oUMAsHV21tTULCozutsdufpqrv4vp3nxY8F6XpspZQACg6KpjnGjffJ3yV3Qlyoi7CM7OoIKLqyH0LfjP5VY7wW6pKu64MdjwSOmcXdWSzx0L6XPhLoef0rwnbWAPQ8q479YY0dQkaKrgHn_ft0lFEG2RFPwuaAnepEi4quXE52Yw1E0rWKYH0kuV-hgYmIE1OaoaCQCyOtWpXLyltVk2U_XZ7Kweg_ZTVq05ZDlg2G-QfHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6156c7481a.mp4?token=mDIbIk_TR9h-k80nRIYfOnPoO1OQLKj6GiAHYzXAXuf5kKcdUjIgFGJ7iT0vWfLx0i2c3nJwKD1jOVFRsXrK87WwFOuOX_mt0Rs8I3oUMAsHV21tTULCozutsdufpqrv4vp3nxY8F6XpspZQACg6KpjnGjffJ3yV3Qlyoi7CM7OoIKLqyH0LfjP5VY7wW6pKu64MdjwSOmcXdWSzx0L6XPhLoef0rwnbWAPQ8q479YY0dQkaKrgHn_ft0lFEG2RFPwuaAnepEi4quXE52Yw1E0rWKYH0kuV-hgYmIE1OaoaCQCyOtWpXLyltVk2U_XZ7Kweg_ZTVq05ZDlg2G-QfHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة للحرائق في العاصمة السعودية الرياض على خلفية الهجوم اليمني  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90978" target="_blank">📅 15:24 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
