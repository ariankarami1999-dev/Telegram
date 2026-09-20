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
<img src="https://cdn4.telesco.pe/file/NWhLFD-6j2D70rOJqjJ53lZlJ-oB8dSYMz5miJho6x2dkU4NsvubCdtT6F6MRS3u0c8IHRYf6E7KzZqoY_6Klzs2PpaVdYAMETqKhtND1ntUjaR-RI6U9ssq0lmrgLHEoBRv4NDvA8Ote1In4GVBuunJtQuX2wP3A5qXpvjGheEZI_F06aRv-81fVPSTjLpvF03Cv9kL-Ral-10xYTLpNs0CXoE8c2Uxv8d7ld7sM7xUiEjOsL27LP4OPbK9zIIBvxRSU8x-AtN-qR8JBB-ntxxfxWmNaHNfQP_V21kUDezol7KMeMR6-1vfp1tnfvd9vHveVXi0h1x1zZ7LJhWiAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 253K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 02:04:20</div>
<hr>

<div class="tg-post" id="msg-83870">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og98ENghO_iXKX0zox6pEKhZxnD6n1S3hRQDG8m_7EwdeElzFS1KZ6PVe2WV3cqsvQeG_vA_nt9lkTJScJOLzdddTzxLNed2arRljzNPcaT6hnkDOTwhjiHBAjDnyn4cM1fbVkGbmAG95ODjj5qKwTiDUYdbXErUF8qmJ4ZvEVMR8eC-lW-JPh87feQBz4HJgumYQs6kwI6gqGvrRy2c283SQGZxcDdrYovp16Dfdfz_PaIFCKFjPtc0MzJZRSkFKxaq32Mdm2_QvsvryZB26vuz2mYKGkspcG73dBIancTZIG8oXa-mz44Q4uGYF8DJjGVyTbSP0WZAVIAX5E841w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/funhiphop/83870" target="_blank">📅 02:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83869">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/funhiphop/83869" target="_blank">📅 01:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83867">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/83867" target="_blank">📅 01:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83866">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/83866" target="_blank">📅 01:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83865">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شاید یادتون نیاد ولی خیلی سال پیش ی بنده خدایی با فوتوشاپ ی ویدیو درست کرده بود که از آسمون بادمجون میبارید و تا مدت ها مردم فکر میکردن واقعا تهران بارون بادمجون اومده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/funhiphop/83865" target="_blank">📅 01:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83864">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/funhiphop/83864" target="_blank">📅 01:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83863">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b69b54bb2.mp4?token=Zv3RLRpDTN5dTSAiXBMtgzGJ3pLhwUyjWreDIqcn-oLWX813feOVFgv9d1Ii1quIfASm177NFvbR5ZXqGBaYCqB53X7yn3XJE8ISkEh0nLW2GQ-hoVlJLK5vkdxh3k_L7QLvFv5GNjRzFrhoXxcJFjkMsR3csx_GVGGkmYLasPQN5Qo8oV5ly9cXQSLVydlmfQ-SxvPA5eSKBGwql_Qv-20wDAL4LDIz74RMznf01Z9O7328tmxNvn9YJmei9j1YTc9K_Ip3d8qIZfK-e6KVwrv3TnQCVqIWQJ8iP_pTMZI0mU8T3MrQYPQiMYsIRht_Vy3WHY2nwrZYusk1eNfhpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b69b54bb2.mp4?token=Zv3RLRpDTN5dTSAiXBMtgzGJ3pLhwUyjWreDIqcn-oLWX813feOVFgv9d1Ii1quIfASm177NFvbR5ZXqGBaYCqB53X7yn3XJE8ISkEh0nLW2GQ-hoVlJLK5vkdxh3k_L7QLvFv5GNjRzFrhoXxcJFjkMsR3csx_GVGGkmYLasPQN5Qo8oV5ly9cXQSLVydlmfQ-SxvPA5eSKBGwql_Qv-20wDAL4LDIz74RMznf01Z9O7328tmxNvn9YJmei9j1YTc9K_Ip3d8qIZfK-e6KVwrv3TnQCVqIWQJ8iP_pTMZI0mU8T3MrQYPQiMYsIRht_Vy3WHY2nwrZYusk1eNfhpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان تبریک میگم مرحله جدید آنلاک شد  @FuunHipHop | FaRib‌</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/83863" target="_blank">📅 01:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83862">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان تبریک میگم مرحله جدید آنلاک شد
@FuunHipHop
| FaRib‌</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/funhiphop/83862" target="_blank">📅 01:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83861">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شبیری زنجانی مرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/funhiphop/83861" target="_blank">📅 01:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83860">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4-w9j0lFj55aukUbt4a4TF8OpbN-quBlWWFbxWuKJSxG5M4BzLLF8LHVnNzbC6suDcKeK-1JRUNOU3Itt8HarwpY1Frccj2HIb4fEmFH__NA8KOYJfMk7D1x7UsbJOeIWNApkni4c1NifaxoRKoZChsUbwSIQiMx6R2c5NSMfe8QN7sGDcHAodRMmH6AtO66vyYYnCZ9ZgCGrgLTNZ4Gg2anIlNOZdThXtlHfOeJXjEgL9wMh6pZo6CL1WnDBVWfDFkiP7sVBMAZdHfhu_Slr8DAypI3kjzLOO9OuGflMXEIElxg4TQ0_YyBBMk1nLujjbjPNL1mOfrSKMdmKcXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبیری زنجانی مرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/83860" target="_blank">📅 01:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83858">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jU8CVOqexpy_j4h81wu3A-qCB4-cuHk0oQA1262uvgWkjZJ8sXY5FlHNGvT-1RfK6lPWkQ83ARAgheXFvF6jPuMvZ2oiNFVYG4jmUhHDhpYHt3qr4bwkPAne4p3xijq8LK28WO9uS1UTXgA63OFsNkmo8XmBb_C4SAeok_fkPZfFmiDd09-q3AFxJLxz4hgSYNd9d36Zd-evSd8BxPa-mdqIdNwR6xYMH09A_WCIMNYPdtmLlg_9bn-deKUrmncjNuV_Zm7fKFp6IQ8WdTLsrhRFTgsnOBClK-Mof86am5covXw9gZxyefUgGLn6l5a6gZFqTZEo7wRfY9zh0Q6-Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozCw7v2BJx4kFfzSWdHTWxjXsXTZRpA7-puvZkQ9Kjff1XPe92wCUju9XTaLnEeY-7Qdxz_5aTsanz6U9t6xhWiSMiyT7YVvCOUQfLKV98M13xT319w19O8d8DFowYTQ4ZeCeqr7NgaVhz_RX1BDVUEqbBJK6M_neZHJA0aapRU2hmXlMyp5dIc2hcOxy473d6wi-RsqWs1LdeZx1sXeFnnLtPfAxjgQnh01YCJX9EZO4OLGT1magUgh39rzS1y8D-pbVYAC3OMIeFRqq9uWmtVpLcJt2dr5wwWVkzJIGgieXNf-IKRLI9mWNGIhRb_tiQrQ583ancnYaqVhEoFFLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چقدر زود پروژه حکومت لو رفت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/83858" target="_blank">📅 00:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83857">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4G2D_P1l43hCGHQCEV_fukn9uY9RSB9X0luCT_DnzFmoqKgX73trJCJI2y2cb3tx-pVad__OB0URltCucFiiMiqiBBBdv_dCNdZCh2Pg42iF8jc2nao7edF1CzGZ_llDcdM5tBSNyEIZ2twIxlvai9HaXz3VE2BPJjw7eQoIhSQfySWPw4ZbzfXJ89AQxVqJavZYxz-20p2bGFNdV8lVdVhbPzwHQ9Zc5Lkcwjn_jk_Wzqtt6jRoMHJVkhX6Q6mutaHXakmL0_4VAXTBE3n0hHDHFlwYQQ583ZJBGX1CqzTErH7P51We7D4ANJBxyhbGvweyJyQiqffi8Bi5D1BeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان امیر تتلو را آزاد کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/83857" target="_blank">📅 00:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83856">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">همون منبع
کیری
به طرز چشمگیری موثقم گفته که صدا پدافند میاد و جنگنده های جمهوری اسلامی دارن بر فراز تهران گشت میزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/83856" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83855">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">طبق منبعی
کیری
به طرز چشمگیری موثق بزودی جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83855" target="_blank">📅 23:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83854">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsnZNHSUf4OC6UgbN-8kifSgaKOrnW3O_ZA7CcR5iy_mP6jykklcGbEK8QesFnrPI52Vv9OIp9bDuKmG0MvUnCZiohBGSYQKccoFTAPKZoH9l_09J25ZlomQWGTI_hswQAy-9CeOWW6AmMHQBceJ-Uxj9I4HTfnBLMI_daQ7b9B3R6f-AOSTGoCcUJ8E_La9Tzg1jKWIGbKERkOVoaQf6WPzRVTpLLbNYJEdqRJ6x3gA9cSITCo4K90WfhGEAmcS4_BvAZaxkhBgUbwoYu31kr71kv5w3H31TZx8lYUPQjrVHMTmUZle0q-KLYcK9nr8I8c0-HABH2QBlmGpPasGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونایی که براشون سوال شده امیرمحمد بزرگ شه چه شکلی میشه داداششو ببینن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83854" target="_blank">📅 20:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83853">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به امباپه اعتماد کنید، الان میزنه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83853" target="_blank">📅 19:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83852">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بمب خندست این مورینیو
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83852" target="_blank">📅 19:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83850">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این کورتوا چرا نمیمیره</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83850" target="_blank">📅 19:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83849">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رئال باز پیشرفت کرده پارسال همین موقعا ۵ تا خوردن از اتلتیکو، ولی امسال فقط ۲ تا خوردن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83849" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83848">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یاسر آسانی > وینیسیوس
عارف اغاسی > هویسن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83848" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83846">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سر رئالو بریدن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83846" target="_blank">📅 19:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83845">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بابا دربیارید شماره 4 رئالو از تن این بچه کونی
حداقل خطا میکنی مردونه خطا کن</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83845" target="_blank">📅 19:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83844">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوتا کارت قرمز مستقیم داور تا الان نداد به بازیکنا اتلتیکو</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83844" target="_blank">📅 18:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83843">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JamL_tp8AIgXmf93bWUgwrOj5kJVIpq-u_OLF8oI3AZRnUKA0pyo1570hn1Oh6rtFBLYLdbLtJJAa8Xq8M8PBV0QKDVojjqoyKBcARrq7TXkNikPn9N-eiFKhRx67vYxNSzoiJSMR3V0i5K2O91sYtLklYzoJHJ6JRw4Aa1ejplS01pfELNSvP1DRSQdKYj7bmuYksnwiZcJwpLiVLQsW3hC20fVW-aD01LI-PWvu-Nruvy_7FrUg6LHVWC8gfOiN76lf5B7ech_GCwDBBbWHQWvJUyT1Oxj9Rv78P_ILbHiA16IQmBaLkBtTk6TS1a6XERdW_MCpg36tn_SX5IGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید با دایرکت دادن دونیتش کنید میخواد پول دکیو جور کنه پس بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83843" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83842">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMIrjkzVL5nlfzZAxc6THv4HM2soAnfo29QE_kgnXrwukDBY557KWYoOkWhtJnJlF4fCPyCi8ITIWlepzp1ErbKco8b7U-l2-O-N2Fibx3eDiHxYda76FqiDPCroowsZKOpgtDNQ1K0MW9Sxuu7eQ7g6w2QNHVBpcT1Yny2XEIHntceIyZ6KQRC3Q-f8bScg457_C6Iokjb2MMiwgEe6oh0YbPEKiVauKE2cnDXFTX8EEX-rQ8NPNk7g-8qIqKH9Gc2dlP99ii6uYgE1RCj2jAuyzd2Bml63Chk9f2Krqkty9aQ1QKd5zH0IRNrzicYHPADBEiEtV7gxp_dwB_o9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت دربی مادرید الماس مادرید رو ببینیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83842" target="_blank">📅 17:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83841">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9TkT7evL5U4nctq2ptU9ncO6oR9A4Dc5OIVjQxScyf1B5K76DjRBwKsiIkTQGVMC7cxpu66UdFZG4jzokJZo9-2Eo_aXHi55YCzEjL-CzllWrjl2e072KqfkOvZ4plsBERoiHoTzvD71Y7Hj3nlUVxtC4VrHDzslqKtgP6sRoDoZ3Kj4JnIjL66qtooqEgfldb3xhnQfBLRJV1X_FcQCFw9sla9Qmn7hAoD35-BGVN4Tk1nsnAUuiKswgigigMOnGLJ7uubcSHJdh6NJoIrbOaU5gqNtw8__hyLjRgrn1G3pvdbQEjeNLQlHb9M2M8zKKy8i1oWNPX8H8JXBMpH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👁
سود روزانه میخوای؟بیا بری بت
💝
0️⃣
2️⃣
🔤
سود برد برای اولین واریز روزانه
👀
😎
کافیست با مبلغ دلخواه حساب خود را شارژ کرده و برگه شرطبندی سود برد را فعال نمایید
🥹
💵
10%
شارژ بیشتر برای شارژ با روش کریپتو
🙌
‼️
برای اطلاعات بیشتر به صفحه بونوس‌های سایت بری بت مراجعه نمایید.
😀
🤖
ادرس سایت:
🅰
g29
👍
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106
📨
کانال تلگرام :
👍
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/83841" target="_blank">📅 17:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83837">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a15289855.mp4?token=e1I9NsydehZGffs7XUiuRBvFHYd1Z2EMs1oyvsWEjbJrh5F7e5IaGU5dxQbvDpVqFLPGPtNPaA1PD7t1aOb2L8Pmt8_Hy_PIlBi5fdizVNhgjD-dH6m0ykjXRJar9A0LrmNuVHtJWKD2-wsSLm5hMTIB7zysXdUy4tr3lpiu0UttSNVorAgR6inQA6jzcAPfTZKom-6N77gUP0ZueX2WFl2HGQSdCv7D0lWs2SI7WRZq6SZuijnCZaX7Xrpp_JTbubv-Acbc5x3llKdReYKkHA21FSLdBpgAabYZAFKMqZEU2Z6xDMBmLHdUTP1aALLVmNpy_woSBYl53R2Cc3EZNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a15289855.mp4?token=e1I9NsydehZGffs7XUiuRBvFHYd1Z2EMs1oyvsWEjbJrh5F7e5IaGU5dxQbvDpVqFLPGPtNPaA1PD7t1aOb2L8Pmt8_Hy_PIlBi5fdizVNhgjD-dH6m0ykjXRJar9A0LrmNuVHtJWKD2-wsSLm5hMTIB7zysXdUy4tr3lpiu0UttSNVorAgR6inQA6jzcAPfTZKom-6N77gUP0ZueX2WFl2HGQSdCv7D0lWs2SI7WRZq6SZuijnCZaX7Xrpp_JTbubv-Acbc5x3llKdReYKkHA21FSLdBpgAabYZAFKMqZEU2Z6xDMBmLHdUTP1aALLVmNpy_woSBYl53R2Cc3EZNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83837" target="_blank">📅 16:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83836">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جنگ کنسله
صداسیما اعلام کرده حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83836" target="_blank">📅 16:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83835">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «کیر، خفه‌شو» دهنشو بست.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83835" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83834">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbbae1cf6.mp4?token=iDmD0I_eXl9spfimrSQJCGdp9jRIolunQwaqyDXux4lIesPj0I61YVLZuEK3gHX8LCD5n_4Mqp89o6hjm9zvY7fcLQQZBr3Z2ka-xA6NF5ZXZ62yL0RyNy25Mvv_LNNYyWPsbCnnRNDnCc1ip1fyTmHcXHhGOPhi0AsxWikRL3Iew9PK0AsYVAISeITP86EDrNfWGqg3Pfmw_mcA6K-pvnbX2bmzuiL0wC-K6IxqU_QRdt-AtBTfLAJXuQ-PxEmKpPOUm_jYMX7qi3VT4PIWhc--kLhEHdW39Z2zHMs8sWDMbIIo3qNHdFeWtyQtTnPIM7gvzs_kHDik8M59izNxZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbbae1cf6.mp4?token=iDmD0I_eXl9spfimrSQJCGdp9jRIolunQwaqyDXux4lIesPj0I61YVLZuEK3gHX8LCD5n_4Mqp89o6hjm9zvY7fcLQQZBr3Z2ka-xA6NF5ZXZ62yL0RyNy25Mvv_LNNYyWPsbCnnRNDnCc1ip1fyTmHcXHhGOPhi0AsxWikRL3Iew9PK0AsYVAISeITP86EDrNfWGqg3Pfmw_mcA6K-pvnbX2bmzuiL0wC-K6IxqU_QRdt-AtBTfLAJXuQ-PxEmKpPOUm_jYMX7qi3VT4PIWhc--kLhEHdW39Z2zHMs8sWDMbIIo3qNHdFeWtyQtTnPIM7gvzs_kHDik8M59izNxZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «کیر، خفه‌شو» دهنشو بست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83834" target="_blank">📅 15:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83833">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">امشب یا یمن کونش پارس یا ما، همه شواهد نشون از عملیات آمریکا تو خاورمیانه میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83833" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83832">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">قرارگاه خاتم: آمریکا میخواد با چراغ سبز کشورهای حاشیه خلیج فارس بهمون حمله کنه، بزنید همرو میزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83832" target="_blank">📅 14:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83831">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">میدونم دلتون برا جاستینا تنگ شده بود   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83831" target="_blank">📅 14:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83830">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3daed41be3.mp4?token=FE9dZLyyDwATXeyYiKaHm_gt8RSyCNyLWwjDzAQN2Rwtui9kiNDfpSwNSzPLKSrT64jjyzAlP0V5aAeTN6FCGrbgJX0GPXuPddXAIjcatf2AtMDJzZ2yc1K1LJIp9__cQfiRx48GLDrW5xa39elqqGzFgeyPviKNrCFDNFeZlWcOedlhDTzvtDflCk0RIODPFCsWeP2HfuFyxbasiNlRYE7xzn60oFXfhVAhLuUE3zcWxmo7-o6RWBKsmeGgaT3FZDwLC3umDADYszl3G4DQoStdOHtzpMWZyzDIdPE8F7b6SQGjYKppxnKbBMAVe8fVeKRXZzmmI2dD3qB-kyXzAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3daed41be3.mp4?token=FE9dZLyyDwATXeyYiKaHm_gt8RSyCNyLWwjDzAQN2Rwtui9kiNDfpSwNSzPLKSrT64jjyzAlP0V5aAeTN6FCGrbgJX0GPXuPddXAIjcatf2AtMDJzZ2yc1K1LJIp9__cQfiRx48GLDrW5xa39elqqGzFgeyPviKNrCFDNFeZlWcOedlhDTzvtDflCk0RIODPFCsWeP2HfuFyxbasiNlRYE7xzn60oFXfhVAhLuUE3zcWxmo7-o6RWBKsmeGgaT3FZDwLC3umDADYszl3G4DQoStdOHtzpMWZyzDIdPE8F7b6SQGjYKppxnKbBMAVe8fVeKRXZzmmI2dD3qB-kyXzAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدونم دلتون برا جاستینا تنگ شده بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83830" target="_blank">📅 14:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83829">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=RiOcwpzYnA4MUPou51FVMCEqsfqnN1imBPL6hkDKF4ReSgtGzBwvY2Wvpi8JxD-B-BHm4WFdTrKGI2LEEig5-3zwe7UnaSthnVLrv_PQXrOm56i6ljfXmBfj-7AJlfwJ0LdZbnJWzekvnmBSqOofyeK61uSub_5qE1q3xIRkMuEz4s_v0bY3hdmoyJWHGYJ6tVcodX4hHM5waMOJTC7gjCt9GjWWiz4_cyEdKnWcquT8OVb1m4AW_SW7gl_CFsCAi_ovHR7gAnmu2fR4K-T-cjIRIs32wQaBwf_cNqxQUs4fbys2CiC2IiJmYHed4mP2RR0kc_vl5m62P5al4PhkQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=RiOcwpzYnA4MUPou51FVMCEqsfqnN1imBPL6hkDKF4ReSgtGzBwvY2Wvpi8JxD-B-BHm4WFdTrKGI2LEEig5-3zwe7UnaSthnVLrv_PQXrOm56i6ljfXmBfj-7AJlfwJ0LdZbnJWzekvnmBSqOofyeK61uSub_5qE1q3xIRkMuEz4s_v0bY3hdmoyJWHGYJ6tVcodX4hHM5waMOJTC7gjCt9GjWWiz4_cyEdKnWcquT8OVb1m4AW_SW7gl_CFsCAi_ovHR7gAnmu2fR4K-T-cjIRIs32wQaBwf_cNqxQUs4fbys2CiC2IiJmYHed4mP2RR0kc_vl5m62P5al4PhkQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83829" target="_blank">📅 13:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83827">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defb7ab2c6.mp4?token=qzXTTdS7NoCHqcInqkKWAaUvL-rrAi0uaHwbfcjP2uSKInZwnHCHBvdVDGdp5s331h50QasyOa46uI3ej_66I4mBO0GsGVToskFSsJlPfKN8YQTYRi9PGHJA34YinOJqSKQ89RPDQg4BGGClTwSDkCitW7fwd2pN9WclkwIa4-o3gABRVVC5H2njF0HYPEaBbbEVqaDoADbjsu-TGztqpsLoL5xu5fLd18vXt-auRjcg5x_wZLHG2nlakJ98BSDgYmAySd6JdizTXAPKlkniDf3yx2wxmJrU7I-YBGTM75axrVCPxfndI1XOy4s8_oixbrA4ODy4nE1viI-pLCS4eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defb7ab2c6.mp4?token=qzXTTdS7NoCHqcInqkKWAaUvL-rrAi0uaHwbfcjP2uSKInZwnHCHBvdVDGdp5s331h50QasyOa46uI3ej_66I4mBO0GsGVToskFSsJlPfKN8YQTYRi9PGHJA34YinOJqSKQ89RPDQg4BGGClTwSDkCitW7fwd2pN9WclkwIa4-o3gABRVVC5H2njF0HYPEaBbbEVqaDoADbjsu-TGztqpsLoL5xu5fLd18vXt-auRjcg5x_wZLHG2nlakJ98BSDgYmAySd6JdizTXAPKlkniDf3yx2wxmJrU7I-YBGTM75axrVCPxfndI1XOy4s8_oixbrA4ODy4nE1viI-pLCS4eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طناز بعد جدایی از شاهین افسرده شده و هر روز داره با آهنگای غمگین ویدیو میگیره و گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83827" target="_blank">📅 12:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83826">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334f5e7f1b.mp4?token=jKT96f2TGqNjOoFVYBr7ZPeJO272BK_PvTVe913dcVZotCb2-sX95xJLM4tHFGmMeXJl-uAyvbQM4ttdWNzizDkEiKUtUXH0tl6aSqO1ta4zJXAbsOQgHPpoKTtUDsQnED-qCAS0-t7RD6Saf6u2i3GSIcUXhf-CfrVQe6UxpgzCyX0TNGYZwrBjqpA6f3UU1cCSP7wFTwfDri1XOAB2XriGdS9Uj6yrm0QLn0wqzxDPjHlwjwGxTenrLcZ18I0BQ1w95EmJTyamKU4BWA2dmtqGdUPU4NHtOoNYYnADq4ir3oh5Gsu7uHfntDwTdi8mm1rs7tc4OdaS3LZNf3XW3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334f5e7f1b.mp4?token=jKT96f2TGqNjOoFVYBr7ZPeJO272BK_PvTVe913dcVZotCb2-sX95xJLM4tHFGmMeXJl-uAyvbQM4ttdWNzizDkEiKUtUXH0tl6aSqO1ta4zJXAbsOQgHPpoKTtUDsQnED-qCAS0-t7RD6Saf6u2i3GSIcUXhf-CfrVQe6UxpgzCyX0TNGYZwrBjqpA6f3UU1cCSP7wFTwfDri1XOAB2XriGdS9Uj6yrm0QLn0wqzxDPjHlwjwGxTenrLcZ18I0BQ1w95EmJTyamKU4BWA2dmtqGdUPU4NHtOoNYYnADq4ir3oh5Gsu7uHfntDwTdi8mm1rs7tc4OdaS3LZNf3XW3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی هرجا که هستی یک قدم از Ai فاصله بگیر  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83826" target="_blank">📅 12:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83825">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DairUmCgEotNDCiG-Zv3VQNEqQmd0yIIszliJNy1y_6vJkGxzlKxtCJuW8BmIu695HOk90ToTGfn4OvmF7TGg9XqvHpg_lsqBoEA7W0Pjwx68vlY8Z9eXrT6TRIcBggStKTLrcETwEZRdb7Q4glk_mIgW26CrhgkW9fwofxFc8OE5-nDaXyBRwmjTtIIAW7gSVDZFv6UcRqhVSP3vV6gDNrTSCB3wjbwcZK0aH-81q3HHWEVy2CtoZ4ZbSoRNdsqMWBoeIvLlGbjkFrAEt-oO1fwztSs5ZIEHNdIimmV0yEr57h5bmt-Qr0vEC7erUWdyWH3wPamiyc8plh2gaVlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
بورنموث - لیورپول
⏰
ساعت ۱۶:۳۰
🌎
📲
آث میلان - لچه
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R29
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83825" target="_blank">📅 12:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83824">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر کیش صدای انفجار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83824" target="_blank">📅 11:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83823">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر کیش صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83823" target="_blank">📅 11:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83822">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ایرانی هرجا که هستی یک قدم از Ai فاصله بگیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83822" target="_blank">📅 11:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83821">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">صرافی او ام پی فینکس بالای ۳ ماهه پول مردمو به بهانه های مختلف بلوکه کرده و نمیده، همه مدیراش هم داخل ایرانن، حتما باید فرار کنن که براشون پرونده سازی و پیگیری بشه؟ حالا اگه فعالیت سیاسی داشتن زیر یه هفته بازداشت میشدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83821" target="_blank">📅 10:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83820">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU63l6eH4aCx3B_g02nuvIbCEQu0UC7_ESZPuLrYAlTmt5P7ykRiHw_oK1pwPvyprM25KkztK5AQFctzq6RRXM6wXTPtcOZKEfhifWTdzyszqP6CGAhfn2rgFn4WoCittylXT4KStIGvjlagDxL9V-wX6mGaGgg-QhuKBidpyQxVlzL3eejYEx91K60y3Mk72QVbqr69OMeV2KCaDSFgYdDwPCe6MXLto1Xqi-WqJJfgzd6qyDLn8b0ns2v8RSeq8U2r3c0FquDTVq2qTGBnW0NIun_Y3-C3EemypJ76RY4nE_WQWNG9YrnOdTUQ3IsrCbUPNeVMA-vtK1O7JdUQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلوت کنید این‌بار واقعا تعویقه
تمام برنامه‌های عمومی‌ای که ترامپ برای امروز داشت (از جمله سخنرانی‌هاش) به صورت ناگهانی و یکجا لغو شدند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/83820" target="_blank">📅 05:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83818">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDG3wuhDwyS7SWOso23Z1V8Hzf0Lh33Dr-9dV4EwmkfkRd-oj7sdLf2AGPGZUM-hOfeU9Sp9vTGioOlwmK4ECptnyvAtaSepwyLGsw1maYqtWTbBgmP7j83WOi5j-TppBVsC315ZUypeDghjQEnfZmOlWNTb1SYVDggrrgpEPwJokRT1Gp0sBzEkbmts4-M_z8qe4ULRb4lXGgqlWfVdZJrVJ2fFa5UmA-2FNI1YZplpDwkxiFUp20exqKoWti_TNjgrQMD3meXhJhzYOMei3KeKsIeb7adP9bTm9s9Od5a2dulgT_9FK7THE5pG67Qlc-4c5oFItTgTf8XH7r4hdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83818" target="_blank">📅 02:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83817">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیتزا فروشای اطراف پنتاگون سکته لاپایی زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/83817" target="_blank">📅 02:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83812">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حاجی میگن ترامپ یهویی برگشت کاخ سفید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83812" target="_blank">📅 02:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83811">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی. تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/83811" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83810">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی. تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل،…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83810" target="_blank">📅 01:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83809">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی.
تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل، فلسطین، اردن، قطر، عمان، کویت، عراق، عربستان و سفارت مجازی آمریکا در ایران به صورت جداگانه و فوری صادر شدن.
یه هشدار کلی هم وزارت خارجه آمریکا برا کل شهروندان خاورمیانه صادر کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/83809" target="_blank">📅 01:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83808">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKOQnOTcGGWLUB3TJMjbUMdz3TtkNcFuLb0FOim1ntG7yzkG5l70rb-hw5tQ4rqp9jSFVF-eaV_iUOEk26J8eC4PqsDaAWZus4M1wNrhPz-bJOuiwBQqIOsEzSA79hfMdrbj-RdbcBXLo0bklt142I3oesUuHASZh6wvSjXTtcjtri8q5tfHu9-pp8ineCR5EWAUKHknWM5s39sFvWZWy1norAJdKMrUqbtpkL7WS0xYZDbVf_8hN7bKj1oB3dYqQZ2NLkuFlt8OJJfiFQXJXgjkSM26vzH0puXChyBpdI7koORv801csKN-h5gdtZeDPeQxoP4HMfaczxScfFz35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر نمیدونید باید بگم سازنده جنگنده A-10، یعنی شرکت فیرچایلد ریپابلیک(FairchilDRepublic) یه زمان لوازم خونگی هم میساخته مثل ماشین ظرفشویی.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/83808" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83805">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎓
آکادمی فتحی  انتخاب رشته تخصصی کنکور ۱۴۰۵  با ۱۶ سال سابقه تخصصی در انتخاب رشته
✨
انتخاب رشته متناسب با رتبه، علایق و شرایط شما  مشاوره در ۳ جلسه: ① بررسی رتبه و شناخت علایق ② بررسی رشته‌ها و شرایط قبولی ③ نهایی‌سازی و اولویت‌بندی انتخاب‌ها
🔹
مشاوره حضوری…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83805" target="_blank">📅 00:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83804">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCHJFCtPxDTk-e_a32CqT_mIViPIg-9nOh2v9gdQjiJvEvtqUvgpovRYfjLaM2F-jpps9ksw7CLVNoyWAtlilDTsMh1IMfHvZB_AfITSbq1hJHcGpF-641xCOxoXq_WnUYthTYRN3_Ina35eMpaYm35dbfqxqSZX_RBo_m77FKaEKkT2e7TnHH1sM627rcbVA94hM1y44YlD9xHfc6JoHyB4pDlRkq5jknKMgvRMFGmkApMAxB9aBc5gy_851RyYD9f4V8GAGPMgkFlvMyyGFxNNnjuOd7W-oy42p9yl5trn-CxvQWMap0ENPf6v0uSzXjtFsVLtjyMFUuQO8Kd3zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
آکادمی فتحی
انتخاب رشته تخصصی کنکور ۱۴۰۵
با
۱۶ سال
سابقه تخصصی در انتخاب رشته
✨
انتخاب رشته متناسب با رتبه، علایق و شرایط شما
مشاوره در ۳ جلسه:
① بررسی رتبه و شناخت علایق
② بررسی رشته‌ها و شرایط قبولی
③ نهایی‌سازی و اولویت‌بندی انتخاب‌ها
🔹
مشاوره حضوری و آنلاین
«انتخاب رشته آگاهانه، شروع یک مسیر تازه»
https://t.me/+XFqj-oe9FrdmYzBk</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83804" target="_blank">📅 00:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83802">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این فلیکو اخراج کنید ناموسا، یعنی چی کلا ۳ گل با یه نیمه اول سخت؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83802" target="_blank">📅 00:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83800">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83800" target="_blank">📅 00:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83797">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه زن دومم داشته انگار پوتک که اسمش دُرسا عه و فرار کرده</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83797" target="_blank">📅 00:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83796">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آرتا ویس یکی به نام نوید رو تو دیس پخش کرد که کون پوتک گذاشته و داره تعریف میکنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83796" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83795">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آرتا ویس یکی به نام نوید رو تو دیس پخش کرد که کون پوتک گذاشته و داره تعریف میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83795" target="_blank">📅 00:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83794">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جواب آرتا به دول سه سانتی گفتن پوتک: لابد آمار غلط داده دخترت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83794" target="_blank">📅 00:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83793">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83793" target="_blank">📅 00:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83792">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کیر تو آرتا داداشم رافینیا چه هتریکی کرد</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83792" target="_blank">📅 00:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83791">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83791" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83790">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pao74XGGQQ_1LJYtee1lHGt41_DSiz0a-sLXycczSMfHA2rWJPlAxa5QSrgJSVnbFTOVEuzb27x4-hikOlnIH8nIa4V0hUaeWjcZMt6k2aGF35R1a33Ktpm0h20m6tCo2MqAIZFSG_RqSijPR8QPURJ8ba9gaIqIlS3bumEBLw7UpRHzR06Y9XryTsCsIUea2mkuLtRiqujjx73Xy_l_PlC0IJqNQ1FuyDpWIq1EgOsQ3Qut35hx2Ya8NoeN_I9LN0EI7EAHyZ14ydu1nhWjl3hhnHpP2vtZcBVG21hOequKCCAZzl0gkeArEpuzcYq2T9F3hkrzhLWlm7e336l87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83790" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83788">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کسحل رسانه ای به من ربطی نداره ینی چی</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83788" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83787">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به من ربطی نداره ولی اگه پوتک هرچی گفته دروغه اینهمه فشار برا چیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83787" target="_blank">📅 23:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83786">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83786" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83785">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کوروش به معنای واقعی کلمه دیوونه شده
داره به تمام مخاطبایی که رو پستای فحاشی تو چنلش ریکشن پوکر فیس (
😐
) می‌زنن سنگین‌ترین فحش‌ها رو می‌ده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83785" target="_blank">📅 23:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83784">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کوروش وانتونز همراه با این ویس، آیدی یک اکانت تلگرام با نام محمد باقری را در چنلش شیر کرده و مدعی است که این اکانت، اکانت تلگرام پوریا پوتک است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83784" target="_blank">📅 23:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83783">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPxeCWbaz6hq2Viif2mEauMwKW-3JIS_-JgDckAjxOnoY8SjsK5k_XT1RwgurD2l-kaMjTs77lgd5M6VIWpOC_rWQ9CYmidRBOxsV1oGld-VNpR6kBYXgJkF1ooH7MvdN4SoMtkhg0Ou4qKq2gbApyBzSuN_jF5ThkcxjZvz0DjfKVG1fq5dpAB9Xv-zNLvNTkehGMip3smQ4HMj1_E0NWnjvINZmjn2qmISepzjeiFVNntNFIPmRDYReSb4iY6KY3Y8ujaOIb9I5jZU7QG5oP9y-AqylQwHIpvbQ9D-ue_iOksVSTqnx5X3R4gOw7_mWqJMuClSmmeIG7Sg8bGguA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما که امشو بیداریم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83783" target="_blank">📅 22:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83782">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrJ_vZoWYvnRYb_A00SxZ2SYmMjmPB2cxkmIxHICNemVB5psIhSULEIQXXN54ugjJLAU6U7LBke2H0qUA_0AhwV4RmtEKbuB4qXT8LOt-4jrTFnSnftBjYAq3boQWRqbOJiJAydjlX0zx2uj2O9uKjzWkRvVrPE_aOEypztcFmfh2sdAv19K_5hBgqZ0XiHzOr-JVeKMv0Wn9RPJBvMVzOD4ZkJI-QP-hLW1gYlXqH_MOODqD8L9Of2wHcAN-AUxrUcN_51-49Q_g0c9ybXawRuNZBuzPzIJXjJz93And6xOVzg941hC_RFCVOIC1pFyEpb0jk_2Vo9LbvkfiN6qMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما که امشو بیداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83782" target="_blank">📅 22:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83781">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f81d21e878.mp4?token=JzGxata3OpcEJMAt-YRNJrUc6BRYqkJTgqepjd0a3iTkeEydIy4LgGA5GCmCHCNOt8iCVoW58idh6B1nvU2JxdCNUYnk9liCYvPEFxN_Blnd_XFQRBv_RoHvle8w_m09huzkxYmO7CSR8IrDsLyLrKvqJ0g5NL3dpTYdpC37slu6rQR4etncYNLTejXeViz9ZT_VM8xDp2xFuiKfX06BSQq3IPU6O5JessTEfD1IUV-QlV5J39S1CDZ8EUDhLYAczTOW6Qp6S-uG-vJNYuxM7PrO0_7EYoaC8A-eKJHl3788rO0uYwzrG-lxskadPvt6-6P1gn9ESGNhyv3Td-h95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f81d21e878.mp4?token=JzGxata3OpcEJMAt-YRNJrUc6BRYqkJTgqepjd0a3iTkeEydIy4LgGA5GCmCHCNOt8iCVoW58idh6B1nvU2JxdCNUYnk9liCYvPEFxN_Blnd_XFQRBv_RoHvle8w_m09huzkxYmO7CSR8IrDsLyLrKvqJ0g5NL3dpTYdpC37slu6rQR4etncYNLTejXeViz9ZT_VM8xDp2xFuiKfX06BSQq3IPU6O5JessTEfD1IUV-QlV5J39S1CDZ8EUDhLYAczTOW6Qp6S-uG-vJNYuxM7PrO0_7EYoaC8A-eKJHl3788rO0uYwzrG-lxskadPvt6-6P1gn9ESGNhyv3Td-h95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب با این پست اعلام کرد که دیگه با فوتبال ۳۶۰ و عادل فردوسی پور کار نمیکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83781" target="_blank">📅 22:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83780">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUGtWqzI0RdIn7Lz0uWVKByt1pmcxHeRI_6cRSngmBW9gi-p4sxsPG9Wq-4iDVMHY2APsp71sMtT6YxUPKmjp3s9dOgsStpigAAmOz-bjdBEPe40I-FHMAbRBedcz-ZQNJFBmhJIIxbMaTZm2f02CMtymWdTJwbdSrWTwa_QVNMMDhNs189dCbYhJQQZEFMXA6FOh5uyQHQqbtaMQCWXg9QnECmISU-ZaAd83gyV-9UBjmNXOQXeDQpo_hqovx6eZx6Md4iIUYiYXLbsl77pE8bpVGIB239eiL0cYLj9ikXf2yqI5DY6BpLs8aIz-b_BKN5OIpniY9S_mMSFUPiowg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرتو گاییدم چرا تموم نمیشی تو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83780" target="_blank">📅 22:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83779">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DP07MRC7NaccgW5w-xC9kYrxnOnceSo63FpgFye5OeYf52HunKbe8hnCRNuIrTeH0xpijEkOAnFcAS23BPC7d8fst7zPn7WRLH8ID_OL5wj7PvXbyCSDRKIzsWsJXErXkbzSAUjK5oc-4ayawt0Uqjr4d35O_EtPuRxPBqcdIe8NlDzXCEV1T0BAPKecCTKoqEvcwu4kNCNFz49UnQHjtKL3Y4TruJf-EXpT_B0-mi-CT6jv7XbsUeWbY8E_w8YzT7tFUKfpj6okupSfqlxt_l4mmN1O-N5dCjt76SAE-xo3xbFda0LcX1AZsWAtlIqEaV7JuZQYJajy_BcleXnixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
10٪ شارژ اضافه بر روی واریزی‌های ارز دیجیتال برای کاربران بری بت
⭐️
🌟
📢
در سایت بری بت وارد حساب کاربری خود شوید.
💸
از روش ارز دیجیتال اقدام به شارژ نمایید.
🔋
🪩
بر روی واریزی‌های ارز دیجیتال تا
0️⃣
1️⃣
🔣
شارژ اضافه دریافت نمایید.
💰
✅
ورود به سایت:
👇
🅰
g28
⭐
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
🌟
کانال رسمی ما در تلگرام:
👇
🔗
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83779" target="_blank">📅 22:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83778">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83778" target="_blank">📅 21:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83777">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کوروش وانتونز با استناد به
یک کامنت
،
دیس‌ترک خود
را پر پانچ‌ترین دیس‌ترک رپ‌فارسی نامید و به فدایی فحاشی رکیک کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83777" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83776">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243abf4097.mp4?token=U2ZBqNPTNONvil0zdeT9XU8klgY6sjeZzrJdTcO2F4Uzl88oDabxxUiv00eH5qLtphu9-CWg_r15ThYOJ7BYOMrnv0l6yUp7Jf6jOnhKILCwAzIakmoXyWbgHW6DmaxiuREP4La1w5FtoUSHkpo_0oqF3J9Z0vKdRSjFxEBKOYwFiDptKAqy9W41CQR4qsImEXavhCFEIW6QXlE1JhQyqYodChrIreXNxDC0x2Yeqaks3K9tz3OLcPiJDxJgWBwnFyH2cwCJbeNJjtxRtoqPBh8qVib2GfPv5KC-ewvKLXbnQNlK0p9_ksuX3cfFUKp_aefPtKGNy8-DGcHkCY1QKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243abf4097.mp4?token=U2ZBqNPTNONvil0zdeT9XU8klgY6sjeZzrJdTcO2F4Uzl88oDabxxUiv00eH5qLtphu9-CWg_r15ThYOJ7BYOMrnv0l6yUp7Jf6jOnhKILCwAzIakmoXyWbgHW6DmaxiuREP4La1w5FtoUSHkpo_0oqF3J9Z0vKdRSjFxEBKOYwFiDptKAqy9W41CQR4qsImEXavhCFEIW6QXlE1JhQyqYodChrIreXNxDC0x2Yeqaks3K9tz3OLcPiJDxJgWBwnFyH2cwCJbeNJjtxRtoqPBh8qVib2GfPv5KC-ewvKLXbnQNlK0p9_ksuX3cfFUKp_aefPtKGNy8-DGcHkCY1QKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیانو اینجوری تهدید کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83776" target="_blank">📅 20:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83775">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سهام شله با کون خورد زمین
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83775" target="_blank">📅 18:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83774">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برایتون یکی فرو کرد به ارسنال   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83774" target="_blank">📅 18:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83773">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">برایتون یکی فرو کرد به ارسنال
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83773" target="_blank">📅 18:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83772">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdD8CzANbLw4rSm4ftMuW3g4rdYEd4mz2l_h-dp0sjWWpJoSIRZc_7kohHEJ-5wepm9GE_BoEftq4zAWR6ZB9_tQ_zPqQho2DL1TiwnvK_Bgnp8ESqBSdwHeub1YO2jBpmBAivkX0X46-FaZ3rbFk1r6kB-gvhpmcbvY-F4j5Cl-URwvGwKfRr-O2n7YY9UX73BIY01ScsTlMWrpPwwwHCdrnukeYdpV7Wmvl8vVPvEikHSGuM1Qqfuw8XMgTp2clkmcoHRzXUadGB348V6fFrFiuAhrWzze06nMB7Pn1e7EKb-SaeyosGAtgHQN7cLGququ3VrmjOmjE2_fqxrNrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حافظه_تاریخی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/83772" target="_blank">📅 17:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83771">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تاتنهام بالاخره گل زد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83771" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83770">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تاتنهام بالاخره گل زد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83770" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83769">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvHO3WWXc_1uxBI-yoQe016qlb4ZjGCMQTJEnKypBPnZoL5WA2nDM6sGQbNL1KugtQ4ySEWAfSC1lllXFMYSGv1pRhQq2hWFygu5mrwtdTJdtzmVQ1LZKP7eDCUA080a7Ijrs9rVHx1gba2k3Z6rklfILYg_q1VMlvGNp2EXLvfwWRdyU_KJiP69ZUqUWMs_k3GzYbZsB15iQRzCH_EliLW4CXaWiy-S5-99cVt-MhfRS3BBAHXRzl65s1QV9znFHxeMDxuiOilWN_GReF1CYu8UJo-6FhnURyO5WL2Q_Nzqeguwzk81UWs48YVQcWCz3o7HFOYq-jRFq_ubpvJn6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/83769" target="_blank">📅 16:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83768">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqzsD8kNxlEEXXNdf0D6uSfZf_AWv0FcahKRV0dyucM7VCDrHIdJ8GAaqed8mkflOMYIPJkU7yb7rwXKXR4Cc3NRtVsESnjPjUB8j1yZohXM3qy_uYB9q-8fpei0pu45CMvGpd-zo3YMJZnW-2MW3BljwPx__CZZbeVgs6klb65UJYoMlOIeWmcvAu62b3VCoToTvfYodhtuakSIQ5H7OT04CGhIGbaKXjwP5NCnPg83dY0QUjXuV6Ttz7yiFtPjAw7WJIOoi04J_kCtZraxhShzHnYBQ7nueBdoqmTSSf_j4DAEWvpQ22whP878rKABCAXbtjAljFpcA_COXbaSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممنون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/83768" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83767">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqRzla7_lFYgTyezB-1mg9jANKbPgtn_btQJkgwEFgLaJxzXtA-aH95xuW-vhhPRLHDD8YUJTC9-MeyRNJla66QBgEOLG3qNqT-Ci7y32nXVZneieD-L3LwC2JmX9uljF1-pax6fxmSfcrLajcvNGF5_fKvZ8dKlE5jqbrsZEJL4F_Y7-fqIRXE9ibCLWYxmB70thohtM7_TLbRNwFihh4JBhoPqAz-iJWKIsKQf3E1eSGtapGQ2wKTIFQMYrGIyErJvdywSgH5rYWz4zNShA1LVtaFgrYhwZW5Quu2-YU4eWMXv7Wv2Ln_74RWc1l5_u9kl21FXWkc39api_bEqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر قذافی که 7 ماه پیش آخرین امید مردم لیبی بود و مردم لیبی خواستار برگشتنش بودن و داشت با رسانه ها اوکی میشد تو سن 53 سالگی ترور شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83767" target="_blank">📅 14:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83766">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به قول امیر پارسا و ناگهان کص ننه چلسی</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83766" target="_blank">📅 14:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83765">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خروج رسمی امریکا از شورای حقوق بشر سازمان ملل.
آمریکا اعلام کرد عضویت و مشارکت خود در شورای حقوق بشر سازمان ملل را پایان داده است. وزارت خارجه این کشور شورای حقوق بشر را به ترویج ادبیات ضد آمریکایی و مماشات با رژیم های متهم به سرکوب مردم متهم کرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83765" target="_blank">📅 13:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83764">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7CINoD6b1Ft8wEQIInEEUNPqkRB7r-EEItvbG3xuC9FybJ-m5G5cFPjBjCHAwRpeGtFsrd6-j4ZagXzBllCd-IqbV-h8uRkAf21bhm2VOyMuRasy7qYaCZ_8uevQbb7D3FMJxrxXNHzu8_ANr-MOu7xsvHzcrj4ju0bvG0fpSHv7liFnxuogjrnCzqVj6IsbQUpaPtSnjXAtYMBUz0Kkq4U_FG6STXKgqOS30smgNSPE1KPqr944NZVXSxOYaDeNmckQS7CA8hQbMo8iJFomfx9x7Ujj29r7l2ORgD_6OMkoQNfsyrZ3wcNW3jNcZOqKGx0FhudhAv_SaLTbsr4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسدالله مادرت گاییدس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/83764" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83763">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ff3a5a22.mp4?token=KNK3HmOKIkCIFoi2siPveIO_W4s90OK2uI4snRAwAxUIybmMvO1yuVpjokDFtU_pKSE0aqwhyrcHQMT5sgUQCeGQuVml_mHAX5ZCNtr3EL7Se8tKfaeO8_MRvHrpwgLhddl0Esy0W-C_BasCIjSr1h9SM_4rax9gjWIAcjRKXWvJCEqRZZXmMzQWwhaYP1UzXFKhPD_H9MGj_a3UB1mazQQWZbsuqL_YcUvSdnx0BohAicXkTsFhe9MmTPBeBLz7OTsRI6gQ3wUVZlwHoAo_Qt-mp9A3sGeBQHclUs4EnpWN6xnNzKxwzxc9fK5SytVKiDtdLD_KXGJmlrqgtHtZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ff3a5a22.mp4?token=KNK3HmOKIkCIFoi2siPveIO_W4s90OK2uI4snRAwAxUIybmMvO1yuVpjokDFtU_pKSE0aqwhyrcHQMT5sgUQCeGQuVml_mHAX5ZCNtr3EL7Se8tKfaeO8_MRvHrpwgLhddl0Esy0W-C_BasCIjSr1h9SM_4rax9gjWIAcjRKXWvJCEqRZZXmMzQWwhaYP1UzXFKhPD_H9MGj_a3UB1mazQQWZbsuqL_YcUvSdnx0BohAicXkTsFhe9MmTPBeBLz7OTsRI6gQ3wUVZlwHoAo_Qt-mp9A3sGeBQHclUs4EnpWN6xnNzKxwzxc9fK5SytVKiDtdLD_KXGJmlrqgtHtZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد مصدومیت خوان گارسیا فلیک داره رافینیا رو تو پست گلر تست می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83763" target="_blank">📅 11:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83762">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7124a1535.mp4?token=nr0j88nyHK0zAmk3rUYy-mmBHdyOuDJSI79abwg6eSYQtNM-EnWJ6XfpCJAXve_J0ObjDTOujmEPMVrieEMCHpL_NYwRCOwsXOBlnxQiKr1ohD0onF08Dpd_Ljs_W-u0qGvyxB1ZdDhDODHzoRAK-L90w5qaDuAX-yMqUdALK34LCrfXiknjpZloTNP_nxntrvaqeYhLSfNt3Da1_0i8E3kkI_ZtVr1cB0HTv-rOdFQRbxzLl76D6iw-h-tdkkxbX4qtR8zi2HyV2_VfqQDiKAFBVHehKHdI_myGrrd8sVefaFNIywxT7Wz0PHEGR9-ZYAFLIKnzyQKHVsM46SH9rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7124a1535.mp4?token=nr0j88nyHK0zAmk3rUYy-mmBHdyOuDJSI79abwg6eSYQtNM-EnWJ6XfpCJAXve_J0ObjDTOujmEPMVrieEMCHpL_NYwRCOwsXOBlnxQiKr1ohD0onF08Dpd_Ljs_W-u0qGvyxB1ZdDhDODHzoRAK-L90w5qaDuAX-yMqUdALK34LCrfXiknjpZloTNP_nxntrvaqeYhLSfNt3Da1_0i8E3kkI_ZtVr1cB0HTv-rOdFQRbxzLl76D6iw-h-tdkkxbX4qtR8zi2HyV2_VfqQDiKAFBVHehKHdI_myGrrd8sVefaFNIywxT7Wz0PHEGR9-ZYAFLIKnzyQKHVsM46SH9rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اشکان شادکامی میتونست باعث بشه این کصشر قابل گوش دادن بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83762" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83761">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiG30pYGkLODV2toM3-tRr5hkJ253oea4_8X9-VWMADHZVpJrwb2AhjO6UdbERGBCZatDI4FJeMRofey4DWz7m5vrXVK0t8N2P26O8-cKASmMTIII-44hBkKVqXQkLmqtH-EfQJt4QqwAX1jh-RM4hSCHA1p9cATbvP9M97WHgFv02bI7lORt_uasnfdAy25g7UcafFFGOA2QYN3ne6-rVi7thiPoRpfjJxCI3kTSL95OihPkn3jhA55yKYLIvE4ARXo0nFxLreF_TRuHxoKYdvDSlAU7pCEBKP91s-UysMDiHTmpHRPkPZX_JpKl8ErLsBGDeUoYiaSmPWYAyPPYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس شیر ایرانی رو بعنوان "بازیگر معروف هالیوودی" معرفی کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83761" target="_blank">📅 10:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83760">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tj4Ji6PNkLMLvXargQkIXaXA_LhPSSgbgFvluj55YfS4KDu3_GzIubHOeF4Cdg00oSYm3aAPuhaCLJdlTiXRB24VE25PmJg0r-FZJxUV85N6JY3f-V3HWkEEqZHkpcrl2KnjBOrc5CjErPz86VPPKmEQ4iY7KptPKnStwYg0ZUeNUw5P48qzx7mkr3wNSJ2CjRy9XQU8ioo1adm10QVqmbtulE9oSo-ReWh0eVqGMPbRmK0_Q8Gr7AkUabm5TUp2ozqn9sXoLwhpPSz5qoGu9-Q8RQ7Deqg0YUmOqzw6q-7W72MM-3UAQgzxTU0C_Fkmr-vE4gJmwuq1d1TJVrptLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
سویا - بارسلونا
⏰
ساعت ۲۲:۳۰
🌎
📲
اتلتیک بیلبائو - دپورتیوو الاوس
😀
ساعت ۱۷:۴۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R28
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83760" target="_blank">📅 10:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83759">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">افزایش قیمت بنزینم نتونست صفای پمپ بنزینا رو کمتر کنه، کونمون پارس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83759" target="_blank">📅 09:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83758">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این امیرمحمد کصکشو با تیر بزنید خیلی نرینه به مارکت موسیقی ترکیه، با همون بلوک۳ و سمی جنک و اینا جمع بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83758" target="_blank">📅 09:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83757">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مصدومیت اجازه میداد میزوگی اصلا نمیذاشت همچین سوالی تو فضای مجازی ردوبدل بشه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83757" target="_blank">📅 08:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83756">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c6f49b83.mp4?token=L8umKcNMeMg_-Fe4EI0cWjQ3ExlbINsCvMfhg_QUl7KdvsWfrRfMl8N6IKZmLl38zwb-6QVnhjBNEGfTUntekq-xpHGcoofxnaPFyDyIapkcO3p1WNUcE2mdvqwo-dB1DlHeyHaDtqLiyyEUMaH3MAxBGmayI3Xqk7RSWXJ3ZNCKc12x38v69GFng3TXdSe3ilQytYCU3UNhbEaPxTvVqIO0pVQYjvg18G-DhJlLZ9GqvFF6YCsEh676ezSJdWyfh_IOYmzqMlPPFHTRWbVdFRtffJMvHeT1yzlozlrBzDwGbPPWNJzEEamPvDmfSPjv-Mgh9j0lHGUlXLUWgSZjeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c6f49b83.mp4?token=L8umKcNMeMg_-Fe4EI0cWjQ3ExlbINsCvMfhg_QUl7KdvsWfrRfMl8N6IKZmLl38zwb-6QVnhjBNEGfTUntekq-xpHGcoofxnaPFyDyIapkcO3p1WNUcE2mdvqwo-dB1DlHeyHaDtqLiyyEUMaH3MAxBGmayI3Xqk7RSWXJ3ZNCKc12x38v69GFng3TXdSe3ilQytYCU3UNhbEaPxTvVqIO0pVQYjvg18G-DhJlLZ9GqvFF6YCsEh676ezSJdWyfh_IOYmzqMlPPFHTRWbVdFRtffJMvHeT1yzlozlrBzDwGbPPWNJzEEamPvDmfSPjv-Mgh9j0lHGUlXLUWgSZjeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت اجازه میداد میزوگی اصلا نمیذاشت همچین سوالی تو فضای مجازی ردوبدل بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83756" target="_blank">📅 08:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83755">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUDX6uHn6PGTAH8-0mmEP9TyhgyyER7a_nZYTyiOdibqi4QgvR0qUDkCwz8WaGe4s5nxySBMmis5vWutNGcU_bOnQA4UE0ItrhUDp9NT7IZtk1c-FPhFUXly2eatgAllRswCv_OaDk94cMh4rtTv55s-Gy1zEi5fySGAvWBrbzUS43O9CY1Zs2k4uG2CGRN1eTc4B65SlCHNmjosQn4S4bAUTrlZvrLiCg-FzwJyn2k9xtkdbd_e18xRRYGFuVApzv3CRTyAy7dmLfq3bWqx69Wq5oT-bM8itUETiW3UziSGHMpmIJo1l5_MR_5gbyDMvhJVN-qiuMoDUqlWKxcPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرفان کیر تو دهنت الان اونی که باید این گلو میداد تو میبودی نه سیجل.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83755" target="_blank">📅 07:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83754">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgWglrX5J_0PI47dhJZWOtpuM-UnGvDTaqw_pg2QCoiXE3SOHK7AN6oR6pXcfOyoMHeOD893u15Fmv9dyqP_SRp2ZPTwFkvT8bjJvKoFg6ciujoird5ihNTmcZitrZ92bHZ2htwhcpco5RRzd-xsrXwmUWy82tP0pGgvzJ7yPsZiIY2AUvfTFg4G-PGKKDoKhyQ9Sa8u8CizsA6phvMKwLSSnQsVnKZ1Z7aox0S7kECQacEitvCy1gzsGU9Jy_qPlVBAHeCFSavz7fuVtHxbbQhyjeMmYltHD9x6Qa4rJk5cD2872uspbhUn00aeNn9PbvHmriJy7BGEccxjNC_1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/83754" target="_blank">📅 02:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83753">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دیگه کم کم آخرین باری که یه نسل چهاری سوپر هیت دادو یادم نمیاد(اگه کصشرایی که با پول پخش کردن ترند میکننو سوپر هیت حساب نکنیم)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/83753" target="_blank">📅 02:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83752">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بهداد اقبالی زنتو گاییدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/83752" target="_blank">📅 00:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83747">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJOFT_idhE_f9EF8lZqjUMEQEGOOAItoKhMwMiSyy0axnhykv9tKLMwJN0H2PLwjkE-HPVEWVk_5zJ1bGeJ057WSu9BqMaTmDia_WBtnmcElDw61DMcpXXU4exvtPyIk4xO5HJR8xKRP3yVlb_Drw7ZEVi0i8Faeut720N2NvvEI5izWYw_Uz1Ioik6IUcnROGklDM2GbvohK6zoyl2_2B7q2lmkUm5eP9o80-mecT9aE7bTSOTNQ21TBi8psURlzsx83Nh83AKb7R8k7gwOJAlob44-dGdtgrfOOfMUCUiWmFQ3rUnBKPOS2-gQQ7E-Vlkq86-d8HKAUCsqdxOPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیویی هوش‌مصنوعی‌ای که آرتا الان و نیم‌ساعت قبل از کنسرتش تو عمان، از هلیا و پوتک تو اکانت اینستاگرامش پست کرده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/funhiphop/83747" target="_blank">📅 22:53 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
