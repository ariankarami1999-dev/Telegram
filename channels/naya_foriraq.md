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
<img src="https://cdn4.telesco.pe/file/L52z560azY1ZursWYVgExhucrSVSWcBV_kxTpCgQrmBYV3nV9Iilrvo6P6Pv53Z3PlhdUKCXTAiZCsby3GlKRrssZtTnjgUbAI9L-nQgeuMYT-LiSF_s01wOpnE-nhgKvX4S5BeRL5K0JH3Ls38_nbui-0cK6fyD1orGfWZhvp6ZIWied2HtQlPbQ9uGLsCQYly3UsMGFWmxfqQqWEcTSL5pXFuE_LOhP0kU6RxXOkGG8Vnq8ePi41ZrRmeD6P8JKC71Ymd9uuTI0Ic8Kgvx5l5GxiQzneLRyniJ4IDHqh4LIaP6peD4UDthLtt7XJYRbZFgM-9JXLc8Hp9baSGNCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 01:19:54</div>
<hr>

<div class="tg-post" id="msg-76179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇷🇺
مبعوث روسيا لدى الأمم المتحدة، إلى دول الخليج بشأن إيران:
أنتم رهائن للسياسة الأمريكية في الشرق الأوسط. كنا نقول منذ وقت طويل إنه إذا حدث شيء من هذا القبيل، فستدخلون حتمًا في هذه الأزمة سواء أردتم ذلك أم لا.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/naya_foriraq/76179" target="_blank">📅 00:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urnnVD2l4SfffUgsuLlFxpLF36gpR6Ahj4156bnyZuUtMi7xNDk8UdFCbjnOhxbYUK5pyMTfTYindRXnZqyaZw79cd6KIWZp2Ann3i6vFOiHZtC4jTfYDOrwbVrwTa2nw5HgemJV3wR81YrGYtkubYLgpRhrB6Ru0tJ1442AK-JbovYSTeb70K0quk5xy1Ei2Zl97isau94ljqX1XrIDUbSQqjgY11BPtRruFiOKYnR3X1VRSwvLDlfcOpOT2TqV1WpHzqjjBla_nrhFwETZZD_um0k3D2YpOahSeXnfmTtf1OIneHOqG4krmBEkrRjNzQk6blmFQFHmqOjkTCZiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يبدو بسبب غلاء اسعار الاتصالات
ترامب يعلن عن الاجتماع القادم في البيت الأبيض بواسطة تغريدة</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/naya_foriraq/76178" target="_blank">📅 00:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76177">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">▫️
🇺🇸
قال سفير روسيا لدى الأمم المتحدة إن الولايات المتحدة رفضت منح تأشيرة دخول لنائب وزير الخارجية ألكسندر إليموف قبل جلسة مجلس الأمن التابع للأمم المتحدة، واصفاً ذلك بأنه انتهاك لالتزامات واشنطن بموجب ميثاق الأمم المتحدة.</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/naya_foriraq/76177" target="_blank">📅 00:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76176">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 26-05-2026 آلية هامر تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/naya_foriraq/76176" target="_blank">📅 00:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76175">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
26-05-2026
آلية هامر تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/naya_foriraq/76175" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76174">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_j_2jc0kIE0GoJJ0Xm_e_phaJT1eUL34Gy1bt5k-BeEsJx4Y2armxjEhXbAV3bBmNm_tQolZUaR9JO9HuH6qACN4g84QNIpY2jnCjv_gTdMsR-PEWp9v6-RJG6nLONsYBnK1y8FsYqVWS9Eow667YFKv9FbwPIP_Yoo_4BVdXBKLnwaD-ZbPWt6vRJiWdc26O0nGEe_-yub12NNTVcDtAREfTMrD4OFp8jL8zdPk43ESRDeaOwWdf5gI1Plmvw-743iAbA8qLX26U2D70loz8JkRs0--i5lA6SZb3eg67MEQgBYXNbfVL_9D91_oytpf9kM2PoQcw-tOjJcocOIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إذا استسلمت إيران، واعترفت بأن بحريتها قد ذهبت وتسترحت في قاع البحر، وأن قواتها الجوية لم تعد معنا، وإذا خرج جيشها بأكمله من طهران، ملقين أسلحتهم ورافعين أيديهم عالياً، ويصرخون جميعاً "أستسلم، أستسلم" بينما يلوحون بعنف بالعلم الأبيض التمثيلي، وإذا وقع قادتها المتبقون جميعاً على "وثائق الاستسلام" الضرورية، واعترفوا بهزيمتهم أمام القوة العظيمة والمذهلة للولايات المتحدة الأمريكية، فإن صحيفة نيويورك تايمز الفاشلة، وصحيفة واشنطن بوست، وشبكة CNN الفاسدة وغير ذات أهمية الآن، وجميع أعضاء وسائل الإعلام المزيفة الأخرى، سيقومون بتغطية عناوين الأخبار بأن إيران حققت انتصاراً رائعاً وذكياً على الولايات المتحدة الأمريكية، ولم يكن الأمر قريباً حتى. لقد ضل الديمقراطيون ووسائل الإعلام طريقهم تماماً. لقد أصبحوا مجانين تماماً!!!</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76174" target="_blank">📅 23:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76173">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
إنفجار خزان مواد كيميائية في واشنطن أدى إلى سقوط عدد من القتلى وإصابات بحالة حرجة.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76173" target="_blank">📅 22:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76172">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135333f897.mp4?token=C-eR-YBWyCG5Ojeqc_ZGp5-flbvXXVAeGO3Y_0FwfFbBx1hMaCJDVMn5PWslzAHsO3JFtyj0Lqqx5X0MlCbJPH4-dJcl4MFlVSvo_b2nl6VfC7P3x_LzxiT-d8Ogb9oKjkCJIJTNQ6qsmq-JBrwN_2AH4ftmkkNanTHb-RyvEesy-CsM2WgCXNDvFvRpi-SBChXr0_RkVmupofFaOTUJFlDfXynzvZuGRD_K6z2ogUlfvG-2CjBqwVmS8lg97CcF0hcqoD1wwKg7m_6wvHgYpqoEKWD3nSRp1y57-twIpZ74snrUWQQ1fvef86DUQ3RQOfj0TFZ3GlJg9PXrzsUjxV6KqGM3qVQ_Ru7z9MJTLSzDkMtponnrCt9kvlX0W93lAnLleZYuyf5tIz1TeTFhm8j2ymAM-Y-qSzozAb630XD1mJB1QPJKbByAvUpT4GcFGGwW21_h0UeISSZLswbrLviz5qjCQbPfHcpYMo2uNTQZ9c5bQpaQtZkq9u9sDy2C8WKCRGoBcT5EAhAvre2TiwpsbFbRsKRG-KOt55gQbKqjO8g70IoXj-YBF7-iEx7q-5Di8IDjhn8bAkFTemRl7U1auYr6HcwvRpwDRVYQAdLy9Sjunq-maTh4DuZT2ifM-LmIKuDUcGC0Zqr27wv9Zc9N6K9ovT5NPmbGpFK_gY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135333f897.mp4?token=C-eR-YBWyCG5Ojeqc_ZGp5-flbvXXVAeGO3Y_0FwfFbBx1hMaCJDVMn5PWslzAHsO3JFtyj0Lqqx5X0MlCbJPH4-dJcl4MFlVSvo_b2nl6VfC7P3x_LzxiT-d8Ogb9oKjkCJIJTNQ6qsmq-JBrwN_2AH4ftmkkNanTHb-RyvEesy-CsM2WgCXNDvFvRpi-SBChXr0_RkVmupofFaOTUJFlDfXynzvZuGRD_K6z2ogUlfvG-2CjBqwVmS8lg97CcF0hcqoD1wwKg7m_6wvHgYpqoEKWD3nSRp1y57-twIpZ74snrUWQQ1fvef86DUQ3RQOfj0TFZ3GlJg9PXrzsUjxV6KqGM3qVQ_Ru7z9MJTLSzDkMtponnrCt9kvlX0W93lAnLleZYuyf5tIz1TeTFhm8j2ymAM-Y-qSzozAb630XD1mJB1QPJKbByAvUpT4GcFGGwW21_h0UeISSZLswbrLviz5qjCQbPfHcpYMo2uNTQZ9c5bQpaQtZkq9u9sDy2C8WKCRGoBcT5EAhAvre2TiwpsbFbRsKRG-KOt55gQbKqjO8g70IoXj-YBF7-iEx7q-5Di8IDjhn8bAkFTemRl7U1auYr6HcwvRpwDRVYQAdLy9Sjunq-maTh4DuZT2ifM-LmIKuDUcGC0Zqr27wv9Zc9N6K9ovT5NPmbGpFK_gY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد لإستهداف واسقاط مسيرة أمريكية من طراز MQ9 في سماء الخليج الفارسي ليلة البارحة بواسطة الدفاعات الجوية الإيرانية.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76172" target="_blank">📅 22:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76170">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/omODEh3e74-cWwjJbtg_1ofeYYFSll__5oLHvbZ9oa2MpN2UhRRyYZMx9e3bh8OhnW6vEAq2JzI12-J1VDj6eAPrufGwubL6oKInE3E8rITSitNO-0GskHTrL5PILNX-qHjDzulKbqjXDoFH5Y7RgB_QIJ8fAk0o4h3DX5xM7kC5LMahHCtoJ9tHW-PX09_rjfVKy_TZzW7sQFbmsjflvfr8Pwtp3PCN18AhPbfmxjD8Jr-j-TYgfLJUb6LyK3BQ4HXobA7bYrnKU3t3X6KQg_7vmL9B5UQncS9AH_btKI3WDejmskHCccmqOdh8yHvCKYOedrHS8VsGNT4V9rUd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbGM3I8ZqjW4O8OGWbjX6bIk4W4frmr5EsKSZMeH8Tai9PC-HO53gxXGGr5PI7skXS2GXwjJsaAkt7PKbQKEEBr1D67cZfLCg7Lu0MGfU54ypasg4Hv4ThAKGS093BqY5Xzf0Ec_fJfZWf_l7TqEzgVBaZse7JgDgAjENI4KwUXIbjXRwIBGrLVIEWp_0cqAq6fheipE7fh2p8hAYNjHqyXkQ0qDqLLgA5jiohuUNvjxO_lJCwpLa1Hd0g1vLTCbaotxavnOU5pzuPdDlYou1X3lN93Wai8t_NSvEO-y1Bg6jiMgR0lUFCA7YoEPR0P3uORtDZG5i67jILCDXIf9Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
توثيق يظهر نظام الدفاع الجوي قصير المدى AD-08 Majid الإيراني، والذي تم عرضه خلال تدريبات ييريفان في 25 مايو في أرمينيا.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/76170" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76169">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11425cc9b7.mp4?token=iXfvHGR_RoSMKzLrQjQFzSqCzGVKKUMlMb9Q1pXetXuRG0efds6PE4UqiZUALbJ3SgBRVizH7q0ohoT1tdpQJTYeGZFTV1c3BPx76HPjQEo4CMRMJGKQqITgs9gYMSEisfppPGYd9YXE9WRsIwPgCRtX4md3EpU_IEwt6pZ7XGhtKXDcrgYnV2oXyqoXcYEDmf36IRHtXSKb8OS9VWRgwQ2jIb81ex6HkCEgEomIkcTOxN4kWZKKqM9dkZggoF-otLrY9eG4tD-O-p3du-XJ0rjJQ9QUBKtkFpbGDiI3I1urHWjU9YasG3zcNj767tbkCVk0dZcSZjf2Z_Hcuxu0CoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11425cc9b7.mp4?token=iXfvHGR_RoSMKzLrQjQFzSqCzGVKKUMlMb9Q1pXetXuRG0efds6PE4UqiZUALbJ3SgBRVizH7q0ohoT1tdpQJTYeGZFTV1c3BPx76HPjQEo4CMRMJGKQqITgs9gYMSEisfppPGYd9YXE9WRsIwPgCRtX4md3EpU_IEwt6pZ7XGhtKXDcrgYnV2oXyqoXcYEDmf36IRHtXSKb8OS9VWRgwQ2jIb81ex6HkCEgEomIkcTOxN4kWZKKqM9dkZggoF-otLrY9eG4tD-O-p3du-XJ0rjJQ9QUBKtkFpbGDiI3I1urHWjU9YasG3zcNj767tbkCVk0dZcSZjf2Z_Hcuxu0CoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد لإستهداف واسقاط مسيرة أمريكية من طراز MQ9 في سماء الخليج الفارسي ليلة البارحة بواسطة الدفاعات الجوية الإيرانية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/76169" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76168">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89068e1197.mp4?token=hbgliVxSmQMAz6oYrpWO_hk4Hn2qzKyXxHzaGFhFT43mfbD7XXsYys39bZUz2Y4JwPUx3N4w7cqFKpQKieyAXjM8dHlIjED59aDN-9K6T51suJX4xi0GYRSJWp0U2MzxyMtNH_v1blZfPkf4sNiHszuOclLevuja_EeE1wuJAw0HSTeSxeA-Aj6huEeL6vwzuxPcsYKDlkX-kQRQH2jzX9qt0piKkavKDIKjzqfPHYewdSgmNHA9NTplqoSD9hWhdNqVGnAebO-eZsQqvHDfmEtxjIHZRxtR41AUWTicfVOEvFbykr0uPzlC0pLuBti-50Nivax-NdeUnfacp8n3Fo4lL4QomogaGJ86iG9W7dL9pm5Kymqn0c__YzbsHMvTP3nQ-qzqR1YFfzBpKp2SAlliQnTBNuaay8ToLE0RolSIFq77aIzVsto0eGNkI8qMssRr-wT2W9aA38d4VJ0C_3-2aVhwyUMhPKGyMPIiFgbcIXwv8jVCj-r4Ab75aA3PfDHyuv8eSTcl6eNRCtuR13YWAHLR6M2_euL70Gq11K_84FryRd5ZoXTTX77dVBrhbuu7Ite--mpHNrZINxZOU8ga1ImviYkIDp0-iK9J9h3jGGridf_X5PEHzhTFHy_wT2AhXnik63KjZnJ7r3O4u3c9tMsilVDOmcYbqjdVe-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89068e1197.mp4?token=hbgliVxSmQMAz6oYrpWO_hk4Hn2qzKyXxHzaGFhFT43mfbD7XXsYys39bZUz2Y4JwPUx3N4w7cqFKpQKieyAXjM8dHlIjED59aDN-9K6T51suJX4xi0GYRSJWp0U2MzxyMtNH_v1blZfPkf4sNiHszuOclLevuja_EeE1wuJAw0HSTeSxeA-Aj6huEeL6vwzuxPcsYKDlkX-kQRQH2jzX9qt0piKkavKDIKjzqfPHYewdSgmNHA9NTplqoSD9hWhdNqVGnAebO-eZsQqvHDfmEtxjIHZRxtR41AUWTicfVOEvFbykr0uPzlC0pLuBti-50Nivax-NdeUnfacp8n3Fo4lL4QomogaGJ86iG9W7dL9pm5Kymqn0c__YzbsHMvTP3nQ-qzqR1YFfzBpKp2SAlliQnTBNuaay8ToLE0RolSIFq77aIzVsto0eGNkI8qMssRr-wT2W9aA38d4VJ0C_3-2aVhwyUMhPKGyMPIiFgbcIXwv8jVCj-r4Ab75aA3PfDHyuv8eSTcl6eNRCtuR13YWAHLR6M2_euL70Gq11K_84FryRd5ZoXTTX77dVBrhbuu7Ite--mpHNrZINxZOU8ga1ImviYkIDp0-iK9J9h3jGGridf_X5PEHzhTFHy_wT2AhXnik63KjZnJ7r3O4u3c9tMsilVDOmcYbqjdVe-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تظهر لقطات جزء من هجوم حزب الله يوم أمس في منطقة شوميراه بالجليل الغربي بواسطة محلّقات مفخخة.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/76168" target="_blank">📅 22:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76167">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799bcc6b46.mp4?token=llT6fmkQvuAjsB2PR6hzhjRmLRspK2Ysmw0VqXX2soZtwCEIV4pMZSzc_QtIu3pYFSgZmEftAZM4JWyQJkMuMIT_IFW4zW4aRwgiAV9g5l3RaEGjwicka_P_cNwJrS88yhiRcR67XSomFcnUxrFRLQjYDuAbuiH2UXkGG8REQ0wtMBcxRjb5DJD0lWcomfvRzoLWeJvjIKRdij9EwuqCtmTlGwyu3jzxmbINWTB31C7mBXgCjEEG0laPSSBhkkXfBgPtrQ-AtR0yzib3YUW-6BCHyZzSWv-SQ3RZR-tEiFfsfeD0THsxPGvJhnOq6QNnIWxjko6_yUS7VniwbzdRGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799bcc6b46.mp4?token=llT6fmkQvuAjsB2PR6hzhjRmLRspK2Ysmw0VqXX2soZtwCEIV4pMZSzc_QtIu3pYFSgZmEftAZM4JWyQJkMuMIT_IFW4zW4aRwgiAV9g5l3RaEGjwicka_P_cNwJrS88yhiRcR67XSomFcnUxrFRLQjYDuAbuiH2UXkGG8REQ0wtMBcxRjb5DJD0lWcomfvRzoLWeJvjIKRdij9EwuqCtmTlGwyu3jzxmbINWTB31C7mBXgCjEEG0laPSSBhkkXfBgPtrQ-AtR0yzib3YUW-6BCHyZzSWv-SQ3RZR-tEiFfsfeD0THsxPGvJhnOq6QNnIWxjko6_yUS7VniwbzdRGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان: لقد مدت إيران الإسلامية يد الأخوة إلى الدول الإسلامية، وفي الوقت نفسه لا تتردد في حماية أراضيها وسيادتها الوطنية.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76167" target="_blank">📅 21:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76166">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
إعلام العدو يزعم: تنفيذ عملية اغتيال القائد المعين للجناح العسكري لحماس "محمد عودة" في منطقة حي الرمال بقطاع غزة بواسطة غارة من الطيران الحربي الإسرائيلي.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/76166" target="_blank">📅 21:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76165">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌟
🏴‍☠️
دبابة ميركافا أخرى تابعة لجيش الإحتلال الإسرائيلي تم إستهدافها في بلدة زوطر الشرقية بجنوب لبنان.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76165" target="_blank">📅 21:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76164">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يستهدفون دبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة رشاف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/76164" target="_blank">📅 21:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76163">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce84f74f6.mp4?token=WouDaHm0h7konkt4xZhLrN6J7xgfzqpGH9OE6A5sO3dpmcJPr7F9K_UajUMSA6YMdJPMuAWLHSSHInXkMFAYYvauG60J9liizVi90DkfJ0oKDSnRvlKnE5mT9SCdKdojHq3X-LC8tIjdb3XJe4FvJ8Rv0poL2LpBeIs5l9so7lKRC5qLJMvv3afVuFJNclpisVXJ22v3RLND4f6WhjfiTsEVqyV175HBTZb9jU50CGs_W7tNfHZWJqMddE4_9ulE9NHBbhIHFCGotfM13y0piT0UKannxYufGLnElFcSzexivNIXobCGiTCMzM9UBnA_Y1T_LZ6IpvALUFwGlHvNyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce84f74f6.mp4?token=WouDaHm0h7konkt4xZhLrN6J7xgfzqpGH9OE6A5sO3dpmcJPr7F9K_UajUMSA6YMdJPMuAWLHSSHInXkMFAYYvauG60J9liizVi90DkfJ0oKDSnRvlKnE5mT9SCdKdojHq3X-LC8tIjdb3XJe4FvJ8Rv0poL2LpBeIs5l9so7lKRC5qLJMvv3afVuFJNclpisVXJ22v3RLND4f6WhjfiTsEVqyV175HBTZb9jU50CGs_W7tNfHZWJqMddE4_9ulE9NHBbhIHFCGotfM13y0piT0UKannxYufGLnElFcSzexivNIXobCGiTCMzM9UBnA_Y1T_LZ6IpvALUFwGlHvNyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو يزعم:
تنفيذ عملية اغتيال القائد المعين للجناح العسكري لحماس "محمد عودة" في منطقة حي الرمال بقطاع غزة بواسطة غارة من الطيران الحربي الإسرائيلي.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/76163" target="_blank">📅 21:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76162">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اشتباكات بين البحرية الإيرانية والقوات الأميركية سقطت عدد من الشهداء وهم كلا من   پاسدار شهید عباس اسلامی  پاسدار شهید قدرت زرنگاری پاسدارشهیدعبدالرضاگلزاری پاسدار شهید حسین ستوده....</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/76162" target="_blank">📅 21:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76159">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdeNdtcxf5YBv19_KY5VPjeoUtAKrlFVqoNZNj46Jew64Qyk6-GN7EqT3OKGZ14nDy6jhMIP1FaUJd8kKUj41ihTCqrurH0MzAcE8Qcu26FCm53f-OAF35w3YMk5Td8NQB8RayN1WTTI_Nx5uPl6N5ep584wppjElAlnNIRvyrOhtAhA07SHBUmr23ybjDmGEyouvOwctLXzrxWcg_VKd8TexJm5S1Of_q1TS6yBnMziCZq9YBScpA8F8H5y5GRdeKOqBWUR6gm0kGOCu4dVeCRKgOabuOj_9v173tx8cMqI_uQ2POswtjzpI4iClMOChi9WKO9LK_EEdlOvTMquKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ded70fc7.mp4?token=hgxcUJ-lD5cLGhemo1OK8CmVOlyidrHeK9XtoANBJZ3kcIUEIEmZC9SUzk3nnUrkVRtQR2i84f3rwsfrdUYqfeCbcBcxUJY8kzOZiOgY-T5elo9oZZqvdkdXvWpjcBcUwa6Dr_-f63q4ilR3gQJ0X46J0LohO3Vlb_XGAPqhlCtEZ8t2TuWdSmqNio0cSDeWHwRB2VZKvRuHRHlMWOkecLOuJX-c2u7n0P6Te0QgF0Vd6ykvHcWUMYPpaqGpK43iEm5CC_ni0JWmvtEfIdFW87FEzYX_wJoeYh6f4G9HwhOuFUjRA5TQEKJZk2aZJU4km08wbXbpx4I_O0SkP9YXZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ded70fc7.mp4?token=hgxcUJ-lD5cLGhemo1OK8CmVOlyidrHeK9XtoANBJZ3kcIUEIEmZC9SUzk3nnUrkVRtQR2i84f3rwsfrdUYqfeCbcBcxUJY8kzOZiOgY-T5elo9oZZqvdkdXvWpjcBcUwa6Dr_-f63q4ilR3gQJ0X46J0LohO3Vlb_XGAPqhlCtEZ8t2TuWdSmqNio0cSDeWHwRB2VZKvRuHRHlMWOkecLOuJX-c2u7n0P6Te0QgF0Vd6ykvHcWUMYPpaqGpK43iEm5CC_ni0JWmvtEfIdFW87FEzYX_wJoeYh6f4G9HwhOuFUjRA5TQEKJZk2aZJU4km08wbXbpx4I_O0SkP9YXZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
أنفجار عجلة بين حيفا وتل أبيب ،مقتل شخص بداخلها كحصيلة أولية ؛ وشرطة الإحتلال تعلن أن الخلفية والظروف قيد الفحص.</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/76159" target="_blank">📅 21:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76158">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f8e898fc0.mp4?token=mDze-yQ8v_xv8SkwoL_R4gY_uK9-AZKmJrsn1C7zThggrR4MxIrp61Zoxg7EUZCDcso61626GsVVAMaMKaY3G1A1NK1wQ17NiaS4lEY64MHBCgK8OC4ssq4jQJvkSkemwAsY1KLI1on_hSX_PkpnaZMzZYoNweEHVPDJ0Ad98rNFkfnN7M-EGnKsDml25hj6bV-t50UwCaljyMLgcGzqMKKh5nrIIonXNOqX0ejtoB-ZAfQ7Ezur3Pionb2eKvSw8rIheCvXlqrvOkcevqWhHHrn7jkv79zV4G8jKQCFpvfiBqJBFdRf8-2UbhuvvHcyF1bh9YxmwtN2zEhgnP9zXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f8e898fc0.mp4?token=mDze-yQ8v_xv8SkwoL_R4gY_uK9-AZKmJrsn1C7zThggrR4MxIrp61Zoxg7EUZCDcso61626GsVVAMaMKaY3G1A1NK1wQ17NiaS4lEY64MHBCgK8OC4ssq4jQJvkSkemwAsY1KLI1on_hSX_PkpnaZMzZYoNweEHVPDJ0Ad98rNFkfnN7M-EGnKsDml25hj6bV-t50UwCaljyMLgcGzqMKKh5nrIIonXNOqX0ejtoB-ZAfQ7Ezur3Pionb2eKvSw8rIheCvXlqrvOkcevqWhHHrn7jkv79zV4G8jKQCFpvfiBqJBFdRf8-2UbhuvvHcyF1bh9YxmwtN2zEhgnP9zXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
أنفجار عجلة بين حيفا وتل أبيب ،مقتل شخص بداخلها كحصيلة أولية ؛ وشرطة الإحتلال تعلن أن الخلفية والظروف قيد الفحص.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/76158" target="_blank">📅 21:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76157">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭐️
عقب فيضان نهر الفرات.. حكومة الجولاني تدعو لإخلاء فوري للمنازل والمحال القريبة من نهر الفرات في محافظتي دير الزور والرقة.</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/76157" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76154">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uXOyy1vw6mYHgGByoJCNL0K49qnvFJsdSx20zBJVJwtN1mh3ofl2nNqmoby62PuTPOTSO5xT1p-FZtqsamFt8Kbm6u41tO--57bGZtOM4SuJEQbfkyMqX2GP7e36HknMtXOVjuaD1sjGdtdcKHrkgqSbZHvsjs_RItyyxSKLL12d1vvKOPbcEUYex2DhD5_eY5pxE4JGoi3Xu8CMkz0N00RDmbOAES2hPLMI2p-NrGIJQmRqWEwSKhQh5lVaiXwWBKoX_ddR2bJOu1VUhmWxJAFFL2YfQ1eNt0I3gqJQ7e1Tez-nc-QIEUUuhwJGBVboF-LAr8NVuAoGBGWFRuU9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rX26-9nuMWO_XDS1TE7nnZAGSZIr5hZDsdno8iIsYCiFZ4E0PBCP-8aLuuKnbmLYO_27Kd9WazKIc2EoC9IqHy6_XGLM7SUU4NIrqnlJ9Zbt8A0WxWax_vrfsWEeu_D8lgOd9lVtPhIkUKPexkt_CLsKuDet_KR5keJHli0NWF6p4PgkxrmNfIrNd64TS427Qi49IgZpfsJEpk4oiR8oORg6hrb_Khx_yFaV29X4DmlFmqo6lkfZjhEO9V1wfhaxsBST1Scd-kCHTjn4Ku2r3efmzTGGQzDhvGMlmGJWbd1RFX-uimWEDmdNK6kZUe0W0jpZxat9_rf2Pn82OtxqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bk2DYFKsXOgVTC0GJursHVH2y8d6OJcSJTW-rdBZQc7HrwYL2HRqGJAKRIK6QkpTXFWzI6f8pNHUfuXoMi7uRzTAalypFBTiqLexE5bO6HGCWG0rPV6fpgOy23ABVyMJUq62NSfMzjKEMxCLyeHAstP9kYfVJOFt5WavCk0DQfmpva8uKhLKfwjjSet3IIS-ECwgM8MrRMO-p-1KdtGBri9YNuwbIftME3Z2E7P4Gl0dKSkAtSzm5Ik9WeDyq3BdpPa6GEp_VpbdSrEHCQhkBkveV-gS7oYXskFvcDcdV5WtiYxxLj-zGrwyQ2Q3_aSf612c_0hB5lh-syjC4TWUqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇶
إيران والعراق لايمكن الفراق..
برای دومین روز متوالی، خدمت رسانی و ایجاد فضایی امن برای زائران ایرانی که برای شرکت در روز عرفه به گذرگاه مرزی مهران مراجعه ميكنن ، توسط فرماندهی عملیات نیروهای حشد الشعبی در استان واسط، ادامه دارد. این کار به دستور مستقیم فرمانده عملیات واسط، آقای احمد خضیر المکصوصی، انجام شده و شامل تهیه غذا، تسهیل مراحل ورود زائران و ارائه پشتیبانی لازم برای انجام زیارت میباشد.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76154" target="_blank">📅 20:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76153">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
لقد مدت إيران الإسلامية يد الأخوة إلى الدول الإسلامية، وفي الوقت نفسه لا تتردد في حماية أراضيها وسيادتها الوطنية.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/76153" target="_blank">📅 20:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76152">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭐️
‏
القناة 14 العبرية:
تقديرات في إسرائيل بأن الاتفاق مع إيران سيشمل بشكل شبه مؤكد لبنان.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/76152" target="_blank">📅 20:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76151">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWH-FJxI1yw8lVIYCWP4SecUXmymhDPH8ZGrgcmphZwGzWjQjaobHsT4kCOqpiS4px5R-c3qU8g-_1TEq1oKu6wdqfuIAl8RhlYD6UYmUlwONJtoGCSRkRha25C_D7LFl1g-2WUZsnbqwFpybsWZn4zL7SiW3jPJ7sx-dH5XSDs8zJKvwXg5SCBq1WF_p38W00x1uee1BhakLRfe8dSz030CJP27HcpyE0f91z87KOBaGZs1STBfbhV-1-_8WxEyIn8fPxpaosXLyEfVvA1aQEjD33G_CnY5JVYMlQjx2Ij5wqzXaf8yBBLpNF3ZUEFVx8NPIdNiV8LWHAkOqNgX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ديدار مشاور امنیت ملی عراق "قاسم الاعرجی" در مسکو با معاون دبیرکل شورای امنیت ملی ایران "علی باقری".
در این دیدار، آخرین تحولات اوضاع منطقه و راه‌های حمایت از گفت‌وگو از طریق کانال‌های دیپلماتیک برای پایان دادن به درگیری‌ها در منطقه بررسی شد، همچنین تقویت روابط تاریخی عمیق بین دو کشور و دو ملت دوست مورد بحث قرار گرفت.
آقای الاعرجی بار دیگر تأکید کرد که قانون اساسی عراق اجازه استفاده از خاک عراق به عنوان نقطه شروع برای حمله به کشورهای همسایه را نمی‌دهد و به نیاز به تشکیل شورای هماهنگی امنیتی بین همه کشورهای منطقه اشاره کرد.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76151" target="_blank">📅 20:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76150">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a65cbfac7.mp4?token=OPaepMYXAnNu2EZln5XZXIA2LEB5yh1VIAo-WyfDRXCUsAohWDiGdrpEtckJfrkBfN1-o3BEi-Fz6egsOiMDntM6PqfjfSsvXQmH-X4-TW4nDZrfRHORe2BDqmiNVSxVdZFD67gkzA-ukwGGkRqMLgpJpaAwNsVuETTnEuzUr9XLv0Az-h22poxIh9zztb4fxqyYn1NdTM-Jd03SHot_RwNnrGpHHq2bvi0HXEtjWf79pisZoq4jCAqXdBTUhD-yZaeVCoS9yT1HVDmNxZVW862KY_SvZMc9kg0YTGuud18lR14DIa9S5r6nIDE1Z_rXXAFqEB_jJB5GY6V2WHm9lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a65cbfac7.mp4?token=OPaepMYXAnNu2EZln5XZXIA2LEB5yh1VIAo-WyfDRXCUsAohWDiGdrpEtckJfrkBfN1-o3BEi-Fz6egsOiMDntM6PqfjfSsvXQmH-X4-TW4nDZrfRHORe2BDqmiNVSxVdZFD67gkzA-ukwGGkRqMLgpJpaAwNsVuETTnEuzUr9XLv0Az-h22poxIh9zztb4fxqyYn1NdTM-Jd03SHot_RwNnrGpHHq2bvi0HXEtjWf79pisZoq4jCAqXdBTUhD-yZaeVCoS9yT1HVDmNxZVW862KY_SvZMc9kg0YTGuud18lR14DIa9S5r6nIDE1Z_rXXAFqEB_jJB5GY6V2WHm9lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
نتنياهو:
قررنا تعميق العمليات العسكرية في لبنان.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76150" target="_blank">📅 20:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76149">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo2CprXpro6MT6z07mj_G7pmEYVjiS8B9_VQD2fH5P07rVZNAAa_EcZfIOUYt3vnVsw_oULLXkAhGs7Pgz59t7F3_ciIydcv87wcsTnUHVR3ce5iHokS2miPXxvi8sxsezWh82-8IDkEnEWOkURB33OB2uPZ7rZUyhWRG0JdNJrs89nsXaiSz3mYj-74tn_GTm0JY5CEYW_BcXtW-ULKhM5unpDaIKK7Glqs6ywOzJh35YHMcN-CCg4ROsYoAMzkG2jiKguZL3uey6JIJbfQbtPfQjprgDT30_eNaelCsZAnr9k7YtTnPear2YqND8pnFSlX5OfEZmWafEFN80iXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
انتهيت للتو من الفحص الطبي الدوري الذي أجري كل ستة أشهر في المركز الطبي العسكري والتر ريد.كل شيء كان على ما يرام. شكرًا للأطباء والموظفين الرائعين! عائد إلى البيت الأبيض.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76149" target="_blank">📅 20:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76146">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0b9345b0.mp4?token=d_Wld_ZaDpdWdaWgK6tE4nZePdB9w-wSUVWDpeJOP8_ikbK2-9zSwxPD_9FhA_nCrk7-vGbhwi0wNPcPKpONLhun9le0c-DMDl_k3r-sKWffDIszw25gGuhya0PlpDc4__q28uS0PFw-HsQGSmNLi56HMsbFU2a4gV6D2Rj_jW2VWKCWtfiSJUFb7aHt0k-kudJTJ-VKEkTftXiK-JUXNZUVonFnTb4h-VhexYkq22xjagzk-UGDbIgRw-brH3fy1iUb7-xhzujN2nLJNlpydG27I0dH8ErnHOX-lRY-tklVDKmKlZ6BFAir-QbpoX9z0ie1vq3nsW-ASkHQKw9HcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0b9345b0.mp4?token=d_Wld_ZaDpdWdaWgK6tE4nZePdB9w-wSUVWDpeJOP8_ikbK2-9zSwxPD_9FhA_nCrk7-vGbhwi0wNPcPKpONLhun9le0c-DMDl_k3r-sKWffDIszw25gGuhya0PlpDc4__q28uS0PFw-HsQGSmNLi56HMsbFU2a4gV6D2Rj_jW2VWKCWtfiSJUFb7aHt0k-kudJTJ-VKEkTftXiK-JUXNZUVonFnTb4h-VhexYkq22xjagzk-UGDbIgRw-brH3fy1iUb7-xhzujN2nLJNlpydG27I0dH8ErnHOX-lRY-tklVDKmKlZ6BFAir-QbpoX9z0ie1vq3nsW-ASkHQKw9HcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إشتباكات عنيفة بين مشجعي فريقي كرة القدم هبوعيل بئر السبع ومكابي تل أبيب في القدس المحتلة.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/76146" target="_blank">📅 20:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76145">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يستهدفون دبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة رشاف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76145" target="_blank">📅 19:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76144">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يستهدفون دبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة رشاف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76144" target="_blank">📅 19:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76143">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
نائب الرئيس الايراني:‏أُعيد فتح الإنترنت وتوفير خدمات ذكية استجابةً لمطالب الشعب، مع التوجه لإزالة العقبات أمام التنمية والريادة العلمية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76143" target="_blank">📅 18:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76142">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">📰
وول ستريت جورنال: البحرية الأمريكية تستأنف توجيه السفن عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76142" target="_blank">📅 18:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76141">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6nEfyCxmpK2coDCxaj8BMmhQbCVxmpKsUXjTA6GOEeYVEq6lAy4MOR8fLgvkGYy3Y0Se941bcS_aE8FC5evM40ruoqqJA5VNzjhJWFAB0fm1s044SDgdBaQWL1uQA8p7TB_IwPtBa2iT8sOXhVSYBosvUVrtCUrYO8v_iYRprbKZGjr_FZfIyWnbL_svhVDFta1SC8RkbGUJC3nhHcelLhTI09uhZY-Ux1vMGNm_xYTxRjgZvKFLxliPnsnLLfATe_u-MVJ1J-pKUpcIjtA1YSirgReNeD3jyPZabYeIbTBd4402h07X5OMXg21WJQhT8oD9vJeqfjadnRG0lmrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
ديمتري ميدفيديف:
قال الاتحاد الأوروبي إنه سيحافظ على وجوده الدبلوماسي في كييف دون تغيير، على الرغم من تحذيرات روسيا. حسنًا، يبدو أن لديهم دبلوماسيين فائضين ويحتاجون إلى تقليص عددهم.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76141" target="_blank">📅 18:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76140">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🌟
‏ترامب يرفع سقف استقبال اللاجئين بمقدار 10 آلاف لاجئ لاستقبال المزيد من البيض من جنوب أفريقيا.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76140" target="_blank">📅 18:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76139">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e929c95856.mp4?token=bNxOCLneAaG1MLVDriFyW_UdCQE_ULZUc8OO6op9hTeMdiWa93ea3nko0uHteeXWA1Jh3IqV8b2BqOwv1qLOVQCzfmwanmKY9-32G1DJls1isELKUhTrpMsaVQgyYojV9-oTyI6Rl8z0l48CrEl8wasXpiJsfjm2MAVelwonioEFyZGoN6ctmZRlGdEb0rqQKtoZMOx5jpQWLdsZ6bW-w1KUnUjtlgv-149UhBypCDh6D2L6cUCdktR8eifVkZ60cRE022rfy4r3nz9AfcPF54A9DVmVhaOpPNgfXL4dx0mbRSqTHHupnpxDoNZ9CZPfkZhbnkSOsDtUaN14Y2gXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e929c95856.mp4?token=bNxOCLneAaG1MLVDriFyW_UdCQE_ULZUc8OO6op9hTeMdiWa93ea3nko0uHteeXWA1Jh3IqV8b2BqOwv1qLOVQCzfmwanmKY9-32G1DJls1isELKUhTrpMsaVQgyYojV9-oTyI6Rl8z0l48CrEl8wasXpiJsfjm2MAVelwonioEFyZGoN6ctmZRlGdEb0rqQKtoZMOx5jpQWLdsZ6bW-w1KUnUjtlgv-149UhBypCDh6D2L6cUCdktR8eifVkZ60cRE022rfy4r3nz9AfcPF54A9DVmVhaOpPNgfXL4dx0mbRSqTHHupnpxDoNZ9CZPfkZhbnkSOsDtUaN14Y2gXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
الاحتلال الصهيوني يستهدف عدة منازل مدنية في محافظة النبطية جنوبي لبنان.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76139" target="_blank">📅 18:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76137">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfd9de336.mp4?token=lo9ZwmDq3-OOYqbJi0xL_RVdpzDOsmvSCNenfhtw8o3AtlWWEsM3Syzw-J9H5eW-ehJ-CJpP0N8eehM6vPehk3YDeXKaqqp10cj1YU1ebwe7GeoyRQRMjAEI7_kqxnXyEQTesb4yNEKf0Lmof8zm-ddOdLXnXOvgl41PKSL1bniEAN3dC9X2CX7eW8nMj0MU5hjB2zV7iB2KqVxqWMcKwU_cH8H8-fySWbve-okDDUXxsako6MFhW4Qquo9rhRJ0WHdkZrOnR3EXvCYHh3SqpqKiG-KczHiqVGJdxN-Vxh2xS8LuTfvyuAhgL2t_NOL-OZkBzgEmPQOABqc9FwIjag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfd9de336.mp4?token=lo9ZwmDq3-OOYqbJi0xL_RVdpzDOsmvSCNenfhtw8o3AtlWWEsM3Syzw-J9H5eW-ehJ-CJpP0N8eehM6vPehk3YDeXKaqqp10cj1YU1ebwe7GeoyRQRMjAEI7_kqxnXyEQTesb4yNEKf0Lmof8zm-ddOdLXnXOvgl41PKSL1bniEAN3dC9X2CX7eW8nMj0MU5hjB2zV7iB2KqVxqWMcKwU_cH8H8-fySWbve-okDDUXxsako6MFhW4Qquo9rhRJ0WHdkZrOnR3EXvCYHh3SqpqKiG-KczHiqVGJdxN-Vxh2xS8LuTfvyuAhgL2t_NOL-OZkBzgEmPQOABqc9FwIjag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
أ ف ب:
رئيس الوزراء الفرنسي يعتزم اللجوء إلى القضاء ضد معاملة إسرائيل "المروعة" لناشطين في أسطول غزة.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/76137" target="_blank">📅 18:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76136">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📰
وول ستريت جورنال:
البحرية الأمريكية تستأنف توجيه السفن عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/76136" target="_blank">📅 18:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76135">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b6835677.mp4?token=QTQ8fJibbr8CRtu4KRAiQO8E6zJbeEigEwqStU1tp31jGpw1vTr_DClSkmfYnsnFqQlFMHIbLZe2Hu5ZkuhNT-YN6Rg-qGln2MJI3LhnD7KIXK_38hcVO-Wa1dGmbQ2JvV7APxKWWhODm-Lp7yGdZH56enThl7MbCqePNvGBH1hMtD8dgR37V-IvTPUuFxO_cshmHahnFV_Nk-imLhMl3aFj4xi7tYY565M0oEF8L25WIFz7oTFeTPecXDpLftaU6rBpm2PXD72brIJKOl0zluzoy0tGrEMD0zDjcENHLxetUiGhc1RldHBxwFLMpmQK-MbsU-KMH9-k_wWQpPAeeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b6835677.mp4?token=QTQ8fJibbr8CRtu4KRAiQO8E6zJbeEigEwqStU1tp31jGpw1vTr_DClSkmfYnsnFqQlFMHIbLZe2Hu5ZkuhNT-YN6Rg-qGln2MJI3LhnD7KIXK_38hcVO-Wa1dGmbQ2JvV7APxKWWhODm-Lp7yGdZH56enThl7MbCqePNvGBH1hMtD8dgR37V-IvTPUuFxO_cshmHahnFV_Nk-imLhMl3aFj4xi7tYY565M0oEF8L25WIFz7oTFeTPecXDpLftaU6rBpm2PXD72brIJKOl0zluzoy0tGrEMD0zDjcENHLxetUiGhc1RldHBxwFLMpmQK-MbsU-KMH9-k_wWQpPAeeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
الصحيفة الالمانية شبيغل: تخطط الولايات المتحدة لتقليص كبير للقوات العسكرية والمعدات التي تلتزم بها تجاه حلف شمال الأطلسي في أوروبا، مما يزيد الضغط على الحلفاء الأوروبيين لملء الفجوات بأنفسهم.  تشمل التخفيضات المقترحة طائرات مقاتلة، وقاذفات استراتيجية، وسفن…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76135" target="_blank">📅 17:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76134">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌟
حزب الله ينشر:
أحرارٌ أعزّاءُ لا عبيدٌ أشقياءُ.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76134" target="_blank">📅 17:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76133">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌟
رويترز
: العقود الآجلة لخام برنت ترتفع 4 دولارات للبرميل، بعد عدة ضربات وجّهها الحرس الثوري على حاملات النفط بسبب مخالفتها قوانين مرور مضيق هرمز.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76133" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76132">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
‏ رويترز: عراقجي وقاليباف في قطر.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/76132" target="_blank">📅 17:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76131">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🌟
🌟
يديعوت أحرونوت:
حزب الله لديه مسيرات قادرة على الوصول حتى مسافة ٣٠ كلم.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/76131" target="_blank">📅 17:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76130">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇩🇪
الصحيفة الالمانية شبيغل:
تخطط الولايات المتحدة لتقليص كبير للقوات العسكرية والمعدات التي تلتزم بها تجاه حلف شمال الأطلسي في أوروبا، مما يزيد الضغط على الحلفاء الأوروبيين لملء الفجوات بأنفسهم.
تشمل التخفيضات المقترحة طائرات مقاتلة، وقاذفات استراتيجية، وسفن حربية، وغواصات، وطائرات بدون طيار، وطائرات التزود بالوقود جواً.
لا تزال واشنطن تعتزم الحفاظ على الردع النووي في أوروبا، لكنها تريد من الأوروبيين تولي معظم مسؤوليات الدفاع التقليدية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/76130" target="_blank">📅 17:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76129">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16fda706f6.mp4?token=YLc5k5IxIpxRmxk3rfCi_qnJamc9JogsFh2oslAr80Ugfz26lULxG2Zhe0PHpcfNKR8BP2AtFvPCbB4g3FzBvqpKzTsu9gVbXGmvNp6PmtLx0T0kT8XfESDPWGjEAns_fVJqmmiZzHBYiM1DoDX46SEwx0_g9jtlufYfKDNaX4JgYHoKt9Kmg1EHROmirgTroBU3AKLMxiQ-23MgZVRxQ2xuBWDA2UntJKlBGO-87CYVBhDE7-FzDpw54Z7aQ185VYCrQ2f1Gh_TqLMDr-0nDeGUjCHeWG__alD0izKuisTtn7IOelcZTP_n70HufoI0fFLt1rKmKdWTbCaows_sXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16fda706f6.mp4?token=YLc5k5IxIpxRmxk3rfCi_qnJamc9JogsFh2oslAr80Ugfz26lULxG2Zhe0PHpcfNKR8BP2AtFvPCbB4g3FzBvqpKzTsu9gVbXGmvNp6PmtLx0T0kT8XfESDPWGjEAns_fVJqmmiZzHBYiM1DoDX46SEwx0_g9jtlufYfKDNaX4JgYHoKt9Kmg1EHROmirgTroBU3AKLMxiQ-23MgZVRxQ2xuBWDA2UntJKlBGO-87CYVBhDE7-FzDpw54Z7aQ185VYCrQ2f1Gh_TqLMDr-0nDeGUjCHeWG__alD0izKuisTtn7IOelcZTP_n70HufoI0fFLt1rKmKdWTbCaows_sXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
الاحتلال الصهيوني يستهدف عدة منازل مدنية في محافظة النبطية جنوبي لبنان.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76129" target="_blank">📅 17:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76128">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34378ee6f.mp4?token=ba1Elp9bfyYYOYbd6K9UOavI5PTnsU2rZn37mSYuSO9a1L3RIpMe84g-uy0wfnhF6bgJeQILYmD4J0_scXYA_MXDEDKo6f2HQUF-XcbLaG4zxjJBakGtFhDOqD5hI6D-9SfC27rEAWK0a02wFvP9We8w32O20nWPj_v8wE3t5S15HBWfFZOjDQ6ybFjmcqVRV90Ybru8otBJezupUKXBP2maFE6yTCzwo6SqXJoWfxXA_ug3sa5WHxAtum48dTV0AXkFYKcIUEpZGDxZqXqqcDp6_gqSvBiKr-EBjeEPhiN-Efc_nMlcuKSTmEmaBa_Qutw3U689OEHNvcaibhD__g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34378ee6f.mp4?token=ba1Elp9bfyYYOYbd6K9UOavI5PTnsU2rZn37mSYuSO9a1L3RIpMe84g-uy0wfnhF6bgJeQILYmD4J0_scXYA_MXDEDKo6f2HQUF-XcbLaG4zxjJBakGtFhDOqD5hI6D-9SfC27rEAWK0a02wFvP9We8w32O20nWPj_v8wE3t5S15HBWfFZOjDQ6ybFjmcqVRV90Ybru8otBJezupUKXBP2maFE6yTCzwo6SqXJoWfxXA_ug3sa5WHxAtum48dTV0AXkFYKcIUEpZGDxZqXqqcDp6_gqSvBiKr-EBjeEPhiN-Efc_nMlcuKSTmEmaBa_Qutw3U689OEHNvcaibhD__g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
السيناتور ديف ماكورميك:
"سيتعين علينا استخدام الجيش لفتح المضيق وطمأنة السفن التجارية. لدينا القدرة على القيام بذلك. لن يكون الأمر سهلاً، لكن هذا هو الطريق الأصعب في نهاية المطاف."
خذها ان استطعت
😎
...</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76128" target="_blank">📅 17:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76127">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPYtE7XE5pNRC_yjA4hMR4kv1VpP9W_DKrIfYUJd7AUwDtxa2SC19OvDuBMRs5YFleBQdnomGWSYUzLMbuHMCkeDm_chx5GxbHnctjZVwi4qyWEPC32A5vcoNg9mk-DuqB_Y5OZgda_T7lZZIkchkuPWOxi719pWKcp4BxdQ82N0HWvjl_jUbHg1O4Xz9KCu4BXuV28v7vHgVGrveSYl1l1KUFw_anCR5I-eVLiNXk3NYai9ZlkI7gezJCxfN06XuRcPdt_mJoX8-aT4VNqc8PjUd57pf7mV_rKgFTyia5Is43aiVaq3yOKbPB2TXhI4MlSaMVVlU4Z-IGjVASoCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نائب الرئيس الايراني:
‏أُعيد فتح الإنترنت وتوفير خدمات ذكية استجابةً لمطالب الشعب، مع التوجه لإزالة العقبات أمام التنمية والريادة العلمية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76127" target="_blank">📅 16:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76126">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجار يهز سواحل عمان</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76126" target="_blank">📅 15:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76125">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجار يهز سواحل عمان</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76125" target="_blank">📅 15:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76124">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d125f4a00.mp4?token=tUwVvDTnheWuwvLdvFgat8yNlov9fs361T7U3yufqKT0xi5Zna5I1dOalhrYpYWULvVR-p93ZNfDT7f4nwFQ743jUMltNrVohmnn0ai-xmlSBeR0vpuvgGXB-bI7bE3pYvFIEaxGTtmLR9j0wD01iku1IsxocGH8d5-eq-2Ks-1JeqFdIpNJW6xg36Vv8lE8g0_-wlIHDOQdmHtatgkSCjB1r8K7KJSCJdCDrQpXSDtFocv4Sxh4aGS0qusk_8I2oe5Q3gigs7Z5mhD9sIswoCUix4ufsqJQuxwRGs-JeWOSyV9drVySueQZZY9Ef6sG7ZIA_xT8vI4KHI9Gla0jsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d125f4a00.mp4?token=tUwVvDTnheWuwvLdvFgat8yNlov9fs361T7U3yufqKT0xi5Zna5I1dOalhrYpYWULvVR-p93ZNfDT7f4nwFQ743jUMltNrVohmnn0ai-xmlSBeR0vpuvgGXB-bI7bE3pYvFIEaxGTtmLR9j0wD01iku1IsxocGH8d5-eq-2Ks-1JeqFdIpNJW6xg36Vv8lE8g0_-wlIHDOQdmHtatgkSCjB1r8K7KJSCJdCDrQpXSDtFocv4Sxh4aGS0qusk_8I2oe5Q3gigs7Z5mhD9sIswoCUix4ufsqJQuxwRGs-JeWOSyV9drVySueQZZY9Ef6sG7ZIA_xT8vI4KHI9Gla0jsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 22-05-2026
دبابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة مركبا جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76124" target="_blank">📅 15:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76123">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJThUTBvEjHI6N2pZtVH1xyB2FuqFXzrtynjfwJQLTiiyiev1OwiqlO02XEV8YR0RjuotoEmSXVA5i6q4_ZMrHaCJKMun48eC2gYLs5PkTftLf2XuuiSioDbcSNnCnbn2P6-q3T5P0yMpIs8J6rltaAZtyiQ2u9prnMMVQhQZDfcQKsJvPeo9EHtQFop3DNAZBLKUHv8m2-wYKduKvUdztM3-TG7j9wuni8P3V0-t6aatHKPtdpVz0jZOeuRKexwugkyiHiJloqPEdghVlmrssIe5TTUSUuHauS8khSWdHkzHHve-59vGA3Dj1FVUsv9nN-w0ujsdf1P_Xb0VkLTIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
الخارجية الإيرانية:
طهران سترد على الخرق الأميركي لوقف النار.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76123" target="_blank">📅 15:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76122">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇷🇺
مجلس ‏الدوما الروسي:
الهجمات على المدنيين قد تدفع موسكو لاستخدام أسلحة لا تترك أثرا لأي شخص.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76122" target="_blank">📅 14:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76121">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">#عاجـــــــــــــــل
⭐️
وفاة أول حاجة عراقية من أهالي محافظة واسط في الديار المقدسة اثناء تأدية مناسك الحج.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76121" target="_blank">📅 13:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76120">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
اندلاع أعمال شغب عنيفة داخل دار تأهيل النساء في منطقة الاعظمية وسط العاصمة بغداد وأنباء عن سقوط عدد من الإصابات</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76120" target="_blank">📅 12:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76119">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏وكالة أ ب: وساطة قطرية نجحت في تحقيق تفاهم أميركي إيراني بشأن "الأموال المجمدة"  ‏من المرجح أن تعلن الولايات المتحدة وإيران اليوم اتفاقا بشأن "الأموال المجمدة"</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76119" target="_blank">📅 12:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76118">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: استهداف قاعدة عسكرية في الجليل الغربي بمسيرات حزب الله</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76118" target="_blank">📅 12:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76117">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏وكالة أ ب: وساطة قطرية نجحت في تحقيق تفاهم أميركي إيراني بشأن "الأموال المجمدة"
‏من المرجح أن تعلن الولايات المتحدة وإيران اليوم اتفاقا بشأن "الأموال المجمدة"</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76117" target="_blank">📅 12:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76116">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">إعلام غربي : يدرس المدعون الإسرائيليون توجيه اتهامات جنائية ضد رئيس ديوان نتنياهو، تساحي برافرمان، بتهم الاحتيال وخيانة الأمانة وعرقلة سير العدالة المرتبطة بالتسريب المزعوم لوثيقة استخباراتية سرية للغاية إلى صحيفة بيلد الألمانية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76116" target="_blank">📅 12:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76115">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
حزب الله: سرديّة استهداف قائد لواء المدرّعات 401 في جيش العدو الإسرائيلي العقيد مئير بيدرمان في أطراف بلدة دبل جنوبيّ لبنان بتاريخ 20-05-2026
بعد سلسلة محاولات تقدّم إلى بلدة حدّاثا ومن عدّة محاور، لم ينجح العدوّ في اختراق دفاعات المقاومة عند أطراف البلدة التي تكبّد فيها العديد من الخسائر من جنوده وآليّاته.
خلال مساء يوم 19/05/2026، هاجم العدوّ حدّاثا بشكل عنيف ومن محوري تقدّم بجمع كبير من الآليّات و34 جنديًّا (قوّة من الكتيبة الهندسيّة القتاليّة 601). دارت اشتباكات واسعة عند أطراف البلدة. وعند الفجر انكفأت القوّة المتقدّمة تاركةً خلفها جرّافتين مدمّرتين و4 دبّابات احترقت نتيجة استهدافها بالمحلّقات والقذائف المباشرة. أمّا الجنود فقد شُوهِد خروج 28 جنديًّا و6 الباقون تمّ نقلهم بواسطة آليّة نميرا بعد إصابتهم منهم قائد السرية النقيب م. ومقاتلة التوثيق العملياتي الرقيب الأول ش.، اللذين أصيبا بجروح متوسطة وخطيرة.
كان هذا التقدّم بإشراف قائد اللواء (401) مباشرةً الذي كان يتابع تقدّم القوّات وكذلك انكفاؤها من التموضع المتقدّم للواء في بلدة رشاف.
عند الساعة 05:00 فجرًا، عاد اللواء مئير بيدرمان إلى المقرّ المستحدث لعمليّات اللواء عند أطراف بلدة دبل بعد انكفاء القوّة كليًّا. هذا كلّه كان تحت عين ورصد المقاومة.
عند الساعة 07:50 صباحًا، وصلت أوّل محلّقات أبابيل الإنقضاضيّة إلى المقرّ وقامت بجولة مسح ميداني للمقرّ ودارت حوله، وعندما رصدت تموضع لضباط العدّو خلف تمويه في الطابق الأخير، وبعد فرارهم إلى الداخل لحقتهم المحلّقة التي استطاعت الدخول خلفهم إلى المقرّ وأصابتهم وأصابت غرفة العمليّات مباشرة. ونتيجة الاستهداف هذا أُصيب قائد اللواء مئير بيدرمان في رأسه وضابطان آخران.
عند الساعة 08:10، قام فريق إسعافي بإخلاء الإصابات عبر آليّة هامر إلى مهبط المروحيات. وصلت الهامر إلى المهبط عند الساعة 08:23، حيث اقلّت المروحيّة اثنين من المصابين، بينما نُقل المصاب الثالث بسيارة إسعاف.
عند الساعة 08:45، عاد الفريق إلى المقرّ عند أطراف بلدة دبل، حيث كانت تنتظره محلّقة أخرى قامت باستهداف المقرّ من جديد. وأصابت أخرى شاحنة ذخيرة، ما أدّى إلى انفجارات واندلاع حريق قرب المقرّ.
عند الساعة 09:00، وبينما كانت القوّة تستعدّ لمغادرة المبنى، استهدفت محلّقة أبابيل أخرى آليّة نميرا عند مدخل المقرّ.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76115" target="_blank">📅 12:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76114">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 20-05-2026 المقر المُستحدَث لقيادة لواء المدرّعات 401 التابع لجيش العدو الإسرائيلي في بلدة دبل جنوبيّ لبنان بسربٍ من محلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76114" target="_blank">📅 12:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76113">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1060dd6c41.mp4?token=YVx5Jp2FYp_NY5WGLD5jpJx3dAP9D1hSaibLHYl0rqPmq6yT6R_IE9KGRu-TSjj_GnvuLC1k9tdoKTpWZ4C8rpG5MO0BcDAlr00mrTimiqCHRz9usuavw0GSrurz4gnvB51zz7OSmyRy0NI4ZQUH3MaTs1uM_CPwRfAlAPpzBca16GS0ri29qHUcvZ93pPEEO5Af28tP4uj1uYqJlkgh0zvhMJD1_p6053vWPa4QTzlZek5KWuwYYA6oufZaxjVeb35rZ11-eKukZvAvd5i0HGbink_VtkQtjnuVM0M1-Rz055oNrX4QUXdctCAeG8jnZQu2MQ-vs36yA0sC6gQ2OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1060dd6c41.mp4?token=YVx5Jp2FYp_NY5WGLD5jpJx3dAP9D1hSaibLHYl0rqPmq6yT6R_IE9KGRu-TSjj_GnvuLC1k9tdoKTpWZ4C8rpG5MO0BcDAlr00mrTimiqCHRz9usuavw0GSrurz4gnvB51zz7OSmyRy0NI4ZQUH3MaTs1uM_CPwRfAlAPpzBca16GS0ri29qHUcvZ93pPEEO5Af28tP4uj1uYqJlkgh0zvhMJD1_p6053vWPa4QTzlZek5KWuwYYA6oufZaxjVeb35rZ11-eKukZvAvd5i0HGbink_VtkQtjnuVM0M1-Rz055oNrX4QUXdctCAeG8jnZQu2MQ-vs36yA0sC6gQ2OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مشهد بات مألوفاً في سوريا تحت حكم الجولاني.. حيث أصبح من هواية الأجانب الإرهابيين التجول في الأحياء المسيحية وتحديداً حي باب توما الدمشقي وترديد التكبيرات لإثارة النعرات الدينية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76113" target="_blank">📅 11:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76112">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: وجّه مجتبى خامنئي، المرشد الأعلى لإيران، رسالة تهديد إلى الولايات المتحدة : "لن تكون أمريكا آمنة في منطقتنا".</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76112" target="_blank">📅 11:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76111">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني: ما تم تداوله في الإعلام حول البنود الـ14 لمذكرة التفاهم بين إيران والولايات المتحدة لا أساس له من الصحة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76111" target="_blank">📅 11:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76109">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">إعلام العدو : بدأت إسرائيل تعبئة احتياطية طارئة، بما في ذلك قوات المدفعية التي تم تسريحها مؤخراً من الخدمة، مع تزايد الاستعدادات لعمليات دفاعية موسعة في لبنان وسط استمرار هجمات حزب الله وانتهاكات وقف إطلاق النار</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76109" target="_blank">📅 10:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_رهبر_انقلاب_اسلامی_به_مناسبت_برگزاری_حج.pdf</div>
  <div class="tg-doc-extra">415.4 KB</div>
