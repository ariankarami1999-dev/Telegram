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
<img src="https://cdn4.telesco.pe/file/Max4xZCaw2eu5CrsAEMtDcsIFEwbGh2jBREciEy66DkSj-2aBeNQqpcHuIcrS2VtjgqtT6BxfwJF3gPv20BVVNF-9HOiibPYeBaTWT29bsXmVl_ukHSCcTac0DCz0zWiQ6s1-Per4TVXbO0SawLoN_L2O_fvy1_WLKQiut8cE0JHPNvqyU6aRoz12InSxvVmcOo4TAXcsRJ9LRN-A6qWHdGJsS2mRJViFO9fs_obcGZlqV7yXdmWLYcQ-E4DpAJTBi5WIptMK9CNVVFAPgQNjBsv-xvQUXI0Gxi4EsYQrQ-6Lo6t5aa_W0dz7Wimk55u0hy61tdSvpo9RAeFI99ewg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 03:38:05</div>
<hr>

<div class="tg-post" id="msg-73033">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/news_hut/73033" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73032">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nv4eZH_RgIvdfNm2ApVA3vKrywhnnVJlKNW-dcKudEgRRkzqaKaZI_u6B8cDOd3vugH3geh1G2Hl3D911nRKbEsO2yYpHN3_PFhgdnS66Bq_Gg7R2ubmLJP0M2svvZnSTYHIZcSLBbhcOUlx_oKRHJFjBTFCtBiW29H5Zde_f73e0dQP8kiDDnXoJU83PljxGsxNHZZJ0Du57kLn9bfncRP7v2WSxS5WmdgQuUQ5vjmK7QCJWdBT5bOirfKWoHclfV3spRFvdjrzHRDxjb5T9sI2yrG7fA7afEZeL4wgzh6tgkjVQUhjaENGLuTyeg6JQq-UuD3vvQA1DhVttF_pTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/news_hut/73032" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73031">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=nvg13yFT1plaQNUn4azmnu7E1x9wugsQqMsT9KVj8-_lR-MweIrSLeGlomEn5i-I4Hs4WeBAsCJ3iABpbcYcg9ewgKKTsTKk-d7HRglRp1Qwg1l3_RqwBpitkU6An4yabknu4f_IPFuPezmMuzR0P8MsijqYPmQ-RKTXNBMPnarfgRSiCx83Teu8wYCGyJNXLcIPsykoRSLcNWLCfJvNj6EKbTYWertLktO6BWQ-ObL8YQbbFvoCodC9-ouAIDlDz0osL9POEv1AsAtuZvdtWcQKvWhQaGkzmB6_IEjs7npIWZq_Ch5JKpgGYnpiOMV9HEOK2bxhxrQ7yX88OnO3gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=nvg13yFT1plaQNUn4azmnu7E1x9wugsQqMsT9KVj8-_lR-MweIrSLeGlomEn5i-I4Hs4WeBAsCJ3iABpbcYcg9ewgKKTsTKk-d7HRglRp1Qwg1l3_RqwBpitkU6An4yabknu4f_IPFuPezmMuzR0P8MsijqYPmQ-RKTXNBMPnarfgRSiCx83Teu8wYCGyJNXLcIPsykoRSLcNWLCfJvNj6EKbTYWertLktO6BWQ-ObL8YQbbFvoCodC9-ouAIDlDz0osL9POEv1AsAtuZvdtWcQKvWhQaGkzmB6_IEjs7npIWZq_Ch5JKpgGYnpiOMV9HEOK2bxhxrQ7yX88OnO3gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/news_hut/73031" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73030">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBo2oJgNQUz01zVKXR0i7N_yslb6jVuKuN0leFzgw617RBWcX5SlFsc4BBjhqAC6t0tRRHq6IYS7NcNPYl_VmsXvZTFoqTAc5C_ht_5yuo6N8EFBxY_pm0IOpJK6riQerS8E4W1N5pt3f0C4W5z8ztmYmp96konlqIJ1cy1TutmUL7d3YFCem9A2-HP4te245fTFqKmXruQkFfKy5aJRhdqpUzIWdZs4ZsfkP640I8h8WFSUnCKA8oCcSAhDh87PKnlwN3cvTzgIb_mmcAeZRAUfXrXUDpOvdkEpqF13ses4kGiN3bUSnq62jgvWJSVdXUhuXUxviFjJkttL3s9afQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار امنیتیِ وزارت امور خارجه آمریکا:
به شهروندان آمریکایی هشدار می‌دیم که فورا ایران رو ترک کنن و به هیچ عنوان به این کشور سفر نکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/news_hut/73030" target="_blank">📅 01:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73029">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">از سیریک چندین پهباد/موشک به سمت شناورها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/news_hut/73029" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73028">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0925073180.mp4?token=JBUcUXzHoPr0Jpz22NL761H5g2wYKszSuynZixIdYgKs3kvOf-Z6dYb7pfEDJP1RGuw1TItggfPpZidZ5O0RW4bvUrE1xlME4pn7JOFLex9_zUdywI0HYnBVtO9JCwcsGL_xnoeaz9TK2Gl7zjhAYEfMgE0et7WFseutlCcjl9y4Y9oGxUJUgdkn6ebqVYOlBrO0AiS88j0UKznNSE67K8pZGAT6rhWPVp2EqhYquP_762XH9GcZfHJO4RhKFzaIgp4RyInrt90FXH8yjYFTHD4rSzkf_jsSKACNFqFHNux_g9TI0g0yINPbJp5YWJa4BhnxGLR8iP8tD6TNyvf0FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0925073180.mp4?token=JBUcUXzHoPr0Jpz22NL761H5g2wYKszSuynZixIdYgKs3kvOf-Z6dYb7pfEDJP1RGuw1TItggfPpZidZ5O0RW4bvUrE1xlME4pn7JOFLex9_zUdywI0HYnBVtO9JCwcsGL_xnoeaz9TK2Gl7zjhAYEfMgE0et7WFseutlCcjl9y4Y9oGxUJUgdkn6ebqVYOlBrO0AiS88j0UKznNSE67K8pZGAT6rhWPVp2EqhYquP_762XH9GcZfHJO4RhKFzaIgp4RyInrt90FXH8yjYFTHD4rSzkf_jsSKACNFqFHNux_g9TI0g0yINPbJp5YWJa4BhnxGLR8iP8tD6TNyvf0FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.
ترامپ: کی اینو گفته؟
خبرنگار: زلنسکی.
ترامپ: باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/news_hut/73028" target="_blank">📅 00:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73027">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=voV0ZOkkNwcj9Tn4Vz5mBFwEKY0IdpxA4jRhohChw8hIH-P1PPSg1n5OVw6EXnOBs_r8FdbOBS8eLdXeh958NUoSkD7m5WaSBJheL-ShTY0by88xiptRE5EUjISEK6SEDtDhk8vf8zJF0HKxKzx5pLn06bbb90CjzvV6WnKDY_JI3yARxYoOowNbka1206baic2dDvSoqX0qhTBs14mJ4uXhVAAYqj7aHYcGylQXh64urZssvKyQwJHmztGV_uLwG6mVUPJtKng0lmBtVqpT7qJFeiB1yebxCtQOozAygYDz6qB8V6k0a-f6etNXyZtzyPAGciEPmN8h_iM44mCq-l4GxzEEBGh9oYNEssSurIi85NGALyfqsO36M03aqB3TPfMpQ2ATpwacm-kouoVONX-Ov4GLgsRHADFP2xZz6R8f_rnpo3dT6p5ni_v6n3-Z7bL1Ucnhklws4vW0mKewPfzWRTR3rgMB_T4j4BI089e6Q0Wox1OnNmVydimQTseQorg4YEFa2WZLtCdK_c_8CBj_3S35sd0Tn6KfUTM0GT-9IHG-4slRofZCmmj6a2GYd3Ds3qTRPwtFh5V46gyl2lX8aaNAqQJ5wdwWBZw7b5k8TLy6s4eMssW8xpL7w9qfU8i-oEAVKhd6MgTRoWXKRNDkMM_eGrHvXieeZVBR4bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=voV0ZOkkNwcj9Tn4Vz5mBFwEKY0IdpxA4jRhohChw8hIH-P1PPSg1n5OVw6EXnOBs_r8FdbOBS8eLdXeh958NUoSkD7m5WaSBJheL-ShTY0by88xiptRE5EUjISEK6SEDtDhk8vf8zJF0HKxKzx5pLn06bbb90CjzvV6WnKDY_JI3yARxYoOowNbka1206baic2dDvSoqX0qhTBs14mJ4uXhVAAYqj7aHYcGylQXh64urZssvKyQwJHmztGV_uLwG6mVUPJtKng0lmBtVqpT7qJFeiB1yebxCtQOozAygYDz6qB8V6k0a-f6etNXyZtzyPAGciEPmN8h_iM44mCq-l4GxzEEBGh9oYNEssSurIi85NGALyfqsO36M03aqB3TPfMpQ2ATpwacm-kouoVONX-Ov4GLgsRHADFP2xZz6R8f_rnpo3dT6p5ni_v6n3-Z7bL1Ucnhklws4vW0mKewPfzWRTR3rgMB_T4j4BI089e6Q0Wox1OnNmVydimQTseQorg4YEFa2WZLtCdK_c_8CBj_3S35sd0Tn6KfUTM0GT-9IHG-4slRofZCmmj6a2GYd3Ds3qTRPwtFh5V46gyl2lX8aaNAqQJ5wdwWBZw7b5k8TLy6s4eMssW8xpL7w9qfU8i-oEAVKhd6MgTRoWXKRNDkMM_eGrHvXieeZVBR4bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«توافق نفتی با روسیه خیلی مهمه؛ حجم عظیمی نفت وارد کشورمون می‌شه.
راستش رو بخواید، می‌خوام از رئیس‌جمهور پوتین تشکر کنم.
این نفت هم گازوئیله؛ همون چیزی که ما می‌خوایم. پس ازش تشکر می‌کنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/news_hut/73027" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73026">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=Vq8JfloKOnxnkx_MP9h3V63QjWOKQiheoYG851d_l7wcZutWatb5BGpLzQFba3BWz4ZYIR7wbXe2j28eGZa40sAU6jNh-CmE7tTwEqb6uuuqkRR-Z1ez2tii62XR56muyvdnCHq3TwubcUjO9Qn3m90X0Di4FwpqGRi_RNehi-lkTLdCNspa-13PEjBBJqJtIycUbV20bwSAJUDXdv-mWwEjApRljxS7x3VXVbWOUmEe5ttvT5ueO3UTGN7geaujqiPVIrYQe4ZhdIn0eMIsjawfPKRLh680i9BBSGZ-xlB_2BpGn7MbRU97C89L5ZJia8ZDFj4kRY13PnB1EULZ7KdWSq4Hm3a7B2WqUMntJbjwgDMybgFlvp-3w8uJ0xsX0Ri8pfQb2ReDC1rB2mGfGdvgHmiZqfiSdIFHqJnrYxllSE8JImUF7BvoURoO6hBOcybFAyN0ZDdOof5-OxEuebCWL7qE8RMDQp8-ZVeBZFQ8niZwa0thm-NddM7yIvR8WkTqScZZj3tR4k1v_EhRLrwkZXnOTVGQ2JOvrHRExKGU_nEWlKnuk3cBLT_MXKGDpslcv0JkYgzromQ__P1P3fBzEDm8Ao6TwlL0tPdXkJvQbiv0NJedaLICxwI14SJclyxF8QCcXD6WOoTdgduyGA4X5D1fmpyMyqO-1Z6mvos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=Vq8JfloKOnxnkx_MP9h3V63QjWOKQiheoYG851d_l7wcZutWatb5BGpLzQFba3BWz4ZYIR7wbXe2j28eGZa40sAU6jNh-CmE7tTwEqb6uuuqkRR-Z1ez2tii62XR56muyvdnCHq3TwubcUjO9Qn3m90X0Di4FwpqGRi_RNehi-lkTLdCNspa-13PEjBBJqJtIycUbV20bwSAJUDXdv-mWwEjApRljxS7x3VXVbWOUmEe5ttvT5ueO3UTGN7geaujqiPVIrYQe4ZhdIn0eMIsjawfPKRLh680i9BBSGZ-xlB_2BpGn7MbRU97C89L5ZJia8ZDFj4kRY13PnB1EULZ7KdWSq4Hm3a7B2WqUMntJbjwgDMybgFlvp-3w8uJ0xsX0Ri8pfQb2ReDC1rB2mGfGdvgHmiZqfiSdIFHqJnrYxllSE8JImUF7BvoURoO6hBOcybFAyN0ZDdOof5-OxEuebCWL7qE8RMDQp8-ZVeBZFQ8niZwa0thm-NddM7yIvR8WkTqScZZj3tR4k1v_EhRLrwkZXnOTVGQ2JOvrHRExKGU_nEWlKnuk3cBLT_MXKGDpslcv0JkYgzromQ__P1P3fBzEDm8Ao6TwlL0tPdXkJvQbiv0NJedaLICxwI14SJclyxF8QCcXD6WOoTdgduyGA4X5D1fmpyMyqO-1Z6mvos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در کنار مایک تایسون در کاخ سفید:
«امروز قرار نیست باهاش مبارزه کنم، اما مدت‌هاست که طرفدارشم. مدت‌هاست با هم دوستیم. هیچ‌کس مثل اون نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/news_hut/73026" target="_blank">📅 00:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73025">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFB0F0hlojlgqhiYUhPAwEmsU_71FEy2ly5dYi0Y1TnF6rsPvy2qXX_2EPQT0vaogcx-0PklA_avK5-REgrfQdYcffn18EdBFTNCEmPVrTOivZAj3hzBSeRwuJmXLS4eyo4BIK38wwTX62RZLwLw58RyboZVXBsXMy5HYKGMahQCTUwBuTpRo5UzA89CBa8sMQktiqQLIhnUXQ05xgubjmtWzGFnSNdWOPU-BTjeLw08ZC66lgGBq7M3OUSvngzOA_blLlhmcj9XIczR6R_8nuFzST-bvEqtJNJ9NU3PWEJPQz_Dl0_eYyr93DVEj4AuScNa6TWdlgZXjO4kh6aj6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وزارت خزانه‌داری ایالات متحده انجام تراکنش‌های مربوط به فروش، تحویل، تخلیه و واردات سوخت دیزل با منشأ روسیه — از جمله واردات به ایالات متحده — را تا ۷ آوریل ۲۰۲۷ به‌طور موقت مجاز اعلام کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/73025" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73024">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=fiiz_Ubd8HRMO1oSY6QkgGtqmeF_ghvpMpNmNP-XXwkAQAn1cerwA2AkF51o2lzCZHzZS_cUI_0yHFgphv9lfnPW8rS9nEFzaH_H3gBA_eJBZVfNYjcr8AYI3_CrL1StIYU5sy8UlTQv7Pj_bdjpUbZopT-jsSVGXUDLYOEVSmnxfMbhPzmsXYyurjlJqPrArV23lQkoRqHpgMPSVmWINnjdoq0atz585myzlsYQC35lIqqJXZaa4jBaApuvZvjkgVFZvuGcZr4CJOXJFMRKL3-M4uGsFhGhH77PNqv4MVsNQbsbqdERv-xjgYjwRY9ou9JhkE4k9BHZ3Gi9IE7gZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=fiiz_Ubd8HRMO1oSY6QkgGtqmeF_ghvpMpNmNP-XXwkAQAn1cerwA2AkF51o2lzCZHzZS_cUI_0yHFgphv9lfnPW8rS9nEFzaH_H3gBA_eJBZVfNYjcr8AYI3_CrL1StIYU5sy8UlTQv7Pj_bdjpUbZopT-jsSVGXUDLYOEVSmnxfMbhPzmsXYyurjlJqPrArV23lQkoRqHpgMPSVmWINnjdoq0atz585myzlsYQC35lIqqJXZaa4jBaApuvZvjkgVFZvuGcZr4CJOXJFMRKL3-M4uGsFhGhH77PNqv4MVsNQbsbqdERv-xjgYjwRY9ou9JhkE4k9BHZ3Gi9IE7gZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال ۱۹۵۴ بمب‌افکن B-57B Canberra نیروی هوایی آمریکا از آزمایش هسته‌ای Castle Bravo فیلم‌برداری کرد
این انفجار در آب‌سنگ مرجانی بیکینی در اقیانوس آرام با قدرت ۱۵ مگاتن انجام شد، حدود هزار برابر قوی‌تر از بمب اتمی هیروشیما.
قدرت انفجار موجب آلودگی رادیواکتیو گسترده در منطقه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/73024" target="_blank">📅 23:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73023">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBx153U7zdyIGDXvalf892AYrqUe-OuzXBpInG66sAEK2034ZHSWZ18uvYwfwpNoiZXVyxKi2WgOCj2B9z3O812rfZtP53HZFG6XwXlJqoYQxpcBBqJTIleklGbbJNGC99iW24In7EkuBAwcrwPatXZyWzn6P65gCNb5tLMx86kiIFB5UkXh71CoAbphraRe-Ls5I0N-Tx2j502keKGRPpDXOI4x4MAh9vAs3QvV2-bvmO6F-87fGYPHs9kkShTlb6ioaWXTjKf-duO0VQJNGC-suecVd56Ehzvxggih11GZ6G8zgwXZlxt_Fr2PmKUmyYd1aig1A-6HKHvhrCToaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
من به‌تازگی گفتگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که طی آن توافق شد روسیه بلافاصله بیش از ۳۰۰ هزار تن سوخت دیزل برای بازار آمریکا و جهان تأمین کند؛ همچنین ۵۰۰ هزار تن دیگر در ماه نوامبر و یک میلیون تن بلافاصله پس از آن تحویل داده شود.
علاوه بر این، با توجه به وضعیت پالایشگاه‌های دیزل روسیه، این کشور در مدت‌زمانی کوتاه، ۳ میلیون تن دیگر سوخت دیزل تحویل خواهد داد. با در نظر گرفتن «کنترل کامل» ما بر تنگه هرمز و این خبر عالی درباره انرژی روسیه، قیمت دیزل برای آمریکایی‌ها و در واقع برای تمام جهان، با سرعتی بالا و به شکلی بی‌سابقه کاهش خواهد یافت!
کاهش قیمت‌ها برای آمریکایی‌ها، به‌ویژه کشاورزان، دامداران و رانندگان کامیونِ فوق‌العاده ما، بزرگ‌ترین اولویت من است. این خبری بسیار بزرگ و مهم است. همچنین باید دانست که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73023" target="_blank">📅 23:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73022">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=VXpnp_Va_PnP53tMWdvuHTfSxCJVeXs4OywKbQTRW1RKJoyit2Pdj3a_0OWwfnDIQfFthJomkh_gRGpxXqUCIV9WvfNPvuWIkoV8nrkLJVcVXaoVgJnkuKfmtpK_kVPV2_L8XKg0q2-ovvxx8vSLo-dFv8XiwLPVKg_oAgQQAdzNtjYKOvSOtzYYFiuGXmvVZRrp7bnlGbB302gEOAbd9L2iUm1uBllKX3lk-9Ar49TC3qQDh1LxO28zN6RytT-ohxIDMNsGAH5Et3TLLLnRw6THkTx94FUeHHx2xveVoBve3N6kXj4PfJNrTNwIgt-cjLq3HcWGP9DCNcwUMAR9gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=VXpnp_Va_PnP53tMWdvuHTfSxCJVeXs4OywKbQTRW1RKJoyit2Pdj3a_0OWwfnDIQfFthJomkh_gRGpxXqUCIV9WvfNPvuWIkoV8nrkLJVcVXaoVgJnkuKfmtpK_kVPV2_L8XKg0q2-ovvxx8vSLo-dFv8XiwLPVKg_oAgQQAdzNtjYKOvSOtzYYFiuGXmvVZRrp7bnlGbB302gEOAbd9L2iUm1uBllKX3lk-9Ar49TC3qQDh1LxO28zN6RytT-ohxIDMNsGAH5Et3TLLLnRw6THkTx94FUeHHx2xveVoBve3N6kXj4PfJNrTNwIgt-cjLq3HcWGP9DCNcwUMAR9gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن پلنگ ایرانی در جاده عسلویه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73022" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73021">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=KuOjf-eYzaoGMpeAanVUgcxUshKmGiEAQ_C2C0fEgk80JDmBHv7OL4UzA25w7768DBNwNzRc5gPVy2_PQr5dbBKtf03p3A2Hg16za8WOkOo32S0gcF9P787JP51JfM_8fhh0DxFtS1XahpYnCtV6CJQkY4DGvGAC-9vuZgpDbGGMFLgO1WG7r1hSLpY2IVpn2FKOpbEkiPy1mHEBuaK6Vnnz7dr4USp1Gt6RhNfYBP-95jZ_svZgk65cR294nbJoO21IFLo4fGaR6p-OPm99-4E1OTww-MBnlWTWYDx6Sy808_hBo1wDM45Hwj40nGPJf_bEcZFpXBJl6oYHPGee3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=KuOjf-eYzaoGMpeAanVUgcxUshKmGiEAQ_C2C0fEgk80JDmBHv7OL4UzA25w7768DBNwNzRc5gPVy2_PQr5dbBKtf03p3A2Hg16za8WOkOo32S0gcF9P787JP51JfM_8fhh0DxFtS1XahpYnCtV6CJQkY4DGvGAC-9vuZgpDbGGMFLgO1WG7r1hSLpY2IVpn2FKOpbEkiPy1mHEBuaK6Vnnz7dr4USp1Gt6RhNfYBP-95jZ_svZgk65cR294nbJoO21IFLo4fGaR6p-OPm99-4E1OTww-MBnlWTWYDx6Sy808_hBo1wDM45Hwj40nGPJf_bEcZFpXBJl6oYHPGee3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه حامی حمید رسایی، سران نظام رو تهدید کرده و این‌بار گفته‌ «کاری نکنید مهرآباد را برایتان ناامن کنیم»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73021" target="_blank">📅 22:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73020">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=JucZ9Jqk-VsJU5gtW8BRcRT4f2vIeIu-WFzayYC4MftKKLdJFqjxAHJk7eNjmoXspC_-WrmkpCVEGu7xkLfHsICblsroplgr1ZVhFwV7ts08np5eYCEPW-8Jgo9rSjZQpdr6AbdTgv_MwzerZXlQHnT1EL0rvUXUdAzXQXTQJbhy-F2y-GkoG2r9o_508kPVltGyI2nYOBAVJnCzt8W2e0H6_9r7-snNvOCjGgs4aW2lUJTT7inayav_1fiqGL0zzVCA40Q3_g-BcTc3SYk8R-lkrVZiznHh03WSzNqtUAuMHxvBUMTVWXxjQ520nZbtLEKS-Xq5NwLvk9nX6wkqZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=JucZ9Jqk-VsJU5gtW8BRcRT4f2vIeIu-WFzayYC4MftKKLdJFqjxAHJk7eNjmoXspC_-WrmkpCVEGu7xkLfHsICblsroplgr1ZVhFwV7ts08np5eYCEPW-8Jgo9rSjZQpdr6AbdTgv_MwzerZXlQHnT1EL0rvUXUdAzXQXTQJbhy-F2y-GkoG2r9o_508kPVltGyI2nYOBAVJnCzt8W2e0H6_9r7-snNvOCjGgs4aW2lUJTT7inayav_1fiqGL0zzVCA40Q3_g-BcTc3SYk8R-lkrVZiznHh03WSzNqtUAuMHxvBUMTVWXxjQ520nZbtLEKS-Xq5NwLvk9nX6wkqZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگروه آماده آبی‌خاکی «مکین آیلند | Makin Island» نیروی دریایی آمریکا وارد پرل‌هاربر تو هاوایی شده؛
این ناوگروه بعد از یه توقف کوتاه تو هاوایی، مسیرش رو به سمت غرب ادامه میده و راهی خاورمیانه و منطقه تحت فرماندهی سنتکام میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73020" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73019">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فشار اقتصادی آمریکا علیه ایران؛ واشینگتن به‌دنبال قطع مسیرهای تجاری تهران؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با شبکه نیوزمکس اعلام کرده که دولت ترامپ قصد دارد فشار اقتصادی بر ایران را به سطحی بی‌سابقه برساند. او از تشدید انزوای اقتصادی ایران و ادامه محاصره بنادر این کشور سخن گفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73019" target="_blank">📅 21:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73018">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=ZbLxWo5Fyo46P4jJEnZG1cmPzo0q1Gw_-j-XLPy5MygOa3FVIFX3MsmCWvkh7f3B7NX81XllEUAtrLkKHs-4kUjTtS74rNAcK9dlBRVQC1z7dzzSdcOh7mBSlz-NnnMcjeT01a9ARy4HA1cVQh3zgcbVLf72n-4xbstzlvLJ7FS578lNOHjfv-Rze1EhPx2h8n44555HQVxQf0yfnQbyuLuhl0HHexNRDPcPW6DjaB-3qDwtjCxsx6t4UL5ulZz3kK-exbcsskkOT53fuz1Vxuw8UFhY2QpCXFt63wEZmcE1E0231MSDeKnNDPApIFDQs4fLoh7h6MBbacyXaVHH2Z-6Gs0Z7vD9c5blI0JLkc4k4zeGBjTfjA6V0pyMK-WSNeD6uXudQpEDJMc6u6kgNeAGLud4dbF3HODV-2wONZis-ti4Hrzxd181ANOxPYISCWra9qJQU9z23yjou1YwNJov-5rlm7nkhLglwxxTtzqgon7BHnN_k3-vSJd2SrRraiqA-YH_f4Xh90Rr7Pm41VCeml0OIji5d0jur9vtGZmX7bT5pE2vXoJ5nZx2IT__lULXtv7Pej1y922_THgJ71wOultl8QwBhrgLMJCWPHbqBBm2-QXzDfxhaEaNHqIvGJ-KNS6zGHV9fTBhPlpP_2n0goMBuq5MR-p0Bs1uKL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=ZbLxWo5Fyo46P4jJEnZG1cmPzo0q1Gw_-j-XLPy5MygOa3FVIFX3MsmCWvkh7f3B7NX81XllEUAtrLkKHs-4kUjTtS74rNAcK9dlBRVQC1z7dzzSdcOh7mBSlz-NnnMcjeT01a9ARy4HA1cVQh3zgcbVLf72n-4xbstzlvLJ7FS578lNOHjfv-Rze1EhPx2h8n44555HQVxQf0yfnQbyuLuhl0HHexNRDPcPW6DjaB-3qDwtjCxsx6t4UL5ulZz3kK-exbcsskkOT53fuz1Vxuw8UFhY2QpCXFt63wEZmcE1E0231MSDeKnNDPApIFDQs4fLoh7h6MBbacyXaVHH2Z-6Gs0Z7vD9c5blI0JLkc4k4zeGBjTfjA6V0pyMK-WSNeD6uXudQpEDJMc6u6kgNeAGLud4dbF3HODV-2wONZis-ti4Hrzxd181ANOxPYISCWra9qJQU9z23yjou1YwNJov-5rlm7nkhLglwxxTtzqgon7BHnN_k3-vSJd2SrRraiqA-YH_f4Xh90Rr7Pm41VCeml0OIji5d0jur9vtGZmX7bT5pE2vXoJ5nZx2IT__lULXtv7Pej1y922_THgJ71wOultl8QwBhrgLMJCWPHbqBBm2-QXzDfxhaEaNHqIvGJ-KNS6zGHV9fTBhPlpP_2n0goMBuq5MR-p0Bs1uKL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش چشمگیر پروازهای ترابری آمریکا در ارتباط با خاورمیانه
طی ۲۴ ساعت گذشته تا همین لحظات، تحرکات گسترده هواپیماهای ترابری آمریکا در ارتباط با خاورمیانه ادامه داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73018" target="_blank">📅 20:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73017">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وزیر آموزش‌وپرورش: تعطیلی احتمالی مدارس بر اساس شرایط هر منطقه تعیین می‌شود
.
کاظمی:
در الگوی جدید بازگشایی مدارس، شرایط هر منطقه به‌صورت جداگانه بررسی می‌شود و در مناطقی که خطری دانش‌آموزان و کادر آموزشی را تهدید نمی‌کند، آموزش حضوری در اولویت خواهد بود!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73017" target="_blank">📅 20:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73016">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#فوری
؛نحوه فعالیت مدارس هرمزگان از یکشنبه ۱۹ مهرماه ۱۴۰۵
بر اساس تصمیم جدید:
- شنبه ۱۸ مهر:
همه مقاطع در هرمزگان غیرحضوری.
از یکشنبه ۱۹ مهر به بعد:
قشم، سیریک و جاسک:
- شهرها: ترکیبی از حضوری و غیرحضوری (تعیین‌شده توسط مدیر مدرسه).
- روستاها:
حضوری اقتضایی.
بندرعباس:
- سه روز حضوری و دو روز غیرحضوری در هفته (برنامه توسط مدیر مدرسه اعلام می‌شود).
سایر شهرستان‌ها:
- حضوری.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73016" target="_blank">📅 19:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73015">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=qq20IWlTPKrbCuncMHzsmQhmvW_vFaY25uZuQYprY0gaaP1cr6_guyaeElwq5yYBep5bLTvHu7eNZGy8fFan_hV_ByocTpVjiLeSVHe1pNoaDzRzDhfvlyQF1LaQDeue3CtD9FhOjpc6N7qeSxndFalpfbKqCacaEbW7-A7h-WiAp0htV0Q9Wb1mClOgLQhn-rjp4WXsn7WqgnZNIZ5ds0aasuvj3EoXV2bo7IFgeLUvEjzmh4HzyB51i4nVxWsj6BosL0RO4cTPV-BRKphKGmEDEzVtioWk6qkolB7h2NGXfHs5MQiDhPEqb_kN3nK6exvMfg-bDE_y2qeo9UvMTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=qq20IWlTPKrbCuncMHzsmQhmvW_vFaY25uZuQYprY0gaaP1cr6_guyaeElwq5yYBep5bLTvHu7eNZGy8fFan_hV_ByocTpVjiLeSVHe1pNoaDzRzDhfvlyQF1LaQDeue3CtD9FhOjpc6N7qeSxndFalpfbKqCacaEbW7-A7h-WiAp0htV0Q9Wb1mClOgLQhn-rjp4WXsn7WqgnZNIZ5ds0aasuvj3EoXV2bo7IFgeLUvEjzmh4HzyB51i4nVxWsj6BosL0RO4cTPV-BRKphKGmEDEzVtioWk6qkolB7h2NGXfHs5MQiDhPEqb_kN3nK6exvMfg-bDE_y2qeo9UvMTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد دانشگاه امام صادق:
دیگه هیچی برای دفاع و حمله نداریم هرچی داشتیمو زدن؛جمهوری اسلامی هیچی نداره دیگه برای حاکمیت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73015" target="_blank">📅 19:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73012">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIqkSNtisBzGIaIVGgcHTmsc8ECaaRwK0KmbhE7uKkLrj0429bFimk7kD_3eFdY4xhX4CuNkHubUQGJLq98koy7MyNyuCYOJNH43XCRXit2G9_tkIS7alHGOxvecoF78mEJQh5My17sO2iB2mmf9vyArPLewLxgoHNQb1jmJCl8l74wlk7ELuUFc1mB_jGrIKHGfriDMir4gxhJFBGe8xN2zq_K7M0kNwNGiyf8OfTGGUvdcsxURJZYQL2wotPU9EkZlIRlQK4VLYN1fY8y1SZE9VVmSrx-SDd3-A3Wc4OXppunTN2EbEbc3Ri-Xi9ckbYkMHvxi5EX_8s8NPSa-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FafT5U9Ts6n5scDIYyo-UxbOs5gM057a5iogxaUixIto9jwsP5mwQgSq6lZi5tVi-QNaqmg-TIAvlGYWGh2JF2_017cZDTzeqoQ5H6HKTBBWbmOBSMLg3eINyu8np1xDWu490gqciRkYNkgypvucUasL2ZKxQ_lhMt8wndhrflrXFWqn2y4pxdGCQBDIJVeql9X-uT094_8JMC73LjsWTwlLKOq6ygo29qlrnmGq0sQ47qaKOfd-qHRPgKNBkEuoy82r5iE6ir6ErhWjo-C3J3JRyCZM6InmspZnqsfHuJ0UAeCoqJ5wIOAR8BNeghYNAxDKAIjPiT17HB5J-JsiZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305d802103.mp4?token=epk4wXPWuUbQ6_2M-qVPFdE8mk5FLD4opgwYoJmFn2lveUECki0LTH7Ijro-T9MK7m6EtZujPjLbSVtJHsqG4lVLdyPMs5ZXZXHgRpBtClyIIihBfPlrxUvaw1UQgJ0gTwta84t2_Mql8tq1OUf_0fut62JK_B22cSkwFezVHbeO_DteYt0dXSeNB6LbjA7ulBHHL10s2w-_3qN7ZAytERSkNZtiEXbIj6iTDxuIMma6G_QJwBjDczMBhXKAkS77kfSbtc8pODqVh6_z16ZT2JJjiNhFJsHN-SYJheKOAHODoVCxksJgK2_59hN_D1S2rNZYB74ghfdY7umE8QJhHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305d802103.mp4?token=epk4wXPWuUbQ6_2M-qVPFdE8mk5FLD4opgwYoJmFn2lveUECki0LTH7Ijro-T9MK7m6EtZujPjLbSVtJHsqG4lVLdyPMs5ZXZXHgRpBtClyIIihBfPlrxUvaw1UQgJ0gTwta84t2_Mql8tq1OUf_0fut62JK_B22cSkwFezVHbeO_DteYt0dXSeNB6LbjA7ulBHHL10s2w-_3qN7ZAytERSkNZtiEXbIj6iTDxuIMma6G_QJwBjDczMBhXKAkS77kfSbtc8pODqVh6_z16ZT2JJjiNhFJsHN-SYJheKOAHODoVCxksJgK2_59hN_D1S2rNZYB74ghfdY7umE8QJhHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو و تصاویر وایرال شده از آخوندفدا‌ها تو شهرستان بابل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73012" target="_blank">📅 18:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73009">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nWapV8zx45gJHJ6aBlFN4-gythig3R4DE6g1v-ZO5vDR4LSzzrJDYmMWz1mVLj2egAwhYa1SFQvsdvgz7Kq7az78FBf4Fvg5y0PooAeErZ4qdaYANc6mvTggQ7Jj_WNlHjueOB68hEWCFRva6CbQaiFX1OOh-hLAXPL3GGz3qBLiVpewnPpDcqfjwUhzCQQlEapUe85oY-bNgAer_5m1vjeQbfz9neuh233Bt5JqZKq_tyHBF98bsTtUm_wN3aIcTozpXUjfbLRPOreWCre46YKkvaOr6ehzrwmcEG1uAXmCocUbSHHG_-dfm9twlTUVscJ049eT0L68Eo_xtq61Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUtoE_qNZ60rSy4vIwfIzHNgKQ5oNsFIvgGraN9wHIYZ9NlUdtif5eSFtIth2OGHZbQBTKB_yOQmm-xVVPT_5rLPrpSrpeYjM6CQMsnQwAI1gxwqwDy-Kr3Ij1kQqHKta0ZmWf1YFFDVX4ZYC2Ixo5eLQpW4EPzIR6Clu-BMn8PoEj8DIq5EmbJCUgBwkOExP-_7hSF6FnAi7oTyWXPtrw-UWWOZ0_tmFTP2-ziWrMSzH63pTTVf0TZHRq-0h7QhXWHQqAXgKfqSfuEOhWZoh4viGwCgrtpM-3lqugNZNGeCFiYKrez_InK9kqrdKUwRRD9mMDi6eX-6MNezS2PnOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=S7GJx990dVQdSC7VF-bxoH4hrM682PKVXcUHgGjlkY5fsScP0c99Fw6ACa5ea-DZwQ1GfiKT9t6wbCbaBJ7KwIoSOk7H7IQJ6E5gByw5kKx9TNSpqhiIxsHbfsoqVQOP3ZNOOJHVDehNsH-QuCkhvvzISXn7h8ZbV663tlGovB5PQQ0mSYtHMN33xmFbyBcX40jub-3Mg2bZOAknNhbnPZUpl6HK5A7bKMie1a06bFtx_S49_SPiJ-mC6hTUbe0SYIAkWMDb6899sJYICneMSsV_FwfFkKghAQNQQIfwtlUiZE0dwyS6N_4a9XYsr60yNydaet0p0OGz5gfD6dzuLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=S7GJx990dVQdSC7VF-bxoH4hrM682PKVXcUHgGjlkY5fsScP0c99Fw6ACa5ea-DZwQ1GfiKT9t6wbCbaBJ7KwIoSOk7H7IQJ6E5gByw5kKx9TNSpqhiIxsHbfsoqVQOP3ZNOOJHVDehNsH-QuCkhvvzISXn7h8ZbV663tlGovB5PQQ0mSYtHMN33xmFbyBcX40jub-3Mg2bZOAknNhbnPZUpl6HK5A7bKMie1a06bFtx_S49_SPiJ-mC6hTUbe0SYIAkWMDb6899sJYICneMSsV_FwfFkKghAQNQQIfwtlUiZE0dwyS6N_4a9XYsr60yNydaet0p0OGz5gfD6dzuLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی عربستان به صنعا پایتخت یمن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73009" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73008">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsQZ5lqFrOIjpgZciHtmQA-DroRyBUWI5H9rDicPXVCZs3D8IIpj8QcA3yIoDusRCP131Vr3dGbvgKsPnmY4uif7RBCiUbkaeV3-j4VvSAzgxNypQ4SZbQBhR3H58FwqRUSq6yw6KsMxNQ1zyL8i2O-XeglTRxCyb_Uo_Buxst5xAxod8YLQdaq1qdKfICZ5GKTUxHpE-386BWtsOY39cNw5gAkhBVCHSID_YJL9qPOBT75NdYqWnIGuHoPHKGOaa0mCVHSEPkeO_sS-367dqSBit7cIFJFnYiVt7TQctRHvYUqZaePf2D4DOV8WQrNBCEm_66dEnFmIjuTc46gGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
از الان به بعد برخورد با شناورهای متخلف محدود به تنگه هرمز نخواهد بود و هر شناوری که از مسیر غیرمجاز تنگه هرمز عبور کنه در سراسر منطقه تحت تعقیب قرار‌می‌گیره و حتما تنبیه می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73008" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73007">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73007" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73007" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73006">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnIQvhpbTSYkZEa-JX4xr6dmQdNhPqQLtddYH2dPSBqj7SeFTx6U3HZd70R9hDKEwEPmjrDo9N4u0GFV4Ucvho6Yu_-czA5KZAI7PA3m6KWCJxN96PGyKthL1AoRs_RLgKp9oA4gdgUkx8D7XMDm876QwS3XLydNV0zWN-LPYfHzN_1HFb1wua8NYPWTYRAdSPg74XqlGup0WnxYTsthxUjHQdboMJ9teJx4cPD2BKB9ky6gj5q5icLBF2Lup16KCPTacjjOoTepgeIBWgN0NByssTLfiBZOQn9CNQQLGJidI_JtMHV6MyJpOCmryrDcISByY6RvdWycOGu3h1Gtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73006" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73005">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=MbUGYhJOT5LOH-5dagIcCh13Ula4gclyzc5Ad-gDkorVRcwL5Hqhm_O9xK0Qszmv6N03BXm69l4b2ZL4YPo8N91jac_GG0D7CSHJz3zVySMCvQoIkbP3mKqXWHmqwO4nuOv8kgL7hZrzSKntgbM4p6qJOGoFBCPqKtcI5SgK5jYQFf05BRfTWOyiFCzFH1YBOKL7Ex_svY_oqFAB5U5JGfnM6jvIu1E1YWPWUNo2mzdBVf4lq29okbH0VapV7ew6rRUqXljO1hUlNJfFamUiQWgTx3eLRNxQ4RPrn_PfHLiI6dkqagTFDgeYwzCsyK4lmjk2cZGoAdK6lL1Z9Xwl-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=MbUGYhJOT5LOH-5dagIcCh13Ula4gclyzc5Ad-gDkorVRcwL5Hqhm_O9xK0Qszmv6N03BXm69l4b2ZL4YPo8N91jac_GG0D7CSHJz3zVySMCvQoIkbP3mKqXWHmqwO4nuOv8kgL7hZrzSKntgbM4p6qJOGoFBCPqKtcI5SgK5jYQFf05BRfTWOyiFCzFH1YBOKL7Ex_svY_oqFAB5U5JGfnM6jvIu1E1YWPWUNo2mzdBVf4lq29okbH0VapV7ew6rRUqXljO1hUlNJfFamUiQWgTx3eLRNxQ4RPrn_PfHLiI6dkqagTFDgeYwzCsyK4lmjk2cZGoAdK6lL1Z9Xwl-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هواداران حکومت : رفتم تو گونی!
رفتیم جلوی مجلس تجمع کردیم پرایوت نامبر بهمون زنگ زدن
با یه شماره به من زنگ زدن از اطلاعات سپاه بهم گفتن بیا اطلاعات باید توضیح بدی
هیچکس با کسایی که هنجار شکنی میکنن و پست های زشت میزارن و کاریکاتور های زشت و زننده میزارن کاری نداره
بعد من که براساس قران عمل کردم ، منو خواستن احضار بشم
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73005" target="_blank">📅 17:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73003">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86531200e8.mp4?token=dFrakDVwJ3_7yV8T6Sf-mBfbAbIlsTlBF8xNFej5wKxW-mCipQwTLvPYgDbraD91flRYutxnuzDevoOsDbuwapFNzawi0aOqH-L8_Hem4AYPIB1iv3qLyKEg2YPxkXy02lERjM4sUWjdlsPrkgczACPCxF-FeGGyN47qAhPnWx4GmP4Kij9B_L5LNHHQYAk4Nx2L8Gv272bRPay2ZjXpieLk246ARvflFlGBfNR9lrolvzMXBx7XbJaPwOv5V0oq30twA5Jnjuu6vbV8amTVOCMLQCP91lrG6jRNS17vEDmHF3F_Dy4K5TRIIOd0mDheYdoGjob-l0621QD7c-T1Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86531200e8.mp4?token=dFrakDVwJ3_7yV8T6Sf-mBfbAbIlsTlBF8xNFej5wKxW-mCipQwTLvPYgDbraD91flRYutxnuzDevoOsDbuwapFNzawi0aOqH-L8_Hem4AYPIB1iv3qLyKEg2YPxkXy02lERjM4sUWjdlsPrkgczACPCxF-FeGGyN47qAhPnWx4GmP4Kij9B_L5LNHHQYAk4Nx2L8Gv272bRPay2ZjXpieLk246ARvflFlGBfNR9lrolvzMXBx7XbJaPwOv5V0oq30twA5Jnjuu6vbV8amTVOCMLQCP91lrG6jRNS17vEDmHF3F_Dy4K5TRIIOd0mDheYdoGjob-l0621QD7c-T1Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛درگیری مسلحانه در چشم‌زیارت زاهدان؛ اعزام گسترده نیروهای نظامی؛
به گزارش حال‌وش، در پی حمله مسلحانه به یک خودروی حامل نیروهای نظامی در منطقه چشم‌زیارت زاهدان، ده‌ها خودروی نظامی و امنیتی به منطقه اعزام شده‌اند و پرواز یک بالگرد نظامی نیز گزارش شده است.
هم‌زمان، رسانه‌های حکومتی از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای انتظامی استان خبر داده‌اند. برخی منابع محلی نیز از کشته‌شدن معاون اجتماعی انتظامی استان در این حادثه خبر داده‌اند؛ با این حال، جزئیات و آمار تلفات هنوز به‌طور مستقل تأیید نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73003" target="_blank">📅 17:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73002">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbHPkaB9MEL8wbVFdqlh0bAKNFlCdilY75XCc1tvQM9tet5uxhaFcuaE4S8iYLHb5FTzy0twc8KXe_dOHg5vkgeI8nc4WTB_9_qfN0BBjVvPcD5Qk4Y051RufX7U2_HXM4OpgnJrpVbs-CQ1pWh2J35wEA8z5SHja3F97hb0VY_q27BWoE9t_jyZq34VJrMk3utPlVtiDcZhOuSHjnKUGmNU5ZKGDgt3z-9Fv3K6O3t81rWBF_YggT_Tqaqd93vA8-gkbOQ4dGlB1dDmY0usIOgorpuByJSqVXdntweCGppBEeJ1I-jZF8_Waem0yE_pwpfQDIh8Oz6gy3lWO6sJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌وش: کشته‌شدن ۱۲ نیروی نظامی در حملات ۴۸ ساعت گذشته
به گزارش حال‌وش، در حملات مسلحانه اخیر در سیستان‌وبلوچستان، ۱۲ نیروی نظامی کشته شده‌اند. در حمله به دو خودروی نظامی در منطقه کرین‌دوک نیکشهر، محمدرضا اوکاتی کشته و پنج نفر مجروح شدند. همچنین سرگرد مهدی جمشیدی در فاریاب و ستوان‌سوم وحید عنایت و عباس آقایی در محور لخشک زاهدان کشته شدند.
هویت سایر کشته‌شدگان هنوز احراز نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73002" target="_blank">📅 16:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73001">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=HltugVuTI8HsQcPmL28nhC_Hu39GB5ndk1FkDIwf3d9Iazc3SpMsmZAtpI4JN5yELAOZZ4WXCjpwJ_FZpUOi8YHf6KhoiyKI1yMYqtQ9-VKwMoIP9Lt9j-i2195qlfzX6VJ5PiCfPd3cRe8cGRZhphhcqmsy7PsvqelDAmlTSz13iDOkTR_5bmoRuxukys1XQJut89m1OtnkxUydHEL6JTfpfFMywBujLz1vWrGHElt-4IeCpwQHEoVvL8NMD1NtodK5wRJ-3anCTfYrnsu71VFovYZ88-ev-k2Te3lL48IsyfJD63vBcQbcJY1FaOSZuLzQRqbrQyrhtcP5_RcwOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=HltugVuTI8HsQcPmL28nhC_Hu39GB5ndk1FkDIwf3d9Iazc3SpMsmZAtpI4JN5yELAOZZ4WXCjpwJ_FZpUOi8YHf6KhoiyKI1yMYqtQ9-VKwMoIP9Lt9j-i2195qlfzX6VJ5PiCfPd3cRe8cGRZhphhcqmsy7PsvqelDAmlTSz13iDOkTR_5bmoRuxukys1XQJut89m1OtnkxUydHEL6JTfpfFMywBujLz1vWrGHElt-4IeCpwQHEoVvL8NMD1NtodK5wRJ-3anCTfYrnsu71VFovYZ88-ev-k2Te3lL48IsyfJD63vBcQbcJY1FaOSZuLzQRqbrQyrhtcP5_RcwOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف برای نامزدش یه شب رویایی رمانتیک ساخته واسش گل خریده کنارش یه ایفون 18 پرومکس ۲۵۶ گیگ هم بهش هدیه داده، دختره همون لحظه میگه ۲۵۶ گیگ چیه اخه ۱ ترابایت میخواستم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73001" target="_blank">📅 16:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73000">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=JS3xKZb_qz76K4jRFZknHN2_PJzvZS10n6ZTB5z36ItFjbiSzPNvZXQNUIJxFPBHHKemL5NYTBgPxFD70Qal2of_UV-18QBlzkQJR_QNuv8iIadEJLcoBEi6qzmuzfpwvFc0Z0g60D7CVVmJAPSCVkZZM_n1bwrlpDMmkA5HZshhAUZKn7igRvD_8fGRYWVvDZn_aKNTSgjEVz3_D7IeSH2hXOAtwglWEu-_SQ1F3RuQf3Uql7ooghdp1joGXHovI0VtwJ9OwHU_T5pf9vLB5vCnDL6STqlHvW_3Dkp_Z2NsIpotdBnSpLMx29uVo8-enqAav5AZVMvC9SvbGpYbOSIVqhyfGAGQ0j5PVd3cHvncoDGwxrciCn1kPXyCENCcNv57lZaVR9utM_drJ6uC8yzBy3lLT66CKc5-_T_lplDZi4eD2OMropt1Vsu9k1Nsefw3QuUXNQZJfuYJi0shGwqudFzLHiQXgQO2uYIojpt5g9kMOMXRyFOd3X1n5pRHAxaKBLeqX7XZ3HFcaf6ChMxtgOI8szqUa1IKVSUJcRSECf832_UC452ZUsM5Oujvcu2VNZOcq44_L45DVhA8zDV8CW41F4S6MwcQtg2kGgwJiF9iEBs7Ei_da7buKPTv7BJ5M_9m7_BTT_bptV_vzHEsao8GbVqW1ulbkZ7kdL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=JS3xKZb_qz76K4jRFZknHN2_PJzvZS10n6ZTB5z36ItFjbiSzPNvZXQNUIJxFPBHHKemL5NYTBgPxFD70Qal2of_UV-18QBlzkQJR_QNuv8iIadEJLcoBEi6qzmuzfpwvFc0Z0g60D7CVVmJAPSCVkZZM_n1bwrlpDMmkA5HZshhAUZKn7igRvD_8fGRYWVvDZn_aKNTSgjEVz3_D7IeSH2hXOAtwglWEu-_SQ1F3RuQf3Uql7ooghdp1joGXHovI0VtwJ9OwHU_T5pf9vLB5vCnDL6STqlHvW_3Dkp_Z2NsIpotdBnSpLMx29uVo8-enqAav5AZVMvC9SvbGpYbOSIVqhyfGAGQ0j5PVd3cHvncoDGwxrciCn1kPXyCENCcNv57lZaVR9utM_drJ6uC8yzBy3lLT66CKc5-_T_lplDZi4eD2OMropt1Vsu9k1Nsefw3QuUXNQZJfuYJi0shGwqudFzLHiQXgQO2uYIojpt5g9kMOMXRyFOd3X1n5pRHAxaKBLeqX7XZ3HFcaf6ChMxtgOI8szqUa1IKVSUJcRSECf832_UC452ZUsM5Oujvcu2VNZOcq44_L45DVhA8zDV8CW41F4S6MwcQtg2kGgwJiF9iEBs7Ei_da7buKPTv7BJ5M_9m7_BTT_bptV_vzHEsao8GbVqW1ulbkZ7kdL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یه جراح و متخصص زنان :
این خانم 16 ساله بعد اولین رابطه‌اش تو شب اول ازدواج (شب زفاف) دچار خونریزی شدید شده ولی چون فکر می‌کرده بخاطر پارگی پرده‌‌شه، نیومده پیش دکتر و الان هموگلوبینش چندین واحد افت کرده!
در واقع شوهرش فکر می‌کرده داره کابینت نصب می‌کنه و بی‌دین زده همزمان پرده، پرینه و فورشت رو باهم پاره کرده.
اصلا پارگی پرده خونریزی زیادی نداره، هرگونه خون‌ریزی بعد رابطه رو لطفا جدی بگیرید...
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73000" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72999">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=rpHt0yqEJNUbSoXm-l7dCemvBDCTXY4i4b702kf19yOvUz4d7591tDc_X93Ui3Bmeq5x-6W3jp9qVkUZ8aT0wu9YDCeSlA3N6CJ49GlWpuRK52H0uAz3YYLR1pMnI2L46UhGzZ4M7zSlMN0KPkDnZyfOjnseO-fnmPOyNiHQIijYa4WaQRet1QnEHBUtuA5dBcCdh_7YDLogY53oGSGCLiPlt1NsN-3ZSnyMB_L_bDHFl-e21Kuu588UIcf-_6KlgLecItMVZM-qsawYPtGh8nLH12jm8n9vKJkEWFmlkD0pyVVFTJgeoaLwKFsIQhDBjl2wPwvuS-cDQKH43qFivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=rpHt0yqEJNUbSoXm-l7dCemvBDCTXY4i4b702kf19yOvUz4d7591tDc_X93Ui3Bmeq5x-6W3jp9qVkUZ8aT0wu9YDCeSlA3N6CJ49GlWpuRK52H0uAz3YYLR1pMnI2L46UhGzZ4M7zSlMN0KPkDnZyfOjnseO-fnmPOyNiHQIijYa4WaQRet1QnEHBUtuA5dBcCdh_7YDLogY53oGSGCLiPlt1NsN-3ZSnyMB_L_bDHFl-e21Kuu588UIcf-_6KlgLecItMVZM-qsawYPtGh8nLH12jm8n9vKJkEWFmlkD0pyVVFTJgeoaLwKFsIQhDBjl2wPwvuS-cDQKH43qFivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه!!!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72999" target="_blank">📅 15:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72998">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=A1ZMYcXIriTtszwmhy7f9ViDeDc_hrWudWcvcrpZq3uyYnk0GQL6jp9q_D3Qjx7rJDserIWWxv2bjey9lQWMqhsD_iJ6JgpQSNxTcC4NtRDDR80GVIYPXalHPJqry6kbTzj_mtkBhXnhRH-Q6VHKt4QY27zZswG2gke_3Eu3Fv9wsz78gZ07wy1Q-jPyM_5VWrFU2RMBHqBQSl0MxVN3Zr_Y9LLxUgevyOaCAU45mnQyQnaQgTeNxuNaPhAIjfLoyFVpDnW6eCARERKzbMCwVFwCnl3O-KGf5x11CH16RbdqWiEyQZyLTuECMFzYXFTuwdtiOamfx7pKAn0SmJS0MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=A1ZMYcXIriTtszwmhy7f9ViDeDc_hrWudWcvcrpZq3uyYnk0GQL6jp9q_D3Qjx7rJDserIWWxv2bjey9lQWMqhsD_iJ6JgpQSNxTcC4NtRDDR80GVIYPXalHPJqry6kbTzj_mtkBhXnhRH-Q6VHKt4QY27zZswG2gke_3Eu3Fv9wsz78gZ07wy1Q-jPyM_5VWrFU2RMBHqBQSl0MxVN3Zr_Y9LLxUgevyOaCAU45mnQyQnaQgTeNxuNaPhAIjfLoyFVpDnW6eCARERKzbMCwVFwCnl3O-KGf5x11CH16RbdqWiEyQZyLTuECMFzYXFTuwdtiOamfx7pKAn0SmJS0MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله پهپاد هرمس هرون تی پی اسرائیل به نیروهای گردان پدافند لشکر3 حمزه سیدالشهدا سپاه در آذربایجان غربی در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72998" target="_blank">📅 15:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72997">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTNxGZQNazei6XsIFj-_4ZNVVh31ks08-AUwAIr1BUKX7VRvyROuMrdJ-L96qD-mmDzlXZqrgXk-JS6Ncx0H0QGUVyIROxggVpTfBQJ7HVgzuhgwFVXe5rcA94Lyp2IY4BG9BKZIkE9woT0Coso_83b7EGsyGnZ_GD_iBRyn4ceyvePgupWBC7-ro8etQcJx6yvgMtA-oJEB9DTJ65WiM8fhxTcv0_bwJahsCOR1CfORrJyDsX2yZE3tfKmMss0V4-hJdHtaJc5IQTkQo0LemhfQYwXj8AVFPrRweKrHrwWxHWPZNA19dpgrLuBc77f0it-d_eLOfI5jNFv940WaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار امنیتی جدید سفارت آمریکا در اردن درباره احتمال اختلال در پروازهای منطقه
؛
سفارت آمریکا در اَمان بار دیگر به شهروندان آمریکایی در خاورمیانه هشدار داد و با اشاره به احتمال تشدید تنش‌های منطقه‌ای، درباره لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرهای هوایی هشدار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72997" target="_blank">📅 14:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72996">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=C5CVhRLau28CPex5vYqcRelVpvBQUp1vEbYuOvZqxrlLx0DlpFIbjSa0gBuClfKVRGPI8LaywLR5q5bjohb08rbzFUeot7BG9KpeRdDDONj5xttr3jltcNhMRvGes8q_NDxG0tujtFMt3PK27UZTkn3L8jITslYWtVJiQwQ3c0v6hWcSIVgWCDRJKhCBRx2OCcjsGHklAe_kCQ15OZ20LrW2mkBc-inugiIwaoXOCTy86dGo20M3OZIXa8ZdJ7ResYQF4_z2CEKMmYZfJ8_EKwA7PyZ1rASfW0Nqc2ekh0--VPDnRsPT0c5QvQjhAu2voeqOXG8FCGFHD__SAPyANTsQTX0lQSdv7dtphJ30O4QBsvRtsCqZnngceNsfyMbEGpA1_SVY0XGjj6pNbbJ-WjsHV6579AMIYAyIPOF060rsI9Lu2BMRYiC8vRslo_pSeN7154UAO2DmVUaT1nCKlJ9imFQvwAQE_FjUTV2MaAbos9DLmTfFYt0YUOj6DSgvFDFA8Up8oZZBPq7dp0ek-0yAclo_DqZuyDyEBg0IQuW4d85BmyYx3iaUzXUtlgAVpzcJZ109A6K3cYluUI6o7Qpz1kkdz1EJjf_HiPpskNyCubO_vOYaRBMuLiDOftrerkHQDZ_w95cS6Z3RT3bxG2WwKxtt52n8CG0xeOjxfng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=C5CVhRLau28CPex5vYqcRelVpvBQUp1vEbYuOvZqxrlLx0DlpFIbjSa0gBuClfKVRGPI8LaywLR5q5bjohb08rbzFUeot7BG9KpeRdDDONj5xttr3jltcNhMRvGes8q_NDxG0tujtFMt3PK27UZTkn3L8jITslYWtVJiQwQ3c0v6hWcSIVgWCDRJKhCBRx2OCcjsGHklAe_kCQ15OZ20LrW2mkBc-inugiIwaoXOCTy86dGo20M3OZIXa8ZdJ7ResYQF4_z2CEKMmYZfJ8_EKwA7PyZ1rASfW0Nqc2ekh0--VPDnRsPT0c5QvQjhAu2voeqOXG8FCGFHD__SAPyANTsQTX0lQSdv7dtphJ30O4QBsvRtsCqZnngceNsfyMbEGpA1_SVY0XGjj6pNbbJ-WjsHV6579AMIYAyIPOF060rsI9Lu2BMRYiC8vRslo_pSeN7154UAO2DmVUaT1nCKlJ9imFQvwAQE_FjUTV2MaAbos9DLmTfFYt0YUOj6DSgvFDFA8Up8oZZBPq7dp0ek-0yAclo_DqZuyDyEBg0IQuW4d85BmyYx3iaUzXUtlgAVpzcJZ109A6K3cYluUI6o7Qpz1kkdz1EJjf_HiPpskNyCubO_vOYaRBMuLiDOftrerkHQDZ_w95cS6Z3RT3bxG2WwKxtt52n8CG0xeOjxfng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72996" target="_blank">📅 13:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72994">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PH1wDFk8qxtvuH3HMoLvjco4drExwpXBnCwvvps9UST_7APK-gphUA3jzJwQyoRNvEBbCnPBGOiahgD5dukOkcQFpc0t_7LKmQEMZkl3C6VhsHMJ-x_9y_Xnqzw5x0qKkgF2VGLThol-b2dNjY7CoTzSNf2I9my64jgGkigaVu58e7jtpPbxf1jRaqtbwFZkzvIKGz_-aGiNzAyEw07Fg4hnF_dgz5bhVRIMzTAiPJJJdxWbFMObQciZXeY6EH_msZxdRQi7gt553fclD5pgki_ni3zNaRq-GC4o_7aACG9YhfbkC1XMi_GgqzYFEJas2av-Qe2W4VPDplzsQlh0_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g98-HcKDiCyWpPlBJ6TAnixx4WOnzz3MxfiAVLiV6Nl8-BWra9ME_KQDtD2TB8DTMCXAbU0TpbWw48SfM-p--rlRnKduzOpnaGjmPsQDzWdcC9WxVQUDFeE9vPjf9q2R_NuasdbnqG_2gomzm6aGUddUXKgB1ZZWRMhu7QX1pfU3T00NP9WoT1QjsqsIiOiWMtMOHPSQzH1Xb9M7bZ6acr2B2pQBwjWdqci3CQalFmuAt9zmF3vn8ZwLrpr5VeioNAJldDnA4b8JaqomQiEdXalEYhiLKJ0G-06ncBTME3jmqB2GTJISpHwl5fV9IJs91lkZdt3QTwv90uoNpGdrhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن پس از ۳۲۱ روز به خانه برگشت؛ در حالی که بدنه جزیره فرماندهی اون با نشانه‌های ثبت‌شده از اهداف منهدم‌شده در جنگ با ایران پوشیده شده.
تحلیلگران دست‌کم ۱۰۳ نماد پهپاد و ۳۴ نماد کشتی رو روی سازه بالای عرشه ناو شمردن.
گروه رزمی این ناو در جریان عملیات «خشم حماسی» (Operation Epic Fury) و محاصره بنادر ایران، ۳۶۹۳ سورتی پرواز رزمی انجام داده و ۴۵۰ موشک تاماهاوک شلیک کرده.
این گروه همچنین رکورد ۲۶۴ روز متوالی در دریا، بدون پهلو گرفتن در هیچ بندری رو ثبت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72994" target="_blank">📅 13:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72993">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=FPzVk72AusfEQo7vzqE9pNIeIuTR-pmDxD4MLyP0etTbfMejUtDdvdH7BhF-BU6dFF7MV-_ZL95NNZjzNYfbB36PU3u3ZedmjGTR08ZJicqUKjxu_vb7yQ0AH91sw30Yr7XhJ3_N5Yfi6QN7XKbpiYykT6p1W4JoG8iQ8JfWv62ynUcBhpEkNzczYSXlLiMNpecpixJ8dNNkdFONOE60ykSuoc0aFJ5wpv0WCFAHVT0K38c9iuH1FZFWNAJWpQpHKEEoFuLJqBzR_EJohiiABl6Xl1tR2WfKvIEAJGGLguj9YMKvr8fIK3u2hKh45k3vorpecdiDPl-u9HFfShl51YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=FPzVk72AusfEQo7vzqE9pNIeIuTR-pmDxD4MLyP0etTbfMejUtDdvdH7BhF-BU6dFF7MV-_ZL95NNZjzNYfbB36PU3u3ZedmjGTR08ZJicqUKjxu_vb7yQ0AH91sw30Yr7XhJ3_N5Yfi6QN7XKbpiYykT6p1W4JoG8iQ8JfWv62ynUcBhpEkNzczYSXlLiMNpecpixJ8dNNkdFONOE60ykSuoc0aFJ5wpv0WCFAHVT0K38c9iuH1FZFWNAJWpQpHKEEoFuLJqBzR_EJohiiABl6Xl1tR2WfKvIEAJGGLguj9YMKvr8fIK3u2hKh45k3vorpecdiDPl-u9HFfShl51YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اسلامی، رئیس سازمان انرژی اتمی ایران:
ایران هرگز از حق غنی‌سازی اورانیوم خود صرف‌نظر نخواهد کرد و ذخایر اورانیوم خود را نیز تحویل نخواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72993" target="_blank">📅 12:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72992">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=St6w0W3cLCE3ZSECw98lwH7kPa_qVyq0zFLe-WHSRzGiXcr_UOhyAJ9Dqp2viKpXhgnyZQ0jhNd8YLItImKmN8LPke9MX4lh6dnPVihhJ4mtjudeGB6EcIIKgqYOE9_VMtnmus9eLCXkFu6ezhpEQLjoQKXUnEB66SWpu4OdvS7hMAq294RY-U-CvykNcezuOaLWxOgr6DVqitrksMcdMvLEuE1n3UjAAlweTRkebOnmtz_m97oJrqYkcjr7my16c_nnrVa4Wg2BC8LO-U1m09Z6kfknaTJ_mZx7W9fO-2cxo4GK_2bzSqZLTM7QAFv-5jvLLEupgynsDwUgMhGhnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=St6w0W3cLCE3ZSECw98lwH7kPa_qVyq0zFLe-WHSRzGiXcr_UOhyAJ9Dqp2viKpXhgnyZQ0jhNd8YLItImKmN8LPke9MX4lh6dnPVihhJ4mtjudeGB6EcIIKgqYOE9_VMtnmus9eLCXkFu6ezhpEQLjoQKXUnEB66SWpu4OdvS7hMAq294RY-U-CvykNcezuOaLWxOgr6DVqitrksMcdMvLEuE1n3UjAAlweTRkebOnmtz_m97oJrqYkcjr7my16c_nnrVa4Wg2BC8LO-U1m09Z6kfknaTJ_mZx7W9fO-2cxo4GK_2bzSqZLTM7QAFv-5jvLLEupgynsDwUgMhGhnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران در حال آزمایش مین‌های جهنده با انفجار هوایی است؛ مین‌هایی که برای پرتاب شدن به هوا و انفجار در ارتفاع طراحی شدن.
هدف از توسعه این فناوری، جلوگیری از عملیات هلیکوپترها و سایر هواگردهای کم‌ارتفاع برای پیاده کردن نیروهاست.
@News_Hut
| C14 News</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72992" target="_blank">📅 12:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72991">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=je4l9mPdh7M-XzvtOcOtavereTRMymVbtkfhSej4oGd03f82OThxSksdgDeXWLnu5ZJ3B_eCTytGAg665A1BSAw9tLGSRyqKD4_6fOy36-cjRm8BmK4wYTzatIN8TZD1GX3w89MZyT_FY2VUPC5PSy6dl7h_UJby-w2gcMud4GROLPbNkMXANCFxiC5wgpcWzCOy7Jxf7-0n3JhCCyA2b8WmXXaSBsBOkVwL9KBDSmVBSThWX8WI7tvgmX60yG4KXm5ip-_3ICaHpg3x_5wm7tWRteU00LdsuNlf6HaSgcfXQV5rDVGOHfhEbKfRzcNcLas5HN0hTkpvTyiSz-G23w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=je4l9mPdh7M-XzvtOcOtavereTRMymVbtkfhSej4oGd03f82OThxSksdgDeXWLnu5ZJ3B_eCTytGAg665A1BSAw9tLGSRyqKD4_6fOy36-cjRm8BmK4wYTzatIN8TZD1GX3w89MZyT_FY2VUPC5PSy6dl7h_UJby-w2gcMud4GROLPbNkMXANCFxiC5wgpcWzCOy7Jxf7-0n3JhCCyA2b8WmXXaSBsBOkVwL9KBDSmVBSThWX8WI7tvgmX60yG4KXm5ip-_3ICaHpg3x_5wm7tWRteU00LdsuNlf6HaSgcfXQV5rDVGOHfhEbKfRzcNcLas5HN0hTkpvTyiSz-G23w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی وایرال شده از سروش هیچکس، رضا‌ پیشرو و حسین تهی از قدیمی های رپ‌فارس در لندن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72991" target="_blank">📅 11:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72987">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtUe_wBy9LA1gZzn5ZEtwQD-1nsM-j1G-zLEJDSVGFogNhii-pwANE-TQgK-DNX9txoOswboclM4lrHnUUqtLnSgZyyJWigjKFUac-_OjK1CI-mDIz_sC9F3n54YEYTwpHoUTPmfIhxoHwe7UDybYfiflKCSCTvYoasG9folLcUpJ79FpuqzUWYHHtGo8J_iyhX2G3wrxQkO9cv0JHn4sK4bFe7DXqRosMj0RPjtz5PySYo237yxPfVjqps5CiionMWcehrr5heWq2-MnUcO79gL1bpHUP9UGqTQShJ60KUx2PNZtABS6pL0yxtTDOtRYs2C3yoxUUA0jwTtNapoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5c0b5VAOgGsTVF4XfjkLtlaVIDO5snbZ8J8uzaM1SjUI4dDVxH2MAMFHVGkaBQ0-ZHpE8n6cgEo5mkVD3Mw5iWMc8Gr35mH1eZPBy3MCfuXhOYQ3mxz3_2Z3pRZYiE1-eD1e9OzTBQTjhFCdsSyGAIN_HakdBtNxGB9vYc7Qa0HFpDerSwhqFi-frgkwBCItOY-K4oj3MjwDwUF4IEs6FECoQY73qKmKvlRuKBsjXUfzm9Bip0sqLA0-4ONi05hS8IWt-ExkopO71WYMM7T7mBnl9ghAMPnU7TJpyGKNFLd96HQEWnu0D3Z-7EAlK7dwY8GHBnx-vNfdqFbpKJvaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bz-oWrnhSb4ZCsgQlANK80ZpTPaByC_RbukDlO1LdhvULsyv72WZnd6U5V-PXkjnIwvDcGEeBCxwRFslOZSvvaoWWFkVyfOuwh1vjUWvwZpulU0wEGu-aMGUk8umiisQj8ueihj_N2nys3qo-LKVOLigSlmGb2CM9dDJx5MwQ2zpkM9TFbQYeZsg-YOW324EanaYrZdv8ft1jKbKCqPYgC4Eg005XPAel3NxiSC_JyIpUNNNmlmzLCVGg6M3VGp8N83IXwUUlyDBFF7WyfhJZWArKXqHe9b-XCNV4SRa08jb8jSsCylW9OtOllCe_JxxlLvp_kb-wTJs7gB5ooLe3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78275c1097.mp4?token=Unz-1QkgbpKLTNCbkcygSDWYKzyri1Vc7xdmVtpLNAk2JcYCbZ3svtA85GKE84bksM1d8eYNM4d8y7VwhyLZW6hgANH6Ql_Fa6_IceBqJmwEB3QnQPIOp9xfy11Rz-wkoTjuGc-WbfbTY46fTPo6_LGuasaFuvcdaIpkCr2zdcHRzfCp6X8C_Ku3OipM28GL6C6qYSScbt2Rz-jW2c4quQi8zPRzntfTYhJsWQ-V0atlbyDYEmz_Qpo8t4BE-GUHHEjjZFEdxVH1ESjblrpBz7zNsZJqbsSGF3mQGmtUPL7bo3K3tFNdq2BHZXK8rSavpCPLz_KkNDTR6Y5HXWQqRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78275c1097.mp4?token=Unz-1QkgbpKLTNCbkcygSDWYKzyri1Vc7xdmVtpLNAk2JcYCbZ3svtA85GKE84bksM1d8eYNM4d8y7VwhyLZW6hgANH6Ql_Fa6_IceBqJmwEB3QnQPIOp9xfy11Rz-wkoTjuGc-WbfbTY46fTPo6_LGuasaFuvcdaIpkCr2zdcHRzfCp6X8C_Ku3OipM28GL6C6qYSScbt2Rz-jW2c4quQi8zPRzntfTYhJsWQ-V0atlbyDYEmz_Qpo8t4BE-GUHHEjjZFEdxVH1ESjblrpBz7zNsZJqbsSGF3mQGmtUPL7bo3K3tFNdq2BHZXK8rSavpCPLz_KkNDTR6Y5HXWQqRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اعتراضات فرانسه از یه نیروی پلیس که خیلی شبیه امباپه‌ست فیلم گرفتن که خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72987" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72986">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72986" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72985">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNaKtFU4Iv0qLb_tPIjVoVGpq7Ip7XqJtCRmkoJmjuK8qnRz_c-JR7u1s2iMzWF8CfJgh31B7hXrdrrxpfhfTUoLJivLkEa0-ujySDhnQe7f9OJFXeytKkJOrDlhnbPi87xq4Y9yPEy0iQIX4L4WxQmWMLiSSWHB2yJ9lfZbgclm4qT1KOTtxA3lkukbmPnAQvFQsLCS72qkXAGUA04VJ0NbHCJ3KMoW4PQbO2D3AabmraQeYrQN3X3J8-iU-Az_qqsKCHt6K8D3_K11C8-4kXyxZlglQJzNgwxo_SHJ58QXv84DU7hHrbos-l-TjZk8tqjY0zy-T7kP_1NtMX5YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیول
🆚
مالاگا
وردربرمن
🆚
دورتموند
لیون
🆚
لنس
صنعت نفت
🆚
پرسپولیس
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72985" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72984">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=OznmB1lcUIl0bA0VUMAjB_JAg6m3YnQPTKqd5q8GM3vibVhtc2aMjbn7YM7Ok4XsXKNIZx9S6ydzD7Dg4r5U_xBiRQ3XnoCIyI546Y2BKQp6rRZxaBCjw53kX5C-FR6kKcLQ-VmsvTeSVLhrR1rT9taSGxt1wFzzDDRUniR8SC8wLRAbDQfs_R-xvEvvHVAg0ruQeO19LFyBeSKo5sn7_WN1xpbaweurpqvhqhtos0AxP5DMgGJ0fp0LNB-T7OihJwE5qBgeOhDhCfE5_NI-W5JGBhnkFSlsIAVHJof-k8zBx41hhOh9GUFtB7moynn5An3JvJl6SpzgPQp2HHzIPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=OznmB1lcUIl0bA0VUMAjB_JAg6m3YnQPTKqd5q8GM3vibVhtc2aMjbn7YM7Ok4XsXKNIZx9S6ydzD7Dg4r5U_xBiRQ3XnoCIyI546Y2BKQp6rRZxaBCjw53kX5C-FR6kKcLQ-VmsvTeSVLhrR1rT9taSGxt1wFzzDDRUniR8SC8wLRAbDQfs_R-xvEvvHVAg0ruQeO19LFyBeSKo5sn7_WN1xpbaweurpqvhqhtos0AxP5DMgGJ0fp0LNB-T7OihJwE5qBgeOhDhCfE5_NI-W5JGBhnkFSlsIAVHJof-k8zBx41hhOh9GUFtB7moynn5An3JvJl6SpzgPQp2HHzIPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
:
زنوزی پول‌هاش رو از کجا آورده؟ رانت؟
نادر قاضی‌پور ، نمایند سابق مجلس
:
بشین سرجات مصطفی، حق نداری به شیرمرد آذربایجان توهین کنی.
شما مردم آذربایجان رو نمی‌تونی مسخره کنی، حواست جمع باشه ما ستارخان باقرخان داریم.
الغدیر مال کیه؟ به ترک‌ها توهین کنی من بلند می‌شم میرم.
سپاه، تراکتور رو هدیه داد به زنوزی! من واسطه‌ی این کار شدم.
شما تو روز روشن داری حق ما رو میخوری.
تراکتور پرطرفدارترین تیم جهانه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72984" target="_blank">📅 11:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72983">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=DCKiFaR82SQ8rdS5WjsuDlMce22xb2MgmtsyDfTztkxdY4nGRjmNb-Kd2Xqn-0_cbxRh_dRz9F7eQAp07ew84WrF9j2b1J-ARkQlNa_ZNbE0-Ga7Xv5itEy5SOkob8xWWO68xX3ts5wHdjuuwhtIkh9Xz3r916lVKJpvOPoqVKZu83i31TpNWSlvA3QAOJIg93bKtCtP2vtNetgvRPgRs8WJuQRLJhNCTduXKyJ6D6hIXHbDDUX30SEmkGf4Jr-NhNu8UQP_Y_LZ8ZxI3wk59zXB0nWUb84FhiGVwb50IhftaGhy7JtDPDoXgARAZHT4L6wnNt7_EAhHOLRu7lbtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=DCKiFaR82SQ8rdS5WjsuDlMce22xb2MgmtsyDfTztkxdY4nGRjmNb-Kd2Xqn-0_cbxRh_dRz9F7eQAp07ew84WrF9j2b1J-ARkQlNa_ZNbE0-Ga7Xv5itEy5SOkob8xWWO68xX3ts5wHdjuuwhtIkh9Xz3r916lVKJpvOPoqVKZu83i31TpNWSlvA3QAOJIg93bKtCtP2vtNetgvRPgRs8WJuQRLJhNCTduXKyJ6D6hIXHbDDUX30SEmkGf4Jr-NhNu8UQP_Y_LZ8ZxI3wk59zXB0nWUb84FhiGVwb50IhftaGhy7JtDPDoXgARAZHT4L6wnNt7_EAhHOLRu7lbtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: گاو که دلار نمی‌خورد، چرا شیر گران می‌شود؟
مدیرعامل اتحادیه لبنی: اتفاقاً دلار می‌خورد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72983" target="_blank">📅 10:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72982">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=mTYWBnKpHDdO9n4quyavRNb2jiEg5G9vhOSD19FggoAwA0Nnj6zowTaqK0YHyEWYCkaQlgTSnmH7Fj1tjQJfhGGUKHxvRpoXKEzvn0LSz5_hYyisuTPOIBLQP6B1lViEbSJCJnQuX1WzHNi5YQGiDvlFFiybKc8xbzd0QeOFX2494izCyzWn9RcARX8VkIuEaOSw3mhrW1FVIl2stadGgM-Az0HTKKoFylOIwqt9HdJzgQO2AKYdhcL0SXmk5aRqEyRziDFMzA3Und7h7wNoJpFzgBfBY8OB2rH2KvqcwEm8sAG9XUkKIiT5q281DUrvuPEAitCD2SIcX70EHCjDXYUW5tDlOJbb8hpB2CFIPUYM2Cdzv5AbmdOeHo9H87dqAgUjWvBG0fX6fLutjLmoAIq9g7gTNIUu0mHKTvV_oE7LSoWpeXgQ9pGpykYeVw81RoFuyJOuVew5I85NJBQTolj8g6wauwHsVfrHLshAUWT_xQKirEe69HCkxzvrd-5PrikgrbGcIEYQoIaTcetGDMLrv-PFBqpIDkbznHZE65FZfmcNnTiyQ0TAZZzE9eDPWEJvEHrx0N6H8wTD5rEJTJb-cZWJ6LudfnN8fQiYrhpkuKinxsJ9-faa7jiV14RhoRZP-q39M-ppv6428LxU1IOfQRCB53Amm5kyODIpudQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=mTYWBnKpHDdO9n4quyavRNb2jiEg5G9vhOSD19FggoAwA0Nnj6zowTaqK0YHyEWYCkaQlgTSnmH7Fj1tjQJfhGGUKHxvRpoXKEzvn0LSz5_hYyisuTPOIBLQP6B1lViEbSJCJnQuX1WzHNi5YQGiDvlFFiybKc8xbzd0QeOFX2494izCyzWn9RcARX8VkIuEaOSw3mhrW1FVIl2stadGgM-Az0HTKKoFylOIwqt9HdJzgQO2AKYdhcL0SXmk5aRqEyRziDFMzA3Und7h7wNoJpFzgBfBY8OB2rH2KvqcwEm8sAG9XUkKIiT5q281DUrvuPEAitCD2SIcX70EHCjDXYUW5tDlOJbb8hpB2CFIPUYM2Cdzv5AbmdOeHo9H87dqAgUjWvBG0fX6fLutjLmoAIq9g7gTNIUu0mHKTvV_oE7LSoWpeXgQ9pGpykYeVw81RoFuyJOuVew5I85NJBQTolj8g6wauwHsVfrHLshAUWT_xQKirEe69HCkxzvrd-5PrikgrbGcIEYQoIaTcetGDMLrv-PFBqpIDkbznHZE65FZfmcNnTiyQ0TAZZzE9eDPWEJvEHrx0N6H8wTD5rEJTJb-cZWJ6LudfnN8fQiYrhpkuKinxsJ9-faa7jiV14RhoRZP-q39M-ppv6428LxU1IOfQRCB53Amm5kyODIpudQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه میخوای بدونی رضاشاه و محمدرضا شاه پهلوی چه کشوری تحویل گرفتن و چه خدمت بزرگی برای این مملکت انجام دادن،
حتما وقت بذار و این کلیپ رو ببین.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72982" target="_blank">📅 10:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72981">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=A8Vz1iab3jO8TGDBkeZ78yt-f6YHYRgGBoMB7_CBZjuAfXON4BEC2SWdbROaXOCkDy0ZvIm9Q0t-4ANfpkWp6bbYQRiwDmQ_xFwm6Pp2hsBMYsrKlTPWoWYFCouhMl2htIY7NfF2ahVOC3fvzKepDsr_blbt-6EJ3zfXYukxXsUfC1WEbZx8x4p2xvZAj4NO7LIRW1-qdJJfPW8TxEPshJ__s6b9AWnAF9hco7waUayFd3t1Gsioud2uqkFV8bGOCymkdC0RsoLtuapCV86ettKZuQM6u3M4i9nxC0vfPmPLSakOStqql_bGz99wuHwjwIBxliFaAaNHT60BYC1RNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=A8Vz1iab3jO8TGDBkeZ78yt-f6YHYRgGBoMB7_CBZjuAfXON4BEC2SWdbROaXOCkDy0ZvIm9Q0t-4ANfpkWp6bbYQRiwDmQ_xFwm6Pp2hsBMYsrKlTPWoWYFCouhMl2htIY7NfF2ahVOC3fvzKepDsr_blbt-6EJ3zfXYukxXsUfC1WEbZx8x4p2xvZAj4NO7LIRW1-qdJJfPW8TxEPshJ__s6b9AWnAF9hco7waUayFd3t1Gsioud2uqkFV8bGOCymkdC0RsoLtuapCV86ettKZuQM6u3M4i9nxC0vfPmPLSakOStqql_bGz99wuHwjwIBxliFaAaNHT60BYC1RNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو گیلان، یه نیسان گاوی و موتوری باهم درگیری لفظی پیدا میکنن و بعد اینجوری موتوره چپ و نیسانه راست میکنن :
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72981" target="_blank">📅 09:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72980">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBf7nxGtEHCojOi6rfbqtXykoXhVD2ptXx78egJy0FWvVbTD1_evtKzrtg-bL5Aw4gzRJO114SzoU38SnZzWogLCUqYQF0H7S0pQmHP2x9b-VmdnrcjiaFeEY1avyMpfZbBuUmgXFWu0oVOdqpic1YQxVbXIcGedJTqlTeBZpfmMDPKK85nViddlFihbp2_2uvEkf5PWvTsAbxYMTfPktdh_G5nTDbYgPQ_cBOctEGpqjEc9TaggVCnohE-iQ7b-o9FcysbP5ZX2BAEapS1vYrYdVl_KPgpTcbDmc8hgzhvrgFDhfPFCNoP1aU5RugaH4J-s5zaca3iO9jetV1zi_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز به نقل از مقام‌های آمریکایی: پنتاگون طرح‌هایی برای احتمال اجرای یک عملیات سه‌روزه با حملات شدید علیه ایران آماده کرده که شامل هدف قرار دادن زرادخانه بازسازی‌شده موشکی و پهپادی ایران، زیرساخت‌های انرژی، مراکز فرماندهی سپاه پاسداران و تأسیسات نظامی می‌شه.
انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات نظامی گسترده آماده می‌کنه.
با این حال، ترامپ هنوز تمایلی به ازسرگیری جنگ نداره و در ماه‌های اخیر پنج پیشنهاد برای عملیات گسترده علیه ایران یا حوثی‌ها رو رد کرده. او گفته پیش از انتخابات میان‌دوره‌ای آمریکا، مجوز حمله رو صادر نخواهد کرد.
مشاوران ترامپ درباره حملات احتمالی اختلاف‌نظر دارن؛ برخی تردید دارن که حملات بیشتر بتونه موضع تهران رو تغییر بده، اما برخی دیگه معتقدن یک عملیات محدود می‌تونه فشار بر اقتصاد بحران‌زده ایران رو افزایش بده.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72980" target="_blank">📅 09:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72979">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y94QRcXCdGquEJ0hxJyLtidty7eUeFVqG4D6E5bHZ_72_O2fTycIf87YQSDxvObolDnM5qvdWia5BQw_HOE8ruCStYBDd6NoFzQFobgOZhFVyuZVZYWFr7lzaU2tZJIryjGjJnBjGC8dRB_sIF6Ehk9TR_FyrVnEH22gG7nlHv_Fx8vBJG8b40fOxR-xDGsXSPzh8GxxZj5pGxMiNGRZ5ZRh_XT89YZVQjvUdBiYZ8fIs6k7GrM6dpUYsT9GSBUKhTAmP3BJEJOQPOVqdHhLlbxpwGEh65xx7VnSn5-2LVvU8iOQJV4U7393bMEBYk11aS3G9h52A_Hc47B1FU0S9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«وزارت خزانه‌داری با قطع منابع مالی، رژیم استبدادی تهران رو از پولی که برای جنگ‌افروزی در منطقه استفاده می‌کنه، محروم می‌کنه و به افشای افرادی که به فروش نفت این رژیم کمک می‌کنن، ادامه می‌دیم.
هیچ‌کس که به ایران برای دور زدن تحریم‌ها کمک کنه، از تمام قدرت و اختیارات وزارت خزانه‌داری آمریکا در امان نخواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72979" target="_blank">📅 07:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72978">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc9Zkyeoc6Ry65Mezh_DXswwe6uI3qZZH2D5kceiZn6SYQM-AIWAGJCM_9ynL2ewGwGzcwber8ACH9P34rqhdRRNkxInf9Rv8LoSj02pZ5pQbK16wm1YpjwFVwS7iS34QMI2xQ3x-P4PJYkynu_hZ6GAfFU7NCh2yWlYx3lp0dAWkfyH5MY4JV9_2PU5nzoEhGyalHg_oVrJeJvZwlP4sJehBLU8RDsyTJ73_7SPdpf7YAGySFTwJDhrGh9rC7XF0MsIg2pcwyv3VhY2aP5Sep4Sfomwvks5ZJY4d0btb-KaNAayYuXLhWwaf5UVGDeIZmZos4wO89VdE5t-LJbYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه شبکه ناوگان سایه ایران
وزارت خزانه‌داری آمریکا از دور جدید تحریم‌ها علیه شبکه باقی‌مانده ناوگان سایه ایران خبر داد؛ این تحریم‌ها در چارچوب کارزار «عملیات مطرود اقتصادی» (Operation Economic Outcast) اعمال شدن.
در این دور از تحریم‌ها، ۲۲ کشتی، ۲۶ شرکت و ۶ فرد مرتبط با شبکه حمل‌ونقل نفت و محصولات پتروشیمی ایران هدف قرار گرفتن.
این تحریم‌ها اپراتورها و شرکت‌هایی در هند، ترکیه، چین، هنگ‌کنگ، امارات متحده عربی و بریتانیا رو هم شامل می‌شن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72978" target="_blank">📅 07:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72977">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72977" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72976">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Zzo8LRqA3lXwgO4CnWlv-cuNoL6fmv7BgzSG_z2k-Dj1QQsc_y3wtiq84XgLU-7cX721b3wXw6AXDGppjjPtlOQqg4v3ICZ0-S9y0EWHgAn8jcXF8LBS4GO0IlCvYi8QcW2A3OwqrjDMFu6JJiuA3gmgQji-w5WJDFEYYZf3YGcC7B5mPmIBHZLxqrLz9WvJI7DwtBOoA4zZ_rHR75HShC--78bJOh3b5TEv_Ez5J6BBOVB9EgcX_7lMGaM63yJ8tQEWTftY8u5PVbGO7c8MJ2x8PxI02GYXX2SvyUIgz7JjazP-dQp6T2Hbhx5vstMIWLZ4RQe2q7B-mdeXvVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72976" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72975">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTOQNxumEKqRvfZcrxbUK0DkEWVpIejKwgYdSttnOug-jUgt1v69GW3iUJkDV8IW3SKeTFl4n86QcxX5izpODZxQbChwVy8jR5vUpr3CmgpwfQmKLYeCae1WeD3Ai8QfVsAkTREQKb5lHSxQzMYf5-a1XD9ytZmDyb9392Dv7KruN3Oq3rVoKTbqTZfUcKT14bmGBIUEssf6jZtR1e8ql0BwB1Q_NEY9JCket_zZimoVFtk03V520ieUt3IFbpzU0bK_lIBirOeuXI3VDwN-iCSWizWjM17HDQmgNB7XSyLfUZhsaylzza9_A_DDTOLQZCRC3FTrAolquVjxsN4NMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی لشکر ۸۸ زرهی نیروی زمینی ارتش:
روز پنجشنبه ۱۶ مهر، مینی‌بوس حامل کارکنان این لشکر در محدوده نیکشهر، سیستان‌ و بلوچستان، هدف حمله مسلحانه قرار گرفت.
بر اساس اطلاعیه رسمی، در این حمله محمدرضا اوکاتی کشته و سه نفر دیگر مجروح شدند.
حال‌وش از تفلات بیشتر خبر داده اما هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72975" target="_blank">📅 01:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72974">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujkkTVcRF5RMeNtnIzsNhf1xJ5R14YI4wX8Jgr3yom3md1DcbLLzIetQFx91e95Fd5itD3_sMxdPG_ybb19OF6oDjJ7CqNBCXNIbwBAO308Iw7s7Cx66AMmW_msmrFyjx_iGh-WkX-fpux8phHiRqCa1C5uEljlgzC4c4_bX0zwU3_xYBZ2xUrcY9HZ8Ft0ozadnEAMkuBTh9tQGrFNQ3csNNYRC8QdJzhpviQzHaPOpGPtX7Mzn177mlH_aUUC9bW4v-KYJWP96XaDeCkW8R2Zh-84dD0-JpXeB-jvovmYMUVj_v72679HjHqIXawXd1h2oQSHAivBVCe6K_1abQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72974" target="_blank">📅 01:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72972">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=Ok4_8jl8pZqpCPGLfX-p-QNMEcjnNCj26iltjKGkcgTggKakRO_klGHp8Y7TJTwC3BJm0mdOhlPgSTivHF3ENtf9Oi_UfgPbWK4guPo_uPDiYy_LLEW9zqz7SRGSptVTv6AvnoD7q6p0D0qWb6Iz1j2l7R7I4Uq-W32nOhKRH4PrXG8JM4iiTB248XaXSNCoaMdFNjDFp1y9xZN_K0b-r_4oqbYke0DykMNCC87F3v5d8kP3ihqiv7CdNc0yP0aej6ncIGIt2APKIlxO1dgNu6gDjsmAfj2P55UxqNuZ7NcgtzvQ00sb2AoDmqLHyEZi0EaRPGCCZoi17rNB2XGeEbc2jFMlga7ybfhBezFEgtY8p-Z556FNLtY_DBoyVPrFE1w_r4cPEgGwsBBF3qnU6wFjJI-TZR3O01G07DFfwAJItPrL-qRQ8dsOYTRFkABb5ewMmilFJDBT9AaR-H07aRtLL23psZzh79pGWygxo91VDJsuOhFyxFTVnxDKnH4ce9k5dfnm92KeEC__1vsdOnAvyYR1Gek_9-q-EBeKne7speFr7iIKvqzYpmiPmi_ZqxvE_FnBNDxEgbwQw1TwQ_Afiic8RAhOcXmmXDehcVkR6YrKn_dpQ9psTxchB8YvUqTsxX_P3mYDNUR9JXcjcWY6sBpqRgHhv2HH-va2YvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=Ok4_8jl8pZqpCPGLfX-p-QNMEcjnNCj26iltjKGkcgTggKakRO_klGHp8Y7TJTwC3BJm0mdOhlPgSTivHF3ENtf9Oi_UfgPbWK4guPo_uPDiYy_LLEW9zqz7SRGSptVTv6AvnoD7q6p0D0qWb6Iz1j2l7R7I4Uq-W32nOhKRH4PrXG8JM4iiTB248XaXSNCoaMdFNjDFp1y9xZN_K0b-r_4oqbYke0DykMNCC87F3v5d8kP3ihqiv7CdNc0yP0aej6ncIGIt2APKIlxO1dgNu6gDjsmAfj2P55UxqNuZ7NcgtzvQ00sb2AoDmqLHyEZi0EaRPGCCZoi17rNB2XGeEbc2jFMlga7ybfhBezFEgtY8p-Z556FNLtY_DBoyVPrFE1w_r4cPEgGwsBBF3qnU6wFjJI-TZR3O01G07DFfwAJItPrL-qRQ8dsOYTRFkABb5ewMmilFJDBT9AaR-H07aRtLL23psZzh79pGWygxo91VDJsuOhFyxFTVnxDKnH4ce9k5dfnm92KeEC__1vsdOnAvyYR1Gek_9-q-EBeKne7speFr7iIKvqzYpmiPmi_ZqxvE_FnBNDxEgbwQw1TwQ_Afiic8RAhOcXmmXDehcVkR6YrKn_dpQ9psTxchB8YvUqTsxX_P3mYDNUR9JXcjcWY6sBpqRgHhv2HH-va2YvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه به مواضع گروه‌های کرد در اقلیم کردستان عراق حملات پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72972" target="_blank">📅 01:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72971">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نیویورک تایمز: انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات‌های نظامی گسترده آماده می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72971" target="_blank">📅 00:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72970">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElIjQTvaJ1CYcW4jp6KCcQ70DHcuWqfinHQwXQ7S9Zgo8IhZq6sK1Eo33tiA5KqXRG8pjj4DIoWRue3lp4HveUPpxul2X7MG6WQsES4Aj9cKZwtPC2nVyMYUntOMK-ldCiPNPz6Li-2GGi-m5gmvrcM96oMikzYOG-U41pFkUSY3BEylSZSAYy2UntVTMIRezL5ys2wEFxOkxqTRjrrcshl_i0tMvn9zQrX2NpmITjGQHGSRQekV2jDBz0LCAnnqKQT52eL4MqDrU_OlHbCsgEC04pkYJUR_l50SoJcEbZthcC4NvkU0OYv_X88YkA8gOXQ15ePu1t7x3FWEigM-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
«رسانه‌های جعلی و دروغ‌پرداز دارن این‌طور القا می‌کنن که من از دشمن دعوت کردم به سن‌دیگو و لس‌آنجلس حمله کنه؛ در حالی که منظور من این بود که افزایش موقت قیمت بنزین، بهای کمیه که باید برای نداشتن سلاح هسته‌ای توسط ایران پرداخت کنیم.
حالا اگه می‌خواید بدونید بهای واقعی و سنگین چیه، تصور کنید اگه ایران به سن‌دیگو و/یا لس‌آنجلس حمله می‌کرد، چه اتفاقی می‌افتاد؟
تمام حرف من فقط مقایسه بین کمی بیشتر پول دادن برای بنزین، آن هم برای مدت کوتاه، با حمله به شهرهای بزرگمون بود.
همه اینو می‌دونستن؛ رسانه‌های جعلی هم می‌دونستن، اما بازم ادامه می‌دن و می‌گن من از دشمن خواستم به دو شهری که دوستشون دارم حمله کنه.
حرف من کاملاً روشنه، اما این آدم‌ها منحرف و فاسدن و فکر می‌کنن می‌تونن مدام به انتشار اخبار جعلی ادامه بدن و از زیرش در برن!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72970" target="_blank">📅 00:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72969">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeQXoJt03s8vDHQHzxp4hKjnoN-C3jeCfwNPq8VLl-dhdozGVRpI9SCBJur3ChvNTYVIhcqIY8vrkKHgYi5dZXa8d2B6KM8Ea0_Ea_ZSfpSi4-Zngwfyk6xQx1zAjz9tvlJ50TjxpnLu2Qs0tyquNQsXg6hJGuFg98s-7vnQGQnfYyROsxmzAnySIc5kMkQFNn9DdMhrdE5TErRBkAyvhaVDVol_T5DioAC-eAaYiyVSc9wwzzxk9kQ3uqkfuK4ltMTZEexgXcZCdmR7ie9SpeDvufjEaWjcjjGJEPCnXWeSzPqX5zHhQbVj3WR6qgt0ldmT2-P5_7R1acEnoU7B_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز 8 October روز جهانی لزبین‌ها بود که به اساتید اهل فن تبریک میگیم
🐸
🐸
🐸
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72969" target="_blank">📅 00:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72968">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=dXZFraorLiJqWYsceQz3lyFJDhqEzU9W5W9aH9KYJY2Ss_TY1jfhMuwc7gEjMWCqviHiYz0ocIye_Ge0q8czOP1rgc7GzjjwXNlRJniUvp5WEEF8UVVJtCqrQxCg-WeGnuok8EeeM1hLKNGh-NCS7nJSPDe1cfNMKEVON2QKlFi660Qvr4DegW_2kbREhQLq5BseanJmBhyKh60OkouPO618R87hJJc8ihGbgOgiFIgMWf3twuZwuB-IaGjRfgyDq4dvdz7wQUIcq7MJ4YO3KtXd1KiomHM7xisShBwMeufLiofO35ZYx-XSdXWUA_pVjizN-zTQb2VXZ4RZ9s3k2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=dXZFraorLiJqWYsceQz3lyFJDhqEzU9W5W9aH9KYJY2Ss_TY1jfhMuwc7gEjMWCqviHiYz0ocIye_Ge0q8czOP1rgc7GzjjwXNlRJniUvp5WEEF8UVVJtCqrQxCg-WeGnuok8EeeM1hLKNGh-NCS7nJSPDe1cfNMKEVON2QKlFi660Qvr4DegW_2kbREhQLq5BseanJmBhyKh60OkouPO618R87hJJc8ihGbgOgiFIgMWf3twuZwuB-IaGjRfgyDq4dvdz7wQUIcq7MJ4YO3KtXd1KiomHM7xisShBwMeufLiofO35ZYx-XSdXWUA_pVjizN-zTQb2VXZ4RZ9s3k2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی دخترا برای پسر خوشگله زندگیشون این حرکتارو میزنن تا دلشو بدست بیارن:
بخاطرت همه پسرا رو آنفالو میکنم.
ساعت کاریتو هم درک میکنم.
حتی عکس دو نفریمون رو میذارم بک گراندم، کی دلش میاد اذیتت کنه خوشگله؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72968" target="_blank">📅 23:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72967">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9487485a01.mp4?token=YktsW5564xmdFBZVEPuegknZ5D1r3xsSxSV83FcaQUuqhqWmfXKjwUhKRoyxFO7HA7w8sc5wp_K-bnXBzYmL8H3NdZF16AKnC4mNk_vhXyUfR9GBcBRlB_cAmy1P3NVmhCSJXiOhWk_1aNTGrnYgljHfzD0JgTfB85PwJRMRScUYTG4gFwQ7h9fsAl7GFDc_-jMt_re29TBsgrkvv4qUxhUmNQB8KuF19T2_WfELqLOkyCeZJLTW5VxttvipI16TSShCE2ZYu09QxSwp7Z5hXP-39n7Mcd_lmrQoghFcyr_L6xa-3Q7cO5mgPQY3osYyDOQJgk4Q2A6NLO8An52AwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9487485a01.mp4?token=YktsW5564xmdFBZVEPuegknZ5D1r3xsSxSV83FcaQUuqhqWmfXKjwUhKRoyxFO7HA7w8sc5wp_K-bnXBzYmL8H3NdZF16AKnC4mNk_vhXyUfR9GBcBRlB_cAmy1P3NVmhCSJXiOhWk_1aNTGrnYgljHfzD0JgTfB85PwJRMRScUYTG4gFwQ7h9fsAl7GFDc_-jMt_re29TBsgrkvv4qUxhUmNQB8KuF19T2_WfELqLOkyCeZJLTW5VxttvipI16TSShCE2ZYu09QxSwp7Z5hXP-39n7Mcd_lmrQoghFcyr_L6xa-3Q7cO5mgPQY3osYyDOQJgk4Q2A6NLO8An52AwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطهرنیا: آمریکا هدفش تغییر رژیم هست اما یواش یواش چون نمیخواد مثل عراق بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72967" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72966">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=gRlMWUv8ODT9a4OcoEDnZXAC22IpXgWpzSMrqqkZH_VQdOG1Unxp_HG_ILiIuWacSnZycsVzql9gs0NyAyWeuOPrin556DSzJFhJ6AYHDK6yrsg9FmQFxiW4yI2L8IntZAl0BpgrWNNRqAMu4L9I2mX27pAUH7_FCZhEigvR2fQv6KGUlZxSQvFPlntNngDFoPAAVZDAqpKbGsn3MNhdXbXiU2X2gKcF0-LxyQbczb8kGe3o8BOVxbIAGGhfPDvSb3_49wlGl2wOfzpMG5pDUxgr2zANiJvwg9oPkzPtlzVzBLBPE1FezK1hSBtqEfLTr0IwLnig53fD_wEqZzR6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=gRlMWUv8ODT9a4OcoEDnZXAC22IpXgWpzSMrqqkZH_VQdOG1Unxp_HG_ILiIuWacSnZycsVzql9gs0NyAyWeuOPrin556DSzJFhJ6AYHDK6yrsg9FmQFxiW4yI2L8IntZAl0BpgrWNNRqAMu4L9I2mX27pAUH7_FCZhEigvR2fQv6KGUlZxSQvFPlntNngDFoPAAVZDAqpKbGsn3MNhdXbXiU2X2gKcF0-LxyQbczb8kGe3o8BOVxbIAGGhfPDvSb3_49wlGl2wOfzpMG5pDUxgr2zANiJvwg9oPkzPtlzVzBLBPE1FezK1hSBtqEfLTr0IwLnig53fD_wEqZzR6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ترامپ رئیس‌جمهوری نیست که بازی دربیاره. رئیس‌جمهوری نیست که زمان زیادی رو تلف کنه.
ترامپ دنبال صلحه، اما حاضره برای رسیدن به صلح، به شکل واقعی و تاریخی، هر کاری که لازم باشه انجام بده.
ایران با داشتن بمب هسته‌ای، اتفاق بدیه؛ نه فقط برای ما، بلکه برای کل جهان.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72966" target="_blank">📅 22:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72965">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=XyFGlaEC70eDMXXbBuClEA96ZD5aydDPV-3knDIkbxCxb1U7MO4b_wyrvJ5qtl4BITeWf2C-DzjU6UnHYvwjJWI2DyMSdhiw1vcWOLvD4OP3GoCh9bxp7qU_-98dr4Ab1YxmSVw8dZw-wZR8QlXOLOfHbtaHowAB5-jAgqydlPwJXy5wE10HF0Lg8UD8S1uX3Dz0kQxMBul-buJU7XO6WcbXQk0GEOXEbiiJrfHkt8IqjyibMorCA6NGHnZIc8Q1As8FlST026DEa6EDeqzKxuq8wIwf3kMSeIZQOTfebxslo7gPypYqw3VS59Hwj5ejH724muXP8RHNF_91JR-Tfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=XyFGlaEC70eDMXXbBuClEA96ZD5aydDPV-3knDIkbxCxb1U7MO4b_wyrvJ5qtl4BITeWf2C-DzjU6UnHYvwjJWI2DyMSdhiw1vcWOLvD4OP3GoCh9bxp7qU_-98dr4Ab1YxmSVw8dZw-wZR8QlXOLOfHbtaHowAB5-jAgqydlPwJXy5wE10HF0Lg8UD8S1uX3Dz0kQxMBul-buJU7XO6WcbXQk0GEOXEbiiJrfHkt8IqjyibMorCA6NGHnZIc8Q1As8FlST026DEa6EDeqzKxuq8wIwf3kMSeIZQOTfebxslo7gPypYqw3VS59Hwj5ejH724muXP8RHNF_91JR-Tfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ما دنبال ملت‌سازی در ایران نیستیم. نمی‌خوایم تعداد زیادی نیروی زمینی وارد ایران کنیم و کنترل مناطق رو به دست بگیریم.
ما فقط می‌خوایم به اون
رژیم، رژیم اسلام‌گرای دیوانه،
بگیم که شما هیچ‌وقت سلاح هسته‌ای نخواهید داشت.
حالا اینکه این اتفاق از راه آسون بیفته یا راه سخت، انتخاب با ایرانه؛ اما در نهایت این
رئیس‌جمهور ترامپه که تصمیم می‌گیره.
و می‌تونم بهتون تضمین بدم که اگر اون لحظه فرا برسه،
اقدام آمریکا سریع و قاطع خواهد بود.
»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72965" target="_blank">📅 22:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72964">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=lD97IQ-BUTC5sJjuSF5t4fsXMLVpKhz8voUi17uNid1uVn5SSKqe8l1brcvX4_rBh4bEuPTMo-3BB7aBySOxDggEmLXYnlr2JyupkjY704vyMKTWOfzjFE1XIBZ5rTgSRdvE3risg9COOPCEsfFtoc7Q2Co8TIgVN5YEiEJgihYDWm9HsXH1yp8VwwfmFGvX6oO87tMJP3XvAOefepdLGsuyjcwPLHLEZQxWTh-oySIbjx4vMd83w_FD4BoK1VcqVIh93KWr7Q4rHreCThS-epGf8QmXBHcEEhEAgr_XhBT_vTGPIAX2R3o_kw-Tjws-xZbAEB-4fb75xv6FPpzUAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=lD97IQ-BUTC5sJjuSF5t4fsXMLVpKhz8voUi17uNid1uVn5SSKqe8l1brcvX4_rBh4bEuPTMo-3BB7aBySOxDggEmLXYnlr2JyupkjY704vyMKTWOfzjFE1XIBZ5rTgSRdvE3risg9COOPCEsfFtoc7Q2Co8TIgVN5YEiEJgihYDWm9HsXH1yp8VwwfmFGvX6oO87tMJP3XvAOefepdLGsuyjcwPLHLEZQxWTh-oySIbjx4vMd83w_FD4BoK1VcqVIh93KWr7Q4rHreCThS-epGf8QmXBHcEEhEAgr_XhBT_vTGPIAX2R3o_kw-Tjws-xZbAEB-4fb75xv6FPpzUAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست درباره ایران:
«ایرانی‌ها فکر می‌کردن توی تنگه هرمز اهرم فشار دارن؛ ما این اهرم رو ازشون گرفتیم. دیگه چنین اهرمی ندارن.
ما کنترل تنگه هرمز رو در اختیار داریم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72964" target="_blank">📅 22:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72963">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=CJBqtMYaptK9PP-WAmOBvFITYCAf4WnVqTefH7O3zDIVATb5O9N2sMeLWsDvaLsbT_c5JMp_imfg7wW_c1iNewM_sb24q5O6fw-GpstJ7rZzeACWqMpeUUSWBESmpKMMZpuEYJLnbFCA6OgAwQcDhBJwPlFz-907-44fkalQqrok2F8wOf9CkjNwSMThaavwzX7cLa34HznApsGtPgNqO31qYd-S4rFgNvRhX2L6VPsST-qkRyp6MlDzyfEBS7I3OGbCqGVn1lXFRcemPOebZwzsvF3p0xmI5Bmkpr2t0bY93PnP5cXvZq5hQwt-MSm7Rs7MYd8BHsRGOAzgPl5GVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=CJBqtMYaptK9PP-WAmOBvFITYCAf4WnVqTefH7O3zDIVATb5O9N2sMeLWsDvaLsbT_c5JMp_imfg7wW_c1iNewM_sb24q5O6fw-GpstJ7rZzeACWqMpeUUSWBESmpKMMZpuEYJLnbFCA6OgAwQcDhBJwPlFz-907-44fkalQqrok2F8wOf9CkjNwSMThaavwzX7cLa34HznApsGtPgNqO31qYd-S4rFgNvRhX2L6VPsST-qkRyp6MlDzyfEBS7I3OGbCqGVn1lXFRcemPOebZwzsvF3p0xmI5Bmkpr2t0bY93PnP5cXvZq5hQwt-MSm7Rs7MYd8BHsRGOAzgPl5GVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایلان ماسک:
«ایلان،
توماس ادیسونِ دوران ماست.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72963" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72962">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voDeUwBtgsHpY5uLDuVXONgUR4RnXBFS1nPA4nvUJeJkE_sMEZBtm8nmL6rRnEHQ5nUFJbsCb21rVMZGm7l6gXxCSZov8RJf4md6N2B1o6DbhjntlozzvuNhfl9TZ1Z-NRhpTVIuZrCp-nX8CUs0AxSPp-qVtEk3ntPF8G7zWcmbyw12LSJYzyQ_zssYHT9w29unQDedN-OgjAyk5g2VcKWpU0j-oIqktXKPBIVnJiV2YBTkwTXUbxr0QY34sCs4CkfdIQkNkdAieT9Rx9NyuDOwkXGFK00kCkDkwFoPwO9lT9FBr3XPMhvVcXFL4A0sIlpt2ZGw-nAnlIqCiYfkwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، ژنرال ایال زمیر، روز سه‌شنبه به مقام‌های ارشد آمریکایی هشدار داد که ازسرگیری جنگ با ایران طی سه هفته آینده ممکنه اسرائیل رو مجبور کنه انتخابات ۲۷ اکتبر رو به تعویق بندازه.
«زمیر نگران بود که ایران در واکنش، اسرائیل رو با حملات موشکی هدف قرار بده. این هشدار بعد از اون مطرح شد که مقام‌های آمریکایی او رو در جریان آماده‌سازی‌ها برای ازسرگیری عملیات نظامی علیه ایران قرار دادن.»
«ترامپ از اون زمان اعلام کرده که آمریکا پیش از انتخابات میان‌دوره‌ای ۳ نوامبر به ایران حمله نخواهد کرد.»
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72962" target="_blank">📅 21:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72961">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=OqP3Sri2iay7W-H0xLUHeFWKdQwiiR-1yAknF9zZzNNeqL-DXEcHJGY8qbmpuhL_vCiPoebpX--ZeydNgh-6BbOhBEwmp_N3bBhlFRJu4rVMhktAtSN97S7VlBTcix02gaQMWrQyAJKjYUEv6mkgCb7PkwD4PVKREDzLrZwgMPsuWS2m7nAp-I6pzfk2w-Xk4DjJno9xB4ypC6WesxG3eER_g_TNAPrkizlg6MMuNemW1HOSenjXC2KIa0pe4-ZA34ZwAM0WKz_dob_pLdBTL8MV9xXljxqpLW-w29qfRBqpWpE5fYX6vZTnIhkjwqRS02GMMVlWc7JR6GZNru65PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=OqP3Sri2iay7W-H0xLUHeFWKdQwiiR-1yAknF9zZzNNeqL-DXEcHJGY8qbmpuhL_vCiPoebpX--ZeydNgh-6BbOhBEwmp_N3bBhlFRJu4rVMhktAtSN97S7VlBTcix02gaQMWrQyAJKjYUEv6mkgCb7PkwD4PVKREDzLrZwgMPsuWS2m7nAp-I6pzfk2w-Xk4DjJno9xB4ypC6WesxG3eER_g_TNAPrkizlg6MMuNemW1HOSenjXC2KIa0pe4-ZA34ZwAM0WKz_dob_pLdBTL8MV9xXljxqpLW-w29qfRBqpWpE5fYX6vZTnIhkjwqRS02GMMVlWc7JR6GZNru65PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیلی معلم به دانش‌آموز در هنرستان؛ سقوط اخلاق در نظام آموزشی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72961" target="_blank">📅 21:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72960">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72960" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72959">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADIodm_HRXBE0rBrLjy-WVIKIah_uPvc9Cd7sKZwDWeTSE-WW4sVztjPlFNkq_gjDa6dMN37cTUzIxJB3guHSGcUmqprZqTzx-dJ8nfgauA3qnKc6lby7cRLryLhm_-nM0QS-QIyZcpi4Q5ctDHxgA6KHinvxZp0ZnjbiKtYmLFX7Tc4MG9EMfRttA5oVXsw6bQ0Oz3mPHMr-jgDIIUL3xVLYZaN8_DQB-G_Iq9DdcppOIw1RcDJmb4OjlIuB5vrRgUhVWL5oXWAL567WgdrjY6hRL20YNKdE38CfAjG7aIwzr42n3aBkBYxuNBJADSY3itCdRzUWwogFizksibduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
ترامپ درباره ایران:
«ما در حال انجام مذاکرات سازنده‌ای با جمهوری اسلامی ایران هستیم.
می‌خوام برای همه روشن کنم که با وجود اینکه ایران هم از نظر اقتصادی و هم نظامی در وضعیت بسیار بدی قرار داره، و با اینکه محاصره همچنان با قدرت ادامه خواهد داشت، نفت با رکورد بی‌سابقه‌ای از تنگه هرمز عبور می‌کنه؛ فقط دیشب ۲۲ میلیون بشکه نفت از هرمز عبور کرد، بدون اینکه حتی یک بشکه از ایران وارد یا به ایران ارسال بشه!
ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72959" target="_blank">📅 20:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72957">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFuvbSO_-2yfbITRzXQ1XuaI0-9OOrqrXYrFECYulvIRNS2XwN2vZCTbrKX1nfEb_1w1DtQS8sBlTV0JZn5O3lKCmyg7lFE53jObYNG__Uvh6U1Q_g276cEVGWWNsMS1cSkCU53YZS5kwB6hcOZTgAL_XpdXwx7ekr9K-EuzwrxdJeRBt8ttZL-A0T4PitpLczYhcaX6YdkLSus8Z1MKi6StM9WxcIqtQWmosOUiscHigMX-MSLxn0y91IioEfJZ6m2IRUjCGDzK1MFBhc8kjo6qE3tHhE13lQcsTgwC-L_ff4x8DXv7PjY6GQbHbethjJPPUdqnIW7yOtiv9Skrtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=Nm2Vnz-pbN9psk9bjR-39VXROMs7Lxxqnt4NDfLVZJyRVqC6xYZbs_NnTSb2m5scfF6a9pNHFsiu_UXi4hDrxyTcwhB-NsTMojn7fTfNoJugZ1UlgdfRuy18jK0B1J9ghIoUyJ22MC9astMX0vQuTpVja5yXigh2BFLm1mDaideHrmGbnBAibXsSeZUP2VtOA40arHL_L9pNx6W7Nerl3AwKG2T-Y7it2N067xHTvq1ZMH9CRIxVkg-2ZwOKinWITw-NQDoaieIwtCP9skUg5EQ_yt7it6adhytb0z9cqNWQusuJf-2eHeBabAxxnuTpEmG1wJXUVThenGU1lt51kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=Nm2Vnz-pbN9psk9bjR-39VXROMs7Lxxqnt4NDfLVZJyRVqC6xYZbs_NnTSb2m5scfF6a9pNHFsiu_UXi4hDrxyTcwhB-NsTMojn7fTfNoJugZ1UlgdfRuy18jK0B1J9ghIoUyJ22MC9astMX0vQuTpVja5yXigh2BFLm1mDaideHrmGbnBAibXsSeZUP2VtOA40arHL_L9pNx6W7Nerl3AwKG2T-Y7it2N067xHTvq1ZMH9CRIxVkg-2ZwOKinWITw-NQDoaieIwtCP9skUg5EQ_yt7it6adhytb0z9cqNWQusuJf-2eHeBabAxxnuTpEmG1wJXUVThenGU1lt51kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر تأیید می‌کنن که یک هواپیمای شرکت هواپیمایی سعودی (Saudia) که در فرودگاه بین‌المللی ملک خالد ریاض متوقف بوده، در حمله موشکی اخیر حوثی‌ها (انصارالله) هدف قرار گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72957" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72956">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=jiJekOgRIMjNhq2yjcibx79y_MTQyzyt1uCgQxwlSmB2BKVzg6HhHubkJYCYoebQwm4I8Onz-S-174CTo8Q_3sVski8091aYEtOFUUR0fyV3mB_MpT3NXZXFXZpERz0Aq09L6gkPxbiS4t4QuCXcVGLBboGxr71RQs6VSWxhONN7eP-U2TOh4u1Fa0e-RIsk_0XHcGJjItHTmASrs6kYmYFyFnwUqCYOGmjwunomxccnbuG17oMaiQMx88Kooz0rMog5EuyYGaAyM3bWI4yjyaWBAWKvoshTyEb-sXgsNxIMm3YWu0JbbeueyrOp_7fmvd6q3MQAkJg56KQobzo2BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=jiJekOgRIMjNhq2yjcibx79y_MTQyzyt1uCgQxwlSmB2BKVzg6HhHubkJYCYoebQwm4I8Onz-S-174CTo8Q_3sVski8091aYEtOFUUR0fyV3mB_MpT3NXZXFXZpERz0Aq09L6gkPxbiS4t4QuCXcVGLBboGxr71RQs6VSWxhONN7eP-U2TOh4u1Fa0e-RIsk_0XHcGJjItHTmASrs6kYmYFyFnwUqCYOGmjwunomxccnbuG17oMaiQMx88Kooz0rMog5EuyYGaAyM3bWI4yjyaWBAWKvoshTyEb-sXgsNxIMm3YWu0JbbeueyrOp_7fmvd6q3MQAkJg56KQobzo2BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:اقای همتی قرار بود وضعیت دلار بهتر بشه پس چیشد؟
همتی کله کیری: فقط به اقای بسنت بگید 3 روز بیشتر وقت نداری
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72956" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72955">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=qSsbp1Wq4N5Q_Ne_i1-GSTZuuFNjNJDKU-wt79Jg79Tdp3UWknWmzclByhuqXF19Tw1q7Gzdrst1I-YH2DUudRdpf_DyNSBT1H0LIsesH2WpWUUGsZU79XPPKw6izL_3lNcvQZe-gGPi-5SV_8tw_Ub7LNU1ESC0CKuJFmduRh8RKniLTjn1BoN0z9LMqL9R9hz92qWw1ftLasd95nrx_T0qnOrCX5P2emsoE2uHltz0q6YmtaCeS3Hg6Tjp5gyqpaT6R5QI6EEXBiJ-b0vciM4Jtw9_4HbSnG8JB8lJb3CHpDnmIvkkoVTXvzYeecjfjJI4Wo1OInMgd1SUYv78fA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=qSsbp1Wq4N5Q_Ne_i1-GSTZuuFNjNJDKU-wt79Jg79Tdp3UWknWmzclByhuqXF19Tw1q7Gzdrst1I-YH2DUudRdpf_DyNSBT1H0LIsesH2WpWUUGsZU79XPPKw6izL_3lNcvQZe-gGPi-5SV_8tw_Ub7LNU1ESC0CKuJFmduRh8RKniLTjn1BoN0z9LMqL9R9hz92qWw1ftLasd95nrx_T0qnOrCX5P2emsoE2uHltz0q6YmtaCeS3Hg6Tjp5gyqpaT6R5QI6EEXBiJ-b0vciM4Jtw9_4HbSnG8JB8lJb3CHpDnmIvkkoVTXvzYeecjfjJI4Wo1OInMgd1SUYv78fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن زنگنه نماینده کاکولد‌زاده مجلس:
قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
البته قرار بود سهم بیشتری بهشون بدین اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری میکنیم که حلش کنیم!
@News_Hut
😐</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72955" target="_blank">📅 18:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72954">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=rdWHjHs1NsQ3A1Ot6cCR-cib2SRoGv6CjC5yA9rQgS5g6ngFGi870b-8HiqQ0E5wOmCBc3g6ZkZfLCzr3Dsc5qRdrEp1TH14XrnXobCbnFhQTB7TPlKQisyJCKevvWLvuOjlgPBfoxyxXAgc55P5dxEVLZrMUNT9NHGahvbYMYRW6JnIPu7KKmB2PDUHs7ExHL3K-jxnwK3H4kDLPmUOUDANLzWbYCC27ybJvuUl0jMRyKduQM9YRHKg7V0_paK3YmyYib9AXvpFdAXo13ti5nMC4HXoISCpbkx0j3jKwgKriplnqH1uCXLtIQS-dLnwPnEYhj3_tDoqqsygT7vIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=rdWHjHs1NsQ3A1Ot6cCR-cib2SRoGv6CjC5yA9rQgS5g6ngFGi870b-8HiqQ0E5wOmCBc3g6ZkZfLCzr3Dsc5qRdrEp1TH14XrnXobCbnFhQTB7TPlKQisyJCKevvWLvuOjlgPBfoxyxXAgc55P5dxEVLZrMUNT9NHGahvbYMYRW6JnIPu7KKmB2PDUHs7ExHL3K-jxnwK3H4kDLPmUOUDANLzWbYCC27ybJvuUl0jMRyKduQM9YRHKg7V0_paK3YmyYib9AXvpFdAXo13ti5nMC4HXoISCpbkx0j3jKwgKriplnqH1uCXLtIQS-dLnwPnEYhj3_tDoqqsygT7vIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌خواید ببینید مشکل واقعی یعنی چی؟ بذارید به لس‌آنجلس حمله کنن، یا به جایی مثل سن‌دیگو حمله کنن. بذارید به یکی از شهرهای بزرگ ما حمله کنن.
اون‌وقت می‌شه گفت
یه مشکل واقعی به وجود اومده.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72954" target="_blank">📅 18:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72953">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=mZ1B5AS29bFA2YD4YuJRNVRQykoUqiIf7arGBdAGZDOdxt_S3obYWWNfuDVRUVYrte4OCIf6TD-531IniXIavqyPZp4yNlYs_nQCohFGT0bVZIpLT0LkuYm8TCAtZ85cDkvnYY2DwNwcYSikFgKVTVvn5LN5AuNvifcD1xofKl8BNmjVxPYMDJsKCO-uo-TuNhfKpqsQvfB8Gpj9BV24J1hmWEOL-tqRrGiN84xIzi388OtzYqCFf4bTbuPJ5uZl3CreuF5d2bWGy9E6dKBsNLRnB0l24qgnA7LR2H-AnpFR7HoBOCofuq2e8QvV6KDt7hJs-Rd3P_HZDeZghMCKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=mZ1B5AS29bFA2YD4YuJRNVRQykoUqiIf7arGBdAGZDOdxt_S3obYWWNfuDVRUVYrte4OCIf6TD-531IniXIavqyPZp4yNlYs_nQCohFGT0bVZIpLT0LkuYm8TCAtZ85cDkvnYY2DwNwcYSikFgKVTVvn5LN5AuNvifcD1xofKl8BNmjVxPYMDJsKCO-uo-TuNhfKpqsQvfB8Gpj9BV24J1hmWEOL-tqRrGiN84xIzi388OtzYqCFf4bTbuPJ5uZl3CreuF5d2bWGy9E6dKBsNLRnB0l24qgnA7LR2H-AnpFR7HoBOCofuq2e8QvV6KDt7hJs-Rd3P_HZDeZghMCKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما داریم ایران رو خیلی شدید شکست می‌دیم. دیگه تهدیدی از بابت سلاح هسته‌ای وجود نداره.
الان اوضاعشون خیلی به‌هم‌ریخته‌ست.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72953" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72952">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=OfbO_s7CcQf6DlXezXzP9fTQp_KcxyWPeZb_mshQddONSOAazpVwgwdJuyeE3Kcc-7VJARmQyWVfctgzLLMhlfZG_lYkSrn-GudeE27wVPjAuz83M96AlyKJlgAuJy0j_DpzWMV9faJ70tGCCxEqizavDZ-7fYTIMGXy8djYm9GhYy7_SmXL4o05kfm5QIJp8HHHSdXs_T2iIzbcwle9fvmar_mbi_TX4Bsq8kjVXXlyuBZgOGci-HBP1jY0SynIZbHRv73bH8X_uib5WThBj_0oARcx_oRWFZ6uDauxqxgif-t39FKdfIFlFJpXjWOHkSLMuOnUpavgPAwnWQuuDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=OfbO_s7CcQf6DlXezXzP9fTQp_KcxyWPeZb_mshQddONSOAazpVwgwdJuyeE3Kcc-7VJARmQyWVfctgzLLMhlfZG_lYkSrn-GudeE27wVPjAuz83M96AlyKJlgAuJy0j_DpzWMV9faJ70tGCCxEqizavDZ-7fYTIMGXy8djYm9GhYy7_SmXL4o05kfm5QIJp8HHHSdXs_T2iIzbcwle9fvmar_mbi_TX4Bsq8kjVXXlyuBZgOGci-HBP1jY0SynIZbHRv73bH8X_uib5WThBj_0oARcx_oRWFZ6uDauxqxgif-t39FKdfIFlFJpXjWOHkSLMuOnUpavgPAwnWQuuDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه پسر ایرانی :
سرمون درد گرفت شماها ولکن نیستید هنوز تو خیابون
خامنه ای رو خاک کردن عمو کردنش زیر خاک ولش کنید
خامنه ای رو خاک کردن شاه رو مومیایی ؛ ایران یعنی شاه
شاه که اومده بود دانشگاه و مدرسه ساخت
جاده خاکی هارو شاه اسفالت کرد و ایرانو شاه درست کرد
اگه شاه اومده بود تخم مرغ نمیخریدیم 50 تومن ماست نمیخریدم 680 تومن
خداوکیلی من تو این مملکت چطوری باید زندگی کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72952" target="_blank">📅 18:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72951">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72951" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72951" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72950">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOA_8bwUr68cF0b6qZdcimrwwhp1sz_MmwkfJvJf8On0i35LNDkDovUKa7qDugiUOoWBYByMYswqRGpMXjJym0S6flwH3C2ihRvv0LScLe8n52K9Eb9ILwz5GBUIh33Auvofnixyti-TsuGcw5WbUgE9INTNXUSWG80KapjcW3HMqAB6bBDjBfoBaU0qHEeH8SAO4oqB901hB6KE3atyo7qO5anJ2G8QdolcXq0iAEwzZ22mkCHlRbazYwFTUS0KK4C_XNxsBgIA-rtvpjuQJLFz5Bd84xPnbIXkP6VyAIDz0ZrdMc5CLKRQY4q26CNxfEh_o5F73vVAhXfTWydpmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72950" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72949">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=QDjmx9WVju3Eoea35FIvRzInoRrBF-0yV2rHayIJl-hokxoMO1BF4hYRgDEXPbCo_XP4wgk4mmckA1xiQ93QNPUHw0iiOAG5fFOTCQAO8L_oJRC8WJse0Y6DSV0nSUmYyqRU2fD_WZPCCM0w3B-uBnPXGXTw9ftBXL4aGrrkgemQS1Ep11yfKgR3tV-gfn9zfoaqn_dD3o27jdJZtDGyRaAdeCmwCzqKrYhZUj5lYctajK0_hhXJt25BTGxs3XmBvPjLe5KuwuYoMgiDaCHf7G279zEupxBI-OaaK-X8e7JO4an7H8grgdx8jqNOTdI3_gYgtMvzmRlc6PCTEnbE6Ume1rutf9ZCO2F9DWIxulGzdSa_y7gN9PvraGWqQPv2xTMGafl5FkWdSNnUfP85GcConYM6wUtLJFKDi6QhU1rTTPwGDtc-yS8foYAwH_yu4lfD147bdXeOb7ESI-MMftlwqqFg9eOZGv1DfU9rEC-c6cKHRggpIYHEVPpRbD0n5dibg8a52nG16KqVf7Y2wFKwUE706GzSAokv7z6uPDo2UlJcyf4KjFmrHay4rbvoUIlKjz7jwkEAEfDR7mZsFIPobKEaptex2FTrvwDCzdsyBQ7ilseXi0dIPaDO00JvlSvCE-xtpaSyEEWh-myE0otO_NfyPERiELYNanIuSR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=QDjmx9WVju3Eoea35FIvRzInoRrBF-0yV2rHayIJl-hokxoMO1BF4hYRgDEXPbCo_XP4wgk4mmckA1xiQ93QNPUHw0iiOAG5fFOTCQAO8L_oJRC8WJse0Y6DSV0nSUmYyqRU2fD_WZPCCM0w3B-uBnPXGXTw9ftBXL4aGrrkgemQS1Ep11yfKgR3tV-gfn9zfoaqn_dD3o27jdJZtDGyRaAdeCmwCzqKrYhZUj5lYctajK0_hhXJt25BTGxs3XmBvPjLe5KuwuYoMgiDaCHf7G279zEupxBI-OaaK-X8e7JO4an7H8grgdx8jqNOTdI3_gYgtMvzmRlc6PCTEnbE6Ume1rutf9ZCO2F9DWIxulGzdSa_y7gN9PvraGWqQPv2xTMGafl5FkWdSNnUfP85GcConYM6wUtLJFKDi6QhU1rTTPwGDtc-yS8foYAwH_yu4lfD147bdXeOb7ESI-MMftlwqqFg9eOZGv1DfU9rEC-c6cKHRggpIYHEVPpRbD0n5dibg8a52nG16KqVf7Y2wFKwUE706GzSAokv7z6uPDo2UlJcyf4KjFmrHay4rbvoUIlKjz7jwkEAEfDR7mZsFIPobKEaptex2FTrvwDCzdsyBQ7ilseXi0dIPaDO00JvlSvCE-xtpaSyEEWh-myE0otO_NfyPERiELYNanIuSR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
« سازمان عفو بین‌الملل یه کلاهبرداریه.
می‌دونید به نظر من عفو بین‌الملل باید روی چی تمرکز کنه؟ روی حکومت ایران که ده‌ها هزار نفر رو در خیابون‌های تهران و جاهای دیگه کشور، خونسردانه به قتل رسونده.
عفو بین‌الملل باید روی این تمرکز کنه که حکومت ایران وقتی معترضان زخمی می‌شن، می‌ره سراغ بیمارستان‌ها و اون‌ها رو روی تخت بیمارستان می‌کشه؛ تازه گاهی پزشک‌ها یا پرستارهایی رو هم که اون‌ها رو درمان کردن، می‌کشه.
این‌ها جنایت جنگی هستن، جنایت علیه بشریتن و جنایت‌هایی هستن که این حکومت علیه مردم خودش مرتکب می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72949" target="_blank">📅 17:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72948">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=ostUQMNMrbE4oG6vIy_oe3Qjswcx0ShFZOEDUC3wlV2P_0fUVR9SVrvggAlrZKQw7jHe2v3D8hrn_WWSOrhA5hWnrBf1loZN1b0CBHBBVFPACJsVzJ3-l6Mg-DX2KmX0TX6ctEBfFTo9ITKdL5g0lHQ42kAcFQBw_qANqbUSLswYy7cHOylAuABmV7PO0bVRofRZasdPRVUHDaV-9lwhkf_yINNDvf1gHUnwR33VLcqr6XKRzc5wfvsA89PKB3LxdHBKpwBfUUfCYPZgVcEAUBPT9rgCNHfvD2CrR2paqQZb6icPKP6cjGgdkUapAtvZUexIpOUAbFskRQvaaJLaDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=ostUQMNMrbE4oG6vIy_oe3Qjswcx0ShFZOEDUC3wlV2P_0fUVR9SVrvggAlrZKQw7jHe2v3D8hrn_WWSOrhA5hWnrBf1loZN1b0CBHBBVFPACJsVzJ3-l6Mg-DX2KmX0TX6ctEBfFTo9ITKdL5g0lHQ42kAcFQBw_qANqbUSLswYy7cHOylAuABmV7PO0bVRofRZasdPRVUHDaV-9lwhkf_yINNDvf1gHUnwR33VLcqr6XKRzc5wfvsA89PKB3LxdHBKpwBfUUfCYPZgVcEAUBPT9rgCNHfvD2CrR2paqQZb6icPKP6cjGgdkUapAtvZUexIpOUAbFskRQvaaJLaDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنج اصل عدالت اجتماعی شاهنشاه آریامهر برای ایران:
1- غذا برای همه
2- سقف بالای سر همه
3- آموزش رایگان برای همه
4- درمان رایگان برای همه
5- اشتغال برای همه
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72948" target="_blank">📅 17:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72947">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=aSKHt6QoJGPuNs204-5GSjR4ngJ50O5I692rPtMvTY1snOm-7J44m8hOlqLIZ8yCK9xZNZ54M0nYzfEndNz-xL5RWzoy1jsxTFtvnavCe_4Ma08Ut_39HzYWooTKSATdzCfX37BYzHwMQPdT6DWPyFO-g6y10REpwSjb7ANAH0G9jSPv_vbq3sTN9qOSwBxfeUHLRG0S923BKFfZ8S9AWW2trLhZx71_UPIJKB43AUxATOPq1gtnJydGUhS_wqSz_9jn54PuyeijF9zcDfJUDSskjjGxqddJgQoGTviFopuBRtRt5P76bG9asa5_G38w2zJRsoSo2WbZt0IRFjL5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=aSKHt6QoJGPuNs204-5GSjR4ngJ50O5I692rPtMvTY1snOm-7J44m8hOlqLIZ8yCK9xZNZ54M0nYzfEndNz-xL5RWzoy1jsxTFtvnavCe_4Ma08Ut_39HzYWooTKSATdzCfX37BYzHwMQPdT6DWPyFO-g6y10REpwSjb7ANAH0G9jSPv_vbq3sTN9qOSwBxfeUHLRG0S923BKFfZ8S9AWW2trLhZx71_UPIJKB43AUxATOPq1gtnJydGUhS_wqSz_9jn54PuyeijF9zcDfJUDSskjjGxqddJgQoGTviFopuBRtRt5P76bG9asa5_G38w2zJRsoSo2WbZt0IRFjL5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر جوگیر شد و می‌خواست جلوی چند تا دختر خودی نشون بده که این شکلی بگا رفت:
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72947" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72946">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=OPUVmxaOf3wCYwGj6N82qo38groAVS3I7SqojOtlkeLqF1HqNWdZM90duJbEWf_G-nz_OSmpP76kn9xBcAje0NKZjOI7eJaJe_Zkth0NDe1zi8T5s-HApxSex_BgiYJ7GsyXraFhDAPU0XdSE5njjFvztyIF2OAxAT5vlNGx3oUPneKoMz4xyQBf_HNi8PrlX7KcA9qXICaNQjzipV7PdiguxVvACAYM-KJoHi31TCKa-cp3GUJR3G7ovDNlOxwhYRFMbG1kH74qaVnDS7SkdGgceo1yCgDqx70NQOxq-zol8ZvMmI9LJFp85G8aRMYfZoz_ZdaZ-13fdM2FbG0uPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=OPUVmxaOf3wCYwGj6N82qo38groAVS3I7SqojOtlkeLqF1HqNWdZM90duJbEWf_G-nz_OSmpP76kn9xBcAje0NKZjOI7eJaJe_Zkth0NDe1zi8T5s-HApxSex_BgiYJ7GsyXraFhDAPU0XdSE5njjFvztyIF2OAxAT5vlNGx3oUPneKoMz4xyQBf_HNi8PrlX7KcA9qXICaNQjzipV7PdiguxVvACAYM-KJoHi31TCKa-cp3GUJR3G7ovDNlOxwhYRFMbG1kH74qaVnDS7SkdGgceo1yCgDqx70NQOxq-zol8ZvMmI9LJFp85G8aRMYfZoz_ZdaZ-13fdM2FbG0uPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو گرگان یه دختر 19 ساله میخواسته خودکشی کنه که اینطوری نجاتش میدن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72946" target="_blank">📅 15:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72945">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=jJsNNdl1s0r7OgdTD7Hy377uBS3Aa7qyNivPH4WtBKZQvFLgWxB63NljQfj7MP3Vh7k4xILz8ENvsGp1fYcVmPi6Y6C3SD7qruti2uZCnvRmbJX1LHWzEabbFtYYqIQPRZSK5Cta1WmMmklToI68JNvxGfFP1nw4EhrvFKqIWSJSMMMUP9KNN9J5NJN8ZUDn09-fO7bcAafbU2bvTD4Ld2iyCy1yJnFToJpfgx3YCcenDCAsddvQogJ8FeKdRrMMpY-fF0TgrhJOOu8eQZyIlA4aeN6evPXzPEmXWgep07ujm3rVAIuJmQs3dHw-wGWBSuRa9tIa3VJmGeSdhxA9ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=jJsNNdl1s0r7OgdTD7Hy377uBS3Aa7qyNivPH4WtBKZQvFLgWxB63NljQfj7MP3Vh7k4xILz8ENvsGp1fYcVmPi6Y6C3SD7qruti2uZCnvRmbJX1LHWzEabbFtYYqIQPRZSK5Cta1WmMmklToI68JNvxGfFP1nw4EhrvFKqIWSJSMMMUP9KNN9J5NJN8ZUDn09-fO7bcAafbU2bvTD4Ld2iyCy1yJnFToJpfgx3YCcenDCAsddvQogJ8FeKdRrMMpY-fF0TgrhJOOu8eQZyIlA4aeN6evPXzPEmXWgep07ujm3rVAIuJmQs3dHw-wGWBSuRa9tIa3VJmGeSdhxA9ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هیچ کاری نیست که بخوایم یا لازم باشه در قبال ایران انجام بدیم و
هنوز نتونیم انجامش بدیم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72945" target="_blank">📅 15:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72944">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=s3h1C51-KmUVkDtWAgW4Nl30l-y7iIL1F9frHQ8g6Bq_rxnzyk1UiJ8O2zQ3ysElnjskKYumKW5Kq4gBbUZBQJ5_uu6_QftsUCPY7lbcn22tjsmR4S3u7m1WpcJ6yQJ6aPlR5z4hcPb9TflMusOG9v-FFEBOARtUORKHJufhZzqrQiPaaW1NY1o68YkYNN9QA5kh_JufOIsaRm98gbyYvkjZyTOE0BsbhZ8glDg_Ir28wwqZKy_8G7iKX-86LgNnpYsveygbZTzNYkmrbsMyr5Q9JDHKLB_CqCjw-U_V0_vn-HlhDbu79rTjP9XS_UDVe2CBUxmH8YN8StgO8uW4fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=s3h1C51-KmUVkDtWAgW4Nl30l-y7iIL1F9frHQ8g6Bq_rxnzyk1UiJ8O2zQ3ysElnjskKYumKW5Kq4gBbUZBQJ5_uu6_QftsUCPY7lbcn22tjsmR4S3u7m1WpcJ6yQJ6aPlR5z4hcPb9TflMusOG9v-FFEBOARtUORKHJufhZzqrQiPaaW1NY1o68YkYNN9QA5kh_JufOIsaRm98gbyYvkjZyTOE0BsbhZ8glDg_Ir28wwqZKy_8G7iKX-86LgNnpYsveygbZTzNYkmrbsMyr5Q9JDHKLB_CqCjw-U_V0_vn-HlhDbu79rTjP9XS_UDVe2CBUxmH8YN8StgO8uW4fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
«روند مذاکرات همچنان ادامه داره و پیام‌ها از طریق میانجی‌ها رد و بدل می‌شن.
ما پیشنهاد خودمون رو که اسمش رو «طرح هفت‌روزه» گذاشتیم ارائه دادیم و دیدگاه طرف آمریکایی درباره این پیشنهاد رو هم شنیدیم.
الان داریم نظرات آمریکایی‌ها رو بررسی می‌کنیم و فکر می‌کنم طی چند روز آینده پاسخ خودمون رو ارائه بدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72944" target="_blank">📅 15:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72943">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612c679392.mp4?token=t1QAM3XGM0IpELH2ohMOCtWJaZ4GRqlhCetPf11_DuLa4M6aXCNwbMO-Lu28fWtu-CjHDkjCSJsYoEWnzu58n_O20A66cQv1deVAjELjU6nl2lG4hvbI2mmlyNtP6MstjcVd0YbYX2yUVfSVV8JEMv6rnXC7jdhkdq97zXqzsrDxXGfMViowQ1DgHIcr0ubrZ77ypbb0UFVeSMgRp-fsQUxqJL8s12AA9mArJGnJaBWbOU3ZUTVWGifU_SCiTXxRnA8x2AghRnm6NTyL1Qm9h6HLfEQxQnUc3_CauOiSGwG8eTI9TmQuO9enYz7MBnwt4LK4b9TAdCaf1q7f-B-auw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612c679392.mp4?token=t1QAM3XGM0IpELH2ohMOCtWJaZ4GRqlhCetPf11_DuLa4M6aXCNwbMO-Lu28fWtu-CjHDkjCSJsYoEWnzu58n_O20A66cQv1deVAjELjU6nl2lG4hvbI2mmlyNtP6MstjcVd0YbYX2yUVfSVV8JEMv6rnXC7jdhkdq97zXqzsrDxXGfMViowQ1DgHIcr0ubrZ77ypbb0UFVeSMgRp-fsQUxqJL8s12AA9mArJGnJaBWbOU3ZUTVWGifU_SCiTXxRnA8x2AghRnm6NTyL1Qm9h6HLfEQxQnUc3_CauOiSGwG8eTI9TmQuO9enYz7MBnwt4LK4b9TAdCaf1q7f-B-auw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک جت جنگنده F-16 نیروی هوایی ایالات متحده که در حال سوخت‌گیری توسط یک هواپیمای تانکر سوخترسان KC-135 در جریان انجام ماموریتی در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72943" target="_blank">📅 15:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72942">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=AaoIlWaOEjmbKwEJkgEU5Kbo9J05IuBasCpU9rjHDNnIBYmfDO_7iLCH-dhNDIYCOgjROQt_YOCGw7vekvkmtir2X7o_Z8b1w8r0Q-a45jjlysHzAevLsib_lgVL1QQBQz3ITjjDs2bmyXifiQxNr4DgmiDbcdXM9bo8xP8hq_DURqrxNksAiwrAr7Rtr6vZWi-i_qHOLH9Wyd7x99e7zUNIYG6ePv0zb0iS5u5gqc7sgbgR803AQLXYacgj1JLrVs_-WanQnCX_0LjChUyWHnHjyQgfmt9oCe0hLxpHx8fLS-DG26eyuM6Iyee4AkYqlNVcg0aUC80N9Ac93Qff8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=AaoIlWaOEjmbKwEJkgEU5Kbo9J05IuBasCpU9rjHDNnIBYmfDO_7iLCH-dhNDIYCOgjROQt_YOCGw7vekvkmtir2X7o_Z8b1w8r0Q-a45jjlysHzAevLsib_lgVL1QQBQz3ITjjDs2bmyXifiQxNr4DgmiDbcdXM9bo8xP8hq_DURqrxNksAiwrAr7Rtr6vZWi-i_qHOLH9Wyd7x99e7zUNIYG6ePv0zb0iS5u5gqc7sgbgR803AQLXYacgj1JLrVs_-WanQnCX_0LjChUyWHnHjyQgfmt9oCe0hLxpHx8fLS-DG26eyuM6Iyee4AkYqlNVcg0aUC80N9Ac93Qff8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا پسر رفته بودن بیرون که دیدن رفیقشون اونارو پیچونده و با یه دختر اومده بیرون،
این لاشیام رحم نکردن و اینطوری شرف رفیقشون رو بردن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72942" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72941">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=WW87ws5NWuu5dADNxh4FtREm0MSLx0qc9vjibknx0BbdzLU7s-NPs_CtRm11y-Y8cELC96YqMjpQEQQnYc38VNBhtSyySNcK946tGoUpIx_o9ZjHc6YfaardqxFOLmWY-veKhEZzlvAkmcIa0D2Mm0wN5TumqW_Bt9A-woyunhr_TP3s-pIsuQxQczlxd0nF97nAiu217R5BI19u6eImHR_QLYBGBJgfI1uM0Km7IYRqv45qgQHxbTcLYE33SG7edx3K9Tfv9rpURLrC2FZsd7bM7MJaJHGlvCUXZ4EAyYCrg1lron7jszRW5UYlyO_Np29zkX1NZOBlFKw23tihqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=WW87ws5NWuu5dADNxh4FtREm0MSLx0qc9vjibknx0BbdzLU7s-NPs_CtRm11y-Y8cELC96YqMjpQEQQnYc38VNBhtSyySNcK946tGoUpIx_o9ZjHc6YfaardqxFOLmWY-veKhEZzlvAkmcIa0D2Mm0wN5TumqW_Bt9A-woyunhr_TP3s-pIsuQxQczlxd0nF97nAiu217R5BI19u6eImHR_QLYBGBJgfI1uM0Km7IYRqv45qgQHxbTcLYE33SG7edx3K9Tfv9rpURLrC2FZsd7bM7MJaJHGlvCUXZ4EAyYCrg1lron7jszRW5UYlyO_Np29zkX1NZOBlFKw23tihqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت مارکو روبیو درباره حمله و تصرف آتن در جریان لشکرکشی خشایارشا به یونان در سال ۴۸۰ پیش از میلاد:
۴۸۰ سال پیش از میلاد، در جریان لشکرکشی خشایارشا، پادشاه هخامنشی، به یونان، ارتش ایران به آتن رسید و بخش‌هایی از شهر و بناهای مقدس آن را ویران کرد.
بیشتر مردم آتن پیش از رسیدن سپاه ایران، شهر را تخلیه کرده و با کشتی به جزیره سالامیس و مناطق اطراف پناه برده بودند؛ اما گروهی از مدافعان حاضر نشدند خانه‌شان را ترک کنند.
آن‌ها در دژ سنگی آکروپولیس سنگر گرفتند تا در برابر سپاه ایران آخرین مقاومت خود را انجام دهند. مدافعان با پرتاب سنگ از فراز صخره‌ها تلاش کردند نیروهای ایرانی را عقب نگه دارند و برای چند روز در برابر بزرگ‌ترین امپراتوری‌ آن دوران مقاومت کردند.
اما سرانجام سپاه خشایارشا موفق شد آکروپولیس را تصرف کند. ایرانیان معابد و بناهای موجود در آکروپولیس را غارت و به آتش کشیدند و بخش زیادی از آن را ویران کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72941" target="_blank">📅 14:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72940">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=etEAP5bqEpykb3oDiB2aOrZg7rWw8AFvIYKCc1wT_-FxLIrqlLn05SZiRNKO8L0JkVm7isEqgRreCgmwYwNosELboJuFLzyBx9ovNuWp_iCo27jiJ4tckgQ2ZNwv-fJWh6fA4LlxMXa5OL9m_obdrNY_shQaeiOHr4KMi-KK_QHjK_7wpKmY8_CsYmy7IcPzf--cHS695mqQbtI0rQ9owt220UBGVpXq8QRUDmoZ_qN0bIjsx5B5umwOHo3fndA2IRMHZk2BKCrPCAFjCqgVdR8oXFRlWku4DKUdPm2uLIJdsypJAEy5R2xdDigTlFG0_O5EWu2pGoRJct63czc2Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=etEAP5bqEpykb3oDiB2aOrZg7rWw8AFvIYKCc1wT_-FxLIrqlLn05SZiRNKO8L0JkVm7isEqgRreCgmwYwNosELboJuFLzyBx9ovNuWp_iCo27jiJ4tckgQ2ZNwv-fJWh6fA4LlxMXa5OL9m_obdrNY_shQaeiOHr4KMi-KK_QHjK_7wpKmY8_CsYmy7IcPzf--cHS695mqQbtI0rQ9owt220UBGVpXq8QRUDmoZ_qN0bIjsx5B5umwOHo3fndA2IRMHZk2BKCrPCAFjCqgVdR8oXFRlWku4DKUdPm2uLIJdsypJAEy5R2xdDigTlFG0_O5EWu2pGoRJct63czc2Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانگیری: از سال ۹۷ تاکنون چین حاضر نشده یک بشکه نفت به صورت رسمی از ایران بخرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72940" target="_blank">📅 13:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72939">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حمله ایران به پایگاه آمریکا در کویت؛
طبق تصاویر جدیدی که CBS منتشر کرده، ایران در روزهای ابتدایی جنگ، پایگاه آمریکا در «کمپ بوهرینگ» کویت را با موشک‌های بالستیک، پهپاد و جنگنده‌های F-5 هدف قرار داده است.
در این حملات، انفجار و آسیب به ساختمان‌ها و تجهیزات نظامی دیده می‌شود. یکی از شاهدان گفته جنگنده‌های F-5 آن‌قدر نزدیک پرواز کردند که حتی کلاه خلبان‌ها را می‌دیده.
@News_Hut
| CBS</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72939" target="_blank">📅 13:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72938">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJuVmRbzMZZCa2KZuQgydYUpmwB8jTXt5Bocz18Rst5Px04h5W5Oo-QFVDxGW37optGTG438ySPVQuSCJMT1JatQi54nN8t_7em1UWTOV8eFOmaj9pHHcyIFt4gq2zv7ZlIXQi22FgS2xh5dodtuqIoKYLpvhL7uIVp-elZKcKRU0so3Y-0QJp9QLG2GvgvT4cG38d8jI16LkNfQEXkTMAa9rdprhKhm3t5a0obAz9UGB2G-H5_bl0MYMMZzPsLpbnUf6hoK3aiBLbAgDm3FupLzV6Pq4FiY8LoMEgj-M-IvJdKrJdHfQgxbw9g3a6PByxiror9zsxLNSvAQD8-HYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی:
لئو، سال‌ها برای کشورت جنگیدی و یه تاریخ موندگار ساختی. بابت همه چیزایی که با آرژانتین به دست آوردی، دمت گرم و کلی احترام برات قائلم. بغلت می‌کنم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72938" target="_blank">📅 12:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72936">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV7s335yWHv46O67Zf41EYySoyT_SBodUFs8ROkt9RY_U_wTiY5WK-Ni0Glk4h3-jrGcwuq69OjXz1cAEhCH2hyFP5WcNLA1XE7y_Cft-KvrEMGaAZ5Lw8mH_TEEjk8uWkO3YC6Fk4A2AMQFK39UjCGBK1GDQRDhEzUEiLbD5M2MseViPa5NhFJpZItC1eU9-s0r1IFkXxXa7sMD35SlDQ34t2RQFnZQpj1Y1Z3INbzeilsXo2vfBijdxsoaDEwyJ3aTkg6wKqDmAJmOwR73KULPZfG85qooQcLJE4k2s16qXD4FMQmKBNHcbZ_zT2L9nZ-STItYMQAn_UHej6apRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=eMfXJKb0-UI-TNhz0EDPko6VUn2LJCi8QHb0CNv-quebsSJdCZYleolKL-atjF5nUYooFu07qY8gntfi3pyk1FNBK81pol8naq42naerEkRYs8PwnAZZ_Pemqc7hGUcgmbEH--B2w17TXDYJyYKeSX3wWsnI7J-1Ey2IzgE-tfO5kiZD1frSK2kgyq9i4_48rGQDaMeV3OmPMRWqxQ_XErWJgJq2eJDtkMIjAQg3mPCN8-DX_35HnssrcPLavrCZpII-b60qoNKSMPOKZQIZcdUpKXRU-dZEmKJLbnDgFis36O74uEf1ZR_tln7JsBWJxmfmVPwmK-FuTCTUeVngDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=eMfXJKb0-UI-TNhz0EDPko6VUn2LJCi8QHb0CNv-quebsSJdCZYleolKL-atjF5nUYooFu07qY8gntfi3pyk1FNBK81pol8naq42naerEkRYs8PwnAZZ_Pemqc7hGUcgmbEH--B2w17TXDYJyYKeSX3wWsnI7J-1Ey2IzgE-tfO5kiZD1frSK2kgyq9i4_48rGQDaMeV3OmPMRWqxQ_XErWJgJq2eJDtkMIjAQg3mPCN8-DX_35HnssrcPLavrCZpII-b60qoNKSMPOKZQIZcdUpKXRU-dZEmKJLbnDgFis36O74uEf1ZR_tln7JsBWJxmfmVPwmK-FuTCTUeVngDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریوش بزرگ؛ نامی که پس از بیش از ۲۵ قرن هنوز در تاریخ ایران می‌درخشد.
پادشاهی که ایران را به یکی از قدرتمندترین و سازمان‌یافته‌ترین امپراتوری‌های جهان تبدیل کرد؛ از ساخت تخت‌جمشید و گسترش راه‌ها تا سامان‌دهی نظام اداری و اقتصادی کشور.
داریوش تنها یک پادشاه نبود؛ بخشی از تاریخ و شکوه ایران بود؛ نامی که قرن‌ها گذشت، اما از یاد تاریخ پاک نشد.
امروز، به احترام مردی که نامش با شکوه ایران گره خورده است؛
یاد داریوش بزرگ گرامی باد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72936" target="_blank">📅 11:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72933">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEYB-7SCpNuMbMkpG5UlSIpYQ_1GVisJCZHGH1XrkmVIKnF-B3gvl-hJojLqnDjICQXBaQ-fY7xzeMPKwApitmBQ-P1V-DstBFKJ9q5lk2Je6mQgfM9QYh4P7MjZAE-2CbOydcB9Vl4iEwhVYzfW5vhPcWFaha_H28N92hROGZUPVY4X6S1RzXM9iT79Nh3iPLBvTUrJkt0a7MNneC0u6kV8NFsr3mobYRSQTkb8gZLYUEqtVnFX-557m9DAc0zq6yJeq7FQLh6qMTBcQ5iKWgiDyxYS0Tg4Zo6zah6iyJWLaYbH-Eiv01TY8JiXfIAIhP5IJv7YPrVK97wtwf8vmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۲۴ ساعت گذشته، ۱۱۰ فروند هواپیمای نظامی در منطقه شناسایی شدند که شامل موارد زیر بود:
۱۶ فروند هواپیمای ترابری ورودی از خارج از منطقه (متشکل از ۱۱ فروند آمریکایی
۲ فروند بریتانیایی
یک فروند ایتالیایی
یک فروند آلمانی
یک فروند با مبدأ نامشخص
۱۰ فروند هواپیمای ترابری نظامی منطقه‌ای
۳۳ فروند تانکر سوخت‌رسان هوایی
۲۱ فروند هواپیمای شناسایی
۲۶ فروند هواپیمای ترابری نظامی فعال در داخل منطقه
۴ فروند بالگرد نظامی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72933" target="_blank">📅 11:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72932">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlm80S0JPdYr0vnPy2y36heYvXtdIbV4j8Ht7zpmYf5kxW9HyZXzILb1PNidhbKnyk_5eXp4fB88J06rNUuFKbYTYyWEKP5Dw_wiRjKFGXhKda7d8KUMmzq6UycQjqxUhKsKwqRtAjssG8qPiOvXJNjKKUqPz6gI2zkBoKbzQVZRBfUSHd0qlIxD8dzGzmTFBcuyHmFs1z3LBeRGtBKVVXE0khvgXyeTn1J30MSgNeb6VEwa-NaDhoVq1yt7A2QqpyVjwSkuA40zFAmxftbZz8fUv8ElQZv9QwQNdwyq7LDyzRMifsREl2Xx_pIGg8_UmrJt0YnY3AlN2b4I9abA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
پنتاگون به ارتش آمریکا گفته خودش رو برای حملات احتمالی دوباره به ایران آماده کنه:
طبق این گزارش، هنوز دستور نهایی حمله صادر نشده و ترامپ همچنان درباره زمان و اصل حمله تصمیم‌گیری می‌کنه.
اگه حمله انجام بشه، احتمالاً اهدافی مثل تأسیسات هسته‌ای، زیرساخت‌های انرژی و دیگر اهداف راهبردی ایران مورد حمله قرار می‌گیرن.
منابع آمریکایی و اسرائیلی می‌گن احتمال انجام عملیات قبل از انتخابات آمریکا و اسرائیل مطرحه.
همزمان، تیم امنیت ملی ترامپ درباره جنگ جلسه داشته و ترامپ هم طی چند روز اخیر دو بار با نتانیاهو تلفنی صحبت کرده.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72932" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72931">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72931" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72931" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72930">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3wcVDhHM2F1bfP_RKSi_ZjCCwek5MlvBx8bMkWP5BOPlnaQ4lHa0iJCmgQA1OjtK51NuQ3THeibp7JC82ra1gzJzJV26TVQ34afu82qoh3M9I0XxxATCmt2ax3ZwnC2yutFGRp8VrHunPRUtES-lcw1lxFPUxCI7akAGKE1WmHapCjT-m-7oJu6Z3pen3I2S5Yk_zk2EmtrF78KG01HWRFDc39Cv-s-AjF4MLIVGKREBCZA_FLXuWnouAdqetQCGYsldbdlNbXhvIUJQS_BzXmJ_q1cHw8YsNmFu9htOxCoXt8j5ZIVQO0desYQxJGq7RdtAU4xr4e0YNi_9OF1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تراکتور
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
⚽️
تراکتور: ۳ برد، ۱ تساوی، ۱ شکست و ۶ گل زده
⚽️
استقلال: ۱ برد، ۳ تساوی، ۱ شکست و ۳ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72930" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72929">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=kDkA-Ccwk0quSw9PS8I7pWVsgCAoP4eE_jZSLWHFRzzECzPhujY0KImcRMGp4aKB6oe7IaCerGscwEAJQZ7fpLw0TjAiO_AWraMFdSTF7KAOQvDwPV1QqqUbOtbpdeq5G6XTcmQKa-nptuwDX02o0rVMoFPw3JLBtGXHnzwwWyuPrCVUg0lbQd6LPPe68WSIGbuve_SqAil4pFeWmYrOuCLMMQQCZRRsR2uFhhWiFLMeVI128GpbMgr7V3F5DkdZo-8V2Tvnq7dY3cQ4aTVb9MpyQJ7Egros24JrmXyisbo6pNz_8yz0fBRzURc-uKkUhAqfWg-jNd72xSlHKt685g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=kDkA-Ccwk0quSw9PS8I7pWVsgCAoP4eE_jZSLWHFRzzECzPhujY0KImcRMGp4aKB6oe7IaCerGscwEAJQZ7fpLw0TjAiO_AWraMFdSTF7KAOQvDwPV1QqqUbOtbpdeq5G6XTcmQKa-nptuwDX02o0rVMoFPw3JLBtGXHnzwwWyuPrCVUg0lbQd6LPPe68WSIGbuve_SqAil4pFeWmYrOuCLMMQQCZRRsR2uFhhWiFLMeVI128GpbMgr7V3F5DkdZo-8V2Tvnq7dY3cQ4aTVb9MpyQJ7Egros24JrmXyisbo6pNz_8yz0fBRzURc-uKkUhAqfWg-jNd72xSlHKt685g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یه هموطن گفتن که این خونه جن داره، اونم خیلی پرقدرت و باشکوه وارد شد،
اما خروج جالبی نداشت:
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72929" target="_blank">📅 10:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72928">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=o5ZLozkszMg4qalNiv6Bo3aiCxyr8My2TpbS8ptMoAnFnCppoJoAnvORxQnXT7xAL34rB8F7h2ALGgfXg6pi8HEuEU6pExfZM1ZJt6-Men6yXAYrT_JstIhxXSEfoqtXXNGuTXXYFXI8buBEKNgWk-Isks4-tTVeeVzZW84jAwAvzyapnpBntrGZmRS2hEaPH6eRM23HQeClhNOSL9N2CJXTGqqSwmW_5fKjtTZ2bVfoMIcoOaBngOeG8Y53WWGRTv5w9aRnlrodLfqpjBi9wDXnv-0PCf-w9OLVJSTCo_Yg740M4a7rFAS_gqX4iBC5Uta2r3BZmSUZZ5qCf3edmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=o5ZLozkszMg4qalNiv6Bo3aiCxyr8My2TpbS8ptMoAnFnCppoJoAnvORxQnXT7xAL34rB8F7h2ALGgfXg6pi8HEuEU6pExfZM1ZJt6-Men6yXAYrT_JstIhxXSEfoqtXXNGuTXXYFXI8buBEKNgWk-Isks4-tTVeeVzZW84jAwAvzyapnpBntrGZmRS2hEaPH6eRM23HQeClhNOSL9N2CJXTGqqSwmW_5fKjtTZ2bVfoMIcoOaBngOeG8Y53WWGRTv5w9aRnlrodLfqpjBi9wDXnv-0PCf-w9OLVJSTCo_Yg740M4a7rFAS_gqX4iBC5Uta2r3BZmSUZZ5qCf3edmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«استیو ویتکاف داره روی توافق با ایران کار می‌کنه و خیلی هم خوب پیش می‌ره.
فکر می‌کنم این توافق واقعاً چیزی نیست که بخوام انجامش بدم، اما ایرانی‌ها حاضرن برای اینکه این وضعیت متوقف بشه،
هر چیزی که ازشون بخوایم پیشنهاد بدن.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72928" target="_blank">📅 10:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72927">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ درباره ایران:
«همون‌طور که قول داده بودم، دارم مطمئن می‌شم که ایران هیچ‌وقت به سلاح هسته‌ای دست پیدا نکنه. خودشون هم اینو می‌دونن.
به‌زودی از اونجا خارج می‌شیم و می‌بینید که قیمت نفت مثل سنگ سقوط می‌کنه و قیمت همه‌چیز هم پایین میاد.
این عملیات بزرگی بود که رئیس‌جمهورهای قبلی باید سال‌ها پیش انجامش می‌دادن. باید انجام می‌شد، ولی هیچ‌کس حاضر نبود زیر بارش بره. ما چاره‌ای نداشتیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72927" target="_blank">📅 10:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72925">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=XI5VvdNPLLJ6eJT_i2a8_rJxabfrc948wuta3H-Tje7u_q2g27k9ipMPwp162OnLyEelbWE9mj15uDWzUSrWud9ssFYhvu8KUhgBZWSqFBt6zBOM8XydMAkmSSlf6y0HEQLTPCrKDmu5hqwa5-pXoVzharyLmqcfhQndjqE9TbDcuzDABknH_7SvzaAI-xxH3dZbha_jqIJ8vmyBL9QJLb8psuv2W13Sm_Qa6qMUfShtrDaocKIzK4_9lr29DgMG5asQ4gh8uPGEk-ZIShUoLxX11BTh-IRp07n_hNoFYBg1MCfip7A4fb0dPR9x2-a6ruZZxygv-jf2lA7fHmgdjLq-P1EiiEzkzJar-JtHOe1CzgJAEYP1KIuYLxLLW984k9qioPRHJoNB62Imlu5_NWKeBvULxkL4tZv9UEJ0PoDo_bqN2V67AufWF2Hf7vl2LMj1MNuckvRxxlX9g6kGy8j21KumZlwna1Zc1y0PWJAbwu-gZDScDG5EsyXzgQQ_A6wFr_6OwLuFAoc2p_bLYVGOHq7RfwCX7gCZqOx-Qz2xYb5EP8DT0j6nVkdgUn_25f47z4mSQQt5GQVQU6D3aNJ92FvXGnLIYKFoa10JPeGQDGfTpghdE9-9A6TSB2Bmqlbp42VlSdj6-f63xHGz6_qkHyuCETlAN0FH642Ggxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=XI5VvdNPLLJ6eJT_i2a8_rJxabfrc948wuta3H-Tje7u_q2g27k9ipMPwp162OnLyEelbWE9mj15uDWzUSrWud9ssFYhvu8KUhgBZWSqFBt6zBOM8XydMAkmSSlf6y0HEQLTPCrKDmu5hqwa5-pXoVzharyLmqcfhQndjqE9TbDcuzDABknH_7SvzaAI-xxH3dZbha_jqIJ8vmyBL9QJLb8psuv2W13Sm_Qa6qMUfShtrDaocKIzK4_9lr29DgMG5asQ4gh8uPGEk-ZIShUoLxX11BTh-IRp07n_hNoFYBg1MCfip7A4fb0dPR9x2-a6ruZZxygv-jf2lA7fHmgdjLq-P1EiiEzkzJar-JtHOe1CzgJAEYP1KIuYLxLLW984k9qioPRHJoNB62Imlu5_NWKeBvULxkL4tZv9UEJ0PoDo_bqN2V67AufWF2Hf7vl2LMj1MNuckvRxxlX9g6kGy8j21KumZlwna1Zc1y0PWJAbwu-gZDScDG5EsyXzgQQ_A6wFr_6OwLuFAoc2p_bLYVGOHq7RfwCX7gCZqOx-Qz2xYb5EP8DT0j6nVkdgUn_25f47z4mSQQt5GQVQU6D3aNJ92FvXGnLIYKFoa10JPeGQDGfTpghdE9-9A6TSB2Bmqlbp42VlSdj6-f63xHGz6_qkHyuCETlAN0FH642Ggxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از مدرسه دخترونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72925" target="_blank">📅 09:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72924">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=GavkoFeeMIljhECQ7pCrrb8i98BW9zfO6TgpdSYvUjS_zAyFKxWrKTijVoxAax4tt1tUtHBPeqLuaEaGkTWtBoJ3o3zTz13SGv5ZUx-V2v2SNV4V5dzgwPPbi_k6n3MC82PMLackojY1OADA3BXOo_tt2zp_wmScXp8oYK519WxsI8KmFbbt1Uk9gzQ6G_U7gw0XHYdDPEcN6zxSc96iQfz8tPk8mijGjPW4YEEOlfxsDqrVxZJqzU1aXC5cU4I_teih_KAT9bBcRMmPQMxRu29tx9Foe2FQW-rMl4_6AhKStIKl682fm3suDlcJv1-j1gXixw1JMpbYM74C0WI5hH-fVYnAgIdUA3O2Qnd-nf6jk0pDJlmFvSWaZLqp563KYfkdRHB2MrEcDMfpM3HxzhabFcoXAwyEs4kM4dXb2GPp3yfuC7szouT5htVF84c-4k_rdckBA5eVA5qhakHZiF8P3ls4wUUQpyGbGA8dng5Y8vNB8AexRG4vmi0PSYEdZuWyU_biKtbE8JJ_nEZR5xZqk7JhDIuBN0ZPsWL-IK31eHrVyA9dEruiwN5R3JGyfxKpB6CTOg_jCJz6XKg8PEh2fJgobZsG11Sdxk0i_btBgvdsO5wlTLHQdyEczhCow2-q-3qc8W0qGvQDx8nYXCZ1IGWSpf2XueWRq8_7R6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=GavkoFeeMIljhECQ7pCrrb8i98BW9zfO6TgpdSYvUjS_zAyFKxWrKTijVoxAax4tt1tUtHBPeqLuaEaGkTWtBoJ3o3zTz13SGv5ZUx-V2v2SNV4V5dzgwPPbi_k6n3MC82PMLackojY1OADA3BXOo_tt2zp_wmScXp8oYK519WxsI8KmFbbt1Uk9gzQ6G_U7gw0XHYdDPEcN6zxSc96iQfz8tPk8mijGjPW4YEEOlfxsDqrVxZJqzU1aXC5cU4I_teih_KAT9bBcRMmPQMxRu29tx9Foe2FQW-rMl4_6AhKStIKl682fm3suDlcJv1-j1gXixw1JMpbYM74C0WI5hH-fVYnAgIdUA3O2Qnd-nf6jk0pDJlmFvSWaZLqp563KYfkdRHB2MrEcDMfpM3HxzhabFcoXAwyEs4kM4dXb2GPp3yfuC7szouT5htVF84c-4k_rdckBA5eVA5qhakHZiF8P3ls4wUUQpyGbGA8dng5Y8vNB8AexRG4vmi0PSYEdZuWyU_biKtbE8JJ_nEZR5xZqk7JhDIuBN0ZPsWL-IK31eHrVyA9dEruiwN5R3JGyfxKpB6CTOg_jCJz6XKg8PEh2fJgobZsG11Sdxk0i_btBgvdsO5wlTLHQdyEczhCow2-q-3qc8W0qGvQDx8nYXCZ1IGWSpf2XueWRq8_7R6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو تهران، عده‌ای ساعت 9 صبح از خونه زدن بیرون، کفن پوشیدن، به سمت قوه‌قضائیه رفتن و به پسر پزشکیان لعنت فرستادن :
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72924" target="_blank">📅 09:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72923">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72923" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72922" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72919">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgSDIjX65DHbi7hSmRS-yttogIqy_BaKeMfmeRQTZ4TOOkBKP_FZ-LnOKe3jccehtwY3EcCd7uz4CmQoSHyMTVidX1sD-LnWOd3eBOnRwCLL3bhcWua4cNQa48HMK82n4G2o-jZAIhnesAO7Fe3dvB2yh2mtPxwJh6hJkaDiwYnGM7vHBBa6UOeDR6_Q_CBxEcO6pwUo-FucARqn1bUrjA-jtJMS0oGBpnJ7CXZykS3ykIRFXwXyNYz1zDRJMIQGETnueeTwbMlexBW-6PucQWi91iuX3_AdnZH_lVL-Mmc59tstGmWa3BTRXuJXN6LK75mNJcRCdwzBa8ZRvF2kpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XC5lNKjwxO16weODJcmAvnempQZWbfUCPj8NnIRkVzw2v5v6DBLYAe3g-aXLHk_EDp8tPmXwP-M0TicbhrfhCggZr95CMNm3TjIs04ww7gyYNWTLCtr7KTD4AnH2s__ItG0GhcQlZwksN19yUekhhssnzQZp2_T3WJu4KB-qUSFm8wSMVTSPev254kjjzLZhhmQKPnt1djjgSBRQF_zOxgWjn1fiY6VkfdTwAoPHTHq4MkczAOCEhRzF-FUasphl30n-RV7SXdy1XWWGhJr9969KyutEGKcDxuQfrOymjVN_mbr6uNgRJG8Nc9v0uTfdMwzqkMR_CvDr0ss0HVzqZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=G_DH5m0IJRFe9f9tpz4EcBmPT3aBEc6KG5o3SezZup3mvOp0Q0tPb9v1KVC7Wm3yeBcUi8dvNRNEty3laLUqQi3m9n_3yilWs3beo3iAE0xRPleOnj6rS09PubFSrBxl3UDPuv-VaRG83hps4deJecwkotNhGpw1dRj6KACyYu_kvrJzPQUMrZkN7u9DbaNWwDZoExMqYothggYOEUHaCfiq4IdX1dbEAgGW_D1SVLKx4ZPIbvzD2SuT96HIG4KpC665ni853sVw_twEOEySF9lUzrAb47Kft5OzAzsD66xrCbXSUD5YB3J-aNeFmRf6j04M1FTRtTQNRagAIM9AFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=G_DH5m0IJRFe9f9tpz4EcBmPT3aBEc6KG5o3SezZup3mvOp0Q0tPb9v1KVC7Wm3yeBcUi8dvNRNEty3laLUqQi3m9n_3yilWs3beo3iAE0xRPleOnj6rS09PubFSrBxl3UDPuv-VaRG83hps4deJecwkotNhGpw1dRj6KACyYu_kvrJzPQUMrZkN7u9DbaNWwDZoExMqYothggYOEUHaCfiq4IdX1dbEAgGW_D1SVLKx4ZPIbvzD2SuT96HIG4KpC665ni853sVw_twEOEySF9lUzrAb47Kft5OzAzsD66xrCbXSUD5YB3J-aNeFmRf6j04M1FTRtTQNRagAIM9AFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۷اکتبر ۲۰۲۶؛ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس رونالد ریگان» (CVN 76) در حال ترک سن‌دیگو:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72919" target="_blank">📅 01:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72918">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=OFKFRJ2t6I7l5JjzHduJlj88ZV6T7GvdA91ead8nQPtgRgWnI7UWctXOtqsNTvFGB5CZgjIspJ-2eDqVMFx3LQi7ktcHrxesZFV8giSPSouZJdumuG64fWRFqp8-2e0rB8xOBAjtPU9u7J0A-Lssm_J50Cc474B70gcYQIcWJ9OZC-BJfcsX2YJZuIQBCBrDjAzRutZg5K0uanNJ0mEBD1tIjP2Pwr1TbXlJk4ouysRJP6LeO-OMKGHQrhodSEoEcje1HfwDhy5n4-0hGcJx50aWJJYCO5hj0wqc49kLDOLF9Ga_HxVNgP9LHAHChwbxiHV_hUOAaWSv-7HdCdH_Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=OFKFRJ2t6I7l5JjzHduJlj88ZV6T7GvdA91ead8nQPtgRgWnI7UWctXOtqsNTvFGB5CZgjIspJ-2eDqVMFx3LQi7ktcHrxesZFV8giSPSouZJdumuG64fWRFqp8-2e0rB8xOBAjtPU9u7J0A-Lssm_J50Cc474B70gcYQIcWJ9OZC-BJfcsX2YJZuIQBCBrDjAzRutZg5K0uanNJ0mEBD1tIjP2Pwr1TbXlJk4ouysRJP6LeO-OMKGHQrhodSEoEcje1HfwDhy5n4-0hGcJx50aWJJYCO5hj0wqc49kLDOLF9Ga_HxVNgP9LHAHChwbxiHV_hUOAaWSv-7HdCdH_Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72918" target="_blank">📅 00:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72917">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svNqV7tNAQMqnW9957-KhP2mJKkV9Z8hJLMZhhPqEw4ThZU200ok9SFT0v3A5-vBdw2SZvsBFB9kob3Sp0KKsomHLoahWyOm-HNsK5lNsl_OHjs7mKHSDU5EhlWVtiSuqhlBBoeb_XBoe9-fZsaWk8LtZOWI28_aoxqSfdbfaxeyr5xKII2LRD4UXDeLStl5oSjPT8QTVTFxusAGUCfXgw_GDJo5juOm11mmrsZHTlDjo5fvvZ1sBlKzowqeo-xavR-FY1aCAt50xuF3Y56MNNjn3LJ9d7aiBhNNS9BISiigpiXx1_4QpmynLDzCvjVxPlyLK2cCOJ89AEDh_uZRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتلانتیک: کاخ سفید از پنتاگون خواسته گزینه‌های حملات جدید آمریکا به ایران رو پیش از انتخابات میان‌دوره‌ای ۳ نوامبر آماده کنه؛ البته هنوز هیچ تصمیم نهایی‌ای گرفته نشده.
به گفته مقام‌های آمریکایی، ترامپ می‌خواد قبل از انتخابات نشون بده که در جنگ پیشرفت حاصل شده و هم‌زمان به کاهش قیمت بنزین کمک کنه.
همچنین گزینه‌های اقدامات نظامی گسترده‌تر برای بعد از انتخابات میان‌دوره‌ای هم در حال بررسیه.
@News_Hut
| The Atlantic</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72917" target="_blank">📅 00:26 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
