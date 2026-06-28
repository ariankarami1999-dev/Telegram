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
<img src="https://cdn4.telesco.pe/file/Ur25_Q7cGH1fH98uesEHtWqvITwn_ZSFBmx4flXlOVQKI2XknxuF1lt2pByp4xL15ZQgxy8nyXxxmZnEk7qDBnK4BCzHKSQanFBubfzZKtem_PTrq9weTvuehU2DDVZIVQ2dQqxZy-TtTZSkRLBVaR0qJp5BDx---nnu7T04MNzhSABhtD-0voz_K2tsL-LFk1UG6PtVdgM864P66QOvtCSi2-f9_Gc9RQTG5BEIvG0g_G03VzFS4bIgPqviVwhGnjueBPAtBrlJs75D3LlASRVVQKx5sk495F9V7z0i6e8FiAwLYlfVc7tGQDwOS9UxFEobRy9K1FK-B1p1JtNFAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 14:07:51</div>
<hr>

<div class="tg-post" id="msg-80199">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">البرلمان العراقي: أمر رفع الحصانة عن المعتقلين وُقّع رسمياً خلال الساعات الـ48 الماضية بالتنسيق مع مجلس القضاء الأعلى</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/naya_foriraq/80199" target="_blank">📅 14:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80198">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رصد تحركات امنية عراقية في محافظة الديوانية جنوبي العراق لاعتقال عدد من المسؤولين المتهمين في قضايا فساد.</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/naya_foriraq/80198" target="_blank">📅 14:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80197">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
بعد دقائق، رسالة لقائد الثورة.</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/naya_foriraq/80197" target="_blank">📅 14:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80196">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
بعد دقائق، رسالة لقائد الثورة.</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/naya_foriraq/80196" target="_blank">📅 13:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80195">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9a1341dc.mp4?token=dIJ_WCZoIuNFJoB9DizBlki4tIAlicvpnOmQRLogz7o_E0_caYW8OR74NNbTyaqV54fN03iU-PHX4Lcsf0XILJKUE-A1kfgx34fXw3IxsdiamCs2_pP7BOVOR0h_lLmbMt8yG8HtEFkkcy5H_XK6X5VlVoFGmQYkX3pHTWBuouVFVbUhssadhzY01R1o-vuQn2h3G9X1tsSUfntLGHHZenBLOyRVtImU53HnGXVPX-i6kjs2k2v8gA_4vP_dyL_d-TtxEz4jp1d_Z1bRMWWtROHG1Xr2TvZqGrKTKEPSmxZg6IP6TMulZ7m1Yi9_gmuv4Eyg7nshc2L9sur8zKzePw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9a1341dc.mp4?token=dIJ_WCZoIuNFJoB9DizBlki4tIAlicvpnOmQRLogz7o_E0_caYW8OR74NNbTyaqV54fN03iU-PHX4Lcsf0XILJKUE-A1kfgx34fXw3IxsdiamCs2_pP7BOVOR0h_lLmbMt8yG8HtEFkkcy5H_XK6X5VlVoFGmQYkX3pHTWBuouVFVbUhssadhzY01R1o-vuQn2h3G9X1tsSUfntLGHHZenBLOyRVtImU53HnGXVPX-i6kjs2k2v8gA_4vP_dyL_d-TtxEz4jp1d_Z1bRMWWtROHG1Xr2TvZqGrKTKEPSmxZg6IP6TMulZ7m1Yi9_gmuv4Eyg7nshc2L9sur8zKzePw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات من بغداد تنتشر في محافظة واسط لتنفيذ عمليات الاعتقال</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/80195" target="_blank">📅 13:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80194">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/836431c75f.mp4?token=d0L4jTJtS2ZBlMsr07W1pxnN_9D5VVKS7SVShGPXWCzV1z7Qy-j4dgg_HfWb9ym_EU1lF3tJFDLW_LyMQieqBlcGzOQ10FZwhmmSeJgOTw4Aw_pPG4vVPEJw40mEkscuq_yYTw8FwC2cXs7Q8OVNhPY9RU_GCjXaTfEOw4gBztBryXVd-CMlBjqrzlyPOIIXyFtd6iYV7gTatdEakL0geKn7Kj0BZa4HbQOUr4Y6IMgQIp9wbrDFesSc5wnnyry-scXlYhOpCie4V2dV9gRDzAg09hZAWq_pEN1AEm6sBusFxqaqnPNtwAEOfQF-W3yDSDBEJ1wjR_q3zuaz1YI3MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/836431c75f.mp4?token=d0L4jTJtS2ZBlMsr07W1pxnN_9D5VVKS7SVShGPXWCzV1z7Qy-j4dgg_HfWb9ym_EU1lF3tJFDLW_LyMQieqBlcGzOQ10FZwhmmSeJgOTw4Aw_pPG4vVPEJw40mEkscuq_yYTw8FwC2cXs7Q8OVNhPY9RU_GCjXaTfEOw4gBztBryXVd-CMlBjqrzlyPOIIXyFtd6iYV7gTatdEakL0geKn7Kj0BZa4HbQOUr4Y6IMgQIp9wbrDFesSc5wnnyry-scXlYhOpCie4V2dV9gRDzAg09hZAWq_pEN1AEm6sBusFxqaqnPNtwAEOfQF-W3yDSDBEJ1wjR_q3zuaz1YI3MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الامنية العراقية تنتشر في قضاء الحي ضمن محافظة واسط لاعتقال عدد من الشخصيات المتهمة في عمليات الفساد</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/naya_foriraq/80194" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80193">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f7136922.mp4?token=ApZQEuACg7HXmEkzNMHq-SMkxTZjKOnOd9IdLupkxwFt88xdk6X_ERv3Jwrrk6ol-KKsTlUMCPqV8HYVV2fSK4oJPIboZw9l8mtwbHKJUN28g1n2waoGayp19FAhRQPIYxvKlJuJKVg-s04D4Clfr8NyrPgxtM3p28ZJRv4eSgsjeP2IZgtAZ4J4iZcQMrA0b9jx4YfHFJ97O7lPwgd2k74tlX81dwxySObJxAmDz9IYufo5Qex8OShfRHQiN_6Gj-g1S83pUoB82HxVrc-lWUuiEJi8Z04G_hl730kvfPNgkz_HKriLi9J530gh10_ncRqZkJcTSsldn5iRGes10A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f7136922.mp4?token=ApZQEuACg7HXmEkzNMHq-SMkxTZjKOnOd9IdLupkxwFt88xdk6X_ERv3Jwrrk6ol-KKsTlUMCPqV8HYVV2fSK4oJPIboZw9l8mtwbHKJUN28g1n2waoGayp19FAhRQPIYxvKlJuJKVg-s04D4Clfr8NyrPgxtM3p28ZJRv4eSgsjeP2IZgtAZ4J4iZcQMrA0b9jx4YfHFJ97O7lPwgd2k74tlX81dwxySObJxAmDz9IYufo5Qex8OShfRHQiN_6Gj-g1S83pUoB82HxVrc-lWUuiEJi8Z04G_hl730kvfPNgkz_HKriLi9J530gh10_ncRqZkJcTSsldn5iRGes10A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الامنية العراقية تنتشر في قضاء الحي ضمن محافظة واسط لاعتقال عدد من الشخصيات المتهمة في عمليات الفساد</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/80193" target="_blank">📅 13:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80192">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">القوات الامنية العراقية تداهم منازل وزير الكهرباء السابق زياد علي فاضل وتعتقل عدد من اشقائه.</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/80192" target="_blank">📅 13:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80191">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzOMLiiU5B9yhxh1fnKRg8fZC51hrBLq31zbyHLoEAQlCJPXYA5WXaTHrDhxKIV87GQ1wyOgKg_spNjRKKXXADY5ow5jqsYT4c3Kl-Vu06TiS08zwApSP4Amd13lGGApB57G5LwVdNp5G7xihzYKk7HH9sC9gIewXYNPhlsBU7anQCHAR9sfLX8BgOr9Q-N0n0NeOu4DyW2atjdbYkGqoiA9Qfv5Ji3qCqiJD-QG7IDr1681HdQmBBSUFw1OOgNmWMbXmnfpebrSpTJoE6J-C0Ur1h5TUSO0rAbiVoa0B5iU5MirV-zUnJYmmQhkP8QkcEaIrO2J9UVT6190EaZK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش الاحتلال يعلن مقتل جندي في جنوب لبنان يدعى ديفد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80191" target="_blank">📅 13:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4420469c23.mp4?token=PLWnWDbsPeIRl4gdFOPK1QwIlyaRE4tykLwF1V-bXOa0mC5-1AIPWeAXNB_S0cluHXeTJZ5W1UoFZ6DjcQw8LncDjar3l_WgJaadEFzPCxxjTx52TU-SUwlWbJY3ldp-R8ui94XPSMGbvBOrICo9WjjVGLtqTUiw40IDAaBfNPcHSIP_LaK3FJf-O8iQzSzjgHbPvfbvpECrMv0LEoBt4r0baIdW3NLER5t66-JWqSw2FD4oP9W2nvHin3C9P3d_tyy1VPWg7cwbro2Jz9SRfsYB4Q9SsJEpJknpoAZ3XeW_DnBQkrIV2u1N15P4bfUO5NTgXsLOaEtogPJbYxC0AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4420469c23.mp4?token=PLWnWDbsPeIRl4gdFOPK1QwIlyaRE4tykLwF1V-bXOa0mC5-1AIPWeAXNB_S0cluHXeTJZ5W1UoFZ6DjcQw8LncDjar3l_WgJaadEFzPCxxjTx52TU-SUwlWbJY3ldp-R8ui94XPSMGbvBOrICo9WjjVGLtqTUiw40IDAaBfNPcHSIP_LaK3FJf-O8iQzSzjgHbPvfbvpECrMv0LEoBt4r0baIdW3NLER5t66-JWqSw2FD4oP9W2nvHin3C9P3d_tyy1VPWg7cwbro2Jz9SRfsYB4Q9SsJEpJknpoAZ3XeW_DnBQkrIV2u1N15P4bfUO5NTgXsLOaEtogPJbYxC0AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انفجار سيارة مفخخة في حولون بتل أبيب</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80189" target="_blank">📅 12:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80188">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa677b1f6.mp4?token=LsRYyf0TH5qCFK5oi__gce7KmLthbwqS88JGgDGvJeqW1nQnootfa_Jn-d503pB2hGo4iB5SLIdnie7K0mWa4TgSztobtVXb61Nx5ADMiP5EORij2C7gXV-lewF4ffBlgtwea8n66pochd6wRnUUiinosRB0QWZ-JbBD_iZWX0Axp9n5gj8WRjgeELZZV88fKT5Y0SraCdGLfcN-TnZTAjQzq5B9_BUyKdsXybSwZj-SuwLgae07vIXu5DKM3FZIi6DEi4ux2e2lmOR4H8O07E4-777ZPWccT-02WfACVMuvXTf_3OyU7I6ALapgfLLmvYpYxGSSE1-7sQqvn1Wgfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa677b1f6.mp4?token=LsRYyf0TH5qCFK5oi__gce7KmLthbwqS88JGgDGvJeqW1nQnootfa_Jn-d503pB2hGo4iB5SLIdnie7K0mWa4TgSztobtVXb61Nx5ADMiP5EORij2C7gXV-lewF4ffBlgtwea8n66pochd6wRnUUiinosRB0QWZ-JbBD_iZWX0Axp9n5gj8WRjgeELZZV88fKT5Y0SraCdGLfcN-TnZTAjQzq5B9_BUyKdsXybSwZj-SuwLgae07vIXu5DKM3FZIi6DEi4ux2e2lmOR4H8O07E4-777ZPWccT-02WfACVMuvXTf_3OyU7I6ALapgfLLmvYpYxGSSE1-7sQqvn1Wgfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انفجار سيارة مفخخة في حولون بتل أبيب</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80188" target="_blank">📅 12:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80187">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نايا - NAYA
pinned «
مصدر لنايا   اعتقال ٣٧ شخص ؛ ٢٥ شخص داخل المنطقة الخضراء ، ١٢ خارج الخضراء .
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80187" target="_blank">📅 12:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80185">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
جيش الاحتلال الإسرائيلي سمح بالنشر: مقتل جندي صهيوني إثر اشتباكات عنيفة مع حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80185" target="_blank">📅 12:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80184">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fd2512544.mp4?token=AN1umLQdgkc0Enf_Lyp1TeNcdQkLoopxmMjDR8FIypH15hYMh2s0iVwG34QYjkxSrOvn4H0mUH_zQnDIy263FavPCEUq_HXOSUp73-DY-7T7ea3OTtTLC3FTgy_1eBmqlyDpZ2EMWOOffvnIdxX2hKQN_6LY-jEmwvuUUpVSm9s4OpiDZugEaI38lgV_y6UF75f8BtETORp4lD2vXTwyC5V0KOIVyToLBVg4ohRpCpvsHOmBRNNi1D3ImeDlO3_ZBYUf2UjdbHaewOaZt6X2tNXrULiZ4oKOH_qCSyV3ueDDtFlN02HNFornXEG2sKcTZBl1HdooJtyvqJsmo0iF3GQBN2kjGuCMPihGFeTVY3cOA1rjrR0ulrZl5ye3cK_9vkwArJmUMkot1mMqZeNqaHrmi1VSlTdPIcKhFUZHlJr_Mdd0AtQGwk0AQ5ph_dkN15k1NFu3NGFaOsRFIDcpeP57RD5juKB8SIfg3w80MtKSWn0zC2zrfNyrjAdI2hq1d7lUzTOZyYfel0rFcYlywTGBpmloOp9-AfVaM7w3yp-Z4T23NJ7CvzmgTXjgwzj0faJ5Ah9CdcGDIZ0ELSkzfnkVMtbt2-hCtFEaC7rvGZOBjUwOcdEVYXidu-0IJ9GApZMy0fju66v1toYiRhOkBzRz5am5tQfpLgoqM_Sqc90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fd2512544.mp4?token=AN1umLQdgkc0Enf_Lyp1TeNcdQkLoopxmMjDR8FIypH15hYMh2s0iVwG34QYjkxSrOvn4H0mUH_zQnDIy263FavPCEUq_HXOSUp73-DY-7T7ea3OTtTLC3FTgy_1eBmqlyDpZ2EMWOOffvnIdxX2hKQN_6LY-jEmwvuUUpVSm9s4OpiDZugEaI38lgV_y6UF75f8BtETORp4lD2vXTwyC5V0KOIVyToLBVg4ohRpCpvsHOmBRNNi1D3ImeDlO3_ZBYUf2UjdbHaewOaZt6X2tNXrULiZ4oKOH_qCSyV3ueDDtFlN02HNFornXEG2sKcTZBl1HdooJtyvqJsmo0iF3GQBN2kjGuCMPihGFeTVY3cOA1rjrR0ulrZl5ye3cK_9vkwArJmUMkot1mMqZeNqaHrmi1VSlTdPIcKhFUZHlJr_Mdd0AtQGwk0AQ5ph_dkN15k1NFu3NGFaOsRFIDcpeP57RD5juKB8SIfg3w80MtKSWn0zC2zrfNyrjAdI2hq1d7lUzTOZyYfel0rFcYlywTGBpmloOp9-AfVaM7w3yp-Z4T23NJ7CvzmgTXjgwzj0faJ5Ah9CdcGDIZ0ELSkzfnkVMtbt2-hCtFEaC7rvGZOBjUwOcdEVYXidu-0IJ9GApZMy0fju66v1toYiRhOkBzRz5am5tQfpLgoqM_Sqc90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
‏وزير الخارجية العراقي: أشكر نظيري الإيراني الذي كان يضع الحكومة العراقية باستمرار بشأن الحرب والمفاوضات  غلق مضيق هرمز كان سبباً من أسباب عدم تصدير النفط العراقي وقد كان له أكثر كبير على الاقتصاد  سنزور طهران لتكملة المحادثات</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80184" target="_blank">📅 12:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80183">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00e129455.mp4?token=JMHli7LcFzZwD9cV-Nt_n6hIlUJ9lhxgx547C-JX4OsRLcn_UUWbBXuGgZpkk64RfMnYfARzWWmwSvobq3Byixpue0tkSGAzMv_igvzlKb86FAKnUhfP77bV5JifhDSQLdq2-Eqxygn3Rct3mL-VpZyw5vzWs_KHjTElMHyIi_RFY_TgbjztKEuCQ9gMRAYIG0JTdT7B98i0tc2tALA0ntVR40jQAyZIbWzcJtRtcPU30TUJLmVIqcMbUoVu_0SCRPfA9b5fliVF8nxFbi16RcwRN87cEnaOh8h-sxLry8L--eCNyHY6hkKXqNnZCrzgg5sZcD_-VvI74U2SVRKpF4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00e129455.mp4?token=JMHli7LcFzZwD9cV-Nt_n6hIlUJ9lhxgx547C-JX4OsRLcn_UUWbBXuGgZpkk64RfMnYfARzWWmwSvobq3Byixpue0tkSGAzMv_igvzlKb86FAKnUhfP77bV5JifhDSQLdq2-Eqxygn3Rct3mL-VpZyw5vzWs_KHjTElMHyIi_RFY_TgbjztKEuCQ9gMRAYIG0JTdT7B98i0tc2tALA0ntVR40jQAyZIbWzcJtRtcPU30TUJLmVIqcMbUoVu_0SCRPfA9b5fliVF8nxFbi16RcwRN87cEnaOh8h-sxLry8L--eCNyHY6hkKXqNnZCrzgg5sZcD_-VvI74U2SVRKpF4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
لحظة إطلاق صواريخ عملية الحسم الصاروخية والطائرات بدون طيار فجر اليوم من قبل قوات الفضاء الجوية والقوات البحرية للحرس الثوري ردًا على اعتداءات أمريكا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80183" target="_blank">📅 11:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80182">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
🇮🇷
وزير الخارجية العراقي فؤاد حسين يستقبل نظيره الإيراني عباس عراقجي.
🔻
لمشاهدة أكثر اضغط هنا</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80182" target="_blank">📅 11:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80181">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصدر لنايا
اعتقال ٣٧ شخص ؛ ٢٥ شخص داخل المنطقة الخضراء ، ١٢ خارج الخضراء .</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80181" target="_blank">📅 11:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80180">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4069bb51f.mp4?token=LQXpjQlMZdJBY1LQnCsKxChOCRAdA9MR5RpNFTK05_SMNVpQNbC_fopR2LE-YxpT-cVK2SljwoWOSnDPb2m-rVeENU7MVsAfHxRrgzUZoESbhbProIlhqluC9HDO0K_t7cKeGx3PuTJOgZr65K20z96KcnnKxwwFJmzOu5PcEe6VoY1rdNcTUhWJQkYSJBoYIv9gVEvbGkKvjJxbUH0z0ZZvQYO4W72L8UKESZ3uVtnrLL5QXahV_0BLhSAzo4x3bRg22n1GA9QP-p-jIC5S85Zwbqtp6W86ijUy2ST-yRHvqQ0yiON3IuiHOtGKZCZFjpGO9ShBgBcIUEUlKUZNCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4069bb51f.mp4?token=LQXpjQlMZdJBY1LQnCsKxChOCRAdA9MR5RpNFTK05_SMNVpQNbC_fopR2LE-YxpT-cVK2SljwoWOSnDPb2m-rVeENU7MVsAfHxRrgzUZoESbhbProIlhqluC9HDO0K_t7cKeGx3PuTJOgZr65K20z96KcnnKxwwFJmzOu5PcEe6VoY1rdNcTUhWJQkYSJBoYIv9gVEvbGkKvjJxbUH0z0ZZvQYO4W72L8UKESZ3uVtnrLL5QXahV_0BLhSAzo4x3bRg22n1GA9QP-p-jIC5S85Zwbqtp6W86ijUy2ST-yRHvqQ0yiON3IuiHOtGKZCZFjpGO9ShBgBcIUEUlKUZNCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سيد عباس عراقجي يزور محل استشهاد الحاج قاسم سليماني و الشهيد ابو مهدي المهندس قبل التوجه الى وزارة الخارجية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80180" target="_blank">📅 11:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80179">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2b16e76c4.mp4?token=KfgM3BrXglaffQDy0QOSJWz8UIlIt8QMXE5-dulViZK3gkIGyXGb2x6p14jTf7nw8fWE_iEc03kwNwRByVt8gcm15q6w0c0XEwwNkdLmCSONVT-le6XAnRG75uyHfHizbiiAyBC28XC8hDRUbgfYtikWFjfiDRSjkEVFL34D2ZlYLZcMVYx0GGpQThDPhcBw8RK5p1RY3GAiS4kK1SQiZ5DE_0-cYJxTnJWvrTw8y710LdwnXvALSsmVB41kGS3COJqM1n4mPxcgVHit4MM8eorumrLaHSVhH_q0n_MzBpLx-5JNSXu0dFIBuJPVX5vmRBHWX8b3ML3EysrXaiD33A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2b16e76c4.mp4?token=KfgM3BrXglaffQDy0QOSJWz8UIlIt8QMXE5-dulViZK3gkIGyXGb2x6p14jTf7nw8fWE_iEc03kwNwRByVt8gcm15q6w0c0XEwwNkdLmCSONVT-le6XAnRG75uyHfHizbiiAyBC28XC8hDRUbgfYtikWFjfiDRSjkEVFL34D2ZlYLZcMVYx0GGpQThDPhcBw8RK5p1RY3GAiS4kK1SQiZ5DE_0-cYJxTnJWvrTw8y710LdwnXvALSsmVB41kGS3COJqM1n4mPxcgVHit4MM8eorumrLaHSVhH_q0n_MzBpLx-5JNSXu0dFIBuJPVX5vmRBHWX8b3ML3EysrXaiD33A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
مصفاة ياروسلافل الروسية تتعرض لهجوم أوكراني صباح هذا اليوم</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80179" target="_blank">📅 11:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80178">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#ترفيهي
جوزيف عون يدين الاعتداءات الإيرانية التي استهدفت البحرين والكويت ويقدم حلاً للنزاعات كاعتماد الحوار والدبلوماسية.
طيب والاعتداءات الإسرائيلية على لبنان
‼️
ولا اسرائيل منا وفينا
😆</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/80178" target="_blank">📅 10:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80177">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اصوات انفجارات تهز الكويت الان</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/80177" target="_blank">📅 10:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80176">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d313bb45.mp4?token=unLj5C6X44lecTYPGp46d3G1Cvba3ayyj_tXFDCCvbggzCQjyHglb0Cnvbzj9RO_bkIMRtpGcwBAslT5_9V0dKARTxnGh3TDuwauNwt09xuiThgvdBcLqdFwVaZU58Eib6xe_hYeezW23TpkSQMMCH_kOlpJLIGisNfjTHN42LOwAXDCza8cdghnEf7ZkmRcg0jPXXVCki9AYNJmz3-nEdP_InmGxOG-9-VcCO2gLRr3R_Li6FwzmRkwjMMG2_U7Gv2QXy79G2Qplgb73LDU8_PSg9zen9n5p1DMdAQamNRrt-GlIKNwitynOjhSdH175TXhUAz7p24M42_k7_A6HEPzHVBUyPZEK72xXxrP1P33TSYGTl9BeU7Vt0kPmiyxBrTmupPDjuSjDUTizsXY7n1lAnRmQu6M17s0iHwDW6HXBTUkyGpRdluoDlm5f478Dz2rkLCZ8UbYzbl-XmjLmhVCUEo3N4zgMjm592ZxHjfRRl4UhvG4D5UkeHo8v78iH2O8J0I85qbPhc8hqZ_cyaHqxd3BBprO_fFQ1VqkpHQ-gnsp7m8Ek5Hl5L16F2i0egIbzTEjkruccoi6Tcyh49PRmZ9O1GFNu4PWdx7_8H1z9s4GlZSdYKMTccTAjcGMXHorzcNkucG_VFGNGok8Q3C0foXBKDbGAj0QWWYnDRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d313bb45.mp4?token=unLj5C6X44lecTYPGp46d3G1Cvba3ayyj_tXFDCCvbggzCQjyHglb0Cnvbzj9RO_bkIMRtpGcwBAslT5_9V0dKARTxnGh3TDuwauNwt09xuiThgvdBcLqdFwVaZU58Eib6xe_hYeezW23TpkSQMMCH_kOlpJLIGisNfjTHN42LOwAXDCza8cdghnEf7ZkmRcg0jPXXVCki9AYNJmz3-nEdP_InmGxOG-9-VcCO2gLRr3R_Li6FwzmRkwjMMG2_U7Gv2QXy79G2Qplgb73LDU8_PSg9zen9n5p1DMdAQamNRrt-GlIKNwitynOjhSdH175TXhUAz7p24M42_k7_A6HEPzHVBUyPZEK72xXxrP1P33TSYGTl9BeU7Vt0kPmiyxBrTmupPDjuSjDUTizsXY7n1lAnRmQu6M17s0iHwDW6HXBTUkyGpRdluoDlm5f478Dz2rkLCZ8UbYzbl-XmjLmhVCUEo3N4zgMjm592ZxHjfRRl4UhvG4D5UkeHo8v78iH2O8J0I85qbPhc8hqZ_cyaHqxd3BBprO_fFQ1VqkpHQ-gnsp7m8Ek5Hl5L16F2i0egIbzTEjkruccoi6Tcyh49PRmZ9O1GFNu4PWdx7_8H1z9s4GlZSdYKMTccTAjcGMXHorzcNkucG_VFGNGok8Q3C0foXBKDbGAj0QWWYnDRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
🇮🇷
وزير الخارجية الإيراني عراقجي يصل إلى العاصمة العراقية بغداد ‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80176" target="_blank">📅 10:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80175">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098c093505.mp4?token=RSurP7j4vaf7Kk8vBZWpft7MeEhgbRIlGjh6kk_h2hfKQ8ZllWj9Zn8LHb747fBBvVo4UKnOGL4d4VYf3WoGs_a3fKf4JNrZU4HuCk8JoFl2-Rxlc0lbu9x2juWl7RWcoflbAc5vbcfxUIIinhYjMjR7T24FFOEShBym8BXA8K4W-n6_o1trcUceiSDs8Lf7OrXjjf52IyBlXoCxesYdTAkQ0Qs_DJEv2tjL9XzUx5Tsh5rKKr3WpKj9QVwEPyBLhALUuKNgsp-31JR_gwVDtCkV5AU0hg3CgQpZ9vP4RNFUirxLg3qgKY2rMQIhZiHXs_403OUeYuSsfUTA6RgrRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098c093505.mp4?token=RSurP7j4vaf7Kk8vBZWpft7MeEhgbRIlGjh6kk_h2hfKQ8ZllWj9Zn8LHb747fBBvVo4UKnOGL4d4VYf3WoGs_a3fKf4JNrZU4HuCk8JoFl2-Rxlc0lbu9x2juWl7RWcoflbAc5vbcfxUIIinhYjMjR7T24FFOEShBym8BXA8K4W-n6_o1trcUceiSDs8Lf7OrXjjf52IyBlXoCxesYdTAkQ0Qs_DJEv2tjL9XzUx5Tsh5rKKr3WpKj9QVwEPyBLhALUuKNgsp-31JR_gwVDtCkV5AU0hg3CgQpZ9vP4RNFUirxLg3qgKY2rMQIhZiHXs_403OUeYuSsfUTA6RgrRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
🇮🇷
وزير الخارجية الإيراني عراقجي يصل إلى العاصمة العراقية بغداد ‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80175" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80173">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇰🇼
🇧🇭
الكويت والبحرين: ندين تكرار الاعتداءات الإيرانية "الآثمة"</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/80173" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80172">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN0c1-Ap2nQUicUrEhFyy6FRmAYFaj6UOecheIrsX7AAhOyYaOEWbfyloFvuWUEIEZOp3rnyqWJoCTFBb7gMGD9DR6RdcyH7EIywGykZ31S9iU8L8lrna4e6cmgXdCsIFgITdHgUS7pGZICKXjF6Z3iiIzsCkFafGhZGCZAYO_8knNA9-YdUBd3Nb6tx07VX0NG7q5nJMLHCtY5E0jd-Y8Mzw0hIoLL0azMM17RE83xrofCCFqrDrAt85_zqpc_9pFgQYyZWS1Wh_VtqI97Tth0aWvYerpoaCPmMkxdP8Y3kd04t4a3wguKMObjJ6XyDn_QPaKOI_yYsIwtp1RowFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: قد يأتي وقت لا نكون فيه قادرين بعد الآن على التصرف بعقلانية، وسنُجبر على إنهاء المهمة التي بدأناها بنجاح كبير عسكريًا.
إذا حدث ذلك، فلن تعد جمهورية إيران الإسلامية موجودة!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/80172" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80171">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
🔻
🇮🇷
وزير الخارجية الإيراني عراقجي يصل إلى العاصمة العراقية بغداد ‌</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/80171" target="_blank">📅 09:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80170">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc28dca857.mp4?token=UjVV33miE_N5M_2lrxKFrBcoh3-xHSPFGm1CkBdxaEuNKl82I4i98AiMum4WeQLiUnYDIul2pGZ97m90MBYv3Br1EtrXImu5QP08DuNDdlNkx8vUZIBZdV6pQj2ry73uvjoSrhZBdQymUqYCTJNz5fFVWL1Rk2vTxTWxLfPAVGlSpfy1e68J3z15uyFasR4XixnZfosMuVajF3fQOqUAPB3qxlfGIoJxQgIXmlWD2ZNW5UL1T_SThy2NPV8WQWQuexGaan5eZmcPs8iMUgJsfRzTvj0WDuTtYqpDW8HIPxbj7Xwdeqj7q8gHkrUdIw74jd9qnyHHa1vs_lrNi8zkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc28dca857.mp4?token=UjVV33miE_N5M_2lrxKFrBcoh3-xHSPFGm1CkBdxaEuNKl82I4i98AiMum4WeQLiUnYDIul2pGZ97m90MBYv3Br1EtrXImu5QP08DuNDdlNkx8vUZIBZdV6pQj2ry73uvjoSrhZBdQymUqYCTJNz5fFVWL1Rk2vTxTWxLfPAVGlSpfy1e68J3z15uyFasR4XixnZfosMuVajF3fQOqUAPB3qxlfGIoJxQgIXmlWD2ZNW5UL1T_SThy2NPV8WQWQuexGaan5eZmcPs8iMUgJsfRzTvj0WDuTtYqpDW8HIPxbj7Xwdeqj7q8gHkrUdIw74jd9qnyHHa1vs_lrNi8zkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
القطعات الأمنية العراقية تنتشر على طول طريق مطار بغداد الدولي.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/80170" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80169">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامب: إيران لن تمتلك أبدا سلاحا نوويا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/80169" target="_blank">📅 08:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80168">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5b7076fa.mp4?token=k8JvIfNXViqiZ8RujGZEsZ1n6QUAgz1sgNw5H0FiEhWrqlHAXjtFpVxhc3NmjylNCE0OP5MYrw_F4504HFeFG4NVf15Z3H7As9YJHghwsx8kfzh86l9eKjKlCFh1spfy4vOJS7TEHVSAFpcDXaW5b-WdpEaQjT0q8Ri2fATz1V6gIjUffr-cqDNeUXTtYGuK_xqqyCJLmuVNDAK0EcoOjmkueu631gfIKx8Qj-dkxfilxBU7jy245Zu8YLQ3l2nj7kdEr4FT1H0u7Iv55s7IbY8r5zloD4hSnZ-K2kzq08eq2ljEuswh1qIZ0CBjUIAEBx-OiVg_W2yakw1o2Q9kZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5b7076fa.mp4?token=k8JvIfNXViqiZ8RujGZEsZ1n6QUAgz1sgNw5H0FiEhWrqlHAXjtFpVxhc3NmjylNCE0OP5MYrw_F4504HFeFG4NVf15Z3H7As9YJHghwsx8kfzh86l9eKjKlCFh1spfy4vOJS7TEHVSAFpcDXaW5b-WdpEaQjT0q8Ri2fATz1V6gIjUffr-cqDNeUXTtYGuK_xqqyCJLmuVNDAK0EcoOjmkueu631gfIKx8Qj-dkxfilxBU7jy245Zu8YLQ3l2nj7kdEr4FT1H0u7Iv55s7IbY8r5zloD4hSnZ-K2kzq08eq2ljEuswh1qIZ0CBjUIAEBx-OiVg_W2yakw1o2Q9kZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
القوات الأمنية تنتشر في مدينة الصدر شرقي العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/80168" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80167">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36264bd695.mp4?token=sCudE2j237Vh1fYr5GD2BS1J4uYGXFHOiBpavDwC6LA-KK_Bb61l-dWx0r3baqYEQE6AMLPLU1CzdZMEJBCEBsohq12m5Xi1yhAweY0PtoWh8t_lBbqHIlCmMKKdcfLcqp1Q8OrZNNtxvTyVLgH3WRQiQr_lCSpVkvlNNeBjLn3wHG-CeHuFjZTmt9BbNwD92GcFBh8WpWiI1suH28PoSM4oe695kO72A8za20UwVTqUhAEAxc40U7eKItbxWqZv6cQpr5abDfKNxLYlFlohEykpV-Ns2KhhtxLbDfdQ1vs1_F9tgxmZg3q6_GZUYozHNftHdrd0Xla4szHvzYeCU3bZGB-Odewa6amsZMnGLBah5G9B00L_d4kz-yX0hLo3RZQVSUrF9t83qnFwnC5Vlap9RqY5LsMLaF-dfwyaonX0tsETT04-szHTSHUp0oxMO7aV7ybDW8Ex89x3IF1htfjkHQtTvYkXP9OSinapO5LMBWDgiY5cSwaguAYokk8VqDMHb1ObwzViiGuS8RJT_jA4VWXyowazDsCL5eBJAf-5mcqXS4SJaxjRTjQSL-7LCmIQQXLCm281BLpFLzffxRMG66VhQxlWrKorkOI9xDOE9jjfv5mjBZ59MbKz7WTWWtZYdqbLL3iad3QbSV-PrQMA_VPmu1Zaw8Yqt9rLsR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36264bd695.mp4?token=sCudE2j237Vh1fYr5GD2BS1J4uYGXFHOiBpavDwC6LA-KK_Bb61l-dWx0r3baqYEQE6AMLPLU1CzdZMEJBCEBsohq12m5Xi1yhAweY0PtoWh8t_lBbqHIlCmMKKdcfLcqp1Q8OrZNNtxvTyVLgH3WRQiQr_lCSpVkvlNNeBjLn3wHG-CeHuFjZTmt9BbNwD92GcFBh8WpWiI1suH28PoSM4oe695kO72A8za20UwVTqUhAEAxc40U7eKItbxWqZv6cQpr5abDfKNxLYlFlohEykpV-Ns2KhhtxLbDfdQ1vs1_F9tgxmZg3q6_GZUYozHNftHdrd0Xla4szHvzYeCU3bZGB-Odewa6amsZMnGLBah5G9B00L_d4kz-yX0hLo3RZQVSUrF9t83qnFwnC5Vlap9RqY5LsMLaF-dfwyaonX0tsETT04-szHTSHUp0oxMO7aV7ybDW8Ex89x3IF1htfjkHQtTvYkXP9OSinapO5LMBWDgiY5cSwaguAYokk8VqDMHb1ObwzViiGuS8RJT_jA4VWXyowazDsCL5eBJAf-5mcqXS4SJaxjRTjQSL-7LCmIQQXLCm281BLpFLzffxRMG66VhQxlWrKorkOI9xDOE9jjfv5mjBZ59MbKz7WTWWtZYdqbLL3iad3QbSV-PrQMA_VPmu1Zaw8Yqt9rLsR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من تحرك القطعات الأمنية بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/80167" target="_blank">📅 08:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80166">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxCs5y5WufK8XuifOTPoSmIsjHx2jdGqtAR_XNjSkVvlhRF0mvL35zvuJ9vsGRDIOI1T-BOjEkoVfipdLc8y5s3B3ylfQKBSqoJT7GbwFoHcqJtD4OKZMnEY23tvZ2aTeFG_HVcueitILQdjDux3SGgLvc8-0E6cusmzpWhfO8SFdH5LeQKTlVKi1chy2XBOi9fBjuMmiE7IoE7JI58LajQL_tj1j45EXGZs_w6J1GjNYRfg8EwiIYSbkxqcX03A5w5OLta68DhrISsnEsDQ1H0lgw5OWOfrkgFWJFtV86ck87Y1VNmvJdsXZ0sXjoFsxDDd3Q9ZUeMNWxOfg2wdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
تدين وزارة خارجية الجمهورية الإسلامية الإيرانية بشدة الغارات الجوية التي شنها الجيش الأمريكي الإرهابي فجر يوم الأحد، على عدد من منشآت الرصد والمراقبة على الساحل الجنوبي للبلاد. وتُعدّ هذه الهجمات الوحشية انتهاكًا صريحًا للمادة 2، الفقرة 4 من ميثاق الأمم المتحدة، وانتهاكًا صريحًا للمادة 1 من مذكرة التفاهم بشأن إنهاء الحرب المفروضة ، مما يُظهر أن النظام الأمريكي لا يُولي أدنى قيمة أو مصداقية لالتزاماته، وأن نقض الوعود جزء لا يتجزأ من طبيعة هذا النظام.
إن الجمهورية الإسلامية الإيرانية، إذ تذكر مسؤوليات مجلس الأمن التابع للأمم المتحدة والأمين العام لهذه المنظمة تجاه السلام والأمن الدوليين، تؤكد عزمها على الدفاع عن السيادة الوطنية الإيرانية والسلامة الإقليمية ضد العدوان العسكري الأمريكي، وفقاً للمادة 51 من ميثاق الأمم المتحدة</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/80166" target="_blank">📅 08:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80165">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
🇸🇾
وسط إنشغال الجولاني وعصاباته الإرهابية بنبش القبور.. جيش الإحتلال الإسرائيلي:
بالأمس (السبت)، قامت قوات لواء عتسيوني (6) تحت قيادة الفرقة 210 بالقضاء على عدد من المسلحين في منطقة الأمن في جنوب سوريا. سيواصل الجيش الإسرائيلي العمل في منطقة الأمن في جنوب سوريا وإزالة أي تهديد على مواطني
دولة إسرائيل
وقوات الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/80165" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80164">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات تهز البحرين الان</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/80164" target="_blank">📅 07:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80163">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اصوات انفجارات تهز الكويت الان</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/80163" target="_blank">📅 07:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80162">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c81df6c5.mp4?token=LIS8vEIKaIwknKG4qfnVewZAIAIZ4RsFFpJlSq243nguB6B55N9KUajRkYEgtBsZIvpYdpWsrtEhb2DaS-uhQSZ7mLPuvc2UJ8S_kgW1lB0fMcimaii875LNrmKDJ-77EnqPHC2zGrQpuotFbZJA0f_j1LoirPuHdHbi7iTP7xtCFseSHXHVn3GlOqkbAqLQ_QIpvo8oNdWaGKRgsOUXncc1W56uKjFG8xdBZLYGZTXciNfLti6czqu2R_GYA9QtxHH0wMiwQTKicsHXQR8Avri1pIWF5tMwhmWBk0XQWUn8ygH1N-siQ0dD78S7xgBx0JXSJrXtAT44soC3jUjzVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c81df6c5.mp4?token=LIS8vEIKaIwknKG4qfnVewZAIAIZ4RsFFpJlSq243nguB6B55N9KUajRkYEgtBsZIvpYdpWsrtEhb2DaS-uhQSZ7mLPuvc2UJ8S_kgW1lB0fMcimaii875LNrmKDJ-77EnqPHC2zGrQpuotFbZJA0f_j1LoirPuHdHbi7iTP7xtCFseSHXHVn3GlOqkbAqLQ_QIpvo8oNdWaGKRgsOUXncc1W56uKjFG8xdBZLYGZTXciNfLti6czqu2R_GYA9QtxHH0wMiwQTKicsHXQR8Avri1pIWF5tMwhmWBk0XQWUn8ygH1N-siQ0dD78S7xgBx0JXSJrXtAT44soC3jUjzVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين الان</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/80162" target="_blank">📅 07:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80161">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجارات تهز البحرين الان</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/80161" target="_blank">📅 07:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80160">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">استمرار خدمات الانترنيت في العراق على الرغم من تلويح وزارة الاتصالات بقطع خدمة الإنترنت من المصدر مؤقتاً خلال أوقات الإمتحانات الوزارية من الساعة 6:00 صباحاً إلى 7:30 صباحاً،</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/80160" target="_blank">📅 06:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80159">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58da81163d.mp4?token=uF4aZEw8lHOK8EXRwAYa1oMVeYA9oOtZDAQCMf0NBw1KGvSggdGpsTDzE6cDetXJQXkm_yKTxxz7mz3sKn5bA0sLARk-x-dQb0bieuiTc2p6QSGk20FrHdwTbMP1gHrqW6Xl-y-Hr63kTLkbnUbfhPAo0rHWLeXLs-LVb0cfLZQQJpeKoZ4da413roL-BuYF9-ZJlGoxQ7jQqFO72QRHHBSof_AoIVQux400Kok_gdPjauz5GFLA-n5Gm21uP0Xg2y7pfggJl2T8f21CFWUjPpuYvjVe9AUJmrpj0TZTUCptVHmGpzP1psfDGQ-gxcXugNGzKoEa9dKRhqUzxHs9tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58da81163d.mp4?token=uF4aZEw8lHOK8EXRwAYa1oMVeYA9oOtZDAQCMf0NBw1KGvSggdGpsTDzE6cDetXJQXkm_yKTxxz7mz3sKn5bA0sLARk-x-dQb0bieuiTc2p6QSGk20FrHdwTbMP1gHrqW6Xl-y-Hr63kTLkbnUbfhPAo0rHWLeXLs-LVb0cfLZQQJpeKoZ4da413roL-BuYF9-ZJlGoxQ7jQqFO72QRHHBSof_AoIVQux400Kok_gdPjauz5GFLA-n5Gm21uP0Xg2y7pfggJl2T8f21CFWUjPpuYvjVe9AUJmrpj0TZTUCptVHmGpzP1psfDGQ-gxcXugNGzKoEa9dKRhqUzxHs9tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تحركات القوات الأمنية في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/80159" target="_blank">📅 06:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80158">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5o9Xgm02o2GAL5NWLYM4MMpxoR5XtubIAlyIxbSqa0OcHd1sWeBGjPfW_w0bwqvQZr-ghLJ5hpKgmPJrdf4hl-J-OHpr7uuYd8uYzXxV5-pH10XPnnqQ0KqYUaFTFVCKnjnjV_2usgY0aEyhD_-Ogl98cQ6R0C1SVAgIEDuJs0EO6UFbFtzzOXg-x8gauokog-45YygJn7AEJo1vbjgkJvGCTw18GknFA3xKm83JfB6QyeK20-xV_F8mFO7Am3K6EzHFKCB9iSz1TS0jLzr4kS5uRPa6zh3igLyZJM1O-88DdKfzqG_Js0qxSgcKRZ-TTsP5GQo5xQi2iiH5FJZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلل حركة السير بالمنطقة الخضراء</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/80158" target="_blank">📅 06:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80157">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">العملية الامنية لا تزال مستمرة حتى اللحظة .. مع انتشار لأفواج مكافحة الارهاب والفرقة الخاصة وارتفاع عدد المعتقلين إلى ٨ أشخاص بأوامر قضائية</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/80157" target="_blank">📅 06:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80156">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00df836d16.mp4?token=bvZ2-TrUScQVaQ6W7UxeKDkuIR332tSiSZsrdTIbJ88Q2hwwwMTn7lAbzURutpLARk8fm4ckBw6UWYB1H_YDxw-AXA0_2rVbjxNGkJ3p5l6lQ7oy9S79cHGVNvPiCddXSwQOf3SNwZBWVphWjiz6erT0UtTR1ZJ4T--m0rKS-rDzoBuizFNNFdhsSSYnWSJglTr66VehT4MmgVZAsfFGPC25OvCPPIPgSSO9-spj188X9eeu7EZVrIpnc9x1P8Ioge74n8yDL3slzPs5EUPiOm--QqcZIE-vr3tGpH2-NSWYhYW-PvNANfGWlNyjisgmCrXpYmM0dFPNxJ-2sWnOKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00df836d16.mp4?token=bvZ2-TrUScQVaQ6W7UxeKDkuIR332tSiSZsrdTIbJ88Q2hwwwMTn7lAbzURutpLARk8fm4ckBw6UWYB1H_YDxw-AXA0_2rVbjxNGkJ3p5l6lQ7oy9S79cHGVNvPiCddXSwQOf3SNwZBWVphWjiz6erT0UtTR1ZJ4T--m0rKS-rDzoBuizFNNFdhsSSYnWSJglTr66VehT4MmgVZAsfFGPC25OvCPPIPgSSO9-spj188X9eeu7EZVrIpnc9x1P8Ioge74n8yDL3slzPs5EUPiOm--QqcZIE-vr3tGpH2-NSWYhYW-PvNANfGWlNyjisgmCrXpYmM0dFPNxJ-2sWnOKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعادة افتتاح بوابات المنطقة الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/80156" target="_blank">📅 06:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80155">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/994fd7d7a3.mp4?token=uSaRj8NfBX4VvhbQ2thx135v3H06xlK0bUTScRfa-ys_N85QqtpoGmoUiqpm8KemPfXEl3MMJwJqoIa4hr5KdiHU1fpg23wX3VZBambldsNbVOyuMbVK8QNN5sbBHZJpcQ7zJy_2FlwAO6q3Gievo4OdNFHudIzO3vV3MpGHCxqQNT9ECQ5tcKVx-jGCSDUH6GAJjQQe48AzaUReOYlgHSjYvOblIGlbDKVslXbI1XRGysBTWtcgun2eh5nyMY5-jtg6tUT__JYU2HUwub9n1DcovluZ5YNhBSwlBfIr0VvosP2LwVKO1evlMrlrJvp_HjrgqHYQ6XwlPX_Rf3Y0SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/994fd7d7a3.mp4?token=uSaRj8NfBX4VvhbQ2thx135v3H06xlK0bUTScRfa-ys_N85QqtpoGmoUiqpm8KemPfXEl3MMJwJqoIa4hr5KdiHU1fpg23wX3VZBambldsNbVOyuMbVK8QNN5sbBHZJpcQ7zJy_2FlwAO6q3Gievo4OdNFHudIzO3vV3MpGHCxqQNT9ECQ5tcKVx-jGCSDUH6GAJjQQe48AzaUReOYlgHSjYvOblIGlbDKVslXbI1XRGysBTWtcgun2eh5nyMY5-jtg6tUT__JYU2HUwub9n1DcovluZ5YNhBSwlBfIr0VvosP2LwVKO1evlMrlrJvp_HjrgqHYQ6XwlPX_Rf3Y0SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجهة المنفذة للواجبات فجر اليوم " جهاز مكافحة الارهاب ، الفرقة الخاصة ، الفرقة المدرعة التاسعة جيش عراقي " ؛ بيان حكومي مرتقب عن العملية العسكرية</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/80155" target="_blank">📅 06:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80154">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عودة الهدوء للمنطقة الخضراء وسط بغداد مع انتشار امني لجهاز مكافحة الارهاب بالمداخل والمخارج</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/80154" target="_blank">📅 06:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80153">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عودة الهدوء للمنطقة الخضراء وسط بغداد مع انتشار امني لجهاز مكافحة الارهاب بالمداخل والمخارج</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/80153" target="_blank">📅 05:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80152">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عودة الهدوء للمنطقة الخضراء وسط بغداد مع انتشار امني لجهاز مكافحة الارهاب بالمداخل والمخارج</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/80152" target="_blank">📅 05:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80150">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سرقة سيارة نوع جكسارة تعود لضابط برتبة عقيد في وزارة الداخلية العراقية .</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/80150" target="_blank">📅 05:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80149">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سيطرات مفاجئة وتدقيق على الأسماء في اغلب شوارع العاصمة بغداد .</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/80149" target="_blank">📅 05:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80148">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قوات أمنية إضافية تنتشر في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/80148" target="_blank">📅 04:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80147">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
توثيق للحظة إطلاق الصواريخ الإيرانية نحو قاعدة علي السالم الأمريكية في الكويت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/80147" target="_blank">📅 04:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80146">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b80a9e9cb.mp4?token=KJGP4The6HjAtdprw-r6mPDLODWSYOnZve9EPEGJ0omR39kgergvmZAPCnvRTCSpBPyhGflDgFYSxLmnCpKzynwELpyaftWxRAcuvJzbiWUyftFnBwcRJmZ8jHOqI3f3EJQ3p1xdkI4DDqrTmnURtIBrrwWoZ7iUMqAobbjrhNM_qMBEiyFOcYLRfv7OsrndkKwbhfFLC5az1gWUN7UOjy9tfXCWpByD14l9Ap-Bi8j4relnCm0IGIUqSYs5yLuLGY3eS8sWutUn1KsyrvSy4uK7UynY_6pNu4H7itQhzFzG9O9zaxFH6-tbKYbC2ips52ZZ5rbUheQtyfVb7xL5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b80a9e9cb.mp4?token=KJGP4The6HjAtdprw-r6mPDLODWSYOnZve9EPEGJ0omR39kgergvmZAPCnvRTCSpBPyhGflDgFYSxLmnCpKzynwELpyaftWxRAcuvJzbiWUyftFnBwcRJmZ8jHOqI3f3EJQ3p1xdkI4DDqrTmnURtIBrrwWoZ7iUMqAobbjrhNM_qMBEiyFOcYLRfv7OsrndkKwbhfFLC5az1gWUN7UOjy9tfXCWpByD14l9Ap-Bi8j4relnCm0IGIUqSYs5yLuLGY3eS8sWutUn1KsyrvSy4uK7UynY_6pNu4H7itQhzFzG9O9zaxFH6-tbKYbC2ips52ZZ5rbUheQtyfVb7xL5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إغلاق تام لبوابات المنطقة الخضراء وانتشار دبابات أبرامز بالتزامن مع حملة اعتقالات طالت عدد من السياسين بتهم قضائية</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/80146" target="_blank">📅 04:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80145">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/911e440568.mp4?token=UTT6lTpWhV7VBjcqbegUPSLl71IncC-_rJBThX1O-UGk6uD63KW2SxlOrSkIgyyrtuid6zS-dgZ0Cw1fEBFID2KOZ9R9-AflJH_cZGpsW7QoXMz3X6_LsLUm8WomLzvMX3DguvEAu7Ivy4Z1MHXNuMqYZQFhQlUw7WjJIa3XSjlr-JwWA_CN9LemVi2oSHEHJq1krBiPWMUxkTv5HM9TRd1OZwWo0tBGcTd83Zu9q7IGYFm8Bd61EvvL7dEy3X-3qBdh9bxsicUG5SdgzycGcVkkjU8f-17fzO2GBfQ60fbcK8ZBkloVJXu4W4lLQBtWZzT0FQ6_LoPezwLyBWvQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/911e440568.mp4?token=UTT6lTpWhV7VBjcqbegUPSLl71IncC-_rJBThX1O-UGk6uD63KW2SxlOrSkIgyyrtuid6zS-dgZ0Cw1fEBFID2KOZ9R9-AflJH_cZGpsW7QoXMz3X6_LsLUm8WomLzvMX3DguvEAu7Ivy4Z1MHXNuMqYZQFhQlUw7WjJIa3XSjlr-JwWA_CN9LemVi2oSHEHJq1krBiPWMUxkTv5HM9TRd1OZwWo0tBGcTd83Zu9q7IGYFm8Bd61EvvL7dEy3X-3qBdh9bxsicUG5SdgzycGcVkkjU8f-17fzO2GBfQ60fbcK8ZBkloVJXu4W4lLQBtWZzT0FQ6_LoPezwLyBWvQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر خاص لنايا: اعتقال ٣ قيادات سياسية مهمة في المنطقة الخضراء بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/naya_foriraq/80145" target="_blank">📅 04:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80144">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80144" target="_blank">📅 04:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80143">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a37338d56.mp4?token=RGEFxit2UZw_Bd6M3NVwq2Ikzs8OqeSt3nGDLLciCQ5I6oBWGlh5wY6S1c_TlzZAb_M9vHagZlrUOFHdZyR9TVC4vKy1cEGXK9ASzjP-zOFJ5F2adj99FzzpTekR9qPSTv_KWGwCwlduiJB6Ji9xpTod4Tj2h_uhhYzdU5c-eZGyTBKlkynrNQAC5ZCytD5UXgPyFsNrF_6WCTVVoamD6WHi_gtHQ4mjqBMTFKB0fjP9fVnXDLCpELsZNmlweXdwAEwX2u870tYXNmYCDRl65oQjYM2dF0AaRrTJOr-ZSiUMpIg7Hq7S1oRYTqnaogfb963xf6MDV6bKqqi-0Ja_Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a37338d56.mp4?token=RGEFxit2UZw_Bd6M3NVwq2Ikzs8OqeSt3nGDLLciCQ5I6oBWGlh5wY6S1c_TlzZAb_M9vHagZlrUOFHdZyR9TVC4vKy1cEGXK9ASzjP-zOFJ5F2adj99FzzpTekR9qPSTv_KWGwCwlduiJB6Ji9xpTod4Tj2h_uhhYzdU5c-eZGyTBKlkynrNQAC5ZCytD5UXgPyFsNrF_6WCTVVoamD6WHi_gtHQ4mjqBMTFKB0fjP9fVnXDLCpELsZNmlweXdwAEwX2u870tYXNmYCDRl65oQjYM2dF0AaRrTJOr-ZSiUMpIg7Hq7S1oRYTqnaogfb963xf6MDV6bKqqi-0Ja_Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تم استهداف قاعدة علي السالم في الكويت</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/80143" target="_blank">📅 04:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80142">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔻
مصدر خاص لنايا: اعتقال ٣ قيادات سياسية مهمة في المنطقة الخضراء بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/80142" target="_blank">📅 04:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80141">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
مصدر خاص لنايا: اعتقال ٣ قيادات سياسية مهمة في المنطقة الخضراء بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/80141" target="_blank">📅 04:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80140">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">توثيق أخر يظهر كثافة الإنتشار الأمني في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/80140" target="_blank">📅 04:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80139">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgecF8CdQqkhGeKojyMazcBEuMTkHPwSfXHWS53ER6E3FiVbL2dNE-gDLdaYLLcdsOP2xTnUIQXqllDay23r8T9drXslVFj1RxlBSWdKs_S2K0ExZ1vZQ4XztIiDTHQbVIui6VCxxJyrk5bjnbciHlpVUplReuRNS6n5Q1sP3UmpVUNb___uOHGLw_tcnLDO5b00xVL4Qg08b9QYkfxSWRWTSkJMTP685WBlI2VBd7zqpD4s6U1m7nB6Qu2I_GkqJUBQ1mYmUpQA-rj1i0c2KgMYsfWuTwTfLXg7vs1ji9kY3QMHmUOM--ZXKpaDOF2CUcY2GTkTnx4mK5sa46TezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العلاقات العامة للحرس الثوري الإسلامي: أيها الشعب الكريم لجمهورية إيران الإسلامية؛  خلال عملية صاروخية وطائرات مسيرة مشتركة بين الساعة الثانية والثالثة فجر اليوم الأحد 28 يوليو، أطلق أبناؤكم البواسل في القوات البحرية والجوية للحرس الثوري صواريخ باليستية وطائرات…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/80139" target="_blank">📅 04:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80138">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f860d0e2.mp4?token=ndpJZAUZMFf9VmKG4-us9JFd8lvStGllwdYHz_BqrcDzlYkxn4Aho_0fJqxiuDVCHqOF3DVS6YRADVGPCv2DBzoYoPrgM9dfvZwpxCr1rkxhDBUpoWK4lw6mpP8L7ieqdEzQ65a698y99N-IwMq6AtRX-rf7QJ25mAc340YVjh6oUio6CJfxLEACscXpTs9mZkr46Mp3kaj3OfQwuDCyATLp8qPyqZ4zXACb7SELXdlDy9bH5TjKMdbU2_xXJCr0fQhPLudf3JOFPT201pMvWTIjgbQadKn3bNI3Sxfqijcma6mLTd2A36lNg-OCvnIWCG1sTjz6Mik_8abYnOZuYAMsCGp3AroLxCLjr-JMhilONQPxV_hsy8bTjWoYJeVjy5HhC8wffHRXIy6cGmEqGmws4lndmSufeSCp9-OZIqbJYN_RM6ivI5uqj-Nb0Zzb-XMSdRrngE775g7PCj38T-A1dCw5HpZqikL9LaVILFU4sr6ZVo4v7fbRa_OA9I9ZP408nOi3QRopEyisTMa5UlIduXxWoBMaQ1XSRfR_1PNPOMzgkcZyBRWsLpSvHnOyqBGAb64h2QaUcnmILBJ74rBKcwRohRQoMm1F_W-ULHrKq9rzoOgOLjDwxCMj3y0X0ROQwf8o4euQqxQOX_YJYct6XGD-JzNalH9hsntikLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f860d0e2.mp4?token=ndpJZAUZMFf9VmKG4-us9JFd8lvStGllwdYHz_BqrcDzlYkxn4Aho_0fJqxiuDVCHqOF3DVS6YRADVGPCv2DBzoYoPrgM9dfvZwpxCr1rkxhDBUpoWK4lw6mpP8L7ieqdEzQ65a698y99N-IwMq6AtRX-rf7QJ25mAc340YVjh6oUio6CJfxLEACscXpTs9mZkr46Mp3kaj3OfQwuDCyATLp8qPyqZ4zXACb7SELXdlDy9bH5TjKMdbU2_xXJCr0fQhPLudf3JOFPT201pMvWTIjgbQadKn3bNI3Sxfqijcma6mLTd2A36lNg-OCvnIWCG1sTjz6Mik_8abYnOZuYAMsCGp3AroLxCLjr-JMhilONQPxV_hsy8bTjWoYJeVjy5HhC8wffHRXIy6cGmEqGmws4lndmSufeSCp9-OZIqbJYN_RM6ivI5uqj-Nb0Zzb-XMSdRrngE775g7PCj38T-A1dCw5HpZqikL9LaVILFU4sr6ZVo4v7fbRa_OA9I9ZP408nOi3QRopEyisTMa5UlIduXxWoBMaQ1XSRfR_1PNPOMzgkcZyBRWsLpSvHnOyqBGAb64h2QaUcnmILBJ74rBKcwRohRQoMm1F_W-ULHrKq9rzoOgOLjDwxCMj3y0X0ROQwf8o4euQqxQOX_YJYct6XGD-JzNalH9hsntikLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات أمنية إضافية تنتشر في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/80138" target="_blank">📅 04:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80137">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366e2bae2f.mp4?token=usS1gle-kk6ZSMPKCA2bYMTf52_pbrdxWgWHLyz-TVPpnodvu-ua0cfgiOuGx9tJ2mjKrOh9qvPKJRcnRTlPUv21CERBir581HppUOA2CnrVNPYTp9SRbEl9v66rGskFWcuPkQu7-R_sfG4tecyEEdvjeghynHSpb87AQkK7e8DbGP-Yi3fRYPWyFRmj1JjNLVm_CcFuxsfvT4IqnrOp_lPhiyPkgmjduYdx8PKoplMCIhuA8-snaLiedEOTm5cWNTUkiAau4KBrJu3UUhqsLJ5CXxIsr1nhEtGiRvG49B6U1Y3fi_igI8b09r7-li12F7UKlZm6A9A39dWRsI9RT4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366e2bae2f.mp4?token=usS1gle-kk6ZSMPKCA2bYMTf52_pbrdxWgWHLyz-TVPpnodvu-ua0cfgiOuGx9tJ2mjKrOh9qvPKJRcnRTlPUv21CERBir581HppUOA2CnrVNPYTp9SRbEl9v66rGskFWcuPkQu7-R_sfG4tecyEEdvjeghynHSpb87AQkK7e8DbGP-Yi3fRYPWyFRmj1JjNLVm_CcFuxsfvT4IqnrOp_lPhiyPkgmjduYdx8PKoplMCIhuA8-snaLiedEOTm5cWNTUkiAau4KBrJu3UUhqsLJ5CXxIsr1nhEtGiRvG49B6U1Y3fi_igI8b09r7-li12F7UKlZm6A9A39dWRsI9RT4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أعلنت القيادة المركزية الأمريكية (CENTCOM) تنفيذ ضربات جديدة استهدفت مواقع عسكرية إيرانية، رداً على هجوم بطائرة مسيّرة استهدف ناقلة نفط قرب مضيق هرمز. وأكدت أن الضربات شملت أنظمة مراقبة واتصالات ودفاعات جوية ومخازن للمسيّرات، مشيرةً إلى استمرار حركة الملاحة…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/80137" target="_blank">📅 04:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80136">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الحرس الثوري الإيراني يتبنى الهجوم</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/80136" target="_blank">📅 04:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80135">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الحرس الثوري الإيراني يتبنى الهجوم</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/80135" target="_blank">📅 04:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80134">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تم استهداف قاعدة علي السالم في الكويت</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/80134" target="_blank">📅 03:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80133">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تم استهداف قاعدة علي السالم في الكويت</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/80133" target="_blank">📅 03:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80131">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EE3MRRNiFl4RrwZDJdLmISftWL0FEJTGl8tmytlml2JW1VfGXoTTOkj8-d5GpoKAooDpqWl-LXsfDNduUcZdUKO33_1tCDVafz6UkwLayeJ0ccL5qMsCFjKEIL8wByDjx95alZJDKaif4KXx4SANj-9DhNiIFsSfWFizWeyJOXtAVw3yIp2wdKhNVeXd_iNBR_ozMDzWCtSEX0huhh-6TysiHd2G_9Er5-RDR_5uJiVbHvwPDh5_gexKUbMEZ-peJIU-UVoTR1BMtEv-ak07eTxvzqdPx0uu64kqlq46WJ6SFj6Q0AqcZWF2zuirhPj0CBKnc22SlqrBNTGLnCRwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRhl0gGp55xbplU_S7usqPWbHXFXDWbsVNG20OvdorTJY6sVgbGw7znDJhuejXPUkHKSNx6LSwRvdwra2cCT0SjKWk727zpC8gdGiElo_JHoesBYweLJFELEt6dgq6mx-3ihcc7lRAJLTbc9ktI-KHDeVp29uZHuwdAxwdk5qGehUOCM4P5s1i2pQmPP28zHuznDFSR5WTeb6H6uGf5yhLYFRFoDbO8SrueP3y22XXx_yQYPdhxEgAZ5Ob8zVW6dvCQgJgJwDat7lIED4VIfhdY-KpIx4x-8M18ERbKayhMlnbCtKL0NROec-27O3Sew2q2AGVt-obCjdYJpfciI7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صافرات الإنذار تدوي بإستمرار في الكويت عقب هجوم صاروخي وبالطائرات المسيرة</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/80131" target="_blank">📅 03:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80130">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">موجة صاروخية جديدة تنطلق نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/80130" target="_blank">📅 03:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80129">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/80129" target="_blank">📅 03:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/80128" target="_blank">📅 03:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71aa5ae7b8.mp4?token=a6_PhDMupf-Ae1VNZCCGBLkysqsDQtMND2g6_bSPU8inFG6hlCO_uhNnJmOjN0Sx-s7Els_y8NepGVRn5CfNg2zHYXfKA-gR3NExODM6GJwBY9In1TrzCUDZRhy51n1W3T2vQJdujFe-CuS5YxxwY3OLbnkVWLYBNNLJzcFUAvykiScngsCS0hy5mKdXgt9VEAKE0cbUVJfmM4d6QZmelSdlc_I99e7gPHsQnlnVye4-JHaU0-IbKsWH8pNP4th0Xq-0aSK93gYK0DvFqYkr_sTPc6_wWDy0SBQCv8irhCYL7aWD0Yu6m2RyISfK3Y37HeWvJbU2p7YxIlOpSz9-Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71aa5ae7b8.mp4?token=a6_PhDMupf-Ae1VNZCCGBLkysqsDQtMND2g6_bSPU8inFG6hlCO_uhNnJmOjN0Sx-s7Els_y8NepGVRn5CfNg2zHYXfKA-gR3NExODM6GJwBY9In1TrzCUDZRhy51n1W3T2vQJdujFe-CuS5YxxwY3OLbnkVWLYBNNLJzcFUAvykiScngsCS0hy5mKdXgt9VEAKE0cbUVJfmM4d6QZmelSdlc_I99e7gPHsQnlnVye4-JHaU0-IbKsWH8pNP4th0Xq-0aSK93gYK0DvFqYkr_sTPc6_wWDy0SBQCv8irhCYL7aWD0Yu6m2RyISfK3Y37HeWvJbU2p7YxIlOpSz9-Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/80127" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f975085a0.mp4?token=F6pjvsXkvq4cYF_KXJua0USjPlgoe-kQIEQAcJJJ9byzvMRcwok1hcjaEzLJWVz1UXu-__bm_0UpDMgDpaxoMJIvGChq660fVps7cPLPm39GTao5DPI6OHphLRO_arTtEueZCyWMuxPpqsVSxMXCsnbUQK_V01tY6PzXe2P4Yrb0ocrLXNUdglD0w7srYcgtzFFvn8x5RDYFzCYp9JBTgP_8gJQLu9dFNrTTpyiXGUyHp26OiOPankMgjIPl5Vl5ZhAnX-oSA3NTB_Ezg8s7ZYOQ976O-Xa0OERV1HoMm5u82H6OQcud_WyMGMmzk4vjkDIM2WInk_Hpt4nYVrx9ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f975085a0.mp4?token=F6pjvsXkvq4cYF_KXJua0USjPlgoe-kQIEQAcJJJ9byzvMRcwok1hcjaEzLJWVz1UXu-__bm_0UpDMgDpaxoMJIvGChq660fVps7cPLPm39GTao5DPI6OHphLRO_arTtEueZCyWMuxPpqsVSxMXCsnbUQK_V01tY6PzXe2P4Yrb0ocrLXNUdglD0w7srYcgtzFFvn8x5RDYFzCYp9JBTgP_8gJQLu9dFNrTTpyiXGUyHp26OiOPankMgjIPl5Vl5ZhAnX-oSA3NTB_Ezg8s7ZYOQ976O-Xa0OERV1HoMm5u82H6OQcud_WyMGMmzk4vjkDIM2WInk_Hpt4nYVrx9ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبابات ومدرعات تجوب شوارع العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/80126" target="_blank">📅 03:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80125">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">منظومة الباتريوت الأمريكية تحاول الإعتراض</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/80125" target="_blank">📅 03:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80124">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/80124" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80123">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الصواريخ الإيرانية تدك الكويت</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/80123" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80122">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صواريخ تنطلق من إيران</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/80122" target="_blank">📅 03:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80121">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ada82ae90.mp4?token=gRT1oh3Lagd8p3vI-mC46Lb_ajElt9vqUVz7ByECtYyMB2N1dQ1_gwdOpyVvCTNQPsVCs87-e_lc-fSvLYp8M-LrArx6lhHNkP9QVUXHzgEeD_M5gE2H6KR-ltESqGcj3ChpW-B590Vh01se5oH35T-f1kB-wS_KyKnr79gBLFcdCctEvm7NZ5AaU9VR7EnqIJxtYjGU3XL4Zczsif4ijgS9D0GHI7bIiAjTXdKZjUUhV2ZomQkQPQ8_yPS5JInqqE7SeNzXSWfcoMoc1TbYczZaBoCDb4C_cjwEFgjoh6-UEyLYhw1iQa-y8Lw0he1843U4YnoowfKyHxZmCLSWeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ada82ae90.mp4?token=gRT1oh3Lagd8p3vI-mC46Lb_ajElt9vqUVz7ByECtYyMB2N1dQ1_gwdOpyVvCTNQPsVCs87-e_lc-fSvLYp8M-LrArx6lhHNkP9QVUXHzgEeD_M5gE2H6KR-ltESqGcj3ChpW-B590Vh01se5oH35T-f1kB-wS_KyKnr79gBLFcdCctEvm7NZ5AaU9VR7EnqIJxtYjGU3XL4Zczsif4ijgS9D0GHI7bIiAjTXdKZjUUhV2ZomQkQPQ8_yPS5JInqqE7SeNzXSWfcoMoc1TbYczZaBoCDb4C_cjwEFgjoh6-UEyLYhw1iQa-y8Lw0he1843U4YnoowfKyHxZmCLSWeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبابات ومدرعات تجوب شوارع العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/80121" target="_blank">📅 03:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80120">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">صواريخ تنطلق من إيران</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/80120" target="_blank">📅 03:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80119">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات وصافرات الإنذار تدوي في البحرين</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/80119" target="_blank">📅 03:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80116">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdgoJEZ-_1kWk5tRz1ejEHVNKz2lImlFhuUrdmvLANIsPxxgzKBj3Y4CTN5pCTXvZ-KRp7GpETkTyBpTx00Ba9ekUP-mewUHLl0QZugVnlH-gy6AMNQ1Oys46oUPMOHxb2fvQjF99zEr81FLhW1c291WRXpf5svqE45F-CCYqWqC5Nc--HdfV08-qGKbWi9i5VycwkvVoTZzKYDmJGqNHaxZ10uaP0LVnpH7psyBJHd3hqQcBQ8i7HAB4I-yGSDu-sbm9CEHwLPLhi5iSSO5FW5kQAA46WSDSAzTObcRBX1tD0De_7TcRkSG6hcRh4e_Qc8X9W6wmbMjcrqLy57vfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d3784e6c.mp4?token=WJxhOn03zwiHqEDaA-FadjTjiA8PTxp_qC0TuXiIo4Pj2b8NIS-u74J7iLICaw8GpSCxNmTOW4eVhzhHuRyeqRE6EUcsUyeL3Wpt3NtYRP0hMXKHK_mtN9D8a178V9BIGQ3SH1aFK7WsbT5nX_xpCHxDUGlMkW80TguKWuhGcClfz7YHZ7BHxHDoVPMWQk9itA0d3qaZz6p3EfS-i-9WuahaqNiS7xc5TJzgyCBMAD-Jjht_Tk1p-d8rOqNPNKIuVdLhJvH-S4eaaIpY4PwnU8C_6V0OEUR12fWIJogsd44Qm9sIeaCSU9tP3-m1xU311ytMiUlcDUzIcfO2WObjPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d3784e6c.mp4?token=WJxhOn03zwiHqEDaA-FadjTjiA8PTxp_qC0TuXiIo4Pj2b8NIS-u74J7iLICaw8GpSCxNmTOW4eVhzhHuRyeqRE6EUcsUyeL3Wpt3NtYRP0hMXKHK_mtN9D8a178V9BIGQ3SH1aFK7WsbT5nX_xpCHxDUGlMkW80TguKWuhGcClfz7YHZ7BHxHDoVPMWQk9itA0d3qaZz6p3EfS-i-9WuahaqNiS7xc5TJzgyCBMAD-Jjht_Tk1p-d8rOqNPNKIuVdLhJvH-S4eaaIpY4PwnU8C_6V0OEUR12fWIJogsd44Qm9sIeaCSU9tP3-m1xU311ytMiUlcDUzIcfO2WObjPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من الإنتشار الواسع للقوات الأمنية في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/80116" target="_blank">📅 03:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a323ca8867.mp4?token=kHgTciw6h3kwFzotYsTfjJQvCnjd4CeYblSNi32JgU8JiXZQrJZnBLHeeqn_tq1i_a7vHqLvAsZncTTw-zyte2horT4iYfeUwCOvq4xj6t2XvwwcyBKE09Rr3xAshV0OK33FLZoDsVruYOQ4gs24mt5e8fsKUp0Gg-60Onux6BSQxlW0NK4j0ocfMnLMNzfbuv2HoMWgRU2sVV_YLxh1JL0-AGRJfBR6liQbXRD2rlOPpGf4c4hjjVCb-Z-PhYbJP3s7PZckRV5iVS5ldPhDCVFuiE4NxqMloL_mR10Ymdow4a8r9hRpDszPG56GlBXLY9VnPqNqVyhOVYJGD7ao6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a323ca8867.mp4?token=kHgTciw6h3kwFzotYsTfjJQvCnjd4CeYblSNi32JgU8JiXZQrJZnBLHeeqn_tq1i_a7vHqLvAsZncTTw-zyte2horT4iYfeUwCOvq4xj6t2XvwwcyBKE09Rr3xAshV0OK33FLZoDsVruYOQ4gs24mt5e8fsKUp0Gg-60Onux6BSQxlW0NK4j0ocfMnLMNzfbuv2HoMWgRU2sVV_YLxh1JL0-AGRJfBR6liQbXRD2rlOPpGf4c4hjjVCb-Z-PhYbJP3s7PZckRV5iVS5ldPhDCVFuiE4NxqMloL_mR10Ymdow4a8r9hRpDszPG56GlBXLY9VnPqNqVyhOVYJGD7ao6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر امني لنايا: إن غلق المنطقة الخضراء في العاصمة بغداد يأتي لغرض تنفيذ ممارسة أمنية، ولا يرتبط بأي طارئ أو حدث استثنائي.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/80114" target="_blank">📅 03:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات وصافرات الإنذار تدوي في البحرين</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/80113" target="_blank">📅 03:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80111">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔻
قسم بالله
🔻
قسم بخدا
🔻
We swear by Allah
🔻
مونتاج نايا:
#شاركها</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/80111" target="_blank">📅 03:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80110">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
مصدر امني لنايا:
إن غلق المنطقة الخضراء في العاصمة بغداد يأتي لغرض تنفيذ ممارسة أمنية، ولا يرتبط بأي طارئ أو حدث استثنائي.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/80110" target="_blank">📅 02:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80109">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egIMNQWpVswlepa9IWUNBWixAki5ZnBEgjAWu9GPXxzk9Gdh9HxLllKESxPw23gJceu4sInEa1FblYdCOwf9JFKMabtEo0RNPaten54VDGF8ADVi-cQY_VZt9Qvlg6lPjMUa9DtYPmDyV98Fep313sIdR1ftcwbVEaLvvQsNwmFB-1efAwiTP-_WEW8ir3M5GSReDRi1NDwIGoIBoIk5LILlryLIxqXZ9xIN7BQw-Wn9Y9sEBIH8FJFJDamtFZp0YjBIr4gTVumIKukZd4C0jIBWYkDBT_DWPV_7HSO5pH291cJZXkgAt0drpkomsP9ZEob3hGAIEOj4uAxOx8qZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامب
:
«شنت طائرات الولايات المتحدة غارات على مواقع تخزين الصواريخ والطائرات المسيّرة الإيرانية، ومواقع الرادار الساحلية، لانتهاكها اتفاق وقف إطلاق النار، مرة أخرى! من المحتمل جدًا ألا يتعلموا أبدًا! قد يأتي وقت نعجز فيه عن التحلي بالمنطق، وسنُجبر على إكمال المهمة التي بدأناها بنجاح عسكريًا. إذا حدث ذلك، فلن تبقى جمهورية إيران الإسلامية موجودة! الرئيس دونالد ترامب»</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/80109" target="_blank">📅 02:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80108">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1-Wc7bNYz29MU7UXuR8Mfmq2Ikl53Ai9RCfsXaUm8QtVY0H_uxHowaTE_AO-QXDYmAxpVg1Zj6NRdclpL8p-hn5qBbjQm6bW1IrGF9vGxOafSy7_GwWslQ57XhilGavv7w9Ahma1jebIJ2EH283e59g_6gCXuLBMFR2Uu9J5XwlnNGJXJ9NZQFEWEXhDL52YFlKzEsJ2AXN6Jsz4r0qdQc9wgxSwQEbh8Hz3-QX-MRnjzbeBkt0TsKsPp4TIoB7gt06uwzVjFaMKHPpfWrj35LR_FEaXR8woycAUPE0OZSC_3f-w5uVgsxPXgFmBjVBaRmRNmVZ7ikI139Lq65IOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
‏نشاط مكثف لسلاح الجو الأمريكي في الشرق الأوسط حالياً.
‏يوجد حاليًا حوالي 13 ناقلة وقود تحلق فوق عدة دول في المنطقة، وخاصة فوق الخليج الفارسي.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/80108" target="_blank">📅 02:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
مسؤول أمريكي: أن الضربات الأمريكية على إيران "اكتملت".</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/80107" target="_blank">📅 02:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80106">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔻
دوي انفجارات في ميناء لنگه وميناء كنگ جنوبي إيران</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/80106" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80105">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
مسؤول اميركي: ردت إيران الليلة الماضية بشن هجمات على القوات الأمريكية في البحرين. وأسقطت القوات الأمريكية والبحرينية تسع طائرات إيرانية مسيّرة هجومية أحادية الاتجاه، دون وقوع أضرار أو إصابات.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/80105" target="_blank">📅 01:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80104">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
مسؤول اميركي: الجيش الأمريكي ينفذ جولة جديدة من الغارات الجوية على إيران الآن، رداً على قيام الحرس الثوري الإيراني باستهداف سفينة في مضيق هرمز في وقت سابق من اليوم. الضربة الأمريكية الحالية أكبر من التي وقعت الليلة الماضية.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/80104" target="_blank">📅 01:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80103">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔻
مجددا سماع دوي إنفجارات في سيريك جنوبي إيران</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/80103" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80102">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/80102" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80101">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/80101" target="_blank">📅 01:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80100">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/80100" target="_blank">📅 01:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80099">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8QCNVGSVGaWCsXbj98yNBcE6yusoEDxK2Jd6WHBjnw4Ex0cF8HXGUaFDlY52VZiSWs3mJE7Z_cpBPtn2NovPKLHTFZliM7WF9YNIYuc7myeoHdAaClndqu8R8pwpRfhtD5sQyOOQlchmnrEdWflKY1ZRC-ONHZ-n14tcwSKZkwR0zZBUFMvLL9bixYuG3jimOE5aKF5rd1Vy36tCRWdieUSooqdYAyFDs7hoMKIam0dHKXrtPZQcxyR5lT6pjyyLoS1QTxXpW251Yu0TolmRJI-8mNayzcUBPicax5RCYWIp9KQF3ghwVVfOZyAOdQMfiX1UDvQ1Yz9m0UtmruqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اختارت الولايات المتحدة ناقلة نفط للتحقق مما إذا كان ممرها الملاحي في المياه العمانية لا يزال "آمناً".  كبش فداء
😂</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/80099" target="_blank">📅 01:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80098">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
غارات تستهدف برج اتصالات في قرية طاهروي بمحافظة سيريك.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/80098" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80097">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/80097" target="_blank">📅 01:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80096">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/80096" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80095">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇯🇵
زلزال بقوة 5.6 ريختر يضرب اليابان وأصدر علماء الزلازل تحذيراً من تسونامي.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/80095" target="_blank">📅 00:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80094">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjrhFZWHvAyvGIBzN-O_VZ6--rNchViLYXVI4pq2XjYMwgQj3KAwonaIUzQQ_byYpe4UqhaWu9XTNQCYbn2Gx8f4Yj2hSeTWHAdRaIyjX9n479AdBp6p1vC99V8pfUgrJPH2c7wNjdu2-hwwpgHNMicJcLFqrmc24tGhEx9duWTsaysS5UAhAqChjjCKh2mr9s6c_9eGlpvZpld23HONB5FzAYPK63-6RnmAQOIGdAKu3RCEvXlnx77LpaTR8A85aQLiiFOqSDjMQRpv5cf2TGS1dDZp1dotLLOfi6Z0RZvpLHzjsaNvTzD9CR2j4fhowPtSSi--3C19_CNpogNy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عُثر على جثة أحد عناصر قوات البيشمركة التابعة لحزب حرية كردستان (PKK) ويُدعى سوران محمد زاده داخل أحد الفنادق في مدينة أربيل.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/80094" target="_blank">📅 23:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80093">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQl0Ec32BeV1aAB2vCJdcGmjkqGFIt1PrizfwC07B161zz-JOO14Crn9lU0_LGt8NxKwMphmKqGgwWcj9Q7bOGNBVmgAuKj2VQbSYViga1Ev9cibf15AcQbeZK3ykybJ-zpXKLzM4oLlciIMHj4n-bKoFUpjMsnsr-LYZtInckBunvzDwZcmBAPY6_CzPuJE7hMGz8WekUTMY4dhqY9o9NtlonfYfLDBDFsOJ9tZjt4K4Wb-LrhyVBVBPHgcBwRuN518Sy4lZuJC9aEQ-w6rPWxc4dCv9JRULuSGPJ0SrM4qaMJnt3qBQGO63rfa2nh2AzR56w_ABceEkZEtyC-nrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اختارت الولايات المتحدة ناقلة نفط للتحقق مما إذا كان ممرها الملاحي في المياه العمانية لا يزال "آمناً".
كبش فداء
😂</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/80093" target="_blank">📅 23:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80092">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
‏زلزال بقوة 5.6 يضرب سواحل أراغوا في فنزويلا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/80092" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80091">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تحت عنوان: "قوموا لله"
🔻
تعلن الفعاليات الشعبية والوطنية العراقية إطلاق الوسم الخاص بتشييع السيد القائد الشهيد علي الخامنئي على مختلف منصات التواصل الاجتماعي وذلك بالتزامن مع قرب وصول جثمان الشهيد في دعوةٍ واسعة للمشاركة في التفاعل وإحياء هذه المناسبة عبر الفضاء الإلكتروني.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/80091" target="_blank">📅 22:49 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