</div>
<a href="https://t.me/naya_foriraq/76108" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">النص الكامل لرسالة قائد الثورة الإسلامية بمناسبة موسم الحج | 5 خرداد 1405</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76108" target="_blank">📅 10:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الجيش الإسرائيلي: لم نشارك في الضربات ضد إيران إلى جانب الولايات المتحدة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76107" target="_blank">📅 10:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76106">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⭐️
هجوم بالطيران المسير الانتحاري وعدة صواريخ يستهدف مقر تابع للمعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76106" target="_blank">📅 10:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76105">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📰
‏القناة 12 الصهيونية عن مصادر:  مجتبى خامنئي لم يصادق بعد على التفاهمات المتبلورة</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76105" target="_blank">📅 10:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76104">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO5k7mXLMtKNjp4q_61SAnyhILI-RZaitHfKjrb89nv2eXkO2MkMmy_AXHe6_BOu4Rsu8A2Xbxc4DzmI7NC25VEdK6DGvVHz12dshL18r1AIBfGDOVVxbSijAE5d6BImx7DulkWdXuzBD_2CRsDOww6hQlMKAnpyWr9FIpP0Oqxz4IpxuoeBKWqS8b2FDvebvSVncP6FIJWPdfUTN4xFDoPJMgFyfdO-4uR1-_Eoky6nKtHlzsXtd93ItNPBHOP82KUHkeRvtcvp3LD0PN0sdb3W0YdnGU9N8ySMkK2oY9RaVqutYwKK5XBBQOg5YdNzefaSYaWQBwftT4vML2yacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني في الشارع الرئيسي بمدينة العفولة نتيجة انفجار سيارة ووجود جريح في موقع الحادث.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76104" target="_blank">📅 09:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76103">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏴‍☠️
انفجارات داخل مستوطنة بيرنيت شمال الكيان نتيجة هجوم بمسيرات حزب الله.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76103" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76102">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي: إيران حاولت مهاجمة القوات الأمريكية على مدى الساعات الـ٢٤ الماضية.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/76102" target="_blank">📅 02:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76101">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
إيران حاولت مهاجمة القوات الأمريكية على مدى الساعات الـ٢٤ الماضية.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/76101" target="_blank">📅 02:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76100">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: ‏القوات الأمريكية تصيب أهدافاً تشمل إطلاق صواريخ و‏مواقع وسفن إيرانية تحاول زرع ألغام.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/76100" target="_blank">📅 02:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76099">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: نفذت القوات الأمريكية ضربات دفاعية في جنوب إيران يوم الاثنين.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/76099" target="_blank">📅 02:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76098">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/76098" target="_blank">📅 02:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76097">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مصدر إيراني:
ماتم تدوله حول تفعيل الدفاعات الجوية في مدينة قم المقدسة لا صحة له.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/76097" target="_blank">📅 01:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76096">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نقل النتن ياهو لمستشفى في القدس</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/76096" target="_blank">📅 01:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76095">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تفعيل الدفاعات الجوية في بندرعباس.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/76095" target="_blank">📅 01:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76094">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03326bd1d2.mp4?token=PhYVkkzbxHQlxFk0gYIq-FXPwxl6tXLSDBPLs_4QWvz8uX9psuKwoWDqCkbeI1EDkSaieuDmuSGVF4r36FcmHqeeyUVbi9H9TllctJyumw8eHHDRAB1NJ0eNSjSokhKExSCEx2MPvni1YHIt9PzPQtgmZEC-HCuKdl_ZqBaHSDqnRC6XCWxCYxtezpHL97Pifp4wW73dTGw3_1B3Ed59z0P9e4jEta0-ke76wMIztFaAdoMi6VWw0w7JQwU4QxvzhB464mldBRkoO-tkIyVfkfbbg2YRiaeYR15cvuS-hnMqBj8BOwT6EOv00R229J6UivrRjTRbikkWNLZAbL41pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03326bd1d2.mp4?token=PhYVkkzbxHQlxFk0gYIq-FXPwxl6tXLSDBPLs_4QWvz8uX9psuKwoWDqCkbeI1EDkSaieuDmuSGVF4r36FcmHqeeyUVbi9H9TllctJyumw8eHHDRAB1NJ0eNSjSokhKExSCEx2MPvni1YHIt9PzPQtgmZEC-HCuKdl_ZqBaHSDqnRC6XCWxCYxtezpHL97Pifp4wW73dTGw3_1B3Ed59z0P9e4jEta0-ke76wMIztFaAdoMi6VWw0w7JQwU4QxvzhB464mldBRkoO-tkIyVfkfbbg2YRiaeYR15cvuS-hnMqBj8BOwT6EOv00R229J6UivrRjTRbikkWNLZAbL41pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇬🇧
السفير البريطاني في بغداد : الأمريكان لم يعلموا أن السيد الخامنئي مرجع شيعي وأفهم تعاطف الشيعة</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/76094" target="_blank">📅 01:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76093">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نقل النتن ياهو لمستشفى في القدس</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/76093" target="_blank">📅 01:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76092">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAz6QeBDH7APxYueLTjFMQQ2-ma8cObkHmzKbXFVwE3n_STB7mn_7TF2197LfvHcRTgN6WhhIYpdVIsHTxnjtGXz3Bv1LvMYBQ-shuDQ1Qq4C9sDT7-K9QUI2CACY2MkYh4E9OrZvO5kbGTPXXdDjCmgCgLkMUCsgiM6qjaaLoTzeSyFgyXJw_3i-77HSsFq28oC7y6PvScbFxvtZMS2TfoV9L7K1CYix8gl2s9n5TDC84T2Y6MAtOGEoAiZCubkeQnMl-txBU_ArMys90ukfJ-MbW0qX-v999WNGI0XxucB0xvsZ3_QByy1fQKYrvS8lavl5qC87hyc9xfPB9ZqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
سيتم تسليم اليورانيوم المُثري (الغبار النووي!) فورًا إلى الولايات المتحدة لإعادته إلى الوطن وتدميره، أو، من الأفضل، بالتعاون والتنسيق مع جمهورية إيران الإسلامية، تدميره في المكان أو في موقع مقبول آخر، مع لجنة الطاقة الذرية، أو ما يعادلها، كشاهد على هذه العملية والحدث. شكرًا لكم على اهتمامكم بهذه المسألة!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/76092" target="_blank">📅 01:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76091">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/76091" target="_blank">📅 01:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76090">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">هجوم صهيوأمريكي طال عدد من القوارب في جزيرة لارك جنوبي إيران</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/76090" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76089">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هجوم صهيوأمريكي طال عدد من القوارب في جزيرة لارك جنوبي إيران</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/76089" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76088">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/76088" target="_blank">📅 01:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76087">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/76087" target="_blank">📅 00:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76086">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6e89360b.mp4?token=Xi4rl1AisZ3ouNbPS29tlIwxP2mVdLWq0P5NbO7P22jZ2-9mYLCoyR91Dur6kQ4a0bIu6hSsOzKjTMlWc-oeEGSORfXD_NelkfonO2H-zN9fXuWNgEoshM6BHi0QDTX1TS-O9ZnqurFL4Zn9s-71J7NwQ6L79QTg8uueVqjrAmrDdtxxNlUqew04Syk_66GSbMtfM6UgZDOKNAwDor08IUZaG40XXDtVf044fzyF5AbrVD6hP6_7ot0w3StWstSowgTX4DgNoeNxTAibGiLRiRqReIMApIfZITyRwDxcTV3FG5HUL4qO9CBvUo54nCedXCuYbWp82-yZmGDfUohgt7SqPfdDCnSgKD-jCQF0kPW38VMAwSSfwQyhGR7MkdPTHXPHyFcChNYumjRlUrruaR0eInAVQa7wQMyGVbKRTw9x58wtBoh3knzzRiMKglTo4sJll5E2OLSqcT2UsEBSBORC_3WHb6dbMSSUSOGkemXJ5kEwyrmUM6f7yz3NMCpK6peerWXhBaYkYzEk1zGej_1510VChMpi54NYAr1TfAcBB8TNMR6CghGPmD8lEkRb0ZFtVdDozBp5bBGMUup1R_wC5zO4fVuLqCWO7DG29WqzwBJgZYDnXSQUPhcknJxKnGu4PAG0629cStFD7TtnrfhTMyQqowz9yaEHhT-XfVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6e89360b.mp4?token=Xi4rl1AisZ3ouNbPS29tlIwxP2mVdLWq0P5NbO7P22jZ2-9mYLCoyR91Dur6kQ4a0bIu6hSsOzKjTMlWc-oeEGSORfXD_NelkfonO2H-zN9fXuWNgEoshM6BHi0QDTX1TS-O9ZnqurFL4Zn9s-71J7NwQ6L79QTg8uueVqjrAmrDdtxxNlUqew04Syk_66GSbMtfM6UgZDOKNAwDor08IUZaG40XXDtVf044fzyF5AbrVD6hP6_7ot0w3StWstSowgTX4DgNoeNxTAibGiLRiRqReIMApIfZITyRwDxcTV3FG5HUL4qO9CBvUo54nCedXCuYbWp82-yZmGDfUohgt7SqPfdDCnSgKD-jCQF0kPW38VMAwSSfwQyhGR7MkdPTHXPHyFcChNYumjRlUrruaR0eInAVQa7wQMyGVbKRTw9x58wtBoh3knzzRiMKglTo4sJll5E2OLSqcT2UsEBSBORC_3WHb6dbMSSUSOGkemXJ5kEwyrmUM6f7yz3NMCpK6peerWXhBaYkYzEk1zGej_1510VChMpi54NYAr1TfAcBB8TNMR6CghGPmD8lEkRb0ZFtVdDozBp5bBGMUup1R_wC5zO4fVuLqCWO7DG29WqzwBJgZYDnXSQUPhcknJxKnGu4PAG0629cStFD7TtnrfhTMyQqowz9yaEHhT-XfVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇬🇧
السفير البريطاني في بغداد : الأمريكان لم يعلموا أن السيد الخامنئي مرجع شيعي وأفهم تعاطف الشيعة</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/76086" target="_blank">📅 00:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76085">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏴‍☠️
إعلام العدو : انتحار جنديين اثنين هذا اليوم ، أحدهما في معسكر للتدريب.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/76085" target="_blank">📅 00:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76084">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اصوات انفجارات سمعت في الخليج الفارسي قبالة سيريك وجاسك</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/76084" target="_blank">📅 00:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76083">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/76083" target="_blank">📅 00:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76082">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭐️
الإعلام الإيراني:
دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/76082" target="_blank">📅 23:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76081">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
مصدر عسكري إيراني:
التحقيقات الفنية تؤكد هجومًا إسرائيليًا بطائرة مسيرة على الإمارات.
تُظهر التحقيقات الفنية التي أجرتها القوات المسلحة أن إسرائيل نفّذت عدة هجمات بطائرات مسيرة خلال الأسابيع القليلة الماضية في عملية "علم زائف" ضد الإمارات. أن هذا العمل الإسرائيلي جاء "لاستفزاز" الإماراتيين. لقد أظهر الكيان الصهيوني أنه لا يُفكّر إلا في مصالحه الخاصة، حيث يتواصل مع بعض دول الخليج، فيجرّها إلى هاوية خطيرة، وفي الوقت نفسه يشنّ عمليات ضدها.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/76081" target="_blank">📅 23:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76080">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
إبطال مفعول عبوة ناسفة في منطقة حزام بغداد بالعاصمة العراقية " جسر الرفرش " ؛ المنطقة نشطت بها خلايا عصابات داعش أعوام ٢٠١٣ - ٢٠١٦ .</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/76080" target="_blank">📅 23:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76079">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
🏴‍☠️
إطلاق صواريخ دفاع جوي من جنوب لبنان نحو طائرات حربية إسرائيلية.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/76079" target="_blank">📅 23:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76078">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
رئيس لجنة الأمن القومي في البرلمان الإيراني:
ما لم تتخذ الولايات المتحدة خمسة إجراءات لبناء الثقة، فلا جدوى من التفاهم والتفاوض معها. وتشمل هذه الإجراءات ما يلي:
▪️
إنهاء الحرب على جميع الجبهات، وخاصة لبنان
▪️
رفع الحصار الأمريكي ومكافحة القرصنة
▪️
السماح بمرور السفن المدنية عبر مضيق هرمز بتنسيق إيراني
▪️
تعليق العقوبات النفطية لمدة 30 أو 60 يومًا
▪️
الإفراج عن الأموال الإيرانية المجمدة</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/76078" target="_blank">📅 23:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76077">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc8092e1.mp4?token=giFXor8z7MjXQSXlMYsy6e9JQ53Iwtx25_ankp5-RTCVBBVKWK1n503kZJ2WjgkELpRnDznmxDeJXsk87rIVU-vRmM5lMJFJXwEi1uUNsAn2s5aeRhA4bsY5bhbp68T-kDwPGZj6-Gs554ipP9U9qWsCKKWr_b-1lrZhJrG6hSs7aGqtFwkvQ48OTA3qloGFkSzoP1QtbTbttT1t2MJ3KxSXKus8empTj2CeibcgqiN3yUNreTN7fWwhCkyUSCwgXAAZBw2q8OXbYdwUq9vBD_i8NW432va1KZD7L5X6q6WmmsJ61hak0wQjJl_pfZJBNFlQCqQyMJEvm78GLHHeUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc8092e1.mp4?token=giFXor8z7MjXQSXlMYsy6e9JQ53Iwtx25_ankp5-RTCVBBVKWK1n503kZJ2WjgkELpRnDznmxDeJXsk87rIVU-vRmM5lMJFJXwEi1uUNsAn2s5aeRhA4bsY5bhbp68T-kDwPGZj6-Gs554ipP9U9qWsCKKWr_b-1lrZhJrG6hSs7aGqtFwkvQ48OTA3qloGFkSzoP1QtbTbttT1t2MJ3KxSXKus8empTj2CeibcgqiN3yUNreTN7fWwhCkyUSCwgXAAZBw2q8OXbYdwUq9vBD_i8NW432va1KZD7L5X6q6WmmsJ61hak0wQjJl_pfZJBNFlQCqQyMJEvm78GLHHeUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
هجوم بالطيران المسير الانتحاري وعدة صواريخ يستهدف مقر تابع للمعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/76077" target="_blank">📅 22:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76076">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تخشى "إسرائيل" من إطلاق حزب الله النار على الشمال، في أعقاب الهجمات الكبيرة التي يخطط لها الجيش الإسرائيلي في لبنان.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76076" target="_blank">📅 22:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76075">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac03e8b15.mp4?token=dF3n7h0P2zGRezAH4sGmDnAx2TAnuggoHdTIepFNarVuvbJUYYLJMZ1mxAYlRInLd8jzIbxdCViT3V-mRfmsEvKox5e52MtOKysL66QJzUTId3k2yj5HJEh8Rd8Ttp0XZrF6OhAiRfzzz_bqAeg7I8Z_hVfioVSEINwSnT3wcxQGlRNJixekH6bnOjJ7AYE6qO-eOit8kkP2vDlgsOsL0oef0sd1l1hxe-aZoFhzy1hXLqS3efyLEKTc6uydeX2zNBAUYXGWl5sxgAxEaSeuJ-4y_cjGy6H5ZWITmISvlH4b9oYuqo0NJL8KpxUMj2NPgILSjvDP1iINy6REpguSCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac03e8b15.mp4?token=dF3n7h0P2zGRezAH4sGmDnAx2TAnuggoHdTIepFNarVuvbJUYYLJMZ1mxAYlRInLd8jzIbxdCViT3V-mRfmsEvKox5e52MtOKysL66QJzUTId3k2yj5HJEh8Rd8Ttp0XZrF6OhAiRfzzz_bqAeg7I8Z_hVfioVSEINwSnT3wcxQGlRNJixekH6bnOjJ7AYE6qO-eOit8kkP2vDlgsOsL0oef0sd1l1hxe-aZoFhzy1hXLqS3efyLEKTc6uydeX2zNBAUYXGWl5sxgAxEaSeuJ-4y_cjGy6H5ZWITmISvlH4b9oYuqo0NJL8KpxUMj2NPgILSjvDP1iINy6REpguSCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
وكما قال الشهيد الأقدس:
بتوسّع منوسّع...بتعلّي منعلّي</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/76075" target="_blank">📅 22:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76074">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🤙
🔥
الخارجية الروسية : على الجاليات الأجنبية مغادرة كييف فورا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76074" target="_blank">📅 22:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76073">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En2uUL1tkf_cOxR3D__b4-MlQzmr5H4CDdxinYMBeLiGYGxBYg02iWn-FkJulbGVV-HLE10jmAZtrsXt3Q-NPhjrTykxJdFHTHjgzMFXxL3EwiLFaH8-I9nMrPU0HH4cqutg2QdC4uIbj7mlZ_2W17Q3HzVvBHUC8roGIbSTWKanx6iPLMzuJ6QBzFIgtZb2CTgPR_a9rWIBVOc2usou9xXvjmkDxF4KJA_hORVfKtu9rHnZfPoetNzqxCahO5rebHqhmoODbtbDn0M5BVIDlU9e8pJtRb11a_R2MjjzWbkGMjuUIUNMvFKbC_iH0BIkF1wNvoW8xtk32N5_o-gGkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو يطلق حملة تبرعات للجنود والعوائل المهجرة في شمال فلسطين المحتلة بسبب ضربات حزب الله.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76073" target="_blank">📅 22:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76072">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126245a760.mp4?token=gfHx9y49m65m7DvT9cYw6C2TOy6dxSQVl_1vLpywakj5mth3KTAjbLzwSxCuZDQAzi31KhrWgg0TL8VPSNBEBXB9rkFV0VwlcW7AXx5LYI6dyVutW8CZgjC-hutqHTW-bVE_aUDzn3KdFgx9hg7wgIdhVKZO5C9dQeEBUzCXzl7w4KSnsmnUeBOxJe_FOheHlM8FdT45pRjSE4QnKgd-6BsY2AksIuFC4ByZt0l1BEKYudJGohveVwN7gcCDus2CKWjZF5gK-1dqybPftrqK39pcwg6h3eP1pGB-vc-Kz04J3mwn20Vgeo5kvUwq-jjmzk3wGhj7eI0Ic5xoz5ydjoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126245a760.mp4?token=gfHx9y49m65m7DvT9cYw6C2TOy6dxSQVl_1vLpywakj5mth3KTAjbLzwSxCuZDQAzi31KhrWgg0TL8VPSNBEBXB9rkFV0VwlcW7AXx5LYI6dyVutW8CZgjC-hutqHTW-bVE_aUDzn3KdFgx9hg7wgIdhVKZO5C9dQeEBUzCXzl7w4KSnsmnUeBOxJe_FOheHlM8FdT45pRjSE4QnKgd-6BsY2AksIuFC4ByZt0l1BEKYudJGohveVwN7gcCDus2CKWjZF5gK-1dqybPftrqK39pcwg6h3eP1pGB-vc-Kz04J3mwn20Vgeo5kvUwq-jjmzk3wGhj7eI0Ic5xoz5ydjoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أعدّ الجيش الإسرائيلي خطة واسعة النطاق وهامة تنتظر موافقة القيادة السياسية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76072" target="_blank">📅 21:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76071">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أعدّ الجيش الإسرائيلي خطة واسعة النطاق وهامة تنتظر موافقة القيادة السياسية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76071" target="_blank">📅 21:16 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
