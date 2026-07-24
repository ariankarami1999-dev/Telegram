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
<img src="https://cdn5.telesco.pe/file/oCRfMHctDv52afti7MeH-h-_cA5m1j7NwspSUXMNMLQHQNSGkUCnqtozIL96feFaNMHLkUjV3vtRkwoiG_8aVaO3nWjHSxeGYPQEfjXaNu6wyK5FgncfrifKt_lWrIAeKyJufjuGv13meGpcxED2491AgyrReStQjt9OZuP1CwJN7XKEUSHe9HTaKnv-zMzkf07atj89DgXUoOn627D7vDAle6Jme-wGCe2XOxi2Iq2rXY8EInYSyOan2lZ54Ex9XfC7Wy8EQMBv9zfNdO28hpNz4wxk9azZa_59zuiCFud_zkzEWDt0oxQgGe9Npxj6PSt73zQ7WYzDMH_2wBGAzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 534K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 17:17:09</div>
<hr>

<div class="tg-post" id="msg-101786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzLDowtEaEwmYu3s6WFGqSZfioBM-EK6Cx7NMSri2YxyoBPqrWV6E9bXkM3oWdc7Ik2cGsWSUb1_bwFz3gLHLEqEXYPSjQtIF444adA_CgBBEtakfQWXiDSIvK6N8RprY2v6gSwKUb-pIS3hIyXqXv3OoJi2nxOOcitCz4DDnTsZNRQQMcacAEfKlCGV0vtZgEiL9cZX2y-q2Dcn6NhSBlyimeAzOBVJxb4mEgFxTNsG0--VHSj0hqjqh1QYNFPVC82c8NYJziPfd2ilLDlpzt-i6y35f8A0l1IqS7JBwXLDCXC4GZvI_8ItS9OIL3yhTRs24QfxSeZugBdJSzviag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسپورت: منچسترسیتی با توجه به شایعات جدایی رودری، مارک‌برنال ستاره جوان بارسلونا رو زیر نظر گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/Futball180TV/101786" target="_blank">📅 17:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/101785" target="_blank">📅 17:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101784">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnoKGlEEvvZ5NJFspNoAQjhWZrDLmQ0UtXD8-pauxgeiwt3bOBCyD-ju3orc08yW7d3AL5Z4ZUG7mCry7MK_7etdT9Z5raYcVxQGVM8ovKWp-VN2CaSVKbwwTQ-grSdo_OX2YImWoKwx3LquG2v_yyG-lQiqPhOljFqpuQPF1-lrOs9cZk-zvXGIVsYOXSnVL2e5Ov4uq7W5XYlUWO9AFzsCsjZsVmo9eHBOGM5zxqHEfm2-bCI0EK22v6rMX-H6tGxj7hQBoRzBeIsTGoy3JsaQ22wGIkBZlY-tzp2DGDYZpV91kJPX9YOM1RqYwFlL6N9tRMRSUKBHnLJTxvfx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇹
✔️
به نقل از گاتزتا دلواسپورت، آندره‌آ پیرلو سرمربی جدید تیم ملی ایتالیا خواهد بود و این قرارداد به زودی نهایی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/101784" target="_blank">📅 17:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101783">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌قایدی ستاره تیم‌ملی ایران: اگر میخواید عاقبت بخیر بشید، بچه‌دار بشید
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/Futball180TV/101783" target="_blank">📅 16:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101781">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTBsOkQ3od8OpQnPP1ReSA57N_P4zA3cvX6E4_47rWgDICUfeLa7aJrbZNsGNP7IhEFkjc2m8YI0jyblU7GZ5ZEPEYJNP67esFSiLH80IQQoxE8xh_Lu62c7a758Bchakh0hSIhSjnsHWm9nlPtfhXKhn07a7U5gPF8p-dkmHqbMgzJP1MxvIhzXl3H6-XpB6D_qyLdKjwvKBhG9MjOILTj9d76UC9INFTLOLEXx_G9Z-xp7uXZQOVx039tgOrkVF1wx7ykvg1fu0v-T672sw-ebn9nPQZ9toxoRE87TdmSDX3YXe8s93BW-SSExcOmEJetoy7j2XXHRt4I-6C37WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avuIHVUerGqT3mSBMqqFQ2qNcGXUK0jQ9y8RZ-cE2Ml-6M3feHXBNZoN6SRInCGz8gouE5OFDMdbXrG9w-wWwx39akZszjcEWwcmkW5wC7AcwNEwsR8tDIj2G71UDUnFbPWO2wsSWnU1H-9SXlENDSFZHtHwOiJnVxAYtz7JjljRF_wpuJ1LNu4wN2S4OHP7ZKGB_Nl9-K0ifnC5fPgxg7TMiqheqrFqgEKX7TAEmeK9QcfMtbpq6RO3mujyzDWIg-BTgCm-6Jy_Ygyxohmt0hSV5wWQEovHjw-gAhrGSnY1a_tpJrCWB04ESEQ2ssMrFZtIddTqQbsWPiSImF9zow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
امروز، ۲۶ سال از جنجالی‌ترین انتقال تاریخ فوتبال می‌گذرد؛ لوئیس فیگو، کاپیتان و ستاره بارسلونا، با فعال شدن بند فسخ ۶۲ میلیون یورویی‌اش توسط فلورنتینو پرز راهی رئال مادرید شد. این انتقال رکورد جهان را شکست و بازگشت او به نیوکمپ با استقبال شدید هواداران بارسا، از جمله پرتاب سرِ خوک به سمتش، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/101781" target="_blank">📅 16:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101780">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnAkUc-nThOo_Ybm71LUIaP_S2Z8WbRq8UfLzEq_OirViGJ9XR06foOk8uc1PAzIZtH0T18fxhGusli-_ErHw9k974m70MAz8o2umKBohhGMkTlDtdrIzHcqKdh0D8ANGJmppAaZ1R2BnK39RN7qU_-9ZlQ1C_oGRz2c9u6kWHbcx5ImRwpjqvt0WyZIAU2uzem6b9OTIVpO_U0KBW2HOUf8qYpzPlPJd3ezlNLuT4pZFbmgkoaawOwd1Jo9IbaKr65LHIzS8cH2-RvmV5LMSxVpwtJAhSzob-8qQKMDhR0tqiKgjiqxpgZvSqY5J6b7mPIalsjymUzjuH3_rKizgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینتر دید کسی حواسش نیست رفت به یه تیم از دسته 5 آلمان 16 تا گل زد. دوستانه نیست این دشمنانه‌ست بیشتر.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/101780" target="_blank">📅 16:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101779">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f574b376.mp4?token=T-PHeDxvqe-N1-ysGLI6GTbSkqq3KrBJUyzlLiBOrSN_6R_l08oDEpKQZzbyzQplXyakoQV1IpjejStcsCFYb8laXZZ2ZVnC7rNwJT19t4WQAoYCnc1GOX9QxquEVwzU6P8BJis8kvd-VDRPjPAfWAmj3E1QfEkmX-vB3AZK-DSJrUOQWFW62t30__T6PPPslV4lLbDRdd-hDL18eDjuBXqrN3D0A6GnirJDTFygAodgnADkviALfYxyLG40spNXWs53JRADDb9SYf21yFZRq66Hael1iJw2qLJBVmpSRRrBcoW4HS_sAfvi-To5nZ2JN97YHl8GCvP2ByJmT8qfqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f574b376.mp4?token=T-PHeDxvqe-N1-ysGLI6GTbSkqq3KrBJUyzlLiBOrSN_6R_l08oDEpKQZzbyzQplXyakoQV1IpjejStcsCFYb8laXZZ2ZVnC7rNwJT19t4WQAoYCnc1GOX9QxquEVwzU6P8BJis8kvd-VDRPjPAfWAmj3E1QfEkmX-vB3AZK-DSJrUOQWFW62t30__T6PPPslV4lLbDRdd-hDL18eDjuBXqrN3D0A6GnirJDTFygAodgnADkviALfYxyLG40spNXWs53JRADDb9SYf21yFZRq66Hael1iJw2qLJBVmpSRRrBcoW4HS_sAfvi-To5nZ2JN97YHl8GCvP2ByJmT8qfqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
برخی از سوپرگل‌های لوئیز سوارز در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/Futball180TV/101779" target="_blank">📅 16:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101778">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=WhgJV2xcVNmNCvh6dbPDlWbwRCR7NGQiomw891BE9Hs01JUd1_XqthrGDcSXfE7SbkOoAs_G0g83DIbIuTmIHXeMLOgClZzd1KR1AEd9v8NBe7EdBuIrUPwVXHO0RhCKhFc2D04C3dJbP_L7sOE9h4z4EW9NI4IAqDzzL3ynoEgKdecfLSn5hPDdJH4Z1DgpSRs9OvkAAIRjSG-8voL785cGuH7MfR2-o-_aKOYKz6q9rhv3Ot6MVUTyunE1PoDOTLcfJAABiF2qYKTYsCQtFNLTkXvLq2FHUMMXABnDUKpyg5iuRBOsyww5ST34go0yEngBYRWEKbIU3mlyrGo5TDOD6wexGj-0mOcKbhf7U5qksx-PWkX_eZRPyQh3s5X4MNfKVaeY13HvyvTu2Rt6P_dsys3tQ5AWLP7cx5Mt0FLG8_zzxNoIaIZx91HYs2Bq-fZ_Zi5h6imYLC5732i_l1bbRAkqwIiOkDrH16fo297plfAnyikTgehRVD646SZEmcauXYawE8TzSe_rCEMpogBxFGpo3fZ04sO4wx4lqOJ7iw3Kq6wo6NhE0KsXULxNptkDHf_Pjg3x34h4ZGQRasMdhUObzeneNbbyC3oC6Jj9BaGu1zuWVZnOFxrUBxBcaYFzYIyStjJ_4FWUaNmCqw5L5j2fqVMg2_CCrTP8aik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=WhgJV2xcVNmNCvh6dbPDlWbwRCR7NGQiomw891BE9Hs01JUd1_XqthrGDcSXfE7SbkOoAs_G0g83DIbIuTmIHXeMLOgClZzd1KR1AEd9v8NBe7EdBuIrUPwVXHO0RhCKhFc2D04C3dJbP_L7sOE9h4z4EW9NI4IAqDzzL3ynoEgKdecfLSn5hPDdJH4Z1DgpSRs9OvkAAIRjSG-8voL785cGuH7MfR2-o-_aKOYKz6q9rhv3Ot6MVUTyunE1PoDOTLcfJAABiF2qYKTYsCQtFNLTkXvLq2FHUMMXABnDUKpyg5iuRBOsyww5ST34go0yEngBYRWEKbIU3mlyrGo5TDOD6wexGj-0mOcKbhf7U5qksx-PWkX_eZRPyQh3s5X4MNfKVaeY13HvyvTu2Rt6P_dsys3tQ5AWLP7cx5Mt0FLG8_zzxNoIaIZx91HYs2Bq-fZ_Zi5h6imYLC5732i_l1bbRAkqwIiOkDrH16fo297plfAnyikTgehRVD646SZEmcauXYawE8TzSe_rCEMpogBxFGpo3fZ04sO4wx4lqOJ7iw3Kq6wo6NhE0KsXULxNptkDHf_Pjg3x34h4ZGQRasMdhUObzeneNbbyC3oC6Jj9BaGu1zuWVZnOFxrUBxBcaYFzYIyStjJ_4FWUaNmCqw5L5j2fqVMg2_CCrTP8aik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چطور در لاماسیا، مسی و اینیستا می‌سازند؟  اینیستا و تشریح سازوکار خاص‌ترین آکادمی فوتبال جهان؛ استعدادیابی در سرتاسر دنیا، مطابق با استانداردهای بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/101778" target="_blank">📅 15:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101777">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">▶️
👤
به بهانه تولد 49 سالگی مهدی مهدوی‌کیا ستاره سابق پرسپولیس؛ تمام گلهایی که در در تیم ملی به ثمر رسانده را در این ویدیو می‌توانید ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101777" target="_blank">📅 15:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101776">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfurPxkr3b3GGrFzNcrw5UewEl_jYP9757ujNvUnLRV2hbQD6PnvKtS11LXsRaRyrI82sZYc-tLWOG6CrFXTdM3eSD9qfRmMD5p8Ka7OXDwbRa4vPlpYvtdRKHUTQg9TcH4krxXTEG2Nhdro54r2YL-jx3or2-hI_GzOXDArFsUXHm_ZDGP8bLZtNAxOyjBSCpgZ2uWZ8TS0hN2-i8IxpOoqKJVNuyUxrhSf3fwDGQ4I6MeMBqUDsoPyloh37i4YvknNagheTB9T1ndAk2fkEmEuJvbIpwPJxr5KLCsf0orN0Iu2VFR1ERMkCeVZ7IWqKUF2PFDVg2MFzszi2cqY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇩🇪
یورگن کلوپ:
با چیزی که خیلی مخالفم فحش به خانوادست! اگر به خانواده‌ام توهین کنید، من می‌روم. اگر روزی فکر کردید من مربی بدی هستم، مستقیم به خودم بگویید؛ همان لحظه بدون اینکه حتی غرامتی بخواهم، کنار می‌روم. من این کار را برای خودم انجام نمی‌دهم، برای شما انجام می‌دهم. با وجود اینکه دیدم با ناگلزمان و توخل چه رفتاری شد، این مسئولیت را پذیرفتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/101776" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101775">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz2sQB_9XbpS2IFCYHNB4glIn5QlaxpZCTvZd1hID2IVMohFsprEopYm8RhotiOvIYQeTe-9kDWqwtzpXRgx7cb2UwCif4imS8vSdLiKwXj3XX7I2PqYl5nnd2VNjoEzdDVh_yLD2o_LA0O0MddM45z-E9KsifxJFVvL732Z2ADvh0OEIH_AXk9UVDx_XGVP_zaT4na2FS4T4t32P3pHw-qULSlqlE9Hi5ePz7-JLwdz0Tw_XGutHeKAERDs1rjVLacWoIMRH1_uvzd7kzkqcvivj0mcI5BpIEJrBmPrUa15qqsoB6-OLx7xIHwl4oZ27AC-QjdMJc5lTUfcbmp5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
دنیله دروسی:
عشق من فوتبال و رمه! اگه بازیکن رم نبودم، حاضر بودم همیشه 10 ساعت با ماشینم سفر کنم تا برم استادیوم و تشویقشون کنم. هیچکسی هیچوقت نمیتونه رم رو بیشتر از من دوست داشته باشه.
تولدت مبارک آخرین گلادیاتور رم
🎉
🎊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/101775" target="_blank">📅 15:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101774">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfxP8gb1t-vA6Eah-xdhVtumuSv18iS7aiaj4EaxyvPFnBmj6hsOuHmcyIYdtKqDXQeSTOJ0wNwC31stTxLIeiYz2d2Hcawik5-RW4wizrYNYroWfj7IPDo4wJEIPsjJXauHVCwBlWr4LBAH_2XcNWKEp1CiYhAfD4ceaL9d9BeVHUnBDgp7fSOuh6qzgg4ezptuIS5jKPONFYrzTD0tjMgGO4blns7HZfGgaWqA3iohK1tHqhGK4m_gTLexZJZOAKA4FdDi-lBkPrVSGXhvkyrtmsSpodq_zx3viASj9npCeSaCYBAsCHCU0_FcdXN1bTvN-1VoqQ_yihMdr1ycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
قرعه کشی مرحله گروهی لیگ قهرمانان اروپا 27 مرداد ماه برگزار میشود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/101774" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101773">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clueHMXRwImuQOT7jECUiS2sSI9KyajBws4zMzuOU7di_HH-zTfgV1VsNMegsGf71CVq2lGRN95e0c9dmq7_RGCxg6RvBKImR5JpMwKW3-cSSpsnFTecwn2fR_7LlfvZi7pgTzy3gt0ZHmsMUgvtNjvx4y3Kx6vfo4niPMe9UWb_DaLIAH2zjozplrNHHrgwZZtgr-iks7fA_COGUEL2ADoutHs8msj95dakRBgL08FsXJJhMttJNAKccJQ3rmlyw3UFNTxWQ5LH4e3gpw-NH3Mnt3tMQZ4VbDasH6xUyvDV1wk1wBEVoD5ZYDB-eWlwKBTHfcQJrR4axd1uAKrqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
📊
مقایسه عملکرد نیمار‌‌ و امباپه برای پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/101773" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101772">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZk2dWg-5cR5S753TyFKFgrwh1sSjlX1UGvi63GZFkcvNy92DOoHaigoC_ay7M4_LMGH_4Nb4jKpU0nszgoJInh4OGOk0PcEEmniUuvoHWi3FLtIYzuS8XewzQTCbDw5WF84gLVvz1roGAjxzoZF9PTplVWfPB4H0H18-xZUrQb5ATPyXmrNvvAuGQSkMJt_YqokQXD0ZS_xaRhqwBZ5vnlqEUVibizDTm8Su6iGMLyhRF-ZHdKHhy6fMhxSRkixbO_j7-x7vYrr6jOSJ0zmlFXOHoXOk2T9dUHKJoPtniufH-F6YFvkYko2WWSZr3ZVQdEoE4zI18zEoQ4epvvzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/101772" target="_blank">📅 15:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101771">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVk1rew7ouBTwZkJHy2bdPCBeOd7wU4Se9eu95wc6dLuZk7lzD8Fo34DzmOrUWpArsTFBE7v5TOqy6eQVSCRUWgYVC8gUiliwecVkH7YjqEJObMlgJ6SYoNSca_yLlcptn2204WVCbbtozaUl4k4wkN2R8VznE8BFJCpjuT53_PRfLjnSqRxmNj4KItr44ikIvO9wCm4xTryzico5e7SX1KfCIBdNGC5jHS38va5o0bwqGWQhvKrgWvTH6OLMzo2OTGmvNHWQOLU5hts9SPDGjrulMriR_GM6n1VAZ20Vv8YUBcvjeOQsszlAku7612UbuZcKCd-m0LLNSAjqlJoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اندریک و خانومش و بچه‌ای که خانومش بارداره به اسم کندریک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/101771" target="_blank">📅 14:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101770">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmaI17uaAk7T7jxuNTe-cegAhxTm9iCQL2hjrebPTMGtF-ihqiopGy0D0gy4Ree05S5QPSZQUHP6eyXtAtKMP3nt_dfznwjdMGzDhIha1dCHBhls_90GZ3ycQi_KhgibUwnba1Gdnb9gj-GXL_uI7M-r_udMTGpC1boWEScFYoHQ9xRGNMNkgmFAccR660-mwYStyoulgniEMeyosGAri-KyJsyWPPHhVlii9LqTDHuNrggLCXIuYAwCML-4GDz0W_ZV5on63AKKje1Vpl-7hE6Y6LOVJjZgvkJzpuzexJ6kAyvQj8stcIl6gGHWUYj3b2BvDO91k-og19aza23iPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🔴
از زمان پیوستن به بارسلونا، فرنکی دی‌یونگ 416 روز رو به علت مصدومیت از دست داده که با این مصدومیت جدیدش احتمالا به 566 روز هم برسه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/101770" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101769">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
در چنین روزی، ۱۶ سال پیش، ماریو بالوتلی در جریان یکی از بازی‌های دوستانه پیش‌فصل منچسترسیتی این حرکت عجیب را انجام داد. روبرتو مانچینی آن‌قدر از این اتفاق عصبانی شد که بلافاصله بالوتلی را تعویض کرد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101769" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101768">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کدگذاری به سبک قلعه‌نویی؛ واکنش قائدی به حرکات عجیب قلعه‌نویی کنار زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101768" target="_blank">📅 14:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101767">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhpcgCfdosoUdpGnn2bEYJNnZk6ySyBKPZu11x_Gb19UC6KEAix9Ms8EaTfm7tiwEBjgxBpBewze_khKr_ZSZF481uhpx77ULGpghpipRn2Dac8EeokLmxbZYoMrnjbpjp0ug-_lVDuu-nJp0DILoWhfGUZkaA2v84ib7bdzNP9VRr0wzsD91rE9vYk0PR3c4KZ38EU-DZquMSX5jQ7LGZ_UGLdcXrPg8UXUvDGXVm79QWc2YNtSLDyIsoM1Qr7QJQwMIrTS6gcjfllzSWs_WGRHyon85apCPxd-RJ9JcsebrSz_agZFwu_Uv7gUwrIVvrOEGDj6wpJ5fHepB7qRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نفرات چلسی برای اردوی استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/101767" target="_blank">📅 14:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101766">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=ltonaENLPwoTnRjhq7MWU7hwv6DlqhbcKYXK8SlWEtCugMn5YOzw9bDavLr9ICJSdcKvNuGESxtqW3-iEQmZMaRFORIwB9EY8xCFBZJYPqiSvtzwZR1RZmJcuw_FbGKkG5oc-WwmcgEICgtMk8NWb2WMT2LlHMf75opI3AI7y_b0kuj6rFrrJ_OiShNR980dVBA9kOmB2LsC3IpvNI4gn7TDCtIpVE6RaPoLLMobkXAA4-Si-uC9VQyVCm3Tu06AlINbdFSS2K45jRv-VJImC7Ry4blM1bw62Heiycywq7NNdGXfedZ6nRzfamZHGHgNYEI2DhJONKC-YTmUPCxX6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=ltonaENLPwoTnRjhq7MWU7hwv6DlqhbcKYXK8SlWEtCugMn5YOzw9bDavLr9ICJSdcKvNuGESxtqW3-iEQmZMaRFORIwB9EY8xCFBZJYPqiSvtzwZR1RZmJcuw_FbGKkG5oc-WwmcgEICgtMk8NWb2WMT2LlHMf75opI3AI7y_b0kuj6rFrrJ_OiShNR980dVBA9kOmB2LsC3IpvNI4gn7TDCtIpVE6RaPoLLMobkXAA4-Si-uC9VQyVCm3Tu06AlINbdFSS2K45jRv-VJImC7Ry4blM1bw62Heiycywq7NNdGXfedZ6nRzfamZHGHgNYEI2DhJONKC-YTmUPCxX6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
مصدومیت شدید یک ورزشکار در جریان مسابقات مردان‌آهنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101766" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101765">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=sFnRmRh1xmYOvJ7JYBWAdFILhexNPVhvcQ-HxSYG8rUzKAv1eDrWV-dxYJhH-whWUYbnk0ZX1au-ALdwGZTUjJ0JjzeTYaXW0sAlAc_494Ew-96CoqMj4UmVgVT8QpRPLYbISJKAr6pb8Z1s43aX0dqAxiI3_NrqMI2-_YIiT8SKmnWDffz7ir66sOBT1Cxj8P2idWNpG-Yn4lLOoucossj0YLDH_pxJKOaXbxdi4QfmEqfL_t5nWvI68R5f2pu7TlbUWgHGADGxFCrzkLqJkjQex_kOuDG7yPoR1V6NcbVl3Gtd0iwpmXSxy-K_wYjDwxJGZU3Do8MtKGlHKJcT2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=sFnRmRh1xmYOvJ7JYBWAdFILhexNPVhvcQ-HxSYG8rUzKAv1eDrWV-dxYJhH-whWUYbnk0ZX1au-ALdwGZTUjJ0JjzeTYaXW0sAlAc_494Ew-96CoqMj4UmVgVT8QpRPLYbISJKAr6pb8Z1s43aX0dqAxiI3_NrqMI2-_YIiT8SKmnWDffz7ir66sOBT1Cxj8P2idWNpG-Yn4lLOoucossj0YLDH_pxJKOaXbxdi4QfmEqfL_t5nWvI68R5f2pu7TlbUWgHGADGxFCrzkLqJkjQex_kOuDG7yPoR1V6NcbVl3Gtd0iwpmXSxy-K_wYjDwxJGZU3Do8MtKGlHKJcT2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
افشاگری پشم‌ریزون اوجی وزیرنفت‌ دولت ابراهیم رئیسی: موساد به من زنگ زد گفت ۳+۵ چند می شود و سپس خط لوله هشتم انتقال گاز به شمال کشور را منفجر کرد!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101765" target="_blank">📅 13:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101764">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=Y3s-6xbjrIvS5F_KqhqFcf02JvvNvav4QADN4HEAOC-Z1baBwl291AyO_9oQHSKXllM7A_TS4GMU4SIj48fjGnk8gwABiiFhhBZrp9t7L5DdwpVPWyLp7os7CdGSzpLSDIFWXPXdYKKXNZH1IvehjXUET5Ij4twq8GEY0WJ61inMYKQrCvkvppltK1y15crZoq8OHQJlrtKpvSlhGdn4YpticxE_8WjZ70smBwGo1ZlBxamn4hyjfzNtPb5gBvrkl5FWD9t4bqiVNBPwvqrZCjhVSOR6AsVJMXHPTXdKHnX-kOg_b_L3B1Yr8j0sIkQ5fe3tvwXa6OCDCP3GQekXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=Y3s-6xbjrIvS5F_KqhqFcf02JvvNvav4QADN4HEAOC-Z1baBwl291AyO_9oQHSKXllM7A_TS4GMU4SIj48fjGnk8gwABiiFhhBZrp9t7L5DdwpVPWyLp7os7CdGSzpLSDIFWXPXdYKKXNZH1IvehjXUET5Ij4twq8GEY0WJ61inMYKQrCvkvppltK1y15crZoq8OHQJlrtKpvSlhGdn4YpticxE_8WjZ70smBwGo1ZlBxamn4hyjfzNtPb5gBvrkl5FWD9t4bqiVNBPwvqrZCjhVSOR6AsVJMXHPTXdKHnX-kOg_b_L3B1Yr8j0sIkQ5fe3tvwXa6OCDCP3GQekXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
پیرس مورگان، مجری معروف تلویزیونی انگلیس، بعد از باخت آرژانتین به اسپانیا تو فینال جام جهانی ۲۰۲۶، دوباره رفت سراغ انتقاد از لیونل مسی.
گفت: مسی فوراً دوید سمت داور، مثل یه بچه مدرسه‌ای که می‌خواد یکی رو لو بده، تا باعث اخراجش بشه. به نظرم این واقعاً چندش‌آور بود.
این‌همه از «سن‌لئو» حرف می‌زنن؛ همون کسی که می‌گن قراره بهترین بازیکن تاریخ فوتبال باشه. ولی توی فینال کاملاً محو شده بود؛ انقدر که اصلاً حس نکردم توی زمین حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101764" target="_blank">📅 13:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101763">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo7dPkxJHJExPnczQqFzZDSBXrlNZfvtHOB468fihtHcDVVgzb3lGDiEUaVZnq6LNPn8btUabfNCtJLc1zV5kbXpDpblqs0tr7tCUu9BxEGxuH3sar0gCET1s4rQCoVtrtvs_5pYrxnCWZL9xbMghTgk082eimqQzqb6lsnaEPC1w74PkkCeQVeLF7p4z9z_S4BHO0QBO318M9v3FR4dTOAvAzEwa1QWzgBxyYIP1975xV2RjTYdZxkCOaYc5EC2lBV-YI2jhcu1ZgmENmoS8dikFqD2IFbp-bVUFg2zy2P4SaofvbgCL6W8vt4c_JWdmhfKK9Z6V7wLpkHGAodQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101763" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101762">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632f699042.mp4?token=B5PtDtVGmiaX4EzxzWXSqU9ekpidDAy1dwLO-odKdQu3QYzRBUXn2mtD4hX33hfGQ3yLm9pHR3tfjefIiW3QKtE6eK_gqIu6rNzC0O-leIDQ91N4O__b4GQMIavaTzdM0tn1oH8pXHKdKLA59xsx4QXCri06wv6PxZPDK9WGK4NlF1sCgxqIx8QPSHmzU90_Jo9EUBoOmmj6sBXbxXF6UQ9L1sfkvNNOrzR4nX2Fs7DC0acmZtEy50uxSkdDxPDMusNdZtrGHYwFLzg0m91_qjr2f0V9DoRdhRtnBLmD-gDaUpISD5n1-6t23MIqUh7ip53KTH69hB0-aBYED128Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632f699042.mp4?token=B5PtDtVGmiaX4EzxzWXSqU9ekpidDAy1dwLO-odKdQu3QYzRBUXn2mtD4hX33hfGQ3yLm9pHR3tfjefIiW3QKtE6eK_gqIu6rNzC0O-leIDQ91N4O__b4GQMIavaTzdM0tn1oH8pXHKdKLA59xsx4QXCri06wv6PxZPDK9WGK4NlF1sCgxqIx8QPSHmzU90_Jo9EUBoOmmj6sBXbxXF6UQ9L1sfkvNNOrzR4nX2Fs7DC0acmZtEy50uxSkdDxPDMusNdZtrGHYwFLzg0m91_qjr2f0V9DoRdhRtnBLmD-gDaUpISD5n1-6t23MIqUh7ip53KTH69hB0-aBYED128Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: ارزیابیت از عملکرد مسی در جام‌جهانی؟⁣
🎙
لوئیس سوارر: با سنی که اون داره، میتونست بشینه توی خونه، اما با انگیزه تمام رفت تا دومین جام‌جهانی رو برای کشورش کسب کنه و تیم ملیش رو هم تا بالاترین سطح بالا آورد اما نشد. فکر نکنم کسی گله و انتقادی ازش داشته باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101762" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101761">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=EMPcfzSSFpOIX3BRp5D1Iuh2TfuFHS6Fhh1-p-oU2gxPvetolk66kQVydo57KxbKJYYCHV7ixJf2HuLkXcchm8J2ejcVkGDgDgXoQ_RCI6g34MaLNaVWqOpcLeFqsztVCUXIbhph38-pZ5wp7L3-g6Gxl7m3aHXBP0xSEJChR0BKPHp2IcvMq-vY_t4IhI2gJjJbWVxsAcJk4GMlnuqM4qyiLNZ2GcsTxkrLVOcszeWFhoR3mxuhh_BHRW_eYzeZxaDqgQ3xHSDAEQgngqVWhMPSjFXbw3u457shrVzdWrwXJgdT_QJAyHaBaJE4G0eN3w_Dlk3V2vI7eMFnyR70fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=EMPcfzSSFpOIX3BRp5D1Iuh2TfuFHS6Fhh1-p-oU2gxPvetolk66kQVydo57KxbKJYYCHV7ixJf2HuLkXcchm8J2ejcVkGDgDgXoQ_RCI6g34MaLNaVWqOpcLeFqsztVCUXIbhph38-pZ5wp7L3-g6Gxl7m3aHXBP0xSEJChR0BKPHp2IcvMq-vY_t4IhI2gJjJbWVxsAcJk4GMlnuqM4qyiLNZ2GcsTxkrLVOcszeWFhoR3mxuhh_BHRW_eYzeZxaDqgQ3xHSDAEQgngqVWhMPSjFXbw3u457shrVzdWrwXJgdT_QJAyHaBaJE4G0eN3w_Dlk3V2vI7eMFnyR70fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
هوگو لوریس درباره برنامه فرانسه برای مهار مسی: "یه دستور ویژه از طرف دشان به انگولو کانته داده شده بود. کانته همیشه باید سایه‌به‌سایه و تو شعاع حرکتیِ لئو مسی میموند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101761" target="_blank">📅 13:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101760">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=H6ZZUWMFhIIN3VlPquU0RVs-rz-RyUBjOGaJV-S58ISBLiW5Sc-6n7qtFKAIW_0A6f_WLVxadqSIVaoxoOY6a2ewqiOJSkRiSYwyvMB05o2J68DTcR4-Y6dMkLxGI4-XorCbVYPy8re557QfTcOcOgte-pi_o58eFvqYO0vYoxcpfJvmOhVwHTyP8xp0sG3fvdQnh3ylDNCTOkOzvCwzco_D5rCDJ6lXVz069ibYF-jYYHALkdpdpJ2bA34KO_zI-au3zO2zIILh_z2KUFXukyWN_L6kQ1JT7xxt841-Y5W0hYUk4GCeIU784ArGz5Ky96zwBqSyfcpxAzMpdpUcD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=H6ZZUWMFhIIN3VlPquU0RVs-rz-RyUBjOGaJV-S58ISBLiW5Sc-6n7qtFKAIW_0A6f_WLVxadqSIVaoxoOY6a2ewqiOJSkRiSYwyvMB05o2J68DTcR4-Y6dMkLxGI4-XorCbVYPy8re557QfTcOcOgte-pi_o58eFvqYO0vYoxcpfJvmOhVwHTyP8xp0sG3fvdQnh3ylDNCTOkOzvCwzco_D5rCDJ6lXVz069ibYF-jYYHALkdpdpJ2bA34KO_zI-au3zO2zIILh_z2KUFXukyWN_L6kQ1JT7xxt841-Y5W0hYUk4GCeIU784ArGz5Ky96zwBqSyfcpxAzMpdpUcD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وضعیت استادیوم فینال جام‌جهانی که درحال کندن چمن و بازسازی برای مسابقات فوتبال آمریکایی هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101760" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101759">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHavaanr95a53tSubLZaaEMUmhbHP_Lkuyf-KL4bOIbi0CNRlBcTsxoYDqqyJ4vbQQnV9juRKIX9vwxA4YlMF31wpzLaaEdw3Q0zB4q0okpWFzfddeGI4gwvFVYNEBf6hdQtev6dFf16fIuxzceKjXqkPmY98ORqfjJ7u3vtTdF23sQf7xnzaKVclGZILTujmVrT0SKYs-LcR4D3YpV1BVxCH3471ubIKAK7sfRN0R7M_vMVzTp98O0mpP1O2ttAZnA_Jn-mgBVCo2lExUFqQr5ErLWN9jo3DwfcI2oOVSXR3X6o7YJ8dWocUAlE_LvX7Fz3Oyi0LcsWOI6aJFf4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون فوتبال آلمان از انتصاب یورگن کلوپ به عنوان سرمربی تیم ملی با قراردادی تا سال 2030 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101759" target="_blank">📅 12:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101758">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMg_vVJY5hwsUHX2GQ5ThU_IOiB45O6h3WLg_CM8StWZsNGzT8MoQniCD8kKrFouOi2v1fU3BpfcCGxbZnFFs_TRzfn2NWEunMz8kW_CCstIl-GMPQBil2InKMJALXJmrnt4lB-i1lMWWFvPOsZGgTy5O0Spp77JGTx6_qSFyALfqN7APmWvrM8a76u7ngyvIjfezc8PS9DQOOjbIexknCu7YyNAUDnwAIa-cA6DETih5rXbXRXG8qAa7RMqmkQd6zxYeyAD0uKOVES4yPBnLusHRjAmmvQJ9nVcgeDkTZgFwO6nUAPZrCPswhC72voPmdHKdgMLtIck6wqgd6xXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101758" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101757">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513714e20.mp4?token=Abzt3iJ-NGrTj_rDnye3RKOTVT2Ym5Kvjh8bvYVS2eJeOA5wgEpS3aOG2H7Jof76EdclXaSp8a-HMfUYbX7wJhBG3ZA1eDztYwq5hNCpi6YNCBl_D3-KO8cpECVbOzjTHtAC496uajHn6L2EB_uCDOTKM_mQe5i2n8JDyogKkp1uGEiPrZqrK5fNGRJLOz8Yw0YQ3bO9SB8VyTsJtIvq9iktkeLbDsCe11E9y7b54nlT-68OBCzdE_T-iVr2WWHVGwKmbrInyeuVc289lt7n9dhus-Rb5iO7sKI8RqInWzfYW1x0YYF_ohujpa7SbGm63liDiZpAJ2Gr5zd0Bph2sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513714e20.mp4?token=Abzt3iJ-NGrTj_rDnye3RKOTVT2Ym5Kvjh8bvYVS2eJeOA5wgEpS3aOG2H7Jof76EdclXaSp8a-HMfUYbX7wJhBG3ZA1eDztYwq5hNCpi6YNCBl_D3-KO8cpECVbOzjTHtAC496uajHn6L2EB_uCDOTKM_mQe5i2n8JDyogKkp1uGEiPrZqrK5fNGRJLOz8Yw0YQ3bO9SB8VyTsJtIvq9iktkeLbDsCe11E9y7b54nlT-68OBCzdE_T-iVr2WWHVGwKmbrInyeuVc289lt7n9dhus-Rb5iO7sKI8RqInWzfYW1x0YYF_ohujpa7SbGm63liDiZpAJ2Gr5zd0Bph2sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101757" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101756">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=NJwwebh4JO8Ps82XeWLsNXT-G7a6UdyFMrqHnEGpw2NGwVMvI3ql5ZVb8l7ewufoOcBZdFo0YGon4I9laptK6I91g3h1Wa9O2GKb2uMgjZiBb1z0-GIGhZolI0P1E6bfEn-Zj1pkGjaGzbNEMSd2zruph2LHPnlmAvohQg77Vt5d2FuBbB-4lC6-gnLuLQzdJ3AToecZITxLgtRcLdC_qH6gRYYCHZipgKLCVOUsStlia1DQhgUW2KKgfXsLr1TR00jn4-ZN19S--2phG2sbPZotG0XWZRXBI7k5oBmSa6y87QbO2yDUO_keip0bx28uhp7WrIvra5p80PbLshqe9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=NJwwebh4JO8Ps82XeWLsNXT-G7a6UdyFMrqHnEGpw2NGwVMvI3ql5ZVb8l7ewufoOcBZdFo0YGon4I9laptK6I91g3h1Wa9O2GKb2uMgjZiBb1z0-GIGhZolI0P1E6bfEn-Zj1pkGjaGzbNEMSd2zruph2LHPnlmAvohQg77Vt5d2FuBbB-4lC6-gnLuLQzdJ3AToecZITxLgtRcLdC_qH6gRYYCHZipgKLCVOUsStlia1DQhgUW2KKgfXsLr1TR00jn4-ZN19S--2phG2sbPZotG0XWZRXBI7k5oBmSa6y87QbO2yDUO_keip0bx28uhp7WrIvra5p80PbLshqe9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🤯
«لی میژن»، دونده ۲۵ ساله چینی، در حالی که تنها ۸ کیلومتر تا خط پایان ماراتن دریاچه هنگ‌شویی فاصله داشت، دچار قاعدگی شد. با وجود خونریزی و شرایط دشوار، از مسابقه انصراف نداد و با اراده‌ای مثال‌زدنی به دویدن ادامه داد. او سرانجام مسابقه را در زمان ۲ ساعت و ۳۵ دقیقه به پایان رساند و موفق شد حدنصاب لازم برای حضور در رقابت‌های قهرمانی را کسب کند؛ عملکردی که تحسین گسترده کاربران فضای مجازی را به دنبال داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101756" target="_blank">📅 12:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101754">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2O9vEwDrGP7GHrc3hkkhvoau5uTr07Jykao-JgOJIz32i1mNaYOlzKDWaKnNnV7XPyaIxlm2X9iL4FtLbSWHJCcplPkUyqr2gkBcc9yWUrmV2bFr5KHX97f_e13JhdyN0u9muBQzCg1FTLRrKDE4YH2-R1spJMkVwibfFqhluQFLFtLLLIlgqZTe70FTXc6lvqmJV5LecuoNNisq00DKViultKY3JIbWSAjT2mSJ6V-DLgibyLHWmG_UaBwseku_ThPTvtqQloLUZFNqNrauuXfi62S5vGjScxYLTWbDyFuzJE6gZG58jfWfCLhZS4-NC2Tf69AB2YdQab9cKY7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101754" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101753">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=NcbUNbukg3LBsMLrUqceL0R7nIDs6-sZjmMKlYiGdEtrtAwxIih4hnb5Hp1_Iwn7MeQuGT4GtN0znVk6e2M5WHPzgLieDICVclsFOhNOa5sMFegUIf0jcYEckxo-c1FQRmlQpO390xB2RbWwmUg27BFMhGIbzEkgTQqf1yaY9OS2oEJm8sWpjrP9AHoIecwfXeTT_La6txMyAFxbumpfh-HivbV9LxnSySs7Ba4Vd_RhHpGfoSjoypD4B-vy1_iQ5zNl3CcVwI4z3S6jtglebjmcytgnDruK1x6qMVIECcB72XrEGS5wjPWUi-kVz6oVrYQDbdVKTW5KCbnkMBfoUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=NcbUNbukg3LBsMLrUqceL0R7nIDs6-sZjmMKlYiGdEtrtAwxIih4hnb5Hp1_Iwn7MeQuGT4GtN0znVk6e2M5WHPzgLieDICVclsFOhNOa5sMFegUIf0jcYEckxo-c1FQRmlQpO390xB2RbWwmUg27BFMhGIbzEkgTQqf1yaY9OS2oEJm8sWpjrP9AHoIecwfXeTT_La6txMyAFxbumpfh-HivbV9LxnSySs7Ba4Vd_RhHpGfoSjoypD4B-vy1_iQ5zNl3CcVwI4z3S6jtglebjmcytgnDruK1x6qMVIECcB72XrEGS5wjPWUi-kVz6oVrYQDbdVKTW5KCbnkMBfoUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد شدید عباس عراقچی از صداوسیما: صداوسیما مصاحبه‌های بین‌المللی من و استقبال مردم عراق را پخش نمی‌کند، اما شعار «مرگ بر سازشگر» و روایت‌های منفی را برجسته می‌کند؛ گاهی با خود می‌گویم شاید اسرائیلی‌ها در این روند نفوذ کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101753" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101752">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-65pl8uMQ7Pv2FL5cjKJ_wtj3RPGru9vba4KGN4L1KYUyYLhkS5-K8tpwpNXIBNffStJiYYrO1xcetrMxb4IREuGZ5AXVUOmCUFybuspohEPNpiEdvPZ4lvum7wKRjiy9_NhybRaP0QOY8xH0Utk5QWcsowOjlyJhxKooRnzgXv_Alh7HPaYccPvFkKaSOB-3pS0OvpkQzpdALIKX-ifghmdsLwI24mautfnZ7Ulfc81lihmvt_gXYfmYIHIcr7P2PU0H0StqniNt551d-rrpXcx7GLbOn9QPSUTPbDwssCXNPQtCAsiZuNH_hismHkjM4JTVemH70f4Q9dz3kTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
اینترمیلان تماس اولیه با نمایندگان کریستین رومرو برقرار کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/101752" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101749">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fb93Z-bbGx1HOMtozJkZvjATUBSxmCp2Co267nspnyTGYAdfqTRIAH7tYszWRCRmlVn3a4-bUu2l4Bqzvu7mFCMgKc_0wCZZmHkTlVG51y4rI225dJ5MQ5Lr0FEDcsHDiQc4wH_J9hcv6NgNvRuIgCL5aUOqKxMLvzhglMk4YG5sbY8L-dKb_T-GbfLO1qlqU-4H5BHHYTgSYSxw_wGXLuiHfG85qj8cO8pfBy1LRrgH9njFavw6gdSZicGKO1hOEb4HJxoY8GBYj-KtbRRUGbzSGficbdPp2TWP32ho695cYfB5wX89v1xIKfeWUBexlmCnN0_e0MWsMnhloNVc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHbBrssoWVhhv6D8mW2QBTXGD1IxPE6i6SteKmfB6uvw8j6RLOdqUycw53dP8o3WUJPMvqVTr2gcZpze4ASgeScfiudsLc60RC2bGggXy5jfgS8MZf_qjgIdbwatzepF1QPiSVP64jW1YqzizISiPJQ8X3A-yzpoTdWAql-bN9u8A2cqhPyEq3sfjh4A9MlusdTFehXdfYaWva2AFr9zJDeQTUFvYnQj-4wI_wuZn5QdLl2PMKspM3vvNe5Zf-a_EeD0XKwL5v6QNmzi3LXQGrOG2h_tudomOneErhzG-6G2EXYPiGxF1kYnUuS06sJlAPKw0KS3VFYb0Bh5ZKwHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcnpPsBeyiSsZ_YcUnn9ypIs3vLD5UYgIysqc7fRwIAEZWBYg0LI2AvS6hF2RcoT0a39PeB-X5PwxVYLO3bWcHI4ZNPfMnI34H0jaxQW4ZntfMWKS_NWyLwbkNmEbcKvZSOYlrtnNB5JhYan2OdfEYSct8QhKba29xifUCsvuV-FP4Uie3d4FIbuuiTW6aTklk9IWhkxhCUYtGJHklOonL8uNeYP0MKZu-Z8NUFpudtXWSg2RMi4Nr1tnB3W8Q3wfoTmkaMBqNaY4Z-kSOvwayS59-52wEJEB6pWsgk-hWQ-BtHb5SSPxKRdCYwdTMZmHos5mEYNw0eHDLjA4kbMQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚫️
کیت‌دوم فصل‌آینده باشگاه نیوکاسل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101749" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101748">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXHraIypG60UJV2mma5PX3YfTxmv1Yzl5dPsMkekACW9KM7qa5xymIuaNX5Q0zVQVzY9RFNZKjyC59hKj9wK0to_QNGDoN6g3ubqKLPxi7-BPI0jc5cWDRkNDiyXOxdhrSqDXq8lvw0QxxpEu9nTyndlvBJAE1Hou8zyCzveX5BTm_iA4i1D0993mmd5031qQ7276IGuP4SRC8LFzjM_cjxXGqWm6rcknqU3NWT0ep2ef1kdfJ8xAbtB3DsTVTq4DTQMapwR_OPL8va5VeE_lkmmnFCm7DEpVKYnHuofMAyvl9Psx-uHg6tQKeNg2KJoNeT5i1fvxr9w1m96cINNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
لاگاتزتا: فنرباغچه ترکیه با ارائه پیشنهادی به ارزش ۴۰ میلیون یورو بدنبال جذب رافائل‌لیائو ستاره میلان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101748" target="_blank">📅 11:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101744">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tza--ZDT7lsGycKmWj76pHW-r6zVrBT-yUri5yHWzmAkd5rOr6LC0-Amu6VQjXdS5MloYRJI4pCe61fhfWrpaZjTp5HJWnCfFINqDaImJgdwEoswGl69zx2pQdqsmDKteZN9eO6B6b6COkLBZ1Bvf-1M325biuTkPCG6dpoJJ2ledfx28bhiDfykeKXSs-HPSDMu7zLRaRG2jcT0ZRHUl1SNHbOXMuLZpFxXEzqj9RldzGkVzkldOHQN56VIzVuFXSW-7FCBPv1tnWazcFM8OPbT8jEJ1JqIePfvLTC9VV-h5FskZP0R4Gf5bd3SAlBdz4_IQO7WaIoURNcQ2Jn-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9pUUYzLjbmvmi1lROAuExOMgaGZQh2AY92G_wIS05QIyuM9GoqWI-iOfS5-kKn9zXDVmkmYGFKnwxq1XchGB_89s2YczGuA4roRLy7r5bcXrXLQ3LJbf5ATw8Xc7iERjdboKnzF7n3q3LIQgAVb-GbMZnfzvBCsdbNO04-_WNDewAmj4fGaYcMtAoeyNQCjBDc8McLtIaWWbBXy6fKyQZA_1C_I0vsg5aSqugygYr0VlXKFEFf7TdT8dG1od8uSQR6ibxUoJ2BUHvddt901CAslI0o60K7fZmbMNSOYiMjWJDQoFfQ2jXPAIInBVTIdSv4s0DDZKOo1C6BegSkaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfJKT4oWPWDhcGNh_HSkfM4bp7k-26v2gvjP87CB5RXgPKXOBaKYvY05PfZOwmWFon58lx-qOU1h0JTeAR-WwHl4t588iTd3lGStWqjSg-vyNwsl9382l0eY-edZF_5I2mzC-DEF8c3fumY6PKf8DBzfb1P9Xipd4RWtExzMNH4LQAjvhsH0Xdu4LiUFZ0xAwR62RAZVHu8HJNfbYgO5C60KBSTayecgL0st5vXF2vXVJdMfMS9rHKvxnFR3MnJB0m-krEBD4JctfeX1W6KbrUOOjy088BcVXq27bOznyTy6YPf6fcBzd15H-EWFoSKhY6U_eXG_uafaXMd4N3Bd_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم فصل‌آینده باشگاه آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101744" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101743">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=LGHGtPCj9CRtKjtTTFYZKKSMxiZlAbuqGxZoL73u6dl8aGvbeptl073LEuf6YvNwsnNQzVVkeIPfDIfhMQ9c2ddGRvLnwLsGA-lcSUqgcljwQ08XaJJPCBFIe54-FgVBVZt0F5ya_tfMHBDoeuDP_bjiZX_8TyhIHxH-UUA9kiVafoUQUJkOpWnLunhmUzKH1FBcdpxF8ZiPKeiDfHdYhUwkxIaZOGfOo-ONFcVLlE_TX-0rN3HysXJL5h9AmN4ht74m5qtQ12dS8z2g0Bp8oUXMGuzn097Ir26Tc-e_VGTgfwxZ3HfKayFjs1t84k_my0pa4EOX9SIgQVMf4-vR3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=LGHGtPCj9CRtKjtTTFYZKKSMxiZlAbuqGxZoL73u6dl8aGvbeptl073LEuf6YvNwsnNQzVVkeIPfDIfhMQ9c2ddGRvLnwLsGA-lcSUqgcljwQ08XaJJPCBFIe54-FgVBVZt0F5ya_tfMHBDoeuDP_bjiZX_8TyhIHxH-UUA9kiVafoUQUJkOpWnLunhmUzKH1FBcdpxF8ZiPKeiDfHdYhUwkxIaZOGfOo-ONFcVLlE_TX-0rN3HysXJL5h9AmN4ht74m5qtQ12dS8z2g0Bp8oUXMGuzn097Ir26Tc-e_VGTgfwxZ3HfKayFjs1t84k_my0pa4EOX9SIgQVMf4-vR3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کاپیتانِ اسپانیا در رویای پیوستن به رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101743" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101742">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=bIBiLS5Qdt8e3Pzb_h1REWM5oRBfULqfb3nRiDMJ9I--ngPEhCcCndh-hQZS2ikfriNvcHg49TqTmvIos4oID_nl3OJiVS29FT4korWoX3qDgJWpf-0Vp-JT1tjITIRtKnWmk5Ybus4k5y15PzJeRzyOKftneBE2_MwSqph7On2XGydWW30UoGPxdMpRrEpCCViALtREw3BGs4GcTjgf9bDsRrqTweovzcGa2EUEBA3l-pDPr9XFDljIWpfFI5dORJS4i05C4eGnvqsw6LaLUx1uBupICVt718uUSHfSJ_De9uYgFgGXWbpJOvXmU4ZpxeHFX5hIbzWHgpOHuY9mnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=bIBiLS5Qdt8e3Pzb_h1REWM5oRBfULqfb3nRiDMJ9I--ngPEhCcCndh-hQZS2ikfriNvcHg49TqTmvIos4oID_nl3OJiVS29FT4korWoX3qDgJWpf-0Vp-JT1tjITIRtKnWmk5Ybus4k5y15PzJeRzyOKftneBE2_MwSqph7On2XGydWW30UoGPxdMpRrEpCCViALtREw3BGs4GcTjgf9bDsRrqTweovzcGa2EUEBA3l-pDPr9XFDljIWpfFI5dORJS4i05C4eGnvqsw6LaLUx1uBupICVt718uUSHfSJ_De9uYgFgGXWbpJOvXmU4ZpxeHFX5hIbzWHgpOHuY9mnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⭐️
🇪🇸
زوج طلایی اینیستا و لیونل‌مسی که از بهترین ترکیب‌های تاریخ فوتبال یاد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101742" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101734">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mh9hyEzZoK6DkU7uHnmPqwZzzAJso8ujWYOCkchSzmfB69heDk3IHzZyglZJGC7iAR3e7TLlWUmTKREou48wqWqhT5QNkBr1-faMi6OtVaThMhRwez-hS4gOvckSQJ-imzFzfaCJGCwZlHR83U7Ku8FFmJvf4Uk2AtK2fyzkH0FzbBXWmQ27E2mwzPVImbFr7VxJxQP7Y-dWyirO1cuLuZa6BWkZbgJu1QBLg9y4113OQQMckKu7KVtv6UtvRozc2z2I92oP0ol0J64CQv5QwGXQo0nEyDJzBNqBgjfqpd5icg-M8O08cKAvLGAoIucaMh3VY7xXtWHxSHQLCDSeuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ho8GSJojYmHbaxpDqdpujhSn960MEKzhlXkP8MGApwFpaJj6rHY5U_JsXevMzHO9YRGGI_8o-1qVJ7iEquHxWEVKF0vtQK9CkL-37jvtDphnIDdwqaeE1nHj1nL1yAJO61R9RfJKpBA9Ou_STFqyTH_D0897IDDENxRVCuJwiflwyOJjybjwZYaq0xkihOIYomtNLnCMtCnfuf0iE_kOevfG_XO7vvgHxATn4u0e6OWuV_bZqxtCOJH1aAVoOHc-brPVvrp5UhQ_glt9lETzBtEQp7uUccpj6qG5LfGRg2aj6zon4U_JU-EcT3rx1ph76jo5eT5jmjZ0gRRyOmF34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-lNsM-Adkjw7M_a2P90yrWe8aAa5GFPPW7NP3kn-bN4eiYDGj0RRArpZy_WCHOXTmNWrLH5qXDO7x9EWxbvQC_w7enDvXquxuKeh0t9-wWRSKm1FqRdVVDlS-Z8C6sH3hUyA-irrFadfdoOqlUSpn-OWRL83FqxNyyZ3pRVnt_9aOfosw6ktJTm3yUuSc5HBl-1rNySaGf7UKNMdRvNRUFANhtG6Wjt7KXcDJRBcE0OeMZ6Ig2DFwqnm9O7r-uIXzlVpqCTKlv3xAa6eUSsKL0QuGFFzNYqo6LeoCGos0P3KKE-c9z1-c14YBf_E8XI9S42hiFdBg_ZtaISf30H8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJffoNMyL9gwqHSZRp-5EfYkv7Ci4geB_4ser8aXrsJk2MGWY88zcad_9eWx3QtZTu4gb3IRN0jJNW8fSIBi6Zd-l2oGEBRSU-JmEab2H2oEVzLe_WTMRxcbF5B_RPw_dImuK2N4wi9cNRI1j8-MKz_zxOjaqp_mWW_E89Xc6rERWEDby59MW4vDZO0FmMi9yRhz2OEOqwWeG-_NuE0CM7-sLGJ08NxstlEPoqx4yjRU69gaUTk-O2Pg0iSrpnxzZEpJAyLN_zVzq37gFFnmUOaiMgNbozuO4GczIyyV-kGhvLOHMVBrI0hjswnfIHg7JDhi0dlovsgwsyBoh5rqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbiCkPrT29di3jZuclRDvyiwRA0_9CHenN3InJ6uaJAQepUdm_96fxuy-bsag5mdcG5Pc15UpmnZtxmgyAegrJv9PbO3K3gpB1UUnKs6OeoM5DDfmI5CYV1HdNvgZwxsruTHvdMYnsYSz80RAhK7tR58X0jlhcKDNNnPMYFwrbYmxvxtcN4dnklRGvbNmZZXtP9VlX-Mu1f6LFzOI6wc278OwODaTm7DIC7jK6Lu7Jhjacu6dQNp2HFQO4py4azppnqei9uiU_MqOesbpLiNPlIeFUGgM4ySFbKU4jumDHZIStWARaEix7xoFb1W9Z6TlgbYf-Aa62lPt72v5pa7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NeTqv4FXr31EsCdi8KcfP_MOaBhZe51Rftq9GLaUD2kdDBpwzV-35YL_DQxlGOWxpmOTrrS0GZ-zhmGDcAhPeify79h9sfllU9okoG7i4iJDhKY0fZ6jDriv9klxxtvQiJYh35k1NrdvzzXAQdZH7gIoPGyJUEZJ_VQrKE2XgV2Kgk2Awo4DMdtGuXF8A7bl1cMrVyrHpLXQxl43vFQX02fkdCMf5P7CZ2eV2afuI9b0PFbpbu9hB0RuzKlQ9_gHPeEopCvsO2RpeK3QMVVmaGZNzv8IKHQKBd23JcmU-Ti3KIiIk00VRDBW_JJIPJWRF5jt2QLJxIGaX0M6hczN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppM2Lnhl3CEtjq8VdrmBzYXigAeCEDzfM7cGakzXO9lX4q92aVE63LPiVs5QclSrkVnqR6NBkwWDIZ6vW58bxEMYasODJ8_NLR9EdJJofDW_2genE13KM7OQdleou8d6k36G5U_SDoxk_IT6olFDU5GOscAUvaKxOYjx2YK61H0MWtUW5pLcDiphoO1AfZw0LHvprzfM1aIot8vyrLcOZBW5r6S_FqD8tJ6yJ0YZPMMga__1YRwl58MgIx0PPqGJeGV-qIJ43qzTZVF0aNhmwP4B3qz1Z1Zu6DZ82-cEli2I9CYjbbCbJSUeReUDB1B7fkL9eaMLs0XU9d9mtFF2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLXiaX1BU7BxXFeqPwbs-Eankxn4fcER_1ASlQOvLZw5Y4j6KvgW81dtuPpM1Fk89tC69Kzesn2LnfMEm3psmsSm87fFURy5YE1Kv3h0hrgHU6rqeL9v71Kf86l6tQto7Zf3KyQRhOkfW_edD0PmgI-ObDm9UGYYKc7htVZGLLeNx5f9YPe7QI_neSo5ZPjSVxIjVMIsuKeV39w_iMHCAycXgd1pc29MZ1SiqYWzMid_e0yXSF0-9lZbdTEwU_pGcniUlAu4ONdGZxQOuYThNtrsndD_RlSBmAnFK7oxnz81c6Z37kkffQQ39ZqneY8z_KZhuXriVKVOu8AW4BujmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
کیت دوم فصل ۲۰۲۶/۲۷ بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101734" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101733">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=UBJ8fhsz7CJkwnzThRUSlRiiZxw1OYVz4o6otyvjpoSz5oeT9NnCO172lU4zQEqicK14YQkz5l-2HZj_0Ll7DvabGN6cLb1XlkYGmP4QzVDIe2Ou9F3iDibFhT4_udeITJ6rTLjrMlpptOCCpBrQuRfSPl2BL7UD2DdFVrNhV-plDhxm8ljDtGJEGjvpVU2uMkSVePgxAxgU1PhQgV-NsH8SsosM9yhGwVBlCxcN01X_Pn3-rHrPqJs8td2BexjoiyoR8wAOZWyP78otxLf-G4KQYzwI077Pj2vu8jdVFQUQ_APu8D-s0J5rYf8QabhltQNZbYr6UllWa9XzVtrt4htaHbCsq71cHLCn4qUezDbKHa8GOrlXqtXDXX60NeBtCr5XR-KlXEAJku7z176LyBdVOsQtesdyLGT-N2-Jn_gla7xrHkEE6fOOksP50I_L58N9FjCEh_Ak1tedgBNgWoSaX0iaoilch1bZHYwaxGI8y-PAB5ReWJZ-uNhixPPtoOVp-ElYCdWvzR3mqt_arwkgbPFUh9z3XmwbP0WDmcLncHSr3_wrKD_ZwPfrdLDZXmVvVR_8CBPEtWyjD2S2BhWWy3Qioa3xVYaG77XC8QlWgfvDA6cwJEDie9_gEvaU82eqe3nQYhdkjfZffhxXY1FCuuR0vsgEafmubLb-SQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=UBJ8fhsz7CJkwnzThRUSlRiiZxw1OYVz4o6otyvjpoSz5oeT9NnCO172lU4zQEqicK14YQkz5l-2HZj_0Ll7DvabGN6cLb1XlkYGmP4QzVDIe2Ou9F3iDibFhT4_udeITJ6rTLjrMlpptOCCpBrQuRfSPl2BL7UD2DdFVrNhV-plDhxm8ljDtGJEGjvpVU2uMkSVePgxAxgU1PhQgV-NsH8SsosM9yhGwVBlCxcN01X_Pn3-rHrPqJs8td2BexjoiyoR8wAOZWyP78otxLf-G4KQYzwI077Pj2vu8jdVFQUQ_APu8D-s0J5rYf8QabhltQNZbYr6UllWa9XzVtrt4htaHbCsq71cHLCn4qUezDbKHa8GOrlXqtXDXX60NeBtCr5XR-KlXEAJku7z176LyBdVOsQtesdyLGT-N2-Jn_gla7xrHkEE6fOOksP50I_L58N9FjCEh_Ak1tedgBNgWoSaX0iaoilch1bZHYwaxGI8y-PAB5ReWJZ-uNhixPPtoOVp-ElYCdWvzR3mqt_arwkgbPFUh9z3XmwbP0WDmcLncHSr3_wrKD_ZwPfrdLDZXmVvVR_8CBPEtWyjD2S2BhWWy3Qioa3xVYaG77XC8QlWgfvDA6cwJEDie9_gEvaU82eqe3nQYhdkjfZffhxXY1FCuuR0vsgEafmubLb-SQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
تمامی‌گل‌های کیلیان امباپه در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101733" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101732">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=ZRSOaYJouaDTPujeqYkxNDEd4q5MWZ2NtiFzvFUC_yXYE7nnBUeFiW09atLbICn59kCzszC8DoH0yk_2mjRMuDidhfHpqvwCdIyfLEOWmMQe3gJjfUi3r5VatrE9nCgUcuvYxukoUtDXfEC6hSk3NtqN3bmbZryUUpzyI-qYLyg92POljHi6WybXrAnq6mqUzyHxRUwhEJMyN2cT7xx6_gwlsypHkv7SAQVDcipgiT500u7IOrwbLmVWNHBYmYTtkB5l0sD667BcF1mbLSfFWaTd1Sv8EKLfQJusxbRAfX7eOrX3mPkyGu1P9GHyhqTipIelIC3OhbTSjeS2mYh16w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=ZRSOaYJouaDTPujeqYkxNDEd4q5MWZ2NtiFzvFUC_yXYE7nnBUeFiW09atLbICn59kCzszC8DoH0yk_2mjRMuDidhfHpqvwCdIyfLEOWmMQe3gJjfUi3r5VatrE9nCgUcuvYxukoUtDXfEC6hSk3NtqN3bmbZryUUpzyI-qYLyg92POljHi6WybXrAnq6mqUzyHxRUwhEJMyN2cT7xx6_gwlsypHkv7SAQVDcipgiT500u7IOrwbLmVWNHBYmYTtkB5l0sD667BcF1mbLSfFWaTd1Sv8EKLfQJusxbRAfX7eOrX3mPkyGu1P9GHyhqTipIelIC3OhbTSjeS2mYh16w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
تفسیر نام اتحاد کلبا توسط مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101732" target="_blank">📅 10:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101731">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=BSGqqbnJJALEMig8Vystga0I4Z9nYv3v-JRWXlp3gMT0kajGjczoY5L2Wifa5usrlTF7a7VGMeN1ErEmLVP605eKsw1UxfCnqH5LrUQBwuCvC82ZViqpK6fAWYXfVsIw1EtyTxnb2x7kFeQdxQ4-YFe9MIs-RBoagxeX0WXw3EW9nm2FUfZIdpVJOZOJqyof30f77grOtCsUbiM5z-S1B95eFSzVjBWW-pdoSKmueGhQvroO7dDOIkS9oJtSLmWU4mqYS1LpnCvXS1MmWpyyyBGCxDdSFs1FmTYssQTEldtstfEwOaSMN4IZnqTq2Gyhum3php3GLA8El4jHsl4sig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=BSGqqbnJJALEMig8Vystga0I4Z9nYv3v-JRWXlp3gMT0kajGjczoY5L2Wifa5usrlTF7a7VGMeN1ErEmLVP605eKsw1UxfCnqH5LrUQBwuCvC82ZViqpK6fAWYXfVsIw1EtyTxnb2x7kFeQdxQ4-YFe9MIs-RBoagxeX0WXw3EW9nm2FUfZIdpVJOZOJqyof30f77grOtCsUbiM5z-S1B95eFSzVjBWW-pdoSKmueGhQvroO7dDOIkS9oJtSLmWU4mqYS1LpnCvXS1MmWpyyyBGCxDdSFs1FmTYssQTEldtstfEwOaSMN4IZnqTq2Gyhum3php3GLA8El4jHsl4sig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇦🇷
صحبت‌های یک‌آخوند حکومتی درباره عدم‌قهرمانی آرژانتین در جام‌جهانی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101731" target="_blank">📅 10:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101729">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVLB0A-7iN7cJ5t9fk3J1upgtKPa4UGautWn0tW6wTLNH5LrJ1oJipDtSxz8TPMihACAcOS3V9OLtlIGygIP7EKqBhRT_jjNRKBELvAuvwcQC_HbZz49rFXcoUAOce7kCo1BR2TXPlGncR1AgszwiV96vfGrGOh583ywgbuCR_me813Vx3b6tB4Jf0F7Xtsdny6jmKbuGxKDFpHFIdefUR3WKT3F_aubZSclsCz8VEKUVLvwadqZ9oU7oFEHzqNxuo9ZcJng6Y9eaLwcQ9iO4hABMIkdBvh30eWN4CmTaffU3RA6hy7J5wJ0V8YPm6ShTkvWFiM7ZSuGOCmgtnvnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJ-LcgsrtdIeX5z2Ak_3ej2xCIoaCbSTIHo02IcQ166z_f7omyqYLrSl37Dc5hIYpoOma-UEkjT0NdCFa87WBytS3ILLxZ6Y_NGeBoBQTWWEDGlkllgh2iHGXtWGA2SbtD-G_-jrSy_lyYIwer719FaPfnN3UqLIhZw3OcHcave4uSLbwTbFOo-k_42gHJQyXKjkt__dSpbTl3IshOU4uWKNCzgvoFge_oQdyu2LRzCfv9d91ST5SoiY6KVmgN1sqztXUgV4U6YHsKkECr0io5OoZHjvzSwNG1PzSblSSPWmSIQTHnu5DArBxk_Qsl5ViqTsB4BzRxNVRztHhC32gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفته میشه لامین یامال، دو هفته پیش به دوست دخترش یک خودروی مرسدس کابریو به ارزش ۹۰۰,۰۰۰ دلار هدیه داده
‼️
این دو نفر در حین خرید خودرو با هم دیده شدند و عجیبه که این هدیه در ابتدای رابطه اونا داده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101729" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101728">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AseL3zOXeTwKF2jw8NUeyaP5qU_W0gDaEj_LuA19q-aHOZIMh7-SGXtM1JQQpOu-bMArM-QR3W2PDmEDtMB65-_g0LEuydNA4sGveoUL35ugENS-7ICrcAAipXv0_0f0YYEY_Md_jPsdXVxuMKbrRrIUVjti9m2VAVgAkIqr59bkJo8ErqsIMRlFq48_w0T4YMO1tw3D5Cv7d_AJo3YkT2ceMvKhRnyijjMle7RSXz-VyDOzAVJ04A_-oa5HAddQq96G4Imv3W-1AWTS-lujTlvf7j9x-LbdRDNMbfSJmU4rgub1KVBcwMnGhwrikBPdkqjp7GVj4tXwVqFQ14-hNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇦🇷
پاردس: آخرین بازی ملی لیونل‌مسی مقابل اسپانیا بود و این بازیکن قصدی برای ادامه دادن نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101728" target="_blank">📅 09:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101727">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaNyUT6KacQ5AZ0wtkXNH0aGjfxBC6VoQIbaIbiq93njPFUEE1QmoauzSMkvcQ2uczifxNWJSbO_tiqlGbn9PH2A4BWwEYqZHxISdZ9zbhd-lxXaW06yoYQTjgZ5wOPSm83retddl2zKd9fwdH8tKnsNY0aDs19YBaYNs8SE8tw5l-Bcc26lEH2tAdjZWa18q-bT7HWcZvU99DR9VCBQiefv3eMzTvdHbLGdctmz4OHSUJeuGQnn7sfBdweTsRxs0IBWSd2IdNpeM5eU7Urv28exT0hniadmY9kvtDb3yu5vZ8SsCYUmzdjt-qLX8pbgqbx_OOjZXlOmUk6v4engng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔻
الکس فرگوسن: "آیا منچسترسیتی از منچستریونایتد پیشی خواهد گرفت؟ در طول عمر من، این اتفاق هرگز نخواهد افتاد."
🔵
🔺
منچسترسیتی از زمان بازنشستگی او در سال 2013، در هر فصل، جایگاه بهتری نسبت به منچستریونایتد کسب کرده است
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101727" target="_blank">📅 09:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm-7OPy82mHXBnRM7ytwtn0-hMnSxp5PJpNgPKPTz5dZJxfo3_TByYqE5rc1t8Qf6XxRLvCUQGwK1dvhlLkcWEnnsEXrnyuCki1qwLPa81NhbN9PyqMQlo9N2um46yAwjG29ejpQyVHx9hrVxBgO-qMQDc1KHFUDmqtIYSRPNGURaq5NxcJiVCDTqixxZqs6QD-pDgFLSBpOZPdk5zhoJMwOL5chVE2cECNyqDkJU3pDpgzDJGpNu0rCfoOPk3G_rCzM8kfKI2unEFQLyWp_S4rJ-ghmSvg871d5nKeGthLRUFaksks1Jjap8T2NmTwan7A5iSp56WR2BHvAu4rsaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
✅
تمامی ورزشگاه‌های میزبان یورو ۲۰۲۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101726" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2N6XwQfkQsVlkzqvG2tODM20KqNMmLTZTEW1mbd9w_cWVT25PGxMKqba4JpcyJVg28sAE-FAs5rPKvIP4TpAbQYUnNXVIv9tXsTp3d3_VVqJXTEECIyg7ZwOL0i5mzVUcZ9xgfXsLbxkyv8JiaPlbXb2gMaDmB7KwpvwDq8ZyrpCXSdCYMTT9GWS1ku1lX2mK3M7Ay1jOPAVdfNH3B41zKv9dAnQUCa6RvNb4M5TTBo3DuMUecEkmqD7cfJXgxHEgeYka7jWoAf2rwMjaLk53dVGAP-TISfUc3uCCwG-YC5vK99pMwfVjwDWSmS4ZMDIuq4ocD6_P2UfSK1j2vLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
کیپ ورد در بازی مرحله گروهی خودش مقابل اسپانیا، 0.28 موقعیت گلزنی (xG) ثبت کرد.
‼️
جالبه بدونید، فرانسه و آرژانتین هم در مرحله نیمه‌نهایی و فینال مقابل اسپانیا به صورت میانگین (Xg) 0.28 رو ثبت کردند.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101725" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101724">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0E6RL5P0ptPiaWQJHKFLDhzf1IYIAg0HyoTJoI8UNrn1ySLCHt9plPGy_sfvuGGH6Yu3HrE7ukih4fpYzRcibU3mZOkl3utx6SRtwnhOnsjXeP1Bp4AXGTZFDuVxp8g29MFODyh4cwvf7gum8INNzPk023c6vS6PWiEnUwHOiwLESAYzYKNluHncTssWWYM8_To493gGGBW0vUx_TsLg4nBZtUbduaXwwzdbin3GcYXNUsIGn_-nqAucebyCJctjx36NtLhnXoaylc1FR0jZJV3b4EqCHvlsGn2VsndzlH5DfkcA0g8yA_fLGiEKYRj03S0k1tAd8kiTMxJotUFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇫🇷
آلمان و فرانسه میخوان درخواست میزبانی مشترک جام جهانی ۲۰۳۸ رو ارائه کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101724" target="_blank">📅 08:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWj6uPG3f6sqnNf3grKujKyJBHg2ZPboiHHO73ZLZtAmlYn6czm7Tw4jLt89q6tNVP08t6ezMs11Wc_Vq5L-e6-v1skorffTwsDYXGTNzhgmRZrK-efKlFpIFFAxF9Gn_crkVuYoZAg97N5EccUgTRHZ1VHwbWhvfT1A96BIACFbvHgbVZWcP0IPMpn5aMfVWS1aDjuvA6KVGoNbdLSvnpa1oib1jDU4jiDhK_ZYtXBANrWq1F0vDdlhaSssNEVfcNi0eArNjRtKIrNGt9QaLzQi7II2j5_lAaXvcu9jWsJIFAQ4qX_8GNV5-cs8MN9GwirwC_cx-6L7b3eA6WecRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#
فکت
؛
پشماتون بریزه که بیشترین مبلغی که آرسنال از فروش یک بازیکن تو تاریخش درآمدزایی کرده 35 میلیون یورو بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101723" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101722">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=G670JvZ3uRGyAuYDTsL7MKF_DirUFN0r6vzA_9yQofHCtf12DrDEdr047odLMx0vfblQPPDVTPLOONUtrOOyYoZVbhRcksyRQCOyaE0RDS9CzzgeZgHsx2X6Blvm1JF5TEvaut-qHGDMd5xCxqmf84Hx79wOlmqxe5fKH8NLHxicrH6bQXUVm1C0bdGggjAR4fh1UeT2EfVmWMhp-memRcoKIcX2yimfdhlDULFaGjloQ4MteYcwu7MeoOMolqzWQMk0ymfT86oT9O1L8dYFvxoCR9iBuMIjFAOUBbPe13-nX-ItZyP-zquuRQgE5kXeoPQ8_3Vn-TQVKMJzx1TByw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=G670JvZ3uRGyAuYDTsL7MKF_DirUFN0r6vzA_9yQofHCtf12DrDEdr047odLMx0vfblQPPDVTPLOONUtrOOyYoZVbhRcksyRQCOyaE0RDS9CzzgeZgHsx2X6Blvm1JF5TEvaut-qHGDMd5xCxqmf84Hx79wOlmqxe5fKH8NLHxicrH6bQXUVm1C0bdGggjAR4fh1UeT2EfVmWMhp-memRcoKIcX2yimfdhlDULFaGjloQ4MteYcwu7MeoOMolqzWQMk0ymfT86oT9O1L8dYFvxoCR9iBuMIjFAOUBbPe13-nX-ItZyP-zquuRQgE5kXeoPQ8_3Vn-TQVKMJzx1TByw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اهواز از این زاویه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101722" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101721">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=mcbgrc1LwUGdSqJijbLiGyNQM_8LWqetiDfvx1Y7eLMsPvYbw5gXcD8NXh5OFLyew3KI4Fp3wu4FehCpWekCqgJSXqCAK_P8hskcQzReQx9ZmJKOKfEZltSv9bCtErbmS-OEUgmWEbypTQ7wYmjyU9DlvVuNR-U58ov59JV4ayC8mjU33I7dp46d5FxvOMQ6ce0h-AE4qHaur8VBNENQ6pJvtwHP8u3jhdR7dLnqIx7sKiyBQjJO3Nne1y1HpMNZwMSxdP44wFVEVDLhE5_48okIvj64nwDehstDBbFppKxFwfYTVSjT34UU6ceAkz3hBYIle-58qqsaH9rLtBVtrK_0JbRfOJ8DQI2Su7CW3Va34HADw4XvXyjvSflBUJLfFrmZwDhdi2CoADUT9Wn9eY4UW9LfC0orFynQzPjdSD2ISRJ_iF6ovRrdz4yS_5nWJQdjufAbhe3jBT6uNqmB0eHQxigq2nqOoWJkwqKcQLkJQKuuSKx9bfgfXFFwCEvh2Rop7NDgMCxC3AUTuIOwXLIEoHkqSM_AjQ6HXMKzYdRxO_p9q0fwsL3M0uO_g2q8UGREQoK4KkGuFuUpiwRML7psQhKOQ5yHHky1EAPQKX4lUimR3Dmphxbk9MA4iPr4fVkaXg-yZ_w5UrJ9RB7IHbe7zwnwynF-tv-OiiyQMY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=mcbgrc1LwUGdSqJijbLiGyNQM_8LWqetiDfvx1Y7eLMsPvYbw5gXcD8NXh5OFLyew3KI4Fp3wu4FehCpWekCqgJSXqCAK_P8hskcQzReQx9ZmJKOKfEZltSv9bCtErbmS-OEUgmWEbypTQ7wYmjyU9DlvVuNR-U58ov59JV4ayC8mjU33I7dp46d5FxvOMQ6ce0h-AE4qHaur8VBNENQ6pJvtwHP8u3jhdR7dLnqIx7sKiyBQjJO3Nne1y1HpMNZwMSxdP44wFVEVDLhE5_48okIvj64nwDehstDBbFppKxFwfYTVSjT34UU6ceAkz3hBYIle-58qqsaH9rLtBVtrK_0JbRfOJ8DQI2Su7CW3Va34HADw4XvXyjvSflBUJLfFrmZwDhdi2CoADUT9Wn9eY4UW9LfC0orFynQzPjdSD2ISRJ_iF6ovRrdz4yS_5nWJQdjufAbhe3jBT6uNqmB0eHQxigq2nqOoWJkwqKcQLkJQKuuSKx9bfgfXFFwCEvh2Rop7NDgMCxC3AUTuIOwXLIEoHkqSM_AjQ6HXMKzYdRxO_p9q0fwsL3M0uO_g2q8UGREQoK4KkGuFuUpiwRML7psQhKOQ5yHHky1EAPQKX4lUimR3Dmphxbk9MA4iPr4fVkaXg-yZ_w5UrJ9RB7IHbe7zwnwynF-tv-OiiyQMY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو جدید از حملات سنگین به اهواز
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101721" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101720">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=rx7VKZvnf7-khc9cv5zPAG1mkNWACLUTwBg4XX7nxnZB9KwzW6X0cyDh0HVO2EUN1eHcAVMNdf4rSAMAj4zuu9KVAC_Ucv4fIlCUoKmzaP6ZszkzK9LwzV2im3oUPOL2IrSCAiIZCmUhCwZl5AYL_umQGTl9PAtq-y5-7lzvZ3fG8BTB0i3FmFOUbIl4Gn1qfIv-ILuSr5jWDRqxgAzuzo8yh17_2gCYSv_H4Q82UKvgqDJ3Uv_Z0PSJP5h9ftRI4HgyHGuHdllvJxNt_x__zW8mU1Cc0uaO9lGAGmwJIxnD2E7GO5v6RPPQ5naRhRjOfcBlGtGwT4G8sUyhXc1idQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=rx7VKZvnf7-khc9cv5zPAG1mkNWACLUTwBg4XX7nxnZB9KwzW6X0cyDh0HVO2EUN1eHcAVMNdf4rSAMAj4zuu9KVAC_Ucv4fIlCUoKmzaP6ZszkzK9LwzV2im3oUPOL2IrSCAiIZCmUhCwZl5AYL_umQGTl9PAtq-y5-7lzvZ3fG8BTB0i3FmFOUbIl4Gn1qfIv-ILuSr5jWDRqxgAzuzo8yh17_2gCYSv_H4Q82UKvgqDJ3Uv_Z0PSJP5h9ftRI4HgyHGuHdllvJxNt_x__zW8mU1Cc0uaO9lGAGmwJIxnD2E7GO5v6RPPQ5naRhRjOfcBlGtGwT4G8sUyhXc1idQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پشماممممم صدای انفجار اهواز بشنویدددد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101720" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101719">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101719" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101718">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=XqLedg_DIhtEr53fO89IbV67riz_MYjjNNZBzukN0xubKlzqxZ1hJgWBM-zfAmEMKa6kwT7339zbFHs3HWs9FI4NsbFz0hwVvbL3ee7F6nZStq2vXewEU2ReVmfzOqakBQGXq87fGuJ_PeKLq-rSufETDKtLxdDoZs0hsNrwsWn_L291ln2VTHM9a5eOOTi35t0-9aR3L9u2QdmBR0BH26rtW_dMsvtsC8tcpiGs938EWgH8umdomDIj5hdSVDn7WZqgxEsMDm7wT4m4RcyslU3w9pJ4ewtXbb7mY_oIe8wHrzjA8na1TPEk_WehYxd6CVs0qLQa3WpZ-ohnQ3-z_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=XqLedg_DIhtEr53fO89IbV67riz_MYjjNNZBzukN0xubKlzqxZ1hJgWBM-zfAmEMKa6kwT7339zbFHs3HWs9FI4NsbFz0hwVvbL3ee7F6nZStq2vXewEU2ReVmfzOqakBQGXq87fGuJ_PeKLq-rSufETDKtLxdDoZs0hsNrwsWn_L291ln2VTHM9a5eOOTi35t0-9aR3L9u2QdmBR0BH26rtW_dMsvtsC8tcpiGs938EWgH8umdomDIj5hdSVDn7WZqgxEsMDm7wT4m4RcyslU3w9pJ4ewtXbb7mY_oIe8wHrzjA8na1TPEk_WehYxd6CVs0qLQa3WpZ-ohnQ3-z_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101718" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101717">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfeOzvSFfXWRRnJ9J4rXyqJZ8vaWGpdxlH61pBFoQJBjHLEY1_Xnia1vsxBmGR_q23y-S1E1o_2IbwN68y8LPZili6KnRFFlh2nkjes7RZD2yjf_hSAhfq6rZMTeqgPtDY8w6K6mgsSxSs0mJPhR3WnJR7oyFLTDmjnHB2YkSBS47RZ3TIa5r_d8PjXJwDr2CUyPEG8UdDt5qJsTh86wlzvMQnOZB0d2vrvf9mwFpP_7ZzIwyaLBEVIHiU3Iez3SzHjMOoKJphRQelOgywSukI_-h1x0SgXELdOAv_1V7PTRuty63cJGVAg_lOmJJI_m_UYEI_RgtbZKO6Pi9r8TPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✅
کریم‌آدیمی ستاره بارسلونا و خانواده‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101717" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101716">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=tdFOgNGI5kqx7ukhcxx-N3Tzmlm4GMvkaUQDqiCwaNdHqdOnXWa-VfMYIdYLahGrp3OVk9Bpkl62Ym4K8byfdqtGgfEmCE39E9wMgbdZtf1TgQ8kgtgTAlEw_GvTmP1U3mJKCqfJeyXy_OYvc3dUxYQQeWNoGCu1QJAPvAYvdm1QNgiKvHCdtaQHAj0GEzDD37jqWJHU2Nb5_obkThtF84OkBip2ZzNx_G88xxCZz66_P7_VPmfH9j2VkwUhOxPLbXv1CygjsNjjltPMtT4Mnz_qnBN0ZyY1GDe1pNRbVNXmm2fXKWLzVb_zuQpV0RD5RN_pQlNc-8GNvxAR4m3sRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=tdFOgNGI5kqx7ukhcxx-N3Tzmlm4GMvkaUQDqiCwaNdHqdOnXWa-VfMYIdYLahGrp3OVk9Bpkl62Ym4K8byfdqtGgfEmCE39E9wMgbdZtf1TgQ8kgtgTAlEw_GvTmP1U3mJKCqfJeyXy_OYvc3dUxYQQeWNoGCu1QJAPvAYvdm1QNgiKvHCdtaQHAj0GEzDD37jqWJHU2Nb5_obkThtF84OkBip2ZzNx_G88xxCZz66_P7_VPmfH9j2VkwUhOxPLbXv1CygjsNjjltPMtT4Mnz_qnBN0ZyY1GDe1pNRbVNXmm2fXKWLzVb_zuQpV0RD5RN_pQlNc-8GNvxAR4m3sRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت تلخ کودکان در‌ جنوب کشور‌ بدلیل قطعی مکرر و گسترده برق...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101716" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101715">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmJG4XuANclVcKZI5Q0TIlkh4dDzXQqC8RhLlcnqjkLiU9AhUp81CEk8Y_UFrDxGDUOTmmQ9tMoaK2ekp4N94rxBElRsMSjjmX3NJOP9DASry9UANUGW3DGI-r6NANZObBAQHPq0IjZAMEBVrgdqIhH5JqX_JkWWMDgg1b5E8vImdZBR3ngPP6Rhs4UgK2_qCCBMNRPfP5zfeiKIcrt8uTA06_pDAojL5xSz4aJYfspyC5Nf9yffuUVOygMadXLtRTYXjjoviWzLmIDfooUvpMqWNvxSR3Tz8_H4GlwppgepO5WJRToyyUfww9aR_Kl_GsZT__6COYj3FsXPSBRvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
❌
اوتامندی رسما از مسابقات ملی برای آرژانتین خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101715" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101714">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N78tgk4yUhcWtJ5R2SvCmLbnyvSGiw0NLF0A5teqXlAm39cUMZOXutT0drGV1SfB4kez00C4y1CfkjUSaTVObbthpW6aHhX3bAZmt5YbBAWxSoquV9Ty7dohIofJYsfU8KhWISw83zCKo50QfPC4Ylmpqd1ZFkqs9m12DBJOtmYIrdn6i_D9vxEJO3YlOA2YHgg_4aL08IRAdzbhueTcJCtdXEvv_I51AsMDZyiPYg6mIgjjExRnYSJ2nuBMkmt-WoH7LJlQ_46lxg_nLBMk81kTBAaJJ2PrIRfbyv48yLK5HQmZFgxU0tpEELK48QfjNDo0hvNvE9Q2Wm7fI8KP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101714" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101713">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=GyW2oJT6G2LJnlUGdWl0-xuB2sHG-rN-8SgQLQtdusZ-sYHM2eJHzHdgSwk7NQXKVWSfINQQdE_0Vr-nGM21PRVIL6AeZMQqcluiCi3lkQ84UynY5s67HgqrTOM9l7FZxJm6KE9qw8wRVHPAYBMPPTG6hKu4hh2PVjVYtL_izjLH2az4mc_Dhsxf4FpeRSIb3lPYrQNA-1PK-742QWcUUb8k1Skw_PbVKJO8s5Qax3AJGKjVRW1J6r3-T2A2E-s5IJZX1Vr_UbuAcDHxjcplXDTws0FO7l3TFcPd04D5lRb-EaG0YBJ7QVjhIUgKpxlCNkM9zhPOXRbI_ivTCnURPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=GyW2oJT6G2LJnlUGdWl0-xuB2sHG-rN-8SgQLQtdusZ-sYHM2eJHzHdgSwk7NQXKVWSfINQQdE_0Vr-nGM21PRVIL6AeZMQqcluiCi3lkQ84UynY5s67HgqrTOM9l7FZxJm6KE9qw8wRVHPAYBMPPTG6hKu4hh2PVjVYtL_izjLH2az4mc_Dhsxf4FpeRSIb3lPYrQNA-1PK-742QWcUUb8k1Skw_PbVKJO8s5Qax3AJGKjVRW1J6r3-T2A2E-s5IJZX1Vr_UbuAcDHxjcplXDTws0FO7l3TFcPd04D5lRb-EaG0YBJ7QVjhIUgKpxlCNkM9zhPOXRbI_ivTCnURPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد! باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101713" target="_blank">📅 00:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101712">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=tcmUvX0w48Xn3zbMZrod1ogRdr4oLu0dMxa01Iqp0eNVxHBcIuhszJFEmYCCtOYg1VpWLd7J3XOQs-99pKfvfgkxOQ8JcU6HfhygPi-klnfQD_hoq6Pqzc-udm-RXcmlOckde_X_0y-7MWu8qLPD1lcPjsKhdlEAGkglxpGsATo90WxGmV_6qXTwUF1K0D7AgTlz7mGhgJeaHx8HedfaGOuZWlHG3Xo4hNjKgUEpPx569thXIdOrqBrIgWD1u9nh0ASZZ9OgzcAaHuADW2CqT2oy-g6BkG-PAB0o-MUlwlxYg57E9WFtvCxKMlcep1Ol_vz5Bcl9fBuTKxmZHb57DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=tcmUvX0w48Xn3zbMZrod1ogRdr4oLu0dMxa01Iqp0eNVxHBcIuhszJFEmYCCtOYg1VpWLd7J3XOQs-99pKfvfgkxOQ8JcU6HfhygPi-klnfQD_hoq6Pqzc-udm-RXcmlOckde_X_0y-7MWu8qLPD1lcPjsKhdlEAGkglxpGsATo90WxGmV_6qXTwUF1K0D7AgTlz7mGhgJeaHx8HedfaGOuZWlHG3Xo4hNjKgUEpPx569thXIdOrqBrIgWD1u9nh0ASZZ9OgzcAaHuADW2CqT2oy-g6BkG-PAB0o-MUlwlxYg57E9WFtvCxKMlcep1Ol_vz5Bcl9fBuTKxmZHb57DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
‼️
🇪🇸
یه فرد فلسطینی رفته وسط اسپانیایی هایی که قهرمانی تیم ملی کشورشون در جام جهانی رو جشن گرفتن، پرچم فلسطین رو بلند کرده و اسپانیایی ها هم پرچم رو میارن پایین و پاره میکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101712" target="_blank">📅 00:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101711">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQfT-M3P8uAPQ_nh4DOnumD8lDqF7Y0C7s_tx5M2C-F6wHvsZbCTImWvbjorfikqtH6xGFky4dbxNYcqBV5QL2-r1h7Lqp5wBjmid37dv51i8kjZ6-PM91irarWahwBZUzabOcVQy4iAKZsZz0YcTx_Z2Bu6KALQRPf2PwFE4VoTU8NfZVF9TQCv7TDWp_ZWAbJ-65XRm2cUafsqqntRjIUtsNUHwCu7C9sgCWr2OcyCR4YQefVTP4eKLLfWgb5GKENhVRToT2Q8pTFy75B-qHvtP9ynxCshdkiE0XJJkOSGxF_C1oqKwfn9l3aeH_Phtrv8dAvhkTGSBA6MJ8Bh1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رامون آلوارز:
لیورپول قصد دارد وینیسیوس جونیور را در تابستان آینده پس از پایان قراردادش با رئال مادرید به عنوان بازیکن آزاد جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101711" target="_blank">📅 00:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101710">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhHdJWnrfqwAsdRny4L6uMvq9sXLIURR5pnE7VH2i4xPVtZ3afuZlsPl9MD5d6szKw1jqCtxn_MKrcPBR9ONE69i-KrMbIKhYF9fRIVmiQKGDWEulL9tNu6TFMhi6YrRtA8qs_VfE91A-4KxoKSA58FrdOphr4KzCYyHCMR_Vg0-VZAg1xXGc4NsnfIglDtA_Oj6JjwVaewnvHEiiCuKBawNKAAwLlwlPnR1tlXjad8jyETeyXTezzVuaavORK_gcsu2PX8IcBFpu51XUrvEGDCnUdrDDLLVhCAxxdZgfDXcDutQvVrzt1hrZgfXRcGn6PMnXk3xgT8xyFY0FxI9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزشمندترین بازیکنای دنیا تو ترانسفرمارکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101710" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101709">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=SBa1dIZsokwqItbRh_-GqZtf7YYfBr4wIHCVUHduGaY4uEotOphcvUbZg6cIegoVPzWR8gCaa46xEi_jQATUW1pr47PZ-E-pr7pFoL6G3MRZtP1yXqPU-f7cpnDZb7Rjubo8EupDMFNyBPKuflWcNOGWD07iGpo4xbl2I2ABeiPDuVamShYHQT1akuDbGFobY4HsCWIG-FPfmdGz1AJhJHzzP1CQPRMOCY7PnTTKXBGSD-4dFzTTVei1JDLczP0xo5dun2ONMqY24AxEN6e22n1v2xOlVCZDvjmgcuJkspWXeNQSjZDZplH-y4hcJ9XgJDC3voFJ7FrNsMgOjgFe7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=SBa1dIZsokwqItbRh_-GqZtf7YYfBr4wIHCVUHduGaY4uEotOphcvUbZg6cIegoVPzWR8gCaa46xEi_jQATUW1pr47PZ-E-pr7pFoL6G3MRZtP1yXqPU-f7cpnDZb7Rjubo8EupDMFNyBPKuflWcNOGWD07iGpo4xbl2I2ABeiPDuVamShYHQT1akuDbGFobY4HsCWIG-FPfmdGz1AJhJHzzP1CQPRMOCY7PnTTKXBGSD-4dFzTTVei1JDLczP0xo5dun2ONMqY24AxEN6e22n1v2xOlVCZDvjmgcuJkspWXeNQSjZDZplH-y4hcJ9XgJDC3voFJ7FrNsMgOjgFe7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
▶️
در سال ۲۰۱۶، مرتضی احمدی، پسربچه افغان که توان خرید پیراهن مسی را نداشت، با یک کیسه پلاستیکی پیراهنی شبیه لباس ستاره آرژانتینی ساخت. تصویر او در شبکه‌های اجتماعی جهانی شد و به گوش لیونل مسی رسید. مسی تحت تأثیر داستانش، مرتضی را به قطر دعوت کرد و در آنجا با او دیدار کرد؛ لحظه‌ای که رؤیای یک کودک عاشق فوتبال را به واقعیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101709" target="_blank">📅 23:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101708">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=HnDGRQ18l_q3EieUSD_fv_etm_RniGYxqMkQMXl-q7vlRZp7Bys8DduzT-wOd451NlHX_RIn3ioMiFnLX-hORAzNj7X8y3deeT3a1pLCghQu2nXky_w3oXo1TXQL1RNgi23HxJ_oFp0-ErqKuKQ53qnyZh8i1oo36EfdnkmD-tNTmXQZp6sYCG42rdjpKyzvqHKkPOxw6At_cEGhmEmnorKMarWSydVKSiSmo2qNA-VGRF28a9zgygq_mgBl3EuttlkH_cT9hbOetwKIbyaUtePJ7RT-8DwFxQyCvXtStB5UqKYzLCZC41mqbFQ5JP24nkOU3KsJdGZXNB55IOZLaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=HnDGRQ18l_q3EieUSD_fv_etm_RniGYxqMkQMXl-q7vlRZp7Bys8DduzT-wOd451NlHX_RIn3ioMiFnLX-hORAzNj7X8y3deeT3a1pLCghQu2nXky_w3oXo1TXQL1RNgi23HxJ_oFp0-ErqKuKQ53qnyZh8i1oo36EfdnkmD-tNTmXQZp6sYCG42rdjpKyzvqHKkPOxw6At_cEGhmEmnorKMarWSydVKSiSmo2qNA-VGRF28a9zgygq_mgBl3EuttlkH_cT9hbOetwKIbyaUtePJ7RT-8DwFxQyCvXtStB5UqKYzLCZC41mqbFQ5JP24nkOU3KsJdGZXNB55IOZLaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101708" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101707">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwMnDmVkKI1Ktlbtgwm1pHlEl6s31qJdCIBtYdTPjRJaQc-9bYacaAfDVTQiDUAFTAhOV0MqG4KiwkML-6BIt7m2yeojqv67H6tD0VVtdOH_JT2lQCVlzQwJfGBBe1Y4XA20UkVfSpu0p7dmTH6bkF_13rdfMoTsrUY21Rht7GxOcKZJLydibpFz93dRRmZjb-jefPbjjttzXjqeMVzRG5W1kqpPipYO9TZ9PeLamEduoxrvFFkmRt6C-IfoMt3vpebzm4VFYRvBVmvfA0x7xiwikAk7kOJUJabiAz9wInhEn1s_Le_o2XwUp0TDw2L53_u-NVcWt8MTVCP3NwluUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ال‌کلاسیکو فقط یک روز قبل از مراسم توپ طلا برگزار می‌شه :
🔵
⚪️
۳ آبان ۱۴۰۵ : بارسلونا × رئال مادرید
📝
۴ آبان ۱۴۰۵ : مراسم توپ طلا ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101707" target="_blank">📅 22:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101706">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVioYisscrv_lfp-sSYx3iuuKB7wckU0s16lVIDd4y1PbjtmJAXxg9gj7_euwTtQ_rTfRSQXSZD1RwmvYWttAAtiw3Xuk2OMPY5bJUzBZZAPSuN2oab4-4-G2Sqsm48jmk7zjCBi4oLwinrv22_kskGcJSaWAMBbb5dMf6wJfoZo0BtmYJax7TL5GBHkIRpQkglCZH0vGwqGZBeuattiQ5KLQcxjfDxsai2vlQOxojIT2Nlt3EAWoJ5XCR0OkLBIvYRRXClO8EWj70Qxq5QEKmB9AFRt4kCQ4LLDHjznx8pn_2-KpX2fEhgSaALOeIfkjfWHvjAxdBFgZOtV_9kkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا درباره اینکه چرا همه بازیکنان کارلو آنچلوتی رو دوست دارن:
از نظر تاکتیکی دقیقا میدونست باید چه کاری انجام بده، اما چیزی که واقعا اون رو خاص می‌کرد، توانایی بالاش در مدیریت آدم‌ها بود. همه رو کنار هم نگه می‌داشت. هیچ‌کس از نیمکت‌نشینی ناراضی نبود، چون با همه عادلانه رفتار میکرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101706" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101705">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X02zvWrI2si_Dwl2FQg7In_pzJH1UMxDaF5Lwi5wuHRxUJhQAs5HrMaXnerpzvZD5EcON07tYKaql7he22tU-6lpzW0M46FGK5NSRetl8aw7q8nF6mHEzCi1Jeo8pMSM5-DtXKQhHqCyBmdaiBJDG4BDtljEnZ-WvZ24TQS2yltRS_zIo7az8aRG-AiRbvYWz0LP5c0znbLl8NDi7dma1H_Pj9aJqHk2Zyq4-qwyoAR2pPa20L-W5_SocsKeRiDE4EVPqSQ6bB0XpzzoQsW4f7oBvHRdI58IlPoQRb1SZqMcU8EODvPLVFotiDY4z1hm_LUpSXTxFhglqgqZLPPJrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
به پرتغال هشدار داده شده بعد از خداحافظی رونالدو ممکنه بخش زیادی از توجه و درآمدش رو از دست بده. کارشناسان میگن فدراسیون باید از الان برای دوران بدون کریستیانو آماده بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101705" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101704">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🔵
پنجره نقل و انتقالاتی استقلال باز میشود؟
🔵
💣
همانطور که ۱۱ روز پیش اعلام کردیم، باز هم دقایقی پیش که از محسن ابراهیمی هم ( ایجنت و معرف وکیل ایتالیایی همه کاره پنجره استقلال) پرسیدیم ایشان اعلام کردند پنجره استقلال به قطع باز می‌شود.
✈️
🏆
@abitajsport</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101704" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101703">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0GRtTNIFyTx33WdclxNlph7cDXA42OoER4khwL2ZUMsi7myizFdnsEca8AprTbmYF-JgxAktYxKYgL743KzPRQO1NkiEAlvsnCOgDOQPCnpqbQ44IVtPxeUFJISPOtG3eWkEORFFtruy79Q0GJoVhXAV_CVubifJfphfFl863RKxf-H1XegUPKwcRiiY5QiMG-FWU8MsYWjxMqktH-aFk9b53hbpvOxysB-q6MCttU4gQFsf8xxFLEQei-CFdugt4KdqOZQcdjJG6FHL5mrpvqp7smrIbWwMOOSAO30Y5Qcdoz68ImqvIUGjTjd0wHGMpDuxebNO8CkoQagOONz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه هنوز شانس بردن توپ طلای ۲۰۲۶ رو داره.
نشریه اکیپ یادآوری کرده که چند بازیکن قبلا بدون کسب هیچ جام تیمی هم توپ طلا رو بردن.
✅
کریستیانو رونالدو در سال ۲۰۱۳ بدون بردن جامی با تیمش، توپ طلا رو گرفت.
🇵🇹
✅
لوئیس فیگو در سال ۲۰۰۰ هم در سالی که جام ملت‌های اروپا برگزار شد و فصل رو بدون جام تموم کرد، برنده توپ طلا شد.
🇵🇹
✅
گرد مولر در سال ۱۹۷۰ بعد از زدن ۱۰ گل در جام جهانی (مثل امباپه)، با اینکه به فینال نرسید و فصل بدون جامی داشت، توپ طلا رو برد.
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101703" target="_blank">📅 22:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101702">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG1e0ALx7rimIwmQ81dXjvsCtzV2JRA93JkP6WX63X-ZMzGRqdmlPq5mQsGryzVgvxFGZvpButxH2812eMkOz_sW3LN56KQ9s1cdHPPipyIzkkRJCzzKapnYO6ntHTDzCCY2zoSF06FpXyrpYsSwxa_zcDuOF0G3Qc6nEltmzlbMqDHk2Cf1vG8WDM_e89wDfmE5CqqrMeY5noiz7uIhjUcwHG5zSXzsj_WcFyOHxcs5fWtyoaDslKjXsOzuFcGcd_NGNhhkRFwQVdp3C8TJ-qK9PlxmkFTpa5pP-heEBvcCPBMF85YfVRDaJPCe67T3ZoPE0XBDQ4_ouEvfBirl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101702" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101701">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO09WcCUjPQ-fNE-0eaFUd4iOMsti-Wy4RWo634bt3jOQM9RjkinBWiwRC-n6Ra-_Qykj48rmkqDljWE8zl5RM7-UcofIHJyyJcVBoCxfp1zn1Ab25Zfr0m5BorHcisp3BF7s_wwenrJToxbjPYFGc0uBpwMewM0_fPPw6eJUd-n76P-Qh8bdaHorWeTvk4pDMmYm5g2J9vlImUFMbTv5xB7ty3Uh2uwTBZ1Mui-Hwre9OO7Zn9qCjyJO1HGsuYuvXrqJ6dIQHvz_vA1LDFi8Y3VfPAGHMv3Q1-TYDmIWWMzi-JCAWHqeUEUA_gM2DXCOFHOWqMT60B6_WXttMhk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا:
رئال مادرید شبیه یک تیم ملی بود؛ چون در هر پست، یکی از بهترین بازیکنان دنیا حضور داشت. هم‌تیمی بودن با کریستیانو رونالدو، بیل، بنزما، مودریچ، کاکا، کاسیاس، سرخیو راموس و په‌په واقعاً چیزی خاص و فراموش‌نشدنی بود. هیچ‌وقت کامل متوجه نشدم که برای بزرگ‌ترین باشگاه دنیا بازی میکنم، چون فقط داشتم از فوتبال لذت میبردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101701" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101700">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAloG3ksLermbr2DL1e4SG5NVDreIYrRV3nm91Me64ZzaMkpDK8nSFUFYp5dLVWT6KoqWaqv7bG4VpyE93BEBYKQVMct3srZcWOx8t4fsYUiqER4WuK7YjDB7v1rjHomK4PpSQAebGSX6MTflUoAbCg9ZMKS3i7ftnybAv8uvf2tMzWIWjcYxxd2irPkUF7nDueu1vQrByJSCw79Y9kHQxqbeKDSIw73ODX4rSwrXqQuaC1DDX4f38LyzVVOw64zFNcRTyxgJukgZBMrJfrt9ZJrEBTUZwrUeS-Q-e1qZviCvVSw8SV-hE3WH9Zae3TUxFxqvbl1GWAVq-wTiPSomw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101700" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101699">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc1D_vgkWN4uKlArvdiUj813oD0gZPKbh9SNJKyuq0iLYs5Fq14qkUY0fHFw6DUfxOU80TzgAqfbn0v3buuWdmgy-sP14ea5N2padtiEW9_sOfeI2K3CJLqYgvEc_1f96Pl8OSBpgcJIPcWAU9K6UvSklIoZ0P0MsScBJf8vF94z39abJtBvsHghEDCpPgPLFwmR1AuEfs_BbRQZRm4lHP41eozJzcMGl0FxYZ0fDvEZ_1Ozt-7r5SjAFE1C3lM-QqCLeonQgaIa_XnfBkTPdhMsWlUYyYjs1rCjk_O9vY9FnWy65dFZ_uDrP2MvRH1jxccgyasLzMJiqS08lteq4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
فدراسیون فوتبال نروژ قصد دارد بعد از دخالت دونالد ترامپ در ماجرای فولارین بالوگون، یک شکایت رسمی به فیفا ارائه کند. این فدراسیون نمی‌خواهد این دخالت بدون عواقب باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101699" target="_blank">📅 21:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101698">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYtrgmNnuEemgfTxZmc8OhwRcxg6cbK1ba7tvPU09sxy6eVaRORsEucG1Tl87UlUeV2kwZQkwmhjYnD3dERH3Jhfa9GfCK7pS9PCzmsC8CYUbRId1RCLh92g-xyGUWZ8QIHiLwowbZlASWuyB7poicSIBX6doX32BapJHo5zJMy3Gpx98cIv8iY8vIUuj4RxXML9CMoB685uypdMtk9sU2v7lr1m5yeAlRsJrAn39YIYm9ficM8goj3irzisNkWVSRxzz7oJyCgidmEiiQaGqwz1mL-kjut-9M64M3KDCkT8qrtnCcfzSXOxhmVjDvSNkvM0P0Ivk9WlYaucin4jjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آنجلوتی پیشنهاد فدراسیون فوتبال ایتالیا برای هدایت کشورش را رد کرده و گفته که میخواد در برزیل بمونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101698" target="_blank">📅 20:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101697">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvemKfVeP3MfwfMmIYmORVZD2eMSXuZs9pyzCfHL-k8alvyGVkyb3drAiKexANwROSM8vpUdIqdXHrqOaU5WTDrc7kMmn74CjxnQLYXM8TPqT1cxMZGA2fSO2chkeCo_W8U5ECfm8-sIM_YiOWQArvh3vlcJMzFng38DajqqGUHxlY72c35xX6VdDVEqk-0DvDywxnGVH74xa9XTAA9yI01B-gV5HJ2NLwlHyUbgXbsBiV3tuzmGAN7C1U1O5cMPa5USuzqgMHQAGkhIbRRIY2rHbuyERfZoYXlnmeqRxK-fg7hmDSvRAG_jtnCbCAstVSjCQiKSLZG8dMRODOAGgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
لوئیس دلافوئنته بعد از قهرمانی اسپانیا در جام جهانی:
بعد از بازی، بازیکن‌هام به من گفتن: ما همه‌چی رو بردیم، در تمام رده‌ها. حالا دیگه چی مونده که ببریم؟
🚨
🔻
یادآوری:
این نسل از اسپانیا قهرمانی در یورو زیر ۱۷ سال، یورو زیر ۱۹ سال، جام ملت‌های اروپا، لیگ ملت‌ها و جام جهانی رو به دست آورده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101697" target="_blank">📅 20:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101696">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIUwqzfDWjKwfzlE6ixVjqonIsWd3_deky5SdzFW9cb4njS38i5X_g-6mptKSCvEOH6jCPrtYOE79ic-RfLS4xiGfTaqAefJnj1l16XIQiriCvvLzXVw-hQ46cbpKMieLdv1geBcXakwND6kC62vB9oxMO1uaadtdKZ7BzbheM6efBiGvjspaL69_zwhm6qBqKRJtpxOzUXBPefCa2sOWHBQ2oJ5snqus2yF2qTrUwnF5XxDtGNT9xk8iawSkLhjeQRzVSlF5RCEK72Ll2EwCUdFLgk34EIdB0YA_AXfhVBJrGS5EoDMweRz3tGHJB3GQNV_uJ7TwLz48GtsY7iSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار در کنار بتموبیل و هلیکوپتر و جتش :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101696" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101695">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY75OaZsessNJtz31uDhN9DMw4oovXD7-wx-fxps_QYVfxpyqIz0PFBucIGVWjgERsqe7JcoCkxG1jO-fPXgFkcCiRa9wV7RfJHdEnuXJVC73f96yetOZjZ6Itlfxuj8fxbiS9ZUFgvqyJ9P6afA0xMGSAiuph6PdZln6tnFMejGjB_uV4NZB5GjXDUWE5NYQddnnpfc-LYWY8g5YZXTU-FjPKgdAz82UDX_zbkX2atlU7dMmuFwAUiAg_PaWBkepwJVO9VmUsz8ybn6U_4m2ylPKQJtoaoY8wrJdhYrG2o62aq_ZzLeB2gOvFmqcvfLpmzgwGWOEIF2Bw_Q3NKIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101695" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPB_cPSqreLd2seEh5nccoHq-TjiKsMocQptiO8onYzIs2Vt7FVFGd9UXRhEduO2B3WkAWWzrCxnhmdx_PCiVBgEq69K4hbvEQFQUut8lGjfP7d40Prfg3okASm3DIh4GfreSPd1eBTyySA5dA-0ZB5oxABxsowap8FiAW55lRyRgtk0dbUaM729elLlExFe7pLrw6kxtgZwt5g6Yhv8-WMFyA3hGBOcycmKa7PsVuUUI4r0kTYZVw3byGCtOIecSmDXQNVrGYBD1zx08aG98UrLfpBIRsvpRVe1enuhxvE002C0dGfAA1AEL256gmTdDO0zMPdyqNqLd7a5OlPWIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
سامی مقبل خبرنگار معتبر BBC:
🔻
باشگاه آرسنال قصد داره پیشنهادی به ارزش 70 میلیون پوند برای جذب برونو گیمارش به نیوکاسل ارائه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101694" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101693">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=IyR8h2LmxFDBtpdPqbZjXxUs0KGqkLG4xI-UYouCWfKkcx19y_WNRo4L6dIfcHUxqEf1qh24lrdc-IYRdcEtE66zMUPTUHDr1tLuN7ZWoTvfB93tMHgFU9LC6jRiY_z_GqDMWn7FI454XqOhsQGihsCKlbh4o-EAvmzYXH0BSA61QCJI271vvxlJ9AkzuXt7Rw4YPGRBsG-zmkDaCLRnR5GlWWZjjj5iZbEioGtVC6Rb39kcp3NhhhuudhUWi5VrVllsaYpZAQ5asDM7uvYKg1fpDXKUtvuJ9nCy7gk6aybFPmokFprsGtjU6_x5G4R31tGc97kzjxe29Q88Q8WfVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=IyR8h2LmxFDBtpdPqbZjXxUs0KGqkLG4xI-UYouCWfKkcx19y_WNRo4L6dIfcHUxqEf1qh24lrdc-IYRdcEtE66zMUPTUHDr1tLuN7ZWoTvfB93tMHgFU9LC6jRiY_z_GqDMWn7FI454XqOhsQGihsCKlbh4o-EAvmzYXH0BSA61QCJI271vvxlJ9AkzuXt7Rw4YPGRBsG-zmkDaCLRnR5GlWWZjjj5iZbEioGtVC6Rb39kcp3NhhhuudhUWi5VrVllsaYpZAQ5asDM7uvYKg1fpDXKUtvuJ9nCy7gk6aybFPmokFprsGtjU6_x5G4R31tGc97kzjxe29Q88Q8WfVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اون دکتراهایی که دکتر علیرضا بیرانوند گرفته
😀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101693" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101692">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz-67gV5roY4gc85GT-nKeHmVaTJThQk1OfwJYFfQounuyzg2YzKR5sXvPR-V29rgh6jn66To3fN_SrHUz-r4kZiRdzEHIFb_82t8MtNdXumxvhnGj-AvbMhC6KTRyuxjOsX-23O5tcL4BMQjuzqvU9M9gSTz4YI9lV5kLUTIDcOYpn5yAPBzbsEXvubp9v-L9JbX-U5DKWf-103KL_jnfxL-OUYEyr67wJHvGQAUKtuL4vK6GPwH2f5xKBKlgjzr-JbRequCFyjK0-A2E189kuE8tnaFcvLmV8OmMOFqlzt8iRC-yRyEBnRKY-RVailAYVbfVQw4vYJH2tSgI2bQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی که همه رئالیا رو برد به سال 2013 و اون کیت معروف..
⚪️
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101692" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101691">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQWf06u6PO_3B4IGyJSRvLLfvnHGo8nSvFv-TkQjaJrx4TiIeUHcIZ6VDce93Msjt-x0spy1BIThDKreMr5N9y704E7KuEl3aogBpNwEHhfSpnVr6kzusauezIWY7UYHrrHRo1JgefFcknoJ_HX6PHXEtrRZ5ckgE1lAl2hUZYU3dhuB9PCc_PDcLEm_1Htxg6HFGgCfG8dcUOR1OjJS5bSH-XViq1UZuGC2b7esq2al5mJpfrA19ED4XJYuufQXMRCqeorrHlwm8uqWwGBtC5Re3oreHipCD6p7kF0ce3KB3uWjDezG77a7Pwnt6fPUyQsoIcRqSSiBKNx81b1Zqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو درباره پیوستن به اینتر میامی:
بی‌صبرانه منتظرم به لئو مسی کمک کنم؛ بازیکنی که یکی از بزرگ‌ترین بازیکنان تاریخ فوتبال است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101691" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101690">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyUZQ-XNS7BdX1bHAM2hQYyCNFltplGQj3Fm-sPuTYWuB4CYUqY-3rvKZPIe2pPm2dzyOC3zkVsqcbUr4LfG9KlBEMAaEnie3e_3iO3OMD4IpQrr47ZZx_W4RZfkZ2Iv1E6xDWwrrdmYftRdUMWLZlqHcYFajkjpICatwcFI5KoCI0pl49HycOvjm3jgG7f-VUQwuZxrO2bl7ZfDwobwxt6Jnb6bHyhCaE88YyOhBkBMWcGMZWkQd6yxRC0R4DDTuo6onjqjKKY9u-9-DDHQ8xCCZ8qaX-iwW7JDOFo8ZMF5xZJQd-F_jFJoh7UXp0uQ4l3zMuvuXwlrCt_Rx7CNMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
فوت‌مرتکاتو: پاتریک‌ویرا اسطوره فوتبال جهان بزودی سرمربی تیم‌ملی سنگال می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101690" target="_blank">📅 20:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101689">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQDPcoudS7SPltnqL6mKUcCxSAR80BIcfHW-Bd95jlI1jiI-bFrDLeaWhYYSMXVG-L7FsognWP-k1FJ4WPvue43_flxNz-AZt6Q5TPU3XGgM19Ws306wk4_zdXhNXXFJwrTmJPasMmlaNVzuTQGQgMJ_1prGLjnQ_IT-xj2tKY1HF-osnDx-qFWzdmX439n-pIIxgS0eS4l38_3uxJD-DRjoNCOibimOiCkliAyz3VOL01ARHDrpldxtDVvs7n6uFp5ibxCo5fFhPjdjdnex-Nk97JFZHn0mnSHgsdEHf-mFN9lMGGwzyx3XyiTQFCU--BiJnFuPtbeDafqG8KmjxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی
؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101689" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101688">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLQ3UF46g9xMhYEeWfgGiAyXVblw01SJlB-8cfKm693dnXjCERidVGgY1JYuS8LsvU7twNTFbPspIk4lTRf6RFyQKyTcuWo01OLqL8EJldFvXcj-LllQi-lEwBZ_qmtEajq2aMNOcVqUpbm96HVA0pyHkzYzs3jgGHd5fnrE1tiOEZTk2Ee-YlAaBm2Sphp1b5zlrLuXzjaaiVb_vFGDRz-TAk3Xk6-iLWlSl6UD6xRnzFGLQX9QQ_H45h1GiuONd8zPx0Yd3IYOoFDkXT-c6pve1zOFZmyNqRom2jKoAiOAf7ijjOeo2KkxV1CYfP6PzE6MKb3IjgVEYYp4gMyjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله کارت زرد به من نشان داد. من مطمئنم که این فقط به این دلیل بود که مسی آنجا حضور داشت. ما 2 بر 0 جلو بودیم، بنابراین احساس می‌کردم که داور فکر می‌کرد:  بیایید کمی به مسی و آرژانتین کمک کنیم.'"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101688" target="_blank">📅 19:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101687">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
فوووری و رسمی؛ تریلر FC 27 منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101687" target="_blank">📅 19:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101686">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMjEF7yfhGsEyk94u73Pi1Re92nRBQ7Q6ULd95BYad7Mo3fr5xkAFwwouG-hiQEASh3n-X3wE-0ESOH898ufmGE8kQkYxTM46d-2M4gRTagLQ8DmrFeedLvM6aRyhGSTyPWFYg4aGQcXmynvXlZ031ArVJ7UZ2_vbzYAWo9tn3QNWrm7R6NskGiieqIDDHdSu9nXfbN0VzACbpEAjpXoSFjBQlUcLu521dhcu9h-wor7qJOPDTi-W4JEIU6WPyg8aAx6qBhq6LcZ1oWTk72N181297kjnHA0CuR7yAJ4HgxvWjlO2ltov1gsIMGl0Mrb3-F6JlAiqQIb0uQgKTfB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101686" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101685">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTCPzwf83rLP53Vw7qxXHlro6_YtYyNb74e57ilRcDLexGI2qmQd7_vJNgzAQxfeqZKtFxSM5nOsU3itxszuxPggmMtSr4awZhDIMAC3a0-MUTmlDiKQj9jx0peFLJyY5NqPu2NiFCR1xvI6j-8iF17t2ur4eer3jAd3InVqYQwReWEhOlwVBMNH8CqbQQOuP_8GIYzP1q34oL3CLdiybhDNFMGTSrGeRLFgu7KAiBEosrSdjYrIRbnEE-sGRf_o4DLOqR5GcP7c3Dq3L0KCuYjhYdR2jyIj7cjBLDH1acaSGs99zezs2k-cVBB_rW9BeXkei94AhTeXaauqOfLqtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101685" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101684">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRJh7Dd1SLhk8suxJ7WZEVwxBzhyOrW194GnKPlk1pUxcPGQYnIcVJNFdr4P0bnMNbtJN4u_HklHEls041oqMlH5a5QVBG98I0tlSxFdgG4teNxk_-VN6eu6DRnpdPT_kLJXvs4poiIJBXVRVL0PdnnMpXlJnb-gfakgBiyENvGTRruOIUaucR7-KQoOGc5hQGlfK2t0yV2lWr4-GekeMp1lg_UveVo8o-j3mTzUPp_OWMh0HspVZf8Imr27ErMqzijJBGyeHGd0S-3RCIgH22B6EtkasnLIn7DAxMx1rKFBc3t_aLZtWAXD25fYUSVWbAGMhoAVreC9PzLhCuDKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسمیرو رویاهای همتونو داره زندگی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101684" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101683">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqbpFhmWIEAUZfdXQDCj3iQ8NfGxz_IGCkxxY_3wbs_kDJI8RcLIxOIXp5hq_w38bEQuTJWFNI8ogwqLEG3TAvTgeO0gJeWmsDwgjGNsRhhL_eTIP8S7bZJjD78qH68jEq857H2dkNvKmrHIfVXf4wlLbJuElFvuCfvGBo6qRQnxymU2KRYWpEeS3IoBQUDpYdOXxudDkV8Z6gwsIc62vU0_cX7o8NFfKYRzNXXNE5YkOoMc1P_boHwxHPPb9A8-dBz4_Caf4Jj6bNcfUO1CTb8t9C7_bLWW5FX7pSRDT2Bb5K-k7RSE6z4ukWMvqaQg5gnX2BTZT1mShYIM3d67ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمیییییی
: قرارداد لوکا مودریچ با میلان به مدت یک‌فصل دیگر تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101683" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101682">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xmz5KaMC4RUluS15aEwXOotK7l2_fp8bqX_CnBK3nSdk4FE0n6IBqkQNUIOtQfKYtD0o3MSK7TolWCYdyvIJMMy4TKmSsjVWnc137SPlZvK5Oy1s7ockDjJsIVt8RRJNuOEvKMHzTEaQ5pFz3oawT-8Le641dM0KbbryS1PLyJ346js5g4a2lWmXsuuYSbAcoOyN_7s28p2HJAMrWWLNup1zwCjW0Xp5gmSkN2t9FCCTdWXdtig8-2NKPQHolmURNPyegzAYl9yCFTASZRdySujMyH0nyJN0cTD6PUjzasp7b18g-Y4et5tUqOIEuXpxdP5b4ZE_ZmrHKLyKlchDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101682" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=TEiluhMeDTM5miI2rf4ui6GfCGUulWAe3Bj6CbTdNXMWisSw3TwfCZT6E78ju_ZbnZU0Wg3oeXNOyr8KnrhALjn08uubRZkrmLFF2Zjh9kmo6NmdBtzlVFedG8x1D1IUoQV9SWfQv-XoKTWQmUNxyQ9uWcjTE80tO69dWrJfLjmxT3h2tOKVSy9XWgXHnLNVJOdOTq_N8lJdIm_Z8an28DrF6k8Zb9I5c99yIFnuOXABjm9HA5Jg-0cIkSClWbHd_VtHNMs16s_p5762K5xCKWzVTlPGm5W33LkJGNVg6LmaP6UROMJyZl7DjMS3mf8fDHwhhuZunxQX7eFEbNL6Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=TEiluhMeDTM5miI2rf4ui6GfCGUulWAe3Bj6CbTdNXMWisSw3TwfCZT6E78ju_ZbnZU0Wg3oeXNOyr8KnrhALjn08uubRZkrmLFF2Zjh9kmo6NmdBtzlVFedG8x1D1IUoQV9SWfQv-XoKTWQmUNxyQ9uWcjTE80tO69dWrJfLjmxT3h2tOKVSy9XWgXHnLNVJOdOTq_N8lJdIm_Z8an28DrF6k8Zb9I5c99yIFnuOXABjm9HA5Jg-0cIkSClWbHd_VtHNMs16s_p5762K5xCKWzVTlPGm5W33LkJGNVg6LmaP6UROMJyZl7DjMS3mf8fDHwhhuZunxQX7eFEbNL6Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سوال: آیا مسی بهترین بازیکن تاریخ است؟
🇮🇱
نتانیاهو: باید بگویم، در کنار پله. اما در دوران ما و در دهه‌های اخیر قطعا مسی. او چند سال پیش به اسرائیل سفر کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101681" target="_blank">📅 19:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
فوووری ترامپ: من در حال بررسی یک حمله گسترده هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام داده‌ایم. به تصمیم‌گیری نزدیک شده‌ام. ما برای انجام آن کاملاً آماده هستیم.
اگر از اسرائیل بخواهم، ظرف دو دقیقه به این عملیات ملحق خواهد شد. ایران به اندازه کافی احساس درد نکرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101680" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101679">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=oFI4BIkfD2_eqC-eRl7E6nRJFYJmoRb1KZ9RFA6yBE0QhwqiVy4G9tH7nPR02DZI_-4Ww3kz_NkgcHTzSGHivNsMxyYR_IqTvw-wxYG1aBavRKJrcGP0MiTcinDPbo1n2ovWjWkFib315GhgsswU1oZHH0zvA3uJ4wjizOahP3YGH7BKx294UaeMXLPbxDURHz7Mw0-5HIHrQnbA2N9p0IUUsfOtdeabRIMZvMMFWCYpkBg3jjvAuV4o8Znu0jnGmwo19anMlqEQyXY7k2MBB8xl1141_7dm3puAwWOJtOZ7hUARGhOTEnIuZRGc987GxA1mYR7SleedAwMjqmaBBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=oFI4BIkfD2_eqC-eRl7E6nRJFYJmoRb1KZ9RFA6yBE0QhwqiVy4G9tH7nPR02DZI_-4Ww3kz_NkgcHTzSGHivNsMxyYR_IqTvw-wxYG1aBavRKJrcGP0MiTcinDPbo1n2ovWjWkFib315GhgsswU1oZHH0zvA3uJ4wjizOahP3YGH7BKx294UaeMXLPbxDURHz7Mw0-5HIHrQnbA2N9p0IUUsfOtdeabRIMZvMMFWCYpkBg3jjvAuV4o8Znu0jnGmwo19anMlqEQyXY7k2MBB8xl1141_7dm3puAwWOJtOZ7hUARGhOTEnIuZRGc987GxA1mYR7SleedAwMjqmaBBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تنها جمله درست گفته شده از صداوسیما در سال جاری خطاب به امیرحسین ثابتی: ‏مگه تنگه هرمز مال ننت بوده که بدیم بره:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101679" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101677">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atRhupBRR8Y5G-LJgFW89ryYJfNqbP1KTK5rUsNMET6yRW7eCjk0KkE-OENjA6FgYCTghfiFpveuP6PrdAOVvpJ7_6s9p6IpRtv_cHk7leuMzOLtgxkXLm3ukMLqjEcoLSykaZUIwp31wZjDz-ZfZh6P0aaJ4Z1b1Y0M5DlHZdg64J8MaE9hZj0NCJQPnVHS9xV_TWNlgy04MmiUgWKfKqjuX1dYJwShIpP5mW7-G7alTASrO_7pa3Y1M6svHb3u1a7AoP-dWGZejsxziRlB6ZNBgSd0VeZlDnTZbvZ4VQZ31h4O5C4eRui7W9s21_CzDB94n4p4m712Ae8o1TE51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzFZaAs3L73FLTc__18x9rvqqKa21Im2I8rrMln-DPYbV2umA9YDpfACqJXI-051ptLE5nTeaGxa4B9mpVQgcccT7m5Ib-XMta2_xwBepMurl2Z-NXfwHJlLo_uvru2QFJI_jk4vkeozGVhDmLY44ELhbeqhzP3vDXDCL3390vnaCKI_GluookJHqWP_2aiwPR6AcBax5H31LlPxjCiPyAuKjEENsD-howGThE6Ygh7wIg4dE49BqWsbomi2iaFHH2upPLCMm4brA4h7mYvOH1zwNCNaXCLgxdL5Oywgk3Bs0-YgpTUVquZd6aAaiKSYQ0lUSQtTlGwaWgdwk-QYdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تبلیغات جورجینا واسه برند خودش Mimoa
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101677" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101676">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btFqSpFXFOL29-10pIxYfuU0hCO0w9sFDdg8CGkk4Px_O3HYDQd5vg9MVo8j0KCY9IbL5ftqTCWpWoQtDbEsDhIbxnrqHMw-wplxOu2RFEW5yS4_xyLN7-W7-YjkUTXokDFC5T-SexGQkQ9oxGNR2Wvk52k0Zerx16AnySb3mV4qKgFJSJoBdyHNu9NMT-BeaSI2Kf4-oSnfhfXkoUPerkRi8MR4WIBkaukZ2YphDlQdzGxpxwqH_dgXK5iAzyZmht4-ZjegTHap2VI5vOkGe9P1sZ6czHKIfeZUaPMePN_RSUuCDDwcSYpQM15mvooY2NJxhskNmOJgxi2wQ91PxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
منتخب بازیکنان آزاد فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101676" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101675">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d6746099.mp4?token=D42yuY-8XSp9s_gpCw_sLB5WhKkpcbKRlMeglc8pgfxMHvNCUBnuquaWc_zrdeiui8c3Kw0b4Oq5aTX7s39-n5Px9dqgpdJspGpd3YYoE2qHAEGymh5yMx85ayONlFHvXznmqIZOAD49_nWCQRXn7hTrAA8ewyY8WzPeUJSFdke0qlIg1Plt8V2pvVPcnYFMss0iWXJ3y0CTy9gnqDNrtvs2SY8Hzx9OHsYU2g_DbvFOo4MUIUcI9jCN3Qo1Oxr8_Hy-DOh5r2ihguvVzjRafhn23Z9L_gQmNGVrOkFaZCwwQr5wyxYJV8M9XRuFXEkC7T6iM0iWbYdJvXcF3dtQ2DJ4vRKc0wFnkaVn-xtkUfu1781i7fI5CqcpebQSINpbYcJm0ViwyTVvAplH4AEVKFVkckg7vHvif42Q_Ze_9vZVqAsmnk8FrHq-IG4cZ1WkdI5Zy-9SLS91QqKFShWs5MGrfKjuxp_mD5uAqagkyZA6PoXWGYpTJck9dC94sHLZmkrkgGVyQx7EyxP1j5o9btDLk_o1k9hc6L0IL0UpxRSVImq8fD25andVZypZ5CgqB1mPgU4NJ8-dnqnvkP8bQ4IRm_Sq2cJ1AFbqAZQO0gGUbO9s8GPbOhZ-yP8JvLWiZf8hmjrL8L24EAkdbhxCxOMbYcUlqD49tfaTmlFqwcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d6746099.mp4?token=D42yuY-8XSp9s_gpCw_sLB5WhKkpcbKRlMeglc8pgfxMHvNCUBnuquaWc_zrdeiui8c3Kw0b4Oq5aTX7s39-n5Px9dqgpdJspGpd3YYoE2qHAEGymh5yMx85ayONlFHvXznmqIZOAD49_nWCQRXn7hTrAA8ewyY8WzPeUJSFdke0qlIg1Plt8V2pvVPcnYFMss0iWXJ3y0CTy9gnqDNrtvs2SY8Hzx9OHsYU2g_DbvFOo4MUIUcI9jCN3Qo1Oxr8_Hy-DOh5r2ihguvVzjRafhn23Z9L_gQmNGVrOkFaZCwwQr5wyxYJV8M9XRuFXEkC7T6iM0iWbYdJvXcF3dtQ2DJ4vRKc0wFnkaVn-xtkUfu1781i7fI5CqcpebQSINpbYcJm0ViwyTVvAplH4AEVKFVkckg7vHvif42Q_Ze_9vZVqAsmnk8FrHq-IG4cZ1WkdI5Zy-9SLS91QqKFShWs5MGrfKjuxp_mD5uAqagkyZA6PoXWGYpTJck9dC94sHLZmkrkgGVyQx7EyxP1j5o9btDLk_o1k9hc6L0IL0UpxRSVImq8fD25andVZypZ5CgqB1mPgU4NJ8-dnqnvkP8bQ4IRm_Sq2cJ1AFbqAZQO0gGUbO9s8GPbOhZ-yP8JvLWiZf8hmjrL8L24EAkdbhxCxOMbYcUlqD49tfaTmlFqwcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ویرجیل فن‌دایک مقابل بازیکنان بزرگ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101675" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101674">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=BWEksHkJKtUM3EkLs7csNNJ35UbCxDUsTCXDBtgwQfgj4VGJRoJdWYhc9r4pB1hDvpXJAJ6dEBpvFhT8FRvjqu2d45lO-sEJkqD5EwTNJqBTQriBR3aSUWGlgur5Qr0yhGngPwSiLTwXUSbpAPLVNLIWOkyX_85A8BXtUv49XEUU4M-9sDnjEHjM2ZCwzy3sML_KYTdV101n1MbCdK2eJDsKNaw0shTa0rsB2U3CNhCyeD3GzHdEnw7adDwqVoTB5Ib5_hi3J2q_2jIV-TDirIj95oar6CqiFRsmyPG1CAThqOMf44kRa9Hly_iMc4oBc57dofs7WxumKsfZeNC03A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=BWEksHkJKtUM3EkLs7csNNJ35UbCxDUsTCXDBtgwQfgj4VGJRoJdWYhc9r4pB1hDvpXJAJ6dEBpvFhT8FRvjqu2d45lO-sEJkqD5EwTNJqBTQriBR3aSUWGlgur5Qr0yhGngPwSiLTwXUSbpAPLVNLIWOkyX_85A8BXtUv49XEUU4M-9sDnjEHjM2ZCwzy3sML_KYTdV101n1MbCdK2eJDsKNaw0shTa0rsB2U3CNhCyeD3GzHdEnw7adDwqVoTB5Ib5_hi3J2q_2jIV-TDirIj95oar6CqiFRsmyPG1CAThqOMf44kRa9Hly_iMc4oBc57dofs7WxumKsfZeNC03A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
داستان دختربازی افشین قطبی
😂
😐
محمدرضا مامانی، بازیکن پرسپولیس در دهه ۸۰ با یه دختره دوست بوده، افشین قطبی خبر نداشته از رابطه‌شون، قطبی به دختره شماره میده، دختره به مامانی میگه، بعد نیکبخت کثافت‌کاری میکرده و چاق شده بوده میخواستن بهش گیر بدن، این با آتویی که از قطبی گرفته بوده گروکشی میکنه
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101674" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101673">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RyfTUKBmqK8Clx2fQueQugKySoW2psDJLzxMpqtghUo1LJjMtU9fozwz9vuc1toC0UKE8m4TnQKAWSM8TsorOAU_IwtyR81CILb_YXOC9gvEtoQmNBiv0CSxvOKvMkpLSdeMSc_sSsX0D7jCmPAQXbHhHLI5mFzkrdn3DfZDsgY25mVJWPaUtypTgMpHKbRF3jDOJVvcULYg3xEyflyYw8NLrZVZrD8WMpyOTkJZpW7Oa1Bp5ozJqA6EimPGGLdw7meeCFatIL1vybP_Jx4DPe1Vyrmy8Kl7t_IusnrItT3EGPbdXDaahMkDYHVfteFB3RYfLviS1eOEhMsmT7B1ypqVhpjlBcZDys6mP5sHHm2gf6NSeNCxqpakIIEcLxMvyrpV-EZCvr1GNFNIfVSghIJBYCjaW785B65xIugeuMVTIjXB95ooRo5tpJ54gs-uis7Y_KuJMx5HSlIY8fSdd7Ej3fbl_dTqr-MOW9aCEtzFvsxL652HbOn92tisiXE_l-mUT_m8cREf0uzXvJJMW8bAPwDrrg5K1pHECVMSdEA3xA2xFOjU4FOHG9SHJiZmB65s2zhFLZsQZiEouJs11acyPPkvrnA4airvWlfEyFbd69835UGUeXj_a4lS6aQyRcHnhWlvakErm7eUdEoMXUuXP0pRe596itDkWxTpz3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RyfTUKBmqK8Clx2fQueQugKySoW2psDJLzxMpqtghUo1LJjMtU9fozwz9vuc1toC0UKE8m4TnQKAWSM8TsorOAU_IwtyR81CILb_YXOC9gvEtoQmNBiv0CSxvOKvMkpLSdeMSc_sSsX0D7jCmPAQXbHhHLI5mFzkrdn3DfZDsgY25mVJWPaUtypTgMpHKbRF3jDOJVvcULYg3xEyflyYw8NLrZVZrD8WMpyOTkJZpW7Oa1Bp5ozJqA6EimPGGLdw7meeCFatIL1vybP_Jx4DPe1Vyrmy8Kl7t_IusnrItT3EGPbdXDaahMkDYHVfteFB3RYfLviS1eOEhMsmT7B1ypqVhpjlBcZDys6mP5sHHm2gf6NSeNCxqpakIIEcLxMvyrpV-EZCvr1GNFNIfVSghIJBYCjaW785B65xIugeuMVTIjXB95ooRo5tpJ54gs-uis7Y_KuJMx5HSlIY8fSdd7Ej3fbl_dTqr-MOW9aCEtzFvsxL652HbOn92tisiXE_l-mUT_m8cREf0uzXvJJMW8bAPwDrrg5K1pHECVMSdEA3xA2xFOjU4FOHG9SHJiZmB65s2zhFLZsQZiEouJs11acyPPkvrnA4airvWlfEyFbd69835UGUeXj_a4lS6aQyRcHnhWlvakErm7eUdEoMXUuXP0pRe596itDkWxTpz3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایت عادل فردوسی پور از الکس فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101673" target="_blank">📅 18:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101672">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGsQCLY9wkyT5JdcqGNxOZCogcUB7YYsKN3GgPxC1Uuv7W9DgOhAbKxjoif5NXCnSZoeUWYcK6z15C_B6FW2U7dhDsRtHwcId9p4RKTP-cpM6JTx2dATLjIwooNSqtFk3OgSTzEbVk0pQJbqfjcR9E5DFND7nHcwAdmN0-TdFFasvBDehTEJV3FiPMUq5Lr-wTLkm60PkBDryf23HRy_XYa66EnwbVgyl2lC2ochsXJLazr1aPdcjHBfd2jkqK8c4ogdWnpgovBI0ePG5iCNN8JVjLH9Hut0_a5X8M5wrEQ5fiQl8fvBXGcg_2ANuDMlAtoWXLTXDjdgM4c0mzE-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180
؛ باشگاه نساجی مازندران با ارائه پیشنهادی خواستار جذب محمد خلیفه به صورت قرضی به مدت نیم فصل از استقلال شد. این درخواست از سوی مجتبی‌حسینی به شهاب‌زندی مدیرعامل این تیم منتقل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101672" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101671">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815514f088.mp4?token=JDaluSOVRvv2hb_AR99XYfcBWz7yNvUwxrjGMCp0zZGt_BQLkAI8wm8ivHAm9M3IICHowSaHijOb49yeH6IF4uBkH9KUcvwHTlzh1PYWd2MoAYeV2nAmORVS2h1Bdz0Zx_o5FhmEJMZxApxPQlGvojNCcN_p2oNvAqdxnpOkMXCd3ldglk-GD8p72dnvKzk5y1JPyt9AxlufIwI7R9VAkMNJA7uN-55NkhqW92-bNITs5ta2WkluB9zGeHnpN__hM_I3yHBVP575q-WvDzrEEgEx8OurcSEqTyY0eMidK0EeEmMf_imuR3_iZl3oVCOaLLISmjeGOJF3U5JtGP9knw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815514f088.mp4?token=JDaluSOVRvv2hb_AR99XYfcBWz7yNvUwxrjGMCp0zZGt_BQLkAI8wm8ivHAm9M3IICHowSaHijOb49yeH6IF4uBkH9KUcvwHTlzh1PYWd2MoAYeV2nAmORVS2h1Bdz0Zx_o5FhmEJMZxApxPQlGvojNCcN_p2oNvAqdxnpOkMXCd3ldglk-GD8p72dnvKzk5y1JPyt9AxlufIwI7R9VAkMNJA7uN-55NkhqW92-bNITs5ta2WkluB9zGeHnpN__hM_I3yHBVP575q-WvDzrEEgEx8OurcSEqTyY0eMidK0EeEmMf_imuR3_iZl3oVCOaLLISmjeGOJF3U5JtGP9knw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مارک کوکوریا موهای بلندش را فقط به خاطر استایلش نگه نداشته است. پسر بزرگ او، «ماتئو»، مبتلا به اوتیسم است و در تشخیص چهره‌ها مشکل دارد. کوکوریا می‌گوید موهای بلندش کمک میکند پسرش هنگام تماشای مسابقه بتواند او را راحت‌تر بین ۲۲ بازیکن پیدا کند. به همین دلیل هم قصد ندارد موهایش را کوتاه کند؛ چون برای پسرش فقط یک مدل مو نیست، بلکه نشانه‌ای است که باعث می‌شود پدرش را گم نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101671" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
