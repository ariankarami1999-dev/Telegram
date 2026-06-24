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
<img src="https://cdn4.telesco.pe/file/gGswR75z_nlH8Ri1Y0wd-o0k0yXvb5PTubho-RQISzmWvPLviyTtBBb0m2OrpMZBgt7DShVwajmQRJC8qrQ-6piwouLvVKOQ1GndH4P96b6dUh3xbmpjJxTHwuTofDaSrrDzA-QONZk-QC4DgZ92o-LB2476E4rYocH_zHo0E1U-uVZg9103qiYpC90E4QKjhThR5fFGp2IplOGN6PeVA_g0jI3itPa1CUxW5wdckzLn-3kUxlaYzcodss7edF-X7KlRKlimdWVxRRyPlF9_1XxQ34RR3mbpMNj1uB2mNoU5pJe4kfs2ElhvSrl7KGXp0Z27Kvvlh9TsEVomYRREbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 09:59:19</div>
<hr>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=IE0jq0s24ChhE0NpUuupgXHQMD9Et1XBOq6QLGMSpDA2PLBF41t1UiYLyNbmUmqUWeEAyZfBGrEqIjfiWOP1c-ON0ZSPbfA4CUtqRumsmm3j60dcjwV5QvbL8S0knoAqBN6JiOcF21HOfl0u7Wk0GNabRMcELc1L6jV43fGNjDf2WWKUzb-UHOCftYO0XqnG9briJXtt8SmNhgXVQw3AbcAdXXmp9daVX-hHs-MiK1Et9HYwltioo0LabCbCyRinSXKm3i0ffChNc6nmg5lEdgUS_X9CXQr966XdKDZgkP7nXsGTC7D2Vr3DeeN3H2rhbiXa_bv_CHAkSdAT76-O0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=IE0jq0s24ChhE0NpUuupgXHQMD9Et1XBOq6QLGMSpDA2PLBF41t1UiYLyNbmUmqUWeEAyZfBGrEqIjfiWOP1c-ON0ZSPbfA4CUtqRumsmm3j60dcjwV5QvbL8S0knoAqBN6JiOcF21HOfl0u7Wk0GNabRMcELc1L6jV43fGNjDf2WWKUzb-UHOCftYO0XqnG9briJXtt8SmNhgXVQw3AbcAdXXmp9daVX-hHs-MiK1Et9HYwltioo0LabCbCyRinSXKm3i0ffChNc6nmg5lEdgUS_X9CXQr966XdKDZgkP7nXsGTC7D2Vr3DeeN3H2rhbiXa_bv_CHAkSdAT76-O0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ffyprLgY_gk3FCwrty6_8kT1wMutnDTXyXstwon8tuvrRgi08hxqjzVPqv-KceDj0phWj96Lvs0Qa2-sQVke7ascleyn6VTjIvn0gIx-dt3VmulX4g7bNqAAzcYlVilQwvG9g2z0VYJ17DdhLu5t2ybH6sjWR5aZwJpT9HS5WJTM9xRbqg3iE4ETI6-wm2TWW6znt56-oSJxml5qS2bSQaUaXJ38X2h_dhFCy9VqQDoe5-GCHBIioByq72GNSKnfd6u5VcWnRwu9S2hHNYx5pMF84ul7dbi0GPSzFxgQ_OQjBSe7b26CQbQCd3oYn_FzEByK2x-C6I2sT1m14RSoqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ffyprLgY_gk3FCwrty6_8kT1wMutnDTXyXstwon8tuvrRgi08hxqjzVPqv-KceDj0phWj96Lvs0Qa2-sQVke7ascleyn6VTjIvn0gIx-dt3VmulX4g7bNqAAzcYlVilQwvG9g2z0VYJ17DdhLu5t2ybH6sjWR5aZwJpT9HS5WJTM9xRbqg3iE4ETI6-wm2TWW6znt56-oSJxml5qS2bSQaUaXJ38X2h_dhFCy9VqQDoe5-GCHBIioByq72GNSKnfd6u5VcWnRwu9S2hHNYx5pMF84ul7dbi0GPSzFxgQ_OQjBSe7b26CQbQCd3oYn_FzEByK2x-C6I2sT1m14RSoqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZyrLAg5Bbfw9Rh1tEQAl8V0TYYGuWDlTxMX9CtSElotiYc-Ui6rCafcyGX3CLiYcTQh71oY24EuWqNJCp7UVpOoHSW3oaZ1Ia1znSc99jY9AgQSLuesiVKjaK256GU7K2-G18FrOw3RAzuG-crxNNWQMnGcpdM6VW1miQE2yVkvArR6mi5lIDrhai1LnhTPjD8W5S35T7F-DxGBhf6EZ9lhR6DHaxH-XOjkRMpDn6Tum3c_3t9XRxapxWIr52HG-8b-DHvwkA3R1Zdi_z0_ZmHwhmDoSDHbptlbMuMLtRezwsCrdNh9hUqR6fD15lowiw2Xy0RpsOBDg9ZRRLME0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=bbdvWT_ef1_ay6zlbJqAn9z3rSY4yUslYqcfR2zv4RTqO7Xj8DtOR6jlKW7YmOtYh9GR3rxSe4wZcO2DzrgITffx_mhFOtJINnR0V0xNOoqKNZ8NC6EBLeHDKjJTtRYETaw-CUzTDtk-8z5Fz-CCdQsp2Neb-mYLTJvhmeSXcfh91ZXAchT9toyPpgPJa4KhNRVlGkelPZpKvNokMAgkeasgAnoSpwThtRwyC13hYyTiLUsPp5S36TyUhABUP1GQHbwLoqxAnhTctigVqmwd3gtqvcYUG_YR1tqltyJhXGUSF65kYB4tT-uFWLjQWMdhL_5eKR06VOuO7ynALGDTCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=bbdvWT_ef1_ay6zlbJqAn9z3rSY4yUslYqcfR2zv4RTqO7Xj8DtOR6jlKW7YmOtYh9GR3rxSe4wZcO2DzrgITffx_mhFOtJINnR0V0xNOoqKNZ8NC6EBLeHDKjJTtRYETaw-CUzTDtk-8z5Fz-CCdQsp2Neb-mYLTJvhmeSXcfh91ZXAchT9toyPpgPJa4KhNRVlGkelPZpKvNokMAgkeasgAnoSpwThtRwyC13hYyTiLUsPp5S36TyUhABUP1GQHbwLoqxAnhTctigVqmwd3gtqvcYUG_YR1tqltyJhXGUSF65kYB4tT-uFWLjQWMdhL_5eKR06VOuO7ynALGDTCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=tEZoJwDp2SaQRTEDrV0T3w1HI5OvLty90nWZHg8YvJCNTZXF_I1WJ9bm7E9qe7OFbWc_HKdNwaF9XHgYUFCYnEY_vn2k_B055ew_Zh_W0ZtT_5sjeSw9t6Otm0YIZldRbxvd4VyPZJNDh3nYz_3uLMS6Tqz9XzFNx6K_wu_r7wjXUX3sz9_njS9GNXbq4qUQMOycAInpFmEV5ATjLHXsrFrPecpZjMApSyW43MQJtVERuzZ_Zr9yXOV3lOS-t70QLsyePtFQzBqvhnWAnE4mPSF3Hb_yP5G8bal2Hkm-EALG8VFcn6C_LrAV4LSQes685xLJMdRfl1Xf3LotV1QJVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=tEZoJwDp2SaQRTEDrV0T3w1HI5OvLty90nWZHg8YvJCNTZXF_I1WJ9bm7E9qe7OFbWc_HKdNwaF9XHgYUFCYnEY_vn2k_B055ew_Zh_W0ZtT_5sjeSw9t6Otm0YIZldRbxvd4VyPZJNDh3nYz_3uLMS6Tqz9XzFNx6K_wu_r7wjXUX3sz9_njS9GNXbq4qUQMOycAInpFmEV5ATjLHXsrFrPecpZjMApSyW43MQJtVERuzZ_Zr9yXOV3lOS-t70QLsyePtFQzBqvhnWAnE4mPSF3Hb_yP5G8bal2Hkm-EALG8VFcn6C_LrAV4LSQes685xLJMdRfl1Xf3LotV1QJVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Tn7ylaltwuJWk3NFPirEk8IX8NnwFH3XBq7Bc76bqMmUZ13nurOujzteifi3JOsBr0M90PxKA2zN9FnD2fEQOrEa3hw-whUd1xcUEpYnWV-G8Jp8XAoEWt3E6Nnc2IpGowT0XkZbd4SCF7puXF4nXmuilOqF808ZtwsWxdeuBOEli08cektP-si0O6dKp1BHps9zIsRR-bOcsyAJpg6DNFq6xKzGgGdOlbl1yFCUTr38e0J513vK2dfMW5slBNpk48ClwqIeXE8kuMm-Qx64Ct8QjyhoEsNTIm8PDM7sGjV_DTSR1_Qc8yL1wK2Cf8rpsEhVUT8xcgxWlMgAT-ecAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Tn7ylaltwuJWk3NFPirEk8IX8NnwFH3XBq7Bc76bqMmUZ13nurOujzteifi3JOsBr0M90PxKA2zN9FnD2fEQOrEa3hw-whUd1xcUEpYnWV-G8Jp8XAoEWt3E6Nnc2IpGowT0XkZbd4SCF7puXF4nXmuilOqF808ZtwsWxdeuBOEli08cektP-si0O6dKp1BHps9zIsRR-bOcsyAJpg6DNFq6xKzGgGdOlbl1yFCUTr38e0J513vK2dfMW5slBNpk48ClwqIeXE8kuMm-Qx64Ct8QjyhoEsNTIm8PDM7sGjV_DTSR1_Qc8yL1wK2Cf8rpsEhVUT8xcgxWlMgAT-ecAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=sa3SZwnGxFsgucLJpb45c86AcBiuC18TRHF6WD8nk3noLF_pJcy2OR-NXyFkH4sPqvIUpJOAC1EXD3_un1z54QvKDz2DJlDe-lX3OgzeFjxmAfKhpZ4AeLLvGAbKMtdWa8QW0vz4gVUKolIG5wPVzk0Yh9y0YQpJDfWhXZe8aZT25QkNbQKdnR5soKXhTbF2gGwb8fd5Qf9ma5zsyB7H_rRlyCxY3NdPd3miWTTlfr5x6BH3ODuUFTUVmALmq_NaknE-JCShGPeDRT4_fFqt4wKPm5r_T78ncKcF9LljeySDm8drkbzgUIVdiBGlsOwieGqhuBYjlxoW0r3X9bXUUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=sa3SZwnGxFsgucLJpb45c86AcBiuC18TRHF6WD8nk3noLF_pJcy2OR-NXyFkH4sPqvIUpJOAC1EXD3_un1z54QvKDz2DJlDe-lX3OgzeFjxmAfKhpZ4AeLLvGAbKMtdWa8QW0vz4gVUKolIG5wPVzk0Yh9y0YQpJDfWhXZe8aZT25QkNbQKdnR5soKXhTbF2gGwb8fd5Qf9ma5zsyB7H_rRlyCxY3NdPd3miWTTlfr5x6BH3ODuUFTUVmALmq_NaknE-JCShGPeDRT4_fFqt4wKPm5r_T78ncKcF9LljeySDm8drkbzgUIVdiBGlsOwieGqhuBYjlxoW0r3X9bXUUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=gC-Q1_op8B-TKcwdGx7Hz0uTx593IQDQ01_qWnhm0dCJeyITi6bqLP0HwEjZUYztg95AU0amrb46XrsoID-Sy2vgxd-wBmksXJMFq4j1Gre0NLdtzMJ663oXQHg6EaLPlL_MmYjiGgcQXeFJ4cVRXmyLMylC3ML_9lfUcVC7k9Hrmm5ZzAXUU2GrOEqX9qbQGFazIxiihiN7JyQ_qgmlPk61GzLkGwTq2qp6OkMCzxSWHFSMXlthlEHytX71cEVgr_0gm9Dwbw7cIMwaTsPKI1RP6KhRFeffHwWXP2jNW1d-ZaU-XilcvNPOrL0TtB7Yd2obYaIhr2KyIN8u6ma1bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=gC-Q1_op8B-TKcwdGx7Hz0uTx593IQDQ01_qWnhm0dCJeyITi6bqLP0HwEjZUYztg95AU0amrb46XrsoID-Sy2vgxd-wBmksXJMFq4j1Gre0NLdtzMJ663oXQHg6EaLPlL_MmYjiGgcQXeFJ4cVRXmyLMylC3ML_9lfUcVC7k9Hrmm5ZzAXUU2GrOEqX9qbQGFazIxiihiN7JyQ_qgmlPk61GzLkGwTq2qp6OkMCzxSWHFSMXlthlEHytX71cEVgr_0gm9Dwbw7cIMwaTsPKI1RP6KhRFeffHwWXP2jNW1d-ZaU-XilcvNPOrL0TtB7Yd2obYaIhr2KyIN8u6ma1bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=cUM10HB9biCFz8OktSb3MKhfsCidu56cLYUUarQ1_Msv7uLc1M8n1BsEeOKJjjo2eQrMXNLpgubpFYLjI_C4eO3IFj16XFlCn5WzBFng6yBHTX7a_K6IIvK2PeP7x4DM_9nr8LYGDXRnjxc60Ioq4nOm1uClivgLclO0BIY9QMoDzYUDcNG2AEL3tDM91Wvx1Rpze0htNU8bUuOPMMZi2f4rywzR3ldkge5pdFKl3uGYje9ptYU0g5PYtfzfUYoFGP8RcTAMJPRnM9kdhb6Trn1JUhmI5K5EHgEPJNUokyXJcaahdxLrYZZ-vFJq0rioE83IhllXC0KnvIqSqvi6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=cUM10HB9biCFz8OktSb3MKhfsCidu56cLYUUarQ1_Msv7uLc1M8n1BsEeOKJjjo2eQrMXNLpgubpFYLjI_C4eO3IFj16XFlCn5WzBFng6yBHTX7a_K6IIvK2PeP7x4DM_9nr8LYGDXRnjxc60Ioq4nOm1uClivgLclO0BIY9QMoDzYUDcNG2AEL3tDM91Wvx1Rpze0htNU8bUuOPMMZi2f4rywzR3ldkge5pdFKl3uGYje9ptYU0g5PYtfzfUYoFGP8RcTAMJPRnM9kdhb6Trn1JUhmI5K5EHgEPJNUokyXJcaahdxLrYZZ-vFJq0rioE83IhllXC0KnvIqSqvi6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=IeGlJKTgWpVihaegopP9rKzRdXEt7KWHglT4ZqNwlgJ96Gltm1lRiLrtYFBh8XwUtVWbfAiHU-OEX55oDyPr-waGk3P1kMA6dro5EU74rncpnGD6LtliyCjhA2GUd1IfgsKleMu38uSowsKiQC_dAWOmyS9VOi2YfddVf_KsNGl1YAUe2mYHByOzEAYwJPVFCMcQu1O64hEJYHeTG0lm93u1Ab-7j_LB66GwRojmsm3_aqN-EkdFklj13avlgs2OjRxeO-WaHOI5FJhIkRQBeS2TZHATywCwUSJ62vtefhO257zam7gJ5E6EvFnAgboWNmIMfmP-wUuZ-wwQWA7Knw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=IeGlJKTgWpVihaegopP9rKzRdXEt7KWHglT4ZqNwlgJ96Gltm1lRiLrtYFBh8XwUtVWbfAiHU-OEX55oDyPr-waGk3P1kMA6dro5EU74rncpnGD6LtliyCjhA2GUd1IfgsKleMu38uSowsKiQC_dAWOmyS9VOi2YfddVf_KsNGl1YAUe2mYHByOzEAYwJPVFCMcQu1O64hEJYHeTG0lm93u1Ab-7j_LB66GwRojmsm3_aqN-EkdFklj13avlgs2OjRxeO-WaHOI5FJhIkRQBeS2TZHATywCwUSJ62vtefhO257zam7gJ5E6EvFnAgboWNmIMfmP-wUuZ-wwQWA7Knw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=ORDwtdeHSLgJBitX-noRS3wk64avsWQkDyXj3hV4OEWlSLlDmBLqf_tiFgEqJclXQqh43gqBlCWXF02n7Ch4n6LDkN21NwrJRTx5vN3_oRKZFTEwP8dVTkcdjxRrFuJEQfBFUPFRg1PnIt_atZ4KNQhCFTx8oBgn3M9wO8xqIbKc0ThtPhQ9fU9AstcqFSQQmtdeDpeuG885gNpZk3nD7mn37oVvkixHA0ajtx-tUSt_y59oCBsoCx4-xuiFqmGiQDTQ8Zk5LrjILU3qpl3OXZyz89Ir0XOpkM6BAvKez7Y5k7v4-VMwOypf6vbD3-zz83F3nFUqqtanP-6VkuV-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=ORDwtdeHSLgJBitX-noRS3wk64avsWQkDyXj3hV4OEWlSLlDmBLqf_tiFgEqJclXQqh43gqBlCWXF02n7Ch4n6LDkN21NwrJRTx5vN3_oRKZFTEwP8dVTkcdjxRrFuJEQfBFUPFRg1PnIt_atZ4KNQhCFTx8oBgn3M9wO8xqIbKc0ThtPhQ9fU9AstcqFSQQmtdeDpeuG885gNpZk3nD7mn37oVvkixHA0ajtx-tUSt_y59oCBsoCx4-xuiFqmGiQDTQ8Zk5LrjILU3qpl3OXZyz89Ir0XOpkM6BAvKez7Y5k7v4-VMwOypf6vbD3-zz83F3nFUqqtanP-6VkuV-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=ioKdt1gFn-q1ysj0HHzhBxulOO8VFcMStzIIM433e6Ryh-KU5OB-hAlYlmdzzgPwvOhdtGc4mzN77BmF_w8PDqXJ_Q9GNfPGkJ3OEIzCNc8rAnc-JJJDNlIAqW922AQZ4C09OGpZeavmqqbaQANvIh18KcGCRoqdXMfQ5ZL9sgVBdI6Y5wMTDuq71VtvWljYGwFsWfTCbMhZ3f7EVxZaTnC31i3LN1kOy7fuqVqS5iVOSSBDsOXXXLRdg4wrpfgiHlv7MPr9OgCMTFBJfm4-Hl7o3Bh37lTKvxt2udzL8gff0rwz49QlYynFhYlQ-GYpNUq3KD2J1plKEyzoKhc28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=ioKdt1gFn-q1ysj0HHzhBxulOO8VFcMStzIIM433e6Ryh-KU5OB-hAlYlmdzzgPwvOhdtGc4mzN77BmF_w8PDqXJ_Q9GNfPGkJ3OEIzCNc8rAnc-JJJDNlIAqW922AQZ4C09OGpZeavmqqbaQANvIh18KcGCRoqdXMfQ5ZL9sgVBdI6Y5wMTDuq71VtvWljYGwFsWfTCbMhZ3f7EVxZaTnC31i3LN1kOy7fuqVqS5iVOSSBDsOXXXLRdg4wrpfgiHlv7MPr9OgCMTFBJfm4-Hl7o3Bh37lTKvxt2udzL8gff0rwz49QlYynFhYlQ-GYpNUq3KD2J1plKEyzoKhc28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=M154quwvTeYLFg_OaCdL7heXOitg6TNs0vpjk-yU3gzYWumPIYZzIvfTQ97QpYTOer2zVqd1dH4j9L5-YiinK1Ty59uxVHK9n8G9ELD9KbtGdnDzFuR-QkvbI59dPaEDk2J0Mvp_3zT9kO-WH3mArMvGxlMLu74EskPImcNqACkDNAFNgqDWNVp-kKTziksEpAVSw00E_LQbI41D12GHejpi_JAKVC4tCewYAziZgftB03fTkkIqRN8LgelWggIhk9gdoFGtHvSNWr8ssj2J5JsCRwnb3a2wueaGsKHbHI5PSJXBrjdAex5KvHNnHuiALSzRMkjP7LUet_20O-Bmxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=M154quwvTeYLFg_OaCdL7heXOitg6TNs0vpjk-yU3gzYWumPIYZzIvfTQ97QpYTOer2zVqd1dH4j9L5-YiinK1Ty59uxVHK9n8G9ELD9KbtGdnDzFuR-QkvbI59dPaEDk2J0Mvp_3zT9kO-WH3mArMvGxlMLu74EskPImcNqACkDNAFNgqDWNVp-kKTziksEpAVSw00E_LQbI41D12GHejpi_JAKVC4tCewYAziZgftB03fTkkIqRN8LgelWggIhk9gdoFGtHvSNWr8ssj2J5JsCRwnb3a2wueaGsKHbHI5PSJXBrjdAex5KvHNnHuiALSzRMkjP7LUet_20O-Bmxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve7P93zhgyCbzKLF-KHp3jc6kto9hMd9H-eEqTku5rmrhVQm9CiBkgmbkvIF_UJJB2yJLXEpo3HfZfi8_7qALz60J27Kv8arP7mjbYCZBBWnAQR9o41TaefH9_AhJ1M6Z6U77p6k9AYJBVs5pdYF-YyuRGb62-5WYdJTQ9zC9Q7KNaFR5NUg772oynKPbgU37kIYY9b60mEPy43_CBZwV7SmPLUvtzsCOkEsZ2fvHPQ1lPxGjNz7ClMTJdSRbWp-q2pgSpULr4CqTtkAee-0XJdygfsDy65oOSM8wepkkBd0vqblHK47ghK0FcMrR7aSlr2lYGwgrLOr5erZRMWkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYYPR0TGhNcDHvHunkwLlaS294kiOgkRyBiAfEuHeuE4Aw39OrIIMa19exNWnrozECeAMv1hLJg4CpnmI3GJ6pFR7EfykWeZXl9lPNYv8GL38gzQWSpZ_ZRtXqe55LitXcnfKbt0SQMg0-jtMKivfGwniwQEP7s9lCA_gCddVZsYT3Wz_7ZQb6Ow8wgyoge0NiDHuHT0Bmw8DwVgS-xrkdI4ijW9UDEFRKtdoZa7F2y33CdY9hMpABcCTwXqTyYa4-3JmsAnv07knGt6VGGtYxAilY3s30FtVPo05a_vGHS6CVql9dYe6xxirUP3739ODpTXVVmYBPKuyCG9PS4c9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=MGCssVA7nPEgvEe0DZIeXKOiItnZuhH5uJubAv3xg97jlelK_0TCAGHbaOoXHKXdPwfEs29wm9C55hTDONHw0e01B7AwaZKGLZJW9iJX0X4Mal5yWTiE1VOY4GbXENxnF-XMIl-dsC4olNkiR5G0ZU8mdgn9QyaEeC7FCUgoJS5-IUIg3lruiIQyMPJ05O8igSDl-ybpcHpF1aMclkfzlI2Yt_BmQfwwOqh1qQo1UlBTr8etCg9hADxwHvz8YSUc3B7BPfPOTuMK8DHjRcTCGn24JBPCDYbALwV_0CXT_dnBHh8kyf-Ufs-rDi7UDOXUHgK3sYVO0tuU16XJkPfTNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=MGCssVA7nPEgvEe0DZIeXKOiItnZuhH5uJubAv3xg97jlelK_0TCAGHbaOoXHKXdPwfEs29wm9C55hTDONHw0e01B7AwaZKGLZJW9iJX0X4Mal5yWTiE1VOY4GbXENxnF-XMIl-dsC4olNkiR5G0ZU8mdgn9QyaEeC7FCUgoJS5-IUIg3lruiIQyMPJ05O8igSDl-ybpcHpF1aMclkfzlI2Yt_BmQfwwOqh1qQo1UlBTr8etCg9hADxwHvz8YSUc3B7BPfPOTuMK8DHjRcTCGn24JBPCDYbALwV_0CXT_dnBHh8kyf-Ufs-rDi7UDOXUHgK3sYVO0tuU16XJkPfTNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=nALPpqNIOWkll96fKwOfvgnro5A_UGj5ysqmBQ4_5TF17tQJ0xuUOOMZzPjAclS9Gae2p7ug6v-4MR9SUrHhDbvjnMqaU1cd4HLwP9rTecAulcWmhm-sfWD2iM95pb2l0M9lCTAqRDkLZ2Fp0hCAaTnr2EOJFqD6uqdvPZy2bniEoBfOs1A_ZZ_Htjh4qeLm9fdGFmIs1y8WoAgX5iYWh2pOIggKKZt9Jyp47SQ-_rtTyGBFL9Eh32ujsRpdkOryCNDR6pRIi873b91KOjIQhg0y_99i6q0IM1awS2grVvwtYQ4xgjW0u_13tzwYMwMVwjkhGXq66Gzz1bt1dmtjQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=nALPpqNIOWkll96fKwOfvgnro5A_UGj5ysqmBQ4_5TF17tQJ0xuUOOMZzPjAclS9Gae2p7ug6v-4MR9SUrHhDbvjnMqaU1cd4HLwP9rTecAulcWmhm-sfWD2iM95pb2l0M9lCTAqRDkLZ2Fp0hCAaTnr2EOJFqD6uqdvPZy2bniEoBfOs1A_ZZ_Htjh4qeLm9fdGFmIs1y8WoAgX5iYWh2pOIggKKZt9Jyp47SQ-_rtTyGBFL9Eh32ujsRpdkOryCNDR6pRIi873b91KOjIQhg0y_99i6q0IM1awS2grVvwtYQ4xgjW0u_13tzwYMwMVwjkhGXq66Gzz1bt1dmtjQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=oTqigYBw3LkRmnkGqM3kUl-n3eBzdML7Nx970_iM1qa4KcCsuZ84xD_C8UEtnKhGNg0gyt465bINdkKOq3qe9kIU4j83pu-LUDF0VmiiHHByuROrd-y1S3kn4YkTPsvNpTtrAaWu6ciBHz2OglzDt8zDbNN4kkMQ-HZEDIHDZlmgpHMpzjBbXyi0WCjJGrVdI0ysd3YydNyKr3dC5E3jfXT-Zd8MtjRXZ7A9P3e4BJCUN-FG_HYz1mAr6GGxuTJrDhFAFi2oGGdt-gqZvWGVXUOS59je71-izIR-dadQMgh1jdo53YBd0Nh_KS21uwGxIUOs3cLs_-9sCo0Ca3ftKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=oTqigYBw3LkRmnkGqM3kUl-n3eBzdML7Nx970_iM1qa4KcCsuZ84xD_C8UEtnKhGNg0gyt465bINdkKOq3qe9kIU4j83pu-LUDF0VmiiHHByuROrd-y1S3kn4YkTPsvNpTtrAaWu6ciBHz2OglzDt8zDbNN4kkMQ-HZEDIHDZlmgpHMpzjBbXyi0WCjJGrVdI0ysd3YydNyKr3dC5E3jfXT-Zd8MtjRXZ7A9P3e4BJCUN-FG_HYz1mAr6GGxuTJrDhFAFi2oGGdt-gqZvWGVXUOS59je71-izIR-dadQMgh1jdo53YBd0Nh_KS21uwGxIUOs3cLs_-9sCo0Ca3ftKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=F3gbZhg_dc08_CykpL8rFmYEBLofWASd40blwy9Shz5AguALFoBId_mXJilQi9m-tP17vsD_M9mywJGbDB4-JEDYj8-sSLVV4Qiopw6OCFcOvJmRXfjtMdQfPsDiAo1uUjNxYYy1ZuCGYqBM8l6WH91z9SZZDk4cBNaltmuBX3t3OIM8erAiol3lh8M-fgnuueNhy6lBF6FHFOdAfuq6CjyjGxWGIdqzl2F2XKL8hw6QOyQt5m2A1tp2uDqcbZRc3C05LXH2BYvlzO1hEGiUBi79ATy3ivGC7ieir33XEMSJlTmhyo0PMHGLIwdyS8CwOWqG_129SV3ckpJb-fqBiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=F3gbZhg_dc08_CykpL8rFmYEBLofWASd40blwy9Shz5AguALFoBId_mXJilQi9m-tP17vsD_M9mywJGbDB4-JEDYj8-sSLVV4Qiopw6OCFcOvJmRXfjtMdQfPsDiAo1uUjNxYYy1ZuCGYqBM8l6WH91z9SZZDk4cBNaltmuBX3t3OIM8erAiol3lh8M-fgnuueNhy6lBF6FHFOdAfuq6CjyjGxWGIdqzl2F2XKL8hw6QOyQt5m2A1tp2uDqcbZRc3C05LXH2BYvlzO1hEGiUBi79ATy3ivGC7ieir33XEMSJlTmhyo0PMHGLIwdyS8CwOWqG_129SV3ckpJb-fqBiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMzliEQINyK0rc6nS_kzPQlNY1f3JZ3HoxNWll-vU__F6j-5Bjh3WSKmbIyccxHriJd3KhOVXs8tGRmxD6_cdtqEbdXDUP6TADNKOPf_jsflt6marIi3Kmaj3gVzbSUPsXqtFp2wjZjFFpLyBG1xnukATwkZo9s6pWjgTwJu41IHvQppt5WZauYX7HRmnM0hpsFAR03_x1dLUdm5zDL7CK5QC_XGvoCvxIunMqekzfMMIAFARUrPFsoynW497643ZbaTtqjk56GkOO6rK1EE-wkeGyiTsxJtU7_gvaRnzz-Ov1EqrHuRbot7mbFp0ijOOSeRKanD6YezeyAQCaoFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCjAD2IkWHJ2rOzGRvoIoeNCwl1Ty9rAee4S7qxGxfSBQQf4B3h9hAiFQLHzWy7FTY8JXkJ-xVwMPatLVfpe5FGKQQsmdEhqkGolpiZS5QBqKnjOqqcKnbCLuXwXGnvYSdA69BoAqNAPMnGl-6mc5IYISk9CmWSB-ciabch28SAULLX-ypIgnA_TtRelmOczVCRl8F8064tN6f2sdceBY_Wth_MhHzE6VkK9Uizr9gKi01SZ7dF0XygoIDbtW5m6zqm2J-n5XZPKD5NhHisRki9Ad7TyWGodJD_IbGtkS8gj15MqQz13kI7hMHPrR3-laOxxzAcUtbuWlALb_oOOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2n6OjDDP_cAqS76SYdXkYjTJ4T7HchDXQX43WTwvBQyW_A5-GCm2F8qQZngpZz-Q9LbbRRH8uJ-Dq3EecZrt4uIDLFOeSSRCCCj7L90Ob_1hJLtJfP8BVNwznIuyxYWfDIkPQHW9sPs7D3FnWpxGazc5-7pvsQRsD8AheYq1-uVlMl9weBKiBPFrRvjDsH23KZpPRDt_7P-G7z8OV84oV6lUlFmDfR0PNcvCWAecdn7AdswN5xsq5NlvV2gAgbDlgO_RDN-Te9zwn167Ki2Fvq-I9ZraKE4KWnVr3WepL_MhN9yY701umwlJMvFyD_ClxmvLRw1-AATdGLFVIkOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«با وجود اعتراض‌ها و اظهارات نادرست آن‌ها بر خلاف واقع، و همچنین هیاهوی مداوم رسانه‌های جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند، ایران به طور کامل و بدون هیچ ابهامی با بازرسی‌های هسته‌ای در بالاترین سطح و برای مدت بسیار طولانی در آینده (تا بی‌نهایت!!!) موافقت کرده است. این امر “صداقت هسته‌ای” را تضمین خواهد کرد.
اگر آن‌ها با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای در کار نبود! بر اساس این توافق و دیگر امتیازات مهمی که ایران در حال ارائه آن‌هاست، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی دیگری اعمال نشود.
با این حال، تمام کشتی‌ها در جای خود باقی خواهند ماند تا در صورت لزوم محاصره دوباره برقرار شود؛ هرچند در این مقطع چنین چیزی بسیار بعید به نظر می‌رسد.
پول‌ها و/یا منابعی که وزارت خزانه‌داری آمریکا آزاد می‌کند، در یک حساب امانی (Escrow) تحت کنترل ایالات متحده نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از خود آمریکا استفاده خواهد شد؛ از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما. ایران به شدت به این اقلام نیاز دارد.
این یک بحران انسانی است و من احساس می‌کنم که لازم است همین حالا کمک کنیم، پیش از آنکه خیلی دیر شود.
گفت‌وگوها به خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=QRdbyjgDTyxEClYnl6oJcmzS-L8uUkms2x4YyGiGGcF7w7QY8H35WENr-0-xmbMKzmehhI47F5gExKuxqQlq41689I_qmPI6NvA0HW3D2XrOwyiv9pjZjjN3tzJTbGfp6R70z3DtN5pl4lP3Vx9CAuNSxZSS_FX6RSj43U4HPEtt-mAWUEjMVgzICVBLtUI7-PejoL2IruUzmWK6sf6sZqMFBeC5tSLHKWaOVIxmA0umEoR07nb9ZjlYehaBjqEztI94-7rWr-MXFU5SlyEzULhdjlpcPnzk9UpsYYFxiNS07FjRX6v5Roq5oW5CyrmOkcjcN1vJIh7V5kgUKH_xSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=QRdbyjgDTyxEClYnl6oJcmzS-L8uUkms2x4YyGiGGcF7w7QY8H35WENr-0-xmbMKzmehhI47F5gExKuxqQlq41689I_qmPI6NvA0HW3D2XrOwyiv9pjZjjN3tzJTbGfp6R70z3DtN5pl4lP3Vx9CAuNSxZSS_FX6RSj43U4HPEtt-mAWUEjMVgzICVBLtUI7-PejoL2IruUzmWK6sf6sZqMFBeC5tSLHKWaOVIxmA0umEoR07nb9ZjlYehaBjqEztI94-7rWr-MXFU5SlyEzULhdjlpcPnzk9UpsYYFxiNS07FjRX6v5Roq5oW5CyrmOkcjcN1vJIh7V5kgUKH_xSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=dmhMIv4Y183I5Jurb7prd_KXHW8QGTvvqJ3ryE2w61eed9ce03MkYMTbYPm7hGvy2b4e1iOpFAU1Oqk-h2N4P9Ua8xSTmsNsymM_R9iDsyBpiiu0pdUvC045sNVZ_l2_rCVWs4odm7Mtm7vLfmYrP8sTeg19dNdb3BlpG7fUn9whBPyY825hb2TsG2tqyy-7AquDiOVNJGN1q8DGlzjFip_r1zyMIa1Uf1RHuS5LRtaQueuJxZUih-hPh3a6hqxMt0PD0ndV8JNnE8OLKghriRaRqd5nDfn7g2jg0suIYGq9gFor3oCiQ7Qlc1KgdRRqvb9I5adxrLjce_uoTCbJPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=dmhMIv4Y183I5Jurb7prd_KXHW8QGTvvqJ3ryE2w61eed9ce03MkYMTbYPm7hGvy2b4e1iOpFAU1Oqk-h2N4P9Ua8xSTmsNsymM_R9iDsyBpiiu0pdUvC045sNVZ_l2_rCVWs4odm7Mtm7vLfmYrP8sTeg19dNdb3BlpG7fUn9whBPyY825hb2TsG2tqyy-7AquDiOVNJGN1q8DGlzjFip_r1zyMIa1Uf1RHuS5LRtaQueuJxZUih-hPh3a6hqxMt0PD0ndV8JNnE8OLKghriRaRqd5nDfn7g2jg0suIYGq9gFor3oCiQ7Qlc1KgdRRqvb9I5adxrLjce_uoTCbJPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cliyiQtJeDtrvxNodcO9ojJCC0huLxON1ikWOmOOlr2SC_rLwAsrl4GI0Heli_oHUQSv5pU7F4hpBseP-R_pudeJYAvOcAUDFE1pRtFOwu08DMcVzY6WV-L_f2C9CFSulul0kb7ULtddmp_QQ-w8vrlYpiX6iIIcj0tFhOBIts_H18LYsB3wvInzBJlmrGMdd0VSH2N7Yon3KYAWRhMVuNm-tad8Y_V9dfPvrXeNYOB3QQ1LGWRMuPI0wa8tYhnWWk7E061NkVeGHF4A1wLDBW_NrWB_v47xiZvQSsPUtvLrBMoCd2v4QqvRtobMLhm1r9tfYLnSLIy66X5W14SDTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HjBN8Vjdtfv6OSk5UVlvcZ3wAA1YIRFUgB6EDECbgu27S-aEDIt8oCe9nPtWbHvrFBVl5tRDDSnFSIDVIZ4hic0yE_1M7LwT3-MMj6ANxZx0yErEIpUMyRqrzH2EhB5b6E3NTK1l2Q8DyVAPZsktzuj8ZHJ3yKsa1m2wPBLhGTtHCwswTmREcY8A0EcMQjsNOvDdsI3juA-spMkJ9MBCGRS8Wzriqlk8CGUcQkE-rpFnCFI5HMHaNbyLzGH3mXJt2R2cJnZVkeKs1NY8CB_NxlKRN_jOjVuv33rTV68d5epZ83JUgqBizxNR5TuR-GXdTBROjt_HPUn_aoIfgSRrvR2xIYCRP3nrgugEsga8RgqD-jbUNZEWWuK8ewpjSw55iDFLno9jAoxC59f1H2iKfGOPB00dMAM39uRMzj1SHzugq3UJy3Drbw5Tj819WVK01yqh0Eh7h6FS5h3NfLCK-qfu9BPpi6Y4MxCVnxyeBK-lTnGJZAcp_L0V_dHiV2d2cI26RxGIJzXG0YzedsM9sD9y5IjmCpEDXaXij9eXOLOyyauLyCQpDPG6SXpK2RF7tsI48n7s9vnGCJ_tbn2YDyYkL_5mj0hrIaxcm8fq_2B7j7HS4ZtEehnZitdUPUxLe75Km2HcGm9Ky6ujpXigFcGVx3oCFztSV3-In0GbY78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HjBN8Vjdtfv6OSk5UVlvcZ3wAA1YIRFUgB6EDECbgu27S-aEDIt8oCe9nPtWbHvrFBVl5tRDDSnFSIDVIZ4hic0yE_1M7LwT3-MMj6ANxZx0yErEIpUMyRqrzH2EhB5b6E3NTK1l2Q8DyVAPZsktzuj8ZHJ3yKsa1m2wPBLhGTtHCwswTmREcY8A0EcMQjsNOvDdsI3juA-spMkJ9MBCGRS8Wzriqlk8CGUcQkE-rpFnCFI5HMHaNbyLzGH3mXJt2R2cJnZVkeKs1NY8CB_NxlKRN_jOjVuv33rTV68d5epZ83JUgqBizxNR5TuR-GXdTBROjt_HPUn_aoIfgSRrvR2xIYCRP3nrgugEsga8RgqD-jbUNZEWWuK8ewpjSw55iDFLno9jAoxC59f1H2iKfGOPB00dMAM39uRMzj1SHzugq3UJy3Drbw5Tj819WVK01yqh0Eh7h6FS5h3NfLCK-qfu9BPpi6Y4MxCVnxyeBK-lTnGJZAcp_L0V_dHiV2d2cI26RxGIJzXG0YzedsM9sD9y5IjmCpEDXaXij9eXOLOyyauLyCQpDPG6SXpK2RF7tsI48n7s9vnGCJ_tbn2YDyYkL_5mj0hrIaxcm8fq_2B7j7HS4ZtEehnZitdUPUxLe75Km2HcGm9Ky6ujpXigFcGVx3oCFztSV3-In0GbY78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=e-r-sP5vNkoIKhFrq54oADfN2SEfucOQZEmjm0hcp3XEQT-QarsseDOKg69DWnoSj7raakKn90XaLTPURMUSWwabkMZLk-bGep2BJCDmS8qEwV5Nxq_Kz_E3Kwf--3JzeGG3ntJb5l9vt0B4DKoi3SRPWYYOovZjGahp49n0yuY644bdLrbSnuF5_lGqGYgjusxfz-y6m29l1nck9UEWIgiFiTQfRGBjelek1lKMO3iV78ijQ2s47D1iYiW6YnKYpqHe4oczFLrO17EJJEe1K5NroBiyegnHrMFq2BVakauhDddV89EwRaaCsP_pdO_uGOFAH75TXwUrLAGPGhmwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=e-r-sP5vNkoIKhFrq54oADfN2SEfucOQZEmjm0hcp3XEQT-QarsseDOKg69DWnoSj7raakKn90XaLTPURMUSWwabkMZLk-bGep2BJCDmS8qEwV5Nxq_Kz_E3Kwf--3JzeGG3ntJb5l9vt0B4DKoi3SRPWYYOovZjGahp49n0yuY644bdLrbSnuF5_lGqGYgjusxfz-y6m29l1nck9UEWIgiFiTQfRGBjelek1lKMO3iV78ijQ2s47D1iYiW6YnKYpqHe4oczFLrO17EJJEe1K5NroBiyegnHrMFq2BVakauhDddV89EwRaaCsP_pdO_uGOFAH75TXwUrLAGPGhmwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=Dku5zEvnHh-SSikZHc-pH5hjzleO34EFKybUqVSchFi0c_OuerZdqDo6hf-5DhIVSSFBId_zQel8XDQ7JLbxQ8ZjD670NY17fF5LUqkeoHf7NbkgWin-GHyiO5CNK7YMIvHFxjeU-N7EKrKGzhuZ3NYr3CF5BgLZVx_qjlY7SGy6Fm2MLyU9e1nd_o1azS4VG-5di9QErDlhX4NQFgB0IXvVlwjZcccBm3j-xoIr9-KFZ6xrN389bLcxZtYSZnFMqNI4F91rHMWZfn7tAqgnvIoSlVvz-XthdUngUCe5KOnOKj7AsnfqU-wlByPpFZJkr7wK2I2Kk3r9EwWIN-qJ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=Dku5zEvnHh-SSikZHc-pH5hjzleO34EFKybUqVSchFi0c_OuerZdqDo6hf-5DhIVSSFBId_zQel8XDQ7JLbxQ8ZjD670NY17fF5LUqkeoHf7NbkgWin-GHyiO5CNK7YMIvHFxjeU-N7EKrKGzhuZ3NYr3CF5BgLZVx_qjlY7SGy6Fm2MLyU9e1nd_o1azS4VG-5di9QErDlhX4NQFgB0IXvVlwjZcccBm3j-xoIr9-KFZ6xrN389bLcxZtYSZnFMqNI4F91rHMWZfn7tAqgnvIoSlVvz-XthdUngUCe5KOnOKj7AsnfqU-wlByPpFZJkr7wK2I2Kk3r9EwWIN-qJ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=owK-i10cAEN09HkSvJpkxiRah9d5KorI-o938Vg3ZAyWWIbq-wEJv5o-djzBAkaB8y19D_RP81o0WzxBwqTaiAWiErLH3DmFTnSHmhNypjqmD4GyQxYL55-Al7OuI6jI3mWYTsSQNu-UtxHBkHCCpiahFZ-0p4NkqQLwffUd_EAd3InCUVd1PGUuh_fC06FL5Hb7eFvuJDqWwebtdhVai8oXplV6bhdLgCeQDhjjH7bEDhYyqQrTh4ciEPKiituLhg2x9BIEM_dpZ7BoEdlQ67srOFAzqOZJTZ_MfpDEI7KwbF7yIymwEgaGpryDhxiZ3oVd2b5JcG84_dSDXV9C8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=owK-i10cAEN09HkSvJpkxiRah9d5KorI-o938Vg3ZAyWWIbq-wEJv5o-djzBAkaB8y19D_RP81o0WzxBwqTaiAWiErLH3DmFTnSHmhNypjqmD4GyQxYL55-Al7OuI6jI3mWYTsSQNu-UtxHBkHCCpiahFZ-0p4NkqQLwffUd_EAd3InCUVd1PGUuh_fC06FL5Hb7eFvuJDqWwebtdhVai8oXplV6bhdLgCeQDhjjH7bEDhYyqQrTh4ciEPKiituLhg2x9BIEM_dpZ7BoEdlQ67srOFAzqOZJTZ_MfpDEI7KwbF7yIymwEgaGpryDhxiZ3oVd2b5JcG84_dSDXV9C8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=OCdz6OWQkOMf03om0_PqD3zO39G5ff9mMFeuiu0Qg75EoyyHtBjXk-eHOrJkE0C4BeZosNAutViB1xDcW3-LlesXT9gejMPuarQfAxjLuT2zitKN-CgpB6o8A-G7-F94Z4WdoI50FdMPY4DJiVrKIuFylJKXjSMhNma9QVI7cligl7chE3Pizp-a8igBzfkodfg-IpKqc8u-f1KS2ASqVxVcbymT9fHxzhOgXJJXR5C_IUZ-VwlSREjrohakRVMmq0UP9TNshGDGnNbDBMlwQQUSVEUku8qnT2lBcrExAr6ghhnKkQacYFBHnrJHmVjhOarDaXMO9acehDHAw-4OtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=OCdz6OWQkOMf03om0_PqD3zO39G5ff9mMFeuiu0Qg75EoyyHtBjXk-eHOrJkE0C4BeZosNAutViB1xDcW3-LlesXT9gejMPuarQfAxjLuT2zitKN-CgpB6o8A-G7-F94Z4WdoI50FdMPY4DJiVrKIuFylJKXjSMhNma9QVI7cligl7chE3Pizp-a8igBzfkodfg-IpKqc8u-f1KS2ASqVxVcbymT9fHxzhOgXJJXR5C_IUZ-VwlSREjrohakRVMmq0UP9TNshGDGnNbDBMlwQQUSVEUku8qnT2lBcrExAr6ghhnKkQacYFBHnrJHmVjhOarDaXMO9acehDHAw-4OtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کریس رایت وزیر انرژی آمریکا: آلبرت اینشتن ۱۲۰ سال پیش مقاله ای منتشر کرد که...
🔴
ترامپ: برای هیچ کس اهمیت نداره
😂
🔴
کریس رایت: به نکته خوبی اشاره کردین قربان
.
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=L8tUlGBz1BBaJRFncf_b71SCNbiWsb9dYfx4b1hEhsZhk6mi6F0M6pfuExSgkMKnPjYrTH852gWAHRmsD7UnkY_06gG4_Z39jaPsC8ei_raV7ubGmXcc-7VQsW-UhCzannx63dmCjThcEvV3WD4H93lEJqebL6o4VP6t4Vc7aBU1aIwul_bvbD249xEEzM3B4WWVEmHYysORfPwCHDh0VKDocuJgJZYui-Wz_2Fui4pAHNk6bCX49pRL_MZZfMmxEKtmNpGUrWgpnwZM1_H8LS5LvJf6Iff687KrNgDRbvvSN6SO3lS6vkyCCQZlls1-nP0YDxsQ9_beM8My2et6MVs2Oj0hYER0gvlQZbSgKbmt96pXMqY4QqXGWqeQBQwNARWZ7TBHaua6ShwvX33L4JEPY__MCrcGkCjQGsnN16AFx1wMG1X5izk1U5zM7GWAXyilIOPrILxMf_K-fItBBEpX24ZfONJnSrfo6BBTHBwDxx4u2R0jZd0X4z9XHt4cTdNn2x71UkF2yJGxiyeaCwvpY8y2higrEZRgwQ3R60yO2n7u0Sa7HydARAiNn0HJCDRCnyXX30Jnkt-fcThwIwCONIpkak0gKzf5wbbe1q2kLfGb0s7bpmZuPuRekkQ3EmoQHjaZnWbVXtig3e11odxoj0pSF4Z_5A4xBBg_XpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=L8tUlGBz1BBaJRFncf_b71SCNbiWsb9dYfx4b1hEhsZhk6mi6F0M6pfuExSgkMKnPjYrTH852gWAHRmsD7UnkY_06gG4_Z39jaPsC8ei_raV7ubGmXcc-7VQsW-UhCzannx63dmCjThcEvV3WD4H93lEJqebL6o4VP6t4Vc7aBU1aIwul_bvbD249xEEzM3B4WWVEmHYysORfPwCHDh0VKDocuJgJZYui-Wz_2Fui4pAHNk6bCX49pRL_MZZfMmxEKtmNpGUrWgpnwZM1_H8LS5LvJf6Iff687KrNgDRbvvSN6SO3lS6vkyCCQZlls1-nP0YDxsQ9_beM8My2et6MVs2Oj0hYER0gvlQZbSgKbmt96pXMqY4QqXGWqeQBQwNARWZ7TBHaua6ShwvX33L4JEPY__MCrcGkCjQGsnN16AFx1wMG1X5izk1U5zM7GWAXyilIOPrILxMf_K-fItBBEpX24ZfONJnSrfo6BBTHBwDxx4u2R0jZd0X4z9XHt4cTdNn2x71UkF2yJGxiyeaCwvpY8y2higrEZRgwQ3R60yO2n7u0Sa7HydARAiNn0HJCDRCnyXX30Jnkt-fcThwIwCONIpkak0gKzf5wbbe1q2kLfGb0s7bpmZuPuRekkQ3EmoQHjaZnWbVXtig3e11odxoj0pSF4Z_5A4xBBg_XpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=Gv0TzzFoeQ7fdSpN7EpjGY92QZqmcjoVCYQ9ot4cdeh-0jbS-qgKnhSwLs_T8emS8eiKEMUWLwNxqFj0jMElC1MSwZn1BDFSf0kuW9CDusnyTOM3USSJBpTWxNchVwrYEGy66fho93L-6SVH-L34QLzWveu_sWfdqF2uJkVRFDOobv298WFAwspeVBmQqwzGs84K-TOxYi5yaF58stsDxbQtgyrdfm5jc1CNfaRABkwcwD-TktV2LaJg6CuEP66z80nHg98Qwo4_ZEgetOAW42yBxK7odgp7fwFSL8PrnDrGW6mfBh2qCLWn1W7frYaQ_pGcWVAz59LVEJbm6N4BkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=Gv0TzzFoeQ7fdSpN7EpjGY92QZqmcjoVCYQ9ot4cdeh-0jbS-qgKnhSwLs_T8emS8eiKEMUWLwNxqFj0jMElC1MSwZn1BDFSf0kuW9CDusnyTOM3USSJBpTWxNchVwrYEGy66fho93L-6SVH-L34QLzWveu_sWfdqF2uJkVRFDOobv298WFAwspeVBmQqwzGs84K-TOxYi5yaF58stsDxbQtgyrdfm5jc1CNfaRABkwcwD-TktV2LaJg6CuEP66z80nHg98Qwo4_ZEgetOAW42yBxK7odgp7fwFSL8PrnDrGW6mfBh2qCLWn1W7frYaQ_pGcWVAz59LVEJbm6N4BkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=IN6Uh8g_EksURo2KfubdqeE-sGBcLzhJGRLI0GlfRNxRm3rXKoCgmULVgNTnhsziPVFvGrM0jqkk4Yh2yPp2GRzHcFQqd_nxw2FERMUkTxJsCcCuNTT-VKCkEXfbRKhMWB02t7QbRMvLvmkrOyxeDNcb-AJdPu9ZxUWnMO9LGYgFxkqWti3gjmxQX-SeHiLp9rxOAeZl4pMECY8-v7HyhAqLpXyt-5U7GJ9YO0wBqU964q6WE9UVMM0KJj6Jf1lncpSm5QRBzt-kO7_OMXYJRaZR_lFTT0MTo81uj-sAW3N1viCTWKQTVqhFY_pXbeEGvmE7gcxZiF-WnfSHKil8QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=IN6Uh8g_EksURo2KfubdqeE-sGBcLzhJGRLI0GlfRNxRm3rXKoCgmULVgNTnhsziPVFvGrM0jqkk4Yh2yPp2GRzHcFQqd_nxw2FERMUkTxJsCcCuNTT-VKCkEXfbRKhMWB02t7QbRMvLvmkrOyxeDNcb-AJdPu9ZxUWnMO9LGYgFxkqWti3gjmxQX-SeHiLp9rxOAeZl4pMECY8-v7HyhAqLpXyt-5U7GJ9YO0wBqU964q6WE9UVMM0KJj6Jf1lncpSm5QRBzt-kO7_OMXYJRaZR_lFTT0MTo81uj-sAW3N1viCTWKQTVqhFY_pXbeEGvmE7gcxZiF-WnfSHKil8QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dZPkT5iOH0T9QD6Gtn6_IcM42sNGScCfy32HSx2Hx5vZDG9a_KrFL6aUF_zxQtrO_voeLIkj6vnCoFvpIllpJ5K8GdINBgV5ZNQLcU05BM4osrmibdaV1moNk4dWhgNUPdPQPQAHtAL4nrtJnQqYCKx-Pn1UNbD2oq9jvisYNk-lfRcR_rjvo8Kxzu5dlruTzXBHUjZkoZmLfWz5sFMXnSjy8PEO5rLeglzys9kvSw5I1nnQoo8a7K1vVO_y5fJGwwpsRRx9sae6wLiVls5f3auhcwu62GF2tq_UVBrYfZcu78immAFoqWOY0PCbsPtMUVU5WDTK5zqXCz_pIrf7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=O_UVT28WYWVdj68O31NWCn_S90afBJMI8OLqx0Fi1jh2r94jStq7LSHloPaHxJSCHm_I0_Ax-xsRyH1efztRrpv1pe84em4nQCCFElH0O1buEkFr5eTIrcbNzSF2xteB8781D2YxhgJFJ71q3TJxJIdSwNde8dHK45dFe9DjAaXym_FZZJN4brp2wHtTdbw827jXz6uUX74ZayrNmjNhtKNzzzBEWEtcYWgbBU7n4wcJQlITgddCwZ10y50vDW88zwSJgSfxpDAJwK97sahzK95U-3MTsp3O4uEI7fTky48sEX4KFTYJam1rJ9s66YIHcoKdjRxrpuikhZq29-yKug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=O_UVT28WYWVdj68O31NWCn_S90afBJMI8OLqx0Fi1jh2r94jStq7LSHloPaHxJSCHm_I0_Ax-xsRyH1efztRrpv1pe84em4nQCCFElH0O1buEkFr5eTIrcbNzSF2xteB8781D2YxhgJFJ71q3TJxJIdSwNde8dHK45dFe9DjAaXym_FZZJN4brp2wHtTdbw827jXz6uUX74ZayrNmjNhtKNzzzBEWEtcYWgbBU7n4wcJQlITgddCwZ10y50vDW88zwSJgSfxpDAJwK97sahzK95U-3MTsp3O4uEI7fTky48sEX4KFTYJam1rJ9s66YIHcoKdjRxrpuikhZq29-yKug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=DhkFCvfD7h0I07Tfa5vi4kut-KwA-1OpL9L1d5fA9ApfPKzaug_8qDOFa8Vy1QYTOmYNKex7EBi_NCS-Sg9TKbboYK4P3ETORuMu7ZF0uClHcw9CzS6JJGaQGcNkEqZ-Q3lK9s84dFZbzNYsh7sg-mKjNUchG80mnUXm4cz1dHI7w50eGcmmHdMlansJb99MVo_dGiqiMWXmQm3iGPZUdkqVLWhcvI59YKiQeBG9pUY8CyQF0sa3tFYI2d2aXhzrXl8Psi7rJprJTAnIqDks_uuU3j1oio6gheOLLM0fqQbtzUFfUag9BVCegYzDM189RoJWJzX9L0MHLOeKujSBhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=DhkFCvfD7h0I07Tfa5vi4kut-KwA-1OpL9L1d5fA9ApfPKzaug_8qDOFa8Vy1QYTOmYNKex7EBi_NCS-Sg9TKbboYK4P3ETORuMu7ZF0uClHcw9CzS6JJGaQGcNkEqZ-Q3lK9s84dFZbzNYsh7sg-mKjNUchG80mnUXm4cz1dHI7w50eGcmmHdMlansJb99MVo_dGiqiMWXmQm3iGPZUdkqVLWhcvI59YKiQeBG9pUY8CyQF0sa3tFYI2d2aXhzrXl8Psi7rJprJTAnIqDks_uuU3j1oio6gheOLLM0fqQbtzUFfUag9BVCegYzDM189RoJWJzX9L0MHLOeKujSBhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-XoIS_pbsgGs6ASTn1IjBpe-KxjXseeODIGeeGb5JZZq2VhVSUGCC1W-ZwxgF2xeteVF3_5UKrynzbivP_GD_LwegVzNybNHhThKVhiIjlmjp5PXZ6NgV05Qf3Ca4c7kE6XXKpCWr4pOVfd2jQe_Ema63QYhK7HIgpnZ6nQbWuFF9jdbcnF_5x3FEHeJ5JGdXnY3w6jDiCkioViKjx6rQWOy87Z3ansifr1r9vSPjqXxNv69YTabikv9NFZ86vDB2-Qd3MJLl7_Kc5S5mMkEjzW9Ta7qm-OzYJx8cGNuhdy2J8K3T7rCJFrivhOmrFyy_lOaMNm_D67rC9mm5GXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=tVqfs_He1vDDAKNcAhsQ8pwkrfq8cwKy0hRlICj7OMvwtkLC7nTANpzeBY8b2mD9qzIbb4DyxNU6mQLGKbs2TX85lwLzymZcGT3-B7tg7lv_iLov60FZj6RTNuGcOfTprMCfnIZucg_tP9rL9jddV_cUDwfMujAgS_Hdlt4XEaZ_rk9pi4wDitxy_0_en5hDh2bxVRk5jI6VeskGMS0RyI6y2LcLLlQlJQtTQKT8l33Cn7XNPTxm-WOfdOCQ-hM9-yFVqaH3vjMKyafDJj7Si82AAQVt6D39lYWdtoF4jAksh4Y2OlhUIar4Ulj64b9bfnuaQG66xbvOF_tUP1Oajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=tVqfs_He1vDDAKNcAhsQ8pwkrfq8cwKy0hRlICj7OMvwtkLC7nTANpzeBY8b2mD9qzIbb4DyxNU6mQLGKbs2TX85lwLzymZcGT3-B7tg7lv_iLov60FZj6RTNuGcOfTprMCfnIZucg_tP9rL9jddV_cUDwfMujAgS_Hdlt4XEaZ_rk9pi4wDitxy_0_en5hDh2bxVRk5jI6VeskGMS0RyI6y2LcLLlQlJQtTQKT8l33Cn7XNPTxm-WOfdOCQ-hM9-yFVqaH3vjMKyafDJj7Si82AAQVt6D39lYWdtoF4jAksh4Y2OlhUIar4Ulj64b9bfnuaQG66xbvOF_tUP1Oajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=jJCxeXKMmx8J6ZDhIYkqD6-NEbRPnYv7j9luvQlIZg6KGCp8-sPBfS_wkuHMWtQy0DZDH3erUXfONhQAoLvyuELnrtBMm2x3UqUcwrv3HNS8JVwgFULW1fQAKp4gXcUIe36aKdHz4_35sx4gjkd8iQveKNflL2WZKaE3ERd3q4tI7dyoxrMTFTBA3CmoWhwhDQdBGh2QCmeg1NZOuj9ay__agmyy2rmu5JKtsVIJhf0jJ_1wz499k3Wr7wWHg7kHUTzqFKS-TlZQO9vXQGb-B0g2BzNnwnusAtSVWMtt3sqB1W9iraDw8NxJwBFtALbnsHndctJiE-P8zIp9BB1g8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=jJCxeXKMmx8J6ZDhIYkqD6-NEbRPnYv7j9luvQlIZg6KGCp8-sPBfS_wkuHMWtQy0DZDH3erUXfONhQAoLvyuELnrtBMm2x3UqUcwrv3HNS8JVwgFULW1fQAKp4gXcUIe36aKdHz4_35sx4gjkd8iQveKNflL2WZKaE3ERd3q4tI7dyoxrMTFTBA3CmoWhwhDQdBGh2QCmeg1NZOuj9ay__agmyy2rmu5JKtsVIJhf0jJ_1wz499k3Wr7wWHg7kHUTzqFKS-TlZQO9vXQGb-B0g2BzNnwnusAtSVWMtt3sqB1W9iraDw8NxJwBFtALbnsHndctJiE-P8zIp9BB1g8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=CuJFSEsJNVOgz1J3t23Nhn-oAF2b9T56_AgNhj8mj87jfPVGkmQ2T1kVUEIWV5EPQeCYe4gQPEufX6K7Ir8EWVYnM9sXwtOsBTYPLLhpQwhFxyn_1Gydg1SyQfw26Caogi8bxgIFHFakPaMhyXnipeTI-rehdFA8ZDv-q6WUE6MpX1tmwxHRMdq3cYfsim4upbnipwY8RCoDSmCZHIHFsq05npNotRn2q4cjQXhPdbXWsYLVIwLm7IhyuxwFjzXMq5f2RIKHyi9SDWOxugfnlpa0E4RYLuGttuXafXzjHHFQEylqdOY7w9wSWuODTiBOmajTvh-Ij2clyr1_8TKtiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=CuJFSEsJNVOgz1J3t23Nhn-oAF2b9T56_AgNhj8mj87jfPVGkmQ2T1kVUEIWV5EPQeCYe4gQPEufX6K7Ir8EWVYnM9sXwtOsBTYPLLhpQwhFxyn_1Gydg1SyQfw26Caogi8bxgIFHFakPaMhyXnipeTI-rehdFA8ZDv-q6WUE6MpX1tmwxHRMdq3cYfsim4upbnipwY8RCoDSmCZHIHFsq05npNotRn2q4cjQXhPdbXWsYLVIwLm7IhyuxwFjzXMq5f2RIKHyi9SDWOxugfnlpa0E4RYLuGttuXafXzjHHFQEylqdOY7w9wSWuODTiBOmajTvh-Ij2clyr1_8TKtiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=O9nwf-jx9pUAoUUD3_HK_A9LeOsRzD_xZOQGdfpaedtQ-FKoHl_t9wExkenKm677N9hipkGGCSDVUvv7r3U-nDIU9eS1t2LJ-xhEPexOtoFv5WQM0QOTtm4bMN2DH_H7WGyp9BsipQtdhfHWowK8SfcRhNqCZNGCJK065iYRWFK43acTlCnadzGvDO9bFIwEKjgf7Tiz9DyWd2WgZB8JjyxeqAO6l5bTGCe6vOHqRe052vM6-poF3NmtV_8Z4vXks1Uz18UMtRBP9nvmMYswCIYbIndh511FHlhfHPzk7xsoJRAby6C9GxRYu7gvJEVkZru2QVLvhEwjVb3JzRhqNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=O9nwf-jx9pUAoUUD3_HK_A9LeOsRzD_xZOQGdfpaedtQ-FKoHl_t9wExkenKm677N9hipkGGCSDVUvv7r3U-nDIU9eS1t2LJ-xhEPexOtoFv5WQM0QOTtm4bMN2DH_H7WGyp9BsipQtdhfHWowK8SfcRhNqCZNGCJK065iYRWFK43acTlCnadzGvDO9bFIwEKjgf7Tiz9DyWd2WgZB8JjyxeqAO6l5bTGCe6vOHqRe052vM6-poF3NmtV_8Z4vXks1Uz18UMtRBP9nvmMYswCIYbIndh511FHlhfHPzk7xsoJRAby6C9GxRYu7gvJEVkZru2QVLvhEwjVb3JzRhqNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=MBubMD4y1o9cKBGfxypH9uCSKC2vm-iglRDCzzCJCiUiW9XF_1q_NPYeeQNvI91JrPUDPtb-_PXn8Ffyd6DpIBTDIPFa8R-1YmiL9ntNchqakm8U_-fLNx2e-2gHPgiZrYvDjEbQ4o5PlPNb75Z1IZqfIZcjAjynKNXq7BHg13iuwtXc5o5CL2u1UafOVKkWM7hkFgV9mlEPxrE7IDRq6aH80SzOHG24ju6yYV0jMGCenyPCdGqrdep5zAx8FvwPN4Nk40Py355vOne0q8MbeQEe8BFRXlX2owHzOuHtFHCbo7Z-hgZknJxIKFw2-jOvKQy4Ge-dTJbrI3TInWO2pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=MBubMD4y1o9cKBGfxypH9uCSKC2vm-iglRDCzzCJCiUiW9XF_1q_NPYeeQNvI91JrPUDPtb-_PXn8Ffyd6DpIBTDIPFa8R-1YmiL9ntNchqakm8U_-fLNx2e-2gHPgiZrYvDjEbQ4o5PlPNb75Z1IZqfIZcjAjynKNXq7BHg13iuwtXc5o5CL2u1UafOVKkWM7hkFgV9mlEPxrE7IDRq6aH80SzOHG24ju6yYV0jMGCenyPCdGqrdep5zAx8FvwPN4Nk40Py355vOne0q8MbeQEe8BFRXlX2owHzOuHtFHCbo7Z-hgZknJxIKFw2-jOvKQy4Ge-dTJbrI3TInWO2pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_MFhm80QPe74Ra4rdrTy0MHSCy3_F-_OOj8biZYDkKpSlowhf0pV7OvPAR1s69TK08BT52MiG51bzmSHiMLsgXI_2eNljTocxFXTiBmS739ONnQ9_PEdiIFO4Se37MlRcjTJfsMD0TZ7mGMNMK7nyNAYaPsscN0PdgdG63nmdPcwbx-MwUmDWRv3M3-u2mdWE5dFeEkKplEtWLeQetVxMIp2ILvWfC3kj8RXeKBiIM2gQ2csQm0AwpwKHO9eghSxYIItOcum99Tn7LbHaFuHW-xmzdFtXerP7_wwlNuP8bdTq2LyM4RbiqsYdNsAZWgW04brQDE7tgKuC2FiTz2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwx3lHSe7p7f-uJ0hNyLt4GEn4ulSclrgYvb7IzBM05qZkqBNtrghMgC3eyhaay1jeiJZ6RSJxQvNAAj_QXCtSq8B16Ltr5eu3mnp72mB7TXkbvCuLlBWezrbgcbGMxRdelI_c0bmXKrLZpga5woCgtR4eIxhZyZOyDKjsjeBl4p8PJ0jAeIQHssvWdzxpQKUOUUPH52rQXJcdzoSX55eV5SCpFtZTG56cgJjbxWA48N74s4anl1N4hXLXae-fuVpxC9GsAfipJS3pQR0dqLZTgnbdqw8zAmhO11hvB4VzqPqomB0UZd8OYIi15JtjtRPfQ4fVFNsil5Bh_eRi5vKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajsKo82VE_IeocRsURqfG7mQqnW7whs5138TEoqFs48VHBkefvJ8Rgz8uWBoZmj3w5KIecI6K5Ddhr1E6N4vEnWrnPNrexj44ce05zSbkUyoPOaMFZmsEu4aKsmDEoqRYpTWcu7Bne6OFB8wAjgvqaC7NaUsXVFKS5BJwhOxyQOelhK6I1qWMl32ZetmTY3pyqPPQR9KmkpgDmIAJaZzKnlQtDB2H1vZPEG2WOiwS_PqLtXVfi9Fd9Fgxa0GHtW6xm2fJA9tnCapaeBDxmTAIpN0ywHfqqcXGk-hUMxTOs8uL_3eUvVezrJVYP_30tMS7H4C-QQkaRfe_9e4EzRTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGdwkydS-VIfrNw_LR6bd5azCQ-L9DUtH7xARCIfvs9glhKl9u-g6i04VLjLb5-SbxaSiRjpSdrrlefdeHq2IDFx2k0VHvAlwDaQfV8x6dWZYBj_jy90ckHabtStvZ2JOjDxgX4uyc8x3o-2NampZWPtsi2oc-wQGbdgUHIOKfAVfijMrwblXDlfBdPvck2ZODj9OtqhkdRieZWfHtXVJ9IYBsFaV1gDfW-5pfexAVwYRJ9UmdpnSHDb_R3DXMvq1jn_f5QB-Dzd4wO6QCNHcPdj8UU01giyg4i06AKwS3-sFMFH12go_CVjuXYriCdH6GGtL-X0qAh04qLc_FZ07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ck_kI87hNkfwam3NlxfemeJ_sgQDYZZffmTFokNIoDwFsWKY-i_OUEKMLijs5mtU1BySIZTeFXsi9Q1rW6vkvR0PpH0VGVfceEyn16rJ4mJKullYtSxk2r88I5a0xqwmiimox4eb3bWKe7CNGMizfBjDB8TlIHFJiOP93oWj9_oM4-BzOx5QALnTGcbTcJD-zukaJhhJjBeWaR5sa0e1_4CpSiJA64ubBH3tyDJ9OBpOiG51x-skdqrUgh1uK2_qoqAZUhGtmIWjZnWF6PJh6CPwVUvah5m1-8xVNT-UrGz6lI_Gx2JIeEHpGf9yz5Gevy1dUHNQyi66JuGe4MfoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLHyPUZmoHs4t1jbAGoqks848KE44DKYpquQg-QsZDF3Y0jyE06p7fBIYbHVNRXfDJbC9_WjuOu1a_7CC5I7tq-sAqYJ1SUTLjHjCGkQZgtpRyEMHw0C3VVfTJKA2GBiA70yhMPVkm_Re7NlzUJYFHReCYaTfn_HypAuz4Pa1jE8mdsS01r8EWzd6dMGQkCHhTWAstXSSdfUCQNHPc5xIw05C5sSpKNXPv7XckWsOaeMx9PWEvpAJylzv2sCNG6RWISlSEs_imr14L5y-QJuEasZJM4rZWUZiY7YOcctRupfbQ6yZ0Sf4GwPgQXVj69IhS3BZWRfrrQWlMg0LcBSl4Yo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLHyPUZmoHs4t1jbAGoqks848KE44DKYpquQg-QsZDF3Y0jyE06p7fBIYbHVNRXfDJbC9_WjuOu1a_7CC5I7tq-sAqYJ1SUTLjHjCGkQZgtpRyEMHw0C3VVfTJKA2GBiA70yhMPVkm_Re7NlzUJYFHReCYaTfn_HypAuz4Pa1jE8mdsS01r8EWzd6dMGQkCHhTWAstXSSdfUCQNHPc5xIw05C5sSpKNXPv7XckWsOaeMx9PWEvpAJylzv2sCNG6RWISlSEs_imr14L5y-QJuEasZJM4rZWUZiY7YOcctRupfbQ6yZ0Sf4GwPgQXVj69IhS3BZWRfrrQWlMg0LcBSl4Yo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=l1cNurC6Khxl8PCGstC5ILSltBkydLmFaT0oXqI-YdmDb1ojoCrMo76vmUtO1sFH02RzrZmt4mz-D6YZbWl2cfAuQXIiaUrTiGzKCss93nM3hIYFWkX9d2g1JevBl0R-o9YfqgG0lv0ko4qjCrNRiRnBR0zj--im8OpojtCScn8hFszGm5LVMwbjGGYV2KFiirzbu5DVwnP5ZnwphAVZB9IddCHJDkqSDHiaZqvCrx4cNuhZ6BD8JNilzb_HSVOIxllpLxiX38wLudLNUg6nXrcgganLCcDcGLxBXkTEmsFa9G020a4rqPa-om1blwTyu0JpuoTLAwXMtWCcIcCrwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=l1cNurC6Khxl8PCGstC5ILSltBkydLmFaT0oXqI-YdmDb1ojoCrMo76vmUtO1sFH02RzrZmt4mz-D6YZbWl2cfAuQXIiaUrTiGzKCss93nM3hIYFWkX9d2g1JevBl0R-o9YfqgG0lv0ko4qjCrNRiRnBR0zj--im8OpojtCScn8hFszGm5LVMwbjGGYV2KFiirzbu5DVwnP5ZnwphAVZB9IddCHJDkqSDHiaZqvCrx4cNuhZ6BD8JNilzb_HSVOIxllpLxiX38wLudLNUg6nXrcgganLCcDcGLxBXkTEmsFa9G020a4rqPa-om1blwTyu0JpuoTLAwXMtWCcIcCrwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=jRbAGbgUFjsgR47OxL2BiBtzIEpQIOnITyJfRO9bwAiuPKiIs2maUk-KKPnMlnI20kU2r2YKxXZvFQ1lpvvpjO3KidAdU-NJlRR3qSO3on2edstG6hyAPxUEdySVhd4B2UtMNrIgd-UbweeRPiU8MwcCFF62Xp5cPj0D_g7io7ocmckM-Fz2PqqH8m8u9ZoQ9cTN6_V2wJEroyaiNZcvAQ6OTwkfHr6MDTEm4tVdje4KLobpbprvK8XuC4-rgN4DvijD0nQifLq0Dp679qs5HExy6gbhwA_5zAQnj5-8tFkCMvz-_XK5solQoAa0QEaPD8UDGMh-SF-Aa2ZrPxsDcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=jRbAGbgUFjsgR47OxL2BiBtzIEpQIOnITyJfRO9bwAiuPKiIs2maUk-KKPnMlnI20kU2r2YKxXZvFQ1lpvvpjO3KidAdU-NJlRR3qSO3on2edstG6hyAPxUEdySVhd4B2UtMNrIgd-UbweeRPiU8MwcCFF62Xp5cPj0D_g7io7ocmckM-Fz2PqqH8m8u9ZoQ9cTN6_V2wJEroyaiNZcvAQ6OTwkfHr6MDTEm4tVdje4KLobpbprvK8XuC4-rgN4DvijD0nQifLq0Dp679qs5HExy6gbhwA_5zAQnj5-8tFkCMvz-_XK5solQoAa0QEaPD8UDGMh-SF-Aa2ZrPxsDcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=Skgg0bPe-5OMnqTqJDhK3t6VPNAvvAaU6uCF343GTLsEeQczXZ4h9Xq-IjFRMNiIfEADlQDWs4I6ncsv3euXOW2fjXGwUuU2G57Z59RE7u5eCK4Ug3iF97KVr3ewYQ47VftgZC8KqHBnYtNjgspWfP4r4ziIYgygY6hVUhFpPbZkrkLqK4xqANZN0-sM9uIJalOPOMsngqgkq46sH7IPwfcEF0D4ajwNC-6eGyzoMG1Or-0N-NDF65cC2QjBOSxppTr1MDPHGySexpOzYDxyggCIJYRvbaYAHDNMnjqDYe5que_J7Gw3VhagIR8Hu27gKBI-UMhppjEqdkolUHZVAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=Skgg0bPe-5OMnqTqJDhK3t6VPNAvvAaU6uCF343GTLsEeQczXZ4h9Xq-IjFRMNiIfEADlQDWs4I6ncsv3euXOW2fjXGwUuU2G57Z59RE7u5eCK4Ug3iF97KVr3ewYQ47VftgZC8KqHBnYtNjgspWfP4r4ziIYgygY6hVUhFpPbZkrkLqK4xqANZN0-sM9uIJalOPOMsngqgkq46sH7IPwfcEF0D4ajwNC-6eGyzoMG1Or-0N-NDF65cC2QjBOSxppTr1MDPHGySexpOzYDxyggCIJYRvbaYAHDNMnjqDYe5que_J7Gw3VhagIR8Hu27gKBI-UMhppjEqdkolUHZVAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKM8w9D8sayYpqo0ZJlhMgSy6AfGWj25PtfUyFIUzAbtdbUMyQGM-HpUEDUNOX6Shgk2Fxmrw61RGakG95Adx_HhPEpUTbkV-Gg51VLwB175qk1UUATcPPsLkod3e-z_R_1fqyY5YM_8dq4dwFPJXZQw6TZ5nhwmKuo22UQTkzA7-O0_NVlwbH2MHsweSOrpGnm88YVSCazZye8GHnqbPjmsQZI57mXq-waCW7RDkQwEFi4h4ppZv6XZyHGVS8HiwkpMApUa7gvwuMuaBi-uvNZkjcK6R3p5lupW-DlVMZiGLU1vmT00V3fpZ_g8k-6DzguMgoMEvtcJinNh108nWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=QGvu396nunAl7kIjoAPlazUIWtqIUP0GV08VsTVUZflFAC1tkJh_5AYXs_Is8BQmZySus-2SmK5HfIAVNMOK8EMtuKWqAJSQJ1WWOZ7kELS5K_owaRz4upK_q1f7RlR6740u3QSInub4Yoq9SIPSCo5z2_WZhZNE4qxZQS5A7FG5O-gctTNgZXXEZw6g8ONp6jp8tR4P_EwfthJGhPkEUgZHPJ8ffnQQ8Yjda3bRvDAKX5zcqQmie8uGYmEHltyBllLLcpXFIgy4GKHbfhiF47iyvQbdnR7gT_cp_CAulTW8nJWe5Xx7z6cufDYfM8-w2GrR16MZFF_XvuX8j_XJFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=QGvu396nunAl7kIjoAPlazUIWtqIUP0GV08VsTVUZflFAC1tkJh_5AYXs_Is8BQmZySus-2SmK5HfIAVNMOK8EMtuKWqAJSQJ1WWOZ7kELS5K_owaRz4upK_q1f7RlR6740u3QSInub4Yoq9SIPSCo5z2_WZhZNE4qxZQS5A7FG5O-gctTNgZXXEZw6g8ONp6jp8tR4P_EwfthJGhPkEUgZHPJ8ffnQQ8Yjda3bRvDAKX5zcqQmie8uGYmEHltyBllLLcpXFIgy4GKHbfhiF47iyvQbdnR7gT_cp_CAulTW8nJWe5Xx7z6cufDYfM8-w2GrR16MZFF_XvuX8j_XJFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=HgOKpptSMQ_wsPSyuQTStjet3JHHvEpJQUyQh53a4EmnCF4Thck4MlwaPhyZMm0TqdA-6QAZMrFb46Ix64LEKq52qfs91Vxz2Ni5QbQ8gbxhr1QwGC5B-l04snltrYvu8IOgCC3nCv7BOeFocE1GgNulfRWUlnYz6a3IPmucYq6vg7DfoNrY55Bi09k86q8M8GaIhwbpzhLxx2QE-5Qx8fuUcAtuMMc5nzyxkGMIB4edI7hIJh_-Ge9U3SubeeqeY4iihB1KyNdzMOUB0MoS_Ax0ONjcaLnGFSAoV-BLGdW4N2g7BQGCr3hKHF1snenlBwdkJssKt4vM71d_O32KZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=HgOKpptSMQ_wsPSyuQTStjet3JHHvEpJQUyQh53a4EmnCF4Thck4MlwaPhyZMm0TqdA-6QAZMrFb46Ix64LEKq52qfs91Vxz2Ni5QbQ8gbxhr1QwGC5B-l04snltrYvu8IOgCC3nCv7BOeFocE1GgNulfRWUlnYz6a3IPmucYq6vg7DfoNrY55Bi09k86q8M8GaIhwbpzhLxx2QE-5Qx8fuUcAtuMMc5nzyxkGMIB4edI7hIJh_-Ge9U3SubeeqeY4iihB1KyNdzMOUB0MoS_Ax0ONjcaLnGFSAoV-BLGdW4N2g7BQGCr3hKHF1snenlBwdkJssKt4vM71d_O32KZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=E5VO5wxpLlML-0M-LlODgry0fPjwWtKHr5qft0TZHOcNDxA-2shy4hiYK7YJay20uge4nHRJDoMZAjMReE1QbnAZEK63bzKCXL841VA4niBgemcf8J7ux5FafArWgS1otPB1StI_nbSS7b70h4qNlz3_BNY2y1D31mI0GI-gdpTonPXwsluGKASdOopMbFn6AFsz3PAcK9CbcQvlIDYksiGYLu-jBScGK5O5wEZZlbyOu2uk8w0x_FVh__2INl_2EkvZzRSDk1KCFR2H4ubNSffTXp_k73wuz7FLml-gapE06yweNMGRsuwNVmnTF-TkshAPzRzoEDvU5IfC5Cs3Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=E5VO5wxpLlML-0M-LlODgry0fPjwWtKHr5qft0TZHOcNDxA-2shy4hiYK7YJay20uge4nHRJDoMZAjMReE1QbnAZEK63bzKCXL841VA4niBgemcf8J7ux5FafArWgS1otPB1StI_nbSS7b70h4qNlz3_BNY2y1D31mI0GI-gdpTonPXwsluGKASdOopMbFn6AFsz3PAcK9CbcQvlIDYksiGYLu-jBScGK5O5wEZZlbyOu2uk8w0x_FVh__2INl_2EkvZzRSDk1KCFR2H4ubNSffTXp_k73wuz7FLml-gapE06yweNMGRsuwNVmnTF-TkshAPzRzoEDvU5IfC5Cs3Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=owBINmeIGAi7unQ9XapsvnmOu7Ih5cQCg4UntnCBY0QelnJfhNlGqpYnbV14vsYTtg1ge3cjoDOhUfxKdAzR-2kgnJxWoWDwV9qVcpXoyYCs7cM69aZwjpwEjgIkcSV1_HSmxIbchGA75IDEv1LIzvPCfDKv5ESZ2aJTjVVfOhN1JXMsKFbE1wpQ4FKPK5NTCeMhfQ7_FJeYtaAKWxdzWcLQOx-8G0ojKRr59nsqckYogwXlL9nzxjZb-cnhk8R1zJRu1dBVFla_SzkFjU5SkQUa0-eR5z5sfmgRTAhvx1_trxgEUFwI6qe6o3Wz_6Hhn-S7PAQW4-AOeHpfUhC0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=owBINmeIGAi7unQ9XapsvnmOu7Ih5cQCg4UntnCBY0QelnJfhNlGqpYnbV14vsYTtg1ge3cjoDOhUfxKdAzR-2kgnJxWoWDwV9qVcpXoyYCs7cM69aZwjpwEjgIkcSV1_HSmxIbchGA75IDEv1LIzvPCfDKv5ESZ2aJTjVVfOhN1JXMsKFbE1wpQ4FKPK5NTCeMhfQ7_FJeYtaAKWxdzWcLQOx-8G0ojKRr59nsqckYogwXlL9nzxjZb-cnhk8R1zJRu1dBVFla_SzkFjU5SkQUa0-eR5z5sfmgRTAhvx1_trxgEUFwI6qe6o3Wz_6Hhn-S7PAQW4-AOeHpfUhC0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=tBmCRxOu1vLs4HGX1kdAJ__OlzGcZcKCXtM4HzUqFtxIe7BblBolLqrFATVVq3bJXNDovJoOkUVKuwuSCyeBxBGAmt3aoaHGwyEYs_EsKYb7xu6Lfc7MXO9UE-tmeRyUfspoPMuVFsW1D94H22Mlde2G4vKbh4ofQ9ItjT1In5xUeLYeWasPn-VjwKXHOyU1eAlCw6Dcn5wOYtiibpSf_CCwtlXkqPDcbOOWNIAlVnLM6Zbsi_xQSeZKFnjPq0cMX2C9Ublf7HilGPNCSlPtujuRRDQR8ryCH3Wmy-CsXQYXJUipBCVoMILYpcXjRdApOwDy8BNWW1fWK9tmLqeboQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=tBmCRxOu1vLs4HGX1kdAJ__OlzGcZcKCXtM4HzUqFtxIe7BblBolLqrFATVVq3bJXNDovJoOkUVKuwuSCyeBxBGAmt3aoaHGwyEYs_EsKYb7xu6Lfc7MXO9UE-tmeRyUfspoPMuVFsW1D94H22Mlde2G4vKbh4ofQ9ItjT1In5xUeLYeWasPn-VjwKXHOyU1eAlCw6Dcn5wOYtiibpSf_CCwtlXkqPDcbOOWNIAlVnLM6Zbsi_xQSeZKFnjPq0cMX2C9Ublf7HilGPNCSlPtujuRRDQR8ryCH3Wmy-CsXQYXJUipBCVoMILYpcXjRdApOwDy8BNWW1fWK9tmLqeboQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=cpgWgLwOItHtT_SRtxv7TGsMqxUbSkpXcgI7WobMfL4eXPfiRWgSN8Kdp4gikAnfABQwj21swaEYt5MID2Dn5PfLvKLZRQIHhcLIRU9XG0GG0U_80vRfv-yCb65_iTFOXOomuwtOslt7n3J7tfijujW0f2UT1Ayh9F9GS44V_SU-ufao0B8ePq0BjlFx_EWzJQvRyaG1iaPAOOsuEwBBt1XQM-IkRRuZt82D96H7b69me6ho6GdSkK_eeDOmy3Ff_cEUB9AqziJzbl7Qi1sfhTOy0qjm8i7sTIfT22qrLqFMfSHHO-ixtCpq2vJmCmHcs3jo92ehNeGj8MEA9oo6wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=cpgWgLwOItHtT_SRtxv7TGsMqxUbSkpXcgI7WobMfL4eXPfiRWgSN8Kdp4gikAnfABQwj21swaEYt5MID2Dn5PfLvKLZRQIHhcLIRU9XG0GG0U_80vRfv-yCb65_iTFOXOomuwtOslt7n3J7tfijujW0f2UT1Ayh9F9GS44V_SU-ufao0B8ePq0BjlFx_EWzJQvRyaG1iaPAOOsuEwBBt1XQM-IkRRuZt82D96H7b69me6ho6GdSkK_eeDOmy3Ff_cEUB9AqziJzbl7Qi1sfhTOy0qjm8i7sTIfT22qrLqFMfSHHO-ixtCpq2vJmCmHcs3jo92ehNeGj8MEA9oo6wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=TiS-OZwx5lCuFrEg543bXhVAuy12uQo-TGLVTm_i1lbtvMu1r592jv8sT2xQe5nrfB_OlVhUltshfy_1o-rwbOV9ktpgNXPr-nGpznIJX_BUd4tJUZsMf63QAEmTPRjnBQPgrju-j1r0-u5roP4yAn141MWbGNil6ir_i77qnG15zW-yBd5H7yxaHmi89oV5r9DqXnFdk21xBPraTHa9QMWqM7ComxIROTgwZ3maeL9V36i-l2CQmp4If_77xjEC8ZMCkShCbC4v2ONFgSPlY3GG4NrJMoHoI5l2CEgSOcP0JC1L630ehuBa60cG2U-jEkDmr93qSGJAD3EM_6YdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=TiS-OZwx5lCuFrEg543bXhVAuy12uQo-TGLVTm_i1lbtvMu1r592jv8sT2xQe5nrfB_OlVhUltshfy_1o-rwbOV9ktpgNXPr-nGpznIJX_BUd4tJUZsMf63QAEmTPRjnBQPgrju-j1r0-u5roP4yAn141MWbGNil6ir_i77qnG15zW-yBd5H7yxaHmi89oV5r9DqXnFdk21xBPraTHa9QMWqM7ComxIROTgwZ3maeL9V36i-l2CQmp4If_77xjEC8ZMCkShCbC4v2ONFgSPlY3GG4NrJMoHoI5l2CEgSOcP0JC1L630ehuBa60cG2U-jEkDmr93qSGJAD3EM_6YdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=lyQfE1lZqoHO672PabLyuiLwdzOG0p5iA5EfrTU_6vmx0xwgVi8QPp6H2TY4yYmP4F_7Yz-IcbD0ld73FpR_Fb2QVUcuoQ2dCx7GX-h-S64I8RBJglQHvzw8ONQaKc903TsEoRmpIzLounSlt55Oj9GdsoHxfVp4mdITp28Ni41QpA1_qn4CFW6ti5TfupsuqMhT6bElwUfeGTsbLhBnTyNp_cYl-dvr5y6lf5p83agGgGn-Y5aZc5Z1LTCxo_gv1XxqjV1gp8k9165ST9WE8kcpdgQ_e4LYkfAFFqVHQ1vOPYK5Xt4hdqFVSO8vCoGZYH2sWNyFZs_6EYkBGTCDJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=lyQfE1lZqoHO672PabLyuiLwdzOG0p5iA5EfrTU_6vmx0xwgVi8QPp6H2TY4yYmP4F_7Yz-IcbD0ld73FpR_Fb2QVUcuoQ2dCx7GX-h-S64I8RBJglQHvzw8ONQaKc903TsEoRmpIzLounSlt55Oj9GdsoHxfVp4mdITp28Ni41QpA1_qn4CFW6ti5TfupsuqMhT6bElwUfeGTsbLhBnTyNp_cYl-dvr5y6lf5p83agGgGn-Y5aZc5Z1LTCxo_gv1XxqjV1gp8k9165ST9WE8kcpdgQ_e4LYkfAFFqVHQ1vOPYK5Xt4hdqFVSO8vCoGZYH2sWNyFZs_6EYkBGTCDJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=TtU_uOyXLe7lXu6auctRMqZjrvgrMb-z9M-VqkvGhxGWDi1jiakRo--dLnxmuTcktwhJeNPHA7X6tZ44Fg4EF_8HUiXM0OzrTYju0MBkCypnNrI97EdCQVo2VUhksWqLIxakFTPtU05STBVC_pwFgIEXs1_KZT-TlnCsMeQQeFc2KBuNunLO9MUwFd6sLCPSOkJB1BB-bXlEm97-ZgYiGtFUA6bPDE-lBC-UVDrJ_NG8ZdrZky1LIgoHGpHVqdaAw0zHu9CzmTDJbR1bI4dDjVgAifseqBAfvgqxd7GlfZtPlHPAQYJUcq3iWecG905ALUwWnPLrvUiSHz3LSjdvCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=TtU_uOyXLe7lXu6auctRMqZjrvgrMb-z9M-VqkvGhxGWDi1jiakRo--dLnxmuTcktwhJeNPHA7X6tZ44Fg4EF_8HUiXM0OzrTYju0MBkCypnNrI97EdCQVo2VUhksWqLIxakFTPtU05STBVC_pwFgIEXs1_KZT-TlnCsMeQQeFc2KBuNunLO9MUwFd6sLCPSOkJB1BB-bXlEm97-ZgYiGtFUA6bPDE-lBC-UVDrJ_NG8ZdrZky1LIgoHGpHVqdaAw0zHu9CzmTDJbR1bI4dDjVgAifseqBAfvgqxd7GlfZtPlHPAQYJUcq3iWecG905ALUwWnPLrvUiSHz3LSjdvCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=ewkpz9Tfxe_AmyqEKLJQNmGAda4fIib0LKqMXa9S6fqTS4QL8TdeB3M9qhBVoiwPITlqH8w_oxtJTb0cn8GcqEfLCB7MurbT6XzbXM1CTjJzBCQoHXk_Gaf1aBLcMg3frf7nGuzBD2EBlJpRC4UEJC7LgT4-94_5j2N8Kghs1KdUFfUc9X088xkAJZXeI7QuWFxKDpLzpEk_kwGMcy78dIurp30tvUN4L32g3rD75UI8dj4oOIfWwhN0_Drq4mKtbsg4Uw54XIDpMckxR9TlYRCjxPRt5n6UJbLdkxNocRx4-ozXQoJlfuePoW_jdBndVEBrf9KR22TSsOJX7QKhiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=ewkpz9Tfxe_AmyqEKLJQNmGAda4fIib0LKqMXa9S6fqTS4QL8TdeB3M9qhBVoiwPITlqH8w_oxtJTb0cn8GcqEfLCB7MurbT6XzbXM1CTjJzBCQoHXk_Gaf1aBLcMg3frf7nGuzBD2EBlJpRC4UEJC7LgT4-94_5j2N8Kghs1KdUFfUc9X088xkAJZXeI7QuWFxKDpLzpEk_kwGMcy78dIurp30tvUN4L32g3rD75UI8dj4oOIfWwhN0_Drq4mKtbsg4Uw54XIDpMckxR9TlYRCjxPRt5n6UJbLdkxNocRx4-ozXQoJlfuePoW_jdBndVEBrf9KR22TSsOJX7QKhiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=H0qWvi2quDS1SEXGMjOpRlOICylnwIciRqgJxxSlGUNLRbP-UHERjIjjvhbHg4khfhk3swKNoyv3QvjvZ0RmwSo56uq7PoRU4Rww8GXtda0mAeOE-OzURaHY-kz6PlfXjkgzL3hLMWft0KaT5A2yg0hl3k-BTAt4x8Jy7bxrXAd7v1F5MzfRNr4ntJWo-vTr-kFw06yeWL9KPm88ZoK72LbexjZL4vjKMtsdhLM85lhXn5uVyo6TLQohzCnDwaOQ1D3gh3nAHqJDl7zdlcSwNlNiVib75Jiq0t05AZYhIzfEsLeOm7ZFRuxk-WKyy6mOVMqa-O4pQVLKFAxLPZr8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=H0qWvi2quDS1SEXGMjOpRlOICylnwIciRqgJxxSlGUNLRbP-UHERjIjjvhbHg4khfhk3swKNoyv3QvjvZ0RmwSo56uq7PoRU4Rww8GXtda0mAeOE-OzURaHY-kz6PlfXjkgzL3hLMWft0KaT5A2yg0hl3k-BTAt4x8Jy7bxrXAd7v1F5MzfRNr4ntJWo-vTr-kFw06yeWL9KPm88ZoK72LbexjZL4vjKMtsdhLM85lhXn5uVyo6TLQohzCnDwaOQ1D3gh3nAHqJDl7zdlcSwNlNiVib75Jiq0t05AZYhIzfEsLeOm7ZFRuxk-WKyy6mOVMqa-O4pQVLKFAxLPZr8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFESUGDUUnxSLvtXqp2vo5N8gKkIKjJSLLD1C1KuelPiM5HqQX-QgQIaZdTIp9JLNy_aITSHwBVkczDCbc6yUEJTmwdAGy9x9U9fDm9A5ISp_9qp4YciO3UaGA7wmOhHK-SNI11lFP4qzO2Kyl02drHZR7dgGPt0XUjLOuU4sEyMDrsrGPba3-PpEyL3v_G13JknhYzfQHZ02gOnom-myeFhgHF7hK7EAzO_O1_k2X1ymNA1f-vk71ZZw5_d0syOf7WIRQPx8RAElqmZv7w-bToemSMQYmn2jHLDGzudRd18lNy1slizTOLmQb-8wkEK_4NZXuujdxhfxVXxX62Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=WM89QLk2L7zS3QTECjxPfz-tKqHlMrW0LYnHvAl5w5BKDsFXc18Blz4y0-GT7KpgB9oqBcBPutiXC7WX7TBCBHlxKNuUTMIhnHcegsApjWub1vleNeuz1SrdIiExO_MnzOBYDRkt9wuJrNt36ZFsH8m45hxP8VQUHUBVvd4EnkZOARsN4Y1DlN7uNSwPh_SViyzao6QrKMqwJjIcMK0UCYIiRkFtr8LOFsWhamt1zfNl7NsCC9EUbpbGKcJfiQAV1fP1Q7f6No7Z1OJKMa_RgB45BtFoDRFgn57a3ZbkB1OiXDBK39tHZzZ05i0-rv-8PuZynyvfsGWbMilX1xQLhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=WM89QLk2L7zS3QTECjxPfz-tKqHlMrW0LYnHvAl5w5BKDsFXc18Blz4y0-GT7KpgB9oqBcBPutiXC7WX7TBCBHlxKNuUTMIhnHcegsApjWub1vleNeuz1SrdIiExO_MnzOBYDRkt9wuJrNt36ZFsH8m45hxP8VQUHUBVvd4EnkZOARsN4Y1DlN7uNSwPh_SViyzao6QrKMqwJjIcMK0UCYIiRkFtr8LOFsWhamt1zfNl7NsCC9EUbpbGKcJfiQAV1fP1Q7f6No7Z1OJKMa_RgB45BtFoDRFgn57a3ZbkB1OiXDBK39tHZzZ05i0-rv-8PuZynyvfsGWbMilX1xQLhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
روز اول جنگ آمریکا از طریق یک کشور اروپایی به ایران گفت مثل ونزوئلا تسلیم بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=GPDaZ9UzDIj3evBMlW7FZ0JlDYnJphW5VAjYOgzzrWFXRKE7QWysj_umfPaojvS4SJxlU4UHbzJ8MaKp9uv74g_qCB_DTqc-zYPjkwCXYzGYIIR-zp31jfnXL4h06mQLLeotmOGAvIXAqmdWAjy46fwzUX9nzTds-S1yfFaq00JVt4qUYxgnH-9jN8bXjooOB8bpaurfGMNpkcWvj722VZdLC2QMwHz_K817bqI1lHsi0C1gD9L1KGvAmW0kmu5bmgOX6-C_KUImo1mQBnGVCRCiNCltxEmaofq5slZ1vxFvOHYq_6Xs3iO5Bu-iJ58l8ke46KtvHwNw04ayFYNUnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=GPDaZ9UzDIj3evBMlW7FZ0JlDYnJphW5VAjYOgzzrWFXRKE7QWysj_umfPaojvS4SJxlU4UHbzJ8MaKp9uv74g_qCB_DTqc-zYPjkwCXYzGYIIR-zp31jfnXL4h06mQLLeotmOGAvIXAqmdWAjy46fwzUX9nzTds-S1yfFaq00JVt4qUYxgnH-9jN8bXjooOB8bpaurfGMNpkcWvj722VZdLC2QMwHz_K817bqI1lHsi0C1gD9L1KGvAmW0kmu5bmgOX6-C_KUImo1mQBnGVCRCiNCltxEmaofq5slZ1vxFvOHYq_6Xs3iO5Bu-iJ58l8ke46KtvHwNw04ayFYNUnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کاپیتان نفتکش وقتی میفهمه تنگه هرمز دوباره میخواد بسته شه:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f482273e.mp4?token=uTRHU4MHJw6zeddE4ekBHBfvoNl2ILYkhHTnMi1uSWc4oYhQr50duThzvHzYEIbtKJV6h5FCn0Zy2tA19GR4Af22EqYqMhPfku-kvi9PULa3W7eQz_C05sv9TkyzIjQ6iyvvZxtTdjoDaPs-wZNqy8VFg0IkKeF6JgLwdb52yVs_cVcbjajP6utNDNxZghhu09aK2SX-MWoQcRHT_NIL2GP9M6QHVmMufZieIZbtOEHLfV80yam-bGTPIoqTr-hc3l9Eo5GqNKT5KdD5PpoNsSAdgbDff4XCi8gfvF1qyo9N9kZNyEBL0tC9JvA8J9uJ-O7r2I0gylcvG5oMNpXH7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f482273e.mp4?token=uTRHU4MHJw6zeddE4ekBHBfvoNl2ILYkhHTnMi1uSWc4oYhQr50duThzvHzYEIbtKJV6h5FCn0Zy2tA19GR4Af22EqYqMhPfku-kvi9PULa3W7eQz_C05sv9TkyzIjQ6iyvvZxtTdjoDaPs-wZNqy8VFg0IkKeF6JgLwdb52yVs_cVcbjajP6utNDNxZghhu09aK2SX-MWoQcRHT_NIL2GP9M6QHVmMufZieIZbtOEHLfV80yam-bGTPIoqTr-hc3l9Eo5GqNKT5KdD5PpoNsSAdgbDff4XCi8gfvF1qyo9N9kZNyEBL0tC9JvA8J9uJ-O7r2I0gylcvG5oMNpXH7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
دلیل موفقیت رزمنده ها بخاطر پشتیبانی ما بود.
دولت بیست میلیون بشکه نفت رو داد به هوافضای سپاه تا بتونه خودشو تامین کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66668" target="_blank">📅 11:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66667">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3yLTfkVEkfsgClcFcOHKtPkegaRtYjSzQ1cmeNI4X9k4jxN1DGKwYllw4g-MgTCyXQo2PTDD-CsrcM7vSNsqa8Fjxn1IveWIE-3BkiTenEWYI69Qv-GczeE93i6jVL1jy3Vx1jmLpfyJmqPB7b2Iab-f7xP8gctUM442f3GfWxN2yeFy5BpyfKkylKVpCxiKtPxGxo5jIqOATBPvZxuQXiZgCbPQkaddSX7wpUoqj5skKf0hnXvb_uvAzNbkCW0XNnYGxkphyVBn_hA5SiFvN8TZ5ro719vNiUmQ4vm7ZbEHXIPq8fcPATIaKsV8Acea1QDEgOz97ZXho7r0ioUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372418cb00.mp4?token=Md1MctbBUN0DMliWGhnbh0AnNZhhEqkoycn6ndsRCRwvL7fGd9tkqxqMkb6wOJ3m0cYAl7IYnI_Aey5FWHfpzo6pIhyyGoOKJmdO6eUaeYKiAdoMh5R90ZcajHcMeeF_2mptx1XbwCqTy2IfdkhEjZUQyIrVlgdCQA4iCV-BlFEp6ppZ5j2a0M6kvg2XdTEBZRdKtaetZEhB6aYD_hUSn2VzYE2awmma8_5Z83HErXw3SmSDt8KODPIRqWrIzPyt989f2SEnhkmmTXSmCnoTs1YYZgIH1l29e0gBf8vDZ9XQz1CVSG26bndIaTnh075XjfZHrgIV90jgoy8-BfLGhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372418cb00.mp4?token=Md1MctbBUN0DMliWGhnbh0AnNZhhEqkoycn6ndsRCRwvL7fGd9tkqxqMkb6wOJ3m0cYAl7IYnI_Aey5FWHfpzo6pIhyyGoOKJmdO6eUaeYKiAdoMh5R90ZcajHcMeeF_2mptx1XbwCqTy2IfdkhEjZUQyIrVlgdCQA4iCV-BlFEp6ppZ5j2a0M6kvg2XdTEBZRdKtaetZEhB6aYD_hUSn2VzYE2awmma8_5Z83HErXw3SmSDt8KODPIRqWrIzPyt989f2SEnhkmmTXSmCnoTs1YYZgIH1l29e0gBf8vDZ9XQz1CVSG26bndIaTnh075XjfZHrgIV90jgoy8-BfLGhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسماعیل بقایی:
با حضور میانجیگران، سازوکاری برای تضمین و نظارت بر تداوم آتش‌بس در لبنان و در تمام جبهه‌ها پیش‌بینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri8GyW5ozSb5fO_cNAa1Rfsi8Na1sC-pTa4GxnveJ9WVxnogPFkmStPMsuKEPiLaLLzQO9WyGCU3H_70xDs7BJ5dCkH2UXrpBt20maz0MBzxXRsWEdGFyo1kWet7-F7grhA-MTQjfffqZ0vQKgdshEjADnTRSv4q792kzj9bDrzMAL229bm32TBuvErfPsnwibQlFwJ4rq9BmJCZaKySasBcaTDQCrp6Gg0vwSyqbYFoMflQtTe2e2HebciTW41XEHC2JrG6KmZT9FYsBuLIJnA7uOL_yTVgmHodvLxT3qrnH2Dx3DBqi0YG6q3AqoLlt3Vd74Dsgb5wDwHkQ9G7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMJreTqwh7jdU2AlLV66HpUovjeex-pilMPhzsMzSnHYDv12NO8o5A7xhe60PEWWQY2rhnQsNwftO_iq3UEXr1hk8nFBeVqmeXLlABrlAdQgA4SYjJ2r4P6un5cFjWl8j1nnRXuUhjnTlTR5R40N5sQf3q6lHDSNdSam9q0Scd90Bs7wNO16obW-k9soQC_NpkFXN0h4CJffs7gPRvQAG9J1YWE38umaClSlSpXqPOjCT420LmFUEqw4fn_Q6UhEXF1yqYna3kyoQHTYqWFOgATl3fBI3yUiQuWOmBY2CG-B5U4rLCjrM_llchiudX40qLBpqNCRR0P_q9EdwWYetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eVzJB_4kwBHNUOwQe5eVmJ9t-SzZa1yAHQXQniITsot8m98mNryDv9En7IwraJHygFtIdXbFlv3qV976mg1s-1XQuTwNcVnpj5QRg0jaUg4LvVBs7eposzQtqBbfN2MkEfVKp5CE7r2V0A5zRGRROySXnLy-votAFK-9ncsLR9UKI1KGmmRB9N5fzQTmbIFNkWgixUj74-ADIy4l8J3H_Ic6j77bxhwPRJTaxdDiRFnm8xJd3lVF8V-ellUUQhT8E98bXa4tv_4yjuahBnZkvG-AsRsca_vIOu5mZ-KK5qBXp3PPvSpyNfzUt_pMaRAmOt3d7xLz0SXKVDCapFJvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0pfqw94ob4zDsoCuveQx4-9Th5LOT0AEsl-RjIMdySyDfrYOM8qc-coOJv88mF8_x3Jpvk9ZXksZzuRYpyY1vqkM6Ywe9ETr88JM77hLAYGBMMF-oJ-scGwPq73rdzmYLp8OJRcIS0463ZSFfGHNWLuT7RO60oSZwaanvEEqe1ZuNFNUWLjYjeWe8m_wEuMTGdP1cplURsgpscLJXHyDw7wA4IRZYCeBninNFzlAZBnTenjJmM0mHg45KCTWjMPss457Zg8Mad0UkwKLkEMMQ93DPhkdqVXijbSqjyD3EB3SXAV3Q8bLCSagTRi2w41Yh4G9ojHQ5psvP4i9o_yLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUCKGn-3dqAKrw32VLfoNKF9sotXmGZ1NEntAHK0Q7Bo6gLozK7vqXAcM2FZyelarA4xqkuvIT-T77JH0rPQoUILDTLKsslZznYiCxBMGoYN9aLZxAsmEouivysZ6CZMjn6GwL8DFeJsKynbyoKgW6GU6yiIGgYNw5MZw7_cbsoxa1f7MxQPit5OBGg5etLynDwfg82x8RtF-Z6g9A-77FGiyj5jSW2Y6ibVX-PitTvoI010WCzm4woQYHWvQQrDnHtWNvKiXp_A5YCFu-8oSIckKSU-69vcMuJ6KZQW505fPcZtmM_dyy-9cj_y_3wPTfuRmDMyixeB97NEsh-U0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=H9PfgE_kXgGiMqH_l17s_-6CpNXjwev7PHB6UTcO5eAsz9n-AY3WFpEgGljGbB4op7LZP-l0hB-z2gGzylCYcQvazztcSPltvsvttNCkSdN3_qyiVxyUpK9cH-qS7X1GQfRkqz7BYVNlUAt6h7bWMiwXYap6dmjiwoz_oURIyVYHm2sbRZMcjqp1L1X4BI6_SVsI1ZKwKRIaBOlVFVcrMIR8cKDZPwUeFLwfBK3mwqDXeKFrFK5iE5vbGK422fc9I9Gq_S3atPFpiYZmGQfmdtYsIw3PXd-kn3DYaoLAF73XaSARkiTmPGsFVhw9qT5gt2JtgLeAMI28ktK5W6VKVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=H9PfgE_kXgGiMqH_l17s_-6CpNXjwev7PHB6UTcO5eAsz9n-AY3WFpEgGljGbB4op7LZP-l0hB-z2gGzylCYcQvazztcSPltvsvttNCkSdN3_qyiVxyUpK9cH-qS7X1GQfRkqz7BYVNlUAt6h7bWMiwXYap6dmjiwoz_oURIyVYHm2sbRZMcjqp1L1X4BI6_SVsI1ZKwKRIaBOlVFVcrMIR8cKDZPwUeFLwfBK3mwqDXeKFrFK5iE5vbGK422fc9I9Gq_S3atPFpiYZmGQfmdtYsIw3PXd-kn3DYaoLAF73XaSARkiTmPGsFVhw9qT5gt2JtgLeAMI28ktK5W6VKVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chPmE7W90TyyeCbASsTeMV7pehU4FQJO9yCtiog26O5xb7UWzuKz6hUmsEAxDaAPB13TJnbzys5pHMzj9WcvzSfJ_0dh3SgMJRAGw5k2g4RwQmxxXRvHEcjRH_A-nU3e8DsIagdtlB1XVZ-NrCy0w556-_iXTb58zW4mUfj5tioId0C4xpz8Fw4Q5fJ6UqxJoPLtIHW92uG0iSfCSE9QnNNO_NgGK8Duyj8fTVx76cNiYJXmdP19wSuEdEStjTjiMm5RzQXy6F-8_93_ls72cu-EeGb9FV6Lzep7SCxwOIVdhMcs91ajH2qXiSS55YxkCOcX_yHCPT7z266ir9lJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66651">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">طارمی گل زد #hjAly‌</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66651" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66648">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">طارمی گل زد
#hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66648" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66647">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">چقد خوشگل بازی می‌کنه بلژیک
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66647" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66646">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGBk2omfErEvwTX5HYIvvNRpfhxBFldo06F4G-7aSRKszNfcQYe-UHQBbO74mkeBgr0HtPMohLOPdkzM6TQz0yQiSzETr6pUQFutPwCj3qoHQ0S4I5VgpZylSTfO2gTvQReaqIiBPDnHL0lkQckEMdUve4BYFGc0XPHtW-dTITCOXneswyRtpy7ea0VBmgpFZIqyPhjq5WZgZ3UrvPyzU3B1ZrRHLznnFqhazeIhcB_VJdaYFalueHdD06DMq-Iop00YJ3EImG81klMqfhDDwUXbHWkYcNvUN3WCvW4EmKGKWPUNZF9bl_NIOHOoJ_VeDwfdrA07TtK5inSKbR4-LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از نکات فنی قلعه نویی به تیم
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66646" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66645">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=MnVCcaikMNnvDCGJobGXbKYz1m2lxPzfc3b2uDRUcOTnxODjb351QzaB25Dv6Pe066C8GsyxzwquyLPr1dOmxuiZF8Rc9JE8Kk705UN1cvMALA3IsWmiN-HWWLHrQaUQzWWpr1PWPeXZsuZ6Zcg6-FS2j6Qnsy8Wpo18U12ei4WWHovocjfIMUvVYFZfRS-mJtX_YI5a9Qa6zEwam5zUYFLvSr27IJINnpxP9xq7KI0OjVI6yooee32M8vqYwIBVr1XEAmbyU6JqBo9Ti2XmEqo_RRCxnBwghXzjAAOnzS-9htR6qN8w7JBFJpPkFOSje3tTpJlgiOc-gZ949E3fYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=MnVCcaikMNnvDCGJobGXbKYz1m2lxPzfc3b2uDRUcOTnxODjb351QzaB25Dv6Pe066C8GsyxzwquyLPr1dOmxuiZF8Rc9JE8Kk705UN1cvMALA3IsWmiN-HWWLHrQaUQzWWpr1PWPeXZsuZ6Zcg6-FS2j6Qnsy8Wpo18U12ei4WWHovocjfIMUvVYFZfRS-mJtX_YI5a9Qa6zEwam5zUYFLvSr27IJINnpxP9xq7KI0OjVI6yooee32M8vqYwIBVr1XEAmbyU6JqBo9Ti2XmEqo_RRCxnBwghXzjAAOnzS-9htR6qN8w7JBFJpPkFOSje3tTpJlgiOc-gZ949E3fYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
ایرانیان حاضر در استادیوم لس‌آنجلس
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66645" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66644">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
سال‌ها به ما می‌گفتند: «شما نمی‌توانید به خاک ایران حمله کنید.»
بله، شما می‌توانید عملیات موساد انجام دهید. ما تعداد زیادی از آنها را انجام دادیم. من به بسیاری از آنها مجوز دادم.
اما شما نمی‌توانید ارتش خود را به ایران بفرستید. ما این را تغییر دادیم.
ما خلبانان شجاع خود را بر فراز آسمان ایران فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66644" target="_blank">📅 22:17 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
