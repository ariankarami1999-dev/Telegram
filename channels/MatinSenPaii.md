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
<img src="https://cdn1.telesco.pe/file/nAtot4PDcDskHZi0ptuWYzZwG-qiRrg2zDXzYRSQfiW40T_u4hhLtFa2PMEIpGRG0dtNj7XAX792yF0c27x7UfWLiekg__YN1UamBSBoBmGFQbbGPu3PfdLZ0QwkNvjdV-Ng-h5HAdxp7LQdBdwe3MSL1iOwbuUoOdO_ZzyJZCHSZkEves2FZLqtzeohOzdQ4uXWe2dPPYCpgTWCLibRsG-TEMYLpAA_bIcg1D5pWfN9mNRHt0uVMBWcbgfC3Rrrfrqo0k3T-y5jWytmVhjmLJOir6liE76EKSv1bqEXO7eo-V9Eib9hbTMqljeSc-vC3SLincaJ8ldVas1Vq8zf1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/slH0EinZ3VyQf9kbGdBG3i8Uf3VItr7Bs-ic4ZMFfC_6JYTQXltCWGSuuTZR_NNusnD1F6Swgkp6YGGGUnkLCYnBtWuY8xT3kLZTgQdFa6EwIhSyZ1ooKlVfSsNDrt0Njy8m4ptJKxohnULDX8oCBTPUuVkE_DnRuAwFc7UrHg3_wfLVCNPVKJ2TCcbnA-B18JsBFIHUod69K0_psn76Uu3XSt7zmnstgi0uB4QHb2r1WDfzvVF-Euqty2A9hkluSzKMOnxANEOGJIhvMYurDxAXWEJe9e7I8XC-GQM983XGyHicPPSzHfI-hS4O42pLBBmyRmN-pN7kc2DqUuadYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jpyRVqtOrCixdrqsDfDEGQj5ujFkhsA7BVB0P_fDGk9XrmXSDuPReGqfXEf9AsF7QtE4zgYW_ZwjpM0sMhIe8yKAxMnFDJd66tGIjXZsvsLa28wlDm1ETdxVrBwkyP93mEVsYFVIA4TlmD0wrkh_eswcAia3jkUhYA_ugfpv6Xza8CPlrnqLwRBSw5NgkO-4cSrIx1N3sPuqT3eGbjwObl56gFWREYTCV0Ie-cb3GgOJTKT4kTgGzqcnGomcDqLZp7ad8RhtRJtH7c8KKLI441Nyp8ZU2btAyzA2JhrhtqM_wAXmAeK43OMd8DwOOdBJvsS46sOF5Q_tBLF8_ikQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TT5pQLBJyUKDcSrsb8xlwxIemxzA3DfKeMZJF-BkCKS5F3mvI_6dqTSa-sWGyECtM_Da7ekkoKg8ienSKrLyn554AKbhvRptz_wafbZlOQfxf78dgtk3YQh6yocgWoWuFlqEerYFz3ZX47dQA7Riu-HO79og2u2ZdS9GA21YlvuMYC4TGNpaAyXUmlfAvD-xUKwPM10fqyZ47oKGbbN779uK0_1jswhzjxvMcuEnETcXbMU262dfkTqcCapzjo8V3QLsYA_AqeZbigWFtAxdXxIEdgrikPG90bNExAuodLRpuY5VceYKXeD70YW48Jcv-jJGdLeyHx9MAyNrN0YE2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWU5lIZzVq2_sydpkfCbh8IoveaJ-sVNhod-a6mIuCEAHINT_dMEAoRkVf40Sl6YCxxp-llJPVrB5c-DQ136X-DCee12NB2uM859jM26zbGItJmbTwXwxTY4wYv3JrHbDwhVTRx2FUyrf_AO1KpAOhbDJJ0H6H2U-Xf7_uzl5VMXoY85dXYYTArwCjLaz7Eb4NzVu1of4tr2izgmOlEqijiJDFL09xd9L6onTvztwpNF-JeazLvgWo7EBoqoG_bThoweav28C1MQoeU2dIp9VgnSBLA1Jupc2BHCltabxpbI4a_LE3o8vs3GWj6oV2m_iSDWLQi1NVVb2Vw-_lMvOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NJR4SZyajLQgLfhSncVwiAtaj5tXQAe3gV3cktaRvthVjBmmB0EZLBHqrDUUSGBzVD9RvkseoCDND74mYSso_a1z0nnIA01gbbEfKrJ3yotnaIP4KkFmZtpzrf91IalnrmJ5ZO2GDUzINRQt7S29RthKNof2KFdUP0FlWJ92ryl7nyUGPvlAzccz-3cqKVQ7KCOCJsGDmBaKcsU5T-teT9kmH29j50LxNcQvehyIvDzlhNNrBLtsBSsOmFXFKLlQA0s9x6_RDSqcbtLOxrfDTF7EcN25aUQIt0jBv-w-5s2BlF27s0taavC63yLpl8C2nUj9lg7HoUm4FKY3Ke95xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uqMy5pK2Do2A-4AmNqPHrvR9BVwCmD85b8x7deWCaXUhRp7tEdgV9YpnzEmnoPgmtMpRta3pgXwlTUfE_bxH7SSX9_UrIyCGxL2lNGLrC2IxjeIBiLe-NKF274EhWQ8iwWmAwVXqL1OtkUGzGWL6ipvNae44c3cpXeWxoSRJ-bGUIpYwBAhfGGfqDIY5a02o1Mxo58L9Kq4AUbowJ5CC6GmUVy91jpoqKb6w8IRWfH3TWXfJj-cgbpUVjoXC3LM2wNO-8xpf8LDlitj6KMx8WqPm7gAQFkax_Gg8uv43LMEXnthFZgBZByB9fhumsjynkJoZhIcapRMpDIkyHcDaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CDFew6PSAqBvCh8-f02Q-aIW5D_3Xsyl3WSqaHZPTKAnn_YBbnKWVhgRmKvpFwr2y1ZGHxsrcdC2ok8Pv4vOQ0pTf3-s9kG6VJhlNv4sKCABF9SejYm8zASxW8cJi8xNcNUX--Y-ZGdKxg7cCFkg46urEi9ODG32fBhkvi1px31dwMbyzNOn_jvupzYWPiVGvwOej7qY3HLUtPkdaNXhG3u2aJvXFWfh5EzHyafa8_DObi9P-Iit1kdKhUFd0-E8iUyvyXbfCaE4c0G8zp6ijkqv7-w9gH5UrpEuhJRQ65Bnw1vbcV-3FtTA_ZUMDf37zXUV1IWe6SQFKTAUwtHvNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GiIjkJK8Dgjv2vAJx0BKrTNs6zHStXo4bbS9zJ8NAHg4dnRNUQQfe1KaImT0QZlqhs5l7gGAsVTNuQOhwqfs43g8NsjAsWiE0RPFlMuQxNg_vpBN9kwxfkZzER0qaYnxOxB_NVsTjIvuUqBg-s8pTY-phIup-39NEW3uAnXBKn-oEbfhIhY9qHMi6YMmLYyq4I636ZlwkhLjd88_z_gtBvBe8pvEBLQbCHPSLu05ynrWccsPxAsNOx-GowODEsj_pLhJlAf24R4ZAcDCIqtK1JLkztaTZ7sdbaZMlXtp6bn-_xsxH_wRhaOmpaN8l0HCGpXMSEouAEn0riOYmQ1H8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Yr5yiPsw7-Cx_By4yHnpMBe89UWp3b8TeKGHYnOg-Eaw_0yufSrjW_USTcY5GCg1T1SsteM0a41Wp4TExEmeKSe4-h9kkl80yDsQlRutkMRj3f7Bs2bNJJRbkYQVm2m49edBrTecFW7zWudqCGq5i6aswEcRpHM-kgc9mojRCfWRIur6KPP_74Uvc3E_OpyNgBPCjp5WJO7V_5ghJh8LGQ2DIow7tuy2E5veC-gFJhcEVGFC57BB7u7fzLAI2FTe6563rDhSA06PgL9VT4gOT0j-DMYBndDsmvJ_3BwxfLZQ5VVbso77VJqJ94A5JX49J_Ov0g9j-bHu8t4u-GVSOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Yr5yiPsw7-Cx_By4yHnpMBe89UWp3b8TeKGHYnOg-Eaw_0yufSrjW_USTcY5GCg1T1SsteM0a41Wp4TExEmeKSe4-h9kkl80yDsQlRutkMRj3f7Bs2bNJJRbkYQVm2m49edBrTecFW7zWudqCGq5i6aswEcRpHM-kgc9mojRCfWRIur6KPP_74Uvc3E_OpyNgBPCjp5WJO7V_5ghJh8LGQ2DIow7tuy2E5veC-gFJhcEVGFC57BB7u7fzLAI2FTe6563rDhSA06PgL9VT4gOT0j-DMYBndDsmvJ_3BwxfLZQ5VVbso77VJqJ94A5JX49J_Ov0g9j-bHu8t4u-GVSOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rezNiVpAwsKjSNkSS0Ijp5vvkc7DVX3YdEyEHvYlwzvxzD1uSr-NCQdI6KWxalALEK9GU3jjdCxpzk2UWzeE4pmKM2n0Sv7wUQnB_H7XjWAAGhFvusxoOfNQdTm4DuDVHtVYHm0oyOgGzCO2bxWaPZ67YatVuFkHrY8SsUzFgAODgMXFCbt34zfeQVOCjplsOqCxUR_xUSQJy7VcFLOVwSZaccr6-Ookomc4F_PY8hiJhHWhkJyYmOnk8HJPsbdYS4jWLgEoef_UqALbejP-KbdADWLhqm1P28CFiy_mLO0thmyWB6Skkaw519ig7uFn06mw5gIDvNxdPdS9geACwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری
گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای اکثر مدلا) تولید می‌کنه و توی بنچمارک‌های مهندسی نرم‌افزار (امتیاز ۷۷.۹٪ در DeepSWE v1.1) و امنیت سایبری پیشتاز شده که به زودی می‌ذارمش. آرگون با هدف کارهای سنگین کدنویسی، تحلیل دیتابیس‌های حجیم و کشف خودکار آسیب‌پذیری‌های امنیتی طراحی شده.
هزینه‌اش برای دوره معرفی، قیمت خیره‌کننده‌ی
2$/10$
و بعد از اون،
4$/20$
اعلام شده. با 0.1$(بعدش 0.2$) برای هر یک میلیون Cache ورودی
دقیقا هم‌قیمت با Opus 5.5
باید فردا ببرمش زیر تست ببینم گوگل واقعا پرقدرت برگشت یا هایپ الکیه:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kx-0bLitRiZ95J11isgggArG_qcmb7pNf6KnqVh3rCYpVza_fqlMzAwKQ1KJ0yql8UQ3W8Gzg8W7sFGkqlrnQepVSX0uCGT2wtlI4L5JRo5aQBOpuj76RPc6m6CQvq6-xjEXnoCg5DBKJ_ORGFqWUrIWeSsWYWINR4-q1elTdc7ifHkVEPgFkoxotcIST45Dr-ckRjg9cKTuKLL__dD2FgBZxlAPfTfkQKnqj1hUbQJ-rpPt48lHoJ8oWPMoQjK0OvSwFzJoBZi7cuqE5jZWOT_mWDHEi8KzkCQer8hpyhdoZmy3HC4bfgPrU24kaYDdo9LaiftzINn2kIWDOyTOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ld5T6BoqroThFIEuibERMm1cJnarQpUhFDe_0FELV_5BSYgiDjqFsJwIvraeoc62m-O8fx0lbOJbtXj2uyL3h34jmjyJsJ5z2oI3isc1Q2Cz41AOLRtUcTjYG7e2kB0VRqAICtuhpQjkvRp2GN-6OFQx41sXq4R2MUN8RVxcMrAFRl5pRksj65jIyB7ELMhpOIn8xpm42ZgJm0jT2cqP2qpqivJHjh5XFXyZPoSwvO-9sg4Ll9XMcbCurfaxa-9s1ade96zBhXqQf2IDPCmbH1aI5bGj0_ruPMCYzBup-a9qi5kKVqzWsh2vmA4R7GHMZvUm2o7Pgf2H2cNncC1rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-poll">
<h4>📊 کدوم ایده رو با هم بسازیم؟</h4>
<ul>
<li>✓ تمرین انگلیسی با Shadowing</li>
<li>✓ زمین بازی سیستم‌دیزاین</li>
<li>✓ تبدیل کانال تلگرام به وب‌سایت</li>
<li>✓ ایده‌ی خودت رو بگو💡</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s4YtyFVdpHKGq1p3lNR09XoWyd7n9F1oDEQbv6sBmLIKqHvpNyuyyJkw4lYQkvLs4O3SCr6AQ2rb5Nwi8KWaYhMu-AnN9x-fRV6CzE9dCtnoI8KEFiqtLl03_900eAifDwsMTYPcin5cIor6pDxRxcN9XC7_IOkSs5fz8R3gZq2dGkr9MOvM7lYLYImBJ5-HYJSIBioVN8-AkTQsJylfwkyrnjsU1V44qGMj5Zlg5hkk4bQkH33RT-PgZGtyHnlusIq2OwwzvBztbBb7tL2_Kt5mZlTFxlVIDkkBlYz4D8f-HpdkMIsJAbveVKzqWmGkY2qwSYikWyhm_lHMYkqgQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qqYC6NDIYYwZwF5GUcvTbelcoLUlqa70U84yHD-2sPshMljsWBOlxV37E3-oahqVr1zK05umA6lgDbalaiiiR3Qnp9BoPKfcJpJvD9xXwAT5aVSnPPi2oXyE0deo_QORYqM9b_sbhf-N83xc07L4xicYSnpboS6AYGt2xbRdUOgxlWiV85pOQ2uk_8B2XNMsx2bzrjJthqZUhhmlLr6bHF2ycHKvHIrJzpNLNwwXJBGMOsLc_Z-Wo3hWNCCjh9YF5MPMHyy92r1skK3lMB4WniUjZLM3_GbyMnUhCLSwypWVN-cgIUP8oI45V_R-jFVQpzkAzcfF7hdcdL1LdkWSqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ll7qMLMfG-pZNKeTMwNttYY_52HLZrmuepSB4S3YCCQSmtyFEM_LF07ohDf5J7LrIGUcbWNzkriafmdkT4T6lB_Wwb2k3O6pXNVURX_loPGdUxCQnUeUk8ATftvxhaMXYIhlmUqBm0VKCfBlnGizwZ_x-QiaTQoKsmAoR95zR16trWpUjJAXtbddHUEnxBkPqNBIIRhnCIHGE8nkyHy3Ow3EdOPGI4aqBKaULCp77B5RprK1DBk_CXXVrt4xPI1a59CDRNv7BfBRh_kNZ9H-0R6ZUh4Ws-aIa7_WuJPg0Eq32sw8sWliu-2HgszvzFr14NGoSulo3k3MwW7z7rcX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mP3J0rvr7-pMaD8AHBPs6dD3TjunkJmx3F8bSfFomkkyyDCy7LQaw50D8OCq0BX9oAhRiE_bNrp1mqfM_v95MgCwSJ1XGme38Jn9bT0dQ14b3vjiitAHHIzg1-BfM9kSjB5_BMBAr75ei7d4FNnwNl__zEZy9Tvc8C0rkwc-ILwc_LghUPwPE5MV00XdajoCGYCZ5eXbZvlt8YNJ70bIe3miVZqIa3jOxFSw3ioMw6-OwzrCUj4jZIHOzLv-wnMFXtQSm-9BPIV8Hpa-VZisnCE7L1mAKCT-wYlLGxJmiB7zAGx2Y-Lv3rWPW0GNrjqYrTRv_vCcpYxlgF6domQ88Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=PNkqBLz39rNtRP8uL1F0e3_ztdbfad-LEgsOQtkknX7EcnCg5tXCjrOYUlzdD5-N9rVyM1u04WZgtwduFUvzPyNxNqyieq98kV8tZKa6wZmba2YVOGjoVgBIpPb3iqJlJ_MoeTGkNvmSK-nX_ETkLd4JxL544Sf00--kzHIYzqXEi6mFL-tN3x9l_AZZ2_jng6KCRAErpTjucfETxwCoDnyl1h140mKNViN8n6glZzmqP5NE6sutUVaj_TEPAPNvFRgGHmeVzg61T88XVznr6RqqF8hfaC19qcqCvDvsEyBDH3f_qyTjuytGNlTKvqNARXVP6QLfFDVEwGmagrhrCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=PNkqBLz39rNtRP8uL1F0e3_ztdbfad-LEgsOQtkknX7EcnCg5tXCjrOYUlzdD5-N9rVyM1u04WZgtwduFUvzPyNxNqyieq98kV8tZKa6wZmba2YVOGjoVgBIpPb3iqJlJ_MoeTGkNvmSK-nX_ETkLd4JxL544Sf00--kzHIYzqXEi6mFL-tN3x9l_AZZ2_jng6KCRAErpTjucfETxwCoDnyl1h140mKNViN8n6glZzmqP5NE6sutUVaj_TEPAPNvFRgGHmeVzg61T88XVznr6RqqF8hfaC19qcqCvDvsEyBDH3f_qyTjuytGNlTKvqNARXVP6QLfFDVEwGmagrhrCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oz8yEuIGxKcQ-i7DnOcobCGeKFC7QLigaFwyBlESC4UQldS6OykuM8C7UK8dQti18oI802Ti8xh1nWfXo81GWj3pt3ROWfUGh9dFVxyaeoFnyLaRM03SyAjFU1yWJ0Y74W7xYqYTDeG-M4GomeNoVNy5Tc69kOGBe3pAZcaGfpyrHPF3MgLM_gAVs_9uLjylfIrRlt89mzROTAL2QBI_RXOIDKu-ljsAhHPmf4xCTtmxZ-IQ8AhVOYBo9lb75bE4bL_CfokOOMQERDPy2BfeyJq9a9RgWKyu3e9DvXxu-qkNBVUx2hKLAXkuNUbhdQZIiC6oosHaO2kdueGrgFT-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ubkc2tL822Bo6IZgRHDAEL6PppbhwTmB3wrIgggtRCSTLTE6veDuoA1iGDG73t4WH2g96AFHSzIh9b-TER46lWxtPXUyTWEIksSJxKvhbhG6NuzF7JU8lrnAsGgHFd3kiHNM1R-s0j4lVlaSDiQTyhJWdJWFiLhUYHbION4iSwpgjVnv4dYxVzIT2xVZYbCVt6FZ6DK5RVFMBe7YdfHCLw-njqBpMN5bUCFpMAlj_g8VRNZrVGvl99lKcL8EEZqM72l-fhsoDzI-DIOGIf3xPVy_s7EEGSETxDbNkVDEajBkDoW5EEBBHlz4PT-pVTQd6Wt2i69yWXJElWYgxobD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oWDMTXCdaPwqYW2AjDnsZ0APT92GUaaNnlyUjN7qkNLzo36YiLpCJaEb5A8WrCrQ9rCXZ88Qc90Bn_Daj6n-RPZmTPGqEMNDoku5NrluA3NNJ9xgRN3i85jVQOLtFq795JCNDSv2HE-Dx7cBvIAbrjGMWWP1idtzhEFdiMDmnEKszwIJpLPd54AufI9Kk7FKvg3gCZeheD0AKTla8V64GAv1kBKEUWjquTBOuMKjAZP0gDznmrzwDoF6G46nsQ_2dB77y2BBOMsHYTVKkspkma9KYz5Cpgo3pfgCx5eGsJHi2mxRHLki3SR6ZDReM7OLTe4dnUaUm7ySaBD-tlP0Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZdBhicqChYmo6nDRmpJYFbPyNqa4fwaZR5KXKPBk4cvf-8idsO2hZT7do8phnKCUc0pssUiJ5fNsK0MIs8Px9PWs50Up30g5uNf2NHngV5C_Md4D3DI2SDWSuIoNlIDQstiMRLU1Mrk32qHKT5nt7mbArBUQYDdrx8O14Aagq-ac6fI0wUybyWgNAtIrxvHXYrafw_wlRv1H2dAtzLmfl12qeFSq4B3IskKXHyDew9Eea3IrMB2PKva5DtLlB4TrhGefD7hTiVRm9Spb9DXTvgYwmKwxVrdIxgayAO1kLb9M5x7k1iHhB8ANMjBdLYGqeH4tuzTkFgIxNLapEPvbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار جدید ماریسا مایر فقط از روی عکس‌های گوشیت می‌فهمه کی هستی
ماریسا مایر، مدیرعامل سابق یاهو، بعد از راند ۸ میلیون دلاریِ seed بالاخره Dazzle رو معرفی کرد:
یه دستیار AI که برخلاف Muse و Instinct، نه خبرنامه‌ات رو می‌خونه نه تقویمت رو؛ کل context از Camera Roll می‌آد. از روی عکس‌ها می‌فهمه چی دوست داری، آخرین سفرت کجا بوده و بچه‌هات به چی علاقه‌مندن.
مثلاً از عکس‌های خود مایر فهمیده خانواده‌اش escape room دوست دارن و چند جایی که نمی‌شناخته پیشنهاد داده
😂
😂
کمی ترسناکه حقیقتا
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=R2mRBozQTjWm_y5jpNjWIyolMGY4qvHBx8ZORwq0fDUjGMtKX-qbfQKUoZos03xLW7MnDIbCLB0-IIxHDL-NNpbv77a1KpOe-za4Aan4sWgldSsTHwdJYfgNhTdSCPgaYnYjFT2ra2CXYijm4CaHyXLlTutvHUFUZ0mxpoQ1lTCq8btUo0jH305vDYVwsy5sYK9lBwbeLW6IgMYgM6kAj7ZN4QaJFSc_ZdXjjuxHIYwG0ms1Nmro6tqwFJs-I0UAuyUpYxBJAayGxjMpjSroTHGXeJXbnf4mUoXvLYjhuAjO4lw66KP7ll4Np3EPBozzpU8kjTVd7ueqWBfe0D7edw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=R2mRBozQTjWm_y5jpNjWIyolMGY4qvHBx8ZORwq0fDUjGMtKX-qbfQKUoZos03xLW7MnDIbCLB0-IIxHDL-NNpbv77a1KpOe-za4Aan4sWgldSsTHwdJYfgNhTdSCPgaYnYjFT2ra2CXYijm4CaHyXLlTutvHUFUZ0mxpoQ1lTCq8btUo0jH305vDYVwsy5sYK9lBwbeLW6IgMYgM6kAj7ZN4QaJFSc_ZdXjjuxHIYwG0ms1Nmro6tqwFJs-I0UAuyUpYxBJAayGxjMpjSroTHGXeJXbnf4mUoXvLYjhuAjO4lw66KP7ll4Np3EPBozzpU8kjTVd7ueqWBfe0D7edw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=pNzKGja8Rw5Nl3AaeHUM8aNucI-ZUxACmZOSpKg1kpNMSN5l-KC-RFMjY-tTt-Wdau1-LsrZZWQnbPK4zk0ljjz1j3hcVBdTKfIh2dnbNVNrWuViDsrokdA_fCOqXLl4TqmWLfPRVGHuV_JmX7X2VRdyV7R-IUKo4k2BkHDNCl-iF7xdQr1gi_UhRd9m4iPKCXDgZ0XzHc532-JXnbOdgHwuglZHj3h7oFBnvXLt8ZL229idp6So-pOlLVJ1MkJlWkqU9bcrnmXq-un3y2OCEkxzfLrrOv34DnwzY_ifyq4z9zG5HKQJmFJ_HZI0B1Ye6eQwWt11KK3YsVf68P00mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=pNzKGja8Rw5Nl3AaeHUM8aNucI-ZUxACmZOSpKg1kpNMSN5l-KC-RFMjY-tTt-Wdau1-LsrZZWQnbPK4zk0ljjz1j3hcVBdTKfIh2dnbNVNrWuViDsrokdA_fCOqXLl4TqmWLfPRVGHuV_JmX7X2VRdyV7R-IUKo4k2BkHDNCl-iF7xdQr1gi_UhRd9m4iPKCXDgZ0XzHc532-JXnbOdgHwuglZHj3h7oFBnvXLt8ZL229idp6So-pOlLVJ1MkJlWkqU9bcrnmXq-un3y2OCEkxzfLrrOv34DnwzY_ifyq4z9zG5HKQJmFJ_HZI0B1Ye6eQwWt11KK3YsVf68P00mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Claude sonnet ۵.۵ توی بنچمارک Terminal-Bench 4.0 نمره‌ی ۷۰.۶٪ گرفت.
بعد این پرامپت معروف بهش داده شد:
«یه کد به HTML بنویس که یه انیمیشن دوبعدی از یه پلیکان سوار دوچرخه رو با گرافیک SVG نمایش بده. نیازی به تست اضافی نیست.»
توی حالت xhigh: یه SVG سالم توی ۴۱ ثانیه، به قیمت ۰.۰۵۷ دلار.
اما توی حالت max: تمام ۱۲۸ هزار توکن خروجی کاملا خرجِ فکر کردن شد، ۱.۲۸ دلار سوخت، و SVG‌ای هم در نیومد.
گاهی سطح Effort/Reasoning بیشتر، فقط یعنی «شکست» با هزینه‌ی بیشتر.
پس الکی درجه‌ی Effort رو بالا نذارید. برای مدلهایی مثل sonnet، همون High-medium کافیه واقعا
🔗
‌
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fYBQ91OcxMpbXBvgHnOilbQbqk4hDycFoO2LRgFwGE4Ysj-Tap0MNFDk7abkfd7i3VpBaBZULSWxkq26C6m5EuKwVUyDHJ6oqYFGzu440ecqk1zH9dvUwi0m3NAU4D_R0-JQgi1R9F-J3U-p5E92s4-C4kZZVtcX1U0IEdVBjog-VixWpVFz6NmUY3dTCEPrUzgY7MUtXRUayVhKJeh-SBTmhtWej4TL1U5EFLLkmpaKsYeHqcQO-V5UylSc-DGm_Um8WYkHSzzgFN6BpwXxMJETib9Ixnm_0uLMMV1IOA-htyTjzHbwtc1bd0aPW2ET0CbvOWGt0uou9kGtYRfiNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GGJz99B1oYjHaVShZfaesHtbDpgGei3fsnmN3zn5zUIpw26EdDHRpEryPrBrCgp2QYc9uO2h2foPqH47tyrwSavrT1PGQIORZk814ZcJcHr2WrpgD48IBnM_CwYgNzpnP9hxEq0AWZy1Fv8UBQD2bRTKXB86GFS0eOCGPHmlo095R-POnqPfax29VuYQTmluw66JAj4iUU_s9E7wQk_69YWHu-tn-igt3ZD_pC7Pdzr5hiVuEm9qGEOcxPXTYgcYVUCNUxYT5aL8TfKKuJ9IImzYwxWRP1ugyOgMx2ob2grvBDf-wHgkKUYPZ2o9HhDetl3Yz9ttKPjH2VQOi-s36A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OOfv3chnuDdSr-kDkW_VfB17lmubQq8cQroD0fxLfSa9sWszKQ1Bqc4-KgFhtxXdviVLSSmJJBd_ytoQmUOfZQUl5wCvEg3SfY1rKTjenC4-KnFdZg_MB0THSpAk8kAs6cxHpJgMlpTrvjKjm_nv1P1x4Wan4ZxJZ4CcMjaw1VbzIp14Zp2iTwINqhmvOsjk9yKAUjO6LAMEe-jTx0zjGiOIaBQKMSktqk0r7pdSTBhF8n5FpjTXvnuUmVIF612tKib2VRTwWBziJZjRjC_j6xf4mzEZMDcqzzv3x_HZ2zLwqC-MC1IEPBcOcIFu17mUZ1bk-2d2kFEDv35sRM4RTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UgZno9EtmgGsUosSrKf8u0-IFjFEhJJ7QC0OMPMrRf6ulvx5kHmXPi8eqwEEOz_YQ3Bfj96PJilxYqhnxLBGfq5_pLKVBGVN8Rm9eARg073sKPoitRp9Zs3dI5K9JuPUQHVwcy5S5-FBPMbS6nzO-rn-5fmAikggpXMtR1KcXCnUEF9wJy7rBHCeJgEN7oqN_mjjJFaYOYCeyD83-0HppMJCrJCtJ5Ip0PraS8uC3eG3wC58JhZnahwGzo6bNojD8FmAFeKaz-wLZxIw3mrsM7sy3dt3FUaKGLWmnRif46aGGZnt0tNAYeFI85CrdMkqg1qWranEJwAG0jd3zQshMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hVtRtH5qGc-X81ANNz59wAd6kvSO0Yb2BdHAziMGb_1VylFiJAAO9-NryXPxC5isfCm2IK-5rjQfO9ZVMtCnM7hlL7J9hVrP0396tKZ-2RQQp_9VUoW9HBxj5-2FKSbqOeVqeQhfm96TUPOYvB0m3uv72C4uLhrbWVwMJLlqWypBndTILP_gH2rAtHt3Ylu2HptzSX44BGuHqDAExjQbKCt2lXOGa-qh9JoZ5GPPs3kUTf3XxsMdWKMrrO4N5CtSq75ysS0xRbW4kJc5RWMcA0_8uigLkL5dz8Vcec4Ks9k0sbJ1T4veCbnE10OvLndfc6BKcaHthU2CMpAWsSkytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sckO41WOhXSSBunOkjM8OF7Dt04tGahBK-YiPRtyzpOWmjMd30UN13T5VQSGFLVf10kZ-YqFJ95BjdLTBee-tL9GUkOfocu_QtmmhVKEaKG5MTX-fYH9xH1uMeN1cHFr1EgIVFl8gdniz1b75GE-wNDl28sUzoul0z60Dk8YZauHv9fc8dTod0Aggd-46I7MgQcOkh5e1K7wsssGjpGcJyekjg_0BbPVwcoAZjbZsj75bwGhLLZSGlbkRaEsIGioYR5H-__pDGBk68a6xgErPuczFwHi0z9EtJSXQXyG2eIDL4XY13Bqqc7jY3-Hi5TloEKC039ctdMO7JjufWJOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LD9ijrDijIeHb7aEFhgAiN7H_LO6o-NMha6GFwA1Az_TON6y7epDZ9An_kBRwIEKmF_T4ob8_-XVA6-BlVWJw55N03Yml_wgpPSEKWQU8fjfOkZsUBJYcHPUpilzOa7Mc5yQPBaTw27t_3ZIgmnpJU3QIlZNB660yixGcmTrDEFzE3bfaPmYX5NT0joLvHSVmI9SaHGe5NEABxhdpDwoeRYVdqp8zJkf8l2_2-ldp8z_6y9oePbtmpGFJGNFC5fN1Yd0AKU8DfbaX0fec3LkFTICp4GA1U3xGdgLDEKC0H0EpkL9qylORhXj9syNzjnkT4q1v8PL9Qkzl6WyDNpPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J1LhNGTSSdxEivgVB7UO_yAuxBYuEX63MDubhmvOPUyymKEzcUabcqTfm6it1ExYzv5TW1apfnvnhnVF_VfnA9QNyxrk2l2F3zkt1zZJi0c4uUDXUB3wvrcc5X-AmG5IJVC7LWQ8Kdux6Xi9tlb0wxA66zzl2eUW-f0ogy2fLys0ovAKZNUixR4jPjjncDQavrIrPuRpG-eycYoERM7jw2fDWCrA2mYKXUMVZeC0FTTwf86UZ-ddkfgunMP0HrrjtvWp3Nsfwfi356TABvTV2IKzK3VoEhI_mLoJfxm6vKljvUBnd2ZJ6hg45PsWkHCJsJy-oUywj52STjwucl_rbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=BJwbY8pETJIP2LkV283e9UAH82zEahowQg6_zPiDPpyy2b5qqtJFuUoG7HIA2NoeKZKR0BA8_anN2vgwQBcELYf2ydnqoPG96tuifMzMAARATWDSxxJq-t8_1aAlSVN25qe3fGVx8Z02cIpac4F6DpXAVEhGgSnq5Rm2HjcCPYT28HUEJjK_vcqI6XUUhYf0uMN1qMQ4LAgjUHVSG8SrHFn7aY21NSKyvMgU2dHJ1Fke_sJwaMCIcD9p-cK6fm-OsEQVQsXvdKwSvUHyICUzZPmRNLPciLl3C8NrE9Fu5g_JLUtgJxXucLXizoI1mFPXlz_KT6YOrXqurSfoMbFtkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=BJwbY8pETJIP2LkV283e9UAH82zEahowQg6_zPiDPpyy2b5qqtJFuUoG7HIA2NoeKZKR0BA8_anN2vgwQBcELYf2ydnqoPG96tuifMzMAARATWDSxxJq-t8_1aAlSVN25qe3fGVx8Z02cIpac4F6DpXAVEhGgSnq5Rm2HjcCPYT28HUEJjK_vcqI6XUUhYf0uMN1qMQ4LAgjUHVSG8SrHFn7aY21NSKyvMgU2dHJ1Fke_sJwaMCIcD9p-cK6fm-OsEQVQsXvdKwSvUHyICUzZPmRNLPciLl3C8NrE9Fu5g_JLUtgJxXucLXizoI1mFPXlz_KT6YOrXqurSfoMbFtkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rKJMZgqO1r-_bXQBDwnr_r7_h_pi4LEp8P4oeDSIhs7-DCYNopZqtm-sGekO7lWBy4WSw4GCVshjzX3rKSv4GBQAVcO941M2xm45RlVR8DVr39GA0mhHUjrQmZwsbZOI1FVP5TicGXMRMAt0gmAolcgNOFFk9txlteKybOcG0BBMeaz8SVP_Tzl6VK5pwZvLeN1wYaSUuk6sKUqj2WFZrymMNhtarsTkURK1PplDmgGye8HGYsImJWpsB58qzZsu5GPek4SPaTAKQ4Ckjey9ETgbY5m0PiUzCOrCiZkkVirr0tIEfGZuHorDyUHjZKC2cA3aBBpiOyDK2v7aoKOKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه‌ی Hermes: از
MEMORY.md
متنی تا گراف دانش
نویسنده این پست ردیت گفته بودش که مثل خیلی‌ها به دیوار
MEMORY.md
دو هزار و دویست کاراکتری خورده بود (۹۹٪ پر و مدام درگیر نوشته‌های کهنه‌ی توی کانتکست). پس برای همین تصمیم گرفت plugin مربوط به ارائه‌دهنده‌ی حافظه‌ی Hindsight رو توی یه کانتینر Docker جدا راه بندازه؛ بعد از کلی تنظیمات مختلف، اولین اجرا و تجمیع گراف تموم شد.
که این باعث میشه:
1- دیگه محدودیت
Memory.md
رو نداشته باشیم
2- سرعت خوندن از حافظه وحشتناک بالا بره
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sQ1Nn8_32bZK-filfTj0bi06s2--Qd5IXslZGbFPa8dZZ2TiNr9RQpAFpp45I0qE9bVi_gOY7JHDY-1-uES9KDk29HRl7eCvKs7UdqlqOOnPxSauY98qwB_a_xydY9v5QOblZetAkWJ4CKAGp-LqCMBYnv1tUB2Fzf2BIhhe-MCduUqgVNn16_vyYEoq0U7r8hVvu-LDBuGktrSmQVP3ZD70sbNb-HlXM7UeBM0dDo6DEvVz0ygB1ZHzc4XTYZyXuVvPibQFJD6-gRStGV_nU6fftS8Aphof7_YxAXh3aUZNOdWQ2I7rdAUsrhi2IXqEnxn8PAw0BCsRHxXQAqaZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UacoOlXV8Z8LZFRzZlDtnkPSsMW37Y1Y8q54HaQyA_NX1CCDJn1Frrs4xAY3B7iOD9jxrKez1vw9YGL8AxEYA2YA6CcZhqJUxfouviLk_j9iKvYdVfUi6z3FsQbH-UqX0ymjZDcGwR4f0_9UVUWTWqEJRAVJJy1AQ4YY1mrK-DjF9vST7EuvGgMjthYc2R-eWtcVHNkWOhDpDOlFVqOsIpq0vuTW4HZsTbL3liTcwwZ6TwHSdtFRru9yuzX6y7jaRrqzj7DDmei7eE6ABoY4Rt13nqdqyzkNhScjGV-su9jw6rxoBRxcbEWR6LsjKOK_lOiB-Gm0r3Y57xgEj2w15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r3uM1ZcWW-DLqXlCdC7TxdM0skGEIs7Cj0wwvb8qkrLUXPDAZYw5jOsDJ6lagJ9jHo6r2dmkW0mE7novyS3K1ZCVFELDVLmo35V0lVEEaL8H00YSw4gx2TfMpwX7w5KSMrcsvaeoJqRXtLJpqJ_m-R_LUtw20XLwW6bQVZkk6B--iQzXprftVN9ko01rHNR2k77qIP36Nd2lIImNDWG7iGPv31ne2Idpmk8zEIxq7VanD_ychJUplB-dSpPgz2lNoyBou_jKpWjF6E2ngbMuO_lfM4MV08rhe2cjVxKZj53GUxUFv3D_GUf-abYH6ciEPq8hsuUyezLRpgPg4_ev5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HkCLUc7aaWb75ZCexjXpWvhOcVe0v-aBMRKG5_B5bLXdJRkKUOqJx9C3KGBeozREMUPnrOaVIPLLhJH15HRHO5kO9BgJQ51RjXRcJ0T18lixyEcDccxakKkUrKTUVEY8ickjhzZoe1vofMJYnmwo-XEP66kTGgiSsUl6LWA9-jadW_MN4uMYLyP9Kc_EjZxquJO4yJfSOiHGTZQ4_BQAqb6TzPCWamlCnNQi8qUOkms-Ys_JphqKBebvXPSKLCEJoILlrqNcCocCSTZePoJNyUxu-bKF-u2rDeqLync4vabWEo4QB-2Uv6RNwvLhSVutXEy9eDMg2cJpAblPavYaNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WUDcm7bb6TzY8ckeCQBFj7awG9m-NzmWlQWQMv5rEjiOonofTri8ZxlcJRjPWnBHBSj8D4orqtiMoGwaPHq4VmJnwj1dFMQtmBI_pDVRygVpq36gGd7uSXaqDz1_5j6eBBujLMHo2jTqVPqLJd9itUfSmCY3-PDe87QWO6uI5y0hwaEkJ36wCsdRGVqXwD8FtEvlEM_9eTcmmIrqHKGqUZhf5NR7wzsjXzppc-WJdpO49oda857-znWYKsY8RQwzfc1ck-1zKdbY63_JRelXpQlse4jk3aR_ltZyU2GWfRcDF9jd8TFNI_3JvrxUCA_qekutjjIg5A-9AdxXo2K44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZpA_KltrRZX1MLmIE8KngZ5UUK1YaasRTlvS1HAljvaLODJgc7I46y34eupNLyjKl1v_sFd3MnGvrA0kH7tXFBC0ADqgizNtKfsVBmtQzzauXMcRmCigLFTHTfSq7cQclhVIrMlmitOVhzGdqE5VE9PAkezTnHrGEAwGDOFs-Nw20NR1K2AKEBAgUnqQoRvAxvj-MOxMsJwZiAaAnQgzAhL10heGuEpdBVWGF5tHithuWStb6DrU8mPLkMD1SZ4KfqwczUCloa6e7ixh4qhfExW8UTO9NRqg_ckd5hlxxFgIkiWzjxq2lhRnTpd1HQXldIi_8eo009asKzA-agLlHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvOknRaGVGHAnq6ev3sV74gjWewqIrjaGk-HFTT7OM2bJBCNa4lJVtzMNVIVDYXqlKiqAp-DFxfdFAoT0heM__Q_IbG4tM4s6XWQyJypPTfluM3WULd35dFiRIKem6XeLh2mOiByg8AGYnprKS_og_zpl1lNLcOKg5wH0bsfcMgTsdhF9jPGbQdEjE70AnrsDPBYFbpk-U9mOijejndMRv2I6DqyGPoJk4S6_-EMDYfY4K5HTNnc7ev_xGTzE9bAoqK_bDobYWAxs_tGdxqR9dqV_OKsSfOonDFt4gnwiRHPp4trpjsMqQD9DAs-OUJil28dU7cDkGCyfcj1-Nxbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C0h47rqeRRZzEL8Hmc1dYK2k13aZMfDAeaPnDCndxB7FbM2c_J-oQVR5fSy5xU4g19X_ttf_OR18v4dPRbJXPKxCvDYOJ_uY8PTeGimIOIgeQtfVmn_CWsNVxkIOnRZ9_fcoZM6Yxr_p2zPPLD6XC6d3q7BciQMDV6lX7-F0DX0GmbR1GMyKWpqxR5HXxIeVvI_0rR5mu5QTvrORfXcWEQ5pgdFIHQveBf92jJRWRK86YRETIp5W0C3P9cAJ18MrHezNuEMGaD7r7UrNbEG2Iju_GEAOONBgMUBGh5cTDVBO7H4-TcUxW6_ZvmD2K9wSPa-P9LyU7Wac4WLZwfp73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حس می‌کنیم هر مدل جدیدی که میاد، انقدر از مدل‌های قدیمی قدرتمندتره؟
باید بگم که این بیشتر از منطقی بودن، «کلک» شرکت‌هاست برای مارکتینگ
اگه یادتون باشه، 2 هفته پیش همه‌ی این بنچمارک‌ها(خصوصا سه بعدی) جوری از GPT Astra تعریف می‌کردن و چیزای خفن می‌ساختن که انگار خدای همه‌ی مدل‌هاست.
بعد که Claude Opus 5.5 اومد، خروجی‌هاش رو جوری نشون دادن انگار اون مقابلش پیامبره.
حالا این قضیه برای هر دوی اونا در مورد Gemini 4 Pro داره تکرار می‌شه
به این کار اکانت‌های بنچمارک و Ai Enthusiast ، قضیه‌ی Strawman Fallacy می‌گن. یعنی مغالطه‌ی آدمکِ پوشالی
توی فلسفه، Strawman fallacy یعنی از رقیب قدرتمندت، یه فرض پوشالی بسازی جلوی مخاطب، شکستش بدی، و بعد خودت رو پیروز جلوه بدی
هم خود کمپانی‌ها، هزینه می‌کنن که اکانت‌های توییتری/ردیتی این کار رو انجام بدن؛ هم خود آدما خیلی وقتا این کارو سر هایپ و ... انجام می‌دن.
چه شکلی انجام می‌شه؟
1- مدل رقیب با پرامپت ساده یا بد تست می‌شه، ولی مدل خودشون با پرامپت بهینه‌شده.
2- قابلیت‌های رقیب مثل reasoning، ابزارها یا context بلند خاموش می‌شه.
3- هایپرپارامترهای رقیب به درستی تنظیم نمی‌شه ولی مال خودشون با دقت tune می‌شه.
این شکلیه که می‌گم هیچوقت به بنچمارک‌های این شکلی توییتری، نمی‌شه اعتماد کرد.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW5FqvKW_LZBbWaLPLdSPCPyvwoDFMmyta1iyIYGi22q4wGzdUsysTVvUnFFx_n5fviRj7s3QVHxbscNf7mEXvJ6m7ESHKwhcoc1VnsGHS53hjbTJuO75dtKGp084xF5sTvkH9NIunHRhS6eleEcI0jZIbkLRqU-4YaJqh7dfWkLqv5_YVUklRmh-vC7rcKzGU4fwInzOml9QY9gIxl_GsM7MBERW3Tb7bAtvcxQYSVApX0rmAe68Q3-124iiLzr2kd1jMQ008HdKyWYuPOt-ZATPZ75nznn-7FFp6iaUdtglY3k3GDxU3YVJTLSdGUywFlSCIOcAQsUqyBNSNp2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=Osnc4mfG0lwHjZvx9aIOnvMke8uyl0zQ9Jk1WIDPudZGlR8pFbpCia3eH4Dx8XyzrycdF8G4cbCUAULHdBuUDTBpQgOHNAbiaSxfl7BblEqpHsdMRxbj5BHiWcaAMnBdx852axmOdxTIpTsGkeSjGz6rWPtIOuqri99Xfkw9XofutBxGTiYqG1xSEgwJ2zsIyC7VvRxv9g_nB2lVGi6stgT4QgneveFUc3_jJBmyUTQBl8zcDexJIJEREc2ZK35GO1HW1V9sSk7cOI12kqx3eZaCPtzo2vUm0kcEfoMas21fub8Qsl6gBzshtQAt0IQfvPlEojCv4cjgMwjUI_ikXZG7LAbxKa9v7fbzSeNPT-Hk1ho_Ckwioyv3_H9VcjZ1ihodEMIOEjcXeGuJVcfzsozNcZPJM1bst6gDE05sA19oKjjJoAO-xxoA8Rsd70_Y4rlemKLz10TtZqvLzdC4630drQljhFuDy6kD8dh3cN-uDJRBOdS2M6fbkg_IhXJIc0F707NlRnxzbdU00-qWtejGbveLT0ubCSgahY90eb7AmU2E4R1HgyhElTGEZqL9csSy8S72X_SDKn4tun5gDaJXrDB-9CTiUJa5RRTvVaKUtV3Sk0DKOq0BAZ4qkaTrTayIotORbqhTR-9BzHZPCdRCBtIIq6IK-MnbSJxgp6E" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=Osnc4mfG0lwHjZvx9aIOnvMke8uyl0zQ9Jk1WIDPudZGlR8pFbpCia3eH4Dx8XyzrycdF8G4cbCUAULHdBuUDTBpQgOHNAbiaSxfl7BblEqpHsdMRxbj5BHiWcaAMnBdx852axmOdxTIpTsGkeSjGz6rWPtIOuqri99Xfkw9XofutBxGTiYqG1xSEgwJ2zsIyC7VvRxv9g_nB2lVGi6stgT4QgneveFUc3_jJBmyUTQBl8zcDexJIJEREc2ZK35GO1HW1V9sSk7cOI12kqx3eZaCPtzo2vUm0kcEfoMas21fub8Qsl6gBzshtQAt0IQfvPlEojCv4cjgMwjUI_ikXZG7LAbxKa9v7fbzSeNPT-Hk1ho_Ckwioyv3_H9VcjZ1ihodEMIOEjcXeGuJVcfzsozNcZPJM1bst6gDE05sA19oKjjJoAO-xxoA8Rsd70_Y4rlemKLz10TtZqvLzdC4630drQljhFuDy6kD8dh3cN-uDJRBOdS2M6fbkg_IhXJIc0F707NlRnxzbdU00-qWtejGbveLT0ubCSgahY90eb7AmU2E4R1HgyhElTGEZqL9csSy8S72X_SDKn4tun5gDaJXrDB-9CTiUJa5RRTvVaKUtV3Sk0DKOq0BAZ4qkaTrTayIotORbqhTR-9BzHZPCdRCBtIIq6IK-MnbSJxgp6E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p6bY-Nz21IePaRngIYvhPQMQUQyH2wzIlURYA1meG6Qm142RpyDW_fhs541wpa_mRUWbWyPZJMj7ae1cDx2zc3wi61vSS5K1bZftAc2sCVKBaib0MaBAyTEoOh8vx0xlHA04sriNo7MbyrpkFIzhHs6dbJsjLYZjJ-y9JBqqai9I9gjG9idHJQxKi1g3kgx6ws8INr54D1FLVwt4urt0cBaA-GXGS7M8PrcBuOz-mxvqKCWg9SxUP8qrlywef07xpw8xLHW8WpMKepM2IjjCGhS1igheU3gP5asWCGZ2Iq5iefu6ezGPgXkyfSm0ZLejVJsYs6qGjI5t_eqph6H9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYiOhz4JU6ndiK0z8A26IXXNh7EXS0brChPGKAqKL7x_dgu6Q8BZEnZcA-1lt9wq4ZqRdonSVWqZ6j-m80eyz_JurqigmcW0QpT7PxpRPO4GK_jKfTNMxisM69ZPK1FLM6DUFOlE75HTpode5QKhzKTA2WePRJo1WPngnRlc1JbbnshNkgXwAhWawkSAte9TEq_g_Ky3jI9FqVAq_6F6fQN72kC2JKMGBD0uMJ7xOGOjTn8LH1gYt82eS276ZGvsO2AfUfTVsLLL2mD6YwUHTvYybbF2tYC5tQTSZ3eUdjyB3TdHYe6vzFHmq_RSO-d1TpG3-Hw0c_EMZnApLEDygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O8KLbBwGlDXiEPCbHbfUMy7pm_Pr3q_Kn4KbJ--uYZGwjctmR9jeEIvgbLb80qx2knWExNijChSCtF7XytBHb033oFT7dA-8kHBbHn77bdEiCGFJINZ-XLLTfx68ts3tkCJY1NiPEkFngcqREJpNIlbc74nD6YBvkP0nF9tpasH6gy8sqLRYtPkpU28_jr1rfn6RrZJ52cFEF97J3QOWcVW0NYG7Me7k1WcoztdiX1dgOb7vrrCHWJBERs1W-ywh3u7eqics3gSteSLpdxzyl_i-RBnSBaEMXXOLbYRzbp3CLJFroD6WBD35oKBvGKydKaVlK_y0CTAk31EQZxaU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4TLEq7LtMlKTR2UGcQ5IBaZOj4coA1O-y7ogSkmV6N8wTsmGwpeKCjhl4vOVS5trGxURKnBfhXivYwegfPWjXJXgSOFFMh6BgEwnUvw3zxGb1vgmOnDYvdKGp4xdUN6eCZEhXq2dXe5R0wlTAYeCjoT1argdwefVnTifdQPnbhEvqdfyQWvMsOEp-SB5MUbyZPCBhPlAYrA7WOoMb7lF3HPnkH_SSc5E-71vCuuaTiMx8cbvU-2ITOLB9o7jzk6VF_-s7KXohX2UdUrVHV3cfC4n68aK8RiyXAKwGDO0elORcK-0uzwgnWji2KIV07u-RFM_G-vF9lqvcMnO4YLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lTw0X5MCGVtQyh-EbTbZLZ4cJCpZJzm1fONmls-9_2b5Ax4AeIa9jshOx8Yq6ga66V4Qe1SrAkgWIHCjF4EbtI1lRaplfH-YDfAmklYFCWlm46nVsAa_InR5RyMLzpEfG-XgVzsMDTKg-0PFWSEAqSq-0fnUbulQeGtW815AT_62RLLmiFo7rn6J3-gXmEPpWUHkC0UL_YU-ccTkEjfY-1W_0X5S4elAzRuT3o5Ozz-BFmHP7MFdUm52FKQWCdWbopllzywa2MHoWbDSodaeG4n1rVPw3jdM8pzvYYfOjc1ap07KRUlqDOlMlYd2EMjrlAEdPZ1BopF647pBFYLFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KWcIVagGdQYRqX2wnL6yFE78p7I_nJMW-9YhskTH23oDVsgI20XGb6shmFCCj-hGL8wPNwOLkkpJAwJPCfIh9iiIRikJdhMvehTYqevBvxel2ljJt29WPSuN5MRphxL3puao8L1VKeos3fuT0YurYbV002eYOqc2_5186TtPa78PV4ttA4Q8Z4nXQiSOpCEXEXF29k7l1Fw25TEhGf5iJiTW_1RpaHFTdbS6gVUjgSId8OgQXPIGeycpqHyv4TG9-Bf6TAfIzZsnfkZZ_nJC9BEeBbUHwDPl60QvRaTPfMfBWr9cSYHuV7TbZfFIDCq-3Mj5zyb8I7LEQwzFLRmSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سایتی رو برای ایجنت‌ها به API تبدیل کن، بدون Browser Automation
💪
یکی از توسعه‌دهنده‌ها توی ساب ردیت هرمس ابزاری به اسم
agent-data.dev
معرفی کرده که ایده‌ی جالبی پشتشه.
حرف اصلیش اینه که برای خیلی از کارهای تکراری وب، مثل چک کردن قیمت پرواز هر روز صبح، دنبال کردن آگهی‌های شغلی جدید یا سرچ توی یوتیوب، browser automation رابط مناسبی نیست. ایجنت باید سایت رو باز کنه، بفهمه چی روی صفحه‌ست، هی کلیک و اسکرول و اسکرین‌شات بگیره، و هر بار که لازم شد کل این چرخه رو از اول تکرار کنه. وقتی کار در اصل «این سایت رو با این پارامترها سرچ کن و نتیجه رو بده» هست، خیلی منطقی‌تره ایجنت یه API call بزنه و JSON ساختاریافته بگیره.
حالا این agent-data چیکار می‌کنه؟
1- یه کاتالوگ از APIهای آماده برای سایت‌هایی مثل X، Reddit، Zillow و کلی سایت دیگه داره
2- اگه API مورد نظرت نبود، URL رو می‌دی و توضیح می‌دی چه دیتا یا عملیاتی می‌خوای؛ خودش API رو می‌سازه و نگهداری می‌کنه
3- از طریق HTTP، MCP یا CLI قابل استفاده‌ست، پس برای ایجنت شبیه یه tool call معمولی می‌شه
نکات فنی:
😟
به‌جای HTML selector، endpointها رو روی همون network requestهایی می‌سازه که خود سایت برای لود دیتا استفاده می‌کنه؛ برای همین با تغییر layout کمتر می‌شکنه
📱
خود APIها مرتب تست می‌شن و خرابی‌ها خودکار شناسایی و برای تعمیر صف می‌شن
💰
زیرساخت proxy و CAPTCHA رو خودش هندل می‌کنه(باید برم ببینم کپچا فارمش چطوری کار میکنه)
سازنده‌ش گفته قراره نشون بده این روش در مقایسه با browser automation چقدر سریع‌تر، قابل‌اعتمادتر و از نظر مصرف توکن بهینه‌تره.
🔗
وبسایتش:
agent-data.dev
📌
ردیت
اصلی پست
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=N75u5JzqIfzV9wfLEaGO86yBhVUIlkKGiOG_sAuSXqCUho1WEj6ZD-R5TLun_MpxGYnhw5LMzEW6o9kDvugMtXRIl7ezNGh-qaS2L63a8VLoY6pqBUzcohynDP9YMBQ1GacHL5zDdU0BjoiBGnSZjkOLu-TuntV9qz0bNOoor0CWPOB9xrF33j5bEkQvdX7LjRrDS_r2KwWNXu8BPHINI9R5nq0LxYLsqNSbECuUTd03TKF9z5_3p6jPhglJpSPZ6fNOoqJkaWaYQRwK-ZJH0SC6DfXnGTLGMa09pIuIzG6o3kQzr_gJfPiQHq0nFn6ll3fjE5_JjUXXmuK8OQItAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=N75u5JzqIfzV9wfLEaGO86yBhVUIlkKGiOG_sAuSXqCUho1WEj6ZD-R5TLun_MpxGYnhw5LMzEW6o9kDvugMtXRIl7ezNGh-qaS2L63a8VLoY6pqBUzcohynDP9YMBQ1GacHL5zDdU0BjoiBGnSZjkOLu-TuntV9qz0bNOoor0CWPOB9xrF33j5bEkQvdX7LjRrDS_r2KwWNXu8BPHINI9R5nq0LxYLsqNSbECuUTd03TKF9z5_3p6jPhglJpSPZ6fNOoqJkaWaYQRwK-ZJH0SC6DfXnGTLGMa09pIuIzG6o3kQzr_gJfPiQHq0nFn6ll3fjE5_JjUXXmuK8OQItAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aD-CijuMD9W8gqnSIuBEToCXLoeH20F9DT1jiKUbEIO_msJj8CUqD059YrjEOYGlbrJ3YjA3o4ukpICiV3mQ3YzEdU4SDDi2ej-Yxak5m3xmTexdqhFCpo_H1WEnDdo3dpBzaB0qCkuYJsjtIg-edFQB1h8w05NDD034lwxr-zvWn5y9kgvaPPVSGd28gRc6xdgyqcuI-zNFGwu_EQwIPjY-e0MxmkFBrsXWQ8oZukNR8ypXN6hya8eBsjDH0xh2iN7Lg55sgCCEMIobevc1S_ZRoDe7eYLm4Iy2RDmGF0oXCbMv9d8vg9KU7sYkcnbldSgUfjluNyJaZUyJuBv9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wsd5qowy0T7o__nn75sLTJbB7kv0UpdTKEaq7OElVlyM00gW4yEe4e2cChN1i56ax40wPS52CeMMAkLWQHyuVCEeOdbDpOsfMh7wbDgp3uTQIC89pXiItysrLPW039aLh6NSzYWd4eSQxmpAbmSuOEGR0EzjpMs530LKoU6RYdYm-KQHxXgAkAQ1xk7OtP5gBvdwOnHq5356givI7Qei3UyazhDMzWNrS4-Gngqm68ITqBszB1czKqxmTwAIG6g7zKTw3hdxpDideTKIMkb_qfcRNVgQH-18vxQvxKP0LLUNmQUTB00JNLboMUYNRx0Uev-rebNJg4ceIQoB0avtxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/soyhZiNq8nHHYheKYYhKG95DxM5-PAQnwSaRiDD7espvObHgsKummEG7jVNJRCIxHUfJyGL8bcN_BTV_XGeK8Fw8lnInRFrE5GmueFzdOqEWICNBPgeiDlj8jVFG-4VX1EDikDG8K5mR-oMCvtCp5pIIL6gAEdG8YhZ0Y3k-tFu0YjzTzHftpE75u65KgOnt3BA9EWhrKGakNqYWzFOMbf5rxbXOS0GEMOv8_TnbU9ZgkJWpqF2HXP_Tmr7vb816YAAP0g0bBvA6HbV6fDj1cUiwBFh7F-c_vmSMEcCY5CfQjKGWKarAYFPsImPcVjkiM8SFZtxPmSdiP3cAH0UvoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A_qdgIrTQk_E7oLFKxMqMudGOWR4FtIF7FvustEBHMWhjN67ITDQH9TQK3wHa4vp1FluEKcVZpoRaiRjImSduVdPH7GLLh6PFnAxCLjznqd5ehUPVhXJPy9eCOL1G_YmZRS_mz9ojcz_i34HWIQc_gnrVar6isrTzjAtrITK0IqD_nqG3mUchHopR2ncQOw__SfzEK1RDPxA_779Fp6IBWy_I51ilsRCLWjV2i-F50AmwVAa6x_tFQuQk_I0hlH8R3ZPLVzU45F-WEq4ipuRRDznod6X2Pm-VZUzbJaa2Y7_Fmay1BIWCQ4269ExYlN7hTaxrJ_SV09ov3Z-zpHBaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اروین از توییتر
یه سایت بهم معرفی کرد شبیه به Mpay، اما بیشتر برای بیزنس‌ها یا کسایی که تراکنش نسبتا بالا دارن؛ با قابلیت برداشت مستقیم از کارت و کارت‌های تبلیغاتی برای کارهای حساس مثل تبلیغات گوگل ادز یا تراکنش‌های سنگین و گرون
از اینجا می‌تونید ثبت نام کنید:
https://finup.io/?code=MATINSENPAI
لینک، رفرال هست. اگر دوست نداشتید میتونید کد آخرش رو پاک کنید. برای شما سود یا ضرری نداره
نقاط قوت:
1- برای ساخت کارت، MasterCard داره به جای Visa(شانس قبول شدن آفرهای رایگان معمولا بیشتره)
2- قابلیت برداشت ازش وجود داره به ولت کریپتو(هنوز تست نکردم که KYC می‌خواد یا نه اما توی مستنداتش چیزی ننوشته بود که احراز می‌خواد یا...)
3- آدرس BIN آمریکا داره
4- از ارزهای مختلف برای واریز پشتیبانی میکنه برخلاف mpay که فقط تتر داشت
5- دو نوع کارت بیزنس و تبلیغاتی(هزینه‌شون یکیه) که کارت Advertising شانس پذیرش بالایی برای کارهایی مثل تبلیغات Adsense گوگل و تیک‌تاک و متا و... داره
6- کارمزد رایگان روی برداشت و تراکنش کارت‌ها
نقاط ضعف:
1- هزینه اولیه ساخت کارت 10 دلار هستش
2- برای KYC شرایط ثابتی نداره اما توی تراست‌پایلت نمره‌ی خوبی داره
3- حداقل هزینه واریز به خود کارت(نه ولت)، 50 دلاره
و اروین گفتش زمان واریز مراقب باشید از صرافی‌هایی که امریکا تحریم کرده نزنید. ترجیحا بریزید توی تراست ولتی، جایی و بعد بزنید به ولت این سایت
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZx49ASuHpsNxByIzvwZYYVUaC8i89LbV6eON8vQ7Qyue-5ZgRQRzEr6Npzoc8Z8OfPZzyLZwee85Kd8VMsNxKxfKfBdUJR7U6q0PoJoTCSytFM48KMU59Xi6HGE96f15Pz7H3dKx-_fnX6_XlTA3IjYwt-JLgo1hblTtITK_AhjEBlt1LwQ79IW6r_YpQM8z__PdI30DXONhY1fbEo_l91fAW-GsrnXshIKCW_1XHyLoYkm7UY0uWo58BK8rPq4JGvrbxrQ46FDsYezQOPpeJ1jf-nq2iws-5775nLa_Ov3jOOSJT6Zc1i62WZnf86tf_oIfTldRQthfXRCAWtKCfzE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZx49ASuHpsNxByIzvwZYYVUaC8i89LbV6eON8vQ7Qyue-5ZgRQRzEr6Npzoc8Z8OfPZzyLZwee85Kd8VMsNxKxfKfBdUJR7U6q0PoJoTCSytFM48KMU59Xi6HGE96f15Pz7H3dKx-_fnX6_XlTA3IjYwt-JLgo1hblTtITK_AhjEBlt1LwQ79IW6r_YpQM8z__PdI30DXONhY1fbEo_l91fAW-GsrnXshIKCW_1XHyLoYkm7UY0uWo58BK8rPq4JGvrbxrQ46FDsYezQOPpeJ1jf-nq2iws-5775nLa_Ov3jOOSJT6Zc1i62WZnf86tf_oIfTldRQthfXRCAWtKCfzE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=LAgSxLclDj6M-driFLnTM4VNJU3psNB1ctDqFGTgJnhIg8fs4qcI5w0zKF88UHJK5MebFocYo-DyH2_RGql6G8fFGG6IYdh9eCE4716hqXZEP4vP7ifbrZKhyMmB5neZNuQs72vjX8LltrwcW1wyDf0jOj9h7FNwXpPEV6MpiSt7uJbJxm4Ub1Vv7c0EpicfIwsw0UbPd_KgIqzRrkKnjQMCQtBrqCmEf6VXcPQ4Miyk8f3FcfOeO4ScwcTPgmQDHGuwRH8w-8DFheztakghhJ0aaq8FnW_pH0uDi-3J9NfO5RY84AYFEA5mY18igjNmb7Q_Y89a3Va_6ug9HJgBDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=LAgSxLclDj6M-driFLnTM4VNJU3psNB1ctDqFGTgJnhIg8fs4qcI5w0zKF88UHJK5MebFocYo-DyH2_RGql6G8fFGG6IYdh9eCE4716hqXZEP4vP7ifbrZKhyMmB5neZNuQs72vjX8LltrwcW1wyDf0jOj9h7FNwXpPEV6MpiSt7uJbJxm4Ub1Vv7c0EpicfIwsw0UbPd_KgIqzRrkKnjQMCQtBrqCmEf6VXcPQ4Miyk8f3FcfOeO4ScwcTPgmQDHGuwRH8w-8DFheztakghhJ0aaq8FnW_pH0uDi-3J9NfO5RY84AYFEA5mY18igjNmb7Q_Y89a3Va_6ug9HJgBDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v_vKrcbJvPFfUmzDvJuGyLeyCboxZBKwrnf8i9bHn4tTIAF4U18jSbJ0VmtrBAZdlE3IHmogtLF2V2BsI5FEno_6VwX2tFr5sTQmEbV70VuV2jwGdMwzHUVnkOSNn4DSFeclKOwff7qJgFN7eF82B1RjNNbjNKc-6Sl8IHB_x1YWx6Ur2e3pHcs7mQyVK-wBhgYKQEWoK_MRHu2Mc-CmIp3oLaED0q9rGswT-GgZQPp3Jw-G6mpZZv48cx_-AIA10cLqVD_nH4rGbuhvO84IDHxQoCg-UcAQd7Yu6dVaTKJUXQN-GXdI5uwfMVjDTUPdoJUa-b3wyMLM3s56-LwVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MrNRnt9giHd69FqQk-BsEQU7fcuJPGmOSRhERbsDqIua0l0rzaA8dfklHylV-8hh0GyG_4Jxm-rvrJaVv6VkKTuVb0tuyYcTMZlAqEI-K2h-9wXb9QepUK8H6JToNrKAPanqw00X1LRyaQEmy_R4YrJMp4fdaULHiNThbWuc_qUw0R2RdLIe-yoi9IzEKXVH7k4hPUa99i5yMKTONtPWTOwYkh61PNhtpqy5eIjezmYlNgEJ3gRFQsGJLqpD3DowL-XtqOp8ULwYtQ6x4TDmYY4f85YW1w-K11dLYWAyY8JmcwfTc0ilcRavG5ghxqYhVGuRySs8eU28dSu8SetLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">زبان‌های برنامه‌نویسی توی عصر AI چی می‌شن و چه بلایی سرشون میاد؟
خوزه والیم، خالق زبان زیبای Elixir، یه مقاله‌ی فکری نوشته درباره‌ی اینکه وقتی ایجنت‌ها بیشتر کد رو می‌نویسن، سر زبان‌ها، ابزارها و کامیونیتی‌هاشون چی میاد.
چند تا نکته‌ی خلاصه از صحبت‌هاش:
۱-
کامیونیتی:
هر زبانی دور یه سری سلیقه‌ی مشترک شکل گرفته؛ پایتون «یه راه واضح برای هر کار»، روبی «خوشحالی برنامه‌نویس»، لیسپ «تغییر خود زبان». وقتی دیگه خودمون کد نمی‌نویسیم، حس تعلق به این کامیونیتی‌ها چی می‌شه؟
۲-
اکوسیستم:
فاصله‌ی اکوسیستم‌ها کم می‌شه، چون پورت کردن کتابخونه‌ها یا پیاده‌سازی الگوریتم‌های یه مقاله با ایجنت خیلی ارزون‌تر شده و زبان‌های کوچیک‌تر سریع‌تر به بزرگ‌ترها می‌رسن. ولی از اون طرف، وقتی ساختن یه کتابخونه ارزون باشه، چرا کسی بیاد روی یه کتابخونه‌ی مشترک همکاری کنه؟ خودش به ایجنت می‌گه دقیقاً همونی که لازم داره رو بسازه.
۳-
سینتکس:
سینتکس‌های خوشگل (مثل optional chaining به‌جای چند تا null check) دیگه اولویت نیست، چون ایجنت از boilerplate خسته نمی‌شه و از دیدش همه‌چیز توکن ورودی و توکن خروجیه. به نظرش زبانی که ادعا کنه «برای ایجنت‌ها ساخته شده» و تمرکزش روی سینتکس باشه، داره حول محدودیت‌های امروز مدل‌ها طراحی می‌شه.
۴-
کامپایلرها از بین نمی‌رن:
اینکه ایجنت مستقیم اسمبلی بنویسه منطقی نیست؛ کسی نمی‌خواد برای هر معماری یه نسخه‌ی جدا نگه داره. تازه هیچ زبونی توی همه‌چیز خوب نیست؛ Rust، زبان‌های اثبات قضیه مثل Lean، Erlang/Elixir برای سیستم‌های توزیع‌شده، SQL، هر کدوم تضمین‌ها و سطح انتزاع خودشون رو دارن.
۵-
تضمین‌های قوی‌تر:
اگه ایجنت کد می‌نویسه، می‌شه trade-offهای زبان رو بازنگری کرد. مثلاً type inference برای آدم‌ها خوبه چون نوشتن تایپ حوصله‌سربره، ولی ایجنت حوصله‌اش سر نمی‌ره. نوشتن صریح تایپ‌ها اطلاعات بیشتری به کامپایلر می‌ده و دست زبان رو برای تایپ‌سیستم قوی‌تر باز می‌ذاره. به نظرش زبان‌ها در آینده با این متمایز می‌شن که چقدر تضمین می‌دن: از طراحی‌ای که حالت نامعتبر رو غیرممکن کنه، تا تایپ و اثبات، تضمین‌های runtime، و تست و fuzzing.
۶-
دیتابیس برنامه به‌جای LSP:
پروتکل LSP برای IDE و آدم‌ها طراحی شده و با فایل و خط و ستون کار می‌کنه، که ایجنت‌ها دقیق دنبالش نمی‌کنن. پیشنهادش اینه که اطلاعاتی مثل سیمبل‌ها، رفرنس‌ها و call graph به شکل یه دیتابیس با زبان کوئری در دسترس باشه. آدم حال نداره برای پیدا کردن رفرنس یه تابع کوئری بنویسه، ولی ایجنت راحت می‌نویسه، حتی کوئری‌هایی مثل «همه‌ی مسیرهایی که یه مقدار می‌تونه nil بشه». برای همین هم جادوهایی مثل monkey-patching که کد رو غیرمحلی می‌کنن، بیشتر مشکل‌ساز می‌شن.
۷- در نهایت
Observability به‌جای دیباگر:
breakpoint گذاشتن و خط‌به‌خط جلو رفتن کار آدمه. ایجنت می‌تونه سریع کد رو instrument کنه، trace جمع کنه و اطلاعات رو کنار هم بذاره. پس باید runtime و state سیستم رو جوری در اختیارش بذاریم که بتونه برنامه‌نویسانه کوئری بزنه، حتی روی پروداکشن. اینجا هم طبیعتاً یه اشاره به Erlang VM می‌کنه که این قابلیت‌ها رو از اول داشته.
جمع‌بندی خودش: زبان‌ها قرار نیست از بین برن، ولی سؤال اصلی عوض می‌شه. اگه دیگه برای «آدمی که کد می‌نویسه» بهینه‌شون نکنیم، برای چی بهینه‌شون کنیم؟
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtYd-m72MIsbjR3Muf9z8b-_06I9lFTaNEB4ppw6e2o5UDT73LHXrPm6hgYFMkD_JxF_iZa2-OlYxXYWLumOMfvafP11LjLCqInPuORj6uF1MMvMhDksu95VGdb78W-0k6JXFVPZTXhq_xrY0gH2GUmyRpxKtqrcZzJesTpxmfuDeqff9DXicmcN4Ch58xknoVABVJtU31gzsILxDcRyTBWnlakMzkzJ7-EUJpeEx317_Evmbv9A_2TxMaGnnB-dcUYieLt6crJfT8inn4oYmnLnfS3JfrfCl7dGvM_3k5oqGZ_ez7X8PPvmNsUX_V7x4hhEXMQaPNLWPDam5ZQAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت
توی 18 دقیقه
هیچ ابزار خاصی هم نصب نبود جز ffmpeg
و اینم پرامپتش:
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
که یه کم بالاتر داده بودم.
روشی هم که ساختتش اینه:
۱. هر فریم فقط تابعی از زمانه
کل ویدیو یک فایل HTML به اسم showreel.html هست که یک تابع renderFrame(t) داره. این تابع زمان رو به ثانیه می‌گیره و همون لحظه رو می‌کشه. هیچ حالتی بین فریم‌ها ذخیره نمیشه و حتی موقعیت ذرات هم مستقیم با فرمول از t حساب میشه. به خاطر همین میشه هر فریمی رو با هر ترتیبی دقیق رندر کرد. تیکهٔ «Rewind» هم ساده بود: فقط renderFrame رو با زمان‌های قبلی صدا زدم.
۲. حرکت‌ها از چند اصل کلاسیک انیمیشن میان
- Easing: فرمول‌هایی مثل outExpo برای ورود تند، outBack برای کمی رد شدن از مقصد و outElastic برای حالت فنری.
- Squash & stretch: نقطه موقع افتادن کشیده میشه و وقتی به زمین می‌خوره پهن میشه.
- Anticipation: قبل از جمع شدن شکل، اول یک لحظه بزرگ‌تر میشه (inBack).
- Stagger: حروف و ذرات هرکدوم با کمی تأخیر نسبت به قبلی حرکت می‌کنن.
- Motion blur ارزون: به جای نقطه، برای هر ذره یک خط از موقعیتش در t - 0.02 تا t کشیدم.
۳. تکنیک هر صحنه
- ذرات: کلمهٔ «FLOW» رو روی یک canvas مخفی نوشتم، پیکسل‌هاش رو نمونه‌برداری کردم و هر پیکسل مقصد یک ذره شد.
- سه‌بعدی: بدون هیچ کتابخونه‌ای. چرخش و projection پرسپکتیو رو خودم با فرمول ریاضی نوشتم.
- مایع: با metaball ساخته شده و داخل یک WebGL shader اجرا میشه. هر حباب یک میدان r²/d² داره و جایی که مجموع میدان‌ها از ۱ بیشتر بشه، سطح مایعه. نورپردازی براقش از روی گرادیان همین میدان حساب میشه.
- جلوه‌های نهایی: یک shader دیگه chromatic aberration، grain فیلم، vignette و فلش رو روی تصویر اضافه می‌کنه. شدتشون به ضرب‌آهنگ‌ها وصله.
۴. صدا هم کامل با ریاضی ساخته شده (audio.mjs)
هیچ فایل صوتی آماده‌ای استفاده نشد:
- Kick: یک موج سینوسی که فرکانسش سریع پایین میاد.
- Clap و hi-hat: نویز سفید که فیلتر شده.
- Reverb: با چند delay که بازخورد دارن ساخته شده.
- Sidechain: صدای بیس موقع هر kick کم میشه تا ضربه‌ها گم نشن.
- زمان‌بندی صدا با تصویر یکیه (۱۲۰ BPM، هر بیت نیم ثانیه)، برای همین همه‌چیز روی ضرب می‌شینه.
۵. رندر نهایی (render.mjs)
اسکریپت Chrome رو بدون پنجره (headless) باز می‌کنه و برای ۹۰۰ فریم (۱۵ ثانیه × ۶۰ فریم) renderFrame رو صدا می‌زنه. هر فریم به صورت PNG مستقیم به ffmpeg فرستاده میشه و ffmpeg اون‌ها رو با صدا به MP4 تبدیل می‌کنه.
۶. کنترل کیفیت
وسط کار فریم‌هایی از هر صحنه رو رندر کردم و کنار هم گذاشتم تا ببینم. صحنهٔ سه‌بعدی زیادی کشیده و شلوغ شده بود، برای همین طول ردّ حرکت و زمان‌بندی تبدیل شکل‌ها رو کم کردم تا واضح بشن.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vKXFAJq30Ev-ur_eEbMMurV_5O-aUBXd1sYFiH0BZ6PXXbj4Fcn_jha4ZrcOR23z9onViMoAbmeCS3LHphcm-4w0w6x44aTqD0FGUzfl561nN1Xf6vImA5Q7cZaO5q9MhUewKHaFN9Ur6PicRc37RyWBWHqqwI-2zY4aHIKUI5t0zlrrK1XmueKCCu-CtuymqUZB_79ZVfVfETH3oLX7U6SGhfRDQhHnwlg_LD08x8axCvADf9Dwjal67hNtNLR4QgocaWVn91l4tsLgDg2j3I60rF6JgQNB0nbuAhu7bYxauhL3YswLoRdGXFuYFcJ7CjNAT8VMa__qr3wh6tGQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsB3sOwP8OBocqWYiADHYCNKOFl7eiQnjeYoEdEWOZ3R58ImJfIOVDvPiTXaiJJ91Du8qQvB8HKaaltJu-jNcvcM0UPeZubmeV4WyGaKJiZmCgwIsJLGDIvT9bXE_7_lwgQVvk0Gzyxro_Z877nR6y5618EgELTkemfa5xdtENAQNHmUQocX-BDnZO0GEnw0z5cbaAwtkfd_ZwVq7x4Fh8iiOVeOplM58cUsdgzirrVeW0caZ87YOgXnVWR0NmXJ056MBnIfqVC4tpZ0npHQEt-nj6F2DXOFtgHwK3bkqPxlvdwIHvkM865CbM-EOUzBFhwsishV9w8Fw33_3YxIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQENFA4l_OegXKAnSESMDo0ncDsUjcZq8VDkhphyYhCKMQVgOnmER3Ik__XrD8GE0yPgJO3MDmed5cJvF4v2ufXRFqQ2oBCisBShY3pJl7z7xVqqoR69kGyRprxuLHvz2ADzd1kk1j5ZLuJwwq4kcUz0l8bxn1of7SRjGCWRjJA67itRrlg2L__0cZ1OMf9GwUglFcqEL7IcnpB2BXqpozDClpln-ot48bkSV--BMZmk3fn6MbdzVqvjKn2mRiuWabEYpxJa-DsOYRLJTu6BSVo9g1HVFZ4dkMQtzO3tjgtBSmKaX1i0cRgV1TDBQspt0cNyY3VI4B5mWf4IFiCzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agYMMDBLh93bufGEP06JGz_gxTeIL9HbacvKnonHX3pvWiyPI8dwX9GgYFDkzzh9B1Ly73gCYy3wmke7_RjKfmT6x2up0rVvLxa6NfyNjUjrtAPRf4nQfLV5_bYZ-wiC-JMOqg8BrJgiuuWeRv7eeiLoj5nKgoxUFoIi_6lXrz3m2k50C5yD3H4-3dlRcUdM5Cn6CRxvNNWuWdpg71_vmPIaC1Dn3VBV7IWCNbSjrWW19mitwWfKikMA6JA6ASN0bMsjYTHK36XCClraRBpIunDIe1fxsBNtw7U8VGjDpEe6S0VPPSD1qFFVHqb6DDoEoV7Zfed3xQe8fOhm4KwrYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X_DTLSqwjcQ4xMBQYWf4d8zRhPPVL7EXaB3GgvXHhHBxz-pu5xH7-X_-goYMRVQnWXMj8uL5SXA9hIB0DoZnU1cXh1HC4_7kwEGgYLoWGAV5Iu0CjumC5R3hakGK502u49mqShnJMUKCbX-_65oJbYm_oXIsDOqrVGmVZIY9tDvn637TSpqWyBa5o2PndcsWofskZkx4i9w256Fvv0Cqh1Cp1o9l-JCyaV226MdJFN1-TcA9WfahW51x0t9m-1nm1kHwByTscM6YmSRhwdnXbEntWMv4JteRiVPVuaR7LUYrNICkax67WyLIAN6Y2OLHHgKbhYSXxfEultS3yz6K8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
