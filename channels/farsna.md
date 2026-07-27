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
<img src="https://cdn4.telesco.pe/file/fG3vvJuw8T0fTfzgoZQSwspEbnIiHj6b5SiEaW0aWg04oHDP7d6U2G2L7jAdOlA6vS4QA7a1-vZyMFFrPtFdItfAiyqSl5N7WVLPoZibzYwFJm394cS3r7peijNEgrhumMIzkkCgHwKgn6twj8M2_JdUoriEpI2Hg5WEiuUThUVPAqt2CgzibHpFYMyIHKYRWyNRL3e8PHMT9qf_GstdYDFbQJHdteAIhYVsmC_4mlgTrxcPmBIH053i9w1OkA_KB1GRnlCH_ANgR6Wl1c46eyhEAo9zxmPNha5mg1Mu8B2a4qb3wIG4bQfU_6V8pIUBPMjpfJ03G2pgdjtARIzUrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 18:50:44</div>
<hr>

<div class="tg-post" id="msg-452962">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1zN9-bLoqOnCRT0uzKXlbBsqfNtdPgOeZdWTicNA01sn_n1qiynTht11ze8XuFMFUCHtqyWjzDcUDfyDy9YZjJBvdQB_CR4Zi8Mf3O7NfsCGBZkNo62JCZ3DTOkg5tpPv0MqPPOCljB4hEqGMBBenG_z1c9nVMYr6FYFw4bddRDRbyvq4neFVeHUfpHdAbO2yYiYEe2OAjVjdXzIpDFO8bkorS7t7WRtABYhKxxk-vj-oQf0ssCCWnZtSAPPUyrIzUbl8nKqrS8QZT4GBfOIKv5Wbo28mJCeTpZultqqP1PRybMUy09ot_O7MJbRcrsoTdUMFC0eqcFSUWdJGN3cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnQ7tG7a6ATeU10woOy6hXC__kNtS8CZ_gpFZDasD0aAd47L4PlA9xjXLerSBx0xRTfr3nYfqOvLB1ZDUr93UpUpL9ISIeHRc2BSXiZ9t97LbXtuhAgqPFLezWfXaA_LU84WIyXHVRjVk1V5z8PY5DGao4wP-pR0zt9CiM90taUfRL3nSvXItRPGiyvsjiBabcK3s3I322U-_tUruRbaNrjjfX29vmfsBjZo8xI7jwV7Gpam1501w4_79x6KNmCfyH55Hh5WgvGRElUH5fRUIJd9gzkjjQ8Ob2_Qgbq79Jny06z1K7_-86HT1DGZIFmTTQz46J_c6g6n6Ih1lLZ98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FLZa3KYHEsWOG_c9REi1ENLUFqnSPFNSM-PKugvgarTRCNTtTNa1bgmlvFWgRHh-VFtYRiwM2nZ_rEReUpvzjOVuu5L5faljIj9USql6pk0083o5LE390gqdIKYVYptpVnASryX94HQ-BEUcXiS3gf5VDQgiWmtN_YeEzVFyIDf6wgfooZCbTkttem65Ftqj06_TvQe46FJVgG7dvwLERYYjQtjZWzjJoD9di00UJ4B3A3kfY9F7MLw2n2Wkfw7qvCBLkjne5OpCZYMKUiROGYJYonooSjDCqRCxQ_9AIbuAteIqYXnxYo3Wyf4ucfi4VZtNEGqO1e44QYgzcKI5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sb1kECSac7C-Gpmn14HDV9PoZAUpSjVYKWfkVZ6vngFBFtUoC5D01Ghgc9wAQHIplifLMuPF-k4C6uuTPPNl3T3vNBNlky_tah-U_5h3AMK1TEcIWuCZYYDzxoKw2iHxwcGSyUO1UrkycYrJyEHqvwRQekwfln44X9m1ukFXRUWK3FgBa-xkIlzBr4Jk7Taf-f6l89bGKed2Jhlp5MGrJs03JYZoZmsAi6D94lRSg2ci9Cc9LTG22tESOdfm1WFsOV8qad9MTYCK4JjH5lPkY-JxS6oUL-RrEIf-K5BPuSNhgBCVun_OPNX9iibtbbfuEhVxbRpOpLz4-PK2zj-ADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sol2IJliYXa18aNHvY4k_yVhG22J019X5PQ_JLV0a8cuG4wfwZEqMajnfZXDL5EriYW7TX9x6o8rUL6H63vJ_hPxxYRZnV1rqxmRF8L8XMTSAWtP_OP8WbBBAo__U9tveKrN7zT0fZW9o5Kt8s21fWBtTYXMvR_Cz7Qreltsd1kC7vJ0mbEP4Rv8hkXATY3gFZ3lrh6yH6f7-LlkrSD93LoSE7HCF8UWem_lJNVV8zrw_WWf5xr49QNoBPu0bycu02QAjSTrhYfesa4qaP8HOTrFzNxL7vqu4XbqOhsGSfbN_1NdWEHyepGvOA2tpejLN3W5W_wxeNJZpky_CnLN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJVDWtCYnpgzZJp95XSxqjErhLbAko6vrZPPIRsQNKysElnjUzGf9yL8DCfDymndSQ3iNC3cA0Pe4NtHrIpPF97hOiwXzf0GnYrW94R1wt8HNLfMwQqyk0EE7e3v1QhmS_UIh0PLqo804zttt4dMlfeCkcnSz6YTI5qHkLKdKuYPw3vBL9_Btc4dlUJf6JGTzSnxhbyzTEGwVZ3XODebm2i95t_aLBt-V6OBD_y3x8wyzdr_uVimtDc1otLmZvgKntLEO1-TJrDLsdTN4fSPYQn5lod6_dk-tTzeZpMgbPOFQBGZmoWFaa4CmwC3KwN4I8RvC0FVpMck6dPJpJCX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuASs-fG022iGenW5uwwoR3Is4RcylKqie0935foHfovGRfDEi_xyBD9j-WbOvGw5lXO8a1DvaJFRQ2va6CM0rE1FJgY_MxQVv0g2xmS72nzQRWVWisiewuKJ3_j8wSyWWU2uDudNlvD3IQKc8JDBc3VXxWLXxFR7UATu0DXOH-FMpVgvsuauzyWg0PsrQg9_yV9tYro8WR6OM5ZVl-94qgSLuOKVOffr9wcA6NN-cO0MO3ep5TBKkR9Myc4mkKc2PylsqoWWN8EbETiKnT_TqZt5lYAIRjYLKjWkd0WbhfT6gNL_ZLVUv-ibyzmmEILEC-hxTDYieO08DJglBqOqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم‌های سرخ «انتقام امام شهید» در دست زائران خسروی
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/farsna/452962" target="_blank">📅 18:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452961">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d49d1698.mp4?token=IH_StLqlZOU1QYcOMuqaLVoiJJNfubhJCiw21RClxIcUUQolGPFdAEOBMqBEjNhEkXjmS11NDEY2oSbGyTx1Tdj1QFa1UjqElV5NiV1KUMAc7Wz0z95moE5-bUL98tuYMeOz9AzleyrArriFYQh28qVRi906jMqsehJPNZmnh3YV7VwM1GsjhxxeA4d-FzdjtJmFuwZwg5pWsvwVN4kAMDcdHoYu44zh_Rh-TxgcopM5h3BSBX8MnrqU7K0grwA2ZZ6b3g8xQvJx0yutTbgXeWDYK-Fi4jXfKt2eJZjdDgFvgMCCSouUCrWFvvtP_HBwWFK3lNa45yPYJ1-1wY4_1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d49d1698.mp4?token=IH_StLqlZOU1QYcOMuqaLVoiJJNfubhJCiw21RClxIcUUQolGPFdAEOBMqBEjNhEkXjmS11NDEY2oSbGyTx1Tdj1QFa1UjqElV5NiV1KUMAc7Wz0z95moE5-bUL98tuYMeOz9AzleyrArriFYQh28qVRi906jMqsehJPNZmnh3YV7VwM1GsjhxxeA4d-FzdjtJmFuwZwg5pWsvwVN4kAMDcdHoYu44zh_Rh-TxgcopM5h3BSBX8MnrqU7K0grwA2ZZ6b3g8xQvJx0yutTbgXeWDYK-Fi4jXfKt2eJZjdDgFvgMCCSouUCrWFvvtP_HBwWFK3lNa45yPYJ1-1wY4_1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین دیدار مردمی آقای شهید ایران...
@Farsna</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/farsna/452961" target="_blank">📅 18:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452960">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbqxsoAoTXiKX5fqZvaQsgLC1QRw3wpMukOcYKgPnV8lRV3ZRP7G0IUFgSVaNDFTTq36o4Th1oqN9nIpNeDQLF3aw-64iCs_KFLp3MlLgmDGB4UbHOUNpQOSlT5SctX4DaRJIMbtQA4X1uDqUcThp3uSPaLEGYNTJK1d7s__fSUr7XczwiVLotCjDnITnfIGKD_zJisRDYR0E4jVR5BobRyEO3RPMae1M1GV8fWXc1ddbsCVMD1HVtItIvQwMznBfOC8nM4h1jWoU1NXsfZ1kTwKSS2vF-rkSPSr2y07Nid-sp0qoaK0lGnX-Cze0wXZIbmRB4cH-cbhBXU2tWeRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار نفتکش‌های عربستانی از دست یمن
🔹
داده‌های ماهواره‌ای کپلر نشان می‌دهد که نفتکش‌های حامل نفت عربستان برای فرار از حملات یمنی‌ها کانال سوئز را به جای باب‌المندب برای خروج از دریای سرخ انتخاب می‌کنند.
🔹
بیش از یک هفته است که محاصرهٔ بنادر عربستان از سوی نیروهای مسلح یمن بر اساس راهبرد «محاصره در برابر محاصره» شروع شده است و دیروز تنها ۱۴ کشتی  حامل کالا از این آبراه عبور کرده که کمترین آمار یک سال اخیر است.
🔹
ابرنفتکش «المپیک لاک» با مالکیت یونانی که بخشی از ظرفیت خود را با نفت عربستان پر کرده از سوئز عبور کرده و حالا با تغییر مقصد خود از اروپا به مقصدی ناشناس در آسیا می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/452960" target="_blank">📅 18:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c9b9bf4b.mp4?token=Xoip262y3akS2PGBeBjDszGsHELeZ807ez2TDhx8nk87lgreN0nMEokiVhILnA-SqjtTjjTnLKH4D4vcr90DjkNhvelRoOBgg0aEktdFLhdCPZo7xG3FJzV7BBk-0wMkyGTaTuSo1LuEvuuHSMsp1TPMU3udgX-O7EIxNBbRwWCwdo9eeFuIMK3ZddtgTCh_ZfiBntMTWYfp0-hnfaNtcx31V9BZPMciHv-BvNR-gytbWLQ_igpvwS_4lx30QFn7b4WQpUY5AK6befE0MgDAzFwEJzbqlxfMfUL2BjYNvGzBTnMTDSSnAuycIk-AHxfx0vWOWirftmBx091JCWDyaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c9b9bf4b.mp4?token=Xoip262y3akS2PGBeBjDszGsHELeZ807ez2TDhx8nk87lgreN0nMEokiVhILnA-SqjtTjjTnLKH4D4vcr90DjkNhvelRoOBgg0aEktdFLhdCPZo7xG3FJzV7BBk-0wMkyGTaTuSo1LuEvuuHSMsp1TPMU3udgX-O7EIxNBbRwWCwdo9eeFuIMK3ZddtgTCh_ZfiBntMTWYfp0-hnfaNtcx31V9BZPMciHv-BvNR-gytbWLQ_igpvwS_4lx30QFn7b4WQpUY5AK6befE0MgDAzFwEJzbqlxfMfUL2BjYNvGzBTnMTDSSnAuycIk-AHxfx0vWOWirftmBx091JCWDyaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور زائران اربعین از مرز تمرچین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farsna/452959" target="_blank">📅 18:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452958">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌
پاسخ شستا به گزارش زیان ۳.۸ همتی این شرکت
🔹
شرکت سرمایه‌گذاری تأمین اجتماعی در پاسخ به گزارش منتشرشده در فارس دربارۀ زیان ۳.۸ همتی این شرکت اعلام کرد: قضاوت براساس صورت‌های مالی میان‌دوره‌ای، تصویر دقیقی از عملکرد شرکت‌های سرمایه‌گذاری ارائه نمی‌دهد.
🔹
بخش عمدۀ سود شستا پس از برگزاری مجامع شرکت‌های زیرمجموعه و شناسایی سود تقسیمی، در صورت‌های مالی سالانه ثبت می‌شود و به‌همین‌دلیل، گزارش‌های میان‌دوره‌ای معیار مناسبی برای ارزیابی سودآوری نهایی نیست.
🔹
براساس برآوردها، مجموع درآمد شرکت‌های گروه شستا در سال ۱۴۰۴ به ۵۷۲ همت و سود عملیاتی آن‌ها به ۱۰۹ همت خواهد رسید که نسبت به سال گذشته افزایش قابل‌توجهی دارد. این ارقام پس از برگزاری مجمع سالانه شستا نهایی خواهد شد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/452958" target="_blank">📅 18:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452957">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpvsBvtRFpeU3v-IbFhTujNXfAmy1A_zLkUM3OD7chC7Uzt3r-cIFKGyC-nTqTXhLlljLEbEXqqBVgdeJdFr_YZuhk1Vr_rFjp856mMdmyo4awRy3B8_6zaFPjt5zkFoGRaDjt4TJaxXSgTT14_-v66CA3hR_99dAIskGlJiqI0tWB15yElkyqGVSOoJGenMre9q4x2MWRRBsWeZDGA18AyDoy9xrcHXQuIth8urcAxLoktN7R_Bq_L-vsAykzGdxxeVoBshDX-ge7PFQWaBJubjEP6Q0WacZlSyyxWZDQ9ZxbNSxCvhBCwJzsNrgO7uw1wViUzFbqzHkWgn5ytNRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلزی که در داغ‌ترین شرایط هم دوام می‌آورد
🔹
اینترستینگ‌انجینیرینگ: محققان چین اکنون آلیاژی توسعه داده‌اند که در شرایط دمایی بسیار بالا، خواص مکانیکی خود را حفظ می‌کند و در برابر تغییر شکل و تخریب مقاوم است.
🔹
به گفتهٔ پژوهشگران، این ویژگی می‌تواند عمر قطعاتی را که در محیط‌های فوق‌داغ کار می‌کنند، افزایش دهد و نیاز به تعویض مکرر آن‌ها را کاهش دهد.
🔹
چنین موادی برای ساخت موتورهای هواپیما، سامانه‌های پیشران فراصوت، توربین‌های صنعتی و راکتورهای هسته‌ای اهمیت زیادی دارند؛ زیرا قطعات این تجهیزات به‌طور مداوم در معرض دماهای بسیار بالا قرار می‌گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/452957" target="_blank">📅 18:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452956">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8DVBkasYcWA4ZoDCLdgaPgnpqPVUcbC-2rkBF-djwvgD27JYvgDjlC1JJ6Pnxw9HAixXYTS_unn2UfPUpL6W0AMjr7fyn3ZTFMycgbKoELVdprnCV7NK7vdUFSKAw7Z_B5nKVdQNxNgOZGDcNEp71-rFlnuskpA76qy8KjCSatTLKt_NMf9nr_NObDAwALKVWnbj0vJdrG5yhLB5Ye2XvrjYoX60BzKcj73pQoO3zQJI7ArFyG_ZqrfMXi_d-lXEPVejXQkjDr-EyCu_kbC9KFS2GK-fIo_nwEicKnwEqacudKKQ9gpjHryOHSJ3RlGJhb8UAVTF2wBQLagsqE0EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعات محرمانهٔ مشتریان بانک بزرگ هند لو رفت
🔹
رویترز: یک پژوهشگر امنیت سایبری خبر داد فایل‌هایی حاوی اطلاعات مشتریان و اسناد داخلی بانک بارودا در یکی از انجمن‌های دارک‌وب برای فروش عرضه شده است. این فایل‌ها شامل اطلاعات هویتی، جزئیات حساب‌های بانکی و برخی اسناد داخلی بود.
🔹
این بانک همچنین تأکید کرد اقدامات لازم برای محافظت از داده‌های مشتریان و بررسی ابعاد حادثه در حال انجام است و در صورت نیاز، اطلاع‌رسانی‌های بعدی انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/452956" target="_blank">📅 17:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452955">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afad1b6c3.mp4?token=hwcFW7sycq-JfKvIgqSjx86ObNtKFP3PcX6MmXH5d_fRdomirACigenxQOymktLUfzaMP1xyOL8jl3pOqTN5ytknYrFIWVzd1ce2ZtUKlrla4nOU05R_2uq7bUoAk2F3rTaUGggdliUgqVF90min3rRBUs_m9WU5-CKbprz7njXFdg93dAydiiuzjZ-SNWrLnpdD2x4aYvUgObD6fWqF_NUTJ8YMNcZoRvRET5lFAtGMMyEu180oje7J4LNyZtGFY2Tx583cKI_b4UoMTmdKHaMUMFiNvg_SeLVTRz_DjTJpMoJk_3Je98XNZ3PPp5FAsljFghT_tnWH79FwMHxihg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afad1b6c3.mp4?token=hwcFW7sycq-JfKvIgqSjx86ObNtKFP3PcX6MmXH5d_fRdomirACigenxQOymktLUfzaMP1xyOL8jl3pOqTN5ytknYrFIWVzd1ce2ZtUKlrla4nOU05R_2uq7bUoAk2F3rTaUGggdliUgqVF90min3rRBUs_m9WU5-CKbprz7njXFdg93dAydiiuzjZ-SNWrLnpdD2x4aYvUgObD6fWqF_NUTJ8YMNcZoRvRET5lFAtGMMyEu180oje7J4LNyZtGFY2Tx583cKI_b4UoMTmdKHaMUMFiNvg_SeLVTRz_DjTJpMoJk_3Je98XNZ3PPp5FAsljFghT_tnWH79FwMHxihg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک پهپاد ناشناس در استان بابل عراق سقوط کرد
🔸
منابع عربی می‌گویند احتمالا این پهپاد لوکاس آمریکایی است.
@Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/452955" target="_blank">📅 17:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452954">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add39ded09.mp4?token=T3QzzyjEHu3V1YS9D8kkzHJVRTBLQckFcghQ1TuwDRXh3uwlm-0fAd4D7j7BLFaLFZ-ktMEIrmjDZOWHLUISFvxg_mRzOiim7VN0ABt-QpsZpND64x9s0I1SuFKAEjQEaB349loBzhip1w8TapUa52Q-950FAZEeQV3QZQKl7yS9sDZzHEX1txFd40kNDWCULcngbZXza4UEe5_LKTRSmRUoO0zKVWn3q5mqedBKNR6mWiNOWLw5copGxUJQa7_0ohTf7ZdeZYdYkPF6AL7ERCvFKmf-GZb7lmxbVATKAweFgIq3HOJyowWCOrOnrML-7svz7d1GMP_F4x8QraR6Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add39ded09.mp4?token=T3QzzyjEHu3V1YS9D8kkzHJVRTBLQckFcghQ1TuwDRXh3uwlm-0fAd4D7j7BLFaLFZ-ktMEIrmjDZOWHLUISFvxg_mRzOiim7VN0ABt-QpsZpND64x9s0I1SuFKAEjQEaB349loBzhip1w8TapUa52Q-950FAZEeQV3QZQKl7yS9sDZzHEX1txFd40kNDWCULcngbZXza4UEe5_LKTRSmRUoO0zKVWn3q5mqedBKNR6mWiNOWLw5copGxUJQa7_0ohTf7ZdeZYdYkPF6AL7ERCvFKmf-GZb7lmxbVATKAweFgIq3HOJyowWCOrOnrML-7svz7d1GMP_F4x8QraR6Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنجره ای به مراسم یادبود رهبر شهید انقلاب ویژهٔ اهالی رسانه
@Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/452954" target="_blank">📅 17:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452953">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwRytSQdBM4mzg-fP2RcgxYDLrjl8bDe6qSdYO-dnDfEvvYTflSozHaHMBfADPewqGuBiFkbg5Zs4rP0W5u7c1qcvQp60AHkVfSIwJNuTF-OjjCArPhsm1ZC7WMgDvL41e79pRXAJBwpmTCpqiHqGYnk34ddeny59ZDXE8AXXEc1yfWzZVdA23sOrSRiHMZeFLjxE-cXunzCcv5RYeEKXKU6OLIDhBoDnBLIIYzw7BtnE1IzaOhhK_HnS0mSSt0xCqr3S2ve8oX9DBN6p7h8hbgCH71ShSjhnNpEvilqM8BUO7cfrpU9gpoirjAzhtuqclKWYqJAoRjZmtVUMNPIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان استقلال آبی‌پوش می‌ماند
🔹
وجود اخبار ضدونقیض پیرامون آینده کاپیتان استقلال، ادامه همکاری روزبه چشمی با آبی‌ها تقریباً به مراحل نهایی رسیده و اگر اتفاق خاصی رخ ندهد، تمدید قرارداد این بازیکن به‌زودی اعلام خواهد شد.
🔸
روزبه چشمی که قرار است برای یازدهمین فصل پیراهن استقلال را به تن کند، در مذاکرات اخیر با استقلال بر سر مبلغ قرارداد اختلافاتی داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/452953" target="_blank">📅 17:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452952">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61854b39d.mp4?token=KWCfj7QxFEtED7K1rUQUt-wmRzzegrVzi7wJLWj_rdICba2cDxW5TYQasxgUqPsBEZ0IAWzmjZjBeFKW43CGAE-vZgvgUv1niWB4400lZz1HeyhBE5d6gHdaybXsFDBnilEvreiI18Piz_VwjLVMCFYM_WpeX6vYi5-B6vDZlSgoWtdrKlxpK8CupVtpSFN59PKsEyZp_3vC35Evtv8td_r8GBKKVNtFugYbBiVH8NFtbngbPn5l5-MaEsM-UHynQSzhLKqZSTaoSmu2CHoQa1ZGbfdW3-NXD0zOsp8g8eCWC_fEZOa5y7MnuHhzLmg-tAt5xCrSD5QvUN5ju0Z1dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61854b39d.mp4?token=KWCfj7QxFEtED7K1rUQUt-wmRzzegrVzi7wJLWj_rdICba2cDxW5TYQasxgUqPsBEZ0IAWzmjZjBeFKW43CGAE-vZgvgUv1niWB4400lZz1HeyhBE5d6gHdaybXsFDBnilEvreiI18Piz_VwjLVMCFYM_WpeX6vYi5-B6vDZlSgoWtdrKlxpK8CupVtpSFN59PKsEyZp_3vC35Evtv8td_r8GBKKVNtFugYbBiVH8NFtbngbPn5l5-MaEsM-UHynQSzhLKqZSTaoSmu2CHoQa1ZGbfdW3-NXD0zOsp8g8eCWC_fEZOa5y7MnuHhzLmg-tAt5xCrSD5QvUN5ju0Z1dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثبت‌نام گذرنامۀ زیارتی در میدان آزادی آغاز شد
🔹
رئیس پلیس گذرنامه و مهاجرت فراجا از راه‌اندازی بخش ثبت‌نام گذرنامه زیارتی در رویداد «محرم‌شهر» میدان آزادی تهران برای نخستین‌بار خبر داد.
🔹
سردار امید نودهی گفت متقاضیان می‌توانند هر روز از ساعت ۱۹ تا ۲۳ با مراجعه به بخش صدور گذرنامه زیارتی اربعین در محرم‌شهر میدان آزادی، برای ثبت‌نام و دریافت گذرنامه زیارتی اقدام کنند.
@Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/452952" target="_blank">📅 17:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452951">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKY8Be0s0yd1Pku1bNaBHYDZKn7FugXDDOVwDbZUpekOo3in4HNcilMo0YoLi6Uluz_bRh1Ti5TtCZLGkaRrSQyExxBOzRKhbpYocBlqKy3JmT87tHB53DVwFL7lxaSk3mfKts-Wl2_nEA0rvRftkTIIJUtXSapzQWnazDJjYWog28V6IsxfoPt21eAGGY497xskKdIvmdo5-pJI7ukrj_hQRbBVfbwQ9kLrpq3E-yy8Fz0g0Zju2hFjEbkEySzwGEW0fSuubNWLNl_95BWngIu0kdHkDm4HoV9JxNedz6yipEyAqpxOUJ46x1772RI3Tz6SzEXfqRZtWMo6V4Ph2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی: از ماه پیش ترمز تورم را کشیدیم
🔹
در تیرماه نرخ تورم ماهانۀ ما نسبت به ماه قبل تقریبا نصف شد. این نشان می‌دهد روندی که برخی فکر می‌کردند در آن تورم بی‌محابا افزایش خواهد یافت کنترل شده. در ماه‌های آینده نیز کنترل بیشتری روی تورم خواهیم داشت.
@Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/452951" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452950">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfuS016Sp99lGvv_BHcQrpjp8lS5fivtm_JUycIqfr2U2928CZrVAH8vsftrdGRM-adLOhChMgb-AplJsZiC7KKnL2tFeNSdWpN8UmcBkBeywzxxu9xcb2orTueothYEwNw6i_Vaco4jZcf4AfqAm4Glg7VSg6HHcEbQNz9nJkoq_4THldT6KuCukTD8ZPAzeyYIs6LC69C2D0K120w3F77AGYmEM-lWc0ONRfOHbQoxnFhxN2xUVT30FPGGJyThM7et2zgWtx0bSvO-OpRwdQqqRCqRmBJl2a94uP87qmmq1dBH4GuwTP1vTHdJ4tSnetjH35rw8A6h75qa8PkJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگهٔ هرمز قیمت پروازهای آسیا-اروپا را ۳ برابر کرد
🔹
درپی تشدید تنش‌های منطقه‌ای غرب آسیا و محدودیت در استفاده از برخی مسیرها و کریدورهای هوایی، بیش‌از ۴۳ هزار پرواز لغو شده و دست‌کم ۷.۵ میلیون مسافر تحت تأثیر این وضعیت قرار گرفته‌اند.
🔹
آماری که نشان می‌دهد اختلال در مسیرهای هوایی چگونه می‌تواند در مدت کوتاهی بخش بزرگی از شبکهٔ حمل‌ونقل هوایی جهان را با مشکل مواجه کند.
🔹
گفتنی است براساس داده‌های سایت‌های بلیت فروشی قیمت برخی پروازها در مسیر آسیا-اروپا، ۳ برابر افزایش قیمت داشته است.
🔹
منشأ اصلی بحران فعلی صنعت هوانوردی، بسته شدن تنگهٔ هرمز و اختلال در صادرات سوخت جت از خلیج‌فارس است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/452950" target="_blank">📅 17:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452949">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8815d452b.mp4?token=XdnIOZGuQwkzSPitIJbMqF3m1Zu6CjFd96UF4Csm-YfZvBeqZ9IG9X3BZh_D2aoIzjfx0RiiK2UeryPQcPqycbF5K44RaAizJAUack1pyjdKrgLkFfVQymmifp4nTDbip6pffWmx4Is199m8HzOIqcsA_BUfteTnQtEYiwoK-ibKTtP0hveeh6TWd9kQa12nbRjtUZ5cEGI30dKWeQqk7MGk5CWjmO2iYJHiwFUEMWjgk_77E5jO16nvAqqHTnytp_MfIOzoyZA79Evwy5kOqMK4v9-4LvCOoXo4EORdN5syhFs0drmBRASy_Dz0NmU5LKZc5N5fwNEp3K5jfjihxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8815d452b.mp4?token=XdnIOZGuQwkzSPitIJbMqF3m1Zu6CjFd96UF4Csm-YfZvBeqZ9IG9X3BZh_D2aoIzjfx0RiiK2UeryPQcPqycbF5K44RaAizJAUack1pyjdKrgLkFfVQymmifp4nTDbip6pffWmx4Is199m8HzOIqcsA_BUfteTnQtEYiwoK-ibKTtP0hveeh6TWd9kQa12nbRjtUZ5cEGI30dKWeQqk7MGk5CWjmO2iYJHiwFUEMWjgk_77E5jO16nvAqqHTnytp_MfIOzoyZA79Evwy5kOqMK4v9-4LvCOoXo4EORdN5syhFs0drmBRASy_Dz0NmU5LKZc5N5fwNEp3K5jfjihxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی، معاون وزیر خارجه: در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.   @Farsna - Link</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/452949" target="_blank">📅 17:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e7fa07d21.mp4?token=PWDlj12k4fhoMgVCQxPFDIRRpYhVzDJ0n6zy8nh72KG-B-7-Sv7MYwAraAmL7HZlVvmwUDSHdXohfyq4pzx6CVx05rfU8P_SUXYKuBjIJMruJGgLqdY3_E-MfyU0NBPCgCrX0frjIw7k3ocUwZSNUyg8zFqQ4zYAag5fHVavB2zaaPSr6UJvJncUGhmjz0sZvbil37873AF6JNGGiF6MMWQ4hQoiDerkhcEcakLNsrA836Stan0WlGWnyuY4GYSwUpIPJLg-cPj6gZbrCyBMflbMiDkg1d5OrOW1yTIoY1H0oDOxtfSoufArK_uuun7DjfOVzrdw8M9V2GN3ac0fH5P4q6sKewTgiHyfDvudmBhkgC407FgZDhtFgHxqWtkRTdUfT4S7boLfd4nFG8-VREmynB7rtG0yhfgd8-sN6nk5lrJALX1mNTMLLOHVjENa6NWtHrDJtxj9f5F2Dxk5b2dAdWXOjpm-O9kDNGg_M1wc5dZKS94QGLaLKBvdTkPcchL4hAiHovaDY6RthjzhGiL6T--XyOcROYDjRx2DepM6cCvosHUUtLYkeiERvJn1sSfPvpLjEX0QhapNUU3yD--BWQXCFd27xnW1NECBpveZAMYL263vRVX08m7u27wS3WU3negYHb1KpoUVojauidvMYTRst1qKycda74cvM1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e7fa07d21.mp4?token=PWDlj12k4fhoMgVCQxPFDIRRpYhVzDJ0n6zy8nh72KG-B-7-Sv7MYwAraAmL7HZlVvmwUDSHdXohfyq4pzx6CVx05rfU8P_SUXYKuBjIJMruJGgLqdY3_E-MfyU0NBPCgCrX0frjIw7k3ocUwZSNUyg8zFqQ4zYAag5fHVavB2zaaPSr6UJvJncUGhmjz0sZvbil37873AF6JNGGiF6MMWQ4hQoiDerkhcEcakLNsrA836Stan0WlGWnyuY4GYSwUpIPJLg-cPj6gZbrCyBMflbMiDkg1d5OrOW1yTIoY1H0oDOxtfSoufArK_uuun7DjfOVzrdw8M9V2GN3ac0fH5P4q6sKewTgiHyfDvudmBhkgC407FgZDhtFgHxqWtkRTdUfT4S7boLfd4nFG8-VREmynB7rtG0yhfgd8-sN6nk5lrJALX1mNTMLLOHVjENa6NWtHrDJtxj9f5F2Dxk5b2dAdWXOjpm-O9kDNGg_M1wc5dZKS94QGLaLKBvdTkPcchL4hAiHovaDY6RthjzhGiL6T--XyOcROYDjRx2DepM6cCvosHUUtLYkeiERvJn1sSfPvpLjEX0QhapNUU3yD--BWQXCFd27xnW1NECBpveZAMYL263vRVX08m7u27wS3WU3negYHb1KpoUVojauidvMYTRst1qKycda74cvM1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شگفتی فرانسوی‌ها از رگ غیرت ایرانی‌ها
روایت جذاب مهرداد میناوند، خداد عزیزی و سایر فوتبالیست‌ها از تقابل با ضدانقلاب و آمریکایی‌ها
@Fars_plus</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/452948" target="_blank">📅 17:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452947">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هلاکت ۴ تروریست در نوار مرزی بانه
🔹
سخنگوی فراجا: درپی اقدام یکی از عناصر اصلی گروهک تروریستی پژاک برای ورود به کشور، یک خودروی سمند تیم تروریستی توسط مأموران شناسایی شد که درپی درگیری مسلحانه ۴ عضو این گروهک به هلاکت رسیدند.
🔹
در بازرسی از خودرو و محل درگیری، مقادیر قابل توجهی سلاح و مهمات اعم از  چندین قبضه کلت کمری،  خشاب، تیر جنگی و  نارنجک دستی کشف شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/452947" target="_blank">📅 17:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452946">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9152360a3a.mp4?token=K-7-_ZTpv83WfvRd6CQ9YH0yae7s6g5U_RC5_LHJXKv3naDa7zcuCA4ReQpTGOGdN44TBywV9wuJoje0ivfh8jXmdIKCHW3JDsHJqltG6Ep3mEE7H7Va6yWKvgUgqn2Yyg2SniCVIqLS3FigyG10o8Yi_amBWlreke50tyBmTrSYp2uvTPD1_jNAaPffY8ZWq8j_z3i9_gy1r7iMhN144runzUpWStD8gMFGxDhZPDlxFF0beHJyrmLWY2DT2jDMQFbFtLwVt6I9vQICyDU76ip48gxziAZkkR15-nkClcfc2M7Bkr5hzHzcc6tuvmEAQweFstiqps46VzA51ulp6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9152360a3a.mp4?token=K-7-_ZTpv83WfvRd6CQ9YH0yae7s6g5U_RC5_LHJXKv3naDa7zcuCA4ReQpTGOGdN44TBywV9wuJoje0ivfh8jXmdIKCHW3JDsHJqltG6Ep3mEE7H7Va6yWKvgUgqn2Yyg2SniCVIqLS3FigyG10o8Yi_amBWlreke50tyBmTrSYp2uvTPD1_jNAaPffY8ZWq8j_z3i9_gy1r7iMhN144runzUpWStD8gMFGxDhZPDlxFF0beHJyrmLWY2DT2jDMQFbFtLwVt6I9vQICyDU76ip48gxziAZkkR15-nkClcfc2M7Bkr5hzHzcc6tuvmEAQweFstiqps46VzA51ulp6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی، معاون وزیر خارجه: در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/452946" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452945">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac119cfee.mp4?token=dc-1o2D-rn2jBmz5u96owGrHZJJ6P1ZeawCCYQh6gScCij5vN6dQ3lRdXn7Ca5hgZunHK-L7a7oKDbc799soa3HtvTHnh7L-EoAhxAB5ZmO-KBprp54-IMUSJbyrfXtu-wEDP770LHrn8EQyobMLrSXlUXt5eFN9ity3Zuc95UpMRHIbeozxpXizY9YKjHJzp9I_cXnogWeoWpx_XmmzEXWdo-t5g00qo7ff-AnqF-0cRgjZa9Z43dvDoj1O5Ta4PuAX1SfHbtBG_pmp-ThOOi-8atlJm5Lz_Ip9gyH7L6i3mQ-ZUwhsvUH7IsszGPeWUEPIOwnHOhqLPGJdKTKyzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac119cfee.mp4?token=dc-1o2D-rn2jBmz5u96owGrHZJJ6P1ZeawCCYQh6gScCij5vN6dQ3lRdXn7Ca5hgZunHK-L7a7oKDbc799soa3HtvTHnh7L-EoAhxAB5ZmO-KBprp54-IMUSJbyrfXtu-wEDP770LHrn8EQyobMLrSXlUXt5eFN9ity3Zuc95UpMRHIbeozxpXizY9YKjHJzp9I_cXnogWeoWpx_XmmzEXWdo-t5g00qo7ff-AnqF-0cRgjZa9Z43dvDoj1O5Ta4PuAX1SfHbtBG_pmp-ThOOi-8atlJm5Lz_Ip9gyH7L6i3mQ-ZUwhsvUH7IsszGPeWUEPIOwnHOhqLPGJdKTKyzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت المیادین از جهنم آمریکایی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/452945" target="_blank">📅 16:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452944">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1554001316.mp4?token=qQySlnB1FxufMGy6WDYBftqgzj9ehDsUvgbJDXQRYgVfrUdEkGq4DW9fC9Kgrrnd2P3XWRSOcx4GKPt7w1sMEY06zq2GNxVv483ptEt-vzyVC_C3cS3gieUui2Rmq9X1dIHxlg7iti3mPsMi5yObodx2mnso_jnLO2epO6hrANu_rKiMFVC4C5kbIJLQ8HIFl7IcCvTdKvhkSqcWbUscNXj1WuGh27TWVOCLFBn7q2mPGPC_ci6es97XdR9rNWt8yFsruT5bDSFhaikVQ2NIsGN2y4I5-r8VeqD0S6fOKCRReEM2fwLToG0sdI7cag5qNO4stk4iNJain7c9_PYBiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1554001316.mp4?token=qQySlnB1FxufMGy6WDYBftqgzj9ehDsUvgbJDXQRYgVfrUdEkGq4DW9fC9Kgrrnd2P3XWRSOcx4GKPt7w1sMEY06zq2GNxVv483ptEt-vzyVC_C3cS3gieUui2Rmq9X1dIHxlg7iti3mPsMi5yObodx2mnso_jnLO2epO6hrANu_rKiMFVC4C5kbIJLQ8HIFl7IcCvTdKvhkSqcWbUscNXj1WuGh27TWVOCLFBn7q2mPGPC_ci6es97XdR9rNWt8yFsruT5bDSFhaikVQ2NIsGN2y4I5-r8VeqD0S6fOKCRReEM2fwLToG0sdI7cag5qNO4stk4iNJain7c9_PYBiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت‌های دردناک حامد عسگری در حاشیۀ محرم شهر دربارۀ مادر یکی از شهدای مدرسۀ میناب که هر روز ماکارونی درست می‌کند تا شاید فرزندش بازگردد.
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/452944" target="_blank">📅 16:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452940">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v09O4J4nVcWJNPbylrAxppTsgaw-T0qrXnXbUR2rKinQUXE3b4auf5XysQauFlSsN1243OxWRS1yoRDtPDE7VyVPP3PJ3F_kbkavsZU50iDhiRbUQxXdJhfX6wTeqQEbEhXRnb_Go7cW1MxGDOypiPTHdO_SPUV0fopZk3Y16yhk0iHijPRJl-KHZFQAyZxZO3QI7E3V5Jt8BY23XL5ro1Bmlfoe2ytYw3Hec8LVO4RkL1wCAF5yPAIPLJHh-oEXsKym2VT0f1rNvJbsTLTMIp1xJqP6wUXHFQoeKDQUORvA4CqJ4SmBUBniBKzwXMX0Mj7USKZUB9LdJlP6spiTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: چندین نقطهٔ حساس در مسیر تأمین و انتقال نفت خام از شرق عربستان به «ینبع»، با چند فروند پهپاد هدف قرار گرفت
🔹
این اقدام در پاسخ به نقض حریم هوایی یمن توسط پهپادهای دشمن سعودی انجام شد. @Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/452940" target="_blank">📅 16:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452939">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j00lDS53Nyinwvz8u7gWDTpQpLoWio5e4R86WSjzCNvbtfOpq2DI6yn_lvXNNVO0F7OLm4GRce0R692aqv5mbGCoItFatY2e8ci6KdcoXcTngV-7N00u8BNosNO1e1hUyDAzvqc47qvOMeThDxLCTpMDi3_dAIzk6FtwV78VrkU3NDqDWiAIxVL_Q8-P0Ma2eRjWLZdU_E-qS_GxMphH_HvTG7f5ISGH2vabbeq0zNQB_OnGnvhwNNgVbMxmflMkAjXCq9B6-DRGmmDHGpDQvP4DUJ80Tf6JV3fAtNXLJM2jfQuJSIMfNRIlQ3JaoL81jK5jzOH1nWqSHK-1dm5GZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راوی اربعین باش
🔹
این روزها میلیون‌ها عاشق، راهی سفر‌ند و هرکدام، روایت خودشان را از این مسیر دارند.
🔹
اگر شما هم امسال زائر اربعین هستید، عکس‌ها و روایت سفرتان را با ما و دیگر کاربران به اشتراک بگذارید.
🔹
مطالب خود را با هشتگ
#اربعین_۱۴۰۵
در سامانۀ فارس تعاملی منتشر یا از طریق پیام‌رسان‌ها به نشانی‌های
@Interactive_Fars
و
@fars_ma
ارسال کنید.
🔹
به برگزیدگان نیز هدایایی به رسم قدردانی‌ اهدا‌می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/452939" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452938">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390cba696e.mp4?token=B9s92zCcktCxGWBGrFLKlGCQ_urADJntO4Kpq3QgBBPoe2qgfkD_Vc8Kcf2_2jUspxT7ciGedaB_h4_5NGWevCLCr7r2ThBEZK6jKu7w19ZPfVKZHnWpVBS48yJNy5HglBMFGMc7PIxBp66mtD0OjAhL6XzWSWWi2t01AJ5s0NrHgcRkmWzV2VvrCeCcyB-_WQoE73YgG6taHd4UHyebyVv5FW7Zgq8lIpQQjpDtZmsS1eGbiBjktoToFuH6iaQ6hiOHLpHTe8hSrvAcQS3PXuKHzSpWvaK-L3W0G0iUR4euG__-CapfM-kAomC8Tv3UxKKoX41meHr9VP3xuyjfug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390cba696e.mp4?token=B9s92zCcktCxGWBGrFLKlGCQ_urADJntO4Kpq3QgBBPoe2qgfkD_Vc8Kcf2_2jUspxT7ciGedaB_h4_5NGWevCLCr7r2ThBEZK6jKu7w19ZPfVKZHnWpVBS48yJNy5HglBMFGMc7PIxBp66mtD0OjAhL6XzWSWWi2t01AJ5s0NrHgcRkmWzV2VvrCeCcyB-_WQoE73YgG6taHd4UHyebyVv5FW7Zgq8lIpQQjpDtZmsS1eGbiBjktoToFuH6iaQ6hiOHLpHTe8hSrvAcQS3PXuKHzSpWvaK-L3W0G0iUR4euG__-CapfM-kAomC8Tv3UxKKoX41meHr9VP3xuyjfug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم عراق! ما این اتفاق را فراموش نمی‌کنیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/452938" target="_blank">📅 16:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452936">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eae8240a.mp4?token=Zb0y05SYg19IQLtKbvWiiRI5TlCGfDnxOiIIRi9v9aU3en4VzaZhFc_YkE980wWsZNJe2WlvIygHNeujDw5US2a9uqN5Lfo23dpF6BOcw6RIw3OErYNOrif9Xx4Ae_WvHWkjRxj0K3itWcIQkDGZWR9LShnExTvrYMMeMkkPseUMTlbbLXK57rHUdvb9lEUI-7XuaiK3v9nwS2Z7Hs3IdQ5q5z213_9SpxSY4Wyg6Hyg3Qc9CFvsMo1lpeybIcsA5FBz8EYT5V3DNJPQhRs8Owwdk7eCWnRCJfilO1mMY8_YzbflSD7c4KvL-RCvNxhnuoodfrK5TbAgzMbi8jx7EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eae8240a.mp4?token=Zb0y05SYg19IQLtKbvWiiRI5TlCGfDnxOiIIRi9v9aU3en4VzaZhFc_YkE980wWsZNJe2WlvIygHNeujDw5US2a9uqN5Lfo23dpF6BOcw6RIw3OErYNOrif9Xx4Ae_WvHWkjRxj0K3itWcIQkDGZWR9LShnExTvrYMMeMkkPseUMTlbbLXK57rHUdvb9lEUI-7XuaiK3v9nwS2Z7Hs3IdQ5q5z213_9SpxSY4Wyg6Hyg3Qc9CFvsMo1lpeybIcsA5FBz8EYT5V3DNJPQhRs8Owwdk7eCWnRCJfilO1mMY8_YzbflSD7c4KvL-RCvNxhnuoodfrK5TbAgzMbi8jx7EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسیرهای جایگزین پل‌های آسیب‌دیدۀ هرمزگان آسفالت شد
🔹
این پل‌ها در حملات آمریکا آسیب دیده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/452936" target="_blank">📅 16:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452935">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌
🔴
وزارت دفاع عربستان: چند پهپاد از سمت عراق وارد آسمان کشور شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/452935" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452934">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_GkOEtOxEPkJDSLaN9rxAYauv0wMeedx3dIu_mtX_2vKcFOEspqmNJEczEHhPnK9yXHQMQT1dlzWIDinoT8X7zbcpVTtOxuccy8jZ7qzfdCyoggkXkyEuKP1-YtbrmdYv_3_TJ72qN_tXvxsNbKxo1xNgy54V-QL0khLgfayoDWHuLPLopzuZDAIu7VK1E5ZC34442f5CE2DAlGjyEqusWwcJLMAuo3LSxO3WZIjLzRS1IYyfdopkd_BZllbaHpt7T4WvP4WXjRPTITT6NCnJwe2PaiMPqzBM7hdomep9ANCyqblIlAK4YIWBE7sR681Jb5iO590UEA3UxljxaHnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطالبات معوق کالابرگ، سرمایه فروشندگان را قفل کرد
🔹
طرح کالابرگ الکترونیکی که با هدف حمایت از معیشت خانوارها اجرا شد، حالا برای برخی فروشندگان به دغدغه‌ای جدی تبدیل شده است.
🔹
مغازه‌دارانی که کالاهای اساسی را در اختیار مردم قرار داده‌اند، اما به دلیل تأخیر…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/452934" target="_blank">📅 16:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452933">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHn4Hmdxr4JNfQKPL7RZHbTFvT53DDF--zOWLho43-iO67QKw2oxBpNjhLa9SIfTNX65PQFeLxJEoaElYe9ntiLSaI4TaE6oxCy3dRVLaTepKdZjts1x6i200GnsYi6F6y89DrKn6STS7a4fyHip1-3sKP7ycKTrUQh6ox_p3tM43KUuBW2o5BJ18oYDX3T9lmRgGZh_Ilu9d6PyPswFZ_nRjJboVjXl1Ek25DIc2uQBIqBPCfmPnR20z_psQLGt8l_N_vO0YIYPnsnrhqI5O_2NmvYOBa5MzLbZ5f2QaBo5lmzWks-h7-LHI9kBqLr40mh9nHz0H1lnEMpetFkSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعزام ۱۸ هزار زائر مناطق کم‌برخوردار به اربعین
🔹
رئیس ستاد اجرایی فرمان امام از حمایت این ستاد برای اعزام ۱۸ هزار زائر مناطق کم‌برخوردار به اربعین ۱۴۰۵ خبر داد.
🔹
سید پرویز فتاح گفت برای خدمت‌رسانی به زائران، امکانات لازم برای طبخ ۲ میلیون پرس غذای گرم، توزیع ۱۲ میلیون بطری آب معدنی و تولید روزانه ۴۰ هزار قالب یخ در مرزهای اربعین فراهم شده است.
🔹
او افزود بیمارستان سیار ۹۲ تخت‌خوابی در مسیر نجف به کربلا، بیمارستان ۴۰ تخت‌خوابی در مرز مهران و درمانگاه ۲۰ تخت‌خوابی در مرز شلمچه به زائران خدمات درمانی ارائه می‌کنند.
🔹
فتاح همچنین از ارائه مشاوره رایگان از طریق سامانه ۴۰۳۰ و اجرای پروژه‌های عمرانی و توسعه زیرساخت‌ها در مرزهای مهران، خسروی و شلمچه برای تسهیل تردد زائران خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/452933" target="_blank">📅 16:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452932">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYx5P8r9fkWE0MMVdxwrdkbYecC0PTENLnzuJNXCyhqQTZiJupO0rsgcVzkHqBKB8QsMC_O4xeHCv54fV-ZQEjxXu7gY_UNUXY6Uh_WFjaw0jDs0LzqFk37-Y3kQTQFvpfxPwz_r30ZrobZcSG20Xp6FNaVwXUfHSbwPnQC6yhUnecS5vFfIzD1jIp6hEFIhmEnXNw3AGqgLpLlQBWO87Kmv7qiCjc6FiF1W-BddlpDrQJ9XoKfXKTfdi4xZ0NOQ2z7Bo6bfo_B33WTKMpTsZRQJ5yY-9uZCmKY3985paguOf2eKhFb1-j_YV279TzM6WlfKKvx6tBFH-svyIWMKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیگ برتر ۱۸ تیمی شد
🔹
در جلسۀ امروز هیئت‌رئیسۀ فدراسیون فوتبال تصمیم گرفته شد با نیمه‌تمام اعلام‌کردن لیگ برتر و عدم معرفی قهرمان این فصل، سال آینده مسابقات به‌صورت ۱۸ تیمی برگزار شود.
🔹
دو تیم نخست لیگ دسته اول به‌صورت مستقیم راهی لیگ برتر خواهند شد و تیم…</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/452932" target="_blank">📅 16:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452931">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c37b1d5a.mp4?token=uuV8bmla3tIPruyBnS-9jEdOyvMNGKSmZ-RXUrVkHgQalUZ9pmebTCIz_xe3eOqluUSPj4ttowdrWKJdz-xzghRpROx_oKWyZ2nFGDEZxK9IgzvibyxLFS5kQBn0vysAf60wKMPYOFKi_8_lkxQP6mBMABI9OqhstwJKlldXUO8MMMwkU543shdGhD_7GngbTU6nK5lqFRKy0LPRw__bjsxIko6kI94vKWfxfMw7DcOY_lUSaDSCq-cBJJi8vHmE3shemljOPgjI-CME9NLS1H1Sd7im61GqNQDryYkW-L82U7Dc2WCPR43hh6xZz9RGk24THUqn5JRrj3l-LdkS0aNOqd9DwULxAy6xWQ7V4qTUMyZeyTBG041H_9Dvwnl5AHU3XVsfroZxBEdstrAP6tbsu6MKDyXS_XvEEdTajlTdHvIW7B3tjNdCIpUX9F849gW-qG5Uf7EMlEraejdXWtolDzVYZFPg-I7xdz-pQ39tPuljYjvsPaj8HkZLlMz_Ir3_w0O0K5pLyA_2M-08sdeIQJ3uprLYfM03yF7k5m8ScHWVkJkzP4vzOntCnZaMIZAD4GhROPQMEVDpENJWWKkoRWJ8m2XWFeNTE6x6jLq4vM7chTVCWxFEhDcVYqDGW7rwoNyVcVZrZ-0PG2f4Wwec0A2LeTFiQx3wWUOm1GE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c37b1d5a.mp4?token=uuV8bmla3tIPruyBnS-9jEdOyvMNGKSmZ-RXUrVkHgQalUZ9pmebTCIz_xe3eOqluUSPj4ttowdrWKJdz-xzghRpROx_oKWyZ2nFGDEZxK9IgzvibyxLFS5kQBn0vysAf60wKMPYOFKi_8_lkxQP6mBMABI9OqhstwJKlldXUO8MMMwkU543shdGhD_7GngbTU6nK5lqFRKy0LPRw__bjsxIko6kI94vKWfxfMw7DcOY_lUSaDSCq-cBJJi8vHmE3shemljOPgjI-CME9NLS1H1Sd7im61GqNQDryYkW-L82U7Dc2WCPR43hh6xZz9RGk24THUqn5JRrj3l-LdkS0aNOqd9DwULxAy6xWQ7V4qTUMyZeyTBG041H_9Dvwnl5AHU3XVsfroZxBEdstrAP6tbsu6MKDyXS_XvEEdTajlTdHvIW7B3tjNdCIpUX9F849gW-qG5Uf7EMlEraejdXWtolDzVYZFPg-I7xdz-pQ39tPuljYjvsPaj8HkZLlMz_Ir3_w0O0K5pLyA_2M-08sdeIQJ3uprLYfM03yF7k5m8ScHWVkJkzP4vzOntCnZaMIZAD4GhROPQMEVDpENJWWKkoRWJ8m2XWFeNTE6x6jLq4vM7chTVCWxFEhDcVYqDGW7rwoNyVcVZrZ-0PG2f4Wwec0A2LeTFiQx3wWUOm1GE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقدم‌فر: دشمن امروز بر ایجاد اختلاف و ناامیدی متمرکز شده است
🔹
مشاور فرمانده کل سپاه: امروز اختلاف‌افکنی، تکنیک دشمن است. دشمن به این نتیجه رسیده که با کار نظامی نمی‌تواند حریف جمهوری اسلامی شود. آن‌ها در دو جنگ شکست خورده‌اند و به این جمع‌بندی رسیده‌اند که باید از داخل ما را شکست دهند؛ از طریق ایجاد اختلاف، بی‌اعتمادی به مسئولان و ناامیدسازی مردم، این‌ها همان عواملی است که انسجام ما را به هم می‌زند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/452931" target="_blank">📅 15:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452930">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb30eccc7e.mp4?token=eWKCM5GONfRkmVSjilIa1MK0sH67MO-NgMp8fn3PAQcdGoOMzb2hDCM-R4xnBS7qkPvFFuJvCVcGQMp7AVYAvLObqmjvZX7H4tI4Wvv7l_7rpI7EmzeUIUwSonjuL6W9BkcjN7pkeUhN5hQOj0_97YU2E2TZLK29gGK-dYsOokdZDm3Bhn2fXdJXW8YqH-b_YwfVHNz7uXdUQ2ZucA3ahUX42AdAiPqiH7q29Fu-HaZOJNfe8qgI0QHKXh9Rrvk2rSn0KcOgNmf2u60h60aefzYlr3jnovulJZeo6ZKIPMzuOe_T1lcv-P9hOz5MUR-itzTJyNOMqE6ckLikIxJ9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb30eccc7e.mp4?token=eWKCM5GONfRkmVSjilIa1MK0sH67MO-NgMp8fn3PAQcdGoOMzb2hDCM-R4xnBS7qkPvFFuJvCVcGQMp7AVYAvLObqmjvZX7H4tI4Wvv7l_7rpI7EmzeUIUwSonjuL6W9BkcjN7pkeUhN5hQOj0_97YU2E2TZLK29gGK-dYsOokdZDm3Bhn2fXdJXW8YqH-b_YwfVHNz7uXdUQ2ZucA3ahUX42AdAiPqiH7q29Fu-HaZOJNfe8qgI0QHKXh9Rrvk2rSn0KcOgNmf2u60h60aefzYlr3jnovulJZeo6ZKIPMzuOe_T1lcv-P9hOz5MUR-itzTJyNOMqE6ckLikIxJ9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های سیدمجید بنی‌فاطمه در حاشیۀ محرم‌شهر دربارۀ عشق اکبر عبدی به امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/452930" target="_blank">📅 15:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452929">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/452929" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452928">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/452928" target="_blank">📅 15:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452927">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74255f8ed.mp4?token=meP5XYp8Ixcw1Yxno7TsfJCZUBI2ugm764zB4FNyuQKMuoBIKfpvbbmvPOI0vbvM-9H6-k26USU1fY2Kc-bV8kPB0L8NJO-2Ec4-RCnltr0tZ5ImWoFM-g32jT6jKw3IZ0NTZZTo9Aegdy9hAG_l33n8dMx9Zkp_Eq0-PBYs6W3WXdXMpw2JzKE7N5QCLazM_Q7H_pGmgMf35XWqizmrFWUYacu0tAfG-bqROPN1DBalXh1gY3Y40U7u-3XEAwM_ydXqNFUDkAl3Thxiigj1Y1BV0JLwweVx9HUifHs1UoH-QVH8TFbLQ8UWfJdtyI5Js2Qd_h1d0DeeNWud5U1sFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74255f8ed.mp4?token=meP5XYp8Ixcw1Yxno7TsfJCZUBI2ugm764zB4FNyuQKMuoBIKfpvbbmvPOI0vbvM-9H6-k26USU1fY2Kc-bV8kPB0L8NJO-2Ec4-RCnltr0tZ5ImWoFM-g32jT6jKw3IZ0NTZZTo9Aegdy9hAG_l33n8dMx9Zkp_Eq0-PBYs6W3WXdXMpw2JzKE7N5QCLazM_Q7H_pGmgMf35XWqizmrFWUYacu0tAfG-bqROPN1DBalXh1gY3Y40U7u-3XEAwM_ydXqNFUDkAl3Thxiigj1Y1BV0JLwweVx9HUifHs1UoH-QVH8TFbLQ8UWfJdtyI5Js2Qd_h1d0DeeNWud5U1sFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در سمت خدا: اربعین دو بال دارد؛ محبت به امام حسین(ع) و بغض به دشمنان
🔹
در اربعین امسال، قرار است خون‌خواهی به عنوان بغض به ظلم و ظالم به اوج خود برسد.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/452927" target="_blank">📅 15:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452926">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📷
زائران اربعین، استوار در مسیر
🔹
باوجود افزایش دمای هوا در مرز شلمچه، موج حضور زائران اربعین همچنان ادامه دارد.  عکس: فرید حمودی @Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/452926" target="_blank">📅 15:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452925">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCIpknsggGHijmUQmGl9WY06yEIUV1AepOKq4xpZYkM82YR5M2ZX3oNldsiXfUkaIpMRu_d5YyX7_isJiqAwHIrPcdECAt01KXF-11-tgVcFeJbkbyrly8HQgZ2xkj_06DpcwL7lho6DhXS183Mn_x-z4jQlgJb0Hst-HGwpF8D5Y2nD68GeLHzmO5B6xwuReoTHgsQtfEipobtOPwO-0a1ldUDC8zCm5Kd0WOh_c723lAUhm30OUI0TyHmIctY6gt645MkupiBe2otpCAk5QVB-BWzhKBhUpW1UUfcn_cZ8QCjQbaZ44DUXFUXAM8vH0x5qSY8vAzmpLU8Hd5GDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام بسته ارتباطی اربعین برای شما مناسب‌تر است؟
با نزدیک شدن به اربعین، انتخاب بسته ارتباطی مناسب به یکی از دغدغه‌های زائران تبدیل شده، به‌ویژه برای کسانی که می‌خواهند در طول سفر بدون نگرانی از هزینه‌ها به اینترنت دسترسی داشته باشند یا با خانواده و همراهان خود تماس بگیرند.
مقایسه بسته‌های همراه اول و زین عراق نشان می‌دهد برای اغلب زائران ایرانی که به اینترنت، پیام‌رسان‌ها و خدمات آنلاین نیاز دارند، بسته‌های همراه اول انتخاب کاربردی‌تر و به‌صرفه‌تری است، درحالی‌که بسته‌های زین بیشتر برای تماس‌های محلی داخل عراق مناسب‌اند.
همراه اول بسته‌هایی با ترکیبی از اینترنت، مکالمه و پیامک ارائه کرده است. در میان این گزینه‌ها، بسته ۵ گیگابایت اینترنت با اعتبار ۱۴ روزه و قیمت ۸۰۰ هزار تومان، برای زائرانی که در طول سفر به اینترنت بیشتری نیاز دارند، انتخاب قابل‌توجهی است.
در مقابل، بسته‌های زین عراق تمرکز بیشتری بر مکالمه دارند. برای نمونه، بسته‌ای شامل ۱۰ دقیقه تماس بین‌الملل و ۳۰ دقیقه تماس درون‌شبکه‌ای زین، با قیمتی حدود ۶۶۵ هزار تومان عرضه شده است.
زائرانی که بیشتر از پیام‌رسان‌ها، مسیریاب‌ها و خدمات آنلاین استفاده می‌کنند، باید حجم اینترنت را در اولویت قرار دهند.</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/452925" target="_blank">📅 15:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452924">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeTsv3JEzOaFEH5gwNiRIR48x-T-HUYXxRYA1xa7xuq5h-lTCVU976A4eBVUcUiPZeupELnJ6b6gRiMe9kN_UbzEl1_MoyKcqPv0kAyvmJeVKYn59Y4yNyogzGBkiKzUJQb0YLID1KB3qqd2XfhNen2oeZEk0jD83fcCcIW5YZKMo_y_ENKrO0CN3L2ynaEpEWsPCEDjaahUbFJCkilFw_u-bDiON6FKx0Zux2j8E5tdoUP_0pHnfKKJZvYoxZulIUzLe7FEXD03HSbqkLlNEtxI2VaUgkgE1oEvDjSKNIFp5DTE22KfFU1a4XdRj5_9yEXp1gTEAPGzxw74cQJuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
خدمت رسانی شعب کشیک بانک کشاورزی در مناطق مرزی به زائران اربعین حسیني
🔻
به منظور رفاه حال زائران اربعین حسینی و سهولت دسترسی آنان به خدمات بانکی، شعب کشیک بانک کشاورزی در شهرهای مرزی غرب و جنوب غرب کشور از ساعت ۰۷:۰۰ تا ۱۹:۰۰ دایر و آماده خدمت رسانی خواهند بود.
🔻
شعب کشیک در استان های آذربایجان غربی، کردستان، کرمانشاه، ایلام و خوزستان تا ۱۵ مردادماه از ابتدای وقت اداری تا ساعت ۱۹:۰۰ به صورت مستمر آماده خدمات رسانی به زائران و مراجعین خواهند بود.
اسامی شعب کشیک بانک کشاورزی در مناطق مرزی در روزهای ۵ تا ۱۵ مرداد ماه
🔗
مشروح خبر</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/452924" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452923">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/452923" target="_blank">📅 15:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452922">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP_bqZIKg01MTa5amaXqcqr7dwQguNXSc64u7Qi3Ou9ICPSx9VuB5LXa9L6qz1CuNt431DnYkSse2G39Emsu-R9jIT41G-o6S7AbjL_V-bJG-GjPBv7iDDXY_qVjX-yu9CbV9lmVXp8Eb-M7AMxOelqRHeDEO6ZBgpZDHnX-x0MNjMRNb8x4hWKldrXFNRBDDwXVYyrpObpfbT772l3Yk3tPN2nj4eSZ9uRJBnWUsEGBIB9J6YDYIjYTQwMkEmUpziJp4-rFg9d8sOS4vVgJFd7w3JaGusALUtWNffr5vf7c6hzeoNJOR1jKGNI6EThaB9Wib9O608gzP8yptj9z7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قلعه‌نویی: بی‌وطن‌های ایران‌فروش گفته‌اند که خوب شد تیم ملی صعود نکرد وگرنه ما بیچاره می‌شدیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/452922" target="_blank">📅 15:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452921">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9419b58485.mp4?token=nNRhWKBF5Vf1MGLFs-Ypu84-sazc7rYAVVjiFPHWCpTbKfY0WhwpEwKf4Q_ABqNXQR9mGIpXV37bUbDLUi5xBYd7kHlwIIS-_JK0quezCulFsujlN2_VVe64utvjavEOlraMstHdRFDAFV-dd6RxcJk0BtI6IBVftdt6kGBQxFAYLuVmlo8tpAU4so6Q98FacTHiFgH_YbgIcYNVgksitHq6JDrArYxDrDJvsg7ViSZNNQm97iYa2HmAKTqWRYqaRc11AnB7CeSzl8JiF9LFk5hzGVYD3dLUGpJ0_QFyeyHp62IAzk4NNkfAcot7iWrUUatOTjnIVj2uYGTcV33emQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9419b58485.mp4?token=nNRhWKBF5Vf1MGLFs-Ypu84-sazc7rYAVVjiFPHWCpTbKfY0WhwpEwKf4Q_ABqNXQR9mGIpXV37bUbDLUi5xBYd7kHlwIIS-_JK0quezCulFsujlN2_VVe64utvjavEOlraMstHdRFDAFV-dd6RxcJk0BtI6IBVftdt6kGBQxFAYLuVmlo8tpAU4so6Q98FacTHiFgH_YbgIcYNVgksitHq6JDrArYxDrDJvsg7ViSZNNQm97iYa2HmAKTqWRYqaRc11AnB7CeSzl8JiF9LFk5hzGVYD3dLUGpJ0_QFyeyHp62IAzk4NNkfAcot7iWrUUatOTjnIVj2uYGTcV33emQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرامکو همچنان در آتش می‌سوزد
🔹
تصاویر ماهواره‌ای نشان می‌دهد که تاسیسات پالایشگاه جازان آرامکو که ۹۹ درصد ذخایر نفت خام عربستان را در خود جای داده، پس‌از حملات یمن همچنان در آتش می‌سوزد؛ احتمالا این دود عظیم ناشی‌از آتش‌سوزی یک مخزن ذخیرهٔ نفت خام است. @Farsna…</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/452921" target="_blank">📅 15:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452920">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فرمانداری بندرلنگه: صدای انفجارهای امروز ناشی‌از خنثی‌سازی مهمات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/452920" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452919">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f433f1e1.mp4?token=GjyYdeMSeP0wXUo8W8HjnB5h4sP0D0KVpXqlIzw4Vpxx6V5omEKJHOHXbF0dzL2d0bOPEby605u7GBWtmvhpkOCPk5DXtMUk9Mik8JHRadEQDgXIoGzvw4i1fTMljay-0piiufeSi6NqPVnMAV4ozo8Gt7MSGMdIISBezV7NvAk4wmX3WLAwxnCHgAqR3LjPMdsj6FSQFhAKkmSYlWGCE5LvwOR_FcFS-WQRCD5pvm3tINeB8I6k82mLcRYG_9_lO3Tl39QdZECqzzhmTRNR3Nj8hX7UDFQ_WS_ZuLIX9Ez3Iyu9cGqFo-kydB_1KqFyD_azQ6MiHlq4riYi-XtCOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f433f1e1.mp4?token=GjyYdeMSeP0wXUo8W8HjnB5h4sP0D0KVpXqlIzw4Vpxx6V5omEKJHOHXbF0dzL2d0bOPEby605u7GBWtmvhpkOCPk5DXtMUk9Mik8JHRadEQDgXIoGzvw4i1fTMljay-0piiufeSi6NqPVnMAV4ozo8Gt7MSGMdIISBezV7NvAk4wmX3WLAwxnCHgAqR3LjPMdsj6FSQFhAKkmSYlWGCE5LvwOR_FcFS-WQRCD5pvm3tINeB8I6k82mLcRYG_9_lO3Tl39QdZECqzzhmTRNR3Nj8hX7UDFQ_WS_ZuLIX9Ez3Iyu9cGqFo-kydB_1KqFyD_azQ6MiHlq4riYi-XtCOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اندیشمند آمریکایی: هیچ راهی برای تسلیم ایران وجود ندارد؛ ما بازندهٔ این جنگیم!
🔹
مرشایمر، نظریه‌پرداز و دانشمند علوم سیاسی: هیچ مجموعه‌ای از اهداف وجود ندارد که بتوانیم آن‌ها را هدف قرار دهیم و ایرانیان را مجبور به تسلیم کنیم. این اتفاق نخواهد افتاد.
🔹
آن‌ها تا پای جان خواهند جنگید و توانایی زیادی برای این کار دارند. ما در جنگی در حال باخت هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/452919" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452918">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GchwRmJ0Khloo-_ZAjLH06hX-ktYOX0quL0DBVV-n9vMH9XdpKY5AJjBhf76SVqYxNYZUNd7GxqAAtUdGztrI_YTPYaryIJ-5dmDb7j98VBFME6IdAH9xLtUxioNIUkl2fNvijnupbfsll-fgMntKQqDp1cC0Mp2DMJCHKWysMyLVEHX0UE51_QicHLglvjGrZn3X7Fu4YlhfeY3IAx53eaUFijeGbhKK3flLS47Y7d4pGYGLiunzPYCnO4yYo7juSKu1TvTJOyDRI0T1CNYx1KIhUD-gVSvzo57ilDMk8bnBqSf9aDWBYsLy5RivrYg4mCTwnODH4APGzP4EUxi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ استاندار ایلام: تردد زائران اربعین از مرز مهران از ۶۶۰ هزار نفر گذشت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/452918" target="_blank">📅 14:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452917">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d783b974e.mp4?token=KyDsM_BAlxJrG148B6N4yOZyk4mFLKf46F5ZUFV2HIAOF77QDj8uqZx4AVClLRE-Ss66w9bL71DmT9SquP3fUlVFsA61pabihQWWYa9MqYQVWe5lvB5zKwsVOWYdQF12KpkAWe84-PQYUDgq0m3Zoi-zfrIQN6cBPlxfv9HdSHbNZ5CUJA_oFxzd0JmALfqXHMD6b58eJlG7x38ydkJYBoXF9Kw-b7FbrOadjlez0x3tRmC0RN6A3q2GKDUgHv9KSGO_hNUluSzu-al76kKxMotUTBwoxkIjr3dFzuRGtNmIqwl1FGn-LL7KwVJpdIfOFpSU8AS7W9oZN_D0mgwH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d783b974e.mp4?token=KyDsM_BAlxJrG148B6N4yOZyk4mFLKf46F5ZUFV2HIAOF77QDj8uqZx4AVClLRE-Ss66w9bL71DmT9SquP3fUlVFsA61pabihQWWYa9MqYQVWe5lvB5zKwsVOWYdQF12KpkAWe84-PQYUDgq0m3Zoi-zfrIQN6cBPlxfv9HdSHbNZ5CUJA_oFxzd0JmALfqXHMD6b58eJlG7x38ydkJYBoXF9Kw-b7FbrOadjlez0x3tRmC0RN6A3q2GKDUgHv9KSGO_hNUluSzu-al76kKxMotUTBwoxkIjr3dFzuRGtNmIqwl1FGn-LL7KwVJpdIfOFpSU8AS7W9oZN_D0mgwH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاهدۀ پلنگ ایرانی در منطقۀ «شکارممنوع» لار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/452917" target="_blank">📅 14:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452916">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fc7819224.mp4?token=WwPIeTTbFS15M7_9DeDk4c9rluGOZnbdfMXjoJmq-JwsFOjxoBQgQ5VsiwqomEkvDnugqCGmfhep_Rx38ud4WINhC6RH0ip18jVuTnd0SqQ8Q0p5M9U1fmkjo1EWvkD-xsrN_-hO9odALaXD1lJWnQ62Q1E0uvjjIAsLu3R6eaE7utrwFmxG1_M1m2n0CMEe70j6HVIkeDp4WF6jTH5pV0FamhMyMDVi8-MeSvT3GRkm_DguLxCWNbKlLlTqJK4tEWK9PNPYcn1QHXhtKs7NKBGRVqLLPsNgHPVyDnxvdtVNLty8TSL4w0x9sT58qPQSgfm1-alBAmbhSpweEYSzrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fc7819224.mp4?token=WwPIeTTbFS15M7_9DeDk4c9rluGOZnbdfMXjoJmq-JwsFOjxoBQgQ5VsiwqomEkvDnugqCGmfhep_Rx38ud4WINhC6RH0ip18jVuTnd0SqQ8Q0p5M9U1fmkjo1EWvkD-xsrN_-hO9odALaXD1lJWnQ62Q1E0uvjjIAsLu3R6eaE7utrwFmxG1_M1m2n0CMEe70j6HVIkeDp4WF6jTH5pV0FamhMyMDVi8-MeSvT3GRkm_DguLxCWNbKlLlTqJK4tEWK9PNPYcn1QHXhtKs7NKBGRVqLLPsNgHPVyDnxvdtVNLty8TSL4w0x9sT58qPQSgfm1-alBAmbhSpweEYSzrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نگرانی زلنسکی از باز شدن جبهۀ جدید جنگ با ایران
🔹
رئیس‌جمهور اوکراین، در توجیه حملۀ پهپادی به یک شناور ایرانی در دریای خزر که به شهادت یک ملوان منجر شد ادعا کرد ایران قبل‌تر با ارسال تسلیحات به روسیه، علیه کشورش اقدام کرده است.
🔸
البته این درحالی است که ایران…</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/452916" target="_blank">📅 14:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452915">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpvKYA34e2k542nyRC5SvpOmP0vWOHjhM8obBRN6x40pO_jLr5zybFw9KTNQ2PaC5jq8YhM5lCpOXsEsmOBKe8yMRU0jiutXVGDR8EK7nII-w-bOqRO46ESVCa2KrhlPjmGhwl7nwth1zBv7kpyB-wNos85eBE4UcVV4KPtzhgFt0alQV8lMe9FpCY1nMMj4lUSkO9pmL5T7hmdtcoRyVQk2fC3MlyWENYzF6lRjElVuo-zrajLLI70ya9xPt8_KK_mmRpQ-Ez7MOSFKzyUxem297h42WwIg5QkAKsWwAetZQFqi5A9ky_3KHWWmPfi2qBQc-CFwTPebG2bQ5NbBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: نبرد هرمز، نبرد برای آیندهٔ ایران است
🔹
‏نظرسنجی یک مجموعه رسمی و معتبر: «ایران باید مدیریت و کنترل خود بر تنگهٔ هرمز را حفظ کند حتی اگر این موضوع منجر به جنگ مجدد با آمریکا شود»
"موافق ۷۸ درصد"
این نظر ملت ایران است
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/452915" target="_blank">📅 14:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452912">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZA3naY0KbPpHM4Vi9Ef-iTCU5oS_F6Ydcm0qQJ4IY_GkZiHfn7Hjjg9u_cXOsDy8kFHZAbTbm_nYTaPpaYln7Z8m_PUZyZScCJYZRlGfnOufWclxa7tSXxdxdx37s8FjWGboGC7Pm2XrKNWg5WDCAsKli_3FzQ0IA1Ls88Ld-EYiPzuJnP01iarQ-l2AdumjuM2NvgBR9lcYZNM8lFCYeqYUZjAqFjB03h3fXW5y3grKxPFu8rvbBrt6GcU6_tihVKurr08dy_rqNC1m4BQVhIiRJaeEKFecg4OVZ5IE-eT_ANxrS28v2UAQSgbCwsb6-y1Yp60T8XfXedJWZiepkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnyXhrGAUTfP7xz8OoH-BbThjAjaUJwZPd81M7gSgnl6zq-zz7zI_C5xKakme0czFmTH8iwksdMMXeNdWEgCQNoAjYtpoKjeGsZe4pZU8nPSOcy-hl7HxhUHwMcvnixxSrEILRegRs6TntFoR_06Ev5sMTs-5iIkIzHaBuyqM6xj8LBYmUUPSnE2USha4f_d2Vj8gv5SUbG9FUh16BhuTYAlMBfFakERBb04OxrtcRanNWU1fTNNOTsDHgt62hlKCGikkKnVsnf-kwu-dHc_MKLdAp1zxlCkbXCYW1dIN3odY-v0ZUy-RuWWhxVnizrAdPiS8ssxKbMBwMLUcHAwgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EItK5lFV8DsMaQq7SUAhKFzyZ7VNLKMUaJ_9RTObi8H65aBVe9qSnfycKlhkZvp3Uby1aE7whoLpETUnqQTVdyadg2MHcoDpz766frWrwxr4Go_yI3_pT1P1Xy-M9ZyISvrLF2X9fw4MElLUrRnVDEThYi_HA8on1IA4G_cj1D-lhbHwud4ziRU318A-ix2aDGpJY8btZyPeZVw61sGADa27E3seyTHDYlE7IgwmSbJ5lP8Zzb6E6JZ6nYwbxk_jUoiUwfocvDeHEuNfg5APIqfEZyy8hfQfvru2lrtTuUhlVD9jx7Gd4bwfU6VOeWTmTZ9hiQMFYXqFodynV4mTEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
آتش‌سوزی در هتل پارسیان تهران
🔹
سخنگوی آتش‌نشانی تهران: آتش‌سوزی در یک مجتمع اقامتی در هتل پارسیان در تقاطع بزرگراه چمران و خیابان ولیعصر باعث شده شعله‌ها به‌طور کامل این بخش را فرا بگیرد.
🔹
عملیات امداد و نجات همزمان با اطفای حریق در حال انجام است. آتش‌نشانان…</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/452912" target="_blank">📅 14:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452911">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1668f513a8.mp4?token=UCsQVb9_ChE1OOBU3U7lONLMF-NdEU2OhEb5xl2uJ9U3UczTLnLWrDT8V_FtungAz_CQvr6gEOmswByivwN_G-tHFGs98K0uGZwpYw0EY_L4123lxSY0K_ZouoD8Sr1bcdsaTtiO4EwtY9YXYyKT3nZ-cOamacHxoZcRc8htiLd92pMmLFWYXE22lRywqjifIrwXJKgdXR3oOg3qL-Kwbh_kQiUnDCFrEIELREWyDIOdLVFGGnIvcD_nx_cpVuI-8ZuRrYgHbl1Lw-sa_M-2akE-KNTkYYfjiuSJ6Z_rk973U4Zbywp7o-wFsl6SBSL1GmRNkTJGb0Bim5jFkEx0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1668f513a8.mp4?token=UCsQVb9_ChE1OOBU3U7lONLMF-NdEU2OhEb5xl2uJ9U3UczTLnLWrDT8V_FtungAz_CQvr6gEOmswByivwN_G-tHFGs98K0uGZwpYw0EY_L4123lxSY0K_ZouoD8Sr1bcdsaTtiO4EwtY9YXYyKT3nZ-cOamacHxoZcRc8htiLd92pMmLFWYXE22lRywqjifIrwXJKgdXR3oOg3qL-Kwbh_kQiUnDCFrEIELREWyDIOdLVFGGnIvcD_nx_cpVuI-8ZuRrYgHbl1Lw-sa_M-2akE-KNTkYYfjiuSJ6Z_rk973U4Zbywp7o-wFsl6SBSL1GmRNkTJGb0Bim5jFkEx0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب زنگ‌زدۀ استعمارگران در جزیرۀ هرمز
🔹
در ساحل شمالی تنگۀ هرمز قلعه‌ای فرو ریخته و توپ‌هایی زنگ زده وجود دارد که پرتغالی‌ها در قرن ۱۶ میلادی آمده بودند بمانند اما حالا فقط قاب استعمارگران است که در ذهن تاریخ جا خوش کرده.
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/452911" target="_blank">📅 14:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452910">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRfENQ9aHouSct6L1V7TKt7bGeIODsVgIKN9k79wR6G-W41yueWQ1mxct6YqhSEs8TXvB8Ihbsy5WbL4HAdeo0sjNv9KTgNwfXV_i2S-00yrKelpj08BqCajG1QHh3bqODDlZXybXUTjiorfcVTGEbLHessQE4KavBUjh6s8HiXjWoXhoyU4Gfepi8iSZ1IDg4S7OkH8sKUDQ6U7l9FWUhv-miTVq5qT_FcssotGh4hvV9BAcKyTgeAme9lxwkyX3801OLwQ61lMWZfR6l6HOf3QvV9MbwcOe_Gv6CcvpkDDOFN92Pu2qQx7ZuZseWWhhHCo-UUVFC598KC48SW9fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان رویداد آموزشی اربعین‌نگار
🔹
مکان: دانشکده رسانه فارس، خیابان انقلاب اسلامی، زیر پل کالج، کوچه سعیدی، مجازی: اسکای‌روم
🗓
تاریخ برگزاری: پنجشنبه ۸ مرداد ساعت: ۱۳ تا ۱۹
📰
سرفصل‌های کارگاهی: عکاسی خبری، روایت‌نویسی و ویدیوی موبایلی
⤴️
مزایا و فرصت‌ها: اعطای گواهی معتبر پایان دوره، انتشار آثار برتر شرکت‌کنندگان و اهدای جوایز ویژه به برگزیدگان
🙍‍♂️
ثبت‌نام و نذر فرهنگی:
https://tavana.news/auth/arbaeen-register
🙍‍♂️
عضویت در کانال اربعین‌نگار ۱۴۰۵ در پیام‌رسان ایتا
eitaa.com/arbaennegar1405
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/452910" target="_blank">📅 14:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452909">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFSL-QcUI0g4lyxQkb9-vdMbtDKlfNKZOWkgH4t6vqDFvRQKRsNSzMzlsoGDoBnd0CXc9HgTtygOYsOigkhhcXP9sZuXdmk30ebDjGTmMiF2HMCSHLu6DC4mvLlThPJhVmnckvTOPxUtzHiwxA22TjlRzxphuhdejAunvnV0o69iSEYW07szScOh74QEVPmwhuaGrvFvTaVART1ldZzTmhctXwcKYkPdtcdwrXftV_1CCyt-kh4KU6z0oeOj6PY-i21EsjW5Pp9P4cE5_4ZPY-JFwIIgWtKJIqvPp7d4yBY9g8ZbXN3oytco9QMjqDYBYqP5vB2tMQ9WzqwlFIEs3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاوره درمانی ۴۰۳۰ با تماس رایگان از عراق برای زوار اربعین
🔹️
سامانه ۴۰۳۰ به صورت رایگان و ۲۴ ساعته آماده مشاوره در زمینه‌ سلامت، تغذیه، لیست داروهای ممنوعه و معرفی نزدیک‌ترین موکب درمانی به زوار است.
🔹
زائران می توانند با شماره گیری 4030 بدون نیاز به پیش شماره از عراق به صورت رایگان، تلفنی تماس بگیرند و یا با شماره گیری  *4030# (ستاره چهل‌سی مربع) اطلاعات را به صورت پیامکی دریافت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/452909" target="_blank">📅 14:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452908">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=SCJfgpqU1Obadf0FeV0LG05CFcolY2dftmtFYmcONR2fjJMVa-tCXoo2ecbQoHnelNbXzfb8BhWgitlw6gSLcMxfvX1OknL7e8iSfyomraY501Axs5POkyanTzi_cJ4IHeddhWkWlJ-m_Zp175rZ1t7fEEnNWGIiRcWx2GCyTYXQsUgMNBFE70TjF03A4jVTeqh8xsi3tnPEe-2dPCQ02S2zb_qdYFs9Y0dPHMoipA2GKakLBHfG-Ry1FDg4itepqf36L-leLhdLiDAqTgasbRueq2DHcs1ARsY_DSHJqBy8zEcmpSlspufs4Wd5daQ0v-D3KljV9EqgiZp0kbHfbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=SCJfgpqU1Obadf0FeV0LG05CFcolY2dftmtFYmcONR2fjJMVa-tCXoo2ecbQoHnelNbXzfb8BhWgitlw6gSLcMxfvX1OknL7e8iSfyomraY501Axs5POkyanTzi_cJ4IHeddhWkWlJ-m_Zp175rZ1t7fEEnNWGIiRcWx2GCyTYXQsUgMNBFE70TjF03A4jVTeqh8xsi3tnPEe-2dPCQ02S2zb_qdYFs9Y0dPHMoipA2GKakLBHfG-Ry1FDg4itepqf36L-leLhdLiDAqTgasbRueq2DHcs1ARsY_DSHJqBy8zEcmpSlspufs4Wd5daQ0v-D3KljV9EqgiZp0kbHfbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
✨
✨
حسابتو طلایی کن
✨
✨
✨
‌
🟡
۶۶۶۶ سکه طلا برای ۳۳۳۳ نفر
و میلیاردها ریال جوایز نقدی دیگر ...
‌
✨
جشنواره بزرگ قرعه‌کشی حساب‌های قرض‌الحسنه بانک سپه
✨
‌
#بانک_سپه
#نخستین_بانک_ایرانی
‌
🌐
https://omidbank.ir
‌
🌐
https://banksepah.ir
‌
📲
@banksepahofficial</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/452908" target="_blank">📅 14:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452907">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/452907" target="_blank">📅 14:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452906">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تعویق سفر نتانیاهو به آمریکا
🔹
«تایمز آو اسرائیل» گزارش داد پرواز هواپیمای نتانیاهو به واشنگتن، بدون ذکر علت تأخیر به تعویق افتاد. @Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/452906" target="_blank">📅 14:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452904">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb14c46a0.mp4?token=qmX1zRTMMpEVfH_i_sjUlsh-ZqCKKu3GFSKAXTE3f3E2d2KKf1NbXZztbjyUJQVPHmahqpcDJ14zx7yEfZKBgiwQ12JY_cy-_7utpEeDbIyNIcwO5S702jADAbO0-FlBaSLYCSYIu5CrSFIJJVr3R1Rxmuvhj4HXRTuJDOWSdMEV5KOklgs1yov5z7npQyZxhHzDeY2YlriAxgBIgEOKfcAZ3EtBfi4eoAjBZQqBpzJd3UuBhQtifmID7AvD7UKsb46mfJ4eohQP7KyuoSPRJCtm06uf4got9h45Y0mzqPldiyc_ILeqRavp-VNtoNGU5SfIiURt1HpBAKs0G8z_4aZL-pGatHU5jkLm471_7OYUUuRPCPZ4AKFNJ8h-V8tZTYkHzGAvCo3pPO1AdciB0NKAgmPF38AHlKd-iLuwaHhkXHuxdGO0oGle34ZmHvhI_6cgVQFsWvu3erAn2Lw8SbFHQRakW2ozdAn05GlAlTpLIId7YRs-phFwuOjSNng2A8HENQy5NnO_AOTU0I6FhQ_f-ZAIYDNMg8pcmyFLYVsUbJ3oG7rpkqLLRGxF3AqqNFbD9w9OBW71ehv7wUXgMLA2LzebmmowvkGv8RtuejnNefpBlmd0aBXrEHxSlwhxu6e42JJCEzC_LDZB-DSZ2CcsrRDMJUzPBI7faerbwlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb14c46a0.mp4?token=qmX1zRTMMpEVfH_i_sjUlsh-ZqCKKu3GFSKAXTE3f3E2d2KKf1NbXZztbjyUJQVPHmahqpcDJ14zx7yEfZKBgiwQ12JY_cy-_7utpEeDbIyNIcwO5S702jADAbO0-FlBaSLYCSYIu5CrSFIJJVr3R1Rxmuvhj4HXRTuJDOWSdMEV5KOklgs1yov5z7npQyZxhHzDeY2YlriAxgBIgEOKfcAZ3EtBfi4eoAjBZQqBpzJd3UuBhQtifmID7AvD7UKsb46mfJ4eohQP7KyuoSPRJCtm06uf4got9h45Y0mzqPldiyc_ILeqRavp-VNtoNGU5SfIiURt1HpBAKs0G8z_4aZL-pGatHU5jkLm471_7OYUUuRPCPZ4AKFNJ8h-V8tZTYkHzGAvCo3pPO1AdciB0NKAgmPF38AHlKd-iLuwaHhkXHuxdGO0oGle34ZmHvhI_6cgVQFsWvu3erAn2Lw8SbFHQRakW2ozdAn05GlAlTpLIId7YRs-phFwuOjSNng2A8HENQy5NnO_AOTU0I6FhQ_f-ZAIYDNMg8pcmyFLYVsUbJ3oG7rpkqLLRGxF3AqqNFbD9w9OBW71ehv7wUXgMLA2LzebmmowvkGv8RtuejnNefpBlmd0aBXrEHxSlwhxu6e42JJCEzC_LDZB-DSZ2CcsrRDMJUzPBI7faerbwlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر: کتک‌ها را می‌خورم اما باج نمی‌دهم
🎙
رئیس فدراسیون کشتی:
🔹
در این چند سال کسی اگر به من بی‌احترامی کرده باشد امکان ندارد او را به کمیته انضباطی برده باشم اما هر کسی تو کار کشتی گذاشته باشد جلوی او می‌ایستم فرقی نمی‌کند معاون وزیر باشد یا کمیته ملی المپیک.
🔹
با شخص خودم کاری ندارم اما برخی‌ها باج می‌خواهند حالا مربی باشد یا هر کسی. من کتک‌ها را می‌خورم اما باج نمی‌دهم.
🔗
صحبت‌های دبیر را
در فارس بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/452904" target="_blank">📅 14:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452903">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
ارتش اردن مدعی شد که ۲ پهپاد را در آسمان این کشور ساقط کرده و خساراتی در پی نداشته است.  @Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/452903" target="_blank">📅 14:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452902">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea5c211d7.mp4?token=en1KU1s8klcLVHbDVMzXaPQxj0AKKCtj-et3p1C8YCKosGbETnveVnIMZU6RmtYYAw_7EFlt3oDkFR8w9uOOrvf3VLMs-Gaj6e2MTXL2PkxseXllJGBfNjDyLygGl_NPytZWlz1OwkSrhypzbkrThN9xWAzmZdiiNYtztCmHNR6p_E9Y-SC_hDCOswsatziefQAU83cxnbdLtS4kfGI1Rv9iq1OwyCPC6znAlyeJBskI77oMB2iOUMwgLR2IJQzj47dHQ9xJP4GWPPjgoCqw0cS8hJfByY3CStxJeNWhMolObbls_sgS9id6dmjhIQgvGmp_mZyLU5kDkOEyFHrczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea5c211d7.mp4?token=en1KU1s8klcLVHbDVMzXaPQxj0AKKCtj-et3p1C8YCKosGbETnveVnIMZU6RmtYYAw_7EFlt3oDkFR8w9uOOrvf3VLMs-Gaj6e2MTXL2PkxseXllJGBfNjDyLygGl_NPytZWlz1OwkSrhypzbkrThN9xWAzmZdiiNYtztCmHNR6p_E9Y-SC_hDCOswsatziefQAU83cxnbdLtS4kfGI1Rv9iq1OwyCPC6znAlyeJBskI77oMB2iOUMwgLR2IJQzj47dHQ9xJP4GWPPjgoCqw0cS8hJfByY3CStxJeNWhMolObbls_sgS9id6dmjhIQgvGmp_mZyLU5kDkOEyFHrczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از حملات پهپادی به مقر تروریست‌های تجزیه‌طلب در شمال اربیل خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/452902" target="_blank">📅 14:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452901">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGhmhhrNb1J37HHVKNU6xNJpT9Wodsm8Iy3g0du6Z-8kIhrde4klFDIqA4kvZxBI5OJfPQT-t4ZgnYGlmt1Cot0rJjw9Mh66SuVnImWkBLhzvUkvsU4uKYKFpNmxCBaHvV6LIEPFKzizhyJHNcnYaPNSXIvhJTRf12SA4siHSkN6V6kljINhYmLeEq7CDqczonfuWta_b_aHkdwoL0bGwg3nFXpisGkep5xLg1HullLnqv19rKa21XfSmXnK8IoA5bCw3uSwAWCzMKXqnVwDZ2D92axWN0EFPONGOPPlsXZCxrKrcw5nB16y9L2SW0YTAYO-OGOw5daKz2c8VfWjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خشم قلعه‌نویی در جام جهانی پیچید
🔹
شرایط نابرابری که آمریکا میزبان جام جهانی برای ایران بوجود آورده باعث اعتراض مجدد امیر قلعه‌نویی در نشست خبری امروز قبل از بازی بلژیک شد که نشریه تلگراف انگلیس در گزارشی به اعتراض سرمربی ایران به سکوت ۴۷ مربی دیگر جام جهانی…</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/452901" target="_blank">📅 14:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452900">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf17741d4.mp4?token=KaVE0eBWwpRzgqhx3X6pdI4WjiGrVceQQqXxQDuW_bbSEB-ssPpJWFQFKAqdmC1WCrQbc__SP43yMeDaM6a_6GKKCIrlCgfl8-KVvty7NI464iv-1wGws_3Jse8FBbOcwnWYzX3FRlF1uwaUdndy_xZ35LLCCaCE0eBaRneH1L-k43-c5tRy9ejE-T1n4hfyZxuZF9XdkYt1IAtem6gmzBFoOPCJE2qSbqLnyVYAx-TaA58wq5oT-se4MiTX8omxjM34JVLkjIOvD9uwpWyBFyeY-zkcop9N2-2P4ysM8M6FnNfDsTfhqYORz967k_WepS7yE5Yy9nNTAC8UzsPPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf17741d4.mp4?token=KaVE0eBWwpRzgqhx3X6pdI4WjiGrVceQQqXxQDuW_bbSEB-ssPpJWFQFKAqdmC1WCrQbc__SP43yMeDaM6a_6GKKCIrlCgfl8-KVvty7NI464iv-1wGws_3Jse8FBbOcwnWYzX3FRlF1uwaUdndy_xZ35LLCCaCE0eBaRneH1L-k43-c5tRy9ejE-T1n4hfyZxuZF9XdkYt1IAtem6gmzBFoOPCJE2qSbqLnyVYAx-TaA58wq5oT-se4MiTX8omxjM34JVLkjIOvD9uwpWyBFyeY-zkcop9N2-2P4ysM8M6FnNfDsTfhqYORz967k_WepS7yE5Yy9nNTAC8UzsPPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خارگ برای شما زیادی گرم است
🔹
انیمیشن لگویی خطاب به تروریست‌های آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/452900" target="_blank">📅 13:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452899">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57c07bae2.mp4?token=An29oQV3GgGlwj4XyIRgsZ0sGUyKeWu_wS1lbE2nwlCjSLaG3J7tXUcKFWdVW5jiXYF9cV2pPOUbO604uSJ5UhKqxblmqLLpr98xTq8gB3zzp1xcSyJEEMs9ERvRzMV1ROZvK4-yF0sKeboTYTJ9oUNpnNr6WteUidGvJqPv2Vt5V1aMRKeVlT8xTvjufV0WLtGgGyd33alY86CKwL2zlt_qfu3k8_Z4thX-eEgqed9zQj_lo4NMKd5xfFH6o2w88hPOhHWLNzYkn6OmLkYsgQ3YtKHp8Cxbe3daEIenPWRH5RJ6v_C0daXPeSms5j_Rxf4P5q1T_UbYKflWXogDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57c07bae2.mp4?token=An29oQV3GgGlwj4XyIRgsZ0sGUyKeWu_wS1lbE2nwlCjSLaG3J7tXUcKFWdVW5jiXYF9cV2pPOUbO604uSJ5UhKqxblmqLLpr98xTq8gB3zzp1xcSyJEEMs9ERvRzMV1ROZvK4-yF0sKeboTYTJ9oUNpnNr6WteUidGvJqPv2Vt5V1aMRKeVlT8xTvjufV0WLtGgGyd33alY86CKwL2zlt_qfu3k8_Z4thX-eEgqed9zQj_lo4NMKd5xfFH6o2w88hPOhHWLNzYkn6OmLkYsgQ3YtKHp8Cxbe3daEIenPWRH5RJ6v_C0daXPeSms5j_Rxf4P5q1T_UbYKflWXogDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در مورد شکایت از زیرمجموعه‌مان باید حساس‌تر و مسئولانه رفتار کنیم
🔹
اگر مردم نسبت به یک فرد در دستگاه قضا بی‌اعتماد بشوند، آثار خیلی بدی دارد.
🔹
اگر کسی از کارگزاران سطوح مختلف قوه‌قضائیه خلافی کرد، نباید به او رحم بکنیم. @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/452899" target="_blank">📅 13:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452898">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e51a5e67.mp4?token=GAV2dghyPaifv_G4rfrPSJh_wX8xdLtoLt3eegZKS_CC4iTML0wpRJB5ZgBb0f7rxqTc07qfaD7PjCRoMbvgL-fjy2Mttj2mjR4JJJ9h8pjg-4hU-v6INMu9jt8dVxLDl1RR-aXnDkM-QucO8EfOLLCr_wghOpgxIixZDtYvHdovluLUPcn4dbOauYt9rc6KXf7AdWXZ2JW0irC8kH2f1H9ILRommCaIZ3SlXma9w9eWwKojd9OZMmquFjYGOUTY_7dkdHq3MwBDH1wrmlzKZJsPP3TTRJXxe6ho4Riz5USF6ps8N8-neefKqb2wvcdNZ39xjRyUGc8fb4xBZnJ33A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e51a5e67.mp4?token=GAV2dghyPaifv_G4rfrPSJh_wX8xdLtoLt3eegZKS_CC4iTML0wpRJB5ZgBb0f7rxqTc07qfaD7PjCRoMbvgL-fjy2Mttj2mjR4JJJ9h8pjg-4hU-v6INMu9jt8dVxLDl1RR-aXnDkM-QucO8EfOLLCr_wghOpgxIixZDtYvHdovluLUPcn4dbOauYt9rc6KXf7AdWXZ2JW0irC8kH2f1H9ILRommCaIZ3SlXma9w9eWwKojd9OZMmquFjYGOUTY_7dkdHq3MwBDH1wrmlzKZJsPP3TTRJXxe6ho4Riz5USF6ps8N8-neefKqb2wvcdNZ39xjRyUGc8fb4xBZnJ33A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در هتل پارسیان تهران
🔹
سخنگوی آتش‌نشانی تهران: آتش‌سوزی در یک مجتمع اقامتی در هتل پارسیان در تقاطع بزرگراه چمران و خیابان ولیعصر باعث شده شعله‌ها به‌طور کامل این بخش را فرا بگیرد.
🔹
عملیات امداد و نجات همزمان با اطفای حریق در حال انجام است. آتش‌نشانان در قالب چند گروه عملیاتی وارد ساختمان شده‌اند و در حال کمک به افراد محبوس هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/452898" target="_blank">📅 13:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452897">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae297a55a3.mp4?token=mb_TJUb1qd3xgFGdoYO1bSFPPCAnyiBNsPjakUJg39hBY4s4UfHelNPHAF_IoQTcJgLNut5KvElj24mVdtw_NOLLScnE3bnH0_8PPcpSpZT0weVrFA_o-tpDFUcIiUe0yvBBDb_etHhgpdzOZBkPqwShS0yhcf4lvoUFEH5fPcBMAn8_wdqT6wOcb0fp1Lsex-2nAnIwWhmV7lpBHDNTvUzHc8NT0-RLCe_BfYyTYHpgHLsl9CdZLnrmmoUciFl7RYR7Yg1XB2ws4UA4LfvY0qkV1cyPXGOb4vtU_2mN242LvadiBRG7ZOlIPH2R9efg3mygN0QE12sCa3t0OQ8G9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae297a55a3.mp4?token=mb_TJUb1qd3xgFGdoYO1bSFPPCAnyiBNsPjakUJg39hBY4s4UfHelNPHAF_IoQTcJgLNut5KvElj24mVdtw_NOLLScnE3bnH0_8PPcpSpZT0weVrFA_o-tpDFUcIiUe0yvBBDb_etHhgpdzOZBkPqwShS0yhcf4lvoUFEH5fPcBMAn8_wdqT6wOcb0fp1Lsex-2nAnIwWhmV7lpBHDNTvUzHc8NT0-RLCe_BfYyTYHpgHLsl9CdZLnrmmoUciFl7RYR7Yg1XB2ws4UA4LfvY0qkV1cyPXGOb4vtU_2mN242LvadiBRG7ZOlIPH2R9efg3mygN0QE12sCa3t0OQ8G9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای: اگر کسی در قوه‌قضائیه دچار فساد بشود، در برخورد با او رحم نخواهیم داشت
🔹
اعتقاد راسخ ما این است که هر مسئولی باید در قبال زیرمجموعهٔ خود نهایت صیانت را داشته باشد. باید نظارت‌ها و هشدار‌ها و تذکرات به‌قدری وسیع و عمیق و سازمان‌یافته باشد که اساساً…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/452897" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452896">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG3rc37O3b_Cqvz1O2Ik7mEdK4zMYtettmPyf-7IFzab3JJXAagMwEIbBrqAEiUJD45tH_KhfWj7l4gSRWlPD7nOGDkTpanIzSMvyqlUFh592HSFxwK8XhJGDhSzJjl-XyXhiHr2MHIvyenn37U3Qs0s-9Er4u230tUQ8iOa5tlX7WlUaOSVzvlfihHDmgPlRaatRLcUhn0pWuvrq__tZ2we774ZLea0djmJmWl-boB0oxin6PMy84lGOCm_v6HPzNqEWpB9R7v8VQTkOOd4qvNyMRFLN63ZS6pQcLbStyqxoKGjLGM5ED1i3JDvx-h6EPmvbLGIA4CWJij8jZhUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نتانیاهو در طول حضورش در آمریکا بازداشت نخواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452896" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452895">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3f8067ef8.mp4?token=UOy3qgL4wQiNhR4nZ53L2na0PpSSxVVmekFVajMWzKvCJcRfNqNS-h9hTjQEQY2y1a1bW15zdcLraO49UdrMEOA6Z2pDtSA_4T2ubgFB0TfMLHnxQMIwgID2sL8KQc6igMwjUvw-E8XILOKaHzhbVNfCaYRBmrqhkTGBxgPWiyRAWCCWwhUWM5rk_7WPsnj_S9gZssC7kpAnfvn8N78lhA1CzezLrmnYuUGChq1jduJtLSP6NsQrnZgfrUcXjpFYXogShZy_jBeXIIPQe-F4bp2s2CjQ_FnChVBwf6FnZcPD5OP-1uoOS3AZDmd9D7XIdBapxaIwyAr30OuZugKc2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3f8067ef8.mp4?token=UOy3qgL4wQiNhR4nZ53L2na0PpSSxVVmekFVajMWzKvCJcRfNqNS-h9hTjQEQY2y1a1bW15zdcLraO49UdrMEOA6Z2pDtSA_4T2ubgFB0TfMLHnxQMIwgID2sL8KQc6igMwjUvw-E8XILOKaHzhbVNfCaYRBmrqhkTGBxgPWiyRAWCCWwhUWM5rk_7WPsnj_S9gZssC7kpAnfvn8N78lhA1CzezLrmnYuUGChq1jduJtLSP6NsQrnZgfrUcXjpFYXogShZy_jBeXIIPQe-F4bp2s2CjQ_FnChVBwf6FnZcPD5OP-1uoOS3AZDmd9D7XIdBapxaIwyAr30OuZugKc2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فتاح، اولین مهمان اتاق گفت‌وگوی جدید خبرگزاری فارس
🔹
رئیس ستاد اجرایی فرمان امام (ره) امروز در خبرگزاری فارس حضور یافت و علاوه‌بر گفت‌وگو در جمع مدیران خبرگزاری، در استودیو و اتاق گفت‌وگوی جدید فارس خاطراتی از رهبر انقلاب گفت که به‌زودی منتشر می‌شود.  @Farsna…</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/452895" target="_blank">📅 13:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452894">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
ارتش اسرائیل مدعی انهدام ۲ پهپاد در مرز اردن شد. گزارشی درباره منشأ این پهپادها منتشر نشده است.  @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/452894" target="_blank">📅 13:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452893">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmOwDE4IPlJqj3eRtuF5QgUIWGheEowoTgG2frlMHlBBXKgrOMjXubDzLhUnygrRllO0CxYyngQl9R4udEmv_TLh1g_1HCvYm06-b9LXOQidrciR_IEeooI2WJGP6t6FM2ndrohxdFb4rVhawNEnE23c5Dcg61YP0JPZftdUMK3A-hFz9ozDIhCTH9TQ9DhP-DhdcP4aj7Kf8cCynNYkXvTw38cpvV-tvIG_N9KOcxFFI39Nd21IOAGE3SnGv4WDIyKYcVAHcBzdRMy_mNZCCSSOeH8K_xr27iC4d178XCjDhW9DQg6G3RNOeFvY2c2hp65B9vNIJNHtMwJ_94Aa4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ارتقای ظرفیت بانک صادرات ایران در اعطای تسهیلات/ وصول ۸۴ همت از معوقات بانکی در سال ۱۴۰۴
🔹
بانک صادرات ایران با هدف افزایش توانمندی در اعطای تسهیلات به مشتریان، فرآیند وصول مطالبات را با شتاب بیشتری پی گرفت و در سال ۱۴۰۴ بیش از ۸۴ همت از پرونده‌های معوق را تعیین تکلیف کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/452893" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452892">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BElSk3yfA_yXljL630nAKfbRn3kzF9zAOPoVYb6owf5E0bFsOGsYYrEPN4802ekZOlRJ7Ds_wx0XGQA84KiJyw9aDhBcG8gSaMgtt1w063KoURnoYbuvmtG6PAh8gpHxX3W63xy5tokGsGta2sTM8ZvlXxW3W-G7z4AZj_3Z6X67dbjtFDkUI760gDWwuVQAP8xzmHoc0vyU0jTfQHu4aKM0I_C2JNfv5iKYmMGqbrga9Hx17V3g8R02dgf6Cca4R5xLIefYx5gzpWdoHfExFXYiUnZed27YTCxO0F9iGHMnoRXYBdBAYane2sb6XeewFsUa8fF5Jp8_KPoXiuY-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
۱۰ پروژه مس ایران در میان ۵۱ پروژه توسعه‌ای مس جهان
🔻
شرکت ملی صنایع مس ایران با در اختیار داشتن ۱۰ پروژه از مجموع ۵۱ پروژه توسعه‌ای در حال احداث صنعت مس جهان، در صدر شرکت‌های جهان از نظر تعداد پروژه‌های توسعه‌ای قرار دارد؛ جایگاهی که با قرار گرفتن تمامی پروژه‌های توسعه‌ای ایران در سطح اطمینان «Committed»، کشور را در رتبه نخست جهان از نظر ظرفیت پروژه‌های قطعی توسعه مس قرار داده است.
🔹
دکتر غلامرضا ملاطاهری، معاون طرح و برنامه‌ریزی راهبردی شرکت ملی صنایع مس ایران، در جریان مجمع عمومی فوق‌العاده این شرکت با تشریح جایگاه صنعت مس ایران در عرصه جهانی گفت: براساس آخرین ارزیابی‌ها، مجموع پروژه‌های توسعه‌ای صنعت مس جهان در سال ۲۰۲۶ شامل ۵۱ پروژه در حال احداث با ظرفیت مجموع ۷میلیون تن مس محتوی است که ۱۰ پروژه از این مجموعه متعلق به شرکت ملی صنایع مس ایران است.
◀️
ادامه خبر در مس‌پرس:
https://mespress.ir/x6S7
#در_مدار_آینده
#مس_ایران
#فملی
@mespress_ir</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/452892" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452891">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/452891" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452890">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0151cde69f.mp4?token=Glybqjs-vakqvuxzHfIdD_067k2jE-Kuyb1mHiUaggbOO_uvNuuuxEqNBzumvLC3FLxf1dmTTlJ9FUshg71ap2bNJD0hIhxuLcmhx5TOWGJrsJnQEkqNImt3vAbx-wi67zt8uFDfNBBH-ry0olbO06g0gvI4eV8ioI2zyZmDohyVvlj_jP4gT4idxrIJ-qcX1ZCahnuSVgfQSQXw69GiseDimD2VdyEoSIK0S3cJKDssm5f3zc3kNQ60k7lklYPEELdge_cyVaPl08Rid0Cuwzd_qgjSjb-p3k4UDDujv2ByqgRxyRBttjJHzUXkl6EJ4EU1_BmCORPJXXTIOFcsew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0151cde69f.mp4?token=Glybqjs-vakqvuxzHfIdD_067k2jE-Kuyb1mHiUaggbOO_uvNuuuxEqNBzumvLC3FLxf1dmTTlJ9FUshg71ap2bNJD0hIhxuLcmhx5TOWGJrsJnQEkqNImt3vAbx-wi67zt8uFDfNBBH-ry0olbO06g0gvI4eV8ioI2zyZmDohyVvlj_jP4gT4idxrIJ-qcX1ZCahnuSVgfQSQXw69GiseDimD2VdyEoSIK0S3cJKDssm5f3zc3kNQ60k7lklYPEELdge_cyVaPl08Rid0Cuwzd_qgjSjb-p3k4UDDujv2ByqgRxyRBttjJHzUXkl6EJ4EU1_BmCORPJXXTIOFcsew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ دستگیری باند سرقت موتورسیکلت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/452890" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452889">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Blpqo4POVBa_E-npVU6HgBLd9fSmAqeCe48obXrlJA_WoDqj92JnVfYY2ZnGiksnaWLM1rXnXFz0mhkXla2c3DR6Yk1oH68tGR07KXg1b4K7yBNI_gxbqogsjjKq2yO6jS9O3MrhgPoKbq35SFtt5Y5hamk5tvEE6j4ljAUfCCEfd0SEjO5aL-aGSNbsUQNGkU1vUEH8BQakPDK5kk4i1qET6n81xaae8gINC1XcBeLXBMA1I9CIqtsLUWaOxcnY50iqEkrRM4I7Jo4rOnAAKjd5mLFTzo0AGtgQT-RKQlSYpB1BfRh8AgsEWd2MKNhYAH7NQ58rQVQFhRXyjxBEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۵۰ هزار واحدی به ۵ میلیون و ۵۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/452889" target="_blank">📅 12:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452888">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e85XE_g8ml58aeSkF_McIokf4vUzc_jrIIFNUlH-y3nztD_bRSM-NHGfZkdbmgXx_KXxSbFF47DBsItLdLMSmM25X4N4RBPT5dlwAw7vb12KWs8WAkGrpx2QbMJKVwHuqkRRY6mXTYZrjV1qm9VfKRerrBxzywlVAtVsmbq7v8ELjrpbcLx3tqSoGVsAMAhF_AuU_9RCbxk6hDJm_0JV73ItpaUvtyD-mjtstEgEGv6VVQNLcn8qlebSc-bT-I0AMZyzrvNWraNgfHWpyZ6rLpC4LbiBuLysatpfuvF6y3dEfgeqseUGpmYqw1ErXRA-W1nNJUVPKE7Pg-qTeQp7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خروج اولین زائران حسینی از مرز سومار به عراق  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/452888" target="_blank">📅 12:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452887">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در خوزستان
🔹
فرمانداری امیدیهٔ خوزستان: درپی انهدام مهمات عمل‌نکرده در شهرستان، احتمال شنیدن صدای انفجار در امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/452887" target="_blank">📅 12:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452885">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d96a362192.mp4?token=BuCKqNJnARzG0lJKWB9JtkmjcOt71FAMRg_o9_nZe--kkcJSk448rZZXQgR7cwcCuRRefR060AUGiA6-eiwLhKeQWTsDOW85J1abrFUsRHPsPT9KKoZhJ7ZOV_vN7hv9NX60jk3WHrVqzpHEM3S0wcFP94bxY2s4PwUKWbzhbnHr4bGcipv4-UMzM2Py-MKU7u_GHAXasrXaRbkxpemrpjI5M1iYzqLBKBAZBfquE5wxNYEHQYWaToAqiV_qyeg9gSZLkIjfdlPvwO-U91mlwftmGzdrJ00qoArtEy4_D029xnmY-mScTqwFmE3uD2HYbNFgEJnO9Gm5-L_oqKI9Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d96a362192.mp4?token=BuCKqNJnARzG0lJKWB9JtkmjcOt71FAMRg_o9_nZe--kkcJSk448rZZXQgR7cwcCuRRefR060AUGiA6-eiwLhKeQWTsDOW85J1abrFUsRHPsPT9KKoZhJ7ZOV_vN7hv9NX60jk3WHrVqzpHEM3S0wcFP94bxY2s4PwUKWbzhbnHr4bGcipv4-UMzM2Py-MKU7u_GHAXasrXaRbkxpemrpjI5M1iYzqLBKBAZBfquE5wxNYEHQYWaToAqiV_qyeg9gSZLkIjfdlPvwO-U91mlwftmGzdrJ00qoArtEy4_D029xnmY-mScTqwFmE3uD2HYbNFgEJnO9Gm5-L_oqKI9Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیاده‌روی عشاق اباعبدالله(ع) در مناطق جنوبی عراق
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/452885" target="_blank">📅 12:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452880">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxyrq5p2-sNsfJVhwj0DqN9LtqyJ9zQKLQZGOiMvjky7IiABF8_RaDxASGOUZrtzJWsVhQsIxCcdZVFj8acHJwEf1axHeOlBTmj2vy07VPp7p1zRcfHOyNsH5ZAy4u4M0OgtIH4mTm53TUQ5X6l_xNYISKvUlQMKE3CNCodz1Yo110i2QezfHIYN9XJIjj2LYGv6cidm2LGnlh-jQi4npAPuYCJlCL0WPiCd8pKyZNMU-PUjv2Dp0MDLfT1gCcm9mT0aE2LtbDCvn7JJ_KB0RM6sR1eQoId6a3AwX52GIPn7xD2lCk2H-R8pZ4GxlnhAK7POTuPgT915wczDJHay5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای: اگر کسی در قوه‌قضائیه دچار فساد بشود، در برخورد با او رحم نخواهیم داشت
🔹
اعتقاد راسخ ما این است که هر مسئولی باید در قبال زیرمجموعهٔ خود نهایت صیانت را داشته باشد. باید نظارت‌ها و هشدار‌ها و تذکرات به‌قدری وسیع و عمیق و سازمان‌یافته باشد که اساساً امکان حرکت به‌سمت فساد برای یک مسئول و نیروی یک نهاد حکومتی و دولتی وجود نداشته باشد.
🔹
چنانچه باوجود تمام این نظارت‌ها و هشدارها، فردی در درون قوه قضائیه یا بیرون از آن مرتکب فساد شد، فی‌المثل رشوه‌ای دریافت کرد یا آلوده به سایر مفاسد شد، مطمئن باشد که هیچگونه ارفاق و اغماضی در قبال او وجود نخواهد داشت.
🔹
ترحم به چنین فردی، در درجهٔ اول، ظلم به خود او و دستگاه متبوع او و در درجهٔ بعدی، ظلم به مردم است و ما هرگز چنین نمی‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/452880" target="_blank">📅 11:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452879">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e21ed4d2f.mp4?token=QS2WSyDGDwP3T5OV8UwxK2fVpMVTM2RJrLYKPCiuSABZDbxUjfC-b5wfmqX5IGEReSb1R22jDkyA1DF-aLdpqdD58QmXrz-5L_MDkA-Jj3NvJIueI1NCAxe5-xgmQUKXYsfcbZl7zV2kKlq3xU-JuIMpRVeLdcEbjNsbu1qkkOqocBNvbb5aNqaiLqsQJzrSJUj070Mf0iKRnea8gsLmupneP21dTUDtYX9gkZQKfO08ezsNc6d82bHKzJfr0BuJGpKIHJAvv3Uy7cG-FyzempqPyd41MLKg7_MzLKjLgDJq2C7hLXpOvtQxMUpWUjVcKhAvxGhsth7u-CbHpHVtRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e21ed4d2f.mp4?token=QS2WSyDGDwP3T5OV8UwxK2fVpMVTM2RJrLYKPCiuSABZDbxUjfC-b5wfmqX5IGEReSb1R22jDkyA1DF-aLdpqdD58QmXrz-5L_MDkA-Jj3NvJIueI1NCAxe5-xgmQUKXYsfcbZl7zV2kKlq3xU-JuIMpRVeLdcEbjNsbu1qkkOqocBNvbb5aNqaiLqsQJzrSJUj070Mf0iKRnea8gsLmupneP21dTUDtYX9gkZQKfO08ezsNc6d82bHKzJfr0BuJGpKIHJAvv3Uy7cG-FyzempqPyd41MLKg7_MzLKjLgDJq2C7hLXpOvtQxMUpWUjVcKhAvxGhsth7u-CbHpHVtRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا در ۲۰ روز کل تفاهم‌نامه را نقض کرد؛ ما از اصول امنیت ملی‌مان کوتاه نخواهیم آمد.  @Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/452879" target="_blank">📅 11:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452878">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d6db134c.mp4?token=Kj_CMVfT-3zv2CpInQG11HGUrOgFvDLZ3WQlpb3UelMggDpDOvgU7e3j1FnVtE6DorOYGm17Hkbyoq0XEWVhismoUfzg1uERx_md0fn_Db6vNvmJqjWqxu2YFjXLkQA6QPXgtRZu_Z-ljaP69bmgDdyDsLGGCmbPgq5_5Y6EKUhw60qrlHb-DEUV4-9Ngkba6DPnJLs_qQ6UJcwljWOOLc7_KcYkk2ZJWeEdwyVfmBbAaR5B9zBbU5fZAatIaGRnzWRZgacJOLH2Ji8akAUaM76Hoxzv36fBGtiIAu0AcvtlkyENOKwrFUK2HM6ifMuV3PqpxOqz7VCfRKMqWZUtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d6db134c.mp4?token=Kj_CMVfT-3zv2CpInQG11HGUrOgFvDLZ3WQlpb3UelMggDpDOvgU7e3j1FnVtE6DorOYGm17Hkbyoq0XEWVhismoUfzg1uERx_md0fn_Db6vNvmJqjWqxu2YFjXLkQA6QPXgtRZu_Z-ljaP69bmgDdyDsLGGCmbPgq5_5Y6EKUhw60qrlHb-DEUV4-9Ngkba6DPnJLs_qQ6UJcwljWOOLc7_KcYkk2ZJWeEdwyVfmBbAaR5B9zBbU5fZAatIaGRnzWRZgacJOLH2Ji8akAUaM76Hoxzv36fBGtiIAu0AcvtlkyENOKwrFUK2HM6ifMuV3PqpxOqz7VCfRKMqWZUtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: جمعه و شنبه چند دور مذاکره بین ایران و عمان برای مدیریت تنگهٔ هرمز برگزار شد که مذاکرات خوبی بود؛ وضعیت تردد در تنگهٔ هرمز هیچ تغییری نکرده است.  @Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/452878" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452877">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b543b1687.mp4?token=H7OLdT4VUvSAg7vCXrfqMqFor-R8bSgsFuEiGRFiWJV3lWl3nVnukh3plxT7mU6lHzPtzMZ_b_7GaJMWX1502F6yfPyjZqgigsP3yuoaj3N7Powl3x0oBNRRT2246mDuA-ASTjna3frvjRp9DHu1MrnFRAxWZK8F5xOE-RZWc5iUziazx0OajQV6pGXX0a4pbWehb-nfNtJPWA1V94qG_lYKL1wOS14imlnyD4bzbK5Nq6f_7_LDXxVK3ahFldO1elYr4Xd8pG2OQ2U7Uaq8nrlsIdRpZfG7GNIb3wuMydfuRYvVuDZeZesLTTbebKxw_H_yTjB4E-8KZYlvW7OoVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b543b1687.mp4?token=H7OLdT4VUvSAg7vCXrfqMqFor-R8bSgsFuEiGRFiWJV3lWl3nVnukh3plxT7mU6lHzPtzMZ_b_7GaJMWX1502F6yfPyjZqgigsP3yuoaj3N7Powl3x0oBNRRT2246mDuA-ASTjna3frvjRp9DHu1MrnFRAxWZK8F5xOE-RZWc5iUziazx0OajQV6pGXX0a4pbWehb-nfNtJPWA1V94qG_lYKL1wOS14imlnyD4bzbK5Nq6f_7_LDXxVK3ahFldO1elYr4Xd8pG2OQ2U7Uaq8nrlsIdRpZfG7GNIb3wuMydfuRYvVuDZeZesLTTbebKxw_H_yTjB4E-8KZYlvW7OoVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: فرانسه با پوشش سفارتخانه و به‌بهانهٔ ارتباط با جامعهٔ مدنی در امور داخلی ما دخالت کرده و باید عذرخواهی کند
🔹
دیروز هم سفیر فرانسه به وزارت خارجه احضار شد و صراحتاً اعلام کردیم که این کشور باید از چنین مداخلاتی در امور ایران با عنوان‌های…</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/452877" target="_blank">📅 11:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452876">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
ارتش اسرائیل مدعی انهدام ۲ پهپاد در مرز اردن شد. گزارشی درباره منشأ این پهپادها منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/452876" target="_blank">📅 11:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452875">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0f6ac7d6.mp4?token=EWAo79GT6DGHSK898mQs-u2KVFwynQ7dyr5hOXcuob6rOp9SpNvu-XtaR4FQM4wdFaO5C6EC1G29cyGyYlOCQn2BmRt7VrvVgEsb0pi8FSSUJmnJNz_A-DAknDjzvFtNhFlFoQyCz-lhZMqOBuP-JXEJjymVMx0Kbz3zC-cwr6FvwTxdfyq73aZMRUzx_q4gLX324IM4JkZU_ZA-yq9tN9Sv_V07kPnXBcm53e9IbT-ERylsNhiA_1MnunjruyeMBDsQ8nqT18OQFtFx5jGFKpDQywNmCFWWvgACzO9ZZ975E0LqR1CEBTj84NVuR1xuy2Pi1kcBCfT4a7JEJ7GxUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0f6ac7d6.mp4?token=EWAo79GT6DGHSK898mQs-u2KVFwynQ7dyr5hOXcuob6rOp9SpNvu-XtaR4FQM4wdFaO5C6EC1G29cyGyYlOCQn2BmRt7VrvVgEsb0pi8FSSUJmnJNz_A-DAknDjzvFtNhFlFoQyCz-lhZMqOBuP-JXEJjymVMx0Kbz3zC-cwr6FvwTxdfyq73aZMRUzx_q4gLX324IM4JkZU_ZA-yq9tN9Sv_V07kPnXBcm53e9IbT-ERylsNhiA_1MnunjruyeMBDsQ8nqT18OQFtFx5jGFKpDQywNmCFWWvgACzO9ZZ975E0LqR1CEBTj84NVuR1xuy2Pi1kcBCfT4a7JEJ7GxUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: بزرگترهای زلنسکی مراقب باشند که پیامدهای اقداماتش دامن‌گیرشان نشود
🔹
رژیم اوکراین از ۴ سال پیش کشورش را در حد ابزار دعوای ژئوپولیتیک بین قدرت‌ها پایین آورد و به‌جای نجات کشورش از جنگی که بر شرق اروپا تحمیل کرده، مدام دیگران را شماتت کرده…</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/452875" target="_blank">📅 11:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452874">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30b0f07414.mp4?token=HSUyG79PYUQNyLfxJOQXISu8u1UEmYpVtG3IPHzUymrV5gnnsfOwnqF5oeQ22UzzGO_moQvfNEKEuxHbD8XS3MUh2ujPQQ_YzNuh3JuJESMnwFGU0tPrOAyg31LwjQy7GZi5FnsatkDllvwXbDCS7YT1N9qW8YFuBmd204iy--FkiqxpD2UuIksQ0Nd215QQ38-A5BrymmpOVxQpzyK3FgoNIHeoN00JvYG4cmKrsmjHupmNl2EOwOY4p6EF1bmuJrxD6DD926M6MmPAOlrU7RmpjPg9RT1RFO-0SXDv61fw9TT0sVfBvdYWpdpLtfHYuCi0DZ87zMkpQqmrVLxdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30b0f07414.mp4?token=HSUyG79PYUQNyLfxJOQXISu8u1UEmYpVtG3IPHzUymrV5gnnsfOwnqF5oeQ22UzzGO_moQvfNEKEuxHbD8XS3MUh2ujPQQ_YzNuh3JuJESMnwFGU0tPrOAyg31LwjQy7GZi5FnsatkDllvwXbDCS7YT1N9qW8YFuBmd204iy--FkiqxpD2UuIksQ0Nd215QQ38-A5BrymmpOVxQpzyK3FgoNIHeoN00JvYG4cmKrsmjHupmNl2EOwOY4p6EF1bmuJrxD6DD926M6MmPAOlrU7RmpjPg9RT1RFO-0SXDv61fw9TT0sVfBvdYWpdpLtfHYuCi0DZ87zMkpQqmrVLxdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ کارخانه‌های اسرائیل در نزدیک غزه
🔹
آتش‌سوزی مهیبی صبح امروز منطقهٔ صنعتی شهرک صهیونیستی سدیروت در شمال غزه را فراگرفت و با سرایت شعله‌ها به چندین کارخانه مجاور، خسارات سنگینی به تاسیسات تولیدی این منطقه وارد کرد.
🔹
برخی منابع محلی احتمال می‌دهند که این حریق بر اثر اصابت ترکش‌های موشکی از نوار غزه رخ داده باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/452874" target="_blank">📅 11:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452873">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRaThNNDMoDrbts0ME7KekQrCWJ7j8wVgefNSO6YSVqmWTRyDgk_ZemGoH7Lfb7ZBNL3BKAPEsE4J69dssJDJsdZALZ8MiT4CfPqxxp-lC1Fit6uLKiNjO8MNy1F9Qpdq82AP5ld1pIZRyu-RkCxzB6lGrx1vW1nZmQMtIcHdivtyyyE9YuV--sVmcPvNbMJ3MWJ-rkGyREFP_VyPt6be1gT5mbM4kUzBsdTfxY7UWL8K6ty8sGrAQM7Pj9hE08hff4iuVMhLHMuiFMmaOCmOz9XTHDwVIm9VlruGpwl7PSeq5TRyz6BfAiOpRpuBV-4XJniYERZ88ornSnxBrdIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجمع هلدینگ خلیج فارس لغو شد
🔹
مجمع عادی هلدینگ خلیج فارس که بنا بود امروز هیئت‌مدیرهٔ جدید را معرفی کند، به‌دلیل آنچه عدم اعلام حضور نمایندگان سهام عدالت عنوان شد، از نصاب افتاد و لغو شد.
🔸
این درحالی‌ست که نمایندگان سهام عدالت ساعتی قبل در مجمع فوق‌العادهٔ هلدینگ برای افزایش سرمایه حاضر شده و رای داده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/452873" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452872">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f262d61d8.mp4?token=OSaDtDBkSfn1-edeofTQZrbT8T-XshuzgdiDVWnhtsTZCQa-QKgusj8LGG4OSJvwyKv31KATtnA0w8JQTG3UkcPVbfbEq8Y08rRKVTFF4H_R8rvgp3D3QEi3-VePFx63qjnvI3MLDhxf3-bfC6eZxIeymF0mdWWvbQm2NFRCghYpgVpbOWoHcoLfJ8LdsSVjkJcw3EYsHKUEeV6NfC-tArMCDZd5DudEppBEussahpZTiUD6dfJ0dLsr-nAXFamtsGQfih-gx8F5kNBUFjiTRJTIajfJ7nffbdDGCJEkg7JaILof_76W4eKedslg1enwbpI-K8fwb8VvIrx-8aLwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f262d61d8.mp4?token=OSaDtDBkSfn1-edeofTQZrbT8T-XshuzgdiDVWnhtsTZCQa-QKgusj8LGG4OSJvwyKv31KATtnA0w8JQTG3UkcPVbfbEq8Y08rRKVTFF4H_R8rvgp3D3QEi3-VePFx63qjnvI3MLDhxf3-bfC6eZxIeymF0mdWWvbQm2NFRCghYpgVpbOWoHcoLfJ8LdsSVjkJcw3EYsHKUEeV6NfC-tArMCDZd5DudEppBEussahpZTiUD6dfJ0dLsr-nAXFamtsGQfih-gx8F5kNBUFjiTRJTIajfJ7nffbdDGCJEkg7JaILof_76W4eKedslg1enwbpI-K8fwb8VvIrx-8aLwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا می‌خواست در ۳ روز ایران را تسلیم کند اما حالا بعداز ۵ ماه در باتلاق خودساخته گیر کرده
🔹
تصمیم‌گیری دربارهٔ منافع ملی کشور معادله‌ای چندمجهولی است که در یک روند مشخص با مشارکت همهٔ دستگاه‌های تصمیم‌گیر انجام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/452872" target="_blank">📅 11:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452871">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op1kY1Fo5fJL_lvYxconhmaDL_HoiNLBwWiAvlYtEhbdJINJIbdMocMloNqDm201ckKzRF5LkCx_SRALSlgYjYPccWxTVDW16WE1m7Upf5eF8D1OycDgA2VEKjdMsj7TmM0aoKIpR9peFxhCbX35N8zs8v83h-garpOcGsD3aVwp6oKuFloHABZ2o3FAxGHHpsGMsicOle9ZlRSanJdx9NGN06hgwzYviKMXaAhZS13iAbRB3HelJZp6V4HpWQ8bpqe67lMtiYzZtXDBoCcSgy1ITcUfm8mkv_3uyEF8cg6LSw7KLuWtnKxFSyoFZVNC9vIoqEM1m5rUlNmJ5GiTLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ مسیر ویژه برای زیارت مرقد رهبر شهید ایجاد شد
🔹
با تغییرات جدید و گشوده‌شدن رواق دارالذکر به روی زائران ۴ مسیر ویژه زیارت مرقد رهبر شهید در حرم رضوی ایجاد شد.
🔹
در مسیر نخست، زائران آقا از صحن آزادی وارد رواق دارالسرور شده و پس از عبور به روضۀ منوره مشرف می‌شوند و در ادامه از مسیر دارالعزه به رواق دارالذکر هدایت خواهند شد.
🔹
مسیر دوم نیز آقایان از طریق مسجد گوهرشاد و شبستان گرم، به رواق دارالعزه و سپس رواق دارالذکر هدایت می‌شوند.
🔹
برای بانوان هم زائران از صحن بعثت وارد رواق دارالعباده شده و سپس از طریق رواق دارالزهد به رواق دارالذکر مشرف می‌شوند.
🔹
مسیر دوم بانوان نیز از طریق مسجد گوهرشاد، شبستان گرم و سپس رواق دارالزهد، به رواق دارالذکر ختم می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/452871" target="_blank">📅 11:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452870">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=czy7XaZwxDIv-6CrgV_2pw4DWg5DK9bWCzyuADwGcgqqHyPao4aM3OW19DUsWL5-Rnwe0JlHBTTylaenkUJCvYoHVN27hlz38oSqaxQu_xIeTEj9HR9k3Q2k7qs4-NAFjQP3-Xu7gVZkDwgIC1IF3uMdnXYzs05VRqJfB6eAvk8b9Te1sai36_JZIRoCFM1xPwjpWNxM_VuKYo0Ycg0Tm_i6o70zwzjajYd-KfKjFh7afWSR4e0EwOH9HrhU4uZ1lRjGLOXVx75MxM8WfRappyRUu42W9JLmWYtNxCVMSWDg4e7YriVfB5W0IbLjaFv-8nK0QZEkHDmjXgNicFH_2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=czy7XaZwxDIv-6CrgV_2pw4DWg5DK9bWCzyuADwGcgqqHyPao4aM3OW19DUsWL5-Rnwe0JlHBTTylaenkUJCvYoHVN27hlz38oSqaxQu_xIeTEj9HR9k3Q2k7qs4-NAFjQP3-Xu7gVZkDwgIC1IF3uMdnXYzs05VRqJfB6eAvk8b9Te1sai36_JZIRoCFM1xPwjpWNxM_VuKYo0Ycg0Tm_i6o70zwzjajYd-KfKjFh7afWSR4e0EwOH9HrhU4uZ1lRjGLOXVx75MxM8WfRappyRUu42W9JLmWYtNxCVMSWDg4e7YriVfB5W0IbLjaFv-8nK0QZEkHDmjXgNicFH_2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه خطاب به اتحادیهٔ اروپا: شما که هرازچندگاهی به بهانهٔ حقوق بشر بیانیه‌ای علیه ایران صادر می‌کنید! آیا کودکان میناب ایرانی نبودند؟!  @Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/452870" target="_blank">📅 11:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452869">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da97f47adf.mp4?token=EH_USHbJQUsyLp1zXwZWQe9_awZIbZmkDtVvHZ_bSuu1N-UCpSs6g_OFaBP9yC0ejQJfs0re8CFm0h1s_ySKr7pB5VKlEDdqMGRvSFO5IC3MCCft-coghmPumHQLxBH0zDwXqWEssZeCZiojTmJut0KV7g6XlXy5xJ7VSVisuogJ6Ie0Y1mAjhta7ldUQSv552vGhtkRpxNb2sGrqut1zl8scFeSKl-Fpgxx5ZXVM9UDLK973YZAiJgzZU78gwOhTC2RIJCKONy9_8ozq74uFzLEUQYJapOGS-F3o3R1zB56loR7R8osyQ_FLfKMoOqOz_Ze8aJC8TK5kJJkeu0rGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da97f47adf.mp4?token=EH_USHbJQUsyLp1zXwZWQe9_awZIbZmkDtVvHZ_bSuu1N-UCpSs6g_OFaBP9yC0ejQJfs0re8CFm0h1s_ySKr7pB5VKlEDdqMGRvSFO5IC3MCCft-coghmPumHQLxBH0zDwXqWEssZeCZiojTmJut0KV7g6XlXy5xJ7VSVisuogJ6Ie0Y1mAjhta7ldUQSv552vGhtkRpxNb2sGrqut1zl8scFeSKl-Fpgxx5ZXVM9UDLK973YZAiJgzZU78gwOhTC2RIJCKONy9_8ozq74uFzLEUQYJapOGS-F3o3R1zB56loR7R8osyQ_FLfKMoOqOz_Ze8aJC8TK5kJJkeu0rGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه خطاب به اتحادیهٔ اروپا: شما که هرازچندگاهی به بهانهٔ حقوق بشر بیانیه‌ای علیه ایران صادر می‌کنید! آیا کودکان میناب ایرانی نبودند؟!
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/452869" target="_blank">📅 10:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452868">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کشف جسد یک نظامی زن در مرکز فلسطین اشغالی
🔹
پلیس تحقیقات نظامی رژیم صهیونیستی از کشف جسد یک نظامی زن در پایگاهی در مرکز فلسطین اشغالی خبر داد؛ به گفتهٔ این نهاد، تحقیقات در این باره آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/452868" target="_blank">📅 10:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452867">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40df3041a.mp4?token=J_U13S9JmeMvT0ojMEsQPEa3i2UjC1UAyXwRr7I6W8GJMnOr_hOTRWcPZmD-Q1VcgmQGfxzyLgkli64GSJivfXhmBmzWUtfrApmQooFPTmsvsQr8u5EPXjWRlYKpVVnZSEl6ECGq1g8v3sQDCeA6seepRhjTGezFb7h-wCcfYTgxi5fMrP2-WUA4qqx7hqJMxpIC5aCkuqUo2PGvCYMPa-LF_hje9YILNs3ebwFLIMDngOVVIPhUJwR9yDwGNU07I52ujfHDg7xjOfN4_t46pJ0dx4UvhDzAO1YJzuUr4Gbm6XlanXoWITjXxtTOYWvmH5aQTd6xnD7aFB3nk0TfCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40df3041a.mp4?token=J_U13S9JmeMvT0ojMEsQPEa3i2UjC1UAyXwRr7I6W8GJMnOr_hOTRWcPZmD-Q1VcgmQGfxzyLgkli64GSJivfXhmBmzWUtfrApmQooFPTmsvsQr8u5EPXjWRlYKpVVnZSEl6ECGq1g8v3sQDCeA6seepRhjTGezFb7h-wCcfYTgxi5fMrP2-WUA4qqx7hqJMxpIC5aCkuqUo2PGvCYMPa-LF_hje9YILNs3ebwFLIMDngOVVIPhUJwR9yDwGNU07I52ujfHDg7xjOfN4_t46pJ0dx4UvhDzAO1YJzuUr4Gbm6XlanXoWITjXxtTOYWvmH5aQTd6xnD7aFB3nk0TfCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدم‌زنان به‌سوی نینوا
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452867" target="_blank">📅 10:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452866">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ابلاغ نسخهٔ جدید دستورالعمل واگذاری اموال مازاد بانک‌ها به شبکهٔ بانکی
🔹
براساس اصلاحات جدید بانک مرکزی، علاوه بر مزایده، روش‌هایی مانند استفاده از سازوکارهای بازار سرمایه، واگذاری به شرکت مدیریت دارایی‌های شبکهٔ بانکی، توکنایزکردن دارایی‌ها و در برخی موارد مذاکره و معاوضه نیز برای واگذاری اموال مازاد مجاز شده است.
🔹
همچنین امکان فروش نسیهٔ دفعی در کنار فروش نقدی و اقساطی پیش‌بینی شده و بانک‌ها موظف شده‌اند دستورالعمل جدید را به تمامی واحدهای مرتبط ابلاغ و بر اجرای دقیق آن نظارت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/452866" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452865">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72e331961.mp4?token=SeFnXVEgkq2d4QRdJveT1cH4zfKCMHF-r3nLgxfvIj989Wsv46tKGQ8gKF4FCget7HC3j9dq_6Kd3AlaBvzyZtl27kgrjUrzcqAsGAwXzmw0TL_lMwzY--hHzeBU2Up8AYbWO2ISQeH1XofPp5qCQsUbnHdV5yxY8PoB5OyxZ1Txc5jerulNvXg5k20OHlnxno_LpZlgGPD4IcmHaqxT3JKTuFxzt-q6opk4xf2Cv_7bKTCPxSOHQiHwH4UiqwlPY3LU1xFJw6QdkXNotXVtkfVU_hPl7_maQMVpg9n8HtNQMJa56vRxml9w5ea59Jk9HmY46dJ6-bgh7_BjfOdExw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72e331961.mp4?token=SeFnXVEgkq2d4QRdJveT1cH4zfKCMHF-r3nLgxfvIj989Wsv46tKGQ8gKF4FCget7HC3j9dq_6Kd3AlaBvzyZtl27kgrjUrzcqAsGAwXzmw0TL_lMwzY--hHzeBU2Up8AYbWO2ISQeH1XofPp5qCQsUbnHdV5yxY8PoB5OyxZ1Txc5jerulNvXg5k20OHlnxno_LpZlgGPD4IcmHaqxT3JKTuFxzt-q6opk4xf2Cv_7bKTCPxSOHQiHwH4UiqwlPY3LU1xFJw6QdkXNotXVtkfVU_hPl7_maQMVpg9n8HtNQMJa56vRxml9w5ea59Jk9HmY46dJ6-bgh7_BjfOdExw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ زنبورها یک مسابقهٔ فوتبال را متوقف کرد!
🔹
حملهٔ ناگهانی دسته‌ای از زنبورها، فینال فوتبال زیر ۲۰ سال برزیل را برای دقایقی متوقف کرد و بازیکنان و داوران برای فرار از نیش حشرات روی زمین دراز کشیدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/452865" target="_blank">📅 10:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452864">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سپاه: عملیات مرصاد درس بزرگی به خائنین داد که هوس هرگونه تجاوز را از سر بیرون کنند
🔹
سپاه پاسداران در بیانیه‌ای به مناسبت سالروز عملیات مرصاد: در پنجم مرداد سال ۱۳۶۷، ملت ایران با تارومار کردن منافقین فریب‌خورده، درس بزرگی به خائنین به ملت و میهن اسلامی داد…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/452864" target="_blank">📅 10:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452863">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انهدام ۲ مرحله‌ای مهمات عمل‌نکرده در پاکدشت
🔹
سپاه استان تهران: انهدام مهمات عمل‌نکرده در پاکدشت امروز در ۲ مرحله از ساعت ۹ تا ۱۱ و ۱۴ تا ۱۷ انجام می‌‍شود؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/452863" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452862">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-Vvh9KmwWcecI697_GvkdWojVtIAk4s1Y5ZiQ5F38JjSHcat7G6ZW8z1R0sWiIBgOcJ2hBy8ouPpuo_nn08T6YVZ6KMEDjz8zTl3ZUe6SldeeFG1NgwDrbwrB0yOrujnjcPUsTweMPfYOFsOysYGPYb9EVo_6qLgQvagIAFpRRv1i5MebBj5xJqj64A4Z2MQf__cuKOzcIIiBfvXxvM0janooON0bETCh_caDqhriKahE_Nt6uojSG66BS_ZKTB-1IVMi5wew147IFeJ_96HM19DJZP2Q0jTUu9968FCjLDcTUFjcB26_KYX9RcoxsjeU7hM6xpvAXOqIkBz9kTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن ۳ نفتکش سعودی را هدف قرار داد
🔹
المیادین: نیروهای مسلح یمن طی ۴۸ ساعت گذشته ۳ نفتکش سعودی را هدف قرار داده‌اند.
🔹
تعداد کشتی‌های عربستانی که از دوشنبه گذشته تا امروز برگشت داده شده‌اند به ۱۶ کشتی رسیده است.
🔹
این منبع همچنین خبر داده که  از زمان آغاز محاصره…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452862" target="_blank">📅 09:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452860">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xt0MUbpMjaiJJtf6nZOwMBfpxunNDoBuRT-LQ6q_7vznQ7TDyJkppzEmgFpT0JUkp5QMK18JFF-d5MqSUMem_GgnJ-I7dMKEn3iUrHNxuoYnwUvZr0wVoNxSWtcM7s9DfM79KTjBfp0dOhY_mM759gu1btC1CJmEaotcK44DrEoUZWWd-eEs_33dA5AnafJfzsntRi7Nrvzfo5ryniWeKma1A-njCeZPhVv_E45rsdQ95XSjRePPLspWBZY2vnc-A1juORU1M2Kw6KbH9WujWMaggBjaYRMznoDIlt4Ppt20umPSPcRyZKQfL7MLoDmfwBMHN7xP_x9SS05xk3PEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnLNZ_FaNtlsBK1WmznQSnId0DyEmZ7a4BNZz1NlqjyXDpMvEWPntbdHw4F1EeuqCyGNloVdy7UVMUcRiXzg4Lr9NKQtCJymtd6Oi9kYFQmchluU1cOuoJM1r_L2dPDPgtsw6w2DXkH1d5v_hNtmStY06FEYVjrrcR8vbCUE1dmB8k7N2yNpfJJn-Y-pYDUY5nPHpP6jhucQ1eyj8-PPRmYV2ZvT406v8d4Wktd_1U_XYEsN4lqUyBxulgxMSQca2GN2DMD-HheM4fh8L0AduKiQ5I2Q1jGJgHTFzIpLAHYbPvXlBmvrW0IBm7L6iDWc3a1ZGaApDahVzQ-l6fJjEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ضرر ۳.۸ هزار میلیاردی مدیران دولتی روی دست بازنشستگان
🔹
طبق جدیدترین صورت‌های مالی شرکت سرمایه‌گذاری تأمین اجتماعی (شستا) این شرکت نه‌تنها در پایان سال گذشته سودی کسب نکرده، بلکه زیان خالص آن از ۲.۲ هزار میلیارد تومان به ۳.۸ هزار میلیارد تومان افزایش یافته است.
🔹
معاون پیشین وزیر کار علیرضا عسگریان می‌گوید شستا بین ۲ تا ۳ هزار عضو هیئت‌مدیره دارد که «۸۰ درصد آن‌ها سقف حقوق را دریافت می‌کنند و برخی حتی با تخلف، بیش از سقف حقوق می‌گیرند.
🔹
گزارش تحقیق و تفحص مجلس از شستا در سال ۱۴۰۳، ریشۀ تخلفات و سوءمدیریت در تعدادی از شرکت‌های زیرمجموعه را به‌کارگیری مدیران فاقد صلاحیت، تعارض منافع و ضعف عملکرد هیئت‌مدیره‌ها عنوان کرده بود.
🔹
شستا در مجموع ۶۲ شرکت زیرمجموعه دارد که از جمله آن‌ها می‌توان به بانک رفاه، شرکت ملی صنایع مس، شرکت ملی نفتکش ایران، لاستیک ارگ کرمان، پتروشیمی ایلام، شرکت نفت ستاره خلیج فارس، سیمان شاهرود و سیمان فارس و خوزستان اشاره کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452860" target="_blank">📅 09:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452859">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5z-YOkjU2BqHU7dTTnrPRtGvztd9ZFuvRRRK_yGmVr8LLlJLvp0qJQn4F6oeivgp3pUEo7Qo2qUl5lY4PrzJEbbiyt1m8YVO-0v4daRWG3arg9VkZ2HGE5sDDQMMxVVdLy_0c3C8iSwATS783y-h9TbvcYI9NMS4ikulfrdy3bWx0zmca-OO4UA3-2BP95fRXsXR8VmP7djeWi7nnme9aUQ-OHXPYXOM7h8240qDad27Z0ZP6ldcvYiPHgRHq6dpnWugqaO28DM40dptvrjhh4hfEejKp9m8Ofhc0k69ohp6gKbe7qCa_dr-GQfdaFkejMkFl4pTpm7DcQWiTuMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ ساعت صف برای چند دقیقه زیارت ضریح امام علی(ع)
🔹
ورودی بانوان حرم علوی به یک مسیر محدود شده و زائران باید ساعت‌ها در صف بایستند و از میان مسیرهای نرده‌کشی‌شده عبور کنند تا به ضریح برسند.
🔹
حسین العباد، یکی از خادمان حرم می‌گوید: برای اینکه جمعیت یک‌باره به‌سمت ضریح نرود، زائران را مرحله‌به‌مرحله وارد می‌کنیم.
🔹
بانوان پس از ورود به مسیر تعیین‌شده باید صف‌های طولانی و چندمرحله‌ای را پشت سر بگذارند که در روزهای شلوغ اربعین، این مسیر گاهی بیش از ۴ ساعت تا رسیدن به ضریح طول می‌کشد. پس از آن هم زائران باید بلافاصله محدودۀ ضریح را ترک کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452859" target="_blank">📅 09:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452858">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ffb7c01e9.mp4?token=cVdNtEtD92aPr2BI1iywDuCFxO2_vMhP3OtneXdnQM4UnlHCUye1cBuKmSO3n4lc5lGT6n27mef-8g0fBkON6LNULXeG-cYRa9pRTdM5_aTbwOSAaNfbaiD7D3w8CGavNT_G9fHox0jyt104oI7FfCrxkCK26AxuKKbVcDpmOSOq9OXXa0yMh6_boJY_pJkgzNSzbNjMmMzOn0B3yqR0d-qGrJS1wklUghdMmYD8SyV7ky9WtF8pgucNO0S6SPH-YAEB1X9b4rMJS7h84Q3fskFGtehKH8TvkwpvZtIBH-d3l8c4Vhd6oB249Eoi78Z_0rifTDaG5S1RfbxGc8xnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ffb7c01e9.mp4?token=cVdNtEtD92aPr2BI1iywDuCFxO2_vMhP3OtneXdnQM4UnlHCUye1cBuKmSO3n4lc5lGT6n27mef-8g0fBkON6LNULXeG-cYRa9pRTdM5_aTbwOSAaNfbaiD7D3w8CGavNT_G9fHox0jyt104oI7FfCrxkCK26AxuKKbVcDpmOSOq9OXXa0yMh6_boJY_pJkgzNSzbNjMmMzOn0B3yqR0d-qGrJS1wklUghdMmYD8SyV7ky9WtF8pgucNO0S6SPH-YAEB1X9b4rMJS7h84Q3fskFGtehKH8TvkwpvZtIBH-d3l8c4Vhd6oB249Eoi78Z_0rifTDaG5S1RfbxGc8xnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از فردا باید منتظر کاهش دما در نیمۀ شمالی کشور باشیم
🔹
امروز در بیشتر مناطق کشور هوا گرم خواهد بود. دمای هوای تهران به ۴۰ درجه می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452858" target="_blank">📅 08:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452857">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f62fbaa4.mp4?token=gDUhT5CMWjCSllyFG4BN1QK-oT8g3o69llWPT9nCm8nx7kO6WK0sxgY4UfeeIo6OIspOcuB1Lb-3KSJS01Xr5Gssx-lOEcnwz19vShYsrMtaLOoMS3R82v-Irl8xgx86UGatQTR0tRlPI_Eqpj6k2YO_voKsJ5IObAf0ckNbfGW9pzNakU5ec3fkrijSMCk1K6sarfpByxrdkVTfyD_ARFtQcUB6fGRBKlC_tEccHrWKvGPuTL5zLJpz1buf8CCMyUW3P0Py6ebn4l7q40YZCPz-gk-DCIY3JdS2SuYjyEy-Y4EeIUcn802KutAExSirtsE9YtZKIbkK_C85QxoYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f62fbaa4.mp4?token=gDUhT5CMWjCSllyFG4BN1QK-oT8g3o69llWPT9nCm8nx7kO6WK0sxgY4UfeeIo6OIspOcuB1Lb-3KSJS01Xr5Gssx-lOEcnwz19vShYsrMtaLOoMS3R82v-Irl8xgx86UGatQTR0tRlPI_Eqpj6k2YO_voKsJ5IObAf0ckNbfGW9pzNakU5ec3fkrijSMCk1K6sarfpByxrdkVTfyD_ARFtQcUB6fGRBKlC_tEccHrWKvGPuTL5zLJpz1buf8CCMyUW3P0Py6ebn4l7q40YZCPz-gk-DCIY3JdS2SuYjyEy-Y4EeIUcn802KutAExSirtsE9YtZKIbkK_C85QxoYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنل‌های خورشیدی به دادِ کشاورزان بویین‌میاندشت اصفهان رسید
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452857" target="_blank">📅 08:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452856">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
مدیریت قاطع ایران در تنگۀ هرمز/ حادثه برای یک کشتی
🔹
یک مقام آگاه: ساعاتی پیش و در ساعات اولیۀ بامداد امروز، ۶ فروند کشتی متخلف با خاموش نمودن سامانه‌های ناوبری و موقعیت‌یاب خود و نیز با تحریک ارتش کودک‌کش و تروریستی آمریکا قصد عبور از مسیر غیرقانونی و ناایمن جنوب تنگۀ هرمز را داشتند که یکی از آن‌ها دچار حادثه شده و بقیه تحت مدیریت قاطع ایران به خلیج‌فارس برگردانده شدند.
🔹
همان‌گونه که قبلا هم اعلام شده بود مسیر تردد در تنگۀ هرمز مسیر مشخص شده توسط ایران است‌ و مابقی مسیرها آلوده است و راه به‌جایی ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452856" target="_blank">📅 07:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452854">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa96a9605.mp4?token=pLyd_SJyQfpBCTLXu5_f-fl2S82RQGTnf9AtX4VUn5q6iC9tvNa6-TqwABLtjEMzA8acFirBZdOs20erM98-DCuJDZdK2_NuyQXfcV1aXUejCtAkatSXO9ziuRxh5pvQfTVQeMy-PErCjYl9IuVsUYZr8oDEwTsz4Q229ltQCZgQzIs8I7NTkit0_lZy76WCGGImunSyvb6-snHdIo_AzvB2nGDMPiYVSLFs6QYfRizYvsdeVbcZ5AnWsg7lbYBwShAzZM1JvlIZBxpgXySh9RRsvp8eh_TJbpMFtAXUs1vUjM51BhQ8XVbVR-cWBvBUMPZtOfphcwhbn_9x7s59KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa96a9605.mp4?token=pLyd_SJyQfpBCTLXu5_f-fl2S82RQGTnf9AtX4VUn5q6iC9tvNa6-TqwABLtjEMzA8acFirBZdOs20erM98-DCuJDZdK2_NuyQXfcV1aXUejCtAkatSXO9ziuRxh5pvQfTVQeMy-PErCjYl9IuVsUYZr8oDEwTsz4Q229ltQCZgQzIs8I7NTkit0_lZy76WCGGImunSyvb6-snHdIo_AzvB2nGDMPiYVSLFs6QYfRizYvsdeVbcZ5AnWsg7lbYBwShAzZM1JvlIZBxpgXySh9RRsvp8eh_TJbpMFtAXUs1vUjM51BhQ8XVbVR-cWBvBUMPZtOfphcwhbn_9x7s59KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی مرگبار در سیاتل؛ ۲ کشته و چندین زخمی
🔹
در پی تیراندازی در یک جشنواره غذا در شهر سیاتل آمریکا، دو نفر جان باختند و دست‌کم چهار نفر دیگر، از جمله یک کودک دو ساله، زخمی و به بیمارستان منتقل شدند.
🔹
به گزارش سی‌ان‌ان، مقامات آمریکایی تاکنون اطلاعاتی درباره هویت یا انگیزه عامل تیراندازی منتشر نکرده‌اند و مشخص نیست که آیا فرد یا افرادی بازداشت شده‌اند یا خیر.
🔸
بر اساس آمار سازمان «آرشیو خشونت مسلحانه» (Gun Violence Archive)، این تیراندازی دست‌کم دویست‌وهفتاد‌ویکمین تیراندازی جمعی در آمریکا از ابتدای سال جاری به شمار می‌رود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452854" target="_blank">📅 07:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452853">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">امروز هوای پایتخت ناسالم است
🔹
بر اساس اعلام شرکت کنترل کیفیت هوا، شاخص کیفیت هوای پایتخت امروز روی عدد ۱۰۳ قرار گرفته و در وضعیت ناسالم برای گروه‌های حساس است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452853" target="_blank">📅 07:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452852">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbdFyAKyj68FB6nZtjyMmHdDCClfey9paqlvbOeSnFaTGmz3BHPNzMxfu25BCCc60RokO-vepzXoJQ7yjcoTKVUMInshwZdswGtvS8QOcASJD-tAUwtIfLEfhSo5cgSfg8QZqOYK1JMm_IaN72jcQtC9KldhF5EtLSYHlCh2fzndmIHvmA73JSy1PgZNTSCKrCKC-Z16fNXl5Prhq-bMVU-EodYIjtFT0C65u2ChTDHUptxY5pl7C2PlcLkjvjl_DiDFsNVFbTjxfzxGeZe_uUmwAfyFdC2-ddj55tbl3s_eUZr9nc2FaYiW0IxJ5A-tqBXHhrHjwIR_mAq_Ad2SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وسایل گمشدۀ زائران اربعین به خانه پست می‌شود
🔹
سال گذشته برای نخستین‌بار، وسایل گمشدۀ زائران در عراق که دارای کد شناسایی سماح بودند و صاحبان‌شان در مسیر پیدا نشده بودند، به نشانی ثبت‌شده در سامانه ارسال شدند.
🔹
امسال هم این طرح ادامه دارد؛ زائران باید پس از ثبت‌نام در سامانۀ سماح، کیوآرکد شناسایی خود را روی وسایل شخصی و حتی تلفن‌همراه نصب کنند تا اگر وسیله‌ای در عراق گم شد، یک اسکن ساده آن را به صاحبش برساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452852" target="_blank">📅 06:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452847">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uh52dQlzT0pO6YBxyIIVKYkx2WcSkswY4x7J_Osd_jUVYoXCFCEWoZ57-XIcixz3Xj4oCBrAfs-5nRjxoPstsi9FeVuNrVUlqKP-sV2Wrt8cvLmxichM5mVQaeSsjdF1u6xgdPLiydNTHQ0rovy6MWAGRQOi0dS99n-qJYR7rjdCT9vZxwKHzpJzMBWx4t_FJR3WPTxCOMORCmOH2xgwRci78ze4crYFDXpAf-SlsOcDdoV2riRbHzsihfjK9G8EcErIdnPZ5kF5LtSxtBwV3TWVcynotwdT_nTKDWWZCgNbRSIn072RTFb7iRozMUBOzPIx1aTrzcdcwO76qNss_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVZNq9vkD6OYIneO2KCMSxZ5YkE7NTEhSQMaGyXfZhDpeCCCM-QnFlnKoCV96SM3tVExtAoEtZ5SfR6eet6B2VODGEZ3LAV-l-DS7Tdl9ZFsxsdQQ_4BkvRpzLgZxfqrt_bCrjdwwZJYqRiKyKmm29cFceYs3-JxHMAeIs6rI8Nf6PuABoD8ePFnNmJSDAJPR6iMhz9_ScoQwsa3YAA4-pntckITblOoX6bTrpgyS_fToBBZ_g7MGWGVgurAVQcuwxpBmGSLZeUxxo7wRmvjb06pnD3o_yK_3bGjX2GAeeh6QgyvuJCi7TReoKzcgM3d5Eues8eH3PdPde4OsTz2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIJSboXnDBV50nZXyo_EC5YrlprOTZQfCRJj-5Bsu5CeCrJtGtQgdKxRt5SkhXTB2eqCZfy80vBpwT0QxnZZreK0vpx1G3oQHYoHk3DKnrkokMYkR8EZkiSDFYkPnTovrIwP0Oh3nmgm2HnT5sP7binJ2YeaFFyy59GGC_icKAh8Qq1qvH4XSFOgEFuTejwMjPGcWI8_giIqc5yZeooSpqD-FoXG0StkTLOJEczxnSJ_X2ctxHf5t3txUVDEw0_sR6lklMsxgsRY3YWs8m5zIhCJaP2xVT1MPqzeMzNuLInrLYgZQz_oL--Xdd2mPnISFJKKUHzrkcFxXZLF8t0n4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoyyZnwDHSoB9q06B84dUM8rTVjepyEO2VdU268zVHQiBv6PTmThzvE8CYrPpk6XmyDwN3Ilo17TMWQBmCfCx-1mFRT3Jl3TIinK3zpdBKwZWmVr1OisVICmUQKIiM0li543jwvbN0cT1Kqt630dO7Sw8KY6st68cbWIHCFDTpFg4z9hiqlV9nNKrOp48_9aWzarPgncwUESuwfS04BQrqysIi62zAVDIFp7N-NlaeG0-QnwnCZfMtbTt9USQ17XodrwEWgx_-dzqbPc1IVHGQMIAlJQrc4U1riWhbw5zNPNKjFZq_YpObjGAt_jQsGx_mR-7yxTJ-3yvmfBtQrFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N41IFuWC_cTSrD_j5OPx-04TgEaxLB8jEKhdiak_FsAN1KbfnuN0F9d-lMDWqcLayGV5TrK64jlvXp9zSPKu0S4hZdh97m7wVBdzl0ykz7-oSRJuYEeYJdSMKkHkiOw7r7M5QeOM-UpyQsE8JP28F-tItBOYZTUH2WcfAdiJltREorZI2GmxiqnPE42B0RoZGxNrDMwrTjoAT_22SDmIaFfct7vudOgG612IVOB7GaGWpv-0fq_igpFqmVIKxCXBlKKa3LuVt-FI4U_IYhN5doJnvxYkS0E-CSV0Eeq6g4TcLvJRUqnbEhn3sheIE_BLS48p7TsHxjD5Uz7sg-gpRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زیارت خانه پدری
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/452847" target="_blank">📅 05:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452846">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-oe5GyyVjGMEiUyXIz71W7foAJjmOfjhz-uu3fh-dO0ch6pAMDRvXpvsA7wzny7_XDX2M0XHSuPvgcBIw6inMxx6TYtIYJBxDmId28ap99FixfrR_E9rUTZ54llrQ-A1rDrdOs8hNaMLU05pjnA7OK0rVDTP-yC1hJpvqT0WuZEJgwqHeF40RUNEaDJQzDq0BWe3ZvCt9kkV90LPmx3N0SfTplV7b3fzsypxhQ7LIxeZWW3nTlMyGVoWSAm6mG_zSuQL0ghiGhG9CJoesPOaeEbiol854qwaBxsyqKaTsIueIC2jbItRw5ersEwxDJEVZYumY9yz6pIl2nIbvT7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگرانی زلنسکی از باز شدن جبهۀ جدید جنگ با ایران
🔹
رئیس‌جمهور اوکراین، در توجیه حملۀ پهپادی به یک شناور ایرانی در دریای خزر که به شهادت یک ملوان منجر شد ادعا کرد ایران قبل‌تر با ارسال تسلیحات به روسیه، علیه کشورش اقدام کرده است.
🔸
البته این درحالی است که ایران تاکنون بارها هرگونه مشارکت در جنگ علیه اوکراین را رد کرده است.
🔹
زلنسکی با ابراز نگرانی از هرگونه حملۀ ایران به اوکراین گفت: باید محتاط باشیم و هر کاری انجام دهیم تا جبهۀ جدیدی در جنگ گشوده نشود، اما باید واقع‌بین باشیم. امیدوارم ایران حملات خود را افزایش ندهد، با این حال باید برای هر احتمالی آماده باشیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/452846" target="_blank">📅 04:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452843">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5PaX55NpEYHjeAj5A-4uWw5ZSIrvaSzBV5AhTC_JoZD97KeS-FP2Kp6VyS6r7qixgCValQAG_jAx4FWyfqIHJHle01xuPzKpyXGbsPI2bJ8XwYlHKDqjovLAr43rstBCeEZi-mU08uqX2ZhgS_8oQy9oZflFdomNvuKJgzydW6qc3KGwoMJSe4qkQNkkfAOWvdWl8JyLo70tzbGP6M5EyRjd3qeYqT_WtWssvx1zvinkTOzzJcWynjx06r0mwMD1itdQsczMS6YHMKYwoJJenT4MPCt1FyLIQ919kQ4ia5xzjB2wH2oq1HGxUTDbj2YbJc9e3k_W9W4trw3D2PyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZcbSwhaVXN74h4bE4KZEUclvhG0c9mCBE5QTJ3dIwy3VN653s4OYcTzNY5WPAhv1Hu4vnMg6flo8965euKx6-PFs7cwBXVNNqMF_XFk8RiJd8pPKGo7cRAAG-4cd5uN4kYhGfW4-eCfmEDOffHJQa3tP8un0tnLJn54GBIcw0QuixOuKNdEV0bDFAfQpdjt49FtJkm4pJeuORQE6HVvasKaS7bu--R2xb6AKVKDdaRZURuYZezMXRUA6XxtRY4dXDKK7NLZghDig6kaG8nJrdhUStJyP9OyNkBSJho26kmKWyZWJRaLzNdqxrEQR9WyAgWQxid_3lUmwWMcT5oawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ac7IFDpjvRIFkYXwAuQh3-nmmdcT1Hl1nirSFRtMJksflBV27LUIQtU_9jgjH-FBguMohfh_htiI75yO6TNpydBfOp0yoHrEkNPg-VlWbtqc-7g1cJUTZMU7OgHuGZdMRTjz7ebjxAz7HP6Bfaeo10wanL_VkZ7D8iLlzC2VaT76F1Yu6Cf4T6plZ_J3AbabSRKSQtYjKvllTgrFtqEEwqBAtAwGxRoFDyGxRgOnGxwCBdzcZWPWU2Vwspt82NCTlx72ki6Cwrc9-uTDMxFkwxpEB8ZSgQVS1CZTy3ZYcTEebfmx5wo6pPMYbTTM_OMc4TAucIk_NbCw6-hZatA8MQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیویورک تایمز: آمریکا در باتلاق ایران گرفتار شده است
روزنامه نیویورک تایمز در تحلیلی درباره گزینه‌های ترامپ در قبال ایران نوشت، رئیس‌جمهوری که تصور می‌کرد قدرتش هیچ مرزی نمی‌شناسد، اکنون دریافته است که با محدودیت‌های متعددی روبه‌روست؛ محدودیت‌هایی که او را بیش از گذشته سرخورده، آشفته و در تصمیم‌گیری و رفتار، غیرقابل پیش‌بینی کرده‌ است.
مشروح این گزارش تحلیلی را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452843" target="_blank">📅 04:13 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
