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
<img src="https://cdn4.telesco.pe/file/nrpSN10HLcftzlyOmHlW0YFm-bAsj5Htns0A75yny8FP5OhbCqbNZSrqvorwEMnqnK1ABsOOkBIewo9qdTmfcdvTKEJlQRblYQjfEPI46OlhmAgZuzyP4RwUVAIP-RRucVwmCWcD8Sqn-vNNdEsPFD4tjdek8C0_69446Qo9dB2Nd5KNY2bnGOqVhEumt25eMjLuj2Yv_eZxqwPYYG08s8r4l4GOs2KN8ZWk86rsfYR_23eySVFpfq8rvmYncICNr0EejpG4oRwwJ4L3a_18BoN5pfi1TKomtV_Z2pFh5dYR89vd2ZAqZFvJrQjoOVw2TdPmj0mg8e-TfDQtmfmCVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 11:14:09</div>
<hr>

<div class="tg-post" id="msg-85336">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/naya_foriraq/85336" target="_blank">📅 11:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجارات البحرين</div>
<div class="tg-footer">👁️ 321 · <a href="https://t.me/naya_foriraq/85335" target="_blank">📅 11:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85334">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5ed4be62.mp4?token=SLVe9NJKmkDSG8a1aZ8cSU1R9pSShOhswnZy8U2DuglMMd3Lk7594HgRYFBGYppRi0rW5iPJ1DUm79fXQogVkqk7MESGJsQIFJCJo1qKW2Na9HPEFAnSCvVYZCyCV4qfuXGckyKuAbg6tXAX4kZ5vdpQPb2-s7yvCJnICWOki6hFPodIyDUmr8C9oMahkdBI_0jKsGvEDIz7v2bUyvrq_KnhBuKldbz4i44zk0p0jksVb-qH60j5_9R5SlAnrM3RPiRl5QEWTUkQOczlW21952pEagwQLO9IkXNiSUWp6yN_vxswknidZowbcDzZtwA-cUxEeqopi7xCPtNyevz4_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5ed4be62.mp4?token=SLVe9NJKmkDSG8a1aZ8cSU1R9pSShOhswnZy8U2DuglMMd3Lk7594HgRYFBGYppRi0rW5iPJ1DUm79fXQogVkqk7MESGJsQIFJCJo1qKW2Na9HPEFAnSCvVYZCyCV4qfuXGckyKuAbg6tXAX4kZ5vdpQPb2-s7yvCJnICWOki6hFPodIyDUmr8C9oMahkdBI_0jKsGvEDIz7v2bUyvrq_KnhBuKldbz4i44zk0p0jksVb-qH60j5_9R5SlAnrM3RPiRl5QEWTUkQOczlW21952pEagwQLO9IkXNiSUWp6yN_vxswknidZowbcDzZtwA-cUxEeqopi7xCPtNyevz4_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط اخر في إحدى مقرات حزب المعارضة الإيراني على طريق سيبيران - أربيل</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/naya_foriraq/85334" target="_blank">📅 11:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85333">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21767db47.mp4?token=GkpwmAKl_jtGqqujEhwrZSyYtrw7b_Sc-mhrAPVhSgUD_78LpZEi0C_VJRa2rVPmHKlLj2leQjQoeLN-V76d-FazcM7m7UejZaS33fzAOf6fYZeTyrbctAWOBFujOy4wePyXzg0LJcGvHkmAhd5ikzxemA0viPUl3prazRnqhyAFZF926V-Yj3rF6QuqoxdukiQ0QPPhBTKXoTwUXaktSRU-klo9Qz5rgEuofbKeBiWh1CG0MtkNlsCIfVI2kMtq4LWMX_nS3S2HV-C9ZoFJ44CVvpv6PmJtLwLiWQ9LY8hWlsy9aekslqopTMkRo3qk5CcLIN678kCSMPuu4EauCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21767db47.mp4?token=GkpwmAKl_jtGqqujEhwrZSyYtrw7b_Sc-mhrAPVhSgUD_78LpZEi0C_VJRa2rVPmHKlLj2leQjQoeLN-V76d-FazcM7m7UejZaS33fzAOf6fYZeTyrbctAWOBFujOy4wePyXzg0LJcGvHkmAhd5ikzxemA0viPUl3prazRnqhyAFZF926V-Yj3rF6QuqoxdukiQ0QPPhBTKXoTwUXaktSRU-klo9Qz5rgEuofbKeBiWh1CG0MtkNlsCIfVI2kMtq4LWMX_nS3S2HV-C9ZoFJ44CVvpv6PmJtLwLiWQ9LY8hWlsy9aekslqopTMkRo3qk5CcLIN678kCSMPuu4EauCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجارات في مخازن القنصلية الأمريكية في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/naya_foriraq/85333" target="_blank">📅 11:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85332">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مشاهد خاصة لنايا من داخل مطار أربيل الدولي حيث موقع الاستهدافات</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/naya_foriraq/85332" target="_blank">📅 10:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85331">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JirE_xGt2uK-zLFSbhTdo3t4qBPevWH-WKbbr06uKHxULlJHeZfeCA6V37YjPT_TAXbjYGyMGhNL0-oJMgDluzJ561V7dtJbtrGG7kyz8NIL3_9Cm5CfEMpVX8T2oBlgvnf01ujYr2DzpOkSGGttWzmwxNsL8AZy8z8jpIGOKYKtMBBJUzy6TEMDlLx0SQiqGU91maaTcYrgMaHhIvoB6h8SPtDqOZhhmOdlR7ieQQVMNDvBFuBxIMgdKpec0gETwyZHeI59Ribue7kCs3-oLRxGMIGsJn3QedmqYssbqmNuwvgEWq8BwPuWh-Y_uHT1iq0iUwhxGaTOZFU6jMj7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد خاصة لنايا من داخل مطار أربيل الدولي حيث موقع الاستهدافات</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/naya_foriraq/85331" target="_blank">📅 10:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85330">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/naya_foriraq/85330" target="_blank">📅 10:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85329">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فرانس برس: بدت عدة انفجارات يوم الجمعة بالقرب من مطار أربيل، الذي يستضيف قوات التحالف التي تقودها الولايات المتحدة في إقليم كردستان العراقي المتمتعة بالحكم الذاتي.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/naya_foriraq/85329" target="_blank">📅 10:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85328">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سقوط مباشر على موقع لحزب المعارضة الإيراني في منطقة ناحية رزكاري "توبزاوا" غرب محافظة أربيل ودوي انفجارات عنيفة في المكان.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/naya_foriraq/85328" target="_blank">📅 10:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85327">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">القنصلية الأمريكية موقع الاستهداف</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/naya_foriraq/85327" target="_blank">📅 10:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85326">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d440c579ec.mp4?token=oSnJW6u1DDTZSWreBj7Kjkd3rJn4WOXerQK-kMYBg4qVgCrwSfD6IqmWohGQ67kcjfjxcq5tMCtyHpnzmwU0zedTCKov9n9E0TAzJ5_rvKyt2DItTg9bWI5CTnzT0Dma7zYhPiApBmzBTb5RQApoDDsXQOqT921gzxB1zjy0CVS4f03OAZxVke9CZPp1RH_Ikm5dRt1AT2N2AVVMUuVW1Z1DfIunHr5C7rdXGpUN1jip23LENkHLKODgxSfwCRg-mYzMFnbbKL4_30IW1Obm3hJ9HPFPAtHWy7taRKO2Gv-zYlNARF0lx8FJa-dWriLlIt2xomYEWV8iUUwJBuSAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d440c579ec.mp4?token=oSnJW6u1DDTZSWreBj7Kjkd3rJn4WOXerQK-kMYBg4qVgCrwSfD6IqmWohGQ67kcjfjxcq5tMCtyHpnzmwU0zedTCKov9n9E0TAzJ5_rvKyt2DItTg9bWI5CTnzT0Dma7zYhPiApBmzBTb5RQApoDDsXQOqT921gzxB1zjy0CVS4f03OAZxVke9CZPp1RH_Ikm5dRt1AT2N2AVVMUuVW1Z1DfIunHr5C7rdXGpUN1jip23LENkHLKODgxSfwCRg-mYzMFnbbKL4_30IW1Obm3hJ9HPFPAtHWy7taRKO2Gv-zYlNARF0lx8FJa-dWriLlIt2xomYEWV8iUUwJBuSAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القنصلية الأمريكية موقع الاستهداف</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/naya_foriraq/85326" target="_blank">📅 10:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85325">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6818cf22b1.mp4?token=EGYst5_Rm5FBEfvFWk2CiKHuZKkZVVAzgxMLa5R7h9t-DxX8cxQkVBlAjp3iHYp5GcMdRLlGwfvfaG-qNNh7Fa7Np1ix1uQUeuN-S_w_6MkitlwXnXlvB6V0vbgp3OsJPZpU8ilA_iNxbyay6tjGraFi4KuqPXcl8bm4J14D_4uR39a9xRa1z4pYQyJ2SEarN0LiaXlnxt49VDblbWfX9EBdMJicxgl-k02BXWtszyy-o9nexW-15dO4a-JxCgDMWVHbI5JMfgdDehqz8gn-fNNYcUcNDNhMFXXwxqaYHwrqrPJx4f74xF7_qdTu06q57ENw-vpBBE1sm2OmLWVhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6818cf22b1.mp4?token=EGYst5_Rm5FBEfvFWk2CiKHuZKkZVVAzgxMLa5R7h9t-DxX8cxQkVBlAjp3iHYp5GcMdRLlGwfvfaG-qNNh7Fa7Np1ix1uQUeuN-S_w_6MkitlwXnXlvB6V0vbgp3OsJPZpU8ilA_iNxbyay6tjGraFi4KuqPXcl8bm4J14D_4uR39a9xRa1z4pYQyJ2SEarN0LiaXlnxt49VDblbWfX9EBdMJicxgl-k02BXWtszyy-o9nexW-15dO4a-JxCgDMWVHbI5JMfgdDehqz8gn-fNNYcUcNDNhMFXXwxqaYHwrqrPJx4f74xF7_qdTu06q57ENw-vpBBE1sm2OmLWVhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الأمريكية تحاول اعتراض المسيرات الإيرانية في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/naya_foriraq/85325" target="_blank">📅 10:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85324">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e49d25fd.mp4?token=WNoDuJQdvfBUbYK-wky4_gFN6bVR5PCox3z8btwKQb5FSan4W7xw6FBZIegdvKJ68L1dABhsz_cXh8AJ7KydKkEXBzJkQnqYdRt4Rmi-NtS1Gl_KTC_7atcfncy2YPykllli6w-qjvJeB35-ccwkhtXQbD6MU5M6bzLMASn4QhlttB2jHLr-Br1cf0q1te7s3Vm1b9-zJFOTJJkH3uL8D4jN_VP17U_AOi0ZjJbWPC_U73qVSi5qCKS_DpmO8BFXGwfZQrdqAPu9bZcCn1IoSc2XLD629ZEkIJJ4qedDRX8ZIbBg0MSKMX1Kpc3FHeYoHvBo-GPrLty6sH8puHN1WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e49d25fd.mp4?token=WNoDuJQdvfBUbYK-wky4_gFN6bVR5PCox3z8btwKQb5FSan4W7xw6FBZIegdvKJ68L1dABhsz_cXh8AJ7KydKkEXBzJkQnqYdRt4Rmi-NtS1Gl_KTC_7atcfncy2YPykllli6w-qjvJeB35-ccwkhtXQbD6MU5M6bzLMASn4QhlttB2jHLr-Br1cf0q1te7s3Vm1b9-zJFOTJJkH3uL8D4jN_VP17U_AOi0ZjJbWPC_U73qVSi5qCKS_DpmO8BFXGwfZQrdqAPu9bZcCn1IoSc2XLD629ZEkIJJ4qedDRX8ZIbBg0MSKMX1Kpc3FHeYoHvBo-GPrLty6sH8puHN1WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط مباشر على موقع لحزب المعارضة الإيراني في منطقة ناحية رزكاري "توبزاوا" غرب محافظة أربيل ودوي انفجارات عنيفة في المكان.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/naya_foriraq/85324" target="_blank">📅 10:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85323">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سماء مدينة أربيل تكتظ بالمسيرات الإيرانية التي اتخذت من مقرات حزب المعارضة الإيرانية أهدافاً لها.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/naya_foriraq/85323" target="_blank">📅 10:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85322">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7763e1bcd2.mp4?token=odRKM8wUMp_N3riZsOcQiGaTOWMo6xIbQvHZdu263nqisLf1uY3i47r9wR9DWGa_c_KYrD1e7kIoPg-SNozqKoidgGU5o3lQxS-4TWXF3amECIG4cRe8BoZnjuvcbk_1iMJIs_PQ9L_faW7XfY4RYN188tAcMJK8KXdhwiH6aju2hhjj5Vdq_oiJTg8lI9XUpGbr-AocwJz-rAZgRRMsp3R1-q5aQLvbr0B6ZODGFY4TgTZFcY-z15rq16ypdAq03O_pDeAYId5Ap98s34VS9A0qVhmlOY4fFq9lTu5ppgVN-D1wsuUdPEr1PTyiY9ZlHodF-QzXRIM15dyuT1GFQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7763e1bcd2.mp4?token=odRKM8wUMp_N3riZsOcQiGaTOWMo6xIbQvHZdu263nqisLf1uY3i47r9wR9DWGa_c_KYrD1e7kIoPg-SNozqKoidgGU5o3lQxS-4TWXF3amECIG4cRe8BoZnjuvcbk_1iMJIs_PQ9L_faW7XfY4RYN188tAcMJK8KXdhwiH6aju2hhjj5Vdq_oiJTg8lI9XUpGbr-AocwJz-rAZgRRMsp3R1-q5aQLvbr0B6ZODGFY4TgTZFcY-z15rq16ypdAq03O_pDeAYId5Ap98s34VS9A0qVhmlOY4fFq9lTu5ppgVN-D1wsuUdPEr1PTyiY9ZlHodF-QzXRIM15dyuT1GFQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة انقضاض الطائرة المسيرة على هدفها في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/naya_foriraq/85322" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85321">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a91a7bc7d.mp4?token=ThdUJhKd1lg-S_0tdhY8JdE8qaXLVXToFCqBWrfLOStNjAXuaShAFZGCo2QSJVc0oxw_XJY1UYQ2rN8rAWAbtJSA4sMbPlYpfAyseKf4jw6rk1g7TbSW8eglsrSJ5QiiZHKbH2PvyPR4WksWbGUIwqImxZDmEXdEeblWey3SldBlBYX9XdyBA-35n1Ew6M8VrJvbcBnhcIs63y_G4uiNCTdGhZuuhC8kdcfkgjh3Q_uUC1tuKfj5FG0UwMfKsECY-IbiQ6kPiJbF2ZFiC3xNnIGWBMmcj5VtVdkqaIJJe3IZpLnCfQG3oxMHcTuXauhue_oQHRbm7eyQOHT4nNO9TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a91a7bc7d.mp4?token=ThdUJhKd1lg-S_0tdhY8JdE8qaXLVXToFCqBWrfLOStNjAXuaShAFZGCo2QSJVc0oxw_XJY1UYQ2rN8rAWAbtJSA4sMbPlYpfAyseKf4jw6rk1g7TbSW8eglsrSJ5QiiZHKbH2PvyPR4WksWbGUIwqImxZDmEXdEeblWey3SldBlBYX9XdyBA-35n1Ew6M8VrJvbcBnhcIs63y_G4uiNCTdGhZuuhC8kdcfkgjh3Q_uUC1tuKfj5FG0UwMfKsECY-IbiQ6kPiJbF2ZFiC3xNnIGWBMmcj5VtVdkqaIJJe3IZpLnCfQG3oxMHcTuXauhue_oQHRbm7eyQOHT4nNO9TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موقع الانفجارات داخل مقر حزب المعارضة الإيراني</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/naya_foriraq/85321" target="_blank">📅 10:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85320">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8443be5d06.mp4?token=BHGlWd2zwNEXMQ4DdwsfmQTl_k-cUlppaCcxTUro9s6XZPegApb9WtB0tEZqMDKPgnDZiLKE-F5B2QH1kqaR1KdtZD5yEIsd4lGERI03k8mCASFNmrmTbK-cO0QzLTolZSg91RDC_2o1zKjjnN0i_nidnGVjEk-lhegTl_E_M8llm2LNmAoZFnfht7EqSe_UZ0pczLDi_zozhErGpJE31Ei1zQEEjkzI1CoU5RMNzB8bdCdisdj0HSNo3nhukbUQ39gH3cYg_DElCTaADrRS12eCCxMTsaX_k2KX-hzqpx2BG0OcEB7z4S3InltfcJqnz0SLRwXp6IU_WN3r5mcVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8443be5d06.mp4?token=BHGlWd2zwNEXMQ4DdwsfmQTl_k-cUlppaCcxTUro9s6XZPegApb9WtB0tEZqMDKPgnDZiLKE-F5B2QH1kqaR1KdtZD5yEIsd4lGERI03k8mCASFNmrmTbK-cO0QzLTolZSg91RDC_2o1zKjjnN0i_nidnGVjEk-lhegTl_E_M8llm2LNmAoZFnfht7EqSe_UZ0pczLDi_zozhErGpJE31Ei1zQEEjkzI1CoU5RMNzB8bdCdisdj0HSNo3nhukbUQ39gH3cYg_DElCTaADrRS12eCCxMTsaX_k2KX-hzqpx2BG0OcEB7z4S3InltfcJqnz0SLRwXp6IU_WN3r5mcVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع أعمدة الدخان من موقع سقوط المسيرات الإيرانية قرب مطار أربيل شمال العراق</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/naya_foriraq/85320" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85319">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae715a6f35.mp4?token=nMWYrK6ntoK_Hp3P6FnssNwcQ1l9tI9BeGP4G_I4qLJ1E75cuKpbtpyO97h8U2-aOIPKBL2isViPK1Vcd6DZC1A0g4cdWI5jFs8HVNjqYNpuL15u7TXwdfepXFDAPQSQQhsWAU-RDXmWfe6dcfaUPllBZzXbjTbqbltX838PtTKhfN2TfX7qNsjJ2JMzUBNNi8E9lU-fiQL_UOYwNfNnl7Fz2I4QrTdUs4QqGLYKidNOOx5ELB3N97vxgcTFq418beR9tBYjyU7P7wJJ4pmz_PfvJg0VzKmTSQc8StNH1SBhAsvL6Qlxrg8-d9jgCgFDAlkGIFNy4B-dLR6REraStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae715a6f35.mp4?token=nMWYrK6ntoK_Hp3P6FnssNwcQ1l9tI9BeGP4G_I4qLJ1E75cuKpbtpyO97h8U2-aOIPKBL2isViPK1Vcd6DZC1A0g4cdWI5jFs8HVNjqYNpuL15u7TXwdfepXFDAPQSQQhsWAU-RDXmWfe6dcfaUPllBZzXbjTbqbltX838PtTKhfN2TfX7qNsjJ2JMzUBNNi8E9lU-fiQL_UOYwNfNnl7Fz2I4QrTdUs4QqGLYKidNOOx5ELB3N97vxgcTFq418beR9tBYjyU7P7wJJ4pmz_PfvJg0VzKmTSQc8StNH1SBhAsvL6Qlxrg8-d9jgCgFDAlkGIFNy4B-dLR6REraStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لحظة السقوط</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/naya_foriraq/85319" target="_blank">📅 10:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85318">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e2fdd71e2.mp4?token=QOBWiWTYtcNgvxwEgapkqHbeLUxGdM7WgJiCJPy6b5yAaOJ9syZDLAVqoRP936SEcFEM3kEtqzzY4WahkqoligtRTYPj8dvCn7v213NMJWCyJzPitwJy2riaeLKYhWzaH6D85jWLE1qlN6wJOGiN_ETF_-Ygd8diYhmSuoNG-wGH8MnFu442tW4yx3peuQJDkO4aBHhrPl7uj6pJRG_OoZIODTq6rNgD0pWKpcDd7nEclqrSIGRuZZMHOOIL_tPfjv1GOf-eR4U0ZGfnmTdWqcn6SFpHN6knTuWcR_i8HdKR5OrlT7XGjMnRzfyKiaqrMSRoOJ4gLclqc3jbExc-iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e2fdd71e2.mp4?token=QOBWiWTYtcNgvxwEgapkqHbeLUxGdM7WgJiCJPy6b5yAaOJ9syZDLAVqoRP936SEcFEM3kEtqzzY4WahkqoligtRTYPj8dvCn7v213NMJWCyJzPitwJy2riaeLKYhWzaH6D85jWLE1qlN6wJOGiN_ETF_-Ygd8diYhmSuoNG-wGH8MnFu442tW4yx3peuQJDkO4aBHhrPl7uj6pJRG_OoZIODTq6rNgD0pWKpcDd7nEclqrSIGRuZZMHOOIL_tPfjv1GOf-eR4U0ZGfnmTdWqcn6SFpHN6knTuWcR_i8HdKR5OrlT7XGjMnRzfyKiaqrMSRoOJ4gLclqc3jbExc-iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار المحاولات الفاشلة للتصدي للطيران المسير</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/naya_foriraq/85318" target="_blank">📅 10:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85317">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dfa85ff76.mp4?token=tREviDV0oa9U2N1rR1eLjnqNK9MwKkit2nM4JW2bvoWDevNnWdIrodHyKrisclKNxnR8ItILofjL3FWsRU2aYZoYSCZbEF7fB5H-hzkbuhOA3o4tUipDyNHPbCiX0UPUYenCYtbqJo0KZGKc-OaupV5FpPfl7tT-wpjkhILQJJOT7a62dcVgnvJmopLEBLQIAmQ7bGnfqFqnMutm7hp8ekxy4D8HrWc0CmvmYWo2wIXxrNqmTt2YNEUhE-KbbVhPCivP911Q1T1hLHjiLIBe6r7aVA_CqqoLl9uyJrqmr70V-kHHgmlrlIES1xJUnHG43lo2u9jHlCTz8wJLY3Mu4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dfa85ff76.mp4?token=tREviDV0oa9U2N1rR1eLjnqNK9MwKkit2nM4JW2bvoWDevNnWdIrodHyKrisclKNxnR8ItILofjL3FWsRU2aYZoYSCZbEF7fB5H-hzkbuhOA3o4tUipDyNHPbCiX0UPUYenCYtbqJo0KZGKc-OaupV5FpPfl7tT-wpjkhILQJJOT7a62dcVgnvJmopLEBLQIAmQ7bGnfqFqnMutm7hp8ekxy4D8HrWc0CmvmYWo2wIXxrNqmTt2YNEUhE-KbbVhPCivP911Q1T1hLHjiLIBe6r7aVA_CqqoLl9uyJrqmr70V-kHHgmlrlIES1xJUnHG43lo2u9jHlCTz8wJLY3Mu4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة سقوط الطائرة المسيرة في أحد مقرات حزب المعارضة الإيراني الإرهابي</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/naya_foriraq/85317" target="_blank">📅 10:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85316">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e2077859.mp4?token=SkoMH_q2aPf8zRTFBtXoX0R5xGdk4Ow2qesnpv_Z4i5fJ95w068RhEaAUAMgM8fEkhPIsBU8QS7jMxHNhzmmMsH8kRsWEFFGyPyTDOU77r66ATW7IUuUYqYotztfI_E0WwTK20z6P3Js2iGs20TPVGldzHCkeqUlCXf0O_dlgrrR8WuaulQis_U6kO-nUkyFwk82wmvZyzK_K6lSmiDlLjvsUl6qgVXwfqyRSP6c_Vmh2_10B1OcS4MUaM19dEvYJyFlXX6rrDKOtpA9V6pgtUqYpdxixjlKgRHbBiqnfBTh6fwxf8zP5-5mZSgWNp7p0SK5SV5Gbuq0juyGmx9zHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e2077859.mp4?token=SkoMH_q2aPf8zRTFBtXoX0R5xGdk4Ow2qesnpv_Z4i5fJ95w068RhEaAUAMgM8fEkhPIsBU8QS7jMxHNhzmmMsH8kRsWEFFGyPyTDOU77r66ATW7IUuUYqYotztfI_E0WwTK20z6P3Js2iGs20TPVGldzHCkeqUlCXf0O_dlgrrR8WuaulQis_U6kO-nUkyFwk82wmvZyzK_K6lSmiDlLjvsUl6qgVXwfqyRSP6c_Vmh2_10B1OcS4MUaM19dEvYJyFlXX6rrDKOtpA9V6pgtUqYpdxixjlKgRHbBiqnfBTh6fwxf8zP5-5mZSgWNp7p0SK5SV5Gbuq0juyGmx9zHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات فاشلة لإسقاط المسيرات الإيرانية قبل وصولها نحو أهدافها في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/naya_foriraq/85316" target="_blank">📅 10:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85315">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2984d00b0.mp4?token=bZ202GO5GiuWDbv4Oy1JifbKc_aso910Lkxz6Psd44odJPN4YeYzmqQYZSI3qlwmgXyT8mYUpE8QkFFf4ReF5bbEdUcDjNfxYxM7Nh6k3SOQBKk8CLwB838oyMUlMlK6GuUnMMna2AirdnlPQAvSmGfR9tF2vev3ZP-9tQdXdRbLL_dffEzrOjQVYeXnTXJDMxOmvvTETXpYdr4sWmoLt8FitRE9G35CiCKO1SxQ5FCNqpxozSCZ47r-momLVk9BuLhthUB2LrwGtcODeoImt-emnh40RVzAl1ztzUfKqWLvmcJ5UGcQMtt9zFaDUq5Y_-WhBpGTaYShzPf3bONFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2984d00b0.mp4?token=bZ202GO5GiuWDbv4Oy1JifbKc_aso910Lkxz6Psd44odJPN4YeYzmqQYZSI3qlwmgXyT8mYUpE8QkFFf4ReF5bbEdUcDjNfxYxM7Nh6k3SOQBKk8CLwB838oyMUlMlK6GuUnMMna2AirdnlPQAvSmGfR9tF2vev3ZP-9tQdXdRbLL_dffEzrOjQVYeXnTXJDMxOmvvTETXpYdr4sWmoLt8FitRE9G35CiCKO1SxQ5FCNqpxozSCZ47r-momLVk9BuLhthUB2LrwGtcODeoImt-emnh40RVzAl1ztzUfKqWLvmcJ5UGcQMtt9zFaDUq5Y_-WhBpGTaYShzPf3bONFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرب من الطيران المسير يتجه نحو مقرات حزب المعارضة الإيراني الإرهابي</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/naya_foriraq/85315" target="_blank">📅 10:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85314">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087ee61fb.mp4?token=r9lFKcJHjsmwQvSxq-JgaDOY1WYkOFrV606ARLk2RWSRYeCy6Y067wZePKBEEizt9Ju8u3E3O3lWhoHN_pKj2X9P4mUZcNLL1vXGDMoWuHzTDcHJYTjQAVUHcf4J8Ra93uryQmTfIJxtHw_0y-wEiV74crbENnirYYzYsIIbJr8pyOu4iW0LeKxMSGXrmEI1UGDbY2QmWf0x1jngoj4r_EHreM4bBYci134riWnRczhe8_j8hg-cojpOQVzJYRmnm8KshpahyMDc4xwxEJxsbjCAb2cdEmwnFioDWfcb4WfJKWrqgwB8cA0G-hObZnhyqi9nEyMg91g9hcT676DqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087ee61fb.mp4?token=r9lFKcJHjsmwQvSxq-JgaDOY1WYkOFrV606ARLk2RWSRYeCy6Y067wZePKBEEizt9Ju8u3E3O3lWhoHN_pKj2X9P4mUZcNLL1vXGDMoWuHzTDcHJYTjQAVUHcf4J8Ra93uryQmTfIJxtHw_0y-wEiV74crbENnirYYzYsIIbJr8pyOu4iW0LeKxMSGXrmEI1UGDbY2QmWf0x1jngoj4r_EHreM4bBYci134riWnRczhe8_j8hg-cojpOQVzJYRmnm8KshpahyMDc4xwxEJxsbjCAb2cdEmwnFioDWfcb4WfJKWrqgwB8cA0G-hObZnhyqi9nEyMg91g9hcT676DqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد أعمدة الدخان قرب مطار أربيل الدولي</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/naya_foriraq/85314" target="_blank">📅 10:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85313">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866d7491f9.mp4?token=o7c_d_Tq4Vx8D6UQsVFsYs6hQgOCXVy1MHvrvIyCSMcMlnt5O6pNSM4_foNhcnP8jphyq_rhow1x_QCtikJo3Lyj4kSo8WrPEsl5vJW31fZYWbOUuKZIcdryGlGCR43Csu__u4HW9pULipDkZyRMaT6G1IKS6vzNm7WX656uR2Q6q1ENAJcIvYD-to4YadGv0BAaHix--HfV0POfZoiWUcE1bc7pZ5urEn5RA1Iv40lj6P0gSmW-AjTUVfHvY60MJ8iAK-hIHAQlnJbPS3-aWjke90PT1foQNwnMcV-98oDxqO56Fg24FXetpZXw9TBcmjxq36CQmIIjJQSVrUFiBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866d7491f9.mp4?token=o7c_d_Tq4Vx8D6UQsVFsYs6hQgOCXVy1MHvrvIyCSMcMlnt5O6pNSM4_foNhcnP8jphyq_rhow1x_QCtikJo3Lyj4kSo8WrPEsl5vJW31fZYWbOUuKZIcdryGlGCR43Csu__u4HW9pULipDkZyRMaT6G1IKS6vzNm7WX656uR2Q6q1ENAJcIvYD-to4YadGv0BAaHix--HfV0POfZoiWUcE1bc7pZ5urEn5RA1Iv40lj6P0gSmW-AjTUVfHvY60MJ8iAK-hIHAQlnJbPS3-aWjke90PT1foQNwnMcV-98oDxqO56Fg24FXetpZXw9TBcmjxq36CQmIIjJQSVrUFiBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجارات قرب مطار أربيل الدولي</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/naya_foriraq/85313" target="_blank">📅 10:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85312">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجارات تهز محافظة أربيل مجدداً</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/naya_foriraq/85312" target="_blank">📅 10:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85311">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات تهز أربيل</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/naya_foriraq/85311" target="_blank">📅 10:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85310">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4169cd22.mp4?token=CXFYctgnll5camVM1Qs5_pXi8XPRKYFG200c7LDUN1_GkFt30Z2XkfLz9GWSsSR-DbTGmixlpIRhgDymDxq_jO4tlGgOGyhxjbco8AJUZ-_WiZdllRjUB5ySfKe2lpuMLtyNRJY1szP6_feZEbzk_Sspo-LQ-TOCJt4FBn50I0D_LCd8XR9bcYlK-0a-odn5-a-12okIQTWnYlg6uRVLI-XqEItBo3Gj3tlVErFZzgpKCJNY5oOSauniSVF4RrkKLjuIwWp1qtuNNBDOXkHoOERNEoyn5nwn4JJVvfPDGkkPGpNXpUnxyXV0oTQuRaHU5J1q7uKgHys8RB9PtV3XYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4169cd22.mp4?token=CXFYctgnll5camVM1Qs5_pXi8XPRKYFG200c7LDUN1_GkFt30Z2XkfLz9GWSsSR-DbTGmixlpIRhgDymDxq_jO4tlGgOGyhxjbco8AJUZ-_WiZdllRjUB5ySfKe2lpuMLtyNRJY1szP6_feZEbzk_Sspo-LQ-TOCJt4FBn50I0D_LCd8XR9bcYlK-0a-odn5-a-12okIQTWnYlg6uRVLI-XqEItBo3Gj3tlVErFZzgpKCJNY5oOSauniSVF4RrkKLjuIwWp1qtuNNBDOXkHoOERNEoyn5nwn4JJVvfPDGkkPGpNXpUnxyXV0oTQuRaHU5J1q7uKgHys8RB9PtV3XYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المسيرات بطريقها نحو محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/naya_foriraq/85310" target="_blank">📅 10:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85309">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9a9da2df.mp4?token=WDK9QWtghdntx2NXY5WQSnk_Qknoh1-nc5yQeKh8guCbhM4iSvqE3xpPHesowgW_wyEL-0-Yk6YVJouKk_v-Co5PxmOu8gjSVxg2wsq0316ic5QR9vBBAd2pQiRQMUqSc8Kg0Zu7yjA6NUr3C1z3QlpSW5rvNlws18JdeU9mwhYenMqhHdyNOj6s90v3FHeB57WkvrWweem487A9mDkiPbLvKz4GrxKG4OVwl5ohXxh5quiJyVPzkSxoz1aWvOm9LhGvH6yqv9IGJIHxUTZ8lhS16umFIbPcEq-bH6_WrJWT-eTCA3c6cXN2_Grb_ZoM-QB3xhTIx7rdiuG2HWB27Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9a9da2df.mp4?token=WDK9QWtghdntx2NXY5WQSnk_Qknoh1-nc5yQeKh8guCbhM4iSvqE3xpPHesowgW_wyEL-0-Yk6YVJouKk_v-Co5PxmOu8gjSVxg2wsq0316ic5QR9vBBAd2pQiRQMUqSc8Kg0Zu7yjA6NUr3C1z3QlpSW5rvNlws18JdeU9mwhYenMqhHdyNOj6s90v3FHeB57WkvrWweem487A9mDkiPbLvKz4GrxKG4OVwl5ohXxh5quiJyVPzkSxoz1aWvOm9LhGvH6yqv9IGJIHxUTZ8lhS16umFIbPcEq-bH6_WrJWT-eTCA3c6cXN2_Grb_ZoM-QB3xhTIx7rdiuG2HWB27Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز أربيل</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/naya_foriraq/85309" target="_blank">📅 10:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85308">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d21a3bd60.mp4?token=parmSU16D9-Xafr3CDnUGUJ6KMSxkIlPY0EJkzKwfWr2-Qhu1QMARRIO8S24CPjERai5OBm_OPs02KTN9-fyBqVtgXMLMWMKNGS2U7WQhFyXMG1i-HQJk4hUP9MXIZuJcZUtsKWqv8Q05yg2Nf5Rpoq2MoEQdq4A6-HMsQIDuhlG3r2zRxRefGrYbSr7EeoVgOE11okewsq3H1dI-CxKXLWJ8kNWxpRLjyBT9s0tfnF1hynHKlfBSm3N3ryaHYSDtDYUNlHykVmdcZzlXKPvswAaUrox9q_KotSNt1KB8q0fgp-XSbQOUaN1YT7d7n0sthp7-Cwgmh6k1PQbrc5dEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d21a3bd60.mp4?token=parmSU16D9-Xafr3CDnUGUJ6KMSxkIlPY0EJkzKwfWr2-Qhu1QMARRIO8S24CPjERai5OBm_OPs02KTN9-fyBqVtgXMLMWMKNGS2U7WQhFyXMG1i-HQJk4hUP9MXIZuJcZUtsKWqv8Q05yg2Nf5Rpoq2MoEQdq4A6-HMsQIDuhlG3r2zRxRefGrYbSr7EeoVgOE11okewsq3H1dI-CxKXLWJ8kNWxpRLjyBT9s0tfnF1hynHKlfBSm3N3ryaHYSDtDYUNlHykVmdcZzlXKPvswAaUrox9q_KotSNt1KB8q0fgp-XSbQOUaN1YT7d7n0sthp7-Cwgmh6k1PQbrc5dEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحليق طائرات مسيرة في سماء العراق باتجاه محافظات شمال العراق.</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/naya_foriraq/85308" target="_blank">📅 10:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85307">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
تحليق طائرات مسيرة في سماء العراق باتجاه محافظات شمال العراق.</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/naya_foriraq/85307" target="_blank">📅 10:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85306">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0b918738f.mp4?token=UBtU6BAqC_cbEolikc6iubP72OOr7nD0DO1JCPtU49FI5jrwDSsoyc1Q-X9mblKBQvLr5BoyT0944fJTk9T2EeJwrwjvgx7PJgVxIhG2gYHduRlGhKzpp7U7bSgHeBuXxC-Gh9LopV4QSI756oqeXYcrZ-vkXKDGVDvPc7NwOaGCXyT_JAuaXD3fduCHCGuhZKAaOlamHOssAF62kEOpZTvr2lq7ne3gquTKPUPZotUPkAD2MEMcO6Ipfcz4N9wJsONBxHg2bojOFKfy4bDxBcY-wuOzO2bSUuFr4TYojdVJ5udcp51M1yY2uGtxRCCfcFRezd4osMa3AK8_CK3zdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0b918738f.mp4?token=UBtU6BAqC_cbEolikc6iubP72OOr7nD0DO1JCPtU49FI5jrwDSsoyc1Q-X9mblKBQvLr5BoyT0944fJTk9T2EeJwrwjvgx7PJgVxIhG2gYHduRlGhKzpp7U7bSgHeBuXxC-Gh9LopV4QSI756oqeXYcrZ-vkXKDGVDvPc7NwOaGCXyT_JAuaXD3fduCHCGuhZKAaOlamHOssAF62kEOpZTvr2lq7ne3gquTKPUPZotUPkAD2MEMcO6Ipfcz4N9wJsONBxHg2bojOFKfy4bDxBcY-wuOzO2bSUuFr4TYojdVJ5udcp51M1yY2uGtxRCCfcFRezd4osMa3AK8_CK3zdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحليق طائرات مسيرة في سماء العراق باتجاه محافظات شمال العراق.</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/naya_foriraq/85306" target="_blank">📅 09:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85305">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇱
إصابة ضابط الأمن الصهيوني ميؤوس منها.</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/naya_foriraq/85305" target="_blank">📅 09:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85304">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj3vDUU-7CO0kBcDvH233gK1Rt-5qp9J72iyT5dyAqE-hWV7Za7mJDZSooZjNPjQzBYW29I7VfNri3xS9dyM0B1lNcRYpHiWI2rO6eS02lI2O49KxnJ3H2ryJ0Z2zL_xK1C5b6ebkFbLmN4lBWj-Noswds0EduF41_J3gGEcM44vwgdhwKCXe8e7VqajKeMWHXFJ3kY651Jbbc6s-Vf9y12BX-aaALtjiRqiaGUg2GbQZYlKYDOzFtPQbWsPlbIUHOBBwfun6-l8y9alXJcl7LLd0F99bMMWr4EOD38dx-D5PPpUIrncHM-_7gSGgWHNan1rVOZSVfVLGDh0DjVc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إعلام إيراني: دوي انفجارات قرب مدينة پیرانشهر شمال غرب إيران</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/naya_foriraq/85304" target="_blank">📅 09:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85303">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ارتفاع عدد الإصابات إلى 5 بينهم ضابط وحارس للمستوطنين في عملية إطلاق النار قرب نابلس.</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/85303" target="_blank">📅 09:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85302">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc6a72ec2.mp4?token=vfJYWnf9V5r5x1UIa3ES8JY99yCBEeiqON1PWsztSM3Fx9ETnUzasUpcH-EfQe6KofDFaajec57MTBaBXsWMJ57mOO93-pesfAkqL3ENvVOv4G_VfPXaxugTOzg6Q0r3jtca8mMGyZbIlPTq4zVM4Wqfnc_P7GjOvUiSJR0iL7SW-jqibEimAvIpJUN1OBA_0BaTIG__X5mA0MdGzwNpAL3G5mxhEf1Q5c06Gw1nTHvpjp2KqySCUE_4xFpTlPvMJ25Dvp3k_8aIHE4fzFQs-tyZGhQGrqJduF-GInx26MydNtvieVlHxEjVHCZflh5Oo0Q-s7ZY-8zh_XK1ZyBQ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc6a72ec2.mp4?token=vfJYWnf9V5r5x1UIa3ES8JY99yCBEeiqON1PWsztSM3Fx9ETnUzasUpcH-EfQe6KofDFaajec57MTBaBXsWMJ57mOO93-pesfAkqL3ENvVOv4G_VfPXaxugTOzg6Q0r3jtca8mMGyZbIlPTq4zVM4Wqfnc_P7GjOvUiSJR0iL7SW-jqibEimAvIpJUN1OBA_0BaTIG__X5mA0MdGzwNpAL3G5mxhEf1Q5c06Gw1nTHvpjp2KqySCUE_4xFpTlPvMJ25Dvp3k_8aIHE4fzFQs-tyZGhQGrqJduF-GInx26MydNtvieVlHxEjVHCZflh5Oo0Q-s7ZY-8zh_XK1ZyBQ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار كثيف لجيش الاحتلال في موقع الحدث الامني</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/85302" target="_blank">📅 09:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85301">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8475162e28.mp4?token=VNl_HQ3u5by4Z3y0sd1bFM3TST9KjGWSZF7jpnlgwkzl_dYntOXLecCdoII1kSDgBUiBI1CJklK58Ac_dKRIY2Gu5lI6GOY9eJKY5knhzhJAheQkL-2NanSDaGlLxslQmcuGWABbXDBjPAAk09KAstNXTTrtAvGh7g0WuYFZhMsASnv5IDLaQuPxu17kMYgRYicXSnq7KEtY9uy0x_rllenYBKzrcFHqcr1dsgL9Upj-PENnVJsxQPAR01P69EbtNWWKVJ6fH3_OS4Uv7kRmxbhKZuChKQFtnaL5cBjDsYj2af318OH60ZfhVSFwfCBzbwFCzqsIVCJe1dgmh7d0KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8475162e28.mp4?token=VNl_HQ3u5by4Z3y0sd1bFM3TST9KjGWSZF7jpnlgwkzl_dYntOXLecCdoII1kSDgBUiBI1CJklK58Ac_dKRIY2Gu5lI6GOY9eJKY5knhzhJAheQkL-2NanSDaGlLxslQmcuGWABbXDBjPAAk09KAstNXTTrtAvGh7g0WuYFZhMsASnv5IDLaQuPxu17kMYgRYicXSnq7KEtY9uy0x_rllenYBKzrcFHqcr1dsgL9Upj-PENnVJsxQPAR01P69EbtNWWKVJ6fH3_OS4Uv7kRmxbhKZuChKQFtnaL5cBjDsYj2af318OH60ZfhVSFwfCBzbwFCzqsIVCJe1dgmh7d0KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع عدد الإصابات إلى 5 بينهم ضابط وحارس للمستوطنين في عملية إطلاق النار قرب نابلس.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/85301" target="_blank">📅 09:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85299">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f981a4cfa.mp4?token=GQc54hk0NfVN7J0lBH5PaizjkGPIqaWrUTMCYEMwRNbR-Jbsph5PdX4xdnRtISPbS_KOlxdXvT4zXif3e4fVatiBwNJSuameGMVU0d9zRRX6E5nGKAB8NQ-UMQD4Asgg1ePAJoQrd2Bu6vG78_2wUnhIvtouI4a4tkghV0PrMG-pc3B_qx4W0s73EXqLmLPHv16FnHAIgseXwB8hWZ8CFzMgKuilo0yZPbN-ffx1xMXpX3Wtz69jgZBNXd66mI_YzuygNUPHkjEVNBm2ANVOL93R1XG-tscYeH2XJA4tdZ3gk4iGpNhglOkjsy1SP0vPylzRMT8uvSzpSLsjo_k7cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f981a4cfa.mp4?token=GQc54hk0NfVN7J0lBH5PaizjkGPIqaWrUTMCYEMwRNbR-Jbsph5PdX4xdnRtISPbS_KOlxdXvT4zXif3e4fVatiBwNJSuameGMVU0d9zRRX6E5nGKAB8NQ-UMQD4Asgg1ePAJoQrd2Bu6vG78_2wUnhIvtouI4a4tkghV0PrMG-pc3B_qx4W0s73EXqLmLPHv16FnHAIgseXwB8hWZ8CFzMgKuilo0yZPbN-ffx1xMXpX3Wtz69jgZBNXd66mI_YzuygNUPHkjEVNBm2ANVOL93R1XG-tscYeH2XJA4tdZ3gk4iGpNhglOkjsy1SP0vPylzRMT8uvSzpSLsjo_k7cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
إصابات خطيرة في عملية إطلاق النار قرب نابلس.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/85299" target="_blank">📅 09:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85298">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇱
جيش الاحتلال: إطلاق نار بالقرب من منطقة مزرعة جلعاد التفاصيل قيد المراجعة</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/85298" target="_blank">📅 09:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85297">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇱
حدث أمني في منطقة مزرعة جلعاد</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/85297" target="_blank">📅 09:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85296">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇱
حدث أمني في منطقة مزرعة جلعاد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/85296" target="_blank">📅 09:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85295">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
إعلام أمريكي: أحد أفراد فريق الحماية الخاص بنائب الرئيس الأميركي متهم بتعريض معلومات حساسة للخطر</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/85295" target="_blank">📅 08:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85294">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
محافظة خوزستان: لم تقع أي عملية قصف صاروخي من قبل العدو الإرهابي الأمريكي على مدينة خرمشهر في الليلة الماضية.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/85294" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85293">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇱
هارتس العبرية: في "إسرائيل" يجدون صعوبة في فهم شخصية خامنئي الإبن (السيد مجتبى)</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/85293" target="_blank">📅 08:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85292">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">4 انفجارات تهز قاعدة عيسى الجوية في البحرين</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/85292" target="_blank">📅 08:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85291">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/85291" target="_blank">📅 08:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85290">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/85290" target="_blank">📅 08:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/85289" target="_blank">📅 08:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85288">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyYovb50YgxAYp0EocrubXYbk_FzfiSJlMa6CyI91xygiqvmSz4Dh466lCC4ypO9JbuAAgAexnyko9F3RDeUmWJnauOUn9nGQUoLUbw8r9R3Tk8Js8-KUUtd7aFzfPEfNRM_BlCMsXbCYGxG62K1YWGAsia0eE9fX9lRDy5hP8ph8g3g-1-RxUkYgJvfHVkfvprpoKwKd32ZLuboO-u1inrdZ94GGygEhRkXGxvbjkOba69Y0SMgjmQ9-qZTvFoEYKVqeH00V_n9ZqOg9h4b-A_SWFS8TeCpZGdk5_zKWxTHGFAicV3RIrcYpt1r8c80ugJQGMEt75tlFk3CyTU0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/85288" target="_blank">📅 08:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85287">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات في مقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/85287" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85286">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/85286" target="_blank">📅 07:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85285">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX3Z_ZpVkzIPS4NEESdlbhsLBV0uXrwlFjXm5WbxX7p5T5n5ZDzsnsyiYDp_RDbUuJ8M3SJunMKR2znF0RWDHXjWJdJxid1igflo5eUv70P-fY_CJK-JhB9pra5rme3fyNIWT-tje3IwUkwoFhpM5uS3qPEIcbwdAVbCMnRxctoZ0AeFkRGvvMqUQqcHHfC5W-qS5DKCfhSWHHyElJOz8X5Mi624t7kaDj38EwF2nKjPfvozEve0gT4plbrgo2wk5PUlKUgU_EXTEL1uTjVMrGmCLCUZMGdxCa52D6aWn3p_jOF6a7SHBdR_svPilSp1A7t7e1BrfqeMypWqAFrXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفارات الإنذار تدوي في البحرين نتيجة هجوم صاروخي إيراني</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/85285" target="_blank">📅 07:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏وول ستريت عن مصادر:  استمرار الحرب مع إيران يترك آثارا شخصية على ترمب ودائرته المقربة</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/85284" target="_blank">📅 06:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85283">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6b49a5ef.mp4?token=gvUj784kXNuWr9FyhbvAj3jiuTAN7bHp3fmyxSIeC_JpaIWuSRC7Umkd5397XoQq1OwPQv1HwmcDCHfL7lP9af6W6cl-9prNv7FmSqazmngo32sD0dvGcObtAYJFsJcL4YyaSJJMqycgjGfuhcI8-qapn9eKX6lL1nVnPrd8m2rk7QO5j_34H65ZvP7e0WvVDHSQyezNgHtu6WvJ7QEa9AsdU4VrZewJredqvMAS01zq1wMBMMYXoCf7MdO2Kd4w9jXGuSs3t2yDGkCOb2OmmVDBllgBZBjJQaTnO6kDFUK2a3rPlLYzRnAGLlaER2B93_ECWB_Uj35aPqnc9HaBRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6b49a5ef.mp4?token=gvUj784kXNuWr9FyhbvAj3jiuTAN7bHp3fmyxSIeC_JpaIWuSRC7Umkd5397XoQq1OwPQv1HwmcDCHfL7lP9af6W6cl-9prNv7FmSqazmngo32sD0dvGcObtAYJFsJcL4YyaSJJMqycgjGfuhcI8-qapn9eKX6lL1nVnPrd8m2rk7QO5j_34H65ZvP7e0WvVDHSQyezNgHtu6WvJ7QEa9AsdU4VrZewJredqvMAS01zq1wMBMMYXoCf7MdO2Kd4w9jXGuSs3t2yDGkCOb2OmmVDBllgBZBjJQaTnO6kDFUK2a3rPlLYzRnAGLlaER2B93_ECWB_Uj35aPqnc9HaBRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاقات صاروخية جديدة من إيران</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/85283" target="_blank">📅 06:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85282">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd05236fdc.mp4?token=nsVM63AiVwyFnhB2fFFXU6jEN-BnQIo5QKiQXYpdqb3A1gm-Q_Io4k0leXGvy0Kto4u5Wyj4katajx3OBvnz8ewzFBidjcG51LLqQbIsT0dLJT8op2qe-2XCBuFI86-74bzXgujSW-1JIgsO5sOmKATsxiz3qc2j9m7Tm8r8KolcA02o6yQVKzb3Tuc9HAXespTt3kGAs_Cwj2YwtwMHYZd1_4b74_-F6Cj58XPBf94RoZxZVNWojZJaWkOZTB_8hobVynRWbbY_KLgQtTOxdAfRGye3NwHjRzQfvcR9OF2M2XGl_7cYHdKuqWg6Hn7DTkqzWG9JPSLHpZtzPSqnDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd05236fdc.mp4?token=nsVM63AiVwyFnhB2fFFXU6jEN-BnQIo5QKiQXYpdqb3A1gm-Q_Io4k0leXGvy0Kto4u5Wyj4katajx3OBvnz8ewzFBidjcG51LLqQbIsT0dLJT8op2qe-2XCBuFI86-74bzXgujSW-1JIgsO5sOmKATsxiz3qc2j9m7Tm8r8KolcA02o6yQVKzb3Tuc9HAXespTt3kGAs_Cwj2YwtwMHYZd1_4b74_-F6Cj58XPBf94RoZxZVNWojZJaWkOZTB_8hobVynRWbbY_KLgQtTOxdAfRGye3NwHjRzQfvcR9OF2M2XGl_7cYHdKuqWg6Hn7DTkqzWG9JPSLHpZtzPSqnDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاحتلال الأمريكي يحاول اعتراض الصواريخ الإيرانية فوق قاعدة موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/85282" target="_blank">📅 06:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1pXWfmgtF_3xzejbvkfG9Z7Jt4adYGvYfPD7wGkkLMhuJBqyCBuynX7p8_A5JbQ7yxq9S54Jr7Nqi9MnPBEPeAB6SPNdAqBOp2pEKpDefCHNPmq-5wMnTWcuAtVK4ulrXkwJHSJgEfl-ZLhr57iK6mWqSz10-FqUraaUZ0OPRfYXWJKVsUmpSuXaQy-YoKzLykwrxeLTbY7CE0JjZaI1E-ZQM4DCLsGviEAyyt4kEnxi4yNKoo9pQ9rVReEgnfPABV577MrHeyDmlLrMXi7caqlF1YfZq9qdeRWqv-EjhQHueOcoTtIyO_lQkLkTQD6CczdDWiZWcBVO2RsGr2Yqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاقات صاروخية جديدة من إيران</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/85281" target="_blank">📅 06:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85280">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd26e288d3.mp4?token=ZwmBGn5qyw62D5PpialMJ3YB6wzoYhHm4NSUpSHwdUQKW4-2mi9DXtd_7ei7weeMeJcUhcNAGNSYboVSIT9lcH-Jmh2C6xriHv0RL59JvwimTqcXSe2k1s51rKOU7NkMbRdQw9PNNPUPRoFw9L5pf72269w6nx0CEogYNIC9YV5LuUljZ3IxVdUHlfHdQeaguBGGaXpC_B2holgx5mPA9T3p-E0VnJ3uerMypTxxQytxoFy0S7yg0xFdH0ED8PpWu5kJpOuZEk_e61q5KtjIv0WGg7rbDyhBHtLpEfJcfSFwoGLwOXSM7F97IoPLZJT9hJ1YH9CBU2vjpFNU0rz-GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd26e288d3.mp4?token=ZwmBGn5qyw62D5PpialMJ3YB6wzoYhHm4NSUpSHwdUQKW4-2mi9DXtd_7ei7weeMeJcUhcNAGNSYboVSIT9lcH-Jmh2C6xriHv0RL59JvwimTqcXSe2k1s51rKOU7NkMbRdQw9PNNPUPRoFw9L5pf72269w6nx0CEogYNIC9YV5LuUljZ3IxVdUHlfHdQeaguBGGaXpC_B2holgx5mPA9T3p-E0VnJ3uerMypTxxQytxoFy0S7yg0xFdH0ED8PpWu5kJpOuZEk_e61q5KtjIv0WGg7rbDyhBHtLpEfJcfSFwoGLwOXSM7F97IoPLZJT9hJ1YH9CBU2vjpFNU0rz-GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الأراضي الأردنية لحظة وصول الصواريخ الإيرانية إلى الأردن قبل سقوطها في مواقعها</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/85280" target="_blank">📅 06:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85279">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e5840a91.mp4?token=WTlLpsxc9bZ1x2R7CSRLiCB3QgZQRcitUowxyO1V5hKNV-7lqVM-nvFRTdxz2E_TQ5Kd8sHVHVyJ4FBAwIX77-Ot8w-iwtglXMOSWEubmVrIErYfGnwv-Mgs-rkwV6KdOHQBolboLvfcyYZu5PMSpPGEhYGuKoVXwlWoIKR-3nathhf-oUBeC9bPUftnKntX5cA5UMgrzkoSlTTDKs_CRAXQOO_t8lMI1HxvxqWfkl-e59qPgjzynAzOsvJehNeNs6u6UG-rUSps3OmPvzNVVOx3z7uyHrDIiI-kJBGxRYMLBhRm_lYe1J2RTalc1NmcJ_Vg7RH_Wl5-TnwmDTDDrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e5840a91.mp4?token=WTlLpsxc9bZ1x2R7CSRLiCB3QgZQRcitUowxyO1V5hKNV-7lqVM-nvFRTdxz2E_TQ5Kd8sHVHVyJ4FBAwIX77-Ot8w-iwtglXMOSWEubmVrIErYfGnwv-Mgs-rkwV6KdOHQBolboLvfcyYZu5PMSpPGEhYGuKoVXwlWoIKR-3nathhf-oUBeC9bPUftnKntX5cA5UMgrzkoSlTTDKs_CRAXQOO_t8lMI1HxvxqWfkl-e59qPgjzynAzOsvJehNeNs6u6UG-rUSps3OmPvzNVVOx3z7uyHrDIiI-kJBGxRYMLBhRm_lYe1J2RTalc1NmcJ_Vg7RH_Wl5-TnwmDTDDrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من انطلاق الصواريخ الإيرانية نحو أهدافها في الأردن</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/85279" target="_blank">📅 06:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85278">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dddaaef9.mp4?token=lzqojNzGbwggok2NLLrO8sZ-vSDmubG4dgSi0RTo8TSLCBOQ5iZwFn7t6cLNMSFCnz6m8onHxfw-v42-15IExYJcXbVheOJm8fkFYy0JV5uYjc_Z7wq3RzECISTPyWmqztPVNDNzMxOFVQglJfRgjXTAkluSgRCzkta3Y3qO5Th8jMcHQYtMym8Wy7EqlqEpkUPbBYzxjdgdazT8tmnT0igWyfBJrRAkDO9KCrVU5gM77SE6iH9YApMscByGuj0RxMBByvBB3SpzaaEdxm3EEdNZWTris1mMsN9SzHQHFtpbBpcpeHpJqFbzYCui3-l8mJvhCUYvNIolN-QRHzy4kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dddaaef9.mp4?token=lzqojNzGbwggok2NLLrO8sZ-vSDmubG4dgSi0RTo8TSLCBOQ5iZwFn7t6cLNMSFCnz6m8onHxfw-v42-15IExYJcXbVheOJm8fkFYy0JV5uYjc_Z7wq3RzECISTPyWmqztPVNDNzMxOFVQglJfRgjXTAkluSgRCzkta3Y3qO5Th8jMcHQYtMym8Wy7EqlqEpkUPbBYzxjdgdazT8tmnT0igWyfBJrRAkDO9KCrVU5gM77SE6iH9YApMscByGuj0RxMBByvBB3SpzaaEdxm3EEdNZWTris1mMsN9SzHQHFtpbBpcpeHpJqFbzYCui3-l8mJvhCUYvNIolN-QRHzy4kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ إيرانية تدك قاعدة الملك فيصل وموفق السلطي في الأردن حيث تتواجد فيهما القوات الأمريكية.</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/naya_foriraq/85278" target="_blank">📅 06:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85277">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaxMC4mu47FKUJAes28PGVGmlfxMyQeswiL1FeX8qlyySTv-asd2ZFF3xtDdU7PZRnbUFDe1JXh3VYDuvuhLpArSKOZ2_IOG4sLdqILHK9eS2EBfn074802P8M0RagFSup1LHjzjAE5_xS4nR90q-aGXr9mFac9dSHKE41PiWYJ1edk3p-RcJOuNXXlCEX3LYPpjQdJhCShhWwqAgs16mB6VbP7IHehmfEVrzMgsYb3n525m7j4y6-2axHy9hPLGDJBd7IIL9umrxpPEf3PEMn8XNCUsMGneCfwX7VVHyjid7IIaJ4f55hqgUMnCQg7kqE55zHDqFLWlbIcCOci8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاحتلال الإسرائيلي يحاول التصدي للصواريخ الإيرانية المتجهة إلى الأردن في سماء محافظة درعا السورية.</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/naya_foriraq/85277" target="_blank">📅 06:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85276">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4febbbbc29.mp4?token=mZeK6Vwh_2Z-Bl1c3L_HKJ7nHrjfi62tTCRYQ_IOtBtypQtw99jWA_iE8kGB86t7rYquf-588YVKdodloQCguqAMBetOyyPCzHOwOepXD9YrDH3LZiMUYqe_Paw-ARBdtap-YYQUmBR87w9UNpNOZj1B9DT1g7WdSLgopzIR1gxKIy3ckhoYCsSkfsm3P-iOCXSmijFLvG2Lqm3KhAYHwnlnibI7q4Osd570qzMGmdTc56ogv_uqK7jFPzGmx8P1xrGdlzqugMyd-mDC--z4Qu_AxruWoNZyqWDLswu8I93Y6mIDJvw3bLJWe88CTB1oDA5jhxa1cPqI4pVaqfd_Roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4febbbbc29.mp4?token=mZeK6Vwh_2Z-Bl1c3L_HKJ7nHrjfi62tTCRYQ_IOtBtypQtw99jWA_iE8kGB86t7rYquf-588YVKdodloQCguqAMBetOyyPCzHOwOepXD9YrDH3LZiMUYqe_Paw-ARBdtap-YYQUmBR87w9UNpNOZj1B9DT1g7WdSLgopzIR1gxKIy3ckhoYCsSkfsm3P-iOCXSmijFLvG2Lqm3KhAYHwnlnibI7q4Osd570qzMGmdTc56ogv_uqK7jFPzGmx8P1xrGdlzqugMyd-mDC--z4Qu_AxruWoNZyqWDLswu8I93Y6mIDJvw3bLJWe88CTB1oDA5jhxa1cPqI4pVaqfd_Roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الأردن تشتعل بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/naya_foriraq/85276" target="_blank">📅 06:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85274">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d31a0f52.mp4?token=L10nSY5CFLXbxLVkAI-RkfnOMav-SgDSzS0DYvOxMyXOpE15P88C37TOXQl1C4Qopih4G58CBmPSgAsmkfA_cO3SZkhoVQ1XBByWJBcOe5eS5y2wQxgdRm101ctzU4QDnLA8j44RXZOTrJ6PPuvCQubVoolVuspSATBuT2Z0SgKY4S-cPexPOhIi6sAn9SxU-50DXmma7kg_DFA4hUy4Nzj-YMQUKrWX82d_6nZMoRy_biE8Wajwe2UM0tyYvLjHlbeWElWO0bsJJQ8YSdf1XFBGesz6MM-lSHXkEzeEClVZzp1L1IUj1UILxCqx1zPMt9Zs1I4Y7CsEguMlxGw5DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d31a0f52.mp4?token=L10nSY5CFLXbxLVkAI-RkfnOMav-SgDSzS0DYvOxMyXOpE15P88C37TOXQl1C4Qopih4G58CBmPSgAsmkfA_cO3SZkhoVQ1XBByWJBcOe5eS5y2wQxgdRm101ctzU4QDnLA8j44RXZOTrJ6PPuvCQubVoolVuspSATBuT2Z0SgKY4S-cPexPOhIi6sAn9SxU-50DXmma7kg_DFA4hUy4Nzj-YMQUKrWX82d_6nZMoRy_biE8Wajwe2UM0tyYvLjHlbeWElWO0bsJJQ8YSdf1XFBGesz6MM-lSHXkEzeEClVZzp1L1IUj1UILxCqx1zPMt9Zs1I4Y7CsEguMlxGw5DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معارك صاروخية في سماء الأردن عقب وصول الموجة الإيرانية إلى القواعد الأمريكية.</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/naya_foriraq/85274" target="_blank">📅 06:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85273">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8a1a7390.mp4?token=Gy0N4onlWS--_zNl9jc1LTKCAtDmFW0yep4q8fDIktivZs6WRaGcUvpp6J0P69Oy7nyikqelkMKpTzVxnupfT5DynNOE2l_6T0A7HVMSfdn2Sd1s_UGqW74Z529P9gMSuYLHAlL4GoJn-ya6jDxn804-6fPT7PdsDc7_l37hJYVaxbMpibJ4BEIU1UPbDqE7b5a4l9UFcAAz6KBO4vrXjfJevO7unJAP7AkHRPO62l8p6w5BolfRhzbM-VZk1espVlE72SxB-raoFfwB1Tu-7gmTrUMsgghoSOslKl-ZOpY9WAdD5T3lg4plW8boQia8XqpIlO7jYSj3iSZvUCUKXRSxRa7cbT5Tld9XolgMCmDNWB76LnSUux0E4zg2f4075bnen1g4GDrD4D7cl8b8xoZHU585Y7Zn2VhStN1pWgD2Xzp1CegSD6y2mz3isNv8qA_ElYUMDTceq9CUq6z0aeu4e0yQhsDCoYfusDJQOj2yTVfQyxb98wRCWgKMlQF3h7YU_J_CLfMUGNsTHiAj12yx-PSvNH6sLeCl8M28R6dgyNX39BKej0jDkfaRyenWMan4d8IwuTBljMjB8ht5TcInfM6rBkbog87u6-obyRi7P-N8AtJXovD81dLjMU3_uvShQaEuGGaFXPuB_umZZcJVXm316r9S7FfxAWz0vwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8a1a7390.mp4?token=Gy0N4onlWS--_zNl9jc1LTKCAtDmFW0yep4q8fDIktivZs6WRaGcUvpp6J0P69Oy7nyikqelkMKpTzVxnupfT5DynNOE2l_6T0A7HVMSfdn2Sd1s_UGqW74Z529P9gMSuYLHAlL4GoJn-ya6jDxn804-6fPT7PdsDc7_l37hJYVaxbMpibJ4BEIU1UPbDqE7b5a4l9UFcAAz6KBO4vrXjfJevO7unJAP7AkHRPO62l8p6w5BolfRhzbM-VZk1espVlE72SxB-raoFfwB1Tu-7gmTrUMsgghoSOslKl-ZOpY9WAdD5T3lg4plW8boQia8XqpIlO7jYSj3iSZvUCUKXRSxRa7cbT5Tld9XolgMCmDNWB76LnSUux0E4zg2f4075bnen1g4GDrD4D7cl8b8xoZHU585Y7Zn2VhStN1pWgD2Xzp1CegSD6y2mz3isNv8qA_ElYUMDTceq9CUq6z0aeu4e0yQhsDCoYfusDJQOj2yTVfQyxb98wRCWgKMlQF3h7YU_J_CLfMUGNsTHiAj12yx-PSvNH6sLeCl8M28R6dgyNX39BKej0jDkfaRyenWMan4d8IwuTBljMjB8ht5TcInfM6rBkbog87u6-obyRi7P-N8AtJXovD81dLjMU3_uvShQaEuGGaFXPuB_umZZcJVXm316r9S7FfxAWz0vwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معارك صاروخية في سماء الأردن عقب وصول الموجة الإيرانية إلى القواعد الأمريكية.</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/85273" target="_blank">📅 06:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85272">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b308e2eb6.mp4?token=NklyhlbBRr60rFvfWEUlEtZ5_ThI0PrAoiDk8Ivz2gJT7gSYuDDQiZFe1MwRkUFlVcZ7yPHoE2a7KwWRzTh7IuqHENN1YZys3kynopD3_MW5YfWFzOJVihGTOATEAsKsedyJ1-W0i02yuCS-ZgOfODISjjjCLxN8zSWbzGam2XMJAGxwyo3sX6ftuRTxwjXv_y50wIdni5oKl_kKU7VyaALbgoK2mKhK6NL9l81ACqabDF6KUdDIOgWIODk0-HoajBh3Bt1EmBQxUEFP_bvjBw4j1xBHEULklwWKxbmwZSiXEc_QwE_j_Ksyr4F4hmY-SHFlHweow6xm9DWKWxPVurOrP3PfHNVeY4_rdIlrl764I50CksCQi1ioxjKd27BVMmlEWGQzP-m-1uI25nUIgoS0uQr5xvEssFEKl8JJPU8uDYcpPHCLo_UC1GnmwzpjkJOaYCAzttmvG1f5WV4hSBgMTUM0KbIJGFxtIwXXzOTvPRGYQsRzZkMyfStaxMh8Dyk4YPwSabT_gaZrjR73BrIc2IFGSx5d6BQuphO-IjNZzLL0icmRYRIVkgZvEvDKajdjbH13_HkIoO4yJ8NzN3NJvYzT-7_NAia6mxTqxXro5PLXboYGfc_cEzBktMyGyiY88gZjlCmoJcjnETqErdruJg9Nkz59qndUSdIMlbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b308e2eb6.mp4?token=NklyhlbBRr60rFvfWEUlEtZ5_ThI0PrAoiDk8Ivz2gJT7gSYuDDQiZFe1MwRkUFlVcZ7yPHoE2a7KwWRzTh7IuqHENN1YZys3kynopD3_MW5YfWFzOJVihGTOATEAsKsedyJ1-W0i02yuCS-ZgOfODISjjjCLxN8zSWbzGam2XMJAGxwyo3sX6ftuRTxwjXv_y50wIdni5oKl_kKU7VyaALbgoK2mKhK6NL9l81ACqabDF6KUdDIOgWIODk0-HoajBh3Bt1EmBQxUEFP_bvjBw4j1xBHEULklwWKxbmwZSiXEc_QwE_j_Ksyr4F4hmY-SHFlHweow6xm9DWKWxPVurOrP3PfHNVeY4_rdIlrl764I50CksCQi1ioxjKd27BVMmlEWGQzP-m-1uI25nUIgoS0uQr5xvEssFEKl8JJPU8uDYcpPHCLo_UC1GnmwzpjkJOaYCAzttmvG1f5WV4hSBgMTUM0KbIJGFxtIwXXzOTvPRGYQsRzZkMyfStaxMh8Dyk4YPwSabT_gaZrjR73BrIc2IFGSx5d6BQuphO-IjNZzLL0icmRYRIVkgZvEvDKajdjbH13_HkIoO4yJ8NzN3NJvYzT-7_NAia6mxTqxXro5PLXboYGfc_cEzBktMyGyiY88gZjlCmoJcjnETqErdruJg9Nkz59qndUSdIMlbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابات مباشرة للصواريخ الإيرانية في القواعد الأمريكية بالأردن</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/85272" target="_blank">📅 06:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85271">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WR1Irr1I8VvB6gkkW_8O0zYBQcHhPhW6ToxOsW_T2IW2DQqim_7ixJDt_rnSVuqg-wTX3KGyOi_Otv_89j8ZOUqL-cAXYWQZJV7L1BS5UziVLEIcP5YtjwPpbIZIkmP1FieCe2pZHyVNCYEWfV4-zLRbY-6LFZlQuM1GBTqSLBLXmeek3wXx0AfEOBHMQQiYmDxOFOeHFvKzSfYYhBMH56CmpIQE--IzbXf7QseSDT3gUWrWZpp8bwA5NssVG_dKtvPyj5aUkix5khCRgT41vk2tb4Eoq2YTU8REx9SUx_v_jcWN4O0rpjEAaLieRTSSrvgK_W3PghNFoFvSqHldjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
إن الاستيلاء على أصول دولة أخرى لدفع مطالبات مستقبلية لا صلة لها بالموضوع يُعد سابقة خطيرة.
يجب على أولئك الذين يحتفلون بهذه الأموال أو يستفيدون منها أن يتذكروا: بمجرد أن تُطبع الحكومات المصادرة، لن تكون أصول أي شخص آمنة. ولن تكون الفوضى التي تلي ذلك جميلة أو سلمية</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/naya_foriraq/85271" target="_blank">📅 06:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85270">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b72a5b6ef8.mp4?token=aTxiIdvWy5_5TZMBakgeQ4grN8jEJCqfjghn6oLLdCcF0dwTbMNE4ngZs49L4K7EYz5WnvPjIK1aFej_rjq5umKhPwMAVLflLuhrrEFdC7-wPghFrAZId5qgdoNT2U-OD4LzUNYZbVkOTfiaUD40NQTLY6Ej3DbA5XrdAfeur4wTv3wTqENGjHtNsl9ZtISuWcjR5nH8H-zDMeauNB_gAa2GfVVh9Dd0epy_Em4d3-VqnlvIEc1uKh-bOe5vLhsD2Ojo5_ztmrsRNsPqvf51pTcTv4YFc5T1zuZDI6_T__VbaT9Tr3YJpQByfUMwDF9dw8ihQKaLMNXmtgBC4LYD4BmraZ9yGvCdMWD1XPKIOTmN6GX3Huu8cgIxyRxWEBi2XbZeagfxqL8GwKCDOynshl8JhRZki2yloGyATEt0N6rDIVJnLCTgV_lg7Rs15U4s7WXPFKlGkItu_jhAZU5fVh-2LA-AOB2qPGJofF3V7BCniYCYARu34WqlUT6qi3J1C_Vb6a5EJljNenNHG235Ke04T1PY_NKHDzKiuv7zrdAOGqOaAYm0bPt9aR_Wm1NaTOeMaqkHyjdblnaN3V_X32_Njqkpt0Bu2gJpRy3ULyhbCKcomUNjXVGhoqT6KOvzM--KhiJcy4iTId45ir4Hi2qG-K1nUjKsZeCebMCXZ2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b72a5b6ef8.mp4?token=aTxiIdvWy5_5TZMBakgeQ4grN8jEJCqfjghn6oLLdCcF0dwTbMNE4ngZs49L4K7EYz5WnvPjIK1aFej_rjq5umKhPwMAVLflLuhrrEFdC7-wPghFrAZId5qgdoNT2U-OD4LzUNYZbVkOTfiaUD40NQTLY6Ej3DbA5XrdAfeur4wTv3wTqENGjHtNsl9ZtISuWcjR5nH8H-zDMeauNB_gAa2GfVVh9Dd0epy_Em4d3-VqnlvIEc1uKh-bOe5vLhsD2Ojo5_ztmrsRNsPqvf51pTcTv4YFc5T1zuZDI6_T__VbaT9Tr3YJpQByfUMwDF9dw8ihQKaLMNXmtgBC4LYD4BmraZ9yGvCdMWD1XPKIOTmN6GX3Huu8cgIxyRxWEBi2XbZeagfxqL8GwKCDOynshl8JhRZki2yloGyATEt0N6rDIVJnLCTgV_lg7Rs15U4s7WXPFKlGkItu_jhAZU5fVh-2LA-AOB2qPGJofF3V7BCniYCYARu34WqlUT6qi3J1C_Vb6a5EJljNenNHG235Ke04T1PY_NKHDzKiuv7zrdAOGqOaAYm0bPt9aR_Wm1NaTOeMaqkHyjdblnaN3V_X32_Njqkpt0Bu2gJpRy3ULyhbCKcomUNjXVGhoqT6KOvzM--KhiJcy4iTId45ir4Hi2qG-K1nUjKsZeCebMCXZ2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الأردن</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/naya_foriraq/85270" target="_blank">📅 06:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85269">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726db6ae6d.mp4?token=jCzUyyrESRwaGN8rnB0Mk2X8x6nH0QS2u7DTx_1kxq3NNJz8aqswXZmiJoq2rtCiHl_AKZ_itRJra0t3aUeYsZDOEW5Lk4Gzket9P3aSXnfMXPT4ezEErFK3_eM04DUXwJE8OEHkfOtCPLIgcrLe4NN57BvICXzbQr5e0rcCWgS9919AK1oWrxrIWbkPkQSMUOIO_Pdbfvf2HNDC3RvvIuy4Pp9z_z6Yw_nH97uP1YORo5gC85QEBnlX4DjvRpq5MZsHjriKmXQzeywsn17BdvRAsmWekXjQmWChWlZFKtJ47hVHmTtBesVwHAY3CTlrmf98HsVjZy47BUBN4wq8ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726db6ae6d.mp4?token=jCzUyyrESRwaGN8rnB0Mk2X8x6nH0QS2u7DTx_1kxq3NNJz8aqswXZmiJoq2rtCiHl_AKZ_itRJra0t3aUeYsZDOEW5Lk4Gzket9P3aSXnfMXPT4ezEErFK3_eM04DUXwJE8OEHkfOtCPLIgcrLe4NN57BvICXzbQr5e0rcCWgS9919AK1oWrxrIWbkPkQSMUOIO_Pdbfvf2HNDC3RvvIuy4Pp9z_z6Yw_nH97uP1YORo5gC85QEBnlX4DjvRpq5MZsHjriKmXQzeywsn17BdvRAsmWekXjQmWChWlZFKtJ47hVHmTtBesVwHAY3CTlrmf98HsVjZy47BUBN4wq8ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موشک های ایران اسلامی در آسمان اردن</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/85269" target="_blank">📅 06:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85268">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0874f68421.mp4?token=LqMd5subwmAnpNWF6Q0I-GtvkRxjZTkMo6TlNLq0Hsn9xXE1rRnAVoAWV7hiVBUCRHAuO-EyvpOW7e2N3WVWzR_Rzs9UUvylGLfGUfz5t8NT9YRAJBtoseX9wsZ7we9vmetd19fRscQUjs2gergjm9JlJaqVnMiDlYnp75bIfkUXFBULfWMM0Wa0eR1s5jhegoSQwKTNU1V_R-KyXZcXsOINaich7Qwu-nLGawRdhF9sVq0VW6dfayViY7b5rfBqNv8us0sVKPuGJiJPp49Qlz3zQFjxDTnOgUizUE1Dd-l6DdVJnV7-IdkdSFx-3lt3tvMj6Y5mkzw6fsJrtaYp5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0874f68421.mp4?token=LqMd5subwmAnpNWF6Q0I-GtvkRxjZTkMo6TlNLq0Hsn9xXE1rRnAVoAWV7hiVBUCRHAuO-EyvpOW7e2N3WVWzR_Rzs9UUvylGLfGUfz5t8NT9YRAJBtoseX9wsZ7we9vmetd19fRscQUjs2gergjm9JlJaqVnMiDlYnp75bIfkUXFBULfWMM0Wa0eR1s5jhegoSQwKTNU1V_R-KyXZcXsOINaich7Qwu-nLGawRdhF9sVq0VW6dfayViY7b5rfBqNv8us0sVKPuGJiJPp49Qlz3zQFjxDTnOgUizUE1Dd-l6DdVJnV7-IdkdSFx-3lt3tvMj6Y5mkzw6fsJrtaYp5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة الباتريوت في سماء الأردن عقب الهجوم الصاروخي الواسع على قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/naya_foriraq/85268" target="_blank">📅 06:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85267">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d84fda6e.mp4?token=XW6zT8pVobxkFTJyA2sr-AioqmoG5UYajAPKi4gUQWRgxMJe1hWT2AYH5WZ2F2A1Cnlmul14FkwwAzAyh2TXl4QGLafib_OhSyHnN7cStSOnD3ykhb55VRwgFp8Gv8TSlwsisGRkWI2TqpLNiCDE-TN-fc58XYfnpGrXUCvP9bqofJtrvntLS_GuTHu6UE3QqH-p-wE2GKbdv5_8r9Xe-tJUNlOvn3KcnXlt_E1vQIppx30COjNeCi0T3rXKndBOx-y0KTwbwvTag0KwARbkWBtUdOEAWH9urn74q-7pI2mM-vwzIGxjMeLPkkmTQEc1zTCZrQS_Bkcqnqje-u3iBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d84fda6e.mp4?token=XW6zT8pVobxkFTJyA2sr-AioqmoG5UYajAPKi4gUQWRgxMJe1hWT2AYH5WZ2F2A1Cnlmul14FkwwAzAyh2TXl4QGLafib_OhSyHnN7cStSOnD3ykhb55VRwgFp8Gv8TSlwsisGRkWI2TqpLNiCDE-TN-fc58XYfnpGrXUCvP9bqofJtrvntLS_GuTHu6UE3QqH-p-wE2GKbdv5_8r9Xe-tJUNlOvn3KcnXlt_E1vQIppx30COjNeCi0T3rXKndBOx-y0KTwbwvTag0KwARbkWBtUdOEAWH9urn74q-7pI2mM-vwzIGxjMeLPkkmTQEc1zTCZrQS_Bkcqnqje-u3iBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة في سماء الأردن</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/naya_foriraq/85267" target="_blank">📅 06:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85266">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458f6a2735.mp4?token=dw-mOlrq9emBHHqA2JuEzrYA8vsz6c-kqkq8Tk-jCKyvkQfuvdyIE_XqZe6FVG0mzRqDjjGd8GjtvMsyb5L1LWfEqMjhPFjHCO8jT5koYpfciGsmM40FIH5WClTbl04T2aFb2Vt4v4hXHje3XUCuj9n071eWb1OQPSS4e3dsgBeP5fPvCG9e5M-YA20wZ4UhgQClNcM_sX_zYD-UMVmBhYzAuQCG1n4p8RotfZbvD_zOBwopAGwRGeFTiq7sFoX68_d-7XbHE671pAttK2ZiT5GWVZ_7fnGR6MyRYZD-Bj0EZQj7PwmHPzZDFMH2Lcn0EvmXxEp9BIabC8pPlnXovw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458f6a2735.mp4?token=dw-mOlrq9emBHHqA2JuEzrYA8vsz6c-kqkq8Tk-jCKyvkQfuvdyIE_XqZe6FVG0mzRqDjjGd8GjtvMsyb5L1LWfEqMjhPFjHCO8jT5koYpfciGsmM40FIH5WClTbl04T2aFb2Vt4v4hXHje3XUCuj9n071eWb1OQPSS4e3dsgBeP5fPvCG9e5M-YA20wZ4UhgQClNcM_sX_zYD-UMVmBhYzAuQCG1n4p8RotfZbvD_zOBwopAGwRGeFTiq7sFoX68_d-7XbHE671pAttK2ZiT5GWVZ_7fnGR6MyRYZD-Bj0EZQj7PwmHPzZDFMH2Lcn0EvmXxEp9BIabC8pPlnXovw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة في سماء الأردن</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/naya_foriraq/85266" target="_blank">📅 06:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85265">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0c09dda6.mp4?token=rz27Fs5vgpqfqTgPNpKWiv5HYyw4-4F-PUKozmBVDRfEig55-oWd8lmwoZaKuzwmHfLU9HY8Ntt1EKiRs4Q4hj9ILtVOCSohR4lngFMjdrT3IcRRUAbtq-KPZhLcmcCFEcxc3ofzsaZ6Rbekx1Cf3SSGwImYA2jd_2BVNCiUuOpflR6gdu1EHfHSgUFgOR7EgZ0_Qbl_RUfUEopycQatUNBhk1-Eh3Sp3QLf77UE5qCLO5489_uuAL3FVq2MfDfzqcoGaVSIw1yvXrMiZB0BD5iRxJylQM7-uvTnBHysi-RODXCYvextz_iWA_9HMuwjfNg-W3IM4Cq-WMdPV2ng-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0c09dda6.mp4?token=rz27Fs5vgpqfqTgPNpKWiv5HYyw4-4F-PUKozmBVDRfEig55-oWd8lmwoZaKuzwmHfLU9HY8Ntt1EKiRs4Q4hj9ILtVOCSohR4lngFMjdrT3IcRRUAbtq-KPZhLcmcCFEcxc3ofzsaZ6Rbekx1Cf3SSGwImYA2jd_2BVNCiUuOpflR6gdu1EHfHSgUFgOR7EgZ0_Qbl_RUfUEopycQatUNBhk1-Eh3Sp3QLf77UE5qCLO5489_uuAL3FVq2MfDfzqcoGaVSIw1yvXrMiZB0BD5iRxJylQM7-uvTnBHysi-RODXCYvextz_iWA_9HMuwjfNg-W3IM4Cq-WMdPV2ng-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات صاروخية واسعة تنطلق من إيران الإسلامية</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/naya_foriraq/85265" target="_blank">📅 06:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85264">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dc03c583.mp4?token=gxVxPpOhNcCpFafCepT9yKNVyWAq1renoUpccH1HR1Y7XsJ8uwdJeHCIcNwJ_ZqDvc_VAhcXlzkciHBpLwsV1LV1cisoH25WK2ZeEZ7dIN22QNekIcnGiPzEi7KCPMwEk5NqrtDJvLDtk0GyIW8O31bHcbqoz4JnwgSGxyuhwUMMVLXL7y3mxSrDC8vPTAWdi46M2pI1b1SAZYJOVb2XkdYFPAVbx-b9-vneHjUJ_uT3Vtd-iTkQou7HRFJ5gujhRH0DjQXEFXLpKBsGZbhMQOiUaiu9WP7QG06r8cifvNTdNIiWrT3ixQ0w10Q2qh6OeI5O7M4P-tmKe8cipzkAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dc03c583.mp4?token=gxVxPpOhNcCpFafCepT9yKNVyWAq1renoUpccH1HR1Y7XsJ8uwdJeHCIcNwJ_ZqDvc_VAhcXlzkciHBpLwsV1LV1cisoH25WK2ZeEZ7dIN22QNekIcnGiPzEi7KCPMwEk5NqrtDJvLDtk0GyIW8O31bHcbqoz4JnwgSGxyuhwUMMVLXL7y3mxSrDC8vPTAWdi46M2pI1b1SAZYJOVb2XkdYFPAVbx-b9-vneHjUJ_uT3Vtd-iTkQou7HRFJ5gujhRH0DjQXEFXLpKBsGZbhMQOiUaiu9WP7QG06r8cifvNTdNIiWrT3ixQ0w10Q2qh6OeI5O7M4P-tmKe8cipzkAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات صاروخية واسعة تنطلق من إيران الإسلامية</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/85264" target="_blank">📅 06:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85263">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات في مدينة خرمشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/85263" target="_blank">📅 06:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85261">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40bc05e0e7.mp4?token=hsBIPuTwScscP40TYRc0j5g5j9ODo0bMMe0jAXVo8GKCzPwUxCSHppaqGXgaluNSoN1VNg0w_4cERO5S8RDbGWIEkj-Ytg7F-1NNkgDiKsvEjehq9iAeIzIEhppTCaEnNDvdSRI3ndldOCkyXAE5jMYljdE9eUByz58zB8UuDesXxD-9_JBDZtWpe86W9wwzu6hj09q-QOcXm2ysvIqRiaKDcZrKvsK9pGfsjP7CaYCsjeHZTw0c3PVOJxLGHTHT-W0n1Ko4NsvPv5Fz-laBbKTQXhjdbUuOTSD7MQjCWYttGYZVi4EJRhlw6ne1mrnAf4rTKQ7CXeRopGllFXgqCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40bc05e0e7.mp4?token=hsBIPuTwScscP40TYRc0j5g5j9ODo0bMMe0jAXVo8GKCzPwUxCSHppaqGXgaluNSoN1VNg0w_4cERO5S8RDbGWIEkj-Ytg7F-1NNkgDiKsvEjehq9iAeIzIEhppTCaEnNDvdSRI3ndldOCkyXAE5jMYljdE9eUByz58zB8UuDesXxD-9_JBDZtWpe86W9wwzu6hj09q-QOcXm2ysvIqRiaKDcZrKvsK9pGfsjP7CaYCsjeHZTw0c3PVOJxLGHTHT-W0n1Ko4NsvPv5Fz-laBbKTQXhjdbUuOTSD7MQjCWYttGYZVi4EJRhlw6ne1mrnAf4rTKQ7CXeRopGllFXgqCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صواريخ واسعة أطلقت من إيران</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/85261" target="_blank">📅 06:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85259">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZsZhs7tBc6eF5v7NunavOAPkwFlKKUw7UUaPTlJ3kaxWLoAhvLuK-5gqI8HTU95ZlrSGKbWWJEvumI_JRER_tOHlfYlfTP0xq7soE2YHuECRG9O-zQoFToZGJpQrNXx-JKIErJAMXNQ9-iys_Oeu-tNUqz7PvJa0mu5aQK0fZPvJbQNALEbtrqvu-C5UU5TaL9Ccy9B5NZcZveftd3IjlPJjh_GF9AO0I5FMq6hQQlpLfekHO2AZRKUe4xJPgQ7crBdOhYom0KgKrVdcBz7daHpFgQDoy6qIcfPVR0mX1GioXb-upBakwa7GDAkkyP6b_8UyU-LXnrnbqMGAe5MNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2638dcbb22.mp4?token=GMzWw962Pivq97RPgVaHIYk3fQVSe_23DPOWRfQxPa08NCPFUxmM78qvzGxpbjRXVuGcUSKNB2TeK0AxL3QmxqBjNjfRR8O3AEjEXEOUai9C7T3D1I4Hn_OwKw4qn9_sZ4NFqPIAg2fWzALAJdyJ8QnttU4-Im3bVSQcfNdAXUfUVC8i7KFJEB1lIIDu404lENCCjC26oKKsUn3doiC9DDQJF896DUGxyFfyqXcCGE7e2HbvcdEFVkK3yY6MFS16QCJJ4bNlxh4f_QzPPn8CtvnsH5NqEVNoUklKGmZO5ucZEqV5Z0MwMT-n1K1n5ZT_B7GJZpNdUvcxcMQOxj1hgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2638dcbb22.mp4?token=GMzWw962Pivq97RPgVaHIYk3fQVSe_23DPOWRfQxPa08NCPFUxmM78qvzGxpbjRXVuGcUSKNB2TeK0AxL3QmxqBjNjfRR8O3AEjEXEOUai9C7T3D1I4Hn_OwKw4qn9_sZ4NFqPIAg2fWzALAJdyJ8QnttU4-Im3bVSQcfNdAXUfUVC8i7KFJEB1lIIDu404lENCCjC26oKKsUn3doiC9DDQJF896DUGxyFfyqXcCGE7e2HbvcdEFVkK3yY6MFS16QCJJ4bNlxh4f_QzPPn8CtvnsH5NqEVNoUklKGmZO5ucZEqV5Z0MwMT-n1K1n5ZT_B7GJZpNdUvcxcMQOxj1hgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ أخر يحلق نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/85259" target="_blank">📅 06:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85258">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4217f405.mp4?token=WC3dZWDqhsvj0h9_iGz6_i9sCXPPKWkwywiDbX-F4axYJBmG5uNB-DTbqPGMows7JtaUdL6XOZfliTFoH-Y5GMfrWQAuaNCLFULrGHUyWHIbSuqj5HneODKmOBUeMIvvbBG0moT4Fdx4HfQxfy0IAZSBcLA6qutGM2GJrHs_8s3YrA9jJNHYJ6u4z6yRwIBRyl7R4xNapK-9NvZDzXhn85_X0wEqax0wL7OefYdI3uQoJr1qUYXr6XSIclccs-7UkWAWiCv8g8lI18z4LzUbEFT1RrR_-E_EceLZgwi5yufVrDR5XMYLd8SxubEObFVrkcYTEP1kFfNDSDN8KYFBPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4217f405.mp4?token=WC3dZWDqhsvj0h9_iGz6_i9sCXPPKWkwywiDbX-F4axYJBmG5uNB-DTbqPGMows7JtaUdL6XOZfliTFoH-Y5GMfrWQAuaNCLFULrGHUyWHIbSuqj5HneODKmOBUeMIvvbBG0moT4Fdx4HfQxfy0IAZSBcLA6qutGM2GJrHs_8s3YrA9jJNHYJ6u4z6yRwIBRyl7R4xNapK-9NvZDzXhn85_X0wEqax0wL7OefYdI3uQoJr1qUYXr6XSIclccs-7UkWAWiCv8g8lI18z4LzUbEFT1RrR_-E_EceLZgwi5yufVrDR5XMYLd8SxubEObFVrkcYTEP1kFfNDSDN8KYFBPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق رشقات الصواريخ لاتتوقف من إيران الشجاعة نحو قواعد العدو الأمريكي</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/naya_foriraq/85258" target="_blank">📅 06:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85257">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">موجة أخرى تنطلق من إيران</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/naya_foriraq/85257" target="_blank">📅 06:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85256">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ياعلي مدد</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/naya_foriraq/85256" target="_blank">📅 06:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85255">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ياعلي مدد</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/85255" target="_blank">📅 06:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85253">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1c6f8344d.mp4?token=AKgLOswgHbsdZ2w9Nk81YfHwgRZGbG7m8CEyxDFEWG-dVZXE3mu11U0oRndK2Al5nuhuwa1WnZY5oYHFFY_4NASVJ4v2IrfVcsb6nndwz0Xij45AI2LeHMO28Uc9zTD7CS8i3cWCK-kxQTkMeFXf0DhmsznN_fjDpy13l5hl7xiFkBZfJ1xogcLDCb66z48JI3ayM5NxHn55PS64OTtcGyOanO4vwSstngcN1uA2Qs5HOeMjAa6r3UFNSRsaKXDs6KQsduuMmXJGzEouxrghkLVAKkzZv3LfQQL9bQifcTmmud1JEzy_O0p5QAlSYcKeLVjrXcX6cpGK3ZmDIipw6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1c6f8344d.mp4?token=AKgLOswgHbsdZ2w9Nk81YfHwgRZGbG7m8CEyxDFEWG-dVZXE3mu11U0oRndK2Al5nuhuwa1WnZY5oYHFFY_4NASVJ4v2IrfVcsb6nndwz0Xij45AI2LeHMO28Uc9zTD7CS8i3cWCK-kxQTkMeFXf0DhmsznN_fjDpy13l5hl7xiFkBZfJ1xogcLDCb66z48JI3ayM5NxHn55PS64OTtcGyOanO4vwSstngcN1uA2Qs5HOeMjAa6r3UFNSRsaKXDs6KQsduuMmXJGzEouxrghkLVAKkzZv3LfQQL9bQifcTmmud1JEzy_O0p5QAlSYcKeLVjrXcX6cpGK3ZmDIipw6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تتوجه نحو الاصول الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/85253" target="_blank">📅 06:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85252">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجاران عنيفة تهز الاردن</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/85252" target="_blank">📅 06:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85251">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجاران عنيفة تهز الاردن</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/naya_foriraq/85251" target="_blank">📅 05:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85250">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الصواريخ الإيرانية تتوجه نحو الاصول الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/85250" target="_blank">📅 05:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85249">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c59ae5186.mp4?token=KLO3XtQIJRuCeqdF7zQ_zJGG9xEiRXXw6XMdKlkMTKnk_cbKH2SH2xGm51R_h1tAWeoFDWyBkeY8syXY3sCjTlvoLuCVMqKu5ymU2X0urMIwjj2N1gjehUwutNHf_O5gxYPu7VVToubb8E4HIhI0SEbxT0rXFgJWzc0KCeOm6aL2ddd_swh7C6A8WizDvBohCN9IyNtTYzaBDOxbZCGjeIOHdKMLr2OidAtZ_n1_zmYJ7MxjK1_BlvOFH9yKHxq-RUlLQDEBjZKVLDbFV2pNtLwcRllpuZBUC4jff7bENIYO3aj9bETfoxW8rCOzIcwWIplqEA9kGzNbVUtsPohudw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c59ae5186.mp4?token=KLO3XtQIJRuCeqdF7zQ_zJGG9xEiRXXw6XMdKlkMTKnk_cbKH2SH2xGm51R_h1tAWeoFDWyBkeY8syXY3sCjTlvoLuCVMqKu5ymU2X0urMIwjj2N1gjehUwutNHf_O5gxYPu7VVToubb8E4HIhI0SEbxT0rXFgJWzc0KCeOm6aL2ddd_swh7C6A8WizDvBohCN9IyNtTYzaBDOxbZCGjeIOHdKMLr2OidAtZ_n1_zmYJ7MxjK1_BlvOFH9yKHxq-RUlLQDEBjZKVLDbFV2pNtLwcRllpuZBUC4jff7bENIYO3aj9bETfoxW8rCOzIcwWIplqEA9kGzNbVUtsPohudw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القواعد الأمريكية تحت مرمى الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/85249" target="_blank">📅 05:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85248">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353c971c6d.mp4?token=smnwySeLvnCwpsCMDSTaUFa7gPZ-TAHPo8Bl_MCrfa3xgjMN86LlkSAfVff86nwdGQATeWEjkyXDCGikOcaAFmMNPdrJY3qkGBib-jZ43NkkpEyKAlrHioI8g5NFjSxH6IPmCo37AGkxbldZ-TN6cQmTGeh8VywQvg-u0yQHTKjOt1BiFoh1YOtERIW6-BtpbhQpoi7vkqDZ6Y3eKJghbNFkXjYTYvt9nfmf9oy7GRI_-vWPGwDYOXsY3qpbfyLzEEph9S9U-F54QTWCm6FNjWlrItCsnmIjXiT_k-1IxBpodAL32RQAPS75RHZyh74i5wEFIXtKCnfDGwMg-h1roA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353c971c6d.mp4?token=smnwySeLvnCwpsCMDSTaUFa7gPZ-TAHPo8Bl_MCrfa3xgjMN86LlkSAfVff86nwdGQATeWEjkyXDCGikOcaAFmMNPdrJY3qkGBib-jZ43NkkpEyKAlrHioI8g5NFjSxH6IPmCo37AGkxbldZ-TN6cQmTGeh8VywQvg-u0yQHTKjOt1BiFoh1YOtERIW6-BtpbhQpoi7vkqDZ6Y3eKJghbNFkXjYTYvt9nfmf9oy7GRI_-vWPGwDYOXsY3qpbfyLzEEph9S9U-F54QTWCm6FNjWlrItCsnmIjXiT_k-1IxBpodAL32RQAPS75RHZyh74i5wEFIXtKCnfDGwMg-h1roA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القواعد الأمريكية تحت مرمى الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/85248" target="_blank">📅 05:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85245">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTMeDzV_sLHwh3rqcxZO5zEfiqETfJghx3jlBjeYVphD_SM2E5yCuGCR6yvYbATJy9urnn2vqLUYA_EX0rqId--KehaxAW8q_izTflY9cpIVNdGcnk6J2HoZlWieU7QgyEoOYJLUXimF_1fmRaB3EpZBNOqumHFtvXQek3w0rs0ousMcB9t_Qke36JLvDFQvuMJ8LzGLbLp9Bq_D_-JikuF73VNJPUwKx2NZZ2gHi_2pkOlNbJzylcnBdeDsVwfnO7iA7LYod4eIMaQgpt1RzpjdBGRI_-FGhLHqb8kMT5F7OkeY6DqIoc5Iu4XQ7zfIQCC_autbrUcgGAVpFepM9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjcpy-6d8v8m43BnkHoQM1WoSo-BTmxNyeYEPy4_13Ko3EEg19i6v0q0AjRSk7CES6eFdzSb0K2jqvZdFDlY9WyFmg_nVmJ1pivxEh_5doeVOuDbtX-eIH89P2DYIY8G-2Wg6e8nsZpZuTHmpKr2w4ExlL9TuCvuqsn13_2Yd4MD83umzvaBwwAEJL7C1okHDJPnc9FPTsl3iNU4TBoYtQiFRUzI38eNmUEWLy27pgml6K8c3bcja5zKzw-vWOM1vFLCVEUrE6-vJ1054lg-kIsMkqAaUsSYoqSJitP5setE0vaoaw93SI2Q-HO2IdVeCg_ZIYsIdI6lF5QRMG4Fbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qvr94sJ6egAjwwI9dTZyMFEkx4yPo1ExVD16cff4gnjtE61KiAXhN8IZJQUfWiJbkoHXhLS0KWVv-SMpu8wI6HgAPIc9ynoplLISGwnT2ooUtlDj33LlFajQwU1wkGm3ZCwq0vlEstLex8wfjXDSvzB6Jy-_8YOuvZYHcC8mU1XkA6N81cDJhAWuaX3XBntbhbk8kMgTpNYFr9aU6H9ms8IRTkE77wqvrnR3bS_cHcWF8DyLuAAQvx02M2H5O6Us9dR_RHpKYWbcE_OrdTqOSqmFHX3EKONSqYO6p7lx82GA9SmymYLKHttOOwWs0Aj4my9wUcSVtilVPNaDXlugBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">إطلاق موجة صواريخ من إيران الإسلامية نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/naya_foriraq/85245" target="_blank">📅 05:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85244">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ae9c6675.mp4?token=U6Sabtw7Tbf9xuEOJpf5AFf5VX-WGRnqYH4oFxXP5aSogTOfVE70Hw0f99VwTGGFS6_mQwpgrrej2PWG8Qej_-oMxzuwWfCL4TzunwV5fOCeqr8gGoLq0VD-Ei6mlZ9SySvJamzTPSRxfxQUIAWpeNaS8AmVBf8fyNJRZqWyLnNBIqrLMAzp3Vi6_Zlw_IxlUGpWnyrdvpoT3TvvLm2uVBmTWbVQMeEe3IMv0Kp1625HjZ1vaZ2qGLsjxJ-WS0tM8nyQdCKP2c6olLDMSKHVxLDPVFfne3jL298UVO989GZ2wBlc1MG4WjQFXzJu0dxm65Z69RfiqHzk_13jAp910A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ae9c6675.mp4?token=U6Sabtw7Tbf9xuEOJpf5AFf5VX-WGRnqYH4oFxXP5aSogTOfVE70Hw0f99VwTGGFS6_mQwpgrrej2PWG8Qej_-oMxzuwWfCL4TzunwV5fOCeqr8gGoLq0VD-Ei6mlZ9SySvJamzTPSRxfxQUIAWpeNaS8AmVBf8fyNJRZqWyLnNBIqrLMAzp3Vi6_Zlw_IxlUGpWnyrdvpoT3TvvLm2uVBmTWbVQMeEe3IMv0Kp1625HjZ1vaZ2qGLsjxJ-WS0tM8nyQdCKP2c6olLDMSKHVxLDPVFfne3jL298UVO989GZ2wBlc1MG4WjQFXzJu0dxm65Z69RfiqHzk_13jAp910A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  موجة صواريخ تنطلق من إيران</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/naya_foriraq/85244" target="_blank">📅 05:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85243">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMZ28naGClPOAVdn3Q3o4KX6nyKsLGSS4TPTZOHyiZqveN0kVnBedh2fK_y7j_1zYeSgFBroJV58tkTpuIjQKdk3vF72ovicdmPyB85jNeGHS2I2reLSnLDHUfSDGEOqpUqKgOV0dnNxKnA4z2-g7XDrr4isWtYMejPEbxi0dfA3Rn_ELPBwBUdXZHkIqSMuNArVKVCzW23mmlwioaNWjMaBKjx0hzXiO9C-gbsa6DGAzunGrFoUNJVh2WGz5PAjWyi5i19ejQF0Oyn1oyHFxcC407Cr6BrPhMwNXeonw2V8eBJN8355LhtjjDt2aNUUxvzrNWHDu2wq33sWwMzSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
موجة صواريخ تنطلق من إيران</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/85243" target="_blank">📅 05:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85242">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">استهداف مناطق سكنية في مدينة الاهواز جنوبي إيران من قبل العدو الأمريكي</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/85242" target="_blank">📅 05:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85241">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
🇮🇷
مسؤول أمريكي:
ترامب لا يرى خيارات جيدة سوى مواصلة الضربات على إيران.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85241" target="_blank">📅 05:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85240">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a00b3eb82.mp4?token=mrDei35rippTtapYdE7Ri2uxbCSlAFezqDgNYnLUnWismxjl0pP8c-nu639EI55v-sa6NKGY4jdl-LcjBMcHdrSKv8hdyI7UrRNcMON2qtDNX2oHFJolhG9Y99BwvhRMbBiz5iL9RIwCemOI_RlfGCXj-hATYRfWqUekmOhxf7ZGt7QVxJeFht_2ywIffWZIvYABylfdWXFSkUzOmDJtFRREpn7WkPIygrOWOFT8tz4_GY58BFda1qToUn9HS7i8lxrZxWZs1CXgYKpPJkTzme4L_gKPyNtV3KxrwW9c37Nyma4WIcrbwxiy57IHOYyoZdA0ZWejNfS6YMiRt5X9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a00b3eb82.mp4?token=mrDei35rippTtapYdE7Ri2uxbCSlAFezqDgNYnLUnWismxjl0pP8c-nu639EI55v-sa6NKGY4jdl-LcjBMcHdrSKv8hdyI7UrRNcMON2qtDNX2oHFJolhG9Y99BwvhRMbBiz5iL9RIwCemOI_RlfGCXj-hATYRfWqUekmOhxf7ZGt7QVxJeFht_2ywIffWZIvYABylfdWXFSkUzOmDJtFRREpn7WkPIygrOWOFT8tz4_GY58BFda1qToUn9HS7i8lxrZxWZs1CXgYKpPJkTzme4L_gKPyNtV3KxrwW9c37Nyma4WIcrbwxiy57IHOYyoZdA0ZWejNfS6YMiRt5X9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الامريكي:
أكملت قوات القيادة المركزية الأمريكية (سنتكوم) بنجاح الليلة الثالثة عشرة على التوالي من الضربات الجوية ضد إيران، وذلك في 23 يوليو/تموز، الساعة التاسعة مساءً بتوقيت شرق الولايات المتحدة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85240" target="_blank">📅 04:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85239">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات في مدينة خرمشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85239" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85238">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجارات في مدينة يزد الإيرانية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85238" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85237">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات في مدينة فيروزآباد بمحافظة فارس الإيرانية.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/85237" target="_blank">📅 04:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85236">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7cdfe133.mp4?token=HKlPzKOm8ofmI0-aF9hxoWxod_1rV33exLSz91Pqn2B38frsPxGhQG9ogCI95DgvWeZ9I6aCXTkg0Bz9UPcq-aXeeNtrm8K424uefBue6s__TGZbJcR45WRrFzGHRNqlMG2jfTwbG7xmonQCLWl_4R6MLckK9qBJPp_eY3M1um3Q_FhIi70nDSlqIhEUZdFXsDD7y6b78cOpR0krvKFFAJSdPR4OWf40LD4tRcrTVsBq0OaFqLhIdLKrqaVkPiCGNZaakDyfCcprOwDermab9cf5dzOpoUGb2zpwCIz3JGgwf3ku4_iZWdnE5sVvMdTTSFxo6eR68R67q9xkXmNrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7cdfe133.mp4?token=HKlPzKOm8ofmI0-aF9hxoWxod_1rV33exLSz91Pqn2B38frsPxGhQG9ogCI95DgvWeZ9I6aCXTkg0Bz9UPcq-aXeeNtrm8K424uefBue6s__TGZbJcR45WRrFzGHRNqlMG2jfTwbG7xmonQCLWl_4R6MLckK9qBJPp_eY3M1um3Q_FhIi70nDSlqIhEUZdFXsDD7y6b78cOpR0krvKFFAJSdPR4OWf40LD4tRcrTVsBq0OaFqLhIdLKrqaVkPiCGNZaakDyfCcprOwDermab9cf5dzOpoUGb2zpwCIz3JGgwf3ku4_iZWdnE5sVvMdTTSFxo6eR68R67q9xkXmNrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية في شرق العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/85236" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85235">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تفعيل الدفاعات الجوية في شرق العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85235" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85234">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0d03f058.mp4?token=gDV2Ki1oHVVA1uCslwpWbydUb0ksqTt9P1JBcvHdrBkaO1u9nzvmvJfmL8IURROo6aya-byyjbYGegBvdxrHPEAYlejPeZljjUhlErKXY8z99DwGyR49oHcO3fJU7taWjeTtdlVeIBuYlGCTwPSMaSC9pb2QcdkH-hArnBXwKj4FvmD-mg8WpdW9_CreNNVU0rcGpjldQGt23EAFmpBdHX49FO5WEFSgFDT84oN1R2hn43hAxg9e3nxy_JpGWX8n8XiIGe0yzJp8n97fAhkI1XruknxYzVExFWfEyvEs_4kMdWwV5oPXw2BTM48cIGBFx8ALCNiopU9rx3R1YIL-wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0d03f058.mp4?token=gDV2Ki1oHVVA1uCslwpWbydUb0ksqTt9P1JBcvHdrBkaO1u9nzvmvJfmL8IURROo6aya-byyjbYGegBvdxrHPEAYlejPeZljjUhlErKXY8z99DwGyR49oHcO3fJU7taWjeTtdlVeIBuYlGCTwPSMaSC9pb2QcdkH-hArnBXwKj4FvmD-mg8WpdW9_CreNNVU0rcGpjldQGt23EAFmpBdHX49FO5WEFSgFDT84oN1R2hn43hAxg9e3nxy_JpGWX8n8XiIGe0yzJp8n97fAhkI1XruknxYzVExFWfEyvEs_4kMdWwV5oPXw2BTM48cIGBFx8ALCNiopU9rx3R1YIL-wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في ميناء جاسك جنوبي إيران</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85234" target="_blank">📅 03:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85233">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">😆
Bahrain and Kuwait, now</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85233" target="_blank">📅 03:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85232">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca971c5573.mp4?token=m4eTC1dXMyxQxsmvQ6vU1hmXpz8LTeg2vX04pMgR2jx79fDEr8oWBCdaSf5xOgqgMoUoxTlIqZ-Ou1EnZFAvQVyMFt1Kk35sPFeY-Rv5H6HkqY2jZxU0x7HIEYrQMU5GnsbxRDY6xIQn27MUgSsa4vhrfFGyxx8au3yDv8uw4rdNUQfeYmSYtQdJGy8W9SjrCjGnGVLjrHckYD2Q3IUxqsUtVb9Y7q8qMj9pvVr-Da9_9_WFtr_lzRYUrooueSZ25ok-XE-1Wkj-74dq1YQHCBBha4o5Cz6tEhB1tDV-DDVv5LXDPzdSxKOxhKSO9E9pKiuUMBD22qeR-_0lXnJ7Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca971c5573.mp4?token=m4eTC1dXMyxQxsmvQ6vU1hmXpz8LTeg2vX04pMgR2jx79fDEr8oWBCdaSf5xOgqgMoUoxTlIqZ-Ou1EnZFAvQVyMFt1Kk35sPFeY-Rv5H6HkqY2jZxU0x7HIEYrQMU5GnsbxRDY6xIQn27MUgSsa4vhrfFGyxx8au3yDv8uw4rdNUQfeYmSYtQdJGy8W9SjrCjGnGVLjrHckYD2Q3IUxqsUtVb9Y7q8qMj9pvVr-Da9_9_WFtr_lzRYUrooueSZ25ok-XE-1Wkj-74dq1YQHCBBha4o5Cz6tEhB1tDV-DDVv5LXDPzdSxKOxhKSO9E9pKiuUMBD22qeR-_0lXnJ7Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي يجوب سماء العاصمة بغداد ومدن عراقية أخرى.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85232" target="_blank">📅 03:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85231">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e36721028.mp4?token=QF2q17oIfAcbvr5U75h19jAyxzebrNwccHwbAg2ta85s6nejRmSR6LA9vvtNvo0bU2b1zNk87yn4NVopegZ7aN8RvDYfgEE0ziM_FxuD6lS-InHfb_T18DNRrt6q3pJPRPo7g8dqqbQuIFub7PzKlKJJ0eYYi29OZYOSjoL0xU0O41cjOsAnk_ObNATeZzEA2QLVUDn2Y2oCnrBek827NN_BoP8JyyJ-o9IRXeREDpH_LZZ-Dblq5QjUHBI09QWEaD2XOjcLA0ry37ZDyBB7h85YGej7deVlWI_uv21zkEkzv4uRDwa7iQr6-MNKOv7utvjOkujEKd5W9K04t9YZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e36721028.mp4?token=QF2q17oIfAcbvr5U75h19jAyxzebrNwccHwbAg2ta85s6nejRmSR6LA9vvtNvo0bU2b1zNk87yn4NVopegZ7aN8RvDYfgEE0ziM_FxuD6lS-InHfb_T18DNRrt6q3pJPRPo7g8dqqbQuIFub7PzKlKJJ0eYYi29OZYOSjoL0xU0O41cjOsAnk_ObNATeZzEA2QLVUDn2Y2oCnrBek827NN_BoP8JyyJ-o9IRXeREDpH_LZZ-Dblq5QjUHBI09QWEaD2XOjcLA0ry37ZDyBB7h85YGej7deVlWI_uv21zkEkzv4uRDwa7iQr6-MNKOv7utvjOkujEKd5W9K04t9YZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي يجوب سماء العاصمة بغداد ومدن عراقية أخرى.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85231" target="_blank">📅 03:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85230">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجارات في مدينة خنداب بمحافظة أراك ومدينة بروجرد الإيرانية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85230" target="_blank">📅 03:38 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
