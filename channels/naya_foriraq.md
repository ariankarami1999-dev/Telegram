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
<img src="https://cdn4.telesco.pe/file/ClMgDAwcwIDs63KMp_3H8KfFmE7yoLtxxWy_04Z-o-i7lc77JT_-cKdLm5BK9fz1s7Q9XIm-rcXzs5tWVOQSBPYuw4gGgTkrZzgB1DApQL1aB4mfoQWYWkKuNxlVymBS-BcljUsldLrBQShGnaq03KYnUoy8HzJjTaOxZ3flRhOsdsN_o5yayyOnkwEaBCDNDgeq7XMcuVBArDeILqoFI3Zsghs__SND9oKInhfa5ZDjrSDEOmNEyY9XGqIwN3Lhu-1YeQkJEfSHSz13oeGyeBeNPISYWdX8rIEo-dT2x6buBALNjLyoSeHAl9ZPdWTukVIh8MOdQ4wK1biUFsiTvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 20:46:10</div>
<hr>

<div class="tg-post" id="msg-86422">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇪🇬
البحرية البريطانية تؤكد تعرض سفينتين في مصر لاستهداف بواسطة مسيرتين.</div>
<div class="tg-footer">👁️ 955 · <a href="https://t.me/naya_foriraq/86422" target="_blank">📅 20:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86421">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏
الخارجية الفرنسية:
إغلاق مضيق هرمز يؤثر على اقتصاد العالم.</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/naya_foriraq/86421" target="_blank">📅 20:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86420">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80be21696.mp4?token=qFQjCRVJiudBVGfgFeH_LhcwBmbBK-fR5gxBvfRDwtWURsRlGkFKsAf_2tsKPeXEaiNjTuPhl41JmVlaYZnIJ5kEMiTjirY9o-LpreSS-4LE7p2Zpv2KZZ_SJQCLA5SBjELD5fM-dO8i4F4KuXUXFAoZIKs-Yi5O7hbUnMOqRpgT6W-rqx9Zs_MEezjY9_Zy_p1nIafrnggiov1x4fEANddnEnVBpay4aPvKf8Pne1JrW9Cqtz66qwRWbFbdQcx3kDyCkZJbsRoV__RJRVnF7MlPPa5aq2wCNvtZjiuBbtREj0GgUH9KLbG58AjT8G0XrRV5V3WAOxq7m1gni4KZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80be21696.mp4?token=qFQjCRVJiudBVGfgFeH_LhcwBmbBK-fR5gxBvfRDwtWURsRlGkFKsAf_2tsKPeXEaiNjTuPhl41JmVlaYZnIJ5kEMiTjirY9o-LpreSS-4LE7p2Zpv2KZZ_SJQCLA5SBjELD5fM-dO8i4F4KuXUXFAoZIKs-Yi5O7hbUnMOqRpgT6W-rqx9Zs_MEezjY9_Zy_p1nIafrnggiov1x4fEANddnEnVBpay4aPvKf8Pne1JrW9Cqtz66qwRWbFbdQcx3kDyCkZJbsRoV__RJRVnF7MlPPa5aq2wCNvtZjiuBbtREj0GgUH9KLbG58AjT8G0XrRV5V3WAOxq7m1gni4KZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع صوت طيران مسير في قضاء كوية بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/naya_foriraq/86420" target="_blank">📅 20:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86419">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phQQuJctdiG2t3ZUrZME-9EVsJuRNhF9UPeef-J5UwFfWXW2Zd19U2XBJKxsSWSuixNLd-7tK4QYC0DSUUIVSVrXUKhWg4OApgDhxQVM3mt5SXDEtt7LYTj5ndjYobA4D5VE5H-E4n26g1JR4U8ZIieiNdt16mcgrwct2xLSv_WLEe3Ea1lucccNHBwzR0ELtd7brnZyN8vLl68a3HPABt0jBt4U3D0h2R8E-HyVX3s-cON871cyW3o5ASJQSZ96LAUChTtUJf672UO5pIm1tIlEGfFNwWVrwZVQwRaX2bc4jgUBOd2IWY_qAVkcPZLVWuuVKI3TpZHDF5lLuJRUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاعلام الاجنبي‏: السلطات المصرية حملت إيران مسؤولية الهجوم على ميناء دمياط.</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/naya_foriraq/86419" target="_blank">📅 19:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86418">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f68ec6f4.mp4?token=Nqo6Ri8L7-LgsFCdPGr22o96gg5iTYWe49shrVXHPY6-C5LIgsVUjXMkTyaXCocgUWQHk3Ij-0yT7HLxn9_7sW0AynRVFFvb5hErFph_ecwG8kj8ZtxTubHihEXipvXADOkTXAmG37Z4kUREwep-qGYeFRDgw32bP89qzzg5JTlrwCccDAGCumk5LFO8jDTrZddLGKo7nslfSrKWRyqwPczFbhxmPuR6Mz36xO3zWKIBWGf0mCFhf6ajUyvMheyd5Z0gcblU3mo4k5zVdxKGVo-DVPeZoPUcbVDd5Sd-FV1B8gJtzdtpetcQ5OPX7QbbEhCKdJ4DLCtWSaEEwY8fiTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f68ec6f4.mp4?token=Nqo6Ri8L7-LgsFCdPGr22o96gg5iTYWe49shrVXHPY6-C5LIgsVUjXMkTyaXCocgUWQHk3Ij-0yT7HLxn9_7sW0AynRVFFvb5hErFph_ecwG8kj8ZtxTubHihEXipvXADOkTXAmG37Z4kUREwep-qGYeFRDgw32bP89qzzg5JTlrwCccDAGCumk5LFO8jDTrZddLGKo7nslfSrKWRyqwPczFbhxmPuR6Mz36xO3zWKIBWGf0mCFhf6ajUyvMheyd5Z0gcblU3mo4k5zVdxKGVo-DVPeZoPUcbVDd5Sd-FV1B8gJtzdtpetcQ5OPX7QbbEhCKdJ4DLCtWSaEEwY8fiTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتنياهو
: عمدة نيويورك زهران مامداني، "يدعم إيران وحماس وحزب الله".</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/86418" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86417">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace29ffb85.mp4?token=cnKnpy-1HMksHgusQ9nubbxPOhmGWTTrtFNjJrufMrGnQIgjl49NYOegf3sXq36tShaeTM0SqNwJWwDjD6dsfOPFcuJO4S833ALD5A7t3zoJk_gWBneL_ss_6ZYpOCZCFxEZOAbXi3iY6BPLY979LPUblCEsLXSpctWaPUjbzfTTSGzJNtd3885tBN6EcK35JpSP1dYu9_ZuIV0_1A9zNvoe2DVzoKH8PGCwy-H1SVx9-5S52xZVveNeQjcgNF26RD8cTwr_7mloM_cDnYWCm5rjXSr8kmSjcSJxkVFB7nArPUxYfYSbYtzx-Q7ECdH0mtQFhOkQrtgJIJT_dRxBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace29ffb85.mp4?token=cnKnpy-1HMksHgusQ9nubbxPOhmGWTTrtFNjJrufMrGnQIgjl49NYOegf3sXq36tShaeTM0SqNwJWwDjD6dsfOPFcuJO4S833ALD5A7t3zoJk_gWBneL_ss_6ZYpOCZCFxEZOAbXi3iY6BPLY979LPUblCEsLXSpctWaPUjbzfTTSGzJNtd3885tBN6EcK35JpSP1dYu9_ZuIV0_1A9zNvoe2DVzoKH8PGCwy-H1SVx9-5S52xZVveNeQjcgNF26RD8cTwr_7mloM_cDnYWCm5rjXSr8kmSjcSJxkVFB7nArPUxYfYSbYtzx-Q7ECdH0mtQFhOkQrtgJIJT_dRxBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من تشييع جثاميين الطاهرة للشهداء الذين استشهدو في القصف السعودي على الاراضي العراقية.</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/86417" target="_blank">📅 19:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86416">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/987b1f2bad.mp4?token=UUQrObsTQ-2uffNnIxgcYhnJUDxQQkj2cCPODraKztFmvG-G8EXi7njebKuskEefBJt8fI9_1ZqKgLGyOaDKF_yIHP--Zq_BQa2hFs8stIwjMC_YcomPBRgimTNaQRkA_Xq4qtkVXokUVf8L8tV-pwsIcKXQgrmMvScqeeRHEgWMwKKXLmZhZ4c_iyJ65rY9X3mIEqQU8mZDvSr4OuN2s1UJVCa7KCEuBPLPsASMl8_Py7O2cqe_yWMKg_0UL9HAuk64kwr4obBg3lTfkBBiCqkj9GIL9QxDaYgiEZCwYCJxh5X9mhRTYWlH7KayKzXAF6-TEtKiwerZJLlDpW_w6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/987b1f2bad.mp4?token=UUQrObsTQ-2uffNnIxgcYhnJUDxQQkj2cCPODraKztFmvG-G8EXi7njebKuskEefBJt8fI9_1ZqKgLGyOaDKF_yIHP--Zq_BQa2hFs8stIwjMC_YcomPBRgimTNaQRkA_Xq4qtkVXokUVf8L8tV-pwsIcKXQgrmMvScqeeRHEgWMwKKXLmZhZ4c_iyJ65rY9X3mIEqQU8mZDvSr4OuN2s1UJVCa7KCEuBPLPsASMl8_Py7O2cqe_yWMKg_0UL9HAuk64kwr4obBg3lTfkBBiCqkj9GIL9QxDaYgiEZCwYCJxh5X9mhRTYWlH7KayKzXAF6-TEtKiwerZJLlDpW_w6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مسير معادي في سماء محافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/naya_foriraq/86416" target="_blank">📅 19:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86415">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الاعلام الاجنبي‏:
السلطات المصرية حملت إيران مسؤولية الهجوم على ميناء دمياط.</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/86415" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86414">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇶
سماع صوت طيران مسير في قضاء كوية بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/86414" target="_blank">📅 19:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86410">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHZ7GUmeLIfAIErkbL_p2A3YS9M8JvOvgj0dhKqSS3Us7eLIsDGLkXgWqeqtD60YRcz_CdD54S_x7Jequ4SU3exQzFl6b5g8vANTmup-sv4VC1IFpE7BLeANzmups5oP-9XOT-4VUaW_Kh2ZGcG3V-PYP6E0Ovq0i5GzorNw10sF--I1mmmpukIF3q77juqkFrvkf8r8SaXtdW22zSNPQGR4BOJJWOzRccLyUrcma0zkORSHKpCaqnjDqmyyXPvhee6ljaixuMPTkps2w29IKybfvawjUOJkEVSVuDWBNqPiLIYgulMn2gFcHcAIl5jDDJSCw7r9TxySkD_QLndUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PE_T4kQjCRYDz5CVrIEk6QN40ACuwLrZuR6o0dI4k-JHzX1oLdHsZ0fiI6YmdRgHAHwltQ2wo1jm9iVY3HwitF_h6tZWZUUod6YfxhKqP1tggmM9xa8BMO2A2y7QAzEJ5vPJgnHynzwJsO4Q-KmGC7zNidAD-5zo0BfgUVMWG4yfDtCCBn0ZXX7ymhj3jT3BTUligIe_rW7bZYomLUzDN3nK3zbZgScOVAZYAV4-ftIffy7GDkDy--yZgmBkHP5-nRr579dMJAQhFheqP7tQWAdCaSryCQOSzJIM_l8KZp2P265CYT3lkRuuDkRR2nhwzLP4DJ8fl1OHUYYFcXDDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVMsSZ-HMfxPRgQUzyO551svjhIFC-82O66_65QhZTV6IFx4OxUi3MuNC7FhpF7bAeDp5ixvdS3AV0gkAX6PksVpbaca__GoQ767BmJRxKDt7Z8iqFB1dAN3Rn9UK5-s-W4JZjNGnNE5xbkcycqRn2Xs28vfp7tLfeOu-SE2YZeetBivKKsERd9KEr7r-1yk5nJX_jX8k9bo4wnKJihs2N_avC_qEaLg-OatmGuVQ68N2GjIfaTYWJs7xTaUv7rczm-IgvadCSN8UvgnIuN3Vhkae_vjCnMMkCiHAnzaAPcrDmdXwRg62M6EE-l8Gv72rfWofeaIZpZ7fD3XdGz1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRDJBTS4QrGPlAa9poS1SJQcp0YaGlCx5AqleY9t9XxqV80WbdK7K3__5DOoeUr2GVZFdd9oIBlllWwiCtRPAaRDwIvDO7BDHNibcPHiazAFpyYeAvekaHfdHYBpWPYS5H2yZFRA6KeLXh-XRdEyGCee2KF_OwcdtdsQ9JGdhm4BeDsPvEEMpf9nhC0QZxYAMnIw0PMCMu6rb6MYHKWn5jlmUlaZUzkk0Or9CsNC6xfGFTT0BCBWajylHe4mnpYLKLrXeY7bLqgPNiLaqVqDyr60ZGmZyJnUvQ5BGVNpns1O6Gq7-PqOpWyLMlRKzOVcvXWhGDaTqQBUHxxyc5TX7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇷
تشييع مهيب لجثامين شهداء الاعتداءات الاميركية السعودية الغادرة في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/86410" target="_blank">📅 19:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86409">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏وافقت الاتحادات الوطنية الـ 55 التابعة للاتحاد الأوروبي لكرة القدم بالإجماع على مقاطعة كأس العالم وجميع مسابقات الفيفا إذا مضى جياني إنفانتينو قدماً في خططه لبيع جزء من الفيفا لمستثمرين من القطاع الخاص.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/86409" target="_blank">📅 19:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86408">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8dcb22e88.mp4?token=Bq87OipJBEGH6nRnjVlICgxYyCDp916aOlVU8ZVqpSwxQKQ_B8zjMGiMt9FE7j_krK40RuzAHw2qLJ8sFBa0GVt8tLHv_r3LxnbixgblqcbDgCewUso5OoZqCMa31MZ1DUNb6mlVCgya9dMbIvAsJ-4aLsHHqzxKTMq4Ic67DirxSBgONX0qpVQ7IribFqjaG1tGQL5IA8e9YQb-M1yqdrWMbeVEvAEq57i5De59oi8OGJzLjxNdkAq6iDsvzyJ3AJGxTV9lFP5K7XDGJ1GuFCwo550NnUMHsbwvYovA2jyWip6fFsVGzA2kr5O6xAet5fbUNIjlPrtu90yJsuSntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8dcb22e88.mp4?token=Bq87OipJBEGH6nRnjVlICgxYyCDp916aOlVU8ZVqpSwxQKQ_B8zjMGiMt9FE7j_krK40RuzAHw2qLJ8sFBa0GVt8tLHv_r3LxnbixgblqcbDgCewUso5OoZqCMa31MZ1DUNb6mlVCgya9dMbIvAsJ-4aLsHHqzxKTMq4Ic67DirxSBgONX0qpVQ7IribFqjaG1tGQL5IA8e9YQb-M1yqdrWMbeVEvAEq57i5De59oi8OGJzLjxNdkAq6iDsvzyJ3AJGxTV9lFP5K7XDGJ1GuFCwo550NnUMHsbwvYovA2jyWip6fFsVGzA2kr5O6xAet5fbUNIjlPrtu90yJsuSntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
سنتكوم تنشر تسجيلًا صوتيًا تزعم أنه يوثق تهديدًا منسوبًا للحرس الثوري للسفن التي تحاول عبور مضيق هرمز لمخالفتها قوانين وتعليمات العبور.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/86408" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86406">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
🇾🇪
🔻
رويترز : قال مسؤولان في المنطقة إن الحوثيين اليمنيين هاجموا السعودية هذا الأسبوع من الأراضي العراقية بالتنسيق مع الجماعات المسلحة العراقية، وفقاً لتقييمات أجرتها السعودية وشركاؤها الإقليميون، مما يعكس تزايد التنسيق بين الميليشيات الموالية لإيران.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/86406" target="_blank">📅 18:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86405">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db13ec2079.mp4?token=LG24BfUBPS1HPp5qQ1goIEZW0USkCJ_yxVgSM1JGKjgqoPgUwXe0pEbe3QvTGWCeqoHeeLfQLVeGpSnj_Y3VPEOpsFiAasLweH5pPZ8LHNN5LKAYw4iBbQVTedlZ20bEHGAARLQVgZQhyUduP7x-7QsM3m8b4TS0gmtkt8PdJceOFbG43yXe5Ui98MnwXjYfHMNGQN8Naa2wCeBN0l473_BIdc--3-IBgiZ5fse8eb3UOuEJGabcAAnFb2ZTLrSACTK-BA2TTVyR9AabgYmkr5_yNFhGQ1-C4z3ut_RgamWxEvCdy4WjuN3Os9rXP8yU735iwq-GW3xj0WGw56M9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db13ec2079.mp4?token=LG24BfUBPS1HPp5qQ1goIEZW0USkCJ_yxVgSM1JGKjgqoPgUwXe0pEbe3QvTGWCeqoHeeLfQLVeGpSnj_Y3VPEOpsFiAasLweH5pPZ8LHNN5LKAYw4iBbQVTedlZ20bEHGAARLQVgZQhyUduP7x-7QsM3m8b4TS0gmtkt8PdJceOFbG43yXe5Ui98MnwXjYfHMNGQN8Naa2wCeBN0l473_BIdc--3-IBgiZ5fse8eb3UOuEJGabcAAnFb2ZTLrSACTK-BA2TTVyR9AabgYmkr5_yNFhGQ1-C4z3ut_RgamWxEvCdy4WjuN3Os9rXP8yU735iwq-GW3xj0WGw56M9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان يستهدف العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/86405" target="_blank">📅 18:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86404">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هزة أرضية في محافظة كركوك</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/86404" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86403">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انباء عن انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/86403" target="_blank">📅 18:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86402">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انباء عن انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/86402" target="_blank">📅 18:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86401">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">السيد عبدالملك الحوثي: ترامب يقول بنفسه عن السعودي بأنه بقرة حلوب يحلبونها حتى يجف ضرعها ثم يذبحونها بعد ذلك</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/86401" target="_blank">📅 18:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86400">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436447c59d.mp4?token=rpw-h2GuQsKczWQeZqAlserf8msRBQU3UNSLR_OgrYi3B8X9BeGrUt3hJ3vCFsKGKSUUreTAQaj3J7aUnK4W0QzRvilNQiCn4R5uHKM6KcaHoYv9E8qMPqI9fJB3EDZALy9EjvHfQmNx-zz6K8dWDHcVn9uNKFWUoryXOSTNix3xkaprTCkiGqqe4h_DJEFBV2NnmqeJzl4fdi-_2FkHV6-fvucLnj2HWHMsxANer0STLeDxhf5NNokCTTdwBFQhAy0VSePitnYqQ2GILYmJBj2OsHupkXDbLkDkSEafGJ9G2eAljhM7LGuaignAsgwNhzraeGUa64R-ijObf1bUgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436447c59d.mp4?token=rpw-h2GuQsKczWQeZqAlserf8msRBQU3UNSLR_OgrYi3B8X9BeGrUt3hJ3vCFsKGKSUUreTAQaj3J7aUnK4W0QzRvilNQiCn4R5uHKM6KcaHoYv9E8qMPqI9fJB3EDZALy9EjvHfQmNx-zz6K8dWDHcVn9uNKFWUoryXOSTNix3xkaprTCkiGqqe4h_DJEFBV2NnmqeJzl4fdi-_2FkHV6-fvucLnj2HWHMsxANer0STLeDxhf5NNokCTTdwBFQhAy0VSePitnYqQ2GILYmJBj2OsHupkXDbLkDkSEafGJ9G2eAljhM7LGuaignAsgwNhzraeGUa64R-ijObf1bUgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇰🇼
الاقمار الصناعية تظهر ان إيران تمكنت من استهداف قاعدة علي السالم الجوية الأمريكية في الكويت الليلة الماضية. لم يتضح بعد نوع المنشآت التي كانت موجودة هناك.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/86400" target="_blank">📅 17:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86399">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
🤡
Zelenskyy, be careful tonight. Mama Odesa is in danger</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86399" target="_blank">📅 17:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86398">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2dVBuLEhshOPKRuR0_dFFtkNpFHl4nm53mLVIzn1i5Uc_0CLhpVO8-l1jV_h9lCQiGnQ9Po7AAO3-h7wCnp7J1FGXBDYofwPdjqgJOTf3wDY3bv1_7gSaFMt9cEJCn-klTmF0FhFQwi6-iBaA5V13OQ6aZETpHaGqUN86Fwuit7d91hsBpMHGlXASBm9auXs83pDDJUgd4oWmPncrM3pVJ1ECqkF8F4yw6cnYBa29DLEfTyESN5i2K7Vl0b7jJ4h2UEfuoP59dJ97hgAoXXVa3W3Z_rgwI4vfkw5u7Hb2GoO_2JtJPX57LrBwoHgcnvbByD041dZKYKsV-IbELCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام غربي : تعمل السعودية على تشكيل تحالف دولي يهدف إلى حماية طرق الشحن في البحر الأحمر من هجمات الحوثيين، وفقًا لمصادر مطلعة على المناقشات.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86398" target="_blank">📅 17:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86397">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇾🇪
🇮🇶
السيد عبدالملك الحوثي: نتوجه بخالص العزاء والمواساة إلى الشعب العراقي العزيز ومؤسسته الأمنية ومجاهديه الأعزاء وإلى أسر الشهداء في العدوان الأمريكي السعودي الغادر الظالم، نستنكر وندين العدوان الأمريكي السعودي الظالم ونؤكد على تضامننا الكامل مع الشعب العراقي…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86397" target="_blank">📅 16:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86396">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇾🇪
🇮🇶
السيد عبدالملك الحوثي:
نتوجه بخالص العزاء والمواساة إلى الشعب العراقي العزيز ومؤسسته الأمنية ومجاهديه الأعزاء وإلى أسر الشهداء في العدوان الأمريكي السعودي الغادر الظالم، نستنكر وندين العدوان الأمريكي السعودي الظالم ونؤكد على تضامننا الكامل مع الشعب العراقي ومؤسسته الأمنية ومجاهديه الأعزاء بكل مستويات التضامن والموقف.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86396" target="_blank">📅 16:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86395">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhnyQfqLOFtncCGJkZuTsNCxeZogjisixhGWCbHD2YNdShnXllHK4vXJAJwxiX2qKwM2s6Nzs0z6jtSfYoYPIwtk-Exg0osLRbXuYaGxgZajt7z18nufcU8WHpTZKBVH-RkoJc7eoSQVRsLfaFT15wRMwKjaq30j53TV7xX6L1whPXtcPnrUu83XA-kVfjTlkSV1ziLFR1JZu1TWrZCGCWvcK-Mu-rtfmQeT_Ht88No2kWL0be51IZ2NifLrzVplegHMp7e7950_Voj-GvzRfZC2n9gfSJ7ixdSbmSxvAgGt3to6HHGgTkD8et8Lt2MdO7pFcHnvsfIzxnX7VqsdCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:  صباح اليوم، وفي إطار العملية "النصر 2" ومعاقبة الغزاة، تم استهداف قاعدة جوية أمريكية في علي السالم، حيث تم إشعال وتدمير منشأتين للطائرات بدون طيار وخزان وقود للطائرات والمروحيات العسكرية.  يجب أن يعلم المسلمون في الكويت أن معاقبة الغزاة…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86395" target="_blank">📅 16:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86394">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0b5a4b97.mp4?token=qlwVIpkri_aXm89YrkMr338xNV5ZMSLX492EVrTn1xV6dnxr9n4dGUauMrfTeyXKvcAQLA8gz7LxwPiIAzV-fr3-ThoM9qbgCRpRIhnh_0UlvlIAfbMN_Gpd3c_m0fKYxeDZcNYOahM0dIcuTEi9pPl5ASUVOtCNC5eaLxyEeWJvPR5eY2OWxmrLmCf-XADjFYFOqOkMerK-UWh-za8BWekpwQthRrHa8zaIF1djpE0wwhfXeV2wIU-9qdeKUppBBwytBIdYLGzxYc3nmajVlEYGuxGnUJFOter_9inw9Fnh_xDlj6t_9HacmaKSP7fCqpkgQVtsZ26GApgBhiAhYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0b5a4b97.mp4?token=qlwVIpkri_aXm89YrkMr338xNV5ZMSLX492EVrTn1xV6dnxr9n4dGUauMrfTeyXKvcAQLA8gz7LxwPiIAzV-fr3-ThoM9qbgCRpRIhnh_0UlvlIAfbMN_Gpd3c_m0fKYxeDZcNYOahM0dIcuTEi9pPl5ASUVOtCNC5eaLxyEeWJvPR5eY2OWxmrLmCf-XADjFYFOqOkMerK-UWh-za8BWekpwQthRrHa8zaIF1djpE0wwhfXeV2wIU-9qdeKUppBBwytBIdYLGzxYc3nmajVlEYGuxGnUJFOter_9inw9Fnh_xDlj6t_9HacmaKSP7fCqpkgQVtsZ26GApgBhiAhYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:
صباح اليوم، وفي إطار العملية "النصر 2" ومعاقبة الغزاة، تم استهداف قاعدة جوية أمريكية في علي السالم، حيث تم إشعال وتدمير منشأتين للطائرات بدون طيار وخزان وقود للطائرات والمروحيات العسكرية.
يجب أن يعلم المسلمون في الكويت أن معاقبة الغزاة مستمرة حتى يتم إنهاء نهب ثروات وموارد المسلمين الوطنية، وطرد المحتلين واللصوص الأمريكيين من المنطقة.
ولا النصر إلا من عند الله العزيز الحكيم.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86394" target="_blank">📅 16:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86393">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg7Efq5TZd9lHgxBoXmvI59siMyhd01uQLb-EdTvWXbIkOrwobVIieyKcTjw3MSNsQLil5DFwHwPlvMwk4U-kaCv6_4yrmqRh8zDfjYMctDYi28mI_AJx6iN96sijjhbsmZe1xPI56BYCHosBeF2CpYZ2foE1SUitoRRx6Ef8mY_8lk45gyOuJNdFMe1Zpb0CZpHhJ4cQSq5KTLIuUyp2keQcd1GgdHY2nl_MXHwBgtO_8cOXW-Toui2yLltMmpb3YeQ5iW-kYoapjcOmBcEc080yI2jLLo1Wi91xAEYZtDQkeDDWbpUI4fUw2VkNNGbAh9tkZw-xnDaFZF76XGj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇵
🇷🇺
اوكرانيا تزعم:
من المرجح أن روسيا استخدمت ولاول مرة صاروخًا كوريًا شماليًا في هجوم مميت استهدف مبنى بالقرب من مدينة كريفي ريه.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86393" target="_blank">📅 16:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86392">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇪🇬
🇾🇪
مصدر بوزارة الخارجية اليمنية:
لا صحة للشائعات حول استهداف اليمن سفينة في ميناء دمياط بجمهورية مصر العربية، الموقف اليمني واضح ومعلن وصريح ويستهدف النظام السعودي فقط لحصاره الظالم وعدوانه المستمر على الشعب اليمني.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86392" target="_blank">📅 16:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86389">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJeCdcbFDU4BPHV1OOBD8v6gIqmhc2ia8ANS-Gqerhaz_xwpHIEuOpU8hl5X55n8eHyAC196abnVBj86sKZ4F4YOmrP7v0l43IKQuOilkldlxfeNDhBxJPD0RP7_SnzTeSkdOJG_-4kfvpDIey7Be53MAWWYemecuWt1C5BHWDs9RLSRmY60KbwaGNnkgZ6WvVvpyHavYqTZT69f1PzUmFyPCaRiJ2A7hK_wsiG9KdyOVo7lAKqvbGV-XeoRCPJnEoP4wmoQcu3_rEBZpYTWToVYaZN_kgP9Iwi65cKdMl0aNbpW3s8Feh6-6o4fmSxiat4_WR9TJg7KngYEmTRISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5lZg6eJ9cr7ji6qVdC7QdoiJ6GfWHUZfc2x1V_84dpFj0b_STGou_zLUNGwBvVxvAz7rxcSxrykQYJIW_kn64JsYCVrQRhP0T2PN9VBImTGJUk9zepwlAbdpxcwrQDCgPu9cvsibcG0NsxN0lc2i8Y1RMviv5MkoQ61dnhUWWsqTL025bPAIfWLVv7Hd5dEIFpOE0LNCbx3PGGWG24fqOeps26s6Rl4TCG1IRo8bO30qXOgYBYQeugpF2--xvT_1pCTnF8Mhc9b7W4gMIqi2gCtC72N0Zrm7Ryr0E1vkRB_-JlTwBs9JDg5VuHYkDrF3l32vBMJBO5kNgqENK2nkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKH_uKUlIN1Z8QA4i3dPSx3yIqu_M6XyOJEOA_wdrjclqU-NUfxnFjQTg46ctAJyUgbz2tPISaeNePg9oaLdVHM1qKJm4plo1msyvMi8nOrOK6YuuPqC7867vHcBl7o_RBmMZpoy-hvz63WRbBQCN-xH36Kbzd6Iq5p6_8264za84_X0vUqjs17JcEom-yGRWKWkDCsaaGvkEeQukAIr6iCUyXtefKXFUabDhapbDNbVZmM4AhRt0JQmb04JtmBYzGGuFzbGSFnHp1H9e0arHQlmnwzF7_sh3G6bQsFbCJbG7Igs91SWy02uuqEJOxR00IjPOoEZwTGPkGN8AuOj_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
خاص لنايا |
هبوط عدة طائرات امريكية في قاعدة عيسى الجوية بالبحرين.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86389" target="_blank">📅 15:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86388">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية
:
في مؤشر يفضح مستوى التنسيق والتعاون الأمريكي، السعودي، الإسرائيلي، استقبل المجرم ترامب كلاً من المجرم نتنياهو ووزير دفاع النظام السعودي.
أن هذه اللقاءات تأتي في وقت يرتكب فيه كيان العدو الإسرائيلي، أبشع الجرائم بحق الشعب الفلسطيني واستمرار احتلاله للأراضي اللبنانية والسورية والعدوان الأمريكي المستمر على الجمهورية الإسلامية في إيران والجمهورية العراقية وبمشاركة النظام السعودي الذي يواصل حصاره على الجمهورية اليمنية وانتهاك سيادتها واستقلالها.
تلك اللقاءات، تكشف الدور السيء الذي يقوم به النظام السعودي في المنطقة العربية والأمة الإسلامية خدمة للمشروع الصهيوني ضمن مخطط ما يسمى بتغيير الشرق الأوسط.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86388" target="_blank">📅 15:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86387">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">النتن يتعرض لموقف محرج
🇮🇱
السيناتور الأميركي جون فيترمان يستقبل نتن ياهو مرتديًا سروالًا قصيرًا، في مشهد عكس حالة من عدم الاكتراث إذ بدا منشغلًا بهاتفه طوال اللقاء دون أن يُظهر اهتمامًا يُذكر أثناء الاستقبال.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86387" target="_blank">📅 15:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86386">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
إنهيار في جيش الإحتلال.. عناصر الجيش الصهيوني يتمردون في قاعدة سديه تيمان بعد خلاف مع قائد الكتيبة ويتركون أسلحتهم ويغادرون القاعدة إلى منازلهم.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86386" target="_blank">📅 14:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86385">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله أكبر
إسقاط مسيرة معادية في سماء ميناء الامام الخميني بمحافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86385" target="_blank">📅 14:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86382">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad4e6f260.mp4?token=MzYX7ZXu0D1fZwsnFysjSyxyldAmEk2kWfQM_nCmRqVzIdvej6O4GFQiOmo0-OFSF9LPz44mreWn8dLdpU7xKbCkJ9wCI1FiaBEH21G3UjKJSEmqYpq5Ss32khs5cmCzwuqjgcdOIhKhit9UxseQSHR33snR66APPXI6YgsmNrdeTo3OmBMJ4LgYRknXw4cWEc0ur1aPMWjasCQ77MZs2jtivOASVK_VsW8_NADYo3mdU5GYyNAXbQ1xq7C2-2SV5H4KsTAoTPzOt903v0cz5rbcJECZJS5lPBdRqn-NlWz2YDh4YOdsM3kRi69v06Xk7gMQAqe_IXXAERVaOxCjpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad4e6f260.mp4?token=MzYX7ZXu0D1fZwsnFysjSyxyldAmEk2kWfQM_nCmRqVzIdvej6O4GFQiOmo0-OFSF9LPz44mreWn8dLdpU7xKbCkJ9wCI1FiaBEH21G3UjKJSEmqYpq5Ss32khs5cmCzwuqjgcdOIhKhit9UxseQSHR33snR66APPXI6YgsmNrdeTo3OmBMJ4LgYRknXw4cWEc0ur1aPMWjasCQ77MZs2jtivOASVK_VsW8_NADYo3mdU5GYyNAXbQ1xq7C2-2SV5H4KsTAoTPzOt903v0cz5rbcJECZJS5lPBdRqn-NlWz2YDh4YOdsM3kRi69v06Xk7gMQAqe_IXXAERVaOxCjpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
إنهيار في جيش الإحتلال..
عناصر الجيش الصهيوني يتمردون في قاعدة سديه تيمان بعد خلاف مع قائد الكتيبة ويتركون أسلحتهم ويغادرون القاعدة إلى منازلهم.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86382" target="_blank">📅 14:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86381">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:
أُذِنَ لِلَّذِينَ يُقَٰتَلُونَ بِأَنَّهُم ظُلِمُواْۚ وَإِنَّ ٱللَّهَ عَلَىٰ نَصرِهِم لَقَدِيرٌ
أيها الشعب الأردني الكريم والنبيه؛ إن تكاتفكم وتعاونكم الصادق، وخاصة مواقف بعض المثقفين الأردنيين الواضحة، قد ضيق الخناق على العدو وجعله في موقف ضعف.
في فجر اليوم، قام العدو الأمريكي، بدافع العجز عن المواجهة العسكرية الشريفة، وباستخدام القواعد العسكرية المحتلة في بلدكم، بشن هجوم جوي على منزلين سكنيين في جزيرة قشم، مستخدمًا قنابل مدمرة. وقد استهدف هذان المنزلان البسيطان اللذان يقطنهما أهالي محليون، مما أسفر عن إصابة الأب والأم وطفل من عائلة شهيد، بالإضافة إلى إصابة طفلين آخرين.
ردًا على هذه الجريمة، وللمساعدة في تحرير الأراضي الإسلامية في الأردن من عار الاحتلال الأمريكي، قام مقاتلو القوة الجوية التابعة لحرس الثورة الإسلامية، في وقت مبكر من صباح اليوم، بشن هجوم على منصة إطلاق وصيانة طائرات F-35 التابعة للعدو الأمريكي في القاعدة الجوية في الأزرق، مستخدمين عدة صواريخ باليستية. وقد أسفر الهجوم عن تدمير كامل لثلاث طائرات من طراز F-35، وإلحاق أضرار جسيمة بثلاث طائرات أخرى.
كما أسفر الهجوم عن مقتل عدد من الضباط والفنيين والمهندسين المسؤولين عن صيانة الطائرات التابعة للعدو.
منطقتنا ليست مكانًا لجيش يقتل الأطفال، والذي يرتكب هذه الفظائع بوحشية، ويقتل عائلات بريئة في منتصف الليل أثناء نومهم. ستستمر معركتنا ومعركتكم حتى طرد آخر محتل أمريكي من الأراضي الإسلامية.
«إِنْ تَنْصُرُوا اللَّهَ یَنْصُرْکُمْ وَ یُثَبِّتْ أَقْدَامَکُمْ»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/86381" target="_blank">📅 14:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86380">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
🇮🇷
هزة أرضية تضرب الحدود العراقية الإيرانية مركزها مدينة حلبجة شمال العراق.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86380" target="_blank">📅 12:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86379">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
لمعرفة خطة تحويل الطرق والمسارات البديلة لزيارة الأربعينية في العراق التي نشرها الإعلام الأمني انضموا إلى قناتنا الثانية عبر الرابط التالي.
https://t.me/nayaforiraq2</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/86379" target="_blank">📅 12:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86378">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇦
🇷🇺
🇵🇱
تصاعد أعمدة الدخان من حدود أوكرانيا _ بولندا بعد انفجار صاروخ كروز روسي من طراز "Kh-101.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/86378" target="_blank">📅 12:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86377">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇪🇬
انفجار بمحطة الغاز الطبيعي المسال في ميناء دمياط بمصر أثناء تفريغ شحنة</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/86377" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86376">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام العراقي:
القوات الأمنية الرسمية هي المسؤولة حصراً عن الملف الأمني ولن تسمح بوجود أي سلاح خارج إطار الدولة".
القائد العام وجه فوراً بتكريم عوائل الشهداء وتوفير الرعاية الصحية الكاملة للجرحى، بما في ذلك نقلهم خارج العراق إذا اقتضت حالتهم الصحية"، مطالبا "بتقديم الدلائل والبراهين بشأن الادعاءات حول انطلاق اعتداءات من داخل العراق".
"الحكومة لن تسمح بأية تصرفات فردية من الداخل، وفي الوقت ذاته لن تقبل بأي انتهاك يأتي من خارج الحدود".</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/86376" target="_blank">📅 11:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86375">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
زلزال بقوة 3.4 درجة ريختر يضرب محافظة خوزستان الإيرانية</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/86375" target="_blank">📅 10:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86374">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebaAHucrttciZGV8Sz1jbRBwJwNIpHuH9DdyWIdnlE2zXuTKg3oowrc3gRiWa-jnVKsemhqgVWP5dVKsTMQ0v4N2wGmeSawHH62IwyYwUYqp1sJHrvY9tKlu_GVn-8pWvhnltd960T_qBD5RxZPmFgbgSzrc2shWsqJkf3ig1lSMLCX5JZI1PDenXUixw0aoSGG5xaeCXuIyvjlVu7sUo-m0nzf4vxKSGUKHSK5F_u55Q2pb7kGHFEYtEomm_FP0_vsFsdcDxJxo90noFZ_9B7EdHtJUmROFZ99UYj3QgqdXiv4suBcQDemOmy6RDOjn0KcPLIAok6NBCyuZDFhbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الحرس الثوري الإيراني: بمشيئة الله تعالى، سيتم اليوم معاقبة المعتدين.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/86374" target="_blank">📅 10:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86373">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الكويت: هجوم ايراني استهدف مبنى تابعًا لإحدى الشركات الصينية مما أسفر عن مقتل أحد العاملين، وإلحاق أضرار مادية جسيمة بالمبنى.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/86373" target="_blank">📅 10:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86372">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/86372" target="_blank">📅 10:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86371">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-dPVmMo9uKN4m799SaPj-jKM4oQSmel46rLnAyzWvYKWf099a3RFS9NjabJV-bocf3H1jbNKqMmCUg47LDIG_9FTJ1PVh-vXFRigK1DB3-0t64MmTOqsg4j-5XPsnhMHXFdu6hlymD5zm2_xYWRSuQv_64YiTZBYZwwT6B4W4CjPgQ_tooCZhJsg0eUqGiwMWjXxZNwfiCKAAj_WqyVYFc9oE3a1jGOIZTOEHQ9JlJQPlRQEllZmZ8R7VctKRXGymDI7wwCcr40LY75DproKXPYmEE16mn9_5N6pHHxaJkKGKYa1-tXKtYSAJn5tqLo_2EKrnJxWLK3-k9BtUmhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد مقتدى الصدر: عدم حصر السلاح بيد الدولة لا زال يتسبب باستشهاد المجاهدين في الحشد الشعبي والقوات الأمنية بلا وجهة حق.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/86371" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86370">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB0suQx1dH2tzCrATzVKyXNVP4SguqhWdOWPGzSTC57mDVHsGbTseThCl3p_OWj44kPW6fMN6jODf-mO5VU5F_v6d5C5BOmlhqvElJIUZ_Q4cFEO3NzW3YtuQks5q6fmNzEPI_rra-keh-rF74KtzQC6vfbkg2NiBfQ4DdP9RCy0Q8_PzJr4bIWdCMt2UIZBX8np00Zqc5v_nTykGkrIM1CdKCMjz6dVRk4_sTB93lVq6qBiPuHfwVXJe0hLKH6RqPXABfhTJTCqszep0CTuoEHPJjERSl5_O6PIbKZ7h_bwzNlBca_Qb6754OXzbtvu0jtze9F3IRCc50obqctdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار النفط بالارتفاع بعد تجدد الصراعات في الشرق الأوسط حيث وصل سعر برميل النفط الواحد إلى ما يقارب 93 دولار.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86370" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86369">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شركة أنابيب بحر قزوين: تعرض ناقلة نفط لهجوم من طائرة مسيرة أثناء تحميلها النفط في مرساها.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/86369" target="_blank">📅 09:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86367">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شركة أنابيب بحر قزوين: تعرض ناقلة نفط لهجوم من طائرة مسيرة أثناء تحميلها النفط في مرساها.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/86367" target="_blank">📅 09:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86366">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8NpnJGDyu9jVRMtB8w1ZiC5DwGFOqE15XaPaWHox_oXGeT7Ka_rljnpjENsGlCATmlmSql9_q0eqpisqsZW6X00gieel8g_AFYlA-Km-uLEV2_aMVdjURuPJWRbvjYt3boZkeY6jHNNM8I_JYj1vb5FOSk01T4xPqKUgPo90wHc7Ieip62ConJC4CA9LO7bAJc_SX1lXQq8iKXqNI4CHR56feepQHNNCs1GMvtGJkA3h4kVNPb9T7BuGHmycV-kDqNHtrZm6u5z7v7MG6OnqsDRvTP9fLvnokJgx76QwQbV47SWRJ6EETD0Uz-4VFiVZIKTjiZFAt8Tc2y4Pu31zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇯🇴
بعد فشل الدفاعات الأمريكية بالتصدي للصواريخ الإيرانية ؛ تظهر بيانات الملاحة الجوية إلى أن طائرات عسكرية ألمانية وفرنسية توجهت إلى القواعد الأمريكية في الأردن لمساعدة الاحتلال الأمريكي في اعتراض الهجمات الإيرانية.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86366" target="_blank">📅 09:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86365">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86365" target="_blank">📅 08:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86364">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86364" target="_blank">📅 08:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86363">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:
الليلة الماضية، حاولت ناقلتا نفط، استفزازًا من طيور أمريكية، مغادرة الممر غير الآمن جنوب مضيق هرمز، ولكن بعد اندلاع حريق هائل في إحداهما، عادت السفينتان أدراجهما على الفور.
مضيق هرمز أرضنا، وبحارة البحرية التابعة للحرس الثوري الإيراني يسيطرون عليه سيطرة تامة، ولن يُسمح لدخيلٍ قادمٍ من آلاف الكيلومترات بالتدخل فيه. وبعون الله تعالى، سيُعاقب المعتدي اليوم.
ستتلقى الدول المتورطة في مساعدة المعتدي ردًا قاسيًا إن لم تُصحح سلوكها.
لن يُفتح مضيق هرمز ما دامت مبالغات وتهديدات المسؤولين الأمريكيين وتدخلهم في الحركة البحرية بالمنطقة مستمرة، ولن تُؤدي التهديدات والتدخلات إلا إلى تفاقم الوضع وتعقيده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86363" target="_blank">📅 08:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86362">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2411719d9.mp4?token=FvZTYyqM8kP6NMl8BE1moCE-jGKurODQA4D8R7tcJIbLn6jlatXNZvWKvEgJZ323z13K-X1DOAk8Yf2AUE7HgEiR-5d7rv9xb81BbUrrQu14tRcx7I_fDLnfLyA6wsb4iwbQNfZjRpUZDqdvceYKMnMCvBAIcXNEKl7h2ELkmYh7J1vDAEk0ORfUku3VDQNW2T2edH8e_FZ2-r8Ai-657QGxoLa6OmhveWR_7IuLV4D9GdRSL1bkBW3HgVtE5Fw7jLXoUXRBp0va_7Vy3Y5mLlKGnYwGq8f0cnms_BBFziDGd0klMfmYuxOQaPmipFFbwggR9QLc1b29wKTLV4ITmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2411719d9.mp4?token=FvZTYyqM8kP6NMl8BE1moCE-jGKurODQA4D8R7tcJIbLn6jlatXNZvWKvEgJZ323z13K-X1DOAk8Yf2AUE7HgEiR-5d7rv9xb81BbUrrQu14tRcx7I_fDLnfLyA6wsb4iwbQNfZjRpUZDqdvceYKMnMCvBAIcXNEKl7h2ELkmYh7J1vDAEk0ORfUku3VDQNW2T2edH8e_FZ2-r8Ai-657QGxoLa6OmhveWR_7IuLV4D9GdRSL1bkBW3HgVtE5Fw7jLXoUXRBp0va_7Vy3Y5mLlKGnYwGq8f0cnms_BBFziDGd0klMfmYuxOQaPmipFFbwggR9QLc1b29wKTLV4ITmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
جثمان الشهيد ليث علك أحد شهداء العدوان الأمريكي السعودي على العراق يصل إلى دائرة الطب العدلي في محافظة ميسان لتسليمه لذويه وتشييعه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/86362" target="_blank">📅 08:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86361">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1726eadc79.mp4?token=AgORI1p2Ef5s4v6qS0HoKc1MVezpTINhFqH7rwXyuBjGuM_97LEVmYM-bPSFGca3IJyxvWkcG3RLIZkgU97ZzymYuWZtszcJMI4Gd-YD6zsTR8KKJ3bLp9gYMK8qbytJ_OHN3e_3RAO__qtTLnu1yrrkhST4bPvPk3Kq2wl7Hf0Zbmv9HgChUuc3KBlqSdxrKM10ef-k-cjSXpWwgxBpFSrRfTSxxl1Y3Q5ff1lem5-Mea9WJmylaqZXC1X4N3DSlJEX9IOtliByWKoqaWcYLhVSr7AEI1kcD9N1Ap7GXgOEzTjJJWVUhZkoa1sKQ3_h5mg-BMgBYG7MBHucJ512zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1726eadc79.mp4?token=AgORI1p2Ef5s4v6qS0HoKc1MVezpTINhFqH7rwXyuBjGuM_97LEVmYM-bPSFGca3IJyxvWkcG3RLIZkgU97ZzymYuWZtszcJMI4Gd-YD6zsTR8KKJ3bLp9gYMK8qbytJ_OHN3e_3RAO__qtTLnu1yrrkhST4bPvPk3Kq2wl7Hf0Zbmv9HgChUuc3KBlqSdxrKM10ef-k-cjSXpWwgxBpFSrRfTSxxl1Y3Q5ff1lem5-Mea9WJmylaqZXC1X4N3DSlJEX9IOtliByWKoqaWcYLhVSr7AEI1kcD9N1Ap7GXgOEzTjJJWVUhZkoa1sKQ3_h5mg-BMgBYG7MBHucJ512zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة لانطلاق وفشل الدفاعات الجوية في قاعدة موفق السلطي في الأردن قبل دكها بالصواريخ الإيرانية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86361" target="_blank">📅 08:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86360">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86360" target="_blank">📅 08:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86359">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86359" target="_blank">📅 08:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86358">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
مراسل نايا |
سقوط صاروخين بشكل مباشر داخل قاعدة موفق السلطي وتصاعد أعمدة الدخان بشكل كثيف وسط فشل فادح للدفاعات الجوية الأمريكية واستمرار دوي صافرات الإنذار</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86358" target="_blank">📅 08:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86356">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpwBvInB_3FJK9kxYVVQaLQOpOmpl2ZhCtOF-2RxUXIO23BfmPtPkNzVxxikq9mxgLU2py6YpVZitMEAB-wwZuY9jN99UXHPDZ1Gbyy0hZ9j--0C7m_N7tpHuvNX8w4Hqwt35eWqg20Xukhct_Ilkww7wefcjL2LRNQUMeK3h3GhpxHlJ3Rh1xqjHn5GpviGEKZd6jrtGzOH97PJ8QHWtiE0i5kxYZrx2ZHAHK-LybPiyY3PF-YOU28qJizhwvFkRXrR_p6NGokSaTGa43Qu-XIQcA_pvqzyAmU-BIhqecipnTbpWkYZPRvA8pjXiVXahyN0fXctZPcQVe2QiSGpiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-RwMotlcnE1O2K7a7uCHQ3w7E8vNHHn-lxSkRhpswX5lX8ZwXhe1zXG0D62AoJKgDPl2HKIgZGCgVyf4V-Knmrop3_PdJXUjlSBFOh_4mKYQ_QF28QsUiHA2jyEVhuar0MEmvVNdGCh-q5iBnL_VuYWXoqu4bUUAR31dbBFU_2OoFfvo-oflFL6H-6x1KGVRSq3kntklT3MFgN1F5rgF20nP0-bMFgsq8nBehorw5iJVwcRNUMLpuUvqTrYP7GrqlKYYCcVKzzDXPHuua31rzpbEVBQb7sVQlKEb1MiRLEP0w8KaZwDCdgweiJhEbSUiFC7JJCcz5nDJCpE0zI2mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الدخان يتصاعد بكثافة فوق القاعدة رغم المحاولات المكثفة للدفاعات الجوية لاعتراض الصواريخ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86356" target="_blank">📅 08:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86355">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86355" target="_blank">📅 08:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86354">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378eb493eb.mp4?token=WaxDYvMWdh__KNIquCL-E7vwShQpl_iwps14I_mDOMku7rHSQpkYtdYKT6DAZred1KF24BPG9biQyGQZ0b07rt2y_bkjP0A-TVuudmUMeQvCDD_hLZDslxU4JdvvkeTUla98XeCHWD8FzeLtgCz5k-Mf82GMLokochM3XgQl75uGr0XjLajLUZBsgf3Irmlq6PX-R0sSKuLbxkg1z-gNhcnC3YjAo_6TqGcV2AcJlndr7-HjLWSjic0qDu3YKIMLoxwVi2IAns-fnSJh-gvNoIUaJYHk9Jb82T70C9fqxSOjG6lI_GOvQGyjnQ_6mxhB2KTfMPmXnG0i05ozC8hJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378eb493eb.mp4?token=WaxDYvMWdh__KNIquCL-E7vwShQpl_iwps14I_mDOMku7rHSQpkYtdYKT6DAZred1KF24BPG9biQyGQZ0b07rt2y_bkjP0A-TVuudmUMeQvCDD_hLZDslxU4JdvvkeTUla98XeCHWD8FzeLtgCz5k-Mf82GMLokochM3XgQl75uGr0XjLajLUZBsgf3Irmlq6PX-R0sSKuLbxkg1z-gNhcnC3YjAo_6TqGcV2AcJlndr7-HjLWSjic0qDu3YKIMLoxwVi2IAns-fnSJh-gvNoIUaJYHk9Jb82T70C9fqxSOjG6lI_GOvQGyjnQ_6mxhB2KTfMPmXnG0i05ozC8hJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد للاطلاق الصاروخي الإيراني المكثف الذي يدك معاقل الاحتلال الأمريكي في الأردن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86354" target="_blank">📅 07:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86353">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/86353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86353" target="_blank">📅 07:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86352">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQAKGk_xuLPLX_fgwaSFSnWUmDXNHcIWrKyrZ72s2BWMfGWBXlvQWUpkHiOsEFUslmUkbGtmJHQdRgsN6E7TKyGLYoTE3geXIAXNtWPk2b0fPGDS1k46fXPICNNKRImYyB0-dqX91Bns5lR75qEmFK-ypmNNRhcbeZaU9POQMMJYhbOU2fG8ftHZlBIVeSEMcLIbuPkJRe0-WvKMFP2wxOc4BIs7KXJz1pdV7I7uUmiLMhVBJYAuATY4CeXQ2sp4-wnCTXm95qof47EimgqFRvHD83Y-6FEou0BA0kWVfbc7vBZOkl5Er3vKKd9EssbNKSYRni3epECsBTEoJx4VfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الدخان يتصاعد بكثافة فوق القاعدة رغم المحاولات المكثفة للدفاعات الجوية لاعتراض الصواريخ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86352" target="_blank">📅 07:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86351">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86351" target="_blank">📅 07:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyLKM9ZxUw-wLflPRm_QDUfKX6lNST2m8Fzm20UKIJOeDfNn7SVGrC9HRHaI1PsxCjIiiwlNJXVXVF6g5gHiGg0WLdnvBBVui5qKXsvu1CL8I8SY52u0ONoWxMUMcpEj5nb8OaT6GVV_trIUg3KTaIPCk0jFwBDHvYcXNoZrhJf7T3HejwB_M-minzlTbLSnXBSB37JF71zeRtW_79VFnkBS6uT5V47XyuG3j8L8_iEwQdtdafbx6X5TsWp2j2fesarh3viRS1uf-P0A8Y6wl_helvl8Zs_TFirXLD_E2jUIItGPFpdl6vJtXMd4Lbn7pIlK3b1Ew7zvZiJPBHLdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86350" target="_blank">📅 07:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86349">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjBq3Kg1JulHOS5eDrL4RvPB4gyPs66isMIe9jKwW_d8nIgcWvrySJDWh62FWZxChT9jVA3PCOa4Z6iH90nCwF6h_jhYuc5xzVJOfBc0Fbso_kS73cVtE3j5iX-kI9i37on-tFlWFAcUR-i4yDyuhxcP07tocynsbYdvvE0Eczqo02LOfT5zc0k3lzTGFBImcpXBoXVpofKENhJohB8aM83t1uZpOQhkLXo_2mV9uAAuWYP9FdKfwpWA2BuwiZb6L2yq9MiFRzJSVdDo03n75TYGzC1OB3rVLHYVyNIUE_1jdgGSG_uS9cV5Xn7NErN0VslBVpXItw-IOn79_vmohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجات صاروخية مكثفة تنطلق من إيران</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86349" target="_blank">📅 07:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfb4b4712.mp4?token=DpBnkjPRrQIE23cxqFdESehD1gJORQoKGz6wB3pfjcWUJrUARroyg_6JHIxANYombxJTJ7_I6gMLwOU6DOtd2bd0BYk4Nm03VLNtYKY9oRJh6dtyy_WTNDD95jRTf8V3eqXufEwUmmgLle3wyK3awFepaOg9-QkAauqgfEg2qFgR6RlQfDCKnAjqzXdaZbGNmdM8ndVP3XZ0CxWOSoHmCcPeE3XylqfkmqvbTQeOvCDqLba1Si79FXlUmUObxd2OBm1iCxzt2nvw4tw_PxlXLAsv8Oc2j8GxGE6oOZ8Yo4KYKSKh7LAGQ_94R7LctlyWYtMUhwakXFtUUpZpHQSNvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfb4b4712.mp4?token=DpBnkjPRrQIE23cxqFdESehD1gJORQoKGz6wB3pfjcWUJrUARroyg_6JHIxANYombxJTJ7_I6gMLwOU6DOtd2bd0BYk4Nm03VLNtYKY9oRJh6dtyy_WTNDD95jRTf8V3eqXufEwUmmgLle3wyK3awFepaOg9-QkAauqgfEg2qFgR6RlQfDCKnAjqzXdaZbGNmdM8ndVP3XZ0CxWOSoHmCcPeE3XylqfkmqvbTQeOvCDqLba1Si79FXlUmUObxd2OBm1iCxzt2nvw4tw_PxlXLAsv8Oc2j8GxGE6oOZ8Yo4KYKSKh7LAGQ_94R7LctlyWYtMUhwakXFtUUpZpHQSNvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الاردن بعد تعرضها لموجة صاروخية كبيرة استهدفت قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86348" target="_blank">📅 07:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86347">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad1427d80.mp4?token=fhMBqVaZExzmxTjTpvhc6R-v_3KskL8QezubmIYP8l6gZifKXfASN4nftnMJDEFAzMSNxRi3z2r0WRz7-NjW1go6-ER2mjGkGSoHK2MUIEa8y2csOFLkF7_26n19ZKpWrfPAI801JsHyD8iVaDwwQCM2riGMctWXVMVBoSmlOxMUia--8icf6KdhvFd9dSMj-MCvsKU9Cv7r0_LpdCGve1K4xpbgz1jxFg81ePeMU9or9_kjPI0-CFj_13vGfLAcc5lbXQ39wu6lK_xLyA2Ld_m-k6I_uPyG87EHwkPhxu0b_pYFnp0f5CzvPqZMrHK7cjR3eFDO69MBnRpgTrZn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad1427d80.mp4?token=fhMBqVaZExzmxTjTpvhc6R-v_3KskL8QezubmIYP8l6gZifKXfASN4nftnMJDEFAzMSNxRi3z2r0WRz7-NjW1go6-ER2mjGkGSoHK2MUIEa8y2csOFLkF7_26n19ZKpWrfPAI801JsHyD8iVaDwwQCM2riGMctWXVMVBoSmlOxMUia--8icf6KdhvFd9dSMj-MCvsKU9Cv7r0_LpdCGve1K4xpbgz1jxFg81ePeMU9or9_kjPI0-CFj_13vGfLAcc5lbXQ39wu6lK_xLyA2Ld_m-k6I_uPyG87EHwkPhxu0b_pYFnp0f5CzvPqZMrHK7cjR3eFDO69MBnRpgTrZn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لمرور الصواريخ الإيرانية في سماء المنطقة قبل وصولها إلى شرق الأردن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86347" target="_blank">📅 07:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات تهز قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86346" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86345">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86345" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86344">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBul0XeKidtJnUXlGbBRlaE0Ho-UxZ6R7arlYL1XGDuIsxAIggWtdguI5Dm3xD1MRLf8q4qUwYI1CwUL3_-8zd2UuEzlmWSUkZmXNjAu42vOu_N-9OzwjQDMF5W7_g4j6B8TOShXlZ73Q7qp9deZko_nHl7B5c0yWsE_JTjv_5ZhDnUW1HCG3KNmGTSKd0wYb25KdEi2LA8STQQqkQwUQBxwqdSNia7ETjDYiPkahBGufADxKhD1pB68cRN79GXA8DCfOFFFa7gxs3C54Jldqoyf0oq1S_KWY-RHOryFWAEcA0GFtObXwAC6WxEMUzcIH1CP3j1S10N36N-8zbQOyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد لمرور الصواريخ الإيرانية في سماء المنطقة قبل وصولها إلى شرق الأردن</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86344" target="_blank">📅 07:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86343">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/86343" target="_blank">📅 07:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86342">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/86342" target="_blank">📅 07:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86341">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot2X1RaaGaceh5OHR8P1STYIZkrqhc9R0k0uORGyHgWp3R7OKhU68ayMLceWmuXnK5Sw4ZLI9ExNL-Ta40TWEiey4lTbIsFhy3ErwSf4ucwscNshr5P62Hpa0o_XtaQ-vcEHiHjEEqFjlZkhgYkJvP3EyEth2wVjsbYhwi2_vXDNAsvkZlXY7jwWYnIm7TxziTZffgzI_FQ45mC-l-fAsHl_n6K-Val6Luh32p_KnHp46sCknTQP698TAYy904MxYfMsQyAsmHr4YuL4-QnlNarwJAo6O_WkdqhAW9bXwET0AZdDAcA4zKR-V_y3MH8XLwQ7nhNk2LuNFfCcfccZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ في طريقها لدك معاقل الاحتلال</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/86341" target="_blank">📅 07:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86340">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaLgRLwSbfKk-97JyjEbzxDAv1pL6e9OpaB5783L9JDqoOVQ50u_eY-6fai_F_Sxu3KJNoq1lPxRrSqatooSRAQtrQFu49X5ygUyZC7-PYSjGfeLAIpmjm2TmNef4uyQ04ouAnPY2yolwebaTf6F6H7KbMMmw-hP1bwtqxNJel1mWX78epc4FymVbus2fV0fco36MgnY10t8MeA-0hYSNFsko2sqWtWHRZSfioEYotp0U5Mk8zKHugVIYukHl4LYJ-PUilIxJz2LR3lsuRIqErcqDeXVN7uEo27JtYk1DeLh38bGkx1nRmdpgFfG6etx-5eXaxAZ6MHAnwYwTn8vEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ في طريقها لدك معاقل الاحتلال</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86340" target="_blank">📅 07:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86339">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/86339" target="_blank">📅 07:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86338">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">إطلاق صواريخ من إيران باتجاه معاقل الاحتلال الأمريكي في المنطقة</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86338" target="_blank">📅 07:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86337">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5367294f98.mp4?token=CN83SUrsSLjmuhoK1VYG9LIJBEv4XewQ0czQGOvYufnMAthIgpZX5VmY29I3cugtdmVYd4JhbWAGZYEBgJNj4E9L8bmmJPE6hXJ21AKSkiiR4ljeR52GxfF4pSpO3YAr7blHEpss0pUTyg-XvavUVRgyxjmqsc2l0TJ-n-BG1PWYnUKvOpC0OOA-fq1XDd59xTgF3ah7-AuVYYAQuD_gLSsQRWjK_dotVL6YEfmn2cV6znFnyW7Mp62ZmhHhhFlEpjxvGUiq1fOmRQ6YW1sIYeZwPx4Mv61jav3XZDGGn-Byo486b3tFO8hsySCtZy9xiTFtRyPBYPb9ooJhb_jJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5367294f98.mp4?token=CN83SUrsSLjmuhoK1VYG9LIJBEv4XewQ0czQGOvYufnMAthIgpZX5VmY29I3cugtdmVYd4JhbWAGZYEBgJNj4E9L8bmmJPE6hXJ21AKSkiiR4ljeR52GxfF4pSpO3YAr7blHEpss0pUTyg-XvavUVRgyxjmqsc2l0TJ-n-BG1PWYnUKvOpC0OOA-fq1XDd59xTgF3ah7-AuVYYAQuD_gLSsQRWjK_dotVL6YEfmn2cV6znFnyW7Mp62ZmhHhhFlEpjxvGUiq1fOmRQ6YW1sIYeZwPx4Mv61jav3XZDGGn-Byo486b3tFO8hsySCtZy9xiTFtRyPBYPb9ooJhb_jJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحليق طيران حربي مكثف في سماء محافظة ديالى العراقية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86337" target="_blank">📅 07:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86336">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bedb34f2c1.mp4?token=XjutqIuEV6m7fnUxQdaWxy1W8Hrcf40rKrA2q_AozhBuv3Yh211uO6-SayGJao3lE6lE1o3aLU1-0UC2xaZZ0W5vJ7HlCCMQqTcK7zGw6SQXZKukSRhb9XD6wWrzeyeRm0ULn5GVqJRDzwdas2bvzkp5cVhSkonfe1PJByF9vL4tkAXWsqdtV9LvilBEa5Z2pTdpIRZ_26W8zvISfYDgz28PX9SdwGc-jbTJNXbIAuuK-2WeBhFAbCb-s3Mrg7CVkZnie-Zl1Uy_KTB-dHgLb1QiIpLWUhMiCHpPzXeXyltKWDGfQzfpMoJbAHJvPmc1-GGwTNxJwzdiDFqePSBx2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bedb34f2c1.mp4?token=XjutqIuEV6m7fnUxQdaWxy1W8Hrcf40rKrA2q_AozhBuv3Yh211uO6-SayGJao3lE6lE1o3aLU1-0UC2xaZZ0W5vJ7HlCCMQqTcK7zGw6SQXZKukSRhb9XD6wWrzeyeRm0ULn5GVqJRDzwdas2bvzkp5cVhSkonfe1PJByF9vL4tkAXWsqdtV9LvilBEa5Z2pTdpIRZ_26W8zvISfYDgz28PX9SdwGc-jbTJNXbIAuuK-2WeBhFAbCb-s3Mrg7CVkZnie-Zl1Uy_KTB-dHgLb1QiIpLWUhMiCHpPzXeXyltKWDGfQzfpMoJbAHJvPmc1-GGwTNxJwzdiDFqePSBx2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇱
نتنياهو حول إيران:
لا أعرف ما إذا كانت الدبلوماسية غير واردة، ولكنني متشكك في طريقة عمل إيران.
إنهم يكذبون دائمًا، ويغشون دائمًا، ودائمًا ما يماطلون.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/86336" target="_blank">📅 07:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86335">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
وول ستريت جورنال عن مسؤول أمريكي: الضربات الأمريكية على إيران ستكون أوسع نطاقا من العمليات التي تمت في الأسابيع الأخيرة</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86335" target="_blank">📅 07:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86334">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34643c0e8.mp4?token=ns8A_XMYrubLEupaI0upPKMBWqd6VkUenLifKkuop4nkjnXYAi8wCl7RpkzqWL8DjmhR6QenAnXYd1_4GBKa4dSmtxt3w6vF-RjKHsxiec4Ao-iWZ7PIUdSsV3fAmxlDhlXRZnhzYrdhbaixLgc731X5JmSqbpCzTGbvOWokWnOAWYJh7gYaKE81NmJvdzXhTHGuGytIG9zsrXVEbnetm8ly9PmIF1KVHwkpjkriq7s22BRLtDRT5mIr9GYKFX6Af11E12v4fA4F_YwpXjO8UujZqxkG-yHVyM0KAAO9VyvKFVwrkNRvK5ZS5AxoKPqk3HtEJGj1SkkDt9aOfrkzBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34643c0e8.mp4?token=ns8A_XMYrubLEupaI0upPKMBWqd6VkUenLifKkuop4nkjnXYAi8wCl7RpkzqWL8DjmhR6QenAnXYd1_4GBKa4dSmtxt3w6vF-RjKHsxiec4Ao-iWZ7PIUdSsV3fAmxlDhlXRZnhzYrdhbaixLgc731X5JmSqbpCzTGbvOWokWnOAWYJh7gYaKE81NmJvdzXhTHGuGytIG9zsrXVEbnetm8ly9PmIF1KVHwkpjkriq7s22BRLtDRT5mIr9GYKFX6Af11E12v4fA4F_YwpXjO8UujZqxkG-yHVyM0KAAO9VyvKFVwrkNRvK5ZS5AxoKPqk3HtEJGj1SkkDt9aOfrkzBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇷🇺
🇵🇱
تصاعد أعمدة الدخان من حدود أوكرانيا _ بولندا بعد انفجار صاروخ كروز روسي من طراز "Kh-101.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86334" target="_blank">📅 07:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86332">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHiHFaNa5ZX_p8ciB_w4Epeq2qNsTwx5K4UUwaGXZKVPGno8O24vjIOiPQ7-GsrpFbDiz2cryMub75c4z6f1-qFjlCjNpu-XA7AJGCyoIOOgSyca6DGZtmGiObvPC85HaN0gzyL6awZ4t32Nh5N4FvfBHDYNIJHatvfpWVzbCSmBO1Wp6NhRcjj8m1y21K7qNaf6BFQw8qOE_GeGFLDzQAe7AxRF9BcQ3F_IdeDrQYBILUX8CyUy1sN7XYgULYtN_RrlhE0tHZqWIhD9DuoRsMcO4LisSHUEJlm6hgG5_QpeeMY2Nq1EMHoQ0ZNc2XzuCfeqEcYVUM86rNu81e1pwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7452bf19ff.mp4?token=mhS-trQgC00nfjngsXCt344HNe7smgCtLNJ_PBLsTxrm6XA_F_YDvSJltMfxVJ1wmOD7i4PiE1XGz7_BR3oSpulQeT7rU46z1sdhw95YSEkORkyUSt7G3S25ij7RZryKDm5-lPcUyer6wOnkd3vz9PN9loyXE6ztCaV4mVpVfkSpHcT-GCa3qY-Am0rYTcQQKtECT1_ZlnZNPtja6MXPlXuLhvP5aKiIKI_7Vb9r2HsgsBNxdNN24NL2ho7B1qFpqS_KogP6YjlrJZnd1P5VVIFnKXVixyyPLSgP7ibhslb1l_OelLzYnbMpCdEkFTfMzJ6heVmo6hDO2-OEMOI_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7452bf19ff.mp4?token=mhS-trQgC00nfjngsXCt344HNe7smgCtLNJ_PBLsTxrm6XA_F_YDvSJltMfxVJ1wmOD7i4PiE1XGz7_BR3oSpulQeT7rU46z1sdhw95YSEkORkyUSt7G3S25ij7RZryKDm5-lPcUyer6wOnkd3vz9PN9loyXE6ztCaV4mVpVfkSpHcT-GCa3qY-Am0rYTcQQKtECT1_ZlnZNPtja6MXPlXuLhvP5aKiIKI_7Vb9r2HsgsBNxdNN24NL2ho7B1qFpqS_KogP6YjlrJZnd1P5VVIFnKXVixyyPLSgP7ibhslb1l_OelLzYnbMpCdEkFTfMzJ6heVmo6hDO2-OEMOI_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری دیگر از حمله آمریکا به شهر اهواز</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86332" target="_blank">📅 06:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24578ec2c9.mp4?token=KKL_OUVr-zD7dokzgOjuUOxcV6PnSa8ogDd9CSYzKoxCX5CDGvYlBF7xQTv6qRsqwg9NYMD9YRE7f1QbxlZu4ZHgpePBggOVrL8uSY9joPBga3f3vynCDwoegG93KAznHAWsX86iX5xTSRT-pxHD6w6x_pjQpcPpB-CQdLlGBfiMe2FXpm7cPwEQ81KMny9ViXiUG4vlBaeyZ6Nfw0ojDisRk-e9WHfseiaOnDRUf8pyYL5uoY4UwCKdg8ktB3-BcSn0s2xsQe96KPe63HEtr-gjO_w8poJbhPyRmt4SpIt4nl13iav2NCfy8khFhOK1y4n8WvdBWFFnN4Ofs13J7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24578ec2c9.mp4?token=KKL_OUVr-zD7dokzgOjuUOxcV6PnSa8ogDd9CSYzKoxCX5CDGvYlBF7xQTv6qRsqwg9NYMD9YRE7f1QbxlZu4ZHgpePBggOVrL8uSY9joPBga3f3vynCDwoegG93KAznHAWsX86iX5xTSRT-pxHD6w6x_pjQpcPpB-CQdLlGBfiMe2FXpm7cPwEQ81KMny9ViXiUG4vlBaeyZ6Nfw0ojDisRk-e9WHfseiaOnDRUf8pyYL5uoY4UwCKdg8ktB3-BcSn0s2xsQe96KPe63HEtr-gjO_w8poJbhPyRmt4SpIt4nl13iav2NCfy8khFhOK1y4n8WvdBWFFnN4Ofs13J7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار عملية البحث عن محاصرين تحت الانقاض جراء عدوان أمريكي غادر على منطقة سكنية في جزيرة قشم الإيرانية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86331" target="_blank">📅 06:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86330">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEuZHcOO9iClTHhwFLT7KI_pebgZVknTFFIOLzq5LoJ53Pnol3HkewQ4Yysr0JHRd4hvBXKC6X-vq1MCbNwu8XLfhljZKU-b27P2T1S1s5fsoLyFV85LqmIvgd7P6AHPqkcAb32cWAspRPaBFYjxYKBlaecSRwXCbxlNB2G71a4sy8EOQN8ZRZlb48Zk55PL7zk0P3VF3b7YHHvmpCdvAPBGPyT2_ZfB0RR3DcWvhOf5_-FWVLr5E0a-BHayGiTz96iNb6qyPZcEit6BOWC86TDkqq9SJ4Vf-eki-euHFB88-sxdffb3COC0W5p6FQoAtbBWBCC5X5Gawo7UI1dZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
يُظهر الرسم البياني انخفاضًا حادًا غير مسبوق في إجمالي مخزونات النفط الأمريكية ("الأربعة الكبار": الخام مع الاحتياطي الاستراتيجي، البنزين، نواتج التقطير، ووقود الطائرات) خلال عام 2026 مقارنة بالأعوام السابقة.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86330" target="_blank">📅 06:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86329">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ocukl-EnEwjl7PNFfJ_mljF5E-8WgY_YXXCb01B3G1JUXMrZCVdZ5uen-qPnVZj5QrAliYLOaPKYlSWLRDK9UD49btmttehDk_eGkYbiV92UtoOgfd-wREOhTbb8YwVCo1lVpjNGANjCmBp84avUsG3K0xRKR0JaSExXBm1o-2vBmkfj9QVyiMGotLt8rbJ86YSmTws1kil-uM6cT-AS532hFY5_UjjFps3KZok_3BRphhO2wAAJwmIVOQfBZbTlsffDO7yA3or8vlqwmYxk_hE8SWhI_r9s-7XJQ_wfZ0zL3Rmm7gbFa_NFvmUIFHpl0e_wPPrRV1Dz4ESEB49iMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من العدوان الأمريكي الغاشم على منطقة سكنية في جزيرة قشم الإيرانية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86329" target="_blank">📅 05:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86328">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd89ac439.mp4?token=WAkWAnFDRvKC9uezaVx9yxjtjakxs2aWjcWo_2X1McComaUN1w4RdFN9O75XMyvSoqUCognlOwggQxM49xEpLZJ0cuj29HAzeGMMLiNlhoEPiC2Lrr3gnWDPyT7DRQbAFmU1sJu6W-y4tCVnKITxvZPIExMsJvP0cLeIINW9S5t7oT4zFdAKIG0MFbprYswDcIFBmSHsUkppC7NpU6qjRY3TZKaGMl8WppAvLIqhAzAW6D5yK_tjUxhRD6IJ2AaZE7b4B1yDoNtDY2AWsCS7-lnnnWwfH3lVPHyarJX4Vngziaz6A3tepGcKqQe10sQ1H05dYAOU1Bv4Np_RTVACfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd89ac439.mp4?token=WAkWAnFDRvKC9uezaVx9yxjtjakxs2aWjcWo_2X1McComaUN1w4RdFN9O75XMyvSoqUCognlOwggQxM49xEpLZJ0cuj29HAzeGMMLiNlhoEPiC2Lrr3gnWDPyT7DRQbAFmU1sJu6W-y4tCVnKITxvZPIExMsJvP0cLeIINW9S5t7oT4zFdAKIG0MFbprYswDcIFBmSHsUkppC7NpU6qjRY3TZKaGMl8WppAvLIqhAzAW6D5yK_tjUxhRD6IJ2AaZE7b4B1yDoNtDY2AWsCS7-lnnnWwfH3lVPHyarJX4Vngziaz6A3tepGcKqQe10sQ1H05dYAOU1Bv4Np_RTVACfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق أخر من العدوان على مدينة الاهواز</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86328" target="_blank">📅 05:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86327">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49818ac28.mp4?token=PzY_fvxyozvVqIGdVefpe1zuFoP2pkDDX_J5dVTouBhOuw9Rx3NzZkqqu78RXpMk9PYoc9OsDcf5_6T5vDXNF0WCCMYNgfbyM3motSu3qAXYNWB_0mFlrpL08_aW1yutdLdrO02xEZSiZAn2jRpHUIoR6YriyvvMQpkM4NK9c3o6m0oINJyynNFVy2k3WY3m3NZ_WdQYaWtGQODN9DK-r9ZmDJtNVqVEAWkcpR0KTzYN7baqp9IH-edjz10zHPrVuALUnvKDWs5dewi3ERQ4OmK1YjtQx--kb_5Ix9A4m2wZ1AcAUTVvsV_cgGHFhlvCyEQLS3pdJC5l_J0Lmm0Fmln4j7Z8-gc9clzoDrylPy1GNan5Lo8VdDuMlaaaMYaUS-3k91y9NPSyez9X6ZnkHpHbXXzzxFYynOOhRRUG1VZxR_sTeL6LUTP_kfzen-SE4ob7HzY7M0YMyzLZecB0ahDwNufFLm0edUtUGtg-HN35G6dREBC8CE6_q4aLF3G9Cu7VS6NifvJHvCTeBmSjPnMgcKB_kB15xHRKAxXEoFhHgKnlW3JGEkCWrbuc0SWOB5F9Hs6jEuun8CKSQ4_-igNHYvDGY5cPNx_qOfCnARuo9OL9EHJO-iY9IqTrdbMWEhV1Soa08pumzjomR6WGudgwYfkJVL8eDN7qb0oX78o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49818ac28.mp4?token=PzY_fvxyozvVqIGdVefpe1zuFoP2pkDDX_J5dVTouBhOuw9Rx3NzZkqqu78RXpMk9PYoc9OsDcf5_6T5vDXNF0WCCMYNgfbyM3motSu3qAXYNWB_0mFlrpL08_aW1yutdLdrO02xEZSiZAn2jRpHUIoR6YriyvvMQpkM4NK9c3o6m0oINJyynNFVy2k3WY3m3NZ_WdQYaWtGQODN9DK-r9ZmDJtNVqVEAWkcpR0KTzYN7baqp9IH-edjz10zHPrVuALUnvKDWs5dewi3ERQ4OmK1YjtQx--kb_5Ix9A4m2wZ1AcAUTVvsV_cgGHFhlvCyEQLS3pdJC5l_J0Lmm0Fmln4j7Z8-gc9clzoDrylPy1GNan5Lo8VdDuMlaaaMYaUS-3k91y9NPSyez9X6ZnkHpHbXXzzxFYynOOhRRUG1VZxR_sTeL6LUTP_kfzen-SE4ob7HzY7M0YMyzLZecB0ahDwNufFLm0edUtUGtg-HN35G6dREBC8CE6_q4aLF3G9Cu7VS6NifvJHvCTeBmSjPnMgcKB_kB15xHRKAxXEoFhHgKnlW3JGEkCWrbuc0SWOB5F9Hs6jEuun8CKSQ4_-igNHYvDGY5cPNx_qOfCnARuo9OL9EHJO-iY9IqTrdbMWEhV1Soa08pumzjomR6WGudgwYfkJVL8eDN7qb0oX78o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الامريكي:
في تمام الساعة العاشرة مساءً بتوقيت شرق الولايات المتحدة يوم 29 يوليو/تموز، نفذت قوات القيادة المركزية الأمريكية (سنتكوم) بنجاح سلسلة من الضربات المكثفة ضد إيران ردًا على محاولة شن هجمات صاروخية على القوات الأمريكية في اليوم السابق.
وضربت أصول سنتكوم عشرات الأهداف التابعة للحرس الثوري الإسلامي في إيران، بما في ذلك مراكز قيادة عسكرية، ومنشآت صواريخ وطائرات مسيرة، ومواقع مراقبة ودفاع ساحلية، وقدرات بحرية. وهدفت هذه الضربات إلى تقليص التهديدات التي تشكلها إيران ووكلائها على القوات الأمريكية، والشحن التجاري، ودول الخليج المجاورة.
وفي 28 يوليو/تموز، أطلقت قوات الحرس الثوري الإسلامي عدة صواريخ باليستية من إيران في محاولة لشن هجوم مفاجئ على القوات الأمريكية المتمركزة في الشرق الأوسط. وقد تم اعتراض جميع الصواريخ الإيرانية بنجاح.
وينتشر حاليًا أكثر من 50 ألف جندي أمريكي في الشرق الأوسط، وهم على أهبة الاستعداد، وفي حالة تأهب قصوى، وذوي تركيز عالٍ، وقادرين على القتال.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86327" target="_blank">📅 05:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86326">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdDU6KOeI4fCUEnfz0NvjIW5uqTPWY2LF2B1-KSy4lzLSAbdVx2LW9nOPq182LkVkZJ5HXw-xlqzLqkU2XZKy5hSQg2zkl57YxQrHN5u5_Gi5X3KMYLDX__5EUolHZTTzUNtK7LzedwmelxL_3NhF3bPrp9FyTZqrZv1vg2lsilWom-PtLmY2Oqmv9A_5KxK6Qj_0Xwk6sDkr1ctel_SuVL7zA-1C0GZls5Ti79iFK3li4t3P2P4JTJVVjRROXLKRpgV3VYHB2IfZ05geMTuj1-uaoVDAgVnl1LiQ9Wo-Bvr_s1vA0WIaaPy8Aefve5In8EMylGG2eFxX0gYu4scLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعمدة الدخان في سماء جزيرة قشم</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86326" target="_blank">📅 05:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86325">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f794cba83.mp4?token=sW0eEU-6oDO1LknRSGQ1EY25NiE-IibVkd1lXP4INLVvKyWHPBtDv5wTK1lkzqLzgN3Hi9dJ-BCBvhLmQ6PCCsQgS2F3xEDOL-ne1MzeIaSK-ZL6LlO1ksP_ozzI67qPhm0_5az-JuYm-bY8B0jBhvbuNLEQZ_lvd5hfx2rZUyN65cXYo7Coirgiy-kc5Y2xb9ngpjy54QzIv-uvFiLo1Ar7-aYT-2vgELRihhw44bYixex_6FTRGFeBgl-jkZdupTXZuuE5aNWpuU-kfAsgIqPs92pRkkMu1WNzJThc9tczJ5RGVaq-9wTip54vliHFA-GegCmBp2tPgYBG0Q0Qig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f794cba83.mp4?token=sW0eEU-6oDO1LknRSGQ1EY25NiE-IibVkd1lXP4INLVvKyWHPBtDv5wTK1lkzqLzgN3Hi9dJ-BCBvhLmQ6PCCsQgS2F3xEDOL-ne1MzeIaSK-ZL6LlO1ksP_ozzI67qPhm0_5az-JuYm-bY8B0jBhvbuNLEQZ_lvd5hfx2rZUyN65cXYo7Coirgiy-kc5Y2xb9ngpjy54QzIv-uvFiLo1Ar7-aYT-2vgELRihhw44bYixex_6FTRGFeBgl-jkZdupTXZuuE5aNWpuU-kfAsgIqPs92pRkkMu1WNzJThc9tczJ5RGVaq-9wTip54vliHFA-GegCmBp2tPgYBG0Q0Qig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان في سماء جزيرة قشم</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/86325" target="_blank">📅 05:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86324">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3204e88b4.mp4?token=OG7PdHm7e6mR6ptKDFHR8rNQIymyootexWSu4NkX61fh8aAHMH5oi1UnK_rhwrxgS4kux47J1R4NL_pxeXX6BG8o2X0_ZuyYc7tKcZfndRitlGjrGokZS9x9Om84X7ctoGwuRqE_rDpAEW7iMojZ3fSrt2CVjoVt_b1Aeuu-1Q1N8HFTR0CUCfYSx8R_J-4AvFcondGjVmOSHFxRdfBcZf0qUOHFeiutGztmQqIPkaaLD4l5e_Z14PbcV3OmAzsPpAnNuu-o-CgVUnZ1QlQoFU5z5tvO33sn_GWhFpmArarTZYjepRkALetG3JVyGLPOIc4dxM3TYVSJDlPz1nwvaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3204e88b4.mp4?token=OG7PdHm7e6mR6ptKDFHR8rNQIymyootexWSu4NkX61fh8aAHMH5oi1UnK_rhwrxgS4kux47J1R4NL_pxeXX6BG8o2X0_ZuyYc7tKcZfndRitlGjrGokZS9x9Om84X7ctoGwuRqE_rDpAEW7iMojZ3fSrt2CVjoVt_b1Aeuu-1Q1N8HFTR0CUCfYSx8R_J-4AvFcondGjVmOSHFxRdfBcZf0qUOHFeiutGztmQqIPkaaLD4l5e_Z14PbcV3OmAzsPpAnNuu-o-CgVUnZ1QlQoFU5z5tvO33sn_GWhFpmArarTZYjepRkALetG3JVyGLPOIc4dxM3TYVSJDlPz1nwvaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق أخر من العدوان على مدينة الاهواز</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86324" target="_blank">📅 05:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86322">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4ZAVARTH6oI5222w29yPXbAqT7ZvahGFOZXO1rfrBlCcEgH3DoK3YbPno109HlbD4KR0z48sub4SWZga1w7qWfSlWLbv8u-Ao0AwcP_687XqB3LuHFi-hBK-Quwu1lhgYY_famdNS1KoTQTc8H8l_Lp_5nTKePSB_bU6UzjMnuMhNtBDtiTOcb7T1_90F3Ns9R9bmMsVmTsBEQMeZgSb8frFvyG8qIkWqlQd3ZMEHPgRsE0cFZLnWjMuXsl-AISUwDwcavu1nnwxjXtBuHaIYMglcwv7vJTNcHxnYmW7YuNX9aQ434yO6RiqXKqSW88VgmdyqMZDl2DYdf6g8H4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fff119810.mp4?token=g0AIqYoPGDtkuLjK5VfHNYOTRyqYBt3jMSRWRyBW5io5YFoytp5kHwzgPJ1YQHfQBGqLdETO7eQ9a6FuG3hdvhL_103ZXXPtDQjWP1NiW2aS1S9PsNtsQGx3aFFZAa14b1pvKDFfkvJtF0P00zSOp86KsyAteMHlNn_kfzAUZlhIDU0ngo6ZijShldlzjDa4-gUV-UWgQnHQe7yRnwsiCc3oN0yWEBcYHYf1EbYlupZIH-8_oXgBrylwUTOGvP7RItas3fRBrTmBFC485K7XxXuiqARQIzNZHoYqoeLL_tFpTjuSxlcuvNHpiwByII-70_SvYE-edFC6qwXViQuYNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fff119810.mp4?token=g0AIqYoPGDtkuLjK5VfHNYOTRyqYBt3jMSRWRyBW5io5YFoytp5kHwzgPJ1YQHfQBGqLdETO7eQ9a6FuG3hdvhL_103ZXXPtDQjWP1NiW2aS1S9PsNtsQGx3aFFZAa14b1pvKDFfkvJtF0P00zSOp86KsyAteMHlNn_kfzAUZlhIDU0ngo6ZijShldlzjDa4-gUV-UWgQnHQe7yRnwsiCc3oN0yWEBcYHYf1EbYlupZIH-8_oXgBrylwUTOGvP7RItas3fRBrTmBFC485K7XxXuiqARQIzNZHoYqoeLL_tFpTjuSxlcuvNHpiwByII-70_SvYE-edFC6qwXViQuYNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي الذي طال مدينة الاهواز قبل قليل.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86322" target="_blank">📅 05:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86321">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f49cff1c.mp4?token=X4MIEDXG4LTgVmYHNvVYfWPFM2JGiH8tnjAgPqYT7G_6t6AyAyVAV-vU0mreuseYVO-xeKjYlZYexh6P-mzAla5b2S0waVwWPUIOlB4_6fRr19epLkJ5bxW0_R9mtJ0DkVxWv_4A7m0m20wqrK9JB-n9ZgG9S3r9GgRqDPoC2rjeADHPgQ82Xot0hAl6TzJx27gBCk77NIR2pJEY0O1zZ507zqKTmQ7ncRj7Kn_TAaCxYFum2EuMk4wTZ4Yhb_PaLlpRhCC8-BJ2KmGjfcaqMkLRix3dxBaQhyZTlFZkvi3fzgZjhze5P2PXsZ9YS0uV6qfGMX2SRLeo_MtiDGnvPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f49cff1c.mp4?token=X4MIEDXG4LTgVmYHNvVYfWPFM2JGiH8tnjAgPqYT7G_6t6AyAyVAV-vU0mreuseYVO-xeKjYlZYexh6P-mzAla5b2S0waVwWPUIOlB4_6fRr19epLkJ5bxW0_R9mtJ0DkVxWv_4A7m0m20wqrK9JB-n9ZgG9S3r9GgRqDPoC2rjeADHPgQ82Xot0hAl6TzJx27gBCk77NIR2pJEY0O1zZ507zqKTmQ7ncRj7Kn_TAaCxYFum2EuMk4wTZ4Yhb_PaLlpRhCC8-BJ2KmGjfcaqMkLRix3dxBaQhyZTlFZkvi3fzgZjhze5P2PXsZ9YS0uV6qfGMX2SRLeo_MtiDGnvPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي الغاشم على مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86321" target="_blank">📅 05:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86320">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">توثيق أخر من العدوان الأمريكي على مدينة الأهواز الإيرانية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/86320" target="_blank">📅 05:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86319">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d82a7c0bb.mp4?token=MVwwYXWZ4ci7rTzg5A1MfM5U5WNgolsCOsqHMqjmysJl0R8FQfhqbtldfjYMfpQfe9-XdIv9qDc2lRLM1COB1thH0_fXot9ehlPDyAgAVJ9hqZLdVC7qtLOFnKphBM1_g-9brwItwjwoSBp10vL2OqEVlyJD_m2aWylcWpe5dLRwftBTYnRBlrSFz7eVtC2M3x1GKL5hR17T_KDDz1Jr5GQBukyMglUB9wz4wm6iXP7W7bUohqRBMHCqmnkWEhM3y8YxlHtv3dbziMlzSViVSW0btTEqUys-Jq25PXXZ5d9SbVLC0dltdA6J6o_4QUwc2k7LppYzqcjK1gz39r3P7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d82a7c0bb.mp4?token=MVwwYXWZ4ci7rTzg5A1MfM5U5WNgolsCOsqHMqjmysJl0R8FQfhqbtldfjYMfpQfe9-XdIv9qDc2lRLM1COB1thH0_fXot9ehlPDyAgAVJ9hqZLdVC7qtLOFnKphBM1_g-9brwItwjwoSBp10vL2OqEVlyJD_m2aWylcWpe5dLRwftBTYnRBlrSFz7eVtC2M3x1GKL5hR17T_KDDz1Jr5GQBukyMglUB9wz4wm6iXP7W7bUohqRBMHCqmnkWEhM3y8YxlHtv3dbziMlzSViVSW0btTEqUys-Jq25PXXZ5d9SbVLC0dltdA6J6o_4QUwc2k7LppYzqcjK1gz39r3P7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان جراء العدوان الأمريكي على مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86319" target="_blank">📅 05:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86318">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvbmZtxs8f_fRPxvaDRSh1d3r0JjSjeNGyLeOq3bJMsayqd6WuQAuZi4bv6TrqWLvTQmdSVSIRj4XmozVJniBHyR6kjGmsfxIG5GcL_aMIT2d81jDO0Vk_QjpeqZsyfnEk6WhROS_wS5YFyAaX37wHhpWGHN99KmrywiXIwE0EFAGHhFSpuUr1hcWZuoiorYVzMTd-1Yl0hcqtSv4VMgXCuteI-bRaJuq_ifjHOZItfqx83vL6qW-UbS8Jm3CYsCvRUlyLfuh9US-_WTAPTfcZcH9MuCS5lJL5RNZbZNoevNHAfgkHj3j8x2AirFA8OEqG5Bd9bNLN3ya4o4-ewMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في مدينة الاهواز مجدداً</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/86318" target="_blank">📅 05:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86317">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انفجارات في مدينة الاهواز مجدداً</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/86317" target="_blank">📅 05:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86316">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
نيويورك تايمز:
إيران ضربت سفينتي غاز طبيعي مسال في ميناء مصري. ‏إحدى هذه الشركات هي إنرجوس سالم، المملوكة لشركة أبولو.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86316" target="_blank">📅 05:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrY0F9d_HvB3KwZg73Ne1xE3Wj9yjRntyUgMNtTwGaH1-WmvnT4ffuxRE0fRkt-Yv6qHxkWS19H9Zn0jz9RNyT_4aY9hg9OQBvA4EX6bshElyaw7CrSOakDFLKK79ZXZPtxPe8aLOcsCn0uAjjaBqjabH4bk2w7RDa1PWleI05RzTLTmhAPDsSOM8rnHL4jDRGQ6jTuUg0IcbgrWCUgToRNEZq_RTuy7ClC3dAKhArclxjhfQ9j-3h8LY1bdZq17tjhS8CdlVHkh_H7laXNYWYuG0XJybMk_ELALjp5sxLNWUSfSikDBoJarOAH0BG7pM5LetlbSqnZqU7Cr1k7f4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/psctdBuSXVbjDybunDyclNMU7wb8q-mvw_yNQO0Q5J_R2srYCOwjVhq9eSlc3KvTvwlsq2gnwsGSn8UiWRh6r7b-UDvixYMgXJMZEZvV1vVoVOo_APSBLkWztT6IRavVuNZhFIEp9pWjcqwAal7VTtNP42z-Wk6c__C9oWliJCagnw2J3iesaPbbkotdAD_l-Zw5EKDHQMrmm4j5Cx7pD3jW9XxIEzoSyn4UKlz7r4KsUnYf1kY1cMPs3pOa5N-1_Slcdu3v3AE9VVhgZt_BDhOzMJmvasovRcthSwnwIf1EiDLugVAuONdTR7Puk12Rc7H5DfZKGoLM6sMTIGotSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNYzWoSfu7V1yZ4bS54_kuwhOXjy_aFatzcfR_vtlS2luY9KXdEFffSZIyqfhNYjHQAwq3FkXbEU50vly7o9IommvcKzKYZ1psgKx7zNOIYJ0m97Hu7g5DOwPNfAWDTbplcA1f2XZqEEX7uYO_G4yx7awC_mapmUafj_wnM0ILcdn3kkmDryo333d10-fWTex3hOfc-IyUumYJQ9vQxpKtL7QJ-h0jBEB-a5sOcqNGSEF-TxgY7DZ6k031yO8P1x6gffQGXw5XG5FTXCKz1DibsTbPSOw4LZlIYS2KQ-TgDBJNbT57_9IIliNGhvb_DYJroA15t4H7lCL0J7A9T2Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استمرار عملية البحث عن محاصرين تحت الانقاض جراء عدوان أمريكي غادر على منطقة سكنية في جزيرة قشم الإيرانية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86313" target="_blank">📅 05:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43cfaca84e.mp4?token=R7NtvZvJw7DnwMdA1OOxbtObRFLzS5PKrja9gTzhVV826FG6LA8Pd0qo7pId2FWzRvaKEBl-lpOUtuH7_6bR4fpNUKM7E8it3Ows6Wvn0PBvDNl9S58in7JVon6TAesMVmGn6nZULDat1oaRYC91ucLFk5zKGJpH3KP7ICfq6vxniPEuKOawQrmoUrWDIhSc5FEP9sFA2GnYpyGPncM774eb9WU6gD2GzrugY1Iiu3z2Ri80LJYfqsVc8SA_02WMlo5XGTf7hHqYpQQHhTDCwMmwSzM4lJDcBfEJpRJsMaRfRslwaVSv7aR8xwRhnP9ZFw6xdkrU8ij2DCoc7OekPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43cfaca84e.mp4?token=R7NtvZvJw7DnwMdA1OOxbtObRFLzS5PKrja9gTzhVV826FG6LA8Pd0qo7pId2FWzRvaKEBl-lpOUtuH7_6bR4fpNUKM7E8it3Ows6Wvn0PBvDNl9S58in7JVon6TAesMVmGn6nZULDat1oaRYC91ucLFk5zKGJpH3KP7ICfq6vxniPEuKOawQrmoUrWDIhSc5FEP9sFA2GnYpyGPncM774eb9WU6gD2GzrugY1Iiu3z2Ri80LJYfqsVc8SA_02WMlo5XGTf7hHqYpQQHhTDCwMmwSzM4lJDcBfEJpRJsMaRfRslwaVSv7aR8xwRhnP9ZFw6xdkrU8ij2DCoc7OekPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تظهر هجومًا أمريكيًا غاشم على حي سكني في جزيرة قشم الإيرانية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86312" target="_blank">📅 05:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLVAElD5U0lWlLHK6UZhZmNLrRKEFvqfXHNXCrBCuOZwZw4xmMaZWjrlN8EGSLvS9AZek5NeKamWzYDRkR5LD1FWZIIrWo9i1JG6FL6OUrwPW7kJzKJBO-e0PKQ5gyxEp8Vj8zNAZ6Sde5IJSPp7FWPTn0lha6HoddivpNxanx1I5ivlG_YeUMGxmGVok8i_j_cP32s6AbBG-IdKn8pHIPBvyVuuF6x6DkoKNe-ALPCEOev8lunfi5HpKjIucCRAHcXbGX1m0B-SRxfoIkCaq4DBWL4YEO5BkC2OtpL7nCW2tAjwUOJ1C7-du5ZjY1sorxDleFwRYJI6kQnKhSBYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86311" target="_blank">📅 05:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e286db0489.mp4?token=upJjjfVXijuuhCtYC8a-h06ExdskmEk8KcBhdEEDUTilkKL7QAyU9jEa_WzA7TdYYywNwekSLYau0ieCgZvGsTr-Vm4FjMfPyO3qzYqrMopknGIx6WWo0gnuUPXPmKbLO8A8LLk-PJOyFanZ_J8sIgABpmXMA8loDqYnZ26IEJBovTFfAELL3cxvhHH7gn4dahjXzNqARHIPgaoFk2F2wiE0irf9U-fIuP57S97eQoCS4RiEvusHnArvjecWdRKH2VoNgzd8YQZP3jh6vtAOLw3SlQvCYoWGXdsUHKdMEH2CUYkMJ-d6BCSbel2u28ISts3kh8pG_l10kHG_jITqqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e286db0489.mp4?token=upJjjfVXijuuhCtYC8a-h06ExdskmEk8KcBhdEEDUTilkKL7QAyU9jEa_WzA7TdYYywNwekSLYau0ieCgZvGsTr-Vm4FjMfPyO3qzYqrMopknGIx6WWo0gnuUPXPmKbLO8A8LLk-PJOyFanZ_J8sIgABpmXMA8loDqYnZ26IEJBovTFfAELL3cxvhHH7gn4dahjXzNqARHIPgaoFk2F2wiE0irf9U-fIuP57S97eQoCS4RiEvusHnArvjecWdRKH2VoNgzd8YQZP3jh6vtAOLw3SlQvCYoWGXdsUHKdMEH2CUYkMJ-d6BCSbel2u28ISts3kh8pG_l10kHG_jITqqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات البحث عن عالقين تحت الانقاض في جزيرة قشم عقب عدوان أمريكي على منطقة سكنية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86310" target="_blank">📅 05:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86309">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5fb69b02b.mp4?token=cqKtHMByEl_QHQlnD5MchN-zB19gsheFiaiO4zkO9OhrOhQPltxu0-qFRWMO7QX2TSdNi2OkjjVLEK1l3Pk2A3iLcSnCJg9EqoaE3N7WITD9WlZV9R6qbprmypMd8PNfzmv8d8r4e3NyCfLyWLTNbODlptkrFtW6ikONGWsfmTD0yfSdoy_qX-jKkfD1U9UJfqqMUzQVJUO9zt7r3FHj9EwgqOD0CO7AQNDwRgz2oQ1xJOXbmxb-3NcbBB0d-hNBPcbFvIIoF4coCd-eSprzxqWUcW_XFPWs-FLk45R3ejfi6uUV_Knc1Ff88W3_1UJX8og3yAheQkj6L2ZUNP5KjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5fb69b02b.mp4?token=cqKtHMByEl_QHQlnD5MchN-zB19gsheFiaiO4zkO9OhrOhQPltxu0-qFRWMO7QX2TSdNi2OkjjVLEK1l3Pk2A3iLcSnCJg9EqoaE3N7WITD9WlZV9R6qbprmypMd8PNfzmv8d8r4e3NyCfLyWLTNbODlptkrFtW6ikONGWsfmTD0yfSdoy_qX-jKkfD1U9UJfqqMUzQVJUO9zt7r3FHj9EwgqOD0CO7AQNDwRgz2oQ1xJOXbmxb-3NcbBB0d-hNBPcbFvIIoF4coCd-eSprzxqWUcW_XFPWs-FLk45R3ejfi6uUV_Knc1Ff88W3_1UJX8og3yAheQkj6L2ZUNP5KjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعرض منطقة سكنية في قشم الى عدوان أمريكي غاشم.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86309" target="_blank">📅 04:57 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
