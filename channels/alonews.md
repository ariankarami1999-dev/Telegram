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
<img src="https://cdn4.telesco.pe/file/PgrcHjsDsPwoEtyTnsbNiYlZod5q46IfzaYKuA85kVY9z-Avmx7rg9aJll6Ls_Jxjsab2EeoNWnBrkFJTTMNp25tEe02z7OcQ3w2sNVdVosCkzBIAkp9Y6Lk1Sbpu8GWJ1G2prr-2QmwhCr139kvIPGV9fATSMNB5mZ90ccG5og415FZaMlSR7yFFhDO8UdezWpoZcRU11Da3sVxjs_P-unnE2KxdZNPANixbdC4Uvk9HKEM8KOz8DklwkeBbPaGeEK28whc0jrPEXZETw63eYhB6QywThkUKEYV7igWDZHyRNF1Py7OjSeKcMQKGe-cQMDl7NFgFzrGKhUB6FY37Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 931K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 01:23:25</div>
<hr>

<div class="tg-post" id="msg-131978">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نتانیاهو: اسرائیل هرقدر لازم باشه تو لبنان می‌مونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/131978" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131977">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de38c0981.mp4?token=TTAMbg1EADo0bSNx9R7n0uYAmPSmNTU_Ouyhk08ma0aNXtyvw2oAADlhsFk37g0W-NlNW9On6m4TsoMOSseQrXO8AcAW7i_gVTPd-W59_4HVn-f7mDbnm7mXuRAfgMlT7u9rRrjYWSNd-D-W6q8LV-sSVYIt9KZq2ppOjnfiZRyvW6_gzKoI2wq1n4vTyIiusq-CFSH_W7aHyzkvgqcO7KEMEpUUT-7FAzleUkQXgG3cxhPdE5HNvRdYELLDxl6bS6Ek0Cghj_6ilviA5RchbJa09aOwIr7QIHJcMw10Xhq5PLk1HHwRYMxKgaij-K2KV7Jc-6d-66wKAc2V2kVETw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de38c0981.mp4?token=TTAMbg1EADo0bSNx9R7n0uYAmPSmNTU_Ouyhk08ma0aNXtyvw2oAADlhsFk37g0W-NlNW9On6m4TsoMOSseQrXO8AcAW7i_gVTPd-W59_4HVn-f7mDbnm7mXuRAfgMlT7u9rRrjYWSNd-D-W6q8LV-sSVYIt9KZq2ppOjnfiZRyvW6_gzKoI2wq1n4vTyIiusq-CFSH_W7aHyzkvgqcO7KEMEpUUT-7FAzleUkQXgG3cxhPdE5HNvRdYELLDxl6bS6Ek0Cghj_6ilviA5RchbJa09aOwIr7QIHJcMw10Xhq5PLk1HHwRYMxKgaij-K2KV7Jc-6d-66wKAc2V2kVETw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بی اعتنایی عجیب پزشکیان به مسعود و میثم خامنه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/131977" target="_blank">📅 00:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131976">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سه غایب بزرگ مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/131976" target="_blank">📅 00:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131973">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4yb2qvYNceNwYTxj1liNh8lTWpkLkUwzHSA1Z3mqNKV8X78nKDDu5B1Otb4iPp_o_LF5sinHft3ozGMrs_jazSwnA9UVzG1FrDJEVHHkWsMnGiNaSR6vnjtmyGHlf7619nplnAMEzgE8jtv1gesAVnMBSN2aIMWkcT_ijP3weQ9meQli1upv3sdKeiIESAULSDW8s1lOj8pcBfi7hL85GD-nLqQ2Ux0736bFEMKGLTqtWrNu07WoaQeDcvWTzk4DEINqmzpT5ktRDqYjpLrgRx_kMCLPVbv6e99t8Stt5lVF6F2gjbkpLV1fwrhwWBnnQKZBP6OtmqPu1o6ryjZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOmk34ReR1lKN2iqwV13niUCkSxuoTksI7sxRoqr7KW81mN6jYoSI-B8u2A1_Ai-IwPyChRQdQ69XXLjJjYDn8j24zt0vUM3Yk96JsWv7T_cgjYPjhsilJWn3Ul9l8OhNr7Tg4K9Yw7-sjryIrA9-bua2gsE-vN5qYhPqynXkx42_uoXg-8uV5Dc34R70Hqn3xpZRdgVBdknujdB1U7d6FNci3_AJ4YmWuZyktlQU7z3syoCMm8zLu3c1U4dSVH2Ee8gh0yf_2WHVAS0xYILUn-G8HXXVxMdQwYHpkjjFFamPZitK88rw8JKOlph-C2fw04zyfNrQBucvwhqZb6IqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwKeBgDdjV7Fh7NCjwzge2F4eM24_BHGWce4gSbR_rMWt8LzOzpaNOCeXZN1aFTaZIsfIhjJrByx5qgVY3yS_5sl4AnqBITyeHUvczoZwF3gyrEPB1hDnLa8u4mnVZ5e0PatzmyngmVJRoKmq8MT3DYV9h6_VVP4sYBb7rOYbCTY7MpVs-hBVYrfPOmJn2johAhwf144mM1XErprBwr4hT9RmUkYKL6FibKbm6Tx73ZL3ANNtmWyr2eYLgXqamq07VyZ2V6BP5w_BvpWXFRok3TlKC5oSu230Zs-H2xyUmPqp75A4g86QwYJ5HjvmWPv8RnPbZi1-oFENDID7jC2MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سه غایب بزرگ مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/131973" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131972">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b55821e32c.mp4?token=I6wtDB8BCgwj0HUJE7qYja70DA_0E-gHqe25NNCj3UNi3vk3Aoes5O92e_M8eavL9wtR4bWHeS_R4kHq2D-AHnbHVYAS-sAKNHn1y7HzRYaRwZu4Tk1RJ24A32or04nGRJV462uXjCyV6Y0Ioig6oRzk0SDXaqla_tiiJv2YWlddC-x-aEi6LDUw1ZtdLg4Y0AcEzVqG_RkhqcCPnnjyE0ODoSMly0kWyeobRLRHh8BIHHOWLQbJl9yj2RCMzKH_OzGTxo8opZVOPcraDPisxFdyeS51Vey6-fyK9hFref1zQzO053J3aRMePkjuW_MSDz9Jdf7W4XXDZt6K7NNrUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b55821e32c.mp4?token=I6wtDB8BCgwj0HUJE7qYja70DA_0E-gHqe25NNCj3UNi3vk3Aoes5O92e_M8eavL9wtR4bWHeS_R4kHq2D-AHnbHVYAS-sAKNHn1y7HzRYaRwZu4Tk1RJ24A32or04nGRJV462uXjCyV6Y0Ioig6oRzk0SDXaqla_tiiJv2YWlddC-x-aEi6LDUw1ZtdLg4Y0AcEzVqG_RkhqcCPnnjyE0ODoSMly0kWyeobRLRHh8BIHHOWLQbJl9yj2RCMzKH_OzGTxo8opZVOPcraDPisxFdyeS51Vey6-fyK9hFref1zQzO053J3aRMePkjuW_MSDz9Jdf7W4XXDZt6K7NNrUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسئولان برگزاری مراسم حتی به آیت الله حسن خمینی هم تیکه انداختن و هنگامی که با برادران و فرزندانشون اومدن ادای احترام کنن آیه زیر خوانده شد
مؤمنان خونه‌نشین که بدون هیچ دلیل و بیماری‌ای جهاد نمیکنن، با مجاهدانی که با جان و مال خودشون تو راه خدا تلاش می‌کنن مساوی نیستن و گروه دوم نسبت به گروه اول برتری دارن.
🔴
حسن خمینی هم همون اول گذاشت رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/131972" target="_blank">📅 00:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131971">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e716df92f8.mp4?token=e-OuIkDWvC16QfW8C49DprdiZyy-KApNXAfIYy2MG_h0QUu86_wmd7mFo6dTbn9dIFhXB-sZQ28-MkZ1ufKdx-Ei2GFcojZrCmeHopZjnxB6KD6zOFh98o_K0SC2yteUvFb0KEG0kQNAKe8g0GgXFpqhE5ur6HCXm9U5K9fIpwFY4IC4fYgjWDDiAswVCMjQrUVieZ9B9pdb4SLV84nhhv8S_hOC06g5ZnQthrEpcM6ALJRXJizkqKGA4MPFjGTcuAwpVRLLbLrxkbEAeDRKV9Ztwr8D_4GJbEHDwp3GSnUlUG1276H7xlIajt8YG3q6AML_as0sq0gJ0CRsgMrw5r_arhWSo8w-XdQrHtxypOFe6loJ2Al5EcAaaC4nu1Z_Y-kFWI_I-7BtOv7tbbi1Lvtp5AOp5STM8H_A_i7h3h_LUT2G1X3zBMat9iucG_nesxY7BPI2iMffyYzg77lFsbfOIwpHbWM04YUoWBSqi0Ht_TECNjbHCzbBxUsgKjv0W_--nh1BmPQp60S90keWk_xthZFf5lEGPDe2m3mtWEhD2eJCtl03DgPTAPgfWOGeUjjlREhWfQi3gSOK8Op6OA4Wj3lfIpS02pRsuX5QY-YKqRznD7HPXvO5tUY2qlIgpvbBTkZ7HklJLPfAzOYhgJhkMOwHOXqzVI_1wHiMIfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e716df92f8.mp4?token=e-OuIkDWvC16QfW8C49DprdiZyy-KApNXAfIYy2MG_h0QUu86_wmd7mFo6dTbn9dIFhXB-sZQ28-MkZ1ufKdx-Ei2GFcojZrCmeHopZjnxB6KD6zOFh98o_K0SC2yteUvFb0KEG0kQNAKe8g0GgXFpqhE5ur6HCXm9U5K9fIpwFY4IC4fYgjWDDiAswVCMjQrUVieZ9B9pdb4SLV84nhhv8S_hOC06g5ZnQthrEpcM6ALJRXJizkqKGA4MPFjGTcuAwpVRLLbLrxkbEAeDRKV9Ztwr8D_4GJbEHDwp3GSnUlUG1276H7xlIajt8YG3q6AML_as0sq0gJ0CRsgMrw5r_arhWSo8w-XdQrHtxypOFe6loJ2Al5EcAaaC4nu1Z_Y-kFWI_I-7BtOv7tbbi1Lvtp5AOp5STM8H_A_i7h3h_LUT2G1X3zBMat9iucG_nesxY7BPI2iMffyYzg77lFsbfOIwpHbWM04YUoWBSqi0Ht_TECNjbHCzbBxUsgKjv0W_--nh1BmPQp60S90keWk_xthZFf5lEGPDe2m3mtWEhD2eJCtl03DgPTAPgfWOGeUjjlREhWfQi3gSOK8Op6OA4Wj3lfIpS02pRsuX5QY-YKqRznD7HPXvO5tUY2qlIgpvbBTkZ7HklJLPfAzOYhgJhkMOwHOXqzVI_1wHiMIfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عربستان حسن نیت نشان داد اما جمهوری اسلامی بازهم نیش زد!
🔴
هنگام ورود هیئت عربستانی و ادای احترام، آیه مخصوص منافقین خوانده شد و به عربستان متلک انداخته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/131971" target="_blank">📅 00:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131970">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dekQpxoJ1RyojUfcPPPBjYrz5I_gXbyywMQ52-u_lNbM6byRO-BycbpZnljemTG-sv08S-7-6njnVTEJn_M_-K8K1IzpZcIHmsBlEEr0oiie8L8YlUHf22x-r0djYvtH-Lsh7Ad4T7hcin-MWz93LIjdczkCc0Nm6PHIdFLbCjItazDtr_yIROzHQWwwqh6K-vx5P2RqxfAWQuuG1LbguV1Hif9aBDxpTnOPHVUSnjUCKhviZm3SANLsx9CbNupLaa-vQ67WJ078nqozjwQJ9-ys15o9msvVT41sKDbc7m2yyYgyKlsx9ZDzOK9_Czh8EWjDdWSWb54gChDxt3pwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی زرنج شهر افغانستان، یه کودک 8 ساله در حوزه علمیه مورد تجاوز گروهی معلمان دینی خودش قرار میگیره و متاسفانه جون خودشو از دست میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/131970" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131969">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/131969" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131968">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S41L3Jtvvd_h1U9UgVXnDtx9KmfRnUauzEvpQ8EszycaQVX5echn3BN_e_6YEWSU_uXaBPoKVjdEn_yTrfif0vcUoZZV2lGXszaGooJ1Jdg5iNLdkDpLlvOmv0OIko8an_-lkeeo4AKQOfjMC5pKqQ-ZVqh5zxZe33oZ1vp1vMxlLhuvn3KxyDZjeo1-KhFPsZZSIi_Tzo6EbtMPX6Er9JJDkdPQGLwP747QIPA8mt9DfqNdOWPWkln6GcS-PAe6Ew2vWwyexLC-6G209jP4zCKBS3IdmVVi7XvQRd4lXh5e3m9jYVAO0qLxgHD2uXZ8eb0uy9DSE8bm91KsW_-vwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین پهپادهایی را به کریمه و غرب روسیه پرتاب کرده است.
🔴
منابع نظارتی نشان می‌دهند که تاکنون تا ۳۱۰ پهپاد پرتاب شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/131968" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131967">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWr-Qxud94m22K_5XFbWbM0T9DfdzVK1SKASDv5UvO4CWX7vn_rOYGNdvPTBIKZ2fk6ax0r2ig6Dequ21RZhnSeWEL94IFB5JTBVjP3wONE9RiF-ByllrZ4ylVximkbx2ESVzSVKbDerRIJ6zRigj6HolqZBTfvalCQM-PbdrYxpZD29p4Ra06zUYRsy1svkes4qRn6i7W0FM9sEQnnp3I0e5eEAHoZvK5cohT8wfGQFRiVz6sUpeQeiZHbp_Oh6NMJJRjNGUsxCsC7TmdOj29USKEZGj0K2QThTm3aqq7fIEdOmGYbz0K2Oos8wm40Fa2eF2oh2rVa6x9irVQgEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال
:
تجمع ساعت ۷:۰۵ عصر شامل ۴۲۲,۰۰۰ نفر بود! همه مجبور به ترک محل شدند زیرا به دلیل آب‌وهوا، رویداد لغو شد و همه به دلیل رعد و برق رفته بودند.
🔴
وقتی شنیدم که لغو شده، بلافاصله آن تصمیم را تغییر دادم و مدتی صبر کردم تا مردم برگردند. باورنکردنی است که حداقل ۱۵۰,۰۰۰ نفر بازگشتند و این شبی حتی باشکوه‌تر از چیزی شد که به صورت عادی می‌توانست باشد! این نشان‌دهنده کار تحت فشار بود.
🔴
تبریک به سرویس مخفی و نیروهای قانون‌گذاری بابت توانایی بازگرداندن این‌همه نفر به داخل استادیوم به این سرعت!
🔴
این شبی شگفت‌انگیز بود که حتی باورنکردنی‌تر شد با این واقعیت که بلافاصله پس از پایان آتش‌بازی بزرگ، باران‌ها با تمام شدت شروع به باریدن کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/131967" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131966">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
استان خوزستان سه‌شنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/131966" target="_blank">📅 23:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131965">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51d88b2c6.mp4?token=YIll9yGFlASafE8lX638WBSlqGfN3PZdoBuyz656XLPHF_wHedKYwuipVv0cl1ilrtoMjVDXIhBXxqy5X_6t71VM78dFDrS8WDjD_-IKxnXUZEkwYZlIpZDwnOij6p5zASytDGrcjxXR9joQWiSz7We7tjN6wGvD1V4ZpcHyZ4hKNySJpzRyLPkN4yT6rm2bb8GKvdsewfNyn8pENVTf2E4ZJp1IaG0VuqppG50PV8mcgoTMU4LYI4Qzn_SlvzPrSz52f37KjwHAFyYdZaQy7WHFdkVuH0PICv5e9ZLsdt3zVBquZR_jtnCeOXnhbZVRzcO4VFp6LFm7tDrItif8HbAw_Tac6caWYhNx-OOuMqnaigvCZzS4zHY-g7cxM3Ux0yeBB9uBuUc0niev6QcXRxsbOGz_tJPrukwuSYhpgnRcXJMU4_KBrxsdG0Cyqw0s1smHmtk20_BUXE4X_vUr3N7gRyxGaTWUjC4E2V61Ts7WtQfzOzSCs99cG371pnBaIzEIcfoWlsH8bvAmcvuyatDB8tZhJjSCY9rfOipSmBBAdov_3S7q9E85ysAJ9B3aKeVfau2vHDk6eITXd3ZIi6xsZZahRXdmbayx0spC5N0yJ9giK1pBTVZ0JPOuoltSgLxbeA6XnSiXlHxAqyO5h4v2WxzeiHYbtHmu-jPi18s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51d88b2c6.mp4?token=YIll9yGFlASafE8lX638WBSlqGfN3PZdoBuyz656XLPHF_wHedKYwuipVv0cl1ilrtoMjVDXIhBXxqy5X_6t71VM78dFDrS8WDjD_-IKxnXUZEkwYZlIpZDwnOij6p5zASytDGrcjxXR9joQWiSz7We7tjN6wGvD1V4ZpcHyZ4hKNySJpzRyLPkN4yT6rm2bb8GKvdsewfNyn8pENVTf2E4ZJp1IaG0VuqppG50PV8mcgoTMU4LYI4Qzn_SlvzPrSz52f37KjwHAFyYdZaQy7WHFdkVuH0PICv5e9ZLsdt3zVBquZR_jtnCeOXnhbZVRzcO4VFp6LFm7tDrItif8HbAw_Tac6caWYhNx-OOuMqnaigvCZzS4zHY-g7cxM3Ux0yeBB9uBuUc0niev6QcXRxsbOGz_tJPrukwuSYhpgnRcXJMU4_KBrxsdG0Cyqw0s1smHmtk20_BUXE4X_vUr3N7gRyxGaTWUjC4E2V61Ts7WtQfzOzSCs99cG371pnBaIzEIcfoWlsH8bvAmcvuyatDB8tZhJjSCY9rfOipSmBBAdov_3S7q9E85ysAJ9B3aKeVfau2vHDk6eITXd3ZIi6xsZZahRXdmbayx0spC5N0yJ9giK1pBTVZ0JPOuoltSgLxbeA6XnSiXlHxAqyO5h4v2WxzeiHYbtHmu-jPi18s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما به خبرنگار نشریه تایمز: برو به مردم دنیا واقعیت ایران رو بگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/131965" target="_blank">📅 23:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131964">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWMbLnUjd3QVrBb2cWNRwqjHJokaOowg3yalHsEZCiGFRuZECRSIPcZmJUlwGrBfzKliX_AgxsUbgYgw3TRN3WnGSpA_JxpkxKezBVuWFTfexTb-8RiHG1GK9vZDLC72sQmljE-hc7mQmvMqM-QgIkezgDlKkmRLx8Q3ui-L6lUyvs_oH5_d6ZFBqPwqByx_1tVVzjif3DKrKzcXKyRw1iblI_4bfvVBwqG8PEWyl9Uz4PNN-7u6WaC-dW7fkJF80iG4euMx9kYd5Gbh3jPDb7d0kOe5llrXQK40ns_xiqpTQ1R6LxUuXH7Yo_Odd_rkcFEvaFlXajSlw0IbyB-QKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسوشیتدپرس: یک مجری (محمد رسولی) در مراسم تشییع رهبری ایران در برابر جمعیتی متشکل از صدها هزار نفر، خواستار کشتن ترامپ شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/131964" target="_blank">📅 23:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131963">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
صابرین نیوز: محمود احمدی‌نژاد، حسن روحانی، محمد خاتمی، محمدجواد ظریف و اسحاق جهانگیری در مراسم وداع رهبر  شرکت نکردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/131963" target="_blank">📅 23:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131962">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
زلنسکی: طبق اطلاعات به دست آمده، روسیه در حال آماده‌سازی یک حمله گسترده دیگر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/131962" target="_blank">📅 23:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131961">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
خبرگزاری رویترز می‌گوید احتمال زیادی وجود دارد صندوق ۳۰۰ میلیارد دلاری بازسازی ایران هرگز عملی نشود.
🔴
این گزارش می‌افزاید یکی از ارکان اصلی آتش‌بس ماه گذشته میان واشینگتن و تهران، ایجاد یک صندوق ۳۰۰ میلیارد دلاری بازسازی ایران بعد از جنگ بود.
🔴
رویترز به ذخایر ۲ تریلیون دلاری سازمان سرمایه‌گذاری ابوظبی و صندوق سرمایه‌گذاری عمومی عربستان سعودی به عنوان گزینه‌های محتمل تامین مالی صندوق بازسازی ایران اشاره کرده، اما می‌گوید با توجه به حملات گسترده جمهوری اسلامی به این کشورها طی ماه‌های گذشته بعید است آنها صرفاً به درخواست واشینگتن هزینه احیای اقتصاد جمهوری اسلامی را بپردازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/131961" target="_blank">📅 23:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131960">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: واشنگتن در حال آماده‌سازی ارائه درخواست‌های رسمی به اسرائیل است که شامل موارد زیر می‌شود:
🔴
کاهش تعداد ایستگاه‌های بازرسی نظامی در کرانه باختری.
🔴
انتقال وجوهی که به دولت فلسطین تعلق دارد.
🔴
اتخاذ تدابیر سخت‌گیرانه‌تر برای محدود کردن اقدامات خشونت‌آمیز و پاسخگو کردن مسئولان آن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/131960" target="_blank">📅 23:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131959">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c5bb8bd4.mp4?token=H-QNJ6hJEMn_eS-1KC1vIJtD9qEYX0EsH0sO6NhSDgQoqWA53R4PGEzXIRDfbmlmWdrcqyQZ4HSsRWJtD3pnspBwxieHE7Di0pQcFpZTebtAPGuyGg0J80Rt5xz-tz85pOr8t0mmE3foXmWu5Qk-L93-ztRO2yGGZooPmEX0nR9wRAf3OxINOMaDEaBuGRe59wsNGnFgSZyCmYg8pB9kASNX2w4IpeIMmdk-AU1H_PV7nkW0nelatV03zk9qclZu9j_ZxTfwgC4WgXNWDi2pMrvlJyQ6kq1zXLXU19R4YwxxcL6fBIRfu4Bp5wMQ-X5RkEbYoGFt5JIr1-i3UGqVfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c5bb8bd4.mp4?token=H-QNJ6hJEMn_eS-1KC1vIJtD9qEYX0EsH0sO6NhSDgQoqWA53R4PGEzXIRDfbmlmWdrcqyQZ4HSsRWJtD3pnspBwxieHE7Di0pQcFpZTebtAPGuyGg0J80Rt5xz-tz85pOr8t0mmE3foXmWu5Qk-L93-ztRO2yGGZooPmEX0nR9wRAf3OxINOMaDEaBuGRe59wsNGnFgSZyCmYg8pB9kASNX2w4IpeIMmdk-AU1H_PV7nkW0nelatV03zk9qclZu9j_ZxTfwgC4WgXNWDi2pMrvlJyQ6kq1zXLXU19R4YwxxcL6fBIRfu4Bp5wMQ-X5RkEbYoGFt5JIr1-i3UGqVfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف‌های چندین کیلومتری بنزین در روسیه در پی حملات اوکراین به زیرساخت های نفتی این کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131959" target="_blank">📅 22:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131958">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USpIYFrISmPBIGEwD2gWsEy59gt5oU89u87WdkzrWPwDDcAMB7W-K2KoabwvU5BgM2XXz-u0ZfK561xxv-NLqa2h6bD_wzDlZRhgHJKJK3WdKHvaMRJkVIBhCA8uuWUN8jIwN-usKAulsPjeGyn5P7Npb0014UWQtbxwJof4syrUvTkLJtgXd3GwRVLxBOxd1_2rz28bIdzFCK0InF2ZUVZ32hdiBj0_ATpiGtnq7D6RqJfAUYslTOFm4GRan3lRPUL5Ei2xyCWv3ejyTCffEzvmPhevLW0aG837gj6NM91a92z3cvYMX6XQ8GfHGN3kfnPMp_JLaydM1wrs-umIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تابلوهای جدید بزرگراه I-95 در جنوب فلوریدا اکنون مسافران را به سمت فرودگاه بین‌المللی رئیس‌جمهور دونالد جی. ترامپ هدایت می‌کنند، حتی پیش از تغییر نام رسمی فرودگاه بین‌المللی پالم بیچ که برای 9 ژوئیه برنامه‌ریزی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131958" target="_blank">📅 22:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131957">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBE3tXqA4COX_6NlrVxgnT0RIF6cISwUbRTKi-u6Bv1h41LnQaklLqmrjXPGiG2mqMTEAQOGdGeBTNdZBTHqmeL08ufvq4qS4fku344SBdfqiPyJTfZ0s0IdSvMAHx8_MsWmT092wfOlrAa8WkMD0ISMch8-T0Lm7vvMgAECjGS84_xS2KCcWv7Lg4p6HMQ_ZtBwdjca46w86WhzXz8QROOQBxQwq98So_frEInXjabb_NnpW7-kEuEAliuYddLq95qyhffzFSeFCS06rsFP5UXrBFmWPrtSfR5DIcMrKqDc1x48oyDjEDMvOb_9cvd-vzAneFHvM62e5uPzI1k7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
⛔️
تصویری لو رفته از همسر سپهر حیدری و ساسی مانکن در ویلای شخصی ساسی
‼️
⛔️
گفته میشه دلیل طلاق اسطوره پرسپولیس هم همین عکس بوده!
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131957" target="_blank">📅 22:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131956">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
شمار قربانیان دو زلزله مرگبار هفته گذشته در ونزوئلا، بر اساس آمار رسمی منتشرشده در روز شنبه، به حدود 3 هزار کشته رسید. هم‌زمان، با کاهش امیدها برای یافتن بازماندگان، تیم‌های بین‌المللی امداد و نجات عملیات جست‌وجو در زیر آوار را محدود کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131956" target="_blank">📅 22:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131955">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it22J6vOT0psEuI324PpdtrSy8xdR_m0af9dIaN-bw1XoLMNTR5BZNxXL8TYOSuOEsSi6okYtuWd9uYetjXm8FPPS8nuwZNPq-KDEQURQbUEicIGW5vviP1WsCRLWOl0AEuCNynveTEMo0tGGMOBD45iVihCTZxOA-P2iwh10g0lUriN_cDEjBdecvjseS-3sXqsUuFIccUZjYcE0DC0FCvLnW6AHiLfSJ_JdIO4Ow50K_zwPu78a6ylYjTWna_JsrGlk5hmx1cvjfG1V_CK3JBCF_Me_8NpbVgilWYkBJGcl6LLgznnMOz6YqnooAE4quqG6FHj8oMZWoTZDgJYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: هیچ کاری وجود ندارد که آمریکایی‌ها نتوانند انجام دهند به جز شناسنامه رای‌دهنده (شناسایی)، اثبات تابعیت یا، مهم‌تر از همه، لغو مانور پارلمانی (که دموکرات‌ها بلافاصله پس از به دست گرفتن قدرت انجام خواهند داد، و ۲ ایالت دیگر، ۴ سناتور دیگر، ۸ نماینده کنگره دیگر، حداقل ۲۰ رای الکترال اضافه خواهند کرد، و غیرممکن خواهد بود که یک جمهوری‌خواه هرگز دوباره به عنوان رئیس‌جمهور انتخاب شود. من نمی‌خواهم آخرین رئیس‌جمهور جمهوری‌خواه باشم!).
🔴
جمهوری‌خواهان، هوشمند شوید، اگر این کار را نکنید، مدت زیادی در قدرت نخواهید بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/131955" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131954">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سی‌ان‌ان: ایالات متحده انتظار دارد رهبران ناتو در اجلاس خود درباره امنیت تنگه هرمز گفت‌وگو کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131954" target="_blank">📅 22:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131953">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بر اساس گزارش ها ،در درگیری های اخیر یمن حدود 50 عضو از حوثی ها کشته شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131953" target="_blank">📅 22:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131952">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=NPSXEvLsx71fpecmAq7lV7AxIzuK0SvlJAgNjOsv_FDIfFy2cwVP489QblOwOi5zrNv9fAef_s1P9e1poT9JWA1WQyNLyc7BKimIKHeCprLwS1nS6u4RyxgdMyZ_vYpIxrDySQlDJC-X6e37phwuBq21u4V2lbstVJC_nJVwJXHcvQN-54FPrIU-JvQ0AxaSyeX7w_gY7wiQ7EuPyvCjQFU8pHfpciH1rGmvys5rpwfFaudQyBwkxvjnCYQTjngFxVflpfxnbMz2KUeNrtiE6NBdPiaixRYHsAfZYhWacXOgkQ0i1p9MnTJw5y4izUOsUSfKcAvG56OPRrvf9GGVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=NPSXEvLsx71fpecmAq7lV7AxIzuK0SvlJAgNjOsv_FDIfFy2cwVP489QblOwOi5zrNv9fAef_s1P9e1poT9JWA1WQyNLyc7BKimIKHeCprLwS1nS6u4RyxgdMyZ_vYpIxrDySQlDJC-X6e37phwuBq21u4V2lbstVJC_nJVwJXHcvQN-54FPrIU-JvQ0AxaSyeX7w_gY7wiQ7EuPyvCjQFU8pHfpciH1rGmvys5rpwfFaudQyBwkxvjnCYQTjngFxVflpfxnbMz2KUeNrtiE6NBdPiaixRYHsAfZYhWacXOgkQ0i1p9MnTJw5y4izUOsUSfKcAvG56OPRrvf9GGVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131952" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131951">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بانک مرکزی: سامانه‌های سحاب، پل و پایا جهت انتقال وجه روز دوشنبه فعال هستند
🔴
با توجه به تعطیلی رسمی فردا، سامانه‌های ساتنا و چکاوک روز دوشنبه ۱۵ تیر در دسترس نخواهند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131951" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131950">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دلار در تهران به 177هزار تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131950" target="_blank">📅 21:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131949">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl3Kw0IUrRBDHPs9X2U6rrh7sN9pH6I4Q4ITULOssZzJF3Brzm4r8q_o8h-OZUIRnlLdeAjJUemSL2j0bsbxFffVrgAxoIGk_nZjoEx1HbnHfaXvycMhDwNC-YVKKSkQwonjB0sVVmvi2SS1CUUOGKipapcrqvaKKHDNjv8OkFg1VvSYtqWmWt9GGMyHtdyzr8iQznRLi4MZJKEsbr4R3gww2qZU0M12LJJfEVC9IpQkZ5kojG3TjyY4GkVleA-U7HsB61sTeIeTJQl6e1bN6GrlkH4gWPfmifcR8911MrNnRPCsbpTM9foUdO6xjrjNbD92L530O5i38sl0UrEtJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه امیدِ صداوسیما:
برید تو بازی ماینکرفت، انتقامِ رهبر شهیدمون رو از آمریکا و اسرائیلِ جنایتکار بگيريد و فیلمش رو واسمون بفرستيد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131949" target="_blank">📅 21:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131948">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نتانیاهو: فکر نمی‌کنم میان من و ترامپ شکافی وجود داشته باشد
🔴
در ۹۹ درصد موارد، من و رئیس‌جمهور آمریکا کاملاً هم‌نظر هستیم، اما مانند هر رابطه‌ای گاهی اختلاف نظر هم وجود دارد
🔴
کسانی که از اسرائیل نفرت دارند، در نهایت به آمریکا هم نفرت پیدا می‌کنند؛ وقتی تظاهرات می‌کنند، پرچم اسرائیل را آتش می‌زنند و خیلی وقت‌ها درست کنار آن، پرچم آمریکا را هم آتش می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131948" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131947">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ: از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/131947" target="_blank">📅 21:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131946">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ادعای شبکه عبری کان: در روزهای اخیر، گفت‌وگویی میان ارتش اسرائیل و ارتش لبنان با میانجی‌گری آمریکا آغاز شده تا معیار روشنی برای مفهومِ “منطقه عاری از حزب‌الله” تعیین شود.
🔴
تنها پس از آن، ارتش اسرائیل مطابق یک طرح آزمایشی و بر اساس تفاهمات انجام‌شده در آمریکا، از مزرعة‌الغربیه و فرون عقب‌نشینی خواهد کرد.
🔴
همزمان، از سوی اسرائیل نام شماری از افسران لبنانی که با حزب‌الله همکاری می‌کنند، منتقل شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/131946" target="_blank">📅 21:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131945">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
الحدث: نتانیاهو در دیدار خود با ترامپ، تلاش خواهد کرد تا بر "توافق" بین واشنگتن و تهران تأثیر بگذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/131945" target="_blank">📅 21:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131944">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlJFwBx_it0o-uvwHKGJgEinKmrnrdKxr6TCEogf6N_t1xryJtpHSHkTEfVanVJyLFRMyKYkQJlQrmeNTE9U6VU-CB4od3khjpqw8CVm5Xeo743IvW-pdeYEzpWp3Z_0BfovlgdHoaBUqxXwHLWJ2k1Vq8LXZiIlUQOov6UVBAgOuutk53zym_gw-wR63P0uGF9h9BPxhErr7F3iPWTIFnN0pzOH0nqEhX6oiLn-nCDyiVrViz5YbjBFVtB1p9tqRyab2zS7bbuYZA0cNz7YR44Fy7ecD55MwC4N2p4HRxOqVZivR4wFHDd1jZqvxQ_460w3D3fKXTNbk46_h3MPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131944" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131943">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کاخ سفید : ترامپ قراره تو اجلاس ناتو با جولانی دیدار کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131943" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131942">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e189569c76.mp4?token=N7XnoM1V2oh_2w7d7RF3mZoYvTDu51asnbi1r8vFlajIhxejK3UsGXuKVllIG6B5hfDFB-8piloZkUOt3t33uds3RgIEoN7Dv6QiMKZj-mHL1q26k9VPVyK2vBQeo-sJqlNAAn6TAlzO6Y-PVs9IuOieHPdED3yKAifJ9RcDtoXIG2hP8OgcqyD9WnHVn4i-C0wny5bYOpZFa9x25A_p6p9qQ9W3SuxgJMt5Uc4R1pki3__SRCQBsu83s49UnIKrKE79N8px5t3cym1pYufSgDMM4Kit69a8u_3UOqJ6OmJRbwYqNlXPh7X4P5G4loaNcTRW1e1MVKVBcVdRhuDC5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e189569c76.mp4?token=N7XnoM1V2oh_2w7d7RF3mZoYvTDu51asnbi1r8vFlajIhxejK3UsGXuKVllIG6B5hfDFB-8piloZkUOt3t33uds3RgIEoN7Dv6QiMKZj-mHL1q26k9VPVyK2vBQeo-sJqlNAAn6TAlzO6Y-PVs9IuOieHPdED3yKAifJ9RcDtoXIG2hP8OgcqyD9WnHVn4i-C0wny5bYOpZFa9x25A_p6p9qQ9W3SuxgJMt5Uc4R1pki3__SRCQBsu83s49UnIKrKE79N8px5t3cym1pYufSgDMM4Kit69a8u_3UOqJ6OmJRbwYqNlXPh7X4P5G4loaNcTRW1e1MVKVBcVdRhuDC5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آزمایش موشک‌های ناوچه "جیانگ جیان" کره شمالی، دیروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/131942" target="_blank">📅 20:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131941">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
به گزارش فارن‌پالیسی، تهاجم اوکراین در کریمه به‌طور جدی توان روسیه برای اجرای عملیات نظامی در جبهه‌های جنوبی را تحت فشار قرار داده و می‌تواند دامنه محدودیت‌های عملیاتی مسکو در این منطقه را افزایش دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131941" target="_blank">📅 20:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131940">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نتانیاهو:برخی از شهرک های مسیحی در جنوب لبنان، درخواست الحاق دائمی به خاک اسرائیل را دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131940" target="_blank">📅 20:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131939">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eawW1Gv0_TuZbpY3qMcLAxE93IuA8vsPGvzy8LPyPWUgRzoz_ps6kSuqlbhlbKD5-49pNkehRjJJ8JV66r8d-iqslW6d1ubZ3ZQqkK8K5gJWY7SMl7RjbE0snsigAdkoNotnq4vhICw1oB7LUWMgiqNfEktKXhOMoDIGxKQOdFTIyhprOymqedg-s-vDeEcL7Sglo0pJETa3ur2GYU-OFlbtejdGLXpt4z8iuc6egYGZkUQvxxyNaWAWRUvWThWTXlwbr7A25UHAwZRWMElzatYFTGVjmuOttxeRqEyqej_uINGZ0cnisRI-9NWim-qTfUI-lRe-yGdiasiMZbdl4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری Uscirf عبری
:
امروز برامون ثابت شد که فردی به اسم ابراهیم ذوالفقاری وجود خارجی نداره و با هوش مصنوعی ساخته شده
🔴
چون حتی احمد وحیدی فرمانده سپاه هم توی مراسم حضور داشت ولی خبری از ابراهیم ذوالفقاری نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131939" target="_blank">📅 20:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131938">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
قالیباف در دیدار با هیئتی از حزب الله لبنان: صلح در لبنان جز از طریق ایران ممکن‌نیست
🔴
با آمادگی برای شهادت مذاکره می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131938" target="_blank">📅 20:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131937">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نتانیاهو: تا زمانی که من نخست وزیر هستم ایران به سلاح اتمی‌دست نخواهد یافت
🔴
نیروهای ما در لبنان باقی خواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131937" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131936">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
به گزارش اکونومیست، ترکیه و اسرائیل ممکن است پس از کنار رفتن بنیامین نتانیاهو و رجب طیب اردوغان از قدرت، زمینه‌ای برای کاهش تنش‌ها پیدا کنند؛ اما نگرانی‌های موجود در روابط دو طرف فراتر از رهبران فعلی ارزیابی می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131936" target="_blank">📅 19:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131935">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک منبع نظامی به فارس گفته خروج حداقل ۱۱ فروند هواپیمای سوخت‌رسان آمریکا از منطقه تأیید شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/131935" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131934">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98cede34f.mp4?token=pqappqsI_vXje1U3lxh0s_jiFLOPX02LOfVyrV8SAhzk7JCO4gF7x6zEK4jCubF-q39--O6pf7VFQWiImxmGWo1e40uyWPhDL9l9zrM36e8vX6Zt_HPQ7ogmEbR6P_c24F-MEE1tU-TybFo-FPoR_u4IYpnX_wmNUX8BEkxg91yv1GWkCvKIOTXzldzcFip3HwB7NFclWs6pil8PJ1Vf88BH-yJnJlnspvPtJoS4lgX6nnu2Aq9rLDUirEA6LvPEJCLC3BeeDoWbcEY3D2_pJlUG8w-vszBSvPOFddNbou4OVOVkIUHiotIhCGQ9nc9y0i1nQea-hKZzVLeaONrooQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98cede34f.mp4?token=pqappqsI_vXje1U3lxh0s_jiFLOPX02LOfVyrV8SAhzk7JCO4gF7x6zEK4jCubF-q39--O6pf7VFQWiImxmGWo1e40uyWPhDL9l9zrM36e8vX6Zt_HPQ7ogmEbR6P_c24F-MEE1tU-TybFo-FPoR_u4IYpnX_wmNUX8BEkxg91yv1GWkCvKIOTXzldzcFip3HwB7NFclWs6pil8PJ1Vf88BH-yJnJlnspvPtJoS4lgX6nnu2Aq9rLDUirEA6LvPEJCLC3BeeDoWbcEY3D2_pJlUG8w-vszBSvPOFddNbou4OVOVkIUHiotIhCGQ9nc9y0i1nQea-hKZzVLeaONrooQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عزیزی، رئیس کمسیون امنیت ملی و سیاست خارجی مجلس: دنیا باید بداند که ما انتقام رهبر شهید و فرماندهان و مردم شهیدمان را می گیریم؛ پیام مراسم مصلی تهران، پیام انتقام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131934" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131933">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28fcbb6feb.mp4?token=UnIoMGZLNnnTNQBRh6pAAHrJeF1-n0axP-z3UKwxzMVtF5KE-fcpka_4HHYWcFgaqDIYMALFdyHAH8eBwkysBtCojxXQys5yt92whoVHEGVFsuWBwh_lPy9iaijuplOdc8xrE2Ekvt-62OYIjj9b2u9_4-xoLVtAhOjVQYUf3v0eDdyz-cWAMyxs1qqrzyau3Bn2HH5aMOZUYvnaBQ5YuB1sUH4pr9crILFxODmKfQoD_L1YoUrw6H6jgcMGnXWtclT7f7zeEAKNDP3jM4ODZFgZM6GablaC1VwbM4eot9lKMAamjbwS-NaX3HrHHksbGHl_5y6CLN6MQQM7Yjkt1BQvIj7rkFn13hgCALncyljyCU1sVPXdxL6cf9yYKXD390G4HOBKZxNkHMVjnO6Hj-sd9djAjHO5LmWFJs0LIXz0-X01lSglhfeVnL2ZeDH7UlG5RrmV_T7qgtG3Zrmlll8RFxg2tTrHaLr4M0eyR1QeQJFVgeo8HMdtQuFios65HKy3oupKdYnu4SVGPfG0-rVGr6cuKkLfG8sL3ou9RAnlxqqUzYY24SvOLXrmgYzri8vJG2QHET5TU6yvgD4ADkAKmxT2sLMMg63ScaD8cdK-_x97jVgDrVuw77ZcMFNUyKrB_NNq8efjXpe60mR2kaldODpswHHhehjlqIcLhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28fcbb6feb.mp4?token=UnIoMGZLNnnTNQBRh6pAAHrJeF1-n0axP-z3UKwxzMVtF5KE-fcpka_4HHYWcFgaqDIYMALFdyHAH8eBwkysBtCojxXQys5yt92whoVHEGVFsuWBwh_lPy9iaijuplOdc8xrE2Ekvt-62OYIjj9b2u9_4-xoLVtAhOjVQYUf3v0eDdyz-cWAMyxs1qqrzyau3Bn2HH5aMOZUYvnaBQ5YuB1sUH4pr9crILFxODmKfQoD_L1YoUrw6H6jgcMGnXWtclT7f7zeEAKNDP3jM4ODZFgZM6GablaC1VwbM4eot9lKMAamjbwS-NaX3HrHHksbGHl_5y6CLN6MQQM7Yjkt1BQvIj7rkFn13hgCALncyljyCU1sVPXdxL6cf9yYKXD390G4HOBKZxNkHMVjnO6Hj-sd9djAjHO5LmWFJs0LIXz0-X01lSglhfeVnL2ZeDH7UlG5RrmV_T7qgtG3Zrmlll8RFxg2tTrHaLr4M0eyR1QeQJFVgeo8HMdtQuFios65HKy3oupKdYnu4SVGPfG0-rVGr6cuKkLfG8sL3ou9RAnlxqqUzYY24SvOLXrmgYzri8vJG2QHET5TU6yvgD4ADkAKmxT2sLMMg63ScaD8cdK-_x97jVgDrVuw77ZcMFNUyKrB_NNq8efjXpe60mR2kaldODpswHHhehjlqIcLhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو:
نگران هستم که این عنصر خصومت علیه اسرائیل، به ویژه در حزب دموکرات، وجود دارد.
من نگران این موضوع هستم، و تا جایی که بتوانیم کاری برای رفع این مشکل انجام دهیم، من قطعا آن را خواهم کرد.
افرادی که از اسرائیل متنفرند، در نهایت از آمریکا نیز متنفر می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131933" target="_blank">📅 19:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131932">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یک بالگرد آمریکایی در دریای عرب سقوط کرد
🔴
نیروی دریایی ایالات متحده اعلام کرد که یکی از نیروهایش کشته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/131932" target="_blank">📅 18:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131931">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6Gix-asE9kzBEvzEqb-mlgrgbTSKpp588e137vWzdJ88jyOGfIleFBs0-PzO7igDIJQjVb-Jb419eTCYsczvC5PQWGT0Mlqzd5QkqvCpw0JEAjiMv1T9C5QWX0BXgAAAu-XC7REDSSDufRzPWb2k7kyjklb-poXZWDVeisyJbDUaWeO-VOL69gYaZDAeJAV8j5dSTHrpc2k0-S4LvBHeXNdioC0lQ8qO-_vLpxAQqeo2lZkaR7qbdd0P60jDxeyNE0iUW5kzADgfzho1YqdD6WUszatfrFHln4JfACvTavyfrAmLB4nY0cgONa1g7WWO4DqgRJ-XD6cwn6ijbpMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:
پیاده‌سازی تفاهم با آمریکا سخت، اما شدنی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/131931" target="_blank">📅 18:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131930">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=rtS7rcwyCZMj7SRnKFGHpiLN13HjBRdLui5Ql9i-3hYjtIoICl6gHNsRarkjt2hSWuqZFkZHDjVvuvY1ysfOq0puDdWPSLEVd-hr10vvvrhCdav2lEFcho5CFBMsHdjll8aRxaWLbvd0IxfFfJ8MtFzbgubBReTxQpTPnPQxegzOu9OVvj3yQjcRMoAbr33WQGuiWOCZ6BbSADCximZZMPDsMOYS5tX_ocuB6iApqXmMpn9sKpvOjrSOvj2M-zVCvMcNqHB3yeM8JdQ4n5Skx9SD4cv3WGjOpFO6pv7jD-cG_NL72yjnA37wwCPlrniZIEMKs-8UKd2BcRVUmHyX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=rtS7rcwyCZMj7SRnKFGHpiLN13HjBRdLui5Ql9i-3hYjtIoICl6gHNsRarkjt2hSWuqZFkZHDjVvuvY1ysfOq0puDdWPSLEVd-hr10vvvrhCdav2lEFcho5CFBMsHdjll8aRxaWLbvd0IxfFfJ8MtFzbgubBReTxQpTPnPQxegzOu9OVvj3yQjcRMoAbr33WQGuiWOCZ6BbSADCximZZMPDsMOYS5tX_ocuB6iApqXmMpn9sKpvOjrSOvj2M-zVCvMcNqHB3yeM8JdQ4n5Skx9SD4cv3WGjOpFO6pv7jD-cG_NL72yjnA37wwCPlrniZIEMKs-8UKd2BcRVUmHyX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی: یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/131930" target="_blank">📅 17:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131929">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf7loJauujROB5QtQkJPTnUMtOmuyliS66-MpHQw82OJ4ByRJX2RT1V_WRY8wWTqRnLryRGBKd0M0fnrfiDi9AthC1Q8iUcjpoVTtgcDPG6ZwGWV-khTB2kWmUpH4a4tomni4yTlImHNNixQ-XAmvNtM9DbOMiTdlh2BXN1zbfq0dUWdwiI_W9fNt8JCB6WFx-HJSGJ1ITwSkicqQIFAiNOH2fQu_Tc5al-vyMXtf993Cl3SV9cpaYKZ1hb85aQmTvHvB2Kbh3zcXOsE0iekelpfomlnEIe1BYVCwx4CAmA6TdGZqGulIOaAPa9EBVhaHyErof2D6iFDtkHelXTXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پربازدید از نیروهای امنیتی مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/131929" target="_blank">📅 17:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131928">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کارشناس صداوسیما: آمریکا رو به افول است و کارش تا ۲۰۳۰ تمام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131928" target="_blank">📅 17:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131927">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/131927" target="_blank">📅 17:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131925">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
شورای هماهنگی تبلیغات اسلامی: مراسم تشییع رهبر شهید روز دوشنبه، ۱۵ تیر، رأس ساعت ۶:۰۰ آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/131925" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131924">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEh8kmRRpq28HwXD78HOZhfH-0tgtdp5oNJ2gNB7CAYnfZykmJ8Fk3GXf2snl151Kx8DqR1IU7o4CwDsSlnvMVdr1RMlqWxDwpa5MqYQihNHbNQ5nvzWO1mwBNdJZq4NKug0V-B2RxAJ5BVlc8P4RNSYb__dv9Bl3nd7mN_IHH5j-20YGUzTfaa4YFSdVLGd40fi5oM64MgVqdl7BzehRXDOpLMzbuPYDQn62_Jn7-XkBd_u_qv1Wp_Qx0XXpJzPhsol64nEYL7BzzMTB1SpuPQboDj74Iolixc5K3KCraVgloupDDIAYPyeS9Rm1fy3RQs5ykxjue8HlyLeJ4R23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/131924" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131923">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f5adc8aa.mp4?token=Ny8fmx3xBjuc7SfOyo1fqjD0JwvAX8yeIIDoFw5Y3ooJXayC43e6I40kY7qCtf-uIkdbAYeOsevEPDjQjWhFb9v8GGwoD4EYEzRl_5Fk45eT8C6oqgyBeNFDa1EtqimAD3Dy1IPY0T2y1DcNA65F3AozkG4F-J-l1s49Xjx2xRZfh3u9PXSsw4R3VwzKxqMpx9aN6ZbuW0y47I4cb0vy2ZCZzBn7WBWhApXc8I6R4D-XzUkg9VDVNxk6VFmnR-kYFaWG_OLc2Jpo3dyedWpNzbCi0LbS2372O4Ld-2IIsY8EuBxtFlFmsx60UQBmdMw3LIlAwS5pIbMoCg_f1gasFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f5adc8aa.mp4?token=Ny8fmx3xBjuc7SfOyo1fqjD0JwvAX8yeIIDoFw5Y3ooJXayC43e6I40kY7qCtf-uIkdbAYeOsevEPDjQjWhFb9v8GGwoD4EYEzRl_5Fk45eT8C6oqgyBeNFDa1EtqimAD3Dy1IPY0T2y1DcNA65F3AozkG4F-J-l1s49Xjx2xRZfh3u9PXSsw4R3VwzKxqMpx9aN6ZbuW0y47I4cb0vy2ZCZzBn7WBWhApXc8I6R4D-XzUkg9VDVNxk6VFmnR-kYFaWG_OLc2Jpo3dyedWpNzbCi0LbS2372O4Ld-2IIsY8EuBxtFlFmsx60UQBmdMw3LIlAwS5pIbMoCg_f1gasFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زینب سلیمانی: شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/131923" target="_blank">📅 17:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131922">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/131922" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131921">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDMFeM2ZZrpY3EwazNnsULKQIPgBen_Ya71PTL1DNBTtr7ixOkUIUruXN_HkgaTLx3m6Dtuwd0uHYSh1J3r-9knPRzbs1r7ShE5KZAV8cxtQCFw_Zav6LNNodJQr9tkpmdG2Py1EkarSDmAdXAmEivnnslDfbrmYUgilkirjfSTN16WP_ocXNkOrwSQ98IGSvqCoCT7cIERV6itlw-isZo7br_T_i__66mw20KPHeDV0V-NuwW86dz_G34-yORtYZmLmX54Q9Zp4NyifEyEyT2HXPiCUm9LDTA3nbkJ6LJB9_0WsAIDaLT9Y_Nlryd--G-z_i_280WhdE8A1Gg_YnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حضور سردار وحیدی در مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/131921" target="_blank">📅 17:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131920">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d57f1ea3b.mp4?token=TRbepTxrtgHW3zI4ZcrPNqU1twM-n7WWf2uD4V0da2NIeRlbmYNpYrasauwIw0hLrLfpd00tJizUf03oljGuN5AYBOKk_8CjQ7yuAD8X0VQd9tU3fJ-X_KM43MaKfYUm70a7nfj0UPitOKPs9s0XYfKciFXERkuWir2bBOCu4OW5CbRsOPQBSBtmLdLIilE7AF784C8Y5MBW3itcIuZjJ9Y_J9q2nXcuwe8qnzoXjwpdanpnPNZnTC9H8eY_ryHTrriznHRfwqX-GxORRW3pO4Qn26nvZSWzmUqIpTxz26vgIVNdLVJlvRxbc-74SmIpjL7kC2I7UUpZjSeWDnJN5ILjl7wGA_JxNjRSrtX3YwyalerJeFMYuyjnvDTiG9106fKOLFMnnXvAGth1BRzfkp9YGxhY91jPtonF1wSGaAaaMMILrrmRC3u7y3JuNzmpWktknX5s2CVCaGkcqBqgFjcBC0sR7g2ESk1fX0BzNIVD6USXGcfypUrv2CAX6uVZOTq3oNs7hQfefgJ_OIFZBeb6Z9zFoeX3GLWKDHfUSQNXqQ11Q76fkaN0ravbX1HeulzQcUXFcIToQgL_slFV_6ky1BfUFQuGyZOsE-ssKONNgKupbCGyFQ3yv2uMshkCFgG9lmFLwAEBwGcZLjluBmZ764Fs00J1mjNTVDO6FEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d57f1ea3b.mp4?token=TRbepTxrtgHW3zI4ZcrPNqU1twM-n7WWf2uD4V0da2NIeRlbmYNpYrasauwIw0hLrLfpd00tJizUf03oljGuN5AYBOKk_8CjQ7yuAD8X0VQd9tU3fJ-X_KM43MaKfYUm70a7nfj0UPitOKPs9s0XYfKciFXERkuWir2bBOCu4OW5CbRsOPQBSBtmLdLIilE7AF784C8Y5MBW3itcIuZjJ9Y_J9q2nXcuwe8qnzoXjwpdanpnPNZnTC9H8eY_ryHTrriznHRfwqX-GxORRW3pO4Qn26nvZSWzmUqIpTxz26vgIVNdLVJlvRxbc-74SmIpjL7kC2I7UUpZjSeWDnJN5ILjl7wGA_JxNjRSrtX3YwyalerJeFMYuyjnvDTiG9106fKOLFMnnXvAGth1BRzfkp9YGxhY91jPtonF1wSGaAaaMMILrrmRC3u7y3JuNzmpWktknX5s2CVCaGkcqBqgFjcBC0sR7g2ESk1fX0BzNIVD6USXGcfypUrv2CAX6uVZOTq3oNs7hQfefgJ_OIFZBeb6Z9zFoeX3GLWKDHfUSQNXqQ11Q76fkaN0ravbX1HeulzQcUXFcIToQgL_slFV_6ky1BfUFQuGyZOsE-ssKONNgKupbCGyFQ3yv2uMshkCFgG9lmFLwAEBwGcZLjluBmZ764Fs00J1mjNTVDO6FEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وحید خزایی جلوی سردان رادان میگه ترامپ گوه خورد وطن فروشا لاشین بعد مثل الاغ ماده میخنده.
🔴
پ.ن: وحید خزایی سال ۹۳ تا ۹۴ یکی از بیشترین پرونده هایه سو استفاده جنسی مال این فرد بوده و بعد از خروج از ایران دائم سایت شرط بندی استوری میکرده
🔴
ویدیوهای متعددی نیز وجود دارد که وحید خزایی به آیت الله خامنه‌ای فحاشی میکرده اما اکنون ژست دیگری گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/131920" target="_blank">📅 17:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131919">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJFlSgNtZZWUcbqjK178pYCYnXHEaQS4zuk9JMuJM9M79ZeKPM8gHvG_-G3KeOBnjIOfsJlNeu2xOh-12vrl5Cwt9IO2BELuQKzgUG_SITvqyuy0r3oAI_ikc7eWbNnPG5ot0kx3jKAd0RMYGiCHZUwulpLd5wPQf7R6Yuj3TAB3iTz-OO1hF1O0ZfdUsM6UqsS4MOcSSYvRGGqG3M46C3CLMfpTfpZ5p9Z9pYaYMWrZM2LsoToZKYWUJCmb-NlRdYnrdhGdtEpFcfMM-C-gYGJWSuGfQobbUCuVARJvKgKj2L8CHaI-HOrvPDVmwQR-ffRWEAYOoGaZNuAV8C_Qtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر برگزیده رویترز از زمین لرزه ونزوئلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/131919" target="_blank">📅 17:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131918">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ : ما بهترین بازار سهام رو داریم، واقعاً عالیه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/131918" target="_blank">📅 17:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131917">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
فارس: کارت ورود به جلسه امتحانات نهایی، تا پایان این هفته منتشر می‌شود. امتحانات نهایی قرار بود از ۲۰ تیر آغاز شود که با یک روز تاخیر از ۲۱ تیر آغاز می‌شود و کارت ورود به جلسه این آزمون هم تا پایان این هفته منتشر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/131917" target="_blank">📅 16:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131916">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
یائیر لاپید، رهبر اپوزیسیون اسرائیل:  اسرائیل باید زیرساخت‌های ایران را بمباران کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131916" target="_blank">📅 16:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131915">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
از سرگیری تجارت دریایی ایران و قطر پس از حدود پنج ماه وقفه
🔴
رایزن بازرگانی جمهوری اسلامی ایران در دوحه از بازگشایی مجدد بندر الرویس قطر به روی کالاهای ایرانی و ازسرگیری تجارت دریایی میان دو کشور خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/131915" target="_blank">📅 16:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131914">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/131914" target="_blank">📅 16:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131913">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بنیامین نتانیاهو: بازسازی غزه بدون خلع سلاح و غیرنظامی‌سازی در مناطق تعیین‌شده،امکان‌پذیر نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131913" target="_blank">📅 16:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131912">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نتانیاهو: ایران می‌خواهد ما را از جنوب لبنان بیرون کند و آنها سعی دارند به ایالات متحده فشار بیاورند.
🔴
ما به خوبی از پس این فشار برمی‌آییم.
🔴
ما حفظ منطقه امنیتی را از دستاورد بزرگ خود علیه لبنان می‌دانیم، اما آنها سعی خواهند کرد از هر طریقی، از جمله اعمال فشار بر دولت لبنان، آن را تضعیف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/131912" target="_blank">📅 16:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131910">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344ee59971.mp4?token=JWORh92mgh_4Aipbd94HPU3a9R1F_JYEEVlZi3NE6uTOum2Gffageh1opkDt15NidKfJXd3qXILyToWvT1m1JZ7leTZy6UQht8HaV8KvBYGhN0G0wd4ER5SwT6SF-WA5yrEv49VxGtLrAjhKYM9MW4SDMjmArvTeQZooCNLuqF4SBbxcF0EUyIroykXDcIqSuYza9S0L89AW66_LaI6fYYOfxYvGTaudTp253v6D144HaRBK_TQEShHgrYflYbOtWtrLRm-ZQx90cSaqaNUne451PNkqIsKRPcAAuIyxntGq8AaRZrq8JD-eyTCdAgt4XHl0oEns0xJe0gAgt3mGxJx3TbgrYa_ZZHzoJAgItEFvIm_7Rb8Mf5FFMMAuXmR5NCPaO1DvvTbKRM4x90FvWx3MdsxXmxfiwmd2aXpMibp0K5IhjHfiyt9N9OryvhaUNCIZQqzwSQBJ3VtDjs_vfgII1J7_mehIG7hpiQZxg3nAk7xfOur2hvEHEFkPfFdOkb_RkXf15if5PJEAy2hp4KMlrCipwo-KzNOeARju1T3gPSb_g3-i5XoKc4TOnJt8yn-d1URRl4Mjddt5SaA9WkNr2A4HFUUK_ni_4bZw101CFbFk7-UZsIPOL3fd0hjyBtMSLSl2pr10ssQn1h8qp8rwdkXmlvVE_aH8di2GY_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344ee59971.mp4?token=JWORh92mgh_4Aipbd94HPU3a9R1F_JYEEVlZi3NE6uTOum2Gffageh1opkDt15NidKfJXd3qXILyToWvT1m1JZ7leTZy6UQht8HaV8KvBYGhN0G0wd4ER5SwT6SF-WA5yrEv49VxGtLrAjhKYM9MW4SDMjmArvTeQZooCNLuqF4SBbxcF0EUyIroykXDcIqSuYza9S0L89AW66_LaI6fYYOfxYvGTaudTp253v6D144HaRBK_TQEShHgrYflYbOtWtrLRm-ZQx90cSaqaNUne451PNkqIsKRPcAAuIyxntGq8AaRZrq8JD-eyTCdAgt4XHl0oEns0xJe0gAgt3mGxJx3TbgrYa_ZZHzoJAgItEFvIm_7Rb8Mf5FFMMAuXmR5NCPaO1DvvTbKRM4x90FvWx3MdsxXmxfiwmd2aXpMibp0K5IhjHfiyt9N9OryvhaUNCIZQqzwSQBJ3VtDjs_vfgII1J7_mehIG7hpiQZxg3nAk7xfOur2hvEHEFkPfFdOkb_RkXf15if5PJEAy2hp4KMlrCipwo-KzNOeARju1T3gPSb_g3-i5XoKc4TOnJt8yn-d1URRl4Mjddt5SaA9WkNr2A4HFUUK_ni_4bZw101CFbFk7-UZsIPOL3fd0hjyBtMSLSl2pr10ssQn1h8qp8rwdkXmlvVE_aH8di2GY_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ  در حال تماشای خودش در فاکس نیوز
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/131910" target="_blank">📅 16:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131909">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
آلن آیر، عضو تیم مذاکره کننده آمریکا در برجام: برای مذاکرات واقعی میان ایران و آمریکا، باید به گفت‌و‌گو‌ها زمان زیادی داد
🔴
به افرادی نیاز دارید که بلد باشند همه ۸۸ کلید پیانوی دولت را بنوازند؛ کوشنر، ویتکاف و ونس؛ این‌ها سرشان شلوغ است و مشغول کار‌های دیگری هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/131909" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131908">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9e3c0b51.mp4?token=fkn5RlKQRFmUKJx69v2FwnDhOxnvhMDrO-KPv5LbuvYi5l4mMRaPps-GPKQG1IqjafUbUvdyfBH1_GOhpY70E6qQDO-Crid0yekv7NSVE24-W3-DjXGzWCGyQZhLb73MhMV_uMJgH12Obs2xqpSXOsJ-ADrS99s-kujJCG2oofPfaGoFwR3lKnIQkX-D-DXF8_fSyzGXXqBlfRhe62kVbpBzS9uUwuSCJWpJfOOU9k6p0BhgyHQd7RwHs8e2K0sF4UWr53qfNvKe2PaNbU25izWT-EHjQTapLZCtnthOJBX_0W_nwGM05Z2nxeOc3P7Ob08HqkDpx-OpbdY25YupaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9e3c0b51.mp4?token=fkn5RlKQRFmUKJx69v2FwnDhOxnvhMDrO-KPv5LbuvYi5l4mMRaPps-GPKQG1IqjafUbUvdyfBH1_GOhpY70E6qQDO-Crid0yekv7NSVE24-W3-DjXGzWCGyQZhLb73MhMV_uMJgH12Obs2xqpSXOsJ-ADrS99s-kujJCG2oofPfaGoFwR3lKnIQkX-D-DXF8_fSyzGXXqBlfRhe62kVbpBzS9uUwuSCJWpJfOOU9k6p0BhgyHQd7RwHs8e2K0sF4UWr53qfNvKe2PaNbU25izWT-EHjQTapLZCtnthOJBX_0W_nwGM05Z2nxeOc3P7Ob08HqkDpx-OpbdY25YupaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی به تخریب منازل در شهر بنت جبیل، در جنوب لبنان، ادامه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/131908" target="_blank">📅 15:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131907">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCTsZBB9a2rQaXwTxwVxTN9OClZLCzOtrH1R8tgCN03mmaPhwRVPn5ZtIMrX_5kSnQ-Xkp0WRzDW8dQLD1o1YYmkTfh1W9iGTVcZVmA--p9T0YND-Jsv7VkVoMaA4S_6wm8vx7avjqq6EF_fATyCKwJst--qrAXFJKnlg4jzxBx7KwPuyITPn8_JfSA2X-5vqqW8O1IhoAxEuP-mOk1C0AcQ2GNlUPW-m3RY6HmxPPcy2AZbbhGiRpb42c9RiYy1oUrYgAefbRbkg3sYOzMthGQI_SR7T--4urJ6X18S3PlXNai20UkBXE1V92sjNejAlqbnmFfMtAQ7RdLLKS0GVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی در سواحل یمن مورد حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/131907" target="_blank">📅 15:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131906">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
قطر، تعلیق موقت فعالیت‌های دریایی را لغو کرده است، که در نتیجه، تمامی فعالیت‌های کشتیرانی و عملیات دریایی فوراً از سر گرفته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/131906" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131905">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ریاست‌جمهوری سوریه: امانوئل مکرون به‌زودی به دمشق سفر خواهد کرد و یک هیئت از سرمایه‌گذاران فرانسوی در این سفر، مکرون را همراهی خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/131905" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131904">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FidBA8KGjMSe9J13ACTRnkh1r3bjppUfYFMLBa89LmSXACwylTQfrke-QOT6dsPltQnJlIC2J2p3oO5q6KWQpbn3cL5Zyu6efD8s4jrYAY7ZcM46QSDK1Tg9VYl-QNAqBINcuwpyXxiVd9yiw3ZrNwIQb0GbqIv4pmkfhcol_Y63RCted6-c4Co68SOfiEtF3eVWYi5FpPqzufNjr5LUErmM7PyyyccIjpmxOJIUslEcKWn9ssA-dQixWG-S6WyKIwN5rTFKBoPHWmWi7teut0M9c2TsnpBCbE8-TIhGImZInSLO-ov_omPKFk9R2gk6ZKxxVLwohEGfPSea7N8Xeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ در تروث: از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131904" target="_blank">📅 15:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131903">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل: تهدید ناشی از غزه برطرف شده و هیچ بازسازی‌ای در این باریکه بدون خلع سلاح انجام نخواهد شد. به ساکنان غزه آزادی انتخاب داده شود تا میان ماندن یا ترک تصمیم بگیرند
🔴
ترامپ از ما نخواسته است که علیه تونل‌های حزب‌الله اقدامی نکنیم و برای باقی ماندن در امتداد «خط زرد» در جنوب لبنان، مشروعیت لازم را به دست آورده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/131903" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131902">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سفیر ایران در چین اعلام کرد تهران پس از پایان دوره ۶۰ روزه توافق اولیه با آمریکا، برای کشتی‌های عبوری از تنگه هرمز هزینه خدمات دریافت خواهد کرد، اما کشورهای «دوست» از شرایط ویژه برخوردار خواهند شد
🔴
رحمانی فضلی گفت ایران همراه با عمان در حال تدوین سازوکارهای جدید برای تردد در تنگه هرمز است. او تأکید کرد مبالغ دریافتی «عوارض عبور» نخواهد بود، بلکه هزینه خدماتی مانند تأمین امنیت مسیر، نظارت بر عبور کشتی‌ها و رسیدگی به پیامدهای زیست‌محیطی تردد دریایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/131902" target="_blank">📅 15:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131901">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فارس: قایق‌های سپاه 6 کشتی رو از تنگه هرمز خارج کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/131901" target="_blank">📅 15:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131900">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کدام فرودگاه‌ها فردا تعطیل هستند؟
🔴
در روز ۱۳ و ۱۴ تیرماه پروازها در سراسر کشور بدون محدودیت انجام می شود و برنامه پروازها به روال عادی ادامه دارد.
🔴
۱۵ تیرماه همزمان با برگزاری مراسم تشییع آسمان تهران به طور کامل بسته خواهد شد.
🔴
۱۶ تیرماه نیز فرودگاه مهرآباد فعالیت عادی خود را از سر می گیرد و فرودگاه امام خمینی نیز تعطیل خواهد بود.
🔴
۱۸ تیرماه همزمان با برگزاری مراسم تشییع در مشهد، آسمان این شهر و فرودگاه هاشمی نژاد به طور کامل بسته خواهد شد.
🔴
در روزهای ۱۷ و ۱۸ تیرماه نیز پروازها در سراسر کشور به جز مشهد بدون محدودیت ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/131900" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131899">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
روزنامه عبری معاریو در گزارشی مدعی شد که دونالد ترامپ، رئیس جمهور آمریکا، برای برگزاری یک دیدار سه جانبه در کاخ سفید با حضور بنیامین نتانیاهو، نخست وزیر اسرائیل و جوزف عون، رئیس جمهور لبنان، تلاش خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/131899" target="_blank">📅 15:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131898">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e49482f3e9.mp4?token=MSfKPppzpTHDXmsx0rwmGARfta9TA1m3pgllC_xY3zdwed6kjWO1MoqMJO1FavFu8Ug7dxUL9JkxHyNVNXqdOboCxyJ65FU4NPAMSFUIlXpruZxy3KKi3QUPnrVF3tVpVIvsgfxgclsTIYEj48ohnVAQAPOgNHOxOc7XA-gVNu2iG2Lne1EVIf-xivPj9EVidq-tKynXEPbHWurqtYE6HX82dDg1495vxiILSqA1SpIH4I9pRhZXikZ4tMRlT2r-WDcG8jQwaNj4_h6r0mH93w0551R6nSvFK8OBOfEQxLC8ufj--eyQQ48i0QNAitXh9o954g-p9UxVN1w_UNwYgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e49482f3e9.mp4?token=MSfKPppzpTHDXmsx0rwmGARfta9TA1m3pgllC_xY3zdwed6kjWO1MoqMJO1FavFu8Ug7dxUL9JkxHyNVNXqdOboCxyJ65FU4NPAMSFUIlXpruZxy3KKi3QUPnrVF3tVpVIvsgfxgclsTIYEj48ohnVAQAPOgNHOxOc7XA-gVNu2iG2Lne1EVIf-xivPj9EVidq-tKynXEPbHWurqtYE6HX82dDg1495vxiILSqA1SpIH4I9pRhZXikZ4tMRlT2r-WDcG8jQwaNj4_h6r0mH93w0551R6nSvFK8OBOfEQxLC8ufj--eyQQ48i0QNAitXh9o954g-p9UxVN1w_UNwYgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور ایمان تاجیک، سخنگوی جنگ ۱۲ روزه، تو مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/131898" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131897">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل: حزب‌الله از توافق ایران حمایت می‌کند و توافق ما را مورد حمله قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/131897" target="_blank">📅 14:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131896">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سفیر ایران در چین: کشتی هایی که از تنگه میگذرن باید هزینه ناوبری بدن ولی برای کشتی های چینی تخفیف و ملاحظات خوبی در نظر گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131896" target="_blank">📅 14:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131895">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlq8ODjZu0oVPhVwrx0K0UyAqKAfmONwy9pkK7vwPKZpbWw0hFkcE6_RLLrkE6YHtKIs8cFS7xHxTHfw9yiQmoc14XypAXhQDx1ZMZYVZYQpGsCglshJyTKl1erryrKkchlADSX-lIQaB7iEmLR-tENh4ak8UhP5xLu-m_4_R5hykToS7DEQuTD3QzmAVj20bHwFu4PZQrkRWv0knKM_NbPiVKPu94llAjParalaPw2dTkkFFBthcEUAODrE51xMNXjCvkhSSIep7MAm9MxhIoXcnwWiHKg-yQr5YqmXZ9I46RWiVYZexN5FinmZ1Vtu4VQql4CytdeDi0x06bPi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در مراسم تشییع
🔴
خواهیم دید چه می‌شود...
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/131895" target="_blank">📅 14:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131894">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
🔴
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
🔴
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/131894" target="_blank">📅 14:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131893">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
محمد مخبر: قاتلین امام به مرگ طبیعی نخواهند مُرد و نظام انتقام خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/131893" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131892">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589db9025b.mp4?token=MKablKOck1pMjUfoQmBknlDYWxqoIf10iwVuyW5pRIslyJwxiJeXJoiJpSrGUveDUx6caAuClQoLCBcYa9LolOR9TxP-o9aOvUDGKq4JmHf7pBsVxpfjVWOnNP8-9Ez7wrcMdObuxnuaCZWN9iQxjzROEw4S5xcZkndg9MN2PFKT5Sz_uD4H47b6CnBUI9DLq04lEAuTGzm7NlosJHlPJtAFx1DyRPCBGvXyclEiZ3cDh6vUiLwP85b611EZh5-afQyA6bjckU2l9YzyJZOMwuanDgviuqGkIsynrTgyzco4zkKKpqNVBmxHu6ErvQq-EzEDlRMgQzrSdcLjOpMjzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589db9025b.mp4?token=MKablKOck1pMjUfoQmBknlDYWxqoIf10iwVuyW5pRIslyJwxiJeXJoiJpSrGUveDUx6caAuClQoLCBcYa9LolOR9TxP-o9aOvUDGKq4JmHf7pBsVxpfjVWOnNP8-9Ez7wrcMdObuxnuaCZWN9iQxjzROEw4S5xcZkndg9MN2PFKT5Sz_uD4H47b6CnBUI9DLq04lEAuTGzm7NlosJHlPJtAFx1DyRPCBGvXyclEiZ3cDh6vUiLwP85b611EZh5-afQyA6bjckU2l9YzyJZOMwuanDgviuqGkIsynrTgyzco4zkKKpqNVBmxHu6ErvQq-EzEDlRMgQzrSdcLjOpMjzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات توپخانه ای اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/131892" target="_blank">📅 14:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131890">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
مدودف: ایران سلاح‌ هسته‌ای اش را حفظ می‌کند!
🔴
ایران به جای داشتن یک سلاح هسته‌ای واقعی، متوجه شده است که سلاح دیگری دارد که از سلاح هسته‌ای ضعیف‌تر نیست، یعنی تنگه هرمز، که وضعیت بین‌المللی پیچیده‌ای دارد. ایران نه تنها این سلاح‌های هسته‌ای را حفظ می‌کند، بلکه یک سلاح هسته‌ای حرارتی نیز دارد که همان تنگه باب المندب است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/131890" target="_blank">📅 14:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131889">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfkvegVKaFS_0qON9CvORdGzims9hGu6tJMAhDBgouudUANa6Cl_O6KoWEk4RqdwPgXYsDWSTwkJo0a1uVC48ise0i93Q8AkFE3sNbOpRii5IdIm2I3PlmYcpTwIQUT9Ze6ZUQwuoioeCy4KRPrexUScG5wTqpeiibqI8RDGF2pisIAiu4wriyRtnNbIliNPuI5AwzbALz69fN3rwF262LeY192t3-5KDfTJ0m6U2b7Tw1ywAlwC_8Ez7HLU4COr0PO9i67EGMQI2sOakDfN9BilaAsDXi3GWes3q2jIHXlJCcXAGijfqi5zfiH0TLzg1FKq_n9B9uto6z7Wpf11fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیرخانه شورای عالی امنیت ملی:
این چند روز چشم‌تان را به ایران بدوزید؛ این همان ایرانی است که خیال می‌کردید چند روزه می‌توانید آن‌ را از پا درآورید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/131889" target="_blank">📅 14:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131888">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خودروسازان چینی با رشد سریع صادرات و استقبال بازار اروپا، برای نخستین‌بار از نظر حجم فروش از رقبای ژاپنی عبور کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/131888" target="_blank">📅 13:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131887">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
شرکت بهره‌برداری متروی تهران: از بامداد تا ساعت ۹ صبح امروز، یک میلیون و ۳۰۸ هزار و ۴۴۵ مسافر، بیش از ۳ میلیون سفر در متروی تهران داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131887" target="_blank">📅 13:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131886">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
به گفته برخی منابع در اسرائیل معتقدند احتمال وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/131886" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131885">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
دولت ژاپن در حال بررسی کاهش سطح هشدار سفر به ایران است
🔴
در پی بروز جنگ آمریکا و اسرائیل علیه ایران، وزارت خارجه ژاپن سطح هشدار سفر اتباع خود به ایران و 3 کشور منطقه را به درجه 4 (تخلیه فوری) افزایش داده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/131885" target="_blank">📅 13:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131884">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ny-4Hp1IxyGcEutB_ZzHXLmJWLRrqPUo73_nRvUZO_uIUt_QDIIsahYnwbQHWr4t6GHl0NVFJ77kdxM3rR9g9m4uU45BWLhEefX8DhKSE5EGwoAGgzROxq52MvEJh0cFSUJ0oVSn_j9EbZn4WPOfngqlNH7Lh4RAtY2pJugEqxSA0m5ECqg9fQ_IUve9RIn-L4xAhHnAp2qFI0G9nxtaBjB6QTTSOAi2SlFHdVoreGKNQBgUitbIJMbv84Nmm4S5g1fGud6Nh1SxnthI0NC-w3K9v7oGsiO6SipEKCvFEjasdX8dIrNjmOQ85nzrkOGArlSW4Tni73ZBuCHnqpG1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت آزاد کشمیرِ تحت کنترل پاکستان
🔴
با گذشت یک ماه از قطعیش، هنوز شدیداً مختلهِ - Nut blocks
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/131884" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131883">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
تلگرام از مرز یک میلیارد کاربر فعال ماهانه عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/131883" target="_blank">📅 13:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131882">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
جوزف عون، رئیس‌جمهور لبنان :
من علاقه‌ای به اسرائیل ندارم، اما راه حل دیگری را به من پیشنهاد دهید که ما را از این جنگ‌ها بیرون ببرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/131882" target="_blank">📅 13:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131881">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
العربیه: ترکیب و سطح هیئت اعزامی‌ایران هنوز نهایی نشده و پس از پایان مراسم تشییع، تعیین خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131881" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131880">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjY0z-DI4c61KiP-U1PlNNhi6xRJTSGWhN1wHdxFJ3rlZ3p-fmbFQHX0lJ64wnWCQ2dwb1kOThIMJSfATuCmKMDWJdaF9vJ10irQpqMM_wMrfW80E4AGYJ8NsOrP_GGtWtss_qmjBST324mM0-X_FP7_e7T4CJJxo8_6nnbbH96iy9xbVm8x_yd1ltAph_HO4WL3SI3l_meL-BwdBjamWExnGNGNpAYvPEMIbp-TTvUj12HG3XovboT2QiGiNR3AULDMgShI4VBnvSt28KJ7PYsN0GQtHbMxK5p5flxVXRvTvNouweKydxSOpz_RkevCaJ_Y0nNpbrsWsP13hsx_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکایی ها مجددا یک گروه از نفتکش ها را ردیف کرده و در حال اسکورت آنها به سمت تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/131880" target="_blank">📅 12:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131879">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سامانه گنبد آهنین به امارات ارسال شد.
🔴
میری رگو، وزیر کابینه اسرائیل مدعی شد که اسرائیل سامانه پدافندی «گنبد آهنین» را به امارات متحده عربی ارسال کرده است.
🔴
وی همچنین ادعا کرد: اماراتی‌ها از ما کمک می‌گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/131879" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131878">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: نتانیاهو احتمالاً هفته آینده به کاخ سفید می‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/131878" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131877">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سازمان دریایی بریتانیا: یک کشتی باری در سواحل الحدیده یمن از سوی افراد مسلح ناشناس مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/131877" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131876">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل از حمله هوایی به غزه و ترور دو عضو ارشد حماس خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/131876" target="_blank">📅 12:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131875">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
استانداری هرمزگان: احتمال شنیدن صدای انفجار ناشی از خنثی‌سازی مهمات در امروز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/131875" target="_blank">📅 12:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131874">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
دعوت رسمی از ترامپ برای سفر به پاکستان
🔴
آصف علی زرداری، رئیس‌جمهور پاکستان، هم‌زمان با روز استقلال آمریکا، به‌صورت رسمی از دونالد ترامپ، رئیس‌جمهور این کشور، برای سفر به پاکستان دعوت کرد.
🔴
حساب رسمی رئیس‌جمهور پاکستان در شبکه اجتماعی «ایکس» اعلام کرد مردم این کشور مشتاق استقبال از ترامپ در اسلام‌آباد هستند و میزبانی از وی را مایه افتخار می‌دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131874" target="_blank">📅 12:24 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
