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
<img src="https://cdn4.telesco.pe/file/IK3PEpKuPD_xoIrT5MgbNFxjDQxU7HwvbnzhUJRqqlNJgZJaEHUox6T5MO1-s3WMeVc3PQ_9yIV1Vk-DJNORsodssZt_WlnaTg8wsKq0slQHrVAClAh5RKV3DKLzIqccbGdMTLsQSg3eQO5YdqKEORJ0mqaADJ8PvB0ROAKNYJ1TNL45N-h_zny7_mupqOCWr682jSEkx90Z2LVjHejUPHPLjkUEa7Gmbz4v6qz1PxjCc7DnCvP--oGVEQ4rEEqIr0pItaIh_OG1LdEFbzJMdPjpHcn22xsP6ryVxSnUa-7-EkJzKmKAFjI7vix2uHDs1Mn31m0t8lfimf99Fyep_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 223K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 03:00:38</div>
<hr>

<div class="tg-post" id="msg-82103">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=sKPBBIPqXSkn3sRvGuzKZ1hgy5_POHZmJO3Y-RuMeRUnyCI-1frOuxeF6N4_j4GEXWwHQFsSYmZKmHft-rTgZRphDn5dYpcN19RIlyiCJlSyzRFJwsTCLX3Ut1NTKR86HbGNaZB6D74np_u3CJzwhnEZqYCPgL-HkIWoQ0HwtHc0kS4oUd5VmcJ-vYtyLtAhy2QNsZRd6f1fbBofcSwb6BY63kWCun4ILypRg_j2CL8pTpWG31pVIbHzijUba1DKWoYaUh42IBhM1_d0nOqOvN4wyn2iy_MhjvwdLsDtJPrE32QjUEIc4KZlN5AsDPuiyIGDPnLqBqzt77WFHXUm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=sKPBBIPqXSkn3sRvGuzKZ1hgy5_POHZmJO3Y-RuMeRUnyCI-1frOuxeF6N4_j4GEXWwHQFsSYmZKmHft-rTgZRphDn5dYpcN19RIlyiCJlSyzRFJwsTCLX3Ut1NTKR86HbGNaZB6D74np_u3CJzwhnEZqYCPgL-HkIWoQ0HwtHc0kS4oUd5VmcJ-vYtyLtAhy2QNsZRd6f1fbBofcSwb6BY63kWCun4ILypRg_j2CL8pTpWG31pVIbHzijUba1DKWoYaUh42IBhM1_d0nOqOvN4wyn2iy_MhjvwdLsDtJPrE32QjUEIc4KZlN5AsDPuiyIGDPnLqBqzt77WFHXUm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروخدا یکی از دوست آشنا های این ببرتش تیمارستانی جایی درمان بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/funhiphop/82103" target="_blank">📅 02:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82102">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کیر تو بارسلونای بدون فران تورس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/funhiphop/82102" target="_blank">📅 01:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82101">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">علی گرامی به کدوم قبله قسمت بدم دیگه نخونی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/82101" target="_blank">📅 00:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82100">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">چشماش دنیام بودا
دلبر بی ناموس
🤙
🤙</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/82100" target="_blank">📅 23:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82099">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpd0Bd-kBfB-MP45iYldJzE3f_xrF0fvOCx3H4cZ-eL0FBnPkzkjOX9footsDXXKcMOM8OG47gZXl9hQimM3lk14ssbITdKrE8FTcDMbroU4wAICHwRJ9-qGsxtFPoEfLCcP_e0Lj8vfRPwfiAGhioU_xKxtY7lPWNTEFHBAVS-JQAJvc_g_-qKRIDZxL4RD6KIeq0Tsj6DIyfJHPPgM8NEjf1-nKyGZEPrV_liN4ChkKUV0HHSxB3PE3K4-FGJjP2_c618Z_d4nrb1whXZmaLftUD8PRya55LKrfyKcJMvKZtQ3MiKBIjh2A9LWWR9r4A-eS3cTUCaIfMLatCIfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس فقط یه کپشن "حسبی الله" کم داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82099" target="_blank">📅 23:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82098">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNoah</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMoIPqbAlCag2yVEMzVDawQ6ZgqN9pS9yekREUmaVa0GMrk4Yw1JYydoTPRtnQBp84GNrYxD-McHxvha7xUuU3PB-IBiPj1XpFzZVu1xcePWfAWI8CSi7w-2TmEypoQKHmwgr6f6YlX8JOyXYUOZ4rp_vD5vy6iJX9rMT2jTInviePexRs_ylWe__SGohXgFJBAYE9mBwwA-toksmK0da9fgEBx1NicB9YLBnE1YwhNGMwaEIB0iHhZRcUIM-xOXxT7qVBP1OgryX6hIqAYGMJb17-AP7hzPZxGV5q8lQBR7F2qcldBFn5v01FMqxoD7wrn0mZ2Eug1i0x9kD9kQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو حرومزاده یعنی چی که اسپید رو دعوت نکردی به عروسیت، من بت زده بودم روش</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82098" target="_blank">📅 23:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82097">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSSuC9suB7PjCsJZUntRqN4Uw3wGFYs6jKVdE2oD698q4HD6IBBEOXOsbHhoqG-BCy8EgtZlibrHE3D1yWj7Kn1wRGKKt-_dYJQZr1jE6H0RRQDcwSnw2G_VFLaU_quH_pa2ZAz9WtOZbdAq0Vd3g4kMU3bk27gNJd-MMZjMeBpLBp9vez0vK838kJnbyuoiOkc7yFkkQJ8QGWORbD6OVWNNIexazaMgrYgWfuFDjrejxXOIYXx2YbEaKzN8SNWjXLNaCd3gw3kSMaVJebpbwqE7yH8umTXr1JPI1Ery6KM5aDEWhh2wg2OqktQkxWTg1ZyjXl4jeQnewj0k4ATtgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رسما دزدیه‌بخدا</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82097" target="_blank">📅 23:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82096">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رونالدو و جورجینا به قاطی مرغا
هیر وی گو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/82096" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82095">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBxH4kaByKYJAU3U0UmXS8pJ8Remwos9xHu1sKFjMfK5uU_1cTDozD-tNec0lmfCymAEhtfnoMhCFqzkBeK2EzOGW6CQjpqwS3gy5kNz_XsBvakgShurBgW1ZOn0Uo-m_f7wRDtqC4Pjw8t_Gguu9ZS26gl_jkf7QQ-NEHBb2pRjWXGh0F7cJLvRz2_sWAzpNOSpJX9Gk4x3jazTXYWkkYQHjtcaRXRHHoiN14pLsgfHajXPO-k-WwvepZSnCvkH6VzkmO3283wrRk09ypOeoYfGusnCrh8vDVg4L2KYlsH4aPepgP4BL7zIEOwiadM_K-vSALCl3pHGYxNt8ShqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داود کیم، خواننده سابق کیپاپ از مسلمان شدن میگوید: صدای اذان در تمام خیابان های کره شنیده خواهد شد و گفت امیدوار است بتواند به ترویج اسلام در کره ادامه دهد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/82095" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82094">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82094" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82093">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82093" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82092">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mST0_T0QvG6jSeOqJNW27_xmgEOLZ6Gd2KDmT_MrexTyCL0tHRrQd-jf4Jzpp8xNG3MDPa-go40tme6m5BvF-i2FfrSGQhBQc-LZ67tYDztVzSqxwDKZKlGG-5kIW6gNK8fEl4y3X1eRbjnJhLYAXR_csDXz6OXuQMnwB1dJ33rfR9YG3zyzKOc_F9PzmFt9fbEKvg8_fwy_zD4O1KVZO3cwSkBqwoRpKef8I5NCpEK5184TARwxRSjJflIBxAPjPnQ7JFObYO7reUq5JKdItF99RLaHm_bgOq7T3_0aIY7ecnxpUlj6UgoYJdOJGaYTnnqRyAGrUjZJ90raiRWTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید خلسه به اسم "
Margo Zendegi
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82092" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82091">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNn80o4h5JJ2f0ZTQ8rOkKsZZe6d_QpvBb8yZaDskohLxs4ifohb8GRa3LGw-ARMc0Cez3lBAQ2lZT2CjQSOkA5v1D_VscsVqSZGDGnrpMTcX7azNn90T_q30uD3dF6uCUdk0wUItdX1ePPoCF-Sha6cAXwVj4n9EJORbsdFn6XyIbNleJQ2tpN4Th1VFnrM2KQQHJKKJvIgZ-3Sa5SKOHLtVHlXl3jqfwuCETUA0HerCgXBM3Q7RrJCqJFSsagdJe6Ddbxh4yOamGGJ-q0zGdaobCTkdPQoSfkasggc1pLcTfHK2qtvYan9xnEd93BviJD1wd5Jz8JVxZ6UAGohLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ایده
#تتو
#مهدی
#پسرعمو
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82091" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82090">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbIpgzBnD_XGC1zDVVmgkLNAOztpr5UisnlK4aa-zNg_OBk8-frtjKmrZHZ5FbK3PQjg_tMKRkrVmQyuPKvZfSEW3w0ioM8xhlwTKsrl3-NT9xN-WMi_wrkfgKh4hzC1IBDVlOcK7d0GC-dNZhxchELTjqja18vYyfLiq5tp6FzQzUy8R1rrkKPDtdWFf6RgE1ngIJ2GE4HFsCbq3ck3-2mgvUtqDMf0BwTqaKVSnxg9bJnM0n9fpobSAMQW7VjBlAYlh8mfuZ2zRYMuQDheauqhA0vNq6PjKOf8KvoBnw0zFg7pqnVgKll43GZrZhkphe_mYcTQMO3QEmoBA95skw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علم‌الهدی : اونایی که داخل کشور میگن جنگ رو تموم کنید، یا بی‌عقل و مریضن یا منافق؛
فکر نکنید اگه جنگ تموم بشه آمریکا دست از سر ما برمی‌داره، حتی اگه همه‌چی رو هم بهش بدیم، باز راضی نمیشه و در نهایت وارد کشور می‌شه و حمله زمینی می‌کنه.
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82090" target="_blank">📅 19:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82089">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuaykhXvoRXpnD-s7utqsX_bFKbbOcFttR0y76cwifxElIUZLqdLM_aP110D3vm3-y02EsAh_lsqyHXQAn52zqczs5pw_HYsAn_Q3F_ysdmi733y0TvOmHOfmOAuk7X08sfqm024qKJE5PN6-xqzfGrb6megdvIg7Pjd8P2yDSoy17pF54QHwAlfneydkrrRy6l3yIkKlLvCVgZZgywLt3V1BgFJysuYgSHOz07z3SkiFuvooEiMsSsacNNicXFkRWPltaN8i6_JqAlssdANancvtEAcfMgnLFGSkV2z3wDcL2KZjPf4GVHWcQKI7sqIq1VIy3tz1Wq-dY9coQsNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دولت لبنان رسما مجازاتِ اعدام توی این کشور رو لغو کرد.
مجلس لبنان با اکثریت آرا به لغو مجازات اعدام رای داد و این مجازات رو با "حبس ابد + اعمال شاقه تشدید شده(احتمالا کارهای سخت و اجباری تو دوران حبس)" جایگزین کرد.
لبنان اولین کشور عرب تو خاورمیانه‌ست که مجازات اعدام رو به طور کامل حذف میکنه.
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82089" target="_blank">📅 19:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82088">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iviyk-1qf4LpSwiMgoglWGO-RZBI_MlZU8ZWT5qQQZptzpvByLP08R-hvxDd0mP8_SqkkGxqTdxEcs4o2oFlUYf_f6bWmenAXXuWET5peU4TCKh-mQJRW2aY_hzzJYqw1kwA9t4hfCxp-A0Ubt1bpcUJl4PHy5UoQQ1R104tnpfWt4oOmoMJ4n3OHjd-ZfRXENT6FI2uwwCMYHV8GZmSe0Zz-p9etSADsGeMmt_j8xHs5VQASOf4GqNucmjLDUfoZ25TnlCdSSr304YCeU01nxeP2BrWVZmm7PxiBKQhtLwBr8WJ4jgSqyoKLXVGvrIxqCSFt5pPlHlrDhRGnOq0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رقابت‌های مرحله مقدماتی
🏆
لیگ قهرمانان اروپا‌
🇪🇺
⏰
سه‌شنبه از ساعت ۱۸:۳۰
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r20
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/82088" target="_blank">📅 19:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82087">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اوه اوه آریا یوسفی از جنوا و مایورکا پیشنهاد دریافت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82087" target="_blank">📅 18:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82086">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=JLUGIKVSo3ibY0_yINOplG24mOTuZGdJAXY4qqyuwkbjzKW34_CBQIaoIc4wkC2XNJOmHfg2EdPQJkFwbGGA6obwxFsDrkseqNnJgEpwSAzGPmMDt3q2djN4bRzmqUG6aiuZAOcvz8Vj3XMcG3-KEvijwdLgSu0uSo2nR1POcW6wjkebcla5gOFW6i7gU4_QP9-3g0GTgUbHWV_s0hV1Pd3-fzlNXJbse8m3uEdi22H52a5XLWKz2m4kei8W06Y-2HOO4dqCEHHQI4j6zyJpth_YiJJ5iM7KdpyTU-Z-m-xWpUOyzbxXPCXvX8LlzLdTD5ocU9LIF2foL9dlbAhdew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=JLUGIKVSo3ibY0_yINOplG24mOTuZGdJAXY4qqyuwkbjzKW34_CBQIaoIc4wkC2XNJOmHfg2EdPQJkFwbGGA6obwxFsDrkseqNnJgEpwSAzGPmMDt3q2djN4bRzmqUG6aiuZAOcvz8Vj3XMcG3-KEvijwdLgSu0uSo2nR1POcW6wjkebcla5gOFW6i7gU4_QP9-3g0GTgUbHWV_s0hV1Pd3-fzlNXJbse8m3uEdi22H52a5XLWKz2m4kei8W06Y-2HOO4dqCEHHQI4j6zyJpth_YiJJ5iM7KdpyTU-Z-m-xWpUOyzbxXPCXvX8LlzLdTD5ocU9LIF2foL9dlbAhdew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضاییان: طارمی بخاطر تیم جلو بلژیک  گل نزد که زیر فشار نریم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82086" target="_blank">📅 18:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82085">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=aM9wwqLpS3edAZhEV5XgsDCo47Li6vyA4Qhe5vvogrN-Dd0Hg2tdDRJogILaR29AuHB0oh5wqiKmPa7eDNk9d8qJrn7LAQrExC6QPetIQ6njPc-zZ4_hncG18aywSc7W0GNx5qbxlZHgmypT78kUSBNvrfCUvH6bvhq0EyQh4Z6vX4q4E46Y8aRmvxE5EMcoGjBHpRS48f3u9NK_4yH1bWoS9OVc4SPFixctZ2z-GSh3yKapyvMxhLttkp8gSwDZgQl57vtCTlnv0dm8wAJ4oGd2VT29-Pm_nU5Z7qGY9ibtrFwi3M5ipEulDmgtczQJhP9wEJi_GghCc-boA9thaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=aM9wwqLpS3edAZhEV5XgsDCo47Li6vyA4Qhe5vvogrN-Dd0Hg2tdDRJogILaR29AuHB0oh5wqiKmPa7eDNk9d8qJrn7LAQrExC6QPetIQ6njPc-zZ4_hncG18aywSc7W0GNx5qbxlZHgmypT78kUSBNvrfCUvH6bvhq0EyQh4Z6vX4q4E46Y8aRmvxE5EMcoGjBHpRS48f3u9NK_4yH1bWoS9OVc4SPFixctZ2z-GSh3yKapyvMxhLttkp8gSwDZgQl57vtCTlnv0dm8wAJ4oGd2VT29-Pm_nU5Z7qGY9ibtrFwi3M5ipEulDmgtczQJhP9wEJi_GghCc-boA9thaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران چقد عجیب شده، تو دیجی کالا مواد می‌فروشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82085" target="_blank">📅 17:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82084">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgcn8F6VhqAMQqNvPP1M5ygI8LAYbA2MzevpJmDe6rrGR6W8A0Mqnlm37cqU3KcL3EbA2CfeQMhBnyCdiCBs4O4Jezl-TsiiHAnsxgxlrEko1pq72iBwC9g5hdas6hwcllRd4rp8NeGZmRPnGsjvJ50OdVFHBY6BXv2BQTw5xurhZNYO7xcaMi6jD2HmAP4bDNrjqWK57h_P-aNdCSdtNs92E1aKJh2A687WuhDgagDXrI_khmqJqZ1ToZ8EIct47-FtvUm47xt19n45xgqD-O5C6G-KmVubTCaH25Tv06ZeVeGE6j-_GI7_OVR5H0b7kBRmdyjnMQzBLfxY4rIe6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دورچیو
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82084" target="_blank">📅 17:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82083">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82083" target="_blank">📅 17:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82082">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dps5hyil2ID1RQ6Tyy4u6H018XqSy_c_eifXG8UyZnTPA1Jb2SBq6aI53S3UxgA0YF0CX-rZPzXR65Sarw2nbOsfQfY3uDsOb6paa3FF9_iYFu0zES5MgSjOg1JDRVBOUQgEQEDGPd_d610Jx2OiP3F5vlNB34FtN4oJEsUNKFi6lWfdu9pSr8xhYQzuxRXCLRQ5Du2OliRsBXNg3q3sJC4MHxymKWObUZTAH9uLUUFomWkxrSfkbCc24MoQFuqZRDy4O0FNNSVjAiSPaCuzwvhz5BhS2DAiu9vhIHTfuExXKMFRGa8YdIIIaGwaRcZCOkHXp5yoQsXBrosn5z_VfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82082" target="_blank">📅 17:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82080">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82080" target="_blank">📅 16:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82079">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82079" target="_blank">📅 16:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82078">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8AMd_k9AmOTOeuz3p6cMA_S-63UJhzpRSs3yxPtuJ0VBqCIBNAnuJKSGKruG_rLquOigbA7ZfZkv-LvqrISBqvonvexSgF6f4LQGiZwVafKJNHZ_baEl9haUQIfJna8a7FHg9RT40ipg7OWcSxXwnWiz036mBA4WqqSWS9SgTbR_7tDy1HKwVJS1AGFeETqEnVKa83QFeoCx-HXWI8OAToTWX_BFTfjKWskFWhvMyJMWsqoZP8wYLt4h1MEcMt5HAxJZKuhHDUChmLGhzucCq_y2FcAoWe5RBk3ALJnRcwX8Uco-0ZasCKkgLPcUeEYpini2E59lLMbgLGBzpi18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82078" target="_blank">📅 16:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82077">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بوی خداحافظی از فوتبال میاد
مسی بعد فوت پدرش هیچ زمان بازگشت دقیقی به اینترمیامی اعلام نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82077" target="_blank">📅 15:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82076">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw_uLJTY44PKJHAbdt5Q2eMAfH9yM6GpBu7GY0By5bnLnPCxSxQEcot2Ld3Vm3EsIAUawga4i4ArKd40NSOEIgdsj0YhOKOosq0t74c_7ZG-20WXbKeGfB6PBOpEYOwgQOjzjLRCnYZN34qgeEazpyQRe_qYGTu2kv4ze2mKGKhnilLFGbUE5cd7CzRTZ3RB51geeTGu6wKvFtRBVNWYMx_J7c0YeQkHbl2vq2W4DhxLi58xvrO31qLJFgs18n_bGRZUKsl6LB_oyEl0oUN6BKpvzcvN77riNcSR8I_ZrhgH-EKK1wtRumLYrAhwu2RIWLj4lmTLJ8gMvLPdTgvqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجشنبه میخواد بگه دکی بیا بدهیتو بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82076" target="_blank">📅 15:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82074">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AV81d8n7VI1nbbQIBEl-qFUpGs1gs_fP44W_Y2wQMcHv1gVD9_Vm45NppnIFAKN82FybWcCgQFZd0KwKbBF0eSpBGhI6yWdbU7T4XG_3vNM5yJSVt_W3GjpDnsig_lhw794mdEAIN00Zls1YMV66FAH4f4SXR-99ImoTiMQg0tLX7FafGuL3IyQFQf0Nq5Abd9DwEh3xHRzyt_kVo3BAYybF_KlDAB322qTfjatMfM5rsR8ZIXalt453PaxnpybDSpCzbhmpUSJZV2-o5I4AWQ_JAXEU9b1L44EqvJUVPMwVFDrGpvowqgbIDdzMQBdoJLqOguSqLNlJRHt743QpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7LF1cOz3cbVRUVnwKJQyqCf3HChcZy69UdEHpwtIvC5z2TcjwDWSM2ouGL6os0YJX0zIJUqQx0hemFEiBzVS29YoR8cI0yxobPXIcYbzXHDVvmJooC0rFgacadCItwR1f7LmFkyWUN2I0q2gM2HWZdZZAIaIGZXBLDYgMDOKUdQvOqkooEHSL0cpxlkeQqnIKr6dOuY8v4iTIl8XQqlGDeFfjIrT4waebXNw5jV_A3NNvoSzPGLbcV0FhJBxCIj9lX0yVgpzlJJ-gO4Q0PCO-sUYhQSIwqldq_SvZManRZ6Zd8JjNE13fdvZU8BgY2vAGtbgMu4NzQWm8IV9zOvlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82074" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82073">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5IUmzvt_NPLKhAdTEV5wrYktelBvztgjf9V8h-QDIfGKMB57uUNdXZh8HgS2tUuAyG99QPWjFSwma70GdNfS91I3BdwTKKNJAuuuMd-wH01kz66d9B9bgCfyGIXhUQS5Qj46XnUDX4jQfzRy1G8-I8nmNbPca0m_N6FEq8K5DljPhNcY_d8nYChXjtJazO4KJPwBHeZre-xZGANHLD47Q11efcj9zXUeSrI_DWi7rYuIcxUNClF-EWFQPucci5VvilfdzMXp9TqoY8G-E-2UHrn1oG9X7R9UwSpTigNb_2fBSRd8Vx5kwNoiEiqk3RVr9aziXKwTllIOiDK9_rCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82073" target="_blank">📅 14:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82072">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82072" target="_blank">📅 13:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82071">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82071" target="_blank">📅 13:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82070">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oaey3u6TD_FbBj8DHVdYCgk6IrPDUJDaIdgF1tI2k4xf2N2H0CUL-so36YsjCserj_NWBrrC_9PtVTr-8lXsokHPbU0p5Hf0MRJDMIsIAqOj4zfTvi_22f0qkt2iau92Srsenxle1IgpKPWQBgvhFONZ2pqqxa_A524JuKCCXAWKJcJ-2UA_9PQ40WNKtKzPBwKMXWVaAa9QY_Bdbkk2-B1_rNCjeW2Lq3Yd-mLa2j00WH-t7xObX1UgxIaT_CDU9EUmSSNF7IkSvt0wNhHxSEcO4mS3bafjda3CkltYpkSyhAvggpxdShD9fr70SJSZFq-R7aEzrtvecVaxKOctgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک پولات به گا رفت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82070" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82069">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEWwLRJ2WIhXyAyN84UO-en-yQ5FqwtatWyGIFDqVefuBIKQUiKArchIqB8ginbRAwhlUCtD3C9gqEbqAbq4MPvPYDLST5bUTrBHquWIuTMxjEBEH5gG8_akLG31f2tmrDOjoUj4-Rj3OnFzqw2JoB0efj9-iUz2U7bREYFwml7evNPAkW1TyzveGoaUOXL-QKeZ8R9S-KuseB5DCRXvKniiJDOFOzmJCqrKSHhYm_vCFha5GuD__2jC7n2g9dTUUR6hH8F6o0WWIAYW1lCYeT7tYw07yLn9lnVxldedkRHo03D31VyDgMNwYkwZO4IB55rBFYVTcYcPh4Nef13fLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82069" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82068">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIks-Uden1rQEJmUZqWUNwnO-WPgEpIBvI4Rzzf62gOmI3vdx-OovOL5dwDmFgbZq_JH4SfLxUJ4Bn3ZF9XJ5nS0PdcIIkxARWOU7CRckJqJ94CwYqiNYDXnXFKmNV2l7onzFCF6IJky0g_ay9ZmUo5FWljrbZtyyhcy7Dw7-97i2jeH67x5jyZZhQle3VJKQrpOF31_a7xEmMoHHeyBAphGk3BbvxJIKNA1sD0FHHc0Q0Ff4uH-h4xAsL1KkccZr9WphSp_GVzWz7CdUe5zsGFH6rQ8_yoHgPGfgPN2Wvg3mnvmTpmyfaQqdRf00x2dwrHuLtzqAzTCVELxfn3RtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رقابت‌های مرحله مقدماتی
🏆
لیگ قهرمانان اروپا‌
🇪🇺
⏰
سه‌شنبه از ساعت ۱۸:۳۰
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r20
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82068" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82067">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hnu1ml4k4KPRcstNnU8_vfg8arsF-FlQ7eUmkyQVXuWp2Is5MOlhGxJB4Kgsw4vq4TYpGw0q0y-ii9Re40586c662qPntDpQy_q0k2ypzf7uAqwSrhzPaufKIrQ5CEs4N6Z-A0PXayvCyFPTDboSDkCNxcflp7SgYvBoIIfZXgs_sjRLBZxxwXRCLyTge6eCJcNeHV-VjoQGJZqH-j059hyPoqGf_Q9nYEm-vlEYI0UInN_4HKCqq8XHQZCPYHxQJxYQVgBhqKVEXchkY3VbLjMRfP4CmhyJXIScB0KwH9tf4JYDmN3vuakxX45djVkNs_R9-s3elynbN7WclnwD_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری احمد خدایی همسر جاویدنام صالحه اکبری از پیامی مجاهدین خلق بهش داده شدن که در ازای پول علیه خاندان پهلوی استوری بذاره و اعلام برائت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82067" target="_blank">📅 10:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82065">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">داشت یادم میرفتا
کصمادر جی جی و دانیال ددان
کوروش
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82065" target="_blank">📅 02:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82064">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSQZOQBYLRDjI53Q3CPMtIvwg4btvkBTeniZQBX_cf_4-Vb7dvgWgrLreN3jTZRlIgAvt3JKT1qMDGuA_TR0A4lMVIxO3MDGF2vjMaw2jZ-9B20EMeQGaOsr8qX1PfycB3Jl7AQYGaUnKqglkwuZjFN2bG-95S5A9X3M6SN9BUXgfr_99Xo83z3s80suioxLZGHVPRsBTowfNxntGra7rUxkbY7KyeJOxoq81WpWvMMv8wmXyAq0QVKs9nNmAWMUtMts6hWZ5yfiNZCLWrGs5Wa1OFQj5wolmRqnnJJMc3tKQuRXqq95fDKbxGbS8k8WaSvgFU3PnRI-AhmJi2ZqaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریک پنج ستاره از ایران داره تکنیک های مارکتینگ یکی از موفق ترین آرتیست های تاریخ تو این زمینه رو زیر سوال میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82064" target="_blank">📅 01:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82063">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دیگه حتی دکل سیریکو هم نمیزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82063" target="_blank">📅 00:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82062">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QerfvtdFH8CMtNT183tocWEPNsIirTPVCPuZaL96YhGodRm48Sl9X1OJ28J3GXT4gS6ybnS-EYbnytQdKi9IOzvKoeMafyVLaOCoST_MZNAhG1wN10v60h3ky4Terl6fBcIMh7nxFBoz6TV3zZyUnXIv8-sv787DuvIcUHlMiuvQQiwpxTwga-3iSt1iQxCSx0bfbuAt8WnN6d7acr4Wc49S6rUPcoS7IsjpMPFVpsUGD9P-McxFenGKTwljz4ruugx-3SYod4rxtQRWZw764xF0jXsFS68aAVjripbEyqAv6Pgf4OinyMFpvEgR3KxJEXhmEH6vywN-hcb8Oqhz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح امیدم به زندگی :
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82062" target="_blank">📅 00:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82061">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید. _چمن در خاک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82061" target="_blank">📅 23:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82060">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7XPpMsM-nAcVexo5KofIt0YB7NDF6K1UIlJ69aSzvEpj3o0plEYuQd1b5nE-Ku6u1lmHgGqlJ9xFTR-65aU2kwmuad05TyPrDx5hozY2NI3xfEmN0WINIL5XB91OTLowHVO9ONCT9pIS3Xz10n7MtEES-DrMpDLR2yFVO5OFo5hKrtyvpeDzp7WtBKsJ4UOKkPb5RtdLoVVnZshe51b-Xg-_X-H-3b3zegL9qxbAy2SdG6VjuzU25c9wxbAP7TibmKjXzHsjRiXnlxLqkRMOmxGJLUoesIjtwuRz7qwSqzsPydiy6RZi7u8_XuDnYosIioin9ZHVpxekBKXuJqLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بی‌بال به نام آزادم زمان منتشر شد
YouTube
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82060" target="_blank">📅 23:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82058">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUmG_L-gYJOJF8Z5-UA3A23lORYlTRL5suC1yhZhnehZ0giChAJ7bavhEdzVEd7ugqvrEI8d_WdVfK60wtNhdfRpNTBiRUWMKHwfDMvEwiAVmOW5uNNSvyxwd7KEq6ZvdZJKX-QTYfvnnEM3YxmFWmqYO09t-NwrBfaIPlLjfKUPqfUozHubnNMCs3vkT3-iBW7tEeP_XxXzAcm_wEI-QOtXGbNCgHLyrmGyW-Ech9qn6tzdDa33b6Ebb5rMeOH-piyCq510wGUXPAOr6CtYDvQlu98G_DTjyhClV7Nsxvx3Qiss-c2r8vcLQsXPpamHcWKfC2N74cV388R6SRPt2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82058" target="_blank">📅 23:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82057">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ عالیه
گفتن خب تنگه رو میبندیم فشار بیاریم، پاشد رفت یکم اونور تر محاصره دریایی گذاشت گفت اصلا خودم میبندم
گفتن خسارت بده، اومد گفت خب من که خسارت نمیدم هیچ شما باید به ۵ تا کشور خسارت بدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82057" target="_blank">📅 22:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82056">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید.
_چمن در خاک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82056" target="_blank">📅 21:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82055">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82055" target="_blank">📅 21:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82054">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=aijtwl_cTaK5bESQGQx1G6TudgtWl3dT0kQy2CShTJdGooyQYN4n7q2I8C6Biw3yoiP1SqH4JkH_fSZgnnm6cZ-NGpI6KZf0UWVCY-h4DeuolQMef3uva-Zhvd3b0RtQ0Vb8rXBWlaU4IJ8ssoQGEyMHYqC_xWRfLgYbXIq7exM_klLKJGc_SVdIS8V-CBNOaCy7vmTyVwsFh5ciPD1ZDKxctEPVH6s_j1h_EydrGu8-RhcaM3E8Em81Gk5LXEIgHxPEoq5KHlopDx_8kPwYVzGTYOC2aohBW_2DDZ6pRb_plQVIhzYCXUGd_J0ATf2myBKYNyx_AQQwl-vUOSoYeA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=aijtwl_cTaK5bESQGQx1G6TudgtWl3dT0kQy2CShTJdGooyQYN4n7q2I8C6Biw3yoiP1SqH4JkH_fSZgnnm6cZ-NGpI6KZf0UWVCY-h4DeuolQMef3uva-Zhvd3b0RtQ0Vb8rXBWlaU4IJ8ssoQGEyMHYqC_xWRfLgYbXIq7exM_klLKJGc_SVdIS8V-CBNOaCy7vmTyVwsFh5ciPD1ZDKxctEPVH6s_j1h_EydrGu8-RhcaM3E8Em81Gk5LXEIgHxPEoq5KHlopDx_8kPwYVzGTYOC2aohBW_2DDZ6pRb_plQVIhzYCXUGd_J0ATf2myBKYNyx_AQQwl-vUOSoYeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82054" target="_blank">📅 21:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82053">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ:
-
من می‌بینم که نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماهه گذشته به آنها وارد شده است (آغاز شده است زیرا آنها سلاح هسته‌ای نخواهند داشت)، حتی اگر هرگز در هیچ یک از مذاکرات یا جلسات ما ذکر نشده باشد! اما این ایده جالبی است زیرا اکنون من نیز از ایران برای همه افرادی که با بمب‌های کنار جاده‌ای و بسیاری از درگیری‌هایی که به خاطر آنها مشهور هستند، کشته و به شدت زخمی کرده‌اند، از جمله خانواده‌های کشته‌شدگان در ناو یو اس اس کول و هزاران نفر دیگر که در جنگ کشته شده‌اند، غرامت می‌خواهم. علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است، غرامت پرداخت شود، و ۵۲۰۰۰ نفری که در پنج ماه گذشته کشته شده‌اند را هم نباید فراموش کرد. من به نمایندگان خود دستور داده‌ام که این موضوع را به طور جدی در هر مذاکره و تمام مذاکرات آینده قرار دهند.
-همچنین، در رابطه با مذاکرات ایران، ایران باید مسئول خسارات و مرگ‌ومیر ایجاد شده برای مردم لبنان، سوریه، یمن و غزه باشد! رئیس‌جمهور دونالد جی. ترامپ.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82053" target="_blank">📅 21:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82052">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0ejUZtI3wdDuYgUTuCW5w45dg-o3CHQaMTQmY9-jBBs25-ZmdIF2SUyovsLXlFMU1wfjkc4WN3-zSXV9GXdiR9SPA9_MdatS_BJ3_94sMQYGcO0P2xK9-qaBgR7YL0JyzlKB3r5RHSQfSWYUvWSEyRMY6TzDTF8ikKPmFsm0YhoC8yOLJoLzCLqUbUElPxu7q5-qtnCLdp5xdL-Imm4eSvRJT-9zLqdjeHwniUWIQc18NfHBMMH4tQESMSwq6mVP6OSEScJui4L3KLXQVEwvZjh9AMlcAOJzBLBp56jgRJg0a7BmuhGFi-tKn0BTPqVKoIhciX5w-GgVFiQTGkuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید امضا کنید لطفا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82052" target="_blank">📅 20:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82051">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiVZZLBknRpFv9MuvorUgczSL_w3OJVcZaZZPzq8la-SKrw3NHi6yEE_6nsexY7Au7oXZQUXz6_Hed3hH_0ENAOYkR1Xn8rh59L5eu1Z4Yk51S5VMoRDOkofcsUClH2WBis6xmoxu2jkAmInJeUELns3iWAOUOm3WNR7alIQcrxDk76plIcgo2bRBRmXxdo7vXnDUNynY7lYMikG3veGzklbrM2QPyHI9g371EwAzQP9WkTRB5-XkW6_hMTJsHn14PO-NezS-r8asCeDoBm7Nxs59Da4nfPsGEmAVhjayg8QltXtgc_ucxuKX_UjeKNjfx7sTM3AAZsID3hcFZafXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزش سه تیتر زده جهانبخش رفته تیم صدرنشین لیگ هلند، حالا چند هفته از لیگ گذشته؟ یک هفته، و تیمه پارسال ۱۳ ام شده بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82051" target="_blank">📅 19:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82050">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6ECgyCoy_eF4j3NxDn9Vd9CReGL7bHgSbkNeRh1XJh5k4VNTfP8Wb2lDglv1U695xRzhwE3MCWO-MJSFlA3-sb9NpqzmFZQtgVIh5rwZfaVNApvosBZjpADB4Ld6RtgJTWanS6zw1VgP7qZhMO9x7U8FP_ZOc-kT73QHU2WuQD9IUgGrQlVO-Ol2vR40A6rN2o8HfmGzv_cjC2TPvJEWrTWXJ3gomrhn0udozGBLq4mhGexnFmbxNQLzZ2wTrgKhEHNeB4dBQ7Z3GEe9nJgHjGApw5x1CG4p1_7TFA7qVafVSF09vK0VdMxtApLL_xM5GCT8yOJCjrPnmWnY6KaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرومزاده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82050" target="_blank">📅 19:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82048">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdnWwMgZg8vmODUE8xri5IuCYtfHBxxBWAagkit8RovnEExuvFFsSJvyjeeMEVZvxX9ZoEGUwdcq_4ZfjNYkVHlppp9GUYsKGwKd1ITPlBZgIHXQ4q-oa4QwUrVIeXvweuB8WVC0aAwniZX0vFFn5Txa3Vd243_YC9F-s3j6B6NW20g7sMhtxCSGx4FM3Er-pFfOTEjAHvLetiglzoJgrOgwHnUn2hL516oJlYCvVYoLZh9_TeKPWpOVvE2JISqVL8mlDRqQk5FCdg-xNHgBZwOLaNVsTvc9NytIn5RG-vCzhsqqb-QD-GtJrdXQpfwfAcxL2-H5-OQ2Nrd61J1C8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید بانو لنا
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82048" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82047">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guZIJPuhohpQpSajd8q4npxzEe9nFUl2aVCKfLXomZHFUQhfQAk-CWCeiTW7jHEfQPyS5ARCa0PLIv9cHUkSt3Wl_iVieEemoVHZ913EvoMh7na5knOPsIoQtZYHTfiKPdjWqg2AUZXQtr_mK1mjiyaJ-cu0E76M3dR1XLTHxNQqjf-fOynhoyoqUeXwiKFiOmVuUaYB0j40kiSGjcmKIsRATmZDnN67skOx2I_B0IFcVA42uDed3env2arARROv1G5VpeYiflOqin3NhUUD1GIq3ZGhEtrBtjLgKqy84bGBcno-vXaCiKjdO3d-kbmmQpRobbVjunHynAp4yWNlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوماد‌های سابق و فعلی علم الهدی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82047" target="_blank">📅 18:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82046">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">زن ابراهیم رئیسی با احمد مروی, تولیت آستان قدس رضوی ازدواج کرد.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82046" target="_blank">📅 16:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82045">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ویناک میگه دکی لندن نیست، ترکیه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82045" target="_blank">📅 16:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82044">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlHBRoIiK7y7KwTwSduQXXQQ-BLRBzl7hc_rUgJDr_gDRbBBHPFklOmNItD4gvOw9ku3B8sz3wSWZzsYeEZmhOT124DBQPs3GFVaOCWP_cf5PycUpGfGOsb69viQTpWp7sHShc4ENNFaIqulvuVGnkyt-fPHzyCCFGgcIlHg9ULWeLZMsDQZgloLMn06Et4vNh6iosSxWpSVnaIQxI2H2amVW7LMMrOiQJa2i1bBX230hK6jJ5yGyBmPCakzDcLznKdbEhhwT9X1EvDWsO-l4t9lohOIHiez8p-sBqdBOUGO8YO-rkuztAi6eXffvk7YPu_QTkH2il5wqSAfvB4_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگتم بانو به روایت دریک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82044" target="_blank">📅 15:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82043">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=iH3XTrVLXMUZXoj_VDfHlPZinds7Ewq0gJ_6r458cECfIE9D_ual2V4NdI9zsyZrqWZB_PtvyZTqBg8_Mwo6xuV7MCnaCc0chqg12-jwKoE8gte3lmm9p3K_yVGN7wrxZC3kHTG_xhrHRByGarfO3kxgEzG9qCumZG2aUbuFlXE7BJxKLpTnsG18P4hB82J7iNFBFRANnA6nkPK6hM06LGlwJzm2FzslZ2bf8hA_Rj-2rySrPsscJhGo07ngqH9zfNG2FyhsvYCHs2b8lg9VPZ-XpDejm8ba2yaGJ3mmyoS3T7mPVkG49xAjpQtAIxfP0qPvfl5mYaoiQK-FqkYfpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=iH3XTrVLXMUZXoj_VDfHlPZinds7Ewq0gJ_6r458cECfIE9D_ual2V4NdI9zsyZrqWZB_PtvyZTqBg8_Mwo6xuV7MCnaCc0chqg12-jwKoE8gte3lmm9p3K_yVGN7wrxZC3kHTG_xhrHRByGarfO3kxgEzG9qCumZG2aUbuFlXE7BJxKLpTnsG18P4hB82J7iNFBFRANnA6nkPK6hM06LGlwJzm2FzslZ2bf8hA_Rj-2rySrPsscJhGo07ngqH9zfNG2FyhsvYCHs2b8lg9VPZ-XpDejm8ba2yaGJ3mmyoS3T7mPVkG49xAjpQtAIxfP0qPvfl5mYaoiQK-FqkYfpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگتم بانو به روایت دریک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82043" target="_blank">📅 14:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82042">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6XU4f337qU05kE9n_Z-G3A2-xyLBUDIMhH41QgaPHvWD6DUqoor2NYePMJLMsVQwbZOtfBc04Gx-4IReeKeSn7Y35KfuMc2XguKr595SWLQwSmKHNDLgC3y89zCkWGw7RqLhL0uvmDcq9jCWcb3W4j2ObkiZ1YrJTZrR0WjiP27ywHJIv1SQikJzwqgs7YAGnjRYJtIyKmH-SSHOB8nPyDwSGDWMZFYuHnGSTPufEKSpsuuI-uydmvGkLaseWIo8MGdYimEZ2oVC9mE8i_iCFZyEcpLXvnwRcFnbHHstdKtwUecV6tuAwwJFASRG4aKIZkYLvjPTm5c_ny_T7gpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۷  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82042" target="_blank">📅 14:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82041">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فابریتزیو
رومانو و اهبر رومانو این روزا سرحالن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82041" target="_blank">📅 14:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82040">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW4Q555C_GloY0hVfZMyiJouJdDODRECNSh13J3Q5k-anQ05CtNyaO1jV5gG5qPO_ecrHNdPFvotELxtSO71PDeOKBVuUUgfTQdWG59f3KApyhCYyJXRFCNT3EShgeiPc3Sve1N_tuZGhZRQ0AFq9OnITcPDImHp-DULSFNiIJWw-scFVUpXOUsOgJEGfyY5TluQRMiEJWZBpWtE-p9zyKTFW2JVK93Y6yqcnDZO05A7W1s5WpH5RgVD5iuKgSTM5_X8Qnwq05-6xtNEyf5v5xPhX6GBrEXb6J5zD-MR1iS7vhbNuiVvyTLm16OlF6DwPZm09pLCFwVBil0XLJr0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عادی ترین رفتار پدر ایرانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82040" target="_blank">📅 13:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82039">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gruH-bODUscCq-xlMSiuivdsuP-zdE4B5ZlUONHzvHmn2n7IFwPfdWFP9O-LOKJP7VeWef6QKvrbobefDZa3o_mq5DpQQ_H6X9x3FclFTSfVfuTVpnO9KKiYaIihl8q9lbfX9t_fxLv-Lfc1Xiv9dGpNQe7Wpoc8TLM8pKB_TOOqud_SDZw-yYypy4Ekun4-2xMsIJhSiYjzivmga8J2w-wydRr103OD1EyXh1YUcWx0wJr4yrffNiDzzuQqNwLOocUM0eLW_5x5ufTCVIl-I03gPkGd1f6r19cEJWhULl4h74uIvdfAD6JQL7UyJEjEmiSb8qKdxsq0dQpAlCSE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده خامنه ای در شعام، محسن رضایی: باید برای رفع تحریم ها بریم یه اکانت فیک از ترامپ بسازیم و توش بنویسیم تحریم های ایران برداشته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82039" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82038">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO6vNMZhxttxsNkD4iJ7tcX3V_R0H2reDL7JGfcTOqB97Imw63fKHkR4cXytJB3vuDxGgb5_GZg8cuLEQ16XWr5L2C0FTVvc-VRej_oAkyOQmxMTP5rDRPthKZkxd4YueXkVhGvPZbQXkZVlt39CWplbuV-JOsnX7rnFm9g5n2eRCK2qW4gLjJ9wtF81STI5U4zUk8jxG1pBt8id49UcbF-K4iZnNb9J4ElUeXGXURL6pR_RV9KPl3yQmo_jXotqsD_TY32MqqV-U5lhYmRoriqHPIQNsrG594Qwq_JX0yJSfbbKvlmaj4dpUzs8wumal_sPkQpt7OLq4Ygdln3oHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فداییو دیس کنید تقصیر اون کصکشه همش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82038" target="_blank">📅 12:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82037">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwSr8wVncAXN9erRGbSCgrSoN4iRx9ufzmSLSJby4cMpep7-ucDxZrz3_wBZVHp6BHAqyMIEpXFAGvh9OnjU4who2HnlbaqfKcTCL1iVG5eWNf5LIe-Gkp3-ISaSTV3zX69ZGfPpdE3IeUEkuTumwJIregP0OGg6A-oPqqq444lpcPuOs3EBkDe9iPxO0A9iBrUQPWr2HRokLWQMvK9yHfnJtZKVM9UPVq4C53PSOrvnna57FO9KtC_VGhc-kubqlkq4m4HTjAFrD8aS5Kt41OEm8HDrq4S5o9EoD-FlJC8eOQhwQ6asgT80choCcQeWcNzOItNoJ9scuf300DSBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ راجع به ارزش پول ایران
کپشن: ۵۱ سال بد رفتاری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82037" target="_blank">📅 12:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82036">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uglEbAjxIolKSYuxu1C0Qr6HGD1P-sik4S-QbX125Av2GYBBQH1JU7yZTQV7tVRMUAhimmISrOhwJ6NFYNLMp036KNYp54PBSkBEPVaTsBooCOxPvjPy5v0mUisuZN1mFeE6iNH72fW0A29gsHihc--zp7AJmtHa_-L5egbKIRkjveMNbEjl6Sr6cTf8VC92Z7BuVFX7zcWI3MeH_1JA-xj_zvv4bqAvyUhPyHHGwmiVs5dixkOw_O7yJlOSxtfCHL8-9BGYkXXIFQxxGC7_XE6z7yoqE01FdShl4QgG_Ica0eNUBlCZ2b0l2c2uFG6iszsbPMUKlUKdCh-eqA_G0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش به همین اسم که تو تصویر میبینید بزودی منتشر میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82036" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82034">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMYzyq4x2XbAvq_pBO-cO8VD-PnMFB3ZpGq1oSjHrWbIv5zPW-egZUoHoNltYlD9VNezNT4rYag37VOpyk3pIsDXP8GvEMVYbkvMFIOXL75VfbBJe2n4tND2dDK7V5G9XTYN7vaPLC_sYzzMfPKG4fcRdcQOJt_ZftcPWFNzRw3_yxmlpFQ_j8zuj-6qWjZWs-GabzOl3s6chgngXXvDWirwU2tIO5OKuTrM2O1KyTeZ3aZBSjptc2gtN9_fFBLzf4IpV_0Yh8ZGQyG3pyQclqCvbeSn8vSLGCh_hvaLlb9lMdmIOcGc2X8fiFLMCrs6_TqtEXnKL1YUBDlxHMTacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپو میخواستن دوباره تو زمین گلفش ترور کنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82034" target="_blank">📅 11:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82033">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">از لحاظ روحی نیاز دارم قاف بیا بگه "قاف، مهدیار، ملتفت، تهران"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82033" target="_blank">📅 03:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82032">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3RaNxScS0hApbRLjb1IEJVO6buOnBP7iNtgwiZL1lWRuRa9cSSEog5O8CJKV2aTB7-CLNkPaAGO3d0HpCEeBKMF_Zgokn9Y9rMbJ-vhdsra2p1xa934HYoa5sOB0bYIJrxgMxjLda4Oy7X-CFtjs-xpnQwNxeoaYPkjUl1B_oHgHU6W1kKKfkFWZJMj5m_7oL3_KGCzRUOygZLD7_VZDuxPF8fhU5JNEFAHLVaN6aMf33K4Ffpbk3t87i9sbP5AFQrraxCOt-q-BLFC6tTqCF30StqHvHaF7CvtsqkmDWoRvgrkuX4pdsa4gviv4YezrX28WLxrWr1CEmtWPRWDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار برای سروش، خطر در کمین است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82032" target="_blank">📅 02:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82031">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyYWJC-cI4ZpVhNuTYm_bhi2_HXYIqOleae_0EzXiFlXgOvPTSlOxAbBp3qgD1MYshO5WvCzOXIcl1pZpghqTRHGhPcQurpySNMFs6LdPvWCNJya8K6tkJ2cwolLluNx0CmSHamgCvt0xsGE1rE-GQ2p6qZZrW28lOLUjo6mBIl0enBGINaL2jxoBbXMV7Q5PYQewjZBwghrEaO6NYpAUjaNhaAZB89JUoAMSLcb6NsBTyQNeJ54rwJ4uG2G1ILdMxSLuAILXBcqAZlnvy_CZfyP2OezjnqM1Uqp6VarxEdvmllORkHZZDPye2XnDOTk8zNNoQ_Dg_l4Sx9tjT0Eqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی داداش آروم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82031" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82030">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">منابع امنیتی گزارش میدهند که ناموس سجاد شاهی ترور شده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82030" target="_blank">📅 01:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82029">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">4 تا انفجار تو تنگه هرمز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/82029" target="_blank">📅 00:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82028">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سپاه زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/82028" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82027">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P60fgXcm7xSHmAQRKNPNo5Vg3pKzAZeJCJ0c9lCUXD74tm8PXnbIN7mMjHvrxRyixsxNfkLZUwVtIgagvCCrSh4JfSzmTVK5ndSzqMy3jdIV2iHIxjU_c70ABBiKjLGyW5mI3r_Cds0JMg7D-vsxjGOPIuUt1oBKVj7E-TtoWKOnhq--pHdx0PZ0HssLgBvh92Ib_dEjnNBpLgkPiA0s1iSexdwkYmaBcNOOa6_BjWh-jmfgqsSxhiYT_w13Mmu9h9XXaUVOo9woe8O2him3qKzAzAcJgovRQe6hayH9P1RTMcIbaLQlaUQOxaruLasz25UbBEN2FOVCT9uf9AYaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد عجیبه این عکس دکی و صدف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/82027" target="_blank">📅 00:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82026">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ژنرال محسن رضایی رسما دبیر شورای عالی امنیت ملی شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82026" target="_blank">📅 23:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82025">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=b2TwwUwZ4EcXk24bU54-rfsyVZ1i3n9gXk6AFMt4KPxuKQ2Rb53uAP0E3ETv4PEqsHzRZPx3aHls-EnhbRZPnR0IhOW-5ph-lkzFk326y3UVeWxQOLMFH2KWRaLPARM7kDvOam-eJ8nS-ERKuO6tFXIAcNj_YLRnxqqkzQnelwgX1gAHcB0qcZDIwuSVPNwt_a8yFt1k3mW9ZFeEMGEI6yQXMFCWKFdvyDQgPW1N-cAFbIUhF2v_IvdILaDJ3zqw4UjaQlgl6x0VAyJU6uho78OuD-qjBrTxGPn-cVsb-SdJ4NG-RTPPHQQaTarf6u9V_ZRca7YVKxfVLjFJOAjyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=b2TwwUwZ4EcXk24bU54-rfsyVZ1i3n9gXk6AFMt4KPxuKQ2Rb53uAP0E3ETv4PEqsHzRZPx3aHls-EnhbRZPnR0IhOW-5ph-lkzFk326y3UVeWxQOLMFH2KWRaLPARM7kDvOam-eJ8nS-ERKuO6tFXIAcNj_YLRnxqqkzQnelwgX1gAHcB0qcZDIwuSVPNwt_a8yFt1k3mW9ZFeEMGEI6yQXMFCWKFdvyDQgPW1N-cAFbIUhF2v_IvdILaDJ3zqw4UjaQlgl6x0VAyJU6uho78OuD-qjBrTxGPn-cVsb-SdJ4NG-RTPPHQQaTarf6u9V_ZRca7YVKxfVLjFJOAjyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر قدیمی خلسه راجب شاهین نجفی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82025" target="_blank">📅 23:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82024">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۰۲۱کید تولدت مبارک ولی قبول داری شبیه شیپ استیلر تو خاندان اژدهایی؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82024" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82023">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=RMHmN9r_A7-3xR8zBOg8QKTm8b4XxcYnbnt__lspCeUq6XPUnhFO08EYpsM-EGp5ttXfc0EnlUHDXBeMCOBn0yKALJRxoW6By8m5og69tgtVrkd3tk4e6ZG9mm2snpT4BwlL52ZgCEV-xQS9CO9EsJH9mPjtIx1ITnOvXE2VVD7ZI0vicqy5t9mi-TYgdDTnL_qaA3Ap2yNS772cE-Wc50hOFG6imMcf9FXwhVHSgOYbXfMa71efM00d69l_y4W2_LCTkqXw8GM4b7CLg0221IflB8rqr_bUI8OwVKlAIM31O8DoKcio57LiXtsILNy40VpoVShdMhJYfnl36uvsAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=RMHmN9r_A7-3xR8zBOg8QKTm8b4XxcYnbnt__lspCeUq6XPUnhFO08EYpsM-EGp5ttXfc0EnlUHDXBeMCOBn0yKALJRxoW6By8m5og69tgtVrkd3tk4e6ZG9mm2snpT4BwlL52ZgCEV-xQS9CO9EsJH9mPjtIx1ITnOvXE2VVD7ZI0vicqy5t9mi-TYgdDTnL_qaA3Ap2yNS772cE-Wc50hOFG6imMcf9FXwhVHSgOYbXfMa71efM00d69l_y4W2_LCTkqXw8GM4b7CLg0221IflB8rqr_bUI8OwVKlAIM31O8DoKcio57LiXtsILNy40VpoVShdMhJYfnl36uvsAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعضای زدبازی، حصین، پوری و الباقی خایه‌مالا بعد از لیک شدن چت‌های مهدیار و فدایی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82023" target="_blank">📅 21:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82022">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE9X6irpi9vhSNSVUz1_7VyTeH0FVAAOVqu3Vm0n4_jwws15jpVBxC8HlZgrVztG10kIz66WlFLG6UIaSHm8P1J5W22r-UlAe1RqGTQH3JF3lIExg6p67YdpBcNakm4aC2daY7_WdGz16JxYBfhs5sWt8zKpbD0diGdy6wUqBNe-R1EI-ZJzzK3MzqLImfwtj3zqNVEpkAXIoxQKZ3U9SdNv7i_91BkAmwXzU2BYq6LugkSbYmy_I2hb6tAgUISurQs3KHj_xFEGXs0HKpcpLsqcndPjHXZGJn5iBYc6T4xNuQL0dWYDV2SmBL3ma1nqObUdk9xQiTLyAnVBNPBMNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی امتحان سلامت و بهداشت امسال سوال اومده که یه مادر چطوری ایدز (HIV) رو به فرزندش منتقل میکنه؟
یکی از دانش آموزا نوشته: سکس مادر با فرزندش از جلو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/82022" target="_blank">📅 20:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82021">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpy8Vg972Iy9gYa1evyYV_i1sypXxgD_j9lxifC-nz3m0tdgJmjaxST690KCNIne4VadlKsxaDtgr4z58F85YKE8jOW6xal-O3cCONmYjEkmtSdahOvQGHUzmPwc-wZjDPthSYlOghmB6haPOeSnbPUeYEKHVkQC-mK_yOFPmwPpulMFt-hNYdB4zdbyJzzlaqUEDU8ibYMagIHVoBl1kw7SkgQxpKBnI86O3WNvyEQTkV6oK_GZF6-SNz1a3NwTXazCKbwYYoAUwD7Yhtj6Nbg0q4-ap_F3Z9RU94XV5HmbbVlOaCbUOZFfjA-W1gLLxnWFOh806zIxtojHqLlXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82021" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82016">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gaoH3RC6AnNTdhrm8pDENErbq5DJFB-FJyTY_JsOM43XzbkRRhgM0AnlhZG-5l3zekPxKI-EHkptTn3-_1dx3J8Ty3Fxbaa2oJ32WxUPkGxHmGL0ocBHJK7jx_JbBinGauE8_JOeNPe-fJ0uIx0M9t8jb5FdixZecspDOrg61Lk58tz8ktq79qVGV_c4dWKd0rIj_SOr2pa8yCF9ElKI_loxzZTLSplvWVbqeD59J8QQrgWb2V2uu3-lkwqsB5sCTTuTBeJ2LIs6OZL_siQULEdLiLCl_K33s933K6XU1o2rnIkFZ_wCScHiYXHEcJa5xaP3ev4gwjq83oQ1jRk1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mR-c8Sq0ttqQZT3P2bwzAOFFCaveXNPorD25MAXjIaSnfH-Ji2WkLUslfjuKqlSWA2Vlr-8TgcgahWA8kStncTmfsdZtI-6rfzl8hJirPSh0cDRck3EkpXFoAvWaoVOXS3TNjYu4FYOUslt84uzcISSQuygZGQjj0Q5buQ9S6i7aBm8YhYqN3POgKjZdBXN1VUCGDxnPjQhedACBO1Zp3yWN03nCj5Imbni5a9f2zyFkGxkRDNqb_Qal87lEyIYY2FVuYlRTlKU_gkVdg-xbW2TmE91IWfE4V_hI_wTsDRgIv7An1gY6F0SW_8FqxrgJBmQZarTlL3tkKKVLxZhntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJWxLf8YEVxkogmn3fBRgA9TAViqoa6bbBmOoBpfki2c2-DVDSYAgAHZWD-NlZRRze4BjToMyJMoJHWQxkycnmkWiV2BbVX5aWfYGgVVXRE0nZoMxzG3Swdi-3hTa1F5YVhJQ7HIEnwo2_xp5zf1r78bPxLxVp8D0zoikkIUq2xElt5bpO3gQty8xYWK7u4ckZxSscOEPN2Dfmy8gNxkAip6K6cTjMD1Fkd6eWmh8PTCbMb15uwzDYg3O9bI6wxm5uA31x7brnFGq1XRLZ_regGTJWB5b-vcu9bq5g_2cPw0W6b-LICbcPMRqszx38qGsxGnpfCvA8fahkOVH2bm8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=JdXx_MuMPzepp1dDIX6arqVuJMWYZ5RVCW2n97EQY2C_laOl0RSkBaZBFj7dt5pbn5OJH3JLvoZA9vOBu_dF8h_R4HQ1mLlmT2UoLV-FA7vsvSp-k6ue1xxi29DFYooeIpdSZ15xk0bEfEJw9iQHzaMTbBwgKq9te1_-dAf6YwTr9XuOmPcdgt1JjS_JabzKVksETrISfSrT5NL5ZORLbV_kRd_daEkPoXh4g5n8LH9kfwDJhKrPH_cWWpzdydkqt4iH1svhcX-y81bUlDE3XzZg0SOMSxmZm9CCQDnFGZYCZCYNgTqwQJeYeDJveNPTMfqJCOhKc4rnTaT1BmBSfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=JdXx_MuMPzepp1dDIX6arqVuJMWYZ5RVCW2n97EQY2C_laOl0RSkBaZBFj7dt5pbn5OJH3JLvoZA9vOBu_dF8h_R4HQ1mLlmT2UoLV-FA7vsvSp-k6ue1xxi29DFYooeIpdSZ15xk0bEfEJw9iQHzaMTbBwgKq9te1_-dAf6YwTr9XuOmPcdgt1JjS_JabzKVksETrISfSrT5NL5ZORLbV_kRd_daEkPoXh4g5n8LH9kfwDJhKrPH_cWWpzdydkqt4iH1svhcX-y81bUlDE3XzZg0SOMSxmZm9CCQDnFGZYCZCYNgTqwQJeYeDJveNPTMfqJCOhKc4rnTaT1BmBSfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیج اومده یه ادیت فیک زده که رونالدو بخاطر فوت بابای مسی عروسیشو عقب انداخته
حالا کامنتا ملت:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82016" target="_blank">📅 19:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82015">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزارت خارجه اسرائیل:
در تابستان ۲۰۲۷ ایرانی ها میتونن از خود ایران برای سفر تابستونی بیان اسرائیل.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82015" target="_blank">📅 17:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82014">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSnkV0rlqH49vTTYpdPEKgFgxLHBMsQzudpzX5MA7l70FZLvEcrlrpUB8F8qXo5GhRXI_9JrBM3NelsBNMhkW6raCYj3E8HfZp_oojniDzyyQidp3dyfYC6AS70u9_Pal5vlGoKv_I0XXsf6Lw2UbAX34TcpEG0tDR92InUPsArhYzdbS7Kaaj5SiRC3BO3S7O1vEBcwEl8kXacWbZ5cIrl_oS-Bbk9iJyclhZCVNjC3JnydMJVqN2-Ho1WcBW77_7DH0uCtWbMcoXHrdcuH9I5tDwDKg1kqI4oicWvewdP5hlHGUKqAN9uhQyqDcZ7hcqezOnJYLzD3-Efs8qf1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تیجی به نام لبه تیغ منتشر شد.
YouTube
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82014" target="_blank">📅 16:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82013">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خدایا یعنی قراره کی بهش دیسبک نده</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82013" target="_blank">📅 15:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82012">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=r8KnvhoFFPj-BD0KoWa2R5zxkWNvsUoFxGsN3W0Nw_1YfdztBZ1l7bMvRZRic6lJnfHZrKxeGnwbc2S-M_EaQRX8Ar_w8fv4RvjNdJ5rhKg0pZti_pN8BJLFLtAMnc-5X4RN9PqGbiwjwVIkGjwWoaZ4yzbjnAEBCE-8jZ8EIquxeAZ617SHqDaEGDt0dJM6Iecnwx_93bWbH_qiSMi_UDUCBkuCaD4KAw2OxTUvxH0kpRHcnq0Fegh-RVX0lQHmm580NtM-cJidmIdB2iOW4ALzRMe_r-sFpZQXuFDlEZ0i2DCBhFyHbZTzxfH10T69ZHpxL2k8AAdaykQe8hZ1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=r8KnvhoFFPj-BD0KoWa2R5zxkWNvsUoFxGsN3W0Nw_1YfdztBZ1l7bMvRZRic6lJnfHZrKxeGnwbc2S-M_EaQRX8Ar_w8fv4RvjNdJ5rhKg0pZti_pN8BJLFLtAMnc-5X4RN9PqGbiwjwVIkGjwWoaZ4yzbjnAEBCE-8jZ8EIquxeAZ617SHqDaEGDt0dJM6Iecnwx_93bWbH_qiSMi_UDUCBkuCaD4KAw2OxTUvxH0kpRHcnq0Fegh-RVX0lQHmm580NtM-cJidmIdB2iOW4ALzRMe_r-sFpZQXuFDlEZ0i2DCBhFyHbZTzxfH10T69ZHpxL2k8AAdaykQe8hZ1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پهلوی و پوریا بشیری
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82012" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82011">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=FdD880b1eMfnFtEBYaqVdCLtLpCAAS7UAKDwyHAupQ721USH7veKQXY213EXvVtnSy3SxrFoP7m52nX_m-JBIrdXZlPCBmduaNr6x98Wq-evGpAeF2-3mGBMSiDqlcfqh-YBQjb_FyXtrzxIffPqeUVvo9YT4q6O2n47HZVpUdkLLRecfKGeScTxWMO9gM4FhgcIreyAGWXoGNf7pOYWAqr4nErAWE6VfuoA4qR2Q6xuaf3fDZXztyZ67A742p8iMm6jXrJCHI6DWLs1ouPKPmfixDqv98UIWnwONbQPBDo7LEKaVna7I0q2DAngcP1iHQsLth4z0e51yWwnW1EXvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=FdD880b1eMfnFtEBYaqVdCLtLpCAAS7UAKDwyHAupQ721USH7veKQXY213EXvVtnSy3SxrFoP7m52nX_m-JBIrdXZlPCBmduaNr6x98Wq-evGpAeF2-3mGBMSiDqlcfqh-YBQjb_FyXtrzxIffPqeUVvo9YT4q6O2n47HZVpUdkLLRecfKGeScTxWMO9gM4FhgcIreyAGWXoGNf7pOYWAqr4nErAWE6VfuoA4qR2Q6xuaf3fDZXztyZ67A742p8iMm6jXrJCHI6DWLs1ouPKPmfixDqv98UIWnwONbQPBDo7LEKaVna7I0q2DAngcP1iHQsLth4z0e51yWwnW1EXvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از کشته‌شدن مداحِ سرکوبگر، حمیدرضا رجب‌زاده، این یارو با انتشار ویدیویی مردم رو تهدید کرده که اگه بازهم بیاید تو خیابون چنان تیکه‌تیکه‌تون میکنیم که پزشکی قانونی با کاردک جمعتون کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82011" target="_blank">📅 14:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82010">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جزئیات جدید از پرونده حمیدرضا رجب زاده:
به گفته رسانه ‌های داخلی؛ قلب حمیدرضا رجب زاده رو از بدنش درآوردن و مایع منی خودشون رو روی جسد این مداح ریختن و از تمام این لحظات فیلم گرفتند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82010" target="_blank">📅 14:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82009">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">محسن رضایی جای جلیلی رو تو شعام گرفت
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82009" target="_blank">📅 13:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82008">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جواد لالیگایی(نکونام) به تراکتور هیرویگو
@FunHipHop
| TaymazROMANO</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82008" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82007">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1jUOok1rSpl1_FgzxOpJHzG_YLVCjMDzDbH435wNzQ3SXMDN3drpx7nPSkAMocllha2a0w56O8LUY5AIp1c8T92Q7nlf8yCBK18S4gdLluF_CnYH7mFqOeqpoaUkk1Wm1I4W-eg_4O6IBeuftetV_fGmrWhwrJEcvvyAaMd9WW3Wl8AGuwlbaHucEP70pFyyom6AxsukKWvl-gKRwkbARSmRwKW5RO-1h0arTc5CEHRDX27QyFjdeH33IKn813fk93gQzL4zKqDdVKxSFyDgQ5vNUyhnFXZWF-quh5cDVhYaFc7wJlnuC9T0MlhKIe_-uYKlwoirrlYeZLOkyAqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرکس سالام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82007" target="_blank">📅 12:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82006">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
وا
عراقچی: در حال حاضر هیچ مذاکره‌ای با آمریکا نداریم، همش تبادل پیامه نه مذاکره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82006" target="_blank">📅 12:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82005">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هنوز متتظرم تا انقلاب نشده آیسم نخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82005" target="_blank">📅 12:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82004">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oolKQK8e4_odvOvnv_dY3XvO-jdHHq29o4twJZ4Dgwllg-ZamSCZ5F2nuigiS7i_VUrDfUL2QkeRvvqEVsFWonjdUbKtptTkNMWNShmiENAomedzxaPVo4HL5dtzUjZa8OA_r_j0rdgQRvxgVy2QSN5tBpksWC17wyCkoWL9RP4hP-Q_-ymsVYV-lYcn6zDjYIFpOhz1pI-XLanYJF2HCKUdm6kXdPBo7xQG8fjOyhsV4eB2GNtve0JmlBTiihPK1mfsAlwfH7giofTBiqf-5esUZLHNhLpa_170rs438_qX_sgGMmwdmjVMIykowcuDhPO1wfSm-coqiT2pPp2GMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس Calvin Klein صاحب برند معروف لباس زیر به همین نام، کنارشم دوست پسرشه
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82004" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82001">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=lvPlM8PFNkkvWIpl29p9_OjGPKub0THDxZGf9gStOYACKFPMKzRsPPEEkBwfAiuqmsjGalx7h2ZEOlIwzjHIzvjZTrX7I5jDzVeEiABwkJ0hrrPw9YUic9orBcfi9kSA3VBA-H24lplmO8lNywWwqSAaJf4tCz2iH471G8igc5NZsRgACqfQ6Aor7yCkCrUCoYBHNmuw2vY5TaV_BPgbN5IIxVwGyv4ubgGF9A2CwYvLxWCgl254x_MQvQA0TBLPbx1QNRMqsX-YPPDrq6yYzfalvTMpeyNwSZN1UsS19qOVnsN7A-iQemucgeMzliJAVTLLkg2W0xIGKXmfPPnm1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=lvPlM8PFNkkvWIpl29p9_OjGPKub0THDxZGf9gStOYACKFPMKzRsPPEEkBwfAiuqmsjGalx7h2ZEOlIwzjHIzvjZTrX7I5jDzVeEiABwkJ0hrrPw9YUic9orBcfi9kSA3VBA-H24lplmO8lNywWwqSAaJf4tCz2iH471G8igc5NZsRgACqfQ6Aor7yCkCrUCoYBHNmuw2vY5TaV_BPgbN5IIxVwGyv4ubgGF9A2CwYvLxWCgl254x_MQvQA0TBLPbx1QNRMqsX-YPPDrq6yYzfalvTMpeyNwSZN1UsS19qOVnsN7A-iQemucgeMzliJAVTLLkg2W0xIGKXmfPPnm1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاسر قلی‌نیا پس از کسب مدال طلای اورال کاسپین ‌کاپ ایران، عکس پهلوان مسعود ذات‌پرور را بالا برد. عکس قهرمانان واقعی مردم همیشه بالاست؛ اما امثال هادی چوپان، جوری فراموش میشن که انگار هیچ‌وقت وجود نداشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82001" target="_blank">📅 10:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82000">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82000" target="_blank">📅 05:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81999">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81999" target="_blank">📅 05:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81996">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxgIQ5Tdja-F0U3UJEJCz8dUY7ZfvPYgKJNZy_WXiP63NJo1LV5gjjDMSL9_VTSkM-UMS86W9_KdUJBh1Uz5yHoyFElH2xGuTE0KIYqAvT5Uy1Ad2PoWpDi_75641fcPvTfJ0KosWX-2QodGj6g92dzXWviAd42jXDqtBeUTYnEtsRCKT5D3DLN6VO8CXcEa7uTro3stP_XUkrHKev60uKNfdJfsw16P7wDcCFUTFFvSK2rRRzvC-SLED2s33ilqHqX2UQWz5yEgGF06_G7koff3u3XZSjlC3Z8RYs5pWB1b7ycHTLaJnolQUn9FTaHyN8HztyO65011Jj5HcAMKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ym8tL4VFi0D6mSBq9OZKCtoy_DT9ctJyanN70t5K3zNXwZ9tfP9rVd_qQh5DBnXwI73Tihk4Y8RgHxIi21vFnElj2EMIrLORfJ2j42ynCqQi1vMJwfOL17cwbn6DueZngFPPAE55h6VGqilLikmXxENOZlkglhpbbEPHEw1jOtcbr0Iy1908leGnNCSfCDyAb-o8iFY61ZnqNSLVSPdN-py00ugpNoHBK-Qmj7UkBnTwPvIIQl-oSn--ZlfPpc8NMRrMLcUa19UCdbdIIKS3daX5bY70lAGTUNYBbTDgQSXmqhVZuoxihxO7B3r7EG6fJrzXjeoB_jcWvt-ge2gHrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بر طبل شادانه بکوبید
جواد محجوب ملی پوش سابق جودو ایران که قهرمانی آسیا رو در کارنامه خودش داره با رکورد بدون باخت 0-5 به سازمان UFC پیوست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/81996" target="_blank">📅 02:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81994">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyQCsI_TARFRjKN8POp8jvUGS3xFSgjcH-hqTbm87-L2rMj1A4hSGushXDgbSs3GpkmYNJN8LTbvJwL_6VOqfoTxKYwMHYCphhz4Z8SMDTy0woQY-5JWiZaKWo5EIQaU8L3Pp6JXuOSfJOpU0QwzDyr1fvSGUDskak5yJ1309ONXwuD5FOe8FV4SIL2G8_LlQiGwmYmShWuCc3VT7GENzH9EjyQgOL1wzITlc758qo_SVv5qEL_BgXMhhZwh2A-wPhJEf6G6Cl1SHaU9BZ7JGODiV1DbPEW134HlszKWrqvabBn8hxpkpRAk7xO5yA25ZeQ9uQyIlHO4PBk0aoDktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کابوس و دیگرد به اسم انگ منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81994" target="_blank">📅 02:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81993">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMyg0wbL2yTc7W-babx755BstHg981MLrpc0zfKKAw537jlQCYlFaLsdQxNmSpcA9PGIbee3FFGUaIxvmjvvm3ESHFNG84I2v3MTOGWI5ZJaB2Hzw7KvpjIT__ddbJoxbGgkwOwMUf6Pj_z1Ci-u79t0vKQdrnbIXk40PUesa-6B1jDQaguPNwfPoS9Lp9598nJHVBFDv7cb4sKrM5LeUC0OPXYli-OXTMg-8L-o_NQhZREkSaEjEW-0J3GJFgExiObHdkdvW8KVcHplxC5pJLV0UAUCNY2bpZ2kpQW5G0JeiYEUl9OD7rieygfAjgAOjDoktg00UudQc6QnfHQ4bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از اعضای سپاه پاسداران در شهر مهاباد با نام عمر دهقان در روستای «گاگش سفلی» از توابع این شهرستان کشته شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81993" target="_blank">📅 00:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81991">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این کصکشی که چتارو پخش کرده چرا اسمشونو سیو نکرده مثل کصخلا تلاش نکنیم بفهمیم sha کیه z کیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81991" target="_blank">📅 23:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81990">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTa25P-3almy0OromkfrHD-xYxvaybsrdS8Ig73vNBlTv2m8T5aNx5qvrty55cvWU65Y5t0ECYLAVCTNJZHOk_Q__pcMfiPsWfsT4uxDjpbI08IMgShRghXpC8N9QfguDZwOJ82YanBb4IsO6omcv58fDB3xpzD4vHIuH4fdw1A-Whz1qQfj4EjeK9EDtDE1hEof2-nyejhC3etwHcfiyV4_T3Ah19gngJjCUf9uU5RS2p00OrpBuJGhwIoqy4_HtCqhBziqRz6W85aMQz3FnKW81NQbFT1cpJnSpZrfyJIWiZb7oacYIYWsUlnXWu9JUTyDOQKlid2S_052ofdE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من که پیشنهادمو دادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/81990" target="_blank">📅 23:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81989">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5C0fDncY4OS9EfcW4pJIc_IVFN_eBz5bIrRj78zTweTeAkN1K3wgDrA4XlPCwlYuvPvPp1hAhrJ3bNJAFW60Udd4hyc_C614KwQ5Ef77p2kQXseX34kIdne9P8vH-zhrdJ0bPD4DQ0XjT0ftwtyi7uCBRG7wUeB75iMAgHr2-ufnkmVIwilzTDRGDDK_1eWJTHzPVlXyGrkr3_QjsMMXwuk0gYQDvJZ4O2ElUdvbYUZMRaYlDSsrXMjmYHiAa3FzYfNXDZ4y19Rlkh60i7qJKLtIqIcKulMJF1JXFAyDiGuzq8OHhtFzF-AZ30htrF-CQmNSO2FkyTSAdzjFtrNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 کا اومد به لطف بیف با بشری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81989" target="_blank">📅 23:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81988">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کار به هیچی ندارم ولی تا تلگرام هست سگ میره سیگنال کصکشا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81988" target="_blank">📅 23:12 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
