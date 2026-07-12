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
<img src="https://cdn4.telesco.pe/file/gXs83xBQpDXPTAqlZDYhWUt60pjHZsJ3-lP-AfDUV1sLWUUTvi5S4xI3MSzmiWmhQx-QDjROtaqChyKSYV55Q37UjIPUfneFozFeX2dYBT26v8cu03LTgnz-8GVCsOmh4x1sKrbAkaiodE9QFDiJGvYYzu8_-z-Dtsngohpf4rAWyM432soQhKaie7WoWGmHxJnJ7cM8kJV2WTyX7DcT7PsPGbZWWjPEqWacLjQwJsH9AF5A_ETaqDDKDAUFZ4eU_6rDNAVhga1E3vmRyQ3Uw2dLqBsgXAgTAdbKn8MZmqG00PuSxKozVhlZT0tlkasbU-hu2pNwimt6meE948vQ8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 919K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 23:32:14</div>
<hr>

<div class="tg-post" id="msg-133558">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHO5G641bDvoQ7KVkPI-jrTzYAG-oreDQ2g8KRmVj-iEKCIHt8F2JLx6kfwDknkJXQ74QWbGBY-MqqmEJxNq1MMgVDlYnkK0Rd25pttho6VwXAWz4vrj4xTb6LhVt8NdlPAzG2w0eJletxIImQmkhkCEqaEKGzG8YUjceJucZ6ICElu9a1wo0CPfDgStd26xIdOBXy0AvaZ6RKF-Ju9uR-AgxcB-ejkyZoAx1GT1Nu0GtNqloLBnu39GiBJccvCnTkMqAyYTEb3KLq6wAk-wt13_6j1JXCdwP0RhvpWonBy9FAjc9i5f_R2V6bPgWtRkgKE7TCWpy0W4lehFThJp3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/133558" target="_blank">📅 23:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133557">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBIolWdVM5e6cs_3dNbSW1cJcO8D91JBKfeCjCRWGIfZCc9pyV9bRy6KY_vb5TLFZmbnEHiWT-b2zLmFzT7KZ0OiEY1DgYv07F3RfbxRRywF23KFcUPCIydw9Z4XjIuvW8PEMVWC3jbI7yKl18UK0rdMCNPFljUZtVwB5o2kQRESuPZaFAtw-SlwxRHKbq3XEGF6mO6tkCcvwT_S7hOyd1Y3EHPgAAXn4LmAMW24Tg4c7Raw7A6qJNm2iX3QgMCKEIMjryFiRPugFoqUX-VuKC0jqIwenTDPqBB7UyHHlvX_Dds5d2LcxHbt7xpFDMsSUrEyL9wJ8EJxfl9g0E0wgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/alonews/133557" target="_blank">📅 23:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133556">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: «الگوی رفح را در جنوب لبنان اجرایی کردیم/منازل و زیرساخت‌های ۲۴ روستای مرزی لبنان را ویران ساختیم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/133556" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133555">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/723cbb9eb0.mp4?token=O0FCy7k-5mtfqR7pfzP0RanEgp2O1gDuatsr7t6vk0xS4hCtyTK3kjywATLAexGL4hUhRHnRh7i2RmW0ECpudDBQqOL9ZsDrZiPaCoAvAouvyppeUFN7J4cpU5gdJaFnSEiczGyS0FyCxRzXZNZKz4dAI5yCwQj4-NCxQQxdrMtufZYqwSmVWHzwjw4ggpdB8Ryom1vQ99_GYdsvLuPZ6pn-ZIZwnZK-uRuUFR9ZIX6TcSvnin_Darh1Z8Rdh9PZdBmnt9a7GW1ZWAgPB3pn_KyedUbKu78GtTCMs8rXVrs2eX02BAuznYtOHk-LwqA2dDQYt7ByiXcxXICgJuxcugkcNE8TNE__tguh0FnZz_3wHgMAS6ZagfBhN33DV1lB8w_imWD2Izw54QOpVi61QgePu168NWjRvrSUzGYyCkfjsvLv39BiwWnrtFC0BsdY_GsQWXVe_S8sHb1KhCUO-LA3mX5wsGG68L5fxrjkasb2uV8Xt9IhN0zgRdE-jik7ITtI1hTJKlokesoDZTqXfGC9mEEtnXCLEuXckiMn9A-oebiGsNgPGVv5IrdvwkqNvxlOBfu7MfT-Bp6PYsjg2qUfmouyRWYkPtjjUGMJpuqrQkdMH6oqjaId3TQ3tSbLZTolThqjP0wtRi2G3m4s1lraxOyMGIQ2LixQRgTn5q4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/723cbb9eb0.mp4?token=O0FCy7k-5mtfqR7pfzP0RanEgp2O1gDuatsr7t6vk0xS4hCtyTK3kjywATLAexGL4hUhRHnRh7i2RmW0ECpudDBQqOL9ZsDrZiPaCoAvAouvyppeUFN7J4cpU5gdJaFnSEiczGyS0FyCxRzXZNZKz4dAI5yCwQj4-NCxQQxdrMtufZYqwSmVWHzwjw4ggpdB8Ryom1vQ99_GYdsvLuPZ6pn-ZIZwnZK-uRuUFR9ZIX6TcSvnin_Darh1Z8Rdh9PZdBmnt9a7GW1ZWAgPB3pn_KyedUbKu78GtTCMs8rXVrs2eX02BAuznYtOHk-LwqA2dDQYt7ByiXcxXICgJuxcugkcNE8TNE__tguh0FnZz_3wHgMAS6ZagfBhN33DV1lB8w_imWD2Izw54QOpVi61QgePu168NWjRvrSUzGYyCkfjsvLv39BiwWnrtFC0BsdY_GsQWXVe_S8sHb1KhCUO-LA3mX5wsGG68L5fxrjkasb2uV8Xt9IhN0zgRdE-jik7ITtI1hTJKlokesoDZTqXfGC9mEEtnXCLEuXckiMn9A-oebiGsNgPGVv5IrdvwkqNvxlOBfu7MfT-Bp6PYsjg2qUfmouyRWYkPtjjUGMJpuqrQkdMH6oqjaId3TQ3tSbLZTolThqjP0wtRi2G3m4s1lraxOyMGIQ2LixQRgTn5q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید جلیلی در واکنش به پرسش مردم که «دولت گفته همه رأی مثبت دادند»، پاسخ داد: «اشتباه کردند؛ من بارها رأی منفی خود را اعلام کردم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/133555" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133554">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9054413b86.mp4?token=bqS9YW9cNv8pGTTqqbfTys6i1a62XjhTnTMgB_DGxMgq7pxoNY7Vg_bCn9nQ2I77Dz_rtue8F4pZ9h8MZUp8GrGr4JKtxygApTSAGLFuTA6nzwF9FMcu8PTktpkZTTLWwGOw1yK3GtwZbzMuqVJhzSPL4uPvYmhP-M63juQL2kcjdhSex2-793lr5YWWq4ffYjHpUKAC-UnlCEG69DXM7mteBIiq-T9P-74TiF9EQpbNxbqaFo4E3rVFSexwimW5B-a82ppygLMigXO8rdXPhuAzpvxVMIHTj0poDJGJfAjQeRjVPP_wcr7mpJYirOBJOmPSH--mjlRGOu1jlfdZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9054413b86.mp4?token=bqS9YW9cNv8pGTTqqbfTys6i1a62XjhTnTMgB_DGxMgq7pxoNY7Vg_bCn9nQ2I77Dz_rtue8F4pZ9h8MZUp8GrGr4JKtxygApTSAGLFuTA6nzwF9FMcu8PTktpkZTTLWwGOw1yK3GtwZbzMuqVJhzSPL4uPvYmhP-M63juQL2kcjdhSex2-793lr5YWWq4ffYjHpUKAC-UnlCEG69DXM7mteBIiq-T9P-74TiF9EQpbNxbqaFo4E3rVFSexwimW5B-a82ppygLMigXO8rdXPhuAzpvxVMIHTj0poDJGJfAjQeRjVPP_wcr7mpJYirOBJOmPSH--mjlRGOu1jlfdZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده جدید نیروی دریایی سپاه:
هیچ کشتی خارجی بدون شناسایی ایران از تنگه هرمز نمی‌گذرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/133554" target="_blank">📅 23:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133553">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نیروهای نظامی ایران با هشداری از شهروندان کشورهای امارات، بحرین و کویت خواستند از مراکز نظامی دوری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/133553" target="_blank">📅 23:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133552">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/065c481a53.mp4?token=SD1MfNKTJi1wXsYjGzvzqIKMb-V7IFXP6C8T5CFb9ReklPcxP0si0_Xo2RC7nEVOVb8bqkyQTikpKQh20PPCowvss6HR85EiAvMDr2ho5WVmXSVqyWi58BzVD4yaD_S0c_OwlU_mdtXorqReH9mH_HFyzSWgU_gE7UWKRHYNLlEjhY7w3a0GLM-k2XtBjXxaUSoyDpgLi4cHusdVWmqiOkBNUcBO8HLtfVS1GOicQ2eTKqiIEPvYQ-bD9U-kY4ZNLaLQIypKByPAOJPUcwseFPhbii2thFJ4zFDUXr7zqQmjEZuzt05dEM3452xTUej3iun09XRu22bK0-oQkVwPAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/065c481a53.mp4?token=SD1MfNKTJi1wXsYjGzvzqIKMb-V7IFXP6C8T5CFb9ReklPcxP0si0_Xo2RC7nEVOVb8bqkyQTikpKQh20PPCowvss6HR85EiAvMDr2ho5WVmXSVqyWi58BzVD4yaD_S0c_OwlU_mdtXorqReH9mH_HFyzSWgU_gE7UWKRHYNLlEjhY7w3a0GLM-k2XtBjXxaUSoyDpgLi4cHusdVWmqiOkBNUcBO8HLtfVS1GOicQ2eTKqiIEPvYQ-bD9U-kY4ZNLaLQIypKByPAOJPUcwseFPhbii2thFJ4zFDUXr7zqQmjEZuzt05dEM3452xTUej3iun09XRu22bK0-oQkVwPAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، درباره فوت لیندسی گراهام:
در اسرائیل، ما ناراحت هستیم در ایران، جشن گرفته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/133552" target="_blank">📅 22:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133551">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6y67aks9c3ewZLjODzdGH4B-8aLQKt2FlRD1Ojitv1LAQc-oEakib3p1WuOM6nqSDdlyP8d6hATWQW3oooiAktQAXLZBZqUE57jRBtvBpAF5fZsZhT1oregjj2WA7jxqB1RYiYKyvuxdMztLSJzhuU-2Y4JX23RHYwGnISwXqAb2Zeu8lXYHMGzc5asMPDhOVwPqce2ZS44Gg_Cl0Eq1SEWuI2kaY5NAgSzhptEEIdjQBB9M3BqTh5VRFPVjsA2IUsN54Gn41NrBDYdl0s6CXcl0Q5UUJOh5dkKnnVr-o4qu90-Li2_B31d2BLwSIENSFuB6yBOYLgHibLcCt5zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون آموزش: استرس، ترک آزمون، برگه‌های سفید، ناامنی در مناطق جنوبی و احتمال تقلب و لو رفتن سوالات؛ ماحصل روز اول امتحانات نهایی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/133551" target="_blank">📅 22:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133550">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fce8q8uPf_MdWOMWdAsvMhhCCUDCrdjJJNhc5pfVBncXt2-b3u4ycQ1lk3JV0LhG5HP_S5di0t2rzCJ67ufH0EC8VQUxzhaoikHdHDIMZILRQJdW2l-gE7ErWK9SctpNDqiW9-bhATgnmjInAfaPweH9XbfhYS_f5V9jSAB0FtHW5tpkIK3_Gs7OXzYwdk0iAwAsYTau66MsNxHzJqgev32QbAeQSIQEY86fqkfOS2vhwqcbNCcXKSjbvYAOK-epVoXUASSWrU_IhrSxIDfjSrQhWccxNAZILy8Kcn9as72fBOH0SCQIcdDku_TK8rrRuDdItUfMVzVG2Mffi-iPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دومین هواپیمای معراج مخصوص گروه مذاکره کننده ایرانی از مشهد به سمت بغداد درحال پرواز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/133550" target="_blank">📅 22:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133549">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخرید و پشتیبانی</strong></div>
<div class="tg-text">💫
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید.
📣
با توجه به سابقه عملکرد سرویس‌های SafeVPN در زمان
📣
اختلالات و‌قطعی کامل اینترنت بین الملل سرویس های
📣
خریداری شما فعال خاهد بود.
خرید فوری از ربات زیر :
🤖
@SafeVPNXBot
✅</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/133549" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133548">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخرید و پشتیبانی</strong></div>
<div class="tg-text">🚀
تعرفه سرویس تک‌لوکیشن های مختلف Safe VPN
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000 تومان
▫️
۴۰ گیگابایت — 60,000 تومان
▫️
۶۰ گیگابایت — 90,000 تومان
▫️
۸۰ گیگابایت — 120,000 تومان
▫️
۱۰۰ گیگابایت — 150,000 تومان
▫️
۱۵۰ گیگابایت — 210,000 تومان
▫️
۲۰۰ گیگابایت — 300,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 450,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 50,000 تومان
♦️
۵۰ گیگابایت — 80,000 تومان
♦️
۷۰ گیگابایت — 105,000 تومان
♦️
۱۰۰ گیگابایت — 155,000 تومان
♦️
۱۵۰ گیگابایت — 230,000 تومان
♦️
۲۰۰ گیگابایت — 305,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 585,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 160,000 تومان
▫️
۱۰۰ گیگابایت — 200,000 تومان
▫️
۱۵۰ گیگابایت — 300,000 تومان
▫️
۲۰۰ گیگابایت — 400,000 تومان
▫️
۳۰۰ گیگابایت — 600,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 680,000 تومان
⭐️
تعرفه سرویس‌های مولتی لوکیشن SafeVPN
▫️
10 گیگ ➜ 50,000 تومان
▫️
20 گیگ ➜ 100,000 تومان
▫️
30 گیگ➜ 150,000 تومان
▫️
50 گیگ ➜ 250,000 تومان
━━━━━━━━━━━━━━
🤖
ربات خرید
@SafeVPNXBot
✅
📞
پشتیبانی
@safevpn_secureSupport
✅
😍
رضایت مشتریان
@safevpn_feedback
✅</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/133548" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رویترز از حمله پهپادی به اردوگاه کردهای مخالف ایران در سلیمانیه عراق خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/133547" target="_blank">📅 22:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133546">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
خبرگزاری فارس: قطر و عربستان بازوهای حملات هوایی آمریکا به ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/133546" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133545">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/پرواز چندین سوخت رسان آمریکایی بر فراز خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/133545" target="_blank">📅 22:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133544">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نتانیاهو: سناتور گراهام به من توصیه کرده بود به تأسیسات هسته‌ای ایران حمله کنیم
🔴
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در واکنش به مرگ سناتور لیندسی گراهام که امروز درگذشت، اظهار داشت:
🔴
«او به من گفته بود: باید به تأسیسات هسته‌ای ایران حمله کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/133544" target="_blank">📅 22:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133541">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
یک هواپیمای دولتی عمان درحال فرود در فرودگاه بغداد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/133541" target="_blank">📅 22:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133539">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bJM1LjbECUjdo6pGlWj66l7qV13b-6deVeRdiwXcUx6z_HV_mePBTQlyjPe3dedwqja9WuDsqGmU2Ix1-eSjr91gBmg9emjpB5myw6pYNFGGN-2Vt1WsDCCJVELDEgaSaBdkgF_52FVHmhf88lGiGHhi2V5F6_xYTGG6AYFwIekqkBElaOJd6njhO9xfqFX9YhJ2xNmJoW3JslosDVYYJEKHbxUqW8-orRK_8YKoK6hwzF9uuGxF59Yf8AZt_KZgpgLs7YT6Ldh0u6NUfmrCTJ9ytI5SQCovCBNli8otl4Xr3XN5h5bsirZJMVa8XkW1i_b_aUzLu6ySoDky-wGi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای میناب ۱۶۸ متعلق به تیم مذاکره کننده ایرانی (عراقچی و قالیباف) بدون مشخص کردن مبدا و مقصد و همچنین روشن کردن رادارش در نزدیکی مرز ، رو آسمون عراق درحال ورود به بغداد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/133539" target="_blank">📅 21:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133538">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
معاون سیاسی امنیتی و اجتماعی استاندار بوشهر خبر منتشر شده در فضای مجازی، مبنی بر حمله به محدوده تیروگاه اتمی بوشهر را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/133538" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133537">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
واکنش دبیرکل سازمان ملل به درگیری‌ها و حملات سپاه و سنتکام: بسه دیگه خیلی نگرانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/133537" target="_blank">📅 21:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133536">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_eL9x0YHdWYktdcOUGFRNbqwc7ps9Q5haOjt7iimZqt6RM37IMFFVgoCjKl3O5yIKUO16EXhd3dXGh01eyIvFLOXQCtGrrLozvDqdmHDapB64-HD4kIiV5sBu1eBB0Cfi8aBAwVKMYRkxRcstTQfaBbJ2hYK-u4ZRSB2vVeNDtjZuzjCgyQwi_DoDRpaFuHkiVcDCbqE919y_4uE-BG9E2shspTbvisclaVwXxEDOQ4ES8J2lM9YuTu-U7Ye-4H8lk-g59Spaw7KfTmHyhKjCAfPo1urnSR4wVfpVGLnTxnzyJNE3pwOn2iLlCXK1K-kXC3n22Fr5kX5PNYjQ_S6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه فرهیختگان خطاب به رضا پهلوی
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/133536" target="_blank">📅 21:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133535">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUVAf76RRJvXCbfC45-aOlSwL1Hw7aEUumGRxHqJ9nLp6RUzv4GIJ4-RwXi7QO6eICYn1kV55hgn_Mb9VV9_JL9uVjDi2FT_SvjjPIdoiyfy0-mfsNYLilcT4yBaR2Cc3xwix-2hDdpbs-gPHjG49qjVKCOyhtJVMz521w7U2NblmKAqplAiIAd744jUFae7oJmngLIdxDFzILzXZDcazXk-Jd7KyiFHzqByuYZwcY2bgns2dlvkIm5Km8fdj-yn3k2rY9Pwj157OsBAC0w7xs9oOoDT26ubhnXzM36TGu-HGR1S_Br9izMI__1mvl_9zqPa-HeJpmMZrwcbCE-TAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون /وضعیت آسمان پروازی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/133535" target="_blank">📅 21:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133534">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/133534" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133533">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فیصل بن فرحان، وزیر امور خارجه عربستان سعودی، در تماس‌های تلفنی متعدد با همتایان خود در کشورهای قطر، عمان، بحرین و اردن، تحولات اخیر منطقه را بررسی کرد.
🔴
وزرای خارجه این کشورها بر ضرورت تلاش‌های دیپلماتیک برای بازیابی امنیت و کاهش تنش‌های منطقه‌ای تأکید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/133533" target="_blank">📅 21:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133532">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC2BfCelgJwJPS-dndkIx9IhGokb3IZozqJ9xpAfe8pzkw6uBmkfA7CjqoTo6vklaSt_2TWB_SQa3vGQSjJlg-4tEKKO4XFmox8e1zjaqkqKiAsrrZUZGwI2caMQgr6jrud0wRGf2yg0_rqT3JPi5ncgjIGJeXAPkNkS6wNA-k8bumVUawNUUQ4cg8U9tPIIGA-u0dF7ZrnU0lr2Ast_XAYwkPP38AI-lB8nvJykfwH0Ba4FUpGSQHS3KtXTkpEv-F3C9Dk_Zvm1FJBtgBKr1insIv_R_-EFq_zCbGA_EA9c_-sv-jCg0j4w6ZTMAGsuWdeCHRG-jv3qgJM2qutJ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون فعالیت گسترده نیروهای امریکایی در جنوب کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/133532" target="_blank">📅 21:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133531">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
هم اکنون هواپیماهای هشدار اولیه و سوخت‌رسانی هوایی ارتش ایالات متحده از پایگاه‌های مستقر در اسرائیل، عربستان سعودی، امارات متحده عربی و قطر به پرواز درآمده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/133531" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133530">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133530" target="_blank">📅 21:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133529">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
گزارش هایی از صدای انفجار در لارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/133529" target="_blank">📅 21:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133528">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کانال 12 اسرائیل: ایران قصد داشت ترامپ را در جریان سفرش به ترکیه از بین ببرد. اطلاعات خارجی این توطئه را کشف و به مقامات آمریکایی هشدار داد، که منجر به تعویض هواپیمای ترامپ با پرواز برگشت او به واشنگتن شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/133528" target="_blank">📅 21:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133527">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByWRMoCC0D_hKWRjefkvCqW7m449ZCDY5DfuXHgYiyqSuFO0mxUasYOVzVM7dWlFdner62O-yH80qb5jWO8r3rYlN58QYn7-qwtURF31-sLUbpAvjvXJ8LiNZu1tjfNre-WeHkCgVfKrswbmEBhDoWhYuNoodArQIHMGH0NH8dzBuAp702_vD7KIuFvMi8AjnLoGPO6Nfxbee26Ko1Lx5xLBdjWFLmSFx0dejkj-qZzjK_Nl2aULga6yP8kWfTdHOYhccXsfolwGFwAs06fMd5_jaDVyi_-NR9WUIBEOjlZuSqL2bymfblBzBXejNoU5fcSP3uXpjFMUG7fvHqkOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک ناو هواپیمابر نیروی دریایی ایالات متحده که توسط دو ناوشکن کلاس ارلی برک همراهی می‌شود، یک‌بار دیگر در ورودی جنوبی خلیج عمان، در ۳۰۰ کیلومتری جنوب سواحل ایران مشاهده شده است.
🔴
نیروی دریایی ایالات متحده دو ناو هواپیمابر در منطقه دارد و به نظر می‌رسد آن‌ها را نزدیک‌تر به ایران نسبت به (مرحله اول) جنگ مستقر کرده است.
🔴
مکان ناو: ۲۲.۵۱۴۶ شمالی ۶۰.۵۸۷۰ شرقی
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/133527" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133526">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
اکسیوس: لیندسی گراهام ساعتی قبل از مرگ گفت «الان نمی‌توانم بمیرم، هنوز باید ماجرای ایران را حل کنم و تحریم‌های روسیه را پیش ببرم»
🔴
او چند ساعت قبل از مرگ، احساس ناخوشی کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/133526" target="_blank">📅 21:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133525">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l54YR81z9k5iFgOnBAi9xFwnYGSyj3TZ5HOkUGJxzBmwyvsBTW-Wg_eAAk67q8MaJCk7OOFxdJ013uCFMCBS1rOupk71fxWqKAbeaI5qfj9R7XjCFj4sybxKIFJiYB-V8ujJwxjPLNjtmuCD_6mAhbRVYjb_fM5O0wDUrrEKa6U-RKhv_YcIZm5UOiSRDrkDwtGjEC69boGQ0NJa4PAE-d03c8FC7MwWDWNQeQ-lwsMnIZYPxybpKv1ZJXFgYS7bAFKRNBODFVHmelVdp0qkqqVlMTklneR5urerrVoemy_8xwB7JweWp-c6-4B8zJXu6o-Kt4PVZbxoIjgGsNxthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منو غذا در سال ۱۲۷۰ شمسی (۱۳۵ سال پیش)
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/133525" target="_blank">📅 21:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133523">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / وب‌سایت واللا: ارتش اسرائیل همراه با ارتش آمریکا سناریوی پیوستن به حملات علیه ایران را بررسی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/133523" target="_blank">📅 20:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133522">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
انفجار مجدد در قشم و بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/133522" target="_blank">📅 20:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133521">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOEUpHLmTzpJEI_8Womu1LVnvYO74AcSydkS1E6Dy7BJVcNkZ1Q0dr4kIRQ58omMdw6XjuOYLVe1VEmQXh8YeRhtvLsKdiQyCBpP3HCA_dXnpDx55gc9pLzjHk0K2SfLJa4f_On4UexXYEMmIbMX3nqgKIw807x8E79zW9paINszkNlHxyOK5HqWeUH0dqs5OdxWd5ESCrBH4uG2ZbXnI8IgjPbN5Oqns_IAmppVvJiBpOLLXs6NXUxCsg8kh8OQjtvlyad5-gfERgYdgwtceeQSnY58kCo1k9gwtInXXuA-tWjKFsnKaXoPAzMAt-hjGp5AReJBNpdotGbD48DgXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوگین نزدیک به پوتین ادعا می‌کند که موساد سناتور گراهام را ترور کرده و این کار را برای ارسال هشدار به ترامپ انجام داده تا جنگ در ایران ادامه یابد.
🔴
"مرگ ناگهانی گراهام می‌تواند لکه ننگی باشد که به ترامپ فرستاده شده است.
🔴
من شک دارم که ایرانی‌ها این کار را کرده باشند.
🔴
واقع‌بینانه‌ترین حالت این است که کار موساد بوده تا ترامپ را به تجدید جنگ تمام‌عیار با ایران سوق دهد. این به وضوح به این معنی است که "شما نفر بعدی هستید". لیندسی گراهام سایه ترامپ بود"
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/133521" target="_blank">📅 20:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133520">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ee15376941.mp4?token=tp1WPlc1CF2jrJqIpf4spZhhHH8m4b0cgPBTTusZQnmE5Fh2HI5otkOb24saK30DUWy0w-2y0Cv6Ni9pQhzEQ0wf2yIahoMDI1POJ4xYj4okxoZI6TU7iL7yH4nqe-siNJh-CqgulfxTxYlGd7hJP0MVSFwE2CvFSZHKp14LWOvZVrxIsB1Dy4klJpZhDMmuJGAVE7Qpm91eKWkPmFs8L_eUTR6gTuTPpQ8TYrN1K9gMXMSJtK-xgvF2GvEYn42s26X9KPtbMKKLbGbQVqIihILUFIuVIrU5Qtq9KqETSs6kfgUDO0Ti40npBKxfz6-HTrtZy42ef4vMUZUULzzipg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ee15376941.mp4?token=tp1WPlc1CF2jrJqIpf4spZhhHH8m4b0cgPBTTusZQnmE5Fh2HI5otkOb24saK30DUWy0w-2y0Cv6Ni9pQhzEQ0wf2yIahoMDI1POJ4xYj4okxoZI6TU7iL7yH4nqe-siNJh-CqgulfxTxYlGd7hJP0MVSFwE2CvFSZHKp14LWOvZVrxIsB1Dy4klJpZhDMmuJGAVE7Qpm91eKWkPmFs8L_eUTR6gTuTPpQ8TYrN1K9gMXMSJtK-xgvF2GvEYn42s26X9KPtbMKKLbGbQVqIihILUFIuVIrU5Qtq9KqETSs6kfgUDO0Ti40npBKxfz6-HTrtZy42ef4vMUZUULzzipg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله دیروز از سوی ایالات متحده، تقریباً به نیروگاه هسته‌ای بوشهر، واقع در سواحل جنوب ایران، آسیب وارد می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/133520" target="_blank">📅 20:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63fb7b34c.mp4?token=oODwerBE2F8C2RebeJufPYxFAf8IBTTzf-OOKBast1IRrs2fLrJnbYz5-VmL5JRqpG-HvBBn2M7xA-fZ0kRmTLHL8QRLaQ4iBpbrL5kCphT_hXcBBhLffO1UNlXm3qxNDzsSC4A3k843jmmEfbgl7Q9ojY48reL-5fF3vXYecKULC60KRErQwbF1Fk8draJXMlfDDSmNLyi_0oLWaxTr6PDTKCvruqeM2pnxA6kvSLxQ_IEnIFgDSBWjRTJsc2oAXJMVUos6heRKPTiNxz7_xeaLz8LDDg5JCCkvvrnmXhnORkfbLg4hxnrextd8HQ3gP3DQR85DtSg3YXpfrvHylUMv2Lryf1HkqfdpQjUdO7H8UCpN-n0qI4XHLyYwty3nGlnPHayECsxctYTS44qialUK3_Zp8Q3t6cCHXwQvBl9Bf-VrvErO-Ja0tTS4NRl9vX4n89NE4aXSziIKc-eimsq79SH88xoYdq1VizzGL4ffPKYm-naqy2RoS2f7j1gE2q1s8bUjf8TpUEEi4ILf17Ny6hGq2K2u2J9PSmQcdtO1m-mZIZpzfQ9B_Zofs357R18U6PhrJ3a80RXx_DZm-ebsX2oBUYfgLJFYLAI6fMar3ScvWSkRZZKxqqHKADDnPmicyiGTr8w7YnWIb45aBKj6bJlWH-z42FsSveYlW4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63fb7b34c.mp4?token=oODwerBE2F8C2RebeJufPYxFAf8IBTTzf-OOKBast1IRrs2fLrJnbYz5-VmL5JRqpG-HvBBn2M7xA-fZ0kRmTLHL8QRLaQ4iBpbrL5kCphT_hXcBBhLffO1UNlXm3qxNDzsSC4A3k843jmmEfbgl7Q9ojY48reL-5fF3vXYecKULC60KRErQwbF1Fk8draJXMlfDDSmNLyi_0oLWaxTr6PDTKCvruqeM2pnxA6kvSLxQ_IEnIFgDSBWjRTJsc2oAXJMVUos6heRKPTiNxz7_xeaLz8LDDg5JCCkvvrnmXhnORkfbLg4hxnrextd8HQ3gP3DQR85DtSg3YXpfrvHylUMv2Lryf1HkqfdpQjUdO7H8UCpN-n0qI4XHLyYwty3nGlnPHayECsxctYTS44qialUK3_Zp8Q3t6cCHXwQvBl9Bf-VrvErO-Ja0tTS4NRl9vX4n89NE4aXSziIKc-eimsq79SH88xoYdq1VizzGL4ffPKYm-naqy2RoS2f7j1gE2q1s8bUjf8TpUEEi4ILf17Ny6hGq2K2u2J9PSmQcdtO1m-mZIZpzfQ9B_Zofs357R18U6PhrJ3a80RXx_DZm-ebsX2oBUYfgLJFYLAI6fMar3ScvWSkRZZKxqqHKADDnPmicyiGTr8w7YnWIb45aBKj6bJlWH-z42FsSveYlW4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی خضریان، عضو کمیسیون امنیت ملی مجلس: مسئولان دستگاه دیپلماسی ایران در دنیای موازی زندگی می‌کنند/ آمریکا و ترامپ می‌گویند که ما از توافق‌نامه خارج شده‌ایم و آتش‌بس تمام شده است بعد مذاکره‌‌کنندگان ایرانی می‌گویند فلان اقدام دشمن نقض آتش‌بس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133519" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
تصاویر بیشتر  از جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/133518" target="_blank">📅 20:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/COCEvyNrlcyRKdRExGj6dVVFeUdks3-BOSGLRB-XAY-9JKW6Qk2bdNU78PFekyG-ukVjxWT_SNPbrknNEZrtLq-9g2ZsndIJL0EQUZLGXOphXymiw39qKWCjRKSTS56ZI584Lzs0gE84kMRUaxqUVDcQB1FjNWiCA3BNIzdUisLk0bgORb7vsD8HysLx04r7RpMYaPE_qL_PHLiyhID0oWqcW5Hg380zzoKvNGBbk8PmZ8OrP9PTHjVIlIYDPpfIoUnzwyz4hhugTlHigwmk-J1wRke5c_uts0AgYx7MRGMEzBKVFXqBjRtpo1zcMvoCdRa6S7e0tuj1hPuACXdfMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ دستور داد که تمام پرچم‌های ایالات متحده در سراسر کشور به مدت شش روز آینده، به احترام لیندسی گراهام، نیمه برافراشته بمانند: به پاس زندگی و دستاوردهای برجسته سناتور لیندسی گراهام، دوست گرامی من و مردی بزرگ که دستاوردهای فراوانی برای کشورمان و ایالت دوست‌داشتنی کارولینای جنوبی به دست آورد، دستور می‌دهم که تمام پرچم‌های آمریکایی در سراسر ایالات متحده تا روز شنبه، ساعت ۶ بعد از ظهر، به حالت نیمه برافراشته درآیند. خداوند شما را حفظ کند، لیندسی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133517" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نتانیاهو در حال حاضر در یک جلسه امنیتی با مقامات ارشد دستگاه‌های امنیتی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133516" target="_blank">📅 20:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
گزارشاتی از شنیده شدن صدای انفجار مجدد در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/133515" target="_blank">📅 20:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/گزارشات از آماده باش جنگی تمام یگان‌های سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/133514" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
اف بی‌آی پرونده درگذشت لیندسی گراهام را بررسی می‌کند/ تا کنون علت رسمی مرگ گراهام تایید نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133513" target="_blank">📅 20:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133512">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
۴ صدای انفجار در روستای مسن قشم تایید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133512" target="_blank">📅 20:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): طی دو ماه گذشته ۸۰ نفر از اعضای حزب الله و ۲۰۰ زیرساخت مرتبط با این گروه رو نابود کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/133509" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوووری/ترامپ: امشب جهنم بپا خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/133508" target="_blank">📅 20:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133507">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ارتش کویت اعلام کرد سه مرکز مرزی این کشور هدف حمله قرار گرفته‌اند که در نتیجه آن خسارت‌های مادی وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133507" target="_blank">📅 20:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فرماندار قشم : اصابت ۱۰ تا ۱۱ پرتابه (موشک) از عصر امروز یکشنبه، تو جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133506" target="_blank">📅 20:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوووری/ فارس: برخی منابع از کشته شدن ۳ آمریکایی در حملات ایران به کویت خبر دادند
🔴
وال استریت ژورنال یک ماه پیش در خبری مدعی شد: در صورت کشته شدن سربازان آمریکایی ترامپ پایان کامل آتش‌بس با ایران را بررسی خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/133505" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی مدعی شد: ارتش آمریکا ساعتی پیش حملاتی را علیه سامانه‌های موشکی، پدافند هوایی و قایق‌های کوچک متعلق به سپاه پاسداران در دو نقطه نزدیک تنگه هرمز انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133504" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نهاد فرودگاه‌های پاکستان از فرود اضطراری یک فروند هواپیمای امارات در این کشور خبر داد.
🔴
یک فروند هواپیمای باری بوئینگ ۷۷۷ متعلق به شرکت  «امارات اسکای‌کارگو» که از اوساکا به مقصد دبی در حال پرواز بود، امروز پس از آنکه خدمه از بروز یک مشکل فنی در حین پرواز مربوط به یکی از موتورهای هواپیما خبر دادند، مسیر خود را تغییر داد و در کراچی فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/133503" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9iPSW1jdr7SToqO1-wDD1IC1riJB6eSeCLBq3XbaQbhwIdIVKD3wc_VtvafnfIguqCSzDPqiOkuizSMvVbfsV1v9NXz7Yk-hjhgTgJfFUw6niXY68G5F0PWoju_n5enqKlph9EvtFm03nF746aXaIuHFVoJkw-9wMb6ZK55pyegXOQFrZOchRUzSttd-F1R_MDlcIiFJKPwTl-WlymmXUG7bVd-X9bNc0j3cBbsyFz3jHNnybclB5We1u7t187bz02bq4WsIUotprP3DrGPd_QlxDTRwi6UchHZvKbI6Yi6az1xyyzQmR-_2Q0K2TTEyX5HKdqxgnXHnXe7Kx9n2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر بیشتر  از جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133502" target="_blank">📅 20:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری / منابع امنیتی به نیویورک تایمز.
🔴
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133501" target="_blank">📅 19:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKeVhMDwrCBWdLYl11afl6K0T7TFnMGX0JmcNqcw1d6Ng2-74rPt6V1iKxb4FQv1td_TTBQCtHARa4K3hu-7m3GPYExxAzCdhq5RqwBIwIvpT_WdMATKMA7wGOmLMipkzwBt0CS0PxP7PbXnnt9LVRWmlFOAmA96-JjaQJT2dumk3Z7Xd9op1JmulxHY7ND2gV2nnZTBum3-GnRKLty6z88UoKgE3d5916jI02Eu86_Ub44O7h9JAOdhbBk5VW4IvrFZO_X0_hI9EiuslPnrJ6Oh6QglpwX8BbCzGkVGrKOxJFfBD0r6M76aWfVuAQKSaziHNSciE7D5Cf1Uj90eBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از آتش سوزی در جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133500" target="_blank">📅 19:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ایالات متحده حملات تلافی‌جویانه‌ای را در پاسخ به حملات ایران به کشتی‌ها آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/133499" target="_blank">📅 19:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری / گزارش‌هایی در برخی رسانه‌های منطقه‌ای از درگیری در دریا بین نیروی دریایی ایران و کشتی‌های جنگی آمریکا منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133498" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ca9785e0.mp4?token=lzibSJQpSBSuwdBe4nJ99J3eylPIVL3vbOpvNQW3tWVochHSoJ2CwJ0F9V6kdhtg-npugPbn1d57NMUgMASyxOtpm7ASXwwB4I_cRpq0l6VVCn9eu_xRF_Vxt9AxRyv6WVptC18GXsTJ7rGRuF5bn_Dr0vxFS6hBlo0MgktHS5txX47qtpCGRHHuahwOR2zExJs9aT6LUFXpRb9POWUZ4ex7K28QfJLmzHpFWkzwQCPQT4e6pHbuY82Y_v_wZ4f8QtdpHRlWCIF6NyFO1F43xjY8oKFDCo3kniz7uNNU1M5hJmcOtKyp2xYFz8oxMJrdQvovdc9ZZAxOHjanL5CtOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ca9785e0.mp4?token=lzibSJQpSBSuwdBe4nJ99J3eylPIVL3vbOpvNQW3tWVochHSoJ2CwJ0F9V6kdhtg-npugPbn1d57NMUgMASyxOtpm7ASXwwB4I_cRpq0l6VVCn9eu_xRF_Vxt9AxRyv6WVptC18GXsTJ7rGRuF5bn_Dr0vxFS6hBlo0MgktHS5txX47qtpCGRHHuahwOR2zExJs9aT6LUFXpRb9POWUZ4ex7K28QfJLmzHpFWkzwQCPQT4e6pHbuY82Y_v_wZ4f8QtdpHRlWCIF6NyFO1F43xjY8oKFDCo3kniz7uNNU1M5hJmcOtKyp2xYFz8oxMJrdQvovdc9ZZAxOHjanL5CtOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از مِسن استان هرمزگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133497" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری/صدای انفجارهای مهیبی از تنگه هرمز به گوش می‌رسد.
🔴
گزارشاتی از درگیری بین نیروی دریایی ایران و ناوهای جنگی آمریکایی مخابره میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/133496" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / صدای دو انفجار در جزیره قشم و بندرعباس، ، شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133495" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری / هم اکنون سفیر آمریکا در سازمان ملل: تهران به یادداشت تفاهم نامه با آمریکا پایبند نیست، همه گزینه ها اکنون روی میز قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/133494" target="_blank">📅 19:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
عراقچی: ایران از تمامیت ارضی و حاکمیت ملی لبنان قاطعانه حمایت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/133493" target="_blank">📅 19:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / منابع خبری از شلیک ۳ موشک بالستیک به سمت منطقه المینا در کویت و محل شلیک موشک‌های آمریکایی ATCAM خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/133492" target="_blank">📅 18:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6a433de38.mp4?token=UQ99txvR2IVifbcKhQOPwN3kR1REwUd7ma0-eWodaYn4uCmn9vjuWsO8uVsfxmMchh7z4TbBQddB7LPeE2YRRhe_HcqbcGrxyc80DgWje6_svYldLMPn4F1ruSXeOcMke3bCvd8zOgw5YP8tQbib_hlD35D8NxAf9vyuBbGZUn2_YYOOThfzPDsWxnfscyqcNY-4ZiTpA5GdZWeh1w1tpsvrxKwp8l2otRE7XD2w2DURHK8-FghuhHCZ9txu1kDTr75ZYDoSj26N_M69grJAWSWWBGGSxBBluswBInfNgpDGZy_DTPbMLEgN3cZWmEz4YCzJJY9EUPrNd_0Q54Kx2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6a433de38.mp4?token=UQ99txvR2IVifbcKhQOPwN3kR1REwUd7ma0-eWodaYn4uCmn9vjuWsO8uVsfxmMchh7z4TbBQddB7LPeE2YRRhe_HcqbcGrxyc80DgWje6_svYldLMPn4F1ruSXeOcMke3bCvd8zOgw5YP8tQbib_hlD35D8NxAf9vyuBbGZUn2_YYOOThfzPDsWxnfscyqcNY-4ZiTpA5GdZWeh1w1tpsvrxKwp8l2otRE7XD2w2DURHK8-FghuhHCZ9txu1kDTr75ZYDoSj26N_M69grJAWSWWBGGSxBBluswBInfNgpDGZy_DTPbMLEgN3cZWmEz4YCzJJY9EUPrNd_0Q54Kx2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انبار در مقر فرماندهی ناوگان پنجم نیروی دریایی ایالات متحده در بحرین نیز شب گذشته مستقیماً مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/133491" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری / منابع خبری از شلیک ۳ موشک بالستیک به سمت منطقه المینا در کویت و محل شلیک موشک‌های آمریکایی ATCAM خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/133490" target="_blank">📅 18:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / منابع خبری از شلیک ۳ موشک بالستیک به سمت منطقه المینا در کویت و محل شلیک موشک‌های آمریکایی ATCAM خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/133489" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133487">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14311630a.mp4?token=eLrni_6JJOxZzf2Q9il9Kc1VAPkIWi0KA3T8OYe_M8vINU4YZ53ixA9CM_2aHg_jrH7HUy5l56LQrItD-nuP5KcaCjsEWic-l-ZOnZZ3b5n8beiHQfs1rWqNdrjdnRpxMurBt-ID2cKUhK3cpjEkAZnqtr8Gq3UUjUYVzA5VTa0QfEZ61Ia8mGlBub5lCqdgVBbaMGIyUeOeCV3gl-HAsxPbJE-swI0vxakw0tfjfzaMpA-6H9UZkakSi0OkK9W5_calfil2toz_7A3NbaAzfhuXcjU_BPTe3RlIwhjYqp3KyJUiCNfTFbIsBi8l1wg9nXEn1BGfThzPswd6iB4PzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14311630a.mp4?token=eLrni_6JJOxZzf2Q9il9Kc1VAPkIWi0KA3T8OYe_M8vINU4YZ53ixA9CM_2aHg_jrH7HUy5l56LQrItD-nuP5KcaCjsEWic-l-ZOnZZ3b5n8beiHQfs1rWqNdrjdnRpxMurBt-ID2cKUhK3cpjEkAZnqtr8Gq3UUjUYVzA5VTa0QfEZ61Ia8mGlBub5lCqdgVBbaMGIyUeOeCV3gl-HAsxPbJE-swI0vxakw0tfjfzaMpA-6H9UZkakSi0OkK9W5_calfil2toz_7A3NbaAzfhuXcjU_BPTe3RlIwhjYqp3KyJUiCNfTFbIsBi8l1wg9nXEn1BGfThzPswd6iB4PzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی گسترده در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/133487" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133486">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbpQOS0b_OI-pEa8OZuYW3xted4-WyfkgrBI8xYm0vjGckwIuZMk3ADYQsQ5qMACnEAgBOQI4cdH56XmfdMWlh4gmVDIHb6VXMIPvEmA4Che1G6eNIbWnxzyv6fSQjY2ECyofPieDmB9skWQNjTm_PFafnrD2gCkKkeJuQrkCNP9xpEnlxNndlcVvT2Szfa5Cgrc6NjJmtTaMsnUoxfPigg5CtPdTOqfWOiRtmeJAmib2mHNKh7Fyt4jmu3qSkeefDdjFHkONhV9PLfDJdz39o25Sex08l1DmRuZOm7gmn4jauoVKCBaSynFc9jftOXtbh09aQ87KgLOYRzyzm5RHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون‌های غلیظ دود در مرزهای مشترک عراق و کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/133486" target="_blank">📅 18:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133485">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
المانیتور به نقل از منابع اسرائیلی:
راهبرد محتمل اسرائیل، دور ماندن از درگیری ایران و آمریکا همزمان با فشار به واشنگتن برای تشدید تحریم‌ها و مقاومت در برابر خواسته‌های تهران
🔴
سناریوی مطلوب و کم‌ریسک تل‌آویو، بازگشت محاصره دریایی است که «بسیار بهتر از یک توافق بد با ایران یا یک جنگ کم‌شدت است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133485" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133484">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn56oozZhKcAZz3rncm_NjlvUFDmvJ6IXLRttOOFiHFKSRzlKHnlBlluvQNd7jLkE48kt8hpnKHSt9XOn2c3Razyv3qrM6WZ_OwEHs_r8D1kw28QHEdd5_rKOZ1VvI2DhmemBR2sE5WHdFpup7rnfAcsG6NC0XHBrAkeoGK1hueCVDB2Ykd0Xo965ONc0uql1sy4e4iIaj7fDz_Kxzau107Z8rZJdgR8Z98TmqBIh5f8Z7UwjOhwDH7a9WZJ49vsqWIB5kJJWtXt8BZ2JiK7tBj3ZuwHAIAYL4z9uqsAUKg9JttAjAX6WbDDwudjwRguW1bjn_AKqW4hdy9nxLFuAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره ای از پایگاه هوایی العدید در قطر که دست کم محل اصابت یک پرتابه ایرانی در آن دیده می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133484" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133483">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رسانه i24: انتخابات اسرائیل در تاریخ ۲۷ اکتبر [ ۵ آبان ] برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133483" target="_blank">📅 18:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133482">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/365f150fdc.mp4?token=je7HCFd9OGph-7wEd9bkSy5089TWy23Opnqw5kEehu5dnewXVPozFCau8-A0JuPMihJer9Cwj9w_Pqa_9p7Nbp6i-bIH3Tsn5DuNcNa0hh7iylwiRFdNyNafiLfzCjrrDIhTCqkmssMYWnCzQAIzBzXddpbIvyQt3Vl9L-ZLzXWzeD0S1boMQc29_CSzD92HU3CwsWTXQQLK65BVESzKtwLHOj4f6WdEfnATG4KA570snUOxH3qTcbN7mM1xFaZoYyAP65bpxnbuieI2RxwEIluPCPMGiLsTs4QFXJj4dw0ZqgMRMowfQLxpxkjIi5GlL09T_z62c7Cx5sFUy-bxxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/365f150fdc.mp4?token=je7HCFd9OGph-7wEd9bkSy5089TWy23Opnqw5kEehu5dnewXVPozFCau8-A0JuPMihJer9Cwj9w_Pqa_9p7Nbp6i-bIH3Tsn5DuNcNa0hh7iylwiRFdNyNafiLfzCjrrDIhTCqkmssMYWnCzQAIzBzXddpbIvyQt3Vl9L-ZLzXWzeD0S1boMQc29_CSzD92HU3CwsWTXQQLK65BVESzKtwLHOj4f6WdEfnATG4KA570snUOxH3qTcbN7mM1xFaZoYyAP65bpxnbuieI2RxwEIluPCPMGiLsTs4QFXJj4dw0ZqgMRMowfQLxpxkjIi5GlL09T_z62c7Cx5sFUy-bxxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: فکر می‌کردم لیندزی قراره تا ابد زنده بمونه! بهش گفتم: "لیندزی، تو که جاودانه‌ای!"
🔴
و قرار بود یه پیروزی بزرگ به دست بیاره؛ همه پیش‌بینی‌ها هم نشون می‌داد با اختلاف زیادی برنده می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133482" target="_blank">📅 18:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133481">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_coqMGP__PV_d_PnemwOjPB6KabCOQilNsFVVS-rWmseVNZz3TyM9a047BgDZftSFmeE4S5K_aMsDbvN6wltsJyJmLqW-61Lzz_d_geDdsICd98gXHauI7OqOz460AhhWkLScBtpSunbLIqaeHd54_ISfSO7VhYP8gUmDI0Gjqr1_tWF0tFgM4oDeRMOo3cx1VCJh3pjbiNDdm9lKXpgDETZp7KnUPmeEOR8ewa8g2QJ5WIMCr-gDc9kLoyB3X97K6W5EFsP9Bt_yN8jj9Ri6HGGVh-LtAxRzZzHCoJXEjZshqeQ4It75gN3smEnA_8Wxp1n7aLTN0lLH5E8movHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حمله گسترده پهپادی اوکراین به سمت روسیه.
🔴
بیشتر این حملات در حال حرکت به سمت مسکو، دریای آزوف و شبه جزیره کریمه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/133481" target="_blank">📅 18:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133480">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664dc8a38e.mp4?token=hGxcpduSbdd8fpmQd1vvSa715doaXaRUgPFQWItvxeVEDulRs9s7HsYp8ET09g_v5GlA9EtZDGwi654nm6wKkBVZm9JHWDuhAcKvRNkZZ3FGHGxIfyGx1HLreDQlAmdRtEat73ROOlIo0G6xmR1ByLylePgg6fWvSOEhw-BcS-P3tiXxXJEzz8EaHltJ7xgt7WxviKG0bQo_FfNDAQuhf3F6Piv1QBq7kCgg2c_5dnb6JJJRwtkrzJB-67lQD07GkwB4_bWZBCP8tEIYnzetNpPmuIHtG7EGoor-BRlMol55G7ASzGL1oyWGqklxlKua8rTdSkF330GssNJL95c0KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664dc8a38e.mp4?token=hGxcpduSbdd8fpmQd1vvSa715doaXaRUgPFQWItvxeVEDulRs9s7HsYp8ET09g_v5GlA9EtZDGwi654nm6wKkBVZm9JHWDuhAcKvRNkZZ3FGHGxIfyGx1HLreDQlAmdRtEat73ROOlIo0G6xmR1ByLylePgg6fWvSOEhw-BcS-P3tiXxXJEzz8EaHltJ7xgt7WxviKG0bQo_FfNDAQuhf3F6Piv1QBq7kCgg2c_5dnb6JJJRwtkrzJB-67lQD07GkwB4_bWZBCP8tEIYnzetNpPmuIHtG7EGoor-BRlMol55G7ASzGL1oyWGqklxlKua8rTdSkF330GssNJL95c0KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع امشب تندروها بخاطر مرگ گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133480" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133479">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
لهستان خواستار دریافت 10 هزار زلوتی در سال از آلمان برای هر قربانی رژیم نازی است.
🔴
در نتیجه تجاوز و اشغال آلمان، حدود 6 میلیون لهستانی جان خود را از دست دادند. بنابراین، درخواست لهستان معادل 13.8 میلیارد یورو در سال است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/133479" target="_blank">📅 18:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133478">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
علی خضریان، عضو کمیسیون امنیت ملی مجلس:
جمهوری اسلامی ایران چه با عمان و چه بدون عمان تنگه هرمز را مدیریت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/133478" target="_blank">📅 18:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133477">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزارت خارجه پاکستان:
پاکستان تحولات اخیر را که
تنش‌های منطقه‌ای را بیش از پیش تشدید می‌کند
، با نگرانی عمیق پیگیری می‌کند.
🔴
پاکستان مجدداً بر حمایت قوی خود از حاکمیت و تمامیت ارضی تمام کشورهای برادر در منطقه تأکید می‌کند و از همه طرف‌ها می‌خواهد که خویشتنداری پیشه کنند،
گام‌های فوری برای کاهش تنش بردارند و تعهدات خود را بر اساس تفاهم‌نامه اسلام‌آباد (mou) حفظ نمایند.
🔴
پاکستان از سوی خود متعهد می‌ماند که از طریق گفت‌وگو و دیپلماسی، همه گونه حمایت را برای دستیابی به صلح و ثبات پایدار در منطقه فراهم آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133477" target="_blank">📅 18:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133476">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: رهبران ایران دیوانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133476" target="_blank">📅 18:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133475">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=sGlLYleMRScAuLFgx-LkaJd8mIz8j6J-1560zLayTutr7iRl8gl_8aZ9M3drxEpwu3cN4OWXP40lttv2PzRtcRUfxB8M1mMLp5CpWWFPw7nTOKRHD0tKoNJKyS2Iwj2QmW3xV8HPP3McJTe71l1rRBaiJje27OWd7CapuPtACGfZyrqKAH1jnUTI1_KXKF0LOrjPn8UQQC51C7fMO51kU1P_U3O3ZklGHspuarVbSNcoPW6ZQAvieK9K9CQCppYiMzrljXhccR6JIMPdHu1KvhZIy0B90E8cU_6KkKs8Kz2mQoak0TjGav9tkiSWUbeAZbvhMLvFuTLNl0EWh-VaNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=sGlLYleMRScAuLFgx-LkaJd8mIz8j6J-1560zLayTutr7iRl8gl_8aZ9M3drxEpwu3cN4OWXP40lttv2PzRtcRUfxB8M1mMLp5CpWWFPw7nTOKRHD0tKoNJKyS2Iwj2QmW3xV8HPP3McJTe71l1rRBaiJje27OWd7CapuPtACGfZyrqKAH1jnUTI1_KXKF0LOrjPn8UQQC51C7fMO51kU1P_U3O3ZklGHspuarVbSNcoPW6ZQAvieK9K9CQCppYiMzrljXhccR6JIMPdHu1KvhZIy0B90E8cU_6KkKs8Kz2mQoak0TjGav9tkiSWUbeAZbvhMLvFuTLNl0EWh-VaNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :
چند دقیقه قبل اینکه لیندسی گراهام فوت بشه، باهاش تلفنی حرف زدم؛ حالش خوب و فقط یه خرده احساس خستگی می‌کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/133475" target="_blank">📅 17:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133474">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ad100662.mp4?token=ednjB5BKPbectra4U9GL1y-PugoOuPxXbVAMEjaTdVncJaOoat-6kQY65_7JEO7amK1nrieJuWoNybxvqq8mY32l1bVUszV6kS1Rz6oWarGLuFTntO7RWb0RDXoide9W77NPS7R88Hsqz30ePqJU3XuPjsBKDb1hNwHWzbj9UMI1T-WPbwF39kPxjUnaiI9M-bD4tkCrP-UaDjfO4JA-OsORdN8q5XYWg8SaSWvvjqYsJ6JWyOJdX4CfOmUkklbX0uhNh1_otF-Qau2qlMip5Ysw_B0YEkqV5aGOPOJU9_GCNv1UTha_dKza5qpSb0e1L1Aw8SorKV2rUzps4vv6tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ad100662.mp4?token=ednjB5BKPbectra4U9GL1y-PugoOuPxXbVAMEjaTdVncJaOoat-6kQY65_7JEO7amK1nrieJuWoNybxvqq8mY32l1bVUszV6kS1Rz6oWarGLuFTntO7RWb0RDXoide9W77NPS7R88Hsqz30ePqJU3XuPjsBKDb1hNwHWzbj9UMI1T-WPbwF39kPxjUnaiI9M-bD4tkCrP-UaDjfO4JA-OsORdN8q5XYWg8SaSWvvjqYsJ6JWyOJdX4CfOmUkklbX0uhNh1_otF-Qau2qlMip5Ysw_B0YEkqV5aGOPOJU9_GCNv1UTha_dKza5qpSb0e1L1Aw8SorKV2rUzps4vv6tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ برای ادای احترام به لیندسی گراهام، دستور داد تا پرچم آمریکا در کاخ سفید به حالت نیمه افراشته در بیاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/133474" target="_blank">📅 17:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133473">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/321fd5e5da.mp4?token=II3evLHEz0K6yfAjeyhpIv3NR1VXBNOh4X-UONurIJENHozaYDAlwUXty_voeYXGVLNbaVvr5oA1YqkGClLdYFxZtZxlz4Vmv8p6-ubh_h6nF8ejmcANEEeCWgLXILFD0DemPqMi-mPOCvx3401rv9R8D93EG8GO6KnAnfyqyxjeSi6z-b4XNyuGX6IIUuGvbPxwjE3ogATVvOQn9zFrzmBitPf2essmWAYScET2auJBMq_-lraWBtWpym37naLbsFSM9yvJ5GG6Hxfdn4OW1jm1wXORhg9rrZcyKCsGDgm6G4jAyqIJGpNab0raqbf3xS_BEkjfh9J8Cw5P0JhrFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/321fd5e5da.mp4?token=II3evLHEz0K6yfAjeyhpIv3NR1VXBNOh4X-UONurIJENHozaYDAlwUXty_voeYXGVLNbaVvr5oA1YqkGClLdYFxZtZxlz4Vmv8p6-ubh_h6nF8ejmcANEEeCWgLXILFD0DemPqMi-mPOCvx3401rv9R8D93EG8GO6KnAnfyqyxjeSi6z-b4XNyuGX6IIUuGvbPxwjE3ogATVvOQn9zFrzmBitPf2essmWAYScET2auJBMq_-lraWBtWpym37naLbsFSM9yvJ5GG6Hxfdn4OW1jm1wXORhg9rrZcyKCsGDgm6G4jAyqIJGpNab0raqbf3xS_BEkjfh9J8Cw5P0JhrFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره
جانشینش :
- یه نفر رو تو ذهنم دارم که فکر می‌کنم گزینه خیلی خوبی باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/133473" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133472">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز باز است. ما حملات شدیدی علیه ایران انجام دادیم.
🔴
ما دیروز با ایرانی‌ها به توافق رسیده بودیم و آن‌ها از همه چیز گذشتند، اما ناگهان دو ساعت بعد، با یک پهپاد به یک کشتی حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/133472" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133471">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: تنگه کاملا بازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133471" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133470">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9TuPQN8kcQCoXG2VEV2sc5SlDGkO3O8RWqOdo4GJFeLGCBQQ8eP75PeUJdGkUEfBsBGLslqVbtvbEutvaadbTyeixZLZQWiMSx3Zm9rczgQAHBXL-_3JbduAij93dcc5ySB3xB_V353GFSt-Zq1ZRCJyIKzL6XIKQsVmsqIzrY-yUCfhpPxJf6IL1uZ5_TY9utaV2QKHBOLFr0mpI5E92kE8KxWu21Rsfuxdi1yDBK4pj5u6h2n3qGIrPNqxOQcpGsl2WOGJoAP0o6eJv3VUUAacc85MPS6MSfcLclTZ_h0gvux7r07YQanhBuS38bxrmDiDE54DaLwFSYoolaV6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به هوش مصنوعی گفتم یه تصویر از تندروهای ایرانی بده که اینو داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/133470" target="_blank">📅 16:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133468">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GYz2zQqrp-srAMSxsuZnmMbNkIu-fnEPXTYFj-rG-vcwT1b2pbip-DrF5GogjA70g7Dw7ZJJx45HKrGSd52Xcw6uQuCwjuYbB1wPCepWJpBMRgbcb9s_29nIJ5WZTgIvhcXiNU4vV2nMKYkCzJuU7ldXqgtcbcxU4SZFEry5wzaaMpJqFAGlslH2sWkcepnw78YN2UzXpXt2w84ThOyKyBGqd-iUm6er79DeHmuAJ7B2GTB_t8yhOATuPBeLpJU88x9DREgZx3vZEybyYzolCvd0N723QVMNw2hSXak-Q8P9LpVpB95SAs2MI2yi6OrclvQjC0q3bfQQczB53l6vSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUg47NzNCQFnX9gpjoAC8JwhvhjSXI4d-W4GfZ7xs2JaitVJfetMA-rAUVhb-jEFrBrcpj2kPLYr-UK5IdTnbx_Z5kTgqM-10iPLcDMxvlDuSrF57OOZCfDQHuW6Ca78bjoT9W6K7L4kdG_a2LmTLJUaV42KIWwVR6aMgZVIOpCw_HpuBu8yLsKbFLRCTJt-YzH98QWd3WapxmDvMn-xfWsurbLQPTNbxwFJRfehQv0r06dd5kr35sqDwxvn2C2CKpO1LmsQQzJsfvunpggftGpz0NaVefUcjI9cbzme0pZVzZYtUg1S8Tl35G4HGFp30eh4ioo2TbPwhpN9jqrbxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فراخوان و لشگرکشی پایداری‌ها(ملت معکوس) برای محاکمه قالیباف و پزشکیان و اعضای شعام
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/133468" target="_blank">📅 16:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133467">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4n8w_xfC2XKij6LBnykxbB-h0BoKqYZ5fpJAaCaP_OElQk-E0PMEYUnDn-zHq_0vxC1v7Kw83u1mmWMXVsVI4ChYEibrHn0z71m5bStk_1lycl0ZAOtWjzyDH4h8wzy8Kqdw-eCuJntIuN2Yj8yHO4mrWsCFkSzfnL9VPaVstmw4wir1G6apf2HbDNCZMp8yeRESm7SuN9GQEw-eLWmpI7TprFZt1o5G6yJOhyFlMAa0zkEaMelrKdC7CxOshMPk8R-AboxqCPq4DU4Lp4E6VFqvvVM3270LWTmLoNdvxsH0Ypne2-kF8NAaiNNmZ64aINUT7UWuoOGMZnfHJgyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان مدیریت مسیر آبی خلیج فارس:
به دلیل تحرکات غیرقانونی اخیر نیروهای نظامی آمریکایی در منطقه، عبور از تنگه هرمز در حال حاضر امکان‌پذیر نیست.
🔴
به محض بازگشت ثبات و آرامش، تمامی درخواست‌ها مطابق با برنامه زمانی بررسی خواهند شد و مجوزهای لازم صادر خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/133467" target="_blank">📅 16:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133466">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=VDQpXbc5KmPZ3EpqJBgKgnTW7wvKWihz15cw1Fz9yrg6VxOVrHlkXMuqirjDkdOZlvBE1nhcjWcH1g1iBDrIi8c5C1zznJ2mSF8opYC0HfBsITvFWYpzazipuHMvXezpzQo87mxcdN2lWmj0l56H40jGyZZy0huMzh_Vn77XDAryMHusq0HbyGhcOJlKBJBXsSQSaX1JtgNmXdKDAuEPHwDtY5nIHKCsrl5dQoPENd6p1LOt8X_O67twM25UqhcVWe48m_vZrSs5AEwXOHHS5pvH4nMUfqL1Dly0JR__oBv5zvMfhhpfhr1wsq-WmxDvL1KLdSj_rw1BWCoBgPrPNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=VDQpXbc5KmPZ3EpqJBgKgnTW7wvKWihz15cw1Fz9yrg6VxOVrHlkXMuqirjDkdOZlvBE1nhcjWcH1g1iBDrIi8c5C1zznJ2mSF8opYC0HfBsITvFWYpzazipuHMvXezpzQo87mxcdN2lWmj0l56H40jGyZZy0huMzh_Vn77XDAryMHusq0HbyGhcOJlKBJBXsSQSaX1JtgNmXdKDAuEPHwDtY5nIHKCsrl5dQoPENd6p1LOt8X_O67twM25UqhcVWe48m_vZrSs5AEwXOHHS5pvH4nMUfqL1Dly0JR__oBv5zvMfhhpfhr1wsq-WmxDvL1KLdSj_rw1BWCoBgPrPNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عادل فردوسی پور: آقای اژدهایی، خبرنگار صداوسیما وقتی صدتا موشک خوردیم و صدنفر آدم کشته شده می گوید همه چیز عادی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133466" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133465">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سنتکام: تنگه هرمز برای همه کشتی‌هایی که مایل به عبور قانونی از این آبراه بین‌المللی هستند، باز است/ نیروهای ما در موقعیت مناسب قرار دارند و آماده‌اند تا علیرغم حملات بی‌دلیل ایران، آزادی مداوم دریانوردی را تضمین کنند
🔴
ایران تنگه هرمز را کنترل نمی‌کند و ترافیک دریایی ادامه دارد.
🔴
بیش از ۱۴۰ کشتی در هفت روز گذشته از تنگه هرمز عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133465" target="_blank">📅 16:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133464">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=sHkPpkQA-QzHTogHsoIceDdSkaCyzbYlo3BYDsRhVYcf4SDvnmTlUhnJam4NW9mdbfHZyr2iZBgsEUfdTZkKgQuw1bEp1bW61LHlbgyCeS9ivNc6xoDr5lorUy4X27O1gdyOKRtSr-j1LeBGuWAukwRfzUn6IBaKXxQnoPD-TurWcOicCNprZP9vlyJHZZHonGgTt0YhMhDxbyasYwSZp9HIVafeZhJCgkeIiuTzOoAfaFCPgUhjw1jLF5AhlXo1BbyobNQhjxcNYzWQ__IGBMiHluhCVI502DbPPdVts8o2jDcNald-FSrkyKg1oC3me4ytcYiJhtDrpofXlsd2XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=sHkPpkQA-QzHTogHsoIceDdSkaCyzbYlo3BYDsRhVYcf4SDvnmTlUhnJam4NW9mdbfHZyr2iZBgsEUfdTZkKgQuw1bEp1bW61LHlbgyCeS9ivNc6xoDr5lorUy4X27O1gdyOKRtSr-j1LeBGuWAukwRfzUn6IBaKXxQnoPD-TurWcOicCNprZP9vlyJHZZHonGgTt0YhMhDxbyasYwSZp9HIVafeZhJCgkeIiuTzOoAfaFCPgUhjw1jLF5AhlXo1BbyobNQhjxcNYzWQ__IGBMiHluhCVI502DbPPdVts8o2jDcNald-FSrkyKg1oC3me4ytcYiJhtDrpofXlsd2XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار اشتباهی در تمرین پدافند هوایی روسیه/ پرتاب شدن سرباز
🔴
فیلم منتشرشده نشان می‌دهد که نقص فنی در جریان یک تمرین پدافند هوایی، منجر به انفجار زودهنگام شده و سرباز مسلح به سلاح را به هوا پرتاب کرده است. این حادثه تقریباً به کشته شدن همرزم وی منجر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/133464" target="_blank">📅 15:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133463">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onOxefS2Ek8UvOygqMspgftmQIfmITlaaaQgucmpDqpM97IE0Chuv8vLbi6zo3d8dBf2EvVMHEsoChLoV578cCJmuhWVmEM4i86iPFkhy--xX8AFIoL0Vi_kgizdB859f7lqKlGVp_CEcq-wvfyFyPeVvMeTU6MBUQPVeJKEoGCFoZuchu0_fd1QBkH1vtVIS4b62FJAZEygNY6kBBBXp76Qmtl-_b0MrEdVkI8v7xMQmfIiZQ1_xdvFoqL79bukOG-yMw1wBOEUs3kQMSmWj61bXXfH2tGzOtdAaUXzWCw3qkt4Taxjf2O_BeFlLRlF89SdbBX9Hg43GQAcQpnPDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمام کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است.
🔴
نیروهای ایالات متحده در موقعیت‌هایی مستقر هستند و آماده‌اند تا اطمینان حاصل کنند که آزادی تردد دریایی همچنان حفظ می‌شود، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران.
🔴
ایران کنترل این تنگه را در اختیار ندارد. ترددها به روال خود ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/133463" target="_blank">📅 15:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133462">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، کاتز : الان وسط غزه هستیم
🔴
نه‌تنها از غزه خارج نشدیم، بلکه حضورمون هر روز بیشتر هم می‌شه؛ الان بیش از ۶۰ درصد غزه رو در اختیار داریم
🔴
همون‌جا هم می‌مونیم و عقب‌نشینی نمی‌کنیم
🔴
این مناطق امنیتی از این به بعد بخشی از سیاست امنیت ملی اسرائیله
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133462" target="_blank">📅 15:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133461">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از داده‌های ردیابی: تردد دریایی از طریق تنگه هرمز پس از اعلام بسته شدن این تنگه از سوی ایران، به طور محسوسی کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133461" target="_blank">📅 15:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133460">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8fTa_g7KWcbBpe2aUvvE4gK_TWUcPvlcRb8s5aAkcivJ0sEn6pef4p6qaupHmY79hgkY30-zwyYK8jzoZYARceRvYZQC4c7obuBQ3shi5Kedt8AQDY4eDi-R33pZcNATbBLHp1dVUn55ofhD6_KpPrgm9-Glhj3xUWr3vRErfgLrIIIIr4pU4mx4P69vfRGhP1R8CHsDRVvFpuVljycU91dffq0abkQfhQfnCgACN2PckvPCiCYCEBFxBTKmG266qVDQxDf7eeZL4acpP1hFjZWDIRxeK4Fsur2TsLFeXHkVKBNZ1sWqgXNeYdGcwF20W3AQ64aaiFcY3C53zB4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاتس وزیر جنگ اسرائیل درباره لیندسی گراهام: او دوستی واقعی برای دولت اسرائیل و یکی از سرسخت‌ترین و استوارترین حامیان ما بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/133460" target="_blank">📅 15:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133459">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
عمان، سفیر ایران رو احضار کرد و حمله‌ها به کشورش رو محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/133459" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133458">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری / وقوع حادثه دریایی در سواحل عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133458" target="_blank">📅 15:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133457">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نواف سلام، نخست‌وزیر لبنان، ضمن اعلام همبستگی با کشورهایی که هدف حملات ایران قرار گرفته‌اند، این حملات به اردن، بحرین، کویت، عمان و قطر را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133457" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133456">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
صداوسیما: از دیشب تاکنون صدای ۲۵ انفجار ناشی از حملات در استان هرمزگان شنیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/133456" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133455">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1747c4666.mp4?token=lnnuP7ll4X0vne93y2pLZPl5WcGX6ZfqZhFRz0movblFzYR5EfbjyR6GrWXZtOmyZmCVqUZLouHA3ziT4htrju22ADB_LxioC3T8IYbHPN216p6GdtfEYiKeErZs8NSU1PNYXMHeM_DZXwiRd_Ql7UewqmbrcAhRg8ghReyDFSIZbEzKe4SUjpx2Giave6zB8HxyrnRTq3OTWvaFBc5QeIB_zkqmZ8OYONISN6Y-XfpkJv9amLIu_-HhhmrbzrDzNje55eTDQjA4ikbN4dBgntZ-Xvr1BBfoNxpnsNNBF1wlwmy8gVIT1FjT0AfopGm9U8I-W4l_HgMr85XW42xOPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1747c4666.mp4?token=lnnuP7ll4X0vne93y2pLZPl5WcGX6ZfqZhFRz0movblFzYR5EfbjyR6GrWXZtOmyZmCVqUZLouHA3ziT4htrju22ADB_LxioC3T8IYbHPN216p6GdtfEYiKeErZs8NSU1PNYXMHeM_DZXwiRd_Ql7UewqmbrcAhRg8ghReyDFSIZbEzKe4SUjpx2Giave6zB8HxyrnRTq3OTWvaFBc5QeIB_zkqmZ8OYONISN6Y-XfpkJv9amLIu_-HhhmrbzrDzNje55eTDQjA4ikbN4dBgntZ-Xvr1BBfoNxpnsNNBF1wlwmy8gVIT1FjT0AfopGm9U8I-W4l_HgMr85XW42xOPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: به ارتش دستور آماده‌سازی برای عملیات مستقل علیه ایران داده شد
🔴
یسرائیل کاتز اعلام کرد نخست‌وزیر و او به ارتش اسرائیل دستور داده‌اند برای یک عملیات نظامی مستقل علیه ایران آماده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/133455" target="_blank">📅 15:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133454">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD4DV9CeAgC0k38y-1WdkrUlLcORhqDIlyURkePTPcIcORxJH7dzOTWx6Aa5mRMW8e4xlYNcLhvm2je9cWJFjt5iwenn-dML4-0wxtnYNmvvdBIxr4EF-6tDy9EdBEvGlPw9hLOtfZSe23y3C89Shl8IBbkssimrGhb9OB41Qq9QQ9tKBXVd786YhE8UU-WJ3U2fpYfht1oTC646sDu3MPpG0C7eE5U0H3y7iXbNSiIGShiJ_eS6kHma4S6vCIPAuUnpp3q2siotuu3ams8fBGBW2RmVSPv7vWFDS1GU9bBgTxaHQBaMf33513MKVKbx67h7w4iJRZE8zQ3nnkKf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تبلیغات موساد در vpnها
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/133454" target="_blank">📅 15:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133453">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyvjNYN5bNLwQmSY47HBX77Ec6BW-vTQ1QaADGZz4Yky5E__s7Yq_6HEEp-WoceIxEXBFlMXY7RnUPeppi0HOvce64VkU_a5TQeeYBEA2z7QWpm3sD_ctf_iHroR95w8bEAhEnQXMitOu0IQIEB24xe3FyUfZ5gvq52hXFLTtQhl7ZwZZk2atkqsYrXV4-uZg_FjTE8eepsH9XXUKLDAjBcsWOXyIJRzWitDHpk7-XZ8_AXKIFJltASclD7cGaFjgPpaU9mnvwgSKzVo1oTwhxzJqRK_MGLkNqwTKvcIeuMBo4g2m3N72fqGs7ig38bWNLHQPPkSEBZeE60lKmbvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کل دنیا دارن مرگ لیدنسی گراهام را گردن ایران میندازن
🔴
جوگیری و گنده گوزی و حماقت تندروها ایران را نابود خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/133453" target="_blank">📅 14:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133452">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1926fd3153.mp4?token=GLJxopR4W5prgtX6GlnYjMDPNNOPYR4twCPJ6IfGoczbG7yLrUD7xwrnEiB6arycf90eoseDERGyk9V15gkjBzKRG7xeE-WfNWBV0YC4g4CSQrtnoGn-7WkAyRW7RFwAZ-kXe6W5Lby19HEgO6IeXGB7PIK2yYw98MBG_aA0_G8RNHqEGnVrvddAj6ELbBaj0TmjI6LE7QQYTtCGMVmcmMxdTOj74SJmrBW56fTh8NRXqhCfcgtLKNx1fNS8ZGc4E35sbzClF4KwVLU4cdFxt5VspV0A6_c9gwH9S0Z7rPjsA8I2kl5LFco4miojwbT3RpjBPQmxBIsCXbr_56Ipty9ZYuXwtEVv5GqV-4KF_8lgrUw7ZMJgX2hinAa-Prxg2y-D7rQmApiq_DliXfwhZB5zyJ-6XvFOLG0tLEXyuQ8rtIu7y9-KFNkd6qNTbEnkRkCoyRvIUCrAIj9q_yaQYQtDEwsw1hjzoHo_zQaQ26i4hfgScLt7NPsjcMKMhvJIYGwPPaAChaaN44Xbc3C0pKW6UoVGtCsAWpIJbBN73bIjaHzz5dBa3RxJ44O_Le2JvyehStI6vs8F2rWBk1x6num9Vf9tbPewJ2XY-e1wQxgp3s2gVgcOs8-jVuybsSF4AG9B4ZoP8M7Ikgi_K_VP3Tlb773WnwuH90tUgOqZDzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1926fd3153.mp4?token=GLJxopR4W5prgtX6GlnYjMDPNNOPYR4twCPJ6IfGoczbG7yLrUD7xwrnEiB6arycf90eoseDERGyk9V15gkjBzKRG7xeE-WfNWBV0YC4g4CSQrtnoGn-7WkAyRW7RFwAZ-kXe6W5Lby19HEgO6IeXGB7PIK2yYw98MBG_aA0_G8RNHqEGnVrvddAj6ELbBaj0TmjI6LE7QQYTtCGMVmcmMxdTOj74SJmrBW56fTh8NRXqhCfcgtLKNx1fNS8ZGc4E35sbzClF4KwVLU4cdFxt5VspV0A6_c9gwH9S0Z7rPjsA8I2kl5LFco4miojwbT3RpjBPQmxBIsCXbr_56Ipty9ZYuXwtEVv5GqV-4KF_8lgrUw7ZMJgX2hinAa-Prxg2y-D7rQmApiq_DliXfwhZB5zyJ-6XvFOLG0tLEXyuQ8rtIu7y9-KFNkd6qNTbEnkRkCoyRvIUCrAIj9q_yaQYQtDEwsw1hjzoHo_zQaQ26i4hfgScLt7NPsjcMKMhvJIYGwPPaAChaaN44Xbc3C0pKW6UoVGtCsAWpIJbBN73bIjaHzz5dBa3RxJ44O_Le2JvyehStI6vs8F2rWBk1x6num9Vf9tbPewJ2XY-e1wQxgp3s2gVgcOs8-jVuybsSF4AG9B4ZoP8M7Ikgi_K_VP3Tlb773WnwuH90tUgOqZDzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ترورهای هدفمند، ایرانی‌ها را دیوانه کرده است
🔴
یسرائیل کاتز درباره ایران گفت: یکی از اولین شروطی که آن‌ها هرگاه مذاکرات آغاز می‌شود مطرح می‌کنند، این است که ترورهای هدفمند باید متوقف شود. این روش اسرائیلی آن‌ها را دیوانه کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133452" target="_blank">📅 14:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133451">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cfj5WmJsEG9jucg7soKyt1XG15DwEWfRpmfWJOBWXUI0SUCoS1XLj70_XE-AqK9HTiZ3w4nfjwTpcJ01WypeNrreSjuZCOiC8Qtxu8DPlcWGboVv684vbIuFqDuoniu9Hmh6f0Aux9temrz4t5R7nzt-yEGeIvZE7BTwHM2D45w1DahQkGWV3M6czsZNssnIyJqjY3cyiPnA-SqO50uwYBfggIsZjjVtWrgZWbHX4-kGNY2fp_OaCIAEuBxU3sgEjkDvY8WkYHyJegh-IB3B8fSDpj7gZ6pwB6V317Y4VDZhqQ1JieRbdEoxkEFlMOZMmlsbADxAHTsgl_EgYuy6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضرغامی: علت مرگ لیندسی گراهام دیدن تصاویر میلیونی مردم ایران‌ و عراق در ادای احترام به ‎رهبر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/133451" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
