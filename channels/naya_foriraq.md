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
<img src="https://cdn4.telesco.pe/file/KvMRwPuDtpbIO-7p1sCDSzxRBmR0cXQo5tlUFByk0WVBLCxPyft15WxNId2Hy4ZlqV7fp-IcH-9du0EfXk_ecw1e6GKIb3s2K0ICLqzz4iamRC1lWURO6SgizKpTf4vUWhhYMKkKQ20NCEQQ7kFiLxPG6exLxN4odnvlmlxg-Ob0kTW070k1b0PwpSurZWej-gT8E31UHb8ZKRyijobrC9kGcH2ZjZfbbTGpa8tD5qMnN68hhnk8Sn96maUsNiUasZk2bS0x9EDPChXTt--3yC_LEVa3s92UjlEX34r364uVojQTUPU6TxKqTRndFtMpaAbpihaFoaRkhp3sP7wh4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 00:24:30</div>
<hr>

<div class="tg-post" id="msg-92210">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47151339e0.mp4?token=bP7SKJDPvWDOwd_WJyhcelxyKT9YX-KllA1cWK6_Lbf33hg1piVtfkmYlFoxel0k0PoLBXF28Fw0Rpkkwx-4h7LOL4yILMSGm_LpIFRupTwrPIlPs5SuAL_f7IqjDkVNfd01cWzxofWkIRa2pcFFXR9Xm0Gggv6Dt3_NLOGMYophgQEoT3GzqoK42wwmT0EOEcXst91P-vDmJsTFFJi0C8QwDImJQWjBXhhLpd2Gy3xy2FCe9UQYG6WYLljahoZXNUXgIagJiPLCKVqbsxQQHxRUa4Btwgsf9SCMpY3ljKNepRS7w1IzHA0gCS6F8WmKKCpf2hgl1RTwLGVktf4mrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47151339e0.mp4?token=bP7SKJDPvWDOwd_WJyhcelxyKT9YX-KllA1cWK6_Lbf33hg1piVtfkmYlFoxel0k0PoLBXF28Fw0Rpkkwx-4h7LOL4yILMSGm_LpIFRupTwrPIlPs5SuAL_f7IqjDkVNfd01cWzxofWkIRa2pcFFXR9Xm0Gggv6Dt3_NLOGMYophgQEoT3GzqoK42wwmT0EOEcXst91P-vDmJsTFFJi0C8QwDImJQWjBXhhLpd2Gy3xy2FCe9UQYG6WYLljahoZXNUXgIagJiPLCKVqbsxQQHxRUa4Btwgsf9SCMpY3ljKNepRS7w1IzHA0gCS6F8WmKKCpf2hgl1RTwLGVktf4mrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
🇮🇷
ترامب حول إيران:
لقد خسرنا 18 شخصًا في مواجهة إيران. وإذا نظرتم إلى العراق، فقد خسرنا 4500 شخص.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/naya_foriraq/92210" target="_blank">📅 00:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92209">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/naya_foriraq/92209" target="_blank">📅 00:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92208">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/naya_foriraq/92208" target="_blank">📅 23:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92207">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نايا - NAYA
pinned «
ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/92207" target="_blank">📅 23:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92206">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/naya_foriraq/92206" target="_blank">📅 23:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92205">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇱
الاعلام العبري
: خطط الطيار للسيطرة على قمرة القيادة فوق الأردن وتحطيم الطائرة في الأراضي الإسرائيلية.</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/naya_foriraq/92205" target="_blank">📅 23:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92204">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
وزير الحرب الأمريكي هيغسيث
يعلن عن إنشاء قيادة جديدة للحرب المستقلة.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92204" target="_blank">📅 22:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92203">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
الاعلام الحربي لعشيرة الشغانبة يؤكد تحرير سفينة ثانية من قراصنة الصوماليين.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92203" target="_blank">📅 22:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92201">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0dd16c8ad.mp4?token=WFWCHq6cxGtuIzc14hMQICUFqDcE4IQS3DW9NDGHXPZKd7tY1mRVPx6RKijIlHEt2fXVjVy_hGyZgl1kILEA5Hm0Ns_tpQeDYh7WrAvE0r4yAV9wHsc15-7mLv6GDkBUEWTnFIdBn7Ew5aM5HgyobFSukg8e9sNF2il6DyGPEnIBOk_v9rcVwKDQumr8c5oytV-GhcvyJ3ys00hod0iRpa6oeBggL0ZOamD0Zety4oS163QOiM7R71gwaycuggHsUyG81eGz9JNPE18PQCIQKJvb_VkMZzgzAfnjh_GsZntvI8w12qAB3sTcixB1nV1IMUvuZbGuxXq5faUdtI5Jgq7CIvnNkNvRwRdUeHghrksFf8naUlur6uxzLSkGElN68_jmTc27ZyE8z4Z8pPQid2bKBE1pxkR-HbhCb9U8V4mrvZv34flweyjqPJJ3ciBPM66P3HOF_GjDS3tDGEamtYN7qZT9eSJXbL9PHusVgzYkWoEVg39BbLmySmrSeltJ-GeV8yvQSnsnBW7E9NJrR8happBTcxKbnWZwGjWqkJ6Ixl4ssNCg_wTAMZxkK3EJWxkgddYjgcrQ9-xJr2Kb5cDEh3Z-8dipMZSG_HueXxA2dH8n_796sxTfxNOp-d37PyETCp77YAZ3SFUTXlZ-JUleTJSxvp20qpdxlvjCbmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0dd16c8ad.mp4?token=WFWCHq6cxGtuIzc14hMQICUFqDcE4IQS3DW9NDGHXPZKd7tY1mRVPx6RKijIlHEt2fXVjVy_hGyZgl1kILEA5Hm0Ns_tpQeDYh7WrAvE0r4yAV9wHsc15-7mLv6GDkBUEWTnFIdBn7Ew5aM5HgyobFSukg8e9sNF2il6DyGPEnIBOk_v9rcVwKDQumr8c5oytV-GhcvyJ3ys00hod0iRpa6oeBggL0ZOamD0Zety4oS163QOiM7R71gwaycuggHsUyG81eGz9JNPE18PQCIQKJvb_VkMZzgzAfnjh_GsZntvI8w12qAB3sTcixB1nV1IMUvuZbGuxXq5faUdtI5Jgq7CIvnNkNvRwRdUeHghrksFf8naUlur6uxzLSkGElN68_jmTc27ZyE8z4Z8pPQid2bKBE1pxkR-HbhCb9U8V4mrvZv34flweyjqPJJ3ciBPM66P3HOF_GjDS3tDGEamtYN7qZT9eSJXbL9PHusVgzYkWoEVg39BbLmySmrSeltJ-GeV8yvQSnsnBW7E9NJrR8happBTcxKbnWZwGjWqkJ6Ixl4ssNCg_wTAMZxkK3EJWxkgddYjgcrQ9-xJr2Kb5cDEh3Z-8dipMZSG_HueXxA2dH8n_796sxTfxNOp-d37PyETCp77YAZ3SFUTXlZ-JUleTJSxvp20qpdxlvjCbmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
أفراح عارمة تجوب شوارع العاصمة العراقية بغداد احتفالاً بانسحاب المذل للاحتلال الأميركي من العراق.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/92201" target="_blank">📅 22:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92200">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy4f1uu7-OZ8xGQLukzThw8NYNON4XuYxFt4H7fbJUPO4cFf7fUKrpja-Ta3SdqmnVBgsgNS9MeKNESSXuofiKvQH0xqo6bailVaCDr9BAkzj5AUHeAXdm9ws9DHnw0VuFCsDo5czIWjgVwzd7RutowMci22wepXTlH0GmQAtrGkgfZwwETo6TzuiK_sUMD28c1AlJklfCWUvzM9Iw2gHW5Jv9X5zm0KOVHZ1fAGtdgiuUyj0RWZShqp-64t18cGSwaVtxYfC6CJwyg5ZEK6YgYnfkST2mxh0Os3xo8c6bcTyzRhkGGNxcaxtJqQ2MQmtqdnxtwBGtYqwtx_3pR6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السلام على من ارعب قاعدة التوحيد الثالثة ..
أسرى ولكن حرروا الوطن ..</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/92200" target="_blank">📅 22:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92199">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
ثاني خط غاز ينفجر خلال يومين في سوريا بعد خط غاز الذي يمر بدير زور.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/92199" target="_blank">📅 22:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92198">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks26IMJr_lsKsA9yEqz65zGdxyTWpOOHbRZ-mpQfzEsFFJG3CEbEEs5zEsjim245Fd5yl7l8W6KgenE8v5jPi8QCalMUlbnrd9orQMcKuPIPjDF7Xv3io9ILem_5fH7Pa3CeLj9E0kjY2fMysyswRQx4IU8r4j8Aigs5xlOJkU1fdzutXPib09ReZfD07pYYguL_xZmxHn1jKMyfT9TaQWffOtzU88naU7_I2LNz3s2NvgDvSwm4YyWp5UMusSP5AKfQW1U8lcYG4Xsnfwp_DKKRv_SWXFPL3_T-E9h9tUSzLkuvCxGQmxHGu3OOWffk1_71MF4LyO0JpYXSLAOFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحمدالله كادر القناة يشجع رونالدو
😆
سييييييييييي</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/92198" target="_blank">📅 22:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92197">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LITrfZWBi_Ki251-U53n-Uh_pKi0YpkD7L_cLc4wg77_IswsxK7UVB2HTVftDL8mkcOclKE0VcQqC7yKBm1ylCc0kJk2htWdAfAM89MNCG1PsiP0z5KzCimHB-Aq9qx4dGWWaCRiZK8Hm9cykKnGWGcPkRnA-Pvr4byngccEgPSAHXYruJ2bINyPeGzRGY7cu-yJXrA1cfU3tOUnSHFxvqpDK-wfWmcUp_MIsEYV-QYBXezubXZZGIngDNOc5dUnmwzVkOypllTTA7wAYAMU2DaRT0vpvSJmG3g0nilwqxwaMq_H94oxaaqJMd6spfUlnUwtA5aO-bqssGk_t6-ZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
توم باراك:
بعد ثلاثة وعشرين عامًا من هبوط أولى القوات الأمريكية في العراق، أكمل الرئيس ترامب عملية إعادة قواتنا إلى الوطن، ليس بالانسحاب، بل بتوحيد جميع جوانب المعادلة الاستراتيجية: بغداد، وأربيل، وحلفائنا الإقليميين، والمصالح الأمريكية، في صورة استراتيجية واحدة، في لحظة بالغة الحساسية. لقد جعل الأمريكيون والعراقيون الذين خدموا وضحوا على مر السنين هذا الأمر ممكنًا؛ ويُكرّم العراق، الذي يقف اليوم على قدميه، خدمتهم. وبهذا التوحيد، فُتح بابٌ كان مغلقًا لفترة طويلة، وهو الفرصة المتاحة لرئيس الوزراء الزيدي والشعب العراقي لتوحيد جميع القوات المسلحة العراقية تحت قيادة دولة واحدة، مع اعتبار أمريكا حليفًا لا مجرد حامية عسكرية. إنها براعة سياسية معقدة مطلوبة لتحريك جزءٍ بالغ الأهمية في معضلة إقليمية ضخمة لا تزال تبحث عن خوارزميتها. أحسنت يا سيادة الرئيس.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/92197" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92196">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed93d8315.mp4?token=gHx5tdCMVCGZI-rK6SsxJIEdiWdErTyKNaf3tF9PwA3k38PlU64M554cAW2cSJkkZzfdSsiovyy7LIQ-xBg1GDMv7K1xXJ1IO5ekOpRkzSj880BVOb3fzsLbEhWiCoFv83iV0_s-E1t6kvN5wicTYfwuFV8oBKe1Midz4OEyAt_1Wit-ZXFTIt6GTxLuRpb0ahaO7UP8IhMqaObFOQR5_VEi2IVgSMBEKoF7XGPm6LS5YLMQkTIoQ5nvaXV0VYyHTYEMxw7wF8dTwU1Jma66kPxBMJUykmszIcire3US-IhdhG19ulmSpyJ8DGuDaQoItQ2_u6uOuk1s-WKcBkZIsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed93d8315.mp4?token=gHx5tdCMVCGZI-rK6SsxJIEdiWdErTyKNaf3tF9PwA3k38PlU64M554cAW2cSJkkZzfdSsiovyy7LIQ-xBg1GDMv7K1xXJ1IO5ekOpRkzSj880BVOb3fzsLbEhWiCoFv83iV0_s-E1t6kvN5wicTYfwuFV8oBKe1Midz4OEyAt_1Wit-ZXFTIt6GTxLuRpb0ahaO7UP8IhMqaObFOQR5_VEi2IVgSMBEKoF7XGPm6LS5YLMQkTIoQ5nvaXV0VYyHTYEMxw7wF8dTwU1Jma66kPxBMJUykmszIcire3US-IhdhG19ulmSpyJ8DGuDaQoItQ2_u6uOuk1s-WKcBkZIsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ثاني خط غاز ينفجر خلال يومين في سوريا بعد خط غاز الذي يمر بدير زور.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92196" target="_blank">📅 21:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92195">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
انفجار عنيف بخط الغاز في دير الزور السورية المجاورة للحدود العراقية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/92195" target="_blank">📅 21:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92194">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f5a08cf9.mp4?token=KCjNSjxvTzZszXSVIkaCIvXjmy8hHusUTl_2MWoFvfTYADQq6-aAzHM9E93e4VwXu6L7MhCrE-b3QBLMxDhqD6ukAl5wvmZXECUY0q3_1rk-YaTnKMIbjlnFkJwfN5hGRkuuVi3ChCqubD3K79u-AALi61Z9PGQDAeVRJ0LSZf2lSUQtyUyJqLACbhxCuS1s3T6aTuvKm3mDkdzFVrTNfjKFa5t9tk9NjWAFjaYELv7nIFg5hOoX8-eK_Y7IwwTRqeyq_Z9WfiWL_CIxa7a8hp612RO4XcR7pc-8nzKSlH_-9CTt2qI9yYjnHSsfxab_eqB3kW-eD06RqvaiEXjwZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f5a08cf9.mp4?token=KCjNSjxvTzZszXSVIkaCIvXjmy8hHusUTl_2MWoFvfTYADQq6-aAzHM9E93e4VwXu6L7MhCrE-b3QBLMxDhqD6ukAl5wvmZXECUY0q3_1rk-YaTnKMIbjlnFkJwfN5hGRkuuVi3ChCqubD3K79u-AALi61Z9PGQDAeVRJ0LSZf2lSUQtyUyJqLACbhxCuS1s3T6aTuvKm3mDkdzFVrTNfjKFa5t9tk9NjWAFjaYELv7nIFg5hOoX8-eK_Y7IwwTRqeyq_Z9WfiWL_CIxa7a8hp612RO4XcR7pc-8nzKSlH_-9CTt2qI9yYjnHSsfxab_eqB3kW-eD06RqvaiEXjwZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نيران لا تتوقف من الموقع الذي حصل فيه انفجار بالعاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92194" target="_blank">📅 21:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92193">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bf201505b.mp4?token=akaGK9RanAY7uxuE7HhV6ozUfqW-3GkggMPV0bbcYgqgyTOlCyNoF0LBQdaH3BEge5SmeBUuA9hIS14TXORoZo70vr1mCOH0VDCwb4qZxhTtvKx7RG1VDkGH69nHnrjeS6pPsTaIFy4GPaCUVJholVX2om3Mn2BWuuiVuGcZrJ2f17g88Mj4Ng2ixSNVSviNEafbXO7cAi9JfWIkbRa5fMUVpSWZ85USBjtnFAree_MoGZjtDj6tW8UwHJ3mrP4z3BEZYFn2vvcmLrTohdJGbDjj_j806TREBBwxDMFNB6naAgqa2BcNd7O67Zqb9Ps_oskoEEzfFTz4UjdHDWBFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bf201505b.mp4?token=akaGK9RanAY7uxuE7HhV6ozUfqW-3GkggMPV0bbcYgqgyTOlCyNoF0LBQdaH3BEge5SmeBUuA9hIS14TXORoZo70vr1mCOH0VDCwb4qZxhTtvKx7RG1VDkGH69nHnrjeS6pPsTaIFy4GPaCUVJholVX2om3Mn2BWuuiVuGcZrJ2f17g88Mj4Ng2ixSNVSviNEafbXO7cAi9JfWIkbRa5fMUVpSWZ85USBjtnFAree_MoGZjtDj6tW8UwHJ3mrP4z3BEZYFn2vvcmLrTohdJGbDjj_j806TREBBwxDMFNB6naAgqa2BcNd7O67Zqb9Ps_oskoEEzfFTz4UjdHDWBFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
انفجار عنيف في ريف دمشق بسوريا.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/92193" target="_blank">📅 21:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92192">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/764dd602ed.mp4?token=oYKCL6qYN25DWqfopycML_vQHVDdEA4MsHmBeO8Qvsq3SfeqArx1w91HOeRIYwAX6pIk05RHSS0skeIfFuv5W6P5yRrKCFpC9tCB9-c-WkO5s22bJ7DhgX9nslt9bys5T4m1l-qYLiGgaQm4VM_9sLf52sljt5sPFlccM34IwfwQ_kB048AuwKvlMPbSAkHsMAg56WwcJg6EWy4PF6zTpE4GN2oCY5Og3c5U5tehD0BuRfoXelxkyiHUuBa4kuI7el6C9S5VMN8eude2Mcp8Xh9PmJvuFfMTvvFYuEHlh5QaPoL7OcrI978qNlxqsWY2Q4XO0_Geotl_idEtUm5yDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/764dd602ed.mp4?token=oYKCL6qYN25DWqfopycML_vQHVDdEA4MsHmBeO8Qvsq3SfeqArx1w91HOeRIYwAX6pIk05RHSS0skeIfFuv5W6P5yRrKCFpC9tCB9-c-WkO5s22bJ7DhgX9nslt9bys5T4m1l-qYLiGgaQm4VM_9sLf52sljt5sPFlccM34IwfwQ_kB048AuwKvlMPbSAkHsMAg56WwcJg6EWy4PF6zTpE4GN2oCY5Og3c5U5tehD0BuRfoXelxkyiHUuBa4kuI7el6C9S5VMN8eude2Mcp8Xh9PmJvuFfMTvvFYuEHlh5QaPoL7OcrI978qNlxqsWY2Q4XO0_Geotl_idEtUm5yDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
انفجار عنيف في ريف دمشق بسوريا.</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/92192" target="_blank">📅 21:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92191">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇸🇾
انفجار عنيف في ريف دمشق بسوريا.</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/92191" target="_blank">📅 21:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92190">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-PLJWJ_q_cFKZ9i0esKv1M85iZQKnygxTGAFgPQ8crKL9zBMSmMs9a7zXvEmy7gtooHhPpITu15n9bN-hE65gOsDdfBSLiY_Xplrg81_XL7_DRHn4LYMwc9jTfVeapCtPuIOm7FYronX_USAU6TMPzVcgWmyxczQspuAl9qKkhaEdIvAw2bVjKkplN8AWRfrafs2bOjc2u27yAP1o1fkeyQn6FwUexc_1nooUSL3K52DGjgTkQLXHN1oU8PS8pqX6FV3I1ly3kk_vJegpFetHvLHwsBSX6H3WLN_2aL5X_HDhrwVi4ZwlXN8ToWGL6tuWEPN5V-qsCZOWm6BEZztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
انفجار عنيف في ريف دمشق بسوريا.</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/92190" target="_blank">📅 21:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92189">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2263171641.mp4?token=vHzNJe-PWGvGEKbvHcdXsroogaOW-GDy91IGHS2kvh45LFw_A8nUU6v6EAcDbQI5Wlo2STJaz8zEXG4gRQhlpOrnT7L0_3oxnw2ZyxsF3X_l0fNnDmtTMBj-Qf7JGxvTOVSJf3UHtknFzmBDeYyqMHEPAGTNAdZymF9awDxGCI7qwujrpwxv9o0sJYbiYem4Dw2kdzlWN8ztb0MzpCm7_ZdlKER83UucEOW6d18HO9He7chxpY1DS6hJ62JN8WHD2zex7cZBMiqQvOnwtvAIy3LhjRKXELRrLGOI9jJij5vyTqwGjDD20cexb3UNb9YnygL0_S4mzmw30ybwr53dZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2263171641.mp4?token=vHzNJe-PWGvGEKbvHcdXsroogaOW-GDy91IGHS2kvh45LFw_A8nUU6v6EAcDbQI5Wlo2STJaz8zEXG4gRQhlpOrnT7L0_3oxnw2ZyxsF3X_l0fNnDmtTMBj-Qf7JGxvTOVSJf3UHtknFzmBDeYyqMHEPAGTNAdZymF9awDxGCI7qwujrpwxv9o0sJYbiYem4Dw2kdzlWN8ztb0MzpCm7_ZdlKER83UucEOW6d18HO9He7chxpY1DS6hJ62JN8WHD2zex7cZBMiqQvOnwtvAIy3LhjRKXELRrLGOI9jJij5vyTqwGjDD20cexb3UNb9YnygL0_S4mzmw30ybwr53dZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد من مقرات الاحزاب المعارضة الايرانية في محافظة اربيل بعد استهدافها.</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/naya_foriraq/92189" target="_blank">📅 21:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92188">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
اصوات قوية مجهولة تسمع في محافظة اربيل.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/92188" target="_blank">📅 21:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92187">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08354de256.mp4?token=RksxYS3lnhQ57kyk50D2ralFS-_obgANxXWZTWM8L5CQYQ4mJsUZyaZ0eg6_-rEvthSSb03v29piHlXbBU5u1EZOF-H1etcXEOP2qLdScriizARbmKK0ATY5NmwRiTzw2CuDY9KaWdBAUPUqRm8IEdohBGlTg3uhW3j8uA6WtEDVboPY1RT3BSipPk4IJfPofzc4HI6v3p9CZLbOQcfN3quvEthn2DRrQKEtVdlzZsyxpOndFMPCDD4c0x5sJNE4QcoK-56mxDI-4hp1tOBe2p3u9cpZr-g9q2YH8OWYtDGSSzW-OnYhFq16l2r-1ogVMDmaL2f8XGlFtgvrVgG-eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08354de256.mp4?token=RksxYS3lnhQ57kyk50D2ralFS-_obgANxXWZTWM8L5CQYQ4mJsUZyaZ0eg6_-rEvthSSb03v29piHlXbBU5u1EZOF-H1etcXEOP2qLdScriizARbmKK0ATY5NmwRiTzw2CuDY9KaWdBAUPUqRm8IEdohBGlTg3uhW3j8uA6WtEDVboPY1RT3BSipPk4IJfPofzc4HI6v3p9CZLbOQcfN3quvEthn2DRrQKEtVdlzZsyxpOndFMPCDD4c0x5sJNE4QcoK-56mxDI-4hp1tOBe2p3u9cpZr-g9q2YH8OWYtDGSSzW-OnYhFq16l2r-1ogVMDmaL2f8XGlFtgvrVgG-eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
ترامب عن العراق:
لقد قاموا بفصل الجميع في العراق - الجنود، والضباط، والشرطة، لم يكن لديهم أحد لإدارة العراق، وهكذا ظهرت تنظيم داعش، نحن نفعل الأمور بطريقة مختلفة تمامًا. لقد تعلمنا من الحماقة التي ارتكبوها في العراق.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/92187" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92186">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران:
ستشهدون أحداثًا مهمة قريبًا جدًا.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92186" target="_blank">📅 21:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92185">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d11445f42.mp4?token=sw0fSyVIW1vsoGs4UHovjEgoc3Ll10TeU7Z1m93aS9fw7BHlNzLs20Kta9VVqLpERVyqmPeXtjnGzzjQsrJpkqDY1PjaTLTvs70J_rd_0pUmok55sQS0E3CCXVAqEHse5KxxFDHSSIzIa24634ICFrYsZrjrZC_9Jykcnl9QCAH-Q6yUobNRAeBCLOEBeDElAcsvvQe5JeiqpeVCxFgQw0GvuFped8h6Z6QXptKO6VQcAvMXcJJSb6_-z_F1ayM3RWDBpSQZwm8RAtcNeVXiHFPLiR0jiLuVZ-2TROLqGTq3-qlPluid2Qt6eOrPkG78SwL3lxm1NEcdt0Ll4wmctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d11445f42.mp4?token=sw0fSyVIW1vsoGs4UHovjEgoc3Ll10TeU7Z1m93aS9fw7BHlNzLs20Kta9VVqLpERVyqmPeXtjnGzzjQsrJpkqDY1PjaTLTvs70J_rd_0pUmok55sQS0E3CCXVAqEHse5KxxFDHSSIzIa24634ICFrYsZrjrZC_9Jykcnl9QCAH-Q6yUobNRAeBCLOEBeDElAcsvvQe5JeiqpeVCxFgQw0GvuFped8h6Z6QXptKO6VQcAvMXcJJSb6_-z_F1ayM3RWDBpSQZwm8RAtcNeVXiHFPLiR0jiLuVZ-2TROLqGTq3-qlPluid2Qt6eOrPkG78SwL3lxm1NEcdt0Ll4wmctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اعمدة الدخان تتصاعد من قضاء كوية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/92185" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92184">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇸🇦
حرائق كبرى بمستودعات عسكرية في الرياض العاصمة.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92184" target="_blank">📅 21:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92183">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
اعمدة الدخان تتصاعد من قضاء كوية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92183" target="_blank">📅 21:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92182">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
ترامب :  ويسرني اليوم أن أعلن أن آخر القوات الأمريكية ستغادر العراق! لقد مر وقت طويل، مع اتخاذ قرارات سيئة للغاية جعلتنا نتورط في هذا المستنقع في المقام الأول، ولكن قريبًا، سيصبح ذلك جزءًا من التاريخ. إن هذا يوم عظيم لأميركا، والأهم من ذلك، أننا نغادر العراق…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/92182" target="_blank">📅 21:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92181">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb1176520.mp4?token=D3fkDNdn7n113Hkswhd7O-trOtS9A3RTNf85eoPH5id1NXW5PWPPdsCoLJ6BD-nkeyLurr38ehHRyddfmk6LJv-R2L-mjV16lLX27gIMkjIQSll0IQsp78j3i5M4BH5BBZ74Vdkb99jxWPa9TUq8IWVKi-ZhNHVp7i4ar3aI0cwWLHAXWsLG6WqOF2P6PV3VeR-SZUAVkR_JlnWA-AXDvHrOhGXV1O1oLcUNMLTTsubZizyDzXNi4YCsMZ9E1ZEcqjv_Y2GeFbzlVu4hYNWoFXpd0UNOq7ZyrgC6SdWiM5ImddRQuq1lNKaaU3AlP11f5uU4GFmNYUXvcGSwuXhssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb1176520.mp4?token=D3fkDNdn7n113Hkswhd7O-trOtS9A3RTNf85eoPH5id1NXW5PWPPdsCoLJ6BD-nkeyLurr38ehHRyddfmk6LJv-R2L-mjV16lLX27gIMkjIQSll0IQsp78j3i5M4BH5BBZ74Vdkb99jxWPa9TUq8IWVKi-ZhNHVp7i4ar3aI0cwWLHAXWsLG6WqOF2P6PV3VeR-SZUAVkR_JlnWA-AXDvHrOhGXV1O1oLcUNMLTTsubZizyDzXNi4YCsMZ9E1ZEcqjv_Y2GeFbzlVu4hYNWoFXpd0UNOq7ZyrgC6SdWiM5ImddRQuq1lNKaaU3AlP11f5uU4GFmNYUXvcGSwuXhssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اصوات قوية مجهولة تسمع في محافظة اربيل.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/92181" target="_blank">📅 20:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92180">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
اصوات قوية مجهولة تسمع في محافظة اربيل.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/92180" target="_blank">📅 20:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92179">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb0IwLgi5_Zt_B2e4budUK5T6VPbM-4RtQRj1-0JUEDg68r3oFFYjeZ4tYy7nrJfNNROQ5TKUItp_i9NQWbMXiFkvppBQqX8ecTcZPCU3MO4zFunD6pr8Nwc80Sj0c7CMK5fs-zL3eNha834jOyRueL-LrSxogrQj7N33RI4U6rBBlB6MSUQ409JimekltQau_j0K3Ry9mlmsBcYwi23Ljmms2FtL9u7SGJsvDRAsGIpkCavrexppAko0FRuvy3_sS--8EeyApEou0nmoi275mF4jsu2eJvGfYqzbTRBYOxRC3iRV6vrLsiJnQOsX1vsNpn8ehMx-42OawGaKhqQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب :
ويسرني اليوم أن أعلن أن آخر القوات الأمريكية ستغادر العراق! لقد مر وقت طويل، مع اتخاذ قرارات سيئة للغاية جعلتنا نتورط في هذا المستنقع في المقام الأول، ولكن قريبًا، سيصبح ذلك جزءًا من التاريخ. إن هذا يوم عظيم لأميركا، والأهم من ذلك، أننا نغادر العراق مع رئيس وزراء جديد رائع، علي الزيدي، وهو شخص دعمته منذ البداية وأؤيده بالكامل. لقد فاز في انتخابات لم يكن من المتوقع أن يفوز بها، وقد فعل ذلك بأغلبية ساحقة!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/92179" target="_blank">📅 20:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92178">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 51 غارةً جويةً وصاروخاً من خلال طائرات "F-15" أقلعت من قاعدة خميس مشيط والعدوان الصاروخي من نجران وجيزان، استهدفت شبكات الاتصالات المدنية والأعيان المدنية فى محافظات مأرب وصعدة والحديدة وتعز وعمران.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1209 غارة جوية وصاروخ.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92178" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92177">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
🔻
الأمين العام لكتائب حزب الله الحاج أبو حسين الحميداوي:
الحاج الأمين للدائرة الإعلامية: المقاومة انتصرت والمنتصر من يفرض شروطه
أدلى الحاج أبو حسين الحميداوي، الأمين العام لكتائب حزب الله، مساء اليوم بتصريحات إلى الدائرة الإعلامية التابعة لكتائب حزب الله، أكد فيها على الآتي:
أولاً: لقد انتصرت المقاومة الإسلامية الظافرة في هذه الجولة مع الاحتلال الأمريكي، والمنتصر فيها هو من يفرض شروطه على العدو، وهذا ما يجب أن يتفهمه الصديق.
ثانياً: المعركة بين الحق والباطل بدأت منذ بداية الخليقة، وقد تتغير الأسماء والأدوات والتواريخ، ولكن المبدأ يبقى واحدًا: صراع بين الخير والشر، لم ينتهِ حتى قيام الساعة. وأضاف الحاج الأمين أن الواقع يُقسّم الناس في هذا الزمان إلى ثلاثة أقسام:
1-أن ينحازوا إلى معسكر الباطل.
2-أن يتمسكوا بمحور الحق (ونحن إن شاء الله من المتمسكين بهذا النهج).
3-ومنهم من لا يُحسب إلى هؤلاء ولا إلى أولئك.
ثالثاً: لا داعي إلى التكهنات والتحليلات، فلم نصل إلى نتيجة مع السيد رئيس الحكومة، فقد انتظرنا جوابه إلى آخر ساعة، والأفضل أن نبدأ من جديد لننتج اتفاقًا متينًا يحفظ للجميع حقوقهم.
رابعاً: إن ثنائية المقاومة الإسلامية والأجهزة الحكومية الرسمية أراها منقبة وأمرا حسنًا، ولا داعي للتحسس منه، والكثير من دول العالم تمتلك أكثر من جيش وأكثر من منظومة عسكرية. نعم، يجب أن يكون القرار الأساسي في السلم والحرب واحدًا، أو على الأقل متفقا عليه، وهو أمر مقبول لدينا.
خامساً: يجب على جميع مجاهدينا في العراق إيقاف جميع العمليات العسكرية والأنشطة اللوجستية المتحركة، ما عدا العمل على استهداف الطيران المعادي المنتهك لأجواء البلاد، إلى أن تكتمل الدفاعات الجوية الحكومية بإذن الله.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92177" target="_blank">📅 20:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92176">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cea8ec4b2.mp4?token=MTajTwtI7LFjFRp6Vc8RO20S8klpbTmtcDb8eusUdcKWbDnkOcEOs_6wW65lZ8DJs1fX-fJjZUq7Ga9cIacfo37zIQsCWHAAIvwL7RxMvMPgyRXbywQ3Y0vCFtXsijy0fJBhVXFtMBz2i1MG5mmPLit2y2IFbJiohypryjAnXKNTVQ5uax_QHKA9ovJ-YgPYWjnwedIUTl302IILxWuI7ILcv-K__4T_2LJeYep-q-t7U35ZIYhkD99XWE42QxtFBlTyoSnqkArI6zqbD-ZYU30yxZfLLBKPvB-Q5jwIWcVVJ1_IElo0vvuZEnKlyOmIIqI909WTFLUsx7ZwNSgHrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cea8ec4b2.mp4?token=MTajTwtI7LFjFRp6Vc8RO20S8klpbTmtcDb8eusUdcKWbDnkOcEOs_6wW65lZ8DJs1fX-fJjZUq7Ga9cIacfo37zIQsCWHAAIvwL7RxMvMPgyRXbywQ3Y0vCFtXsijy0fJBhVXFtMBz2i1MG5mmPLit2y2IFbJiohypryjAnXKNTVQ5uax_QHKA9ovJ-YgPYWjnwedIUTl302IILxWuI7ILcv-K__4T_2LJeYep-q-t7U35ZIYhkD99XWE42QxtFBlTyoSnqkArI6zqbD-ZYU30yxZfLLBKPvB-Q5jwIWcVVJ1_IElo0vvuZEnKlyOmIIqI909WTFLUsx7ZwNSgHrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
لحظات من هبوط الطائرة التي تقل ركاب صهاينة في اسرائيل التي انطلقت من السعودية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92176" target="_blank">📅 19:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92175">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bee006731e.mp4?token=RYawBUoAaw7ezNMN3Ki3JgEJn50U0NcCpysEBdxPPh2mhiPmCX5VxBfRMyxAyf4w8U87QKKmAXJBb0mK1tF14xtSuH0OlXh8DyEqaEsnOgc9gbU9062m-Xxf9AWoevLpnKibVUrpiuVTAXoDDO1R0OchMrkVkQy5jgyU8bQFLpUunVgJn-xfRUnevxp45jXEmCg8OxQBz7BEnlTrHGFef3hPikQSe98TvctwVni8WsfZCzmvOz7VKwrmeTAeidqy2AyoCuuXU3H_ccQBo_YXZkL1vD3mq2ggFo9S4Zh7nUqrO8vY3WE9HjDnW91mnrZwHErYSlImBlZLwBDvfsMnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bee006731e.mp4?token=RYawBUoAaw7ezNMN3Ki3JgEJn50U0NcCpysEBdxPPh2mhiPmCX5VxBfRMyxAyf4w8U87QKKmAXJBb0mK1tF14xtSuH0OlXh8DyEqaEsnOgc9gbU9062m-Xxf9AWoevLpnKibVUrpiuVTAXoDDO1R0OchMrkVkQy5jgyU8bQFLpUunVgJn-xfRUnevxp45jXEmCg8OxQBz7BEnlTrHGFef3hPikQSe98TvctwVni8WsfZCzmvOz7VKwrmeTAeidqy2AyoCuuXU3H_ccQBo_YXZkL1vD3mq2ggFo9S4Zh7nUqrO8vY3WE9HjDnW91mnrZwHErYSlImBlZLwBDvfsMnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول الطائرة البديلة الى تل ابيب قادمة من السعودية بعد الخدمة الـVIP التي قدمها النظام السعودي للصهاينة</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92175" target="_blank">📅 19:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92174">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u38dhSRWQcoMnOLRaGLTo_3wazGW4gJJxyG2P4VkMwv3POuYOO99f6RoAlyi23Nne66BBKu_FoXpg7CgEwz3HCVVXCIOjezDaq00mqAD1UfoVHVziJc42j8jr5X5bvgz7OK805oWqbV1nfBDWflKxSD8rC1BXPzUXUSherrEtlMSWM0lD5p8a-3gTsMC7wCQRiwYFdW80e9BHoHd57hKF13D7IbARJscJe4XqNM8vHxyt2UQA1OtTqU64_Ck-8ZnQnEvHx4iYk3-M_Pa9AFBZhAUr7ay3BIse2VwR06Ng990jsDND0LZuhMYNc0aEMYOEsSnGMvC_O-IQR5x046btw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منظمة العمل الاسلامي: نؤكد ضرورة رفع أي حجوزات أو قيود مفروضة على الأموال والعائدات العراقية الناتجة عن تصدير النفط بما يضمن أن تكون موارد العراق تحت إدارة الدولة العراقية وبما يخدم مصالح شعبها</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/92174" target="_blank">📅 19:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92173">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUgqYbUba5VNG8EYjmPz1dbmW7q6-0QGVisZbyQDKzdrSYnGV5SX2K2R07Wu_GxJuCHKV4wAmRI9xMB_8VXU2UPZNtdF-oznpqE_MCDGe02kmYkaMlS_NCVOExceESq-C2m5secfqYlDb0RRLRUr5ImAwA3fQlxLyzNjsosC7DrdKCBK11PQJf83RxEowMvV4GDfPQt4Jm6-x8so1pot44GBTxR9TCTanvhhq4cRtI0twS9LFFzS51BYGCqloB9nbO2Pv15imWVN2qn35Ucx26hc6UcAzquEF44wtg8o7MntXamTjk8jbe1mWfN63_OdXri-Gb74stNSCPwyKcdM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولى المشاهد من قاعدة فكتوريا في العاصمة بغداد بعد تحريرها من الاحتلال الامريكي</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92173" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92172">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee502fdcdf.mp4?token=oGgPdHpJBUyl9x8duMBgtv2YLmGPVg4R4NRG94DcVMLYC0XkaDK8VzkTv5eRmW185oiKJBR0WaT4Y-wK6eWK7y99FoE1dG5cFLUOXyTTJ6zjvtPYRt1VAoq1m9QrMATVf2x7nGtGR-lNcZ-ix9gwEXK-_5E6dluywMTCuOjjKJHf-jSgMrBfUrEXgcPk76wN6kbyrVjyPKQSUhKcb_4sjcXMTD43On6qmJ1hEC5CrjzxWwX4QawYr_ovDycqSHm-ljdERu-tdwkFdbn2044mtpSj-gkXErKw3yRGlxJooJd__nkUULBxJmrSeGRNRfRu_L46SQEK_HdA20Eqp7QcWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee502fdcdf.mp4?token=oGgPdHpJBUyl9x8duMBgtv2YLmGPVg4R4NRG94DcVMLYC0XkaDK8VzkTv5eRmW185oiKJBR0WaT4Y-wK6eWK7y99FoE1dG5cFLUOXyTTJ6zjvtPYRt1VAoq1m9QrMATVf2x7nGtGR-lNcZ-ix9gwEXK-_5E6dluywMTCuOjjKJHf-jSgMrBfUrEXgcPk76wN6kbyrVjyPKQSUhKcb_4sjcXMTD43On6qmJ1hEC5CrjzxWwX4QawYr_ovDycqSHm-ljdERu-tdwkFdbn2044mtpSj-gkXErKw3yRGlxJooJd__nkUULBxJmrSeGRNRfRu_L46SQEK_HdA20Eqp7QcWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تأكيدا لنايا مرة اخرى
🇮🇱
مستوطن صهيوني: حينما نزلنا في المطار السعودي قدم السعوديين لنا الكعك والبسكويت والعصائر والقهوة ثم بعدها قدموا لنا الطعام الساخن ووفروا لنا فريق طبي يعتني بنا واحد تلو الاخر طوال الوقت</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/92172" target="_blank">📅 19:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92171">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4d721dc53.mp4?token=c6CefBCbZKbrrK1hiRsArt2A65ReY-vqAiCyoOLBMkM5HSGX6rR6a9l2zQVOsoEijjV5vAipoePvvwRSpZTtSoqkW7VeRb6XyezqK88C-Zwj8QyKm0IHGroDL1jYaiKIepWXbmM5FracoRyaVc61vB3FIAc7TVca7nXKqHXGql8_h38x8fdmJtRT6vLdlQ-G6aCBwwLmxf_y1gvONEPMbBtgVmjQVdoHJW-Ry3L6P3YoppIhk4Ae0B2jTr9z3eSwsuSGMEgzzlWm6JrWEEwklx1nExgsfQVkUU-TSpuJy7zUawEcu5ehgeKjy22mQVARUT91eHl7xP2Al8K7f8YohniXI4aa0fmofYFW5M1gjBx8i181Sw5reSxw9dg97EfgCMaP-dEH6fVKd8aJeJyPB6Oy5guXTm_bbMk8aOdxEQzOdGPRef49YLhcDGSfIUZpEXo_-kBQMXBxBtKtM8AOsUNkQdzrBgFCyJ0PQlfo-6faKOdI7Obu43vwb6JZSGSfV8AisCeFw5553hjN-0gcgVhgzPkUG3WDNT0dVi3fEd1NYlxQQkJ7-EpoYluQvcOSlaFdj1JTuCoCjWaD19QnV95UfkShGlWxaQcu59YppF8-I-L5L45MRWJlU5pr2Yyc4x13M_OqvYxcaZ_WIn3RuE25X2qj_jfrSCyIxjnHlco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4d721dc53.mp4?token=c6CefBCbZKbrrK1hiRsArt2A65ReY-vqAiCyoOLBMkM5HSGX6rR6a9l2zQVOsoEijjV5vAipoePvvwRSpZTtSoqkW7VeRb6XyezqK88C-Zwj8QyKm0IHGroDL1jYaiKIepWXbmM5FracoRyaVc61vB3FIAc7TVca7nXKqHXGql8_h38x8fdmJtRT6vLdlQ-G6aCBwwLmxf_y1gvONEPMbBtgVmjQVdoHJW-Ry3L6P3YoppIhk4Ae0B2jTr9z3eSwsuSGMEgzzlWm6JrWEEwklx1nExgsfQVkUU-TSpuJy7zUawEcu5ehgeKjy22mQVARUT91eHl7xP2Al8K7f8YohniXI4aa0fmofYFW5M1gjBx8i181Sw5reSxw9dg97EfgCMaP-dEH6fVKd8aJeJyPB6Oy5guXTm_bbMk8aOdxEQzOdGPRef49YLhcDGSfIUZpEXo_-kBQMXBxBtKtM8AOsUNkQdzrBgFCyJ0PQlfo-6faKOdI7Obu43vwb6JZSGSfV8AisCeFw5553hjN-0gcgVhgzPkUG3WDNT0dVi3fEd1NYlxQQkJ7-EpoYluQvcOSlaFdj1JTuCoCjWaD19QnV95UfkShGlWxaQcu59YppF8-I-L5L45MRWJlU5pr2Yyc4x13M_OqvYxcaZ_WIn3RuE25X2qj_jfrSCyIxjnHlco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تأكيدا لنايا مرة اخرى
🇮🇱
مستوطن صهيوني: حينما نزلنا في المطار السعودي قدم السعوديين لنا الكعك والبسكويت والعصائر والقهوة ثم بعدها قدموا لنا الطعام الساخن ووفروا لنا فريق طبي يعتني بنا واحد تلو الاخر طوال الوقت</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92171" target="_blank">📅 19:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92170">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ced3ab6da.mp4?token=XzcForKWz74sjPkyJMmOu0Y-cINuGKd7DKBy7Gz7VIlquEdIBhPzLsU468Hjuw0cnl6lHy_4rnOCYrSQnnLpQKRNFdwPKEvnPQ4mOiqiEkRMX8kZyGJxCq-WOY_VTfXUssgghXzCQ9pD7Ndjz9Rp6NLkWiUREBBL2jwW-o0fzkX6YaogUH4QLzhseoLAQdbi8935oPS9n2zlBfqG5rXHhbWOyUT_jeoFWmGWuuFTPAZ2kigEqLcAOM00baFnZNaBUFREDVSlPuabs6WFN-Fb6FeyLNL6GJh6sbS7IQA3tCzGjOf-OuINkggfLpdXTZEGw_jXzkGDZLsW75UqOJmgbY9-Ae7bZKbnSlf7lPvhSoyn9FntD-1y5np-o9myESeCTlr19UjZx1d5fcxihmBox4h1Fp_OiwaekiH--LPGVFnE44dKZMNC4hOuYJ6DXSuAIMC0pIxu9u5RmfAwwwYrAw5trbwtf6YwE8Ra3xCoA9k2hBsiWqVy8zApEY0NgZPx2AZqQdoAb83mI1ksXeMFpg0hNdbdE1zE3mnSmmDsVWAAg3n6zhMQGCWSHwN68_j8bkB-DxbNZ0RKqBuuVhDCW6iutSIXl3fZSH7KAq6g3uoYplnB8-b_VUN6X85ZgSD0Gn5hmmJpyY0_lpN6sDHyu202KTZ-aN_1sWocuenO-ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ced3ab6da.mp4?token=XzcForKWz74sjPkyJMmOu0Y-cINuGKd7DKBy7Gz7VIlquEdIBhPzLsU468Hjuw0cnl6lHy_4rnOCYrSQnnLpQKRNFdwPKEvnPQ4mOiqiEkRMX8kZyGJxCq-WOY_VTfXUssgghXzCQ9pD7Ndjz9Rp6NLkWiUREBBL2jwW-o0fzkX6YaogUH4QLzhseoLAQdbi8935oPS9n2zlBfqG5rXHhbWOyUT_jeoFWmGWuuFTPAZ2kigEqLcAOM00baFnZNaBUFREDVSlPuabs6WFN-Fb6FeyLNL6GJh6sbS7IQA3tCzGjOf-OuINkggfLpdXTZEGw_jXzkGDZLsW75UqOJmgbY9-Ae7bZKbnSlf7lPvhSoyn9FntD-1y5np-o9myESeCTlr19UjZx1d5fcxihmBox4h1Fp_OiwaekiH--LPGVFnE44dKZMNC4hOuYJ6DXSuAIMC0pIxu9u5RmfAwwwYrAw5trbwtf6YwE8Ra3xCoA9k2hBsiWqVy8zApEY0NgZPx2AZqQdoAb83mI1ksXeMFpg0hNdbdE1zE3mnSmmDsVWAAg3n6zhMQGCWSHwN68_j8bkB-DxbNZ0RKqBuuVhDCW6iutSIXl3fZSH7KAq6g3uoYplnB8-b_VUN6X85ZgSD0Gn5hmmJpyY0_lpN6sDHyu202KTZ-aN_1sWocuenO-ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر لنايا: ال سعود يقدمون القهوة والتمر للصهاينة في مطار تبوك وخدمات اخرى افضل من تلك الخدمات التي تقدم لحجاج بيت الله الحرام.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/92170" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92169">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHtagHh-xUySDpZxYKRBi4fLKTM51sah10Sra9Zk3ZFg_MHIdhGykOiTXoKfJBztQvxcOrZGE17ZPdU8F4iG2DT_hMKfAe0SZn9ZyfeDMecmBuAbNfAy7RfaIsdfAD3jALiN0mNS8kvg5A7O6ISKrCdtUBYlvABpYjshAORXoM1g0Utc3Me4tsMQ0KZj1JuP18j_iEZPEZLFN-FHPSwAGEfg4IAPP7RJitbYRL-KyB4oA-YDKO8v64cQd-lDZy42H2F-ZKMQEujCq99pwb8lISBfMgzNzYxZjo7MPdFX8yPzSAHBMG2B44f6wbxmC346rx1uDzUPHZkffhvvfZaqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92169" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92168">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJm4SV3m6rjvE2f4PNhwsiTNdtbfE3dNHPK_R0pOgQcfkqqRo4witGMy8TKKCWWzu11lzZICGKV_vrx9dFDlPGS655GB9hXwi0-sfsuNohyKyNYP9e4oTZdR4JMdE24YHAqTmkNmOjjxCIUUpCsOskS_y94QT3ufngkMQrmrfBa7ISwz9g7W8Q1eEtzZYATCt0csZ6v2iOqYKK3m-D18Ko6ujtGhaHlbflXgJYSNme7S_PTas-yaicI4P-bmWLTpG38aXnCKTmBO43bCNshIPxmrhB2EXJTCGnFrdIEWe7l0r2DVWO-WnMfQGMNTYzzlFDJehCy77YrwSn45fNFePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستر : الواوي الذي طيح حظكم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/92168" target="_blank">📅 18:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92167">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtUDnPvOTcyz3oHFMtbBb7C4AtFhJH1kTH5eptYDaPGOCYDJFdJwKrZAKUt4gdjVCNUca-2G3JXGoHmyxVtYru2lgtq1sILhZaEkfIaXmcbYl3BUGmCP-J4PS05yCHP4dSrCCzVc-JUAM-1hqi8HaG3hnbpFeRhbSnfEtyFdI3wek_trVAmsrjxdKlK_5dlpIBMWHcNJAg6Ovq2Ibito2lDmAUaIgss7udlkIQVgrfSxhSsuLqh-DGZNd0u8qi8WK57ug-wZqMLlB9YAVzsQmyOpKXcxO1P9aIOKx-2uPE0kcvLCG8TTx8HdBpHamUrVviKpVwgnGLNRgL8ORMvxsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخاناً أسود يتصاعد من حقل عين دار النفطي السعودي بالقرب من خط الأنابيب الشرقي الغربي</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92167" target="_blank">📅 18:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92166">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الانفجارات سمعت في الخبر و مقتربات البقيق غرب السعودية</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/92166" target="_blank">📅 18:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92165">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/92165" target="_blank">📅 18:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92164">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0264db5cd.mp4?token=j42eYCBC3IXcWwgnKGEojM5swMvbH8Yem_TleyAI0toKtQq_tfZfNtcAbMRV_VXd3ZyOJgnPLiCRbdTc4JCwkvpSHc0W53bUg1cLEIlUPQBznuXugX7pRJBXOXg6aonrFyRe06NIPXPwqWlQ7aZsImYi_y1a7-OyTlhlJQHI-oDUaGUV2zz_e73mJvyfXhSd4Jc5tyO4G87l7ZKbyOdTVo4V71ZmFF1P3fYhJDKfpL1qfoZdHcyxhxDKZa7Rmw7WBW3Ghbr8lY5qZ9f6fl5uoIG1fwK7FrsQ2pRkXeOloeDEb7tG-5TXP72wbejSxqZ7FR6m5Fr3PF4H4nKJeBPadQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0264db5cd.mp4?token=j42eYCBC3IXcWwgnKGEojM5swMvbH8Yem_TleyAI0toKtQq_tfZfNtcAbMRV_VXd3ZyOJgnPLiCRbdTc4JCwkvpSHc0W53bUg1cLEIlUPQBznuXugX7pRJBXOXg6aonrFyRe06NIPXPwqWlQ7aZsImYi_y1a7-OyTlhlJQHI-oDUaGUV2zz_e73mJvyfXhSd4Jc5tyO4G87l7ZKbyOdTVo4V71ZmFF1P3fYhJDKfpL1qfoZdHcyxhxDKZa7Rmw7WBW3Ghbr8lY5qZ9f6fl5uoIG1fwK7FrsQ2pRkXeOloeDEb7tG-5TXP72wbejSxqZ7FR6m5Fr3PF4H4nKJeBPadQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رصد اطلاق صواريخ من الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92164" target="_blank">📅 18:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92161">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBinqxTdbny9Mkrgo7efhifly2RoCHfeaASZVmvqLWA3tmEQZE0HXYp2BmtDmXz9NtyRH3zoetfFbush02NoCPERM_-TFY9qI_C3GX7GXYv9VkGMydQJlnukEsrDiewY0cvJoukH4p-Xoh00UaMcWKSIBW8uwUA4PaJSh7O8wjY85dDXJ8_6HeuBDnL2NdUhRLsBN_ivfdF6Yum6enELBNe0GLDLN8NgG6hR20meq_i4NQaRaiw7buewFILJM4O8dSMbER85XrLxCpg-ma938lcq_P8PwqE9rqUKpTK9hYa8Wd0HJD1-Nf9UdHwVeAw04roKH5AbvAPtDUUrOftrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEG4hOUFmfjYyVe_BjqkX-07dPg5-dgcO_tLQq_RciArutEnaLA4MOr31r_AYYxxG1AGqFvXNJcGv2znOtpCGHvmxWOK3k6lZMb63T0Z1O4W9n_dMdnihB-X50AFHuPLmpM-egcqo6HnJlO4IECjVnYpEpCISHarpuVAqUV_LEnLKaq59l6mTkXa8UCCs37Cogm2htRiz5d_T2NjLVbJrV52A20uvhVDuDuQaTimTVS9vU5xUphTTvu9gFoYiHm641SkeV_KkTDecBj6b35GCcK2E1uVj6Xqoi2rIS6AheC5ENtYHqdl4lI_fQb9Zj3CCu7oKi2u5hZ0LbvbV7n0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NeoQBjz6BrOUyW4_eMP0rA8Igh_V0IDy3WvnfsNqVp7HUJSwFWXT3_8fzjKdOIHhIYzgTdS2HjxJe-BQJSbzathWxz3TArISyNrQptOY73SRCMHzUKCv1Ml3BpBN_MX8soJxXU863vz4naiK8hbIorvDIPA3LWSL87GVzVUX7jpvXmjlXKoLjdg7JxW8AYpZcHqBBwsBx7dr3iWTDvQT_sue5UHfplCvA_eHZR_MsHNOuV0gut2D4CVcTTGwFBAv01WTnyiOpV-rJiuESheWmvDuW8klFDt53sOH-lCXZ4Ht-tO7rNqEfXaWoqXjTCepr215foLNXiowuf-JGKe4Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🇮🇶
اخر ما صورته عدسات الكاميرات للهروب الامريكي المخزي من العراق: طائرات الشحن التابعة للتحالف تغادر المجال الجوي لإقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/92161" target="_blank">📅 18:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92160">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔻
مصدر لنايا: ال سعود يقدمون القهوة والتمر للصهاينة في مطار تبوك وخدمات اخرى افضل من تلك الخدمات التي تقدم لحجاج بيت الله الحرام.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/92160" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92159">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇱
‏
إعلام العدو:
نتن ياهو سيستقبل طائرة فلاي دبي البديلة في مطار بن غوريون.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92159" target="_blank">📅 18:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92158">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
حزب الله ينشر:
من مجاهدي المقاومة الإسلامية إلى سيد شهداء الأمة السيد حسن نصر اللّه (قدّس سرّه):
يا سيّدنا... سيبقى صدى صوتك يشعل بنا الثّورة، فنرفض الذلّ والهوان، ونطالب بثأرنا الكربلائيّ من كل ظالمٍ ومتغطرس، وستشهد الأيام ألا إنَّ حزب الله هم الغالبون.
ترقبوا الرسالة الكاملة عند الساعة السابعة والنصف من مساء اليوم</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92158" target="_blank">📅 18:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92157">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شهود عيان لنايا   انفجارات عنيفة تهز المنطقة الشرقية في السعودية .</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92157" target="_blank">📅 18:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92156">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/92156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92156" target="_blank">📅 18:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92155">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شهود عيان لنايا
انفجارات عنيفة تهز المنطقة الشرقية في السعودية .</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92155" target="_blank">📅 18:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92154">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزارة الخارجية البريطانية: ننتقل مع العراق إلى مرحلة جديدة من التعاون الأمني والدفاعي</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92154" target="_blank">📅 18:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92151">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfiCMJC4XIKa9WR59fJjuEM4EZZfUfwXhn7A7qjI3CFyTeJ83BmS0yO1I2ALtBMaJcDr--uhRZC9Efw4p-DbLWNFVsGe_JQQuNZImTAl6yZdwQsh9Lkdu4gtfzzmZRj7aEGEeDrURI57J_7GfHTO91u0bKBQfR535L9AJJCn62bXGwrfZjJEgacUuYeL2jHpGnBSOuMzBT91tfsHKrZm2IAHT44nykSxpel79jXW-0vmO-Me0CIF7GvLSl87yqoLHKCBLXwTwOZ-ZsHL2RXJibw5gFx7fH7VpPqegBqymlCj_M4Z-DOf__0pFLJvIRUuTO4UaubWjFniuu0bcVPEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnzEg8o3jfcNI2l-bFhtFtv3YC6td67MifMxtFUZ0l4Siw1_1noHasMXpjS3EvHObPqNWsI7yKfxAo5Ed6UHKnwavqsC7ynwZlc34Rp0Hs4pksFARC-RWGUKVlJAPqEhM9jVNNNeFFL2JN7973X57oy4Q0UC6XD6rtgmOEb-fpSVv1C_IL_YELtGv0A21maeLIttJx9-Tg3q1mxpk0BrdncdLAW71cvJwM_KSG3_aAR-HjxbJBwiTg-znbq-bQ3xiy5K9qtsg0Ha_p3WHRFD9-c-BZwvufNMOFtN-4OphOLdWo69jNn0NRJtTPIuI2AW5_KzdvjsRYjfyjjbUtwRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfxQOkfZrzOtjpEg2xFzEX0mY8Hg1nb6Im3jtUaoFLUE55eYPcGXSRBAaSw3gqPBpxaTpVQvNzQaBbgpQ413RZ081h4AQWdCogqD4KCpcHT6ghmkryJWO64BS-V9xN7Pb5Vv1I5HDrU6MWyOb-DZxOThUBtHNqCjv-hBwhn3dfEJBwMfRwSiL1U5yPCYvI_Jk2TBQHufq-g87NR57y22eJQx1ZP3NSYfCayQYpODSL6_xV8MSIyCp3P3zr0m3_dybhvLktyprLOY2-CyZdhF8SEa9PpIxAQmTqArN3r5S4nXda9dPpBvZc5qVrScm_Lc7soT03LjIWTMvlnQcdmK8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلاح الشيعة الباشط سودة بوجهة الفرط بيه</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92151" target="_blank">📅 17:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92150">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44874274af.mp4?token=vzk3dL07NtA8VbcwNxsuDx2lSFB0Fy9a4XgaN3xXAAc0xlCpomvu73EP5YiSqCY_L6v7pQCYApbB2GHlpQ8EMnJjdge3cMWOCrGXyokTyFVE_LU15UJbOnx4eBJm6PIMvtLdF5AkLfPHrjMYDwqd6fnqx79Lomsq-ErJutJFwI35pHgEPFTFdmhp5WOTP9iICyotFiGhm1bj2JtFL0nlx18-r9CHjXQNXylO9JXAnSLpM3PDTrkN1S7W29xNPnhZW882sYjIErzcXu-BiAzSJApug-D3ni5cCzsRQA5KOClMV_1VZsr1L7D19Z5dkfBzvBaC03Uw7ndoI_zxiHshvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44874274af.mp4?token=vzk3dL07NtA8VbcwNxsuDx2lSFB0Fy9a4XgaN3xXAAc0xlCpomvu73EP5YiSqCY_L6v7pQCYApbB2GHlpQ8EMnJjdge3cMWOCrGXyokTyFVE_LU15UJbOnx4eBJm6PIMvtLdF5AkLfPHrjMYDwqd6fnqx79Lomsq-ErJutJFwI35pHgEPFTFdmhp5WOTP9iICyotFiGhm1bj2JtFL0nlx18-r9CHjXQNXylO9JXAnSLpM3PDTrkN1S7W29xNPnhZW882sYjIErzcXu-BiAzSJApug-D3ni5cCzsRQA5KOClMV_1VZsr1L7D19Z5dkfBzvBaC03Uw7ndoI_zxiHshvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گالوا ما يضل محتل بهاي الگاع</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/92150" target="_blank">📅 17:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92149">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4557c1107.mp4?token=euEin2G9e2wrtenDhxyuLQbS89O0hxK3OHz_zevJS4DRQfQjHqAoTwz4lPD0BjRtqckxheXQjYcX_EimOQ1j1Z9xHoPKhw2BfDTqXjjNsOR02ii19jgUGUDL7o052hDswkOOEtauH9Pkxx4fGIwUs22t2SMHLgTGKfqHxgdvvheuWCmZc5JCr3_QABbkkTYAwofuP_dgt7ROgYdqRTEo2bKg_rNLJTULvgBjKTVO4Krb9sTDvYMHdRsJxCjHwNX8hsx9tHxuL3TsvvkxY0PJlcGXaaY0Y2UqGkfcu4-EopijdMFHAq2Szsw3iSkbNZyveXr6BBcfunoDduOOIE2B9ZRu666sOAQ99grE4SqGtaOMuCz3DbcpNfBUa9AzOBiECzX3uRVfYA3XN4Yg-YIQeVqTLFSR3iLu1LiU14WAY6DylELRY1RPssm0u9j476DQEL5H6h0VVOJ3LZRPJMMWdYMTt1pTlnSb4Rv28X3HOO5ivk3w5VvyXhbfXwQay5mIu-q8tv9U5q7rT_WXsUIrakKpY5xQbyA0snzPzcz1GY9GBkpZ37-2uE89iwJR64vwLGK_GsEOBTiRm9JQNqTiez2uV3SBb7J_VqczHdyi4DYAFwzw0hlEHCQ9aoai9cpZtsoV6kCS3ZcrUN9amN5kFxT1Eogg-gruDCHxuzLejUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4557c1107.mp4?token=euEin2G9e2wrtenDhxyuLQbS89O0hxK3OHz_zevJS4DRQfQjHqAoTwz4lPD0BjRtqckxheXQjYcX_EimOQ1j1Z9xHoPKhw2BfDTqXjjNsOR02ii19jgUGUDL7o052hDswkOOEtauH9Pkxx4fGIwUs22t2SMHLgTGKfqHxgdvvheuWCmZc5JCr3_QABbkkTYAwofuP_dgt7ROgYdqRTEo2bKg_rNLJTULvgBjKTVO4Krb9sTDvYMHdRsJxCjHwNX8hsx9tHxuL3TsvvkxY0PJlcGXaaY0Y2UqGkfcu4-EopijdMFHAq2Szsw3iSkbNZyveXr6BBcfunoDduOOIE2B9ZRu666sOAQ99grE4SqGtaOMuCz3DbcpNfBUa9AzOBiECzX3uRVfYA3XN4Yg-YIQeVqTLFSR3iLu1LiU14WAY6DylELRY1RPssm0u9j476DQEL5H6h0VVOJ3LZRPJMMWdYMTt1pTlnSb4Rv28X3HOO5ivk3w5VvyXhbfXwQay5mIu-q8tv9U5q7rT_WXsUIrakKpY5xQbyA0snzPzcz1GY9GBkpZ37-2uE89iwJR64vwLGK_GsEOBTiRm9JQNqTiez2uV3SBb7J_VqczHdyi4DYAFwzw0hlEHCQ9aoai9cpZtsoV6kCS3ZcrUN9amN5kFxT1Eogg-gruDCHxuzLejUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانب من الاحتفالات في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/92149" target="_blank">📅 17:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92148">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏وزير الحرب الصهيوني: حادثة طائرة فلاي دبي كانت محاولة لتنفيذ عمل إرهابي</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/92148" target="_blank">📅 17:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92147">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1fc55825.mp4?token=mW3gEOUBaVi0xb1OcGrzBOXhNl5jkgK8lzBKbSj5RgjzT1krNybrrM5Nqp3LxIPfpHYT7HbVwLmxxNeuvR0fZGCSwv9NTsgTDCUtIRzpknCay1S-7sA3NvJ8BwUARD8WPXy3T1e6rOgGBUTdtSGGBLSC3itoObXIApNZdeMVRykesqPt2HXddKuvn8TZj3u286goY6el2pcZkGU5YSr4Qhqp4CQHL6xA8EL38R62-QPnj9qTI5u2TDaInPCrjXh-y1NVQczIi62sYQVTfdzzg1lnyonEKNFDQ2r9sbVdIHYoD9FUDuOsofTxd2HG6xA7zZkM_Dtj8Jusb7KsbCA1bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1fc55825.mp4?token=mW3gEOUBaVi0xb1OcGrzBOXhNl5jkgK8lzBKbSj5RgjzT1krNybrrM5Nqp3LxIPfpHYT7HbVwLmxxNeuvR0fZGCSwv9NTsgTDCUtIRzpknCay1S-7sA3NvJ8BwUARD8WPXy3T1e6rOgGBUTdtSGGBLSC3itoObXIApNZdeMVRykesqPt2HXddKuvn8TZj3u286goY6el2pcZkGU5YSr4Qhqp4CQHL6xA8EL38R62-QPnj9qTI5u2TDaInPCrjXh-y1NVQczIi62sYQVTfdzzg1lnyonEKNFDQ2r9sbVdIHYoD9FUDuOsofTxd2HG6xA7zZkM_Dtj8Jusb7KsbCA1bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانب من الاحتفالات في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92147" target="_blank">📅 17:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92145">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STWTx2lfKkJm2e-cT25y778cUpaaGH4xaBscWJ6gsdudbAxuaXNVLgV2BTdU6356X_oGvD1w3hup7MMlTAOObRX8EqrDN2CBYQEf8FDFaUhFg2NCoJfdgTTCssu9pSyGvs8_U03Ls99lrCINyDQwKxcUtt_Sv72HnHKAeqD48Fv85YIONmOeyI6pLKftaf6E4wztBzmZJT-e_MRN0DaIeQqE5X6xToogKKVsAi4AALKzzVU04Ds0XxHgwBVKegXUXLPrNtmtJBMhaU0bgOOiakn-QzS6zF_67DaFErW__YzNN6cIBCy3MOvS6EM1Dsnlv5t3MxwaKDvHdfOxDLuOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPyyCvZIJsQEWlq31-zaFH8oxzxZkgaC-l-1lPwTgrievPCE_YecLWGQcvrUnSJFvRnKQEO48MRFmDKoatPYHk9REFq7BjxjIsTSmip-gD8zt_t81vxwRrxMK4pC0KIYZowOA1PSwqAxkrV-ZjxjezEWq9QWvlZBts0gbQt_iUmBPkd2czmCIMwqV9RvA43dLSmTP_dCeCIq0Wx89ma1zLOmRKYeeqtH2oROFyv4rPCUa4a4jUsyCF8cEsFOtppX7ZAwZ6UffhYQOGNpd74ztL93H6diMdCFCMzNnkPsDhVQ5XgkvXy0z4YkuyX40BT26jB_2sSKashFmaKhnToHAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعداد حاشدة تحتفل في العاصمة العراقية بغداد بمناسبة دحر واذلال قوات الاحتلال</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/92145" target="_blank">📅 17:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92144">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وختاماً نقول:
منذ أكثر من أربعين يوماً، انخرطت المقاومة الإسلامية من خلال اللجنة الرباعية المُشكلة من الإطار التنسيقي بالاتفاق مع الحكومة العراقية في مفاوضات لبحث عملية تنظيم سلاح المقاومة مقابل تحقيق سيادة العراق الكاملة والشاملة، المتمثلة بانسحاب القوات الأمريكية والناتو وكافة أشكال الوجود العسكري الأجنبي من العراق(أرضا وجوا وبحرا)، مع احتفاظ المقاومة الإسلامية بحقها في الرد المباشر على أي خرق أو انتهاك أمريكي أو صهيوني لسيادة العراق، غير أن رد الحكومة العراقية لم يصلنا حتى هذه الساعة رغم توقيع ورقة الاتفاق رسمياً من اللجنة الرباعية المكلفة من طرف الإطار التنسيقي وكذلك أطراف المقاومة المتمثلة بالفصائل الأربعة.
وبناءً على ذلك، تعلن المقاومة الإسلامية أنها غير ملزمة بأي توقيت أو اتفاق قد تحدث عنه –أو يتحدث عنه- أي طرف حكومي أو سياسي.
إن سلاح المقاومة سيظل أمانة بأيدي مجاهدينا، وكما كان دوماً فأن بوصلته ستبقى موجهة ضد أي عدو يستهدف العراق وشعبه، وفي الوقت ذاته، ستبقى أبوابنا مفتوحة أمام أي حوار يضمن سيادة العراق وعزته والانعتاق من هيمنة أمريكا الشر والجريمة والطغيان.
عاش العراق حرا أبيا سيد نفسه
والسلام عليكم ورحمة الله وبركاته
المقاومة الإسلامية في العراق
30 أيلول 2026</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/92144" target="_blank">📅 17:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92142">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">البيان الكامل للمقاومة الاسلامية في العراق
بسم الله الرحمن الرحيم
﴿وَلَقَدْ سَبَقَتْ كَلِمَتُنَا لِعِبَادِنَا الْمُرْسَلِينَ * إِنَّهُمْ لَهُمُ الْمَنصُورُونَ * وَإِنَّ جُندَنَا لَهُمُ الْغَالِبُونَ﴾
حينما احكمت قوات الاحتلال الأمريكي قبضتها على أرض العراق سنة 2003، فاحتلت البلاد وقتلت العباد، لم يكن أمام الأحرار إلا مواجهة من جاء بديلاً عن الطغيان البعثي، فكانت عبوات المقاومة الإسلامية تمزق آليات المحتلين وتحيلها خراباً، وتمطر قواعدهم بالصواريخ فتجعلها ركاماً طيلة مدة بقاء الاحتلال في عراقنا العزيز، فما كان لجيشهم المنكسر إلا الهزيمة عام 2011 بذريعة الاتفاق الأمني مع الحكومة العراقية آنذاك، ليسجل العراقيون بذلك الانتصار الأول على أقوى جيوش العالم؛ جيش الولايات المتحدة الأمريكية وبإسناد قرابة الثلاثين من جيوش حلفائها.
وما لبث العدو الأمريكي أن استوعب صدمة الهزيمة في العراق حتى بدأ بتعزيز مخططاته الخبيثة وتنفيذها في سوريا بعد تحشيد مرتزقة التكفير السعودي في محاولة لتفكيك بيئة المقاومة والممانعة وتضعيفها في المنطقة، فما كان لرجال المقاومة الإسلامية إلا أن هبوا لفرض الاستقرار والأمن وطرد التكفيريين من أرض السيدة زينب (عليها السلام).
وحينما بانت بشائر انهزام جيوش التكفير المدعومة بالمال السعودي، سعت أمريكا الشر إلى نقل المعركة إلى أرض العراق في محاولة خبيثة لاستغلال انشغال رجال المقاومة العراقية في سوريا، فزحفت العصابات الإجرامية إلى المدن العراقية واستباحت حرمها وسبت نساءها، وقتلت أطفالها، فما كان لرجال المقاومة العراقية إلا التوجه لمواجهة المد التكفيري الذي كاد أن يسقط العاصمة بغداد.
وبعد انهيار المنظومة الأمنية والعسكرية العراقية في المحافظات الغربية وتهديد العاصمة بالسقوط، طلبت الحكومة برئاسة السيد نوري المالكي من المقاومة العراقية التصدي لهذا الخطر الذي داهم العراق، فانبرى رجالها بسد الثغرات واستحداث المواقع الدفاعية وإيقاف زحف العدو، بل ومطاردته.
أما بعد صدور الفتوى المباركة، فقد كان من أدوار فصائل المقاومة هو إنجاح الفتوى باستيعاب وتدريب الجزء الأكبر من المتطوعين على مختلف صنوف الأسلحة وتفويجهم إلى سوح الوغى في معارك تحرير المدن العراقية المستباحة وإمساك الأرض بعد تحريرها.
وفي خضم المعارك مع التكفيريين وبعد أن لاحت هزيمتهم في الأفق، فقد تم إعادة تدخل العدو الأمريكي للمشهد العراقي بذريعة الدعم الجوي ضد عصابات التكفير -المدعومة أصلاً أمريكياً- فتمكن الأمريكان مرة أخرى من استعادة تواجدهم العسكري، ولكن هذه المرة مدركين ضرورة تجاوز خطر المقاومة العراقية باستحداث قواعد الاشتباك؛ فأنشأ الاحتلال معسكراته داخل البلاد بما يؤمن له –متوهماً– عدم وصول صواريخ المقاومة أو عبواتها لقواته، إلا أن المقاومة كانت له بالمرصاد وتمكنت من تطوير صواريخها ومسيراتها بما يؤمن تهديد وجود قواته ودك قواعدها، فكانت جولات المنازلة بما يتناسب وقواعد الاشتباك الجديدة في مرحلة الاحتلال الأمريكي الثانية.
وفي غمار الأحداث واستهداف تواجد الاحتلال طيلة المرحلة التي أعقبت هزيمة داعش، ولا سيما في عمليات الإسناد لشعب فلسطين وإيران الإسلام، استهدف طيران الاحتلال الأمريكي المواقع الدفاعية للحشد الشعبي في القائم وعموم المناطق القريبة للحدود العراقية السورية، ومعسكراته الرسمية في أطراف المدن العراقية، واغتيال القادة في بيئتهم المدنية، وفي مقدمتهم الحاج الكبير قاسم سليماني، والحاج أبو مهدي المهندس، واستمر مسلسل الاغتيالات للقادة ومنهم الحاج القائد أبو تقوى السعيدي والحاج القائد أبو باقر الساعدي، ومؤخراً اغتيال القائد الكبير الحاج أبو حسن الفريجي، وسقوط مئات الشهداء والجرحى إثر الاعتداءات الأمريكية على الأرض العراقية.
ولم يكن أمام المقاومة الإسلامية بفصائلها الأربعة إلا مقاومة الاحتلال بشتى صنوف الأسلحة المتاحة طيلة هذه السنوات التسع، وعلى مر مراحل تغيير الرئاسات للحكومات العراقية، كانت المقاومة توجع الاحتلال بضرباتها الذي أخطأ في حسابات قدرة الوصول لقواته وقواعده مرة أخرى، فكان خياره مجبراً هو الخضوع لإرادة المقاومين والخروج من عراق المقدسات مذلولاً، منكسراً، على الرغم من محاولاته لإخفاء هزيمته بتأطيرها بالاتفاقات وغيرها من الأكاذيب.
إن المقاومة العراقية المتمثلة بفصائلها الأربعة وثلة من المجاهدين الأشداء هم من حملوا السلاح بوجه المحتلين، ووضعوا أرواحهم على أكفهم، وتحملوا أعباء هزيمة الاحتلال الأمريكي، فداءً للدين والوطن، لتكون بداية تعزيز السيادة العراقية.
وختاماً نقول:</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/92142" target="_blank">📅 17:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92141">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f12290f3e.mp4?token=JNWoavXvmMCcTNSu9Xc83OD9j6hZEAenj2ikyrx7HoOpsbMJy7L9sv8dLwhwdl-UmfVzhXRq3-4_xScOtI7T1QoQcg3hMj5dZn1Wwiu6lT9b6Q0sZQRSE5uPlIlEaYIppBBPKNteyve4s54qEaGb_DIu_pgRaAYO_HiYiPhPC5JXo1sNOWx2XLs11vzHW_qG0ONrD8-ztJI6sjCFAvwJk1lEYexJqpAtqZAYCIWFJT8jWDzIxPWKFwOLNIMrSTn8Y7ZWp3uLmhIH_xJae6DaDKpD9pCRuYY8hqzqrjoQpY-_h1rVA1F19yf-f_QGICdRvV0v2pKLBK6Os5touEi93gibOuyNNVDyrDyS4Vs9ve131JAC9j17FViHNCNvvlZQ-gHud28cPIv-XSZ0A3edw1W1C8oIUEFDoKqqHRagUzzsNAUGJcZCIoo1ffjroXBsJmv03cXEM1JzWXrVZALH_bC4cfoEIcwYREfx5w1sWvIw0qRiuKfUmXiU8-Se97Sb9dHn2tAmOhqZ-tpa3qAPBOtZ2HiHrfUXbrccIEoq3ADpdQ8jpSGa22f7OkD58aiv8rKacSBRpaZR5g6HGOre3u3I7NQ6SJyHClqi6EERfKPgDiA6xPJxzAobuBMJcny2X5GRXrnx0f1B3L8eaVFMbnp0yxI7s66rMjYDf8d_v-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f12290f3e.mp4?token=JNWoavXvmMCcTNSu9Xc83OD9j6hZEAenj2ikyrx7HoOpsbMJy7L9sv8dLwhwdl-UmfVzhXRq3-4_xScOtI7T1QoQcg3hMj5dZn1Wwiu6lT9b6Q0sZQRSE5uPlIlEaYIppBBPKNteyve4s54qEaGb_DIu_pgRaAYO_HiYiPhPC5JXo1sNOWx2XLs11vzHW_qG0ONrD8-ztJI6sjCFAvwJk1lEYexJqpAtqZAYCIWFJT8jWDzIxPWKFwOLNIMrSTn8Y7ZWp3uLmhIH_xJae6DaDKpD9pCRuYY8hqzqrjoQpY-_h1rVA1F19yf-f_QGICdRvV0v2pKLBK6Os5touEi93gibOuyNNVDyrDyS4Vs9ve131JAC9j17FViHNCNvvlZQ-gHud28cPIv-XSZ0A3edw1W1C8oIUEFDoKqqHRagUzzsNAUGJcZCIoo1ffjroXBsJmv03cXEM1JzWXrVZALH_bC4cfoEIcwYREfx5w1sWvIw0qRiuKfUmXiU8-Se97Sb9dHn2tAmOhqZ-tpa3qAPBOtZ2HiHrfUXbrccIEoq3ADpdQ8jpSGa22f7OkD58aiv8rKacSBRpaZR5g6HGOre3u3I7NQ6SJyHClqi6EERfKPgDiA6xPJxzAobuBMJcny2X5GRXrnx0f1B3L8eaVFMbnp0yxI7s66rMjYDf8d_v-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتهاء كلمة المقاومة الاسلامية</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/92141" target="_blank">📅 17:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92140">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcc56e602.mp4?token=dlG_dNiCERNu8JbJnitBDEylZajr-HAJWb6bA65hwJ06k8Wr1FbwblG-yvjIyoYerlQTUBtLGOJmXBy_2kfhx23iDE22GsoMx47yxMFaS6esVkAlYH1h-XKmZbTyzIK3jfBvQHUf7ywbqNXUzo05XaF0JJt8rSUl5dFTgMA-AwTMFCLvO5mno4_8LGkbfvtwpBTTufGkzuULsUJnztp6nr2R1hMc0nswEhmS6XkjnOBXHY2bJeSR1GNyENh1qWNsUTOKqp3wrG_yh7Ko5Tmva1RoPzFDwHbw7ipPU4DoqB9GUgjb4mOU1dCAd3Js5JNEGeZdhsqAYyvutRfFAgkWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcc56e602.mp4?token=dlG_dNiCERNu8JbJnitBDEylZajr-HAJWb6bA65hwJ06k8Wr1FbwblG-yvjIyoYerlQTUBtLGOJmXBy_2kfhx23iDE22GsoMx47yxMFaS6esVkAlYH1h-XKmZbTyzIK3jfBvQHUf7ywbqNXUzo05XaF0JJt8rSUl5dFTgMA-AwTMFCLvO5mno4_8LGkbfvtwpBTTufGkzuULsUJnztp6nr2R1hMc0nswEhmS6XkjnOBXHY2bJeSR1GNyENh1qWNsUTOKqp3wrG_yh7Ko5Tmva1RoPzFDwHbw7ipPU4DoqB9GUgjb4mOU1dCAd3Js5JNEGeZdhsqAYyvutRfFAgkWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد جعفر الحسيني: رد الحكومة العراقية لم يصلنا لهذه الساعة</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/92140" target="_blank">📅 17:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92139">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">السيد جعفر الحسيني: عادت القوات الأميركية للدخول إلى العراق بحجة محاربة الإرهاب</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/92139" target="_blank">📅 17:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92138">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">السيد جعفر الحسيني: انخرطت المقاومة الاسلامية في مفاوضات عملية تنظيم السلاح اي سلاح المقاومة مقابل تحقيق سيادة العراق الكاملة المتمثلة بانسحاب القوات الاميركية والناتو وكافة اشكال وجود عسكري اجنبي برا وجوا وبحرا مع احتفاظ المقاومة الاسلامية في حقها للرد المباشر…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/92138" target="_blank">📅 17:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92137">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">السيد جعفر الحسيني: ان المقاومة العراقية المتمثلة بالفصائل الاربعة هم من حملو السلاح بوجه المحتلين وتحملو اعباء هزيمة الاحتلال الاميركي</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92137" target="_blank">📅 17:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92136">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">السيد جعفر الحسيني: عادت القوات الأميركية للدخول إلى العراق بحجة محاربة الإرهاب</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/92136" target="_blank">📅 17:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92135">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">السيد جعفر الحسيني: عادت القوات الأميركية للدخول إلى العراق بحجة محاربة الإرهاب</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/naya_foriraq/92135" target="_blank">📅 17:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92134">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hj-diPHgerYL4_-J8h0It68IgG48KnSjKsN-BJA7W3OLNYDDDNVb0b_3Tv2QohTf1D5s5ON7Xz50GziCpeISAvSsZn1sRM9J9N97dQOiRV1BkY6GXzqXioRMQCw-mkaugwHFVYaDnKAKU3vtchZPl2jjZnKaFoLW0ZbMoZmRAUukwlfNTd0mzt-4_kF-nu-yQQ6tqkSZBzQvq-ylyqCH6TXzPJC_Jeh_CbGgrYO5Ppoe8VQGN0oarSXiT6OpocA_WE_12TgerPoQuIXA0TYlYqVVjWIBLFGq7Qn9Mfo9Hrbc1WBLH0JVaZYf3RhZEBpNCtlqI7ScV8Vkfg89GGQHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد جعفر الحسيني: بعد صدور فتوى المرجعية كان دور فصائل المقاومة إنجاح الفتوى من خلال تدريب النسبة الأكبر من المتطوعين</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/92134" target="_blank">📅 17:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92133">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518dc989ba.mp4?token=H6ywncx6kEfUx2z2DItSbb5Kzuw6FCDe3DMVEA6eRWrtv1ro1TQP8eelkHiMkjeG5AE2LMpiIi3bbqF2Vhhlgnl9kl2VkGfi4Hgzelphlkrkis9cljyNmUW3NCkpx8axl8h109poCJJlCd4sIvS-zjoNyNMmc2IizJ_GbsmN-j0O5Q2g8QH49gyM74hqGGYE1n7qA8Ja2-uhCZdhawkuYmUluBnaxJDlHK5AkSJiVeYjJBVG9SNcdgqK3C7IZV0kXPFrOYlJwBFe3k73_Zwpq6z9FmGnCUzZelOfFmPkKlP6ixhrpK8Dn5frnY2bS_ExeMd3uBL29ZX6NC8pGGQgFLd0y95GTItPosw4jIjHr1UAJdG5UiHyc3C8zxXKhxzl4qEN4BEMXDTn6zLpnmkARcKhnmvs3YP5-iXeo4NY6O9NdKpUMXIZCjnitSsQ6UjHbr3Cl5QaJS6uFkSSe2RsLa1tRvtB_6sX-58HRowJait-8qijBEYPECg0YO0HMWMHyS0Zjbe-nX4274jF1_lHVG_2fJgZJacjdk-VwcYwSoMKb5dfC7fhUpUdP0Y-TdAp-58f0XkC2AaC5cVLRbitFDyUWLIYHL3mvIng7eErlnqaxaQn7JzdcVQiDVhxlaxTvYHYpOWff_KC954QI4ihjb18OxlcOSFk1q2DvxsW_QE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518dc989ba.mp4?token=H6ywncx6kEfUx2z2DItSbb5Kzuw6FCDe3DMVEA6eRWrtv1ro1TQP8eelkHiMkjeG5AE2LMpiIi3bbqF2Vhhlgnl9kl2VkGfi4Hgzelphlkrkis9cljyNmUW3NCkpx8axl8h109poCJJlCd4sIvS-zjoNyNMmc2IizJ_GbsmN-j0O5Q2g8QH49gyM74hqGGYE1n7qA8Ja2-uhCZdhawkuYmUluBnaxJDlHK5AkSJiVeYjJBVG9SNcdgqK3C7IZV0kXPFrOYlJwBFe3k73_Zwpq6z9FmGnCUzZelOfFmPkKlP6ixhrpK8Dn5frnY2bS_ExeMd3uBL29ZX6NC8pGGQgFLd0y95GTItPosw4jIjHr1UAJdG5UiHyc3C8zxXKhxzl4qEN4BEMXDTn6zLpnmkARcKhnmvs3YP5-iXeo4NY6O9NdKpUMXIZCjnitSsQ6UjHbr3Cl5QaJS6uFkSSe2RsLa1tRvtB_6sX-58HRowJait-8qijBEYPECg0YO0HMWMHyS0Zjbe-nX4274jF1_lHVG_2fJgZJacjdk-VwcYwSoMKb5dfC7fhUpUdP0Y-TdAp-58f0XkC2AaC5cVLRbitFDyUWLIYHL3mvIng7eErlnqaxaQn7JzdcVQiDVhxlaxTvYHYpOWff_KC954QI4ihjb18OxlcOSFk1q2DvxsW_QE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد جعفر الحسيني: بعد صدور فتوى المرجعية كان دور فصائل المقاومة إنجاح الفتوى من خلال تدريب النسبة الأكبر من المتطوعين</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/naya_foriraq/92133" target="_blank">📅 17:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92132">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">السيد جعفر الحسيني: هبّ رجال المقاومة الإسلامية العراقية لمواجهة المدّ التكفيري الذي كاد أن يُسقط العاصمة بغداد</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/92132" target="_blank">📅 17:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92131">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">السيد جعفر الحسيني: ما كان للجيش الأميركي إلا الهزيمة عام 2011 ليسجل العراق الانتصار الأول</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/92131" target="_blank">📅 17:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92130">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بدأ كلمة المقاومة الاسلامية في العراق باحتفالية اخراج قوات الاحتلال الامريكية من البلاد</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/naya_foriraq/92130" target="_blank">📅 17:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92129">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d5329142.mp4?token=czGw_FpB_5Fs9OxL1m_bGJp0Myu3TUtNANMdr2s-dC2vGvey_64sgt0hps8NTXo59ncLKL3cnRORPprZGlT_zULCgjHkKieCnXzcRr9gIif-mWcndJ-WIEo5tYwB9_Qn0ujUT8DqpoTXFf2uqwxcIwROnTHWcw35HfKjAzCl1QMRqlo0UL60nBKTxkWvSn11qaWHP9WyJ6iwlDllASJj-43Bvwzjt95yrsCKRlA0cj02tMERzgBfad1jtli6lp7bgVbXJxxZbeuZ3RgyAcLXyJBpuiASQLIy6M6sdZ3ZyJ0sAI-BuJD9-WnyK-v0FxxcXjCsUN9iKa7OfX0M37dKNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d5329142.mp4?token=czGw_FpB_5Fs9OxL1m_bGJp0Myu3TUtNANMdr2s-dC2vGvey_64sgt0hps8NTXo59ncLKL3cnRORPprZGlT_zULCgjHkKieCnXzcRr9gIif-mWcndJ-WIEo5tYwB9_Qn0ujUT8DqpoTXFf2uqwxcIwROnTHWcw35HfKjAzCl1QMRqlo0UL60nBKTxkWvSn11qaWHP9WyJ6iwlDllASJj-43Bvwzjt95yrsCKRlA0cj02tMERzgBfad1jtli6lp7bgVbXJxxZbeuZ3RgyAcLXyJBpuiASQLIy6M6sdZ3ZyJ0sAI-BuJD9-WnyK-v0FxxcXjCsUN9iKa7OfX0M37dKNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بيان المقاومة الاسلامية في العراق يقرأ الان.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/92129" target="_blank">📅 16:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92128">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇶
بيان المقاومة الاسلامية في العراق يقرأ الان.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/92128" target="_blank">📅 16:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92127">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040edd486e.mp4?token=XWbq2XAoS1yEs9AAKmG6Tw03CbzeQ2AkiCuwhF07XzoIm--3mS43xQww8HLZr28Hm0QJnkzYXyv-1msKDaJl5Iz5e0I0j6CigBq8s7O_2UNiWJSKVDK07Xkkej-X3HrB1lQ19M8-XuAJ-4e7vUs2zSrDYX1Gi1EHuqO3nLQbuMYN9GdDAn9ITztoJoz4QujnzticezaPB3x5RHi4ISjEFlbiibsfg3ftoRiGAlhgjDaZRolF8WQaW5p8m_CvHykaecoP_yT6weJS9qlwh9QDPWVDaLObFCR7WN-FOa5gwuIfX5K7yGgPsiG--TetKFggJYRA_VXukwEamMBKeExhcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040edd486e.mp4?token=XWbq2XAoS1yEs9AAKmG6Tw03CbzeQ2AkiCuwhF07XzoIm--3mS43xQww8HLZr28Hm0QJnkzYXyv-1msKDaJl5Iz5e0I0j6CigBq8s7O_2UNiWJSKVDK07Xkkej-X3HrB1lQ19M8-XuAJ-4e7vUs2zSrDYX1Gi1EHuqO3nLQbuMYN9GdDAn9ITztoJoz4QujnzticezaPB3x5RHi4ISjEFlbiibsfg3ftoRiGAlhgjDaZRolF8WQaW5p8m_CvHykaecoP_yT6weJS9qlwh9QDPWVDaLObFCR7WN-FOa5gwuIfX5K7yGgPsiG--TetKFggJYRA_VXukwEamMBKeExhcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حشود غفيرة تحتفل في العاصمة العراقية بغداد بدحر قوات الاحتلال الامريكية</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/92127" target="_blank">📅 16:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92126">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇱
نتن ياهو: أحيي الأبطال الذين كانوا على متن الرحلة القادمة من دبي والذين أظهروا براعة وشجاعة. لقد أصدرت تعليماتي للمؤسسة الأمنية بالاستعداد لمزيد من التهديدات المحتملة.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/92126" target="_blank">📅 16:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92125">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb80e777a.mp4?token=WEoH2OEfWly--nadkdCAAqNPrE8CYFH7DL-FPwPtB4okoVg_PCiha89rkMToP5CYq4xxHYfgNFc5EyHFTjQtE8z2NBicHCztK5DEpjiaKNcjX9tz216rcRChSunmP9OnAmzdRlJmuxhSuFfL-48tuQOjftTsw4b6lBoXcMOKVU9KR1npw2LhOIDy6y5YNBQjEp8StQ3MRTXnUIm0Zf3VU367H6YB0e75BLfBzZ7vaNKkcSSUxLcUMrgM1y5JymjXZPPssjV9t7YOQ4VlSgjiibApRcc0DB42SZodZuQwOqOGJ9z6cwWYI01ftfkLQXRJ-Myi762woGXjz7qGyWXFdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb80e777a.mp4?token=WEoH2OEfWly--nadkdCAAqNPrE8CYFH7DL-FPwPtB4okoVg_PCiha89rkMToP5CYq4xxHYfgNFc5EyHFTjQtE8z2NBicHCztK5DEpjiaKNcjX9tz216rcRChSunmP9OnAmzdRlJmuxhSuFfL-48tuQOjftTsw4b6lBoXcMOKVU9KR1npw2LhOIDy6y5YNBQjEp8StQ3MRTXnUIm0Zf3VU367H6YB0e75BLfBzZ7vaNKkcSSUxLcUMrgM1y5JymjXZPPssjV9t7YOQ4VlSgjiibApRcc0DB42SZodZuQwOqOGJ9z6cwWYI01ftfkLQXRJ-Myi762woGXjz7qGyWXFdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعدادات كبرى   بمشاركة جماهير فصائل المقاومة العراقية مع ابناء الشعب العراقي   للاحتفال بالخروج العسكري الأمريكي المذل من العراق</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/92125" target="_blank">📅 16:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92124">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇱
نتن ياهو:
أحيي الأبطال الذين كانوا على متن الرحلة القادمة من دبي والذين أظهروا براعة وشجاعة. لقد أصدرت تعليماتي للمؤسسة الأمنية بالاستعداد لمزيد من التهديدات المحتملة.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92124" target="_blank">📅 16:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92123">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الاتحاد الاوروبي يمدد منع الطيران في المجال الجوي للأردن حتى 16 أكتوبر 2026</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/92123" target="_blank">📅 16:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92122">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الاتحاد الاوروبي يمدد منع الطيران في المجال الجوي للأردن حتى 16 أكتوبر 2026</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/92122" target="_blank">📅 16:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92121">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwkHBWDeY5uzzZJdMuhPbd4WU7pmXRULhIPtXkBXioyZVu8V-5VKY_QvxqAshYzupP9rX0rzRL0OrE_hTT50ihzlpg7TYFsVnY_xZe80VDau70Y197k7PS6OOAfsg5hjjnxhuC7k13B1cBxWggIxj576Wvzb8gfHkBo6pd_ihVizPT70I_3u9qmCcEajFVtCMxPO0A4PspdMqRy7kbmH7FuOqFL0-_nw32v2ujvCy_RG1lamTTKvc-jwURkdGwdtYKdqT6Wy9E8YIBH9cGAYlXl-OtHLaJiQCy3CJn0-SeztENBJm1edrQupvFYKWFQ-BS5JWEEqSFv32-poAm-I1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اربعة من حمايات النائبة عن حزب البرزاني نازك احمد يعتدون على شاب في قضاء خانقين ضمن محافظة ديالى بالضرب المبرح بسبب تغزله بالنائبة في تعليق على الفيسبوك.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92121" target="_blank">📅 16:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92120">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رئيس الوزراء الصهيوني الاسبق إيهود أولمرت يزعم ان الموساد استخدم الذكاء الاصطناعي للمرة الأولى في العام 2008 أثناء عملية اغتيال الشهيد القائد عماد مغنية</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/92120" target="_blank">📅 16:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92119">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAla1Cciwaxnbv1YnjScJAffCvaEjdBeJwToHOzZePP-BOD1xCKOvQu-Xt2rIxjhCZPwO9fhCkLEtXDhyZwxkHPkA6Bq8jgiBttoLU0HOKI9qsI-quUhTp6xRkcHAsUbNmYvZLf81CMELyeSM4ieQvPvwjx93TJAjHUAtbctv5Dyjm5ItRkKSyfnqLxRUFOe9BYdEXuIhCTIXAzzDBXIo2V8AjMgbY5j_mGX2h6fEqcqRqbMGEpb91zRSA2DxspoZiN1KD0kUXxURmdRJh5luLVgCsUKhpDKeVelTySWewg9P0rsr3v2Eh70E0TNo-x3es9NT48BVZ_Tj7274znG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مصدر لنايا: ال سعود يقدمون القهوة والتمر للصهاينة في مطار تبوك وخدمات اخرى افضل من تلك الخدمات التي تقدم لحجاج بيت الله الحرام.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92119" target="_blank">📅 15:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92118">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_a9WvaSsZR4nHt7oTnBx8oyaA9Vl7s1mut8Y2CIhPYKMLD-9luaT_-jF-sbG8CPoATujeSeEAu4U5Tc31zBGqZ4P3ntMTpa3Qf3Lxp3-fVoFiEjsCD8k7T0mitXVqBS65gWp1czH49I9RI48essBctoW2D4ju4rXtWpf73WP9fTlKKQCT1HCsiOGlaadQ5BS4RCBo7x4pdsYxPCtow2_EPYEmP1E7lG9lsFu0nsK03ld2NsaOskoSXwTbW62nYDJ0axBxU6aMWKHxNZbTmotqe0KLm2eKDpuIeBrJ8XNX86mL8DUMprwIoaf9Rqh4IVqFOgvbUDiab35qy_lSql7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام العدو: الولايات المتحدة تتعرض للسخرية في العراق.. الميليشيات تحتفل في الشوارع</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92118" target="_blank">📅 15:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92117">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مكتب الحاج هادي العامري ينشر
سنخرج الأمريكان اذلاء</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92117" target="_blank">📅 15:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92116">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f367381d4b.mp4?token=v1JsFNcxbrYVoYvO3No1c96OtC3UwY5b3FdpjskScUMkubpvnxnj12wXlnqag3LkP8I7cIZ4DH3_LzUeTa1WXDyV5au8zAcU-4mB0yBRwJK7vcS5TDU01jozDnkiVhXBb7yaK3mzP1MggMl2e7bbzgnt3sCWIBFKW8Ki--cR5GMkj3UkFqo-R07MXcWUgqfd7L3rUv3D1LXUhsMOaO4f5mSvcGH_kmX_4g_gaqjaB96H2NmM3EeKmMrbNvr34Encv79c2GuHz87vzLutPuc1rUtkragPL94jFyX3382tB0hVK2B8bvrFOAhqOFlYkR7FFTWbTH_8swd5Zwq5f5dWHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f367381d4b.mp4?token=v1JsFNcxbrYVoYvO3No1c96OtC3UwY5b3FdpjskScUMkubpvnxnj12wXlnqag3LkP8I7cIZ4DH3_LzUeTa1WXDyV5au8zAcU-4mB0yBRwJK7vcS5TDU01jozDnkiVhXBb7yaK3mzP1MggMl2e7bbzgnt3sCWIBFKW8Ki--cR5GMkj3UkFqo-R07MXcWUgqfd7L3rUv3D1LXUhsMOaO4f5mSvcGH_kmX_4g_gaqjaB96H2NmM3EeKmMrbNvr34Encv79c2GuHz87vzLutPuc1rUtkragPL94jFyX3382tB0hVK2B8bvrFOAhqOFlYkR7FFTWbTH_8swd5Zwq5f5dWHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منصة المقاومة العراقية من منطقة شارع فلسطين تتزين باعلام فصائل المقاومة الأربعة التي واجهت امريكا بالعراق بالتزامن مع الانسحاب الأمريكي المذل …</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92116" target="_blank">📅 15:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92115">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d02a4d60a.mp4?token=to8EkVf9v0GCnieijAmoTpwpMjSSG68B-OoeeHfmNcJNtWBDEOj8wli4MR-l9Wax3VP6PTPlfRh2UFoDqAVrOPi8LgDposyYsLlH1CuCTWFmlS7qEz-6IXly8yo4RzSq4qkHRFO7_AfG9acyQuBM3YjztQpJkrMpO4Da369rsImJACWpNFvm4gs8IB62Li_dv8uts8SKg9ukOulPuTCVZbSFHfG24Vj7hKSGD0V4P4ckFcyPyRMI6wKc2mn0CQLYzlXzIhGQC0Js_fLQn_kWgWGkd2nQaZs74zDd3FMCJKIpb4F7kaZ1NP-TTmit_V7AeaA6uqokKG8iKAXGN5rc8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d02a4d60a.mp4?token=to8EkVf9v0GCnieijAmoTpwpMjSSG68B-OoeeHfmNcJNtWBDEOj8wli4MR-l9Wax3VP6PTPlfRh2UFoDqAVrOPi8LgDposyYsLlH1CuCTWFmlS7qEz-6IXly8yo4RzSq4qkHRFO7_AfG9acyQuBM3YjztQpJkrMpO4Da369rsImJACWpNFvm4gs8IB62Li_dv8uts8SKg9ukOulPuTCVZbSFHfG24Vj7hKSGD0V4P4ckFcyPyRMI6wKc2mn0CQLYzlXzIhGQC0Js_fLQn_kWgWGkd2nQaZs74zDd3FMCJKIpb4F7kaZ1NP-TTmit_V7AeaA6uqokKG8iKAXGN5rc8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بغداد تحتفل بالخروج الأمريكي المذل من العراق</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92115" target="_blank">📅 15:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92114">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac267d21ae.mp4?token=LOj2rKp_acsqse8Ve_nDXUw_rNCLAWW0w1nNQjpdTbNC-cKsdBpNcEDu-mGJhrYBx1xacoI96Ovn10_U6g4SrluZojlWuphWbBuOSKOw6rcFUXMRY8eRQwdBskVQMYP8wgy4aqDxZcLJw6KXGIDkxJ012VnzP2KW0OR1ZvC8eBblDlhdO12D8Qx1Cb-VugA94RxNzvxl87G69JLGkZmUmU_vJil0htDsYk8Tx4cxRhc06CgtbcGBTapLEWIPyxJoTPlrvp0SCFrI6nMogwg9CdFrAIGD7D32zRmDL1ScHP1HGmTqezspSYyJTmXphV4KxL4bYo43tUb7UwPNTgo95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac267d21ae.mp4?token=LOj2rKp_acsqse8Ve_nDXUw_rNCLAWW0w1nNQjpdTbNC-cKsdBpNcEDu-mGJhrYBx1xacoI96Ovn10_U6g4SrluZojlWuphWbBuOSKOw6rcFUXMRY8eRQwdBskVQMYP8wgy4aqDxZcLJw6KXGIDkxJ012VnzP2KW0OR1ZvC8eBblDlhdO12D8Qx1Cb-VugA94RxNzvxl87G69JLGkZmUmU_vJil0htDsYk8Tx4cxRhc06CgtbcGBTapLEWIPyxJoTPlrvp0SCFrI6nMogwg9CdFrAIGD7D32zRmDL1ScHP1HGmTqezspSYyJTmXphV4KxL4bYo43tUb7UwPNTgo95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منصة المقاومة العراقية من منطقة شارع فلسطين تتزين باعلام فصائل المقاومة الأربعة التي واجهت امريكا بالعراق بالتزامن مع الانسحاب الأمريكي المذل …</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92114" target="_blank">📅 15:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92113">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJDD5uIR11SaJgn35BPjlvapwe3AM-YhgPWrI4r_g4mYN3L0syIQUvNp8i2B-BayWvYaGhTaJKcoCpcC2j1-TnpSaqyxom0MZLLM9clB5C1jF1njOLKSDEXxls8hCgZbVJ3i3bzP8F_ONoZKgi3tGoPoN6cZApDdb7WY6-XAN6ilc2VJ3kJDr1oRqIllxfkZI0WGtz7dCK_qT-VfGSyirgRPM2oJ8v4NS_nZ0QRWKZ2ZZbeFQfABJKCk5nuLMn6PsnhsK60fXFzxBazuOcJz3B7apQJ358rzQdU2lpYejEV0jrYceJ9tAl12PZClggu67x_AF1hmqtCznOoYcnRdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كتائب حزب الله في العراق الميدان</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92113" target="_blank">📅 15:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92112">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8a62a5be.mp4?token=F6ZrEWI9-pq7EK4OEGuW3VJnsjSUiN741Nqr-r6Kav6CetKqpT1XB4cZSS_kexoO-vrro7thskxGa_oYWNixnhKG9Vo89J-EhG8RT01I5ttrEgLTspLB46Sulvrw4Vop73KcBQYsLSYse_X5u0AkMh-yRbFNncJzVo3YOKi29Abk543N_v22ZXqHvPN1APeIYNoJJ-ed1cJsMA99hFdtNsJlmoeJ67-j1FNINWirSjU4KBgykptPufS4BI6_OZ1xLV-GeJCNXot5vU4kvj4VXnj7sE_NqeYOi02R38ZLBZuemh1X2Ja02HPRD0untKRiRDuAnKuSv8fxZCzXzCm8aUdPBxK3q-bTkotxr74fVd71TtmzybDb5nOr1XyvpPP4IzxXcmEV7klkJ-0_GR1ZHgmBDBQShv7hxHWJjyU-2nNVo5mJRzZmiDAzoDNU1TRLZSeFGSevRm24IKxYI712P8HRffs8jsmQCTwujug9DakE45cunJF7HDBWIM6NGg152NHSWFylvKsj8Fw9u9hVXyWP8d-PAjoW6cklkRb2Vgb3Dy4xYaWdw6QyTbUAAvWMtHvFVp-l18rKi2Q2Qk1jFYzcKEBFbVxibrUmhXQ5ZccCmOiAbZvf1xyoX59sio63MSFY12ElqkFZMFlEgrG1vBZInyaIwOrP_mMv7aw3KbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8a62a5be.mp4?token=F6ZrEWI9-pq7EK4OEGuW3VJnsjSUiN741Nqr-r6Kav6CetKqpT1XB4cZSS_kexoO-vrro7thskxGa_oYWNixnhKG9Vo89J-EhG8RT01I5ttrEgLTspLB46Sulvrw4Vop73KcBQYsLSYse_X5u0AkMh-yRbFNncJzVo3YOKi29Abk543N_v22ZXqHvPN1APeIYNoJJ-ed1cJsMA99hFdtNsJlmoeJ67-j1FNINWirSjU4KBgykptPufS4BI6_OZ1xLV-GeJCNXot5vU4kvj4VXnj7sE_NqeYOi02R38ZLBZuemh1X2Ja02HPRD0untKRiRDuAnKuSv8fxZCzXzCm8aUdPBxK3q-bTkotxr74fVd71TtmzybDb5nOr1XyvpPP4IzxXcmEV7klkJ-0_GR1ZHgmBDBQShv7hxHWJjyU-2nNVo5mJRzZmiDAzoDNU1TRLZSeFGSevRm24IKxYI712P8HRffs8jsmQCTwujug9DakE45cunJF7HDBWIM6NGg152NHSWFylvKsj8Fw9u9hVXyWP8d-PAjoW6cklkRb2Vgb3Dy4xYaWdw6QyTbUAAvWMtHvFVp-l18rKi2Q2Qk1jFYzcKEBFbVxibrUmhXQ5ZccCmOiAbZvf1xyoX59sio63MSFY12ElqkFZMFlEgrG1vBZInyaIwOrP_mMv7aw3KbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر لنايا: ال سعود يقدمون القهوة والتمر للصهاينة في مطار تبوك وخدمات اخرى افضل من تلك الخدمات التي تقدم لحجاج بيت الله الحرام.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/92112" target="_blank">📅 15:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92111">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">العراق سيد نفسه</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92111" target="_blank">📅 15:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92110">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">عشاق مواجهة امريكا في الميدان
السلام على قاذفة حسام الحميداوي</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92110" target="_blank">📅 15:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92109">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/92109" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">واحد معطب السرفة و واحد معطب الهمر
#شاركها</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92109" target="_blank">📅 15:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92108">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الكربلائيون في الميدان</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92108" target="_blank">📅 15:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92107">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBvrGhLCST2s8Pxg_yO_CHQgyU198qaaK6WlvGXVdtf0UyqJR0exJ3zb8ZaRylU4j_9IsdCa0jxzSMi1wpZbwymlfl58SzUWpwzsTwZddelJzdNYt1fQ5_uxxsN3WZT2XZeOfC-FGj1_FOD_d_idH9txjbwhBfPYtmTsBVXcO3sTD0Rt0wYYo0GPyN2k9-jd3Co_ZVwPgtN5Q7Xy9Vm1gowqj2uhtRgBGp9VWSEkwJxdg8XBaVuk1vvMnJGZXbsBIEiwgq0Nvjm_dNFICTmR2ylqTfHPytSFskeQpzjObuSUkOu5f_zupcU0bDr-p8uSrR82d3llO594zMWa10P1CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العراق سيد نفسه</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/naya_foriraq/92107" target="_blank">📅 15:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92106">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2kLvfF6NILpxl4k3LEyXOaMSLsWAfIW71YXn1Yu8QdPIe3iOpzvDOxOXCoFvJV_c0_hCf9xRY0xbpjiF6xBjVFHRkY7vFLAD6tNTdLefJxiiXoMZRvZMTbOqhiKDfW2_-zgW7rEtf-Q1T4JAPq-tXfHYcdjJGRwG9KLJ1pBhXEY8-nLbxlwWBJujHkQ5OvXBujWgYM3Y5ErVderRkt1545WoRFLDyFp4UhWrAzHPXQcQ-68sM96_ppxjuAGYCD61_9yRN8sgoQbpU-uDE_U2Hp92zCQPP3OOsY0ofBg2bvBjEGlIxMwPZZb9NxkSmlzp0i-PlbGoo0jFNIJe4ggOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات من الرعب عاشها الصهاينة داخل الطائرة المتجهة من دبي الى تل ابيب</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92106" target="_blank">📅 14:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92105">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
كتائب حزب الله:
بسم الله الرحمن الرحيم
إن طيران العدو الأمريكي التجسسي والحربي لا زال حتى هذه الساعة يعمل في الأجواء العراقية، وهذا ما وثقته استخبارات كتائب حزب الله، فضلاً عن وجود برقيات لحركة أفراد قوات الاحتلال الأمريكي لغاية 30 تشرين الأول المقبل من هذا العام، وسيتم الإعلان عن تفاصيل ذلك لاحقاً.
وكان المسؤول الأمني قد حذّر سابقاً من (كاشير) الأمريكان في مكتب رئيس الوزراء</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92105" target="_blank">📅 14:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92104">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUc7K_4WgvjTwLh6_mY6s2EzvwvSf6I606Ea-7ezh-_fIdeheUBU3hN6xhkXtzNnQD4fyokkW-gHtMTJZX6ZV50pTkecwgVEr77AM6TmHiXUobWGbAw4LEinHHXJ7aioK5SFFz5C6lv7xrjng6fQ4jXNEEt3egR9M-OW_jP1Z01vBL6_JzD-k4XCpFgxXZe0pktPd4HyC2D-SaJQhn-H1LWDnIvlFVlvkeZKyaCs3QAZtQc1MsRC5QQv7iAh8_VRZtraRUAoze9Ye61KBXAVw1f5bl4WuX-8WWiznGzFevua82oRHW_jMYVSk67qJFzcQ1XRaRsd0Si6BU1xRub8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92104" target="_blank">📅 14:53 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
